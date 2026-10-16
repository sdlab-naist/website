---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "本研究室の学生がESEM2026で研究発表を行いました"
subtitle: ""
summary: ""
authors: [ayane-shirakawa, suzuka-yoshimoto]
tags: ["Continuous Integration (CI)", "Test failures", "Empirical analysis", "Self-Admitted Technical Debt", "Test Coverage", "Software Testing"]
categories: []
date: 2026-10-14T16:04:55+09:00
lastmod: 2026-10-14T16:04:55+09:00
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
本研究室の白川さんと吉本さんが，2026年にドイツ・ミュンヘンで開催された実証的ソフトウェア工学に関する国際会議 [The 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)](https://conf.researchr.org/home/eseiw-2026) において，下記の2本の論文を発表しました．

ESEMはソフトウェア工学の実証的研究に関する国際会議であり，今年で20回目の開催となるトップカンファレンスのひとつです．白川さんと吉本さんが投稿したTechnical Paperでは，去年の投稿数より75%増加し，269本の投稿のうち51本の論文が採択されました（採択率18.9%）．

> Ayane Shirakawa, Tatsuya Shirai, Yutaro Kashiwa, Masanari Kondo, Yasutaka Kamei, Hajimu Iida,
> "Test Alert Snooze: An Empirical Study of Consecutive Test Failures on CI", In Proceedings of the 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)

白川さんが発表しました．本研究では，継続的インテグレーション（CI）におけるテスト連続失敗の実態やそれに関連する開発者の行動を明らかにするために，同一のテストメソッドが2つ以上の連続するリビジョンで失敗し続ける状態をTest Alert Snoozeと定義し，Test Alert Snoozeの発生率・継続期間・開発者の行動を実証分析しました．その結果として，Test Alert Snoozeは全27件のOSSプロジェクトのうち4件（約15%）が発生していました．その4件のプロジェクトに着目すると，全体の61.1%が2リビジョン連続で失敗し，全体の52.9%が1日以内で解消されたことが明らかになりました．また，CSSタイプを用いてリビジョンを分類して開発者の行動を分析した結果，Test Alert Snoozeが発生中はドキュメントが修正される傾向が高く，解消時にはテストが修正される傾向が高いことが判明しました．([LIPIcs.ESEM.2026.24](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.24))

> Suzuka Yoshimoto, Kosei Horikawa, Daniel Feitosa, Yutaro Kashiwa, Hajimu Iida,
> "Is Self-Admitted Technical Debt Tested? An Empirical Study of Coverage, Co-change, and Impact", In Proceedings of the 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)

吉本さんが発表しました．([LIPIcs.ESEM.2026.36](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.36))