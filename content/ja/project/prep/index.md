---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "PReP（Product Relation-based Process modeling）"
summary: ""
authors: ["hajimu-iida"]
tags: ["Software Process"]
categories: []
date: 2020-02-17T13:36:29+09:00

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

PRePはソニー株式会社と当講座およびソフトウェア工学講座の共同研究で開発された成果物指向のソフトウェアプロセスモデル化手法です．

## 研究背景
ソフトウェア開発プロセスを改善するためには，プロセスのモデル化が重要となってきます．従来のソフトウェアプロセスモデルの多くは，作業の順序関係によってプロセスを記述しています．しかし，いくつかの組織においては，このような方法で記述することが困難な場合があります．

## PRePモデル
PRePモデルでは，ソフトウェア開発で作成される成果物間の関係を描くことで，容易にプロセスをモデル化します．PRePモデルは，以下の3つのサブモデルから構成されます．

- 作業モデル：成果物を定義し，それを作成するのに必要な作業を関連付けるモデル
- 構造モデル：成果物間の関係を定義するモデル
- 工程モデル：構造モデルに，マイルストーンと工程，反復を定義したモデル

{{< figure src="prep.jpg" lightbox="true" >}}

## PReP/SGTs（Schedule Generation Tools）
PReP/SGTsはPRePモデルによるプロセス記述からスケジュールを半自動的に生成し，運用を支援するためのツール群です．

- Visio2PReP：作画ツール（Microsoft Visio）で作成されたXMLファイルを，PRePモデル標準形式のXMLファイルへ変換する
- PReP2Project：PRePモデル標準形式のXMLファイルから，プロジェクト管理ツール（Microsoft Project）で読み込み可能なスケジュールデータを生成する

{{< figure src="sgts.jpg" lightbox="true" >}}
