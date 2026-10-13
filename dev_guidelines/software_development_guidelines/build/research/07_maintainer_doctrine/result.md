# Research result: maintainer doctrine on verification, delivery, operation, tooling and documentation (area MAINT)

All claims are the maintainer's own codified practice, restated stack-neutral where the doctrine's reasoning supports it. One non-citable source (MAINT-S01). The `agreement` and `vs common practice` fields are the slot's own reading from general knowledge, not from fetched sources: the later judge weighs them against public sources. Leads named under "public leads" are unread and are not citations.

## L1 headline

The maintainer's codified practice is a coherent, risk-graded doctrine of verification and change safety (undoable tests on real data, once-only immutable migrations, human-run production bulk work, designed staleness with monitoring, documentation kept as one durable explanation), strongest where changes are irreversible and data is large, and it departs from common practice on eleven points; certainty is grounded in the doctrine's own text, not checked against the running system or against public sources.

Pinned:
- Claims: 67, all from one source (MAINT-S01, the maintainer's codified practice, not citable); sources by tier: 0 T1, 0 T2, 0 T3, 0 T4, 1 maintainer source; 0 public fetches, so no failed T1 fetch.
- Claims per sibling area: SRC 0, ADOPT 6, VERIFY 20, DELIVER 23, OPERATE 7, TRANS 11.
- Contradicts common practice (11): MAINT-C01 tests on real shared data behind forced rollback, not isolated environments; MAINT-C24 forward-only with a written undo, not automatic down migrations; MAINT-C26 manual production gate and manual lane, not continuous deployment; MAINT-C30 registry content deployed by script, not through the migration pipeline; MAINT-C31 coordinated breaking changes, no version numbers; MAINT-C45 function with signature, not view, as the stable interface; MAINT-C46 custom cache tables, not the built-in materialized view; MAINT-C47 scheduler inside the data store, not a dedicated orchestrator; MAINT-C54 mandatory header and dated change log on every unit; MAINT-C64 environment differences routed, not dev/prod parity; MAINT-C66 design for probable future use, not YAGNI. Open, if confirmed: MAINT-C67 no automated regression run found.
- Contested topics (13): real-data tests versus isolation (C01); colocated versus separate tests (C06); written undo versus down migrations (C24); manual versus continuous production deploy (C26); script versus migration for registry content (C30); versioned versus coordinated interfaces (C31); function versus view interface (C45); built-in versus custom cache (C46); in-store scheduler versus orchestrator (C47); mandatory header versus self-documenting code (C54); guidelines induced versus deduced (C59); parity versus routed divergence (C64); future-proofing versus YAGNI (C66).
- Doctrine-internal disagreements: 10, listed in L2.

## L2 claims

Pinned:
- Claims: 67, all from one source (MAINT-S01, the maintainer's codified practice, not citable); sources by tier: 0 T1, 0 T2, 0 T3, 0 T4, 1 maintainer source; 0 public fetches, so no failed T1 fetch.
- Claims per sibling area: SRC 0, ADOPT 6, VERIFY 20, DELIVER 23, OPERATE 7, TRANS 11.
- Contradicts common practice (11): MAINT-C01 tests on real shared data behind forced rollback, not isolated environments; MAINT-C24 forward-only with a written undo, not automatic down migrations; MAINT-C26 manual production gate and manual lane, not continuous deployment; MAINT-C30 registry content deployed by script, not through the migration pipeline; MAINT-C31 coordinated breaking changes, no version numbers; MAINT-C45 function with signature, not view, as the stable interface; MAINT-C46 custom cache tables, not the built-in materialized view; MAINT-C47 scheduler inside the data store, not a dedicated orchestrator; MAINT-C54 mandatory header and dated change log on every unit; MAINT-C64 environment differences routed, not dev/prod parity; MAINT-C66 design for probable future use, not YAGNI. Open, if confirmed: MAINT-C67 no automated regression run found.
- Contested topics (13): real-data tests versus isolation (C01); colocated versus separate tests (C06); written undo versus down migrations (C24); manual versus continuous production deploy (C26); script versus migration for registry content (C30); versioned versus coordinated interfaces (C31); function versus view interface (C45); built-in versus custom cache (C46); in-store scheduler versus orchestrator (C47); mandatory header versus self-documenting code (C54); guidelines induced versus deduced (C59); parity versus routed divergence (C64); future-proofing versus YAGNI (C66).
- Doctrine-internal disagreements: 10, listed in L2.

Clusters (claim ids; every cluster: maintainer decision, grounded unless stated):

1. Tests run on real, curated data and are made harmless by construction: a guaranteed-undone boundary, shaping inside it, vehicle chosen by risk and by who runs it, self-reporting verdicts, tests beside the unit, test configuration isolated from production code. Departs from the isolated-environment norm. MAINT-C01, MAINT-C02, MAINT-C03, MAINT-C04, MAINT-C05, MAINT-C06, MAINT-C07, MAINT-C08, MAINT-C09.
2. Defects that survive review and deployment are a named class, answered by production-shaped data, input guards, an error-indexed pitfall catalog, empirical checks of unstated platform behaviour, explicit rules for silent limits, integrity where write paths converge, and an explicit opt-in for unbounded destruction. MAINT-C10, MAINT-C11, MAINT-C12, MAINT-C13, MAINT-C14, MAINT-C15, MAINT-C16.
3. Derived data and invariants stay true by a graded tool ladder with an up-front checklist, detection queries, self-auditing conventions, an observe-only-first runtime audit and a deployed-versus-source drift check. MAINT-C17, MAINT-C18, MAINT-C19, MAINT-C20, MAINT-C21.
4. Changes ship as ordered, once-only, immutable, ticket-tagged migrations with a written undo, idempotent DDL, an automatic/manual split by risk, a manual production step by authorized people, application deploys gated on schema version, CI on a data dump, backward-compatible interfaces coordinated rather than versioned, and forward-only convention evolution. Departs from continuous deployment, dev/prod parity and versioned interfaces. MAINT-C22, MAINT-C23, MAINT-C24, MAINT-C25, MAINT-C26, MAINT-C27, MAINT-C28, MAINT-C29, MAINT-C30, MAINT-C31, MAINT-C32.
5. Review uses the anti-pattern catalog by change type and escalates by risk (locks, duration, availability) to named senior approvers. Contains an internal staleness (see disagreements). MAINT-C33, MAINT-C34.
6. Very large one-off changes are a four-decision procedure: batching key, work list, fan-out, observe and recover, with per-batch idempotence, a convergence query as definition of done, ramped concurrency, a halt-on-first-failure first run, a preconditions checklist, statements tagged with their ticket, and the target system watched, not just the job. MAINT-C35, MAINT-C36, MAINT-C37, MAINT-C38, MAINT-C39, MAINT-C40, MAINT-C41, MAINT-C42, MAINT-C43.
7. Adoption: every new layer or moving part must earn its cost through a short list of strong reasons, with the costs recorded; interfaces with a signature are preferred to shape-bound ones; platform built-ins are passed over only for stated missing capabilities; scheduling lives next to the data with stated limits; core technology is chosen by problem fit. Departs from prefer-the-built-in and from dedicated orchestrators. MAINT-C44, MAINT-C45, MAINT-C46, MAINT-C47, MAINT-C48, MAINT-C60.
8. Operation: scheduled and derived work is monitored on four signals, staleness is a designed property with sync built before first use, errors name component and values with stable codes, jobs are tested by direct call and in a reduced mode, index health is watched. MAINT-C49, MAINT-C50, MAINT-C51, MAINT-C52, MAINT-C53.
9. Documentation and transverse practice: one durable explanation per unit, dated verification and honest open-defect records, derived artifacts never fed back into their source, a role-based router with size caps, layered detail and audience, guidelines induced from production practice with explicit evolution notes, least privilege at the lowest layer, agents on an enforced narrow path and writing but not running high-blast-radius scripts, environment differences routed rather than removed. MAINT-C54, MAINT-C55, MAINT-C56, MAINT-C57, MAINT-C58, MAINT-C59, MAINT-C61, MAINT-C62, MAINT-C63, MAINT-C64.
10. Process: structure before code with deliberate naming, and design for probable future use. Contested against incremental design. MAINT-C65, MAINT-C66.
11. Open: how and when tests run as a regression suite is unstated. MAINT-C67.

Live debates (forces in tension):
- Realistic shared data with rollback versus isolated disposable test environments: confidence in real shapes and cost of cloning versus isolation and blast radius (MAINT-C01, MAINT-C02).
- Manual production gate versus continuous deployment: reversibility and control versus delivery speed (MAINT-C26, MAINT-C27).
- Dev/prod parity versus accepting divergence with routed manual steps: reversibility and low ownership cost versus predictability (MAINT-C64).
- Coordinated breaking changes without version numbers versus versioned interfaces: cost of ownership versus control, winning with few in-house consumers (MAINT-C31).
- Function with signature versus view as the stable interface: change absorption versus simplicity (MAINT-C45).
- Custom cache tables versus built-in materialized views, in-database scheduler versus dedicated orchestrator: control and fit versus cost of ownership and exit risk (MAINT-C46, MAINT-C47).
- Design for probable future usage versus build only for today (YAGNI): reversibility and cost of schema change versus delivery speed (MAINT-C66).
- Mandatory docstring with dated change log versus self-documenting code and history in version control: cognitive load and durability versus duplication (MAINT-C54).
- Tests colocated with the unit versus a separate test tree: sync and discoverability versus tooling convention (MAINT-C06).

Candidate central decisions (others depend on them):
1. Where tests run and what makes them harmless: isolated environment, or real data inside a guaranteed-undone boundary (MAINT-C01, MAINT-C03).
2. How a change reaches production and which changes leave the automatic path (MAINT-C26, MAINT-C27).
3. How an interface that several consumers bind to evolves: version numbers, or backward-compatible plus coordination (MAINT-C31, MAINT-C45).
4. What a new layer must justify before it exists, and who records its costs (MAINT-C44, MAINT-C60).
5. How derived data stays correct: which rung of the sync ladder, with what staleness window and monitoring (MAINT-C17, MAINT-C49, MAINT-C50).
6. What automation and AI agents may execute versus only write (MAINT-C62, MAINT-C63).

Where the doctrine disagrees with itself:
- Test vehicle: the testing guideline reserves an interactive begin/rollback wrapper for humans and gives automation a single rolled-back block, while the fixtures guideline's "typical script" is a begin / set-local / rollback script, and its single-statement context cannot carry a transaction wrapper at all (MAINT-C03, MAINT-C08).
- Fixture lifetime: session-scoped fixtures are said to clean themselves at session end, and the same family of guidelines says to reset at the top of a re-runnable script because a failed run leaves stale values (pooled or long sessions never end) (MAINT-C08).
- Two delivery truths: functions and schema go through the migration history, but configuration-registry content is deployed by running an idempotent authoring script, with a migration only as an optional audit mirror (MAINT-C22, MAINT-C30).
- Environments: the migration guide has three (development, staging, production) and a flow with staging verification; the testing, bulk and tooling guides speak of two, and the production preconditions require only a development dry run (MAINT-C27, MAINT-C39).
- Always drop before create for functions versus create-or-replace for stability, with a drop-if-exists idempotence rule; a drop also discards grants and dependents (a general platform fact, not stated in the doctrine) (MAINT-C25).
- Predictive design (design for probable future usage, high normal form, no duplication) versus the schema guideline's "normalize until it hurts, denormalize until it works", "do not optimize prematurely", and rules induced from ten thousand observed queries (MAINT-C59, MAINT-C66).
- Strategy comments before tactics (philosophy) versus the comment discipline of one docstring plus at most about three lines of why-comments (MAINT-C54, MAINT-C65).
- The review rubric is stale against the modules it should reflect: the anti-pattern catalog recommends serial and simple keys and calls composite keys on unpartitioned tables a defect, while the design-principles guideline mandates identity columns and scope-leading composite keys (MAINT-C33).
- Documentation rots against its own rule: the indexes carry line counts and line-number TOCs that are stale when measured (function-design guideline listed at 215 lines, measured 403; query-style listed at 505, measured 622; anti-pattern module listed 260, measured 281), and the module table names do not match current file names (MAINT-C57).
- Dates in documents: the function docstring change log and the dated verification stamps are required, while the maintainer's workspace-wide documentation standard says no versions or dates in documents because version control tracks them (MAINT-C54, MAINT-C55).

What this slot did not cover: SQL formatting and query style (skipped as instructed); database design rules already entered by the earlier database slot (keys, deletion, JSON, bulk mechanics in domain terms) except where they carry a cross-cutting rule; CI configuration details beyond the pipeline's shape; the substance of the function-sync validator beyond its purpose; the whole architecture folder beyond the cost-gate, cache, scheduler, ownership and permission pages; web research (not needed).

## L3 full

Pinned:
- Claims: 67, all from one source (MAINT-S01, the maintainer's codified practice, not citable); sources by tier: 0 T1, 0 T2, 0 T3, 0 T4, 1 maintainer source; 0 public fetches, so no failed T1 fetch.
- Claims per sibling area: SRC 0, ADOPT 6, VERIFY 20, DELIVER 23, OPERATE 7, TRANS 11.
- Contradicts common practice (11): MAINT-C01 tests on real shared data behind forced rollback, not isolated environments; MAINT-C24 forward-only with a written undo, not automatic down migrations; MAINT-C26 manual production gate and manual lane, not continuous deployment; MAINT-C30 registry content deployed by script, not through the migration pipeline; MAINT-C31 coordinated breaking changes, no version numbers; MAINT-C45 function with signature, not view, as the stable interface; MAINT-C46 custom cache tables, not the built-in materialized view; MAINT-C47 scheduler inside the data store, not a dedicated orchestrator; MAINT-C54 mandatory header and dated change log on every unit; MAINT-C64 environment differences routed, not dev/prod parity; MAINT-C66 design for probable future use, not YAGNI. Open, if confirmed: MAINT-C67 no automated regression run found.
- Contested topics (13): real-data tests versus isolation (C01); colocated versus separate tests (C06); written undo versus down migrations (C24); manual versus continuous production deploy (C26); script versus migration for registry content (C30); versioned versus coordinated interfaces (C31); function versus view interface (C45); built-in versus custom cache (C46); in-store scheduler versus orchestrator (C47); mandatory header versus self-documenting code (C54); guidelines induced versus deduced (C59); parity versus routed divergence (C64); future-proofing versus YAGNI (C66).
- Doctrine-internal disagreements: 10, listed in L2.

### Source register

- MAINT-S01 (not citable, no tier): the maintainer's codified practice for a large production relational database platform: a set of guidelines (schema design, function design, function testing, SQL test scripts, bulk parallel execution, runtime pitfalls), architecture notes (cost-gate for a function API, denormalization and caches, scheduled jobs, permissions, write ownership), a migration and delivery guide, a deployed-versus-source validator readme, and a personal work-thinking philosophy. Authoritative on: what this maintainer requires in verification, delivery, operation, tooling choice and documentation, and why. URL read: none (private files, listed only in the private trace).

### Field notes

- `agreement`: slot's reading of public practice (consensus, majority or contested), inferred from general knowledge and unfetched.
- `vs common practice`: agrees, extends (adds something public practice lacks), or contradicts.
- `public leads` (unread, not citations): where the judge may look.
- `area`: sibling area the claim belongs to; `boundary:` marks a claim also touching another.

### Claims

**MAINT-C01** area VERIFY
- claim: A test run against shared or production-sized data must never leave a durable effect: it executes inside a boundary that is guaranteed to be undone, and any reshaping of data for the scenario happens inside that boundary and is never committed, on any environment.
- level: principle; stack: neutral; sources: MAINT-S01, function testing guideline (data shaping, anti-patterns); certainty: grounded
- agreement: contested; vs common practice: contradicts (the common norm is an isolated disposable environment per test run)
- positions: (a) isolated disposable environment per test run, strongest argument: no shared state, no risk to real data (testing literature, most test frameworks); serves isolation and speed of feedback; wins when the dataset is small or cloning is cheap. (b) the maintainer: real shapes exist only in real data and the dataset is too large to clone, so run on it behind a forced rollback; serves confidence (realism) and cost of ownership; wins when data is large, complex and its shapes cannot be synthesized, and the platform can undo every effect of a test.
- public leads: hermetic-test guidance (Software Engineering at Google, testing chapters); Fowler on test isolation.

**MAINT-C02** area VERIFY
- claim: Tests that need real data use a curated, catalogued set of real records selected by queryable compatibility attributes (task type, asset type, answer shape, state, volume); selection is the first test step; do not invent rows or pick arbitrary production rows; a persistent new shape is feature work done by a separate idempotent script, not by test code.
- level: decision; stack: neutral; sources: MAINT-S01, function testing guideline (test data decision); certainty: grounded
- agreement: majority; vs common practice: extends (curated real corpus catalogued by attributes; many teams use synthetic factories)
- positions: (a) synthetic fixtures or factories built per test, strongest argument: explicit, hermetic, self-describing tests; serves speed of feedback and isolation; wins when the domain is small and shapes are easy to construct. (b) curated real corpus: serves confidence; wins when shapes are rich and costly to fabricate. Related evidence: a defect that worked on low-valued keys failed on real ones (MAINT-C10).
- public leads: test data management literature; production-like test data in Humble and Farley.

**MAINT-C03** area VERIFY
- claim: Choose the test execution vehicle by risk and by who runs it: read-only tests run as plain queries with no wrapper; tests that can raise, break or mutate run, when automated, as one atomic unit that is rolled back; an interactive open-transaction wrapper is reserved for a human at the keyboard, because a dropped connection can leave an open transaction.
- level: decision; stack: neutral (the atomic-unit form is realized per platform, see MAINT-C04); sources: MAINT-S01, function testing guideline (execution vehicle by risk); certainty: grounded
- agreement: majority; vs common practice: extends (ties the vehicle to the runner's failure mode)
- positions: single atomic unit for automation serves reliability and cost of cleanup; an interactive wrapper serves readability and wins when a human supervises. Nothing under test needs a wrapper when it is read-only.
- public leads: none beyond general test-isolation guidance.

**MAINT-C04** area VERIFY
- claim: Where a block that completes normally commits its changes, a mutating test must end by raising an error whose message is the verdict, so that every outcome, pass or fail, rolls back.
- level: practice; stack: PostgreSQL anonymous blocks (stack-tagged pointer); sources: MAINT-S01, function testing guideline (forced rollback); certainty: grounded
- agreement: majority; vs common practice: extends (the platform-specific idiom for MAINT-C01)
- positions: none competing in the doctrine.
- public leads: PostgreSQL documentation on transaction semantics of blocks.

**MAINT-C05** area VERIFY
- claim: A test reports its own verdict in a fixed, searchable shape that carries unit and scenario identity ("unit>scenario: passed" or "FAILED, expected X, got Y"), so that a run's output is its own report.
- level: practice; stack: neutral; sources: MAINT-S01, function testing guideline (verdict channel); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: test-framework conventions.

**MAINT-C06** area VERIFY
- claim: Tests live beside the unit they test (at the bottom of its source file under a banner), one single-statement case each, so that each case runs through the platform's single-statement tooling and cannot drift from the unit.
- level: practice; stack: neutral in the colocation, the single-statement constraint comes from the tooling; sources: MAINT-S01, function testing guideline (where tests live); certainty: grounded
- agreement: contested; vs common practice: agrees in some ecosystems, differs in others
- positions: (a) colocated, strongest argument: tests and unit change together, discoverable; serves team cognitive load; wins when the tooling lacks a test tree. (b) separate mirrored test tree, strongest argument: clean production artifacts, test tooling support; serves isolation of concerns; wins when the language has a test runner.
- public leads: language-specific norms (doctests, Rust inline tests versus separate trees).

**MAINT-C07** area VERIFY
- claim: Test configuration lives in a namespace disjoint from production request context; production code must never read the test namespace; tests may write the production-context keys only to simulate a context.
- level: principle; stack: neutral; sources: MAINT-S01, SQL test scripts guideline (naming rule, anti-patterns); certainty: grounded
- agreement: consensus; vs common practice: agrees (test configuration must not leak into production paths)
- positions: none.
- public leads: Twelve-Factor config discipline.

**MAINT-C08** area VERIFY
- claim: Fixture values reused across the steps of a multi-statement test are set once at the top as named session-scoped variables, not hard-coded in every statement; in a re-runnable script reset them at the top, keep structured fixtures as JSON, and keep bulk fixtures in scratch tables, not in variables.
- level: practice; stack: PostgreSQL custom configuration parameters (stack-tagged pointer; mechanics: a dotted namespace is mandatory; a value set and read in the same statement is unreliable in single-statement contexts, so use the setter's return value; everything is text, cast at each read); sources: MAINT-S01, SQL test scripts guideline (all sections); certainty: grounded; empirical claim marked verified by the maintainer, not by this slot
- agreement: majority; vs common practice: extends
- positions: variables reduce duplication and let the unit under test read the fixture without a signature change (debug output inside the unit, no production impact); the cost is untyped text and a footgun in one-statement contexts; wins in clients without scripting meta-commands.
- public leads: PostgreSQL documentation on configuration settings.

**MAINT-C09** area VERIFY
- claim: Make mutations conditional on an actual change (add a predicate that skips rows already at the target value), so that re-runs behave identically, test shaping is no-op-safe, write volume and trigger executions drop.
- level: practice; stack: neutral (SQL form shown in the doctrine); sources: MAINT-S01, function design guideline (performance considerations), function testing guideline (data shaping); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: idempotent operation guidance (Humble and Farley on repeatable deployment).

**MAINT-C10** area VERIFY
- claim: Passing review and deployment is not evidence that code works: a class of defects survives both and fails at runtime on real data (name resolution deferred to execution, a branch taken only on rare data, a narrowing cast that is range-checked, an aggregate returning a wider type than its input, an array function fed null or a scalar). Exercise every branch with production-shaped data, and guard inputs whose absence of null is not guaranteed, always, not only where null seems possible.
- level: principle; stack: neutral (examples PostgreSQL); sources: MAINT-S01, runtime pitfalls guideline (all entries); certainty: grounded
- agreement: majority; vs common practice: extends (names the class and its remedy)
- positions: static analysis and types catch part of the class (serves speed of feedback); the maintainer's position is that they do not catch these, so tests on production-shaped data are required (serves correctness).
- public leads: testing pyramid (Fowler); Beck on test-driven development.

**MAINT-C11** area OPERATE
- claim: Keep a pitfall catalog indexed by error code or symptom, each entry with where it bit, the fix in order of preference, and a rule of thumb; read it before writing in the affected area and first when meeting an unfamiliar error; add an entry after any defect found twice.
- level: practice; stack: neutral; sources: MAINT-S01, runtime pitfalls guideline (header, entries); certainty: grounded
- agreement: majority; vs common practice: agrees (blameless postmortem knowledge capture), extends (indexed by the searchable symptom)
- positions: none.
- public leads: Google SRE postmortem culture.

**MAINT-C12** area VERIFY
- claim: Do not apply a blanket search-and-replace across a file that holds two syntactic contexts (for example production bodies and test blocks); anchor edits on context, and after any such change re-check the places the other context depends on.
- level: practice; stack: neutral; sources: MAINT-S01, runtime pitfalls guideline (statement-context entry); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: refactoring guidance (Fowler).

**MAINT-C13** area VERIFY
- claim: Where public documentation is unclear about a platform behaviour that a design relies on, verify it empirically on a live instance and record the finding with its scope (for example that sibling writes in one statement are invisible to each other, and that ordering is not visibility), and treat the claim as that environment's verified fact.
- level: principle; stack: neutral (examples PostgreSQL); sources: MAINT-S01, SQL test scripts guideline (footgun), write-ownership architecture note; certainty: grounded
- agreement: consensus; vs common practice: agrees (characterization tests)
- positions: none.
- public leads: Feathers on characterization tests.

**MAINT-C14** area VERIFY
- claim: When a platform silently truncates or coerces (for example identifiers over a byte limit), make the limit a hard rule with a check, because the failure is a collision or a mis-resolved reference with no error.
- level: practice; stack: PostgreSQL (stack-tagged pointer: names over 63 bytes are truncated silently); sources: MAINT-S01, function design guideline (identifier length); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: PostgreSQL documentation on identifiers.

**MAINT-C15** area VERIFY
- claim: Enforce integrity where all write paths converge (declared constraints, referential links, validation near the data), in addition to validation at the edge, because migrations, administrative tools and ad-hoc statements bypass application code; invalid states should be unrepresentable and fail fast with a clear error.
- level: principle; stack: neutral; sources: MAINT-S01, schema design principles, philosophy (integrity by design); certainty: grounded
- agreement: majority; vs common practice: extends (matches defence in depth; some domain-driven teams keep invariants in the application)
- positions: (a) invariants in the application domain layer, strongest argument: one place for logic, richer language; serves team cognitive load; wins with a single application owning the store. (b) the maintainer: integrity at the store; serves correctness across several writers and tools; wins when several consumers and ad-hoc access exist.
- public leads: web architecture slot sibling, constraints guidance.

**MAINT-C16** area VERIFY
- claim: A destructive or bulk operation whose scope can be unbounded must require an explicit opt-in flag from its caller, plus validation of mandatory keys, key order and timestamp sanity, so that omitting a filter by mistake cannot silently widen the effect.
- level: practice; stack: neutral; sources: MAINT-S01, soft-delete function guide (validation in the base function); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: safe-by-default interface guidance.

**MAINT-C17** area VERIFY
- claim: Every piece of derived or denormalized data needs a synchronisation plan before it exists, chosen from a ladder by cost and strength: documentation only, declared constraints, detection queries, scheduled refresh, same-transaction triggers; pick by impact of divergence, change frequency and tolerable staleness, avoiding both over-engineering and under-protection, and answer up front: what, sync level, freshness target, change frequency, impact of divergence, how drift is found and fixed, what alerts.
- level: decision; stack: neutral; sources: MAINT-S01, denormalization and cache architecture notes (ladder, up-front clarity); certainty: grounded
- agreement: majority; vs common practice: extends
- positions: always-consistent (same-transaction) serves correctness and costs write latency and coupling; eventual with a stated window serves delivery speed and cost; the maintainer ranks by impact of divergence. Wins by context: criticality, change rate.
- public leads: cache invalidation literature; Kleppmann on derived data.

**MAINT-C18** area VERIFY
- claim: Run detection queries on a schedule set by importance (daily, weekly, quarterly): periodic audits that find where derived data diverges from its source, with a stated action on divergence (manual fix or a reconciliation job).
- level: practice; stack: neutral; sources: MAINT-S01, denormalization architecture note (detection queries); certainty: grounded
- agreement: majority; vs common practice: agrees (reconciliation jobs)
- positions: none.
- public leads: reconciliation patterns.

**MAINT-C19** area VERIFY
- claim: Make conventions self-auditing: every rule ships with, or can be checked by, a query or script that finds its violations (for example a catalog query for objects not owned by the standard owner role), and a catalog of anti-patterns serves as the audit list.
- level: practice; stack: neutral; sources: MAINT-S01, schema design principles (ownership verification), anti-pattern catalog; certainty: grounded
- agreement: majority; vs common practice: agrees (policy as code)
- positions: none.
- public leads: policy-as-code; fitness functions (Ford, Parsons).

**MAINT-C20** area DELIVER, boundary: OPERATE
- claim: Roll out a new invariant check in observe-only mode first: the audit runs on every change and records its findings, autofix is a dry run, nothing raises; a kill-switch default of "observe" makes known defects tolerable and is recorded as not being the fix, and enforcement is switched on only after the open defects are removed.
- level: decision; stack: neutral; sources: MAINT-S01, write-ownership architecture note (current posture); certainty: grounded
- agreement: majority; vs common practice: agrees (shadow mode, feature flags)
- positions: enforce immediately serves correctness; observe first serves reversibility and delivery speed; wins when known violators exist in production.
- public leads: feature-flag and dark-launch guidance (Humble and Farley).

**MAINT-C21** area DELIVER, boundary: VERIFY
- claim: Compare the deployed definitions of executable database objects against their source in the repository mechanically (export the deployed definitions, parse both sides, compare signature and body after normalization, report by severity), because the two drift.
- level: practice; stack: neutral in the idea, tool is PostgreSQL-specific; sources: MAINT-S01, deployed-versus-source validator readme; certainty: grounded
- agreement: majority; vs common practice: agrees (drift detection, infrastructure as code)
- positions: none.
- public leads: configuration drift detection; GitOps.

**MAINT-C22** area DELIVER
- claim: Ship schema, function and data changes as ordered, once-only, version-tracked migration files recorded in a history table; never apply changes manually; the stated reason is the earlier state of inconsistent environments, missing migrations and untracked manual changes.
- level: principle; stack: neutral; sources: MAINT-S01, migration guide (why a migration tool); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: Fowler and Sadalage, Evolutionary Database Design; Flyway documentation.

**MAINT-C23** area DELIVER
- claim: Never edit a migration after it has been applied; if it failed, fix and rerun it; if it succeeded but was wrong, add a new migration; a recorded checksum enforces this; forced replay is rare and administrator-only.
- level: practice; stack: neutral (Flyway-shaped); sources: MAINT-S01, migration guide (changing migrations); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: Flyway documentation.

**MAINT-C24** area DELIVER
- claim: Every migration names its ticket and carries a written undo section (rollback is a documented reverse change prepared ahead, not an automatic down step), and migration files do not open their own transactions because the tool manages them.
- level: practice; stack: neutral in the first part; sources: MAINT-S01, migration guide (workflow, transaction handling); certainty: grounded
- agreement: contested; vs common practice: partly differs (forward-only versus down migrations)
- positions: (a) automatic down migrations, strongest argument: one-command reversal; serves reversibility; wins for reversible schema changes. (b) forward-only with a documented undo: serves control and honesty about data migrations that cannot be reversed; wins when data changes dominate.
- public leads: expand and contract (parallel change, Fowler).

**MAINT-C25** area DELIVER
- claim: Write DDL idempotently (create if not exists, drop if exists, conditional column adds) "as if it will be run twice", except where re-running would corrupt data (one-time data migrations) or where the operation must fail if its precondition does not hold.
- level: practice; stack: neutral (SQL form); sources: MAINT-S01, schema design principles (DDL idempotency), function design guideline (drop before create); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: idempotent serves resilience of partially applied scripts; once-only (tool guarantee) already serves that, so idempotence is defence in depth, at the cost of verbosity. Internal tension: see disagreements.
- public leads: Humble and Farley, repeatable deployment.

**MAINT-C26** area DELIVER
- claim: Split change automation by risk: ordinary changes apply automatically on the integration branch to the development environment; changes that run long (over about five minutes), take locks, are environment-specific, cannot run in a transaction (concurrent index builds) or need monitoring are manual migrations excluded from the automatic path; production is applied manually by a small authorized group.
- level: decision; stack: neutral; sources: MAINT-S01, migration guide (manual migrations, workflow, historical pain points); certainty: grounded
- agreement: contested; vs common practice: contradicts continuous deployment
- positions: (a) automated deployment of every change to production, strongest argument: small frequent changes are safer and measured better (DORA); serves delivery speed and confidence; wins when changes are reversible and rollouts staged. (b) the maintainer: database changes on a very large store are partly irreversible and lock-prone, so a human gate and a manual lane for risky operations; serves reversibility and control; wins at large data volume and low tolerance for downtime.
- public leads: DORA and Accelerate; Humble and Farley, Continuous Delivery.

**MAINT-C27** area DELIVER
- claim: The delivery path is: feature branch carrying the ticket key, migration, manual test on development, pull request with approval, automatic apply on development, verification on staging, a release pull request that is approved but not merged, manual production run by authorized people, then application deploy; the release pull request is explicitly not merged until the production run.
- level: practice; stack: neutral; sources: MAINT-S01, migration guide (development flow); certainty: grounded
- agreement: majority; vs common practice: agrees in shape, extends (the unmerged release approval)
- positions: none beyond MAINT-C26.
- public leads: Continuous Delivery pipeline stages.

**MAINT-C28** area DELIVER
- claim: Gate an application deploy on a declared minimum schema version: a version file names the required migration version, and the deploy fails if the target database's history does not contain it.
- level: practice; stack: neutral; sources: MAINT-S01, migration guide (version dependencies); certainty: grounded
- agreement: majority; vs common practice: agrees (compatibility gate between schema and code)
- positions: none.
- public leads: expand and contract; Fowler on database refactoring.

**MAINT-C29** area DELIVER, boundary: VERIFY
- claim: On every change request, a workflow restores a dump of development data and applies every migration of the request, including manual ones; a migration that cannot work on the partial dump carries a skip marker with its reason, and still runs on the real environments.
- level: practice; stack: neutral; sources: MAINT-S01, migration guide (testing strategy); certainty: grounded
- agreement: majority; vs common practice: agrees (migration CI on a representative dataset)
- positions: none.
- public leads: continuous integration for database changes.

**MAINT-C30** area DELIVER
- claim: Configuration-like registry content (for example validation schemas) has an idempotent authoring script as its source of truth, deployed by running that script against the target; a migration may mirror the change as an audit trail but is not the deployment vehicle.
- level: decision; stack: neutral; sources: MAINT-S01, JSON patterns guideline (authoring workflow); certainty: grounded
- agreement: contested; vs common practice: contradicts (one pipeline for all changes)
- positions: (a) every change through the same migration pipeline, strongest argument: single audited path; serves control. (b) script-as-source for content that is re-authored often and must stay in a pure form; serves delivery speed and avoids stale embedded copies; wins when content is data-like and small. Internal tension: two delivery truths (see disagreements).
- public leads: configuration-as-data guidance.

**MAINT-C31** area DELIVER, boundary: ADOPT
- claim: Evolve a shared interface additively and backward-compatibly by default (new units, new parameters with defaults); coordinate breaking changes with every consumer and deploy them together; do not introduce version numbers, keep a dated change log with each unit.
- level: decision; stack: neutral; sources: MAINT-S01, function-API architecture note (evolution and coordination); certainty: grounded
- agreement: contested; vs common practice: contradicts for public interfaces, agrees for in-house ones
- positions: (a) explicit versioning, strongest argument: consumers choose when to move; serves consumer independence and exit risk; wins with many or external consumers. (b) additive plus coordination: serves cost of ownership; wins with few in-house consumers reachable by review and conversation.
- public leads: semantic versioning; Hyrum's Law (Software Engineering at Google); parallel change.

**MAINT-C32** area DELIVER
- claim: A new convention applies to new objects and is not retroactive: existing objects are not forced to rename; a deprecated item is marked in its name, kept with documented deprecation and relationships during the transition, and removed by a later planned change.
- level: practice; stack: neutral; sources: MAINT-S01, naming guideline (deliberate evolution, deprecated pattern); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: retroactive rename serves consistency and costs risk; forward-only serves cost and reversibility; wins when the surface has many consumers.
- public leads: deprecation policies.

**MAINT-C33** area DELIVER
- claim: Review uses a maintained anti-pattern catalog read by the type of change (table, function, query, JSON, index), then the guideline for that change; the catalog doubles as an audit list.
- level: practice; stack: neutral; sources: MAINT-S01, guideline router (reviewing code), anti-pattern catalog; certainty: grounded
- agreement: majority; vs common practice: agrees (review checklists)
- positions: none. Note the catalog is stale against the modules (see disagreements); a rubric that is not kept current misdirects review.
- public leads: Software Engineering at Google, code review chapter.

**MAINT-C34** area DELIVER
- claim: Escalate review by risk, not by size: any change that holds locks, runs longer than about five minutes or can affect availability needs review by named senior approvers; production runs are restricted to the same small group.
- level: decision; stack: neutral; sources: MAINT-S01, migration guide (when to consult), bulk execution guide (preconditions); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: risk-based gates serve safety and cost review effort where it pays; wins with a small trusted senior group and few critical changes.
- public leads: change advisory practice versus lightweight peer review (DORA discusses the latter as better).

**MAINT-C35** area DELIVER
- claim: Run a single statement over very large data (backfill, archival copy, column population, order of ten million to a billion rows) as a four-decision procedure, in order: batching key (indexed key part, then numeric range, modulo only as a last resort), work list (generated from the data so batch count follows population, not a cartesian grid), fan-out (workers), observe and recover; if one statement finishes in minutes, just run it as a migration.
- level: decision; stack: neutral procedure (shell runner and database client named in the doctrine are PostgreSQL and GNU parallel pointers); sources: MAINT-S01, bulk parallel execution guide (the four decisions, steps 1 and 2); certainty: grounded
- agreement: majority; vs common practice: extends
- positions: one long transaction serves simplicity and costs locks, bloat and an hours-long open transaction; sharding serves control; the size gate decides.
- public leads: batch-processing and online migration guidance (gh-ost, pt-online-schema-change literature).

**MAINT-C36** area DELIVER
- claim: Every batch must be safely re-runnable in isolation: prefer a self-limiting predicate (the data is its own ledger) to external bookkeeping; make non-idempotent updates absolute; keep one logical unit (insert and delete of a move) in one statement, never two calls; do not combine automatic retries with non-idempotent batches.
- level: principle; stack: neutral; sources: MAINT-S01, bulk execution guide (idempotence and resumability, anti-patterns); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: idempotency in distributed systems.

**MAINT-C37** area DELIVER, boundary: VERIFY
- claim: "Done" for a bulk change is a written convergence query that returns zero remaining work, not the job process returning; a non-zero result means skipped or silently failed batches, and re-runs must strictly decrease it.
- level: practice; stack: neutral; sources: MAINT-S01, bulk execution guide (verify convergence); certainty: grounded
- agreement: majority; vs common practice: extends
- positions: none.
- public leads: reconciliation checks in data migration.

**MAINT-C38** area DELIVER
- claim: Ramp concurrency, never guess it: run one batch by hand with its plan inspected, then one worker, then a modest default, then higher only with a reason and a metric; on the first production run halt on the first failure; keep a ledger of batches with exit codes and separate error and progress streams; detach the job from the operator's session; bound worker count by connections, headroom and replica lag, and compute total time from batch time before blaming the worker count.
- level: practice; stack: neutral procedure; sources: MAINT-S01, bulk execution guide (sizing the pool, observe and recover, setup); certainty: grounded
- agreement: majority; vs common practice: agrees (progressive rollout), extends (the ledger and halt rules)
- positions: none.
- public leads: progressive delivery; SRE guidance on load.

**MAINT-C39** area DELIVER
- claim: Do not start a production bulk job until a checklist holds: a ticket exists and its key is in the statement text; a full development run at one worker, then a few; the batch predicate is index-backed (verified by a plan, not assumed); every batch is idempotent or the predicate makes the job convergent; the convergence query is written; the job runs detached with a ledger; the change is a manual migration; senior review if it holds locks or runs long; a stop plan names what to cancel and whether partial completion is acceptable.
- level: practice; stack: neutral; sources: MAINT-S01, bulk execution guide (production preconditions); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: production readiness reviews (Google SRE).

**MAINT-C40** area DELIVER
- claim: Do not shard schema changes: they need whole-object locks; use the platform's concurrent variant in a manual migration, and shard only data changes.
- level: practice; stack: PostgreSQL (stack-tagged pointer); sources: MAINT-S01, bulk execution guide (load, locks, bloat; anti-patterns); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: PostgreSQL documentation on concurrent index builds.

**MAINT-C41** area OPERATE
- claim: While a job runs, watch the target system, not only the job's shell: lock waits, per-batch runtime climbing (a sign the predicate is not index-backed), dead-tuple growth, and replica lag as the governing signal for concurrency; escalate (reduce workers, stop) on those signals.
- level: practice; stack: neutral in the signals; sources: MAINT-S01, bulk execution guide (watch the database, load, locks and bloat); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: Google SRE, monitoring chapters.

**MAINT-C42** area OPERATE
- claim: Put the change's ticket key in a comment inside long-running statements, so that it appears in activity views and logs and identifies the job during an incident.
- level: practice; stack: neutral; sources: MAINT-S01, bulk execution guide (production preconditions); certainty: grounded
- agreement: consensus; vs common practice: agrees (query tagging, trace correlation)
- positions: none.
- public leads: sqlcommenter-style query tagging; OpenTelemetry context.

**MAINT-C43** area ADOPT
- claim: For one-off bulk work, compose standard command-line tools (a parallel runner, a terminal multiplexer, the database client) rather than building a framework, and verify each part in isolation, then compose at one worker on the lower environment.
- level: practice; stack: neutral in the principle; sources: MAINT-S01, bulk execution guide (setup, fan-out); certainty: grounded
- agreement: majority; vs common practice: agrees (Unix composition)
- positions: a framework serves repeatability and costs ownership; wins when the job recurs.
- public leads: Unix philosophy.

**MAINT-C44** area ADOPT
- claim: Treat every new layer or moving part as a cost (write, test, maintain, evolve, onboard) and create it only when at least one strong reason outweighs that cost: reuse across consumers, hiding internals behind a business-level verb, keeping a query tunable by its owner without redeploying consumers, or enforcing integrity once; otherwise the logic stays in the simpler place.
- level: decision; stack: neutral (stored functions in the doctrine); sources: MAINT-S01, function-API architecture note (the decision), function design guideline (header); certainty: grounded
- agreement: majority; vs common practice: agrees (build-versus-not discipline)
- positions: default to the layer (database-centric) versus default to not creating it (application-centric); the maintainer defaults to not creating it, then accepts a wide band once justified (the earlier database slot records the band).
- public leads: Fowler on avoiding premature abstraction; Software Engineering at Google on dependencies and cost.

**MAINT-C45** area ADOPT, boundary: DELIVER
- claim: Prefer an interface with a signature (parameters, defaults, overloads) to one consumers bind to by exact shape, because a shape-bound object ossifies like a table and has nothing to absorb change; keep shape-bound objects for owner-only throwaway or introspection use.
- level: decision; stack: neutral in the principle, realized as function over view in the doctrine; sources: MAINT-S01, function-API architecture note (avoid views); certainty: grounded
- agreement: contested; vs common practice: contradicts (views are commonly offered as a stable interface)
- positions: (a) views as a stable read interface, strongest argument: declarative, no code, plannable; serves cost of ownership; wins for read-only reporting with several consumers. (b) function: serves change absorption and owner-tunable performance; wins when many backends depend on the contract.
- public leads: Hyrum's Law; interface stability guidance.

**MAINT-C46** area ADOPT
- claim: Prefer a platform built-in over custom code unless it lacks a stated capability; when custom code is chosen, record the missing capabilities (here: partial refresh, per-entry sync strategies, lazy invalidation) and revisit if the need shrinks to what the built-in does; the doctrine marks the built-in "not currently used".
- level: decision; stack: neutral in the rule (materialized views versus manual cache tables); sources: MAINT-S01, cache architecture note (cache versus materialized views); certainty: grounded
- agreement: contested; vs common practice: contradicts (prefer the built-in)
- positions: (a) built-in, strongest argument: less code to own, supported behaviour; serves cost of ownership and exit risk; wins when its model fits. (b) custom: serves control and fit; wins when granularity or per-entry strategies are needed.
- public leads: build versus buy guidance (Software Engineering at Google).

**MAINT-C47** area ADOPT
- claim: Run scheduled work where the data lives when it acts on database state (atomicity with the data, one system to run and observe, job history queryable), and record the limits that send work elsewhere: no operating-system commands, CPU-heavy work belongs in the application tier, highly parallel work and streaming belong to other infrastructure.
- level: decision; stack: PostgreSQL in-database scheduler (stack-tagged pointer); sources: MAINT-S01, scheduled-jobs architecture note (why in the database, trade-offs); certainty: grounded
- agreement: contested; vs common practice: contradicts (a dedicated orchestrator is the usual norm)
- positions: (a) external orchestrator, strongest argument: retries, dependencies, backfills, visibility across systems; serves control and scale; wins for multi-system pipelines. (b) in-store scheduler: serves cost of ownership and consistency; wins for small jobs on one store.
- public leads: scheduler and orchestrator documentation.

**MAINT-C48** area ADOPT
- claim: Choose the core technology by problem fit, not dogma (a relational engine because it solves integrity and scale cleanly), and choose the programming paradigm per part by intent (object-oriented for taxonomies, functional for transformation pipelines, imperative for control flow).
- level: principle; stack: neutral; sources: MAINT-S01, work-thinking philosophy (structured data first, intentional polyglotism); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: general engineering guidance.

**MAINT-C49** area OPERATE
- claim: Monitor scheduled and derived-data work on four signals: duration against a documented expectation, failure (any), backlog (queue size and age of oldest entry), and missed runs (not run within twice the interval); jobs are short, idempotent, scheduled off-peak without overlapping, named descriptively, and wrap errors so that they log and re-raise, so the scheduler records the failure.
- level: practice; stack: neutral; sources: MAINT-S01, scheduled-jobs architecture note (monitoring and best practices), cache notes (maintenance); certainty: grounded
- agreement: majority; vs common practice: agrees (golden signals differ in kind)
- positions: none.
- public leads: Google SRE golden signals; dead-man switch alerting.

**MAINT-C50** area OPERATE
- claim: Staleness is a designed property: store timestamps for staleness detection, state the freshness target up front, build the sync mechanism and its monitoring hooks before first production use, and treat "no invalidation" and "no monitoring" as defects.
- level: principle; stack: neutral; sources: MAINT-S01, cache architecture note (lifecycle, anti-patterns); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: service-level objectives for data freshness.

**MAINT-C51** area OPERATE
- claim: Errors name the component and the offending values and carry stable custom codes; mandatory inputs are validated first, and a failure is explicit rather than silent.
- level: practice; stack: neutral; sources: MAINT-S01, function design guideline (error handling, input validation); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: error-handling guidance.

**MAINT-C52** area VERIFY
- claim: Test a scheduled job before scheduling it: call its unit directly and in a reduced test mode (a parameter that limits scope) and inspect the affected data.
- level: practice; stack: neutral; sources: MAINT-S01, scheduled-jobs architecture note (testing jobs); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: none beyond general testing guidance.

**MAINT-C53** area OPERATE
- claim: Watch index and storage health: find unused indexes by usage counters and drop them, watch index and table bloat, and rebuild concurrently.
- level: practice; stack: PostgreSQL (stack-tagged pointer); sources: MAINT-S01, schema performance guideline (monitoring), indexing guideline; certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: none.
- public leads: PostgreSQL documentation on statistics views.

**MAINT-C54** area TRANS
- claim: Keep one durable explanation per unit: a mandatory structured header comment (summary, parameters, returns, notes, change log, examples with expected output) is the only multi-line comment; inline comments carry only why, invariant or gotcha, never what the next line does, at most about three consecutive lines; complex logic gets compact step banners whose outline is mirrored in the header.
- level: practice; stack: neutral; sources: MAINT-S01, function design guideline (documentation standards, comment discipline); certainty: grounded
- agreement: contested; vs common practice: partly contradicts (mandatory header on every unit and a dated change log duplicating version control)
- positions: (a) self-documenting code with history in version control, strongest argument: comments rot; serves cost of ownership. (b) mandatory header plus change log: serves team cognitive load and durability where the unit is called by many consumers and lives apart from its history; wins when readers cannot see the repository history.
- public leads: Clean Code comment guidance versus API documentation norms.

**MAINT-C55** area TRANS
- claim: Date-stamp verification against the live system in documents ("verified live on <date>", "verified against live code on <date>"), point fast-moving topics to the more current tracker, and record open known violations with their status and the mitigation, without presenting a mitigation as a fix.
- level: practice; stack: neutral; sources: MAINT-S01, write-ownership architecture note, JSON patterns guideline; certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none beyond the dates tension (see disagreements).
- public leads: documentation freshness guidance.

**MAINT-C56** area TRANS
- claim: A generated or derived document is read-only and never copied back into the source of truth; an expanded copy written into a registry that resolves references can silently shadow its source (the resolver skips a reference whose target already exists), so edits to the source stop propagating with no error.
- level: principle; stack: neutral; sources: MAINT-S01, JSON patterns guideline (registry model, shadowing trap); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: single source of truth guidance.

**MAINT-C57** area TRANS
- claim: Organize guidelines as a router set: an index by role and situation ("designing a table? read in this order"), modules under a size cap with line-number tables of contents, cross-references kept, indexes updated with every change, and each guideline linked to the formal model node it derives from.
- level: practice; stack: neutral; sources: MAINT-S01, guideline router (index, maintenance); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none; evidence that the line counts and tables of contents rot is in disagreements (measured).
- public leads: documentation structure (Diataxis).

**MAINT-C58** area TRANS
- claim: Write documentation at layered detail (one sentence, one paragraph, then full what, why and how) with diagrams at three zoom levels (macro, flow, detailed), and split the audience: a non-engineer understands the why and an engineer the how; technical vocabulary stays in the internal "engine room".
- level: practice; stack: neutral; sources: MAINT-S01, permissions architecture note (rough, medium, full), philosophy (anti-jargon, visualization); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: none.
- public leads: Diataxis; C4 model.

**MAINT-C59** area TRANS
- claim: Guidelines are induced from analysis of real production code (including observed queries) and updated as practice evolves, with deliberate-evolution notes that state which earlier rule a new rule overrides and for which objects.
- level: practice; stack: neutral; sources: MAINT-S01, guideline router (overview), query style guideline (header), naming guideline (reconciliation); certainty: grounded
- agreement: contested; vs common practice: extends
- positions: (a) induced from practice, strongest argument: reflects what works and gets adopted; serves cost of ownership; wins in a mature codebase. (b) deduced from principles first (the maintainer's philosophy asks for structure before implementation): serves correctness and consistency. Internal tension: see disagreements.
- public leads: engineering handbooks of large organizations.

**MAINT-C60** area TRANS, boundary: ADOPT
- claim: A decision record states the costs it accepts as the other half of the decision (here: tests are difficult and manual, no refactoring tools, harder onboarding, limited expressiveness), so a strong reason has something concrete to outweigh.
- level: principle; stack: neutral; sources: MAINT-S01, function-API architecture note (limitations); certainty: grounded
- agreement: majority; vs common practice: agrees (decision records, trade-off analysis)
- positions: none.
- public leads: architecture decision records (Nygard).

**MAINT-C61** area TRANS
- claim: Enforce access at the lowest layer every path passes through (so migrations, debugging and ad-hoc statements are governed like application code), as least privilege by role, separately from application-level business permissions; have all objects owned by one standard owner for migration safety, with a catalog query that finds violations.
- level: principle; stack: neutral (PostgreSQL roles in the doctrine); sources: MAINT-S01, permissions architecture note, schema design principles (ownership); certainty: grounded
- agreement: consensus; vs common practice: agrees
- positions: application-only authorization serves speed and misses direct paths.
- public leads: OWASP access-control guidance; least privilege (NIST).

**MAINT-C62** area TRANS
- claim: Give an AI agent or other automation one sanctioned path to the data system and enforce its limits in the tooling (single statement, read-only on production, statement timeout, audit log), not by instruction in a prompt.
- level: principle; stack: neutral; sources: MAINT-S01, bulk execution guide (relationship to the query wrappers); certainty: grounded
- agreement: majority; vs common practice: agrees (least privilege for automation)
- positions: none.
- public leads: OWASP guidance on agentic systems and least privilege.

**MAINT-C63** area TRANS, boundary: DELIVER
- claim: An agent may write the script, the work-list query and the convergence query for a high-blast-radius production job, but must not execute them; the human runs them at their own terminal, because the execution bypasses the tooling's guards.
- level: decision; stack: neutral; sources: MAINT-S01, bulk execution guide (relationship to the query wrappers, preconditions); certainty: grounded
- agreement: majority; vs common practice: agrees
- positions: agent executes under approval serves speed; agent writes only serves control and audit; wins when blast radius is large and guards cannot be applied.
- public leads: human-in-the-loop guidance.

**MAINT-C64** area TRANS
- claim: Document known environment differences (data volume, permissions, missing schemas, performance) as recurring pain points and handle them by routing the change to a manual, environment-specific migration or conditional SQL, rather than pursuing identical environments.
- level: decision; stack: neutral; sources: MAINT-S01, migration guide (known issues and exceptions); certainty: grounded
- agreement: contested; vs common practice: contradicts (dev/prod parity)
- positions: (a) dev/prod parity, strongest argument: failures found early; serves speed of feedback; wins when environments are cheap to make alike. (b) accept divergence and route: serves cost of ownership; wins when production-sized data is unaffordable to replicate.
- public leads: Twelve-Factor, dev/prod parity.

**MAINT-C65** area DELIVER
- claim: Derive before coding, in order: usage and functional scenario, data flow, schema, system design, implementation strategy, then code; write the strategy (why and how in abstract terms) before the tactics; invest time in names that are hierarchical, unambiguous and intuitive (a newcomer should understand them).
- level: decision; stack: neutral; sources: MAINT-S01, work-thinking philosophy (process, naming protocol, interaction protocol); certainty: grounded
- agreement: majority; vs common practice: agrees in intent, differs from test-first or emergent design
- positions: design first serves correctness and reversibility; emergent design serves speed of feedback.
- public leads: Beck on test-driven development; Domain-Driven Design.

**MAINT-C66** area DELIVER
- claim: Design the structure for probable future usage, not only today's ticket (for example decide column versus table by whether a cardinality drift is plausible), while avoiding speculative optimization.
- level: decision; stack: neutral; sources: MAINT-S01, work-thinking philosophy (future-proofing), schema design principles (adding a column versus a table); certainty: grounded
- agreement: contested; vs common practice: contradicts (YAGNI)
- positions: (a) build only for today (YAGNI), strongest argument: speculation is usually wrong and costs complexity; serves delivery speed and cost; wins when change is cheap. (b) predict probable use: serves reversibility; wins when changes to structure are costly (a very large relational store).
- public leads: Beck, extreme programming (YAGNI); evolutionary architecture.

**MAINT-C67** area VERIFY
- claim: The doctrine states how a function test is built and run but not who runs the suite, when, on what trigger, nor how regressions are caught across changes; the practice in force appears to be on-demand runs by a human or agent.
- level: open; stack: neutral; sources: MAINT-S01, absence across the testing guidelines; certainty: open (inferred absence: what was checked: the testing guideline, the fixtures guideline, the router and the migration guide for a regression run, a suite or a CI step for function tests, and found none; the migration pull-request workflow applies migrations but is not a function-test run)
- agreement: n/a; vs common practice: contradicts if confirmed absent (automated regression in CI is the norm)
- positions: none (an observation of a gap).
- public leads: Continuous Delivery, automated test stages.

### Gaps

- Regression execution and test-suite health (MAINT-C67): unstated.
- Review beyond the anti-pattern catalog and risk escalation: no checklist for what a reviewer checks in application code.
- Rollback rehearsals, backups and restore tests, disaster recovery: not found in the files read.
- Supply-chain and dependency pinning for the tools used (parallel runner, client): not stated.
- Alert routing and on-call: the doctrine says an external process polls an alert table and notifies, nothing on escalation or SLOs.
- Secrets handling beyond a credential file with restricted permissions: not stated.
