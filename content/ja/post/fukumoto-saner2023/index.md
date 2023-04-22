---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "福本大介君がSANER2023で発表しました"
subtitle: ""
summary: ""
authors: ["Daisuke Fukumoto"]
tags: ["Code Completion", "Deep Learning"]
categories: []
date: 2023-03-23T16:05:10+09:00
lastmod: 2023-03-23T16:05:10+09:00
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
本研究室M2の福本大介君が2023年3月21日〜24日にかけて開催された[30th IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER 2023)](https://saner2023.must.edu.mo/index)で下記の論文を発表しました．

> Daisuke Fukumoto, Yutaro Kashiwa, Toshiki Hirao, Kenji Fujiwara and Hajimu Iida, 
> "An Empirical Investigation on the Performance of　Domain Adaptation for T5 Code Completion", 30th IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER 2023), Mar. 2023.

SANER2023はIEEEが主催するソフトウェア解析，進化．リエンジニアリングに関する国際会議で，統合前の会議も含めると今回で30回目の開催となる歴史あるトップカンファレンスです．福本君が投稿したERAトラックでは，30本の投稿のうち12本の論文が採択されました（採択率40%）．

本研究では深層学習に基づくコード補完モデルが，プロジェクトのコーディング規約に違反するといった問題に対して，対象プロジェクトのソースコードを用いたドメイン適応の改善効果について調査しました．実験結果として，ソフトウェア工学における最先端のコード関連タスク向けのモデルであるCodeT5を用いた検証結果と，プロジェクトの規模による影響について説明しました．

![](image2.jpg)