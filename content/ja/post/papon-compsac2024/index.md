---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "パポン氏が第 48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024) で研究を発表しました"
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

SDLabの修士1年生である　パポン・チューハクライ　氏が、[48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024)](https://ieeecompsac.computer.org/2024/program/) にて以下の論文を発表しました。


> Papon Choonhaklai, Kohei Ichikawa, Hajimu Iida, "An Evaluation of Time-Sliced GPU Sharing with KubeRay for Machine Learning Workloads," 48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024), pp. 1456-1459, July. 2024. [doi: 10.1109/COMPSAC61105.2024.00194.](https://ieeexplore.ieee.org/document/10633645)

本論文では、著者らはKubernetes環境における機械学習ワークロードのGPU利用率を向上させるために、KubeRayとタイムスライスを用いた代替のGPU共有手法を評価しました。研究の結果、この方法はメモリ効率を改善し、複数の同時実行ワークロード間でより効率的なGPU共有を可能にすることが示されました。しかしながら、このアプローチは分散タスクの管理オーバーヘッドにより、特に並列ワークロードにおいてタスク完了時間が長くなる結果となりました。この研究は、GPUリソースの利用率向上と実行時間の増加との間のトレードオフを明らかにし、分散機械学習環境におけるGPU共有の最適化に関する洞察を提供しています。