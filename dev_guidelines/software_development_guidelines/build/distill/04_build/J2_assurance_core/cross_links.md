# Cross links of J2_assurance_core

Links with one endpoint outside the unit, for the linker. Type vocabulary as in the batch: requires, refines, dataflow, conflicts, see (the judge records say "realizes", "index" and "points to"; "realizes" is kept where a record uses it, a pointer is `see`). Source is the node that carries the statement in its record or in the cross-unit line named in the last column.

| source uid | target uid | type | intent | origin |
|---|---|---|---|---|
| ASSURANCE.SECURITY.2 | ASSURANCE.RULES.1 | requires | Security findings block or advise under the false-alarm budget that RULES.1 holds; SECURITY.2 keeps only its release-time block on exploitable findings, who may waive, and the published figure. | X4 |
| ASSURANCE.SECURITY.3 | ASSURANCE.BEHAVIOUR.6 | see | The coverage floor is decided in BEHAVIOUR.6 (none, security-relevant code included); SECURITY.3 states no coverage figure of its own. | X1, R21 |
| CHANGE_FLOW.BUILD | ASSURANCE.RULES.2 | realizes | The build pipeline carries out the placement of checks and the minutes-long blocking feedback. | RULES.2 Links |
| CHANGE_FLOW.INTEGRATION | ASSURANCE.RULES.3 | realizes | Protecting the mainline is how a gate that cannot be skipped is carried out at integration. | RULES.3 Links |
| ASSURANCE.ARTIFACT.2 | ASSURANCE.RULES.3 | realizes | The protected mainline realizes the gate that always runs and fails closed. | RULES.3 Links |
| ASSURANCE.ARTIFACT.2 | ASSURANCE.RULES.4 | realizes | The protected mainline realizes the independent review and the approval that binds the exact content. | RULES.4 Links (L131, L1063) |
| ASSURANCE.RULES.4 | CHANGE_FLOW.REVIEW | see | RULES.4 decides what makes a review independent and binding; CHANGE_FLOW.REVIEW holds how review is carried out (index, MD-03). | RULES.4 Links |
| CHANGE_FLOW.REVIEW.1 | ASSURANCE.RULES.4 | see | Review is not reserved for uncertain changes because that leaves the classification to the author at the moment of the change; the reason is held in RULES.4 (Rejected P3 of REVIEW.1 points here). | X14 |
| CHANGE_FLOW.REVIEW | ASSURANCE.RULES.5 | see | The evidence that completion is shown, not asserted, is realized in review. | RULES.5 Links |
| CHANGE_FLOW.BUILD | ASSURANCE.BEHAVIOUR.1 | realizes | The build runs the self-testing suite on every change. | BEHAVIOUR.1 Links |
| ASSURANCE.AVAILABILITY.3 | ASSURANCE.BEHAVIOUR.5 | see | A gap found by an experiment in production is a defect handled by BEHAVIOUR.5 (cites REG-228 directly). | X13 |
| ASSURANCE.AVAILABILITY.5 | ASSURANCE.BEHAVIOUR.5 | see | Corrective actions update the plan; the tests that a found gap becomes are held in BEHAVIOUR.5. | X13 |
| CONSTRUCTION.PARADIGM | ASSURANCE.BEHAVIOUR.5 | see | The placement of a scheduled job is held in CONSTRUCTION.PARADIGM; BEHAVIOUR.5 holds that the job is tested before it is scheduled. | BEHAVIOUR.5 Links |
| ASSURANCE.BEHAVIOUR.7 | ASSURANCE.AVAILABILITY.3 | see | The durable-data rule for tests in production is held in BEHAVIOUR.7; AVAILABILITY.3 holds the guardrails every production test shares, and load and locks as transient effects. | X5 |
| ASSURANCE.PERFORMANCE.4 | ASSURANCE.AVAILABILITY.3 | see | Testing in production for performance points to the shared guardrails; relevant here only as the other end of X5, owned by J4. | X5 |
| ASSURANCE.BEHAVIOUR.7 | TRANSVERSE.PRIVACY | see | Real records in test data are subject to the privacy rules held in TRANSVERSE.PRIVACY (index only, MD-03). | BEHAVIOUR.7 d2, R22 |
| ASSURANCE.BEHAVIOUR | ASSURANCE.DATA_INTEGRITY | see | The property-specific tests of data integrity are held there; BEHAVIOUR holds the general testing decisions. | BEHAVIOUR Links |
| ASSURANCE.BEHAVIOUR | ASSURANCE.SECURITY | see | The security-specific tests (verification techniques, fuzz depth) are held there. | BEHAVIOUR Links |
| ASSURANCE.BEHAVIOUR | ASSURANCE.PERFORMANCE | see | The performance-specific tests are held there. | BEHAVIOUR Links |
| ASSURANCE.BEHAVIOUR | ASSURANCE.ARTIFACT | see | The artifact-specific checks are held there. | BEHAVIOUR Links |
| OPERATION.FEEDBACK | ASSURANCE.BEHAVIOUR.8 | see | The pitfall catalogue and the no-blanket-search-and-replace practice are held in BEHAVIOUR.8; OPERATION.FEEDBACK links here rather than holding them. | BEHAVIOUR.8, R31 |
| OWNERSHIP.SERVICES.2 | ASSURANCE.CONTRACTS.1 | see | SERVICES.2 keeps only the consumer side (read the promise, consume deprecation signals, pin the version) and points to CONTRACTS.1 for the provider policies and when each is best. | X7 |
| EVOLUTION.DECOMMISSION.4 | ASSURANCE.CONTRACTS.1 | see | The indefinitely compatible, date-pinned surface is held in CONTRACTS.1. | X7 |
| ASSURANCE.CONTRACTS.1 | OWNERSHIP.CONTAINMENT | see | The consumer side of depending on a rented service is held in OWNERSHIP.CONTAINMENT. | CONTRACTS.1 Links |
| ASSURANCE.CONTRACTS.1 | CONSTRUCTION.BOUNDARY | see | How a declared public interface and its compatibility are realized in code is held in CONSTRUCTION.BOUNDARY. | CONTRACTS.1 Links |
| CONSTRUCTION.BOUNDARY | ASSURANCE.CONTRACTS | realizes | Contracts are realized in code at the boundary. | CONTRACTS Links |
| ASSURANCE.CONTRACTS.2 | OWNERSHIP.SERVICES | see | Doubles of rented services are backed by contract tests against the real service. | CONTRACTS.2 Links |
| ASSURANCE.CONTRACTS.2 | OWNERSHIP.CONTAINMENT | see | Contract tests at the containment seam of an external service. | CONTRACTS.2 Links |
| ASSURANCE.CONTRACTS.3 | TRANSVERSE.DOCS | see | The authoring of reference documentation is held in TRANSVERSE.DOCS; CONTRACTS.3 holds only where the description originates (MD-03). | CONTRACTS.3 Links |

Not listed: the links of the L1 node ASSURANCE and the parent-child arcs (the L1 batch and the batch tree), and the "used by every other property node" statement of RULES (no single target). The L2 statements "BEHAVIOUR requires RULES.1 to RULES.3" and "CONTRACTS requires RULES.3" are carried at L3 level in the batch (BEHAVIOUR.1, BEHAVIOUR.2, CONTRACTS.3). The row of PERFORMANCE.4 and the two AVAILABILITY lines are owned by J4; they are listed so the linker sees the pairing, drop them if J4 already emits them.
