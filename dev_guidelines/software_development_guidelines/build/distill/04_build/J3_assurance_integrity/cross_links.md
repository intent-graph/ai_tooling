# Cross links: unit J3_assurance_integrity

Links whose other endpoint is outside the unit, for the linker. Direction: source depends on, refines, or points to target. Types: `requires`, `refines`, `see`, `index` (the target holds the practice, MD-03), `realizes`. Source: the "Links" line of each judged record (`build/distill/03_judge/J3_assurance_integrity/judged.md`).

| source uid | target uid | type | intent sentence |
|---|---|---|---|
| ASSURANCE.DATA_INTEGRITY | CHANGE_FLOW.DATA_CHANGE | index | The procedures (batching, rehearsal) are held there; this node holds which mechanism guarantees integrity. |
| ASSURANCE.DATA_INTEGRITY | OPERATION.RECOVERY | index | Backup practice is held there. |
| ASSURANCE.DATA_INTEGRITY.1 | CONSTRUCTION.BOUNDARY | requires | Validation at the edge stays in force beside the rules declared in the store. |
| ASSURANCE.DATA_INTEGRITY.1 | CHANGE_FLOW.DATA_CHANGE | index | Procedures for changing data and schema are held there. |
| ASSURANCE.DATA_INTEGRITY.2 | ASSURANCE.RULES.3 | refines | A gate with an explicit, visible override: the opt-in and the migration-lint assertion are overrides of that kind. |
| ASSURANCE.DATA_INTEGRITY.2 | CHANGE_FLOW.DATA_CHANGE | index | The data-change procedure that carries the guarded operations is held there. |
| ASSURANCE.DATA_INTEGRITY.3 | OPERATION.RECOVERY | index | Backup practice, the second protection layer, is held there. |
| ASSURANCE.DATA_INTEGRITY.3 | OPERATION.RECOVERY.2 | see | How long backups are kept is set there. |
| ASSURANCE.DATA_INTEGRITY.3 | TRANSVERSE.PRIVACY.2 | see | Retention periods for personal data, backup copies included, are set there. |
| ASSURANCE.DATA_INTEGRITY.3 | TRANSVERSE.PRIVACY.3 | see | Erasure of data in backups is held there. |
| ASSURANCE.DATA_INTEGRITY.3 | ASSURANCE.AVAILABILITY.4 | requires | The restore that undoes a destructive change is proven there. |
| ASSURANCE.DATA_INTEGRITY.3 | TRANSVERSE.PRIVACY | requires | The privacy and retention obligations bound the retention window and the form of deletion (the judge writes "TRANSVERSE (privacy and retention)"; the L2 uid is inferred). |
| ASSURANCE.DATA_INTEGRITY.4 | OPERATION.TELEMETRY.8 | requires | Detection queries and refreshes are scheduled work whose duration, failure, backlog and missed runs are signalled there (node created by unit J7 at graph build, cross-unit fix X12). |
| ASSURANCE.DATA_INTEGRITY.4 | CHANGE_FLOW.DATA_CHANGE | index | Procedures for introducing derived structures are held there. |
| ASSURANCE.DATA_INTEGRITY.5 | CHANGE_FLOW.DATA_CHANGE | requires | Rehearsal and rollout of the data change are held there; the checks here run inside them. |
| ASSURANCE.DOCS_SYNC | TRANSVERSE.DOCS | index | Authoring and organisation of documentation are held there; this node holds the mechanism that keeps it in sync. |
| ASSURANCE.DOCS_SYNC | ASSURANCE.CONTRACTS.3 | see | One source of description for interfaces is held there. |
| ASSURANCE.DOCS_SYNC | ASSURANCE.RULES.3 | see | Gates that cannot be skipped: the documentation gate is one. |
| ASSURANCE.DOCS_SYNC | ASSURANCE.RULES.5 | see | One bar and evidence for every change: documentation is part of that evidence. |
| ASSURANCE.DOCS_SYNC.1 | TRANSVERSE.DOCS | index | Authoring and organisation practice is held there. |
| ASSURANCE.DOCS_SYNC.2 | ASSURANCE.RULES.3 | requires | The documentation gate is a gate with a recorded, visible override. |
| ASSURANCE.DOCS_SYNC.2 | ASSURANCE.RULES.4 | requires | The waiver is granted by the reviewer who approves the change, independent of its author. |
| ASSURANCE.DOCS_SYNC.2 | TRANSVERSE.DOCS | see | Authoring and organisation practice is held there. |
| ASSURANCE.DOCS_SYNC.3 | ASSURANCE.CONTRACTS.3 | requires | One origin per fact for interface descriptions is held there. |
| ASSURANCE.DOCS_SYNC.3 | OPERATION.RECOVERY | see | Upkeep of the recovery plan and runbooks sits there (L1111). |
| ASSURANCE.DOCS_SYNC.3 | TRANSVERSE.DOCS | index | Authoring and organisation practice is held there. |
| ASSURANCE.SECURITY | TRANSVERSE.SECURITY | index | Programme practice is held there; this node holds verification and enforcement. |
| ASSURANCE.SECURITY | ASSURANCE.RULES.3 | see | Gates that cannot be skipped: security gates follow it. |
| ASSURANCE.SECURITY | ASSURANCE.RULES.5 | see | One bar and evidence for every change. |
| ASSURANCE.SECURITY | ASSURANCE.ARTIFACT | see | Integrity of the produced artifact complements verification of the code. |
| ASSURANCE.SECURITY.1 | TRANSVERSE.SECURITY | requires | The risk model and programme that set the depth are held there. |
| ASSURANCE.SECURITY.2 | ASSURANCE.RULES.1 | requires | Block or advise, under a stated false-alarm budget, is decided there. |
| ASSURANCE.SECURITY.2 | ASSURANCE.RULES.2 | requires | Placement of a check by feedback speed is decided there. |
| ASSURANCE.SECURITY.2 | ASSURANCE.RULES.3 | requires | Gates that cannot be skipped, with an audited override, are decided there. |
| ASSURANCE.SECURITY.2 | CHANGE_FLOW.BUILD | realizes | The pipeline stages that run the checks are built there. |
| ASSURANCE.SECURITY.3 | ASSURANCE.BEHAVIOUR.3 | requires | The test levels the security tests sit in are decided there. |
| ASSURANCE.SECURITY.3 | ASSURANCE.BEHAVIOUR.6 | see | Adequacy and the coverage decision (no coverage floor; security-relevant code included) are held there (cross-unit fix X1). |
| ASSURANCE.SECURITY.4 | ASSURANCE.BEHAVIOUR.2 | refines | The static layer is refined here for security weaknesses, with their scheduled and noise-handling practice. |
| ASSURANCE.SECURITY.5 | OWNERSHIP.LIFECYCLE | see | The inventory of consumed components stays in the dependency lifecycle. |
| ASSURANCE.SECURITY.5 | TRANSVERSE.CONFIG | index | Configuration and secrets practice (custody, rotation of a found secret) is held there; the judge writes "TRANSVERSE (configuration and secrets)", the L2 uid is inferred. |
| ASSURANCE.SECURITY.6 | TRANSVERSE.SECURITY | requires | The security programme sets the access and automation policy that the tooling enforces. |
| ASSURANCE.SECURITY.6 | CHANGE_FLOW.INTEGRATION | requires | Attribution of every automated change (L1062) is held there. |
| ASSURANCE.SECURITY.6 | ASSURANCE.RULES.4 | requires | The accountable person or named group who authorizes and triggers a large-blast-radius run. |
| ASSURANCE.SECURITY.6 | CHANGE_FLOW.DATA_CHANGE.3 | see | The database procedure, an authorization stage of the one pipeline, is held there (cross-unit fix X6). |
| ASSURANCE.SECURITY.6 | CHANGE_FLOW.DATA_CHANGE.8 | see | Running and watching a production data job (cross-unit fix X6). |
| ASSURANCE.SECURITY.6 | ASSURANCE.ARTIFACT.2 | see | The protected mainline binds every actor, automated ones included. |
| ASSURANCE.SECURITY.7 | ASSURANCE.AVAILABILITY.4 | requires | The ability to restore is proven there. |
| ASSURANCE.SECURITY.7 | ASSURANCE.BEHAVIOUR.8 | see | Defect classes that survive review are held there. |
| ASSURANCE.SECURITY.7 | OPERATION.INCIDENTS | see | A found defect that reached operation is handled there. |
