---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "An Interactive Monitoring Tool for OpenFlow Networks (Opimon)"
summary: ""
authors: [Wassapon Watanakeesuntorn]
tags: ["SDN"]
categories: []
date: 2020-10-05T14:00:24+09:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Architecture of Opimon"
  focal_point: ""
  preview_only: false

---

Software Defined Network (SDN) is an another approach to networking that realizes network programmability and dynamic control over the network. OpenFlow is a de facto standard protocol used to implement an SDN. However, understanding the dynamic behavior of an OpenFlow network is challenging since the information about the operation is distributed across numerous network switches. Opimon (OpenFlow Interactive Monitoring) is developed for monitoring and visualizing the network topology and flow tables of switches in real-time. Furthermore, it analyzes network traffic to detect DDoS attacks. A web-based user interface enables users to quickly understand network behavior and identify problems.

## Design and Implementation

Opimon is composed of three main modules: (1) monitoring module, (2) visualization module, and (3) security analysis module.

The monitoring module is designed to monitor the control plane in the network for collecting the routing of the flows and status of the switches. Opimon acts as a proxy between the OpenFlow controller and OpenFlow switches. This design allows Opimon to monitor the network without changing the implementation of the controller and the switches. The visualization module is designed for assisting the network administrators to easily understand the behavior of the monitored OpenFlow network. Opimon shows the status of the network on a single web interface. 

The security analysis module is designed to detect issues in the network and protect the network from attackers. This module uses machine learning techniques for analyzing the traffic collected from the data plane and control plane. Currently, we conducted a preliminary research to compare the performance of SVM and deep learning to detect DDoS attack on DARPA dataset.

## Evaluation

We evaluate the monitoring tool of Opimon by deploy the Opimon on a real OpenFlow network testbed, [PRAGMA Experimental Networking Testbed (PRAGMA-ENT)](http://www.pragma-grid.net/projects/ent/). This testbed is built and used by the Pacific Rim Application and Grid Middleware Assembly (PRAGMA) researchers.

{{< figure src="opimon_pragma-ent.png" title="Opimon monitor on PRAGMA-ENT Network" >}}

The figure shows the network status of PRAGMA-ENT which monitored with Opimon. The Opimon showed the topology of the PRAGMA-ENT network correctly, include with connection status on the network due to some connections are unidirectional link.

The preliminary result of machine learning algorithm for the problem of DDoS attack detection has been addressed. Two algorithms, Support Vector Machine (SVM) and Deep Feed Forward (DFF) were compared in terms of classification accuracy and computing time. It was found that DFF can classify the data with a higher accuracy compared to SVM. Therefore, deep learning is a useful choice for the classification of DDoS attack packets in terms of accuracy. However, SVM is an appropriate choice for faster classification.

## Future Work

We are working on reducing the overhead of the monitoring as much as possible. The high overhead incurred by the monitoring tool may cause problems to the monitored network, such as high latency of the communication between OpenFlow switches and OpenFlow controller. This optimization should help the monitoring tool to forward the messages between the controller and switches quicker and make the overall network faster.

Regarding DDoS detection, the preliminary experiment was conducted for comparing to choose a suitable machine learning technique to detect DDoS attack in real-time. For the next step, we will apply a machine learning on the security analysis server in Opimon for detecting the attack traffic in the OpenFlow network.

## Publication
- W. Wassapon, P. Uthayopas, C. Chantrapornchai and K. Ichikawa, "Real-time monitoring and visualization software for OpenFlow network," 2017 15th International Conference on ICT and Knowledge Engineering (ICT&KE), Thailand, November 2017, pp. 1-5, DOI: [10.1109/ICTKE.2017.8259622](https://ieeexplore.ieee.org/abstract/document/8259622).

- W. Watanakeesuntorn, K. Ichikawa, H. Iida, “A proposal of a real-time OpenFlow DDoS detection tool,” 研究報告インターネットと運用技術（IOT）, Vol. 2018-IOT-40, No. 34, March 2018, pp. 1-4, http://id.nii.ac.jp/1001/00186184/.

- P. Khuphiran, P. Leelaprute, P. Uthayopas, K. Ichikawa and W. Watanakeesuntorn, "Performance Comparison of Machine Learning Models for DDoS Attacks Detection," 2018 22nd International Computer Science and Engineering Conference (ICSEC), Thailand, November 2018, pp. 1-4, DOI: [10.1109/ICSEC.2018.8712757](https://ieeexplore.ieee.org/document/8712757).

- W. Watanakeesuntorn, "An Interactive Monitoring Tool for OpenFlow Networks," Master's Thesis, Nara Institute of Science and Technology, Japan, September 2019, https://library.naist.jp/mylimedio/search/av1.do?target=local&bibid=92478.