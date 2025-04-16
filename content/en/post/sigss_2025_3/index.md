---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Shirai and Mr. Kato presented their papers at the SIGSS in the Amami Oshima"
subtitle: ""
summary: ""
authors: ["Riku Kato"]
tags: ["Continuous fuzzing", "Just In Time"]
categories: []
date: 2025-03-12T15:13:22+09:00
lastmod: 2025-03-12T15:13:22+09:00
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
Tatsuya Shirai and Riku Kato from our laboratory presented at the [Technical Committee on Software Science (SS)](https://ken.ieice.org/ken/program/index.php?mode=program&tgs_regid=467a2ef7771c23683bb71c6ec6b3ca61a419e5c002fb2d05466b685a2ac8ce77&tgid=&layout=&lang=eng), held from March 10 to 12, 2025.

Mr. Shirai presented his paper titled ["Towards a Large-Scale Empirical Study on the Effectiveness of Continuous Fuzzing"](https://ken.ieice.org/ken/paper/20250312uc8r/). He discussed the impact of continuous fuzzing on vulnerability detection. The empirical study on OSS-Fuzz revealed that (1) a large number of vulnerabilities are detected in the initial stages of continuous fuzzing, and detection continues over time, (2) continuous fuzzing improves coverage as it progresses, and (3) the increase in coverage contributes to the detection of more vulnerabilities.

Mr. Kato presented his paper titled ["Proposal of Just-In-Time Vulnerability Prediction using Continuous Fuzzing"](https://ken.ieice.org/ken/paper/20250312Xc8u/). He proposed a "Just-In-Time vulnerability prediction" method using continuous fuzzing data, which demonstrated 5.4% to 13.6% higher performance in predicting vulnerabilities compared to conventional feature-based prediction methods, as revealed through experiments on 78 OSS projects.

