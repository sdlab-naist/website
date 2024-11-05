---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "森川君がSCAM2024で発表しました"
subtitle: ""
summary: ""
authors: ["Yasuhito Morikawa"]
tags: ["コードレビュー", "大規模言語モデル"]
categories: []
date: 2024-11-05T13:07:05+09:00
lastmod: 2024-11-05T13:07:05+09:00
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

本研究室のM2森川君が2024年10月9〜11日にかけてアメリカで開催された[The 40th International Conference on Software Maintenance and Evolution (ICSME2024)](https://conf.researchr.org/home/icsme-2024)で第一著者として投稿した下記の論文を発表しました.

>Yasuhito Morikawa, Yutaro Kashiwa, Kenji Fujiwara, Hajimu Iida: RevToken: A Token-Level Review Recommendation: How Far Are We?, In Proceedings of the 40th IEEE International Conference on Software Maintenance and Evolution(ICSME2024), Oct. 2024.

ICSME2024はソフトウェア保守と開発に関する研究を扱うCoreAランクの国際会議です．森川君が投稿したNew Ideas and Emerging Results Trackトラックでは，35本の投稿のうち10本の論文が採択されました（採択率28%）．

[本研究]()ではモダンコードレビューにおけるレビュアーの負担軽減を目的として，従来の提案手法よりもより細かなトークンレベルでの指摘箇所推薦手法を発表しました．


本研究では事前学習言語モデルであるCodeBERTをベースとしてFine-tuningを行い，モデルを構築しました．
また，推薦時には，LIMEとCodeBERT内部のAttention機構の２つを用いることでトークンレベルの推薦を可能にし，OpenStackとQtBaseデータセットを使用した実証的評価では，変更が必要であると予測されたトークンの最大84%が実際に変更されていたことが実証されました．
