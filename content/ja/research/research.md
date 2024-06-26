+++
# About widget.
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear in.

title = "研究トピック"
+++

{{< figure src="eyecatch.jpeg" title="" >}}
ソフトウェアシステムは現代社会にとって欠かせないものとなっています．ほとんどの企業がシステムを中心に経済活動を行うため，システムの優劣が企業の将来に大きな影響を与えるといっても過言ではありません．ソフトウェア設計学研究室では，安心安全なシステムを構築するソフトウェア技術を開発することで，社会に貢献できるように取り組んでいます．具体的には，ソースコード，テストコード，ネットワーク，インフラストラクチャなどの現代システムにおける必須要素を研究対象とし，設計や開発，品質管理，運用工程を効率化しています．
以下では，当研究室の研究を大きく2つに分け，紹介します．


## **ソフトウェア開発を支援するソフトウェア技術**
### [ソフトウェア開発を加速させるAI](/project/se4ai/)
ソフトウェア開発の高速化は年々進んでおり，その中心的な技術が人工知能（AI）を活用した開発工程の自動化です．例えば，身近な例で挙げると，[GitHub Copilot](https://github.com/features/copilot)のようにLLM（大規模言語モデル）を用いて，プログラミングの大部分をAIが代わりに代行する世界が近づいてきています．我々はプログラミング以外の工程でも，人工知能×ビッグデータ分析をフル活用して，これまで開発者が実施してきた工程を自動化して，ソフトウェア開発の更なる高速化を実現する研究に取り組んでおります．

### [NoOps (No Operation) を実現するソフトウェア開発自動化](/project/noops/)
質の高いソフトウェアをより短い期間でユーザーに提供するために，モダンなソフトウェア開発プロジェクトではDevOpsと呼ばれる，テストやリリースの自動化が行われています．例えば，ソフトウェア変更のたびに，コンパイルやテストなどを自動化する継続的インテグーションもその取り組みの一つです．当研究室では，DevOpsをさらに発展させ，不具合検出・修正や運用監視など，より広い範囲の運用の自動化により，人手が全く不要となるNoOpsの実現を目指しています．

### [ソースコードやプロジェクトのあるべき姿を追求するソフトウェアアナリティクス](/project/software-analytics/)
現代のソフトウェア開発では，Gitや，Pull request，不具合管理システムなど様々なシステム・ツールを駆使して，開発が効率化されています．これらのシステムを用いることで，開発データが蓄積していくため，いつ・だれが・どのような開発をしたのかを分析することが可能です．また，GitHubで公開されているリポジトリは，1億2800万を超えており，すべて分析が可能です．
ソフトウェアアナリティクスと呼ばれる分野では，これらの蓄積された膨大な公開データや提携企業のデータを分析し，ソフトウェア開発の個人やチームがより良い意思決定できるようにする事を目指してといます．当研究室でも，開発リポジトリから，機能実装やリファクタリング，テストなどのデータを取得し，開発者がどのような問題に会しているか，その問題はどう解決すべきかを，分析を通して追求しています．


## **計算機サービス全体のソフトウェア化技術**

### [クラウド基盤のためのソフトウェア](/project/cloud-computing/)
近年のクラウドコンピューティングの飛躍的な普及の背景には，ソフトウェア技術により計算機資源を仮想化することで，計算機環境の構築・割当を動的かつ自動的に実行できるようになってきたことが挙げられます．本研究では計算機資源をソフトウェアでもって制御する技術の研究を進めています．特に，ネットワークのソフトウェア制御技術であるSoftware Defined Networking (SDN) 技術を中心に，クラウドゲーミング，ビッグデータ解析，機械学習，IoTなど，クラウドコンピューティングを支えるためのソフトウェア技術を広くかつ深く追求しています．

### [HPCのためのソフトウェア](/project/high-performance-computing)
PC上では不可能な規模の計算を実現する高性能計算機（スーパコンピュータ）は，天気予報のように身近なところから，ビッグデータ解析や人工知能の研究開発に至るまで，幅広い領域において利活用されています．本研究では，数値計算，システムソフトウェア，ハードウェア等，異なる階層の計算機技術を垂直的に統合し，高性能計算機の性能を最大限に引き出すアプリケーションおよびミドルウェアを設計・開発しています．



その他，[こちら](/project/projects)でも各個別の研究を見ることが可能です．
