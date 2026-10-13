# Judged records: unit J7_operation

Branch OPERATION: the L1 node, 9 L2 nodes and 31 L3 nodes (41 nodes, 109 rows; TELEMETRY.7 and .8 added by the final pass). Decisions follow MD-01 (the best, not the average), MD-02 (outcomes, whoever does the work) and MD-03 (one location per fact). Rows are cited by ledger id, sources by register id (REG); MAINT rows (REG-181) are not citable and weigh as a strong position. Certainty words: grounded, inferred, open.

Decided inputs read: J4 (ASSURANCE.PERFORMANCE, AVAILABILITY) and J3 (DATA_INTEGRITY.3, .4, DOCS_SYNC.3, SECURITY.7), final after review. Realization rule: this unit carries out those decisions and never re-decides them.
Decisions marked undecided: none.
Settled decisions disagreed with: none. The one wording tension with a settled decision (flag F1) is settled by the final pass (cross-unit line X11).
Flags raised: F1 to F11, listed at the end; all settled by the final pass, none open.
Role of the L1 record: written as a roll-up of its nine children (the review found FEEDBACK missing from the first wording, now added); wave 3 may re-roll it.

How the realization nodes bind to the decided ones (read once, not restated below):
- AVAILABILITY.4 and .5 (J4) fix the proof of restore and recovery exercises; OPERATION.RECOVERY holds the practice and its objectives, which are the criteria that proof is fixed against.
- PERFORMANCE.2 (J4) fixes the breaking point and its early-warning metrics; OPERATION.CAPACITY consumes them. PERFORMANCE.1 and .5 fix targets and distributions for tests; OPERATION.RELIABILITY fixes the same for the service in production.
- DATA_INTEGRITY.4 (J3) requires the scheduled-work monitoring signals held in TELEMETRY.8.
- DOCS_SYNC.3 (J3) fixes owner, dated verification and review for every hand-written document; RUNBOOKS and RECOVERY.6 apply it to procedures and recovery plans and add what is specific to them.
- SECURITY.7 (J3) fixes that detection itself is probed; INCIDENTS.2 and TELEMETRY.2 apply the same idea to postmortems and the telemetry pipeline.

---

## OPERATION Operation

Intent: how the running system is kept within its reliability targets and recovered when it fails.
1. Decision: The running system is held to a stated reliability objective measured as users experience it, paged on only when a human is needed, observable well enough to answer questions nobody planned, run by an incident process that changes the system, sized and checked before launch, documented by procedures that were run before they were needed, and recoverable by backups and strategies chosen against stated recovery objectives; production feedback on delivery is tracked per service and never made a target. Outcome: the system stays within its objectives at a cost and load the team can sustain, and when it fails it is restored within them.
2. Grounds: roll-up of the nine L2 records; the claim is inferred from them, each with its own certainty.
3. Positions: see children.
4. Rejected: see children.
5. Context: see children (objective consequence, team size, load shape, threat model, criticality).
6. Certainty: inferred (roll-up). The weakest children are TELEMETRY.6, RECOVERY.5 and READINESS.2.
7. Flags: none.
Constraints: every child's MUST. Links: Realizes ASSURANCE.AVAILABILITY and PERFORMANCE; index only here.

## OPERATION.RELIABILITY Reliability Targets

Intent: how reliability is defined and traded against release speed: indicators, objectives, error budget.
1. Decision: Reliability is defined as an objective below 100 percent on a few user-view indicators, and the gap to it is a written, agreed rule that trades release speed against reliability, with its consequence decided before it is needed. Outcome: reliability is a number users would recognise, and speed and reliability are traded by rule, not by argument.
2. Grounds: roll-up of RELIABILITY.1 to .4.
3. Positions: see children. 4. Rejected: see children.
5. Context: see children (.4 only).
6. Certainty: inferred (roll-up); children grounded except one open minority view in .3.
7. Flags: none.
Constraints: every child's MUST. Links: Realizes ASSURANCE.AVAILABILITY (objectives and budget the availability proof is read against); refined by ASSURANCE.PERFORMANCE.1 (targets for tests); index only here.

### OPERATION.RELIABILITY.1 Indicators

Intent: what is measured to define reliability, so that the definition matches what users experience.
1. Decision: Define reliability through a handful of simple indicators measured from the user's point of view and anchored on critical user journeys; add one only for a coverage gap. State latency as percentiles or distributions, never as an average alone. Outcome: the number the team watches moves when users are hurt, and the tail is not hidden.
2. Grounds: user-view, journeys, few and simple (L175, L176, L178, L1174; REG-117, REG-125, REG-134, consensus); percentiles (L177, L1173; REG-124, REG-125, REG-226, consensus). The percentile rule is held here (cross-unit line X11): ASSURANCE.PERFORMANCE.1 keeps its threshold on a percentile and points here; PERFORMANCE.5 keeps its own run-to-run distribution rule.
3. Positions: P1 user-view indicators on journeys (fit to user need, cognitive load). P2 latency as distribution (realism of the signal).
4. Rejected: infrastructure metrics as the definition of reliability (they do not show user experience; best as diagnostic signals, see TELEMETRY.1). Averages alone (hide the tail; best never as a sole statement).
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST measure indicators from the user's side; MUST state latency as a percentile or distribution; MUST keep the indicator set small. Links: Requires nothing; required by RELIABILITY.2 and ALERTING.2; holds the percentile rule that ASSURANCE.PERFORMANCE.1 points to; see ASSURANCE.PERFORMANCE.5.

### OPERATION.RELIABILITY.2 Objective Level and Starting Point

Intent: how the reliability objective is chosen, and from what it starts.
1. Decision: Set the objective below 100 percent, from user need and the cost of each extra step, never copied from current performance as a final value. Where no objective exists and user need is not yet known, a provisional objective taken from what is cheaply measurable (existing logs) is allowed, marked provisional and reviewed on a fixed cadence until it is replaced by one derived from user need. Outcome: the objective reflects what users need, and no objective stays a mere record of the past.
2. Grounds: below 100 percent (L174; REG-128, REG-134, consensus); not from history, with a way to iterate (L179, L1174; REG-125, REG-134). The two Google sources are reconciled by "start, then review" (ledger note on L179): they disagree on the starting point only, so the decision keeps one rule with the start as its stated condition, not a blend.
3. Positions: P1 below 100, cost-weighed (cost of ownership, fit). P2 from user need (reliability fit). P3 start from the measurable and iterate (delivery speed, feedback).
4. Rejected: 100 percent (cost rises steeply, users cannot tell; best never). An objective fixed from history with no review (ratifies what exists; best never). Waiting for a perfect user-need study before any objective (best never: no feedback loop exists meanwhile).
5. Context: user need known (contracts, known users): set from need directly; not known and no objective exists: provisional start as above (L179 states both conditions).
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST NOT set 100 percent; MUST derive from user need or mark provisional with a review date; MUST be set on an indicator of RELIABILITY.1. Links: Requires RELIABILITY.1; required by RELIABILITY.3, ALERTING.2.

### OPERATION.RELIABILITY.3 Error Budget as Trade Mechanism

Intent: whether and how the gap between 100 percent and the objective is used as the shared rule that trades release speed against reliability.
1. Decision: Use the gap between 100 percent and the objective as an error budget: a written policy, agreed by those who decide release speed and those who answer for reliability, states how the remaining budget governs release decisions; without that agreement the objective is only a report. Consumption of the budget is one of the written postmortem triggers (INCIDENTS.2), with thresholds set in the policy. Outcome: velocity and reliability are traded by a rule both sides accepted before the dispute.
2. Grounds: budget as shared objective rule (L180; REG-113, REG-128, majority); written and agreed (L181; REG-134 and REG-128 state that product and operations must agree; REG-133 is an example policy and is kept for the freeze and the postmortem trigger, not for the agreement rule; consensus); postmortem trigger from consumption (L183; REG-133, one example policy). The row's own condition (separate parties needing a depoliticised rule) is where the budget earns most; the written-policy requirement holds wherever more than one party decides.
3. Positions: P1 budget as shared rule (velocity and reliability jointly). P2 no budget, judgment (unsourced minority). P3 written, agreed policy (binding effect). P4 postmortem triggers from consumption (ties learning to the budget).
4. Rejected: judgment without a budget: best when one party owns both speed and reliability and the choice is its own (inferred; the row records no source, open). An unwritten or unagreed budget (a report, not a rule; best never as a trade mechanism). The numbers of the example trigger (20 percent in four weeks) are illustrative of one policy and are not adopted as a threshold.
5. Context: none beyond the separate-parties note above.
6. Certainty: grounded for P1 and P3; grounded as an example for P4; open for P2.
7. Flags: none.
Constraints: MUST write the budget policy and have it agreed; MUST name the consumption levels that trigger a postmortem. Links: Requires RELIABILITY.2; refines INCIDENTS.2 (L205 holds the trigger list).

### OPERATION.RELIABILITY.4 Budget Exhaustion Consequence

Intent: what the exhaustion of the error budget does to releases, decided before it happens.
1. Decision: The consequence of exhausting the budget is decided in advance, written in the budget policy, and binding. With many consumers, strict commitments or a weak safety culture it is a freeze of changes except top-priority and security fixes, with disputes escalated to a named person; in a small, high-trust team it may be self-regulation (the team slows and adds testing), still stated beforehand. Outcome: when the budget runs out the response is automatic and not a negotiation.
2. Grounds: L182 (REG-128, REG-133); the row names both forms and the conditions under which each wins. Contested; both are conditional best, neither is the average of the other.
3. Positions: P1 hard freeze (control, reliability). P2 self-regulation (delivery speed, autonomy).
4. Rejected: no stated consequence (the budget then does not bind; best never). Freeze in a small high-trust team is not wrong but costs speed it does not need (P2 is best there); self-regulation with many consumers or strict commitments gives no assurance (P1 is best there).
5. Context: number of consumers, strictness of commitments, safety culture (L182).
6. Certainty: grounded for the need to decide in advance; inferred for the culture condition (one pair of sources, no measurement of either form).
7. Flags: none.
Constraints: MUST state the consequence before exhaustion; MUST name the escalation owner where a freeze applies. Links: Requires RELIABILITY.3.

## OPERATION.ALERTING Alerting

Intent: when a human is paged and how alerts are built.
1. Decision: A human is paged only for what needs a human now, on the symptom users feel, and the rule set is pruned to that. Outcome: every page is worth waking someone for.
2. Grounds: roll-up of ALERTING.1 and .2.
3.-4. See children.
5. Context: see .2.
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.PERFORMANCE (alerts on the objective); index only here.

### OPERATION.ALERTING.1 Paging Criterion and Rule Hygiene

Intent: which conditions justify waking a person, and how the rule set is kept to those.
1. Decision: Page only for a condition that is urgent, actionable and actively or imminently user-visible; everything else is a ticket or a log. Every page must need human judgment: a page answerable by a mechanical response is automated or removed. Rules and signals that are never exercised or never exposed are removed; rules that catch real incidents stay simple and predictable. Outcome: pages are few, each is real, and none is a task a script could do.
2. Grounds: L184, L1175 (REG-113, REG-124, consensus); L186 (REG-124); L188 (REG-124). The three are one outcome seen from the page, the response and the rule set, not competing practices.
3. Positions: P1 page criterion (cognitive load). P2 human judgment required. P3 prune unexercised rules.
4. Rejected: paging on any threshold breach or on every cause signal (each page costs attention; best never as paging, kept as ticket or diagnosis). Retaining rarely exercised rules for completeness (best never).
5. Context: none.
6. Certainty: grounded (one source family, REG-124, for the last two clauses).
7. Flags: none.
Constraints: MUST classify every alert as page, ticket or log; MUST automate or remove a page answerable by script; MUST review rules for never-exercised ones. Links: Related RUNBOOKS.2 (automation), INCIDENTS.3 (alert-to-incident ratio).

### OPERATION.ALERTING.2 Alert Basis

Intent: what an alert is built on: user-visible symptom, internal cause, or the rate of error-budget consumption.
1. Decision: Page on user-visible symptoms; keep cause signals for diagnosis. A cause signal pages only when it predicts imminent user-visible failure that the symptom signal cannot yet show (a failure masked by retries, a resource about to run out), because only then does it meet the paging criterion of ALERTING.1. Where an objective exists and false pages are costly, express the symptom alert as budget burn rate over several windows (page for fast burn, ticket for slow burn); where no objective exists, simple threshold alerts on the symptom are enough; where traffic is too low for a burn rate to be meaningful, use the source's remedies (synthetic traffic, combining services under one objective) rather than simple thresholds. Outcome: pages track user harm, with early warning only where harm is imminent.
2. Grounds: symptoms, with white-box for imminent or retry-masked failures (L185; REG-124, REG-131, majority); burn rate versus thresholds (L187; REG-132, one authority, simpler strategies documented as inferior on precision, recall and reset time; the low-traffic remedies are from the same source, fetched in the final pass review). The ledger's early-warning-against-noise tension is resolved by the criterion of ALERTING.1, not by a blend.
3. Positions: P1 symptoms only (cognitive load). P2 symptoms plus white-box cause alerts (early warning). P3 simple thresholds (maintenance cost). P4 multiwindow burn rate (precision).
4. Rejected: cause alerts as a default page (noise; best only under the imminent-failure condition). Thresholds when an objective exists and false pages cost much (P4 is better; best where no objective exists). Burn-rate alerts with no objective (nothing to burn; best never).
5. Context: whether an objective exists and the cost of a false page (L187); on-call capacity moves how many cause alerts can be afforded (L185).
6. Certainty: grounded for symptoms; grounded on a single authority for burn rate (no independent measurement; open); inferred for the imminent-failure reconciliation.
7. Flags: none.
Constraints: MUST page on a symptom or on a cause with a stated imminent user-visible consequence; MUST NOT use burn-rate alerts without an objective. Links: Requires RELIABILITY.2, .3.

## OPERATION.TELEMETRY Telemetry

Intent: what is measured, logged and traced, how it is correlated, and what it costs.
1. Decision: Every service exposes the signals that show user harm and resource strain, observed from inside and outside, emitted through a vendor-neutral path, joined by one correlation context, sampled by an explicit rule, and bounded as a cost. Outcome: any incident can be reconstructed and any slow query or silent failure found, at a volume the team can afford.
2. Grounds: roll-up of TELEMETRY.1 to .8.
3.-4. See children.
5. Context: see .5 (volume, retention).
6. Certainty: inferred (roll-up); .2 and .6 carry open parts.
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.PERFORMANCE (signals, L1177), required by ASSURANCE.DATA_INTEGRITY.4 through TELEMETRY.8 (job signals); index only here.

### OPERATION.TELEMETRY.1 What Is Measured: Service and Resource Signals

Intent: which signals every service exposes and how resources and queries are read.
1. Decision: The standard set is latency, traffic, errors and saturation: latency, traffic and errors are the request signals every service exposes alike, so anyone can be on call for code they did not write, and saturation is read per resource (utilisation, saturation, errors). Infrastructure is read through utilisation, saturation and errors per resource, used as a quick first check and, when a bottleneck is investigated, by enumerating resources first and checking each. Database statistics per statement are enabled so slow queries are found by measurement. Outcome: service harm and resource strain are visible, and slow queries are found by measurement.
2. Grounds: four golden signals (L190, L1172; REG-124, REG-138); minimal per-service set, T3 sources with the T2 golden signals as counterpart (L191); USE as first check, not a full method (L192, L1180; REG-138); statistics (L1177; REG-1108). The four positions answer different questions (which signals, for which resource, which queries), so each stands. Vantage points are held in TELEMETRY.7 and scheduled-work signals in TELEMETRY.8 (cross-unit line X12; split of the former eleven-row node).
3. Positions: P1 golden signals. P2 minimal per-service set (on-call familiarity). P3 USE as first check. P4 per-statement statistics.
4. Rejected: USE as a complete diagnostic method (REG-138 says it is not).
5. Context: none.
6. Certainty: grounded for P1, P3, P4; P2 as stated by T3 sources with the T2 signals as counterpart.
7. Flags: none.
Constraints: MUST expose latency, traffic, errors and saturation per user-facing service. Links: Related TELEMETRY.7, TELEMETRY.8, ASSURANCE.PERFORMANCE.3, .5; stack pointer L1177 (PostgreSQL statistics).

### OPERATION.TELEMETRY.2 Observability Model and Pipeline Health

Intent: how monitoring and observability relate, how telemetry is stored, who is proficient with it, and how the pipeline itself is checked.
1. Decision: Provide monitoring (predefined questions, for alerting) and observability (the ability to ask questions nobody defined, for unknown failures), designed in across every tier as correlated signals of one system, and make every developer proficient with them. The storage model is chosen by condition: separate metrics, logs and traces with standard signals where metric alerting dominates and cardinality is low (cheap aggregates, mature tooling); wide structured events as the single store where failures are novel and distributed and high-cardinality questions are routine. Whatever the model, the pipeline is itself checked, so silence from it is detected. Outcome: unknown failures are answerable, and a dead telemetry pipeline cannot pass for a healthy system.
2. Grounds: both needed (L193; REG-117, REG-136); correlated signals designed in (L1163, L1181; REG-044, REG-118, REG-1103, REG-1110, L1181 inferred); storage model contested (L194; REG-118, REG-140 vendor T3, REG-141): evidence is argued, not measured; shared proficiency (L195; REG-136); monitor the monitoring (L455; REG-217, single T2, one line). The decision states the required outcome (exploration across high-cardinality data, bounded cost) and gives each store its stated condition.
3. Positions: P1 both. P2 replace the three-pillars model (vendor). P3 separate stores. P4 wide events. P5 trade-off framing. P6 correlated, designed in. P7 shared proficiency. P8 monitor the monitoring.
4. Rejected: the claim that the three-pillars model is to be replaced as a universal (vendor interest, T3; the underlying point, correlation and high-cardinality questions, is kept in the decision). Wide events as the universal store (best in the stated condition; the cost premise is disputed by REG-141). Separate stores as the universal (best in the stated condition). Observability as an operations-only task (best never: code authors hold the context).
5. Context: alerting load against failure novelty and cardinality (L194).
6. Certainty: grounded for both-needed, correlation and proficiency; inferred for the pipeline check mechanism (a heartbeat or known test event that must arrive, not stated in the source) and for the condition split (argued, not measured).
7. Flags: none.
Constraints: MUST design correlation in; MUST detect a silent failure of the pipeline. Links: Related SECURITY.7 (probe that detection works, J3); TELEMETRY.4 (correlation).

### OPERATION.TELEMETRY.3 Instrumentation and Log Emission

Intent: how code is instrumented and how logs leave the application.
1. Decision: Instrument against a vendor-neutral API with standard semantic conventions, so names stay consistent and the backend can change; use automatic instrumentation for framework, HTTP and database-client coverage and code-based instrumentation only for business logic; libraries depend on the instrumentation API only, never on an implementation, so applications that collect nothing pay nothing. The application writes logs as an unbuffered event stream (structured, so they carry correlation ids) to standard output and does not own routing or storage; the execution environment collects and routes them. Outcome: telemetry is consistent across code, libraries and platforms, with no lock-in and no cost where unused.
2. Grounds: neutral API (L196; REG-120, REG-121, majority); combined instrumentation (L197, L1168; REG-121, REG-1104); libraries depend on the API (L198; REG-121); stdout event stream (L201, L1166; REG-137, REG-1103, REG-1109). Structured form inferred from TELEMETRY.4 (ids in every record).
3. Positions: P1 vendor-neutral API (exit risk). P2 vendor SDK (time to value). P3 zero-code plus code-based. P4 libraries depend on the API. P5 stdout event stream (separation of concerns). P6 logging libraries writing to files or collectors.
4. Rejected: the vendor SDK as default (unsourced against REG-120; best when one backend is fixed and a vendor feature outweighs exit cost, then behind the neutral API where possible; inferred). Application-managed log files and routing where an environment collector exists (best never there; best where no execution environment collects output, with routing configured outside the code, inferred).
5. Context: process-based application with a collecting environment: stdout; otherwise log to a file or collector as structured events (L201).
6. Certainty: grounded for P1, P3, P4; grounded for P5 for process-based apps; inferred for P2 and P6 (unargued in a read source).
7. Flags: none.
Constraints: MUST use a vendor-neutral instrumentation API; MUST NOT make a library depend on an implementation; MUST NOT route or store logs in application code where the environment does. Links: Related OWNERSHIP.CONTAINMENT; stack pointers L196-L198 (OpenTelemetry).

### OPERATION.TELEMETRY.4 Correlation and Context Propagation

Intent: how the events of one request are joined across tiers, logs, traces and client events.
1. Decision: Propagate one trace context across every tier and process boundary in the standard format of the transport (HTTP: W3C traceparent, tracestate for vendor data); put trace and span ids in every log record; tag every event of one user interaction with a shared correlation id (the trace id serves); stamp client error and real-user events with the release version and the trace or request id. Outcome: one request can be reconstructed from browser to database, and a browser error joins its server logs.
2. Grounds: propagation (L199, L1164; REG-122, REG-1102); ids in logs and shared correlation (L1165, L1167; REG-1089, REG-1103); client stamp (L1253; REG-1141, inferred). One outcome, not competing positions.
3. Positions: P1 standard propagation. P2 ids everywhere.
4. Rejected: per-vendor proprietary headers (traces from different vendors do not correlate; best only inside a closed single-vendor system, inferred). Correlation by timestamp matching (best never as primary).
5. Context: none.
6. Certainty: grounded for P1 and ids in logs; inferred for the client stamp.
7. Flags: none.
Constraints: MUST propagate context at every boundary; MUST put trace and span ids in every log record. Links: Related TELEMETRY.5; TRANSVERSE.PRIVACY holds the rule on personal data in the propagated context (L1171, one location); stack pointers L199, L1164 (HTTP).

### OPERATION.TELEMETRY.5 Trace Sampling

Intent: whether traces are sampled and where the decision is made.
1. Decision: Decide sampling explicitly. Keep every trace while volume is low, metrics are aggregate-only or retention obligations apply; when volume forces sampling, head sampling (simple, cheap) suits healthy, predictable traffic; where rare error and slow traces must all be kept, sample at the tail (or a hybrid), accepting a stateful, heavier pipeline. At a public boundary never continue the sampling decision of an untrusted caller blindly. Outcome: the trace needed in an incident exists, and tracing cost cannot be forced up by outsiders.
2. Grounds: the three forms and their conditions (L200; REG-119, REG-141, REG-237, contested; REG-119 calls tail sampling almost always necessary in larger systems and a hybrid common); start with head, add tail with volume (L1169, inferred); untrusted caller (L1170; REG-122). The volume hint of about 1,000 traces per second is one documentation's illustration, not adopted as a threshold.
3. Positions: P1 head. P2 tail. P3 none. P4 head then tail. P5 distrust the caller's decision.
4. Rejected: head sampling where every error trace must be kept (cannot guarantee it; best under healthy predictable traffic). Tail sampling where the team cannot run the infrastructure (best when it can). No sampling at high volume (cost; best at low volume or under retention obligation).
5. Context: trace volume, rarity of errors that must be kept, retention obligations, capacity to run the tail pipeline (L200).
6. Certainty: grounded for forms and conditions; inferred for the ladder order; grounded for P5 (one source).
7. Flags: none.
Constraints: MUST state the sampling rule; MUST NOT honour an untrusted caller's sampling flag at a public boundary unexamined. Links: Related TELEMETRY.6 (cost); stack pointer L1170 (HTTP).

### OPERATION.TELEMETRY.6 Telemetry Cost

Intent: how the volume and cardinality of telemetry are bounded as a cost.
1. Decision: Treat telemetry volume and cardinality as a designed cost: keep metric label cardinality bounded (no unbounded values such as user ids; per-entity detail goes to logs or traces), filter low-value telemetry and coarsen detail with a stated loss of granularity, and instrument broadly because the bound is on labels, not on metrics. Each service should have a stated bound on volume, series count and retention, reviewed when it grows (a recommendation, inferred: no normative source). Outcome: telemetry cost is predictable and does not silently decide what can be observed.
2. Grounds: cost to design (L456; REG-119, REG-235, REG-237, consensus); bounded labels (L457; REG-235, REG-237); filtering (L458; REG-237, single vendor); broad instrumentation, benchmark only the hottest code (L459; REG-235); the ledger's tension between breadth and cardinality is resolved in REG-235 by bounding labels. The explicit per-service budget (L460) has no normative source: adopted as the cost counterpart of the objective, inferred.
3. Positions: P1 cost as design. P2 bounded labels. P3 filtering. P4 instrument broadly. P5 explicit budget.
4. Rejected: unbounded labels (best never). Dropping instrumentation instead of bounding labels (loses signal; best only on the hottest code paths, where the numbers are a tool's own). A fixed budget with no review (best never).
5. Context: none.
6. Certainty: grounded for P1 to P4; inferred for P5 (open: no source treats telemetry cost as a governed budget).
7. Flags: none.
Constraints: MUST bound label cardinality; SHOULD state a volume or series bound per service. Links: Related TELEMETRY.5; stack pointers L457-L459 (Prometheus-style numbers are that tool's).

### OPERATION.TELEMETRY.7 Vantage Points

Intent: from where the system is observed: inside, outside and from real users.
1. Decision: Observation combines internal measurement with external probing of real customer routes on a schedule from several vantage points (payload validated, latency kept as a time series, credentials secured), and real-user measurement for experienced performance. Outcome: a failure is seen from where it hurts, including failures that never reached the service and emit no signal of their own.
2. Grounds: white-box and black-box together (L189, L1176; REG-124, REG-131); synthetic and real-user together, real-user part inferred from T4 (L453, L454; REG-131, REG-236, REG-243). Split out of the former TELEMETRY.1 (cross-unit line X12), grounds unchanged.
3. Positions: P1 white-box plus black-box. P2 synthetic plus real-user.
4. Rejected: White-box only (cannot see what never reached the service; best never alone). Synthetic only (does not measure experienced performance; best only where real-user data cannot be collected).
5. Context: none.
6. Certainty: grounded for P1 and for synthetic probing; inferred for real-user measurement (T4 only).
7. Flags: none.
Constraints: MUST have a probe from outside for each critical user route; MUST secure probe credentials. Links: Related TELEMETRY.1; stack pointer L454 (managed canaries).

### OPERATION.TELEMETRY.8 Scheduled Work Signals

Intent: how scheduled and derived-data work is watched, since it is not request-driven and fails silently.
1. Decision: Scheduled and derived-data work is monitored on four signals: duration against a documented expectation, any failure, backlog (queue size and age of the oldest entry), and missed runs (not run within twice the interval); a job wraps errors so it logs and re-raises, so the scheduler records the failure. Outcome: a job that did not run, ran too long or failed is noticed, including failures that emit no signal of their own.
2. Grounds: the maintainer's four job signals (L313; REG-181, not citable): public golden signals differ in kind (jobs are not request-driven, so backlog and missed runs have no golden-signal counterpart), so the maintainer practice is the best for scheduled work and does not compete with the golden signals of TELEMETRY.1. Split out of the former TELEMETRY.1 (cross-unit line X12). The job-design habits of L313 (short, idempotent, off-peak, non-overlapping, named) belong to CONSTRUCTION.PARADIGM; they appear here only as far as they make the four signals meaningful.
3. Positions: P1 four job signals (maintainer).
4. Rejected: Treating a completed job as success with no duration, backlog or missed-run signal (best never).
5. Context: none.
6. Certainty: grounded (a single maintainer source; public practice agrees in direction).
7. Flags: none.
Constraints: MUST monitor scheduled work on duration, failure, backlog and missed runs. Links: Required by ASSURANCE.DATA_INTEGRITY.4 and by CONSTRUCTION.PARADIGM.2 (monitoring of scheduled work); applied by RECOVERY.6 (backup and restore jobs); related TELEMETRY.1.

## OPERATION.INCIDENTS Incidents

Intent: how an incident is declared, run and learned from, and how on-call load is bounded.
1. Decision: Incidents are declared on written conditions, run by named roles, learned from by blameless review with tracked actions, and the human cost of operating is bounded and measured. Outcome: an incident is handled at low cost, repeated less, and the people who handle it can sustain it.
2. Grounds: roll-up of INCIDENTS.1 to .3.
3.-4. See children.
5. Context: see children.
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.AVAILABILITY.5 and ASSURANCE.SECURITY.7 (defects change the process); index only here.

### OPERATION.INCIDENTS.1 Declaring and Running an Incident

Intent: on what conditions an incident is declared, who does what while it runs, and how the process is prepared.
1. Decision: Declare an incident on clear written conditions (a second team is needed, the problem is customer-visible, it is unresolved after an hour of focused analysis) and make declaring cheap. Run a major incident with named roles (commander, operations, communications, planning or scribe): the commander keeps a live incident document and only the operations lead and the team they direct change the system. Severity levels and the response each gets are defined before an incident, rehearsed until routine, and command is handed over explicitly. Outcome: response is fast, shared and coordinated, and changes to the system during an incident come from one named group.
2. Grounds: roles (L202; REG-127, REG-142, consensus); declaration (L203; REG-127, "cheap" inferred); severity, rehearsal and handover (L204; REG-127, REG-142).
3. Positions: P1 named roles. P2 low-bar written declaration. P3 high bar for severe events only (unsourced). P4 severities defined and rehearsed.
4. Rejected: a high declaration bar (P3): best never as a declaration rule (unsourced; REG-127 prefers early activation to delay); in a tiny team the process cost is cut by scaling the response (one person holds several roles, a shorter incident document), not by raising the bar. Declaring by individual judgment in the moment (best never: delays the second team).
5. Context: team size: in a very small team one person may hold several roles; the written conditions and the rule on who may change the system stay.
6. Certainty: grounded for roles, written conditions, severities; inferred for "cheap"; open for the high-bar position.
7. Flags: none.
Constraints: MUST write the declaration conditions; MUST name roles, and who may change the system during an incident, forbidding changes from anyone else; MUST rehearse. Links: Related RECOVERY.6 (roles in a recovery, L1113: see L202, L204).

### OPERATION.INCIDENTS.2 Learning From Incidents

Intent: how incidents are reviewed so that they change the system, and how that ties into risk management.
1. Decision: Write a blameless postmortem for every significant incident whether or not it paged, on written triggers (user-visible downtime, data loss, manual intervention, slow resolution, monitoring failure, and the budget-consumption level of RELIABILITY.3). Every action item has an owner, a priority and a tracker entry, is measurable and preventative, is published within days, and closeout is checked and rewarded, not only writing. Incident response is tied to the organisation's risk management so lessons reach safeguards and detection as soon as identified, aiming to reduce both the number and impact of incidents. Outcome: each incident changes the system and the next one is rarer or smaller.
2. Grounds: blameless with triggers (L205; REG-113, REG-126, REG-135, consensus); action items (L206; REG-135); risk management integration (L209, L1148; REG-123, REG-1082: same claim twice, L209 body unread so grounded at abstract level).
3. Positions: P1 blameless postmortems on triggers. P2 owned, tracked actions. P3 integration with risk management.
4. Rejected: postmortems only for paged incidents (misses silent failures and monitoring failures; best never). Postmortems without tracked actions (best never). Blame-based review (best never; REG-135 argues the reverse).
5. Context: none.
6. Certainty: grounded for P1 and P2; grounded at abstract level for P3.
7. Flags: none.
Constraints: MUST set written postmortem triggers; MUST track every action with an owner; MUST feed findings into detection and safeguards. Links: Requires RELIABILITY.3 (budget trigger); related ASSURANCE.SECURITY.7 (fix, change the process, preclude the class), TRANSVERSE.SECURITY_MONITORING.

### OPERATION.INCIDENTS.3 On-Call and Toil Load

Intent: how the human cost of operating the system is bounded.
1. Decision: Bound the human cost of operating with stated, measured limits and keep them under review: operational work (toil) at most half of an engineer's time, on-call about a quarter of time and about two incidents per twelve-hour shift, alert-to-incident ratio near one to one, a rotation sized to meet these and so that every engineer of the rotation is on call often enough to stay familiar with production (about once or twice a quarter in the source's model). Where developers own operations in a small team, the team sets its own limit with the same outcome and records it. Outcome: operating the system does not consume the team that must also improve it.
2. Grounds: limits (L207; REG-113, REG-129, REG-130, majority); rotation size (L452; REG-130, single T2: single-site 24/7 needs at least eight engineers in that model). The numbers are from dedicated teams of six to eight or more per site.
3. Positions: P1 caps and ratio (cognitive load, retention). P2 size the rotation. P3 team-set limit for small teams (inferred).
4. Rejected: no stated limit (best never). The numbers as universal thresholds for small teams (best only for dedicated rotations; for a small team the principle is a stated, measured limit, inferred).
5. Context: dedicated rotation or developers own operations (L207, L452).
6. Certainty: grounded for the numbers as that model's; inferred for small teams.
7. Flags: none.
Constraints: MUST state the load limits and measure against them. Links: Related ALERTING.1 (ratio).

## OPERATION.CAPACITY Capacity

Intent: how capacity is planned, headroom decided and storage health kept.
1. Decision: Capacity is planned in resources before predictable change, headroom is decided explicitly against a measured breaking point, and the data store is kept healthy. Outcome: the system does not run out of resources unannounced.
2. Grounds: roll-up of CAPACITY.1 to .3.
3.-4. See children.
5. Context: see children.
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.PERFORMANCE.2 (consumes the breaking point); index only here.

### OPERATION.CAPACITY.1 Planning Method

Intent: when capacity is planned and in what units and from what inputs.
1. Decision: Plan capacity before any predicted change in usage (design, launch, campaign, seasonal peak, feature release) and periodically, from history for existing workloads and from pilots, expert judgment and external data for new ones. Model it directly in resources (CPU, memory, bandwidth, storage), not requests per second, because query costs differ widely; derive the resource proposal from requirements and iterate designs through scaling and failure domains, discarding a design a reliability requirement defeats. With many services and frequent change, hold declared requirements from which allocations are computed; for a small team a spreadsheet or dashboard forecast suffices. Outcome: capacity is ready for the change that was foreseen and its basis is explicit.
2. Grounds: timing and inputs (L436; REG-217, REG-221, REG-227, consensus); resource units (L437; REG-220, REG-227); requirements-derived (L438; REG-224, single T2); declared requirements versus spreadsheet (L441; REG-221, REG-227, one organisation's scale; the small-team case inferred).
3. Positions: P1 plan before change and periodically. P2 resources, not request rate. P3 derive from requirements. P4 declared requirements (many services). P5 spreadsheet or dashboard (small team).
4. Rejected: request-rate models alone (query costs differ; best only where cost per request is uniform, inferred). Declared requirements for a few services (overhead; best at scale). Spreadsheets across many fast-changing services (brittle; best for small teams).
5. Context: number of services and change frequency (L441).
6. Certainty: grounded for P1 and P2; grounded on a single T2 for P3; grounded and inferred for P4 and P5.
7. Flags: none.
Constraints: MUST plan before predicted change; MUST express capacity in resources. Links: Related ASSURANCE.PERFORMANCE.2.

### OPERATION.CAPACITY.2 Headroom and Overload

Intent: how much spare capacity is held and what protects against what planning cannot predict.
1. Decision: Decide headroom explicitly, from the tested breaking point and its early-warning metrics, counting the scaling lag between trigger and new capacity and the capacity of the failover environment; pair planning with load tests and defined overload behaviour, because planning lowers the chance of cascading failure but cannot protect against infrastructure loss, partitions or unexpected spikes. Pre-provision for peak and failover where peaks are hard, scale-up is slow or the system is critical; autoscale within tested limits where load varies and scale-up is fast. Outcome: spare capacity is a stated number with a reason, and overload degrades before it fails.
2. Grounds: pairing with load tests and overload behaviour (L439; REG-203, REG-225, consensus); headroom form (L440; REG-227, REG-228, contested, conditions stated by the row; neither source fixes a number, open).
3. Positions: P1 pair with load tests and overload behaviour. P2 pre-provision (reliability, reversibility). P3 autoscale with tested limits (cost).
4. Rejected: autoscaling with untested limits (best never). Pre-provisioning everything for a variable load with fast scale-up (cost; best for hard peaks). No stated headroom (best never).
5. Context: load variability, scale-up time, criticality (L440).
6. Certainty: grounded for P1; grounded for the conditions; open for any numeric headroom.
7. Flags: none.
Constraints: MUST derive headroom from a tested breaking point; MUST count scaling lag and failover capacity; MUST test autoscale limits. Links: Realizes ASSURANCE.PERFORMANCE.2 and ASSURANCE.AVAILABILITY.1 (overload behaviour, J4).

### OPERATION.CAPACITY.3 Storage Health

Intent: how index and table health of the database store is kept as operational upkeep.
1. Decision: Keep storage healthy by routine: find indexes that are never used from the engine's usage counters and drop them, watch index and table bloat, and rebuild without blocking writes. Outcome: the store does not degrade through dead indexes and bloat.
2. Grounds: maintainer practice (L317; REG-181, not citable); the ledger reads public practice as agreeing. The practice is best here: it is cheap, measured and reversible by recreating an index. Caveats inferred, not in the row: the observation window must span the longest workload cycle, and an index that backs a constraint is kept.
3. Positions: P1 maintainer practice.
4. Rejected: keeping every index "just in case" (write cost and bloat; best never). Dropping on a short window (best never).
5. Context: none.
6. Certainty: grounded as a single maintainer source with public agreement; the caveats are inferred.
7. Flags: none.
Constraints: MUST (inferred: dropping an index that a monthly workload uses costs far more than waiting one full cycle) drop unused indexes only on usage evidence covering a full workload cycle; MUST rebuild without blocking writes. Links: stack pointer L317 (PostgreSQL).

## OPERATION.READINESS Operational Readiness

Intent: what must hold before a workload is launched and how that review is kept current.
1. Decision: A workload is launched only after a readiness review that shows its team can operate it, and the review is kept true over the workload's life. Outcome: what launches is operable.
2. Grounds: roll-up of READINESS.1 to .3.
3.-4. See children.
5. Context: see .2.
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.AVAILABILITY (failure modes, recovery proof); index only here.

### OPERATION.READINESS.1 Launch Gate and Checklist

Intent: what a workload must show before launch and how the checklist is built.
1. Decision: Verify readiness before launch against a checklist covering architecture, capacity, failure modes, monitoring, emergency response, change management and rollout, and do not launch a workload whose team cannot operate it. Build the checklist from your own incidents and past launch failures, with concrete, achievable items; start short (about thirty items) and tier it by risk, with a fast path for low-risk launches. Outcome: a launch fails the gate for a reason the team has seen, not for a generic one.
2. Grounds: gate (L443; REG-217, REG-218, REG-219, REG-231, consensus); checklist construction (L445; REG-218, REG-231, REG-232).
3. Positions: P1 gate with coverage list. P2 checklist from own history, short, tiered.
4. Rejected: a generic long checklist (items nobody can satisfy; best never as a start). One bar for all launches (best never: slows low-risk launches without safety gain).
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST block launch of a workload whose team cannot operate it; MUST cover monitoring, failure modes, emergency response and rollout. Links: Related CAPACITY, RECOVERY.1; CHANGE_FLOW.RELEASE.

### OPERATION.READINESS.2 Who Performs the Review

Intent: whether readiness is judged by an independent team or certified by the owning team.
1. Decision: The review must be a trustworthy judgment that the workload is operable. For critical services, and wherever ownership passes to a separate operations team, it is performed by an independent reviewer who examines the service and negotiates improvements, with the capacity to review every service that needs it; where many teams launch services and the culture is mature and sponsored, the owning team certifies against a self-service checklist. Outcome: the party that judges readiness has the knowledge and the standing to say not yet, scaled to the cost of being wrong.
2. Grounds: independent (REG-218, REG-219) and self-service (REG-231, REG-232), contested (L444); the conditions are the row's own. No evidence of relative effectiveness was read (open), so the criticality condition rests on the cost-of-error argument.
3. Positions: P1 independent reviewing team (control, quality, knowledge transfer). P2 self-service certification (delivery speed, scalability).
4. Rejected: independent review of every launch with too few reviewers (becomes the bottleneck; best only when reviewer capacity matches service count). Self-certification for critical services or in an immature culture (best never there).
5. Context: number of teams, criticality, culture, sponsorship (L444).
6. Certainty: inferred (no effectiveness evidence for either form).
7. Flags: none.
Constraints: MUST name who can block a launch. Links: Related READINESS.1.

### OPERATION.READINESS.3 Keeping the Review Current

Intent: how the review stays true over the workload's life and how repeated findings become defaults.
1. Decision: Re-run the review over the workload's life, a subset on a regular cadence, to catch drift and add lessons; convert findings that repeat into automated guardrails and defaults so they stop depending on the review. Outcome: the workload stays operable as it changes, and the review shrinks as defaults absorb it.
2. Grounds: periodic subset (L446; REG-231, single T1); guardrails (L447; REG-218, REG-231; examples are one vendor's services).
3. Positions: P1 periodic re-review. P2 guardrails and defaults.
4. Rejected: a one-off launch review (drift goes unseen; best never for a changing workload). Manual review of the same finding forever (best never).
5. Context: none.
6. Certainty: grounded; the cadence is open (no source fixes it).
7. Flags: none.
Constraints: MUST re-run a subset of the review on a cadence; MUST convert repeated findings into guardrails. Links: Related RECOVERY.6 (plan upkeep), RUNBOOKS.1.

## OPERATION.RUNBOOKS Runbooks and Playbooks

Intent: how operating procedures are written, owned, validated and automated.
1. Decision: Operating procedures exist as owned, validated documents, split by purpose, and move toward automation. Outcome: a responder who did not write the procedure can follow it under stress.
2. Grounds: roll-up of RUNBOOKS.1 and .2.
3.-4. See children.
5. Context: none.
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: DOCS_SYNC.3 (J3) applies to every document here; index only here.

### OPERATION.RUNBOOKS.1 Form, Ownership and Validation

Intent: what a procedure document contains, who owns it, how it is proved usable, and how investigation differs from mitigation.
1. Decision: Keep each runbook as a versioned, step-by-step document with an owner, required tools and permissions, error handling and escalation, validated by having another team member run it and updated through change management. Keep playbooks (investigate and scope an incident) separate from runbooks (mitigate a known cause), link the playbook from the alert, and give each an escalation path for an unknown cause. Outcome: a procedure was proved usable by someone other than its author before it was needed.
2. Grounds: runbook form (L448; REG-222, REG-233, single T1 consistent with REG-222); playbook split (L450; REG-223, REG-234, consensus). Owner, date and review schedule are the settled DOCS_SYNC.3 rule, applied here, not restated.
3. Positions: P1 runbook form and validation. P2 playbook versus runbook.
4. Rejected: an unvalidated runbook (best never; the author's own read proves nothing). One undifferentiated document for investigation and mitigation (best never: the two need different escalation).
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST have another person run each runbook before it is relied on; MUST link the playbook from its alert. Links: Related ALERTING.1, RECOVERY.6 (L1111), DOCS_SYNC.3.

### OPERATION.RUNBOOKS.2 Automation

Intent: whether and in what order procedures are turned into scripts and automatic remediation.
1. Decision: Mature runbooks and playbooks from text toward scripts and then automatic remediation, starting with short, frequently used, low-risk ones; a script is validated and exercised like any procedure before it runs unattended (inferred). Outcome: routine work leaves the human path in order of safety and payoff.
2. Grounds: L449 (REG-233, REG-234, single vendor); ALERTING.1 states the matching rule for pages.
3. Positions: P1 staged automation.
4. Rejected: automating a long, rare or high-risk procedure first (best never: failure cost exceeds payoff). Never automating (best never for frequent routine work).
5. Context: none.
6. Certainty: grounded on a single vendor; open: cost and risk of automating a wrong runbook.
7. Flags: none.
Constraints: MUST start with short, frequent, low-risk procedures. Links: Related ALERTING.1.

## OPERATION.RECOVERY Backup, Restore and Disaster Recovery

Intent: how backups are designed and protected, objectives set, strategy chosen and failover and failback carried out.
1. Decision: Recovery is designed backward from stated recovery objectives per workload: backups that cannot be lost to the failure or attacker that threatens production, a strategy and a failover rule chosen by tier against cost, a recovery that does not depend on what failed, and an owner and plan kept current. Outcome: the system can be restored within its objectives, and the proof that it can (ASSURANCE.AVAILABILITY.4 and .5) has stated criteria to test against.
2. Grounds: roll-up of RECOVERY.1 to .6.
3.-4. See children.
5. Context: see .3 (threat model), .4 (objectives).
6. Certainty: inferred (roll-up).
7. Flags: none.
Constraints: children's MUSTs. Links: Realizes ASSURANCE.AVAILABILITY (holds the proof; this node holds the practice, MD-03); required by ASSURANCE.DATA_INTEGRITY.3 (second layer: backups); related TRANSVERSE.PRIVACY.

### OPERATION.RECOVERY.1 Recovery Objectives

Intent: how tolerable downtime and data loss are defined, per workload, before any mechanism is chosen.
1. Decision: Set a recovery time objective and a recovery point objective per workload or data class from the impact of downtime and data loss, grouped in criticality tiers; never arbitrary, zero or stricter than needed, since cost and complexity rise as the objective shortens. Make a workload's objectives compatible with those of its dependencies and dependants (derived data inherits the recovery point of its sources). Define what counts as a disaster, a major disruption and a small incident by user and business impact, and build the thresholds into monitoring so recovery starts on criteria. State data recovery (how much may be lost, whether intact) and service recovery (how fast it runs) as separate objectives: a data disaster has a recovery time above zero and a recovery point before its discovery even where failover is near instant. Outcome: every later recovery choice and every restore test has a stated target.
2. Grounds: L1080 (REG-1054, REG-1059, REG-1064, REG-1065); L1081 (REG-1054, REG-1055, REG-1059, REG-1065); L1082 (REG-1054, one source, none disagrees); L1083 (REG-1060, REG-1064); L1084 (REG-1051, REG-1055, REG-250; the two-objective framing inferred). Consensus; the five are nested, not competing.
3. Positions: P1 per workload and tier. P2 no excessive objectives. P3 compatible with dependencies. P4 impact-defined thresholds in monitoring. P5 separate data and service recovery.
4. Rejected: one organisation-wide objective (over- or under-protects; best never). An objective of zero (cost; best never). Objectives set by the mechanism available instead of impact (best never).
5. Context: none.
6. Certainty: grounded; P3 single-source, P5 framing inferred.
7. Flags: none.
Constraints: MUST set RTO and RPO per workload or data class; MUST state data and service recovery separately; MUST derive from impact. Links: Related RELIABILITY.2 (L1081: see L174); required by RECOVERY.4; criteria for ASSURANCE.AVAILABILITY.4.

### OPERATION.RECOVERY.2 Backup Scope and Design

Intent: what is backed up, how often, with which capability, and how platform state is covered; what to verify of a rented service's backups is held in OWNERSHIP.SERVICES.
1. Decision: Replication and redundancy are availability measures, not recovery: keep versioned or point-in-time copies, because replication propagates damage. Classify all data sources and back up what cannot be recreated; for data reproducible from other sources, define and test the reproduction path instead, provided it meets the recovery time objective. Back up everything needed to rebuild the service (configuration, infrastructure definitions, code and images, system information, recovery documentation), and cryptographic keys with the information to use them on independent storage separate from the encrypted data, decided per key type. Choose frequency from the recovery point, locality from the recovery time, and provide point-in-time recovery where corruption may be found late; where a database needs it, use continuous archiving of the transaction log with base backups (a logical dump alone cannot). Retention is tiered by age (recent copies close for fast restore, older copies on cheaper, more distant storage, L1092); the oldest copy is kept at least as long as corruption may go undetected (detection, ASSURANCE.DATA_INTEGRITY.5) and as legal retention requires, and no longer than the periods of TRANSVERSE.PRIVACY.2 allow; no row gives a number. Where cluster or platform state is the source of truth, back it up explicitly and test its restore: the platform's own availability does not replace it. Outcome: whatever is lost can be restored to the objective's point from copies that exist.
2. Grounds: L1079 (REG-1051, REG-1055, REG-250); L1085 (REG-1052, REG-1054); L1086 (REG-1051, REG-1061, REG-1062); L1091 (REG-1068, one source); L1092 (retention tiered by age, cross-unit line X8); L1093 and L1094 (REG-1051, REG-1052, REG-1066, REG-250); L1118 (REG-1051, REG-1071, REG-250). Consensus; the seven positions cover different scopes.
3. Positions: P1 versioned copies, not replication. P2 classify, back up the irreplaceable. P3 test a reproduction path instead. P4 back up the rebuild set. P5 keys separately. P6 frequency, locality, point-in-time. P7 platform state.
4. Rejected: relying on replication as backup (propagates damage; best never). Backing up reproducible data with no tested path (best never skipping; skipping is best only with the tested path and RTO met). A logical dump alone where point-in-time is needed (cannot provide it).
5. Context: none.
6. Certainty: grounded; "HA does not replace it" for platform state inferred.
7. Flags: none.
Constraints: MUST keep point-in-time or versioned copies; MUST test the reproduction path where backup is skipped; MUST back up keys separately from the data they protect; MUST back up platform state where it is the source of truth. Links: Related OWNERSHIP.SERVICES (L1112 held there); TRANSVERSE.PRIVACY.2 (periods), .3 (erasure in backups); ASSURANCE.DATA_INTEGRITY.3 (points here for retention); stack pointers L1094 (PostgreSQL), L1118 (Kubernetes).

### OPERATION.RECOVERY.3 Backup Protection and Isolation

Intent: how backups are kept out of reach of the failure and the attacker that threaten production.
1. Decision: Keep at least one backup copy outside the failure and attack domain of production, and put an attacker who already holds production credentials in the backup threat model: a backup reachable with production credentials is not independent. Choose the form of isolation by the stated threat and the restore-speed requirement, and state who can delete or shorten retention: a separate account, region or provider for vendor- or account-level loss; immutable (write-once) retention enforced by the platform where restores must be fast and the platform account is itself protected; an offline or air-gapped copy where the threat model includes a destructive adversary and the restore time allows. Baseline several copies on more than one kind of storage with one off-site (3-2-1), adding an immutable or offline copy and a verified restore (3-2-1-1-0) where ransomware or insider deletion is in scope. Backups are encrypted, write and delete rights restricted, and no single credential or person can delete every copy or shorten its retention: deletion needs dual authorisation, or retention is enforced as immutable by the platform. How long copies are kept is held in RECOVERY.2; erasure of personal data in a backup, including a copy locked as immutable (the lock's expiry being its schedule), is held in TRANSVERSE.PRIVACY.3. Outcome: no single incident, fault or compromised credential can destroy the data and every copy of it.
2. Grounds: independence (L1087; REG-1051, REG-1061, REG-1062, REG-1063, REG-1067, REG-250); form by threat (L1088; REG-1051, REG-1062, REG-1063, REG-1067, contested, conditions stated by the row); baseline and extension (L1089; REG-1062, REG-1063, REG-1067, REG-1077 vendor T3, extension inferred); protection (L1090; REG-1061, REG-1062; the outcome of L1090 holds for a team of one, where dual authorisation is impossible, hence the immutable-retention alternative); credential-holding attacker (L1117; REG-1062, REG-1063, REG-1076, percentages T3 not used).
3. Positions: P1 independent copy. P2 offline. P3 immutable. P4 separate account, region or provider. P5 3-2-1. P6 3-2-1-1-0. P7 protect confidentiality, integrity, availability. P8 production-credential attacker.
4. Rejected: any copy reachable with production credentials counted as independent (best never). Offline-only where restores must be fast (best when the adversary is destructive and time allows). Immutability where the platform account is unprotected (best when it is protected). 3-2-1 alone where destructive attack is in scope (best for hardware, site or operator error). Separate provider for every system (cost; best when vendor-level loss is in the threat model).
5. Context: threat model and restore-speed requirement (L1088, L1089).
6. Certainty: grounded for independence, protection and the credential-holding attacker; grounded for 3-2-1; inferred for the 3-2-1-1-0 extension.
7. Flags: none.
Constraints: MUST keep one copy independent of production credentials; MUST state the threat model and who can delete backups or shorten retention; MUST encrypt backups and ensure no single credential or person can delete every copy or shorten its retention (dual authorisation, or platform-enforced immutable retention). Links: Related TRANSVERSE.SECURITY (L1090 boundary), ASSURANCE.SECURITY.6, OWNERSHIP.SERVICES (L359); retention in RECOVERY.2 and ASSURANCE.DATA_INTEGRITY.3, erasure in TRANSVERSE.PRIVACY.3; stack example L1088 (object-storage compliance modes).

### OPERATION.RECOVERY.4 Recovery Strategy, Failover and Failback

Intent: which standby posture each tier gets, who triggers failover, and how the way back is run.
1. Decision: Choose the strategy per tier from the ladder (backup and restore, pilot light, warm standby, active/active) by the objectives against cost and complexity, never a rung stricter than needed. Every recovery path relied on is exercised (ASSURANCE.AVAILABILITY.4, .5). A standby that cannot be exercised realistically is either converted to failover, with both paths carrying traffic continuously, where the objectives justify running everything everywhere (latency, global audience, near-zero recovery time; L1106), or removed, recovery then relying on the tested restore; active/active does not remove the need for backups and a tested data-disaster recovery. A fallback that is neither exercised nor removed is a liability: it must be exercised or removed. Failover is started by a person through an automated push-button procedure where a false alarm costs availability or data; it is automatic on health signals, with trained oversight and tuned thresholds, only where the objective is shorter than a human can meet. Failback is planned as its own process; re-synchronising data stores is the hard part, and the recovery site may be promoted to primary instead. Outcome: each tier's recovery matches its objective at the least cost and complexity, and the path used in a disaster has been used before.
2. Grounds: ladder (L1105; REG-1051, REG-1055, REG-1059, REG-1064, REG-1065; rung boundaries are one vendor's figures, not used); standby versus no-fallback (L1101; REG-1051, REG-1055, REG-1056, REG-1075 T3, fetched in review: convert fallback to failover, exercise both code paths continuously): the sources agree an unexercised path is a liability and differ on exercise versus removal, reconciled by the objective and cost condition (REG-1055: active/active only when business requirements necessitate it); active/active versus warm (L1106; REG-1051, REG-1055); trigger (L1107; REG-1051, REG-1055, REG-1064); failback (L1110; REG-1055, REG-1064).
3. Positions: P1 ladder by tier. P2 standby, rehearsed. P3 production path only. P4 active/active. P5 warm standby. P6 human-started automated failover. P7 automatic failover. P8 separate failback.
4. Rejected: an unexercised standby (best never; P2 requires the rehearsal of ASSURANCE.AVAILABILITY.5). Active/active chosen for resilience alone at its cost (best only under the stated condition). Automatic failover with untuned thresholds (best never). Failback treated as failover reversed (best never).
5. Context: objectives against cost, and recovery time against human response time (L1105, L1107).
6. Certainty: grounded for the ladder, the exercised-path rule and failback; inferred for the reconciliation of standby against single path; grounded for the trigger conditions.
7. Flags: none.
Constraints: MUST choose the rung by tier and objectives; MUST exercise every recovery path relied on, converting to failover or removing a standby that cannot be exercised; MUST state the failover trigger rule; MUST plan failback separately. Links: Requires RECOVERY.1; related ASSURANCE.AVAILABILITY.5.

### OPERATION.RECOVERY.5 Recoverability of Recovery Itself

Intent: how recovery is kept independent of what failed, rebuilt from source, and held to the production baseline.
1. Decision: Make recovery independent of what failed: simple operations that remain available, pre-provisioned capacity, and recovery tooling, runbooks, credentials, certificates, pipelines and contact paths placed where the failure cannot take them away, with offline copies for the worst case. Define infrastructure and environment as code and be able to rebuild from source on a clean machine or account; rebuilding regularly detects drift and is itself a recovery capability. Hold the recovered environment to the production security baseline and address the root cause before recovery starts. The trade-off between hardening recovery-critical systems and the speed of recovery from a non-malicious failure is stated as an explicit decision per system; the default is to accept slower recovery for rare events in return for day-to-day security of those systems. Outcome: recovery does not need what failed, does not reintroduce the failure, and does not weaken security.
2. Grounds: independence (L1108; REG-1051, REG-1057, REG-1062, REG-1064, REG-1074; control-plane vocabulary is one vendor's, principle neutral); rebuild from source (L1109; REG-1051, REG-1062, REG-1072); baseline and root cause (L1116; REG-1064, REG-1065); trade-off (L1115; REG-1074, single T3 large operator; the opposite position is argued in no source read).
3. Positions: P1 independent recovery. P2 rebuild from source. P3 accept slower recovery for security. P4 favour recovery speed. P5 baseline and root cause.
4. Rejected: recovery tooling stored inside the system it recovers (best never). Favouring speed over hardening as the default (unsourced, open; best when the objective cannot be met by the hardened path, then the objective or the design is revisited, inferred). Recovering into a weaker environment and fixing later (best never).
5. Context: none beyond the stated trade-off.
6. Certainty: grounded for P1, P2 and P5; the default toward hardening is inferred (one T3 source states and accepts the trade-off, REG-1074); the stated per-system decision is the rule.
7. Flags: none.
Constraints: MUST keep recovery tooling and credentials outside the failure domain; MUST be able to rebuild from source; MUST state the hardening-against-speed decision; MUST hold the recovered environment to the production baseline. Links: Related CHANGE_FLOW (infrastructure as code), TRANSVERSE.SECURITY; ASSURANCE.AVAILABILITY.4 (restore path independent of schema tooling).

### OPERATION.RECOVERY.6 Ownership, Monitoring, Roles and Plan Upkeep

Intent: who owns durability, how backup jobs are watched, who does what in a recovery, and how the plan stays current.
1. Decision: Name an owner for data durability, including regular testing of backup and restore: a procedure nobody owns is not tested. Monitor backup and restore jobs and route failure alerts over a path that is itself verified: an undelivered failure notice is no monitoring. Keep the recovery plan, runbooks and contact lists current, reviewed periodically and on every change to the system or the organisation and after every test or incident, and kept accessible to the team when production is down. Assign recovery roles ahead of time (who declares, executes, communicates, closes), prepare channels and templates, and declare the end of recovery by stated criteria once restored assets are verified. Outcome: someone answers for recovery, its failure is noticed, the plan matches the system, and the people know their part.
2. Grounds: monitoring (L1095; REG-1073, REG-250, inferred from a case); owner (L1096; REG-1053, REG-1073, inferred, one case study); upkeep (L1111; REG-1055, REG-1059, REG-1064); roles and end criteria (L1113; REG-1059, REG-1060, REG-1064). Owner, date and review for the documents are the settled DOCS_SYNC.3 rule, applied.
3. Positions: P1 monitor the jobs and the alert path. P2 owner. P3 plan upkeep. P4 roles and end criteria.
4. Rejected: counting a completed backup job as success (stated in ASSURANCE.AVAILABILITY.4, pointer only). Plan review on a calendar only (misses changes; best never alone). Roles assigned at the time of a recovery (best never).
5. Context: none.
6. Certainty: grounded for P3 and P4; inferred for P1 and P2.
7. Flags: none.
Constraints: MUST name the owner of durability; MUST verify the alert path of backup failures; MUST review the plan on every change to the system, the organisation, a test or an incident; MUST assign recovery roles beforehand. Links: Applies TELEMETRY.8 (four job signals: backup and restore jobs are scheduled work); related INCIDENTS.1 (L1113: see L202, L204), RUNBOOKS.1 (L1111: see L448), ASSURANCE.AVAILABILITY.4 (regular restore testing), DOCS_SYNC.3.

## OPERATION.FEEDBACK Feedback into Development

Intent: how production signals about delivery return to the people who change the system.
1. Decision: Track failed-deployment recovery time and change failure rate as production feedback on delivery, at the level of one service, shared across development and operations, and never as targets. Outcome: the signal stays honest and reaches the people who change the system.
2. Grounds: L208 (REG-093, DORA, majority). The warning that metric targets invite gaming is the argument; the contrary view (set targets to drive improvement) is argued in no source read. The reliability objective of RELIABILITY is a target on user experience, not on these delivery measures, so the two do not conflict.
3. Positions: P1 feedback, not targets (honest signal). P2 targets to drive improvement (open, unsourced).
4. Rejected: targets on these measures (invite gaming; best never on evidence read, condition unknown, open).
5. Context: none.
6. Certainty: grounded on one source; open for the contrary view.
7. Flags: none.
Constraints: MUST measure per service and share across development and operations; MUST NOT set targets on these measures. Links: Related CHANGE_FLOW.MEASURE (L208 boundary, see L169).

---

## Flags raised

All flags below are settled by the final pass (see Final pass applied); none remains open. Kept as history.

- F1 (RELIABILITY.2): settled PERFORMANCE.1 says test targets are "never from current performance" (L420, best never); L179 allows a provisional objective from measurable history with a review. Read as compatible (a provisional start is never final), but PERFORMANCE.1's wording is stricter than its sibling row. No settled decision is contested; the Opus pass may align the wording.
- F2 (TELEMETRY.1): eleven rows on seven subjects; may split in the graph build. The job-design habits of L313 (short, idempotent, off-peak, non-overlapping, named) are left to CONSTRUCTION.PARADIGM and kept here only as far as they make the four signals meaningful; placement unsettled.
- F3 (TELEMETRY.2): the storage model rests on argued, not measured, evidence and a vendor T3 source; decided by condition.
- F4 (TELEMETRY.6): the per-service telemetry bound has no normative source; adopted as inferred.
- F5 (RECOVERY.5): hardening against recovery speed rests on one T3 source and the opposite side is unsourced; decided toward hardening, certainty open.
- F6 (INCIDENTS.3): all numbers are Google-scale for dedicated rotations; small-team treatment inferred.
- F7 (READINESS.2): no source compares independent and self-service review; the criticality condition is an inference from cost of error.
- F8 (RECOVERY.3): the 3-2-1-1-0 extension is vendor-originated (T3) and inferred; the dual-authorisation clause (L1090) sits on a boundary with TRANSVERSE.SECURITY and ASSURANCE.SECURITY.6.
- F9 (RECOVERY.4, CAPACITY.3, CAPACITY node): the reconciliation of standby against single path is inferred; CAPACITY.3 caveats (full-cycle observation window, constraint-backing index) are inferred, not in the row.
- F10 (OPERATION L1): units.md assigns the L1 node to the first unit of a branch and also lists the L1 intents of realization branches for wave 3; the L1 record here is a roll-up the wave-3 pass may replace.
- F11 (TELEMETRY.5): the sampling volume hint (about 1,000 traces per second) is one documentation's illustration and is not adopted as a threshold.

## Review applied

- R-01: applied (INCIDENTS.3 decision: every engineer of the rotation on call often enough to stay familiar, about once or twice a quarter in the source's model).
- R-02: applied (INCIDENTS.1 decision, outcome, context and constraint: the operations lead and the team they direct; no "single operator" or "single-writer").
- R-03: applied (OPERATION L1 decision carries the FEEDBACK clause; header note updated).
- R-04: applied (TELEMETRY.4 MUST NOT on personal data removed; Links point to TRANSVERSE.PRIVACY).
- R-05: applied (RECOVERY.6 rejected restated rule reduced to a pointer to ASSURANCE.AVAILABILITY.4; Links add TELEMETRY.1 four job signals).
- R-06: applied (RELIABILITY Links add Realizes ASSURANCE.AVAILABILITY).
- R-07: applied (RELIABILITY.3 grounds cite REG-134 and REG-128 for the agreement rule; REG-133 kept for the example).
- Flags R-08 to R-18: applied by the final pass (see Final pass applied).

## Final pass applied

Resolutions (J7 section of the final pass):
- R-08 (ALERTING.2): applied. Decision, Rejected and Context replaced as stated (service size dropped; low-traffic remedies added); grounds note the fetched source.
- R-09 / F4 (TELEMETRY.6): applied. Volume or series bound is a recommendation (SHOULD, inferred); MUST bound label cardinality kept.
- R-10 / F9 (RECOVERY.4): applied with one reading. The resolution names "second and fourth sentences", but the fourth sentence of the record is the failover trigger, which the resolution does not touch; the replacement covers the standby and fallback text, so it replaced sentences two and three, and the failover and failback sentences are kept. The clause "active/active does not remove the need for backups and a tested data-disaster recovery" (in a replaced sentence, not contradicted) is kept inside the new text. Constraint and grounds aligned.
- R-11 (INCIDENTS.1): applied. Rejected P3 replaced as stated.
- R-12 / F2 (TELEMETRY.1): applied. First sentence replaced as stated; the split is line X12 below.
- R-13 / F1 (RELIABILITY.2, with ASSURANCE.PERFORMANCE.1): applied through X11; RELIABILITY.2 text unchanged, flag F1 removed.
- R-14 (RELIABILITY.1): applied through X11.
- R-15 (RECOVERY.2): applied through X8.
- R-16 / F5 (RECOVERY.5): applied. Certainty replaced as stated; decision unchanged.
- R-17 / F8 (RECOVERY.3): applied. Dual-authorisation clause and constraint replaced as stated.
- R-18 / F9 (CAPACITY.3): applied. MUST kept, marked inferred.
- Judge flags F3, F6, F7, F10, F11 (closed by the review, confirmed): flags removed from the records; no text change.

Cross-unit lines naming J7:
- X8 (backup retention and erasure): applied. RECOVERY.2 holds the retention clause (tiered by age, oldest copy bounded below by undetected corruption and legal retention and above by TRANSVERSE.PRIVACY.2, no number; L1092 added to grounds). RECOVERY.3 points to RECOVERY.2 for retention and to TRANSVERSE.PRIVACY.3 for erasure, including the immutable lock. The DATA_INTEGRITY.3 and DECOMMISSION.6 pointers belong to J3 and J8, not applied here.
- X11 (percentiles and starting point): applied. RELIABILITY.1 holds the percentile rule and is named as the target of PERFORMANCE.1's pointer; RELIABILITY.2 unchanged. The PERFORMANCE.1 edits belong to J4, not applied here.
- X12 (split of TELEMETRY.1): applied. TELEMETRY.1 keeps service and resource signals; TELEMETRY.7 Vantage Points and TELEMETRY.8 Scheduled Work Signals added with their MUSTs; the L2 TELEMETRY roll-up, header, RECOVERY.6 link and the DATA_INTEGRITY.4 requirement now point to TELEMETRY.8. The pointers inside ASSURANCE.DATA_INTEGRITY.4 and CONSTRUCTION.PARADIGM.2 belong to J3 and J5, not applied here (TELEMETRY.8 Links name both).
- X1 to X7, X9, X10, X13, X14: do not name J7; not applicable.

Nodes added: OPERATION.TELEMETRY.7 Vantage Points; OPERATION.TELEMETRY.8 Scheduled Work Signals.

Maintainer point (ASSURANCE.RULES.4, J2 only): not applicable to J7.

Flags still open: none.
