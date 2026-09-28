
# Wang-BITS Lab Website

Website of the Bioengineered Intelligence Theory and Systems (BITS) Lab at Rensselaer Polytechnic Institute, led by Dr. Ge Wang.

Visit **[wang-bits.github.io](https://wang-bits.github.io)**

## Updating the site

- **Members:** one file per person in `_members/`. Set `group: current` or `group: alumni`.
- **Projects:** cards in `_data/projects.yaml` (`group: ongoing` or `past`), with a page per project in `projects/<name>/index.md`.
- **Publications:** found automatically from OpenAlex for the authors and topic keywords in `_data/openalex.yaml`. Add descriptions, images, tags, and buttons, or add and hide papers, in `_data/sources.yaml`. Regenerate with `python _cite/cite.py`.
- **Resources:** code, datasets, equipment, and facilities in `resources/index.md`.

_Built with [Lab Website Template](https://greene-lab.gitbook.io/lab-website-template-docs)_
