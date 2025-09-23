---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Papon君がSWoPP2025で発表しました"
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
当研究室の Papon Choonhaklai 君 が、2025年8月4日から6日に日本で開催された [Summer United Workshops on Parallel, Distributed and Cooperative Processing (SWoPP 2025)](https://sites.google.com/site/swoppweb/) において、以下の論文を発表しました：

> Papon Choonhaklai, Kohei Ichikawa, Hajimu Iida: A Metric-Driven Kubernetes Operator for Dynamic MPS-Based GPU Sharing in Inference Workloads, IPSJ SIG Technical Report, Vol. 2025-HPC-200, No. 23, pp. 1-8, Jul. 2025.

SWoPP は、並列・分散・協調処理分野における複数のワークショップを集めた国内会議です。

本研究では、NVIDIA の Multi-Process Service (MPS) を用いた効率的な GPU 共有を可能にする メトリクス駆動型 Kubernetes オペレーター を提案しました。従来の静的パーティションや CRD (Custom Resource Definition) に依存する方式とは異なり、本手法は DCGM Exporter により収集された実行時メトリクス を活用して推論ワークロードを動的にスケジューリングします。

大規模言語モデル (LLM) の推論ワークロードを対象とした実験評価の結果、本手法は GPU 利用率 89%、メモリ利用率 60%、スループット 8.4 req/s、平均応答時間 34,183 ms を達成し、NVIDIA の Time-Slicing や単独の NOS 手法と比較して大幅に優れた性能を示しました。
