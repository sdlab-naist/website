---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "藤田君がICSME2023で発表しました"
subtitle: ""
summary: ""
authors: ["Yutaro Kashiwa"]
tags: ["Software Test"]
categories: []
date: 2023-11-05T16:05:10+09:00
lastmod: 2023-11-05T16:05:10+09:00
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
本研究室のインターンシップ生である藤田駿君（現，京都大学所属）が2023年10月1日〜6日にかけてコロンビアで開催された[The 39th IEEE International Conference on Software Maintenance and Evolution and Reengineering (ICSME 2023)](https://conf.researchr.org/home/icsme-2023)で下記の論文を発表しました．

> Shun Fujita, Yutaro Kashiwa, Bin Lin, and Hajimu Iida, 
> "An Empirical Study on the Use of Snapshot Testing", In Proceedings of the 39th IEEE International Conference on Software Maintenance and Evolution, pp. 335--440, 2023.

ICSME2023はIEEEが主催するソフトウェアメインテナンスに関する国際会議で，今回で39回目の開催となる歴史あるトップカンファレンスです．藤田君が投稿したERA (Early Research Achivement)トラックでは，33本の投稿のうち13本の論文が採択されました（採択率39%）．

本研究ではスナップショットテストと呼ばれるReactなどの開発で広く用いられるテストがどのように利用されているかについて調査しました．GitHubプロジェクトから約1,500リポジトリを収集し，分析した結果，（1）スナップショットテストと単体テストを利用するプロジェクトでは，単体テストのみを用いるプロジェクトよりも，多くのテストを利用していること（2）8.2%のコミットでスナップショットファイルが変更され，その際には多くのファイルと同時に編集されること等を明らかにしました．
当該論文は[GitHub](https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2023_Fujita.pdf)にて公開されています．本研究はインターンシップの一環として実施すると共に，オランダ・Radboud大学との共同研究として実施されました．

![](image2.jpg)
