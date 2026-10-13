# Review of the DATA branch: J2 (web-app-philosophy DATA) and J6 (pig-web-defaults PIG-WEB.DATA)

This is an adversarial review of `../J2_phil_data/` and `../J6_pig_data/` (result.md, records.md and questions.md in each). They were checked against the max rule (`../../target_hierarchy.md`), the maintainer decisions MD-01 to MD-03 (`../../maintainer_decisions.md`), J1's settled placements and its Q1 (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/questions.md`), the ledger (`../../02_skeleton/claims_ledger.md`), the doctrine research (`../../../research/15_maintainer_doctrine/result.md`), and three sources fetched where the stakes were high. The judges' files were not edited.

Pinned:
- Findings: 1 blocking, 4 major, 8 minor (13 in all).
  - Blocking, B1: J1's stated default for per-user read visibility is narrowed in J2 DATA.GUARD and in J6 GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1. J1 records read functions as "acceptable when a per-user read rule must hold for two or more backends". Both units forbid them until the maintainer answers.
  - Major, M1: J6 MAINTAIN.2's question is not a genuine trade-off as written. Its own text says both options keep deleted data recoverable and "the difference is integrity". It is also one-sided on MD-03 and leaves out a cost of option B.
  - Major, M2: J6's soft-delete safeguard 1 and DERIVE.1's "writer function" option are not bound to the table. That goes against J6's own rule that only what is bound to the table holds for every writer.
  - Major, M3: in J6 GUARD.2, deletion, archive and invalidation functions run with the owner role's rights, where a narrow NOLOGIN role is enough. The owner can disable the history triggers.
  - Major, M4: J2 DATA.ORGANIZE says the higher normal forms "cost nothing" and its exemption condition is too broad. A Boyce-Codd decomposition can lose a dependency, and Kent's fifth-normal-form example has a single composite key.
- Verdicts against the maintainer doctrine:
  - L471 (inherited from J1): sound.
  - L517 (J2 narrows it, J6 decides it): sound; the max rule is on its side under MD-03.
  - L529 (updated_at by trigger): sound; the ground needs tightening (m3).
  - L503 (8-byte keys): sound; the ground is mislabelled as integrity (m1).
  - L493 (declared parent link): sound; the ground is partly wrong about closure tables (m2).
  - One departure from L498 is not counted (m4).
  - Doctrine-internal tensions 1, 2, 4 and 6 are resolved soundly, except that tension 2's resolution picks the broadest privilege available (M3).
- Questions:
  - J2 has none: sound.
  - J6 Q1 (deletion default): the max rule favours B. Preferred fix: decide B as a fifth partial verdict against L520. Otherwise keep the question only after restating the force that A wins on and making the framing even-handed (M1).

## Findings

### Blocking

**B1. Read-visibility default narrowed in both units.** Nodes: J2 DATA.GUARD; J6 GUARD, GUARD.2, GUARD.3, INTERFACE, INTERFACE.1.
- **Issue**: the task requires the open clause to stay open with its stated default. J1 states that default in `../J1_allocation/questions.md` ("If unanswered, the graph records"): A, each backend filters with the specification and shared-tests mitigation, **and** B as "acceptable when a per-user read rule must hold for two or more backends". Both units carry A only, and they turn the condition on B into a prohibition:
  - J6 INTERFACE: "read functions for rows with per-user rules are not part of the API until answered";
  - J6 GUARD.2 and J2 DATA.GUARD: per-user filtering "stays in each backend ... until the maintainer answers"; "If the maintainer chooses read functions instead...".

  Under MD-03 several backends share the database, so B's condition can easily hold in the default context. As written, the PIG-WEB node would contradict the placement it realizes (ALLOCATION.GUARD.3).
- **Secondary wording problem**: J6 GUARD.3 and INTERFACE.1 say "row security stays excluded either way (MD-01)". MD-01 makes row security "not a default", acceptable under three conditions. It is not excluded.
- **Evidence**: `../J1_allocation/questions.md` Q1, "If unanswered, the graph records"; J6 records INTERFACE (line 521) and GUARD.2 (line 241); J2 records DATA.GUARD ("Awaiting maintainer").
- **Fix**: in every carrying node, record J1's default word for word: "A provisional, with one written specification per rule and a shared denial suite; B acceptable when a per-user read rule must hold for two or more backends". Replace "not part of the API until answered" with "where B's condition holds, read functions join INTERFACE.1 and read GUARD.3's context". Replace "excluded either way" with "not a default (MD-01)".

### Major

**M1. J6 MAINTAIN.2: the deletion question undercuts its own trade-off and is one-sided.** Node: PIG-WEB.DATA.MAINTAIN.2 and `questions.md` Q1.
- **Issue (max rule)**:
  - `undecided` is reserved for a case where maximizing one force the node serves costs another it also serves. The records name recoverability against integrity. The question's own text then concedes "In both options, deleted data can be recovered and is kept for audit. The difference is integrity."
  - So B does not cost recoverability. It costs restore effort (one function the team owns) and the speed of undo. Undo speed is the user's ability to work with the data, an INTERACTION force, and B already keeps soft delete wherever the product offers undo.
  - On the node's own forces, B dominates. J6 decided four other conflicts with the doctrine in favour of the max (L503, L529, L493, L517), so this one is treated inconsistently: here the default left in place when unanswered is the doctrine's, not the max.
- **Issue (fairness)**:
  - (a) MD-03 is presented as cutting only one way. Under B, a reporting or BI consumer that needs deleted items in historical figures (last year's orders, including those deleted since) must union the archive. Under A they are still in the base table. That is a real cost of B for exactly the consumers MD-03 adds.
  - (b) The situation lists "cascade functions repeat what a foreign-key cascade would remove" as A's cost. B pays it too: GUARD.1 (L492) forbids CASCADE on core entities, so a hard delete of a parent with children also needs a deletion function that archives and removes the children in order.
  - (c) "Restores of deleted items are reported as rare" rests on one T3 source (L204, SRC-265) and should say so.
- **Evidence**: J6 records MAINTAIN.2 "Forces" against `questions.md` "Why B is recommended"; L492; L204 (one T3 critique, "undelete is rarely used"); the doctrine research D2 (suggested record: soft delete by default with its mitigations).
- **Fix (preferred)**: decide B as the max and record it as a fifth partial verdict against L520. A stays "acceptable when the product offers restore or undo on the table", which B already contains, "or when reporting consumers must count deleted rows in place". This verdict reaches the maintainer through the against-doctrine list, as the other four do.
- **Fix (if the question is kept)**: replace "why it is a genuine trade-off" with the real cross-branch force (immediate undo and in-place history for users and reporting, against reference integrity for every consumer). Add (a) and (b) to the options, and state the source tier behind "rare".

**M2. J6 binds two safeguards to writer functions where its own rule requires the table.** Nodes: PIG-WEB.DATA.MAINTAIN.2 (soft-delete safeguard 1); PIG-WEB.DATA.DERIVE.1 (the "trigger or the writer function" option).
- **Issue**:
  - J6's headline is "the tier binds every rule to the database itself, not to its callers, because several consumers write". It applies that rule in ORGANIZE.1 (array checks), ORGANIZE.5 (JSON validation by trigger) and GUARD.4 (updated_at by trigger). Its stated reasons are owner-run jobs and DB_API's single-consumer direct-write exception.
  - Safeguard 1 ("the writer functions refuse to attach an active row to a soft-deleted parent") is bound only to the functions. A direct single-table insert under the DB_API exception, or an owner-run job, attaches an active child to a deleted parent unchecked, which is the very hole the safeguard exists to close.
  - Likewise, DERIVE.1 allows "the writer function" to keep a copy that a reader decides writes from, and a direct writer would skip it.
- **Evidence**: J6 records ORGANIZE.1 (line 60, "met by binding that function to the column, not by asking every writer to call it"), GUARD.4 item 5, MAINTAIN.2 safeguard (1), DERIVE.1 "Mechanism"; J1 RECORD.2 (the direct-write exception) and the owner-role access path.
- **Fix**:
  - Safeguard 1 becomes a constraint trigger on the child table that refuses an active row whose parent is soft-deleted, under Serializable or with a lock on the parent row (CONCURRENCY.1).
  - DERIVE.1's top rung becomes "a same-transaction trigger; the writer function only when the source table admits no other writer (no direct-write grant, no owner-run job)".

**M3. J6 GUARD.2: privileged functions are owned by the owner role, the widest privilege, where a narrow role is enough.** Nodes: PIG-WEB.DATA.GUARD.2 (also MAINTAIN.3's history trigger function and DERIVE.2's invalidation functions).
- **Issue**:
  - Deletion functions, archive writes and cache invalidation run with the **owner's** rights. A table owner holds rights that cannot be granted separately (L182, SRC-146), including ALTER TABLE ... DISABLE TRIGGER. A bug or injectable dynamic SQL in any of these functions can therefore switch off the history and constraint triggers, or drop objects.
  - J6 itself concedes in MAINTAIN.3 that "the owner role bypasses grants" and calls for tamper detection because of it.
  - The more demanding practice, and the one closer to the doctrine, is a dedicated NOLOGIN role per sensitive function family. That role owns the functions and holds only the DML they need (DELETE on the target tables, INSERT on the archive). Doctrine-internal tension 2 is that "the same doctrine grants DELETE to one admin role for cache invalidation" (L525 note), which is the narrow-role pattern. L514 adds "narrow roles for sensitive features can be granted independently", and L184 says to grant the narrow attributes needed.
  - J6's resolution of tension 2 chose the broadest holder instead.
- **Evidence**: L182 (SRC-146: ownership rights cannot be granted separately), L184, L514, L525's tension note; J6 records GUARD.2 "Owner role" bullet, MAINTAIN.3 "Tamper detection".
- **Fix**: definer functions are owned by narrow NOLOGIN roles (for example a deletion role, a history-writer role, a cache-maintenance role), each holding only the DML it executes, with a fixed search_path. The owner role owns tables and runs migrations only. No consumer role is a member of these roles. State tension 2's resolution as "DELETE is held by a narrow non-login role that owns the deletion functions", which is consistent with L514 and L525. Mark it inferred.

**M4. J2 DATA.ORGANIZE: the higher normal forms do not "cost nothing", and the exemption condition is too broad.** Node: web-app-philosophy DATA.ORGANIZE (decision and rejected P2).
- **Issue**:
  - (a) Normalizing to Boyce-Codd normal form where candidate keys overlap is not always dependency-preserving. In such cases a functional dependency that one table's key enforced in third normal form now spans two tables and can no longer be enforced by a key. The verdict is stated as the max with no cost, while the cost is precisely an integrity cost: a rule that moves from a declarative key to a procedural cross-table check.
  - (b) The rejection says skipping analysis beyond third normal form is acceptable "when every table has a single candidate key and no multi-valued facts". Kent's own fifth-normal-form example (agents, companies, products) is an all-key table with one composite candidate key, and it still needs fifth normal form. The known sufficient condition is narrower: a third-normal-form table whose candidate keys are all single columns.
  - (c) SRC-254 (Kent) is cited for Boyce-Codd normal form, but the paper covers first to fifth normal form and does not discuss Boyce-Codd (fetched and checked).
- **Evidence**: J2 records DATA.ORGANIZE ("costs nothing there", "Acceptable not to analyze beyond third normal form when..."); SRC-254 (fetched: no Boyce-Codd section; section 5 notes that "certain redundancies seem to be unavoidable"); the Boyce-Codd normal form article, which states that "In some cases, a non-BCNF table cannot be decomposed into tables that satisfy BCNF and preserve the dependencies that held in the original table", with its "nearest shops" example (fetched; encyclopedic, not in the ledger).
- **Fix**:
  - Decide "normalize to Boyce-Codd, fourth and fifth normal form where they apply; where a Boyce-Codd decomposition loses a dependency, the lost dependency is enforced by a constraint trigger under DATA.GUARD's rule (Serializable or a lock)". Under the max rule that keeps both "each fact once" and "every rule enforced".
  - Narrow the exemption to "every candidate key is a single column, and no multi-valued facts".
  - Cite SRC-254 for fourth and fifth normal form only, and mark the Boyce-Codd claim as inferred, or add a source.

### Minor

**m1. J6 ORGANIZE.2, L503 (key width): sound verdict, mislabelled ground.** An overflowing key refuses writes. That is a loss of availability and changeability, not of integrity, since no stored fact becomes wrong. The verdict holds on J1's own tie-break, "the force whose loss is hardest to repair later wins" (a rewrite of the table and every referencing column at its largest, L197). **Fix**: state that ground, not "storage, which the node does not trade integrity for".

**m2. J6 GUARD.1, L493 (hierarchies): sound verdict, partly wrong ground and one invented attribution.**
- A closure table does carry foreign keys on both ancestor and descendant. What no constraint protects is its transitive completeness. Only materialized path and nested set list ancestors with no foreign key.
- "A fixed-depth hierarchy is one table per level, as L493 prefers": L493 says no such thing.
- The acyclicity check is a multi-row rule, so the record should say it runs under Serializable or with a lock (CONCURRENCY.1).

**Fix**: correct the ground per form, mark the fixed-depth rule as inferred, and add the isolation clause.

**m3. J6 GUARD.4, L529 (updated_at): sound verdict, one weak ground.**
- The record cites "timestamp-based readers (L594)". L594 is about sequence ids, and its application to `updated_at` is marked "plausibly ... inferred" in the ledger. J6's own CONCURRENCY.5 also forbids bare timestamp cursors. The verdict rests safely on "every writer" plus L537.
- L529's stated reason, avoiding WAL traffic and needless trigger work, can also be met at the table: the trigger stamps only when NEW IS DISTINCT FROM OLD (inferred).

**Fix**: drop or qualify the L594 ground and add the stamp-on-change form.

**m4. J6 ORGANIZE.3: one departure from L498 is not counted against the doctrine.** L498 (MAINT): "every table carries created_at and updated_at". J6 omits updated_at on append-only tables and gives them "only their record time". The departure is harmless, but it is unrecorded in the against-doctrine list and the state calls it only "unvalidated". **Fix**: list it as a partial departure, or keep `created_at` as the record-time name so that only `updated_at` departs.

**m5. J6 DERIVE.2, UNLOGGED: the stated consequence is probably wrong.** The Postgres manual says only that the "contents of an unlogged table are also not replicated to standby servers" (fetched). As far as I recall, a query on an unlogged table during hot-standby recovery raises an error rather than returning no rows. I did not check that against a source. Either way, the rule (no UNLOGGED where a replica reader needs the data) stands. **Fix**: write "unavailable on a standby" instead of "would read them empty".

**m6. J6 CONCURRENCY.1/.2: nobody owns the retry for consoles and scripts.** Under Serializable every writing caller must retry 40001 and 40P01. J6 hands the retry only to the backends (J7) and the job runner. MD-03's operator consoles and scripts also call writer functions. **Fix**: add "every consumer that calls a writer function owns a bounded retry; the shared specification names it", and hand it to J9 for console tooling.

**m7. J6 INTERFACE.2: the prepared-statement rule may be dated and has a stack consequence.** "Prepared statements ... are not used through it (L200)" stays the safe default. However, as I recall, PgBouncer 1.21 and later support protocol-level prepared statements in transaction mode, and Python drivers that cache prepared statements by default must be configured to match. I did not check either point in a source. **Fix**: hand the driver configuration to J7 or J9 and mark the PgBouncer version point for research.

**m8. J2 accounting on L517.** J2's pinned block says "0 new" verdicts against the doctrine and that L517 is "flagged, not judged". Yet DATA.MAINTAIN records "Rejected: P3' narrowed" and the state `conflict: narrows L517`. J6 then decides the same row and counts it as new. **Fix**: in J2, keep the clause as a principle-level requirement ("an incompatible change keeps every running consumer working"), remove the `conflict` state, and leave the L517 verdict with J6 alone, so the graphs carry the conflict once.

## Checks of the maintainer decisions

- **MD-01**: applied in J6 GUARD.3, ORGANIZE.6 and ROW_SECURITY. The tension with L619 and L688 is recorded and not overridden. One overstatement remains: "excluded either way" (B1).
- **MD-02**: applied. The schema is the origin of stored facts, and the origin of interface-only facts is decided per project (J6 ORGANIZE; J2 DATA.MAINTAIN).
- **MD-03**: applied throughout and used as the main ground for every verdict that departs from the doctrine. The two places where it is not followed through are M2 and the fairness gap in M1.
- **J1 placements**: no authority, copy or forbidden tier is changed. The exception is B1, which narrows J1's recorded default.

## Nodes found sound

J2 (web-app-philosophy):
- DATA: an honest roll-up; the structure gap (no DATA.INTERFACE) is correctly raised.
- DATA.GUARD: the six ways each realize a J1 verdict. L043 and L476 are well used. Only B1 needs fixing.
- DATA.MAINTAIN: separating the origin of change (migrations) from the truth of state (the live database) is a sound reconciliation of L046 and L474. Expand, migrate, contract is the max under MD-03 (see m8 for the accounting).
- DATA.DERIVE: the doctrine (L488) adopted as the max; stored predicates allowed only as generated columns.

J6 (pig-web-defaults):
- DATA, ORGANIZE, GUARD, CONCURRENCY, MAINTAIN, DERIVE: faithful roll-ups.
- ORGANIZE.1: arrays bound to the column.
- ORGANIZE.2: composite scope-leading keys; soft delete correctly removed as a criterion of key shape (tension 1 is grounded in the doctrine research); UUIDv7 only with a reason (see m1).
- ORGANIZE.3: precise types adopted; collation correctly left open with requirements (see m4).
- ORGANIZE.4: the naming doctrine adopted whole.
- ORGANIZE.5: JSON validation bound by trigger, consistent with GUARD.2.
- ORGANIZE.6: the API schema justified by its access need; tenancy under MD-01.
- ORGANIZE.7: indexes adopted, with the predicate-lock link to L574.
- GUARD.1: constraints required and L492 adopted as the stricter max (see m2).
- GUARD.3: context passed transaction-locally and the actor pairing checked (see B1 for the wording).
- GUARD.4: a closed list of trigger work (see m3).
- CONCURRENCY.1: Serializable on every writing role is the max for integrity, with versions on user-edited rows (see m6).
- CONCURRENCY.2 to .4: mechanics adopted; the L572/L587 tension resolved by keying.
- CONCURRENCY.5: claim-and-mark first, then the xid8 horizon; a guarantee chosen over a heuristic.
- CONCURRENCY.6: L597 adopted; observe-only mode limited to migration.
- MAINTAIN.1: online-safe migrations; the drift gate correctly marked inferred.
- MAINTAIN.3: trigger-written history with the session role and the actor; tamper detection honestly left open (see M3).
- MAINTAIN.4: the bulk-job doctrine adopted whole within the owner-run path.
- MAINTAIN.5: point-in-time recovery proven by rehearsed restore.
- DERIVE.1: every copy carries a drift guard (see M2 for the mechanism).
- DERIVE.2: SKIP LOCKED fills the doctrine's gap 6; single-owner caches limited (see m5).
- INTERFACE.1: L516 adopted; the override flag restricted; breaking changes by expand, migrate, contract (see B1).
- INTERFACE.2: transaction pooling with per-role limits and timeouts (see m7).
