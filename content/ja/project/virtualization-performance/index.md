---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Comparative performance study of lightweight hypervisors used in container environment"
summary: ""
authors: [Guoqing Li]
tags: ["Cloud", "Virtualization Performance", "Container Technology", "Lightweight Hypervisor", "isolation"]
categories: []
date: 2021-03-01T14:13:31+09:00

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
Virtual Machines (VMs) are used extensively in cloud computing. The underlying hypervisor allows hardware resources to be split into multiple virtual units which enhances resource utilization. However, VMs with traditional architecture introduce heavy overhead and reduce workload performance. Containers have been introduced to overcome this drawback, yet such a solution raises security concerns due to poor isolation. Lightweight hypervisors have been leveraged to strike a balance between performance and isolation. We conducted a comprehensive performance evaluation of containers based on modern lightweight hypervisors, elaborated on the limitations that affect virtualization performance, identified the best fit use case for practitioners and provided pros and cons analysis of each solution in great detail. We hope our study provides a guidance on how cloud infrastructure should be built and gives the community a better picture of the current technological trend.

## Emerging solutions that provides better isolation - gVisor and Kata Containers

{{< figure src="gVisor.png" title="gVisor Architecture" width="80%">}}

gVisor is a container sandbox developed by Google. It shipped with a user space kernel, acting like a lightweight hypervisor which provides an isolation boundary between applications and host kernel. Sentry is the application kernel that implements substantial portion of the Linux system interface by using a limited set of system calls. gVisor uses ptrace to intercept the system calls from applications. KVM can also be used to boost virtualization performance. System calls invoked from the Sentry are further filtered using seccomp. File I/O is handled by a separate process - Gofer, which communicates with the Sentry through the 9P protocol.

{{< figure src="Kata.png" title="Kata Container Architecture" width="80%">}}

Kata builds lightweight VMs which seamlessly integrate with the container ecosystem. It ships with a default hypervisor Kata-qemu, which is based on QEMU/KVM. Significant optimization effort has been made. Kata provides a customized guest kernel which reduces startup time and memory footprint. Each Kata container runs inside a dedicated lightweight VM to enforce strong isolation. 

Our study covered several prominent lightweight hypervisors backed by Docker, Amazon, Google and Intel. We identified a number of bottlenecks that affect virtualization performance and elabrated the trade offs made by each organization. The pros and cons of each system are discussed in detail and some limitations that could be potentially addressed in the future are also mentioned. It is evident that the current architectural trend of lightweight hypervisors tends to march forward a new era and lightweight VMs have the potential to partially replace traditional VMs. However, lightweight hypervisors have not reached the point to become a mature alternative, and thus traditional VMs would still be the preferred options for many organizations. Kata is on the right track to earn the title of having the security of a VM and offering the performance of a container. Future research on reducing the memory footprint of lightweight hypervisor based containers would be practical. A research conducted by NEC Lab using optimized [Xen hypervisor with customized unikernels](https://dl.acm.org/doi/pdf/10.1145/3132747.3132763) opens the possibility of creating lighter and safer VMs than containers which is an exicting research worth looking into.

## Publication
- Guoqing Li, Keichi Takahashi, Kouhei Ichikawa, Hajimu Iida, Pree Thiengburanathum, Passakorn Phannachitta, “Comparative Performance Study of Lightweight Hypervisors Used in Container Environment”, 11th International Conference on Cloud Computing and Services Science (CLOSER 2021), Apr. 2021.
