---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "SDNを応用した動的な相互結合網制御"
summary: ""
authors: ["keichi-takahashi"]
tags: ["HPC", "SDN"]
categories: []
date: 2020-04-27T17:18:44+09:00

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

高性能計算機の多くは，複数の計算機を相互結合網と呼ばれるネットワークを介して相互接続したクラスタアーキテクチャを採用しています．クラスタでは，計算機間の通信性能がアプリケーションの計算性能を大きく左右します． しかし，多数の計算機が同時多発的に通信すると，相互結合網の一部にトラフィックが集中し，通信性能の劣化を招いてしまう問題が知られています．本研究では，ネットワークをソフトウェアのように動的に制御可能にするSoftware-Defined Networking (SDN) 技術を応用し，高性能計算機上で実行されるアプリケーションの通信パターンを考慮して相互結合網網内のトラフィックを動的に制御し，トラフィックの集中を緩和する技術の研究開発に取り組んでいます．
