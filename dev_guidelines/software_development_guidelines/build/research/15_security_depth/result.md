# Slot 15_security_depth (SECD): security depth, detection, privacy, maturity models

## L1 headline

Best practice on security depth is settled on the principle (depth is set by risk, verification is layered automated plus manual, security events are logged, protected and alerted on, personal data is minimised and given a retention limit) and open on the numbers (blocking thresholds, retention length, bug-bounty fit, evidence that maturity models improve outcomes); certainty is grounded for what the sources say and inferred for every placement rule that no source states outright.

Pinned: 29 sources (T1: 23, T2: 3, T3: 3, T4: 0); 44 claims; contested topics: blocking versus advisory placement of security analysis; log retention depth versus data minimisation; bug bounty versus disclosure policy only; prescriptive versus descriptive maturity framework as the anchor; T1 fetch failures: NIST IR 8397, NIST SP 800-61r3 and OMB M-20-32 PDFs unreadable through the fetch tool (recovered by local text extraction, read in full); ASVS raw-file URL 404 (recovered from the repository page); OWASP Top 10 and WSTG URLs redirected (Top 10 recovered, WSTG body never read, foreword excerpt only); not recovered: NIST SP 800-92 and SP 800-115 bodies (abstract only), CISA/ASD event-logging guidance PDF (landing page only), SAMM maturity-level definition pages (practice pages read instead).

## L2 claims

Clusters
1. Depth of security verification is set by the application's risk, not uniform; ASVS (requirements with three levels), SAMM (per-practice target maturity) and BSIMM (descriptive benchmark) answer different questions, and no source claims that maximum level everywhere is the aim. Consensus on risk-based depth, contested on which framework anchors; grounded. SECD-C01 to C07, C44.
2. A minimum floor of developer security testing exists (threat model, static scan, secret heuristics, run-time checks, black-box and structural tests, regression tests from past bugs, fuzzer, web scanner, same checks on included components); NIST states it is a lower bar, not best practice. Majority, grounded. SECD-C08, C09, C10, C21, C22.
3. Automated analysis: static analysis early and often with triage because of false positives and blind spots (authentication, access control, cryptography); fuzzing and dynamic checks continuous or nightly; pre-release fuzzing denies attackers the same tool. Majority, grounded. SECD-C11, C12, C15, C16, C17.
4. Placement and blocking of findings: only high-confidence checks block; noise is measured as effective false-positive rate and checks over the budget are disabled; sources differ on blocking by default. Contested, grounded. SECD-C13, C14.
5. Manual expert testing complements automation, scaled to criticality, and security tests should also prove the detection works (a pen test that raises no alert is a finding). Consensus on the complement, grounded; depth rule inferred. SECD-C18, C19, C20.
6. Vulnerability intake: publish a reporting process, a private channel and a response time; start with a disclosure policy, treat a paid bounty as a cost and maturity decision. Consensus on intake, contested on bounty; grounded. SECD-C23, C24.
7. Security logging: what to log, a documented inventory, metadata and a common format, protection against tampering and log injection, never secrets or unjustified personal data, optional pseudonymised timelines. Consensus, grounded. SECD-C25, C26, C27, C33, C34.
8. Detection is alerting plus response, not logging alone: verification standards leave alerting out of scope, dwell time is the cost, incident response is integrated into risk management and feeds lessons back, detection rules can be kept in a tool-neutral format. Majority, grounded; portability of rules inferred. SECD-C28, C29, C30, C31.
9. Data lifecycle: collect only what the purpose needs, classify data into protection levels, set retention per purpose and delete on schedule, decide by design and by default; erasure reaching copies and backups is an open edge. Consensus on principle (legal text and ASVS), contested on log retention, open on erasure in backups. SECD-C32, C35, C36, C37, C38, C39.
10. Privacy governance: impact assessment when risk is high, breach notification clock and breach record, regular testing of the measures, risk-based privacy framework. Grounded for legal text (EU), inferred for stack-neutral transfer. SECD-C40, C41, C42, C43.

Live debates (forces in tension)
- Block versus advise on security findings (placement in code review, build, release): security and confidence against delivery speed and developer trust; blocking suits high-confidence low-noise checks, advisory suits noisy analysis (NIST must-fix list and OpenSSF "fix confirmed exploitable findings" against Google's "developers ignore warnings, so errors or nothing").
- Log retention: investigation power (long dwell times, 200-day figure) against data minimisation and storage limitation (keep no longer than the legal or purpose limit); tiered retention is the proposed compromise.
- Bug bounty versus disclosure policy only versus periodic pen test: cost of ownership and speed of finding against control and noise; OMB M-20-32 puts the disclosure policy first and tells bounty owners to weigh cost, competence and maturity.
- Prescriptive requirements (ASVS), prescriptive roadmap (SAMM) and descriptive benchmark (BSIMM): control and correctness against fit to what peers do; a descriptive model records common practice, which is evidence, not the verdict.
- Automated breadth against manual depth: delivery speed and cost against confidence on business-logic flaws; consensus is to run both, order and share open.

Candidate central decisions (every team makes these first)
1. Target assurance level per application, and the risk trigger that raises it (ASVS level or SAMM target per practice), recorded and revisited.
2. The floor of security tests every change must pass, which of them block, and the noise budget that disables a check.
3. Which logged security events exist, who gets alerted on which, and whether a pen test or scan is expected to trip an alert.
4. Retention period per data class and per log class, and the deletion mechanism, set before collection starts.
5. Vulnerability intake channel and whether a paid bounty is in or out.

Not covered
- Empirical evidence on detection tools, pen-test frequency and maturity-model effect on outcomes (none read).
- Bodies of NIST SP 800-92, SP 800-115, the CISA/ASD logging guidance, WSTG test cases, ASVS 5.0 assessment chapter, BSIMM activity list and report, CIS Controls, MITRE ATT&CK, ISO/IEC 27001, 27701 and 29147 (not public or not read).
- SIEM and detection-engineering practice beyond one T3 source; privacy law outside the EU text (US states, other regimes); consent management; AI-specific security testing.

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| SECD-S01 | T1 | OWASP Application Security Verification Standard, project page | OWASP | https://owasp.org/www-project-application-security-verification-standard/ | purpose of ASVS, current version 5.0.0 |
| SECD-S02 | T1 | ASVS 5.0, chapter "What is the ASVS" | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x03-What-is-the-ASVS.md | levels, level choice, procurement and incremental use |
| SECD-S03 | T1 | ASVS 5.0, V16 Security Logging and Error Handling | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md | logging requirements by level |
| SECD-S04 | T1 | ASVS 5.0, V14 Data Protection | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x23-V14-Data-Protection.md | classification, retention, sensitive data |
| SECD-S05 | T1 | OWASP SAMM model overview | OWASP | https://owaspsamm.org/model/ | 5 functions, 15 practices, 3 maturity levels |
| SECD-S06 | T1 | SAMM practice: Security Testing | OWASP | https://owaspsamm.org/model/verification/security-testing/ | automated and manual streams |
| SECD-S07 | T1 | SAMM practice: Incident Management | OWASP | https://owaspsamm.org/model/operations/incident-management/ | detection and response streams |
| SECD-S08 | T1 | SAMM practice: Threat Assessment | OWASP | https://owaspsamm.org/model/design/threat-assessment/ | risk profile and threat modelling streams |
| SECD-S09 | T1 | SAMM about and self-assessment | OWASP | https://owaspsamm.org/about/ | how SAMM is meant to be used |
| SECD-S10 | T3 | BSIMM maturity model page | Black Duck (BSIMM maintainer) | https://www.blackduck.com/services/security-program/bsimm-maturity-model.html (plus a search snippet of an early BSIMM description, not read in full) | BSIMM as descriptive benchmark |
| SECD-S11 | T1 | NIST IR 8397, Guidelines on Minimum Standards for Developer Verification of Software | NIST | https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8397.pdf (fetch tool unreadable, local text extraction read sections 1, 2, 3.4, SAST part) | minimum developer testing |
| SECD-S12 | T1 | NIST SP 800-61r3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf (local text extraction; introduction and CSF profile skimmed) | incident response in risk management |
| SECD-S13 | T1 | NIST SP 800-92, Guide to Computer Security Log Management | NIST | https://csrc.nist.gov/pubs/sp/800/92/final (abstract only) | existence and scope of log management guidance (2006) |
| SECD-S14 | T1 | NIST SP 800-115, Technical Guide to Information Security Testing and Assessment | NIST | https://csrc.nist.gov/pubs/sp/800/115/final (abstract only) | existence and scope of security testing guidance (2008) |
| SECD-S15 | T1 | OWASP Logging Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | what to log, protect, retain |
| SECD-S16 | T1 | OWASP Top 10:2021 A09 Security Logging and Monitoring Failures | OWASP | https://top10.owasp.org/2021/A09_2021-Security_Logging_and_Monitoring_Failures | failure modes of detection |
| SECD-S17 | T1 | OWASP Web Security Testing Guide, home page | OWASP | https://wstg.owasp.org/latest/ (foreword excerpt only) | testing phases across lifecycle |
| SECD-S18 | T1 | OWASP DevSecOps Guideline | OWASP | https://owasp.github.io/www-project-devsecops-guideline/latest (introduction only) | pipeline stages for security checks |
| SECD-S19 | T2 | Software Engineering at Google, ch. 20 Static Analysis | Google | https://abseil.io/resources/swe-book/html/ch20.html | false-positive budget, analysis in review |
| SECD-S20 | T2 | Building Secure and Reliable Systems, ch. 13 Testing Code | Google | https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html | static, dynamic, fuzzing in CI |
| SECD-S21 | T2 | Building Secure and Reliable Systems, ch. 15 Investigating Systems | Google | https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html | logging for investigation, retention, privacy |
| SECD-S22 | T1 | OpenSSF Best Practices Badge criteria | OpenSSF | https://www.bestpractices.dev/en/criteria/0 and https://www.bestpractices.dev/en/criteria/2 | analysis and vulnerability-reporting criteria |
| SECD-S23 | T1 | GDPR, Articles 5, 17, 25, 32, 33, 35 | European Union | https://gdpr-info.eu/art-5-gdpr/ (and /art-17, /art-25, /art-32, /art-33, /art-35) | legal principles on personal data (unofficial text mirror) |
| SECD-S24 | T1 | NIST Privacy Framework 1.1 (initial public draft page) | NIST | https://www.nist.gov/privacy-framework | privacy risk management framework |
| SECD-S25 | T1 | OMB Memorandum M-20-32, Improving Vulnerability Identification, Management, and Remediation | US Office of Management and Budget | https://www.whitehouse.gov/wp-content/uploads/2020/09/M-20-32.pdf (local text extraction) | disclosure policy and bug bounty |
| SECD-S26 | T1 | RFC 9116, security.txt | IETF | https://www.rfc-editor.org/rfc/rfc9116 | machine-readable disclosure contact |
| SECD-S27 | T3 | Why Don't Software Developers Use Static Analysis Tools to Find Bugs? (ICSE 2013) | Johnson, Song, Murphy-Hill, Bowdidge | search result summary of https://cs.gmu.edu/%7Ejohnsonb/docs/icse2013.pdf (paper not read; abstract level only) | peer-reviewed interview study of 20 developers |
| SECD-S28 | T3 | Sigma, generic signature format for log events | SigmaHQ maintainers | https://github.com/SigmaHQ/sigma | tool-neutral detection rule format |
| SECD-S29 | T1 | Best practices for event logging and threat detection | CISA with ASD and international partners | https://www.cisa.gov/resources-tools/resources/best-practices-event-logging-and-threat-detection (landing page only) | existence of a five-area logging baseline |

### Claims

**SECD-C01** — Depth of security verification should be set per application from its risk profile, not applied uniformly.
- level: principle; stack: neutral; sources: S02 ("Selecting Appropriate Levels": a startup collecting limited sensitive data may focus on Level 1, a bank can hardly justify less than Level 3), S09 (SAMM "does not insist that all organizations achieve the maximum maturity level in every category"), S08.
- agreement: consensus; certainty: grounded.

**SECD-C02** — A team should choose which framework anchors its security practice by the question it needs answered: ASVS to specify and verify technical requirements, SAMM to assess and plan a programme, BSIMM to benchmark against peers.
- level: decision; stack: neutral; sources: S01, S02, S05, S09, S10.
- agreement: contested; certainty: inferred (synthesis of what each source says it is for).
- positions: (a) requirements standard (ASVS): strongest argument is testable, level-graded requirements usable in procurement (S02); serves correctness and control; wins for a single application or a supplier contract. (b) Prescriptive maturity model (SAMM): measurable, actionable, versatile, with a roadmap (S09); serves delivery of a programme at organisation scale; wins with many teams. (c) Descriptive benchmark (BSIMM): "BSIMM is descriptive, documenting your actual practices"; built on observations of 100+ organizations (S10); serves comparison; wins for a security group justifying investment, loses as a decision rule since common practice is not best practice.

**SECD-C03** — ASVS level 1 holds roughly 20% of the requirements (first-layer defences, no preconditions), level 2 roughly 50% (about 70% cumulative), level 3 roughly 30% (defence in depth, hard-to-implement controls).
- level: practice; stack: web application and API; sources: S02.
- agreement: consensus; certainty: grounded (percentages as given by the chapter, read through the fetch tool's summary).

**SECD-C04** — The chosen assurance target should be written down and revisited when the application's risk changes (new personal data, new regulatory scope).
- level: practice; stack: neutral; sources: S02 (organizations "strongly encouraged to look deeply at their unique risk characteristics"), S08 (periodic review of application risk profile).
- agreement: majority; certainty: inferred (the revisit trigger is not stated as a rule in S02 or S08; a secondary page stated it and was not used).

**SECD-C05** — Set a target maturity per practice from context; a higher level in one practice does not require it in the others.
- level: practice; stack: neutral; sources: S09.
- agreement: consensus; certainty: grounded.

**SECD-C06** — Treat descriptive benchmark data as evidence of what peers do, not as the verdict on what to do.
- level: principle; stack: neutral; sources: S10 (descriptive, observed practices), brief selection rule.
- agreement: consensus; certainty: inferred (S10 states descriptive; the consequence is derived).

**SECD-C07** — Use a maturity model as a cycle: assess current practice, set targets, build a roadmap, take prescriptive activity guidance from the model.
- level: practice; stack: neutral; sources: S09, S05.
- agreement: consensus; certainty: grounded.

**SECD-C08** — Every change to software should pass a floor of developer security testing: threat model, static code scan for top bugs, heuristic search for hardcoded secrets, run with built-in checks, black-box tests from specifications and threats, structural tests to reach at least 80% statement coverage, tests from past bugs, a fuzzer, and a web application scanner if the software serves a web service.
- level: decision; stack: neutral (scanner item: web services); sources: S11 (section 2), S22 (static analysis MUST, dynamic analysis SUGGESTED at the base badge level), S06.
- agreement: majority; certainty: grounded.
- positions: floor as listed (NIST) serves confidence at low cost and applies to any developer; fuller programmes (SAMM maturity 2-3: application-specific automation, regular penetration tests) serve higher assurance and win under high criticality or regulation.

**SECD-C09** — A verification floor is a lower bar, not best practice, and the concrete process must be tailored to the product, language, toolchain and lifecycle.
- level: principle; stack: neutral; sources: S11 (sections 1 and 1.3: "not a guide to most effective practices"; process "must be very specific and tailored").
- agreement: consensus; certainty: grounded.

**SECD-C10** — Threat modelling output should select test cases and the code that gets focused review, not stand alone.
- level: practice; stack: neutral; sources: S11 (2.1, 2.6); boundary: TRANS.
- agreement: consensus; certainty: grounded.

**SECD-C11** — Run static analysis as soon as code is written and repeat it automatically (every commit, or at least daily), so that no new weaknesses go unreported.
- level: practice; stack: neutral; sources: S11 (2.2, 2.3), S22 (static_analysis_often SUGGESTED), S20 ("as early as possible in the development cycle").
- agreement: majority; certainty: grounded.
- positions: per-commit or in code review (Google, S19) serves speed of feedback; nightly for slow whole-system or sanitizer runs (S20) serves cost of ownership; both held by the same sources for different tool speeds.

**SECD-C12** — Static analysis has known blind spots and false positives, so teams should standardise on tools, keep a "must fix" list, triage and suppress deliberately, and use more than one analyzer where weakness classes differ.
- level: practice; stack: neutral; sources: S11 (3.6 text: weak on authentication, access control, cryptography use; false positives; run more than one analyzer), S20 (false positive and false negative tradeoffs).
- agreement: consensus; certainty: grounded.

**SECD-C13** — Decide which security findings block a change and which advise, and state who may waive a block.
- level: decision; stack: neutral; sources: S19 (analysis in code review; highest-confidence checks pushed into compilers as errors because "developers ignore compiler warnings"), S11 (fix "must fix" bugs), S22 (static_analysis_fixed MUST for confirmed exploitable medium-and-higher findings), S18 ("free to select tools and the exact location"), S20.
- agreement: contested; certainty: grounded for each position, inferred for the synthesis.
- positions: (a) block on a curated high-confidence set, advise on the rest (Google, NIST must-fix list); force: delivery speed with developer trust; wins when noise is nonzero, which is almost always. (b) Block on confirmed exploitable findings above a severity (OpenSSF, applied at release); force: security; wins for public-facing or regulated software. (c) Leave placement to the team (OWASP DevSecOps); force: team cognitive load; loses on consistency. Boundary with TRANS-C37.

**SECD-C14** — Measure the effective false-positive rate as developers perceive it, keep each check under a stated budget (Google: at most 10%), and disable or fix checks that exceed it.
- level: practice; stack: neutral; sources: S19 (Tricorder: under 10% effective false positives, platform just below 5%; feedback channel), S20, S27 (interview study of 20 developers: false positives and presentation are barriers to use), S11.
- agreement: majority; certainty: grounded (the 10% figure is one organisation's policy, not a standard).

**SECD-C15** — Run fuzzing continuously or at least pre-release, on components and on the whole system, because it finds input-handling bugs that tests do not cover and denies attackers the same tool.
- level: practice; stack: neutral (harness effort differs by language); sources: S11 (2.9, 3.4), S20.
- agreement: majority; certainty: grounded.

**SECD-C16** — If the software serves a web interface, run a dynamic scanner (DAST) or interactive tool (IAST) against a running instance.
- level: practice; stack: web; sources: S11 (2.10), S18, S22 (dynamic_analysis).
- agreement: majority; certainty: grounded. Note: OpenSSF marks dynamic analysis SUGGESTED at the base level and MUST at a higher badge level (criteria page 2).

**SECD-C17** — Run slower dynamic pipelines (sanitizers, run-time assertions) on a schedule such as nightly rather than on every change.
- level: practice; stack: native languages for sanitizers (C and C++ named); sources: S20, S22 (dynamic_analysis_enable_assertions).
- agreement: majority; certainty: grounded.

**SECD-C18** — Combine automated testing (scalable baseline) with manual expert testing (deep understanding of business logic); automation frees experts for complex attack vectors.
- level: principle; stack: neutral; sources: S06 (streams A and B), S17 (tools for breadth, human guide for depth).
- agreement: consensus; certainty: grounded.

**SECD-C19** — Direct manual security testing first at the highest-risk components and let regular penetration testing follow as the practice matures.
- level: practice; stack: neutral; sources: S06 (stream B maturity 1: manual testing of high-risk components; maturity 2: manual penetration testing).
- agreement: majority; certainty: inferred (single model; no source gives pen-test frequency).

**SECD-C20** — Security tests should also check that detection works: penetration tests and DAST scans that raise no alert indicate a monitoring failure.
- level: principle; stack: neutral; sources: S16 (Description).
- agreement: consensus; certainty: grounded (one authoritative source).

**SECD-C21** — Fix the bugs a verification step finds, change the process to catch that class earlier, and where possible choose an approach (such as a language) that precludes the class.
- level: principle; stack: neutral; sources: S11 (section 2, 2.8).
- agreement: consensus; certainty: grounded.

**SECD-C22** — Apply the same verification to included libraries, packages and services as to own code.
- level: practice; stack: neutral; sources: S11 (2.11); boundary: ADOPT.
- agreement: consensus; certainty: grounded.

**SECD-C23** — Publish how to report a vulnerability, offer a private channel, answer within a stated time (OpenSSF: 14 days), fix known medium-or-higher vulnerabilities within a stated time (OpenSSF: 60 days), and announce the contact in a standard place (security.txt with Contact and Expires).
- level: practice; stack: neutral; sources: S22, S26, S25.
- agreement: consensus; certainty: grounded (day counts are one project's criteria).

**SECD-C24** — Start with a vulnerability disclosure policy; add a paid bounty only after weighing cost, organisational competence and maturity.
- level: decision; stack: neutral; sources: S25 ("most effective methods ... high return on investment"; "carefully weigh the cost, organizational competence, and maturity"), S22.
- agreement: contested; certainty: grounded for the government position, open for the commercial position (only vendor documentation surfaced, not read).
- positions: disclosure policy only (OMB): serves cost of ownership and control; wins when triage capacity is small. Bounty added (OMB allows it after weighing): serves speed of finding; wins with mature triage and wide attack surface. Periodic pen test alone: serves control and scope; wins when the system cannot be exposed to outside researchers. No source read compares yield.

**SECD-C25** — Log security-relevant events: authentication successes and failures, authorization failures, input validation failures, administrative actions, sensitive data access, security control failures and bypass attempts.
- level: practice; stack: neutral; sources: S03 (V16.3), S15, S16.
- agreement: consensus; certainty: grounded. Note: all V16 logging requirements are level 2 or 3 in ASVS 5.0, so an application held to level 1 is not required to log security events.

**SECD-C26** — Keep an inventory of what is logged at each layer, record who, what, when and where on every entry, synchronise time sources (UTC), use a common format, and send logs only to documented destinations.
- level: practice; stack: neutral; sources: S03 (V16.1, V16.2).
- agreement: consensus; certainty: grounded.

**SECD-C27** — Protect logs: encode against log injection, prevent modification, restrict and monitor access, ship them to a logically separate system for analysis, detection and alerting.
- level: practice; stack: neutral; sources: S03 (V16.4), S15, S16, S21 ("difficult to alter" and remote centralised logging).
- agreement: consensus; certainty: grounded.

**SECD-C28** — Logging without alerting and response is a failure: the application and platform must detect and escalate active attacks in near real time, and must detect when logging stops.
- level: principle; stack: neutral; sources: S16, S15; S03 (states alerting and correlation are out of scope of ASVS).
- agreement: consensus; certainty: grounded. Gap noted: the leading verification standard does not verify alerting.

**SECD-C29** — Time to detect (dwell time) is the cost to manage: detection delays of months raise damage, and one source reports an average of about 200 days to discover a compromise.
- level: principle; stack: neutral; sources: S07 (detection delays "months or years"), S21 (200-day figure, undated in the chapter).
- agreement: majority; certainty: grounded as quoted; the figure is dated and open as a current value.

**SECD-C30** — Incident response should be integrated into cybersecurity risk management, with lessons shared as soon as identified and improvements fed back into safeguards and detection.
- level: principle; stack: neutral; sources: S12 (introduction; Improvement notes), S07; boundary: OPERATE.
- agreement: consensus; certainty: grounded.

**SECD-C31** — Where the detection platform may change, express detection rules in a tool-neutral format so they survive a platform exit.
- level: decision; stack: detection tooling; sources: S28 (vendor-neutral rules convertible to several platforms).
- agreement: majority; certainty: inferred (one T3 source; the exit-risk argument is mine).

**SECD-C32** — Set log retention explicitly: long enough for investigation, no longer than the legal or purpose limit.
- level: decision; stack: neutral; sources: S15 ("must not be kept beyond this time"), S21 (long retention supports forensics; tiered warm and cold storage; degrade to summaries; consult privacy colleagues), S23 (Article 5(1)(e)).
- agreement: contested; certainty: grounded for each position.
- positions: (a) retain for the legal minimum and delete (OWASP, GDPR): serves privacy and cost; wins when logs hold personal data. (b) Retain long, tier by age (Google): serves investigation power; wins when dwell time is long and logs can be pseudonymised. Neither source gives a number.

**SECD-C33** — Never log passwords, tokens, keys, connection strings, payment data, session identifiers (or hash them), or personal data without legal justification; apply logging by the data's protection level.
- level: practice; stack: neutral; sources: S15, S03 (V16.2.5).
- agreement: consensus; certainty: grounded.

**SECD-C34** — Where logs must support investigation but not identification, pseudonymise so investigators can follow one user's timeline without learning who the user is.
- level: practice; stack: neutral; sources: S21.
- agreement: majority; certainty: grounded (one source).

**SECD-C35** — Collect and process only the personal data necessary for each stated purpose (data minimisation), by default.
- level: principle; stack: neutral (legal basis EU); sources: S23 (Art. 5(1)(c), 25(2)).
- agreement: consensus; certainty: grounded.

**SECD-C36** — Define retention per purpose and delete on schedule (storage limitation); automate deletion by retention class.
- level: principle; stack: neutral; sources: S23 (Art. 5(1)(e)), S04 (14.1.2 retention in documented safeguards; 14.2.7 level 3: data retention classification with automatic deletion).
- agreement: consensus; certainty: grounded.

**SECD-C37** — Identify and classify sensitive data into protection levels (including encoded forms) and document the required safeguards per level: encryption, integrity, retention, logging, database security, privacy.
- level: practice; stack: neutral; sources: S04 (14.1.1, 14.1.2, both level 2).
- agreement: consensus; certainty: grounded.

**SECD-C38** — Build data protection into design and defaults, with measures scaled to the state of the art, cost, and the nature, scope, context and risk of processing.
- level: principle; stack: neutral; sources: S23 (Art. 25(1)-(2)), S04.
- agreement: consensus; certainty: grounded.

**SECD-C39** — Decide how an erasure request reaches copies: caches, logs, derived stores, third parties and backups.
- level: decision; stack: neutral; sources: S23 (Art. 17(1)-(2): erase without undue delay, take reasonable technical steps to inform other processors; the text read does not address backups); boundary: RECOV.
- agreement: contested; certainty: open (backups and logs are not settled by any source read).

**SECD-C40** — Run a data protection impact assessment before high-risk processing, with at least a description of the processing and purposes, necessity and proportionality, risks to individuals, and mitigating measures.
- level: practice; stack: neutral; sources: S23 (Art. 35(1), 35(7)).
- agreement: consensus; certainty: grounded for the EU text, inferred as a stack-neutral practice; applies where regulation applies.

**SECD-C41** — Be able to determine within a short, stated clock what a breach touched, and record every breach with facts, effects and remedial action (EU: notify the authority within 72 hours where feasible).
- level: principle; stack: neutral; sources: S23 (Art. 33(1), 33(5)).
- agreement: consensus; certainty: grounded for text, inferred for the link to logging and classification (C26, C37).

**SECD-C42** — Run a regular process to test, assess and evaluate the effectiveness of security measures, including the ability to restore availability and access to personal data.
- level: principle; stack: neutral; sources: S23 (Art. 32(1)(c)-(d)); boundary: RECOV.
- agreement: consensus; certainty: grounded.

**SECD-C43** — Manage privacy as a risk through a framework (NIST Privacy Framework, voluntary, enterprise risk management) rather than as compliance alone.
- level: decision; stack: neutral; sources: S24 (version 1.1 was an initial public draft on the page read).
- agreement: majority; certainty: grounded as to purpose, open as to detail (framework body not read).

**SECD-C44** — Open: no source read shows that higher maturity-model scores or higher ASVS levels reduce incidents; the models measure programme activity and requirements coverage.
- level: principle; stack: neutral; sources: S02, S05, S09, S10 (none cites outcome evidence in the parts read).
- agreement: contested; certainty: open (I checked these five sources; the BSIMM report data and SAMM benchmark data were not read).

### Gaps

- Empirical evidence: on SAST and DAST effectiveness (only an abstract-level T3 study on usability), pen-test frequency, bug-bounty yield, detection tooling, maturity model against outcomes.
- Unread T1/T2 bodies: NIST SP 800-92 and SP 800-115, CISA and ASD logging guidance PDF, WSTG test chapters, ASVS 5.0 assessment chapter (0x04) and V13 configuration, SAMM maturity-level definitions and benchmark data, BSIMM activity list and report, CIS Controls, MITRE ATT&CK, Google SRE incident chapters, ISO/IEC 27001, 27701, 29147 (not freely public).
- Directive files named in the task addendum (target hierarchy and maintainer decisions, expected at the sibling `distill/` folder) were not present in the guideline folder when this slot ran; the hierarchy was therefore not used to select claims.
- Detection engineering (SIEM operation, rule quality, alert fatigue) rests on one T3 source; no minority school was found in T1/T2 sources.
- Privacy beyond the EU text: other jurisdictions, consent, data subject request tooling; GDPR was read from an unofficial mirror of the legal text, not the Official Journal.
- Threat modelling, secrets, secure SDLC framework and supply chain are covered by slots 06 and 02 and are not repeated here.
