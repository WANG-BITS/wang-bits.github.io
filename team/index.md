---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

Below are our PI, Dr. Wang, and our current team members.

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}

{% include list.html data="members" component="portrait" filter="role != 'pi'" %}



{% include section.html background="images/background.jpg" dark=true %}

We also thank our former members, collaborators, and well-wishers for their continuous help, support, and contributions.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/team_mxwbio.jpg" %}
{% include figure.html image="images/team_rpi_collaborators.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
