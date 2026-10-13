# J9 pig-web-defaults TRANSVERSE: judge records

One judge record per node of the PIG-WEB.TRANSVERSE branch of `pig-web-defaults` (28 nodes, one deferred), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves its purpose; weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. MAINT rows (source MAINT-S01) weigh as a strong position. The maintainer's decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points and are cited by id. The allocation verdicts (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled, and the philosophy verdicts these nodes refine (`../J5_phil_transverse/records.md`; LOGIC.PROCESS in `../J3_phil_logic/records.md`) are binding: these nodes are their stack realization and re-decide neither. Summary at three levels: `result.md`; questions: `questions.md`.

Pinned:
- Nodes judged: 27 of 28 (pig-web-defaults PIG-WEB.TRANSVERSE; 6 roll-ups judged from their children: PIG-WEB.TRANSVERSE, .SECURITY, .CONTRACTS, .OPERABILITY, .TOPOLOGY, .EVOLUTION; 1 deferred, not judged: OPERABILITY.7 Incident Response).
- Decided 27, undecided 0. Two decided nodes carry the pending clause `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`: SECURITY.1 and OPERABILITY.5. Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted.
- Questions: 1, a context check, not a trade-off, awaiting maintainer: the default context names no hosting model; TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 assume one or a few self-managed hosts without a container orchestrator and name the winner that changes when one exists. Under that assumption the managed secret store holds only once the team adds one; until then the file fallback is in force.
- Verdicts against the maintainer doctrine: 0 new; realizes the L517 narrowing (J5, J6), counted once at PIG-WEB.DATA.INTERFACE.1: "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract (CONTRACTS, OPERABILITY.6). Adopted as the max choice: L567 (never-committing boundary for shared environments), L517's coordination and "no formal version numbers" (the new function name is J5's expand step and L512's route, not L517's text), L545 (ticket id on owner-run jobs), L566 (transaction-local context, here also carrying the correlation id, inferred).
- Conflicts with J1 placements: 0. L564 (derive Postgres, Python and TypeScript types from a logical type in the contract) is rejected for stored facts because RECORD.3 and TYPE_CHAIN make the Postgres schema their origin; its logical-versus-physical split is kept as documentation. EVOLUTION.2's module rule now matches ACT.1 and MD-03: modules never reach another domain's tables; the function API, cross-domain operations included, is reachable from every module within its role's grants.
- Tensions recorded, not overridden: (a) L350, secrets in environment variables against a managed store: the store is the authority, delivery by file or environment at start; under the assumed hosting the store is a technology to add, and until then the file fallback is in force. (b) L251 with L248: behaviour config versioned, reviewed and promoted with the release; deploy-specific values per deploy from the environment. (c) L565's contract version against L517: the function API carries change in names, the HTTP description in its document version. (d) L351's 90-day minimum for secret-access logs against L048: retention set by obligations, 90 days as the floor where none exists. (e) L369: every trace kept while volume allows, then tail sampling; ratio head sampling that drops error traces rejected. (f) L147 and L148, HSTS preload: the default end state is a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS; preload only as a recorded decision when the team controls the registrable domain.
- Gaps in the evidence: (1) L304: ASVS chapter list not read; the Level 2 default is now grounded (ASVS 5.0: "most applications should be striving" for it). (2) No row on TLS for database connections of consumers across a network hop, nor on re-encryption from proxy to application server (L140 open). (3) Correlation id carried into the database transaction, inferred (from J5). (4) No ledger row on concurrency testing; the tests are required by GUARD.2 and part of the default suite, with committing sessions in a disposable database (inferred). (5) No source-stated server latency target and none for the agent surface; a derived server budget (about 1 s for the server's part of a page at the 75th percentile, well under 1 s for an interaction's request) is inferred from L295, L297, L013 and ACT.3. (6) Previous releases' fingerprinted assets kept during the compatibility window, inferred (J4 hand-off). (7) Authorization refusals decided inside database functions reaching the security event log, inferred. (8) No module-boundary tool read for Python (L123 inferred). (9) The 6 roll-ups own no row.
- Review fixes: 12 of the 14 findings of the TRANSVERSE review touch this unit (B1, M1, M2, M3, M4, M5, M6, m1, m2, m3, m6, m7), with the cross-branch resolutions X1 to X5 and X7; all applied, 0 rejected.

## How to read

- **Rows**: ledger rows the node owns, read in full; rows owned elsewhere are cited as positions or grounds.
- **Positions**: P1.. with ledger ids. **Forces**: what each serves, at what cost. **Decision**: the max choice and its grounds. **Rejected**: each other position, why, and the condition under which it wins.
- **Realizes**: the philosophy node it refines (skeleton inter link), the skeleton intentlinks to placements, then the J1 placements the decision rests on (cited, not re-decided).
- **State**: proposed `epistemic_state`, in J1's notation: `known`; `known | unvalidated: X` (X inferred); `| conflict:`; `| gap:`; `speculative` for thin evidence; `| undecided: awaiting maintainer, X` (a clause of a decided node that waits on an open maintainer question; the same token in every unit, so the graph builder finds every node the answer changes).
- **Review fixes**: each record changed by the TRANSVERSE review (`../review_transverse/review.md`) or by the cross-branch resolutions (`../cross_branch_fixes.md`) ends with a **Review fixes** line naming the finding ids.
- **Default context** throughout: MD-03 as restated by J1 (a classic website, one team, JavaScript + Python + Postgres, single tenant, humans and agents as users; the database shared by several backends and by BI and reporting, admin consoles and scripts, each with its own role; browsers and agents never connect to it). Python renders HTML (PRESENT.1, JS_SERVER). Hosting model: not stated; assumed one or a few self-managed hosts without a container orchestrator (questions.md, Q1).

## PIG-WEB.TRANSVERSE Transverse Defaults

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its five children. The stack realizes each cross-tier property of TRANSVERSE once, and turns it into an automated gate where a check exists (L110, J5):
  - security: ASVS 5.0 as the requirement catalogue; TLS and the header set at one edge, HSTS preload only as a recorded decision; secrets from a managed store once one exists, a file fallback until then; a pinned, scanned supply chain with signed provenance at SLSA Build L3;
  - performance: Core Web Vitals at the 75th percentile as targets, budgets in the build;
  - contracts: one verification per seam (catalogue diff and consumer suites for the function API, description checks for HTTP, scheduled tests for external doubles); meaning, owner and lifecycle recorded with each contract;
  - operations: W3C trace context from the browser into the database transaction; the four golden signals plus the placement triggers; a security event log outside the application database; tests on real Postgres; a staged pipeline with migrations first;
  - topology: one buffering reverse proxy; WSGI with sync workers, threaded workers, ASGI or a short timeout for routes with blocking external calls, ASGI where connections are long-lived; process manager per unit; static assets built once and served outside Python;
  - evolution: several backends may share the database, each backend one deployable, not split into services without a measured need; modular by business concept, every module reaching data through the function API, never another domain's tables; decisions in ADRs.
- **Realizes**: refines TRANSVERSE (J5); through its children, ACT.4, JS_SERVER and LOGIC.PROCESS.
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: children's lines updated after B1 (X3), M3 (X5), M5, M6, m3, m6.

## PIG-WEB.TRANSVERSE.SECURITY Security Defaults

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its five children: ASVS 5.0 as the verifiable catalogue at a recorded level (Level 2 by default, grounded in the ASVS 5.0 text); HTTPS terminated at the proxy, HSTS with a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS, preload only as a recorded decision; a strict nonce-based CSP rolled out report-only first, plus a small header baseline; secrets held in a managed store, per consumer role, rotated and audited, with a file fallback in force until a store is added under the assumed hosting; dependencies pinned with hashes, an SBOM scanned continuously, signed provenance at SLSA Build L3 verified before deploy, Build L2 acceptable when the build platform cannot isolate runs.
- **Realizes**: refines TRANSVERSE.SECURITY (J5): realizes its transport, exposure and verifiability decisions and the A02 (misconfiguration), A03 (supply chain), A04 (transport: proxy TLS, database connection TLS) and A08 (integrity: signed provenance, trusted sources) owners.
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: updated after m1, M4, M5, M6, m6.

## PIG-WEB.TRANSVERSE.SECURITY.1 Security Requirement Catalogue

- **Rows**: L304 (ledger state `open`: level definitions and chapter list not read from a T1 source upstream). The level definitions are now read from the ASVS 5.0 text at tag v5.0.0 (by the TRANSVERSE review): Level 1 "contains the minimum requirements ... a critical starting point"; Level 2: "Most applications should be striving to achieve this level of security"; Level 3 "should be the goal for applications looking to demonstrate the highest levels of security"; and an organisation "should analyze its risks and decide what level". The chapter list stays unread.
- **Positions**:
  - P1 ASVS 5.0 as the catalogue of verifiable requirements, cited by versioned id (for example v5.0.0-1.2.5), at a verification level chosen by application risk (L304).
  - P2 the OWASP Top 10 as the checklist (L303, owned by TRANSVERSE.SECURITY; J5 kept it as the awareness map only).
- **Forces**: P1 serves verifiability (each property testable and traceable), at a cost scaled by the level. P2 serves awareness at low cost and is not testable.
- **Decision**: P1, as J5 requires (a verifiable catalogue at a risk-chosen level).
  - ASVS 5.0 is the catalogue. Requirements are cited by their versioned id in this guideline's traces and in the project's tests and reviews (L304).
  - The level is a recorded decision per project, by risk (EVOLUTION.3; the source's own rule). Default: Level 2, the level the ASVS 5.0 text says most applications should strive for (grounded). The MD-03 context fits it: the application holds business data of several consumers and accepts writes from humans and agents. Level 3 when a breach would be critical (payments, health, safety; the source's "highest levels of security", the examples inferred). Level 1 is never the default, consistent with the source's "starting point".
  - Each requirement is verified at the tier the placements name. Access control is checked where GUARD.3 puts it: writer functions for per-user write rules, the backend for product policy and identity, Postgres roles per consumer (MD-01, MD-03). **Undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database** (not settled here). Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. Database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends. Consequence for verification: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted; no access-control requirement is marked met on a stronger guarantee than this.
  - Where a requirement has an automated check, it runs in the pipeline (OPERABILITY.6; L110).
- **Rejected**: P2 as the requirement set: never; it stays the awareness map (L303, J5). A catalogue without a recorded level: never, since the level is what makes the claim verifiable.
- **Realizes**: refines TRANSVERSE.SECURITY (its verifiability decision); rests on GUARD.3, MD-01, MD-03.
- **State**: `known | gap: ASVS chapter list not read (L304's level part now grounded) | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **Review fixes**: m1 (Level 2 default grounded in the ASVS 5.0 text; L304's level part moved from open to grounded; "recorded per project by risk" kept); m7 and X1 (one notation for the pending clause; default, fallback and consequence stated).

## PIG-WEB.TRANSVERSE.SECURITY.2 Transport Security

- **Rows**: L141, L142, L143, L144, L145, L146, L147, L148.
- **Positions**:
  - P1 terminate TLS at the proxy or edge (L141, majority: FastAPI docs, Twelve-Factor routing, Uvicorn's layered setup).
  - P2 terminate TLS in the Python server (Uvicorn documents certificate options, L141 positions).
  - Consensus practices: HTTP to HTTPS permanent redirect at the proxy, only HTTPS-originated requests forwarded (L142); automated certificate issuance and renewal at about two thirds of validity (L143); TLS 1.3, 1.2 only for compatibility (L144); Secure cookies, no HTTP subresource (L145); HSTS on HTTPS responses only with max-age (L146); includeSubDomains and preload only after every subdomain serves HTTPS, max-age raised in steps (L147); the redirect stays because HSTS does not cover the first request (L148).
- **Forces**: P1 serves one place for certificates, protocol policy and the edge limits (L091, J3), at the cost of a plaintext hop to the application server. P2 serves end-to-end encryption to the process, and spreads certificates over every application process. Preload serves the first request (L148); its cost is a commitment that breaks any subdomain still on HTTP (L147).
- **Decision**: P1 with every consensus practice; HSTS on the application's host by default, preload as a recorded decision.
  - TLS terminates at the single reverse proxy (TOPOLOGY.1). The proxy redirects HTTP permanently and forwards only HTTPS-originated requests (L142). It obtains and renews certificates itself, or through a tested ACME client (L143). TLS 1.3, with 1.2 kept only for clients that need it (L144).
  - HSTS is sent on every HTTPS response, set in one place (L146). Default end state: a long max-age on the application's host, reached by raising max-age in steps, with includeSubDomains once its subdomains serve HTTPS (L147). The HTTP redirect stays (L148).
  - Preload is the target when the team controls the registrable domain and commits every subdomain, internal ones included, to HTTPS for the long term. It is recorded as an ADR (EVOLUTION.3) because removal from the preload list takes months to reach users. Grounds: the preload list's operators advise "do not include the `preload` directive by default", and preloading covers every subdomain of the base domain, "including internal subdomains that are not publicly accessible" (hstspreload.org, read by the TRANSVERSE review); L147 calls the scope "a commitment". A web application often runs on a subdomain of a domain its team does not control. Preload stays the strongest protection of the first request (L148).
  - Session and CSRF cookies are Secure; no subresource is loaded over HTTP (L145).
  - Proxy to application server: a unix domain socket on the same host (L140). Across a network hop, re-encryption is open (gap).
  - Database connections that cross a network hop, from every consumer role (backends, BI, consoles, scripts), are encrypted and verify the server's certificate. Inferred from J5 TRANSVERSE.SECURITY (MD-03 adds consumers outside the request path); no row read on Postgres connection settings (gap).
- **Rejected**:
  - P2: acceptable when there is no proxy, which only local development allows (L091, J3).
  - Preload as the default end state: rejected; it commits the whole registrable domain, internal subdomains included, and is slow to undo. It wins under the recorded condition above (team controls the registrable domain, long-term HTTPS commitment for every subdomain), as an ADR.
  - HTTPS only on sensitive pages: never (L029, J5).
- **Realizes**: refines TRANSVERSE.SECURITY (transport; part of the A04 owner: the proxy's TLS and the database connection TLS); rests on LOGIC.PROCESS (proxy in front, J3) and GUARD.4 (Secure session cookie).
- **State**: `known | unvalidated: staged HSTS ramp (L147); database connection encryption | gap: no row on Postgres connection TLS; proxy-to-app re-encryption open (L140)`.
- **Review fixes**: M6 (default end state is HSTS with a long max-age on the application's host, includeSubDomains once subdomains serve HTTPS; preload only under its recorded condition, as an ADR); M4 (A04 transport owner named).

## PIG-WEB.TRANSVERSE.SECURITY.3 Security Headers and CSP

- **Rows**: L334, L335, L336, L337.
- **Positions**:
  - P1 a strict CSP: nonce or hash with `strict-dynamic`, `object-src 'none'`, `base-uri 'none'`, no `unsafe-inline` or `unsafe-eval` (L334).
  - P2 an allowlist CSP (the alternative L334 ranks below P1).
  - Rollout: report-only first, fix, then enforce (L335). Nonces unique per response, injected by a real templating engine; hashes for static inline scripts (L336).
  - Baseline headers: HSTS, `nosniff`, `Referrer-Policy`, CSP `frame-ancestors` in place of `X-Frame-Options`, `Permissions-Policy`, COOP; remove `X-XSS-Protection`, `Expect-CT`, `Server`, `X-Powered-By` (L337).
- **Forces**: P1 serves containment of injected script (the second layer after escaping, L026, J4), at the cost of nonce plumbing and refactoring inline handlers. P2 serves ease of adoption, and is bypassable through allowed hosts (L334's ranking).
- **Decision**: P1, with nonces from the Python templates.
  - Python renders the HTML (PRESENT.1, JS_SERVER), so each response gets a fresh nonce from the server's templating engine (L336). Pages produced at build time use hashes for their inline scripts (L336, L285).
  - A page that carries a nonce is never stored in a shared cache, or the nonce would repeat across responses (inferred from L336; consistent with J4's no-store rule for personalised pages).
  - Rollout: Content-Security-Policy-Report-Only first, violations sent to a Reporting API endpoint (L380, OPERABILITY.2), fixed, then enforced (L335).
  - The baseline headers of L337 are sent on every response, the obsolete ones removed. Each header has one setter: the application for CSP (it holds the nonce), the proxy for the static baseline so static files carry it too (inferred).
  - CSP stays the second layer. Templates escape by default (L026, J4).
- **Rejected**: P2: acceptable never as the target; tolerated only as a temporary step while inline handlers are removed (inferred). `X-Frame-Options` and `X-XSS-Protection` as protections: never (L337).
- **Realizes**: refines TRANSVERSE.SECURITY (A02); realizes INTERACTION.ENVIRONMENT.7's hand-off (J4); rests on PRESENT.1 and JS_SERVER (server-rendered HTML makes nonces available).
- **State**: `known | unvalidated: one setter per header; no shared caching of nonce pages`.

## PIG-WEB.TRANSVERSE.SECURITY.4 Secrets

- **Rows**: L350, L351, L352, L353. Cited: L102, L250, L036.
- **Positions**:
  - P1 secrets in environment variables (Twelve-Factor: simple, language-neutral, portable; L350).
  - P2 runtime injection from a managed store, with access control, rotation and audit (OWASP; L350, L351).
  - Consensus: centralised storage, least privilege per service, short-lived dynamic secrets with automated rotation, every access audited with logs kept at least 90 days (L351); the framework signing secret kept confidential (L352); CI/CD treated as production (L353); secrets never in source (L102, L250).
- **Forces**: P2 serves confidentiality, revocation and accountability (who read which secret), at the cost of a store to run or rent. P1 serves simplicity and portability; environment variables are visible to many processes and leak through dumps and error pages (L350). The positions answer two different questions: where the secret is held, and how it reaches the process.
- **Decision**: P2 as the authority; delivery at process start by file or environment.
  - Every secret is held in one managed store: the platform's secret store, or a secrets manager. Access is granted per service and per consumer role, least privilege, and every access is audited (L351).
  - Each database consumer role of MD-03 has its own credentials: each backend, the reporting role, the operator role and the owner role (J1 access paths). They are rotated automatically; short-lived dynamic credentials are preferred where the store issues them (L351).
  - Delivery: the secret reaches the process at start, as a file readable only by the service account or as an environment variable. The environment is acceptable when no other process can read it and the framework never dumps it (debug off, L250). It is reconciled from L350, inferred.
  - The framework signing secret is held like any other, never committed, and rotated (L352).
  - CI/CD: least-privilege service accounts, secrets scoped per environment, none in pipeline output (L353).
  - Secret-access logs are kept as long as obligations require, at least 90 days where none exists (L351 read with L048).
- **Rejected**: P1 as the place where secrets are held: acceptable when no managed store exists on the platform and adding one is not budgeted (EVOLUTION.4). The secret then sits in a file outside source control, readable only by the service account (L250), and rotation is a scheduled task.
- **Under the assumed hosting** (self-managed hosts, no orchestrator; questions.md, Q1): there is no platform store, so the managed store is a technology to add, weighed under EVOLUTION.4 (J5: a new technology past a measured need, its operating cost budgeted). Until it is added, the file fallback above is in force. On a platform that offers a store, the store is the authority from the start.
- **Realizes**: refines TRANSVERSE.SECURITY (exposure, L036); rests on the J1 access paths (one role per consumer, MD-03).
- **State**: `known | conflict: L350 contested (environment variables against a managed store), reconciled by authority and delivery | unvalidated: the reconciliation; credentials per consumer role; the file fallback in force under the assumed hosting until a store is added`.
- **Review fixes**: m6 (the default under the assumed hosting stated plainly: the store is a technology to add, the file fallback in force until then; folded into Q1).

## PIG-WEB.TRANSVERSE.SECURITY.5 Supply Chain

- **Rows**: L354, L355, L356, L357.
- **Positions** (consensus): lockfiles, and for Python hash-checked installs covering transitive dependencies, optionally binary-only (L354); an SBOM of direct and transitive dependencies, scanned continuously (L355); components only from official sources over secure links, signed where possible, updates rolled out in stages (L356); verifiable build provenance, at least SLSA Build L2 from a hosted build platform, verified before use (L357).
- **Forces**: integrity of what runs, at the cost of pipeline work. No position opposes them.
- **Decision**: all four, on every artifact the system runs.
  - Python: lockfile with hashes, `--require-hashes` over the whole tree (L354). JavaScript build dependencies: lockfile, installed from it exactly (L354; per-ecosystem flag inferred). Container base images pinned (L156).
  - SBOM per release artifact, scanned continuously, not only at build (L355). Updates go through the staged pipeline, then a staged or canary rollout (L356, OPERABILITY.6).
  - Provenance: signed provenance at SLSA Build L3, verified before deploy: a hardened build platform where runs cannot influence one another and the signing secrets are out of the build steps' reach. L357 sets Build L2 as the floor; its source SRC-242 (the SLSA v1.0 levels page) describes Build L3 as "Intended for: Most software releases", while noting it "usually requires significant changes to existing build platforms". Under the max rule L3 is the target for the node's purpose, the integrity of what runs.
  - Database extensions and the Postgres packages come from official sources at a pinned version (inferred: Postgres hosts the queue scheduler and other backing roles, POSTGRES_FIRST and JOB_HOST).
- **Rejected**:
  - Build L2 as the target: acceptable when the build platform cannot isolate runs or keep the signing key from the build steps (L357, SRC-242).
  - Unpinned installs, builds on developer machines, scanning only at release: none wins in this context.
- **Realizes**: refines TRANSVERSE.SECURITY (A03 owner, and the pipeline half of the A08 owner: signed provenance, trusted sources, J5 after review); rests on OPERABILITY.3 of J5 (one immutable artifact).
- **State**: `known | unvalidated: extensions and JavaScript lockfile practice by extension of L354`.
- **Review fixes**: M5 (Build L3 as the target, L2 under its condition; the "levels above L2 not weighed" gap removed: the evidence is in the cited source); M4 (A08 pipeline owner named).

## PIG-WEB.TRANSVERSE.PERFORMANCE Page Experience Targets

- **Rows**: L295, L296. Cited: L015, L381, L376.
- **Positions**:
  - P1 Core Web Vitals as the targets, judged at the 75th percentile and split by mobile and desktop: LCP at most 2.5 s, INP at most 200 ms, CLS at most 0.1 (L295).
  - P2 budgets per page type enforced in the build, for example Lighthouse CI (L296), with SRC-174's sample numbers (TTI under 5 s, 170 KB, 3G) tied to an old device baseline.
- **Forces**: P1 serves what users experience, measured in the field, after release. P2 serves prevention before release; lab runs cannot measure INP (L015).
- **Decision**: P1 as the target, P2 as the gate, both on Core Web Vitals.
  - Targets: the "good" thresholds of L295 at the 75th percentile, per device class, from field data (OPERABILITY.2). They are the user-facing service level indicators of OPERABILITY.3.
  - Build budgets per page type (L296) on the lab-measurable vitals (LCP, CLS) and on page weight. A build over budget fails or the page is optimised. INP is gated on field data after release (L015). SRC-174's numbers are not adopted (L296).
  - The server's share of each page is visible: Server-Timing carries server and database time for authorised audiences (L376), joined to field data through the trace id (J5 whole path, inferred).
  - Derived server budget (inferred from grounded rows, `unvalidated`): about 1 s at most for the server's part of a page at the 75th percentile, and well under 1 s for an interaction's request. Grounds: the HTML response (TTFB) is about 40% of LCP time (L297) against LCP's 2.5 s (L295); 1 s keeps the flow of thought and 0.1 s feels instantaneous (L013); work over about 1 s is deferred (ACT.3, settled). Database time is part of this server share.
- **Rejected**: lab-only targets: acceptable before launch or while traffic is too low for a stable 75th percentile (J5). Averages: never (L381). The non-vitals timings of SRC-174 as targets: never (L296).
- **Realizes**: refines TRANSVERSE.PERFORMANCE (field truth, lab gate); feeds FORCES.3 and FORCES.4 through J5; rests on ACT.3 (deferral of work over about 1 s).
- **State**: `known | unvalidated: lab budgets limited to LCP, CLS and weight; derived server budget | gap: no source-stated server target; no agent-surface latency target`.
- **Review fixes**: m2 (derived server budget stated as unvalidated from L297, L295, L013 and ACT.3; the gap kept only for the agent surface and a source-stated server target).

## PIG-WEB.TRANSVERSE.CONTRACTS Contract Verification and Meaning

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its two children. Every contract of the default context has a verification matched to its seam and a written meaning, owner and lifecycle. The contracts are the function API (several consumers), the tables and columns granted to BI, the HTTP interface (own browser code, agents), the agent tool surface and the external services. Each verification runs in the pipeline. Breaking changes follow J5's expand, migrate, contract; "deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration. This realizes the L517 narrowing, counted at PIG-WEB.DATA.INTERFACE.1 (J6), not here.
- **Realizes**: refines TRANSVERSE.CONTRACTS (J5); rests on RECORD.2, RECORD.3, DB_API, TYPE_CHAIN, MD-02.
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: M1 and X2 (narrowing cited, condition word for word); X7 (agent tool surface listed among the contracts).

## PIG-WEB.TRANSVERSE.CONTRACTS.1 Contract Verification

- **Rows**: L401, L402, L559, L560, L561. Cited: L487, L517, L634, L275.
- **Positions**:
  - P1 contract tests between independently deployed components; consumer-driven where a provider serves consumers (L401).
  - P2 for one team's monolith: schema-based API checks plus a few consumer-driven tests suffice (L402, inferred).
  - P3 consumer-driven tests for any client and front-end pair, even within one team (Pact, L560, contested).
  - P4 schema checks and consumer contracts answer different questions, so use both (L559).
  - P5 tests of external-service doubles run on the external service's rhythm, often daily; a failure opens a realignment task (L561).
- **Forces**: P1, P3, P4 serve correctness at each seam; consumer contracts make hidden coupling explicit at the cost of a shared channel between teams (L487). P2 serves effort where both sides ship together. P5 serves catching supplier drift without blocking every commit.
- **Decision**: one verification per seam, both questions of L559 answered wherever consumers deploy separately.
  - **Function API** (provider: the database owner; consumers: several backends, consoles, scripts that deploy separately, MD-03):
    - provider side: the catalogue diff in CI fails on a removed function or an incompatible signature unless marked coordinated (DB_API, J1); the mark holds only for the contract phase of expand, migrate, contract, or when every consumer of the changed object ships in the same deployment as the migration (X2, J5);
    - consumer side: each consumer's typed wrappers are generated from the catalogue (TYPE_CHAIN), and each consumer's integration suite runs against the candidate schema before a migration is promoted. That suite is its consumer contract: the union of what consumers use (L487) is executed, not assumed (L401, L559; mechanism inferred).
  - **Tables and columns granted to BI**: the same catalogue diff covers every object granted to a consumer role, so a removed or retyped granted column fails the gate (inferred extension of DB_API's gate). The change then goes expand, migrate, contract (J5).
  - **HTTP interface to the team's own browser code**: the OpenAPI description is kept in sync with the implementation by the MD-02 gate. A diff against the last released description fails on a breaking change inside the compatibility window (L009, J4). Island types are generated from it at build time (TYPE_CHAIN), so the compile is the consumer check. Consumer-driven tests are not required for this seam (L402); this settles L560 for the default context.
  - **Agents**: they run code the team does not control, so no consumer test can be collected. The description, its breaking-change diff and machine-readable deprecation signals are the whole contract (L634, L275; inferred). "Always in sync by process" and the compatibility window apply to every interface description agents read: the HTTP description and the agent tool surface (for example an MCP server's tool list and schemas) both sit under the MD-02 drift gate and the breaking-change diff (X7).
  - **External services**: contract tests of the doubles run daily or on the supplier's change rhythm; a failure opens a realignment task (L561).
- **Rejected**:
  - P3 for the team's own browser islands: wins when the browser client is a separately deployed application or is built by another team, or when several independently released clients consume the same endpoints (L560's condition).
  - P2 for the function API: rejected because its consumers deploy separately (MD-03); a few tests do not cover the union of what they use.
  - Consumer contracts as the origin of the provider's contract: never (L487, J5).
- **Realizes**: refines TRANSVERSE.CONTRACTS (provider authoritative, consumer contracts as tests); rests on DB_API (catalogue gate), TYPE_CHAIN, RECORD.3, MD-02.
- **State**: `known | unvalidated: consumer suites against the candidate schema; the catalogue gate extended to granted tables and columns | conflict: L560 contested, settled for the default context`.
- **Review fixes**: X7 (the agent tool surface under the MD-02 sync gate and the compatibility window); M1 and X2 (what the "coordinated" mark requires, word for word).

## PIG-WEB.TRANSVERSE.CONTRACTS.2 Contract Meaning and Ownership

- **Rows**: L562, L563, L564, L565. Cited: L474, L483, L517, L512, L275.
- **Positions**:
  - P1 a schema is necessary, not sufficient: record units, time zone, precision and rounding in the contract text or in constraints (L562; JSON `format` is only an annotation, JSON has no integer or date type, Pydantic emits Decimal as a string).
  - P2 the ODCS document format for data contracts; for one application database use its field list as a checklist and skip the format unless data leaves for a platform team (L563, `open`).
  - P3 keep the logical type in the contract and derive the Postgres, Python and TypeScript types from it (L564; derivation inferred).
  - P4 one owner, a version and a lifecycle status per contract (L565).
  - Read against L517 (MAINT): a breaking change is coordinated with every consuming team and deployed together; no formal version numbers on the function API.
- **Forces**: P1 and P4 serve correct reading by consumers outside the producer, at the cost of writing meaning down. P2's format serves exchange with data platforms, at the cost of a second document. P3 serves one logical origin, against J1's placement of the origin.
- **Decision**: P1, P4, and P2's checklist; P3 as documentation only.
  - Meaning is machine-checked where it can be: units, ranges and precision as column types and constraints in Postgres, as field constraints in Pydantic. Where it cannot, it is written next to the object: units, time zone, precision, rounding (L562).
  - Every contract records owner, meaning, quality rules, freshness or availability promise and lifecycle (L563's checklist). This includes the function API and the tables BI reads (MD-03). Stored facts are documented from the live database (L474), the meaning text kept in the catalogue next to each object (mechanism inferred).
  - Owner: the database owner for the function API and granted tables (L515), or a domain schema's owning team when teams multiply (J5); the backend team for HTTP.
  - Version and lifecycle (L565, reconciled with L517). Each function, granted column and endpoint carries a status: active, deprecated, retired. The function API carries no formal version number (L517). Change is carried in names: a new function beside the old, which is J5's expand step (L047) and the route the maintainer's own L512 takes for stored contract schemas, not L517's text. "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise expand, migrate, contract (X2; the narrowing is counted at PIG-WEB.DATA.INTERFACE.1). The HTTP description carries its document version and the deprecation signals of L275.
  - Money and decimals cross JSON as strings with stated precision and currency or unit (L562; inferred form).
- **Rejected**:
  - P3's derivation direction for stored facts: rejected by RECORD.3 and TYPE_CHAIN (J1), which make the Postgres schema the origin. The logical-versus-physical split is kept as documentation of each field.
  - The ODCS format itself: acceptable when data leaves the system for a separate data platform team (L563).
  - A schema without written meaning: never (L562, L483).
- **Realizes**: refines TRANSVERSE.CONTRACTS (explicit artifact with meaning); rests on RECORD.3, TYPE_CHAIN, MD-02, DB_API (L517).
- **State**: `known | unvalidated: meaning stored in the catalogue; decimal form | conflict: L564's derivation direction against RECORD.3 (J1 wins); L565's version field read through L517 (MAINT); realizes the L517 narrowing, counted at PIG-WEB.DATA.INTERFACE.1`.
- **Review fixes**: M1 and X2 (the new-name rule credited to J5's expand step and L512, not to L517; the narrowing realized here, cited, counted at its owner).

## PIG-WEB.TRANSVERSE.OPERABILITY Operations

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its six judged children (OPERABILITY.7 deferred).
  - One trace context runs from the browser through the backend and workers into the database transaction. Logs carry its ids on stdout.
  - Client errors and field vitals come back stamped with release and trace id.
  - Monitoring covers the four golden signals, the triggers that move the Postgres-first placements, and database load per consumer role.
  - The security event log sits outside the application database.
  - Tests run on real Postgres at the production version, rolled back by default; commit-time and concurrent behaviour, GUARD.2's concurrency rules included, is tested with committing sessions in a disposable database.
  - A staged pipeline promotes one artifact, with migrations released before the code that needs them.
- **Realizes**: refines TRANSVERSE.OPERABILITY (J5); through OPERABILITY.4, ACT.4.
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: test line updated after M2 (X4).

## PIG-WEB.TRANSVERSE.OPERABILITY.1 Tracing and Logs

- **Rows**: L369, L370, L371, L372, L373, L374, L375, L376. Cited: L566, L658, L545, L036.
- **Positions**:
  - Sampling: P1 head sampling, simple and cheap, cannot guarantee keeping error traces; P2 tail sampling keeps errors and slow traces, stateful and harder to run; start with head, add tail with volume (L369, "start with head" inferred; SRC-095 calls tail "almost always necessary" at scale).
  - Consensus: W3C `traceparent` across every boundary (L370); trace and span id in every log record (L371); unbuffered stdout, routing by the environment (L372); library instrumentation for framework, HTTP and database client, code instrumentation for business logic only (L373); do not continue an untrusted caller's sampling decision (L374); no personal data in trace headers (L375); Server-Timing only to the audience that may see it (L376).
- **Forces**: diagnosis across tiers (J5 whole path), at the cost of propagation work. In sampling, P2 serves keeping the traces that matter, at an operating cost; P1 serves simplicity and loses error traces once it samples below 100%.
- **Decision**: every consensus practice, the trace carried into the database, and sampling that never drops an error trace.
  - One W3C trace context per user interaction: from the browser (OPERABILITY.2), through the backend, onto every outbound call, and into each job row so workers continue the trace (L370; job carrier inferred).
  - Into the database: the backend sets the trace id in a transaction-local setting in the reserved namespace, beside the actor (L566, MAINT). Writer functions and audit triggers write it on transition and history rows (L658 requires a correlation id for agent actions; ACT.4). Inferred carrier; it gives the work MD-03 places in database functions the same id as the request. Owner-run jobs carry the ticket id in the statement comment (L545).
  - Logs: one JSON event per line on stdout, unbuffered, with trace and span id (L371, L372). Nothing secret or personal in logs or trace headers (L036, L375).
  - Instrumentation: library instrumentation for the framework, HTTP clients and the Postgres driver; code spans only around business steps (L373).
  - Public and agent endpoints: an incoming `traceparent` from an unauthenticated or external caller is recorded but does not decide sampling (L374).
  - Sampling: every trace is kept while volume allows. When volume forces sampling, tail sampling keeps every error and slow trace (L369, P2). Logs still carry the trace id of every error (L371).
  - Server-Timing carries server and database time to authenticated audiences only (L376).
- **Rejected**: head sampling at a ratio below 1: acceptable only when the dropped traces are of successful, fast requests and every error is still captured in logs with its trace id, and while tail sampling cannot be operated (L369). Per-tier silos: never (L095, J5).
- **Realizes**: refines TRANSVERSE.OPERABILITY.1 (one correlation id into the transaction); rests on ACT.4 (role and actor recorded, J1 R1-3) and GUARD.3 (actor setting).
- **State**: `known | unvalidated: trace id in the transaction-local setting and on audit rows; trace context in job rows; keep-all then tail sampling`.

## PIG-WEB.TRANSVERSE.OPERABILITY.2 Client Telemetry

- **Rows**: L377, L378, L379, L380, L381, L382. Cited: L395, L035.
- **Positions** (no competing position; one status caveat):
  - Browser-side OpenTelemetry is experimental: do not depend on it alone; fall back to a propagated header plus real-user measurements (L377, fallback inferred).
  - Uncaught errors through the window `error` event and `unhandledrejection` (L378).
  - Send with `sendBeacon` from `visibilitychange`, fetch as fallback, about 64 KiB per payload (L379).
  - Browser-detected problems through the Reporting API with `Reporting-Endpoints`; not failsafe, not guaranteed (L380).
  - Field vitals with the web-vitals library, 75th percentile, segmented by device, connection and release, collecting only what is used (L381).
  - Events stamped with release and trace or request id (L382, inferred).
- **Forces**: visibility of what users experience and of client failures, at the cost of page weight and of an endpoint that receives untrusted data.
- **Decision**: all six.
  - The server-rendered page carries the trace id of the request that produced it. Client events and the fetches of islands carry it, or a child `traceparent`, so a browser error joins the server trace (L382, L370; injection into the page inferred). No dependence on browser OpenTelemetry (L377).
  - Errors: both global handlers (L378). Vitals: web-vitals, segmented as L381 says. Delivery: `sendBeacon` on `visibilitychange` (L379).
  - A Reporting API endpoint receives CSP violations, deprecations, crashes and interventions (L380). It is the report sink of SECURITY.3's rollout.
  - The collection endpoint treats every event as untrusted input: validated, sanitised before logging (L395). It collects no personal data (L035).
- **Rejected**: browser OpenTelemetry as the only correlation path: never while it is experimental (L377). Sending on `unload` or `beforeunload`: never (L379).
- **Realizes**: refines TRANSVERSE.OPERABILITY (and the field truth of TRANSVERSE.PERFORMANCE); feeds PIG-WEB.TRANSVERSE.PERFORMANCE.
- **State**: `known | unvalidated: trace id injected into rendered pages; release and trace stamping (L382 inferred)`.

## PIG-WEB.TRANSVERSE.OPERABILITY.3 Monitoring

- **Rows**: L383, L384, L385, L386, L387, L388, L389. Cited: L605, L533, L127.
- **Positions** (consensus): latency, traffic, errors and saturation at least (L383); percentiles or histograms (L384); a handful of indicators from what users care about, objectives not set from current performance (L385); page a human only when urgent, actionable and user-visible (L386); white-box and black-box together (L387); utilisation, saturation and errors per resource when hunting a bottleneck (L388); `pg_stat_statements` preloaded (L389).
- **Forces**: detection and diagnosis, at the cost of instrumentation and of alert discipline.
- **Decision**: all seven, extended to the placements that wait on a measurement.
  - The four signals per process type (web, worker) and for Postgres, as histograms (L383, L384). Black-box probes of the critical journeys (L387).
  - Indicators: the page targets of PERFORMANCE at the 75th percentile, availability and server latency of the critical journeys. Objectives are set from what users need (L385).
  - Pages go to a human only on urgent, user-visible conditions (L386); everything else is a ticket.
  - `pg_stat_statements` is enabled from the first deploy (L389). Its per-role figures give database load per consumer role (backends, BI, operators), which J1's access paths need to decide when BI moves to a replica (inferred).
  - The triggers that move POSTGRES_FIRST, JOB_HOST and CACHE_STORE are measured, not guessed (J1): queue backlog age and claim contention, commit latency under NOTIFY, cache hit latency and load on the primary (L127). Job failures, durations and missed runs follow L605 (MAINT); the drift guard on denormalised data alerts on divergence (L533, MAINT).
- **Rejected**: averages as the latency measure: never (L384). Alerting on every cause: never as pages (L386).
- **Realizes**: refines TRANSVERSE.OPERABILITY; supplies the measurements that POSTGRES_FIRST, JOB_HOST and CACHE_STORE name as their triggers (J1) and that RECORD.2's BI path needs.
- **State**: `known | unvalidated: per-role database load; placement triggers as monitored signals`.

## PIG-WEB.TRANSVERSE.OPERABILITY.4 Security Event Log

- **Rows**: L390, L391, L392, L393, L394, L395. Cited: L049, L098, L658.
- **Positions**:
  - Content: when, where, who, what per record (L390); one event vocabulary with category prefixes and ISO 8601 timestamps with offset (L391).
  - Placement: P1 a separate partition or a separate database account used only to write logs, with very restrictive permissions (L392); P2 a central collector in a standard format over secure transport (L392).
  - Protection: read-only copies as soon as possible, every access recorded, origin of external logs verified (L393); synchronised clocks (L394); client events validated and sanitised (L395).
  - Skeleton link: conflicts ACT.4. The security event log stays apart from the business audit trail.
- **Forces**: P2 serves integrity against a compromised application or database owner, at the cost of a collector. P1 in the application database serves simplicity; the database owner can alter it.
- **Decision**: P2, with every content and protection practice.
  - The security event log is written to a central collector outside the application database, in one vocabulary, over secure transport (L391, L392). It is copied to read-only storage as soon as possible, and every access to it is recorded (L393).
  - It records L098's list (J5): validation failures, authentication results, authorization failures, session failures, errors, use of higher-risk functions. Agent authorization failures are included (L658's identity fields).
  - Under MD-03 many authorization refusals happen inside writer functions (GUARD.3) and in Postgres privilege checks. The backend logs each refusal it receives with actor, role and trace id. Postgres's own log (authentication failures, privilege errors, role changes) is shipped to the same collector, which covers the consumers outside a backend: BI, operators, scripts. Inferred.
  - Business history stays in the database (ACT.4); the two records stay apart (L049).
- **Rejected**: P1 inside the application database: acceptable when no collector exists, as a dedicated append-only table written by a log-only role (L392), and only as a stopgap: the owner role can still alter it. Data-change events as the security log: never (ACT.4).
- **Realizes**: conflicts ALLOCATION.ACT.4 (skeleton link), realized as two records kept apart; refines TRANSVERSE.OPERABILITY.1 (J5).
- **State**: `known | unvalidated: database-side refusals reaching the log`.

## PIG-WEB.TRANSVERSE.OPERABILITY.5 Testing

- **Rows**: L396, L397, L398, L399, L400, L567.
- **Positions** (consensus, one MAINT row): lowest level that catches the failure (L396); few end-to-end tests on critical journeys (L397); test code cared for like production code (L398); a real engine of the production kind (L399); a disposable database, each test isolated by a rolled-back transaction (L400); a test that mutates shared data runs in a boundary that never commits (L567, MAINT).
- **Forces**: fidelity and speed. The never-committing boundary serves isolation and safety, at the cost of not exercising commit-time behaviour.
- **Decision**: all six, with L567 adopted as the max (MAINT), and a disposable database for what needs a commit.
  - Every test that touches data runs on Postgres at the production version (L399, L103). It uses a disposable database per run, never production (L400).
  - Each test runs in a transaction that is rolled back (L400). In any shared environment, a mutating test runs in a forced-rollback boundary; a human uses an explicit rollback (L567).
  - Behaviour that only shows at commit cannot be tested inside a rolled-back transaction: serialisation failures and retries, lock waits between sessions, deferred constraints, the outbox and NOTIFY. It is tested with concurrent committing sessions in the disposable database, which is then dropped, never in a shared one (X4; L567 governs shared environments, so this does not breach it).
  - Concurrency tests for the rules GUARD.2 requires (Serializable with retry, locks) are part of the default test suite, not a gap: every invariant GUARD.2 enforces procedurally has a concurrent test (inferred from GUARD.2; J5 OPERABILITY.2).
  - Database tests connect as the consumer role under test, never as the owner (inferred: ROW_SECURITY's "denial tested through the deployed role", L310, generalised to every grant). They cover writer functions, constraints, grants per role, the actor pairing and the refusal of writes without an actor (J5 OPERABILITY.2, ACT.4).
  - Backend product policy and parsing are tested in memory (L042).
  - **Undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database** (not settled here). Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs. Database read functions that receive the verified actor are acceptable when a per-user read rule must hold for two or more backends; their denial tests then run against those functions. Roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted; the suite asserts no stronger guarantee for them.
  - End-to-end tests are few, on critical journeys (L397).
- **Rejected**: mocking the database or another engine: never (L399). Tests on the production database: never (L400). A committing test in a shared environment: never (L567).
- **Realizes**: refines TRANSVERSE.OPERABILITY.2 (J5); tests what GUARD.2, GUARD.3, ACT.1 and ACT.4 place in the database.
- **State**: `known | unvalidated: commit-time behaviour tested in a disposable database; concurrency tests required by GUARD.2; tests run as the consumer role | gap: no row on concurrency testing | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database`.
- **Review fixes**: M2 and X4 (concurrency tests for GUARD.2 part of the default suite, not a gap; the gap kept only for the missing source row); m7 and X1 (one notation for the pending clause; default, fallback and consequence stated).

## PIG-WEB.TRANSVERSE.OPERABILITY.6 Delivery and Configuration

- **Rows**: L247, L248, L249, L250, L251, L403, L404, L405. Cited: L101, L047, L519.
- **Positions**:
  - App construction: explicit factory with injected settings (L247, majority: Flask, FastAPI); Django selects a settings module per deploy.
  - Variables: P1 independent per deploy (L248, Twelve-Factor); P2 grouped into named environments (Django checklist, FastAPI `.env`).
  - Settings loaded once into a typed, validated object at start (L249). Secrets outside source, debug off, the framework's deploy check before release (L250).
  - Non-secret config: P3 environment variables only (Twelve-Factor); P4 reviewed, version-controlled config promoted with the release (Google SRE) (L251, contested; reconciliation inferred).
  - Staged pipeline, fast first stages, thorough later stages (L403). Feature toggles decouple deploy from release; release toggles are short-lived with a removal task (L404). One-time steps run once per release, in one process, before the workers start (L405).
- **Forces**: P4 serves review and reproducibility of behaviour; P3 serves keeping deploy-specific values out of code. P1 serves independent deploys; P2 serves convenience.
- **Decision**: P1 and P4 split by kind of value, and the delivery practices extended to the shared database.
  - Settings: one typed, validated object built at start and injected (L247, L249). With Django, the settings module reads it from the environment (framework choice is PIG-WEB.LOGIC.ENFORCE.5's).
  - Config that changes behaviour (limits, defaults, toggle defaults) is versioned, reviewed and promoted with the release (L251, P4). Deploy-specific values (addresses, credential references) are independent variables per deploy (L248, P1). Secrets come from the store (SECURITY.4). Reconciled from L251's own reconciliation; inferred.
  - Release gates: debug off and the framework's deploy check run in the pipeline (L250).
  - Pipeline stages (L403): first lint, unit tests, the interface drift gate (MD-02) and the catalogue diff (DB_API); then integration on real Postgres and the consumer suites (CONTRACTS.1); then the few end-to-end tests.
  - Migrations: the shared database's migrations are released before any consumer release that depends on them, once, in one process (L405, L519). They stay additive through the window, with removals only in the contract phase once no consumer role uses the old object (L047, J5). "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration (X2; the L517 narrowing, counted at PIG-WEB.DATA.INTERFACE.1). Static assets are collected at build into the artifact (L101), not at release.
  - Toggles: release toggles are short-lived, each with a removal task created with it (L404).
- **Rejected**: P2 named environment groupings: acceptable for local development files (inferred). P3 for behaviour config: acceptable when that config never changes between releases of the same build (inferred). Schema changes run by each backend's deploy: never under MD-03 (one owner of the database, L515).
- **Realizes**: refines TRANSVERSE.OPERABILITY.3 (J5: database changes inside the pipeline); rests on RECORD.2, RECORD.3, DB_API, MD-02.
- **State**: `known | conflict: L251 contested, reconciled by kind of value | unvalidated: migration release order across separately deployed consumers`.
- **Review fixes**: M1 and X2 (lockstep condition stated word for word; the narrowing realized here is cited, not counted).

## PIG-WEB.TRANSVERSE.TOPOLOGY Runtime Topology

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its four children. One buffering reverse proxy is the only public entry, terminating TLS. A WSGI server with sync workers runs under a process manager by default; routes that make blocking external calls in the request (the identity provider's code exchange at login included) run with threaded workers or on the ASGI process type, or carry a short timeout; ASGI serves long-lived connections. Web and worker processes come from the same image, under a supervisor, as an unprivileged account. Static assets are built once, fingerprinted and served outside Python, with a CDN added on a measured need.
- **Realizes**: refines LOGIC.PROCESS (J3: stateless disposable processes, proxy in front, process types, supervisor); through TOPOLOGY.2, JS_SERVER.
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: worker line updated after m3.

## PIG-WEB.TRANSVERSE.TOPOLOGY.1 Reverse Proxy Edge

- **Rows**: L134, L135, L136, L137, L138, L139, L140.
- **Positions**:
  - P1 one reverse proxy as the single public entry: nginx, Caddy, Traefik, HAProxy or a cloud load balancer (L134, majority: required for sync workers, advice for ASGI).
  - P2 the ASGI server facing clients directly (Uvicorn can, L134 positions).
  - Consensus: buffer request and response (L135); pass original Host and scheme (L136); trust forwarded headers only from the proxy, app reachable only through it (L137); the framework reads the scheme from the proxy header, which the proxy overwrites (L138); Host validated at proxy and framework (L139); a unix socket on a shared host (L140).
- **Forces**: P1 serves protection against slow clients, one place for TLS and limits, and header hygiene, at the cost of one component. P2 serves one component fewer.
- **Decision**: P1 with every consensus practice, for WSGI and ASGI alike.
  - The proxy is the only public entry; the application listens on a unix socket or a private address (L137, L140; L091, J3).
  - It buffers requests and responses (L135), except on streaming routes (SSE, streamed agent responses), where buffering is turned off so events are not held back (inferred).
  - It sets Host and the forwarded scheme itself, overwriting any client copy (L136, L138). The application trusts forwarded headers only from the proxy's address (L137) and validates Host against its allowed list (L139).
  - It carries TLS (SECURITY.2), compression (TOPOLOGY.4), static files and the outermost request limits (J3, LOGIC.SECURE).
  - Product choice by hosting model. Criteria: full buffering, automatic certificates or a tested ACME client (L143), forwarded-header control. No source ranks them (L134).
- **Rejected**: P2: acceptable only in local development (L091, J3).
- **Realizes**: refines LOGIC.PROCESS (P6: the application never faces the internet).
- **State**: `known | unvalidated: buffering off on streaming routes | gap: proxy-to-app re-encryption across a network hop open (L140)`.

## PIG-WEB.TRANSVERSE.TOPOLOGY.2 Application Server

- **Rows**: L149, L150, L151, L152, L153, L154, L155. Cited: L455, L088.
- **Positions**:
  - P1 WSGI by default; ASGI when the application needs long-lived connections or native async I/O; ASGI hosts WSGI, so the choice is reversible (L149).
  - P2 the whole application on ASGI (the alternative L149 conditions).
  - Server: Gunicorn for WSGI, Uvicorn for ASGI (L150, inferred default). The development server is never production (L151). A parent owns the socket and several workers (L152). Sync workers behind a buffering proxy; threaded or async workers for long blocking calls or streaming (L153). Start at (2 x cores) + 1 and tune (L154). Memory budget: footprint times workers plus database connections, 50 to 90% use (L155).
  - Skeleton link: constrains JS_SERVER (a JavaScript server is one more runtime tier).
- **Forces**: P1 serves fault isolation and simple synchronous code. P2 serves one server for request and connection work; threads and async lose some fault isolation (L153).
- **Decision**: P1 with the consensus practices.
  - WSGI with Gunicorn sync workers serves request and response work (L149, L150, L153). Foreign effects run in workers through the outbox (ACT.2, ACT.3), not in the request, so sync workers fit most of the request path (inferred).
  - Some external calls stay in the request: the code-for-token exchange of GUARD.4's backend-for-frontend login, external reads, and model calls on an agent surface. Routes that make such blocking external calls run with threaded workers or on the ASGI process type, or carry a short timeout (L153: threaded or async workers "for long blocking external calls"; inferred).
  - Long-lived connections (real-time channels, streamed agent responses) run on an ASGI server, Uvicorn (L149, L455). They run as their own process type routed by the proxy, so request work keeps the sync workers' isolation (inferred from L153 and L087). Whether the product needs them is PIG-WEB.INTERACTION's decision.
  - Worker count starts at (2 x cores) + 1 and is tuned by measurement (L154). Memory and connections are budgeted per host (L155). Under MD-03 the connection budget covers every consumer of the database, all backends, BI and operators included; pooling is PIG-WEB.DATA.INTERFACE.2's (inferred link).
  - Workers stop gracefully on SIGTERM (L088, J3). The development server never runs in production (L151).
  - The Python server is the only request-time server runtime. JavaScript runs at build time only (JS_SERVER).
- **Rejected**: P2: acceptable when most routes need native async I/O or long-lived connections, or when the chosen framework runs async end to end (L149). A request-time JavaScript server: rejected by JS_SERVER except under its condition.
- **Realizes**: constrains JS_SERVER (skeleton link); refines LOGIC.PROCESS (process types, disposability); rests on ACT.2 and ACT.3 (foreign effects off the request path) and GUARD.4 (the login's code exchange, in the request).
- **State**: `known | unvalidated: Gunicorn and Uvicorn as defaults (L150); a separate ASGI process type; total connection budget across consumers; worker type or timeout for routes with blocking external calls`.
- **Review fixes**: m3 (routes making blocking external calls in the request, login included, run with threaded workers or on the ASGI process type, or carry a short timeout; inferred).

## PIG-WEB.TRANSVERSE.TOPOLOGY.3 Process Placement

- **Rows**: L156, L157, L158, L159, L160.
- **Positions**:
  - Images: staged builds, non-root, pinned base, minimal context (L156).
  - Replication (L157, contested): P1 a process manager inside the unit (Gunicorn with workers, or Uvicorn `--workers`) for a single server or Compose; P2 one server process per container, replicated by an orchestrator or platform.
  - Supervisor, unprivileged account (L158).
  - Workers: P3 extra units on the web host; P4 separately scaled containers or services (L159, synthesis).
  - Workers and admin processes from the same release image, code, dependencies and config; admin code ships with the application (L160).
- **Forces**: P1 serves crash containment inside a unit without an orchestrator (L152). P2 serves replication and scaling by the platform (one concern per container, L092), at the cost of running an orchestrator. P3 serves simplicity; P4 serves scaling jobs apart from web load.
- **Decision**: the image and supervision practices; P1 and P3 under the assumed hosting.
  - One image per release, multi-stage, non-root, pinned base (L156). Web, worker and admin processes all start from it with the same config (L160).
  - Under the assumed hosting (one or a few self-managed hosts, no orchestrator; questions.md, Q1): each unit runs a process manager with several workers (P1, L152). Workers run as extra units on the web host (P3). A supervisor runs everything as an unprivileged account (L158).
  - Admin consoles and scripts run from the same release image with the operator role's credentials. Migrations and human-run data jobs use the owner role under L545 (J1 access paths; inferred).
  - The choice is recorded per project (L157; EVOLUTION.3).
- **Rejected**: P2: wins when an orchestrator or platform replicates containers; then each container runs one server process (L157). P4: wins when job load differs from web load enough to scale apart, measured (L159).
- **Realizes**: refines LOGIC.PROCESS (process types, supervisor, one concern per container); rests on the J1 access paths (roles per kind of process).
- **State**: `known | conflict: L157 contested, settled by hosting model | unvalidated: hosting assumption (Q1); roles per kind of process`.

## PIG-WEB.TRANSVERSE.TOPOLOGY.4 Static Assets and CDN

- **Rows**: L161, L162, L163, L164, L165, L166, L167. Cited: L009, L101.
- **Positions**:
  - Where to serve (L161, majority): P1 from the proxy on the application host; P2 a dedicated static server; P3 object storage behind a CDN; P4 in-app (WhiteNoise-style) behind a CDN (L164, single T3).
  - Consensus: collect into one directory, serve outside Python request handlers (L162); hashed file names rewritten inside CSS and JS (L163); compress at proxy or CDN (L167).
  - CDN: optional, added for distant users or origin load (L165, threshold inferred); long-term caching of fingerprinted files, seconds-long micro-caching of anonymous dynamic responses, hit ratio watched (L166).
- **Forces**: P1 serves simplicity on one region. P3 serves distant users and origin load, at the cost of another service. P4 serves platforms without a proxy, and needs a CDN in front.
- **Decision**: P1 by default, with fingerprinting, compression and a kept asset history.
  - Assets are built and collected once into the release artifact (L101, L162), with fingerprinted names (L163). The proxy serves them with long-lived immutable caching and compression (L166, L167).
  - Fingerprinted files of previous releases stay available for the compatibility window, as long as an old page can stay open (L009, J4 hand-off). The asset store is cumulative across releases and pruned after the window (inferred).
  - A CDN is added when users are distant or origin load justifies it (L165). It caches fingerprinted files for the long term. It micro-caches only anonymous responses carrying no nonce and no personal data (L166; SECURITY.3; J4).
- **Rejected**: P3: wins when users are geographically distant or origin load is measured too high (L165). P4: acceptable on a platform without a proxy, always behind a CDN (L164). Serving static files through Python handlers without a CDN: never in production (L162).
- **Realizes**: refines LOGIC.PROCESS through TOPOLOGY; realizes J4's hand-offs from INTERACTION.ENVIRONMENT.3 and .4.
- **State**: `known | unvalidated: cumulative asset store across the compatibility window; CDN threshold (L165)`.

## PIG-WEB.TRANSVERSE.EVOLUTION Evolution Defaults

- **Rows**: none (roll-up).
- **Decision**: the roll-up of its three children. Several backends may share the database (MD-03); each backend is one deployable, not split into services without a measured need. The team's Python backend is one deployable over the shared database, with the schema and function API as the database owner's codebase. The backend is modular by business concept, its modules aligned with domain schemas and their boundaries checked automatically: no module touches another domain's tables, every module may call the function API within its role's grants, and a cross-domain business operation is one database function. Every architecturally significant decision, the per-project ones the guideline leaves open included (HSTS preload among them), is a short ADR, superseded and never edited.
- **Realizes**: refines TRANSVERSE.EVOLUTION (J5).
- **State**: `known | gap: owns no row (roll-up)`.
- **Review fixes**: updated after B1 (X3), M3 (X5) and M6.

## PIG-WEB.TRANSVERSE.EVOLUTION.1 Deployables

- **Rows**: L113, L114, L115, L116, L117, L118, L119, L120, L121.
- **Positions**:
  - P1 one deployable first; split only on proven boundaries when the single unit is the bottleneck (L113, L114, L115, L116; majority).
  - P2 services from the start when the domain is well known, the size needs distribution, and the parts develop and deploy independently (L117, Tilkov, contested).
  - P3 consolidating services back is legitimate when operating cost grows with their number (L118, one T3 case).
  - P4 replace at seams, never by big-bang rewrite (L119).
  - P5 a Backend for Frontend only when aggregation or divergent clients justify it; with one browser client over one backend, the backend already is the BFF; an agent surface can be another client (L120).
  - P6 micro frontends only when several teams are blocked by one frontend; server-rendered teams compose on the server (L121).
- **Forces**: P1 serves changeability while the domain is unknown and saves the distribution premium (J5). P2 serves team independence on a known domain. P5 and P6 serve divergent clients and many teams, at the cost of more pipelines.
- **Decision**: P1, P3, P4; no BFF and no micro frontends by default.
  - Several backends may share the database (MD-03). Each backend is one deployable; it is not split into services without a measured need (X5, J5 EVOLUTION.3). The team's own backend is one Python deployable over the shared database; MD-03's several backends do not by themselves license splitting it. The schema and function API are the database owner's codebase and pipeline (J5 OPERABILITY.3).
  - A further deployable is split only when size, complexity or the number of teams make the single unit the bottleneck, on a proven boundary (L113, L114). It reaches the data through the function API with its own role (RECORD.2) and never holds a second system of record (RECORD.1).
  - Because the data seam is already the function API, such a split moves no data; only deploy independence and the distribution premium remain to be weighed (J5 EVOLUTION.3; inferred).
  - Likely future services get their own domain schema now, not their own database (L116 read with MD-03 and L513; J5).
  - No BFF deployable: the backend is the browser's BFF. The agent surface is another client of the same core (L120; RULES.4). Whether it needs its own process type is PIG-WEB.INTERACTION.AGENT's decision.
  - No micro frontends; server-side composition if teams multiply (L121). No request-time JavaScript server (JS_SERVER).
  - Replacement at seams (L119). Consolidation is legitimate when operating cost grows with the number of services (L118).
- **Rejected**: P2: acceptable when all of L117's and L115's conditions hold (known domain, size, independent deploys, operational maturity). A BFF: wins with mobile and web clients or heavy aggregation (L120). Micro frontends: win when several teams are blocked by one frontend and can carry the extra pipelines (L121).
- **Realizes**: refines TRANSVERSE.EVOLUTION.3 (J5); rests on RECORD.1, RECORD.2, RULES.4, JS_SERVER.
- **State**: `known | conflict: L117 (services first) contested, rejected as default | unvalidated: future services as domain schemas (MD-03); a split moves no data`.
- **Review fixes**: M3 and X5 ("one Python backend deployable" replaced: several backends may share the database, each backend one deployable, not split into services without a measured need; a later split moves no data, inferred).

## PIG-WEB.TRANSVERSE.EVOLUTION.2 Modular Monolith

- **Rows**: L122, L123, L124. Cited: L513, L596.
- **Positions** (no opposing position): modules by business concept with public interfaces (L122); boundaries enforced by automated checks (L123, inferred); framework layers loosely coupled, each concept or datum in one place (L124).
- **Forces**: changeability and future extraction, at the cost of boundary tooling.
- **Decision**: all three, aligned with the database's domains.
  - The backend is cut by business concept (orders, billing), each module with a public interface (L122).
  - The module boundary forbids reaching another domain's **tables** directly. The function API is reachable from every module, within its role's grants, the same as for a backend in another language (RECORD.2). Inferred, `unvalidated`.
  - One business operation is one database function call in its own transaction (J1 R1-4); backends never compose several calls into one operation. A database function may call another domain's published functions inside the same transaction: composition across domains happens in the database. What is forbidden across domains is direct access to another domain's tables, not calling its published functions (X3).
  - A cross-domain business operation (for example an order that also creates an invoice) is therefore one database function. It is called by the module that owns the workflow and owned by the team that owns that workflow, reviewed by the cross-schema owner role (J5 EVOLUTION.5).
  - The Python module interface carries workflow and product policy, never a second path to another domain's data.
  - Module boundaries are checked automatically in the pipeline, as a fitness function (L123, L110): the check fails on a direct read or write of another domain's tables. The tool is open (gap).
  - One place per concept (L124). A business operation lives in its database function; the Python module holds workflow and product policy, with only tested copies of per-user write rules (ACT.1, J1).
- **Rejected**:
  - Modules by technical layer: never (L122). Boundaries by convention alone: never (L123).
  - A module reaching another domain's data only through that module's Python interface: rejected. A business operation that writes two domains would then need two calls, either in two transactions (atomicity lost) or in one backend transaction wrapping several API calls, which ACT.1 forbids (MD-03). It would also give a backend in another language more reach than a module of the team's own backend.
- **Realizes**: refines TRANSVERSE.EVOLUTION.2, .3 and .5 (J5); rests on ACT.1 (one call per operation, operations in the database, workflow in the backend), RECORD.2 (function API per role) and MD-03.
- **State**: `known | unvalidated: modules aligned with domain schemas; the module rule (tables forbidden, function API reachable within grants) | gap: no module-boundary tool read (L123)`.
- **Review fixes**: B1 and X3 (the rule forbids another domain's tables only; the function API, cross-domain operations included, is reachable from every module within its role's grants; cross-domain operations are one database function owned per J5 EVOLUTION.5; the rule marked unvalidated).

## PIG-WEB.TRANSVERSE.EVOLUTION.3 Decision Records

- **Rows**: L129, L130, L131, L132, L133.
- **Positions** (consensus, one majority): one short ADR per architecturally significant decision (L129); title, context, decision, status, consequences (L130); in the repository, lightweight markup, numbered (L131); never edited once accepted, superseded (L132); serious alternatives with pros and cons and the confidence (L133, majority).
- **Forces**: shared understanding of costly decisions (J5 EVOLUTION.1), at the cost of writing them.
- **Decision**: all five, in the form J5 requires.
  - One ADR per significant decision, one to two pages, in the repository it governs, numbered, in Markdown (L129, L131). Decisions binding every consumer of the shared database live with the database's codebase (inferred).
  - Fields: context with forces, decision, status, consequences (L130), the alternatives with pros and cons, the confidence (L133), and the condition that would reverse it (J5 EVOLUTION.1).
  - Accepted ADRs are never edited, only superseded (L132).
  - The guideline leaves these decisions to each project, and each gets an ADR:
    - the interface origin direction (MD-02);
    - row-level security under MD-01's three conditions;
    - the ASVS level (SECURITY.1);
    - secret delivery (SECURITY.4);
    - process replication (TOPOLOGY.3);
    - the CDN (TOPOLOGY.4);
    - HSTS preload, under its condition (SECURITY.2);
    - adding a managed secret store under the assumed hosting (SECURITY.4);
    - a build platform held at SLSA Build L2 rather than L3 (SECURITY.5);
    - every move of a Postgres-first role past its measured limit (J1).
- **Rejected**: decisions kept only in code or chat: never (L105, J5). Editing an accepted record: never (L132).
- **Realizes**: refines TRANSVERSE.EVOLUTION.1 (J5).
- **State**: `known`.
- **Review fixes**: M6 (HSTS preload added to the per-project ADRs); with M5 and m6, the L2 build-level exception and the secret-store addition, which those fixes make per-project decisions.

## PIG-WEB.TRANSVERSE.OPERABILITY.7 Incident Response [deferred]

Not judged: deferred in the skeleton (scope out, recorded only).
