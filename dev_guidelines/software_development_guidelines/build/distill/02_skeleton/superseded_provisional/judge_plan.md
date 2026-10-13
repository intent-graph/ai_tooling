# Judge plan: units, order and reading lists

The judges choose, node by node, the most demanding practice that best serves the node's purpose, if the maintainer ratifies the max rule for this graph (the web guideline's rule: positions, forces, decision, rejected). This plan only groups the nodes of `skeleton.md` into units and orders them; it judges nothing. Rows are read in full from `../01_consolidate/claims_ledger.md`, sources resolve through `../01_consolidate/sources.md`. The default team context is not set: each unit needs the maintainer's answer on it before judging (see Open).

Pinned:
- Units: 10. Order: J1 and J2 (OWNERSHIP) and J3 to J5 (ASSURANCE) first, as decision branches, in parallel; then J6 to J9 (realization and cross-cutting), in parallel, each after the decision units it links to; J10 (roll-ups) last.
- Every one of the 170 nodes is in exactly one unit; the units own 460 rows, the ledger has 460.
- Unit sizes (nodes, rows owned): J1 20, 69; J2 18, 50; J3 15, 54; J4 19, 57; J5 18, 40; J6 23, 48; J7 8, 51; J8 22, 61; J9 21, 30; J10 6, 0. No unit exceeds 60 nodes.

## Order

1. J1 to J5, decision branches. Inside a unit, judge the L3 sub-decisions, then roll up to the L2 property or decision node. J1 and J2 may run before J3 to J5 or beside them; J1 and J2 link to no ASSURANCE node; ASSURANCE.SECURITY cites OWNERSHIP.LIFECYCLE.6 (dependency scanning).
2. J6 to J9: each node links back (`Realizes`) to decision nodes; read their verdicts first (listed per unit).
3. J10: roll-ups, after every child is judged.

## Units

### J1 OWNERSHIP: stance, selection, lifecycle

Nodes (20): OWNERSHIP.STANCE, OWNERSHIP.STANCE.1, OWNERSHIP.STANCE.2, OWNERSHIP.STANCE.3, OWNERSHIP.STANCE.4, OWNERSHIP.SELECTION, OWNERSHIP.SELECTION.1, OWNERSHIP.SELECTION.2, OWNERSHIP.SELECTION.3, OWNERSHIP.SELECTION.4, OWNERSHIP.SELECTION.5, OWNERSHIP.SELECTION.6, OWNERSHIP.SELECTION.7, OWNERSHIP.LIFECYCLE, OWNERSHIP.LIFECYCLE.1, OWNERSHIP.LIFECYCLE.2, OWNERSHIP.LIFECYCLE.3, OWNERSHIP.LIFECYCLE.4, OWNERSHIP.LIFECYCLE.5, OWNERSHIP.LIFECYCLE.6

Rows owned, read in full (69): L001-L030, L037, L038, L040-L047, L049-L059, L061-L067, L070-L072, L076, L077, L079, L308, L310-L312, L330

Rows cited by these nodes, owned elsewhere, also read (0): -

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J2 OWNERSHIP: containment, external services, licence

Nodes (18): OWNERSHIP.CONTAINMENT, OWNERSHIP.CONTAINMENT.1, OWNERSHIP.CONTAINMENT.2, OWNERSHIP.CONTAINMENT.3, OWNERSHIP.CONTAINMENT.4, OWNERSHIP.CONTAINMENT.5, OWNERSHIP.SERVICES, OWNERSHIP.SERVICES.1, OWNERSHIP.SERVICES.2, OWNERSHIP.SERVICES.3, OWNERSHIP.SERVICES.4, OWNERSHIP.SERVICES.5, OWNERSHIP.SERVICES.6, OWNERSHIP.LICENCE, OWNERSHIP.LICENCE.1, OWNERSHIP.LICENCE.2, OWNERSHIP.LICENCE.3, OWNERSHIP.LICENCE.4

Rows owned, read in full (50): L031, L033-L036, L039, L068, L069, L073-L075, L078, L340-L351, L353-L378

Rows cited by these nodes, owned elsewhere, also read (0): -

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J3 ASSURANCE: common rules and behaviour

Nodes (15): ASSURANCE.RULES, ASSURANCE.RULES.1, ASSURANCE.RULES.2, ASSURANCE.RULES.3, ASSURANCE.BEHAVIOUR, ASSURANCE.BEHAVIOUR.1, ASSURANCE.BEHAVIOUR.2, ASSURANCE.BEHAVIOUR.3, ASSURANCE.BEHAVIOUR.4, ASSURANCE.BEHAVIOUR.5, ASSURANCE.BEHAVIOUR.6, ASSURANCE.BEHAVIOUR.7, ASSURANCE.BEHAVIOUR.8, ASSURANCE.BEHAVIOUR.9, ASSURANCE.BEHAVIOUR.10

Rows owned, read in full (54): L080-L101, L106, L107, L109-L117, L121-L123, L145, L147, L265-L278, L316, L331

Rows cited by these nodes, owned elsewhere, also read (2): L144, L244

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J4 ASSURANCE: contracts, data integrity, documentation in sync, artifact integrity

Nodes (19): ASSURANCE.CONTRACTS, ASSURANCE.CONTRACTS.1, ASSURANCE.CONTRACTS.2, ASSURANCE.CONTRACTS.3, ASSURANCE.CONTRACTS.4, ASSURANCE.DATA_INTEGRITY, ASSURANCE.DATA_INTEGRITY.1, ASSURANCE.DATA_INTEGRITY.2, ASSURANCE.DATA_INTEGRITY.3, ASSURANCE.DATA_INTEGRITY.4, ASSURANCE.DATA_INTEGRITY.5, ASSURANCE.DOCS_SYNC, ASSURANCE.DOCS_SYNC.1, ASSURANCE.DOCS_SYNC.2, ASSURANCE.DOCS_SYNC.3, ASSURANCE.DOCS_SYNC.4, ASSURANCE.DOCS_SYNC.5, ASSURANCE.DOCS_SYNC.6, ASSURANCE.ARTIFACT

Rows owned, read in full (57): L048, L060, L102-L105, L151, L152, L171, L210-L224, L226-L230, L237-L239, L279-L285, L295, L296, L309, L313-L315, L318-L320, L352, L388, L389, L391, L396, L414-L417

Rows cited by these nodes, owned elsewhere, also read (1): L133

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J5 ASSURANCE: security, performance, availability

Nodes (18): ASSURANCE.SECURITY, ASSURANCE.SECURITY.1, ASSURANCE.SECURITY.2, ASSURANCE.SECURITY.3, ASSURANCE.SECURITY.4, ASSURANCE.SECURITY.5, ASSURANCE.SECURITY.6, ASSURANCE.PERFORMANCE, ASSURANCE.PERFORMANCE.1, ASSURANCE.PERFORMANCE.2, ASSURANCE.PERFORMANCE.3, ASSURANCE.PERFORMANCE.4, ASSURANCE.PERFORMANCE.5, ASSURANCE.AVAILABILITY, ASSURANCE.AVAILABILITY.1, ASSURANCE.AVAILABILITY.2, ASSURANCE.AVAILABILITY.3, ASSURANCE.AVAILABILITY.4

Rows owned, read in full (40): L032, L108, L118-L120, L243-L248, L251, L252, L325, L326, L332-L339, L420-L435, L442

Rows cited by these nodes, owned elsewhere, also read (1): L265

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J6 CHANGE_FLOW: integration, review, build, release, deploy, rollback, measure

Nodes (23): CHANGE_FLOW.INTEGRATION, CHANGE_FLOW.INTEGRATION.1, CHANGE_FLOW.INTEGRATION.2, CHANGE_FLOW.INTEGRATION.3, CHANGE_FLOW.INTEGRATION.4, CHANGE_FLOW.REVIEW, CHANGE_FLOW.REVIEW.1, CHANGE_FLOW.REVIEW.2, CHANGE_FLOW.REVIEW.3, CHANGE_FLOW.BUILD, CHANGE_FLOW.RELEASE, CHANGE_FLOW.RELEASE.1, CHANGE_FLOW.RELEASE.2, CHANGE_FLOW.RELEASE.3, CHANGE_FLOW.RELEASE.4, CHANGE_FLOW.DEPLOY, CHANGE_FLOW.DEPLOY.1, CHANGE_FLOW.DEPLOY.2, CHANGE_FLOW.DEPLOY.3, CHANGE_FLOW.ROLLBACK, CHANGE_FLOW.ROLLBACK.1, CHANGE_FLOW.ROLLBACK.2, CHANGE_FLOW.MEASURE

Rows owned, read in full (48): L124-L144, L146, L148-L150, L153-L157, L159-L167, L169, L170, L172, L173, L288, L297, L298, L387, L390

Rows cited by these nodes, owned elsewhere, also read (3): L208, L290, L328

Verdicts to read first (11): ASSURANCE.ARTIFACT, ASSURANCE.AVAILABILITY, ASSURANCE.AVAILABILITY.4, ASSURANCE.BEHAVIOUR, ASSURANCE.BEHAVIOUR.5, ASSURANCE.DATA_INTEGRITY.5, ASSURANCE.PERFORMANCE.2, ASSURANCE.RULES.1, ASSURANCE.RULES.3, ASSURANCE.SECURITY.2, OWNERSHIP.LIFECYCLE.1

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J7 CHANGE_FLOW: data and schema change

Nodes (8): CHANGE_FLOW.DATA_CHANGE, CHANGE_FLOW.DATA_CHANGE.1, CHANGE_FLOW.DATA_CHANGE.2, CHANGE_FLOW.DATA_CHANGE.3, CHANGE_FLOW.DATA_CHANGE.4, CHANGE_FLOW.DATA_CHANGE.5, CHANGE_FLOW.DATA_CHANGE.6, CHANGE_FLOW.DATA_CHANGE.7

Rows owned, read in full (51): L168, L286, L287, L289-L294, L299-L307, L327, L328, L379-L386, L392-L395, L397-L413, L418, L419

Rows cited by these nodes, owned elsewhere, also read (1): L159

Verdicts to read first (6): ASSURANCE.AVAILABILITY, ASSURANCE.CONTRACTS.2, ASSURANCE.DATA_INTEGRITY, ASSURANCE.DATA_INTEGRITY.4, ASSURANCE.SECURITY.6, CHANGE_FLOW.RELEASE.4

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J8 OPERATION

Nodes (22): OPERATION.RELIABILITY, OPERATION.RELIABILITY.1, OPERATION.RELIABILITY.2, OPERATION.ALERTING, OPERATION.TELEMETRY, OPERATION.TELEMETRY.1, OPERATION.TELEMETRY.2, OPERATION.TELEMETRY.3, OPERATION.TELEMETRY.4, OPERATION.TELEMETRY.5, OPERATION.INCIDENTS, OPERATION.INCIDENTS.1, OPERATION.INCIDENTS.2, OPERATION.INCIDENTS.3, OPERATION.CAPACITY, OPERATION.CAPACITY.1, OPERATION.CAPACITY.2, OPERATION.READINESS, OPERATION.RUNBOOKS, OPERATION.RUNBOOKS.1, OPERATION.RUNBOOKS.2, OPERATION.FEEDBACK

Rows owned, read in full (61): L174-L209, L317, L436-L441, L443-L460

Rows cited by these nodes, owned elsewhere, also read (0): -

Verdicts to read first (6): ASSURANCE.AVAILABILITY, ASSURANCE.AVAILABILITY.2, ASSURANCE.PERFORMANCE, ASSURANCE.PERFORMANCE.5, CHANGE_FLOW.MEASURE, CHANGE_FLOW.RELEASE.4

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J9 TRANSVERSE

Nodes (21): TRANSVERSE.DOCS, TRANSVERSE.DOCS.1, TRANSVERSE.DOCS.2, TRANSVERSE.DOCS.3, TRANSVERSE.DOCS.4, TRANSVERSE.DOCS.5, TRANSVERSE.DOCS.6, TRANSVERSE.SECURITY, TRANSVERSE.SECURITY.1, TRANSVERSE.SECURITY.2, TRANSVERSE.SECURITY.3, TRANSVERSE.SECURITY.4, TRANSVERSE.SECURITY.5, TRANSVERSE.CONFIG, TRANSVERSE.CONFIG.1, TRANSVERSE.CONFIG.2, TRANSVERSE.CONFIG.3, TRANSVERSE.ENVIRONMENTS, TRANSVERSE.ENVIRONMENTS.1, TRANSVERSE.ENVIRONMENTS.2, TRANSVERSE.DESIGN

Rows owned, read in full (30): L158, L225, L231-L236, L240-L242, L249, L250, L253-L264, L321-L324, L329

Rows cited by these nodes, owned elsewhere, also read (0): -

Verdicts to read first (11): ASSURANCE.DOCS_SYNC, ASSURANCE.SECURITY, ASSURANCE.SECURITY.1, ASSURANCE.SECURITY.2, ASSURANCE.SECURITY.5, CHANGE_FLOW.BUILD, CHANGE_FLOW.DEPLOY.2, OWNERSHIP.LIFECYCLE.1, OWNERSHIP.LIFECYCLE.6, OWNERSHIP.SELECTION.1, OWNERSHIP.SERVICES.6

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

### J10 Roll-ups: ROOT and the five L1 nodes

Nodes (6): ROOT, OWNERSHIP, ASSURANCE, CHANGE_FLOW, OPERATION, TRANSVERSE

Rows owned, read in full (0): -

Rows cited by these nodes, owned elsewhere, also read (0): -

Output: one judge record per node with positions, forces, decision, rejected positions and the context that would move it (the web guideline's judge record).

## Open, for the maintainer (before judging)

1. The default context for the max rule: team size, criticality, regulation, shared database, AI coding agents as contributors (variables listed in `skeleton.md`). Without it, the max rule has no reference for choices such as cooldown against immediate updates or hard merge gates.
2. The three scope additions (backup and recovery, technical debt, AI agents as contributors): rows are listed under Awaiting scope in `skeleton.md`; a yes creates nodes and a judging unit for each.
3. The cut itself: confirm the decision and practice split of documentation and security between ASSURANCE and TRANSVERSE, and the two extension nodes (OWNERSHIP.LICENCE, ASSURANCE.ARTIFACT).
