---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Repository Mining"
summary: ""
authors: ["hajimu-iida"]
tags: ["Repository Mining", "Software Test", "Design Pattern", "Refactoring"]
categories: []
date: 2020-02-17T13:14:49+09:00

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

## Treasure digging in software development history -- Repository Mining

In this research, we aim at supporting software comprehension. By analyzing
and arranging software development history, we propose methods to present the
corresponding data. Especially, we focus on software repository which is our
major data source.

Software Repository refers to a development infrastructure that allows
developers to collaborate among others for software development via network.
It is also a collective term of version control system that manages source
code, as well as a mailing list management system that keeps track of
discussions among developers. Majorly used in Open Source Software, software
repository has been being practically applied in different software
developments. Within software repository, immensive amount of development
history data is stored. However, due to the enormous amount of data, it cannot
be fully utilized without any proper arrangement

By exploiting these data, the goal of this research field is to perform
integration that filters out irrelevant information and summarizes the
commons. Furthermore, we also aims at providing developers with useful
information in a comprehensible way. Such activities are called as Software
Repository Mining.

## Our on-going research topics:

- Analyzing the relationship between refactoring and bugs by using development history

  Refactoring refers to improving source code design without changing the
  behavior of the program. As the renowned pioneer of refactoring, Martin
  Fowler mentioned that performing refactoring can help to reduce bugs’ mixing
  into source code in his book. As such, this research aims at clarify such
  point by estimating the happening of refactoring from source code change log
  and comparing the results with the bug fix data stored in bug management
  system.
- A support environment for understanding code clone by using development history

  Code clone refers to the duplicated portion within source code. In this
  research, we aim at constructing an environment that presents the transition
  of code clone in a comprehensible way by utilizing the development
  history in version control system. [Click for more details (in
  Japanese)](/project/code-clone-history)．
- MUDABlue: System for automatically classifying software

  Massive number of software are registered in software repository. In this
  research, we aim at facilitating the reuse of software as well as
  communication between developers by providing mechanism that can discover
  similar software from software repository. [Click for more details (in
  Japanese)](/project/muda-blue).
- Extracting and Analyzing micro process

  For improving software process, it is mandatory to perform analysis not only
  at organization level, but also at individual level such as micro process.
  In this research group, based on the data collected from software
  development, we aim at extracting and analyzing micro process. {{% staticref
  "files/mpa_200802.pdf" "newtab" %}}Click for more details (in Japanese){{%
  /staticref %}}
- Analyzing Design Pattern by using history information

  Design Pattern refers to a set of reusable know-how which is accumulated
  from design stage in software development. Although it has been considered
  that software quality could be improved by applying design pattern, the
  actual case has not be clarified yet. Therefore, in this research project,
  we aim at revealing the relationship between usage of design pattern and
  software quality.
- Analyzing development project based on the co-occurrence information between developers

  In open source software development, project activity is a critical factor
  that largely influences the software quality. In this research group, by
  focusing on the mailing lists used in software development, we attempt to
  predict how the co-occurrence between developers may affect the project.
