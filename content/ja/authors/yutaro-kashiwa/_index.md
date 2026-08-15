---
# Display name
title: "柏 祐太郎"

# Username (this should match the folder name and the name on publications)
authors:
  - "yutaro-kashiwa"

# Is this the primary user of the site?
superuser: false

# Role/position (e.g., Professor of Artificial Intelligence)
role: 准教授

# Organizations/Affiliations
organizations:
  - name: 先端科学技術研究科 情報科学領域
    url: "http://isw3.naist.jp/"
  - name: 総合情報基盤センター
    url: "https://itcw3.naist.jp/"

# Short bio (displayed in user profile at end of posts)
bio: 2015 年 (株)日立製作所に入社，システムエンジニアとして勤務．2017 年日本学術振興会特別研究員(DC1)．2020 年 和歌山大学大学院システム工学研究科博士後期課程修了． 同年九州大学大学院システム情報科学研究院 特任助教．2022年 奈良先端科学技術大学院大学 助教．2025年 奈良先端科学技術大学院大学 准教授．2026年 JST創発研究者．ソフトウェア工学，特にソフトウェア品質保証の研究に従事. 博士（工学）．

#education:
#  courses:
#  - course: Title course 1
#    institution: Name of Institution
#   year: 2012
# - course: Title course 1
#    institution: Name of Institution
#   year: 2012

# Social/Academic Networking
# For available icons, see: https://wowchemy.com/docs/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.
# social:
# - icon: home
#   icon_pack: fas
#   link: https://keichi.dev
#   - icon: twitter
#   icon_pack: fab
#   link: https://twitter.com/USERNAME
# - icon: google-scholar
#   icon_pack: ai
#   link: https://scholar.google.com/citations?user=PERSON-ID
# - icon: github
#   icon_pack: fab
#   link: https://github.com/USERNAME

# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
# - icon: cv
#   icon_pack: ai
#   link: files/cv.pdf

# Enter email to display Gravatar (if Gravatar enabled in Config)
email: ""

# Highlight the author in author lists? (true/false)
highlight_name: false

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups:
  - Full-Time Staff

weight: 20
---

<style>
/* セクションブロック */
.section-block {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.section-block h3 {
  background: #1565c0;
  color: #fff;
  padding: 0.6rem 1rem;
  margin: -1.5rem -1.5rem 1rem -1.5rem;
  border-radius: 8px 8px 0 0;
  font-size: 1.1rem;
  font-weight: 600;
}
/* タブ */
.tab-container {
  margin-top: 0.5rem;
}
.tab-buttons {
  display: inline-flex;
  background: #e8e8e8;
  border-radius: 6px;
  padding: 3px;
  margin-bottom: 1rem;
}
.tab-btn {
  padding: 0.5rem 1.2rem;
  cursor: pointer;
  border: none;
  background: transparent;
  font-size: 0.9rem;
  font-weight: 500;
  color: #666;
  border-radius: 4px;
  transition: all 0.2s;
}
.tab-btn:hover {
  color: #333;
}
.tab-btn.active {
  background: #fff;
  color: #1565c0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.tab-pane {
  display: none;
}
.tab-pane.active {
  display: block;
}
/* アコーディオンアイテム */
.grant-item {
  margin-bottom: 0;
  padding: 0.15rem 0;
}
.grant-header {
  display: flex;
  align-items: flex-start;
  cursor: pointer;
  padding: 0.1rem 0;
}
.grant-header::before {
  content: '▶';
  font-size: 0.65rem;
  margin-right: 0.5rem;
  margin-top: 0.3rem;
  transition: transform 0.2s;
  color: #1565c0;
}
.grant-header.active::before {
  transform: rotate(90deg);
}
.grant-title {
  font-weight: 600;
  flex: 1;
  color: #333;
}
.pub-venue {
  margin-left: 0.5rem;
  font-size: 0.8rem;
  color: #fff;
  background: #1565c0;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-weight: 500;
  white-space: nowrap;
}
/* 略歴リスト */
.career-list > div {
  padding: 0.15rem 0;
  line-height: 1.5;
}
.sub-item {
  padding-left: 1.5rem;
  color: #555;
  font-size: 0.95rem;
}
/* 受賞・資格リスト（箇条書き風） */
.award-list > div:not(.group-label), .qual-list > div {
  padding: 0.2rem 0 0.2rem 0;
  line-height: 1.4;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.award-list > div:not(.group-label)::before {
  content: '🏆';
  font-size: 0.75rem;
  flex-shrink: 0;
}
.qual-list > div::before {
  content: '✓';
  font-size: 0.85rem;
  font-weight: bold;
  color: #1565c0;
  flex-shrink: 0;
}
/* グループ見出し */
.group-label {
  font-weight: 600;
  color: #1565c0;
  margin-top: 0.8rem;
  margin-bottom: 0.2rem;
  padding-bottom: 0.2rem;
  border-bottom: 1px solid #e0e0e0;
}
.group-label:first-child {
  margin-top: 0;
}
/* 研究プロジェクト */
.project-area {
  margin-bottom: 0.8rem;
  padding-left: 1rem;
  border-left: 3px solid #1565c0;
}
.project-title {
  margin-bottom: 0.2rem;
}
.project-title b {
  font-size: 1rem;
  display: block;
}
.project-desc {
  font-size: 0.85rem;
  color: #666;
}
.project-papers {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-top: 0.3rem;
}
.project-topic {
  display: inline-flex;
  align-items: center;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  padding: 0.2rem 0.5rem;
  font-size: 0.8rem;
}
.project-topic-name {
  color: #333;
  margin-right: 0.4rem;
}
.project-topic a {
  background: #e3f2fd;
  color: #1565c0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  font-size: 0.75rem;
  margin-left: 0.15rem;
  text-decoration: none;
  transition: background 0.2s;
}
.project-topic a:hover {
  background: #bbdefb;
}
.grant-detail {
  display: none;
  padding-left: 1.2rem;
  margin-top: 0.2rem;
  margin-bottom: 0.2rem;
  color: #555;
  font-size: 0.85rem;
  line-height: 1.5;
  background: #f8f8f8;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
}
.grant-detail.active {
  display: block;
}
.pub-pdf {
  display: inline-block;
  margin-top: 0.3rem;
  background: #e3f2fd;
  color: #1565c0;
  padding: 0.1rem 0.45rem;
  border-radius: 3px;
  font-size: 0.8rem;
  text-decoration: none;
  transition: background 0.2s;
}
.pub-pdf:hover {
  background: #bbdefb;
}
</style>

<div class="section-block">
<h3>プロフィール</h3>

専門はマイニングソフトウェアリポジトリ，特にソフトウェア品質の向上やソフトウェア開発の効率化を目的とし，継続的インテグレーションやDevOpsなどで生じるデータを活用した研究に従事．
近年は，テスト実行時に動的解析を実施することで得られるトレースログを活用し，Just-In-Time不具合予測や自動リファクタリング等に盛んに取り組んでいる．その他，多数のプロジェクトで国際共同研究に取り組み，カナダ・スイス・オランダ・ルクセンブルグ・タイの大学に所属する多くの研究者と協力して研究を進める．博士（工学）．

</div>

<div class="section-block">
<h3>略歴</h3>

<div class="career-list">
  <div><b>2015年4月～2017年3月：</b>株式会社 日立製作所</div>
  <div><b>2017年4月～2020年3月：</b>和歌山大学大学院システム工学研究科 博士後期課程</div>
  <div><b>2017年4月～2020年3月：</b>日本学術振興会 特別研究員（DC1）</div>
  <div class="sub-item">2019年4月～2019年9月：Polytechnique Montréal 客員研究員</div>
  <div><b>2020年4月～2022年3月：</b>九州大学 システム情報科学研究院 特任助教</div>
  <div class="sub-item">2021年11月～2022年2月：Università della Svizzera italiana 客員研究員</div>
  <div><b>2022年4月〜2025年3月：</b>奈良先端科学技術大学院大学 先端科学技術研究科 助教</div>
  <div><b>2022年10月～2026年3月：</b>科学技術振興機構 さきがけ研究員(兼任)</div>
  <div class="sub-item">2022年10月～2022年11月：Radboud University 客員研究員</div>
  <div class="sub-item">2023年9月～2023年10月：Radboud University 客員研究員</div>
  <div><b>2025年4月〜現在：</b>奈良先端科学技術大学院大学 先端科学技術研究科 准教授</div>
  <div><b>2026年8月〜現在：</b>科学技術振興機構 創発研究者(兼任)</div>
</div>

</div>

<div class="section-block">
<h3>主な研究実績</h3>

<p style="font-size:0.85rem; color:#666; margin-bottom:1rem;">
国際会議のランクは<a href="https://portal.core.edu.au/conf-ranks/" target="_blank">CORE Rankings</a>、論文誌のランクは<a href="https://www.scimagojr.com/" target="_blank">SCImago Journal Rankings (SJR)</a>に基づく
</p>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Large-Scale Empirical Analysis of Continuous Fuzzing</span>
    <span class="pub-venue">TSE【Q1】</span>
  </div>
  <div class="grant-detail">
    T Shirai, O Nourry, Y Kashiwa, K Fujiwara, Y Kamei, H Iida<br>
    IEEE Transactions on Software Engineering, 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TSE26_Shirai.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Agent READMEs: An Empirical Study of Context Files for Agentic Coding</span>
    <span class="pub-venue">TOSEM【Q1】</span>
  </div>
  <div class="grant-detail">
    W Chatlatanagulchai, H Li, Y Kashiwa, B Reid, K Thonglek, P Leelaprute, A Rungsawang, B Manaskasemsak, B Adams, A E Hassan, H Iida<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Worrawalan.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub</span>
    <span class="pub-venue">TOSEM【Q1】</span>
  </div>
  <div class="grant-detail">
    M Watanabe, H Li, Y Kashiwa, B Reid, H Iida, A E Hassan<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Watanabe.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Understanding Self-Admitted Technical Debt in Test Code</span>
    <span class="pub-venue">TOSEM【Q1】</span>
  </div>
  <div class="grant-detail">
    I Nakamura, Y Kashiwa, B Lin, H Iida<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Nakamura.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Is Self-Admitted Technical Debt Tested?</span>
    <span class="pub-venue">ESEM【A】</span>
  </div>
  <div class="grant-detail">
    S Yoshimoto, K Horikawa, D Feitosa, Y Kashiwa, H Iida<br>
    ESEM 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Yoshimoto.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Test Alert Snooze: An Empirical Study of Consecutive Test Failures on CI</span>
    <span class="pub-venue">ESEM【A】</span>
  </div>
  <div class="grant-detail">
    A Shirakawa, T Shirai, Y Kashiwa, M Kondo, Y Kamei, H Iida<br>
    ESEM 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Shirakawa.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study of Policy as Code</span>
    <span class="pub-venue">MSR【A】</span>
  </div>
  <div class="grant-detail">
    R Opdebeeck, M Alfadel, A Rahman, Y Kashiwa, J F Ferreira, R G Kula, C De Roover<br>
    MSR 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Opdebeeck.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection</span>
    <span class="pub-venue">MSR【A】</span>
  </div>
  <div class="grant-detail">
    T Shirai, O Nourry, Y Kashiwa, K Fujiwara, H Iida<br>
    MSR 2026.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Shirai.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">My Fuzzers Won't Build: An Empirical Study of Fuzzing Build Failures</span>
    <span class="pub-venue">TOSEM【Q1】</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, W Shang, H Shu, Y Kamei<br>
    ACM Transactions on Software Engineering and Methodology, 2024.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2024_Nourry.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Developer-Applied Accelerations in Continuous Integration</span>
    <span class="pub-venue">ASE【A*】</span>
  </div>
  <div class="grant-detail">
    M Yin, Y Kashiwa, K Gallaba, M Alfadel, Y Kamei, S McIntosh<br>
    ASE 2024.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ASE2024_Yin.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Understanding the Characteristics and the Role of Visual Issue Reports</span>
    <span class="pub-venue">EMSE【Q1】</span>
  </div>
  <div class="grant-detail">
    H Kuramoto, D Wang, M Kondo, Y Kashiwa, Y Kamei, N Ubayashi<br>
    Empirical Software Engineering, 2024.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2024_Kuramoto.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">The Human Side of Fuzzing</span>
    <span class="pub-venue">TOSEM【Q1】</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, B Lin, G Bavota, M Lanza, Y Kamei<br>
    ACM Transactions on Software Engineering and Methodology, 2023.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2023_Nourry.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study on Self-admitted Technical Debt in Modern Code Review</span>
    <span class="pub-venue">IST【Q1】</span>
  </div>
  <div class="grant-detail">
    Y Kashiwa, R Nishikawa, Y Kamei, M Kondo, E Shihab, R Sato, N Ubayashi<br>
    Information and Software Technology, 2022.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2022_Kashiwa.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study of Issue-Link Algorithms</span>
    <span class="pub-venue">EMSE【Q1】</span>
  </div>
  <div class="grant-detail">
    M Kondo, Y Kashiwa, Y Kamei, O Mizuno<br>
    Empirical Software Engineering, 2022.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2022_Kondo.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Refactoring Break Tests and to What Extent?</span>
    <span class="pub-venue">ICSME【A】</span>
  </div>
  <div class="grant-detail">
    Y Kashiwa, K Shimizu, B Lin, G Bavota, M Lanza, Y Kamei, N Ubayashi<br>
    ICSME 2021.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2021_Kashiwa.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Shortening the Release Cycle Affect Refactoring Activities</span>
    <span class="pub-venue">IST【A】</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, Y Kamei, N Ubayashi<br>
    Information and Software Technology, 2021.
    <br><a class="pub-pdf" href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2021_Nourry.pdf" target="_blank" rel="noopener">📄 PDF</a>
  </div>
</div>

その他の論文：<https://github.com/Yutaro-Kashiwa/papers>

</div>

<div class="section-block">
<h3>受賞</h3>

<div class="award-list">
  <div class="group-label">自身の受賞</div>
  <div>2026年: <b>Distinguished Mining Challenge Paper Award, MSR 2026</b></div>
  <div>2025年: ソフトウェアエンジニアリングシンポジウム(SES) 2025 研究奨励賞</div>
  <div>2023年: 電子情報通信学会ソフトウェアサイエンス研究会研究奨励賞</div>
  <div>2022年: IEEE CS Kansai Chapter Young Author Award 2022</div>
  <div>2022年: 電子情報通信学会ソフトウェアサイエンス研究会研究奨励賞</div>
  <div>2021年: <b>情報処理学会論文誌　特選論文</b></div>
  <div>2016年: <b>情報処理学会論文誌　論文賞</b></div>
  <div>2016年: <b>情報処理学会　山下記念研究賞</b></div>
  <div>2015年: ソフトウェアシンポジウム2015　論文奨励賞</div>
  <div>2015年: 和歌山大学　学長表彰</div>
  <div>2015年: 情報処理学会ソフトウェア工学研究会　学生研究賞</div>
  <div>2015年: <b>情報処理学会論文誌　特選論文</b></div>
  <div>2014年: <b>ソフトウェアエンジニアリングシンポジウム(SES) 2014 最優秀論文賞</b></div>
  <div>2013年: ソフトウェアエンジニアリングシンポジウム(SES) 2013 インタラクティブ賞</div>
  <div style="color:#666; font-size:0.9rem;">その他，学内表彰4件</div>
  <div class="group-label">指導学生の受賞</div>
  <div>2025年：FOSE2025 ポスター優秀発表賞（受賞者：清水 公亮）</div>
  <div>2025年：SES 2025 Best International Poster Award（受賞者：堀川 康生）</div>
  <div>2023年：情報処理学会九州支部 若手の会セミナー2023 奨励賞（受賞者：森田 一成）</div>
  <div>2023年：FOSE2023 ポスター・デモ賞（受賞者：米倉 未樹）</div>
  <div>2023年：FOSE2023 ポスター・デモ賞（受賞者：渡邉 未来）</div>
  <div>2022年：IEEE CS Japan Chapter FOSE Young Researcher Award（受賞者：松田 雄河）</div>
</div>

</div>

<div class="section-block">
<h3>研究助成</h3>

<div class="tab-container">
  <div class="tab-buttons">
    <button class="tab-btn active" onclick="showTab(event, 'grant-ongoing')">進行中</button>
    <button class="tab-btn" onclick="showTab(event, 'grant-completed')">終了</button>
  </div>
  <div id="grant-ongoing" class="tab-pane active">

<div class="group-label" style="margin-top:0;">研究代表者</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2034：JST 創発的研究支援事業</span>
  </div>
  <div class="grant-detail">
    研究課題：「AI駆動型ソフトウェア開発のための品質保証基盤」<br>
    直接経費：4,900万円，間接経費：1,470万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2028：科研費 挑戦的研究（萌芽）</span>
  </div>
  <div class="grant-detail">
    研究課題：「ユーザビリティ低下の即時検出を実現する継続的ユーザビリティテスト基盤の創出」<br>
    直接経費：500万円，間接経費：150万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2024-2028：科研費 基盤研究B</span>
  </div>
  <div class="grant-detail">
    研究課題：「不完全なシステムログから不具合原因箇所特定技術の構築：システム自動復旧への挑戦」<br>
    直接経費：1,430万円，間接経費：429万円
  </div>
</div>

<div class="group-label">研究分担者</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2030：科研費 基盤研究A（代表：亀井靖高）</span>
  </div>
  <div class="grant-detail">
    研究課題：「ソフトウェア工学ニューロン：LLM中間表現に潜むソフトウェア工学知識の解明と応用」<br>
    直接経費：3,210万円，間接経費：963万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2029：科研費 基盤研究B（代表：大平雅雄）</span>
  </div>
  <div class="grant-detail">
    研究課題：「システム開発における生成AIのモデル崩壊のメカニズム解明と防止・抑止技術の構築」<br>
    直接経費：1,410万円，間接経費：423万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2028：JST さきがけ融合研究加速課題（代表：三輪忍）</span>
  </div>
  <div class="grant-detail">
    研究課題：「AIの利活用による並列秘密計算コード自動生成」<br>
    直接経費：6,000万円，間接経費：1,800万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2025-2029：科研費 基盤研究B（代表：近藤将成）</span>
  </div>
  <div class="grant-detail">
    研究課題：「既存のソフトウェアのコード理解支援のための合理的判断マイニングの提案」<br>
    直接経費：1,450万円，間接経費：435万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2024-2028：JST ASPIRE（代表：亀井靖高）</span>
  </div>
  <div class="grant-detail">
    研究課題：「Context-Awareなソフトウェア開発AIの実現に向けた国際頭脳循環」<br>
    直接経費：6,923万円，間接経費：2,077万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2023-2029：JST CREST（代表：青木利晃）</span>
  </div>
  <div class="grant-detail">
    研究課題：「次世代車載基盤システムのための形式手法と検証ツールの創出」
  </div>
</div>

</div>
  <div id="grant-completed" class="tab-pane">

<div class="group-label" style="margin-top:0;">研究代表者</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2022-2026：JST さきがけ</span>
  </div>
  <div class="grant-detail">
    研究課題：「プログラム異常動作の自動検出技術の創出：機械が実現するセキュアな自動テスト」<br>
    直接経費：4,000万円，間接経費：1,200万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2021-2024：科研費 若手研究</span>
  </div>
  <div class="grant-detail">
    研究課題：「リファクタリングにより破壊されるテストスイート予測技術の開発」<br>
    直接経費：350万円，間接経費：105万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2017-2020：科研費 特別研究員奨励費</span>
  </div>
  <div class="grant-detail">
    研究課題：「重大な影響を及ぼす不具合の検出手法の構築」<br>
    直接経費：280万円
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2018-2019：若手研究者海外挑戦プログラム</span>
  </div>
  <div class="grant-detail">
    研究課題：「重大な影響を及ぼす不具合の検出手法の構築」<br>
    直接経費：140万円
  </div>
</div>

<div class="group-label">研究分担者</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2025-2026：JST AIP加速課題（代表：吉田則裕）</span>
  </div>
  <div class="grant-detail">
    研究課題：「ソフトウェア解析技術に基づく説明可能自動バグ修正」<br>
    直接経費：1,000万円，間接経費：300万円
  </div>
</div>

</div>
</div>

</div>

<div class="section-block">
<h3>研究プロジェクト</h3>

<div class="project-area">
  <div class="project-title">
    <b>Agentic Software Engineering</b>
    <span class="project-desc">AIエージェントによる自律的なソフトウェア開発の実態調査と品質向上</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Context Files</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Worrawalan.pdf" target="_blank" rel="noopener">📄 TOSEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Pull Requests</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Watanabe.pdf" target="_blank" rel="noopener">📄 TOSEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Quality</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Horikawa.pdf" target="_blank" rel="noopener">📄 MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Watanabe.pdf" target="_blank" rel="noopener">📄 MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EASE2026_Sawada.pdf" target="_blank" rel="noopener">📄 EASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Test Generation</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Yoshimoto.pdf" target="_blank" rel="noopener">📄 MSR</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>AI-assisted Software Development</b>
    <span class="project-desc">機械学習・LLMを活用した開発支援（不具合予測、コード補完、レビュー自動化）</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">JIT Defect Prediction</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2024_Morita.pdf" target="_blank" rel="noopener">📄 SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Completion</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2023_Fukumoto.pdf" target="_blank" rel="noopener">📄 SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Review</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2024_Morikawa.pdf" target="_blank" rel="noopener">📄 ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EASE2024_Watanabe.pdf" target="_blank" rel="noopener">📄 EASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Bug Triage</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IEICE2020_Kashiwa.pdf" target="_blank" rel="noopener">📄 IEICE</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>DevOps & Testing</b>
    <span class="project-desc">CI/CDパイプラインの最適化、ファジング、テスト自動化の研究</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Build Acceleration</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ASE2024_Yin.pdf" target="_blank" rel="noopener">📄 ASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Continuous Fuzzing</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TSE26_Shirai.pdf" target="_blank" rel="noopener">📄 TSE</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2023_Nourry.pdf" target="_blank" rel="noopener">📄 TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2024_Nourry.pdf" target="_blank" rel="noopener">📄 TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Shirai.pdf" target="_blank" rel="noopener">📄 MSR</a></span>
    <span class="project-topic"><span class="project-topic-name">Test Maintenance</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2023_Fujita.pdf" target="_blank" rel="noopener">📄 ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2021_Kashiwa.pdf" target="_blank" rel="noopener">📄 ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Shirakawa.pdf" target="_blank" rel="noopener">📄 ESEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Cloud & Container</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/APSEC2023_Suwanachote.pdf" target="_blank" rel="noopener">📄 APSEC</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SCAM2024_Mabuchi.pdf" target="_blank" rel="noopener">📄 SCAM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2022_Higashi.pdf" target="_blank" rel="noopener">📄 SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Dependency & Config</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2025_Suwanachote.pdf" target="_blank" rel="noopener">📄 MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Opdebeeck.pdf" target="_blank" rel="noopener">📄 MSR</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>Technical Debt & Refactoring</b>
    <span class="project-desc">技術的負債の検出・管理とリファクタリングがテストに与える影響の分析</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Refactoring</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2021_Nourry.pdf" target="_blank" rel="noopener">📄 IST</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2022_Nourry.pdf" target="_blank" rel="noopener">📄 ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SCAM2021_Atwi.pdf" target="_blank" rel="noopener">📄 SCAM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2026_Liu.pdf" target="_blank" rel="noopener">📄 SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">SATD</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2022_Kashiwa.pdf" target="_blank" rel="noopener">📄 IST</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Nakamura.pdf" target="_blank" rel="noopener">📄 TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Yoshimoto.pdf" target="_blank" rel="noopener">📄 ESEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICPC2025_Yonekura.pdf" target="_blank" rel="noopener">📄 ICPC</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>Bug Analysis</b>
    <span class="project-desc">不具合報告の分析、重大バグの予測、イシューとコミットの紐付け</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Visual Issues</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2024_Kuramoto.pdf" target="_blank" rel="noopener">📄 EMSE</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICPC2022_Kuramoto.pdf" target="_blank" rel="noopener">📄 ICPC</a></span>
    <span class="project-topic"><span class="project-topic-name">High Impact Bugs</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2014_Kashiwa.pdf" target="_blank" rel="noopener">📄 ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2015_Ohira.pdf" target="_blank" rel="noopener">📄 MSR</a></span>
    <span class="project-topic"><span class="project-topic-name">Issue Linking</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2022_Kondo.pdf" target="_blank" rel="noopener">📄 EMSE</a></span>
  </div>
</div>

</div>

<div class="section-block">
<h3>資格</h3>

<div class="qual-list">
  <div>情報処理推進機構 データベーススペシャリスト</div>
  <div>情報処理推進機構 応用情報技術者</div>
</div>

</div>

<div class="section-block">
<h3>Contact</h3>

yutaro.kashiwa［ａｔ］is.naist.jp

</div>

<script>
function showTab(event, tabId) {
  const container = event.target.closest('.tab-container');
  container.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  container.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  container.querySelector('#' + tabId).classList.add('active');
  event.target.classList.add('active');
}
function toggleGrant(header) {
  header.classList.toggle('active');
  header.nextElementSibling.classList.toggle('active');
}
</script>
