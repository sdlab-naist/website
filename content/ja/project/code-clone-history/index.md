---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "コードクローン履歴理解支援環境"
summary: ""
authors: ["hajimu-iida"]
tags: ["Software Analytics", "Code Clone"]
categories: []
date: 2020-02-18T10:58:21+09:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "過去にコードクローン関係にあったコード片の例"
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

## コードクローンとは
ソースコード中に現れる重複コードのことをコードクローンと呼ばれています． コードクローンの多くは安易なコピー&ペーストによって生みだされていま す．これらのコードクローンは保守作業における大きな障害になります．もしそ の部分を修正しなければならない場合，すべてのコードクローンについて修正を 加えなければならないからです．

しかし，大規模なソフトウェアには大量のコードクローンが存在するため，どの コードクローンから除去するべきなのか，そのコードクローンは除去すべき部分 なのかといったことを判断するのは困難です．

## コードクローン履歴の理解支援
本研究では，コードクローンの変遷履歴を提示することでコードクローンの理解 支援を行います．例えば，そのコードクローンが発生した当時の状況やコードク ローンの増殖過程を提示することで，そのモジュール開発に携わっていない開発 者が判断を下す際のてがかりを提供します．

これまでにコードクローン履歴を活用して，過去にコードクローン関係にあった コード間の関係抽出を行う手法を提案しています．そして，過去にコードクロー ン関係にあったコード片は，一見異なるように見えて同様の処理を行っている箇 所が多く，このような部分もまた留意する必要があることを確認しています．


## 今後の研究課題
1. 履歴情報を用いたコードクローンの定量的評価手法の確立

    履歴情報を用いることで従来の評価手法とはまた異る評価基準を提示できるのではないか，と考えています．例えばコードクローンを作成した人に着目して，あまりにもコードクローンを安易にコピーしている開発者がいれば，その開発者が関わったコードクローンは危険度が高いなどの判断ができます．

    このような仮説からコードクローン履歴の評価基準を定式化し，実際のソフトウェア品質と有為な関連があるものを厳選することで，対処優先度の定式化，および優先的に対処すべきコードクローンの自動的提示を目指します．

2. コードクローン履歴閲覧環境の構築

    コードクローンの除去作業を支援するためには，得られたコードクローンの履歴や，それに基づく定量的評価の結果をプログラマにわかりやすく提示する必要があります．そのような環境の構築を行います．

## 関連文献
- 川口　真司, “版管理システムを用いたクローン履歴分析手法,” ソフトウェア工学工房 第8, 9回セミナー　コードクローン検出技術とその応用, 2007.2.7
- 川口　真司, 松下　誠, 井上　克郎, 飯田　元, “コードクローン履歴閲覧環境を用いたクローン評価の試み,” 情報処理学会第154回ソフトウェア工学研究会, pp49-56, 2006.11.27
- 川口　真司, 松下　誠, 井上　克郎, “版管理システムを用いたクローン履歴分析手法の提案,” 電子情報通信学会論文誌 D, vol.89, no.10, pp.2279-2287, 2006.10.1.
- 川口　真司, “集合知の活用を考慮したクローン履歴閲覧環境の実現を目指して,” Workshop on Leveraging Web2.0 Technologies in Software Development Environments (WebSDE), pp10-11, 2006.9.19
- 川口真司, 松下誠, 井上克郎: "クローン履歴を利用したクローン分析環境", ウィンターワークショップ 2006 イン 鴨川, 東洋大学 鴨川セミナーハウス, 2006.1.26.
- 川口真司, 松下誠, 井上克郎: "版管理システムを用いたコードクローン履歴分析", 電子情報通信学会技術研究報告, SS2005-31, Vol.105, No.228, pp.43-48, 小樽商科大学, 2005.8.4. [pdf](548.pdf) [ppt](548.ppt)
