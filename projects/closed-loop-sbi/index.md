---
title: Toward closed-loop synthetic biological intelligence
---

# Toward closed-loop synthetic biological intelligence

_Forward models for controlling living neural networks_ · **Status:** ongoing

{% include section.html %}

## Overview

In synthetic biological intelligence (SBI), a living neural network is trained on a goal-directed task through a closed loop: the state of a task is encoded as electrical stimulation, the network's response is recorded and decoded, and a controller chooses the next stimulus. Closed-loop learning in cultured neurons has been demonstrated, for example in a Pong-like game, but the controllers involved rely on simple readouts of the network.

Every interaction with living tissue is expensive: cultures take weeks to mature, change as they age, and vary from chip to chip. A learned model that predicts how a network will respond would let much of a controller's development happen in silico, before it is used on the living preparation.

## Approach

We are building on our [generative models of neural activity](../neural-data-modeling/) toward a **forward model**: one that predicts upcoming activity from recent activity and measured experimental conditions. Such a model is the component that the main approaches to controlling biological neural networks require.

{%
  include figure.html
  image="images/projects/figures/model-based-rl.png"
  caption="Model-based reinforcement learning for a biohybrid system. A learned model of the environment, here the neural network, supports planning and policy updates without every interaction taking place on living tissue."
%}

{%
  include figure.html
  image="images/projects/figures/active-inference.png"
  caption="Active inference. Candidate actions are evaluated by expected free energy, which requires a generative model that predicts observations under intervention."
  width="70%"
%}

- **Reinforcement learning:** the forward model serves as the learned environment model used for planning and experience replay.
- **Active inference:** the same model supplies the predictions that candidate stimulation strategies are scored against.
- **Digital twins:** more broadly, the model forms the electrophysiology component of a digital twin of the culture, updated from data and used to predict the effect of an intervention (see [Neural function under stimulation and disease](../stimulation-and-disease/)).

## What's next

This project is at an early stage. Our immediate steps are to make the forward model accurate over short time horizons and to condition it on measured experimental variables. We will then evaluate whether it can predict stimulus-evoked responses, and ultimately whether a controller pretrained against it needs fewer interactions with living tissue than one trained from scratch.

{% include section.html %}

## Related publications

{% include citation.html lookup="arxiv:2509.23896" style="rich" %}
{% include citation.html lookup="doi:10.1016/j.patter.2025.101232" style="rich" %}

## People

{% include portrait.html lookup="ms-tanveer" %}
{% include portrait.html lookup="dhruvik-patel" %}
{% include portrait.html lookup="ge-wang" %}
