---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software for High Performance Computing"
summary: ""
authors: ["keichi-takahashi"]
tags: ["HPC"]
categories: []
date: 2020-02-18T22:13:48+09:00

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

PC上では不可能な規模の計算を実現する高性能計算機（スーパコンピュータ）は，天気予報のように身近なところから，ビッグデータ解析や人工知能の研究開発に至るまで，幅広い領域において利活用されています．本研究では，数値計算，システムソフトウェア，ハードウェア等，異なる階層の計算機技術を垂直的に統合し，高性能計算機の性能を最大限に引き出すアプリケーションおよびミドルウェアを設計・開発しています．

## 取り組んでいる研究テーマ

### SDNを応用した動的な相互結合網制御

高性能計算機の多くは，複数の計算機を相互結合網と呼ばれるネットワークを介して相互接続したクラスタアーキテクチャを採用しています．クラスタでは，計算機間の通信性能がアプリケーションの計算性能を大きく左右します． しかし，多数の計算機が同時多発的に通信すると，相互結合網の一部にトラフィックが集中し，通信性能の劣化を招いてしまう問題が知られています．本研究では，ネットワークをソフトウェアのように動的に制御可能にするSoftware-Defined Networking (SDN) 技術を応用し，高性能計算機上で実行されるアプリケーションの通信パターンを考慮して相互結合網網内のトラフィックを動的に制御し，トラフィックの集中を緩和する技術の研究開発に取り組んでいます．
詳しくは[こちら](/project/sdn-mpi)．

### In-situワークフローに関する研究

高性能計算機の演算性能は急速に拡大しているにも関わらず，ストレージの帯域幅や容量の性能向上は演算性能の向上に追従できていません．ストレージボトルネックに対する解決方法の1つとして注目を集めているのが，In-situ可視化・解析技術です．In-situ可視化・解析は，シミュレーションからの出力結果をストレージを経由することなく，リアルタイムに可視化・解析することにより，ストレージボトルネックを回避します．本研究では，In-situワークフローを構成するアプリケーションへの資源配分最適化や，異種アーキテクチャの高性能計算機を跨ぐIn-situワークフローの実現に取り組んでいます．
詳しくは[こちら](/project/in-situ-workflows)．

### Empirical Dynamic Modelingの最適化・並列化

[Empirical Dynamic Modeling (EDM)](https://deepeco.ucsd.edu/nonlinear-dynamics-research/edm/) は，
[Takensの埋め込み定理](https://doi.org/10.3156/jfuzzy.10.4_82)を応用した非線形時系列解析手法です．
EDMは，力学系の状態変数の予測，非線形性の評価，状態変数間の因果分析等に用いることが可能な手法であり，生態学や神経科学などの分野で活用されています．
しかし，これまでEDMはその計算量の大きさから，小規模なデータに適用が限られていました．
本研究では，高性能計算技術を活用し，既存のEDM実装であるpyEDMやrEDMより高速に大規模なデータを解析可能にするEDM実装を開発しています．
詳しくは[こちら](/project/optimization-of-edm)．
