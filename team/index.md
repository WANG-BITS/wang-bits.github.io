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

{% include section.html %}

## Collaborators

We are grateful to our collaborators for their contributions to our work:

- **[Dr. Mohammed A. Mostajo-Radji](https://mostajo-radji.com/)**, University of California, Santa Cruz, and the [Braingeneers](https://braingeneers.ucsc.edu/) group: brain organoids and high-density microelectrode array recordings, in our generative modeling and synthetic biological intelligence work.
- **[Cortical Labs](https://corticallabs.com/)**, Melbourne, Australia, including Dr. Brett J. Kagan: synthetic biological intelligence and the DishBrain system, in our work on starting an SBI lab and on NeuroAI.
- **[Dr. Christopher Puleo](https://faculty.rpi.edu/christopher-puleo)**, Rensselaer Polytechnic Institute, and **Dr. Karthikeyan Narayanan**, Director of the [CBIS Stem Cell Research Core](https://biotech.rpi.edu/core-facilities/stem-cell-research): building our synthetic biological intelligence lab and HD-MEA recording.
- **Dr. Sergey Pryshchep**, Director of the CBIS [Cell & Molecular Biology](https://biotech.rpi.edu/core-facilities/cell-and-molecular-biology) and [Microscopy & Cellular Imaging](https://biotech.rpi.edu/core-facilities/microscopy) Cores: wet-lab training and imaging for our neural culture work.

We also thank [MaxWell Biosystems](https://www.mxwbio.com/) for demonstrating their high-density microelectrode array platform at RPI.

{% include figure.html image="images/team_mxwbio.jpg" caption="An HD-MEA demonstration with MaxWell Biosystems at RPI." %}
