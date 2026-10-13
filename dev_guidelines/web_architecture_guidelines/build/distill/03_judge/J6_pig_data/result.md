# Result: J6 pig-web-defaults PIG-WEB.DATA judged

## L1 headline

33 of the 36 nodes of the Postgres data tier are judged; the 3 deferred nodes are not. 32 are decided and 1 awaits the maintainer. Each node realizes the settled placements of J1 and the DATA principles of J2 under the shared-database default (MD-03), and none re-decides them. The adversarial review's 11 findings on this unit are applied, none rejected, together with the cross-branch resolutions.

The tier binds every rule to the database itself, not to its callers, because several consumers write. In practice that means:
- declared constraints, and constraint triggers for rules that span rows, including no active child under a soft-deleted parent;
- one role per consumer, no consumer holding DELETE, and privileged functions owned by narrow non-login roles, never by the owner role;
- triggers for history, `updated_at`, validation and same-transaction derived copies;
- Serializable isolation for every writing role, with a bounded retry owned by every caller.

One question goes to the maintainer, the default deletion of user-facing data, now framed even-handed: the archive wins on reference integrity for every consumer, soft delete on immediate undo and in-place history. Recommended: archive; recorded if unanswered: soft delete with three safeguards. Per-user read visibility stays awaiting the maintainer with J1's default, read functions acceptable when a rule must hold for two or more backends. Five verdicts go partly against the doctrine: `updated_at` by trigger, 8-byte keys, how hierarchies are stored, breaking function-API changes, and no `updated_at` on append-only tables. No verdict conflicts with a J1 placement. Collation stays open.

Pinned:
- Nodes judged: 33 of 36 (7 roll-ups, 26 leaves); 3 deferred nodes not judged (PIG-WEB.DATA.MAINTAIN.6, PIG-WEB.DATA.MAINTAIN.7, PIG-WEB.DATA.DERIVE.3); the 138 owned rows read in full and all cited, L526 only as input to its deferred node.
- Decided 32; 1 `undecided: awaiting maintainer`: PIG-WEB.DATA.MAINTAIN.2, the default deletion of user-facing transactional data. Recommendation: hard delete with a same-transaction archive, the max for integrity. Recorded if unanswered: the doctrine's soft delete (L520) with three mandatory safeguards, the first now a constraint trigger on the child table.
- J1's read-visibility clause is carried, not settled, in GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1 as `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1 (deletion default), reframed even-handed: soft delete wins on immediate undo and in-place history for users and reporting; the archive wins on reference integrity for every consumer.
- Verdicts against the maintainer doctrine: 5 new, all partial: L529 (updated_at set by a narrow trigger that stamps only on change); L503 (8-byte keys unless the table's size is bounded by design); L493 (a hierarchy's parent link stays a declared self-referencing foreign key; path, closure or nested set only as derived copies); L517 (counted here for both graphs: "deployed together" only when every consumer of the changed object ships in the same deployment as the migration, otherwise expand, migrate, contract); L498 (append-only tables carry `created_at` and no `updated_at`). Inherited from J1 and realized in GUARD.1: declarative constraints required (against L471). Four doctrine-internal tensions resolved, none against it; tension 2 now reads: DELETE is held by a narrow non-login role that owns the deletion functions.
- Conflicts with J1 placements: 0.
- Review: 11 of the DATA-branch review's 13 findings concern this unit (B1, M1, M2, M3, m1 to m7); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3, X4, X7 (X5 and X6 do not touch this unit).
- Gaps: (1) collation: no row grounds a choice; left open with what any choice must satisfy, research proposed. (2) Mechanisms inferred with no source read: the structure drift gate, usage evidence before a function is removed, tamper detection on history, the JSON schema validator, the narrow function-owner roles. (3) PIG-WEB.DATA.INTERFACE has no philosophy counterpart (J2's gap 1). (4) Evidence thin for the agent attribution row (L685, inferred, one source). (5) Not checked against a source: prepared statements in transaction-mode pooling by pooler version, and the exact standby behaviour of UNLOGGED tables.

## L2 claims

### Review fixes

- B1, X1: the read-visibility clause in GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1 now records J1's default word for word, read functions included where a rule must hold for two or more backends; row security is "not a default", no longer "excluded".
- M1: the deletion question is reframed: the force soft delete wins on is named, and the archive's missing costs are added.
- M2: the soft-delete safeguard and DERIVE.1's top rung are bound to the table by trigger.
- M3: definer functions are owned by narrow non-login roles, not the owner role (GUARD.2, MAINTAIN.2, MAINTAIN.3, DERIVE.2, INTERFACE.1).
- m1 to m5: grounds corrected: key width, hierarchy forms, `updated_at` stamped on change, the L498 departure counted, UNLOGGED on a standby.
- m6, m7: every caller of a writer function owns a bounded retry; the driver and pooler prepared-statement point is handed on and marked for research.
- X2 to X4, X7: the L517 departure is counted here once; one operation is one call, with cross-domain composition inside the database; the test boundary; the function catalogue is kept in sync by process (MD-02).

### Claims

- **ORGANIZE** (schema): the schema in migrations is the origin of every stored fact; generated models inherit it.
  - Repeating groups become child tables. Arrays hold only bounded, reference-free sets, and their rules are declared (L169, L489).
  - Keys:
    - Scoped rows get a composite key led by the scope column, which also blocks references across scopes (L499 to L501, MAINT).
    - Soft deletion plays no part in key shape.
    - Keys are identity columns, 8 bytes unless the table's size is bounded by design (partly against L503, on the tie-break "the loss hardest to repair wins").
    - A UUID needs a stated reason (L504), and it is then UUIDv7.
  - Column types: `timestamptz`, `text` with CHECK, `numeric`, lookup tables instead of enums, `created_at` everywhere and `updated_at` on updated tables (L177, L497, L498; partly against L498 for append-only tables). **Collation stays open**: no row covers it.
  - Names follow L505 to L507 whole.
  - JSON is JSONB, validated on write by a trigger against the in-database registry (L508 to L512).
  - Schemas are domain namespaces. The function-API schema qualifies by its access need (L513).
  - Every index serves a stated query, and every foreign key is indexed (L173, L490).
  - State: `known | conflict: L498, L503 | gap: collation`.
- **GUARD** (declared integrity):
  - Constraints are required and named.
    - Foreign keys are strict: NO ACTION by default, narrow CASCADE (L492).
    - Unbounded hierarchies keep a declared parent foreign key, with an acyclicity trigger under Serializable or a lock. Path, closure or nested-set forms exist only as derived copies (partly against L493).
  - Roles:
    - Group roles per functional branch hold the privileges.
    - Each consumer has its own login role. No consumer has DELETE or owns objects.
    - EXECUTE is revoked from PUBLIC. Functions that write what the caller cannot are owned by narrow non-login roles (deletion, history writing, cache maintenance), each holding only its DML; the owner role owns tables and runs migrations only (L181 to L186, L514, L525).
  - Row-level security is not a default (MD-01). The acting user and the person an agent acts for always travel as transaction-local settings, which are checked against the session role (L311, L566).
  - Triggers do a closed list of work, which includes `updated_at`, stamped only on change (against L529). Business transitions stay in writer functions.
  - Per-user read visibility: `undecided: awaiting maintainer`, with J1's default (each backend filters from one specification with a shared denial suite; read functions acceptable when a rule must hold for two or more backends). Reporting and operator roles see every row they may SELECT unless restricted.
  - State: `known | conflict: L471 (inherited), L493, L529 | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **CONCURRENCY**:
  - Every writing role, the owner included, runs Serializable, set on the role and asserted by the writer functions. Every caller of a writer function (backends, jobs, consoles, scripts) owns a bounded retry of the whole call. User-edited rows carry a version checked in the write (L568 to L577, L676).
  - Concurrency tests for Serializable and locks are in the default suite; commit-only behaviour is tested in a disposable database (X4).
  - Locks are transaction-scoped only (L578 to L581).
  - An inseparable change is one statement. Re-runnable work is idempotent by form, while keyed operations may use relative updates (L585 to L588).
  - Readers that must see every row claim and mark them, or use the `xid8` horizon. Gapless numbers come from a counter row (L591 to L595).
  - Facts are written first and the state label last (L597). Observe-only checks are only a migration aid (L598).
  - State: `known`.
- **MAINTAIN**:
  - Migrations are small, re-runnable and online-safe, follow expand, migrate, contract, and pass a CI drift gate (L189 to L198, L519). The drift gate is inferred.
  - **Deletion is decided per table. The default for user-facing data awaits the maintainer (question 1)**: recommended archive; if unanswered, soft delete with three safeguards, the first a constraint trigger on the child table.
  - History is trigger-written and append-only, by a function owned by a narrow history-writer role. It records the session role, the actor and the person acted for, with tamper detection for high-value data (L208 to L213, L685).
  - Bulk jobs follow L540 to L545 whole.
  - Recovery to a chosen moment is proven by rehearsed restores (L218 to L223).
  - State: `known | open child: MAINTAIN.2 (undecided: awaiting maintainer)`.
- **DERIVE**:
  - A copy is made only when it is needed, with a sync plan and a drift guard. The database guards it, not one application: a copy that decides writes is kept by a same-transaction trigger, by the writer function only when the source admits no other writer (L168, L176, L531 to L533).
  - Cache tables follow the doctrine (L535 to L539), with these additions:
    - workers claim invalidation keys with SKIP LOCKED;
    - single-owner caches are limited under MD-03;
    - UNLOGGED tables are not used where a standby reader needs the data, since their contents are not replicated.
  - State: `known`.
- **INTERFACE**:
  - Writes go through functions, one business operation per call; cross-domain composition happens inside the database, through published functions. The function conventions (L530) are adopted, and an override is allowed only to granted roles and is recorded.
  - Procedures are used only for jobs. Views are never part of the contract (L516).
  - A breaking change goes expand, migrate, contract unless every consumer ships with the migration (partly against L517; counted here for both graphs).
  - The pooler runs in transaction mode, with limits and timeouts set per consumer role (L199 to L203).
  - State: `known | conflict: L517 | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database | gap: no philosophy counterpart`.

Pinned:
- Nodes judged: 33 of 36 (7 roll-ups, 26 leaves); 3 deferred nodes not judged (PIG-WEB.DATA.MAINTAIN.6, PIG-WEB.DATA.MAINTAIN.7, PIG-WEB.DATA.DERIVE.3); the 138 owned rows read in full and all cited, L526 only as input to its deferred node.
- Decided 32; 1 `undecided: awaiting maintainer`: PIG-WEB.DATA.MAINTAIN.2, the default deletion of user-facing transactional data. Recommendation: hard delete with a same-transaction archive, the max for integrity. Recorded if unanswered: the doctrine's soft delete (L520) with three mandatory safeguards, the first now a constraint trigger on the child table.
- J1's read-visibility clause is carried, not settled, in GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1 as `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1 (deletion default), reframed even-handed: soft delete wins on immediate undo and in-place history for users and reporting; the archive wins on reference integrity for every consumer.
- Verdicts against the maintainer doctrine: 5 new, all partial: L529 (updated_at set by a narrow trigger that stamps only on change); L503 (8-byte keys unless the table's size is bounded by design); L493 (a hierarchy's parent link stays a declared self-referencing foreign key; path, closure or nested set only as derived copies); L517 (counted here for both graphs: "deployed together" only when every consumer of the changed object ships in the same deployment as the migration, otherwise expand, migrate, contract); L498 (append-only tables carry `created_at` and no `updated_at`). Inherited from J1 and realized in GUARD.1: declarative constraints required (against L471). Four doctrine-internal tensions resolved, none against it; tension 2 now reads: DELETE is held by a narrow non-login role that owns the deletion functions.
- Conflicts with J1 placements: 0.
- Review: 11 of the DATA-branch review's 13 findings concern this unit (B1, M1, M2, M3, m1 to m7); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3, X4, X7 (X5 and X6 do not touch this unit).
- Gaps: (1) collation: no row grounds a choice; left open with what any choice must satisfy, research proposed. (2) Mechanisms inferred with no source read: the structure drift gate, usage evidence before a function is removed, tamper detection on history, the JSON schema validator, the narrow function-owner roles. (3) PIG-WEB.DATA.INTERFACE has no philosophy counterpart (J2's gap 1). (4) Evidence thin for the agent attribution row (L685, inferred, one source). (5) Not checked against a source: prepared statements in transaction-mode pooling by pooler version, and the exact standby behaviour of UNLOGGED tables.

## L3 full

### Review fixes

Source: `../review_data/review.md` (13 findings on the DATA branch, 11 on this unit) and `../cross_branch_fixes.md` (X1 to X7). Every fix was checked against its evidence before applying; none was found wrong. Applied: 11. Rejected: 0.

| id | node(s) | change in `records.md` / `questions.md` |
|---|---|---|
| B1 + X1 | GUARD, GUARD.2, GUARD.3, INTERFACE, INTERFACE.1; DATA roll-up state | J1's default recorded word for word: "A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends". INTERFACE's "not part of the API until answered" replaced by "where B's condition holds, read functions join INTERFACE.1 and read GUARD.3's context". GUARD.3's "excluded either way" replaced by "not a default (MD-01)". One notation in every state: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. X1's consequence added in GUARD and GUARD.2: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless restricted. X1's "verified actor" is glossed in GUARD.3 and INTERFACE.1: verified by the backend, a claim to the database (J1 R1-3). |
| M1 | MAINTAIN.2; `questions.md` Q1 | The forces are rewritten: integrity of references and reads for every consumer (archive) against immediate undo and in-place history for users and reporting (soft delete, a force of other branches); recoverability is not what divides them. Added to the options: (a) under the archive, reporting must union it to count deleted rows; (b) the archive also needs a children-handling deletion function, since CASCADE is forbidden on core entities (L492); (c) "restores are rare" rests on one T3 source (L204, SRC-265). The question stays with the maintainer, as instructed: its recommendation (archive, the max for the node's force) and its unanswered default (L520 with three safeguards) are both recorded, marked `undecided: awaiting maintainer`. The review's preferred fix, a fifth partial verdict against L520, is recorded in MAINTAIN.2 and not taken. Q1 also gains "what would make A the better default". |
| M2 | MAINTAIN.2 safeguard 1; DERIVE.1; DERIVE roll-up; DERIVE.2 invalidation (follow-through) | Safeguard 1 is a constraint trigger on the child table refusing an active row whose parent is soft-deleted, under Serializable or with a lock on the parent row. DERIVE.1's top rung: "a same-transaction trigger; the writer function only when the source table admits no other writer (no direct-write grant, no owner-run job)". DERIVE.2's invalidation-key insert follows the same rule. |
| M3 | GUARD.2, MAINTAIN.2, MAINTAIN.3, DERIVE.2, INTERFACE.1; GUARD roll-up | Definer functions are owned by narrow NOLOGIN roles (deletion, history writer, cache maintenance), each holding only the DML it executes, with a fixed search_path; the owner role owns tables and runs migrations only; no consumer role is a member. Tension 2 now reads: "DELETE is held by a narrow non-login role that owns the deletion functions" (inferred). Owner-owned definer functions are added to GUARD.2's rejected list. |
| m1 | ORGANIZE.2 | Ground for 8-byte keys restated: overflow is a loss of availability and changeability, not integrity; the verdict holds on J1's tie-break, the loss hardest to repair later wins (L197). |
| m2 | GUARD.1 | Closure tables carry foreign keys on both ends; what no constraint protects is their transitive completeness; only path and nested set lack the foreign keys. "One table per level, as L493 prefers" becomes an inferred rule. The acyclicity trigger runs under Serializable or a lock. |
| m3 | GUARD.4 | The L594 ground is dropped (L594 is about sequence ids; CONCURRENCY.5 forbids timestamp cursors anyway). The trigger stamps only when `NEW IS DISTINCT FROM OLD` (inferred), which meets L529's own reason at the table. |
| m4 | ORGANIZE.3; MAINTAIN.3 | No `updated_at` on append-only tables is recorded as a partial departure from L498; `created_at` stays their record-time name, so only `updated_at` departs. Counted in the against-doctrine list (now 5). |
| m5 | DERIVE.2 | "Would read them empty" replaced by "unavailable on a standby" (contents not replicated); the exact standby behaviour is marked unchecked. |
| m6 | CONCURRENCY.1, CONCURRENCY.2 | "Every consumer that calls a writer function owns a bounded retry; the shared specification names it"; console tooling handed to J9. |
| m7 | INTERFACE.2 | The prepared-statement rule stays the safe default; driver configuration handed to J7 and J9; prepared-statement support by pooler version marked for research. |
| X2 | INTERFACE.1 | The L517 departure is counted here once for both graphs, with X2's condition word for word; L517's coordination with every consumer and "no formal version numbers, a new function name carries the change" kept. |
| X3 | INTERFACE.1 | One business operation is one function call in its own transaction; backends never compose calls; a function may call another domain's published functions in the same transaction; only direct access to another domain's tables is forbidden. |
| X4 | CONCURRENCY.2, INTERFACE.1 | Logic tests in never-committing transactions; commit-only behaviour in a disposable database; concurrency tests for Serializable and locks in the default suite. |
| X7 | INTERFACE.1 | "Always in sync by process" and the compatibility window cover the function API catalogue; the CI catalogue diff is that process here. |

X5 (backend deployables) and X6 (tokens in URLs) do not touch this unit.

### Files

- `records.md`: one judge record per node (33 judged, 3 deferred listed at the end), each with positions and ledger ids, forces, the decision with grounds, rejected positions with their winning condition, the placements realized, and a proposed `epistemic_state`. Passages changed by the review name their finding or resolution id.
- `questions.md`: question 1, self-contained and even-handed, with the recommendation and what is recorded if it goes unanswered.
- `result.md`: this file.

### Method

- Inputs read: `../../target_hierarchy.md` and `../../maintainer_decisions.md` in full; the J6 section of `../../02_skeleton/judge_plan.md`; `../J1_allocation/allocation_matrix.md` in full, plus the default context, the access paths and the records of GUARD.2, GUARD.3, GUARD.5, GUARD.6, ACT.1 to ACT.4, DERIVE.1, DERIVE.2, DB_API, TYPE_CHAIN, ROW_SECURITY, JOB_HOST and CACHE_STORE in `../J1_allocation/records.md`; `../J2_phil_data/records.md` and `questions.md` in full; from `../../02_skeleton/skeleton.md`, the partition rationale, the tree and node table rows of PIG-WEB.DATA, the intentlinks and the deferred nodes; and the 138 owned ledger rows in full.
- Additional rows read: the rows owned elsewhere that the placements cite (L040, L187, L409, L413, L469 to L476, L482, L485, L488, L527, L534, L584, L596, L599, L604, L619, L622, L625, L626, L688, among others). From the doctrine research result (`build/research/15_maintainer_doctrine/result.md`), the doctrine-internal tensions and the answers to the key-type and deletion questions, because L499, L503 and L520 refer to them.
- Review pass: `../review_data/review.md` and `../cross_branch_fixes.md` in full; J1's Q1 "If unanswered, the graph records" re-read in `../J1_allocation/questions.md`; ledger rows L182, L184, L204, L493, L498, L503, L514, L525, L529 and L594 re-read to check each finding's evidence.
- Rule: the max for DATA is integrity of the stored data. Under MD-03, "integrity" means the rule holds for every writer: several backends, the operator role, and owner-run migrations and jobs. That is J1's ground in GUARD.2. Most decisions below follow from it, and the review's M2 applied it where it had been missed.

### Verdicts by node, with what decides each

| node | verdict (short) | decided by | state |
|---|---|---|---|
| DATA | roll-up of six ways Postgres holds the database's work | children | known, open child, awaiting maintainer |
| ORGANIZE | schema is the origin of stored facts | TYPE_CHAIN, J2 | known, gap collation |
| ORGANIZE.1 | child tables for repeating groups; arrays bounded, declared | L169, L489 (MAINT) | known |
| ORGANIZE.2 | scope-leading composite keys; identity, 8 bytes unless bounded; UUIDv7 only with a reason | L499-L504 (MAINT), partly against L503 (tie-break ground, m1) | known, conflict |
| ORGANIZE.3 | precise types; lookup tables; timestamps; no updated_at on append-only tables; collation open | L177, L178, L497, L498; partly against L498 (m4) | known, conflict, gap |
| ORGANIZE.4 | naming doctrine whole | L505-L507 (MAINT) | known |
| ORGANIZE.5 | JSONB, registry, validated on write by trigger | L508-L512 (MAINT), L511 | known |
| ORGANIZE.6 | domain schemas; API schema by access need; single tenant | L513, L180, L128, MD-01 | known |
| ORGANIZE.7 | every index serves a query; foreign keys indexed | L173, L490 | known |
| GUARD | roll-up | children | known, awaiting maintainer |
| GUARD.1 | every expressible rule declared and named; strict foreign keys; declared parent links, acyclicity under Serializable or a lock | L492, L494, L495, J1 GUARD.2; partly against L493 (ground corrected, m2) | known, conflict |
| GUARD.2 | group roles, login per consumer, no DELETE, narrow non-login function-owner roles | L181-L186, L514, L525, J1 access paths (M3) | known, awaiting maintainer |
| GUARD.3 | no row security by default; actor always passed and checked | MD-01, L311, L566, J1 R1-3 | known, conflict (L619, L688), awaiting maintainer |
| GUARD.4 | closed list of trigger work, including updated_at stamped on change | L216, L217; against L529 (m3) | known, conflict |
| CONCURRENCY | roll-up | children | known |
| CONCURRENCY.1 | Serializable for every writing role plus versions on edited rows; every caller retries | L568 (a)+(c), L569, L570, L573 (m6) | known |
| CONCURRENCY.2 | isolation mechanics, retry by the caller, test boundary | L571-L577, L676, X4 | known |
| CONCURRENCY.3 | transaction-scoped locks for contention, queues, exceptions | L578-L581 | known |
| CONCURRENCY.4 | one statement or one transaction; idempotent by form unless keyed | L585-L588, L572 | known |
| CONCURRENCY.5 | gappy sequences; claim-and-mark or xid8 horizon | L591-L595 | known |
| CONCURRENCY.6 | facts first, label last; observe-only only to migrate | L597, L598 | known |
| MAINTAIN | roll-up | children | known, open child |
| MAINTAIN.1 | online-safe, re-runnable migrations; expand-contract; drift gate | L189-L198, L519, J2 | known |
| MAINTAIN.2 | per-table decision; default for user-facing data awaiting maintainer; soft-delete parent check by trigger | L205, L520 against L204 (M1, M2, M3) | **undecided: awaiting maintainer** (question 1) |
| MAINTAIN.3 | trigger-written append-only history with role, actor, subject; narrow history-writer role | L208-L213, L685, J1 ACT.4 (M3) | known, gap |
| MAINTAIN.4 | bulk job doctrine whole | L540-L545 (MAINT) | known |
| MAINTAIN.5 | point-in-time recovery proven by restore | L218-L223 | known, gap |
| DERIVE | roll-up | children | known |
| DERIVE.1 | copies only when needed, sync plan, drift guard; trigger-first top rung | L168, L176, L531-L533 (M2) | known |
| DERIVE.2 | cache doctrine plus SKIP LOCKED, MD-03 limit, UNLOGGED limit, narrow cache role | L420, L535-L539 (M3, m5) | known |
| INTERFACE | roll-up | children | known, awaiting maintainer, gap |
| INTERFACE.1 | function API conventions; one operation one call; breaking changes expand-contract | L516, L530, DB_API, X2, X3, X7; partly against L517 | known, conflict, awaiting maintainer |
| INTERFACE.2 | transaction pooling, per-role limits and timeouts | L199-L203 (m7) | known, gap |

### Against the doctrine, and why each is the max

- **L529, updated_at**: owner-run jobs and the single-consumer direct-write exception write rows without a writer function. Only a trigger sets `updated_at` for every writer, and cache staleness checks depend on it (L537). L216 lists exactly this use as a narrow trigger. L529's reason, avoiding WAL traffic and needless trigger work, is met at the table: writers skip unchanged rows and the trigger stamps only when the row changes (inferred). L529 is acceptable when every writer of the table is a function that sets the column.
- **L503, key width**: overflow refuses writes from every consumer, a loss of availability and changeability rather than integrity; the repair is a rewrite of the table and of every referencing column at its largest (L197). On J1's tie-break, the loss hardest to repair later wins, so 8 bytes is the default. L503 is acceptable for tables whose size is bounded by design.
- **L493, hierarchies**: a materialized path or nested set lists ancestors that no foreign key protects; a closure table has foreign keys but no constraint protects its transitive completeness. The parent link is the fact, stored once and declared; the other forms are derived copies (J2's "each fact once" and "store the minimum").
- **L517, breaking changes** (counted here once, for both graphs): under MD-03, consumers deploy on their own schedules, so "deployed together" leaves a window where old code meets new structure. "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract. L517's coordination and its no-version-number rule are kept.
- **L498, append-only tables** (added after review, m4): no `updated_at` on tables whose rows are never updated, since it would state nothing; `created_at` stays as the record time.
- **Inherited**: L471's "CHECK optional" (J1 GUARD.2).
- **Doctrine-internal tensions resolved**, each consistent with the doctrine's own stronger statement:
  - (1) key shape does not depend on soft deletion;
  - (2) DELETE is held by a narrow non-login role that owns the deletion functions (inferred; consistent with L514 and L525; changed from "the functions' owner" after review, M3);
  - (4) JSON validation is bound by a trigger;
  - (6) invalidation-queue workers claim with SKIP LOCKED and recompute set-based.

### The question and the awaiting-maintainer clause

- **Question 1** (MAINTAIN.2): the deletion default, `undecided: awaiting maintainer`. Reframed after review (M1): both options keep deleted data recoverable and kept for audit. The archive wins on the integrity of references and reads for every consumer of the shared database; soft delete wins on immediate undo and in-place history, for users and agents and for reporting that counts deleted rows in historical figures. The archive also pays a cascade-like cost (a deletion function that handles children, since CASCADE is forbidden on core entities), and reports must union the archive. "Restores are rare" rests on one T3 source. Recommendation: archive by default; soft delete where the product offers restore or undo, or where reports must count deleted rows in place. If unanswered, the doctrine's default is recorded with three safeguards:
  - a constraint trigger on the child table refuses an active child of a soft-deleted parent, under Serializable or a lock on the parent (M2);
  - the active-row predicate is written once in the shared specification;
  - a restore re-checks constraints.
- **Awaiting maintainer** (J1 Q1, not asked again): `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Where B's condition holds, read functions join INTERFACE.1 and read GUARD.3's context. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.

### Hand-offs and notes for other units

- **J7 (LOGIC)**:
  - the bounded retry wrapper around each function call (40001, 40P01; 23505 with care);
  - mapping of named constraints and stable function error codes to interface errors;
  - zero-row version writes become precondition failures;
  - whether internal keys may appear in URLs or agent payloads (ORGANIZE.2 guarantees a non-enumerable alternate key can be added);
  - the outbox relay reads by claim-and-mark (CONCURRENCY.5);
  - the database driver's prepared-statement caching configured to match the transaction-mode pooler (m7).
- **J8 (INTERACTION)**: database-notification listeners connect outside the transaction-mode pooler (INTERFACE.2).
- **J9 (TRANSVERSE)**: pooler placement; the drift gate and the function catalogue diff in CI; pgaudit output to the security event log; recovery objectives (no row); a bounded retry in console tooling and scripts that call writer functions (m6); driver configuration for consoles and scripts (m7).
- **Skeleton owner**: J2's proposed philosophy node for the database interface; proposed links: GUARD.2 realizes ALLOCATION.GUARD.3 and PIG-WEB.ALLOCATION.DB_API; CONCURRENCY.5 realizes ALLOCATION.ACT.2.
- **Research**: collation provider and locale, and whether a provider upgrade can change order and invalidate indexes; tamper-detection mechanisms for append-only history; a JSON schema validator inside Postgres; evidence of function usage before removal; prepared-statement support in transaction-mode pooling by pooler version (m7); the standby behaviour of UNLOGGED tables (m5).
- **Ledger owner**: L684 still has no source (J1's note), and MAINTAIN.3 does not rely on it.

### Checks run

- A script compared the owned set (138 rows, from the J6 section of the judge plan) with the ids cited in `records.md`: 0 owned rows uncited. Cited rows owned elsewhere are listed in `records.md` under "How to read".
- `records.md` has 33 node records, plus the 3 deferred nodes listed without verdicts. One record is `undecided: awaiting maintainer` (MAINTAIN.2), and the two roll-ups above it are `known` with an open child.
- After the review pass: every finding naming this unit (B1, M1, M2, M3, m1 to m7) has a changed passage in `records.md` carrying its id; no state line still says "awaiting maintainer: J1 Q1", "excluded either way" or "not part of the API until answered"; no remaining record gives a definer function to the owner role.
- No graph file was created, no other unit's file was edited, nothing was committed, and no absolute path or private name was written.

Pinned:
- Nodes judged: 33 of 36 (7 roll-ups, 26 leaves); 3 deferred nodes not judged (PIG-WEB.DATA.MAINTAIN.6, PIG-WEB.DATA.MAINTAIN.7, PIG-WEB.DATA.DERIVE.3); the 138 owned rows read in full and all cited, L526 only as input to its deferred node.
- Decided 32; 1 `undecided: awaiting maintainer`: PIG-WEB.DATA.MAINTAIN.2, the default deletion of user-facing transactional data. Recommendation: hard delete with a same-transaction archive, the max for integrity. Recorded if unanswered: the doctrine's soft delete (L520) with three mandatory safeguards, the first now a constraint trigger on the child table.
- J1's read-visibility clause is carried, not settled, in GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1 as `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default, J1's word for word: A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1 (deletion default), reframed even-handed: soft delete wins on immediate undo and in-place history for users and reporting; the archive wins on reference integrity for every consumer.
- Verdicts against the maintainer doctrine: 5 new, all partial: L529 (updated_at set by a narrow trigger that stamps only on change); L503 (8-byte keys unless the table's size is bounded by design); L493 (a hierarchy's parent link stays a declared self-referencing foreign key; path, closure or nested set only as derived copies); L517 (counted here for both graphs: "deployed together" only when every consumer of the changed object ships in the same deployment as the migration, otherwise expand, migrate, contract); L498 (append-only tables carry `created_at` and no `updated_at`). Inherited from J1 and realized in GUARD.1: declarative constraints required (against L471). Four doctrine-internal tensions resolved, none against it; tension 2 now reads: DELETE is held by a narrow non-login role that owns the deletion functions.
- Conflicts with J1 placements: 0.
- Review: 11 of the DATA-branch review's 13 findings concern this unit (B1, M1, M2, M3, m1 to m7); all applied, 0 rejected. Cross-branch resolutions applied: X1, X2, X3, X4, X7 (X5 and X6 do not touch this unit).
- Gaps: (1) collation: no row grounds a choice; left open with what any choice must satisfy, research proposed. (2) Mechanisms inferred with no source read: the structure drift gate, usage evidence before a function is removed, tamper detection on history, the JSON schema validator, the narrow function-owner roles. (3) PIG-WEB.DATA.INTERFACE has no philosophy counterpart (J2's gap 1). (4) Evidence thin for the agent attribution row (L685, inferred, one source). (5) Not checked against a source: prepared statements in transaction-mode pooling by pooler version, and the exact standby behaviour of UNLOGGED tables.
