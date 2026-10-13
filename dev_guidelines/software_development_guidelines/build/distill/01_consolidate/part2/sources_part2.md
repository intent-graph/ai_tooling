# Source register, part 2

Part 2 of the source register. Part 1 (`../sources.md`) is read-only and holds REG-001 to REG-264. This part holds the sources cited by the part-2 ledger that part 1 does not hold, as REG-1001 and up (one row per distinct source: same normalised URL means the same source), and a table of the original source ids that resolve to a row of part 1.

Tiers (brief_shared): T1 normative or official, T2 recognized authority, T3 reputable practice, T4 community (never the sole ground of a claim). Tier of a new row is the highest among its origin ids. `maintainer` is REG-181 in part 1: not citable, no tier; round-3 slot 13 counted three maintainer claims as an internal source AUTH-S21, which is mapped to REG-181 here and not given a tier. Web-guideline source ids are prefixed `WEB:` and listed only when a claim imported into part 2 cites them.

Distinct new sources by tier: T1 70, T2 46, T3 38, T4 6; total 160. Original source ids resolved to part 1: 49.

## New sources (REG-1001 and up)

| reg | tier | title | author or body | url read | authoritative on | replaces (original ids) | notes |
|---|---|---|---|---|---|---|---|
| REG-1001 | T2 | Technical Debt | Martin Fowler | https://martinfowler.com/bliki/TechnicalDebt.html | interest and principal, where to pay | EVOL-S01 | - |
| REG-1002 | T2 | Deprecation (ch. 15, Software Engineering at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch15.html | code as liability, advisory vs compulsory deprecation, ownership | EVOL-S02 | - |
| REG-1003 | T2 | Large-Scale Changes (ch. 22, SWE at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch22.html | sharded, automated change, ownership | EVOL-S03 | - |
| REG-1004 | T2 | Branch by Abstraction | Martin Fowler | https://martinfowler.com/bliki/BranchByAbstraction.html | replacing a supplier without a long-lived branch | EVOL-S05 | - |
| REG-1005 | T2 | The WyCash Portfolio Management System (experience report, 1992) | Ward Cunningham | https://c2.com/doc/oopsla92.html | origin of the debt metaphor | EVOL-S06 | - |
| REG-1006 | T2 | Managing Technical Debt in Software Engineering (Dagstuhl Seminar 16162 report) | Avgeriou, Kruchten, Ozkaya, Seaman | https://utupub.fi/bitstream/10024/169748/1/dagrep_v006_i004_p110_s16162.pdf (executive summary and definition read, pages 1 to 6) | consensus definition and model of debt | EVOL-S07 | - |
| REG-1007 | T2 | Design Stamina Hypothesis | Martin Fowler | https://martinfowler.com/bliki/DesignStaminaHypothesis.html | design payoff line, status as conjecture | EVOL-S08 | - |
| REG-1008 | T2 | Opportunistic Refactoring | Martin Fowler | https://martinfowler.com/bliki/OpportunisticRefactoring.html | refactoring inside feature work | EVOL-S09 | - |
| REG-1009 | T2 | Refactoring Malapropism | Martin Fowler | https://martinfowler.com/bliki/RefactoringMalapropism.html | strict definition of refactoring | EVOL-S10 | - |
| REG-1010 | T2 | First, After, Later, Never | Kent Beck | https://newsletter.kentbeck.com/p/first-after-later-never (partial, paywalled) | timing of tidying | EVOL-S11 | - |
| REG-1011 | T2 | Architectural decision record process | AWS Prescriptive Guidance | https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | scope, states, ownership, review, immutability | EVOL-S13 | - |
| REG-1012 | T2 | Architecture decision records | Google Cloud Architecture Center | https://docs.cloud.google.com/architecture/architecture-decision-records | when to write, where to store | EVOL-S14 | - |
| REG-1013 | T2 | PEP 1, PEP Purpose and Guidelines | Python project | https://peps.python.org/pep-0001/ | proposal documents as decision record, statuses | EVOL-S15 | - |
| REG-1014 | T2 | What Is Software Engineering? (ch. 1, SWE at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch01.html | time, change, Hyrum's Law | EVOL-S16 | - |
| REG-1015 | T2 | Code maintainability | DORA | https://dora.dev/capabilities/code-maintainability/ | maintainability as a capability and its metrics | EVOL-S18 | - |
| REG-1016 | T2 | Microservices (article) | Fowler and Lewis | https://martinfowler.com/articles/microservices.html (decentralized governance section) ; https://martinfowler.com/articles/microservices.html | polyglot choice position / characteristics and trade-offs | EVOL-S19, WEB:ARCH-S03 | - |
| REG-1017 | T1 | Order, In the Matter of Knight Capital Americas LLC (Release 34-70694) | US Securities and Exchange Commission | https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf (pages 1 to 4) | finding on code left on servers | EVOL-S24 | - |
| REG-1018 | T1 | COST04-BP02 Implement a decommissioning process | AWS Well-Architected | https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_implement_process.html | decommissioning steps | EVOL-S25 | - |
| REG-1019 | T3 | MADR, Markdown Architectural Decision Records | ADR community | https://adr.github.io/madr/ | considered options, drivers, confirmation | EVOL-S26 | - |
| REG-1020 | T3 | Rust RFC template | Rust project | https://github.com/rust-lang/rfcs/blob/master/0000-template.md | drawbacks, alternatives, unresolved questions | EVOL-S27 | - |
| REG-1021 | T3 | Things You Should Never Do, Part I | Joel Spolsky | https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/ | case against rewrites | EVOL-S28 | - |
| REG-1022 | T3 | Choose Boring Technology (talk) | Dan McKinley | https://boringtechnology.club/ | replace, do not add; retire older tool / innovation tokens | EVOL-S29, WEB:ARCH-S04 | - |
| REG-1023 | T3 | How We Use Golden Paths to Solve Fragmentation | Spotify Engineering | https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/ | supported-not-mandated path | EVOL-S31 | - |
| REG-1024 | T3 | Lightweight Architecture Decision Records (Radar entry) | Thoughtworks | https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records | ADRs in source control; Adopt in 2018, not on current edition | EVOL-S33 | - |
| REG-1025 | T3 | Defining, Measuring, and Managing Technical Debt | Jaspan and Green, IEEE Software 2023 | https://research.google/pubs/defining-measuring-and-managing-technical-debt (abstract only) | peer-reviewed Google study of debt | EVOL-S34 | - |
| REG-1026 | T3 | Guide to our approach to the retirement of API endpoints | UK Office for National Statistics developer site | https://developer.ons.gov.uk/retirement/ | staged retirement with blackouts | EVOL-S35 | - |
| REG-1027 | T3 | Self-admitted technical debt studies (Potdar and Shihab and replications) | academic | read through a search-result summary only, no paper fetched | removal rates of debt marked in comments | EVOL-S36 | EVOL-S36: no full page read (as recorded by origin) |
| REG-1028 | T4 | Architecture decision record (repository) | Joel Parker Henderson | https://github.com/joelparkerhenderson/architecture-decision-record | mutable ADR minority view; when to skip | EVOL-S37 | - |
| REG-1029 | T4 | Getting away with rewriting code from scratch | programming is terrible (personal blog) | https://programmingisterrible.com/post/73023853878/getting-away-with-rewriting-code-from-scratch | case for rewriting under conditions | EVOL-S38 | - |
| REG-1030 | T4 | How Google Measures and Manages Tech Debt | DX newsletter | https://newsletter.getdx.com/p/measuring-and-managing-tech-debt | figures of the Google paper (secondary) | EVOL-S39 | - |
| REG-1031 | T4 | Lehman's Laws of Software Evolution | lawsofsoftwareengineering.com | read through a search-result summary only | continuing change, increasing complexity | EVOL-S40 | EVOL-S40: no full page read (as recorded by origin) |
| REG-1032 | T1 | NIST SP 800-218A, SSDF Community Profile for Generative AI and dual-use foundation models (July 2024) | NIST | https://csrc.nist.gov/pubs/sp/800/218/a/final (landing page) | scope: AI model development; no AI-generated-code statement seen | AUTH-S01 | - |
| REG-1033 | T1 | OWASP LLM06:2025 Excessive Agency | OWASP GenAI Security Project | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | excessive functionality, permissions, autonomy; prevention list | AUTH-S02 | - |
| REG-1034 | T1 | OWASP Top 10 for Agentic Applications for 2026 (published 9 Dec 2025) | OWASP GenAI Security Project | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (landing page only; body not read) | agentic risk taxonomy (ASI01 goal hijack, ASI02 tool misuse, ASI03 identity and privilege, ASI04 supply chain, ASI05 unexpected code execution); mitigations known from search-result summaries only | AUTH-S03 | AUTH-S03: no full page read (as recorded by origin) |
| REG-1035 | T1 | Security-Focused Guide for AI Code Assistant Instructions (1 Aug 2025) | OpenSSF Best Practices and AI/ML Working Groups | https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions | AI output does not bypass review, testing, static analysis; accountability stays with the developer | AUTH-S04 | - |
| REG-1036 | T1 | GitHub Copilot cloud agent: risks and built-in protections | GitHub Docs | https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations | vendor risk list and controls: human merge, requester cannot approve, single branch, firewall, workflow approval, signed commits and session logs | AUTH-S05 | - |
| REG-1037 | T1 | Claude Code: Security | Anthropic docs | https://code.claude.com/docs/en/security | permission modes, sandbox, cloud isolation, credential proxy, push restrictions, audit logging, user responsibility to review | AUTH-S07 | - |
| REG-1038 | T1 | Claude Code: Best practices | Anthropic docs | https://code.claude.com/docs/en/best-practices | give the agent a check to run, evidence over assertion, hooks versus advisory instructions, writer/reviewer fresh context, approval fatigue, checkpoints versus git | AUTH-S08 | - |
| REG-1039 | T1 | Codex: Agent approvals and security | OpenAI docs | https://learn.chatgpt.com/docs/agent-approvals-security (redirect from developers.openai.com) | default sandbox, network off by default, protected paths, prompt-injection note | AUTH-S09 | - |
| REG-1040 | T2 | Linux kernel documentation: tool-generated content | Linux kernel project | https://docs.kernel.org/process/generated-content.html | disclosure and defend-what-you-submit rule; scrutiny proportional to generated share | AUTH-S10 | - |
| REG-1041 | T2 | Introducing DORA's inaugural AI Capabilities Model (23 Sep 2025), with dora.dev 2025 landing and InfoQ summary (Sep 2025) | DORA / Google Cloud; InfoQ (T3 secondary for the stability sentence) | https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model ; https://dora.dev/research/2025/dora-report/ ; https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025 | seven capabilities; AI as amplifier; throughput now positive, instability still rising | AUTH-S11 | - |
| REG-1042 | T2 | Announcing the 2024 DORA report | DORA / Google Cloud | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report | 2024: AI adoption associated with -1.5% throughput and -7.2% stability, with the hedged batch-size explanation | AUTH-S12 | - |
| REG-1043 | T3 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (July 2025, arXiv preprint) | METR | https://arxiv.org/abs/2507.09089 (abstract) | randomized trial, 16 developers, 246 tasks: 19% slower with AI; expected -24%, believed -20% | AUTH-S13 | - |
| REG-1044 | T3 | Do Users Write More Insecure Code with AI Assistants? (ACM CCS 2023, peer reviewed) | Perry, Srivastava, Kumar, Boneh | https://arxiv.org/abs/2211.03622 (abstract) | user study, 47 participants: less secure code, more confidence | AUTH-S14 | - |
| REG-1045 | T3 | We Have a Package for You! Package hallucinations in code-generating LLMs (USENIX Security 2025, peer reviewed) | Spracklen et al. | https://arxiv.org/abs/2406.10279 (abstract) | 576,000 samples, 16 models: at least 5.2% (commercial) and 21.7% (open) hallucinated packages | AUTH-S15 | - |
| REG-1046 | T3 | Does AI-Assisted Coding Deliver? A difference-in-differences study of Cursor adoption (MSR 2026) | arXiv 2511.04427 | https://arxiv.org/abs/2511.04427 (abstract) | transient velocity gain, persistent rise in static-analysis warnings and complexity | AUTH-S16 | - |
| REG-1047 | T3 | AI Productivity Paradox (July 2025) | Faros AI (vendor telemetry, 10,000+ developers, 1,255 teams) | https://www.faros.ai/blog/ai-software-engineering | PRs +98%, review time +91%, PR size +154%, bugs per developer +9%, no company-level correlation | AUTH-S17 | - |
| REG-1048 | T3 | 2025 GenAI Code Security Report (30 Jul 2025) | Veracode (vendor) | via search-result summaries only; vendor page not read | 80 tasks, 100+ models: insecure in 45% of cases (secondary; not read directly) | AUTH-S18 | AUTH-S18: no full page read (as recorded by origin) |
| REG-1049 | T3 | Agents Rule of Two (31 Oct 2025) | Meta | https://ai.meta.com/blog/practical-ai-agent-security/ | no more than two of: untrusted input, sensitive access, state change or external communication | AUTH-S19 | - |
| REG-1050 | T3 | Stack Overflow Developer Survey 2025, AI section | Stack Overflow | https://survey.stackoverflow.co/2025/ai | 46% distrust vs 33% trust AI accuracy; "almost right" is the top frustration | AUTH-S20 | - |
| REG-1051 | T1 | Disaster recovery options in the cloud (whitepaper) | AWS | https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html | four DR strategies, data disaster, control versus data plane, isolation by account | RECOV-S02 | - |
| REG-1052 | T1 | REL09-BP01 Identify and back up all data, or reproduce it | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html | classifying data, backup versus reproduction, cadence from RPO | RECOV-S03 | - |
| REG-1053 | T1 | REL09-BP04 Perform periodic recovery of the data | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html | restore test content, validation, timing, automation | RECOV-S04 | - |
| REG-1054 | T1 | REL13-BP01 Define recovery objectives | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html | RTO and RPO, tiers, anti-patterns, dependency compatibility | RECOV-S05 | - |
| REG-1055 | T1 | REL13-BP02 Use defined recovery strategies | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html | strategy ladder, cost trade-off, failover trigger, failback | RECOV-S06 | - |
| REG-1056 | T1 | REL13-BP03 Test disaster recovery implementation | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html | test failover regularly, few recovery paths | RECOV-S07 | - |
| REG-1057 | T1 | REL11-BP04 Rely on the data plane and not the control plane during recovery | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_avoid_control_plane.html | recovery dependencies, static stability | RECOV-S08 | - |
| REG-1058 | T1 | Testing disaster recovery (whitepaper section) | AWS | https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.html | rarely executed paths, drift in the recovery site | RECOV-S09 | - |
| REG-1059 | T1 | NIST SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems | NIST | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf (read via local text extraction, sections 3.1 to 3.6) | seven-step contingency process, BIA, MTD/RTO/RPO, alternate sites, tests, exercises, plan maintenance | RECOV-S10 | - |
| REG-1060 | T1 | NIST Cybersecurity Framework 2.0 (CSWP 29) | NIST | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (read via local text extraction: RECOVER function, PR.DS-11) | outcomes for recovery plan execution and backups | RECOV-S11 | - |
| REG-1061 | T1 | NIST SP 800-53 Rev. 5 control CP-9 System Backup | NIST (text read on a mirror of the control catalogue) | https://csf.tools/reference/nist-sp-800-53/r5/cp/cp-9/ | backup testing, separate storage, cryptographic protection, dual authorization | RECOV-S12 | - |
| REG-1062 | T1 | #StopRansomware Guide | CISA | https://www.cisa.gov/stopransomware/ransomware-guide | offline encrypted backups, testing, golden images, infrastructure as code | RECOV-S13 | - |
| REG-1063 | T1 | Offline backups in an online world | NCSC (UK) | https://www.ncsc.gov.uk/blog-post/offline-backups-in-an-online-world | offline backup rationale, 3-2-1, testing | RECOV-S14 | - |
| REG-1064 | T1 | Architecture strategies for disaster recovery (RE:09) | Microsoft Azure Well-Architected Framework | https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery | tiers, thresholds, communication, drills, failback, plan currency, access during outage | RECOV-S15 | - |
| REG-1065 | T1 | Disaster recovery planning guide | Google Cloud | https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide | RTO/RPO, cost relation, cold/warm/hot, test, security of recovered environment | RECOV-S16 | - |
| REG-1066 | T1 | Continuous archiving and point-in-time recovery | PostgreSQL documentation | https://www.postgresql.org/docs/current/continuous-archiving.html | PITR, logical dumps not usable for it (stack: PostgreSQL) | RECOV-S17 | - |
| REG-1067 | T1 | Locking objects with Object Lock | AWS S3 documentation | https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html | WORM retention, governance versus compliance mode (stack: AWS S3) | RECOV-S18 | - |
| REG-1068 | T1 | NIST SP 800-57 Part 1 Rev. 5, Recommendation for Key Management | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf (read via local text extraction, 8.2.2.1 and Appendix B) | backup and recovery of keys | RECOV-S19 | - |
| REG-1069 | T1 | Right to erasure: do we have to erase personal data from backup systems | ICO (UK regulator) | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/ | "beyond use" standard for backups | RECOV-S20 | - |
| REG-1070 | T1 | Shared Responsibility Model | AWS | https://aws.amazon.com/compliance/shared-responsibility-model/ | provider infrastructure versus customer data | RECOV-S21 | - |
| REG-1071 | T1 | Operating etcd clusters for Kubernetes | Kubernetes documentation | https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/ | cluster state backup (stack: Kubernetes) | RECOV-S22 | - |
| REG-1072 | T2 | PhoenixServer | Martin Fowler | https://martinfowler.com/bliki/PhoenixServer.html | rebuilding from source as drift detection and recovery capability | RECOV-S23 | - |
| REG-1073 | T3 | Postmortem of database outage of January 31 | GitLab | https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/ | case: backups that did not restore, no ownership, silent alert failure | RECOV-S24 | - |
| REG-1074 | T3 | More details about the October 4 outage | Meta Engineering | https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/ | case: recovery tools depended on failed network; hardening versus recovery speed | RECOV-S25 | - |
| REG-1075 | T3 | Avoiding fallback in distributed systems | AWS Builders' Library | https://builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/avoiding-fallback-in-distributed-systems | argument against rarely exercised fallback paths | RECOV-S26 | - |
| REG-1076 | T3 | Sophos State of Ransomware reports (impact of compromised backups) | Sophos | read only through search-result summaries of https://assets.sophos.com/X24WTUEQ/at/539j6fwcmx6wk6whnhxc47/sophos-the-impact-of-compromised-backups-on-ransomware-outcomes-wp.pdf | survey statistics: share of victims whose backups were targeted (vendor survey, not read in full) | RECOV-S27 | RECOV-S27: no full page read (as recorded by origin) |
| REG-1077 | T3 | 3-2-1-1-0 Rule | Veeam | read only through search-result summaries of https://bp.veeam.com/vbo/guide/design/3-2-1 | vendor extension of 3-2-1 with immutable copy and zero verification errors | RECOV-S28 | RECOV-S28: no full page read (as recorded by origin) |
| REG-1078 | T1 | ASVS 5.0, chapter "What is the ASVS" | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x03-What-is-the-ASVS.md | levels, level choice, procurement and incremental use | SECD-S02 | - |
| REG-1079 | T1 | ASVS 5.0, V16 Security Logging and Error Handling | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md | logging requirements by level | SECD-S03 | - |
| REG-1080 | T1 | ASVS 5.0, V14 Data Protection | OWASP | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x23-V14-Data-Protection.md | classification, retention, sensitive data | SECD-S04 | - |
| REG-1081 | T1 | SAMM practice: Security Testing | OWASP | https://owaspsamm.org/model/verification/security-testing/ | automated and manual streams | SECD-S06 | - |
| REG-1082 | T1 | SAMM practice: Incident Management | OWASP | https://owaspsamm.org/model/operations/incident-management/ | detection and response streams | SECD-S07 | - |
| REG-1083 | T1 | SAMM practice: Threat Assessment | OWASP | https://owaspsamm.org/model/design/threat-assessment/ | risk profile and threat modelling streams | SECD-S08 | - |
| REG-1084 | T1 | SAMM about and self-assessment | OWASP | https://owaspsamm.org/about/ | how SAMM is meant to be used | SECD-S09 | - |
| REG-1085 | T3 | BSIMM maturity model page | Black Duck (BSIMM maintainer) | https://www.blackduck.com/services/security-program/bsimm-maturity-model.html (plus a search snippet of an early BSIMM description, not read in full) | BSIMM as descriptive benchmark | SECD-S10 | SECD-S10: no full page read (as recorded by origin) |
| REG-1086 | T1 | NIST IR 8397, Guidelines on Minimum Standards for Developer Verification of Software | NIST | https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8397.pdf (fetch tool unreadable, local text extraction read sections 1, 2, 3.4, SAST part) | minimum developer testing | SECD-S11 | - |
| REG-1087 | T1 | NIST SP 800-92, Guide to Computer Security Log Management | NIST | https://csrc.nist.gov/pubs/sp/800/92/final (abstract only) | existence and scope of log management guidance (2006) | SECD-S13 | - |
| REG-1088 | T1 | NIST SP 800-115, Technical Guide to Information Security Testing and Assessment | NIST | https://csrc.nist.gov/pubs/sp/800/115/final (abstract only) | existence and scope of security testing guidance (2008) | SECD-S14 | - |
| REG-1089 | T1 | OWASP Logging Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | what to log, protect, retain / what to log, never log, log protection, correlation / what to log, what never to log, storage, retention, protection, integrity, injection | SECD-S15, WEB:OPS-S18, WEB:THIN-S01 | - |
| REG-1090 | T1 | OWASP Top 10:2021 A09 Security Logging and Monitoring Failures | OWASP | https://top10.owasp.org/2021/A09_2021-Security_Logging_and_Monitoring_Failures | failure modes of detection / what to log, audit trail integrity (read after two redirects) | SECD-S16, WEB:THIN-S03 | - |
| REG-1091 | T1 | OWASP Web Security Testing Guide, home page | OWASP | https://wstg.owasp.org/latest/ (foreword excerpt only) | testing phases across lifecycle | SECD-S17 | - |
| REG-1092 | T2 | Building Secure and Reliable Systems, ch. 13 Testing Code | Google | https://google.github.io/building-secure-and-reliable-systems/raw/ch13.html | static, dynamic, fuzzing in CI | SECD-S20 | - |
| REG-1093 | T2 | Building Secure and Reliable Systems, ch. 15 Investigating Systems | Google | https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html | logging for investigation, retention, privacy | SECD-S21 | - |
| REG-1094 | T1 | OpenSSF Best Practices Badge criteria | OpenSSF | https://www.bestpractices.dev/en/criteria/0 and https://www.bestpractices.dev/en/criteria/2 | analysis and vulnerability-reporting criteria | SECD-S22 | - |
| REG-1095 | T1 | GDPR, Articles 5, 17, 25, 32, 33, 35 | European Union | https://gdpr-info.eu/art-5-gdpr/ (and /art-17, /art-25, /art-32, /art-33, /art-35) | legal principles on personal data (unofficial text mirror) | SECD-S23 | - |
| REG-1096 | T1 | NIST Privacy Framework 1.1 (initial public draft page) | NIST | https://www.nist.gov/privacy-framework | privacy risk management framework | SECD-S24 | - |
| REG-1097 | T1 | OMB Memorandum M-20-32, Improving Vulnerability Identification, Management, and Remediation | US Office of Management and Budget | https://www.whitehouse.gov/wp-content/uploads/2020/09/M-20-32.pdf (local text extraction) | disclosure policy and bug bounty | SECD-S25 | - |
| REG-1098 | T1 | RFC 9116, security.txt | IETF | https://www.rfc-editor.org/rfc/rfc9116 | machine-readable disclosure contact | SECD-S26 | - |
| REG-1099 | T3 | Why Don't Software Developers Use Static Analysis Tools to Find Bugs? (ICSE 2013) | Johnson, Song, Murphy-Hill, Bowdidge | search result summary of https://cs.gmu.edu/%7Ejohnsonb/docs/icse2013.pdf (paper not read; abstract level only) | peer-reviewed interview study of 20 developers | SECD-S27 | SECD-S27: no full page read (as recorded by origin) |
| REG-1100 | T3 | Sigma, generic signature format for log events | SigmaHQ maintainers | https://github.com/SigmaHQ/sigma | tool-neutral detection rule format | SECD-S28 | - |
| REG-1101 | T1 | Best practices for event logging and threat detection | CISA with ASD and international partners | https://www.cisa.gov/resources-tools/resources/best-practices-event-logging-and-threat-detection (landing page only) | existence of a five-area logging baseline | SECD-S29 | - |
| REG-1102 | T1 | Context propagation | OpenTelemetry | https://opentelemetry.io/docs/concepts/context-propagation/ | propagators, W3C default | WEB:OPS-S03 | - |
| REG-1103 | T1 | Logs specification | OpenTelemetry | https://opentelemetry.io/docs/specs/otel/logs/ | TraceId/SpanId in log records, log appenders | WEB:OPS-S04 | - |
| REG-1104 | T1 | Zero-code instrumentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/instrumentation/zero-code/ | automatic vs code-based instrumentation | WEB:OPS-S07 | - |
| REG-1105 | T1 | Lab and field data differences | web.dev | https://web.dev/articles/lab-and-field-data-differences | lab vs field (RUM) data | WEB:OPS-S12 | - |
| REG-1106 | T1 | Testing in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/testing/overview/ | test database, transaction isolation | WEB:OPS-S14 | - |
| REG-1107 | T1 | Django's cache framework | Django docs | https://docs.djangoproject.com/en/stable/topics/cache/ | cache levels, backends, local-memory caveat, vary | WEB:OPS-S15 | - |
| REG-1108 | T1 | pg_stat_statements | PostgreSQL docs | https://www.postgresql.org/docs/current/pgstatstatements.html | per-statement statistics | WEB:OPS-S17 | - |
| REG-1109 | T2 | The Twelve-Factor App (factors I codebase, III config, IV backing services, V build-release-run, VI processes, IX disposability, X dev/prod parity, XI logs, XII admin processes) | Wiggins et al. | https://12factor.net/ (pages /codebase /config /backing-services /build-release-run /processes /disposability /dev-prod-parity /logs /admin-processes) ; https://12factor.net/ | delivery and runtime contract of a deployable app / SaaS app build and run contract | WEB:OPS-S19, WEB:ARCH-S07 | - |
| REG-1110 | T2 | DORA capabilities | DORA (Google Cloud) | https://dora.dev/capabilities/ | capability list: continuous delivery, test automation, observability, database change management | WEB:OPS-S31 | - |
| REG-1111 | T2 | Two Hard Things | Fowler (attributing Karlton) | https://martinfowler.com/bliki/TwoHardThings.html | folklore only; supports "invalidation is hard", nothing normative | WEB:OPS-S34 | - |
| REG-1112 | T2 | Monolith First | Martin Fowler | https://martinfowler.com/bliki/MonolithFirst.html | start-as-monolith argument | WEB:ARCH-S01 | - |
| REG-1113 | T2 | Microservice Premium | Martin Fowler | https://martinfowler.com/bliki/MicroservicePremium.html | cost of microservices | WEB:ARCH-S02 | - |
| REG-1114 | T2 | Architecture Decision Record | Martin Fowler | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | ADR practice | WEB:ARCH-S06 | - |
| REG-1115 | T2 | Presentation Domain Data Layering | Martin Fowler | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | three-layer modularisation, team shape | WEB:ARCH-S08 | - |
| REG-1116 | T3 | The Majestic Monolith | David Heinemeier Hansson | https://signalvnoise.com/svn3/the-majestic-monolith/ | small-team monolith | WEB:ARCH-S09 | - |
| REG-1117 | T3 | Deconstructing the Monolith | Shopify Engineering | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity | modular monolith in practice | WEB:ARCH-S10 | - |
| REG-1118 | T2 | Sacrificial Architecture | Martin Fowler | https://martinfowler.com/bliki/SacrificialArchitecture.html | planned replacement | WEB:ARCH-S11 | - |
| REG-1119 | T2 | Evolutionary Architecture (book site) | Ford, Parsons, Kua | https://evolutionaryarchitecture.com/ | definition, fitness functions | WEB:ARCH-S12 | - |
| REG-1120 | T2 | Is High Quality Software Worth the Cost? | Martin Fowler | https://martinfowler.com/articles/is-quality-worth-cost.html | internal quality economics | WEB:ARCH-S14 | - |
| REG-1121 | T2 | Software Architecture Guide | Martin Fowler | https://martinfowler.com/architecture/ | what architecture is | WEB:ARCH-S15 | - |
| REG-1122 | T3 | Goodbye Microservices | Twilio Segment | https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/ (redirect from segment.com) | reverse migration case | WEB:ARCH-S16 | - |
| REG-1123 | T2 | Bounded Context | Martin Fowler | https://martinfowler.com/bliki/BoundedContext.html | model boundaries | WEB:ARCH-S17 | - |
| REG-1124 | T2 | REST dissertation ch. 4, Web architecture | Roy Fielding | https://www.ics.uci.edu/~fielding/pubs/dissertation/web_arch_domain.htm | styles as sets of constraints | WEB:ARCH-S18 | - |
| REG-1125 | T2 | REST dissertation ch. 5, REST | Roy Fielding | https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | constraints and their trade-offs | WEB:ARCH-S19 | - |
| REG-1126 | T1 | PostgreSQL docs, SELECT, locking clause | PostgreSQL Global Development Group | https://www.postgresql.org/docs/current/sql-select.html | SKIP LOCKED semantics | WEB:ARCH-S20 | - |
| REG-1127 | T2 | How Do Committees Invent? | Melvin Conway | https://www.melconway.com/Home/Committees_Paper.html | Conway's law | WEB:ARCH-S22 | - |
| REG-1128 | T4 | Postgres for Everything | Stephan Schmidt (amazingcto) | https://www.amazingcto.com/postgres-for-everything/ | the popular "just use Postgres" case | WEB:ARCH-S25 | - |
| REG-1129 | T4 | How to Collapse Your Stack Using PostgreSQL | Tiger Data (vendor, commercial interest) | https://www.tigerdata.com/blog/how-to-collapse-your-stack-using-postgresql-for-everything/ | vendor version of the case | WEB:ARCH-S26 | - |
| REG-1130 | T2 | Technical Debt Quadrant | Martin Fowler | https://martinfowler.com/bliki/TechnicalDebtQuadrant.html | prudent vs reckless debt | WEB:ARCH-S27 | - |
| REG-1131 | T1 | Django design philosophies | Django project | https://docs.djangoproject.com/en/stable/misc/design-philosophies/ | loose coupling, DRY, layer separation in a Python framework | WEB:ARCH-S28 | - |
| REG-1132 | T2 | Simplicity (SRE book ch. 9) | Google SRE | https://sre.google/sre-book/simplicity/ | simplicity and reliability | WEB:ARCH-S29 | - |
| REG-1133 | T2 | Integration Database | Martin Fowler | https://martinfowler.com/bliki/IntegrationDatabase.html | shared-database coupling | WEB:ARCH-S30 | - |
| REG-1134 | T3 | Fitness function-driven development | Thoughtworks | https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development | fitness functions in delivery | WEB:ARCH-S32 | - |
| REG-1135 | T1 | Software Supply Chain Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html | dependency management | WEB:SEC-S28 | - |
| REG-1136 | T1 | Logging Vocabulary Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html | event naming, timestamps | WEB:THIN-S02 | - |
| REG-1137 | T1 | Table Partitioning, removing old data | PostgreSQL docs (current) | https://www.postgresql.org/docs/current/ddl-partitioning.html | DROP/DETACH vs bulk DELETE | WEB:THIN-S04 | - |
| REG-1138 | T1 | CREATE TABLE | PostgreSQL docs (current, version 18) | https://www.postgresql.org/docs/current/sql-createtable.html | WITHOUT OVERLAPS, PERIOD | WEB:THIN-S05 | - |
| REG-1139 | T1 | Constraints | PostgreSQL docs (current, version 18) | https://www.postgresql.org/docs/current/ddl-constraints.html | exclusion constraints; list of constraint types / what the database enforces, null semantics | WEB:THIN-S06, WEB:DCON-S04 | - |
| REG-1140 | T1 | Overview of Trigger Behavior | PostgreSQL docs (current) | https://www.postgresql.org/docs/current/trigger-definition.html | trigger timing, transaction scope | WEB:THIN-S07 | - |
| REG-1141 | T1 | How to measure Core Web Vitals in the field | web.dev | https://web.dev/articles/vitals-field-measurement-best-practices | RUM practice | WEB:THIN-S15 | - |
| REG-1142 | T2 | Audit Log (Patterns of Enterprise Application Architecture, further development) | Martin Fowler | https://www.martinfowler.com/eaaDev/AuditLog.html | audit log pattern and its limits | WEB:THIN-S18 | - |
| REG-1143 | T2 | Domain Logic and SQL | Martin Fowler | https://martinfowler.com/articles/dblogic.html | logic in SQL vs application | WEB:THIN-S19 | - |
| REG-1144 | T2 | A Simple Guide to Five Normal Forms in Relational Database Theory (CACM 26(2), 1983) | William Kent | https://www.bkent.net/Doc/simple5.htm (author's copy) | normalization | WEB:THIN-S20 | - |
| REG-1145 | T3 | Soft deletion probably isn't worth it | Brandur Leach (blog) | https://brandur.org/soft-deletion | critique of deleted_at | WEB:THIN-S21 | - |
| REG-1146 | T3 | Database normalization description (archived support article) | Microsoft Learn | https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description | beginner normalization; its statement "fourth normal form, also called Boyce-Codd Normal Form" is inaccurate and not used | WEB:THIN-S22 | - |
| REG-1147 | T1 | JSON Schema reference: object (additionalProperties, required, unevaluatedProperties), json-schema.org | - | https://json-schema.org/understanding-json-schema/reference/object | open vs closed objects, required vs null | WEB:DCON-S01 | - |
| REG-1148 | T1 | JSON Schema reference: type, json-schema.org | - | https://json-schema.org/understanding-json-schema/reference/type | null, integer/number, format as annotation | WEB:DCON-S02 | - |
| REG-1149 | T1 | OpenAPI Specification (latest), OpenAPI Initiative | - | https://spec.openapis.org/oas/latest.html | purpose of an API description, 3.1 and JSON Schema 2020-12 | WEB:DCON-S03 | - |
| REG-1150 | T1 | FastAPI docs: Response Model | - | https://fastapi.tiangolo.com/tutorial/response-model/ | code-first schema from types, output filtering | WEB:DCON-S06 | - |
| REG-1151 | T2 | Parse, don't validate, Alexis King | - | https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/ | parsing at the boundary, illegal states | WEB:DCON-S07 | - |
| REG-1152 | T2 | Consumer-Driven Contracts, Ian Robinson on martinfowler.com | - | https://martinfowler.com/articles/consumerDrivenContracts.html | provider vs consumer contracts | WEB:DCON-S09 | - |
| REG-1153 | T2 | Open Data Contract Standard (overview, fundamentals, schema pages), Bitol / Linux Foundation | - | https://bitol-io.github.io/open-data-contract-standard/latest/ (and /fundamentals/, /schema/) | data-engineering contract fields | WEB:DCON-S11 | - |
| REG-1154 | T3 | Pydantic docs: JSON Schema | - | https://pydantic.dev/docs/validation/latest/concepts/json_schema/ | model to JSON Schema, modes | WEB:DCON-S12 | - |
| REG-1155 | T3 | Pydantic docs: Strict Mode | - | https://pydantic.dev/docs/validation/latest/concepts/strict_mode/ | coercion, strict, JSON input | WEB:DCON-S13 | - |
| REG-1156 | T3 | PostgREST docs: Schema Isolation (read from source copy on GitHub; docs host returned 429) | - | https://raw.githubusercontent.com/PostgREST/postgrest-docs/main/docs/explanations/schema_isolation.rst | database as API | WEB:DCON-S14 | - |
| REG-1157 | T3 | Pact docs: how Pact works | - | https://docs.pact.io/getting_started/how_pact_works | pact file, provider verification | WEB:DCON-S16 | - |
| REG-1158 | T3 | oasdiff README | - | https://github.com/oasdiff/oasdiff | breaking-change detection in CI | WEB:DCON-S17 | - |
| REG-1159 | T3 | openapi-typescript docs | - | https://openapi-ts.dev/introduction | TypeScript types from OpenAPI | WEB:DCON-S18 | - |
| REG-1160 | T3 | SQLModel docs, Sebastian Ramirez | - | https://sqlmodel.tiangolo.com/ | one class for table and validation | WEB:DCON-S19 | - |

## Original source ids that resolve to a row of part 1

| original id | part-1 reg | part-1 tier | origin tier | notes |
|---|---|---|---|---|
| EVOL-S04 | REG-105 | T2 | T2 | - |
| EVOL-S12 | REG-154 | T2 | T2 | - |
| EVOL-S17 | REG-106 | T2 | T2 | - |
| EVOL-S20 | REG-030 | T1 | T2 | - |
| EVOL-S21 | REG-183 | T1 | T1 | - |
| EVOL-S22 | REG-182 | T1 | T1 | - |
| EVOL-S23 | REG-008 | T1 | T1 | same document as REG-008 under its redirected path (docs/reference/deprecation-policy to docs/reference/using-api/deprecation-policy) |
| EVOL-S30 | REG-013 | T2 | T3 | - |
| EVOL-S32 | REG-015 | T2 | T3 | - |
| AUTH-S06 | REG-114 | T1 | T1 | - |
| AUTH-S21 | REG-181 | maintainer | internal | internal maintainer inputs (MAINT-C62, MAINT-C63, DELIVER-C49): not an outside source, not citable |
| RECOV-S01 | REG-250 | T2 | T2 | - |
| SECD-S01 | REG-180 | T1 | T1 | - |
| SECD-S05 | REG-171 | T1 | T1 | - |
| SECD-S12 | REG-123 | T1 | T1 | same publication as REG-123 (PDF read here, landing page in part 1), as part 1 did for NIST SP 800-218 |
| SECD-S18 | REG-169 | T1 | T1 | - |
| SECD-S19 | REG-052 | T2 | T2 | - |
| WEB:OPS-S01 | REG-122 | T1 | T1 | - |
| WEB:OPS-S02 | REG-118 | T1 | T1 | - |
| WEB:OPS-S05 | REG-119 | T1 | T1 | - |
| WEB:OPS-S20 | REG-044 | T2 | T2 | - |
| WEB:OPS-S21 | REG-072 | T2 | T2 | - |
| WEB:OPS-S22 | REG-070 | T2 | T2 | - |
| WEB:OPS-S23 | REG-105 | T2 | T2 | - |
| WEB:OPS-S24 | REG-087 | T2 | T2 | - |
| WEB:OPS-S25 | REG-107 | T2 | T2 | - |
| WEB:OPS-S26 | REG-244 | T2 | T2 | - |
| WEB:OPS-S27 | REG-089 | T2 | T2 | - |
| WEB:OPS-S28 | REG-124 | T2 | T2 | - |
| WEB:OPS-S29 | REG-125 | T2 | T2 | - |
| WEB:OPS-S30 | REG-082 | T2 | T2 | - |
| WEB:OPS-S32 | REG-138 | T3 | T2 | origin tier T2 is higher than the part-1 tier T3; part 1 is read-only, tier kept as in part 1 |
| WEB:OPS-S33 | REG-241 | T3 | T2 | origin tier T2 is higher than the part-1 tier T3; part 1 is read-only, tier kept as in part 1 |
| WEB:OPS-S35 | REG-045 | T3 | T3 | - |
| WEB:OPS-S36 | REG-053 | T1 | T3 | - |
| WEB:ARCH-S05 | REG-154 | T2 | T2 | - |
| WEB:ARCH-S13 | REG-034 | T2 | T2 | - |
| WEB:ARCH-S21 | REG-033 | T2 | T2 | - |
| WEB:ARCH-S23 | REG-039 | T2 | T2 | - |
| WEB:ARCH-S31 | REG-244 | T2 | T2 | - |
| WEB:ARCH-S33 | REG-163 | T3 | T3 | - |
| WEB:SEC-S05 | REG-166 | T1 | T1 | - |
| WEB:SEC-S11 | REG-025 | T1 | T1 | - |
| WEB:SEC-S29 | REG-032 | T1 | T1 | - |
| WEB:SEC-S34 | REG-167 | T2 | T2 | - |
| WEB:SEC-S35 | REG-086 | T1 | T2 | - |
| WEB:DCON-S08 | REG-208 | T2 | T2 | - |
| WEB:DCON-S10 | REG-070 | T2 | T2 | - |
| WEB:DCON-S15 | REG-053 | T1 | T3 | - |
