---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "渡邉さん，藤田君，狩野君，堀川君が2024年7月合同研究会＠北海道で発表を行いました"
subtitle: ""
summary: ""
authors: ["Shun Fujita"]
tags: ["Refactoring","Software test","Techinical Debt"]
#todo
categories: []
date: 2024-07-31T21:00:00+09:00
lastmod: 2024-07-31T21:00:00+09:00
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
本研究室の渡邉未来さん，藤田駿君が2024年7月25日〜27日にかけて開催された[第217回SE研究発表会](https://www.ipsj.or.jp/kenkyukai/event/se217.html)にて，
狩野悟君，堀川康生君が同じく2024年7月25日〜27日にかけて開催された[2024年7月ソフトウェアサイエンス研究会](https://ken.ieice.org/ken/form/index.php?tgs_regid=2fc4be9075af971c827c62a8a625c209fee16e014a7c586bb466c9d8c814fa1c&cmd=info)にて発表しました．

<!-- SE研究発表会（SIGSE）はソフトウェア開発に関する理論から実践までの幅広い諸問題について，研究・開発の成果や経験を発表し，討論することで相互に理解を深めることを目的とした研究会です． -->
<!-- sigss -->


渡邉さんは[「リリースサイクルの短縮化に伴うSelf Admitted Technical Debt導入・解決の影響調査にむけて」](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=237361&item_no=1&page_id=13&block_id=8) というタイトルで，短縮されたリリースサイクルの採用がSATDに与える影響について発表しました．Eclipseを調査対象にして分析を行った結果，短縮されたリリースサイクルを採用することはSATDの観点ではネガティブな影響がないことを明らかにしました．

藤田君は[「スナップショットテストにおける欠陥検出力の実証的評価にむけて」](https://ipsj.ixsq.nii.ac.jp/ej/index.php?active_action=repository_view_main_item_detail&page_id=13&block_id=8&item_id=237362&item_no=1)というタイトルで，スナップショットテストの欠陥検出力について発表しました．GitHubにおけるスナップショットテスト採用リポジトリを対象に調査を行い，スナップショットテストがその他のテストでは検出できない欠陥を検出していることを明らかにしました．

堀川君は[「テストコード固有のリファクタリングが及ぼす影響調査にむけて」](https://ken.ieice.org/ken/paper/202407269c3d/) というタイトルで，実際のOSS開発で実施されるテストコード固有のリファクタリングの頻度や種類，その影響について発表しました．既存研究にはないテストコード固有リファクタリングの発見やテストスメル（テスト品質の低下を招く問題）との関連性を明らかにしました．

狩野君は[「テスト品質とプロダクションコード設計の関連性調査に向けて」](https://ken.ieice.org/ken/paper/20240726fc3d/) というタイトルで，プロダクションコードの設計とテスト品質の関連性について発表しました．先行研究よりも細かな粒度であるメソッドレベルでの関連性について調査を行い，品質の低いテストメソッドと品質の低いプロダクションメソッドの共起関係について明らかにしました．

![](fujita.jpg)
![](horikawa.jpg)
![](kano.jpg)

