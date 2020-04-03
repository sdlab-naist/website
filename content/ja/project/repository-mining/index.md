---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Repository Mining"
summary: ""
authors: ["hajimu-iida"]
tags: []
categories: []
date: 2020-02-17T13:14:49+09:00

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

## ソフトウェア開発履歴からのお宝発掘 - リポジトリマイニング
本研究ではソフトウェア理解を支援するために，これまでに開発されたソフトウェア群の開発履歴を分析・整理して提示する手法を提案しています．特にその情報源としてソフトウェアリポジトリに着目しています．

ソフトウェアリポジトリとは多数の開発者がネットワークを通じて協調して開発するときに用いる開発基盤を提供するサービスです．その構成物は，ソースコードを管理する版管理システムや，開発者間で交わされた議論を保管しておくメーリングリスト管理システムなどがあります．これまでにソフトウェアリポジトリはオープンソースソフトウェアを中心に，さまざまなソフトウェア開発で実際に利用されており，膨大な開発履歴が蓄積されています．ただ，これらの情報はあまりにも膨大なため，そのままでは十分に活用することができません．

そこで，これらの情報から枝葉末節を省略したり，類似情報をまとめたりといった整理統合を行って，有用な情報を把握可能な形で提供しよう，というのが本研究の狙いです．このような作業をリポジトリマイニングと呼びます．

## 現在取り組んでいる研究テーマ

### 開発履歴を用いたリファクタリングと欠陥の関係分析
リファクタリングとは，プログラムの動作を変えることなくソースコードの設計を改善することを言います． リファクタリングの伝道者として有名なファウラーは，「リファクタリングを実施すると欠陥（バグ）の混入が減少する」と著書で述べています． そこで，この研究ではソースコードの変更履歴からリファクタリングの実施を推定し，バグ管理システムに記録された欠陥の修正情報と照らし合わすことで，リファクタリングが本当に欠陥混入を減少させるのかどうかを明らかにします．

### 開発履歴を用いたコードクローン理解支援環境
コードクローンとは，プログラム中のソースコードのうち重複している箇所のことを指します．この研究では版管理システムが持つ開発履歴を利用してコードクローンの変遷をわかりやすく提示する環境の構築を目指します．詳細は[こちら](/project/code-clone-history)．

### 履歴情報を用いたデザインパターン分析
デザインパターンとは，ソフトウェア開発の設計段階で蓄積されたノウハウを再利用できるかたちでまとめたものです．デザインパターンを用いることで，ソフトウェアの品質を向上させることができると言われていますが，その実態は明らかになっていません．本研究プロジェクトでは，デザインパターンの利用状況やソフトウェアの品質との関連を明らかにすることを目的として研究を行っています．

### 開発者の共起関係に基づく開発プロジェクト分析
オープンソースソフトウェア開発において，プロジェクトのアクティビティはソフトウェアの品質に影響を及ぼす大きな要因とされています．本研究グループでは，開発に用いられるメーリングリストに着目し，開発者の共起性からプロジェクトの共起性について予測する手法を研究しています．
