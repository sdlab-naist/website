---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "A Hybrid Game Contents Streaming Method to Improve Graphic Quality Delivered on Cloud Gaming"
summary: ""
authors: ["kohei-ichikawa"]
tags: []
categories: []
date: 2020-02-17T23:59:25+09:00

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

## Background

In recent years, Cloud Gaming, also regarded as gaming on demand, is an emerging gaming service that envisions a promising future of providing million clients with novel and highly accessible gaming experiences, as it has been an active topic both in industries and research fields recently. Compared to Online Game which only stores game status, Cloud Gaming takes more advantages of cloud infrastructures by leveraging reliable, elastic and high-performance computing resources. In its simplest form, it shifts intensive workloads of game processing from client’s device to powerful Cloud server. As shown in Figure 1, within Cloud Gaming, the actual interactive gaming application is stored at the Cloud server and gets executed once requested. The 3D-rendered game scenes are then streamed back to client’s device as encoded video sequence over a network with sufficient bandwidth, such as 5Mbits/s recommended by OnLive. At client’s side, control events input from devices such as mouse, keyboard, joystick are accurately recorded and sent from client’s device back to Cloud server for manipulation of game logics.

## Motivation

The on demand feature of Cloud Gaming benefits both clients and game developers by easing the possible incompatibility issues between gaming software and hardware environment that process the game. However, a challenging objective of developing a sustainable Cloud Gaming service is to maintain and improve user’s Quality of Experience (QoE). In general, interaction delay and graphic quality are two important criteria of influencing client’s QoE while playing video games locally. Significantly these two aspects are addressed more in Cloud Gaming, because network constraints play a critical role in affecting the system performance. Compared to general live video streaming, more rigid real-time responsiveness is demanded in Cloud Gaming in order to sustain good enough QoE, so currently most related researches focus on alleviating interaction delay. However, findings from a conducted subject test show that clients are sensitive to changes in graphic quality and smoothness during gameplay, as such implies that graphic quality notably affects QoE of Cloud Gaming as well.

As such, the primary goal of this research is to enhance graphic quality delivered on existing Cloud Gaming system. Especially we address the use case of client’s device, here refers to PC, for being rendering-capable to certain extent. Better graphic quality here refers to improvement over traditional Cloud Gaming streaming method by which the output quality is degraded from original.

Based on existing Cloud Gaming system, the proposed method is to also utilize available rendering power at client’s side for performing partial rendering tasks locally. The final output at client’s devices is represented by combining the contents streamed as encoded video and the locally rendered products which the original graphic quality is preserved. In addition, By distributing partial contents to client ́s device for local rendering, server workload is mitigated as well. Furthermore, the method is designed to maintain reasonable network load as well.

### Related Techniques

In general, the streaming methods used in Cloud Gaming system can be categorised into two main types: Image- based Streaming and Instruction-based Streaming. These two methods differ from each other in how the game contents are streamed from server to client.

- Image-based Streaming:
  - Mechanism: As shown in Figure 2, 3D graphics rendering are processed through de=dicated Graphic Processing Unit. The rendered game contents are then captured, encoded into video and streamed to client's device. Client's device takes the encoded video, decodes the contents and finally shows the corresponding frame on the display
  - Advantages:
    - Suitable to be streamed in general network environment.
    - Decoding can be processed by using low-cost decoder chips which are massively embedded in client's device. Therefore, it also indicates wide availability of service based on this method.
  - Disadvantages:
    - The graphic quality is degraded from original, may not meet client's rising demand of photo-realistic graphic quality.
- Instruction-based Streaming
    - Mechanism: As shown in Figure 3, after game logics are calculated at server, API calls to graphic library, for corresponding rendering are intercepted. The intercepted API functions, or referred as graphics commands, are then compressed and sent to client’s device. Together with the graphics commands, related 3D data such as geometry mesh and texture are streamed to client’s device as well. Soon after the arrival of the data, game rendering according to the received graphic commands is processed on-site at client’s device. Put simply, game logics are calculated at the server, while the corresponding game contents are rendered locally at client’s device.
    - Advantages:
      - Preserve the original quality of game contents.
    - Disadvantages:
      - Client's device needs to be well equipped, which indicates less availability of the service.

## Proposed Approach: Hybrid-Streaming System

The goal of this research is to enhance graphic quality based on the more preferred Cloud Gaming strucutre of Image-based Streaming. As such, our proposed solution is to integrate the mechanism of Instruction-based Streaming and take the advantages of it to achieve the desired improvement.

This Hybrid-Streaming System, which stands for utillizing both major Cloud Gaming streaming methods, distributes partial game data to be streamed as 3D graphics commands and rendered locally at client’s device, while keeping most rendering tasks to be processed at resourceful Cloud server and then streamed as video sequence. Graphic improvement is mainly contributed by the portion of game contents rendered at client’s device, while the system which is built upon the structure of Image-based Streaming maintains relatively high availability. Furthermore, by offloading partial rendering tasks to client’s device, server’s workload is mitigated as well.

System Structure Overview:
Figure 4 presents the overall structure of our Hybrid-Streaming System. The green boxes indicate the original data flow of Image-based Streaming which the Hybrid-Streaming system is based on, while the yellow boxes refer to the additional features for achieving the proposed Hybrid-Streaming System.
Within the system, how the final representation of game contents is correspondingly composed from the products of two different stream is an important design object, which largely depend on the way of splitting game contents at server. By comparing the depth value, all the objects are separated into two groups, the upper layer which contains shallower objects (closer to client’s view), and lower layer which contains deeper objects (further away from client’s view). Considering that the contents delivered through Image-based Streaming result in video frame without any depth factor, the game contents represented as this form should be treated as background. For this purpose, objects belonging to lower layer are streamed as video sequence, which undergoes the original process Image-based Streaming. On the other hands, objects belonging to upper layer are streamed as graphics commands. Therefore, as soon as the rendering operation is completed at the client side, the products can be overlaid on top of the background filled by the contents streamed as video sequence. The graphical representation of final product is indicated by Figure 5.

## Preliminary Evaluation

We implemented a prototype system based on the open source Image-based structure of GamingAnyWhere. The main purpose of the prototype is to simulate the outputs of our system which allows us to achieve the main goal of evaluating graphics quality. Furthermore, we also performed preliminary evaluation on the bandwidth usage and server workload, as we also compared the results with the Image-based Streaming approach. At current stage, we conducted the evaluation based on a simple interactive demo application for evaluations.
- Demo Application:
  The demo application is shown as below, as we also demonstrate how the contents are respectively distribute to server and client's device:

  We can also conveniently add more jet-fighter for additional test cases.
- Evaluation:
  Referring to previous researches related to cloud gaming, Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity (SSIM) are measured to evaluate graphic quality. Beside the primary goal of improving graphics quality, the hybrid streaming system is expected to reduce server workload as well since partial rendering tasks are offloaded to client’s device. Therefore, we also measured the respective workload at client's device and server. Furthermore, we also took measurement of incurred network traffic load since the system need to be a viable option in common broadband network environment.

## Results
All the measurement results are presented as below:

The quantitive results show that the implemented prototype of Hybrid-Streaming System achieve better graphic quality than GamingAnyWhere's state-of-art Image-based Streaming, while maintaining insignificant overhead during network streaming. Furthermore, the Hybrid-Streaming System also alleviates server's graphics processing workload by offloading rendering tasks to clinet's device.

## Future Work
Currently, the Hybrid-Streaming System is still at prototype stage, as more thorough investigation is needed to evaluate the Hybrid-Streaming System as a prospective Cloud Gaming platform. As future works, we plan to qualitatively evaluate the QoE of the system, as well as applying actual gaming softwares to conduct further testing. Moreover, we will continue to improve the applicability of the Hybrid-Streaming System by developing a more comprehensive framework.

Contact: If you have any question, please feel free to contact kar_long.chan.jr2[at]is.naist.jp

