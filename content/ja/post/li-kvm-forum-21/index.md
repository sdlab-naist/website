---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Mr. Guoqing Li and Dr.Dario Faggioli's Collabrative Talk at KVM FORUM 2021"
subtitle: ""
summary: ""
authors: ["Guoqing Li"]
tags: ["Cloud Computing", "Virtualization Performance", "KubeVirt", "Kubernetes"]
categories: []
date: 2021-09-30T16:49:12+09:00
lastmod: 2021-09-30T16:49:12+09:00
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

Mr.Guoqing Li, a master student from SDLab and Dr.Dario Faggioli, a virtualization specialist from SUSE lab gave a joint [talk](https://youtu.be/x_czS9Iuo2o) on the topic of KubeVirt: The cost of Containerizing VMs at [KVM FORUM 2021](https://events.linuxfoundation.org/kvm-forum/).

KubeVirt is an add-on for Kubernetes to manage both containers and VMs in a unified manner. They evaluated the performance impact of resource usage accounting and limitation caused by container runtimes, as well as the achitectural limitation resulted from integrating QEMU/KVM into Kubernetes stack.

They showed that Kubevirt's limitation on configuring NUMA CPU topology can slow down the CPU performance up to 60%, and proper tunning can mitigate this CPU performance overhead to some degree but further improvement is needed since this will not only have the impact on theperformance, but can also lead to issues with live migrations.

The introduction and presentation slides of the talk is available at [here](https://events.linuxfoundation.org/kvm-forum/program/schedule/).
