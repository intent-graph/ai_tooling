# Result: routing objections resolved

Files beside this one: `resolution.md` (one row per objection and per flagged row). Each section below reads alone. Certainty words: grounded (a file or a script run states it), inferred (my reading of node records and ledger rows, not checked against the sources), open (undecided, with what was checked).

## L1 headline

Pinned: Objections: 39 raised; moved: 12; kept: 27. Flagged rows (not language-neutral): 4; restated with a neutral statement: 3 (L1501, L1514, L1288); marked stack pointer: 1 (L1518). Scripts: ASSURANCE check_branch.py: PASS; CHANGE_FLOW check_branch.py: PASS; CONSTRUCTION check_branch.py: PASS; EVOLUTION check_branch.py: PASS; OPERATION check_branch.py: PASS; OWNERSHIP check_branch.py: PASS; TRANSVERSE check_branch.py: PASS; check_routing.py: PASS.

- Twelve rows now sit on the branch whose node intent states their subject; the 27 kept rows stay because the source node's intent names them, the row cannot be split, or the target has no node that fits (grounded: scripts prove 814 of 814 rows routed once, every branch attached 100%).
- The move rule was MD-03: the decision node keeps which mechanism guarantees a property, the realization node keeps how it is carried out; duplicates of one claim were brought to one node (inferred: a reading, not a verdict on any practice).
- Out-of-scope files touched, for the scripts to pass: `tree_l2.md` row counts, three pin lines of the ASSURANCE `result.md` (grounded: listed in `resolution.md`).

## L2 claims

Pinned: Objections: 39 raised; moved: 12; kept: 27. Flagged rows: 4; neutral statement: 3; stack pointer: 1. All eight scripts: PASS (ASSURANCE, CHANGE_FLOW, CONSTRUCTION, EVOLUTION, OPERATION, OWNERSHIP, TRANSVERSE check_branch.py, and check_routing.py).

- Moves by cause (grounded, from `resolution.md`):
  - Same claim already held on the target: L118 (canary, DEPLOY.2), L341 (read what you use, BOUNDARY.5), L369 (build levels, ARTIFACT.1), L1535 (hardcoded secrets, CONFIG.1), L1286 (constraints, DATA_INTEGRITY.1).
  - Target intent names the subject: L311 (place of logic, PARADIGM.2), L1171 (minimisation, PRIVACY.1), L313 (monitoring signals, TELEMETRY.1), L263 and L1112 (adopted tool and rented service terms, OWNERSHIP), L229 and L318 (authoring practice, TRANSVERSE.DOCS).
- Kept by cause (inferred): source intent names the row (L208, L1096, L1111, L1007, L1062, L141, L1544, L1545); row is one cluster with others there (L131, L367, L368, L330, L1208, L342, L1257); row cannot be split (L312, L409); no node on the target fits (L238, L358, L1536, L1231).
- Flagged rows: L1501, L1514, L1288 have a neutral statement in their own evidence (REG-1501, REG-1509, REG-1153), recorded as a bullet in the node positions; L1518 is a stack pointer because REG-1514 to REG-1516 are all one language's module system and bundler (grounded for the sources, inferred for the outcome).
- Side effects: node CONSTRUCTION.DATA_NOT_CODE.5 removed (it held only L1535); CONSTRUCTION and OWNERSHIP script `MAINT_ROWS` adjusted for L311; fit is partial for L229 (to DOCS.1, budget) and L238 stays for lack of a better node (inferred, open: a judge may prefer another L3).

## L3 full

Pinned: Objections: 39 raised; moved: 12; kept: 27. Flagged rows: 4; neutral statement: 3; stack pointer: 1. All eight scripts: PASS.

Script lines after the edits (grounded, run once at the end):

- ASSURANCE: nodes 54 (L1 1, L2 9, L3 44); rows routed 241, attached 241, unattached 0; routing objections 3; `check_branch.py: PASS`.
- CHANGE_FLOW: nodes 43; rows 117 attached, 0 unattached; objections 3; PASS.
- CONSTRUCTION: nodes 48 (was 49); 87 rows attached once; objections 3; PASS.
- EVOLUTION: nodes 33; 53 rows attached; objections 3; PASS.
- OPERATION: nodes 39; 109 rows attached; PASS (objections kept in branch.md: 4).
- OWNERSHIP: nodes 36; 133 rows attached; objections 9; PASS.
- TRANSVERSE: nodes 36; 74 rows attached; objections 2; PASS.
- `check_routing.py`: 814 rows routed once, counts agree with `tree_l2.md`; PASS.

Rows per branch before and after: OWNERSHIP 134 to 133, ASSURANCE 243 to 241, CONSTRUCTION 87 to 87, CHANGE_FLOW 116 to 117, OPERATION 110 to 109, EVOLUTION 53, TRANSVERSE 71 to 74; total 814.

Moved rows, from to to (grounded, `resolution.md` holds the reasons):

- L118: ASSURANCE.AVAILABILITY.3 to CHANGE_FLOW.DEPLOY.2.
- L229: ASSURANCE.DOCS_SYNC.2 to TRANSVERSE.DOCS.1. L318: ASSURANCE.DOCS_SYNC.3 to TRANSVERSE.DOCS.3.
- L313: ASSURANCE.DATA_INTEGRITY.4 to OPERATION.TELEMETRY.1.
- L1535: CONSTRUCTION.DATA_NOT_CODE.5 (removed) to TRANSVERSE.CONFIG.1. L1286: CONSTRUCTION.BOUNDARY.4 to ASSURANCE.DATA_INTEGRITY.1.
- L1112: OPERATION.RECOVERY.2 to OWNERSHIP.SERVICES.3. L1171: OPERATION.TELEMETRY.4 to TRANSVERSE.PRIVACY.1.
- L311: OWNERSHIP.STANCE.2 to CONSTRUCTION.PARADIGM.2. L341: OWNERSHIP.CONTAINMENT.4 to CONSTRUCTION.BOUNDARY.5. L369: OWNERSHIP.SERVICES.6 to ASSURANCE.ARTIFACT.1.
- L263: TRANSVERSE.ENVIRONMENTS.3 to OWNERSHIP.LIFECYCLE.4.

Kept rows (27): L131, L238, L275, L1062, L141, L409, L1536, L1265, L1235, L1236, L1231, L1007, L208, L1177, L1096, L1111, L312, L330, L1208, L342, L358, L367, L368, L1544, L1545, L1257, L1159.

Open points (what I checked: node records of source and target, the ledger rows, the source register for REG-1501, REG-1509, REG-1514 to REG-1516, REG-1153):
- Whether L330 and L1208 belong with design effort (CONSTRUCTION.DESIGN.2) rather than with L038 is a close call; kept to hold the contested positions on one node (inferred).
- L1112 leaves OPERATION.RECOVERY.2 without a rented-service backup position; the node links to the new location (inferred that this is the better split).
- Stale and not touched: prose and counts in the six other branch `result.md` files and in `../result.md`; the judge briefs should be built from `branch.md` and `routing.md`.
