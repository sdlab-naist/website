---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Students from our laboratory presented their research at ESEM2026."
subtitle: ""
summary: ""
authors: [ayane-shirakawa, suzuka-yoshimoto]
tags: ["Continuous Integration (CI)", "Test failures", "Empirical analysis", "Self-Admitted Technical Debt", "Test Coverage", "Software Testing"]
categories: []
date: 2026-10-14T17:31:06+09:00
lastmod: 2026-10-14T17:31:06+09:00
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
Mr. Shirakawa and Mr. Yoshimoto from our laboratory presented the following two papers at [The 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)](https://conf.researchr.org/home/eseiw-2026), held in Munich, Germany, in 2026.

ESEM is an international conference dedicated to empirical research in software engineering and is considered a top-tier conference; this year marks its 20th edition. For the technical paper track—which saw a 74% increase in submissions compared to the previous year—51 papers were accepted out of 269 submissions (an acceptance rate of 18.9%).

> Ayane Shirakawa, Tatsuya Shirai, Yutaro Kashiwa, Masanari Kondo, Yasutaka Kamei, Hajimu Iida,
> "Test Alert Snooze: An Empirical Study of Consecutive Test Failures on CI", In Proceedings of the 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)

Mr. Shirakawa presented the findings of this study, which aimed to clarify the realities of consecutive test failures in Continuous Integration (CI) and the associated developer behaviors. The study defined a "Test Alert Snooze" — the state in which the same test method fails across two or more consecutive revisions on CI — and empirically analyzed its occurrence rate, duration, and developer actions. The results showed that Test Alert Snooze occurred in 4 out of the 27 OSS projects studied (approximately 15%). A detailed analysis of these four projects revealed that 61.1% of the instances involved failures across two consecutive revisions, while 52.9% were resolved within one day. Furthermore, an analysis of developer behavior based on the classification of revisions using CSS types indicated a tendency for documentation to be modified while a Test Alert Snooze was active, whereas tests were more likely to be modified when the issue was resolved. ([LIPIcs.ESEM.2026.24](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.24))

> Suzuka Yoshimoto, Kosei Horikawa, Daniel Feitosa, Yutaro Kashiwa, Hajimu Iida,
> "Is Self-Admitted Technical Debt Tested? An Empirical Study of Coverage, Co-change, and Impact", In Proceedings of the 20th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)

Mr. Shirakawa presented the findings of this study. ([LIPIcs.ESEM.2026.36](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.36))