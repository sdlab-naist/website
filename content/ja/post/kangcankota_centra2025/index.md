---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "「CENTRA 2025 in Hsinchu, Taiwan における Ms. Kang Xingyuan、Mr. Papon Choonhaklai、および Mr. Kota Nakagawa の研究発表」"
subtitle: ""
summary: ""
authors: ["xingyuan-kang", "papon-choonhaklai", "kota-nakagawa"]
tags: ["Distributed SDN", "Inter-Communication Mechanism", "Consistency Model", "Disributed Datastore", "Information Synchronization","In-band Network Telemetry","SRv6","GPU sharing"]
categories: []
date: 2025-03-03T18:43:23+09:00
lastmod: 2025-03-03T18:43:23+09:00
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

Ms. Kang Xingyuan, Mr. Papon Choonhaklai, および Mr. Kota Nakagawa は、それぞれの研究を [CENTRA 2025 in Hsinchu, Taiwan (CENTRA 8)](https://www.globalcentra.org/centra8/) の Technical Paper セッションにおいて発表しました。

まず、Technical Paper セッションのオープニングスピーカーとして、Ms. Kang Xingyuan が Investigating the Impact of Data Storage Mechanisms on Distributed Software-Defined Networking Controllers Performance を発表しました。研究の詳細は以下のとおりです。

> Kang Xingyuan, Keichi Takahashi, Chawanat Nakasan, Kohei Ichikawa, Hajimu Iida, "Investigating the Impact of Data Storage Mechanisms on Distributed Software-Defined Networking Controllers Performance", CENTRA 2025, February 22–25, 2025.

本研究では、SDN（Software-Defined Networking）コントローラによるネットワーク情報の同期管理を効率化するため、さまざまなネットワークデータに適した一貫性モデルを探求しています。IoTデバイスの急増とデータトラフィックの増大に伴い、より高度なデータストレージおよび管理手法が求められています。分散型SDNは、分散ストレージとネットワーク制御機構を組み合わせることで、スケーラビリティと信頼性の向上を狙うアプローチです。広く採用されている SDN コントローラ ONOS では、Atomix という分散データストアと Raft 合意アルゴリズムにより、ネットワーク状態の一貫性を維持しています。しかし、ONOS/Atomix アーキテクチャにおける複雑な同期プロセスは、大規模ネットワークでレイテンシや効率の低下を引き起こす可能性があります。
本研究では、ONOS/Atomix における代替ストレージ機構を調査し、ネットワーク性能に与える影響を分析しました。Flow Setup Time (FST) モデルを用いて、さまざまなデータ一貫性モデルや同期戦略を比較・評価し、SDN コントローラの動作最適化を図っています。その結果、Atomix が強い一貫性を要求することで生じる課題や、同期頻度とシステム効率を両立する方策が示唆されました。データの保存および取得方法を改善することで、大規模ネットワークを扱う分散 SDN アーキテクチャの性能向上を目指す取り組みです。

![](mya.jpg)

<!-- Papon san's session -->
次に、Technical Paper セッションの2番目のスピーカーとして、Mr. Papon Choonhaklai が Reducing Overhead in Time-Sliced GPU Sharing with Dynamic MPS Partitioning in Kubernetes を発表しました。研究の詳細は以下のとおりです。

> Papon Choonhaklai, Kohei Ichikawa, Hajimu Iida, "Reducing Overhead in Time-Sliced GPU Sharing with Dynamic MPS Partitioning in Kubernetes", CENTRA 2025, February 22–25, 2025.

本研究では、Kubernetes 上で機械学習（ML）のワークロードを実行する際の GPU リソース管理の課題に注目しています。GPU のタイムスライシングは、1 つの GPU を複数の ML タスクで共有することにより、GPU の利用効率を高める一般的な方法です。しかし、大量の Pod が同時に稼働すると、頻繁に発生するコンテキストスイッチがオーバーヘッドとなり、スループットの低下や実行時間の増加を招く場合があります。
そこで本研究では、CUDA MPS (Multi-Process Service) を利用した動的 GPU パーティショニングを実現する Kubernetes Operator を提案しています。具体的には、Kubernetes Admission Webhook により、Pod の仕様に事前設定された CUDA のパーセンテージ値を自動的に注入し、ノード全体で一貫性のある GPU パーティショニングポリシーを実行可能にしました。この動的パーティショニングは Nebuly 社の GPU スケジューラ (nos) によって管理され、ワークロードに応じた最適な GPU リソース割り当てを実現します。実験結果からは、MPS を活用したアプローチにより、コンテキストスイッチングに起因するオーバーヘッドが削減され、従来のタイムスライシング手法に比べて合計実行時間が短縮されることが示されています。

![](papon.jpg)

<!-- Kota san's session -->
最後に、Mr. Kota Nakagawa が A Proposal of an Efficient Path Selection Method Using INT-Based Delay Measurement を発表しました。研究の詳細は以下のとおりです。

> Kota Nakagawa, Kohei Ichikawa, Hajimu Iida, "A Proposal of an Efficient Path Selection Method Using INT-Based Delay Measurement", CENTRA 2025, February 22–25, 2025.

本研究では、In-band Network Telemetry（INT）を活用した遅延計測に基づく最適パス選択手法を提案しています。従来のパス選択は、最短ホップ数に依拠することが多く、帯域幅や輻輳状況を十分に考慮していないため、必ずしも最も遅延が低い経路を選択できるとは限りません。
提案手法では、INT パケットを中間ノードで複製し、複数経路に送ることで効率的に遅延を測定し、最も遅延の低い経路を選択できるようにしています。この手法の効果を確認するため、Internet2 OS3E ネットワークトポロジを用いたシミュレーションを実施し、従来の OSPFv3 ベースのパス選択と比較を行いました。その結果、直接接続されているノードを除く 519 の送受信ノードペアのうち 73 ペアについて、提案手法がより低遅延の経路を選択できることが確認されました。

![](kota.jpg)