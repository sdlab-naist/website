---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Papon presented his research at The 48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024)"
subtitle: ""
summary: ""
authors: ["papon-choonhaklai"]
tags: ["Time-Slicing GPU", "MLOps", "Distributed training"]
categories: []
date: 2024-07-03T22:29:12+09:00
lastmod: 2024-07-03T22:29:12+09:00
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

Mr. Papon Choonhaklai, a first-year master's student at SDLab presented the following paper at the [48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024)](https://ieeecompsac.computer.org/2024/program/)

<!--more-->

> Papon Choonhaklai, Kohei Ichikawa, Hajimu Iida, "An Evaluation of Time-Sliced GPU Sharing with KubeRay for Machine Learning Workloads", 48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024), July. 2024.

In this paper, the authors evaluated an alternative GPU sharing methodology using KubeRay and time slicing to enhance GPU utilization for machine learning workloads in Kubernetes environments. The study demonstrated that this method improved memory efficiency and allowed for more efficient GPU sharing among multiple concurrent workloads. However, the approach resulted in longer task completion times, particularly with parallel workloads, due to the overhead of managing distributed tasks. The study highlights the trade-off between improved GPU resource utilization and increased execution times, providing insights into optimizing GPU sharing in distributed machine learning environments​.
