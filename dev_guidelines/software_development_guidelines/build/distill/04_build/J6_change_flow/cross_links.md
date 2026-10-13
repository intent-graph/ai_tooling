# Cross links from J6_change_flow

Links whose other endpoint is outside this unit; for the linker. Type `realizes` or `related` (shape type). Direction is source to target as the judge record states it. Source uids exist after this batch; targets belong to other units (and ASSURANCE.CONTRACTS, ASSURANCE.ARTIFACT, ASSURANCE.AVAILABILITY, ASSURANCE.DATA_INTEGRITY, ASSURANCE.RULES, OPERATION.TELEMETRY and similar are L2 or L1 nodes there).

Notes: the skeleton's Conflicts links (DEPLOY.1 and DEPLOY.3 against DATA_CHANGE.3, ROLLBACK.1 against ROLLBACK.3) are resolved by the judge record (a gate inside one pipeline, undo decided per class) and carry no link. Cross-unit X6 and X14 are reflected in the SECURITY.6 and RULES.4 rows. X7, X12 name no J6 node; DATA_CHANGE.8 and OPERATION.TELEMETRY: the linker may point to TELEMETRY.1 (service and resource signals).

| source uid | target uid | type | intent |
|---|---|---|---|
| CHANGE_FLOW.INTEGRATION | ASSURANCE.RULES | realizes | Version control and integration realize the rule that checks bind and review is accountable. |
| CHANGE_FLOW.INTEGRATION | ASSURANCE.ARTIFACT.2 | related | The mechanism that binds every actor on the mainline is held at ARTIFACT.2. |
| CHANGE_FLOW.INTEGRATION.1 | OWNERSHIP.LIFECYCLE | related | The one-version rule for shared components is a dependency rule. |
| CHANGE_FLOW.INTEGRATION.2 | ASSURANCE.RULES.2 | related | Small, frequent integrations are the small feedback loops RULES.2 asks for. |
| CHANGE_FLOW.INTEGRATION.6 | ASSURANCE.SECURITY.6 | related | Distinct automation identities and actor boundaries sit beside the limits enforced in tooling. |
| CHANGE_FLOW.INTEGRATION.6 | ASSURANCE.ARTIFACT.2 | related | The recorded trail supports the mainline that binds every actor. |
| CHANGE_FLOW.INTEGRATION.6 | ASSURANCE.RULES.4 | related | A named accountable person approves a change not attributable to a person. |
| CHANGE_FLOW.INTEGRATION.6 | ASSURANCE.RULES.5 | related | One bar for every change is why no disclosure rule is needed. |
| CHANGE_FLOW.REVIEW | ASSURANCE.RULES | realizes | Review carries out the independent, accountable, content-bound review the rules decide. |
| CHANGE_FLOW.REVIEW.1 | ASSURANCE.RULES.4 | related | Mechanism and depth realize independent review; the reason the post-merge show is only a low-risk tier is held there (cross-unit X14). |
| CHANGE_FLOW.REVIEW.1 | ASSURANCE.RULES.5 | related | One bar for every change, depth set by risk and evidence. |
| CHANGE_FLOW.REVIEW.3 | ASSURANCE.BEHAVIOUR.8 | related | The defect catalog meets the defect classes that survive review. |
| CHANGE_FLOW.REVIEW.4 | ASSURANCE.RULES.2 | related | Automated checks run before the reviewer, where the rules place each check. |
| CHANGE_FLOW.REVIEW.4 | ASSURANCE.RULES.4 | related | A machine may assist but is never the accountable approving party. |
| CHANGE_FLOW.BUILD | ASSURANCE.ARTIFACT | realizes | The scripted build and promoted artifact make provenance and the bound mainline checkable. |
| CHANGE_FLOW.BUILD.1 | ASSURANCE.BEHAVIOUR.1 | related | What the self-testing suite contains is decided at BEHAVIOUR.1. |
| CHANGE_FLOW.BUILD.1 | OWNERSHIP.LIFECYCLE | related | Reproducible builds depend on pinned, declared dependencies. |
| CHANGE_FLOW.BUILD.2 | ASSURANCE.ARTIFACT | realizes | Build once and promote by identity makes the provenance match to source checkable per environment. |
| CHANGE_FLOW.BUILD.2 | ASSURANCE.ARTIFACT.1 | related | Provenance of the promoted artifact is verified before use. |
| CHANGE_FLOW.BUILD.2 | TRANSVERSE.CONFIG | related | Environment configuration lives outside the artifact. |
| CHANGE_FLOW.RELEASE | ASSURANCE.RULES | realizes | A staged pipeline with stated gates is how the rules bind at release. |
| CHANGE_FLOW.RELEASE.2 | ASSURANCE.CONTRACTS.1 | related | A compatibility-promising version number belongs where consumers are many, external or independent. |
| CHANGE_FLOW.RELEASE.3 | EVOLUTION.DECOMMISSION | related | A release toggle's expiry and removal task is a retirement. |
| CHANGE_FLOW.RELEASE.5 | OPERATION.INCIDENTS | related | Deployment is blocked during an incident except for the change that remediates it. |
| CHANGE_FLOW.DEPLOY | ASSURANCE.AVAILABILITY | realizes | Progressive, observable deployment realizes tested, progressive resilience. |
| CHANGE_FLOW.DEPLOY.2 | ASSURANCE.AVAILABILITY | realizes | Progressive rollout with automatic detection and rollback realizes resilience by blast radius. |
| CHANGE_FLOW.DEPLOY.2 | ASSURANCE.AVAILABILITY.3 | related | Production experiments and rollouts share the guardrails held at AVAILABILITY.3. |
| CHANGE_FLOW.DEPLOY.2 | OPERATION.RUNBOOKS | related | The playbook clause of the outage-from-change claim lives with runbooks. |
| CHANGE_FLOW.DEPLOY.3 | TRANSVERSE.ENVIRONMENTS | related | Environment parity and its documented differences meet the environment rules. |
| CHANGE_FLOW.ROLLBACK | ASSURANCE.AVAILABILITY | realizes | A decided, rehearsed way back realizes resilience to a bad change. |
| CHANGE_FLOW.ROLLBACK.3 | ASSURANCE.DATA_INTEGRITY | realizes | Deciding and recording the undo of a data change realizes the guarantees on data. |
| CHANGE_FLOW.ROLLBACK.3 | ASSURANCE.DATA_INTEGRITY.3 | related | A change that can lose data is undone by the prepared and tested restore held there. |
| CHANGE_FLOW.DATA_CHANGE | ASSURANCE.DATA_INTEGRITY | realizes | The procedures here carry out the data-integrity guarantees (rules, scope for bulk and destructive operations, layered protection, sync, old against new). |
| CHANGE_FLOW.DATA_CHANGE.1 | ASSURANCE.ARTIFACT.1 | related | The reviewed script is the deployed unit, so deployed objects match reviewed source. |
| CHANGE_FLOW.DATA_CHANGE.3 | ASSURANCE.DATA_INTEGRITY | realizes | One pipeline and one history for database change realizes what-runs-is-what-was-reviewed. |
| CHANGE_FLOW.DATA_CHANGE.3 | ASSURANCE.SECURITY.6 | related | The authorization stage applies the principle for starting a large-blast-radius job (cross-unit X6). |
| CHANGE_FLOW.DATA_CHANGE.4 | ASSURANCE.DATA_INTEGRITY | realizes | Order and compatibility with running code realize the old-against-new guarantee. |
| CHANGE_FLOW.DATA_CHANGE.4 | ASSURANCE.CONTRACTS | related | A compatibility surface for a shared structure meets the compatibility defined by consumer reach. |
| CHANGE_FLOW.DATA_CHANGE.4 | CONSTRUCTION.HIDING | related | Database access behind a clear layer in code (second clause of the compatibility-layer row). |
| CHANGE_FLOW.DATA_CHANGE.6 | ASSURANCE.DATA_INTEGRITY.2 | related | Bulk work is bounded by the explicit scope the data-integrity decision requires. |
| CHANGE_FLOW.DATA_CHANGE.7 | TRANSVERSE.PRIVACY | related | Masking personal data in a rehearsal copy is here; retention is held there. |
| CHANGE_FLOW.DATA_CHANGE.7 | ASSURANCE.BEHAVIOUR.7 | related | Rehearsal data is a case of test data management. |
| CHANGE_FLOW.DATA_CHANGE.8 | OPERATION.TELEMETRY | related | Watching the target system (lock waits, lag, dead-tuple growth) uses service and resource signals. |
| CHANGE_FLOW.DATA_CHANGE.8 | OPERATION.INCIDENTS | related | A long-running statement is identifiable to its change during an incident. |
| CHANGE_FLOW.DATA_CHANGE.8 | ASSURANCE.SECURITY.6 | related | A large-blast-radius job is a reviewed script whose run is authorized and triggered through the guarded path (cross-unit X6). |
| CHANGE_FLOW.MEASURE | ASSURANCE.RULES | realizes | Outcome measures judge whether the rules produce trustworthy delivery. |
| CHANGE_FLOW.MEASURE | OPERATION.FEEDBACK | related | Delivery outcomes feed the operational feedback loop. |
| CHANGE_FLOW.MEASURE.1 | OPERATION.RELIABILITY | related | Recovery time and change fail rate are reliability outcomes. |
