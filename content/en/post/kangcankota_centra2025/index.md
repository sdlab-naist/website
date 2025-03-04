---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Research Presentation by Ms. Kang Xingyuan, Mr. Papon Choonhaklai, and Mr. Kota Nakagawa at CENTRA 2025 in Hsinchu, Taiwan"
subtitle: ""
summary: ""
authors: ["xingyuan-kang", "papon-choonhaklai", "kota-nakagawa"]
tags: ["Distributed SDN", "Inter-Communication Mechanism", "Consistency Model", "Disributed Datastore", "Information Synchronization"]
categories: []
date: 2025-03-03T18:44:41+09:00
lastmod: 2025-03-03T18:44:41+09:00
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

Ms. Kang Xingyuan, Mr. Papon Choonhaklai, and Mr. Kota Nakagawa each presented thier individual research in the Technical Paper session at [CENTRA 2025 in Hsinchu, Taiwan (CENTRA 8)](https://www.globalcentra.org/centra8/).

First, as the opening speaker in Technical Paper session, Ms. Kang Xingyuan presented her research titled "Investigating the Impact of Data Storage Mechanisms on Distributed Software-Defined Networking Controllers Performance" to the audience. The details of her study are as follows:

> Kang Xingyuan, Keichi Takahashi, Chawanat Nakasan, Kohei Ichikawa, Hajimu Iida, "Investigating the Impact of Data Storage Mechanisms on Distributed Software-Defined Networking Controllers Performance", CENTRA 2025, February 22–25, 2025.

This research focuses on enhancing the efficiency of SDN controllers in managing network information synchronization by identifying suitable consistency models for different types of network data. The rapid expansion of IoT devices and the exponential growth of global data traffic necessitate advanced data storage and management solutions. Distributed Software-Defined Networking (SDN) has emerged as a promising approach, integrating distributed storage and network control mechanisms to enhance scalability and reliability. ONOS, a widely adopted SDN controller, employs the Atomix distributed datastore to maintain network state consistency using the Raft consensus algorithm. However, the complex synchronization processes in ONOS/Atomix architecture introduce latency and inefficiencies, particularly in large-scale networks. This study investigates alternative storage mechanisms within ONOS/Atomix, analyzing their impact on network performance. Leveraging the Flow Setup Time (FST) model, we evaluate different data consistency models and synchronization strategies to optimize SDN controller operations. Our findings highlight the challenges posed by Atomix’s strong consistency requirements and propose potential improvements for balancing synchronization frequency and system efficiency. By refining data storage and retrieval mechanisms, this research aims to enhance the performance of distributed SDN architectures in handling large-scale network demands.

![](mya.jpg)

<!-- Papon san's session -->

<!-- Kota san's session -->
Mr. Kota Nakagawa presented his research titled "A Proposal of an Efficient Path Selection Method Using INT-Based Delay Measurement" to the audience. The details of his study are as follows:

> Kota Nakagawa, Kohei Ichikawa, Hajimu Iida, "A Proposal of an Efficient Path Selection Method Using INT-Based Delay Measurement", CENTRA 2025, February 22–25, 2025.

In this study, we propose an optimal path selection method based on delay measurement utilizing In-band Network Telemetry (INT). Conventional path selection methods typically determine routes based on the shortest hop count. However, this approach does not take bandwidth or congestion conditions into account, and therefore, it does not necessarily select the lowest-latency path.In our proposed method, INT packets are duplicated at intermediate nodes and forwarded across multiple paths, enabling efficient delay measurement and allowing the selection of the lowest-latency path. To evaluate the effectiveness of our method, we conducted simulations using the Internet2 OS3E network topology and compared it with conventional OSPFv3-based path selection. As a result, our method successfully selected lower-latency paths in 73 out of 519 source-destination node pairs, excluding directly connected nodes.

![](kota.jpg)