---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Software for Cloud Computing"
summary: ""
authors: ["kohei-ichikawa"]
tags: []
categories: []
date: 2020-02-17T13:20:39+09:00

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

近年のクラウドコンピューティングの飛躍的な普及の背景には，ソフトウェア技術により計算機資源を仮想化することで，計算機環境の構築・割当を動的かつ自動的に実行できるようになってきたことが挙げられます．本研究では計算機資源をソフトウェアでもって制御する技術の研究を進めています．特に，ネットワークのソフトウェア制御技術であるSoftware Defined Networking (SDN) 技術を中心に，クラウドゲーミング，ビッグデータ解析，機械学習，IoTなど，クラウドコンピューティングを支えるためのソフトウェア技術を広くかつ深く追求しています．

## 取り組んでいる研究テーマ

### Software Defined Networking (SDN) に関する研究
計算資源をソフトウェア技術で仮想化し，計算機環境の構築・割当を動的かつ自動的に実行する仮想計算機技術 (VM: Virtual Machine) は確立されつつあります．オープンソースではKVMやXen，商用ではVMwareなどの基盤ソフトウェアが普及し，誰もがクラウド環境を構築できるようになってきました．一方で，次のステップとしてはネットワークの仮想化が注目されています．ネットワークもソフトウェアによって設定・割当を動的かつ自動的に実行することができるようになれば，利用者の要求に応じてネットワークを提供でき，それをクラウドの計算機と統合できれば，より最適な計算機環境を構築できると考えられています．そのような環境を実現する技術のコンセプトとして，近年，Software Defined Networking (SDN)という概念が提唱され始めています．その名のとおり，ソフトウェアでもってネットワークを定義するという概念です．SDNでは，Programmable Networkingという概念を提案し，ネットワークをプログラムできるような環境の構築を目指しています．

本研究室は，SDNの研究アイデアを地球規模に分散する大規模なネットワークで検証可能とする実証研究ネットワークを構築・運用するための国際プロジェクト，PRAGMA-ENT (Experimental Network Testbed) ，を率いており，学生が考えたアイデアを直ぐに国際ネットワーク環境で実証し，分析・評価する環境を有しています．詳しくはこちらのプロジェクトページをご覧ください．
また，本プロジェクトに関する[NICTのインタビュー記事](https://testbed.nict.go.jp/interview/005_1.html)もご参照ください．

関連論文：
- Kohei Ichikawa, Pongsakorn U-chupala, Che Huang, Chawanat Nakasan, Te-Lung Liu, Jo-Yu Chang, Li-Chi Ku, Whey-Fone Tsai, Jason Haga, Hiroaki Yamanaka, Eiji Kawai, Yoshiyuki Kido, Susumu Date, Shinji Shimojo, Philip Papadopoulos, Mauricio Tsugawa, Matthew Collins, Kyuho Jeong, Renato Figueiredo, and Jose Fortes, "Pragma-ENT: an International Sdn Testbed for a Cyberinfrastructure in the Pacific Rim," Concurrency And Computation: Practice And Experience, e4138 March 2017.

### Application-aware Routingに関する研究
近年，ネットワークを利用するアプリケーションは映像配信であったり，チャット・SNSであったり，Web閲覧であったり，多岐に渡ります．ただ，現状のネットワークのルーティングはアプリケーションに応じて最適化して設計されているわけではなく，送信元と送信先のみで経路が決まり，効率的であるとは言えません．Application-aware Routing技術ではSDN技術を活用し，アプリケーションごとに最適な経路を選択できるようにする技術を研究開発しています．詳しくは[こちら](/en/project/overseer)．

### Multipath Routingに関する研究
ネットワークの送信元と送信先を結ぶ経路は代替路を含めると通常複数存在します．しかし，現状のネットワークルーティングではこれら複数のパスを同時に活用することはなく，一つのアプリケーションは通常一つの経路しか選択できません．Multipath Routing技術ではアプリケーションから生成される複数のTCP通信を複数の異なる経路に分散することでネットワークのパフォーマンスを最大化する研究開発をしています．複数のTCP通信を発生させる仕組みとして，OSのTCP通信ライブラリのレベルで実施するMPTCP技術，アプリケーションの独自実装で複数TCP通信を行うアプリケーションレベルの双方において研究開発しています．詳しくは[こちら](/en/project/openflow-gridftp)と[こちら](/en/project/openflow-mptcp)．

### SDNによるネットワークのモニタリング・分析に関する研究
SDN技術によって，ネットワークはより詳細にモニタリング可能となります．上述のApplication-aware Routingを実現しようとすると，どういった性質の通信を行うアプリケーションがどのように通信を行っているのかより詳細に知る必要があります．本研究では，大規模なパケットキャプチャデータベースをディープラーニング等の機械学習技術で解析・分類することで，ネットワーク上のアプリケーションの通信をSDNで効率的に分類する手法を研究開発しています．

### SDNのためのソフトウェア工学に関する研究
Programmable Networkingの概念の下，プログラムで制御できるようになったネットワークでは，ソフトウェアの役割は非常に重要なものとなってきています．SDNを実現するプログラム開発自身にも既存のソフトウェア工学で培われてきた技術を適用するべきですが，現在のところまだ十分に環境が整っているとは言えません．本研究では，SDNのプログラムを効率よく開発するためのソフトウェア工学的な支援技術を研究開発しています．

### クラウドゲーミングに関する研究
クラウドによってストレージや計算サービスの提供が普及しつつありますが，近年はこれらの実用サービスに加えて，エンターテイメント関連サービスのクラウド化も進みつつあります．クラウドゲーミングはクラウドのサーバ上でゲームを実行し，利用者はネットワークさえあればいつでも，どこでも高品質なグラフィックスのゲームを利用可能とするものです．本研究では，このクラウドゲーミングの仕組みを改善し，高品質なグラフィックスを提供可能なフレームワークやVR (Virtual Reality) ゲームのクラウド化における問題解決に関して研究開発しています．詳しくは[こちら](/en/project/cloud-gaming/)
