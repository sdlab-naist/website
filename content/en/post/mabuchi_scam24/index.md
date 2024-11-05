---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Mabuchi presented his research at SCAM 2024"
subtitle: ""
summary: ""
authors: ["Yasuhito Morikawa"]
tags: ["Docker", "Preprocessors"]
categories: []
date: 2024-11-05T12:27:13+09:00
lastmod: 2024-11-05T12:27:13+09:00
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
Wataru Mabuchi, an M2 student in our laboratory, presented the following paper at [The 24th International Conference on Source Code Analysis & Manipulation(SCAM2024)](https://conf.researchr.org/home/scam-2024) on Oct 7th-8th, 2024.

> Wataru Mabuchi, Yutaro Kashiwa, Kenji Fujiwara, Hajimu Iida: "An Empirical Investigation Into the Use of Dockerfile Preprocessors for Docker Image Management", In Proceedings of The 24th Source Code Analysis and Manipulation (SCAM2024), Oct. 2024.

[This study]() conducted an empirical investigation into the use of Dockerfile Preprocessors (DPP), a set of scripts designed to generate Dockerfiles compatible with multiple environments.

We collected and analyzed 146 Docker official images from GitHub projects, and we found
- DPP projects support more images and release more frequently than non-DPP projects
- The adoption of DPP reduces the effort of creating Dockerfiles, but might not facilitate releases or commit activities.