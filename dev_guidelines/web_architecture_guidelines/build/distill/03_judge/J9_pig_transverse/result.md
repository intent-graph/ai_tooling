# Result: J9 pig-web-defaults TRANSVERSE judged

## L1 headline

The 27 judged nodes of PIG-WEB.TRANSVERSE are decided under the max rule, and the adversarial review of the branch is applied: 12 of its 14 findings touch this unit, all applied, none rejected; the blocking one (the module rule) now lets every module call the function API and composes cross-domain operations in the database. One deferred node (incident response) is not judged. The nodes are the JavaScript + Python + Postgres realization of the philosophy's TRANSVERSE verdicts and of the process model, under the maintainer's default context: a database shared by several backends and by BI, consoles and scripts (MD-03). In one line each:
- **Security**: ASVS 5.0 at a recorded level, Level 2 by default (grounded). TLS at the proxy with HSTS on the application's host; preload only as a recorded decision. A strict nonce CSP from the Python templates. Secrets in a managed store per consumer role, a file fallback until one is added. Hash-pinned dependencies, SBOM, signed SLSA Build L3 provenance (L2 under a stated condition).
- **Performance**: Core Web Vitals "good" thresholds at the 75th percentile are the targets; build budgets are the gate; a derived server budget of about 1 s per page (inferred).
- **Contracts**: one verification per seam. The function API gets a catalogue diff plus every consumer's suite against the candidate schema. HTTP and the agent tool surface stay in sync under the drift gate, with deprecation signals; external services get scheduled tests of their doubles. Meaning, owner and lifecycle are written with each contract.
- **Operations**: W3C trace context into the database transaction. Golden signals plus the measured triggers of the Postgres-first placements. A security log outside the application database. Tests on real Postgres, concurrency tested with committing sessions in a disposable database. Migrations released before the code that needs them.
- **Topology**: one buffering reverse proxy. WSGI sync workers; threaded workers, ASGI or a short timeout for routes with blocking external calls; ASGI for long-lived connections. A process manager per unit. Fingerprinted assets served outside Python, kept for the compatibility window.
- **Evolution**: each backend one deployable over the shared database, not split without a measured need; modular by business concept, no module touching another domain's tables; decisions in ADRs.

One question, awaiting maintainer: a context check on the hosting model, not a trade-off. No new departure from the maintainer's practice: the stack realizes the L517 narrowing counted at the function-API node. None conflicts with an allocation placement. The open read-visibility question is recorded as awaiting maintainer, with its default, not settled.

Pinned:
- Nodes judged: 27 of 28 (pig-web-defaults PIG-WEB.TRANSVERSE; 6 roll-ups judged from their children: PIG-WEB.TRANSVERSE, .SECURITY, .CONTRACTS, .OPERABILITY, .TOPOLOGY, .EVOLUTION; 1 deferred, not judged: OPERABILITY.7 Incident Response).
- Decided 27, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: SECURITY.1 and OPERABILITY.5. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1, a context check, not a trade-off, awaiting maintainer: the default context names no hosting model; TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 assume one or a few self-managed hosts without a container orchestrator and name the winner that changes when one exists. Under that assumption the managed secret store holds only once the team adds one; until then the file fallback is in force.
- Verdicts against the maintainer doctrine: 0 new; realizes the L517 narrowing (J5, J6), counted once at PIG-WEB.DATA.INTERFACE.1: "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract (CONTRACTS, OPERABILITY.6). Adopted as the max choice: L567 (never-committing boundary for shared environments), L517's coordination and "no formal version numbers" (the new function name is J5's expand step and L512's route, not L517's text), L545 (ticket id on owner-run jobs), L566 (transaction-local context, here also carrying the correlation id, inferred).
- Conflicts with J1 placements: 0. L564 (derive Postgres, Python and TypeScript types from a logical type in the contract) is rejected for stored facts because RECORD.3 and TYPE_CHAIN make the Postgres schema their origin; its logical-versus-physical split is kept as documentation. EVOLUTION.2's module rule now matches ACT.1 and MD-03: modules never reach another domain's tables; the function API, cross-domain operations included, is reachable from every module within its role's grants.
- Tensions recorded, not overridden: (a) L350, secrets in environment variables against a managed store: the store is the authority, delivery by file or environment at start; under the assumed hosting the store is a technology to add, and until then the file fallback is in force. (b) L251 with L248: behaviour config versioned, reviewed and promoted with the release; deploy-specific values per deploy from the environment. (c) L565's contract version against L517: the function API carries change in names, the HTTP description in its document version. (d) L351's 90-day minimum for secret-access logs against L048: retention set by obligations, 90 days as the floor where none exists. (e) L369: every trace kept while volume allows, then tail sampling; ratio head sampling that drops error traces rejected. (f) L147 and L148, HSTS preload: the default end state is a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS; preload only as a recorded decision when the team controls the registrable domain.
- Gaps in the evidence: (1) L304: ASVS chapter list not read; the Level 2 default is now grounded (ASVS 5.0: "most applications should be striving" for it). (2) No row on TLS for database connections of consumers across a network hop, nor on re-encryption from proxy to application server (L140 open). (3) Correlation id carried into the database transaction, inferred (from J5). (4) No ledger row on concurrency testing; the tests are required by GUARD.2 and part of the default suite, with committing sessions in a disposable database (inferred). (5) No source-stated server latency target and none for the agent surface; a derived server budget (about 1 s for the server's part of a page at the 75th percentile, well under 1 s for an interaction's request) is inferred from L295, L297, L013 and ACT.3. (6) Previous releases' fingerprinted assets kept during the compatibility window, inferred (J4 hand-off). (7) Authorization refusals decided inside database functions reaching the security event log, inferred. (8) No module-boundary tool read for Python (L123 inferred). (9) The 6 roll-ups own no row.
- Review fixes: 12 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, M5, M6, m1, m2, m3, m6, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

Files: `records.md` (one judge record per node), `questions.md` (Q1, awaiting maintainer), this file.

## L2 claims

### Review fixes

Applied from `../review_transverse/review.md` and `../cross_branch_fixes.md`; 0 rejected.
- **B1 / X3** (EVOLUTION.2, EVOLUTION roll-up): modules never reach another domain's tables; the function API is reachable from every module within its role's grants; a cross-domain operation is one database function, owned by the workflow's team (J5 EVOLUTION.5); rule `unvalidated`.
- **M1 / X2** (CONTRACTS, CONTRACTS.1, CONTRACTS.2, OPERABILITY.6; pins): pin reworded to "0 new; realizes the L517 narrowing"; one lockstep condition, word for word; new-name rule credited to J5's expand step and L512.
- **M2 / X4** (OPERABILITY.5, OPERABILITY roll-up): concurrency tests for GUARD.2 part of the default suite; gap kept only for the missing source row.
- **M3 / X5** (EVOLUTION.1, EVOLUTION roll-up, TRANSVERSE roll-up): "one Python backend deployable" replaced; a split moves no data (inferred).
- **M4** (SECURITY roll-up, SECURITY.2, SECURITY.5): the A04 transport owner and the A08 pipeline owner named.
- **M5** (SECURITY.5): signed provenance at SLSA Build L3; L2 acceptable when the build platform cannot isolate runs or keep the signing key from the build steps; gap removed.
- **M6** (SECURITY.2, EVOLUTION.3): default HSTS end state on the application's host; preload only as an ADR under its condition.
- **m1** (SECURITY.1): Level 2 default grounded in the ASVS 5.0 text.
- **m2** (PERFORMANCE): derived server budget stated `unvalidated`.
- **m3** (TOPOLOGY.2, TOPOLOGY roll-up): routes with blocking external calls get threaded workers, ASGI or a short timeout.
- **m6** (SECURITY.4, Q1): under the assumed hosting the store is to be added; the file fallback is in force until then.
- **m7 / X1** (SECURITY.1, OPERABILITY.5): one notation for the pending clause, with default, fallback and consequence.
- **X7** (CONTRACTS.1, CONTRACTS roll-up): the agent tool surface sits under the MD-02 sync gate and the compatibility window.

### Verdicts

Default context: MD-03 as restated by J1 (`../J1_allocation/allocation_matrix.md`); Python renders HTML; hosting assumed self-managed without an orchestrator (Q1). Each line gives a node's verdict and its proposed `epistemic_state`. Evidence ids resolve in `../../02_skeleton/claims_ledger.md`.

- **PIG-WEB.TRANSVERSE** (roll-up): each cross-tier property is realized once in the stack and gated automatically where a check exists. `known | gap: roll-up`.
- **SECURITY** (roll-up): realizes the A02, A03, A04 (transport) and A08 (pipeline) owners. `known | gap: roll-up`.
  - **SECURITY.1**:
    - ASVS 5.0, requirements cited by versioned id (L304). The level is recorded per project by risk: Level 2 by default, the level ASVS 5.0 says most applications should strive for; Level 3 for critical data; never Level 1.
    - Access control is verified where GUARD.3 places it. Per-user read visibility across backends: recorded default (each backend filters from a shared specification, shared denial tests; read functions with the verified actor acceptable for two or more backends); reporting and operator roles see every row unless restricted.
    - `known | gap: ASVS chapter list not read | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
  - **SECURITY.2**:
    - TLS at the proxy, with a permanent redirect and automated certificates; TLS 1.3, 1.2 for compatibility (L141 to L144).
    - HSTS on every HTTPS response: a long max-age on the application's host, raised in steps, includeSubDomains once its subdomains serve HTTPS (L146, L147). Preload only when the team controls the registrable domain and commits every subdomain, internal ones included, to HTTPS, recorded as an ADR (L148; preload list operators). Secure cookies (L145).
    - Database connections across a network hop are encrypted and verified (inferred).
    - `known | unvalidated: ramp, database TLS | gap: no Postgres TLS row; re-encryption open (L140)`.
  - **SECURITY.3**:
    - A strict CSP with per-response nonces from the Python templates and hashes for build-time pages; report-only first (L334 to L336).
    - The baseline headers of L337, each with one setter. Nonce pages are never stored in shared caches (inferred).
    - `known | unvalidated: setters, caching`.
  - **SECURITY.4**:
    - A managed store is the authority; least privilege, rotation and audit (L351). Each database consumer role has its own credentials.
    - Delivery at start by file or by a non-shared environment (L350 reconciled).
    - Under the assumed hosting the store is a technology to add (EVOLUTION.4 of J5); until it is added, a file outside source control, readable only by the service account, with scheduled rotation, is in force (Q1).
    - `known | conflict: L350 reconciled | unvalidated: reconciliation; fallback in force until a store is added`.
  - **SECURITY.5**:
    - Hash-pinned Python installs and JavaScript lockfiles; pinned base images; an SBOM scanned continuously; staged rollouts (L354 to L356).
    - Signed SLSA Build L3 provenance verified before deploy (L357, SRC-242: "intended for most software releases"); Build L2 acceptable when the build platform cannot isolate runs or keep the signing key from the build steps. Postgres extensions from official sources (inferred).
    - `known | unvalidated: extensions`.
- **PERFORMANCE**:
  - LCP 2.5 s, INP 200 ms and CLS 0.1 at the 75th percentile per device class, from field data (L295).
  - Build budgets per page type on LCP, CLS and weight (L296); INP gated in the field (L015). Server-Timing joins server and database time (L376).
  - Derived server budget: about 1 s at most for the server's part of a page at the 75th percentile, well under 1 s for an interaction's request (L297, L295, L013, ACT.3; inferred).
  - `known | unvalidated: lab budget set; derived server budget | gap: no source-stated server target; no agent latency target`.
- **CONTRACTS** (roll-up): breaking changes go expand, migrate, contract; lockstep only when every consumer ships in the same deployment as the migration (realizes the L517 narrowing, counted at PIG-WEB.DATA.INTERFACE.1). `known | gap: roll-up`.
  - **CONTRACTS.1**:
    - The function API has two checks: the catalogue diff (provider) and each consumer's suite against the candidate schema (consumers, L401, L559, L487). Columns granted to BI fall under the same diff (inferred).
    - HTTP uses the MD-02 sync gate, a breaking-change diff and generated island types. No consumer-driven tests for the team's own islands, which settles L560 for the default.
    - Agents rely on the description, the agent tool surface and deprecation signals, all under the sync gate and the compatibility window. External doubles are tested daily (L561).
    - `known | unvalidated: consumer suites, granted-column gate | conflict: L560 settled`.
  - **CONTRACTS.2**:
    - Meaning is enforced by constraints where possible and written otherwise (L562). L563's field list covers every contract, the function API and BI tables included.
    - Owners per L515. A lifecycle status on every element; no version numbers on the function API (L517), change carried by new names (J5's expand step, L512); the HTTP description carries its document version (L565 reconciled).
    - L564's type derivation is rejected for stored facts (RECORD.3).
    - `known | conflict: L564 against RECORD.3 (J1 wins); L565 read through L517; realizes the L517 narrowing`.
- **OPERABILITY** (roll-up). `known | gap: roll-up`.
  - **OPERABILITY.1**:
    - W3C traceparent everywhere, job rows included. The trace id goes into a transaction-local setting beside the actor (L566) and onto audit rows (L658).
    - JSON logs on stdout with trace ids (L371, L372). An untrusted caller's sampling is not continued (L374).
    - Every trace is kept while volume allows, then tail sampling (L369).
    - `known | unvalidated: database carrier, job carrier, sampling rule`.
  - **OPERABILITY.2**:
    - The rendered page carries its trace id. Both error handlers, web-vitals, sendBeacon on visibilitychange (L378 to L381).
    - A Reporting API endpoint is the CSP report sink (L380). Incoming events are treated as untrusted (L395).
    - `known | unvalidated: page trace id`.
  - **OPERABILITY.3**:
    - The four signals per process type and for Postgres, as histograms; few user-facing indicators; pages only when urgent (L383 to L387).
    - pg_stat_statements from day one, which gives load per consumer role (L389, inferred). The Postgres-first triggers are monitored (J1, L605, L533).
    - `known | unvalidated: per-role load, trigger signals`.
  - **OPERABILITY.4**:
    - A central collector outside the application database, with read-only copies and every access recorded (L392, L393).
    - L098's events, including refusals made inside database functions, and the Postgres log (role and privilege changes included) shipped to it (inferred). Kept apart from the business audit trail (ACT.4).
    - `known | unvalidated: database-side refusals`.
  - **OPERABILITY.5**:
    - Real Postgres at the production version, a disposable database, rolled-back transactions; never-committing boundaries in shared environments (L399, L400, L567 adopted).
    - Commit-time and concurrent behaviour is tested with committing sessions in the disposable database, never a shared one; concurrency tests for GUARD.2's rules are part of the default suite (inferred). Tests run as the consumer role. Read-visibility denial: recorded default, awaiting maintainer.
    - `known | unvalidated: commit-time tests, concurrency tests, consumer role | gap: no row on concurrency testing | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
  - **OPERABILITY.6**:
    - One typed settings object. Behaviour config is versioned and reviewed; deploy values are per deploy; secrets come from the store (L247 to L251).
    - A staged pipeline with drift and catalogue gates first (L403). Migrations ship before dependent consumers, additive across the window (L405, L047); lockstep only under the same-deployment condition. Short-lived toggles (L404).
    - `known | conflict: L251 reconciled`.
  - OPERABILITY.7: deferred, not judged.
- **TOPOLOGY** (roll-up). `known | gap: roll-up`.
  - **TOPOLOGY.1**:
    - One buffering proxy as the only entry, with buffering off on streaming routes (inferred).
    - Forwarded headers set by the proxy and trusted only from it; Host validated twice; a unix socket (L134 to L140).
    - `known | gap: re-encryption`.
  - **TOPOLOGY.2**:
    - Gunicorn sync workers for request work; Uvicorn ASGI as its own process type for long-lived connections (L149, L150, L153, L455).
    - Routes making blocking external calls in the request (the login's code exchange, external reads, model calls) run with threaded workers or on the ASGI process type, or carry a short timeout (L153; inferred).
    - Workers start at (2 x cores) + 1. The connection budget covers every database consumer. Python is the only request-time server (JS_SERVER).
    - `known | unvalidated: defaults, separate ASGI type, blocking-call routes`.
  - **TOPOLOGY.3**:
    - One image per release, non-root, pinned. A process manager per unit; workers as extra units; a supervisor (L156 to L160).
    - One server process per container wins when an orchestrator exists.
    - `known | conflict: L157 settled by hosting | unvalidated: Q1`.
  - **TOPOLOGY.4**:
    - Assets built once, fingerprinted, served by the proxy, compressed (L161 to L163, L167).
    - The previous releases' files are kept for the compatibility window (inferred). A CDN only on measured need, micro-caching only anonymous, nonce-free responses.
    - `known | unvalidated: asset history`.
- **EVOLUTION** (roll-up). `known | gap: roll-up`.
  - **EVOLUTION.1**:
    - Several backends may share the database; each backend is one deployable, not split into services without a measured need (MD-03). Split only on proven boundaries (L113 to L116); a split moves no data (inferred).
    - Future services get a domain schema. No BFF, no micro frontends, no JavaScript server. Replacement at seams (L119).
    - `known | conflict: L117 rejected as default | unvalidated: domain schemas, split moves no data`.
  - **EVOLUTION.2**:
    - Modules by business concept, aligned with domain schemas, boundaries checked in the pipeline (L122 to L124).
    - No module touches another domain's tables; every module may call the function API within its role's grants. A cross-domain operation is one database function, composed in the database, called by the module that owns the workflow (ACT.1, X3).
    - `known | unvalidated: module rule | gap: boundary tool`.
  - **EVOLUTION.3**:
    - Short, numbered, superseded-never-edited ADRs with alternatives, confidence and the reversing condition (L129 to L133).
    - Every per-project decision the guideline leaves open gets one, HSTS preload, a secret store to add and an L2 build platform included.
    - `known`.

Pinned:
- Nodes judged: 27 of 28 (pig-web-defaults PIG-WEB.TRANSVERSE; 6 roll-ups judged from their children: PIG-WEB.TRANSVERSE, .SECURITY, .CONTRACTS, .OPERABILITY, .TOPOLOGY, .EVOLUTION; 1 deferred, not judged: OPERABILITY.7 Incident Response).
- Decided 27, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: SECURITY.1 and OPERABILITY.5. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1, a context check, not a trade-off, awaiting maintainer: the default context names no hosting model; TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 assume one or a few self-managed hosts without a container orchestrator and name the winner that changes when one exists. Under that assumption the managed secret store holds only once the team adds one; until then the file fallback is in force.
- Verdicts against the maintainer doctrine: 0 new; realizes the L517 narrowing (J5, J6), counted once at PIG-WEB.DATA.INTERFACE.1: "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract (CONTRACTS, OPERABILITY.6). Adopted as the max choice: L567 (never-committing boundary for shared environments), L517's coordination and "no formal version numbers" (the new function name is J5's expand step and L512's route, not L517's text), L545 (ticket id on owner-run jobs), L566 (transaction-local context, here also carrying the correlation id, inferred).
- Conflicts with J1 placements: 0. L564 (derive Postgres, Python and TypeScript types from a logical type in the contract) is rejected for stored facts because RECORD.3 and TYPE_CHAIN make the Postgres schema their origin; its logical-versus-physical split is kept as documentation. EVOLUTION.2's module rule now matches ACT.1 and MD-03: modules never reach another domain's tables; the function API, cross-domain operations included, is reachable from every module within its role's grants.
- Tensions recorded, not overridden: (a) L350, secrets in environment variables against a managed store: the store is the authority, delivery by file or environment at start; under the assumed hosting the store is a technology to add, and until then the file fallback is in force. (b) L251 with L248: behaviour config versioned, reviewed and promoted with the release; deploy-specific values per deploy from the environment. (c) L565's contract version against L517: the function API carries change in names, the HTTP description in its document version. (d) L351's 90-day minimum for secret-access logs against L048: retention set by obligations, 90 days as the floor where none exists. (e) L369: every trace kept while volume allows, then tail sampling; ratio head sampling that drops error traces rejected. (f) L147 and L148, HSTS preload: the default end state is a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS; preload only as a recorded decision when the team controls the registrable domain.
- Gaps in the evidence: (1) L304: ASVS chapter list not read; the Level 2 default is now grounded (ASVS 5.0: "most applications should be striving" for it). (2) No row on TLS for database connections of consumers across a network hop, nor on re-encryption from proxy to application server (L140 open). (3) Correlation id carried into the database transaction, inferred (from J5). (4) No ledger row on concurrency testing; the tests are required by GUARD.2 and part of the default suite, with committing sessions in a disposable database (inferred). (5) No source-stated server latency target and none for the agent surface; a derived server budget (about 1 s for the server's part of a page at the 75th percentile, well under 1 s for an interaction's request) is inferred from L295, L297, L013 and ACT.3. (6) Previous releases' fingerprinted assets kept during the compatibility window, inferred (J4 hand-off). (7) Authorization refusals decided inside database functions reaching the security event log, inferred. (8) No module-boundary tool read for Python (L123 inferred). (9) The 6 roll-ups own no row.
- Review fixes: 12 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, M5, M6, m1, m2, m3, m6, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

## L3 full

Full records: `records.md`, one per node, with positions and ledger ids, forces, decision and grounds, rejected positions with their winning conditions, links, and proposed `epistemic_state`. Question: `questions.md`. Below: the review fixes, how this unit sits against the settled verdicts, what it hands to the other stack judges, and what a reviewer should check first.

### Review fixes

Sources: `../review_transverse/review.md` (14 findings) and `../cross_branch_fixes.md` (X1 to X7, applied verbatim, overriding the review where both speak). Each finding's evidence was checked against the ledger, the allocation matrix and the records before applying it; none was found wrong, so none is rejected. Every changed record ends with a **Review fixes** line in `records.md`.

| finding | records changed | change | evidence check |
|---|---|---|---|
| B1, X3 (blocking) | EVOLUTION.2, EVOLUTION roll-up, TRANSVERSE roll-up; pins | The module boundary forbids another domain's tables only; the function API is reachable from every module within its role's grants. One business operation is one database function call in its own transaction; a database function may call another domain's published functions in the same transaction. A cross-domain operation is called by the workflow's module and owned per J5 EVOLUTION.5. The Python module interface carries workflow and policy, never a second path to data. The old rule moved to *Rejected* with its reason. Rule `unvalidated`. | ACT.1 forbids "multi-table writes composed in a backend; a backend transaction wrapping several API calls"; RECORD.2 gives each consumer role the function API: confirmed. |
| M1, X2 | CONTRACTS roll-up, CONTRACTS.1, CONTRACTS.2, OPERABILITY.6; pins; questions | Pin: "0 new; realizes the L517 narrowing (J5, J6)", counted at PIG-WEB.DATA.INTERFACE.1. X2's condition word for word. The new-name rule credited to J5's expand step and L512, not to L517. What the catalogue gate's "coordinated" mark requires stated. | L517's text has no new-name clause; L512 does (new named version): confirmed. |
| M2, X4 | OPERABILITY.5, OPERABILITY roll-up; pins gap (4) | Concurrency tests for GUARD.2's rules are part of the default suite, not a gap; commit-time behaviour tested with concurrent committing sessions in a disposable database, never a shared one; gap kept only for the missing ledger row. | L400 gives rollback as an example; L567 scoped to shared environments: confirmed. |
| M3, X5 | EVOLUTION.1, EVOLUTION roll-up, TRANSVERSE roll-up; pins | "One Python backend deployable" replaced by X5; MD-03's several backends do not license splitting a backend; a later split moves no data (inferred). | MD-03 and J5 EVOLUTION.3 read: confirmed. |
| M4 | SECURITY roll-up, SECURITY.2, SECURITY.5 | The stack nodes now name the owners J5's corrected map gives them: A04 transport (proxy TLS, database connection TLS) at SECURITY.2, the A08 pipeline half (signed provenance, trusted sources) at SECURITY.5. | J5's corrected map: consistent. |
| M5 | SECURITY.5, SECURITY roll-up, EVOLUTION.3; pins | Signed provenance at SLSA Build L3, verified before deploy; Build L2 acceptable when the build platform cannot isolate runs or keep the signing key from the build steps; the "levels above L2 not weighed" gap removed; the L2 exception added to the per-project ADRs. | L357 cites SRC-242 (slsa.dev/spec/v1.0/levels), the page the review read: confirmed as the cited source. |
| M6 | SECURITY.2, SECURITY roll-up, EVOLUTION.3; pins tension (f) | Default HSTS end state: a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS. Preload only when the team controls the registrable domain and commits every subdomain, internal ones included, to HTTPS for the long term, as an ADR. | L147 calls the scope "a commitment"; the review read hstspreload.org: accepted. |
| m1 | SECURITY.1, SECURITY roll-up; pins gap (1) | Level 2 default grounded ("most applications should be striving"); "recorded per project by risk" kept; L304's level part moved from open to grounded; chapter list still unread. | The review read the ASVS 5.0 text at tag v5.0.0. The ledger row L304 still says `open`; updating it is outside this unit's scope. |
| m2 | PERFORMANCE; pins gap (5) | Derived server budget (about 1 s for a page's server part at the 75th percentile, well under 1 s per interaction) stated `unvalidated`; gap kept for the agent surface and a source-stated server target. | L297 (TTFB about 40% of LCP), L295 (2.5 s), L013 (0.1 s, 1 s), ACT.3: confirmed. |
| m3 | TOPOLOGY.2, TOPOLOGY roll-up | Routes making blocking external calls in the request (GUARD.4's code exchange, external reads, model calls) run with threaded workers or on the ASGI process type, or carry a short timeout; inferred. | L153 moves to threaded or async workers "for long blocking external calls": confirmed. |
| m6 | SECURITY.4, EVOLUTION.3; questions Q1; pins | Under the assumed hosting the managed store is a technology to add (weighed under J5 EVOLUTION.4); the file fallback is in force until then. Q1 gains the line that the store holds only if one is added. | The record's own fallback condition and Q1's cost line: confirmed. |
| m7, X1 | SECURITY.1, OPERABILITY.5; How to read; pins; questions | One notation, X1's; recorded default, J1's fallback and the SELECT-role consequence stated on both nodes. | J1 Q1's "if unanswered" records A: consistent. |
| X7 | CONTRACTS.1, CONTRACTS roll-up | The agent tool surface (for example an MCP server's tool list and schemas) sits under the MD-02 sync gate and the compatibility window. | MD-02: consistent. |

Not touching this unit: m4, m5 (J5 nodes; m5's owner is cited by EVOLUTION.2); X6 (no node here carries a credential in a URL).

### Reading done

- Read in full:
  - `../../target_hierarchy.md` and `../../maintainer_decisions.md`;
  - section J9 of `../../02_skeleton/judge_plan.md`;
  - `../J1_allocation/allocation_matrix.md`; the default context, access paths, ACT.4 and every PIG-WEB.ALLOCATION record of `../J1_allocation/records.md`;
  - `../J5_phil_transverse/records.md`, and its hand-offs to this unit in its `result.md`;
  - LOGIC.PROCESS in `../J3_phil_logic/records.md`;
  - the J4 environment records that hand work to this unit.
- From the skeleton: the PIG-WEB.TRANSVERSE subtree, the node table and the intentlinks touching it.
- Ledger: all 116 owned rows, in full. Rows owned elsewhere and cited were read for statement and certainty: L009, L026 to L030, L036, L044, L047 to L049, L086 to L104, L110, L127, L226 to L235, L252, L253, L275 to L278, L285, L288, L290, L303, L310, L311, L417, L455 to L457, L474, L483, L487, L512, L513, L515 to L517, L519, L533, L545, L566, L596, L604, L605, L634, L655, L658, L659.
- No research result file was opened.
- For the review fixes: `../review_transverse/review.md`, `../cross_branch_fixes.md`, J1's Q1; ledger rows L013, L147, L148, L153, L297, L304, L357, L400, L512, L517, L567 re-read; SRC-242 resolved in `../../02_skeleton/sources.md`.

### Placements and philosophy verdicts realized

| node | refines (philosophy) | skeleton link to a placement | rests on (cited, not re-decided) |
|---|---|---|---|
| PIG-WEB.TRANSVERSE | TRANSVERSE | none | through children |
| SECURITY, .1 to .5 | TRANSVERSE.SECURITY | none | GUARD.3, GUARD.4, MD-01, MD-03, J1 access paths, PRESENT.1, JS_SERVER |
| PERFORMANCE | TRANSVERSE.PERFORMANCE | none | FORCES.3, FORCES.4 (through J5), ACT.3 |
| CONTRACTS, .1, .2 | TRANSVERSE.CONTRACTS | none | RECORD.2, RECORD.3, DB_API, TYPE_CHAIN, MD-02 |
| OPERABILITY.1 | TRANSVERSE.OPERABILITY.1 | none | ACT.4 (role and actor), GUARD.3 |
| OPERABILITY.2 | TRANSVERSE.OPERABILITY | none | none |
| OPERABILITY.3 | TRANSVERSE.OPERABILITY | none | POSTGRES_FIRST, JOB_HOST, CACHE_STORE triggers; RECORD.2's BI path |
| OPERABILITY.4 | TRANSVERSE.OPERABILITY.1 | conflicts ACT.4 | ACT.4 (two records kept apart) |
| OPERABILITY.5 | TRANSVERSE.OPERABILITY.2 | none | GUARD.2, GUARD.3, ACT.1, ACT.4 |
| OPERABILITY.6 | TRANSVERSE.OPERABILITY.3 | none | RECORD.2, RECORD.3, DB_API, MD-02 |
| TOPOLOGY, .1 to .4 | LOGIC.PROCESS | TOPOLOGY.2 constrains JS_SERVER | ACT.2, ACT.3 (foreign effects off the request path), GUARD.4 (login code exchange in the request), J1 access paths |
| EVOLUTION, .1 to .3 | TRANSVERSE.EVOLUTION | none | RECORD.1, RECORD.2, RULES.4, ACT.1 (one call per operation), JS_SERVER, MD-01, MD-02, MD-03 |

### Hand-offs to the other stack judges (J6 to J8)

- **PIG-WEB.DATA.INTERFACE.1** (J6): owns the count of the L517 narrowing; CONTRACTS, CONTRACTS.2 and OPERABILITY.6 realize it with X2's condition and cite it.
- **PIG-WEB.DATA.INTERFACE.2** (J6): TOPOLOGY.2 assumes one connection budget across every database consumer (all backends, BI, operators, workers). Pool sizing per process must fit it.
- **PIG-WEB.DATA.GUARD.3** (J6): OPERABILITY.1 puts the trace id in the same reserved transaction-local namespace as the actor (L566). The namespace layout is J6's.
- **PIG-WEB.DATA** functions (J6): EVOLUTION.2 lets a database function call another domain's published functions in the same transaction (X3); the grants that allow it are J6's.
- **PIG-WEB.LOGIC.SECURE.6 and LOGIC.EXPOSE.5** (J7): the proxy carries the outermost request limits (TOPOLOGY.1). Their values and the CORS policy are J7's.
- **PIG-WEB.LOGIC.ENFORCE.5** (J7): TOPOLOGY.2's WSGI default and OPERABILITY.6's settings object assume a framework that supports both. A framework that runs async end to end moves TOPOLOGY.2 to its ASGI condition. The login route's code exchange is a blocking external call (TOPOLOGY.2, m3).
- **PIG-WEB.INTERACTION.REALTIME and AGENT** (J8): if real-time channels or streamed agent responses are adopted, they run on an ASGI process type behind proxy routes with buffering off (TOPOLOGY.1, .2). Model calls made in the request follow TOPOLOGY.2's blocking-call rule. Whether the agent surface is its own process type is J8's; its tool surface sits under the MD-02 sync gate (CONTRACTS.1, X7).
- **PIG-WEB.INTERACTION.VISUALIZE.1** (J8): pages produced at build time use CSP hashes (SECURITY.3).

### Reviewer checklist (where invented facts would hide)

1. EVOLUTION.2: the module rule (tables forbidden, function API reachable within grants) is inferred from ACT.1, RECORD.2 and X3; its boundary tool is open.
2. OPERABILITY.4: database-side authorization refusals reaching the security log is a synthesis. The two carriers are the backend logging the refusal it receives and Postgres's own log shipped to the collector.
3. OPERABILITY.5: committing tests in a disposable database and required concurrency tests are inferred from L400, L567 and GUARD.2. They do not contradict L567, which governs shared environments.
4. CONTRACTS.1: consumer suites run against the candidate schema, and the catalogue diff is extended to granted tables and columns. Both are mechanisms inferred from L401, L559 and DB_API's gate.
5. PERFORMANCE: the derived server budget is arithmetic on L297 and L295, bounded by L013 and ACT.3; no source states it.
6. TOPOLOGY.4: keeping previous releases' assets for the compatibility window answers J4's hand-off. No row states it.

Pinned:
- Nodes judged: 27 of 28 (pig-web-defaults PIG-WEB.TRANSVERSE; 6 roll-ups judged from their children: PIG-WEB.TRANSVERSE, .SECURITY, .CONTRACTS, .OPERABILITY, .TOPOLOGY, .EVOLUTION; 1 deferred, not judged: OPERABILITY.7 Incident Response).
- Decided 27, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: SECURITY.1 and OPERABILITY.5. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1, a context check, not a trade-off, awaiting maintainer: the default context names no hosting model; TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 assume one or a few self-managed hosts without a container orchestrator and name the winner that changes when one exists. Under that assumption the managed secret store holds only once the team adds one; until then the file fallback is in force.
- Verdicts against the maintainer doctrine: 0 new; realizes the L517 narrowing (J5, J6), counted once at PIG-WEB.DATA.INTERFACE.1: "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract (CONTRACTS, OPERABILITY.6). Adopted as the max choice: L567 (never-committing boundary for shared environments), L517's coordination and "no formal version numbers" (the new function name is J5's expand step and L512's route, not L517's text), L545 (ticket id on owner-run jobs), L566 (transaction-local context, here also carrying the correlation id, inferred).
- Conflicts with J1 placements: 0. L564 (derive Postgres, Python and TypeScript types from a logical type in the contract) is rejected for stored facts because RECORD.3 and TYPE_CHAIN make the Postgres schema their origin; its logical-versus-physical split is kept as documentation. EVOLUTION.2's module rule now matches ACT.1 and MD-03: modules never reach another domain's tables; the function API, cross-domain operations included, is reachable from every module within its role's grants.
- Tensions recorded, not overridden: (a) L350, secrets in environment variables against a managed store: the store is the authority, delivery by file or environment at start; under the assumed hosting the store is a technology to add, and until then the file fallback is in force. (b) L251 with L248: behaviour config versioned, reviewed and promoted with the release; deploy-specific values per deploy from the environment. (c) L565's contract version against L517: the function API carries change in names, the HTTP description in its document version. (d) L351's 90-day minimum for secret-access logs against L048: retention set by obligations, 90 days as the floor where none exists. (e) L369: every trace kept while volume allows, then tail sampling; ratio head sampling that drops error traces rejected. (f) L147 and L148, HSTS preload: the default end state is a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS; preload only as a recorded decision when the team controls the registrable domain.
- Gaps in the evidence: (1) L304: ASVS chapter list not read; the Level 2 default is now grounded (ASVS 5.0: "most applications should be striving" for it). (2) No row on TLS for database connections of consumers across a network hop, nor on re-encryption from proxy to application server (L140 open). (3) Correlation id carried into the database transaction, inferred (from J5). (4) No ledger row on concurrency testing; the tests are required by GUARD.2 and part of the default suite, with committing sessions in a disposable database (inferred). (5) No source-stated server latency target and none for the agent surface; a derived server budget (about 1 s for the server's part of a page at the 75th percentile, well under 1 s for an interaction's request) is inferred from L295, L297, L013 and ACT.3. (6) Previous releases' fingerprinted assets kept during the compatibility window, inferred (J4 hand-off). (7) Authorization refusals decided inside database functions reaching the security event log, inferred. (8) No module-boundary tool read for Python (L123 inferred). (9) The 6 roll-ups own no row.
- Review fixes: 12 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, M5, M6, m1, m2, m3, m6, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.
