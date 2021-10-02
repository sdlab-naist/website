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
Virtual Machines (VMs) are used extensively in the cloud. The underlying hypervisors allow hardware resources to be split into multiple virtual units which enables server consolidation, fault containment and resource management. However, VMs with traditional architecture introduce heavy overhead and reduce application performance. Containers are becoming popular options for running applications, yet such a solution raises security concerns due to weaker isolation than VMs. We are at the point of container and traditional virtualization convergence where lightweight hypervisors are implemented and integrated into the container ecosystem in order to maximize the benefits of VM isolation and container performance. However, there has been no comprehensive comparison among different convergence architectures. To identify limitations and best fit use cases, we investigate the characteristics of Docker, Kata, gVisor, Firecracker and QEMU/KVM by measuring the performance of disk storage, main memory, CPU, network, system call, and startup time. In addition, we evaluate their performance of running the Nginx web server and the MySQL database management system. We use QEMU/KVM as an example of running traditional VMs, Docker as the standard runc container, and the rest as the representatives of lightweight hypervisors. We compare and analyze the benchmark results, discuss the possible implications, explain the trade-off each organization made, and elaborate on the pros and cons of each architecture.

## Emerging solutions that provides better isolation - gVisor and Kata Containers

{{< figure src="gVisor.png" title="gVisor Architecture" width="80%">}}

gVisor is a container sandbox developed by Google. It shipped with a user space kernel - Sentry, acting like a lightweight hypervisor which provides an isolation boundary between applications and host kernel. Sentry is the application kernel that implements substantial portion of the Linux system interface by using a limited set of system calls. gVisor uses ptrace to intercept the system calls from applications. KVM can also be used to trap system calls at hardware level to boost virtualization performance. System calls invoked from the Sentry are further filtered using seccomp. File I/O is handled by a separate file proxy process - Gofer, which communicates with the Sentry through the 9P protocol.

{{< figure src="kata.png" title="Kata Container Architecture" width="80%">}}

Kata container is a collaboration between the Intel Clear Linux project and hyper.sh projects. It is an example of a container and virtualization convergence technology that allows users to run containers inside lightweight VMs. It has been seamlessly integrated into the containerd system using a shim, named containered-shim-kata-v2. The virtualization part is based on QEMU/KVM to enable hardware assisted virtualization, and a highly optimized guest kernel includes the functionalities to run only container workloads. The customized kernel is optimized to reduce boot time and memory footprint, and a minimal root file system based on Clear Linux reduces attack surface significantly by removing many of the binaries commonly found in general purpose Linux distributions. The only two processes running inside of the VM at startup are systemd and a kata agent. The containerd-shim-kataand kata agent communicates across a VSOCK socket.

Our study covered several prominent lightweight hypervisors backed by Docker, Amazon, Google and Intel. We identified a number of bottlenecks that affect virtualization performance and elabrated the trade offs made by each organization. The pros and cons of each system are discussed in detail and some limitations that could be potentially addressed in the future are also mentioned. It is evident that the current architectural trend of lightweight hypervisors tends to march forward a new era and lightweight VMs have the potential to supplant traditional VMs. However, lightweight hypervisors have not reached the point to become a mature alternative, and thus traditional VMs would still be the preferred options for many organizations. Kata is on the right track to earn the title of having the security of a VM and offering the performance of a container. Future research on reducing the memory footprint of lightweight hypervisor based containers would be practical. A research conducted by NEC Lab using optimized [Xen hypervisor with customized unikernels](https://dl.acm.org/doi/pdf/10.1145/3132747.3132763) opens the possibility of creating lighter and safer VMs than containers which is an exicting research worth looking into.

## Publication
- Guoqing Li, Keichi Takahashi, Kouhei Ichikawa, Hajimu Iida, Pree Thiengburanathum, Passakorn Phannachitta, “Comparative Performance Study of Lightweight Hypervisors Used in Container Environment”, 11th International Conference on Cloud Computing and Services Science (CLOSER 2021), Apr. 2021.
