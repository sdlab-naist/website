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
[Takensの埋め込み定理](https://doi.org/10.3156/jfuzzy.10.4_82)を応用した非線形時系列解析手法です．
EDMは，力学系の状態変数の予測，非線形性の評価，状態変数間の因果分析等に用いることが可能な手法であり，生態学や神経科学などの分野で活用されています．
しかし，これまでEDMはその計算量の大きさから，小規模なデータに適用が限られていました．
本研究では，高性能計算技術を活用し，既存のEDM実装であるpyEDMやrEDMより高速に大規模なデータを解析可能にするEDM実装を開発しています．
本研究は，米国Scripps海洋研究所およびSalk研究所との連携・協力の下，推進しています．
