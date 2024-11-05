---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "馬渕君がSCAM2024で発表しました"
subtitle: ""
summary: ""
authors: ["Yasuhito Morikawa"]
tags: ["Docker", "プリプロセッサ"]
categories: []
date: 2024-11-05T12:27:07+09:00
lastmod: 2024-11-05T12:27:07+09:00
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
本研究室のM2馬渕君が2024年10月7〜8日にかけてアメリカで開催された[IEEE International Conference on Source Code Analysis & Manipulation(SCAM2024)](https://conf.researchr.org/home/scam-2024)で第一著者として投稿した下記の論文を発表しました.

> Wataru Mabuchi, Yutaro Kashiwa, Kenji Fujiwara, Hajimu Iida: "An Empirical Investigation Into the Use of Dockerfile Preprocessors for Docker Image Management", In Proceedings of The 24th  Source Code Analysis and Manipulation (SCAM2024), Oct. 2024.

SCAMはソースコードの分析や操作に関する理論，技術，アプリケーションに関する研究を扱う国際会議です．


[本研究]()ではDockerfile Preprocessors(DPP)の使用に関する実証的な研究を行いました．
GitHubから146つのDocker official imagesを対象とし，分析を行った結果，

(1)DPPプロジェクトは，DPP非採用プロジェクトよりも多くのイメージをサポートし，より頻繁にリリースすること．

(2)DPPの採用により，Dockerfile作成の労力が軽減されるものの，リリースやコミットアクティビティは促進されない可能性があること．


を明らかにしました．