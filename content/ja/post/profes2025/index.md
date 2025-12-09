---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "金地君，Amyさん，TonnamさんがPROFES2025にて研究発表を行いました"
subtitle: ""
summary: ""
authors: [rintaro-kanaji]
tags: ["Security","Agentic Coding","Software Libraries","Ecosystem"]
categories: []
date: 2025-12-10T14:32:55+09:00
lastmod: 2025-12-10T14:32:55+09:00
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
![](Kanaji.png)

本研究室の金地君と，Kasetsart UniversityのAmyさん，Tonnamさんが，2025年12月1日~3日にかけて行われた[26th International Conference on Product-Focused Software Process Improvement (PROFES 2025)](https://conf.researchr.org/home/profes-2025)で発表を行いました．


金地くんは “An Empirical Study of Security-Policy Related Issues in Open Source Projects” というタイトルで発表しました．
本研究では，GitHub リポジトリ内で脆弱性を報告するためのファイルである，SECURITY.mdに着目し，その普及率が低い理由を調査しました．具体的には，SECURITY.mdファイルと5種類のコミュニティヘルスファイルに関連するIssueを分析し，導入が進まない要因を明らかにしました．その結果、SECURITY.mdの導入がかえってコントリビューターを混乱させているケースが存在することが確認されました．


Amyさんは "On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code" というタイトルで発表しました．
本研究では，エージェンティックコーディングツールにおけるエージェントマニフェストの役割と実態を調査しています．発表では，242のリポジトリから収集した253個のClaude.mdファイルを分析し，マニフェスト構造の特徴，記述内容の傾向，および共通パターンを明らかにしました．
その結果，マニフェストは1つの主要見出しと複数のサブセクションから成る浅い階層構造を持ち，内容の多くが運用コマンド，技術的な実装メモ，高レベルアーキテクチャの説明に集中していることが分かりました．


Tonnam さんは "Detecting and Characterizing Low and No Functionality Packages in the NPM Ecosystem" というタイトルで発表しました．
本研究では，最小限の機能しか持たない trivial packages と，実行可能なロジックを含まない data-only packages を対象に，それらの普及状況とセキュリティリスクを調査しています．発表では，これらのパッケージを検出するための規則ベース静的解析手法を開発し，2025年時点の npm エコシステムにおけるリスク評価を行いました．
分析の結果，パッケージの 17.92%が trivial packages に分類され，その脆弱性レベルは非 trivial パッケージと同程度であることが示されました。また，data-only packages は頻度こそ低いものの，依然としてリスクを含むことも確認されました。提案手法による検出ツールは94%の精度（macro-F1 0.87）を達成し，大規模解析やセキュリティリスク低減に有用であることが示されました．



![](Amy.jpg)

![](Tonnam.jpeg)




