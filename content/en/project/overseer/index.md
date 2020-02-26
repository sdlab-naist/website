---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Overseer: SDN-Assisted Bandwidth and Latency Aware Route Optimization based on Application Requirement"
summary: ""
authors: ["kohei-ichikawa"]
tags: []
categories: []
date: 2020-02-17T23:49:29+09:00

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

Bandwidth and latency are two major factors that contribute the most to
network application performance. Between each pair of switches in a network,
there may be multiple paths connecting them. Each path has different proper-
ties because of multiple factors. Traditional shortest-path routing does not
take this knowledge into consideration and may result in sub-optimal
performance of applications and underutilization of the network. We propose a
concept of “bandwidth and latency aware routing”. The idea is that we could
improve overall performance of the network by separating application into
bandwidth- oriented and latency-oriented application and allocate separate
route for each type of application accordingly. We also proposed a design of
this network implemented with OpenFlow as well as Overseer, a reference
implementation. Routes are calculated based on monitored information using
Dijkstra algorithm and its variation. To demonstrate possible application of
bandwidth and latency aware network, integration with MPI is employed as an
example. To evaluate eligibility, feasibility and practicality of this work,
we tested Overseer with emulated environment, controlled virtual environment
and real world global-scale environment. Compared with traditional routing,
bandwidth and latency aware routing increase overall bandwidth and reduce
overall latency significantly in network with congestion.
