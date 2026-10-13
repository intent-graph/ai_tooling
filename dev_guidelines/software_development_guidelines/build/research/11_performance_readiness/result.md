# Research result: 11_performance_readiness (area code PERF)

## L1 headline

Best practice on performance, load, capacity and operational readiness is well settled at principle level (measurable targets, percentile metrics, test beyond expected load on a production-like system, capacity modelled in resources, a pre-launch readiness review fed by incidents, versioned and rehearsed runbooks) but open at decision level (where and how often to run performance tests, test-environment fidelity, who runs the readiness review, how much telemetry to keep), and rests mostly on two large cloud-platform frameworks and Google's SRE books, with no standards-body text and no empirical study; certainty: grounded for what was read, inferred for syntheses, open for telemetry cost as a budget.

Pinned:
- Sources by tier: 35 sources: 14 T1, 16 T2, 4 T3, 1 T4.
- Claims: 44 (PERF-C01 to PERF-C44).
- Contested topics: test-environment fidelity (production-identical vs scaled-down vs production); real third-party calls vs mocks in load tests; performance tests per change vs scheduled vs pre-event; testing in production with live load; performance work early by design vs measured and late; capacity headroom vs cost (provision for peak vs autoscale); external reviewer vs self-service readiness review; head vs tail trace sampling.
- Failed fetches on T1 sources: Azure Well-Architected "workload supportability" page returned 404 and was not recovered (no readiness claim rests on it); the first AWS runbook URL returned an empty shell and was recovered at the correct URL (OPS07-BP03); the AWS Operational Readiness Reviews whitepaper returned only its introduction, so its checklist chapters and Appendix B were not read; the AWS reliability-pillar monitoring page returned an empty shell and was dropped.

## L2 claims

### 1. Clusters (agreement; certainty; claim ids)

- Performance needs measurable targets from user need, expressed as percentiles with pass/fail thresholds, split into per-layer budgets so a failing test localizes. Consensus; grounded. PERF-C01, C02, C03.
- Load testing must cover the whole workload, with representative traffic and data, past expected load to the breaking point, using a portfolio of test types matched to risk. Consensus; grounded. PERF-C05, C07, C08, C13.
- Results are only as good as the harness: open-loop load generation avoids coordinated omission; compare against baselines; detect regression and drift; hypothesis-driven experiments for changes. Majority; grounded, but the harness claim rests on one T3 source. PERF-C10, C11, C12.
- Where and when to test is contested: environment fidelity, mocks vs real third parties, per-change gate vs schedule, live-traffic tests. Contested; grounded positions. PERF-C04, C06, C09, C14, C15.
- Capacity planning is forward-looking, done before predicted change, measured in resources not request counts, derived from requirements and failure domains, and never a substitute for overload handling. Consensus; grounded. PERF-C18, C19, C20, C21, C24; headroom vs cost contested (C22); automation of planning is a scale-dependent minority (C23).
- Operational readiness is verified before launch by a curated, incident-fed, risk-tiered checklist and repeated periodically; who runs it is contested. Consensus on the practice, contested on the mechanism; grounded. PERF-C25, C26, C27, C28, C29.
- Runbooks and playbooks are versioned, owned, validated by a second person, linked from alerts, automated from short frequent ones outward, and rehearsed. Consensus; grounded (T1 AWS, T2 Google). PERF-C30, C31, C32, C33, C34.
- Synthetic monitoring complements internal metrics because it sees what users see even with no traffic; combine with real-user data. Majority; grounded for synthetic checks, real-user monitoring only from a T4 summary. PERF-C35, C36, C37, C38.
- Telemetry has a cost set by volume and cardinality; control it at design time by bounded labels, filtering and sampling, each with a stated loss of information. Majority; grounded for mechanisms, open for cost as an explicit budget. PERF-C39, C40, C41, C42, C43, C44.
- Performance work should follow measurement, but design-time resource estimation and early testing are also advised; contested. PERF-C16, C17.

### 2. Live debates (forces in tension)

- Test environment: production-identical (confidence, fidelity) vs scaled-down (cost) vs test in production (realism vs user impact). PERF-C04, C14.
- Performance gate per change vs scheduled runs: speed of feedback and regression locality vs noise and infrastructure cost. PERF-C09.
- Real third-party calls vs mocks under load: realism vs repeatability, third-party policy and cost. PERF-C06.
- Optimize early by design vs only after measurement: avoided rework vs cost of ownership and delivery speed. PERF-C16.
- Headroom: provision for peak (reliability, scaling lag) vs autoscale (cost). PERF-C22.
- Readiness review: independent reviewer (control, quality) vs self-service (delivery speed, scalability). PERF-C26.
- Tracing: head sampling (simplicity, cost) vs tail sampling (completeness of interesting traces, operational complexity). PERF-C41.

### 3. Candidate central decisions

- D-PERF-1: what the performance target is, and in which unit (percentile latency, throughput, resource budget), derived from which user need. Others depend on it: tests, SLOs, capacity.
- D-PERF-2: test fidelity and location (production-like, scaled, in production) per criticality, and what is mocked.
- D-PERF-3: when performance tests run (per change, nightly, before events) and what blocks a release.
- D-PERF-4: capacity model and headroom policy (resource unit, forecast horizon, peak vs autoscale).
- D-PERF-5: readiness gate: which changes or launches need a review, run by whom, with which checklist, re-run how often.
- D-PERF-6: telemetry budget: volume, cardinality and sampling policy decided before instrumentation spreads.

### 4. Not covered

- Canonical T2 books not read: Release It! (Nygard), Systems Performance (Gregg), Accelerate and Humble and Farley on non-functional testing, Software Engineering at Google; Knuth's paper read only through secondary summaries.
- No standards body text (ISO/IEC 25010, SPEC benchmarks) and no empirical study on the effect of performance testing or readiness reviews.
- Mobile and on-device performance, ML inference capacity, data-pipeline throughput, on-premise hardware procurement.
- Quantitative guidance on test cost, and any normative source on telemetry cost as a budget (only vendor docs).
- Chaos experiments, backup and disaster recovery are other slots' topics (OPERATE-C28b, VERIFY-C41; gap G6).

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| PERF-S01 | T2 | Launch Coordination Checklist (SRE book appendix) | Google SRE | https://sre.google/sre-book/launch-checklist/ | launch readiness checklist domains |
| PERF-S02 | T2 | Reliable Product Launches at Scale (SRE book) | Google SRE | https://sre.google/sre-book/reliable-product-launches/ | checklist design, rigor vs velocity, gradual rollout |
| PERF-S03 | T2 | Evolving SRE Engagement Model (SRE book, production readiness review) | Google SRE | https://sre.google/sre-book/evolving-sre-engagement-model/ | production readiness review |
| PERF-S04 | T2 | Addressing Cascading Failures (SRE book) | Google SRE | https://sre.google/sre-book/addressing-cascading-failures/ | load testing to failure, limits of capacity planning |
| PERF-S05 | T2 | Handling Overload (SRE book) | Google SRE | https://sre.google/sre-book/handling-overload/ | capacity in resources, load shedding, retry budgets |
| PERF-S06 | T2 | Software Engineering in SRE (SRE book) | Google SRE | https://sre.google/sre-book/software-engineering-in-sre/ | capacity planning and intent-based planning |
| PERF-S07 | T2 | Monitoring Distributed Systems (SRE book) | Google SRE | https://sre.google/sre-book/monitoring-distributed-systems/ | black-box vs white-box, golden signals, percentiles |
| PERF-S08 | T2 | Practical Alerting (SRE book) | Google SRE | https://sre.google/sre-book/practical-alerting/ | prober (synthetic checks), SLO alerting |
| PERF-S09 | T2 | Service Level Objectives (SRE book) | Google SRE | https://sre.google/sre-book/service-level-objectives/ | percentile targets, targets from user need |
| PERF-S10 | T2 | Being On-Call (SRE book) | Google SRE | https://sre.google/sre-book/being-on-call/ | operational load limits, team size |
| PERF-S11 | T2 | Emergency Response (SRE book) | Google SRE | https://sre.google/sre-book/emergency-response/ | preparation, rehearsal, testing response |
| PERF-S12 | T2 | Effective Troubleshooting (SRE book) | Google SRE | https://sre.google/sre-book/effective-troubleshooting/ | playbook linked from alert, investigation logs |
| PERF-S13 | T2 | Introducing Non-Abstract Large System Design (SRE Workbook ch. 12) | Google SRE | https://sre.google/workbook/non-abstract-design/ | resource planning from requirements and failure domains |
| PERF-S14 | T2 | Canarying Releases (SRE Workbook) | Google SRE | https://sre.google/workbook/canarying-releases/ | canary metrics, limits of synthetic load |
| PERF-S15 | T2 | Using load shedding to avoid overload (Amazon Builders' Library) | Amazon | https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload (redirect from the aws.amazon.com/builders-library URL) | overload tests, goodput |
| PERF-S16 | T2 | Continuous Integration | M. Fowler | https://martinfowler.com/articles/continuousIntegration.html | read for performance tests in pipeline: only dark launching mentioned; negative finding |
| PERF-S17 | T1 | Architecture strategies for performance testing (PE:06), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/performance-test | performance test practice, budgets, types, production testing |
| PERF-S18 | T1 | Architecture strategies for capacity planning (PE:02), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning | capacity planning method |
| PERF-S19 | T1 | Designing a reliability testing strategy (RE:08), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/reliability/reliability-test | load and scaling response, runbook validation, DR tests |
| PERF-S20 | T1 | REL07-BP04 Load test your workload, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_load_tested_adapt.html | load test anti-patterns |
| PERF-S21 | T1 | PERF05-BP04 Load test your workload, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html | load test steps, pipeline integration |
| PERF-S22 | T1 | OPS07-BP02 Ensure a consistent review of operational readiness, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_const_orr.html | operational readiness review |
| PERF-S23 | T1 | Operational Readiness Reviews (ORR) whitepaper, introduction only | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html | origin and purpose of ORR |
| PERF-S24 | T1 | OPS07-BP03 Use runbooks to perform procedures, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html | runbooks |
| PERF-S25 | T1 | OPS07-BP04 Use playbooks to investigate issues, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_playbooks.html | playbooks |
| PERF-S26 | T1 | Sampling, OpenTelemetry documentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/sampling/ | sampling as cost control, head vs tail |
| PERF-S27 | T1 | Instrumentation practices, Prometheus documentation | Prometheus | https://prometheus.io/docs/practices/instrumentation/ | label cardinality, instrumentation overhead |
| PERF-S28 | T1 | CloudWatch Synthetics canaries, AWS documentation | AWS | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html | what synthetic monitors do (one tool) |
| PERF-S29 | T1 | Application Observability cost optimization, Grafana Cloud documentation | Grafana Labs | https://grafana.com/docs/grafana-cloud/monitor-applications/application-observability/optimize-costs/ | telemetry cost drivers and trade-offs (one tool) |
| PERF-S30 | T1 | Load test types, Grafana k6 documentation | Grafana Labs | https://grafana.com/docs/k6/latest/testing-guides/test-types/ | smoke, load, stress, spike, soak, breakpoint |
| PERF-S31 | T3 | Coordinated Omission (mechanical-sympathy group post) | G. Tene | https://groups.google.com/g/mechanical-sympathy/c/icNZJejUHfE/m/BfDekfBEs_sJ | coordinated omission in load measurement |
| PERF-S32 | T3 | Performance budgets 101 | web.dev (Google) | https://web.dev/articles/performance-budgets-101 | client-side performance budgets in CI |
| PERF-S33 | T3 | Revisiting Knuth's "Premature Optimization" Paper (secondary; the 1974 paper itself not read) | probablydance.com, via search summary | https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/ (search result only, page not fetched) | context of the premature-optimization quote |
| PERF-S34 | T3 | Benchmarks in CI without noise (vendor blog), search summary only, page not fetched | CodSpeed | https://codspeed.io/blog/benchmarks-in-ci-without-noise | variance of benchmarks on shared CI runners |
| PERF-S35 | T4 | Synthetic vs real user monitoring (vendor pages), search summary only | SpeedCurve and others | https://www.speedcurve.com/web-performance-guide/synthetic-vs-real-user-monitoring/ (search result only) | live debate and definitions of real-user monitoring |

Note on authority: S17 to S30 are vendor platform and tool documentation, T1 by the brief's "official documentation" rule, but cloud-flavoured and single-vendor; where two vendors agree, agreement is recorded as consensus, otherwise single-source claims are `majority` with that stated.

### Claims

#### Targets and measurement

- id: PERF-C01
  claim: Define performance targets from user needs and the SLO, translate them into measurable test objectives with explicit pass/fail thresholds (for example p95 under a stated latency), and do not set targets from current performance.
  level: principle; stack: neutral; sources: S17 (Set measurable goals), S09 (Don't pick a target based on current performance); agreement: consensus; certainty: grounded.

- id: PERF-C02
  claim: State latency targets and test results as percentiles or distributions, never as averages, because tail requests compound across dependencies.
  level: principle; stack: neutral; sources: S09, S07 (latency distributions), S17 (threshold at 95th percentile); agreement: consensus; certainty: grounded.

- id: PERF-C03
  claim: Split performance and error budgets across layers (for example API, database) so that a failing test identifies the layer to optimize.
  level: practice; stack: neutral; sources: S17 (assign budgets); agreement: majority (single T1 source); certainty: grounded.

#### Load testing

- id: PERF-C04
  claim: Choose test-environment fidelity by criticality: match production on compute, scaling, caching, network and dependencies for mission-critical workloads; accept a scaled-down production-like environment for non-critical ones; record the choice.
  level: decision; stack: neutral; sources: S17 (Mirror your production environment), S20 (anti-pattern: configuration differs from production), S21 (production-like environment), S04 (real traffic tests more realistic but cost user pain); agreement: contested; certainty: grounded.
  positions: (a) production-identical environment: confidence and fidelity, held by S20, S17 for critical workloads; wins for high criticality and when results gate capacity spend. (b) scaled-down environment: cost of ownership, held by S17 for non-critical workloads; wins when load behaviour scales predictably and criticality is low. (c) test in production: highest realism, impact on users, held by S04, S17; wins when only production has the data and dependencies, with guardrails (see PERF-C14). Cloud elasticity lowers the cost of (a) per S20.

- id: PERF-C05
  claim: Load test the whole workload end to end, not isolated components.
  level: principle; stack: neutral; sources: S20 (anti-pattern), S21 (anti-pattern), S19 (test full flows); agreement: consensus; certainty: grounded.

- id: PERF-C06
  claim: Use a representative request mix and realistic data (synthetic or sanitized production data), including edge cases such as large payloads and high concurrency.
  level: practice; stack: neutral; sources: S17 (Use real-world usage patterns), S20 (anti-pattern: subset of requests), S21 (synthetic or sanitized data), S14 (synthetic load gives code coverage but poor state coverage); agreement: contested on third-party calls; certainty: grounded.
  positions: (a) include real third-party calls: realism of end-to-end latency, S17; wins when the dependency is critical and the provider permits tests. (b) mock external dependencies: repeatability and speed, noted by S17 as the faster option that hides problems; provider testing policies can forbid load (S21 cites a cloud testing policy); wins when the provider limits tests or when isolating own code.

- id: PERF-C07
  claim: Test past expected load to the breaking point and far beyond it, not to a small safety factor, so failure modes and the metrics that signal approach to them are known.
  level: principle; stack: neutral; sources: S04 (Load test components until they break), S15 (load tested far beyond the point where it breaks), S20 (anti-pattern: small safety factor), S21 (anti-pattern: only expected load), S30 (stress and breakpoint); agreement: consensus; certainty: grounded.

- id: PERF-C08
  claim: Use several test types matched to risk (smoke, average load, stress, spike, soak, breakpoint); begin with basic load tests and widen as risks and experience grow.
  level: decision; stack: neutral; sources: S17 (Apply multiple performance test types), S30 (six types and when to run each, "no single test type eliminates all risk"); agreement: consensus; certainty: grounded.

- id: PERF-C09
  claim: Decide when performance tests run: as a smoke check when code changes, load tests in the delivery pipeline against thresholds, soak and spike before anticipated events or after large changes, breakpoint tests occasionally.
  level: decision; stack: neutral; sources: S17 (Start early and test continuously; pipelines plus periodic automated tests), S21 (automatically in delivery pipeline; regular cadence after changes), S30 (when to run), S34 (shared CI runners are noisy; search summary only); agreement: contested; certainty: grounded for positions, inferred for the noise argument (T3 summary only).
  positions: (a) every change gated in the pipeline: speed of feedback, regression traced to one change, S17, S21; wins when the system has a stable, low-variance harness and fast tests. (b) scheduled or event-driven runs: cost, low noise, S30 for stress, soak, spike, breakpoint; wins when tests are long, expensive or noisy. Tradeoff stated by S17: early testing needs dedicated infrastructure and expertise. boundary: VERIFY (performance regression tests, VERIFY-C29) and DELIVER (pipeline stages).

- id: PERF-C10
  claim: Record a baseline of normal performance, compare each run against it to detect regression and slow drift, and refresh baselines after architectural or scaling changes.
  level: practice; stack: neutral; sources: S17 (Use test results to guide design; definitions of regression and drift), S21 (compare against predefined KPIs and thresholds); agreement: consensus; certainty: grounded. boundary: VERIFY.

- id: PERF-C11
  claim: Validate performance changes as hypotheses: state the prediction, run the same load test on baseline and variant, and compare measured results, reserving this for high-impact changes.
  level: practice; stack: neutral; sources: S17 (Validate changes with hypothesis-driven experiments, tradeoff note); agreement: majority (single T1 source); certainty: grounded.

- id: PERF-C12
  claim: Generate load open-loop (constant arrival rate) or correct for coordinated omission, because a load generator that waits for each response before sending the next under-reports tail latency during stalls.
  level: practice; stack: neutral (a measurement property of any closed-loop generator); sources: S31 (definition, HdrHistogram correction, open-loop testers); agreement: majority (single T3 source, widely cited); certainty: grounded in S31, T3 only, so inferred as a normative rule.

- id: PERF-C13
  claim: Measure client-perceived outcomes (goodput: successful responses with usable latency) rather than only server-side throughput when testing overload.
  level: practice; stack: neutral; sources: S15 (Goodput vs throughput); agreement: majority (single T2 source); certainty: grounded.

- id: PERF-C14
  claim: Supplement pre-production tests with controlled production tests (off-peak, ramped from a small traffic share, extra capacity reserved, rollback ready) for what only production reveals; treat real-traffic tests as higher fidelity and higher user risk.
  level: decision; stack: neutral; sources: S17 (Validate performance in production; risk note), S04 (real traffic tests may be more realistic at risk of user-visible pain), S20 (load testing in production as part of game days); agreement: contested; certainty: grounded.
  positions: (a) pre-production only: user safety, reversibility; wins for high-impact or regulated systems with faithful replicas. (b) controlled production tests: realism of data, network, third parties; wins when a faithful replica is unaffordable. S14 adds that synthetic load alone misses state coverage, which supports canarying on organic traffic as a complement. boundary: DELIVER (rollout), OPERATE.

- id: PERF-C15
  claim: Synthetic load maximizes code coverage but not state coverage, especially in systems with caches, cookies or request affinity; complement it with canary analysis on organic traffic.
  level: principle; stack: neutral; sources: S14 (Canary metrics and synthetic traffic); agreement: majority (single T2 source); certainty: grounded. boundary: DELIVER.

- id: PERF-C16
  claim: Base optimization on measurement and keep it iterative and data-driven, while estimating resources and testing early enough that architectural bottlenecks are found before they are costly.
  level: decision; stack: neutral; sources: S17 (Start early; Optimization is iterative and data-driven), S13 (resource planning at design time), S33 (Knuth context: forget small efficiencies about 97% of the time, but do not pass up the critical 3%; secondary summary only); agreement: contested; certainty: grounded for S17 and S13, inferred for the Knuth reading (secondary source).
  positions: (a) measure first, optimize the critical few: cost of ownership, delivery speed; held via S33. (b) estimate and test from design onward: avoided rework, held by S17 and S13 (early analysis catches architectural bottlenecks); wins where architecture is hard to change and load is high. Both agree on measurement before tuning.

- id: PERF-C17
  claim: For client-delivered software, enforce performance budgets on artefact size and timing metrics in the build pipeline and, when exceeded, optimize, remove or block the addition.
  level: practice; stack: web front end (budget metrics such as Time to Interactive); sources: S32 (Setting budgets; Enforcing in CI/CD); agreement: majority (single T3 source); certainty: grounded. Pointer for the JavaScript and web guidelines.

#### Capacity

- id: PERF-C18
  claim: Do capacity planning before predicted changes in usage (design, launch, marketing push, seasonal peaks, feature release, business change) and periodically, using historical data for existing workloads and pilots, expert judgment and external data for new ones.
  level: principle; stack: neutral; sources: S18 (PE:02, Gather capacity data, Forecast demand), S06 (demand forecasting, organic vs inorganic growth), S01 (traffic estimates six months out); agreement: consensus; certainty: grounded.

- id: PERF-C19
  claim: Model capacity directly in resources (CPU cores, memory, bandwidth, storage) rather than in requests per second, because query costs differ widely.
  level: decision; stack: neutral; sources: S05 (capacity measured in available resources), S18 (measure capacity at the resource level); agreement: consensus; certainty: grounded.

- id: PERF-C20
  claim: Derive the resource proposal from requirements (SLOs, traffic rates, record sizes) and iterate designs through scaling and failure domains, discarding a design when a reliability requirement defeats it.
  level: practice; stack: neutral; sources: S13 (Derive resources from requirements; iterate through failure analysis); agreement: majority (single T2 source); certainty: grounded.

- id: PERF-C21
  claim: Pair capacity planning with load testing and overload behaviour, because planning lowers the probability of cascading failure but does not protect against infrastructure loss, partitions or unexpected spikes.
  level: principle; stack: neutral; sources: S04 (Capacity planning has limits), S15 (load shedding, goodput); agreement: consensus; certainty: grounded.

- id: PERF-C22
  claim: Decide capacity headroom explicitly: over-provisioning costs money, under-provisioning costs performance; account for scaling lag between trigger and new capacity, and for capacity in the failover environment.
  level: decision; stack: neutral; sources: S18 (Tradeoff note; autoscaling), S19 (Account for scaling lag; Validate capacity in the failover environment); agreement: contested; certainty: grounded.
  positions: (a) pre-provision for peak and failover: reliability, reversibility, wins for hard peaks, long scale-up times and critical systems. (b) autoscale with tested limits: cost, wins for variable load with fast scale-up. Neither source fixes a numeric headroom; open.

- id: PERF-C23
  claim: Replace spreadsheet-based capacity plans with declared requirements from which allocations are computed when the number of services makes manual plans brittle.
  level: decision; stack: neutral (context: large fleets); sources: S06 (Intent-Based Capacity Planning: specify requirements, not implementation; spreadsheets limited); agreement: majority (single T2 source, one organization's scale); certainty: grounded; context under which it wins: many services and frequent change; for a small team a spreadsheet or dashboard forecast (S18) suffices (inferred).

- id: PERF-C24
  claim: Design and test overload behaviour: reject early when out of quota or capacity, serve degraded responses before errors, cap client retries (per-request and per-client budgets) and throttle on the client.
  level: practice; stack: neutral (application design; pointer, out of scope as architecture); sources: S05, S15, S19 (graceful degradation tests); agreement: consensus; certainty: grounded. Verification of this behaviour belongs here, design to application architecture.

#### Operational readiness

- id: PERF-C25
  claim: Verify operational readiness before launch against a checklist covering architecture, capacity, failure modes, monitoring, emergency response, change management and rollout, and do not launch a workload whose team cannot operate it.
  level: principle; stack: neutral; sources: S01 (nine categories), S03 (PRR analysis phase), S22 (ORR; anti-pattern: launch without knowing if you can operate it), S02; agreement: consensus; certainty: grounded.

- id: PERF-C26
  claim: Decide who performs the readiness review: an independent reviewing team that examines the service and negotiates improvements, or a self-service checklist the owning team certifies against.
  level: decision; stack: neutral; sources: S03 (one to three SREs conduct the PRR; negotiated improvements), S22 and S23 (self-service experience, certification by the team, built to avoid slowing builders), S02 (consulting unit as objective mediator); agreement: contested; certainty: grounded.
  positions: (a) independent reviewer: control, quality, knowledge transfer, S03, S02; wins for critical services, few reviewers' capacity matched to service count, or when ownership is handed to a separate operations team. (b) self-service review: delivery speed and scalability across decentralized teams, S22, S23; wins with many teams, mature culture, executive sponsor. Evidence of relative effectiveness: none read; open.

- id: PERF-C27
  claim: Build the checklist from your own incidents and past launch failures, make each item concrete and achievable, start short (about thirty items), and tier it by risk with fast paths for low-risk launches.
  level: practice; stack: neutral; sources: S02 (concrete, curated from previous launch disasters, risk-stratified), S22 (limit first iteration to thirty or fewer; post-incident analysis drives the ORR), S23 (curated questions from incidents); agreement: consensus; certainty: grounded.

- id: PERF-C28
  claim: Re-run the readiness review periodically over the workload lifecycle, with a subset on a regular cadence, to catch drift and incorporate new lessons.
  level: practice; stack: neutral; sources: S22 (run before GA and throughout; example yearly subset); agreement: majority (single T1 source); certainty: grounded.

- id: PERF-C29
  claim: Convert repeated readiness findings into automated guardrails and defaults over time.
  level: practice; stack: neutral (examples are AWS services); sources: S22 (build ORR requirements into defaults and guardrails), S02 (converge on standard infrastructure); agreement: majority; certainty: grounded.

- id: PERF-C30
  claim: Keep runbooks as versioned step-by-step documents with an owner, required tools and permissions, error handling and escalation, validated by having another team member run them, and updated through change management.
  level: practice; stack: neutral; sources: S24 (Implementation guidance; anti-pattern: runbooks drift out of sync with the system); agreement: majority (single T1 source, consistent with S11 on documenting what broke); certainty: grounded.

- id: PERF-C31
  claim: Mature runbooks and playbooks from text toward scripts and auto-remediation, starting with short, frequently used, low-risk ones.
  level: decision; stack: neutral; sources: S24, S25; agreement: majority (single vendor); certainty: grounded. Cost and risk of automating a wrong runbook: open.

- id: PERF-C32
  claim: Separate playbooks (investigate and scope an incident) from runbooks (mitigate a known cause), link the playbook from the alert, and give each an escalation path when the cause is unknown.
  level: practice; stack: neutral; sources: S25, S12 (alert links to playbook entry); agreement: consensus; certainty: grounded. boundary: OPERATE (OPERATE-C35 holds the playbook outcome claim).

- id: PERF-C33
  claim: Exercise recovery procedures under realistic conditions (manual runbooks, failover and failback, tabletop exercises) and turn gaps found into tests; a team does not know how a system reacts until it has failed.
  level: practice; stack: neutral; sources: S19 (Validate manual recovery runbooks; tabletop exercises; DR), S11 (preparation and periodic hands-on training); agreement: consensus; certainty: grounded. boundary: OPERATE.

- id: PERF-C34
  claim: Size the on-call team so that on-call stays under about 25 percent of engineers' time and incident handling stays sustainable (a single-site 24/7 rotation needs at least eight engineers in the source's model).
  level: practice; stack: neutral; sources: S10 (operational load limits; minimum team sizing); agreement: majority (single T2 source, Google's staffing model); certainty: grounded. Context: large organizations with a dedicated rotation; small teams must trade this against coverage (inferred). boundary: OPERATE.

#### Synthetic monitoring

- id: PERF-C35
  claim: Combine internal (white-box) monitoring with external synthetic (black-box) checks, because internal metrics alone miss what users see (for example DNS failures and crashed servers that emit no signal).
  level: principle; stack: neutral; sources: S08 (White-box limitations; Prober), S07 (black-box tests externally visible behavior; modest but critical use); agreement: consensus; certainty: grounded. boundary: OPERATE.

- id: PERF-C36
  claim: Use synthetic monitoring to detect failures before users do and even with no traffic, and real-user monitoring to measure experienced performance; use both together.
  level: decision; stack: neutral; sources: S28 (canaries verify the customer experience without customer traffic), S35 (T4 vendor summaries on real-user monitoring and on combining both); agreement: majority; certainty: grounded for synthetic, inferred for real-user monitoring (T4 only).

- id: PERF-C37
  claim: Run synthetic checks along real customer routes on a fixed schedule from several vantage points, validate payloads and capture latency as time series, and secure the credentials and artifacts they use.
  level: practice; stack: neutral (tool example: managed canaries, runs as often as once per minute); sources: S28 (scripts, schedules, security considerations link), S08 (check payload; multiple vantage points, suppress alerts for localized failures); agreement: majority; certainty: grounded.

- id: PERF-C38
  claim: Monitor the monitoring: verify that the observability pipeline itself works.
  level: practice; stack: neutral; sources: S01 (Monitoring the monitoring); agreement: majority (single T2 source, one line); certainty: grounded.

#### Telemetry cost

- id: PERF-C39
  claim: Treat telemetry volume and cardinality as a cost to design, because cost scales with the number of active series (roughly the product of distinct label values) and with trace, log and profile volume.
  level: principle; stack: neutral; sources: S29 (Cost drivers), S27 (label cardinality and resource cost), S26 (sampling reduces cost); agreement: consensus; certainty: grounded.

- id: PERF-C40
  claim: Keep metric label cardinality bounded: avoid unbounded values such as user ids, keep most metrics at low cardinality, limit high-cardinality ones to a handful across the system, and move per-entity detail to logs or traces.
  level: practice; stack: Prometheus-style metrics systems (numbers are that tool's); sources: S27 (Do not overuse labels: "below 10", investigate beyond 100), S29 (generalize span names, remove unused dimensions); agreement: consensus between two tools; certainty: grounded. Pointer for tool stacks.

- id: PERF-C41
  claim: Decide the trace sampling policy: head sampling is simple and cheap but cannot select on the whole trace; tail sampling can always keep errors and slow traces but needs stateful infrastructure; do not sample low-volume systems, aggregate-only analysis or where regulation forbids data loss.
  level: decision; stack: neutral (OpenTelemetry semantics); sources: S26 (head vs tail; When to sample / When not to sample, consider sampling above about 1000 traces per second), S29 (enable trace sampling, loses complete visibility); agreement: contested; certainty: grounded. boundary: OPERATE (OPERATE-C27 holds the sampling claim; here the cost framing).
  positions: (a) head sampling: cost, simplicity. (b) tail sampling: completeness of interesting traces, at operational complexity. (c) no sampling: exploratory power, compliance, wins at low volume.

- id: PERF-C42
  claim: Filter low-value telemetry (health checks, static assets), coarsen histogram buckets and drop unused dimensions, accepting a stated loss of granularity, and never mix incompatible histogram formats within a service.
  level: practice; stack: Grafana and Prometheus-style tooling; sources: S29 (table of optimizations and trade-offs); agreement: majority (single vendor); certainty: grounded.

- id: PERF-C43
  claim: Instrument broadly (every library, subsystem and service gets basic metrics) because per-metric overhead is negligible except on code executed above about 100,000 times per second, where it should be benchmarked.
  level: practice; stack: Prometheus client libraries (numbers are that tool's); sources: S27 (instrument everything; Instrumentation costs); agreement: majority (single tool documentation); certainty: grounded. Tension with PERF-C39: breadth of instrumentation vs cardinality of labels; resolved in S27 by bounding labels, not metrics.

- id: PERF-C44
  claim: Set an explicit telemetry budget (volume, series count, retention) per service and review it, as the cost counterpart of an SLO.
  level: decision; stack: neutral; sources: none read at T1 or T2 (S29 and S26 describe cost levers only); agreement: n/a; certainty: open. Recorded as a gap: no normative source found on telemetry cost as a governed budget.

### Gaps

- Canonical T2 books not read, so claims on non-functional test strategy and stability patterns have no Nygard, Humble and Farley or Gregg grounding; Fowler's CI article, read in full for the topic, has no performance-test claim (only dark launching).
- The 1974 Knuth paper was not read; PERF-C16 rests on a secondary summary for that half.
- Headroom size: no numeric guidance found at T1 or T2 (PERF-C22).
- Relative effectiveness of independent vs self-service readiness reviews (PERF-C26): no empirical evidence read.
- Noise of performance tests on shared CI runners (PERF-C09) rests on a vendor-blog search summary (S34); no T1 or T2 source read.
- Real-user monitoring is documented only through T4 vendor summaries (S35).
- The AWS ORR whitepaper checklist and Appendix B example questions were not read (only the introduction was returned).
- Capacity planning for on-premise hardware, mobile, ML inference and data pipelines is not covered.
- Cloud-vendor sources (S17 to S21, S28) dominate T1 for this area; a vendor-neutral standard was not found.
