# J5_construction: judge records

Unit: the realization branch CONSTRUCTION: the L1 node, its ten L2 nodes (DESIGN, SYSTEM_SHAPE, HIDING, BOUNDARY, STATE, DEPENDENCY_DIRECTION, NAMING, PARADIGM, DATA_NOT_CODE, PROCESS) and their 37 L3 nodes: 48 records, tree order. Rows by ledger id (L001-L460, L1001-L1289, L1501-L1565), sources by register id (REG-nnn). The maintainer's codified practice is source MAINT-S01 (REG-181, not citable): a strong position, never an automatic winner; a decision resting only on it is marked inferred. Binding: MD-01 (the best, not the average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-05 (code design in scope when true for every language).

Decided inputs read (settled, never re-decided): ASSURANCE.CONTRACTS.1 to .3 (J2), ASSURANCE.RULES.3 (J2), ASSURANCE.DATA_INTEGRITY.1, .4 (J3), ASSURANCE.SECURITY.2, .6 (J3). Cross-unit fixes read: X1 to X3 (none touches a CONSTRUCTION node); X7, X9 and X12 applied in the final pass. Judged OWNERSHIP.STANCE.4 (J1) read for consistency of DESIGN.2 and DESIGN.4 only.

Reading note. Where a node holds several independent rows, the Decision is a lead of one to three sentences followed by sub-decisions per row, each one sentence; the lead is the node's claim, the sub-decisions are the graph build's leaf constraints. Language-neutrality: no language mechanism is stated; where the evidence is one language's, the decision is stated as a principle with its scope condition.

Pinned:
- Nodes judged: 48 (CONSTRUCTION; DESIGN, .1 to .4; SYSTEM_SHAPE, .1 to .4; HIDING, .1 to .4; BOUNDARY, .1 to .6; STATE, .1 to .5; DEPENDENCY_DIRECTION, .1, .2; NAMING, .1 to .3; PARADIGM, .1, .2; DATA_NOT_CODE, .1 to .4; PROCESS, .1 to .3). The L1 record is a provisional index; wave 3 re-rolls it.
- Decisions marked undecided: none.
- Flags raised: 9 (F1 to F9); all settled (F6, F8 by review; the other seven by the final pass); none open.
- Review fixes applied: 16 of 16 (section Review applied).
- Settled decisions disagreed with: none. Two seams checked and found consistent: CONTRACTS.1 (coordinated breaking change under few reachable in-house consumers) against SYSTEM_SHAPE.3; CONTRACTS.3 (the chain of types starts where the team records it) against BOUNDARY.3 (types derived from the contract).

---

## CONSTRUCTION Construction

Intent (sharpened): how code is structured, in its language-neutral form, so that it is correct and stays changeable; carries out what OWNERSHIP and ASSURANCE decide and re-decides none of it.

1. **Decision.** Provisional index; the claim is re-rolled in wave 3 from the ten L2 nodes. Working claim: design is derived from usage before code and effort goes where error is costly; the system starts as the simplest shape that serves and is cut by hidden decision and business concept; what crosses a trust boundary is parsed once into a precise form and never reaches an interpreter as code; each fact has one place, dependencies flow one way, names carry concepts; logic is placed by the property it must have (hold across writers, change with the product, be fast to test, act on data in place); a process can be stopped and replaced at any time. Outcome: the code is correct at its boundaries and a change touches few places.
2. **Grounds.** Roll-up of the ten L2 nodes (87 rows).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Inferred (roll-up).
7. **Flags.** none of its own.

Links: Realizes ASSURANCE.CONTRACTS (via BOUNDARY), ASSURANCE.DATA_INTEGRITY.1 (via BOUNDARY.1, .4, PARADIGM.2), ASSURANCE.RULES.3 (via DEPENDENCY_DIRECTION.2); related ASSURANCE.SECURITY, TRANSVERSE.SECURITY, TRANSVERSE.CONFIG.

---

## CONSTRUCTION.DESIGN Design Derivation

Intent (sharpened): how design is derived before code and where design effort and timing go.

1. **Decision.** Design is derived from what the system must do down to code, in order of the cost of reversing each decision (DESIGN.1); effort concentrates on the decisions costly to get wrong and takes them no earlier than the product is understood (DESIGN.2); the required properties lead and the structural constraints that induce them are tested against every change (DESIGN.3); the design is sized for a stated growth horizon and kept replaceable part by part (DESIGN.4). Outcome: the design was good before the code existed, and costly decisions were not taken blind.
2. **Grounds.** Roll-up of DESIGN.1 to .4 (5 rows).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none beyond the children.
6. **Certainty.** Inferred (roll-up; children mostly single-source or maintainer).
7. **Flags.** none.

Links: children DESIGN.1 to .4; OWNERSHIP.STANCE.4 (speculative building, J1); EVOLUTION.INCREMENTAL.

### CONSTRUCTION.DESIGN.1 Derivation Order

Intent (sharpened): in what order a design is derived before code is written.

1. **Decision.** Derive the design from the outside in and from the costly to the cheap to reverse: the usage and scenarios the system must serve, the data flow they imply, the structure of the stored data, the shape of the system, the implementation strategy (why and how, stated abstractly), and only then the code. Test-first or emergent design is a legitimate way to fill in the parts that are cheap to reverse once that frame exists (a test encodes a usage scenario; the ordering of tests and code is decided in ASSURANCE.BEHAVIOUR.5), and a throwaway probe is legitimate to learn usage before it is understood, never as the keeper. The order is the order in which the decisions depend on each other; when each is taken is governed by DESIGN.2 (no earlier than the product is understood) and SYSTEM_SHAPE.3. Outcome: what is costly to change was decided against real usage, not discovered in code.
2. **Grounds.** Design first serves correctness and reversibility (L329; MAINT-S01, REG-181, public practice read as majority, differs from test-first or emergent). The ordering is not arbitrary: each step fixes what the next must obey, and the cost of reversal grows from the code (cheap) through the stored-data structure and the system shape (costly). Ordering of tests against code is decided in ASSURANCE.BEHAVIOUR (F4 there: by context).
3. **Positions.** P1 maintainer: derive in the stated order, strategy before tactics (correctness, reversibility). P2 test-first or emergent design (speed of feedback).
4. **Rejected.** P2 as the way to derive the costly-to-reverse structure: feedback arrives after the data and the boundaries exist; best for parts cheap to change (internal logic, small modules), and for exploration when usage is unknown. P1 as a fixed sequence for everything: unnecessary ceremony where reversal is cheap.
5. **Context.** Cost of reversal per part: costly (stored data structure, boundaries) follows the order; cheap (internal logic) may emerge.
6. **Certainty.** Inferred: the order rests on one maintainer row (grounded as the maintainer's practice) and the reversal-cost argument; no source measures it.
7. **Flags.** none. The naming half of L329 is decided in NAMING.3 (MD-03).

Constraints: MUST decide the data structure and the system boundaries against stated usage before the code that depends on them is kept. Links: related NAMING, OWNERSHIP.STANCE.4.

### CONSTRUCTION.DESIGN.2 Effort and Timing on Costly Decisions

Intent (sharpened): where design effort is spent and when hard-to-reverse decisions are taken.

1. **Decision.** Architecture is the shared understanding of the important decisions, those costly to get wrong, and design effort is spent there. A hard-to-reverse decision is taken as late as the product's understanding allows and no later than the point where deferring it costs more than deciding; when it cannot wait (stored data already in use), the probable use is weighed in it without speculative optimisation. Outcome: effort and certainty are spent where an error would be expensive, and the cheap decisions stay cheap.
2. **Grounds.** Effort at the costly decisions (L1206; REG-1121); deferral until understood, no distributed boundaries up front (L1209; REG-1112); the structure for probable use where reversal is costly (L330, MAINT, held and decided in OWNERSHIP.STANCE.4, J1: consistent).
3. **Positions.** P1 effort at costly decisions (cost of error). P2 defer the hard to reverse (reversibility). They answer two questions, how much effort and when, and do not compete.
4. **Rejected.** Deciding early to remove uncertainty: best when the decision cannot be deferred (a shared interface already published) or when a platform imposes it. Deferring everything: best never; some decisions block the work that produces the understanding.
5. **Context.** none.
6. **Certainty.** Grounded (two consensus principle rows); inferred for "no later than deferral costs more".
7. **Flags.** none.

Constraints: MUST record a hard-to-reverse decision with its reason. Links: related OWNERSHIP.STANCE.4, SYSTEM_SHAPE.3.

### CONSTRUCTION.DESIGN.3 Properties First, Then Constraints

Intent (sharpened): design starts from the required properties and tests every change against the constraints that induce them.

1. **Decision.** Choose the system's required properties first (stated so they can be checked), then adopt the set of architectural constraints that induces them, and test each proposed change against those constraints; where a constraint can be checked mechanically it is a blocking check (ASSURANCE.RULES.3). Outcome: the structure fits the properties the system must have, and a change cannot erode it unnoticed.
2. **Grounds.** L1226 (consensus; REG-1124, REG-1125; origin wording HTTP-framed, the principle is neutral); mechanical enforcement of boundaries and fitness properties is settled in ASSURANCE.RULES.3.
3. **Positions.** P1 properties, then constraints, then test changes against them (fit between structure and properties). No competing position recorded.
4. **Rejected.** Constraints chosen by habit or fashion without a property they serve: best never.
5. **Context.** none.
6. **Certainty.** Grounded (consensus, two register sources); the single-source origin is one body of design writing, so strength is moderate.
7. **Flags.** none.

Constraints: MUST name the property a constraint serves. Links: Requires ASSURANCE.RULES.3; related DEPENDENCY_DIRECTION.2.

### CONSTRUCTION.DESIGN.4 Growth Horizon

Intent (sharpened): for what scale a design is made and how replacement is planned.

1. **Decision.** Size the structures that are costly to reverse (stored data layout, partitioning, system shape, published interfaces) for a stated growth horizon (a common heuristic: about 10x the present need) and write the horizon and the measured signal that will end it down; parts cheap to change are sized to the present need (OWNERSHIP.STANCE.4). Keep parts replaceable behind their boundaries so replacement, when the signal comes, is part by part (EVOLUTION.INCREMENTAL decides rewrite against replacement); a part may be knowingly sacrificial if it is kept modular. Outcome: no over-design now, and no surprise when the horizon is reached.
2. **Grounds.** L1235 (majority; REG-1118: roughly 10x, rewrite before 100x, sacrificial parts); incremental replacement behind the existing interface (L039; REG-033, EVOLUTION.INCREMENTAL).
3. **Positions.** P1 design for 10x, plan the rewrite before 100x (avoid over-design). P2 replace incrementally, not wholesale (reversibility, delivery speed).
4. **Rejected.** A wholesale rewrite as the plan: best when behaviour is well specified, the old system is small, or the architecture itself is the obstacle (EVOLUTION.INCREMENTAL holds the condition). Designing for the final scale now: best when the final scale is already contracted or the structure cannot change later (stored data at very large size, L330).
5. **Context.** none.
6. **Certainty.** Inferred: one source for the figures (REG-1118) and they are an example of the principle (an order of magnitude), not a measured threshold.
7. **Flags.** none.

Constraints: MUST state the horizon and the signal for each structure costly to reverse. Links: related EVOLUTION.INCREMENTAL, OWNERSHIP.STANCE.4, OPERATION.CAPACITY.

---

## CONSTRUCTION.SYSTEM_SHAPE System Shape

Intent (sharpened): how the system is divided into deployable units and how that follows domain and teams.

1. **Decision.** Start as one deployable unit with module boundaries inside (SHAPE.1), pay the distribution premium knowingly and consolidate again when its cost outgrows its benefit (SHAPE.2), place unit boundaries only after the domain is understood and make them deployable independently (SHAPE.3), and design team and module structure together (SHAPE.4). Outcome: the system is no more distributed than its forces require and a boundary, once drawn, is cheap to live with.
2. **Grounds.** Roll-up of SHAPE.1 to .4 (10 rows).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** Team count and independence of release moves SHAPE.1 and .3.
6. **Certainty.** Inferred (roll-up; the sources are practitioner essays, no controlled evidence).
7. **Flags.** none of its own.

Links: children; Realizes in code the unit boundaries that ASSURANCE.CONTRACTS.1 and .2 verify; OPERATION.RELIABILITY.

### CONSTRUCTION.SYSTEM_SHAPE.1 Initial Shape, One Unit or Several

Intent (sharpened): whether a new hosted service starts as one deployable unit or several.

1. **Decision.** A new service starts as one deployable unit with module boundaries inside (HIDING.2), and a unit is split out only when a named force requires it: independent scaling, independent release by separate teams, fault isolation that matters, or a different runtime need. Outcome: complexity of distribution is paid only for a measured benefit.
2. **Grounds.** One unit first (L1210; majority; REG-1016, REG-1112, REG-1113, REG-1116, REG-1122); no services unless too complex to manage as one (L1211; REG-1113); avoid distributing computation, remote calls cost more and move complexity into the connections (L1214; REG-1016, REG-1116); the small-team "one head" criterion (L1218; REG-1112, REG-1116) is one practitioner's and is not adopted as a test: Fowler agrees on direction only.
3. **Positions.** P1 one unit first (simplicity, cost). P2 not services unless forced (same direction, trigger stated). P3 services from the start (fault isolation, independent scaling; evidence sparse, large organisations report success). P4 avoid distribution. P5 small team integrates.
4. **Rejected.** P3 as the default: pays the distribution premium before any force exists; best when the domain boundaries are already known (rebuilding an existing system), the team already has reasonable experience of building a system of services (REG-1112), and, inferred, several teams must release independently from the first day and the supporting platform (deployment automation, monitoring) already exists. Copying large-organisation patterns in a small team: best never as a reason.
5. **Context.** Team count and independence, and system complexity (L1218, L1211): the split triggers above are the conditions that move the answer.
6. **Certainty.** Grounded for the direction (majority, several practitioner sources, T3 case studies, no controlled evidence); inferred for the list of split triggers and for the services-first condition.
7. **Flags.** none.

Constraints: MUST state the force that justifies a split. Links: related SHAPE.3, SHAPE.2; HIDING.2.

### CONSTRUCTION.SYSTEM_SHAPE.2 Distribution Premium and Its Reversal

Intent (sharpened): what must be budgeted before adopting services and when consolidating is legitimate.

1. **Decision.** Before a unit is split off the distribution premium is budgeted and in place: automated deployment, monitoring, failure handling, and a stated answer to eventual consistency. The shape is not a one-way door: when operating cost grows with the number of units faster than the benefit, units are consolidated, accepting less fault isolation. Outcome: a split is never taken on without the means to run it, and a bad split can be undone.
2. **Grounds.** Budget the premium (L1212; consensus; REG-1016, REG-1113); consolidation legitimate when cost grows with unit count (L1219; majority; one case study, REG-1122).
3. **Positions.** P1 budget the premium (cost of operation). P2 consolidate back (cost of operation; loses fault isolation).
4. **Rejected.** Splitting now and building the premium later: best never, the failure modes arrive first. Never consolidating: best only where fault isolation or independent scaling is worth more than the operating cost.
5. **Context.** Number of units against operating cost.
6. **Certainty.** Grounded for the premium (consensus); inferred for the consolidation rule (one T3 case, no T2 source states it as a rule; it follows from the symmetric argument that a cost is reversible).
7. **Flags.** none.

Constraints: MUST have deployment automation, monitoring and failure handling before a split goes live. Links: related OPERATION.RELIABILITY, CHANGE_FLOW.DEPLOY.

### CONSTRUCTION.SYSTEM_SHAPE.3 Placing Service Boundaries

Intent (sharpened): when a unit boundary is placed and what it must guarantee.

1. **Decision.** A boundary between deployable units is placed only once the domain is understood, because moving functionality across one is far costlier than within one. Units across a boundary are designed to deploy independently, without orchestrated lock-step upgrades (compatibility defined and verified as ASSURANCE.CONTRACTS.1 and .2 decide). Where two units can only ever change and deploy together, that is a boundary in the wrong place: they are merged or the boundary is moved; coordinated breaking changes deployed together stay legitimate only for the case ASSURANCE.CONTRACTS.1 states (few, in-house, reachable consumers) and are the exception, not the operating mode. Outcome: a boundary buys independent change instead of hiding a coupled system behind a network.
2. **Grounds.** Boundaries after understanding (L1213; consensus; REG-1016, REG-1112); independent deployability among the strongest predictors of continuous delivery (L171; consensus; REG-092, REG-097); the maintainer's additive-plus-coordination practice (L295; REG-181) wins with few reachable consumers and is already placed by the settled CONTRACTS.1, which this decision follows.
3. **Positions.** P1 boundaries after the domain is understood (reversibility). P2 independently deployable units (delivery speed). P3 additive evolution plus coordinated breaking change deployed together (cost of ownership; contradicts P2 when consumers release independently).
4. **Rejected.** P3 as the general rule: impossible when consumers release independently or are external; best, and kept, for few in-house reachable consumers. P2 as an absolute: costly where the units are one team's and release together, in which case the boundary itself is the question.
5. **Context.** Number and reach of consumers (settled in CONTRACTS.1).
6. **Certainty.** Grounded for P1 and P2 (consensus; REG-092, REG-097 are delivery-research sources for loose coupling); inferred for "lock-step is a signal of a misplaced boundary" (follows from P2 and P3, no row states it).
7. **Flags.** none. Settled in the final pass: independent deployability is the purpose of a boundary (L171, consensus); the coordinated breaking change of CONTRACTS.1 stays legitimate as an exception.

Constraints: MUST NOT place a unit boundary before the domain is understood without recording why. Links: Realizes ASSURANCE.CONTRACTS.1, .2; related SHAPE.1, OWNERSHIP.SERVICES.2.

### CONSTRUCTION.SYSTEM_SHAPE.4 Teams and Structure

Intent (sharpened): how team organisation and system structure relate.

1. **Decision.** Team boundaries and module boundaries are designed together, because structure follows the communication structure that exists. A team is organised around a capability with the skills to deliver it end to end, not around a technical layer; individuals need not be generalists. Outcome: a typical change completes inside one team's boundary and one module's boundary.
2. **Grounds.** Not by layer, teams cross-functional around a capability (L1221; consensus; REG-1016, REG-1115); structure copies communication structure, design both together (L1222; consensus; REG-1016, REG-1127).
3. **Positions.** P1 capability teams (delivery flow). P2 structure follows communication (design both together). No competing position recorded.
4. **Rejected.** Layer teams: best only where a layer is a scarce specialism shared by all capabilities and handoffs are cheap (inferred; no row states it).
5. **Context.** A single team: the principle applies to its module boundaries only.
6. **Certainty.** Grounded as consensus of practitioner and design writing (REG-1016 is one essay collection, so independent support is thin); inferred for the single-team reading.
7. **Flags.** none.

Constraints: none beyond the decision. Links: related HIDING.2, SYSTEM_SHAPE.1.

---

## CONSTRUCTION.HIDING Information Hiding and Modularity

Intent (sharpened): how code is cut into modules so each difficult or changing decision lives behind one boundary.

1. **Decision.** Modules are cut by the decision each hides (HIDING.1), along business concepts first with layer separation inside a module (HIDING.2, .3), and a stored schema has one owner (HIDING.4). Outcome: a change to one decision touches one module.
2. **Grounds.** Roll-up of HIDING.1 to .4 (10 rows) and L1511 (an origin roll-up with no claim of its own, its parts spread over HIDING, STATE, DEPENDENCY_DIRECTION, NAMING, PARADIGM).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Inferred (roll-up).
7. **Flags.** none of its own.

Links: children; related STATE, DEPENDENCY_DIRECTION, NAMING, PARADIGM.

### CONSTRUCTION.HIDING.1 Cut by Hidden Decision

Intent (sharpened): by what modules are cut and how much of a module is exposed.

1. **Decision.** Put each difficult or likely-to-change decision behind one module boundary and expose from each module only what others need, at every level at which something can be exposed. A design states, for each interface, whether it hides a representation behind operations (an abstract type) or varies its implementation per instance behind a common set of operations (procedural abstraction), and an API does not conflate the two. Outcome: a change to a hidden decision stays inside its module.
2. **Grounds.** Decompose by hidden decisions, not processing steps (L1512, L1513; single source Parnas, T2, principle without effect evidence; REG-1508); expose only what others need at every level (L1515; REG-1508, REG-1510, REG-1511, REG-1512, inferred cross-level rule); the two hiding styles (L1514; REG-1509 Cook, T2, distinction without effect evidence). The grounds are one principle with long-standing practitioner acceptance and no measurement of effect.
3. **Positions.** P1 hide decisions (changeability). P2 cut by processing steps. P3 expose only what is needed. P4 know which hiding style an interface offers.
4. **Rejected.** P2 as the cut: the steps are the part most likely to change; best where the steps themselves are the stable concept (a fixed pipeline of transformations; inferred). Choosing one hiding style for all interfaces: no evidence for either (open); the requirement is to state which, not to prefer one.
5. **Context.** none.
6. **Certainty.** Grounded as principle (single source, T2, no effect evidence); inferred for the cross-level extension and for P4's use in API design.
7. **Flags.** none.

Constraints: MUST expose only what consumers need; MUST NOT cut a module by processing step where the step is the likely-to-change decision. Links: Required by PARADIGM.1; related OWNERSHIP.CONTAINMENT.

### CONSTRUCTION.HIDING.2 Cut by Business Concept or by Layer

Intent (sharpened): along which axis a modular system is divided and how large domains are split.

1. **Decision.** The primary cut is by business concept (orders, billing), each module with a public interface, with the layer separation of HIDING.3 inside the module; the two axes do not compete once the primary one is chosen. A large domain is not forced under one unified model: it is split into bounded contexts with explicit mappings between them. Outcome: a change to a business capability touches one module, not every layer.
2. **Grounds.** Modular by business concept (L1215; majority; Shopify T3 the only practitioner case, Fowler states the goal without the cut; REG-1016, REG-1117), supported by the changeability force: changes cluster by business concept; bounded contexts (L1217; consensus; REG-1123).
3. **Positions.** P1 by business concept (changeability). P2 by technical layer (L1220). P3 several bounded contexts, not one model.
4. **Rejected.** P2 as the primary axis: a feature change then crosses every layer; best as the primary axis when changes cluster by technology (replacing a whole presentation technology) or for a system with one business capability (inferred). One unified model for a large domain: best for a small domain with one meaning per term.
5. **Context.** none.
6. **Certainty.** Inferred: one practitioner case (T3) and a consensus statement; the argument (changes cluster by concept) is stated by the rows' own reasoning, not measured.
7. **Flags.** none.

Constraints: MUST give each business-concept module a public interface. Links: related HIDING.3, SYSTEM_SHAPE.1, SYSTEM_SHAPE.4.

### CONSTRUCTION.HIDING.3 Separating Presentation, Domain and Data Access

Intent (sharpened): whether domain logic is kept apart from presentation and data access and how loosely layers couple.

1. **Decision.** Domain logic is kept free of presentation and storage entanglement, so it can be driven by users, tests, batch jobs or other programs and exercised without the real presentation or store behind a replaceable interface; layers couple loosely through narrow interfaces, and each concept or datum lives in one place (STATE.1). Where a part has no domain logic (a thin pass-through of data), no separate domain layer is built. Outcome: one domain serves several presentations and its rules are testable in isolation.
2. **Grounds.** Separate the three, narrows the scope of attention, several presentations, test seams (L1220; consensus; REG-1115); logic free of UI and database so any driver can run it (L1223; REG-039, REG-1115); loosely coupled layers, each thing once (L1224; REG-1131). Where domain logic is placed in the data tier (PARADIGM.2) the isolation is of the interface, and the data tier is tested against a real store.
3. **Positions.** P1 separate the three (testability, changeability). P2 logic free of UI and store. P3 loose coupling, one place. P4 modularise by concept (competing axis, resolved in HIDING.2).
4. **Rejected.** A mandatory layer for every system: best never; for a thin data pass-through it only adds indirection (inferred). Presentation and domain in one place: best for a throwaway or single-presentation script whose rules will never be reused.
5. **Context.** Presence of domain logic (none: no layer needed).
6. **Certainty.** Grounded (consensus, T2 design sources; one origin family for the three rows); inferred for the thin pass-through exception.
7. **Flags.** none.

Constraints: MUST NOT let domain logic depend on presentation or storage details. Links: related HIDING.2, STATE.1, DEPENDENCY_DIRECTION.2, PARADIGM.2.

### CONSTRUCTION.HIDING.4 Data Ownership by One Application

Intent (sharpened): who owns a stored schema and whether a shared store is an integration mechanism.

1. **Decision.** Each schema has one owner who alone changes it; other parties reach the data through an interface the owner publishes, never by binding to the base structures. A store shared by several applications through its base structures is not used as an integration mechanism, because every change then needs every consumer; direct data access by several consumers goes through a published interface layer (BOUNDARY.4). Outcome: the owner can change internals without coordinating with unknown consumers.
2. **Grounds.** L1225 (consensus; REG-1133: one application owns its schema; avoid the shared database as integration); the near claim L1285 (contested, kept apart) is the published-interface route, decided in BOUNDARY.4.
3. **Positions.** P1 one owner, no shared integration database (freedom to change the schema). P2 shared access through a dedicated contract layer (BOUNDARY.4).
4. **Rejected.** A shared store bound through base structures: best only for a short-lived transition or a single consumer maintained by the same people, with the structure documented as a contract (inferred; no row states it).
5. **Context.** none.
6. **Certainty.** Grounded (consensus, one register source family).
7. **Flags.** none.

Constraints: MUST name one owner per schema. Links: related BOUNDARY.4; ASSURANCE.DATA_INTEGRITY.1.

---

## CONSTRUCTION.BOUNDARY Boundary Contracts and Call Shape

Intent (sharpened): what a boundary states and how a call is shaped, so that a violated expectation is reported where it arises.

1. **Decision.** What crosses a trust boundary is parsed once into a precise form (BOUNDARY.1) under a positive definition of valid (.2); a boundary is written as an explicit contract readable without the producer's code (.3), the stored data is exposed to several consumers only through a published interface (.4), a call is shaped so it carries meaning and can change (.5), and a failure is explicit and diagnosable (.6). Outcome: code past a boundary may rely on what it receives, and an interface can change without breaking its consumers.
2. **Grounds.** Roll-up of BOUNDARY.1 to .6 (23 rows) and L1503 (the origin's roll-up with no claim of its own).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** Consumer reach moves BOUNDARY.3 and .4 (as in ASSURANCE.CONTRACTS.1).
6. **Certainty.** Grounded for the parse-at-the-edge core (consensus, two T1 sources); inferred for the shape and call rules.
7. **Flags.** none.

Links: Realizes ASSURANCE.CONTRACTS (this node holds the form a boundary takes; that node holds how compatibility is verified, MD-03) and ASSURANCE.DATA_INTEGRITY.1 (edge validation).

### CONSTRUCTION.BOUNDARY.1 Parse or Validate at the Edge

Intent (sharpened): in what form what crosses a trust boundary is checked, where, and how strictly typed.

1. **Decision.** Every datum that crosses a trust boundary, including data from internal services, queues, stored records and third-party responses, is converted once at the boundary into the most precise representation the code needs, rejecting what does not fit, before any of it is acted on; code past the boundary relies on that representation and does not re-check its structure (narrowing at each sink stays under DATA_NOT_CODE), and a check done by the untrusted party does not count as the boundary. Coercion is decided explicitly per boundary: strict by default, coercing only where the source cannot produce the type (a form or query string), done in one place. Outcome: partly processed invalid data cannot get past the edge.
2. **Grounds.** Parse, do not validate: scattered re-checking lets partly processed data through (L1274; consensus, single source; REG-1151); validate all trust-boundary data including internal sources (L1505; two T1 sources; REG-1503, REG-1504); the parse is the same act as the validation, so L1274 and L1505 do not differ in outcome: validation is the rejecting half of parsing; precise structure carried by types at the boundary and by store constraints (L1275; REG-1139, REG-1151; the store half is settled in DATA_INTEGRITY.1); coercion per boundary (L1280; REG-1155); the intent row L1504 (inferred).
3. **Positions.** P1 parse once at the edge (correctness past the edge). P2 parse every datum into the expected shape. P3 validate all boundary data before use. P4 most precise structure, illegal states unrepresentable. P5 decide coercion per boundary.
4. **Rejected.** Validation scattered through the code: best never as the defence (it is still needed for rules that depend on current state, which are domain rules, not boundary checks). Trusting internal sources without checking: best only where the producer and the consumer are one release and one owner (inferred; REG-1503 states internal sources are checked). Always coercing: best where the source cannot produce the type; always strict: best for a machine API.
5. **Context.** Strict against coercing parsing by boundary kind (L1280).
6. **Certainty.** Grounded (consensus; two T1 sources for P3); grounded for "the untrusted party's check is not the boundary" (REG-1503: client-side validation is bypassable; the architecture half of L1505 stays deferred to the sibling web-architecture guideline and is not judged here).
7. **Flags.** none.

Constraints: MUST parse at every trust boundary before use; MUST NOT rely on a check performed by the party being checked. Links: Realizes ASSURANCE.DATA_INTEGRITY.1 (edge validation, in addition to store constraints); related BOUNDARY.2, STATE.1, OWNERSHIP.CONTAINMENT.2 and .4.

### CONSTRUCTION.BOUNDARY.2 What Counts as Valid

Intent (sharpened): how validity is defined for an input.

1. **Decision.** Valid is defined by a positive rule (an allowlist of values, a pattern, a range, a comparison with an expected structure) and everything else is rejected; validity covers syntax and meaning, including combinations of related fields. Input languages are kept simple enough to be recognised completely before anything is computed from them; for a complex input language a real parser is used, not a hand-written list of allowed or denied patterns. A credential or token is valid only if every cryptographic and validation step its specification requires passes; otherwise it is rejected whole, never trusted in part. Outcome: what is accepted is exactly what was specified, nothing by omission.
2. **Grounds.** Allowlist (L1506; consensus, two T1; REG-1503, REG-1504); syntax and semantics (L1507; REG-1503, REG-1504); input handling as a recogniser (L1508; single T2 source, authors' position, no effect evidence; REG-1505); token acceptance (second half of L1535; REG-166, REG-1551, REG-1552, REG-1553; moved here from TRANSVERSE.CONFIG.1 by cross-unit fix X9, grounded as judged in J9; CONFIG.1 keeps a see-link).
3. **Positions.** P1 positive rule, reject the rest. P2 syntax and semantics. P3 simple input languages, real parsers. P4 a token accepted whole or not at all.
4. **Rejected.** Denylisting bad input: best never as the sole rule (it can add a second layer after an allowlist where the allowlist cannot be complete). Hand-written pattern lists for complex languages: unreliable, best never.
5. **Context.** none.
6. **Certainty.** Grounded for P1 and P2; P3 grounded as one source's position; P4 grounded (as judged in J9).
7. **Flags.** none.

Constraints: MUST define valid positively; MUST reject a credential or token whole unless every cryptographic and validation step its specification requires passes. Links: refined by DATA_NOT_CODE (L1528 refines L1506); related BOUNDARY.1.

### CONSTRUCTION.BOUNDARY.3 What a Contract States

Intent (sharpened): what a written contract at a boundary states and carries.

1. **Decision.** A data contract is an explicit artifact, readable without the producer's source, stating structure and meaning: names, types, nullability, units, invariants, an owner, and the version or change-log form that ASSURANCE.CONTRACTS.1 decides for the consumer reach. A schema alone is not enough: units, time zone, precision and rounding are written in the contract or enforced by constraints, and "may be null" is declared separately from "may be absent". Types are stated logically in the contract, and the store's, server's and client's types are derived from the one place where the team records that the chain of types starts (ASSURANCE.CONTRACTS.3), never hand-copied; every contract has one owner, one authoritative provider description and a lifecycle status (proposed, active, deprecated, retired). For one application database, take the data-engineering contract format as a checklist (owner, meaning, quality rules, freshness or availability promise, lifecycle) and adopt the full format only when data leaves the application for a platform team. Outcome: a consumer knows what it may rely on and what to ask the owner.
2. **Grounds.** Explicit artifact (L1268; consensus; REG-1149, REG-1153); schema not sufficient, units and precision (L1269; REG-1148, REG-1154); null against absent (L1270; REG-1147, REG-1154); logical type, derive physical (L1288; REG-1153; separation grounded, derivation inferred); owner, version, lifecycle (L1289; REG-1152, REG-1153); data-engineering format as a checklist (L1287; open, REG-1153). The version rule is held in the settled CONTRACTS.1 (over L295, MAINT-C31) and is not restated; the chain-of-types origin is held in CONTRACTS.3.
3. **Positions.** P1 explicit artifact. P2 schema insufficient. P3 null against absent. P4 logical type, physical mapping. P5 owner, version, lifecycle (MAINT: no version numbers). P6 data-engineering format.
4. **Rejected.** A contract that lives in the producer's code: best never for an interface with more than one consumer. The full data-engineering format for one application database: best when data leaves the application for a platform team (data pipelines are deferred by MD-05).
5. **Context.** Consumer reach (versioning, as in CONTRACTS.1); whether data leaves the application for a platform team (format).
6. **Certainty.** Grounded for P1 to P3 (consensus, T2 and standards sources); inferred for the derivation of physical types and for the checklist reading (L1287 open).
7. **Flags.** none.

Constraints: MUST state structure and meaning without the producer's source; MUST give each contract one owner; MUST NOT hand-copy a type across tiers. Links: Realizes ASSURANCE.CONTRACTS.1, .3; related EVOLUTION.DECOMMISSION (lifecycle statuses), STATE.1.

### CONSTRUCTION.BOUNDARY.4 The Contract Over Stored Data

Intent (sharpened): whether and when the store itself is the contract.

1. **Decision.** The base structures of a store are internal; consumers bind to a published interface. When one application owns the store and all access passes through it, that application's interface is the contract and no second layer is added (migration discipline carries change). When several consumers need the data, the owner publishes an interface: an application interface by default; a dedicated published layer in the store, with the base structures private, where consumers need direct query access (set queries, reporting) or privileges must be separated in the store itself. Both are interfaces the owner publishes (HIDING.4); neither is an integration database, which binds consumers to the base structures. Which form that layer takes (a shape-bound read surface or an operation with a signature) is decided in BOUNDARY.5. Outcome: a change to the stored structure cannot break an unknown consumer.
2. **Grounds.** Database as contract: a dedicated schema for consumers, base structures private (L1285; contested, one source family, REG-1156, T3); the condition is the row's own (several consumers or strict privilege separation favour it; a single owning server does not need it, WL187 now read); the owner-only structure follows HIDING.4 (L1225; REG-1133). Final pass: REG-1133 fetched in review (integration databases avoided, application-level interfaces preferred); REG-1156 (T3) gives the store layer with no conditions; the conditions are inferred.
3. **Positions.** P1 the store is the contract (independent change of internals). P2 an application API over base tables with migration discipline (no second layer). P3 signature over shape (maintainer, BOUNDARY.5).
4. **Rejected.** P1 for a single owning application: adds a layer and a second place for logic with no consumer to benefit. P2 for several direct consumers or privilege separation: the base structures become the contract and ossify; best only while there is one owner.
5. **Context.** Number of consumers with direct access and whether privilege separation is required (L1285).
6. **Certainty.** Inferred: contested (one T3 source family against one practice), condition inferred in the row; the decision is the row's own condition made explicit.
7. **Flags.** none.

Constraints: MUST NOT expose base structures to a consumer other than the owner. Links: Realizes ASSURANCE.CONTRACTS.1; related ASSURANCE.DATA_INTEGRITY.1, HIDING.4, BOUNDARY.5.

### CONSTRUCTION.BOUNDARY.5 Call Shape and Evolvable Interfaces

Intent (sharpened): the shape a call or interface takes so consumers can bind to it and it can change.

1. **Decision.** Choose the form of an interface by who composes the result: an operation with a signature (parameters, optional parameters) where the consumer asks a question or requests a change and the owner composes the answer, which lets the owner change how the result is produced and add inputs; a shape-bound read surface where consumers must filter, join and aggregate the result themselves (reporting, several readers), since a signature cannot be composed by the caller or planned with the caller's own query. Writes always go through operations. In both, the output shape is evolved additively and removal follows the rule of ASSURANCE.CONTRACTS.1 for the consumer reach. A call carries its meaning by name: past a small number of parameters they are passed by name or as a named structure. The output model limits what leaves (the split of input and output models is held in ASSURANCE.CONTRACTS.3); a response that fails its declared output is a server defect (BOUNDARY.6). The interface is strict for what it accepts from callers it controls (unknown fields rejected) and tolerant for what it reads from a provider it does not control (read what you use, ignore the rest, validate the fields you use for type, range and size). Outcome: a consumer binds to what it needs and the owner can evolve the rest.
2. **Grounds.** Signature over shape (L309; MAINT-S01, REG-181, grounded as the maintainer's position, public practice contested: views are commonly offered as a stable interface). Final pass: L309 is the maintainer's alone and its own sub-position (a) is the shape-bound case; a view also hides how its result is produced, so the remaining differences are input parameters and caller-side composition, and those decide by who composes; the "prefer a signature" default is removed. Names over positions (L1509; one T1 tool documentation, inferred; REG-1506). Separate input and output models (L1272; REG-1150; settled alongside CONTRACTS.3). Open for readers, closed for writers (L1279; REG-1147, inferred). Tolerant reader (L1278, L341; REG-1152, REG-208) against strict validation of all received (REG-194): the synthesis (L341, inferred) is the decision, and drift is detected by contract tests (ASSURANCE.CONTRACTS.2), not by breaking at run time.
3. **Positions.** P1 signature over shape (change absorption; sub-positions: view for read-only reporting, function for many dependents). P2 name over position. P3 separate input and output models. P4 open for readers, closed for writers. P5 read what you use. P6 tolerant reader against strict schema validation.
4. **Rejected.** A signature as the default for every interface, and a shape-bound surface as the default: the form follows who composes the result. A shape-bound surface is best for read-only reporting with several consumers and for introspection or throwaway owner use. A signature everywhere: loses composability where consumers must filter and join, and is opaque to the caller's own planning. Generating consumers from the full producer schema: trades resilience for convenience; best where producer and consumer release together or drift detection matters more than uptime. Fully tolerant parsing of data that feeds an interpreter: best never (validate what you use).
5. **Context.** Read-only reporting for several consumers (shape-bound acceptable); consumers composing the result themselves; data that crosses a trust boundary or feeds an interpreter (validate the fields used).
6. **Certainty.** Inferred: L309 is the maintainer's alone, so the decision rests on who composes the result, not on the maintainer's row as a default; grounded for the tolerant-reader family (consensus, two sources).
7. **Flags.** none.

Constraints: MUST evolve an interface's output additively, and remove only under the rule of CONTRACTS.1 for the consumer reach; MUST NOT generate consumers from the full schema of a provider the consumer does not control; own-provider stubs follow CONTRACTS.3. Links: Refines NAMING (names carry meaning); related BOUNDARY.4, ASSURANCE.CONTRACTS.

### CONSTRUCTION.BOUNDARY.6 Errors at the Boundary

Intent (sharpened): what a failure at a boundary carries and who is at fault when output is malformed.

1. **Decision.** A failure is explicit, never silent: mandatory inputs are validated first, and an error names the component and the offending values and carries a stable code (the violated constraint maps to a stable contract error, ASSURANCE.DATA_INTEGRITY.1). Detail is audience-scoped: the full detail (values, internals) goes to the log and to a trusted caller, while an untrusted caller receives the stable code and field names, not secrets or internals. A response that fails its own declared output is a defect in the producing code: return a server error and alert, never a malformed body. Outcome: a failure is diagnosable by its owner and a malformed answer never passes as a success.
2. **Grounds.** Errors name component and values, stable codes, validate mandatory inputs first, explicit failure (L315; MAINT-S01, REG-181, public practice agrees); output that fails the model is a server defect (L1273; REG-1150). The audience scoping is not in a row; it follows from BOUNDARY.1 (an untrusted party must not be handed what feeds an attack). Final pass: the OWASP Error Handling Cheat Sheet, fetched, says "the error details are logged server side for investigation, and not returned to the user"; settled against the maintainer's practice, narrowing L315.
3. **Positions.** P1 diagnosable, stable-coded explicit errors (diagnosability). P2 malformed output is a server defect.
4. **Rejected.** Echoing offending values to every caller: best only where the caller is trusted and the values are not sensitive. Repairing a malformed output silently: best never.
5. **Context.** Trust level of the recipient of the error.
6. **Certainty.** Grounded for P1 core and P2 (agreeing practice, one source for P2) and for withholding internals from untrusted callers (OWASP); inferred for returning the stable code and field names.
7. **Flags.** none.

Constraints: MUST give an error a stable code; MUST NOT return a malformed body as a success. Links: related ASSURANCE.DATA_INTEGRITY.1, BOUNDARY.1, OPERATION.INCIDENTS.

---

## CONSTRUCTION.STATE State, Values and Load-Time Effects

Intent (sharpened): each fact held in one place, values that state their precision and changeability, and modules whose loading has no effect.

1. **Decision.** One authoritative place per fact (STATE.1), stored relational data normalised to remove update anomalies and denormalised only for measured need (STATE.2), shared derived state treated as derived with a plan (STATE.3), values that state their precision and changeability (STATE.4), and no effect when a module is loaded (STATE.5). Outcome: state cannot silently drift and loading code cannot change behaviour.
2. **Grounds.** Roll-up of STATE.1 to .5 (13 rows).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none beyond the children.
6. **Certainty.** Inferred (roll-up).
7. **Flags.** none.

Links: children; ASSURANCE.DATA_INTEGRITY.4 (sync plan, settled).

### CONSTRUCTION.STATE.1 One Place per Fact

Intent (sharpened): how many places hold a fact and how copies are prevented from drifting.

1. **Decision.** Each fact has one authoritative place; every other representation is derived from it (generated, computed, or a managed copy with the synchronisation plan ASSURANCE.DATA_INTEGRITY.4 requires); repeated type definitions across tiers are held in BOUNDARY.3. Outcome: copies cannot silently disagree.
2. **Grounds.** One place, hold once and derive the rest (L1516, L1517; Codd, T2, grounded for shared data, inferred for application state; REG-1513); one source of truth, duplicated representations are a representable illegal state, including hand-copied type definitions across tiers (L1276; REG-1151, cross-tier application inferred).
3. **Positions.** P1 one place and derive (consistency). P2 one source of truth for each fact (same).
4. **Rejected.** Duplicating for convenience without a plan: best never. Duplicating for performance or independence: best with a plan and a detection (DATA_INTEGRITY.4), then it is derived data.
5. **Context.** none.
6. **Certainty.** Grounded for shared data, inferred for application state.
7. **Flags.** none.

Constraints: MUST NOT keep a second copy without a sync plan. Links: related STATE.2, HIDING.3, ASSURANCE.DATA_INTEGRITY.4.

### CONSTRUCTION.STATE.2 Normal Form for Stored Data

Intent (sharpened): how relational tables are shaped so each fact is stored once and when that is relaxed.

1. **Decision.** Design relational tables to the normal form that removes the update anomalies of their actual dependencies: third normal form by default (every non-key field states a fact about the key, the whole key and nothing but the key), with repeating groups moved to a child table; a higher form (Boyce-Codd, fourth, fifth) where candidate keys overlap or independent multi-valued facts share a table, because there third normal form still permits anomalies. Denormalise deliberately and only for a measured performance requirement, with the redundancy guarded by the synchronisation plan of ASSURANCE.DATA_INTEGRITY.4; prefer a derived read structure over distorting the base tables. Outcome: each fact is stored and changed in one place, and any redundancy is chosen, measured and guarded.
2. **Grounds.** Third normal form by default (L1263; consensus; REG-1144, REG-1146); purpose, no redundancy, update anomalies, inconsistent dependencies (L1264; REG-1144, REG-1146); deliberate denormalisation under measured need (L1265; consensus; REG-1144, REG-1146); third normal form the practical target, higher forms for specific designs (L1266; majority; REG-1146 T3 says rarely considered, REG-1144 covers 3NF, 4NF and 5NF without ranking; 3NF grounded, "specific designs" inferred; the Boyce-Codd clause is grounded by definition (it follows from the definition of the forms, a definitional fact that needs no empirical source), REG-1144 does not cover it, and REG-1146 calls 4NF "Boyce-Codd" wrongly); remove repeating groups (L1267; REG-1146). The maintainer's practice (3NF and beyond by default) is the same as the first clause; the dependency-driven rule and the maintainer's "3NF+" coincide: where keys do not overlap and no independent multi-valued facts share a table, the higher forms equal third normal form.
3. **Positions.** P1 3NF default. P2 normalise to remove anomalies. P3 denormalise for measured need. P4 3NF the practical target. P5 child table for repeating groups.
4. **Rejected.** A higher form chosen without the dependency that needs it: adds nothing. Denormalising by anticipation: best never; best when a measured requirement exists and the guard is in place.
5. **Context.** Measured performance requirement (L1265); overlapping candidate keys or independent multi-valued facts (higher forms).
6. **Certainty.** Grounded for 3NF default and measured denormalisation (consensus); grounded by definition for the Boyce-Codd clause; inferred for the dependency-driven use of higher forms.
7. **Flags.** none.

Note: technology-bound to relational storage, not to a programming language; for other stores STATE.1 holds. Constraints: MUST NOT denormalise without a measured need and a sync plan. Links: related STATE.1, ASSURANCE.DATA_INTEGRITY.4.

### CONSTRUCTION.STATE.3 Shared Derived State

Intent (sharpened): where a cache lives and how it is invalidated.

1. **Decision.** A cache is derived state and never the source of truth or permanent storage; it has an owner, an explicit expiry or invalidation plan and versioned or prefixed keys. State read by several processes lives in a cache shared by them; a per-process cache is used only for data whose divergence between processes is tolerable within a stated staleness (immutable data, short expiry). Outcome: processes agree on shared derived data, and an invalidation failure is bounded.
2. **Grounds.** Shared cache in multi-process production, never permanent storage (L1204; consensus; REG-1107, REG-1109); expiry or invalidation plan, versioned keys (L1205; practice, inferred, REG-1107; REG-1111 is a proverb's attribution, not evidence).
3. **Positions.** P1 shared cache (coherence across processes). P2 per-process memory as the cache. P3 explicit invalidation plan.
4. **Rejected.** P2 for mutable data read by several processes: they diverge; best for immutable or short-lived data and for a single process. A cache with no plan: best never.
5. **Context.** Single process or tolerable staleness (per-process acceptable).
6. **Certainty.** Grounded for shared against local in multi-process production; inferred for the invalidation rule.
7. **Flags.** none.

Constraints: MUST give every cache an expiry or invalidation plan. Links: related PROCESS.3, STATE.1, ASSURANCE.DATA_INTEGRITY.4.

### CONSTRUCTION.STATE.4 Value Precision and Mutability

Intent (sharpened): which values a type may carry and whether the code states changeability.

1. **Decision.** A numeric type carries exactly only the values within its precision and range; a value beyond them (money, counters, identifiers) uses a type that represents it exactly, and where a type rounds, equality of computed values is not restored by an arbitrary fixed tolerance (it is arbitrary and not transitive), a tolerance being justified only when derived from the known error of a measured quantity. The code states whether a value cannot change at all or may be changed only by some holders, and what states it also enforces it; no preference between the two is derived. Outcome: no value is silently altered by its representation, and who may change a shared value is known.
2. **Grounds.** Precision and range (L1501; Goldberg 1991, T2, single source; REG-1501; grounded for the tolerance point, inferred for the positive statement; scope: any language with a type that rounds, the row's own); immutability against read-only restriction (L1502; one T2 taxonomy; REG-1502; open for any preference).
3. **Positions.** P1 exact representation beyond precision. P2 a fixed tolerance as the general cure (rejected). P3 state immutability or restriction.
4. **Rejected.** P2 as general cure: best when the quantity is a measurement with a known error and the bound comes from it. A stated preference for immutability over restriction: no admitted source states it; open.
5. **Context.** none beyond the row's own scope (types that round).
6. **Certainty.** Grounded for the tolerance point (one T2 source); inferred for the positive statement; open for any preference between immutability and restriction.
7. **Flags.** none.

Constraints: MUST use an exact representation for values beyond a type's precision. Links: none stated.

### CONSTRUCTION.STATE.5 Load-Time Effects

Intent (sharpened): whether loading a module may have effects beyond constructing its own definitions.

1. **Decision.** Where a language runs module code when the module is loaded, loading does nothing beyond constructing its own definitions: no input or output, registration, connection or global change; effects happen in explicit start-up steps called from the program's entry point. Outcome: loading order never changes behaviour.
2. **Grounds.** L1518 (single source family, inferred, no source states the rule, quote not obtained; REG-1514, REG-1515, REG-1516: one language's module system and one bundler). The principle follows from DEPENDENCY_DIRECTION.1 (order must not decide behaviour). Final pass: the isocpp FAQ, fetched, describes the same hazard class in C++ (the "static initialization order fiasco": an initialisation that uses another unit's object before it is constructed fails depending on the order units are initialised), so the hazard is shown in two unrelated language families.
3. **Positions.** P1 effect-free loading (predictability). No competing position recorded.
4. **Rejected.** Registration on load as a convenience: best where the platform's design mandates it and the order is irrelevant (inferred).
5. **Context.** Holds only for languages that run module code at load time (the row's own scope).
6. **Certainty.** Grounded for the hazard class in two languages; inferred for the general rule; the mechanics stay stack pointers (the stack guidelines of languages that run module code at load carry them).
7. **Flags.** none.

Constraints: MUST NOT perform effects in module-load code. Links: Refines DEPENDENCY_DIRECTION.1.

---

## CONSTRUCTION.DEPENDENCY_DIRECTION Dependency Direction

Intent (sharpened): dependencies between modules flow one way, never in a cycle, under a declared layering that is enforced.

1. **Decision.** Dependencies between modules form an acyclic graph at each level (.1), and the allowed directions between kinds of module are declared and checked on every change (.2). Outcome: a change propagates predictably and order never decides whether code works.
2. **Grounds.** Roll-up of .1 and .2 and L1519 (node-level statement, inferred).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Inferred.
7. **Flags.** none.

Links: children; related HIDING.3, ASSURANCE.RULES.3.

### CONSTRUCTION.DEPENDENCY_DIRECTION.1 No Cycles

Intent (sharpened): whether modules may depend on each other in a cycle.

1. **Decision.** Modules do not depend on each other in a cycle across module boundaries: a cycle is removed by extracting the shared part into a module both depend on, or by inverting one dependency through an abstraction owned by the depended-upon side. A cycle inside one module (inside one hidden decision) is not a violation. Outcome: each module can be understood, tested and changed with only the modules below it, and load or initialisation order never decides correctness.
2. **Grounds.** L1520 (no claim of its own, inferred; REG-1516; no source measures the cost; the conflict recorded is that one platform documents cycles as supported and states no recommendation). Supported by the information-hiding purpose (HIDING.1): a cycle makes two modules one decision unit.
3. **Positions.** P1 no cycles. P2 tolerate cycles (supported mechanism).
4. **Rejected.** P2: a supported mechanism is not a reason to use it; best only inside one module whose parts are one decision.
5. **Context.** Cycle inside one module is acceptable.
6. **Certainty.** Inferred (no source measures the cost).
7. **Flags.** none.

Constraints: MUST NOT create a dependency cycle across module boundaries. Links: Refined by STATE.5; related HIDING.1, DEPENDENCY_DIRECTION.2.

### CONSTRUCTION.DEPENDENCY_DIRECTION.2 Declared Layering

Intent (sharpened): whether allowed directions between kinds of module are declared and mechanically enforced.

1. **Decision.** Where the design states which kinds of module may depend on which (DESIGN.3 constraints, HIDING.3 layers), that rule is declared in a checkable form and enforced by a blocking check on every change (ASSURANCE.RULES.3); a declared layering that is only convention is not a rule. Whether a codebase needs a layering at all is decided by DESIGN.3, not here. Outcome: the declared structure does not erode.
2. **Grounds.** Mechanical enforcement of boundaries as a gate (settled in ASSURANCE.RULES.3: L1216, L1234; REG-1117, REG-1119); proposed changes tested against the constraints (L1226; REG-1124, REG-1125); the fact kept by the row: a lint-style rule can forbid imports by path or pattern (L1521; REG-1517, REG-1508). No admitted source grounds a layering principle by itself; the decision rests on the enforcement principle, not on layering as such.
3. **Positions.** P1 declare and enforce import directions. No competing position recorded.
4. **Rejected.** Convention or review alone: best only when the rule cannot be expressed as a check (RULES.3).
5. **Context.** none.
6. **Certainty.** Inferred (open as a standalone principle in the origin; grounded now only through the settled enforcement rule).
7. **Flags.** none.

Constraints: MUST make a declared layering a blocking check. Links: Realizes ASSURANCE.RULES.3; related HIDING.3, DESIGN.3.

---

## CONSTRUCTION.NAMING Naming

Intent (sharpened): names let a reader recover the concept without the author.

1. **Decision.** Names are whole words (NAMING.1), one concept has one name used consistently (NAMING.2), and a name is derived from the concept it covers and defined where it is shared (NAMING.3). Outcome: a newcomer recovers the concept from the name.
2. **Grounds.** Roll-up of NAMING.1 to .3 and L1522 (node-level statement; transfer of the experiments across languages is inference).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Inferred (roll-up; experiments in one language, transfer inferred).
7. **Flags.** none.

Links: children; related DESIGN.1 (L329), BOUNDARY.5 (names over positions); L196 (semantic conventions, another branch).

### CONSTRUCTION.NAMING.1 Whole Words

Intent (sharpened): whole words or abbreviations in identifiers.

1. **Decision.** Name identifiers with whole words, not single letters or letter-deleting abbreviations, except where the abbreviation is itself the established term of the domain and its audience. Outcome: defects are found faster and a reader does not decode names.
2. **Grounds.** An experiment with 72 professional developers (one language): words gave about 19 percent faster defect finding than letters or abbreviations, no significant difference between letters and abbreviations (L1523; single T2 source; REG-1518; grounded for the experiment, inferred for other languages).
3. **Positions.** P1 whole words (reading speed). P2 letters or abbreviations (no better than letters; slower than words).
4. **Rejected.** P2: best only for established domain terms (inferred; no row states it) and tiny scopes where the meaning is local and visible.
5. **Context.** none stated by the row; the exception is the judge's inference.
6. **Certainty.** Grounded for the experiment; inferred for the transfer and for the domain-term exception.
7. **Flags.** none.

Constraints: MUST NOT shorten a name by deleting letters, except an established term of the domain and its audience. Links: related NAMING.2.

### CONSTRUCTION.NAMING.2 One Concept One Name

Intent (sharpened): how names are composed and kept consistent.

1. **Decision.** Give one concept one name, made of common descriptive words, and use it the same way in code, data, interfaces and documents. Outcome: searching for a concept finds all of it and no two concepts share a name.
2. **Grounds.** L1524 (single source family: four style or design guides, holder positions, not evidence; transfer from web-platform API design inferred; REG-1519, REG-1510, REG-1520, REG-1521).
3. **Positions.** P1 one concept, one name, common words, consistent.
4. **Rejected.** Synonyms for variety: best never.
5. **Context.** none.
6. **Certainty.** Inferred (holder positions of guides, no effect evidence).
7. **Flags.** none.

Constraints: MUST use one name per concept across all artifacts. Links: related NAMING.1, TRANSVERSE.DOCS.

### CONSTRUCTION.NAMING.3 Names Derived from Concepts

Intent (sharpened): how a name is coined.

1. **Decision.** Derive a name from the concepts it covers: select the concepts, choose a word for each, compose; because two people rarely coin the same name, a shared name carries a definition where it is introduced, and names are tested on a newcomer, who should recover the concept; names within a family are hierarchical and unambiguous. Outcome: names are understood by readers who did not coin them.
2. **Grounds.** Two developers coin the same name rarely (median 6.9 percent over 47 instances) while a chosen name is usually understood (L1525; single T2 source; REG-1522; language of the experiments not checked); hierarchical, unambiguous, intuitive, a newcomer should understand (L329; MAINT-S01, REG-181; the maintainer's naming half, held here, MD-03).
3. **Positions.** P1 derive from concepts (understandability). Maintainer: invest time in names.
4. **Rejected.** Coining a name from the first word that comes to mind: best never for a shared name; best for a local, short-lived one.
5. **Context.** none.
6. **Certainty.** Inferred (single experiment source; the maintainer's naming test is single-source).
7. **Flags.** none.

Constraints: MUST define a shared name where it is introduced. Links: related DESIGN.1.

---

## CONSTRUCTION.PARADIGM Paradigm and Placement of Logic

Intent (sharpened): how a programming paradigm and the place of logic (application, data tier, scheduler) are chosen by intent.

1. **Decision.** The paradigm is chosen per part by what the problem is (PARADIGM.1), and logic is placed by the property it must have: holds across writers, changes with the product, is fast to test, or acts on data in place (PARADIGM.2). Outcome: each piece of logic is where its purpose is best served.
2. **Grounds.** Roll-up of PARADIGM.1 and .2 (5 rows); L312 (paradigm half, held in OWNERSHIP.SELECTION.2).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none beyond the children.
6. **Certainty.** Inferred.
7. **Flags.** none.

Links: children; OWNERSHIP.SELECTION.2, ASSURANCE.DATA_INTEGRITY.1.

### CONSTRUCTION.PARADIGM.1 Paradigm by Intent

Intent (sharpened): whether a paradigm is chosen by the problem or by a defect-rate claim.

1. **Decision.** Choose the programming paradigm per part by what the problem is, mixing paradigms deliberately at stated boundaries (a taxonomy of kinds with shared behaviour, a transformation of data, a sequence of control are natural fits for different styles), and never by a defect-rate claim for a paradigm. Outcome: the code takes the shape of the problem it solves.
2. **Grounds.** No admitted evidence supports a paradigm mandate (L1526; REG-1523, REG-1524, REG-1509, REG-1525): the defect-rate studies compare languages, not paradigms within one language, with exceedingly small effects and a contested reproduction (T3, not peer-reviewed); the maintainer chooses per part by intent (L312, MAINT-S01, REG-181), which agrees with the evidence.
3. **Positions.** P1 by intent (fit to the problem). P2 by defect-rate evidence (rejected in the origin; contested).
4. **Rejected.** P2: the evidence does not support it; best when a paradigm-level effect on defects is shown inside one language.
5. **Context.** none.
6. **Certainty.** Inferred (from the absence of evidence scoped to a paradigm choice; the contested fact is recorded as contested).
7. **Flags.** none.

Constraints: MUST NOT mandate a paradigm on a defect-rate claim. Links: Requires HIDING.1 (the two hiding styles); OWNERSHIP.SELECTION.2.

### CONSTRUCTION.PARADIGM.2 Placement of Domain Logic

Intent (sharpened): where each kind of logic lives (application, data tier, scheduler) and what moves it.

1. **Decision.** Place each piece of logic by the property it must have. A rule that must hold whichever code writes is declared in the store (settled, ASSURANCE.DATA_INTEGRITY.1). Domain logic that changes with product decisions, is branching or algorithmic, or must be tested fast lives in the application first, and a proven measured hot spot moves into the data tier as a set-based query, not as domain rules. A set-oriented transformation of stored data, where moving the data costs measurably more or atomicity with the data is needed, runs in the data tier (inferred: no row states it). Team skill is a legitimate tie-breaker between placements that meet the properties equally, never a reason to leave an invariant out of the store. Scheduled work runs where the data lives when it acts only on that store's state as bounded statements or batches, and needs no operating-system commands, no retries beyond a rerun and no cross-system dependencies or backfills; otherwise it runs in the application tier or an orchestrator. Scheduled work is monitored through the scheduled-work signals of OPERATION.TELEMETRY.8. Logic placed in the data tier is versioned and tested against a real disposable store. Outcome: each kind of logic is where it holds, changes and is tested at least cost.
2. **Grounds.** Application first, profile, move hot spots into SQL (L1259; contested; REG-1143, T2, 2003; database-heavy position not found at T1 or T2 as an argument for domain logic; consensus that constraints and keys belong in the store); team skill (L1260; REG-1143; kept a tie-breaker: a cost-of-ownership force, not a rule about who writes code, MD-02); testability, in memory behind a replaceable interface against a database needed to test (L1261; REG-1143); scheduled work where the data lives, with the limits that send it elsewhere (L311; MAINT-S01, REG-181, public practice read as contested, a dedicated orchestrator being the usual norm). The decision does not choose between "application" and "database" as camps: the settled DATA_INTEGRITY.1 already splits by kind, and this node extends the same split to the remaining kinds of logic.
3. **Positions.** P1 application first (modifiability; wins with no measured hot spot). P2 logic in the database (correctness across writers, data locality). P3 team skill as input. P4 application logic tests faster. P5 scheduled work in the store against an external orchestrator (cost of ownership and consistency against control and scale).
4. **Rejected.** Database-first for domain rules that change with the product: they change at product speed and need a store to test; best for invariants across writers and for set-based data transformations. Application-only for invariants: leaves migrations and ad-hoc access unguarded (settled). An external orchestrator for every job: best for multi-system pipelines and jobs with retries and dependencies; costs one more system to run for a bounded in-store job.
5. **Context.** Measured hot spot; team comfort with the store's language (L1260); bounded in-store job against multi-system pipeline (L311).
6. **Certainty.** Inferred: placement by property follows from grounded rows and the settled split; the scheduler clause is single-source maintainer practice with no public claim to confirm it; the application-first clause is contested (one T2 source); the set-oriented transformation clause has no row and is inferred.
7. **Flags.** none.

Note: technology-bound (a store with a query language), not language-bound. Constraints: MUST test logic placed in the store against a real store; MUST monitor scheduled work (OPERATION.TELEMETRY.8). Links: related OWNERSHIP.STANCE (L308), HIDING.3, ASSURANCE.DATA_INTEGRITY.1, ASSURANCE.BEHAVIOUR.7.

---

## CONSTRUCTION.DATA_NOT_CODE Keeping Data From Becoming Code

Intent (sharpened): untrusted data is never interpreted as code, a query, a path, a destination or an object.

1. **Decision.** Every sink that interprets data as code, a command, a query, a path, a destination or a serialised object is treated as dangerous: data reaches it only as data (separately passed values, allowlisted shapes, pure data formats), hostile data is narrowed at each sink and a second layer (least privilege, containment) limits what slips through. Outcome: hostile data cannot become an instruction or a location an interpreter acts on.
2. **Grounds.** Roll-up of .1 to .4 (7 rows) and L1527, L1528 (origin roll-up and node intent, no claim of their own); secrets drawn, compared, stored and logged only through audited mechanisms is held in TRANSVERSE.CONFIG (L1535 moved there).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Grounded for the children (consensus, T1 sources); inferred as a roll-up.
7. **Flags.** none of its own.

Links: Requires BOUNDARY.1 (L1527 requires L1505); Refines BOUNDARY.2 (L1528 refines L1506); related ASSURANCE.SECURITY (SECURITY.2, .6 settled), TRANSVERSE.SECURITY.

### CONSTRUCTION.DATA_NOT_CODE.1 Code and Commands

Intent (sharpened): whether and how text becomes code or an operating-system command.

1. **Decision.** Never build code from strings: dynamic evaluation of attacker-influenced text executes it with the caller's privileges, through whatever interface offers it, and a template system that evaluates expressions makes template source code, not data. Start a process without a shell and with a program not chosen by input, so arguments stay arguments; prefer library functions to operating-system commands; where a command is unavoidable, allowlist the executable and its arguments and run it with least privilege. Outcome: input cannot cause execution.
2. **Grounds.** Dynamic evaluation (L1529; grounded for the rule, consensus, four T1 sources; template injection single source T3 and T2; REG-1526 to REG-1531); process start without a shell (L1530; single T1 source, principles only; REG-1532); adjacent L325 (least privilege at the lowest layer, SECURITY.6, settled).
3. **Positions.** P1 never build code from strings. P2 no shell, no input-chosen programs.
4. **Rejected.** Escaping or sanitising input to be evaluated: best never as the defence. Where a product must run user-authored logic: a restricted language recognised by a parser (BOUNDARY.2), confined with least privilege (inferred; the rows do not cover it).
5. **Context.** none.
6. **Certainty.** Grounded for the rule (four T1 sources); inferred for the user-authored logic case.
7. **Flags.** none.

Constraints: MUST NOT evaluate attacker-influenced text as code; MUST NOT start a process through a shell with input-derived text. Links: required by DATA_NOT_CODE.4.

### CONSTRUCTION.DATA_NOT_CODE.2 Queries

Intent (sharpened): how untrusted values reach a query engine.

1. **Decision.** A query reaches its engine as fixed text plus separately passed values, in every store, SQL or not; untrusted values are never concatenated or templated into the text, identifiers, keywords and sort order are redesigned or mapped through a fixed allowlist, and the application's store account has least privilege as a second layer. Outcome: input cannot change the structure of a query.
2. **Grounds.** L1531 (consensus for parameterisation, identifiers and non-immunity; single source for least privilege and the rejection of escaping; REG-1533 to REG-1542).
3. **Positions.** P1 fixed text plus separate values (injection resistance). P2 escaping all input as the primary defence. P3 the belief that non-SQL stores are immune.
4. **Rejected.** P2: fragile, not guaranteed to stop all injections; best only as a last layer where a parameter cannot be used (inferred). P3: false.
5. **Context.** none.
6. **Certainty.** Grounded.
7. **Flags.** none.

Constraints: MUST NOT build query text from untrusted values. Links: related ASSURANCE.SECURITY (L325), BOUNDARY.1.

### CONSTRUCTION.DATA_NOT_CODE.3 Paths and Destinations

Intent (sharpened): how a file location or network destination chosen from input is confined.

1. **Decision.** A file location chosen from input stays inside its base directory: paths are built from internally generated or trusted names, user-supplied names are unavoidable only under strict allowlist validation, and containment is checked on the resolved location that is then actually used. A server fetches only destinations it allows: match the host against an allowlist and build the request itself, do not accept complete URLs from users where avoidable, validate the resolved addresses against the permitted networks and connect only to the validated address, and re-check redirect targets. Outcome: input cannot name a location outside what was allowed.
2. **Grounds.** Paths (L1532; consensus for the constraint, single source for one clause; REG-1536, REG-1543, REG-1529, REG-1544); destinations (L1534; consensus for the allowlist, single source for the URL and DNS points; REG-1550, REG-1535, REG-1536); adjacent L340 (redirect allowlist, OWNERSHIP.CONTAINMENT.4, settled).
3. **Positions.** P1 paths stay in the base directory. P2 allowlisted destinations checked at the connected address.
4. **Rejected.** A hostname check alone: not enough, the name can resolve elsewhere; best never alone.
5. **Context.** none.
6. **Certainty.** Grounded for the constraints; open for "checked after resolution and used without a race" as a clause (no claim grounds it; kept as the logical form of the containment check, inferred).
7. **Flags.** none.

Constraints: MUST check containment on the resolved location used. Links: related OWNERSHIP.CONTAINMENT.4, ASSURANCE.SECURITY.

### CONSTRUCTION.DATA_NOT_CODE.4 Structured Payloads

Intent (sharpened): how structured data crossing a trust boundary is exchanged and parsed.

1. **Decision.** Data crossing a trust boundary is exchanged in a pure data format that carries neither types nor code and is never deserialised into executable structures; when the set of expected messages is known, serialised data is signed and verified before deserialising; a new object is populated from validated fields; when untrusted XML is parsed, document type definitions are disabled (and, where required, external entities and external definitions disabled and entity expansion limited). Where two components read the same bytes their parsers must agree: control and delimiter characters that can alter structure never reach a field value (reject the message or neutralise them at the first parser). Outcome: payload content cannot become executable structure or desynchronise two parsers.
2. **Grounds.** Format, signing, populating a new object, XML (L1533; consensus for the format rule and the XML rule, single source for signing and the new object; REG-1545, REG-1536, REG-1528, REG-1546 to REG-1549); parser disagreement and control characters in a protocol field (L1536; single source RFC section, T1; REG-184; protocol-level, kept here as injection of protocol structure).
3. **Positions.** P1 pure data format, never executable. P2 parsers agree, control characters rejected.
4. **Rejected.** Native object serialisation across a trust boundary: best only inside one trust zone where both ends are one release (inferred).
5. **Context.** none.
6. **Certainty.** Grounded for the format and XML rules (consensus); single-source for the signing step and the protocol rule.
7. **Flags.** none.

Constraints: MUST NOT deserialise untrusted data into executable structures. Links: Requires DATA_NOT_CODE.1.

---

## CONSTRUCTION.PROCESS Process Lifecycle

Intent (sharpened): how a process starts, stops, fails and holds state so it can be replaced and scaled.

1. **Decision.** A process starts fast and stops on request without losing work (.1), ends on a failure it cannot repair and is restarted by something outside it (.2), and holds no state that cannot be lost (.3). Outcome: any process can be replaced or added at any time.
2. **Grounds.** Roll-up of .1 to .3 (3 rows).
3. **Positions.** None here.
4. **Rejected.** Not applicable.
5. **Context.** Hosted-service scope (MD-05).
6. **Certainty.** Inferred (roll-up; sources are one operations-practice family and one runtime page).
7. **Flags.** none of its own.

Links: children; related CHANGE_FLOW.DEPLOY, OPERATION.CAPACITY.

### CONSTRUCTION.PROCESS.1 Fast Start and Graceful Stop

Intent (sharpened): how quickly a process starts and how it ends on request.

1. **Decision.** A process starts in seconds and, on a request to stop, stops accepting new work, finishes or returns its in-flight work, and exits; work that cannot finish within the stop window is checkpointed or resumable. Outcome: releases and scaling are cheap and no work is lost.
2. **Grounds.** L1202 (consensus; REG-1109, one operations-practice document); names an operating-system stop signal in the row, a mechanism not stated here; the checkpoint clause is inferred.
3. **Positions.** P1 fast start, graceful stop (cheap release and scaling). No competing position recorded.
4. **Rejected.** Slow-start processes: best where a start cost is unavoidable (large in-memory model), then the cost is budgeted in release and scaling plans (inferred).
5. **Context.** none.
6. **Certainty.** Grounded (one source family); inferred for the checkpoint clause.
7. **Flags.** none.

Constraints: MUST handle a stop request without dropping in-flight work. Links: related PROCESS.3, CHANGE_FLOW.DEPLOY.

### CONSTRUCTION.PROCESS.2 Fail Fast Under Supervision

Intent (sharpened): what a process does after a failure it cannot repair.

1. **Decision.** After a failure the program cannot repair, its state is undefined: it records the failure, releases what it owns and ends, and restarting is the job of something outside it; failures the program can repair (expected, bounded) are handled where they occur. Outcome: a broken process does not keep serving on undefined state, and recovery does not depend on the broken code.
2. **Grounds.** L1510 (single T1 page, grounded by the origin's merged rule; REG-1507; the origin names runtime hooks, dropped here).
3. **Positions.** P1 end and let a supervisor restart. No competing position recorded.
4. **Rejected.** Continuing after an unrepairable failure: best never. Restart loops with no alert: best never; the supervisor's restart policy and crash-loop alert belong to OPERATION (inferred).
5. **Context.** none.
6. **Certainty.** Grounded for the one runtime whose documentation states it (one T1 page, REG-1507); inferred as a general principle.
7. **Flags.** none.

Constraints: MUST end the process after an unrepairable failure and record it. Links: related OPERATION.INCIDENTS, PROCESS.1.

### CONSTRUCTION.PROCESS.3 Stateless Processes

Intent (sharpened): where a process keeps state.

1. **Decision.** A process holds no state that cannot be lost or rebuilt: session and durable state live in external stores, processes share nothing, and a request does not depend on reaching a particular process; stickiness is at most a performance optimisation with a correct fallback. Outcome: any process can be replaced and capacity added by adding processes.
2. **Grounds.** L1203 (consensus; REG-1109, one operations-practice document).
3. **Positions.** P1 stateless, share nothing (replaceability, scaling). No competing position recorded.
4. **Rejected.** Sticky sessions as the state mechanism: best never; derived state held in memory (a cache, STATE.3) is allowed because it can be rebuilt.
5. **Context.** none.
6. **Certainty.** Grounded (one source family); inferred for the "rebuildable" boundary.
7. **Flags.** none.

Constraints: MUST NOT keep authoritative or session state only in a process. Links: related STATE.3, PROCESS.1.

---

## Flags raised (9)

All nine are settled and removed from their records. F6 (BOUNDARY.1) and F8 (NAMING.1) were settled by review (R12, R07). F1 (BOUNDARY.5, R17), F2 (PARADIGM.2, R19), F3 (SYSTEM_SHAPE.3, R20), F4 (DESIGN.4, R21), F5 (STATE.5, R23), F7 (STATE.2, R24) and F9 (BOUNDARY.6, R25) were settled by the final pass. Flags still open: none.

Seam, resolved by cross-unit fix X7: OWNERSHIP.SERVICES.2 (J1) against the settled CONTRACTS.1. CONTRACTS.1 now holds which evolution policy a provider follows, by consumer reach and artifact kind; OWNERSHIP.SERVICES.2 keeps only the consumer side. No J5 record restates either; SYSTEM_SHAPE.3 and BOUNDARY.3 to .5 already point to CONTRACTS.1.

## Review applied

Review fixes applied: 16 of 16. Flag findings R17 to R25 were acted on in the final pass (section Final pass applied).

- R01 applied: BOUNDARY.3 derives types from the place where the team records the chain starts (CONTRACTS.3); version rule pointed to CONTRACTS.1, not restated.
- R02 applied: STATE.1 keeps "every other representation is derived"; cross-tier types clause replaced by a pointer to BOUNDARY.3.
- R03 applied: BOUNDARY.5 decision and MUST say removal follows CONTRACTS.1's rule for the consumer reach.
- R04 applied: BOUNDARY.5 keeps only the output-model and malformed-output points; the input/output split points to CONTRACTS.3.
- R05 applied: "(parameters, optional parameters)"; MUST reworded as a provider-not-controlled rule, own-provider stubs per CONTRACTS.3.
- R06 applied: "small enough to understand as a whole" dropped; team-experience condition (REG-1112) added to the services-first condition, the other conditions marked inferred.
- R07 applied: NAMING.1 constraint carries the established-domain-term exception; F8 settled.
- R08 applied: NAMING.2 clause on deleting letters removed.
- R09 applied: DESIGN.1 says test-first or emergent design is a legitimate way; ordering points to BEHAVIOUR.5.
- R10 applied: DESIGN.4 states the 10x horizon as a common heuristic.
- R11 applied: STATE.2 Rejected reworded; REG-1144 cited for 3NF, 4NF, 5NF only; Boyce-Codd clause marked inferred from the definition.
- R12 applied: BOUNDARY.1 marks the untrusted-party clause grounded (REG-1503), adds that sink narrowing stays under DATA_NOT_CODE; F6 settled.
- R13 applied: PROCESS.2 certainty: grounded for the one runtime, inferred as a general principle.
- R14 applied: STATE.5 outcome no longer names tool behaviour.
- R15 applied: STATE.4 "(money, counters, identifiers)", scope kept to types that round.
- R16 applied: PARADIGM.2 set-oriented clause marked inferred in the decision and in Certainty.

## Final pass applied

Resolutions (final_pass/resolutions.md, unit J5):
- R17 (F1) BOUNDARY.5: applied (first sentence replaced, default removed, grounds and certainty updated, F1 removed; Rejected first clause reworded to match).
- R18 BOUNDARY.4: applied (third sentence replaced, grounds added; HIDING.4 unchanged as stated).
- R19 (F2) PARADIGM.2: applied (scheduler sentence replaced; "small" replaced by "bounded" in Rejected and Context to match; team-skill tie-breaker grounds added; F2 removed).
- R20 (F3) SYSTEM_SHAPE.3: applied, record text unchanged; F3 removed.
- R21 (F4) DESIGN.4: applied (first sentence replaced; MUST narrowed to structures costly to reverse; F4 removed).
- R22 DESIGN.1: applied (dependency-order sentence added).
- R23 (F5) STATE.5: applied, kept as conditional principle (isocpp grounds, certainty reworded; F5 removed).
- R24 (F7) STATE.2: applied, text unchanged; Boyce-Codd clause "grounded by definition" in grounds and certainty; F7 removed.
- R25 (F9) BOUNDARY.6: applied, text unchanged; OWASP grounds and certainty added; F9 removed.
- Judge flags F6 (R12) and F8 (R07): confirmed closed, no change.
Resolutions not applied: none.

Cross-unit lines:
- X7 (J1, J2, J5, J8): applied as far as J5 is concerned: the seam note is marked resolved; no J5 record restates the evolution policy, so no text change. The edits to CONTRACTS.1, OWNERSHIP.SERVICES.2 and DECOMMISSION belong to J2, J1, J8.
- X9 (J9, J5): applied (BOUNDARY.2 holds token acceptance as decision, grounds, position P4 and constraint).
- X12 (J3, J5, J7): applied (PARADIGM.2 decision and MUST point to OPERATION.TELEMETRY.8; the node itself is created by J7).
- X1 to X6, X8, X10, X11, X13, X14: not for J5 (Units column does not name J5); not applied here.
Cross-unit lines not applied: none.

Nodes added in J5: none (OPERATION.TELEMETRY.7 and .8 are J7 nodes).

Flags still open: none.
