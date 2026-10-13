# Assurance: Performance and Availability

## Table of Contents

1. [Performance](#performance) _(Lines 24-26)_
   1. [Targets and Budgets](#targets-and-budgets) _(Lines 29-38)_
   1. [Load Test Design](#load-test-design) _(Lines 41-56)_
   1. [When Tests Run and Baselines](#when-tests-run-and-baselines) _(Lines 59-70)_
   1. [Testing in Production for Performance](#testing-in-production-for-performance) _(Lines 73-81)_
   1. [Measurement Before Optimization](#measurement-before-optimization) _(Lines 84-95)_
1. [Availability and Recovery](#availability-and-recovery) _(Lines 98-100)_
   1. [Tolerating a Degraded Dependency](#tolerating-a-degraded-dependency) _(Lines 103-112)_
   1. [Protecting Remote Calls](#protecting-remote-calls) _(Lines 115-131)_
   1. [Verifying Resilience Under Real Conditions](#verifying-resilience-under-real-conditions) _(Lines 134-145)_
   1. [Proving Restore](#proving-restore) _(Lines 148-158)_
   1. [Exercising Recovery](#exercising-recovery) _(Lines 161-171)_

---

Part of [Assurance](assurance.md). Speed and capacity under the real workload, and service and recovery when something fails.

## Performance
<!-- Lines 24-26 -->

Speed and capacity hold under the real workload because targets derive from user need, load tests resemble real use and run at the stage that fits their cost, every run is compared with a baseline, production supplies what replicas cannot, and no speed claim stands without measurement. A regression is caught on the change that caused it. `ASSURANCE.PERFORMANCE`

### Targets and Budgets
<!-- Lines 29-38 -->

A performance target is derived from user need and the service objective and stated as a measurable pass-or-fail threshold on a percentile, never from current performance as a final value (that ratifies whatever exists). Where a request crosses layers, the budget is split per layer so a failing test names the layer to optimize.

Rules:
- MUST state the target as a threshold on a percentile.
- MUST NOT derive it from current performance as a final value.
- MUST name the layer budget when a layered path is tested.

For client-delivered software, also enforce budgets on artefact size and timing metrics in the build. The target is an objective derived from [Reliability Targets](operation_objectives_and_signals.md#reliability-targets); the percentile rule is in [Indicators](operation_objectives_and_signals.md#indicators) and a provisional start from measured history in [Objective Level and Starting Point](operation_objectives_and_signals.md#objective-level-and-starting-point). `ASSURANCE.PERFORMANCE.1`

### Load Test Design
<!-- Lines 41-56 -->

A load test exercises the whole workload end to end with a representative request mix and realistic data. The environment matches production on the properties that decide the result. It is driven at a constant arrival rate and run past expected load to the breaking point, so its result predicts real behaviour, including how and where the system fails. Test types are chosen by risk and widened as risk and experience grow. Overload is read as goodput, not server throughput.

Rules:
- MUST test end to end, with a representative mix and realistic data.
- MUST record the environment fidelity chosen and which third parties were real.
- MUST report tail latency under an open-loop or corrected generator (a closed-loop generator stops sending when responses stall and understates slow samples).
- MUST know the breaking point and its early-warning metrics.

Best instead when:
- Production-identical environment: mission-critical workload, or the result gates capacity spend. A scaled-down environment when criticality is low and load is known to scale predictably.
- Real third-party calls: the dependency is critical and the provider permits load tests. Stub it when policy forbids load or to isolate own code, and say which calls were mocked.
- Isolated-component load tests: as a diagnostic after the end-to-end result localizes a layer.

Judged against [Targets and Budgets](#targets-and-budgets); whether it may run in production is decided in [Testing in Production for Performance](#testing-in-production-for-performance); the breaking point feeds [Planning Method](operation_response_and_readiness.md#planning-method) and [Headroom and Overload](operation_response_and_readiness.md#headroom-and-overload). Open: open-loop generation as a rule rests on one source with the mechanism stated. `ASSURANCE.PERFORMANCE.2`

### When Tests Run and Baselines
<!-- Lines 59-70 -->

Each performance test is placed by its cost and noise. Fast, stable checks gate every change. Long, expensive or noisy tests run on a schedule or before anticipated events, and a noisy test does not gate until its variance is below the threshold it enforces. Every run is compared with a recorded baseline of normal performance, so a regression is found within one scheduled interval and, for the cheap tier, on the change that caused it. A change predicted to move performance materially is validated as a hypothesis: state the prediction, run the same load test on baseline and variant, compare.

Rules:
- MUST compare each run with a baseline, and refresh it after architectural or scaling change.
- MUST NOT gate a change on a signal whose noise exceeds the threshold it enforces.
- MUST check production configuration, not only code.

Best instead when: gating every change on the full load suite, if the harness is stable, low-variance and fast; scheduled-only, for tests that are long, expensive or noisy (at the price of attribution to one change).

Applies [Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed); needs the distribution rule of [Measurement Before Optimization](#measurement-before-optimization); reads the signals of [What Is Measured - Service and Resource Signals](operation_objectives_and_signals.md#what-is-measured---service-and-resource-signals); realised in [Build and Pipeline](change_flow_delivery.md#build-and-pipeline). `ASSURANCE.PERFORMANCE.3`

### Testing in Production for Performance
<!-- Lines 73-81 -->

Pre-production tests are the base. Controlled production tests add what only production has: real data, network, third parties, and state such as caches and request affinity. The exception is a system where a faithful replica is affordable and the impact is high. Every production test applies the shared guardrails of [Verifying Resilience Under Real Conditions](#verifying-resilience-under-real-conditions); a load test adds off-peak timing, a ramp from a small share of traffic and reserved capacity.

Rules:
- MUST apply those guardrails.
- A production load test MUST run off-peak, ramp from a small share and reserve capacity.

Best instead when: pre-production only, if the system is high-impact and a faithful replica exists and is affordable. Leaves no durable effect on data: [Tests Without Durable Effect on Data](assurance_behaviour.md#tests-without-durable-effect-on-data). Canary analysis and rollback: [Deployment](change_flow_delivery.md#deployment). `ASSURANCE.PERFORMANCE.4`

### Measurement Before Optimization
<!-- Lines 84-95 -->

Optimization targets only what measurement on the real workload has shown critical, prioritized with field data and tested with lab data before release. Where architecture is hard to change and load is high, add a design-time estimate. A measurement counts as evidence only when reported as a distribution across several runs; a performance belief becomes a rule only after such a measurement.

Rules:
- MUST measure before optimizing.
- MUST report a distribution, not one number, and separate warm-up where the runtime has one.
- MUST prioritize by field data where it exists.

Best instead when: measurement alone with no design-time estimate, if architecture is cheap to change or load is low; restructuring on mechanism alone, only once the claimed mechanism is itself confirmed by a measurement on this workload.

Open: the two measurement methods come from studies on specific runtimes; transfer to others is inferred. Required by [When Tests Run and Baselines](#when-tests-run-and-baselines); which signals exist: [What Is Measured - Service and Resource Signals](operation_objectives_and_signals.md#what-is-measured---service-and-resource-signals). `ASSURANCE.PERFORMANCE.5`

## Availability and Recovery
<!-- Lines 98-100 -->

The system keeps serving when a dependency fails because each dependency has a designed degraded mode and a bounded call. Resilience is verified by hypothesis-driven experiments under real conditions, and recovery is guaranteed by restores proven against criteria fixed beforehand and by exercised procedures with measured times. An untested mode, backup or plan is treated as absent. This section holds the proof; the practice (backup, objectives, strategy, failover) is in [Backup, Restore and Disaster Recovery](operation_recovery_and_feedback.md#backup-restore-and-disaster-recovery). `ASSURANCE.AVAILABILITY`

### Tolerating a Degraded Dependency
<!-- Lines 103-112 -->

Each non-essential dependency has a designed and regularly exercised degraded mode. Hard dependencies are made soft where possible and kept few. Overload behaviour is defined: reject early when out of quota or capacity, serve degraded responses before errors, and a client that sees much of its recent traffic rejected for quota limits its own outgoing traffic. One slow or failed non-essential dependency, or a load beyond capacity, then reduces service instead of ending it.

Rules:
- MUST define the degraded mode for each non-essential external dependency, and MUST exercise it.
- MUST define behaviour at quota or capacity exhaustion.
- A client rejected for quota MUST limit its own outgoing traffic.

Best instead when: failing hard is right only for an essential dependency, which then needs the bounds of [Protecting Remote Calls](#protecting-remote-calls). Which dependencies are essential is a per-system fact. Design lives in [construction.md](construction.md); exercised under the conditions of [Verifying Resilience Under Real Conditions](#verifying-resilience-under-real-conditions). `ASSURANCE.AVAILABILITY.1`

### Protecting Remote Calls
<!-- Lines 115-131 -->

Every remote call is bounded by connection and request timeouts sized from the dependency's measured latency percentile, and by a deadline propagated across calls. Retries are limited to transient failures, capped, made at one layer only, safe for non-read operations only if idempotent, and bounded system-wide by a retry budget. Back-pressure signals from the provider are honoured. A circuit breaker, whose state changes are logged, is added only where a dependency fails slowly or is shared by many callers (shorten a long timeout first). So a failing dependency cannot exhaust the caller's resources and retries cannot amplify an outage.

Rules:
- MUST use the provider's tested client where one exists, and verify what it retries by default.
- MUST set both timeouts on every remote call.
- MUST NOT retry permanent errors, or non-idempotent operations without a key.
- MUST retry at one layer and MUST bound system-wide retries.
- MUST log breaker state changes.

Best instead when:
- Retry budget alone: the dependency tolerates retries and callers are few.
- Queue with dead-letter, or a mesh that already breaks circuits: message-driven designs.
- Hand-written client code: no provider client exists; then implement the same bounds and document what a client would retry.

Open: the idempotency-key mechanism is contested and left to the interface. Retry caps are stated once, here. Breaker signals: [What Is Measured - Service and Resource Signals](operation_objectives_and_signals.md#what-is-measured---service-and-resource-signals). `ASSURANCE.AVAILABILITY.2`

### Verifying Resilience Under Real Conditions
<!-- Lines 134-145 -->

Resilience is verified by automated experiments built on a steady-state hypothesis over measurable outputs. Run them in pre-production by default; on production traffic only when the steady state is measurable, rollback is proven and the blast radius is bounded. These guardrails govern the transient effects every production test shares; durable effects on data fall under [Tests Without Durable Effect on Data](assurance_behaviour.md#tests-without-durable-effect-on-data). A gap an experiment finds is a defect handled by [Tests Driven by Change](assurance_behaviour.md#tests-driven-by-change).

Rules:
- MUST state a steady-state hypothesis over measurable outputs, or an abort criterion.
- MUST have a proven rollback and MUST bound blast radius.
- MUST treat a gap found as a defect.

Best instead when: pre-production only, if observability or rollback is immature, or the system is safety-critical or has low recovery capability (it is also the entry rung for everyone). Ad hoc fault injection without a hypothesis yields no measurable result.

Open: the preference for production-first experiments rests on one source; the ladder is grounded. Used by [Testing in Production for Performance](#testing-in-production-for-performance); canary analysis is in [Deployment](change_flow_delivery.md#deployment). `ASSURANCE.AVAILABILITY.3`

### Proving Restore
<!-- Lines 148-158 -->

A backup counts only if a restore from it was tested end to end, regularly and automatically, by the procedure of a real recovery, against criteria fixed beforehand: data present, uncorrupted, accessible and within the recovery point; restore complete within the recovery time. A restore runs by its own path, independent of schema-change tooling. Backup integrity is verified before restore, and restored assets before service is declared restored. The recovery objectives are shown by test, not assumed.

Rules:
- MUST test restore by the real-recovery procedure.
- MUST fix criteria beforehand.
- MUST verify integrity before and after.
- MUST NOT route restore through schema-change tooling.

A completed backup job is not success; an ad hoc restore test, or one from a different procedure, proves a different system. Open: no source fixes the cadence beyond "regular"; it follows the team's objectives. Relied on by [Layered Protection and Deletion Form](assurance_interfaces_data.md#layered-protection-and-deletion-form) and [Closing the Loop on Findings](assurance_docs_security.md#closing-the-loop-on-findings). `ASSURANCE.AVAILABILITY.4`

### Exercising Recovery
<!-- Lines 161-171 -->

Recovery is exercised on a ladder: tabletop and functional exercises, then a dry run in a non-production environment, then production-level drills for complex or critical paths. Unannounced game days are added once the procedure has passed announced exercises. Restore or failover time and the achieved recovery point are measured in every exercise against the objectives, and an after-action report updates the plan.

Rules:
- MUST measure restore time and recovery point in every exercise, and compare with the objectives.
- MUST update the plan from the after-action report.
- MUST exercise again after changes to the system or the plan.

Best instead when: production drills first, for critical, complex paths once the procedure is proven and a staging environment cannot reproduce load or quotas; non-production only, when a failed drill's blast radius is unacceptable and no safe production form exists. Estimated recovery times are not a planning basis.

Open: no source gives a frequency for production drills (regularly and after changes only); ordering unannounced game days after announced exercises is inferred. Repeats and measures the path proven in [Proving Restore](#proving-restore); tests for gaps found: [Tests Driven by Change](assurance_behaviour.md#tests-driven-by-change); incident handling in [operation.md](operation.md). `ASSURANCE.AVAILABILITY.5`
