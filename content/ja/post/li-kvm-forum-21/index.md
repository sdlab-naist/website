---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Guoqing Li君とDario Faggioli博士がKVM Forum 2021で発表しました"
subtitle: ""
summary: ""
authors: ["Guoqing Li"]
tags: ["Cloud", "Virtualization Performance", "KubeVirt", "Kubernetes"]
categories: []
date: 2021-09-30T16:49:12+09:00
lastmod: 2021-09-30T16:49:12+09:00
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

当研究室の修士課程学生のGuoqing Li君とSUSE LabsのDario Faggioli博士が，
[KVM Forum 2021](https://events.linuxfoundation.org/kvm-forum/) にて
["KubeVirt: The cost of Containerizing VMs"](https://youtu.be/x_czS9Iuo2o) という題目で共同研究の成果を発表しました．

KubeVirtはコンテナオーケストレーション基盤であるKubernetes上でコンテナと仮想マシンを統一的に管理可能にする拡張機能です．
KubeVirtは仮想マシンをコンテナと同様にスケジューリングするため，
コンテナ内でQEMU/KVM仮想マシンを起動します．
本研究では，このアーキテクチャに起因するKubeVirtの性能オーバヘッドや制限を評価しました．

本研究の主要な成果として，KubeVirtが物理マシンのNUMAトポロジを考慮しないため，
最大で60%程度の顕著な性能劣化が生じ，適切なチューニングが必要であることを示しました．
また，ライブマイグレーションにおいても問題が生じることを示しました．

本研究のスライドと発表ビデオは[こちら](https://sched.co/ke2r)からご覧になれます．
