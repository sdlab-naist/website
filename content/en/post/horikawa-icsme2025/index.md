---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Horikawa's research presentation at ICSME2025"
subtitle: ""
summary: ""
authors: [kosei-horikawa]
tags: ["Refactoring", "Code Metrics", "Code Readability", "Code Smell", "Mining Software Repository"]
categories: []
date: 2025-09-22T10:45:00+09:00
lastmod: 2025-09-22T10:45:00+09:00
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
Kosei Horikawa from our laboratory, presented his work at [The 41st IEEE International Conference on Software Maintenance and Evolution (ICSME 2025)](https://conf.researchr.org/home/icsme-2025). ICSME is considered one of top conferences in the software maintenance research field. He presented the following paper: 

> Kosei Horikawa, Yutaro Kashiwa, Bin Lin, Kenji Fujiwara, and Hajimu Iida,
> "How Does Test Code Differ From Production Code in Terms of Refactoring? An Empirical Study", In Proceedings of the 41st IEEE International Conference on Software Maintenance and Evolution, pp. 779--784, 2025.

This research investigates how the impact of refactoring differs between production code and test code. We collected 455 Java projects from GitHub and analyzed a total of 6.7 million refactoring instances. The analysis revealed that: (i) refactoring in production code focuses on structural improvements (such as API-level changes), whereas in test code, it centers on method renamings and test-specific operations to improve readability; and (ii) while refactoring improves the readability of both production and test code, metrics such as lines of code and complexity tend to decrease in production code but increase in test code.

The paper is available on [GitHub](https://github.com/Mont9165/ProdTestRefactoringAndMetrics/blob/main/How%20Does%20Test%20Code%20Differ%20From%20Production%20Code%20in%20Terms%20of%20Refactoring%3F%20An%20Empirical%20Study.pdf).

![](image2.jpg)
