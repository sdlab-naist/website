---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "In-situワークフローに関する研究"
summary: ""
authors: ["keichi-takahashi"]
tags: ["HPC"]
categories: []
date: 2020-04-27T17:18:52+09:00

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

## 概要

高性能計算機の演算性能は急速に拡大しているにも関わらず，ストレージの帯域幅や容量の性能向上は演算性能の向上に追従できていません．ストレージボトルネックに対する解決方法の1つとして注目を集めているのが，In-situ可視化・解析技術です．In-situ可視化・解析は，シミュレーションからの出力結果をストレージを経由することなく，リアルタイムに可視化・解析することにより，ストレージボトルネックを回避します．本研究では，In-situワークフローを構成するアプリケーションへの資源配分最適化や，異種アーキテクチャの高性能計算機を跨ぐIn-situワークフローの実現に取り組んでいます．

## 関連論文

1. Kshitij Mehta, Bryce Allen, Matthew Wolf, Jeremy Logan, Eric Suchyta, Jong
   Choi, Keichi Takahashi, Igor Yakushin, Todd Munson, Ian Foster, Scott
   Klasky, "A Codesign Framework for Online Data Analysis and Reduction",
   Workflows in Support of Large-Scale Science (WORKS 2019), Nov. 2019.
2. 堤誠司, 藤田直行, 伊藤浩之, 大日向大地, 井上敬介, 松村洋祐, 高橋慧智, Greg
   Eisenhauer, Norbert Podhorszki, Scott Klasky, "In Situ/In Transitアプローチ
   を用いた大規模数値解析におけるポスト処理効率化", 第33回数値流体力学シンポジ
   ウム, Nov. 2019.
