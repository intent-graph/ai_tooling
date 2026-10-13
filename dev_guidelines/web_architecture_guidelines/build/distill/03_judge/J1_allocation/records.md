# J1 ALLOCATION: judge records, both graphs (revision 3)

One judge record per ALLOCATION node of `web-app-philosophy` (39 nodes) and `pig-web-defaults` (8 nodes), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves its purpose; weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. MAINT rows (source MAINT-S01) weigh as a strong position. The maintainer's decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override the judge and the review on their points and are cited by id. Revision 1 applies them and the findings F1 to F12 of `../J1_review/review.md`; revision 2 applies the re-review's findings R1-1 to R1-9 (`../J1_review/review_r1.md`); revision 3 applies three hand-offs from the tier reviews (ACT.2 against ACT.3, the read-visibility notation, and the cross-branch resolutions X1 to X3, X6 and X7 of `../cross_branch_fixes.md`); the change lists are in `result.md`, and each record ends with what each revision changed in it. The one-page review is `allocation_matrix.md`; the open trade-off is in `questions.md`.

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

## Default context (MD-03)

Stated by the maintainer: a classic website (documents, forms, CRUD), one team, JavaScript + Python + Postgres, single tenant, humans and agents as users; **the database may be shared by several backends and by other consumers: BI and reporting, admin consoles, scripts** (MD-03).

Access paths to the database (F5; my realisation of MD-03, role names illustrative, inferred):

| path | role | may | may not | actor it may assert (R1-3) |
|---|---|---|---|---|
| each backend | its own request role, neither owner nor superuser | EXECUTE the API functions it uses; SELECT for simple reads where granted (L516); a direct single-table write only under DB_API's exception | write tables directly where a state column or a multi-table effect is involved; UPDATE state columns; open a transaction around several API calls (R1-4) | an end user or agent it has authenticated |
| BI and reporting | read-only reporting role | SELECT on the tables and columns it needs, on a replica or reporting copy when its load matters | any write; columns it does not need (personal data by default) | none (reads only) |
| admin consoles, scripts | operator role | EXECUTE the API functions, like a backend; SELECT on the tables and columns its tasks need, with the reporting role's column restrictions (R1-6) | direct DML | only itself: the named operator, never an end user |
| migrations, human-run data jobs | owner role | change schema; run reviewed data jobs under the checklist of L545; state columns only through their writer function, or as a recorded exception under L545 (R1-6) | serve requests | only itself: the operator and the ticket id (L545) |
| browsers, agents | none | reach data through a backend (agents through an adapter, RULES.4) | connect to the database | n/a |

**Actor trust (R1-3)**: the database verifies only the consumer (the session's role); the acting user in the transaction-local setting is a claim made by that consumer (inferred: any session can set such a setting; L311's "derive it from the verified identity" binds the backend, not the database). Therefore: audit and transition logs record both the session role and the claimed actor; writer functions and audit triggers refuse a write when no actor is set; and they check the pairing in the last column (a backend role may assert an end user, an operator or owner role only itself).

Assumed where MD-03 is silent: online use; Postgres is a long-term commitment (portability sunk, L042); write load fits one primary; the team can write and test database functions, which MD-03 presupposes (without that skill L041 applies).

## How to read

- **Positions**: P1.. as numbered in the skeleton's placement records, with ledger ids.
- **Forces**: what each position serves and what it costs.
- **Decision**: the max choice and its grounds; a maintainer decision is cited by id.
- **Rejected**: each other position, why, and the condition under which it wins.
- **Placement** (placement nodes only): authority tier; permitted copies and their purpose; forbidden tiers; the context that would move it.
- **State**: proposed `epistemic_state`. `known` = grounded verdict or maintainer decision; `known | unvalidated: X` = with an inferred part X; `speculative` = thin evidence; `undecided` = question to the maintainer; `| conflict:` names a disagreement with a MAINT row, a research row or a maintainer decision; `| gap:` names missing evidence.
- **Changed (R1)**, **(R2)**, **(R3)**: what each revision changed in the record, and why.
- Roll-up nodes own no row; their decision is the roll-up of their children.

## ALLOCATION Allocation of Responsibilities

- **Positions**: one. L610: each placement records its authority, permitted copies and forbidden tiers, because a rule can legitimately exist in three tiers (feedback, decision, last guard) and only one decides.
- **Forces**: correctness (one decider), changeability (the record makes the decision reviewable).
- **Decision**: every responsibility gets one placement record (authority, permitted copies with their purpose, forbidden tiers, moving context), decided before any tier is designed. Roll-up of the 26 placements for the default context:
  - **Postgres is the authority for the truth of stored data and for everything that must hold whoever touches it**: system of record, invariants, multi-table operations and state transitions behind the function API (one call, one transaction), per-user write rules decidable from the row and the actor, per-role privileges, concurrency detection, derived data, audit with role and claimed actor (MD-03; R1-1, R1-3, R1-4).
  - **Each backend is the authority for decisions about its users and its workflow**: validation at entry, authorization for product policy not stored in the data and for identity (MD-01; per-user write rules decidable from the row belong to the writer functions, R1-1), sessions, orchestration across operations, side-effect delivery, deferred work, HTML rendering.
  - **Browsers and agent clients are the authority for nothing durable**: they hold the view, ephemeral state and copies for feedback and latency.
- **Rejected**: none (no competing position).
- **State**: `known | unvalidated: the record format is a synthesis (L610 inferred)`.
- **Changed (R1)**: the database half widened to operations, privileges and audit (MD-03).
- **Changed (R2)**: per-user write rules moved to the database half (R1-1).

## ALLOCATION.FORCES Allocation Forces

- **Positions**: no row; roll-up of the six forces.
- **Decision**: the forces act in order, not on one scale.
  1. Correctness and security decide which tiers may be the authority; a tier that cannot see every writer, or that the requester controls, is vetoed (L606, L608, L019).
  2. Among admissible tiers, the force whose loss is hardest to repair later wins (F10). In the default context that orders them: changeability of the contract and of the rule's location (a rule placed in the wrong tier, or copied across consumers, needs every consumer changed to repair) before performance (repairable later by a measured move, L097, L215) before scalability (repairable at a measured limit, L125).
  3. Latency and performance justify copies in other tiers, never a move of authority (L607, L609, L012).
  Each placement settled at step 2 names the force it preferred.
- **Rejected**: a weighted sum of forces per placement: it is the average the maintainer rejected; it wins never as a rule.
- **State**: `known | unvalidated: the order and the repairability criterion are my synthesis of L606-L609, L019, L097, L125`.
- **Changed (R1)**: criterion among the choosing forces added (F10).

## ALLOCATION.FORCES.1 Correctness

- **Positions**: no row of its own (skeleton gap 1). The demand is stated by rows owned elsewhere: L606 (the tier with knowledge and finality), L608 (the data store is an end for rules about stored data), L628 (the tier that sees every writer), L473 (check-then-write fails below serializable isolation), L623 (atomicity only inside one transaction).
- **Decision**: correctness demands that the deciding tier sees every writer and every fact the decision needs, and completes the decision atomically with the data it guards. In the default context several consumers write, so rules about stored data and operations that span tables go to the database (MD-03); rules that need the end user's identity or the request go to the backend. Veto force (FORCES).
- **Gap handling**: judged as the roll-up of the rule rows that state it; no row invented, no research launched.
- **State**: `known: demand stated by L606, L608, L628 | gap: owns no row`.
- **Changed (R1)**: default context per MD-03.

## ALLOCATION.FORCES.2 Security

- **Positions**: no row of its own (skeleton gap 1). Demand stated by L019 (a check that grants access or protects integrity runs in a tier the requester cannot modify), L644 (model output is never an authorization decision), L650 (client hints never enforce), L622 (no schema across a trust boundary), L468 (database permissions cannot be bypassed by ad-hoc SQL).
- **Decision**: a decision that grants access or protects integrity runs in a tier the requester cannot modify (backend or database), on every access path; model output and client hints are input, never a decision. With several consumers, every consumer is bounded by its own database role (MD-01, MD-03). Veto force.
- **State**: `known: demand stated by L019, L644, L650 | gap: owns no row`.
- **Changed (R1)**: per-consumer roles added (MD-01, MD-03).

## ALLOCATION.FORCES.3 Performance

- **Positions**: P1 measure before optimising (L097); P2 place set work with its data by design (L613, L614).
- **Decision**: both, by kind. Data reduction (filter, aggregate, sort, page) is placed with the data by design, because that is a placement, not an optimisation (L613). Every other performance-driven move or copy waits for a measurement that identifies the path (L097, L607).
- **Rejected**: optimising up front; wins never (L097).
- **State**: `known`.

## ALLOCATION.FORCES.4 Latency

- **Positions**: one (L012, L013).
- **Decision**: latency is a design criterion from the start (L012). Count round trips per interaction, browser to server and backend to database (L614), and budget them against 0.1 s, 1 s and 10 s and the Web Vitals targets (L013). Latency justifies copies near the user under RULES.1, never authority. The round-trip structure is designed in; micro-optimisation waits for measurement.
- **State**: `known`.

## ALLOCATION.FORCES.5 Scalability

- **Positions**: P1 keep per-request computation off the database, because writes scale only through one primary (L615, inferred, no primary source); P2 one Postgres until a measured limit (L125).
- **Decision**: weigh each placement against the single write primary. Set-based reductions that return small results are exempt (L615's own exception), and so are the database functions MD-03 places there: they replace several round trips by one and do not add work the backend would not send anyway (inferred). Scalability moves a placement only when a measured write or connection load approaches the primary's limit (L125, L097).
- **Rejected**: placing logic off the database pre-emptively; wins when measured write load is the limit (L615).
- **State**: `speculative: the premise lacks a read primary source (L615) | gap: no measured comparison of placements in any source`.
- **Changed (R1)**: database functions under MD-03 weighed against L615.

## ALLOCATION.FORCES.6 Changeability

- **Positions**: one, research and doctrine agreeing (L042, L472 MAINT, L041).
- **Decision**: the costs of database logic are explicit inputs to every placement: testing needs a live database, tooling and debugging are poor, the onboarding floor is higher, expressiveness is limited (L472, L042). Portability is sunk when the DBMS is a long-term commitment (L042). Under MD-03 these costs are accepted for what must hold for every consumer, and must be paid for with tooling: functions in versioned migrations, tested against a live database in CI. L472 (MAINT) is the max choice.
- **State**: `known`.
- **Changed (R1)**: costs accepted under MD-03, with their tooling.

## ALLOCATION.CONTEXT Allocation Context

- **Positions**: L621 (the number of consumers moves allocation; agreed as a variable, contested on the answer); L041 (team skill is a legitimate input).
- **Decision**: the variables below move placements in the stated direction; the default context (above, MD-03) fixes their values. MD-03 settles L621's contested answer for this guideline: with several consumers, rules that must hold for all of them belong in the database, behind the function API.

  | variable | moves toward | placements |
  |---|---|---|
  | database consumers: several (default, MD-03) / one only | database function API / rules may live in that one backend | RECORD.2, ACT.1, DB_API |
  | access paths and their roles (backends, BI, consoles, scripts, owner) | per-role privileges and function grants | GUARD.3, RECORD.2 |
  | per-user rules every consumer must respect | writes: the writer function (R1-1); read visibility: Q1 | GUARD.3, ACT.1 |
  | which consumer may assert which actor | trusted-actor pairing checked by functions and audit triggers | GUARD.3, ACT.4 (R1-3) |
  | client kind: same-site browser / mobile, third-party, agent | server session / bearer tokens with server-held revocation | GUARD.4 |
  | automated callers (agents) | required idempotency keys, audit with delegation | GUARD.6, ACT.4 |
  | offline need, user-owned data | client replica (local-first) | RECORD.1, PRESENT.3, GUARD.5 |
  | latency budget | copies near the user | RULES.1, DERIVE.3 |
  | data volume against result size | the database | DERIVE.2 |
  | write load near the primary's limit | computation and backing roles off the database | FORCES.5, POSTGRES_FIRST |
  | team SQL skill: low | application (L041); conflicts with MD-03, which presupposes the skill | ACT.1 |
  | policy change cadence: fast | backend, for product policy not stored in the data | GUARD.3 |
  | domain complexity | domain model and use cases in the backend for workflow | ACT.1 (L226) |
  | DBMS commitment | portability cost sunk | ACT.1, DB_API (L042) |
  | conflict rate, data shape, edit length | concurrency policy | GUARD.5 |
  | effect losable; crosses a service with its own database | post-commit hook; saga | ACT.2 |
  | staleness tolerance | cache tier and lifetime | DERIVE.1, DERIVE.3 |
  | UI interdependence, update frequency, crawlability | client rendering, JavaScript server | PRESENT.1, JS_SERVER |
  | consumer outside the owning team | function API published as a contract, or that team's service | RECORD.2 (L622) |
  | project type | description or code as the interface origin, recorded per project by RECORD.3's criteria; in the default context agents read the description and are often hosts the team does not control, which points to description first, but the project records the choice | RECORD.3, TYPE_CHAIN (MD-02) |

- **State**: `known | unvalidated: the directions for write load and DBMS commitment are inferred (L615, L042)`.
- **Changed (R1)**: default per MD-03; access paths, per-user rules and project type added (F5, MD-02).
- **Changed (R2)**: per-user rules split into writes (writer function) and reads (Q1) (R1-1, R1-2); actor pairing added (R1-3); project-type row reworded so neither origin is the residual default (R1-8).

## ALLOCATION.RULES Allocation Rules

- **Decision**: roll-up. The rules apply to every placement in this order: RULES.3 (who may decide at all) → RULES.2 (which end can complete it) → RULES.1 (one authority; copies carry staleness) → RULES.4 (one core for every client) → RULES.5 (atomicity ends at the transaction). The first two are the security and correctness vetoes of FORCES.
- **State**: `known | unvalidated: the order is mine`.

## ALLOCATION.RULES.1 Authority and Copies

- **Positions**: one (L609, L072, L481).
- **Decision**: exactly one tier is the authority for each responsibility. Every other copy is a snapshot (L609): it may be stale without breaking correctness, carries a version or timestamp that detects staleness, and never decides. A copy that rejects input early (a validator) is admitted only when generated from or tested against the authority, so it can never refuse what the authority accepts (F3). Store the minimum and derive the rest (L072). Read-your-writes is a per-operation requirement where a second copy exists: after an asynchronous step, show the pending state from the status resource or the optimistic local value (L481).
- **Rejected**: copies without a staleness marker, or hand-maintained rejecting copies; win never.
- **State**: `known | unvalidated: the rule on rejecting copies is inferred (F3)`.
- **Changed (R1)**: rejecting copies must be generated or tested (F3).

## ALLOCATION.RULES.2 End-to-End Placement

- **Positions**: one (L606-L608).
- **Decision**: place a function at the end that has the knowledge and finality to complete it (L606). Identify the ends first (L608): every writer converges on the database, so the database is an end for rules about stored data; the user is the end for feedback. A partial copy elsewhere exists only to improve performance or latency (L606). A rule in a shared lower tier needs measured performance, because every client pays for it, unless every consumer needs the same rule (L607's own condition), which is the MD-03 default for what must hold whoever touches the data.
- **State**: `known | unvalidated: the data store as an end is inferred (L608)`.
- **Changed (R1)**: L607's exception tied to MD-03.

## ALLOCATION.RULES.3 Trust Boundary

- **Positions**: one (L019).
- **Decision**: any check that grants access or protects integrity runs in a tier the requester cannot modify, the backend or the database. The browser, agent clients, model output and client-supplied hints never decide (L019, L644, L650). Browser checks are feedback; every submitted value is re-checked on the server.
- **State**: `known`.

## ALLOCATION.RULES.4 One Core for Every Client

- **Positions**: one (L633).
- **Decision**: every client drives the same core through adapters that translate and shape only; rules, validation, authorization and state transitions exist once and never in an adapter or a prompt (L633). With several consumers (MD-03) the core has two levels: the database function API is the one core for what must hold for every consumer (operations, transitions with their single writer function, L596, and per-user write rules decidable from the row and the actor, R1-1); each backend's use cases are the core for its own workflow and product policy, and browsers and agents are adapters to a backend. Per-user read visibility is the one place where this rule and MD-01 pull apart (Q1).
- **State**: `known | conflict: per-user read visibility across backends (Q1)`.
- **Changed (R1)**: two-level core under MD-03; Q1 named.
- **Changed (R2)**: per-user write rules placed in the function API (R1-1); Q1 narrowed to reads (R1-2).

## ALLOCATION.RULES.5 Atomicity Ends at the Transaction

- **Positions**: P1 atomicity scoped to one entity, messages across entities (Helland, L477); P2 full cross-table transactions inside one Postgres (L477's single-database reading, L125, L590).
- **Decision**: atomicity exists only inside one database transaction (L623). Within one Postgres, use cross-table transactions, which the function API makes one call (MD-03, L584). **One business operation is one function call in its own transaction; a backend never opens a transaction around several API calls** (R1-4; L066, L584). A step that must be atomic with another step is a new business operation, hence a new function; that function may call another domain's published functions inside the same transaction, so composition across domains happens in the database (X3). What is forbidden across domains is direct access to another domain's tables, not calling its published functions. Workflows across operations advance through state columns and the outbox (ACT.2), with idempotent steps (GUARD.6). Anything that spans the database and an external system is a request to reconcile (outbox, idempotency keys), never a distributed commit. Keep aggregates addressable by key so that a later split stays possible.
- **Rejected**: P1 as a constraint today; wins when a split of the data across nodes or services is planned (L477). Backend transactions wrapping several API calls: the boundary would have two owners (L066 against L584), and the backend would compose a multi-table write after all; wins never in the MD-03 default.
- **State**: `known | unvalidated: the single-Postgres reading of Helland is inferred; the no-wrapping rule is inferred from L066, L584, L623`.
- **Changed (R2)**: one operation, one call, one transaction; workflows through state columns and the outbox (R1-4).
- **Changed (R3)**: cross-domain composition through published functions in the same transaction (X3).

## ALLOCATION.RECORD Data Authority Placements

- **Decision**: roll-up. The server database is the one system of record; consumers reach it through the function API and their own roles; each fact has one origin and the interface description is always in sync with the implementation (MD-02).
- **State**: `known`.
- **Changed (R1)**: function API default (MD-03); one origin per fact (F3); sync by process (MD-02).

## ALLOCATION.RECORD.1 System of Record

- **Positions**: P1 server database as the single system of record (L045, L609, L482, L071); P2 client replica primary, local-first (L302); P3 ordered log as the truth (L626).
- **Forces**: P1 serves correctness: rules that need one global order (uniqueness, balances, authorization) hold. P2 serves latency, offline availability and user ownership; every replica is an authority (L302) and peers cannot enforce server rules (L680). P3 serves correctness of many derived stores and scalability, at the cost of stream infrastructure.
- **Decision**: P1. Postgres is the single system of record for governed business data. Caches, search indexes, browser state, messages and history derive from it in transaction order; no consumer writes two stores (L045, L609). It is the only position under which the rules hold for every write, which MD-03's several consumers make decisive.
- **Rejected**: P2: wins when offline use, multi-device sync or user ownership matter more than central enforcement and the data is user-owned (L302). P3: wins with many derived stores outside the database at high write rate and a team able to run stream infrastructure (L626); in the default, Postgres plus an outbox table plays that role (inferred).
- **Placement**: authority **database**. Copies: browser server-state cache (versioned, for latency), HTTP caches, cache tables, search index, reporting copy, browser drafts of unsent input. Forbidden: any copy acting as authority; dual writes from any consumer. Moved by: offline need with user-owned data; many external derived stores at high write rate.
- **State**: `known`.

## ALLOCATION.RECORD.2 Data Access Interface

- **Positions**: P1 one application owns the database; others go through its service or a read-only reporting copy (L044, L622, L621); P2 shared database behind a database function API owned by the database owner (L515 MAINT, L517, L617, L616); P3 the schema is the API, views and functions (L518, L618, L187); P4 base tables through the ORM (L187, L516).
- **Forces**: changeability (coupling, deploy autonomy) against correctness (one rule for every consumer) and security (per-consumer grants).
- **Decision**: P2 is the default contract (MD-03; L515, L517; MAINT, max).
  - Every consumer has its own role (access paths table above). Backends, consoles and scripts write through the API functions; consumer roles get EXECUTE on the API schema, and on base tables at most SELECT for simple reads (L516). One exception, as in DB_API (R1-5): a direct single-table write grant for a table that only one consumer writes and that has no state column or multi-table effect.
  - BI and reporting read through a read-only role with table and column grants, on a replica or reporting copy when its load matters. Reports bind to table shapes; the coupling is accepted because reports are not part of the operational contract and break visibly (inferred; tension with L622 recorded).
  - Evolution is additive; breaking changes are coordinated with every consumer (L517). "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (X2; this departure from L517 is counted once, at PIG-WEB.DATA.INTERFACE.1).
  - Browsers and agents never connect; they reach data through a backend.
  - A consumer outside the owning team gets the function API as a published contract under L517's rules; a service interface wins where that team needs independent deploys from the database (L622, L044).
- **Rejected**:
  - P1: wins when one backend is truly the only consumer and the team wants no SQL interface (L044, research consensus). Tension recorded: MD-03 sets the shared database as the default against L044 and SRC-216; the doctrine mitigates with the function contract, constraints and roles (L515).
  - P3: views bind consumers to a name and exact shape with nothing to absorb change (L516). Wins when a CRUD-dominant application is served by a database-as-API server with a strong Postgres team (L618).
  - P4 for writes by any consumer: bypasses the operations MD-03 places in the database.
- **Placement**: authority **database function API**, owned by the database owner. Copies: replica or reporting copy for BI. Forbidden: direct writes by consumers to tables with state columns or multi-table effects; database connections from browsers or agents; views as contract. Moved by: a single consumer (P1 possible); a consumer outside the team needing independent deploys (service interface); team SQL skill.
- **State**: `known: MD-03 | conflict: L044 and L622 (research) against the shared database and BI reading base tables`.
- **Changed (R1)**: function API is the default, not the two-backend exception (MD-03); reporting resolved (F5).
- **Changed (R2)**: direct-write exception aligned with DB_API (R1-5).
- **Changed (R3)**: breaking-change condition per X2, departure counted at PIG-WEB.DATA.INTERFACE.1.

## ALLOCATION.RECORD.3 Type and Contract Definitions

- **Positions**: P1 database schema first (L474 MAINT, L485, L549); P2 application models first, code-first (L548, L549); P3 interface description first, design-first (L272, L634); P4 readers take only what they use (L556).
- **Forces**: correctness (no drift between tiers) against changeability (who can change a shape, and how fast).
- **Decision**:
  - **One origin per fact** (L486; F3). A fact about stored data (type, nullability, enum values, ranges, lengths) originates in the database schema, in versioned migrations; the live database is the truth for structure (L474, MAINT, max). Persistence models are generated from the live schema; interface fields that echo a stored fact are generated from the catalogue or checked against it in CI. Which generator: open (none read). A hand-written mirror with a CI comparison is acceptable only when no generator fits.
  - **The database function API's contract** is the function signatures; its documentation is generated from the live database (L474). MD-02's process applies to it too (R1-7): a catalogue diff in CI fails on a removed function or an incompatible signature unless every consumer of the changed object ships in the same deployment as the migration; otherwise the change goes expand, migrate, contract (L517, X2); the backends' typed wrappers are generated from the same catalogue (TYPE_CHAIN).
  - **Every interface description consumers read is always in sync with the implementation** (MD-02, X7): the HTTP description (OpenAPI or equivalent), the database function API catalogue, and the agent tool surface (for example an MCP server's tool list and schemas). This is guaranteed by process: one origin per fact; the other side generated or conformance-checked; review rules on contract diffs; a CI/CD gate that fails on drift.
  - **The origin direction of the interface is a per-project decision**, recorded with its criteria (MD-02):
    - description first when consumers are independent of the producing team (third parties, other teams, agent hosts the team does not control: L634, L635), when several implementations must agree, or when the contract must be agreed before the code (L272; SRC-241 says code-first descriptions are incomplete);
    - code first when every consumer is code the team builds and ships together and the description is a by-product of typed models (L548).
- **Rejected**: P1 for the interface (one class for table and API): acceptable when the API shape equals the storage shape, as in simple CRUD (L549); otherwise fields leak (L553). P4 is a reading discipline for independent consumers (L556), not an origin. The judge's former code-first default and the review's design-first default (F2) are both replaced by MD-02.
- **Placement**: authority **database** for every stored fact and for the function API's contract; **the project's recorded origin** for interface-only facts. Copies: generated persistence models, generated or checked interface models and description, generated browser types (build-time only). Forbidden: hand-copied types without a CI comparison; drift between description and implementation; the browser as an origin. Moved by: project type (MD-02 criteria).
- **State**: `known: MD-02 | unvalidated: generators for persistence models and interface fields not read`.
- **Changed (R1)**: origin per fact (F3); sync by process and per-project direction (MD-02, F2).
- **Changed (R2)**: drift gate on the function API's signatures (R1-7).
- **Changed (R3)**: every interface description consumers read, agent tool surface included (X7); drift gate condition per X2.

## ALLOCATION.GUARD Guarding Placements

- **Decision**: roll-up. Deciding checks run in the database for rules about stored data, for multi-table operations and for per-role access; in the backend for meaning and access that need the end user's identity, policy or request context, and for sessions. Browsers and agent clients only echo checks, for feedback.
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (GUARD.3, Q1)`.

## ALLOCATION.GUARD.1 Validation

- **Positions**: P1 re-validate at every trust crossing, internal transports and stored records included (L612, OWASP); P2 parse once at the boundary into a precise type and trust it after (L484); P3 split by kind: syntax at the edge, meaning with the state (L611).
- **Forces**: security and correctness against latency of feedback and changeability.
- **Decision**: parse at every point where data enters a process from outside its type system (browser to backend, agent to backend, queue or stored payload to worker, any consumer to a database function) into the most precise type, once, and trust the type inside that process (L484; L612). At the function API the precise types are the parameter types and domains, so every consumer's input is checked by the database (MD-03, L485). Meaning sits with the tier that holds the state: database constraints and functions decide rules about stored rows (GUARD.2), the backend decides rules that need the end user or policy (L611). Checks in the browser or an agent client are feedback copies, generated from or tested against the authority (L019, RULES.1).
- **Reconciliation**: P1 and P2 disagree only on what a boundary is; taking every deserialisation point as a boundary gives both.
- **Placement**: authority **backend** (parsing, request-level meaning) and **database** (function parameters, meaning about stored data). Copies: browser checks, for feedback. Forbidden: browser, agent client or model output as the deciding check. Moved by: tiers with different owners or trust levels (more crossings).
- **State**: `known | unvalidated: the reconciliation of P1 and P2 is mine`.
- **Changed (R1)**: function API as a crossing (MD-03); label inferred in the matrix (F6).

## ALLOCATION.GUARD.2 Invariants

- **Positions**: P1 declare in the database (L040, L473, L471 MAINT); P2 application-only validation (common practice, rejected by L473 for uniqueness); P3 database functions and triggers for multi-row rules (L528 MAINT, L471).
- **Forces**: correctness against changeability (testing needs a live database, tooling).
- **Decision**: rules that must hold whatever writes the data are enforced by the database (MD-03).
  - Declarative constraints (NOT NULL, CHECK, UNIQUE, foreign keys, domains) for every rule they can express: required. For cross-row rules, a partial unique index or an exclusion constraint first (L174, L175); these are safe under concurrent writers at any isolation level and bind every writer, owner-run migrations included.
  - Rules beyond them (other multi-row rules, legal state transitions): a constraint trigger or the writer function, run under Serializable isolation with retry, or after locking the governing row; the trigger asserts the isolation level it needs (F4; L569, L577, SRC-331). Read Committed alone admits violations, and Repeatable Read admits write skew (L577).
  - The default isolation is handed to the DATA judge (PIG-WEB.DATA.CONCURRENCY.1) with this constraint; the review recommends L568 (a), Serializable with retry as the default (L569), and I concur (inferred). Hand-off conditions (R1-9; L573): set the default isolation per consumer role, because a lower-isolation transaction from any writing role voids the Serializable guarantee; writer functions assert the isolation level, as triggers do; reports on a replica cannot be Serializable and accept snapshot anomalies.
  - Backend and browser validators are generated from or tested against the constraints (F3, RULES.1); named constraints map violations to stable errors (L495).
- **MAINT**: L471 adopted on authority. **Against L471** on "triggers and CHECK constraints optional as defence in depth": procedural checks, inside a function or a trigger, need serializable isolation or a lock to be correct (L473, L577), and only declarative constraints bind every writer, owner-run migrations and human-run jobs included; the function API's privilege wall does not cover the owner role.
- **Rejected**: P2 for any rule that must hold for every writer; wins never.
- **Placement**: authority **database**. Copies: generated or tested backend validators and types, browser feedback. Forbidden: application-only enforcement of any rule that must hold for every writer; a procedural check under Read Committed without a lock. Moved by: nothing in the default.
- **State**: `known | conflict: against L471 (MAINT) on optional CHECK constraints | unvalidated: default isolation level belongs to the DATA judge`.
- **Changed (R1)**: multi-row branch under Serializable or a lock (F4); ground against L471 narrowed (F4); copies generated or tested (F3); several writers per MD-03 (F5).
- **Changed (R2)**: isolation bound per consumer role; writer functions assert it; replica reports accept snapshot anomalies (R1-9, L573).

## ALLOCATION.GUARD.3 Authorization

- **Positions**: P1 backend only (L020, L620, L305, L306); P2 the database enforces through roles and row-level security (L619, L620, L688); P3 two layers: database permissions limit objects, application permissions decide business actions (L468 MAINT, L620, L128).
- **Forces**: security against changeability of policy.
- **Decision**: P3, two layers (MD-01; L468, MAINT, max). With several consumers the work divides by **where the rule's facts live** (R1-1; inferred from MD-03 and L608).
  - **The writer function decides per-user write rules that can be decided from the stored row and the acting user** (author, owner, assignee: "only the assignee may close a task") and that must hold for every consumer (MD-03, L596, ACT.1). A backend's identical check is a copy for early feedback, generated or tested under RULES.1.
  - **Each backend decides product policy that is not stored in the data**: product roles, plan limits, feature flags, workflow steps; and who the human or agent is. One central mechanism per backend, deny by default, object level, on every request from every client (L020, L305, L306, L644).
  - **The database decides per consumer**: each consumer has its own role, neither owner nor superuser. Grants say which API functions it may EXECUTE, which tables and columns it may SELECT, and that it writes no table directly except under DB_API's exception; state columns are revoked from UPDATE so the writer function is the only path (L468, L310, L596). This bounds what every backend, BI tool, console and script can do whatever its code.
  - **Functions** run with their owner's rights only where they must write tables the caller cannot. They read the acting user from a transaction-local setting (L311, L566). That actor is the consumer's claim, not a verified fact (R1-3): functions refuse a write without an actor, check that the session role may assert that kind of actor (a backend an end user, an operator or owner role only itself; default-context table), and record both the session role and the claimed actor.
  - **Row-level security** is not used by default (MD-01). It is acceptable only when the data model is simple, the scoping key leads the composite primary key of every table the policy covers, and no all-powerful administrator role must read or write across scopes (MD-01).
- **Undecided clause (Q1)**: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Read visibility of rows that carry per-user rules ("a draft is visible only to its author"; comments on restricted targets are covered by the same rule). Under MD-01 as written each backend filters reads, one copy per backend, against RULES.4 (L633). Writes are not in the question: they are settled above under MD-03.
  - Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs (X1).
  - Fallback kept, not forbidden: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends (X1). Under MD-03 several backends share the database by default, so this condition is always met: the fallback is available wherever MD-03's default holds. The actor is verified by the backend that asserts it and is a claim to the database (R1-3).
  - Consequence, under either position: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted. No statement in this guideline claims stronger visibility than this (X1).
- **Tension (MD-01 against evidence)**: L619 and L688 call for row security when several applications or agents read the database, which MD-03 makes the default. MD-01 overrides; the residual risk is that a consumer with SELECT on a table sees every user's rows, and that each backend's read filter is the only per-user gate on reads.
- **Rejected**: P1 without the database layer; wins never (L468). P2 as sole authority: loses product policy that lives in application code (L468); row-level security wins only under MD-01's conditions. The backend as authority for per-user write rules decidable from the row: two authorities for one rule (R1-1); the backend keeps a tested copy.
- **Placement**: authority **writer function** for per-user write rules decidable from the row and the actor; **backend** for product policy not stored in the data and for identity; **database** per consumer role. Copies: the backend's check of per-user write rules (generated or tested, early feedback); the browser hides controls the user may not use (cosmetic). Forbidden: browser, agent client, model output, client hints; row security by default (MD-01); any consumer role owning tables or bypassing grants; a write without an actor, or with an actor its role may not assert. Moved by: MD-01's three conditions (row security becomes acceptable); Q1's answer (read visibility into read functions).
- **State**: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database | known: two layers per MD-01; write rules in writer functions (MD-03) | conflict: L619, L688 favour row security when several consumers share the database (MD-03)`.
- **Changed (R1)**: division of work with several consumers (MD-03); row security per MD-01 (F1 closed); new clause Q1.
- **Changed (R3)**: Q1 notation unified; recorded default and fallback reworded; comments covered; visibility of SELECT-capable roles stated (X1).
- **Changed (R2)**: one authority per per-user write rule, the writer function; backend check is a tested copy; backend owns product policy not stored in data (R1-1). Actor treated as a claim, pairing checked, writes without actor refused (R1-3). Q1 narrowed to read visibility, awaiting maintainer (R1-2).

## ALLOCATION.GUARD.4 Identity and Session State

- **Positions**: P1 server-held opaque session, HttpOnly cookie (L315, L022, L319, L086); P2 backend-for-frontend holds the tokens (L313, L314); P3 browser application holds bearer tokens (L316, L320, L321); P4 no application state in cookies (L318).
- **Forces**: security (token theft, revocation) against scalability and latency (stateless verification).
- **Decision**: each backend holds the sessions and credentials of its users; the browser holds only an HttpOnly, Secure, SameSite cookie carrying an opaque identifier.
  - Default (first-party, same-site browser): an opaque server-side session, revoked on logout (L315, L022, L319), stored in a backing service, never in process memory (L086).
  - Login through an external identity provider: backend-for-frontend (L313).
  - Agents and other non-browser clients: bearer tokens per delegation, short-lived, with server-held state that can revoke them (L316, L022).
  - Database roles identify consumers, never end users; the end user reaches the database only as the actor a backend asserts in a transaction-local setting, from its verified identity, checked against the backend's role (R1-3) (L311, L566).
- **Rejected**: P3 for the browser: wins only when no backend is possible (L314); localStorage acceptance (L320, L321) loses. P4 as stated loses; its narrow sense is kept: the cookie carries an identifier, never application state.
- **Placement**: authority **backend** (session store in Postgres under POSTGRES_FIRST). Copies: the browser's opaque cookie; an agent's own bearer token. Forbidden: tokens in JavaScript-readable storage; any session token, bearer token or long-lived credential in a URL, the one exception being short-lived, single-purpose, scope-limited signed URLs for file delivery, with lifetime and scope stated (X6); session state in process memory; stateless, non-revocable sessions; end users as database roles. Moved by: client kind; instant revocation; no backend possible.
- **State**: `known`.
- **Changed (R1)**: end user versus consumer role stated (MD-03).
- **Changed (R3)**: no tokens in URLs except short-lived signed file URLs (X6).

## ALLOCATION.GUARD.5 Concurrency Control and Conflict Resolution

- **Positions**: P1 the database decides (L628, L473, L568); P2 optimistic version across requests (L475, L260); P3 pessimistic checkout (L570); P4 silent last-writer-wins per property (L674); P5 merge on the client (L677, L302).
- **Forces**: correctness (no lost update) against latency and user effort.
- **Decision**: the database detects; the conflict policy follows the data shape (L678).
  - Detection: constraints, isolation, row locks and version checks inside one short transaction, inside the writer function (L628, L473, L475; MD-03). Isolation level per GUARD.2 (DATA judge).
  - Discrete fields edited by users (default): optimistic version; ETag and If-Match; a stale write is rejected (412); the condition is required (428) where a lost update matters (L475, L260). The writer function takes the expected version as a parameter.
  - Toggles, status, assignment, ordering: per-property last-writer-wins is acceptable (L674).
  - Frequent conflicts with costly lost work: a lease with owner and expiry, checked by the writer function (L570).
  - Long collaborative text: a text engine with the server as central authority (L677, L679).
  - Never a transaction or lock held across user think time (L475).
- **Rejected**: silent whole-record last-writer-wins; wins never (L674). P5: wins with local-first data or offline and peer-to-peer text (L677). Check-then-write without serializable isolation or a lock; wins never (L628).
- **Placement**: authority **database** (detection in the writer function), with the **backend** carrying the version through its contract. Copies: the browser holds the version it read. Forbidden: browser or agent resolving conflicts; locks across requests. Moved by: conflict rate, data shape, edit length, offline use.
- **State**: `known`.
- **Changed (R1)**: detection inside the writer function (MD-03); isolation handed to DATA (F4).

## ALLOCATION.GUARD.6 Duplicate Suppression

- **Positions**: P1 idempotent by design (L051, L655, L587, L588); P2 idempotency key recorded with the effect (L269, L546, L270, L599); P3 layered across tiers (L582).
- **Forces**: correctness of effects against simplicity.
- **Decision**: layered, and the database decides. Ground: exactly-once is unavailable across a process or network boundary, and a lost acknowledgement leaves the caller unsure (L478, L479); effects are made effectively-once by at-least-once delivery plus idempotence where the effect is recorded.
  1. Idempotent by design where the domain allows: client-supplied identifiers, upserts, absolute assignments (L655, L587 MAINT, L588).
  2. Otherwise an idempotency key recorded by the API function in the same transaction as the effect; the first response is replayed and a different payload under the same key is rejected (L269, L546, L270, L599). Required on every mutation offered to agents that is not idempotent by design, and on payment-like creates (L051).
  3. A unique constraint as the backstop (L582).
  The browser layer (disable resubmission, 303 after POST, a form token minted at render) only reduces repeats (L582).
- **Rejected**: P1 alone: wins when every mutation has a natural idempotent form. A key store apart from the effect; wins never (L270, L479).
- **Placement**: authority **database** (key and effect in the writer function's transaction; unique constraint as final arbiter); the **backend** passes the key through its contract. Copies: browser pending state and form token; agent clients send keys. Forbidden: the browser as the only guard; a key store separate from the effect. Moved by: automated callers; payment-like or external effects.
- **State**: `known`.
- **Changed (R1)**: key recorded inside the API function (MD-03).

## ALLOCATION.ACT Acting Placements

- **Decision**: roll-up. The database carries the business operations that change data (functions behind the API, one writer per state column), the invariants, the staged intent of side effects and deferred work, and history (MD-03). The backends orchestrate operations into workflows, call the outside world and decide what to defer.
- **State**: `known`.
- **Changed (R1)**: operations moved to the database (MD-03).

## ALLOCATION.ACT.1 Business Rules and State Transitions

- **Positions**: P1 application first; profile, move proven hot spots to SQL; the use-case layer owns the transaction (L215, L066, L226); P2 split by kind, middle zone disputed (L214); P3 database behind a cost-benefit gate, with a listed in-database band and one writer per state column (L527, L528, L584, L596, all MAINT); P4 thick database, SmartDB (L616, L617).
- **Forces**: correctness across several writers, round trips and lock time (L614) against changeability (testability, tooling, skill: L042, L472).
- **Decision**: P3, with MD-03 meeting L527's gate by default (reuse by two or more consumers).
  - **Database**: everything that must hold whoever writes: constraints and multi-row invariants (GUARD.2); every operation that changes several tables as one business operation, as one database function (L584, MD-03); state transitions, each state column with exactly one authoritative writer function that every entry point (backends, consoles, ingestion, agents through a backend) routes through and that logs each transition (L596); per-user write rules decidable from the stored row and the acting user (author, owner, assignee), decided by that writer function, with any backend check a generated or tested copy (R1-1); set-based algorithms over large data (L528, L613).
  - **Owner-run jobs** (R1-6): the owner role bypasses grants and column revokes, but not constraints or triggers (GUARD.2). A data job that changes a state column calls its writer function, or is a recorded exception under L545's checklist, with the operator and ticket id set as actor (R1-3).
  - **Backend**: workflow orchestration across operations, product policy not stored in the data (product roles, plan limits, feature flags, workflow steps: R1-1), external calls, presentation, sessions and authentication (L528's application half).
  - **Unit of work (R1-4)**: one business operation is one function call in its own transaction; a backend never opens a transaction around several API calls. A step that must be atomic with another is a new business operation, so a new function, which may call other domains' published functions in the same transaction (X3); direct access to another domain's tables is forbidden. A workflow across operations advances through state columns and the outbox (ACT.2), each step idempotent (GUARD.6). L066's "one boundary per operation" holds, with the function as its owner (L584).
  - **Enforcement**: consumer roles hold no UPDATE on state columns and no direct write on tables with multi-table effects; the writer functions do (L596; F8).
  - L584 stands (MD-03); L527, L528 and L596 are the max choice.
- **Costs weighed (F8)**: one round trip per operation instead of one per statement (L614), and locks held for one call instead of across round trips, which also lowers retries under Serializable (inferred); against that, tests need a live database (L042, L472) — already true for any use case whose invariants the database guards (GUARD.2) — and tooling and onboarding costs (L472), paid with versioned migrations and CI against a live database (FORCES.6).
- **Tension (MD-03 against evidence)**: research puts domain logic in the application first, profiling hot spots into SQL (L215, Fowler, T2), and keeps the transaction boundary in the use-case layer (L066); the doctrine's heavier-database position is what L214 calls the disputed middle zone. MD-03 decides it for this guideline.
- **Rejected**:
  - P1: wins when one backend is the only writer, the team's SQL skill is low (L041), and policy changes faster than migrations can follow (L215).
  - P4 (workflow and external calls in the database too): external calls cannot run inside a database transaction (L234) and stay in the backend (L528).
- **Placement**: authority **database** for operations, transitions, invariants and per-user write rules decidable from the row; **backend** for workflow, product policy not stored in the data and external calls. Copies: the backend's check of per-user write rules (generated or tested); the browser previews which actions are allowed (feedback). Forbidden: multi-table writes composed in a backend; a backend transaction wrapping several API calls; business rules in the browser, agent adapters or prompts (L633); a second writer of a state column, owner-run jobs included unless a recorded exception. Moved by: a single consumer with low SQL skill (P1); latency-critical multi-statement operations reinforce the database placement.
- **State**: `known: MD-03, L584 | conflict: L215, L066 (research, application first)`.
- **Changed (R1)**: re-judged under MD-03; the verdict against L584 is withdrawn; costs weighed (F8); column privileges as enforcement (F8).
- **Changed (R2)**: per-user write rules in the writer function, backend product policy defined (R1-1); one operation, one call, one transaction, no wrapping (R1-4); owner-run jobs through the writer function or a recorded exception (R1-6).
- **Changed (R3)**: cross-domain composition through published functions (X3).

## ALLOCATION.ACT.2 Side Effects and Integrations

- **Positions**: P1 backend effects staged in the database and delivered after commit (L624, L409, L410); P2 post-commit hooks in the request process (L600, L233); P3 atomic phases with recovery points (L589, L234, L246); P4 sagas with compensation (L590, L480).
- **Forces**: correctness (no lost or doubled effect) against request latency.
- **Decision**: P1. The database function that performs the state change writes the intent (outbox row or staged job) in the same transaction (L624, L409); a backend worker delivers it after commit to idempotent consumers (L410, L599). External calls are made by backends, never by the database. No database transaction stays open across a remote call (L234).
  - **Foreign mutations** (a payment, a remote API write) run as atomic phases with recovery points and an idempotency key passed to the foreign system (P3 as a complement: L589, L234, L246), **in a worker behind a 202 response with a status resource** (ACT.3, L271, L602).
  - **In the request only when the user must see the outcome within about 1 s** (L013): the database function still records the intent (outbox row) first and commits; the request then performs the call as one atomic phase with the idempotency key and marks the row done. If the request dies, the worker's completer picks the row up (L589). (Revision 3: adopted from the logic unit's realization, M4.)
- **Rejected**: P2 (post-commit hook): acceptable only for losable work that touches no foreign system, such as cache invalidation (L600); a losable notice to a foreign system still goes through the outbox, which costs one row. P4: only when one business transaction spans services with separate databases (L590, L480).
- **Placement**: authority **backend** (delivery, external calls), **database** (the staged intent, written by the operation). Copies: none. Forbidden: third-party credentials in the browser (inferred, L624); calls to external systems from inside the database; dual writes to the database and a broker; remote calls inside an open transaction; a foreign call in the request without its intent recorded first; post-commit hooks for foreign effects. Moved by: an outcome the user must see within about 1 s (in-request phase, intent recorded first); a business transaction crossing services with their own databases (saga).
- **State**: `known | unvalidated: the 1 s in-request exception is inferred (L013, L589)`.
- **Changed (R1)**: intent written by the database function (MD-03).
- **Changed (R3)**: tension with ACT.3 resolved: foreign mutations in a worker behind 202; in the request only for an outcome needed within about 1 s, intent recorded first; post-commit hooks only for losable work touching no foreign system (logic review M4).

## ALLOCATION.ACT.3 Deferred and Scheduled Work

- **Positions**: P1 inside the request what the user sees next (L601); P2 separate worker processes (L406, L407); P3 scheduled work inside the database (L604 MAINT); P4 asynchrony only for derived data and bulk jobs (L482 MAINT, L545).
- **Forces**: latency against correctness and scalability.
- **Decision**:
  - Inside the request: validation, authorization, every change atomic with what the user sees next, and the persisted intent of deferred work, in one transaction, which is one function call when the change is a database operation (L601, MD-03). Core writes are never asynchronous (L482, MAINT, max).
  - Deferred: foreign effects, work that would push the response past the 1 s flow budget (L013, L271), fan-out, derived data. Foreign mutations run as atomic phases in a worker behind 202; the one in-request exception is ACT.2's: an outcome the user must see within about 1 s, with the intent recorded by the database function first.
  - Host: workers fed from the database-staged queue (L406, L407, L409); scheduled pure data work inside the database (L604; JOB_HOST).
  - An operation that outlasts the request answers 202 with a status resource (L271, L602). Every asynchronous stream states its staleness window and a convergence check (L482).
- **Rejected**: in-process background tasks: only for small tasks that may be lost (L407). P3 for everything: not for Python logic, foreign effects, highly parallel or OS-level work (L604).
- **Placement**: authority **backend** (what is deferred) and **database** (staged intent, data schedules). Copies: the status resource shows the pending state. Forbidden: deferring core writes; foreign effects inside the request, except ACT.2's in-request phase (outcome needed within about 1 s, intent recorded first). Moved by: duration, foreign effects, set-based data work.
- **State**: `known | unvalidated: the 1 s threshold is my choice between L601's two rules of thumb`.
- **Changed (R3)**: in-request exception aligned with ACT.2 (logic review M4).

## ALLOCATION.ACT.4 Audit and History

- **Positions**: P1 written where writes converge, atomically, actor passed in (L627, L684, L212, L566); P2 application-level history (L627, L208); P3 two separate records, security event log and business audit trail (L049, L392).
- **Forces**: correctness (completeness) against changeability (hidden behaviour, testability).
- **Decision**: P1 and P3; audit is the database's (MD-03).
  - Business history is written by database triggers into append-only history tables, in the same transaction as the change (L627, L212). The writer functions log each transition (L596).
  - **Actor (R1-3)**: each history row records both the session role, which the database verifies, and the claimed actor from the transaction-local setting (L566 MAINT, L311), which the consumer sets. Triggers and writer functions refuse a write with no actor, and check that the session role may assert that kind of actor (default-context table: a backend may assert an end user; operator and owner roles only themselves, with the ticket id for owner-run jobs, L545).
  - Agent actions carry acting identity, delegating subject, operation, correlation id and outcome, on the server (L658); agent-originated writes are marked in the data (L659).
  - Business events that row changes do not express (reason, intent) are passed by the backend to the function, which records them in the same transaction.
  - The security event log is a separate record with its own store, integrity and retention (L049, L392).
- **Evidence note (F12)**: L684 is marked grounded in the ledger with no source; flagged to the ledger owner. Until fixed, the verdict rests on MD-03, L627 (inferred) and L212 (grounded for the mechanism).
- **Rejected**: P2 alone: wins when only one application writes and business events matter more than row changes (L627); never in the MD-03 default.
- **Placement**: authority **database** (history, transitions logged by writer functions); **backend** supplies actor and business events; a **separate log sink** holds security events. Copies: none. Forbidden: application-only audit; audit only in a model transcript; an actor taken from a client-supplied id; a write without an actor; an actor the session role may not assert. Moved by: nothing in the default (several writers by MD-03).
- **State**: `known: MD-03 | gap: L684 cites no source; evidence for the trigger placement is inferred (L627)`.
- **Changed (R1)**: decided by MD-03; evidence note (F12); label (F6).
- **Changed (R2)**: session role and claimed actor both recorded; writes without actor refused; actor pairing checked (R1-3).

## ALLOCATION.DERIVE Derivation Placements

- **Decision**: roll-up. Derived data is computed where its source is, as close to the source transaction as its freshness requires; queries reduce data where it lives, with the database's collation; every derived copy states its staleness.
- **State**: `known`.

## ALLOCATION.DERIVE.1 Derived Data and Aggregation

- **Positions**: P1 inside the database with the source (L176, L532, L534, L536); P2 from an ordered log by a dedicated process (L626, L045); P3 computed on read (L488 MAINT).
- **Forces**: correctness against performance and scalability.
- **Decision**: choose the tier by required freshness and atomicity (L625), in this order (my order, F6): compute on read when affordable (L488, L072); when it must change atomically with the source, maintain it in the database in the same transaction (generated column, trigger: L176, L532); when a stated staleness is acceptable, database cache tables with an invalidation queue or scheduled refresh (L532, L535, L536, all MAINT). The doctrine is the max choice here.
- **Rejected**: P2: wins with many derived stores outside the database, a high write rate and a team able to run stream infrastructure (L626). Dual writes by any consumer: never (L045).
- **Placement**: authority **database**. Copies: derived columns and tables with a stated staleness. Forbidden: consumers writing derived stores beside the source. Moved by: number of external derived stores, write rate, staleness tolerance.
- **State**: `known | unvalidated: the order of options is mine (L625 inferred)`.
- **Changed (R1)**: order marked as mine (F6).

## ALLOCATION.DERIVE.2 Filtering, Sorting, Paging and Search

- **Positions**: P1 with the data, set-based (L613, L614); P2 reads bypass the domain model (L237); P3 in the backend or browser on a loaded set (no row; skeleton gap 2).
- **Forces**: performance and latency against scalability (L615 exempts reductions that return small results).
- **Decision**: the database reduces many rows to the few a client needs, set-based, in one statement or read function; only the result travels (L613, L614). The server enforces a maximum page size and pages by keyset behind an opaque continuation (L265, L266, L541). Reads that need no domain behaviour may be plain queries (P2, L237; L516). Search follows the same placement and stays deferred. **Collation (F11)**: the database owns the collation of every order it serves, declared per column or per query; which collation is open, under DATA.
- **Gap handling (P3)**: no row argues for it; rejected as an authority on L613, L614, L615. Kept only as a copy: the browser may re-sort or filter rows it already holds, for instant feedback, with the same locale as the database's collation or not at all (F11), never deciding which rows exist beyond them. This condition is inferred.
- **Placement**: authority **database**, including collation. Copies: the browser over rows already loaded, same collation. Forbidden: loading full sets into a backend or browser to reduce them; queries in loops; a browser re-sort with another collation. Moved by: data volume against result size; write load.
- **State**: `known | gap: P3 unargued; browser-copy condition inferred | unvalidated: collation choice open (DATA)`.
- **Changed (R1)**: collation owned here (F11).

## ALLOCATION.DERIVE.3 Caching

- **Positions**: P1 cache tables in the database (L534 MAINT, L535); P2 shared cache service (L417); P3 HTTP caches in browsers and intermediaries (L010, L414-L416); P4 server state cached in the browser (L071, L291).
- **Forces**: latency and performance against correctness (staleness).
- **Decision**: the positions are kinds of cache; each cache is a copy with a stated staleness bound and an expiry or invalidation plan (L419, L609).
  - Derived-data caches: database tables, invalidated in the source transaction (L534, MAINT, max).
  - HTTP: every response labelled on purpose; HTML no-cache with validators; fingerprinted assets immutable; personalised responses private or no-store; lifetimes set by tolerable staleness (L414, L415, L416, L010).
  - Server state in client-rendered parts: a client cache with background refresh (L071, L291).
  - Response and fragment caches shared by processes: Postgres by default under POSTGRES_FIRST (L125, inferred), a cache service on measured need (CACHE_STORE; F7).
- **Rejected**: per-process memory shared beyond one request in multi-process production (L417, L086); a cache as permanent storage (L417).
- **Placement**: authority **none**: the source is the authority. Copies allowed in: database tables, a shared backend store, HTTP intermediaries, the browser. Forbidden: process memory beyond one request; personalised responses in shared caches. Moved by: staleness tolerance, number of processes, need for atomic invalidation.
- **State**: `known`.
- **Changed (R1)**: L534 limited to derived-data caches (F7).

## ALLOCATION.PRESENT Presentation Placements

- **Decision**: roll-up. Backends render HTML and format what they render; the browser enhances, holds ephemeral and in-progress state and formats what it renders itself; durable and shared state stays in the database.
- **State**: `known`.

## ALLOCATION.PRESENT.1 Rendering

- **Positions**: P1 server-rendered hypermedia (L252, L629, L630, L003); P2 client-rendered application over a JSON API (L252, L253); P3 hybrid server-first (L252, L255); P4 decide per page (L281).
- **Forces**: latency and changeability against correctness (one source of logic).
- **Decision**: server-rendered HTML is the default contract with the browser. The backend holds rendering and navigation; pages work as HTML and are enhanced with CSS and JavaScript (L629, L003, L281). A page or region becomes a client-rendered island when it meets L253's criteria. Agents get their own adapter over the same core (RULES.4). Grounds: one source of logic, LCP from server-visible content (L297), a small JavaScript budget (L016). Unchanged by MD-03: rendering is per backend.
- **Rejected**: P2 as default: wins when most of the product meets L253's criteria (L254). P3: wins for transitional apps (L255) when the team commits to a JavaScript server. P4 is kept as the mechanism for islands.
- **Placement**: authority **backend** (HTML and navigation logic). Copies: browser view state and islands' client state. Forbidden: business rules in browser code. Moved by: UI interdependence, offline use, update frequency, crawlability.
- **State**: `known | unvalidated: the default is a judgment; positions are T3 and T4, neutral T1 guidance accepts it (L281)`.

## ALLOCATION.PRESENT.2 Formatting and Localization

- **Positions**: P1 at the edge nearest the reader, storage canonical (L632); P2 database collation (inferred, open, L632). Skeleton gap 3: one grounded position.
- **Forces**: correctness of stored data against user experience.
- **Decision**: storage is canonical (UTC timestamps with zone, plain numbers, codes). The tier that renders the text formats it for the reader: the backend for the HTML, email and PDF it renders, with the reader's locale and time zone; the browser runtime (Intl) for client-rendered islands (L632).
- **Gap handling**: no competing placement exists; L632 rests on a capability page. P2 is not a formatting placement: collation is owned by DERIVE.2 (the database, for any order it serves; F11), its choice open under DATA. Internationalisation stays deferred.
- **Placement**: authority **the rendering tier** (formatting), **database** (canonical values). Copies: none. Forbidden: formatted or local-time values stored as data. Moved by: which tier renders the text.
- **State**: `speculative: placement inferred from a capability source (L632) | gap: one position only`.
- **Changed (R1)**: collation handed to DERIVE.2 (F11).

## ALLOCATION.PRESENT.3 UI and Ephemeral State

- **Positions**: P1 by lifetime and sharing (L631, L070, L292); P2 server state in the browser is a cache (L071, L291); P3 presence is ephemeral (L681); P4 local-first (L302).
- **Forces**: latency against correctness.
- **Decision**: P1, with P2 and P3 as its rules. Ephemeral view state in the browser; form state in the browser until submitted; shareable view state in the URL (L292); durable or shared state in the database; server state held in the browser is a stale-able cache (L071); presence is broadcast through a channel with a timeout and never written to tables (L681).
- **Rejected**: P4: RECORD.1's condition.
- **Placement**: authority **by kind**: browser, URL, database, channel. Copies: the browser's server-state cache. Forbidden: presence in database tables; durable state held only in the browser. Moved by: offline use; sharing between users or tabs.
- **State**: `known | unvalidated: the four kinds are a synthesis (L070)`.

## PIG-WEB.ALLOCATION Stack Allocation

- **Decision**: roll-up. Postgres carries the data, the function API every consumer calls, the per-role grants and the backing roles (queue, schedules, derived caches, sessions) until a measured limit; Python backends own sessions, per-user authorization, workflow and HTML rendering; browser JavaScript enhances; no JavaScript server tier; no row-level security by default (MD-01).
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (GUARD.3, Q1)`.
- **Changed (R1)**: MD-01, MD-03.

## PIG-WEB.ALLOCATION.POSTGRES_FIRST Postgres First for Backing Roles

- **Positions**: P1 one Postgres until a measured limit (L125, L534, L604); P2 specialised services from the start or past the limit (L126, L417, L457).
- **Forces**: changeability (fewer components) and correctness (backing roles share the data's transaction) against scalability.
- **Decision**: P1. Postgres carries the job queue, schedules, derived caches, sessions and documents until a measured limit for that role. Each role names its trigger: queue lock contention or backlog age; NOTIFY's commit serialisation under write concurrency; cache latency or cache load on the primary. NOTIFY is a low-rate wake-up, never the message carrier (L127).
- **Rejected**: P2: wins past a measured limit, or where the framework's only production backend is a service (Django's channel layer on Redis, L457).
- **Placement**: authority **Postgres** per role. Forbidden: a second store written beside Postgres without staging. Moved by: write concurrency, queue volume, fan-out processes.
- **State**: `known | unvalidated: L125 rests on T4 sources and the T1 SKIP LOCKED page; thresholds open (L126, L127)`.

## PIG-WEB.ALLOCATION.DB_API Database Function API

- **Positions**: P1 function API, backend of backends (L515 MAINT, L617); P2 schema as the API, views and functions (L518, L618, L187); P3 ORM over base tables, views off the contract path (L187, L516 MAINT).
- **Forces**: changeability against correctness for several consumers.
- **Decision**: P1 is the default contract (MD-03; L515, L517, L617; MAINT, max).
  - A dedicated API schema of functions; each consumer role gets EXECUTE on the functions it uses and nothing to write on base tables; state columns are written only by their writer functions (L596).
  - Writes go through functions: every multi-table operation and every state transition (MD-03, L584, L596). A direct single-table write grant is acceptable for a table that only one consumer writes and that has no state column or multi-table effect (L527's default; inferred).
  - Simple reads may query base tables under SELECT grants (L516); read functions where a read must apply a rule.
  - A procedure only where transaction control is needed (L516). Evolution is additive, breaking changes coordinated with every consumer (L517); no formal version numbers, a new function name carries the change; "deployed together" only when every consumer of the changed object ships in the same deployment as the migration, otherwise expand, migrate, contract (X2, counted at PIG-WEB.DATA.INTERFACE.1). Views are never contract objects (L516).
  - Functions live in versioned migrations and are tested against a live database in CI (FORCES.6).
  - **Drift gate (R1-7, MD-02)**: a catalogue diff in CI fails on a removed function or an incompatible signature unless every consumer of the changed object ships in the same deployment as the migration; otherwise the change goes expand, migrate, contract (L517, X2); the backends' typed wrappers are generated from the same catalogue.
  - **One call per operation (R1-4)**: each API call runs in its own transaction; consumers do not wrap several calls in one (RULES.5).
- **Rejected**: P2: views bind consumers to a name and exact shape (L516); wins when a CRUD-dominant application is served by a database-as-API server with a strong Postgres team (L618). P3 for writes: bypasses the operations MD-03 places in the database; for simple reads it is kept (L516).
- **Placement**: authority **the Postgres function API**. Forbidden: direct consumer writes outside the exception above; views as contract; consumer roles owning objects. Moved by: a single consumer (direct queries become the default again, L527); team SQL skill.
- **State**: `known: MD-03 | conflict: views as contract (L187, L518) rejected in favour of L516 (MAINT)`.
- **Changed (R1)**: function API is the default (MD-03).
- **Changed (R2)**: drift gate on signatures (R1-7); no transaction around several calls (R1-4).
- **Changed (R3)**: X2 wording for breaking changes, departure counted at PIG-WEB.DATA.INTERFACE.1.

## PIG-WEB.ALLOCATION.TYPE_CHAIN Type Definition Chain

- **Positions**: P1 Postgres schema first, one class for table and validation (L549); P2 Pydantic models first, OpenAPI generated and committed (L548); P3 OpenAPI first, checked in CI (L272).
- **Forces**: correctness against changeability.
- **Decision** (RECORD.3, MD-02):
  - **Stored facts**: the Postgres schema in migrations is the origin; Python persistence models and the typed wrappers of API functions are generated from the live catalogue (generators open); field types in interface models that echo a stored fact are generated from it or checked against it in CI (F3).
  - **Default interface chain (F9)**: the browser receives HTML (PRESENT.1), so the default chain starts at form and query input parsed into Pydantic models (GUARD.1), then reaches the agent surface (L634, L635) and any JSON endpoints.
  - **The OpenAPI description, and the agent tool descriptions derived from the same core, are always in sync with the Pydantic models** (MD-02): one origin per fact, the other side generated or conformance-checked, review rules on contract diffs, a CI/CD gate failing on drift. Which side is the origin is recorded per project with RECORD.3's criteria: OpenAPI first for independent consumers or agent hosts the team does not control; Pydantic first when every consumer ships with the team.
  - **TypeScript types** are generated from the description for client-rendered islands only, build-time only (L555).
- **Rejected**: P1's single class: acceptable for simple CRUD where shapes are equal (L549). The former fixed defaults (judge: Pydantic first; review: OpenAPI first) are replaced by MD-02's per-project decision.
- **Placement**: authority **Postgres schema** (stored facts), **the project's recorded origin** (interface-only facts). Forbidden: hand-written copies without a CI comparison; drift between description and models. Moved by: project type (MD-02).
- **State**: `known: MD-02 | unvalidated: generators not read; no source recommends the whole chain (L549)`.
- **Changed (R1)**: per-project origin and sync process (MD-02, F2); chain starts at HTML forms and the agent surface (F9); stored facts from the catalogue (F3).

## PIG-WEB.ALLOCATION.ROW_SECURITY Row Security Placement

- **Positions**: P1 row security on every path (L619); P2 row security only with several consumers (L688); P3 row security as a second line (L128).
- **Forces**: security (defence in depth per user) against changeability and testability of policy, and against the administrator roles and composite keys row policies require.
- **Decision**: row-level security is not used by default (MD-01). It is acceptable only when all three hold: the data model is simple; the scoping key (client, tenant or owner id) is present in every table the policy covers, which in practice means composite primary keys led by that key; and no all-powerful administrator role must read or write across scopes (MD-01). Where it is used: backend checks are kept (L128) and the mechanics of L310, L311 and L566 apply (non-owner request role, FORCE where the owner connects, context from the verified identity in a transaction-local setting, indexed policy columns, denial tested through the deployed role). Authorization stays a backend decision with per-role privileges as the second gate (GUARD.3).
- **Tension (MD-01 against evidence)**: L619 and L688 favour row security exactly when several applications or agents read the database, which MD-03 makes the default; L310 records that the sources do not settle row security against application-side filtering. MD-01 decides it. The residual risk and its mitigation are in GUARD.3 (Q1). The review's recommendation (F1) is replaced by MD-01.
- **Rejected**: P1 and P3 as defaults; they win under MD-01's three conditions. P2's condition fires in the default but is overridden by MD-01.
- **Placement**: authority **Python backends** per user; **Postgres** per role. Forbidden: row security by default; row security replacing backend checks; a request role that owns tables or bypasses policies. Moved by: MD-01's three conditions.
- **State**: `known: MD-01 | conflict: L619, L688 favour row security when several consumers share the database (MD-03 default)`.
- **Changed (R1)**: decided by MD-01; former Q1 closed (F1).

## PIG-WEB.ALLOCATION.JOB_HOST Job and Schedule Host

- **Positions**: P1 queue table in Postgres, SKIP LOCKED (L126, L413); P2 staged in Postgres, drained to a broker (L126, L409); P3 broker from the start (L126, L408); P4 schedules inside Postgres (L604 MAINT).
- **Forces**: changeability (one component fewer) and correctness (job atomic with data) against scalability.
- **Decision**:
  - Jobs with Python logic or foreign effects: a queue table in Postgres, written by the database function in the same transaction as the data change and claimed by Python workers with FOR UPDATE SKIP LOCKED (L126, L413, L409; MD-03).
  - Scheduled pure data work: a Postgres scheduler extension calling named functions (L604, MAINT, max).
  - A schedule that needs Python inserts a job row for the workers (inferred).
  - Jobs are short, idempotent and monitored whatever the host (L605, L410).
- **Rejected**: P3: wins at measured lock contention, backlog or multi-server fan-out; then P2, never an enqueue outside the data transaction (L409).
- **Placement**: authority **Postgres** (queue and data schedules); **Python workers** execute. Forbidden: enqueuing to a broker outside the data transaction. Moved by: job volume, lock contention, multi-server fan-out.
- **State**: `known | unvalidated: the contention threshold is open (L126)`.

## PIG-WEB.ALLOCATION.CACHE_STORE Cache Store

- **Positions**: P1 shared cache service, Redis or Memcached (L417); P2 Postgres cache tables, UNLOGGED for rebuildable data (L534 MAINT, L420).
- **Forces**: latency against correctness (atomic invalidation) and changeability.
- **Decision** (F7):
  - Derived-data caches: Postgres tables, invalidated in the source transaction (L534, MAINT, max).
  - Response and fragment caches shared by processes: Postgres by default under POSTGRES_FIRST, UNLOGGED when rebuildable (L125, L420; inferred, no doctrine row covers them: the ledger's note on L534 sets L417 and L420 apart).
  - Per-process memory is never shared beyond one request; a cache is never permanent storage (L417).
- **Rejected**: P1: wins when measured cache latency or cache load on the primary demands it, or for ephemeral cross-process state the framework requires there.
- **Placement**: authority **source data**; cache store **Postgres**. Forbidden: per-process memory caches in multi-process production; caches as permanent storage. Moved by: number of processes, atomic invalidation need, measured hit latency.
- **State**: `known | unvalidated: response caches in Postgres rest on L125, not on doctrine; hit latency not measured`.
- **Changed (R1)**: L534 limited to derived data (F7).

## PIG-WEB.ALLOCATION.JS_SERVER JavaScript Server Tier

- **Positions**: P1 request-time JavaScript server (L288, L290); P2 Python renders HTML (L288, L252, L629); P3 build-time rendering (L288, L285).
- **Forces**: changeability (one server language) against latency.
- **Decision**: no request-time JavaScript server in the default. Python renders HTML (P2, following PRESENT.1); build-time rendering serves pages whose URL set is known (P3, L285).
- **Rejected**: P1: wins when PRESENT.1 picks a client-rendered application for most of the product and first load or crawlability needs server rendering (L290); its operating cost is unweighed (open).
- **Placement**: authority **Python backend** for HTML. Forbidden: a second request-time server runtime without that condition. Moved by: SEO and first-load needs, team JavaScript skill, the rendering placement.
- **State**: `known | gap: no source weighs the extra tier's operational cost (L288)`.
