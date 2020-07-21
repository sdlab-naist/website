---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Thonglek君のIJCNN2020での研究発表"
subtitle: ""
summary: ""
authors: ["kundjanasith-thonglek"]
tags: []
categories: []
date: 2020-07-20T13:25:56+09:00
lastmod: 2020-07-20T13:25:56+09:00
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

当研究室M2のKundjanasith Thonglek君が，下記の論文をIEEE Word Congress on Computational Intelligence (WCCI) の国際会議 [International Joint Conference on Neural Networks (IJCNN)](https://wcci2020.org/ijcnn-2020-program/) にて発表しました．

> Kundjanasith Thonglek, Keichi Takahashi, Kohei Ichikawa, Chawanat Nakasan, Hidemoto Nakada, Ryousei Takano and Hajimu Iida, 
> "Retraining Quantized Neural Network Models with Unlabeled Data", International Joint Conference on Neural Networks (IJCNN 2020), Jul. 2020.

エッジデバイスは計算性能やストレージ容量が限られているため，クラウド向けに設計された大規模なニューラルネットワークをそのまま実行することができません．そのため，ニューラルネットワークの重みパラメータを量子化し，モデルのサイズを削減することにより，エッジデバイス上でモデルを実行可能にするモデル量子化が注目されています．

本論文では，量子化されたニューラルネットワークをラベル無しデータセットを用いて再訓練し，元のニューラルネットワークと遜色のない分類精度を実現する手法を提案しました．提案手法はラベル付きデータセットを必要としないため，プライバシやライセンスの問題によりラベル付きデータセットが入手できない状況において有用であると考えられます．

本研究は，産業総合技術研究所との共同研究です


