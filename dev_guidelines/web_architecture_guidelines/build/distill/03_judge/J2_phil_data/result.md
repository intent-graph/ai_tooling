# Result: J2 web-app-philosophy DATA judged

## L1 headline

All 5 DATA nodes of `web-app-philosophy` are judged and decided. Each realizes the settled allocation of J1 under the shared-database default (MD-03), and none re-decides it. The adversarial review's 3 findings on this unit are applied, none rejected, together with the cross-branch resolutions.
- **Organize**: each fact is stored once. Third normal form is the floor; Boyce-Codd, fourth and fifth normal form apply where they apply, and a dependency a Boyce-Codd split loses is enforced by a constraint trigger.
- **Guard**: every rule a constraint can express is declared. The rest are checked in writer functions or constraint triggers under Serializable isolation or a lock. One business operation is one function call, with cross-domain composition inside the database. The consistency model is stated per operation.
- **Maintain**: structure changes only through versioned migrations applied by automation. An incompatible change keeps every running consumer working, and the live database is the truth for structure.
- **Derive**: store the minimum and derive the rest. Every stored derived value is a copy with a sync plan and a drift guard, kept by a trigger wherever another writer exists.

There are no maintainer questions. Per-user read visibility stays awaiting the maintainer under J1's question, with J1's default recorded word for word: each backend filters for now, and read functions are acceptable when a rule must hold for two or more backends. The doctrine row on breaking function-API changes is cited here and judged and counted only by J6. One structure gap is reported: under MD-03, no philosophy node realizes the database function API.

Pinned:
- Nodes judged: 5 of 5 (DATA, DATA.ORGANIZE, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE); the 12 owned rows read in full and all cited.
- Decided 5, undecided 0. DATA.GUARD carries one clause it does not settle: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (J1's Q1). Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0. No genuine trade-off between forces a DATA node serves; `questions.md` says none.
- DATA.ORGANIZE after review: third normal form is the floor; Boyce-Codd, fourth and fifth normal form apply where they apply; a dependency lost by a Boyce-Codd decomposition is enforced by a constraint trigger under Serializable or a lock; stopping at third normal form is acceptable only when every candidate key is a single column, and no multi-valued facts.
- Verdicts against the maintainer doctrine: 0 new. Inherited from J1 and realized in DATA.GUARD: declarative constraints required, not optional (partly against L471). L517 is cited, not counted: J6 owns and counts that departure once for both graphs ("deployed together" only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract). DATA.MAINTAIN keeps the principle: an incompatible change keeps every running consumer working.
- Conflicts with J1 placements: 0.
- Review: 3 of the DATA-branch review's 13 findings concern this unit (B1, M4, m8); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3. J6's M2 followed through in DATA.DERIVE for consistency.
- Gaps: (1) structure: under MD-03 no philosophy node realizes the database function API (RECORD.2) or the database share of ACT.1, and DATA.GUARD and DATA.MAINTAIN have no link to the per-role layer of GUARD.3 or to ACT.4; links and one node proposed, nothing created. (2) Collation, left open "under DATA" by J1: no row grounds a choice; handed open to J6 (PIG-WEB.DATA.ORGANIZE.3). (3) Data lifecycle (retention, deletion, recovery) has no principle-level row; it exists only at PIG-WEB.DATA.MAINTAIN.2 to .5. (4) The drift check between the live catalogue and the migration history is inferred; no source read. (5) The Boyce-Codd claims (same kind of anomaly; dependency loss) rest on standard theory, not on a ledger row.

## L2 claims

### Review fixes

- B1, X1: DATA.GUARD's read-visibility clause now records J1's default word for word, read functions included where a rule must hold for two or more backends, plus the consequence that reporting and operator roles see every row they may SELECT; the notation is `undecided: awaiting maintainer, ...`.
- M4: DATA.ORGANIZE no longer claims the higher normal forms cost nothing. A dependency lost by a Boyce-Codd decomposition is enforced by a constraint trigger, the exemption is narrowed to single-column candidate keys, and the source is cited for fourth and fifth normal form only.
- m8, X2: DATA.MAINTAIN drops its `conflict: narrows L517` and keeps the principle; the L517 verdict is J6's alone.
- X3: one operation is one function call, and cross-domain composition happens inside the database (DATA.GUARD).
- M2 follow-through (J6's finding, for consistency): DATA.DERIVE's same-transaction copies are kept by a trigger, by the writer function only when the source admits no other writer.

### Claims

- **DATA** (roll-up): the database is the system of record and holds everything that must hold whoever touches the data (RECORD.1, MD-03). It organizes, guards, maintains and derives, as below. State: `known | gap` (structure gap 1, lifecycle gap 3).
- **DATA.ORGANIZE**: the rule is "each fact once" (L038), and the normal forms are its tests.
  - Third normal form is the floor for every table (L037, L469 MAINT).
  - Boyce-Codd, fourth and fifth normal form apply where they apply (L039; fourth and fifth per SRC-254, Boyce-Codd inferred).
  - Where a Boyce-Codd decomposition loses a dependency, the lost dependency is enforced by a constraint trigger under Serializable or a lock (inferred). That cost is an integrity cost, and the trigger is what keeps both "each fact once" and "every rule enforced".
  - Stopping at third normal form is acceptable only when every candidate key is a single column, and no multi-valued facts.
  - Denormalization is a derived copy, governed by DATA.DERIVE, and needs L469's sync plan recorded before it is built.
  - One-to-one attributes follow L470 (MAINT, max): a nullable column by default, split only for cardinality, permission boundary, own lifecycle or blast radius, never for sparsity.
  - Collation has no row and is handed open to J6.
  - State: `known | unvalidated | gap: collation`.
- **DATA.GUARD**: the database guards consistency in six ways, each realizing J1's GUARD.2, GUARD.5, RULES.5 and ACT.1.
  1. Every rule a declarative constraint can express is declared, constraints are named, and they are required (L485, L040, L473, L174, L175, L495).
  2. Other multi-row rules, lost dependencies included, live in the writer function or a constraint trigger, under Serializable with retry or a lock, with the isolation asserted. The default isolation level belongs to J6.
  3. One business operation is one transaction in one function call (L584). Backends never compose calls; a function may call another domain's published functions in the same transaction, and only direct access to another domain's tables is forbidden (X3).
  4. The writer function detects conflicts against an expected version, and no lock is held across think time (L475).
  5. A correctness lock is fenced by the store: row version, unique constraint or row lock (L476). A lock outside the database only saves duplicate work.
  6. The consistency model is stated per operation, never as "CP" or "AP" (L043). Reports on a replica accept snapshot anomalies.
  - Per-role grants realize GUARD.3's database layer. Row-level security is not a default (MD-01).
  - Per-user read visibility: `undecided: awaiting maintainer`, with J1's default: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Reporting and operator roles see every row they may SELECT unless their own role is restricted.
  - The partial verdict against L471 is inherited from J1.
  - State: `known | conflict: L471 (inherited) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database | unvalidated`.
- **DATA.MAINTAIN**:
  - There is one path of change: versioned migrations applied by automation, the same way in every environment (L046, L519). Long data jobs are versioned scripts run by a human under L545's checklist.
  - Migrations are the origin of change, and the live database is the truth for structure, from which documentation and models are generated (L474). A difference between them is a defect to reconcile. The check is inferred and handed to J6.
  - An incompatible change keeps every running consumer working: expand, migrate, contract, for tables and the function API alike (L047, L192). Under MD-03 this is the only route that keeps every running consumer working (inferred).
  - L517 is cited, not judged: J6 decides and counts it once for both graphs.
  - Conventions evolve forward only (L474).
  - State: `known | unvalidated | gap: lifecycle`.
- **DATA.DERIVE**: store the minimum and derive the rest (L488 MAINT, L072).
  - Predicates such as eligibility are computed, not stored.
  - A derived outcome is its own row, and a state label is flipped last (L597).
  - A stored derived value is a copy kept only when measured cost requires it, in DERIVE.1's order: generated column, then same-transaction maintenance by trigger (the writer function only when the source admits no other writer), then cache table with stated staleness. Each copy has L469's sync plan and L533's drift guard.
  - State: `known | unvalidated` (the order is inherited as inferred from J1).

Pinned:
- Nodes judged: 5 of 5 (DATA, DATA.ORGANIZE, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE); the 12 owned rows read in full and all cited.
- Decided 5, undecided 0. DATA.GUARD carries one clause it does not settle: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (J1's Q1). Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0. No genuine trade-off between forces a DATA node serves; `questions.md` says none.
- DATA.ORGANIZE after review: third normal form is the floor; Boyce-Codd, fourth and fifth normal form apply where they apply; a dependency lost by a Boyce-Codd decomposition is enforced by a constraint trigger under Serializable or a lock; stopping at third normal form is acceptable only when every candidate key is a single column, and no multi-valued facts.
- Verdicts against the maintainer doctrine: 0 new. Inherited from J1 and realized in DATA.GUARD: declarative constraints required, not optional (partly against L471). L517 is cited, not counted: J6 owns and counts that departure once for both graphs ("deployed together" only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract). DATA.MAINTAIN keeps the principle: an incompatible change keeps every running consumer working.
- Conflicts with J1 placements: 0.
- Review: 3 of the DATA-branch review's 13 findings concern this unit (B1, M4, m8); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3. J6's M2 followed through in DATA.DERIVE for consistency.
- Gaps: (1) structure: under MD-03 no philosophy node realizes the database function API (RECORD.2) or the database share of ACT.1, and DATA.GUARD and DATA.MAINTAIN have no link to the per-role layer of GUARD.3 or to ACT.4; links and one node proposed, nothing created. (2) Collation, left open "under DATA" by J1: no row grounds a choice; handed open to J6 (PIG-WEB.DATA.ORGANIZE.3). (3) Data lifecycle (retention, deletion, recovery) has no principle-level row; it exists only at PIG-WEB.DATA.MAINTAIN.2 to .5. (4) The drift check between the live catalogue and the migration history is inferred; no source read. (5) The Boyce-Codd claims (same kind of anomaly; dependency loss) rest on standard theory, not on a ledger row.

## L3 full

### Review fixes

Source: `../review_data/review.md` (13 findings on the DATA branch, 3 on this unit) and `../cross_branch_fixes.md` (X1 to X7). Every fix was checked against its evidence before applying; none was found wrong. Applied: 3. Rejected: 0.

| id | node | change in `records.md` / `questions.md` |
|---|---|---|
| B1 + X1 | DATA.GUARD | The clause records J1's default word for word: "A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends". The former "If the maintainer chooses read functions instead" framing, which treated B as excluded until answered, is removed. X1's notation and its consequence (roles that may SELECT the base tables see every row, comments included, unless restricted) are added. X1's "verified actor" is glossed: verified by the backend, a claim to the database (J1 R1-3). `questions.md` restates the default in plain terms. |
| M4 | DATA.ORGANIZE | Decision: "normalize to Boyce-Codd, fourth and fifth normal form where they apply; where a Boyce-Codd decomposition loses a dependency, the lost dependency is enforced by a constraint trigger under DATA.GUARD's rule (Serializable or a lock)". "Costs nothing there" is removed. The exemption is narrowed to "every candidate key is a single column, and no multi-valued facts", with Kent's all-key fifth-normal-form example as the reason. SRC-254 is cited for fourth and fifth normal form only; the Boyce-Codd claim is marked inferred. DATA.GUARD's procedural rules now name lost dependencies. |
| m8 + X2 | DATA.MAINTAIN | The clause is kept as a principle-level requirement, "an incompatible change keeps every running consumer working"; `conflict: narrows L517` is removed; the P3' rejection becomes "not judged here", citing J6's verdict with X2's condition word for word. The pinned block no longer flags a narrowing. |
| X3 | DATA.GUARD | X3's text added to "Partial change": one operation one call, no composition by backends, cross-domain composition through published functions inside the database. |
| M2 (J6 finding, follow-through) | DATA.DERIVE | Same-transaction maintenance by trigger; the writer function only when the source table admits no other writer, so the philosophy level matches PIG-WEB.DATA.DERIVE.1. |

X4 to X7 do not touch this unit.

### Files

- `records.md`: one judge record per node, with positions (ledger ids and source tiers), forces, decision, rejected positions with their winning condition, the placements realized, links proposed, and the proposed `epistemic_state`. Passages changed by the review name their finding or resolution id.
- `questions.md`: none. It says where the three non-questions went: J1's Q1, the L517 verdict held by J6, and the structure gaps.

### Method

- Read in order: the target hierarchy and selection rule; MD-01 to MD-03; the J2 section of the judge plan; J1's allocation matrix (revision 2) in full, and in J1's records the default context, the access paths and the records of RECORD.1, RECORD.3, GUARD.2, GUARD.3, GUARD.5 and DERIVE.1; the skeleton's DATA nodes and every intentlink touching them; the 12 owned ledger rows in full (L037-L039, L043, L046, L047, L469, L470, L474, L476, L485, L488) and the sources they cite (tiers resolved in `sources.md`).
- Also read, because a placement or a sibling realization cites them: L040, L045, L072, L168-L170, L174-L176, L189-L198, L204, L218, L471, L473, L475, L486, L489, L491, L495, L497, L517, L519, L520, L531-L533, L540, L543, L545, L549, L568, L569, L573, L577, L584, L596, L597, L625-L627, L632. No research result was opened: no owned row was too compressed to judge.
- Review pass: `../review_data/review.md` and `../cross_branch_fixes.md` in full; J1's Q1 "If unanswered, the graph records" re-read; L037 and L039 re-read for M4.
- Purpose per node: integrity of stored data (the DATA role in the selection rule). A position that serves another force (read performance, speed of change) is kept as "acceptable when <condition>", not as a trade-off, because the DATA nodes do not own those forces.

### Verdicts, with what decides each

- **DATA.ORGANIZE**:
  - The max is the purpose of normalization (L038), not a fixed form. Stopping at third normal form where Boyce-Codd, fourth or fifth form applies leaves the anomaly the rule exists to prevent.
  - The higher forms are not free: a Boyce-Codd decomposition can lose a dependency, which then needs a constraint trigger. Under the max rule both "each fact once" and "every rule enforced" are kept (M4).
  - The research row that calls the higher forms rarely considered (L039, a T3 source) describes frequency, not merit.
  - L470 is adopted as both MAINT and max. No row argues the opposite (splitting for sparsity); L470 names that position only to reject it.
  - Nullable columns must state their meaning: grounded in L485 and in L040's note citing the Postgres documentation. The co-presence CHECK is inferred from L485 and L174.
- **DATA.GUARD**:
  - Each of the six ways is a J1 verdict realized: GUARD.2 for constraints and procedural rules under isolation or a lock, RULES.5 and ACT.1 for one transaction per operation (with X3's cross-domain rule), GUARD.5 for version detection.
  - The node's own rows add two things: consistency stated per operation, not per store (L043), and fencing by the store (L476).
  - Access guarding (per-role grants) is outside the node's worded question but within the PIG-WEB nodes that refine it (PIG-WEB.DATA.GUARD.2 and .3). It is written as the realization of GUARD.3's database layer, with a link proposed.
  - The per-user read clause records J1's default and is marked `undecided: awaiting maintainer`, as instructed. It is not settled here.
- **DATA.MAINTAIN**:
  - L046 (consensus) and L474 (MAINT) look like two truths for structure. They are reconciled as origin of change against truth of state, which must agree.
  - L047 is the max for "without breaking running code". The database and its consumers never deploy atomically, and MD-03's several consumers deploy on their own schedules.
  - L517 belongs to J6, which decides it and counts the departure once for both graphs (X2). This node keeps the principle and cites the verdict (m8). It sits within J1's RECORD.3 rule ("a function-API signature change neither additive nor marked coordinated" is forbidden): the contract phase is the change marked coordinated.
- **DATA.DERIVE**: the doctrine (L488) is the max choice and agrees with the research (L072). Stored copies follow J1's DERIVE.1 order, which J1 marks as its own inference, with the same-transaction rung kept by trigger wherever another writer exists. The generated-column exception for stored predicates is inferred from L176.

### The awaiting-maintainer clause

- **Situation**: a read rule such as "a draft is visible only to its author" must hold for every backend sharing the database.
- **What is open**: whether each backend filters such reads, or read functions in the database do. This is J1's Q1, already before the maintainer.
- **What the graph records** (J1's default, word for word): A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. The database's part otherwise is per-role grants; row-level security stays not a default (MD-01), acceptable under its three conditions.
- **Consequence**: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- **Where B's condition holds**: the filter lives in read functions of the database's function API, which raises gap 1's proposed DATA.INTERFACE node in priority; DATA.GUARD's clause then reads "read functions filter by the acting user" for those tables.

### Hand-offs

- **To J6 (PIG-WEB.DATA)**:
  - the default isolation level, set by J1 and unchanged here;
  - collation, open, with no row;
  - the drift-check mechanism between the live catalogue and the migration history;
  - the L517 verdict, which J6 holds and counts (X2);
  - the sync gradient and drift guard for derived copies (L532, L533);
  - the state-label-last order (L597);
  - the constraint trigger for dependencies lost by a Boyce-Codd decomposition (GUARD.1 and GUARD.4 there).
- **To the skeleton owner (gap 1)**: three proposals, none applied.
  - A philosophy node `DATA.INTERFACE`, realizing RECORD.2 and the database share of ACT.1, refined by PIG-WEB.DATA.INTERFACE. The target hierarchy places the database's function API under DATA, and PIG-WEB.DATA.INTERFACE has no philosophy counterpart. The skeleton's LOGIC.ENFORCE realizes ACT.1 only for the backend's share.
  - Links `DATA.GUARD realizes ALLOCATION.GUARD.3` (database layer) and `DATA.GUARD realizes ALLOCATION.RULES.5`.
  - Link `DATA.MAINTAIN realizes ALLOCATION.ACT.4`.

### Checks run

- Every owned row (12) is cited in at least one record: L037, L038, L039, L469 and L470 in ORGANIZE; L043, L476 and L485 in GUARD; L046, L047 and L474 in MAINTAIN; L488 in DERIVE.
- Each decision was compared with J1's matrix line for RECORD.1, RECORD.3, GUARD.2, GUARD.3, GUARD.5 and DERIVE.1: no authority, copy or forbidden tier was changed. Conflicts with J1 placements: 0.
- MD-01 (no row-level security by default), MD-02 (not touched by DATA nodes beyond RECORD.3's function-API contract) and MD-03 (shared database) were applied and cited by id.
- After the review pass: no record still says "costs nothing", "excluded", "If the maintainer chooses read functions instead" or `conflict: narrows L517`.
- Written only inside this folder, with no absolute paths and no private names. No graph file was created, and nothing was committed.

Pinned:
- Nodes judged: 5 of 5 (DATA, DATA.ORGANIZE, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE); the 12 owned rows read in full and all cited.
- Decided 5, undecided 0. DATA.GUARD carries one clause it does not settle: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (J1's Q1). Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0. No genuine trade-off between forces a DATA node serves; `questions.md` says none.
- DATA.ORGANIZE after review: third normal form is the floor; Boyce-Codd, fourth and fifth normal form apply where they apply; a dependency lost by a Boyce-Codd decomposition is enforced by a constraint trigger under Serializable or a lock; stopping at third normal form is acceptable only when every candidate key is a single column, and no multi-valued facts.
- Verdicts against the maintainer doctrine: 0 new. Inherited from J1 and realized in DATA.GUARD: declarative constraints required, not optional (partly against L471). L517 is cited, not counted: J6 owns and counts that departure once for both graphs ("deployed together" only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract). DATA.MAINTAIN keeps the principle: an incompatible change keeps every running consumer working.
- Conflicts with J1 placements: 0.
- Review: 3 of the DATA-branch review's 13 findings concern this unit (B1, M4, m8); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3. J6's M2 followed through in DATA.DERIVE for consistency.
- Gaps: (1) structure: under MD-03 no philosophy node realizes the database function API (RECORD.2) or the database share of ACT.1, and DATA.GUARD and DATA.MAINTAIN have no link to the per-role layer of GUARD.3 or to ACT.4; links and one node proposed, nothing created. (2) Collation, left open "under DATA" by J1: no row grounds a choice; handed open to J6 (PIG-WEB.DATA.ORGANIZE.3). (3) Data lifecycle (retention, deletion, recovery) has no principle-level row; it exists only at PIG-WEB.DATA.MAINTAIN.2 to .5. (4) The drift check between the live catalogue and the migration history is inferred; no source read. (5) The Boyce-Codd claims (same kind of anomaly; dependency loss) rest on standard theory, not on a ledger row.
