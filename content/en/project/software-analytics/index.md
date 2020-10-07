---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software Analytics"
summary: ""
authors: ["hajimu-iida"]
tags: ["Software Analytics", "Code Clone", "Refactoring", "Programming Education", "Software Test"]
categories: []
date: 2020-02-17T13:17:13+09:00
weight: -80

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

## What is Software Analytics

Software analytics aims at helping individual or team to make better decision
in software development. For this reason, software-related data such as source
code or development history is analyzed. Afterwards, the corresponding result
is provided in a way that can be shared among individual or team.

- Reference Work：Tim Menzies, Thomas Zimmermann. "Software Analytics: So
  What?". In Journal IEEE Software archive Volume 30 Issue 4, July 2013 Pages
  31-37.

## Our current Research Topics

### Keyword: Code Clone

Code Clone refers to the duplicated portions within program source code. As a
research example, please refer to [Code Clone Origin Analysis Using Version
Control System](/project/code-clone-history) (The goal of this work is to
construct an environment that could present the transition of code clone in a
comprehensible way by analyzing development history managed by version control
system).

Other related research:

- Investigation into the Defect Occurrence Based on Positional Relationship
  between Code Clone and Clone Fragment
- Investigation into the Effect of Positional Relationship between Code Clone
  and Code Fragment on Defect Occurrence
- Investigation for Code Clone in Hardware Description Language

### Keyword: Refactoring

Refactoring refers to improving source code design without changing the
behavior of the program. As the renowned pioneer of refactoring, Martin Fowler
mentioned that performing refactoring can help to reduce bugs’ mixing into
source code in his book. As such, this research aims at clarify such point by
estimating the happening of refactoring from source code change log and
comparing the results with the bug fix data stored in bug management system.

Other related research:

- Investigating the Characteristics of  Method Extract Cases by Using Process
  Metrics
- An Approach for Fine-Grained Detection of Refactoring Instances Using
  Repository with Syntactic Information
- Recommending Extract Method Opportunities Using Machine Learning
- Survey of Refactoring Detection Techniques Based on Change History Analysis
- Methods for Empirical Analysis and Evaluation of Refactoring Instances

### Keyword: Programming Education


- Investigating build errors in software development PBL
- Using snapshot to specify points of blockage in programming exercise
- Pockets: An Exploratory Programming Support Environment for Introductory
  Programming Exercises
- Detecting Exploratory Programming Behaviors for Introductory Programming
  Exercises
- Investigating the Model of Automatically Detecting Exploratory Programming
  Behaviors
- An Investigation into the Behavior of the Novice Programmers Based on Build
  Histories in Software Development Practice
- A System to Support Understanding of  Programming Behavior in Exploratory
  Programming by Novices

### Other research for software analytics

- MUDABlue: System for automatically classifying software

  Massive number of software are registered in software repository. In this
  research, we aim at facilitating the reuse of software as well as
  communication between developers by providing mechanism that can discover
  similar softwares from software repository. [Click for more details (in
  Japanese)](/project/muda-blue)．
