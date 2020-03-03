---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Testing"
summary: ""
authors: ["Ryosuke-Kurachi"]
tags: []
categories: []
date: 2020-02-17T13:17:13+09:00

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

## ソフトウェア テストとは
ソフトウェアテストとは(以下，テスト)とは，ソフトウェア開発プロセスの中で最後のソフトウェアの品質を確かめる工程である．テストは，ソフトウェアが仕様書通りに動作することを確認することであり，不具合を検出し修正することでソフトウェアの品質を向上させることを目的として行われる。

- 参考Webサイト：[ビッグデータ時代のソフトウェアメトリクス - ソフトウェアアナリティクスとは：森崎修司の「どうやってはかるの？」：オルタナティブ・ブログ](https://blogs.itmedia.co.jp/morisaki/2013/07/--e8a3.html)（参考日：2017年4月1日）
- 参考文献：Tim Menzies, Thomas Zimmermann. "Software Analytics: So What?". In Journal IEEE Software archive Volume 30 Issue 4, July 2013 Pages 31-37.


## 現在取り組んでいる研究テーマ
### テストコード自動推薦ツール
これまでにソフトウェアのテスト工程を支援するために，様々な自動生成技術が提案されてきた。しかし，既存技術によって自動生成されるテストコードは，テスト対象コードの作成経緯や意図に基づいて生成されていないので，開発者の保守作業を困難にさせる。この課題の解決方法として，既存テストの再利用が有効であると考えられる。本研究では，オープンソースソフトウェアに存在する品質が高いテストコードを推薦するツールSuiteRecを提案する。推薦手法のキーアイディアは，類似するコード間でテストコードを再利用

その他のコードクローンに関する研究

- コードクローンとの位置関係に基づく欠陥発生傾向の調査
- コードクローンとの位置関係がコード片の欠陥発生傾向に与える影響の調査
- ハードウェア記述言語におけるコードクローンの調査


### キーワード：リファクタリング
リファクタリングとは，プログラムの動作を変えることなくソースコードの設計を改善することを言います． リファクタリングの伝道者として有名なファウラーは，「リファクタリングを実施すると欠陥（バグ）の混入が減少する」と著書で述べています．研究例としては，開発履歴を用いたリファクタリングと欠陥の関係分析（この研究ではソースコードの変更履歴からリファクタリングの実施を推定し，バグ管理システムに記録された欠陥の修正情報と照らし合わすことで，リファクタリングが本当に欠陥混入を減少させるのかどうかを明らかにします．）などがあります．

その他のリファクタリングに関する研究

- プロセスメトリクスを用いたメソッド抽出事例の特徴調査
- 構文情報リポジトリを用いた細粒度リファクタリング検出手法
- 機械学習を用いたメソッド抽出リファクタリングの推薦手法
- 変更履歴解析に基づくリファクタリング検出技術の調査
- リファクタリングがソフトウェア品質に及ぼす影響の実証的評価に関する研究

### キーワード：プログラミング教育
- ソフトウェア開発PBLにおけるビルドエラーの調査
- スナップショットを用いたプログラミング演習における行き詰まり箇所の特定
- 初学者向けプログラミング演習のための探索的プログラミング支援環境Pocketsの提案
- Detecting Exploratory Programming Behaviors for Introductory Programming Exercises
- 探索的プログラミング行動の自動検出によるモデル化の検討
- ソフトウェア開発実習におけるビルドログを対象とした初学者の特徴的な振る舞いの調査
- 初学者の探索的プログラミングにおけるプロセス認識を支援するシステムの提案

### その他のソフトウェア アナリティクスに関する研究例
- MUDABlue: ソフトウェア自動分類システム
ソフトウェアリポジトリには膨大な数のソフトウェアが登録されています．これらの中から類似ソフトウェアを発見するためのメカニズムを提供することで，ソフトウェアの再利用や，開発者間のコミュニケーション促進を目指します．詳細は[こちら](/project/muda-blue)．
