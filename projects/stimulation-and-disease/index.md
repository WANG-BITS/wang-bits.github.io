---
title: Neural function under stimulation and disease
---

# Neural function under stimulation and disease

_How in vitro neural networks respond to perturbation_ · **Status:** ongoing (exploratory)

{% include section.html %}

## Overview

Lab-grown neural networks let us measure directly how neural activity changes when a network is perturbed, whether by electrical, optical, or mechanical stimulation, by drugs, or by the cellular changes that come with disease. Human-derived cultures and brain organoids make it possible to study models of neurodegenerative diseases such as Alzheimer's and Parkinson's disease, and of neurodevelopmental disorders such as ADHD and autism spectrum disorder, in human cells.

The challenge is comparison. Cultures vary substantially from chip to chip and over time even under identical protocols, so separating the effect of an intervention from ordinary variability requires good models of what normal activity looks like.

{%
  include figure.html
  image="images/projects/figures/culture-variability.jpg"
  caption="Neural cultures on microelectrode arrays (top) and the development of spiking, bursting, and network-burst activity over days in vitro across six chips (bottom), showing how much activity varies between cultures prepared the same way."
  width="75%"
%}

## Approach

We are exploring how computational models of recorded activity can characterize and compare these conditions:

- **Baselines from spontaneous activity.** Generative models of spontaneous activity (see [Generative models of neural activity](../neural-data-modeling/)) provide a reference distribution against which stimulus-evoked or disease-related changes can be measured.
- **Stimulus-response modeling.** Conditioning those models on stimulation parameters such as site, current, and pulse width, to predict evoked activity and to test whether activity patterns shift systematically with intervention.
- **Digital twins.** In the longer term, models of electrophysiology are one component of a digital twin of the culture, alongside morphology, metabolism, and gene expression, which could support in silico drug screening and disease modeling.

{%
  include figure.html
  image="images/projects/figures/digital-twin.png"
  caption="A digital-twin framework for biological neural networks. Electrophysiological modeling is one component; others include morphology, metabolism, gene and biomarker expression, and disease and survivability modeling."
%}

## What's next

This is the most exploratory of our projects. Our first step is stimulus-response modeling on stimulation-labeled recordings; disease-model studies depend on data from collaborating labs and are a longer-term direction.

{% include section.html %}

## Related publications

{% include citation.html lookup="doi:10.1016/j.patter.2025.101232" style="rich" %}
{% include citation.html lookup="arxiv:2509.23896" style="rich" %}

## People

{% include portrait.html lookup="ms-tanveer" %}
{% include portrait.html lookup="dhruvik-patel" %}
{% include portrait.html lookup="ge-wang" %}
