# Result: J1 ALLOCATION judged, both graphs (revision 3)

## L1 headline

All 47 ALLOCATION nodes are judged. The verdicts take in the maintainer's three decisions, two review rounds (F1 to F12, then R1-1 to R1-9) and, in revision 3, three hand-offs from the tier reviews. The database is shared by several backends and by BI, consoles and scripts (MD-03). Postgres is therefore the authority for everything that must hold whoever touches the data:
- each business operation is one function call in its own transaction, which may call other domains' published functions;
- each state column has one writer function;
- per-user write rules that can be decided from the row and the actor are enforced in the database;
- so are invariants and per-role privileges;
- audit records both the consumer's role and the actor it claims.

Each backend is the authority for its product policy not stored in the data, for its users' identity and for its workflows, which advance through state columns and the outbox. Foreign mutations run as atomic phases in a worker behind a 202 response. They run in the request only when the user must see the outcome within about 1 s, and even then the database function records the intent first. Browsers and agent clients decide nothing durable; no token travels in a URL except a short-lived signed file URL. Row-level security is not a default (MD-01). Every interface description consumers read stays in sync by process, with its origin chosen per project (MD-02). One verdict still goes partly against the doctrine: CHECK constraints are required, not optional. One clause is `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Its recorded default is a backend filter from one shared specification; read functions remain an acceptable fallback; and reporting and operator roles that may SELECT the base tables see every row, comments included, unless their own role is restricted.

Pinned:
- Nodes judged: 47 of 47 (web-app-philosophy 39, pig-web-defaults 8).
- Revision 3: ACT.2 against ACT.3 resolved (foreign mutations as atomic phases in a worker behind a 202 response; in the request only when the user must see the outcome within about 1 s, with the intent recorded by the database function first); read-visibility notation, default and fallback aligned with X1; cross-branch X2, X3, X6 and X7 applied where they touch J1 (the L517 departure is counted at PIG-WEB.DATA.INTERFACE.1, not here).
- Revision 2: re-review findings R1-1 to R1-9 applied as proposed (R1-2 by narrowing Q1); none of their evidence found wrong.
- Revision 1: default context restated per MD-03 and every placement re-judged under it; MD-01, MD-02, MD-03 applied; review findings F1-F12 resolved (F1 by MD-01; F2 and F9 by MD-02; F5 by MD-03; F3, F4, F6, F7, F8, F10, F11, F12 applied as proposed).
- Placements: 26; decided 25, undecided 1 (ALLOCATION.GUARD.3, one clause: read visibility of rows that carry per-user rules).
- Questions: 1, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (Q1, ALLOCATION.GUARD.3; a scope check on MD-01, whose "database privileges per role" and MD-03's "per-role privileges" leave per-user reads to each backend; row security stays excluded, functions are not). Recorded default: each backend filters from one shared specification with shared denial tests; fallback: database read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends, which MD-03 makes the default case. Per-user write rules are decided: the writer function (R1-1). The former question on row security is closed by MD-01.
- Verdicts against the maintainer doctrine: 1, partial. ALLOCATION.GUARD.2 goes against L471 on "triggers and CHECK constraints optional": only declarative constraints bind every writer, owner-run migrations included, and procedural checks need serializable isolation or a lock. The former verdict against L584 (ACT.1) is withdrawn: MD-03 makes multi-table operations database functions.
- Tensions between maintainer decisions and evidence, recorded, not overridden: (a) MD-01 against L619 and L688, which call for row security when several consumers share the database, the MD-03 default; (b) MD-03 against L044 (one application owns its database) and L215 with L042 (application-first logic, testable in memory); (c) MD-01 with MD-03: per-user read filters implemented in each backend become copies across backends, against RULES.4 (L633), hence Q1.
- Skeleton gaps: (1) FORCES.1 and .2 own no row: judged from the rows owned elsewhere that state their demand (L606, L608, L628; L019, L644, L650), state `known | gap: owns no row`, nothing invented. (2) DERIVE.2's backend-or-browser position is unargued: rejected as an authority; kept only as a browser copy over rows already loaded, re-sorted with the database's collation or not at all, condition marked inferred. (3) PRESENT.2 has one grounded position: decided on it, the placement marked `speculative`; collation is now owned by DERIVE.2 (the database, for any order it serves), its choice left open under DATA.

## L2 claims

### Revision 3

- **ACT.2 against ACT.3** (logic review M4): adopted the logic unit's realization.
  - Foreign mutations run as atomic phases with an idempotency key in a worker behind a 202 response.
  - They run in the request only when the user must see the outcome within about 1 s; the database function records the intent (outbox row) first, and the worker completes the call if the request dies.
  - Post-commit hooks are limited to losable work that touches no foreign system.
  - Applied in both records and the matrix.
- **Read-visibility clause** (X1): GUARD.3, the roll-ups, the matrix and `questions.md` now use the notation `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
  - The fallback is reworded: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Under MD-03 that condition always holds.
  - Comments are covered by the rule.
  - Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- **X2**: RECORD.2, DB_API, RECORD.3 and the matrix use X2's condition. "Deployed together" holds only when every consumer of the changed object ships in the same deployment; otherwise the change goes expand, migrate, contract. The departure from L517 is cited, not counted: it is counted at PIG-WEB.DATA.INTERFACE.1.
- **X3**: RULES.5, ACT.1 and the matrix allow a database function to call other domains' published functions in the same transaction. Direct access to another domain's tables stays forbidden.
- **X6**: GUARD.4 and the matrix forbid session tokens, bearer tokens and long-lived credentials in URLs. The one exception is a short-lived, single-purpose, scope-limited signed file URL, with its lifetime and scope stated.
- **X7**: RECORD.3 and the matrix extend MD-02's sync to every description consumers read: the HTTP description, the function API catalogue and the agent tool surface.
- **Unchanged counts**: placements 25 decided and 1 undecided; 1 question; 1 partial verdict against the doctrine.

### Revision 2

- **R1-1 (blocking)**: per-user write rules now have one authority.
  - A rule that can be decided from the stored row and the acting user ("only the assignee may close a task") is decided by the column's writer function. A backend's identical check is a generated or tested copy, kept for early feedback.
  - Backends are the authority for product policy not stored in the data (product roles, plan limits, feature flags, workflow steps) and for identity.
  - Applied in GUARD.3, ACT.1, RULES.4, the root roll-up, CONTEXT and the matrix.
- **R1-2**: Q1 is narrowed to read visibility and framed as a scope check on MD-01: row security stays excluded, functions do not.
  - B gives one implementation every consumer passes through, but still trusts the actor each consumer sets.
  - BI and operator roles keep full visibility unless they are restricted too.
  - Recommendation B; default if unanswered A; marked "awaiting maintainer".
- **R1-3**: the actor is the consumer's claim.
  - Audit and transition logs record both the session role and the claimed actor; writes without an actor are refused.
  - The default context states which roles may assert an end user (backends) and which may assert only themselves (operator, owner with ticket id); functions and triggers check that pairing.
  - Applied in the default context, GUARD.3, ACT.4 and the matrix.
- **R1-4**: one business operation is one function call in its own transaction, and backends never wrap several calls.
  - A step that must be atomic with another becomes a new function.
  - Workflows advance through state columns and the outbox, with idempotent steps.
  - Applied in RULES.5, ACT.1, DB_API, the access paths and the matrix.
- **R1-5**: RECORD.2's direct-write exception is aligned with DB_API's.
- **R1-6**: owner-run jobs change state columns only through the writer function or as a recorded exception under L545; the operator role's read grants are stated.
- **R1-7**: MD-02's drift gate now covers the function API: a CI catalogue diff fails on a removed function or an incompatible signature unless the change is marked coordinated (L517). Typed wrappers come from the same catalogue. Applied in RECORD.3, DB_API and the matrix.
- **R1-8**: CONTEXT's project-type row is reworded so that neither origin is the residual default. Agents as users point to description first, but the project records the choice.
- **R1-9**: the isolation hand-off to the DATA judge now asks for isolation per consumer role, writer functions that assert their isolation level, and replica reports that accept snapshot anomalies (L573).
- **Evidence**: I found none of the re-review's evidence wrong; I read L573 to confirm R1-9.

### Revision 1

- **MD-03, the shared database, is the default context.** It replaces "the backend is the only consumer". The access paths are now listed: one role per backend, a read-only BI role, an operator role for consoles and scripts, an owner role for migrations, and no database connection for browsers or agents. F5 is resolved.
  - Re-judged: RECORD.2 (the function API is the default contract); ACT.1 (multi-table operations and state transitions are database functions; the verdict against L584 is withdrawn); GUARD.3 (the work divided between backends and per-role grants); ACT.4 (audit set by MD-03); DB_API (writes through functions); GUARD.2 (several writers).
  - Adjusted: GUARD.1, GUARD.5, GUARD.6, ACT.2, ACT.3 and JOB_HOST (the database function now records parameters, versions, keys and staged intent); RULES.2 and RULES.4 (L607's exception, the two-level core); FORCES.1, .2, .5 and .6; CONTEXT; the root and family roll-ups.
  - Checked and unchanged: RECORD.1, GUARD.4 (one line added), DERIVE.1 to .3, PRESENT.1 to .3, POSTGRES_FIRST, JS_SERVER.
- **MD-01** decides ROW_SECURITY: no row-level security by default, acceptable only under its three conditions. The former Q1 is closed, and F1's recommendation is replaced.
- **MD-02** decides RECORD.3 and TYPE_CHAIN. The description is always in sync by process (one origin per fact, the other side generated or checked, review rules, a CI/CD gate on drift). The origin direction is recorded per project, with criteria for each direction. F2's design-first default and my former code-first default are both replaced.
- **F3**: one origin per fact. Stored facts come from the schema; persistence models are generated; validators that reject early must be generated or tested copies (RULES.1).
- **F4**: GUARD.2's multi-row rules run under Serializable with retry or behind a lock, with partial unique indexes and exclusion constraints first (L174, L175, L569, L577). The isolation default goes to the DATA judge. The ground against L471 is narrowed.
- **F6**: matrix certainty is relabelled. GUARD.1 and DERIVE.1 are now inferred; ACT.1 and ACT.4 are marked as set by MD-03, with the tension stated.
- **F7**: L534 covers derived-data caches only. Response caches sit in Postgres under POSTGRES_FIRST (inferred).
- **F8**: ACT.1's costs are weighed, and under MD-03 they now favour the database. Column privileges enforce the single writer.
- **F9**: TYPE_CHAIN starts at HTML form input and the agent surface; TypeScript applies to islands only.
- **F10**: FORCES orders the choosing forces by how hard their loss is to repair later.
- **F11**: DERIVE.2 owns collation, and the browser re-sort uses the same collation or none.
- **F12**: L684 has no source and is flagged to the ledger owner; ACT.4 rests on MD-03, L627 and L212.
- **Review evidence**: I found none of it wrong. Where a maintainer decision covers a finding, the decision replaces the review's fix.
- **New Q1**: MD-01 and MD-03 overlap on per-user rules that every backend must respect.

Pinned:
- Nodes judged: 47 of 47 (web-app-philosophy 39, pig-web-defaults 8).
- Revision 3: ACT.2 against ACT.3 resolved (foreign mutations as atomic phases in a worker behind a 202 response; in the request only when the user must see the outcome within about 1 s, with the intent recorded by the database function first); read-visibility notation, default and fallback aligned with X1; cross-branch X2, X3, X6 and X7 applied where they touch J1 (the L517 departure is counted at PIG-WEB.DATA.INTERFACE.1, not here).
- Revision 2: re-review findings R1-1 to R1-9 applied as proposed (R1-2 by narrowing Q1); none of their evidence found wrong.
- Revision 1: default context restated per MD-03 and every placement re-judged under it; MD-01, MD-02, MD-03 applied; review findings F1-F12 resolved (F1 by MD-01; F2 and F9 by MD-02; F5 by MD-03; F3, F4, F6, F7, F8, F10, F11, F12 applied as proposed).
- Placements: 26; decided 25, undecided 1 (ALLOCATION.GUARD.3, one clause: read visibility of rows that carry per-user rules).
- Questions: 1, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (Q1, ALLOCATION.GUARD.3; a scope check on MD-01, whose "database privileges per role" and MD-03's "per-role privileges" leave per-user reads to each backend; row security stays excluded, functions are not). Recorded default: each backend filters from one shared specification with shared denial tests; fallback: database read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends, which MD-03 makes the default case. Per-user write rules are decided: the writer function (R1-1). The former question on row security is closed by MD-01.
- Verdicts against the maintainer doctrine: 1, partial. ALLOCATION.GUARD.2 goes against L471 on "triggers and CHECK constraints optional": only declarative constraints bind every writer, owner-run migrations included, and procedural checks need serializable isolation or a lock. The former verdict against L584 (ACT.1) is withdrawn: MD-03 makes multi-table operations database functions.
- Tensions between maintainer decisions and evidence, recorded, not overridden: (a) MD-01 against L619 and L688, which call for row security when several consumers share the database, the MD-03 default; (b) MD-03 against L044 (one application owns its database) and L215 with L042 (application-first logic, testable in memory); (c) MD-01 with MD-03: per-user read filters implemented in each backend become copies across backends, against RULES.4 (L633), hence Q1.
- Skeleton gaps: (1) FORCES.1 and .2 own no row: judged from the rows owned elsewhere that state their demand (L606, L608, L628; L019, L644, L650), state `known | gap: owns no row`, nothing invented. (2) DERIVE.2's backend-or-browser position is unargued: rejected as an authority; kept only as a browser copy over rows already loaded, re-sorted with the database's collation or not at all, condition marked inferred. (3) PRESENT.2 has one grounded position: decided on it, the placement marked `speculative`; collation is now owned by DERIVE.2 (the database, for any order it serves), its choice left open under DATA.

Claims:
1. **Coverage is complete.** *Grounded: a script re-parsed the written files.*
   - 47 judge records, one per J1 node, and 26 matrix lines.
   - Every cited ledger id exists. Beyond J1's 174-row list, I read and cite six rows the reviews raised: L174, L175, L569, L573, L577, L635.
2. **Postgres is the authority for stored-data truth and for everything that must hold whoever touches it.** *MD-03; grounded on L045, L040, L473, L584, L596, L628, L627.*
   - It owns the system of record, invariants, business operations and state transitions (one function call per operation, one writer function per state column), per-user write rules decidable from the row and the actor, concurrency detection, derived data and audit.
   - The function API is every consumer's contract: one role per consumer, writes through functions with one stated exception, simple reads direct (L515, L516, L517).
3. **Each backend is the authority for its product policy, its users' identity and its workflow.** *Grounded; the split by "where the rule's facts live" is inferred (R1-1).*
   - Product policy not stored in the data: roles, plan limits, flags, workflow steps (MD-01).
   - Sessions, server-side and revocable (L313, L315, L316).
   - Workflows advance through state columns and the outbox, never as a transaction around several calls (R1-4, L624). Foreign mutations run in a worker behind 202, or in the request only for an outcome needed within about 1 s, with the intent recorded first (revision 3).
   - HTML rendering by default (L629, L281). This part is *inferred*: a judgment.
4. **Authorization divides by where the rule's facts live.** *MD-01, MD-03; division inferred.*
   - Writer functions decide per-user write rules; backends decide product policy; Postgres bounds each consumer by role (L468, L596).
   - The actor is a claim: both role and actor are recorded, writes without an actor are refused, and the role-to-actor pairing is checked (R1-3).
   - No row-level security unless MD-01's three conditions hold.
5. **Interface documentation is always in sync, and its origin is per project.** *MD-02; per-fact rule inferred (L486).*
   - Stored facts originate in the schema. The function API's signatures are guarded by a catalogue diff in CI (L517).
   - The interface description is guarded by a drift gate; description first or code first is recorded per project with criteria.
6. **One partial verdict goes against the doctrine.** *Grounded.* GUARD.2 against L471's optional CHECK constraints: only declarative constraints bind every writer, and procedural checks need Serializable or a lock (L473, L577, L569). Isolation is set per consumer role (L573).
7. **Three tensions between maintainer decisions and the evidence are recorded, not overridden.** *Grounded on the rows.*
   - MD-01 against L619 and L688.
   - MD-03 against L044, L622, L215 and L066.
   - MD-01 with MD-03: per-user read filters copied per backend (L633).
8. **One question, Q1: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.** *Open.*
   - Who filters reads of rows that carry per-user rules, comments included: each backend (A, MD-01 as written) or read functions in the API (B)? It is a scope check on MD-01.
   - My recommendation: B. It gives one implementation, but it still trusts the actor each consumer sets.
   - Recorded default: A, with a shared specification and shared denial tests. Kept fallback: read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends, which is always the case under MD-03.
   - Under either answer, roles that may SELECT the base tables see every row, comments included, unless their own role is restricted.
9. **Open: evidence the verdicts lean on but do not hold.**
   - Scalability premise (L615): FORCES.5 stays `speculative`.
   - Unmeasured thresholds: queue contention (L126), NOTIFY (L127), the 1 s deferral threshold (my choice).
   - Generators for persistence models, interface fields and function wrappers: none read.
   - Collation choice: open under DATA.
   - Operating cost of a JavaScript server (L288).
   - L684 has no source (flagged).
   - The isolation default is handed to the DATA judge with per-role conditions (L568, L569, L573).
   - The role-to-actor pairing check is inferred; no source describes it.
10. **Open: process.** Revision 2 had no independent review of its own. Its changes are the re-review's proposed fixes, applied as written.

## L3 full

### Revision 3

Inputs added: the coordinator's three hand-offs; `../cross_branch_fixes.md` (X1 to X7; X4 and X5 do not touch J1). Changes:

| cause | nodes | change |
|---|---|---|
| logic review M4 | ACT.2, ACT.3, matrix | foreign mutations as atomic phases in a worker behind 202; in-request only for an outcome needed within about 1 s, intent recorded by the database function first, worker completer as backstop; post-commit hooks only for losable work touching no foreign system |
| X1 | GUARD.3, ALLOCATION.GUARD and PIG-WEB.ALLOCATION roll-ups, matrix, questions.md, pins | notation `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`; recorded default (shared specification, shared denial tests); fallback reworded (read functions with the verified actor, acceptable for a rule that must hold for two or more backends, always the case under MD-03); comments covered; SELECT-capable roles see every row unless restricted |
| X2 | RECORD.2, DB_API, RECORD.3, matrix | "deployed together" only when every consumer of the changed object ships in the same deployment, otherwise expand, migrate, contract; L517 departure cited, counted at PIG-WEB.DATA.INTERFACE.1 |
| X3 | RULES.5, ACT.1, matrix | database functions may call other domains' published functions in the same transaction; direct access to another domain's tables forbidden |
| X6 | GUARD.4, matrix | no session token, bearer token or long-lived credential in a URL; short-lived signed file URLs the one exception |
| X7 | RECORD.3, matrix | MD-02 sync covers the HTTP description, the function API catalogue and the agent tool surface |

### Revision 2

Inputs added: `../J1_review/review_r1.md` (R1-1 to R1-9). Ledger row read for the revision: L573. Changes, by finding:

| finding | nodes | change |
|---|---|---|
| R1-1 | GUARD.3, ACT.1, RULES.4, ALLOCATION roll-up, CONTEXT, matrix | per-user write rules decidable from the row and the actor are decided by the writer function; a backend's identical check is a generated or tested copy; backends own product policy not stored in the data and identity |
| R1-2 | questions.md, GUARD.3, CONTEXT, roll-ups | Q1 narrowed to read visibility; framed as a scope check on MD-01 (MD-01's "database privileges per role", MD-03's "per-role privileges"; row security excluded, functions not); B's gain restated as one implementation that still trusts the consumer-set actor; BI and operator visibility stated for both positions; marked awaiting maintainer |
| R1-3 | default context (actor column, actor-trust paragraph), GUARD.3, ACT.4, ACT.1, matrix | the actor is the consumer's claim; history records session role and claimed actor; writes without an actor refused; role-to-actor pairing checked |
| R1-4 | RULES.5, ACT.1, DB_API, access paths, matrix | one business operation, one function call, one transaction; no backend transaction around several calls; atomic steps become new functions; workflows through state columns and the outbox, idempotent steps |
| R1-5 | RECORD.2, matrix | direct single-table write exception aligned with DB_API |
| R1-6 | ACT.1, default context, matrix | owner-run jobs use the writer function or a recorded L545 exception, with the actor set; operator role's reads stated |
| R1-7 | RECORD.3, DB_API, matrix | catalogue diff in CI fails on a removed function or incompatible signature unless marked coordinated (L517); wrappers from the same catalogue |
| R1-8 | CONTEXT | project-type row: origin per project by RECORD.3's criteria, neither residual; default context leans description first, project records it |
| R1-9 | GUARD.2, matrix | DATA hand-off: isolation per consumer role, writer functions assert isolation, replica reports accept snapshot anomalies (L573) |

Review evidence I disagreed with: none.

### Revision 1

Inputs added: `../../maintainer_decisions.md` (MD-01 to MD-03) and `../J1_review/review.md` (F1 to F12). Ledger rows read for the revision: L174, L175, L568, L569, L577, L635. Changes, by cause:

| cause | nodes | change |
|---|---|---|
| MD-03 | default context (records, matrix) | "the backend is the only consumer" replaced by a shared database (backends, BI, consoles, scripts); access-path table added (resolves F5) |
| MD-03 | RECORD.2, DB_API | function API is the default contract; one role per consumer; writes through functions; simple reads direct (L516); BI through a read-only role, on a replica or copy when load matters; tension with L044 and L622 recorded |
| MD-03 | ACT.1 | multi-table operations and state transitions are database functions (L584 stands, L596 writer function); backend keeps workflow, product policy and external calls; the former verdict against L584 is withdrawn; tension with L215 and L066 recorded |
| MD-03 | GUARD.3 | division of work with several consumers: backend per user and action, database per consumer role and function grants, functions get the verified actor |
| MD-03 | ACT.4 | audit in the database set by MD-03 |
| MD-03 | GUARD.1, GUARD.5, GUARD.6, ACT.2, ACT.3, JOB_HOST | the database function receives typed parameters, the expected version and the idempotency key, and writes the staged intent and job rows |
| MD-03 | RULES.2, RULES.4, FORCES.1, .2, .5, .6, CONTEXT, roll-ups | L607's "every consumer needs the same rule" is now the default; two-level core; database functions weighed against L615; costs of database logic accepted with tooling |
| MD-01 | ROW_SECURITY, GUARD.3 | no row-level security by default, acceptable only under its three conditions; former Q1 closed (F1); tension with L619 and L688 recorded |
| MD-02 | RECORD.3, TYPE_CHAIN | interface description always in sync by process; origin direction per project with criteria for each direction (F2) |
| F3 | RECORD.3, TYPE_CHAIN, GUARD.2, RULES.1 | one origin per fact; persistence models generated from the live schema; rejecting copies only when generated or tested |
| F4 | GUARD.2, GUARD.5 | cross-row rules by partial unique index or exclusion constraint first (L174, L175); other multi-row rules under Serializable with retry or a lock, with the trigger asserting the isolation level (L569, L577); default isolation handed to the DATA judge (L568) |
| F6 | matrix | GUARD.1 and DERIVE.1 inferred; ACT.1 and ACT.4 marked as set by MD-03 with their tension |
| F7 | CACHE_STORE, DERIVE.3, matrix doctrine section | L534 limited to derived-data caches; response caches in Postgres under POSTGRES_FIRST (inferred); "L534 over L417" removed |
| F8 | ACT.1 | round trips and lock time weighed (L614); testability argument qualified; column privileges enforce the single writer |
| F9 | TYPE_CHAIN | default chain starts at HTML form input and the agent surface; TypeScript only for islands |
| F10 | FORCES | among admissible tiers, the force whose loss is hardest to repair later wins |
| F11 | DERIVE.2, PRESENT.2 | the database owns collation for every order it serves; browser re-sort uses the same collation or none; the choice of collation stays open under DATA |
| F12 | ACT.4 | L684 cites no source, flagged to the ledger owner; ACT.4 rests on MD-03, L627 and L212 |
| MD-01 with MD-03 | GUARD.3, questions.md | new Q1 on per-user rules across backends |

Review evidence I disagreed with: none. Where a maintainer decision covers a finding (F1, F2, F5, F9 in part), the decision replaces the review's fix, as the decisions say.

Pinned:
- Nodes judged: 47 of 47 (web-app-philosophy 39, pig-web-defaults 8).
- Revision 3: ACT.2 against ACT.3 resolved (foreign mutations as atomic phases in a worker behind a 202 response; in the request only when the user must see the outcome within about 1 s, with the intent recorded by the database function first); read-visibility notation, default and fallback aligned with X1; cross-branch X2, X3, X6 and X7 applied where they touch J1 (the L517 departure is counted at PIG-WEB.DATA.INTERFACE.1, not here).
- Revision 2: re-review findings R1-1 to R1-9 applied as proposed (R1-2 by narrowing Q1); none of their evidence found wrong.
- Revision 1: default context restated per MD-03 and every placement re-judged under it; MD-01, MD-02, MD-03 applied; review findings F1-F12 resolved (F1 by MD-01; F2 and F9 by MD-02; F5 by MD-03; F3, F4, F6, F7, F8, F10, F11, F12 applied as proposed).
- Placements: 26; decided 25, undecided 1 (ALLOCATION.GUARD.3, one clause: read visibility of rows that carry per-user rules).
- Questions: 1, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (Q1, ALLOCATION.GUARD.3; a scope check on MD-01, whose "database privileges per role" and MD-03's "per-role privileges" leave per-user reads to each backend; row security stays excluded, functions are not). Recorded default: each backend filters from one shared specification with shared denial tests; fallback: database read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends, which MD-03 makes the default case. Per-user write rules are decided: the writer function (R1-1). The former question on row security is closed by MD-01.
- Verdicts against the maintainer doctrine: 1, partial. ALLOCATION.GUARD.2 goes against L471 on "triggers and CHECK constraints optional": only declarative constraints bind every writer, owner-run migrations included, and procedural checks need serializable isolation or a lock. The former verdict against L584 (ACT.1) is withdrawn: MD-03 makes multi-table operations database functions.
- Tensions between maintainer decisions and evidence, recorded, not overridden: (a) MD-01 against L619 and L688, which call for row security when several consumers share the database, the MD-03 default; (b) MD-03 against L044 (one application owns its database) and L215 with L042 (application-first logic, testable in memory); (c) MD-01 with MD-03: per-user read filters implemented in each backend become copies across backends, against RULES.4 (L633), hence Q1.
- Skeleton gaps: (1) FORCES.1 and .2 own no row: judged from the rows owned elsewhere that state their demand (L606, L608, L628; L019, L644, L650), state `known | gap: owns no row`, nothing invented. (2) DERIVE.2's backend-or-browser position is unargued: rejected as an authority; kept only as a browser copy over rows already loaded, re-sorted with the database's collation or not at all, condition marked inferred. (3) PRESENT.2 has one grounded position: decided on it, the placement marked `speculative`; collation is now owned by DERIVE.2 (the database, for any order it serves), its choice left open under DATA.

### Files

- `records.md`: 47 judge records. Each has positions with ledger ids, forces, decision with grounds, rejected positions with reason and winning condition, and a proposed `epistemic_state`. Placement records also give authority, permitted copies, forbidden tiers and moving context. Each record notes what revision 1 changed in it.
- `allocation_matrix.md`: one line per placement (26), standalone, with the MD-03 context and access paths up front, and a closing section on maintainer decisions, tensions and doctrine.
- `questions.md`: Q1 (`undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`), with positions, recommendation and what the graph records if unanswered; the former row-security question and per-user write rules are marked closed (MD-01, R1-1).

### Method

- Inputs, round 0: the target hierarchy; J1 in the judge plan; the ALLOCATION parts of the skeleton; the 174 ledger rows J1 lists, read in full; source tiers; the allocation research slot's context table and gaps.
- Inputs, revision 1: MD-01 to MD-03 and F1 to F12, plus L174, L175, L568, L569, L577, L635.
- Inputs, revision 2: R1-1 to R1-9, plus L573.
- Selection: per node, the most demanding practice that best serves its stated force. Weaker positions are kept as "rejected, wins when <condition>". `undecided` is used only where the node serves both forces of a trade-off that neither the evidence nor a maintainer decision settles: one clause of one node.
- Maintainer decisions override the judge and the review on their points. Where a decision runs against read evidence in a way that matters, the record states the tension and does not override the decision: three tensions.
- MAINT rows weigh as a strong position. Each record says where the doctrine is the max choice and where a verdict goes against it.
- `epistemic_state` follows the IntentGraph convention: a base state, then `| gap:`, `| conflict:` or `| unvalidated:` annotations; `known: MD-0n` marks a node a maintainer decision sets.

### Verdicts by family

- **FORCES**:
  - Correctness and security are vetoes. Among the admissible tiers, the force whose loss is hardest to repair later wins: changeability of the rule's location, then performance, then scalability. Latency and performance justify copies.
  - Performance: data reduction goes with the data by design (L613); anything else waits for a measurement (L097).
  - Latency: designed in from the start (L012, L013).
  - Scalability: a tie-breaker until a measured limit (L615, `speculative`).
  - Changeability: the costs of database logic are explicit inputs, accepted under MD-03 and paid for with tooling (L472, L042).
- **CONTEXT**: 20 variables with directions. MD-03 fixes the number of consumers at several, which settles L621's contested answer. Access paths, per-user rules (writes settled, reads Q1), actor pairing and project type (origin per project, neither residual) are added.
- **RULES**: applied in order: trust boundary, end-to-end, authority and copies, one core, atomicity ends at the transaction.
  - Rejecting copies must be generated or tested (F3).
  - L607's exception is now the default (MD-03).
  - The core has two levels: the function API for everything that must hold for every consumer; each backend's use cases for its own workflow.
- **RECORD**:
  - Postgres is the system of record (L045).
  - The function API is every consumer's contract; BI reads through a read-only role (MD-03, L515-L517).
  - One origin per fact, with the stored facts in the schema (L474, L486). The interface description is always in sync, and its origin is chosen per project (MD-02).
- **GUARD**:
  - Validation: parse at every entry, function parameters included (L484, L612).
  - Invariants: declarative constraints required; procedural multi-row rules under Serializable or a lock (L473, L174, L175, L569, L577). Against L471 in part.
  - Authorization: writer functions decide per-user write rules decidable from the row and the actor; backends decide product policy and identity; the database bounds each consumer by role; the actor is a checked claim; no row-level security by default. Per-user read visibility is Q1, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (MD-01, L468; R1-1, R1-3).
  - Sessions: server-side and revocable; end users are never database roles; no token in a URL except short-lived signed file URLs (L313, L315, L316; X6).
  - Concurrency: the database detects inside the writer function, and the policy follows the data shape (L628, L678, L260).
  - Duplicates: the key and the effect are recorded in the function's transaction, with a unique constraint as the backstop (L478, L270, L582).
- **ACT**:
  - Business operations: each is one function call in its own transaction, never wrapped by a backend; state transitions through one writer function per state column, enforced by column privileges; per-user write rules in that function; owner-run jobs through it or a recorded exception (MD-03, L584, L596; R1-1, R1-4, R1-6). Workflow, product policy and external calls stay in the backend, workflows advancing through state columns and the outbox (L528).
  - Side effects: the function writes the outbox row and a backend worker delivers it (L624); foreign mutations run as atomic phases in a worker behind 202, or in the request only for an outcome needed within about 1 s, after the intent is recorded (L589; revision 3).
  - Deferred work: core writes are never asynchronous; the rest goes to staged workers or Postgres schedules (L601, L482, L604).
  - Audit: trigger history in the same transaction recording the session role and the claimed actor, writes without an actor refused (R1-3), agent delegation recorded, a separate security log (MD-03, L627, L658, L049).
- **DERIVE**:
  - Derived data: computed on read, else maintained in the database according to its freshness need (L625, L532).
  - Reduction: in the database, with keyset paging. The database owns collation (L613, L266; F11).
  - Caching: every cache is a copy with a staleness bound. Derived-data caches live in Postgres tables (L534); response caches go in Postgres under POSTGRES_FIRST (F7).
- **PRESENT**: server-rendered HTML with islands (L629, L281). Formatting happens in the rendering tier (L632, `speculative`). UI state is placed by lifetime and sharing, and presence is never written to tables (L631, L681).
- **PIG-WEB.ALLOCATION**:
  - Postgres hosts the backing roles until a measured limit (L125).
  - The function API in a dedicated schema is the default (MD-03); no views in the contract (L516).
  - Type chain: stored facts are generated from the catalogue; the interface origin is chosen per project (MD-02).
  - No row-level security by default (MD-01).
  - The queue table is written by the functions and claimed with SKIP LOCKED; data schedules run in Postgres (L126, L604).
  - Postgres hosts the caches (F7).
  - No JavaScript server (L288).

### The three skeleton gaps

1. **FORCES.1 and .2 own no row.** Judged from the rows owned elsewhere that state their demand: correctness from L606, L608, L628, L473, L623; security from L019, L644, L650, L622, L468. State: `known: demand stated by ... | gap: owns no row`. Nothing invented and no research launched. If these nodes should own evidence, the fix belongs in the skeleton.
2. **DERIVE.2 position 3 is unargued.** Rejected as an authority on L613, L614 and L615. Kept only as a browser copy over rows already loaded, using the database's collation or no re-sort at all (F11). That condition is inferred.
3. **PRESENT.2 has one grounded position.** Decided on it: canonical storage, formatting in the rendering tier. The node is `speculative` because L632 rests on a capability page. Collation now belongs to DERIVE.2 (F11), and the choice of collation stays open under DATA.

### Checks run

- A script parsed `judge_plan.md` and the written files and found:
  - 47 plan nodes against 47 record headings, none missing or extra;
  - 26 matrix lines;
  - one `undecided` state;
  - every cited `Lnnn` present in the ledger; the ids outside J1's list are exactly L174, L175, L569, L573, L577 and L635, read for the revisions;
  - the pinned block identical in records, matrix and every result level;
  - no absolute path or private name in the outputs.
- Not checked: revision 1 was reviewed (R1-1 to R1-9, all applied); revision 2 has had no review of its own.

### Open items for the next steps

- Q1 awaits the maintainer.
  - J3 and J7 (LOGIC: secure and enforce) depend on it for per-user read filters; per-user write rules are settled (writer functions).
  - J6 (PIG-WEB.DATA) depends on it for read functions on tables with per-user rules; it also receives the actor-pairing check (R1-3) and the per-role isolation conditions (R1-9).
  - J2, J4, J5, J8 and J9 can proceed.
- J6 receives the default isolation decision (PIG-WEB.DATA.CONCURRENCY.1). The constraint from GUARD.2 applies, and the review and I both recommend Serializable with retry (L568 (a), L569).
- Flag to the ledger owner: L684 is marked grounded but cites no source.
- Evidence gaps: a primary source for L615; measured thresholds for queue contention, NOTIFY and Postgres cache latency; generators for persistence models and interface fields.
- Optional: a short check of revision 2's new rules (R1-3 actor pairing, R1-4 no wrapping), which are inferred, before J3, J6 and J7 build on them.
