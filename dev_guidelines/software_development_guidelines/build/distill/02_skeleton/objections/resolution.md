# Resolution of the routing objections

One row per objection (39) and per language-neutrality flag (4). `from` is the node record the row sat on; `to or kept` is the node record it sits on now. A move took the row and its positions out of the source record and put them on the target (an existing L3, no L2 was needed), updated both records and `../routing.md`, and left no restated content. Rule applied (MD-03): the row goes where its subject is the node's stated intent, and the decision node keeps which mechanism guarantees a property while the realization node keeps how it is carried out. No verdicts. All reasons are inferred from the node records and the ledger rows, not checked against the sources.

Totals: 39 objections, 12 moved, 27 kept. 4 flagged rows: 3 carry a language-neutral statement, 1 is marked a stack pointer.

## Objections

| row | raised by | from | to or kept | reason |
|---|---|---|---|---|
| L131 | ASSURANCE | ASSURANCE.ARTIFACT.2 | kept | One cluster with L1063 and L1070 on which mechanism guarantees that what runs was reviewed; CHANGE_FLOW.INTEGRATION has no node on mainline protection to receive it. |
| L118 | ASSURANCE | ASSURANCE.AVAILABILITY.3 | CHANGE_FLOW.DEPLOY.2 | Canary analysis and A/B diff are rollout evaluation, the same family as L161 there. |
| L238 | ASSURANCE | ASSURANCE.DOCS_SYNC.1 | kept | A lever on whether documentation travels with the change, beside L211; no CHANGE_FLOW.BUILD node fits a change-type-dependent pipeline. |
| L229 | ASSURANCE | ASSURANCE.DOCS_SYNC.2 | TRANSVERSE.DOCS.1 | Who writes documentation is authoring practice (TRANSVERSE.DOCS holds authoring, MD-03); closest L3 is the budget of upkeep effort, fit partial. |
| L318 | ASSURANCE | ASSURANCE.DOCS_SYNC.3 | TRANSVERSE.DOCS.3 | The form of the header and inline explanation is how text is written for readers. |
| L313 | ASSURANCE | ASSURANCE.DATA_INTEGRITY.4 | OPERATION.TELEMETRY.1 | Four monitoring signals for scheduled work are a monitoring practice; integrity is carried by L281, L282, L314. |
| L275 | ASSURANCE | ASSURANCE.BEHAVIOUR.8 | kept | Trigger is any defect, not a production incident, and it sits beside L274 to L278; OPERATION.INCIDENTS.2 reviews incidents. |
| L1062 | CHANGE_FLOW | CHANGE_FLOW.INTEGRATION.6 | kept | Attribution is that node's subject; ASSURANCE.SECURITY.6 holds sandbox and credential limits, not attribution. |
| L141 | CHANGE_FLOW | CHANGE_FLOW.REVIEW.4 | kept | That node's intent is the checks that run before the reviewer; ASSURANCE.RULES holds no position on it. |
| L409 | CHANGE_FLOW | CHANGE_FLOW.DATA_CHANGE.4 | kept | A row is not split; the first clause (compatibility layer in a transition) leads and carries the contested positions. |
| L1535 | CONSTRUCTION | CONSTRUCTION.DATA_NOT_CODE.5 | TRANSVERSE.CONFIG.1 | Never hardcoding secrets duplicates L158 there; the node DATA_NOT_CODE.5 held only this row and was removed. |
| L1536 | CONSTRUCTION | CONSTRUCTION.DATA_NOT_CODE.4 | kept | A control character reaching a header value is data turned into protocol structure (injection); no TRANSVERSE.SECURITY or ASSURANCE node holds a parsing rule. |
| L1286 | CONSTRUCTION | CONSTRUCTION.BOUNDARY.4 | ASSURANCE.DATA_INTEGRITY.1 | Constraints that hold whichever code writes is where integrity is placed, with L279 and L1262. |
| L1265 | CONSTRUCTION | CONSTRUCTION.STATE.2 | kept | Lead clause is the normal-form decision beside L1263 and L1264; the guard clause is already stated by L281 in DATA_INTEGRITY.4. |
| L1235 | CONSTRUCTION | CONSTRUCTION.DESIGN.4 | kept | Lead clause sizes the design (10x) and DESIGN.4 names planned replacement in its intent; EVOLUTION.INCREMENTAL.3 is linked. |
| L1236 | EVOLUTION | EVOLUTION.INCREMENTAL.1 | kept | Its subject is step size and feedback; L1208 is itself kept in OWNERSHIP.STANCE.4. |
| L1231 | EVOLUTION | EVOLUTION.DEBT.2 | kept | OPERATION.RELIABILITY holds indicators, objectives and error budget, no node on simplicity. |
| L1007 | EVOLUTION | EVOLUTION.DECISIONS.5 | kept | That node's intent names use in review; CHANGE_FLOW.REVIEW.3 would hold one record-specific item. |
| L208 | OPERATION | OPERATION.FEEDBACK | kept | The node exists for exactly this row; moving it would leave an L2 node empty. |
| L1112 | OPERATION | OPERATION.RECOVERY.2 | OWNERSHIP.SERVICES.3 | What to verify of a rented service's backups and the independent copy sit with L359 and L356 (exit and data terms). |
| L1177 | OPERATION | OPERATION.TELEMETRY.1 | kept | It is instrumentation (which signal is switched on); ASSURANCE.PERFORMANCE.5 states measure before optimising, not which signals exist. |
| L1171 | OPERATION | OPERATION.TELEMETRY.4 | TRANSVERSE.PRIVACY.1 | No personal data in trace context is data minimisation; the correlation node keeps how context is propagated. |
| L1096 | OPERATION | OPERATION.RECOVERY.6 | kept | The claim is who owns durability (the node's intent); the restore-test proof is already stated by L1097 and L1078 in ASSURANCE.AVAILABILITY.4. |
| L1111 | OPERATION | OPERATION.RECOVERY.6 | kept | Upkeep of the recovery plan and runbooks sits with L446 and L448 in OPERATION; DOCS_SYNC.3 holds the generic freshness rule only. |
| L311 | OWNERSHIP | OWNERSHIP.STANCE.2 | CONSTRUCTION.PARADIGM.2 | Where scheduled work runs is the place of logic, named in the CONSTRUCTION.PARADIGM intent. |
| L312 | OWNERSHIP | OWNERSHIP.SELECTION.2 | kept | A row is not split; the lead clause (technology by problem fit) agrees with L023; PARADIGM.1 carries the paradigm by L1526 and points to L312. |
| L330 | OWNERSHIP | OWNERSHIP.STANCE.4 | kept | Contrary position to L038 on one contested question; the judge needs both on one node; DESIGN.2 already points to L330. |
| L1208 | OWNERSHIP | OWNERSHIP.STANCE.4 | kept | Same do-not-build-speculatively claim as L038; its tension with L330 is judged on this node. |
| L341 | OWNERSHIP | OWNERSHIP.CONTAINMENT.4 | CONSTRUCTION.BOUNDARY.5 | Same claim as L1278 and L1279 there (read only what you use); one location for the tolerant-reader decision. |
| L342 | OWNERSHIP | OWNERSHIP.CONTAINMENT.2 | kept | The claim is isolating the system from an external model (the adapter), with L344 and L345; BOUNDARY.1 converts input to a precise type. |
| L358 | OWNERSHIP | OWNERSHIP.SERVICES.4 | kept | A contract term of renting a service; no TRANSVERSE.PRIVACY node holds contract terms. |
| L369 | OWNERSHIP | OWNERSHIP.SERVICES.6 | ASSURANCE.ARTIFACT.1 | Its build levels restate L151 and L1244 there; stated once. |
| L367 | OWNERSHIP | OWNERSHIP.SERVICES.6 | kept | Belongs with L366 (a CI service is supply chain) and L368; CHANGE_FLOW.BUILD has no node on pipeline security. |
| L368 | OWNERSHIP | OWNERSHIP.SERVICES.6 | kept | Same cluster as L366 and L367. |
| L1544 | OWNERSHIP | OWNERSHIP.LIFECYCLE.3 | kept | Content is lockfile review and pinning to earlier versions; the node intent names how a compromise is answered; credential rotation is held by L252 in TRANSVERSE.CONFIG.6. |
| L1545 | OWNERSHIP | OWNERSHIP.LIFECYCLE.4 | kept | The node intent covers the supply chain of the team's own packages; no TRANSVERSE.SECURITY node (programme practice) holds account protection. |
| L263 | TRANSVERSE | TRANSVERSE.ENVIRONMENTS.3 | OWNERSHIP.LIFECYCLE.4 | Pinning and changing build tools is the lifecycle of an adopted tool, with L1074 (own tooling supply chain). |
| L1257 | TRANSVERSE | TRANSVERSE.PRIVACY.3 | kept | L1258 on the same node names the partition drop as the bulk-expiry choice; DATA_CHANGE.6 is how a large change is batched. |
| L1159 | TRANSVERSE | TRANSVERSE.PRIVACY.4 | kept | The notification duty and breach record sit with the impact assessment (L1158); OPERATION.INCIDENTS holds running an incident and is linked. |

## Language-neutrality flags (CONSTRUCTION)

Question per row: does the row's own evidence (its statement and its source entries) support a statement that holds without naming a language construct, apart from a scope condition? Yes: the neutral statement is written into the node's positions as a "Language-neutral statement" bullet; the ledger is untouched. No: the row is marked a stack pointer on its node.

| row | node | outcome | reason |
|---|---|---|---|
| L1501 | CONSTRUCTION.STATE.4 | neutral statement recorded | The source REG-1501 (Goldberg 1991) states a mechanism of floating-point arithmetic with no language-specific rule; the statement holds in any language with such a type. Tolerance point grounded (one T2 source), positive statement inferred. |
| L1518 | CONSTRUCTION.STATE.5 | stack pointer | Its only sources are REG-1514 (the JavaScript import statement), REG-1515 (one bundler's tree-shaking field), REG-1516 (CommonJS loading); no source states the load-order rule neutrally, and the origin says no source states the rule. |
| L1514 | CONSTRUCTION.HIDING.1 | neutral statement recorded | REG-1509 (Cook) is a conceptual distinction between abstract data types and procedural abstraction, independent of a language; "object" is read as the second design, not a construct. One T2 source, no effect evidence. |
| L1288 | CONSTRUCTION.BOUNDARY.3 | neutral statement recorded | REG-1153 separates a logical type from a physical type; the three named technologies are the origin's examples of derived targets. Separation grounded, derivation inferred. |

## Side effects

- `../routing.md`: 12 lines changed to the new L2 node, each with a one-clause reason.
- `../tree_l2.md`: only the `rows` column changed, for the 23 entries (L1 and L2 nodes) whose count moved (recomputed from routing; needed by `../check_routing.py`).
- Branch `branch.md` files: records, row lists, positions, pins and the "Routing objections" section updated; moved rows no longer listed there, kept rows listed with a `resolution` note.
- Scripts: CONSTRUCTION `MAINT_ROWS` gained L311 (now attached there); OWNERSHIP `MAINT_ROWS` lost L311. No other script constant changed; their counts are recomputed from the files.
- ASSURANCE `result.md`: the three pin lines were updated to 241 rows and 3 objections, because `check_branch.py` compares them. The prose and counts of the other six branch `result.md` files and of `../result.md` are stale and not script-checked (not touched).
