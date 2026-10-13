# Result: J5 web-app-philosophy TRANSVERSE judged

## L1 headline

All 14 TRANSVERSE nodes of `web-app-philosophy` are decided under the max rule, and the adversarial review of the branch is applied: 9 of its 14 findings touch this unit, all applied, none rejected. The nodes realize the settled allocation verdicts and the maintainer's default context: a database shared by several backends and by BI, consoles and scripts (MD-03). In one line each:
- **Security**: whole-site HTTPS and data minimisation; every threat category owned by a tier the requester cannot modify; insecure design answered by a threat model per placement and critical flow, with misuse-case tests.
- **Performance**: field measurement at the 75th percentile is the truth; lab budgets are the gate.
- **Contracts**: every contract is an explicit artifact, kept in sync and changed additively; a break goes expand, migrate, contract, unless every consumer ships in the same deployment as the migration.
- **Operability**: one correlation id from browser to database transaction; tests at the lowest level that catches each failure, data logic on the real engine, concurrency tested with committing sessions in a disposable database; one immutable build with migrations in the pipeline.
- **Evolution**: recorded decisions; small increments with automated fitness checks; each backend one deployable, not split without a measured need; few mature technologies; teams by capability, cross-domain operations composed in the database.

There are no questions. No departure from the maintainer's codified practice is counted here: the L517 narrowing is realized and counted at its owner in the stack graph. The open read-visibility question is recorded as awaiting maintainer, with its default, not settled.

Pinned:
- Nodes judged: 14 of 14 (web-app-philosophy TRANSVERSE; 3 roll-ups judged from their children: TRANSVERSE, TRANSVERSE.OPERABILITY, TRANSVERSE.EVOLUTION).
- Decided 14, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: TRANSVERSE.SECURITY and TRANSVERSE.OPERABILITY.2. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0.
- Verdicts against the maintainer doctrine: 0 counted here. TRANSVERSE.CONTRACTS realizes the L517 narrowing, counted once at its owner, PIG-WEB.DATA.INTERFACE.1 (J6): "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (L047). L517's coordination with every consumer and its "no formal version numbers" are kept; the new function name that carries the change is the expand step, the route the maintainer's own L512 already takes for stored contract schemas.
- Conflicts with J1 placements: 0. L098 read against ACT.4: business data changes stay out of the security event log (the business history is the database's, L049); security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events.
- Tensions recorded, not overridden: (a) EVOLUTION.3: several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need; L116's separate data schemas become domain schemas in the shared database (L513); L044 stays as J1 rejected it. (b) EVOLUTION.5: L068 (no teams by layer) against L515's database owner: each capability team owns its domain schema and its functions; a cross-schema business function belongs to the team that owns the workflow, reviewed by one named owner role (inferred). (c) OPERABILITY.2: L042's in-memory testing advantage is lost for the logic MD-03 puts in the database; those tests run on the real engine, rolled back by default, and behaviour that only shows at commit or between sessions is tested with committing sessions in a disposable database, never a shared one (L399, L400, L567).
- Gaps in the evidence: (1) PERFORMANCE owns one row and no row measures server or database time: whole-path measurement inferred (L095, L376, L382). (2) OPERABILITY.1: carrying the correlation id into the database transaction and audit rows inferred (L371, L566, L658). (3) OPERABILITY.2: no ledger row on concurrency testing; the concurrency tests themselves are required (inferred from GUARD.2), part of the default suite. (4) SECURITY: L303's tier map is inferred and assigns 7 of 10 categories; A06, A08 and A10 are assigned here, inferred, A06 and A08 corrected against the OWASP Top 10:2025 text; the ASVS chapter list (L304) is not read, its level definitions are. (5) The 3 roll-ups own no row.
- Review fixes: 9 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, m1, m4, m5, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

Files: `records.md` (one judge record per node), `questions.md` (none; the open read-visibility question and the flagged narrowing, in plain words), this file.

## L2 claims

### Review fixes

Applied from `../review_transverse/review.md` and `../cross_branch_fixes.md`; 0 rejected.
- **B1 / X3** (EVOLUTION.5): one business operation is one database function call in its own transaction; a database function may call another domain's published functions inside it; only direct access to another domain's tables is forbidden across domains.
- **M1 / X2** (CONTRACTS): the L517 narrowing is cited here, counted at PIG-WEB.DATA.INTERFACE.1; one lockstep condition, word for word; the new name credited to the expand step and L512.
- **M2 / X4** (OPERABILITY.2): rollback by default; commit-time and concurrent behaviour tested with committing sessions in a disposable database; concurrency tests for GUARD.2 in the default suite.
- **M3 / X5** (EVOLUTION.3, EVOLUTION roll-up): "one backend deployable" replaced; a later split moves no data (inferred).
- **M4** (SECURITY): A08 to the pipeline and the parsing tier; A06 as a threat model with misuse-case tests; A04 completed; the whole map unvalidated.
- **m1** (SECURITY): ASVS level definitions grounded; L304's level part no longer open.
- **m4** (OPERABILITY.1): only business data changes stay out of the security log.
- **m5** (EVOLUTION.5): cross-schema business functions owned by the workflow's team, reviewed by the owner role.
- **m7 / X1** (SECURITY, OPERABILITY.2): one notation for the pending clause, with default, fallback and consequence; added to OPERABILITY.2's state.
- **X7** (CONTRACTS): "always in sync" and the compatibility window cover every interface description, the agent tool surface included.

### Verdicts

Default context: MD-03 as restated by J1 (`../J1_allocation/allocation_matrix.md`). Each line is a node's verdict and its proposed `epistemic_state`. Evidence ids resolve in `../../02_skeleton/claims_ledger.md`.

- **TRANSVERSE** (roll-up): each cross-tier property is stated once and designed in across every tier and database consumer (L096), checked automatically where a check exists (L110). `known | gap: roll-up`.
- **TRANSVERSE.SECURITY**:
  - HTTPS everywhere with HSTS (L029, L030); minimal collection and no secrets in logs or trace context (L035, L036).
  - Every OWASP Top 10 category has an owning tier the requester cannot modify (L303, RULES.3), named through the placements. A06: a threat model per placement and critical flow, with misuse-case tests per tier. A08: the pipeline (signed provenance, trusted sources, reviewed changes) and the parsing tier for untrusted serialized input. A04: backend, proxy, database connections, storage at rest.
  - Access control follows GUARD.3 (MD-01, MD-03). Per-user read visibility across backends: recorded default (each backend filters from a shared specification, shared denial tests; read functions with the verified actor acceptable for two or more backends); reporting and operator roles see every row unless restricted.
  - The Top 10 is an awareness map; the requirement set is a verifiable catalogue at a risk-chosen level, Level 2 being what most applications should strive for (L304, ASVS 5.0 text).
  - `known | unvalidated: whole tier map, A06/A08/A10 added, A04 completed | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **TRANSVERSE.PERFORMANCE**:
  - Field data at the 75th percentile by device class is the truth (L015, L381). Lab budgets gate changes (L296) and never override it. Optimise only after measurement (L097).
  - Page metrics are joined to server and database time through the correlation id (inferred). It feeds FORCES.3 and FORCES.4.
  - `known | unvalidated: whole-path join | gap: one row`.
- **TRANSVERSE.CONTRACTS**:
  - Every contract is an explicit artifact with meaning (L483). Its origin is per RECORD.3 and it stays in sync by a CI gate (MD-02), for the HTTP description, the function API catalogue and the agent tool surface alike. The provider contract is authoritative (L487).
  - Changes are additive (L056) and readers tolerant (L057); usage is known before any removal (L058).
  - A break goes expand, migrate, contract (L047), the function API included, with coordination and no version numbers kept (L517); the new name is the expand step (L512). "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration.
  - Counted at PIG-WEB.DATA.INTERFACE.1, not here.
  - `known | conflict: L517 "deployed together" narrowed (counted at INTERFACE.1) | unvalidated: usage per consumer role`.
- **TRANSVERSE.OPERABILITY** (roll-up): observed, tested and delivered as one whole (L096). `known | gap: roll-up`.
- **TRANSVERSE.OPERABILITY.1**:
  - One correlation id from browser to database transaction, on logs, spans, client events and audit rows (L095, L371, L382, L658).
  - The security event log holds L098's list, security-relevant data changes (privileges, roles, credentials, grants, the role-to-actor pairing) included; business data changes stay in the database's audit trail (L049, ACT.4).
  - Retention is recorded per record type, no shorter and no longer than obligations require (L048).
  - `known | unvalidated: id carried into the transaction`.
- **TRANSVERSE.OPERABILITY.2**:
  - Test at the lowest level that catches the failure (L396); the pyramid follows, with no fixed ratio (L099).
  - Database logic (business operations, writer functions, constraints, actor checks) is tested on the real engine, each test isolated by a rolled-back transaction by default (L399, L400); shared data only in never-committing transactions (L567). Commit-time and concurrent behaviour is tested with committing sessions in a disposable database, never a shared one. Every invariant GUARD.2 enforces procedurally has a concurrent test. Backend policy is tested in memory (L042).
  - Denial tests per role and actor, the first misuse-case tests; per-user read denial across backends: recorded default, awaiting maintainer. Few end-to-end tests (L397).
  - `known | unvalidated: concurrency tests required by GUARD.2 | gap: no row on concurrency testing | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **TRANSVERSE.OPERABILITY.3**:
  - One codebase, one immutable build promoted everywhere, configuration and secrets apart, same engine and version everywhere, small frequent releases (L100 to L104).
  - Migrations are versioned and promoted with the code (L519). They run once per release before the code (L405) and stay additive across the window.
  - `known | unvalidated: database as its own codebase`.
- **TRANSVERSE.EVOLUTION** (roll-up): deliberate change through recorded decisions, increments, deployables, technologies and teams. `known | gap: roll-up`.
- **TRANSVERSE.EVOLUTION.1**:
  - Name the costly decisions early, the allocation placements first. Decide each when enough is known (L073), from the properties (L106).
  - Record each with its forces, alternatives and reversing condition, MD-01 and MD-02 project decisions included, and test changes against it.
  - `known`.
- **TRANSVERSE.EVOLUTION.2**:
  - Quality from the start (L107); no speculative features (L108); deliberate debt only (L109); automated fitness functions (L110).
  - About 10x capacity headroom (L111), read as headroom for load, not for features (inferred).
  - `known | unvalidated: features against capacity split`.
- **TRANSVERSE.EVOLUTION.3**:
  - Several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need. Split only for independent deployability on proven boundaries, with the distribution premium budgeted (L073 to L080).
  - Bounded contexts become domain schemas in the shared database (L513); a new deployable reaches data through the function API with its own role (RECORD.2). A later split therefore moves no data; only deploy independence and the distribution premium remain (inferred).
  - Services-first is acceptable only under L117's conditions plus distributed-systems experience.
  - `known | unvalidated: contexts as schemas; a split moves no data | conflict: L044, L116 against MD-03`.
- **TRANSVERSE.EVOLUTION.4**:
  - Few mature technologies; a new one only past a measured limit, with its perpetual operating cost budgeted (L081 to L085); realized by POSTGRES_FIRST.
  - Paradigm choice inside a language (POLYGLOT) is out of scope.
  - `known | unvalidated: scope reconciliation`.
- **TRANSVERSE.EVOLUTION.5**:
  - Cross-functional teams by capability; structure designed with the teams (L068, L069).
  - The database owner is a role, not a layer team: per domain schema when teams multiply, with one owner role for cross-schema conventions (L513, L515).
  - Cross-domain operations are composed in the database: a function may call another domain's published functions in the same transaction, never its tables. A cross-schema business function belongs to the team that owns the workflow, reviewed by the owner role (inferred); this refines RECORD.2's single owner only when teams multiply.
  - `known | unvalidated: multi-team ownership, cross-schema functions`.

Pinned:
- Nodes judged: 14 of 14 (web-app-philosophy TRANSVERSE; 3 roll-ups judged from their children: TRANSVERSE, TRANSVERSE.OPERABILITY, TRANSVERSE.EVOLUTION).
- Decided 14, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: TRANSVERSE.SECURITY and TRANSVERSE.OPERABILITY.2. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0.
- Verdicts against the maintainer doctrine: 0 counted here. TRANSVERSE.CONTRACTS realizes the L517 narrowing, counted once at its owner, PIG-WEB.DATA.INTERFACE.1 (J6): "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (L047). L517's coordination with every consumer and its "no formal version numbers" are kept; the new function name that carries the change is the expand step, the route the maintainer's own L512 already takes for stored contract schemas.
- Conflicts with J1 placements: 0. L098 read against ACT.4: business data changes stay out of the security event log (the business history is the database's, L049); security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events.
- Tensions recorded, not overridden: (a) EVOLUTION.3: several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need; L116's separate data schemas become domain schemas in the shared database (L513); L044 stays as J1 rejected it. (b) EVOLUTION.5: L068 (no teams by layer) against L515's database owner: each capability team owns its domain schema and its functions; a cross-schema business function belongs to the team that owns the workflow, reviewed by one named owner role (inferred). (c) OPERABILITY.2: L042's in-memory testing advantage is lost for the logic MD-03 puts in the database; those tests run on the real engine, rolled back by default, and behaviour that only shows at commit or between sessions is tested with committing sessions in a disposable database, never a shared one (L399, L400, L567).
- Gaps in the evidence: (1) PERFORMANCE owns one row and no row measures server or database time: whole-path measurement inferred (L095, L376, L382). (2) OPERABILITY.1: carrying the correlation id into the database transaction and audit rows inferred (L371, L566, L658). (3) OPERABILITY.2: no ledger row on concurrency testing; the concurrency tests themselves are required (inferred from GUARD.2), part of the default suite. (4) SECURITY: L303's tier map is inferred and assigns 7 of 10 categories; A06, A08 and A10 are assigned here, inferred, A06 and A08 corrected against the OWASP Top 10:2025 text; the ASVS chapter list (L304) is not read, its level definitions are. (5) The 3 roll-ups own no row.
- Review fixes: 9 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, m1, m4, m5, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

## L3 full

### Review fixes

Sources: `../review_transverse/review.md` (14 findings) and `../cross_branch_fixes.md` (X1 to X7, applied verbatim, overriding the review where both speak). Each finding's evidence was checked against the ledger and the records before applying it; none was found wrong, so none is rejected. Every changed record ends with a **Review fixes** line in `records.md`.

| finding | records changed | change | evidence check |
|---|---|---|---|
| B1, X3 | EVOLUTION.5, EVOLUTION roll-up | Cross-domain business operations: one database function call in its own transaction; a database function may call another domain's published functions inside it; only direct access to another domain's tables is forbidden. The stack rule itself is J9's (PIG-WEB.TRANSVERSE.EVOLUTION.2). | ACT.1 row of the allocation matrix forbids "multi-table writes composed in a backend; a backend transaction wrapping several API calls": confirmed. |
| M1, X2 | CONTRACTS; pins | Lockstep condition replaced by X2's, word for word. The departure is cited, not counted: counted once at PIG-WEB.DATA.INTERFACE.1 (J6). The new function name is credited to the expand step and to L512, not to L517. L512 noted as already taking this route for stored contract schemas. | L517 reads "coordinated with every consuming team and deployed together; there are no formal version numbers": no new-name clause, confirmed. L512: new named version, old soft-deleted, gradual migration: confirmed. |
| M2, X4 | OPERABILITY.2, OPERABILITY roll-up, TRANSVERSE roll-up; pins | Each test isolated, rollback by default; commit-time and between-session behaviour tested with concurrent committing sessions in a disposable database, never a shared one; every invariant GUARD.2 enforces procedurally has a concurrent test, part of the default suite. Gap kept only for the missing source row. | L400 gives rollback "for example", L567 is scoped to shared environments: confirmed. |
| M3, X5 | EVOLUTION.3, EVOLUTION roll-up, TRANSVERSE roll-up; pins | "One backend deployable first" replaced by X5: several backends may share the database; each backend is one deployable, not split into services without a measured need. Added: a later split moves no data, only deploy independence and the distribution premium remain (inferred). | MD-03 default context and L074, L076 read: confirmed. |
| M4 | SECURITY; pins | A08: pipeline (signed provenance, trusted sources, review, segregated CI/CD) and parsing tier for untrusted serialized input; declarative constraints dropped. A06: threat model per placement and critical flow, misuse-case tests per tier; allocation records are its input. A04: backend, proxy, database connections, storage at rest. Whole map `unvalidated`. A rejected line added for allocation records as the whole answer to A06. | The review fetched the OWASP Top 10:2025 A06 and A08 pages; their definitions are consistent with SRC-115's category names already in the record. Accepted as grounded by the review. |
| m1 | SECURITY (P4, verifiability); pins gap (4) | ASVS level definitions grounded: Level 2 is what most applications should strive for; the level is chosen by risk. L304's chapter list stays unread. | The review read the ASVS 5.0 text at tag v5.0.0; the ledger still marks L304 `open` (to be updated by the ledger owner, outside this unit's scope). |
| m4 | OPERABILITY.1; pins | "Data-change events stay out" narrowed to business data changes; privilege, role, credential, grant and role-to-actor changes are security events. | L098 lists "use of higher-risk functionality": confirmed. |
| m5 | EVOLUTION.5, EVOLUTION roll-up; pins | Cross-schema business functions owned by the team that owns the workflow, reviewed by the owner role; the multi-team arrangement marked as the condition that refines RECORD.2's single owner (inferred). | RECORD.2 names one database owner (L515): confirmed. |
| m7, X1 | SECURITY, OPERABILITY.2; How to read; pins; questions | One notation, X1's: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default, J1's fallback (read functions with the verified actor, acceptable for two or more backends) and the SELECT-role consequence stated. Clause added to OPERABILITY.2's state. | J1 Q1's "if unanswered" text records A (each backend filters): consistent. |
| X7 | CONTRACTS | "Always in sync" and the compatibility window apply to the HTTP description, the function API catalogue and the agent tool surface. | MD-02 read: consistent. |

Not touching this unit: M5, M6, m2, m3, m6 (J9 nodes only); X6 (no URL-borne credential in these nodes).

### What was read

- `../../target_hierarchy.md` (whole), `../../maintainer_decisions.md` (MD-01 to MD-03), `../../02_skeleton/judge_plan.md` (section J5).
- `../J1_allocation/allocation_matrix.md` (whole) and, in `../J1_allocation/records.md`: the default context, the access paths, and the records of FORCES.3, FORCES.4, RULES.3, RECORD.3 and ACT.4; `../J1_allocation/questions.md` for the open read-visibility question.
- `../../02_skeleton/skeleton.md`: the TRANSVERSE tree, node table and intentlinks.
- Ledger: the 44 owned rows in full (L015, L029, L030, L035, L036, L048, L056 to L058, L068, L069, L073 to L085, L095, L096, L098 to L112, L303, L483, L487). Also every MAINT row, and the rows owned elsewhere that the records cite as positions or grounds: L009, L019, L042, L044, L047, L049, L113 to L124, L129 to L133, L275 to L278, L295, L296, L304, L369 to L382, L392, L396 to L405, L512, L513, L515, L517, L519, L533, L545, L556, L559 to L567, L607, L613, L614, L622, L634, L635, L658.
- Sources: tiers resolved for the cited ids. No research result opened: no owned row was too compressed to judge.
- For the review fixes: `../review_transverse/review.md`, `../cross_branch_fixes.md`; ledger rows L098, L400, L512, L513, L515, L517, L567 re-read.

### Method

- Each node was judged as the realization of the settled placements: J1's verdicts are cited, never re-decided.
- MAINT rows weighed as strong positions.
- Where a MAINT row and a grounded research row differed (L517 against L047), the more demanding practice for the node's purpose was chosen and the departure flagged; after review it is counted at its owner node only.
- Positions owned by stack nodes (`pig-web-defaults`) were read as evidence for the principle and left to their judge for the stack choice.

### Verdicts by node

Full records, positions, forces, rejected positions with their winning conditions, and placement links: `records.md`. In brief, with what each verdict turns on:

1. **TRANSVERSE** (roll-up). Turns on L096, which makes every transverse property whole-system, and L110, which makes fit automated.
2. **TRANSVERSE.SECURITY**. Turns on RULES.3: each threat category gets an owning tier the requester cannot modify.
   - L303 assigns 7 of the 10 categories (A01, A02, A03, A04, A05, A07, A09); A04 is completed with the proxy, database connections and storage at rest. The record adds A06 (a threat model per placement and critical flow, with misuse-case tests), A08 (the pipeline and the parsing tier for untrusted serialized input) and A10 (fail closed in the tier that holds the check). The whole map is inferred.
   - A01 follows GUARD.3 as J1 settled it; per-user read visibility across backends stays at the recorded default, awaiting maintainer, with its fallback and the SELECT-role consequence.
3. **TRANSVERSE.PERFORMANCE**. Field truth (L015) against lab gates (L296): both kept, field authoritative.
   - The whole-path extension is inferred. It is needed because MD-03 moves per-request work into database functions, which page metrics alone cannot see.
4. **TRANSVERSE.CONTRACTS**. The node's purpose is compatible evolution so that components upgrade independently (L056).
   - Expand, migrate, contract (L047) serves that purpose better than a lockstep deploy (L517). Under MD-03 the database, several backends, BI and scripts deploy separately, and browser tabs keep old code (L009, L278). "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration.
   - L517's coordination and its rule against version numbers are kept; the new name is the expand step (L512). The departure is counted at PIG-WEB.DATA.INTERFACE.1. The verdict fills in what J1's "marked coordinated" gate on the function-API catalogue diff requires; it does not change that placement.
5. **TRANSVERSE.OPERABILITY** (roll-up).
6. **TRANSVERSE.OPERABILITY.1**. The correlation id reaches the database transaction (inferred from L371, L566, L658).
   - L098's "data-change events optional" applies to the security event log only; business data changes stay in the database's audit trail (ACT.4), security-relevant changes go to the security log. The skeleton's conflicts link is realized by keeping the two records apart.
7. **TRANSVERSE.OPERABILITY.2**. L396 (lowest level that catches) is the rule; the pyramid (L099) is its usual result.
   - MD-03 puts business operations in the database, so their low-level tests run on the real engine, rolled back by default; commit-time and concurrent behaviour runs with committing sessions in a disposable database (L399, L400, L567, MAINT). This is the price recorded in FORCES.6 (L042, L472). Concurrency tests for GUARD.2's procedural invariants are required.
8. **TRANSVERSE.OPERABILITY.3**. Consensus on all five rows. The extension to migrations (L519, L405) and to the database as its own codebase is inferred from L100 and L515.
9. **TRANSVERSE.EVOLUTION** (roll-up).
10. **TRANSVERSE.EVOLUTION.1**. L105 and L106 against L073: name the costly decisions early, decide them when enough is known. The allocation placements and the MD-01 and MD-02 project decisions are its first instances.
11. **TRANSVERSE.EVOLUTION.2**. L108 (no speculative features) and L111 (about 10x headroom) are reconciled by object: features against capacity, inferred.
12. **TRANSVERSE.EVOLUTION.3**. Monolith first (four sources) against services-first (L117, contested): each backend one deployable, not split without a measured need; services-first only under its stated conditions.
    - Under MD-03, L116's separate data schemas become domain schemas in the shared database (L513), inferred. Every split keeps one system of record (RECORD.1, RECORD.2) and moves no data.
13. **TRANSVERSE.EVOLUTION.4**. Few mature technologies, realized in the stack graph by POSTGRES_FIRST, CACHE_STORE and JOB_HOST. The conflict with POLYGLOT is settled by scope: technologies, not paradigms; inferred.
14. **TRANSVERSE.EVOLUTION.5**. L068 against L515's database owner: the owner is a role inside one cross-functional team. When teams multiply, ownership goes per domain schema, with one role for cross-schema conventions, and a cross-schema business function belongs to the workflow's team; inferred. Cross-domain composition happens in the database (X3).

### Links to the placements (realized or cited, none re-decided)

| node | skeleton link | J1 placements the verdict rests on |
|---|---|---|
| TRANSVERSE.SECURITY | refines RULES.3 | GUARD.1, GUARD.2, GUARD.3 (MD-01, MD-03; read visibility awaiting maintainer), GUARD.4, ACT.4, access paths |
| TRANSVERSE.PERFORMANCE | dataflow FORCES.3, FORCES.4 | RULES.2 (L607) |
| TRANSVERSE.CONTRACTS | requires RECORD.3 | RECORD.2 (function API, MD-03), MD-02 |
| TRANSVERSE.OPERABILITY.1 | conflicts ACT.4 | ACT.4 (role and claimed actor recorded) |
| TRANSVERSE.OPERABILITY.2 | none | FORCES.6, GUARD.2, GUARD.3, ACT.1, ACT.4 |
| TRANSVERSE.OPERABILITY.3 | none | RECORD.2, RECORD.3 |
| TRANSVERSE.EVOLUTION.1 | none | the allocation placements as first instances; MD-01, MD-02 |
| TRANSVERSE.EVOLUTION.3 | none | RECORD.1, RECORD.2 |
| TRANSVERSE.EVOLUTION.4 | none | PIG-WEB.ALLOCATION.POSTGRES_FIRST, CACHE_STORE, JOB_HOST |
| TRANSVERSE.EVOLUTION.5 | none | RECORD.2 (database owner, L515), ACT.1 (one call per operation) |

### For the stack judge (J9), who reads these verdicts

- PIG-WEB.TRANSVERSE.SECURITY.1: the philosophy node requires a verifiable catalogue at a risk-chosen level; the catalogue is J9's. Its level definitions are now grounded (ASVS 5.0: Level 2 for most applications).
- PIG-WEB.TRANSVERSE.SECURITY.5: it realizes the A08 owner as well as A03 (signed provenance, trusted sources).
- PIG-WEB.TRANSVERSE.CONTRACTS.1: whether a single team's browser client needs consumer-driven tests (L560) is left to J9.
- PIG-WEB.TRANSVERSE.OPERABILITY.1 and .5:
  - how the correlation id enters the transaction (the inferred carrier is a transaction-local setting beside the actor, L566);
  - concurrency behaviour is tested with concurrent committing sessions in a disposable database, part of the default suite.
- PIG-WEB.TRANSVERSE.EVOLUTION.1 and .2: the default deployable and module cut follow EVOLUTION.3 (each backend one deployable, domain schemas); cross-domain operations are database functions any module may call within its role's grants (EVOLUTION.5, X3).

Pinned:
- Nodes judged: 14 of 14 (web-app-philosophy TRANSVERSE; 3 roll-ups judged from their children: TRANSVERSE, TRANSVERSE.OPERABILITY, TRANSVERSE.EVOLUTION).
- Decided 14, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: TRANSVERSE.SECURITY and TRANSVERSE.OPERABILITY.2. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0.
- Verdicts against the maintainer doctrine: 0 counted here. TRANSVERSE.CONTRACTS realizes the L517 narrowing, counted once at its owner, PIG-WEB.DATA.INTERFACE.1 (J6): "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (L047). L517's coordination with every consumer and its "no formal version numbers" are kept; the new function name that carries the change is the expand step, the route the maintainer's own L512 already takes for stored contract schemas.
- Conflicts with J1 placements: 0. L098 read against ACT.4: business data changes stay out of the security event log (the business history is the database's, L049); security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events.
- Tensions recorded, not overridden: (a) EVOLUTION.3: several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need; L116's separate data schemas become domain schemas in the shared database (L513); L044 stays as J1 rejected it. (b) EVOLUTION.5: L068 (no teams by layer) against L515's database owner: each capability team owns its domain schema and its functions; a cross-schema business function belongs to the team that owns the workflow, reviewed by one named owner role (inferred). (c) OPERABILITY.2: L042's in-memory testing advantage is lost for the logic MD-03 puts in the database; those tests run on the real engine, rolled back by default, and behaviour that only shows at commit or between sessions is tested with committing sessions in a disposable database, never a shared one (L399, L400, L567).
- Gaps in the evidence: (1) PERFORMANCE owns one row and no row measures server or database time: whole-path measurement inferred (L095, L376, L382). (2) OPERABILITY.1: carrying the correlation id into the database transaction and audit rows inferred (L371, L566, L658). (3) OPERABILITY.2: no ledger row on concurrency testing; the concurrency tests themselves are required (inferred from GUARD.2), part of the default suite. (4) SECURITY: L303's tier map is inferred and assigns 7 of 10 categories; A06, A08 and A10 are assigned here, inferred, A06 and A08 corrected against the OWASP Top 10:2025 text; the ASVS chapter list (L304) is not read, its level definitions are. (5) The 3 roll-ups own no row.
- Review fixes: 9 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, m1, m4, m5, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.
