---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Analytics"
summary: ""
authors: ["hajimu-iida"]
tags: ["Software Analytics"]
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

## ソフトウェア アナリティクスとは
ソフトウェア アナリティクスは ， ソフトウェア開発の個人やチームがより良い意思決定できるようにする事を目的としています．そのために ， ソフトウェアに関するデータ（ソースコードや開発履歴など）を分析します．分析した結果は ， ソフトウェア開発の個人やチームが共有できる形にして提供します．

- 参考Webサイト：[ビッグデータ時代のソフトウェアメトリクス - ソフトウェアアナリティクスとは：森崎修司の「どうやってはかるの？」：オルタナティブ・ブログ](https://blogs.itmedia.co.jp/morisaki/2013/07/--e8a3.html)（参考日：2017年4月1日）
- 参考文献：Tim Menzies, Thomas Zimmermann. "Software Analytics: So What?". In Journal IEEE Software archive Volume 30 Issue 4, July 2013 Pages 31-37.


## 現在取り組んでいる研究テーマ
### キーワード：コードクローン
コードクローンとは，プログラム中のソースコードのうち重複している箇所のことを指します．研究例としては，[コードクローン履歴を用いたソフトウェア理解支援環境の研究](/project/code-clone-history/)（この研究では版管理システムが持つ開発履歴を利用してコードクローンの変遷をわかりやすく提示する環境の構築を目指します．)などがあります。

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

### キーワード：ソフトウェアテスト
ソフトウェアテスト(以下，テスト)は，ソフトウェアが仕様書通りに動作することを確認することであり，不具合を検出し修正することでソフトウェアの品質を向上させることを目的として行われます．このテスト工程で不具合を検出できなかったソフトウェアはそのままユーザにリリースされてしまうため，テストは非常に重要です．しかし，大規模なソフトウェアに対して手作業でのテスト作成は多くのコストがかかり，開発全体のコストの中で30~50%が必要とされています．そのため，ソフトウェアの品質を確保しつつ，コスト削減を達成するために様々な研究が行われています．研究例としては，[テストコード自動推薦ツール](/project/testcode-recommendation)などがあります．

- 参考文献：丹野 治門, 倉林 利行, 張 暁晶, 伊山 宗吉, 安達 悠, 岩田真治, 切貫 弘之. テスト入力値生成技術の研究動向. コンピュータ ソフトウェア, 34(3):121–147,2017.

### その他のソフトウェア アナリティクスに関する研究例
- MUDABlue: ソフトウェア自動分類システム
ソフトウェアリポジトリには膨大な数のソフトウェアが登録されています．これらの中から類似ソフトウェアを発見するためのメカニズムを提供することで，ソフトウェアの再利用や，開発者間のコミュニケーション促進を目指します．詳細は[こちら](/project/muda-blue)．