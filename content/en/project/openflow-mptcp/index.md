---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Multipath TCP routing with OpenFlow"
summary: ""
authors: ["kohei-ichikawa"]
tags: []
categories: []
date: 2020-02-17T23:48:51+09:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Multipath TCP (MPTCP) is an extension to TCP that allows multiple TCP subflows to be created from a single application socket. This is done automatically by operating system kernel implementation, such as MPTCP Kernel. MPTCP has advantages over network layer and application layer multipathing. This is because MPTCP, unlike network layer mechanisms such as Equal-Cost Multipathing (ECMP), is capable of independent congestion control on multiple paths and therefore works well in unequal networks, which is the situation of PRAGMA-ENT. Also unlike application layer protocols, MPTCP is aware of network resources availability and can adjust data flow, scheduling, prioritization, and other factors. However, since MPTCP is a transport layer protocol, it has no control over the actual paths taken in the network. This can limit performance when many subflows go through the same route as a result of multipath-unaware routing.

## Objectives

Our objective is to design and develop a software-defined network (SDN) solution to achieve true multipath routing for MPTCP by independently routing multiple subflows through multiple paths.

Other possible actions that we are considering include developing and maintaining a ROCKS roll. While an alternative-kernel roll is more complicated compared to others, it is possible. Rolling MPTCP kernel for ROCKS can make MPTCP more widely used by existing ROCKS users and administrators.

We currently have developed a very simple topological algorithm and implemented it into a POX-based controller, Simple Multipath OpenFlow Controller (smoc).

## Architecture of smoc

{{< figure src="mptcp_fig_controller_blocks.png" title="Architecture of smoc" >}}

smoc is based on POX, a Python OpenFlow framework. The basic functions such as topology management and controller-switch communication are based on Overseer.

smoc itself contains two parts: The first part is path calculation & selection algorithm which expands on shortest-path to provide additional paths. These additional paths are ranked. The controller will use paths with least edges shared with the shortest path first to make sure that we are not overloading a specific link. In case of a tie, the shorter path is preferred. The second path is MPTCP subflow detection and group management. It takes form of a small run-time database inside smoc that keeps track of all MPTCP instances and their subflows to support the algorithm in the first part.

In current development we are creating an independent monitoring and reporting module that strives to be simple and can be quickly adapted for use with other networks in PRAGMA.

## Current Progress

{{< figure src="mptcp_fig_e_hosts.png" >}}
{{< figure src="mptcp_plot_e.png" >}}

We have achieved a topological routing algorithm. While this works very well in data centers or LANs, it does not fare very well on WANs such as PRAGMA-ENT. Testing on LANs indicated that smoc can quickly take advantage of the network and achieve maximum throughput. On the other hand, in PRAGMA-ENT, smoc takes a long time to achieve higher performance. We suspect that it is due to TCP congestion control mechanism.

We are currently investigating on how to further improve the performance of smoc in WANs by studying the effects of unequal bandwidth and latency.

## Publications

- Nakasan, C., K. Ichikawa K, H. Iida, P Uthayopas. "A simple multipath OpenFlow controller using topology-based algorithm for multipath TCP," in Concurrency and Computation: Practice and Experience. 2017, no. e4134. DOI: 10.1002/cpe.4134
- Nakasan, C., K. Ichikawa, P. Uthayopas. "Performance Evaluation of MPTCP over OpenFlow Network," in IPSJ SIG Notes 2014-HPC-145(30), 2014, pp. 1-6.

