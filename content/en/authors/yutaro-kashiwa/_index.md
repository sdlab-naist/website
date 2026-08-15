---
# Display name
title: "Yutaro Kashiwa"

# Username (this should match the folder name and the name on publications)
authors:
  - "yutaro-kashiwa"

# Is this the primary user of the site?
superuser: false

# Role/position (e.g., Professor of Artificial Intelligence)
role: Associate Professor

# Organizations/Affiliations
organizations:
  - name: Division of Information Science
    url: "http://isw3.naist.jp/home-en.html"
  - name: Information Initiative Center
    url: "https://itcw3.naist.jp/index.en.html"

# Short bio (displayed in user profile at end of posts)
bio: Yutaro Kashiwa is an associate professor at Nara Institute of Science and Technology (NAIST), Japan, and a JST FOREST Researcher. He worked for Hitachi Ltd. as a full-time software engineer for two years before spending three years as a research fellow of the Japan Society for the Promotion of Science. He received his Ph.D. degree in engineering from Wakayama University in 2020. His research interests include empirical software engineering, specifically the analysis of software bugs, testing, refactoring, and release.

# Social/Academic Networking
# For available icons, see: https://wowchemy.com/docs/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.
<!-- social:
  - icon: envelope
    icon_pack: fas
    link: "#contact" # For a direct email link, use "mailto:test@example.org".
  - icon: twitter
    icon_pack: fab
    link: https://twitter.com/USERNAME
  - icon: google-scholar
    icon_pack: ai
    link: https://scholar.google.com/citations?user=PERSON-ID
  - icon: github
    icon_pack: fab
    link: https://github.com/USERNAME -->
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
/* Section blocks */
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
/* Tabs */
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
/* Accordion items */
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
/* Career list */
.career-list > div {
  padding: 0.15rem 0;
  line-height: 1.5;
}
.sub-item {
  padding-left: 1.5rem;
  color: #555;
  font-size: 0.95rem;
}
/* Award & Qualification lists */
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
/* Group labels */
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
/* Research projects */
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
</style>

<div class="section-block">
<h3>Profile</h3>

I am an associate professor at Nara Institute of Science and Technology (NAIST), Japan, and a JST FOREST Researcher. I worked for Hitachi Ltd. as a full-time software engineer for two years before spending three years as a research fellow of the Japan Society for the Promotion of Science. I received my Ph.D. degree in engineering from Wakayama University in 2020. After this, I was a post-doc under SENSOR (SENsible SOftware Refactoring) project led by Yasutaka Kamei and Gabriele Bavota.

My research interests include empirical software engineering, specifically mining software repositories. I focus on utilizing data generated from continuous integration and DevOps to improve software quality and development efficiency. In recent years, I have been actively working on Just-In-Time defect prediction and automatic refactoring using trace logs obtained through dynamic analysis during test execution. I also collaborate with many researchers from universities in Canada, Switzerland, the Netherlands, Luxembourg, and Thailand on numerous international joint research projects. Ph.D. in Engineering.

</div>

<div class="section-block">
<h3>Biography</h3>

<div class="career-list">
  <div><b>Apr. 2015 - Mar. 2017:</b> Full-time Software Developer at Hitachi, Ltd.</div>
  <div><b>Apr. 2017 - Mar. 2020:</b> Doctoral Student at Wakayama University</div>
  <div><b>Apr. 2017 - Mar. 2020:</b> JSPS Research Fellow (DC1)</div>
  <div class="sub-item">Apr. 2019 - Sep. 2019: Visiting Researcher at Polytechnique Montréal</div>
  <div><b>Apr. 2020 - Mar. 2022:</b> Research Assistant Professor at Kyushu University</div>
  <div class="sub-item">Nov. 2021 - Feb. 2022: Visiting Researcher at Università della Svizzera italiana</div>
  <div><b>Apr. 2022 - Mar. 2025:</b> Assistant Professor at Nara Institute of Science and Technology</div>
  <div><b>Oct. 2022 - Mar. 2026:</b> JST PRESTO Researcher (concurrent)</div>
  <div class="sub-item">Oct. 2022 - Nov. 2022: Visiting Researcher at Radboud University</div>
  <div class="sub-item">Sep. 2023 - Oct. 2023: Visiting Researcher at Radboud University</div>
  <div><b>Apr. 2025 - Present:</b> Associate Professor at Nara Institute of Science and Technology</div>
  <div><b>Aug. 2026 - Present:</b> JST FOREST Researcher (concurrent)</div>
</div>

</div>

<div class="section-block">
<h3>Selected Publications</h3>

<p style="font-size:0.85rem; color:#666; margin-bottom:1rem;">
Conference rankings are based on <a href="https://portal.core.edu.au/conf-ranks/" target="_blank">CORE Rankings</a>. Journal rankings are based on <a href="https://www.scimagojr.com/" target="_blank">SCImago Journal Rankings (SJR)</a>.
</p>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Large-Scale Empirical Analysis of Continuous Fuzzing</span>
    <span class="pub-venue">TSE [Q1]</span>
  </div>
  <div class="grant-detail">
    T Shirai, O Nourry, Y Kashiwa, K Fujiwara, Y Kamei, H Iida<br>
    IEEE Transactions on Software Engineering, 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Agent READMEs: An Empirical Study of Context Files for Agentic Coding</span>
    <span class="pub-venue">TOSEM [Q1]</span>
  </div>
  <div class="grant-detail">
    W Chatlatanagulchai, H Li, Y Kashiwa, B Reid, K Thonglek, P Leelaprute, A Rungsawang, B Manaskasemsak, B Adams, A E Hassan, H Iida<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub</span>
    <span class="pub-venue">TOSEM [Q1]</span>
  </div>
  <div class="grant-detail">
    M Watanabe, H Li, Y Kashiwa, B Reid, H Iida, A E Hassan<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Understanding Self-Admitted Technical Debt in Test Code</span>
    <span class="pub-venue">TOSEM [Q1]</span>
  </div>
  <div class="grant-detail">
    I Nakamura, Y Kashiwa, B Lin, H Iida<br>
    ACM Transactions on Software Engineering and Methodology, 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Is Self-Admitted Technical Debt Tested?</span>
    <span class="pub-venue">ESEM [A]</span>
  </div>
  <div class="grant-detail">
    S Yoshimoto, K Horikawa, D Feitosa, Y Kashiwa, H Iida<br>
    ESEM 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Test Alert Snooze: An Empirical Study of Consecutive Test Failures on CI</span>
    <span class="pub-venue">ESEM [A]</span>
  </div>
  <div class="grant-detail">
    A Shirakawa, T Shirai, Y Kashiwa, M Kondo, Y Kamei, H Iida<br>
    ESEM 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study of Policy as Code</span>
    <span class="pub-venue">MSR [A]</span>
  </div>
  <div class="grant-detail">
    R Opdebeeck, M Alfadel, A Rahman, Y Kashiwa, J F Ferreira, R G Kula, C De Roover<br>
    MSR 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Programming Language Matter? An Empirical Study of Fuzzing Bug Detection</span>
    <span class="pub-venue">MSR [A]</span>
  </div>
  <div class="grant-detail">
    T Shirai, O Nourry, Y Kashiwa, K Fujiwara, H Iida<br>
    MSR 2026.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">My Fuzzers Won't Build: An Empirical Study of Fuzzing Build Failures</span>
    <span class="pub-venue">TOSEM [Q1]</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, W Shang, H Shu, Y Kamei<br>
    ACM Transactions on Software Engineering and Methodology, 2024.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Developer-Applied Accelerations in Continuous Integration</span>
    <span class="pub-venue">ASE [A*]</span>
  </div>
  <div class="grant-detail">
    M Yin, Y Kashiwa, K Gallaba, M Alfadel, Y Kamei, S McIntosh<br>
    ASE 2024.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Understanding the Characteristics and the Role of Visual Issue Reports</span>
    <span class="pub-venue">EMSE [Q1]</span>
  </div>
  <div class="grant-detail">
    H Kuramoto, D Wang, M Kondo, Y Kashiwa, Y Kamei, N Ubayashi<br>
    Empirical Software Engineering, 2024.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">The Human Side of Fuzzing</span>
    <span class="pub-venue">TOSEM [Q1]</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, B Lin, G Bavota, M Lanza, Y Kamei<br>
    ACM Transactions on Software Engineering and Methodology, 2023.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study on Self-admitted Technical Debt in Modern Code Review</span>
    <span class="pub-venue">IST [Q1]</span>
  </div>
  <div class="grant-detail">
    Y Kashiwa, R Nishikawa, Y Kamei, M Kondo, E Shihab, R Sato, N Ubayashi<br>
    Information and Software Technology, 2022.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">An Empirical Study of Issue-Link Algorithms</span>
    <span class="pub-venue">EMSE [Q1]</span>
  </div>
  <div class="grant-detail">
    M Kondo, Y Kashiwa, Y Kamei, O Mizuno<br>
    Empirical Software Engineering, 2022.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Refactoring Break Tests and to What Extent?</span>
    <span class="pub-venue">ICSME [A]</span>
  </div>
  <div class="grant-detail">
    Y Kashiwa, K Shimizu, B Lin, G Bavota, M Lanza, Y Kamei, N Ubayashi<br>
    ICSME 2021.
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">Does Shortening the Release Cycle Affect Refactoring Activities</span>
    <span class="pub-venue">IST [Q1]</span>
  </div>
  <div class="grant-detail">
    O Nourry, Y Kashiwa, Y Kamei, N Ubayashi<br>
    Information and Software Technology, 2021.
  </div>
</div>

Other publications: <https://github.com/Yutaro-Kashiwa/papers>

</div>

<div class="section-block">
<h3>Awards</h3>

<div class="award-list">
  <div class="group-label">Personal Awards</div>
  <div>2026: <b>Distinguished Mining Challenge Paper Award, MSR 2026</b></div>
  <div>2025: Research Encouragement Award, Software Engineering Symposium (SES) 2025</div>
  <div>2023: Research Encouragement Award, IEICE Special Interest Groups on Software Science</div>
  <div>2022: IEEE CS Kansai Chapter Young Author Award 2022</div>
  <div>2022: Research Encouragement Award, IEICE Special Interest Groups on Software Science</div>
  <div>2021: <b>Specially Selected Paper Award, Transactions of IPSJ</b></div>
  <div>2016: <b>IPSJ Outstanding Paper Award, Transactions of IPSJ</b></div>
  <div>2016: <b>IPSJ Yamashita SIG Research Award</b></div>
  <div>2015: Research Encouragement Award, Software Symposium 2015</div>
  <div>2015: President's Award, Wakayama University</div>
  <div>2015: Student Research Award, IPSJ SIGSE</div>
  <div>2015: <b>Specially Selected Paper Award, Transactions of IPSJ</b></div>
  <div>2014: <b>Best Paper Award, Software Engineering Symposium 2014</b></div>
  <div>2013: Interactive Award, Software Engineering Symposium 2013</div>
  <div style="color:#666; font-size:0.9rem;">Plus 4 internal university awards</div>
  <div class="group-label">Student Awards (as Supervisor)</div>
  <div>2025: FOSE2025 Best Poster Presentation Award (Recipient: Kosuke Shimizu)</div>
  <div>2025: SES 2025 Best International Poster Award (Recipient: Kosei Horikawa)</div>
  <div>2023: IPSJ Kyushu-branch Young Research Seminar 2023 Encouraged Award (Recipient: Issei Morita)</div>
  <div>2023: FOSE2023 Poster and Demo Award (Recipient: Miki Yonekura)</div>
  <div>2023: FOSE2023 Poster and Demo Award (Recipient: Miku Watanabe)</div>
  <div>2022: IEEE CS Japan Chapter FOSE Young Researcher Award (Recipient: Yuga Matsuda)</div>
</div>

</div>

<div class="section-block">
<h3>Grants</h3>

<div class="tab-container">
  <div class="tab-buttons">
    <button class="tab-btn active" onclick="showTab(event, 'grant-ongoing')">Ongoing</button>
    <button class="tab-btn" onclick="showTab(event, 'grant-completed')">Completed</button>
  </div>
  <div id="grant-ongoing" class="tab-pane active">

<div class="group-label" style="margin-top:0;">Principal Investigator</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2034: JST FOREST</span>
  </div>
  <div class="grant-detail">
    Project: "Quality Assurance Infrastructure for AI-Driven Software Development"<br>
    Direct Cost: 49,000,000 JPY, Indirect Cost: 14,700,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2028: JSPS KAKENHI Challenging Research (Exploratory)</span>
  </div>
  <div class="grant-detail">
    Project: "Creating Continuous Usability Testing Infrastructure for Immediate Detection of Usability Degradation"<br>
    Direct Cost: 5,000,000 JPY, Indirect Cost: 1,500,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2024-2028: JSPS KAKENHI (B)</span>
  </div>
  <div class="grant-detail">
    Project: "Developing Technique for Bug Localization with Incomplete System Logs: Challenge for Automatic System Recovery"<br>
    Direct Cost: 14,300,000 JPY, Indirect Cost: 4,290,000 JPY
  </div>
</div>

<div class="group-label">Co-Investigator</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2030: JSPS KAKENHI (A) (PI: Yasutaka Kamei)</span>
  </div>
  <div class="grant-detail">
    Project: "Software Engineering Neurons: Understanding and Applying SE Knowledge in LLM Intermediate Representations"<br>
    Direct Cost: 32,100,000 JPY, Indirect Cost: 9,630,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2029: JSPS KAKENHI (B) (PI: Akinori Ihara)</span>
  </div>
  <div class="grant-detail">
    Project: "Understanding and Preventing Model Collapse of Generative AI in System Development"<br>
    Direct Cost: 14,100,000 JPY, Indirect Cost: 4,230,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2026-2028: JST PRESTO Fusion Research (PI: Shinobu Miwa)</span>
  </div>
  <div class="grant-detail">
    Project: "Automatic Generation of Parallel Secure Computation Code Using AI"<br>
    Direct Cost: 60,000,000 JPY, Indirect Cost: 18,000,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2025-2029: JSPS KAKENHI (B) (PI: Masanari Kondo)</span>
  </div>
  <div class="grant-detail">
    Project: "Proposal for Rational Decision Mining to Support Understanding of Existing Software Code"<br>
    Direct Cost: 14,500,000 JPY, Indirect Cost: 4,350,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2024-2028: JST ASPIRE (PI: Yasutaka Kamei)</span>
  </div>
  <div class="grant-detail">
    Project: "International Brain Circulation Initiative for Context-Aware AI in Software Development"<br>
    Direct Cost: 69,230,000 JPY, Indirect Cost: 20,770,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2023-2029: JST CREST (PI: Toshiaki Aoki)</span>
  </div>
  <div class="grant-detail">
    Project: "Formal Methods and Verification Tools for Next-Generation Automotive Platform Systems"
  </div>
</div>

</div>
  <div id="grant-completed" class="tab-pane">

<div class="group-label" style="margin-top:0;">Principal Investigator</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2022-2026: JST PRESTO</span>
  </div>
  <div class="grant-detail">
    Project: "Developing Technique for Automatic Detection of Anomalous Program Behavior: Machine-Enabled Secure Automatic Testing"<br>
    Direct Cost: 40,000,000 JPY, Indirect Cost: 12,000,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2021-2024: JSPS KAKENHI (Young Researcher)</span>
  </div>
  <div class="grant-detail">
    Project: "Developing Technique for Predicting Test Suites Broken by Refactoring"<br>
    Direct Cost: 3,500,000 JPY, Indirect Cost: 1,050,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2017-2020: JSPS KAKENHI (JSPS Fellows)</span>
  </div>
  <div class="grant-detail">
    Project: "Development of a Detection Method for High Impact Bugs"<br>
    Direct Cost: 2,800,000 JPY
  </div>
</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2018-2019: JSPS Overseas Challenge Program</span>
  </div>
  <div class="grant-detail">
    Project: "Development of a Detection Method for High Impact Bugs"<br>
    Direct Cost: 1,400,000 JPY
  </div>
</div>

<div class="group-label">Co-Investigator</div>

<div class="grant-item">
  <div class="grant-header" onclick="toggleGrant(this)">
    <span class="grant-title">2025-2026: JST AIP Acceleration (PI: Norihiro Yoshida)</span>
  </div>
  <div class="grant-detail">
    Project: "Explainable Automatic Bug Fixing Based on Software Analysis Technology"<br>
    Direct Cost: 10,000,000 JPY, Indirect Cost: 3,000,000 JPY
  </div>
</div>

</div>
</div>

</div>

<div class="section-block">
<h3>Research Projects</h3>

<div class="project-area">
  <div class="project-title">
    <b>Agentic Software Engineering</b>
    <span class="project-desc">Empirical analysis and quality improvement of autonomous software development by AI agents</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Context Files</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Worrawalan.pdf">TOSEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Pull Requests</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Watanabe.pdf">TOSEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Quality</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Horikawa.pdf">MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Watanabe.pdf">MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EASE2026_Sawada.pdf">EASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Test Generation</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Yoshimoto.pdf">MSR</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>AI-assisted Software Development</b>
    <span class="project-desc">Development support using ML/LLM (defect prediction, code completion, review automation)</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">JIT Defect Prediction</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2024_Morita.pdf">SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Completion</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2023_Fukumoto.pdf">SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Code Review</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2024_Morikawa.pdf">ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EASE2024_Watanabe.pdf">EASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Bug Triage</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IEICE2020_Kashiwa.pdf">IEICE</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>DevOps & Testing</b>
    <span class="project-desc">CI/CD pipeline optimization, fuzzing, and test automation research</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Build Acceleration</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ASE2024_Yin.pdf">ASE</a></span>
    <span class="project-topic"><span class="project-topic-name">Continuous Fuzzing</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TSE2026_Shirai.pdf">TSE</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2023_Nourry.pdf">TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2024_Nourry.pdf">TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Shirai.pdf">MSR</a></span>
    <span class="project-topic"><span class="project-topic-name">Test Maintenance</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2023_Fujita.pdf">ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2021_Kashiwa.pdf">ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Shirakawa.pdf">ESEM</a></span>
    <span class="project-topic"><span class="project-topic-name">Cloud & Container</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/APSEC2023_Suwanachote.pdf">APSEC</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SCAM2024_Mabuchi.pdf">SCAM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2022_Higashi.pdf">SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">Dependency & Config</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2025_Suwanachote.pdf">MSR</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2026_Opdebeeck.pdf">MSR</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>Technical Debt & Refactoring</b>
    <span class="project-desc">Detection and management of technical debt, and analysis of refactoring impact on tests</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Refactoring</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2021_Nourry.pdf">IST</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2022_Nourry.pdf">ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SCAM2021_Atwi.pdf">SCAM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/SANER2026_Liu.pdf">SANER</a></span>
    <span class="project-topic"><span class="project-topic-name">SATD</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/IST2022_Kashiwa.pdf">IST</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/TOSEM2026_Nakamura.pdf">TOSEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ESEM2026_Yoshimoto.pdf">ESEM</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICPC2025_Yonekura.pdf">ICPC</a></span>
  </div>
</div>

<div class="project-area">
  <div class="project-title">
    <b>Bug Analysis</b>
    <span class="project-desc">Analysis of bug reports, prediction of high-impact bugs, and issue-commit linking</span>
  </div>
  <div class="project-papers">
    <span class="project-topic"><span class="project-topic-name">Visual Issues</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2024_Kuramoto.pdf">EMSE</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICPC2022_Kuramoto.pdf">ICPC</a></span>
    <span class="project-topic"><span class="project-topic-name">High Impact Bugs</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/ICSME2014_Kashiwa.pdf">ICSME</a><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/MSR2015_Ohira.pdf">MSR</a></span>
    <span class="project-topic"><span class="project-topic-name">Issue Linking</span><a href="https://github.com/Yutaro-Kashiwa/papers/blob/master/EMSE2022_Kondo.pdf">EMSE</a></span>
  </div>
</div>

</div>

<div class="section-block">
<h3>Qualifications</h3>

<div class="qual-list">
  <div>Database Specialist (Information-technology Promotion Agency, Japan)</div>
  <div>Applied Information Technology Engineer (Information-technology Promotion Agency, Japan)</div>
</div>

</div>

<div class="section-block">
<h3>Contact</h3>

yutaro.kashiwa [at] is.naist.jp

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
