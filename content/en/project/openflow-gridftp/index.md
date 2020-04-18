---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "A Multipath Controller for Accelerating GridFTPTransfer over SDN"
summary: ""
authors: ["kohei-ichikawa"]
tags: ["Cloud", "SDN"]
categories: []
date: 2020-02-17T23:52:23+09:00

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

A large amount of scientific data needs to be transferred from one site to another as fast as possible in the computational science fields. High-speed data transfer between sites is very important, especially in the Grid computing field; GridFTP has been widely used for bulk data transfer over a wide area network. GridFTP achieves greater performance by supporting parallel TCP streams. Using parallel TCP streams improves the throughput of slow-start algorithms and lossy networks even on a single path. This research proposes a traffic engineering technique that increases the data transfer performance by using multiple paths simultaneously for the parallel TCP streams. For this purpose, we use SoftwareDefined Network (SDN) technology and its implementation, OpenFlow.

