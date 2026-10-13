# J5 web-app-philosophy TRANSVERSE: judge records

One judge record per node of the TRANSVERSE branch of `web-app-philosophy` (14 nodes), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves its purpose; weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. MAINT rows (source MAINT-S01) weigh as a strong position. The maintainer's decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points and are cited by id. The allocation verdicts (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled: these nodes realize them and re-decide no placement. Summary at three levels: `result.md`; questions: `questions.md`.

Pinned:
- Nodes judged: 14 of 14 (web-app-philosophy TRANSVERSE; 3 roll-ups judged from their children: TRANSVERSE, TRANSVERSE.OPERABILITY, TRANSVERSE.EVOLUTION).
- Decided 14, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: TRANSVERSE.SECURITY and TRANSVERSE.OPERABILITY.2. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 0.
- Verdicts against the maintainer doctrine: 0 counted here. TRANSVERSE.CONTRACTS realizes the L517 narrowing, counted once at its owner, PIG-WEB.DATA.INTERFACE.1 (J6): "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (L047). L517's coordination with every consumer and its "no formal version numbers" are kept; the new function name that carries the change is the expand step, the route the maintainer's own L512 already takes for stored contract schemas.
- Conflicts with J1 placements: 0. L098 read against ACT.4: business data changes stay out of the security event log (the business history is the database's, L049); security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events.
- Tensions recorded, not overridden: (a) EVOLUTION.3: several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need; L116's separate data schemas become domain schemas in the shared database (L513); L044 stays as J1 rejected it. (b) EVOLUTION.5: L068 (no teams by layer) against L515's database owner: each capability team owns its domain schema and its functions; a cross-schema business function belongs to the team that owns the workflow, reviewed by one named owner role (inferred). (c) OPERABILITY.2: L042's in-memory testing advantage is lost for the logic MD-03 puts in the database; those tests run on the real engine, rolled back by default, and behaviour that only shows at commit or between sessions is tested with committing sessions in a disposable database, never a shared one (L399, L400, L567).
- Gaps in the evidence: (1) PERFORMANCE owns one row and no row measures server or database time: whole-path measurement inferred (L095, L376, L382). (2) OPERABILITY.1: carrying the correlation id into the database transaction and audit rows inferred (L371, L566, L658). (3) OPERABILITY.2: no ledger row on concurrency testing; the concurrency tests themselves are required (inferred from GUARD.2), part of the default suite. (4) SECURITY: L303's tier map is inferred and assigns 7 of 10 categories; A06, A08 and A10 are assigned here, inferred, A06 and A08 corrected against the OWASP Top 10:2025 text; the ASVS chapter list (L304) is not read, its level definitions are. (5) The 3 roll-ups own no row.
- Review fixes: 9 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, m1, m4, m5, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

## How to read

- **Rows**: ledger rows the node owns, read in full; rows owned elsewhere are cited as positions or grounds (ownership says where a row is judged, not the only place it is read).
- **Positions**: P1.. with ledger ids. **Forces**: what each serves, at what cost. **Decision**: the max choice and its grounds. **Rejected**: each other position, why, and the condition under which it wins.
- **Placements realized**: the intentlinks of the skeleton for this node, then the J1 placements the decision rests on (cited, not re-decided).
- **State**: proposed `epistemic_state`, in J1's notation: `known`; `known | unvalidated: X` (X inferred); `| conflict:` (disagreement with a MAINT row, a research row or a maintainer decision); `| gap:` (missing evidence); `| undecided: awaiting maintainer, X` (a clause of a decided node that waits on an open maintainer question; the token is the same in every unit, so the graph builder finds every node the answer changes).
- **Review fixes**: each record changed by the TRANSVERSE review (`../review_transverse/review.md`) or by the cross-branch resolutions (`../cross_branch_fixes.md`) ends with a **Review fixes** line naming the finding ids.
- Default context throughout: MD-03 as restated by J1 (a classic website, one team, JavaScript + Python + Postgres, single tenant, humans and agents as users, the database shared by several backends and by BI and reporting, admin consoles and scripts, each with its own role).

## TRANSVERSE Transverse Concerns

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its five children. Each property that spans every tier is stated once, here, and designed in across browser, backend, database and every other database consumer, not added per tier (L096). Each is turned into an automated check where one exists (fitness functions, L110): the interface drift gate (MD-02), the function-API catalogue diff (RECORD.3), page budgets, module-boundary checks, tests at every tier. Tier branches realize these properties and do not restate them; the stack choices sit in `pig-web-defaults` under PIG-WEB.TRANSVERSE.
- **Children's claims**: security is a set of verifiable properties, each threat owned by a tier the requester cannot modify, insecure design answered by a threat model per placement and critical flow; performance truth is field measurement, correlated down the path; every contract is an explicit artifact that evolves by expand, migrate, contract; the system is observed, tested and delivered as one whole, tests isolated by rollback by default and commit-time and concurrent behaviour tested in a disposable database; it evolves through recorded decisions, small increments, each backend one deployable not split without a measured need, few mature technologies, and teams cut by capability.
- **Placements realized**: through its children (RULES.3, FORCES.3, FORCES.4, RECORD.3, ACT.4).
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: children's claims updated after M2, M3 (X5) and M4.

## TRANSVERSE.SECURITY Security Across Tiers

- **Rows**: L029, L030, L035, L036, L303.
- **Positions**:
  - P1 whole-site HTTPS, never mixed with HTTP in a session, HSTS (L029); HTTPS as the precondition for browser capabilities (L030).
  - P2 minimal exposure: a visit is safe, only the data the user's goal needs is collected (L035); secrets, session ids, tokens, keys, payment data, connection strings and unneeded personal data never logged, pseudonymised where identity is not needed, logged input sanitised (L036).
  - P3 the OWASP Top 10:2025 as an awareness map, each category assigned to an owning tier (L303; tier map inferred, SRC-115 does not state it).
  - P4 a catalogue of verifiable requirements (ASVS) at a level chosen by risk (L304, owned by PIG-WEB.TRANSVERSE.SECURITY.1; its level definitions are now read from the ASVS 5.0 text, its chapter list is not).
- **Forces**: P1 and P2 serve confidentiality and integrity at a low, one-off cost; no position in the evidence opposes them. P3 serves coverage (no threat without an owner); its cost is that an awareness list is not testable. P4 serves verifiability; its cost is effort scaled by the chosen level.
- **Decision**: P1, P2, and P3 completed by P4's demand.
  - Transport: every page and every API over HTTPS with HSTS, no mixed content (L029, L030). Database connections from every consumer role are covered by the same property (inferred: MD-03 adds consumers outside the request path).
  - Exposure: collect the minimum (L035); log no secret or unneeded personal data (L036), trace headers included (L375). The reporting role's column grants exclude personal data by default (J1 access paths), which realizes L035 for the MD-03 consumers.
  - Threat map: every Top 10 category has an owning tier that the requester cannot modify (RULES.3, L019), named through the allocation placements:
    - A01 Broken Access Control: backend and database, as GUARD.3 settles it: writer functions decide per-user write rules; the backend decides product policy and identity; the database bounds each consumer by its role (MD-01, MD-03). **Undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database** (not settled here). Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. Database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Consequence: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted; no statement here claims a stronger visibility guarantee.
    - A04 Cryptographic Failures: the backend (GUARD.4; L303), the proxy's TLS, the database connections of every consumer role, and storage at rest (the review's completion of L303's backend-only assignment; inferred).
    - A07 Authentication Failures: backend (GUARD.4; L303).
    - A05 Injection: backend and database (L303): parsing into precise types at every entry and typed function parameters (GUARD.1).
    - A02 Security Misconfiguration: headers, CSP and deployment; A03 Supply Chain: the pipeline and dependencies (L303; realized in PIG-WEB.TRANSVERSE.SECURITY and OPERABILITY.3).
    - A09 Logging and Alerting Failures: operations (L303), realized in OPERABILITY.1.
    - Assigned here, inferred:
      - A06 Insecure Design: a threat model per placement and per critical flow (authentication, access control, business operations, agent access), with misuse-case tests per tier; OPERABILITY.2's denial tests are their first instance. The allocation records (EVOLUTION.1) are the model's input, not the model. Grounded in the OWASP Top 10:2025 A06 preventions (threat modelling for authentication, access control, business logic and key flows; use-case and misuse-case tests per tier), read by the review.
      - A08 Software or Data Integrity Failures: the delivery pipeline (signed provenance, trusted sources, review of code and configuration changes, segregated CI/CD; one immutable artifact, L101; realized in PIG-WEB.TRANSVERSE.SECURITY.5) and the parsing tier for untrusted serialized input (GUARD.1). The OWASP 2025 category is untrusted code or data treated as trusted; the database's declarative constraints are not an A08 control and are not assigned here.
      - A10 Mishandling of Exceptional Conditions: the tier that holds each check, which fails closed (inferred from RULES.3).
  - Verifiability (max): each property is stated as a verifiable requirement at a level chosen by risk, with requirement ids traceable; the catalogue is a stack choice (P4, PIG-WEB.TRANSVERSE.SECURITY.1). Its level definitions are grounded: ASVS 5.0 says most applications should strive for Level 2, and each organisation decides its level from its risks. The Top 10 stays the awareness map, not the requirement set.
- **Rejected**:
  - HTTPS only on login or sensitive pages: never (L029).
  - Logging raw identifiers or secrets for debugging: never; a hashed session id is acceptable when sessions must be tracked (L036).
  - The Top 10 as the requirement set or a compliance checklist: it is an awareness document (L303); wins never as the only catalogue.
  - Security as a per-tier add-on without an owning tier per threat: against RULES.3 and L096.
  - The recorded allocation decisions as the answer to insecure design: they are the threat model's input; OWASP's A06 asks for threat modelling and misuse-case tests. Wins never as the whole answer.
- **Placements realized**: refines RULES.3 (skeleton link). Rests on GUARD.1, GUARD.3, GUARD.4, GUARD.2, ACT.4 and the J1 access paths.
- **State**: `known | unvalidated: the whole tier map, L303's 7 categories and the 3 added here (A06, A08, A10), A04 completed | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **Review fixes**: M4 (A08 reassigned to the pipeline and the parsing tier, declarative constraints dropped; A06 as a threat model with misuse-case tests; A04 completed; whole map unvalidated); m1 (ASVS level definitions grounded, L304's level part no longer open); m7 and X1 (one notation for the pending clause, recorded default, fallback and consequence stated).

## TRANSVERSE.PERFORMANCE Measured Performance

- **Rows**: L015.
- **Positions**:
  - P1 field (real-user) measurement at the 75th percentile, split by mobile and desktop, as the truth that sets priorities; lab tools test changes before release and find opportunities (L015; L381 for percentiles over averages).
  - P2 lab budgets enforced in the build (L296, owned by PIG-WEB.TRANSVERSE.PERFORMANCE).
  - P3 optimise only after measurement has found the critical path (L097, owned by FORCES.3; J1 verdict).
- **Forces**: P1 serves truth about what users experience (latency, FORCES.4); its cost is that field data arrives only after release and needs traffic. P2 serves prevention before release; its cost is that lab conditions miss real devices and cannot measure INP (L015). P3 serves effort.
- **Decision**: P1 is the truth, P2 the gate, P3 the discipline.
  - User-perceived performance is judged on field data at the 75th percentile, segmented by device class (L015, L381); it sets the priorities and feeds the allocation forces: a performance-driven copy needs a measurement that names the path (RULES.2, L607; FORCES.3); round trips are budgeted against FORCES.4.
  - Lab budgets in the build gate each change (L296, a fitness function in the sense of L110) and never override field data.
  - Whole path (max, inferred): field page metrics are joined, through the correlation id, to server timing and to database time per request (L095, L376, L382). The reason is the default context: the per-request work MD-03 places in database functions is invisible to page metrics alone.
- **Rejected**:
  - Lab-only measurement: never the truth (cannot measure INP, L015). It is acceptable as the primary source before launch, or when traffic is too low for a stable 75th percentile (condition inferred).
  - Averages: never (L381).
  - Optimising up front: never (L097; J1 FORCES.3).
- **Placements realized**: dataflow to FORCES.3 and FORCES.4 (skeleton links). Rests on RULES.2 (L607).
- **State**: `known | unvalidated: whole-path join to server and database time | gap: owns one row; no row measures server or database time`.

## TRANSVERSE.CONTRACTS Standards and Contracts

- **Rows**: L056, L057, L058, L483, L487.
- **Scope**: what every contract shares. The contracts of the default context are the database function API (offered to several backends, consoles and scripts; RECORD.2, realized under PIG-WEB.DATA.INTERFACE), the grants and meaning of tables BI reads, and the backend's HTTP interface (to its browser code, which runs at an older version for days, L009, and to agents; LOGIC.EXPOSE).
- **Positions**:
  - P1 an explicit artifact stating structure and meaning (names, types, nullability, units, invariants, owner, version), readable without the producer's code (L483; L562 and L565 at stack level).
  - P2 evolve by compatible additions; versioning is the exception (L056); readers tolerant, writers conservative (L057); before changing or removing a behaviour, find how it is used (L058).
  - P3 the provider contract is singular and authoritative; consumer contracts are partial and plural, and the one that matters for change is the union of what consumers use; consumer-driven contracts fit a closed community (L487).
  - P4 a breaking change is coordinated with every consuming team and **deployed together**, with no formal version numbers (L517, MAINT, for the function API).
  - P5 a breaking change goes expand (support old and new), migrate (move every client), contract (remove the old), so each phase can be released, verified and rolled back (L047, owned by DATA.MAINTAIN, grounded); for HTTP, removal is announced with machine-readable signals and a support window (L275, L277).
- **Forces**: P1 serves correctness across tiers and readers outside the producer, at the cost of writing meaning down. P2 serves independent upgrade of components at different times (L056); its cost is carrying old shapes for a while. P3 serves conceptual integrity; consumer-driven tests make hidden coupling explicit at the cost of a shared channel between teams (L487). P4 serves simplicity (one shape at any time, no version bookkeeping); it costs a window of breakage, since no deployment across separate deployables is atomic (L009). P5 serves the same independence as P2 for the unavoidable break; it costs a period with two shapes.
- **Decision**: P1, P2, P3 and P5; P4's coordination kept, its "deployed together" replaced.
  - Every contract is an explicit artifact with structure and meaning, readable without the producer's code (L483). Its origin is the one RECORD.3 names: the database schema for stored facts and for the function API (documentation generated from the live database, L474); the project's recorded origin for interface-only facts, kept always in sync by a CI gate that fails on drift (MD-02).
  - "Always in sync by process" and the compatibility window apply to every interface description consumers read: the HTTP description, the database function API catalogue, and the agent tool surface (for example an MCP server's tool list and schemas) (MD-02, X7).
  - The provider's contract is authoritative (L487): the database owner's for the function API (L515), the backend's for HTTP.
  - Changes are additive by default (L056); readers are tolerant (L057). Before a change or removal, usage is known, not assumed (L058). Under MD-03 every database consumer has its own role, so usage can be read per consumer: from its grants, and from the session role that audit records on every write (ACT.4). Inferred; how reads are counted per role is open.
  - **A breaking change to any contract goes expand, migrate, contract** (L047). For the function API: the new function or signature is added beside the old, each consumer moves, and the old one is removed once no consumer role calls it. The new name is the expand step, and it carries the change, so no formal version number is needed: "no formal version numbers" is L517's rule, the new name is the expand phase (L047) and the route the maintainer's own L512 takes for stored contract schemas (new named version, old one soft-deleted, consumers migrate gradually). The coordination with every consumer that L517 demands is kept.
  - "Deployed together" (L517) stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract (X2).
  - Grounds for expand, migrate, contract as the default: the database, several backends, BI reports and scripts deploy separately (MD-03), and backends roll out instance by instance. A browser tab keeps old code for days (L009, L278). There is usually a window in which old and new meet.
  - Counting: this is the L517 narrowing, realized here and counted once at its owner, PIG-WEB.DATA.INTERFACE.1 (J6). It is narrower than "against the doctrine" suggests, since L512 already takes this route for stored contract schemas.
  - Consumer-driven contract tests where consumers are separate teams in a closed community (L487); for the single team's own browser client, whether they add value beyond schema checks stays with the stack judge (L560, contested, PIG-WEB.TRANSVERSE.CONTRACTS.1).
- **Rejected**:
  - P4 lockstep ("deployed together") for a breaking change: acceptable only when every consumer of the changed object ships in the same deployment as the migration (X2). This is never the case for HTTP contracts with browser clients, whose open tabs are consumers that do not ship with the deployment (L009), or for contracts BI reports or scripts read.
  - Versioning as the routine way to change (version per release): versioning is the exception (L056); when a break is unavoidable, the version sits in one agreed place (L276, stack level).
  - Removing behaviour on the assumption that nobody uses it: never (L058).
  - Consumer-driven contracts as the authority: they are partial views (L487); acceptable as tests, never as the origin.
- **Placements realized**: requires RECORD.3 (skeleton link); required by INTERACTION.ENVIRONMENT.3 (version skew). Rests on RECORD.2 (function API as the default contract, MD-03) and MD-02. J1's RECORD.3 gate lets a function-API break through when it is marked as coordinated; this record fills in what that mark requires (the expand, migrate, contract sequence, or the lockstep condition above). No placement is changed.
- **State**: `known | conflict: L517 (MAINT) "deployed together", narrowed to the same-deployment condition, otherwise expand, migrate, contract (L047); counted at PIG-WEB.DATA.INTERFACE.1 | unvalidated: usage known per consumer role`.
- **Review fixes**: M1 and X2 (one lockstep condition, word for word; the departure cited here and counted once at its owner; the new name credited to the expand step and L512, not to L517; L512 noted as already taking this route); X7 (sync and compatibility window extended to every interface description, the agent tool surface included).

## TRANSVERSE.OPERABILITY Operability

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its three children. The running system is observed, tested and delivered as one whole across browser, backend, database and the other database consumers, designed in from the start (L096):
  - one correlation id runs from the browser to the database transaction; a separate security event log and a retention decision per record type;
  - tests at the lowest level that catches each failure, the database tier tested on the real engine, isolated by rollback by default, with commit-time and concurrent behaviour tested in a disposable database;
  - one immutable build promoted everywhere, database changes inside the same pipeline.
- **Placements realized**: through its children (ACT.4).
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: test line updated after M2 (X4).

## TRANSVERSE.OPERABILITY.1 Whole-Path Observability

- **Rows**: L048, L095, L096, L098.
- **Positions**:
  - P1 logs, metrics and traces are one system's signals, designed to be correlated (L095), across browser, server and database (L096; inferred synthesis).
  - P2 always log validation failures, authentication successes and failures, authorization failures, session failures, application errors and use of higher-risk functions; data-change events are optional extras (L098).
  - P3 retention is a recorded decision set by legal, regulatory and contractual obligations: no shorter, no longer (L048).
  - Read against ACT.4 (J1): business history is mandatory, written by database triggers in the same transaction, and kept apart from the security event log (L049, L392).
- **Forces**: P1 serves diagnosis across tiers; its cost is propagating context everywhere. P2 serves detection of attacks. P3 serves accountability and privacy (L035) against the convenience of keeping everything.
- **Decision**: P1, P2 and P3, with the two records apart.
  - One correlation id per user interaction, carried from the browser through the backend into the database transaction. It is stamped on every log record, span and client event (L371, L382), and on audit rows (L658 requires a correlation id for agent actions). Carrying it into the transaction alongside the actor (L566's transaction-local settings) is inferred; it reaches the work MD-03 places in database functions.
  - Database consumers outside the request path are part of the path: operator and owner sessions carry their identity and ticket id (L545; J1 access paths).
  - The security event log records P2's list (L098) and is a separate record with its own store, integrity and retention (L049, L392). Business data changes stay out of it: the business audit trail is the database's (ACT.4). Security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events: they are data changes that L098 lists as "use of higher-risk functionality". L098's "optional" applies to the security log only, so there is no conflict with ACT.4.
  - Retention is a recorded decision per record type (application logs, traces, security event log, audit trail), set by obligations, no shorter and no longer (L048). Where no obligation exists, the decision still has to be recorded; the period is set per project (open, by design).
  - Nothing secret or unneeded and personal is logged or placed in trace context (L036, L375).
- **Rejected**:
  - Per-tier silos of logs, metrics and traces: never (L095).
  - Data-change events in the security log as the business history: forbidden by ACT.4 (application-only audit).
  - Keeping logs indefinitely "in case": against L048 and L035; acceptable never without a recorded obligation.
- **Placements realized**: conflicts ACT.4 (skeleton link: the security event log and the business audit trail are kept apart). Rests on ACT.4's actor and role recording (J1 R1-3).
- **State**: `known | unvalidated: correlation id carried into the database transaction and audit rows (L371, L566, L658)`.
- **Review fixes**: m4 (only business data changes stay out of the security log; security-relevant changes are security events).

## TRANSVERSE.OPERABILITY.2 Proportioned Testing

- **Rows**: L099.
- **Positions**:
  - P1 a pyramid: many small fast tests, some coarser, very few high-level; ratios team-specific (L099).
  - P2 if high-level tests are fast, reliable and cheap, fewer low-level tests are needed (Fowler, SRC-198, noted in L099).
  - P3 test at the lowest level that can catch the failure; when a high-level test finds a bug, add the low-level test (L396); end-to-end tests few, on critical journeys (L397).
  - P4 integration tests against a real engine of the production kind, never mocks or another engine (L399); a disposable database, each test isolated (L400); a test that mutates shared data runs in a boundary that never commits (L567, MAINT).
  - Read against FORCES.6 (J1): logic in the application tests in memory; logic in the database needs a database to test (L042, L472 MAINT).
- **Forces**: P1 and P3 serve fast, precise feedback; their cost is many tests to write. P2 serves fewer tests when tooling allows; it fails when high-level tests are slow or flaky (L397). P4 serves fidelity (the constraints, isolation and functions are the real ones); its cost is a running database in every test run.
- **Decision**: P3 as the rule, P1 as its usual result, P4 for every test that touches data.
  - Proportion follows "the lowest level that catches the failure" (L396). The pyramid is what that rule usually yields (L099); ratios are not prescribed.
  - In the MD-03 default the database holds the business operations, the writer functions, the invariants and the audit. Their low-level tests run on the real engine of the production kind (L399). Each test is isolated: a rolled-back transaction by default (L400 gives it as its example). Logic tests on shared data run in never-committing transactions (L567). Behaviour that only shows at commit or between sessions (serialization failures and retries, lock waits, deferred constraints, the outbox) is tested with concurrent committing sessions in a disposable database, never a shared one (L567 governs shared environments; X4). They cover constraints, writer functions, the actor pairing and the refusal of writes without an actor (ACT.4).
  - Every invariant that GUARD.2 enforces procedurally, under Serializable with retry or under a lock, has a concurrent test. These concurrency tests are part of the default test suite, not a gap (inferred from GUARD.2: a placement whose correctness depends on concurrent behaviour needs a test of that behaviour).
  - Backend product policy and request parsing are tested in memory (L042).
  - Authorization is tested by denial: each role and actor is refused what it may not do (GUARD.3); these denial tests are the first misuse-case tests the threat model asks for (SECURITY, A06). **Undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database** (not settled here). Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. Database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. The denial suite does not cover roles that may SELECT the base tables (reporting, operator): they see every row, comments included, unless their own role is restricted.
  - Contract tests at the seams (stack judge); a few end-to-end tests on critical journeys (L397).
- **Rejected**:
  - P2 as the default: acceptable when high-level tests are measured fast, reliable and cheap (L099's note).
  - A fixed ratio (for example 70/20/10) as a rule: ratios are team-specific (L099).
  - Mocking the database, or another engine, for logic placed in the database: never (L399, L103). In-memory tests stay for logic the backend owns.
  - End-to-end-heavy suites: never as the default (L397).
- **Placements realized**: no skeleton link to a placement; rests on FORCES.6 (L042, L472), GUARD.2, GUARD.3, ACT.1 and ACT.4, whose database realizations it tests.
- **State**: `known | unvalidated: concurrency tests required by GUARD.2 | gap: no row on concurrency testing | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **Review fixes**: M2 and X4 (each test isolated, rollback by default; commit-time and concurrent behaviour tested with committing sessions in a disposable database; concurrency tests required by GUARD.2 in the default suite; the gap kept only for the missing source row); m7 and X1 (pending clause added to the state, one notation, default, fallback and consequence stated).

## TRANSVERSE.OPERABILITY.3 Reproducible Delivery

- **Rows**: L100, L101, L102, L103, L104.
- **Positions** (no competing position in the evidence; all consensus):
  - one codebase in version control, many deploys; shared code becomes a library (L100);
  - build, release, run strictly separate; build once, assets included, promote the same immutable artifact everywhere (L101);
  - configuration apart from code, secrets out of source (L102);
  - environments as similar as possible, same database engine and version, no adapters hiding differences (L103);
  - small, frequent releases (L104).
- **Forces**: reproducibility and safe change, at the cost of pipeline and environment work. No force in the evidence opposes them.
- **Decision**: all five, extended to the database tier.
  - Schema and function-API changes are versioned migrations in version control (L519, MAINT), promoted through the same environments as the code. They run once per release before the new code starts (L405), additive across the release window (CONTRACTS: expand, migrate, contract).
  - Under MD-03 the database's schema and function API have one owner (L515). Treating them as their own codebase, with the backends' typed wrappers generated from its catalogue in CI (RECORD.3, TYPE_CHAIN), is inferred from L100 ("one codebase per app").
  - Every environment runs Postgres at the production version (L103), which OPERABILITY.2's tests need.
- **Rejected**: rebuilding per environment, mutating a release, secrets in the repository, a different engine in development or test, large infrequent releases. None wins in this context.
- **Placements realized**: no skeleton link to a placement; rests on RECORD.2 and RECORD.3 (generated wrappers, catalogue diff in CI).
- **State**: `known | unvalidated: the database's schema and function API as their own codebase; migrations before code within the release window`.

## TRANSVERSE.EVOLUTION Deliberate Evolution

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its five children:
  - the costly decisions are named, chosen from the properties they must induce, and recorded;
  - the system grows in small tested increments without speculative features, its fit checked automatically;
  - several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need, and a split happens only for independent deployability on proven boundaries;
  - it adopts few mature technologies, a new one only past a measured limit;
  - teams are cut by capability, and structure follows them; a cross-schema business function belongs to the team that owns the workflow.
- **Placements realized**: through its children (RECORD.1, RECORD.2, POSTGRES_FIRST in the stack graph).
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: deployable line replaced after M3 (X5); ownership line after m5.

## TRANSVERSE.EVOLUTION.1 Explicit Decisions

- **Rows**: L105, L106.
- **Positions**:
  - P1 architecture is the shared understanding of the decisions that are costly to get wrong; design effort goes there (L105).
  - P2 choose the properties first, then the constraints that induce them, and test proposed changes against those constraints (L106).
  - At stack level: one short decision record per architecturally significant decision, never edited once accepted, only superseded (L129 to L133, owned by PIG-WEB.TRANSVERSE.EVOLUTION.3).
  - Read with L073 (EVOLUTION.3): defer hard-to-reverse decisions until the product is understood.
- **Forces**: P1 and P2 serve getting the irreversible parts right; the cost is writing them down. L073 serves not fixing what is not yet known.
- **Decision**: P1 and P2, recorded, with their constraints checked automatically where possible.
  - The costly decisions are named early. The allocation placements are the first of them, decided from the forces (target hierarchy).
  - Each is decided when enough is known (L073) and recorded with its forces, its alternatives and the condition that would reverse it: the same form as the judge record and as J1's "would move it".
  - The per-project decisions the maintainer requires are recorded the same way: the interface origin direction with its criteria (MD-02); the adoption of row-level security under its three conditions (MD-01).
  - Changes are tested against the constraints the decision set, automatically where a check exists (L106, L110).
  - Identifying a decision early is not deciding it early: L073 governs the timing, P1 the attention.
- **Rejected**: decisions left implicit in code (against L105); deciding every hard-to-reverse choice up front (against L073). Neither wins in this context.
- **Placements realized**: no skeleton link to a placement; the allocation placements are its first application.
- **State**: `known`.

## TRANSVERSE.EVOLUTION.2 Incremental Change

- **Rows**: L107, L108, L109, L110, L111, L112.
- **Positions**:
  - P1 internal quality from the start; it pays back in weeks (L107).
  - P2 no capabilities for presumed future features, but investment in ease of change: tests, refactoring, continuous delivery (L108); build to learn, since about a third of presumed features improve their metric (L112, majority).
  - P3 prudent, deliberate debt only knowingly (L109).
  - P4 small increments, with "fit" made explicit as automated fitness functions, non-functional ones included (L110).
  - P5 design for about 10x growth, plan a rewrite before 100x; early parts may be sacrificial (L111, majority, one T2 source).
- **Forces**: P1, P2 and P4 serve changeability; P5 serves capacity headroom; P2 and P5 look opposed: build nothing for the future, versus design for growth.
- **Decision**: all five, with P2 and P5 split by object.
  - P2 governs features: none built for presumed needs.
  - P5 governs capacity: the design has headroom for about 10x the current load; reaching about 100x is planned as a rewrite of the part concerned, not anticipated in code. This is inferred: no source states the split; L108 and L111 address different objects.
  - Fit is automated (L110), and the checks already named are its realizations: the interface drift gate (MD-02), the function-API catalogue diff (RECORD.3), page budgets (L296), module-boundary checks (L123), the drift guard on denormalised data (L533, MAINT).
  - Debt is taken only as prudent, deliberate debt, recorded (L109; EVOLUTION.1).
  - Replacement happens at seams, never by big-bang rewrite (L119).
- **Rejected**: features built ahead of need (never, L108); trading quality for speed (rejected by L107); reckless debt (L109); a big-bang rewrite (L119).
- **Placements realized**: none in the skeleton.
- **State**: `known | unvalidated: features against capacity as the split between L108 and L111; L111 rests on one source`.

## TRANSVERSE.EVOLUTION.3 Deployable Boundaries

- **Rows**: L073, L074, L075, L076, L077, L078, L079, L080.
- **Positions**:
  - P1 one deployable first. Defer hard-to-reverse boundaries (L073), place service boundaries only once the domain is understood (L075), avoid distribution when possible (L076), integrate in a small team (L078). At stack level: L113 to L116, the four-source default.
  - P2 services from the start when the domain is well known, the system needs distribution, and the parts can develop and deploy independently (L117, Tilkov; contested).
  - P3 the goal of a split is independent deployability, not the count; start with one or two (L080); budget the distribution premium first (L074).
  - P4 bounded contexts with explicit mappings, not one unified model (L077).
  - P5 all advice here is tentative: the evidence is anecdotal, and a modular monolith does not make extraction free (L079).
  - Read against RECORD.1 and RECORD.2 (J1, MD-03): one shared system of record behind a function API. Also L044 (one application owns its database), rejected by J1 in this context, and L116 (keep separate data schemas for likely future services).
- **Forces**: P1 serves changeability while the domain is unknown and saves the distribution premium; P2 serves team independence when the domain is known; P3 and P4 serve keeping each split meaningful.
- **Decision**: P1 by default, P3 and P4 for any split, and the data seam given by the allocation.
  - Several backends may share the database (MD-03). Each backend is one deployable, modular by business concept (stack level); it is not split into services without a measured need (X5). MD-03's several backends do not by themselves license splitting a backend. A further deployable is split off only when a team needs independent releases, the boundary has proven stable, and the distribution premium is budgeted (L080, L074, L114).
  - Because the data seam is already the function API, a later split of a backend does not move data. Only deploy independence and the distribution premium of L074 remain to be weighed, so a split costs less than the research rows assume (inferred; L074 and L076 price a data split this context does not have).
  - Bounded contexts (L077) map to domain schemas in the shared database, each with its own functions and roles (L513, MAINT: schemas are business-domain namespaces with ownership and permissions). This is how L116's "separate data schemas for likely future services" is realized under MD-03; inferred.
  - A new deployable reaches the data through the function API with its own role (RECORD.2). It never writes tables beside it and never holds a second system of record (RECORD.1 forbids a consumer writing two stores).
  - The confidence of this verdict is bounded by L079: anecdotal evidence.
- **Rejected**:
  - P2 services-first: acceptable when all of these hold: the domain is well known (ideally a second version), the size requires distribution, the parts develop and deploy independently, and the team already runs distributed systems (L117, L115, L116).
  - A database per service: rejected in this context by RECORD.2 and MD-03. It wins only under J1's "would move it": a consumer outside the team that needs independent deploys gets that team's service interface.
- **Placements realized**: no skeleton link to a placement; rests on RECORD.1 and RECORD.2 (MD-03).
- **State**: `known | unvalidated: bounded contexts as domain schemas in the shared database; a later split moves no data | conflict: L044 and L116 (separate data per application or service) against MD-03, recorded by J1 and realized here`.
- **Review fixes**: M3 and X5 ("one backend deployable first" replaced by: several backends may share the database, each backend one deployable, not split into services without a measured need; the lower cost of a later split weighed, inferred).

## TRANSVERSE.EVOLUTION.4 Few Mature Technologies

- **Rows**: L081, L082, L083, L084, L085.
- **Positions**:
  - P1 novelty is a scarce budget, spent on what differentiates the product (L081).
  - P2 prefer mature technology with known failure modes (L082).
  - P3 few distinct technologies covering the domain (L083, majority).
  - P4 weigh perpetual operating cost, not adoption convenience; consult others before adopting (L084).
  - P5 simplicity is a reliability property (L085).
  - P6, from the skeleton's conflicts link to python-kb-philosophy POLYGLOT: pick the right paradigm per problem.
- **Forces**: P1 to P5 serve operability and reliability at the cost of sometimes using a less specialised tool; P6 serves fit per problem.
- **Decision**: P1 to P5.
  - The system adopts few, mature technologies. A new technology enters only when an existing one's measured limit is reached and its perpetual operating cost is budgeted (L084).
  - In this stack that is POSTGRES_FIRST: Postgres hosts queue, schedules, derived caches and sessions until a measured limit; CACHE_STORE and JOB_HOST follow the same rule.
  - P6 is reconciled by scope, inferred. EVOLUTION.4 counts runtimes, stores, services and frameworks. The choice of paradigm inside an adopted language (POLYGLOT) is not limited by it, so the two do not compete.
- **Rejected**: the best tool per problem across infrastructure, acceptable when the existing tool's measured limit is reached and the added operating cost is budgeted (L084; POSTGRES_FIRST's "would move it").
- **Placements realized**: no skeleton link to a philosophy placement; realized in the stack graph by PIG-WEB.ALLOCATION.POSTGRES_FIRST, CACHE_STORE and JOB_HOST (J1).
- **State**: `known | unvalidated: scope reconciliation with POLYGLOT`.

## TRANSVERSE.EVOLUTION.5 Team-Shaped Structure

- **Rows**: L068, L069.
- **Positions**:
  - P1 teams are not organised by layer; teams are cross-functional, around a capability (L068).
  - P2 structure copies communication; design team and module structure together (L069).
  - Read against L515 (MAINT): the function API's implementation belongs to the database owner, who can change it without redeploying consumers. A separate database team would be a team by layer.
- **Forces**: P1 and P2 serve delivery without hand-offs. L515 serves one owner for the shared data's integrity (MD-03).
- **Decision**: P1 and P2, with the database owner as a role, not a layer team.
  - Default context, one team: the team is cross-functional, and the database owner is a named role inside it.
  - When teams multiply: each capability team owns its domain schema, its functions and its backend (L513: schemas carry team ownership). One named owner role holds what spans schemas: conventions, roles and grants, review of the function API's catalogue diff (RECORD.3). Inferred.
  - Cross-domain business operations: one business operation is one database function call in its own transaction (J1 R1-4); backends never compose several calls into one operation. A database function may call another domain's published functions inside the same transaction, so composition across domains happens in the database. What is forbidden across domains is direct access to another domain's tables, not calling its published functions (X3).
  - Ownership of a cross-schema business function: the team that owns the workflow, reviewed by the owner role (inferred). This multi-team arrangement is the condition that refines RECORD.2's single "database owner"; in the default context (one team) the single owner of RECORD.2 holds.
  - Module and schema boundaries are cut with the team boundaries (L069; EVOLUTION.3).
- **Rejected**: teams by layer, a database team writing other teams' business operations (L068). Acceptable never in this context; an owner role for conventions is not a layer team.
- **Placements realized**: no skeleton link to a placement; rests on RECORD.2 (the database owner of the function API, L515).
- **State**: `known | unvalidated: ownership per domain schema when teams multiply; cross-schema business functions owned by the workflow's team`.
- **Review fixes**: m5 (owner of cross-schema business functions named; the multi-team arrangement marked as the condition that refines RECORD.2's single owner); B1 and X3 (composition across domains happens in the database; only direct access to another domain's tables is forbidden).
