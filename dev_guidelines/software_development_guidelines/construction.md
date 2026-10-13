# Construction

## Table of Contents

1. [Thesis](#thesis) _(Lines 60-72)_
1. [Map](#map) _(Lines 75-88)_
1. [Design Derivation](#design-derivation) _(Lines 91-93)_
   1. [Derivation Order](#derivation-order) _(Lines 96-104)_
   1. [Effort and Timing on Costly Decisions](#effort-and-timing-on-costly-decisions) _(Lines 107-115)_
   1. [Properties First, Then Constraints](#properties-first-then-constraints) _(Lines 118-124)_
   1. [Growth Horizon](#growth-horizon) _(Lines 127-135)_
1. [System Shape](#system-shape) _(Lines 138-140)_
   1. [Initial Shape, One Unit or Several](#initial-shape-one-unit-or-several) _(Lines 143-151)_
   1. [Distribution Premium and Its Reversal](#distribution-premium-and-its-reversal) _(Lines 154-162)_
   1. [Placing Service Boundaries](#placing-service-boundaries) _(Lines 165-173)_
   1. [Teams and Structure](#teams-and-structure) _(Lines 176-183)_
1. [Information Hiding and Modularity](#information-hiding-and-modularity) _(Lines 186-188)_
   1. [Cut by Hidden Decision](#cut-by-hidden-decision) _(Lines 191-200)_
   1. [Cut by Business Concept or by Layer](#cut-by-business-concept-or-by-layer) _(Lines 203-209)_
   1. [Separating Presentation, Domain and Data Access](#separating-presentation-domain-and-data-access) _(Lines 212-218)_
   1. [Data Ownership by One Application](#data-ownership-by-one-application) _(Lines 221-230)_
1. [Boundary Contracts and Call Shape](#boundary-contracts-and-call-shape) _(Lines 233-235)_
   1. [Parse or Validate at the Edge](#parse-or-validate-at-the-edge) _(Lines 238-247)_
   1. [What Counts as Valid](#what-counts-as-valid) _(Lines 250-257)_
   1. [What a Contract States](#what-a-contract-states) _(Lines 260-271)_
   1. [The Contract Over Stored Data](#the-contract-over-stored-data) _(Lines 274-282)_
   1. [Call Shape and Evolvable Interfaces](#call-shape-and-evolvable-interfaces) _(Lines 285-294)_
   1. [Errors at the Boundary](#errors-at-the-boundary) _(Lines 297-304)_
1. [State, Values and Load-Time Effects](#state-values-and-load-time-effects) _(Lines 307-309)_
   1. [One Place per Fact](#one-place-per-fact) _(Lines 312-318)_
   1. [Normal Form for Stored Data](#normal-form-for-stored-data) _(Lines 321-327)_
   1. [Shared Derived State](#shared-derived-state) _(Lines 330-336)_
   1. [Value Precision and Mutability](#value-precision-and-mutability) _(Lines 339-347)_
   1. [Load-Time Effects](#load-time-effects) _(Lines 350-356)_
1. [Dependency Direction](#dependency-direction) _(Lines 359-361)_
   1. [No Cycles](#no-cycles) _(Lines 364-370)_
   1. [Declared Layering](#declared-layering) _(Lines 373-383)_
1. [Naming](#naming) _(Lines 386-388)_
   1. [Whole Words](#whole-words) _(Lines 391-397)_
   1. [One Concept One Name](#one-concept-one-name) _(Lines 400-406)_
   1. [Names Derived from Concepts](#names-derived-from-concepts) _(Lines 409-415)_
1. [Paradigm and Placement of Logic](#paradigm-and-placement-of-logic) _(Lines 418-420)_
   1. [Paradigm by Intent](#paradigm-by-intent) _(Lines 423-429)_
   1. [Placement of Domain Logic](#placement-of-domain-logic) _(Lines 432-441)_
1. [Keeping Data From Becoming Code](#keeping-data-from-becoming-code) _(Lines 444-446)_
   1. [Code and Commands](#code-and-commands) _(Lines 449-456)_
   1. [Queries](#queries) _(Lines 459-465)_
   1. [Paths and Destinations](#paths-and-destinations) _(Lines 468-476)_
   1. [Structured Payloads](#structured-payloads) _(Lines 479-485)_
1. [Process Lifecycle](#process-lifecycle) _(Lines 488-490)_
   1. [Fast Start and Graceful Stop](#fast-start-and-graceful-stop) _(Lines 493-499)_
   1. [Fail Fast Under Supervision](#fail-fast-under-supervision) _(Lines 502-508)_
   1. [Stateless Processes](#stateless-processes) _(Lines 511-516)_


---

## Thesis
<!-- Lines 60-72 -->


Design is derived from usage down to code, with effort where error is costly. The system starts as the simplest shape that serves and is cut by the decision each module hides. What crosses a trust boundary is parsed once into a precise form and never reaches an interpreter as code. Each fact has one place, dependencies flow one way, names come from concepts, and a process starts fast, stops cleanly and holds no state it cannot lose: the code is correct at its boundaries and a change touches few places. `CONSTRUCTION`

Four rules hold across the whole branch:

- Untrusted data MUST NOT reach an interpreter as code, command, query, path or object.
- Input MUST NOT be accepted unless it meets the whole of its positive definition of valid.
- Modules MUST NOT form a dependency cycle.
- Loading a module MUST NOT perform an effect.

Strength of grounds: the parse-at-the-edge and data-not-code cores are grounded in consensus and top-tier sources. The structure rules (shape, modularity, layering, naming) rest on practitioner essays and maintainer practice, with no controlled evidence. Each node says where it is inferred or open. Where a node gives a condition under which another practice is best, it appears as "Best instead when". Compatibility verification belongs to [Interfaces and Contracts](assurance_interfaces_data.md#interfaces-and-contracts); this file holds the form a boundary takes.

## Map
<!-- Lines 75-88 -->

| Section | What it decides |
|---|---|
| [Design Derivation](#design-derivation) | Order, timing and sizing of design decisions |
| [System Shape](#system-shape) | One unit or several, where boundaries go, teams |
| [Information Hiding and Modularity](#information-hiding-and-modularity) | How modules are cut, layers, schema ownership |
| [Boundary Contracts and Call Shape](#boundary-contracts-and-call-shape) | Parsing, validity, contracts, interface form, errors |
| [State, Values and Load-Time Effects](#state-values-and-load-time-effects) | One place per fact, normal form, caches, exact values |
| [Dependency Direction](#dependency-direction) | No cycles, declared layering |
| [Naming](#naming) | Whole words, one concept one name |
| [Paradigm and Placement of Logic](#paradigm-and-placement-of-logic) | Paradigm per part, where logic lives |
| [Keeping Data From Becoming Code](#keeping-data-from-becoming-code) | Code, queries, paths, payloads |
| [Process Lifecycle](#process-lifecycle) | Start, stop, fail, stateless |

## Design Derivation
<!-- Lines 91-93 -->

Design is derived from what the system must do down to code. Effort goes to decisions costly to get wrong, taken no earlier than the product is understood. Required properties lead, constraints that induce them are tested against every change, and the design is sized for a stated horizon. `CONSTRUCTION.DESIGN`

### Derivation Order
<!-- Lines 96-104 -->

Derive the design from the outside in and from the costly to the cheap to reverse: usage and scenarios, data flow, structure of stored data, shape of the system, implementation strategy, and only then code. The order follows how decisions depend on each other, so what is costly to change is decided against real usage.

- MUST decide the data structure and the system boundaries against stated usage before the code that depends on them is kept.

Best instead when: test-first or emergent design, for parts cheap to reverse (internal logic, small modules) once the frame exists; a throwaway probe to learn usage, never kept as the result.

Carries out the probable-use stance of [Speculative Building and Probable Use](ownership_stance_selection.md#speculative-building-and-probable-use). Inferred: one maintainer claim plus the reversal-cost argument; no source measures the order. `CONSTRUCTION.DESIGN.1`

### Effort and Timing on Costly Decisions
<!-- Lines 107-115 -->

Architecture is the shared understanding of the decisions that are costly to get wrong, and design effort is spent there. A hard-to-reverse decision is taken as late as the product's understanding allows, and no later than the point where deferring it costs more than deciding. When it cannot wait, weigh the probable use without speculative optimisation. Cheap decisions stay cheap.

- MUST record a hard-to-reverse decision with its reason.

Best instead when: deciding early, if the decision cannot be deferred (an interface already published) or a platform imposes it.

Service boundaries wait on this rule: see [Placing Service Boundaries](#placing-service-boundaries). The "no later than deferral costs more" clause is inferred. `CONSTRUCTION.DESIGN.2`

### Properties First, Then Constraints
<!-- Lines 118-124 -->

Choose the required properties first, stated so they can be checked. Then adopt the architectural constraints that induce them, and test each proposed change against those constraints. A constraint that can be checked mechanically is a blocking check, enforced under [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped).

- MUST name the property a constraint serves.

A constraint adopted by habit or fashion, with no property behind it, is never best. Declared layering is how these constraints are carried out: [Declared Layering](#declared-layering). Strength is moderate: the two sources come from one body of design writing. `CONSTRUCTION.DESIGN.3`

### Growth Horizon
<!-- Lines 127-135 -->

Size the structures costly to reverse (stored data layout, partitioning, system shape, published interfaces) for a stated growth horizon, commonly about ten times the present need, and write down the horizon and the measured signal that will end it. Parts cheap to change are sized to the present need. Keep parts replaceable behind their boundaries, so replacement goes part by part; a part may be knowingly sacrificial if kept modular.

- MUST state the horizon and the signal for each structure costly to reverse.

Best instead when: a wholesale rewrite, if behaviour is well specified, the old system is small, or the architecture itself is the obstacle (see [Replacement Versus Rewrite](evolution.md#replacement-versus-rewrite)); designing for the final scale now, if that scale is already contracted or the structure cannot change later (stored data at very large size).

The signal comes from [Capacity](operation_response_and_readiness.md#capacity) measurements. Sizing cheap parts to the present need carries out [Speculative Building and Probable Use](ownership_stance_selection.md#speculative-building-and-probable-use). Inferred: the ten-times figure illustrates the principle (an order of magnitude), it is not a measured threshold. `CONSTRUCTION.DESIGN.4`

## System Shape
<!-- Lines 138-140 -->

A system starts as one deployable unit with module boundaries inside, pays the distribution premium knowingly, and consolidates again when its cost outgrows its benefit. Boundaries are placed after the domain is understood, and team structure and module structure are designed together. Inferred as a roll-up: practitioner essays, no controlled evidence. Team count and independence of release move the answers here. `CONSTRUCTION.SYSTEM_SHAPE`

### Initial Shape, One Unit or Several
<!-- Lines 143-151 -->

A new service starts as one deployable unit with module boundaries inside. A unit is split out only when a named force requires it: independent scaling, independent release by separate teams, fault isolation that matters, or a different runtime need.

- MUST state the force that justifies a split.

Best instead when: services from the start, if the domain boundaries are already known (rebuilding an existing system), the team has experience building a system of services, and, inferred, several teams must release independently from day one on a platform that already exists. Copying large-organisation patterns in a small team is never a reason.

The inside of the first unit is cut by business concept ([Cut by Business Concept or by Layer](#cut-by-business-concept-or-by-layer)); a split follows [Placing Service Boundaries](#placing-service-boundaries), is paid by [Distribution Premium and Its Reversal](#distribution-premium-and-its-reversal), and follows team lines per [Teams and Structure](#teams-and-structure). Grounded for the direction (majority of practitioner sources, case studies); the list of split triggers is inferred. `CONSTRUCTION.SYSTEM_SHAPE.1`

### Distribution Premium and Its Reversal
<!-- Lines 154-162 -->

Before a unit is split off, the premium is budgeted and in place: automated deployment, monitoring, failure handling, and a stated answer to eventual consistency. The shape is not a one-way door: when operating cost grows with the number of units faster than the benefit, units are consolidated, accepting less fault isolation.

- MUST have deployment automation, monitoring and failure handling before a split goes live.

Best instead when: never consolidating, only where fault isolation or independent scaling is worth more than the operating cost. Splitting now and building the premium later is never best: the failure modes arrive first.

Requires the [Automated Deployment Path](change_flow_delivery.md#automated-deployment-path). Grounded for the premium; the consolidation rule is inferred (one case study, no source states it as a rule). `CONSTRUCTION.SYSTEM_SHAPE.2`

### Placing Service Boundaries
<!-- Lines 165-173 -->

Place a boundary between deployable units only once the domain is understood, because moving functionality across a boundary costs far more than within a unit. Units across a boundary are designed to deploy independently, without lock-step upgrades. Two units that can only ever change and deploy together are a boundary in the wrong place: merge them or move the boundary.

- MUST NOT place a unit boundary before the domain is understood without recording why.

Best instead when: a coordinated breaking change across the boundary, for few, in-house, reachable consumers, as [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible) allows.

Carries out independent deployability ([What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible)) and the compatibility checks of [Contract Tests](assurance_interfaces_data.md#contract-tests). Inferred: "lock-step signals a misplaced boundary" follows from the two positions, no source states it. `CONSTRUCTION.SYSTEM_SHAPE.3`

### Teams and Structure
<!-- Lines 176-183 -->

Design team boundaries and module boundaries together, because structure follows the communication structure that exists. A team is organised around a capability with the skills to deliver it end to end, not around a technical layer; individuals need not be generalists. A typical change then completes inside one team and one module.

- MUST design team boundaries and module boundaries together.
- MUST organise a team around a capability, not around a technical layer.

Best instead when: layer teams, if a layer is a scarce specialism shared by all capabilities and handoffs are cheap (inferred). With a single team the principle applies to its module boundaries only. Independent support is thin (one essay collection). `CONSTRUCTION.SYSTEM_SHAPE.4`

## Information Hiding and Modularity
<!-- Lines 186-188 -->

Modules are cut by the decision each hides, along business concepts first with layer separation inside a module, and a stored schema has one owner. A change to one decision then touches one module. Hidden decisions are kept apart by the one-way rules of [Dependency Direction](#dependency-direction). `CONSTRUCTION.HIDING`

### Cut by Hidden Decision
<!-- Lines 191-200 -->

Put each difficult or likely-to-change decision behind one module boundary and expose only what others need, at every level at which something can be exposed. For each interface, state whether it hides a representation behind operations or varies its implementation per instance behind a common set of operations; an interface does not conflate the two.

- MUST expose only what consumers need.
- MUST NOT cut a module by processing step where the step is the likely-to-change decision.

Best instead when: a cut by processing step, where the steps are themselves the stable concept (a fixed pipeline of transformations; inferred). No evidence favours one hiding style for all interfaces: state which, do not prefer one (open).

A cycle makes two modules one decision unit ([No Cycles](#no-cycles)). Containing a dependency behind a boundary carries this out ([Containment and Exit](ownership_lifecycle_containment.md#containment-and-exit)). Grounded as a principle by a single long-standing source, without effect evidence. `CONSTRUCTION.HIDING.1`

### Cut by Business Concept or by Layer
<!-- Lines 203-209 -->

Cut the system primarily by business concept, each module with a public interface, with layer separation ([Separating Presentation, Domain and Data Access](#separating-presentation-domain-and-data-access)) inside the module. A large domain is not forced under one unified model: split it into bounded contexts with explicit mappings between them.

- MUST give each business-concept module a public interface.

Best instead when: layers as the primary axis, if changes cluster by technology (replacing a whole presentation technology) or the system has one business capability (inferred); one unified model, for a small domain with one meaning per term. Inferred: one practitioner case plus a consensus statement; "changes cluster by concept" is not measured. `CONSTRUCTION.HIDING.2`

### Separating Presentation, Domain and Data Access
<!-- Lines 212-218 -->

Keep domain logic free of presentation and storage entanglement, so users, tests, batch jobs or other programs can drive it, and so it can run without the real presentation or store behind a replaceable interface. Layers couple through narrow interfaces. A part with no domain logic, a thin pass-through of data, gets no separate domain layer.

- MUST NOT let domain logic depend on presentation or storage details.

Best instead when: presentation and domain in one place, for a throwaway or single-presentation script whose rules will never be reused; a mandatory layer for every system is never best (inferred). Database access sits behind this layer ([Order and Compatibility With Running Code](change_flow_data_and_measure.md#order-and-compatibility-with-running-code) relies on it). Grounded (one family of design sources); the pass-through exception is inferred. `CONSTRUCTION.HIDING.3`

### Data Ownership by One Application
<!-- Lines 221-230 -->

Each schema has one owner who alone changes it. Other parties reach the data through an interface the owner publishes, never by binding to the base structures. A store shared by several applications through base structures is not an integration mechanism: every change then needs every consumer.

- MUST name one owner per schema.
- MUST NOT expose base structures to a consumer other than the owner.

Best instead when: a shared store, only for a short-lived transition or a single consumer maintained by the same people, with the structure documented as a contract (inferred).

The form of the published interface is decided in [The Contract Over Stored Data](#the-contract-over-stored-data). Integrity rules declared in the store presuppose this single owner ([Where Integrity Rules Live](assurance_interfaces_data.md#where-integrity-rules-live)). `CONSTRUCTION.HIDING.4`

## Boundary Contracts and Call Shape
<!-- Lines 233-235 -->

What crosses a trust boundary is parsed once into a precise form under a positive definition of valid. A boundary is an explicit contract readable without the producer's code. Stored data reaches several consumers only through a published interface. A call carries meaning and can change, and a failure is explicit. Code past a boundary may rely on what it receives. This section holds the form a boundary takes; [Interfaces and Contracts](assurance_interfaces_data.md#interfaces-and-contracts) holds how compatibility is verified. Consumer reach moves the contract and stored-data decisions. Grounded for the parse-at-the-edge core; the rest is inferred. `CONSTRUCTION.BOUNDARY`

### Parse or Validate at the Edge
<!-- Lines 238-247 -->

Convert every datum that crosses a trust boundary once, at the boundary, into the most precise representation the code needs, rejecting what does not fit, before any of it is acted on. This covers data from internal services, queues, stored records and third-party responses. Code past the boundary relies on that representation. A check done by the untrusted party does not count as the boundary. Coercion is decided per boundary, strict by default.

- MUST parse at every trust boundary before use.
- MUST NOT rely on a check performed by the party being checked.

Best instead when: coercing parsing, where the source cannot produce the type; always strict, for a machine API; trusting internal sources unchecked, only where producer and consumer are one release and one owner (inferred). Validation scattered through the code is never the defence; it remains for rules that depend on current state, which are domain rules.

Uses the definition in [What Counts as Valid](#what-counts-as-valid); the parsed form is the single source other forms derive from ([One Place per Fact](#one-place-per-fact)); carries out the integrity rules beside store constraints ([Where Integrity Rules Live](assurance_interfaces_data.md#where-integrity-rules-live)). `CONSTRUCTION.BOUNDARY.1`

### What Counts as Valid
<!-- Lines 250-257 -->

Valid is defined by a positive rule (an allowlist of values, a pattern, a range, a comparison with an expected structure), and everything else is rejected. Validity covers syntax and meaning, including combinations of related fields. Keep input languages simple enough to be recognised completely before anything is computed from them. A credential or token is valid only if every step its specification requires passes; otherwise it is rejected whole.

- MUST define valid positively.
- MUST reject a credential or token whole unless every cryptographic and validation step its specification requires passes.

Best instead when: denylisting, never as the sole rule (a second layer after an allowlist that cannot be complete). Hand-written pattern lists for complex languages are unreliable and never best. The recogniser rule is one source's position. `CONSTRUCTION.BOUNDARY.2`

### What a Contract States
<!-- Lines 260-271 -->

A data contract is an explicit artifact, readable without the producer's source, stating structure and meaning: names, types stated logically, nullability, units, invariants, an owner, and the version or change-log form that the compatibility policy sets for the consumer reach. Each contract has one owner, one authoritative provider description and a lifecycle status. Its concrete types in each tier are derived, never hand-copied ([One Source of Description](assurance_interfaces_data.md#one-source-of-description)).

- MUST state structure and meaning without the producer's source.
- MUST give each contract one owner.

Best instead when: a contract kept in the producer's code, never for an interface with more than one consumer; the full data-engineering contract format for one application database, only when data leaves the application for a platform team.

Carries out the compatibility policy of [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible); the deprecated and retired statuses rely on [Decommissioning](evolution.md#decommissioning).

Open point: the checklist reading of the data-engineering contract format is not settled by the sources read; the checklist above is the inferred form. `CONSTRUCTION.BOUNDARY.3`

### The Contract Over Stored Data
<!-- Lines 274-282 -->

The interface through which consumers reach a store ([Data Ownership by One Application](#data-ownership-by-one-application)) takes one of two forms. When one application owns the store and all access passes through it, that application's interface is the contract. When several consumers need the data, the owner publishes an application interface by default, or a dedicated published layer in the store where consumers need direct query access or privileges must be separated in the store itself.

- MUST serve several consumers through an application interface unless they need direct query access or privileges must be separated in the store.

Best instead when: an application interface in front of a single owning application, never (it adds a layer and a second place for logic); direct access to base structures, only while there is one owner, since otherwise the base structures become the contract and ossify.

The form of the published layer, read surface or operation, is decided in [Call Shape and Evolvable Interfaces](#call-shape-and-evolvable-interfaces); it carries out [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible). Inferred and contested (one source family against one practice); the conditions are the source claim's own condition made explicit. `CONSTRUCTION.BOUNDARY.4`

### Call Shape and Evolvable Interfaces
<!-- Lines 285-294 -->

Choose the form of an interface by who composes the result. Use an operation with a signature where the consumer asks a question or requests a change and the owner composes the answer. Use a shape-bound read surface where consumers must filter, join and aggregate the result themselves. Writes always go through operations. In both forms output evolves additively, a call carries meaning by name, and the interface is strict for callers it controls and tolerant for providers it does not control.

- MUST evolve an interface's output additively, and remove only under the rule of [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible) for the consumer reach.
- MUST NOT generate consumers from the full schema of a provider the consumer does not control; own-provider stubs follow [One Source of Description](assurance_interfaces_data.md#one-source-of-description).

Best instead when: a shape-bound surface, for read-only reporting with several consumers and for introspection or throwaway owner use; a signature everywhere loses composability where consumers filter and join; generating consumers from the full producer schema, where producer and consumer release together or drift detection matters more than uptime. Fully tolerant parsing of data that feeds an interpreter is never best: validate what you use.

A call carries its meaning by name: see [Naming](#naming). Inferred: the form rests on the maintainer's claim alone, so the decision rests on who composes the result; the tolerant-reader family is grounded. `CONSTRUCTION.BOUNDARY.5`

### Errors at the Boundary
<!-- Lines 297-304 -->

A failure is explicit, never silent. Mandatory inputs are validated first, and an error names the component and offending values and carries a stable code. Scope detail to the audience: full detail goes to the log and to a trusted caller; an untrusted caller receives the stable code and field names, never secrets or internals. A response that fails its own declared output is a defect of the producer, answered with a server error and an alert, never a malformed body.

- MUST give an error a stable code.
- MUST NOT return a malformed body as a success.

Best instead when: echoing offending values to every caller, only where the caller is trusted and the values are not sensitive. Repairing a malformed output silently is never best. A violated store constraint is mapped to a stable contract error here ([Where Integrity Rules Live](assurance_interfaces_data.md#where-integrity-rules-live)). Returning the stable code and field names to untrusted callers is inferred. `CONSTRUCTION.BOUNDARY.6`

## State, Values and Load-Time Effects
<!-- Lines 307-309 -->

Each fact has one authoritative place; stored relational data is normalised and denormalised only for measured need; shared derived state is treated as derived, with a plan; values state their precision and changeability; loading a module has no effect. State cannot silently drift and loading code cannot change behaviour. `CONSTRUCTION.STATE`

### One Place per Fact
<!-- Lines 312-318 -->

Each fact has one authoritative place, and every other representation is derived from it: generated, computed, or a managed copy under the synchronisation plan of [Derived Data Sync and Staleness](assurance_interfaces_data.md#derived-data-sync-and-staleness). Type definitions repeated across tiers are derived as [One Source of Description](assurance_interfaces_data.md#one-source-of-description) holds.

- MUST derive every other representation of a fact from its authoritative place.

Best instead when: duplicating for performance or independence, with a plan and a detection (it is then derived data). Duplicating for convenience without a plan is never best. Grounded for shared data, inferred for application state. `CONSTRUCTION.STATE.1`

### Normal Form for Stored Data
<!-- Lines 321-327 -->

Design relational tables to the normal form that removes the update anomalies of their actual dependencies: third normal form by default, repeating groups moved to a child table, and a higher form where candidate keys overlap or independent multi-valued facts share a table. Denormalise only for a measured performance requirement, with the redundancy guarded by the plan of [Derived Data Sync and Staleness](assurance_interfaces_data.md#derived-data-sync-and-staleness), and prefer a derived read structure over distorting the base tables.

- MUST NOT denormalise without a measured performance need.

Best instead when: denormalising, once a measured requirement exists and the guard is in place; by anticipation it is never best. A higher form chosen without the dependency that needs it adds nothing. Applies to relational storage; for other stores [One Place per Fact](#one-place-per-fact) holds. The use of higher forms driven by dependencies is inferred. `CONSTRUCTION.STATE.2`

### Shared Derived State
<!-- Lines 330-336 -->

A cache is derived state, never the source of truth or permanent storage. It has an owner, an explicit expiry or invalidation plan, and versioned or prefixed keys. State read by several processes lives in a cache they share. A per-process cache is used only for data whose divergence is tolerable within a stated staleness.

- MUST give every cache an expiry or invalidation plan.

Best instead when: a per-process cache, for immutable or short-lived data and for a single process. A cache with no plan is never best. The cache is a derived copy under [One Place per Fact](#one-place-per-fact) and needs the plan of [Derived Data Sync and Staleness](assurance_interfaces_data.md#derived-data-sync-and-staleness). The invalidation rule is inferred. `CONSTRUCTION.STATE.3`

### Value Precision and Mutability
<!-- Lines 339-347 -->

A numeric type carries exactly only the values within its precision and range. A value beyond them (money, counters, identifiers) uses a type that represents it exactly, and equality of rounded values is not restored by an arbitrary fixed tolerance. State whether a value cannot change at all or may be changed only by some holders, and enforce what is stated.

- MUST use an exact representation for values beyond a type's precision.

Best instead when: a tolerance, if the quantity is a measurement with a known error and the bound comes from that error.

Open point: no source read states a preference between immutability and restriction; none is made here. The tolerance point rests on one source; the positive statement is inferred. `CONSTRUCTION.STATE.4`

### Load-Time Effects
<!-- Lines 350-356 -->

Where a language runs module code when the module is loaded, loading does nothing beyond constructing its own definitions: no input or output, registration, connection or global change. Effects happen in explicit start-up steps called from the program's entry point, so loading order never changes behaviour.

- MUST NOT perform effects in module-load code.

Best instead when: registration on load, where the platform's design mandates it and the order is irrelevant (inferred). Holds only for languages that run module code at load time. Load order must not decide behaviour, which refines [No Cycles](#no-cycles). Grounded as a hazard in two language families, the general rule is inferred; mechanics belong to the stack guidelines. `CONSTRUCTION.STATE.5`

## Dependency Direction
<!-- Lines 359-361 -->

Dependencies between modules form an acyclic graph at each level, and the allowed directions between kinds of module are declared and checked on every change. A change propagates predictably and order never decides whether code works. Inferred as a roll-up. `CONSTRUCTION.DEPENDENCY_DIRECTION`

### No Cycles
<!-- Lines 364-370 -->

Modules do not depend on each other in a cycle across module boundaries. Remove a cycle by extracting the shared part into a module both depend on, or by inverting one dependency through an abstraction owned by the depended-upon side. A cycle inside one module, one hidden decision, is not a violation. Each module can then be understood, tested and changed with only the modules below it.

- MUST NOT create a dependency cycle across module boundaries.

Best instead when: a cycle, only inside one module whose parts are one decision; that a mechanism is supported is no reason to use it. A cycle makes two modules one decision unit ([Cut by Hidden Decision](#cut-by-hidden-decision)); acyclicity is one of the rules checked in [Declared Layering](#declared-layering). Inferred: no source measures the cost of a cycle. `CONSTRUCTION.DEPENDENCY_DIRECTION.1`

### Declared Layering
<!-- Lines 373-383 -->

Where the design states which kinds of module may depend on which, declare that rule in a checkable form and enforce it by a blocking check on every change. A layering that is only convention is not a rule. Whether a codebase needs a layering at all is decided in [Properties First, Then Constraints](#properties-first-then-constraints).

- MUST make a declared layering a blocking check.

Best instead when: convention or review alone, only when the rule cannot be expressed as a check.

Requires the layers of [Separating Presentation, Domain and Data Access](#separating-presentation-domain-and-data-access); carries out [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped).

Open point: as a standalone principle the sources read leave it open; it is grounded only through the settled mechanical-enforcement rule. `CONSTRUCTION.DEPENDENCY_DIRECTION.2`

## Naming
<!-- Lines 386-388 -->

Names are whole words, one concept has one name used consistently, and a name is derived from the concept it covers and defined where it is shared. A newcomer recovers the concept from the name. Inferred: the experiments are in one language and their transfer is inferred. `CONSTRUCTION.NAMING`

### Whole Words
<!-- Lines 391-397 -->

Name identifiers with whole words, not single letters or letter-deleting abbreviations, except where the abbreviation is itself the established term of the domain and its audience. Defects are found faster and a reader does not decode names.

- MUST NOT shorten a name by deleting letters, except an established term of the domain and its audience.

Best instead when: short names, for established domain terms and tiny scopes where the meaning is local and visible (inferred). Grounded by one experiment in one language; transfer is inferred. `CONSTRUCTION.NAMING.1`

### One Concept One Name
<!-- Lines 400-406 -->

Give one concept one name, made of common descriptive words, and use it the same way in code, data, interfaces and documents. Searching for a concept then finds all of it, and no two concepts share a name.

- MUST use one name per concept across all artifacts.

Synonyms for variety are never best. The rule binds documents as well as code ([Documentation Practice](transverse_documentation.md#documentation-practice)). Inferred: holder positions of style guides, no effect evidence. `CONSTRUCTION.NAMING.2`

### Names Derived from Concepts
<!-- Lines 409-415 -->

Derive a name from the concepts it covers: select the concepts, choose a word for each, compose. A shared name carries a definition where it is introduced. Test names on a newcomer, who should recover the concept. Names within a family are hierarchical and unambiguous.

- MUST define a shared name where it is introduced.

Best instead when: the first word that comes to mind, for a local, short-lived name only. This is the naming half of [Derivation Order](#derivation-order). Inferred: a single experiment and the maintainer's naming test. `CONSTRUCTION.NAMING.3`

## Paradigm and Placement of Logic
<!-- Lines 418-420 -->

The paradigm is chosen per part by what the problem is, and logic is placed by the property it must have: holds across writers, changes with the product, is fast to test, or acts on data in place. Inferred as a roll-up. `CONSTRUCTION.PARADIGM`

### Paradigm by Intent
<!-- Lines 423-429 -->

Choose the programming paradigm per part by what the problem is, mixing paradigms deliberately at stated boundaries, and never on a defect-rate claim for a paradigm. The code takes the shape of the problem it solves.

- MUST NOT mandate a paradigm on a defect-rate claim.

Best instead when: choosing by defect rate, only when a paradigm-level effect on defects is shown inside one language. Applies the fit-over-novelty rule of [Fit, Maturity and Novelty](ownership_stance_selection.md#fit-maturity-and-novelty) to paradigms, and presupposes the hiding style an interface offers ([Cut by Hidden Decision](#cut-by-hidden-decision)). Inferred from the absence of evidence scoped to a paradigm choice; the defect-rate fact is contested. `CONSTRUCTION.PARADIGM.1`

### Placement of Domain Logic
<!-- Lines 432-441 -->

Place each piece of logic by the property it must have. Where an integrity rule lives is held in [Where Integrity Rules Live](assurance_interfaces_data.md#where-integrity-rules-live). Other domain logic that changes with the product, is branching or algorithmic, or must be tested fast lives in the application first; a proven hot spot moves into the data tier as a set-based query. Scheduled work runs where the data lives only when it acts on that store's state as bounded statements and needs no operating-system commands, no retries beyond a rerun and no cross-system dependencies; otherwise it runs in the application tier or an orchestrator. Scheduled work is monitored.

- MUST test logic placed in the store against a real store ([Tests Without Durable Effect on Data](assurance_behaviour.md#tests-without-durable-effect-on-data)).
- MUST monitor scheduled work ([Scheduled Work Signals](operation_objectives_and_signals.md#scheduled-work-signals)).

Best instead when: database-first, for invariants across writers and for set-based data transformations; an external orchestrator for every job, for multi-system pipelines and jobs with retries and dependencies (it costs one more system to run for a bounded in-store job). Application-only for invariants is never best: it leaves migrations and ad-hoc access unguarded. Team comfort with the store's language moves the answer.

Depends on the layer isolation of [Separating Presentation, Domain and Data Access](#separating-presentation-domain-and-data-access). Bound to a store with a query language, not to a programming language. Inferred: the scheduler clause is single-source maintainer practice, the application-first clause is contested, the set-oriented clause has no source. `CONSTRUCTION.PARADIGM.2`

## Keeping Data From Becoming Code
<!-- Lines 444-446 -->

Every sink that interprets data as code, a command, a query, a path, a destination or a serialised object is treated as dangerous. Data reaches it only as data, hostile data is narrowed at each sink, and a second layer of least privilege and containment ([Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access)) limits what slips through. Sink narrowing presupposes that boundary data was parsed first ([Parse or Validate at the Edge](#parse-or-validate-at-the-edge)) and refines [What Counts as Valid](#what-counts-as-valid). Grounded: the children rest on consensus and top-tier sources. `CONSTRUCTION.DATA_NOT_CODE`

### Code and Commands
<!-- Lines 449-456 -->

Never build code from strings: dynamic evaluation of attacker-influenced text executes it with the caller's privileges, and a template system that evaluates expressions makes template source code, not data. Start a process without a shell and with a program not chosen by input, prefer library functions to operating-system commands, and where a command is unavoidable allowlist the executable and its arguments and run it with least privilege.

- MUST NOT evaluate attacker-influenced text as code.
- MUST NOT start a process through a shell with input-derived text.

Escaping or sanitising input that will be evaluated is never the defence. Where a product must run user-authored logic: a restricted language recognised by a parser ([What Counts as Valid](#what-counts-as-valid)), confined with least privilege (inferred; the sources do not cover it). Grounded for the rule (four top-tier sources). `CONSTRUCTION.DATA_NOT_CODE.1`

### Queries
<!-- Lines 459-465 -->

A query reaches its engine as fixed text plus separately passed values, in every store, SQL or not. Untrusted values are never concatenated or templated into the text. Identifiers, keywords and sort order are redesigned or mapped through a fixed allowlist. The application's store account has least privilege as a second layer.

- MUST NOT build query text from untrusted values.

Best instead when: escaping, only as a last layer where a parameter cannot be used (inferred; fragile, not guaranteed). Grounded. `CONSTRUCTION.DATA_NOT_CODE.2`

### Paths and Destinations
<!-- Lines 468-476 -->

A file location chosen from input stays inside its base directory: build paths from internally generated or trusted names, use user-supplied names only under strict allowlist validation, and check containment on the resolved location actually used. A server fetches only destinations it allows: match the host against an allowlist, validate the resolved addresses against the permitted networks, connect only to the validated address, and re-check redirect targets.

- MUST check containment on the resolved location used.

A hostname check alone is never enough: the name can resolve elsewhere. Relies on the bounds of [Bounding Runtime Effect and Untrusted Responses](ownership_lifecycle_containment.md#bounding-runtime-effect-and-untrusted-responses).

Open point: no source read grounds "checked after resolution and used without a race"; it is kept as the logical form of the containment check (inferred). `CONSTRUCTION.DATA_NOT_CODE.3`

### Structured Payloads
<!-- Lines 479-485 -->

Data crossing a trust boundary is exchanged in a pure data format that carries neither types nor code, and is never deserialised into executable structures. When the expected messages are known, sign serialised data and verify before deserialising, and populate a new object from validated fields. Parse an untrusted document with embedded definitions and external references disabled. Where two components read the same bytes their parsers must agree, so control and delimiter characters that can alter structure never reach a field value.

- MUST NOT deserialise untrusted data into executable structures.

Best instead when: native object serialisation, only inside one trust zone where both ends are one release (inferred). The payload must not become code, the rule of [Code and Commands](#code-and-commands). Grounded for the format and XML rules; the signing step and the protocol rule are single-source. `CONSTRUCTION.DATA_NOT_CODE.4`

## Process Lifecycle
<!-- Lines 488-490 -->

A process starts fast, stops on request without losing work, ends on a failure it cannot repair and is restarted by something outside it, and holds no state that cannot be lost. Any process can be replaced or added at any time, which is how [Capacity](operation_response_and_readiness.md#capacity) grows. Scope: hosted services. Inferred: one operations-practice family and one runtime page. `CONSTRUCTION.PROCESS`

### Fast Start and Graceful Stop
<!-- Lines 493-499 -->

A process starts in seconds. On a request to stop, it stops accepting new work, finishes or returns its in-flight work, and exits; work that cannot finish within the stop window is checkpointed or resumable. Releases and scaling are cheap and no work is lost.

- MUST handle a stop request without dropping in-flight work.

Best instead when: slow-start processes, where a start cost is unavoidable (a large in-memory model); the cost is then budgeted in release and scaling plans (inferred). Fast replacement needs [Stateless Processes](#stateless-processes); instance replacement during a release relies on this ([Automated Deployment Path](change_flow_delivery.md#automated-deployment-path)). The checkpoint clause is inferred. `CONSTRUCTION.PROCESS.1`

### Fail Fast Under Supervision
<!-- Lines 502-508 -->

After a failure the program cannot repair, its state is undefined: it records the failure, releases what it owns and ends. Restarting is the job of something outside it. Failures the program can repair are handled where they occur.

- MUST end the process after an unrepairable failure and record it.

Continuing after an unrepairable failure is never best. Restart loops with no alert are never best; the supervisor's restart policy and crash-loop alert belong to operation. Relies on [Fast Start and Graceful Stop](#fast-start-and-graceful-stop). Grounded for the one runtime whose documentation states it; the general principle is inferred. `CONSTRUCTION.PROCESS.2`

### Stateless Processes
<!-- Lines 511-516 -->

A process holds no state that cannot be lost or rebuilt: session and durable state live in external stores, processes share nothing, and a request does not depend on reaching a particular process. Stickiness is at most a performance optimisation with a correct fallback.

- MUST NOT keep authoritative or session state only in a process.

Sticky sessions as the state mechanism are never best. Derived state held in memory, such as a cache ([Shared Derived State](#shared-derived-state)), is allowed because it can be rebuilt; where "rebuildable" ends is inferred. `CONSTRUCTION.PROCESS.3`
