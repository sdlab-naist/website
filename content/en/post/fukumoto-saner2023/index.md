---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Mr. Fukumoto presented his research at SANER 2023"
subtitle: ""
summary: ""
authors: ["Daisuke Fukumoto"]
tags: ["Code Completion", "Deep Learning"]
categories: []
date: 2023-03-23T16:05:10+09:00
lastmod: 2023-03-23T16:05:10+09:00
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
Daisuke Fukumoto, M2 in our laboratory, presented the following paper at [the 30th IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER 2023)](https://saner2023.must.edu.mo/index) that took place on 21st-24th March 2023 in Macau. SANER is one of top conferences in the software engineering research field. SANER has been orginizsed by IEEE and had its 30th anniversary this year. 



> Daisuke Fukumoto, Yutaro Kashiwa, Toshiki Hirao, Kenji Fujiwara and Hajimu Iida, 
> "An Empirical Investigation on the Performance of　Domain Adaptation for T5 Code Completion", 30th IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER 2023), Mar. 2023.



In recent years, DL-based code completion techniques have been proposed. In particular, pre-trained models have shown outstanding performance because they can complete code by considering the context before and after it is completed. However, the models might not be able to select the most appropriate candidate that fits a specific project because many projects have their own coding rules. 
This paper investigated the performance of domain adaptation for code completion tasks to address this challenge. Domain adaptation is a technique to develop a suitable model for a specific domain, by fine-tuning a pre-trained model with additional data from a specific domain (e.g., a project). This technique has the potential to complete code optimized for a specific project, understanding their coding rules. 

Our experiment result demonstrated that fine-tuning with the dataset from a specific project fits the project and improves the code completion performance (i.e., 2.5% in the edit distance rate and 5.3% in the perfect prediction rate), rather than fine-tuning with the out-of-domain datasets. 
Also, our results showed that the larger repositories, the greater improvement due to domain adaptation. The result implies that domain adaptation is ineffective for small projects. 




![](image2.jpg)