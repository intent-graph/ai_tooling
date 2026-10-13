# Judged records: unit J4_assurance_runtime

Branch ASSURANCE, L2 nodes PERFORMANCE, AVAILABILITY, ARTIFACT and their 12 L3 nodes (15 nodes, 53 rows). Decisions follow MD-01 (the best, not the average) and MD-02 (outcomes, whoever does the work). Rows are cited by ledger id, sources by register id. Certainty words: grounded, inferred, open. No decision is undecided; flags F1 to F8 are all settled by the review and the final pass and are listed at the end with their outcome. No settled decision is in this unit's inputs (wave 1); none is contested.

---

## ASSURANCE.PERFORMANCE Performance

Intent: which tests, measurements and budgets guarantee that speed and capacity hold under the real workload.
1. Decision: Performance targets come from user need and the SLO, load tests resemble the real workload and run at the stage that matches their cost, every run is compared with a baseline, production supplies what replicas cannot, and no speed claim stands without measurement on the real workload. Outcome: speed and capacity hold under the real workload, and a regression is caught on the change that caused it.
2. Grounds: rolled up from PERFORMANCE.1 to .5; the claim is inferred from the five child decisions, each with its own certainty.
3. Positions: see children.
4. Rejected: see children.
5. Context: see children (criticality, harness stability, replica affordability, client-delivered software).
6. Certainty: inferred (roll-up); the weakest children are .3 (cost and noise argument) and .5 (method transfer).
7. Flags: none.
Constraints: every child's MUST. Links: Realized by OPERATION (alerting, capacity), CHANGE_FLOW.DEPLOY (canary analysis); index only here.

### ASSURANCE.PERFORMANCE.1 Targets and Budgets

Intent: what a performance target is derived from and how it is divided and enforced.
1. Decision: Derive every target from user need and the SLO, state it as a measurable objective with an explicit pass or fail threshold on a percentile (for example p95 under a stated latency; the percentile rule itself is held in OPERATION.RELIABILITY.1), never from current performance as a final value; a provisional start from measured history follows OPERATION.RELIABILITY.2. Where a request crosses layers, split the budget per layer so a failing test names the layer to optimize. Guarantees: a performance test has a verdict that means something to a user.
2. Grounds: L420 (REG-125 T2, REG-226 T1, consensus); L421 (REG-226 T1, single source, practice follows from the layering argument).
3. Positions: P1 targets from user need and SLO (outcome relevance); P2 per-layer budgets (diagnosability); P3 enforced artefact-size and timing budgets in the build (cost of regressions caught early, client-delivered software).
4. Rejected: targets set from current performance as a final value (L420 states it is wrong: it ratifies whatever exists; best never). P3 is not rejected: it is the same decision where the artefact is delivered to a client, see Context.
5. Context: for client-delivered software (web front end pointer, L435; REG-240, T3 single source) add budgets on artefact size and timing metrics enforced in the build, block or optimize the addition when exceeded. Other software: not applicable.
6. Certainty: grounded for P1; grounded but single-source for P2 and P3. P3 is a stack pointer for the JavaScript and web guidelines.
7. Flags: none.
Constraints: MUST state target as threshold on percentile; MUST NOT derive from current performance as a final value; MUST name the layer budget when a layered path is tested.
Links: Refines OPERATION.RELIABILITY (SLO owner; RELIABILITY.1 holds percentiles, RELIABILITY.2 holds the provisional start); L435 pointer to the web guideline.

### ASSURANCE.PERFORMANCE.2 Load Test Design

Intent: what a load test must resemble and which kinds are run so that its result predicts real behaviour.
1. Decision: A load test exercises the whole workload end to end with a representative request mix and realistic data (synthetic or sanitized, including edge cases such as large payloads and high concurrency), in an environment that matches production on the properties that decide the result (compute, scaling, caching, network, dependencies), driven open-loop at a constant arrival rate and run past expected load to the breaking point. Test types are chosen by risk (smoke, average load, stress, spike, soak, breakpoint), starting with basic load tests and widening as risk and experience grow; when overload is tested the result is read as goodput, not server throughput. Guarantees: a result predicts real behaviour, including how and where the system fails.
2. Grounds: L423 (REG-228, REG-229, REG-230, T1, consensus); L424 (REG-226, REG-229, REG-230 T1, REG-104 T2); L425 (REG-203, REG-225, REG-229, REG-230, REG-238); L426 (REG-226, REG-238 T1); L422 (REG-226, REG-229, REG-203); L430 (REG-239): a closed-loop generator waits on a stalled response and stops sending, so it records fewer slow samples than real users would; this is a mechanism, not a taste, so it is a validity condition of the measurement; L431 (REG-225 T2).
3. Positions: P1 production-identical environment (fidelity); P2 scaled-down (cost); P3 test in production (realism, user impact; judged in PERFORMANCE.4); P4 end to end; P5 representative mix, real vs mocked third parties (realism vs repeatability); P6 to the breaking point; P7 several types by risk; P8 open-loop; P9 goodput.
4. Rejected: isolated-component load tests as the only evidence (P4: they miss the interactions that fail first; best as a diagnostic after the end-to-end result localizes a layer). A small safety factor above expected load as the ceiling (P6: it hides the failure mode and the early-warning metrics). Closed-loop generation without correction (P8: understates tail latency; acceptable only when the generator is known not to stall, which is rare). Server-side throughput alone under overload (P9).
5. Context: (a) Environment: production-identical when the workload is mission-critical or the result gates capacity spend (cloud elasticity lowers the cost); a scaled-down production-like environment when criticality is low and load behaviour is known to scale predictably; record the choice (L422). (b) Third-party calls: include the real dependency when it is critical and the provider permits load tests; stub or mock it when the provider's policy forbids load or to isolate own code, and say which calls were mocked (L424).
6. Certainty: grounded for P4, P5 (mix and data), P6, P7 (T1 consensus); grounded for the fidelity-by-criticality condition (contested between sources, conditions stated by the row); inferred for P8 as a normative rule (one T3 source, but the mechanism is stated); P9 grounded, single T2.
7. Flags: none.
Constraints: MUST test end to end; MUST use a representative mix and realistic data; MUST record the environment fidelity chosen and which third parties were real; MUST report tail latency under an open-loop or corrected generator; MUST know the breaking point and its early-warning metrics.
Links: Requires PERFORMANCE.1 (thresholds); see PERFORMANCE.4 (production tests), OPERATION.CAPACITY (consumes the breaking point).

### ASSURANCE.PERFORMANCE.3 When Tests Run and Baselines

Intent: at which moments performance tests run and against what a result is compared.
1. Decision: Place each test by its cost and noise: a smoke check and a threshold check that is stable and fast gate every change; long and expensive tests (soak, spike, breakpoint, full-scale load) run on a schedule for cost and duration, and a noisy test does not gate until its variance is below the threshold it enforces, before anticipated events and after large changes. Every run is compared with a recorded baseline of normal performance, refreshed after architectural or scaling changes, and slow drift and misconfiguration are caught by regression tests plus production-side configuration checks. Guarantees: a regression is found within one scheduled interval and, for the cheap tier, on the change that caused it.
2. Grounds: L427 (REG-226, REG-230 T1, REG-238 T1; REG-242 T3, read: shared CI runners are too noisy to gate on, a 2.66 percent coefficient of variation gives about a 45 percent false-positive chance at a 2 percent threshold, and the source's remedy is lower-variance infrastructure, not scheduling); L428 (REG-226, REG-230); L108 (REG-051, REG-067 T2); L429 (REG-226 T1). The split follows the placement rule of ASSURANCE.RULES.2 (feedback speed against cost), applied per test type; it is the one the row itself states.
3. Positions: P1 regression tests plus production configuration checks (drift); P2 gate every change (speed of feedback, attribution); P3 scheduled or event-driven (cost, low noise); P4 baseline and comparison; P5 hypothesis validation for high-impact changes.
4. Rejected: gating every change on the full load suite (P2 as the only placement: a noisy or slow signal on every change trains the team to ignore it; best when the harness is stable, low-variance and fast). Scheduled-only (P3 as the only placement: loses attribution to one change; best when tests are long, expensive or noisy, which is the tier it keeps). Hypothesis validation for every change (P5: cost; kept for high-impact changes only).
5. Context: harness variance and test cost move a test between the per-change tier and the scheduled tier (L427); a harness whose variance is below the gating threshold may gate. A change predicted to move performance materially (high impact) is validated as a hypothesis: state the prediction, run the same load test on baseline and variant, compare measured results.
6. Certainty: grounded for the baseline (consensus T1), for regression tests and for the hypothesis method (one T1 source); grounded for the noise rule (REG-242 T3, read); the scheduling of expensive tests is justified by cost and duration (REG-226, REG-238), not by noise.
7. Flags: none (F5 closed by review).
Constraints: MUST compare each run with a baseline; MUST refresh the baseline after architectural or scaling change; MUST NOT gate a change on a signal whose noise exceeds the threshold it enforces (REG-242); MUST check production configuration, not only code.
Links: Requires PERFORMANCE.5 (distribution-aware comparison, L1565); Realized by CHANGE_FLOW.BUILD (pipeline stages); L453 synthetic monitoring held in OPERATION.TELEMETRY.

### ASSURANCE.PERFORMANCE.4 Testing in Production for Performance

Intent: what only production reveals about performance and under which guardrails it is tested there.
1. Decision: Pre-production tests are the base; add controlled production tests for what only production has, except where a faithful replica is affordable and the system is high impact (then pre-production only) (real data, network, third parties, state such as caches, cookies and request affinity). Apply the production-test guardrails of ASSURANCE.AVAILABILITY.3; for load, additionally run off-peak, ramp from a small share of traffic and reserve capacity. Complement synthetic load, which maximizes code coverage but not state coverage, with canary analysis on organic traffic. Guarantees: the realism gap of the replica is closed without exposing more users than the guardrails allow.
2. Grounds: L432 (REG-104 T2, REG-203 T2, REG-226 T1, REG-229 T1); L433 (REG-104 T2, single source, mechanism stated).
3. Positions: P1 pre-production only (user safety, reversibility); P2 controlled production tests (realism); P3 canary on organic traffic (state coverage).
4. Rejected: production tests without the guardrails (the force is realism, the cost is user impact, so the guardrails of AVAILABILITY.3 are the condition of the practice, never optional). Pre-production only is the best when the system is high-impact and a faithful replica exists and is affordable.
5. Context: impact class of the system and affordability of a faithful replica (L432): replica faithful and affordable, high impact: pre-production only; replica unaffordable: controlled production tests.
6. Certainty: grounded (the contested split is resolved by the row's own condition); P3 single-source but mechanism stated.
7. Flags: none.
Constraints: MUST apply the production-test guardrails of AVAILABILITY.3; MUST, for load, run off-peak, ramp from a small share and reserve capacity.
Links: Requires AVAILABILITY.3 (the guardrails every production test shares); held in CHANGE_FLOW.DEPLOY: canary analysis and rollback (L118, moved there); load and locks are transient effects governed by those guardrails, while the durable-data rule (a functional test never runs against production data unless every durable effect is provably undone) is held in ASSURANCE.BEHAVIOUR.7 (L265).

### ASSURANCE.PERFORMANCE.5 Measurement Before Optimization

Intent: that speed is established by measurement of the real workload, never by belief, and how a measurement is made trustworthy.
1. Decision: Optimize only what measurement on the real workload has shown to be critical, prioritizing with field (real-user) data and testing changes with lab data before release. A measurement counts as evidence only when reported as a distribution (percentiles or confidence intervals across several runs, warm-up separated from steady state where warm-up exists, setup varied); a performance belief, including advice about implementation internals, becomes a rule only after such a measurement. Where architecture is hard to change and load is high, also estimate resources and test from design onward, so architectural bottlenecks surface before they are costly. Guarantees: effort goes to what is slow, and a claimed gain is a real one.
2. Grounds: L1563 (origin node intent, no claim of its own; rolled up by L1564 and L1565); L434 and L1178 (REG-241 T3 secondary, REG-138 T3, REG-1105 T1; REG-224 T2, REG-226 T1 for the design-time estimate); L1179 (REG-1105 T1); L1564 (REG-1571 to REG-1577, one T2 body; rule inferred, as its origin says); L1565 (REG-1578, REG-1579 T2, Java and C; transfer inferred); L177 (distributions). Origin: judged in the JavaScript guideline, re-examined here; its position is kept in substance because two independent measurement studies show setup bias can flip conclusions, and dropped as to the JavaScript-specific parts.
3. Positions: P1 measure first, optimize the critical few (delivery speed, cost); P2 estimate from design onward (avoided rework); P3 field data to prioritize, lab data to test; P4 belief becomes rule only by measurement (conflict: restructuring on mechanism alone); P5 distribution-aware measurement.
4. Rejected: optimizing from belief or from the description of a mechanism (P4 conflict: the origin gives no condition under which it is best, and its own source says the studied differences are usually too small to measure; it is the best only when the claimed mechanism is itself confirmed by a measurement on this workload, which makes it P4). Measurement-only with no design-time estimation (P1 alone): best when architecture is cheap to change or load is low.
5. Context: design-time estimation is added when architecture is hard to change and load is high (L434). Warm-up separation applies where the runtime or system has warm-up (compiled-on-demand code, caches, pools); elsewhere report the distribution only.
6. Certainty: grounded for P1 and P3; grounded for the two measurement methods (two T2 sources) with transfer to other runtimes inferred. The rule that a belief about implementation internals becomes a rule only after measurement is an instance of measure before optimising (P1, grounded); the T2 body (REG-1571 to REG-1577) shows the case for internals advice. Warm-up separation is a scope (it applies where warm-up exists), inferred.
7. Flags: none.
Constraints: MUST measure before optimizing; MUST report a distribution, not one number; MUST prioritize by field data where it exists.
Links: Requires (within node) L1565 by L1564; Required by PERFORMANCE.3 (baseline comparison); Related: OPERATION.TELEMETRY (L1177 which signals exist).

---

## ASSURANCE.AVAILABILITY Availability and Recovery

Intent: which design mechanisms and exercised procedures guarantee the system stays available under dependency failure and can be recovered.
1. Decision: Availability is guaranteed by designing a degraded mode and a bounded call for every dependency, and recovery by a restore proven against criteria fixed beforehand and by exercised procedures with measured times; an untested mode, backup or plan is treated as absent. Outcome: the system keeps serving when a dependency fails and can be restored within its objectives, as shown by test.
2. Grounds: rolled up from AVAILABILITY.1 to .5; the shared claim (verified, not assumed) is stated by L032, L1097, L451, L120.
3. to 4. see children.
5. Context: see children.
6. Certainty: inferred (roll-up); .4 grounded, .3 weakest.
7. Flags: none.
Constraints: children's MUSTs.
Links: Index link OPERATION.RECOVERY holds the practice (backup, objectives, strategy, failover); this node holds the proof (MD-03). OPERATION.RELIABILITY and OPERATION.READINESS realize.

### ASSURANCE.AVAILABILITY.1 Tolerating a Degraded Dependency

Intent: that the system keeps serving when a non-essential dependency is slow or down, and that overload degrades before it fails.
1. Decision: Each non-essential dependency has a designed degraded mode (cached or default result, reduced feature), hard dependencies are made soft where possible and kept few, and the system's overload behaviour (reject early when out of quota or capacity, serve degraded responses before errors, and a client that sees much of its recent traffic rejected for quota limits its own outgoing traffic) is defined. Both are exercised regularly, so tolerance is shown, not assumed. Guarantees: one slow or failed non-essential dependency, or a load beyond capacity, reduces service instead of ending it.
2. Grounds: L032 (REG-007 T1, REG-185 T1, REG-203 T2, REG-209 T2; consensus); L442 (REG-220 T2, REG-225 T2, REG-228 T1; consensus). The row places verification here and design in application architecture; this node holds the verification obligation and the design rule in one line.
3. Positions: P1 loose coupling and degraded mode per non-essential dependency; P2 designed and tested overload behaviour, including client-side throttling (REG-220: a client that detects a significant share of recent requests rejected as out of quota self-regulates and caps its outgoing traffic).
4. Rejected: none competes; a client that keeps sending at full rate into quota rejection is rejected (it adds load to an overloaded provider; best never); they are two parts of one outcome (dependency failure, overload). Failing hard on a dependency is the best only for an essential dependency (no degraded mode exists), which then needs the bounds of AVAILABILITY.2.
5. Context: none. Which dependencies are essential is a per-system fact, not a condition on the rule.
6. Certainty: grounded for the degraded mode (REG-007) and overload behaviour; inferred for graceful-degradation detail (as the row says).
7. Flags: none (client retry caps in L442 overlap L333 and L337; stated once in AVAILABILITY.2).
Constraints: MUST define the degraded mode for each non-essential external dependency; MUST exercise it; MUST define behaviour at quota or capacity exhaustion; MUST have a client that is rejected for quota limit its own outgoing traffic.
Links: Conflicts with none; related AVAILABILITY.2 (retry caps, held there), AVAILABILITY.3 (exercise under real conditions); design held in CONSTRUCTION.

### ASSURANCE.AVAILABILITY.2 Protecting Remote Calls

Intent: how each call to a remote dependency is bounded so that one failing dependency cannot take the caller down or be amplified by it.
1. Decision: Every remote call carries a connection timeout and a request timeout sized from the dependency's measured latency percentile and an accepted false-timeout rate, and a deadline propagated across calls so no work starts for a caller that gave up. The provider's tested client or SDK is used for timeouts and retries, and its default retry behaviour is verified (REG-228: test what happens when built-in mechanisms are exhausted). Retries are limited to transient failures, with capped exponential backoff and jitter, a per-request attempt cap, at one layer only, honouring the provider's explicit throttling and wait signals, on non-read operations only if idempotent by contract or protected by an idempotency key, and bounded system-wide by a retry budget. A circuit breaker is added per dependency when the dependency fails slowly (calls hang until the timeout and hold resources even with timeouts sized to its latency percentile) or is shared by many callers; a long timeout is shortened first (the first rule of this node); a breaker does not protect against timeouts left long (REG-185); it is not added where a queue with dead-letter or the platform already breaks circuits. Guarantees: a failing dependency cannot exhaust the caller's resources, and retries cannot amplify an outage.
2. Grounds: L332 (REG-194 T1, REG-203, REG-211); L339 (REG-203 T2); L333 (REG-203, REG-205 T2, REG-211 T3; consensus; retries are "selfish": caller success against provider load, so the cap and budget serve the provider as well as the caller); L334 (REG-184 T1, REG-205, REG-206, REG-211); L335 (REG-184, REG-185); L336 (REG-201, REG-211); L337 (REG-203, REG-211, consensus); L338 (REG-185 T1, REG-209 T2, REG-203, REG-211; contested, conditions stated by the row).
3. Positions: P1 timeouts and deadline; P2 bounded retry; P3 idempotency; P4 honour throttling signals; P5 provider SDK; P6 retry budget; P7 circuit breaker (protection of own resources, fast failure); P8 retry budget alone (simplicity, cognitive load); P9 neither (queue and dead-letter, or platform).
4. Rejected: retrying without limits or on permanent errors (amplifies; no condition). Retrying at several layers (multiplies attempts; best never, one layer owns it). Blind retry against a 429 or 503 (P4). Hand-written socket code (P5), best only when no SDK exists, then the same bounds are implemented by hand and what the SDK would retry is documented. Circuit breaker everywhere (P7) is rejected as a default: it earns its complexity under the stated condition. Retry budget as the only protection (P8) is the best only when the dependency tolerates retries and callers are few; the budget itself is not an alternative to the breaker but the baseline that the breaker adds to. Neither (P9) is the best in message-driven designs with dead-letter queues or a mesh that already breaks circuits.
5. Context: dependency failure mode and number of callers (L338): slow-failing, synchronous, many callers: add a breaker with half-open probing, logged state changes and a fallback; event-driven: queue and dead-letter; otherwise the retry budget is the protection.
6. Certainty: grounded for timeouts, retry, budget, deadline (T1 and T2 consensus); grounded for the breaker conditions; inferred in part for P4 (HTTP semantics not read in full; the neutral form is "honour back-pressure signals"); the idempotency mechanism is contested (header not standardised, REG-206 an expired draft), so the decision states the principle and leaves the key mechanism to the API.
7. Flags: none.
Constraints: MUST use the provider's tested client where one exists and verify what it retries by default; MUST set both timeouts on every remote call; MUST NOT retry permanent errors or non-idempotent operations without a key; MUST retry at one layer; MUST bound system-wide retries; MUST log breaker state changes.
Links: Related AVAILABILITY.1 (degraded mode); OWNERSHIP.CONTAINMENT (adapter); OPERATION.TELEMETRY (breaker signals); stack pointer L335 (HTTP).

### ASSURANCE.AVAILABILITY.3 Verifying Resilience Under Real Conditions

Intent: how resilience is verified against real traffic without harming users; the canary analysis of regressions before full rollout is held in `CHANGE_FLOW.DEPLOY`.
1. Decision: Verify resilience with automated experiments, continuous where the system allows, built on a steady-state hypothesis over measurable outputs; run them in pre-production by default and on production traffic only when the steady state is measurable, rollback is proven and the blast radius is bounded, with test data isolated from real data. Guardrails every production test shares (the load test of PERFORMANCE.4 too): a measurable steady state or abort criterion, proven rollback, bounded blast radius, test data isolated, marked and removed after the run, and any other durable effect suppressed or undone (the durable-data rule is held in ASSURANCE.BEHAVIOUR.7). A gap an experiment finds is a defect handled by ASSURANCE.BEHAVIOUR.5 (REG-228), which makes it a test that fails first. Guarantees: the resilience claims were exercised under real failure, at a user impact the team chose.
2. Grounds: L120 (REG-069 T3, one source: states the production preference; no counter-source read); L119 (REG-051 T2, REG-069: valuable and risky; issues found there already affect users, test data can become visible); REG-228 (T1, cited directly: a team does not know how a system reacts until it has failed; a gap found is a defect to fix and test; L451 leaves this node's grounds and stays a row of AVAILABILITY.5). The maturity condition is the row's own ("wins with mature observability and rollback").
3. Positions: P1 testing in production, bounded; P2 chaos experiments, ideally in production, continuously (authenticity of confidence); P3 pre-production only (safety; unsourced).
4. Rejected: production experiments without measurable steady state, proven rollback or bounded blast radius (a failure there is a user-visible incident, not a finding). Pre-production only (P3) is the best when observability or rollback is immature, or the system is safety-critical or has low recovery capability; it is also the entry step of the ladder for everyone. Ad hoc fault injection without a hypothesis (no measurable result).
5. Context: observability and rollback maturity, and safety criticality (L120): mature: production experiments allowed; immature or safety-critical: pre-production only.
6. Certainty: grounded for the ladder (pre-production by default, production only on conditions): REG-228 (T1, cited through L451) says to start in non-production and move to production only after non-production insight is exhausted and safeguards limit blast radius and allow quick rollback. Inferred for the production-first preference of L120, which stays one T3 source (REG-069); P3 as a stand-alone position (never production) is unsourced and rejected above with its condition.
7. Flags: none.
Constraints: MUST state a steady-state hypothesis over measurable outputs or an abort criterion; MUST have a proven rollback; MUST bound blast radius; MUST isolate and mark test data from real data and remove it after the run; MUST suppress or undo any other durable effect; MUST treat a gap found as a defect handled by BEHAVIOUR.5.
Links: Related AVAILABILITY.5 (recovery drills); required by PERFORMANCE.4 (its production load tests apply these guardrails); ASSURANCE.BEHAVIOUR.7 holds the durable-data rule, ASSURANCE.BEHAVIOUR.5 holds gap-to-test (load and locks are transient effects, governed by the guardrails here, not by BEHAVIOUR.7's d1); CHANGE_FLOW.DEPLOY holds canary analysis.

### ASSURANCE.AVAILABILITY.4 Proving Restore

Intent: that a backup is defined by whether it restores, and that the restore is proven by test against criteria fixed beforehand.
1. Decision: A backup is a backup only if a restore from it was tested: end to end, regularly, automated, by the same procedures used in a real recovery, against criteria fixed beforehand (data present, uncorrupted, accessible and within the RPO; restore complete within the RTO, with enough resources and no hidden external dependency). Backup integrity is verified before restore and restored assets before service is declared restored; the restore path does not depend on schema-change tooling; every recovery path relied on is exercised, the number of paths kept small, and drift in the recovery site (capacity, quotas, images, configuration) is checked. Guarantees: recovery objectives are shown by test, not assumed.
2. Grounds: L389 (REG-250 T2, REG-251 T1); L1078 (REG-1053 T1, REG-1073 T3 case: backups that did not restore, no ownership); L1097 (REG-1053, REG-1059, REG-1060, REG-1061, REG-1064, REG-1065 T1); L1098 (REG-1053, REG-250); L1099 (REG-1053, REG-1060); L1100 (REG-1056, REG-1058 T1, REG-250). All consensus; the rows are consistent and nested, not competing.
3. Positions: P1 backup defined by restore; P2 regular automated end-to-end test; P3 criteria fixed beforehand; P4 verify before declaring restored; P5 exercise every path, few paths.
4. Rejected: counting a completed backup job as success (the case REG-1073 shows). Restore tests on an ad hoc basis or from procedures that differ from the real recovery (the test then proves a different system). No position competes; no condition makes them best.
5. Context: none.
6. Certainty: grounded (T1 consensus, several sources). Open: no source fixes the cadence beyond "regular"; the cadence is left to the team's objectives.
7. Flags: none.
Constraints: MUST test restore by the real-recovery procedure; MUST fix criteria beforehand; MUST verify integrity before and after; MUST NOT route restore through schema-change tooling.
Links: Index link OPERATION.RECOVERY (practice: backup, RPO and RTO, strategy); related AVAILABILITY.5 (exercise), DATA_INTEGRITY (soft deletion and layered protection).

### ASSURANCE.AVAILABILITY.5 Exercising Recovery

Intent: how recovery procedures are exercised, where, how often, and how measured times feed back.
1. Decision: Exercise recovery on a ladder: tabletop and functional exercises, then a dry run in a non-production environment, then production-level drills for complex or critical paths whose load or quotas a staged environment cannot reproduce; unannounced game days are added once the procedure has passed announced exercises (inferred: a surprise drill of an unproven procedure shows only that it is unproven, at the risk of a real outage). Run the ladder regularly and after changes to the system or the plan; sources give no number for production drills (REG-1056: regularly, regardless of need; REG-1064 reviews the plan about every six months); measure restore or failover time and achieved recovery point in every exercise against the objectives, use measured times, not estimates, as the planning minimum, and record an after-action report whose corrective actions update the plan (the tests a gap calls for are written under ASSURANCE.BEHAVIOUR.5). Guarantees: the recovery objectives are shown by measurement under realistic conditions, at a drill risk the team chose.
2. Grounds: L451 (REG-222, REG-228); cadence: REG-1056, REG-1064 fetched in review; L1102 (REG-1056, REG-1058 T1 AWS; REG-1064 T1 Azure; REG-1059 T1 NIST); L1103 (REG-1059, REG-1064); L1104 (REG-250, REG-1053, REG-1064). The two vendor positions agree that a production-level drill is needed for critical paths and differ on whether to start in non-production; the ladder follows REG-1064 and is compatible with REG-1056 for critical paths.
3. Positions: P1 realistic conditions and tests from gaps; P2 production failover regularly (AWS: realism); P3 non-production first (Azure: safety, since production drills can cause severe failures); P4 ladder plus unannounced game days; P5 ladder with after-action report; P6 measured times.
4. Rejected: production drills first and without a rehearsal (P2 alone): best for critical, complex paths once the procedure is proven and a staged environment cannot reproduce load or quotas. Non-production only (P3 alone): the objectives cannot be shown in real conditions; best when a failed drill's blast radius is unacceptable and no safe production form exists. Estimated recovery times as the planning basis (P6).
5. Context: complexity and criticality of the recovery path, blast radius of a failed drill, novelty of the procedure (L1102): new procedure or high blast radius: climb from the lower rungs first; complex, critical path: include the production-level rung.
6. Certainty: grounded for the ladder, the measurement and the after-action report (T1 consensus); inferred for the sequencing of unannounced game days after proven procedures; open: no source gives the drill frequency in production.
7. Flags: none (the cadence and the game-day ordering are marked open and inferred in Certainty).
Constraints: MUST measure restore time and recovery point in every exercise; MUST compare with the objectives; MUST update the plan from the after-action report; MUST exercise again after changes to the system or the plan.
Links: Index link OPERATION.RECOVERY and OPERATION.INCIDENTS; related AVAILABILITY.3, AVAILABILITY.4; ASSURANCE.BEHAVIOUR.5 holds the tests for gaps found.

---

## ASSURANCE.ARTIFACT Artifact Integrity

Intent: which mechanism guarantees that what runs is what was reviewed and built from reviewed source.
1. Decision: What runs is tied to reviewed source by two mechanisms that the other branches only operate: a protected mainline that binds every actor, and verifiable build provenance checked before the artifact is used. Outcome: what runs is what was reviewed, whoever pushed or built it.
2. Grounds: rolled up from ARTIFACT.1 and .2; claim stated by L1063 (REG-1037, REG-114) and L151, L1244.
3. to 4. see children.
5. Context: see children.
6. Certainty: inferred (roll-up); children grounded.
7. Flags: none.
Constraints: children's MUSTs.
Links: Realized by CHANGE_FLOW.BUILD, CHANGE_FLOW.RELEASE, CHANGE_FLOW.INTEGRATION; related SECURITY.5 and .6 (J3), OWNERSHIP.SERVICES.6 (CI service as supply chain).

### ASSURANCE.ARTIFACT.1 Build Provenance and Match to Source

Intent: how a built artifact is shown to correspond to its source, and how strongly.
1. Decision: Every artifact that is deployed or distributed is produced by a hosted build platform that emits signed provenance (SLSA Build L2), and that provenance is verified before the artifact is used. Raise to hardened, isolated builds (L3: runs isolated from each other, signing material out of reach of user-defined steps) where insider or credential-compromise risk matters or the software is distributed to others or high-value; use bit-identical reproducible builds with independent rebuild only at the highest assurance. For executable objects that are deployed without a build artifact (database functions and the like), compare the deployed definition with the source mechanically (export, normalize, compare signature and body, report by severity). Archive each release with its provenance. Guarantees: a deployed artifact or object is shown to come from reviewed source.
2. Grounds: L151 (REG-023, REG-086 T1; at least L1, L2 for anything distributed, L3 where risk), L1244 (REG-086, REG-1135 T1; at least L2 and verify), L369 (REG-086; L2 and L3 properties), L048 (REG-041, REG-035 T1: reproducible rebuild, adopted at the highest tier only; REG-023: trust signed provenance, most teams); L152 (REG-004 T1, names only: PS.1 to PS.3 protect code, release integrity, archive); L285 (REG-181, maintainer; public practice read as majority, drift detection). Provenance is useless unless verified, which L1244 adds to L151. GitHub documentation (fetched in the final pass): "Artifact attestations by itself provides SLSA v1.0 Build Level 2" (one workflow step, three permissions, one CLI command to verify); this is one platform's fact, inferred for others. The L2 floor is not the most demanding option (L3 and reproducible rebuilds stay conditional); it is the floor because on a hosted platform it costs one step, while L1 provenance can be produced by whoever runs the build. L1 stays best only without a hosted build platform.
3. Positions: P1 reproducible builds (security, control; build discipline); P2 trust signed provenance (cost); P3 level by risk from L1; P4 at least L2 and verify; P5 SSDF protection and archive; P6 L2/L3 build service properties; P7 maintainer: drift comparison of deployed objects against source.
4. Rejected: reproducible rebuilds as the default (P1): best for high-assurance or widely distributed artifacts, costing build discipline. Provenance without signing, L1 only (P3 floor): best only where no hosted build platform is in use, where it is the achievable floor and the gap is declared. Trusting provenance unverified (nothing is guaranteed until a verifier checks it). SSDF names as a standalone rule (P5): its content is open; only the archive point is kept.
5. Context: risk of insider or credential compromise, and breadth of distribution (L151, L048, L369): raises the level from L2 to L3, and from signed provenance to reproducible rebuild. The maintainer's drift check (P7) applies where deployed definitions can change outside the pipeline.
6. Certainty: grounded for the L2 floor on one platform (GitHub documentation), inferred in general; grounded for L2, L3 and reproducibility conditions (T1); the L151 and L1244 difference on the floor is resolved by the platform-cost argument above; inferred for archiving (REG-004 names only, open on content); P7 grounded as maintainer practice, inferred as public practice, a PostgreSQL tool is a stack pointer.
7. Flags: none.
Constraints: MUST produce provenance from a hosted build platform; MUST verify provenance before use; MUST declare the level and the gap where below L2; MUST detect drift of objects that bypass the build.
Links: Realized by CHANGE_FLOW.BUILD and CHANGE_FLOW.RELEASE; Related OWNERSHIP.SERVICES.6 (CI service as supply chain, kept there), SECURITY.5 (consumed code); stack pointer L285 (PostgreSQL tool).

### ASSURANCE.ARTIFACT.2 Protected Mainline Binds Every Actor

Intent: that required reviews and checks bind every actor, including bots and administrators, and restrict where automation may write.
1. Decision: Protect the mainline mechanically: required review and required status checks before merge, no force push, restricted push rights, and these rules bind every actor, including bots and administrators, with signed commits where provenance of authorship is required. Automation pushes only to a restricted, non-protected target (one branch), never directly to protected branches, by tag or by deletion, and cannot bypass the rules through the access it holds. Guarantees: what is merged was reviewed and checked, whoever pushed it.
2. Grounds: L131 (REG-091 T1, REG-094 T2, REG-114 T1; consensus); L1063 (REG-1037, REG-114; consensus); L1070 (REG-1036, REG-1037 T1 vendor documentation; majority).
3. Positions: P1 protect the mainline; P2 rules bind every actor; P3 automation writes only to a restricted target.
4. Rejected: advisory review or checks that an administrator or bot can bypass (they guarantee nothing about what ran); best never for the guarantee "what runs is what was reviewed". No competing position; the three rows are layers of one mechanism.
5. Context: signed commits where provenance of authorship is required (L131). Whether a mechanism enforces the rules is platform-specific (GitHub terms in the sources; neutral in principle).
6. Certainty: grounded (T1 documentation, consensus; L1070 majority, from vendor documentation of two products).
7. Flags: none.
Constraints: MUST enforce review and checks by the platform, not by convention; MUST apply them to bots and administrators; MUST restrict automation to a non-protected target.
Links: Index to CHANGE_FLOW.INTEGRATION (carries it out); related RULES.3 and RULES.4, SECURITY.6 (limits on automation and access, J3); stack pointers L131, L1063, L1070 (GitHub terms).

---

## Flags raised

All settled; none remains open on a record. Outcome of each:

- F1 (AVAILABILITY.3): settled (ladder grounded in REG-228; closed by the review, confirmed in the final pass).
- F2 (ARTIFACT.1): settled in the final pass (flag-4): decision unchanged, fetched GitHub fact replaces the uncited cost claim; grounded for one platform, inferred in general.
- F3 (AVAILABILITY.3 and PERFORMANCE.4): settled by X5 (guardrails in AVAILABILITY.3; durable-data rule in BEHAVIOUR.7; load and locks are transient effects).
- F4 (PERFORMANCE.5): settled in the final pass (flag-6): instance of measure before optimising; warm-up separation a scope.
- F5 (PERFORMANCE.3): closed by review fix-4 (REG-242 read; supports the no-gating-on-noise rule, not scheduling by noise).
- F6 (AVAILABILITY.1): closed by the review (retry caps stated once in AVAILABILITY.2), confirmed in the final pass.
- F7 (AVAILABILITY.5): settled in the final pass (flag-5): game-day ordering inferred with its reason, cadence stated as unsourced with REG-1056 and REG-1064.
- F8 (PERFORMANCE.2): closed by the review (REG-239 mechanism), confirmed in the final pass.

## Review applied

- fix-1: applied (AVAILABILITY.3 certainty and F1: ladder grounded in REG-228).
- fix-2: applied (AVAILABILITY.1 decision, positions, rejected, constraint: client-side throttling).
- fix-3: applied (AVAILABILITY.2 decision and constraint: provider's tested client, verify default retries).
- fix-4: applied (PERFORMANCE.3 decision, grounds, certainty, constraint, context; F5 closed).
- fix-5: applied (PERFORMANCE.4 decision carries the replica condition).
- fix-6: applied (PERFORMANCE.5 grounds cite L1563).

## Final pass applied

Resolutions (J4 section of the final-pass resolutions file):

- flag-1 (F3), ASSURANCE.PERFORMANCE.4 and ASSURANCE.AVAILABILITY.3, cross-unit X5: applied (see X5 below).
- flag-2, PERFORMANCE.4 and AVAILABILITY.3: applied. AVAILABILITY.3 holds the shared guardrails; PERFORMANCE.4 keeps off-peak, ramp, reserved capacity; its constraints now read "MUST apply the production-test guardrails of AVAILABILITY.3; MUST, for load, run off-peak, ramp from a small share and reserve capacity".
- flag-3, AVAILABILITY.3 and AVAILABILITY.5, cross-unit X13: applied (see X13 below).
- flag-4 (F2), ARTIFACT.1: applied. Decision unchanged; grounds carry the fetched GitHub fact; certainty grounded for one platform, inferred in general; F2 removed from ARTIFACT.1 and ARTIFACT.
- flag-5 (F7), AVAILABILITY.5: applied. Game-day ordering and cadence text replaced as stated; REG-1056, REG-1064 added to grounds; F7 removed.
- flag-6 (F4), PERFORMANCE.5: applied. Decision unchanged; certainty replaced as stated; F4 removed.
- flag-7, AVAILABILITY.2: applied. Breaker trigger replaced; the "shorten a long timeout first; a breaker does not protect against timeouts left long (REG-185)" sentence added.
- Judge flags F1, F5, F6, F8: applied as confirmed closed; removed from the records' Flags.

Cross-unit lines naming J4:

- X5: applied. AVAILABILITY.3 holds the guardrails and points to BEHAVIOUR.7; PERFORMANCE.4 points to AVAILABILITY.3 and keeps only off-peak, ramp and reserved capacity. BEHAVIOUR.7 text (d1) is J2's record, not edited here.
- X11: applied. PERFORMANCE.1 keeps its percentile threshold, points to OPERATION.RELIABILITY.1 for percentiles and drops L177 from its grounds; "never from current performance as a final value; a provisional start from measured history follows OPERATION.RELIABILITY.2" (decision, rejected, constraint). PERFORMANCE.5 keeps L177 for its own run-to-run distribution rule.
- X13: applied. AVAILABILITY.3 treats a gap found as a defect handled by BEHAVIOUR.5 and cites REG-228 directly (L451 leaves its grounds); AVAILABILITY.5 keeps "corrective actions update the plan", L451 stays its row, and it points to BEHAVIOUR.5 for the tests.
- X2: not applied here: the ASSURANCE L1 re-roll is a wave 3 roll-up, outside this unit's records.

Nodes added: none (the J4 resolutions create none).
Maintainer point: none for J4 (ASSURANCE.RULES.4 is J2 only).
Flags still open: none. Open items kept in Certainty text: no source fixes the backup-restore cadence beyond "regular" (AVAILABILITY.4); no source gives a production-drill number (AVAILABILITY.5).
