# ARCH research result: whole-system architecture and design philosophy of a web app

## L1 headline

Best practice for whole-web-app architecture is well settled on a few principles (start as a modular monolith, keep the number of technologies small, keep business logic apart from UI and database, record decisions and let the architecture evolve under automated checks) and thin on the claim that a web app as a whole needs its own philosophy, which no source states directly and which here is my synthesis; certainty is high for the principles, medium for the stack-level decisions, low for "just use Postgres".

Pinned:
- Sources: 33 read, by tier: T1 = 3, T2 = 22, T3 = 6, T4 = 2.
- Claims: 45 (principle 26, decision 10, practice 9).
- Contested: "just use Postgres for everything" (scope and limits; T4 and vendor sources only, one T1 constraint).
- Failed fetches on T1 sources: none. Failed or missing elsewhere: Prime Video monitoring post (T3, redirect to a marketing page, not used); Fowler "Distributed Objects Myth" and "Modular Monolith" pages (404); Kleppmann DDIA read only through secondary summaries, so not cited.

## L2 claims

Pinned (same as L1): 33 sources (T1 = 3, T2 = 22, T3 = 6, T4 = 2); 45 claims; contested = "just use Postgres for everything"; no failed T1 fetch (Prime Video T3 fetch failed, DDIA not read directly).

Clusters:
1. Architecture is the costly-to-change important stuff, and internal quality pays back within weeks, so invest in modifiability but do not build for presumed features. Consensus, grounded. ARCH-C01, C02, C03, C44.
2. Default to one deployable, modular monolith; consider services only when the monolith is too complex to manage. Majority (T2 and T3 agree; the microservices-first dissent was not read), grounded. ARCH-C04, C05, C06, C14.
3. Distribution has a premium: remote calls, eventual consistency, deployment and monitoring burden, and boundaries that are hard to place early. Consensus, grounded. ARCH-C07, C08, C09.
4. Modularity inside the monolith follows business concepts, not technical layers, is enforced mechanically, and respects bounded contexts. Majority, grounded. ARCH-C10, C11, C12, C13.
5. Separate presentation, domain and data concerns so logic can be tested and reused, but organise teams across layers, and expect the architecture to mirror team communication. Consensus, grounded. ARCH-C15, C16, C17, C18, C19.
6. One application owns its schema, and the schema evolves by versioned migrations with the code. Consensus, grounded. ARCH-C20, C21 (both boundary: DATA).
7. The web itself is an architecture of chosen constraints (client-server, stateless, cache, layered); each buys a property and costs something. Consensus, grounded. ARCH-C22 to C25, C26 (boundary: UI).
8. Boring technology: few tools, mature, spend scarce novelty on the business; simplicity is a reliability property. Consensus, grounded. ARCH-C27 to C33.
9. "Just use Postgres" for queue, cache, search until real limits are hit. Contested, inferred. ARCH-C34.
10. Record architecturally significant decisions as short, numbered, version-controlled ADRs that are superseded, never edited. Consensus, grounded. ARCH-C35 to C39.
11. Evolve deliberately: increments, automated fitness functions, sacrificial parts, strangler-fig replacement, prudent debt. Consensus, grounded. ARCH-C40 to C43.
12. A web app as a whole owns the end-to-end concerns that a backend or database alone does not (rendering location, client-server contract, team shape). Inferred synthesis, no source states it. ARCH-C45.

Live debates:
- "Just use Postgres for everything": proponents (T4, one vendor) say operate one system until limits are hit; the one T1 source only documents SKIP LOCKED for queue-like tables and says it is not for general use.
- Monolith first versus microservices first: the sources read favour monolith first; the opposing case was not read, so treat as majority, not consensus.

Not covered: DDIA and Newman-style microservice pattern books (not read directly); serverless and edge architecture; micro-frontends; multi-tenancy; cost and team-size thresholds with numbers; the dissenting "microservices first" literature; data tier, API, UI, security and operations detail (siblings).

## L3 full

### Source register

Note on method: pages were read through the fetch tool, which returns a model-written digest of the page, not the raw text. Quotes below are as returned by that digest; verify wording against the page before quoting publicly.

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| ARCH-S01 | T2 | Monolith First | Martin Fowler | https://martinfowler.com/bliki/MonolithFirst.html | start-as-monolith argument |
| ARCH-S02 | T2 | Microservice Premium | Martin Fowler | https://martinfowler.com/bliki/MicroservicePremium.html | cost of microservices |
| ARCH-S03 | T2 | Microservices (article) | Fowler and Lewis | https://martinfowler.com/articles/microservices.html | characteristics and trade-offs |
| ARCH-S04 | T3 | Choose Boring Technology | Dan McKinley (talk) | https://boringtechnology.club/ | innovation tokens |
| ARCH-S05 | T2 | Documenting Architecture Decisions | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | origin and format of ADRs |
| ARCH-S06 | T2 | Architecture Decision Record | Martin Fowler | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | ADR practice |
| ARCH-S07 | T2 | The Twelve-Factor App | Adam Wiggins | https://12factor.net/ | SaaS app build and run contract |
| ARCH-S08 | T2 | Presentation Domain Data Layering | Martin Fowler | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | three-layer modularisation, team shape |
| ARCH-S09 | T3 | The Majestic Monolith | David Heinemeier Hansson | https://signalvnoise.com/svn3/the-majestic-monolith/ | small-team monolith |
| ARCH-S10 | T3 | Deconstructing the Monolith | Shopify Engineering | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity | modular monolith in practice |
| ARCH-S11 | T2 | Sacrificial Architecture | Martin Fowler | https://martinfowler.com/bliki/SacrificialArchitecture.html | planned replacement |
| ARCH-S12 | T2 | Evolutionary Architecture (book site) | Ford, Parsons, Kua | https://evolutionaryarchitecture.com/ | definition, fitness functions |
| ARCH-S13 | T2 | Yagni | Martin Fowler | https://martinfowler.com/bliki/Yagni.html | scope of "do not build ahead" |
| ARCH-S14 | T2 | Is High Quality Software Worth the Cost? | Martin Fowler | https://martinfowler.com/articles/is-quality-worth-cost.html | internal quality economics |
| ARCH-S15 | T2 | Software Architecture Guide | Martin Fowler | https://martinfowler.com/architecture/ | what architecture is |
| ARCH-S16 | T3 | Goodbye Microservices | Twilio Segment | https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/ (redirect from segment.com) | reverse migration case |
| ARCH-S17 | T2 | Bounded Context | Martin Fowler | https://martinfowler.com/bliki/BoundedContext.html | model boundaries |
| ARCH-S18 | T2 | REST dissertation ch. 4, Web architecture | Roy Fielding | https://www.ics.uci.edu/~fielding/pubs/dissertation/web_arch_domain.htm | styles as sets of constraints |
| ARCH-S19 | T2 | REST dissertation ch. 5, REST | Roy Fielding | https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | constraints and their trade-offs |
| ARCH-S20 | T1 | PostgreSQL docs, SELECT, locking clause | PostgreSQL Global Development Group | https://www.postgresql.org/docs/current/sql-select.html | SKIP LOCKED semantics |
| ARCH-S21 | T2 | Strangler Fig Application | Martin Fowler | https://martinfowler.com/bliki/StranglerFigApplication.html | incremental replacement |
| ARCH-S22 | T2 | How Do Committees Invent? | Melvin Conway | https://www.melconway.com/Home/Committees_Paper.html | Conway's law |
| ARCH-S23 | T2 | Hexagonal Architecture | Alistair Cockburn | https://alistair.cockburn.us/hexagonal-architecture/ | ports and adapters |
| ARCH-S24 | T1 | Rendering on the Web | web.dev (Google) | https://web.dev/articles/rendering-on-the-web | SSR, static, CSR, hybrid choice |
| ARCH-S25 | T4 | Postgres for Everything | Stephan Schmidt (amazingcto) | https://www.amazingcto.com/postgres-for-everything/ | the popular "just use Postgres" case |
| ARCH-S26 | T4 | How to Collapse Your Stack Using PostgreSQL | Tiger Data (vendor, commercial interest) | https://www.tigerdata.com/blog/how-to-collapse-your-stack-using-postgresql-for-everything/ | vendor version of the case |
| ARCH-S27 | T2 | Technical Debt Quadrant | Martin Fowler | https://martinfowler.com/bliki/TechnicalDebtQuadrant.html | prudent vs reckless debt |
| ARCH-S28 | T1 | Django design philosophies | Django project | https://docs.djangoproject.com/en/stable/misc/design-philosophies/ | loose coupling, DRY, layer separation in a Python framework |
| ARCH-S29 | T2 | Simplicity (SRE book ch. 9) | Google SRE | https://sre.google/sre-book/simplicity/ | simplicity and reliability |
| ARCH-S30 | T2 | Integration Database | Martin Fowler | https://martinfowler.com/bliki/IntegrationDatabase.html | shared-database coupling |
| ARCH-S31 | T2 | Evolutionary Database Design | Sadalage and Fowler | https://martinfowler.com/articles/evodb.html | schema evolves with code |
| ARCH-S32 | T3 | Fitness function-driven development | Thoughtworks | https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development | fitness functions in delivery |
| ARCH-S33 | T3 | Architectural Decision Records | ADR GitHub organization | https://adr.github.io/ | ADR vocabulary, endorsements |

Tier count: T1 = 3 (S20, S24, S28); T2 = 22 (S01, S02, S03, S05, S06, S07, S08, S11, S12, S13, S14, S15, S17, S18, S19, S21, S22, S23, S27, S29, S30, S31); T3 = 6 (S04, S09, S10, S16, S32, S33); T4 = 2 (S25, S26). Total 33.

### Claims

Columns: id | claim | level | stack | sources (section) | agreement | positions | certainty. Positions only where not consensus.

**A. Foundations**

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C01 | Treat architecture as the shared understanding of the important decisions, those that are costly to get wrong, and spend design effort there. | principle | neutral | S15 (what is architecture) | consensus | grounded |
| ARCH-C02 | Invest in internal quality from the start: it pays back in weeks, not months, and does not trade against delivery speed. | principle | neutral | S14, S15 | consensus | grounded |
| ARCH-C03 | Do not build capabilities for presumed future features, but do invest in making the software easy to modify (tests, refactoring, continuous delivery). | principle | neutral | S13 (when yagni does not apply) | consensus | grounded |
| ARCH-C44 | Distinguish prudent from reckless technical debt, and take deliberate debt only knowingly. | principle | neutral | S27 | consensus | grounded |

**B. Monolith, modular monolith, services**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| ARCH-C04 | Defer decisions that are hard to reverse until the product is understood; in a new product that means do not fix distributed boundaries up front. | principle | neutral | S01 (YAGNI, bounded context) | consensus | | grounded |
| ARCH-C05 | Start a new web application as one deployable unit (a monolith) and split only when it becomes a problem. | decision | neutral | S01, S02, S03 (are microservices the future), S09, S16 | majority | For: Fowler, DHH, Segment, Shopify's path. Against (microservices first): not read; Fowler notes the evidence is sparse and that large organisations (Amazon, Netflix) report success with services. | grounded |
| ARCH-C06 | Do not consider microservices unless the system is too complex to manage as a monolith; if it can stay simple, keep it. | decision | neutral | S02 | consensus | | grounded |
| ARCH-C14 | Consolidating services back into one deployable is legitimate when operating cost grows with the number of services (Segment: 140+ services, per-service scaling and dependency drift), accepting less fault isolation. | decision | neutral | S16 | majority | One case study (T3); no T2 source states the reverse migration as a rule. | grounded |
| ARCH-C07 | Budget for the distribution premium before adopting services: automated deployment, monitoring, failure handling and eventual consistency. | principle | neutral | S02, S03 (trade-offs) | consensus | | grounded |
| ARCH-C08 | Place service boundaries only after the domain is understood: moving functionality between services is much harder than within a monolith. | principle | neutral | S01, S03 | consensus | | grounded |
| ARCH-C09 | Avoid distributing computation when you can; remote calls are costlier than in-process calls and moving to services shifts complexity into the connections. | principle | neutral | S03, S09 | consensus | | grounded |
| ARCH-C13 | In a small team, integrate until one person can hold the system in their head; copying large-company service patterns is a risk. | principle | neutral | S09, S01 | majority | DHH (T3) states it strongly; Fowler agrees on direction, not on the "one head" criterion. | grounded |
| ARCH-C10 | Make the monolith modular by business concept (orders, billing) rather than by technical layer, with public interfaces between modules. | decision | neutral | S10 (modular monolith), S03 (keep together what changes together) | majority | Shopify (T3) is the only practitioner case; Fowler states the same goal (keep it modular) without prescribing the cut. | grounded |
| ARCH-C11 | Enforce module boundaries with automated checks, not convention alone. | practice | neutral | S10 (boundary-violation tracking in CI), S12, S32 | majority | Shopify built tooling; Ford et al. generalise as fitness functions. | inferred (S10 + S12) |
| ARCH-C12 | Do not force one unified model on a large domain; use several bounded contexts with explicit mappings between them. | principle | neutral | S17 | consensus | | grounded |

**C. Layering, ports, teams**

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C15 | Separate presentation, domain logic and data access: it narrows the scope of attention, enables several presentations over one domain, and creates test seams. | principle | neutral | S08 | consensus | grounded |
| ARCH-C16 | Do not organise teams by layer; developers need not be full-stack but teams should be (cross-functional, around a capability). | principle | neutral | S08, S03 (business-capability organisation) | consensus | grounded |
| ARCH-C17 | Expect system structure to copy team communication structure; design the team structure and the module structure together. | principle | neutral | S22, S03 | consensus | grounded |
| ARCH-C18 | Keep business logic free of UI and database entanglement so it can be driven by users, tests, batch jobs or other programs and run without a live database. | principle | neutral | S23, S08 | consensus | grounded |
| ARCH-C19 | In the Python server, keep framework layers loosely coupled and put each concept or datum in one place only. | practice | python | S28 (loose coupling, DRY) | consensus | grounded |

**D. Data tier at architecture level** (boundary: DATA)

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C20 | One application owns its database schema; avoid a database shared by several applications as an integration mechanism. | decision | postgres | S30 | consensus | grounded |
| ARCH-C21 | Evolve the schema with the code: every change is a versioned migration kept in version control with the application. | practice | postgres | S31 | consensus | grounded |

**E. The web as an architecture** (boundaries: API, UI, APP)

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C22 | Choose the system's properties first, then adopt the set of constraints that induces them, and test proposed changes against those constraints. | principle | http | S18, S19 | consensus | grounded |
| ARCH-C23 | Keep client and server separated so UI and server-side logic and storage evolve independently. | principle | http | S19 (client-server) | consensus | grounded |
| ARCH-C24 | Make each request self-contained (stateless server) to gain scalability, visibility and recovery, accepting repeated data per request. Boundary: APP. | decision | http | S19 (stateless), S07 (factor VI) | consensus | grounded |
| ARCH-C25 | Accept that every added intermediary or layer (cache, proxy) bounds complexity at the price of latency, and that caches can serve stale data. | principle | http | S19 (cache, layered system) | consensus | grounded |
| ARCH-C26 | Decide per page where rendering happens (server, static, client, hybrid); shipping mostly HTML with minimal JavaScript is a legitimate default; measure before choosing. Boundary: UI. | decision | js | S24 | consensus | grounded |
| ARCH-C27 | Treat backing services (database, queue, cache) as attached resources reached through configuration, and keep config in the environment. Boundary: OPS. | practice | neutral | S07 (factors III, IV) | consensus | grounded |
| ARCH-C28 | Keep development, staging and production as similar as possible. Boundary: OPS. | practice | neutral | S07 (factor X) | consensus | grounded |

**F. Boring technology and simplicity**

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C29 | Treat novelty as a scarce budget (a few innovation tokens) and spend it on what differentiates the product, not on infrastructure. | principle | neutral | S04 | consensus | grounded |
| ARCH-C30 | Prefer mature technology: its failure modes are known, whereas new technology adds unknown unknowns. | principle | neutral | S04, S29 | consensus | grounded |
| ARCH-C31 | Keep the number of distinct technologies small; pick few tools that cover the whole domain, so shared platform work benefits all. | principle | neutral | S04 | majority | grounded |
| ARCH-C32 | Weigh perpetual operating cost, not adoption convenience, when choosing a technology; talk to others before adopting. | principle | neutral | S04 | majority | grounded |
| ARCH-C33 | Treat simplicity as a reliability property: delete code, keep APIs minimal, stay modular, release small and often. | principle | neutral | S29 | consensus | grounded |
| ARCH-C34 | Prefer one Postgres for queue, cache, search and documents until its limits are actually reached, then add a specialised system. | decision | postgres | S25, S26, S20 | contested | see below | inferred |

ARCH-C34 positions:
- Proponents (S25, T4; S26, T4 with commercial interest): fewer systems mean fewer failure points and less context switching; add tools "when you actually hit Postgres limits, not when you think you will"; S26 adds a guard: only while Postgres meets the need now with about 10x headroom.
- Grounding in T1 (S20): SKIP LOCKED is documented for queue-like tables with multiple consumers, and the docs state it gives an inconsistent view and is not suitable for general-purpose work.
- Gaps: S25 gives no numeric thresholds; no T1 or T2 source read states the "one database for everything" rule; the limits (cache throughput, search relevance, scale) were not verified from primary sources. Applies when: small team, modest load. Does not apply when: sub-millisecond cache or large-scale search are requirements. Consistency with C29 to C31 is by inference.
- Boundary: DATA.

**G. Recording and evolving decisions**

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C35 | Record every architecturally significant decision as its own short ADR (one to two pages). | decision | neutral | S05, S06, S33 | consensus | grounded |
| ARCH-C36 | An ADR states title, context (forces, value-neutral), decision ("We will..."), status (proposed, accepted, deprecated, superseded) and consequences (positive, negative, neutral). | practice | neutral | S05 | consensus | grounded |
| ARCH-C37 | Keep ADRs in the source repository (doc/adr or doc/arch), in lightweight markup, numbered monotonically. | practice | neutral | S05, S06 | consensus | grounded |
| ARCH-C38 | Once accepted, never reopen or edit an ADR: supersede it and keep the old one marked. | practice | neutral | S05, S06 | consensus | grounded |
| ARCH-C39 | An ADR names the serious alternatives with pros and cons and the confidence in the decision; writing it also clarifies group thinking. | practice | neutral | S06 | majority | grounded |
| ARCH-C40 | Build and evolve in small increments, and make "fit" explicit as automated fitness functions (including non-functional ones such as performance, security and operability). | principle | neutral | S12, S32 | consensus | grounded |
| ARCH-C41 | Design for roughly 10x growth and plan to rewrite before 100x; early parts may be sacrificial, kept modular, and replaced by the team that built them. | principle | neutral | S11 | majority | grounded |
| ARCH-C42 | Replace parts of a system incrementally at seams (strangler fig) rather than by big-bang rewrite. | decision | neutral | S21 | consensus | grounded |
| ARCH-C43 | Short feedback beats up-front analysis: only about a third of presumed features improved their target metrics, so build to learn. | principle | neutral | S13 | majority | grounded |

**H. Synthesis**

| id | claim | level | stack | sources | agreement | certainty |
|---|---|---|---|---|---|---|
| ARCH-C45 | Designing a web app as a whole adds end-to-end decisions beyond a backend or a database alone: where rendering happens, the client-server contract and its statelessness, how tiers are owned by teams, and how many deployables and technologies exist; the backend and database keep their own concerns (domain layering, schema ownership). | principle | neutral | inferred from S08, S16-S19, S22, S24 | n/a | inferred: no source read states this contrast; it is my synthesis |

### Gaps

- No source read defines a distinct philosophy for "the web app as a whole" (the user's hypothesis); ARCH-C45 is synthesis and should be checked by the user. Candidate further sources: Fowler's work on micro frontends, Jamstack and HTMX-style hypermedia essays (T3/T4), Kleppmann DDIA ch. 1 and 12 read directly.
- Microservices-first dissent not read (e.g. Newman, Tilkov); C05 stays "majority".
- "Just use Postgres" has no T1/T2 backing beyond SKIP LOCKED documentation; limits need primary evidence (Postgres docs, benchmarks) in the DATA slot.
- Prime Video monitoring-service case (T3) could not be fetched; omitted.
- Team-size and load thresholds for monolith vs services: no source gives numbers (Fowler's own examples vary from 4 people with 200 services to 60 with 20); open.
- Serverless, edge, multi-tenancy, micro-frontends: not covered.
- Tooling note: fetch output was a digest, not raw page text.
