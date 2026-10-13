# Skeleton of the two IntentGraphs on the maintainer's hierarchy (round 4, no node created)

Proposed trees for `intent_graphs/web_app_philosophy.ig.yaml` (graph id `web-app-philosophy`, product graph) and `intent_graphs/web_defaults.ig.yaml` (graph id `pig-web-defaults`, projection graph, uids `PIG-WEB.*`), cut on the maintainer's functional hierarchy (`../target_hierarchy.md`). It replaces the rejected partition of `../01_consolidate/skeleton.md`. Every node lists the ledger rows it owns (`claims_ledger.md`, this folder); a row's `merges` ids become the node's impl_pointers (`build/research/<slot>/result.md::<CLAIM-ID>`) and its `sources` ids (`sources.md`) go to design_notes. This file structures the graphs and attaches the evidence; it states no verdict. The placement records list the competing positions for the judges, who work as `judge_plan.md` says.

Pinned:
- Nodes: web-app-philosophy 79 (L0 1, L1 5, L2 25, L3 48); pig-web-defaults 132 (L0 1, L1 5, L2 29, L3 97); total 211, of which 7 deferred.
- Placement nodes: 26 (web-app-philosophy 19, pig-web-defaults 7); the initial 12 responsibilities plus 7 added from the evidence.
- Claims: 793 original claim ids in, 793 placed through 689 ledger rows, each row owned by exactly one node; 0 claims not placed.
- Intentlinks proposed: intra web-app-philosophy 31, intra pig-web-defaults 11, inter pig-web-defaults to web-app-philosophy 60 (25 same-branch refines, 8 placement refines, 27 tier to placement), inter web-app-philosophy to python-kb-philosophy 15.

## How to read

- A node line gives uid, name, the question it decides (not its answer) and the ledger rows it owns. `Lnnn-Lmmm` means every row in the range. `-` means the node owns no row: it is the roll-up of its children, or (for two forces) a criterion the maintainer named that no row states alone.
- A placement record (sections Placement records) adds the competing positions present in the evidence, each with its ledger ids, then the evidence on copies and forbidden tiers, the forces in tension, the context that moves the placement, and the tier nodes that realize it. Positions cite rows wherever they are owned; ownership says where a row is judged, not the only place it is read.
- Deferred nodes (scope out of round 2, recorded, not researched) are marked `[deferred]`.

## Partition rationale

### The cut

- Both graphs share the maintainer's L1 cut, in this order: ALLOCATION, DATA, LOGIC, INTERACTION, TRANSVERSE. `web-app-philosophy` holds the stack-neutral why; `pig-web-defaults` holds the JavaScript, Python and Postgres choices under the same branches.
- L2 follows the maintainer's verbs where the evidence fills them: DATA organize, guard, maintain, derive (PIG-WEB adds concurrency and the database interface); LOGIC secure, enforce, process, expose; INTERACTION visualize, edit, collaborate, agent access, environment (PIG-WEB adds real-time channels); TRANSVERSE security, performance, contracts, operability, evolution (PIG-WEB adds runtime topology). A verb without a principle-level row in the philosophy graph (edit, the database interface) has no philosophy node; inventing one would add a node without grounds.
- Tier branches hold realization only. They do not re-decide allocation: each tier node links to the placement nodes that assign it work (section Intentlinks). A contract sits with the role that offers it: the database function API under PIG-WEB.DATA.INTERFACE (and its placement PIG-WEB.ALLOCATION.DB_API), the HTTP interface under LOGIC.EXPOSE; TRANSVERSE.CONTRACTS keeps only what every contract shares.

### ALLOCATION

- Philosophy ALLOCATION has eight children: FORCES (one child per force the maintainer named: correctness, security, performance, latency, scalability, changeability), CONTEXT (one node), RULES (five rules the evidence supports), and five placement families: RECORD (who owns the data), GUARD (who decides the checks), ACT (who carries the logic that changes data), DERIVE (who computes views of it), PRESENT (who turns it into what users see).
- Placements: the 12 responsibilities of the initial list, some widened by the evidence (UI state to UI and ephemeral state, for presence; audit to audit and history; concurrency control to conflict resolution; business rules to the unit of work), plus 7 the evidence demanded, each with a contest in the ledger:
  - system of record: server database, client replica (local-first) or ordered log (L045, L302, L626);
  - data access interface: application-owned database against a shared database behind a function API (L044 against L515, L622);
  - type and contract definitions: database, application models or API description as the origin (L486, L548, L549, L272);
  - identity and session state: server session, backend-for-frontend or browser-held tokens (L313, L315, L320, L321);
  - duplicate suppression: browser, HTTP contract, server key and database constraint layered (L582, L478, L479);
  - deferred and scheduled work: request, worker or database scheduler (L601, L406, L604, L482);
  - rendering: server hypermedia, client application or hybrid (L252, L629, L253).
- CONTEXT is one node holding the variable list: most variables are grounded by rows that also argue a placement and are owned there (data volume in L613, write load in L615, offline need in L302), so children would own almost nothing. FORCES has children because placements weigh forces against each other and four forces have their own rows.
- PIG-WEB.ALLOCATION holds only the 7 placements where this stack offers competing mechanisms in the evidence (Postgres functions, row security, the type chain, the job and cache hosts, a JavaScript server, Postgres as the backing store for everything). Each refines its stack-neutral placement by an inter link.

### Routing rules

1. One owner per row. A row is owned by the node whose decision it grounds most directly; placement records cite rows owned elsewhere by id.
2. ALLOCATION: a row whose subject is which tier holds a responsibility goes to a placement node, whatever its level. If it is stated in tier terms (database, backend, browser, client) it goes to `web-app-philosophy`; if it names a stack mechanism (a Postgres feature, a Python framework, a JavaScript runtime, a cache service) it goes to `PIG-WEB.ALLOCATION`. Rules 2 and 3 moved 26 round-3 rows from pig-web-defaults to web-app-philosophy (listed at the end of the ledger): 24 placement rows, for example L214, L215, L527, L528 (logic placement), L252 to L255 (rendering) and L313 to L321 (session placement), and 2 stack-neutral principles that round 3 had parked on a PIG-WEB parent (L303, L435). No row moved the other way.
3. Tier branches keep the round-3 routing: principle rows in `web-app-philosophy`, decision and practice rows in `pig-web-defaults`; the language-swap test settles edge cases: principle rows tied to one mechanism stay in PIG-WEB (L148 HSTS, L151 development server, L577 and L591 Postgres semantics).
4. Round 4: a claim that restates an existing row joins its `merges` column with a note on what it adds (24 claims into 23 rows); a claim that adds a position, a mechanism or a new subject gets its own row (84 rows, L606-L689); three round-4 claims merge into another new row.

### Rejected alternatives

- Clusters of the evidence as L1 (ENVIRONMENT, TRUST, CONTRACT, STRUCTURE, CONSISTENCY, MECH): rejected by the maintainer; the old nodes survive as L3 wording where they fit (INTERACTION.ENVIRONMENT.1-.7, TRANSVERSE.EVOLUTION.1-.5).
- A single PLACEMENT child holding all placements (a literal mirror of the four bullets of the target hierarchy): one parent with 19 children, every placement at L4 with all-numeric uids. Families keep each placement an L3 with a meaningful prefix and give each family a roll-up claim.
- Placements directly under ALLOCATION: 22 L2 children, same objection.
- Mirroring all 19 placements in PIG-WEB.ALLOCATION: 12 of them would own no stack-specific row; nodes without grounds were not created.
- Consistency and contracts as their own L1 (round 3): the target hierarchy has neither. Consistency splits into placements (GUARD.5, GUARD.6, ACT.2, ACT.3) and realization (DATA.GUARD, PIG-WEB.DATA.CONCURRENCY, PIG-WEB.LOGIC.PROCESS.2); contracts sit with their offering role.
- Runtime topology under LOGIC: the proxy, CDN, worker and image decisions span tiers, so PIG-WEB.TRANSVERSE.TOPOLOGY holds them and refines the philosophy's LOGIC.PROCESS, which holds the process-model principles.

### Tensions the judges will meet (pointers, no verdict)

- Shared database with a function API (L515, doctrine) against one application owning its database (L044, research); placement ALLOCATION.RECORD.2.
- Database-heavy logic (L528, L584, L616) against application first (L215); placement ALLOCATION.ACT.1.
- Soft delete by default (L520, doctrine) against hard delete plus archive (L204); node PIG-WEB.DATA.MAINTAIN.2.
- updated_at written by code (L529) against a narrow trigger (L216); node PIG-WEB.DATA.GUARD.4.
- Views as a contract (L187, L518) against views off the contract path (L516); placement PIG-WEB.ALLOCATION.DB_API.

## Tree: `web-app-philosophy`

```text
ROOT  Web App Philosophy  (L001)
    ALLOCATION  Allocation of Responsibilities  (L610)
        ALLOCATION.FORCES  Allocation Forces  (-)
            ALLOCATION.FORCES.1  Correctness  (-)
            ALLOCATION.FORCES.2  Security  (-)
            ALLOCATION.FORCES.3  Performance  (L097)
            ALLOCATION.FORCES.4  Latency  (L012, L013)
            ALLOCATION.FORCES.5  Scalability  (L615)
            ALLOCATION.FORCES.6  Changeability  (L042, L472)
        ALLOCATION.CONTEXT  Allocation Context  (L041, L621)
        ALLOCATION.RULES  Allocation Rules  (-)
            ALLOCATION.RULES.1  Authority and Copies  (L072, L481, L609)
            ALLOCATION.RULES.2  End-to-End Placement  (L606-L608)
            ALLOCATION.RULES.3  Trust Boundary  (L019)
            ALLOCATION.RULES.4  One Core for Every Client  (L633)
            ALLOCATION.RULES.5  Atomicity Ends at the Transaction  (L477, L623)
        ALLOCATION.RECORD  Data Authority Placements  (-)
            ALLOCATION.RECORD.1  System of Record  (L045, L302)
            ALLOCATION.RECORD.2  Data Access Interface  (L044, L622)
            ALLOCATION.RECORD.3  Type and Contract Definitions  (L486)
        ALLOCATION.GUARD  Guarding Placements  (-)
            ALLOCATION.GUARD.1  Validation  (L484, L611, L612)
            ALLOCATION.GUARD.2  Invariants  (L040, L471, L473)
            ALLOCATION.GUARD.3  Authorization  (L020, L468, L620, L644)
            ALLOCATION.GUARD.4  Identity and Session State  (L022, L313-L316, L318-L321)
            ALLOCATION.GUARD.5  Concurrency Control and Conflict Resolution  (L475, L628, L674, L678)
            ALLOCATION.GUARD.6  Duplicate Suppression  (L051, L478, L479, L582)
        ALLOCATION.ACT  Acting Placements  (-)
            ALLOCATION.ACT.1  Business Rules and State Transitions  (L066, L214, L215, L527, L528, L584, L596, L616)
            ALLOCATION.ACT.2  Side Effects and Integrations  (L480, L624)
            ALLOCATION.ACT.3  Deferred and Scheduled Work  (L406, L482, L601)
            ALLOCATION.ACT.4  Audit and History  (L049, L627, L658, L684)
        ALLOCATION.DERIVE  Derivation Placements  (-)
            ALLOCATION.DERIVE.1  Derived Data and Aggregation  (L625, L626)
            ALLOCATION.DERIVE.2  Filtering, Sorting, Paging and Search  (L613)
            ALLOCATION.DERIVE.3  Caching  (L534)
        ALLOCATION.PRESENT  Presentation Placements  (-)
            ALLOCATION.PRESENT.1  Rendering  (L016, L252-L255, L281, L629, L630)
            ALLOCATION.PRESENT.2  Formatting and Localization  (L632)
            ALLOCATION.PRESENT.3  UI and Ephemeral State  (L070, L071, L631, L681)
    DATA  Durable Data  (-)
        DATA.ORGANIZE  Organized Facts  (L037-L039, L469, L470)
        DATA.GUARD  Guarded Consistency  (L043, L476, L485)
        DATA.MAINTAIN  Maintained Over Time  (L046, L047, L474)
        DATA.DERIVE  Derived, Not Stored  (L488)
    LOGIC  Business Logic Tier  (-)
        LOGIC.SECURE  Secured Entry  (L021, L023, L031-L034)
        LOGIC.ENFORCE  Business Core  (L062-L065, L067)
        LOGIC.PROCESS  Processing Model  (L086-L094)
        LOGIC.EXPOSE  Backend Interface  (-)
            LOGIC.EXPOSE.1  Protocol Semantics  (L050, L052, L053)
            LOGIC.EXPOSE.2  Self-Contained Requests  (L054, L055)
            LOGIC.EXPOSE.3  Hypermedia Controls  (L059-L061)
    INTERACTION  Interaction  (-)
        INTERACTION.VISUALIZE  Perceivable Interface  (L005)
        INTERACTION.COLLABORATE  Collaboration on Data  (L006, L435, L664, L682, L686, L687)
        INTERACTION.AGENT  Agent Access  (L640, L642, L645, L648, L652)
        INTERACTION.ENVIRONMENT  Web Environment  (-)
            INTERACTION.ENVIRONMENT.1  Uncontrolled Client Runtime  (L002-L004)
            INTERACTION.ENVIRONMENT.2  Unstable Page Lifecycle  (L007, L008)
            INTERACTION.ENVIRONMENT.3  Non-Atomic Deployment  (L009)
            INTERACTION.ENVIRONMENT.4  Caches Beyond Reach  (L010, L011)
            INTERACTION.ENVIRONMENT.5  Unreliable Network  (L014)
            INTERACTION.ENVIRONMENT.6  URL as Public Interface  (L017, L018)
            INTERACTION.ENVIRONMENT.7  Hostile Page Script  (L024-L028)
    TRANSVERSE  Transverse Concerns  (-)
        TRANSVERSE.SECURITY  Security Across Tiers  (L029, L030, L035, L036, L303)
        TRANSVERSE.PERFORMANCE  Measured Performance  (L015)
        TRANSVERSE.CONTRACTS  Standards and Contracts  (L056-L058, L483, L487)
        TRANSVERSE.OPERABILITY  Operability  (-)
            TRANSVERSE.OPERABILITY.1  Whole-Path Observability  (L048, L095, L096, L098)
            TRANSVERSE.OPERABILITY.2  Proportioned Testing  (L099)
            TRANSVERSE.OPERABILITY.3  Reproducible Delivery  (L100-L104)
        TRANSVERSE.EVOLUTION  Deliberate Evolution  (-)
            TRANSVERSE.EVOLUTION.1  Explicit Decisions  (L105, L106)
            TRANSVERSE.EVOLUTION.2  Incremental Change  (L107-L112)
            TRANSVERSE.EVOLUTION.3  Deployable Boundaries  (L073-L080)
            TRANSVERSE.EVOLUTION.4  Few Mature Technologies  (L081-L085)
            TRANSVERSE.EVOLUTION.5  Team-Shaped Structure  (L068, L069)
```

Nodes: 79 (L0 1, L1 5, L2 25, L3 48).

## Nodes: `web-app-philosophy`

| uid | name | decides | owns |
|---|---|---|---|
| ROOT | Web App Philosophy | What a web application is (users, human or agent, interacting with data under business logic) and which principles govern its design as a whole rather than a backend or a database alone. | L001 |
| ALLOCATION | Allocation of Responsibilities | For every responsibility of the application, which tier (database, backend, browser) is its authority, which tiers may hold copies and which may not hold it, from stated forces, context and rules; decided before any tier is designed. | L610 |
| ALLOCATION.FORCES | Allocation Forces | Which forces a placement trades against each other, and what each force demands of the tier that takes a responsibility. | - |
| ALLOCATION.FORCES.1 | Correctness | What correctness demands of a placement: the deciding tier sees every writer and every fact the decision needs. | - |
| ALLOCATION.FORCES.2 | Security | What security demands of a placement: a decision that grants access or protects integrity runs where the requester cannot alter it. | - |
| ALLOCATION.FORCES.3 | Performance | What performance demands of a placement: work runs where its data is, set-based where possible, and moves only on measured need. | L097 |
| ALLOCATION.FORCES.4 | Latency | What latency demands of a placement: few round trips and responses within human perception budgets, which may justify copies near the user. | L012, L013 |
| ALLOCATION.FORCES.5 | Scalability | What scalability demands of a placement: weigh each one against the tier that is hardest to scale out. | L615 |
| ALLOCATION.FORCES.6 | Changeability | What changeability demands of a placement: deploy cadence, testability, tooling and team skill of the tier that holds the responsibility. | L042, L472 |
| ALLOCATION.CONTEXT | Allocation Context | Which project variables move a placement and in which direction: database consumers, client kinds including agents, offline need, latency budget, data volume against result size, write load, team SQL skill, policy change cadence, domain complexity, DBMS commitment. | L041, L621 |
| ALLOCATION.RULES | Allocation Rules | Which rules turn forces and context into a placement, applied the same way to every responsibility. | - |
| ALLOCATION.RULES.1 | Authority and Copies | How the one authoritative tier of a responsibility relates to copies held elsewhere, and what a copy must carry to be safe. | L072, L481, L609 |
| ALLOCATION.RULES.2 | End-to-End Placement | How to identify the ends that can complete a function correctly, and when a partial copy in another tier is justified. | L606-L608 |
| ALLOCATION.RULES.3 | Trust Boundary | Which tiers may hold a decision that grants access or protects integrity, given who controls each tier. | L019 |
| ALLOCATION.RULES.4 | One Core for Every Client | How browsers, agents, jobs and other programs drive the same business core without copies of its rules. | L633 |
| ALLOCATION.RULES.5 | Atomicity Ends at the Transaction | What can be made atomic, and how effects that cross a transaction or system boundary are handled instead. | L477, L623 |
| ALLOCATION.RECORD | Data Authority Placements | Which tier owns the durable data, the interface through which consumers reach it, and the definition of its shapes. | - |
| ALLOCATION.RECORD.1 | System of Record | Which tier holds the authoritative copy of durable business data, and which stores are derived from it. | L045, L302 |
| ALLOCATION.RECORD.2 | Data Access Interface | Through which interface other consumers (backends, reports, agents) reach the data, and who owns that interface. | L044, L622 |
| ALLOCATION.RECORD.3 | Type and Contract Definitions | Which tier holds the origin definition of a data shape from which the other tiers derive their types and contracts. | L486 |
| ALLOCATION.GUARD | Guarding Placements | Which tiers decide, and which only echo, the checks that keep data correct and access controlled. | - |
| ALLOCATION.GUARD.1 | Validation | Where input is checked for syntax and for meaning, which check decides and which only gives feedback. | L484, L611, L612 |
| ALLOCATION.GUARD.2 | Invariants | Which tier enforces the rules that must hold whatever code writes the data, and which tiers may mirror them. | L040, L471, L473 |
| ALLOCATION.GUARD.3 | Authorization | Which tier is the authority for access decisions, which tiers may add a layer, and which may never decide. | L020, L468, L620, L644 |
| ALLOCATION.GUARD.4 | Identity and Session State | Which tier holds the authenticated session and the credentials, and what the browser may hold of them. | L022, L313-L316, L318-L321 |
| ALLOCATION.GUARD.5 | Concurrency Control and Conflict Resolution | Which tier detects and resolves concurrent changes to the same data, with which conflict policy per kind of data. | L475, L628, L674, L678 |
| ALLOCATION.GUARD.6 | Duplicate Suppression | Which tier recognizes a repeated request so that its effect happens once, and which tiers only reduce repeats. | L051, L478, L479, L582 |
| ALLOCATION.ACT | Acting Placements | Which tiers carry the business logic that changes data, and its consequences in time and outside the system. | - |
| ALLOCATION.ACT.1 | Business Rules and State Transitions | Which tier holds business rules, state transitions and the unit of work of an operation, between database and backend. | L066, L214, L215, L527, L528, L584, L596, L616 |
| ALLOCATION.ACT.2 | Side Effects and Integrations | Which tier performs effects on external systems, and how those effects are tied to the data change that causes them. | L480, L624 |
| ALLOCATION.ACT.3 | Deferred and Scheduled Work | Which work runs inside the request and which later, and which tier hosts the later work. | L406, L482, L601 |
| ALLOCATION.ACT.4 | Audit and History | Where the record of who changed what is written so that it is complete and attributable. | L049, L627, L658, L684 |
| ALLOCATION.DERIVE | Derivation Placements | Which tiers compute views of the data: derived values, query results and cached copies. | - |
| ALLOCATION.DERIVE.1 | Derived Data and Aggregation | Which tier maintains derived data and aggregates, and how freshly and how atomically with their source. | L625, L626 |
| ALLOCATION.DERIVE.2 | Filtering, Sorting, Paging and Search | Which tier reduces many rows to the few a client needs. | L613 |
| ALLOCATION.DERIVE.3 | Caching | Which tiers may keep cached copies of data or responses, and how their staleness is bounded. | L534 |
| ALLOCATION.PRESENT | Presentation Placements | Which tiers turn data into what users see and hold the state of their interaction. | - |
| ALLOCATION.PRESENT.1 | Rendering | Which tier produces the user interface from the data and holds the logic of navigation and display. | L016, L252-L255, L281, L629, L630 |
| ALLOCATION.PRESENT.2 | Formatting and Localization | Which tier formats values for a reader and in which form values are stored. | L632 |
| ALLOCATION.PRESENT.3 | UI and Ephemeral State | Where each kind of interaction state lives: view, form, URL, server copy, presence. | L070, L071, L631, L681 |
| DATA | Durable Data | How the database carries out the work the placements give it: organizing facts, guarding them, keeping them correct over time, and deriving values. | - |
| DATA.ORGANIZE | Organized Facts | How facts are shaped so that each is stored once and changed in one place. | L037-L039, L469, L470 |
| DATA.GUARD | Guarded Consistency | How the database keeps data valid and consistent under concurrent and partial change. | L043, L476, L485 |
| DATA.MAINTAIN | Maintained Over Time | How schema and data evolve without breaking running code, and what is the source of truth for structure. | L046, L047, L474 |
| DATA.DERIVE | Derived, Not Stored | What is stored and what is derived from stored facts. | L488 |
| LOGIC | Business Logic Tier | How the backend carries out the work the placements give it: securing entry, enforcing business logic, processing work and exposing its interface. | - |
| LOGIC.SECURE | Secured Entry | How the backend authenticates callers, treats their input as untrusted and bounds what they can consume. | L021, L023, L031-L034 |
| LOGIC.ENFORCE | Business Core | How the business logic is structured so that it is separable from transport and storage and testable alone. | L062-L065, L067 |
| LOGIC.PROCESS | Processing Model | How the backend runs its work: stateless, disposable processes of distinct types, with durable state in backing services. | L086-L094 |
| LOGIC.EXPOSE | Backend Interface | How the backend offers its interface to browsers, agents and other programs. | - |
| LOGIC.EXPOSE.1 | Protocol Semantics | How requests and errors use the defined meanings of HTTP. | L050, L052, L053 |
| LOGIC.EXPOSE.2 | Self-Contained Requests | How each request carries what is needed to serve it, so client and server stay independent. | L054, L055 |
| LOGIC.EXPOSE.3 | Hypermedia Controls | Whether server representations drive client transitions, and what that buys or costs. | L059-L061 |
| INTERACTION | Interaction | How users, human or agent, see, edit and discuss the data through clients the team does not control. | - |
| INTERACTION.VISUALIZE | Perceivable Interface | How the interface stays usable by everyone, people with disabilities included. | L005 |
| INTERACTION.COLLABORATE | Collaboration on Data | How several users discuss and change the same data and learn of each other's changes. | L006, L435, L664, L682, L686, L687 |
| INTERACTION.AGENT | Agent Access | How agents act as users with bounded authority, verifiable identity and limited consumption. | L640, L642, L645, L648, L652 |
| INTERACTION.ENVIRONMENT | Web Environment | Which properties of browsers, networks, caches and URLs the design must accept as given. | - |
| INTERACTION.ENVIRONMENT.1 | Uncontrolled Client Runtime | How the design copes with browsers of unknown capability, speed and script completion. | L002-L004 |
| INTERACTION.ENVIRONMENT.2 | Unstable Page Lifecycle | How state and side effects survive pages that are restored, frozen, discarded or open in several tabs. | L007, L008 |
| INTERACTION.ENVIRONMENT.3 | Non-Atomic Deployment | How client and server changes coexist while old pages run against a new server. | L009 |
| INTERACTION.ENVIRONMENT.4 | Caches Beyond Reach | How responses stored by caches the team cannot purge are anticipated. | L010, L011 |
| INTERACTION.ENVIRONMENT.5 | Unreliable Network | How the client keeps core function when requests or scripts fail. | L014 |
| INTERACTION.ENVIRONMENT.6 | URL as Public Interface | How URLs serve as stable public addresses and as the contract for navigable state. | L017, L018 |
| INTERACTION.ENVIRONMENT.7 | Hostile Page Script | How the design limits what script running in the page with the application's privileges can do. | L024-L028 |
| TRANSVERSE | Transverse Concerns | Which concerns span every tier and are stated once: security, performance, contracts, operability and evolution. | - |
| TRANSVERSE.SECURITY | Security Across Tiers | Which security properties hold for the whole system: transport, minimal exposure, and the map of threats to owning tiers. | L029, L030, L035, L036, L303 |
| TRANSVERSE.PERFORMANCE | Measured Performance | What counts as the truth about performance and how it is measured. | L015 |
| TRANSVERSE.CONTRACTS | Standards and Contracts | How every contract between tiers is made explicit and evolves compatibly. | L056-L058, L483, L487 |
| TRANSVERSE.OPERABILITY | Operability | How the running system is observed, tested and delivered as one whole. | - |
| TRANSVERSE.OPERABILITY.1 | Whole-Path Observability | How signals from every tier are designed to be correlated, what is logged and how long it is kept. | L048, L095, L096, L098 |
| TRANSVERSE.OPERABILITY.2 | Proportioned Testing | How the test suite is proportioned across levels. | L099 |
| TRANSVERSE.OPERABILITY.3 | Reproducible Delivery | How code, configuration and artifacts move from commit to production reproducibly. | L100-L104 |
| TRANSVERSE.EVOLUTION | Deliberate Evolution | How the system and its structure change deliberately over time. | - |
| TRANSVERSE.EVOLUTION.1 | Explicit Decisions | How the costly decisions are identified, chosen from properties, and recorded. | L105, L106 |
| TRANSVERSE.EVOLUTION.2 | Incremental Change | How the system grows in small, tested increments without speculative features. | L107-L112 |
| TRANSVERSE.EVOLUTION.3 | Deployable Boundaries | When and where the system is split into separately deployed units. | L073-L080 |
| TRANSVERSE.EVOLUTION.4 | Few Mature Technologies | How many and which technologies the system adopts. | L081-L085 |
| TRANSVERSE.EVOLUTION.5 | Team-Shaped Structure | How team structure and system structure are designed together. | L068, L069 |

## Placement records: `web-app-philosophy`

#### ALLOCATION.RECORD.1 System of Record

Decides: Which tier holds the authoritative copy of durable business data, and which stores are derived from it. Owns: L045, L302.

Positions in the evidence:
- P1 Server database is the single system of record: caches, indexes, client state and messages are derived copies of it; no dual writes from application code (L045, L609, L482, L071).
- P2 Client replica is primary (local-first): each device holds the primary copy and syncs in the background; the server is a sync peer (L302).
- P3 Ordered log is the truth: the database and caches are views derived from an ordered log by a dedicated process (L626, L045).

Evidence on copies, forbidden tiers and limits: a CRDT replica cannot enforce server rules on each operation; derived stores must not be written twice (L680, L045).
Forces in tension: correctness against latency (and offline availability); scalability for the log position. Context that moves it: offline need, latency budget, governed versus user-owned data, number of derived stores, write rate.
Realized or refined by: DATA.ORGANIZE (realizes), PIG-WEB.INTERACTION.ENVIRONMENT.2 (requires).

#### ALLOCATION.RECORD.2 Data Access Interface

Decides: Through which interface other consumers (backends, reports, agents) reach the data, and who owns that interface. Owns: L044, L622.

Positions in the evidence:
- P1 One application owns the database: other consumers reach the data through that application's service or a read-only reporting copy; expose operations, never the schema, across a team boundary (L044, L622, L621).
- P2 Shared database behind a database function API: several backends in different languages share one database; the function signature is the contract, owned by the database owner (L515, L517, L617, L616).
- P3 The schema is the API: a dedicated schema of views and functions (PostgREST style) is the contract; base tables stay hidden (L518, L618, L187).
- P4 Base tables through the ORM: consumers use base tables with migration discipline; simple reads may query tables directly (L187, L516).

Evidence on copies, forbidden tiers and limits: L515 (doctrine) contradicts L044 and its sources; L622 (SQL is anti-encapsulation) is in tension with L618 (L515, L044, L622, L618).
Forces in tension: changeability (coupling, team autonomy) against correctness (one rule for all consumers) and security (object-level grants). Context that moves it: number of database consumers, whether consumers sit inside or outside the owning team, team SQL skill.
Realized or refined by: LOGIC.EXPOSE (realizes), PIG-WEB.ALLOCATION.DB_API (refines).

#### ALLOCATION.RECORD.3 Type and Contract Definitions

Decides: Which tier holds the origin definition of a data shape from which the other tiers derive their types and contracts. Owns: L486.

Positions in the evidence:
- P1 Database schema first: the live database is the source of truth for structure; precise types (NOT NULL, CHECK, domains) carry meaning; application models follow (L474, L485, L549).
- P2 Application models first (code-first): typed application models generate the API description, which becomes a build artifact (L548, L549).
- P3 API description first (design-first): the description is written before the code and is the source of truth; humans, code generators and agents read one description (L272, L634).
- P4 Readers take what they use: consumers read only the elements they need rather than generating code from the full producer schema (L556).

Evidence on copies, forbidden tiers and limits: one source of truth per fact; hand-copied types across tiers create out-of-sync states; generated browser types are build-time only (L486, L555).
Forces in tension: correctness (no drift between tiers) against changeability (who can change a shape, and how fast). Context that moves it: one team owning both ends versus independent consumers; number of consumers; agent consumers.
Realized or refined by: DATA.MAINTAIN (realizes), TRANSVERSE.CONTRACTS (requires), PIG-WEB.ALLOCATION.TYPE_CHAIN (refines).

#### ALLOCATION.GUARD.1 Validation

Decides: Where input is checked for syntax and for meaning, which check decides and which only gives feedback. Owns: L484, L611, L612.

Positions in the evidence:
- P1 Validate at every trust crossing: internal transports, queues and stored records are re-validated by each receiving component (L612).
- P2 Parse once at the boundary: convert input into the most precise type once, at the system boundary, and trust the type after (L484, L612).
- P3 Split by kind: syntax at the edge nearest the input, meaning in the tier that holds the state (L611).

Evidence on copies, forbidden tiers and limits: browser checks are feedback only and are always repeated on the server; database constraints are the last guard and application validation an optimisation (L019, L471).
Forces in tension: security and correctness against latency of feedback and changeability. Context that moves it: whether tiers have different owners or trust levels; type system available at the boundary.
Realized or refined by: LOGIC.SECURE (realizes), PIG-WEB.LOGIC.EXPOSE.6 (realizes).

#### ALLOCATION.GUARD.2 Invariants

Decides: Which tier enforces the rules that must hold whatever code writes the data, and which tiers may mirror them. Owns: L040, L471, L473.

Positions in the evidence:
- P1 Declare in the database: rules that must hold whatever writes the data are database constraints; application check-then-write is correct only under serializable isolation (L040, L473, L471).
- P2 Application-only validation: the ORM or application code validates; recorded only as common practice (T4) and rejected by L473 for uniqueness (L040, L473).
- P3 Database functions and triggers for multi-row rules: integrity beyond row-local constraints (multi-table validation, cascades) runs in database code (L528, L471).

Evidence on copies, forbidden tiers and limits: application types and validators mirror database constraints for early feedback; the data store is an end for rules about stored data (L495, L485, L608).
Forces in tension: correctness against changeability (testing needs a live database, tooling). Context that moves it: number of writers and code paths (scripts, migrations, consoles, agents); team SQL skill.
Realized or refined by: DATA.GUARD (realizes), PIG-WEB.DATA.GUARD.1 (realizes).

#### ALLOCATION.GUARD.3 Authorization

Decides: Which tier is the authority for access decisions, which tiers may add a layer, and which may never decide. Owns: L020, L468, L620, L644.

Positions in the evidence:
- P1 Backend only: one central server-side mechanism checks every request, object-level rules included (L020, L620, L305, L306).
- P2 Database enforces: roles and row-level security make the database decide visibility on every access path, including paths that skip the backend (L619, L620, L688).
- P3 Two layers: database permissions limit which objects can be touched; application permissions decide business actions; row security, where used, keeps application checks (L468, L620, L128).

Evidence on copies, forbidden tiers and limits: the browser never decides access; model output and client-supplied hints never decide (L019, L644, L650).
Forces in tension: security against changeability of policy. Context that moves it: number of access paths (agents, consoles, several backends), policy change cadence, assurance level.
Realized or refined by: LOGIC.SECURE (realizes), INTERACTION.COLLABORATE (requires), INTERACTION.AGENT (requires), PIG-WEB.INTERACTION.AGENT.4 (requires), PIG-WEB.ALLOCATION.ROW_SECURITY (refines).

#### ALLOCATION.GUARD.4 Identity and Session State

Decides: Which tier holds the authenticated session and the credentials, and what the browser may hold of them. Owns: L022, L313-L316, L318-L321.

Positions in the evidence:
- P1 Server-held opaque session: the server keeps session state and can revoke it; the browser holds only an HttpOnly cookie (L315, L022, L319, L086).
- P2 Backend-for-frontend holds the tokens: the server is the confidential OAuth client and proxies resource calls; the browser holds only a cookie session; token-mediating and browser-only clients are fallbacks (L313, L314).
- P3 Browser application holds bearer tokens: tokens in memory (or local storage when lifetimes are short); preventing XSS matters more than the storage location (L316, L320, L321).
- P4 No application state in cookies: cookie-based applications are unreliable (REST purist position) (L318).

Evidence on copies, forbidden tiers and limits: stateless tokens cannot be revoked without server state; bearer tokens fit clients that are not a same-site page (L022, L316).
Forces in tension: security (theft, revocation) against scalability and latency (stateless verification). Context that moves it: same-site first-party browser versus mobile, third-party or agent clients; need for instant revocation.
Realized or refined by: LOGIC.SECURE (realizes), LOGIC.PROCESS (constrains), PIG-WEB.LOGIC.SECURE.2 (realizes), PIG-WEB.LOGIC.SECURE.4 (realizes), PIG-WEB.INTERACTION.AGENT.3 (realizes).

#### ALLOCATION.GUARD.5 Concurrency Control and Conflict Resolution

Decides: Which tier detects and resolves concurrent changes to the same data, with which conflict policy per kind of data. Owns: L475, L628, L674, L678.

Positions in the evidence:
- P1 The database decides: isolation levels, locks and constraints, because the database sees every writer (L628, L473, L568).
- P2 Optimistic version across requests: a version check validated inside one short transaction at write time; a stale write is rejected (L475, L260).
- P3 Pessimistic checkout: a lease with owner and expiry when conflicts are frequent and lost work is costly (L570).
- P4 Silent last-writer-wins per property: accepted where different users rarely edit the same property (L674).
- P5 Merge on the client: text engines or CRDT replicas merge concurrent edits (L677, L302).

Evidence on copies, forbidden tiers and limits: the strategy follows the data shape (discrete fields versus long text) (L678, L679).
Forces in tension: correctness (no lost update) against latency and user effort. Context that moves it: conflict rate, data shape, length of edits, offline use.
Realized or refined by: DATA.GUARD (realizes), INTERACTION.COLLABORATE (realizes), PIG-WEB.DATA.CONCURRENCY (realizes), PIG-WEB.INTERACTION.EDIT (realizes), PIG-WEB.INTERACTION.COLLABORATE.3 (realizes).

#### ALLOCATION.GUARD.6 Duplicate Suppression

Decides: Which tier recognizes a repeated request so that its effect happens once, and which tiers only reduce repeats. Owns: L051, L478, L479, L582.

Positions in the evidence:
- P1 Idempotent by design: methods, upserts and client-supplied identifiers make repeats harmless (L051, L655, L587, L588).
- P2 Idempotency key recorded with the effect: the server stores the key atomically with the effect and replays the first response (L269, L546, L270, L599).
- P3 Layered across tiers: the browser disables resubmission, a successful POST answers 303, the server checks a key or form token, a unique constraint is the backstop (L582).

Evidence on copies, forbidden tiers and limits: exactly-once is unavailable across a network boundary; a lost commit acknowledgement leaves the client unsure (L478, L479).
Forces in tension: correctness of effects against simplicity. Context that moves it: automated callers and agents (retries likelier), payment-like or external effects.
Realized or refined by: LOGIC.EXPOSE (realizes), INTERACTION.AGENT (requires), PIG-WEB.DATA.CONCURRENCY.4 (realizes), PIG-WEB.LOGIC.EXPOSE.3 (realizes), PIG-WEB.INTERACTION.EDIT (realizes).

#### ALLOCATION.ACT.1 Business Rules and State Transitions

Decides: Which tier holds business rules, state transitions and the unit of work of an operation, between database and backend. Owns: L066, L214, L215, L527, L528, L584, L596, L616.

Positions in the evidence:
- P1 Application first: domain logic in the backend for modifiability; profile and move proven hot spots into SQL; the use-case layer owns the transaction boundary (L215, L066, L226).
- P2 Split by kind: invariants in the database, workflow and policy in the application, presentation in the browser; the middle zone (multi-row validation, state transitions, cascades) is disputed (L214).
- P3 Database behind a cost-benefit gate: a function only for reuse by two or more consumers, hiding internals, tunable performance or integrity beyond constraints; cascades, multi-table validation, operations used by several backends and set-based algorithms live in the database; one authoritative writer per state column (L527, L528, L584, L596).
- P4 Thick database (SmartDB): as much processing as possible inside the database, behind entry points per use (L616, L617).

Evidence on copies, forbidden tiers and limits: business rules are not duplicated in agent adapters or prompts (L633).
Forces in tension: changeability (testability, tooling, skill) against correctness across several writers and performance of set work. Context that moves it: number of consumers, team SQL skill, policy change cadence, domain complexity, DBMS commitment (L042, L472, L041, L621, L613).
Realized or refined by: LOGIC.ENFORCE (realizes), PIG-WEB.DATA.GUARD.4 (realizes), PIG-WEB.DATA.CONCURRENCY.6 (realizes), PIG-WEB.LOGIC.ENFORCE.1 (realizes).

#### ALLOCATION.ACT.2 Side Effects and Integrations

Decides: Which tier performs effects on external systems, and how those effects are tied to the data change that causes them. Owns: L480, L624.

Positions in the evidence:
- P1 Backend effects staged in the database: the backend owns external calls; the intent is written in the same transaction as the change and delivered after commit by a separate process to idempotent consumers (L624, L409, L410).
- P2 Post-commit hooks in the request process: for losable work only; lost if the process dies after commit (L600, L233).
- P3 Atomic phases with recovery points: local transactions between foreign calls, idempotency keys passed on, completer and reaper (L589, L234, L246).
- P4 Sagas with compensation: only when a business transaction spans services with separate databases; compensation is a business operation (L590, L480).

Evidence on copies, forbidden tiers and limits: the browser holds no third-party credentials (inferred) (L624).
Forces in tension: correctness (no lost or doubled effect) against latency of the request. Context that moves it: whether effects cross a service or vendor boundary; whether the effect may be lost.
Realized or refined by: PIG-WEB.LOGIC.PROCESS.2 (realizes), PIG-WEB.INTERACTION.COLLABORATE.4 (realizes).

#### ALLOCATION.ACT.3 Deferred and Scheduled Work

Decides: Which work runs inside the request and which later, and which tier hosts the later work. Owns: L406, L482, L601.

Positions in the evidence:
- P1 Inside the request what the user sees next: validate, perform every change atomic with the next view, persist the intent of deferred work in the same transaction; defer foreign effects, long work and fan-out (L601).
- P2 Separate worker processes: slow or non-essential work runs in workers fed by a task queue (L406, L407).
- P3 Scheduled work inside the database: a scheduler extension calls named functions in the data transaction context (L604).
- P4 Asynchrony only for derived data and bulk jobs: core writes are synchronous; asynchronous work has a stated staleness window; long data jobs are run by a human (L482, L545).

Evidence on copies, forbidden tiers and limits: 202 with a status resource (L271, L602).
Forces in tension: latency against correctness and scalability. Context that moves it: duration of the work, foreign effects, whether the work is set-based data work.
Realized or refined by: PIG-WEB.DATA.MAINTAIN.4 (realizes), PIG-WEB.LOGIC.EXPOSE.3 (realizes), PIG-WEB.ALLOCATION.POSTGRES_FIRST (refines), PIG-WEB.ALLOCATION.JOB_HOST (refines).

#### ALLOCATION.ACT.4 Audit and History

Decides: Where the record of who changed what is written so that it is complete and attributable. Owns: L049, L627, L658, L684.

Positions in the evidence:
- P1 Where writes converge, atomically: a database trigger or log writes history in the same transaction, with the actor passed in (L627, L684, L212, L566).
- P2 Application-level history: knows the business actor and is easier to test, but bulk operations and raw SQL escape it (L627, L208).
- P3 Two separate records: the security event log and the business audit trail differ in purpose, storage, integrity and retention (L049, L392).

Evidence on copies, forbidden tiers and limits: evidence for agents: every agent action is recorded on the server with actor and delegating subject, never only in a model transcript (L658, L659).
Forces in tension: correctness (completeness) against changeability (hidden behaviour, testability). Context that moves it: number of writers, ad-hoc SQL paths, agents, need for business-level events.
Realized or refined by: INTERACTION.AGENT (requires), TRANSVERSE.OPERABILITY.1 (conflicts), PIG-WEB.DATA.MAINTAIN.3 (realizes), PIG-WEB.TRANSVERSE.OPERABILITY.4 (conflicts).

#### ALLOCATION.DERIVE.1 Derived Data and Aggregation

Decides: Which tier maintains derived data and aggregates, and how freshly and how atomically with their source. Owns: L625, L626.

Positions in the evidence:
- P1 Inside the database, with the source: generated columns, triggers, cache tables with an invalidation queue; sync level chosen per copy (L176, L532, L534, L536).
- P2 From an ordered log by a dedicated process: one order of writes for all derived stores, no invalidation races (L626, L045).
- P3 Computed on read: store the minimum and derive the rest (L488).

Evidence on copies, forbidden tiers and limits: tier chosen by required freshness and atomicity with the source; application dual writes are rejected (L625, L045).
Forces in tension: correctness against performance and scalability. Context that moves it: number of derived stores, write rate, staleness tolerance, stream infrastructure the team can run.
Realized or refined by: DATA.DERIVE (realizes), PIG-WEB.DATA.DERIVE.1 (realizes).

#### ALLOCATION.DERIVE.2 Filtering, Sorting, Paging and Search

Decides: Which tier reduces many rows to the few a client needs. Owns: L613.

Positions in the evidence:
- P1 With the data: filtering, aggregation, sorting and paging are set-based in the database; only the result travels; one statement, no queries in loops (L613, L614).
- P2 Reads bypass the domain model: hand-written SQL, views or read stores serve reads that need no domain behaviour (L237).
- P3 In the backend or browser on a loaded set: no row in the evidence argues for it (open) (no row).

Evidence on copies, forbidden tiers and limits: server-enforced page size, continuation tokens, keyset paging; per-request computation weighs on the hardest tier to scale; search is deferred (L265, L266, L541, L615).
Forces in tension: performance and latency against scalability. Context that moves it: data volume against result size, write load.
Realized or refined by: PIG-WEB.LOGIC.ENFORCE.3 (realizes), PIG-WEB.LOGIC.EXPOSE.1 (realizes).

#### ALLOCATION.DERIVE.3 Caching

Decides: Which tiers may keep cached copies of data or responses, and how their staleness is bounded. Owns: L534.

Positions in the evidence:
- P1 Cache tables in the database: derived caches share the source transaction, invalidate atomically and are queryable (L534, L535).
- P2 Shared cache service: an application cache shared across processes; never permanent storage (L417).
- P3 HTTP caches in browsers and intermediaries: every response labelled cacheable or not; lifetime set by tolerable staleness (L010, L414, L415, L416).
- P4 Server state cached in the browser: a dedicated client cache with background refresh (L071, L291).

Evidence on copies, forbidden tiers and limits: per-process memory in multi-process production; every cache needs an expiry or invalidation plan (L417, L419).
Forces in tension: latency and performance against correctness (staleness). Context that moves it: staleness tolerance, number of processes, need for atomic invalidation.
Realized or refined by: LOGIC.PROCESS (constrains), INTERACTION.ENVIRONMENT.4 (constrains), PIG-WEB.ALLOCATION.POSTGRES_FIRST (refines), PIG-WEB.ALLOCATION.CACHE_STORE (refines).

#### ALLOCATION.PRESENT.1 Rendering

Decides: Which tier produces the user interface from the data and holds the logic of navigation and display. Owns: L016, L252-L255, L281, L629, L630.

Positions in the evidence:
- P1 Server-rendered hypermedia: business logic, state and rendering stay on the server; HTML is the contract; behaviour stays local to the element (L252, L629, L630, L003).
- P2 Client-rendered application over a JSON API: the browser renders and holds substantial state (L252, L253).
- P3 Hybrid server-first: server rendering with client components or islands; transitional apps mix both (L252, L255).
- P4 Decide per page: mostly HTML with minimal JavaScript as a legitimate default; measure before choosing (L281).

Evidence on copies, forbidden tiers and limits: client JavaScript budget, SPA costs, LCP needs server-visible content (L016, L254, L297).
Forces in tension: latency and changeability against correctness (one source of logic). Context that moves it: UI interdependence, offline use, update frequency, non-browser consumers, crawlability (L286).
Realized or refined by: INTERACTION.VISUALIZE (realizes), PIG-WEB.ALLOCATION.JS_SERVER (refines).

#### ALLOCATION.PRESENT.2 Formatting and Localization

Decides: Which tier formats values for a reader and in which form values are stored. Owns: L632.

Positions in the evidence:
- P1 At the edge nearest the reader: the browser runtime formats dates, numbers and plurals; the server formats what it renders (HTML, email, PDF); storage stays canonical (L632).
- P2 Database collation: matters only for sort and index behaviour (inferred, open) (L632).

Evidence on copies, forbidden tiers and limits: none further; internationalization is deferred (L632).
Forces in tension: correctness of stored data against user experience. Context that moves it: which tier renders the text.
Realized or refined by: INTERACTION.VISUALIZE (realizes), PIG-WEB.INTERACTION.ENVIRONMENT.3 (requires).

#### ALLOCATION.PRESENT.3 UI and Ephemeral State

Decides: Where each kind of interaction state lives: view, form, URL, server copy, presence. Owns: L070, L071, L631, L681.

Positions in the evidence:
- P1 By lifetime and sharing: ephemeral view state in the browser, durable or shared state on the server, shareable view state in the URL (L631, L070, L292).
- P2 Server state in the browser is a cache: a stale-able copy of data owned elsewhere (L071, L291).
- P3 Presence is ephemeral: broadcast with a timeout and never written to database tables (L681).
- P4 Local-first: durable state moves to the client (L302).

Evidence on copies, forbidden tiers and limits: four kinds of client state, each with an explicit owner (L070).
Forces in tension: latency against correctness. Context that moves it: offline use, sharing between users or tabs.
Realized or refined by: INTERACTION.COLLABORATE (realizes), PIG-WEB.INTERACTION.VISUALIZE.2 (realizes).

## Tree: `pig-web-defaults`

```text
PIG-WEB.ROOT  Web Defaults  (-)
    PIG-WEB.ALLOCATION  Stack Allocation  (-)
        PIG-WEB.ALLOCATION.POSTGRES_FIRST  Postgres First for Backing Roles  (L125, L127)
        PIG-WEB.ALLOCATION.DB_API  Database Function API  (L187, L515, L518, L617, L618)
        PIG-WEB.ALLOCATION.TYPE_CHAIN  Type Definition Chain  (L272, L548, L549)
        PIG-WEB.ALLOCATION.ROW_SECURITY  Row Security Placement  (L619, L688)
        PIG-WEB.ALLOCATION.JOB_HOST  Job and Schedule Host  (L126, L604)
        PIG-WEB.ALLOCATION.CACHE_STORE  Cache Store  (L417)
        PIG-WEB.ALLOCATION.JS_SERVER  JavaScript Server Tier  (L288)
    PIG-WEB.DATA  Postgres Data Tier  (-)
        PIG-WEB.DATA.ORGANIZE  Schema Organization  (-)
            PIG-WEB.DATA.ORGANIZE.1  Tables and Normalization  (L169, L489)
            PIG-WEB.DATA.ORGANIZE.2  Keys  (L170, L179, L499-L504)
            PIG-WEB.DATA.ORGANIZE.3  Column Types  (L177, L178, L497, L498)
            PIG-WEB.DATA.ORGANIZE.4  Naming  (L505-L507)
            PIG-WEB.DATA.ORGANIZE.5  JSON Documents  (L508-L512)
            PIG-WEB.DATA.ORGANIZE.6  Schemas and Tenancy  (L128, L180, L513)
            PIG-WEB.DATA.ORGANIZE.7  Indexes  (L173, L490)
        PIG-WEB.DATA.GUARD  Declared Integrity  (-)
            PIG-WEB.DATA.GUARD.1  Constraints  (L171, L172, L174, L175, L491-L496)
            PIG-WEB.DATA.GUARD.2  Roles and Privileges  (L181-L186, L514)
            PIG-WEB.DATA.GUARD.3  Row Security Policies  (L309-L311, L566)
            PIG-WEB.DATA.GUARD.4  Triggers  (L216, L217, L529)
        PIG-WEB.DATA.CONCURRENCY  Concurrency Mechanics  (-)
            PIG-WEB.DATA.CONCURRENCY.1  Default Concurrency Strategy  (L568-L570)
            PIG-WEB.DATA.CONCURRENCY.2  Isolation Mechanics  (L571-L577, L676)
            PIG-WEB.DATA.CONCURRENCY.3  Locks  (L578-L581)
            PIG-WEB.DATA.CONCURRENCY.4  Atomic Statements  (L585-L588)
            PIG-WEB.DATA.CONCURRENCY.5  Sequences and Commit Order  (L591-L595)
            PIG-WEB.DATA.CONCURRENCY.6  State Transition Order  (L597, L598)
        PIG-WEB.DATA.MAINTAIN  Data Maintenance  (-)
            PIG-WEB.DATA.MAINTAIN.1  Migrations  (L189-L198, L519)
            PIG-WEB.DATA.MAINTAIN.2  Deletion, Retention and Partitioning  (L204-L207, L520-L525)
            PIG-WEB.DATA.MAINTAIN.3  History Tables  (L208-L213, L685)
            PIG-WEB.DATA.MAINTAIN.4  Bulk Data Jobs  (L540-L545)
            PIG-WEB.DATA.MAINTAIN.5  Backup and Recovery  (L218-L223)
            PIG-WEB.DATA.MAINTAIN.6  Personal Data Erasure  [deferred]  (L526)
            PIG-WEB.DATA.MAINTAIN.7  High Availability and Replication  [deferred]  (-)
        PIG-WEB.DATA.DERIVE  Derived Data in Postgres  (-)
            PIG-WEB.DATA.DERIVE.1  Denormalization and Sync  (L168, L176, L531-L533)
            PIG-WEB.DATA.DERIVE.2  Cache Tables  (L420, L535-L539)
            PIG-WEB.DATA.DERIVE.3  Search  [deferred]  (-)
        PIG-WEB.DATA.INTERFACE  Database Interface  (-)
            PIG-WEB.DATA.INTERFACE.1  Functions and Views  (L188, L516, L517, L530)
            PIG-WEB.DATA.INTERFACE.2  Connections and Pooling  (L199-L203)
    PIG-WEB.LOGIC  Python Application Tier  (-)
        PIG-WEB.LOGIC.SECURE  Backend Security  (-)
            PIG-WEB.LOGIC.SECURE.1  Access Control Enforcement  (L305-L308)
            PIG-WEB.LOGIC.SECURE.2  Sessions  (L317, L322-L329)
            PIG-WEB.LOGIC.SECURE.3  CSRF Defense  (L330-L333)
            PIG-WEB.LOGIC.SECURE.4  Federated Login and Tokens  (L312, L338-L343)
            PIG-WEB.LOGIC.SECURE.5  Passwords and Login Throttling  (L344-L349)
            PIG-WEB.LOGIC.SECURE.6  Abuse and Rate Limits  (L358-L368)
            PIG-WEB.LOGIC.SECURE.7  Server-Side Fetch  (L662)
        PIG-WEB.LOGIC.ENFORCE  Business Logic Realization  (-)
            PIG-WEB.LOGIC.ENFORCE.1  Use-Case Layer  (L224-L227)
            PIG-WEB.LOGIC.ENFORCE.2  Transactions  (L228-L232)
            PIG-WEB.LOGIC.ENFORCE.3  Data Access  (L235-L237, L614)
            PIG-WEB.LOGIC.ENFORCE.4  Concurrency Model  (L238-L241)
            PIG-WEB.LOGIC.ENFORCE.5  Framework Choice  (L242)
        PIG-WEB.LOGIC.PROCESS  Processing and Side Effects  (-)
            PIG-WEB.LOGIC.PROCESS.1  Background and Scheduled Jobs  (L407, L408, L411-L413, L605)
            PIG-WEB.LOGIC.PROCESS.2  Side Effects and Delivery  (L233, L234, L270, L409, L410, L589, L590, L599, L600)
            PIG-WEB.LOGIC.PROCESS.3  Resilience  (L243-L246)
            PIG-WEB.LOGIC.PROCESS.4  File Upload Path  (L421-L427)
            PIG-WEB.LOGIC.PROCESS.5  File Scanning and Storage  (L428-L431)
            PIG-WEB.LOGIC.PROCESS.6  File Serving  (L432-L434)
            PIG-WEB.LOGIC.PROCESS.7  Email and Push Delivery  [deferred]  (-)
        PIG-WEB.LOGIC.EXPOSE  HTTP Interface  (-)
            PIG-WEB.LOGIC.EXPOSE.1  Contract Style and Resources  (L256, L257, L264-L268)
            PIG-WEB.LOGIC.EXPOSE.2  Status Codes and Errors  (L259, L261-L263)
            PIG-WEB.LOGIC.EXPOSE.3  Retries and Asynchronous Operations  (L269, L271, L546, L602, L603, L655)
            PIG-WEB.LOGIC.EXPOSE.4  Response Caching  (L414-L416, L418, L419)
            PIG-WEB.LOGIC.EXPOSE.5  Origin and CORS  (L279, L280)
            PIG-WEB.LOGIC.EXPOSE.6  Payload Schemas  (L550-L558)
            PIG-WEB.LOGIC.EXPOSE.7  API Evolution  (L273-L278, L547)
    PIG-WEB.INTERACTION  Browser and Agent Surface  (-)
        PIG-WEB.INTERACTION.VISUALIZE  Browser Rendering  (-)
            PIG-WEB.INTERACTION.VISUALIZE.1  Rendering Technique  (L282-L286, L289, L290)
            PIG-WEB.INTERACTION.VISUALIZE.2  Client State  (L291, L292)
            PIG-WEB.INTERACTION.VISUALIZE.3  Page Performance  (L297-L299)
            PIG-WEB.INTERACTION.VISUALIZE.4  Accessibility  (L300, L301)
        PIG-WEB.INTERACTION.EDIT  Editing Without Loss  (L258, L260, L583, L675)
        PIG-WEB.INTERACTION.REALTIME  Real-Time Channels  (-)
            PIG-WEB.INTERACTION.REALTIME.1  Channel Choice  (L436-L442)
            PIG-WEB.INTERACTION.REALTIME.2  Channel Operation  (L443-L454)
            PIG-WEB.INTERACTION.REALTIME.3  Long-Lived Connection Servers  (L455-L458)
            PIG-WEB.INTERACTION.REALTIME.4  Channel Security  (L459-L461)
            PIG-WEB.INTERACTION.REALTIME.5  Database Notifications  (L462-L467)
        PIG-WEB.INTERACTION.COLLABORATE  Comments and Collaboration  (-)
            PIG-WEB.INTERACTION.COLLABORATE.1  Comment Anchoring  (L665-L668)
            PIG-WEB.INTERACTION.COLLABORATE.2  Threads and Comment Lifecycle  (L669-L673)
            PIG-WEB.INTERACTION.COLLABORATE.3  Collaborative Text Editing  (L677, L679, L680)
            PIG-WEB.INTERACTION.COLLABORATE.4  Notifications and Moderation  (L683, L689)
        PIG-WEB.INTERACTION.AGENT  Agent Surface  (-)
            PIG-WEB.INTERACTION.AGENT.1  Surface and Protocol  (L634-L636, L661, L663)
            PIG-WEB.INTERACTION.AGENT.2  Discovery and Registration  (L637, L653, L654)
            PIG-WEB.INTERACTION.AGENT.3  Identity and Delegation  (L638, L639, L641, L643, L659, L660)
            PIG-WEB.INTERACTION.AGENT.4  Approval and Injection Defense  (L646, L647, L649, L650)
            PIG-WEB.INTERACTION.AGENT.5  Agent-Shaped Responses and Limits  (L651, L656, L657)
        PIG-WEB.INTERACTION.ENVIRONMENT  Browser Environment  (-)
            PIG-WEB.INTERACTION.ENVIRONMENT.1  Capability and Page Lifecycle  (L287, L293, L294)
            PIG-WEB.INTERACTION.ENVIRONMENT.2  Offline and Installable Apps  [deferred]  (-)
            PIG-WEB.INTERACTION.ENVIRONMENT.3  Internationalization  [deferred]  (-)
    PIG-WEB.TRANSVERSE  Transverse Defaults  (-)
        PIG-WEB.TRANSVERSE.SECURITY  Security Defaults  (-)
            PIG-WEB.TRANSVERSE.SECURITY.1  Security Requirement Catalogue  (L304)
            PIG-WEB.TRANSVERSE.SECURITY.2  Transport Security  (L141-L148)
            PIG-WEB.TRANSVERSE.SECURITY.3  Security Headers and CSP  (L334-L337)
            PIG-WEB.TRANSVERSE.SECURITY.4  Secrets  (L350-L353)
            PIG-WEB.TRANSVERSE.SECURITY.5  Supply Chain  (L354-L357)
        PIG-WEB.TRANSVERSE.PERFORMANCE  Page Experience Targets  (L295, L296)
        PIG-WEB.TRANSVERSE.CONTRACTS  Contract Verification and Meaning  (-)
            PIG-WEB.TRANSVERSE.CONTRACTS.1  Contract Verification  (L401, L402, L559-L561)
            PIG-WEB.TRANSVERSE.CONTRACTS.2  Contract Meaning and Ownership  (L562-L565)
        PIG-WEB.TRANSVERSE.OPERABILITY  Operations  (-)
            PIG-WEB.TRANSVERSE.OPERABILITY.1  Tracing and Logs  (L369-L376)
            PIG-WEB.TRANSVERSE.OPERABILITY.2  Client Telemetry  (L377-L382)
            PIG-WEB.TRANSVERSE.OPERABILITY.3  Monitoring  (L383-L389)
            PIG-WEB.TRANSVERSE.OPERABILITY.4  Security Event Log  (L390-L395)
            PIG-WEB.TRANSVERSE.OPERABILITY.5  Testing  (L396-L400, L567)
            PIG-WEB.TRANSVERSE.OPERABILITY.6  Delivery and Configuration  (L247-L251, L403-L405)
            PIG-WEB.TRANSVERSE.OPERABILITY.7  Incident Response  [deferred]  (-)
        PIG-WEB.TRANSVERSE.TOPOLOGY  Runtime Topology  (-)
            PIG-WEB.TRANSVERSE.TOPOLOGY.1  Reverse Proxy Edge  (L134-L140)
            PIG-WEB.TRANSVERSE.TOPOLOGY.2  Application Server  (L149-L155)
            PIG-WEB.TRANSVERSE.TOPOLOGY.3  Process Placement  (L156-L160)
            PIG-WEB.TRANSVERSE.TOPOLOGY.4  Static Assets and CDN  (L161-L167)
        PIG-WEB.TRANSVERSE.EVOLUTION  Evolution Defaults  (-)
            PIG-WEB.TRANSVERSE.EVOLUTION.1  Deployables  (L113-L121)
            PIG-WEB.TRANSVERSE.EVOLUTION.2  Modular Monolith  (L122-L124)
            PIG-WEB.TRANSVERSE.EVOLUTION.3  Decision Records  (L129-L133)
```

Nodes: 132 (L0 1, L1 5, L2 29, L3 97).

## Nodes: `pig-web-defaults`

| uid | name | decides | owns |
|---|---|---|---|
| PIG-WEB.ROOT | Web Defaults | The JavaScript, Python and Postgres choices that realize the web-app philosophy, under the same five branches. | - |
| PIG-WEB.ALLOCATION | Stack Allocation | Which component of this stack (Postgres, the Python backend, browser JavaScript, auxiliary services) carries a placement where the stack offers competing mechanisms. | - |
| PIG-WEB.ALLOCATION.POSTGRES_FIRST | Postgres First for Backing Roles | Whether Postgres also carries the queue, cache, schedule, notification and search roles until a measured limit, or specialised services take them. | L125, L127 |
| PIG-WEB.ALLOCATION.DB_API | Database Function API | Whether consumers reach Postgres through a function API, a schema exposed as the API, or an ORM over base tables. | L187, L515, L518, L617, L618 |
| PIG-WEB.ALLOCATION.TYPE_CHAIN | Type Definition Chain | Where the chain of type definitions starts (Postgres schema, Python models or the OpenAPI description) and how the browser types follow. | L272, L548, L549 |
| PIG-WEB.ALLOCATION.ROW_SECURITY | Row Security Placement | Whether Postgres row-level security enforces visibility on every access path, beside or instead of the Python backend checks. | L619, L688 |
| PIG-WEB.ALLOCATION.JOB_HOST | Job and Schedule Host | Which component holds the job queue and the schedules: Postgres tables and a scheduler extension, or a broker with a worker framework. | L126, L604 |
| PIG-WEB.ALLOCATION.CACHE_STORE | Cache Store | Which component stores application caches shared by processes: Postgres tables or a cache service. | L417 |
| PIG-WEB.ALLOCATION.JS_SERVER | JavaScript Server Tier | Whether browser rendering adds a JavaScript server runtime beside the Python application server. | L288 |
| PIG-WEB.DATA | Postgres Data Tier | How Postgres realizes the database share of each placement. | - |
| PIG-WEB.DATA.ORGANIZE | Schema Organization | How tables, keys, column types, names, JSON documents, namespaces and indexes are laid out in Postgres. | - |
| PIG-WEB.DATA.ORGANIZE.1 | Tables and Normalization | How repeating groups, wide tables and arrays are handled in table design. | L169, L489 |
| PIG-WEB.DATA.ORGANIZE.2 | Keys | Which primary-key shape and type each table gets. | L170, L179, L499-L504 |
| PIG-WEB.DATA.ORGANIZE.3 | Column Types | Which column types are used for time, text, numbers, enumerations and flags. | L177, L178, L497, L498 |
| PIG-WEB.DATA.ORGANIZE.4 | Naming | How identifiers are named so that role and type read from the name. | L505-L507 |
| PIG-WEB.DATA.ORGANIZE.5 | JSON Documents | When JSON documents are stored and how their schemas are held and evolved. | L508-L512 |
| PIG-WEB.DATA.ORGANIZE.6 | Schemas and Tenancy | How schemas group objects and how tenants are isolated. | L128, L180, L513 |
| PIG-WEB.DATA.ORGANIZE.7 | Indexes | Which indexes exist and what justifies each. | L173, L490 |
| PIG-WEB.DATA.GUARD | Declared Integrity | How Postgres declares integrity and access: constraints, roles, row policies and triggers. | - |
| PIG-WEB.DATA.GUARD.1 | Constraints | Which rules are declared as keys, NOT NULL, CHECK, foreign keys, unique and exclusion constraints and domains. | L171, L172, L174, L175, L491-L496 |
| PIG-WEB.DATA.GUARD.2 | Roles and Privileges | How database roles, grants and authentication separate owners, runtime users and humans. | L181-L186, L514 |
| PIG-WEB.DATA.GUARD.3 | Row Security Policies | How row-level security policies and the request context they read behave and are set. | L309-L311, L566 |
| PIG-WEB.DATA.GUARD.4 | Triggers | Which work triggers may do and which stays with the writing code. | L216, L217, L529 |
| PIG-WEB.DATA.CONCURRENCY | Concurrency Mechanics | How Postgres isolation, locks, atomic statements and sequences keep concurrent change correct. | - |
| PIG-WEB.DATA.CONCURRENCY.1 | Default Concurrency Strategy | Which concurrency-control strategy is the default for transactions and for user-edited rows. | L568-L570 |
| PIG-WEB.DATA.CONCURRENCY.2 | Isolation Mechanics | How isolation levels behave, what they cost and how failed transactions are retried. | L571-L577, L676 |
| PIG-WEB.DATA.CONCURRENCY.3 | Locks | How row and advisory locks are taken, ordered and released. | L578-L581 |
| PIG-WEB.DATA.CONCURRENCY.4 | Atomic Statements | Which changes are expressed as single idempotent statements. | L585-L588 |
| PIG-WEB.DATA.CONCURRENCY.5 | Sequences and Commit Order | What sequences guarantee and how readers follow rows in commit order. | L591-L595 |
| PIG-WEB.DATA.CONCURRENCY.6 | State Transition Order | In which order facts and state labels are written, and how transition checks are introduced. | L597, L598 |
| PIG-WEB.DATA.MAINTAIN | Data Maintenance | How Postgres schema and data are changed, retired, recorded and recovered over time. | - |
| PIG-WEB.DATA.MAINTAIN.1 | Migrations | How schema changes are written and run against live tables. | L189-L198, L519 |
| PIG-WEB.DATA.MAINTAIN.2 | Deletion, Retention and Partitioning | How rows are deleted, archived or expired per table. | L204-L207, L520-L525 |
| PIG-WEB.DATA.MAINTAIN.3 | History Tables | How row history and audit records are written and queried in Postgres. | L208-L213, L685 |
| PIG-WEB.DATA.MAINTAIN.4 | Bulk Data Jobs | How large data changes are batched, run, observed and recovered. | L540-L545 |
| PIG-WEB.DATA.MAINTAIN.5 | Backup and Recovery | How the database is backed up and proven restorable. | L218-L223 |
| PIG-WEB.DATA.MAINTAIN.6 | Personal Data Erasure [deferred] | How personal data is erased or anonymized on request (scope out, recorded only). | L526 |
| PIG-WEB.DATA.MAINTAIN.7 | High Availability and Replication [deferred] | How the database survives the loss of its primary (scope out, recorded only). | - |
| PIG-WEB.DATA.DERIVE | Derived Data in Postgres | How Postgres holds derived values and caches and keeps them in sync with their sources. | - |
| PIG-WEB.DATA.DERIVE.1 | Denormalization and Sync | When data is denormalized and which sync mechanism and drift check each copy gets. | L168, L176, L531-L533 |
| PIG-WEB.DATA.DERIVE.2 | Cache Tables | How cache tables are classified, invalidated, named and refreshed. | L420, L535-L539 |
| PIG-WEB.DATA.DERIVE.3 | Search [deferred] | How full-text and faceted search is provided (scope out, recorded only). | - |
| PIG-WEB.DATA.INTERFACE | Database Interface | How the database offers itself to its consumers: functions, views and connections. | - |
| PIG-WEB.DATA.INTERFACE.1 | Functions and Views | How database functions and views are written, named, secured and evolved. | L188, L516, L517, L530 |
| PIG-WEB.DATA.INTERFACE.2 | Connections and Pooling | How consumers connect, how connections are pooled and how sessions are bounded. | L199-L203 |
| PIG-WEB.LOGIC | Python Application Tier | How the Python backend realizes the backend share of each placement. | - |
| PIG-WEB.LOGIC.SECURE | Backend Security | How the Python backend authenticates, keeps sessions, defends against forgery and abuse, and checks access. | - |
| PIG-WEB.LOGIC.SECURE.1 | Access Control Enforcement | How the backend implements and tests its access checks. | L305-L308 |
| PIG-WEB.LOGIC.SECURE.2 | Sessions | How the backend creates, protects, renews and ends sessions. | L317, L322-L329 |
| PIG-WEB.LOGIC.SECURE.3 | CSRF Defense | How cross-site request forgery is prevented. | L330-L333 |
| PIG-WEB.LOGIC.SECURE.4 | Federated Login and Tokens | How login is delegated to identity providers and how tokens are verified. | L312, L338-L343 |
| PIG-WEB.LOGIC.SECURE.5 | Passwords and Login Throttling | How own credentials are stored and login abuse is slowed. | L344-L349 |
| PIG-WEB.LOGIC.SECURE.6 | Abuse and Rate Limits | Where and how request limits are applied and signalled. | L358-L368 |
| PIG-WEB.LOGIC.SECURE.7 | Server-Side Fetch | How the server fetches URLs named by clients without reaching internal addresses. | L662 |
| PIG-WEB.LOGIC.ENFORCE | Business Logic Realization | How the Python backend structures use cases, transactions, data access and concurrency. | - |
| PIG-WEB.LOGIC.ENFORCE.1 | Use-Case Layer | How operations are defined once and called by every entry point. | L224-L227 |
| PIG-WEB.LOGIC.ENFORCE.2 | Transactions | How the backend scopes, commits and rolls back database transactions. | L228-L232 |
| PIG-WEB.LOGIC.ENFORCE.3 | Data Access | How the backend reaches the database: ORM, raw SQL and round trips. | L235-L237, L614 |
| PIG-WEB.LOGIC.ENFORCE.4 | Concurrency Model | Whether handlers are synchronous or asynchronous and what each constrains. | L238-L241 |
| PIG-WEB.LOGIC.ENFORCE.5 | Framework Choice | Which Python web framework the backend uses and on which criteria. | L242 |
| PIG-WEB.LOGIC.PROCESS | Processing and Side Effects | How the Python backend runs background work, delivers side effects, survives faults and handles files. | - |
| PIG-WEB.LOGIC.PROCESS.1 | Background and Scheduled Jobs | How background and scheduled jobs are queued, written and run. | L407, L408, L411-L413, L605 |
| PIG-WEB.LOGIC.PROCESS.2 | Side Effects and Delivery | How effects outside the transaction are staged, delivered and made idempotent. | L233, L234, L270, L409, L410, L589, L590, L599, L600 |
| PIG-WEB.LOGIC.PROCESS.3 | Resilience | How calls to other services retry, time out and break. | L243-L246 |
| PIG-WEB.LOGIC.PROCESS.4 | File Upload Path | Which path upload bytes take and which limits apply on it. | L421-L427 |
| PIG-WEB.LOGIC.PROCESS.5 | File Scanning and Storage | How uploaded files are scanned, tracked and stored. | L428-L431 |
| PIG-WEB.LOGIC.PROCESS.6 | File Serving | How stored files are served back safely. | L432-L434 |
| PIG-WEB.LOGIC.PROCESS.7 | Email and Push Delivery [deferred] | How email and push notifications are delivered (scope out, recorded only). | - |
| PIG-WEB.LOGIC.EXPOSE | HTTP Interface | How the Python backend shapes its HTTP interface: style, errors, retries, caching, origin, payloads and evolution. | - |
| PIG-WEB.LOGIC.EXPOSE.1 | Contract Style and Resources | Which contract style the API follows and how resources and collections are designed. | L256, L257, L264-L268 |
| PIG-WEB.LOGIC.EXPOSE.2 | Status Codes and Errors | Which status codes and error format the API returns. | L259, L261-L263 |
| PIG-WEB.LOGIC.EXPOSE.3 | Retries and Asynchronous Operations | How repeatable creates and long operations are expressed in the API. | L269, L271, L546, L602, L603, L655 |
| PIG-WEB.LOGIC.EXPOSE.4 | Response Caching | How responses and application caches declare and bound their reuse. | L414-L416, L418, L419 |
| PIG-WEB.LOGIC.EXPOSE.5 | Origin and CORS | From which origins pages, API and assets are served and who may read them. | L279, L280 |
| PIG-WEB.LOGIC.EXPOSE.6 | Payload Schemas | How request and response payloads are typed, validated and published. | L550-L558 |
| PIG-WEB.LOGIC.EXPOSE.7 | API Evolution | How the API changes, deprecates and versions without breaking clients. | L273-L278, L547 |
| PIG-WEB.INTERACTION | Browser and Agent Surface | How browser JavaScript and the agent surface realize the interaction share of each placement. | - |
| PIG-WEB.INTERACTION.VISUALIZE | Browser Rendering | How pages are rendered, hold client state, perform and stay accessible in the browser. | - |
| PIG-WEB.INTERACTION.VISUALIZE.1 | Rendering Technique | Which rendering technique each kind of page uses and what JavaScript it ships. | L282-L286, L289, L290 |
| PIG-WEB.INTERACTION.VISUALIZE.2 | Client State | Where server data and navigable view state are held in the browser. | L291, L292 |
| PIG-WEB.INTERACTION.VISUALIZE.3 | Page Performance | Which page techniques keep loading, interaction and layout fast and stable. | L297-L299 |
| PIG-WEB.INTERACTION.VISUALIZE.4 | Accessibility | Which accessibility level is required and how controls meet it. | L300, L301 |
| PIG-WEB.INTERACTION.EDIT | Editing Without Loss | How forms submit, and how concurrent and repeated edits are detected and shown. | L258, L260, L583, L675 |
| PIG-WEB.INTERACTION.REALTIME | Real-Time Channels | How the server pushes changes to the browser. | - |
| PIG-WEB.INTERACTION.REALTIME.1 | Channel Choice | Which channel (polling, long polling, SSE, WebSocket) each push need uses. | L436-L442 |
| PIG-WEB.INTERACTION.REALTIME.2 | Channel Operation | How channels resume, stay alive through intermediaries and reconnect. | L443-L454 |
| PIG-WEB.INTERACTION.REALTIME.3 | Long-Lived Connection Servers | Which server processes hold long-lived connections and how they fan out. | L455-L458 |
| PIG-WEB.INTERACTION.REALTIME.4 | Channel Security | How long-lived connections are authenticated, authorized and bounded. | L459-L461 |
| PIG-WEB.INTERACTION.REALTIME.5 | Database Notifications | How Postgres notifications wake application processes. | L462-L467 |
| PIG-WEB.INTERACTION.COLLABORATE | Comments and Collaboration | How comments, threads, shared text editing, notifications and moderation are realized. | - |
| PIG-WEB.INTERACTION.COLLABORATE.1 | Comment Anchoring | To what a comment is anchored and how anchors survive edits. | L665-L668 |
| PIG-WEB.INTERACTION.COLLABORATE.2 | Threads and Comment Lifecycle | How threads are stored and resolved and how comments are edited and deleted. | L669-L673 |
| PIG-WEB.INTERACTION.COLLABORATE.3 | Collaborative Text Editing | Which engine merges concurrent edits of long text, and for which fields. | L677, L679, L680 |
| PIG-WEB.INTERACTION.COLLABORATE.4 | Notifications and Moderation | How collaboration notifications are created and how comments are moderated. | L683, L689 |
| PIG-WEB.INTERACTION.AGENT | Agent Surface | How agents reach, identify themselves to, act through and are limited by the application. | - |
| PIG-WEB.INTERACTION.AGENT.1 | Surface and Protocol | Which protocol surface and content forms agents get, and how the surface keeps state. | L634-L636, L661, L663 |
| PIG-WEB.INTERACTION.AGENT.2 | Discovery and Registration | How agent clients discover the authorization server and register. | L637, L653, L654 |
| PIG-WEB.INTERACTION.AGENT.3 | Identity and Delegation | How an agent identity, its delegating user and its credentials are represented and recorded. | L638, L639, L641, L643, L659, L660 |
| PIG-WEB.INTERACTION.AGENT.4 | Approval and Injection Defense | How consequential agent actions are approved and how prompt injection is contained. | L646, L647, L649, L650 |
| PIG-WEB.INTERACTION.AGENT.5 | Agent-Shaped Responses and Limits | How responses, errors and rate-limit partitions are shaped for agent callers. | L651, L656, L657 |
| PIG-WEB.INTERACTION.ENVIRONMENT | Browser Environment | How browser capability, page lifecycle, offline use and locale are handled. | - |
| PIG-WEB.INTERACTION.ENVIRONMENT.1 | Capability and Page Lifecycle | How pages detect features and survive back-forward restore, freezing and discard. | L287, L293, L294 |
| PIG-WEB.INTERACTION.ENVIRONMENT.2 | Offline and Installable Apps [deferred] | How the application works offline or installed (scope out, recorded only). | - |
| PIG-WEB.INTERACTION.ENVIRONMENT.3 | Internationalization [deferred] | How the interface is translated and adapted to locales (scope out, recorded only). | - |
| PIG-WEB.TRANSVERSE | Transverse Defaults | Which stack choices span every tier: security, performance targets, contract verification, operations, runtime topology and evolution. | - |
| PIG-WEB.TRANSVERSE.SECURITY | Security Defaults | Which security catalogue, transport, headers, secrets and supply-chain practices the stack adopts. | - |
| PIG-WEB.TRANSVERSE.SECURITY.1 | Security Requirement Catalogue | Which catalogue of verifiable security requirements the project cites. | L304 |
| PIG-WEB.TRANSVERSE.SECURITY.2 | Transport Security | Where TLS terminates and how HTTPS is enforced. | L141-L148 |
| PIG-WEB.TRANSVERSE.SECURITY.3 | Security Headers and CSP | Which response headers and content security policy pages carry. | L334-L337 |
| PIG-WEB.TRANSVERSE.SECURITY.4 | Secrets | Where secrets live at runtime and how they are managed. | L350-L353 |
| PIG-WEB.TRANSVERSE.SECURITY.5 | Supply Chain | How dependencies and builds are pinned, scanned and proven. | L354-L357 |
| PIG-WEB.TRANSVERSE.PERFORMANCE | Page Experience Targets | Which performance targets and budgets pages are held to. | L295, L296 |
| PIG-WEB.TRANSVERSE.CONTRACTS | Contract Verification and Meaning | How contracts between tiers are verified and how their meaning and ownership are recorded. | - |
| PIG-WEB.TRANSVERSE.CONTRACTS.1 | Contract Verification | Which contract tests verify the seams between components. | L401, L402, L559-L561 |
| PIG-WEB.TRANSVERSE.CONTRACTS.2 | Contract Meaning and Ownership | How units, semantics, owner, version and lifecycle of a contract are recorded. | L562-L565 |
| PIG-WEB.TRANSVERSE.OPERABILITY | Operations | How the stack is traced, monitored, logged, tested, configured and delivered. | - |
| PIG-WEB.TRANSVERSE.OPERABILITY.1 | Tracing and Logs | How traces are propagated and sampled and how logs are written and correlated. | L369-L376 |
| PIG-WEB.TRANSVERSE.OPERABILITY.2 | Client Telemetry | How errors and real-user measurements are collected from the browser. | L377-L382 |
| PIG-WEB.TRANSVERSE.OPERABILITY.3 | Monitoring | Which signals are monitored and what pages a human. | L383-L389 |
| PIG-WEB.TRANSVERSE.OPERABILITY.4 | Security Event Log | What the security event log records and how it is protected. | L390-L395 |
| PIG-WEB.TRANSVERSE.OPERABILITY.5 | Testing | How tests are placed, isolated and run against real databases. | L396-L400, L567 |
| PIG-WEB.TRANSVERSE.OPERABILITY.6 | Delivery and Configuration | How the pipeline is staged, releases decoupled from deploys, one-time steps run and configuration loaded. | L247-L251, L403-L405 |
| PIG-WEB.TRANSVERSE.OPERABILITY.7 | Incident Response [deferred] | How incidents are detected, handled and reviewed (scope out, recorded only). | - |
| PIG-WEB.TRANSVERSE.TOPOLOGY | Runtime Topology | How proxy, application server, worker processes and static assets are deployed. | - |
| PIG-WEB.TRANSVERSE.TOPOLOGY.1 | Reverse Proxy Edge | What the reverse proxy in front of the application does. | L134-L140 |
| PIG-WEB.TRANSVERSE.TOPOLOGY.2 | Application Server | Which Python application server and worker model run the backend. | L149-L155 |
| PIG-WEB.TRANSVERSE.TOPOLOGY.3 | Process Placement | How images are built and where web and worker processes are replicated. | L156-L160 |
| PIG-WEB.TRANSVERSE.TOPOLOGY.4 | Static Assets and CDN | Where static assets are built and served and when a CDN is added. | L161-L167 |
| PIG-WEB.TRANSVERSE.EVOLUTION | Evolution Defaults | How many deployables the system starts with, how its modules are bounded and how decisions are recorded. | - |
| PIG-WEB.TRANSVERSE.EVOLUTION.1 | Deployables | How many separately deployed units the system has and when that changes. | L113-L121 |
| PIG-WEB.TRANSVERSE.EVOLUTION.2 | Modular Monolith | How modules inside one deployable are cut and their boundaries enforced. | L122-L124 |
| PIG-WEB.TRANSVERSE.EVOLUTION.3 | Decision Records | How architecture decisions are written, stored and superseded. | L129-L133 |

## Placement records: `pig-web-defaults`

#### PIG-WEB.ALLOCATION.POSTGRES_FIRST Postgres First for Backing Roles

Decides: Whether Postgres also carries the queue, cache, schedule, notification and search roles until a measured limit, or specialised services take them. Owns: L125, L127.

Positions in the evidence:
- P1 One Postgres until a measured limit: queue, cache, scheduling, documents and search stay in Postgres until its limits are reached (L125, L534, L604).
- P2 Specialised services: a broker, a cache service or a channel layer from the start or past the limit (L126, L417, L457).

Evidence on copies, forbidden tiers and limits: the NOTIFY commit lock under write concurrency, queue tables degrading under load; the database is the hardest tier to scale (L127, L126, L615).
Forces in tension: changeability (fewer components) against scalability. Context that moves it: write concurrency, queue volume, number of processes that fan out.
Realized or refined by: PIG-WEB.INTERACTION.REALTIME.5 (requires).

#### PIG-WEB.ALLOCATION.DB_API Database Function API

Decides: Whether consumers reach Postgres through a function API, a schema exposed as the API, or an ORM over base tables. Owns: L187, L515, L518, L617, L618.

Positions in the evidence:
- P1 Function API (backend of backends): consumers call Postgres functions; the signature is the contract; additive evolution (L515, L617).
- P2 Schema as the API: a dedicated schema of views and functions served as the API (PostgREST) (L518, L618, L187).
- P3 ORM over base tables: application code queries base tables through the ORM; views kept off the contract path (L187, L516).

Evidence on copies, forbidden tiers and limits: the function API conflicts with application-owned databases; database logic needs a live database to test (L044, L042).
Forces in tension: changeability against correctness for several consumers. Context that moves it: number of backends, their languages, team SQL skill.
Realized or refined by: PIG-WEB.DATA.INTERFACE.1 (realizes).

#### PIG-WEB.ALLOCATION.TYPE_CHAIN Type Definition Chain

Decides: Where the chain of type definitions starts (Postgres schema, Python models or the OpenAPI description) and how the browser types follow. Owns: L272, L548, L549.

Positions in the evidence:
- P1 Postgres schema first: one class for table and validation for simple CRUD (L549).
- P2 Pydantic models first: the OpenAPI description is generated and committed as a build artifact (L548).
- P3 OpenAPI first: the description is designed before code and checked in CI (L272).

Evidence on copies, forbidden tiers and limits: TypeScript types generated from OpenAPI are runtime-free; separate input and output models filter what leaves the server (L555, L553).
Forces in tension: correctness against changeability. Context that moves it: one team owning both ends, independent consumers, API shape differing from storage shape.
Realized or refined by: PIG-WEB.DATA.ORGANIZE (realizes), PIG-WEB.LOGIC.EXPOSE.6 (realizes).

#### PIG-WEB.ALLOCATION.ROW_SECURITY Row Security Placement

Decides: Whether Postgres row-level security enforces visibility on every access path, beside or instead of the Python backend checks. Owns: L619, L688.

Positions in the evidence:
- P1 Row security on every path: roles and row-level security make Postgres decide visibility for any client (L619).
- P2 Row security only with several consumers: RLS when more than one application or agent reads the database; backend checks alone with one tier (L688).
- P3 Row security as second line: application checks are kept and denial is tested through the deployed role (L128).

Evidence on copies, forbidden tiers and limits: owners and BYPASSRLS skip policies, foreign-key checks bypass them, context is passed transaction-locally (L310, L311, L566).
Forces in tension: security against changeability and testability of policy. Context that moves it: direct database access by agents, consoles or other backends.
Realized or refined by: PIG-WEB.DATA.GUARD.3 (realizes), PIG-WEB.LOGIC.SECURE.1 (realizes).

#### PIG-WEB.ALLOCATION.JOB_HOST Job and Schedule Host

Decides: Which component holds the job queue and the schedules: Postgres tables and a scheduler extension, or a broker with a worker framework. Owns: L126, L604.

Positions in the evidence:
- P1 Queue table in Postgres: jobs claimed with FOR UPDATE SKIP LOCKED (L126, L413).
- P2 Staged in Postgres, drained to a broker: the job is written with the data change and relayed (L126, L409).
- P3 Broker from the start: a worker framework with Redis or RabbitMQ (L126, L408).
- P4 Schedules inside Postgres: a scheduler extension calls named functions; the doctrine also names an external poller and a queue-driven worker (L604).

Evidence on copies, forbidden tiers and limits: job tasks are short, idempotent and monitored whatever the host (L605, L410).
Forces in tension: changeability (one component fewer) against scalability. Context that moves it: job volume, lock contention, multi-server fan-out.
Realized or refined by: PIG-WEB.LOGIC.PROCESS.1 (realizes).

#### PIG-WEB.ALLOCATION.CACHE_STORE Cache Store

Decides: Which component stores application caches shared by processes: Postgres tables or a cache service. Owns: L417.

Positions in the evidence:
- P1 Shared cache service: Redis or Memcached across processes (L417).
- P2 Postgres cache tables: transactional invalidation; UNLOGGED tables for rebuildable data (L534, L420).

Evidence on copies, forbidden tiers and limits: per-process memory in multi-process production (L417).
Forces in tension: latency against correctness (atomic invalidation) and changeability. Context that moves it: number of processes, need for atomic invalidation, cache volume.
Realized or refined by: PIG-WEB.DATA.DERIVE.2 (realizes), PIG-WEB.LOGIC.EXPOSE.4 (realizes).

#### PIG-WEB.ALLOCATION.JS_SERVER JavaScript Server Tier

Decides: Whether browser rendering adds a JavaScript server runtime beside the Python application server. Owns: L288.

Positions in the evidence:
- P1 Request-time JavaScript server: an SSR meta-framework runs a JavaScript server beside the Python application server (L288, L290).
- P2 Python renders HTML: hypermedia sources keep logic in the one server language (L288, L252, L629).
- P3 Build-time rendering: static export avoids the extra tier (L288, L285).

Evidence on copies, forbidden tiers and limits: no source weighs the operational cost of the extra tier (open) (L288).
Forces in tension: changeability (one server language) against latency. Context that moves it: SEO and first-load needs, team JavaScript skill, the rendering placement chosen above.
Realized or refined by: PIG-WEB.INTERACTION.VISUALIZE.1 (realizes), PIG-WEB.TRANSVERSE.TOPOLOGY.2 (constrains).

## Intentlinks

Kinds: `realizes` (a tier node carries out the share a placement assigns it), `requires`, `constrains`, `refines`, `dataflow`, `conflicts`. Links from tier nodes point to placements; they do not decide them.

### Tier to placement, intra `web-app-philosophy`

| src | dst | kind | intent |
|---|---|---|---|
| DATA.ORGANIZE | ALLOCATION.RECORD.1 | realizes | holds the durable facts in the form the system-of-record placement gives the database |
| DATA.GUARD | ALLOCATION.GUARD.2 | realizes | enforces the invariants the placement gives the database |
| DATA.GUARD | ALLOCATION.GUARD.5 | realizes | carries the concurrency control the placement gives the database |
| DATA.DERIVE | ALLOCATION.DERIVE.1 | realizes | keeps derived values in the tier and freshness the placement sets |
| DATA.MAINTAIN | ALLOCATION.RECORD.3 | realizes | keeps the database structure as the origin of shapes when the placement makes it the origin |
| LOGIC.SECURE | ALLOCATION.GUARD.1 | realizes | performs the boundary checks the validation placement gives the backend |
| LOGIC.SECURE | ALLOCATION.GUARD.3 | realizes | enforces the access decisions the authorization placement gives the backend |
| LOGIC.SECURE | ALLOCATION.GUARD.4 | realizes | holds sessions and credentials as the identity placement sets |
| LOGIC.ENFORCE | ALLOCATION.ACT.1 | realizes | holds the business rules and transitions the placement gives the backend |
| LOGIC.ENFORCE | ALLOCATION.RULES.4 | requires | one business core serves every client |
| LOGIC.PROCESS | ALLOCATION.GUARD.4 | constrains | stateless processes keep session state in a backing service |
| LOGIC.PROCESS | ALLOCATION.DERIVE.3 | constrains | process memory holds no cache shared beyond one request |
| LOGIC.EXPOSE | ALLOCATION.RECORD.2 | realizes | offers the interface through which consumers reach data when the placement routes them through the backend |
| LOGIC.EXPOSE | ALLOCATION.GUARD.6 | realizes | gives repeated requests safe method semantics |
| INTERACTION.VISUALIZE | ALLOCATION.PRESENT.1 | realizes | renders what the rendering placement gives the browser |
| INTERACTION.VISUALIZE | ALLOCATION.PRESENT.2 | realizes | formats values for the reader where the placement says |
| INTERACTION.COLLABORATE | ALLOCATION.GUARD.5 | realizes | surfaces conflicts with the policy the concurrency placement chose |
| INTERACTION.COLLABORATE | ALLOCATION.PRESENT.3 | realizes | keeps presence and other ephemeral state where the placement says |
| INTERACTION.COLLABORATE | ALLOCATION.GUARD.3 | requires | comment visibility follows the authorization placement |
| INTERACTION.AGENT | ALLOCATION.RULES.4 | requires | the agent surface is one more adapter on the same core |
| INTERACTION.AGENT | ALLOCATION.GUARD.3 | requires | agents never decide access; the authorization authority does |
| INTERACTION.AGENT | ALLOCATION.GUARD.6 | requires | agent retries are absorbed by the duplicate-suppression placement |
| INTERACTION.AGENT | ALLOCATION.ACT.4 | requires | agent actions are recorded where the audit placement writes history |
| INTERACTION.ENVIRONMENT.7 | ALLOCATION.RULES.3 | constrains | script in the page has the application's privileges, so the browser cannot hold deciding checks |
| INTERACTION.ENVIRONMENT.4 | ALLOCATION.DERIVE.3 | constrains | copies in caches the team does not own cannot be recalled |
| INTERACTION.ENVIRONMENT.3 | TRANSVERSE.CONTRACTS | requires | version skew between client and server needs compatible contract evolution |
| TRANSVERSE.SECURITY | ALLOCATION.RULES.3 | refines | cross-tier security properties rest on the trust-boundary rule |
| TRANSVERSE.PERFORMANCE | ALLOCATION.FORCES.3 | dataflow | field measurement supplies the evidence that performance-driven placements need |
| TRANSVERSE.PERFORMANCE | ALLOCATION.FORCES.4 | dataflow | field measurement supplies the latency evidence placements weigh |
| TRANSVERSE.CONTRACTS | ALLOCATION.RECORD.3 | requires | explicit contracts derive from the origin definition the placement names |
| TRANSVERSE.OPERABILITY.1 | ALLOCATION.ACT.4 | conflicts | the security event log and the business audit trail are kept apart |

### Tier to placement, intra `pig-web-defaults`

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB.DATA.INTERFACE.1 | PIG-WEB.ALLOCATION.DB_API | realizes | writes the functions and views the database API placement calls for |
| PIG-WEB.DATA.ORGANIZE | PIG-WEB.ALLOCATION.TYPE_CHAIN | realizes | supplies the schema the type chain starts from or follows |
| PIG-WEB.LOGIC.EXPOSE.6 | PIG-WEB.ALLOCATION.TYPE_CHAIN | realizes | publishes payload schemas in the place the type chain assigns |
| PIG-WEB.DATA.GUARD.3 | PIG-WEB.ALLOCATION.ROW_SECURITY | realizes | writes the row policies the placement calls for |
| PIG-WEB.LOGIC.SECURE.1 | PIG-WEB.ALLOCATION.ROW_SECURITY | realizes | keeps or drops backend checks as the placement sets |
| PIG-WEB.LOGIC.PROCESS.1 | PIG-WEB.ALLOCATION.JOB_HOST | realizes | runs jobs and schedules on the host the placement names |
| PIG-WEB.DATA.DERIVE.2 | PIG-WEB.ALLOCATION.CACHE_STORE | realizes | holds cache tables when the placement keeps caches in Postgres |
| PIG-WEB.LOGIC.EXPOSE.4 | PIG-WEB.ALLOCATION.CACHE_STORE | realizes | uses the cache store the placement names |
| PIG-WEB.INTERACTION.VISUALIZE.1 | PIG-WEB.ALLOCATION.JS_SERVER | realizes | renders with or without a JavaScript server as the placement sets |
| PIG-WEB.TRANSVERSE.TOPOLOGY.2 | PIG-WEB.ALLOCATION.JS_SERVER | constrains | a JavaScript server is one more runtime tier beside the Python server |
| PIG-WEB.INTERACTION.REALTIME.5 | PIG-WEB.ALLOCATION.POSTGRES_FIRST | requires | database notifications as wake-up depend on Postgres carrying the notification role |

### Inter, `pig-web-defaults` to `web-app-philosophy`

Stack placements refine stack-neutral placements (kind `refines`):

| src | dst |
|---|---|
| PIG-WEB.ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.DERIVE.3 |
| PIG-WEB.ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.ACT.3 |
| PIG-WEB.ALLOCATION.DB_API | web-app-philosophy:ALLOCATION.RECORD.2 |
| PIG-WEB.ALLOCATION.TYPE_CHAIN | web-app-philosophy:ALLOCATION.RECORD.3 |
| PIG-WEB.ALLOCATION.ROW_SECURITY | web-app-philosophy:ALLOCATION.GUARD.3 |
| PIG-WEB.ALLOCATION.JOB_HOST | web-app-philosophy:ALLOCATION.ACT.3 |
| PIG-WEB.ALLOCATION.CACHE_STORE | web-app-philosophy:ALLOCATION.DERIVE.3 |
| PIG-WEB.ALLOCATION.JS_SERVER | web-app-philosophy:ALLOCATION.PRESENT.1 |

Stack tier nodes realize stack-neutral placements that have no stack placement in between:

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB.DATA.GUARD.1 | web-app-philosophy:ALLOCATION.GUARD.2 | realizes | declares the invariants the placement gives the database |
| PIG-WEB.DATA.GUARD.4 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | keeps trigger logic within what the business-rules placement allows the database |
| PIG-WEB.DATA.CONCURRENCY | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | implements the concurrency control the placement gives the database |
| PIG-WEB.DATA.CONCURRENCY.4 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | makes mutations idempotent statements |
| PIG-WEB.DATA.CONCURRENCY.6 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | orders state transitions written by their single authoritative writer |
| PIG-WEB.DATA.MAINTAIN.3 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | writes history where the audit placement says |
| PIG-WEB.DATA.MAINTAIN.4 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | runs bulk data work as the deferred-work placement allows |
| PIG-WEB.DATA.DERIVE.1 | web-app-philosophy:ALLOCATION.DERIVE.1 | realizes | keeps denormalized copies in sync as the placement sets |
| PIG-WEB.LOGIC.SECURE.2 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | holds sessions as the identity placement sets |
| PIG-WEB.LOGIC.SECURE.4 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | handles tokens where the identity placement allows them |
| PIG-WEB.LOGIC.ENFORCE.1 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | holds the use cases the business-rules placement gives the backend |
| PIG-WEB.LOGIC.ENFORCE.3 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | pushes filtering and aggregation to the tier the placement names |
| PIG-WEB.LOGIC.PROCESS.2 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | stages and delivers side effects as the placement sets |
| PIG-WEB.LOGIC.EXPOSE.1 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | exposes paging and filtering in the contract |
| PIG-WEB.LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | expresses idempotency keys in the HTTP contract |
| PIG-WEB.LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | expresses deferred operations in the HTTP contract |
| PIG-WEB.LOGIC.EXPOSE.6 | web-app-philosophy:ALLOCATION.GUARD.1 | realizes | parses payloads at the boundary the validation placement names |
| PIG-WEB.INTERACTION.VISUALIZE.2 | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | holds client state where the placement says |
| PIG-WEB.INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | shows conflicts the concurrency placement detects |
| PIG-WEB.INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | keeps the browser share of duplicate suppression |
| PIG-WEB.INTERACTION.COLLABORATE.3 | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | merges long text where the conflict policy calls for an engine |
| PIG-WEB.INTERACTION.COLLABORATE.4 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | creates and delivers notifications as side effects |
| PIG-WEB.INTERACTION.AGENT.3 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | represents agent identity and delegation as the identity placement sets |
| PIG-WEB.INTERACTION.AGENT.4 | web-app-philosophy:ALLOCATION.GUARD.3 | requires | approval designs never replace the authorization authority |
| PIG-WEB.INTERACTION.ENVIRONMENT.2 | web-app-philosophy:ALLOCATION.RECORD.1 | requires | offline use depends on where the system of record is placed |
| PIG-WEB.INTERACTION.ENVIRONMENT.3 | web-app-philosophy:ALLOCATION.PRESENT.2 | requires | translation follows the formatting placement |
| PIG-WEB.TRANSVERSE.OPERABILITY.4 | web-app-philosophy:ALLOCATION.ACT.4 | conflicts | the security event log stays apart from the business audit trail |

Same-branch counterparts (kind `refines`: the stack choices realize the philosophy node):

| src | dst |
|---|---|
| PIG-WEB.ALLOCATION | web-app-philosophy:ALLOCATION |
| PIG-WEB.DATA | web-app-philosophy:DATA |
| PIG-WEB.LOGIC | web-app-philosophy:LOGIC |
| PIG-WEB.INTERACTION | web-app-philosophy:INTERACTION |
| PIG-WEB.TRANSVERSE | web-app-philosophy:TRANSVERSE |
| PIG-WEB.DATA.ORGANIZE | web-app-philosophy:DATA.ORGANIZE |
| PIG-WEB.DATA.GUARD | web-app-philosophy:DATA.GUARD |
| PIG-WEB.DATA.CONCURRENCY | web-app-philosophy:DATA.GUARD |
| PIG-WEB.DATA.MAINTAIN | web-app-philosophy:DATA.MAINTAIN |
| PIG-WEB.DATA.DERIVE | web-app-philosophy:DATA.DERIVE |
| PIG-WEB.LOGIC.SECURE | web-app-philosophy:LOGIC.SECURE |
| PIG-WEB.LOGIC.ENFORCE | web-app-philosophy:LOGIC.ENFORCE |
| PIG-WEB.LOGIC.PROCESS | web-app-philosophy:LOGIC.PROCESS |
| PIG-WEB.LOGIC.EXPOSE | web-app-philosophy:LOGIC.EXPOSE |
| PIG-WEB.INTERACTION.VISUALIZE | web-app-philosophy:INTERACTION.VISUALIZE |
| PIG-WEB.INTERACTION.REALTIME | web-app-philosophy:INTERACTION.COLLABORATE |
| PIG-WEB.INTERACTION.COLLABORATE | web-app-philosophy:INTERACTION.COLLABORATE |
| PIG-WEB.INTERACTION.AGENT | web-app-philosophy:INTERACTION.AGENT |
| PIG-WEB.INTERACTION.ENVIRONMENT | web-app-philosophy:INTERACTION.ENVIRONMENT |
| PIG-WEB.TRANSVERSE.SECURITY | web-app-philosophy:TRANSVERSE.SECURITY |
| PIG-WEB.TRANSVERSE.PERFORMANCE | web-app-philosophy:TRANSVERSE.PERFORMANCE |
| PIG-WEB.TRANSVERSE.CONTRACTS | web-app-philosophy:TRANSVERSE.CONTRACTS |
| PIG-WEB.TRANSVERSE.OPERABILITY | web-app-philosophy:TRANSVERSE.OPERABILITY |
| PIG-WEB.TRANSVERSE.TOPOLOGY | web-app-philosophy:LOGIC.PROCESS |
| PIG-WEB.TRANSVERSE.EVOLUTION | web-app-philosophy:TRANSVERSE.EVOLUTION |

### Inter, `web-app-philosophy` to `python-kb-philosophy`

| src | dst | kind | intent |
|---|---|---|---|
| ALLOCATION | python-kb-philosophy:POLYGLOT | refines | each responsibility goes to the tier whose paradigm fits it (set work in SQL, flow in the backend, rendering at the edge) |
| ALLOCATION.RULES.1 | python-kb-philosophy:DATACENTRICITY | refines | data is the enduring artifact and has one authority; every other copy is derived |
| ALLOCATION.RULES.3 | python-kb-philosophy:DEFENSIVE | refines | checks that decide run where they cannot be bypassed |
| ALLOCATION.GUARD.1 | python-kb-philosophy:DEFENSIVE | refines | input is checked at the boundary |
| ALLOCATION.GUARD.2 | python-kb-philosophy:DEFENSIVE | refines | invariants fail fast at the data |
| DATA.ORGANIZE | python-kb-philosophy:STRUCTURE | refines | the data model is designed before the code |
| DATA.ORGANIZE | python-kb-philosophy:DATACENTRICITY | refines | facts are stored once, normalized |
| DATA.MAINTAIN | python-kb-philosophy:REPRODUCIBILITY | refines | schema changes are versioned and applied by automation |
| LOGIC.EXPOSE | python-kb-philosophy:COMMUNICATION | refines | the interface is designed for its readers |
| TRANSVERSE.CONTRACTS | python-kb-philosophy:COMMUNICATION | refines | contracts are explicit, readable artifacts |
| TRANSVERSE.OPERABILITY.2 | python-kb-philosophy:DEFENSIVE | refines | tests catch failures at the lowest level |
| TRANSVERSE.OPERABILITY.3 | python-kb-philosophy:REPRODUCIBILITY | refines | one build promoted through every environment |
| TRANSVERSE.EVOLUTION.1 | python-kb-philosophy:INTENTIONALITY | refines | the costly decisions are named and recorded with their reasons |
| TRANSVERSE.EVOLUTION.2 | python-kb-philosophy:ROUGHTOFINE | refines | the system grows from a thin whole in increments |
| TRANSVERSE.EVOLUTION.4 | python-kb-philosophy:POLYGLOT | conflicts | few technologies on purpose, against the right paradigm per problem |

## Deferred nodes (scope out, recorded, not researched)

| node | topic | rows owned | related placement |
|---|---|---|---|
| PIG-WEB.DATA.MAINTAIN.6 | GDPR erasure | L526 | - |
| PIG-WEB.DATA.MAINTAIN.7 | high availability and replication | - | ALLOCATION.FORCES.5 |
| PIG-WEB.DATA.DERIVE.3 | search | - | ALLOCATION.DERIVE.2 |
| PIG-WEB.LOGIC.PROCESS.7 | email (scheduled jobs are no longer deferred: ACT.3, JOB_HOST) | - | ALLOCATION.ACT.2 |
| PIG-WEB.INTERACTION.ENVIRONMENT.2 | PWA and offline | - | ALLOCATION.RECORD.1 |
| PIG-WEB.INTERACTION.ENVIRONMENT.3 | internationalisation | - | ALLOCATION.PRESENT.2 |
| PIG-WEB.TRANSVERSE.OPERABILITY.7 | incident response | - | - |

Multi-tenancy stays in light scope (PIG-WEB.DATA.ORGANIZE.6, L128). The local-first position (L302) is no longer deferred: it competes in ALLOCATION.RECORD.1.

## Conventions to check at creation

- Root uids: philosophy root `ROOT`; PIG-WEB follows the `PIG-PY.*` precedent: root `PIG-WEB.ROOT`, L1 `PIG-WEB.<AREA>`, L2 `PIG-WEB.<AREA>.<KEYWORD>`, L3 `PIG-WEB.<AREA>.<KEYWORD>.<n>`; check with the validator before creation, as in round 3.
- Keyword suffixes only at L2; every L3 uid is numeric. Names contain none of `/ \ : * ? " < > | [ ] # ^` (checked by script).
- Traceability: impl_pointers are the `merges` ids of the owned rows; round-4 slots are `18_allocation` (ALLOC), `19_agent_users` (AGENT), `20_collaboration` (COLLAB). Rows whose originals cited no source (L278, L270's API-C25 part, L673, L684) carry `-` or only ledger references.
- Public repository: no private name or absolute path; MAINT-S01 is cited only by its id.
