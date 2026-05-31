---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Students from our laboratory presented their research at MSR 2026"
subtitle: ""
summary: ""
authors: [kan-watanabe, suzuka-yoshimoto, kosei-horikawa, tatsuya-shirai]
tags: ["AI Agent", "Code Generation", "Software Test", "Code Readability", "Fuzzing", "Mining Software Repository"]
categories: []
date: 2026-05-29T12:00:00+09:00
lastmod: 2026-05-29T12:00:00+09:00
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
Members of our laboratory attended the [48th IEEE/ACM International Conference on Software Engineering (ICSE 2026)](https://conf.researchr.org/home/icse-2026), held in Rio de Janeiro, Brazil from April 12 to 18, 2026, and presented the following four papers at the co-located [22nd International Conference on Mining Software Repositories (MSR 2026)](https://conf.researchr.org/home/msr-2026). MSR is the premier conference in the field of mining software repositories.

> Kan Watanabe, Tatsuya Shirai, Yutaro Kashiwa, and Hajimu Iida,
> "What to Cut? Predicting Unnecessary Methods in Agentic Code Generation", In Proceedings of the 22nd International Conference on Mining Software Repositories (MSR 2026).

Mr. Watanabe presented this work, which tackles how reviewers can efficiently spot AI-generated functions that end up being removed during pull-request review. The study found that functions deleted for different reasons exhibit distinct characteristics, and the proposed prediction model identifies such unnecessary methods with an AUC of 87.1%, helping reviewers prioritize their effort. ([arXiv:2602.17091](https://arxiv.org/abs/2602.17091))

![poster session](kan.jpg)

> Tatsuya Shirai, Olivier Nourry, Yutaro Kashiwa, Kenji Fujiwara, and Hajimu Iida,
> "Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection", In Proceedings of the 22nd International Conference on Mining Software Repositories (MSR 2026).

This work empirically studies whether the programming language affects fuzzing bug detection, analyzing 61,444 fuzzing bugs across 559 open-source projects. The results show that the language significantly influences fuzzing behavior: C++ and Rust exhibit higher bug-detection frequencies, while Rust and Python expose fewer but more severe vulnerabilities, and crash reproducibility and patch coverage also vary notably by language. The presentation was given by Associate Professor Yutaro Kashiwa, the corresponding author, on behalf of Mr. Shirai. ([arXiv:2602.05312](https://arxiv.org/abs/2602.05312))

> Suzuka Yoshimoto, Shun Fujita, Kosei Horikawa, Daniel Feitosa, Yutaro Kashiwa, and Hajimu Iida,
> "Testing with AI Agents: An Empirical Study of Test Generation Frequency, Quality, and Coverage", In Proceedings of the 22nd International Conference on Mining Software Repositories (MSR 2026).

Ms. Yoshimoto presented this empirical study of how AI coding agents generate tests in terms of frequency, quality, and coverage. The study found that AI authored 16.4% of all commits that add tests, and that AI-generated tests tend to be longer with more assertions but lower cyclomatic complexity, while achieving code coverage comparable to human-written tests. ([arXiv:2603.13724](https://arxiv.org/abs/2603.13724))

![poster session](suzuka_msr2026.jpg)

> Kyogo Horikawa, Kosei Horikawa, Yutaro Kashiwa, Hidetake Uwano, and Hajimu Iida,
> "Do AI Agents Really Improve Code Readability?", In Proceedings of the 22nd International Conference on Mining Software Repositories (MSR 2026).

This work empirically investigates whether AI coding agents actually improve code readability, analyzing 403 readability-focused commits. Counterintuitively, the Maintainability Index decreased in 56.1% of the commits and Cyclomatic Complexity increased in 42.7%; although the agents concentrated on reducing logic complexity (42.4%) and improving documentation (24.2%), their refactoring often degraded traditional quality metrics. As the first author, Kyogo Horikawa, joined our laboratory as an internship student from National Institute of Technology, Nara College, the presentation was given on his behalf by Kosei Horikawa. ([arXiv:2603.13723](https://arxiv.org/abs/2603.13723))
