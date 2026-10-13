# Cross links: unit J4_assurance_runtime

Links with one endpoint outside this unit, for the linker. Direction: source depends on, refines, realizes or points to target. Types: requires, refines, realizes, see (related or index pointer). Targets marked (new) are created by cross-unit fix X12 at graph build; targets marked (check) are L2 or L3 uids taken from the skeleton tree.

| source | target | type | intent |
|---|---|---|---|
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY | refines | The performance target is an objective derived from the service objective that RELIABILITY owns. |
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY.1 | see | The percentile rule for latency is held in RELIABILITY.1 (X11). |
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY.2 | see | A provisional start from measured history follows RELIABILITY.2 (X11). |
| ASSURANCE.PERFORMANCE.2 | OPERATION.CAPACITY | see | Capacity planning consumes the breaking point that the load test finds. |
| ASSURANCE.PERFORMANCE.3 | CHANGE_FLOW.BUILD | see | The pipeline stages of the build carry the per-change and scheduled placement of performance tests. |
| ASSURANCE.PERFORMANCE.3 | ASSURANCE.RULES.2 | see | The placement of a test by cost and noise applies the placement rule of RULES.2. |
| ASSURANCE.PERFORMANCE.3 | OPERATION.TELEMETRY.7 (new) | see | Synthetic monitoring of customer routes is held in the vantage-point node of telemetry (X12). |
| ASSURANCE.PERFORMANCE.4 | CHANGE_FLOW.DEPLOY | see | Canary analysis and rollback on organic traffic are held in DEPLOY. |
| ASSURANCE.PERFORMANCE.4 | ASSURANCE.BEHAVIOUR.7 | see | The durable-data rule for tests in production is held in BEHAVIOUR.7; load and locks are transient effects governed by the guardrails of AVAILABILITY.3 (X5). |
| ASSURANCE.PERFORMANCE.5 | OPERATION.TELEMETRY.1 | see | Which signals exist, and so what can be measured, is held in TELEMETRY.1. |
| ASSURANCE.PERFORMANCE | OPERATION.RELIABILITY | see | Index: alerting and objectives realize performance targets in operation. |
| ASSURANCE.PERFORMANCE | OPERATION.CAPACITY | see | Index: capacity planning realizes the headroom that tests establish. |
| ASSURANCE.PERFORMANCE | CHANGE_FLOW.DEPLOY | see | Index: canary analysis in deployment realizes production-side performance checks. |
| ASSURANCE.AVAILABILITY | OPERATION.RECOVERY | see | Index (MD-03): RECOVERY holds the practice of backup, objectives, strategy and failover; this node holds the proof. |
| ASSURANCE.AVAILABILITY | OPERATION.RELIABILITY | see | RELIABILITY realizes the availability guarantees in operation. |
| ASSURANCE.AVAILABILITY | OPERATION.READINESS | see | READINESS realizes the availability guarantees in operation. |
| ASSURANCE.AVAILABILITY.1 | CONSTRUCTION | see | The design of a degraded mode is held in code construction; this node holds the verification (target node left to the linker, no L3 named by the record). |
| ASSURANCE.AVAILABILITY.2 | OWNERSHIP.CONTAINMENT.2 | see | The adapter between code and dependency is where timeouts and retries are applied. |
| ASSURANCE.AVAILABILITY.2 | OPERATION.TELEMETRY.1 | see | Circuit-breaker state changes are signals that telemetry records. |
| ASSURANCE.AVAILABILITY.3 | ASSURANCE.BEHAVIOUR.5 | requires | A gap an experiment finds is a defect handled by BEHAVIOUR.5, which makes it a test that fails first (X13). |
| ASSURANCE.AVAILABILITY.3 | ASSURANCE.BEHAVIOUR.7 | see | The durable-data rule is held in BEHAVIOUR.7; the guardrails here govern transient effects (X5). |
| ASSURANCE.AVAILABILITY.3 | CHANGE_FLOW.DEPLOY | see | Canary analysis of regressions before full rollout is held in DEPLOY. |
| ASSURANCE.AVAILABILITY.4 | OPERATION.RECOVERY | see | Index: backup, objectives and strategy are held in RECOVERY. |
| ASSURANCE.AVAILABILITY.4 | ASSURANCE.DATA_INTEGRITY.3 | see | Layered protection and soft deletion relate to what a restore must bring back. |
| ASSURANCE.AVAILABILITY.5 | OPERATION.RECOVERY | see | Index: recovery objectives and strategy are held in RECOVERY. |
| ASSURANCE.AVAILABILITY.5 | OPERATION.INCIDENTS | see | Exercises relate to how incidents are run and reviewed. |
| ASSURANCE.AVAILABILITY.5 | ASSURANCE.BEHAVIOUR.5 | see | The tests a gap found in an exercise calls for are written under BEHAVIOUR.5 (X13). |
| CHANGE_FLOW.BUILD | ASSURANCE.ARTIFACT | realizes | Build operates the provenance mechanism. |
| CHANGE_FLOW.RELEASE | ASSURANCE.ARTIFACT | realizes | Release operates the provenance mechanism. |
| CHANGE_FLOW.INTEGRATION | ASSURANCE.ARTIFACT | realizes | Integration operates the protected mainline. |
| CHANGE_FLOW.BUILD | ASSURANCE.ARTIFACT.1 | realizes | The build platform produces the signed provenance this node requires. |
| CHANGE_FLOW.RELEASE | ASSURANCE.ARTIFACT.1 | realizes | Release archives each release with its provenance. |
| ASSURANCE.ARTIFACT.1 | OWNERSHIP.SERVICES.6 | see | The CI service as supply chain is kept in SERVICES.6; this node holds provenance. |
| ASSURANCE.ARTIFACT.1 | ASSURANCE.SECURITY.5 | see | Consumed code is treated in SECURITY.5. |
| ASSURANCE.ARTIFACT.2 | CHANGE_FLOW.INTEGRATION | see | Index: INTEGRATION carries out the protected mainline. |
| ASSURANCE.ARTIFACT.2 | ASSURANCE.RULES.3 | see | Gates that cannot be skipped bind through the same mechanism. |
| ASSURANCE.ARTIFACT.2 | ASSURANCE.RULES.4 | see | Independent review that binds is enforced by the protected mainline. |
| ASSURANCE.ARTIFACT.2 | ASSURANCE.SECURITY.6 | see | Limits on automation and access are set in SECURITY.6. |
