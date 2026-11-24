---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "本研究室の学生がFOSE2026でポスター発表を行いました"
subtitle: ""
summary: ""
authors: [akihiro-saeki, suzuka-yoshimoto, hirohito-ota, sota-onuma, ryosuke-ono, yamamoto-ryotaro]
tags: ["FOSE", "ポスター発表"]
categories: []
date: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more projects.
#   Simply enter the project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
本研究室の佐伯さん，吉本さん，大田さん，大沼さん，大野さん，山本さんが，[ソフトウェア工学の基礎ワークショップ（FOSE2026）](https://fose.jssst.or.jp/fose2026/)に参加し，ポスター発表を行いました．

FOSE2026は2026年11月12日から3日間にわたり，秋田県の秋田温泉さとみで開催されました．

各発表の概要を以下に紹介します．

### 佐伯さん

**発表タイトル：** 【タイトルを追記してください】

【研究内容・発表概要を追記してください】

### 吉本さん

**発表タイトル：大規模言語モデルによる開発作業の完了判定能力の評価**  

LLMが自律的な開発作業の成否を判断する能力を評価するため，開発者が課題を記録したコメント（SATD）の削除履歴に着目する．単なるコメント削除と技術的負債の実質的な解消をLLMがどの程度判別できるかを実証的に検証し，LLMによる作業完了判断の可能性と限界を明らかにする．

### 大田さん

**発表タイトル：** メソッドの配置順序がLLMのコード理解に与える影響の調査

LLM を用いたソフトウェア開発では，既存コードの構造や振る舞いを理解する能力が求められる．先行研究では，プログラムの意味を変えないメソッドの並び替えによって Fault Localization（FL）の精度が変動することが報告されている．しかし，メソッドの配置順序がコード理解そのものに及ぼす影響は明らかになっていない．本研究では，実行経路の理解を必要とするカバレッジ予測を用いて，メソッドの配置順序が LLM のコード理解に与える影響を調査する．

### 大沼さん

**発表タイトル：LLMを用いたSilent Horrorsの大規模実態調査にむけて**  

テストとプロダクション双方のバグでテストが誤って成功する「Silent Horrors」は，既存調査の制約により実態が未解明である．本研究では双方の変更を含むコミットも対象とし，LLMを用いて大規模に分析することで，その実態と特徴を明らかにする．

### 大野さん

**発表タイトル：テスト品質指標が自動プログラム修正エージェントの修正精度に与える影響の調査**  

LLMを用いたバグ修正エージェントの修正精度が，与えるテストケースの質によってどう変わるかを調査する．LLMで生成したテストケースを段階的に追加しながらエージェントに渡し，テスト品質指標の変化に伴う修正の様子を観察した結果を報告する．

### 山本さん

**発表タイトル： Agent Context File の遵守に関する大規模評価基盤の構築に向けて**

AGENTS.md や CLAUDE.md などの Agent Context File (ACF) は開発者がエージェントにプロジェクト固有の指示を伝える手段として広く用いられつつある．LLM が実際に ACF の指示を守っているのか，注目されつつある．しかし，指示が守られたかどうかを自動的に評価する手法はまだ確立していない．本研究では，LLM を用い，ACF の指示が遵守されているかどうかを判定する枠組みを構築する．
