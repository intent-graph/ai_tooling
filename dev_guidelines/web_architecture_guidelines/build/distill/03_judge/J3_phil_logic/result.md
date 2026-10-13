# J3 LOGIC (web-app-philosophy): result

The judge's verdicts on the 8 nodes of the `web-app-philosophy` LOGIC branch (the backend tier), under the max rule of `../../target_hierarchy.md`, building on the settled allocation (`../J1_allocation/allocation_matrix.md`) and the maintainer decisions MD-01 to MD-03 (`../../maintainer_decisions.md`). The adversarial review of the branch (`../review_logic/review.md`) and the cross-branch resolutions (`../cross_branch_fixes.md`) are applied. Each level below reads alone. Grounds per node: `records.md`; questions: `questions.md`.

## L1 headline

The backend is the trusted entry and the workflow tier: it authenticates and authorizes every caller, parses all input, bounds consumption, carries workflow and product policy in a core that calls the database function API once per operation (composition across domains happens inside the database), runs as stateless disposable processes, and exposes one HTTP interface per backend (HTML hypermedia for browsers, a described resource-oriented JSON interface for programs and agents, every interface description kept in sync). All 8 nodes decided; no question; no conflict with the allocation verdicts. The inherited read-visibility clause stays with the maintainer, now with J1's fallback (read functions) and its consequence for directly-reading roles stated. Review: 2 findings applied, 0 rejected.

Pinned:
- Nodes judged: 8 of 8 (LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE, LOGIC.EXPOSE.1, LOGIC.EXPOSE.2, LOGIC.EXPOSE.3); 2 are roll-ups owning no row (LOGIC, LOGIC.EXPOSE); 28 of 28 owned rows used.
- Decided 8, undecided 0, apart from one clause inherited from J1 and held in LOGIC.SECURE: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 0 (questions.md says none).
- Verdicts against the maintainer doctrine: 0; none of the 28 rows is a MAINT row; LOGIC.ENFORCE applies the doctrine rows L527, L584, L596 as J1 placed them under MD-03.
- Conflicts with J1 placements: 0. Three source positions narrowed to fit settled placements, recorded as tensions: L063 "testable without a live database" holds for the backend's own share only (ACT.1, MD-03); L066's use-case-owned transaction becomes one database function call per operation (ACT.1); strict client-held session state (Fielding's reading of L054) yields to the server-held revocable session (GUARD.4).
- Evidence gaps: (1) no row on hypermedia controls for agent clients; the JSON half of LOGIC.EXPOSE.3 is decided from MD-02 and L634, marked inferred; server-computed allowed actions for agents recorded as a candidate for the agent-surface judge; (2) L067 rests on one exploratory source, adopted only for its up-front data dependency half, inferred; (3) MFA required by default on human accounts applies the max rule to L033, inferred; (4) L053's RFC 9110 wording was seen only in an extract (grounded via MDN and RFC 7231).
- Review fixes (`../review_logic/review.md`): 2 findings for this unit (M1, m9), 2 applied, 0 rejected; cross-branch resolutions applied (`../cross_branch_fixes.md`): X1 (LOGIC, LOGIC.SECURE), X3 and X4 (LOGIC.ENFORCE), X5 (LOGIC.PROCESS), X6 (LOGIC.EXPOSE.2), X7 (LOGIC.EXPOSE, LOGIC.EXPOSE.3).

## L2 claims

### Review fixes

- **M1** (LOGIC.SECURE, LOGIC): the read-visibility clause now carries J1's fallback (database read functions that receive the verified actor, acceptable when a per-user read rule must hold for two or more backends) and what changes under it (the read goes through the function; the table loses direct SELECT). Note for J1's owner kept: the fallback's condition already holds in MD-03's default context, so J1 should reword it.
- **m9** (LOGIC.EXPOSE.3): server-computed allowed actions for agents added as a candidate under the evidence gap, handed to INTERACTION.AGENT's judge; the decision is unchanged.
- **X1** (LOGIC, LOGIC.SECURE): one notation, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`; consequence stated: roles that may SELECT the base tables see every row unless restricted.
- **X3** (LOGIC.ENFORCE): backends never compose several calls into one operation; a database function may call another domain's published functions in its transaction; only direct access to another domain's tables is forbidden.
- **X4** (LOGIC.ENFORCE): logic tests on shared data never commit; commit-only behaviour is tested in a disposable database; concurrency tests are in the default suite.
- **X5** (LOGIC.PROCESS): each backend is one deployable, not split without a measured need.
- **X6** (LOGIC.EXPOSE.2): credentials never travel in a URL; short-lived, scope-limited signed file URLs are the one exception.
- **X7** (LOGIC.EXPOSE, LOGIC.EXPOSE.3): "always in sync" and the compatibility window cover the HTTP description, the function API catalogue and the agent tool surface.

### Verdicts

The backend's verdicts, one per node, in the default context of MD-03 (the database is shared by several backends and other consumers; operations, transitions and per-user write rules decidable from the row are database functions).

- **LOGIC** (roll-up): the backend secures entry, carries workflow, product policy, identity and external calls, runs stateless, and exposes the HTTP interface; it decides no invariant, multi-table operation, state transition or per-user write rule decidable from the row (those are database functions; its checks of them are tested copies). `known (roll-up)`, with the inherited read-visibility clause `undecided: awaiting maintainer`.
- **LOGIC.SECURE**: one gate for every caller, deciding nothing on the caller's word: sessions for humans, audience-checked short-lived tokens for agents, never an ID token as an API credential; central, deny-by-default, object-level authorization of product policy on every request; the verified actor asserted to the database, which decides per-user write rules; all input parsed at entry, uploads and model output included; consumption bounded at the edge (size, rate, time) and per operation in the backend; harmful flows protected by flow, never by blanket bot blocking (agents are users); logins defended in layers, MFA required by default (inferred). Per-user reads: each backend filters from one shared specification with a shared denial-test suite (recorded default); read functions receiving the verified actor acceptable when a rule must hold for two or more backends; directly-reading roles see every row unless restricted; awaiting maintainer.
- **LOGIC.ENFORCE**: one core per backend; adapters (HTML, JSON, agent, jobs) translate only; every external system behind a port, the database function API included; one function call per business operation in its own transaction, never several composed or wrapped; cross-domain composition inside the database through published functions; the backend's own logic testable without a live database, the database's rules tested against one (never-committing transactions on shared data, a disposable database for commit-only behaviour, concurrency tests in the default suite); behaviour lives with its authority (rich objects only for complex backend policy, transaction script otherwise); data gathered in one call, then decided without I/O. Tension recorded: L063 and L066 narrowed by ACT.1 and MD-03.
- **LOGIC.PROCESS**: stateless, share-nothing, disposable processes of distinct types (web, worker) from one build, under a supervisor, behind a reverse proxy, one concern per container; each backend one deployable; sessions and shared caches in backing services; each backend its own database role from configuration, a small pool, never a connection or a transaction per client or across a remote call; long-lived connections the one tolerated per-process state, clients reconnect and resync. `known`; L093 inferred.
- **LOGIC.EXPOSE** (roll-up): one HTTP interface per backend over its one core, for browsers and agents (the database function API serves backends, consoles and scripts); every interface description (HTTP, function catalogue, agent tools) always in sync with the implementation, origin recorded per project (MD-02, X7); repeated requests safe (idempotent methods, keys recorded with the effect).
- **LOGIC.EXPOSE.1**: HTTP means what it says: safe methods change nothing, 303 after a form POST, status codes by definition (412, 428 for versions), every error with a stable machine-readable id apart from its message; RPC tunnelling only as a custom method no standard method fits.
- **LOGIC.EXPOSE.2**: each request carries its credential (never in the URL) and parameters and is servable by any instance; server-held state limited to the revocable session (GUARD.4); workflow progress is resource state in the database, never hidden in a session or connection; strict client-held sessions rejected (no revocation).
- **LOGIC.EXPOSE.3**: hypermedia for the browser (the rendered HTML is the contract; controls shown are cosmetic copies, requests re-authorized); level-2 resource JSON, not called REST, for programs and agents, with server-issued links where the server mints the next step (paging, created resources, handles); full JSON hypermedia acceptable for independently evolving clients without a synchronised description. JSON half inferred; no evidence on hypermedia for agents (candidate: server-computed allowed actions, for the agent-surface judge).

Pinned:
- Nodes judged: 8 of 8 (LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE, LOGIC.EXPOSE.1, LOGIC.EXPOSE.2, LOGIC.EXPOSE.3); 2 are roll-ups owning no row (LOGIC, LOGIC.EXPOSE); 28 of 28 owned rows used.
- Decided 8, undecided 0, apart from one clause inherited from J1 and held in LOGIC.SECURE: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 0 (questions.md says none).
- Verdicts against the maintainer doctrine: 0; none of the 28 rows is a MAINT row; LOGIC.ENFORCE applies the doctrine rows L527, L584, L596 as J1 placed them under MD-03.
- Conflicts with J1 placements: 0. Three source positions narrowed to fit settled placements, recorded as tensions: L063 "testable without a live database" holds for the backend's own share only (ACT.1, MD-03); L066's use-case-owned transaction becomes one database function call per operation (ACT.1); strict client-held session state (Fielding's reading of L054) yields to the server-held revocable session (GUARD.4).
- Evidence gaps: (1) no row on hypermedia controls for agent clients; the JSON half of LOGIC.EXPOSE.3 is decided from MD-02 and L634, marked inferred; server-computed allowed actions for agents recorded as a candidate for the agent-surface judge; (2) L067 rests on one exploratory source, adopted only for its up-front data dependency half, inferred; (3) MFA required by default on human accounts applies the max rule to L033, inferred; (4) L053's RFC 9110 wording was seen only in an extract (grounded via MDN and RFC 7231).
- Review fixes (`../review_logic/review.md`): 2 findings for this unit (M1, m9), 2 applied, 0 rejected; cross-branch resolutions applied (`../cross_branch_fixes.md`): X1 (LOGIC, LOGIC.SECURE), X3 and X4 (LOGIC.ENFORCE), X5 (LOGIC.PROCESS), X6 (LOGIC.EXPOSE.2), X7 (LOGIC.EXPOSE, LOGIC.EXPOSE.3).

## L3 full

### Review fixes

The review of the LOGIC branch named two findings in this unit; the cross-branch resolutions X1 to X7 were applied first, verbatim where this unit touches them. Evidence for each finding was re-checked before applying it; none was found wrong, so none is rejected.

| id | node(s) | evidence re-checked | change made in `records.md` |
|---|---|---|---|
| M1 | LOGIC.SECURE (and LOGIC's state) | `../J1_allocation/questions.md` Q1, "If unanswered, the graph records: A …; B as 'acceptable when a per-user read rule must hold for two or more backends'": confirmed | Fallback added in J1's (and X1's) words; under it, the read goes through the read function and the table loses direct SELECT; the note asking J1's owner to reword the fallback's condition recorded. |
| m9 | LOGIC.EXPOSE.3 | ACT.1 admits previewed controls as copies; L661 (server-minted handles): confirmed | "Candidate under the gap" line added: server-computed allowed actions for agents, handed to INTERACTION.AGENT's judge; state's gap clause names it. Decision unchanged. |
| X1 | LOGIC, LOGIC.SECURE | `../cross_branch_fixes.md` | Clause notation `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`; recorded default; J1's fallback kept; consequence for roles that may SELECT the base tables stated, and "per-role grants bound the damage" reworded so it claims no per-user guarantee. |
| X3 | LOGIC.ENFORCE step 2 | `../cross_branch_fixes.md` | One operation is one call (J1 R1-4); backends never compose calls; cross-domain composition through published functions inside the database; only direct access to another domain's tables forbidden. |
| X4 | LOGIC.ENFORCE step 3 | `../cross_branch_fixes.md` | Test boundary added: never-committing transactions on shared data (L567); committing sessions in a disposable database for commit-only behaviour; concurrency tests in the default suite. |
| X5 | LOGIC.PROCESS | `../cross_branch_fixes.md` | Several backends may share the database; each one deployable, not split without a measured need. |
| X6 | LOGIC.EXPOSE.2 | `../cross_branch_fixes.md` | The request's credential travels in a cookie or header, never in a URL; signed file URLs the one exception, lifetime and scope stated. |
| X7 | LOGIC.EXPOSE, LOGIC.EXPOSE.3 | `../cross_branch_fixes.md` | MD-02's "always in sync" and compatibility window extended to the function API catalogue and the agent tool surface. |

Not applicable to this unit: X2 (no node here cites L517). Findings M2 to M7 and m1 to m8, m10 to m12 concern `../J7_pig_logic/` only.

### Inputs read

- `../../target_hierarchy.md` (whole), `../../maintainer_decisions.md` (MD-01 to MD-03), `../../02_skeleton/judge_plan.md` (section J3).
- `../J1_allocation/allocation_matrix.md` (whole); in `../J1_allocation/records.md`: the default context, the access paths, and the records of RULES.4, RECORD.2, GUARD.1, GUARD.3, GUARD.4, GUARD.5, GUARD.6, ACT.1, ACT.2, ACT.3, DERIVE.3; `../J1_allocation/questions.md` (Q1, for the review fix).
- `../../02_skeleton/skeleton.md`: the LOGIC nodes in the tree and node table, the partition rationale, every intentlink touching LOGIC.
- `../../02_skeleton/claims_ledger.md`: the 28 owned rows in full (L021, L023, L031-L034, L050, L052-L055, L059-L065, L067, L086-L094); rows owned elsewhere cited by the J1 records or bearing on the backend's interface (L019, L020, L022, L041, L042, L044, L051, L066, L214, L215, L226, L234, L252, L253, L258, L260, L264-L268, L272, L305, L306, L310, L311, L315, L318, L358-L368, L417, L478, L479, L484, L527, L528, L534, L582, L584, L596, L611, L612, L614, L622, L629, L633-L657, L659-L661, L663); `../../02_skeleton/sources.md` for tiers. No research claim was opened: no owned row was too compressed to judge.
- For the fixes: `../review_logic/review.md` and `result.md`, `../cross_branch_fixes.md`.

### Verdicts by node

The full judge records (positions with ledger ids, forces, decision with grounds, rejected positions with their winning conditions, realized placements, proposed `epistemic_state`) are in `records.md`. The decisions in brief:

| node | decision | proposed epistemic_state |
|---|---|---|
| LOGIC | roll-up: the backend secures entry, carries workflow, product policy, identity and external calls, runs stateless, exposes the HTTP interface; decides nothing the database owns | `known (roll-up) \| undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from J1, see LOGIC.SECURE)` |
| LOGIC.SECURE | one gate for every caller: authenticate, then authorize centrally, deny by default, object level; assert the verified actor to the database; parse all input at entry; bound consumption at edge and per operation; protect harmful flows by flow; layered login defence, MFA required by default; per-user reads at J1's recorded default with its fallback | `known \| unvalidated: MFA required by default (max applied to L033) \| undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (recorded default: each backend filters from one shared specification with a shared denial-test suite; database read functions receiving the verified actor acceptable when a per-user read rule must hold for two or more backends)` |
| LOGIC.ENFORCE | one core per backend, adapters translate only, ports for every external system including the function API, one call per operation in its own transaction, cross-domain composition in the database, testability by share with the X4 boundary, behaviour with its authority, data in then decision out | `known \| tension: L063 narrowed to the backend's share and L066's boundary owned by the database function (ACT.1, MD-03) \| unvalidated: data in, decision out (P5 single exploratory source, joined with L614)` |
| LOGIC.PROCESS | stateless, disposable processes by type under a supervisor, behind a proxy; one deployable per backend; durable state in backing services; own database role, small pool, no per-client connection; long-lived connections reconnect and resync | `known \| unvalidated: L093's reconciliation of stateless processes with long-lived connections (inferred by its slot)` |
| LOGIC.EXPOSE | roll-up: one HTTP interface per backend for browsers and agents, every interface description always in sync (MD-02, X7), repeated requests safe (GUARD.6) | `known (roll-up)` |
| LOGIC.EXPOSE.1 | HTTP by its defined meanings; 303 after POST; precondition codes; stable machine-readable error ids | `known \| unvalidated: L053's RFC 9110 wording (grounded via MDN and RFC 7231)` |
| LOGIC.EXPOSE.2 | each request self-contained for the process serving it, credential never in the URL; server state limited to the revocable session; workflow state as resource state | `known \| tension: L054's strict reading (client-held session state) yields to GUARD.4 \| unvalidated: workflow state as resource state (inferred from L661, L318, ACT.1)` |
| LOGIC.EXPOSE.3 | hypermedia for the browser; described level-2 JSON for programs and agents, server-issued links where the server mints the next step | `known: browser half (PRESENT.1, L059) \| unvalidated: JSON half rests on MD-02 and L634 \| gap: no row on hypermedia controls for agent clients (candidate: server-computed allowed actions, for INTERACTION.AGENT)` |

### Where the verdicts meet the allocation and the maintainer decisions

- **Placements realized**: GUARD.1, GUARD.3, GUARD.4 (LOGIC.SECURE); ACT.1 and RULES.4 (LOGIC.ENFORCE); GUARD.4 and DERIVE.3 as constraints (LOGIC.PROCESS); RECORD.2 and GUARD.6 (LOGIC.EXPOSE); followed without a skeleton link: GUARD.5 (LOGIC.EXPOSE.1's 412 and 428), PRESENT.1 and RECORD.3 (LOGIC.EXPOSE.3), GUARD.4 (LOGIC.EXPOSE.2).
- **Maintainer decisions applied**: MD-03 (the backend's share of business logic; one function call per operation; the actor asserted to the database), MD-02 (every interface description always in sync, origin recorded per project; extended to the function catalogue and the agent tool surface by X7), MD-01 (row security excluded by default, named in the read-visibility default).
- **Open maintainer question, not settled**: per-user read visibility when several backends share the database. The graph records, in LOGIC.SECURE, the stated default (each backend filters, with a shared specification and a shared denial-test suite), J1's fallback (read functions receiving the verified actor, acceptable when a rule must hold for two or more backends) and the consequence for roles that read the base tables directly; marked `undecided: awaiting maintainer`.
- **Tensions recorded, no conflict**: L063 (testable without a live database) narrowed to the backend's own share, because the database's rules are tested against a live database (ACT.1 accepts that cost; L042, L472); L066 (use-case-owned transaction) realized as the use case owning the call and the function owning the transaction (ACT.1, L584); L054 read as instance independence, not as Fielding's client-held session state, because GUARD.4 keeps a revocable server session (L022).
- **Doctrine**: no owned row is a MAINT row; nothing in the branch goes against the doctrine. LOGIC.ENFORCE applies L527, L584 and L596 as J1 placed them.

### Rejected positions that survive as "acceptable when"

- Backend as authority for all business rules: one backend is the only database consumer and the team's SQL skill is low (ACT.1).
- Blanket bot blocking: no automated client is an intended user of the interface concerned (inferred).
- MFA optional for human accounts: the application's audience cannot practically be required to use a second factor (inferred).
- Anemic services over data-only objects: the backend's share is simple CRUD orchestration (L226).
- Dependency graphs driving cache invalidation: a derived store outside the database must be invalidated precisely and no transactional invalidation exists (inferred).
- Application server facing the internet: local development only (inferred).
- Client-held session state: no backend can hold sessions (GUARD.4).
- RPC-style POST operations: an operation that no standard method fits, as a custom method (L264).
- Full JSON hypermedia: independently developed clients must keep working over a long horizon without a synchronised description (inferred from L059, L061).
- Client-rendered browser application: PRESENT.1's conditions (L253).
- Database read functions for per-user reads (J1's fallback, pending the maintainer's answer): a per-user read rule must hold for two or more backends.

### Notes for the graph builder (not verdicts)

- The skeleton's intent text for LOGIC.EXPOSE realizes RECORD.2 ("when the placement routes them through the backend") predates MD-03; under MD-03 the backend's interface is the route for browsers and agents, and for an outside consumer needing deploys independent of the database. The link stands; its intent text could say so.
- The placements give LOGIC.PROCESS work under ACT.2 (the backend delivers side effects from the outbox) and ACT.3 (workers execute deferred work), but the philosophy graph has no link from LOGIC.PROCESS to either; only PIG-WEB nodes realize them. A `realizes` link from LOGIC.PROCESS to each would make the philosophy graph self-contained. Proposed, not created.
- LOGIC.EXPOSE.2 and LOGIC.EXPOSE.3 have no skeleton intentlink; their records name the placements they follow (GUARD.4; PRESENT.1, RECORD.3).
- For J1's owner (review M1): the read-visibility fallback's condition, "two or more backends", already holds in MD-03's default context; reword it so it does not read as the fallback winning by default. For J1's owner (review M4, carried in `../J7_pig_logic/`): ACT.2 allows in-request atomic phases while ACT.3 forbids foreign effects inside the request.

### Evidence gaps

- No ledger row on hypermedia controls for agent clients: the JSON half of LOGIC.EXPOSE.3 rests on MD-02 and L634 (inferred). Candidate recorded for the agent-surface judge: server-computed allowed actions.
- L067 is one exploratory source (contested by adoption, no opposing source): adopted only for "logic declares its data up front", joined with L614; its cache-invalidation half is not adopted (DERIVE.3).
- MFA required by default: the max rule applied to L033, which orders MFA first without saying "required"; the condition for "optional" is inferred, not in the ledger row.
- L053: RFC 9110's wording on 303 was seen only in a search-result extract; the verdict stands on MDN and RFC 7231.
- LOGIC and LOGIC.EXPOSE own no row; they are judged as the roll-up of their children.

Pinned:
- Nodes judged: 8 of 8 (LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE, LOGIC.EXPOSE.1, LOGIC.EXPOSE.2, LOGIC.EXPOSE.3); 2 are roll-ups owning no row (LOGIC, LOGIC.EXPOSE); 28 of 28 owned rows used.
- Decided 8, undecided 0, apart from one clause inherited from J1 and held in LOGIC.SECURE: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 0 (questions.md says none).
- Verdicts against the maintainer doctrine: 0; none of the 28 rows is a MAINT row; LOGIC.ENFORCE applies the doctrine rows L527, L584, L596 as J1 placed them under MD-03.
- Conflicts with J1 placements: 0. Three source positions narrowed to fit settled placements, recorded as tensions: L063 "testable without a live database" holds for the backend's own share only (ACT.1, MD-03); L066's use-case-owned transaction becomes one database function call per operation (ACT.1); strict client-held session state (Fielding's reading of L054) yields to the server-held revocable session (GUARD.4).
- Evidence gaps: (1) no row on hypermedia controls for agent clients; the JSON half of LOGIC.EXPOSE.3 is decided from MD-02 and L634, marked inferred; server-computed allowed actions for agents recorded as a candidate for the agent-surface judge; (2) L067 rests on one exploratory source, adopted only for its up-front data dependency half, inferred; (3) MFA required by default on human accounts applies the max rule to L033, inferred; (4) L053's RFC 9110 wording was seen only in an extract (grounded via MDN and RFC 7231).
- Review fixes (`../review_logic/review.md`): 2 findings for this unit (M1, m9), 2 applied, 0 rejected; cross-branch resolutions applied (`../cross_branch_fixes.md`): X1 (LOGIC, LOGIC.SECURE), X3 and X4 (LOGIC.ENFORCE), X5 (LOGIC.PROCESS), X6 (LOGIC.EXPOSE.2), X7 (LOGIC.EXPOSE, LOGIC.EXPOSE.3).
