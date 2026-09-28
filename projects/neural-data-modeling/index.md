---
title: Generative models of neural activity
---

# Generative models of neural activity

_Neural data modeling on high-density microelectrode arrays_ · **Status:** ongoing

{% include section.html %}

## Overview

High-density CMOS microelectrode arrays (HD-MEAs) record extracellular activity from lab-grown neural tissue across tens of thousands of electrode sites at millisecond resolution. That makes them a natural readout for synthetic biological intelligence, but the data are unusual for machine learning: activity is extremely sparse (most electrode-time bins are empty), only a subset of electrodes is routed in any recording, and that subset changes from one recording to the next.

Summary statistics such as firing rates, burst counts, and interspike intervals are useful for quality control, but they are not a generative description of the network's state. Two recordings can have similar spike counts while differing in which sites participate, in what order, and whether activity spreads across the network.

{%
  include figure.html
  image="images/projects/figures/hdmea-recording.jpg"
  caption="An HD-MEA recording from a cultured neural network: culture images, firing-rate and spike-amplitude maps, interspike intervals, raster activity, and network-burst statistics."
  width="75%"
%}

## Approach

We treat the electrode array as a fixed spatial canvas and learn a discrete vocabulary of spatiotemporal activity motifs:

- **A sparse tokenizer.** Recordings are split into small spatiotemporal patches. Empty patches get a dedicated blank token, and active patches are encoded by a residual vector-quantized autoencoder into a shared alphabet of motifs.
- **A factorized generative prior.** A masked transformer first predicts _where_ activity occurs, then _which_ motif appears at each active location, mirroring the structure of the data.
- **Shared across preparations.** The model is trained on open-access HD-MEA recordings from human brain organoids and acute human hippocampal tissue, recorded on the same platform, so a single vocabulary covers both.

{%
  include figure.html
  image="images/projects/figures/motif-vocabulary.png"
  caption="The most frequently used motifs, and evidence that the vocabulary is reused across recordings and across organoid and tissue-slice preparations."
%}

The learned motifs are broadly reused: recording identity explains only a small fraction of which motifs are used, and motif overlap between organoids and tissue slices is comparable to overlap within each. The model supports masked completion and free generation of array-wide activity.

## What's next

- **Better temporal prediction.** The motif vocabulary preserves more timing information than the current prior recovers, so we are developing causal sequence priors and event-time objectives that predict upcoming activity more accurately.
- **Conditioning on measured variables.** Replacing per-recording identity with descriptors of the preparation and the recording, so the model can transfer to recordings it has never seen.
- **Toward control.** A model that predicts future activity is the forward model a closed-loop controller needs; see [Toward closed-loop synthetic biological intelligence](../closed-loop-sbi/).

{% include section.html %}

## Related publications

{% include citation.html lookup="arxiv:2609.23907" style="rich" %}

## People

{% include portrait.html lookup="ms-tanveer" %}
{% include portrait.html lookup="ge-wang" %}
