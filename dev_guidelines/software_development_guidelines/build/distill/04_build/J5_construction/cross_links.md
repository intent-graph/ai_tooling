# J5_construction: cross links for the linker

Links whose other endpoint is outside the unit, plus those whose source is the L1 node CONSTRUCTION (built in the TOP batch, not in this batch). Columns: source uid, target uid, link type, intent sentence. The linker applies each as `link.create` with `shape: {type: <type>}`. A target created by another unit's batch exists only after that batch is applied.

| source | target | type | intent |
|---|---|---|---|
| CONSTRUCTION | ASSURANCE.CONTRACTS | realizes | CONSTRUCTION realizes ASSURANCE.CONTRACTS: this branch holds the form a boundary takes, via CONSTRUCTION.BOUNDARY (L1 node, built in the TOP batch; listed for completeness). |
| CONSTRUCTION | ASSURANCE.DATA_INTEGRITY.1 | realizes | CONSTRUCTION realizes ASSURANCE.DATA_INTEGRITY.1 via BOUNDARY.1, BOUNDARY.4 and PARADIGM.2 (L1 node, TOP batch; listed for completeness). |
| CONSTRUCTION | ASSURANCE.RULES.3 | realizes | CONSTRUCTION realizes ASSURANCE.RULES.3 via DEPENDENCY_DIRECTION.2 (L1 node, TOP batch; listed for completeness). |
| CONSTRUCTION | ASSURANCE.SECURITY | related | CONSTRUCTION relates to ASSURANCE.SECURITY (L1 node, TOP batch; listed for completeness). |
| CONSTRUCTION | TRANSVERSE.SECURITY | related | CONSTRUCTION relates to TRANSVERSE.SECURITY (L1 node, TOP batch; listed for completeness). |
| CONSTRUCTION | TRANSVERSE.CONFIG | related | CONSTRUCTION relates to TRANSVERSE.CONFIG (L1 node, TOP batch; listed for completeness). |
| CONSTRUCTION.DESIGN | OWNERSHIP.STANCE.4 | related | DESIGN relates to OWNERSHIP.STANCE.4: speculative building is held there, sizing to present need here. |
| CONSTRUCTION.DESIGN | EVOLUTION.INCREMENTAL | related | DESIGN relates to EVOLUTION.INCREMENTAL: replacement part by part is decided there. |
| CONSTRUCTION.DESIGN.1 | OWNERSHIP.STANCE.4 | related | DESIGN.1 relates to OWNERSHIP.STANCE.4: structure for probable use where reversal is costly. |
| CONSTRUCTION.DESIGN.2 | OWNERSHIP.STANCE.4 | related | DESIGN.2 relates to OWNERSHIP.STANCE.4: consistent with the maintainer's structure-for-probable-use row held there. |
| CONSTRUCTION.DESIGN.3 | ASSURANCE.RULES.3 | requires | DESIGN.3 requires ASSURANCE.RULES.3: mechanically checkable constraints are blocking checks. |
| CONSTRUCTION.DESIGN.4 | EVOLUTION.INCREMENTAL | related | DESIGN.4 relates to EVOLUTION.INCREMENTAL: rewrite against replacement is decided there. |
| CONSTRUCTION.DESIGN.4 | OWNERSHIP.STANCE.4 | related | DESIGN.4 relates to OWNERSHIP.STANCE.4: parts cheap to change are sized to the present need. |
| CONSTRUCTION.DESIGN.4 | OPERATION.CAPACITY | related | DESIGN.4 relates to OPERATION.CAPACITY: the horizon signal is a capacity measurement. |
| CONSTRUCTION.SYSTEM_SHAPE | ASSURANCE.CONTRACTS.1 | realizes | SYSTEM_SHAPE realizes in code the unit boundaries that ASSURANCE.CONTRACTS.1 verifies. |
| CONSTRUCTION.SYSTEM_SHAPE | ASSURANCE.CONTRACTS.2 | realizes | SYSTEM_SHAPE realizes in code the unit boundaries that ASSURANCE.CONTRACTS.2 verifies. |
| CONSTRUCTION.SYSTEM_SHAPE | OPERATION.RELIABILITY | related | SYSTEM_SHAPE relates to OPERATION.RELIABILITY: fault isolation and distribution cost. |
| CONSTRUCTION.SYSTEM_SHAPE.2 | OPERATION.RELIABILITY | related | SYSTEM_SHAPE.2 relates to OPERATION.RELIABILITY: failure handling is part of the distribution premium. |
| CONSTRUCTION.SYSTEM_SHAPE.2 | CHANGE_FLOW.DEPLOY | related | SYSTEM_SHAPE.2 relates to CHANGE_FLOW.DEPLOY: automated deployment is part of the distribution premium. |
| CONSTRUCTION.SYSTEM_SHAPE.3 | ASSURANCE.CONTRACTS.1 | realizes | SYSTEM_SHAPE.3 realizes ASSURANCE.CONTRACTS.1: independent deployability, with the coordinated breaking change as its exception. |
| CONSTRUCTION.SYSTEM_SHAPE.3 | ASSURANCE.CONTRACTS.2 | realizes | SYSTEM_SHAPE.3 realizes ASSURANCE.CONTRACTS.2: compatibility across the boundary is verified there. |
| CONSTRUCTION.SYSTEM_SHAPE.3 | OWNERSHIP.SERVICES.2 | related | SYSTEM_SHAPE.3 relates to OWNERSHIP.SERVICES.2: the consumer side of provider evolution. |
| CONSTRUCTION.HIDING.1 | OWNERSHIP.CONTAINMENT | related | HIDING.1 relates to OWNERSHIP.CONTAINMENT: hiding a decision behind a boundary is containment. |
| CONSTRUCTION.HIDING.4 | ASSURANCE.DATA_INTEGRITY.1 | related | HIDING.4 relates to ASSURANCE.DATA_INTEGRITY.1: one owner per schema. |
| CONSTRUCTION.BOUNDARY | ASSURANCE.CONTRACTS | realizes | BOUNDARY realizes ASSURANCE.CONTRACTS: it holds the form a boundary takes, that node how compatibility is verified. |
| CONSTRUCTION.BOUNDARY | ASSURANCE.DATA_INTEGRITY.1 | realizes | BOUNDARY realizes ASSURANCE.DATA_INTEGRITY.1: edge validation. |
| CONSTRUCTION.BOUNDARY.1 | ASSURANCE.DATA_INTEGRITY.1 | realizes | BOUNDARY.1 realizes ASSURANCE.DATA_INTEGRITY.1: edge validation in addition to store constraints. |
| CONSTRUCTION.BOUNDARY.1 | OWNERSHIP.CONTAINMENT.2 | related | BOUNDARY.1 relates to OWNERSHIP.CONTAINMENT.2: third-party responses are parsed at the wrapper. |
| CONSTRUCTION.BOUNDARY.1 | OWNERSHIP.CONTAINMENT.4 | related | BOUNDARY.1 relates to OWNERSHIP.CONTAINMENT.4: data from external destinations is untrusted. |
| CONSTRUCTION.BOUNDARY.3 | ASSURANCE.CONTRACTS.1 | realizes | BOUNDARY.3 realizes ASSURANCE.CONTRACTS.1: the version or change-log form follows consumer reach. |
| CONSTRUCTION.BOUNDARY.3 | ASSURANCE.CONTRACTS.3 | realizes | BOUNDARY.3 realizes ASSURANCE.CONTRACTS.3: types are derived from where the team records the chain starts. |
| CONSTRUCTION.BOUNDARY.3 | EVOLUTION.DECOMMISSION | related | BOUNDARY.3 relates to EVOLUTION.DECOMMISSION: contract lifecycle statuses (deprecated, retired). |
| CONSTRUCTION.BOUNDARY.4 | ASSURANCE.CONTRACTS.1 | realizes | BOUNDARY.4 realizes ASSURANCE.CONTRACTS.1: the published interface over stored data. |
| CONSTRUCTION.BOUNDARY.4 | ASSURANCE.DATA_INTEGRITY.1 | related | BOUNDARY.4 relates to ASSURANCE.DATA_INTEGRITY.1: store constraints and the published layer. |
| CONSTRUCTION.BOUNDARY.5 | ASSURANCE.CONTRACTS | related | BOUNDARY.5 relates to ASSURANCE.CONTRACTS: removal and evolution follow CONTRACTS.1 and the input and output split follows CONTRACTS.3. |
| CONSTRUCTION.BOUNDARY.6 | ASSURANCE.DATA_INTEGRITY.1 | related | BOUNDARY.6 relates to ASSURANCE.DATA_INTEGRITY.1: a violated store constraint maps to a stable contract error. |
| CONSTRUCTION.BOUNDARY.6 | OPERATION.INCIDENTS | related | BOUNDARY.6 relates to OPERATION.INCIDENTS: failure detail goes to the log for investigation. |
| CONSTRUCTION.STATE | ASSURANCE.DATA_INTEGRITY.4 | related | STATE relates to ASSURANCE.DATA_INTEGRITY.4: the sync plan for copies is settled there. |
| CONSTRUCTION.STATE.1 | ASSURANCE.DATA_INTEGRITY.4 | related | STATE.1 relates to ASSURANCE.DATA_INTEGRITY.4: a managed copy needs that sync plan. |
| CONSTRUCTION.STATE.2 | ASSURANCE.DATA_INTEGRITY.4 | related | STATE.2 relates to ASSURANCE.DATA_INTEGRITY.4: denormalised redundancy is guarded by that sync plan. |
| CONSTRUCTION.STATE.3 | ASSURANCE.DATA_INTEGRITY.4 | related | STATE.3 relates to ASSURANCE.DATA_INTEGRITY.4: a cache is derived data needing a plan. |
| CONSTRUCTION.DEPENDENCY_DIRECTION | ASSURANCE.RULES.3 | related | DEPENDENCY_DIRECTION relates to ASSURANCE.RULES.3: mechanical enforcement of boundaries. |
| CONSTRUCTION.DEPENDENCY_DIRECTION.2 | ASSURANCE.RULES.3 | realizes | DEPENDENCY_DIRECTION.2 realizes ASSURANCE.RULES.3: a declared layering is a blocking check. |
| CONSTRUCTION.NAMING.2 | TRANSVERSE.DOCS | related | NAMING.2 relates to TRANSVERSE.DOCS: one name per concept holds in documents too. |
| CONSTRUCTION.PARADIGM | OWNERSHIP.SELECTION.2 | related | PARADIGM relates to OWNERSHIP.SELECTION.2: the paradigm half of the maintainer row is held there. |
| CONSTRUCTION.PARADIGM | ASSURANCE.DATA_INTEGRITY.1 | related | PARADIGM relates to ASSURANCE.DATA_INTEGRITY.1: invariants across writers are declared in the store. |
| CONSTRUCTION.PARADIGM.1 | OWNERSHIP.SELECTION.2 | related | PARADIGM.1 relates to OWNERSHIP.SELECTION.2: paradigm choice is by intent. |
| CONSTRUCTION.PARADIGM.2 | OWNERSHIP.STANCE | related | PARADIGM.2 relates to OWNERSHIP.STANCE (row L308). |
| CONSTRUCTION.PARADIGM.2 | ASSURANCE.DATA_INTEGRITY.1 | related | PARADIGM.2 relates to ASSURANCE.DATA_INTEGRITY.1: the settled split by kind of logic. |
| CONSTRUCTION.PARADIGM.2 | ASSURANCE.BEHAVIOUR.7 | related | PARADIGM.2 relates to ASSURANCE.BEHAVIOUR.7: logic in the store is tested against a real store. |
| CONSTRUCTION.PARADIGM.2 | OPERATION.TELEMETRY.8 | related | PARADIGM.2 relates to OPERATION.TELEMETRY.8 (cross-unit fix X12): scheduled work is monitored through its signals; TELEMETRY.8 is created by the J7 batch. |
| CONSTRUCTION.DATA_NOT_CODE | ASSURANCE.SECURITY.2 | related | DATA_NOT_CODE relates to ASSURANCE.SECURITY.2: security findings and their enforcement. |
| CONSTRUCTION.DATA_NOT_CODE | ASSURANCE.SECURITY.6 | related | DATA_NOT_CODE relates to ASSURANCE.SECURITY.6: least privilege as the second layer. |
| CONSTRUCTION.DATA_NOT_CODE | TRANSVERSE.SECURITY | related | DATA_NOT_CODE relates to TRANSVERSE.SECURITY: programme practice. |
| CONSTRUCTION.DATA_NOT_CODE.2 | ASSURANCE.SECURITY | related | DATA_NOT_CODE.2 relates to ASSURANCE.SECURITY: least privilege of the store account. |
| CONSTRUCTION.DATA_NOT_CODE.3 | OWNERSHIP.CONTAINMENT.4 | related | DATA_NOT_CODE.3 relates to OWNERSHIP.CONTAINMENT.4: redirect and destination allowlists. |
| CONSTRUCTION.DATA_NOT_CODE.3 | ASSURANCE.SECURITY | related | DATA_NOT_CODE.3 relates to ASSURANCE.SECURITY. |
| CONSTRUCTION.PROCESS | CHANGE_FLOW.DEPLOY | related | PROCESS relates to CHANGE_FLOW.DEPLOY: cheap replacement makes releases cheap. |
| CONSTRUCTION.PROCESS | OPERATION.CAPACITY | related | PROCESS relates to OPERATION.CAPACITY: capacity is added by adding processes. |
| CONSTRUCTION.PROCESS.1 | CHANGE_FLOW.DEPLOY | related | PROCESS.1 relates to CHANGE_FLOW.DEPLOY: graceful stop makes a release lose no work. |
| CONSTRUCTION.PROCESS.2 | OPERATION.INCIDENTS | related | PROCESS.2 relates to OPERATION.INCIDENTS: the supervisor's restart policy and crash-loop alert belong to OPERATION. |
