# Result: review of the DATA branch (J2 philosophy DATA, J6 Postgres data tier)

## L1 headline

The DATA branch is mostly sound, but it is not ready to build. The one blocking finding: both units record a narrower default than J1's for the open per-user read-visibility question. J1 keeps read functions "acceptable when a per-user read rule must hold for two or more backends"; J2 and J6 forbid them until the maintainer answers.

Four major fixes:
- J6's deletion question admits its options differ only in integrity, so the max rule should decide it.
- Two of J6's safeguards rely on writer functions where its own rule requires the table.
- Privileged functions run with the owner role's rights.
- J2 says the higher normal forms "cost nothing".

All five verdicts against the doctrine hold. Three need their grounds corrected.

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

## L2 claims

- **B1, read visibility (blocking)**:
  - J1's "if unanswered" record has two parts: A is provisional, with one written specification per rule and shared denial tests, and B is acceptable when a per-user read rule must hold for two or more backends.
  - J2 and J6 carry A only and turn B's condition into a prohibition. J6 INTERFACE says "not part of the API until answered".
  - Under MD-03's shared database, B's condition is easily met, so the PIG-WEB nodes would contradict ALLOCATION.GUARD.3.
  - "Row security excluded either way" also overstates MD-01, which allows it under three conditions.
  - Fix: record J1's default word for word in every carrying node.
- **M1, deletion question (major)**:
  - Both options keep deleted data recoverable, and J6 says the difference is integrity. On the node's own forces, B (archive by default, soft delete where the product offers undo) therefore dominates.
  - J6 decided four other doctrine conflicts in favour of the max but defers this one.
  - The framing leaves out two things: reporting consumers that need deleted rows in historical figures must union the archive under B, and B also needs cascade-aware deletion functions, because L492 forbids CASCADE on core entities.
  - Fix: decide B against L520, or reframe the question around the real cross-branch force and add both costs.
- **M2, safeguards bound to functions (major)**:
  - J6 binds rules to the table in ORGANIZE.1, ORGANIZE.5 and GUARD.4, because owner-run jobs and DB_API's direct-write exception skip writer functions.
  - Two rules break that pattern. Soft-delete safeguard 1 (no active child under a deleted parent) and DERIVE.1's "writer function" option for decision-relevant copies sit in writer functions only.
  - Fix: a constraint trigger for safeguard 1, and DERIVE.1's top rung as a trigger unless the source admits no other writer.
- **M3, owner-owned definer functions (major)**:
  - An owner holds rights that cannot be granted separately (L182, SRC-146), including disabling the history triggers, and J6 itself calls for tamper detection because of this.
  - A narrow NOLOGIN role that owns each sensitive function family is closer to L514 ("narrow roles for sensitive features") and to the doctrine's own DELETE-holding admin role (L525's tension note).
  - Fix: narrow definer roles. The owner owns the tables and runs migrations only.
- **M4, normal forms (major)**:
  - A Boyce-Codd decomposition is not always dependency-preserving, so the "max" has an integrity cost.
  - The exemption "single candidate key, no multi-valued facts" misses Kent's all-key fifth-normal-form example.
  - Kent (SRC-254) does not cover Boyce-Codd normal form at all.
  - Fix: decompose and enforce any lost dependency with a constraint trigger; narrow the exemption to single-column candidate keys; correct the citation.
- **Minor (8)**:
  - m1: L503's ground should be J1's "hardest to repair later" rule, not integrity.
  - m2: L493's ground is wrong for closure tables, the fixed-depth rule is misattributed to L493, and the acyclicity check needs Serializable or a lock.
  - m3: L529's ground leans on the inferred part of L594; add stamp-on-change.
  - m4: the departure from L498 on append-only tables is not counted.
  - m5: UNLOGGED tables on a standby are probably unavailable, not empty (my recollection, not checked in a source).
  - m6: no owner for the retry in consoles and scripts under Serializable.
  - m7: the prepared-statement rule may be dated (as I recall, PgBouncer 1.21 and later; not checked); the Python driver configuration is not handed off.
  - m8: J2 both says it does not judge L517 and records a conflict on it.
- **Maintainer decisions**: MD-01, MD-02 and MD-03 are applied faithfully. The exceptions are B1's wording on MD-01 and M2, where MD-03's every-writer rule is not followed through.
- **J1 placements**: no authority, copy or forbidden tier is changed. B1 narrows J1's recorded default.
- **Sound**: the 4 J2 nodes and the 33 judged J6 nodes are sound apart from the clauses above. One line per node is in `review.md`.

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

## L3 full

### Files

- `review.md` (this folder): each finding with its severity, node, issue, evidence and proposed fix; then the checks of the maintainer decisions; then one line per node found sound.
- `result.md`: this file.

### Method

- **Read in full**: `../../target_hierarchy.md`; `../../maintainer_decisions.md`; `../J1_allocation/allocation_matrix.md` and `../J1_allocation/questions.md`; the three files of `../J2_phil_data/` and of `../J6_pig_data/`.
- **Ledger rows checked against the judges' citations**: L037 to L047, L072, L168 to L187, L192, L197, L204, L205, L216, L420, L469 to L476, L485, L488 to L504, L509 to L512, L514, L516, L517, L519 to L525, L529 to L533, L536 to L538, L540, L543, L545, L566, L568 to L577, L581, L584, L585, L587, L594 to L598, L618, L619, L622, L626, L627, L684, L685, L688.
- **Doctrine research** (`../../../research/15_maintainer_doctrine/result.md`): the six doctrine-internal tensions and the D1 and D2 answers, to check tension 1 (soft delete and key shape) and the deletion question.
- **Sources fetched where the stakes were high**:
  - SRC-254 (Kent): it does not discuss Boyce-Codd normal form, and it notes unavoidable redundancies.
  - The encyclopedic Boyce-Codd normal form article: a decomposition can fail to preserve dependencies.
  - The Postgres CREATE TABLE manual on UNLOGGED tables.
- **Not checked in a source**: two points from memory are marked as such (m5, m7).
- **Checks run per node**: (a) hedging; (b) grounding and certainty words; (c) consistency with J1, with MD-01 to MD-03, between the two units, and across J6's own siblings; (d) a stronger position missed; (e) whether the max rule supports each verdict against the doctrine; (f) the questions.

### What decides each finding

- **B1**: J1's "If unanswered, the graph records" paragraph is the stated default the task requires to be kept. The two units' wording ("until answered", "if the maintainer chooses read functions instead") removes B's "acceptable when". Severity is blocking because a refining node would contradict the placement it realizes, on the one clause the maintainer has not yet settled.
- **M1**:
  - The test is target_hierarchy's definition of `undecided`. J6's records name two forces. Its own question then states that both options recover deleted data and that the difference is integrity, which leaves one force the node serves and B ahead on it.
  - The cost that does remain, immediate undo, belongs to INTERACTION, and B keeps soft delete where undo is offered.
  - The fairness gaps come from MD-03 (reporting consumers) and from L492 (no CASCADE on core entities).
  - Major, not blocking: the maintainer would still see the choice. The issue is a question framed against its own reasoning.
- **M2**:
  - Internal consistency: J6 states the every-writer rule as its headline and applies it three times. Its exceptions to the rule are DB_API's direct single-table writes and owner-run jobs, which are the very writers the two flagged rules would miss.
  - The fix uses J6's own mechanism (constraint triggers under CONCURRENCY.1).
- **M3**:
  - Postgres ownership semantics (L182 via SRC-146) and the doctrine's own narrow-role pattern (L514; L525's note) support a narrower definer role.
  - J6's MAINTAIN.3 concedes the owner's bypass.
  - The fix is inferred from those rows; no source states it as a rule.
- **M4**:
  - Standard dependency theory: Boyce-Codd decompositions may lose dependencies.
  - Kent's 5NF example shows the exemption fails for a single composite key.
  - The citation was checked by reading Kent.
  - The fix keeps the max for both "each fact once" and "every rule enforced".
- **Minors**: each is a ground, attribution or bookkeeping correction that leaves the verdict standing (m1 to m4, m8), a factual nuance (m5, m7), or a missing hand-off (m6).

### Verdicts against the doctrine, one by one

| Row | Unit | Verdict | Is the max rule on the judge's side? |
|---|---|---|---|
| L471 | J1 → J2, J6 | declarative constraints required | yes (inherited; only declared constraints bind every writer) |
| L517 | J2 narrows, J6 decides | breaking function-API changes go expand, migrate, contract | yes (MD-03 consumers deploy on their own schedules) |
| L529 | J6 GUARD.4 | updated_at set by a narrow trigger | yes (every writer); tighten the ground (m3) |
| L503 | J6 ORGANIZE.2 | 8-byte keys unless size is bounded by design | yes, on J1's hardest-to-repair rule, not on integrity (m1) |
| L493 | J6 GUARD.1 | declared parent foreign key; other forms derived | yes; correct the closure-table ground (m2) |
| L498 | J6 ORGANIZE.3 | no updated_at on append-only tables | harmless; not counted (m4) |
| L499, L525 (tensions 1, 2) | J6 | soft delete not a key criterion; DELETE held by function owner | tension 1 sound; tension 2 should go to a narrow role, not the owner (M3) |
| L520 | J6 MAINTAIN.2 | left undecided | the max favours B; decide it (M1) |

### Questions, one by one

- **J2: none.** Sound. The Boyce-Codd case in M4 is decided by the max (decompose and enforce the lost dependency), not asked.
- **J6 Q1, the deletion default.** Not a genuine trade-off between DATA forces as written. Preferred: decide B as a partial verdict against L520. Alternative: keep the question with a corrected reason and a balanced framing (M1). Its "if unanswered" default (L520 with three safeguards) follows J1's pattern. Safeguard 1 must then be a constraint trigger (M2).

### Scope kept

- Written only in this folder.
- No judge file edited, nothing committed, no absolute path or private name written.

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
