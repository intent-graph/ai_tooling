# Branch CONSTRUCTION: tree and node records

Realization branch (`../../../target_hierarchy.md`): how code is structured, in its language-neutral form, so that it is correct and stays changeable. Cut top-down from each L2 node's intent in `../../tree_l2.md`, then the 87 routed rows were attached (`../../routing.md`). No verdict, no ranking, no merging or editing of ledger rows. Positions are the competing practices the rows record; a row that states a single practice is listed as one position with "no competing position recorded". Rows judged earlier in the JavaScript guideline keep that verdict as one position ("prior verdict"), never as the decision (the row text says the judge here re-examines it). Certainty marks are the rows' own.

How to read a record: `Decides` is the question; `Rows` the attached ledger ids; each position gives the practice, its strongest argument, the force it serves, the condition under which it would be the best (or "condition not stated by the row"), with row and source (REG) ids; `Context` appears only where a row itself says the best practice moves with a variable (MD-02), quoting the row; `Links` only where a row states the relation, or marked "related (no row states the type)".

## Tree

- `CONSTRUCTION` Construction
  - `CONSTRUCTION.DESIGN` Design Derivation
    - `CONSTRUCTION.DESIGN.1` Derivation Order
    - `CONSTRUCTION.DESIGN.2` Effort and Timing on Costly Decisions
    - `CONSTRUCTION.DESIGN.3` Properties First, Then Constraints
    - `CONSTRUCTION.DESIGN.4` Growth Horizon
  - `CONSTRUCTION.SYSTEM_SHAPE` System Shape
    - `CONSTRUCTION.SYSTEM_SHAPE.1` Initial Shape, One Unit or Several
    - `CONSTRUCTION.SYSTEM_SHAPE.2` Distribution Premium and Its Reversal
    - `CONSTRUCTION.SYSTEM_SHAPE.3` Placing Service Boundaries
    - `CONSTRUCTION.SYSTEM_SHAPE.4` Teams and Structure
  - `CONSTRUCTION.HIDING` Information Hiding and Modularity
    - `CONSTRUCTION.HIDING.1` Cut by Hidden Decision
    - `CONSTRUCTION.HIDING.2` Cut by Business Concept or by Layer
    - `CONSTRUCTION.HIDING.3` Separating Presentation, Domain and Data Access
    - `CONSTRUCTION.HIDING.4` Data Ownership by One Application
  - `CONSTRUCTION.BOUNDARY` Boundary Contracts and Call Shape
    - `CONSTRUCTION.BOUNDARY.1` Parse or Validate at the Edge
    - `CONSTRUCTION.BOUNDARY.2` What Counts as Valid
    - `CONSTRUCTION.BOUNDARY.3` What a Contract States
    - `CONSTRUCTION.BOUNDARY.4` The Contract Over Stored Data
    - `CONSTRUCTION.BOUNDARY.5` Call Shape and Evolvable Interfaces
    - `CONSTRUCTION.BOUNDARY.6` Errors at the Boundary
  - `CONSTRUCTION.STATE` State, Values and Load-Time Effects
    - `CONSTRUCTION.STATE.1` One Place per Fact
    - `CONSTRUCTION.STATE.2` Normal Form for Stored Data
    - `CONSTRUCTION.STATE.3` Shared Derived State
    - `CONSTRUCTION.STATE.4` Value Precision and Mutability
    - `CONSTRUCTION.STATE.5` Load-Time Effects
  - `CONSTRUCTION.DEPENDENCY_DIRECTION` Dependency Direction
    - `CONSTRUCTION.DEPENDENCY_DIRECTION.1` No Cycles
    - `CONSTRUCTION.DEPENDENCY_DIRECTION.2` Declared Layering
  - `CONSTRUCTION.NAMING` Naming
    - `CONSTRUCTION.NAMING.1` Whole Words
    - `CONSTRUCTION.NAMING.2` One Concept One Name
    - `CONSTRUCTION.NAMING.3` Names Derived from Concepts
  - `CONSTRUCTION.PARADIGM` Paradigm and Placement of Logic
    - `CONSTRUCTION.PARADIGM.1` Paradigm by Intent
    - `CONSTRUCTION.PARADIGM.2` Placement of Domain Logic
  - `CONSTRUCTION.DATA_NOT_CODE` Keeping Data From Becoming Code
    - `CONSTRUCTION.DATA_NOT_CODE.1` Code and Commands
    - `CONSTRUCTION.DATA_NOT_CODE.2` Queries
    - `CONSTRUCTION.DATA_NOT_CODE.3` Paths and Destinations
    - `CONSTRUCTION.DATA_NOT_CODE.4` Structured Payloads
  - `CONSTRUCTION.PROCESS` Process Lifecycle
    - `CONSTRUCTION.PROCESS.1` Fast Start and Graceful Stop
    - `CONSTRUCTION.PROCESS.2` Fail Fast Under Supervision
    - `CONSTRUCTION.PROCESS.3` Stateless Processes

## Nodes

#### CONSTRUCTION Construction

Decides: How is code structured, in its language-neutral form, so that it is correct and stays changeable (L1 branch, realization; carries out what OWNERSHIP and ASSURANCE decide).
Rows: none (0)
Positions in the evidence: none at this level; see the ten L2 nodes.
Links: Realizes `ASSURANCE.CONTRACTS` (boundary contracts, via CONSTRUCTION.BOUNDARY); related (no row states the type) `ASSURANCE.SECURITY`, `TRANSVERSE.SECURITY`, `TRANSVERSE.CONFIG`.

#### CONSTRUCTION.DESIGN Design Derivation

Decides: How design is derived before code and where design effort is spent.
Rows: none (0)
Positions in the evidence: see children.

#### CONSTRUCTION.DESIGN.1 Derivation Order

Decides: In what order is a design derived before code is written, and does naming get design effort.
Rows: L329 (1)
Positions in the evidence (no verdict):
- P1 MAINT position (L329, source MAINT-S01, not citable): derive before coding, in order usage and functional scenario, data flow, schema, system design, implementation strategy, then code; write the strategy (why and how in abstract terms) before the tactics; invest in hierarchical, unambiguous, intuitive names. Strongest argument: design first. Force: correctness, reversibility. Condition: not stated beyond "design first"; the row reads public practice as majority (REG-181).
- P2 Test-first or emergent design (named in L329 as the practice it differs from). Force: speed of feedback. Condition: not stated by the row.
Forces in tension: correctness and reversibility against speed of feedback.
Note: L329 bundles two statements (derivation order; naming); the naming half is also the subject of CONSTRUCTION.NAMING.
Links: related (no row states the type) `CONSTRUCTION.NAMING`, `OWNERSHIP.STANCE`.

#### CONSTRUCTION.DESIGN.2 Effort and Timing on Costly Decisions

Decides: Where is design effort spent, and when are hard-to-reverse decisions taken.
Rows: L1206, L1209 (2)
Positions in the evidence (no verdict):
- P1 Treat architecture as the shared understanding of the important decisions, those costly to get wrong, and spend design effort there (L1206; consensus; REG-1121). Force: cost of error. Condition: not stated; no competing position recorded.
- P2 Defer decisions that are hard to reverse until the product is understood; in a new product, do not fix distributed boundaries up front (L1209; consensus; REG-1112). Force: reversibility. Condition: not stated; no competing position recorded in these rows. The ledger records the maintainer's opposite lean for another node: L330 (design for probable future use; routed to OWNERSHIP.STANCE) is listed by L1209 as related.
Links: related (no row states the type) `OWNERSHIP.STANCE`.

#### CONSTRUCTION.DESIGN.3 Properties First, Then Constraints

Decides: Does design start from the required properties, and are proposed changes tested against the constraints that induce them.
Rows: L1226 (1)
Positions in the evidence (no verdict):
- P1 Choose the system's required properties first, then adopt the set of architectural constraints that induces them, and test proposed changes against those constraints (L1226; consensus; REG-1124, REG-1125; origin wording was HTTP-framed, restated neutral by the ledger). Force: fit between structure and required properties. Condition: not stated; no competing position recorded.
Stack pointers: L1226 origin stack http.

#### CONSTRUCTION.DESIGN.4 Growth Horizon

Decides: For what scale is a design made, and is replacement planned.
Rows: L1235 (1)
Positions in the evidence (no verdict):
- P1 Design for roughly 10x growth and plan to rewrite before 100x; early parts may be sacrificial, kept modular, and replaced by the team that built them (L1235; majority; REG-1118). Force: avoid over-design now. Condition: not stated.
- P2 Replace incrementally behind the existing interface instead of rewriting wholesale (L039 from OWNERSHIP, listed by L1235 as related; REG-033; force reversibility and delivery speed; wins when behaviour is poorly specified and users cannot wait).
Links: related (no row states the type) `EVOLUTION.INCREMENTAL`, `OWNERSHIP.STANCE`.

#### CONSTRUCTION.SYSTEM_SHAPE System Shape

Decides: How the system is divided into deployable units and how that division follows teams and domain.
Rows: none (0)
Positions in the evidence: see children.

#### CONSTRUCTION.SYSTEM_SHAPE.1 Initial Shape, One Unit or Several

Decides: Does a new hosted service start as one deployable unit or as several, and what moves that.
Rows: L1210, L1211, L1214, L1218 (4)
Positions in the evidence (no verdict):
- P1 Start as one deployable unit (a monolith) and split only when it becomes a problem (L1210; majority; for: Fowler, DHH, Segment, Shopify's path; REG-1016, REG-1112, REG-1113, REG-1116, REG-1122). Force: simplicity, cost. Condition: the system can stay simple.
- P2 Do not consider microservices unless the system is too complex to manage as a monolith (L1211; consensus; REG-1113). Same direction as P1, with its trigger stated.
- P3 Services from the start (the "against" side of L1210). Not read by the origin; Fowler notes the evidence is sparse and that large organisations (Amazon, Netflix) report success with services. Condition: not stated.
- P4 Avoid distributing computation when you can: remote calls cost more than in-process calls and moving to services shifts complexity into the connections (L1214; consensus; REG-1016, REG-1116).
- P5 In a small team, integrate until one person can hold the system in their head; copying large-company service patterns is a risk (L1218; majority; DHH strongly, Fowler agrees on direction not on the "one head" criterion; REG-1112, REG-1116).
Forces in tension: simplicity and cost against fault isolation and independent scaling.
Context: team size (L1218: "In a small team"); system complexity (L1211: "unless the system is too complex to manage as a monolith").
Stack pointers: L1210 restated from a web wording (origin stack neutral).
Links: related (no row states the type) `CONSTRUCTION.SYSTEM_SHAPE.3` (L1210 lists L171 and L308 as related).

#### CONSTRUCTION.SYSTEM_SHAPE.2 Distribution Premium and Its Reversal

Decides: What must be budgeted before adopting services, and when is consolidating services back legitimate.
Rows: L1212, L1219 (2)
Positions in the evidence (no verdict):
- P1 Budget for the distribution premium before adopting services: automated deployment, monitoring, failure handling, eventual consistency (L1212; consensus; REG-1016, REG-1113). Condition: not stated; no competing position recorded.
- P2 Consolidating services back into one deployable is legitimate when operating cost grows with the number of services (Segment: 140+ services, per-service scaling and dependency drift), accepting less fault isolation (L1219; majority; one case study T3, no T2 source states the reverse migration as a rule; REG-1122). Force: cost of operation. Wins when: operating cost grows with the number of services.
Context: number of services against operating cost (L1219).
Links: related (no row states the type) `OPERATION.RELIABILITY`.

#### CONSTRUCTION.SYSTEM_SHAPE.3 Placing Service Boundaries

Decides: When service boundaries are placed and what they must guarantee.
Rows: L171, L1213 (2)
Positions in the evidence (no verdict):
- P1 Place service boundaries only after the domain is understood: moving functionality between services is much harder than within a monolith (L1213; consensus; REG-1016, REG-1112). Force: reversibility.
- P2 Design services so they can be deployed independently, without orchestrated lock-step upgrades; loose coupling is among the strongest predictors of continuous delivery (L171; consensus; REG-092, REG-097). Force: delivery speed. The origin records its source as application architecture, then out of scope, "recorded as a pointer"; MD-05 now puts code design in scope.
- P3 Evolve shared interfaces additively and coordinate breaking changes with every consumer, deploying them together (L295, MAINT-C31, routed to another branch; the coverage check records that it contradicts L171). Force: cost of ownership. Wins when few in-house consumers are reachable by review and conversation (row L295).
Links: related (no row states the type) `ASSURANCE.CONTRACTS` (L171 routing note: the contract tests that verify independent deployability stay there).

#### CONSTRUCTION.SYSTEM_SHAPE.4 Teams and Structure

Decides: How team organisation and system structure relate.
Rows: L1221, L1222 (2)
Positions in the evidence (no verdict):
- P1 Do not organise teams by layer; developers need not be full-stack but teams should be, cross-functional and organised around a capability (L1221; consensus; REG-1016, REG-1115). Force: delivery flow.
- P2 Expect system structure to copy team communication structure; design the team structure and the module structure together (L1222; consensus; REG-1016, REG-1127).
No competing position recorded for either.

#### CONSTRUCTION.HIDING Information Hiding and Modularity

Decides: How code is cut into modules so that each difficult or changing decision lives behind one boundary.
Rows: L1511 (1)
Positions in the evidence: L1511 is the origin's roll-up of its structure principles (decisions hidden behind module boundaries, state in one place, importing free of hidden effects, one-way dependencies, names carrying concepts, paradigm by intent). It has no claim of its own (not assessable; inferred); its parts are spread over HIDING, STATE, DEPENDENCY_DIRECTION, NAMING and PARADIGM. Prior verdict: carved out at the split of a node that stays narrowed in the JavaScript guideline.
Links: related (no row states the type) `CONSTRUCTION.STATE`, `CONSTRUCTION.DEPENDENCY_DIRECTION`, `CONSTRUCTION.NAMING`, `CONSTRUCTION.PARADIGM`.

#### CONSTRUCTION.HIDING.1 Cut by Hidden Decision

Decides: By what are modules cut, and how much of a module is exposed.
Rows: L1512, L1513, L1514, L1515 (4)
Positions in the evidence (no verdict):
- P1 Put each difficult or likely-to-change decision behind one module boundary and expose as little as possible (L1512; node intent, no claim of its own; prior verdict: known; inferred). Decompose by listing those decisions and hiding each in one module (L1513; single source Parnas, T2, principle only, no effect evidence; REG-1508). Force: changeability. Condition: not stated by the row.
- P2 Decompose by the steps of processing (named in L1513 as the practice it replaces). Condition: not stated.
- P3 Expose from each module only what others need, at every level at which the language lets a name be exposed (L1515; inferred cross-level rule; single source; REG-1508, REG-1510, REG-1511, REG-1512; prior verdict: known, unvalidated). Requires L1513 (row-stated).
- P4 Know which of two hiding styles an interface offers: an abstract data type hides a representation behind operations; an object exports a procedural interface and hides by procedural abstraction; they are not conflated when designing an API (L1514; single source Cook, T2, distinction without effect evidence for choosing either; REG-1509; prior verdict: known).
- Language-neutral statement for L1514 (resolved from the flag; taken from the row's own evidence, REG-1509 Cook, T2: "the conceptual distinction between objects and abstract data types", independent of any one language): an interface hides information either by an abstract type that hides a representation behind operations, or by a set of operations whose implementation varies per instance (procedural abstraction); the two designs differ, a design states which it offers, and an API does not conflate them. "Object" here means the second design, not a language construct. Grounded for the distinction (one T2 source); no effect evidence for choosing either. No ledger edit.
Links: L1515 requires L1513 (both here, internal); related (no row states the type) `OWNERSHIP.CONTAINMENT` (L1512 lists L068, a thin wrapper around a dependency, and L308 as adjacent).

#### CONSTRUCTION.HIDING.2 Cut by Business Concept or by Layer

Decides: Is a modular system divided along business concepts or technical layers, and how are large domains split.
Rows: L1215, L1217 (2)
Positions in the evidence (no verdict):
- P1 Make the monolith modular by business concept (orders, billing) rather than by technical layer, with public interfaces between modules (L1215; majority; Shopify T3 is the only practitioner case, Fowler states the same goal without prescribing the cut; REG-1016, REG-1117). Force: changeability.
- P2 Cut by technical layer: presentation, domain, data access (L1220, attached to CONSTRUCTION.HIDING.3). The two rows are in tension on the axis of the cut; no row states which wins.
- P3 Do not force one unified model on a large domain; use several bounded contexts with explicit mappings between them (L1217; consensus; REG-1123; related L344 EXT-C14).
Links: related (no row states the type) `CONSTRUCTION.HIDING.3`.

#### CONSTRUCTION.HIDING.3 Separating Presentation, Domain and Data Access

Decides: Is domain logic kept apart from presentation and data access, and how loosely are layers coupled.
Rows: L1220, L1223, L1224 (3)
Positions in the evidence (no verdict):
- P1 Separate presentation, domain logic and data access: it narrows the scope of attention, enables several presentations over one domain, and creates test seams (L1220; consensus; REG-1115). Force: testability, changeability.
- P2 Keep business logic free of UI and database entanglement so it can be driven by users, tests, batch jobs or other programs and run without a live database (L1223; consensus; REG-039, REG-1115).
- P3 Keep the layers loosely coupled and each concept or datum in one place only (L1224; consensus; REG-1131; origin stack python, restated neutral). Its second half restates CONSTRUCTION.STATE.1.
- P4 Modularise by business concept rather than by technical layer (L1215, attached to CONSTRUCTION.HIDING.2): the competing axis.
Stack pointers: L1224 origin stack python.
Links: related (no row states the type) `CONSTRUCTION.HIDING.2`, `CONSTRUCTION.STATE.1`, `CONSTRUCTION.DEPENDENCY_DIRECTION.2` (L1220 and L1223 list L409, DATA-C32, as related).

#### CONSTRUCTION.HIDING.4 Data Ownership by One Application

Decides: Who owns a database schema, and is a shared database an integration mechanism.
Rows: L1225 (1)
Positions in the evidence (no verdict):
- P1 One application owns its database schema; avoid a database shared by several applications as an integration mechanism (L1225; consensus; REG-1133). Force: freedom to change the schema. Condition: not stated.
- P2 Shared access through a dedicated contract schema (L1285, attached to CONSTRUCTION.BOUNDARY.4, contested): the ledger keeps the two as near claims apart.
Stack pointers: L1225 origin stack postgres.
Links: related (no row states the type) `CONSTRUCTION.BOUNDARY.4`.

#### CONSTRUCTION.BOUNDARY Boundary Contracts and Call Shape

Decides: What a boundary states and how a call is shaped.
Rows: L1503 (1)
Positions in the evidence: L1503 is the origin's roll-up: make intent checkable at run time by parsing untrusted data at every trust boundary and by the shape of calls, so a violated expectation is reported where it arises (principle, no claim of its own; inferred; prior verdict: part carved out of a node that stays narrowed in the JavaScript guideline; the build-time type layer was dropped there as language-specific). It rolls up the children .1 to .6.
Links: Realizes `ASSURANCE.CONTRACTS` (routing notes of L171 and L309: this branch holds the form a boundary takes, that node holds how compatibility is verified).

#### CONSTRUCTION.BOUNDARY.1 Parse or Validate at the Edge

Decides: In what form is what crosses a trust boundary checked, where, and how strictly typed.
Rows: L1504, L1505, L1274, L1275, L1280 (5)
Positions in the evidence (no verdict):
- P1 Parse, do not validate: convert untrusted input into the most precise type needed once, at the boundary, before any of it is acted on; scattered re-checking deeper ("shotgun parsing") lets partly processed invalid data through (L1274; consensus, single source no dissent; REG-1151). Force: correctness of everything past the boundary.
- P2 Parse every datum that crosses a trust boundary into the shape the program expects before use, so code past the boundary may rely on that shape (L1504; node intent, no claim of its own; inferred; prior verdict: known; no source ids).
- P3 Validate all data crossing a trust boundary before the application uses it, including data from internal services, queues and stored records (L1505; consensus, two T1 sources; REG-1503, REG-1504; prior verdict: known). The origin's TYPES-C29 half (validate at a trusted service layer, never rely on client-side validation as a security control) is placed deferred to the sibling web-architecture guideline and travels with this row unjudged.
- P4 Model data with the most precise structure reasonably available so illegal states cannot be represented, carried by types at the boundary and by NOT NULL, CHECK, foreign keys and domains in the database (L1275; consensus; REG-1139, REG-1151).
- P5 Decide coercion at the boundary explicitly: strict or coercing parsing per boundary (L1280; decision; single source; REG-1155). Wins for coercing: a form or query string where coercion is needed; strict: a JSON API.
No row states whether P1 and P3 differ in outcome or only in wording: P1 says re-checking deeper is a defect, P3 says validate before use at every trust boundary.
Context: strict or coercing parsing per boundary kind (L1280: "per boundary (a JSON API versus a form or query string, where coercion is needed)").
Stack pointers: L1280 origin stack python; L1275 restated from web wording.
Links: related (no row states the type) `CONSTRUCTION.BOUNDARY.2`, `CONSTRUCTION.STATE.1` (adjacent rows: L342 parse an external payload in one place, L340 third-party responses are untrusted, L279 integrity enforced where writes converge, MAINT-C15).

#### CONSTRUCTION.BOUNDARY.2 What Counts as Valid

Decides: How validity is defined for an input.
Rows: L1506, L1507, L1508 (3)
Positions in the evidence (no verdict):
- P1 Accept by positive rule: state what is valid (allowlist of values, patterns, ranges, or comparison to an expected structure) and reject the rest (L1506; consensus, two T1 sources; REG-1503, REG-1504; prior verdict: known). Rejected position: denylisting bad input; the origin states no condition under which it would be best. Refines L1508 (row-stated).
- P2 A well-formed value can still break a rule: check syntax and semantics, including combinations of related fields (L1507; consensus, two T1; REG-1503, REG-1504; prior verdict: known).
- P3 Input handling is a recognizer of valid inputs: keep input languages simple enough to be recognized completely before anything is computed from them; do not hand-write ad-hoc allow or deny pattern lists for complex input languages, which are unreliable (L1508; single source, T2, a 2011 technical report; REG-1505; no effect evidence; prior verdict: position kept as a position, complex input languages need a real parser).
Links: related (no row states the type) `CONSTRUCTION.DATA_NOT_CODE`.

#### CONSTRUCTION.BOUNDARY.3 What a Contract States

Decides: What a written contract at a boundary must state and carry.
Rows: L1268, L1269, L1270, L1288, L1289, L1287 (6)
Positions in the evidence (no verdict):
- P1 A data contract is an explicit artifact stating structure and meaning (names, types, nullability, units, invariants, owner, version), readable without the producer's source code (L1268; consensus; REG-1149, REG-1153; synthesis for "units, invariants" inferred).
- P2 A schema is necessary but not sufficient: record units, time zone, precision and rounding in the contract text or in constraints, because a schema format may carry no integer, float or date type and its format keywords may be annotations, not assertions (L1269; consensus; REG-1148, REG-1154; origin stack http).
- P3 Declare "may be null" and "may be absent" separately: a null value is not a missing property (L1270; consensus; REG-1147, REG-1154; origin stack http).
- P4 State types logically and map physically: keep the logical type in the contract and derive the database, server and client types from it (L1288; consensus, single source; REG-1153; the separation is grounded, the derivation inferred).
- Language-neutral statement for L1288 (resolved from the flag; taken from the row's own evidence, REG-1153 Open Data Contract Standard, T2, which separates a logical type from a physical type): state each type logically in the contract (string, date, timestamp, number, integer, object) and map it physically per technology, deriving the store's, the server's and the client's types from the contract; the three technologies the ledger statement names are the origin's examples of derived targets, not part of the claim. Separation grounded; derivation inferred. No ledger edit.
- P5 Give every contract one owner, a version and a lifecycle status (proposed, draft, active, deprecated, retired); the provider contract is singular and authoritative (L1289; consensus; REG-1152, REG-1153). MAINT-C31 (L295, routed to another branch) states the opposite on version numbers: do not introduce them, keep a dated change log.
- P6 Data contracts in the data-engineering sense are a platform-agnostic document with sections for fundamentals, schema, quality, SLA, team, roles, support and authoritative definitions; for one application database take the field list as a checklist (owner, meaning, quality rules, freshness or availability promise, lifecycle) and skip the format unless data leaves the application for a platform team (L1287; open; inferred; REG-1153; no source says whether it applies to an application database). MD-05 defers data and ML pipelines.
Context: whether data leaves the application for a platform team (L1287).
Stack pointers: L1269 and L1270 origin stack http; L1288 names three stacks.
Links: related (no row states the type) `ASSURANCE.CONTRACTS`, `EVOLUTION.DECOMMISSION` (L1289 lists L215 and L1006 as related or near; lifecycle statuses overlap deprecation).

#### CONSTRUCTION.BOUNDARY.4 The Contract Over Stored Data

Decides: Is the database itself a contract (the constraints that hold whichever code writes are placed in `ASSURANCE.DATA_INTEGRITY`).
Rows: L1285 (1)
Positions in the evidence (no verdict):
- P1 The database is the contract: expose a dedicated schema of views and functions, not base tables, so internals change while backward compatibility holds, and the layer gives a natural way to version the interface (L1285; contested; single source family PostgREST-style, REG-1156, T3; origin boundary DATA). Force: independent change of internals. Wins when: several consumers or strict privilege separation.
- P2 An application API over base tables with migration discipline (L1285 position b; WL187 unread in part 1, now read). Wins when: a single application server owns the database.
- P3 Prefer an interface with a signature over a shape-bound view (MAINT position, L309, attached to CONSTRUCTION.BOUNDARY.5): its positions on views against functions bear on P1.
Context: number of consumers and whether privilege separation is required (L1285: "several consumers or strict privilege separation favor the contract schema; a single app server owning the database does not need it").
Stack pointers: L1285 origin stack postgres, restated neutral.
Links: related (no row states the type) `ASSURANCE.DATA_INTEGRITY`, `CONSTRUCTION.HIDING.4`, `CONSTRUCTION.BOUNDARY.5`.

#### CONSTRUCTION.BOUNDARY.5 Call Shape and Evolvable Interfaces

Decides: What shape a call or interface takes so that consumers can bind to it and it can change.
Rows: L309, L1509, L1272, L1279, L1278, L341 (6)
Positions in the evidence (no verdict):
- P1 MAINT position (L309, source MAINT-S01, not citable): prefer an interface with a signature (parameters, defaults, overloads) to one consumers bind to by exact shape, because a shape-bound object ossifies like a table and has nothing to absorb change; keep shape-bound objects for owner-only throwaway or introspection use (grounded; REG-181; public practice read as contested). Recorded sub-positions: (a) views as a stable read interface, declarative, no code, plannable, serves cost of ownership, wins for read-only reporting with several consumers; (b) function, serves change absorption and owner-tunable performance, wins when many backends depend on the contract. The ledger notes the doctrine contradicts the common practice of offering views as a stable interface.
- P2 A call carries its meaning by name and not by position: cap positional parameters, because each parameter, its type and its order must be memorised by every reader and writer (L1509; single source, one T1 tool documentation; REG-1506; the principle inferred, quote tool-extracted; prior verdict: known, no numeric cap imported). Refines L1522 (row-stated, CONSTRUCTION.NAMING).
- P3 Use separate input and output models so the output model limits and filters what leaves the server (L1272; consensus, single source; REG-1150; origin stack python; origin boundary SEC).
- P4 Treat object schemas as open for readers and closed for writers: reject unknown fields on request bodies you control, tolerate them in responses consumers parse (L1279; consensus single source; REG-1147; the reader and writer rule inferred; origin stack http).
- P5 Generating consumer code from the full producer schema trades resilience for convenience; prefer readers that take only the elements they need (read what you use, ignore the rest) (L1278; consensus; REG-1152, REG-208; L341 EXT-C11, now attached to this node as P6, states the same, kept apart).
- P6 Parse only the fields you need and ignore unknown ones, so a provider can add fields without breaking you (L341; contested; moved here from `OWNERSHIP.CONTAINMENT`). (a) Tolerant reader (REG-208; force evolution without breakage, delivery speed; wins when the provider evolves additively and is outside your control). (b) Strict schema validation of everything received (REG-194 "validate and sanitize"; force security, detection of drift; wins when data crosses a trust boundary or feeds an interpreter). Synthesis, inferred by the row: tolerate unknown fields, validate the fields you use for type, range and size. Grounded for each position, inferred for the synthesis; REG-194, REG-204, REG-208. Same claim as P5 (L1278) and P4 (L1279).
Links: Refines `CONSTRUCTION.NAMING` (L1509); related (no row states the type) `CONSTRUCTION.BOUNDARY.4`, `ASSURANCE.CONTRACTS` (L309 routing note: this is the form a boundary takes, not how compatibility is verified).

#### CONSTRUCTION.BOUNDARY.6 Errors at the Boundary

Decides: What a failure at a boundary carries and who is at fault when output is malformed.
Rows: L315, L1273 (2)
Positions in the evidence (no verdict):
- P1 MAINT position (L315, source MAINT-S01, not citable): errors name the component and the offending values and carry stable custom codes; mandatory inputs are validated first, and a failure is explicit rather than silent (grounded; REG-181; public practice read as consensus, agrees). Force: diagnosability.
- P2 A response that fails its declared output model is a defect in server code, not a client error: return a server error rather than a malformed body (L1273; consensus single source; REG-1150; origin stack python).
Links: related (no row states the type) `ASSURANCE.DATA_INTEGRITY` (L1286, now attached there, names constraints so violations map to stable contract errors), `CONSTRUCTION.BOUNDARY.1` (L1274 lists L315 as related).

#### CONSTRUCTION.STATE State, Values and Load-Time Effects

Decides: Each fact held in one place, values that state their precision and mutability, modules without load-time effects.
Rows: none (0)
Positions in the evidence: see children.

#### CONSTRUCTION.STATE.1 One Place per Fact

Decides: How many places hold a piece of state, and how copies are prevented from drifting.
Rows: L1516, L1517, L1276 (3)
Positions in the evidence (no verdict):
- P1 Keep each piece of state in one place (L1516; node intent, no claim of its own; inferred; prior verdict: part carved out of a node that stays narrowed). Hold each piece once and derive the rest so copies cannot drift (L1517; single source Codd, T2; grounded for shared data, inferred for application state; REG-1513; prior verdict: known). Force: consistency.
- P2 Keep one source of truth per fact: duplicated representations create "places getting out of sync" as a representable illegal state, which applies to hand-copied type definitions across tiers (L1276; consensus, single source; REG-1151; the cross-tier application inferred).
Links: related (no row states the type) `CONSTRUCTION.STATE.2`, `CONSTRUCTION.HIDING.3` (L1517 lists L281 derived data needs a synchronisation plan, and L218 one canonical document per topic, as adjacent).

#### CONSTRUCTION.STATE.2 Normal Form for Stored Data

Decides: How relational tables are shaped so that each fact is stored once, and when that is relaxed.
Rows: L1263, L1264, L1265, L1266, L1267 (5)
Positions in the evidence (no verdict):
- P1 Design relational tables to third normal form by default: every non-key field states a fact about the key, the whole key, and nothing but the key (L1263; consensus; REG-1144, REG-1146). Force: one place per fact.
- P2 Purpose of normalization: prevent redundancy, update anomalies and inconsistent dependencies so each fact is stored and changed in one place (L1264; consensus; REG-1144, REG-1146; L281 MAINT-C17 related).
- P3 Denormalize deliberately, not by default: no obligation to fully normalize where measured performance requires otherwise, but the application must then guard the redundancy; normalization tends to penalize retrieval (L1265; consensus; REG-1144, REG-1146). Force: retrieval speed. Wins when: measured performance requires it.
- P4 Third normal form is the practical target for most applications; higher forms matter in specific multi-valued or overlapping-key designs (L1266; majority; REG-1146 T3 says higher forms are rarely considered, REG-1144 describes them without ranking; 3NF grounded, "specific designs" inferred).
- P5 Remove repeating groups (Class1, Class2, Class3 columns) into a child table linked by a foreign key (L1267; consensus single source; REG-1146).
Context: measured performance requirement (L1265: "where measured performance requires otherwise").
Note: technology-bound to relational storage, not to a programming language.
Links: related (no row states the type) `CONSTRUCTION.STATE.1`, `ASSURANCE.DATA_INTEGRITY`.

#### CONSTRUCTION.STATE.3 Shared Derived State

Decides: Where a cache lives and how it is invalidated.
Rows: L1204, L1205 (2)
Positions in the evidence (no verdict):
- P1 Use an application cache shared across processes in multi-process production; a cache is never permanent storage (L1204; consensus; REG-1107, REG-1109; origin stack python, origin named two cache servers, restated neutral). Force: coherence across processes.
- P2 Per-process local memory as the cache (named in L1204 as not suitable in multi-process production). Condition: not stated beyond the single-process case the row implies.
- P3 Give every cache an explicit expiry or invalidation plan and version or prefix its keys, because invalidation is the hard part (L1205; practice; inferred, REG-1111 is the attribution of a proverb, not evidence; REG-1107).
Links: related (no row states the type) `CONSTRUCTION.PROCESS.3`, `CONSTRUCTION.STATE.1`.

#### CONSTRUCTION.STATE.4 Value Precision and Mutability

Decides: Which values a type may carry, and whether a value's changeability is stated by the code.
Rows: L1501, L1502 (2)
Positions in the evidence (no verdict):
- P1 The precision and range of a numeric type decide which values may travel in it: values beyond them use an exact representation (L1501; single source; inferred for the positive statement, which the origin takes from its JavaScript rule; prior verdict; REG-1501). Holds for any language with binary floating point (row's own scope).
- P2 A fixed tolerance E as the general cure for float equality (L1501, rejected in the origin: choosing E is arbitrary and "differs by less than E" is not transitive; Goldberg 1991, T2, single source; no condition under which it would be best is stated).
- P3 Whether a value cannot change at all (immutability) or may be changed only by some holders (read-only restriction) is a distinction the code states, and a language mechanism is chosen for the one it gives (L1502; single source, T2 taxonomy; grounded for the distinction; open for any preference between the two; no admitted source states immutability as a design preference; REG-1502; prior verdict: known).
- Language-neutral statement for L1501 (resolved from the flag; taken from the row's own evidence, REG-1501 Goldberg 1991, T2, which states a mechanism of floating-point arithmetic and no language-specific rule): a numeric type carries exactly only the values within its precision and range; a value beyond them needs a type that represents it exactly; where a type rounds (binary floating point), equality of computed values is not restored by an ad-hoc fixed tolerance, which is arbitrary and not transitive. Scope condition stays the row's own: it applies in any language that has such a type. Grounded for the tolerance point (one T2 source); inferred for the positive statement. No ledger edit.
Links: none stated.

#### CONSTRUCTION.STATE.5 Load-Time Effects

Decides: May loading a module have effects beyond initialising its own exports.
Rows: L1518 (1)
Positions in the evidence (no verdict):
- P1 Loading a module is safe in any order because its top level has no effect beyond initialising its own exports; effect-free initialisation also lets tools drop unused code (L1518; single source; inferred, no source states the rule, quote not obtained; REG-1514, REG-1515, REG-1516; prior verdict: known, unvalidated). Holds for any language that runs module code at load time (row's own scope). No competing position recorded.
Links: Refines `CONSTRUCTION.DEPENDENCY_DIRECTION.1` (row-stated: L1518 refines L1520).
Stack pointers: L1518 (stack pointer, resolved from the flag: its only sources REG-1514, REG-1515 and REG-1516 are the JavaScript import statement, one bundler's tree-shaking field and CommonJS loading; the row's own evidence holds no language-neutral statement of the load-order rule, so the rule is carried by the stack guideline of languages that run module code at load time).

#### CONSTRUCTION.DEPENDENCY_DIRECTION Dependency Direction

Decides: Dependencies between modules flow one way, never in a cycle, under declared layering.
Rows: L1519 (1)
Positions in the evidence: L1519 is the node-level statement: let dependencies flow in one direction so that a change propagates predictably (no claim of its own; inferred, rolls up two child rows; prior verdict: known, gap: layering undecided).

#### CONSTRUCTION.DEPENDENCY_DIRECTION.1 No Cycles

Decides: May modules depend on each other in a cycle.
Rows: L1520 (1)
Positions in the evidence (no verdict):
- P1 No cycles, so load or initialization order never decides whether code works (L1520; no claim of its own; inferred, derived from a JavaScript rule, no source measures the cost; REG-1516).
- P2 Tolerate cycles: they are a supported mechanism (the Node CommonJS documentation states no recommendation against them) (L1520, conflict kept by the origin; the origin gives no condition under which tolerating would be best).
Links: none stated beyond the incoming `CONSTRUCTION.STATE.5` (L1518 refines this row).

#### CONSTRUCTION.DEPENDENCY_DIRECTION.2 Declared Layering

Decides: Are allowed import directions between kinds of module declared and mechanically enforced.
Rows: L1521 (1)
Positions in the evidence (no verdict):
- P1 Declare which kinds of module may import which kinds and enforce it mechanically (L1521; practice; open: undecided in the origin, no admitted source grounds a layering principle, the only mechanism source documents environment fit; REG-1517, REG-1508). Fact kept: a lint-style rule can forbid imports by path or pattern. Condition: not stated.
Links: related (no row states the type) `CONSTRUCTION.HIDING.3`.

#### CONSTRUCTION.NAMING Naming

Decides: How names are chosen so that a reader recovers the concept without the author.
Rows: L1522 (1)
Positions in the evidence: L1522 is the node-level statement: choose names that let a reader recover the concept without the author (no claim of its own; inferred, rolls up three child rows; the origin notes the transfer from experiments on C# and other languages is inference; prior verdict: known). L196 (standard semantic conventions for consistent naming, another branch) is adjacent.
Links: related (no row states the type) `CONSTRUCTION.DESIGN.1` (L329 also states naming).

#### CONSTRUCTION.NAMING.1 Whole Words

Decides: Whole words or abbreviations in identifiers.
Rows: L1523 (1)
Positions in the evidence (no verdict):
- P1 Name identifiers with whole words, not single letters or letter-deleting abbreviations: an experiment with 72 professional C# developers found words gave about 19 percent faster defect finding than letters or abbreviations, with no significant difference between letters and abbreviations (L1523; single source T2 experiment; REG-1518; grounded for the experiment, inferred for other languages). Force: reading speed. Condition: not stated.
- P2 Letters or abbreviations (the alternative the experiment measured; no significant difference between the two).

#### CONSTRUCTION.NAMING.2 One Concept One Name

Decides: How names are composed and kept consistent.
Rows: L1524 (1)
Positions in the evidence (no verdict):
- P1 Give one concept one name, made of common descriptive words and used consistently; do not shorten names by deleting letters (L1524; single source; holder positions of four style or design guides, positions not evidence; transfer from web-platform API design inferred; REG-1519, REG-1510, REG-1520, REG-1521). Related L196.

#### CONSTRUCTION.NAMING.3 Names Derived from Concepts

Decides: How a name is coined.
Rows: L1525 (1)
Positions in the evidence (no verdict):
- P1 Derive a name from the concepts it covers: select the concepts, choose a word per concept, then compose; expect two developers to coin the same name only rarely (median 6.9 percent over 47 instances) while a chosen name is usually understood (L1525; single source T2; REG-1522; the language of the experiments was not checked by the origin).

#### CONSTRUCTION.PARADIGM Paradigm and Placement of Logic

Decides: How the programming paradigm and the place of logic (application, database, scheduler) are chosen by intent.
Rows: none (0)
Positions in the evidence: see children. L312 (MAINT-C48, routed to OWNERSHIP.SELECTION) holds the paradigm half of the maintainer's position (paradigm per part by intent, object-oriented for taxonomies); it is not attached here.

#### CONSTRUCTION.PARADIGM.1 Paradigm by Intent

Decides: Is a paradigm chosen by the problem or by a defect-rate claim.
Rows: L1526 (1)
Positions in the evidence (no verdict):
- P1 Choose the programming paradigm per problem by what the problem is (intent), not by a defect-rate claim: no admitted evidence supports a paradigm mandate (L1526; decision; inferred from the absence of evidence scoped to a paradigm choice inside one language; REG-1523, REG-1524, REG-1509, REG-1525; prior verdict). Same as L312's paradigm half (MAINT position, held in OWNERSHIP.SELECTION).
- P2 Choose an object-oriented or a functional style on defect-rate evidence: Ray et al. 2014 report a modest language effect, functional somewhat better than procedural (restricted); the reproduction finds four of eleven languages significant with exceedingly small effects; the original authors answer that it largely replicated them (T3, not peer-reviewed). The studies compare languages, not paradigms within one language. Rejected in the origin; no condition under which it would be best is stated. Contested fact (STRUCT-C63).
Links: Requires `CONSTRUCTION.HIDING.1` (row-stated: L1526 requires L1514).

#### CONSTRUCTION.PARADIGM.2 Placement of Domain Logic

Decides: Does domain logic live in the application or in the database, what moves that, and where scheduled work runs.
Rows: L1259, L1260, L1261, L311 (4)
Positions in the evidence (no verdict):
- P1 Put domain logic in the application first for modifiability, do not let performance be the first question, profile, and move proven hot spots into SQL, preferably as data-source queries rather than domain logic (L1259; decision; contested; REG-1143, T2, 2003; database-heavy not found at T1 or T2 as an argument for domain logic; round 1 holds consensus that constraints and keys belong in the database). Force: modifiability. Wins when: no measured hot spot.
- P2 Logic in the database (the contrasting side of the same row; the ledger lists L279 MAINT-C15 as possible tension, L311 MAINT-C47 and L312 MAINT-C48 as related; L311 is now attached here as P5, L279 is routed to ASSURANCE and L312 to OWNERSHIP). Condition: not stated by this row.
- P3 Team skill is a legitimate input: if most of the team is less comfortable with SQL, that is a reason to keep domain logic out of SQL (L1260; consensus single source; REG-1143).
- P4 Logic in the application is faster to test in memory behind a replaceable database interface; logic in the database needs a database to test (L1261; consensus single source; REG-1143). Force: testability.
- P5 MAINT position (L311, source MAINT-S01, not citable): run scheduled work where the data lives when it acts on database state (atomicity with the data, one system to run and observe, queryable job history), and record the limits that send work elsewhere: no operating-system commands, CPU-heavy work to the application tier, highly parallel work and streaming to other infrastructure (grounded; REG-181; moved here from `OWNERSHIP.STANCE`; public practice read as contested). (a) External orchestrator: retries, dependencies, backfills, visibility across systems; serves control and scale; wins for multi-system pipelines. (b) In-store scheduler: serves cost of ownership and consistency; wins for small jobs on one store. Contradicts the usual norm of a dedicated orchestrator; no public claim exists to support or contradict it.
Context: team comfort with SQL (L1260: "if most of the team is less comfortable with SQL"); multi-system pipelines against small jobs on one store (L311: "wins for multi-system pipelines", "wins for small jobs on one store").
Note: technology-bound (SQL), not language-bound.
Links: related (no row states the type) `OWNERSHIP.STANCE` (L308).
Stack pointers: L311 (in-database scheduler of one relational engine; stack-tagged pointer).

#### CONSTRUCTION.DATA_NOT_CODE Keeping Data From Becoming Code

Decides: How untrusted data is kept from being interpreted as code, query, path, destination or object.
Rows: L1527, L1528 (2)
Positions in the evidence: L1527 is the origin's roll-up: every sink that interprets data as code, query, path, destination or serialized object is dangerous; secrets are drawn, compared, stored and logged only through audited mechanisms; hostile data is narrowed at each sink and what slips through is contained by a second layer (no claim of its own; inferred; part carved out of a node that stays narrowed; the page, origin, prototype and process parts stay in the JavaScript guideline). L1528 is the node intent: hostile data must not become an instruction or a location for an interpreter (no claim of its own; inferred; prior verdict: known). Adjacent: L340 third-party responses are untrusted input.
Links: Requires `CONSTRUCTION.BOUNDARY.1` (row-stated: L1527 requires L1505); Refines `CONSTRUCTION.BOUNDARY.2` (row-stated: L1528 refines L1506); related (no row states the type) `ASSURANCE.SECURITY`, `TRANSVERSE.SECURITY`.

#### CONSTRUCTION.DATA_NOT_CODE.1 Code and Commands

Decides: Whether and how text becomes code or an operating-system command.
Rows: L1529, L1530 (2)
Positions in the evidence (no verdict):
- P1 Never build code from strings: dynamic evaluation of attacker-influenced text executes it with the caller's privileges, whatever API offers it; template injection is a server-side code-execution class, unlike cross-site scripting (L1529; grounded for the rule, consensus, four T1 sources; the template-injection fact single source T3 and T2; REG-1526, REG-1527, REG-1528, REG-1529, REG-1530, REG-1531; prior verdict: known; the origin keeps the class statement and drops a named case).
- P2 Start a process without a shell and without input-chosen programs so arguments stay arguments: prefer built-in library functions to invoking operating-system commands; when a command is unavoidable, allowlist the executable and the arguments and run it with the least privilege required (L1530; single source T1, principles only; REG-1532; prior verdict: known). Adjacent: L325 least privilege at the lowest layer.
Links: none stated beyond the incoming link from `CONSTRUCTION.DATA_NOT_CODE.4` (L1533 requires L1529).

#### CONSTRUCTION.DATA_NOT_CODE.2 Queries

Decides: How untrusted values reach a query engine.
Rows: L1531 (1)
Positions in the evidence (no verdict):
- P1 A query reaches its engine as fixed text plus separately passed values, in every store, SQL or not: never concatenate or template untrusted values into the query; bind variables carry values only (identifiers, keywords and sort order are redesigned or mapped through a fixed allowlist); run the application's database account with least privilege as a second layer; a store that is not SQL is not immune (L1531; consensus for parameterization, identifiers and non-immunity, single source for least privilege and the rejection of escaping; REG-1533 to REG-1542; prior verdict: known). Force: injection resistance.
- P2 Escaping all user input as the primary defence (rejected in the origin: strongly discouraged, fragile, not guaranteed to stop all injections; single source OWASP; no condition under which it would be best).
- P3 The belief that non-SQL stores are immune (rejected in the origin; consensus).
Links: related (no row states the type) `ASSURANCE.SECURITY` (adjacent: L325).
Note: names SQL but states "in every store"; technology-bound, language-independent.

#### CONSTRUCTION.DATA_NOT_CODE.3 Paths and Destinations

Decides: How a file location or network destination chosen from input is confined.
Rows: L1532, L1534 (2)
Positions in the evidence (no verdict):
- P1 A file location chosen from input stays inside its base directory: build paths from internally generated or trusted names, not user-submitted file names; where user names are unavoidable, apply strict allowlist validation and sanitization (L1532; consensus for the constraint, single source for one clause; grounded for the constraint, open for the clause "checked after resolution and used without a race", which no claim grounds; REG-1536, REG-1543, REG-1529, REG-1544; prior verdict: known).
- P2 A server fetches only destinations it allows, checked at the address it will actually connect to: when the destination is known, match the host against an allowlist and build the request yourself; do not accept complete URLs from users when avoidable; validate the resolved addresses against the permitted networks and connect only to the validated addresses, because a hostname check alone is not enough (L1534; consensus for the allowlist, single source for the URL and DNS points; REG-1550, REG-1535, REG-1536; prior verdict: known). Adjacent: L340 allowlist of redirect targets.

#### CONSTRUCTION.DATA_NOT_CODE.4 Structured Payloads

Decides: How structured data crossing a trust boundary is exchanged and parsed.
Rows: L1533, L1536 (2)
Positions in the evidence (no verdict):
- P1 Data crossing a trust boundary is exchanged in a pure data format, never one that carries types or code, and is never deserialized into executable structures; serialized data is signed and verified before deserializing when the set of expected messages is known; a new object is populated from validated fields; when parsing untrusted XML, document type definitions are disabled (and where required external entity resolution and external DTD loading disabled and entity expansion limited) (L1533; consensus for the format rule and the XML rule, single source for signing and populating a new object; REG-1545, REG-1536, REG-1528, REG-1546, REG-1547, REG-1548, REG-1549; prior verdict: known). Requires L1529 (row-stated, CONSTRUCTION.DATA_NOT_CODE.1).
- P2 Where a proxy and a server read the same bytes, any disagreement between their parsers is an attack and the defence belongs at both parsers; CR, LF or NUL must never reach an HTTP field value: reject the message or replace each with a space (L1536; single source RFC 9110 section 5.5, T1; REG-184; inferred as a carved-out part; protocol-level). See the routing objection on L1536.
Links: Requires `CONSTRUCTION.DATA_NOT_CODE.1` (row-stated).

#### CONSTRUCTION.PROCESS Process Lifecycle

Decides: How a process starts, stops, fails and holds state so that it can be replaced and scaled.
Rows: none (0)
Positions in the evidence: see children.
Links: related (no row states the type) `CHANGE_FLOW.DEPLOY`, `OPERATION.CAPACITY`.

#### CONSTRUCTION.PROCESS.1 Fast Start and Graceful Stop

Decides: How quickly a process starts and how it ends on request.
Rows: L1202 (1)
Positions in the evidence (no verdict):
- P1 Processes start in seconds and shut down gracefully on SIGTERM (stop accepting requests, finish in-flight work, return jobs to the queue) so releases and scaling are cheap (L1202; consensus; REG-1109). Force: cheap release and scaling. No competing position recorded.
Note: names an operating-system signal; hosted-service scope (MD-05), language-independent.

#### CONSTRUCTION.PROCESS.2 Fail Fast Under Supervision

Decides: What a process does after a failure it cannot repair.
Rows: L1510 (1)
Positions in the evidence (no verdict):
- P1 After a failure the program cannot repair, its state is undefined: it records the failure, releases what it owns and ends, and restarting is the job of something outside it (L1510; single source, one T1 page; grounded by the origin's merged rule row; REG-1507; prior verdict: known; the origin names Node hooks, dropped here).
No competing position recorded.

#### CONSTRUCTION.PROCESS.3 Stateless Processes

Decides: Where a process keeps state.
Rows: L1203 (1)
Positions in the evidence (no verdict):
- P1 Processes are stateless and share nothing; no sticky sessions; session and durable state live in external stores (L1203; consensus; REG-1109; origin boundary APP). Force: replaceability, scaling. No competing position recorded.
Links: related (no row states the type) `CONSTRUCTION.STATE.3`.

## Routing objections

Five were raised; each is resolved in `../../objections/resolution.md`. Moved (row now sits on the target branch, no longer listed): L1535 to `TRANSVERSE.CONFIG` (node `CONSTRUCTION.DATA_NOT_CODE.5` removed, it held only that row), L1286 to `ASSURANCE.DATA_INTEGRITY`. Kept (listed, with the reason): the three rows below. 3 objections.

| row | routed to | would route to | reason | resolution |
|---|---|---|---|---|
| L1536 | CONSTRUCTION.DATA_NOT_CODE | TRANSVERSE.SECURITY | Parser disagreement between a proxy and a server and control characters in an HTTP field are request-smuggling defences at a protocol, not data interpreted as code; no other construction node fits. | kept: a control character reaching a header value is data turned into protocol structure (injection), which is this node's subject; no TRANSVERSE.SECURITY node (programme practice) or ASSURANCE node holds a parsing rule |
| L1265 | CONSTRUCTION.STATE | ASSURANCE.DATA_INTEGRITY | The row's second half, the application must guard deliberate redundancy, is the derived-data synchronisation that node holds as its index of which-mechanism rows. | kept: the lead clause is the normal-form decision (when to leave it), beside L1263 and L1264; the guard clause is already stated by L281 in DATA_INTEGRITY, so moving the row would add nothing there |
| L1235 | CONSTRUCTION.DESIGN | EVOLUTION.INCREMENTAL | "Plan to rewrite before 100x", sacrificial parts replaced by their builders, is replacement over time; L1235 lists L039 (incremental replacement) as related. | kept: the lead clause sizes the design (10x growth) and DESIGN.4 is cut for it, with replacement named in its intent; EVOLUTION.INCREMENTAL.3 holds the rewrite-or-replace positions and is reached by the DESIGN.4 link |

## Language-neutrality flags

The maintainer's ruling (`../../inputs_from_javascript_guideline.md`): code design belongs here as long as it is true for all languages. Rows whose statement, as written in the ledger, does not hold for every language. 4 rows, all resolved in `../../objections/resolution.md`: three carry a language-neutral statement taken from the row's own evidence (recorded in the node's positions, ledger untouched); one is marked a stack pointer.

| row | node | why the statement is not language-neutral | resolution |
|---|---|---|---|
| L1501 | CONSTRUCTION.STATE.4 | Scoped by its own text to languages with binary floating point; true only where such a type exists. | neutral statement recorded (REG-1501, Goldberg 1991) |
| L1518 | CONSTRUCTION.STATE.5 | Scoped by its own text to languages that run module code at load time. | stack pointer (sources REG-1514 to REG-1516 are all one language's module system and a bundler) |
| L1514 | CONSTRUCTION.HIDING.1 | Distinguishes abstract data types from objects; presumes a language offering both constructs. | neutral statement recorded (REG-1509, Cook) |
| L1288 | CONSTRUCTION.BOUNDARY.3 | The statement names Postgres, Python and TypeScript; the ledger kept the origin wording. | neutral statement recorded (REG-1153, logical against physical type) |

Technology-bound but not language-bound, not counted above (true in every language that uses the technology): L1202 (operating-system signal), L1259 to L1261 (SQL), L1263 to L1267 (relational storage), L1269 and L1279 (schema formats), L1275 (NOT NULL, CHECK), L1285 (database as contract), L1287 (data-engineering contract format; data pipelines are deferred by MD-05), L1531 (SQL and other stores), L1533 (XML), L1534 (URLs), L1536 (HTTP). Rows whose evidence is one language while the statement is general: L1523 (C# experiment; statement kept general, transfer inferred), L1524 and L1525 (holder positions and experiments of unchecked language).
