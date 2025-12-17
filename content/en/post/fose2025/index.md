---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Students from our laboratory presented their research at FOSE 2025"
subtitle: ""
summary: ""
authors: [tatsuya-shirai]
tags: ["Continuous Integration", "Automated Driving System", "Software Test", "Fuzzing"]
categories: []
date: 2025-11-08T07:02:47Z
lastmod: 2025-11-08T07:02:47Z
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
Tatsuya Shirai, Keitaro Ito, Ayane Shirakawa, and Kan Watanabe from our laboratory presented at the [32nd Workshop on Foundations of Software Engineering (FOSE2025)](https://fose.jssst.or.jp/fose2025/), taken place in Ehime prefecture from November 6-8, 2025.

Shirai presented "An Empirical Study on the Impact of Programming Languages in Fuzzing." This research focused on fuzzing, an automated software testing technique, and conducted a large-scale analysis of how the characteristics of different programming languages affect fuzzing results. The findings revealed significant differences between languages in terms of detected bug patterns and metrics such as coverage, demonstrating the importance of optimizing fuzzing methods according to language characteristics.

Ito presented "Construction of a Just-in-Time Safety Prediction Model for Autonomous Driving". Simulation testing is crucial for autonomous driving software development from a safety perspective, but it faces the challenge of being time-consuming. Therefore, this research constructed a model that predicts, at the commit level, how changes made to the software will affect safety. The results showed that the model could predict correctly with approximately a 40% probability, and demonstrated that, among the changes, the number of lines added and the number of lines deleted are more deeply involved in safety.

Shirakawa presented "Empirical Analysis of Consecutive Test Failures (Test Alert Snooze) in Continuous Integration." Existing research has not clarified the actual situation or causes of consecutive test failures in continuous integration (CI). Therefore, in this study, we defined consecutive failures of a test method as "test alert snooze" and empirically analyzed its characteristics. The results were shown in bar graphs and box plots for the percentage of test alert snoozes, the number of consecutive failures, and the correction time.

Watanabe presented in the Poster Presentation Track, titled “Towards Leveraging Program Invariant Changes for Just-In-Time Defect Detection.” Starting from the hypothesis that invariants could be used as dynamic features for JIT defect detection, he analyzed whether errors caught by test code could be detected through changes in invariants. The results confirmed, via box plots showing significant differences, that only bug-containing commits exhibited changes in the number of lines and characters of invariants.

![](shirai.jpg)

![](ito.jpg)

![](shirakawa.jpg)

![](watanabe.jpg)