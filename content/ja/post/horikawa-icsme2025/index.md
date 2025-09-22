---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "堀川君がICSME2025で発表しました"
subtitle: ""
summary: ""
authors: [kosei-horikawa]
tags: []
categories: ["Refactoring", "Code Metrics", "Code Readability", "Code Smell", "Mining Software Repository"]
date: 2025-09-19T20:40:05+09:00
lastmod: 2025-09-19T20:40:05+09:00
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
本研究室の堀川君が2025年9月7日〜12日にかけてニュージーランドで開催された[The 41st IEEE International Conference on Software Maintenance and Evolution (ICSME 2025)](https://conf.researchr.org/home/icsme-2025)において下記の論文を発表しました．

> Kosei Horikawa, Yutaro Kashiwa, Bin Lin, Kenji Fujiwara, and Hajimu Iida, 
> "How Does Test Code Differ From Production Code in Terms of Refactoring? An Empirical Study", In Proceedings of the 41st IEEE International Conference on Software Maintenance and Evolution, pp. 779--784, 2025.

ICSME2025はIEEEが主催するソフトウェアメンテナンスに関する国際会議で，今回で41回目の開催となる歴史あるトップカンファレンスです．堀川君が投稿したNIER (New Ideas and Emerging Results Track)トラックでは，43本の投稿のうち17本の論文が採択されました（採択率39.5%）．

本研究ではプロダクションコードとテストコードでリファクタリングの影響がどのように異なるのかについて調査しました．GitHubから455件のJavaプロジェクトを収集し，合計670万件のリファクタリングを分析しました．分析の結果，（1）プロダクションコードのリファクタリングは構造的な改善（APIレベルの変更など）に焦点を当てているのに対し，テストコードでは可読性向上のためのメソッド名の変更やテスト固有の操作が中心であること（2）リファクタリングによってコードの可読性はプロダクションコード・テストコード双方で向上するものの，コード行数や複雑さといった指標は，プロダクションコードでは減少傾向である一方，テストコードでは増加傾向にあること等を明らかにしました．
当該研究は[GitHub](https://github.com/Mont9165/ProdTestRefactoringAndMetrics/blob/main/How%20Does%20Test%20Code%20Differ%20From%20Production%20Code%20in%20Terms%20of%20Refactoring%3F%20An%20Empirical%20Study.pdf)にて公開されています．本研究は杭州电子科技大学のBin Lin 特任准教授，奈良女子大学の藤原賢二 専任講師との共同研究として実施されました．

![](image2.jpg)
