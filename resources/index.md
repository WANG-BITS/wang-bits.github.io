---
title: Resources
nav:
  order: 4
  tooltip: Code, data, equipment, and facilities
---

# {% include icon.html icon="fa-solid fa-flask" %}Resources

Wang-BITS lab is part of the Biomedical Imaging Center at Rensselaer Polytechnic Institute, housed in the Center for Biotechnology and Interdisciplinary Studies (CBIS). Here we share our code and the datasets we use. Our work also draws on our own electrophysiology equipment, CBIS core facilities for cell culture and imaging, and the Center's GPU servers and RPI's supercomputing resources for modeling.

{% include figure.html image="images/resources/cbis.jpg" caption="The Center for Biotechnology and Interdisciplinary Studies (CBIS) at Rensselaer Polytechnic Institute." %}

{% include section.html %}

## Code & data

### {% include icon.html icon="fa-brands fa-github" %}Code

- **[Organoid-Binary-Spike-Spatiotemporal-Data-Modeling](https://github.com/tanveerderik/Organoid-Binary-Spike-Spatiotemporal-Data-Modeling).** A hierarchical vector-quantized autoencoder and factorized generative prior for ultra-sparse spiking activity on high-density microelectrode arrays, including training stages and the full evaluation harness. Accompanies [our preprint](https://arxiv.org/abs/2609.23907).

### {% include icon.html icon="fa-solid fa-database" %}Datasets we use

Our generative modeling uses publicly released high-density microelectrode array recordings from our collaborators' labs:

- **[Extracellular recordings from human brain organoids using high-density CMOS arrays](https://doi.org/10.25349/D9031Z)** (Dryad). Recordings of human brain organoids, from Sharf et al. and the Kosik Lab, UC Santa Barbara.
- **[Multimodal evaluation of network activity and optogenetic interventions in human hippocampal slices](https://dandiarchive.org/dandiset/001132)** (DANDI Archive, dandiset 001132). Recordings of acute human hippocampal slices, from Andrews et al. (2024).

{% include section.html %}

## Lab equipment

### {% include icon.html icon="fa-solid fa-microchip" %}Multielectrode array system

{% include figure.html image="images/resources/mea2100.jpg" caption="MEA2100 multielectrode array system." width="60%" %}

An MEA2100 system (Multi Channel Systems) records electrical activity from cultured neurons and delivers stimulation to them. It includes a headstage, signal interface, and temperature controller, multiple 60-electrode MEA wells for neural culture, and synthetic signal generators for calibration and stimulation.

### {% include icon.html icon="fa-solid fa-bolt" %}X-ray electrophysiological stimulation platform

A platform originally built to combine x-ray stimulation with optogenetics, developed in Dr. Wang's earlier work on x-ray optogenetics ([Berry et al., _Photonics_ 2015](https://doi.org/10.3390/photonics2010023)), and now repurposed for NeuroAI research. It combines a microfocus x-ray source with a collimator and a PC-controlled solenoid shutter to deliver pencil-beam x-ray pulses, a visible light source, a Faraday cage, platinum electrodes with a differential amplifier, and a PowerLab unit (ADInstruments) that coordinates the system.

### {% include icon.html icon="fa-solid fa-magnifying-glass" %}Patch-clamp setup

A patch-clamp electrophysiology rig with an Olympus differential interference contrast (DIC) microscope, perfusion system, motorized micromanipulator, Axopatch 200B amplifier, and Axon DigiData A/D converter. Together with the x-ray and visible light sources, it measures single-cell and single-channel responses to light and x-ray pulses. It was built in collaboration with Prof. Jian Kang (University of California, Irvine).

{% include section.html %}

## Shared facilities

Our wet-lab work uses CBIS core facilities, which provide equipment, training, and support.

- **Cell & Molecular Biology Core.** A BSL-2+ tissue and cell culture facility with CO<sub>2</sub> incubators, environmental rooms, centrifuges, and an inverted microscope, plus real-time PCR and fluorescence and bioluminescence imaging.
- **Stem Cell Research Core.** A fully equipped aseptic cell culture facility with biosafety cabinets, CO<sub>2</sub>/O<sub>2</sub>-controlled incubators, automated liquid handling, high-content and time-lapse imaging, dissecting and inverted microscopes, cryo storage, and a 3D bioprinter.
- **Microscopy Core.** Brightfield, phase-contrast, widefield fluorescence, confocal (Zeiss LSM 510 META), and super-resolution STED (Leica TCS SP8) microscopy, laser dissection, and atomic force microscopy, with training and sample-preparation support.

{% include figure.html image="images/resources/microscopy-core.jpg" caption="An inverted fluorescence microscope in the CBIS Microscopy Core." width="40%" %}

{% include section.html %}

## Computing

- **Biomedical Imaging Center GPU servers.** Dedicated deep-learning servers with ten NVIDIA H100, five RTX A5000, two TITAN RTX, two TITAN Xp, and eight GTX 1080 Ti GPUs, up to 1 TB of RAM per workstation, and 117 TB of shared storage.
- **Center for Computational Innovations (CCI).** RPI's high-performance computing center, including AiMOS, an eight-petaflop IBM POWER9 supercomputer designed for AI, and the NPL cluster of NVIDIA V100 GPUs.

{% include figure.html image="images/resources/aimos.jpg" caption="The AiMOS supercomputer at RPI's Center for Computational Innovations." width="60%" %}
