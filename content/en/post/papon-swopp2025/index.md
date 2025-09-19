---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Papon Choonhaklai presented his research at SWoPP 2025"
subtitle: ""
summary: ""
authors: ["kohei-ichikawa", "papon-choonhaklai"]
tags: ["Kubernetes", "GPU Sharing", "Multi-Process Service (MPS)"]
categories: []
date: 2025-09-12T16:38:08+09:00
lastmod: 2025-09-12T16:38:08+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
Mr. Papon Choonhaklai from our laboratory presented the following paper at [Summer United Workshops on Parallel, Distributed and Cooperative Processing (SWoPP 2025)](https://sites.google.com/site/swoppweb/), held in Japan from August 4 to 6, 2025:

> Papon Choonhaklai, Kohei Ichikawa, Hajimu Iida: A Metric-Driven Kubernetes Operator for Dynamic MPS-Based GPU Sharing in Inference Workloads, In Proceedings of SWoPP 2025, Aug. 2025.

SWoPP is a domestic conference that brings together multiple workshops in the field of parallel, distributed, and cooperative processing.

In this study, we proposed a metric-driven Kubernetes operator that enables efficient GPU sharing using NVIDIA’s Multi-Process Service (MPS). Unlike conventional methods relying on static partitions or custom resource definitions (CRDs), our operator leverages runtime metrics collected from the DCGM exporter to dynamically schedule inference workloads.

Empirical evaluation on LLM inference workloads demonstrated that our approach achieved 89% GPU utilization, 60% memory utilization, the highest throughput (8.4 req/s), and the lowest average response time (34,183 ms), significantly outperforming NVIDIA time-slicing and standalone NOS methods
