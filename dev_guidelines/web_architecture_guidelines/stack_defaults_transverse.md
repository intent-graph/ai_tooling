# Stack Defaults: Transverse Concerns

Defaults for the properties that cut across the data, logic and interaction tiers on this stack: security, page performance, contract verification, operations, runtime topology and evolution. Each property is realized once and, wherever a check exists, turned into an automated gate.

## Table of Contents

1. [Transverse Overview](#transverse-overview) _(Lines 19-27)_
1. [Security Defaults](#security-defaults) _(Lines 30-92)_
1. [Page Experience Targets](#page-experience-targets) _(Lines 95-104)_
1. [Contract Verification and Meaning](#contract-verification-and-meaning) _(Lines 107-137)_
1. [Operations](#operations) _(Lines 140-219)_
1. [Runtime Topology](#runtime-topology) _(Lines 222-265)_
1. [Evolution Defaults](#evolution-defaults) _(Lines 268-300)_

---

## Transverse Overview
<!-- Lines 19-27 -->

The stack realizes each cross-tier property once: [ASVS](glossary.md#asvs)-based security with one TLS edge and managed secrets, Core Web Vitals targets, one verification per contract seam, tracing from the browser into the database transaction, a buffering reverse proxy in front of [WSGI](glossary.md#asgi) workers, and decisions kept in [ADRs](glossary.md#adr). Several backends may share the database; each backend is one deployable and is not split into services without a measured need. Refines [Transverse Concerns](philosophy.md#transverse-concerns); the [placement](glossary.md#placement) of responsibilities is in the [Allocation Matrix](allocation.md#allocation-matrix).

Access control is verified where [Authorization](allocation.md#authorization) puts it, database read functions for [sensitive reads](glossary.md#sensitive-read) included; no access-control requirement is marked met on a stronger guarantee than that rule gives ([Security Requirement Catalogue](#security-requirement-catalogue), [Testing](#testing)).

The hosting model is a per-project choice, recorded as an ADR: a prototype takes the fastest secure path, and an orchestration platform is added when reliability and scaling are needed. The self-managed defaults below (process manager per host, proxy serving static files, a file fallback for secrets) are one acceptable route, and each affected section names what changes on an orchestrator ([Secrets](#secrets), [Process Placement](#process-placement), [Static Assets and CDN](#static-assets-and-cdn)).

`PIG-WEB-TRANSVERSE`

## Security Defaults
<!-- Lines 30-92 -->

Security is verified against ASVS 5.0 at a recorded level paired with outcome measures. Each security property is testable and has one owner. Refines [Security Across Tiers](philosophy.md#security-across-tiers). `PIG-WEB-TRANSVERSE.SECURITY`

### Security Requirement Catalogue

ASVS 5.0 is the catalogue of verifiable requirements, cited by versioned id in traces, tests and reviews. The OWASP Top 10 is an awareness map only.
- The verification level is recorded per project, by risk. Level 2 by default; Level 3 when a breach would be critical (payments, health, safety); never Level 1.
- The level measures activity and coverage, not outcomes: it is recorded beside outcome measures chosen per project (for example open findings by severity and age, time to fix a vulnerability, incidents and their causes; examples inferred) and is never reported as proof that the system is safer.
- Each requirement is verified at the tier the placements name: [writer functions](glossary.md#writer-function) for [per-user write rules](glossary.md#per-user-rule), the backend for product policy and identity, database roles per [consumer](glossary.md#consumer), database read functions for sensitive reads; no access-control requirement is marked met on a stronger guarantee than that rule gives.
- Where a requirement has an automated check, it runs in the pipeline ([Delivery and Configuration](#delivery-and-configuration)).

Changes when: the project's risk class changes; record the level as an ADR.

Principle: [Anchor Framework](../software_development_guidelines/transverse_security.md#anchor-framework), [Maturity Targets and Cycle](../software_development_guidelines/transverse_security.md#maturity-targets-and-cycle).
`PIG-WEB-TRANSVERSE.SECURITY.1`

### Transport Security

TLS terminates at the single reverse proxy.
- The proxy redirects HTTP permanently and forwards only HTTPS-originated requests. Automated certificates (the proxy or a tested ACME client), TLS 1.3 with 1.2 only for clients that need it.
- [HSTS](glossary.md#hsts) on every HTTPS response, set in one place. Long max-age on the application's host, reached in steps (inferred); `includeSubDomains` once its subdomains serve HTTPS.
- Session and [CSRF](glossary.md#csrf) cookies are Secure; no subresource is loaded over HTTP.
- Proxy to application server: a unix domain socket on the same host. Open: re-encryption across a network hop.
- Database connections that cross a network hop, from every [consumer role](glossary.md#consumer-role) (backends, BI, consoles, scripts), are encrypted and verify the server certificate (inferred; gap: no source on Postgres connection settings was read).

Changes when: the team controls the registrable domain and commits all its subdomains, internal ones included, to HTTPS long term; HSTS preload is then the target, recorded as an ADR because it is slow to undo.
`PIG-WEB-TRANSVERSE.SECURITY.2`

### Security Headers and CSP

Every response carries a strict [CSP](glossary.md#csp) with a fresh per-response nonce from the Python templates; build-time pages use hashes. CSP is the second layer after template escaping.
- Rollout: Report-Only first, violations to the Reporting API endpoint, fix, then enforce.
- A small baseline header set on every response, obsolete headers removed.
- One setter per header (inferred): the application for CSP (it holds the nonce), the proxy for the static baseline so static files carry it too.
- A page carrying a nonce is never stored in a shared cache (inferred).

`PIG-WEB-TRANSVERSE.SECURITY.3`

### Secrets

A managed store is the [authority](glossary.md#authority) for every secret.
- Least privilege per service and per database consumer role (each backend, reporting, operator, owner, each with its own credentials; inferred), automated rotation, audited access; short-lived dynamic credentials where the store issues them.
- Delivery at process start by runtime injection from the store: a mounted file readable only by the service account, or the store's own interface; never inside the artifact or the repository. An environment variable is an exception, allowed only where the platform offers neither or where the process environment is shown not to leak (no other process can read it, the framework never dumps it, debug off); the channel and the reason are recorded as an ADR.
- The framework signing secret is held like any other, never committed, rotated.
- CI/CD: least-privilege service accounts, secrets scoped per environment, none in pipeline output. Secret-access logs kept as long as obligations require, at least 90 days where none exists.
- Hosting is a per-project choice: on self-managed hosts without an orchestrator, one acceptable route, the store is a technology to add, and until then a file outside source control, readable only by the service account and rotated by a scheduled task, is the recorded exception; on an orchestrated platform its secret store is the managed store.

Principle: [Central Secret Custody and Lifecycle](../software_development_guidelines/transverse_config_environments.md#central-secret-custody-and-lifecycle), [Delivery Channel to the Running Software](../software_development_guidelines/transverse_config_environments.md#delivery-channel-to-the-running-software).
`PIG-WEB-TRANSVERSE.SECURITY.4`

### Supply Chain

Every artifact the system runs has hash-pinned dependencies, a continuously scanned [SBOM](glossary.md#sbom), components from official sources and signed build provenance verified before deploy.
- Python: lockfile with hashes, `--require-hashes` over the whole tree. JavaScript build dependencies: lockfile, installed from it exactly (inferred). Container base images pinned.
- SBOM per release artifact, scanned continuously, not only at build. Updates go through the staged pipeline, then a staged or canary rollout.
- Provenance: signed, from a hosted build platform, verified before deploy; [SLSA](glossary.md#slsa) Build L2 is the floor. The level reached, and the gap to the floor where below it, is recorded per project.
- Database extensions and Postgres packages come from official sources at a pinned version (inferred).

Acceptable when insider or credential-compromise risk matters or the software is distributed to others: a hardened, isolated build, Build L3 (runs cannot influence one another, the signing secrets are out of the build steps' reach), recorded as an ADR.

Principle: [Declare and Lock](../software_development_guidelines/ownership_lifecycle_containment.md#declare-and-lock), [Channels, Mirrors and Supply-Chain Integrity](../software_development_guidelines/ownership_lifecycle_containment.md#channels-mirrors-and-supply-chain-integrity), [Inventory, Watching and End of Life](../software_development_guidelines/ownership_lifecycle_containment.md#inventory-watching-and-end-of-life), [Build Provenance and Match to Source](../software_development_guidelines/assurance_rules.md#build-provenance-and-match-to-source).
`PIG-WEB-TRANSVERSE.SECURITY.5`

## Page Experience Targets
<!-- Lines 95-104 -->

Core Web Vitals at the 75th percentile, per device class, from field data, are the targets: [LCP](glossary.md#lcp) 2.5 s, [INP](glossary.md#inp) 200 ms, [CLS](glossary.md#cls) 0.1. Build budgets per page type are the gate before release. Refines [Measured Performance](philosophy.md#measured-performance).
- Build budgets cover the lab-measurable vitals (LCP, CLS) and page weight (inferred); a build over budget fails or the page is optimised. INP is gated on field data after release.
- The server's share of each page is visible: Server-Timing carries server and database time to authenticated and authorised audiences only, joined to field data through the trace id (inferred).
- Derived server budget (inferred): about 1 s at most for the server part of a page at the 75th percentile, well under 1 s for an interaction's request; work expected to exceed a few seconds or the request timeout is deferred; 1 s is the interactive target, not the cut-off. Database time counts inside it. No source states a server target.
- Not adopted: the sample budget numbers of the public performance-budget guide.
- Gap: no latency target for the agent surface.

`PIG-WEB-TRANSVERSE.PERFORMANCE`

## Contract Verification and Meaning
<!-- Lines 107-137 -->

Every contract has a verification matched to its seam, run in the pipeline, and a written meaning, owner and lifecycle. The contracts are the [function API](glossary.md#function-api), the tables granted to BI, the HTTP interface, the agent tool surface and external services. Breaking changes go [expand, migrate, contract](glossary.md#expand-migrate-contract); "[deployed together](glossary.md#deployed-together)" holds only when every consumer of the changed object ships in the same deployment as the migration. Refines [Standards and Contracts](philosophy.md#standards-and-contracts). `PIG-WEB-TRANSVERSE.CONTRACTS`

### Contract Verification

One verification per seam.

| Seam | Verification |
|---|---|
| Function API (several consumers, deployed separately) | Provider side: catalogue diff in CI fails on a removed function or incompatible signature unless marked coordinated. Consumer side: typed wrappers generated from the catalogue, and each consumer's integration suite runs against the candidate schema before a migration is promoted (inferred). |
| Tables and columns granted to BI | The same catalogue diff covers every object granted to a consumer role (inferred); a removed or retyped granted column fails the gate; then expand, migrate, contract. |
| HTTP interface to the team's own browser code | The description is kept in sync with the implementation by the always-in-sync gate; diff against the last released description fails on a breaking change inside the compatibility window; [island](glossary.md#island) types are generated from it at build time. |
| Agent tool surface | Description, breaking-change diff and machine-readable deprecation signals are the whole contract; the same [drift gate](glossary.md#drift-gate) and compatibility window apply as for HTTP. |
| External services | Contract tests of the doubles run daily or on the supplier's change rhythm; a failure opens a realignment task. |

- The "coordinated" mark holds only for the contract phase of expand, migrate, contract, or when every consumer of the changed object ships with the migration.
- Consumer-driven tests are not required for the team's own browser islands; agents run code the team does not control, so none can be collected.

`PIG-WEB-TRANSVERSE.CONTRACTS.1`

### Contract Meaning and Ownership

A schema is necessary, not sufficient.
- Units, ranges and precision are enforced as column types and constraints in Postgres and as field constraints in Pydantic; where that is impossible they are written next to the object with time zone and rounding. The meaning text lives in the catalogue next to each object (inferred).
- Every contract records owner, meaning, quality rules, freshness or availability promise and lifecycle status (active, deprecated, retired). This includes the function API and the tables BI reads.
- Owner: the database owner for the function API and granted tables (a domain schema's owning team when teams multiply); the backend team for HTTP.
- The function API carries no formal version number: change is carried in names, a new function beside the old (the expand step). The HTTP description carries its document version and the deprecation signals.
- Money and decimals cross JSON as strings with stated precision and currency or unit (inferred).

`PIG-WEB-TRANSVERSE.CONTRACTS.2`

## Operations
<!-- Lines 140-219 -->

One W3C trace context runs from the browser through backend and workers into the database transaction, with logs, client telemetry and the four golden signals correlated to it. Refines [Operability](philosophy.md#operability). `PIG-WEB-TRANSVERSE.OPERABILITY`

### Tracing and Logs

- One trace context per user interaction: from the browser, through the backend, onto every outbound call, into each job row so workers continue the trace (job carrier inferred).
- Into the database: the backend sets the trace id in a transaction-local setting beside the [actor](glossary.md#actor); writer functions and audit triggers write it on transition and history rows (inferred). Owner-run jobs carry the ticket id in the statement comment.
- Logs: one JSON event per line on stdout, unbuffered, with trace and span id. Nothing secret or personal in logs or trace headers.
- Library instrumentation for the framework, HTTP clients and the Postgres driver; code spans only around business steps.
- An incoming traceparent from an unauthenticated or external caller is recorded but does not decide sampling.
- Keep every trace while volume allows; then tail sampling keeps every error and slow trace (inferred). Logs still carry the trace id of every error.
- Server-Timing carries server and database time to authenticated and authorised audiences only.

Principle: [Instrumentation and Log Emission](../software_development_guidelines/operation_objectives_and_signals.md#instrumentation-and-log-emission), [Trace Sampling](../software_development_guidelines/operation_objectives_and_signals.md#trace-sampling).
`PIG-WEB-TRANSVERSE.OPERABILITY.1`

### Client Telemetry

- The rendered page carries the trace id of the request that produced it (inferred); client events and island fetches carry it or a child traceparent. No dependence on browser OpenTelemetry.
- Errors: both global handlers. Vitals: web-vitals, segmented by device class. Delivery: `sendBeacon` on `visibilitychange`, stamped with release and trace id (inferred).
- A Reporting API endpoint receives CSP violations, deprecations, crashes and interventions; it is the report sink of the CSP rollout.
- The collection endpoint treats every event as untrusted input (validated, sanitised before logging) and collects no personal data.

Principle: [Vantage Points](../software_development_guidelines/operation_objectives_and_signals.md#vantage-points).
`PIG-WEB-TRANSVERSE.OPERABILITY.2`

### Monitoring

- The four golden signals (latency, traffic, errors, saturation) per process type and for Postgres, as histograms; black-box probes of critical journeys.
- Indicators: the page targets at the 75th percentile, availability and server latency of the critical journeys; objectives set from what users need.
- Pages to a human only on urgent, user-visible conditions; everything else is a ticket.
- `pg_stat_statements` on from the first deploy; its per-role figures give database load per consumer role (backends, BI, operators) (inferred).
- The triggers that move the Postgres-first placements are measured, not guessed (inferred): queue backlog age and claim contention, commit latency under NOTIFY, cache hit latency and load on the primary. Job failures, durations and missed runs are monitored; the drift guard on denormalised data alerts on divergence.

Principle: [What Is Measured - Service and Resource Signals](../software_development_guidelines/operation_objectives_and_signals.md#what-is-measured---service-and-resource-signals), [Paging Criterion and Rule Hygiene](../software_development_guidelines/operation_objectives_and_signals.md#paging-criterion-and-rule-hygiene), [Indicators](../software_development_guidelines/operation_objectives_and_signals.md#indicators).
`PIG-WEB-TRANSVERSE.OPERABILITY.3`

### Security Event Log

- Written to a central collector outside the application database, in one vocabulary, over secure transport; copied to read-only storage as soon as possible; every access recorded.
- Records validation failures, authentication results, authorization failures (agent identity fields included), session failures, errors and use of higher-risk functions.
- Refusals made inside writer functions and Postgres privilege checks reach it two ways (inferred): the backend logs each refusal it receives with actor, role and trace id, and Postgres's own log (authentication failures, privilege errors, role changes) is shipped to the same collector. This covers consumers outside a backend: BI, operators, scripts.
- Business history stays in the database; the two records stay apart.

Principle: [Entry Content, Time and Format](../software_development_guidelines/transverse_security.md#entry-content-time-and-format).
`PIG-WEB-TRANSVERSE.OPERABILITY.4`

### Testing

- Every test that touches data runs on Postgres at the production version, in a disposable database per run, never production.
- Each test runs in a rolled-back transaction; in any shared environment a mutating test runs in a forced-rollback boundary.
- Behaviour visible only at commit (serialisation failures and retries, lock waits between sessions, deferred constraints, [outbox](glossary.md#outbox), NOTIFY) is tested with concurrent committing sessions in a disposable database, then dropped, never in a shared one (inferred).
- Concurrency tests for every invariant enforced procedurally are part of the default suite (inferred).
- Database tests connect as the consumer role under test, never as the owner (inferred). They cover writer functions, constraints, grants per role, the actor pairing and refusal of writes without an actor.
- Backend product policy and parsing are tested in memory. End-to-end tests are few, on critical journeys.
- Per-user read visibility: the shared denial-test suite every backend runs is part of the default suite, and denial tests of the database read functions run against those functions.

`PIG-WEB-TRANSVERSE.OPERABILITY.5`

### Delivery and Configuration

- Settings load once into a typed, validated object, built at start and injected. With Django, the settings module reads it from the environment.
- Behaviour config (limits, defaults, toggle defaults) is versioned, reviewed and promoted with the release. Deploy-specific values (addresses, credential references) are per deploy. Secrets come from the store.
- Release gates: debug off and the framework's deploy check run in the pipeline.
- Stages: first lint, unit tests, the interface drift gate and the catalogue diff; then integration on real Postgres and the consumer suites; then the few end-to-end tests.
- Migrations of the shared database are released once, in one process, before any consumer release that depends on them (inferred). They stay additive through the compatibility window; removals only in the contract phase, once no consumer role uses the old object.
- Static assets are collected at build into the artifact, not at release.
- Release toggles are short-lived, each with a removal task created with it.
- Gap: no rollback or fix-forward rule for releases or data changes; principle in [Rollback](../software_development_guidelines/change_flow_delivery.md#rollback) (MD-10).

Principle: [Shape of Per-Environment Configuration](../software_development_guidelines/transverse_config_environments.md#shape-of-per-environment-configuration), [Separating Release From Deployment](../software_development_guidelines/change_flow_delivery.md#separating-release-from-deployment), [Staged Pipeline and Human Gates](../software_development_guidelines/change_flow_delivery.md#staged-pipeline-and-human-gates).
`PIG-WEB-TRANSVERSE.OPERABILITY.6`

### Incident Response

Deferred for the web-specific realization: not researched or judged, and no web practice is decided. How incidents are declared, handled and reviewed is decided in the software development guidelines.

Principle: [Incidents](../software_development_guidelines/operation_response_and_readiness.md#incidents), [Operational Readiness](../software_development_guidelines/operation_response_and_readiness.md#operational-readiness), [Runbooks and Playbooks](../software_development_guidelines/operation_response_and_readiness.md#runbooks-and-playbooks).
`PIG-WEB-TRANSVERSE.OPERABILITY.7`

## Runtime Topology
<!-- Lines 222-265 -->

One buffering reverse proxy is the only public entry and terminates TLS. A WSGI server runs under a process manager. Web and worker processes start from one image; static assets are built once and served outside Python. `PIG-WEB-TRANSVERSE.TOPOLOGY`

### Reverse Proxy Edge

- The proxy is the only public entry; the application listens on a unix socket or private address.
- It buffers requests and responses, except on streaming routes ([SSE](glossary.md#sse), streamed agent responses), where buffering is off so events are not held back (inferred).
- It sets Host and the forwarded scheme itself, overwriting any client copy. The application trusts forwarded headers only from the proxy's address and validates Host against its allowed list.
- It carries TLS, compression, static files and the outermost request limits ([Abuse and Rate Limits](stack_defaults_logic_security.md#abuse-and-rate-limits)).
- Product choice depends on the hosting model, a per-project decision. Criteria: full buffering, automatic certificates or a tested ACME client, forwarded-header control. No source ranks products.

`PIG-WEB-TRANSVERSE.TOPOLOGY.1`

### Application Server

- WSGI with Gunicorn sync workers serves request and response work (inferred: the server choice rests on one source); foreign effects run in workers through the outbox, not in the request.
- Routes that make blocking external calls in the request (the identity provider's code exchange at login, external reads, model calls) use threaded workers or the ASGI process type, or carry a short timeout (inferred).
- Long-lived connections (real-time channels, streamed agent responses) run on Uvicorn ASGI as their own process type routed by the proxy (inferred), so request work keeps the sync workers' isolation. Whether the product needs them is decided in [Real-Time Channels](stack_defaults_interaction.md#real-time-channels) and the [Agent Surface](stack_defaults_agents.md#agent-surface-overview).
- Worker count starts at (2 x cores) + 1 and is tuned by measurement. The connection budget covers every database consumer, all backends, BI and operators included (inferred); pooling is decided in [Connections and Pooling](stack_defaults_data.md#connections-and-pooling).
- Workers stop gracefully on SIGTERM. The development server never runs in production.
- Python is the only request-time server runtime; JavaScript runs at build time only.

`PIG-WEB-TRANSVERSE.TOPOLOGY.2`

### Process Placement

- One image per release, multi-stage, non-root, pinned base. Web, worker and admin processes start from it with the same config.
- Admin consoles and scripts run from the same image with the operator role's credentials. Migrations and human-run data jobs use the [owner role](glossary.md#owner-role) under the [data-job checklist](glossary.md#data-job-checklist) (inferred).
- The hosting model is chosen per project and recorded as an ADR: a prototype takes the fastest secure path; an orchestration platform is added when reliability and scaling are needed.
- On one or a few self-managed hosts without an orchestrator, one acceptable route: each unit runs a process manager with several workers, workers run as extra units on the web host, and a supervisor runs everything as an unprivileged account.

Changes when: with a container orchestrator, one server process per container replaces the process manager; the unprivileged supervisor, same-image and same-config rules still hold.
`PIG-WEB-TRANSVERSE.TOPOLOGY.3`

### Static Assets and CDN

- Assets are built once into the release artifact with fingerprinted names; the proxy serves them with long-lived immutable caching and compression.
- Fingerprinted files of previous releases stay available for the compatibility window, as long as an old page can stay open; the asset store is cumulative and pruned after the window (inferred).
- A [CDN](glossary.md#cdn) caches fingerprinted files long term and micro-caches only anonymous responses carrying no nonce and no personal data.
- On the self-managed route the proxy on the application host serves static files; on an orchestrated platform the platform's edge or object store may serve the built assets, with the fingerprinting and window rules unchanged (inferred).

Changes when: users are distant or origin load justifies a CDN (threshold inferred); record it as an ADR.
`PIG-WEB-TRANSVERSE.TOPOLOGY.4`

## Evolution Defaults
<!-- Lines 268-300 -->

Several backends may share the database; each backend is one deployable. It is modular by business concept with automatically checked boundaries, and every significant decision is an ADR. The team's Python backend is one deployable over the shared database, with the schema and function API as the database owner's codebase. Refines [Deliberate Evolution](philosophy.md#deliberate-evolution). `PIG-WEB-TRANSVERSE.EVOLUTION`

### Deployables

- Several backends sharing the database do not by themselves license splitting the team's backend.
- No [BFF](glossary.md#bff) deployable (the backend is the browser's BFF; the agent surface is another client of the same core), no micro frontends (server-side composition if teams multiply), no request-time JavaScript server.
- Likely future services get their own domain schema now, not their own database (inferred).
- Replacement happens at seams. Consolidation is legitimate when operating cost grows with the number of services.

Changes when: a named force requires it (independent scaling that process types of one deployable cannot give, independent release by separate teams, fault isolation that matters, or a different runtime need) on a proven boundary, with the distribution premium budgeted and the force stated in the ADR. The new deployable reaches data through the function API with its own role, never holds a second system of record, and moves no data (inferred).
`PIG-WEB-TRANSVERSE.EVOLUTION.1`

### Modular Monolith

- Cut the backend by business concept (orders, billing), each module with a public interface aligned with a domain schema (inferred).
- A module never reads or writes another domain's tables directly. The function API is reachable from every module within its role's grants (inferred).
- One business operation is one database function call in its own transaction. A cross-domain operation (an order that also creates an invoice) is one database function, called by the module that owns the workflow, owned by the team that owns the workflow and reviewed by the database owner role ([Team-Shaped Structure](philosophy.md#team-shaped-structure)).
- The Python module holds workflow and product policy, with only tested copies of per-user write rules; never a second path to another domain's data.
- Boundaries are checked in the pipeline as a fitness function that fails on a direct access to another domain's tables. Gap: the tool is not chosen.

Principle: [Declared Layering](../software_development_guidelines/construction.md#declared-layering), [Cut by Business Concept or by Layer](../software_development_guidelines/construction.md#cut-by-business-concept-or-by-layer).
`PIG-WEB-TRANSVERSE.EVOLUTION.2`

### Decision Records

- One ADR per architecturally significant decision: one to two pages, numbered Markdown, in the repository it governs. Decisions binding every consumer of the shared database live with the database's codebase.
- Fields: context with forces, decision, status, consequences, alternatives with pros and cons, confidence, and the condition that would reverse it.
- An accepted ADR is not rewritten to change its decision: a changed decision is a new ADR that supersedes it; the old one stays in place marked superseded, with a link to its successor. Only corrections that do not change the decision (a typo, a broken link) edit an accepted ADR.
- Decisions the guideline leaves to each project, one ADR each: interface description origin direction; [row-level security](glossary.md#row-level-security) under its three conditions; ASVS level and its outcome measures; secret delivery, each environment variable used for a secret included; process replication; CDN; HSTS preload; adding a managed secret store; the build level, Build L2 or L3 by risk; every move of a Postgres-first role past its measured limit, with what it replaces and who retires it; every split of a deployable, with its named force.

Principle: [Form and Storage](../software_development_guidelines/evolution.md#form-and-storage), [Changing an Accepted Record](../software_development_guidelines/evolution.md#changing-an-accepted-record).
`PIG-WEB-TRANSVERSE.EVOLUTION.3`
