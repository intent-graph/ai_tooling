# J1 ALLOCATION: adversarial review of the judge's verdicts

This is a review of `../J1_allocation/` (`records.md`, `allocation_matrix.md`, `questions.md`, `result.md`) under the max rule of `../../target_hierarchy.md`. I checked every placement for hedging, grounding, consistency, fit with the default context, stronger positions the judge missed, and whether Q1 is a genuine question. Evidence ids `Lnnn` resolve in `../../02_skeleton/claims_ledger.md`, and source ids in `../../02_skeleton/sources.md`. I read two sources directly for this review: the OpenAPI Initiative best-practices page (SRC-241) and the PostgreSQL page "Data Consistency Checks at the Application Level" (the T1 family of SRC-331 and SRC-337).

Certainty: **grounded** means I read the rows or the source and they say it. **Inferred** means it follows from grounded rows or from logic, but no source states it. **Open** means not settled.

Pinned:
- Findings: 12. Blocking 2: F1 Q1 is mis-framed and its recommendation should flip (PIG-WEB.ALLOCATION.ROW_SECURITY); F2 code-first interface origin is a convenience default, not the max (ALLOCATION.RECORD.3, PIG-WEB.ALLOCATION.TYPE_CHAIN). Major 4: F3 one origin per shape instead of per fact, with hand-mirrored copies the judge itself forbids; F4 GUARD.2's multi-row rules are check-then-write under Read Committed; F5 the default context is used inconsistently (consoles, migrations, reporting role); F6 the matrix labels judgments "grounded". Minor 6: F7 CACHE_STORE stretches L534 past its scope; F8 ACT.1 leaves the costs of its verdict against L584 unweighed; F9 TYPE_CHAIN assumes a JSON API although the default browser contract is HTML; F10 FORCES sets no order among changeability, performance and scalability; F11 collation has no owner and the browser re-sort copy can contradict it; F12 ACT.4 leans on a row marked grounded that has no source.
- Verdict on TYPE_CHAIN and RECORD.3: the storage origin (database schema) is the max and stands. The interface origin (code-first, Pydantic models) is a convenience default, not the max. Design-first is the max under the judge's own moving condition, and the default context meets that condition: agents as users read the contract, and the browser gets HTML. Re-decide: the interface description is written first and is the origin; Pydantic interface models are generated from it or conformance-checked in CI; fields that echo stored facts take them from the database schema. Code-first stays as "acceptable when every consumer of the interface is code the team builds and ships together".
- Verdict on Q1: it is a genuine trade-off (security against changeability), so it stays a question. But it is mis-framed, and the recommendation should flip:
  - the claim that drift between the two gates harms security is wrong, because two gates in conjunction can only over-deny;
  - two of the costs it lists for A are already paid by decided placements (the non-owner request role in GUARD.3, the transaction-local actor in ACT.4);
  - the recommendation for B rests on source agreement;
  - the default context already holds an access path that skips the backend (the reporting role that RECORD.2 permits).

  Recommend A: row security as a second line on tables with per-user visibility rules. B is acceptable when no table has per-user visibility and the backend's request role is the only role that reads the data.
- New maintainer questions: none as a trade-off; Q1 stays, re-framed. One context fact to confirm, which decides TYPE_CHAIN and Q1's trigger: are agent clients the users' own hosts (independent of the team), and does any role other than the backend's request role read the data (reporting, consoles)?

## Findings

### F1 (blocking) Q1 is mis-framed and its recommendation rests on agreement

**Node**: PIG-WEB.ALLOCATION.ROW_SECURITY; ALLOCATION.GUARD.3 (its second-line clause).

**What is wrong.**
1. *The decisive argument is false (inferred, by logic).* `questions.md` says A's cost "falls on the security property itself once the two drift". Row security is a second gate in conjunction with the backend check, and the decided part forbids "row security replacing backend checks". When the two drift, a request passes only if both gates permit it. Drift can therefore make the database deny what the backend allows, which is a functional bug, but it can never let through what the backend denies. The same holds for the sub-select race of L310: the leak is relative to the policy, and the backend check still stands in front of it. Under conjunction, A's security is never below B's.
2. *Two of the costs listed for A are already paid by decided placements (grounded in the judge's own records).*
   - "The acting user must reach every transaction through a transaction-local setting (L311, L566)": ACT.4 already requires this, in its words "actor taken from the verified identity through a transaction-local setting (L566 MAINT, L311)".
   - The request role must be neither owner nor superuser (L310): GUARD.3 already decides "the request role is least-privilege, neither owner nor superuser".
   What A actually adds is the policy definitions, their indexes and the denial tests.
3. *The recommendation is the averaged verdict the max rule forbids.* "B is what the evidence and the doctrine recommend for exactly this context" (L688, L620, L468) is agreement among sources used as the verdict. `target_hierarchy.md`: "Agreement among sources is evidence for the judgment, never the verdict." L310 itself records that the sources do not settle row security against application-side filtering ("Whether to use RLS rather than application-side filtering is not settled by the sources", grounded).
4. *"Single tenant weakens A" mistakes the target.* A guards per-user visibility (record ownership), which is exactly the object-level rule that L306 makes mandatory. A missed object-level check is the failure that A bounds, and a tenant boundary has nothing to do with it (inferred).
5. *The trigger condition already fires in the default.* RECORD.2 permits "reports use a read-only role or reporting copy (L044)". A read-only role on the live database is an access path that skips the backend, and ROW_SECURITY's decided part makes row security required for such paths. L044 itself names only "a separate read-only reporting copy", not a role (grounded). See F5.

**Fix.** Keep Q1 as the one trade-off: security against changeability (the policy kept in two places) is genuine. Rewrite it:
- Remove the drift-harms-security argument.
- Restate A's incremental cost as the policies, the policy indexes and the denial tests.
- Recommend A, scoped: row security as a second line on tables that carry per-user or per-role row visibility, with denial tested through the deployed role (L128). The max for security, inferred.
- Keep B as "acceptable when no table carries per-user visibility rules and the backend's request role is the only role that reads the data".
- Resolve the reporting role first (F5): either a reporting copy without per-user data, or a reporting role under row security.

### F2 (blocking) The code-first interface origin is a convenience default, not the max

**Node**: ALLOCATION.RECORD.3; PIG-WEB.ALLOCATION.TYPE_CHAIN.

**What is wrong.**
1. *The judge's own moving condition fires in its own default context (inferred, from grounded rows).*
   - RECORD.3 rejects design-first only "when consumers are independent of the producing team (third parties, other teams)". The default context has "humans and agents as users".
   - Agent clients read the API description directly: L634 says "so humans, code generators and agents read one description" (grounded). They are typically hosts the team does not write: L635, "expose an MCP server when third-party LLM hosts must connect" (grounded, contested on the surface).
   - PRESENT.1 makes server-rendered HTML the browser's contract, so in the default the main reader of the JSON interface is the agent, an independent consumer. That is the design-first case under L548's own condition ("design-first fits independent consumers").
2. *The "zero drift" argument does not separate the positions.* RECORD.3 says "design-first keeps two (description and code) aligned by a conformance check". That compares code-first against a hand-maintained design-first, not against design-first done well. A description written first, with models generated from it or checked against it in CI, also has one origin. The OpenAPI Initiative gives exactly these two options: keep one source and "either using Continuous Integration testing or avoiding duplicate maintenance altogether" (SRC-241, read for this review). Drift is a tie, so the decision falls to the remaining forces.
3. *On the remaining forces the evidence favours design-first.*
   - The strongest sources are explicit: "The importance of using Design-first cannot be stressed strongly enough", and code-first yields "unintuitive and incomplete descriptions, that will rarely scale in the future" (SRC-241, read; L272 majority, Zalando MUST).
   - The code-first side is a single source family describing a mechanism (FastAPI and Pydantic docs, SRC-328, SRC-356), and the condition that favours it is marked inferred in the ledger (L548: "grounded for the mechanism; the condition is inferred").
   - The judge's "completeness gate" is its own synthesis, invented to patch the objection, and no row supports it.
4. *It inverts the derivation order the guideline holds elsewhere.* The judge puts structure first for storage (L474, max) and then lets implementation code be the origin of the interface structure. Design-first makes the contract a deliberate act. Under code-first, a refactor of a Pydantic model changes the contract, and CI catches it only afterwards (inferred).

**Fix.** Re-decide RECORD.3's interface shape and TYPE_CHAIN's interface chain as follows:
- The interface description (OpenAPI for the HTTP surface; the agent surface's tool descriptions derived from the same core, L635) is written first and is the origin.
- Pydantic input and output models are generated from it or conformance-checked against it in CI. Which generator to use is *open*: no generator was read.
- TypeScript types are generated from it, build-time only (L555).
- Code-first is acceptable when every consumer of the interface is code the team builds and ships together (for example a client-rendered island's types in the same deploy).
- State `known | unvalidated: agents as independent consumers is inferred (L634, L635)`.

If the maintainer confirms that the agent clients are the team's own programs, the condition does not fire and code-first may stand as the default. That is the context fact pinned above.

### F3 (major) One origin per shape, not per fact; the judge keeps hand-mirrored copies it forbids

**Node**: ALLOCATION.RECORD.3, ALLOCATION.GUARD.2, PIG-WEB.ALLOCATION.TYPE_CHAIN; RULES.1.

**What is wrong.**
- L486 is about one source of truth per *fact* ("hand-copied type definitions across database, Python and browser"). RECORD.3 weakens it to "one origin per shape" with two shapes and two origins.
- Facts that both shapes carry then have two origins: a status enum, a length limit, nullability, a CHECK range. One origin is the schema; the other is the Pydantic interface model.
- The judge also keeps two hand mirrors:
  - "Application persistence models mirror it, checked by a test" (RECORD.3);
  - "Application validators mirror the constraints for early feedback" (GUARD.2).
  Both contradict RECORD.3's and TYPE_CHAIN's own forbidden lists ("hand-copied types in any tier"; "hand-written TypeScript or Python copies of a shape").
- They also break RULES.1: a copy "never decides". A backend validator that rejects input before the database sees it does decide. If the copy is stricter than the constraint, valid data is refused.

Grounding: L486 grounded for the sentence, with the cross-tier application inferred; L495's "mirror" advice is marked inferred in the ledger.

**Fix.**
- State the rule per fact: a fact about stored data (type, nullability, enum values, ranges, lengths) originates in the database schema.
- Persistence models are generated from the live schema (L474: the live database is the truth for structure). The generator is *open*.
- Interface fields that echo a stored fact are generated from the catalogue or checked against it in CI.
- Hand-written mirrors with a CI comparison are kept only as "acceptable when no generator fits".
- GUARD.2's validators become generated or tested copies, not mirrors.

### F4 (major) GUARD.2's multi-row branch has the defect it uses against L471

**Node**: ALLOCATION.GUARD.2 (and its link to GUARD.5).

**What is wrong.**
- GUARD.2 rejects L471's in-function validation because "a check inside a write function is check-then-write, correct only under serializable isolation (L473)". It then places multi-row rules in "constraint triggers, or a function that is the only write path".
- A trigger or function that reads other rows to check a rule is check-then-write too, at the default Read Committed level. PostgreSQL: "It is very difficult to enforce business rules regarding data integrity using Read Committed transactions because the view of the data is shifting with each statement". It recommends Serializable for all writes, or explicit locks ("SELECT FOR UPDATE, SELECT FOR SHARE, or an appropriate LOCK TABLE"). It even suggests "checks of the transaction isolation level in triggers" (read for this review).
- Repeatable Read still allows write skew (L577, grounded).
- The judge never cites L568 or L569, which carry this stronger position: "If Serializable is used for all writes ... no other effort is needed for consistency; make it a framework-level default with automatic retry" (L569, grounded, T1).
- The verdict against L471 still stands, on narrower grounds. Declarative unique, exclusion and foreign-key constraints are concurrency-safe at any isolation level, and they hold for owner-run migrations, which a function's privilege wall does not cover.

**Fix.**
- GUARD.2: multi-row rules beyond declarative constraints (prefer exclusion constraints and partial unique indexes first: L174, L175) run under Serializable with retry, or lock the governing row before checking. The trigger asserts the isolation level.
- Restate the ground against L471 as "procedural checks need serializable isolation or a lock, and only declarative constraints bind every writer".
- Hand the isolation default to the DATA judge with this constraint. My recommendation for that judge is L568 (a), Serializable with retry as the default (inferred, from L569 and the PostgreSQL page).

### F5 (major) The default context is used inconsistently

**Node**: default context (records.md); ALLOCATION.RECORD.2, GUARD.2, ACT.1, ACT.4; PIG-WEB.ALLOCATION.ROW_SECURITY.

**What is wrong (grounded in the records).**
- The context assumes "the Python backend is the only database consumer".
- Yet GUARD.2 argues that "a migration or console writing the table skips it", and ACT.4 rejects application audit "when consoles, migrations or bulk SQL write". These verdicts rely on other writers existing.
- RECORD.2 permits a read-only reporting *role* (L044 names only a reporting *copy*), which is also "base tables as a contract" for a consumer outside the owner, and RECORD.2's own forbidden list excludes exactly that.
- Q1 and ACT.1 rely on there being no such paths.
Each verdict may be right on its own, but they assume different worlds.

**Fix.** List the access paths of the default context explicitly:
- the backend request role (non-owner);
- an owner role for migrations (bypasses row security by design, L310);
- operator consoles (state whether they exist and under which role);
- reporting, as a separate copy by default; a reporting role on the live database only under row security.

Then re-check GUARD.2, ACT.4, RECORD.2 and Q1 against that one list.

### F6 (major) The matrix labels judgments "grounded"

**Node**: allocation_matrix.md, certainty column.

**What is wrong.** The matrix defines *inferred* as "it follows from grounded rows but no source states it, or it is a judgment between positions". By that definition these lines are mislabelled "grounded":
- ACT.1: a verdict against the doctrine (L584), resting on L214, which is contested and inferred.
- GUARD.1: its records say "the reconciliation of P1 and P2 is mine".
- ACT.4: it rests on L627 (inferred) and L684 (see F12).
- DERIVE.1: it rests on L625 (inferred), with the order of options the judge's own.
The matrix is what the maintainer reads first, so grounded labels on contested judgments steer attention away from them.

**Fix.**
- ACT.1: "grounded (database band); inferred (backend default against L584)".
- GUARD.1: "inferred (reconciliation)".
- ACT.4: "inferred (trigger over application audit)".
- DERIVE.1: "inferred (order of options)".

### F7 (minor) CACHE_STORE stretches L534 past its own scope

**Node**: PIG-WEB.ALLOCATION.CACHE_STORE; the "doctrine over research" list.

**What is wrong.**
- L534 covers derived-data caches and says sessions and request-scoped data stay out of them.
- The ledger's own note on L534: "distinct from L417 and L420, which concern response and process-level caches" (grounded).
- The judge uses L534 to set Postgres for every cache shared by processes and lists it as "L534 over L417's named stores". For response and fragment caches no doctrine row speaks.

**Fix.**
- Derived-data caches go in Postgres (L534, doctrine, max).
- For response caches, Postgres is the default under POSTGRES_FIRST (L125, inferred), with a measured-latency trigger.
- Drop the response-cache part from the "doctrine over research" list.

### F8 (minor) ACT.1 leaves the costs of its verdict against L584 unweighed

**Node**: ALLOCATION.ACT.1.

**What is wrong.**
- The verdict may stand, but the record weighs only changeability.
- A multi-statement backend use case pays one round trip per statement (L614, grounded) and holds its locks across those round trips. That lengthens lock time and, under Serializable (F4), raises retries (inferred).
- "Testable in memory (L042)" is weaker here than claimed: GUARD.2 puts the invariants in the database, so meaningful tests of the use case need it anyway.
- L596's "authoritative writer *function*" is silently read as a backend writer. Nothing but convention stops a second writer, unless the request role loses UPDATE on state columns (inferred).

**Fix.**
- Add the round-trip and lock-duration cost to Forces.
- Add "latency-critical multi-statement operations" to Moved by.
- Say explicitly that L596 is realised in the backend in the default, with legality and history guarded by the database.
- Name column privileges as the enforcement when more than one entry point exists.

### F9 (minor) TYPE_CHAIN assumes a JSON API although the default browser contract is HTML

**Node**: PIG-WEB.ALLOCATION.TYPE_CHAIN vs ALLOCATION.PRESENT.1.

**What is wrong (grounded in the records).** The chain ends in "TypeScript types generated, build-time only" as if the browser consumed JSON. PRESENT.1 decides server-rendered HTML.

**Fix.** Start the default interface chain at form and query input parsed into Pydantic models (GUARD.1), and the agent surface (F2). The TypeScript link applies to islands only.

### F10 (minor) FORCES sets no order among the forces that choose

**Node**: ALLOCATION.FORCES.

**What is wrong.**
- "Changeability, performance and scalability choose" among admissible tiers, but no order or criterion is given among them.
- ACT.1 and TYPE_CHAIN were both settled on changeability without saying why it beats performance or contract quality. That is where averaging can hide.

**Fix.** State the criterion: the force whose loss the receiving tier cannot repair later. Otherwise mark each such choice inferred and name the force that was preferred.

### F11 (minor) Collation has no owner, and the browser re-sort copy can contradict it

**Node**: ALLOCATION.PRESENT.2, ALLOCATION.DERIVE.2.

**What is wrong.**
- PRESENT.2 sends collation to DERIVE.2, and DERIVE.2 marks it "open". No node decides it.
- DERIVE.2 permits a browser re-sort over loaded rows. With a different collation, the browser re-sort orders rows differently from the server's pages (inferred).

**Fix.**
- The database owns the collation for any order it serves (declared per column or per query).
- The browser copy re-sorts with the same locale or not at all.
- Keep the choice of collation open under DATA.

### F12 (minor) ACT.4 cites a ledger row marked grounded with no source

**Node**: ALLOCATION.ACT.4; ledger row L684.

**What is wrong.** L684 is "consensus | grounded" with an empty sources column.

**Fix.** Flag it to the ledger owner. Until it is fixed, ACT.4 rests on L627 (inferred) and L212 (grounded for the mechanism).

## Placements checked and found sound

- ALLOCATION (root roll-up): three-line allocation consistent with the records; it changes only where F1 to F3 apply.
- FORCES.1, FORCES.2: veto forces stated from rows owned elsewhere; gap marked honestly.
- FORCES.3: placement-by-design for data reduction, measurement for the rest.
- FORCES.4: latency justifies copies, never authority.
- FORCES.5: correctly `speculative` (L615 has no source).
- FORCES.6: L472 as the max is sound.
- CONTEXT: variables and directions sound; add access paths per F5.
- RULES.1 to RULES.5: compatible with each other. RULES.1 is broken only by the hand mirrors of F3.
- RECORD.1: database as the single system of record, with local-first and log-derived kept as "wins when". Max for correctness.
- RECORD.2: owner-operations and the function API for several backends are sound. Only the reporting role conflicts (F5).
- GUARD.1: parse at every deserialisation point, meaning with the state; sound (label per F6).
- GUARD.2: declarative constraints required, against L471; sound. Multi-row branch per F4.
- GUARD.3: two layers with the backend as authority; sound. Second line per F1.
- GUARD.4: opaque revocable server session, backend-for-frontend, bearer tokens only for non-browser clients; the max for security.
- GUARD.5: the database detects and the policy follows the data shape; sound (isolation per F4).
- GUARD.6: key and effect in one transaction, unique backstop; sound.
- ACT.1: the verdict against L584 holds for the default; costs per F8, label per F6.
- ACT.2: outbox, atomic phases for foreign mutations, no remote call in an open transaction; sound.
- ACT.3: core writes synchronous, deferred work staged in Postgres; the 1 s threshold is flagged by the judge and is defensible (L013).
- ACT.4: trigger history, actor from verified identity, separate security log; sound (label per F6).
- DERIVE.1: computed on read, then same transaction, then cache table with stated staleness; sound.
- DERIVE.2: set-based in the database, keyset paging, server page cap; sound (collation per F11).
- DERIVE.3: every cache a copy with a staleness bound; sound.
- PRESENT.1: server-rendered HTML default with islands by L253's criteria; a judgment, correctly marked inferred.
- PRESENT.3: state by lifetime and sharing; sound.
- PIG-WEB.ALLOCATION.POSTGRES_FIRST: Postgres per role until a measured limit, NOTIFY as wake-up only; sound.
- PIG-WEB.ALLOCATION.DB_API: L516 ladder, function API for several backends, views off the contract; sound.
- PIG-WEB.ALLOCATION.JOB_HOST: queue table with SKIP LOCKED, scheduler for data work, stage-then-drain past the limit; sound.
- PIG-WEB.ALLOCATION.JS_SERVER: no request-time JavaScript server in the default; sound, gap marked.
