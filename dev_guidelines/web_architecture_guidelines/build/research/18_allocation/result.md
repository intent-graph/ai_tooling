# ALLOC: allocation of responsibilities across database, backend and browser (round 4)

## L1 headline

Allocation has one near-consensus rule (a tier that an adversary or a second writer can bypass is never the authority; copies elsewhere serve latency only) and four genuine schools in tension over the rest: database-as-authority (SmartDB, PostgREST), application-as-authority (Fowler), server-owned hypermedia versus client-owned local-first, and log-derived versus in-database derived data. Certainty: grounded for the principles and the school statements, inferred for most per-responsibility "wins when" conditions; the school sources are mostly T3 and carry no measured comparisons.

Pinned:
- Sources: 24 read (T1 6, T2 9, T3 9, T4 0); 3 further sources located but not read (not counted).
- Claims: 39.
- Main positions in tension: database-as-authority (SmartDB, PostgREST, maintainer doctrine) vs application-as-authority over an application-owned database (Fowler); server-owned hypermedia vs client-owned local-first; validate at every trust crossing vs parse once at the boundary; derived data built from a log by a dedicated process vs maintained inside the database.
- Contested topics: where logic that spans rows lives; where the authorization authority sits; shared database with a function API vs one application owning its database; where derived data is maintained; how thin the browser should be.
- Failed T1 fetches: none (all 6 T1 sources were read). Failed non-T1: Koppelaars resource page (403), SmartDB workshop slides (host not found), OpenAI scaling post (403), Hypermedia Systems chapter (404), one Saltzer mirror (404); the PostgREST docs site returned 429 three times and was read from its source repository.

## L2 claims

Pinned:
- Sources: 24 read (T1 6, T2 9, T3 9, T4 0); 3 further sources located but not read (not counted).
- Claims: 39.
- Main positions in tension: database-as-authority (SmartDB, PostgREST, maintainer doctrine) vs application-as-authority over an application-owned database (Fowler); server-owned hypermedia vs client-owned local-first; validate at every trust crossing vs parse once at the boundary; derived data built from a log by a dedicated process vs maintained inside the database.
- Contested topics: where logic that spans rows lives; where the authorization authority sits; shared database with a function API vs one application owning its database; where derived data is maintained; how thin the browser should be.
- Failed T1 fetches: none (all 6 T1 sources were read). Failed non-T1: Koppelaars resource page (403), SmartDB workshop slides (host not found), OpenAI scaling post (403), Hypermedia Systems chapter (404), one Saltzer mirror (404); the PostgREST docs site returned 429 three times and was read from its source repository.

Clusters (agreement, certainty, ids):
1. Authority versus copies and the end-to-end argument: put a function where the knowledge and the finality are; lower or other-tier copies are performance aids; the argument is a guideline, one must identify the ends. consensus; grounded. C01 to C05.
2. Trust boundary: decisions that protect integrity or access run where the adversary does not control them; browser checks are UX only; semantic checks sit with stored data. consensus (T1); grounded. C06 to C09.
3. Data locality, round trips, set-based work: do selection and aggregation where the data is; but maintainability first, profile, move hot spots (Fowler) against database-first (SmartDB). majority with a live debate; grounded. C10 to C13.
4. Database as authority, the thick school: as much processing as possible in the database behind a function or table API; PostgREST derives the API from the schema; RLS makes the database the authorization enforcer for any path. minority school, strongest on multi-consumer and long-lived data; grounded as statements, wins-when inferred. C14 to C19.
5. Application as authority and the number of consumers: application-owned database, integration through services; shared collections have one owning service; consumers count moves the allocation. contested against cluster 4. grounded. C20 to C23.
6. Inside versus outside data, staleness and cross-boundary effects: copies are snapshots of the past; atomicity ends at the transaction; side effects are requests, written with the transaction and relayed. consensus; grounded. C24 to C26.
7. Derived data, caching, audit: derived data is a copy of a source of record; tier chosen by freshness and atomicity needs; log-based derivation (Kleppmann) vs in-database tables and triggers. contested; grounded for each position, inferred for the choice rule. C27 to C30.
8. Concurrency and business rules: the tier that sees all writers owns concurrency control; rule placement by kind (invariants to data, policy and workflow to application, presentation to browser) with a team-skill and testability gate. majority; grounded and inferred. C31 to C33.
9. Browser side: hypermedia keeps logic on the server (fits CRUD, deep links; fails for interdependent UIs, offline, high-frequency state); locality of behaviour; UI state ownership; formatting at the edge. majority for server-owned, local-first as the strong minority; grounded with inferred wins-when. C34 to C37.
10. Thick client and local-first: client-owned replicas, server as sync peer, for zero-latency and offline; cost is client responsibility and invariants that need a single order. minority school; grounded, invariants part inferred. boundary: collaboration. C38.
11. Backend-for-frontend and the extra tier: a client-specific backend layer pays when clients diverge; with one browser client the backend already is the BFF. consensus; grounded. C39.

Live debates (one line each):
- Thick database vs application-first: SmartDB and PostgREST say as much as possible in the database; Fowler and the maintainer's own gate say application first, database for what must hold whatever writes.
- Authorization authority: backend only (OWASP), database RLS (PostgREST, Supabase), or two layers (maintainer doctrine).
- Shared database with a function API vs application-owned database with services (Fowler, Helland).
- Derived data: stream-derived from a log (Kleppmann) vs cache tables and triggers in the database (maintainer doctrine).
- Browser thinness: server-owned hypermedia vs client-owned replicas (local-first).
- Validate at every crossing (OWASP) vs parse once at the boundary (ledger parse-do-not-validate).

Not covered: the SPA school's own primary argument (no source from its authors read); measured latency or throughput comparisons of the placements; primary evidence on database-tier scalability (OpenAI scaling post not read); Llewellyn's thick-database paper and Sivers' essay (located, not read); GraphQL as a placement of query shaping; edge and serverless compute as a fourth tier; cost models (licence, hardware).

## L3 full

Pinned:
- Sources: 24 read (T1 6, T2 9, T3 9, T4 0); 3 further sources located but not read (not counted).
- Claims: 39.
- Main positions in tension: database-as-authority (SmartDB, PostgREST, maintainer doctrine) vs application-as-authority over an application-owned database (Fowler); server-owned hypermedia vs client-owned local-first; validate at every trust crossing vs parse once at the boundary; derived data built from a log by a dedicated process vs maintained inside the database.
- Contested topics: where logic that spans rows lives; where the authorization authority sits; shared database with a function API vs one application owning its database; where derived data is maintained; how thin the browser should be.
- Failed T1 fetches: none (all 6 T1 sources were read). Failed non-T1: Koppelaars resource page (403), SmartDB workshop slides (host not found), OpenAI scaling post (403), Hypermedia Systems chapter (404), one Saltzer mirror (404); the PostgREST docs site returned 429 three times and was read from its source repository.

Reading method: Saltzer et al. and Helland were read in full from the PDFs. The other pages were read through a fetch-and-extract tool that returns an extract with quotes, not the full text; claims resting on them are marked grounded only for what the extract states. Ledger ids (L...) cite the round-3 claims ledger; MAINT ids cite the maintainer-doctrine result (maintainer's codified practice, strong position, not an automatic winner).

### Source register

| id | tier | title | author or body | read | authoritative on |
|---|---|---|---|---|---|
| ALLOC-S01 | T1 | Row Security Policies | PostgreSQL docs | postgresql.org/docs/current/ddl-rowsecurity.html | RLS semantics, default-deny, bypass, caveats |
| ALLOC-S02 | T1 | Constraints | PostgreSQL docs | postgresql.org/docs/current/ddl-constraints.html | declarative enforcement, CHECK row-locality |
| ALLOC-S03 | T1 | Input Validation Cheat Sheet | OWASP | cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | client vs server validation, trust crossings |
| ALLOC-S04 | T1 | Authorization Cheat Sheet | OWASP | cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | server-side, every-request, deny-by-default |
| ALLOC-S05 | T1 | Intl | MDN | developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl | locale-sensitive formatting in the runtime |
| ALLOC-S06 | T1 | Database access optimization | Django docs | docs.djangoproject.com/en/stable/topics/db/optimization/ | work in the database, round trips, profile first |
| ALLOC-S07 | T2 | End-to-End Arguments in System Design (1984) | Saltzer, Reed, Clark | web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf (full) | function placement, identifying the ends |
| ALLOC-S08 | T2 | Data on the Outside versus Data on the Inside (2005) | Helland | cidrdb.org/cidr2005/papers/P12.pdf (full) | encapsulation, snapshots, shared-collection owner |
| ALLOC-S09 | T2 | Domain Logic and SQL | Fowler | martinfowler.com/articles/dblogic.html | SQL vs application logic trade-offs |
| ALLOC-S10 | T2 | Integration Database | Fowler | martinfowler.com/bliki/IntegrationDatabase.html | shared database coupling |
| ALLOC-S11 | T2 | Application Database | Fowler | martinfowler.com/bliki/ApplicationDatabase.html | single-owner database, integration by services |
| ALLOC-S12 | T2 | Turning the database inside-out with Apache Samza | Kleppmann | confluent.io/blog/turning-the-database-inside-out-with-apache-samza/ | log as truth, derived views |
| ALLOC-S13 | T2 | Local-first software | Kleppmann, Wiggins, van Hardenberg, McGranaghan (Ink and Switch) | inkandswitch.com/essay/local-first/ | client-owned data, seven ideals |
| ALLOC-S14 | T2 | Backends for Frontends pattern | Microsoft Azure Architecture Center | learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends | when to use BFF, costs |
| ALLOC-S15 | T2 | Backends For Frontends | Newman | samnewman.io/patterns/architectural/bff/ | BFF definition and motivation |
| ALLOC-S16 | T3 | Helsinki Declaration (IT-version), observation 1 | Koppelaars | thehelsinkideclaration.blogspot.com/2009/03/helsinki-declaration-observation-1.html | SmartDB school's founding argument |
| ALLOC-S17 | T3 | Helsinki code layers in the DBMS | Koppelaars | thehelsinkideclaration.blogspot.com/2009/04/helsinki-code-layers-in-dbms.html | SmartDB layering |
| ALLOC-S18 | T3 | PostgREST documentation, motivation | PostgREST maintainers | raw docs source (docs/index.rst, main branch) | database-as-API philosophy |
| ALLOC-S19 | T3 | SQL and business logic | Fontaine | tapoueh.org/blog/2017/06/sql-and-business-logic/ | SQL as business-logic carrier, isolation |
| ALLOC-S20 | T3 | Row Level Security guide | Supabase docs | supabase.com/docs/guides/database/postgres/row-level-security | RLS for browser-to-database access |
| ALLOC-S21 | T3 | Locality of Behaviour | htmx maintainers | htmx.org/essays/locality-of-behaviour/ | LoB vs SoC and DRY |
| ALLOC-S22 | T3 | Hypermedia-Driven Applications | htmx maintainers | htmx.org/essays/hypermedia-driven-applications/ | server-owned logic and state |
| ALLOC-S23 | T3 | When Is Hypermedia Right For You? | htmx maintainers | htmx.org/essays/when-to-use-hypermedia/ | fit and misfit of hypermedia |
| ALLOC-S24 | T3 | Transactional outbox | Richardson (microservices.io) | microservices.io/patterns/data/transactional-outbox.html | dual write, outbox, at-least-once |

Located, not read (not counted, not cited as grounds): Llewellyn "Why use PL/SQL" (thick-database paradigm), Sivers on business logic in PostgreSQL, OpenAI "Scaling PostgreSQL". Search snippets only.

### Claims

Format per claim: claim; level / stack; sources; agreement; positions; certainty; serves; wins when. Boundary tags where relevant.

**A. Principles of placement**

**ALLOC-C01.** Place a function in the tier that has the knowledge and finality to complete it correctly; an incomplete version in another tier is acceptable only as a performance enhancement. level: principle / neutral. sources: S07 (Introduction, End-to-end caretaking). agreement: consensus. certainty: grounded ("the function in question can completely and correctly be implemented only with the knowledge and help of the application standing at the end points"). serves: correctness. wins when: a function's final verdict depends on information only one tier holds.

**ALLOC-C02.** A copy of a function in a lower or shared tier must be justified by measured performance, because a shared tier makes every client pay for it and has less information than the higher tier. level: principle / neutral. sources: S07 (Performance aspects). agreement: consensus. certainty: grounded. serves: performance without cost to other clients. wins when: the lower tier is shared by many applications that do not all need the function (this argues against a thick database for a shared one-size rule; it argues for it when every consumer needs the same rule).

**ALLOC-C03.** The end-to-end argument is a guideline, not an absolute rule: first identify the ends. For rules about stored data every writer converges on the data store, so the store is an end; for user feedback the end is the user. level: principle / neutral. sources: S07 (Identifying the ends); inferred application to the data store. agreement: consensus for the guideline; the data-store reading is inferred. certainty: grounded (guideline), inferred (data store as end). serves: correctness of invariants across writers. wins when: more than one code path, migration or console writes the data.

**ALLOC-C04.** One tier is the authority for each responsibility; copies in other tiers are snapshots of the past that may be wrong without breaking correctness, and must carry what is needed to detect staleness. level: principle / neutral. sources: S08 (2.2, 3.3, 4.1, 4.5), S07, ledger L071. agreement: consensus. certainty: grounded ("anything called current is not stable"; a reference-data version "must be assumed to be somewhat out of date"). serves: correctness, latency (copies allowed). wins when: any responsibility has a copy for latency (always).

**ALLOC-C05.** Each placement should record its authority, its permitted copies and its forbidden tiers, because the same rule can legitimately exist twice (browser for feedback, server for decision, database as last guard) and only one of them decides. level: principle / neutral. sources: S03, S04, S07, S08; synthesis. agreement: consensus on the parts; the record format is a synthesis. certainty: inferred. serves: correctness, changeability. wins when: always; it is the form of the decision.

**B. Trust boundary**

**ALLOC-C06.** Any check that grants access or protects integrity must run in a tier the requester cannot modify; browser-side checks only improve user experience. level: principle / http. sources: S03 ("client-side validation is bypassable; use it for immediate feedback"), S04 ("never rely on client-side access control checks"). agreement: consensus. certainty: grounded. serves: security. wins when: always for web apps; browser and network are untrusted.

**ALLOC-C07.** Authorization is checked on every request, deny by default, with the failure path centralized. level: principle / http. sources: S04, S01 (default-deny once row security is on). agreement: consensus. certainty: grounded. serves: security. wins when: always. boundary: agents as users (any non-browser client reaches the same checks).

**ALLOC-C08.** Validate both syntax and semantics; syntax (type, format, range) may sit at the edge nearest the input, semantics (does it make sense given stored state) sits with the tier that holds the state. level: principle / neutral. sources: S03 (syntactic vs semantic); the split by tier is inferred. agreement: consensus on the distinction. certainty: grounded (distinction), inferred (tier split). serves: correctness, latency of feedback. wins when: semantic rules depend on stored rows (uniqueness, availability, balance).

**ALLOC-C09.** Validation positions: re-validate at every trust crossing, including internal APIs, queues and stored records (S03: "an internal transport does not establish that a value meets the receiving component's rules"); or parse into a precise type once at the boundary and trust the type after (ledger L484). level: decision / neutral. sources: S03, ledger L484. agreement: contested. positions: crossing-by-crossing (OWASP) wins when tiers have different owners or trust levels; parse-once wins inside one codebase with a type system. certainty: grounded. serves: security (first), simplicity (second). wins when: see positions.

**C. Data locality, latency, scalability**

**ALLOC-C10.** Filtering, aggregation, sorting and paging that reduce many rows to few are placed with the data: do the work in the database and ship the result. level: principle / neutral (practice in Postgres). sources: S09 ("schlep a handful of values back" against five thousand rows), S06 ("do database work in the database rather than in Python"), S19 (five queries with round trips against one 2 ms statement). agreement: consensus. certainty: grounded. serves: performance, latency. wins when: the data volume is much larger than the result and the logic is expressible as a query.

**ALLOC-C11.** Each extra database round trip in a request adds network latency; fetch related data in one statement and avoid queries in loops. level: practice / python. sources: S06 ("accessing the database multiple times to retrieve different parts of a single set of data is less efficient"), S19. agreement: consensus. certainty: grounded. serves: latency. wins when: the database is a network hop away and the code loops over rows. boundary: LOGIC realization.

**ALLOC-C12.** Maintainability first, profile, then move proven hot spots into SQL; do not decide placement on performance alone. level: decision / neutral. sources: S09 ("focus on writing maintainable code, then use a profiler"), S06 ("profile first"; every suggestion "might even be reversed"), ledger L215. agreement: majority. positions: Fowler and the Django docs hold application first; the SmartDB school (C14) holds database first. certainty: grounded. serves: changeability. wins when: the team is less comfortable with SQL, the logic changes with product decisions, or data volumes are modest.

**ALLOC-C13.** Scalability favours keeping per-request computation off the database tier because writes scale only through one primary while stateless backends scale out; set-based work that returns small results is the exception. level: principle / postgres. sources: none read as primary; ledger L125, L127 and the target hierarchy state the premise; secondary search results about large single-primary deployments only. agreement: majority. certainty: inferred (primary evidence not read). serves: scalability. wins when: write load, not data size, is the limit. Open: needs a read primary source (Postgres docs on replication, an engineering post).

**D. The database-as-authority school**

**ALLOC-C14.** SmartDB / Helsinki: do as much of the processing as possible inside the database and as little as possible in other layers; since 2000 the industry pushed logic out to middle tiers while DBMS features grew, losing manageability and performance. level: decision / postgres (stated for Oracle, applies to any capable DBMS). sources: S16. agreement: contested (minority school). positions: holders Koppelaars and the thick-database authors; opposed by Fowler (C12, C20). certainty: grounded as the school's statement; no measurement read. serves: correctness, performance, one source of logic. wins when: the database outlives its applications, several languages or backends consume it, the team has strong SQL skills and accepts one DBMS.

**ALLOC-C15.** SmartDB layering: expose database entry points per use (UI API objects), keep business logic in its own layer, shared data services below it, and data logic (constraints, triggers) independent of business logic so that direct SQL still meets the protections. level: practice / postgres. sources: S17. agreement: contested (as C14). certainty: grounded. serves: correctness against bypass, changeability inside the database. wins when: C14 wins. Matches the maintainer function API (L2 of the doctrine slot).

**ALLOC-C16.** The maintainer's doctrine places logic in the database behind a four-reason cost-benefit gate (reuse, hiding internals, tunable performance, integrity beyond constraints) with the costs listed as inputs. level: decision / postgres. sources: MAINT-C42, MAINT-C44, MAINT-C45 (maintainer practice, not citable); ledger L214, L527, L528. agreement: contested vs the application-first lean (L215). certainty: grounded. serves: integrity across several backends. wins when: two or more backends share the database.

**ALLOC-C17.** PostgREST: the database is the API; structure, constraints and permissions define endpoints; there is a single declarative source of truth; permissions go on database objects, not controller guards; constraints replace scattered sanity checks; the planner replaces loops. level: decision / postgres. sources: S18 (Motivation). agreement: contested (minority school). certainty: grounded. serves: minimal code, correctness, one source of truth. wins when: the application is CRUD-dominant over a well-designed schema, the team is strong in Postgres, and the schema is acceptable as the contract. Limit the project states itself: focused scope, works with other tools.

**ALLOC-C18.** Use roles plus row-level security so the database enforces who may see which rows on every access path, including paths that skip the application. Row security is default-deny once enabled; table owners, superusers and BYPASSRLS roles bypass it; foreign-key integrity checks bypass it; policy columns need indexes; grants and policies are separate layers. level: practice / postgres. sources: S01, S20, S18. agreement: majority. positions: database enforces (S18, S20) vs backend enforces (C19). certainty: grounded. serves: security (defence in depth), correctness under several access paths. wins when: browsers or agents or consoles reach the database directly, or several backends share it. boundary: agents as users.

**ALLOC-C19.** The authorization authority has three positions: the backend only (OWASP: decisions server-side, gateway or functions), the database via roles and RLS (PostgREST, Supabase), or both layers, with database permissions limiting objects and application permissions deciding business actions (ledger L468, maintainer doctrine). level: decision / neutral. sources: S04, S18, S20, ledger L468. agreement: contested. certainty: grounded. serves: security versus changeability of policy. wins when: backend-only for one backend with fast-changing policy; database for many access paths; both for high-assurance with several consumers.

**E. The application-as-authority school and consumer count**

**ALLOC-C20.** Prefer an application database controlled by one application, sharing data through services, over an integration database shared by several applications, because shared schema is deep coupling that raises the cost of changing any application. level: decision / neutral. sources: S10 ("integration databases should be avoided"), S11. agreement: majority (T2). positions: Fowler; opposed by the maintainer doctrine (MAINT-C41, one database, many backends, function API). certainty: grounded. serves: changeability, team autonomy. wins when: one team owns the application and the database; consumers can use a service.

**ALLOC-C21.** The number of consumers of the database moves the allocation: with one consumer, rules can live in that application; with several, rules that must hold for all consumers belong in the shared tier (database, or one owning service). level: principle / neutral. sources: S08 (4.5: shared collection has one owning service enforcing business rules), S10, S11, ledger L040. agreement: consensus on the variable; contested on the answer. positions: owning service (Helland, Fowler) vs database function API (SmartDB, maintainer doctrine). certainty: grounded for positions, inferred for the variable. serves: correctness. wins when: see positions.

**ALLOC-C22.** Do not expose a relational schema across a team or trust boundary as the public contract: SQL is anti-encapsulation by nature and only table-level access control exists below it; expose operations (messages, function or service API). level: principle / neutral. sources: S08 (6.4 to 6.7: "SQL doesn't really do encapsulation"). agreement: majority. certainty: grounded. serves: changeability, security. wins when: the consumer is outside the owning team. Tension with C17 (schema as the API), resolved only where the schema is the contract.

**ALLOC-C23.** Logic is cheaper to test in memory behind a replaceable data interface; logic in the database needs a live database; portability is a cost of heavy SQL. level: practice / neutral. sources: S09; ledger L042, L472. agreement: consensus. certainty: grounded. serves: changeability. wins when: fast test feedback and DBMS independence matter more than locality; loses when the DBMS is a long-term commitment (Postgres here; inferred).

**F. Inside and outside data, atomicity, side effects**

**ALLOC-C24.** Copies of another authority's data (browser state, caches, messages, replicas) are outside data: snapshots with a version, never "now"; design consumers to tolerate it. level: principle / neutral. sources: S08 (2.1 to 2.5, 3). agreement: consensus. certainty: grounded. serves: correctness under staleness, latency. wins when: any copy exists.

**ALLOC-C25.** Atomicity and simultaneity exist only inside one transaction; a requirement spanning the database and an external system is a request to be reconciled, not an atomic commit. level: principle / neutral. sources: S08 (2.1, 2.3), S07 (two-phase commit as end-to-end acknowledgement). agreement: consensus. certainty: grounded. serves: correctness. wins when: effects cross a service or vendor boundary.

**ALLOC-C26.** Side effects and integrations belong to the backend; record the intent in the database in the same transaction as the state change and let a separate process deliver it (transactional outbox), with idempotent consumers because delivery is at least once. level: decision / neutral. sources: S24, S08, ledger L045, L482. agreement: consensus. certainty: grounded. serves: reliability, correctness. wins when: a state change must cause an email, payment or message exactly-in-effect. The browser holds no third-party credentials (inferred).

**G. Derived data, caching, audit**

**ALLOC-C27.** Derived data (aggregates, caches, indexes, summaries) is a copy of a source of record; choose its maintenance tier by required freshness and by whether it must change atomically with the source. level: principle / neutral. sources: S12, ledger L176, L532, L534; synthesis. agreement: majority. certainty: inferred. serves: correctness of derived data, performance. wins when: always; the rule for choosing among C28 positions.

**ALLOC-C28.** Derive caches and read views from an ordered log with a dedicated process, not by application code, because the log fixes one order of writes for all views and removes invalidation races and cold-start problems. level: decision / neutral. sources: S12. agreement: contested. positions: Kleppmann (log-derived) vs maintainer doctrine (cache tables in the database, invalidation queue, same transaction; L534 to L539) vs triggers and generated columns (L176, L217). certainty: grounded. serves: correctness of many derived stores. wins when: many derived stores, high write rate, a team able to run stream infrastructure; the in-database tables win for one Postgres, modest scale, atomic invalidation.

**ALLOC-C29.** Caches in the browser or intermediaries are outside the team's control; set cache lifetimes by how stale a copy may be, since a long-lived stored response cannot be recalled. level: principle / http. sources: S08, ledger L010, L011, L071. agreement: consensus. certainty: grounded (via ledger). serves: latency, correctness. wins when: responses cross caches the team does not own. boundary: transverse performance.

**ALLOC-C30.** Audit records are written where all writes converge and atomically with the change (database trigger or log), with the acting user passed in; an application-only audit misses direct writes and migrations. level: decision / postgres. sources: S07 (end identification), ledger L208, L212, L217; the placement argument is inferred. agreement: majority. positions: trigger audit (atomic, complete) vs application audit (knows the business actor, easier to test). certainty: inferred. serves: completeness of the record. wins when: more than one writer or any ad-hoc SQL path; application audit wins when only the application writes and business events matter more than row changes.

**H. Concurrency and business rules**

**ALLOC-C31.** Concurrency control is owned by the tier that sees all writers, the database: locks, isolation levels and unique, exclusion and foreign-key constraints; check-then-write in application code is correct only under serializable isolation. level: principle / postgres. sources: S02 (CHECK is row-local; use UNIQUE, EXCLUDE, FOREIGN KEY for cross-row rules), S19 (several queries without a proper isolation level "open the door of inconsistencies"), ledger L473. agreement: consensus. certainty: grounded. serves: correctness. wins when: more than one request can touch the same rows at once (always on the web).

**ALLOC-C32.** Place rules by kind: invariants that must hold whatever writes the data go to declarative database constraints; workflow, policy and rules that change with product decisions go to the application; presentation and immediate feedback go to the browser. level: decision / postgres. sources: S02, S09, S03, ledger L040, L214. agreement: majority. certainty: grounded. serves: correctness (invariants), changeability (policy). wins when: default. The middle zone (multi-row validation, state transitions, cascades) is the contested part: C12 vs C14 vs C16.

**ALLOC-C33.** Logic complexity gates the application pattern: transaction script or CRUD for simple domains, a domain model plus use-case layer when rules are intricate; both keep state transitions in the backend unless C16's gate is met. level: decision / python. sources: ledger L226, L227 (Fowler's patterns), S09. agreement: consensus. certainty: grounded (via ledger). serves: changeability. wins when: complexity of the domain is the discriminator. Team SQL skill is a legitimate input (S09, ledger L041).

**I. Browser side, hypermedia, locality**

**ALLOC-C34.** Keep business logic, state and rendering decisions on the server and send hypermedia; the browser is a hypermedia client with scripting inside the document. level: decision / http. sources: S22, S23. agreement: majority. positions: HDA (htmx, S22, S23) vs client-rendered SPA with JSON API (ledger L252). certainty: grounded. serves: simplicity, one source of logic, deep linking, small client code. wins when: CRUD and text-heavy applications and nested screen regions; fails when many UI parts depend on each other (spreadsheet-like), offline is required, or state changes at high frequency (the extract names mouse-move games). Maintainers of the tool concerned, so a T3 position with self-stated limits.

**ALLOC-C35.** Locality of behaviour: the behaviour of a unit should be obvious from the unit; it conflicts with separation of concerns and DRY, and the trade-off is subjective. level: principle / neutral. sources: S21. agreement: contested. positions: LoB (htmx) vs separation of concerns. certainty: grounded. serves: comprehensibility, changeability for small teams. wins when: behaviour is simple and per-element; separation wins when behaviour is shared and complex. Allocation reading (co-locate behaviour with the artifact that uses it) is inferred.

**ALLOC-C36.** UI state is placed by lifetime and sharing: ephemeral view state (focus, open panels, drafts) in the browser; durable or shared state on the server; server state held in the browser is a cache that can go stale; the URL carries shareable view state. level: principle / js. sources: ledger L071, L284, S08, S22; synthesis. agreement: majority. certainty: inferred. serves: correctness, latency. wins when: default; local-first (C38) moves durable state to the client.

**ALLOC-C37.** Formatting and localization happen at the edge nearest the reader (browser runtime for dates, numbers, plural rules, collation, or the server when it renders HTML, email or PDF), while storage stays canonical (UTC timestamps, plain numbers, codes). level: practice / js. sources: S05 (the Intl API provides language-sensitive formatting and comparison in the runtime); canonical storage and server rendering are inferred. agreement: majority. certainty: grounded (capability), inferred (placement). serves: correctness of stored data, user experience. wins when: the server renders text (use server-side formatting); database collation matters only for sort and index behaviour (inferred, open).

**J. Thick client and local-first**

**ALLOC-C38.** Local-first: keep data and logic on the user's device with the server as an optional sync peer, for no spinners, offline work, multi-device access and ownership; replicate with CRDTs. level: decision / js. sources: S13. agreement: contested (minority school). certainty: grounded (ideals, server role, CRDT, stated costs: more user responsibility, large change history), inferred for the limit that rules needing one global order (uniqueness, balances, authorization) cannot rest on merge alone. serves: latency (zero), availability, ownership. wins when: offline needs, a latency budget that cannot take a round trip, long-lived user-owned data, collaborative editing. Inverts the authority rule (each replica has authority) at the price of invariant enforcement. boundary: collaboration.

**K. Backend-for-frontend**

**ALLOC-C39.** A backend-for-frontend holds client-specific shaping, aggregation and orchestration and nothing cross-cutting (auth, monitoring stay shared); it pays when several client types diverge or one call fans out to many services, and costs an extra hop, duplicated code and a deployable. For a single browser client over one backend, the backend already is the BFF and a separate tier is not justified. level: decision / neutral. sources: S14, S15. agreement: consensus. certainty: grounded. serves: changeability, team autonomy, client performance. wins when: mobile plus web, third-party consumers, or heavy aggregation; not when "only one interface interacts with the backend" or requests are the same. boundary: agents as users (an agent surface can be another client).

### Context variables that move an allocation

Each is grounded in the sources named; the direction is the move it causes.

| variable | moves toward | source |
|---|---|---|
| number of database consumers | database or owning service (rules shared) | S08, S10, S11, C21 |
| team SQL skill | application (low skill), database (high) | S09, ledger L041 |
| data volume vs result size | database (large ratio) | S09, S06 |
| latency budget | client copy or local-first (tight), server (loose) | S07 (voice example), S23, S13 |
| offline need | client-owned replica | S13, S23 |
| untrusted or many clients (agents, consoles) | enforcement in the database or a gateway | S01, S20, S04 (boundary: agents) |
| deploy cadence of policy | application (fast), database (slow, migration-bound) | S09, ledger L215 |
| number of client types | BFF | S14, S15 |
| write load | away from the database tier | C13 (inferred) |
| DBMS commitment | portability cost is sunk (thick DB cheaper) | S09, C23 |

### Gaps

- No primary source from the SPA school's authors; its argument appears only through critiques (S23) and the local-first essay.
- No measured comparison of placements (latency, throughput, defect rates) in any source read.
- Scalability premise (C13) lacks a read primary source.
- Llewellyn and Sivers located but not read; the SmartDB school is represented by its founder's blog and by the maintainer doctrine.
- GraphQL, edge compute and serverless as placement alternatives not covered.
- Formatting and collation placement (C37) rests on a capability page, not on an argued source.
