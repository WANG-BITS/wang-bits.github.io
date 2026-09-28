import json
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from util import *


def main(entry):
    """
    receives single list entry from openalex data file
    returns list of sources to cite, keeping only works whose title or abstract
    mentions one of the entry's keywords
    """

    # openalex api
    endpoint = "https://api.openalex.org/works"

    # get author ids and filters from entry
    authors = get_safe(entry, "authors", [])
    if not authors:
        raise Exception('No "authors" key')
    keywords = [k.lower() for k in get_safe(entry, "keywords", [])]
    if not keywords:
        raise Exception('No "keywords" key')
    exclude = {normalize_id(e) for e in get_safe(entry, "exclude", [])}

    # query api, following cursor pagination
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(authors):
        works = []
        cursor = "*"
        while cursor:
            params = {
                "filter": "author.id:" + "|".join(authors),
                "select": "id,doi,title,type,publication_date,ids,abstract_inverted_index",
                "per-page": 200,
                "cursor": cursor,
            }
            request = Request(url=f"{endpoint}?{urlencode(params)}")
            response = json.loads(urlopen(request).read())
            works += get_safe(response, "results", [])
            cursor = get_safe(response, "meta.next_cursor", None)
        return works

    response = query(tuple(authors))

    # keep works matching any keyword
    matches = []
    for work in response:
        abstract = " ".join(get_safe(work, "abstract_inverted_index", {}) or {})
        text = f"{get_safe(work, 'title', '')} {abstract}".lower()
        if not any(keyword in text for keyword in keywords):
            continue

        _id = work_id(work)
        if not _id or _id in exclude:
            continue

        matches.append((work, _id))

    # when a preprint and its published version both match, keep the published one
    by_title = {}
    for work, _id in matches:
        key = re.sub(r"[^a-z0-9]", "", (get_safe(work, "title", "") or "").lower())
        kept = by_title.get(key)
        if kept is None or (
            get_safe(kept[0], "type", "") == "preprint"
            and get_safe(work, "type", "") != "preprint"
        ):
            by_title[key] = (work, _id)

    # list of sources to return
    return [{"id": _id} for _, _id in by_title.values()]


def work_id(work):
    """
    get id Manubot can cite, e.g. doi:10.1234/5678 or arxiv:2412.14112
    """
    doi = get_safe(work, "doi", "") or ""
    doi = doi.replace("https://doi.org/", "").lower()
    arxiv = re.match(r"10\.48550/arxiv\.(.+)", doi)
    if arxiv:
        return f"arxiv:{arxiv.group(1)}"
    if doi:
        return f"doi:{doi}"
    return None


def normalize_id(_id):
    """
    normalize user-entered id to match work_id output
    """
    _id = _id.strip()
    prefix, _, value = _id.partition(":")
    return f"{prefix.lower()}:{value.lower()}"
