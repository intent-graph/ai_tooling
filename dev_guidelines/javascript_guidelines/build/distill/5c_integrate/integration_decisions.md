These are the choices made while joining the eight branches. Rows named in the branch texts below as `CONTROL-011` and
`DEFENSE-091` now live in `CONTROL-078` and `SUBSET-051` (I1, I2). Provenance of every link: `5c_integrate/link_resolution.md`.

### I1. Process-end principle: one row, principle kept as intent (P5 merge, flagged by CONTROL)

- Decision: the rows `CONTROL-011` (ASYNC-C05, philosophy node `CONTROL.LIFECYCLE`) and `CONTROL-078` (RUNTIME-C37, defaults node
  `PIG-JS.CONTROL.PROCESS.2`) state one principle (overlap O02: after an uncaught exception the state is undefined, so clean up
  synchronously, end, and let a supervisor restart). They are merged into `CONTROL-078` with both claim ids. `CONTROL.LIFECYCLE` keeps the
  language-neutral principle as intent and no row of its own; `PIG-JS.CONTROL.PROCESS.2` now states only the Node rendering and links up
  with a `refines` inter link.
- Rejected: leaving both rows (the principle is stated twice); putting the merged row on `CONTROL.LIFECYCLE` (the statement names the Node
  hooks, so it fails the language-swap test). Wins: the second, if the maintainer wants every principle node to carry its own evidence;
  then move `CONTROL-078` to `CONTROL.LIFECYCLE` and restore the old intent of `PROCESS.2`.
- Grounds: both claims cite the same single T1 source (SRC-082, unrestricted). Epistemic state unchanged: `known | unvalidated: single T1 source`.

### I2. Own-property read: one rule on the owner node (P5 merge, found at integration)

- Decision: `SUBSET-051` (LANG-C55) and `DEFENSE-091` (RUNSEC-C07) both decide `Object.hasOwn` over `hasOwnProperty` and no `for...in` on
  untrusted keys (overlap O15, owner LANG-C55). Merged into `SUBSET-051` on `PIG-JS.SUBSET.OBJECTS.6` with both claim ids and
  agreement `consensus` (RUNSEC-C07 has two T1 grounds, SRC-078 unrestricted for slot 06 and SRC-139). `PIG-JS.DEFENSE.PROTOTYPE.1` keeps the
  nested-write, merge and `__proto__` rules and links to `OBJECTS.6` with `requires`.
- Rejected: keeping the rule in both nodes; moving it to DEFENSE (SUBSET also applies it to trusted keys). Wins: DEFENSE as owner if the
  guideline is read as two standalone documents; then restore `DEFENSE-091` and drop the merge.

### I3. Shared facts linked, not merged (P5 by link)

- Held once, linked from the other node: the run-once fact of ES modules (`PIG-JS.SUBSET.STRICTNESS.2`, linked from
  `PIG-JS.STRUCTURE.LOADING.1`); the shallow-freeze fact (hub `PIG-JS.SUBSET.MUTATION.1`, linked from `PIG-JS.STRUCTURE.SURFACE.3` and
  `PIG-JS.DEFENSE.PROTOTYPE.3`); framework security facts (held in `PIG-JS.DEFENSE.DOM.6`, linked from
  `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE` and `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`, as the CONTROL, DEFENSE and DEPENDENCIES
  branches proposed); secrets in package contents (`PIG-JS.DEPENDENCIES.PUBLISH.2` requires `PIG-JS.DEFENSE.SECRETS.5`); the single shared
  thread (`DEFENSE.HOST.1` requires `CONTROL.SCHEDULING`); type check as evidence not proof (`CONTRACTS.STATIC.2` refines
  `VERIFICATION.STATIC_BASELINE.3`).
- Kept as a conflict, not merged: built-ins (`PIG-JS.SUBSET.OBJECTS.5` conflicts `PIG-JS.DEFENSE.PROTOTYPE.3`): two purposes (predictable
  language, hardening) disagree on one practice, scope separates them.
- Rule applied: merge when two nodes state the same intent; link when two nodes share a fact. The rows are evidence and stay in place.
- Residue at statement level, left as written: `DEFENSE-097` repeats the refuted deep-freeze belief that `SUBSET-056` rejects, and
  `STRUCTURE-024` repeats the run-once fact of `SUBSET-006` inside a rule about repeatable work.
- Cross-branch text similarity of the 589 branch rows peaks at 0.22 (token Jaccard): no other duplicated statement exists.

### I4. DEFENSE.INJECTION is not split

- Decision: `DEFENSE.INJECTION` (philosophy) and `PIG-JS.DEFENSE.INJECTION` (defaults) stay one L2 node each, six L3 classes below.
- Why the split is not clean: the natural cut is INSTRUCTION (strings as code, commands, queries, serialized data: 34 claims, plus 3 on the
  defaults L3 node) against LOCATION (paths, destinations: 24 claims). It would make DEFENSE seven L2 children in both graphs, over the
  limit of six; renumber the nodes of 61 claims, the INJECTION inter links, three undecided uids (`INJECTION.4.4`, `.5.3`, `.6.4`) and the judge records; and class 5 (serialized data)
  sits on the boundary (revived behaviour, but also a format that crosses a boundary). No class is large: claims per class are 10, 4, 13, 12, 7, 12.
- Rejected: the split. Wins: if the maintainer folds PROTOTYPE (14 claims) into one of the two halves to stay at six L2 children, or accepts seven.
- Grounds: grounded for the counts (ledger), inferred for the cleanliness judgment.

### I5. T3 relabel and what was checked

- Relabelled `known | unvalidated: single T3 source` to `risky | unvalidated: single T3 source`: `PIG-JS.STRUCTURE.LOADING.6` (barrel files,
  SRC-315 measurement; the T1 MDN page documents aggregation and recommends nothing), `PIG-JS.STRUCTURE.DIRECTION.2` (SRC-313, the rule's
  own documentation), `VERIFICATION.TEST_SUITE.3` (SRC-321), `VERIFICATION.TEST_STABILITY.3` (SRC-320).
- Checked against `build/audit/source_register.md` (11 T3 sources) and not relabelled, because a T1 or T2 ground sits beside the T3 one:
  `PIG-JS.DEFENSE.DOM.2.2` (ASVS requirement is T1, only the mechanism is T3), `PIG-JS.DEFENSE.ORIGIN.4`, `PIG-JS.STRUCTURE.SURFACE.3`,
  `STRUCTURE.NAMING.2` (T2 grounds), `PIG-JS.DEFENSE.INJECTION.4.2`, the SUBSET nodes that cite Airbnb beside MDN or ESLint.
- The tension the STRUCTURE branch noted (the plan says T3 alone never makes a node `known`, the brief's format would allow it) is closed by the
  5c rule: the four nodes are `risky`.

### I6. Cross-branch links: 101 proposals resolved

- 72 retargeted to a uid, 10 flipped (the sentence made the proposer the dependent), 2 retyped (CONTRACTS Q11 and Q12, `refines` and `requires`
  became `dataflow`), 9 mirror proposals folded into another link, 6 dropped as moot, 2 turned into planned boundary links. 83 links result from them
  (13 philosophy, 68 defaults, 2 defaults-to-philosophy); 3 more were added at integration (2 philosophy, 1 defaults-to-philosophy: I1, I3).
- Corrections to proposals that rested on a wrong premise: CONTRACTS Q6 (SUBSET lists no enum or namespaces), Q13 (DEFENSE lists no
  mass-assignment node), CONTROL 8 (the API-shape cluster is in `PIG-JS.CONTRACTS.SIGNATURE`, not in STRUCTURE).
- Open, grounded as gaps in the target trees: VERIFICATION defaults hold no tool-neutral gate node, so the type-check, audit, secret-scan and bundling
  gates all point at `PIG-JS.VERIFICATION.LINT.2` (coarse); RUNTIME holds no node on the Node release lifecycle; no DEFENSE node on mass assignment.

### I7. Shape of the trees

- Every node has zero or two to six children, except the two roots (eight L1 branches, given) and seven defaults nodes with a single child:
  `PIG-JS.CONTROL.PROMISES.4`, `PIG-JS.CONTROL.ERRORS.2`, `PIG-JS.CONTROL.SCHEDULING.2`, `PIG-JS.DEPENDENCIES.UPDATE.1`,
  `PIG-JS.DEPENDENCIES.UPDATE.3`, `PIG-JS.RUNTIME.MEMORY.6` (each holds an undecided sub-question as its only child, kept visible on purpose) and
  `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` (its one child is the platform baseline; the four frameworks sit in the parent's decision).
- Decision: kept as written. Alternative for the assembly step: one node per short-list candidate under `FRAMEWORK_SHORTLIST`, grounded in
  rows DEPENDENCIES-048 to DEPENDENCIES-075.

### I8. Conventions normalized

- DEFENSE and DEPENDENCIES wrote the IG separator as a bare `|` in epistemic cells and DEFENSE abbreviated ledger rows (`028-034`): cells
  rejoined with `\|`, the ledger-rows column derived from the merged ledger for every node (the branch columns agreed with the ledger everywhere).
- Link ids that looked like node uids (`P1`, `Q1`, `X1`, `I1`) are plain numbers; the checker would count them as nodes. RUNTIME's `graph:uid`
  prefix on link sources is dropped; defaults-to-philosophy targets all carry `js-philosophy:`.
- Judge records are copied in the layout each branch used (bold records, headed records, tables); only headings are demoted.
