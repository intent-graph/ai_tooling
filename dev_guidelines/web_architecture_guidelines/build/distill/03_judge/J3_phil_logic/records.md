# J3 LOGIC (web-app-philosophy): judge records

One judge record per node of the `web-app-philosophy` LOGIC branch (8 nodes), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves the purpose of the LOGIC role (enforcement and security); weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. The maintainer decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points and are cited by id. The allocation verdicts (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled: these nodes realize them and never re-decide who does what.

Pinned:
- Nodes judged: 8 of 8 (LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE, LOGIC.EXPOSE.1, LOGIC.EXPOSE.2, LOGIC.EXPOSE.3); 2 are roll-ups owning no row (LOGIC, LOGIC.EXPOSE); 28 of 28 owned rows used.
- Decided 8, undecided 0, apart from one clause inherited from J1 and held in LOGIC.SECURE: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 0 (questions.md says none).
- Verdicts against the maintainer doctrine: 0; none of the 28 rows is a MAINT row; LOGIC.ENFORCE applies the doctrine rows L527, L584, L596 as J1 placed them under MD-03.
- Conflicts with J1 placements: 0. Three source positions narrowed to fit settled placements, recorded as tensions: L063 "testable without a live database" holds for the backend's own share only (ACT.1, MD-03); L066's use-case-owned transaction becomes one database function call per operation (ACT.1); strict client-held session state (Fielding's reading of L054) yields to the server-held revocable session (GUARD.4).
- Evidence gaps: (1) no row on hypermedia controls for agent clients; the JSON half of LOGIC.EXPOSE.3 is decided from MD-02 and L634, marked inferred; server-computed allowed actions for agents recorded as a candidate for the agent-surface judge; (2) L067 rests on one exploratory source, adopted only for its up-front data dependency half, inferred; (3) MFA required by default on human accounts applies the max rule to L033, inferred; (4) L053's RFC 9110 wording was seen only in an extract (grounded via MDN and RFC 7231).
- Review fixes (`../review_logic/review.md`): 2 findings for this unit (M1, m9), 2 applied, 0 rejected; cross-branch resolutions applied (`../cross_branch_fixes.md`): X1 (LOGIC, LOGIC.SECURE), X3 and X4 (LOGIC.ENFORCE), X5 (LOGIC.PROCESS), X6 (LOGIC.EXPOSE.2), X7 (LOGIC.EXPOSE, LOGIC.EXPOSE.3).

## How to read

- **Positions**: P1.. the competing practices, with ledger ids (owned rows first; rows owned elsewhere are cited, not re-judged).
- **Forces**: what each position serves and at what cost.
- **Decision**: the max choice and its grounds.
- **Rejected**: each other position, why, and the condition under which it would win ("acceptable when").
- **Realizes**: the placements this node carries out, from the skeleton's intentlinks, with the J1 verdict it follows.
- **State**: proposed `epistemic_state`. `known` = grounded verdict or maintainer decision; `known | unvalidated: X` = an inferred part X; `| tension:` = a source position narrowed to fit a settled placement or maintainer decision; `| awaiting maintainer:` = a clause held at its stated default until the maintainer answers; `| gap:` = missing evidence.

## Context the records assume

From J1 and MD-03, not re-decided here: a classic website (documents, forms, CRUD), one team, JavaScript + Python + Postgres, single tenant, humans and agents as users; the database is shared by several backends and by other consumers (BI and reporting, admin consoles, scripts). The database function API is the default contract to the data; every operation that changes several tables, every state transition (one writer function per state column) and every per-user write rule decidable from the stored row and the acting user is a database function (ACT.1, GUARD.3, MD-03). Each backend owns product policy not stored in the data (product roles, plan limits, feature flags, workflow steps), its users' identity and sessions, workflow across operations, external calls and rendering. Browsers and agents never connect to the database; they reach data through a backend.

---

## LOGIC Business Logic Tier

- **Positions**: owns no row; roll-up of LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE. One competing framing comes from the placements: the backend as the home of all business logic (application-first, L215, L066) against the backend as the workflow, policy and entry tier over a database that owns operations and transitions (L527, L528, L584, L596; MD-03).
- **Forces**: enforcement and security (the role's purpose); changeability of product policy; scalability (stateless backends scale out, the database scales up, L615).
- **Decision**: the backend is the trusted entry and the workflow tier of the application.
  - It **secures entry**: authenticates every caller, parses every input into precise types, enforces product policy deny by default on every request, and bounds what each caller can consume (LOGIC.SECURE).
  - It **enforces its share of the business logic** in a core separable from transport and storage: workflow across operations, product policy not stored in the data, external calls; for every operation on stored data it calls the database function API through a port, one call per operation in its own transaction (LOGIC.ENFORCE; ACT.1).
  - It **runs** as stateless, disposable processes of distinct types, with every durable fact (sessions included) in backing services (LOGIC.PROCESS).
  - It **exposes** one HTTP interface per backend with the protocol's defined meanings: HTML hypermedia for browsers, a described resource-oriented JSON interface and an agent adapter on the same core (LOGIC.EXPOSE).
  - It **does not decide** invariants, multi-table operations, state transitions or per-user write rules decidable from the row (database, GUARD.2, ACT.1, GUARD.3); its checks of those are tested copies for early feedback (RULES.1). It holds no cache beyond one request (DERIVE.3) and resolves no write conflict (the database detects, GUARD.5).
- **Rejected**: the backend as the authority for all business rules (P1 of ACT.1): rejected by MD-03; acceptable when a single backend is the only database consumer and the team's SQL skill is low (ACT.1's condition, L041, L215).
- **Realizes**: through its children GUARD.1, GUARD.3, GUARD.4, ACT.1, RULES.4, RECORD.2, GUARD.6; constrained by GUARD.4 and DERIVE.3.
- **State**: `known (roll-up) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from J1, see LOGIC.SECURE)`.

## LOGIC.SECURE Secured Entry

- **Positions**:
  - P1 authentication is not authorization; an OpenID Connect ID token is for the client, never an access credential to APIs (L021).
  - P2 every client-supplied part of an upload is untrusted: allowlisted extensions, actual signature checked, stored name generated by the server (L023).
  - P3 bound every resource a client can make the server consume (rate, payload size, memory, concurrency, time, third-party spend), each limit tuned to the operation and the business need; agents as principals make loops and retries likelier, so expensive operations get their own limits (L031).
  - P4 maximum body size, minimum read rate and read timeouts enforced at the outermost layer with 413 or 408, plus a size check in the client because browsers show the proxy's error poorly (L032).
  - P5 credential stuffing defended in layers: MFA first, breached-password checks, device fingerprinting and CAPTCHA understood as spoofable, never IP blocking alone (L033).
  - P6 identify the business flows whose automation harms the business and protect those specifically, machine-to-machine APIs included (L034); cited, owned by INTERACTION.AGENT: do not apply blanket bot blocking where agents are intended users (L652).
  - Placement rows cited, owned elsewhere: deny by default (L020); one central mechanism on every request (L305); object-level rules (L306); model output is untrusted input, never an authorization decision (L644); client hints are not enforcement (L650); a server accepts only tokens issued for it and never forwards a client's token (L640); parse once at each entry (L484, L612).
- **Forces**: security (all positions); availability and cost control (P3, P4); usability of login (P5's MFA) and openness to agents (P6 against blanket blocking).
- **Decision**: the backend is the one gate every caller passes, human or agent, and decides nothing on the caller's word.
  1. **Authenticate every caller, then authorize every request.** Humans by the server-held session of GUARD.4; agents by their own short-lived, revocable tokens, accepted only when issued for this server (audience check), never forwarded downstream (L640, GUARD.4). An ID token proves a login to the client and is never accepted as an API credential (L021). Authorization is a separate, central mechanism, deny by default, object level, applied to every request from every client (L020, L305, L306), for what the backend owns: product policy not stored in the data and identity (GUARD.3).
  2. **Assert the actor, do not decide for the database.** For every call into the function API the backend sets the acting user it has verified (transaction-local, from the verified identity, never a client-supplied id; L311 via GUARD.3); per-user write rules decidable from the row are decided by the writer function, and the backend's identical check is a generated or tested copy for early feedback (GUARD.3, RULES.1).
  3. **Treat all input as untrusted and parse it at entry** into the most precise type, once per process boundary (GUARD.1; L484, L612): request bodies, query parameters, headers, uploaded files (P2, L023), payloads read back from queues, and anything a model or agent produced (L644). Client hints, tool annotations and claimed identities are never enforcement (L650).
  4. **Bound consumption at two depths** (P3, P4): identity-blind size, rate, read-rate and time limits at the outermost layer, answering 413 or 408 there, with the client's own size check as a feedback copy (L032); identity-aware limits in the backend, per operation and per business need, with tighter limits on operations that cost money, trigger third parties or are expensive for agents to loop on (L031).
  5. **Protect harmful automation by flow, not by client kind** (P6): name the flows whose automation harms the business (sign-up, purchase, booking, referral) and protect each specifically (L034); no blanket bot blocking, because agents are intended users in this context (L652).
  6. **Defend logins in layers** (P5): MFA first, then breached-password checks, then device signals and challenges known to be spoofable; never IP blocking alone (L033). Max applied: MFA is required by default on human accounts (inferred: L033 orders MFA first; requiring it is the most demanding form).
  - **Per-user read visibility** (`undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`): who filters reads of rows that carry per-user rules ("a draft is visible only to its author") is J1's open question to the maintainer (Q1), not re-asked here (X1).
    - Recorded default: **each backend filters these reads from one shared written specification of the visibility rules, with a shared denial-test suite every backend runs**. Row security stays excluded by default (MD-01).
    - J1's fallback, kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends (J1 Q1). Under that answer, the read goes through the read function and the table loses direct SELECT. (Review M1, note for J1's owner: the fallback's condition, two or more backends, already holds in MD-03's default context; a reader may take it as the fallback winning by default, so J1 should reword it.)
    - Consequence, stated so no line claims more: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted. Per-role grants bound which tables and columns a role sees, not which users' rows.
- **Rejected**:
  - Accepting ID tokens, forwarded tokens or client-declared identity as API credentials: never (L021, L640, L650).
  - Validation or authorization decided in the browser, the agent client or model output: never (GUARD.1, GUARD.3; L019, L644).
  - IP blocking as the only login defence, and IP alone as the limiting key: never (L033).
  - Blanket bot blocking: acceptable when no automated client is an intended user of the interface concerned (inverse of L652's condition; inferred).
  - MFA optional for human accounts: acceptable when the application's audience cannot practically be required to use a second factor; the other layers of L033 then carry the defence (condition inferred, not in the ledger row).
  - Limits only at the edge, or only in the application: each misses what the other sees (identity-blind volume against per-identity and per-operation cost; L031, L032; layering inferred, its stack form owned by PIG-WEB.LOGIC.SECURE.6).
- **Realizes**: GUARD.1 (the backend's parsing and request-level meaning); GUARD.3 (product policy and identity; tested copy of per-user write rules; actor asserted, not decided); GUARD.4 (sessions and credentials held by the backend).
- **State**: `known | unvalidated: MFA required by default (max applied to L033) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (recorded default: each backend filters from one shared specification with a shared denial-test suite; database read functions receiving the verified actor acceptable when a per-user read rule must hold for two or more backends)`.

## LOGIC.ENFORCE Business Core

- **Positions**:
  - P1 separate presentation, domain logic and data access; several presentations over one domain; test seams (L062).
  - P2 business logic free of UI and database entanglement, drivable by users, tests, batch jobs or other programs, runnable in isolation with test adapters and without a live database (L063).
  - P3 every external system (database, mail, payment, third-party API) reached through an adapter behind an application-owned port (L064).
  - P4 no anemic model in a complex domain: a thin service layer around behaviour-rich objects (L065).
  - P5 logic free of data fetching and network concerns, declaring its data dependencies up front, so it runs online, in batch or in cache invalidation, and dependency graphs can drive cache invalidation (L067; one exploratory source, contested by adoption only).
  - Placement rows cited: one core for every client, agents through an adapter that translates and shapes only (L633, RULES.4); multi-table operations as one database function, one writer function per state column (L584, L596, MAINT); the use-case layer owns the transaction boundary (L066); scale layering to domain complexity (L226, owned by PIG-WEB.LOGIC.ENFORCE.1); each extra round trip adds latency (L614).
- **Forces**: correctness (one rule, one place: L633, L596); changeability and testability (P1-P3); performance and latency (round trips, L614); cost of structure on simple domains (L226).
- **Decision**: one business core per backend, separable from transport and storage, holding only what the placements give the backend.
  1. **Layers** (P1, L062): adapters on the outside (HTML views, the JSON interface, the agent adapter, job runners) translate requests into use-case calls and shape results; they hold no rule (L633). Use cases on the inside carry the backend's share: workflow across operations, product policy not stored in the data, external calls (ACT.1, GUARD.3).
  2. **Ports for every external system, the database function API included** (P3, L064). The core calls each business operation as one function call in its own transaction (J1 R1-4) and never composes several calls into one operation or wraps them in one transaction (ACT.1); a step that must be atomic with another is a new database function. Composition across domains happens in the database: a database function may call another domain's published functions inside the same transaction; what is forbidden across domains is direct access to another domain's tables, not calling its published functions (X3). L066's "one explicit boundary per operation" holds with the function as its owner (L584).
  3. **Testability, by share** (P2, L063): the backend's own logic (policy, workflow, orchestration of external calls) runs in isolation with fake adapters and no live database. The rules the database owns (invariants, operations, transitions, per-user write rules decidable from the row) are tested against a live database, as ACT.1 accepts (L042, L472); the backend never reimplements them to make its tests pass without one, except as a copy generated from or tested against the function (RULES.1). Test boundary (X4): logic tests on shared data run in never-committing transactions (L567); behaviour that only shows at commit (serialization retries, lock waits, deferred constraints, the outbox) is tested with committing sessions in a disposable database, never a shared one; concurrency tests for the rules GUARD.2 requires (Serializable with retry, locks) are part of the default test suite.
  4. **Behaviour lives with its authority** (P4, L065): rules about stored data live in the database's writer functions, never in backend objects that would be a second authority; the backend's own policy and workflow logic, when complex, lives in behaviour-rich domain objects with a thin use-case layer around them. A simple share is a transaction script (L226).
  5. **Data in, decision out** (P5's first half, with L614): a use case gathers the data it needs in as few calls as possible (one read function or statement, never queries in loops), then decides in code that does no fetching; that keeps the decision testable without I/O and runnable from any driver (online, batch, agent).
- **Rejected**:
  - All logic in the backend core, including multi-table operations and state transitions (application-first, L215, L066 as stated): rejected by MD-03 and ACT.1; acceptable when one backend is the only database consumer and the team's SQL skill is low (ACT.1's condition).
  - "Without a live database" for every business rule (L063 read literally): it would force a backend copy of the database's rules; narrowed to the backend's share (tension recorded).
  - Anemic services over data-only models for complex backend policy: rejected (L065); acceptable when the backend's share is simple CRUD orchestration (L226).
  - Rules or transitions in adapters, agent wrappers or prompts: never (L633).
  - Dependency graphs driving cache invalidation (P5's second half): not adopted; derived caches are database tables invalidated in the source transaction (DERIVE.3, L534). Acceptable when a derived store outside the database must be invalidated precisely and no transactional invalidation is available (inferred).
- **Realizes**: ACT.1 (the backend's share: workflow, product policy, external calls; one call per operation, no wrapping); requires RULES.4 (one core per backend, adapters translate only).
- **State**: `known | tension: L063 narrowed to the backend's share and L066's boundary owned by the database function (ACT.1, MD-03) | unvalidated: data in, decision out (P5 single exploratory source, joined with L614)`.

## LOGIC.PROCESS Processing Model

- **Positions** (all owned rows, consensus unless stated):
  - P1 stateless, share-nothing processes; anything durable, sessions included, in a backing service; no sticky sessions; process memory or disk at most a single-request cache (L086).
  - P2 scale out by process type (web, worker) from one codebase, release and configuration, scaled independently under an external process manager (L087).
  - P3 disposability: start in seconds, stop gracefully on SIGTERM (stop accepting, finish in-flight work, return the current job to the queue), tolerate sudden death (L088).
  - P4 the database and every other backing service is an attached resource located and credentialled by configuration, swappable without code changes (L089).
  - P5 an external supervisor starts and restarts processes; no self-daemonizing or PID files (L090).
  - P6 the application server never faces the public internet; a reverse proxy or routing layer sits in front (L091).
  - P7 containers are disposable and hold one concern each (L092).
  - P8 a long-lived connection is disposable state held by one process; truth lives in backing services; clients reconnect to any process and resync (L093; majority, reconciliation inferred).
  - P9 never a database connection or transaction per connected client; client count independent of the small server-side pool (L094; inferred from sources).
- **Forces**: scalability and availability (P1-P3); security (P6, P4's credentials in configuration); correctness under failure (P3, P8); database protection (P9).
- **Decision**: adopt P1 to P9 together; no position contests another.
  - Each process is disposable and replaceable: durable state, sessions (GUARD.4) and shared caches (DERIVE.3) live in backing services; process memory caches nothing beyond one request (L086).
  - Several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need (X5).
  - Distinct process types from one build: web processes serve requests; worker processes run deferred work and schedules, claim jobs from the queue the database holds (ACT.3), and return an unfinished job on SIGTERM (L087, L088).
  - Each backend reaches the database as its own role, neither owner nor superuser, located and credentialled by configuration (L089; J1 access paths); a small pool per process; never a connection or an open transaction per connected client, and never a transaction held across a remote call (L094; L234 via ACT.1, ACT.2).
  - A supervisor owns the process lifecycle (L090); a reverse proxy faces the internet and enforces the outermost limits of LOGIC.SECURE (L091, L032); one concern per container (L092).
  - Long-lived connections (real-time channels, agent streams) are the one tolerated per-process state: clients reconnect to any process and resync from the backing services (L093).
- **Rejected**:
  - Sticky sessions and in-memory sessions: never in this context (L086, GUARD.4).
  - Process-memory caches shared beyond one request: never in multi-process production (DERIVE.3, L417).
  - Self-daemonizing processes, PID files: never (L090).
  - Application server facing the internet: acceptable only for local development (inferred from L091's production framing).
  - Per-client database connections: never (L094).
- **Realizes**: constrains GUARD.4 (sessions in a backing service) and DERIVE.3 (no process cache beyond one request). Refined by PIG-WEB.TRANSVERSE.TOPOLOGY. Not linked in the skeleton, though the placements give this node work: ACT.2 (the backend delivers side effects from the outbox) and ACT.3 (workers execute deferred work); see the note in `result.md`.
- **State**: `known | unvalidated: L093's reconciliation of stateless processes with long-lived connections (inferred by its slot)`.

## LOGIC.EXPOSE Backend Interface

- **Positions**: owns no row; roll-up of LOGIC.EXPOSE.1 to .3. Framing from the placements: under MD-03 the database function API is the contract to the data for backends, consoles and scripts (RECORD.2); the backend's interface is the contract for browsers and agents, and for a consumer outside the team that needs deploys independent of the database (RECORD.2's moving condition).
- **Forces**: security and correctness of what callers can do (safe and idempotent semantics, GUARD.6); changeability (independent evolution of client and server); readability for every client kind, human, program and agent (L634).
- **Decision**: each backend offers one HTTP interface over its one core.
  - Browsers get server-rendered HTML whose links and forms are the contract (PRESENT.1, LOGIC.EXPOSE.3).
  - Programs and agents get a resource-oriented JSON interface on the same use cases, described machine-readably and kept in sync with the implementation by process: one origin per fact, the other side generated or conformance-checked, a CI gate that fails on drift; the origin direction is recorded per project (MD-02, L634). An agent protocol adapter, where offered, sits on the same core (L633, L635).
  - MD-02 covers every interface description consumers read (X7): "always in sync by process" and the compatibility window apply to the HTTP description, to the database function API catalogue and to the agent tool surface (for example an MCP server's tool list and schemas).
  - Every endpoint uses HTTP's defined meanings (LOGIC.EXPOSE.1), and every request is self-contained (LOGIC.EXPOSE.2).
  - Repeated requests are safe: safe methods change nothing, PUT and DELETE are idempotent, non-idempotent mutations offered to agents carry an idempotency key that the database function records with the effect (GUARD.6, L051).
- **Rejected**: browsers or agents reaching the database directly: never (RECORD.2). A separate rule-bearing core per client kind: never (RULES.4).
- **Realizes**: RECORD.2 (the backend half: the interface through which browsers and agents reach data); GUARD.6 (safe and idempotent request semantics, keys passed to the database).
- **State**: `known (roll-up)`.

## LOGIC.EXPOSE.1 Protocol Semantics

- **Positions**:
  - P1 methods by their defined semantics: GET and HEAD safe, PUT and DELETE idempotent, POST for non-idempotent processing; never change state through GET or another safe method (L050).
  - P2 each error carries a stable machine-readable identifier (a `type` URI, `ErrorInfo.reason`, an error code) separate from the human-readable message (L052).
  - P3 303 redirects to a different resource that answers the request indirectly, fetched with GET (L053; RFC 9110 wording seen only in an extract).
  - Cited, owned elsewhere: retried operations idempotent by method or key (L051, GUARD.6); stale writes rejected with 412 and preconditions required with 428 (L260, GUARD.5); 303 after a successful POST (L582, GUARD.6); problem details with correction hints for agent tools (L656).
  - Competing practice in the field, without a ledger row defending it: tunnelling every operation through POST (RPC style); custom methods are admitted only where standard ones do not fit (L264, owned by PIG-WEB.LOGIC.EXPOSE.1).
- **Forces**: correctness and safety (crawlers, prefetchers, caches and retrying agents rely on safe and idempotent meanings); machine handling of errors by programs and agents; changeability (error ids survive message rewording).
- **Decision**: the interface means what HTTP says it means.
  - Safe methods never change state; mutations use POST, PUT, PATCH or DELETE with their defined idempotence; a successful form POST answers 303 to a GET page (L050, L053, L582).
  - Browser forms submit only GET and POST, so HTML mutations are POST, each one made safe to repeat by GUARD.6's layers (inferred from the HTML platform; no ledger row).
  - Status codes carry their defined meaning, the precondition codes included for concurrency (412, 428; GUARD.5).
  - Every error has a stable machine-readable identifier separate from its human message, in a standard problem format whose detail helps the caller correct the request (L052, L656).
- **Rejected**:
  - State change through GET (links that delete or confirm): never (L050).
  - Human-readable messages as the only error signal: never; programs and agents cannot branch on them (L052).
  - RPC-style tunnelling of every operation through POST in the JSON interface: rejected as the default; acceptable for an operation no standard method fits, as a custom method (L264).
- **Realizes**: GUARD.6 through LOGIC.EXPOSE (safe and idempotent semantics); GUARD.5 (412 and 428 carry the version check to the caller).
- **State**: `known | unvalidated: L053's RFC 9110 wording (grounded via MDN and RFC 7231)`.

## LOGIC.EXPOSE.2 Self-Contained Requests

- **Positions**:
  - P1 each request carries all the information needed to understand it, so any server instance can serve it; the repeated per-request data is the price of scalability, visibility and recovery (L054).
  - P2 client and server stay separated so UI and server-side logic and storage evolve independently (L055).
  - Strict reading of P1 (Fielding, SRC-244): session state is kept entirely on the client, so the server holds no session.
  - Cited: server-held, revocable sessions behind an opaque cookie (GUARD.4; L022, L315); an agent surface with no hidden per-connection session, cross-call state as an explicit server-minted handle validated against the caller (L661); no application state in cookies, narrow sense kept by J1 (L318).
- **Forces**: scalability and recovery (any instance serves any request); security (revocation needs server-held state, L022); changeability (P2).
- **Decision**: every request is self-contained with respect to the process that serves it.
  - It carries its credential (the opaque session identifier or the agent's token, in a cookie or a header, never in the URL; X6: short-lived, single-purpose, scope-limited signed URLs for file delivery are the one exception, with their lifetime and scope stated) and every parameter its use case needs; anything it references is resolved from backing services, never from the memory of the instance that served the previous request (L054, L086).
  - The server-held state is limited to identity and security state (the session, revocable; GUARD.4). Workflow progress is resource state in the database (state columns, ACT.1), addressed by identifiers in the request, never hidden in a session or a connection (L661; inferred from L318's narrow sense and ACT.1).
  - Client and server are coupled only through the interface contract (HTML links and forms, or the described JSON interface), so either can change behind it (L055).
- **Rejected**:
  - Strict client-held session state with no server session (stateless signed tokens or cookie sessions): rejected because it cannot be revoked (L022), against the settled GUARD.4 placement; acceptable when no backend can hold sessions (GUARD.4's moving condition).
  - Hidden server-side conversational or workflow state per session or per connection: never (L661; inferred for the browser case).
- **Realizes**: no direct link in the skeleton; follows GUARD.4 (session held by the backend, in a backing service) and is bounded by LOGIC.PROCESS (stateless processes).
- **State**: `known | tension: L054's strict reading (client-held session state) yields to GUARD.4 | unvalidated: workflow state as resource state (inferred from L661, L318, ACT.1)`.

## LOGIC.EXPOSE.3 Hypermedia Controls

- **Positions**:
  - P1 server-provided representations drive client transitions; no fixed, out-of-band URL hierarchies; documentation-driven clients are the most frequent violation (L059; Fielding; contested).
  - P2 a JSON API without hypermedia controls is resource-oriented HTTP (Richardson level 2), not REST (L060; definition agreed).
  - P3 the uniform interface trades efficiency for visibility and independent evolution (L061).
  - Common API practice: documented fixed URLs and an out-of-band description (L059's positions column; L634 OpenAPI for humans, generators and agents).
  - Cited: server-rendered HTML by default (PRESENT.1; L252, L629); in a hypermedia design the HTML is the contract and an OpenAPI file covers only the JSON endpoints that exist (L257, owned by PIG-WEB.LOGIC.EXPOSE.1); the description is always in sync (MD-02).
- **Forces**: changeability (independent evolution of clients over a long horizon, P1, P3); efficiency and tooling for program and agent clients (common practice); enforcement (the server decides which transitions to offer).
- **Decision**: hypermedia where the client is a browser; a described, level-2 resource interface where the client is a program or an agent.
  - **Browser**: the HTML the server renders is the contract: links and forms drive every transition, and the server renders only the controls the user may use. The control is a cosmetic copy; the request is re-authorized on arrival (GUARD.3, RULES.1). This is P1 in full, and it follows from PRESENT.1 (L059, L629).
  - **Programs and agents**: a resource-oriented JSON interface called what it is, resource-oriented HTTP, not REST (L060), whose contract is the machine-readable description kept in sync by process (MD-02, L634); the same rule holds for the agent tool surface's description (X7). Server-issued links are used where the server mints the next step: continuation links for paging (L266, owned by PIG-WEB), the created resource's location, explicit handles for cross-call state (L661). Clients do not build URLs the description does not define.
  - Grounds: MD-02 makes an always-synchronised description the contract programs and agents read; it buys the independent evolution P1 seeks by additive change and conformance checks, at lower cost per client (inferred). P3's trade is accepted where it pays: browser pages.
- **Rejected**:
  - Full hypermedia controls in the JSON interface (links and forms in every representation): not the default; acceptable when independently developed clients must keep working over a long horizon without a shared, synchronised description (L059, L061; condition inferred).
  - A client-rendered browser application driven by an out-of-band JSON description: not the default; acceptable under PRESENT.1's conditions (many interdependent UI parts, offline, high-frequency or real-time state; L253).
  - Calling a level-2 JSON interface REST: rejected on definition (L060).
- **Candidate under the gap** (review m9; no change to the decision): server-computed allowed actions for agents, the agent analogue of the browser's rendered controls, which ACT.1 already admits as a permitted copy (the server previews what the caller may do; the request is still re-authorized on arrival). Handed to INTERACTION.AGENT's judge with L661 (explicit server-minted handles) as the nearest evidence.
- **Realizes**: no direct link in the skeleton; follows PRESENT.1 (server-rendered HTML) and RECORD.3 with MD-02 (contract origin per project, always in sync).
- **State**: `known: browser half (PRESENT.1, L059) | unvalidated: JSON half rests on MD-02 and L634 | gap: no row on hypermedia controls for agent clients (candidate: server-computed allowed actions, for INTERACTION.AGENT)`.
