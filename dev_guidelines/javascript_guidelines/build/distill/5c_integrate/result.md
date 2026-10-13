# Step 5c result: integration of the eight branches

## L1 headline

The eight consolidated branches are one ledger (608 claims in 587 rows, 0 dropped), one skeleton (378 nodes in two graphs, 307 links, 10 planned boundary links) and one review file (98 branch decisions plus 8 integration decisions, 13 undecided nodes), ready for IntentGraph assembly; certainty: grounded for counts, tree shape, link endpoints and the checker run, inferred for the two P5 merges, the 101 link resolutions and the decision not to split DEFENSE.INJECTION.

Pinned:
- Claims in 608 (SUBSET 61, CONTRACTS 52, CONTROL 82, STRUCTURE 57, DEFENSE 195, DEPENDENCIES 84, VERIFICATION 43, RUNTIME 34). Ledger rows in 589, out 587: placed 608 claims in 559 claim rows (514 hold one claim, 45 hold several) plus 28 claim-less folklore rows; merged at 5c: 2 rows (`CONTROL-011` into `CONTROL-078`, `DEFENSE-091` into `SUBSET-051`, all claim ids kept); dropped 0. Rows by graph 114 philosophy, 473 defaults; by role decision 349, fact 137, rejected 56, acceptable-when 35, deferred 10. Claim RUNSEC-C07 now sits in a SUBSET row (the one claim that changed branch).
- Nodes, js-philosophy 108: ROOT 1, L1 8, L2 40, L3 59. pig-js-defaults 270: PIG-JS.ROOT 1, L1 8, L2 43, L3 185, L4 33. Total 378; 188 defaults nodes hold a decision, 13 are undecided. Per branch (philosophy / defaults): SUBSET 7/35, CONTRACTS 10/37, CONTROL 6/35, STRUCTURE 17/34, DEFENSE 21/58, DEPENDENCIES 23/28, VERIFICATION 17/22, RUNTIME 6/20.
- Links: philosophy 33 inside branches + 15 across branches + 23 to python-kb-philosophy; defaults 78 inside + 68 across branches + 90 to js-philosophy; 10 planned boundary links to `web-app-philosophy` and `pig-web-defaults` (not created). 101 branch proposals resolved: 72 retargeted to a uid, 10 flipped, 2 retyped, 9 mirrors folded, 6 dropped as moot, 2 turned into planned links.
- Normalization: 2 P5 merges (process-end principle on `PIG-JS.CONTROL.PROCESS.2`; own-property read on `PIG-JS.SUBSET.OBJECTS.6`); framework security facts held once in `PIG-JS.DEFENSE.DOM.6` and linked from `FRAMEWORK_EVIDENCE` and `FRAMEWORK_SHORTLIST`; `DEFENSE.INJECTION` not split (a seventh L2 child of DEFENSE, over the limit of six); 4 nodes relabelled `risky` (T3 alone): `PIG-JS.STRUCTURE.LOADING.6`, `PIG-JS.STRUCTURE.DIRECTION.2`, `VERIFICATION.TEST_SUITE.3`, `VERIFICATION.TEST_STABILITY.3`.
- Decisions for review (`decisions_for_review.md`): 8 at integration (I1 to I8) and 98 from the branches (SUBSET 10, CONTRACTS 11, CONTROL 14 weighty plus 39 single-source rows, STRUCTURE 12, DEFENSE 16, DEPENDENCIES 9, VERIFICATION 16, RUNTIME 10). Most contestable: `== null` forbidden (SUBSET), TypeScript as the type layer (CONTRACTS), framework short list (DEPENDENCIES), no `DEFENSE.INJECTION` split (I4).
- Undecided nodes, 13: `PIG-JS.CONTROL.PROMISES.4.1`, `PIG-JS.CONTROL.ERRORS.2.1`, `PIG-JS.CONTROL.SCHEDULING.2.1`, `PIG-JS.STRUCTURE.DIRECTION.3` with `STRUCTURE.DIRECTION.2`, `PIG-JS.DEFENSE.DOM.2.3`, `PIG-JS.DEFENSE.INJECTION.4.4`, `.5.3`, `.6.4`, `PIG-JS.DEPENDENCIES.UPDATE.1.1`, `.UPDATE.3.1`, `.PUBLISH.4`, `PIG-JS.RUNTIME.MEMORY.6.1`.
- Restriction demotions, as the branches reported them (56): SUBSET 7 (LANG-C07, C08, C14, C16 to acceptable-when; LANG-C13, C25, C27 to fact), CONTRACTS 8, CONTROL 6, STRUCTURE 4, DEFENSE 19 (7 overstepping, 12 vendor facts held at fact), DEPENDENCIES 6, VERIFICATION 5, RUNTIME 1. The 5c merges and relabels add none; both merged rows were checked against the register (SRC-082, SRC-078, SRC-139 unrestricted for their use).
- Checker, `python3 build/distill/check_ledger.py` (exit 0):
  - `claims in: 608; placed: 608; missing 0; duplicated 0; unknown 0`
  - `ledger rows by graph: {'js-philosophy': 114, 'pig-js-defaults': 473}; by role: {'rejected': 56, 'fact': 137, 'decision': 349, 'acceptable-when': 35, 'deferred': 10}; skeleton nodes: 378`

## L2 claims

- Grounded: the three files hold what the brief asks. `claims_ledger.md` has one table in branch order; `skeleton.md` has both roots, the eight subtrees per graph, all links with cross-branch proposals resolved to uids, the inter links, the planned boundary links and the judge records; `decisions_for_review.md` has the integration decisions, the branch decisions batched by branch, then the undecided nodes.
- Grounded: placement. 608 claims in, 608 placed once; no row names an absent node; the checker counts exactly 378 skeleton nodes, equal to the 107 plus 269 nodes the branches wrote plus the two roots.
- Grounded: the branch skeletons' `ledger rows` columns agreed with the branch ledgers for every node; the integrated column is derived from the merged ledger, so DEFENSE ranges (`028-034`) and RUNTIME's `see` references are now full row ids.
- Grounded: tree shape. No orphan node; every node has zero or two to six children except the two roots (eight L1 branches, given) and seven defaults nodes with one child (six undecided placeholders, plus `FRAMEWORK_SHORTLIST` whose only child is the platform baseline). UIDs follow the format (keyword only at L2, numeric from L3); no node name holds a forbidden character.
- Grounded: links. All 307 link endpoints exist; no duplicate pair, no reverse pair, no cycle among `requires` links; the 23 python targets are uids of `python_kb_philosophy.yaml`.
- Inferred: P5 merge 1, the process-end principle. Rows `CONTROL-011` (ASYNC-C05) and `CONTROL-078` (RUNTIME-C37, overlap O02) became one row on `PIG-JS.CONTROL.PROCESS.2`; `CONTROL.LIFECYCLE` keeps the principle as intent without a row of its own; `PROCESS.2` now states only the Node rendering.
- Inferred: P5 merge 2, found at integration. `SUBSET-051` (LANG-C55) and `DEFENSE-091` (RUNSEC-C07, overlap O15) decided one rule in two nodes; merged on `PIG-JS.SUBSET.OBJECTS.6`, with `PIG-JS.DEFENSE.PROTOTYPE.1` linking to it. This is the one claim moved from DEFENSE to SUBSET.
- Grounded: no other duplicate exists. Token similarity between rows of different branches peaks at 0.22 and between node intents at 0.22; the remaining overlaps are shared facts, so they are links (run-once, shallow freeze, framework security facts, secrets in packages, single thread), and the built-ins disagreement stays a `conflicts` link.
- Grounded: framework security facts are held once, in `PIG-JS.DEFENSE.DOM.6` (6.1 escape hatches, 6.2 default encoding, 6.3 htmx), and linked: `DOM.6` dataflow `FRAMEWORK_EVIDENCE`, `FRAMEWORK_SHORTLIST` requires `DOM.6`. Open: the evidence matrix still lacks a per-candidate security-model node in DEPENDENCIES.
- Inferred: `DEFENSE.INJECTION` stays whole (I4). The clean cut would be INSTRUCTION (strings as code, commands, queries, serialized data: 34 claims) against LOCATION (paths, destinations: 24), but it makes DEFENSE seven L2 children in both graphs; claims per class are 10, 4, 13, 12, 7, 12, so no class is oversized.
- Grounded: T3 relabel. The four nodes carrying `known | unvalidated: single T3 source` are now `risky | ...`; the register has 11 T3 sources and every other node citing one has a T1 or T2 ground beside it (checked claim by claim).
- Inferred: link resolution. 101 proposals: 72 retargeted, 10 flipped because the sentence made the proposer the dependent, 2 retyped, 9 mirror proposals folded into their twin, 6 dropped as moot with a reason, 2 planned. Three corrections: CONTRACTS Q6 (SUBSET lists no enum or namespaces), Q13 (DEFENSE lists no mass-assignment node), CONTROL 8 (the API-shape cluster is in CONTRACTS.SIGNATURE).
- Open: VERIFICATION defaults hold no tool-neutral gate node; the type-check, audit, secret-scan and bundling gates all link to `PIG-JS.VERIFICATION.LINT.2`, which is coarse. RUNTIME holds no node on the Node release lifecycle. A defaults node per short-list candidate could be added at assembly.
- Open: the 13 undecided nodes each name the evidence that would settle them in `decisions_for_review.md`; the branches' open facts that are not nodes (type predicate bodies, schema library ranking, overloads, mutation testing, other CI hosts) stay in the branch decision texts.
- Not done: no independent review pass (the instructions send reviews to a separate agent); nothing committed, nothing pushed; the branch folders are untouched.

## L3 full

### Files written (all under `build/distill/`)

| file | content |
|---|---|
| `claims_ledger.md` | one table, 587 rows, branch order, header with the two merge notes |
| `skeleton.md` | both graphs: roots, eight subtrees each, links, inter links, planned links, judge records |
| `decisions_for_review.md` | I1 to I8, then the eight branches' decisions, then the undecided nodes |
| `5c_integrate/result.md` | this file |
| `5c_integrate/integrate.py` | the integration, re-runnable from the guideline root: `python3 build/distill/5c_integrate/integrate.py` |
| `5c_integrate/integration_decisions.md` | the text of I1 to I8, read by the script |
| `5c_integrate/link_resolution.md` | every one of the 101 proposals with its disposition |
| `5c_integrate/stats.json` | the counts quoted here |

### Ledger accounting

| branch | claims in | rows in | rows out | claim ids in rows out | note |
|---|---|---|---|---|---|
| SUBSET | 61 | 70 | 70 | 62 | takes RUNSEC-C07 |
| CONTRACTS | 52 | 52 | 52 | 52 | |
| CONTROL | 82 | 86 | 85 | 82 | `CONTROL-011` folded into `CONTROL-078` |
| STRUCTURE | 57 | 48 | 48 | 57 | |
| DEFENSE | 195 | 182 | 181 | 194 | gives RUNSEC-C07 away, `DEFENSE-091` folded |
| DEPENDENCIES | 84 | 77 | 77 | 84 | |
| VERIFICATION | 43 | 43 | 43 | 43 | |
| RUNTIME | 34 | 31 | 31 | 34 | |
| total | 608 | 589 | 587 | 608 | 559 claim rows, 28 claim-less folklore rows |

Placed, merged, dropped: all 608 claims placed once; 47 claims were already merged into shared rows by the branches (43 rows), two more rows are merged now (4 claims in 2 rows); dropped 0.

### Node counts, per graph, level and branch

| branch | philosophy L1 | L2 | L3 | total | defaults L1 | L2 | L3 | L4 | total |
|---|---|---|---|---|---|---|---|---|---|
| SUBSET | 1 | 6 | 0 | 7 | 1 | 6 | 28 | 0 | 35 |
| CONTRACTS | 1 | 3 | 6 | 10 | 1 | 6 | 30 | 0 | 37 |
| CONTROL | 1 | 5 | 0 | 6 | 1 | 6 | 25 | 3 | 35 |
| STRUCTURE | 1 | 6 | 10 | 17 | 1 | 6 | 27 | 0 | 34 |
| DEFENSE | 1 | 6 | 14 | 21 | 1 | 6 | 32 | 19 | 58 |
| DEPENDENCIES | 1 | 6 | 16 | 23 | 1 | 6 | 19 | 2 | 28 |
| VERIFICATION | 1 | 5 | 11 | 17 | 1 | 3 | 10 | 8 | 22 |
| RUNTIME | 1 | 3 | 2 | 6 | 1 | 4 | 14 | 1 | 20 |
| branches | 8 | 40 | 59 | 107 | 8 | 43 | 185 | 33 | 269 |
| roots (L0) | | | | 1 | | | | | 1 |
| graph | 8 | 40 | 59 | 108 | 8 | 43 | 185 | 33 | 270 |

### Links

| set | count |
|---|---|
| js-philosophy, inside branches | 33 |
| js-philosophy, across branches (resolved) | 15 (13 from proposals, 2 added) |
| js-philosophy to python-kb-philosophy | 23 |
| pig-js-defaults, inside branches | 78 |
| pig-js-defaults, across branches (resolved) | 68 |
| pig-js-defaults to js-philosophy | 90 (87 within a branch, 3 across) |
| planned boundary links to the web-architecture graphs | 10 (5 DEFENSE, 3 DEPENDENCIES, 2 from proposals) |

Added at integration, not proposed by a branch: `CONTRACTS.STATIC.2` refines `VERIFICATION.STATIC_BASELINE.3`; `DEFENSE.HOST.1` requires `CONTROL.SCHEDULING`; `PIG-JS.CONTROL.PROCESS.2` refines `js-philosophy:CONTROL.LIFECYCLE`.

Dropped proposals (reasons in `link_resolution.md`): CONTRACTS Q9; STRUCTURE philosophy 2 and 3, defaults 5; DEFENSE 8; DEPENDENCIES 7.

### Normalizations

- Edited intents and states (every edit, all at integration): `PIG-JS.CONTROL.PROCESS.2` intent; `CONTROL.LIFECYCLE` state; `PIG-JS.DEFENSE.PROTOTYPE.1` intent; `PIG-JS.SUBSET.OBJECTS.6` state; `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE` state (pointer to `DOM.6.2`); the four `risky` states.
- Written new: the two root nodes `ROOT` (name "Solid JavaScript") and `PIG-JS.ROOT`, intents from the L0 of `target_hierarchy.md` and the plan's Goal; both `known` (maintainer decision).
- DEFENSE and DEPENDENCIES had bare `|` in epistemic cells; rejoined with `\|`. Link ids `P1`, `Q1`, `X1`, `I1` of CONTRACTS match the checker's node pattern and are now plain numbers.
- Judge records copied unchanged (headings demoted), with three integration notes (CONTROL, SUBSET, DEFENSE).

### Restriction demotions as reported by the branches

- SUBSET: to acceptable-when LANG-C07, C08, C14, C16 (Google position only); to fact LANG-C13, C25, C27; kept but flagged LANG-C22, C54, STRUCT-C46, QUALITY-C19.
- CONTRACTS (8): TYPES-C25 to fact; TYPES-C35, C38, C42, C43, C46 to fact or status only; RUNSEC-C42 ground dropped; STRUCT-C47 default not recorded; STRUCT-C48 to C52 scoped to declared APIs.
- CONTROL (6): ASYNC-C52 a dated position; ASYNC-C50, C49, C51 to fact; ASYNC-C21 to acceptable-when; RUNTIME-C12 illustration only.
- STRUCTURE (4): STRUCT-C60 to fact, STRUCT-C32 to acceptable-when, STRUCT-C29 blanket position not adopted, STRUCT-C54 to rejected.
- DEFENSE (19): overstepping DOMSEC-C07, C14, C21, C28, RUNSEC-C11, SRVSEC-C11, C13; vendor facts held at fact FW-C01, C03, C05, C06, C08, C09, C10, C11, C12, C18, C19, C20.
- DEPENDENCIES (6): SUPPLY-C42, C16, C20, FW-C07, FW-C13 to fact; SRC-154 range position to acceptable-when inside SUPPLY-C06; FW-C36 to C40 not adopted as rules.
- VERIFICATION (5): rows 010, 015, 030, 034 acceptable-when, row 033 partial; restriction overrides flagged on rows 008, 009, 018 (Google positions, now `risky`).
- RUNTIME (1): STRUCT-C43 to acceptable-when; RUNTIME-C22 flag part left open.

### Method and checks

- The script reads the branch files only; every output is regenerated by one run. Checks run: the checker above; tree integrity (parents, child counts, uid grammar, name characters); link endpoints, duplicates, reverse pairs, `requires` cycles; node-row columns against ledgers; every proposal accounted for (the script fails otherwise); no home paths or private names in the outputs.
- Certainty: the placement, counts and structure checks are grounded (run). The direction of the 10 flipped links, the target chosen for each retargeted proposal and the two merges are judgment on the proposal sentences and on the nodes' intents; the maintainer can read each in `link_resolution.md` and `decisions_for_review.md` (I1, I2, I6).
