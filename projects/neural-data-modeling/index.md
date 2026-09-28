---
title: Generative models of neural activity
---

# Generative models of neural activity

_Neural data modeling on high-density microelectrode arrays_ · **Status:** ongoing

{% include section.html %}

## Overview

High-density CMOS microelectrode arrays (HD-MEAs) record extracellular activity from lab-grown neural tissue across tens of thousands of electrode sites at millisecond resolution. That makes them a natural readout for synthetic biological intelligence and organoid research, but the data are unusual for machine learning: activity is extremely sparse (most electrode-time bins are empty), only a subset of electrodes is routed in any recording, and that subset changes from one recording to the next.

Summary statistics such as firing rates, burst counts, and interspike intervals are useful for quality control, but they are not a generative description of the network's state. Two recordings can have similar spike counts while differing in which sites participate, in what order, and whether activity spreads across the network.

## Approach

We treat the electrode array as a fixed spatial canvas and learn a discrete vocabulary of spatiotemporal activity motifs:

- **A sparse tokenizer.** Recordings are split into small spatiotemporal patches. Empty patches get a dedicated blank token, and active patches are encoded by a residual vector-quantized autoencoder into a shared alphabet of motifs.
- **A factorized generative prior.** A masked transformer first predicts _where_ activity occurs, then _which_ motif appears at each active location, mirroring the structure of the data.
- **Shared across preparations.** The model is trained on HD-MEA recordings from human brain organoids and acute human hippocampal tissue from our collaborators, recorded on the same platform, so a single vocabulary covers both.

The learned motifs are broadly reused: recording identity explains only a small fraction of which motifs are used, and motif overlap between organoids and tissue slices is comparable to overlap within each.

{%
  include figure.html
  image="images/projects/figures/tokenizer-reconstruction.png"
  caption="Reconstructing activity from motif tokens, for two brain-organoid recordings (A, B) and two ex vivo hippocampal recordings (C, D). Blue marks correctly reconstructed spikes, red missed spikes, and yellow spurious ones; the right column is each recording's site map. The bottom row compares summary statistics of real and reconstructed clips across the test set. From Tanveer et al., arXiv:2609.23907."
%}

The same model can generate activity as well as reconstruct it. Given nothing, it generates an entire clip; given part of a clip, it completes the rest, whether that means predicting later frames from earlier ones, filling a gap in time, or filling in a region of the array.

{%
  include figure.html
  image="images/projects/figures/generation-and-completion.png"
  caption="One recorded clip under four tasks: free generation with nothing observed (R), causal completion of later frames (C), non-causal completion of a gap in time (N), and spatial completion of part of the array (S). Gray panels are observed and black panels are generated. From Tanveer et al., arXiv:2609.23907."
%}

## What's next

- **Better temporal prediction.** The motif vocabulary preserves more timing information than the current prior recovers, so we are developing causal sequence priors and event-time objectives that predict upcoming activity more accurately.
- **Conditioning on measured variables.** Replacing per-recording identity with descriptors of the preparation and the recording, so the model can transfer to recordings it has never seen.
- **Longer term.** A model that predicts future activity under given conditions is the forward model that closed-loop training of living neural networks would need, and a baseline for measuring how networks respond to stimulation or disease.

{% include section.html %}

## Related publications

{% include citation.html lookup="arxiv:2609.23907" style="rich" %}

## People

{% include portrait.html lookup="ms-tanveer" %}
{% include portrait.html lookup="ge-wang" %}
