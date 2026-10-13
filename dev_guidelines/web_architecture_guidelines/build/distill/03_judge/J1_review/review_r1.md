# J1 ALLOCATION revision 1: review

This review checks revision 1 of `../J1_allocation/` against the maintainer decisions in `../../maintainer_decisions.md` (MD-01, MD-02, MD-03) and against my first review (`review.md`, F1 to F12). It covers:
- `result.md` (its "Revision 1" subsections), `allocation_matrix.md` and `questions.md`;
- in `records.md`: the default context, CONTEXT, RULES, FORCES, RECORD.2, RECORD.3, GUARD.1 to GUARD.3, ACT.1, ACT.4, DERIVE.3, DB_API, TYPE_CHAIN, ROW_SECURITY and CACHE_STORE.

The maintainer decisions are not under review. I checked that they were applied faithfully and that the verdicts built on them hold. Evidence ids `Lnnn` resolve in `../../02_skeleton/claims_ledger.md`.

Certainty: **grounded** means I read it. **Inferred** means it follows from the records, the rows or Postgres behaviour, but no source in the ledger states it.

Pinned:
- Revision 1 findings: 9. Blocking 1: R1-1 GUARD.3 and ACT.1 give per-user write rules two authorities (backend per user and action; writer function with the actor). Major 3: R1-2 Q1 is over-broad and overstates B; R1-3 the actor that audit and functions trust is set by any consumer; R1-4 no rule on whether a backend may wrap several API calls in one transaction. Minor 5: R1-5 RECORD.2 and DB_API disagree on direct writes; R1-6 owner-run jobs bypass the single writer; R1-7 MD-02's drift gate not applied to the function API; R1-8 CONTEXT makes code the residual origin; R1-9 Serializable not bound per consumer role.
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully; MD-02 wording tilts in one CONTEXT row (R1-8).
- Earlier fixes: F3, F4, F6, F7, F8, F9, F10, F11, F12 landed as intended; F1, F2, F5 correctly replaced by MD-01, MD-02, MD-03.
- Verdict on new Q1: a genuine trade-off for read visibility only (security against changeability), not for writes, which MD-03 and ACT.1 already place in the writer functions. Narrow it to reads, say it asks the maintainer to revisit MD-01's scope (MD-03 lists "per-role privileges", not per-user rules), and state that B removes forgotten or drifted checks but still trusts the actor each consumer sets. Recommendation B for read visibility stands as the max for security.

## Findings

### R1-1 (blocking) Per-user write rules have two authorities

**Node**: ALLOCATION.GUARD.3, ALLOCATION.ACT.1 (and Q1's example).

**Issue (grounded in the records).** For a rule like "only the assignee may close a task", two records each claim the decision:
- GUARD.3 makes each backend the authority "per user and per action: who the human or agent is and what they may do on which record".
- The same record lets functions use the acting user "for rules about the data (legal transitions, ownership recorded on the row)".
- ACT.1 puts every state transition in its single writer function, in the database (MD-03, L596).

Q1 then offers that example as undecided. RULES.1 allows one authority per responsibility. As written, this one has two, and neither record says which one is the copy.

**Evidence**: GUARD.3, "Functions … use it for audit and for rules about the data (legal transitions, ownership recorded on the row)". ACT.1, "state transitions, each state column with exactly one authoritative writer function". MD-03: "Everything that must hold whoever touches the data lives in the database". `questions.md`, Q1 example "only the assignee may close a task".

**Fix.** Draw the line by where the rule's facts live (inferred, from MD-03 and L608):
- A write rule that can be decided from the stored row and the acting user (author, owner, assignee), and that must hold for every consumer, is decided by the writer function. A backend's identical check is a copy, kept for early feedback, and must be generated or tested under RULES.1.
- The backend is the authority for product policy that is not stored in the data: product roles, plan limits, feature flags, workflow steps.

Write this line into GUARD.3, ACT.1 and the matrix. It also removes writes from Q1 (R1-2).

### R1-2 (major) Q1 is broader than the trade-off and overstates B

**Node**: `questions.md` Q1; ALLOCATION.GUARD.3 (undecided clause).

**Issue.**
1. *Writes are already decided.* By MD-03 and ACT.1, together with R1-1's line, per-user write rules belong to the writer functions. What remains open is read visibility: "a draft is visible only to its author". Grounded in the records.
2. *The maintainer's own text points to A, and Q1 does not say so.* MD-01: "Authorization stays a backend decision with database privileges per role as the second gate". MD-03's list of what lives in the database names "per-role privileges", not per-user rules. Q1 is therefore a request to revisit MD-01's scope in light of MD-03, not a gap between the two decisions, and it should say that. Grounded in the decisions file.
3. *B's security gain is overstated (inferred).*
   - Under B, the function filters by the actor from the transaction-local setting.
   - Postgres lets any session set such a setting, so the function trusts whatever actor each consumer supplies.
   - L311's "derive the value from the verified identity" is met by the backend, not by the database.
   - B therefore removes forgotten or drifted checks (one implementation, every consumer passes through it). It does not protect against a consumer that sets the wrong actor.
4. *B's read cost is only partly stated.*
   - B removes direct SELECT on those tables for every consumer role. That cuts into L516's "simple reads may query base tables" (DB_API), and it removes BI's direct reads too.
   - Otherwise the BI role still sees every user's rows, the cost listed against A.
   - Q1 mentions "administrator and BI paths need explicit functions or grants", but not that BI keeps full visibility unless it is restricted as well.

**Fix.**
- Narrow Q1 to read visibility of rows that carry per-user rules.
- Quote MD-01 and MD-03's "per-role privileges" and present the question as a scope check on MD-01.
- Restate B's gain as "one implementation every consumer passes through; the actor is still each consumer's claim".
- Add the BI consequence to both positions.
- Keep the recommendation B for read visibility. It is the more demanding practice for security, and the trade-off is genuine: it costs changeability (L042, L472, L620), which the placement also serves.

### R1-3 (major) The actor that audit and functions rely on is set by every consumer

**Node**: ALLOCATION.ACT.4, ALLOCATION.GUARD.3 (functions), ALLOCATION.ACT.1; default context.

**Issue.** Several places use the acting user read from a transaction-local setting (L311, L566): audit, transition logging, ownership checks in functions, and Q1-B. Under MD-03 that setting is written by several backends, consoles, scripts and owner-run jobs. The database can verify only the consumer role, not the claimed actor (inferred: Postgres lets any session set a custom setting). Consequences:
- an owner-run data job that does not set the actor writes history with no actor;
- a misconfigured script can attribute its writes to any user.

L311 itself ("never from a client-supplied id") is about the backend's input; between consumer and database, the setting is client-supplied.

**Evidence**: ACT.4, "actor from the verified identity in a transaction-local setting (L566 MAINT, L311)". The access-path table in `records.md` (default context). L545 (human-run jobs carry a ticket id).

**Fix.**
- Audit and transition logs record both the database-verified consumer (the session's role) and the claimed actor.
- Writer functions and audit triggers refuse a write when no actor is set. Owner-run jobs set the operator and the ticket id (L545).
- The default context states which consumer roles are trusted to assert an end-user actor (backends) and which assert only themselves (BI, consoles, scripts). The trigger checks that pairing (inferred).

### R1-4 (major) The unit of work across backend and functions is unstated

**Node**: ALLOCATION.ACT.1, ALLOCATION.RULES.5.

**Issue (grounded in the records; consequence inferred).** ACT.1 forbids "multi-table writes composed in a backend". It says "L066's boundary is the function's transaction when the operation is one call", which leaves open what happens when a use case calls two functions. Either answer has a consequence:
- If a backend may wrap several calls in one transaction, it composes a multi-table write after all, and the transaction boundary has two owners (L066 against L584).
- If it may not, a workflow across operations is not atomic, and the guideline must say how it converges.

RULES.5 says the function API "makes one call" of a cross-table transaction, but does not forbid wrapping.

**Fix.** State the rule:
- One business operation is one function call in its own transaction. Backends do not open a transaction around several API calls.
- A workflow step that needs atomicity with another step is a new business operation, so a new function.
- Workflows across operations advance through state columns and the outbox (ACT.2), with idempotent steps (GUARD.6).

Add this to ACT.1, RULES.5 and the matrix's forbidden column (inferred; L066, L584, L623).

### R1-5 (minor) RECORD.2 and DB_API disagree on direct writes

**Node**: ALLOCATION.RECORD.2, PIG-WEB.ALLOCATION.DB_API.

**Issue.** RECORD.2: "Backends, consoles and scripts write only through the API functions". DB_API and both matrix lines allow "a direct single-table write grant … for a table that only one consumer writes and that has no state column or multi-table effect".

**Fix.** Align RECORD.2's decision text with DB_API's exception.

### R1-6 (minor) Owner-run jobs bypass the single writer; the operator role's reads are unstated

**Node**: ALLOCATION.ACT.1, default context.

**Issue.**
- ACT.1: "every entry point (backends, consoles, ingestion, agents through a backend) routes through" the writer function. The owner role, used for migrations and human-run data jobs, holds every privilege and bypasses the writer functions and the column revokes. Triggers and constraints still bind it (GUARD.2).
- The operator role for consoles and scripts gets EXECUTE but no stated SELECT.

**Fix.**
- Owner-run jobs that change a state column call its writer function, or are recorded exceptions under L545's checklist, with the actor set (R1-3).
- State the operator role's read grants.

### R1-7 (minor) MD-02's drift gate is not applied to the function API

**Node**: ALLOCATION.RECORD.3, PIG-WEB.ALLOCATION.DB_API.

**Issue.**
- Under MD-03, the function API is the default contract to the data. RECORD.3 generates its documentation from the live database (L474), so the documentation cannot drift.
- MD-02's process also asks for review rules and a CI/CD gate. For the function API that means a gate that fails on a non-additive signature change, which is how L517's additive evolution gets enforced. Neither record states one.

**Fix.**
- Apply MD-02 to the function API: a catalogue diff in CI that fails on a removed function or an incompatible signature, unless the change is marked as coordinated (L517).
- Generate the backends' typed wrappers from the same catalogue (TYPE_CHAIN already does).

### R1-8 (minor) CONTEXT makes code the residual origin

**Node**: ALLOCATION.CONTEXT, last row.

**Issue.** "Interface description as origin (otherwise code as origin)" turns MD-02's per-project choice into a default with an exception. RECORD.3 states criteria for both directions, which is faithful.

**Fix.**
- Reword the row: "description or code as origin, recorded per project by RECORD.3's criteria".
- Optionally state how those criteria fall for the default context. Agents as users, read by hosts the team does not control, point to description first, but the project records the choice.

### R1-9 (minor) Serializable is not bound per consumer role

**Node**: ALLOCATION.GUARD.2 (hand-off to the DATA judge).

**Issue.**
- With several consumer roles, any role that writes at a lower isolation level voids the Serializable guarantee (L573). The trigger assertion covers writes that reach a trigger, but not writer functions without one.
- BI reads on a replica cannot be Serializable (L573).

**Fix.** In the DATA hand-off:
- set the default isolation per consumer role;
- have writer functions assert the isolation level, as triggers do;
- state that reports on a replica accept snapshot anomalies.

## Earlier findings: did the fixes land?

| finding | status | where |
|---|---|---|
| F1 Q1 row security | replaced by MD-01, faithfully | ROW_SECURITY, GUARD.3, `questions.md` "Closed" |
| F2 interface origin | replaced by MD-02, faithfully; R1-8 is a wording tilt | RECORD.3, TYPE_CHAIN |
| F3 one origin per fact | landed | RECORD.3, RULES.1, GUARD.1, GUARD.2, TYPE_CHAIN |
| F4 multi-row rules under Read Committed | landed; R1-9 extends it | GUARD.2 (Serializable or lock, trigger asserts isolation, exclusion and partial unique first) |
| F5 default context | replaced by MD-03 with an access-path table | `records.md` default context |
| F6 certainty labels | landed | matrix: GUARD.1, DERIVE.1 inferred; ACT.1, ACT.4 marked MD-03 with tension |
| F7 L534 scope | landed | DERIVE.3, CACHE_STORE (response caches inferred, under L125) |
| F8 ACT.1 costs, single writer | landed; under MD-03 the costs favour the database | ACT.1 |
| F9 chain starts at HTML forms | landed | TYPE_CHAIN |
| F10 order of choosing forces | landed, marked as the judge's synthesis | FORCES |
| F11 collation | landed | DERIVE.2, PRESENT.2, matrix |
| F12 L684 without source | landed | ACT.4 evidence note |

## Checked and sound

- MD-01 in ROW_SECURITY and GUARD.3: the three conditions are reproduced as stated, the tension with L619 and L688 is recorded, and authorization stays two-layered.
- MD-02 in RECORD.3 and TYPE_CHAIN: always in sync by process, origin per project with criteria in both directions, one origin per fact.
- MD-03 in the default context, RECORD.2, ACT.1, DB_API and ACT.4: the function API is the default contract; L584 stands; audit and per-role privileges are in the database; tensions with L044, L622, L215 and L066 are recorded, not hidden.
- Direct BI and console paths: covered by the access-path table (BI read-only with column grants, operators through functions, owner never serving requests, browsers and agents never connecting). Gaps only as R1-3 and R1-6.
- RULES.1 (rejecting copies generated or tested), RULES.2 (L607's exception tied to MD-03), RULES.4 (two-level core): consistent with MD-03.
- GUARD.1 (the function API as a typed crossing), GUARD.2 (apart from R1-9), GUARD.5 and GUARD.6 (version and key recorded in the writer function): sound.
- ACT.2 (outbox written by the function, no external calls from the database), ACT.3, DERIVE.1 to DERIVE.3, PRESENT.1 to PRESENT.3: sound.
- POSTGRES_FIRST, JOB_HOST (queue row written by the function), CACHE_STORE, JS_SERVER: sound.
- The one remaining verdict against the doctrine (GUARD.2 against L471): sound on its narrowed grounds.
