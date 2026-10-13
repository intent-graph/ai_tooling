# J7 PIG-WEB.LOGIC (pig-web-defaults): result

The judge's verdicts on the 31 nodes of the `pig-web-defaults` LOGIC branch, the Python backend of the JavaScript + Python + Postgres stack. They apply the max rule of `../../target_hierarchy.md` and build on the settled allocation (`../J1_allocation/allocation_matrix.md`), the maintainer decisions MD-01 to MD-03 (`../../maintainer_decisions.md`) and the philosophy verdicts these nodes refine (`../J3_phil_logic/records.md`). The adversarial review of the branch (`../review_logic/review.md`) and the cross-branch resolutions (`../cross_branch_fixes.md`) are applied. Each level below reads alone. The grounds for each node are in `records.md` and the questions in `questions.md`.

## L1 headline

The Python backend is a Django application with synchronous handlers, one deployable per backend. It is the gate every caller passes:
- one central, deny-by-default, object-level policy module, which also authorizes any override of a blockable rule;
- sessions held in Postgres behind a `__Host-` cookie, whose `SameSite` value is raised to the maintainer (recorded default: Lax plus a cross-site navigation check, Strict for operator consoles);
- every CSRF layer, and no credential ever in a URL;
- login delegated to an OpenID Connect server, the required authentication context checked on every login;
- limits at the proxy and per identity.

Its use cases call the Postgres function API, one generated wrapper call per transaction with the verified actor set. Reads that need the actor run in a short read-only transaction through the same wrapper; plain reads take one autocommit statement, paged in the database. Deferred work, side effects and foreign mutations are rows that database functions write. Python workers claim them through writer functions and deliver to idempotent consumers; a foreign mutation answers 202. Files go directly to object storage and are type-checked from their bytes and scanned before anyone can read them. Programs and agents get resource-oriented JSON under `/v1` with:
- problem details mapped from function error codes;
- idempotency keys recorded with the effect: wait and replay for single calls, 409 for a multi-phase operation in flight;
- 202 status resources;
- every interface description kept in sync;
- additive evolution.

30 of the 31 nodes are judged: 29 decided, 1 raised as the one question (SameSite); the remaining node is deferred. There is no conflict with the allocation and no verdict against the doctrine. One tension inside J1's own records (ACT.2 against ACT.3) is carried to J1's owner. One inherited clause stays with the maintainer: who filters per-user reads, now recorded with J1's fallback and the points it would change. Review: 17 findings applied, 0 rejected.

Pinned:
- Nodes judged: 30 of 31 in the PIG-WEB.LOGIC branch; 1 deferred and not judged (PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery); 5 are roll-ups owning no row (PIG-WEB.LOGIC, .SECURE, .ENFORCE, .PROCESS, .EXPOSE); 133 of 133 owned rows used.
- Decided 29, undecided 1: PIG-WEB.LOGIC.SECURE.2's `SameSite` attribute on the session cookie, a genuine trade-off between the session's function (carrying a login across arrivals from other sites) and protection against attacker-triggered navigations; raised as the one question, recorded default `Lax` plus a cross-site navigation check, `Strict` for operator consoles.
- One clause inherited from J1, held in PIG-WEB.LOGIC.SECURE.1: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends; under it ENFORCE.3, SECURE.1 and PROCESS.6 read through the function and the table loses direct SELECT. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 1 (SameSite on the session cookie); five other candidate trade-offs considered and not raised, each with its reason.
- Verdicts against the maintainer doctrine: 0. The one MAINT row owned here (L605, scheduled jobs) is adopted as the max choice; the doctrine rows J1 placed (L516, L527, L534, L584, L596, L604) are applied as placed; L530 (function error codes, override flag), L566 (actor from a transaction-local setting) and L587 (idempotent mutations) are applied; L517 is applied with its departure counted once at J6 (X2).
- Conflicts with J1 placements: 0. One tension inside J1 carried and routed to J1's owner: ACT.2 runs a foreign mutation the user waits for as atomic phases in the request, while ACT.3 forbids foreign effects inside the request; resolved here in favour of both by running the phases in a worker behind a 202 status resource, in-request only under a stated condition. Source positions narrowed to fit settled placements, recorded as tensions: request-wide and use-case-wide transactions (L229) and ORM-first writes (L235, L227 Active Record) yield to one database function call per transaction (ACT.1, DB_API); views and separate read stores (L237) yield to L516 and DERIVE.1; post-commit hooks (L233) carry only losable work (L600, ACT.2); limiter state in a cache service (L365) yields to Postgres until a measured limit (POSTGRES_FIRST, CACHE_STORE); replay of stored failures (Stripe v1 in L269, L546) yields to key and effect committed together (GUARD.6).
- Evidence gaps: (1) framework (L242): no source gives neutral criteria; Django is chosen on criteria the settled verdicts set (framework sessions and CSRF, L323, L330; server-rendered HTML; synchronous default), inferred; how Pydantic models and the OpenAPI description are produced under Django was not read (Django Ninja is the candidate to verify: OpenAPI 3.1 output, Pydantic v2); (2) upload path (L421): no source weighs direct-to-storage against through-the-app; direct chosen, inferred; (3) version location (L276): five contested positions; URL-path major version, `/v1` from the start, inferred; (4) login delegation (L338): no source ranks it; delegation to an OpenID Connect server (a provider or self-run) chosen, inferred; the `acr`/`amr` check rests on OpenID Connect Core, not on a ledger row; (5) no Python job runner over a queue table written by database functions was read (JOB_HOST pattern set, library open); (6) rate-limiter counters in Postgres follow POSTGRES_FIRST by analogy, no source; (7) Postgres behaviour not in the ledger: transaction-local settings vanish in autocommit, deadlocks and serialization failures outside Serializable (inferred).
- Review fixes (`../review_logic/review.md`): 17 findings for this unit (M1 to M7, m1 to m8, m10 to m12; m9 is J3's), 17 applied, 0 rejected; cross-branch resolutions X1 to X7 applied where these nodes touch them (`../cross_branch_fixes.md`).

## L2 claims

### Review fixes

Major:
- **M1** (SECURE.1, ENFORCE.3, PROCESS.6; with X1): J1's fallback kept (read functions receiving the verified actor, acceptable when a per-user read rule must hold for two or more backends). Each node now says what changes under it: the read goes through the function, the table loses direct SELECT. J1's owner is asked to reword the fallback's condition.
- **M2** (ENFORCE.2, ENFORCE.3): a read needing the actor runs in a short read-only transaction through the generated wrapper, because a transaction-local setting does not survive autocommit; read functions refuse a missing actor.
- **M3** (EXPOSE.3, PROCESS.2): concurrent duplicates split by operation shape. A single-call operation waits, then gets the replay. A multi-phase operation keeps a recovery point and a lock with an expiry on the key row: the duplicate gets 409 with `Retry-After`, and the completer resumes an expired lock.
- **M4** (PROCESS.2, PROCESS.3, EXPOSE.3; pinned conflicts line): foreign mutations run as atomic phases in a worker behind 202. In-request phases are acceptable only when the user must see the outcome and the call fits 1 s. The ACT.2/ACT.3 tension is routed to J1's owner.
- **M5** (SECURE.2, SECURE.3, SECURE roll-up, `questions.md`): SameSite is raised as a question, because the session's function is a force the node serves (distinct from login friction). Recorded default: Lax plus a cross-site navigation check, Strict for operator consoles. The claim that Strict protects only safe requests is withdrawn.
- **M6** (SECURE.4, SECURE.5): the backend requests and checks `acr` or `amr`, with step-up through `max_age` for sensitive operations. The provider bar includes emitting these claims.
- **M7** (EXPOSE.2, SECURE.1, ENFORCE.1; pinned doctrine line): function error codes are mapped to problem types on L530's ground. Blockable-rule errors get a distinct type. The override flag is authorized by the policy module, set by the use case and audited, never taken from client input.

Minor:
- **m1** (ENFORCE.2): retries on 40001 and 40P01 always, at any isolation level.
- **m2** (PROCESS.5): the file signature is checked against an allowlist before availability; the stored type comes from it.
- **m3** (SECURE.6): no challenge for agents; challenges only on human-only flows.
- **m4** (EXPOSE.7, EXPOSE.6): a new request field ships server first, then client.
- **m5** (EXPOSE.7): JSON under `/v1` from the start; HTML routes unversioned.
- **m6** (PROCESS.1): claim, outcome and expiry go through the job table's writer functions.
- **m7** (ENFORCE.3, ENFORCE.5, EXPOSE.6): one read layer, the Django ORM plus the wrappers, with SQLAlchemy Core dropped; Django Ninja recorded as the candidate to verify.
- **m8** (SECURE.1, ENFORCE.3): collection reads use a query predicate from the policy module.
- **m10** (SECURE.2, EXPOSE.4): `no-store` for "responses that set or contain a session identifier".
- **m11** (SECURE.4): delegation includes a self-run OpenID Connect server; own-store fallback narrowed.
- **m12** (EXPOSE.3): natural idempotence cited from L587 (MAINT).

Cross-branch:
- **X1** (LOGIC, SECURE, SECURE.1, ENFORCE.3, PROCESS.6): the read-visibility clause notation, recorded default, fallback and consequence for directly-reading roles.
- **X2** (EXPOSE.7, pinned doctrine line): L517 cited, its departure counted at J6 with the deployed-together condition word for word.
- **X3** (ENFORCE.1, ENFORCE.2): no backend composition; cross-domain composition through published functions inside the database.
- **X4** (SECURE.1, ENFORCE.2): never-committing tests on shared data, a disposable database for commit-only behaviour, concurrency tests in the default suite.
- **X5** (LOGIC, ENFORCE): each backend one deployable.
- **X6** (SECURE, SECURE.2, SECURE.4, PROCESS.4, PROCESS.6, EXPOSE.1): no credential in a URL; the upload policy and download URLs are the stated exceptions, with scope and lifetime.
- **X7** (EXPOSE, EXPOSE.6, EXPOSE.7): the sync rule and compatibility window cover the HTTP description, the function catalogue and the agent tool surface.

### Verdicts

The verdict on each node, in the default context of MD-03: the database is shared by several backends and by other consumers; operations, transitions and per-user write rules that can be decided from the row are database functions; no row-level security by default.

- **PIG-WEB.LOGIC** (roll-up): Django, synchronous, one deployable per backend. The backend secures entry, holds sessions, policy, workflow and external calls, and calls the function API once per operation. It decides no rule the database owns. `known (roll-up)`; read visibility awaiting maintainer; SameSite raised; framework unvalidated.
- **SECURE** (roll-up): one gate, deciding nothing on the caller's word; no credential in a URL.
  - **SECURE.1 Access control**:
    - one policy module, deny by default, with object-level checks combining product roles and attribute and relationship rules; collections filtered by a query predicate;
    - all backend checks kept (MD-01); its checks of the writer functions' rules are tested copies;
    - overrides of blockable rules authorized per actor and audited;
    - denials tested through the deployed role (never-committing on shared data) and logged to the security event log;
    - per-user reads: each backend filters from one shared specification with a shared denial-test suite; read functions acceptable when a rule must hold for two or more backends; directly-reading roles see every row unless restricted (awaiting maintainer).
  - **SECURE.2 Sessions**: Django database sessions in Postgres. The cookie is `__Host-`, `Secure`, `HttpOnly`, with an explicit `SameSite`, its value `undecided` and raised (recorded: Lax plus a navigation check, Strict for consoles). The id rotates on every privilege change; idle and absolute timeouts are enforced on the server; logout deletes the record. Responses that set or contain the id are `no-store`. Never signed-cookie or JWT sessions; never an id in a URL.
  - **SECURE.3 CSRF**: the framework token, the cookie's `SameSite`, and Fetch Metadata or `Origin` checks, the checks first in logging-only mode, plus a header token for scripts. Only bearer-token endpoints are exempt.
  - **SECURE.4 Federated login**:
    - delegated to an OpenID Connect server (a provider or self-run) through a backend-for-frontend, with code flow and PKCE, exact redirects and a validated ID token;
    - the authentication context (`acr` or `amr`) requested and checked, with step-up for sensitive operations;
    - identities keyed by issuer plus subject;
    - agent tokens audience-bound, short-lived and revocable, sender-constrained where supported; JWTs verified strictly;
    - an own password store acceptable only when no OpenID Connect server can be used or run.
  - **SECURE.5 Passwords**: NIST policy; Argon2id; MFA required, passkeys offered; generic errors, per-account growing delays, no lockout, real limits outside the framework. The same bar applies to the chosen server, which must emit authentication-context claims.
  - **SECURE.6 Rate limits**: identity-blind limits at the proxy; identity-aware, cost-weighted and concurrency limits in the backend. Counters live in Postgres until a measured load. Over-limit answers are 429 with `Retry-After`, never cached, with IETF RateLimit fields for agents. New limits roll out observe-first; challenges only on human-only flows, never for agents.
  - **SECURE.7 Server-side fetch**: one helper that blocks private, loopback and link-local addresses at connect time, checks every redirect and leaves through an egress proxy (made required).
- **ENFORCE** (roll-up): one Django deployable per backend, a use-case layer, one call per transaction, reads reduced in Postgres, synchronous handlers.
  - **ENFORCE.1 Use cases**:
    - every entry point (HTML, JSON, agent, commands, jobs) calls one use-case layer, behind thin handlers; use cases hold only the backend's share;
    - several calls never composed into one operation; cross-domain composition inside the database;
    - the use case decides an authorized override;
    - the domain is decoupled from the ORM: ORM models are read mappers, never saved on shared tables; Active Record acceptable only for a single consumer with low SQL skill.
  - **ENFORCE.2 Transactions**:
    - one transaction holds the actor setting and exactly one API function call, explicit commit, rollback on any error; `ATOMIC_REQUESTS` off;
    - plain reads in autocommit; reads needing the actor in a short read-only transaction through the wrapper; the write carries the version it read;
    - 40001 and 40P01 retried at any isolation; an unknown commit retried only with a key;
    - commit-only behaviour and concurrency tested in a disposable database.
  - **ENFORCE.3 Data access**: writes go only through the generated wrappers. Reads go through one layer: Django ORM read mappers plus read functions through the wrappers. Each read is one statement or read function, joined, with keyset paging, never queries in loops; bound parameters always. Per-user read rules and collection predicates sit inside the statement, or in the read function under J1's fallback. No views as contract.
  - **ENFORCE.4 Concurrency**: synchronous by default; asynchronous code only in the long-lived-connection process type, under its hard constraints.
  - **ENFORCE.5 Framework**: Django, on criteria taken from settled verdicts: framework sessions and CSRF, HTML, synchronous handlers. FastAPI wins for a backend serving only bearer-token programs and agents. No neutral source; OpenAPI production under Django to verify (candidate Django Ninja).
- **PROCESS** (roll-up): durable effects as rows, delivered at least once to idempotent consumers; foreign mutations in workers behind 202; files type-checked and scanned before anyone reads them.
  - **PROCESS.1 Jobs**: job rows written by database functions; claim (`SKIP LOCKED` inside the function), outcome and expiry go through the job table's writer functions. Arguments are ids; jobs never wait on one another. L605's job rules and monitoring are adopted (MAINT, max). The runner library is open.
  - **PROCESS.2 Side effects**: an outbox written by the function; receivers idempotent through processed ids. Foreign mutations run as atomic phases in a worker, the key row carrying recovery points and a lock with an expiry, behind a 202; in-request only when the user must see the outcome within 1 s. Post-commit hooks only for losable work; no saga inside one Postgres.
  - **PROCESS.3 Resilience**: a timeout on every call; retries only when idempotent or keyed, with backoff and jitter, at one layer. In requests: three attempts and a 10% budget, foreign mutations excluded by default; in jobs: the runner. Circuit breakers on the request path.
  - **PROCESS.4 Upload path**: direct to object storage under a POST policy (one random key, size range, exact type, short expiry; scope and lifetime stated), behind the gates; multipart for large files. Through the application only when a small file must be read within the request.
  - **PROCESS.5 Scanning and storage**: one row per upload, with a state column that has one writer function. A signature check sets the stored type, then scanning and reconstruction run, all before availability; nothing is readable before clean, the uploader included. Stale uploads are swept; `bytea` only for small atomic files.
  - **PROCESS.6 Serving**: authorization and state checked (through a read function under J1's fallback), then a redirect to a short-lived, one-object signed URL on the storage origin. Responses carry the stored type, `nosniff`, and `attachment` unless the file is meant inline.
- **EXPOSE** (roll-up): HTML for browsers, described resource-oriented JSON under `/v1` for programs and agents.
  - **EXPOSE.1 Style and resources**: resources with standard methods; state transitions as custom methods mapped to their writer function. Every collection is paged by keyset behind an opaque token that carries no authorization, with a maximum page size. GraphQL is acceptable for many clients needing different field subsets.
  - **EXPOSE.2 Errors**: RFC 9457 problem details with stable types and corrective details. Named constraints and function error codes (L530) map to types (412, 428, 409, 422, 400); a blockable-rule error has its own type naming the override.
  - **EXPOSE.3 Retries and long operations**: natural idempotence first (L587), else an `Idempotency-Key` recorded in the effect's transaction. Only committed outcomes are replayed. A concurrent duplicate of a single-call operation waits, then gets the replay; for a multi-phase operation it gets 409 with `Retry-After` until completion. Keys are kept at least 24 h. Long operations and foreign mutations answer 202 with a full status resource, the job written before the 202.
  - **EXPOSE.4 Caching**: every response labelled, `Vary` complete, personalised responses `private, no-cache`, responses that set or contain a session id `no-store`. Application caches live in Postgres, keyed per user where personalised.
  - **EXPOSE.5 Origin**: one origin; CORS off by default; an explicit allowlist when needed; credentialed CORS only for the team's own origins.
  - **EXPOSE.6 Payloads**: Pydantic at every entry, strict for JSON and lax for forms and query strings. Requests are closed to unknown fields and responses open; input and output models are separate. OpenAPI 3.1, the function catalogue and the agent tool schemas are in sync; a response that fails its model is a 500.
  - **EXPOSE.7 Evolution**: MD-02's CI gate (conformance, a breaking diff, contract tests) over every interface description. JSON lives under `/v1` from the start and changes are additive; `/v2` with Deprecation and Sunset comes only for an unavoidable break. New request fields ship server first. The skew window is at least the absolute session timeout.
- **PROCESS.7 Email and Push Delivery**: deferred, not judged.

Pinned:
- Nodes judged: 30 of 31 in the PIG-WEB.LOGIC branch; 1 deferred and not judged (PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery); 5 are roll-ups owning no row (PIG-WEB.LOGIC, .SECURE, .ENFORCE, .PROCESS, .EXPOSE); 133 of 133 owned rows used.
- Decided 29, undecided 1: PIG-WEB.LOGIC.SECURE.2's `SameSite` attribute on the session cookie, a genuine trade-off between the session's function (carrying a login across arrivals from other sites) and protection against attacker-triggered navigations; raised as the one question, recorded default `Lax` plus a cross-site navigation check, `Strict` for operator consoles.
- One clause inherited from J1, held in PIG-WEB.LOGIC.SECURE.1: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends; under it ENFORCE.3, SECURE.1 and PROCESS.6 read through the function and the table loses direct SELECT. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 1 (SameSite on the session cookie); five other candidate trade-offs considered and not raised, each with its reason.
- Verdicts against the maintainer doctrine: 0. The one MAINT row owned here (L605, scheduled jobs) is adopted as the max choice; the doctrine rows J1 placed (L516, L527, L534, L584, L596, L604) are applied as placed; L530 (function error codes, override flag), L566 (actor from a transaction-local setting) and L587 (idempotent mutations) are applied; L517 is applied with its departure counted once at J6 (X2).
- Conflicts with J1 placements: 0. One tension inside J1 carried and routed to J1's owner: ACT.2 runs a foreign mutation the user waits for as atomic phases in the request, while ACT.3 forbids foreign effects inside the request; resolved here in favour of both by running the phases in a worker behind a 202 status resource, in-request only under a stated condition. Source positions narrowed to fit settled placements, recorded as tensions: request-wide and use-case-wide transactions (L229) and ORM-first writes (L235, L227 Active Record) yield to one database function call per transaction (ACT.1, DB_API); views and separate read stores (L237) yield to L516 and DERIVE.1; post-commit hooks (L233) carry only losable work (L600, ACT.2); limiter state in a cache service (L365) yields to Postgres until a measured limit (POSTGRES_FIRST, CACHE_STORE); replay of stored failures (Stripe v1 in L269, L546) yields to key and effect committed together (GUARD.6).
- Evidence gaps: (1) framework (L242): no source gives neutral criteria; Django is chosen on criteria the settled verdicts set (framework sessions and CSRF, L323, L330; server-rendered HTML; synchronous default), inferred; how Pydantic models and the OpenAPI description are produced under Django was not read (Django Ninja is the candidate to verify: OpenAPI 3.1 output, Pydantic v2); (2) upload path (L421): no source weighs direct-to-storage against through-the-app; direct chosen, inferred; (3) version location (L276): five contested positions; URL-path major version, `/v1` from the start, inferred; (4) login delegation (L338): no source ranks it; delegation to an OpenID Connect server (a provider or self-run) chosen, inferred; the `acr`/`amr` check rests on OpenID Connect Core, not on a ledger row; (5) no Python job runner over a queue table written by database functions was read (JOB_HOST pattern set, library open); (6) rate-limiter counters in Postgres follow POSTGRES_FIRST by analogy, no source; (7) Postgres behaviour not in the ledger: transaction-local settings vanish in autocommit, deadlocks and serialization failures outside Serializable (inferred).
- Review fixes (`../review_logic/review.md`): 17 findings for this unit (M1 to M7, m1 to m8, m10 to m12; m9 is J3's), 17 applied, 0 rejected; cross-branch resolutions X1 to X7 applied where these nodes touch them (`../cross_branch_fixes.md`).

## L3 full

### Review fixes

The cross-branch resolutions X1 to X7 were applied first, verbatim where these nodes touch them; then the branch review's findings. Each finding's evidence was re-checked before applying it: the ledger rows (L023, L276, L311, L324, L327, L331, L338, L422, L434, L517, L530, L546, L557, L566, L587, L589, L596, L652), J1's Q1, ACT.2 and ACT.3 text, and Postgres and OpenID Connect behaviour the reviewer cited as inferred or fetched. None was found wrong; none is rejected.

| id | node(s) | evidence re-checked | change in `records.md` |
|---|---|---|---|
| M1 | SECURE.1, ENFORCE.3, PROCESS.6 | J1 Q1 "If unanswered … B as 'acceptable when …'": confirmed | Fallback kept in J1's and X1's words; a "under J1's read-function answer" line in each of the three nodes (read through the function, table loses direct SELECT); note for J1's owner to reword the condition. |
| M2 | ENFORCE.2 step 3, ENFORCE.3 | L311 and L566 (transaction-local actor): confirmed; autocommit scoping is Postgres behaviour, marked inferred | Plain reads in autocommit; actor-needing reads in a short read-only transaction through the wrapper; read functions refuse a missing actor; autocommit rejected for such reads. |
| M3 | EXPOSE.3 step 3, PROCESS.2 step 3 | L589 (phases, recovery points), L546 (409 or serialized behind a locked key row): confirmed | Duplicate handling split: single-call waits then replays; multi-phase keeps recovery point and expiring lock on the key row, 409 with `Retry-After` while locked, replay after completion, expired lock resumed by the completer; rejection of 409 narrowed to single-call operations. |
| M4 | PROCESS.2 step 3, PROCESS.3, EXPOSE.3 step 5; pinned conflicts | J1 ACT.2 ("runs as atomic phases") and ACT.3 ("Forbidden: … foreign effects inside the request"): confirmed contradictory | Phases run in a worker; the request writes the intent with its key and answers 202; in-request acceptable when the user must see the outcome and it fits 1 s; tension recorded and routed to J1's owner. |
| M5 | SECURE.2, SECURE.3, SECURE roll-up; `questions.md` | L324 (both admitted), L331 (Lax allows top-level GET); the cookie draft's "speedbump" as cited by the reviewer; J3's MFA reasoning | The session's function named as a force SECURE.2 serves, kept distinct from login friction; `SameSite` set `undecided` and raised as the one question; recorded default Lax plus a Fetch Metadata navigation check, Strict for consoles; the "Strict only protects safe requests" claim withdrawn. |
| M6 | SECURE.4 (new step 3), SECURE.5 | OpenID Connect Core 1.0 as cited by the reviewer (`acr`, `amr`, `acr_values`, "SHOULD check"); not in the ledger, marked inferred | Required context requested and checked on every login; step-up with `max_age` and `auth_time` for sensitive operations; provider bar includes emitting the claims; skipping the check rejected. |
| M7 | EXPOSE.2, SECURE.1, ENFORCE.1; pinned doctrine | L530 (MAINT): confirmed | Mapping grounded on L530; blockable-rule errors get a distinct type naming the override; override authorized by the policy module, set by the use case, audited, never from client input. |
| m1 | ENFORCE.2 step 6 | Postgres error behaviour (inferred) | Always retry 40001 and 40P01 for the whole one-call transaction within PROCESS.3's caps; dependency on Serializable removed. |
| m2 | PROCESS.5 (new step 3) | L023, L423: confirmed | Signature verified against an allowlist before availability; stored type set from it; mismatch moves the row to failed. |
| m3 | SECURE.6 step 5 | L652, L034: confirmed | Challenges only on human-only flows; agents get 429 with RateLimit fields. |
| m4 | EXPOSE.7 step 4, EXPOSE.6 | L557, L278: confirmed | New request fields ship server first, then client. |
| m5 | EXPOSE.7 steps 2-3 | L276 (Google: MUST `v1`): confirmed | JSON under `/v1` from the start; `/v2` beside it for a break; HTML routes unversioned. |
| m6 | PROCESS.1 step 2 | L596 (MAINT): confirmed | Claim (with `SKIP LOCKED` inside the function), outcome and expiry through the job table's writer functions. |
| m7 | ENFORCE.3, ENFORCE.5, EXPOSE.6 | Django Ninja front page as cited by the reviewer (version not stated) | One read layer named (Django ORM read mappers plus wrappers; raw SQL through Django's connection); SQLAlchemy Core rejected under Django; Django Ninja recorded as the candidate to verify. |
| m8 | SECURE.1 step 1, ENFORCE.3 step 4 | DERIVE.2: confirmed | Collection reads use a query predicate from the policy module; per-object checks for single objects only. |
| m10 | SECURE.2, EXPOSE.4 | L327: confirmed | Both read "responses that set or contain a session identifier". |
| m11 | SECURE.4 step 1, rejected list | L338: confirmed | Delegation includes a self-run OpenID Connect server; own-store fallback narrowed to "no OpenID Connect server can be used or run". |
| m12 | EXPOSE.3 step 1 | L587 (MAINT): confirmed | Natural idempotence cited from L587 as the doctrine's max. |
| X1 | LOGIC, SECURE, SECURE.1, ENFORCE.3, PROCESS.6 | `../cross_branch_fixes.md` | Clause notation, recorded default, kept fallback, consequence for roles that may SELECT the base tables. |
| X2 | EXPOSE.7 (cited rows), pinned doctrine | `../cross_branch_fixes.md` | L517 cited with its condition word for word; counted at J6, not here. |
| X3 | ENFORCE.1 step 2, ENFORCE.2 step 2 | `../cross_branch_fixes.md` | No backend composition of calls; cross-domain composition through published functions inside the database. |
| X4 | SECURE.1 step 5, ENFORCE.2 step 8 | `../cross_branch_fixes.md` | Test boundary: never-committing on shared data, committing sessions in a disposable database, concurrency tests in the default suite. |
| X5 | LOGIC, ENFORCE | `../cross_branch_fixes.md` | "One Django backend per deployable" replaced: each backend one deployable, not split without a measured need. |
| X6 | SECURE, SECURE.2, SECURE.4, PROCESS.4, PROCESS.6, EXPOSE.1 | `../cross_branch_fixes.md` | No session, bearer or long-lived credential in a URL; the upload policy and the download URL stated as the exceptions with scope and lifetime (minutes, recorded per project; no source gives a number); the authorization code and page tokens noted as not credentials. |
| X7 | EXPOSE, EXPOSE.6, EXPOSE.7 | `../cross_branch_fixes.md` | Sync rule and compatibility window extended to the function API catalogue and the agent tool surface. |

### Inputs read

- `../../target_hierarchy.md` (whole), `../../maintainer_decisions.md` (MD-01 to MD-03), `../../02_skeleton/judge_plan.md` (J7 section).
- `../J1_allocation/allocation_matrix.md` (whole) and `../J1_allocation/records.md` (whole, including the default context and access paths; the 16 verdicts listed for J7 read first), `../J1_allocation/questions.md` (Q1).
- `../J3_phil_logic/records.md` (the philosophy verdicts these nodes refine) and its `questions.md`.
- `../../02_skeleton/skeleton.md`: partition rationale, the J7 tree and node table, every intentlink touching the branch.
- `../../02_skeleton/claims_ledger.md`: all 133 owned rows in full; cited rows owned elsewhere: L022, L051, L086, L125 to L127, L258, L260, L272, L310, L311, L313, L315, L316, L318, L319, L417, L420, L457, L478 to L482, L486, L516, L517, L527, L530, L545, L548, L549, L566, L582, L584, L587, L596, L601, L604, L634, L635, L640, L656, L658, L661.
- `../../02_skeleton/sources.md`: tiers of the sources behind contested rows.
- For the fixes: `../review_logic/review.md` and `result.md`, `../cross_branch_fixes.md`. The reviewer's fetched sources (the cookie draft, OpenID Connect Core 1.0, the Django Ninja front page) were taken as cited, not re-fetched; the lines resting on them are marked inferred.
- No research result (L3) was opened: no owned row was too compressed to judge.
- Outside the evidence, as a consistency check only: the sibling Python guideline's scenario page on frameworks (`../../../../../python_guidelines/LOD_2_phases/7.1_scenarios.md`).

### Method

Each node was judged on its owned rows, under the max rule for the LOGIC role (enforcement and security). The J1 placements and the J3 philosophy verdicts were taken as fixed, and the maintainer decisions were applied by id. Where a source position could only stand by contradicting a placement, it was narrowed and the narrowing recorded as a tension, not a conflict: the placement wins, and the source position stays as "acceptable when <the placement's moving condition>". Where two placements contradict each other (ACT.2 and ACT.3), the realization that satisfies both is chosen and the tension routed to J1's owner. Inferred steps are marked in each record's state.

### Verdicts at a glance

| node | verdict | realizes | state |
|---|---|---|---|
| PIG-WEB.LOGIC | Django backend, one deployable: entry gate, use cases calling the function API, workers for deferred effects, HTML plus described JSON | refines LOGIC | known (roll-up); awaiting maintainer (reads); SameSite undecided; framework unvalidated |
| SECURE | one gate for every caller; no credential in a URL | refines LOGIC.SECURE | known (roll-up); awaiting maintainer; SameSite undecided |
| SECURE.1 | central, deny by default, object-level with relationship and attribute rules; collection predicates; overrides authorized and audited; backend checks kept; denial tests through the real role; per-user reads at the recorded default with J1's fallback | ROW_SECURITY; follows GUARD.3 | known; undecided: awaiting maintainer (read visibility) |
| SECURE.2 | Django database sessions in Postgres; `__Host-`; rotation, timeouts, `no-store` on responses that set or contain the id; SameSite raised | GUARD.4 | known; undecided: SameSite (Lax plus navigation check recorded) |
| SECURE.3 | token, SameSite, Fetch Metadata, header token; bearer endpoints exempt | follows GUARD.4 | known |
| SECURE.4 | OIDC server (provider or self-run) through a backend-for-frontend; PKCE; `acr`/`amr` checked, step-up; issuer plus subject; audience-bound agent tokens | GUARD.4 | known; ranking and acr check unvalidated |
| SECURE.5 | NIST policy, Argon2id, MFA required, throttling without lockout; provider emits context claims | follows LOGIC.SECURE | known |
| SECURE.6 | two layers; costly operations tighter; counters in Postgres; 429 and RateLimit fields; no challenge for agents | follows POSTGRES_FIRST, CACHE_STORE | known; gap (draft headers) |
| SECURE.7 | guarded fetch helper with an egress proxy | follows RULES.3 | known |
| ENFORCE | one deployable per backend; use cases, one call per transaction, reads in Postgres | refines LOGIC.ENFORCE | known (roll-up) |
| ENFORCE.1 | one use-case layer for every entry point; no composed calls; the use case sets authorized overrides; domain decoupled from the ORM | ACT.1 | known; tension L226, L227 |
| ENFORCE.2 | actor plus one function call per transaction; actor-needing reads in a read-only transaction; 40001 and 40P01 retried; X4 tests | follows ACT.1, RULES.5, DB_API | known; tension L229; Postgres scoping inferred |
| ENFORCE.3 | writes through wrappers; one read layer; one-statement reads with keyset paging; bound parameters; flips under J1's fallback | DERIVE.2 | known; tension L235, L237; awaiting maintainer (read visibility) |
| ENFORCE.4 | synchronous; async only for long-lived connections | follows LOGIC.PROCESS | known |
| ENFORCE.5 | Django | serves GUARD.4, PRESENT.1, TYPE_CHAIN | known; unvalidated; gap (Django Ninja to verify) |
| PROCESS | rows for durable effects; foreign mutations in workers; files checked before access | refines LOGIC.PROCESS | known (roll-up) |
| PROCESS.1 | database-written queue, claim and outcome through writer functions, `SKIP LOCKED`, L605 rules | JOB_HOST | known; gap (runner) |
| PROCESS.2 | outbox, idempotent receivers, atomic phases in a worker behind 202 | ACT.2; follows ACT.3 | known; tension L233; tension ACT.2/ACT.3 (J1) |
| PROCESS.3 | timeouts, keyed or idempotent retries at one layer, breakers | follows ACT.2, GUARD.6 | known |
| PROCESS.4 | direct to storage under a POST policy, scope and lifetime stated | follows GUARD.1, GUARD.3 | known; unvalidated |
| PROCESS.5 | upload rows with a writer-function state; signature check, then scan, before availability | follows ACT.1 | known; unvalidated |
| PROCESS.6 | authorize, then redirect to a one-object signed URL; safe headers; flips under J1's fallback | follows GUARD.3 | known; awaiting maintainer (read visibility) |
| PROCESS.7 | deferred | - | not judged |
| EXPOSE | HTML plus described JSON under `/v1` | refines LOGIC.EXPOSE | known (roll-up) |
| EXPOSE.1 | resources, custom methods for transitions, keyset continuation paging | DERIVE.2 | known; unvalidated |
| EXPOSE.2 | problem details; constraints and L530 codes mapped to types; blockable-rule type | follows GUARD.5, GUARD.1 | known; blockable type inferred |
| EXPOSE.3 | natural idempotence (L587), else a key recorded with the effect; duplicates by operation shape; 202 status resources | GUARD.6, ACT.3 | known; tension (Stripe v1); gap (draft) |
| EXPOSE.4 | every response labelled; application caches in Postgres | CACHE_STORE | known |
| EXPOSE.5 | one origin; CORS allowlist only | follows GUARD.4 | known |
| EXPOSE.6 | Pydantic at entry, strict JSON, closed requests, every description in sync | TYPE_CHAIN, GUARD.1 | known |
| EXPOSE.7 | MD-02 gate over every description; `/v1` from the start; server-first fields; `/v2` for a break | follows RECORD.3, TYPE_CHAIN | known (MD-02); unvalidated |

### Tensions: source positions narrowed to fit settled placements (not conflicts)

1. **L229**: a request-wide or use-case-wide transaction becomes one transaction per API function call. Source: ACT.1, RULES.5, DB_API (J1's R1-4). Either form is acceptable for a single consumer.
2. **L235, L227**: ORM-first access and Active Record. Writes go only through the generated wrappers, and ORM models are read mappers (DB_API). Acceptable for a single consumer with low SQL skill.
3. **L226**: state transitions in the backend unless L527's gate is met. MD-03 meets the gate by default, so transitions are database functions.
4. **L237**: views and separate read stores. No view as a contract (L516); derived data stays in the database (DERIVE.1, RECORD.1).
5. **L233**: post-commit hooks as the carrier of side effects. Only for losable work (L600); everything else goes through the outbox (ACT.2).
6. **L365**: limiter state in a shared cache service. Postgres until a measured load (POSTGRES_FIRST, CACHE_STORE).
7. **L269, L546**: Stripe v1's replay of stored failures. The key commits with the effect (GUARD.6), so only committed outcomes replay.

A tension inside J1's own records, carried and routed to J1's owner (review M4): ACT.2 runs a foreign mutation the user waits for as atomic phases in the request; ACT.3 forbids foreign effects inside the request. PROCESS.2 runs the phases in a worker behind 202, which satisfies both; in-request phases stay acceptable when the user must see the foreign outcome in the same response within ACT.3's 1 s budget.

### Evidence gaps

1. **Framework** (L242): no source gives neutral criteria. Django is chosen on criteria the settled verdicts set: framework-provided sessions and CSRF (L323, L330), server-rendered HTML, synchronous handlers. How Pydantic models and OpenAPI are produced under Django was not read; MD-02's gate depends on it. Candidate to verify: Django Ninja (OpenAPI 3.1 output, Pydantic v2).
2. **Upload path** (L421): no source weighs the two paths; direct to storage is inferred. Whether a presigned PUT can bound size was not verified (L423).
3. **Version location** (L276): five contested positions; the URL-path major version, `/v1` from the start, is inferred.
4. **Login delegation** (L338): no source ranks it; delegation is inferred. Sender-constraining support across agent hosts was not read. The `acr`/`amr` check rests on OpenID Connect Core 1.0, not on a ledger row.
5. **Job runner**: no Python runner over a queue table written by database functions was read. The pattern is set by JOB_HOST; the library is open.
6. **Rate-limiter counters in Postgres**: by analogy to POSTGRES_FIRST, with no source.
7. **Postgres behaviour not in the ledger**: transaction-local settings lost in autocommit (ENFORCE.2), 40001 and 40P01 outside Serializable (ENFORCE.2), inferred.
8. **SameSite**: no longer a gap but the one question; the navigation check of the recorded default has no ledger row (inferred).
9. **Smaller items**:
   - The RateLimit fields and the idempotency-key header are IETF drafts (T2).
   - Atomic phases (L589) and load shedding (L363) rest on single T3 sources.
   - The upload state machine (L430) has no source.
   - Scanning was read only as one managed vendor service.
   - Signed-URL and upload-policy lifetimes: no source gives a number; recorded per project.

### Proposed intentlinks (not created; for the graph builder)

The skeleton gives no link to these nodes, though the placements give them work:
- PIG-WEB.LOGIC.SECURE.1 → ALLOCATION.GUARD.3 (`realizes`: the backend's share of authorization);
- PIG-WEB.LOGIC.ENFORCE.2 → ALLOCATION.ACT.1 (`realizes`: one operation, one call, one transaction);
- PIG-WEB.LOGIC.PROCESS.5 → ALLOCATION.ACT.1 (`realizes`: the upload state has one writer function);
- PIG-WEB.LOGIC.EXPOSE.7 → PIG-WEB.ALLOCATION.TYPE_CHAIN (`realizes`: the always-in-sync gate of MD-02);
- PIG-WEB.LOGIC.PROCESS.2 → ALLOCATION.ACT.3 (`realizes`: foreign effects deferred to a worker, review M4).

### Hand-offs to the sibling judges and to J1 (stated, not decided here)

- **J1 (ALLOCATION)**: reword the read-visibility fallback's condition ("two or more backends" already holds by default under MD-03; review M1). Resolve ACT.2 against ACT.3 on foreign mutations in the request (review M4); this unit's realization is the worker path.
- **J6 (DATA)**:
  - ENFORCE.2 retries 40001 and 40P01 at any isolation level; the level itself stays PIG-WEB.DATA.CONCURRENCY.1's.
  - Read functions refuse a missing actor, as writer functions do. The job table's claim, outcome and expiry are writer functions (PROCESS.1).
  - L530's override flag: the function side; this unit authorizes and audits it.
  - L517's departure is counted at the function-API node (X2).
  - The session table and other backend-owned single-writer tables rely on DB_API's direct-write exception. The upload row's state column needs its writer function (PROCESS.5).
- **J8 (INTERACTION)**:
  - Whether islands validate server responses at runtime (EXPOSE.6, L555).
  - The browser share of duplicate suppression, the form token, sits in PIG-WEB.INTERACTION.EDIT, and EXPOSE.3 relies on it.
  - The process type for long-lived connections (ENFORCE.4).
  - The agent tool surface's schemas fall under the sync rule (X7).
  - Islands send new request fields only after the server accepts them (EXPOSE.7).
- **J9 (TRANSVERSE)**: SECURE.1's denial alerts go to the security event log (OPERABILITY.4). The proxy carries SECURE.6's identity-blind limits and the 429 setting (TOPOLOGY.1). The cross-site navigation check of SECURE.2's recorded default may sit in the proxy or the backend.

### Questions

One (`questions.md`): the `SameSite` value of the session cookie, a trade-off between the session's function and protection against attacker-triggered navigations, both forces of the sessions node; the question gives the options with their costs, the recommendation (Lax plus a cross-site navigation check, Strict for operator consoles) and what is recorded if unanswered. Five other candidate trade-offs were considered and not raised: framework, login delegation, upload path, version location, limiter state. Each is decided by a force the node serves or by a settled placement, and `questions.md` gives the reason for each. The inherited per-user read-visibility question stays with the maintainer and is not re-asked.

Pinned:
- Nodes judged: 30 of 31 in the PIG-WEB.LOGIC branch; 1 deferred and not judged (PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery); 5 are roll-ups owning no row (PIG-WEB.LOGIC, .SECURE, .ENFORCE, .PROCESS, .EXPOSE); 133 of 133 owned rows used.
- Decided 29, undecided 1: PIG-WEB.LOGIC.SECURE.2's `SameSite` attribute on the session cookie, a genuine trade-off between the session's function (carrying a login across arrivals from other sites) and protection against attacker-triggered navigations; raised as the one question, recorded default `Lax` plus a cross-site navigation check, `Strict` for operator consoles.
- One clause inherited from J1, held in PIG-WEB.LOGIC.SECURE.1: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. J1's fallback is kept: database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends; under it ENFORCE.3, SECURE.1 and PROCESS.6 read through the function and the table loses direct SELECT. Roles that may SELECT the base tables (reporting, operator) see every row unless their own role is restricted. Not settled, not re-asked.
- Questions: 1 (SameSite on the session cookie); five other candidate trade-offs considered and not raised, each with its reason.
- Verdicts against the maintainer doctrine: 0. The one MAINT row owned here (L605, scheduled jobs) is adopted as the max choice; the doctrine rows J1 placed (L516, L527, L534, L584, L596, L604) are applied as placed; L530 (function error codes, override flag), L566 (actor from a transaction-local setting) and L587 (idempotent mutations) are applied; L517 is applied with its departure counted once at J6 (X2).
- Conflicts with J1 placements: 0. One tension inside J1 carried and routed to J1's owner: ACT.2 runs a foreign mutation the user waits for as atomic phases in the request, while ACT.3 forbids foreign effects inside the request; resolved here in favour of both by running the phases in a worker behind a 202 status resource, in-request only under a stated condition. Source positions narrowed to fit settled placements, recorded as tensions: request-wide and use-case-wide transactions (L229) and ORM-first writes (L235, L227 Active Record) yield to one database function call per transaction (ACT.1, DB_API); views and separate read stores (L237) yield to L516 and DERIVE.1; post-commit hooks (L233) carry only losable work (L600, ACT.2); limiter state in a cache service (L365) yields to Postgres until a measured limit (POSTGRES_FIRST, CACHE_STORE); replay of stored failures (Stripe v1 in L269, L546) yields to key and effect committed together (GUARD.6).
- Evidence gaps: (1) framework (L242): no source gives neutral criteria; Django is chosen on criteria the settled verdicts set (framework sessions and CSRF, L323, L330; server-rendered HTML; synchronous default), inferred; how Pydantic models and the OpenAPI description are produced under Django was not read (Django Ninja is the candidate to verify: OpenAPI 3.1 output, Pydantic v2); (2) upload path (L421): no source weighs direct-to-storage against through-the-app; direct chosen, inferred; (3) version location (L276): five contested positions; URL-path major version, `/v1` from the start, inferred; (4) login delegation (L338): no source ranks it; delegation to an OpenID Connect server (a provider or self-run) chosen, inferred; the `acr`/`amr` check rests on OpenID Connect Core, not on a ledger row; (5) no Python job runner over a queue table written by database functions was read (JOB_HOST pattern set, library open); (6) rate-limiter counters in Postgres follow POSTGRES_FIRST by analogy, no source; (7) Postgres behaviour not in the ledger: transaction-local settings vanish in autocommit, deadlocks and serialization failures outside Serializable (inferred).
- Review fixes (`../review_logic/review.md`): 17 findings for this unit (M1 to M7, m1 to m8, m10 to m12; m9 is J3's), 17 applied, 0 rejected; cross-branch resolutions X1 to X7 applied where these nodes touch them (`../cross_branch_fixes.md`).
