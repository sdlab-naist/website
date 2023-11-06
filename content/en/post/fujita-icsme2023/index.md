---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Our internship student Shun Fujita presented his research at ICSME 2023"
subtitle: ""
summary: ""
authors: ["Yutaro Kashiwa"]
tags: ["Software Test"]
categories: []
date: 2023-11-05T16:05:10+09:00
lastmod: 2023-11-05T16:05:10+09:00
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
Shun Fujita, an internship student in our laboratory, presented his work at [the 39th IEEE International Conference on Software Maintenance and Evolution and Reengineering (ICSME 2023)](https://conf.researchr.org/home/icsme-2023). ICSME is considered one of top conferences in the software maintenance research field. He presented the following paper: 

> Shun Fujita, Yutaro Kashiwa, Bin Lin, and Hajimu Iida,
> "An Empirical Study on the Use of Snapshot Testing", In Proceedings of the 39th IEEE International Conference on Software Maintenance and Evolution, pp. 335--440, 2023.

This paper presents a preliminary study which examines how developers use snapshot tests. Snapshot testing is a type of output comparison testing technique that asserts whether the outputs by the current state of the product remain unchanged. Our result shows that (i) projects using both unit tests and snapshot tests have much more test cases than projects using only unit tests although they have similar numbers of unit tests; (ii) A non-negligible number of commits (8.2%) update the snapshot files, and co-changes with snapshots occur frequently. 

The paper is available on [GitHub](https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2023_Fujita.pdf).

![](image2.jpg)
