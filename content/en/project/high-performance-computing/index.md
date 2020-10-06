---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software for High Performance Computing"
summary: ""
authors: ["keichi-takahashi"]
tags: ["HPC"]
categories: []
date: 2020-02-18T22:13:48+09:00
weight: -60

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

## Overview

High-Performance Computing Systems (i.e., Supercomputers) provide massive
computing performance to solve diverse problems in science and engineering. At
our laboratory, we research and develop software to fully utilize the
performance of state-of-the-art HPC systems. We develop massively parallel
scientific applications in close collaboration with domain scientists.
Furthermore, we design and implement middleware for large-scale HPC systems.

## Research Topics

### Dynamic Interconnect Control using SDN

Modern HPC systems are based on the cluster architecture where multiple
computers are connected through a high-performance network
(i.e., interconnect). In a cluster, the total performance of applications
heavily relies on the communication performance over the interconnect. However,
it is known that hotspots occur in the interconnect and degrade the
communication performance when many computers communicate simultaneously. We
apply _Software-Defined Networking (SDN)_, a network paradigm that allows one
to dynamically manage the network as a software resource, to control the
traffic in the interconnect and mitigate hotspots by considering the
communication patterns of applications. Please see [here](/project/sdn-mpi)
for details．

### Research on In-situ Scientific Workflows

The gap between the computational performance and the storage performance
(bandwidth, capacity, etc.) in HPC systems is rapidly widening. One of the
approaches to tackle the storage bottleneck problem is _in-situ visualization
and analysis_. In an in-situ workflow, the output from the simulations is
directly sent over to visualization and analysis applications without going
through the parallel filesystem. We are working on optimizing the resource
allocation in in-situ workflows and realizing workflows that span across
multiple heterogeneous HPC systems.
Please see [here](/project/in-situ-workflows) for details．

### Optimization and Parallelization of Empirical Dynamic Modeling

_[Empirical Dynamic Modeling (EDM)](https://deepeco.ucsd.edu/nonlinear-dynamics-research/edm/)_
is a nonlinear time series analysis framework based on the
_[Takens' Embedding Theorem](https://www.worldscientific.com/doi/abs/10.1142/s0218127491000634)_ on state space reconstruction.
EDM is used for predicting the behavior of dynamical system, evaluating the
nonlinearity of a system and finding the causal relationships between
variables in diverse fields including ecology, sociology and neuroscience.
Despite its wide applicability, EDM has traditionally been applied to
relatively small datasets only because of its high computational cost. We are
developing an implementation of EDM targeted for modern GPU-centric HPC
systems to allow processing large-scale datasets.
Please see [here](/project/optimization-of-edm) for details.
