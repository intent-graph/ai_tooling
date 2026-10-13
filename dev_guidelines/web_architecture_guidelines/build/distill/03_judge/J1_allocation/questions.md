# J1 ALLOCATION: questions for the maintainer (revision 3)

Only the genuine trade-offs: choices where maximising one force the node serves costs another it also serves, and which neither the evidence nor a maintainer decision settles. The default context is set by MD-03: a classic website, one team, JavaScript + Python + Postgres, single tenant, humans and agents as users, and a database shared by several backends and by BI, consoles and scripts. Every other placement is decided in `records.md` and `allocation_matrix.md`.

Pinned:
- Questions: 1, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (Q1, ALLOCATION.GUARD.3; a scope check on MD-01, whose "database privileges per role" and MD-03's "per-role privileges" leave per-user reads to each backend; row security stays excluded, functions are not). Recorded default: each backend filters from one shared specification with shared denial tests; fallback: database read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends, which MD-03 makes the default case. Per-user write rules are decided: the writer function (R1-1). The former question on row security is closed by MD-01.
- Placements: 26; decided 25, undecided 1 (ALLOCATION.GUARD.3, one clause: read visibility of rows that carry per-user rules).

Closed:
- The former row-security question is decided by MD-01: no row-level security by default, acceptable only under its three conditions.
- Per-user **write** rules are decided under MD-03 (R1-1). A rule that can be decided from the stored row and the acting user ("only the assignee may close a task") is decided by the column's writer function, and a backend's identical check is a generated or tested copy.

## Q1 Who filters reads of rows that carry per-user rules, when several backends share the database

State: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.

**Decision**: a read rule such as "a draft is visible only to its author", which every backend must respect. Comments are covered by the same rule: a comment on a restricted target, or a private comment, is a row with a per-user read rule. Is it filtered by each backend, or by read functions in the database API that every consumer passes through?

**My recommendation**: B, read functions. If you do not answer, the graph records A, MD-01 as written, and keeps ALLOCATION.GUARD.3's read-visibility clause `undecided`.

**What this asks**: a scope check on MD-01, not a gap between two decisions. MD-01: "Authorization stays a backend decision with database privileges per role as the second gate". MD-03 lists among what lives in the database "per-role privileges", not per-user rules. Read literally, the two decisions put per-user read filtering in each backend, which is A. The question is whether MD-01's scope was meant to cover per-user reads once MD-03 makes several backends the default. MD-01 excludes row-level security; it does not exclude functions, and B uses functions only.

**Consequence under either answer** (X1): roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted. No statement in this guideline claims stronger visibility than this.

**Already decided either way**:
- each backend decides product policy and identity; the database bounds every consumer by its role (MD-01, L468);
- per-user write rules belong to the writer functions (R1-1);
- every write carries an actor, its pairing with the session role is checked, and audit records both (R1-3);
- no row-level security by default (MD-01).

**Positions**:
- **A. Each backend filters reads (MD-01 as written).** Serves changeability: read policy stays in application code, tested in memory, changed at the backends' cadence (L620, L042). Costs: one copy of each read rule per backend, possibly in different languages; a backend that drifts or forgets the filter leaks rows (against RULES.4, L633). Any role with SELECT on the table, BI and operator roles included, sees every user's rows in the columns it is granted. Mitigation if chosen: one written specification per rule, and a shared denial test suite every backend runs.
- **B. Read functions in the API filter by the acting user.** Tables carrying such rules are readable only through these functions; consumer roles get no direct SELECT on them. Serves security: one implementation that every consumer passes through, so no backend can forget or drift (L608, L633, MD-03). B does not verify who the user is. The function filters by the actor the consumer sets in the transaction-local setting, which is still each consumer's claim (R1-3), so B stops forgotten and drifted filters, not a consumer that sets the wrong actor. Costs: read policy in SQL, tested against a live database and changed through migrations (L042, L472, L620); those tables lose L516's direct-read shortcut, for backends and for BI alike. BI and operator roles keep full visibility only if they are given their own unrestricted functions or grants; otherwise they are restricted as well, which has to be decided per role.

**Why it is a genuine trade-off**: the node serves security, and B is the more demanding practice for it. B costs changeability, which the authorization placement also serves, since policy that changes often belongs where it can change fast (L620). B also widens what the database decides beyond what MD-01 and MD-03 state.

**What would make A the clear answer**: only one backend reads tables with per-user rules, while the others and BI read other data or aggregates; or read policy changes much faster than the schema.

**If unanswered, the graph records**: A as the recorded default (each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs); the fallback kept and not forbidden: "database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends". Under MD-03 several backends share the database by default, so that condition always holds: the fallback is available wherever the default context applies. "Verified" means verified by the backend that asserts the actor; to the database it is a claim (R1-3). On ALLOCATION.GUARD.3: `epistemic_state: "undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database | known: two layers per MD-01; write rules in writer functions (MD-03) | conflict: L619, L688 favour row security when several consumers share the database (MD-03)"`.
