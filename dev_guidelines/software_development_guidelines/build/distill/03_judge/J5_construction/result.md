# J5_construction: result

## L1 headline

J5_construction judged all 48 nodes of CONSTRUCTION (the L1 node as a provisional index, 10 L2, 37 L3); records in `judged.md`. Pinned: nodes judged 48; decisions marked undecided: none; flags raised: 9 (F1 to F9; F6 and F8 settled by review, 7 carried); review fixes applied: 16 of 16; settled decisions disagreed with: none (two seams checked consistent: CONTRACTS.1 against SYSTEM_SHAPE.3, CONTRACTS.3 against BOUNDARY.3). The contested nodes were decided by property, not by camp: interfaces by signature unless consumers must compose a read surface (F1), logic placed by what it must guarantee (F2), store as contract only for several direct consumers or privilege separation, normalisation by the dependencies actually present, one deployable unit first (grounded for direction, inferred for triggers).

## L2 claims

Pinned (word for word at every level): nodes judged: 48 (CONSTRUCTION; DESIGN .1-.4; SYSTEM_SHAPE .1-.4; HIDING .1-.4; BOUNDARY .1-.6; STATE .1-.5; DEPENDENCY_DIRECTION .1-.2; NAMING .1-.3; PARADIGM .1-.2; DATA_NOT_CODE .1-.4; PROCESS .1-.3). Decisions marked undecided: none. Flags raised: 9 (F1 to F9; F6 and F8 settled by review, 7 carried). Review fixes applied: 16 of 16. Settled decisions disagreed with: none.

Each claim is marked grounded (named sources support it), inferred (follows from them) or open.

DESIGN
- Derive from usage outward, in order of cost of reversal; test-first or emergent design fills the cheap parts, a probe may learn usage, never ships as the keeper. Inferred (one maintainer row plus the reversal-cost argument).
- Effort goes where error is costly; hard-to-reverse decisions are taken as late as understanding allows. Grounded (two consensus rows); the "no later than deferral costs more" clause inferred.
- Properties first, then the constraints that induce them, changes tested against them, mechanical where possible. Grounded (consensus).
- Size for a stated horizon (a common heuristic: about 10x), record horizon and signal, keep parts replaceable. Inferred (figures one engineer's aphorism, F4).

SYSTEM_SHAPE
- One deployable unit first; split only for a named force; services-first best when domain known, several independent teams, platform exists. Grounded for direction (practitioner essays, no controlled evidence); services-first also needs team experience of services (REG-1112); other triggers inferred.
- Budget the distribution premium before splitting; consolidate when cost outgrows benefit. Grounded for the premium; inferred for consolidation (one T3 case).
- Boundaries only once the domain is understood, deployable independently; routine lock-step deployment signals a misplaced boundary; coordinated breaking change stays the exception under CONTRACTS.1's condition. Grounded for the two principles; inferred for the lock-step reading (F3).
- Team and module structure designed together, teams around a capability. Grounded as consensus (thin independent support).

HIDING
- Cut by hidden decision, expose only what is needed at every level, state which hiding style an interface offers. Grounded as principle (single T2 source, no effect evidence); inferred for the cross-level extension.
- Primary cut by business concept, layers inside the module; bounded contexts for large domains. Inferred (one practitioner case plus the changeability argument).
- Keep domain logic free of presentation and storage; no layer where there is no domain logic. Grounded (consensus); the exception inferred.
- One owner per schema; shared store not an integration mechanism. Grounded (consensus, one source family).

BOUNDARY
- Parse once at every trust boundary (internal sources and third-party responses included) into a precise form; no re-check past it; explicit coercion per boundary. Grounded (consensus, two T1 sources), including that the untrusted party's own check is not the boundary (REG-1503); sink narrowing stays under DATA_NOT_CODE; F6 settled.
- Valid is defined positively, syntax and meaning, simple input languages, real parsers for complex ones. Grounded.
- A contract is an explicit artifact readable without producer code: units, null against absent, logical types with physical types derived from the place the team records the chain starts (CONTRACTS.3), one owner, lifecycle; versioning is held in CONTRACTS.1. Grounded for core; inferred for derivation and checklist.
- Store as contract: application API when one owner mediates all access; a published interface layer, base structures private, for several direct consumers or privilege separation. Inferred (contested, T3 source family).
- Signature over shape-bound interface, with a reporting exception; names over positions; the output model limits what leaves (split held in CONTRACTS.3); strict for callers you control, tolerant for providers you do not. Inferred (maintainer row contradicts common practice, F1); tolerant-reader family grounded.
- Errors explicit, stable-coded, detail scoped to audience; malformed output is a server defect. Grounded for the core; audience scoping inferred (F9).

STATE
- One authoritative place per fact, copies derived with a sync plan. Grounded for shared data, inferred for application state.
- Normalise to the dependencies present: 3NF default, higher forms when keys overlap or independent multi-valued facts share a table; denormalise only for measured need, with a guard. Grounded for 3NF and denormalisation; inferred for higher forms, Boyce-Codd clause from the definition (F7).
- A cache is derived state with an owner and an invalidation plan; shared across processes unless divergence is tolerable. Grounded for shared against local; inferred for the plan.
- Exact representation beyond a type's precision, no arbitrary tolerance; state immutability or restriction, no preference derived. Grounded for the tolerance point; open for the preference.
- Loading a module has no effect beyond its own definitions, for languages that run code at load. Inferred (F5).

DEPENDENCY_DIRECTION
- No cycles across module boundaries (inside one module acceptable). Inferred.
- A declared layering is a blocking check, never convention. Inferred (rests on the settled enforcement rule RULES.3).

NAMING
- Whole words, except domain-established abbreviations. Grounded for one experiment; transfer and exception inferred (F8).
- One concept one name across code, data, interfaces and documents. Inferred.
- Derive names from concepts, define shared names, test on a newcomer. Inferred.

PARADIGM
- Paradigm per part by intent, never by a defect-rate claim. Inferred (absence of evidence).
- Logic placed by property: invariants across writers in the store (settled), product-changing and fast-test logic in the application, set-based transformations (inferred, no row) and small state-only scheduled work in the data tier, heavy or multi-system work in an orchestrator; team skill breaks ties only. Inferred (F2).

DATA_NOT_CODE
- Never build code from strings; no shell with input-derived text. Grounded (four T1 sources).
- Fixed query text plus separate values in every store, least privilege second layer. Grounded.
- Paths stay in their base directory; fetch only allowed destinations, checked at the connected address. Grounded; the race clause open, kept as inferred.
- Pure data formats, no deserialisation into executable structures, signed when messages known, parsers agree on structure-altering bytes. Grounded for format and XML; single-source for signing and protocol rule.

PROCESS
- Fast start, graceful stop, resumable when it cannot finish. Grounded (one source family); checkpoint clause inferred.
- End on an unrepairable failure, restart by something outside. Grounded for the one runtime documenting it, inferred as a general principle.
- No state that cannot be lost or rebuilt; no sticky sessions as state mechanism. Grounded (one source family).

Flags (word for word; F6 and F8 settled by review): F1 BOUNDARY.5 signature over shape-bound rests only on the maintainer's argument; F2 PARADIGM.2 maintainer leans further to the data tier than any source; F3 SYSTEM_SHAPE.3 lock-step as a boundary defect, confirm reading of the coordinated-deploy practice; F4 DESIGN.4 10x/100x figures single-source; F5 STATE.5 no language-neutral source; F6 BOUNDARY.1 deferred client-side validation half unjudged (settled by review: REG-1503); F7 STATE.2 higher normal forms from definition, not a register source; F8 NAMING.1 single experiment, domain-term exception inferred (settled by review); F9 BOUNDARY.6 audience scoping qualifies the maintainer's row.

## L3 full

The full records (decision, grounds with row and register ids, positions, rejected with the condition under which each would be best, context, certainty, flags, constraints, links) are in `judged.md`, in tree order; this section gives the reasoning that moved the contested nodes and the pin again.

Pinned: nodes judged: 48 (CONSTRUCTION; DESIGN .1-.4; SYSTEM_SHAPE .1-.4; HIDING .1-.4; BOUNDARY .1-.6; STATE .1-.5; DEPENDENCY_DIRECTION .1-.2; NAMING .1-.3; PARADIGM .1-.2; DATA_NOT_CODE .1-.4; PROCESS .1-.3). Decisions marked undecided: none. Flags raised: 9 (F1 to F9; F6 and F8 settled by review, 7 carried). Review fixes applied: 16 of 16. Settled decisions disagreed with: none.

Decided inputs read: ASSURANCE.CONTRACTS.1 to .3, RULES.3 (J2); DATA_INTEGRITY.1, .4, SECURITY.2, .6 (J3); X1 to X3 do not touch a CONSTRUCTION node. OWNERSHIP.STANCE.4 (J1) read to keep DESIGN.2 and DESIGN.4 consistent with it.

Contested nodes, reasoning in brief:
- BOUNDARY.5 (views against functions as interface; maintainer against common practice). The argument that holds: a shape-bound surface lets the owner only add; a signature also takes new inputs with defaults and hides the computation. The argument that limits it: the output shape of a signature is just as bound, and a signature cannot be composed by the consumer. Decision: signature by default; shape-bound for owner-only use and for read-only access consumers must filter and combine (the maintainer's own sub-position a). No outside source; marked inferred and flagged (F1).
- BOUNDARY.4 and HIDING.4 (database as contract). Not a choice of camp: the row's own condition decides. One owning application mediating all access: its interface is the contract, no second layer. Several direct consumers or privilege separation: a published layer in the store, base structures private. Inferred (contested, T3 source family).
- PARADIGM.2 (logic in the database). The settled DATA_INTEGRITY.1 already splits by kind of rule; this node extends the split by the property each logic must have. Application first for product-changing logic (modifiability, test speed), data tier for invariants, set-based transformations and small state-only scheduled work, orchestrator for heavy or multi-system work. The maintainer's scheduler position is kept as the default for state-only jobs, with its own limits as conditions. Inferred (F2).
- SYSTEM_SHAPE.3 (coordinated breaking changes against independent deployability). CONTRACTS.1 settles the condition (few, in-house, reachable consumers). Added only the consequence at the structure level: if lock-step deployment is the routine, the boundary is misplaced. Inferred (F3).
- STATE.2 (normalisation). 3NF default is consensus and agrees with the maintainer; higher forms are condition-driven by the dependencies present (overlapping keys, independent multi-valued facts), not a blanket default. Denormalise only for measured need with a guard (DATA_INTEGRITY.4).
- BOUNDARY.1 (parse against validate). Not different outcomes: validation is the rejecting half of parsing; internal and stored data cross trust boundaries too; re-checking structure deeper is the defect.
- SYSTEM_SHAPE.1 (monolith or services first). Practitioner essays and case studies, no controlled evidence; direction grounded, triggers inferred, with the condition under which services-first is best stated.

Seam noted for the J1 review or wave 3 (not a flag): OWNERSHIP.SERVICES.2 favours explicit major versions for few or controlled consumers, while the settled CONTRACTS.1 favours additive coordinated evolution for few, reachable, in-house consumers; the roles differ (consumer of a rented service against provider of an interface) but a reader may see a conflict.

Language-neutrality: no language mechanism is stated; STATE.5 is a principle scoped to languages that run module code at load, marked inferred; the rows flagged in the skeleton (L1501, L1514, L1288) use the neutral statements recorded there; L1518 stays a stack pointer.
