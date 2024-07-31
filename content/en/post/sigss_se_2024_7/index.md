---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Ms. Watanabe, Mr.Fujita, Mr.Horikawa and Mr.Kano presented their paper at the SIGSE/SIGSS workshop in Hokkaido"
subtitle: ""
summary: ""
authors: ["Shun Fujita"]
tags: ["Refactoring","Software test","Techinical Debt"]
#todo
categories: []
date: 2024-07-31T21:00:00+09:00
lastmod: 2024-07-31T21:00:00+09:00
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
Ms.Watanabe and Mr.Fujita from SDlab presented at [SIGSE](https://www.ipsj.or.jp/kenkyukai/event/se217.html) and Mr.Kano and Mr.Horikawa from SDlab presented at [SIGSS](https://ken.ieice.org/ken/form/index.php?tgs_regid=2fc4be9075af971c827c62a8a625c209fee16e014a7c586bb466c9d8c814fa1c&cmd=info), both held on July 25th-27th, 2024 in Hokkaido.


<!-- SE研究発表会（SIGSE）はソフトウェア開発に関する理論から実践までの幅広い諸問題について，研究・開発の成果や経験を発表し，討論することで相互に理解を深めることを目的とした研究会です． -->
<!-- sigss -->

Ms. Watanabe presented her paper titled ["Investigating the Impact of Shortening Release Cycle on Introduction and Resolution of Self-Admitted Technical Debt"](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=237361&item_no=1&page_id=13&block_id=8). She discussed the impact of adopting shortened release cycles on SATD, focusing on Eclipse. The analysis revealed that adopting shortened release cycles does not have a negative impact from the perspective of SATD.


Shun Fujita presented his paper titled ["Towards An Empirical Evaluation of Defect Detection Capability in Snapshot Testing"](https://ipsj.ixsq.nii.ac.jp/ej/index.php?active_action=repository_view_main_item_detail&page_id=13&block_id=8&item_id=237362&item_no=1). He conducted a survey targeting repositories that adopt snapshot testing on GitHub and revealed that snapshot testing can detect defects that other tests cannot detect.

Mr. Horikawa presented his paper titled ["Toward Investigating the Impact of Test-Specific Refactoring"](https://ken.ieice.org/ken/paper/202407269c3d/). He discussed the frequency, types, and impact of refactoring specific to test code in actual OSS development. The study revealed new findings on test code-specific refactoring, not covered in existing research, and its relationship with test smells (issues that lead to a decline in test quality).

Mr. Kano presented his paper titled ["Toward Investigation into the Relationship between Test Quality and Production Code Design"](https://ken.ieice.org/ken/paper/20240726fc3d/). He discussed the relationship between the design of production code and test quality, investigating at a finer granularity of method-level relationships compared to previous research. The study revealed the co-occurrence of low-quality test methods and low-quality production methods.

![](fujita.jpg)
![](horikawa.jpg)
![](kano.jpg)

