---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Empirical Dynamic Modelingの最適化・並列化"
summary: ""
authors: ["keichi-takahashi"]
tags: ["HPC"]
categories: []
date: 2020-04-27T17:20:29+09:00

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

[Empirical Dynamic Modeling (EDM)](https://deepeco.ucsd.edu/nonlinear-dynamics-research/edm/) は，
[Takensの埋め込み定理](https://doi.org/10.3156/jfuzzy.10.4_82)に基づく非線形時系列解析手法です．
EDMは，力学系の状態変数の予測，非線形性の評価，変数間の因果分析等を可能にする手法であり，生態学や神経科学などの分野で主に用いられています．
しかし，従来EDMはその計算量の大きさから，小規模なデータに適用が限られていました．

本研究では，最適化および並列化技術を活用し，既存のEDM実装であるpyEDMやrEDMより高速なEDM実装を開発しています．
また，計算基盤として産業総合技術研究所が有する国内最大規模の高性能計算機
[AI Bridging Cloud Infrastructure (ABCI)](https://abci.ai/ja/)
を用い，1,000 CPU・2,000 GPU以上を活用した，前例にない規模のEDM計算の実現を目指します．

本研究は，[産業総合技術研究所](https://www.aist.go.jp/)，
米国[Salk研究所](https://www.salk.edu/)，
米国[Scripps海洋研究所](https://scripps.ucsd.edu/)
との連携・協力の下，推進しています．

## 関連論文

1. Wassapon Watanakeesuntorn, Keichi Takahashi, Kohei Ichikawa, Joseph Park,
   George Sugihara, Ryousei Takano, Jason Haga, Gerald M. Pao, "Massively
   Parallel Causal Inference of Whole Brain Dynamics at Single Neuron
   Resolution", 26th International Conference on Parallel and Distributed
   Systems (ICPADS 2020), Dec. 2020.

{{< youtube fevurdpiRYg >}}
