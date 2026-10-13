## L1 headline

- Links created: 86 inter links of shape `refines`, role `linker`, all from a web node to a node of `software-development-philosophy`: 51 in `web_app_philosophy.ig.yaml` (from 25 web nodes), 35 in `web_defaults.ig.yaml` (from 21 PIG-WEB nodes). The manifest `intent_graphs/intent_resources.yaml` now lists `software-development-philosophy` in `product`.
- Markdown: 46 "Principle:" pointers added, one per section whose node got a link (philosophy.md 16, allocation.md 10, stack_defaults_transverse.md 10, stack_defaults_logic.md 5, stack_defaults_data.md 4, stack_defaults_logic_security.md 1); README "Related Guidelines" now lists the software and JavaScript guidelines and the manifest row names the software graph; CLAUDE.md gained one pointer line. No web content removed (graph diff: 0 deleted lines).
- Checks: `ig-tool validate -g <graph> -m intent_graphs/intent_resources.yaml` gives 0 errors, 0 warnings, 0 issues on both graphs (philosophy: 80 nodes, 66 inter links; defaults: 132 nodes, 167 inter links). Relative link and anchor check over the 11 web markdown files: 626 links, 0 broken. Every edited file is at most 500 lines (longest: allocation.md, 489); `md-structure-sync --max-level 2` run on the 7 files that carry a TOC.
- Contradictions and tensions found, none changed on either side: 12 between decisions (K1 to K5 are direct conflicts of a web default with a software decision, K6 to K12 are narrower or stricter web positions), 3 scope overlaps where a web node defers a topic the software guideline now owns (S1 to S3), 1 gap (G1, no rollback rule on the web side).

## L2 claims

Link groups (web node, software targets):

- `TRANSVERSE.SECURITY` refines `TRANSVERSE.SECURITY.3`, `ASSURANCE.SECURITY.1`, `TRANSVERSE.PRIVACY.1`
- `TRANSVERSE.PERFORMANCE` refines `ASSURANCE.PERFORMANCE`
- `TRANSVERSE.CONTRACTS` refines `ASSURANCE.CONTRACTS.1`, `ASSURANCE.CONTRACTS.2`, `CONSTRUCTION.BOUNDARY.3`, `EVOLUTION.INCREMENTAL.2`
- `ALLOCATION.RECORD.3` refines `ASSURANCE.CONTRACTS.3`
- `ALLOCATION.RULES.1` refines `CONSTRUCTION.STATE.1`
- `ALLOCATION.RULES.3` refines `CONSTRUCTION.BOUNDARY.1`
- `ALLOCATION.GUARD.1` refines `CONSTRUCTION.BOUNDARY.2`
- `ALLOCATION.GUARD.2` refines `ASSURANCE.DATA_INTEGRITY.1`
- `ALLOCATION.ACT.4` refines `TRANSVERSE.SECURITY_MONITORING.5`
- `ALLOCATION.DERIVE.1` refines `ASSURANCE.DATA_INTEGRITY.4`
- `ALLOCATION.DERIVE.3` refines `CONSTRUCTION.STATE.3`
- `ALLOCATION.RECORD.2` refines `CONSTRUCTION.HIDING.4`, `CONSTRUCTION.BOUNDARY.4`
- `DATA.MAINTAIN` refines `CHANGE_FLOW.DATA_CHANGE`, `EVOLUTION.INCREMENTAL.6`, `ASSURANCE.AVAILABILITY.4`
- `LOGIC.PROCESS` refines `CONSTRUCTION.PROCESS.3`, `CONSTRUCTION.PROCESS.1`
- `LOGIC.ENFORCE` refines `CONSTRUCTION.HIDING.3`
- `LOGIC.EXPOSE` refines `CONSTRUCTION.BOUNDARY.5`
- `INTERACTION.ENVIRONMENT.3` refines `CHANGE_FLOW.ROLLBACK.2`
- `TRANSVERSE.OPERABILITY.1` refines `OPERATION.TELEMETRY.4`, `TRANSVERSE.SECURITY_MONITORING.1`, `TRANSVERSE.SECURITY_MONITORING.3`, `TRANSVERSE.PRIVACY.2`
- `TRANSVERSE.OPERABILITY.2` refines `ASSURANCE.BEHAVIOUR.3`, `ASSURANCE.BEHAVIOUR.7`, `CONSTRUCTION.PARADIGM.2`
- `TRANSVERSE.OPERABILITY.3` refines `CHANGE_FLOW.BUILD.2`, `TRANSVERSE.CONFIG.1`, `CHANGE_FLOW.DEPLOY.3`, `CHANGE_FLOW.DATA_CHANGE.3`, `CHANGE_FLOW.RELEASE.1`
- `TRANSVERSE.EVOLUTION.1` refines `EVOLUTION.DECISIONS.1`, `CONSTRUCTION.DESIGN.2`
- `TRANSVERSE.EVOLUTION.2` refines `EVOLUTION.INCREMENTAL.1`, `EVOLUTION.DEBT.2`, `CONSTRUCTION.DESIGN.4`, `ASSURANCE.RULES.3`, `EVOLUTION.INCREMENTAL.3`
- `TRANSVERSE.EVOLUTION.3` refines `CONSTRUCTION.SYSTEM_SHAPE.1`, `CONSTRUCTION.SYSTEM_SHAPE.2`, `CONSTRUCTION.SYSTEM_SHAPE.3`
- `TRANSVERSE.EVOLUTION.4` refines `EVOLUTION.TECHNOLOGY.1`
- `TRANSVERSE.EVOLUTION.5` refines `CONSTRUCTION.SYSTEM_SHAPE.4`, `CONSTRUCTION.HIDING.4`
- `PIG-WEB-TRANSVERSE.SECURITY.1` refines `TRANSVERSE.SECURITY.1`
- `PIG-WEB-TRANSVERSE.SECURITY.4` refines `TRANSVERSE.CONFIG.4`, `TRANSVERSE.CONFIG.2`
- `PIG-WEB-TRANSVERSE.SECURITY.5` refines `OWNERSHIP.LIFECYCLE.1`, `OWNERSHIP.LIFECYCLE.4`, `OWNERSHIP.LIFECYCLE.5`, `ASSURANCE.ARTIFACT.1`
- `PIG-WEB-TRANSVERSE.OPERABILITY.1` refines `OPERATION.TELEMETRY.3`, `OPERATION.TELEMETRY.5`
- `PIG-WEB-TRANSVERSE.OPERABILITY.2` refines `OPERATION.TELEMETRY.7`
- `PIG-WEB-TRANSVERSE.OPERABILITY.3` refines `OPERATION.TELEMETRY.1`, `OPERATION.ALERTING.1`, `OPERATION.RELIABILITY.1`
- `PIG-WEB-TRANSVERSE.OPERABILITY.4` refines `TRANSVERSE.SECURITY_MONITORING.2`
- `PIG-WEB-TRANSVERSE.OPERABILITY.6` refines `TRANSVERSE.CONFIG.3`, `CHANGE_FLOW.RELEASE.3`, `CHANGE_FLOW.RELEASE.4`
- `PIG-WEB-TRANSVERSE.EVOLUTION.2` refines `CONSTRUCTION.DEPENDENCY_DIRECTION.2`, `CONSTRUCTION.HIDING.2`
- `PIG-WEB-TRANSVERSE.EVOLUTION.3` refines `EVOLUTION.DECISIONS.3`, `EVOLUTION.DECISIONS.4`
- `PIG-WEB-ALLOCATION.POSTGRES_FIRST` refines `EVOLUTION.TECHNOLOGY.4`
- `PIG-WEB-DATA.MAINTAIN.1` refines `CHANGE_FLOW.DATA_CHANGE.5`, `CHANGE_FLOW.DATA_CHANGE.6`
- `PIG-WEB-DATA.MAINTAIN.2` refines `ASSURANCE.DATA_INTEGRITY.3`
- `PIG-WEB-DATA.MAINTAIN.4` refines `CHANGE_FLOW.DATA_CHANGE.8`
- `PIG-WEB-DATA.MAINTAIN.5` refines `OPERATION.RECOVERY.2`, `OPERATION.RECOVERY.3`
- `PIG-WEB-LOGIC.PROCESS.1` refines `OPERATION.TELEMETRY.8`
- `PIG-WEB-LOGIC.PROCESS.3` refines `ASSURANCE.AVAILABILITY.2`
- `PIG-WEB-LOGIC.EXPOSE.2` refines `CONSTRUCTION.BOUNDARY.6`
- `PIG-WEB-LOGIC.EXPOSE.7` refines `EVOLUTION.DECOMMISSION.3`, `EVOLUTION.DECOMMISSION.4`
- `PIG-WEB-LOGIC.SECURE.7` refines `CONSTRUCTION.DATA_NOT_CODE.3`
- `PIG-WEB-LOGIC.ENFORCE.5` refines `OWNERSHIP.SELECTION.1`

Not linked on purpose:
- A node whose philosophy counterpart already carries the link: the PIG nodes for testing (OPERABILITY.5), contract verification and meaning (CONTRACTS.1, CONTRACTS.2), performance targets, deployables (EVOLUTION.1), and the data-tier realizations of ALLOCATION.GUARD.2 and RECORD.2 (DATA.GUARD.*, DATA.INTERFACE.*).
- PIG-WEB-TRANSVERSE.OPERABILITY.7 (incident response), PIG-WEB-DATA.MAINTAIN.6 (personal data erasure) and PIG-WEB-DATA.MAINTAIN.7 (high availability): the web nodes record no practice (see the scope tensions below), so a `refines` link would claim a refinement that does not exist.
- Nodes with no software counterpart: browser rendering, real-time channels, collaboration, agent surface, web-specific security mechanisms (CSRF, sessions, CSP, headers).

Contradictions and tensions (web node vs software node):
- K1 reads on base tables: `ALLOCATION.RECORD.2` and `PIG-WEB-ALLOCATION.DB_API` allow simple reads on base tables under SELECT grants and forbid views as a contract object; `CONSTRUCTION.HIDING.4` says consumers never bind to base structures, and `CONSTRUCTION.BOUNDARY.4` allows a dedicated published layer in the store when direct query access is needed.
- K2 default deletion: web maintainer decision 4 (`PIG-WEB-DATA.MAINTAIN.2`) defaults to soft delete with `deleted_at`; `ASSURANCE.DATA_INTEGRITY.3` keeps a deleted flag only where undelete is a user-facing feature and otherwise deletes and archives in the same transaction.
- K3 secret delivery: `PIG-WEB-TRANSVERSE.SECURITY.4` offers a file or an environment variable as equal channels, and a file outside source control until a store is added; `TRANSVERSE.CONFIG.2` and `CONFIG.4` make the managed store primary and the environment variable an exception whose reason is recorded.
- K4 provenance level: `PIG-WEB-TRANSVERSE.SECURITY.5` defaults to SLSA Build L3; `ASSURANCE.ARTIFACT.1` raises to hardened isolated builds only where insider or credential-compromise risk matters or the software is distributed.
- K5 fetch of client-named URLs: `PIG-WEB-LOGIC.SECURE.7` refuses private, loopback and link-local ranges (open to every other host); `CONSTRUCTION.DATA_NOT_CODE.3` matches the host against an allowlist and validates the resolved address against permitted networks.
- K6 backup independence and objectives: `PIG-WEB-DATA.MAINTAIN.5` puts the archive on another host, makes point-in-time recovery the default for every database and rehearses restores on a schedule; `OPERATION.RECOVERY.3` needs a copy out of reach of production credentials, `RECOVERY.1` and `RECOVERY.4` set the strategy from recovery objectives per workload, `AVAILABILITY.4` tests restores automatically against fixed criteria.
- K7 circuit breaker: `PIG-WEB-LOGIC.PROCESS.3` puts a breaker on every external dependency called from the request path; `ASSURANCE.AVAILABILITY.2` adds one only where a dependency fails slowly or is shared by many callers.
- K8 JSON versioning: `PIG-WEB-LOGIC.EXPOSE.7` serves JSON under `/v1` from the start; `ASSURANCE.CONTRACTS.1` and `CHANGE_FLOW.RELEASE.2` tie explicit versions to many, external or independently released consumers.
- K9 reasons to split a deployable: `TRANSVERSE.EVOLUTION.3` names independent releases by a team (PIG: size, complexity or number of teams); `CONSTRUCTION.SYSTEM_SHAPE.1` also names independent scaling, fault isolation and a different runtime need.
- K10 new technology: `TRANSVERSE.EVOLUTION.4` admits one past a measured limit with budgeted cost; `EVOLUTION.TECHNOLOGY.1` adds it as a replacement with the retirement of the older one planned and owned.
- K11 ADR edits: `PIG-WEB-TRANSVERSE.EVOLUTION.3` says accepted ADRs are never edited; `EVOLUTION.DECISIONS.4` allows corrections that do not change the decision.
- K12 ASVS level: `PIG-WEB-TRANSVERSE.SECURITY.1` fixes a level default; `TRANSVERSE.SECURITY.2` says a level measures coverage and must be paired with outcome measures, which the web node does not state.
- S1 incident response: `PIG-WEB-TRANSVERSE.OPERABILITY.7` records it as out of scope; `OPERATION.INCIDENTS` (and `OPERATION.READINESS`, `RUNBOOKS`) now own it.
- S2 personal data erasure: `PIG-WEB-DATA.MAINTAIN.6` defers it; `TRANSVERSE.PRIVACY.3` owns the principle.
- S3 high availability: `PIG-WEB-DATA.MAINTAIN.7` defers it; `OPERATION.RECOVERY.4` and `ASSURANCE.AVAILABILITY.1` own the principle.
- G1 rollback: no web node states a release rollback or fix-forward rule or a per-change undo for a data change; `CHANGE_FLOW.ROLLBACK.1` to `.3` require one decided before a change ships (searched both web graphs).

## L3 full

### Links (web node, software node, intent)

#### In `web_app_philosophy.ig.yaml` (graph id `web-app-philosophy`)

- `TRANSVERSE.SECURITY` to `TRANSVERSE.SECURITY.3`: Threat models are kept per critical flow and trust boundary of a web application (authentication, access control, business operations, agent access) and revisited when a placement on the flow changes; each threat category also names an owning tier the requester cannot modify.
- `TRANSVERSE.SECURITY` to `ASSURANCE.SECURITY.1`: Each security property is stated as a verifiable requirement with a traceable id at a level chosen by risk, and insecure design is answered with misuse-case tests per tier; the threat list is an awareness map, never the requirement set.
- `TRANSVERSE.SECURITY` to `TRANSVERSE.PRIVACY.1`: A web site collects only the data the user's goal needs and exposes only the minimum its purpose needs; web adds that this holds for every page, API and trace header.
- `TRANSVERSE.PERFORMANCE` to `ASSURANCE.PERFORMANCE`: Web performance is judged on field data of real users at the 75th percentile by device class; lab budgets gate each change but never override field data, and field metrics are joined through the correlation id to server and database time.
- `TRANSVERSE.CONTRACTS` to `ASSURANCE.CONTRACTS.1`: Contracts between tiers change by compatible additions with tolerant readers, and usage is known before anything is removed; web adds that consumers deploy separately and old clients linger, so the compatibility window is explicit.
- `TRANSVERSE.CONTRACTS` to `ASSURANCE.CONTRACTS.2`: The provider's contract is authoritative and consumer-driven contracts are tests, never the origin; web adds that consumers are several backends, consoles and scripts of one shared database.
- `TRANSVERSE.CONTRACTS` to `CONSTRUCTION.BOUNDARY.3`: Every contract between tiers or consumers states names, types, nullability, units, invariants, owner and version, readable without the producer's code.
- `TRANSVERSE.CONTRACTS` to `EVOLUTION.INCREMENTAL.2`: A breaking change takes expand, migrate, contract unless every consumer ships in the same deployment as the change; web adds that browsers and agent clients never do.
- `ALLOCATION.RECORD.3` to `ASSURANCE.CONTRACTS.3`: Every interface description consumers read (HTTP description, function API catalogue, agent tool surface) has one origin per fact with the other side generated or conformance-checked and a CI gate that fails on drift; the origin direction is recorded per project with criteria.
- `ALLOCATION.RULES.1` to `CONSTRUCTION.STATE.1`: Exactly one tier is the authority for each responsibility; every copy carries a version or timestamp that detects staleness and never decides, and a rejecting copy is generated from or tested against the authority.
- `ALLOCATION.RULES.3` to `CONSTRUCTION.BOUNDARY.1`: Deciding checks run only in the backend or the database; the browser, agent clients, model output and client-supplied hints never decide, and every submitted value is re-checked on the server.
- `ALLOCATION.GUARD.1` to `CONSTRUCTION.BOUNDARY.2`: Meaning is checked by the tier that holds the state (constraints and functions for stored rows, the backend for rules needing the end user or policy), and at the database function API the parameter types and domains are the precise types for every consumer.
- `ALLOCATION.GUARD.2` to `ASSURANCE.DATA_INTEGRITY.1`: Every rule that must hold whatever writes the data is declared in the database, CHECK constraints included; rules beyond declarative constraints run under serializable isolation with retry or after locking the governing row, and backend and browser validators are generated from or tested against the constraints.
- `ALLOCATION.ACT.4` to `TRANSVERSE.SECURITY_MONITORING.5`: Business history is written by the database in the same transaction as the change and records both the verified consumer role and the claimed actor; the security event log stays a separate record with its own store, integrity and retention.
- `ALLOCATION.DERIVE.1` to `ASSURANCE.DATA_INTEGRITY.4`: Derived data is computed where its source is, in the order compute on read, same-transaction maintenance in the database, then cache tables with a stated staleness; consumers never write derived stores beside the source.
- `ALLOCATION.DERIVE.3` to `CONSTRUCTION.STATE.3`: Every cache states its staleness bound and an expiry or invalidation plan; derived-data caches are database tables invalidated in the source transaction, HTTP responses are labelled on purpose, and a cache is never permanent storage.
- `ALLOCATION.RECORD.2` to `CONSTRUCTION.HIDING.4`: The database owner alone changes the schema, and every consumer reaches the data through the owner's published function API with its own role; simple reads may query granted base tables.
- `ALLOCATION.RECORD.2` to `CONSTRUCTION.BOUNDARY.4`: The published contract over the shared database is a function API, never views, with one business operation per call; it evolves additively and breaking changes are coordinated with every consumer.
- `DATA.MAINTAIN` to `CHANGE_FLOW.DATA_CHANGE`: Schema changes are versioned migrations applied only by automation as a step of every release, long-running data work is a human-launched script under a checklist with a ticket id, and an incompatible change goes expand, migrate, contract.
- `DATA.MAINTAIN` to `EVOLUTION.INCREMENTAL.6`: Conventions evolve forward only: new objects follow the new rule and legacy objects are not renamed in bulk.
- `DATA.MAINTAIN` to `ASSURANCE.AVAILABILITY.4`: Recovery to a chosen moment is the default for the database, and a backup counts only once a restore of it has been rehearsed.
- `LOGIC.PROCESS` to `CONSTRUCTION.PROCESS.3`: Backend processes are disposable: durable state, sessions and shared caches live in backing services and process memory caches nothing beyond one request; long-lived connections are the one tolerated per-process state.
- `LOGIC.PROCESS` to `CONSTRUCTION.PROCESS.1`: Worker processes return an unfinished job on SIGTERM, so releases and scaling lose no work.
- `LOGIC.ENFORCE` to `CONSTRUCTION.HIDING.3`: One business core per backend, separable from transport and storage: adapters hold no rule and every external system, the database function API included, is reached through a port.
- `LOGIC.EXPOSE` to `CONSTRUCTION.BOUNDARY.5`: Browsers get server-rendered hypermedia and programs and agents a resource-oriented structured interface over the same use cases, each described machine-readably and evolved additively.
- `INTERACTION.ENVIRONMENT.3` to `CHANGE_FLOW.ROLLBACK.2`: Client and server changes coexist because every client-server contract has a compatibility window at least as long as an old page can stay open; lockstep deployment is acceptable only when every consumer ships in the same deployment, which a browser tab never does.
- `TRANSVERSE.OPERABILITY.1` to `OPERATION.TELEMETRY.4`: One correlation id per user interaction runs from the browser through the backend into the database transaction and is stamped on every log record, span, client event and audit row; database consumers outside the request path carry their identity and ticket id in the session.
- `TRANSVERSE.OPERABILITY.1` to `TRANSVERSE.SECURITY_MONITORING.1`: Validation failures, authentication results, authorization failures, session failures, application errors and use of higher-risk functions go to a security event log; changes to privileges, roles, credentials and grants count as security events.
- `TRANSVERSE.OPERABILITY.1` to `TRANSVERSE.SECURITY_MONITORING.3`: Secrets, session ids, tokens and unneeded personal data are never logged or placed in trace context, trace headers included.
- `TRANSVERSE.OPERABILITY.1` to `TRANSVERSE.PRIVACY.2`: Retention is a recorded decision per record type, set by legal, regulatory and contractual obligations, no shorter and no longer.
- `TRANSVERSE.OPERABILITY.2` to `ASSURANCE.BEHAVIOUR.3`: Tests sit at the lowest level that catches the failure, ratios are not prescribed and end-to-end tests are few on critical journeys; web adds that logic placed in the database is tested on a real engine of the production kind.
- `TRANSVERSE.OPERABILITY.2` to `ASSURANCE.BEHAVIOUR.7`: Data tests are isolated by a rolled-back transaction by default, and behaviour visible only at commit or between sessions is tested with committing sessions in a disposable database, never a shared one.
- `TRANSVERSE.OPERABILITY.2` to `CONSTRUCTION.PARADIGM.2`: Logic placed in the database is tested against a real engine, never a mock or another engine, and every invariant enforced procedurally has a concurrent test in the default suite.
- `TRANSVERSE.OPERABILITY.3` to `CHANGE_FLOW.BUILD.2`: Build, release and run are separate and one immutable artifact, assets included, is built once and promoted everywhere; web adds that the database changes ship in the same pipeline.
- `TRANSVERSE.OPERABILITY.3` to `TRANSVERSE.CONFIG.1`: Configuration is kept apart from code and secrets out of source, so one build serves every deploy.
- `TRANSVERSE.OPERABILITY.3` to `CHANGE_FLOW.DEPLOY.3`: Every environment runs the same database engine and version as production, with no adapters hiding differences.
- `TRANSVERSE.OPERABILITY.3` to `CHANGE_FLOW.DATA_CHANGE.3`: Schema and function-API changes are versioned migrations promoted through the same pipeline as application code, run once per release before the new code starts and additive across the release window.
- `TRANSVERSE.OPERABILITY.3` to `CHANGE_FLOW.RELEASE.1`: Releases are small and frequent increments.
- `TRANSVERSE.EVOLUTION.1` to `EVOLUTION.DECISIONS.1`: Each costly decision is recorded with its forces, alternatives and the condition that would reverse it; web adds the per-project decisions the guideline leaves open (interface origin direction, row-level security adoption).
- `TRANSVERSE.EVOLUTION.1` to `CONSTRUCTION.DESIGN.2`: Costly, hard-to-reverse choices are identified early and decided when enough is known, not up front for every one.
- `TRANSVERSE.EVOLUTION.2` to `EVOLUTION.INCREMENTAL.1`: The system grows in small tested increments with internal quality kept from the start and no capability built for presumed future features.
- `TRANSVERSE.EVOLUTION.2` to `EVOLUTION.DEBT.2`: Debt is taken only as prudent, deliberate and recorded, and internal quality is invested in from the start.
- `TRANSVERSE.EVOLUTION.2` to `CONSTRUCTION.DESIGN.4`: Capacity has headroom for about ten times the current load, and reaching about a hundred times is planned as a rewrite of the part concerned rather than anticipated in code.
- `TRANSVERSE.EVOLUTION.2` to `ASSURANCE.RULES.3`: Fit is made explicit as automated fitness functions, non-functional ones included, that run as gates.
- `TRANSVERSE.EVOLUTION.2` to `EVOLUTION.INCREMENTAL.3`: Replacement happens at seams behind the existing interface, never by big-bang rewrite.
- `TRANSVERSE.EVOLUTION.3` to `CONSTRUCTION.SYSTEM_SHAPE.1`: Each backend is one deployable modular by business concept and is not split into services without a measured need; web adds that several backends may share one database.
- `TRANSVERSE.EVOLUTION.3` to `CONSTRUCTION.SYSTEM_SHAPE.2`: A further deployable is split off only when the distribution premium is budgeted; web adds that a new deployable reaches data only through the function API with its own role.
- `TRANSVERSE.EVOLUTION.3` to `CONSTRUCTION.SYSTEM_SHAPE.3`: A boundary is placed only once it has proven stable; web adds that bounded contexts map to domain schemas in the shared database, so a later split moves no data.
- `TRANSVERSE.EVOLUTION.4` to `EVOLUTION.TECHNOLOGY.1`: Few mature technologies are adopted, and a new one enters only when an existing one's measured limit is reached and its perpetual operating cost is budgeted; runtimes, stores, services and frameworks are counted.
- `TRANSVERSE.EVOLUTION.5` to `CONSTRUCTION.SYSTEM_SHAPE.4`: Teams are cross-functional around a capability and system structure is cut together with team structure; web adds the database owner as a named role inside the team and a domain schema, functions and backend per capability team.
- `TRANSVERSE.EVOLUTION.5` to `CONSTRUCTION.HIDING.4`: When teams multiply each capability team owns its domain schema, and one named owner role holds what spans schemas; cross-domain operations are composed inside the database by published functions, never by direct access to another domain's tables.

#### In `web_defaults.ig.yaml` (graph id `pig-web-defaults`)

- `PIG-WEB-TRANSVERSE.SECURITY.1` to `TRANSVERSE.SECURITY.1`: The requirements standard is ASVS 5.0, cited by versioned id, at a level recorded per project by risk (Level 2 by default, Level 3 for critical data, never Level 1).
- `PIG-WEB-TRANSVERSE.SECURITY.4` to `TRANSVERSE.CONFIG.4`: One managed store holds every secret, with least privilege per service and per database consumer role, automated rotation and audited access; each backend, the reporting role, the operator role and the owner role of the shared database has its own credentials.
- `PIG-WEB-TRANSVERSE.SECURITY.4` to `TRANSVERSE.CONFIG.2`: A secret reaches the process at start as a file readable only by the service account or as an environment variable that no other process can read and the framework never dumps.
- `PIG-WEB-TRANSVERSE.SECURITY.5` to `OWNERSHIP.LIFECYCLE.1`: Python dependencies come from a lockfile with hashes installed with --require-hashes over the whole tree, JavaScript build dependencies from a lockfile installed exactly, and container base images are pinned.
- `PIG-WEB-TRANSVERSE.SECURITY.5` to `OWNERSHIP.LIFECYCLE.4`: Components come from official sources; Postgres packages and database extensions are taken from official sources at a pinned version.
- `PIG-WEB-TRANSVERSE.SECURITY.5` to `OWNERSHIP.LIFECYCLE.5`: An SBOM is produced per release artifact and scanned continuously, not only at build, and updates go through the staged pipeline and a staged or canary rollout.
- `PIG-WEB-TRANSVERSE.SECURITY.5` to `ASSURANCE.ARTIFACT.1`: Signed provenance at SLSA Build L3 is verified before deploy; Build L2 is acceptable only when the build platform cannot isolate runs or keep the signing key from the build steps.
- `PIG-WEB-TRANSVERSE.OPERABILITY.1` to `OPERATION.TELEMETRY.3`: Instrumentation is library instrumentation for the framework, HTTP clients and the Postgres driver with code spans only around business steps, and logs are one JSON event per line on stdout, unbuffered, with trace and span id.
- `PIG-WEB-TRANSVERSE.OPERABILITY.1` to `OPERATION.TELEMETRY.5`: Every trace is kept while volume allows, then tail sampling keeps every error and slow trace; an incoming traceparent from an unauthenticated or external caller is recorded but does not decide sampling.
- `PIG-WEB-TRANSVERSE.OPERABILITY.2` to `OPERATION.TELEMETRY.7`: Real-user measurement is browser errors, field vitals segmented by device class and Reporting API reports, sent with sendBeacon on visibilitychange and stamped with release and trace id; the collection endpoint treats every event as untrusted input and collects no personal data.
- `PIG-WEB-TRANSVERSE.OPERABILITY.3` to `OPERATION.TELEMETRY.1`: Latency, traffic, errors and saturation are monitored per process type (web, worker) and for Postgres as histograms, with pg_stat_statements on from the first deploy and black-box probes of the critical journeys.
- `PIG-WEB-TRANSVERSE.OPERABILITY.3` to `OPERATION.ALERTING.1`: Pages go to a human only on urgent, user-visible conditions and everything else is a ticket.
- `PIG-WEB-TRANSVERSE.OPERABILITY.3` to `OPERATION.RELIABILITY.1`: Indicators are the page targets at the 75th percentile plus availability and server latency of the critical journeys, with objectives set from what users need.
- `PIG-WEB-TRANSVERSE.OPERABILITY.4` to `TRANSVERSE.SECURITY_MONITORING.2`: Security events use one vocabulary over secure transport to a central collector outside the application database, copied to read-only storage with every access recorded; refusals made inside database functions reach it through the backend log and the shipped Postgres log.
- `PIG-WEB-TRANSVERSE.OPERABILITY.6` to `TRANSVERSE.CONFIG.3`: Settings load once into one typed, validated object; behaviour config is versioned and promoted with the release and deploy-specific values are independent variables per deploy.
- `PIG-WEB-TRANSVERSE.OPERABILITY.6` to `CHANGE_FLOW.RELEASE.3`: Release toggles are short-lived and each has a removal task created with it.
- `PIG-WEB-TRANSVERSE.OPERABILITY.6` to `CHANGE_FLOW.RELEASE.4`: The staged pipeline runs lint, unit tests, the interface drift gate and the catalogue diff first, then integration on real Postgres and the consumer suites, then the few end-to-end tests; the shared database's migrations are released before any consumer that depends on them.
- `PIG-WEB-TRANSVERSE.EVOLUTION.2` to `CONSTRUCTION.DEPENDENCY_DIRECTION.2`: Module boundaries are checked automatically in the pipeline as a fitness function that fails on a direct read or write of another domain's tables; the tool is open.
- `PIG-WEB-TRANSVERSE.EVOLUTION.2` to `CONSTRUCTION.HIDING.2`: The Python backend is cut by business concept, each module with a public interface, while a business operation lives in its database function and the module holds workflow and product policy.
- `PIG-WEB-TRANSVERSE.EVOLUTION.3` to `EVOLUTION.DECISIONS.3`: Each decision is a short, numbered Markdown ADR in the repository it governs, one to two pages; decisions binding every consumer of the shared database live with the database's codebase.
- `PIG-WEB-TRANSVERSE.EVOLUTION.3` to `EVOLUTION.DECISIONS.4`: Accepted ADRs are never edited, only superseded.
- `PIG-WEB-ALLOCATION.POSTGRES_FIRST` to `EVOLUTION.TECHNOLOGY.4`: One Postgres carries the job queue, schedules, derived caches, sessions and documents until a measured limit for that role, each role naming its trigger to leave Postgres; NOTIFY is a low-rate wake-up, never the message carrier.
- `PIG-WEB-DATA.MAINTAIN.1` to `CHANGE_FLOW.DATA_CHANGE.5`: Postgres online-safe forms: a short lock_timeout with retry on every DDL, constraints NOT VALID then VALIDATE, indexes built concurrently, and a column default added only when non-volatile.
- `PIG-WEB-DATA.MAINTAIN.1` to `CHANGE_FLOW.DATA_CHANGE.6`: A backfill is a separate, batched data step outside the schema migration's transaction and beyond a threshold a human-run job.
- `PIG-WEB-DATA.MAINTAIN.2` to `ASSURANCE.DATA_INTEGRITY.3`: Deletion is a per-table choice weighed on importance, reconstructability, change rate and business value, always through functions of a narrow non-login deletion role; the default is basic soft delete with deleted_at and hard delete with a same-transaction archive where consumers must be unable to reach history.
- `PIG-WEB-DATA.MAINTAIN.4` to `CHANGE_FLOW.DATA_CHANGE.8`: Large data changes are batched idempotent jobs run by a human after a checklist as the owner role with the operator and a ticket id as actor, each batch its own Serializable transaction, done only when a convergence query reaches zero, with a stop plan.
- `PIG-WEB-DATA.MAINTAIN.5` to `OPERATION.RECOVERY.2`: Point-in-time recovery by default: base backups plus continuous WAL archiving to a repository on another host with retention and tracked chains; logical dumps serve portability only, fsync is never off and synchronous_commit is relaxed only for data that may be lost on a crash.
- `PIG-WEB-DATA.MAINTAIN.5` to `OPERATION.RECOVERY.3`: The WAL and base-backup repository lies on another host; restores are rehearsed on a schedule.
- `PIG-WEB-LOGIC.PROCESS.1` to `OPERATION.TELEMETRY.8`: Jobs and schedules are monitored on failures, duration, missed runs (no run within twice the interval) and backlog age.
- `PIG-WEB-LOGIC.PROCESS.3` to `ASSURANCE.AVAILABILITY.2`: Every outbound call has a timeout shorter than its caller's remaining deadline, retries run at exactly one layer (at most three attempts and a 10% retry budget per client in the request path) only for idempotent or keyed calls, and a circuit breaker guards each external dependency called from the request path.
- `PIG-WEB-LOGIC.EXPOSE.2` to `CONSTRUCTION.BOUNDARY.6`: Every JSON error is application/problem+json with a stable type URI and the matching status, each named constraint and stable function error code maps to one problem type, and detail helps the caller correct the request without exposing internals.
- `PIG-WEB-LOGIC.EXPOSE.7` to `EVOLUTION.DECOMMISSION.3`: An unavoidable break ships as /v2 beside /v1, the old one announced with Deprecation and Sunset headers, a documentation link and the OpenAPI deprecated flag.
- `PIG-WEB-LOGIC.EXPOSE.7` to `EVOLUTION.DECOMMISSION.4`: Both versions are served through a published window at least as long as a page can live with a valid session (the absolute session timeout).
- `PIG-WEB-LOGIC.SECURE.7` to `CONSTRUCTION.DATA_NOT_CODE.3`: Every server-side fetch of a client- or agent-named URL goes through one helper that refuses private, loopback and link-local addresses, checks the address actually connected to and validates every redirect hop; an egress proxy or outbound rules back it where the hosting can enforce them.
- `PIG-WEB-LOGIC.ENFORCE.5` to `OWNERSHIP.SELECTION.1`: Django is the default backend framework, recorded as a decision with criteria taken from settled decisions (server-held revocable sessions, built-in CSRF protection, server-rendered forms, synchronous handlers, password hashing); FastAPI wins when the backend serves only programs and agents.
### Contradictions and tensions in full

K1. Reads on base tables, and views as a contract.
- Web: `ALLOCATION.RECORD.2` (and `PIG-WEB-ALLOCATION.DB_API`, maintainer decision 5): every consumer reaches the data through the function API owned by the database owner, with one role each; writes go through functions, but simple reads may query base tables under SELECT grants; views are never a contract object. Mitigation on the web side: `PIG-WEB-TRANSVERSE.CONTRACTS.1` extends the catalogue diff to every object granted to a consumer role, so a removed or retyped granted column fails the gate.
- Software: `CONSTRUCTION.HIDING.4`: other parties reach the data through an interface the owner publishes, never by binding to the base structures; a store shared through its base structures is not an integration mechanism. `CONSTRUCTION.BOUNDARY.4`: when several consumers need the data, an application interface by default, or a dedicated published layer in the store where consumers need direct query access or privileges must be separated in the store itself.
- Tension: the web allows a granted-table read path the software calls unpublished structure, and the web forbids the published layer in the store (views) that the software accepts where direct query access is needed (reporting reads in the web default context).

K2. Default form of deletion.
- Web: maintainer decision 4, `PIG-WEB-DATA.MAINTAIN.2`: deletion is a per-table choice; the default is basic soft delete (`deleted_at`, no change to the primary key, every consumer excludes deleted rows); hard delete with a same-transaction archive is the case for some caches and for data consumers must be unable to reach.
- Software: `ASSURANCE.DATA_INTEGRITY.3`: where recovery or audit of deleted records is needed the row is deleted and archived in the same transaction; a deleted flag is kept only when undelete is a user-facing feature whose costs are paid.
- Tension: opposite defaults. The web default keeps deleted rows in the live table for every consumer to filter; the software default archives, and keeps the flag only for a user-facing undelete.

K3. Delivery channel of secrets.
- Web: `PIG-WEB-TRANSVERSE.SECURITY.4`: the secret reaches the process at start by a file readable only by the service account or by an environment variable that no other process can read and the framework never dumps; on self-managed hosts without an orchestrator, until a managed store is added, a file outside source control is in force (maintainer decision 6).
- Software: `TRANSVERSE.CONFIG.2`: secrets live in a managed store and reach the process by runtime injection as mounted files or through the store interface; an environment variable only where the platform offers neither or where the process environment is shown not to leak, with the channel and reason recorded. `TRANSVERSE.CONFIG.4`: secrets are centralized in one managed solution.
- Tension: the web treats file and environment variable as equal channels and accepts a file-only interim without a store; the software ranks the store first and the environment variable as a recorded exception.

K4. Default level of build provenance.
- Web: `PIG-WEB-TRANSVERSE.SECURITY.5`: signed provenance at SLSA Build L3 verified before deploy, by default; L2 acceptable only when the build platform cannot isolate runs or keep the signing key from the build steps.
- Software: `ASSURANCE.ARTIFACT.1`: signed provenance from a hosted build platform, verified before use; hardened, isolated builds only where insider or credential-compromise risk matters or the software is distributed to others; reproducible builds only at the highest assurance.
- Tension: the web fixes the higher level as the default for the default context; the software makes the level depend on the stated risk.

K5. Server-side fetch of client-named URLs.
- Web: `PIG-WEB-LOGIC.SECURE.7`: one fetch helper refuses private, loopback and link-local addresses, checks the address actually connected to and validates each redirect hop; a network guard (egress proxy) is preferred and required only when the server's network holds internal services or a token-less metadata endpoint.
- Software: `CONSTRUCTION.DATA_NOT_CODE.3`: a server fetches only destinations it allows: the host is matched against an allowlist, the resolved addresses are validated against the permitted networks, the connection goes only to the validated address, and redirect targets are re-checked.
- Tension: the web excludes a set of ranges and allows every other host; the software admits only an allowlisted set of hosts. Both validate the connected address and every redirect.

K6. Backup independence, default recovery tier and restore proof.
- Web: `PIG-WEB-DATA.MAINTAIN.5`: point-in-time recovery by default (base backups plus continuous WAL archiving to a repository on another host); restores rehearsed on a schedule.
- Software: `OPERATION.RECOVERY.3`: at least one copy outside the failure and attack domain of production, an attacker holding production credentials in the threat model, no single credential able to delete every copy; `OPERATION.RECOVERY.1` and `.4`: recovery objectives per workload and a strategy never stricter than needed; `ASSURANCE.AVAILABILITY.4`: restores tested end to end, regularly and automatically, against criteria fixed beforehand.
- Tension: "another host" does not state credential independence or immutability; the PITR default is not derived from per-workload objectives; "rehearsed on a schedule" does not state automation or fixed criteria.

K7. Circuit breaker.
- Web: `PIG-WEB-LOGIC.PROCESS.3`: a circuit breaker per external dependency called from the request path.
- Software: `ASSURANCE.AVAILABILITY.2`: a breaker (state changes logged) only where a dependency fails slowly or is shared by many callers.
- Tension: unconditional versus conditional. Timeouts, single-layer retries and idempotency rules agree.

K8. Version in the JSON path from the start.
- Web: `PIG-WEB-LOGIC.EXPOSE.7`: JSON served under `/v1` from the start, no minor version, `/v2` beside `/v1` for an unavoidable break; unversioned JSON paths are forbidden until the first break.
- Software: `ASSURANCE.CONTRACTS.1`: for few, in-house, reachable consumers, additive change and a coordinated deploy without version numbers; explicit versioning with a deprecation window for many, external or independently released consumers; `CHANGE_FLOW.RELEASE.2`: a compatibility-promising scheme only for an artifact with a declared public interface consumed by others.
- Tension: the web fixes versioning for the default context (browser code that lingers in open tabs, agent clients); the software ties it to consumer reach. Compatible if the lingering clients count as independently released consumers; the web node does not say so.

K9. Reasons to split a deployable.
- Web: `TRANSVERSE.EVOLUTION.3`: split only when a team needs independent releases, the boundary has proven stable and the distribution premium is budgeted (`PIG-WEB-TRANSVERSE.EVOLUTION.1`: when size, complexity or the number of teams make the single unit the bottleneck).
- Software: `CONSTRUCTION.SYSTEM_SHAPE.1`: a named force: independent scaling, independent release by separate teams, fault isolation that matters, or a different runtime need.
- Tension: the web list is narrower (no scaling, fault isolation or runtime need) and the PIG wording differs from the philosophy wording.

K10. Admission of a new technology.
- Web: `TRANSVERSE.EVOLUTION.4`: a new technology enters only when an existing one's measured limit is reached and its perpetual operating cost is budgeted.
- Software: `EVOLUTION.TECHNOLOGY.1`: a new technology is introduced as a replacement, with the retirement of the older one planned and owned (a few independent components excepted, `TECHNOLOGY.3`); `TECHNOLOGY.4` agrees with the measured-limit condition for a second store.
- Tension: the web states no retirement of what the new technology replaces, and keeps no register of positions (`TECHNOLOGY.2`).

K11. Editing an accepted decision record.
- Web: `PIG-WEB-TRANSVERSE.EVOLUTION.3`: accepted ADRs are never edited, only superseded.
- Software: `EVOLUTION.DECISIONS.4`: not rewritten, but corrections that do not change the decision (a typo, a broken link) edit an accepted record.
- Tension: absolute versus with a stated exception; marginal.

K12. Meaning of an ASVS level.
- Web: `PIG-WEB-TRANSVERSE.SECURITY.1`: ASVS 5.0 at a level recorded per project by risk (Level 2 by default, Level 3 for critical data, never Level 1), requirements cited by id.
- Software: `TRANSVERSE.SECURITY.2`: a maturity score or requirement level measures activity and coverage, not security outcomes, so it is paired with outcome measures and never reported as proof that the system is safer.
- Tension: the web node states no outcome measure beside the level.

S1. Incident response: `PIG-WEB-TRANSVERSE.OPERABILITY.7` records it as out of scope and decides no practice; the software guideline decides it in `OPERATION.INCIDENTS`, `OPERATION.READINESS` and `OPERATION.RUNBOOKS`. Not linked; the web statement is now outdated for readers of both guidelines.

S2. Personal data erasure: `PIG-WEB-DATA.MAINTAIN.6` is deferred; `TRANSVERSE.PRIVACY.3` owns the principle (deletion decided per entity, an inventory of copies, erased data in a backup put beyond use). Interacts with K2. Not linked.

S3. High availability and replication: `PIG-WEB-DATA.MAINTAIN.7` is deferred; `OPERATION.RECOVERY.4` and `ASSURANCE.AVAILABILITY.1` own the principle. Not linked.

G1. Rollback: no web node states how a bad release is detected and reversed, nor a per-change undo for a data change (both web graphs searched for rollback, roll back, undo, fix forward, reverse: only the rollback of test transactions and of expand-phase steps appear). The software guideline requires the decision before a change ships (`CHANGE_FLOW.ROLLBACK.1` to `.3`). The link `INTERACTION.ENVIRONMENT.3` to `CHANGE_FLOW.ROLLBACK.2` covers only backward compatibility with old clients.

### Method notes

- Link placement: each link sits at the highest web node that fits; where a web node and its philosophy counterpart both state the principle, the link is on the philosophy node (for example `TRANSVERSE.OPERABILITY.3` carries the build-once and configuration links, so `PIG-WEB-TRANSVERSE.OPERABILITY.6` links only the toggle, pipeline-stage and configuration-shape nodes it adds). Where several web nodes touch one software node, the link is on the node that owns the web decision (`ALLOCATION.RECORD.3` for one source of description, `TRANSVERSE.CONTRACTS` for compatibility and contract tests).
- Software nodes were read at intent level (constraints are one-line), and the grounds of every pair compared were read from the graph nodes, never from the whole graph file.
- Graph edits used `ig-tool link create` one link at a time with qualified uids; the manifest edit was the only other graph-side change.
