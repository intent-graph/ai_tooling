# Web App Philosophy: Tiers

How each tier carries the share the [allocation](allocation.md#overview) gives it, stack-neutral: durable data, the business logic tier, interaction, and the concerns that span every tier. Each section ends with its graph uid; the stack realization of each tier is in its stack defaults file, linked from the tier's introduction.

## Table of Contents

1. [Durable Data](#durable-data) _(Lines 16-79)_
1. [Business Logic Tier](#business-logic-tier) _(Lines 82-153)_
1. [Interaction](#interaction) _(Lines 156-259)_
1. [Transverse Concerns](#transverse-concerns) _(Lines 262-397)_

---

## Durable Data
<!-- Lines 16-79 -->

The database is the system of record and holds everything that must hold whoever touches the data. Several backends and other [consumers](glossary.md#consumer) (reporting, admin consoles, scripts) may share it, so what must hold for every consumer lives in the database, not in any one backend. Its five duties: organize facts, guard them, maintain structure over time, derive instead of storing, offer one contract. Stack: [Postgres Data Tier](stack_defaults_data.md#data-tier-overview).

- Gap: data lifecycle (retention, deletion, recovery) has no principle-level rule; it exists only in the stack defaults ([Data Maintenance](stack_defaults_data.md#data-maintenance)).
- Reads: simple reads directly under grants; sensitive, complex or shared reads, per-user visibility rules included, through database functions ([Guarded Consistency](#guarded-consistency)).
`DATA`

### Organized Facts

Each fact is stored once and changed in one place; the normal forms are the tests of that rule.
- Every table passes third normal form. Boyce-Codd, fourth and fifth normal form apply where they apply; stopping at third is acceptable only when every candidate key is a single column and there are no multi-valued facts (inferred).
- Where a Boyce-Codd decomposition would lose a dependency, keep the dependency-preserving third-normal-form design and enforce every dependency declaratively: the repeated determinant is covered by a composite foreign key to the table that owns the pair, so it cannot diverge and needs no sync plan (inferred). A constraint trigger under the rule of [Guarded Consistency](#guarded-consistency) only where no declarative form exists.
- Denormalization is not an organizing choice: a denormalized value is a [derived copy](glossary.md#copy) under [Derived, Not Stored](#derived-not-stored), built only with a sync plan recorded first in the table comment (what and why, sync level, freshness, change frequency, impact of divergence, drift detection and reconciliation, alerting).
- A new one-to-one attribute is a nullable column by default; a separate table only for, in this order: cardinality likely to change, a different permission boundary, an independent audit or lifecycle, blast radius on heavily used tables. Sparsity and NULL count are never reasons to split.
- A column is nullable only when absence is a meaningful state; a CHECK states that columns must be present together where they must (inferred).
- Collation is a declared property of the stored text, not of a consumer.

Realizes [System of Record](allocation.md#system-of-record). `DATA.ORGANIZE`

### Guarded Consistency

The database keeps data valid and consistent under concurrent and partial change.
- Declare every rule a declarative constraint can express: NOT NULL unless absence is a meaningful state; row-local CHECK paired with NOT NULL; foreign keys; unique, partial unique and exclusion constraints for cross-row rules; domains for value types used in several places. Constraints are named, so a violation maps to a stable error. Required, not optional.
- Rules no constraint can express (other multi-row rules, legal transitions, dependencies lost by a Boyce-Codd decomposition when no declarative form exists) are checked in the [writer function](glossary.md#writer-function) or a constraint trigger, under serializable isolation with retry or after locking the governing row. The check asserts the isolation it needs, set per [consumer role](glossary.md#consumer-role); the default isolation level is the stack's choice.
- Each business operation is one function call in its own transaction.
- Concurrent change is detected inside the writer function, which takes the expected version as a parameter; no transaction or lock is held across user think time.
- Mutual exclusion that guards correctness is enforced by the store (row version, unique constraint, row lock); a [lease](glossary.md#lease) is checked by the writer function as a fencing token (inferred). A lock outside the database is acceptable only to save duplicate work.
- State the consistency model per operation: isolation, primary or replica, accepted staleness. A check that decides a write never reads a replica (inferred); a datastore is never labelled "CP" or "AP".
- Access: each consumer has its own role, neither owner nor all-powerful; grants bound which functions it may call and which tables and columns it may read; [state columns](glossary.md#state-column) are revoked from direct update. No [row-level security](glossary.md#row-level-security) by default.
- Departs from the maintainer's practice, which treats CHECK constraints and triggers as optional defence in depth: every rule a declarative constraint can express is declared.
- Reads: simple reads that carry no logic query base tables under grants; sensitive, complex or shared reads, per-user visibility rules included, go through database functions that receive the acting user ([Authorization](allocation.md#authorization)).

Realizes Invariants, Concurrency Control and the role layer of Authorization ([Guarding Placements](allocation.md#guarding-placements)). `DATA.GUARD`

### Maintained Over Time

Schema and data evolve without breaking running code. Migrations are the only origin of change; the live database is the truth for current structure.
- Every schema change is a versioned migration in version control with the code, ordered, reviewed, applied only by automation as an explicit release step, identically in every environment. No production change, structural or data, is ad hoc SQL.
- Long-running data work is a versioned script outside the automated migration run, launched by a human under a checklist with a ticket id.
- Documentation, persistence models and function wrappers are generated from the live database; a structure the migrations would not produce is a defect to reconcile, not a new truth (the drift check inferred).
- An incompatible change keeps every running consumer working: add the new structure or function beside the old, move every consumer, then remove the old in a change marked coordinated once no deployed consumer references it. Tables and the [function API](glossary.md#function-api) alike; with a shared database this is the only route (inferred).
- Conventions evolve forward only: new objects follow the new rule, legacy ones are not renamed in bulk.
- Recovery follows objectives set per workload or data class and is never stricter than needed; at least one backup copy lies out of reach of production credentials; a backup counts only once a restore from it was tested end to end, regularly and automatically, against criteria fixed beforehand.

Realizes Type and Contract Definitions and Audit and History ([allocation](allocation.md#data-authority-placements)). Principle: [Data and Schema Change](../software_development_guidelines/change_flow_data_and_measure.md#data-and-schema-change), [Conventions Applied Forward Only](../software_development_guidelines/evolution.md#conventions-applied-forward-only), [Proving Restore](../software_development_guidelines/assurance_performance_availability.md#proving-restore). `DATA.MAINTAIN`

### Derived, Not Stored

Store the minimum and derive the rest: a value that is not stored cannot diverge from its facts.
- Compute on read by default; eligibility and other predicates over stored facts are computed, not stored.
- A derived outcome (an aggregate result) is its own row, never folded into a state value. Where a state label must agree with such facts, the facts are written first and the label flipped last by its single writer function.
- A stored derived value is a copy, allowed only when computing on read is measured too costly, in this order (inferred): same-row values as generated columns; values that must change atomically with their source, maintained in the same transaction by a trigger (by the writer function only when the source table admits no other writer); values that tolerate a stated staleness, in cache tables with scheduled refresh or an invalidation queue.
- Each stored copy has its recorded sync plan and a drift guard. A stored predicate exists only as a generated column, which cannot diverge (inferred).

Realizes [Derived Data and Aggregation](allocation.md#derived-data-and-aggregation). `DATA.DERIVE`

### Offered Contract

The database offers every consumer one published contract: a function API owned by the database owner, one business operation per call in its own transaction, one role per consumer, evolving additively.
- Writes and state transitions go through it, each state column written only by its writer function; simple reads may query base tables under grants; browsers and agents never connect.
- Its catalogue is an interface description kept in sync with the implementation by process.

Realizes Data Access Interface and the database share of Business Rules ([allocation](allocation.md#data-authority-placements)). `DATA.INTERFACE`

## Business Logic Tier
<!-- Lines 82-153 -->

The backend is the trusted entry and the workflow tier: it secures entry for every caller, enforces its share of the business logic in a core separable from transport and storage, runs as stateless disposable processes, and exposes one HTTP interface per backend. It does not decide invariants, multi-table operations, state transitions or [per-user write rules](glossary.md#per-user-rule) decidable from the stored row (the database does, and the backend's checks of those are tested copies); it holds no cache beyond one request and resolves no write conflict. Stack: [Python Application Tier](stack_defaults_logic.md#python-tier-overview) and [Backend Security](stack_defaults_logic_security.md#backend-security-overview).
- Acceptable when a single backend is the only database consumer and the team's SQL skill is low: the backend as [authority](glossary.md#authority) for all business rules.
`LOGIC`

### Secured Entry

The backend is the one gate every caller passes, human or agent, and decides nothing on the caller's word.
- Authenticate every caller, then authorize every request. Humans by the server-held session; agents by their own short-lived, revocable tokens, accepted only when issued for this server and never forwarded downstream. An ID token proves a login to the client and is never an API credential.
- Authorization of what the backend owns (product policy not stored in the data, identity): one central mechanism, deny by default, object level, on every request from every client.
- Assert the [actor](glossary.md#actor), do not decide for the database: for every call into the function API, set the verified acting user, scoped to the transaction, never from a client-supplied id.
- Parse all input at entry into the most precise type, once per process boundary: bodies, query parameters, headers, uploads, payloads read back from queues, anything a model or agent produced. Client hints, tool annotations and claimed identities never enforce.
- Bound consumption at two depths: identity-blind size, rate, read-rate and time limits at the outermost layer (413 or 408), with the client's size check as a feedback copy; identity-aware limits in the backend per operation, tighter for operations that cost money, call third parties or are expensive for agents to loop on.
- Protect harmful automation by flow (sign-up, purchase, booking, referral), not by client kind; no blanket bot blocking, because agents are intended users.
- Defend logins in layers: [MFA](glossary.md#mfa) first, then breached-password checks, then device signals and challenges known to be spoofable; never IP blocking alone. Offer MFA on every human account, phishing-resistant authenticators (passkeys, WebAuthn) preferred; require it on privileged accounts (operator, owner, administrator) and before sensitive operations (step-up). Whether it is required on every account follows the security level the project chooses by risk ([Security Across Tiers](#security-across-tiers); scope inferred). Acceptable when the project's chosen risk level requires it, or when one account's exposure is severe: MFA required on every human account.
- Server-side fetches of client- or agent-named URLs reach only destinations they allow: a host allowlist where the hosts are known, otherwise a refusal of private, loopback and link-local addresses; the connection goes only to the validated address and redirect targets are re-checked.
- Per-user read visibility: simple reads that carry no logic are written by the backend directly; sensitive, complex, high-impact or shared reads, per-user visibility rules included, go through database functions that receive the verified actor ([Authorization](allocation.md#authorization)).

Realizes Validation, Authorization and Identity and Session State ([Guarding Placements](allocation.md#guarding-placements)). `LOGIC.SECURE`

### Business Core

One business core per backend, separable from transport and storage, holds only what the [placements](glossary.md#placement) give the backend: workflow across operations, product policy not stored in the data, external calls.
- Adapters on the outside (HTML views, the structured-data interface, the agent adapter, job runners) translate requests into use-case calls and shape results; they hold no rule.
- Ports for every external system, the database function API included. Each business operation is one call in its own transaction; a step that must be atomic with another is a new database function.
- Test by share: the backend's own logic runs in isolation with fake adapters and no live database. The rules the database owns are tested against a live database; the backend never reimplements them to make its tests pass without one, except as generated or tested copies.
- Behaviour lives with its authority: rules about stored data in the database's writer functions; complex backend policy and workflow in behaviour-rich domain objects inside a thin use-case layer; a simple share is a transaction script.
- Data in, decision out: gather the data in as few calls as possible (one read function or statement, never queries in loops), then decide in code that does no fetching, testable without I/O and runnable from any driver (inferred: one exploratory source).

Realizes Business Rules, One Core for Every Client and Atomicity Ends at the Transaction ([allocation](allocation.md#rules)). Principle: [Separating Presentation, Domain and Data Access](../software_development_guidelines/construction.md#separating-presentation-domain-and-data-access). `LOGIC.ENFORCE`

### Processing Model

Stateless, disposable processes of distinct types (web, worker) built once, with every durable fact, sessions included, in backing services: processes can be added, replaced and killed freely, and the database is protected from per-client connections.
- Process memory caches nothing beyond one request; no sticky or in-memory sessions.
- Several backends may share the database; each backend is one deployable, not split into services without a measured need.
- Workers run deferred work and schedules, claim jobs from the queue the database holds, and return an unfinished job on SIGTERM.
- Each backend reaches the database as its own role, located and credentialled by configuration; a small pool per process; never a connection or open transaction per connected client, never a transaction held across a remote call.
- A supervisor owns the process lifecycle; a reverse proxy faces the internet and enforces the outermost limits; one concern per container.
- Long-lived connections (real-time channels, agent streams) are the one tolerated per-process state: clients reconnect to any process and resync from the backing services (inferred).
- No file is readable before a clean scan.

Realizes Identity and Session State, Caching, Side Effects and Deferred Work ([allocation](allocation.md#acting-placements)). Principle: [Stateless Processes](../software_development_guidelines/construction.md#stateless-processes), [Fast Start and Graceful Stop](../software_development_guidelines/construction.md#fast-start-and-graceful-stop). `LOGIC.PROCESS`

### Backend Interface

Each backend offers one HTTP interface over its one core: server-rendered HTML whose links and forms are the contract for browsers; a resource-oriented structured-data interface and an agent adapter on the same use cases for programs and agents. Every interface description consumers read (HTTP description, function API catalogue, agent tool surface) stays in sync by process, its origin recorded per project. Repeated requests are safe: safe methods change nothing, PUT and DELETE are idempotent, non-idempotent mutations offered to agents carry an [idempotency key](glossary.md#idempotency-key) the database function records. Principle: [Call Shape and Evolvable Interfaces](../software_development_guidelines/construction.md#call-shape-and-evolvable-interfaces). `LOGIC.EXPOSE`

#### Protocol Semantics

- Safe methods never change state; mutations use POST, PUT, PATCH or DELETE with their defined idempotence; a successful form POST answers 303 to a GET page. HTML forms submit only GET and POST, so HTML mutations are POST, made safe to repeat by duplicate suppression.
- Status codes carry their defined meaning, the precondition codes included for concurrency (412, 428).
- Every error has a stable machine-readable identifier separate from its human message, in a standard problem format whose detail helps the caller correct the request.
- Acceptable for an operation no standard method fits: a custom method. Never RPC-style tunnelling of every operation through POST.
`LOGIC.EXPOSE.1`

#### Self-Contained Requests

- A request carries its credential (session identifier or agent token, in a cookie or header, never in a URL except a signed file URL) and every parameter its use case needs; what it references is resolved from backing services, never from the memory of an instance.
- Server-held state is limited to the revocable session. Workflow progress is resource state in the database (state columns), addressed by identifiers in the request, never hidden in a session or a connection (inferred).
- Client and server are coupled only through the interface contract, so either can change behind it.
- Tension recorded: the strict reading, session state kept entirely on the client, yields to the revocable server session.
`LOGIC.EXPOSE.2`

#### Hypermedia Controls

- Browser: the rendered HTML is the contract; links and forms drive every transition and only the controls the user may use are rendered (a cosmetic copy: the request is re-authorized on arrival).
- Programs and agents: a described level-2 resource interface, called resource-oriented HTTP, not REST, whose contract is the machine-readable description kept in sync by process. Server-issued links where the server mints the next step (paging continuations, the created resource's location, cross-call handles); clients build no URL the description does not define.
- Acceptable when independently developed clients must keep working over a long horizon without a shared, synchronised description: full hypermedia controls in the JSON interface.
- Gap: no rule yet on hypermedia controls for agent clients.
`LOGIC.EXPOSE.3`

## Interaction
<!-- Lines 156-259 -->

The interaction tier lets humans and agents see, edit and discuss the data through clients the team does not control, and decides nothing durable: it holds copies for feedback and latency, and every decision reaches a backend. Agents are users through an adapter on the same core, never a second implementation of the rules. Stack: [Browser Surface](stack_defaults_interaction.md#browser-surface-overview) and [Agent Surface](stack_defaults_agents.md#agent-surface-overview). `INTERACTION`

### Perceivable Interface

Accessibility is a project requirement from the first design.
- State a conformance target before building; conformance is judged per full page, embedded third-party content included.
- Start from native HTML semantics and keyboard operation; [ARIA](glossary.md#aria) only where native elements cannot express the control (inferred from the rendering default).
- Users with disabilities take part in early testing, not only at acceptance.
- Format for the reader's locale and time zone where [Formatting and Localization](allocation.md#formatting-and-localization) says.
- Acceptable only for an existing page brought to the target: a retrofit. Never the plan for new pages.
- Gap: the conformance level (A, AA or AAA) is not grounded.
`INTERACTION.VISUALIZE`

### Collaboration on Data

Push is a hint over a correct pull: every page is correct on plain load.
- A client that missed events catches up from a server-issued cursor that no later commit can fall behind (a sequence id is not such a cursor), and never trusts the events it happened to receive.
- Use the simplest channel that meets direction of flow, update frequency and tolerable latency: polling, then long polling or [server-sent events](glossary.md#sse), then a two-way channel. Correctness never depends on the channel.
- A stale write is rejected and shown as a conflict with both versions, never merged silently; browsers and agent clients never resolve a conflict. Per-property last-writer-wins only for toggles, status, assignment and ordering; a text engine only for collaborative long text.
- Presence is ephemeral, broadcast through a channel with a timeout, never written to tables; a persisted last-seen is a separate, coarse field.
- A comment is its own entity: a mandatory target, its own author, lifecycle and permissions, append-only rows.
- Read, comment, edit, resolve and moderate are separate abilities, deny by default, checked per object on every request, streams and exports included; none implies another.
- A comment is never more visible than its target, on every surface the application serves: counts, notifications, search results, history, exports, ETags, real-time channels (the surface list is inferred). Notifications go only to recipients who may see the target. A report queue is required whenever people outside the team read comments.
- Agent writes are marked as agent-originated and pass the same abilities and filters.
- Per-user comment reads go through database functions ([Authorization](allocation.md#authorization)), whose written specification lists every secondary surface.
- The reporting role reads comment content and comments whose audience is narrower than their target only through database functions; the operator role sees every row.

Realizes Concurrency Control, UI and Ephemeral State and Authorization ([allocation](allocation.md#guarding-placements)). `INTERACTION.COLLABORATE`

### Agent Access

An agent is one more user with bounded authority, served through an adapter on the same core that translates and shapes but never decides.
- Agents never connect to the database and never decide access; model output and client hints are untrusted input.
- The server accepts only tokens issued for it and never forwards a caller's token. Each agent holds its own short-lived, revocable credential. Narrowest scopes, read first, elevation on demand through a precise insufficient-scope challenge, no wildcard scope; every request is still authorized in server code.
- Few purpose-specific tools, each with only the permissions it needs; no raw shell, raw SQL or arbitrary URL fetch on the live system.
- Where the application runs or hosts an agent, no session holds untrusted input, private data and the power to change state or send outward together (inferred for agents the application runs); if all three are needed, a supervised step or a split session. For agents the team does not run, no tool sends data to an arbitrary destination.
- Irreversible or external effects need approval by the owning user, shown the exact action on the application's own page; the effect's writer function refuses an agent operation without it. An approval dialog in the agent host is a hint, never the gate.
- Agents that identify and authenticate themselves are admitted to every flow their scopes allow, limited by quota per agent identity (inferred). Flows whose automation harms the business are named and protected: per-flow limits, anonymous automation denied or challenged. On a flow that hands out scarce goods or rewards automation per account, a human completes it or agents are excluded; the list of such flows is recorded per project.
- Every non-idempotent mutation offered to agents takes an idempotency key. Every agent action is logged on the server (acting identity, delegating subject, operation, correlation id, outcome), never only in a model transcript; agent writes are marked in the data.
- Acceptable when the agent is first-party and every request is still authorized in server code: coarser scopes. Inside a sandbox with no authority and no connection to the system of record: open-ended tools.

Realizes [One Core for Every Client](allocation.md#one-core-for-every-client), [Authorization](allocation.md#authorization), [Duplicate Suppression](allocation.md#duplicate-suppression) and [Audit and History](allocation.md#audit-and-history). `INTERACTION.AGENT`

### Web Environment

Seven properties of the web are accepted as given, each with the design response that keeps users able to work with the data. `INTERACTION.ENVIRONMENT`

#### Uncontrolled Client Runtime

Everybody is a non-JavaScript user until the script has loaded.
- Core read and write paths work as HTML forms and links; enhancement is added by feature detection, in loosely coupled layers, and fails without taking the core down.
- No feature works in one browser, OS or device class only; client-rendered [islands](glossary.md#island) sit inside a page whose content and navigation still work as HTML.
`INTERACTION.ENVIRONMENT.1`

#### Unstable Page Lifecycle

- Pages stay eligible for back/forward restore and refresh time-sensitive or sensitive state when restored. Acceptable for pages that display sensitive data: opting out of restore (no-store).
- Unsaved input is persisted when the page is hidden, never on unload: the browser may freeze or discard the page without notice.
- Two tabs are two concurrent writers: the version check rejects the stale one and idempotency keys absorb repeated background work (inferred). Client-side coordination between tabs is an optimization; correctness never depends on it.
`INTERACTION.ENVIRONMENT.2`

#### Non-Atomic Deployment

Tabs keep old code for days, so every client-server contract has an explicit compatibility window at least as long as an old page can stay open.
- Within the window, changes are additive and readers ignore what they do not know; before removing or changing a behaviour, its current use is found per consumer role.
- The window covers every surface used by code the team does not redeploy at once: structured-data endpoints, HTML form fields and URLs posted by old pages, the agent tools and their schemas (the last three inferred). Each interface description stays in sync by process.
- A breaking change goes [expand, migrate, contract](glossary.md#expand-migrate-contract). "[Deployed together](glossary.md#deployed-together)" only when every consumer of the changed object ships in the same deployment; a browser tab never does.

Principle: [Reversible by Design](../software_development_guidelines/change_flow_delivery.md#reversible-by-design).
`INTERACTION.ENVIRONMENT.3`

#### Caches Beyond Reach

A stored response cannot be recalled, so cacheability is declared per URL in advance.
- Every response is labelled on purpose: long lifetimes only for immutable, fingerprinted URLs; HTML and other in-place content no-cache with validators; personalised responses private or no-store.
- Every intermediary is kept on purpose, its staleness and added latency counted against its benefit.
- Acceptable for a cache the team owns and can purge, with short lifetimes for browsers and other intermediaries: long lifetimes with purging (condition inferred).
`INTERACTION.ENVIRONMENT.4`

#### Unreliable Network

Any request may fail, time out, arrive late or arrive twice.
- Core paths work as plain HTML requests; the client shows pending and failed states and keeps the user's input across a failure (inferred).
- The client retries only what is idempotent or carries an idempotency key; real-time channels reconnect and catch up by cursor.
`INTERACTION.ENVIRONMENT.5`

#### URL as Public Interface

- URLs are stable and free of author, status, file extension and implementation details; the team owns the mapping over time, and a moved resource's old URL keeps resolving.
- View state that users navigate, bookmark or share lives in the URL.
- No session token, bearer token or long-lived credential ever travels in a URL. The one exception: a short-lived, single-purpose, scope-limited signed URL for file delivery, issued after an authorization check, granting one operation on one object, expiring quickly, served from another origin than the application, its issuing response no-store and the referrer policy not leaking it (conditions inferred). One-time authorization codes bound to the client by [PKCE](glossary.md#pkce) are not a forbidden kind (inferred).
`INTERACTION.ENVIRONMENT.6`

#### Hostile Page Script

Script in the page holds the application's privileges, so assume it may be hostile.
- No long-lived credential is readable by script: the session cookie is opaque, HttpOnly, Secure and SameSite.
- Output is escaped by default by the templates; [CSP](glossary.md#csp) is the second layer, not the first. XSS prevention comes before [CSRF](glossary.md#csrf) defence, because XSS defeats every CSRF defence.
- [CORS](glossary.md#cors) is not access control; CSRF defence stands on its own.
- User uploads are served from a distinct registrable domain. Content written by other users or by models is untrusted wherever it is rendered (inferred for model output).
- No check that grants access or protects integrity runs in the page.
`INTERACTION.ENVIRONMENT.7`

## Transverse Concerns
<!-- Lines 262-397 -->

Properties that span every tier are stated once and designed in across browser, backend, database and every other consumer of the data, not added per tier. Each becomes an automated check where one exists: the interface [drift gate](glossary.md#drift-gate), the function-API catalogue diff, page budgets, module-boundary checks, tests at every tier. Stack: [Transverse Concerns](stack_defaults_transverse.md#transverse-overview). `TRANSVERSE`

### Security Across Tiers

- Serve every page and every API over encrypted transport with strict transport enforcement and no mixed content; database connections of every consumer role included.
- Collect only the data the user's goal needs. Never log secrets, session ids, tokens, keys, payment data, connection strings or unneeded personal data, trace headers included; a hashed session id is acceptable when sessions must be tracked.
- Give every threat category an owning tier the requester cannot modify (table below). Answer insecure design with a threat model per critical flow and trust boundary (authentication, access control, business operations, agent access), revisited when a placement on that flow changes, with misuse-case tests per tier; the allocation records are the model's input, not the model.
- State each property as a verifiable requirement with a traceable id, at a level chosen by risk and paired with outcome measures (a level measures coverage, not outcomes); the threat list is an awareness map, never the requirement set.

| Threat category | Owning tier |
|---|---|
| Broken access control | backend and database, as [Authorization](allocation.md#authorization) divides it |
| Security misconfiguration | headers, CSP and deployment |
| Supply chain | the pipeline and dependencies |
| Cryptographic failures | the backend, the proxy's TLS, the database connections of every role, storage at rest |
| Injection | backend and database: precise types at every entry, typed function parameters |
| Insecure design | a threat model per critical flow and trust boundary, revisited when a placement on the flow changes; misuse-case tests per tier |
| Authentication failures | backend |
| Software or data integrity | the delivery pipeline, and the parsing tier for untrusted serialized input; declarative constraints are not this control |
| Logging and alerting failures | operations |
| Mishandling of exceptional conditions | the tier that holds each check, which fails closed |

Never claim a stronger read-visibility guarantee than [Authorization](allocation.md#authorization) gives: roles that may read the base tables see every row unless their own role is restricted.

The tier map is inferred. Rests on [Trust Boundary](allocation.md#trust-boundary). Principle: [Design-Time Risk Modelling](../software_development_guidelines/transverse_security.md#design-time-risk-modelling), [Verification Depth and Design Review](../software_development_guidelines/assurance_docs_security.md#verification-depth-and-design-review), [Minimisation, Classification and Design-In](../software_development_guidelines/transverse_privacy.md#minimisation-classification-and-design-in). `TRANSVERSE.SECURITY`

### Measured Performance

- Judge user-perceived performance on field data at the 75th percentile, segmented by device class; never averages.
- Lab budgets gate each change in the build and never override field data. Acceptable before launch, or when traffic is too low for a stable 75th percentile: lab data as the primary source.
- Optimise only after measurement has named the critical path.
- Join field page metrics through the correlation id to server timing and database time per request, so work placed in database functions stays visible (inferred).

Feeds the Performance and Latency forces ([allocation](allocation.md#forces)). Principle: [Performance](../software_development_guidelines/assurance_performance_availability.md#performance). `TRANSVERSE.PERFORMANCE`

### Standards and Contracts

Every contract between tiers or consumers is an explicit artifact, readable without the producer's code and always in sync with the implementation.
- It states structure and meaning: names, types, nullability, units, invariants, owner, version.
- Every interface description consumers read (HTTP description, function API catalogue, agent tool surface) is kept in sync by process and a CI gate that fails on drift.
- The provider's contract is authoritative; consumer-driven contracts are tests, never the origin, used where consumers are separate teams in a closed community.
- Change by compatible additions, with tolerant readers and conservative writers; versioning is the exception. Know how a behaviour is used before changing or removing it: per consumer role, from its grants and the session roles audit records (inferred).
- A breaking change goes expand, migrate, contract, coordinated with every consumer, unless every consumer of the changed object ships in the same deployment as the change. For the function API the new function name is the expand step; no formal version number.
- Departs from the maintainer's practice, where "deployed together" is the general rule for breaking changes: it holds only under that same-deployment condition.

Requires [Type and Contract Definitions](allocation.md#type-and-contract-definitions). Principle: [What Counts as Compatible](../software_development_guidelines/assurance_interfaces_data.md#what-counts-as-compatible), [Contract Tests](../software_development_guidelines/assurance_interfaces_data.md#contract-tests), [What a Contract States](../software_development_guidelines/construction.md#what-a-contract-states), [Expand, Migrate, Contract](../software_development_guidelines/evolution.md#expand-migrate-contract). `TRANSVERSE.CONTRACTS`

### Operability

The running system is observed, tested and delivered as one whole across every tier, designed in from the start. `TRANSVERSE.OPERABILITY`

#### Whole-Path Observability

- One correlation id per user interaction, carried from the browser through the backend into the database transaction, stamped on every log record, span, client event and audit row (the database leg inferred). Consumers outside the request path carry their identity and ticket id in the session.
- A security event log with its own store, integrity and retention records validation failures, authentication successes and failures, authorization failures, session failures, application errors and use of higher-risk functions. Changes to privileges, roles, credentials, grants and the role-to-actor pairing are security events; business data changes never go there.
- A retention decision per record type (application logs, traces, security event log, audit trail), set by legal, regulatory and contractual obligations, no shorter and no longer; recorded even where no obligation exists.
- Nothing secret or unneeded and personal is logged or placed in trace context.

Kept apart from [Audit and History](allocation.md#audit-and-history). Principle: [Correlation and Context Propagation](../software_development_guidelines/operation_objectives_and_signals.md#correlation-and-context-propagation), [Events Logged](../software_development_guidelines/transverse_security.md#events-logged), [Log Protection and Sanitising](../software_development_guidelines/transverse_security.md#log-protection-and-sanitising), [Retention Periods](../software_development_guidelines/transverse_privacy.md#retention-periods). `TRANSVERSE.OPERABILITY.1`

#### Proportioned Testing

Test at the lowest level that can catch the failure, and add the low-level test when a high-level test finds a bug; ratios are not prescribed.
- Logic placed in the database is tested on a real engine of the production kind; never a mock or another engine.
- Each data test is isolated, by a rolled-back transaction by default; tests that mutate shared data never commit. Behaviour that only shows at commit or between sessions (serialization retries, lock waits, deferred constraints, the [outbox](glossary.md#outbox)) is tested with concurrent committing sessions in a disposable database, never a shared one.
- Every invariant enforced procedurally (serializable with retry, or a lock) has a concurrent test in the default suite (inferred).
- Backend product policy and request parsing are tested in memory.
- Authorization is tested by denial: each role and actor is refused what it may not do. End-to-end tests are few, on critical journeys.
- Per-user read visibility: [sensitive reads](glossary.md#sensitive-read) in database functions are tested by denial against the functions themselves ([Authorization](allocation.md#authorization)).

Principle: [Test Level Mix](../software_development_guidelines/assurance_behaviour.md#test-level-mix), [Tests Without Durable Effect on Data](../software_development_guidelines/assurance_behaviour.md#tests-without-durable-effect-on-data), [Placement of Domain Logic](../software_development_guidelines/construction.md#placement-of-domain-logic).
`TRANSVERSE.OPERABILITY.2`

#### Reproducible Delivery

- One codebase per application in version control, many deploys. Build, release and run are separate: build once, assets included, and promote the same immutable artifact everywhere.
- Configuration apart from code; secrets out of source.
- Every environment runs the production database engine and version, with no adapters hiding differences.
- Schema and function-API changes are versioned migrations promoted through the same pipeline, run once per release before the new code starts, additive across the release window (inferred).
- Release in small, frequent increments.
- Gap: no rollback or fix-forward rule for releases or data changes; principle in [Rollback](../software_development_guidelines/change_flow_delivery.md#rollback) (MD-10).

Principle: [Build Once, Promote One Artifact](../software_development_guidelines/change_flow_delivery.md#build-once-promote-one-artifact), [Separation of Configuration from Code and Secrets](../software_development_guidelines/transverse_config_environments.md#separation-of-configuration-from-code-and-secrets), [Environment Parity](../software_development_guidelines/change_flow_delivery.md#environment-parity), [Delivery Path and Gating of Database Change](../software_development_guidelines/change_flow_data_and_measure.md#delivery-path-and-gating-of-database-change), [Cadence and Batch Size](../software_development_guidelines/change_flow_delivery.md#cadence-and-batch-size).
`TRANSVERSE.OPERABILITY.3`

### Deliberate Evolution

The system changes deliberately: costly decisions named and recorded, growth in small tested increments, few mature technologies, deployables split only on measured need, teams cut by capability. `TRANSVERSE.EVOLUTION`

#### Explicit Decisions

- Identify the decisions that are costly to get wrong early; decide each when enough is known, not all up front.
- Record each with its forces, alternatives and the condition that would reverse it, per-project decisions included: the interface origin direction with its criteria, any adoption of row-level security with its conditions.
- Test changes against the constraints a decision set, automatically where a check exists.

Principle: [Content of a Record](../software_development_guidelines/evolution.md#content-of-a-record), [Effort and Timing on Costly Decisions](../software_development_guidelines/construction.md#effort-and-timing-on-costly-decisions).
`TRANSVERSE.EVOLUTION.1`

#### Incremental Change

- Keep internal quality from the start; build nothing for presumed future features, and invest in tests, refactoring and continuous delivery.
- Design capacity headroom for about 10x the current load; reaching about 100x is planned as a rewrite of the part concerned, not anticipated in code (inferred).
- Make fit explicit as automated fitness functions, non-functional ones included.
- Take debt only prudently, deliberately and recorded. Replace at seams, never by big-bang rewrite.

Principle: [Step Size and Feedback](../software_development_guidelines/evolution.md#step-size-and-feedback), [Taking Debt Versus Investing in Quality](../software_development_guidelines/evolution.md#taking-debt-versus-investing-in-quality), [Growth Horizon](../software_development_guidelines/construction.md#growth-horizon), [Gates That Cannot Be Skipped](../software_development_guidelines/assurance_rules.md#gates-that-cannot-be-skipped), [Replacement Versus Rewrite](../software_development_guidelines/evolution.md#replacement-versus-rewrite).
`TRANSVERSE.EVOLUTION.2`

#### Deployable Boundaries

- Each backend is one deployable, modular by business concept. Several backends may share the database, but that does not by itself license splitting a backend.
- Split off a further deployable only when a named force requires it: independent scaling, independent release by separate teams, fault isolation that matters, or a different runtime need. The boundary has proven stable, the distribution premium is budgeted and the force is stated. A later split moves no data, since the data seam is already the function API (inferred).
- Bounded contexts map to domain schemas in the shared database, each with its own functions and roles (inferred).
- A new deployable reaches data only through the function API with its own role; it never writes tables beside it or holds a second system of record.
- Acceptable when the domain is well known, the size requires distribution, the parts develop and deploy independently and the team already runs distributed systems: services first. The evidence for services first is anecdotal.

Principle: [Initial Shape, One Unit or Several](../software_development_guidelines/construction.md#initial-shape-one-unit-or-several), [Distribution Premium and Its Reversal](../software_development_guidelines/construction.md#distribution-premium-and-its-reversal), [Placing Service Boundaries](../software_development_guidelines/construction.md#placing-service-boundaries).
`TRANSVERSE.EVOLUTION.3`

#### Few Mature Technologies

- Adopt few, mature technologies with known failure modes: novelty is a scarce budget, and simplicity is a reliability property.
- A new technology enters as a replacement, with the retirement of the older one planned and owned, and only when an existing one's measured limit is reached and its perpetual operating cost is budgeted. The rule counts runtimes, stores, services and frameworks, not the paradigm chosen inside an adopted language (inferred).

Realized in the stack by [Stack Placements](allocation.md#stack-placements) (Postgres first). Principle: [Adding as Replacing](../software_development_guidelines/evolution.md#adding-as-replacing). `TRANSVERSE.EVOLUTION.4`

#### Team-Shaped Structure

- Teams are cross-functional around a capability, never organised by layer; no database team writes other teams' business operations. The database owner is a named role inside the team.
- When teams multiply, each capability team owns its domain schema, functions and backend; one named [owner role](glossary.md#owner-role) holds conventions, roles, grants and review of the function API catalogue diff (inferred). A cross-schema business function belongs to the team that owns the workflow, reviewed by the database owner role (inferred).
- Cross-domain business operations are composed inside the database through published functions, never by direct access to another domain's tables.
- Module and schema boundaries are cut with the team boundaries.

Principle: [Teams and Structure](../software_development_guidelines/construction.md#teams-and-structure), [Data Ownership by One Application](../software_development_guidelines/construction.md#data-ownership-by-one-application).
`TRANSVERSE.EVOLUTION.5`
