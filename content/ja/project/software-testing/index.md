---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Testing"
summary: ""
authors: ["Ryosuke-Kurachi"]
tags: []
categories: []
date: 2020-03-03T11:16:48+09:00

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

## ソフトウェアテストとは
ソフトウェアテスト(以下，テスト)は，ソフトウェアが仕様書通りに動作することを確認することであり，不具合を検出し修正することでソフトウェアの品質を向上させることを目的として行われます．このテスト工程で不具合を検出できなかったソフトウェアはそのままユーザにリリースされてしまうため，テストは非常に重要です．しかし，大規模なソフトウェアに対して手作業でのテスト作成は多くのコストがかかり，開発全体のコストの中で30~50%が必要とされています．そのため，ソフトウェアの品質を確保しつつ，コスト削減を達成するために様々な研究が行われています．

- 参考文献：丹野 治門, 倉林 利行, 張 暁晶, 伊山 宗吉, 安達 悠, 岩田真治, 切貫 弘之. テスト入力値生成技術の研究動向. コンピュータ ソフトウェア, 34(3):121–147,2017.

## 現在取り組んでいる研究テーマ
### キーワード：テストコード自動推薦システム
開発者に高品質のテストコードを自動推薦するツールの開発に取り組んでいます．ソフトウェアの品質確保の要と言えるソフトウェアテストを支援することは，重要です．これまでにテスト工程を支援するために，様々な自動生成技術が提案されてきました．しかし，既存技術によって自動生成されたテストコードは，テスト対象コードの作成経緯や意図に基づいて生成されていないため，開発者の保守作業を困難にさせる課題があります．そこで，本研究ではオープンソースソフトウェアに存在する品質の高いテストコードを自動で推薦することで，開発者のテストコード作成を支援することを目指しています。

{{< figure src="SuiteRec.jpg" title="" lightbox="true" >}}



