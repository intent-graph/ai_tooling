# Branch OPERATION: tree and node records

Realization branch (`../../../target_hierarchy.md`): how the running system is kept within its reliability targets and recovered when it fails. Refined below the nine L2 nodes of `../../tree_l2.md`; every row routed to OPERATION in `../../routing.md` is attached to exactly one node. No verdict, no ranking: positions are listed for the judges. Rules cited: MD-01 (best, not average, decided later by judges), MD-02 (context variables only where a row says so), MD-03 (one location per fact).

Pinned: nodes 39 (L1 1, L2 9, L3 29); rows attached 109 of 109; unattached 0; routing objections 4 (6 were raised, 2 resolved by moving the row, see `../../objections/resolution.md`).

## Tree

```text
OPERATION  Operation  (-)
    OPERATION.RELIABILITY  Reliability Targets  (-)
        OPERATION.RELIABILITY.1  Indicators  (L175, L176, L177, L178, L1173, L1174)
        OPERATION.RELIABILITY.2  Objective Level and Starting Point  (L174, L179)
        OPERATION.RELIABILITY.3  Error Budget as Trade Mechanism  (L180, L181, L183)
        OPERATION.RELIABILITY.4  Budget Exhaustion Consequence  (L182)
    OPERATION.ALERTING  Alerting  (-)
        OPERATION.ALERTING.1  Paging Criterion and Rule Hygiene  (L184, L1175, L186, L188)
        OPERATION.ALERTING.2  Alert Basis  (L185, L187)
    OPERATION.TELEMETRY  Telemetry  (-)
        OPERATION.TELEMETRY.1  What Is Measured and From Where  (L190, L191, L192, L1172, L1180, L1177, L189, L1176, L453, L454, L313)
        OPERATION.TELEMETRY.2  Observability Model and Pipeline Health  (L193, L194, L195, L1163, L1181, L455)
        OPERATION.TELEMETRY.3  Instrumentation and Log Emission  (L196, L197, L198, L1168, L201, L1166)
        OPERATION.TELEMETRY.4  Correlation and Context Propagation  (L199, L1164, L1165, L1167, L1253)
        OPERATION.TELEMETRY.5  Trace Sampling  (L200, L1169, L1170)
        OPERATION.TELEMETRY.6  Telemetry Cost  (L456, L457, L458, L459, L460)
    OPERATION.INCIDENTS  Incidents  (-)
        OPERATION.INCIDENTS.1  Declaring and Running an Incident  (L202, L203, L204)
        OPERATION.INCIDENTS.2  Learning From Incidents  (L205, L206, L209, L1148)
        OPERATION.INCIDENTS.3  On-Call and Toil Load  (L207, L452)
    OPERATION.CAPACITY  Capacity  (-)
        OPERATION.CAPACITY.1  Planning Method  (L436, L437, L438, L441)
        OPERATION.CAPACITY.2  Headroom and Overload  (L439, L440)
        OPERATION.CAPACITY.3  Storage Health  (L317)
    OPERATION.READINESS  Operational Readiness  (-)
        OPERATION.READINESS.1  Launch Gate and Checklist  (L443, L445)
        OPERATION.READINESS.2  Who Performs the Review  (L444)
        OPERATION.READINESS.3  Keeping the Review Current  (L446, L447)
    OPERATION.RUNBOOKS  Runbooks and Playbooks  (-)
        OPERATION.RUNBOOKS.1  Form, Ownership and Validation  (L448, L450)
        OPERATION.RUNBOOKS.2  Automation  (L449)
    OPERATION.RECOVERY  Backup, Restore and Disaster Recovery  (-)
        OPERATION.RECOVERY.1  Recovery Objectives  (L1080, L1081, L1082, L1083, L1084)
        OPERATION.RECOVERY.2  Backup Scope and Design  (L1079, L1085, L1086, L1091, L1093, L1094, L1118)
        OPERATION.RECOVERY.3  Backup Protection and Isolation  (L1087, L1088, L1089, L1090, L1117)
        OPERATION.RECOVERY.4  Recovery Strategy, Failover and Failback  (L1101, L1105, L1106, L1107, L1110)
        OPERATION.RECOVERY.5  Recoverability of Recovery Itself  (L1108, L1109, L1115, L1116)
        OPERATION.RECOVERY.6  Ownership, Monitoring, Roles and Plan Upkeep  (L1095, L1096, L1111, L1113)
    OPERATION.FEEDBACK  Feedback into Development  (L208)
```

Split topic held here (MD-03): `OPERATION.RECOVERY` is the content holder for backup, objectives, strategy, failover; `ASSURANCE.AVAILABILITY` holds the proof and is the index. No index node in this branch.

## Node records

### OPERATION Operation

- uid: `OPERATION`
- intent: Realization: how the running system is kept within its reliability targets and recovered when it fails.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.RELIABILITY Reliability Targets

- uid: `OPERATION.RELIABILITY`
- intent: How reliability is defined and traded against release speed: indicators, objectives, error budget.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.RELIABILITY.1 Indicators

- uid: `OPERATION.RELIABILITY.1`
- intent: What is measured to define reliability, so that the definition matches what users experience.
- rows: L175, L176, L177, L178, L1173, L1174 (6)
- positions (no verdict):
  - P1 User-view SLIs anchored on critical user journeys, few and simple, added only for coverage gaps. Argument: infrastructure metrics do not show user experience. Force: fit to user need, cognitive load. Best when: no condition recorded (consensus). Rows L175, L176, L178, L1174; sources REG-117, REG-125, REG-134.
  - P2 State latency as percentiles or distributions, never as averages alone. Argument: the tail dominates user experience and compounds across dependencies. Force: realism of the signal. Best when: no condition recorded (consensus). Rows L177, L1173; sources REG-124, REG-125, REG-226.
- context variables: none (no row says the best practice moves with a variable)
- links: Refines OPERATION.RELIABILITY.2 (L1174 also states that objectives are not set merely from current performance, see also L179)

### OPERATION.RELIABILITY.2 Objective Level and Starting Point

- uid: `OPERATION.RELIABILITY.2`
- intent: How the reliability objective is chosen, and from what it starts.
- rows: L174, L179 (2)
- positions (no verdict):
  - P1 Treat 100 percent as the wrong target; choose a level below it from user need and weigh its cost. Argument: cost rises steeply and users cannot tell. Force: cost of ownership, fit. Best when: no condition recorded (consensus). Row L174; sources REG-128, REG-134.
  - P2 Set the objective from user need, not history. Argument: avoids heroics and a target that merely copies today's performance. Force: reliability fit. Best when: users or contracts have known needs. Row L179 (a); source REG-125.
  - P3 Start from what is measurable and cheap (existing logs), then iterate. Argument: gives a feedback loop where no objective exists yet. Force: delivery speed, feedback. Best when: no objectives exist yet. Row L179 (b); source REG-134. Ledger note: both sources are Google and are reconciled by 'start, then review', so the disagreement is the starting point.
- context variables: none (no row says the best practice moves with a variable)
- links: Requires OPERATION.RELIABILITY.1 (an objective is set on an indicator)

### OPERATION.RELIABILITY.3 Error Budget as Trade Mechanism

- uid: `OPERATION.RELIABILITY.3`
- intent: Whether and how the gap between 100 percent and the objective is used as the shared rule that trades release speed against reliability.
- rows: L180, L181, L183 (3)
- positions (no verdict):
  - P1 Use an error budget as the shared, objective trade between velocity and reliability. Argument: depoliticises the argument between product and operations. Force: velocity and reliability jointly. Best when: product and operations are separate parties. Row L180; sources REG-113, REG-128.
  - P2 No error budget, reliability by judgment (minority view). Not found in any read source; open. Row L180.
  - P3 Write the budget policy down and have product and operations agree to it; without it the objective is only a report. Force: binding effect. Rows L181; sources REG-133, REG-134.
  - P4 Set postmortem triggers from budget consumption (example: one incident over 20 percent of the budget in four weeks). Argument: ties learning to the budget. Numbers illustrative, one example policy. Row L183; source REG-133.
- context variables: none (no row says the best practice moves with a variable)
- links: Requires OPERATION.RELIABILITY.2; Refines OPERATION.INCIDENTS.2 (postmortem triggers, L205 holds the written triggers)

### OPERATION.RELIABILITY.4 Budget Exhaustion Consequence

- uid: `OPERATION.RELIABILITY.4`
- intent: What the exhaustion of the error budget does to releases, decided before it happens.
- rows: L182 (1)
- positions (no verdict):
  - P1 Hard freeze of changes except top-priority and security fixes, disputes escalated to a named executive. Force: control, reliability. Best when: many consumers, strict SLAs or a weak safety culture. Row L182 (a); sources REG-128, REG-133.
  - P2 Self-regulation: the team slows and adds testing voluntarily. Force: delivery speed, autonomy. Best when: small, high-trust teams. Row L182 (b); sources REG-128, REG-133.
- context variables: Number of consumers and strictness of SLAs, and safety culture (L182: 'wins with many consumers, strict SLAs, or a weak safety culture' against 'small, high-trust teams').
- links: Requires OPERATION.RELIABILITY.3

### OPERATION.ALERTING Alerting

- uid: `OPERATION.ALERTING`
- intent: When a human is paged and how alerts are built.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.ALERTING.1 Paging Criterion and Rule Hygiene

- uid: `OPERATION.ALERTING.1`
- intent: Which conditions justify waking a person, and how the rule set is kept to those.
- rows: L184, L1175, L186, L188 (4)
- positions (no verdict):
  - P1 Page only for a condition that is urgent, actionable and user-visible (actively or imminently); everything else is a ticket or a log. Argument: every page costs attention. Force: cognitive load. Best when: no condition recorded (consensus). Rows L184, L1175; sources REG-113, REG-124.
  - P2 Every page must require human judgment; a page answerable by a robotic response is automated or removed. Row L186; source REG-124.
  - P3 Remove rules and signals that are rarely exercised or never exposed; keep rules that catch real incidents simple and predictable. Row L188; source REG-124.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OPERATION.RUNBOOKS.2 (L186: an automatable page is automated)

### OPERATION.ALERTING.2 Alert Basis

- uid: `OPERATION.ALERTING.2`
- intent: What an alert is built on: user-visible symptom, internal cause, or the rate of error-budget consumption.
- rows: L185, L187 (2)
- positions (no verdict):
  - P1 Alert on user-visible symptoms only; keep cause-level signals for diagnosis. Argument: low noise. Force: cognitive load. Best when: on-call capacity is limited. Row L185; sources REG-124, REG-131.
  - P2 Symptoms plus white-box cause alerts for imminent or retry-masked failures. Argument: early warning (REG-124: heavy white-box with modest but critical black-box). Force: early warning. Best when: imminent failures matter more than the added noise. Row L185. The ledger records the tension as early warning against noise.
  - P3 Simple threshold alerts. Argument: fewest parameters, easiest to maintain. Force: cost of maintenance. Best when: small services. Row L187; source REG-132.
  - P4 Multiwindow multi-burn-rate alerts on the budget consumption rate, page for fast burn, ticket for slow burn. Argument: best precision, recall and reset time (one authority). Force: precision. Best when: an objective exists and false pages cost a lot. Row L187; source REG-132.
- context variables: On-call capacity (L185: symptom-only 'wins with limited on-call capacity').; Service size and existence of an objective (L187: threshold alerts 'win for small services', burn rate 'when an SLO exists and false pages cost a lot').
- links: Requires OPERATION.RELIABILITY.3 (P4 alerts on the error budget burn rate)

### OPERATION.TELEMETRY Telemetry

- uid: `OPERATION.TELEMETRY`
- intent: What is measured, logged and traced, how it is correlated, and what it costs.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.TELEMETRY.1 What Is Measured and From Where

- uid: `OPERATION.TELEMETRY.1`
- intent: Which signals every service exposes and from which vantage point they are observed (inside, outside, real users).
- rows: L190, L191, L192, L1172, L1180, L1177, L189, L1176, L453, L454, L313 (11)
- positions (no verdict):
  - P1 Measure latency, traffic, errors and saturation for user-facing services. Rows L190, L1172; sources REG-124, REG-138.
  - P2 Standardise a minimal per-service metric set (rate, errors, duration) so anyone can be on call for code they did not write; utilisation, saturation, errors per resource for infrastructure. Argument: on-call familiarity. T3 sources; the golden signals of P1 are the T2 counterpart. Row L191; sources REG-124, REG-138, REG-139.
  - P3 Treat the resource-oriented check (utilisation, saturation, errors) as a quick first check, one tool among others, not a full diagnostic method; when investigating a bottleneck enumerate resources first and check each. Rows L192, L1180; source REG-138.
  - P4 Enable per-statement database statistics so slow queries are found by measurement. Row L1177; source REG-1108.
  - P5 Combine internal white-box monitoring with external black-box probing. Argument: internal views cannot see what never reached the service (DNS failures, crashed servers that emit no signal). Rows L189, L1176; sources REG-124, REG-131.
  - P6 Use synthetic monitoring (detects failures before users, even with no traffic) and real-user monitoring (experienced performance) together; run synthetic checks along real customer routes on a schedule from several vantage points, validate payloads, keep latency as time series, secure their credentials. Real-user part inferred (T4 only). Rows L453, L454; sources REG-131, REG-236, REG-243.
  - P7 (MAINT) Monitor scheduled and derived-data work on four signals: duration against a documented expectation, failure (any), backlog (queue size and age of oldest entry), and missed runs (not run within twice the interval); jobs are short, idempotent, scheduled off-peak without overlapping, named descriptively, and wrap errors so that they log and re-raise, so the scheduler records the failure. Maintainer's codified practice, single source, not citable (REG-181); public practice read as majority (golden signals differ in kind). Row L313, moved here from ASSURANCE.DATA_INTEGRITY.
- context variables: none (no row says the best practice moves with a variable)
- links: Related ASSURANCE.DATA_INTEGRITY (L313: the integrity guarantee of derived data is carried by L281, L282 and L314 there)
- stack pointers: L1177: origin stack PostgreSQL, restated neutral by the ledger; L454: managed canaries as the tool example.

### OPERATION.TELEMETRY.2 Observability Model and Pipeline Health

- uid: `OPERATION.TELEMETRY.2`
- intent: How monitoring and observability relate, how telemetry is stored, who is proficient with it, and how the pipeline itself is checked.
- rows: L193, L194, L195, L1163, L1181, L455 (6)
- positions (no verdict):
  - P1 Monitoring (predefined metrics) and observability (exploring unknown unknowns) are complementary; provide both. Argument: unknown failures need exploration. Rows L193; sources REG-117, REG-136.
  - P2 The old three-pillars model should be replaced. Held by REG-140 (Honeycomb, vendor, T3). Row L193.
  - P3 Store metrics, logs and traces separately (three pillars, with standard signals). Argument: standard, mature tooling, cheap aggregated metrics for alerting. Force: cost of ownership, ecosystem fit. Best when: metric alerting dominates and cardinality is low. Row L194; source REG-118.
  - P4 Store arbitrarily wide structured events as the single source of truth, aggregated at read time. Argument: exploratory power, high-cardinality questions, one store. Force: speed of diagnosis. Best when: complex distributed systems with frequent novel failures. Held by a vendor with an interest (T3). Row L194; source REG-140.
  - P5 Frame it as trade-offs among throughput, cardinality, retention and unsampled data, aiming at positive-return systems; the cost premise of P4 is disputed. Row L194; source REG-141. Evidence is argued, not measured.
  - P6 Treat logs, metrics and traces as complementary signals of one system, designed to be correlated; design observability in across every tier. Rows L1163, L1181 (L1181 inferred); sources REG-044, REG-118, REG-1103, REG-1110.
  - P7 Make every developer proficient with monitoring; observability is shared, not operations-only. Row L195; source REG-136.
  - P8 Monitor the monitoring: verify the observability pipeline works. Single T2 source, one line. Row L455; source REG-217.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.TELEMETRY.3 Instrumentation and Log Emission

- uid: `OPERATION.TELEMETRY.3`
- intent: How code is instrumented and how logs leave the application.
- rows: L196, L197, L198, L1168, L201, L1166 (6)
- positions (no verdict):
  - P1 Adopt a vendor-neutral instrumentation API and standard semantic conventions. Argument: consistent names across code, libraries and platforms. Force: exit risk, interoperability. Best when: no condition recorded; OpenTelemetry is the reference realisation. Row L196; sources REG-120, REG-121.
  - P2 Use the vendor SDK or agent. Argument: less setup, deeper vendor features. Force: time to value. Not argued in a read source; inferred. Row L196.
  - P3 Combine zero-code instrumentation (framework, HTTP and database client coverage) with code-based instrumentation for business logic. Rows L197, L1168; sources REG-121, REG-1104.
  - P4 Libraries depend only on the instrumentation API, not the SDK, so applications that collect no telemetry pay nothing. Boundary with dependency practice. Row L198; source REG-121.
  - P5 The application writes logs unbuffered to standard output as an event stream; the environment collects and routes them. Force: separation of concerns. Best when: process-based applications. Rows L201, L1166; sources REG-137, REG-1103, REG-1109.
  - P6 Structured logging libraries writing directly to files or collectors. Best when: non-container contexts. Not argued in a read source; inferred. Row L201.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OWNERSHIP.CONTAINMENT (L198 boundary: library wrapping and dependencies)
- stack pointers: L197, L198: OpenTelemetry (stack tag).; L196: OpenTelemetry as reference realisation.

### OPERATION.TELEMETRY.4 Correlation and Context Propagation

- uid: `OPERATION.TELEMETRY.4`
- intent: How the events of one request are joined across tiers, logs, traces and client events.
- rows: L199, L1164, L1165, L1167, L1253 (5)
- positions (no verdict):
  - P1 Propagate one trace context across every tier and process boundary using the standard format of the transport (HTTP: W3C traceparent, tracestate for vendor data). Argument: traces from different vendors correlate. Rows L199, L1164; sources REG-122, REG-1102.
  - P2 Put trace id and span id in every log record; tag every event of one user interaction with a shared correlation id; stamp client error and real-user events with the release version and the trace or request id. Argument: incidents can be reconstructed, browser errors join server logs. Rows L1165, L1167, L1253 (L1253 inferred); sources REG-1089, REG-1103, REG-1141.
- context variables: none (no row says the best practice moves with a variable)
- links: Related TRANSVERSE.PRIVACY (L1171, now attached there: no personal data in the propagated context)
- stack pointers: L199: HTTP.; L1164: origin stack HTTP, restated neutral by the ledger.

### OPERATION.TELEMETRY.5 Trace Sampling

- uid: `OPERATION.TELEMETRY.5`
- intent: Whether traces are sampled and where the decision is made.
- rows: L200, L1169, L1170 (3)
- positions (no verdict):
  - P1 Head sampling: simple and cheap, cannot guarantee keeping error traces. Force: cost, simplicity. Best when: above about 1,000 traces per second with healthy predictable traffic. Rows L200, L1169; sources REG-119, REG-141, REG-237.
  - P2 Tail sampling: criteria-based, keeps errors and slow traces, stateful and operationally heavy. Force: completeness of rare-error traces. Best when: errors are rare and must all be kept and the team can run the infrastructure. REG-119 says it is almost always necessary in larger systems and that a hybrid is common. Rows L200, L1169.
  - P3 No sampling. Force: control, no missed signal. Best when: low volume, aggregate-only metrics, or retention obligations. Row L200.
  - P4 Start with head sampling and add tail sampling when volume requires (inferred). Row L1169.
  - P5 At a public boundary do not blindly continue the sampling decision of an untrusted caller: it can force tracing overhead. Row L1170; source REG-122.
- context variables: Trace volume and retention obligations (L200: head 'wins above about 1,000 traces/s', none 'at low volume or under regulation').
- links: none stated by a row
- stack pointers: L1170: origin stack HTTP, restated neutral.

### OPERATION.TELEMETRY.6 Telemetry Cost

- uid: `OPERATION.TELEMETRY.6`
- intent: How the volume and cardinality of telemetry are bounded as a cost.
- rows: L456, L457, L458, L459, L460 (5)
- positions (no verdict):
  - P1 Treat telemetry volume and cardinality as a cost to design (series count is roughly the product of distinct label values; trace, log and profile volume also count). Rows L456; sources REG-119, REG-235, REG-237.
  - P2 Keep metric label cardinality bounded: no unbounded values such as user ids, most metrics low-cardinality, a handful of high-cardinality ones, per-entity detail in logs or traces. Row L457; sources REG-235, REG-237.
  - P3 Filter low-value telemetry (health checks, static assets), coarsen histogram buckets, drop unused dimensions, accept a stated loss of granularity. Row L458 (single vendor); source REG-237.
  - P4 Instrument broadly: per-metric overhead is negligible except on code run above about 100,000 times per second, where it is benchmarked. Row L459; source REG-235. The ledger notes the tension with P1 (breadth against cardinality), resolved in REG-235 by bounding labels, not metrics.
  - P5 Set an explicit telemetry budget (volume, series count, retention) per service and review it, as the cost counterpart of an objective. Row L460. Open: no normative source found on telemetry cost as a governed budget.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row
- stack pointers: L457: Prometheus-style metrics systems (numbers are that tool's).; L458: Grafana and Prometheus-style tooling.; L459: Prometheus client libraries (numbers are that tool's).

### OPERATION.INCIDENTS Incidents

- uid: `OPERATION.INCIDENTS`
- intent: How an incident is declared, run and learned from, and how on-call load is bounded.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.INCIDENTS.1 Declaring and Running an Incident

- uid: `OPERATION.INCIDENTS.1`
- intent: On what conditions an incident is declared, who does what while it runs, and how the process is prepared.
- rows: L202, L203, L204 (3)
- positions (no verdict):
  - P1 Run major incidents with named roles (commander, operations, communications, planning or scribe); the commander keeps a live incident document; only the operations lead changes the system. Row L202; sources REG-127, REG-142.
  - P2 Declare on clear written conditions (second team needed, customer-visible, unresolved after an hour of focused analysis) and make declaring cheap. Argument: shared load, faster response. Row L203; source REG-127 (the 'cheap' part inferred).
  - P3 Reserve declaration for severe events (high bar). Argument: lower process cost and fatigue. Best when: tiny teams. Not found in a read source; open. Row L203.
  - P4 Define severity levels and the response each gets before an incident, rehearse until routine, hand over command explicitly. Row L204; sources REG-127, REG-142.
- context variables: Team size (L203: a high bar 'wins in tiny teams').
- links: none stated by a row

### OPERATION.INCIDENTS.2 Learning From Incidents

- uid: `OPERATION.INCIDENTS.2`
- intent: How incidents are reviewed so that they change the system, and how that ties into risk management.
- rows: L205, L206, L209, L1148 (4)
- positions (no verdict):
  - P1 Write blameless postmortems for significant incidents whether or not they paged, with written triggers (user-visible downtime, data loss, manual intervention, slow resolution, monitoring failure). Row L205; sources REG-113, REG-126, REG-135.
  - P2 Give every action item an owner, priority and tracker entry; make items measurable and preventative; publish within days; reward closeout, not only writing. Row L206; source REG-135.
  - P3 Integrate incident response with the organisation's (cybersecurity) risk management; aim to reduce the number and impact of incidents; share lessons as soon as identified and feed improvements into safeguards and detection. Argument: lessons reach the controls. Rows L209 (abstract level grounded, body unread), L1148 (the two rows state the same claim); sources REG-123, REG-1082.
- context variables: none (no row says the best practice moves with a variable)
- links: Related TRANSVERSE.SECURITY_MONITORING (L1148: improvements fed back into detection)

### OPERATION.INCIDENTS.3 On-Call and Toil Load

- uid: `OPERATION.INCIDENTS.3`
- intent: How the human cost of operating the system is bounded.
- rows: L207, L452 (2)
- positions (no verdict):
  - P1 Cap operational work (toil) at 50 percent of an engineer's time, on-call at about 25 percent and about two incidents per 12-hour shift, aim for near 1:1 alert-to-incident ratio, keep engineers on call occasionally for familiarity. Argument: team cognitive load and retention. Row L207; sources REG-113, REG-129, REG-130. The numbers assume dedicated teams of 6 to 8 or more per site.
  - P2 Size the on-call team so that on-call stays under about 25 percent and incident handling stays sustainable (single-site 24/7 needs at least eight engineers in the source's model). Row L452; source REG-130.
  - P3 Where developers own operations (small teams), each team decides its own limit or a different structure. Inferred by the ledger. Rows L207, L452.
- context variables: Operations ownership structure: dedicated rotation or developers own operations (L207: 'small teams where developers own operations must decide their own limit'; L452: 'small teams must trade this against coverage').
- links: none stated by a row

### OPERATION.CAPACITY Capacity

- uid: `OPERATION.CAPACITY`
- intent: How capacity is planned, headroom decided and storage health kept.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.CAPACITY.1 Planning Method

- uid: `OPERATION.CAPACITY.1`
- intent: When capacity is planned and in what units and from what inputs.
- rows: L436, L437, L438, L441 (4)
- positions (no verdict):
  - P1 Plan before predicted changes in usage (design, launch, marketing push, seasonal peak, feature release) and periodically; use historical data for existing workloads, pilots, expert judgment and external data for new ones. Row L436; sources REG-217, REG-221, REG-227.
  - P2 Model capacity directly in resources (CPU, memory, bandwidth, storage), not requests per second, because query costs differ widely. Row L437; sources REG-220, REG-227.
  - P3 Derive the resource proposal from requirements (objectives, traffic, record sizes) and iterate designs through scaling and failure domains, discarding a design a reliability requirement defeats. Single T2 source. Row L438; source REG-224.
  - P4 Replace spreadsheet plans with declared requirements from which allocations are computed. Best when: many services and frequent change (one organisation's scale). Row L441; sources REG-221, REG-227.
  - P5 A spreadsheet or dashboard forecast. Best when: a small team (inferred by the ledger, REG-227). Row L441.
- context variables: Number of services and change frequency (L441: declared requirements 'when the number of services makes manual plans brittle'; spreadsheet 'suffices' for a small team).
- links: none stated by a row

### OPERATION.CAPACITY.2 Headroom and Overload

- uid: `OPERATION.CAPACITY.2`
- intent: How much spare capacity is held and what protects against what planning cannot predict.
- rows: L439, L440 (2)
- positions (no verdict):
  - P1 Pair capacity planning with load testing and overload behaviour: planning lowers the probability of cascading failure but does not protect against infrastructure loss, partitions or unexpected spikes. Row L439; sources REG-203, REG-225.
  - P2 Pre-provision for peak and failover. Force: reliability, reversibility. Best when: hard peaks, long scale-up times, critical systems. Row L440 (a); sources REG-227, REG-228.
  - P3 Autoscale with tested limits. Force: cost. Best when: variable load with fast scale-up. Row L440 (b). Neither source fixes a numeric headroom; open. Account for scaling lag and for capacity in the failover environment.
- context variables: Load variability and scale-up time (L440: pre-provision 'wins for hard peaks, long scale-up times'; autoscale 'for variable load with fast scale-up').
- links: Realizes ASSURANCE.PERFORMANCE (L439 pairs planning with load testing, that node holds the measurements and budgets)

### OPERATION.CAPACITY.3 Storage Health

- uid: `OPERATION.CAPACITY.3`
- intent: How index and table health of the database store is kept as operational upkeep.
- rows: L317 (1)
- positions (no verdict):
  - P1 (MAINT) Find unused indexes by usage counters and drop them, watch index and table bloat, rebuild concurrently. Maintainer's codified practice, single source, not citable (REG-181); ledger notes public practice read as agreeing. Row L317.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row
- stack pointers: L317: PostgreSQL (stack-tagged pointer).

### OPERATION.READINESS Operational Readiness

- uid: `OPERATION.READINESS`
- intent: What must hold before a workload is launched and how that review is kept current.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.READINESS.1 Launch Gate and Checklist

- uid: `OPERATION.READINESS.1`
- intent: What a workload must show before launch and how the checklist is built.
- rows: L443, L445 (2)
- positions (no verdict):
  - P1 Verify readiness against a checklist covering architecture, capacity, failure modes, monitoring, emergency response, change management and rollout; do not launch a workload whose team cannot operate it. Row L443; sources REG-217, REG-218, REG-219, REG-231.
  - P2 Build the checklist from your own incidents and past launch failures, concrete and achievable items, start short (about thirty), tier by risk with fast paths for low-risk launches. Row L445; sources REG-218, REG-231, REG-232.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OPERATION.CAPACITY (capacity is a checklist area)

### OPERATION.READINESS.2 Who Performs the Review

- uid: `OPERATION.READINESS.2`
- intent: Whether readiness is judged by an independent team or certified by the owning team.
- rows: L444 (1)
- positions (no verdict):
  - P1 Independent reviewing team that examines the service and negotiates improvements. Force: control, quality, knowledge transfer. Best when: critical services, few reviewers' capacity matched to service count, or ownership handed to a separate operations team. Sources REG-218, REG-219.
  - P2 Self-service checklist the owning team certifies against. Force: delivery speed, scalability across decentralised teams. Best when: many teams, mature culture, executive sponsor. Sources REG-231, REG-232. Evidence of relative effectiveness: none read; open.
- context variables: Number of teams and service criticality (L444: independent 'wins for critical services'; self-service 'wins with many teams, mature culture, executive sponsor').
- links: none stated by a row

### OPERATION.READINESS.3 Keeping the Review Current

- uid: `OPERATION.READINESS.3`
- intent: How the review stays true over the workload's life and how repeated findings become defaults.
- rows: L446, L447 (2)
- positions (no verdict):
  - P1 Re-run the review periodically with a subset on a regular cadence to catch drift and add lessons. Single T1 source. Row L446; source REG-231.
  - P2 Convert repeated findings into automated guardrails and defaults. Examples are AWS services. Row L447; sources REG-218, REG-231.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row
- stack pointers: L447: examples are AWS services (stack tag neutral).

### OPERATION.RUNBOOKS Runbooks and Playbooks

- uid: `OPERATION.RUNBOOKS`
- intent: How operating procedures are written, owned, validated and automated.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.RUNBOOKS.1 Form, Ownership and Validation

- uid: `OPERATION.RUNBOOKS.1`
- intent: What a procedure document contains, who owns it, how it is proved usable, and how investigation differs from mitigation.
- rows: L448, L450 (2)
- positions (no verdict):
  - P1 Versioned step-by-step documents with an owner, required tools and permissions, error handling and escalation; validated by having another team member run them; updated through change management. Single T1 source, consistent with REG-222. Row L448; sources REG-222, REG-233.
  - P2 Separate playbooks (investigate and scope an incident) from runbooks (mitigate a known cause); link the playbook from the alert; give each an escalation path when the cause is unknown. Row L450; sources REG-223, REG-234.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OPERATION.ALERTING.1 (L450: playbook linked from the alert); Related OPERATION.RECOVERY.6 (L1111: recovery plan and runbooks kept current)

### OPERATION.RUNBOOKS.2 Automation

- uid: `OPERATION.RUNBOOKS.2`
- intent: Whether and in what order procedures are turned into scripts and automatic remediation.
- rows: L449 (1)
- positions (no verdict):
  - P1 Mature runbooks and playbooks from text toward scripts and auto-remediation, starting with short, frequently used, low-risk ones. Single vendor. Row L449; sources REG-233, REG-234. Open: cost and risk of automating a wrong runbook.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.RECOVERY Backup, Restore and Disaster Recovery

- uid: `OPERATION.RECOVERY`
- intent: How backups are designed and protected, objectives set, strategy chosen and failover and failback carried out.
- rows: - (roll-up of children)
- positions: on the children
- context variables: none (no row says the best practice moves with a variable)
- links: Realizes ASSURANCE.AVAILABILITY (that node holds the proof: restore tests and exercises, this node holds the practice, MD-03)

### OPERATION.RECOVERY.1 Recovery Objectives

- uid: `OPERATION.RECOVERY.1`
- intent: How tolerable downtime and data loss are defined, per workload, before any mechanism is chosen.
- rows: L1080, L1081, L1082, L1083, L1084 (5)
- positions (no verdict):
  - P1 Set a recovery time and a recovery point objective per workload or data class from the impact of downtime and data loss, grouped in criticality tiers. Row L1080; sources REG-1054, REG-1059, REG-1064, REG-1065.
  - P2 Do not set arbitrary, zero or stricter-than-needed objectives: cost and complexity rise as the objective shortens. Row L1081; sources REG-1054, REG-1055, REG-1059, REG-1065.
  - P3 Make a workload's objectives compatible with those of its dependencies and dependants; derived data inherits the recovery point of its sources. Row L1082; source REG-1054.
  - P4 Define what counts as a disaster, a major disruption or a small incident by user and business impact, build the thresholds into monitoring so recovery is triggered by criteria. Row L1083; sources REG-1060, REG-1064.
  - P5 State data recovery (how much may be lost, whether intact) and service recovery (how fast it runs again) as separate objectives; a data disaster has recovery time above zero and a recovery point before its discovery even where failover is near instant. Row L1084 (framing as two objectives inferred); sources REG-1051, REG-1055, REG-250.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OPERATION.RELIABILITY.2 (L1081: see also L174, a target below 100 percent)

### OPERATION.RECOVERY.2 Backup Scope and Design

- uid: `OPERATION.RECOVERY.2`
- intent: What is backed up, how often, with which capability, and how platform state is covered; what to verify of a rented service's backups is held in `OWNERSHIP.SERVICES`.
- rows: L1079, L1085, L1086, L1091, L1093, L1094, L1118 (7)
- positions (no verdict):
  - P1 Replication and redundancy are availability measures, not recovery: keep versioned or point-in-time copies, because replication propagates damage. Row L1079; sources REG-1051, REG-1055, REG-250.
  - P2 Identify and classify all data sources; back up what cannot be recreated. Row L1085; sources REG-1052, REG-1054.
  - P3 For data reproducible from other sources define and test the reproduction path instead of backing it up, provided it meets the recovery time objective. Row L1085.
  - P4 Back up everything required to rebuild the service (configuration, infrastructure definitions, code and images, system information, recovery documentation). Row L1086; sources REG-1051, REG-1061, REG-1062.
  - P5 Back up cryptographic keys and the information to use them on independent storage separate from the encrypted data; decide per key type. Row L1091 (one source); source REG-1068.
  - P6 Choose frequency from the recovery point and locality from the recovery time; provide point-in-time recovery where corruption may be found late; where a database needs it, use continuous archiving of the transaction log with base backups (a logical dump alone cannot). Rows L1093, L1094; sources REG-1051, REG-1052, REG-1066, REG-250.
  - P7 Where cluster or platform state is the source of truth, back it up explicitly and test its restore; the platform's high availability does not replace it. Row L1118; sources REG-1051, REG-1071, REG-250.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OWNERSHIP.SERVICES (L1112, now attached there, with its see also L359, L040, L356)
- stack pointers: L1094: PostgreSQL (pointer for the stack guideline).; L1118: Kubernetes (pointer).

### OPERATION.RECOVERY.3 Backup Protection and Isolation

- uid: `OPERATION.RECOVERY.3`
- intent: How backups are kept out of reach of the failure and the attacker that threaten production.
- rows: L1087, L1088, L1089, L1090, L1117 (5)
- positions (no verdict):
  - P1 Keep at least one backup copy outside the failure and attack domain of production. Consensus on the need, majority on the form. Row L1087; sources REG-1051, REG-1061, REG-1062, REG-1063, REG-1067, REG-250.
  - P2 Offline or air-gapped copy. Argument: strongest against an attacker with network or credential access (a case where tape survived a redundancy failure). Force: security, correctness. Cost: slow restore, handling effort. Best when: the threat model includes a destructive adversary and restore time allows. Row L1088; sources REG-1062, REG-1063, REG-250.
  - P3 Immutable (write-once) retention enforced by the platform, in a mode even the account owner cannot override or one privileged users can. Force: restore speed, reversibility. Cost: trust in the platform, no early deletion (retention against erasure). Best when: restores must be fast and the platform account is itself protected. Row L1088; sources REG-1062, REG-1067.
  - P4 Separate account, region or provider. Force: exit risk, blast radius. Cost: duplicate tooling and spend. Best when: vendor-level or account-level loss is in the threat model. Row L1088; sources REG-1051, REG-1062.
  - P5 3-2-1 baseline (several copies, more than one storage kind, one off-site). Best when: the threat is hardware, site or operator error. Row L1089; source REG-1063.
  - P6 3-2-1-1-0 (adds an immutable or offline copy and a verified restore). Vendor-originated (T3). Best when: ransomware or insider deletion is in scope. Row L1089 (extension inferred); sources REG-1062, REG-1067, REG-1077.
  - P7 Protect backups' confidentiality, integrity and availability: encrypt, restrict write and delete rights, require dual authorisation for deletion. Row L1090 (boundary SECD); sources REG-1061, REG-1062.
  - P8 Put an attacker who already holds production credentials in the backup threat model: a backup reachable with production credentials is not independent. Row L1117 (percentages are T3, read in summaries); sources REG-1062, REG-1063, REG-1076.
- context variables: Threat model and restore-speed requirement (L1088: each isolation form 'wins when' a named threat is in scope; L1089: 3-2-1 against 3-2-1-1-0 by 'when ransomware or insider deletion is in scope').
- links: none stated by a row
- stack pointers: L1088: REG-1067 AWS S3 as stack example.

### OPERATION.RECOVERY.4 Recovery Strategy, Failover and Failback

- uid: `OPERATION.RECOVERY.4`
- intent: Which standby posture each tier gets, who triggers failover, and how the way back is run.
- rows: L1101, L1105, L1106, L1107, L1110 (5)
- positions (no verdict):
  - P1 Choose the strategy per tier from the ladder (backup and restore, pilot light, warm standby, active/active) by objectives against cost and complexity; never a rung stricter than needed. Row L1105 (rung boundaries are AWS figures); sources REG-1051, REG-1055, REG-1059, REG-1064, REG-1065.
  - P2 Maintain a standby (pilot light, warm) and rehearse it. Force: recovery cost against time. Best when: objectives do not justify running everything everywhere and the standby is exercised. Row L1101; sources REG-1051, REG-1055, REG-1056.
  - P3 Avoid a rarely used fallback: make the production path the only path (for example active in every location). Argument: a rarely used path hides latent bugs, is hard to test and can turn a partial outage into a full one. Force: correctness, cognitive load. Best when: the fallback would run seldom and cannot be tested realistically. Row L1101; source REG-1075 (T3, argued for request-time fallback). Ledger reconciliation (inferred): both agree an unexercised path is a liability.
  - P4 Active/active as an availability and recovery choice together. Force: recovery time, utilisation. Best when: a full second environment is accepted for other reasons (latency, global audience); it does not remove the need for backups and a tested data-disaster recovery. Row L1106; sources REG-1051, REG-1055.
  - P5 Warm standby as the economical simpler alternative. Force: cost, cognitive load. Best when: seconds-to-minutes recovery is acceptable. Row L1106.
  - P6 Failover started by a person through an automated push-button procedure. Argument: a false alarm costs availability and data because recovery time and point are above zero. Force: reversibility, correctness. Best when: failover itself costs data or availability. Row L1107; sources REG-1051, REG-1055.
  - P7 Automatic failover on health signals with trained oversight and tuned thresholds (manual approval gates only where needed). Force: recovery time. Best when: the objective is shorter than a human can meet. Row L1107; source REG-1064.
  - P8 Plan failback as a separate defined process; the hard part is re-synchronising data stores; the recovery site may instead be promoted to primary. Row L1110; sources REG-1055, REG-1064.
- context variables: none (no row says the best practice moves with a variable)
- links: Requires OPERATION.RECOVERY.1 (a rung is chosen against the objectives)

### OPERATION.RECOVERY.5 Recoverability of Recovery Itself

- uid: `OPERATION.RECOVERY.5`
- intent: How recovery is kept independent of what failed, rebuilt from source, and held to the production baseline.
- rows: L1108, L1109, L1115, L1116 (4)
- positions (no verdict):
  - P1 Make recovery independent of what failed: simple operations that remain available, pre-provisioned capacity, recovery tooling, runbooks, credentials, certificates, pipelines and contact paths where the failure cannot take them away, offline copies for the worst case. Row L1108 (control-plane vocabulary is AWS; principle neutral); sources REG-1051, REG-1057, REG-1062, REG-1064, REG-1074.
  - P2 Define infrastructure and environment as code and be able to rebuild from source on a clean machine or account; rebuilding regularly detects drift and is itself a recovery capability. Row L1109 (boundary DELIVER, TRANS); sources REG-1051, REG-1062, REG-1072.
  - P3 Accept slower recovery for rare events in return for day-to-day security of recovery-critical systems. Single T3 source (a large operator). Row L1115; source REG-1074.
  - P4 Favour recovery speed over hardening. Not argued in any source read; open. Row L1115.
  - P5 Hold the recovered environment to the production security baseline and address the root cause before recovery starts. Row L1116 (boundary SECD); sources REG-1064, REG-1065.
- context variables: none (no row says the best practice moves with a variable)
- links: none stated by a row

### OPERATION.RECOVERY.6 Ownership, Monitoring, Roles and Plan Upkeep

- uid: `OPERATION.RECOVERY.6`
- intent: Who owns durability, how backup jobs are watched, who does what in a recovery, and how the plan stays current.
- rows: L1095, L1096, L1111, L1113 (4)
- positions (no verdict):
  - P1 Monitor backup and restore jobs and route failure alerts over a path that is itself verified: an undelivered failure notice equals no monitoring. Row L1095 (inferred from a case and REG-250); sources REG-1073, REG-250.
  - P2 Name an owner for data durability, including regular testing of backup and restore; a procedure nobody owns is not tested. Row L1096 (inferred, one case study); sources REG-1053, REG-1073.
  - P3 Keep the recovery plan, runbooks and contact lists current: review periodically and on every change to the system, the organisation, or after a test or incident; keep them accessible. Row L1111 (boundary TRANS); sources REG-1055, REG-1059, REG-1064.
  - P4 Assign recovery roles ahead of time (declares, executes, communicates, closes), prepare channels and templates, declare the end of recovery by stated criteria once restored assets are verified. Row L1113 (boundary OPERATE); sources REG-1059, REG-1060, REG-1064.
- context variables: none (no row says the best practice moves with a variable)
- links: Related OPERATION.INCIDENTS.1 (L1113: see also L202, L204); Related OPERATION.RUNBOOKS.1 (L1111: see also L448); Related ASSURANCE.AVAILABILITY (L1096: regular restore testing)

### OPERATION.FEEDBACK Feedback into Development

- uid: `OPERATION.FEEDBACK`
- intent: How production signals about delivery return to the people who change the system.
- rows: L208 (1)
- positions (no verdict):
  - P1 Track failed-deployment recovery time and change fail rate as production feedback on delivery, at the level of one service, shared across development and operations, never as targets. Argument: DORA warns that metric targets invite gaming. Force: honest signal. Row L208; source REG-093.
  - P2 Set targets on these measures to drive improvement. Contrary view; not argued in a read source; open. Row L208.
- context variables: none (no row says the best practice moves with a variable)
- links: Related CHANGE_FLOW.MEASURE (L208 boundary DELIVER, see also L169)

## Routing objections

Six were raised; each is resolved in `../../objections/resolution.md`. Moved (row now sits on the target branch, no longer listed): L1112 to `OWNERSHIP.SERVICES`, L1171 to `TRANSVERSE.PRIVACY`. Kept (listed with the node it might belong to, and the reason it stays).

| row | node I would route it to | reason | resolution |
|---|---|---|---|
| L208 | `CHANGE_FLOW.MEASURE` | Failed-deployment recovery time and change fail rate are delivery measures; MEASURE holds how delivery is measured. L208 cites L169 (DELIVER-C46) as a near row. | kept: OPERATION.FEEDBACK exists for exactly this row (production signals about delivery returning to developers) and moving it would leave that L2 node empty |
| L1177 | `ASSURANCE.PERFORMANCE` | Enabling per-statement database statistics so slow queries are found by measurement is a performance measurement mechanism; origin boundary tag DATA. | kept: it is the instrumentation that exposes a signal (what is measured and from where); ASSURANCE.PERFORMANCE.5 states measure-before-optimising, not which signals are switched on |
| L1096 | `ASSURANCE.AVAILABILITY` | Regular testing of backup and restore is the proof of recovery, which that node holds (split-topic table); the owner clause could stay here. | kept: the row's claim is who owns durability (the node's intent); the proof by regular restore test is already stated there by L1097 and L1078, so moving would add nothing |
| L1111 | `ASSURANCE.DOCS_SYNC` | Keeping a plan and runbooks current on every change is documentation in sync; origin boundary tag TRANS (documentation in sync); see also L448, L446, L216. | kept: the upkeep of the recovery plan and runbooks is stated with L446 and L448 in OPERATION (readiness and runbooks); the generic freshness rule of DOCS_SYNC.3 does not carry the review triggers of a recovery plan |
