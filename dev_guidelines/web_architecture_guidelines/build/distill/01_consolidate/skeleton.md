# Skeleton of the two IntentGraphs (proposal, no node created)

Proposed trees for `intent_graphs/web_app_philosophy.ig.yaml` (graph id `web-app-philosophy`, product graph) and `intent_graphs/web_defaults.ig.yaml` (graph id `pig-web-defaults`, projection graph, uids `PIG-WEB.*`), for the maintainer to review before any node exists. Every node lists the ledger rows it owns (`claims_ledger.md`); each row lists the original claim ids that become the node's impl_pointers (`build/research/<slot>/result.md::<CLAIM-ID>`) and the register ids (`sources.md`) that go to its design_notes.

Pinned:
- Nodes: `web-app-philosophy` 41 (L0 1, L1 7, L2 33, L3 0); `pig-web-defaults` 140 (L0 1, L1 10, L2 63, L3 66); 181 in total.
- States: 24 undecided nodes (1 philosophy, 23 PIG-WEB; one maintainer question each), 6 deferred nodes and 1 partly deferred (scope out), all others known, some with `conflict`, `gap` or `unvalidated` annotations.
- Ownership: 605 ledger rows, 133 owned by philosophy nodes and 472 by PIG-WEB nodes; every original claim placed once (682).
- Round 3: new nodes 24 (philosophy DATA.CONSISTENCY and CONTRACT.DATA; PIG-WEB L1 CONSISTENCY with 6 L2 and 6 L3, CONTRACT.DATA with 4 L3, DATA.DERIVED, DATA.BULK, DATA.SCHEMA.4 and .5); 12 round-2 rows moved to a better owner; no uid renamed.
- Intentlinks proposed: 21 intra philosophy, 32 intra PIG-WEB, 16 inter to `python-kb-philosophy`, 23 inter from PIG-WEB to the philosophy graph.

## Round 3 changes

- **Consistency gets an owner in both graphs.** Philosophy `DATA.CONSISTENCY` (consistency model per operation, one atomic write path, what happens inside the request and what is deferred, at-least-once effects); PIG-WEB L1 `CONSISTENCY` as the third cross-tier concern beside SEC and OPS, with CONTROL (isolation, default strategy, locks), EDITS (double submit, concurrent edits), ATOMICITY, ORDERING (sequences, incremental readers, single writer and write order), DELIVERY (outbox, idempotent consumers, post-commit hooks) and BOUNDARY (request versus deferred work).
- **Data contracts get an owner in both graphs.** Philosophy `CONTRACT.DATA` under the L1 now named Tier Contracts (its uid is unchanged): schema plus semantics, one source of truth, parse at the boundary, provider and consumer contracts. PIG-WEB `CONTRACT.DATA` (also renamed Tier Contracts at L1) has four children: type source of truth, boundary parsing, contract verification, meaning and ownership. The database-as-API position stays at `PIG-WEB.DATA.ACCESS.2`, because it is a choice about how consumers reach Postgres and question C3 already sits on that uid; `CONTRACT.DATA` links to it.
- **PIG-WEB.DATA deepened from the maintainer doctrine.** Naming (`DATA.SCHEMA.4`), JSONB contracts (`DATA.SCHEMA.5`), derived data and caches with drift guards (`DATA.DERIVED`), and bulk jobs (`DATA.BULK`) are new nodes. Keys, foreign keys, constraints, temporal columns, permission layering and deletion add rows to existing nodes. Scheduled work fills the formerly deferred `MECH.SCHEDULED`, which is now known for in-database work and still deferred for email.
- **Rows moved, ids unchanged:**
  - L043 (CV-C21) and L066 (APP-C09) to DATA.CONSISTENCY.
  - L168 (THIN-C34) to DATA.DERIVED.
  - L233 and L234 (APP-C15, APP-C16) to CONSISTENCY.ATOMICITY.
  - L260 (API-C08) to CONSISTENCY.EDITS.
  - L270 (API-C25, now grounded by CONS-C24), L409 and L410 to CONSISTENCY.DELIVERY.
  - L272 (API-C12, now contested by DCON-C06) to CONTRACT.DATA.1.
  - L401 and L402 (contract tests) to CONTRACT.DATA.3.
- **Rows not moved, and why:**
  - L045 (one system of record): ownership is its subject.
  - L127 (NOTIFY ceiling): part of question C1.
  - L228-L232: framework transaction handling, kept at APP.TRANSACTIONS and linked.
  - L467 (NOTIFY at-most-once): NOTIFY-specific, kept at MECH.REALTIME.5.
- **The maintainer doctrine is a separate authority.** Its 74 rows are new rows beside the research rows they agree with, extend or contradict; the five contradictions are not settled and sit in the undecided nodes of questions C2, C3 and D2.

## Design rationale

### Philosophy graph: why these seven branches

Each L1 answers one question a designer must answer about a web application as a whole, and the seven questions do not overlap:

- **ENVIRONMENT**: where does it run? Browsers, networks, caches and URLs the team does not control. All 17 of its principles are tagged web-distinct: this branch is the distinct core that round 2 found (L001).
- **TRUST**: whom does it trust? The trust boundary the environment draws: server authority, hostile page script, transport, bounded consumption, minimal exposure (8 web-distinct, 11 shared-backend principles).
- **DATA**: what endures? Shape, integrity, ownership, consistency of change, migration, retention (18 shared-data, 10 shared-backend).
- **CONTRACT**: how do the tiers talk? Protocol semantics, stateless requests, compatible evolution, hypermedia strictness, data contracts (10 shared-backend, 5 web-distinct, 1 shared-data, 1 shared-all).
- **STRUCTURE**: how is it cut? Layers, teams, state ownership, deployables, technologies, processes (20 shared-backend, 9 shared-all, 4 web-distinct).
- **OPERATION**: how is it run? Observability, testing, delivery (6 shared-all, 3 shared-backend, 1 web-distinct).
- **EVOLUTION**: how does it change? Explicit decisions, incremental change (8 shared-all).

Distinct and shared principles thus sit side by side in the branch their subject belongs to, each carrying its tag; the shared ones point to their counterpart through the inter intentlinks to `python-kb-philosophy` listed below, instead of copying its eight principles (P5).

Alternatives rejected:
- **Branches by distinctness** (a web-distinct branch, a shared branch): the tag is a property of a principle, not a capability; this cut would separate server-side authority (web-distinct) from deny-by-default (shared), which form one principle cluster.
- **Branches by tier** (browser, server, database): tiers are projection material and belong to PIG-WEB; most principles span tiers (statelessness, compatibility, observability).
- **The eight Python axioms as branches**: it would duplicate `python-kb-philosophy` and hide what is web-specific; the overlap is expressed by links.
- **A flat list like the Python philosophy graph**: 31 principle nodes in one level is past what a reader can hold; the seven questions give the needed intermediate level.

### PIG-WEB graph: why these ten branches

Each L1 is the part of the system a decision configures: the system's logical shape (SHAPE), its physical runtime (TOPOLOGY), the three tiers (DATA, APP, UI) and the contracts between them (CONTRACT), three concerns that cross every tier (SEC, OPS and, since round 3, CONSISTENCY), and mechanisms that span tiers and are adopted per project (MECH: jobs, caching, uploads, real-time, scheduled work).

CONSISTENCY is an L1 of its own because its decisions span the database (isolation, locks, sequences), the application (transaction scope, retries), the contract (idempotency, 202) and the browser (double submit, concurrent tabs), like SEC and OPS. Folding it into DATA would hide the request and delivery rules; folding it into APP would hide the database mechanics.

- **MECH keeps cross-tier mechanisms whole.** Real-time push, for instance, touches the contract (channel), the topology (ASGI processes, proxy buffering), the data tier (LISTEN/NOTIFY) and the application (fan-out). Splitting it by tier would scatter one decision over four branches and force a link per row; it stays whole, linked to the tiers it touches.
- **SHAPE and TOPOLOGY stay apart**: how many deployables, modules and backing services exist (logical) is decided before how processes, proxies and certificates are arranged (physical).
- **Ten L1 branches, above the usual two to six:** grouping the tiers under one `TIERS` branch would push the keyword uids (`DATA.SCHEMA`, `APP.CONFIG`) to L3, where the uid rule allows only numbers. Ten keyword-addressable areas cost less than unreadable numeric uids.
- **L3 only where demanded:** an L2 gets L3 children when an undecided decision sits beside known ones (it needs its own epistemic state), when a scope-out topic needs a deferred node, or when the L2 holds two or more distinct decisions with their own alternatives. Flat L2 nodes (MIGRATION, TESTING, JOBS) hold several practices of one decision.

Alternatives rejected:
- **Mirror the 14 research slots**: slot boundaries were research logistics; the coverage check found five topics split across slots and eight with no owner.
- **One flat decision register**: 116 decision rows without hierarchy cannot be read at claim level.
- **By user-facing feature**: features are not orthogonal to tiers; every feature would re-decide the same tier questions.

### How the coverage check's overlaps were resolved

- Postgres as queue, cache, everything (item 11): one undecided node, `PIG-WEB.SHAPE.BACKING` (L125-L127); queue mechanics stay at MECH.JOBS, NOTIFY mechanics at MECH.REALTIME.5.
- Configuration and secrets (item 12): split in two, non-secret storage `PIG-WEB.APP.CONFIG.2` (L251) and secret storage `PIG-WEB.SEC.SUPPLY.1` (L350); the shared principle (configuration outside code, open-source test) is one philosophy row (L102).
- Hypermedia versus SPA (item 13): one undecided node, `PIG-WEB.CONTRACT.STYLE` (L252-L257); UI.RENDERING holds its consequences.
- Monolith first (item 14): labelled majority with the Tilkov dissent (L113, L117).
- Row-level security (item 15): one decision node `PIG-WEB.SEC.ACCESS.2`, with the data slot's mechanics merged in (L310).
- Duplicates (item 16): merged into single rows: HTTP caching and fingerprinted assets (L414-L416), Core Web Vitals and field data (L015, L295), stateless processes (L054, L086), expand-migrate-contract (L046, L047), server-side authority (L019), layering (L062, L063), attached database (L089). Idempotency stays as two linked nodes because the two sides differ: the server accepting keys (`PIG-WEB.CONTRACT.RETRIES`) and the client sending them to external services (`PIG-WEB.APP.RESILIENCE`).
- Boring technology versus a Node SSR tier (item 17): an inter link from `PIG-WEB.UI.RENDERING.2` to `STRUCTURE.TECHNOLOGY`.
- Orphans (items 6, 7): audit logging is split into the security event log (`PIG-WEB.OPS.AUDIT_LOG`) and the business audit trail (`PIG-WEB.DATA.LIFECYCLE.3`), following THIN-C13 (L049); client error reporting is `PIG-WEB.OPS.OBSERVABILITY.2`.

### Routing rules applied

- **Graph by level:** principle rows go to the philosophy graph; decision and practice rows to PIG-WEB. Eight principle-level rows sit in PIG-WEB because each only serves one decision or is Postgres-specific: L148 (TOPO-C19), L151 (TOPO-C22), L254 (CV-C04), L303 (SEC-C59), L321 (CV-C18), L435 (RT-C01), L577 (CONS-C03), L591 (CONS-C18).
- **Re-levelling:** 17 rows carry a level different from at least one original, shown as `level (from …)` in the ledger. Mostly a practice or decision restating a principle was merged into the principle; CV-C22 alone was re-levelled to principle (the rule, not its log carrier); UI-C26's numeric targets became a decision.
- **Epistemic state** (brief_distill): consensus gives `known`; majority gives `known | conflict: <minority>`; contested gives `undecided`, with every position in design_notes. A node's state follows its central claim; L1 and L2 parents annotate undecided and deferred children. Four contested-labelled rows sit on non-undecided nodes for stated reasons (`maintainer_questions.md`, appendix).
- **Tags** (principle rows only): web-distinct 40, shared-backend 56, shared-data 21, shared-all 24 (the 8 principle rows in PIG-WEB included).
- **Maintainer rows:** agreement `maintainer decision (single source)`. A node holding only maintainer rows is `known: maintainer decision, single source`; a node where they contradict research rows is undecided and its question states the doctrine first.

## Trees and nodes

`(Lnnn-Lmmm)` is the range of ledger rows a node owns; `-` means it owns none and is the roll-up of its children.

### Tree: `web-app-philosophy` (`web_app_philosophy.ig.yaml`)

```text
ROOT  Web App Philosophy  (L001)
    ENVIRONMENT  Web Environment  (-)
        ENVIRONMENT.CLIENT  Uncontrolled Client Runtime  (L002-L006)
        ENVIRONMENT.PAGE  Unstable Page Lifecycle  (L007-L008)
        ENVIRONMENT.SKEW  Non-Atomic Deployment  (L009)
        ENVIRONMENT.CACHES  Caches Beyond Reach  (L010-L011)
        ENVIRONMENT.NETWORK  Latency as Design Material  (L012-L016)
        ENVIRONMENT.URL  URL as Public Interface  (L017-L018)
    TRUST  Trust Boundaries  (-)
        TRUST.AUTHORITY  Server-Side Authority  (L019, L020, L021, L022, L023, L468)
        TRUST.BROWSER  Hostile Page Script  (L024-L028)
        TRUST.TRANSPORT  HTTPS Everywhere  (L029-L030)
        TRUST.CONSUMPTION  Bounded Consumption  (L031-L034)
        TRUST.EXPOSURE  Minimal Exposure  (L035-L036)
    DATA  Durable Data  (-)
        DATA.SHAPE  Normalized Facts  (L037, L038, L039, L469, L470)
        DATA.INTEGRITY  Guarded Invariants  (L040, L041, L042, L471, L472, L473)
        DATA.OWNERSHIP  Single System of Record  (L044-L045)
        DATA.MIGRATION  Versioned Schema Evolution  (L046, L047, L474)
        DATA.HISTORY  Deliberate Retention  (L048-L049)
        DATA.CONSISTENCY  Atomic and Ordered Change  (L043, L066, L475, L476, L477, L478, L479, L480, L481, L482)
    CONTRACT  Tier Contracts  (-)
        CONTRACT.SEMANTICS  Protocol Semantics  (L050-L053)
        CONTRACT.STATELESS  Self-Contained Requests  (L054-L055)
        CONTRACT.COMPATIBILITY  Compatible Evolution  (L056-L058)
        CONTRACT.HYPERMEDIA  Hypermedia-Driven Interaction  [undecided]  (L059-L061)
        CONTRACT.DATA  Explicit Data Contracts  (L483-L487)
    STRUCTURE  System Structure  (-)
        STRUCTURE.LAYERS  Separated Concerns  (L062, L063, L064, L065, L067)
        STRUCTURE.TEAMS  Team-Shaped Structure  (L068-L069)
        STRUCTURE.STATE  Single-Owner State  (L070, L071, L072, L488)
        STRUCTURE.DEPLOYABLES  Distribution Premium  (L073-L080)
        STRUCTURE.TECHNOLOGY  Few Mature Technologies  (L081-L085)
        STRUCTURE.RUNTIME  Disposable Stateless Processes  (L086-L094)
    OPERATION  Operability  (-)
        OPERATION.OBSERVE  Whole-Path Observability  (L095-L098)
        OPERATION.TEST  Proportioned Testing  (L099)
        OPERATION.DELIVERY  Reproducible Delivery  (L100-L104)
    EVOLUTION  Deliberate Evolution  (-)
        EVOLUTION.DECISIONS  Explicit Decisions  (L105-L106)
        EVOLUTION.CHANGE  Incremental Change  (L107-L112)
```

Nodes: 41 (L0 1, L1 7, L2 33).

### Nodes: `web-app-philosophy`

| uid | name | intent | epistemic_state | tags of owned principles | owns |
|---|---|---|---|---|---|
| ROOT | Web App Philosophy | Design a web application as one system: a durable data model projected to people through browsers, networks and caches the team does not control; the principles distinct to that environment stand beside principles shared with any backend or data system. | known: maintainer decision (two graphs, narrow distinct core) \| unvalidated: the thesis is inferred, no source states it | web-distinct 1 | L001 |
| ENVIRONMENT | Web Environment | The client runtime, the network, intermediary caches and public URLs are outside the team's control, so the design treats them as given constraints, not as parts it can fix. | known | - | - |
| ENVIRONMENT.CLIENT | Uncontrolled Client Runtime | Browsers differ in capability, speed and script completion, so the core of every page works as plain HTML and everything else is an enhancement that may be absent. | known \| unvalidated: real-time-as-enhancement rests on one T3 source | web-distinct 5 | L002-L006 |
| ENVIRONMENT.PAGE | Unstable Page Lifecycle | A page is not a stable process: it can be restored from memory, frozen, discarded or open in several tabs, so state and side effects survive those transitions. | known | web-distinct 2 | L007-L008 |
| ENVIRONMENT.SKEW | Non-Atomic Deployment | Client code and server code never change at the same instant; old pages keep running against new servers, so every client-server change carries a compatibility window. | known | web-distinct 1 | L009 |
| ENVIRONMENT.CACHES | Caches Beyond Reach | Browsers and intermediaries store responses the team cannot purge, so cacheability is decided per URL before anything is served. | known | web-distinct 2 | L010-L011 |
| ENVIRONMENT.NETWORK | Latency as Design Material | Latency and unreliability of the network dominate what users feel, so round trips, client weight and failure behaviour are design inputs, judged by field measurement at the user. | known \| unvalidated: the distributed-computing fallacies were read through a T4 copy | web-distinct 5 | L012-L016 |
| ENVIRONMENT.URL | URL as Public Interface | URLs are the long-lived public names of resources and the carrier of navigable state, so they stay stable and free of implementation detail. | known | web-distinct 2 | L017-L018 |
| TRUST | Trust Boundaries | Nothing on the client side of the wire is trusted, so authority, verification and limits sit on the server side, with layered defences in the browser. | known | - | - |
| TRUST.AUTHORITY | Server-Side Authority | Every access decision, validation and domain rule is made by trusted server code and denied by default; client-side checks exist only for the user's convenience. | known | shared-backend 5, web-distinct 1 | L019, L020, L021, L022, L023, L468 |
| TRUST.BROWSER | Hostile Page Script | Any script running in the page may be an attacker's, so long-lived credentials stay out of its reach, cross-site scripting is prevented first, and other browser defences are second layers. | known | web-distinct 5 | L024-L028 |
| TRUST.TRANSPORT | HTTPS Everywhere | Every page and request travels over HTTPS, because transport security protects sessions and is a precondition of modern browser capabilities. | known | shared-backend 1, web-distinct 1 | L029-L030 |
| TRUST.CONSUMPTION | Bounded Consumption | Every resource a client can make the server spend (requests, bytes, time, concurrency, third-party cost) is bounded, and flows whose automation harms the business are protected specifically. | known | shared-backend 4 | L031-L034 |
| TRUST.EXPOSURE | Minimal Exposure | The system collects and emits only the data its purpose needs: secrets and unneeded personal data never reach logs, traces or URLs. | known | shared-backend 1, web-distinct 1 | L035-L036 |
| DATA | Durable Data | Data outlives code, so its shape, integrity, ownership, consistency of change and history are designed deliberately and enforced where every writer passes. | known | - | - |
| DATA.SHAPE | Normalized Facts | Each fact is stored once, in tables normalized to third normal form, so a change touches one place and update anomalies cannot arise. | known | shared-data 5 | L037, L038, L039, L469, L470 |
| DATA.INTEGRITY | Guarded Invariants | Rules that must hold whatever code writes the data are declared in the database; rules that change with product decisions live in the application. | known \| conflict: application-only validation is common practice (DATA-C07 is majority) \| conflict: maintainer doctrine places multi-table validation and state logic in the database (MAINT-C44, question C2) | shared-data 6 | L040, L041, L042, L471, L472, L473 |
| DATA.OWNERSHIP | Single System of Record | One application owns each database and one system of record holds each fact; every other store is derived from it. | known \| conflict: maintainer doctrine shares one database among several backends through a function API (MAINT-C41); maintainer to confirm in question C3 | shared-data 2 | L044-L045 |
| DATA.MIGRATION | Versioned Schema Evolution | The schema evolves with the code through versioned, automated migrations that keep old and new code working during every change. | known | shared-data 3 | L046, L047, L474 |
| DATA.HISTORY | Deliberate Retention | What is kept, for how long and why is set by obligation and purpose, and the security event log is kept apart from the business record of change. | known \| unvalidated: the log versus audit-trail split is inferred | shared-backend 1, shared-data 1 | L048-L049 |
| DATA.CONSISTENCY | Atomic and Ordered Change | Each operation states the consistency it needs; a business operation commits through one atomic write path; what the user's next view depends on happens inside the request and the rest is deferred with a stated staleness window; effects beyond the database are at-least-once and made idempotent. | known \| conflict: entity-scoped atomicity (Helland, CONS-C23) applies only when a split across stores is planned | shared-backend 9, shared-data 1 | L043, L066, L475, L476, L477, L478, L479, L480, L481, L482 |
| CONTRACT | Tier Contracts | Tiers talk through explicit contracts: HTTP used by its meaning, one self-contained request at a time, data contracts that state structure and meaning, all evolved without breaking the other side. | known \| undecided child: CONTRACT.HYPERMEDIA | - | - |
| CONTRACT.SEMANTICS | Protocol Semantics | Methods, status codes and error identifiers carry their standard meaning, so browsers, intermediaries and clients can retry, redirect and cache without guessing. | known | shared-backend 3, web-distinct 1 | L050-L053 |
| CONTRACT.STATELESS | Self-Contained Requests | Each request carries everything needed to understand it and client and server stay separated, so any server instance can answer and each side evolves on its own. | known \| conflict: cookie-held session state (Fielding, WEB-C20), recorded at PIG-WEB.SEC.SESSION.1 | shared-backend 1, web-distinct 1 | L054-L055 |
| CONTRACT.COMPATIBILITY | Compatible Evolution | Contracts change by compatible additions read by tolerant readers; breaking an existing client needs strong justification and is the versioned exception. | known | shared-backend 3 | L056-L058 |
| CONTRACT.HYPERMEDIA | Hypermedia-Driven Interaction | Whether server-provided representations drive every client transition (REST in Fielding's strict sense) or a documented, fixed URL contract is acceptable. | undecided: strict hypermedia (Fielding) versus documented fixed contracts (common API practice) | web-distinct 3 | L059-L061 |
| CONTRACT.DATA | Explicit Data Contracts | Data that crosses a tier boundary (database, server, browser) has one explicit, owned, versioned contract stating structure and meaning, one source of truth for its types, and is parsed once into precise types at each boundary. | known \| unvalidated: the full cross-tier type chain is stated by no source (DCON-C12) | shared-all 1, shared-backend 3, shared-data 1 | L483-L487 |
| STRUCTURE | System Structure | The system is cut into separated concerns, single-owner state, few deployables and few technologies, run as disposable processes. | known | - | - |
| STRUCTURE.LAYERS | Separated Concerns | Presentation, domain logic and data access are separate, and business logic is independent of delivery and storage so it can be driven and tested in isolation. | known \| gap: CV-C24 (logic free of data fetching, to drive cache invalidation) is open, one exploratory source | shared-backend 5 | L062, L063, L064, L065, L067 |
| STRUCTURE.TEAMS | Team-Shaped Structure | Teams are organised around capabilities across layers, because system structure copies team communication structure. | known | shared-all 2 | L068-L069 |
| STRUCTURE.STATE | Single-Owner State | Every piece of state has one owner; client-side copies of server data are caches that can go stale, and everything else is derived. | known \| unvalidated: the four-way client-state taxonomy is inferred | shared-all 2, web-distinct 2 | L070, L071, L072, L488 |
| STRUCTURE.DEPLOYABLES | Distribution Premium | Distribution costs remote calls, consistency, operations and hard-to-move boundaries, so it is paid only for independent deployability that is actually needed. | known | shared-backend 8 | L073-L080 |
| STRUCTURE.TECHNOLOGY | Few Mature Technologies | Novelty is a scarce budget spent on what differentiates the product; the set of technologies stays small, mature and simple. | known | shared-all 5 | L081-L085 |
| STRUCTURE.RUNTIME | Disposable Stateless Processes | Server processes are stateless, disposable, supervised and attached to backing services through configuration, so they can be started, stopped and multiplied freely. | known | shared-backend 7, web-distinct 2 | L086-L094 |
| OPERATION | Operability | The running system is observable end to end, tested in proportion, and delivered reproducibly in small releases. | known | - | - |
| OPERATION.OBSERVE | Whole-Path Observability | Logs, metrics and traces are correlated across browser, server and database, security-relevant events are always recorded, and optimisation follows measurement. | known | shared-all 1, shared-backend 2, web-distinct 1 | L095-L098 |
| OPERATION.TEST | Proportioned Testing | The test suite is a pyramid: many fast low-level tests, fewer integration tests, very few end-to-end tests. | known \| conflict: ratios are team-specific; fewer low-level tests are acceptable when high-level tests are fast and cheap (Fowler) | shared-all 1 | L099 |
| OPERATION.DELIVERY | Reproducible Delivery | One codebase is built once into immutable releases, configured from outside, and promoted through similar environments in small, frequent steps. | known | shared-all 4, shared-backend 1 | L100-L104 |
| EVOLUTION | Deliberate Evolution | The architecture is the set of costly-to-change decisions; they are made explicitly, and the system evolves in small, checked increments. | known | - | - |
| EVOLUTION.DECISIONS | Explicit Decisions | Design effort goes to the decisions that are costly to reverse, starting from the properties wanted and adopting the constraints that induce them. | known | shared-all 2 | L105-L106 |
| EVOLUTION.CHANGE | Incremental Change | Internal quality, small increments, automated fitness checks and planned replacement keep the system cheap to change without building for presumed futures. | known | shared-all 6 | L107-L112 |

### Tree: `pig-web-defaults` (`web_defaults.ig.yaml`)

```text
PIG-WEB.ROOT  Web Defaults  (-)
    PIG-WEB.SHAPE  System Shape  (-)
        PIG-WEB.SHAPE.DEPLOYABLES  System Deployables  (-)
            PIG-WEB.SHAPE.DEPLOYABLES.1  Monolith First  (L113-L119)
            PIG-WEB.SHAPE.DEPLOYABLES.2  Frontend-Shaped Servers  (L120-L121)
        PIG-WEB.SHAPE.MODULES  Modular Monolith  (L122-L124)
        PIG-WEB.SHAPE.BACKING  Backing Services  [undecided]  (L125-L127)
        PIG-WEB.SHAPE.TENANCY  Tenancy Model  (L128)
        PIG-WEB.SHAPE.RECORDS  Decision Records  (L129-L133)
    PIG-WEB.TOPOLOGY  Runtime Topology  (-)
        PIG-WEB.TOPOLOGY.EDGE  Reverse Proxy Entry  (L134-L140)
        PIG-WEB.TOPOLOGY.TLS  TLS and HSTS  (-)
            PIG-WEB.TOPOLOGY.TLS.1  TLS Termination  (L141-L145)
            PIG-WEB.TOPOLOGY.TLS.2  HSTS Rollout  (L146-L148)
        PIG-WEB.TOPOLOGY.APP_SERVER  Application Server  (L149-L155)
        PIG-WEB.TOPOLOGY.PROCESSES  Process Supervision  (L156)
            PIG-WEB.TOPOLOGY.PROCESSES.1  Replication Location  [undecided]  (L157)
            PIG-WEB.TOPOLOGY.PROCESSES.2  Worker Processes  (L158-L160)
        PIG-WEB.TOPOLOGY.STATIC  Static Assets and CDN  (L161-L167)
    PIG-WEB.DATA  Postgres Data Tier  (-)
        PIG-WEB.DATA.SCHEMA  Schema Design  (L169, L489, L490)
            PIG-WEB.DATA.SCHEMA.1  Declared Constraints  (L170, L171, L172, L173, L174, L175, L176, L491, L492, L493, L494, L495, L496)
            PIG-WEB.DATA.SCHEMA.2  Column Types  (L177, L178, L497, L498)
            PIG-WEB.DATA.SCHEMA.3  Primary Key Type  [undecided]  (L179, L499, L500, L501, L502, L503, L504)
            PIG-WEB.DATA.SCHEMA.4  Naming  (L505-L507)
            PIG-WEB.DATA.SCHEMA.5  Semi-Structured Columns  (L508-L512)
        PIG-WEB.DATA.ACCESS  Roles and Namespaces  (-)
            PIG-WEB.DATA.ACCESS.1  Roles and Privileges  (L180, L181, L182, L183, L184, L185, L186, L513, L514)
            PIG-WEB.DATA.ACCESS.2  Contract Schema  [undecided]  (L187, L188, L515, L516, L517, L518)
        PIG-WEB.DATA.MIGRATION  Live Schema Change  (L189, L190, L191, L192, L193, L194, L195, L196, L197, L198, L519)
        PIG-WEB.DATA.CONNECTIONS  Connections and Pooling  (L199-L203)
        PIG-WEB.DATA.LIFECYCLE  Deletion and History  (-)
            PIG-WEB.DATA.LIFECYCLE.1  Deletion Strategy  [undecided]  (L204, L205, L520, L521, L522, L523, L524, L525)
            PIG-WEB.DATA.LIFECYCLE.2  Time-Based Retention  (L206-L207)
            PIG-WEB.DATA.LIFECYCLE.3  History and Audit Trail  (L208-L213)
            PIG-WEB.DATA.LIFECYCLE.4  Personal Data Erasure  [deferred]  (L526)
        PIG-WEB.DATA.LOGIC  Logic in the Database  [undecided]  (L214, L215, L216, L217, L527, L528, L529, L530)
        PIG-WEB.DATA.RECOVERY  Backup and Recovery  (-)
            PIG-WEB.DATA.RECOVERY.1  Point-in-Time Recovery  (L218-L223)
            PIG-WEB.DATA.RECOVERY.2  High Availability  [deferred]  (-)
        PIG-WEB.DATA.DERIVED  Derived Data and Caches  (L168, L531, L532, L533, L534, L535, L536, L537, L538, L539)
        PIG-WEB.DATA.BULK  Bulk Data Jobs  (L540-L545)
    PIG-WEB.APP  Python Application Tier  (-)
        PIG-WEB.APP.LAYERS  Application Layers  (-)
            PIG-WEB.APP.LAYERS.1  Use-Case Layer  (L224-L226)
            PIG-WEB.APP.LAYERS.2  Domain Model and ORM  [undecided]  (L227)
        PIG-WEB.APP.TRANSACTIONS  Transaction Boundaries  (L228-L232)
        PIG-WEB.APP.DATA_ACCESS  ORM and SQL  (L235-L237)
        PIG-WEB.APP.CONCURRENCY  Sync and Async  (L238-L241)
        PIG-WEB.APP.FRAMEWORK  Web Framework  [undecided]  (L242)
        PIG-WEB.APP.RESILIENCE  Outbound Calls  (L243-L246)
        PIG-WEB.APP.CONFIG  Configuration  (-)
            PIG-WEB.APP.CONFIG.1  Configuration Loading  (L247-L250)
            PIG-WEB.APP.CONFIG.2  Configuration Storage  [undecided]  (L251)
    PIG-WEB.CONTRACT  Tier Contracts  (-)
        PIG-WEB.CONTRACT.STYLE  Contract Style  [undecided]  (L252-L257)
        PIG-WEB.CONTRACT.HTTP  HTTP Usage  (L258, L259, L261, L262, L263)
        PIG-WEB.CONTRACT.RESOURCES  Resources and Collections  (L264-L268)
        PIG-WEB.CONTRACT.RETRIES  Idempotent Retries  (L269, L271, L546)
        PIG-WEB.CONTRACT.EVOLUTION  Contract Evolution  (L273, L274, L275, L547)
            PIG-WEB.CONTRACT.EVOLUTION.1  Version Identifier  [undecided]  (L276)
            PIG-WEB.CONTRACT.EVOLUTION.2  Version Skew Policy  [undecided]  (L277-L278)
        PIG-WEB.CONTRACT.ORIGIN  Origin and CORS  (L279-L280)
        PIG-WEB.CONTRACT.DATA  Cross-Tier Data Contract  (-)
            PIG-WEB.CONTRACT.DATA.1  Type Source of Truth  [undecided]  (L272, L548, L549)
            PIG-WEB.CONTRACT.DATA.2  Boundary Parsing  (L550-L558)
            PIG-WEB.CONTRACT.DATA.3  Contract Verification  [undecided]  (L401, L402, L559, L560, L561)
            PIG-WEB.CONTRACT.DATA.4  Meaning and Ownership  (L562-L565)
    PIG-WEB.UI  Browser Presentation Tier  (-)
        PIG-WEB.UI.RENDERING  Rendering  (-)
            PIG-WEB.UI.RENDERING.1  Per-Page Rendering  (L281-L287)
            PIG-WEB.UI.RENDERING.2  JavaScript Server Tier  [undecided]  (L288-L290)
        PIG-WEB.UI.STATE  Client State and Navigation  (L291-L294)
        PIG-WEB.UI.PERFORMANCE  Performance Targets  (L295-L299)
        PIG-WEB.UI.ACCESSIBILITY  Accessibility  (L300-L301)
        PIG-WEB.UI.I18N  Internationalisation  [deferred]  (-)
        PIG-WEB.UI.OFFLINE  Offline and Local-First  [deferred]  (L302)
    PIG-WEB.SEC  Identity and Security  (L303-L304)
        PIG-WEB.SEC.ACCESS  Access Control  (-)
            PIG-WEB.SEC.ACCESS.1  Authorization Mechanism  (L305-L308)
            PIG-WEB.SEC.ACCESS.2  Row-Level Security  (L309, L310, L311, L566)
        PIG-WEB.SEC.SESSION  Browser Sessions  (L312)
            PIG-WEB.SEC.SESSION.1  Browser Authentication Model  [undecided]  (L313-L318)
            PIG-WEB.SEC.SESSION.2  Tokens in the Browser  [undecided]  (L319-L321)
            PIG-WEB.SEC.SESSION.3  Session Cookie and Lifecycle  (L322-L329)
        PIG-WEB.SEC.BROWSER  Browser Defences  (-)
            PIG-WEB.SEC.BROWSER.1  CSRF Defences  (L330-L333)
            PIG-WEB.SEC.BROWSER.2  CSP and Response Headers  (L334-L337)
        PIG-WEB.SEC.LOGIN  Login and Credentials  (L338)
            PIG-WEB.SEC.LOGIN.1  Delegated Login  (L339-L343)
            PIG-WEB.SEC.LOGIN.2  Credentials and MFA  (L344-L346)
            PIG-WEB.SEC.LOGIN.3  Login Throttling  (L347-L349)
        PIG-WEB.SEC.SUPPLY  Secrets and Supply Chain  (-)
            PIG-WEB.SEC.SUPPLY.1  Secret Storage  [undecided]  (L350)
            PIG-WEB.SEC.SUPPLY.2  Secret Handling  (L351-L353)
            PIG-WEB.SEC.SUPPLY.3  Dependencies and Provenance  (L354-L357)
        PIG-WEB.SEC.ABUSE  Rate Limiting and Abuse  (-)
            PIG-WEB.SEC.ABUSE.1  Limit Layers and Keys  (L358-L365)
            PIG-WEB.SEC.ABUSE.2  Over-Limit Response  (L366)
            PIG-WEB.SEC.ABUSE.3  Quota Headers  [undecided]  (L367-L368)
    PIG-WEB.OPS  Operations  (-)
        PIG-WEB.OPS.OBSERVABILITY  Telemetry  (L369)
            PIG-WEB.OPS.OBSERVABILITY.1  Server Telemetry  (L370-L376)
            PIG-WEB.OPS.OBSERVABILITY.2  Browser Telemetry  (L377-L382)
        PIG-WEB.OPS.MONITORING  Monitoring and Alerting  (L383-L389)
        PIG-WEB.OPS.AUDIT_LOG  Security Event Log  (L390-L395)
        PIG-WEB.OPS.TESTING  Testing  (L396, L397, L398, L399, L400, L567)
        PIG-WEB.OPS.DELIVERY  Delivery Pipeline  (L403-L405)
        PIG-WEB.OPS.INCIDENT  Incident Response  [deferred]  (-)
    PIG-WEB.CONSISTENCY  Consistency and Ordering  (-)
        PIG-WEB.CONSISTENCY.CONTROL  Concurrency Control  (-)
            PIG-WEB.CONSISTENCY.CONTROL.1  Default Strategy  [undecided]  (L568-L570)
            PIG-WEB.CONSISTENCY.CONTROL.2  Isolation and Retry  (L571-L577)
            PIG-WEB.CONSISTENCY.CONTROL.3  Explicit Locks  (L578-L581)
        PIG-WEB.CONSISTENCY.EDITS  Duplicates and Concurrent Edits  (L260, L582, L583)
        PIG-WEB.CONSISTENCY.ATOMICITY  Atomic Writes  (L233, L234, L584, L585, L586, L587, L588, L589, L590)
        PIG-WEB.CONSISTENCY.ORDERING  Ordering  (-)
            PIG-WEB.CONSISTENCY.ORDERING.1  Sequences and Numbering  (L591-L593)
            PIG-WEB.CONSISTENCY.ORDERING.2  Incremental Readers  [undecided]  (L594-L595)
            PIG-WEB.CONSISTENCY.ORDERING.3  Write Ownership and Order  (L596-L598)
        PIG-WEB.CONSISTENCY.DELIVERY  Effects After Commit  (L270, L409, L410, L599, L600)
        PIG-WEB.CONSISTENCY.BOUNDARY  Request and Deferred Work  (L601-L603)
    PIG-WEB.MECH  Cross-Tier Mechanisms  (-)
        PIG-WEB.MECH.JOBS  Background Jobs  (L406, L407, L408, L411, L412, L413)
        PIG-WEB.MECH.CACHE  Caching  (-)
            PIG-WEB.MECH.CACHE.1  HTTP Cache Policy  (L414-L416)
            PIG-WEB.MECH.CACHE.2  Application Cache  (L417-L420)
        PIG-WEB.MECH.FILES  File Uploads  (-)
            PIG-WEB.MECH.FILES.1  Upload Path  [undecided]  (L421-L424)
            PIG-WEB.MECH.FILES.2  Upload Intake  (L425-L427)
            PIG-WEB.MECH.FILES.3  File Storage and Scanning  (L428-L431)
            PIG-WEB.MECH.FILES.4  Serving User Files  (L432-L434)
        PIG-WEB.MECH.REALTIME  Real-Time Push  (L435)
            PIG-WEB.MECH.REALTIME.1  Channel Choice  [undecided]  (L436-L442)
            PIG-WEB.MECH.REALTIME.2  Streaming Connections  (L443-L454)
            PIG-WEB.MECH.REALTIME.3  Connection Processes  (L455-L458)
            PIG-WEB.MECH.REALTIME.4  Connection Security  (L459-L461)
            PIG-WEB.MECH.REALTIME.5  Postgres Notifications  (L462-L467)
        PIG-WEB.MECH.SEARCH  Search  [deferred]  (-)
        PIG-WEB.MECH.SCHEDULED  Scheduled Jobs and Email  (L604-L605)
```

Nodes: 140 (L0 1, L1 10, L2 63, L3 66).

### Nodes: `pig-web-defaults`

| uid | name | intent | epistemic_state | owns |
|---|---|---|---|---|
| PIG-WEB.ROOT | Web Defaults | Default architecture decisions for a classic website (JavaScript in the browser, a Python application server, Postgres), each traced to its sources; a project overrides a default by recording why. | known \| undecided children: 23 decision nodes await the maintainer | - |
| PIG-WEB.SHAPE | System Shape | How many deployables, modules, backing services and tenants the system has, and how its significant decisions are recorded. | known \| undecided child: SHAPE.BACKING | - |
| PIG-WEB.SHAPE.DEPLOYABLES | System Deployables | Start as one deployable and split along proven boundaries only when independent deployability is needed; frontend-specific server pieces are options, not defaults. | known \| conflict: services-first when the domain is known, the system large and the organisation mature (Tilkov, CV-C09) | - |
| PIG-WEB.SHAPE.DEPLOYABLES.1 | Monolith First | One deployable unit by default; services only on proven, stable boundaries and real team bottlenecks, reached incrementally. | known \| conflict: services-first (Tilkov, CV-C09) | L113-L119 |
| PIG-WEB.SHAPE.DEPLOYABLES.2 | Frontend-Shaped Servers | Backends-for-frontends in Newman's sense and micro frontends are options for aggregation-heavy or multi-team products, not defaults for a single-team site. | known \| conflict: the counter-voices slot labels micro frontends contested | L120-L121 |
| PIG-WEB.SHAPE.MODULES | Modular Monolith | Inside the deployable, modules follow business concepts behind public interfaces, and their boundaries are checked automatically. | known \| unvalidated: the module cut rests on one practitioner case | L122-L124 |
| PIG-WEB.SHAPE.BACKING | Backing Services | Whether Postgres alone serves as job queue, cache and notification source until a measured limit, or specialised stores are adopted from the start. | undecided: Postgres-first versus dedicated broker or cache; no T1/T2 threshold | L125-L127 |
| PIG-WEB.SHAPE.TENANCY | Tenancy Model | Single-tenant by scope decision; separate databases, separate schemas or shared tables with row-level security are the recorded options if tenancy is introduced. | known: single-tenant by scope decision (brief) \| gap: options listed, not evaluated | L128 |
| PIG-WEB.SHAPE.RECORDS | Decision Records | Every architecturally significant decision, overrides of these defaults included, is a short, numbered, immutable record kept with the code. | known | L129-L133 |
| PIG-WEB.TOPOLOGY | Runtime Topology | The run-time shape of the tiers: a reverse proxy as the single entry terminating TLS, a supervised Python server pool, worker processes from the same release, and static assets served outside Python. | known \| undecided child: TOPOLOGY.PROCESSES.1 | - |
| PIG-WEB.TOPOLOGY.EDGE | Reverse Proxy Entry | One reverse proxy is the only public entry: it buffers slow clients, forwards the original host and scheme, and is the only source the application trusts for forwarded headers. | known \| conflict: for ASGI servers the proxy is advised, not required (Uvicorn docs) | L134-L140 |
| PIG-WEB.TOPOLOGY.TLS | TLS and HSTS | HTTPS is terminated at the proxy or edge with automated certificates and current protocol versions; HSTS is adopted in stages because its scope is hard to undo. | known | - |
| PIG-WEB.TOPOLOGY.TLS.1 | TLS Termination | TLS ends at the proxy or edge, HTTP is permanently redirected to HTTPS, certificates renew automatically, and only current protocol versions are enabled. | known \| unvalidated: protocol-version rule rests on one T1 source | L141-L145 |
| PIG-WEB.TOPOLOGY.TLS.2 | HSTS Rollout | HSTS is sent on HTTPS responses only and its scope widened step by step; the HTTP redirect stays because the first visit is unprotected. | known \| unvalidated: the staged ramp is inferred | L146-L148 |
| PIG-WEB.TOPOLOGY.APP_SERVER | Application Server | A production WSGI server by default and ASGI when long-lived connections or native async are needed, run as a pre-fork worker pool sized from measurement. | known \| unvalidated: worker-count formulas have no empirical study | L149-L155 |
| PIG-WEB.TOPOLOGY.PROCESSES | Process Supervision | An external supervisor runs every process type from the same release, under unprivileged accounts, in minimal images; where replication happens depends on the hosting model. | known \| undecided child: PROCESSES.1 | L156 |
| PIG-WEB.TOPOLOGY.PROCESSES.1 | Replication Location | Whether server processes are replicated by a process manager inside the unit or by an orchestrator running one process per container. | undecided: three supervision shapes, chosen by hosting model | L157 |
| PIG-WEB.TOPOLOGY.PROCESSES.2 | Worker Processes | Background workers and admin commands are separate process types from the same release and configuration; where workers run is a placement choice. | known \| unvalidated: placement options are inferred | L158-L160 |
| PIG-WEB.TOPOLOGY.STATIC | Static Assets and CDN | Static files are collected and fingerprinted at build time and served outside Python request handlers; a CDN is added when distance or origin load justifies it. | known \| unvalidated: the CDN adoption threshold is inferred | L161-L167 |
| PIG-WEB.DATA | Postgres Data Tier | Postgres holds the system of record: a constrained, consistently named schema, least-privilege roles, lock-safe schema change, bounded connections, deliberate deletion and history, recorded derived data, designed bulk jobs, and tested point-in-time recovery. | known \| undecided children: SCHEMA.3, ACCESS.2, LIFECYCLE.1, LOGIC \| conflict: four of these carry the maintainer doctrine against the research | - |
| PIG-WEB.DATA.SCHEMA | Schema Design | Tables are normalized to third normal form, shaped by access and lifecycle, indexed for their query patterns; keys, nullability, references and row rules are declared constraints on suitable, consistently named types. | known \| undecided child: SCHEMA.3 | L169, L489, L490 |
| PIG-WEB.DATA.SCHEMA.1 | Declared Constraints | Every table has a primary key, most columns are NOT NULL, references are foreign keys with ownership-driven delete rules, and row, uniqueness and overlap rules are constraints. | known | L170, L171, L172, L173, L174, L175, L176, L491, L492, L493, L494, L495, L496 |
| PIG-WEB.DATA.SCHEMA.2 | Column Types | Column types state meaning precisely (time zone aware timestamps, text, numeric, identity columns) and creation time is an explicit column. | known | L177, L178, L497, L498 |
| PIG-WEB.DATA.SCHEMA.3 | Primary Key Type | Which primary-key shape and type the schema uses: identity integers sized by cardinality, composite scope-leading keys, UUIDv7 or UUIDv4. | undecided: maintainer doctrine (identity sized by cardinality, composite for scoped tables, UUID only with a reason) versus research lean (bigint identity, UUIDv7 for exposed keys); UUIDv7 not covered by the doctrine | L179, L499, L500, L501, L502, L503, L504 |
| PIG-WEB.DATA.SCHEMA.4 | Naming | Identifiers are lower-case, schema-qualified, within the 63-byte limit, and carry role and type, so joins never yield ambiguous columns. | known: maintainer decision, single source | L505-L507 |
| PIG-WEB.DATA.SCHEMA.5 | Semi-Structured Columns | JSONB holds bounded semi-structured data only, validated against centrally held schemas at every boundary and evolved by relaxing in place or adding a named version. | known: maintainer decision, single source \| gap: no public source on JSONB contracts | L508-L512 |
| PIG-WEB.DATA.ACCESS | Roles and Namespaces | Database objects live in domain schemas reached by a hierarchy of least-privilege roles; whether consumers see base tables or a contract surface of functions or views is a recorded choice. | known \| undecided child: ACCESS.2 | - |
| PIG-WEB.DATA.ACCESS.1 | Roles and Privileges | Objects live in dedicated schemas; an owner role runs migrations, a non-superuser runtime role gets only the privileges it needs, and connections authenticate with SCRAM over TLS. | known \| unvalidated: the owner/runtime role split is inferred | L180, L181, L182, L183, L184, L185, L186, L513, L514 |
| PIG-WEB.DATA.ACCESS.2 | Contract Schema | Whether consumers reach the data through a database contract surface (functions, or views and functions) or read base tables through the ORM; the database-as-API position of the data contract lives here. | undecided: maintainer doctrine (function API shared by several backends, views excluded) versus research (base tables for one owner, contract schema of views and functions for several consumers) | L187, L188, L515, L516, L517, L518 |
| PIG-WEB.DATA.MIGRATION | Live Schema Change | Migrations run in CI and on per-developer databases, change one small thing, follow expand-migrate-contract, and use lock-safe DDL forms on live tables. | known | L189, L190, L191, L192, L193, L194, L195, L196, L197, L198, L519 |
| PIG-WEB.DATA.CONNECTIONS | Connections and Pooling | Server-side concurrency is small and enforced by a pooler, session-dependent features stay off transaction pooling, and timeouts stop abandoned work from holding locks. | known \| unvalidated: the pool-size formula is a T3 rule of thumb | L199-L203 |
| PIG-WEB.DATA.LIFECYCLE | Deletion and History | How rows are deleted, expired and remembered is decided per entity from the reason the data is kept. | known \| undecided child: LIFECYCLE.1 \| deferred child: LIFECYCLE.4 | - |
| PIG-WEB.DATA.LIFECYCLE.1 | Deletion Strategy | Whether deleted rows are flagged (soft delete), moved to an archive in the same transaction, or removed outright. | undecided: maintainer doctrine (soft delete by default for user-facing data, with explicit mitigations) versus research lean (hard delete plus same-transaction archive) | L204, L205, L520, L521, L522, L523, L524, L525 |
| PIG-WEB.DATA.LIFECYCLE.2 | Time-Based Retention | Time-bounded data is partitioned by time when size justifies it, and old partitions are detached or dropped instead of bulk-deleted. | known | L206-L207 |
| PIG-WEB.DATA.LIFECYCLE.3 | History and Audit Trail | Business history is recorded by triggers or application-written history tables with actual and record dates, chosen by how tightly history is queried, with integrity controls for high-value records. | known \| unvalidated: audit design rests on T2 pattern and T1 mechanics, applied by inference | L208-L213 |
| PIG-WEB.DATA.LIFECYCLE.4 | Personal Data Erasure | How personal data is erased on request across tables, archives, backups and stored files. | deferred: out of scope (GDPR erasure), not researched \| maintainer sketch recorded (MAINT-C23) | L526 |
| PIG-WEB.DATA.LOGIC | Logic in the Database | How much logic beyond declared constraints lives in the database (triggers, functions, views) versus the application. | undecided: maintainer doctrine (four-reason gate, then cascades, multi-table validation and state logic in database functions; updated_at by the writer) versus research (domain logic in the application, narrow triggers) | L214, L215, L216, L217, L527, L528, L529, L530 |
| PIG-WEB.DATA.RECOVERY | Backup and Recovery | The data survives loss of the database host through continuous archiving and rehearsed restores; availability beyond recovery is deferred. | known \| deferred child: RECOVERY.2 | - |
| PIG-WEB.DATA.RECOVERY.1 | Point-in-Time Recovery | A base backup plus continuous WAL archiving, stored off the database host, tested and monitored, gives recovery to a chosen moment. | known \| unvalidated: restore-rehearsal wording to re-check against the source | L218-L223 |
| PIG-WEB.DATA.RECOVERY.2 | High Availability | Replication, failover and major-version upgrades of the database. | deferred: out of scope (HA and replication), not researched | - |
| PIG-WEB.DATA.DERIVED | Derived Data and Caches | Every denormalization and derived-data cache is a recorded choice with a sync mechanism, a staleness window and a drift guard, and caches of database data live in database tables. | known: maintainer decision, single source; agrees with THIN-C34 | L168, L531, L532, L533, L534, L535, L536, L537, L538, L539 |
| PIG-WEB.DATA.BULK | Bulk Data Jobs | Data changes over millions of rows run as designed parallel jobs: batched by an index-backed key, atomic per batch, resumable, converging, and run by a human after a checklist. | known: maintainer decision, single source | L540-L545 |
| PIG-WEB.APP | Python Application Tier | The Python server exposes use cases behind thin HTTP handlers, owns short explicit transactions, reaches Postgres through an ORM with a sanctioned SQL route, and treats outbound calls and configuration defensively. | known \| undecided children: LAYERS.2, FRAMEWORK, CONFIG.2 | - |
| PIG-WEB.APP.LAYERS | Application Layers | Use cases form a layer every entry point calls, its depth scaled to domain complexity; how far the domain is decoupled from the ORM is a recorded choice. | known \| undecided child: LAYERS.2 | - |
| PIG-WEB.APP.LAYERS.1 | Use-Case Layer | A service layer of use cases serves HTTP, CLI and jobs alike; handlers parse, call and map; transaction scripts suffice for simple logic, a domain model for complex logic. | known | L224-L226 |
| PIG-WEB.APP.LAYERS.2 | Domain Model and ORM | Whether the domain model is decoupled from the ORM behind repositories or the ORM models are the domain. | undecided: repositories (Cosmic Python) versus Active Record models (Django), by domain complexity | L227 |
| PIG-WEB.APP.TRANSACTIONS | Transaction Boundaries | In the framework, transactions are short, scoped to a use case, explicitly committed, never swallow exceptions, and use one session per thread or task; cross-effect atomicity is at CONSISTENCY. | known \| conflict: Django's default is autocommit, not explicit commit (APP-C12) | L228-L232 |
| PIG-WEB.APP.DATA_ACCESS | ORM and SQL | An ORM handles routine mapping, hand-written SQL with bound parameters handles what it expresses badly, and reads may bypass the domain model. | known | L235-L237 |
| PIG-WEB.APP.CONCURRENCY | Sync and Async | Handlers are synchronous by default; async is used only where in-process I/O concurrency pays, never blocks the event loop, and respects the constraints of async data access. | known \| unvalidated: Django async transaction support is version-dependent | L238-L241 |
| PIG-WEB.APP.FRAMEWORK | Web Framework | Which Python web framework the server is built on (Django, FastAPI, Flask), judged against the product's needs. | undecided: no neutral T1/T2 selection criteria; each framework's docs state its own niche | L242 |
| PIG-WEB.APP.RESILIENCE | Outbound Calls | Calls to external services expect transient faults: bounded retries at one layer for idempotent operations, circuit breaking and short timeouts for persistent faults, idempotency keys for mutations. | known | L243-L246 |
| PIG-WEB.APP.CONFIG | Configuration | Configuration is loaded once into a validated object and injected; where non-secret configuration is stored is a recorded choice. | known \| undecided child: CONFIG.2 | - |
| PIG-WEB.APP.CONFIG.1 | Configuration Loading | The application and its settings are constructed explicitly, validated at startup and injectable, with secrets from outside source control and debug off in production. | known \| conflict: independent variables versus per-environment settings (APP-C48) | L247-L250 |
| PIG-WEB.APP.CONFIG.2 | Configuration Storage | Whether non-secret configuration lives only in environment variables or in reviewed, version-controlled files promoted with the release. | undecided: Twelve-Factor environment variables versus SRE versioned configuration | L251 |
| PIG-WEB.CONTRACT | Tier Contracts | What crosses tier boundaries and how: the contract style, HTTP usage, resources and collections, idempotent retries, evolution rules, the origin policy, and the cross-tier data contract. | known \| undecided children: STYLE, EVOLUTION.1, EVOLUTION.2, DATA.1, DATA.3 | - |
| PIG-WEB.CONTRACT.STYLE | Contract Style | Whether the browser receives server-rendered HTML (hypermedia) or JSON for client-side rendering by default, with the agreed conditions that justify a rich client. | undecided: server-HTML default (hypermedia camp) versus client-app default (React ecosystem); conditions for a rich client agreed | L252-L257 |
| PIG-WEB.CONTRACT.HTTP | HTTP Usage | Forms post-redirect-get with 303, status codes are precise, and API errors are problem details without internals; ETag preconditions are at CONSISTENCY.EDITS. | known \| conflict: error model (problem+json versus Google and Azure models) | L258, L259, L261, L262, L263 |
| PIG-WEB.CONTRACT.RESOURCES | Resources and Collections | A data API models named resources with standard methods, and every collection is paginated by server-issued opaque continuation with a capped page size. | known \| conflict: Fielding rejects fixed resource hierarchies | L264-L268 |
| PIG-WEB.CONTRACT.RETRIES | Idempotent Retries | Creating or charging requests accept a client key under a published contract (scope, payload match, concurrent duplicate, expiry) and replay the stored first response; slow operations return 202 with a status monitor. | known \| conflict: key mechanism differs; the IETF header is an expired draft | L269, L271, L546 |
| PIG-WEB.CONTRACT.EVOLUTION | Contract Evolution | The contract description is checked in CI and diffed for breaking changes, breaking changes are defined and announced, and version placement and skew handling are recorded choices. | known \| undecided children: EVOLUTION.1, EVOLUTION.2 | L273, L274, L275, L547 |
| PIG-WEB.CONTRACT.EVOLUTION.1 | Version Identifier | Where the version identifier of a breaking change sits: URL path, query parameter, media type, date header, or none. | undecided: five positions held by Google, Azure, Zalando, Stripe and GitHub, GraphQL | L276 |
| PIG-WEB.CONTRACT.EVOLUTION.2 | Version Skew Policy | How old browser code is kept working against a new server: a compatibility window only, versioned paths, or routing each client to the server version that served it. | undecided: mitigations known, default for this stack open | L277-L278 |
| PIG-WEB.CONTRACT.ORIGIN | Origin and CORS | Pages, API and static paths share one origin by default; CORS is added only for truly cross-origin consumers, with an explicit allowlist. | known \| unvalidated: the single-origin default is inferred | L279-L280 |
| PIG-WEB.CONTRACT.DATA | Cross-Tier Data Contract | The shapes and meanings that cross the database, Python and browser boundaries come from one chosen source of truth, are parsed at each boundary, carry an owner, version and semantics, and are verified by schema diff and contract tests; the database contract surface is decided at DATA.ACCESS.2. | known \| undecided children: DATA.1, DATA.3 | - |
| PIG-WEB.CONTRACT.DATA.1 | Type Source of Truth | Where the type chain starts (database schema, Python models, or the API description), whether the description is written first or generated, and whether table and API models are one class or separate. | undecided: design-first (Zalando, OpenAPI Initiative) versus code-first from typed models (FastAPI, Pydantic); one model (SQLModel) versus separate models | L272, L548, L549 |
| PIG-WEB.CONTRACT.DATA.2 | Boundary Parsing | Input is parsed once into precise types at the boundary with explicit coercion rules, request and response models are separate and published, null and absent are distinct, and request schemas are closed while response readers stay tolerant. | known \| unvalidated: several rules rest on one framework source | L550-L558 |
| PIG-WEB.CONTRACT.DATA.3 | Contract Verification | Whether a single team's browser client and server need consumer-driven contract tests beyond schema checks, and how contract tests are scheduled. | undecided: consumer-driven tests for any client and front-end pair (Pact) versus schema checks plus a few consumer tests (inferred, OPS-C29) | L401, L402, L559, L560, L561 |
| PIG-WEB.CONTRACT.DATA.4 | Meaning and Ownership | Each contract states what a schema cannot (units, time zone, precision, invariants), separates logical from physical types, and has one owner, a version and a lifecycle status. | known \| unvalidated: applicability of the data-engineering contract standard to one application database is open | L562-L565 |
| PIG-WEB.UI | Browser Presentation Tier | The browser tier renders per page where it fits, sends script only where interaction needs it, keeps state in its rightful owner, and meets field performance and accessibility targets. | known \| undecided child: RENDERING.2 \| deferred children: I18N, OFFLINE | - |
| PIG-WEB.UI.RENDERING | Rendering | Rendering location is chosen per page, static where the URL set is known, with script shipped only to interactive regions; adding a JavaScript server tier is a recorded choice. | known \| undecided child: RENDERING.2 | - |
| PIG-WEB.UI.RENDERING.1 | Per-Page Rendering | Each page is rendered on the server or at build time where possible, hydrates only its interactive islands, detects features rather than browsers, and stays crawlable. | known \| conflict: React and Next.js treat full hydration as the normal mechanism | L281-L287 |
| PIG-WEB.UI.RENDERING.2 | JavaScript Server Tier | Whether a request-time JavaScript rendering server is added beside the Python server, or rendering stays in Python and build-time output. | undecided: framework docs treat the Node runtime as normal; hypermedia camp keeps one server language; operating cost unsourced | L288-L290 |
| PIG-WEB.UI.STATE | Client State and Navigation | Navigable view state lives in URLs through the History API, server data in a client cache only for client-rendered views, and pages stay eligible for back/forward restore. | known \| unvalidated: the server-state cache claim rests on one vendor source | L291-L294 |
| PIG-WEB.UI.PERFORMANCE | Performance Targets | Core Web Vitals at the 75th percentile are the targets, budgets per page type are enforced in the build, and pages are built for fast LCP, low INP and no layout shift. | known | L295-L299 |
| PIG-WEB.UI.ACCESSIBILITY | Accessibility | A WCAG 2.2 conformance level is a recorded requirement judged per page, met with native HTML before ARIA and full keyboard operability. | known \| gap: AA as the default level is not sourced | L300-L301 |
| PIG-WEB.UI.I18N | Internationalisation | How the site handles languages, locales and translated content. | deferred: out of scope (i18n), not researched | - |
| PIG-WEB.UI.OFFLINE | Offline and Local-First | Whether the client works offline or holds the primary copy of data and syncs (PWA, service workers, local-first). | deferred: out of scope (PWA and offline), not researched; local-first position recorded (CV-C08) | L302 |
| PIG-WEB.SEC | Identity and Security | Access is decided centrally on the server, browser sessions keep credentials out of script, browser defences are layered, credentials and secrets are handled to current standards, and abuse is rate limited. | known \| undecided children: SESSION.1, SESSION.2, SUPPLY.1, ABUSE.3 \| open: ASVS levels unread | L303-L304 |
| PIG-WEB.SEC.ACCESS | Access Control | One central authorization mechanism checks every request down to object ownership; Postgres row-level security can add a default-deny second line. | known | - |
| PIG-WEB.SEC.ACCESS.1 | Authorization Mechanism | Authorization is implemented once, applied to every request, enforced at record level, modelled by attributes or relationships as granularity grows, tested for denial and logged. | known | L305-L308 |
| PIG-WEB.SEC.ACCESS.2 | Row-Level Security | When used, row-level security is a second line under application checks, with the request-path role unable to bypass it and identity passed transaction-locally. | known: mechanics \| unclear: whether to use it is not settled by the sources; optional for a single tenant | L309, L310, L311, L566 |
| PIG-WEB.SEC.SESSION | Browser Sessions | How a browser proves who it is: the authentication model, where any token lives, and the session cookie's properties and lifecycle. | known \| undecided children: SESSION.1, SESSION.2 | L312 |
| PIG-WEB.SEC.SESSION.1 | Browser Authentication Model | Whether a first-party browser authenticates with an opaque server-side session cookie (directly or through a backend-for-frontend) or with bearer tokens held by script. | undecided: server-side session or BFF cookie (IETF, OWASP, Django) versus bearer JWT (FastAPI tutorial path, Auth0) | L313-L318 |
| PIG-WEB.SEC.SESSION.2 | Tokens in the Browser | If any token reaches the browser, where it is kept: nowhere script can read, in memory, or in localStorage with XSS prevention as the real control. | undecided: never JavaScript-readable (OWASP) versus in-memory (Auth0) versus storage-is-secondary (De Ryck) | L319-L321 |
| PIG-WEB.SEC.SESSION.3 | Session Cookie and Lifecycle | Session identifiers are random and meaningless, carried in hardened host-only cookies, renewed on privilege change, expired on the server and invalidated at logout. | known \| conflict: timeout numbers differ by risk class and body (OWASP, NIST) | L322-L329 |
| PIG-WEB.SEC.BROWSER | Browser Defences | Cross-site request forgery is defended in layers and a strict Content Security Policy plus a small header baseline back up output encoding. | known | - |
| PIG-WEB.SEC.BROWSER.1 | CSRF Defences | The framework's CSRF token plus SameSite cookies, with Origin or Fetch Metadata checks on unsafe methods; CORS never replaces them. | known | L330-L333 |
| PIG-WEB.SEC.BROWSER.2 | CSP and Response Headers | A nonce- or hash-based strict CSP rolled out report-only first, and a small baseline of security headers with obsolete ones removed. | known | L334-L337 |
| PIG-WEB.SEC.LOGIN | Login and Credentials | Login is delegated to an identity provider or run on an own credential store by recorded choice, following current OAuth, password, MFA and throttling standards. | known \| unvalidated: the identity-source choice is inferred | L338 |
| PIG-WEB.SEC.LOGIN.1 | Delegated Login | Delegated login uses the authorization code flow with PKCE, exact redirect matching, protected refresh tokens, validated ID tokens, and links accounts by issuer and subject. | known | L339-L343 |
| PIG-WEB.SEC.LOGIN.2 | Credentials and MFA | Passwords are long, unconstrained by composition or rotation, checked against breach lists and hashed with Argon2id; MFA with phishing-resistant options is offered. | known \| conflict: Django's default hasher is PBKDF2; Argon2 is opt-in | L344-L346 |
| PIG-WEB.SEC.LOGIN.3 | Login Throttling | Failed logins count per account with growing delays and a recovery path, enforced outside framework throttling, with failure-only counting on code endpoints. | known | L347-L349 |
| PIG-WEB.SEC.SUPPLY | Secrets and Supply Chain | Secrets are stored, scoped, rotated and audited, and dependencies and builds are pinned, scanned and provenance-checked. | known \| undecided child: SUPPLY.1 | - |
| PIG-WEB.SEC.SUPPLY.1 | Secret Storage | Whether runtime secrets live in environment variables or are injected from a secrets manager. | undecided: Twelve-Factor environment variables versus OWASP managed store with runtime injection | L350 |
| PIG-WEB.SEC.SUPPLY.2 | Secret Handling | Secret storage is centralized, least-privilege, short-lived and audited, the framework signing key stays confidential, and CI/CD is treated as production. | known | L351-L353 |
| PIG-WEB.SEC.SUPPLY.3 | Dependencies and Provenance | Dependencies are pinned and hash-checked, inventoried in an SBOM and scanned, taken from trusted sources, rolled out in stages, and built with verifiable provenance. | known | L354-L357 |
| PIG-WEB.SEC.ABUSE | Rate Limiting and Abuse | Limits are layered between edge and application, keyed on more than the IP, answered with 429, and operated like production features. | known \| undecided child: ABUSE.3 | - |
| PIG-WEB.SEC.ABUSE.1 | Limit Layers and Keys | Coarse limits and size bounds sit at the proxy, identity-aware limits in the application, keyed on trusted client addresses plus account or session, with shared limiter state and staged rollout. | known \| unvalidated: the proxy/application split is inferred | L358-L365 |
| PIG-WEB.SEC.ABUSE.2 | Over-Limit Response | Over-limit requests get 429 with an explanation and Retry-After where known, never cached. | known | L366 |
| PIG-WEB.SEC.ABUSE.3 | Quota Headers | Whether and how remaining quota is advertised: the IETF RateLimit draft fields, de facto X-RateLimit headers, or none. | undecided: IETF draft (T2, unstable) versus X-RateLimit (GitHub) versus 429 and Retry-After only | L367-L368 |
| PIG-WEB.OPS | Operations | The running site is traced across tiers, monitored from the user's side, keeps a protected security event log, is tested in proportion, and is delivered through a staged pipeline. | known \| deferred child: INCIDENT | - |
| PIG-WEB.OPS.OBSERVABILITY | Telemetry | One trace context links browser, server and outbound calls, logs carry its ids, sampling is chosen explicitly, and browser errors and real-user metrics join the same trail. | known | L369 |
| PIG-WEB.OPS.OBSERVABILITY.1 | Server Telemetry | W3C trace context crosses every boundary, every log record carries trace and span ids, logs stream to stdout, and trace headers are neither trusted blindly nor carriers of personal data. | known | L370-L376 |
| PIG-WEB.OPS.OBSERVABILITY.2 | Browser Telemetry | Uncaught browser errors, platform reports and real-user metrics are captured and beaconed to the server, stamped with release and trace ids; browser OpenTelemetry is not relied on alone. | known \| unvalidated: browser OpenTelemetry is experimental; the fallback is inferred | L377-L382 |
| PIG-WEB.OPS.MONITORING | Monitoring and Alerting | The golden signals are monitored as percentiles against a few user-centred objectives, pages go only to actionable user-visible conditions, and slow queries are found by statistics. | known | L383-L389 |
| PIG-WEB.OPS.AUDIT_LOG | Security Event Log | Security-relevant events are logged with who, what, when and where in one vocabulary, stored apart from application data, protected, time-synchronized and sanitized. | known | L390-L395 |
| PIG-WEB.OPS.TESTING | Testing | Tests sit at the lowest level that catches the failure, integration tests use a disposable Postgres of the production kind inside a boundary that never commits, and end-to-end tests cover critical journeys only; contract tests are at CONTRACT.DATA.3. | known \| unvalidated: test-transaction boundary rests on the maintainer doctrine only | L396, L397, L398, L399, L400, L567 |
| PIG-WEB.OPS.DELIVERY | Delivery Pipeline | A staged automated pipeline promotes releases, one-time release steps run once per release, and feature toggles decouple deploy from release. | known | L403-L405 |
| PIG-WEB.OPS.INCIDENT | Incident Response | How incidents are detected, handled and learned from (on-call, post-mortems). | deferred: out of scope (incident response), not researched | - |
| PIG-WEB.CONSISTENCY | Consistency and Ordering | Concurrent and repeated changes stay correct across tiers: a recorded concurrency-control strategy, atomic write paths, explicit ordering, idempotent effects after commit, and a clear line between work done in the request and work deferred. | known \| undecided children: CONTROL.1, ORDERING.2 | - |
| PIG-WEB.CONSISTENCY.CONTROL | Concurrency Control | Each use case runs at a recorded isolation level with whole-transaction retry; explicit locks are short, ordered and transaction-scoped; the default strategy is a recorded choice. | known \| undecided child: CONTROL.1 | - |
| PIG-WEB.CONSISTENCY.CONTROL.1 | Default Strategy | Which concurrency-control strategy is the default: SERIALIZABLE with retry for all transactions, default isolation plus selected locks and constraints, or optimistic version columns on user-edited rows. | undecided: Serializable everywhere (PostgreSQL docs) versus selected Serializable and locks (Jepsen) versus by conflict rate (Fowler) | L568-L570 |
| PIG-WEB.CONSISTENCY.CONTROL.2 | Isolation and Retry | The anomalies each Postgres isolation level permits are known per use case, Serializable's preconditions are met where used, and serialization failures and deadlocks retry the whole transaction at the use-case boundary. | known | L571-L577 |
| PIG-WEB.CONSISTENCY.CONTROL.3 | Explicit Locks | Row and advisory locks are taken in one consistent order, scoped to the transaction, keyed on every dimension of the logical key, and never held across user think time. | known | L578-L581 |
| PIG-WEB.CONSISTENCY.EDITS | Duplicates and Concurrent Edits | Double submission is stopped in layers from the button to a unique constraint, and concurrent edits of one record are lost-update cases answered by a version check from the form to the write. | known \| unvalidated: render-time form token seen only in T4 sources | L260, L582, L583 |
| PIG-WEB.CONSISTENCY.ATOMICITY | Atomic Writes | A business operation commits in one local transaction; inseparable changes are one statement; mutations are idempotent; foreign calls sit between atomic phases, never inside a transaction. | known | L233, L234, L584, L585, L586, L587, L588, L589, L590 |
| PIG-WEB.CONSISTENCY.ORDERING | Ordering | Sequence values are neither gapless nor commit-ordered, incremental readers account for late commits, each state column has one writer and coupled facts a canonical write order. | known \| undecided child: ORDERING.2 | - |
| PIG-WEB.CONSISTENCY.ORDERING.1 | Sequences and Numbering | Sequence gaps are normal, sequence values leave the database only after commit, and gapless business numbers come from a counter row inside the business transaction. | known | L591-L593 |
| PIG-WEB.CONSISTENCY.ORDERING.2 | Incremental Readers | How a reader polling new rows (outbox relay, change feed, export) avoids skipping rows that commit late: transaction-id horizon filter or gap detection. | undecided: xid8 horizon filter (Dudycz) versus high-water-mark gap detection; one T3 source for the hazard | L594-L595 |
| PIG-WEB.CONSISTENCY.ORDERING.3 | Write Ownership and Order | Every state column has exactly one authoritative writer, coupled facts follow a canonical write order with the state flipped last, and transition checks start in observe-only mode. | known: maintainer decision, single source | L596-L598 |
| PIG-WEB.CONSISTENCY.DELIVERY | Effects After Commit | Work that must follow a commit is recorded in the same transaction (outbox) and delivered at least once to idempotent consumers; post-commit hooks carry only losable work. | known | L270, L409, L410, L599, L600 |
| PIG-WEB.CONSISTENCY.BOUNDARY | Request and Deferred Work | The request validates, authorizes and commits everything the user's next view depends on plus the durable intent of deferred work; slow or foreign work is deferred behind a 202 status resource. | known \| conflict: deferral thresholds differ (1 s Azure, 10 s Google) | L601-L603 |
| PIG-WEB.MECH | Cross-Tier Mechanisms | Mechanisms that span several tiers and are adopted per project: background jobs, caching, file uploads, real-time push, scheduled work; search is deferred. | known \| undecided children: FILES.1, REALTIME.1 \| deferred child: SEARCH; SCHEDULED partly deferred | - |
| PIG-WEB.MECH.JOBS | Background Jobs | Slow or non-essential work leaves the request into worker processes with ids, not objects, as arguments; atomic enqueue and idempotent consumption are at CONSISTENCY.DELIVERY, the queue store at SHAPE.BACKING. | known | L406, L407, L408, L411, L412, L413 |
| PIG-WEB.MECH.CACHE | Caching | Every response declares its cacheability, fingerprinted assets are cached for a year and HTML revalidated, and any application cache is shared, auth-aware and has an invalidation plan. | known | - |
| PIG-WEB.MECH.CACHE.1 | HTTP Cache Policy | Explicit Cache-Control and Vary on every response, immutable long-lived fingerprinted assets, revalidated HTML, private or no-store for personalised and sensitive responses. | known | L414-L416 |
| PIG-WEB.MECH.CACHE.2 | Application Cache | Any server-side cache is shared across processes, varies on authentication state, has an expiry or invalidation plan, and holds only rebuildable data. | known \| unvalidated: the invalidation-plan rule is inferred | L417-L420 |
| PIG-WEB.MECH.FILES | File Uploads | Uploaded files are untrusted: their path to storage is a recorded choice, intake is bounded and validated, bytes live in object storage with metadata and state in Postgres, and they are served from a separate domain. | known \| undecided child: FILES.1 | - |
| PIG-WEB.MECH.FILES.1 | Upload Path | Whether file bytes travel from the browser directly to object storage under a short-lived credential or stream through the application. | undecided: direct-to-storage versus through-the-app; no source weighs the two | L421-L424 |
| PIG-WEB.MECH.FILES.2 | Upload Intake | Upload endpoints are authenticated, CSRF-protected and bounded in size at the proxy and the framework, and the application streams files instead of reading them whole. | known | L425-L427 |
| PIG-WEB.MECH.FILES.3 | File Storage and Scanning | Bytes go to object storage and metadata with an explicit upload state to Postgres; files are scanned and unreadable until clean. | known \| unvalidated: the upload state machine is inferred | L428-L431 |
| PIG-WEB.MECH.FILES.4 | Serving User Files | User files are served through an identifier-to-object handler with a correct type, nosniff and attachment disposition, and private files through short-lived signed URLs. | known \| unvalidated: the signed-URL redirect pattern is inferred | L432-L434 |
| PIG-WEB.MECH.REALTIME | Real-Time Push | The weakest channel that meets the need is chosen; long-lived connections run on async processes, survive every hop's timeouts and buffering, are authorized per action, and fan out from Postgres notifications or a shared layer. | known \| undecided child: REALTIME.1 | L435 |
| PIG-WEB.MECH.REALTIME.1 | Channel Choice | Which channel serves server-to-client push by default: polling, server-sent events or WebSocket. | undecided: SSE-first (T3) versus WebSocket-first (T4 vendor); default order inferred | L436-L442 |
| PIG-WEB.MECH.REALTIME.2 | Streaming Connections | Streams are uncached, resumable where the server can replay, kept alive under every hop's idle timeout, unbuffered at the proxy, and reconnect with backoff. | known | L443-L454 |
| PIG-WEB.MECH.REALTIME.3 | Connection Processes | Long-lived connections run on an ASGI process type of their own, and fan-out across processes goes through a shared layer. | known \| unvalidated: separate process type is inferred | L455-L458 |
| PIG-WEB.MECH.REALTIME.4 | Connection Security | WebSocket traffic uses wss, an Origin allowlist and no tokens in URLs, authorizes each action, and caps message size, rate and connections. | known | L459-L461 |
| PIG-WEB.MECH.REALTIME.5 | Postgres Notifications | LISTEN/NOTIFY is a wake-up signal over a session-level connection; consumers re-read state from tables, and events that must not be lost go through an outbox table. | known | L462-L467 |
| PIG-WEB.MECH.SEARCH | Search | How the site searches its content (Postgres full-text or a dedicated engine). | deferred: out of scope (search), not researched | - |
| PIG-WEB.MECH.SCHEDULED | Scheduled Jobs and Email | How time-triggered jobs run and how email is sent; the maintainer's practice runs scheduled database work inside the database as short, idempotent, monitored calls to named functions. | known: maintainer practice for scheduled database work (MAINT-C66, C67) \| deferred: email and scheduler placement beyond the database, not researched | L604-L605 |

## Candidate intentlinks

Types follow PRIMER_01: dataflow, requires, conflicts, refines. Each is a candidate for review, grounded in the ledger rows named; none is created.

### Intra `web-app-philosophy`

| # | src | dst | type | intent |
|---|---|---|---|---|
| 1 | ENVIRONMENT.SKEW | CONTRACT.COMPATIBILITY | requires | Because old pages keep running against new servers, every contract change must be compatible across the skew window (L009, L056). |
| 2 | ENVIRONMENT.SKEW | DATA.MIGRATION | requires | Expand-migrate-contract must also cover the old client code still running, not only old server code (L009, L047). |
| 3 | ENVIRONMENT.CACHES | ENVIRONMENT.SKEW | dataflow | Cached old assets and pages lengthen the window in which old client code runs (L010, L009). |
| 4 | ENVIRONMENT.CLIENT | TRUST.AUTHORITY | requires | A client the team does not control cannot hold decisions, so authority stays on the server (L002, L019). |
| 5 | TRUST.BROWSER | TRUST.AUTHORITY | refines | Hostile page script is the sharpest case of the untrusted client (L024, L019). |
| 6 | DATA.INTEGRITY | TRUST.AUTHORITY | refines | The database is the last guard of invariants when server code errs or a new writer appears (L040, L019). |
| 7 | STRUCTURE.STATE | DATA.OWNERSHIP | dataflow | Client-side copies of server data derive from the single system of record and may go stale (L071, L045). |
| 8 | ENVIRONMENT.URL | STRUCTURE.STATE | refines | The URL is the owner of navigable view state (L018, L070). |
| 9 | CONTRACT.STATELESS | STRUCTURE.RUNTIME | requires | Self-contained requests are what let any stateless process answer any request (L054, L086). |
| 10 | STRUCTURE.TEAMS | STRUCTURE.DEPLOYABLES | dataflow | Team communication structure shapes module and deployable boundaries (Conway, L069, L080). |
| 11 | STRUCTURE.DEPLOYABLES | STRUCTURE.TECHNOLOGY | refines | Few deployables and few technologies are the same economy of moving parts (L076, L083). |
| 12 | OPERATION.DELIVERY | DATA.MIGRATION | requires | Migrations are an explicit step of every release (L046, L101). |
| 13 | OPERATION.OBSERVE | ENVIRONMENT.NETWORK | dataflow | Field measurement from the observability path is how latency is judged at the user (L096, L015). |
| 14 | TRUST.EXPOSURE | OPERATION.OBSERVE | conflicts | Recording every security-relevant event must not leak secrets or personal data into logs and traces (L036, L098). |
| 15 | CONTRACT.HYPERMEDIA | STRUCTURE.LAYERS | refines | If representations drive transitions, application logic stays on the server side of the presentation layer (L059, L062). |
| 16 | EVOLUTION.DECISIONS | EVOLUTION.CHANGE | requires | Incremental change needs the costly decisions to be explicit and recorded first (L105, L107). |
| 17 | DATA.CONSISTENCY | DATA.INTEGRITY | requires | Concurrent writers keep invariants only where constraints back them; check-then-write races (L473, L040). |
| 18 | DATA.CONSISTENCY | ENVIRONMENT.NETWORK | refines | A lost response leaves the client unsure whether its write committed, so retried writes must be idempotent (L479, L014). |
| 19 | CONTRACT.DATA | CONTRACT.COMPATIBILITY | refines | Data contracts evolve under the additive and tolerant-reader rules (L483, L057). |
| 20 | CONTRACT.DATA | DATA.INTEGRITY | requires | Database constraints are the half of the data contract that holds whichever code writes (L485, L040). |
| 21 | CONTRACT.DATA | TRUST.AUTHORITY | refines | Parsing untrusted input once at the boundary is how server-side validation is done (L484, L019). |

### Intra `pig-web-defaults`

| # | src | dst | type | intent |
|---|---|---|---|---|
| 1 | PIG-WEB.SHAPE.BACKING | PIG-WEB.MECH.JOBS | requires | The queue store decided by BACKING carries the job rules (L126, L411-L413). |
| 2 | PIG-WEB.SHAPE.BACKING | PIG-WEB.MECH.REALTIME.5 | requires | Whether NOTIFY remains the wake-up source depends on the backing-service decision and its ceiling (L127, L462). |
| 3 | PIG-WEB.SHAPE.BACKING | PIG-WEB.MECH.CACHE.2 | requires | The application cache store (Postgres UNLOGGED or a shared cache) follows the backing-service decision (L125, L417, L420). |
| 4 | PIG-WEB.CONTRACT.STYLE | PIG-WEB.UI.RENDERING.1 | dataflow | The default contract style fixes where most pages render (L252, L281). |
| 5 | PIG-WEB.CONTRACT.STYLE | PIG-WEB.UI.RENDERING.2 | requires | A JavaScript server tier is only in question if the style is client-app first (L252, L288). |
| 6 | PIG-WEB.CONTRACT.STYLE | PIG-WEB.CONTRACT.EVOLUTION | dataflow | In a hypermedia design OpenAPI covers only the JSON endpoints (L257, L273). |
| 7 | PIG-WEB.CONTRACT.STYLE | PIG-WEB.APP.FRAMEWORK | dataflow | The default style is the main criterion for the framework choice (L252, L242). |
| 8 | PIG-WEB.SEC.SESSION.1 | PIG-WEB.SEC.SESSION.2 | requires | Token placement is a question only if the authentication model lets tokens reach the browser (L315, L319). |
| 9 | PIG-WEB.SEC.SESSION.1 | PIG-WEB.SEC.BROWSER.1 | requires | Cookie sessions require layered CSRF defences (L313, L330-L333). |
| 10 | PIG-WEB.TOPOLOGY.APP_SERVER | PIG-WEB.MECH.REALTIME.3 | requires | Long-lived connections need the ASGI choice and their own process type (L149, L455). |
| 11 | PIG-WEB.TOPOLOGY.EDGE | PIG-WEB.MECH.REALTIME.2 | conflicts | Proxy buffering protects sync workers but must be off on streaming routes (L135, L451). |
| 12 | PIG-WEB.TOPOLOGY.EDGE | PIG-WEB.SEC.ABUSE.1 | dataflow | The proxy carries the coarse, identity-blind limits and trusted client addresses (L134-L140, L358-L361). |
| 13 | PIG-WEB.DATA.CONNECTIONS | PIG-WEB.MECH.REALTIME.5 | conflicts | LISTEN needs a session-level connection that transaction pooling cannot give (L200, L465). |
| 14 | PIG-WEB.APP.TRANSACTIONS | PIG-WEB.CONSISTENCY.DELIVERY | dataflow | The use-case transaction is the one the outbox row rides on; side effects run after its commit (L229, L409). |
| 15 | PIG-WEB.CONTRACT.RETRIES | PIG-WEB.APP.RESILIENCE | refines | Server-side acceptance of idempotency keys and client-side sending of them are the two halves of one retry contract (L269, L246). |
| 16 | PIG-WEB.DATA.MIGRATION | PIG-WEB.OPS.DELIVERY | dataflow | Migrations run as a one-time release step before workers start (L189, L405). |
| 17 | PIG-WEB.CONTRACT.EVOLUTION.2 | PIG-WEB.MECH.CACHE.1 | requires | Keeping previous fingerprinted assets available and HTML revalidated bounds the skew window (L277, L415). |
| 18 | PIG-WEB.SHAPE.TENANCY | PIG-WEB.SEC.ACCESS.2 | requires | Row-level security matters mainly if tenancy moves beyond single-tenant (L128, L309). |
| 19 | PIG-WEB.DATA.ACCESS.1 | PIG-WEB.SEC.ACCESS.2 | requires | RLS is effective only if the runtime role is not owner or superuser (L180-L186, L310). |
| 20 | PIG-WEB.MECH.FILES.4 | PIG-WEB.CONTRACT.ORIGIN | conflicts | User files go to a distinct registrable domain, an explicit exception to the single-origin default (L432-L434, L279). |
| 21 | PIG-WEB.UI.RENDERING.2 | PIG-WEB.SHAPE.DEPLOYABLES | requires | A JavaScript server tier is an extra deployable (L288, L113). |
| 22 | PIG-WEB.OPS.OBSERVABILITY.2 | PIG-WEB.SEC.BROWSER.2 | dataflow | CSP violation reports arrive through the Reporting API endpoint (L380, L334-L337). |
| 23 | PIG-WEB.CONSISTENCY.DELIVERY | PIG-WEB.MECH.JOBS | dataflow | Outbox rows feed the job queue and its task design (L409, L411). |
| 24 | PIG-WEB.CONSISTENCY.ORDERING.2 | PIG-WEB.CONSISTENCY.DELIVERY | requires | The outbox relay is an incremental reader that must not skip late commits (L594, L409). |
| 25 | PIG-WEB.CONSISTENCY.EDITS | PIG-WEB.CONTRACT.HTTP | refines | The ETag precondition and its 412 answer are the wire half of the version check (L260, L259). |
| 26 | PIG-WEB.CONSISTENCY.BOUNDARY | PIG-WEB.CONTRACT.RETRIES | requires | A 202 submit needs an idempotency key, since a lost response cannot be told from a lost request (L603, L546). |
| 27 | PIG-WEB.CONSISTENCY.CONTROL.1 | PIG-WEB.DATA.CONNECTIONS | requires | Serializable stays cheap only with short transactions and a bounded pool (L569, L199). |
| 28 | PIG-WEB.CONTRACT.DATA.1 | PIG-WEB.CONTRACT.EVOLUTION | dataflow | The chosen contract source is what the CI breaking-change diff and conformance checks run against (L548, L547). |
| 29 | PIG-WEB.CONTRACT.DATA.2 | PIG-WEB.DATA.SCHEMA.1 | refines | Boundary models mirror the database constraints, and named constraints map violations to stable contract errors (L550, L495). |
| 30 | PIG-WEB.DATA.ACCESS.2 | PIG-WEB.CONTRACT.DATA | refines | A database contract surface, if chosen, is the database end of the data contract (L518, L548). |
| 31 | PIG-WEB.DATA.DERIVED | PIG-WEB.MECH.CACHE.2 | conflicts | Derived-data caches in database tables versus a shared process-level cache store (L534, L417). |
| 32 | PIG-WEB.DATA.BULK | PIG-WEB.DATA.MIGRATION | refines | Bulk data jobs run outside the schema migrations, as the migration rules require (L540, L198). |

### Inter, `web-app-philosophy` to `python-kb-philosophy`

Qualified endpoints `graph_id:uid`; the Python philosophy's eight principles are referenced, never copied.

| # | src | dst | type | intent |
|---|---|---|---|---|
| 1 | web-app-philosophy:EVOLUTION.DECISIONS | python-kb-philosophy:INTENTIONALITY | refines | Recording costly decisions with their alternatives is intentionality applied to architecture. |
| 2 | web-app-philosophy:EVOLUTION.CHANGE | python-kb-philosophy:ROUGHTOFINE | refines | Small, checked increments are rough-to-fine applied to a running system. |
| 3 | web-app-philosophy:STRUCTURE.LAYERS | python-kb-philosophy:STRUCTURE | refines | Separated presentation, domain and data layers are structure primacy at system scale. |
| 4 | web-app-philosophy:STRUCTURE.TECHNOLOGY | python-kb-philosophy:POLYGLOT | conflicts | Few technologies at system scale versus the right paradigm per problem in code: paradigms vary, the technology count stays small. |
| 5 | web-app-philosophy:STRUCTURE.RUNTIME | python-kb-philosophy:DEFENSIVE | refines | Processes that tolerate sudden death are "assume failure" at run time. |
| 6 | web-app-philosophy:DATA.SHAPE | python-kb-philosophy:DATACENTRICITY | refines | Normalized facts are the durable data model that outlives code. |
| 7 | web-app-philosophy:DATA.INTEGRITY | python-kb-philosophy:DATACENTRICITY | refines | Database-declared invariants are "schema as constraint" and "make invalid states unrepresentable". |
| 8 | web-app-philosophy:DATA.OWNERSHIP | python-kb-philosophy:DATACENTRICITY | refines | One system of record with derived stores keeps data the enduring artifact. |
| 9 | web-app-philosophy:TRUST.AUTHORITY | python-kb-philosophy:DEFENSIVE | refines | Server-side validation and deny-by-default are "validate at boundaries, trust after validation" across the network. |
| 10 | web-app-philosophy:TRUST.EXPOSURE | python-kb-philosophy:DEFENSIVE | refines | Emitting only needed data is defensive design for logs, traces and errors. |
| 11 | web-app-philosophy:CONTRACT.SEMANTICS | python-kb-philosophy:COMMUNICATION | refines | Standard methods, status codes and stable error identifiers make the wire interface readable: error messages are UI. |
| 12 | web-app-philosophy:ENVIRONMENT.URL | python-kb-philosophy:COMMUNICATION | refines | Stable, implementation-free URLs are naming as UX for the public interface. |
| 13 | web-app-philosophy:OPERATION.DELIVERY | python-kb-philosophy:REPRODUCIBILITY | refines | Build once, immutable releases and environment parity are reproducibility of deployments. |
| 14 | web-app-philosophy:OPERATION.OBSERVE | python-kb-philosophy:DEFENSIVE | refines | Correlated telemetry and always-logged security events make errors visible early. |
| 15 | web-app-philosophy:CONTRACT.DATA | python-kb-philosophy:DEFENSIVE | refines | Parsing once at the boundary into precise types is "validate at boundaries, trust after validation" across tiers. |
| 16 | web-app-philosophy:DATA.CONSISTENCY | python-kb-philosophy:DEFENSIVE | refines | Lost acknowledgements, at-least-once delivery and idempotent effects are "assume failure" for state changes. |

### Inter, `pig-web-defaults` to `web-app-philosophy`

Each PIG-WEB area materializes philosophy nodes (P4: projection realizes product intent).

| # | src | dst | type | intent |
|---|---|---|---|---|
| 1 | pig-web-defaults:PIG-WEB.SHAPE.DEPLOYABLES | web-app-philosophy:STRUCTURE.DEPLOYABLES | refines | Monolith first is the stack's answer to the distribution premium. |
| 2 | pig-web-defaults:PIG-WEB.SHAPE.BACKING | web-app-philosophy:STRUCTURE.TECHNOLOGY | refines | Postgres-first is the few-technologies principle applied to backing services. |
| 3 | pig-web-defaults:PIG-WEB.SHAPE.RECORDS | web-app-philosophy:EVOLUTION.DECISIONS | refines | Decision records are where explicit decisions live. |
| 4 | pig-web-defaults:PIG-WEB.TOPOLOGY.PROCESSES | web-app-philosophy:STRUCTURE.RUNTIME | refines | Supervision and process types realize disposable stateless processes. |
| 5 | pig-web-defaults:PIG-WEB.TOPOLOGY.TLS | web-app-philosophy:TRUST.TRANSPORT | refines | Termination, redirects and HSTS realize HTTPS everywhere. |
| 6 | pig-web-defaults:PIG-WEB.DATA.SCHEMA | web-app-philosophy:DATA.SHAPE | refines | Third normal form and declared constraints realize normalized, guarded facts. |
| 7 | pig-web-defaults:PIG-WEB.DATA.LOGIC | web-app-philosophy:DATA.INTEGRITY | refines | The logic-placement decision draws the line the integrity principle sets. |
| 8 | pig-web-defaults:PIG-WEB.DATA.MIGRATION | web-app-philosophy:DATA.MIGRATION | refines | Lock-safe DDL and expand-contract steps realize versioned schema evolution. |
| 9 | pig-web-defaults:PIG-WEB.DATA.LIFECYCLE | web-app-philosophy:DATA.HISTORY | refines | Deletion, retention and audit decisions realize deliberate retention. |
| 10 | pig-web-defaults:PIG-WEB.APP.LAYERS | web-app-philosophy:STRUCTURE.LAYERS | refines | The use-case layer realizes separated concerns in Python. |
| 11 | pig-web-defaults:PIG-WEB.CONTRACT.STYLE | web-app-philosophy:CONTRACT.HYPERMEDIA | refines | The contract style decision is where hypermedia strictness lands for this stack. |
| 12 | pig-web-defaults:PIG-WEB.CONTRACT.STYLE | web-app-philosophy:ENVIRONMENT.CLIENT | refines | A server-HTML default is progressive enhancement applied to the contract. |
| 13 | pig-web-defaults:PIG-WEB.CONTRACT.EVOLUTION | web-app-philosophy:ENVIRONMENT.SKEW | refines | Version and skew policies answer non-atomic deployment. |
| 14 | pig-web-defaults:PIG-WEB.UI.RENDERING.2 | web-app-philosophy:STRUCTURE.TECHNOLOGY | conflicts | An extra JavaScript server tier spends a technology token (coverage check item 17). |
| 15 | pig-web-defaults:PIG-WEB.UI.STATE | web-app-philosophy:STRUCTURE.STATE | refines | URL state, server-state caches and bfcache eligibility realize single-owner state. |
| 16 | pig-web-defaults:PIG-WEB.UI.PERFORMANCE | web-app-philosophy:ENVIRONMENT.NETWORK | refines | Core Web Vitals targets realize latency judged at the user. |
| 17 | pig-web-defaults:PIG-WEB.SEC.SESSION | web-app-philosophy:TRUST.BROWSER | refines | Keeping credentials out of script is the session form of the hostile-script principle. |
| 18 | pig-web-defaults:PIG-WEB.SEC.ABUSE | web-app-philosophy:TRUST.CONSUMPTION | refines | Layered rate limits realize bounded consumption. |
| 19 | pig-web-defaults:PIG-WEB.OPS.OBSERVABILITY | web-app-philosophy:OPERATION.OBSERVE | refines | Trace context and browser telemetry realize whole-path observability. |
| 20 | pig-web-defaults:PIG-WEB.MECH.CACHE | web-app-philosophy:ENVIRONMENT.CACHES | refines | The HTTP cache policy realizes deciding cacheability before serving. |
| 21 | pig-web-defaults:PIG-WEB.CONSISTENCY | web-app-philosophy:DATA.CONSISTENCY | refines | Concurrency control, atomic writes, ordering and delivery rules realize atomic and ordered change. |
| 22 | pig-web-defaults:PIG-WEB.CONTRACT.DATA | web-app-philosophy:CONTRACT.DATA | refines | The type source, boundary parsing and verification decisions realize explicit data contracts. |
| 23 | pig-web-defaults:PIG-WEB.DATA.DERIVED | web-app-philosophy:DATA.SHAPE | refines | Sync plans and drift guards are the condition under which denormalization is allowed. |

## Deferred nodes (scope out, recorded, not researched)

| node | topic (brief_shared round-2 scope out) | claims owned |
|---|---|---|
| PIG-WEB.DATA.RECOVERY.2 | high availability and replication | none |
| PIG-WEB.UI.I18N | internationalisation | none |
| PIG-WEB.UI.OFFLINE | PWA and offline | L302 (CV-C08, local-first) |
| PIG-WEB.DATA.LIFECYCLE.4 | GDPR erasure | L526 (MAINT-C23, the maintainer's anonymization sketch, recorded as input) |
| PIG-WEB.MECH.SEARCH | search | none |
| PIG-WEB.MECH.SCHEDULED | email and scheduled jobs; partly deferred since round 3 | L604, L605 (maintainer practice for scheduled database work); email and scheduler placement beyond the database stay deferred |
| PIG-WEB.OPS.INCIDENT | incident response | none |

Multi-tenancy is in light scope: `PIG-WEB.SHAPE.TENANCY` records single-tenant as the default with the options of L128, as known, not deferred.

## Conventions to check at creation

- **Root uids:** the philosophy root is `ROOT` (validator rule). The PIG-WEB graph follows the `PIG-PY.*` precedent, as brief_distill fixes: root `PIG-WEB.ROOT`, L1 `PIG-WEB.<AREA>`, L2 `PIG-WEB.<AREA>.<KEYWORD>`, L3 `PIG-WEB.<AREA>.<KEYWORD>.<n>`. `ig-tool tree` reads `python_defaults.ig.yaml` with root `PIG-PY.ROOT` without complaint, but PRIMER_01 states both "root exactly ROOT" and an L1 pattern `PIG-{SEMANTIC}-{COMPONENT}`; run `ig-tool validate` on the first PIG-WEB nodes before creating the rest.
- **Names:** no node name contains `/ \ : * ? " < > | [ ] #` or `^` (checked by script).
- **Traceability:** a node's impl_pointers are the `merges` ids of the rows it owns, each written `build/research/<slot>/result.md::<CLAIM-ID>`; its design_notes take the positions and the `SRC-` ids of those rows. A row whose original cited no source (API-C25, API-C32) carries none.
- **Public repository:** nothing here names a private project or an absolute path.
