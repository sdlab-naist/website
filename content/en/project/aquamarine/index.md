---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "AQUAMarine - 定量的管理計画立案支援システム"
summary: ""
authors: ["hajimu-iida"]
tags: []
categories: []
date: 2020-02-17T13:32:03+09:00

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

## AQUAMarineとは
AQUAMarine は，プロジェクト計画者による定量的管理計画の立案作業支援を目的としたシステムです．AQUAMarine は本講座が株式会社日立製作所との共同研究にやEASEプロジェクトの成果に基づいて開発したシステムで，EPDG2 (Electronic Process Data Guidebook 2) という名称で開発が進められてきました．

AQUAMarine では，プロジェクトの計画者が個々の開発プロジェクトを立案する際に，管理指標の選択や管理に必要なデータの測定・分析活動の開発計画への組み込みといった作業の支援を行います．このシステムにより，十分な経験を積んでいない計画者でも，定量的管理を取り入れた管理計画の立案を円滑に行うことが可能となります．

AQUAMarine の試用を希望される方は，以下のダウンロードとリリースノートをご覧下さい．

## 背景 ～ 失敗するプロジェクト
近年，社会においてソフトウェアは重要な役割を担っています．しかし，その一方で，ソフトウェアの開発プロジェクトは，ソフトウェアのリリースに至らず失敗に終わることや，欠陥が見過ごされたままソフトウェアがリリースされてしまうことが多く，莫大な損失を生み出していることが報告されています．

この背景として，プロジェクトの規模が年々大きくなっているにも関わらず，開発計画が不十分なままであることが考えられます．すなわち，計画が不十分なままプロジェクトが進行し，結果としてスケジュールの遅れやコスト超過などの問題が発生していると考えられます．

## 開発プロセスの改善
このような状況の中で，ソフトウェアの品質改善・コスト削減を目的としたソフトウェア開発プロセス改善が注目されています．例としては，CMU/SEIのCMMIなどが挙げられます．これらは品質管理や進捗管理などの改善・効率化のための枠組みとして，多くの開発組織において取り入られています．

## 開発プロセスの定量的管理
CMMIなど，多くのプロセス改善の枠組みの中では，定量的管理がソフトウェア開発における最も重要な主題の一つと言われています．定量的管理とは，「ソフトウェアのコード行数」や「プロジェクトの進捗会議の開催回数」といった定量的測定データを監視し，一定の基準（管理指標）に基づき随時プロジェクトを是正していく管理手法を指します．

定量的管理は，開発プロジェクトが実施されている最中に，早期に問題を特定し改善するために重要であると言われています．

## 定量的管理は難しい！
しかし，開発プロセスの定量的を実際に行うことは非常に困難です．なぜならば，ソフトウェアの開発は人間の知的作業を多く含むために，開発プロセスをどの観点から定量的に計測し，その計測した値をどのように解釈し，プロセスを改善していけば良いかが明らかになっていないためです．

また，定量的管理を行うことを考慮して開発プロジェクトを立案するためには，納期や予算などの制約や管理指標や定量的測定データに対する理解が必要となります．このため立案作業は非常に複雑となり，特に十分な経験を積んでいないプロジェクトの管理者（計画者）にとっては非常に困難なものとなっています．

## AQUAMarine: 定量的管理計画の立案支援システム
本研究では，プロジェクトの計画者による定量的管理計画の立案作業支援を目的とした，定量的管理計画の立案支援システムAQUAMarineを提案します．

AQUAMarine の利用者は，図 1 の画面から，開発プロセスを概観する事ができ，個々の開発プロセスに対して定量データの測定・分析活動を関連づける事ができます．また，プロセスや管理指標，成果物の詳細な定義を確認する事も可能です．

{{< figure src="aquamarine_snapshot.jpg" title="図1 AQUAMarine のスナップショット" lightbox="true" >}}

## AQUAMarine の利点
AQUAMarine がプロジェクト計画者に対して行う支援には，以下のような効果があると考えられます．

- プロジェクトを管理する際に用いる定量データを一覧することができ，その場で取捨選択が行えるため，一貫した視点にもとづいて定量的管理計画の立案が行える．
- 各プロセスや定量データの測定結果収集作業が視覚的に確認できるため，定量データの測定結果収集作業やプロジェクト管理に対して，具体的なイメージを持って望むことができる．
- 定量データの概念と詳細を容易に参照できるため，管理計画の指針や定量データに対する理解を深めることができる．

総合的な効果としては，AQUAMarine の活用により，プロジェクト計画者と管理者が，定量的管理の目的を理解できるようになることが挙げられます．したがって，プロジェクト管理や測定が正しく実践され，形式的な管理体制に陥りにくくなることが期待されます．

## ダウンロードとリリースノート
AQUAMarine の最新版は[こちら](http://sdlab.naist.jp/projects/aquamarine/agreement.html)からダウンロードできます．

リリースノートは[こちら](http://sdlab.naist.jp/projects/aquamarine/release.html)からご覧になれます．
