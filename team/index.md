---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include section.html %}

## Principal Investigator

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

## Current members

{% include list.html data="members" component="portrait" filter="group == 'current' && role != 'principal-investigator'" %}

## Alumni

{% include list.html data="members" component="portrait" filter="group == 'alumni'" style="small" %}

{% include section.html background="images/background.jpg" dark=true %}

We also thank our collaborators and well-wishers for their continuous help, support, and contributions.

{% include section.html %}

{% include figure.html image="images/team_mxwbio.jpg" %}
