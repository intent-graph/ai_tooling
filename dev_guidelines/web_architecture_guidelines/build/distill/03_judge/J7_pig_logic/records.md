# J7 PIG-WEB.LOGIC (pig-web-defaults): judge records

One judge record per node of the `pig-web-defaults` LOGIC branch (31 nodes, 1 deferred and not judged), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves the purpose of the LOGIC role (enforcement and security); weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. The maintainer decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points and are cited by id. The allocation verdicts (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled: these nodes realize them and never re-decide who does what. The philosophy verdicts these nodes refine are `../J3_phil_logic/records.md` (LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE and its children); nothing here contradicts them.

Pinned:
- Nodes judged: 30 of 31 in the PIG-WEB.LOGIC branch; 1 deferred and not judged (PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery); 5 are roll-ups owning no row (PIG-WEB.LOGIC, .SECURE, .ENFORCE, .PROCESS, .EXPOSE); 133 of 133 owned rows used.
- Decided 29, undecided 1: PIG-WEB.LOGIC.SECURE.2's `SameSite` attribute on the session cookie, a genuine trade-off between the session's function (carrying a login across arrivals from other sites) and protection against attacker-triggered navigations; raised as the one question, recorded default `Lax` plus a cross-site navigation check, `Strict` for operator consoles.
- One clause inherited from J1, held in PIG-WEB.LOGIC.SECURE.1: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends; under it ENFORCE.3, SECURE.1 and PROCESS.6 read through the function and the table loses direct SELECT. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 1 (SameSite on the session cookie); five other candidate trade-offs considered and not raised, each with its reason.
- Verdicts against the maintainer doctrine: 0. The one MAINT row owned here (L605, scheduled jobs) is adopted as the max choice; the doctrine rows J1 placed (L516, L527, L534, L584, L596, L604) are applied as placed; L530 (function error codes, override flag), L566 (actor from a transaction-local setting) and L587 (idempotent mutations) are applied; L517 is applied with its departure counted once at J6 (X2).
- Conflicts with J1 placements: 0. One tension inside J1 carried and routed to J1's owner: ACT.2 runs a foreign mutation the user waits for as atomic phases in the request, while ACT.3 forbids foreign effects inside the request; resolved here in favour of both by running the phases in a worker behind a 202 status resource, in-request only under a stated condition. Source positions narrowed to fit settled placements, recorded as tensions: request-wide and use-case-wide transactions (L229) and ORM-first writes (L235, L227 Active Record) yield to one database function call per transaction (ACT.1, DB_API); views and separate read stores (L237) yield to L516 and DERIVE.1; post-commit hooks (L233) carry only losable work (L600, ACT.2); limiter state in a cache service (L365) yields to Postgres until a measured limit (POSTGRES_FIRST, CACHE_STORE); replay of stored failures (Stripe v1 in L269, L546) yields to key and effect committed together (GUARD.6).
- Evidence gaps: (1) framework (L242): no source gives neutral criteria; Django is chosen on criteria the settled verdicts set (framework sessions and CSRF, L323, L330; server-rendered HTML; synchronous default), inferred; how Pydantic models and the OpenAPI description are produced under Django was not read (Django Ninja is the candidate to verify: OpenAPI 3.1 output, Pydantic v2); (2) upload path (L421): no source weighs direct-to-storage against through-the-app; direct chosen, inferred; (3) version location (L276): five contested positions; URL-path major version, `/v1` from the start, inferred; (4) login delegation (L338): no source ranks it; delegation to an OpenID Connect server (a provider or self-run) chosen, inferred; the `acr`/`amr` check rests on OpenID Connect Core, not on a ledger row; (5) no Python job runner over a queue table written by database functions was read (JOB_HOST pattern set, library open); (6) rate-limiter counters in Postgres follow POSTGRES_FIRST by analogy, no source; (7) Postgres behaviour not in the ledger: transaction-local settings vanish in autocommit, deadlocks and serialization failures outside Serializable (inferred).
- Review fixes (`../review_logic/review.md`): 17 findings for this unit (M1 to M7, m1 to m8, m10 to m12; m9 is J3's), 17 applied, 0 rejected; cross-branch resolutions X1 to X7 applied where these nodes touch them (`../cross_branch_fixes.md`).

## How to read

- **Positions**: P1.. the competing practices, with ledger ids (owned rows first; rows owned elsewhere are cited, not re-judged).
- **Forces**: what each position serves and at what cost.
- **Decision**: the max choice and its grounds.
- **Rejected**: each other position, why, and the condition under which it would win ("acceptable when").
- **Realizes**: the placements this node carries out, from the skeleton's intentlinks, with the J1 verdict it follows; "follows" names a placement the node obeys without a skeleton link (proposed links are listed in `result.md`, L3).
- **State**: proposed `epistemic_state`. `known` = grounded verdict or maintainer decision; `known | unvalidated: X` = an inferred part X; `| tension:` = a source position narrowed to fit a settled placement or maintainer decision; `| awaiting maintainer:` = a clause held at its stated default until the maintainer answers; `| gap:` = missing evidence.

## Context the records assume

From J1 and MD-03, not re-decided here: a classic website (documents, forms, CRUD), one team, JavaScript + Python + Postgres, single tenant, humans and agents as users; the database is shared by several backends and by other consumers (BI and reporting, admin consoles, scripts). The Postgres function API is the default contract to the data: every business operation is one function call in its own transaction, never wrapped with another; every state column has one writer function; per-user write rules decidable from the stored row and the acting user are decided by that writer function; invariants, audit (session role and claimed actor) and per-role privileges are the database's (ACT.1, GUARD.2, GUARD.3, ACT.4, DB_API, MD-03). No row-level security by default (MD-01). Each Python backend owns product policy not stored in the data (product roles, plan limits, feature flags, workflow steps), its users' identity and sessions, workflow across operations, external calls, deferred-work execution and HTML rendering. Browsers and agents never connect to the database. From J3: the backend is the trusted entry and the workflow tier, runs stateless disposable processes of distinct types, and exposes HTML hypermedia to browsers and a described resource-oriented JSON interface to programs and agents, the description always in sync with the implementation (MD-02).

---

## PIG-WEB.LOGIC Python Application Tier

- **Positions**: owns no row; roll-up of SECURE, ENFORCE, PROCESS and EXPOSE (PROCESS.7 deferred). One framing contest runs through the children: the Python backend as the home of all business logic, with ORM models as the domain and the request or use case as the transaction (L226's application-first reading, L227's Active Record, L229, L235), against the backend as the workflow, policy and entry tier that calls the Postgres function API (DB_API, ACT.1, MD-03).
- **Forces**: enforcement and security (the role's purpose); changeability of product policy; scalability (stateless backends scale out, L086 via J3).
- **Decision**: the Python backend realizes J3's LOGIC verdict as follows.
  - **Framework and runtime**: Django, synchronous handlers; asynchronous code only in the process type that holds long-lived connections (ENFORCE.5, ENFORCE.4). Several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need (X5).
  - **Secure**: one central, deny-by-default, object-level policy module, which also authorizes any override of a blockable rule; Django database sessions in Postgres behind a `__Host-` cookie (its `SameSite` value raised to the maintainer); every CSRF layer; login delegated to an OpenID Connect server through a backend-for-frontend, the required authentication context requested and checked; no credential in a URL; limits at the proxy and per identity in the backend; guarded server-side fetch (SECURE.1 to .7).
  - **Enforce**: a use-case layer every entry point calls; each business operation one call to a generated, typed wrapper of an API function, in one transaction that also sets the verified actor; reads that need the actor in a short read-only transaction through the same wrapper; reads gathered in one statement, filtered, sorted and paged in Postgres (ENFORCE.1 to .3).
  - **Process**: Python workers claim jobs and outbox rows that database functions wrote, through the job table's writer functions; delivery at least once to idempotent consumers; foreign mutations as atomic phases in a worker behind a 202 status resource; bounded retries at one layer; file bytes in object storage, file rows and their state in Postgres (PROCESS.1 to .6).
  - **Expose**: HTML for browsers; resource-oriented JSON under `/v1` with problem details, idempotency keys and status resources for programs and agents; every response labelled for caches; one origin; Pydantic models at every entry; every interface description (OpenAPI 3.1, function catalogue, agent tools) in sync; additive evolution (EXPOSE.1 to .7).
- **Rejected**: the Python backend as the authority for all business rules, with Active Record models writing the tables: rejected by MD-03, ACT.1 and DB_API; acceptable when one backend is the only database consumer and the team's SQL skill is low (ACT.1's condition).
- **Realizes**: refines LOGIC (J3); through its children ALLOCATION.GUARD.1, GUARD.4, GUARD.6, ACT.1, ACT.2, ACT.3, DERIVE.2 and PIG-WEB.ALLOCATION.ROW_SECURITY, JOB_HOST, CACHE_STORE, TYPE_CHAIN.
- **State**: `known (roll-up) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (see SECURE.1) | undecided: SameSite on the session cookie (SECURE.2, raised) | unvalidated: framework choice (ENFORCE.5)`.

## PIG-WEB.LOGIC.SECURE Backend Security

- **Positions**: owns no row; roll-up of SECURE.1 to .7.
- **Forces**: security (all children); availability and cost control (SECURE.6); the session's function, carrying a login across arrivals into the application (SECURE.2: served by that node, because it is what a session is for); login friction (SECURE.4, SECURE.5: not a force this branch serves, which is why MFA is required). The two are kept apart (review M5): friction makes a step slower, while dropping the session on arrival defeats the node's function.
- **Decision**: the Python backend is the one gate every caller passes and decides nothing on the caller's word (J3 LOGIC.SECURE):
  - access checked by one central policy module, deny by default, object level, the backend's checks kept in full because row-level security is off (SECURE.1, MD-01);
  - humans hold an opaque server-side session in Postgres (SECURE.2; its `SameSite` value raised to the maintainer), protected against forgery by every CSRF layer (SECURE.3), after an OpenID Connect login delegated to an identity provider (SECURE.4) that meets SECURE.5's bar, the authentication context checked on every login;
  - no session token, bearer token or long-lived credential ever travels in a URL (X6);
  - agents hold short-lived, audience-bound, revocable tokens (SECURE.4);
  - consumption is bounded at the proxy and per identity and operation in the backend (SECURE.6);
  - fetches of client-named URLs cannot reach internal addresses (SECURE.7).
- **Realizes**: refines LOGIC.SECURE (J3); through its children ALLOCATION.GUARD.4 and PIG-WEB.ALLOCATION.ROW_SECURITY.
- **State**: `known (roll-up) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (SECURE.1) | undecided: SameSite on the session cookie (SECURE.2, raised)`.

## PIG-WEB.LOGIC.SECURE.1 Access Control Enforcement

- **Positions**:
  - P1 implement the authorization mechanism once, centrally (filters or middleware), and apply it to every request whatever its origin (L305).
  - P2 enforce object-level rules (record ownership), not only route or role checks (L306).
  - P3 prefer attribute- or relationship-based control over plain role-based control when granularity or tenancy grows (L307; one T1 source, no dissent).
  - P4 test authorization with unit and integration tests including denial cases; log access-control failures with alerting (L308).
  - Placement positions cited, settled by MD-01 in ROW_SECURITY: row security on every path (L619), only with several consumers (L688), as a second line (L128).
- **Forces**: security (all positions); changeability of policy (P3's richer model against plain roles); detection (P4).
- **Decision**:
  1. **One policy module per backend, deny by default** (P1; L020 via GUARD.3). Middleware refuses any route that declares no permission; every use case calls the module with actor, action and object for each single object it reads or changes (P2). For collection reads, the module emits a query predicate that the read statement applies (ENFORCE.3), never a check on rows already loaded, which would yield short pages and leak counts (review m8; DERIVE.2). Central and object-level at once.
     - **Overrides of blockable rules** (L530, MAINT; review M7): a writer function's blockable business rule can be overridden by an explicit flag. Setting that flag is an action the policy module authorizes per actor, like any other; it never comes from client input unchecked, and the override is audited with the actor (ACT.4). The use case decides whether to set it (ENFORCE.1).
  2. **Model**: product roles for product policy not stored in the data, plus attribute and relationship rules evaluated on the object (owner, author, assignee, plan, flag) (P3). The default context already carries per-user rules, so P3's condition holds from the start (inferred).
  3. **Division with the database** (GUARD.3, ROW_SECURITY, MD-01): no row-level security, so the backend's checks are kept in full. Per-user write rules decidable from the row are decided by the writer function; the backend's identical check is a copy generated from or tested against that function (RULES.1), and the function's named denial maps to the same response as the backend's (EXPOSE.2). The backend sets the verified actor for every call (ENFORCE.2; L311, L566).
  4. **Per-user read visibility** (`undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`): who filters reads of rows that carry per-user rules ("a draft is visible only to its author") is J1's open question (Q1), not re-asked here (X1).
     - Recorded default: **each backend filters these reads from one shared written specification of the visibility rules, inside the read statement (ENFORCE.3), with a shared denial-test suite every backend runs**. Row security stays excluded by default (MD-01).
     - J1's fallback, kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends (J1 Q1). **Under that answer** (review M1): the read goes through the read function, run with the actor set (ENFORCE.2); the table loses direct SELECT; this step's filter moves from the backend's statement into the function. Note for J1's owner: the fallback's condition, two or more backends, already holds in MD-03's default context, so a reader may take it as the fallback winning by default; J1 should reword it.
     - Consequence, stated so no line claims more: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted. Per-role grants bound which tables and columns a role sees, not which users' rows.
  5. **Tests and logs** (P4): a denial test for every rule, at unit level and through the deployed stack against a live database under the backend's real role, because the database's half of authorization cannot be tested otherwise (ACT.1). Those tests run in never-committing transactions when the database is shared; behaviour that only shows at commit is tested with committing sessions in a disposable database, never a shared one (X4). Every denial goes to the security event log, a sink separate from the business audit (ACT.4), with alerting on bursts (mechanics owned by PIG-WEB.TRANSVERSE.OPERABILITY.4).
- **Rejected**:
  - Route- or role-only checks: never (P2).
  - Checks written per view without one module: never (P1).
  - Plain role-based control: acceptable when no rule depends on an object's attributes or relations (inverse of P3's condition; inferred); not this context.
  - Row-level security by default, or replacing backend checks: never by default (MD-01); acceptable when MD-01's three conditions hold, with the backend checks kept (L128).
  - Per-object checks on loaded rows for collections: never (DERIVE.2; review m8).
  - An override flag passed through from client input: never (L530, GUARD.3; review M7).
- **Realizes**: PIG-WEB.ALLOCATION.ROW_SECURITY (keeps the backend checks, as the placement sets). Follows ALLOCATION.GUARD.3 (no skeleton link; proposed).
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (recorded default: each backend filters from one shared specification with a shared denial-test suite; database read functions receiving the verified actor acceptable when a per-user read rule must hold for two or more backends) | unvalidated: P3's condition taken as met in the default context; collection predicates emitted by the policy module (inferred)`.

## PIG-WEB.LOGIC.SECURE.2 Sessions

- **Positions**:
  - P1 use the framework's session management, not a custom one, kept updated (L323).
  - P2 random session identifiers (CSPRNG, at least 64 bits), meaningless, carrying no personal data; user data server-side (L322).
  - P3 cookie with `Secure`, `HttpOnly`, explicit `SameSite=Lax` or `Strict`, the `__Host-` prefix, no `Domain`, the narrowest `Path` (L324); never scoped to a parent domain, because sibling subdomains could plant cookies (L329).
  - P4 renew the identifier on every privilege change, above all at login (L325).
  - P5 idle and absolute timeouts enforced on the server, calibrated to risk; numbers differ by body (L326).
  - P6 logout invalidates the session on the server; responses carrying session identifiers are `no-store` (L327).
  - P7 the signed-cookie session backend is not for sensitive data: not encrypted, replayable until expiry, not revocable (L328).
  - P8 the framework's JWT bearer tutorial leaves token storage, revocation and sessions undecided (L317).
  - Placement cited: an opaque server-side session, revocable, in a backing service, never in process memory (GUARD.4; L315, L022, L319, L086); sessions in Postgres (POSTGRES_FIRST).
- **Forces**: security (theft, fixation, revocation, attacker-triggered navigations); the session's function, carrying a login across every arrival into the application. This node serves both: the second is what a session is for, not login friction, which no LOGIC node serves (SECURE roll-up; review M5). They pull apart only on the `SameSite` value.
- **Decision** (all but the `SameSite` value; that value is `undecided` and raised):
  - **Store**: Django's session framework with the database backend, sessions in Postgres (P1, GUARD.4, POSTGRES_FIRST). The session table is written only by its own backend and carries no state column and no multi-table effect, so it falls under DB_API's direct-write exception (inferred). Expired sessions are purged by a scheduled job (PROCESS.1; inferred).
  - **Identifier**: framework-generated, random, opaque; user data stays server-side (P2). It travels only in the cookie, never in a URL (X6).
  - **Cookie**: a `__Host-`-prefixed name, `Secure`, `HttpOnly`, an explicit `SameSite`, no `Domain`, `Path=/` (P3).
  - **`SameSite` value** (`undecided`, raised in `questions.md`; review M5). L324 admits Lax and Strict; the choice trades the session's function against protection, both forces of this node.
    - Strict: the cookie is not sent on any cross-site request, top-level navigations included, so an arrival from another site's link starts logged out; it closes attacker-opened windows and navigations carrying the session, through which reflected script injection or cross-site leaks run with the user's session (inferred; the cookie draft, draft-ietf-httpbis-rfc6265bis, calls Lax "only a speedbump" against them).
    - Lax: the login holds on arrival from links, and cross-site top-level GET navigations carry the session (L331).
    - The earlier claim that Strict's extra protection "covers only safe requests, which change nothing" is withdrawn: a safe request that changes nothing can still render user data or reflect input under the session.
    - **Recorded default if unanswered**: `SameSite=Lax`, plus a Fetch Metadata check that refuses or redirects cross-site navigations (`Sec-Fetch-Site: cross-site`, `Sec-Fetch-Mode: navigate`) to authenticated pages that are not declared entry points (inferred; no ledger row); `SameSite=Strict` for operator consoles and other applications never entered from other sites' links.
  - **Lifecycle**: identifier renewed at login, logout, privilege change and step-up (P4); idle and absolute timeouts both enforced by the server, their values recorded per project by risk class with the NIST assurance levels as reference (P5); logout deletes the server record, and responses that set or contain a session identifier are `Cache-Control: no-store` (P6, L327; personalised responses that merely run under the session are `private, no-cache`, EXPOSE.4; review m10). Because state is server-held, deleting a user's session rows revokes every session at once (L022; inferred use).
- **Rejected**:
  - Signed-cookie sessions and stateless JWT sessions in the browser: never (P7, P8, L022, GUARD.4); acceptable when no backend can hold sessions (GUARD.4's moving condition).
  - A custom session mechanism: never (P1).
  - `SameSite=Strict` or `Lax` as the general default: not decided here (raised; see the `SameSite` value above). Strict is required under the recorded default for applications never entered from cross-site links, such as an internal operator console (inferred).
  - `SameSite=None` or a parent-domain scope: never (P3).
  - A session identifier in a URL (query string, path): never (X6).
  - Sessions in process memory: never (L086). A cache service as the session store: acceptable at a measured limit of Postgres (POSTGRES_FIRST).
- **Realizes**: ALLOCATION.GUARD.4 (holds sessions as the identity placement sets).
- **State**: `known | undecided: SameSite on the session cookie (raised; recorded default Lax plus a cross-site navigation check, Strict for operator consoles) | unvalidated: session table under DB_API's direct-write exception (inferred); the navigation check (inferred, no ledger row)`.

## PIG-WEB.LOGIC.SECURE.3 CSRF Defense

- **Positions**:
  - P1 use the framework's built-in CSRF protection first and avoid exempting views (L330).
  - P2 layer defences: a synchronizer token (or a signed double-submit for stateless applications) plus SameSite cookies; SameSite alone is insufficient (Lax allows top-level GET, covers the site not the origin, does not stop client-side forgery) (L331).
  - P3 reject cross-site unsafe-method requests by `Origin` or `Sec-Fetch-Site` (Fetch Metadata), allowing requests that lack the headers, exempting deliberate CORS endpoints, trialled in logging-only mode (L332).
  - P4 a custom request header on script requests relies on the CORS preflight; CORS must list explicit origins; it does not replace CSRF protection (L333).
- **Forces**: security; compatibility with browsers that send no Fetch Metadata (P3's allowance).
- **Decision**: every layer, on every request that the session cookie authenticates.
  1. Django's CSRF middleware, synchronizer token in every form and in a request header for island scripts; no view that accepts the session cookie is exempted (P1, P2, P4).
  2. The session cookie's explicit `SameSite` value (SECURE.2: raised to the maintainer, `Lax` recorded by default) as a second layer (P2).
  3. A Fetch Metadata and `Origin` check that rejects cross-site unsafe requests, deployed first in logging-only mode, then enforced; requests without the headers fall back to the token check (P3).
  4. Safe methods change nothing (EXPOSE.1 via J3, L050), so GET carries no token.
  - Endpoints authenticated by bearer tokens (agents, programs) carry no ambient credential and never accept the session cookie, so forgery does not apply to them; they are the only exemption, matching P3's deliberate cross-origin endpoints (inferred).
- **Rejected**: SameSite alone: never (P2). A custom header alone: never (P4). Signed double-submit: acceptable when the application holds no server session (P2); not this context. Exempting a view that accepts the session cookie: never (P1).
- **Realizes**: no skeleton link; follows ALLOCATION.GUARD.4 (cookie session) and ALLOCATION.RULES.3.
- **State**: `known | unvalidated: the cookie and bearer endpoints kept apart (inferred)`.

## PIG-WEB.LOGIC.SECURE.4 Federated Login and Tokens

- **Positions**:
  - P1 choose explicitly between delegating login to an external identity provider (OAuth 2, OpenID Connect, SAML) and operating an own credential store, and record the choice; no source ranks them (L338).
  - P2 the authorization code grant with PKCE, never the implicit grant; for agents acting for a human, the code flow with PKCE, exact redirect match, HTTPS; client credentials for agents acting on their own behalf; static keys only for short scripts (L339).
  - P3 redirect URIs matched by exact string, no open redirectors (L340).
  - P4 rotate or sender-constrain the refresh tokens of public clients; sender-constrain access tokens (mutual TLS or DPoP) (L341).
  - P5 validate the OpenID Connect ID token: issuer, audience containing the client id, expiry, nonce (L342).
  - P6 link federated identities by issuer plus subject, never by e-mail; reauthenticate before changing links (L343).
  - P7 a JWT verifier pins accepted algorithms, rejects `none`, validates issuer, subject and audience, and keeps token kinds distinguishable (L312).
  - Cited: backend-for-frontend when login goes through a provider (L313, GUARD.4); a server accepts only tokens issued for it and never forwards a client's token (L640); an ID token is never an API credential (L021 via J3).
- **Forces**: security (credential handling, token theft, token confusion); the cost and availability of an external dependency (P1's other side).
- **Decision**:
  1. **Login is delegated to an OpenID Connect server**, recorded as a decision (P1): an external identity provider or a self-run OpenID Connect server, which removes cost and data-residency objections to a provider (review m11). Grounds: the backend then stores no password, and MFA, phishing-resistant authenticators and breached-password checks (SECURE.5) come from a service built for them; agents as users need OAuth authorization anyway (P2's agent half), which such a server supplies, while an own credential store would also need an own authorization server for agents (inferred).
  2. **The Python backend is the confidential client, backend-for-frontend** (L313, GUARD.4): code flow with PKCE (P2), exact redirect URIs and no open redirector (P3), ID token validated (P5), then an opaque server session (SECURE.2). Provider tokens never reach the browser. The authorization code in the redirect is single-use, short-lived and bound to PKCE, not a session or bearer token; no session token, bearer token or long-lived credential ever travels in a URL (X6).
  3. **The authentication context is verified, not assumed** (review M6; inferred from OpenID Connect Core 1.0, not in the ledger): the backend requests the required context (`acr_values`, or the provider's MFA policy that yields a known `amr`) and refuses a login whose ID token lacks it; for sensitive operations it requires a fresh, sufficient context (step-up with `max_age`, checking `auth_time`). Without this check a provider policy change could drop MFA while every other check passes, which is deciding on the caller's word (J3 LOGIC.SECURE).
  4. **Local identity** keyed by issuer plus subject; reauthentication before any link change (P6).
  5. **Agents**: tokens issued for this server only (audience, L640), short-lived and revocable (GUARD.4); code flow with PKCE when acting for a human, client credentials when acting on their own (P2); refresh tokens rotated or sender-constrained; access tokens sender-constrained (DPoP or mutual TLS) wherever the provider and the agent host support it (P4).
  6. **Every JWT** verified with pinned algorithms, `none` rejected, issuer, subject and audience checked, explicit `typ` (P7).
  7. Downstream calls use the backend's own token, never a forwarded one (L640).
- **Rejected**:
  - An own credential store: acceptable when no OpenID Connect server can be used or run, a self-run one included (review m11); SECURE.5 then applies in full, MFA included (P1; condition inferred).
  - Accepting a login without checking the asserted authentication context: never while MFA is required (review M6).
  - Implicit grant, password grant, shared static keys for agents: never (P2); static keys only for short-lived scripts (L339).
  - Account linking by e-mail: never (P6).
  - Tokens held by browser JavaScript: never by default (GUARD.4).
  - Bearer-only access tokens: acceptable when the provider or the agent host cannot sender-constrain, with a short lifetime and server-held revocation (inferred).
- **Realizes**: ALLOCATION.GUARD.4 (handles tokens where the identity placement allows them).
- **State**: `known | unvalidated: delegation ranked above an own store (L338 ranks neither; ranking mine); the acr/amr check and step-up (OpenID Connect Core, not in the ledger); sender-constraining support across agent hosts not read`.

## PIG-WEB.LOGIC.SECURE.5 Passwords and Login Throttling

- **Positions**:
  - P1 password policy: at least 64 characters allowed, all printable Unicode, no composition rules, no periodic rotation, checks against compromised and common-password lists; minimum length 8 with MFA, 15 without; Django's default validators still include a numeric-only check (L344).
  - P2 hash with Argon2id (at least 19 MiB, 2 iterations, parallelism 1), with scrypt, bcrypt or PBKDF2 as fallbacks, and upgrade hashes at login; Django's default is PBKDF2, Argon2 opt-in; PBKDF2 stays acceptable under FIPS-140 (L345).
  - P3 offer MFA and phishing-resistant authenticators (WebAuthn, passkeys) (L346).
  - P4 generic authentication errors; failures counted per account, not only per source address; growing delays rather than hard lockout; a recovery path; the login endpoint rate-limited (L347).
  - P5 framework throttling is not a security control (Django does not throttle authentication; DRF says its throttling is not brute-force protection); the real limit sits in the proxy, a dedicated limiter or the login logic (L348).
  - P6 one-time-code and verification endpoints count failed attempts only (L349; one T3 source).
  - Cited: MFA required by default on human accounts (J3 LOGIC.SECURE, max applied to L033).
- **Forces**: security; login usability, which this node does not serve as a force (J3's reasoning on MFA).
- **Decision**: this node governs an own credential store (SECURE.4's acceptable fallback) and is the bar the chosen OpenID Connect server must meet (selection criterion; inferred). That bar includes emitting the authentication-context claims (`acr` or `amr`, and `auth_time`) that SECURE.4 checks, so the backend can verify MFA rather than assume it (review M6; OpenID Connect Core, not in the ledger).
  1. **Policy** (P1): maximum length at least 64, all printable Unicode, no composition rules, no rotation, compromised and common lists checked; minimum 8 where MFA is enforced (the default, J3), 15 for any account a password alone authenticates. Django's validators are configured to length and list checks only; the numeric-only check, a composition rule, is removed (mapping of P1 to Django inferred).
  2. **Hashing**: Argon2id first in the hasher list with the OWASP parameters; older hashes upgraded at login (P2).
  3. **Second factor**: MFA required; passkeys and WebAuthn offered (P3; J3).
  4. **Throttling**: generic error messages; failures counted per account and per source; growing delays, never a hard lockout; a recovery path (P4); the limit enforced in the proxy and in the login logic, never by framework throttling alone (P5); one-time-code endpoints count failures only (P6).
- **Rejected**: hard lockout: never, it lets an attacker lock users out (P4). Composition rules and periodic rotation: never (P1). PBKDF2 as the default hasher: acceptable where FIPS-140 applies (P2). Framework throttling as the control: never (P5). MFA optional: acceptable when the audience cannot practically be required to use a second factor (J3's condition), then minimum length 15 (P1).
- **Realizes**: no skeleton link; follows J3 LOGIC.SECURE (layered login defence, L033).
- **State**: `known | unvalidated: the provider bar (authentication-context claims included) and the Django validator mapping are inferred`.

## PIG-WEB.LOGIC.SECURE.6 Abuse and Rate Limits

- **Positions**:
  - P1 two layers: coarse, identity-blind limits and size and time bounds at the proxy or edge; identity-aware limits (per user, API key, plan) in the application (L358; synthesis, no source argues the split).
  - P2 tighter per-client limits for operations that cost money or trigger third parties (SMS, e-mail, exports, uploads, egress), weighted by cost; spending limits and billing alerts with every provider, an alert where a cap is impossible (L359).
  - P3 behind proxies, limit only on addresses appended by a proxy you control, counted from the right of `X-Forwarded-For` (L360).
  - P4 never the address alone as the key: combine it with an account, API key, session or path (L361).
  - P5 limit concurrency as well as rate on heavy endpoints; count, bytes and concurrency are distinct units (L362).
  - P6 a load shedder that reserves capacity for critical requests (L363; one T3 source).
  - P7 roll out a new limit in observe-only mode, escalate gradually, keep a switch (L364).
  - P8 limiter state outside the process (shared cache or the proxy), or accept approximate limits (L365).
  - P9 over-limit answers 429 with an explaining body and `Retry-After`; never cache a 429; the proxy set to 429 where it defaults to 503; RateLimit fields for programmatic clients (L366).
  - P10 quota headers, contested: (a) IETF `RateLimit` and `RateLimit-Policy` (draft, T2); (b) de facto `X-RateLimit-*`; (c) none, 429 and `Retry-After` only (L367).
  - P11 remaining quota is advisory; `Retry-After` takes precedence; a server sends no `Retry-After` earlier than the window's end (L368).
  - Cited: limits at the outermost layer (L032), per operation and business need (L031), harmful flows protected by flow (L034), no blanket bot blocking where agents are users (L652), all via J3.
- **Forces**: availability and cost control; security (brute force, scraping, abuse); agents' ability to pace themselves; scalability of where limiter state lives.
- **Decision**:
  1. **Two layers** (P1, J3). The reverse proxy enforces identity-blind rate, connection, body-size and time limits keyed on the address it appends itself (P3). The backend enforces identity-aware limits keyed on account, API key or session combined with the address (P4), per operation, tighter and cost-weighted on operations that spend money or call third parties (P2), with concurrency limits on heavy endpoints (P5).
  2. **Providers**: a spending cap and a billing alert with every external provider, an alert alone where no cap exists (P2).
  3. **Limiter state** (P8): the proxy keeps its own; the backend's counters live in Postgres, in a rebuildable `UNLOGGED` table, under POSTGRES_FIRST, and move to a shared cache service when measured counter writes load the primary (CACHE_STORE's moving condition) (by analogy; no source).
  4. **Load shedding**: reserved capacity for critical routes (login, the core write paths) when workers saturate (P6).
  5. **Rollout**: observe-only first, then enforce, with a switch (P7). A challenge before blocking (CAPTCHA-like) only on human-only flows named under L034; agents, intended users here (L652), get 429 with RateLimit fields, never a challenge (review m3).
  6. **Signalling**: 429 with a problem-details body (EXPOSE.2), `Retry-After` never earlier than the window's end, `Cache-Control: no-store`; the proxy configured to 429 (P9, P11).
  7. **Quota headers**: IETF `RateLimit` and `RateLimit-Policy` on the JSON interface and the agent surface, so programs and agents pace themselves, marked unstable until the draft is published (P10 (a), P9's agent merge).
- **Rejected**:
  - Proxy-only or application-only limits: never; each misses what the other sees (J3).
  - The leftmost `X-Forwarded-For` value or the address alone as key: never (P3, P4).
  - Per-process in-memory counters: acceptable only for a single-process deployment (P8).
  - `X-RateLimit-*` names: acceptable where existing clients already expect them (P10 (b)).
  - No quota headers: acceptable for HTML pages read by humans (inferred).
  - 503 for an over-limit answer: never (P9).
- **Realizes**: no skeleton link; follows J3 LOGIC.SECURE (limits at two depths) and PIG-WEB.ALLOCATION.POSTGRES_FIRST and CACHE_STORE (limiter state).
- **State**: `known | unvalidated: the two-layer split is a synthesis (L358); counters in Postgres by analogy; load shedder from one T3 source | gap: RateLimit fields are a draft (T2)`.

## PIG-WEB.LOGIC.SECURE.7 Server-Side Fetch

- **Positions**: one. P1 any server-side fetch of an agent- or client-supplied URL blocks private, loopback and link-local ranges, validates each redirect hop and preferably goes through an egress proxy (L662).
- **Forces**: security (requests forged toward internal services and metadata endpoints) against the function itself (metadata documents, webhooks, link previews).
- **Decision**: every fetch of a client- or agent-named URL goes through one fetch helper that refuses private, loopback and link-local addresses, checking the address actually connected to rather than the hostname (inferred), validates every redirect hop the same way, and leaves through an egress proxy: P1's "preferably" made required (max). The helper runs with a timeout and a size cap (PROCESS.3, SECURE.6), and in a worker when the response does not need the result (ACT.3, a foreign effect) (inferred).
- **Rejected**: fetching without range checks: never (P1). Direct egress without a proxy: acceptable when the deployment has no egress proxy; the helper's checks are then the only guard (inferred).
- **Realizes**: no skeleton link; follows ALLOCATION.RULES.3 (client-supplied input never decides).
- **State**: `known | unvalidated: egress proxy required (max applied to "preferably"); connect-time address check inferred`.

## PIG-WEB.LOGIC.ENFORCE Business Logic Realization

- **Positions**: owns no row; roll-up of ENFORCE.1 to .5.
- **Forces**: correctness (one rule, one place); changeability and testability; latency (round trips, L614).
- **Decision**: each backend is one Django deployable, not split into services without a measured need, and several backends may share the database (X5, MD-03); its use-case layer is what every entry point calls (ENFORCE.1); each business operation is one transaction holding the verified actor and one call to a generated wrapper of an API function, and a read that needs the actor runs in a short read-only transaction through the same wrapper (ENFORCE.2); writes only through those wrappers, reads gathered in one statement with filtering, sorting and paging in Postgres (ENFORCE.3); synchronous handlers (ENFORCE.4); Django as the framework (ENFORCE.5).
- **Realizes**: refines LOGIC.ENFORCE (J3); through its children ALLOCATION.ACT.1 and DERIVE.2.
- **State**: `known (roll-up) | unvalidated: framework choice (ENFORCE.5)`.

## PIG-WEB.LOGIC.ENFORCE.1 Use-Case Layer

- **Positions**:
  - P1 define application operations in a use-case (service) layer that every entry point (HTTP, CLI, jobs) calls; one source notes the layer may be unnecessary for web-only applications with controllers alone (L224).
  - P2 thin handlers: parse input, call a use case, map outcomes to status codes (L225).
  - P3 scale layering to domain complexity: transaction script for simple or CRUD logic, a domain model plus use cases when complex; round 4 adds that both keep state transitions in the backend unless the database gate of L527 is met, and that team SQL skill is an input (L226).
  - P4 decouple the domain model from the ORM, or use ORM models as the domain (Active Record): a recorded decision, contested (L227).
  - Cited: one core for every client, adapters translate only (L633, RULES.4); one function call per business operation (ACT.1); MD-03 meets L527's gate by default.
- **Forces**: correctness (one rule, one place); changeability and testability; the cost of structure on simple logic.
- **Decision**:
  1. **One use-case layer per backend, the only way into its logic** (P1): HTML views, JSON endpoints, the agent adapter, management commands and job handlers call the same use-case functions (RULES.4). Handlers parse into Pydantic models (EXPOSE.6), call one use case and map its outcome to a status and a representation (P2). The layer is required even for a web-only backend, because agents and jobs are entry points in the default context, so P1's objection does not apply (inferred).
  2. **A use case holds the backend's share only** (ACT.1): product policy not stored in the data, workflow across operations, external calls. Each business operation on stored data is one call through a port whose implementation is the typed wrappers generated from the function catalogue (DB_API, TYPE_CHAIN). A use case never composes several calls into one business operation; composition across domains happens inside the database, where a function may call another domain's published functions in its transaction, and only direct access to another domain's tables is forbidden (X3).
     - **Overrides of blockable rules** (L530; review M7): the use case, not the adapter, decides whether to set a writer function's override flag, after the policy module authorizes it for the actor (SECURE.1); an adapter never forwards it from client input.
  3. **Transitions stay in the database**: P3's round-4 condition is met, because MD-03 meets L527's gate by default. The backend's own share scales with its complexity: a transaction script for simple orchestration, a domain model of plain Python objects for complex policy and workflow (P3, J3 LOGIC.ENFORCE).
  4. **P4 decided: the domain is decoupled from the ORM.** ORM models are read mappers of the tables the backend reads and are never saved, except for tables under DB_API's direct-write exception (the session table, other single-writer tables the backend owns), because Active Record's save is a direct table write that DB_API forbids for shared tables (inferred from DB_API).
- **Rejected**:
  - Orchestration written in each handler: never (P1, RULES.4).
  - ORM models as the domain (Active Record): acceptable when one backend is the only database consumer and the team's SQL skill is low (ACT.1's condition); L227's "mostly CRUD" criterion then applies.
  - State transitions in backend domain objects: never in the default context (ACT.1, MD-03).
- **Realizes**: ALLOCATION.ACT.1 (holds the use cases the business-rules placement gives the backend).
- **State**: `known | tension: L227's Active Record narrowed by DB_API and L226's backend transitions by MD-03 | unvalidated: ORM models as read-only mappers (inferred)`.

## PIG-WEB.LOGIC.ENFORCE.2 Transactions

- **Positions**:
  - P1 keep transactions short (L228).
  - P2 prefer a use-case-scoped transaction over one around the whole request; a request-wide transaction is acceptable for simple applications (Django `ATOMIC_REQUESTS`, with a warning on overhead) (L229).
  - P3 the safe path by default: nothing persisted unless the use case commits explicitly; roll back on any exception; Django's default autocommit is the opposite (L230).
  - P4 never catch and swallow exceptions inside an atomic block (L231).
  - P5 a database session is stateful and not shareable: one per thread, one per task under async, created and closed at the entry point (L232).
  - Cited: one business operation is one function call in its own transaction, never several calls wrapped (RULES.5, ACT.1, DB_API); the actor in a transaction-local setting from the verified identity (L311, L566); no transaction across a remote call (L234); isolation set per consumer role, its default with the DATA judge (GUARD.2).
- **Forces**: correctness (atomicity, the actor bound to the write); latency and lock time; simplicity.
- **Decision**:
  1. **One business operation, one transaction**, holding exactly two things: the transaction-local actor setting from the verified identity (L311, L566) and one API function call. Commit on success, roll back on any exception (P1, P3; ACT.1). In Django: `transaction.atomic()` around those two statements, `ATOMIC_REQUESTS` off.
  2. Never two API calls in one transaction, never a transaction per request, never one open across a remote call or a user's think time (RULES.5, L234, GUARD.5). Backends never compose several calls into one business operation; a step that must be atomic with another is a database function, which may call another domain's published functions inside its own transaction (X3).
  3. **Reads apart from the write**: a use case reads what it needs in one statement or read function (ENFORCE.3); the write then carries the version it read, so the writer function rejects a decision taken on stale data (GUARD.5).
     - Plain reads (base tables under SELECT grants, no rule needing the actor) run in autocommit.
     - A read that calls a read function needing the actor, or under J1's read-function answer any per-user read (SECURE.1 step 4), runs in a short read-only transaction that sets the actor and makes the one read call, through the same generated wrapper as writes (review M2). In autocommit, a transaction-local setting (`set_config(…, true)`, `SET LOCAL`) is its own transaction and is gone before the next statement, so a read function would see no actor (L311, L566; Postgres scoping inferred, not in the ledger).
     - Read functions refuse a missing actor, as writer functions do (GUARD.3, R1-3).
  4. No exception swallowed inside the block (P4); database errors are mapped after it (EXPOSE.2).
  5. One connection per thread, never shared; one per task under async (P5).
  6. **Retries** (review m1): the wrapper always retries the whole one-call transaction on a serialization failure (SQLSTATE 40001) or a deadlock (40P01), whatever isolation level PIG-WEB.DATA.CONCURRENCY.1 sets: deadlocks occur at every level and serialization failures under Repeatable Read too (Postgres behaviour, inferred, not in the ledger). Retries are bounded by PROCESS.3's caps and safe because nothing committed. When the commit outcome is unknown (connection lost during COMMIT, L479), only calls carrying an idempotency key are retried (GUARD.6) (inferred).
  7. The isolation level is set per consumer role in the database (GUARD.2's hand-off); the backend never lowers it per transaction (inferred from J1's R1-9).
  8. **Tests** (X4): logic tests on shared data run in never-committing transactions (L567); the retry path, lock waits, deferred constraints and the outbox only show at commit and are tested with committing sessions in a disposable database, never a shared one; concurrency tests for the rules GUARD.2 requires (Serializable with retry, locks) are part of the default test suite, not a gap.
- **Rejected**:
  - A request-wide transaction: it would wrap several calls and the whole request; acceptable when one backend is the only database consumer (ACT.1's condition) and the request makes no remote call (P2, L234).
  - A use-case transaction spanning several statements composed in Python (P2 as stated): acceptable only under the same single-consumer condition (narrowed by ACT.1, MD-03).
  - Autocommit for writes, and for reads that need the actor: the actor setting must share the function's transaction (L311, L566; review M2; inferred from Postgres scoping).
  - Retrying only when Serializable is set: rejected; 40001 and 40P01 occur outside it (review m1).
- **Realizes**: no skeleton link; follows ALLOCATION.ACT.1, RULES.5 and PIG-WEB.ALLOCATION.DB_API (proposed link to ACT.1).
- **State**: `known | tension: L229's use-case-scoped transaction narrowed to one function call (ACT.1, RULES.5) | unvalidated: transaction-local scoping in autocommit and the retryable error codes (Postgres behaviour, not in the ledger)`.

## PIG-WEB.LOGIC.ENFORCE.3 Data Access

- **Positions**:
  - P1 an ORM for routine mapping, understanding the relational model, with a sanctioned route to hand-written SQL; explore the ORM first (L235).
  - P2 raw SQL always uses bound parameters, never string formatting (L236).
  - P3 reads that need no domain behaviour may bypass the domain model: hand-written SQL, views, denormalized tables, separate read stores (L237).
  - P4 each extra round trip adds latency: fetch related data in one statement, no queries in loops (L614).
  - Cited: writes through the API functions, simple reads on base tables under SELECT grants, read functions where a read applies a rule, views never a contract (DB_API, L516); reduction in the database, keyset pages, a server maximum page size (DERIVE.2); wrappers generated from the catalogue (TYPE_CHAIN).
- **Forces**: correctness; security (injection); latency; changeability.
- **Decision**:
  1. **Writes**: only through the generated, typed wrappers of the API functions (DB_API, TYPE_CHAIN); the ORM writes only tables under DB_API's direct-write exception.
  2. **Reads**, one read layer under the Django default (review m7): the Django ORM, its models used as read-only mappers, for simple reads on base tables under SELECT grants (L516); read functions, called through the generated wrappers, where a read must apply a rule (DB_API), in a short read-only transaction when they need the actor (ENFORCE.2). Each use case gathers its data in one statement or read function, related rows joined or eagerly loaded in that statement, never queries in loops (P4; J3's "data in, decision out"). Filtering, sorting and paging in the statement, keyset pages, the server's maximum page size (DERIVE.2, EXPOSE.1).
  3. **Raw SQL**, where the ORM cannot express a read, through Django's database connection, always with bound parameters (P2); identifiers that must vary come from an allowlist (inferred).
  4. **Per-user read rules** (`undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`, SECURE.1): at the recorded default, applied inside the read statement from the shared specification, never by filtering loaded rows in Python (DERIVE.2); for collections, the policy module's query predicate goes into the statement (SECURE.1, review m8). **Under J1's read-function answer** (review M1): the read goes through the read function, run with the actor set (ENFORCE.2), and the table loses direct SELECT, so step 2's "simple reads on base tables" no longer covers it. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted (X1).
  5. **Read models**: derived data from database cache tables or derived columns (DERIVE.1); no view as a contract (L516); no read store outside the database (RECORD.1).
- **Rejected**:
  - Views as a read contract (P3's views): never (L516, DB_API); acceptable only as throwaway objects no consumer depends on.
  - Read stores outside Postgres (P3's separate stores): acceptable under DERIVE.1's condition (many external derived stores at a high write rate).
  - ORM-first writes (P1 as stated): acceptable when one backend is the only consumer (L527's default then applies).
  - Loading full sets into Python to reduce them: never (DERIVE.2).
  - A second query layer (SQLAlchemy Core) beside the Django ORM: rejected under the Django default (review m7); acceptable as the read layer of a backend whose framework is not Django (inferred).
- **Realizes**: ALLOCATION.DERIVE.2 (pushes filtering and aggregation to the database).
- **State**: `known | tension: L235's ORM-first and L237's views and separate stores narrowed by DB_API, L516 and DERIVE.1 | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (step 4 changes under the read-function answer)`.

## PIG-WEB.LOGIC.ENFORCE.4 Concurrency Model

- **Positions**:
  - P1 default to synchronous handlers; adopt async only where in-process I/O concurrency pays (many external calls, streaming, long-lived connections); async is not inherently faster (L238).
  - P2 never run blocking code on the event loop; use `def` handlers or executors for blocking libraries (L239).
  - P3 async data access has hard constraints: Django transactions do not work in async mode (wrap transactional code in one synchronous function; version-dependent); SQLAlchemy needs one `AsyncSession` per task, no lazy loading, `expire_on_commit` off (L240).
  - P4 under Django's async mode: `CONN_MAX_AGE` 0, a pool sized to in-flight query concurrency, database work short and outside the lifetime of long-lived connections (L241).
- **Forces**: simplicity and correctness of transactions; throughput for long-lived connections.
- **Decision**: synchronous handlers on a synchronous application server by default (P1): the HTML and JSON request paths are synchronous. Asynchronous code only in the separate process type that holds long-lived connections (real-time channels, agent streams; PIG-WEB.INTERACTION.REALTIME.3, PIG-WEB.TRANSVERSE.TOPOLOGY) or in a handler that fans out many concurrent external calls. There P2 to P4 apply: nothing blocking on the loop; every transaction in one synchronous function (Django) or one `AsyncSession` per task (SQLAlchemy); `CONN_MAX_AGE` 0 and a pool sized to in-flight queries; no database work held for a connection's lifetime (L094 via J3 LOGIC.PROCESS).
- **Rejected**: async everywhere: acceptable when a process is dominated by long-lived connections or concurrent external I/O (P1). Blocking calls on the event loop: never (P2).
- **Realizes**: no skeleton link; follows J3 LOGIC.PROCESS (no connection or transaction per connected client).
- **State**: `known`.

## PIG-WEB.LOGIC.ENFORCE.5 Framework Choice

- **Positions** (L242, contested; no T1 or T2 source gives neutral criteria, gap):
  - P1 Django: batteries included, ORM, loose coupling, Active Record models (SRC-009).
  - P2 Flask: micro, no database layer, thread locals, "not designed for large applications or asynchronous servers", async through threads at a cost (SRC-124, SRC-126).
  - P3 FastAPI: ASGI, dependency injection, `def` and `async def` handlers, router modules for larger applications (SRC-031, SRC-032, SRC-030); its official security tutorial teaches a JWT bearer flow and does not address cookies, sessions or revocation (L317).
  - The row's own rule: the framework is a recorded decision whose criteria are the product's needs.
- **Forces**: security of the browser path (sessions and CSRF from the framework, L323, L330); correctness of the contract chain (Pydantic models, TYPE_CHAIN); changeability (one framework the team knows).
- **Decision**: **Django is the default for the default context**, recorded as a decision with these criteria, each taken from a settled verdict rather than from a source ranking:
  1. server-held, revocable sessions in Postgres from the framework's own session management (GUARD.4, L323): Django documents a database session backend (SRC-021); no FastAPI page read documents sessions (L317);
  2. the framework's built-in CSRF protection (L330, SECURE.3): documented by Django (SRC-024);
  3. server-rendered HTML with forms as the default contract (PRESENT.1, JS_SERVER);
  4. synchronous handlers by default (L238, ENFORCE.4);
  5. password hashing and validators built in, Argon2 opt-in (L344, L345).
  - Costs accepted: Django's Active Record and admin are constrained by DB_API (models of shared tables are read mappers; an admin console does not write shared tables directly, because consoles are an operator role calling the API functions); Pydantic parsing (TYPE_CHAIN) is added as a library; how Pydantic models and the OpenAPI description are produced under Django was not read (gap). MD-02's gate depends on it, so the gap names a candidate to verify (review m7): Django Ninja, which builds on Pydantic and generates an OpenAPI schema (its front page, fetched by the reviewer); to verify: OpenAPI 3.1 output and Pydantic v2 support. Forms keep Django's form handling for HTML rendering, with Pydantic as the parsing step at the boundary (EXPOSE.6; inferred); Django's task framework needs a worker backend, here PROCESS.1's Postgres queue (L408).
  - Consistent with the sibling Python guideline's scenario page (`../../../../../python_guidelines/LOD_2_phases/7.1_scenarios.md`: full web application, Django; API-first, FastAPI); that page is not ledger evidence.
- **Rejected**:
  - FastAPI: wins when the backend serves only programs and agents with bearer tokens (no browser session, no forms), so the session and CSRF criteria fall away and native Pydantic models and OpenAPI generation dominate (inferred from L242, L317, TYPE_CHAIN).
  - Flask: acceptable for a small backend not expected to grow; rejected as the default by its own design statement (L242).
- **Realizes**: no skeleton link; serves ALLOCATION.GUARD.4, ALLOCATION.PRESENT.1 and PIG-WEB.ALLOCATION.TYPE_CHAIN.
- **State**: `known | unvalidated: criteria derived from settled verdicts, no neutral source (L242) | gap: Pydantic and OpenAPI production under Django not read (candidate to verify: Django Ninja, OpenAPI 3.1 output, Pydantic v2)`.

## PIG-WEB.LOGIC.PROCESS Processing and Side Effects

- **Positions**: owns no row; roll-up of PROCESS.1 to .6 (PROCESS.7 deferred).
- **Forces**: correctness (no lost or doubled effect); availability; security of files.
- **Decision**: deferred work and side effects are rows that database functions write in the transaction of the change, claimed by Python workers with `SKIP LOCKED` inside the job table's writer functions and delivered at least once to idempotent consumers (PROCESS.1, PROCESS.2); foreign mutations run as atomic phases in a worker, the request answering 202 with a status resource (PROCESS.2, EXPOSE.3); outbound calls are bounded in time and retried at one layer only (PROCESS.3); files go directly to object storage under a constrained policy, are tracked as rows with a state column and one writer function, are scanned before anyone can read them, and are served through an authorization check and a short-lived signed URL (PROCESS.4 to .6).
- **Realizes**: refines LOGIC.PROCESS (J3); through its children PIG-WEB.ALLOCATION.JOB_HOST and ALLOCATION.ACT.2.
- **State**: `known (roll-up)`.

## PIG-WEB.LOGIC.PROCESS.1 Background and Scheduled Jobs

- **Positions**:
  - P1 in-process background execution only for small tasks that need the same process; a task queue for heavy, durable or multi-server work; an async view in a WSGI Flask app cannot spawn tasks (L407).
  - P2 Django's task framework ships no worker and its built-in backends are for development and testing; production needs a third-party backend and a separate worker (L408).
  - P3 task arguments are small serializable data (ids), re-fetched inside the task (L411).
  - P4 a task never waits synchronously for another; chain instead (L412).
  - P5 a Postgres-backed queue claims rows with `FOR UPDATE SKIP LOCKED`, which suits queue-like tables only (L413).
  - P6 scheduled jobs are short, idempotent, error-handled so a failure shows in the job history, descriptively named, heavy work off-peak, with no overlapping schedules and a documented expected duration; monitor failures, duration, missed runs (no run within twice the interval) and backlog (L605, MAINT).
  - Placement: JOB_HOST (queue table written by the database function, claimed by Python workers; data schedules in the Postgres scheduler; a schedule that needs Python inserts a job row; no enqueue outside the data transaction; L126, L409, L604).
- **Forces**: correctness (the job atomic with its data); durability; changeability (one component fewer); scalability.
- **Decision**:
  1. **Host, as JOB_HOST sets**: job rows written by the database function in the transaction of the change that needs them (MD-03); Python worker processes, a separate process type (J3 LOGIC.PROCESS), claim them with `FOR UPDATE SKIP LOCKED` (P5). Pure data schedules run in the Postgres scheduler as calls to named functions (L604); a schedule that needs Python inserts a job row.
  2. **Claim protocol**: job status is a state column, so claim, outcome and expiry go through the job table's writer functions (L596, MAINT; review m6). The claim function selects with `FOR UPDATE SKIP LOCKED` inside itself and marks the job running with an expiry, in one short call; the worker does the work with no transaction held over it; it records the outcome through the outcome function; a job whose expiry passes is claimable again; on SIGTERM the worker returns its job through the same functions (L088 via J3) (inferred from L234, L410, L088).
  3. **Jobs**: ids as arguments, re-fetched (P3); idempotent, because delivery is at least once (L410); never waiting on another job, chained by inserting the next job row (P4); short, named, error-handled so every failure is recorded and visible, no overlapping schedules, a documented expected duration, heavy work off-peak (P6, max).
  4. **Monitoring**: failures, duration, missed runs (no run within twice the interval) and backlog age (P6); JOB_HOST's moving condition (contention, backlog) is measured from these.
  5. **In-process background work**: only for small work that may be lost (P1, ACT.3).
  6. **Library**: any runner that claims from this table. A framework task backend that enqueues by its own insert from Python, outside the database function's transaction, is not used for work that must not be lost (L409, JOB_HOST). Which runner: open (none read).
- **Rejected**: a broker (Celery with Redis or RabbitMQ) from the start: wins at measured lock contention, backlog or multi-server fan-out, and then as a drain from the Postgres stage, never as an enqueue outside the data transaction (JOB_HOST, L126). In-process tasks for durable work: never (P1). Tasks blocking on tasks: never (P4).
- **Realizes**: PIG-WEB.ALLOCATION.JOB_HOST (runs jobs and schedules on the host the placement names).
- **State**: `known | unvalidated: claim protocol with expiry through writer functions (inferred) | gap: no Python runner over a queue table written by database functions was read`.

## PIG-WEB.LOGIC.PROCESS.2 Side Effects and Delivery

- **Positions**:
  - P1 trigger side effects (e-mail, enqueue, publish, cache invalidation) only after commit, through post-commit hooks (L233).
  - P2 never hold a database transaction open across calls to remote services; bracket each foreign mutation with its own short local transactions (L234; synthesis).
  - P3 a data change and a message cannot be made atomic by two writes: record the message or job in the same transaction (outbox, staged job table) and deliver after commit (L409).
  - P4 relays and queues deliver at least once, so consumers and tasks are idempotent (processed message ids); late acknowledgement only for idempotent tasks (L410).
  - P5 record the idempotency key and the effect atomically (L270, grounded since by L599).
  - P6 for a request that mutates foreign state: atomic phases, a recovery point after each phase and foreign call, commit before the foreign call, an idempotency key passed to the foreign system, a completer for abandoned requests and a reaper for old keys (L589; one T3 source).
  - P7 within one Postgres, one local ACID transaction, not a saga; sagas only across services with separate databases, accepting their lack of isolation and hand-written compensations (L590).
  - P8 the receiver records processed messages in the transaction of its state change and answers a repeat as it answered the first (L599).
  - P9 a post-commit hook is not part of the transaction: a crash after commit loses the effect, a failing hook can skip later ones unless robust; use it for losable work, the outbox when the follow-up must not be lost; enqueuing before commit lets a worker see uncommitted data, after commit risks a crash between the two (L600).
- **Forces**: correctness (no lost, early or doubled effect); request latency.
- **Decision** (ACT.2):
  1. Every effect that must not be lost is an outbox or job row written by the database function in the transaction of the change (P3, ACT.2, MD-03); Python workers deliver it after commit (PROCESS.1's claim).
  2. Delivery is at least once and every consumer idempotent: the receiver records the processed message id in the transaction of its own state change and answers a repeat as the first (P4, P8); late acknowledgement only for idempotent tasks (P4).
  3. **Foreign mutations** (a payment): atomic phases (P6) **run in a worker** (review M4). The request writes the intent with its idempotency key through one API function call and answers 202 with a status resource (EXPOSE.3, ACT.3); the worker runs the phases. Each local phase is one API function call that records a recovery point on the key row; commit before each foreign call; the idempotency key passed to the foreign system; a completer job for abandoned operations and a reaper for old keys (PROCESS.1). The key row carries the recovery point and a lock with an expiry, so a duplicate request is answered by EXPOSE.3's multi-phase rule (review M3).
     - In-request phases are acceptable when the user must see the foreign outcome in the same response and the call fits ACT.3's 1 s budget.
     - Grounds: J1's ACT.2 allows in-request atomic phases while ACT.3 forbids foreign effects inside the request; the worker path satisfies both, and matches this branch's refusal to hold synchronous workers on slow I/O (PROCESS.4, ENFORCE.4). The tension is J1's own and is routed to J1's owner.
  4. Never a transaction open across a remote call (P2).
  5. Post-commit hooks only for losable work (cache invalidation, best-effort notices), registered as robust so one failure does not skip the others (P9; P1 narrowed).
  6. No saga inside one Postgres (P7).
- **Rejected**: post-commit hooks as the default carrier: acceptable for losable work (P9). Enqueueing to a broker before or after commit: never (P9, L409). Sagas: win when a business transaction spans services with separate databases (P7, L480). Foreign mutations inside the request by default: rejected (ACT.3's forbidden column; review M4); acceptable under step 3's condition.
- **Realizes**: ALLOCATION.ACT.2 (stages and delivers side effects as the placement sets); follows ALLOCATION.ACT.3 (foreign effects deferred).
- **State**: `known | tension: L233's post-commit hooks narrowed to losable work by L600; J1's ACT.2 (in-request phases) against ACT.3 (no foreign effect inside the request), resolved by the worker path and routed to J1's owner | unvalidated: atomic phases rest on one T3 source (L589)`.

## PIG-WEB.LOGIC.PROCESS.3 Resilience

- **Positions**:
  - P1 expect transient faults on calls to external services: bounded retries with increasing, spread delay, only for idempotent operations; fail fast with few retries in interactive requests, retry more in batch work (L243).
  - P2 retry at one layer only; cap per-request and per-client retries (three attempts, a 10% retry ratio) (L244).
  - P3 for persistent faults, fail fast with a circuit breaker and timeouts short enough to protect threads and connections; a breaker never replaces business exception handling (L245).
  - P4 for calls that mutate foreign state, client-supplied idempotency keys and recorded recovery points (L246; one T3 source).
- **Forces**: availability; correctness (no duplicated foreign effect); latency.
- **Decision**:
  1. Every outbound call has a timeout shorter than its caller's remaining deadline (P3; "shorter than the deadline" inferred).
  2. Retries only for idempotent operations or calls that carry an idempotency key (P1, P4, GUARD.6); exponential backoff with jitter.
  3. **One retrying layer** (P2). In the request path, the outbound client retries within the request's deadline: at most three attempts and a 10% retry budget per client. Foreign mutations are not in the request path by default (PROCESS.2 step 3, review M4); request-path retries cover idempotent calls and the in-request phases PROCESS.2 admits under its condition. For deferred work, the job runner is the one retrying layer, with more attempts and growing delays, then a failed state that monitoring shows (PROCESS.1, L605). HTTP client libraries do not retry on their own beneath either layer.
  4. A circuit breaker per external dependency called from the request path; business errors are handled as business errors (P3).
  5. Foreign mutations carry keys and recovery points (P4, realized by PROCESS.2's atomic phases). Database retries (serialization failure, unknown commit) follow ENFORCE.2.
- **Rejected**: unbounded or immediate retries: never (P1). Retries at several layers: never (P2). Retrying a non-idempotent call without a key: never (P1).
- **Realizes**: no skeleton link; follows ALLOCATION.ACT.2 and GUARD.6.
- **State**: `known`.

## PIG-WEB.LOGIC.PROCESS.4 File Upload Path

- **Positions**:
  - P1 bytes travel from the browser directly to object storage; the application authorizes and issues a short-lived credential (L421; a capability in vendor documentation, the load benefit inferred).
  - P2 bytes travel through the application, which streams, validates and stores them (L421; OWASP and framework documentation assume it).
  - P3 L421's own split: direct for large or numerous files, through the application for small files that need synchronous validation; no source weighs the two, the size threshold is open.
  - P4 a presigned URL is a bearer token: a random key chosen by the server, one operation on one key, a short expiry, the requester authorized first (L422).
  - P5 when storage must enforce limits on a browser upload, a POST policy with a content-length range, an exact content type and a key prefix (L423).
  - P6 multipart or resumable upload for large files, checksums, and a lifecycle rule that deletes incomplete uploads (L424).
  - P7 gates on the upload endpoint: authenticated and authorized uploaders, size and filename-length limits, post-decompression size for archives, CSRF protection (L425).
  - P8 stream uploads in the application instead of reading them whole (Django `chunks()`, FastAPI `UploadFile`) (L426).
  - P9 set the body-size limit in the web server as well as the framework (L427).
- **Forces**: security (validation, abuse); availability (synchronous workers not held by transfers); latency of the user's feedback.
- **Decision**: **direct to object storage is the default path for user files.**
  1. The backend authorizes the uploader (SECURE.1), records a pending upload row through an API function (PROCESS.5), and issues a POST policy for one random server-chosen key with a content-length range, an exact content type, a key prefix and a short expiry (P4, P5). A plain HTML form can post to it, so the path needs no browser script (inferred from P5). This signed policy is the one kind of credential allowed in a URL or form target (X6), with its scope and lifetime stated: scope, one upload to one key under the policy's limits; lifetime, minutes, the value recorded per project (no source gives a number; L422's "short expiry" is itself inferred).
  2. Large files: multipart or resumable with checksums; a lifecycle rule deletes incomplete uploads (P6).
  3. The bytes are checked after arrival by the scanning path, and nobody can read them before (PROCESS.5), so synchronous validation in the application adds no safety here (inferred).
  4. The endpoint that issues the policy carries the gates (P7): authentication, authorization, CSRF, size and filename limits; archives are checked for post-decompression size by the scanner.
  - **Through the application** is acceptable when a small file's content must be read within the same request (an import validated before the response): then streamed (P8), with body-size limits at the proxy and in the framework (P9), and the same gates (P7).
- **Rejected**: through the application as the default: it ties synchronous workers (ENFORCE.4) to transfers and puts every byte through the backend; wins in the condition above (P3). An unconstrained presigned URL when storage must enforce limits: never (P5).
- **Realizes**: no skeleton link; follows ALLOCATION.GUARD.1 (every part of an upload untrusted, L023 via J3) and GUARD.3.
- **State**: `known | unvalidated: direct as the default (no source weighs the two, L421); the HTML form posting to storage (inferred) | gap: whether a presigned PUT can bound size was not verified (L423)`.

## PIG-WEB.LOGIC.PROCESS.5 File Scanning and Storage

- **Positions**:
  - P1 scan untrusted uploads with antivirus or a sandbox, and apply content disarm and reconstruction to document formats such as PDF and Office, before any other user can open them (L428; consensus on scanning, majority on mechanism).
  - P2 for asynchronous scanning in storage, objects unreadable until the scan reports clean (tag-based access), and a consumer that tolerates duplicate scan results (L429; one vendor).
  - P3 each upload a Postgres row with an explicit state: pending when the URL is issued, available only after storage confirmation and a clean scan, failed or expired otherwise; a sweep for rows and objects that never complete (L430; inferred, no source gives the state machine).
  - P4 metadata (key, owner, size, content type, checksum, state) in Postgres, bytes in object storage; `bytea` only for small files that must commit atomically with other data (L431).
  - Cited: one writer function per state column (L596, ACT.1); idempotent consumers (L410).
- **Forces**: security (malware reaching other users); correctness of each file's state.
- **Decision**:
  1. Every upload is a Postgres row (key, owner, size, content type, checksum, state); the bytes live in object storage (P4).
  2. **The state column has one writer function** (L596, MD-03): pending at issue; available only after storage confirmation and a clean scan; failed or expired otherwise. A scheduled sweep expires stale pending rows and deletes their objects (P3, PROCESS.1).
  3. **Signature check** (review m2; L023 via J3 LOGIC.SECURE P2): before availability, the worker verifies the file's actual signature against an allowlist of types and sets the stored content type from it, not from the declared header. The POST policy's "exact content type" binds only the declared header, not the bytes (L423). A mismatch moves the row to failed through the writer function.
  4. **Scanning** runs asynchronously, in a worker or the storage provider's scanner, with content disarm and reconstruction for document formats before availability (P1); objects stay unreadable until clean (P2); scan results reach the writer function idempotently, duplicates absorbed (P2, L410).
  5. No download URL is issued for a row that is not available, to the uploader either (stricter than P1's "any other user"; one gate; inferred).
  6. `bytea` only for small files that must commit atomically with other data (P4).
- **Rejected**: serving a file before a clean scan: never (P1). Trusting the declared content type: never (L023). Bytes in Postgres by default: acceptable for small files that must commit with other data (P4).
- **Realizes**: no skeleton link; follows ALLOCATION.ACT.1 (writer function for the upload state; proposed link).
- **State**: `known | unvalidated: state machine (L430) and the uploader gate inferred | gap: scanning and reconstruction read only as one managed vendor service`.

## PIG-WEB.LOGIC.PROCESS.6 File Serving

- **Positions**:
  - P1 store uploads outside the web root or on another host; serve publicly reachable ones through a handler that maps an identifier to the stored object, never a file path (L432).
  - P2 serve with the correct stored `Content-Type`, `X-Content-Type-Options: nosniff`, and `Content-Disposition: attachment` with a sanitized filename for anything not meant to render inline (L433).
  - P3 serve private files through the application's authorization check, redirecting to a short-lived signed download URL instead of proxying bytes or exposing a public bucket (L434; the redirect is a synthesis).
- **Forces**: security (access, content sniffing, script in user content); availability (bytes off the application).
- **Decision**: the backend maps a file id to its row (P1), checks authorization (SECURE.1: product policy and the per-user read rule, the latter `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`) and the available state (PROCESS.5), then redirects to a short-lived signed URL for that one object (P3), served from the storage host, an origin other than the application's (P1, EXPOSE.5), with the stored content type, `nosniff`, and `attachment` with a sanitized filename unless the type is one meant to render inline (P2). The redirect response is `private, no-store` (EXPOSE.4; inferred).
  - **The signed URL is the one allowed exception to "no credential in a URL"** (X6): single-purpose (a GET of one object), scope-limited (that object, no listing), lifetime minutes, the value recorded per project (no source gives a number).
  - **Under J1's read-function answer** (review M1): the per-user check is the file row's read through a read function, run with the actor set (ENFORCE.2), instead of the backend's statement; the file table loses direct SELECT.
- **Rejected**: a public bucket for private files: never (P3). Exposing storage paths: never (P1). Proxying the bytes through the application: acceptable when the storage cannot sign URLs or the bytes must be transformed on the way (inferred).
- **Realizes**: no skeleton link; follows ALLOCATION.GUARD.3.
- **State**: `known | unvalidated: the redirect pattern is a synthesis (L434) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (the per-user check moves into a read function under the read-function answer)`.

## PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery [deferred]

Not judged (scope out, `judge_plan.md`). Related placement ALLOCATION.ACT.2. When it is judged, it inherits PROCESS.2 (outbox delivery to idempotent consumers) and SECURE.6 (tighter limits and spending alerts on operations that trigger third parties, L359).

## PIG-WEB.LOGIC.EXPOSE HTTP Interface

- **Positions**: owns no row; roll-up of EXPOSE.1 to .7.
- **Forces**: security and correctness of what callers can do; readability for browsers, programs and agents; changeability (independent evolution of client and server).
- **Decision**: HTML hypermedia for browsers; a resource-oriented JSON interface for programs and agents, served under `/v1` from the start, with named resources, custom methods for state transitions and keyset continuation paging (EXPOSE.1, EXPOSE.7); RFC 9457 problem details with stable types, function error codes mapped to them (EXPOSE.2, L530); idempotency by design or by key recorded with the effect, split by operation shape, and 202 status resources for long operations and foreign mutations (EXPOSE.3); every response labelled for caches, application caches in Postgres (EXPOSE.4); one origin, CORS only for real cross-origin consumers (EXPOSE.5); Pydantic models at every entry, every interface description in sync (OpenAPI 3.1, the function catalogue, the agent tool surface; EXPOSE.6, X7); additive evolution under a CI gate, server first then client for new request fields, a new major version only for an unavoidable break (EXPOSE.7).
- **Realizes**: refines LOGIC.EXPOSE (J3); through its children ALLOCATION.DERIVE.2, GUARD.1, GUARD.6, ACT.3 and PIG-WEB.ALLOCATION.CACHE_STORE, TYPE_CHAIN.
- **State**: `known (roll-up)`.

## PIG-WEB.LOGIC.EXPOSE.1 Contract Style and Resources

- **Positions**:
  - P1 GraphQL as a third option when many clients need different field subsets of one graph; its own pages claim versionless evolution and say the specification is silent on network, authorization and pagination (L256; advocate pages only, T3).
  - P2 in a hypermedia design the HTML (links, forms) is the contract, and an OpenAPI file is needed only for the JSON endpoints that exist (L257; inferred).
  - P3 a data API as a hierarchy of named resources manipulated by a small set of standard methods; custom methods only where standard ones do not fit; Fielding dissents on fixing hierarchies in advance (L264).
  - P4 every collection paginated, the server enforcing a maximum page size and coercing larger requests (L265).
  - P5 paging by a server-issued continuation (opaque token or next link), not offset and limit (L266).
  - P6 page tokens opaque, unparseable by clients, carrying no authorization; the end signalled by an empty token or no next link (L267).
  - P7 a total count is optional; an estimated total is documented as an estimate (L268).
- **Forces**: changeability; readability for programs and agents; performance (DERIVE.2); security (tokens that carry no authority).
- **Decision**:
  1. **Browsers**: the server-rendered HTML is the contract (P2; J3 LOGIC.EXPOSE.3); OpenAPI describes only the JSON endpoints that exist (P2).
  2. **Programs and agents**: resource-oriented JSON over HTTP with named resources and standard methods (P3). State transitions are custom methods on their resource (a POST naming the transition), each mapped to its one writer function, never a PATCH of the state field (inferred from P3 with L596).
  3. **Collections** (P4 to P7): every collection paginated, the server's maximum page size enforced; keyset paging in the database (DERIVE.2) behind an opaque continuation token or next link; the token encodes position only and carries no authorization, so every page is re-authorized and the token is not a credential in the URL (X6); no next link ends the collection; no total count by default, an estimate labelled as such where offered.
  4. HTML lists page the same way, with next links built from the keyset (inferred).
- **Rejected**: GraphQL: acceptable when many clients need different field subsets of one graph and the team designs authorization, pagination and limits itself (P1). Offset and limit for client-facing collections: never (P5). PATCH of a state column owned by a writer function: never (inferred). RPC tunnelling of every operation: rejected (J3 LOGIC.EXPOSE.1).
- **Realizes**: ALLOCATION.DERIVE.2 (exposes paging and filtering in the contract).
- **State**: `known | unvalidated: custom methods for state transitions (inferred from L264, L596); the OpenAPI-only-for-JSON corollary (L257, inferred)`.

## PIG-WEB.LOGIC.EXPOSE.2 Status Codes and Errors

- **Positions**:
  - P1 precise codes: 409 for a conflict with current state, 412 for a failed precondition, 428 when a precondition is required, 422 for well-formed but unprocessable content (L259).
  - P2 errors as RFC 9457 problem details (`application/problem+json`) (L261, majority); against Google's `google.rpc.Status` with mandatory `ErrorInfo` and Azure's top-level `error` object with a code header.
  - P3 the body supplements the status line; its `detail` helps the client correct the problem, never exposes stack traces or internals (L262).
  - P4 clients ignore extension members they do not recognize, so problem types can evolve (L263).
  - Cited: a stable machine-readable identifier separate from the message (L052 via J3); correction hints for agent tools (L656); named constraints map to stable errors (L495 via GUARD.2); function errors name the function and carry stable custom codes, with an explicit override flag for blockable business rules (L530, MAINT, owned by DATA; review M7).
- **Forces**: machine handling by programs and agents; security (no internals); changeability.
- **Decision**:
  1. Every JSON error is `application/problem+json` (P2) with a stable `type` URI per error kind (L052), the status that matches it (P1), and a `detail` that tells the caller, agent tools included, how to correct the request (L656), never internals (P3); extensions are documented and ignored by clients that do not know them (P4).
  2. **Database errors map to problem types**: each named constraint (L495) and each stable custom code a function raises (L530, MAINT; review M7) maps to one type. An error from a blockable business rule maps to a distinct type that names the override, so a caller sees that an authorized override exists; whether the override is set is decided by the use case after the policy module authorizes it (ENFORCE.1, SECURE.1), never by passing the flag through from the request. A stale version gives 412, a missing required precondition 428, a conflict with current state 409, well-formed but invalid input 422, malformed input 400, and an idempotency key reused with another payload 422 (L546).
  3. HTML responses use the same status codes, with a page for humans.
- **Rejected**: Google's and Azure's formats: acceptable when the API joins an ecosystem that already uses them (L261's other positions; condition inferred). Messages as the only error signal: never (L052).
- **Realizes**: no skeleton link; follows ALLOCATION.GUARD.5 (412, 428) and GUARD.1.
- **State**: `known | unvalidated: the distinct problem type for blockable-rule errors (inferred from L530)`.

## PIG-WEB.LOGIC.EXPOSE.3 Retries and Asynchronous Operations

- **Positions**:
  - P1 design POST and PATCH idempotent by nature (client-supplied identifiers, upserts, conditional requests); add a key where impossible; contested between natural idempotence (Zalando), a header (Stripe, the IETF draft) and a body field `request_id` (AIP-155) (L655).
  - P2 for POSTs that create or charge: a client-generated unique key, the stored first response returned on repeat, the same key with another payload rejected, key retention documented; header or body-field forms differ by source (L269).
  - P3 the key contract: never reused with another payload (422); a retry arriving while the first runs gets 409, or is serialized behind a locked key row (SRC-267); a missing required key gets 400; a published expiry; a scoped lookup (per user); the first response replayed. Replay positions: the first result including errors (Stripe v1), completing the work on retry (Stripe v2), or the current state (AIP-155); retention 24 hours or a reaper at 72 hours (L546).
  - P4 operations that may outlast a request return 202 with a status-monitor URL; thresholds differ (1 s, 10 s) (L271).
  - P5 the status resource: 202 with `Location` and `Retry-After`; a closed status set (pending, running, succeeded, failed, canceled); `createdAt` and `lastUpdatedAt`; an RFC 9457 error when failed; a retention policy (`Expires`); 303 to the result; DELETE to cancel; never polling the target and reading 404 as "not yet" (L602).
  - P6 the accepted job record is durable before the 202; the submit carries an idempotency key (L603).
  - Placements: GUARD.6 (the key recorded by the API function in the effect's transaction; required on agent mutations not idempotent by design and on payment-like creates); ACT.3 (a 1 s budget; 202 with a status resource).
- **Forces**: correctness (no duplicate effect, no lost acceptance); simplicity; interoperability with existing clients.
- **Decision**:
  1. **Natural idempotence first** (P1; L587, MAINT, the doctrine's max: mutations whose re-run affects no further rows, by absolute assignments, upserts or conflict-ignoring inserts and self-limiting predicates; review m12): PUT to client-chosen identifiers, upserts, conditional updates with `If-Match` (GUARD.5).
  2. **Otherwise an `Idempotency-Key` header** (P2), required on every mutation offered to agents that is not idempotent by design, on payment-like creates and on 202 submits (GUARD.6, P6). HTML forms carry the form token minted at render (GUARD.6; browser share in PIG-WEB.INTERACTION.EDIT); the agent adapter maps its tool-call key onto the same field (inferred).
  3. **The key is recorded by the API function in the transaction of the effect, scoped to the acting user** (P3, GUARD.6). Consequences (inferred from GUARD.6 and L270): only committed outcomes are stored and replayed; a request that committed nothing leaves no key, so its retry re-executes, which is safe; the same key with another payload gets 422; a missing required key gets 400. A duplicate arriving while the first is in flight is answered by operation shape (review M3):
     - **Single-call operation** (one function call, one short transaction): the duplicate waits on the key's unique index, then gets the replay.
     - **Multi-phase operation** (atomic phases around a foreign call, PROCESS.2, L589): the key row is committed in the first phase, before any outcome exists, and carries the recovery point and a lock with an expiry. A duplicate that finds the key locked gets 409 with `Retry-After` (L546); after completion it gets the replay; a duplicate that finds an expired lock does not re-run the phases itself: the completer resumes the operation from its recovery point (L589), and the duplicate gets 409 with `Retry-After` until then. Re-executing from the recovery point in the duplicate's request would run the foreign call twice in parallel.
  4. **Retention**: published, at least 24 hours (P2), keys reaped by a scheduled job (PROCESS.1).
  5. **Long operations and foreign mutations** (ACT.3's 1 s budget; foreign effects are deferred, PROCESS.2 step 3, review M4): 202 with `Location` of a status resource and `Retry-After` (P4, P5); the job record is written by the API function before the 202 goes out (P6, JOB_HOST); the status resource has the closed status set, both timestamps, problem details on failure, an `Expires` retention, 303 to the result when done and DELETE to cancel; clients never poll the target resource (P5).
- **Rejected**:
  - The body field `request_id`: acceptable in RPC-style APIs where headers are awkward (P1).
  - Replaying stored failures (Stripe v1): never in this stack, because the key commits with the effect (GUARD.6); a separate key store is forbidden by GUARD.6.
  - Answering 409 to a concurrent duplicate of a single-call operation: rejected, because one-call transactions are short and waiting yields the replay (inferred). 409 with `Retry-After` is the answer for multi-phase operations (step 3, L546; review M3).
  - Returning the current state (AIP-155): acceptable for naturally idempotent updates, where the current state is the answer (inferred).
  - The 10 s threshold: rejected for ACT.3's 1 s budget.
- **Realizes**: ALLOCATION.GUARD.6 (idempotency keys in the HTTP contract); ALLOCATION.ACT.3 (deferred operations in the HTTP contract).
- **State**: `known | tension: Stripe v1's replay of failures (L269, L546) narrowed by GUARD.6 | unvalidated: the single-call wait and the expired-lock hand-off to the completer, and the retention minimum (inferred) | gap: the idempotency-key header is an expired IETF draft (T2)`.

## PIG-WEB.LOGIC.EXPOSE.4 Response Caching

- **Positions**:
  - P1 label every response cacheable or not on purpose with an explicit `Cache-Control`; send `Vary` for every request header the representation depends on, never `User-Agent` (L414).
  - P2 fingerprinted static assets `public, max-age=31536000, immutable`; HTML and unversioned resources `no-cache` with `ETag` or `Last-Modified`; `no-store` only when nothing may be stored (L415).
  - P3 personalised responses `private` (`no-store` when sensitive); a shared cache never reuses a response to a request carrying `Authorization` unless allowed (L416).
  - P4 page and view caches must vary on authentication, session and cookie state; the framework does not do it automatically (L418).
  - P5 every cache has an explicit expiry or invalidation plan and versioned keys (L419; inferred).
  - Placement: CACHE_STORE (derived-data caches in database tables; response and fragment caches shared by processes in Postgres, `UNLOGGED` when rebuildable; never per-process memory beyond one request; a cache service at a measured need).
- **Forces**: latency and load; correctness and privacy (stale or leaked responses).
- **Decision**:
  1. **Every response labelled** by a middleware default, overridden per view on purpose (P1): HTML `no-cache` with validators (P2); personalised HTML and JSON `private, no-cache`; sensitive pages and responses that set or contain a session identifier `no-store` (P3, L327; same wording as SECURE.2, review m10); 429 responses `no-store` (L366); fingerprinted assets `public, max-age=31536000, immutable` (P2). `Vary` names every header the representation depends on, `Cookie` included for personalised responses (P1, P3).
  2. **Application caches**: view and fragment caches in Postgres tables as CACHE_STORE sets, `UNLOGGED` when rebuildable (L420); keys versioned and including the user or session for personalised content (P4, P5); each with an explicit expiry or invalidation plan (P5). Derived-data caches are database tables invalidated in the source transaction (DERIVE.3, L534), outside this node. Never a per-process memory cache beyond one request.
  3. A shared cache service (Redis, Memcached) when measured cache latency or load on the primary demands it (CACHE_STORE).
- **Rejected**: heuristic caching by omission: never (P1). Personalised responses in shared caches: never (P3). `Vary: User-Agent`: never (P1).
- **Realizes**: PIG-WEB.ALLOCATION.CACHE_STORE (uses the cache store the placement names).
- **State**: `known | unvalidated: response caches in Postgres (CACHE_STORE, inferred)`.

## PIG-WEB.LOGIC.EXPOSE.5 Origin and CORS

- **Positions**:
  - P1 serve pages, their API and static paths from one public origin by default (one hostname, path routing at the proxy, one certificate, one HSTS scope); add CORS only for consumers that are truly cross-origin; a separate host for non-credentialed static assets or a CDN is common and harmless (L279; a synthesis, no source states the default).
  - P2 when a second origin must read responses: an explicit allowlist of origins, never `*` with credentials, `Vary: Origin` when the allowed origin is computed, preflights cached with `Access-Control-Max-Age` (L280).
- **Forces**: security (cookie scope, cross-origin reads); simplicity of operation.
- **Decision**: one origin for pages, the JSON interface and the agent surface (P1); static assets may come from a CDN host without credentials (P1); user files from the storage host (PROCESS.6). CORS is off by default. When a browser-based consumer on another origin must read responses: an explicit allowlist, never `*` with credentials, `Vary: Origin` when computed, `Access-Control-Max-Age` (P2). Credentialed cross-origin access (cookies) only for origins the same team operates; third parties use bearer tokens (SECURE.4) (inferred).
- **Rejected**: a separate API origin for the first-party interface: never by default (P1). `*` with credentials: never (P2).
- **Realizes**: no skeleton link; follows ALLOCATION.GUARD.4 (cookie scope) and SECURE.3.
- **State**: `known | unvalidated: the single-origin default is a synthesis (L279); credentialed CORS limited to the team's own origins (inferred)`.

## PIG-WEB.LOGIC.EXPOSE.6 Payload Schemas

- **Positions**:
  - P1 declare "may be null" and "may be absent" separately; a Pydantic `Optional` field allows null (L550).
  - P2 one schema dialect across tiers: OpenAPI 3.1 adopts JSON Schema 2020-12, Pydantic emits schemas compliant with both; type arrays instead of the old `nullable` (L551).
  - P3 publish request and response schemas separately where they differ (Pydantic's validation and serialization modes) (L552).
  - P4 separate input and output models, so the response model limits what leaves the server (L553).
  - P5 a response that fails its response model is a server defect: a server error, never a malformed body (L554).
  - P6 TypeScript types generated from OpenAPI are runtime-free; runtime validation of server responses in the browser is a separate decision (L555).
  - P7 consumers generated from the full producer schema are brittle; readers take only what they use (L556).
  - P8 object schemas open for readers, closed for writers: `additionalProperties: false` on request bodies you control, not on responses; `unevaluatedProperties` for composed schemas (L557; the rule inferred).
  - P9 decide coercion per boundary: Pydantic coerces by default, strict mode errors instead and is looser for JSON than for Python input; strict for a JSON API, coercion for forms and query strings (L558).
  - Placements: TYPE_CHAIN (stored facts from the schema; the interface origin recorded per project; OpenAPI and Pydantic models in sync by CI, MD-02); GUARD.1 (parse at every entry into precise types).
- **Forces**: correctness of the contract; security (closed inputs, filtered outputs); changeability (tolerant readers).
- **Decision**:
  1. **Pydantic models at every entry**, forms and query strings included (GUARD.1, TYPE_CHAIN): strict mode for JSON bodies, lax coercion for form and query strings (P9). Request models forbid unknown fields (`additionalProperties: false`, `unevaluatedProperties: false` when composed); response schemas stay open to readers (P8).
  2. Separate input and output models (P4); request and response schemas published separately where they differ (P3); null and absent declared separately (P1).
  3. OpenAPI 3.1 with JSON Schema 2020-12 and type arrays (P2), kept in sync with the models by MD-02's process (TYPE_CHAIN; the gate in EXPOSE.7); fields that echo stored facts are generated from the catalogue or checked against it (TYPE_CHAIN). How the description is produced under Django is ENFORCE.5's gap (candidate to verify: Django Ninja; review m7). The same always-in-sync rule covers the agent tool surface's schemas (for example an MCP server's tool list) and the function API catalogue (X7).
     - Closed request models and deploy skew (review m4): because requests are closed to unknown fields, a client sends a new request field only once every server instance accepts it (EXPOSE.7 step 4).
  4. A response that fails its model is a 500 and a defect, never sent malformed (P5).
  5. TypeScript types for islands are generated at build time only (TYPE_CHAIN, P6). Whether islands validate responses at runtime is the browser tier's decision (PIG-WEB.INTERACTION), not this node's; the server's share is P5 plus additive evolution (EXPOSE.7).
  6. Generated clients, agents' included, read only what they use (P7).
- **Rejected**: one model for input and output: acceptable when the shapes are equal, as in simple CRUD (L549 via TYPE_CHAIN). Closed response schemas: never (P8). Coercion everywhere, or strict everywhere: rejected (P9).
- **Realizes**: PIG-WEB.ALLOCATION.TYPE_CHAIN (publishes payload schemas where the type chain assigns); ALLOCATION.GUARD.1 (parses payloads at the boundary).
- **State**: `known | unvalidated: the reader and writer rule (L557, inferred); L552 to L558 rest on single sources`.

## PIG-WEB.LOGIC.EXPOSE.7 API Evolution

- **Positions**:
  - P1 check in CI that the implementation conforms to its OpenAPI description; design inside what OpenAPI can express (L273).
  - P2 write down what counts as breaking: removing or renaming, a new required request field, a changed type, default, format or meaning (L274).
  - P3 announce removal with `Deprecation` and `Sunset` headers, a documentation link, the flag in the OpenAPI file, and two versions coexisting during the transition (L275).
  - P4 when a break is unavoidable, the version identifier sits in one agreed place; contested: a major version in the URL path (Google), a required dated `api-version` query parameter (Azure), media-type versioning (Zalando), a dated request header with account pinning (Stripe, GitHub), no version and continuous additive evolution (GraphQL) (L276).
  - P5 an explicit skew policy: compatible changes within a window, clients tolerant of unknown fields, and either versioned paths or routing each client to the server version that served its code; contested, the routing option seen only in search snippets (L277).
  - P6 a first-party browser client that ships with the server still sees skew, so changes stay additive across that window (L278; inferred).
  - P7 a breaking-change diff of the description in CI (oasdiff); it covers the description only, behaviour needs contract tests (L547).
  - Cited: MD-02 (always in sync, a CI gate on drift); L517 (the function API evolves additively without version numbers; its departure is counted once at J6's function-API node, X2: "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise a breaking change goes expand, migrate, contract).
- **Forces**: changeability without breaking clients; correctness of the contract.
- **Decision**:
  1. **MD-02's gate**: CI fails on drift between description and implementation (P1) and on a breaking diff not released as a new version (P7); contract tests cover behaviour (P7); the written list of breaking changes (P2) is the diff's policy. The gate and the compatibility window cover every interface description consumers read: the HTTP description, the database function API catalogue and the agent tool surface (X7).
  2. **Additive by default**: the JSON interface is served under `/v1` from the start, and its major version does not change while every change is compatible (review m5; L276's URL-path position, Google: MUST `v1`); no minor version (the discipline L517 sets for the function API, applied with X2's condition). HTML routes carry no version: their contract is the rendered page (EXPOSE.1).
  3. **An unavoidable break**: `/v2` beside `/v1`, both served through a published window, the old one announced with `Deprecation` and `Sunset`, a documentation link and the OpenAPI deprecated flag (P3; P4's URL-path position).
  4. **Skew** (P5, P6): one team owns both sides. Pages and islands opened before a deploy keep working because changes stay additive across a window at least as long as a page can live with a valid session, the absolute session timeout (SECURE.2), and clients tolerate unknown fields (inferred). Because request models are closed (EXPOSE.6), a new request field ships server first, then client: clients send it only once every server instance accepts it; otherwise a new island would get 422 from an old instance mid-deploy (review m4; L557, L278).
- **Rejected**:
  - Media-type versioning: invisible in URLs, logs and agent tool calls, and caches must vary on `Accept` (inferred); acceptable when joining an ecosystem that uses it.
  - A dated query parameter (Azure): acceptable when joining that ecosystem.
  - A dated header with account pinning (Stripe, GitHub): acceptable when many external integrators must keep working indefinitely and the team can maintain transformations between versions (L276; condition inferred).
  - Routing each client to its matching deployment: acceptable where the hosting offers it (P5; snippets only).
  - Unversioned JSON paths until the first break: rejected, because they would leave unversioned paths beside `/v2` (review m5); "no version" stays acceptable for HTML routes.
- **Realizes**: no skeleton link; follows ALLOCATION.RECORD.3 and PIG-WEB.ALLOCATION.TYPE_CHAIN under MD-02 (proposed link to TYPE_CHAIN).
- **State**: `known: MD-02 for the gate (X7: every interface description) | unvalidated: the URL-path major version, v1 from the start, chosen among contested positions; the skew window bound and server-first field rollout (inferred)`.
