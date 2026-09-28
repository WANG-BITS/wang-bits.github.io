---
title: Building a synthetic biological intelligence lab
---

# Building a synthetic biological intelligence lab

_Neural culture and microelectrode-array recording_ · **Status:** paused

{% include section.html %}

## Overview

Synthetic biological intelligence (SBI) needs expertise that rarely sits in one lab: tissue engineering, cell culture, electrophysiology, signal processing, programming, and AI. Most groups specialize in either the biological or the computational side, so starting SBI research is slow and costly.

As a computational lab, we set out to build the biological side ourselves: culturing neurons on microelectrode arrays, recording their activity, and preparing the infrastructure a closed-loop experiment would need. We documented the process, including what went wrong and how to avoid it, as a practical guide for other labs.

## What we did

- **Culture workflow.** Workspace preparation and sterilization, substrate coating, cell plating, media preparation and exchange, contamination control, viability monitoring, and maturation, drawing on both primary neural cultures and human iPSC-derived neurons.
- **Choosing an electrophysiology interface.** Comparing patch clamp, calcium and voltage imaging, passive MEAs, and high-density CMOS MEAs, which support repeated extracellular recording and stimulation over long periods.
- **Recording spontaneous activity.** Recording cultured networks on HD-MEA chips and characterizing firing rates, spike amplitudes, interspike intervals, and network bursts.
- **Planning for closed-loop experiments.** Specifying the real-time software interface that closing the loop between recording, a task, and stimulation would require.

{%
  include figure.html
  image="images/projects/figures/hdmea-recording.jpg"
  caption="An HD-MEA recording from a cultured neural network: culture images, firing-rate and spike-amplitude maps, interspike intervals, raster activity, and network-burst statistics. Adapted from Tanveer et al., _Patterns_ (2025)."
  width="75%"
%}

{%
  include figure.html
  image="images/projects/figures/culture-variability.jpg"
  caption="Neural cultures on microelectrode arrays (top) and the development of spiking, bursting, and network-burst activity over days in vitro across six chips (bottom). Cultures prepared the same way can behave very differently. Adapted from Tanveer et al., _Patterns_ (2025)."
  width="75%"
%}

These recordings also showed us the limits of summary statistics, which motivated our ongoing work on [generative models of neural activity](../neural-data-modeling/).

## Status

This work is currently paused. We plan to resume it in the future, with the goal of running closed-loop experiments in which cultured networks are trained on tasks.

{% include section.html %}

## Related publications

{% include citation.html lookup="doi:10.1016/j.patter.2025.101232" style="rich" %}

## People

{% include portrait.html lookup="ms-tanveer" %}
{% include portrait.html lookup="dhruvik-patel" %}
{% include portrait.html lookup="ge-wang" %}
