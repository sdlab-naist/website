---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Students from our laboratory presented their research at SES 2024"
subtitle: ""
summary: ""
authors: ["Shun Fujita"]
tags: ["Software Test","Techinical Debt"]
categories: []
date: 2024-09-20T17:33:10+09:00
lastmod: 2024-10-07T00:00:00+09:00
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
Shun Fujita, Ibuki Nakamura, Tatsuya Shirai, and Riku Kato from our laboratory presented at the [Software Engineering Symposium 2024 (SES 2024)](https://ses.sigse.jp/2024/), held from September 17 to 19, 2024.

Nakamura presented in the General Paper Track on the topic, [“Towards an Empirical Investigation into Self-Admitted Technical Debt in Test Code”](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=239243&item_no=1&page_id=13&block_id=8). His research focused on the distribution and types of SATD (Self-Admitted Technical Debt) in test code. He revealed that various types of SATD exist in test code, and certain SATD unique to test code that have not been covered in previous research were identified.

Fujita presented in the Previously Published Paper Track on ["An Empirical Study on the Use of Snapshot Testing"](https://ieeexplore.ieee.org/document/10336316). This research was previously presented at ICSME 2023. His study investigated how snapshot testing, widely used in development frameworks such as React, is utilized. By analyzing approximately 1,500 repositories collected from GitHub, he discovered that (1) projects utilizing both snapshot testing and unit testing employ more tests than those using only unit tests, and (2) in 8.2% of commits, snapshot files were modified, often accompanied by changes in a large number of other files.

Shirai presented in the Poster Presentation Track on “An Examination of the Relationship Between Fuzzing Coverage and Vulnerability Detection”. His research investigates the relationship between fuzzing coverage and vulnerability detection in software testing. The presentation reported that (1) there is no correlation between the number of fuzzing runs and coverage, and (2) there is an inverse correlation between coverage and the vulnerability detection rate.

Kato presented in the Poster Presentation Track on “A Study on Vulnerability Prediction Using Continuous Fuzzing Data”. His research proposes a method to detect vulnerable code at the point it is added to the repository by utilizing fuzzing data. In this presentation, he reported how long it took for the fuzzer to detect vulnerabilities.

![](fujita.jpg)
![](kato.jpg)
![](shirai.jpg)
