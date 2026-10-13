# 14_recovery (RECOV): backup, restore, disaster recovery, continuity

## L1 headline

Public best practice on recovery is mature and largely consensual on principles (objectives per tier, restore-tested backups, isolated copies, exercised recovery paths) and divides only on how much standby to buy, how to isolate backups, whether to fail over automatically, and where to run drills; certainty is high on principles, medium on decisions because the T1 evidence is dominated by two cloud vendors (AWS, Azure) plus NIST.

Pinned:
- Sources by tier: T1 = 21, T2 = 2, T3 = 5, T4 = 0 (28 sources).
- Claims: 41.
- Contested topics: automatic versus manual failover; disaster-recovery drills in production versus non-production first; form of backup isolation (offline, immutable lock, separate account, other provider); standby recovery path versus no fallback path; hardening versus recovery speed (single source, open).
- Failed fetches on T1 sources: ISO 22301 page (HTTP 403, abstract obtained only through a search snippet, standard not read); NIST SP 800-34 Rev 1, NIST CSF 2.0 and NIST SP 800-57 returned unreadable PDF text and were recovered by local text extraction (read in full where cited). Non-T1 failure: Google DiRT article (ACM Queue, HTTP 403, not used as a source).

## L2 claims

Clusters (agreement, certainty, ids):

1. A backup is defined by whether it restores; the goal is recovery, not copies. Consensus, grounded. C01, C20, C21.
2. Replication and redundancy are not recoverability: protection against corruption, deletion and malicious change needs versioned or point-in-time copies kept apart from the live copy. Consensus, grounded. C02, C15, C16, C17.
3. Recovery objectives (time to restore service, tolerable data loss) are set per workload or data class from impact, tiered, and drive the strategy and its cost; avoid zero, arbitrary or over-strict values. Consensus, grounded. C03, C04, C05, C06, C07.
4. Decide what is backed up, what is reproducible, and back up everything needed to rebuild the service (data, configuration, infrastructure definitions, keys, recovery procedures). Consensus, grounded. C08, C09, C14, C32.
5. Keep at least one copy outside the failure and attack domain of production; attackers with production access target backups. Majority on the form, consensus on the need, grounded (T1) with T3 statistics. C10, C11, C12, C13, C40.
6. Restore testing: end to end, regular, automated, with explicit validation criteria and measured time; an untested backup is an assumption. Consensus, grounded. C20, C21, C22, C27, C18, C19.
7. Only exercised recovery paths work; keep few of them; exercise them on a ladder (tabletop, functional, full). Consensus on principle, contested on where and how. C23, C24, C25, C26.
8. Strategy ladder (backup and restore, pilot light, warm standby, active/active) chosen by objectives versus cost and complexity, never stricter than needed; backups remain needed at every rung. Majority, grounded. C28, C29.
9. Recovery must not depend on what failed: control plane, shared tooling, documentation and credentials held inside the failure domain. Consensus, grounded. C31, C32.
10. Failover and failback are separate designed processes with a declared trigger, roles, communication and an end criterion; the plan is kept current. Consensus, grounded. C06, C30, C33, C34, C36.
11. Boundaries: managed services and SaaS (provider owns infrastructure, customer owns data), privacy in backups (beyond-use rule), security of the recovered environment. Mostly one source each, grounded or inferred. C35, C37, C39, C41.

Live debates (forces in tension):
- Automatic versus manual failover: recovery time versus the cost of a false-alarm failover (C30).
- Drills in production versus non-production first: realism of confidence versus safety of the test (C25).
- Backup isolation form: offline air gap (strongest isolation, slowest restore, operational cost) versus immutable lock (fast, but trust in the platform and account) versus separate account or provider (exit risk, cost) (C11).
- Standby recovery path versus avoid fallback: speed of recovery versus the latent-bug risk of a rarely used path (C24).
- Hardening versus recovery speed: security versus time to recover; one source, open (C38).
- Active/active versus tiered standby: recovery time near zero versus complexity and cost (C29).

Candidate central decisions of the area (others depend on them):
1. Tiers and per-tier recovery objectives for service and for data, and the definition of a disaster (C03, C06).
2. Which data is irreplaceable and which is reproducible (C08), and what must be rebuildable from source (C32).
3. Backup isolation form and who can delete backups (C10, C11, C13).
4. Restore-test cadence, automation, and named owner (C19, C20).
5. Strategy rung per tier and failover trigger (C28, C30).
6. Where recovery tooling and documentation live so recovery does not depend on the failed system (C31).

Not covered: ISO 22301 and ISO 27031 text (paywalled, abstract only); detailed stack mechanics (database engines other than PostgreSQL, object stores other than S3, Kubernetes beyond etcd); Google DiRT and chaos-engineering drill design (source returned 403); regulated-sector recovery mandates (financial, health); cost models and insurance; recovery of developer-side assets (source hosting, CI service, issue trackers) beyond a pointer in C35; incident handling itself (OPERATE).

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| RECOV-S01 | T2 | Data Integrity: What You Read Is What You Wrote (Site Reliability Engineering, ch. 26) | Google | https://sre.google/sre-book/data-integrity/ | backups versus restores, defense in depth, recovery testing, replication is not recovery |
| RECOV-S02 | T1 | Disaster recovery options in the cloud (whitepaper) | AWS | https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html | four DR strategies, data disaster, control versus data plane, isolation by account |
| RECOV-S03 | T1 | REL09-BP01 Identify and back up all data, or reproduce it | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html | classifying data, backup versus reproduction, cadence from RPO |
| RECOV-S04 | T1 | REL09-BP04 Perform periodic recovery of the data | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html | restore test content, validation, timing, automation |
| RECOV-S05 | T1 | REL13-BP01 Define recovery objectives | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html | RTO and RPO, tiers, anti-patterns, dependency compatibility |
| RECOV-S06 | T1 | REL13-BP02 Use defined recovery strategies | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html | strategy ladder, cost trade-off, failover trigger, failback |
| RECOV-S07 | T1 | REL13-BP03 Test disaster recovery implementation | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html | test failover regularly, few recovery paths |
| RECOV-S08 | T1 | REL11-BP04 Rely on the data plane and not the control plane during recovery | AWS Well-Architected Reliability | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_avoid_control_plane.html | recovery dependencies, static stability |
| RECOV-S09 | T1 | Testing disaster recovery (whitepaper section) | AWS | https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.html | rarely executed paths, drift in the recovery site |
| RECOV-S10 | T1 | NIST SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems | NIST | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf (read via local text extraction, sections 3.1 to 3.6) | seven-step contingency process, BIA, MTD/RTO/RPO, alternate sites, tests, exercises, plan maintenance |
| RECOV-S11 | T1 | NIST Cybersecurity Framework 2.0 (CSWP 29) | NIST | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (read via local text extraction: RECOVER function, PR.DS-11) | outcomes for recovery plan execution and backups |
| RECOV-S12 | T1 | NIST SP 800-53 Rev. 5 control CP-9 System Backup | NIST (text read on a mirror of the control catalogue) | https://csf.tools/reference/nist-sp-800-53/r5/cp/cp-9/ | backup testing, separate storage, cryptographic protection, dual authorization |
| RECOV-S13 | T1 | #StopRansomware Guide | CISA | https://www.cisa.gov/stopransomware/ransomware-guide | offline encrypted backups, testing, golden images, infrastructure as code |
| RECOV-S14 | T1 | Offline backups in an online world | NCSC (UK) | https://www.ncsc.gov.uk/blog-post/offline-backups-in-an-online-world | offline backup rationale, 3-2-1, testing |
| RECOV-S15 | T1 | Architecture strategies for disaster recovery (RE:09) | Microsoft Azure Well-Architected Framework | https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery | tiers, thresholds, communication, drills, failback, plan currency, access during outage |
| RECOV-S16 | T1 | Disaster recovery planning guide | Google Cloud | https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide | RTO/RPO, cost relation, cold/warm/hot, test, security of recovered environment |
| RECOV-S17 | T1 | Continuous archiving and point-in-time recovery | PostgreSQL documentation | https://www.postgresql.org/docs/current/continuous-archiving.html | PITR, logical dumps not usable for it (stack: PostgreSQL) |
| RECOV-S18 | T1 | Locking objects with Object Lock | AWS S3 documentation | https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html | WORM retention, governance versus compliance mode (stack: AWS S3) |
| RECOV-S19 | T1 | NIST SP 800-57 Part 1 Rev. 5, Recommendation for Key Management | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf (read via local text extraction, 8.2.2.1 and Appendix B) | backup and recovery of keys |
| RECOV-S20 | T1 | Right to erasure: do we have to erase personal data from backup systems | ICO (UK regulator) | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/ | "beyond use" standard for backups |
| RECOV-S21 | T1 | Shared Responsibility Model | AWS | https://aws.amazon.com/compliance/shared-responsibility-model/ | provider infrastructure versus customer data |
| RECOV-S22 | T1 | Operating etcd clusters for Kubernetes | Kubernetes documentation | https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/ | cluster state backup (stack: Kubernetes) |
| RECOV-S23 | T2 | PhoenixServer | Martin Fowler | https://martinfowler.com/bliki/PhoenixServer.html | rebuilding from source as drift detection and recovery capability |
| RECOV-S24 | T3 | Postmortem of database outage of January 31 | GitLab | https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/ | case: backups that did not restore, no ownership, silent alert failure |
| RECOV-S25 | T3 | More details about the October 4 outage | Meta Engineering | https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/ | case: recovery tools depended on failed network; hardening versus recovery speed |
| RECOV-S26 | T3 | Avoiding fallback in distributed systems | AWS Builders' Library | https://builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/avoiding-fallback-in-distributed-systems | argument against rarely exercised fallback paths |
| RECOV-S27 | T3 | Sophos State of Ransomware reports (impact of compromised backups) | Sophos | read only through search-result summaries of https://assets.sophos.com/X24WTUEQ/at/539j6fwcmx6wk6whnhxc47/sophos-the-impact-of-compromised-backups-on-ransomware-outcomes-wp.pdf | survey statistics: share of victims whose backups were targeted (vendor survey, not read in full) |
| RECOV-S28 | T3 | 3-2-1-1-0 Rule | Veeam | read only through search-result summaries of https://bp.veeam.com/vbo/guide/design/3-2-1 | vendor extension of 3-2-1 with immutable copy and zero verification errors |

### Claims

**RECOV-C01**
- claim: Define a backup by whether it restores, not by whether it was taken; design and judge the backup system by recovery.
- level: principle | stack: neutral | sources: S01 (Backups versus archives; "backups don't matter; what matters is recovery"), S04 (anti-patterns: assuming a backup exists), S24 (backups never restored) | agreement: consensus | certainty: grounded

**RECOV-C02**
- claim: Treat replication and redundancy as availability measures, not recovery: keep versioned or point-in-time copies to recover from corruption, accidental or malicious deletion, because replication propagates damage.
- level: principle | stack: neutral | sources: S01 (Replication is not recovery), S02 (continuous replication may not protect against corruption or malicious deletion), S06 (additional practices for protecting data) | agreement: consensus | certainty: grounded

**RECOV-C03**
- claim: Set a recovery time objective and a recovery point objective per workload or data class, derived from the impact of downtime and data loss (financial, reputational, operational, regulatory), grouped into criticality tiers.
- level: decision | stack: neutral | sources: S05 (implementation guidance), S10 (3.2 BIA, MTD/RTO/RPO), S15 (Prioritize by business impact), S16 (RTO/RPO definitions) | agreement: consensus | certainty: grounded

**RECOV-C04**
- claim: Do not set arbitrary, zero, or stricter-than-needed recovery objectives; stricter objectives force costlier and more complex recovery than the business needs, and cost rises as the objective shortens.
- level: practice | stack: neutral | sources: S05 (anti-patterns), S10 (Cost balancing: shorter RTO costs more), S16 ("smaller RTO and RPO values often mean greater complexity"), S06 (avoid a strategy more stringent than needed) | agreement: consensus | certainty: grounded

**RECOV-C05**
- claim: Make a workload's recovery objectives compatible with those of the workloads it depends on and those that depend on it; derived data inherits the RPO of its sources.
- level: practice | stack: neutral | sources: S05 (questions 4 to 6) | agreement: consensus (one source read; none disagrees) | certainty: grounded

**RECOV-C06**
- claim: Define what counts as a disaster versus a major disruption versus a small incident, by user and business impact rather than by failing components, and build the thresholds into monitoring so recovery is triggered by criteria, not improvisation.
- level: decision | stack: neutral | sources: S15 (Define disaster thresholds; DR activation criteria), S11 (RC.RP-06 end of recovery declared on criteria) | agreement: consensus (one operational source, one framework) | certainty: grounded
- boundary: OPERATE

**RECOV-C07**
- claim: State data recovery (how much data may be lost, whether it is intact) and service recovery (how fast it runs again) as separate objectives; a data disaster (corruption, deletion, malicious change) has a recovery time greater than zero and a recovery point before its discovery even where service failover is near instant.
- level: principle | stack: neutral | sources: S01 (data integrity SLOs stricter than uptime; "data integrity without availability is the same as no data"), S02 (multi-site active/active: data disaster recovery time always greater than zero), S06 | agreement: consensus | certainty: grounded (S01, S02); the framing as two objectives is inferred from both

**RECOV-C08**
- claim: Identify all data sources and classify them by criticality; back up what cannot be recreated, and for data that can be reproduced from other sources define and test the reproduction path instead, provided it meets the RTO.
- level: decision | stack: neutral | sources: S03 (steps 1, 2, 4; reproduce versus back up), S05 (derived data) | agreement: consensus | certainty: grounded

**RECOV-C09**
- claim: Back up everything required to rebuild the service, not only user data: configuration, infrastructure definitions, application code and images, system-level information, the documentation of recovery procedures.
- level: practice | stack: neutral | sources: S02 (back up code and configuration; IaC), S12 (CP-9: user-level, system-level information and system documentation), S13 (golden images, template files offline) | agreement: consensus | certainty: grounded

**RECOV-C10**
- claim: Keep at least one backup copy outside the failure and attack domain of production, so that no single incident, fault, or compromised credential can destroy the data and every copy of it.
- level: principle | stack: neutral | sources: S13 (offline encrypted backups; ransomware deletes or encrypts accessible backups), S14 ("one or more backups offline"), S02 (separate account per region; cross-account copies protect against insider threat or account compromise), S12 (CP-9(3) separate facility), S18 (immutable retention), S01 (media isolation and diversity) | agreement: consensus on the need, majority on the form (see C11) | certainty: grounded

**RECOV-C11**
- claim: Choose the form of backup isolation by threat and by restore-speed requirement; state it and who can delete or shorten retention.
- level: decision | stack: neutral (S18 AWS S3 as stack example) | sources: S13, S14, S02, S18, S28, S01 | agreement: contested
- positions:
  - Offline or air-gapped copy: strongest against an attacker with network or credential access (S14, S13, S01 tape in the Gmail case where tape survived a redundancy failure); force: security, correctness; cost: slow restore, handling effort; wins when the threat model includes a destructive adversary and the restore time allows.
  - Immutable (write-once) retention enforced by the platform, in a mode even an account owner cannot override (S18 compliance mode) or one privileged users can (governance mode); force: speed of restore, reversibility; cost: trust in the platform, inability to delete early (retention versus erasure, see C37); wins when restores must be fast and the platform account itself is protected. S13 notes immutable storage needs cautious implementation due to compliance and cost.
  - Separate account, region, or provider (S02 account isolation, S13 multi-cloud "in case all accounts under the same vendor are impacted"); force: exit risk, blast radius; cost: duplicate tooling and cost; wins when a vendor-level or account-level loss is in the threat model.
  - Vendor extension "3-2-1-1-0" (one copy offline, air-gapped or immutable): S28 (T3, vendor).

**RECOV-C12**
- claim: As a baseline keep several copies on more than one kind of storage with one off-site (3-2-1), and add an immutable or offline copy and a verified restore (3-2-1-1-0) where destructive attack is in scope.
- level: practice | stack: neutral | sources: S14 ("at least 3 copies, on 2 devices, and 1 offsite"), S28 (3-2-1-1-0, vendor, summary only) | agreement: majority (3-2-1 official; the extension is vendor-originated) | certainty: grounded for 3-2-1; the extension is inferred from S28 snippets and S13, S18
- positions: 3-2-1 sufficient (S14) when threat is hardware, site or operator error; 3-2-1-1-0 (S28) when ransomware or insider deletion is in scope.

**RECOV-C13**
- claim: Protect backups' confidentiality, integrity and availability: encrypt them, restrict write and delete rights, and require dual authorization for deletion or destruction of backup information.
- level: practice | stack: neutral | sources: S12 (CP-9 base, CP-9(7), CP-9(8)), S13 (encrypted backups) | agreement: consensus | certainty: grounded
- boundary: SECD

**RECOV-C14**
- claim: Back up cryptographic keys and the information needed to use them, on independent secure storage and separately from the encrypted data, because encrypted data cannot be recovered when the key is lost; not every key needs backing up, so decide per key type.
- level: practice | stack: neutral | sources: S19 (8.2.2.1 backup storage; "encrypted information cannot be transformed back ... if the decryption key is lost") | agreement: consensus (one source) | certainty: grounded
- boundary: TRANS

**RECOV-C15**
- claim: Layer protection for data: a first layer that makes deletion reversible (soft deletion with a retention delay), a second layer of backups with tiered retention and locality, and a third layer of early detection that catches corruption before it spreads.
- level: practice | stack: neutral | sources: S01 (Defense in depth: three layers; soft deletion delays of 15 to 60 days; out-of-band validators), S02 (S3 versioning for human-error disasters) | agreement: consensus | certainty: grounded
- boundary: DATA

**RECOV-C16**
- claim: Choose backup frequency from the RPO and backup locality from the RTO; provide point-in-time recovery where corruption may be discovered late.
- level: practice | stack: neutral | sources: S01 (Choosing a strategy; point-in-time recovery), S02 (backup frequency determines achievable recovery point), S03 (cadence from RPO), S17 | agreement: consensus | certainty: grounded

**RECOV-C17**
- claim: Where point-in-time recovery of a database is required, use the engine's continuous archiving of the transaction log with base backups; a logical dump alone cannot be used for it.
- level: practice | stack: PostgreSQL (pointer for the stack guideline) | sources: S17 ("pg_dump ... cannot be used as part of a continuous-archiving solution"; stop replay at any point) | agreement: consensus (one engine's official documentation) | certainty: grounded

**RECOV-C18**
- claim: Monitor backup and restore jobs and route their failure alerts over a path that is itself verified; a failure notice that is never delivered is equivalent to no monitoring.
- level: practice | stack: neutral | sources: S24 (alert emails were rejected, nobody saw failures), S01 (monitoring during recovery, trust but verify) | agreement: consensus | certainty: inferred (from S24 case and S01)

**RECOV-C19**
- claim: Name an owner for data durability, including the regular testing of backup and restore; a procedure nobody owns is not tested.
- level: practice | stack: neutral | sources: S24 ("no ownership ... nobody was responsible for testing"; remediation: assign ownership), S04 (notify stakeholders on failed validation) | agreement: consensus | certainty: inferred (one case study, consistent with S04)

**RECOV-C20**
- claim: Test recovery end to end on a regular schedule, automate the test, and run it from the same procedures used in a real recovery; an untested backup, restore path or recovery plan is an assumption.
- level: principle | stack: neutral | sources: S01 ("You only know that you can recover ... if you actually do so"; continuous automated testing), S04 (anti-patterns; automate), S12 (CP-9(1), CP-9(2)), S11 (PR.DS-11 backups "created, protected, maintained, and tested"), S10 (3.5.1), S16, S15 | agreement: consensus | certainty: grounded

**RECOV-C21**
- claim: A restore test checks, against criteria fixed beforehand, that data is present, uncorrupted, accessible and within the RPO, and that the restore completes within the RTO with enough resources and without hidden external dependencies.
- level: practice | stack: neutral | sources: S04 (steps 2, 6, 7; checksum comparison), S01 (what the test reveals: validity, resources, wall time, monitoring, external dependencies) | agreement: consensus | certainty: grounded

**RECOV-C22**
- claim: Verify the integrity of backups before restoring from them, and verify the integrity of restored assets before declaring service restored.
- level: practice | stack: neutral | sources: S11 (RC.RP-03, RC.RP-05), S04 | agreement: consensus | certainty: grounded

**RECOV-C23**
- claim: Exercise every recovery path you rely on, and keep the number of recovery paths small, because the only recovery that works is the one tested frequently; also check drift in the recovery site (capacity, quotas, images, configuration).
- level: principle | stack: neutral | sources: S07 ("the only error recovery that works is the path you test frequently"), S09 (drift and quotas in the DR region), S01 ("components that aren't continually exercised fail when you need them most") | agreement: consensus | certainty: grounded

**RECOV-C24**
- claim: Decide per tier whether to maintain a standby recovery path, or to make the production path the only path (for example active in every location) and avoid a rarely used fallback.
- level: decision | stack: neutral | sources: S26, S06, S02, S07 | agreement: contested
- positions:
  - Maintain a standby (pilot light, warm standby) and rehearse it: serves recovery cost versus time (S06, S02); wins when objectives do not justify running everything everywhere and the standby is exercised regularly (S07).
  - Avoid fallback: a path used rarely hides latent bugs, is hard to test in distributed systems and can turn a partial outage into a full one; invest in the primary path instead (S26, T3, argued for request-time fallback, not for disaster recovery explicitly); serves correctness and cognitive load; wins when the fallback would run seldom and cannot be tested realistically. Reconciliation (inferred): S07 and S26 agree an unexercised path is a liability; they differ on whether to exercise it or remove it.

**RECOV-C25**
- claim: Decide where and how recovery drills run: in production or first in non-production, and combine scheduled drills with unannounced exercises.
- level: decision | stack: neutral | sources: S07, S09, S15 | agreement: contested
- positions:
  - Exercise failover in production regularly, regardless of need, for complex or critical recovery paths (S07, S09; AWS): serves realism of confidence; wins for critical paths where a staged environment cannot reproduce load or quotas.
  - Test in non-production first to validate safety, then production-level drills because they are "the only way to verify that your plan meets RTO and RPO ... in real conditions"; production drills can themselves cause severe failures (S15; Azure): serves safety of the test; wins when the blast radius of a failed drill is high or the procedure is new.
  - Both, as a ladder: tabletop, then dry run, then production-level, and surprise game days (S15); S10 describes tabletop and functional exercises and says tests should be "in as close to an operating environment as possible".

**RECOV-C26**
- claim: Use a ladder of exercises (discussion-based tabletop, functional exercise, full test), run them periodically and after changes to the system or the plan, and record an after-action report whose corrective actions update the plan.
- level: practice | stack: neutral | sources: S10 (3.5 TT&E; tabletop and functional exercises; after-action report), S15 (Practice with regular drills; test results as inputs) | agreement: consensus | certainty: grounded

**RECOV-C27**
- claim: Measure the restore or failover time and the achieved recovery point in every test, compare them with the objectives, and use the measured times, not estimates, as the planning minimum for recovery.
- level: practice | stack: neutral | sources: S04 (step 7), S15 ("use metrics from testing as the minimum time needed"), S01 | agreement: consensus | certainty: grounded

**RECOV-C28**
- claim: Choose the recovery strategy for each tier from the ladder (backup and restore; pilot light; warm standby; active/active, also called cold, warm, hot) by objectives against cost and complexity, and never implement a rung stricter than the objectives need.
- level: decision | stack: neutral | sources: S06 (RPO and RTO per strategy, cost and complexity increasing), S02, S16 (cold, warm, hot), S10 (3.4.3 alternate sites; cost balance), S15 (cold and warm standby) | agreement: consensus | certainty: grounded
- note: the rung boundaries (for example "RTO within 24 hours" for backup and restore) are AWS figures, not general.

**RECOV-C29**
- claim: Choose active/active only when the business requirement for near-zero recovery time justifies the most complex and costly option; it does not remove the need for backups and for a tested data-disaster recovery.
- level: decision | stack: neutral | sources: S06 ("should only be selected when business requirements necessitate it"), S02 (backup and recovery still required; data disaster recovery time greater than zero; "most customers find that if they ... stand up a full environment ... use it active/active") | agreement: majority
- positions: active/active as an availability and DR choice together (S02: a full second environment is better used than idle; serves recovery time, utilisation; wins when running a full copy is accepted for other reasons such as latency or global audience, S06); warm standby as the economical and operationally simpler alternative (S02, S06; serves cost of ownership, cognitive load; wins when seconds-to-minutes recovery is acceptable).

**RECOV-C30**
- claim: Decide the failover trigger: initiate failover by a person through an automated, push-button procedure, or automatically on health signals; state the rule.
- level: decision | stack: neutral | sources: S02, S06, S15 | agreement: contested
- positions:
  - Manual initiation of automated steps: a false alarm incurs unavailability and data loss because recovery time and point are greater than zero (S02, S06; "automatically initiated failover ... should be used with caution"); serves reversibility, correctness; wins when failover itself costs data or availability.
  - Automated failover and recovery with trained oversight and tuned thresholds: serves recovery time; S15 recommends automating recovery wherever possible, with manual approval gates only when needed, while warning that automation carries risk and thresholds must be tuned to limit false positives; wins when the recovery time objective is shorter than a human can meet.

**RECOV-C31**
- claim: Make recovery independent of what failed: use only simple operations that remain available (data-plane actions, pre-provisioned capacity), and keep recovery tooling, runbooks, credentials, certificates, pipelines and contact paths where the failure cannot take them away, with offline copies for the worst case.
- level: principle | stack: neutral | sources: S08 (rely on data plane, not control plane; static stability), S02 (data plane for failover; restore is a control plane operation, so restore periodically), S15 (Ensure accessibility during outages: replicate DR assets across regions, offline or printed copies, predeploy pipelines), S25 (loss of DNS broke internal tools; access hindered), S13 (templates kept offline) | agreement: consensus | certainty: grounded
- note: the cloud control plane versus data plane vocabulary is AWS; the principle (recovery dependencies must survive the failure) is stack-neutral.

**RECOV-C32**
- claim: Define infrastructure and environment as code, and be able to rebuild from source on a clean machine or account; rebuilding regularly detects drift and is itself a recovery capability.
- level: practice | stack: neutral | sources: S02 (IaC to redeploy quickly; without it RTO may be exceeded), S13 (golden images, IaC templates kept offline), S23 (rebuild from scratch picks up all drift) | agreement: consensus | certainty: grounded
- boundary: DELIVER, TRANS

**RECOV-C33**
- claim: Plan failback as a separate, defined process from failover; the hard part is re-synchronising data stores, and the recovery site may instead be promoted to primary.
- level: practice | stack: neutral | sources: S06 (step 6 failback; rotating primary and recovery regions), S15 (Keep failback strategy separate from failover) | agreement: consensus | certainty: grounded

**RECOV-C34**
- claim: Keep the recovery plan, runbooks and contact lists current: review them periodically and on every change to the system, the organization or after a test or incident, and keep them accessible to the team.
- level: practice | stack: neutral | sources: S10 (3.6 plan maintenance; contact lists reviewed more often), S15 (Keep plans current, review about every six months), S06 (playbook available to all and reviewed) | agreement: consensus | certainty: grounded
- boundary: TRANS (documentation in sync)

**RECOV-C35**
- claim: For managed services and SaaS, assume the provider is responsible for its infrastructure and the customer for its own data; verify what the provider's backups cover and for whose recovery, and keep an independent copy of what the team cannot afford to lose.
- level: decision | stack: neutral (S21 AWS) | sources: S21 (customer manages its data; the document does not state backup responsibility explicitly), S11 (PR.DS-11) | agreement: consensus (one source) | certainty: inferred (S21 gives the split of responsibility; the backup consequence and the independent-copy advice are inferred)
- boundary: ADOPT, EXT

**RECOV-C36**
- claim: Assign recovery roles ahead of time (who declares, who executes, who communicates, who closes), prepare communication channels and templates, and declare the end of recovery by stated criteria once restored assets are verified.
- level: practice | stack: neutral | sources: S15 (Establish communication protocols), S11 (RC.RP-01 to 06, RC.CO-03, RC.CO-04), S10 (roles and responsibilities, 3.4.6) | agreement: consensus | certainty: grounded
- boundary: OPERATE

**RECOV-C37**
- claim: Give backups a retention schedule; when personal data must be erased, erase it from live systems and put backup copies beyond use until they are overwritten on schedule, and tell the data subject what happens to the backup.
- level: practice | stack: neutral (UK regulator) | sources: S20 | agreement: consensus (one regulator) | certainty: grounded
- boundary: SECD (privacy and retention); tension with immutable retention in C11 (open: how a locked backup is put beyond use is not addressed in the sources read)

**RECOV-C38**
- claim: Weigh, and state, the trade-off between hardening recovery-critical systems (physical and system protection) and the speed of recovery from a non-malicious failure.
- level: decision | stack: neutral | sources: S25 (hardening "slowed us down" but the trade-off "is worth it") | agreement: contested
- positions: accept slower recovery for rare events in return for day-to-day security (S25, T3, a single large operator); the opposing position (favour recovery speed) is not argued in any source read. certainty: open (one T3 source; the opposite side is unsourced).

**RECOV-C39**
- claim: Hold the recovered environment to the production security baseline (network separation, encryption, permissions, audit), and address the root cause before recovery starts so the failure does not repeat.
- level: practice | stack: neutral | sources: S16 (Security integration), S15 ("ensure root-cause issues are addressed before recovery begins") | agreement: consensus | certainty: grounded
- boundary: SECD

**RECOV-C40**
- claim: Include in the backup threat model an attacker who already holds production credentials: attackers attempt to find and delete or encrypt accessible backups, so a backup reachable with production credentials is not independent.
- level: principle | stack: neutral | sources: S13 ("many ransomware variants attempt to find and subsequently delete or encrypt accessible backups"), S14, S27 (vendor survey: 94 percent of ransomware victims reported attempts on their backups, 57 percent of attempts succeeded; summary read only) | agreement: consensus | certainty: grounded for the T1 statements; the percentages are T3 and read only in summaries
- boundary: SECD

**RECOV-C41**
- claim: Where cluster or platform state is the system's source of truth (for example the Kubernetes etcd store), back up that state explicitly and test its restore as part of the recovery plan; the platform's own high availability does not replace it.
- level: practice | stack: Kubernetes (pointer for the stack guideline) | sources: S22 ("make sure you have a back up plan for the data"; snapshot methods and a restore procedure) | agreement: consensus (one source) | certainty: grounded for the backup instruction; "HA does not replace it" is inferred from S01 and S02 (replication is not recovery)

### Gaps

- Open: ISO 22301 (business continuity management system) and ISO/IEC 27031: standard text not read; only a search-result abstract. Whether it adds claims beyond NIST SP 800-34 is unknown.
- Open: evidence for recovery drills at large scale (Google DiRT) not read (HTTP 403); chaos-engineering as a recovery test is only touched through AWS and Azure pages.
- Open: empirical evidence (peer-reviewed or survey) on the rate of failed restores and of tests found failing; only case studies (S24, S01 case studies) and a vendor survey summary (S27) were available.
- Open: how an immutable or offline backup is reconciled with erasure obligations (C11 versus C37).
- Open: whether manual versus automatic failover and production versus non-production drills have a neutral, non-vendor source; the positions come from AWS and Azure.
- Open: guidance for small scale (single operator, no standby site): the sources assume organizational DR programs; the tiering of C03 and C28 covers it in principle, but no source states the minimum viable restore practice. Inferred minimum from C01, C20 and C10: one isolated copy plus a periodic tested restore.
- Open: recovery of developer-side assets (source hosting, CI service, issue tracker, registry) not covered by any source read; C35 is a pointer only.
- Evidence weight: the T1 cloud sources are vendor documentation; S02 to S09 are all AWS and S15, S16 Azure and Google Cloud. Claims resting only on them are stated neutrally where the principle is vendor-independent, and flagged where the vocabulary or figures are vendor-specific (C28, C31).
- Not covered by design: incident handling (OPERATE), data and schema change safety (DATA), security testing (SECD).
