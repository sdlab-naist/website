---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "MUDABlue ソフトウェア自動分類システム"
summary: ""
authors: []
tags: ["Software Analytics"]
categories: []
date: 2020-02-18T11:03:43+09:00

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

## 類似ソフトウェアの発見
MUDABlue はソフトウェアリポジトリに蓄積されている膨大なソフトウェアの分類を自動化するためのシステムです．

MUDABlue が提供する分類結果を利用することで，もし要求を満すソフトウェアが発見できれば，これを **そのまま再利用** することで開発工程を大幅に削減することが可能になります．また，再利用が困難であっても比較的類似したソフトウェ アが発見できれば，その開発履歴，例えばバグレポートやソースコードの変遷などを見ることで，バグが多くでた部分はどこか，どの部分の実装に工数を要したのか，など **開発が困難であろうと思われる部分を事前に知る** ことができます．

## MUDABlueの特長
1. 多重分類の許容
    もっとも単純な分類はソフトウェアの用途による分類です．しかし，ソフ トウェアにはそれ以外にもさまざまな分類基準が考えられます．例えば Windows 上で動作するのか，Mac 上で動作するのかといった対応 OS による分類などが考えられます．

    このような分類を実現するために，MUDABlue は一つのソフトウェアが複 数個のカテゴリに属することを許しています．これにより，Windows 上で動作するテキストエディタといった概念をごく自然に表現しています．

    {{< figure src="soft_categorize.png" title="多重分類されるソフトウェア" lightbox="true" >}}

2. カテゴリの自動抽出

    これまでに提案されている自動分類手法では分類対象であるカテゴリの集合は前もって与えられており，各ソフトウェアがどのカテゴリに当てはまるのかを決定するものでした．しかし，ソフトウェアを取りまく環境の変化は目まぐるしく，日々新たなアーキテクチャやライブラリが提案されています．

    そこで MUDABlue ではカテゴリをも自動的に抽出することで，アーキテクチャやライブラリの追加にも自動的に対応します．

3. ソースコードのみから分類

    多くの研究ではソフトウェアに付属するドキュメントを用いて分類を行いますが，付属するドキュメントの質や量はソフトウェアによって大きなバラツキがあります．そもそも付属ドキュメントがないソフトウェアもたく さんあります．

    MUDABlue ではソースコードだけを利用して分類を行います．ドキュメン トがないソフトウェアはあっても，ソースコードが存在しないソフトウェアは存在しません．

## 今後の研究課題
1. ヒューマンファクターの適度なとりこみ

    MUDABlue はソフトウェアの自動分類する際には事前知識を一切必要としません．このことは本手法の大きなメリットですが，同時に予測精度向上のための支援ができないことも意味します．そこで何らかの形で事前知識を用いることで分類の精度向上を目指します．

2. より大規模なソフトウェアリポジトリへの本手法の適用

    実際に数百，数千個規模のソフトウェアに対して本手法を適用して分類が適正にできるかどうかの評価を行うことで，本手法をより実践的なものにすることを目指します．

## 関連文献
- Shinji Kawaguchi, Pankaj K. Garg, Makoto Matsushita, Katsuro Inoue: "MUDABlue: An Automatic Categorization System for Open Source Repositories", The Journal of Systems and Software, Vol 79/7, pp.939-953, 2006.
- 川口真司, パンカジ ガーグ，松下誠, 井上克郎: "MUDABlue: ソフトウェアリポジトリ自動分類システム", 電子情報通信学会論文誌 D-I, Vol.J88-D-I, No.8, pp.1217-1225, 2005. [pdf](525.pdf)
- Shinji Kawaguchi, Pankaj K. Garg, Makoto Matsushita, Katsuro Inoue: "MUDABlue: An Automatic Categorization System for Open Source Repositories", The 11th Asia-Pacific Software Engineering Conference(APSEC2004), pp.184-193, Busan, Korea, November 30th - December 3rd, 2004. [pdf](506.pdf) [ppt](506.ppt)
- Shinji Kawaguchi, Pankaj K. Garg, Makoto Matsushita, Katsuro Inoue: "Automatic Categorization Algorithm for Evolvable Software Archive", Sixth International Workshop on Principles of Software Evolution (IWPSE2003), pp-195-200, Helsinki, Finland, September 1-2, 2003. [pdf](438.pdf) [ppt](438.ppt)
- 川口真司, 松下誠, 井上克郎: "潜在的意味解析法 LSA を利用したソフトウェア分類システムの試作", 情報処理学会研究報告, 2003-SE-140, Vol.2003, No.22, pp.55-62, 情報処理学会本部会議室, 2003.3.6. (学生研究賞受賞) [pdf](414.pdf) [ppt](414.ppt)
