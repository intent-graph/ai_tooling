# Maintainer questions: the 24 undecided nodes

Each undecided node of the two skeletons (`skeleton.md`) is one question below. A question gives the decision, a recommendation, and what the graph records if nobody answers, then the positions with their best sources. Ledger ids (`L…`) point to `claims_ledger.md`, source ids (`SRC-…`) to `sources.md`. Questions are batched by shared context; answering one question in a batch often settles part of the next.

Round 3: the maintainer's codified practice (MAINT, source MAINT-S01) carries the maintainer's authority but was written for one context. Where it contradicts the research, the question states the doctrine first, then the research position and the condition under which each applies, and the maintainer confirms; nothing is settled here.

Scope used for every recommendation: a classic website (browser with JavaScript, Python application server, Postgres), single team, single tenant (brief_shared round-2 scope). A recommendation is marked *grounded* when a T1/T2 source states it and *inferred* when it is my synthesis.

Pinned:
- Undecided nodes: 24 (1 in `web-app-philosophy`, 23 in `pig-web-defaults`), so 24 questions in 9 batches (round 3 added H1, H2, I1, I2).
- Maintainer doctrine contradictions: 5, each turned into a question that states the doctrine first, then the research position and the condition for each: MAINT-C17 and MAINT-C44 in C2; MAINT-C41 and MAINT-C43 in C3; MAINT-C18 in D2. D1 is revised with the doctrine's extension (no contradiction).
- Default when unanswered, for every question: the node stays `undecided`, every position goes to its design_notes, and nodes that depend on it record their rules as conditional on the answer. No default is silently chosen.
- Contested-labelled claims not raised as questions: 5 (appendix).

## Batch A: what crosses the wire (contract style, rendering, evolution)

A1 decides the rest of this batch: if the default is server-rendered HTML, A3 to A5 shrink to edge cases.

### A1. Default contract style: `PIG-WEB.CONTRACT.STYLE` (L252-L257)

- **Decision:** by default, does the browser receive server-rendered HTML (hypermedia, optionally enhanced with partial HTML updates) or JSON rendered by a client application?
- **Recommendation:** server-rendered HTML as the default, with a rich client (JSON) chosen per page or feature only when the agreed conditions of L253 hold (many interdependent UI states, offline use, very high update frequency, real-time collaboration). Inferred: both camps agree on these conditions (L253; SRC-288, SRC-319); a classic website is text, forms and CRUD, which is the case where the conditions do not hold; the philosophy's progressive-enhancement principle (L003) and few-technologies principles (L081-L085) point the same way.
- **If nobody answers:** the node records both defaults and the agreed trigger conditions; UI.RENDERING.2, CONTRACT.EVOLUTION.1 and .2, SEC.SESSION.1 and APP.FRAMEWORK keep their rules conditional on the style.
- **Positions:**
  - Server HTML default: htmx maintainers (SRC-288, T3), Turbo handbook (SRC-284, T3), Hypermedia Systems (SRC-282, T3), MacWright (SRC-321, T4).
  - Client-app default: React docs present the SPA as the default architecture of most build tools (SRC-306, T3); hybrid server-first with client components: React Server Components and Next.js (SRC-305, SRC-292, T3).
  - Neutral platform guidance: web.dev Rendering on the Web (SRC-181, T1) and MDN SPA glossary (SRC-076, T1) list costs of each and state no default (L254).
  - Side positions inside the node: GraphQL as a third option (L256, advocate source only); transitional apps mixing both (L255, secondhand T4 report); in a hypermedia design the HTML is the contract and OpenAPI covers only JSON endpoints (L257, inferred).

### A2. Strict hypermedia as a principle: `CONTRACT.HYPERMEDIA` (philosophy, L059-L061)

- **Decision:** must server-provided representations drive every client transition (Fielding's strict REST), or is a documented, fixed URL contract an acceptable principle?
- **Recommendation:** state hypermedia-driven interaction as the principle for the HTML surface (links and forms already drive the browser), and accept documented fixed contracts for whatever JSON endpoints exist, named honestly as resource-oriented HTTP (level 2), not REST (L060, consensus). Inferred: the strict reading buys independent evolution over decades at an upfront cost (L059, SRC-245, SRC-244, T2), a cost a single-team site with a first-party client does not need to pay.
- **If nobody answers:** the principle node stays undecided with both readings; only A1 depends on it, and A1's recommendation does not need A2 answered.
- **Positions:** strict hypermedia: Fielding's dissertation and 2008 post (SRC-244, SRC-245, T2). Documented fixed URL hierarchies: common API practice and the Google, Zalando and Azure guidelines, which design level-2 APIs (SRC-203, SRC-255, SRC-238, T2; L264). Uniform-interface trade-off agreed by all (L061).

### A3. A JavaScript server tier: `PIG-WEB.UI.RENDERING.2` (L288-L290)

- **Decision:** may a request-time JavaScript rendering server (an SSR meta-framework on Node) sit beside the Python server, or does rendering stay in Python plus build-time output?
- **Recommendation:** no request-time JavaScript tier by default; render in Python and at build time; add the tier only if A1 chooses a client-app default and first-load or crawlability needs then require server rendering, and record it as an extra deployable (SHAPE.DEPLOYABLES). Inferred: static export or build-time rendering avoids the tier (L288, SRC-293, T3); no source weighs the operational cost of the extra tier; the few-technologies principles (L081-L085) and the round-1 coverage check (item 17) tie the two.
- **If nobody answers:** the node stays undecided; the rules that apply whenever a server/client code boundary exists (L289: mark it, keep secrets server-side) and when a React client app is chosen (L290: use a framework) remain recorded.
- **Positions:** framework docs treat the Node server runtime as normal (SRC-305, SRC-292, T3); hypermedia sources keep logic in one server language (SRC-282, SRC-284, T3).

### A4. Version identifier placement: `PIG-WEB.CONTRACT.EVOLUTION.1` (L276)

- **Decision:** when a breaking change is unavoidable, where does the version identifier go: URL path, query parameter, media type, date header, or nowhere?
- **Recommendation:** none while the only consumer is the site's own browser client: evolve additively (L056, consensus) and handle skew (A5); if a JSON API gains external consumers, put a major version in the URL path. Inferred: versioning is the exception by consensus (L056); the URL-path choice is Google's MUST (SRC-203, T2) and the most visible form, but no source ranks the five positions for this case.
- **If nobody answers:** the node lists the five positions; the additive-evolution and deprecation rules (L273-L275, L547) apply regardless.
- **Positions:** URL path major version: Google AIP-185 (SRC-203, T2). Required api-version query parameter: Azure (SRC-238, T2). Media type, URL versions prohibited: Zalando (SRC-255, T2). Date in a request header, account pinned: Stripe, GitHub (SRC-309, SRC-276, T3). No versions: GraphQL (SRC-281, T3).

### A5. Version skew policy: `PIG-WEB.CONTRACT.EVOLUTION.2` (L277-L278)

- **Decision:** how is old browser code kept working against a new server: a compatibility window only, versioned API paths, or routing each client to the server version that served its page?
- **Recommendation:** a compatibility window: every release keeps accepting requests from the previous release's client (additive changes, tolerant readers), and the previous release's fingerprinted assets stay available. Inferred: the problem is consensus (L009, SRC-290, T3; Fielding SRC-244); the cure is Ubl's list, each item with a cost; routing to matching deployments needs platform support that was seen only in search snippets (L277). The window length (one release, N days) is open.
- **If nobody answers:** the node lists the three mitigations; the inferred practice of keeping first-party API changes additive across the window (L278) stays recorded as open.
- **Positions:** compatibility window plus tolerant clients plus either versioned paths or deployment routing, each with a cost (Ubl, SRC-290, T3); deployment-layer skew protection when one team owns both sides (hosting vendors, not read).

## Batch B: browser identity (where credentials live)

B2 only matters if B1 lets tokens reach the browser.

### B1. Browser authentication model: `PIG-WEB.SEC.SESSION.1` (L313-L318)

- **Decision:** does the first-party browser authenticate with an opaque server-side session in a cookie (directly, or through a backend-for-frontend when an external identity provider is used), or with bearer tokens held by script?
- **Recommendation:** an opaque server-side session in a hardened cookie, built with the framework's session management, on the site's own origin; a backend-for-frontend when login is delegated to an external OAuth or OpenID provider; bearer tokens only for non-browser clients (L316). Grounded: the IETF browser-apps BCP, now RFC 10017 (SRC-042, T1; L313), OWASP session and HTML5 sheets (SRC-119, SRC-107, T1), Django docs (SRC-021, T1); Degges (SRC-303, T3) adds that statelessness buys little for an ordinary site (L315).
- **If nobody answers:** the node lists both models; the cookie and lifecycle rules of SEC.SESSION.3 and the CSRF rules of SEC.BROWSER.1 apply whenever cookies are used.
- **Positions:**
  - Server-side session or BFF cookie: SRC-042, SRC-210 (draft, T2), SRC-119, SRC-107, SRC-021 (T1), SRC-303, SRC-275 (T3, vendor).
  - Bearer JWT for the browser: FastAPI's tutorial path (SRC-039, T1; it does not address cookies, sessions or revocation, L317), Auth0 (SRC-258, T3, vendor). No T1/T2 source argues for a stateless JWT as a first-party browser session.
  - Fielding: cookie-held application state "will never be reliable" (L318, SRC-244, T2), a purist objection to any cookie session.

### B2. Tokens in the browser: `PIG-WEB.SEC.SESSION.2` (L319-L321)

- **Decision:** if any token reaches the browser, where is it kept: nowhere script can read, in memory, or in localStorage with cross-site-scripting prevention as the real control?
- **Recommendation:** nowhere script can read; with B1 answered as recommended, record this node as "no tokens in the browser". Grounded: OWASP (SRC-107, SRC-119, T1; L319); all three camps agree that malicious script holds the page's privileges, so XSS defeats any storage choice (L024).
- **If nobody answers:** the node lists the three positions; L319 stays recorded as majority with its dissents.
- **Positions:** never JavaScript-readable storage: OWASP (T1), relabelled majority by the counter-voices slot. In memory or a Web Worker: Auth0 (SRC-258, T3, vendor). Storage location is secondary, prevent XSS, localStorage acceptable when unsure: De Ryck (SRC-299, T3 practitioner).

## Batch C: how much Postgres does

### C1. Backing services: `PIG-WEB.SHAPE.BACKING` (L125-L127)

- **Decision:** does Postgres alone serve as job queue and notification source until a measured limit, or are a broker and a separate cache adopted from the start?
- **Recommendation:** Postgres first for the job queue (jobs staged in a table in the same transaction, claimed with SKIP LOCKED) and for wake-up notifications, with the trigger to add a broker or Redis written down as measured lock contention on the queue table or commit serialization from NOTIFY. Two consensus claims already name a shared store elsewhere and stay as they are: a multi-process application cache must be shared (L417), and cross-process fan-out in Django Channels needs Redis (L457). Inferred: the few-technologies principles are consensus (L081-L085, T2/T3); SKIP LOCKED for queue tables is T1 (SRC-151); the "Postgres for everything" rule itself has only T4 backing (SRC-320, SRC-322) and the limits only T3 evidence (SRC-266, SRC-307). The maintainer doctrine supports Postgres first: derived-data caches live in database tables (L534) and scheduled database work runs inside the database (L604).
- **If nobody answers:** the node lists the positions; MECH.JOBS and MECH.REALTIME.5 stay store-agnostic, their delivery rules (CONSISTENCY.DELIVERY: outbox, idempotent consumers; NOTIFY as signal only) apply either way.
- **Positions:** database queue at low volume (PostgreSQL docs, SRC-151, T1); staged drain to a broker when load grows (Brandur, SRC-266, T3); broker from the start (FastAPI and Flask docs point to Celery with Redis or RabbitMQ, SRC-029, SRC-125, T1); one Postgres for queue, cache, search and documents (SRC-320, SRC-322, T4); NOTIFY commit serialization under write concurrency (one postmortem, SRC-307, T3; no threshold).

### C2. Logic in the database: `PIG-WEB.DATA.LOGIC` (L214-L217, L527-L530)

Contradictions settled here by the maintainer: MAINT-C44 (L528) against L215 and the round-2 recommendation; MAINT-C17 (L529) against L216.

- **Decision:** beyond declared constraints, how much logic lives in the database (functions, triggers), and who writes `updated_at`?
- **Doctrine (maintainer, MAINT-S01):**
  - The default is a plain query in application code. A database function exists only when it earns its cost by one of four reasons: reuse by two or more consumers; hiding internals behind a business verb; performance the database owner must tune independently; integrity beyond schema constraints (L527).
  - Past that gate, these live in database functions: cascades mirroring foreign keys, multi-table validation that must be atomic, integrity beyond constraints, operations shared by several backends, and set-based algorithms over large data. Presentation, sessions, workflow orchestration and external calls stay in the application (L528).
  - The costs are stated as inputs (L472) and the functions follow conventions (L530).
  - `updated_at` is written by the code that updates the row, not by a trigger, and unchanged rows are skipped (L529).
- **Research position:** domain logic and workflow in the application, the database for invariants, and triggers only for narrow documented cases, `updated_at` included (L214-L216; Fowler SRC-224, T2; Brandur SRC-264, T3). Before the doctrine, the heavier-database band had T4 support only.
- **When each applies (inferred):**
  - The doctrine fits a database shared by several consumers (its first reason) and a team fluent in SQL; team skill is a legitimate input (L041).
  - The research split fits one Python application owning its database with a Python-centric team.
  - The writer-sets-`updated_at` rule needs every write to go through one path (the single-writer rule, L596); a trigger fits when many code paths write directly.
- **Recommendation:**
  - Record the doctrine's four-reason gate as the rule; it already agrees with the research on the application-first default.
  - Record the in-database band and writer-set `updated_at` as the doctrine's practice, applying when the gate's reasons hold.
  - Keep the research split as the reading for a single-owner application.
  - The maintainer confirms the doctrine as the unconditional default, or this conditional reading.
- **If nobody answers:** the node stays undecided with the doctrine and the research split side by side; the philosophy node DATA.INTEGRITY (database guards invariants) binds both, with the doctrine noted as a conflict there.

### C3. Database contract surface and ownership: `PIG-WEB.DATA.ACCESS.2` (L187-L188, L515-L518)

Contradictions settled here by the maintainer: MAINT-C41 (L515) against L044, the philosophy principle "one application owns its database" (node `DATA.OWNERSHIP`, now annotated with this conflict); MAINT-C43 (L516) against the view half of L187.

- **Decision:** does the database serve one application through its base tables, or several backends through a contract surface, and are views part of that surface?
- **Doctrine (maintainer, MAINT-S01):**
  - One database serves several backends, in different languages, through a function API. The signature is the contract; the body belongs to the database owner, who can rewrite or re-plan it without redeploying consumers (L515).
  - Views are excluded, because consumers bind to their exact shape. Base tables stay queryable for simple reads. The tool ladder is query, then function, then procedure (L516).
  - The function API evolves additively, with coordinated breaking changes and no version numbers (L517).
- **Research position:** one application owns its database, and others reach the data through its service or a reporting copy (L044; Fowler SRC-216, SRC-215, T2; consensus). Where several consumers or strict privilege separation exist, a contract schema of views and functions (L187; PostgREST SRC-355, T3, L518). For a single owner, base tables through the ORM.
- **When each applies (inferred):** the doctrine applies when several backends must share one database and an owner role for the database exists; the research applies to a single application owning its database, which is the classic-website case and one on which the doctrine is silent.
- **Recommendation:**
  - Record the doctrine's function contract, views excluded, as the rule whenever two or more consumers share the database.
  - Keep base tables through the ORM for a single owner.
  - The maintainer confirms one of two wordings for the philosophy principle: L044 kept as stated, with the doctrine as its multi-consumer exception; or L044 rewritten to "one owner of the schema, possibly serving several backends through a function contract".
- **If nobody answers:** DATA.ACCESS.2 stays undecided; DATA.OWNERSHIP stays known with the conflict annotation.

## Batch D: data modelling defaults

### D1. Primary key shape and type: `PIG-WEB.DATA.SCHEMA.3` (L179, L499-L504)

No contradiction; the doctrine extends the research.

- **Decision:** which key shape and type the schema uses by default.
- **Doctrine (maintainer, MAINT-S01):**
  - Identity columns, not serial (L502), sized by expected cardinality: a 4-byte integer under about two billion rows, 8-byte for very large tables or keys referenced by large tables, and the same type on both sides of every relationship (L503).
  - Tables scoped to a parent get a composite key that leads with the scope column, at most about four columns (L499-L501).
  - UUIDs only for global uniqueness, external integration or sequence contention; a deterministic UUID can be derived from a composite natural key (L504).
- **Research position:** bigint identity by default, UUIDv7 for keys exposed in public URLs where enumeration matters, not UUIDv4 (L179; SRC-138, SRC-154, T1; locality benchmarks T4).
- **Differences:** default width (sized by cardinality versus always bigint); composite scope-leading keys (the research is silent); UUIDv7 and enumeration (the doctrine is silent). The doctrine's own rationale tying key shape to soft deletion is weak (its tension 1).
- **Recommendation:** record the doctrine's rule (identity sized by cardinality, composite for scoped tables, UUID only with a stated reason); the maintainer decides whether keys exposed in public URLs take UUIDv7, a point the doctrine does not cover.
- **If nobody answers:** the node lists the doctrine and the research options; L178 (never use a UUIDv7 timestamp as the creation time) applies either way.

### D2. Deletion strategy: `PIG-WEB.DATA.LIFECYCLE.1` (L204-L205, L520-L525)

Contradiction settled here by the maintainer: MAINT-C18 (L520) against L204 and the round-2 recommendation.

- **Decision:** soft delete, hard delete plus an archive written in the same transaction, or hard delete only, and which is the default?
- **Doctrine (maintainer, MAINT-S01):**
  - Deletion follows a per-table gradient by retention need (L520).
  - Soft delete is the default for user-facing transactional data, marked by a nullable timestamptz `deleted_at` with partial indexes over active rows (L521).
  - The five mitigations:
    - constraints and uniqueness exempt deleted rows (L522);
    - cascades shadow the foreign-key graph in dedicated functions (L523);
    - delete functions are idempotent and polyvalent (L524);
    - hard deletion only for rebuildable caches or after an archive copy (L525);
    - no DELETE privilege for application roles (L525).
- **Research position:** decide per entity (L205); otherwise hard delete plus a same-transaction archive, with soft delete only where the product itself offers undo. One critique (Brandur, SRC-265, T3) names the costs: the predicate leaks into every query, foreign keys stop protecting, and a legal purge gets harder. No defender was read; the doctrine is that defender, with the mitigations the critique says are missing.
- **When each applies (inferred):** the doctrine's default holds where its mitigations are in place (all deletes through functions, no DELETE grants, partial indexes and check escapes). Hard delete plus archive fits an application deleting through an ORM, without a function layer to contain the predicate leak.
- **Recommendation:** record the doctrine's soft-delete default with its five mitigations as its conditions, and hard delete plus archive where they are not in place; the maintainer confirms.
- **If nobody answers:** the node lists both strategies and the per-entity rule.

## Batch E: Python application shape

### E1. Web framework: `PIG-WEB.APP.FRAMEWORK` (L242)

- **Decision:** Django, FastAPI or Flask?
- **Recommendation:** conditional on A1: Django when the default is server-rendered HTML (its sessions, CSRF, forms, ORM, migrations, static-file pipeline and deployment checklist are the T1 sources behind many defaults in this graph); FastAPI when the default is a JSON API; Flask not for large or async applications, by its own statement. Inferred: each framework's docs state its own niche (SRC-009, SRC-124, SRC-031, T1); no neutral T1/T2 selection criteria exist.
- **If nobody answers:** the node lists the three self-descriptions; framework-specific practices in the graph (Django sessions, CSRF, static storage; FastAPI settings, UploadFile) stay marked as conditional on the framework.
- **Positions:** Django: batteries included, Active Record models (SRC-009). Flask: micro, no database layer, "not designed for large applications or asynchronous servers" (SRC-124). FastAPI: ASGI, dependency injection, def and async def (SRC-031).

### E2. Domain model and ORM: `PIG-WEB.APP.LAYERS.2` (L227)

- **Decision:** decouple the domain model from the ORM behind repositories, or use ORM models as the domain?
- **Recommendation:** ORM models as the domain behind a use-case layer (L224) for a CRUD-shaped site, moving a module to repositories when its domain logic becomes complex. Grounded: Cosmic Python itself says CRUD-focused applications do not require domain models or repositories (SRC-243, T2); layering scales with complexity (L226, consensus).
- **If nobody answers:** the node lists both with the complexity criterion.
- **Positions:** decouple with repositories (Cosmic Python, SRC-243, T2); models carry the domain logic (Django, SRC-009, T1); ORMs handle most mapping better than home-grown code (Fowler, SRC-195, T2).

### E3. Replication location: `PIG-WEB.TOPOLOGY.PROCESSES.1` (L157)

- **Decision:** are server processes replicated by a process manager inside the unit or by an orchestrator running one process per container?
- **Recommendation:** decide by hosting model and record it; for the expected single host or Compose deployment of a classic website, a pre-fork process manager in the unit (Gunicorn, with Uvicorn workers if ASGI). Grounded as a conditional rule in the tool docs (SRC-161, SRC-035, SRC-040, T1); the hosting assumption is inferred.
- **If nobody answers:** the node records the conditional rule (single server or Compose: manager in the unit; orchestrator: one process per container).
- **Positions:** Gunicorn with Uvicorn workers (Uvicorn docs, SRC-161); Uvicorn's own --workers (same); one process per container, replicated by the cluster (FastAPI docs, SRC-035; Docker one-concern rule, SRC-028).

## Batch F: configuration and secrets (Twelve-Factor versus managed configuration)

### F1. Configuration storage: `PIG-WEB.APP.CONFIG.2` (L251)

- **Decision:** does non-secret configuration live only in environment variables, or in reviewed, version-controlled files promoted with the release?
- **Recommendation:** the reconciliation stated with the claim: non-secret configuration may live in reviewed version control and be promoted with the release; values that differ per deploy come from the environment; secrets never in the repository. Inferred (L251) from Twelve-Factor (SRC-183, T2) and Google SRE release engineering (SRC-204, T2).
- **If nobody answers:** the node lists both; the delivery principle (configuration separate from code, the open-source test, L102) binds either way.
- **Positions:** environment variables only (Twelve-Factor, SRC-183); reviewed configuration in source control, packaged or external for dynamic values (SRE, SRC-204).

### F2. Secret storage: `PIG-WEB.SEC.SUPPLY.1` (L350)

- **Decision:** do runtime secrets live in environment variables, or are they injected from a secrets manager?
- **Recommendation:** inject secrets at runtime from a managed store (the hosting platform's secret store or a secrets manager), keeping plain environment files for local development only. Grounded: OWASP prefers runtime injection from a managed store and warns that environment variables are visible to many processes (SRC-118, T1), and centralized, rotated, audited storage is consensus (L351); Twelve-Factor's environment variables are T2.
- **If nobody answers:** the node lists both; secret handling (L351-L353) and "never in source" (L102) apply either way.
- **Positions:** environment variables (Twelve-Factor, SRC-183, T2); managed store with runtime injection (OWASP, SRC-118, T1).

## Batch G: optional cross-tier mechanisms

These matter only for projects that adopt the mechanism.

### G1. Real-time channel: `PIG-WEB.MECH.REALTIME.1` (L436-L442)

- **Decision:** which channel serves server-to-client push by default: polling, server-sent events or WebSocket?
- **Recommendation:** the order of L437: no real-time; polling for slow-changing views; SSE for one-way push; WebSocket only for true two-way traffic. Inferred: SSE fits when the path to the user is under the team's control, which the single-origin, own-proxy topology provides; the case for WebSocket first rests on one T4 vendor source (SRC-317); mechanics are T1 (SRC-043, SRC-182, SRC-044).
- **If nobody answers:** the node lists both defaults and the majority order of L437 as inferred.
- **Positions:** SSE first (Railway guide, SRC-302, T3); WebSocket first, because intermediaries may buffer SSE (Ably, SRC-317, T4 vendor).

### G2. Upload path: `PIG-WEB.MECH.FILES.1` (L421-L424)

- **Decision:** do file bytes go from the browser directly to object storage under a short-lived credential, or stream through the application?
- **Recommendation:** through the application for small files that need synchronous validation (the common case of a classic website), direct-to-storage with a constrained POST policy for large or numerous files; the size threshold stays open. Inferred: no source weighs the two (L421); OWASP and framework docs describe the through-the-app path (SRC-106, SRC-027, T1), vendor docs the direct path (SRC-262, SRC-261, T3).
- **If nobody answers:** the node lists both; intake, storage and serving rules (MECH.FILES.2 to .4) apply to both paths.
- **Positions:** direct to storage (AWS docs, T3); through the application (OWASP, Django, FastAPI docs, T1).

### G3. Quota headers: `PIG-WEB.SEC.ABUSE.3` (L367-L368)

- **Decision:** advertise remaining quota with the IETF RateLimit draft fields, with de facto X-RateLimit headers, or not at all?
- **Recommendation:** none: 429 with Retry-After only (RFC 6585 baseline) while clients are the site's own pages; adopt the IETF fields if a programmatic API with third-party clients appears and the draft is published. Inferred: browsers do not act on quota headers; 429 is T1 (SRC-045); the IETF fields are a T2 draft (SRC-209); X-RateLimit is a vendor convention (SRC-277, T3).
- **If nobody answers:** the node lists the three options; the 429 rule (L366) applies regardless.
- **Positions:** IETF RateLimit and RateLimit-Policy (draft -11, SRC-209, T2); X-RateLimit-* (GitHub, SRC-277, T3); 429 and Retry-After only (RFC 6585, SRC-045, T1; Django REST framework, SRC-274).

## Batch H: consistency and ordering

### H1. Default concurrency control: `PIG-WEB.CONSISTENCY.CONTROL.1` (L568-L570)

- **Decision:** the default concurrency-control strategy: (a) SERIALIZABLE with retry for all transactions, (b) default isolation plus selected explicit locks and declarative constraints, or (c) optimistic version columns on user-edited rows.
- **Recommendation:**
  - (b) as the default: constraints back the invariants (L473), changes are single atomic statements (L572, L585, L588), and multi-row invariants use short, ordered, transaction-scoped locks (L578-L581).
  - (c) for records users edit in forms (L583, L260).
  - SERIALIZABLE with a framework-level retry for named use cases with write-skew risk.
  - Inferred: the maintainer doctrine practises locks, advisory locks and single-statement atomicity and states no isolation default (L581, L585); Jepsen advises selected Serializable (SRC-343, T2); Fowler chooses optimistic or pessimistic by conflict rate (SRC-344, SRC-345, T2).
  - The PostgreSQL documentation (T1, SRC-331) recommends (a) as the simplest correct route, provided every transaction runs under it and the framework retries the whole transaction (L569, L575); that is the strongest-sourced alternative.
- **If nobody answers:** the node lists the three strategies; the isolation and lock mechanics (CONTROL.2 and .3) apply under any of them.
- **Positions:** (a) PostgreSQL docs (SRC-331, SRC-337, T1); (b) Jepsen (SRC-343, T2), and Repeatable Read plus locks where replicas must be protected (L573); (c) Fowler (SRC-344, SRC-345, T2).

### H2. Incremental reader ordering: `PIG-WEB.CONSISTENCY.ORDERING.2` (L594-L595)

- **Decision:** how a reader that polls new rows (outbox relay, change feed, export) avoids skipping rows whose transaction commits after a higher id.
- **Recommendation:**
  - Where cross-row order does not matter, consume the outbox as a queue: claim rows with SKIP LOCKED and mark or delete them, with no cursor to skip past (L595, L413).
  - Where a cursor is unavoidable, use the transaction-id horizon filter.
  - Inferred: the hazard is T3 (Dudycz, SRC-351) on a T1 mechanism (SRC-334); gap detection is described as non-trivial, and a locked counter table serializes all writers.
- **If nobody answers:** the node lists both techniques; ORDERING.1 (sequence values are not commit-ordered) applies regardless.
- **Positions:** xid8 horizon filter (Dudycz, SRC-351, T3); high-water-mark gap detection (reported by the same source); locked counter table, rejected by the same source.

## Batch I: data contracts

I1 depends on A1 and E1: the contract style and the framework shape the type chain.

### I1. Type source of truth: `PIG-WEB.CONTRACT.DATA.1` (L272, L548-L549)

- **Decision:** where the type chain starts (the database schema, the Python models, or the API description), whether the description is written first or generated, and whether table and API models are one class or separate.
- **Recommendation:**
  - For one team owning both ends: code-first from typed Python models, with the generated description committed and diffed in CI (L547).
  - Separate input and output models (L553), and TypeScript types generated from the description, which do not validate at run time (L555).
  - Database constraints stay the authority for invariants (L471, L495).
  - Design-first when independent consumers exist.
  - Inferred: no source states the whole chain (L549).
- **Doctrine (maintainer):** the live database is the source of truth for structure and documentation is generated from it (L474, L471). That points to a database-first chain, which no research source covered (DCON gap); the maintainer says whether the chain starts at the database.
- **If nobody answers:** the node lists the three starting points and both model shapes; boundary parsing rules (CONTRACT.DATA.2) apply regardless.
- **Positions:** design-first (Zalando, OpenAPI Initiative, L272); code-first from typed models (FastAPI SRC-328, T1; Pydantic SRC-356, T3; L548); one class for table and API (SQLModel SRC-358, T3) versus separate models (FastAPI, L549).

### I2. Contract verification for one team: `PIG-WEB.CONTRACT.DATA.3` (L401-L402, L559-L561)

- **Decision:** does a single team's own browser client and server need consumer-driven contract tests beyond schema checks?
- **Recommendation:** schema-level checks (CI breaking-change diff L547, response-model validation L554, description conformance L273) plus a few consumer tests on critical journeys (L402); consumer-driven contracts once consumers multiply or release independently. Inferred: Pact applies contract testing to any client and front-end pair (SRC-295, T3); Robinson ties consumer-driven contracts to a community of consumers (SRC-342, T2); a schema covers all states, a pact only what a consumer uses (L559).
- **If nobody answers:** the node lists both positions; tests of external-service doubles keep their own cadence (L561, L401).

## Appendix: contested-labelled claims not raised as questions

- **L001 (ARCH-C45, WEB-C27), ROOT:** the thesis that a web application has a narrow philosophy of its own is labelled contested and inferred by its slots, but the maintainer already decided the two-graph shape (brief_distill); recorded as `known: maintainer decision | unvalidated`.
- **L067 (CV-C24), STRUCTURE.LAYERS:** labelled contested, yet no source opposes it; the uncertainty is adoption of one exploratory essay. Recorded as an open gap on a known node.
- **L117 (CV-C09), PIG-WEB.SHAPE.DEPLOYABLES.1:** the services-first dissent (Tilkov) inside a majority node, as the counter-voices slot itself recommends; recorded as `known | conflict`.
- **L477 (CONS-C23), DATA.CONSISTENCY:** Helland's entity-scoped atomicity is contested only as to when it applies; the consistency slot itself conditions it on a planned split across stores, so it is recorded as a conflict on a known node, with the single-Postgres reading (one local transaction, CONS-C30) as the central claim.
- **L302 (CV-C08), PIG-WEB.UI.OFFLINE:** local-first data ownership belongs to a deferred topic (offline and PWA); recorded on the deferred node, not asked.
- Also: L121 merges WEB-C26 (majority) and CV-C07 (contested), both resting on the same article; recorded as majority with the counter-position in positions.
