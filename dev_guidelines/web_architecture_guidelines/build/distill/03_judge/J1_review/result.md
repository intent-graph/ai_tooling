# Result: adversarial review of the J1 ALLOCATION verdicts

## L1 headline

The J1 allocation mostly holds: 21 of its 26 placements are sound, some with minor fixes. Two verdicts must change before the eight tier judges build on them. Q1 (row security) uses a false argument and an averaged recommendation. The code-first default for API types is a convenience default, not the max choice. Four more issues are major.

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

### Revision 1 check

Revision 1 applies the three maintainer decisions faithfully and lands every earlier fix. It leaves one blocking gap: per-user write rules (such as "only the assignee may close a task") are claimed by both the backend (GUARD.3) and the database writer function (ACT.1). Closing that gap also narrows the new Q1 to read visibility. Details are in `review_r1.md`.

Pinned:
- Revision 1 findings: 9. Blocking 1: R1-1 GUARD.3 and ACT.1 give per-user write rules two authorities (backend per user and action; writer function with the actor). Major 3: R1-2 Q1 is over-broad and overstates B; R1-3 the actor that audit and functions trust is set by any consumer; R1-4 no rule on whether a backend may wrap several API calls in one transaction. Minor 5: R1-5 RECORD.2 and DB_API disagree on direct writes; R1-6 owner-run jobs bypass the single writer; R1-7 MD-02's drift gate not applied to the function API; R1-8 CONTEXT makes code the residual origin; R1-9 Serializable not bound per consumer role.
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully; MD-02 wording tilts in one CONTEXT row (R1-8).
- Earlier fixes: F3, F4, F6, F7, F8, F9, F10, F11, F12 landed as intended; F1, F2, F5 correctly replaced by MD-01, MD-02, MD-03.
- Verdict on new Q1: a genuine trade-off for read visibility only (security against changeability), not for writes, which MD-03 and ACT.1 already place in the writer functions. Narrow it to reads, say it asks the maintainer to revisit MD-01's scope (MD-03 lists "per-role privileges", not per-user rules), and state that B removes forgotten or drifted checks but still trusts the actor each consumer sets. Recommendation B for read visibility stands as the max for security.

## L2 claims

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

Claims:
1. **Q1's case for B does not hold as written.** *Inferred (logic) and grounded (the judge's own records).*
   - Two gates in conjunction cannot leak more than the backend alone. The drift argument is wrong.
   - The transaction-local actor (ACT.4) and the non-owner request role (GUARD.3) are already required, so A's real extra cost is the policies, their indexes and the denial tests.
   - "B is what the evidence recommends" is agreement used as the verdict, which the max rule forbids. L310 records that the sources do not settle the question.
2. **The code-first default fails the judge's own condition.** *Grounded on L634, L635, L548 and SRC-241, read for this review; the application to agents is inferred.*
   - The judge rejects design-first except for independent consumers. In the default, agents (users' own hosts) are the main readers of the JSON contract, because the browser gets HTML.
   - "Zero drift" does not separate the positions: design-first with generated or CI-checked models also has one origin.
   - The OpenAPI Initiative: "The importance of using Design-first cannot be stressed strongly enough". Code-first gives "unintuitive and incomplete descriptions".
3. **Facts need one origin, not shapes.** *Grounded on L486; the application to cross-tier types is inferred.*
   - Enum values, lengths and nullability have two origins under RECORD.3.
   - Persistence models and validators are hand mirrors, which RECORD.3 and TYPE_CHAIN themselves forbid. A stricter mirror decides, which breaks RULES.1.
4. **GUARD.2's multi-row branch needs Serializable or a lock.** *Grounded: the PostgreSQL docs, read for this review, and L569, L577.*
   - A trigger or function that reads other rows is check-then-write under Read Committed. PostgreSQL calls rule enforcement there "very difficult" and recommends Serializable or explicit locks.
   - The judge did not cite L568 or L569. The verdict against L471 stands on narrower grounds: only declarative constraints bind every writer at any isolation level.
5. **The default context assumes different worlds in different verdicts.** *Grounded in the records.*
   - GUARD.2 and ACT.4 rely on consoles and migrations writing the data. Q1 and ACT.1 rely on the backend being the only consumer.
   - RECORD.2's reporting role is an access path that skips the backend, and also a base-table contract its own forbidden list excludes.
6. **Certainty labels are inflated in the matrix.** *Grounded: the matrix's own legend.* ACT.1, GUARD.1, ACT.4 and DERIVE.1 are judgments between positions, labelled "grounded".
7. **Minor issues.** *Mostly grounded; F8 and F11 inferred.*
   - L534 is used beyond its scope for response caches.
   - ACT.1 leaves its round-trip and lock-duration costs unweighed, and reads L596's writer "function" as a backend writer.
   - TYPE_CHAIN assumes a JSON browser API.
   - FORCES gives no order among changeability, performance and scalability.
   - Collation has no owner.
   - L684 has no source.
8. **Sound: 21 of the 26 placements, plus the 13 forces, context and rules nodes** (listed in `review.md`); the 8 roll-ups follow their children. They include the main verdicts against the doctrine: GUARD.2 against L471, and ACT.1 against L584 in the default context. *Grounded on the cited rows.*
9. **Open.**
   - Which generators fit the stack (OpenAPI to Pydantic, live schema to persistence models). None was read.
   - Whether the default's agents are the users' own hosts or the team's programs. This is a context fact for the maintainer.

### Revision 1 check

Pinned:
- Revision 1 findings: 9. Blocking 1: R1-1 GUARD.3 and ACT.1 give per-user write rules two authorities (backend per user and action; writer function with the actor). Major 3: R1-2 Q1 is over-broad and overstates B; R1-3 the actor that audit and functions trust is set by any consumer; R1-4 no rule on whether a backend may wrap several API calls in one transaction. Minor 5: R1-5 RECORD.2 and DB_API disagree on direct writes; R1-6 owner-run jobs bypass the single writer; R1-7 MD-02's drift gate not applied to the function API; R1-8 CONTEXT makes code the residual origin; R1-9 Serializable not bound per consumer role.
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully; MD-02 wording tilts in one CONTEXT row (R1-8).
- Earlier fixes: F3, F4, F6, F7, F8, F9, F10, F11, F12 landed as intended; F1, F2, F5 correctly replaced by MD-01, MD-02, MD-03.
- Verdict on new Q1: a genuine trade-off for read visibility only (security against changeability), not for writes, which MD-03 and ACT.1 already place in the writer functions. Narrow it to reads, say it asks the maintainer to revisit MD-01's scope (MD-03 lists "per-role privileges", not per-user rules), and state that B removes forgotten or drifted checks but still trusts the actor each consumer sets. Recommendation B for read visibility stands as the max for security.

Claims:
1. **The maintainer decisions are applied faithfully.** *Grounded: the records and the decisions file.*
   - MD-01: no row security by default, its three conditions reproduced as stated.
   - MD-02: always in sync by process, with criteria for both origin directions.
   - MD-03: the function API is the default contract; multi-table operations, per-role privileges and audit are in the database; L584 stands.
   - Tensions with the evidence are recorded, not hidden.
2. **R1-1 (blocking): two authorities for per-user write rules.** *Grounded in the records.*
   - GUARD.3 makes the backend the authority per user and per action. The same record, together with ACT.1, lets the writer function decide ownership and transitions with the actor.
   - Fix: a rule decidable from the row and the actor that must hold for every consumer belongs to the writer function, and the backend's check is a tested copy. The backend decides product policy not stored in the data.
3. **R1-2 (major): Q1 is over-broad.** *Grounded on MD-01, MD-03 and the records; the security point is inferred.*
   - Writes are decided by R1-1, so only read visibility is open.
   - MD-03 lists "per-role privileges" in the database. Q1 is therefore a scope check on MD-01 and should say so.
   - B guarantees one implementation, but the actor it filters on is still each consumer's claim. BI keeps full visibility unless it is restricted too.
4. **R1-3 (major): the actor is set by every consumer.** *Inferred (any Postgres session can set a custom setting).*
   - Audit and functions trust a transaction-local actor that backends, scripts and owner jobs all set.
   - Fix: record the session role and the claimed actor; refuse writes with no actor; state which roles may assert an end user.
5. **R1-4 (major): the unit of work is unstated.** *Grounded in the records; the consequence is inferred.*
   - Fix: one business operation is one function call in its own transaction. Backends never wrap several calls. Workflows across operations advance through state columns and the outbox.
6. **Minor (R1-5 to R1-9).**
   - R1-5: align RECORD.2 with DB_API's direct-write exception.
   - R1-6: owner-run jobs call writer functions or are recorded exceptions under L545; state the operator role's reads.
   - R1-7: a CI gate on non-additive function-signature changes (MD-02 applied to the function API, L517).
   - R1-8: CONTEXT's "(otherwise code as origin)" reworded.
   - R1-9: Serializable set per consumer role, and writer functions assert the isolation level (L573).
7. **Earlier fixes landed.** *Grounded.* F3, F4, F6 to F12 landed as proposed; F1, F2 and F5 are replaced by the maintainer decisions. The table is in `review_r1.md`.
8. **New maintainer questions: none.** Q1 stays, narrowed per R1-2. R1-1 and R1-4 are judge fixes, not questions.

## L3 full

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

**Scope and method.** I reviewed every node of `../J1_allocation/records.md`, the matrix, `questions.md` and `result.md` against `../../target_hierarchy.md` (the max rule). For each cited row I checked that it supports the verdict, in `../../02_skeleton/claims_ledger.md`. I also opened the research claims behind the type-chain rows: API-C12 in `research/03_contract`, DCON-C06 and DCON-C12 in `research/17_data_contracts`, and AGENT-C03 in `research/19_agent_users`. Two sources I read directly:
- the OpenAPI Initiative best-practices page (SRC-241);
- the PostgreSQL page "Data Consistency Checks at the Application Level" (the T1 family of SRC-331 and SRC-337).

I edited none of the judge's files and launched no research.

**Full findings.** Each finding, with its severity, node, evidence (row ids and quotes) and proposed fix, is in `review.md` in this folder (F1 to F12). In short:
- **F1 (blocking, Q1).** A conjunctive second gate cannot weaken security, so the drift argument is wrong. A's listed costs are already paid by ACT.4 (L566, L311) and GUARD.3 (L310). The recommendation rests on the agreement of L688, L620 and L468. "Single tenant weakens A" ignores the per-user rule of L306. RECORD.2's reporting role already meets the trigger. Fix: recommend A scoped to tables with per-user visibility, with B acceptable when no such table exists and only the request role reads.
- **F2 (blocking, RECORD.3, TYPE_CHAIN).** The judge's own condition (independent consumers) is met by agents (L634, L635) while the browser takes HTML (PRESENT.1). The drift argument is a tie. SRC-241 and L272 favour design-first, and the code-first condition is inferred in L548. Fix: the description is written first and is the origin; models are generated from it or CI-checked; the generator is open.
- **F3 (major).** L486 asks for one source per fact. Persistence models (L495) and validators (GUARD.2) are hand mirrors that the judge's own forbidden lists exclude, and they break RULES.1. Fix: stored facts originate in the schema; persistence models are generated from the live schema (L474); hand mirrors with a CI comparison are acceptable only when no generator fits.
- **F4 (major).** Multi-row triggers and functions are check-then-write under Read Committed (PostgreSQL docs; L577 write skew). L568 and L569 were missed. Fix: Serializable with retry, or a lock on the governing row, for procedural multi-row rules. The verdict against L471 is restated on declarative constraints, and the isolation default goes to the DATA judge with L568 (a) recommended.
- **F5 (major).** Fix: list the default's access paths once (request role, migration owner, consoles, reporting copy) and re-check GUARD.2, ACT.4, RECORD.2 and Q1 against that list.
- **F6 (major).** Fix: relabel ACT.1, GUARD.1, ACT.4 and DERIVE.1 as inferred where they are judgments.
- **F7 to F12 (minor).**
  - F7: restrict L534 to derived-data caches; response caches go in Postgres under POSTGRES_FIRST, inferred.
  - F8: add round-trip and lock-duration costs to ACT.1, and name column privileges for L596.
  - F9: start the chain at form input; TypeScript applies to islands only.
  - F10: state the order or criterion among the forces that choose.
  - F11: the database owns collation, and the browser re-sorts with the same locale or not at all.
  - F12: flag L684's missing source.

**Sound: 21 of the 26 placements, plus 13 other nodes.** The ALLOCATION roll-up; FORCES.1 to FORCES.6; CONTEXT; RULES.1 to RULES.5; RECORD.1; RECORD.2 except its reporting role; GUARD.1, GUARD.2 (the declarative part), GUARD.3 (two layers), GUARD.4, GUARD.5, GUARD.6; ACT.1 (with F8), ACT.2, ACT.3, ACT.4; DERIVE.1, DERIVE.2, DERIVE.3; PRESENT.1, PRESENT.3; POSTGRES_FIRST, DB_API, JOB_HOST, JS_SERVER. One line each, in `review.md`. Placements that need change (5): RECORD.3, TYPE_CHAIN, ROW_SECURITY, PRESENT.2 (collation), CACHE_STORE (scope).

**Process.** This is one Opus reviewer's view and has not been reviewed itself. The F2 and F1 recommendations reverse a flagged judge reading and a judge recommendation, so the maintainer decides both.
