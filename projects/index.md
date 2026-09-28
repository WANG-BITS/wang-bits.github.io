---
title: Projects
nav:
  order: 2
  tooltip: Ongoing and past projects
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

Our projects span computational modeling of neural recordings, using publicly released data from our collaborators' labs, and building the experimental side of synthetic biological intelligence. Select a project to read more about it.

{% include search-info.html %}

{% include section.html %}

## Ongoing projects

{% include list.html component="card" data="projects" filter="group == 'ongoing'" %}

{% assign past = site.data.projects | where: "group", "past" %}
{% if past.size > 0 %}

{% include section.html %}

## Past projects

{% include list.html component="card" data="projects" filter="group == 'past'" %}

{% endif %}
