# Skeleton (stage 5c): js-philosophy and pig-js-defaults

Both graphs of the JavaScript guideline, assembled from the eight branch skeletons: the two roots first, then the
eight branch subtrees (each breadth-first, the L1 node first), then the intentlinks, the inter links, the planned
boundary links and the judge records. Node columns: `| uid | name | intent | epistemic_state | ledger rows |`.

Conventions:

- Epistemic cells write the IG multi-issue separator as `\|`; the `ledger rows` column is derived from `claims_ledger.md`.
- A node with `-` in `ledger rows` rolls up its children (or is an undecided placeholder).
- Cross-branch links were proposals naming a branch keyword; they are resolved to uids here and their provenance is
  in `5c_integrate/link_resolution.md`. Link ids are plain numbers, restarted per table.
- Links to the web-architecture graphs are planned, not created: those graphs do not exist yet.
- Nodes relabelled `risky` (decision on one T3 source): `PIG-JS.STRUCTURE.LOADING.6`, `PIG-JS.STRUCTURE.DIRECTION.2`, `VERIFICATION.TEST_SUITE.3`, `VERIFICATION.TEST_STABILITY.3`. Relabelled `risky` at stage 7: `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` (gates are the build's judgment), `PIG-JS.CONTRACTS.LAYER.1` (decided by the build on mechanism facts and one holder).
- Slot 14_secgap2 (second security gap round) was folded by patch (`build/patch/14_secgap2/`): 17 defaults nodes added, `DOM.2.3`, `INJECTION.5.3` and `INJECTION.6.4` decided from `undecided`, `INJECTION.4.4` kept undecided; decisions in `decisions_for_review.md` section `Slot 14_secgap2`. Its review fixes (17 findings) are recorded in `build/review/patch14/fixes/result.md`.
- Software-guideline split (maintainer decision "if they are core to js , keep them, else, send them to the other session"): of the 108 js-philosophy nodes, 56 were sent to the software development guideline, 9 were split and narrowed, 43 kept; the philosophy graph now has 52 nodes. Links touching sent nodes were removed or retargeted as recorded in `build/handoff/to_software_guideline/result.md`; the package is `build/handoff/to_software_guideline/package.md`.
- Restoration with JavaScript emphasis (maintainer decision: general principles belong to the software development guideline, but those "especially important in JS" stay here, stated as why JavaScript makes them matter more): four philosophy nodes came back (`SUBSET.NUMBERS`, `SUBSET.STATE`, `CONTRACTS.BOUNDARY`, `DEFENSE.CODE`), 2 claims moved back from `deferred`, 20 intentlinks, 1 inter link to the Python philosophy and 6 defaults inter links re-created; the philosophy graph has 56 nodes. Record: `build/handoff/to_software_guideline/kept_with_js_emphasis.md` and `build/handoff/to_software_guideline/recheck/result.md`.

## Graph js-philosophy

### Root

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| ROOT | Solid JavaScript | JavaScript code whose behaviour is predictable, whose changes stay cheap and which resists attack, in the browser and in Node. JavaScript is permissive and widely misused; with strong principles it is made useful and safe by narrowing it to a checked subset rather than by avoiding it. | known | - |

### SUBSET

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| SUBSET | Predictable subset | Code does what its text says: the team writes in a checked subset of a permissive language, so no hidden conversion, silent loss of precision, silent failure, ambient default or surprise mutation decides an outcome. | known \| unvalidated: principle inferred as the roll-up of the PIG-JS.SUBSET decisions | SUBSET-001, SUBSET-002 |
| SUBSET.VISIBLE | Visible conversion | Comparison and conversion are stated where they happen, so what an expression does follows from the declared kind of its operands, not from their values or from a coercion table the reader must recall. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.CONVERSION | - |
| SUBSET.FAILURE | Loud failure | A mistake stops the program at the mistake: code runs in the strictest mode its language offers, in which a misspelt name, a write to a locked value or an unowned receiver raises an error instead of silently changing state. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.STRICTNESS.1, MUTATION.1 and OBJECTS.1 | - |
| SUBSET.BINDING | Enforced binding and access | A name's mutability and reach are declared and enforced by the language, not by naming convention or discipline: bindings are fixed by default, private means unreachable, and the receiver of a call is never implicit. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.STRICTNESS.3, STRICTNESS.4, OBJECTS.1 and OBJECTS.3 | - |
| SUBSET.MATURITY | Settled features | Code uses only language features whose meaning is settled and available on every target, retires deprecated ones, and leaves the language's built-in objects unaltered, because later growth of the language would change what the code means. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.EVOLUTION and OBJECTS.5 | - |
| SUBSET.NUMBERS | One number type, stated limits | JavaScript has one numeric type for everyday arithmetic, a 64-bit binary floating-point number, so every count, identifier and amount shares its precision and range and loses exactness silently beyond them: the limits are stated where a value could exceed them, and exactness beyond them comes from another representation. | known \| unvalidated: intent restated for JavaScript by the build, the general principle is owned by the software development guideline \| unvalidated: inferred roll-up of PIG-JS.SUBSET.NUMBERS | - |
| SUBSET.STATE | Immutability is stated, not assumed | In JavaScript a value is locked only as far as its mechanism reaches: a fixed binding does not freeze the value, a freeze reaches one level and fails silently outside strict code, and some array methods change the array they are called on; so code states which guarantee it relies on, that nobody can change a value or that only some holders may. | known \| unvalidated: intent restated for JavaScript by the build, the general principle is owned by the software development guideline \| unvalidated: inferred roll-up of PIG-JS.SUBSET.MUTATION and PIG-JS.SUBSET.STRICTNESS.3 | - |

### CONTRACTS

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| CONTRACTS | Contracts | Make intent checkable at build time through a type layer, while holding that the layer is a build-time artefact of a language that has no types at run time, so that what the checker passes says nothing about the data that arrives and is never taken as proof; only parsing that data at the trust boundary attests its shape. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | CONTRACTS-005, CONTRACTS-006, CONTRACTS-007, CONTRACTS-008, CONTRACTS-009, CONTRACTS-010 |
| CONTRACTS.STATIC | Static contract | Express expectations as types that a tool checks before the program runs, while holding that a type layer is a build-time artefact of a language that has no types at run time | known | - |
| CONTRACTS.BOUNDARY | Boundary parse is the only attestation | Types are erased before run time and every value from outside (a request, a message, a queue entry, a stored record, parsed text) arrives with no run-time type, so parsing it into the shape the program expects, at every trust boundary and before use, is the only place a value earns that shape; code past the boundary relies on the shape only because the parse happened. | known \| unvalidated: intent restated for JavaScript by the build, the general principle is owned by the software development guideline \| unvalidated: inferred roll-up of PIG-JS.CONTRACTS.BOUNDARY | - |
| CONTRACTS.STATIC.1 | Types attest nothing at run time | Run-time data is checked only by run-time code: types and assertions are erased and say nothing about the values that arrive | known | CONTRACTS-001, CONTRACTS-002 |
| CONTRACTS.STATIC.2 | A passing check is evidence, not proof | The checker is intentionally unsound in places and detects a measured part of defects, so it complements run-time checks and tests and never replaces them | known \| unvalidated: quote tool-extracted; measurement single T2 source, 2017 | CONTRACTS-003, CONTRACTS-004 |

### CONTROL

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| CONTROL | Explicit control of time, failure and resources | Behaviour under delay, error and load stays predictable because every asynchronous operation, failure and resource of a JavaScript program has an owner, a bound and a defined end. | known \| rolls up its five children | - |
| CONTROL.FAILURE | Failure has an owner | A failure in JavaScript travels one of two channels, synchronous throw or asynchronous rejection or event, and a failure nobody observes is lost or escalated by the host; every failure therefore has a named owner who handles it, passes it on with its origin, or lets the program end. Fail fast and never swallow silently are shared with Python and held by the inter link, not copied. | known \| rolls up PIG-JS.CONTROL.PROMISES and PIG-JS.CONTROL.ERRORS; the asynchronous channel rests on one consensus fact | CONTROL-001 |
| CONTROL.BOUNDS | Every wait and every task has a bound and a stopper | Waiting has a time limit and running work has a party that can stop it, because a promise cannot be cancelled and an unbounded wait or task holds resources for as long as its slowest peer. | known \| rolls up PIG-JS.CONTROL.BOUNDS | CONTROL-002, CONTROL-003 |
| CONTROL.SCHEDULING | One shared cooperative thread | All work of a program shares one thread that nothing preempts, with a fixed order between immediate continuations and later tasks and with time only as a lower bound; long work delays every other client, so code states what it needs and never relies on order or precision. | known \| rolls up PIG-JS.CONTROL.SCHEDULING | CONTROL-004, CONTROL-005, CONTROL-006, CONTROL-007, CONTROL-008 |
| CONTROL.FLOW | Producers pace to consumers | Data moves only as fast as its slowest consumer can take it; a buffer threshold is a signal to stop, not a memory bound, so unpaced production costs memory, collection time and latency. | known \| rolls up PIG-JS.CONTROL.FLOW; the cost fact is an illustration from one demo | CONTROL-009, CONTROL-010 |

### STRUCTURE

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| STRUCTURE | Structure for locality of change | Organize code so that a change touches one place: what a module exports is state shared by every importer, because an importer cannot rebind it but can change it, so the sharing is made visible instead of left implicit. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | STRUCTURE-001, STRUCTURE-002, STRUCTURE-003, STRUCTURE-006, STRUCTURE-007, STRUCTURE-008, STRUCTURE-009, STRUCTURE-010, STRUCTURE-011, STRUCTURE-012 |
| STRUCTURE.STATE | Shared state is visible | Make shared state visible as shared: an exported object is state held by every importer. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | STRUCTURE-004 |
| STRUCTURE.STATE.2 | Exported state is shared state | Treat anything a module exports as state shared by all importers, and freeze it or hide it when sharing is not intended. | known \| unvalidated: quote tool-extracted | STRUCTURE-005 |

### DEFENSE

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| DEFENSE | Defense | Input from outside the trust boundary is hostile; JavaScript sharpens this because a permissive language shares one runtime with untrusted code: hostile data must not become live markup in the page or a string that is compiled and run, code and content from another origin stays behind explicit boundaries, a hostile key must not rewrite what every object inherits, and one hostile input must not exhaust the single-threaded process. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | DEFENSE-002, DEFENSE-007, DEFENSE-008, DEFENSE-009, DEFENSE-010, DEFENSE-011, DEFENSE-012, DEFENSE-013, DEFENSE-014, DEFENSE-015, DEFENSE-016, DEFENSE-017, DEFENSE-018, DEFENSE-019, DEFENSE-020, DEFENSE-185, DEFENSE-186, DEFENSE-188 |
| DEFENSE.DOM | Hostile data in the document | Hostile data must never become live markup, script or navigation in the page, and no verdict about it outlives the parse it was made for. | known | - |
| DEFENSE.ORIGIN | Boundaries between origins | Code and content from another origin stays behind explicit, verified boundaries, because every script in a page, first-party or not, holds the whole page's authority. | known | DEFENSE-001, DEFENSE-189 |
| DEFENSE.PROTOTYPE | Hostile keys and the shared object model | A permissive object model lets a hostile key rewrite what every object inherits; keys from outside are untrusted data, and the application, not the runtime, answers for them. | known | - |
| DEFENSE.HOST | The process under hostile input | One hostile input or one hostile peer must not exhaust the single-threaded process or reach what the process can reach; availability and exposure are part of safety. | known | - |
| DEFENSE.CODE | Strings become code in many ways | JavaScript turns a string into running code through many doors (eval, the Function constructor, string arguments to timers, template engines, the vm module), each running it with the caller's privileges, and a template is code too, so template injection reaches the server like code execution; hostile data is therefore never compiled, evaluated or used as a template, whatever API offers it. | known \| unvalidated: intent restated for JavaScript by the build, the general principle is owned by the software development guideline | DEFENSE-007, DEFENSE-188 |
| DEFENSE.DOM.1 | Sources and sinks | Every injection is a flow from an attacker-controlled source to a dangerous sink, so both ends of every flow are audited. | known | DEFENSE-003 |
| DEFENSE.DOM.2 | A verdict holds only for its parse | A filter, sanitizer or gate decides about one parse of the data; safety is lost when a later parse differs, so verdicts are validated in the consumer. | known | DEFENSE-004 |
| DEFENSE.DOM.3 | Script tags are not the only way in | Disabling script execution or blocking handlers does not make markup safe; HTML alone can rewrite the page's names and behaviour. | known | DEFENSE-005, DEFENSE-006 |
| DEFENSE.PROTOTYPE.1 | The application answers for keys | The runtime trusts application input, so validating attacker-influenced keys is the application's job and cannot be left to the platform. | known | DEFENSE-021 |
| DEFENSE.PROTOTYPE.2 | Pollution can be code execution | A polluted shared prototype is read later by legitimate code, so the worst outcome is remote code execution, not a logic error. | known | DEFENSE-022 |
| DEFENSE.HOST.1 | One request can stall the process | Single-threaded execution means CPU spent on one request is stolen from all; untrusted input must not control the cost of a match. | known | DEFENSE-023 |
| DEFENSE.HOST.2 | Heuristics are not proofs | A pattern check that flags or misses vulnerable code is a signal, never a proof either way. | known | DEFENSE-024 |
| DEFENSE.HOST.3 | Two parsers must agree | Where a proxy and the runtime's own HTTP parser read the same bytes, the runtime does not count spec-consistent behaviour as its own flaw, so the defence against any disagreement belongs at both parsers. | known \| unvalidated: rests on single-source claims only \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | DEFENSE-025, DEFENSE-187 |

### DEPENDENCIES

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| DEPENDENCIES | Dependencies | Third-party code runs with the application's full privileges, so each dependency is a trust decision: weighed against the routes by which trust is lost, vetted for maintenance and install-time behaviour before adoption, installed reproducibly, changed deliberately, and judged by evidence whose limits are known. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | DEPENDENCIES-031 |
| DEPENDENCIES.TRUST | Dependencies are trusted code | Whatever enters the dependency graph acts with the application's authority and nothing inside the process contains it, so trust is granted by the act of adding. | known | DEPENDENCIES-006 |
| DEPENDENCIES.THREATS | How trust is lost | Controls aim at the routes by which trusted code turns hostile: takeover of the people and accounts behind a package, and confusion about which package is meant. | known | - |
| DEPENDENCIES.ADMISSION | Admission | A package's maintenance and what it runs at install are weighed before it enters. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | DEPENDENCIES-010, DEPENDENCIES-013, DEPENDENCIES-014 |
| DEPENDENCIES.EVIDENCE | Evidence and its limits | Signals about a package (provenance, signatures, assurance levels, audit findings) are read for what they establish and no further; none is a verdict of safety. | known | - |
| DEPENDENCIES.CHANGE | Controlled change | The tree that was reviewed is the tree that runs, and it changes only by a deliberate, reviewable act. | known \| conflict: see CHANGE.2 | DEPENDENCIES-027, DEPENDENCIES-028, DEPENDENCIES-029, DEPENDENCIES-030 |
| DEPENDENCIES.TRUST.1 | Every dependency is trusted code | Direct or transitive, development or runtime, every package acts with the application's privileges and is vetted as such. | known \| unvalidated: dev-versus-runtime figures rest on a single T2 source | DEPENDENCIES-001, DEPENDENCIES-002, DEPENDENCIES-003 |
| DEPENDENCIES.TRUST.2 | No containment inside the process | The runtime offers no privilege boundary between application code and its dependencies, so no design relies on one. | known | DEPENDENCIES-004, DEPENDENCIES-005 |
| DEPENDENCIES.THREATS.1 | Takeover of maintainership | Four incidents show that control of a maintainer account or of maintainership is a recurring route of compromise, so who maintains a package is a risk to weigh beside flaws in its code. | known \| unvalidated: four incidents; their weight against code flaws is not measured | DEPENDENCIES-007, DEPENDENCIES-008 |
| DEPENDENCIES.THREATS.2 | Confusion is many mechanisms | Package confusion is a family of mechanisms, many semantic, so defences address the namespace and not only spelling. | known \| unvalidated: single T2 source | DEPENDENCIES-009, DEPENDENCIES-085 |
| DEPENDENCIES.ADMISSION.2 | Maintenance as a signal | Adoption weighs how many people maintain a package, how recently, and what it runs at install. | known | DEPENDENCIES-011, DEPENDENCIES-012 |
| DEPENDENCIES.EVIDENCE.1 | Provenance and signatures | Provenance and signatures state origin and integrity; assurance is graded and consumed as such, never read as safety. | known \| unvalidated: rests on single-source claims only | DEPENDENCIES-015, DEPENDENCIES-016, DEPENDENCIES-017, DEPENDENCIES-018, DEPENDENCIES-019 |
| DEPENDENCIES.EVIDENCE.2 | Audit findings | Vulnerability findings are triage input; reachability, not count, measures risk. | known | DEPENDENCIES-020 |
| DEPENDENCIES.CHANGE.1 | Reproducible tree | Every install resolves the same tree because the lockfile, not the manifest, fixes it; lockfile semantics are verified per manager, not assumed. | known | DEPENDENCIES-021, DEPENDENCIES-022, DEPENDENCIES-023 |
| DEPENDENCIES.CHANGE.2 | Pin policy | Which versions may enter is fixed deliberately: the lockfile fixes the tree, direct dependencies of an application are exact, and release type is no guarantee of compatibility. | known \| conflict: ranges only, OpenSSF npm guide v1.1 (SRC-154, archived 2023); collective ecosystem pinning, SRC-287 \| unclear: library scope is inferred | DEPENDENCIES-024, DEPENDENCIES-025 |
| DEPENDENCIES.CHANGE.3 | Lockfile review | A lockfile change is a code change and is reviewed like one. | known \| unvalidated: claim is inferred from a listed attack vector \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (SUPPLY-C07) | DEPENDENCIES-026 |

### VERIFICATION

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| VERIFICATION | Verification | Defects that people forget to look for are found by machines on every change, with a result that blocks the change: the checked subset and the type layer hold only while a tool checks them there. | known \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | VERIFICATION-001, VERIFICATION-002, VERIFICATION-003, VERIFICATION-004, VERIFICATION-005, VERIFICATION-006, VERIFICATION-044, VERIFICATION-007, VERIFICATION-008, VERIFICATION-009, VERIFICATION-010, VERIFICATION-011, VERIFICATION-012, VERIFICATION-013, VERIFICATION-014, VERIFICATION-015, VERIFICATION-016, VERIFICATION-017, VERIFICATION-018, VERIFICATION-019 |

### RUNTIME

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| RUNTIME | Runtime behaviour | Code stays well behaved over time because its memory behaviour follows from what the collector can reach and from how long state lives, not from belief or folklore about references. | known \| unvalidated: most grounds are single-source \| unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline | RUNTIME-001, RUNTIME-002 |
| RUNTIME.MEMORY | Memory model | Memory behaviour follows from what the collector can reach and from how long state lives; this model, not folklore about references, decides what counts as a leak and what bounds it. | known \| unvalidated: both children rest on single T1 pages with tool-extracted quotes | - |
| RUNTIME.MEMORY.1 | Reachability decides leaks | A leak is an object kept reachable from a root by a retainer; unreachable objects are collected whatever their mutual references, so cycles alone are not leaks. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | RUNTIME-003, RUNTIME-004 |
| RUNTIME.MEMORY.2 | Bounded long-lived state | State that lives long is promoted into the collector's costlier region, so caches, sessions and other long-lived state carry an explicit bound. | known \| unvalidated: bounding advice inferred, quote tool-extracted | RUNTIME-005 |

### Intentlinks inside js-philosophy: within branches

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | CONTROL.SCHEDULING | CONTROL.BOUNDS | requires | A shared thread turns unbounded work into a failure for every client, so bounds on time and work are the remedy. |
| 2 | CONTROL.FLOW | CONTROL.BOUNDS | refines | Pacing is the bound that stream production has against consumption. |
| 3 | CONTROL.BOUNDS | CONTROL.FAILURE | dataflow | Timeouts and cancellation end operations with a failure value (an abort or timeout reason) that needs an owner. |
| 4 | DEFENSE.DOM.2 | DEFENSE.DOM.1 | requires | A verdict about a filter or gate presupposes the flow it guards, so the flow is known before the verdict is trusted. |
| 5 | DEFENSE.ORIGIN | DEFENSE.DOM.1 | dataflow | Messages, storage reads and third-party output are sources whose data ends at the same DOM sinks. |
| 6 | DEPENDENCIES.THREATS.1 | DEPENDENCIES.ADMISSION.2 | requires | The takeover route makes maintainer count and recency a vetting criterion. |
| 7 | DEPENDENCIES.CHANGE.1 | DEPENDENCIES.CHANGE.2 | requires | A pin policy means something only once the lockfile fixes the tree. |
| 8 | DEPENDENCIES.CHANGE.3 | DEPENDENCIES.THREATS.1 | dataflow | Reviewing lockfile diffs surfaces poisoned resolutions, one of the routes of compromise. |
| 9 | RUNTIME.MEMORY.2 | RUNTIME.MEMORY.1 | requires | Bounding long-lived state presumes the reachability model of what counts as retained. |
| 10 | SUBSET.STATE | SUBSET.FAILURE | requires | A lock on state protects only as far as a write to it fails loudly. |
| 11 | CONTRACTS.BOUNDARY | CONTRACTS.STATIC.1 | requires | Because a type layer attests nothing about arriving data, the boundary check is what gives the types their truth. |
| 12 | CONTRACTS.STATIC.2 | CONTRACTS.BOUNDARY | requires | Since a passing check is not proof, run-time validation stays in place even in fully typed code. |
| 13 | DEFENSE.PROTOTYPE.2 | DEFENSE.CODE | dataflow | A polluted shared prototype feeds gadgets that compile or run attacker-shaped values, ending in code execution. |

### Intentlinks inside js-philosophy: across branches (resolved from proposals)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | CONTROL.FAILURE | SUBSET.FAILURE | requires | Loud failure at the language level is the base on which explicit error propagation and unhandled-rejection policy stand. |
| 2 | SUBSET.MATURITY | DEPENDENCIES.ADMISSION.2 | requires | Settled features and a supported-runtime floor are the language-side counterpart of choosing a supported dependency set. |
| 3 | DEPENDENCIES.TRUST.2 | DEFENSE.HOST | requires | The permission model is a seat belt for trusted code, not containment of hostile dependencies (topic 12 of 12_dissent). |
| 4 | DEFENSE.HOST.1 | CONTROL.SCHEDULING | requires | The single shared thread that makes one request able to stall the process is stated once, in CONTROL.SCHEDULING; this node adds that untrusted input must not control the cost. |
| 5 | STRUCTURE.STATE.2 | SUBSET.STATE | requires | Freezing is shallow and does not make nested data immutable; the freeze mechanics are owned by SUBSET. |
| 6 | SUBSET.VISIBLE | CONTRACTS.BOUNDARY | requires | What an expression does follows from the declared kind of its operands; for data from outside, that kind is established by parsing at the boundary. |
| 7 | DEFENSE | CONTRACTS.BOUNDARY | requires | Treating every input as hostile in DEFENSE presupposes that inputs are parsed at the boundary. |

### Inter links from js-philosophy to python-kb-philosophy

Target file `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`; the uids were read there.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | SUBSET.VISIBLE | python-kb-philosophy:DEFENSIVE | refines | Explicit over implicit and least surprise, applied to comparison and conversion. |
| 2 | SUBSET.FAILURE | python-kb-philosophy:DEFENSIVE | refines | Fail fast and never swallow errors, applied to the language's strict mode. |
| 3 | SUBSET.MATURITY | python-kb-philosophy:REPRODUCIBILITY | refines | The same code means the same on every target only if it uses settled features (inferred). |
| 4 | CONTRACTS.STATIC | python-kb-philosophy:DATACENTRICITY | refines | Make invalid states unrepresentable and let a schema be the constraint: the shared principle realised through a separate type layer |
| 5 | CONTROL.FAILURE | python-kb-philosophy:DEFENSIVE | refines | Fail fast, no silent swallowing and visible errors are the shared principle; this node adds the two JavaScript failure channels. |
| 6 | STRUCTURE | python-kb-philosophy:STRUCTURE | refines | Structure precedes implementation; here it is specialised to the JavaScript module graph, where a change must stay inside one module. |
| 7 | DEFENSE | python-kb-philosophy:DEFENSIVE | refines | Defensive design (assume failure, validate at boundaries, trust after validation) is the language-neutral base; this branch adds the JavaScript hazards. |
| 8 | DEPENDENCIES.TRUST.1 | python-kb-philosophy:DEFENSIVE | refines | Assume failure and hostility: here the hostile party can be a dependency. |
| 9 | DEPENDENCIES.CHANGE.1 | python-kb-philosophy:REPRODUCIBILITY | refines | Same inputs, same tree: lockfiles and version pinning. |
| 10 | DEPENDENCIES.CHANGE.2 | python-kb-philosophy:REPRODUCIBILITY | refines | Version pinning is a reproducibility rule with a contested scope. |
| 11 | CONTRACTS.BOUNDARY | python-kb-philosophy:DEFENSIVE | refines | Validate at boundaries and trust after validation: the shared principle, here with the JavaScript-distinct fact that the language has no run-time types. |

## Graph pig-js-defaults

### Root

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.ROOT | Solid JavaScript defaults | The concrete rules that make JavaScript predictable, cheap to change and attack-resistant in the browser and in Node: the safe subset, the type layer and boundary parsing, explicit control of time and failure, locality of change, hostile-input defence, trusted dependencies, machine verification and measured runtime behaviour. Each rule is one decision traced to ledger rows. | known | - |

### PIG-JS.SUBSET

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.SUBSET | Checked JavaScript subset | Make JavaScript behaviour predictable by narrowing the language: strict semantics, explicit comparison and conversion, stated numeric limits, visible mutation, enforced privacy, settled features only. | known | - |
| PIG-JS.SUBSET.STRICTNESS | Strict by construction | All code runs under strict semantics through ES modules, and every binding is block-scoped and fixed by default. | known | - |
| PIG-JS.SUBSET.CONVERSION | Explicit comparison and conversion | A comparison or conversion never depends on an implicit coercion the reader must predict. | known | - |
| PIG-JS.SUBSET.NUMBERS | Numbers with stated limits | Number carries only values within its precision and range; exactness beyond them is obtained by another representation. | known | - |
| PIG-JS.SUBSET.OBJECTS | Objects, classes and receivers | Object and class code fixes its receiver, its construction order, its privacy and its prototype chain at the language level. | known \| unvalidated: accessor rule rests on a position only | - |
| PIG-JS.SUBSET.MUTATION | Visible mutation | State changes happen where the code says they do: freezing is understood as shallow, copies are deep on purpose, sorting states whether it mutates. | known | - |
| PIG-JS.SUBSET.EVOLUTION | Settled features and retired legacy | New code uses only settled features checked against its targets and none of the retired or deprecated ones. | known \| unvalidated: statement-termination rule rests on a position only | - |
| PIG-JS.SUBSET.STRICTNESS.1 | Strict mode everywhere | Every file runs in strict mode, so a typo or an unowned receiver raises an error instead of creating a global or a hidden default. | known \| unvalidated: practice inferred from MDN's stated reasons; quote tool-extracted \| unvalidated: rests on single-source claims only | SUBSET-003, SUBSET-004, SUBSET-005 |
| PIG-JS.SUBSET.STRICTNESS.2 | ES modules as the unit | Code is written as ES modules, which are strict, module-scoped, evaluated once and deferred. | known | SUBSET-006, SUBSET-007 |
| PIG-JS.SUBSET.STRICTNESS.3 | Fixed bindings by default | A binding is fixed unless the code reassigns it, and a fixed binding is not mistaken for an immutable value. | known | SUBSET-008, SUBSET-009, SUBSET-010 |
| PIG-JS.SUBSET.STRICTNESS.4 | No function-scoped declarations | Names are block-scoped, never function-scoped, hoisted or silently redeclarable. | known | SUBSET-011 |
| PIG-JS.SUBSET.CONVERSION.1 | Strict equality | Values are compared without type conversion; the comparison result follows from the operands alone. | known | SUBSET-012, SUBSET-013, SUBSET-014, SUBSET-015 |
| PIG-JS.SUBSET.CONVERSION.2 | Null and undefined checks | A check for absence names the values it tests, with no loose-equality exception. | known \| conflict: Google JS guide and ESLint option null ignore allow == null as the one exception \| unvalidated: a rule has no claim of its own, it is the build's judgment | SUBSET-016, SUBSET-017 |
| PIG-JS.SUBSET.CONVERSION.3 | NaN test | NaN is detected by a dedicated test, since it is unequal to every value. | known | SUBSET-018 |
| PIG-JS.SUBSET.CONVERSION.4 | Explicit conversion | A conversion is written as a call that names its target type; a conversion hidden in an operator is flagged as a readability convention. | known \| unvalidated: positions only, no mechanism evidence \| conflict: Pradel and Sen (T2, 2015 corpus) found 98.85 percent of implicit coercions likely harmless | SUBSET-019, SUBSET-020, SUBSET-021, SUBSET-022 |
| PIG-JS.SUBSET.CONVERSION.5 | Number is not validation | Number conversion is never the test that an input is a valid number. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | SUBSET-023 |
| PIG-JS.SUBSET.CONVERSION.6 | Nullish defaults and chains | A default replaces only absence, and optional chaining is used within its syntactic limits. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | SUBSET-024, SUBSET-025, SUBSET-026, SUBSET-027 |
| PIG-JS.SUBSET.NUMBERS.1 | Rounded fractions | Fractional arithmetic is treated as approximate wherever results are compared or accumulated. | known \| gap: exact decimal and money arithmetic has no admitted source (G-M01) | SUBSET-028 |
| PIG-JS.SUBSET.NUMBERS.2 | Safe integer range | Integers stay within the safe range or change representation. | known | SUBSET-029 |
| PIG-JS.SUBSET.NUMBERS.3 | BigInt scope | BigInt appears only where values exceed the safe range, and never meets Number in one expression. | known | SUBSET-030, SUBSET-031, SUBSET-032 |
| PIG-JS.SUBSET.NUMBERS.4 | Integers across JSON | Integers that exceed the safe range cross JSON as strings or through an explicit codec. | known | SUBSET-033, SUBSET-034 |
| PIG-JS.SUBSET.OBJECTS.1 | Explicit receiver | The receiver of a call is never implicit: no code relies on the global this, and callbacks keep the outer receiver lexically. | known | SUBSET-035, SUBSET-036, SUBSET-037, SUBSET-038, SUBSET-039 |
| PIG-JS.SUBSET.OBJECTS.2 | Construction order | A class is declared before use and a derived class initialises its base before touching its own state. | known \| unvalidated: quote tool-extracted (class declaration rule) | SUBSET-040, SUBSET-041, SUBSET-042 |
| PIG-JS.SUBSET.OBJECTS.3 | Language-enforced privacy | Private means unreachable from outside, by a mechanism the language enforces. | known \| conflict: Google TS guide (TypeScript private, not hash fields), Google JS guide (optional trailing underscore), Airbnb (no underscores) \| unvalidated: a rule has no claim of its own, it is the build's judgment | SUBSET-043, SUBSET-044, SUBSET-045, SUBSET-046 |
| PIG-JS.SUBSET.OBJECTS.4 | Accessor properties | Properties do not run code on access; behaviour that does work is an explicit method call. | known \| unvalidated: holder position only (Google JS), no mechanism evidence | SUBSET-047, SUBSET-069 |
| PIG-JS.SUBSET.OBJECTS.5 | Untouched built-ins | The language's built-in prototypes carry only what the language put there. | known | SUBSET-048, SUBSET-049, SUBSET-050 |
| PIG-JS.SUBSET.OBJECTS.6 | Own properties and enumeration | Own properties are tested and enumerated without visiting the prototype chain. | known \| unvalidated: for-in rule on arrays single T2 source; hasOwn preference grounded for untrusted keys by two T1 sources (RUNSEC-C07, merged here), extension to all reads inferred | SUBSET-051, SUBSET-052, SUBSET-053 |
| PIG-JS.SUBSET.MUTATION.1 | Shallow freeze | Freezing is relied on for one level only and only in strict code; deeper immutability is designed in. | known | SUBSET-054, SUBSET-055, SUBSET-056 |
| PIG-JS.SUBSET.MUTATION.2 | Deliberate deep copy | A deep copy uses the platform clone and knows what the clone drops. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | SUBSET-057, SUBSET-058 |
| PIG-JS.SUBSET.MUTATION.3 | Sorting | Sorting states whether the original may change and never relies on the default order for numbers. | known \| unvalidated: quote tool-extracted (comparator rule) | SUBSET-059, SUBSET-060 |
| PIG-JS.SUBSET.EVOLUTION.1 | Finished proposals only | Production code uses only features that reached the final standardisation stage. | known \| unvalidated: single T1 source restricted to status facts; rule inferred | SUBSET-061 |
| PIG-JS.SUBSET.EVOLUTION.2 | Temporal adoption | The new date-time API is adopted only once every target is verified to ship it or a polyfill covers the gap. | known \| unvalidated: availability facts dated, recheck before citing | SUBSET-062, SUBSET-071, SUBSET-063 |
| PIG-JS.SUBSET.EVOLUTION.3 | No legacy syntax | Syntax that strict mode forbids or that blocks reasoning about names is not written. | known | SUBSET-064, SUBSET-065 |
| PIG-JS.SUBSET.EVOLUTION.4 | No deprecated features | Deprecated and browser-only legacy features are replaced by their listed successors in new code. | known | SUBSET-066, SUBSET-067 |
| PIG-JS.SUBSET.EVOLUTION.5 | Statement termination | Every statement is terminated explicitly and every control structure is braced, so no statement boundary or scope is left to automatic insertion or indentation. | known \| unvalidated: holder position only (Google JS); insertion hazards not extracted | SUBSET-068, SUBSET-070 |

### PIG-JS.CONTRACTS

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.CONTRACTS | Contracts defaults | Make JavaScript intent checkable with TypeScript at build time and schema parsing at run time, every escape from the checker being deliberate | known | - |
| PIG-JS.CONTRACTS.LAYER | Type layer | Choose the type layer and keep its check in the loop whatever runs the code | known | - |
| PIG-JS.CONTRACTS.STRICT | Checker strictness | Run the checker at its most demanding setting and keep that setting stable across upgrades | known | CONTRACTS-054 |
| PIG-JS.CONTRACTS.ESCAPE | Escape hatches | Keep the escape hatches of the type system shut, and open one only deliberately and with a reason | known | - |
| PIG-JS.CONTRACTS.MODEL | Modelling and narrowing | Model variants and absence so that the checker can prove more, and narrow explicitly | known | - |
| PIG-JS.CONTRACTS.SIGNATURE | Function shapes | Declare function shapes that reject the calls the contract does not allow | known | - |
| PIG-JS.CONTRACTS.BOUNDARY | Parse at the boundary | Turn untrusted data into typed values by parsing at the boundary | known | - |
| PIG-JS.CONTRACTS.LAYER.1 | Type layer is TypeScript | Write JavaScript projects in TypeScript with strict checking when a build or type-check step can be adopted; JSDoc-checked JavaScript is the stated alternative when none can | risky \| conflict: JSDoc-checked JavaScript, none \| unvalidated: decided by the build on T1 mechanism facts and one T2 holder \| unvalidated: rests on claims marked inferred or open (TYPES-C46) | CONTRACTS-011, CONTRACTS-053, CONTRACTS-012 |
| PIG-JS.CONTRACTS.LAYER.2 | JSDoc-checked JavaScript as the no-compile-step fallback | Where no compile step can exist, check JavaScript with the same compiler through JSDoc, naming its weaker guarantees | known \| unvalidated: no admitted advocate; TypeScript 7.0 facts are vendor facts | CONTRACTS-013, CONTRACTS-014, CONTRACTS-015, CONTRACTS-016 |
| PIG-JS.CONTRACTS.LAYER.3 | Type check is a step of its own | Running TypeScript never counts as checking it: a separate type check with no emit runs wherever types are stripped | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-017, CONTRACTS-018 |
| PIG-JS.CONTRACTS.LAYER.4 | Only erasable syntax under type stripping | When Node strips types, the code uses only syntax that stripping can erase, enforced by the compiler option | known | CONTRACTS-019 |
| PIG-JS.CONTRACTS.LAYER.5 | Compiler options aligned with Node | The checker is configured as Node documents for type stripping, since Node ignores the configuration file at run time | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-020 |
| PIG-JS.CONTRACTS.LAYER.6 | Per-file transpilation safety | Where files are transpiled one at a time, code needing cross-file type information is reported by the checker | known \| unvalidated: quote tool-extracted | CONTRACTS-021 |
| PIG-JS.CONTRACTS.STRICT.1 | strict on | Enable the whole strict family and never turn a member off; noImplicitAny and strictNullChecks are its load-bearing members | known | CONTRACTS-022, CONTRACTS-023, CONTRACTS-024 |
| PIG-JS.CONTRACTS.STRICT.2 | Unchecked index access | Reads of undeclared keys are typed as possibly undefined | known \| unvalidated: source says consider (TypeScript documentation, typescript-eslint); the MUST is the build's choice under the max rule; mechanism only, no admitted source mandates the flag \| conflict: friction cost (typescript-eslint) | CONTRACTS-025 |
| PIG-JS.CONTRACTS.STRICT.3 | Exact optional properties | An optional property means absent, not possibly undefined | known \| unvalidated: source says consider (TypeScript documentation); the MUST is the build's choice under the max rule; mechanism only, quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-026 |
| PIG-JS.CONTRACTS.STRICT.4 | Compiler version is pinned | The compiler version is pinned and upgraded deliberately, because defaults and strict-family checks change between releases | known \| unvalidated: pinning inferred from single T1 source | CONTRACTS-027, CONTRACTS-028 |
| PIG-JS.CONTRACTS.ESCAPE.1 | unknown, not any | A value of unknown shape is typed unknown and narrowed before use | known | CONTRACTS-029 |
| PIG-JS.CONTRACTS.ESCAPE.2 | Explicit any is a lint error | Explicit any is rejected by the linter, which is the check that closes the escape hatch | known | CONTRACTS-030 |
| PIG-JS.CONTRACTS.ESCAPE.3 | Leaked any is caught | Values typed any that enter from libraries and untyped sources are caught at assignment by type-aware lint | known | CONTRACTS-031 |
| PIG-JS.CONTRACTS.ESCAPE.4 | No Function type | Callable values carry a specific signature, never the Function type | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-032 |
| PIG-JS.CONTRACTS.ESCAPE.5 | Assertions need a reason | Type and non-null assertions appear only with an obvious reason, and an explicit run-time check is preferred | known | CONTRACTS-033 |
| PIG-JS.CONTRACTS.ESCAPE.6 | No suppression directives | Type errors are fixed and never silenced by directive; a lint suppression is allowed only with a comment saying why | known \| unvalidated: holder position only (Google TS), single T2 source | CONTRACTS-034, CONTRACTS-035 |
| PIG-JS.CONTRACTS.MODEL.1 | Discriminated unions with exhaustive switches | Variants are discriminated unions closed by a never assignment, so a new member breaks the build where it is unhandled | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-036 |
| PIG-JS.CONTRACTS.MODEL.2 | Explicit narrowing, not truthiness | Primitives are narrowed by explicit tests, because falsy values are legitimate data | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (TYPES-C22) | CONTRACTS-037 |
| PIG-JS.CONTRACTS.MODEL.3 | Optional chaining only on nullable values | Optional chaining appears only where the type says the value can be absent | known \| unvalidated: preference inferred from rule behaviour \| unvalidated: rests on single-source claims only | CONTRACTS-038 |
| PIG-JS.CONTRACTS.MODEL.4 | Type predicates are assertions | A user-defined type predicate is held to the standard of a type assertion: its body performs a real run-time check, and built-in narrowing or a schema parse is preferred | known \| unvalidated: inferred from assertion and unsoundness grounds; no admitted source states that the compiler does not verify the body \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (TYPES-C20) | CONTRACTS-039 |
| PIG-JS.CONTRACTS.MODEL.5 | Object types by interface | Object types are declared by interface, which can be extended and re-opened; aliases are for what an interface cannot express | known \| unvalidated: holder position only (Google TS); the alias exception is inferred | CONTRACTS-040 |
| PIG-JS.CONTRACTS.SIGNATURE.1 | Options object | Calls with several optional or same-typed primitive arguments take one named options object | known \| unvalidated: inferred, transfer to application APIs \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (STRUCT-C49) | CONTRACTS-041, CONTRACTS-042 |
| PIG-JS.CONTRACTS.SIGNATURE.2 | Optional trailing parameters, not overloads | A declared API expresses optional trailing arguments as optional parameters | known \| unvalidated: quote tool-extracted; declared APIs only \| unvalidated: rests on single-source claims only | CONTRACTS-043 |
| PIG-JS.CONTRACTS.SIGNATURE.3 | Unions, not overloads | A declared API expresses a varying argument type as a union | known \| unvalidated: quote tool-extracted; declared APIs only \| unvalidated: rests on single-source claims only | CONTRACTS-044 |
| PIG-JS.CONTRACTS.SIGNATURE.4 | Callback result and parameter types | An ignored callback result is void and callback parameters are never optional | known \| unvalidated: quote tool-extracted; declared APIs only \| unvalidated: rests on single-source claims only | CONTRACTS-045 |
| PIG-JS.CONTRACTS.BOUNDARY.1 | JSON.parse yields unknown | The result of JSON.parse is unknown until validated | known \| unvalidated: rests on claims marked inferred or open (TYPES-C18) | CONTRACTS-046 |
| PIG-JS.CONTRACTS.BOUNDARY.2 | Schema rejects unneeded properties | Untrusted structured input is checked against a schema that allows only the keys and types it names, before merge or lookup code sees it | known | CONTRACTS-047 |
| PIG-JS.CONTRACTS.BOUNDARY.3 | Bind to a dedicated allowlisted object | Request data binds to a purpose-built object with allowlisted fields and never to a domain model | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | CONTRACTS-048 |
| PIG-JS.CONTRACTS.BOUNDARY.4 | Validate before Node or language APIs | External input is validated by allowlist in application code before it reaches Node or language APIs | known | CONTRACTS-049 |
| PIG-JS.CONTRACTS.BOUNDARY.5 | Schema infers the static type | Boundary schemas are written in a library whose schema is the single source of the static type, so the parse and the type cannot drift; schemas are never built from untrusted input | known \| unvalidated: vendor documentation facts only; no admitted ranking between Zod and Valibot, so no library is named as the default \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (TYPES-C36) | CONTRACTS-050, CONTRACTS-051, CONTRACTS-052 |

### PIG-JS.CONTROL

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.CONTROL | Explicit control in JavaScript code | JavaScript code makes time, failure and resources explicit through the host's own mechanisms: promises and async functions, error values, abort signals, scheduling choices, streams and process hooks. | known \| rolls up six children | - |
| PIG-JS.CONTROL.PROMISES | Promises and async functions | Every promise is created correctly, chained without loss, observed by someone and combined so that failure and ordering stay visible. | known \| rolls up six children | - |
| PIG-JS.CONTROL.ERRORS | Error values and their channels | Failures are Error objects with an origin, identified by a stable code, handled or rethrown with their cause, and routed through the channel the caller can observe. | known \| rolls up four children | - |
| PIG-JS.CONTROL.BOUNDS | Cancellation, timeouts and caps | Every asynchronous wait ends by a signal, a timeout or a configured cap, and the party that starts the work can stop it. | known \| rolls up three children | - |
| PIG-JS.CONTROL.SCHEDULING | Event loop, timers and threads | Code states the ordering and timing it needs, keeps callbacks short, moves CPU work to workers and carries request state explicitly. | known \| rolls up four children | - |
| PIG-JS.CONTROL.FLOW | Streams and backpressure | Streams move data at the pace of the consumer, are composed so that errors close every stage, and never rely on a buffer size as a memory limit. | known \| rolls up three children | - |
| PIG-JS.CONTROL.PROCESS | Process lifecycle and handles | Unobserved failures end the process visibly, exit and shutdown finish their work, and handles are closed by the code that owns them. | known \| rolls up five children | - |
| PIG-JS.CONTROL.PROMISES.1 | Chaining without loss | Every promise started inside a chain is returned into it, so later steps wait for the work they depend on. | known \| unvalidated: single T2 source for the forked-chain case; single T1 editorial position for flat chains | CONTROL-012, CONTROL-013, CONTROL-014, CONTROL-015 |
| PIG-JS.CONTROL.PROMISES.2 | Constructing promises | Promises are constructed only when no promise exists yet, and every constructed promise settles once on every path. | known \| unvalidated: single T1 rule document for the executor rule (quote tool-extracted); T2 papers sharing a co-author for the others | CONTROL-016, CONTROL-017, CONTROL-018 |
| PIG-JS.CONTROL.PROMISES.3 | Every promise observed | No promise is dropped, silenced or misread: each is awaited, returned or given a rejection handler. | known \| unvalidated: single T1 rule documentation for the void and condition rules (quote tool-extracted) | CONTROL-019, CONTROL-020, CONTROL-021, CONTROL-022 |
| PIG-JS.CONTROL.PROMISES.4 | Combining and ordering async work | Independent work runs concurrently, started promises are combined before awaiting, and shared state is guarded across suspension points. | known \| unvalidated: single T1 source for the early-rejection and stale-read rules (quote tool-extracted) \| gap: concurrency limits not covered | CONTROL-023, CONTROL-024, CONTROL-025, CONTROL-026, CONTROL-027 |
| PIG-JS.CONTROL.PROMISES.5 | Async functions without waste | Asynchronous code adds no promise that does no work. | known \| unvalidated: single T2 source (DrAsync sample); return await inside try/catch not covered | CONTROL-028, CONTROL-030 |
| PIG-JS.CONTROL.PROMISES.6 | Async functions over then chains | Asynchronous code is written with async functions and await by default, so failure travels one visible path; explicit chains remain where kept flat. | known \| unvalidated: single T2 source, V8 team position of 2018 (restricted to history, dated); chain exception inferred from the MDN position | CONTROL-029, CONTROL-086 |
| PIG-JS.CONTROL.ERRORS.1 | Error values | Thrown and rejected values are Error instances identified by a stable code. | known \| unvalidated: single T1 source for the code rule (quote tool-extracted) | CONTROL-031, CONTROL-032 |
| PIG-JS.CONTROL.ERRORS.2 | Catching | A catch acts on the failure; caught values are unknown until narrowed, and failures of asynchronous callbacks go through a channel the caller observes. | known \| unvalidated: single T1 sources; the no-empty-catch rule rests on one style-guide position (Google JS) | CONTROL-033, CONTROL-034, CONTROL-035 |
| PIG-JS.CONTROL.ERRORS.3 | Rethrowing with a cause | A rethrown failure keeps the original as its cause and states what failed at this level. | known \| unvalidated: single T1 source for the one-site rule \| unvalidated: quote not obtained (ASYNC-C20) | CONTROL-036, CONTROL-037 |
| PIG-JS.CONTROL.ERRORS.4 | Emitter failures | An event emitter's error event always has a listener, and rejections of async listeners reach it. | known \| unvalidated: single T1 source for captureRejections and events.once | CONTROL-038, CONTROL-039, CONTROL-040 |
| PIG-JS.CONTROL.BOUNDS.1 | Abort signals | Cancellable operations accept a signal, check it first, reject with its reason, and use one controller per operation. | known \| unvalidated: single T1 source for the pipeline signal | CONTROL-041, CONTROL-042, CONTROL-043, CONTROL-044 |
| PIG-JS.CONTROL.BOUNDS.2 | Timeouts | Waits are bounded by a timeout signal, a cancellable timer or a configured server timeout. | known \| unvalidated: single T1 source for timers and server timeouts; do-not-disable rule inferred \| unvalidated: quote not obtained (RUNTIME-C42) | CONTROL-045, CONTROL-046, CONTROL-047 |
| PIG-JS.CONTROL.BOUNDS.3 | Abort listener hygiene | Listeners on signals are removed at the end of the operation and registered through the Node API that cannot be defeated. | known \| unvalidated: single T1 source each (quote tool-extracted) | CONTROL-048, CONTROL-049 |
| PIG-JS.CONTROL.SCHEDULING.1 | Ordering and timer precision | Code does not rely on the order of timers and immediates or on exact delays, and defers work in the way that cannot starve I/O. | known \| unvalidated: single T1 source for the nextTick rule | CONTROL-050, CONTROL-051, CONTROL-052, CONTROL-053, CONTROL-054 |
| PIG-JS.CONTROL.SCHEDULING.2 | Event-loop blocking | Callback cost stays bounded by input size and synchronous blockers stay off the server's event loop. | known \| unvalidated: single T1 source, mechanism only (restricted); the concrete API list is not admitted \| unvalidated: rests on claims marked inferred or open (ASYNC-C41) | CONTROL-055, CONTROL-056, CONTROL-057, CONTROL-058 |
| PIG-JS.CONTROL.SCHEDULING.3 | Workers | CPU-bound work moves to a few workers whose messages, failures and resources are explicit. | known \| unvalidated: single T1 source for sparing use and resource limits \| unvalidated: quote not obtained (ASYNC-C46) | CONTROL-059, CONTROL-060, CONTROL-061, CONTROL-062, CONTROL-063 |
| PIG-JS.CONTROL.SCHEDULING.4 | Async context | Request-scoped state is carried by the platform's scoped store, not by hand-built hooks. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-064, CONTROL-065 |
| PIG-JS.CONTROL.FLOW.1 | Backpressure | Writers stop when told to stop and resume when told to resume. | known \| unvalidated: single T1 source, mechanism only (restricted), for push and data-listener rules | CONTROL-066, CONTROL-067, CONTROL-068 |
| PIG-JS.CONTROL.FLOW.2 | Pipelines and iteration | Streams are composed with the function that closes every stage on failure, and early exit semantics are known. | known \| unvalidated: single T1 source for pipeline and finished rules | CONTROL-069, CONTROL-070, CONTROL-071 |
| PIG-JS.CONTROL.FLOW.3 | Web Streams | Web Streams propagate errors by default and share chunk objects across tee branches. | known \| unvalidated: single T1 source each | CONTROL-072, CONTROL-073, CONTROL-074 |
| PIG-JS.CONTROL.PROCESS.1 | Unhandled rejections | An unhandled rejection is treated as a defect that ends the process in Node and is reported in browsers. | known | CONTROL-075, CONTROL-076, CONTROL-077 |
| PIG-JS.CONTROL.PROCESS.2 | Uncaught exceptions | Node's uncaughtException hook is used only for synchronous cleanup before the process ends, and uncaughtExceptionMonitor only to log; the end-and-restart contract itself is CONTROL.LIFECYCLE. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-078, CONTROL-079 |
| PIG-JS.CONTROL.PROCESS.3 | Exit | Exit lets pending writes drain and does cleanup only in synchronous exit listeners. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-080, CONTROL-081 |
| PIG-JS.CONTROL.PROCESS.4 | Shutdown | A signal listener finishes cleanup and ends the process; servers close gracefully before connections are forced. | known \| unvalidated: single T1 source; the must-exit rule is inferred \| gap: shutdown contract owned by the web-architecture sibling | CONTROL-082, CONTROL-083 |
| PIG-JS.CONTROL.PROCESS.5 | Owned handles | The code that opens or takes over a handle or socket closes it on every path. | known \| unvalidated: single T1 source; the FileHandle wording comes from a digest, not verbatim \| unvalidated: quote not obtained (RUNTIME-C17) | CONTROL-084, CONTROL-085 |
| PIG-JS.CONTROL.PROMISES.4.1 | Concurrency limits, retry and backoff | How many operations run at once, and when a failed operation is retried with what delay. | undecided \| missing: no admitted source | - |
| PIG-JS.CONTROL.ERRORS.2.1 | Operational versus programmer errors | How a program tells expected failures from defects, and what error detail reaches callers. | undecided \| missing: no admitted source | - |
| PIG-JS.CONTROL.SCHEDULING.2.1 | Yielding to the main thread in browsers | How browser code splits long tasks. | undecided \| missing: no admitted source recommends a method (the scheduler APIs are a draft, Node exposes only experimental ones) | - |

### PIG-JS.STRUCTURE

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.STRUCTURE | JavaScript structure defaults | Concrete JavaScript and Node rules that keep a change inside one module or one package boundary: module format, import-time behaviour, exposed surface, dependency direction, package entry points. | known \| gap: layering rule undecided (PIG-JS.STRUCTURE.DIRECTION.3) | - |
| PIG-JS.STRUCTURE.FORMAT | Module format and host | State which module system and which host load each file, so that a specifier means one thing wherever the code runs. | known | - |
| PIG-JS.STRUCTURE.NODE | Node ESM and CommonJS interop | Write module code for Node so that it loads the same under both module systems, without relying on detection or on globals that do not exist. | known | - |
| PIG-JS.STRUCTURE.LOADING | Import-time behaviour | Make what happens when a module is imported predictable: once, hoisted, effect-free, asynchronous only at the edge. | known | - |
| PIG-JS.STRUCTURE.SURFACE | Exposed surface of a module | Expose from a module only the names others need, in a form that cannot be silently mutated or merged ambiguously. | known | - |
| PIG-JS.STRUCTURE.DIRECTION | Dependency direction | Keep the import graph acyclic and, where a source supports it, layered, so that a change flows one way. | known \| gap: layering undecided | - |
| PIG-JS.STRUCTURE.PACKAGE | Package entry points and internal addressing | Declare a package's public entry points and its internal aliases so that consumers and tools see one stable interface. | known | - |
| PIG-JS.STRUCTURE.FORMAT.1 | Explicit module format | Mark each file's module format with an extension or the package type field instead of letting Node guess from syntax. | known \| unvalidated: practice inferred from the detection order \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (STRUCT-C14) | STRUCTURE-013 |
| PIG-JS.STRUCTURE.FORMAT.2 | Browser module scripts | Load browser code with module scripts so that import and export work under CORS and same-origin rules. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | STRUCTURE-014 |
| PIG-JS.STRUCTURE.FORMAT.3 | Resolution matches the host | Configure the type checker to resolve specifiers as the host that runs the code does, since ECMAScript leaves resolution to the host. | known \| unvalidated: quote tool-extracted | STRUCTURE-015 |
| PIG-JS.STRUCTURE.FORMAT.4 | Modules as the only sharing mechanism | Share code between files only through module import and export, never through namespaces. | known \| unvalidated: holder position only (Google TS) \| unvalidated: quote not obtained (STRUCT-C27) | STRUCTURE-016 |
| PIG-JS.STRUCTURE.NODE.1 | Full specifiers | Write the file extension and the directory index on every relative specifier in Node ESM. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | STRUCTURE-017 |
| PIG-JS.STRUCTURE.NODE.2 | Module equivalents of CommonJS globals | Replace the CommonJS wrapper globals with their module equivalents and import JSON with the type attribute. | known \| unvalidated: quote tool-extracted | STRUCTURE-018 |
| PIG-JS.STRUCTURE.NODE.3 | Loading ESM from CommonJS | Load an ES module from CommonJS through require only when its graph has no top-level await, otherwise through dynamic import. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only | STRUCTURE-019, STRUCTURE-020 |
| PIG-JS.STRUCTURE.NODE.4 | Importing CommonJS from ESM | Use the default import of a CommonJS module and do not depend on detected named exports of unusual export patterns. | known \| unvalidated: quote tool-extracted | STRUCTURE-021 |
| PIG-JS.STRUCTURE.NODE.5 | CommonJS export assignment | Assign module.exports, never the exports shortcut, to replace what a CommonJS module exports. | known \| unvalidated: quote tool-extracted | STRUCTURE-022 |
| PIG-JS.STRUCTURE.LOADING.1 | Imports run once and hoisted | Never use import order to sequence work; run repeatable work by exporting a function. | known | STRUCTURE-023, STRUCTURE-024 |
| PIG-JS.STRUCTURE.LOADING.2 | Side-effect-only imports | Reserve bare imports for a module's side effect and name the module as such. | known \| unvalidated: quote tool-extracted | STRUCTURE-025 |
| PIG-JS.STRUCTURE.LOADING.3 | Dynamic import for conditional loading | Load conditionally or lazily with dynamic import, because static imports are top-level, hoisted and unconditional. | known \| unvalidated: quote tool-extracted | STRUCTURE-026 |
| PIG-JS.STRUCTURE.LOADING.4 | Top-level await confined to entry points | Use top-level await only where no other module imports or requires the file, because it makes every importer wait. | known \| conflict: top-level await is acceptable anywhere, champions in the TC39 proposal (education suffices) \| unvalidated: scope of the rule inferred from the mechanism, no measurement of the hazard | STRUCTURE-027, STRUCTURE-028 |
| PIG-JS.STRUCTURE.LOADING.5 | Static structure for dropping unused code | Keep import and export static so that tools can drop unused code, and give a bundler the hints it needs where import does more than export. | known \| gap: no decision row, facts and one acceptable-when only \| unvalidated: rests on single-source claims only | STRUCTURE-029, STRUCTURE-030 |
| PIG-JS.STRUCTURE.LOADING.6 | Barrel files | Import from the defining module and keep re-exporting modules to a package's public entry point. | risky \| unvalidated: single T3 source, one synthetic measurement on one machine \| unvalidated: holder position only (the barrel-file article's author) \| conflict: barrels are a documented use of aggregation, MDN (no recommendation) | STRUCTURE-031 |
| PIG-JS.STRUCTURE.SURFACE.1 | Named exports | Export by name only, so every importer uses the exporter's name. | known \| conflict: default export for single-export modules, Airbnb \| unvalidated: holder position only (Google JS, Google TS) | STRUCTURE-032 |
| PIG-JS.STRUCTURE.SURFACE.2 | Minimal exported surface | Export only the symbols used outside the module. | known \| unvalidated: holder position only (Google TS) | STRUCTURE-033 |
| PIG-JS.STRUCTURE.SURFACE.3 | Read-only exported state | Never write to an import and export no mutable bindings, so state has one owner. | known \| unvalidated: holder position only (Google JS, Google TS, Airbnb) for the strongest form (no mutable export); the mechanism is T1 | STRUCTURE-034, STRUCTURE-035 |
| PIG-JS.STRUCTURE.SURFACE.4 | Unambiguous re-exports | Do not merge modules by wildcard re-export when names may collide, because a collision silently drops the name. | known \| unvalidated: quote tool-extracted | STRUCTURE-036, STRUCTURE-037 |
| PIG-JS.STRUCTURE.SURFACE.5 | No static-only container classes | Use the module as the namespace and export functions and constants individually. | known \| conflict: stateless groupings as static methods, W3C TAG \| unvalidated: holder position only (Google JS, Google TS) | STRUCTURE-038, STRUCTURE-039 |
| PIG-JS.STRUCTURE.DIRECTION.1 | No import cycles | Create no import cycle between modules, in ESM or CommonJS. | known \| conflict: cycles are a supported mechanism, Node CommonJS docs (no recommendation) \| unvalidated: single T1 ground (MDN advice, used from its slot-01 claim where the register leaves it unrestricted), quote tool-extracted; other holders are positions only, no source measures the cost | STRUCTURE-040, STRUCTURE-041 |
| PIG-JS.STRUCTURE.DIRECTION.2 | Mechanical cycle detection | Detect cycles with a lint rule, enabled knowingly and with its cost bounded. | risky \| unvalidated: single T3 source (the rule's own documentation) \| unvalidated: holder position only (eslint-plugin-import maintainers) | STRUCTURE-042 |
| PIG-JS.STRUCTURE.DIRECTION.3 | Declared layering | Declare which module kinds may import which and enforce it mechanically. | undecided \| missing: no admitted source grounds a layering rule (the restriction-by-pattern rule documents environment fit only) | STRUCTURE-043 |
| PIG-JS.STRUCTURE.PACKAGE.1 | Exports field | Declare a package's public entry points with the exports field so that every other subpath is encapsulated. | known \| unvalidated: quote tool-extracted | STRUCTURE-044, STRUCTURE-045 |
| PIG-JS.STRUCTURE.PACKAGE.2 | Conditional export order | Order conditional export keys from most to least specific with default last. | known \| unvalidated: quote tool-extracted | STRUCTURE-046 |
| PIG-JS.STRUCTURE.PACKAGE.3 | Internal aliases by imports field | Express package-internal aliases with the imports field, which Node resolves natively. | known \| unvalidated: quote tool-extracted | STRUCTURE-047 |
| PIG-JS.STRUCTURE.PACKAGE.4 | Relative paths within a project | Import files of one logical project by relative path so the project can move. | known \| unvalidated: holder position only (Google TS) \| unvalidated: quote not obtained (STRUCT-C28) | STRUCTURE-048 |

### PIG-JS.DEFENSE

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.DEFENSE | Defense defaults | Treat all data from outside the trust boundary as hostile and every interpreting sink as dangerous; use the platform's safe API for each sink, check what cannot be avoided against an allowlist, enforce the check in the language runtime where an API exists, and add a second layer for what slips through. | known | - |
| PIG-JS.DEFENSE.DOM | Document sinks and sanitizing | Untrusted data enters the page as text or built nodes, never as parsed markup, script, event-handler attribute or script URL; the rare HTML that must be rendered is sanitized last and passed through Trusted Types enforced in the page. | known | - |
| PIG-JS.DEFENSE.ORIGIN | Origin boundaries | Messages, frames, third-party scripts and storage are each treated as an origin boundary: verified senders, sandboxed and separate-origin untrusted content, integrity-pinned external code, no secrets in storage, and code that a strict CSP can run. Forged cross-site requests are refused by the page's own checks. | known | - |
| PIG-JS.DEFENSE.INJECTION | Injection classes | Each interpreter outside the page gets its own safe channel: no code from strings, no shell, parameters for queries, confined resolved paths, pure-data serialization and allowlisted resolved destinations. | known \| unvalidated: rests on single-source claims only | DEFENSE-026, DEFENSE-027 |
| PIG-JS.DEFENSE.PROTOTYPE | Prototype pollution defaults | Untrusted keys never reach a nested write, a merge or an inherited-property read, and dictionaries keyed by untrusted strings are Maps, Sets or null-prototype objects. | known | - |
| PIG-JS.DEFENSE.SECRETS | Secrets and cryptography defaults | Randomness comes from the platform CSPRNG, comparison of secrets is constant-time through the built-in function, passwords use a slow salted function, secrets stay out of code and responses, and crypto designs are reviewed. | known | - |
| PIG-JS.DEFENSE.HOST | Node process hardening | The Node process limits what hostile input can exhaust and what hostile code can reach: bounded regex work, parser limits, a strict HTTP parser, no exposed inspector, a seat-belt permission model and trusted module directories. | known | - |
| PIG-JS.DEFENSE.DOM.1 | Markup and attribute sinks | Untrusted data is inserted as text or built nodes; HTML-parsing sinks, event-handler attributes and unquoted attribute values never carry it. | known \| conflict: setAttribute unconditionally safe, OWASP DOM XSS sheet \| unvalidated: MDN TrustedScript condition inferred | DEFENSE-028, DEFENSE-029, DEFENSE-030, DEFENSE-031, DEFENSE-032, DEFENSE-033, DEFENSE-034 |
| PIG-JS.DEFENSE.DOM.2 | URL and navigation sinks | A URL that selects code to load or a page to navigate to is a sink: only allowlisted or Trusted values reach it. | known | - |
| PIG-JS.DEFENSE.DOM.3 | Sanitizing HTML | Untrusted HTML that must be rendered goes through the native Sanitizer API where available, otherwise a reputable library, immediately before insertion and never modified afterwards. | known \| conflict: library-first sanitizing, OWASP and MDN naming DOMPurify \| unvalidated: advice to keep the sanitizer current is inferred | DEFENSE-035, DEFENSE-036, DEFENSE-037, DEFENSE-038, DEFENSE-039, DEFENSE-040 |
| PIG-JS.DEFENSE.DOM.4 | Trusted Types enforcement | Injection sinks accept only typed values produced by named policies, rolled out in report-only mode, then enforced; Trusted Types is a gate, not a sanitizer. | known \| conflict: default policy as normal practice, Roth et al. USENIX 2024, for third-party code \| unvalidated: rests on claims marked inferred or open (DOMSEC-C19, DOMSEC-C22) \| unvalidated: quote not obtained (DOMSEC-C19) | DEFENSE-041, DEFENSE-042, DEFENSE-043, DEFENSE-044, DEFENSE-045, DEFENSE-046, DEFENSE-047, DEFENSE-048, DEFENSE-049, DEFENSE-050 |
| PIG-JS.DEFENSE.DOM.5 | DOM clobbering | Application state never lives on window or document, named-property reads are type-checked, and sanitizers neutralize id and name. | known | DEFENSE-051, DEFENSE-052, DEFENSE-053, DEFENSE-054 |
| PIG-JS.DEFENSE.DOM.6 | Framework output and escape hatches | Framework default encoding is relied on and every documented escape hatch is a sink that receives sanitized input only. | known | - |
| PIG-JS.DEFENSE.ORIGIN.1 | Cross-origin messages | A page listens only for messages it expects, verifies origin by exact match, validates every message and names an exact target origin. | known | DEFENSE-055, DEFENSE-056, DEFENSE-057, DEFENSE-058, DEFENSE-059 |
| PIG-JS.DEFENSE.ORIGIN.2 | Frames and window links | Untrusted and vendor content lives in sandboxed iframes from a separate origin; target=_blank links carry rel=noopener noreferrer explicitly; the own page refuses to be framed. | known \| conflict: explicit rel unnecessary because the HTML Standard implies noopener, HTML Standard | DEFENSE-060, DEFENSE-061, DEFENSE-062, DEFENSE-063, DEFENSE-064 |
| PIG-JS.DEFENSE.ORIGIN.3 | Third-party and service worker code | External scripts are pinned and integrity-checked, a data layer is not mistaken for a sandbox, and service workers come only from the own origin. | known | DEFENSE-065, DEFENSE-066, DEFENSE-067, DEFENSE-068, DEFENSE-069 |
| PIG-JS.DEFENSE.ORIGIN.4 | Web storage | Web Storage holds no secrets because every script of the origin reads it, and what is read from it or from messages is validated. | known \| unvalidated: validation rule inferred from a T2 finding and a T3 catalogue | DEFENSE-070, DEFENSE-071, DEFENSE-072 |
| PIG-JS.DEFENSE.ORIGIN.5 | CSP-ready code and policy handoff | Code runs under a strict CSP without exceptions; the policy and its deployment, CORS and JSONP rules belong to web_architecture. | known \| deferred: policy deployment owned by web_architecture | DEFENSE-073, DEFENSE-074, DEFENSE-075, DEFENSE-076, DEFENSE-077, DEFENSE-078, DEFENSE-079, DEFENSE-080 |
| PIG-JS.DEFENSE.ORIGIN.6 | Cross-site request forgery | A state-changing request that authenticated cookies can trigger from another site is accepted only with an unforgeable token or a trusted origin signal, never through a safe method, and never on one layer where script injection exists. | known | - |
| PIG-JS.DEFENSE.INJECTION.1 | No code from strings | Browser and Node code never compiles untrusted strings, whether through eval, Function, string timers, node:vm or a template engine; lint rules enforce the language-level cases. | known | - |
| PIG-JS.DEFENSE.INJECTION.2 | OS commands | A child process receives a program and an argument array, never a shell string built from input. | known \| unvalidated: the stronger form (no shell string from input, sanitized or not) is inferred from OWASP's parameterization principle; Node's own sentence states only the unsanitized case | DEFENSE-081, DEFENSE-082 |
| PIG-JS.DEFENSE.INJECTION.3 | SQL and NoSQL queries | Values go through the driver's parameter channel, MongoDB filters take typed scalars, server-side JavaScript in the database is off. | known \| conflict: escape dynamic identifiers with pg-format, node-postgres docs | DEFENSE-083, DEFENSE-084, DEFENSE-085, DEFENSE-086, DEFENSE-087, DEFENSE-088 |
| PIG-JS.DEFENSE.INJECTION.4 | File paths and archives | A path from input is resolved and checked inside its base, archive entries never choose their location, uploaded files are named, stored and bounded by the server, and the file is opened without a prior check. | known \| unvalidated: Node-specific recipe inferred, one T2 ground for canonicalization | - |
| PIG-JS.DEFENSE.INJECTION.5 | Deserialization | Untrusted data is parsed with data-only parsers, XML external entities included; code-reviving serializers are rejected. | known | - |
| PIG-JS.DEFENSE.INJECTION.6 | Outbound requests | Outbound requests go to allowlisted hosts, are connected to the validated address and follow no unvetted redirects. | known | - |
| PIG-JS.DEFENSE.PROTOTYPE.1 | Key writes and reads | No nested write with untrusted keys, no unfiltered merge and no __proto__ accessor; the own-property read for untrusted keys is the rule of PIG-JS.SUBSET.OBJECTS.6. | known | DEFENSE-089, DEFENSE-090, DEFENSE-092 |
| PIG-JS.DEFENSE.PROTOTYPE.2 | Dictionaries for untrusted keys | Map or Set first, null-prototype objects when a plain object is required, parsed JSON keys untrusted. | known \| unvalidated: rests on claims marked inferred or open (TYPES-C50) | DEFENSE-093, DEFENSE-094, DEFENSE-095 |
| PIG-JS.DEFENSE.PROTOTYPE.3 | Hardening and evidence | Application configuration is frozen, built-ins are locked down only where tested, and --disable-proto is never the only defence. | known \| conflict: never modify built-ins, SUBSET branch \| unvalidated: quote not obtained (DOMSEC-C52) | DEFENSE-096, DEFENSE-097, DEFENSE-098, DEFENSE-099 |
| PIG-JS.DEFENSE.SECRETS.1 | Randomness | Tokens and keys come from the platform CSPRNG with at least 128 bits; Math.random and non-v4 UUIDs are rejected. | known | DEFENSE-100, DEFENSE-101, DEFENSE-102 |
| PIG-JS.DEFENSE.SECRETS.2 | Cryptographic APIs and tokens | SubtleCrypto designs are reviewed by a knowledgeable person, encryption uses authenticated modes, and a token is accepted only on the verifier's terms: its algorithm, keys, issuer and audience are fixed by the verifier, never chosen by the token. | known \| unvalidated: single T1 source; Node crypto page truncated in every fetch \| unvalidated: authenticated-encryption rule rests on one source (OWASP), restricted to principles | DEFENSE-103, DEFENSE-104 |
| PIG-JS.DEFENSE.SECRETS.3 | Password storage | Passwords use Argon2id, else scrypt, bcrypt or PBKDF2 at OWASP minimums. | known \| unvalidated: quote tool-extracted \| unvalidated: single T1 position \| unvalidated: rests on claims marked inferred or open (SRVSEC-C11) | DEFENSE-105, DEFENSE-106 |
| PIG-JS.DEFENSE.SECRETS.4 | Constant-time comparison | Secrets are compared with timingSafeEqual on equal-length digests; no hand-written constant-time code, no BigInt for crypto. | known \| unvalidated: Node crypto text read in v6 docs only; the current timingSafeEqual entry could not be re-read (page truncated in every fetch, browser tool did not answer) \| unvalidated: rests on claims marked inferred or open (SRVSEC-C14) | DEFENSE-107, DEFENSE-108, DEFENSE-109, DEFENSE-110, DEFENSE-111, DEFENSE-112, DEFENSE-113 |
| PIG-JS.DEFENSE.SECRETS.5 | Secret handling | Secrets stay out of code, environment variables are a weaker fallback, and detection and rotation are routine. | known \| unvalidated: source says consider (secrets detection at the developer level); the MUST is the build's choice under the max rule; rotation has no quote of its own, single source | DEFENSE-114, DEFENSE-115 |
| PIG-JS.DEFENSE.SECRETS.6 | Leakage through output and memory | Errors reach clients generically, uninitialized Buffers and diagnostic reports do not leak, and a secure heap limits shared-host exposure. | known \| unvalidated: rests on claims marked inferred or open (RUNTIME-C52) \| unvalidated: quote not obtained (RUNTIME-C13, RUNTIME-C15, RUNTIME-C52) | DEFENSE-116, DEFENSE-117, DEFENSE-118, DEFENSE-119, DEFENSE-120 |
| PIG-JS.DEFENSE.HOST.1 | Permission model | The permission model is a seat belt for trusted code with narrow grants, known symlink and descriptor limits and a patched Node. | known \| conflict: permission model contains hostile or compromised dependencies, Node best-practices page \| unvalidated: rests on claims marked inferred or open (RUNSEC-C40) | DEFENSE-121, DEFENSE-122, DEFENSE-123, DEFENSE-124 |
| PIG-JS.DEFENSE.HOST.2 | Inspector exposure | The inspector is never public, never in production and never activated by SIGUSR1. | known \| unvalidated: single T1 source, quote tool-extracted | DEFENSE-125 |
| PIG-JS.DEFENSE.HOST.3 | HTTP parsing and smuggling | The strict HTTP parser stays on, the front end normalizes ambiguous requests, and no control character reaches a header. | known \| unvalidated: rests on single-source claims only | DEFENSE-126, DEFENSE-127, DEFENSE-128 |
| PIG-JS.DEFENSE.HOST.4 | Regex cost | Input length and repetition are bounded, nested quantifiers avoided, a non-backtracking engine preferred where one exists. | known \| unvalidated: rests on claims marked inferred or open (RUNSEC-C35) | DEFENSE-129, DEFENSE-130, DEFENSE-131, DEFENSE-132, DEFENSE-133 |
| PIG-JS.DEFENSE.HOST.5 | Parser resource limits | Parsers have size, depth and number limits and Node is patched against parser hash collisions. | known \| unvalidated: single T2 source for the Node patch rule | DEFENSE-134, DEFENSE-135 |
| PIG-JS.DEFENSE.HOST.6 | Module load path | Directories Node loads modules from are trusted and hardened. | known \| unvalidated: single T1 source | DEFENSE-136 |
| PIG-JS.DEFENSE.DOM.2.1 | Script URL sinks | script.src, Worker constructors, importScripts and serviceWorker.register receive only allowlisted or Trusted URLs. | known \| unvalidated: quote not obtained (DOMSEC-C24) | DEFENSE-137 |
| PIG-JS.DEFENSE.DOM.2.2 | Redirect targets | Automatic redirects go only to destinations on an allowlist. | known \| unvalidated: quote tool-extracted \| unvalidated: mechanism from a T3 catalogue only \| unvalidated: rests on single-source claims only | DEFENSE-138 |
| PIG-JS.DEFENSE.DOM.2.3 | URL validation by parsing | A URL is validated by parsing it and comparing scheme, canonical host and effective port with an explicit allowlist, with userinfo and dangerous protocols refused, rather than by substring tests. | known \| unvalidated: inferred from DOMSEC-C57, SECGAP2-C70, C71, C73 and C74, each step grounded by a claim but the composed rule stated whole by no source; parser-differential examples are open (SECGAP2-C75) \| unvalidated: quote not obtained (DOMSEC-C57) | DEFENSE-139, DEFENSE-259, DEFENSE-260, DEFENSE-261, DEFENSE-262, DEFENSE-263, DEFENSE-264 |
| PIG-JS.DEFENSE.DOM.6.1 | Escape hatches | Escape hatches of a framework are treated as sinks needing sanitized input; the per-framework documentation facts are recorded here. | known | DEFENSE-140, DEFENSE-184, DEFENSE-141, DEFENSE-142, DEFENSE-143, DEFENSE-144, DEFENSE-145, DEFENSE-146 |
| PIG-JS.DEFENSE.DOM.6.2 | Framework default encoding | Angular and Vue document their default encoding; rely on it for interpolation and bindings. | known \| unvalidated: single T1 source, vendor facts only | DEFENSE-147, DEFENSE-148 |
| PIG-JS.DEFENSE.DOM.6.3 | htmx hardening facts | htmx documents escaping, scrubbing, hx-disable and configuration options as its security tools; recorded as facts. | known \| unvalidated: single T1 source, vendor facts only | DEFENSE-149, DEFENSE-150, DEFENSE-151 |
| PIG-JS.DEFENSE.INJECTION.1.1 | Strings as code | Untrusted strings never reach eval, Function or string timers; JSON.parse replaces eval for data. | known \| unvalidated: quote not obtained (ASYNC-C33) | DEFENSE-152, DEFENSE-153, DEFENSE-154, DEFENSE-155, DEFENSE-156, DEFENSE-157 |
| PIG-JS.DEFENSE.INJECTION.1.2 | The vm module | node:vm is never used to run untrusted code. | known \| unvalidated: single T1 source, quote tool-extracted | DEFENSE-158, DEFENSE-159 |
| PIG-JS.DEFENSE.INJECTION.4.1 | Containment check | A path is canonicalized, symlinks resolved, and only then compared to the base directory, never by a raw string-prefix test. | known \| unvalidated: Node-specific recipe inferred, one T2 ground for canonicalization \| unvalidated: rests on single-source claims only | DEFENSE-160, DEFENSE-161, DEFENSE-162, DEFENSE-163, DEFENSE-164, DEFENSE-165, DEFENSE-217, DEFENSE-218, DEFENSE-219 |
| PIG-JS.DEFENSE.INJECTION.4.2 | Archive extraction | Archive entry names and symlinks never decide where files land. | known | DEFENSE-166, DEFENSE-167 |
| PIG-JS.DEFENSE.INJECTION.4.3 | Check then use | A file is opened directly and errors handled, never pre-checked. | known \| unvalidated: single T1 source on a v10 page, extension inferred \| unvalidated: quote not obtained (RUNTIME-C18) | DEFENSE-168 |
| PIG-JS.DEFENSE.INJECTION.4.4 | Node containment recipe | A path derived from input is confirmed to stay inside its base directory by one stated Node recipe: resolve, follow symlinks, then compare against the base with a separator. | undecided \| missing: no admitted source states the symlink-resolving Node call (fs.realpath) or the separator-aware containment test; the pieces that are grounded sit on PIG-JS.DEFENSE.INJECTION.4.1 | DEFENSE-169 |
| PIG-JS.DEFENSE.INJECTION.5.1 | Structured clone | Structured clone is a data-only copy; its fitness for untrusted input is open. | known | DEFENSE-170 |
| PIG-JS.DEFENSE.INJECTION.5.2 | YAML and legacy serializers | Untrusted YAML goes to js-yaml 4 or later; node-serialize unserialize never sees untrusted input. | known \| unvalidated: single T1 source, facts only, advice partly inferred | DEFENSE-171, DEFENSE-172 |
| PIG-JS.DEFENSE.INJECTION.5.3 | v8.deserialize | A buffer reaches v8.deserialize only after a trusted party's integrity check has been verified, and the result is copied into a new object from validated fields; whether the function is safe on its own is stated by no admitted source. | known \| unvalidated: inferred from SECGAP2-C83, C84, C85, SRVSEC-C44 and the general deserialization rules (SRVSEC-C45, RUNSEC-C44, held on the principle js-philosophy:DEFENSE.INJECTION.5); whether v8.deserialize is safe for untrusted bytes is open \| unvalidated: rests on single-source claims only \| unvalidated: the MUST NOT is the strict form of sources that say could or if available (CWE-502: use signing or sealing if available, an HMAC could be used; OWASP: they could sign them); no source says v8.deserialize is unsafe | DEFENSE-173, DEFENSE-233, DEFENSE-234, DEFENSE-235 |
| PIG-JS.DEFENSE.INJECTION.6.1 | Destination rules | Hosts are matched against an allowlist, URLs are parsed with the WHATWG URL class, and a deny-list is the weaker fallback. | known \| unvalidated: rests on single-source claims only \| unvalidated: a rule has no claim of its own, it is the build's judgment | DEFENSE-174, DEFENSE-183, DEFENSE-175, DEFENSE-176 |
| PIG-JS.DEFENSE.INJECTION.6.2 | Connection to the validated address | The address is resolved once, checked, and connected to; DNS rebinding is the attack this closes. | known \| unvalidated: pinned-connection recipe inferred from three rows \| unvalidated: rests on single-source claims only | DEFENSE-177, DEFENSE-178, DEFENSE-179 |
| PIG-JS.DEFENSE.INJECTION.6.3 | Redirect handling | A redirect lets the remote server choose the next destination; the rule, and how Node's fetch applies it, is stated once on Node fetch redirect semantics. | known | DEFENSE-270 |
| PIG-JS.DEFENSE.INJECTION.6.4 | Node fetch redirect semantics | Node's fetch is told what to do with a redirect (error when none is expected, manual with revalidation otherwise), its automatic header stripping is not relied on, and the Node release is kept current. | known \| unvalidated: rests on single-source claims about undici's code and documentation (SECGAP2-C86, C87, C89, C90, C91), read at an unpinned commit; Node documents none of it (SRVSEC-C37 open); the strict rule (error, or manual with revalidation) is the build's choice over ASVS 'unless intended' | DEFENSE-181, DEFENSE-182, DEFENSE-265, DEFENSE-266, DEFENSE-267, DEFENSE-268, DEFENSE-271 |
| PIG-JS.DEFENSE.SECRETS.2.1 | Token and JWT verification | A token is accepted only after the verifier applies its own fixed policy: allowed algorithms, trusted pre-configured keys bound to the issuer, audience, validity time and type; nothing in the token chooses any of them. | known \| unvalidated: several MUSTs are strict forms of weaker wording (ASVS 9.1.2: ideally only symmetric or asymmetric; OWASP JWT sheet: if possible hardcode the algorithm, do not mix), exp on every token is stricter than ASVS 9.2.1 (validity is checked if exp is present), and three rules rest on one source each (SECGAP2-C04, C08, C15) | DEFENSE-190, DEFENSE-191, DEFENSE-192, DEFENSE-193, DEFENSE-194, DEFENSE-195, DEFENSE-196, DEFENSE-197, DEFENSE-198, DEFENSE-199, DEFENSE-200, DEFENSE-201 |
| PIG-JS.DEFENSE.SECRETS.2.2 | Token library settings | The JavaScript token libraries accept more than the policy allows unless told otherwise: the verify call gets an explicit algorithm list, the library is current, and decoding is never verification. | known \| unvalidated: rests on claims marked inferred or open (SECGAP2-C11, SECGAP2-C14) | DEFENSE-202, DEFENSE-203, DEFENSE-204, DEFENSE-205, DEFENSE-206, DEFENSE-207, DEFENSE-272 |
| PIG-JS.DEFENSE.INJECTION.1.3 | Template injection | A template is code: untrusted input never becomes template source, and user-supplied expression content is sanitized or off. | known \| unvalidated: the acceptable-when row rests on one T3 source (the author's position) | DEFENSE-208, DEFENSE-209, DEFENSE-210 |
| PIG-JS.DEFENSE.INJECTION.1.4 | Handlebars and EJS | The two template engines with admitted security guidance are used within what their own documents state: no unescaped output of untrusted values, no untrusted ASTs, no end-user access to EJS, current versions. | known \| unvalidated: rests on claims marked inferred or open (SECGAP2-C39) | DEFENSE-211, DEFENSE-212, DEFENSE-213, DEFENSE-214, DEFENSE-215, DEFENSE-216, DEFENSE-275, DEFENSE-276 |
| PIG-JS.DEFENSE.INJECTION.4.5 | Upload content checks | An uploaded file is accepted by an extension allowlist and a server-side content check and is re-encoded or scanned before use; the client's Content-Type is never trusted. | known \| unvalidated: rests on claims marked inferred or open (SECGAP2-C48) | DEFENSE-220, DEFENSE-221, DEFENSE-222 |
| PIG-JS.DEFENSE.INJECTION.4.6 | Upload storage, names and limits | Uploads get server-generated names, live outside the web root, are never run as code, and are bounded in size, count and unpacked size before the file is accepted. | known | DEFENSE-223, DEFENSE-224, DEFENSE-225, DEFENSE-226, DEFENSE-227, DEFENSE-228 |
| PIG-JS.DEFENSE.INJECTION.5.4 | XML and external entities | XML from outside is parsed with DTDs and external entity resolution off, schema validation uses XSD, and a missing hardening setting is a failure, not a fallback. | known \| unvalidated: rests on claims marked inferred or open (SECGAP2-C22) \| unvalidated: rests on single-source claims only | DEFENSE-229, DEFENSE-230, DEFENSE-231, DEFENSE-232, DEFENSE-277 |
| PIG-JS.DEFENSE.HOST.3.1 | Header field values | No CR, LF or NUL reaches a header name or value, whether the application sets a header or passes a value to a client library; Node's own check is relied on and applied before a value is reused. | known \| unvalidated: three rules rest on one source each (SECGAP2-C26, C27, C28) | DEFENSE-236, DEFENSE-237, DEFENSE-238, DEFENSE-239, DEFENSE-240, DEFENSE-273, DEFENSE-274 |
| PIG-JS.DEFENSE.HOST.3.2 | Connection-specific fields | HTTP/2 and HTTP/3 requests are accepted only without CR, LF or CRLF in fields and without connection-specific fields. | known \| unvalidated: rests on single-source claims only | DEFENSE-241 |
| PIG-JS.DEFENSE.ORIGIN.2.1 | Framing of the own page | The page forbids being framed by other origins with frame-ancestors on every response, sent as a header, with X-Frame-Options only as a fallback that states the same policy. | known \| conflict: frame-ancestors alone, since ASVS 3.4.6 requires the directive and is silent on a fallback, and CSP3 with RFC 7034 hold that the directive supersedes the header; OWASP and MDN both also send X-Frame-Options \| unvalidated: the same-policy condition for the fallback is inferred from the ALLOW-FROM support gap (SECGAP2-C67) | DEFENSE-242, DEFENSE-243, DEFENSE-244, DEFENSE-245 |
| PIG-JS.DEFENSE.ORIGIN.2.2 | Frame-busting and double clicks | Frame-busting scripts are not a defence, and a sensitive action behind a double click needs server-enforced transaction authorization. | known \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (SECGAP2-C65) | DEFENSE-246, DEFENSE-247, DEFENSE-248 |
| PIG-JS.DEFENSE.ORIGIN.6.1 | Primary defence | A synchronizer or signed double-submit token, unique per session, random and kept out of URLs and logs, is the primary defence, layered with the Sec-Fetch-Site check and an Origin or Referer fallback; tokens are compared in constant time. | known \| unvalidated: token-first and the layering are stricter than both sources, which list a Fetch Metadata check among the primary defences (OWASP, MDN); the acceptable-when row is the build's judgment about the condition and has no claim of its own | DEFENSE-249, DEFENSE-250, DEFENSE-251, DEFENSE-252, DEFENSE-253, DEFENSE-269 |
| PIG-JS.DEFENSE.ORIGIN.6.2 | Methods and API endpoints | Safe methods never change state, and an API that relies on CORS preflight makes sure no request can reach it without one. | known | DEFENSE-254, DEFENSE-255 |
| PIG-JS.DEFENSE.ORIGIN.6.3 | SameSite and CSRF libraries | SameSite is defence in depth set per cookie purpose, and csurf is not adopted for new code. | known \| unvalidated: the csurf rule rests on a facts-only source (the repository archive notice) and is inferred; the Express blog wording was not re-confirmed (SECGAP2-C62) | DEFENSE-256, DEFENSE-257, DEFENSE-258 |

### PIG-JS.DEPENDENCIES

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.DEPENDENCIES | Dependencies (JavaScript defaults) | Concrete npm-era rules that keep third-party code trusted: deterministic installs, blocked install scripts, deliberate updates, screened evidence, safe publishing, and a framework choice made on trust evidence. | known | - |
| PIG-JS.DEPENDENCIES.INSTALL | Install | What is fetched and what runs at install is deterministic and reviewed. | known | - |
| PIG-JS.DEPENDENCIES.UPDATE | Update | Versions move on a schedule the project controls, on supported runtimes and toolchains, with findings triaged. | known \| gap: cooldown length and audit threshold have no admitted source | - |
| PIG-JS.DEPENDENCIES.SCREEN | Screening evidence | Tool outputs about a package are read within the limits their authors state. | known | - |
| PIG-JS.DEPENDENCIES.PUBLISH | Publish | A published package leaves with short-lived credentials, reviewed contents and runnable JavaScript. | known \| gap: target assurance level undecided | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE | Framework evidence | The facts that bear on trusting a front-end framework as the largest dependency, taken from each framework's own documentation and from measured usage, with every gap shown. | known \| gap: governance, usage, support window, type support and default escaping missing for several candidates (the Angular and Vue facts sit in PIG-JS.DEFENSE.DOM.6.2) | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | Framework short list | The candidates a team may choose among, cut by trust evidence under the max rule: the platform first, then four frameworks. | risky \| unvalidated: gates are the build's judgment, no admitted source states them \| conflict: keep Vue and drop the platform baseline, an earlier proposal (inferred) | DEPENDENCIES-078 |
| PIG-JS.DEPENDENCIES.INSTALL.1 | Frozen install | CI and production install exactly the committed lockfile and fail on any mismatch. | known | DEPENDENCIES-032 |
| PIG-JS.DEPENDENCIES.INSTALL.2 | Install scripts blocked | Code that runs at install time is approved package by package, never by default. | known | DEPENDENCIES-033, DEPENDENCIES-034 |
| PIG-JS.DEPENDENCIES.INSTALL.3 | Non-registry sources | Dependencies from git or tarball URLs bypass registry controls and enter only as named exceptions. | known \| unvalidated: claim is inferred from npm 12 defaults \| unvalidated: rests on single-source claims only | DEPENDENCIES-035 |
| PIG-JS.DEPENDENCIES.INSTALL.4 | Owned scope for internal packages | Internal package names cannot be shadowed by a public package. | known \| unvalidated: rests on single-source claims only | DEPENDENCIES-036 |
| PIG-JS.DEPENDENCIES.INSTALL.5 | Expected repository and inventory | Third-party components, direct and transitive, are inventoried and each is checked to come from its expected repository, with no dependency confusion risk. | known \| unvalidated: rests on single-source claims only | DEPENDENCIES-086 |
| PIG-JS.DEPENDENCIES.UPDATE.1 | Release-age cooldown | A freshly published version is not installed at once, while security fixes are never delayed. | known \| gap: effectiveness unmeasured; claim relabelled single-source \| unvalidated: rests on single-source claims only | DEPENDENCIES-037 |
| PIG-JS.DEPENDENCIES.UPDATE.2 | Supported runtime and toolchain | Production runs on versions that still receive security fixes, and the toolchain is pinned to what the framework supports. | known \| unvalidated: rests on single-source claims only | DEPENDENCIES-038, DEPENDENCIES-081, DEPENDENCIES-039, DEPENDENCIES-082 |
| PIG-JS.DEPENDENCIES.UPDATE.3 | Audit in CI | Known-vulnerability data is checked against the committed lockfile and read as triage. | known \| unvalidated: no admitted source states running npm audit in CI as a practice (SRC-149 gives behaviour facts only) \| unvalidated: rests on single-source claims only | DEPENDENCIES-040, DEPENDENCIES-080 |
| PIG-JS.DEPENDENCIES.SCREEN.1 | Scorecard as per-check evidence | Scorecard results inform adoption per check and never stand for safety. | known \| unvalidated: single T1 restricted source, limits restated | DEPENDENCIES-041 |
| PIG-JS.DEPENDENCIES.SCREEN.2 | Publisher-trust downgrade check | A package manager may compare a version's publishing trust with earlier releases; availability is recorded, reliance is not recommended. | known \| unvalidated: single T1 restricted source, tool fact only | DEPENDENCIES-042 |
| PIG-JS.DEPENDENCIES.SCREEN.3 | Typosquatting screening | A package name is checked against well-known names before adoption, so that a look-alike package is not installed by mistake. | undecided \| missing: no admitted T1 source states a screening procedure for adding a dependency; the screening methods rest on one T3 paper and one T3 preprint | DEPENDENCIES-087, DEPENDENCIES-088, DEPENDENCIES-089, DEPENDENCIES-090 |
| PIG-JS.DEPENDENCIES.PUBLISH.1 | CI publishing credentials | Publishing from CI uses short-lived, workflow-bound credentials, and provenance follows from it. | known | DEPENDENCIES-043, DEPENDENCIES-044, DEPENDENCIES-045, DEPENDENCIES-084 |
| PIG-JS.DEPENDENCIES.PUBLISH.2 | Tarball contents | What leaves in the tarball is reviewed before every publish, and secrets never enter it. | known | DEPENDENCIES-046 |
| PIG-JS.DEPENDENCIES.PUBLISH.3 | Ship JavaScript | Consumers receive code their runtime can load. | known \| unvalidated: claim is inferred from one runtime limitation \| unvalidated: rests on single-source claims only | DEPENDENCIES-047 |
| PIG-JS.DEPENDENCIES.PUBLISH.4 | Target assurance level | Which SLSA Build level a published package aims at. | undecided \| missing: no admitted source recommends a target level | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | Support window | Whether a framework states which versions receive security fixes, and until when. | known \| conflict: main htmx docs site documents 2.x as current (SRC-213) \| unvalidated: htmx 4.0.0 release date open \| gap: Svelte, Solid and Vue state no support window | DEPENDENCIES-048, DEPENDENCIES-083, DEPENDENCIES-049, DEPENDENCIES-050, DEPENDENCIES-051, DEPENDENCIES-052, DEPENDENCIES-053, DEPENDENCIES-054 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | Governance | Who owns and steers a framework, as stated by the project. | known \| gap: no source for Angular, Svelte, htmx | DEPENDENCIES-055, DEPENDENCIES-056, DEPENDENCIES-057, DEPENDENCIES-058, DEPENDENCIES-059 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.3 | Type support | How each framework relates to the type layer. | known \| gap: htmx has no source | DEPENDENCIES-060, DEPENDENCIES-061, DEPENDENCIES-062, DEPENDENCIES-063, DEPENDENCIES-064, DEPENDENCIES-065 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | Measured usage | What measured usage can and cannot support. | known \| gap: figures exist for React, jQuery and platform features only | DEPENDENCIES-066, DEPENDENCIES-067, DEPENDENCIES-068, DEPENDENCIES-069, DEPENDENCIES-070 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | Vulnerability record | Advisories and reporting channels as facts about response, not as a ranking. | known \| gap: Solid and Angular advisories lack affected versions or policy | DEPENDENCIES-071, DEPENDENCIES-072, DEPENDENCIES-073, DEPENDENCIES-074, DEPENDENCIES-075 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 | Platform baseline | Framework-free components are the default and the first candidate. | known \| unvalidated: the platform-first default is the build's judgment, no claim states it (FW-C46 says only that the platform offers components) \| unvalidated: rests on single-source claims only | DEPENDENCIES-079, DEPENDENCIES-076, DEPENDENCIES-077 |
| PIG-JS.DEPENDENCIES.UPDATE.1.1 | Cooldown length beyond tool defaults | How long to wait when the tool default is not what the project wants. | undecided \| missing: no admitted source gives a measured duration | - |
| PIG-JS.DEPENDENCIES.UPDATE.3.1 | Failing severity of the audit gate | Which severity fails the build. | undecided \| missing: no admitted source names a level | - |

### PIG-JS.VERIFICATION

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.VERIFICATION | Verification defaults | A JavaScript or TypeScript change merges only after lint, format and tests have run unattended and passed. | known | - |
| PIG-JS.VERIFICATION.LINT | Linting | Lint rules run on every change with a configuration that makes findings binding and reviewable, so that the safe subset is enforced by machine. | known | - |
| PIG-JS.VERIFICATION.FORMAT | Formatting | Layout is produced and checked by machine so that review never spends attention on it. | known | - |
| PIG-JS.VERIFICATION.TESTS | Test code | Test code in JavaScript is written so that a pass cannot hide a wrong comparison or a race. | known | - |
| PIG-JS.VERIFICATION.LINT.1 | Rule set | The configuration states which rules run on which files, from a maintained baseline upward. | known | - |
| PIG-JS.VERIFICATION.LINT.2 | Enforcement | A finding changes the exit status of the run, so CI can block on it, cheaply enough to run every time. | known \| unvalidated: a rule has no claim of its own, it is the build's judgment | VERIFICATION-045 |
| PIG-JS.VERIFICATION.LINT.3 | Security findings triage | Findings of security lint rules are leads for a human, because the rules over-report. | known \| unvalidated: rests on single-source claims only | VERIFICATION-029 |
| PIG-JS.VERIFICATION.LINT.4 | Linter selection | ESLint with typescript-eslint runs the rules, because it is the family with documented type-aware rules, a security plugin and the rule documents the other branches cite. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source \| unvalidated: rests on single-source claims only | VERIFICATION-030 |
| PIG-JS.VERIFICATION.FORMAT.1 | Dedicated formatter | Layout belongs to a formatter that sees the whole file, not to lint rules. | known \| unvalidated: single T2 source | VERIFICATION-031, VERIFICATION-032 |
| PIG-JS.VERIFICATION.FORMAT.2 | Formatting checked in CI | Unformatted code fails the build, so formatting needs no reviewer. | known \| unvalidated: rests on single-source claims only | VERIFICATION-033 |
| PIG-JS.VERIFICATION.FORMAT.3 | Formatter selection | Prettier prints the code, run apart from the linter, because it only prints and its check mode has documented exit codes. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source | VERIFICATION-034, VERIFICATION-035, VERIFICATION-036 |
| PIG-JS.VERIFICATION.TESTS.1 | Runner selection | node:test runs the suite, because it ships with Node, is stable and adds no dependency to the code that is trusted with the build. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source \| unvalidated: rests on claims marked inferred or open (QUALITY-C24, QUALITY-C26, QUALITY-C27, QUALITY-C28) \| unvalidated: rests on single-source claims only | VERIFICATION-037, VERIFICATION-038, VERIFICATION-039, VERIFICATION-040 |
| PIG-JS.VERIFICATION.TESTS.2 | Strict assertions | Assertions compare with strict semantics, so unequal values never pass. | known \| unvalidated: rests on single-source claims only | VERIFICATION-041, VERIFICATION-042 |
| PIG-JS.VERIFICATION.TESTS.3 | Condition waits | Asynchronous tests wait for a condition, never for elapsed time. | known \| unvalidated: single T2 source, transfer inferred | VERIFICATION-043 |
| PIG-JS.VERIFICATION.LINT.1.1 | Config file and scoping | One flat configuration file at the project root, with rules scoped to files and ordered general to specific. | known \| unvalidated: rests on single-source claims only | VERIFICATION-020 |
| PIG-JS.VERIFICATION.LINT.1.2 | Baseline rule set | Every project starts from the tool's maintained recommended set, for TypeScript too, so that the floor is not hand-built. | known \| unvalidated: baseline suitability inferred \| unvalidated: rests on single-source claims only | VERIFICATION-021 |
| PIG-JS.VERIFICATION.LINT.1.3 | Strict rule set | Teams with enough TypeScript proficiency take the stricter set, accepting that it changes between minor versions. | known \| unvalidated: rests on single-source claims only | VERIFICATION-022 |
| PIG-JS.VERIFICATION.LINT.1.4 | Type-aware rules | Rules that need type information run, because the defects they find (a floating promise) are invisible to syntax-only rules. | known \| gap: no admitted figure for the cost, see G-L20 \| unvalidated: rests on single-source claims only | VERIFICATION-023, VERIFICATION-024 |
| PIG-JS.VERIFICATION.LINT.2.1 | Warnings fail the run | Warnings count as failures in CI, so nothing is tolerated by default silence. | known \| unvalidated: rests on claims marked inferred or open (QUALITY-C05) \| unvalidated: rests on single-source claims only | VERIFICATION-025 |
| PIG-JS.VERIFICATION.LINT.2.2 | Tool failure is not a finding | A broken configuration is told apart from lint findings in CI, so a broken gate is not read as a pass or as code defects. | known \| unvalidated: rests on single-source claims only | VERIFICATION-026 |
| PIG-JS.VERIFICATION.LINT.2.3 | Stale suppressions reported | A suppression that no longer suppresses anything is flagged, so old exceptions cannot hide new errors. | known \| unvalidated: rests on single-source claims only | VERIFICATION-027 |
| PIG-JS.VERIFICATION.LINT.2.4 | Repeat runs are cheap | Unchanged files are not re-linted, so the gate stays fast enough to run on every change. | known \| unvalidated: rests on claims marked inferred or open (QUALITY-C08) \| unvalidated: rests on single-source claims only | VERIFICATION-028 |

### PIG-JS.RUNTIME

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.RUNTIME | Runtime behaviour in JavaScript | In Node and the browser, speed and memory choices are made from measurements taken with the runtime's own tools and a sound method, and a running process is diagnosed from symptom to cause with those tools. | known \| unvalidated: 83 percent of the branch claims are single-source | - |
| PIG-JS.RUNTIME.MEASURE | Measure before changing | Code is changed for speed or memory only after a measurement of the real workload shows where the cost is; engine-level tuning and speed-motivated API swaps are hypotheses until measured. | known \| conflict: unmeasured micro-optimization advice, MDN (SRC-083, SRC-088) | - |
| PIG-JS.RUNTIME.METHOD | Benchmark method | Benchmarks follow a statistical method in a controlled environment, so that a reported difference is a real one. | known \| unvalidated: figures rest on one T2 harness document | - |
| PIG-JS.RUNTIME.DIAGNOSE | Diagnosis of a running process | A running Node process is diagnosed from its symptom to its cause with built-in tools, context recorded first. | known \| unvalidated: single T1 pages, quotes tool-extracted | - |
| PIG-JS.RUNTIME.MEMORY | Memory diagnosis and retention | Memory problems are classified, signalled, localized and handled with the engine's own diagnostics, with production-safe capture and no unintended retention. | known \| unvalidated: single T1 pages, quotes tool-extracted; container sizing open | - |
| PIG-JS.RUNTIME.MEASURE.1 | Profile before optimizing | The cost is located with the V8 profiler on the running application before any code is changed. | known \| unvalidated: quote tool-extracted; the rule is inferred from the docs workflow \| unvalidated: rests on single-source claims only | RUNTIME-006 |
| PIG-JS.RUNTIME.MEASURE.2 | Engine-level tuning needs a measurement | Array element kinds, hidden classes, closure creation and prototype mutation are tuned only where a measurement shows the cost; mechanism alone does not justify restructuring. | known \| conflict: restructuring on mechanism alone, MDN (SRC-083, SRC-088) \| unvalidated: single T2 source for the measured statement (SRC-302) | RUNTIME-007, RUNTIME-008, RUNTIME-009, RUNTIME-010, RUNTIME-011, RUNTIME-012 |
| PIG-JS.RUNTIME.MEASURE.3 | Callback file APIs only on a measured need | File system calls use the promise API unless a measurement shows the callback API's lower time or allocation cost is needed. | known \| unvalidated: quote tool-extracted; the measurement gate is inferred from the docs wording \| unvalidated: rests on single-source claims only | RUNTIME-013 |
| PIG-JS.RUNTIME.METHOD.1 | Compare runs statistically | Comparisons use many runs and a significance test, with a stricter threshold when many comparisons are made. | known \| unvalidated: Node figures single T2 source, JavaScript transfer of the principle inferred | RUNTIME-014 |
| PIG-JS.RUNTIME.METHOD.2 | Quiet measurement environment | Benchmarks run in isolation on a machine whose CPU frequency scaling is set to performance mode. | known \| unvalidated: single T2 source \| unvalidated: quote not obtained (RUNTIME-C60) | RUNTIME-015 |
| PIG-JS.RUNTIME.DIAGNOSE.1 | Context and symptom first | The environment, symptoms, reproduction steps and recent changes are recorded before investigating, and the diagnostic path is chosen by symptom: behaviour, memory, or latency and CPU. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C25) | RUNTIME-016 |
| PIG-JS.RUNTIME.DIAGNOSE.2 | Event loop health in production | Event loop health is measured in production, not guessed, and each measurement observer is removed when done. | known \| unvalidated: C23 no quote recorded, C24 quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C23) | RUNTIME-017, RUNTIME-018 |
| PIG-JS.RUNTIME.DIAGNOSE.3 | Built-in profilers | CPU and heap profiles come from the profilers built into Node; no third-party tool is needed to capture them. | known \| unvalidated: quote tool-extracted, the no-third-party step is inferred; perf flags partly unreconfirmed \| unvalidated: quote not obtained (RUNTIME-C22) | RUNTIME-019, RUNTIME-020 |
| PIG-JS.RUNTIME.MEMORY.1 | Classify the memory problem | A memory problem is first classed as running out of memory or as inefficient use, which selects the tool. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C26) | RUNTIME-021 |
| PIG-JS.RUNTIME.MEMORY.2 | Leak signals | Cheap signals, the emitter listener warning and the GC trace pattern, are read before anything is captured. | known \| unvalidated: quote tool-extracted, the advice to justify raising the listener limit is inferred \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C47) | RUNTIME-022 |
| PIG-JS.RUNTIME.MEMORY.3 | Leak localization by snapshot comparison | A leak is localized by comparing two heap snapshots taken around the suspect path and following large positive deltas to their retainers. | known \| unvalidated: quote tool-extracted \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C45) | RUNTIME-023 |
| PIG-JS.RUNTIME.MEMORY.4 | Production capture | In production the sampling heap profiler runs and snapshots are taken only where a crash is harmless and the trigger is never public. | known \| unvalidated: quote tool-extracted; snapshot cost on current Node versions unmeasured here \| unvalidated: quote not obtained (RUNTIME-C46) | RUNTIME-024, RUNTIME-025, RUNTIME-026, RUNTIME-027 |
| PIG-JS.RUNTIME.MEMORY.5 | Intended retention | Only intended state stays reachable: weak collections for object-keyed metadata, no weak references, unpooled Buffers for long-retained chunks. | known \| unvalidated: quote tool-extracted; the ECMA-262 processing notes for WeakRef were not read \| unvalidated: rests on single-source claims only \| unvalidated: quote not obtained (RUNTIME-C14, RUNTIME-C29) | RUNTIME-028 |
| PIG-JS.RUNTIME.MEMORY.6 | Heap limit and the collector | The heap limit is read from the runtime and changed only for a measured need, and the collector is left to run itself. | known \| unvalidated: the measured-need rule is inferred; no quote recorded for the limit statement \| unvalidated: quote not obtained (RUNTIME-C48) | RUNTIME-029, RUNTIME-030, RUNTIME-031 |
| PIG-JS.RUNTIME.MEMORY.6.1 | Heap limit inside a container | How the default heap limit and the limit flag behave under a container or cgroup memory limit. | undecided \| missing: no admitted source | - |

### Intentlinks inside pig-js-defaults: within branches

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.SUBSET.STRICTNESS.2 | PIG-JS.SUBSET.STRICTNESS.1 | refines | ES modules are the way strictness is obtained without a directive. |
| 2 | PIG-JS.SUBSET.MUTATION.1 | PIG-JS.SUBSET.STRICTNESS.1 | requires | A write to a frozen object throws only under strict mode. |
| 3 | PIG-JS.SUBSET.OBJECTS.1 | PIG-JS.SUBSET.STRICTNESS.1 | requires | A detached method sees undefined as its receiver only in strict code. |
| 4 | PIG-JS.SUBSET.EVOLUTION.3 | PIG-JS.SUBSET.STRICTNESS.1 | requires | Octal literals and the with statement are errors only under strict mode, which is what makes forbidding them enforceable. |
| 5 | PIG-JS.SUBSET.CONVERSION.2 | PIG-JS.SUBSET.CONVERSION.1 | refines | The null check is the one place where loose equality could be kept; the rule forbids even that. |
| 6 | PIG-JS.SUBSET.CONVERSION.3 | PIG-JS.SUBSET.CONVERSION.1 | refines | Strict equality is never true for NaN, so NaN needs its own test. |
| 7 | PIG-JS.SUBSET.CONVERSION.6 | PIG-JS.SUBSET.CONVERSION.2 | refines | Nullish coalescing and chaining test exactly the null-or-undefined set that the null check names. |
| 8 | PIG-JS.SUBSET.NUMBERS.3 | PIG-JS.SUBSET.NUMBERS.2 | requires | BigInt is the carrier for integers beyond the safe range. |
| 9 | PIG-JS.SUBSET.NUMBERS.4 | PIG-JS.SUBSET.NUMBERS.2 | requires | The safe range is the threshold above which integers must cross JSON as strings or BigInt. |
| 10 | PIG-JS.SUBSET.EVOLUTION.2 | PIG-JS.SUBSET.EVOLUTION.1 | refines | Temporal is stage 4, so the stage rule admits it; target support is the second check. |
| 11 | PIG-JS.SUBSET.OBJECTS.3 | PIG-JS.SUBSET.MUTATION.1 | refines | Hash private fields escape freeze and seal, so privacy and immutability are separate tools. |
| 12 | PIG-JS.CONTRACTS.LAYER.3 | PIG-JS.CONTRACTS.LAYER.1 | requires | TypeScript is a contract only while a separate check runs; execution alone checks nothing |
| 13 | PIG-JS.CONTRACTS.LAYER.4 | PIG-JS.CONTRACTS.LAYER.3 | requires | The erasable-syntax rule is enforced by the same compiler run that checks types |
| 14 | PIG-JS.CONTRACTS.LAYER.5 | PIG-JS.CONTRACTS.LAYER.4 | refines | The Node-aligned options include the option that enforces erasable syntax |
| 15 | PIG-JS.CONTRACTS.LAYER.2 | PIG-JS.CONTRACTS.LAYER.1 | conflicts | A project uses one type layer: JSDoc-checked JavaScript applies only where TypeScript cannot |
| 16 | PIG-JS.CONTRACTS.STRICT.1 | PIG-JS.CONTRACTS.LAYER.1 | requires | The strict family exists only inside the compiler that the type layer runs |
| 17 | PIG-JS.CONTRACTS.STRICT.4 | PIG-JS.CONTRACTS.STRICT.1 | refines | Pinning keeps the strict family from changing under the code between releases |
| 18 | PIG-JS.CONTRACTS.ESCAPE.3 | PIG-JS.CONTRACTS.ESCAPE.2 | refines | Leaked any catches what the explicit-any rule cannot see in code that never wrote the word |
| 19 | PIG-JS.CONTRACTS.ESCAPE.1 | PIG-JS.CONTRACTS.BOUNDARY.1 | dataflow | An unknown value is narrowed by the validation that BOUNDARY.1 and BOUNDARY.2 perform |
| 20 | PIG-JS.CONTRACTS.ESCAPE.5 | PIG-JS.CONTRACTS.BOUNDARY.2 | requires | The explicit run-time check preferred over an assertion is, at a boundary, the schema parse |
| 21 | PIG-JS.CONTRACTS.BOUNDARY.1 | PIG-JS.CONTRACTS.BOUNDARY.2 | dataflow | The unknown result of parsing text flows into schema validation |
| 22 | PIG-JS.CONTRACTS.BOUNDARY.5 | PIG-JS.CONTRACTS.BOUNDARY.2 | refines | A library is only a realisation of the schema rule |
| 23 | PIG-JS.CONTRACTS.MODEL.1 | PIG-JS.CONTRACTS.LAYER.1 | requires | Discriminated unions and never checks exist only in TypeScript, not in checked JavaScript with the weaker mode |
| 24 | PIG-JS.CONTROL.PROMISES.3 | PIG-JS.CONTROL.PROCESS.1 | dataflow | A promise nobody observes becomes an unhandled rejection that the host escalates, so the observation rules feed the rejection policy. |
| 25 | PIG-JS.CONTROL.BOUNDS.2 | PIG-JS.CONTROL.BOUNDS.1 | requires | A timeout is expressed as an abort signal and ends an operation through the signal protocol. |
| 26 | PIG-JS.CONTROL.FLOW.2 | PIG-JS.CONTROL.BOUNDS.1 | requires | Cancelling a pipeline passes an abort signal to it. |
| 27 | PIG-JS.CONTROL.ERRORS.4 | PIG-JS.CONTROL.PROCESS.2 | dataflow | An emitter error without a listener is thrown and reaches the uncaught-exception path. |
| 28 | PIG-JS.CONTROL.SCHEDULING.3 | PIG-JS.CONTROL.ERRORS.4 | dataflow | A worker's uncaught exception surfaces only as error and exit events, which are emitter failures. |
| 29 | PIG-JS.CONTROL.SCHEDULING.2 | PIG-JS.CONTROL.SCHEDULING.3 | dataflow | CPU work that blocks the event loop is moved to a worker; partitioning on the loop is the weaker alternative. |
| 30 | PIG-JS.CONTROL.PROMISES.1 | PIG-JS.CONTROL.PROMISES.3 | refines | A promise that a chain fails to return is a floating promise, the case this node narrows. |
| 31 | PIG-JS.CONTROL.PROCESS.4 | PIG-JS.CONTROL.PROCESS.2 | requires | A shutdown handler must end the process itself, as the uncaught-exception path does. |
| 32 | PIG-JS.STRUCTURE.DIRECTION.2 | PIG-JS.STRUCTURE.DIRECTION.1 | requires | Mechanical detection is how the no-cycle rule is kept true after the first commit. |
| 33 | PIG-JS.STRUCTURE.NODE.3 | PIG-JS.STRUCTURE.LOADING.4 | requires | require() of an ES module fails with ERR_REQUIRE_ASYNC_MODULE when any module in the graph uses top-level await. |
| 34 | PIG-JS.STRUCTURE.NODE.3 | PIG-JS.STRUCTURE.LOADING.3 | requires | Dynamic import is the route from CommonJS to ES modules that use top-level await. |
| 35 | PIG-JS.STRUCTURE.LOADING.6 | PIG-JS.STRUCTURE.SURFACE.4 | requires | Barrel files are built from wildcard re-exports, so the collision rule applies to them. |
| 36 | PIG-JS.STRUCTURE.PACKAGE.1 | PIG-JS.STRUCTURE.SURFACE.2 | refines | The exports field is the package-level form of the minimal exported surface. |
| 37 | PIG-JS.STRUCTURE.PACKAGE.2 | PIG-JS.STRUCTURE.PACKAGE.1 | refines | Conditional exports are keys inside the exports field. |
| 38 | PIG-JS.STRUCTURE.LOADING.6 | PIG-JS.STRUCTURE.PACKAGE.1 | requires | The one place a re-exporting module remains is the package's public entry point. |
| 39 | PIG-JS.STRUCTURE.DIRECTION.3 | PIG-JS.STRUCTURE.DIRECTION.1 | refines | Layering would constrain the direction of imports beyond acyclicity. |
| 40 | PIG-JS.DEFENSE.DOM.1 | PIG-JS.DEFENSE.DOM.3 | requires | HTML that must be rendered is handed to the sanitizer rather than inserted through a sink. |
| 41 | PIG-JS.DEFENSE.DOM.4 | PIG-JS.DEFENSE.DOM.3 | requires | A Trusted Types createHTML policy wraps a vetted sanitizer; the gate is only as good as that function. |
| 42 | PIG-JS.DEFENSE.DOM.5 | PIG-JS.DEFENSE.DOM.3 | requires | The sanitizer neutralizes id and name, which is the HTML-only injection route to clobbering. |
| 43 | PIG-JS.DEFENSE.DOM.6.1 | PIG-JS.DEFENSE.DOM.1 | refines | A framework escape hatch is a markup sink and obeys the sink rules. |
| 44 | PIG-JS.DEFENSE.ORIGIN.1 | PIG-JS.DEFENSE.DOM.1 | dataflow | Validated message data is still a source that ends at DOM sinks. |
| 45 | PIG-JS.DEFENSE.ORIGIN.4 | PIG-JS.DEFENSE.DOM.1 | dataflow | Data read from web storage is a source that ends at DOM sinks. |
| 46 | PIG-JS.DEFENSE.ORIGIN.5 | PIG-JS.DEFENSE.DOM.1 | requires | Strict-CSP code needs addEventListener and no inline handlers, which the markup sink rules already enforce. |
| 47 | PIG-JS.DEFENSE.INJECTION.1.1 | PIG-JS.DEFENSE.DOM.4 | requires | In browsers string compilation is gated by Trusted Types and the trusted-types-eval keyword. |
| 48 | PIG-JS.DEFENSE.DOM.2.3 | PIG-JS.DEFENSE.INJECTION.6.1 | dataflow | Parsing a URL with the standard parser before judging scheme and origin is one rule in browser and server. |
| 49 | PIG-JS.DEFENSE.INJECTION.4.1 | PIG-JS.DEFENSE.INJECTION.4.3 | requires | A containment check is sound only if the file is opened without a gap between check and use. |
| 50 | PIG-JS.DEFENSE.INJECTION.6.2 | PIG-JS.DEFENSE.INJECTION.6.1 | requires | Pinning the connection to a validated address applies to hosts that passed the destination rules. |
| 51 | PIG-JS.DEFENSE.INJECTION.6.3 | PIG-JS.DEFENSE.INJECTION.6.2 | requires | Each redirect target is checked by the same resolved-address validation. |
| 52 | PIG-JS.DEFENSE.INJECTION.6.2 | PIG-JS.DEFENSE.HOST.2 | dataflow | The rebinding attack closed for outbound requests also reaches a local inspector. |
| 53 | PIG-JS.DEFENSE.PROTOTYPE.2 | PIG-JS.DEFENSE.INJECTION.5 | dataflow | Keys in parsed JSON reach merges and assignments, which is where pollution happens. |
| 54 | PIG-JS.DEFENSE.HOST.1 | PIG-JS.DEFENSE.INJECTION.4.1 | requires | Permission grants are paths with documented symlink and prefix limits, so containment checks remain needed. |
| 55 | PIG-JS.DEFENSE.HOST.4 | PIG-JS.DEFENSE.HOST.5 | requires | Bounding input length before matching relies on size limits at the parsing boundary. |
| 56 | PIG-JS.DEPENDENCIES.INSTALL.1 | PIG-JS.DEPENDENCIES.INSTALL.2 | requires | Version-pinned script approvals bind only under a frozen install. |
| 57 | PIG-JS.DEPENDENCIES.UPDATE.3 | PIG-JS.DEPENDENCIES.UPDATE.1 | dataflow | Audit findings identify the security updates that bypass the cooldown. |
| 58 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | PIG-JS.DEPENDENCIES.UPDATE.2 | dataflow | The chosen framework supplies the compatibility table the toolchain is pinned to. |
| 59 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Stated support windows are gate A of the short list. |
| 60 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Stated governance is gate C of the short list. |
| 61 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.3 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Type support is carried as a fact of each candidate, not a gate. |
| 62 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Usage figures bound what the list may claim: context only. |
| 63 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Advisories and reporting channels are facts about response, carried per candidate. |
| 64 | PIG-JS.VERIFICATION.LINT.2 | PIG-JS.VERIFICATION.LINT.1 | requires | Enforcement acts on the rules the configuration selects. |
| 65 | PIG-JS.VERIFICATION.LINT.2.3 | PIG-JS.VERIFICATION.LINT.2.1 | requires | A stale suppression is reported as a warning by default, so it binds only while warnings fail the run. |
| 66 | PIG-JS.VERIFICATION.LINT.1.2 | PIG-JS.VERIFICATION.FORMAT.1 | requires | The baseline can leave out layout rules only because a dedicated formatter owns layout. |
| 67 | PIG-JS.VERIFICATION.FORMAT.2 | PIG-JS.VERIFICATION.FORMAT.1 | requires | A check mode needs a formatter whose output is the reference layout. |
| 68 | PIG-JS.VERIFICATION.LINT.1.3 | PIG-JS.VERIFICATION.LINT.1.2 | refines | The strict set extends the recommended set for proficient teams. |
| 69 | PIG-JS.VERIFICATION.TESTS.2 | PIG-JS.VERIFICATION.TESTS.1 | requires | Assertion mode is chosen inside the runner that executes the tests. |
| 70 | PIG-JS.RUNTIME.DIAGNOSE.3 | PIG-JS.RUNTIME.MEASURE.1 | dataflow | Profiles captured with the built-in profilers are what the profile-before-optimizing step reads. |
| 71 | PIG-JS.RUNTIME.MEASURE.2 | PIG-JS.RUNTIME.METHOD.1 | requires | The measurement that justifies an engine-level change must follow the statistical method. |
| 72 | PIG-JS.RUNTIME.MEASURE.3 | PIG-JS.RUNTIME.MEASURE.1 | requires | Swapping to the callback file API needs the measurement that shows the cost. |
| 73 | PIG-JS.RUNTIME.DIAGNOSE.1 | PIG-JS.RUNTIME.MEMORY.1 | dataflow | A symptom classed as memory hands over to the memory classification. |
| 74 | PIG-JS.RUNTIME.MEMORY.1 | PIG-JS.RUNTIME.MEMORY.2 | dataflow | The class of problem selects which cheap signals to read. |
| 75 | PIG-JS.RUNTIME.MEMORY.2 | PIG-JS.RUNTIME.MEMORY.3 | dataflow | A leak signal triggers the snapshot comparison. |
| 76 | PIG-JS.RUNTIME.MEMORY.3 | PIG-JS.RUNTIME.MEMORY.4 | requires | Taking snapshots on a live process presumes the production capture rules. |
| 77 | PIG-JS.RUNTIME.MEMORY.4 | PIG-JS.RUNTIME.MEMORY.6 | dataflow | The limit read from the runtime sets when near-limit capture fires. |
| 78 | PIG-JS.RUNTIME.MEMORY.6.1 | PIG-JS.RUNTIME.MEMORY.6 | refines | The container case would specialize the heap limit rule once a source exists. |
| 79 | PIG-JS.DEFENSE.SECRETS.2.2 | PIG-JS.DEFENSE.SECRETS.2.1 | refines | The library settings carry the algorithm allowlist and the key rules of the verification policy into each call. |
| 80 | PIG-JS.DEFENSE.ORIGIN.6.1 | PIG-JS.DEFENSE.SECRETS.4 | requires | A CSRF token is a secret compared in constant time with the same built-in function. |
| 81 | PIG-JS.DEFENSE.ORIGIN.6.2 | PIG-JS.DEFENSE.ORIGIN.6.1 | refines | Method discipline and preflight reliance narrow what the token or origin check has to cover. |
| 82 | PIG-JS.DEFENSE.ORIGIN.2.2 | PIG-JS.DEFENSE.ORIGIN.2.1 | refines | A double click acts in a top-level window, where the framing restrictions of the page do not apply. |
| 83 | PIG-JS.DEFENSE.INJECTION.1.4 | PIG-JS.DEFENSE.INJECTION.1.3 | refines | The engine-specific rules apply the no-untrusted-template rule to the two engines with admitted guidance. |
| 84 | PIG-JS.DEFENSE.INJECTION.4.6 | PIG-JS.DEFENSE.INJECTION.4.1 | requires | A client file name that must be used goes through the containment check before any path is built. |
| 85 | PIG-JS.DEFENSE.INJECTION.4.6 | PIG-JS.DEFENSE.INJECTION.4.2 | requires | Size and file-count limits on compressed uploads apply before the archive is extracted. |
| 86 | PIG-JS.DEFENSE.DOM.2.2 | PIG-JS.DEFENSE.DOM.2.3 | requires | A redirect target is compared with the allowlist only after it is parsed. |
| 87 | PIG-JS.DEFENSE.INJECTION.6.4 | PIG-JS.DEFENSE.INJECTION.6.3 | refines | The rule on Node fetch redirect semantics carries the purpose stated here: a remote server must not choose the next destination unchecked. |
| 88 | PIG-JS.DEFENSE.HOST.3.2 | PIG-JS.DEFENSE.HOST.3.1 | refines | HTTP/2 and HTTP/3 add the connection-specific fields to what must never reach a header. |
| 89 | PIG-JS.DEPENDENCIES.INSTALL.5 | PIG-JS.DEPENDENCIES.INSTALL.4 | requires | The expected-repository check covers the namespaces that an owned scope does not close. |
| 90 | PIG-JS.DEPENDENCIES.SCREEN.3 | PIG-JS.DEPENDENCIES.INSTALL.5 | requires | A package that passes a name screen still has to come from the expected repository. |

### Intentlinks inside pig-js-defaults: across branches (resolved from proposals)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.STRUCTURE.FORMAT.1 | PIG-JS.SUBSET.STRICTNESS.2 | requires | The module-format rules presuppose that ES modules are the chosen format, which SUBSET decides; cycles, side-effect-free imports and the Node ESM facts build on ES modules as the unit. |
| 2 | PIG-JS.STRUCTURE.LOADING.1 | PIG-JS.SUBSET.STRICTNESS.2 | refines | A module runs once however often it is imported (stated at SUBSET.STRICTNESS.2); the import-order rule builds on that fact and adds the rule to export a function for repeatable work. |
| 3 | PIG-JS.SUBSET.STRICTNESS | PIG-JS.VERIFICATION.LINT.1.1 | requires | no-var and prefer-const are lint rules written in the lint configuration; that is what enforces fixed, block-scoped bindings. |
| 4 | PIG-JS.SUBSET.CONVERSION | PIG-JS.VERIFICATION.LINT.1.1 | requires | eqeqeq and no-implicit-coercion are the lint rules, written in the lint configuration, that enforce the conversion rules. |
| 5 | PIG-JS.SUBSET.CONVERSION.5 | PIG-JS.CONTRACTS.BOUNDARY | requires | Validation of numeric input belongs to boundary parsing, which this node says Number conversion is not. |
| 6 | PIG-JS.SUBSET.CONVERSION.6 | PIG-JS.CONTRACTS.MODEL.3 | requires | Optional chaining is used only on values whose type can really be nullish; the rule and its type condition live in CONTRACTS.MODEL.3. |
| 7 | PIG-JS.SUBSET.NUMBERS.4 | PIG-JS.CONTRACTS.BOUNDARY.1 | dataflow | Large integers cross a JSON boundary as strings; the boundary parser decodes them. |
| 8 | PIG-JS.SUBSET.NUMBERS.4 | PIG-JS.DEFENSE.PROTOTYPE.2 | requires | JSON.parse of untrusted input has its own prototype-key hazard (RUNSEC-C13, overlap O14). |
| 9 | PIG-JS.STRUCTURE.SURFACE.3 | PIG-JS.SUBSET.MUTATION.1 | requires | Freezing is shallow, so a frozen exported object still has mutable nested state; the freeze mechanics are owned by SUBSET and this rule builds read-only exports on them. |
| 10 | PIG-JS.DEFENSE.PROTOTYPE.3 | PIG-JS.SUBSET.MUTATION.1 | requires | Freezing application configuration as a hardening step inherits the shallow-freeze limit stated at SUBSET.MUTATION.1. |
| 11 | PIG-JS.SUBSET.OBJECTS.5 | PIG-JS.DEFENSE.PROTOTYPE.3 | conflicts | Freezing or locking down built-ins as hardening is the sanctioned exception to leaving built-ins alone; scope (high-sensitivity, tested environments) separates the two. |
| 12 | PIG-JS.SUBSET.OBJECTS.5 | PIG-JS.RUNTIME.MEASURE.2 | requires | Setting a prototype at creation, not later, is an engine-optimisation fact held by RUNTIME (STRUCT-C43). |
| 13 | PIG-JS.DEFENSE.PROTOTYPE.1 | PIG-JS.SUBSET.OBJECTS.6 | requires | The own-property read for untrusted keys is the rule of SUBSET.OBJECTS.6 (merged row SUBSET-051); this node holds the pollution writes, merges and __proto__. |
| 14 | PIG-JS.SUBSET.EVOLUTION.5 | PIG-JS.VERIFICATION.FORMAT.1 | requires | A formatter, not review, is what would enforce statement termination. |
| 15 | PIG-JS.SUBSET.EVOLUTION.1 | PIG-JS.DEPENDENCIES.UPDATE.2 | requires | Target runtime floor (Node LTS, browser Baseline) is the second input to the feature-maturity check. |
| 16 | PIG-JS.CONTRACTS.LAYER.3 | PIG-JS.VERIFICATION.LINT.2 | requires | The no-emit type check is a CI gate |
| 17 | PIG-JS.CONTRACTS.ESCAPE.2 | PIG-JS.VERIFICATION.LINT.1.4 | requires | The explicit-any, unsafe-assignment and directive rules are lint rules that VERIFICATION configures |
| 18 | PIG-JS.CONTRACTS.ESCAPE.6 | PIG-JS.VERIFICATION.LINT.2.3 | requires | Suppression handling is a lint and review rule |
| 19 | PIG-JS.CONTRACTS.STRICT.4 | PIG-JS.DEPENDENCIES.UPDATE.2 | requires | A pinned compiler is one case of the lockfile and update policy |
| 20 | PIG-JS.CONTRACTS.LAYER.6 | PIG-JS.STRUCTURE.FORMAT | refines | Type-only exports and import forms are module conventions that STRUCTURE owns |
| 21 | PIG-JS.CONTRACTS.LAYER.4 | PIG-JS.SUBSET.EVOLUTION | refines | The erasable-syntax rule excludes enum and namespaces; SUBSET.EVOLUTION holds the general rule that new code uses only settled features and no legacy syntax (SUBSET lists neither enum nor namespaces). |
| 22 | PIG-JS.CONTRACTS.MODEL.2 | PIG-JS.SUBSET.CONVERSION | refines | Explicit narrowing is the typed side of the equality and coercion rules |
| 23 | PIG-JS.CONTRACTS.BOUNDARY.1 | PIG-JS.CONTROL.ERRORS.2 | requires | JSON.parse throws SyntaxError, which CONTROL's error propagation must handle |
| 24 | PIG-JS.CONTRACTS.BOUNDARY.1 | PIG-JS.DEFENSE.PROTOTYPE.2 | dataflow | A parsed object with an own __proto__ key is harmless until merged; the parse result flows to the hostile-key rules, which treat parsed JSON keys as untrusted. |
| 25 | PIG-JS.CONTRACTS.BOUNDARY.2 | PIG-JS.DEFENSE.PROTOTYPE.1 | dataflow | The schema allowlist is the first defence against prototype pollution: only declared keys reach the merge and lookup code that PROTOTYPE.1 guards. |
| 26 | PIG-JS.CONTRACTS.BOUNDARY.3 | PIG-JS.DEFENSE.PROTOTYPE.1 | refines | Binding request data to a dedicated allowlisted object is the key-write control against mass assignment, an untrusted-key hazard beside pollution; DEFENSE has no separate mass-assignment node. |
| 27 | PIG-JS.DEFENSE.INJECTION | PIG-JS.CONTRACTS.BOUNDARY.4 | requires | Allowlisted input validated before it reaches Node or language APIs underlies the command and path rules. |
| 28 | PIG-JS.DEFENSE.HOST.4 | PIG-JS.CONTRACTS.BOUNDARY.4 | requires | Allowlisted input validated before it reaches Node or language APIs underlies the regex input bounds. |
| 29 | PIG-JS.CONTROL.PROMISES.3 | PIG-JS.VERIFICATION.LINT.1.4 | requires | Type-aware lint rules that report floating and misused promises are what enforce these rules (rule documents are cited as positions only). |
| 30 | PIG-JS.CONTROL.ERRORS.2 | PIG-JS.CONTRACTS.STRICT.1 | requires | Typing caught values as unknown belongs with the type layer's strictness settings. |
| 31 | PIG-JS.CONTROL.SCHEDULING.2 | PIG-JS.DEFENSE.HOST | dataflow | Event-loop blocking by long computation, JSON or regular expressions is a denial-of-service lever. |
| 32 | PIG-JS.CONTROL.BOUNDS.2 | PIG-JS.DEFENSE.HOST | dataflow | HTTP server timeouts drop slow or idle connections, the defence against slow-request exhaustion. |
| 33 | PIG-JS.CONTROL.FLOW | PIG-JS.RUNTIME.MEMORY | dataflow | Unpaced streams cost memory and collection time, whose diagnosis lives in the runtime branch. |
| 34 | PIG-JS.CONTROL.PROMISES.5 | PIG-JS.SUBSET.EVOLUTION.1 | dataflow | Edition years of promise and error features feed the modern-feature baseline. |
| 35 | PIG-JS.CONTROL.BOUNDS.1 | PIG-JS.CONTRACTS.SIGNATURE | requires | A signal option on async APIs is part of declared API shape (coverage flags STRUCT-C50 to C54 as the API-shape cluster). |
| 36 | PIG-JS.STRUCTURE.FORMAT.3 | PIG-JS.CONTRACTS.LAYER.5 | requires | The type checker's module-resolution setting must match the host; the setting is a CONTRACTS decision. |
| 37 | PIG-JS.STRUCTURE.FORMAT.4 | PIG-JS.CONTRACTS.LAYER.4 | requires | The TypeScript namespace ban belongs with the type-layer rules. |
| 38 | PIG-JS.STRUCTURE.NODE.1 | PIG-JS.CONTRACTS.LAYER.5 | requires | Importing with the .ts extension under Node type stripping is a type-layer rule (TYPES-C06 sits here by routing). |
| 39 | PIG-JS.STRUCTURE.SURFACE.5 | PIG-JS.SUBSET.OBJECTS | requires | Class design rules (classes, this, private members) are owned by SUBSET. |
| 40 | PIG-JS.STRUCTURE.LOADING.4 | PIG-JS.CONTROL.PROCESS | requires | A never-resolving top-level await ends the process with status 13, which belongs with process-lifecycle rules. |
| 41 | PIG-JS.STRUCTURE.LOADING.5 | PIG-JS.VERIFICATION.LINT.2 | requires | Bundling and tree-shaking configuration is a build gate (boundary 08 QUALITY). |
| 42 | PIG-JS.STRUCTURE.DIRECTION.2 | PIG-JS.VERIFICATION.LINT.2 | requires | The severity of the cycle lint rule in CI is a gate decision owned by VERIFICATION. |
| 43 | PIG-JS.STRUCTURE.DIRECTION.3 | PIG-JS.VERIFICATION.LINT.2 | requires | If a layering rule is ever grounded, its enforcement is a lint-gate decision. |
| 44 | PIG-JS.STRUCTURE.PACKAGE.1 | PIG-JS.DEPENDENCIES.PUBLISH | requires | A package's public entry points are the interface that consumers and the supply chain see (boundary 07 SUPPLY). |
| 45 | PIG-JS.STRUCTURE.LOADING.6 | PIG-JS.RUNTIME.MEASURE.2 | requires | The barrel rule is motivated by load cost and rests on one synthetic measurement; a structure rule motivated by speed needs the measurement gate of RUNTIME. |
| 46 | PIG-JS.DEFENSE.PROTOTYPE.3 | PIG-JS.DEPENDENCIES.UPDATE | requires | Third-party pollution flaws (RUNSEC-C11 evidence) need the update policy owned by DEPENDENCIES. |
| 47 | PIG-JS.DEFENSE.INJECTION.1.1 | PIG-JS.VERIFICATION.LINT.1 | requires | The no-eval, no-implied-eval and no-new-func rules are enforced by the lint rule set owned by VERIFICATION. |
| 48 | PIG-JS.DEFENSE.SECRETS.5 | PIG-JS.VERIFICATION.LINT.2 | requires | Secret detection before commit is a gate owned by VERIFICATION. |
| 49 | PIG-JS.DEPENDENCIES.PUBLISH.2 | PIG-JS.DEFENSE.SECRETS.5 | requires | Secrets in published package contents are the leak class that the secret-handling rules of DEFENSE govern. |
| 50 | PIG-JS.DEFENSE.HOST.4 | PIG-JS.CONTROL.SCHEDULING.2 | requires | A blocked event loop is the failure CONTROL's timeout and load rules contain. |
| 51 | PIG-JS.DEFENSE.HOST.5 | PIG-JS.CONTRACTS.BOUNDARY | refines | Parser limits are part of parsing untrusted data at every trust boundary. |
| 52 | PIG-JS.DEFENSE.HOST.6 | PIG-JS.DEPENDENCIES.INSTALL | requires | Module resolution trust rests on the dependency and install policy of DEPENDENCIES. |
| 53 | PIG-JS.DEFENSE.INJECTION.4.3 | PIG-JS.CONTROL.ERRORS.2 | requires | Handling the error of a direct open is the explicit-failure rule of CONTROL. |
| 54 | PIG-JS.DEFENSE.INJECTION.5 | PIG-JS.CONTRACTS.BOUNDARY | requires | Parsing untrusted data into validated shapes is the boundary rule of CONTRACTS. |
| 55 | PIG-JS.DEFENSE.DOM.6 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE | dataflow | Framework security facts recorded in DEFENSE (escape hatches, default encoding, htmx hardening) feed the framework evidence in DEPENDENCIES; they are held once, here. |
| 56 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | PIG-JS.DEFENSE.DOM.6 | requires | Gate B of the short list, a documented security model, cites the per-framework facts held in DEFENSE.DOM.6 and does not restate them. |
| 57 | PIG-JS.DEPENDENCIES.UPDATE.3 | PIG-JS.VERIFICATION.LINT.2 | dataflow | The audit gate runs in CI under VERIFICATION. |
| 58 | PIG-JS.VERIFICATION.LINT.2 | PIG-JS.DEPENDENCIES.INSTALL.1 | requires | The CI job that runs the gate installs dependencies by the frozen-install rule of DEPENDENCIES. |
| 59 | PIG-JS.DEPENDENCIES.PUBLISH.3 | PIG-JS.CONTRACTS.LAYER.1 | requires | The type-layer decision determines what is compiled before publishing. |
| 60 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | PIG-JS.CONTRACTS.LAYER.1 | requires | The type-support criterion depends on the type-layer decision. |
| 61 | PIG-JS.VERIFICATION.LINT.1.4 | PIG-JS.CONTRACTS.LAYER.1 | requires | Type-aware rules need the type layer CONTRACTS decides, and TYPES-C44 binds tool support to the TypeScript 7.1 API. |
| 62 | PIG-JS.VERIFICATION.LINT.3 | PIG-JS.DEFENSE.INJECTION.1 | dataflow | Security lint findings are leads that feed DEFENSE's injection and eval rules. |
| 63 | PIG-JS.VERIFICATION.TESTS.2 | PIG-JS.SUBSET.CONVERSION.1 | refines | Strict assertions apply SUBSET's strict-equality rule to test code. |
| 64 | PIG-JS.RUNTIME.MEASURE.3 | PIG-JS.CONTROL.PROMISES.6 | refines | The speed-motivated exception to the promise-by-default choice of file APIs. |
| 65 | PIG-JS.RUNTIME.DIAGNOSE.2 | PIG-JS.CONTROL.SCHEDULING.2 | dataflow | Event loop utilization and delay measurements feed the event-loop blocking rules. |
| 66 | PIG-JS.RUNTIME.MEMORY.4 | PIG-JS.DEFENSE.HOST.2 | requires | A snapshot trigger endpoint must never be reachable by untrusted callers. |
| 67 | PIG-JS.RUNTIME.MEMORY.5 | PIG-JS.SUBSET.EVOLUTION | refines | Avoiding WeakRef and FinalizationRegistry is an instance of the features-to-avoid rule. |
| 68 | PIG-JS.RUNTIME.MEMORY.2 | PIG-JS.CONTROL.ERRORS.4 | requires | The emitter listener warning belongs with emitter error and listener handling. |
| 69 | PIG-JS.DEFENSE.SECRETS.2.1 | PIG-JS.CONTRACTS.BOUNDARY | requires | Token claims are untrusted data, parsed and validated at the trust boundary before they are used. |
| 70 | PIG-JS.DEFENSE.INJECTION.5.4 | PIG-JS.CONTRACTS.BOUNDARY | requires | XML is parsed into validated shapes at the boundary, and XSD validation is the shape check. |
| 71 | PIG-JS.DEFENSE.INJECTION.1.4 | PIG-JS.DEPENDENCIES.UPDATE.3 | requires | The version floors for Handlebars and EJS are enforced by the audit and update policy owned by DEPENDENCIES. |
| 72 | PIG-JS.DEFENSE.INJECTION.6.4 | PIG-JS.DEPENDENCIES.UPDATE.3 | requires | Keeping undici current is the update policy owned by DEPENDENCIES. |

### Inter links from pig-js-defaults to js-philosophy

Within a branch (each defaults node to the principle it renders), then across branches.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.SUBSET.CONVERSION | js-philosophy:SUBSET.VISIBLE | refines | Strict equality, explicit conversion and nullish operators are the concrete rules of visible conversion. |
| 2 | PIG-JS.SUBSET.STRICTNESS.1 | js-philosophy:SUBSET.FAILURE | refines | Strict mode is the language's loud-failure mode. |
| 3 | PIG-JS.SUBSET.MUTATION.1 | js-philosophy:SUBSET.FAILURE | refines | A frozen write fails loudly only in strict code. |
| 4 | PIG-JS.SUBSET.STRICTNESS.3 | js-philosophy:SUBSET.BINDING | refines | const and no var fix bindings by default. |
| 5 | PIG-JS.SUBSET.OBJECTS.3 | js-philosophy:SUBSET.BINDING | refines | Hash fields make privacy enforced instead of conventional. |
| 6 | PIG-JS.SUBSET.OBJECTS.1 | js-philosophy:SUBSET.BINDING | refines | An explicit receiver is the call-side half of enforced binding. |
| 7 | PIG-JS.SUBSET.EVOLUTION | js-philosophy:SUBSET.MATURITY | refines | Stage-4-only, retired legacy and untouched built-ins are the concrete settled-feature rules. |
| 8 | PIG-JS.SUBSET.OBJECTS.5 | js-philosophy:SUBSET.MATURITY | refines | Leaving built-ins unaltered keeps later language growth from changing the code's meaning. |
| 9 | PIG-JS.CONTRACTS.LAYER | js-philosophy:CONTRACTS.STATIC | refines | The type layer realises the static contract |
| 10 | PIG-JS.CONTRACTS.STRICT | js-philosophy:CONTRACTS.STATIC.2 | refines | Maximum strictness is the answer to a check that is evidence and not proof |
| 11 | PIG-JS.CONTRACTS.ESCAPE | js-philosophy:CONTRACTS.STATIC.2 | refines | Each escape hatch is a place where the check proves nothing |
| 12 | PIG-JS.CONTRACTS.MODEL | js-philosophy:CONTRACTS.STATIC | refines | Modelling lets the checker prove more |
| 13 | PIG-JS.CONTRACTS.BOUNDARY.1 | js-philosophy:CONTRACTS.STATIC.1 | requires | Because types are erased, parsed data is typed only after run-time validation |
| 14 | PIG-JS.CONTROL.PROMISES | js-philosophy:CONTROL.FAILURE | refines | The promise rules apply failure ownership to the asynchronous channel. |
| 15 | PIG-JS.CONTROL.ERRORS | js-philosophy:CONTROL.FAILURE | refines | The error rules apply failure ownership to values, causes and emitters. |
| 16 | PIG-JS.CONTROL.BOUNDS | js-philosophy:CONTROL.BOUNDS | refines | Signals, timeouts and caps are the JavaScript form of the bound. |
| 17 | PIG-JS.CONTROL.SCHEDULING | js-philosophy:CONTROL.SCHEDULING | refines | The scheduling rules apply the shared-thread principle. |
| 18 | PIG-JS.CONTROL.FLOW | js-philosophy:CONTROL.FLOW | refines | The stream rules apply pacing to Node and Web Streams. |
| 19 | PIG-JS.CONTROL.PROCESS | js-philosophy:CONTROL | refines | The process rules apply the designed end to Node hooks and handles. |
| 20 | PIG-JS.STRUCTURE.SURFACE.3 | js-philosophy:STRUCTURE.STATE.2 | refines | Read-only live bindings and no mutable exports are how JavaScript keeps shared state with one owner. |
| 21 | PIG-JS.DEFENSE | js-philosophy:DEFENSE | refines | The default renders the principle in JavaScript. |
| 22 | PIG-JS.DEFENSE.DOM | js-philosophy:DEFENSE.DOM | refines | The default renders the principle in JavaScript. |
| 23 | PIG-JS.DEFENSE.ORIGIN | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 24 | PIG-JS.DEFENSE.PROTOTYPE | js-philosophy:DEFENSE.PROTOTYPE | refines | The default renders the principle in JavaScript. |
| 25 | PIG-JS.DEFENSE.HOST | js-philosophy:DEFENSE.HOST | refines | The default renders the principle in JavaScript. |
| 26 | PIG-JS.DEFENSE.DOM.1 | js-philosophy:DEFENSE.DOM.1 | refines | The default renders the principle in JavaScript. |
| 27 | PIG-JS.DEFENSE.DOM.3 | js-philosophy:DEFENSE.DOM.2 | refines | The default renders the principle in JavaScript. |
| 28 | PIG-JS.DEFENSE.DOM.4 | js-philosophy:DEFENSE.DOM.2 | refines | The default renders the principle in JavaScript. |
| 29 | PIG-JS.DEFENSE.DOM.5 | js-philosophy:DEFENSE.DOM.3 | refines | The default renders the principle in JavaScript. |
| 30 | PIG-JS.DEFENSE.ORIGIN.2 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 31 | PIG-JS.DEFENSE.ORIGIN.3 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 32 | PIG-JS.DEFENSE.PROTOTYPE.1 | js-philosophy:DEFENSE.PROTOTYPE.1 | refines | The default renders the principle in JavaScript. |
| 33 | PIG-JS.DEFENSE.PROTOTYPE.2 | js-philosophy:DEFENSE.PROTOTYPE.1 | refines | The default renders the principle in JavaScript. |
| 34 | PIG-JS.DEFENSE.PROTOTYPE.3 | js-philosophy:DEFENSE.PROTOTYPE.2 | refines | The default renders the principle in JavaScript. |
| 35 | PIG-JS.DEFENSE.HOST.3 | js-philosophy:DEFENSE.HOST.3 | refines | The default renders the principle in JavaScript. |
| 36 | PIG-JS.DEFENSE.HOST.4 | js-philosophy:DEFENSE.HOST.1 | refines | The default renders the principle in JavaScript. |
| 37 | PIG-JS.DEFENSE.HOST.4 | js-philosophy:DEFENSE.HOST.2 | refines | The default renders the principle in JavaScript. |
| 38 | PIG-JS.DEPENDENCIES.INSTALL.1 | js-philosophy:DEPENDENCIES.CHANGE.1 | refines | The frozen install realizes the reproducible tree. |
| 39 | PIG-JS.DEPENDENCIES.INSTALL.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Blocking install scripts acts on the install-script risk signal. |
| 40 | PIG-JS.DEPENDENCIES.INSTALL.3 | js-philosophy:DEPENDENCIES.CHANGE.3 | refines | Git and tarball sources are what a lockfile review has to explain. |
| 41 | PIG-JS.DEPENDENCIES.UPDATE.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Running only maintained versions applies maintenance as a signal. |
| 42 | PIG-JS.DEPENDENCIES.UPDATE.3 | js-philosophy:DEPENDENCIES.EVIDENCE.2 | refines | The audit gate is the tool form of triaging findings. |
| 43 | PIG-JS.DEPENDENCIES.SCREEN.1 | js-philosophy:DEPENDENCIES.EVIDENCE.1 | refines | Scorecard is read within its stated limits like any other signal. |
| 44 | PIG-JS.DEPENDENCIES.SCREEN.2 | js-philosophy:DEPENDENCIES.EVIDENCE.1 | refines | A trust-downgrade check is one more graded signal. |
| 45 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | A stated support window is the maintenance signal for a framework. |
| 46 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Stated governance is the maintainer-count signal for a framework. |
| 47 | PIG-JS.VERIFICATION.LINT.2 | js-philosophy:VERIFICATION | refines | CI exit status is how a lint finding blocks the merge in JavaScript. |
| 48 | PIG-JS.VERIFICATION.LINT.1.2 | js-philosophy:VERIFICATION | refines | The recommended rule set is the switched-on analysis for JavaScript. |
| 49 | PIG-JS.RUNTIME.MEMORY.2 | js-philosophy:RUNTIME.MEMORY.1 | refines | Leak signals are read against the reachability model. |
| 50 | PIG-JS.RUNTIME.MEMORY.5 | js-philosophy:RUNTIME.MEMORY.1 | refines | Weak collections change what counts as reachable through a key. |
| 51 | PIG-JS.RUNTIME.MEMORY.6 | js-philosophy:RUNTIME.MEMORY.2 | refines | The heap limit and the collector are the concrete setting of the bound on long-lived state. |
| 52 | PIG-JS.DEFENSE.HOST.1 | js-philosophy:DEPENDENCIES.TRUST.2 | refines | Dependencies are fully trusted code and give no in-process isolation (SUPPLY-C01, RUNSEC-C41); the permission model is a seat belt on top. |
| 53 | PIG-JS.DEPENDENCIES.SCREEN.1 | js-philosophy:VERIFICATION | requires | Scorecard checks (tests before merge, review, branch protection) overlap CI gates. |
| 54 | PIG-JS.DEFENSE.ORIGIN.2.1 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 55 | PIG-JS.DEFENSE.ORIGIN.2.2 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 56 | PIG-JS.DEFENSE.ORIGIN.6 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 57 | PIG-JS.DEFENSE.ORIGIN.6.1 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 58 | PIG-JS.DEFENSE.ORIGIN.6.2 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 59 | PIG-JS.DEFENSE.ORIGIN.6.3 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 60 | PIG-JS.DEFENSE.DOM.2.3 | js-philosophy:DEFENSE.DOM.2 | refines | The default renders the principle in JavaScript. |
| 61 | PIG-JS.DEPENDENCIES.INSTALL.5 | js-philosophy:DEPENDENCIES.THREATS.2 | refines | The default renders the principle in JavaScript. |
| 62 | PIG-JS.DEPENDENCIES.SCREEN.3 | js-philosophy:DEPENDENCIES.THREATS.2 | refines | The default renders the principle in JavaScript. |
| 63 | PIG-JS.SUBSET.NUMBERS | js-philosophy:SUBSET.NUMBERS | refines | Binary64 precision, the safe-integer range and BigInt are the concrete numeric limits. |
| 64 | PIG-JS.SUBSET.MUTATION.1 | js-philosophy:SUBSET.STATE | refines | Object.freeze is the language mechanism whose reach (own keys only) must be known. |
| 65 | PIG-JS.CONTRACTS.BOUNDARY | js-philosophy:CONTRACTS.BOUNDARY | refines | Parsing at the boundary realises the boundary contract. |
| 66 | PIG-JS.DEFENSE.INJECTION.1 | js-philosophy:DEFENSE.CODE | refines | The default renders the principle in JavaScript. |
| 67 | PIG-JS.DEFENSE.INJECTION.1.3 | js-philosophy:DEFENSE.CODE | refines | The default renders the principle in JavaScript. |
| 68 | PIG-JS.DEFENSE.INJECTION.1.4 | js-philosophy:DEFENSE.CODE | refines | The default renders the principle in JavaScript. |

## Planned boundary links to the web-architecture graphs (planned, not created)

The target graphs `web-app-philosophy` and `pig-web-defaults` of `../web_architecture_guidelines/` do not exist yet;
target uids are chosen when they do. Each row is a claim or rule that the web-architecture guideline owns.

| # | from | to graph | content owned there |
|---|---|---|---|
| 1 | PIG-JS.DEFENSE.DOM.4 | pig-web-defaults | code half here, CSP header and policy deployment in web_architecture (DOMSEC-C15, FW-C48) |
| 2 | PIG-JS.DEFENSE.ORIGIN.4 | pig-web-defaults | token and session architecture in web_architecture (DOMSEC-C35) |
| 3 | PIG-JS.DEFENSE.ORIGIN.5 | pig-web-defaults | CSP deployment, JSONP, CORS and framework CSP and CSRF options in web_architecture (DOMSEC-C26, C28, C29, C59, C60, FW-C04, FW-C14) |
| 4 | PIG-JS.DEFENSE.INJECTION.6.1 | pig-web-defaults | cloud metadata service configuration in web_architecture (SRVSEC-C38) |
| 5 | PIG-JS.DEFENSE.HOST.3 | pig-web-defaults | front-end proxy normalization is deployment, with the Node parser side kept here (SRVSEC-C58) |
| 6 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | pig-web-defaults | rendering strategy (SPA, server HTML, hypermedia) decides which candidate fits; owned by web-architecture |
| 7 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | pig-web-defaults | FW-C44 (usage by rendering strategy, deferred) and FW-C45 (CSP and SRI prevalence) |
| 8 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | pig-web-defaults | FW-C07 and FW-C13 (framework advisories, update policy of server rendering) |
| 9 | PIG-JS.CONTROL.PROCESS.4 | pig-web-defaults | the Node side of shutdown (signal listener, server close) and the external supervisor of PROCESS.2 serve the shutdown contract that the web-architecture guideline owns |
| 10 | PIG-JS.DEFENSE.ORIGIN.2.1 | pig-web-defaults | response header deployment of frame-ancestors and the CSP policy around it in web_architecture (SECGAP2-C63, C64) |
| 11 | PIG-JS.DEFENSE.ORIGIN.6.3 | pig-web-defaults | cookie attribute design and session architecture beside SameSite in web_architecture (SECGAP2-C61) |
| 12 | PIG-JS.DEFENSE.SECRETS.2.1 | pig-web-defaults | token revocation, logout and session design in web_architecture (SECGAP2-C16) |

## Judge records

One record per defaults node holding a decision, as written by the branches (positions, forces, decision, rejected
with the condition under which each would win). Layouts differ by branch and are kept. Integration notes are marked.

### SUBSET

Format: Positions (claim ids), Forces, Decision, Rejected (with the condition under which it would win).

#### PIG-JS.SUBSET.STRICTNESS.1
- Positions: strict everywhere (LANG-C02, LANG-C01); sloppy mode left on in scripts (nobody holds it); use strict per file by hand (LANG-C02 for classic scripts).
- Forces: predictability gains loud failure (LANG-C03); cost is none in modules and classes, one directive in scripts.
- Decision: all code strict, via modules or classes, directive only in classic scripts.
- Rejected: sloppy mode in legacy scripts; would win only for code that cannot be edited.

#### PIG-JS.SUBSET.STRICTNESS.2
- Positions: ES modules (LANG-C57, STRUCT-C21); classic scripts and globals (implicit alternative).
- Forces: module scope and single evaluation remove ambient globals; cost is a build or type=module loading.
- Decision: write ES modules.
- Rejected: classic scripts with a directive; would win for a single-file page with no tooling.

#### PIG-JS.SUBSET.STRICTNESS.3
- Positions: const by default (LANG-C36); let everywhere; belief that const means constant value (LANG-C35).
- Forces: a fixed binding states intent at the declaration; cost none.
- Decision: const unless reassigned.
- Rejected: let-by-default (no ground); the belief, refuted by MDN.

#### PIG-JS.SUBSET.STRICTNESS.4
- Positions: never var (LANG-C37); var in scripts for global export.
- Forces: block scope and no silent redeclaration; the global-property side effect of var is a hazard.
- Decision: never var.
- Rejected: var for a deliberate script global; would win never (use globalThis or a module export).

#### PIG-JS.SUBSET.CONVERSION.1
- Positions: === everywhere (LANG-C17); == where the types are known (LANG-C27 measurement only).
- Forces: result follows from operands alone versus a measured fraction of redundant ==; cost none.
- Decision: === and !==; Object.is only for signed zero (acceptable-when, LANG-C20).
- Rejected: == with types known; would win never as a rule, since the types are not checked.

#### PIG-JS.SUBSET.CONVERSION.2
- Positions: forbid all == (eqeqeq always, Airbnb); allow == null only (Google JS, eqeqeq null ignore).
- Forces: both are exact in mechanism (ECMA-262 7.2.13); one uniform rule asks nothing of the reader, the exception asks the reader to know the one exception.
- Decision: forbid every ==, the null check included. Max rule: the more demanding of two grounded options.
- Rejected: == null as the one exception; would win where the code base already encodes it in lint and values brevity over uniformity (recorded as acceptable-when, SUBSET-017).

#### PIG-JS.SUBSET.CONVERSION.3
- Positions: Number.isNaN (LANG-C21); x === NaN, self-comparison.
- Forces: NaN is unequal to itself; the dedicated test is the only reading that cannot be wrong.
- Decision: Number.isNaN.
- Rejected: x === NaN, never correct (MDN, ECMA-262 7.2.14).

#### PIG-JS.SUBSET.CONVERSION.4
- Positions: forbid shorthands with the lint rule (SRC-003, Google, Airbnb); allow them (Pradel and Sen: harm rare).
- Forces: conversion visible at the site versus a measured low defect rate; the rule is readability, not defect prevention.
- Decision: explicit Boolean(), Number(), String() and no-implicit-coercion, stated as a readability convention with no defect claim. Max rule on predictability of reading.
- Rejected: allowing shorthands; wins where a team does not adopt the rule (SUBSET-022). Grounds are positions only, flagged for review.

#### PIG-JS.SUBSET.CONVERSION.5
- Positions: Number(x) as validation (rejected by LANG-C23); Number.isFinite or boundary parsing (not in this branch).
- Forces: Number() accepts null, empty and whitespace as 0.
- Decision: never use Number(x) as the validity test.
- Rejected: Number(x) with an isNaN check; would win never, as null and empty string pass as 0.

#### PIG-JS.SUBSET.CONVERSION.6
- Positions: ?? for defaults (LANG-C50); logical OR for defaults (folklore).
- Forces: falsy-but-valid values (0, empty string, false) versus brevity.
- Decision: ?? whenever any falsy value is valid; parenthesise any mix (LANG-C51).
- Rejected: logical OR default; wins only if all falsy values are invalid (SUBSET-027).

#### PIG-JS.SUBSET.NUMBERS.1
- Positions: treat fractions as rounded (LANG-C28); fixed tolerance as cure (rejected in js-philosophy by LANG-C29).
- Forces: binary64 cannot hold decimal fractions exactly; the tolerance relation is not transitive.
- Decision: treat all fraction arithmetic as approximate.
- Rejected: tolerance as general cure; wins never as a general rule.

#### PIG-JS.SUBSET.NUMBERS.2
- Positions: Number inside the safe range with isSafeInteger, larger as BigInt or string (LANG-C30).
- Forces: exactness beyond 2^53 versus type friction.
- Decision: as stated.
- Rejected: Number for large ids; wins never (silent corruption).

#### PIG-JS.SUBSET.NUMBERS.3
- Positions: BigInt only above 2^53 (LANG-C31); BigInt everywhere (folklore); mixed arithmetic (rejected by LANG-C32).
- Forces: exact arithmetic versus a separate type with no mixing.
- Decision: BigInt only where values exceed the safe range, never mixed with Number.
- Rejected: BigInt as default integer; wins never in everyday code.

#### PIG-JS.SUBSET.NUMBERS.4
- Positions: ids as strings (LANG-C33, TYPES-C49); explicit replacer and reviver.
- Forces: JSON numbers are parsed to binary64 before any reviver; stringify throws on BigInt.
- Decision: strings or an explicit codec; never plain numbers beyond the safe range.
- Rejected: plain JSON numbers for 64-bit ids; wins never.

#### PIG-JS.SUBSET.OBJECTS.1
- Positions: never rely on implicit this (LANG-C04); arrows for lexical this (LANG-C06); Google conventions (LANG-C07, C08, demoted).
- Forces: this set at call time makes detached methods fail; the Google conventions are stronger but grounded only by a position.
- Decision: never rely on an implicit global this; use arrows for lexical this in nested callbacks.
- Rejected: restricting this to class code (LANG-C08) and arrows over bind everywhere (LANG-C07) as rules; would win as a team convention (acceptable-when).

#### PIG-JS.SUBSET.OBJECTS.2
- Positions: declare before use, super() first (LANG-C09, C10).
- Forces: TDZ and field-initialisation timing make order observable.
- Decision: as stated.
- Rejected: using a class before its declaration; wins never.

#### PIG-JS.SUBSET.OBJECTS.3
- Positions: hash private fields (MDN, TC39); trailing underscore (Google JS); no underscores, they are public API (Airbnb); TypeScript private, no hash fields (Google TS).
- Forces: runtime-enforced privacy versus convention and emit-size cost on down-levelled output; the mechanism is undisputed.
- Decision: hash private fields wherever privacy must hold; an underscore never counts as privacy.
- Rejected: TypeScript private; wins on down-levelled targets where the emit cost is measured. Underscore convention; wins never as privacy.

#### PIG-JS.SUBSET.OBJECTS.5
- Positions: leave built-ins alone (STRUCT-C44, MDN); never modify built-ins and no direct prototype work (LANG-C14, Google, demoted).
- Forces: a later language addition of the same name breaks the patch (SmooshGate).
- Decision: add nothing to built-in prototypes.
- Rejected: patching; wins only for backporting an already-specified feature.

#### PIG-JS.SUBSET.OBJECTS.6
- Positions: Object.hasOwn (LANG-C55); hasOwnProperty (STRUCT-C45); for-in on arrays (rejected by LANG-C26).
- Forces: an inherited method can be shadowed or absent; for-in visits inherited keys.
- Decision: Object.hasOwn; arrays iterated by element, not for-in.
- Rejected: hasOwnProperty; wins on targets without Object.hasOwn.

#### PIG-JS.SUBSET.MUTATION.1
- Positions: freeze is shallow (LANG-C38, C39); freeze as deep immutability (folklore).
- Forces: SetIntegrityLevel touches own keys only; strict-only throwing.
- Decision: rely on freeze for one level and in strict code; deep immutability by recursive freeze on acyclic graphs or an immutable design.
- Rejected: freeze as deep guarantee; wins never.

#### PIG-JS.SUBSET.MUTATION.2
- Positions: structuredClone (LANG-C44); JSON round trip.
- Forces: cycles, typed arrays, prototypes versus JSON-safe simplicity.
- Decision: structuredClone for cloneable data.
- Rejected: JSON round trip; wins for JSON-safe data only (SUBSET-058).

#### PIG-JS.SUBSET.MUTATION.3
- Positions: toSorted (LANG-C40); sort with a comparator (LANG-C41); default sort.
- Forces: sort mutates in place; default order is by string.
- Decision: toSorted when the original must stay; always a comparator for numbers.
- Rejected: default sort of numbers; wins never.

#### PIG-JS.SUBSET.OBJECTS.4
- Positions: no accessor properties, use methods (STRUCT-C46, Google JS, position only); accessors allowed (implicit, no holder).
- Forces: a property read that runs code hides cost and side effects from the reader, which is the predictability purpose; cost is a call-style API.
- Decision: no getter or setter properties; behaviour is a method.
- Rejected: accessors; would win for a cheap, side-effect-free view of stored state on a data-like object (SUBSET-069, inferred). Grounds are one position, flagged for review.

#### PIG-JS.SUBSET.EVOLUTION.1
- Positions: stage 4 only (LANG-C54, inferred); earlier stages with a transpiler (no admitted source).
- Forces: earlier stages can change or be dropped.
- Decision: stage 4 only.
- Rejected: stage 3 with transpiler; would win only with a source that states the maturity and target guarantees (none admitted).

#### PIG-JS.SUBSET.EVOLUTION.2
- Positions: check support, polyfill (LANG-C43); adopt Temporal now; keep Date (no source states a rule).
- Forces: availability is a runtime fact, dated.
- Decision: adopt only after verifying every target or covering it by a polyfill.
- Rejected: adopting unchecked; wins never.

#### PIG-JS.SUBSET.EVOLUTION.3
- Positions: no legacy octal, no with (LANG-C24, C46).
- Forces: strict-mode errors versus legacy code.
- Decision: neither is written.
- Rejected: legacy syntax in old files; wins never in new code.

#### PIG-JS.SUBSET.EVOLUTION.4
- Positions: replace deprecated features (LANG-C47); no Annex B in new code (LANG-C48).
- Forces: Annex B is normative only for browsers and optional elsewhere.
- Decision: replace and avoid.
- Rejected: relying on Annex B; wins never for portable code.

#### PIG-JS.SUBSET.EVOLUTION.5
- Positions: explicit semicolons and braces, no reliance on automatic insertion (QUALITY-C19, Google JS, position only); reliance on insertion with a formatter and lint (no holder in the claim base).
- Forces: explicit termination makes statement boundaries independent of the next token and of line breaks, the predictability purpose; cost is typing, which a formatter removes.
- Decision: semicolon on every statement, braces on every control structure.
- Rejected: reliance on automatic insertion; would win where a formatter and hazard-catching lint rules both run in CI and the team adopts that style (SUBSET-070). No admitted source documents the hazards (not extracted, G-M02): grounds are one position, flagged for review.

Integration note (SUBSET): the claim RUNSEC-C07 sits in the merged row SUBSET-051 on PIG-JS.SUBSET.OBJECTS.6 (own-property reads, one rule for all keys); the node PIG-JS.DEFENSE.PROTOTYPE.1 links to it.

### CONTRACTS

Each record: Positions, Forces, Decision, Rejected (position, reason, condition under which it wins).

**PIG-JS.CONTRACTS.LAYER.1.** Positions: TypeScript (Google JS guide, frozen, recommends migrating, SRC-239; Google TS guide, SRC-244; TYPES-C01); JSDoc-checked JavaScript (no advocate; documented by SRC-047, SRC-044; weaker checks TYPES-C40; JSDoc forms removed in 7.0, TYPES-C42); none (no holder; only SRC-240 measuring 15 percent detection). Forces: checkability is served most by the position whose checker sees the most (full type syntax, unions, strict family); its cost is a compile or type-check step, which Node type stripping lowers (TYPES-C03, C04). Decision: TypeScript with strict. Condition table: TypeScript wins when a build or type-check step can be adopted (compilation, or Node type stripping); JSDoc-checked JavaScript wins when none can (LAYER.2); no type layer wins under no admitted condition; native type syntax is not planned on (Stage 1, no run-time enforcement). The choice among them is the build's judgment (the claim reads: decision for the maintainer), flagged. Rejected: JSDoc-checked JavaScript, because checking is weaker (open objects, optional parameters, any initialisers) and 7.0 drops forms; it wins where no build or type-check step can be adopted (LAYER.2). None, because no admitted holder argues for it and SRC-240 measures benefit; it wins on no admitted evidence. Native type syntax, because it is Stage 1 with no run-time enforcement.

**PIG-JS.CONTRACTS.LAYER.2.** Positions: checkJs project-wide; ts-check per file (TYPES-C39). Forces: project-wide checking leaves no unchecked file; per-file allows gradual adoption. Decision: checkJs for the project, with the 7.0-safe tag set. Rejected: per-file ts-check wins during an incremental migration of an existing code base (inferred condition).

**PIG-JS.CONTRACTS.LAYER.3.** Positions: run and check as one step (belief that Node checks, refuted); separate no-emit check. Forces: execution speed against a gate that actually fails on type errors. Decision: separate no-emit check wherever types are stripped. Rejected: relying on the runner, refuted by SRC-038; it never wins.

**PIG-JS.CONTRACTS.LAYER.4.** Positions: erasable syntax only under stripping (consensus); use enum and namespaces with a build step. Forces: stripping needs no build; enum and namespaces need code generation. Decision: erasable syntax only, enforced by erasableSyntaxOnly, whenever Node strips types. Rejected: generating-syntax features win when a compile step exists and the team accepts it (inferred); whether the rule extends to every TypeScript project is not grounded (open, see decisions).

**PIG-JS.CONTRACTS.LAYER.5.** Positions: the Node-documented option set only. Forces: options steer only the checker. Decision: use the documented set with TypeScript 5.8 or newer. Rejected: none stated by an admitted source.

**PIG-JS.CONTRACTS.LAYER.6.** Positions: isolatedModules on; off. Forces: single-file transpilers cannot see other files. Decision: on wherever a single-file transpiler is used. Rejected: off wins where tsc alone emits all files (inferred).

**PIG-JS.CONTRACTS.STRICT.1.** Positions: strict on (default since 6.0); selected flags only. Forces: the family gives guarantees at an adoption cost on untyped code. Decision: strict on, no member turned off. Rejected: selected flags win while migrating an existing code base (inferred); typescript-eslint's own "strict" lint config is a project position conditioned on proficiency, not a compiler choice (SRC-054, not evidence).

**PIG-JS.CONTRACTS.STRICT.2.** Positions: enable; leave off because the friction is often unwieldy (typescript-eslint, SRC-026). Forces: undefined-on-read catches missing keys; friction cost on index-heavy code. Decision: enable for new code. Rejected: off wins where index-heavy legacy code makes the friction exceed the defects found (inferred condition; the friction statement is typescript-eslint's).

**PIG-JS.CONTRACTS.STRICT.3.** Positions: enable; leave off. Forces: exact optionals remove the absent-versus-undefined ambiguity; they break libraries typed the old way (not read in a source, not stated). Decision: enable for new code. Rejected: off wins where typings from dependencies assign undefined to optional properties (inferred).

**PIG-JS.CONTRACTS.STRICT.4.** Positions: pin and upgrade deliberately; float. Forces: new checks surface as errors on upgrade. Decision: pin. Rejected: floating wins never for application code (inferred); libraries publishing types are a case for DEPENDENCIES.

**PIG-JS.CONTRACTS.ESCAPE.1 to .4.** Positions: any as the default for unknown values; unknown (TYPES-C15, consensus, folklore confirmed); lint ban of any (TYPES-C16); leak detection (TYPES-C17); Function type (avoid, TYPES-C24). Forces: any disables checks; unknown forces narrowing at the cost of ceremony. Decision: unknown for unknown shape; no-explicit-any and no-unsafe-assignment enabled; no Function type. Rejected: any wins nowhere in admitted sources, except as a documented lint suppression in a test mock (QUALITY-C18).

**PIG-JS.CONTRACTS.ESCAPE.5.** Positions: assertions freely; assertions only with an obvious reason and a run-time check preferred (TYPES-C19). Forces: assertions silence the checker without inserting checks. Decision: reason required, run-time check preferred. Rejected: free use, because it voids the contract.

**PIG-JS.CONTRACTS.ESCAPE.6.** Positions: ban all three directives (Google TS guide); allow with a reason (no admitted holder; the handbook documents the directives). Forces: a ban forces the real fix; a directive is the only exit for a third-party typing bug (inferred). Decision: ban, lint suppressions with documented reason. Rejected: allowing with a reason wins for a third-party typing bug that cannot be fixed locally (inferred condition). Scoping: the register restriction on SRC-244 is per slot; it is unrestricted for the quality slot, so QUALITY-C18 may ground the rule, and TYPES-C25 (types slot, position only) is kept as a fact row. Weakness: one T2 holder.

**PIG-JS.CONTRACTS.MODEL.1 to .3.** Positions: boolean flags and string tags without exhaustiveness; discriminated unions closed with never (TYPES-C21); truthiness narrowing (rejected by TYPES-C22); optional chaining everywhere (rejected by LANG-C53). Forces: compile-time exhaustiveness against ceremony. Decision: unions with never; explicit tests; optional chaining only on nullable types. Rejected: truthiness narrowing wins where every falsy value is invalid data (condition from LANG-C50 logic, inferred); defensive optional chaining wins on untyped boundary data, which is BOUNDARY's job instead.

**PIG-JS.CONTRACTS.SIGNATURE.1.** Positions: positional lists; options object (TAG position, ESLint rationale; inferred for application code). Forces: names against order memorisation. Decision: options object when several arguments are optional or same-typed primitives. Rejected: positional wins for one to three required, distinct-typed arguments (the rule default of 3 is a configuration default, not evidence; condition inferred).

**PIG-JS.CONTRACTS.SIGNATURE.2 to .4.** Positions: overloads; optional parameters, unions, void callbacks (handbook, declared APIs). Forces: overloads let wrongly typed functions pass compatibility. Decision: handbook rules for declared APIs. Rejected: overloads win where return type depends on the argument type (not stated by the handbook page read; open).

**PIG-JS.CONTRACTS.BOUNDARY.1.** Positions: JSON.parse result typed by assertion; unknown then validated (TYPES-C18, three T1 grounds). Forces: assertion silences the checker. Decision: unknown, validated. Rejected: assertion, never wins for untrusted data.

**PIG-JS.CONTRACTS.BOUNDARY.2.** Positions: schema rejects unneeded properties (OWASP, MDN); manual field checks. Forces: allowlist of keys and types against code volume. Decision: schema with additionalProperties false, nested objects explicit. Rejected: manual checks win for a single flat field (inferred).

**PIG-JS.CONTRACTS.BOUNDARY.3.** Positions: bind to domain model with a blocklist; dedicated object with allowlisted fields (OWASP). Forces: blocklists miss fields added later. Decision: dedicated allowlisted object. Rejected: blocklist, which OWASP says is fragile; wins never.

**PIG-JS.CONTRACTS.BOUNDARY.4.** Positions: validate in application code before Node APIs (Node threat model, OWASP Node cheat sheet). Forces: Node trusts what application code gives it. Decision: allowlist validation before the call. Rejected: relying on the API to reject, refuted by the threat model.

**PIG-JS.CONTRACTS.MODEL.4.** Positions: trust a predicate as written (the handbook documents narrowing through predicates, SRC-046); treat it as an assertion whose body must check at run time (TYPES-C19, C23: assertions silence the compiler without inserting checks; compiling is not proof). Forces: a predicate that lies makes every later use unsound at no visible cost; a real check costs a few lines. Decision: assertion standard, built-in narrowing or schema parse preferred. Rejected: trusting predicates as written wins for a one-line test of a discriminant already validated at the boundary (inferred). Searched: handbook narrowing page and typescript-eslint pages for a statement on predicate verification; none found (TYPES-C20), so the decision is inference from the two grounds above.

**PIG-JS.CONTRACTS.MODEL.5.** Positions: interface for object types (Google TS guide, SRC-244, position; handbook fact: interfaces extend and re-open, aliases do not, SRC-043); type alias (no admitted holder). Forces: extension and re-opening keep one named shape across declarations, at the cost of accidental declaration merging (inferred). Decision: interface for object types; alias for unions, tuples, mapped and other forms an interface cannot express (inferred). Rejected: alias everywhere wins where accidental merging must be impossible (inferred). The restriction (position only) is respected: the position is used to choose among positions, not as evidence of a defect class.

**PIG-JS.CONTRACTS.BOUNDARY.5.** Positions: JSON Schema with Ajv (schemas as trusted code, SRC-031); Zod (parse, safeParse, infer, TypeScript 5.5 or newer with strict, SRC-051); Valibot (inferred output type, SRC-050); a Standard Schema compliant library for tool interoperability (SRC-041). Forces: checkability is highest where one schema yields both the run-time check and the static type; vendor documentation gives facts and never a ranking. Decision: a schema library that infers the static type, compliant with Standard Schema V1 where tools must accept it, schemas never compiled from untrusted input. Rejected: JSON Schema with Ajv wins where the schema is a language-neutral contract shared with non-TypeScript code (inferred); a specific library is not named because no admitted source ranks them (open, not a reason to abstain on the class).

### CONTROL

One per defaults node holding a decision. Each lists positions (claim ids, source ids), forces,
the decision and the rejected positions with the condition under which each would win. "No
admitted source names a condition" means exactly that, not that none exists.

#### PIG-JS.CONTROL.PROMISES.1 Chaining without loss
- Positions: return or await the inner promise (ASYNC-C01; SRC-075, SRC-245, SRC-072); return the promise p.then produced (ASYNC-C14; SRC-245); flat chains (ASYNC-C15; SRC-075) against nesting; leave the inner promise unreturned (folklore).
- Forces: predictability of order at no cost; flatness serves readability and catch scope.
- Decision: always return or await; return the then result; keep chains flat and nest only to confine a catch.
- Rejected: unreturned inner promise, refuted (SRC-075, SRC-072), never wins; returning p, loses the continuation, never wins; nesting by default, wins when a catch must cover only the inner scope (SRC-075).

#### PIG-JS.CONTROL.PROMISES.2 Constructing promises
- Positions: async executor in new Promise (ASYNC-C11; SRC-059); wrapping an existing promise or hand-written promisification (ASYNC-C12; SRC-245, SRC-246); promise that may never settle or settle twice (ASYNC-C13; SRC-245).
- Forces: rejections must not be lost; one settlement per promise.
- Decision: no async executor; return the existing promise and use util.promisify; settle exactly once on every path.
- Rejected: async executor, drops the thrown error, no admitted source names a condition; wrapper pattern, drops inner rejections, no condition named; hand-written promisification, no condition named.

#### PIG-JS.CONTROL.PROMISES.3 Every promise observed
- Positions: floating promise (ASYNC-C02; SRC-072, SRC-082, SRC-077); void as handling (ASYNC-C03; SRC-072); async function as void callback (ASYNC-C16; SRC-073, SRC-081); promise as condition (ASYNC-C17; SRC-073).
- Forces: explicit failure against convenience; each rule closes one way a rejection is lost.
- Decision: await, return or handle every promise; void is not handling; catch inside handlers; await before testing.
- Rejected: floating promises, void-as-handling, async handlers and promise conditions, each no condition named by an admitted source. The rule documents are positions of the rule's holder, not a preference for that tool.

#### PIG-JS.CONTROL.PROMISES.4 Combining and ordering async work
- Positions: sequential awaiting of started promises (ASYNC-C08; SRC-056); Promise.all against allSettled (ASYNC-C09; SRC-075, SRC-056, SRC-028); concurrent against sequential (ASYNC-C10; SRC-056, SRC-246, SRC-075); unguarded read-modify-write across await (ASYNC-C54; SRC-060).
- Forces: early rejection reporting and speed against ordering needs.
- Decision: combine started promises first; allSettled when every operation must finish; concurrent by default; guard shared state across suspension.
- Rejected: sequential awaiting wins when a later operation depends on an earlier result (ASYNC-C10); Promise.all wins when failing fast is wanted and the remaining outcomes are not needed (inferred from SRC-075); unguarded state, no condition named.

#### PIG-JS.CONTROL.PROMISES.5 Async functions without waste
- Positions: remove promises that do no work (ASYNC-C53; SRC-246).
- Forces: fewer allocations and simpler flow against a refactor cost the paper samples (65 of 80 sampled instances refactorable).
- Decision: avoid async functions without await, awaits on returned values and Promise.resolve().then(f). A return await inside try/catch is not evaluated by the source (open): the rule does not cover it.
- Rejected: keeping flagged promises, no condition named.

#### PIG-JS.CONTROL.PROMISES.6 Async functions over then chains
- Positions: async functions and await over hand-written promise code (ASYNC-C52; SRC-249, V8 team, 2018, dated position); flat then chains, nested only to confine a catch (ASYNC-C15; SRC-075, MDN editorial position); async functions turn every uncaught exception into a rejection (ASYNC-C07; SRC-056, SRC-245, SRC-075); await is slower than chains (folklore).
- Forces: explicit failure: one syntax in which a thrown error and a rejection both leave through the function's promise and try/catch (inferred from ASYNC-C07) against the new traps of await (ASYNC-C08, C10, C54, handled by PROMISES.4); speed, no admitted current measurement.
- Decision: async functions and await by default; chains are acceptable when kept flat (inferred from ASYNC-C15). Maximum demanded here is the only direction any admitted position takes.
- Rejected: hand-written chains as the default, wins when a flat chain is the whole function body or nesting must confine a catch (MDN position, inferred); the slower-await belief, refuted for 2018 only (SRC-249, history), a present-day gap would win only if an admitted current measurement showed one (open).

#### PIG-JS.CONTROL.ERRORS.1 Error values
- Positions: throw only Error instances (ASYNC-C18, LANG-C45; SRC-074, SRC-239); throw any value; identify errors by code (ASYNC-C24; SRC-065) against by message.
- Forces: Error records origin; code is stable, message is not.
- Decision: Error instances only; match on error.code.
- Rejected: strings and plain objects, no admitted source names a condition; matching on error.message, unstable across versions.

#### PIG-JS.CONTROL.ERRORS.2 Catching
- Positions: caught value unknown and narrowed (TYPES-C12; SRC-052); callback throws routed through a channel (ASYNC-C22; SRC-065); empty catch with a reason (ASYNC-C21; SRC-239, position only).
- Forces: a thrown value need not be an Error; try/catch cannot see asynchronous callbacks.
- Decision: unknown plus narrowing; route callback failures through rejection, error-first argument or emitter event. A catch that does nothing is forbidden unless a comment states why taking no action is right.
- Rejected: any-typed catch variable, no condition named; empty catch without a reason, no condition named.

#### PIG-JS.CONTROL.ERRORS.3 Rethrowing with a cause
- Positions: wrap and pass cause (ASYNC-C19; SRC-058, SRC-070, SRC-065); cause for one site, aggregate for several (ASYNC-C20; SRC-058).
- Forces: keeping origin against message clarity.
- Decision: wrap with a specific message and pass the original as cause; one site per cause.
- Rejected: dropping the original, no condition named; assuming cause is an Error, wrong by spec; cause for several failures, use an aggregate.

#### PIG-JS.CONTROL.ERRORS.4 Emitter failures
- Positions: listener on every emitter (ASYNC-C23, RUNTIME-C31; SRC-081, SRC-065, SRC-078); captureRejections (RUNTIME-C32; SRC-081); sequential events.once (RUNTIME-C33; SRC-081).
- Forces: an emitted error without a listener ends the process (also a denial-of-service lever).
- Decision: always attach the listener; enable captureRejections; await same-turn events together.
- Rejected: no listener, no condition named; sequential events.once for same-turn events, loses events.

#### PIG-JS.CONTROL.BOUNDS.1 Abort signals
- Positions: signal option rejecting with reason (ASYNC-C26, STRUCT-C53; SRC-057, SRC-055, SRC-066, SRC-261); throwIfAborted first (ASYNC-C27; SRC-055, SRC-066); one controller per operation (ASYNC-C29; SRC-055, SRC-066); signal to pipeline (RUNTIME-C06; SRC-196).
- Forces: a single platform primitive for cancellation against ad hoc tokens.
- Decision: AbortSignal everywhere cancellation is offered, with the four rules.
- Rejected: reusing one aborted controller, the signal is one-shot; assuming promises cancel (see CONTROL.BOUNDS).

#### PIG-JS.CONTROL.BOUNDS.2 Timeouts
- Positions: AbortSignal.timeout and any (ASYNC-C28; SRC-055, SRC-066, SRC-057); timers/promises with signal, unref (ASYNC-C34; SRC-067); server timeouts (ASYNC-C55, RUNTIME-C42; SRC-078, SRC-190).
- Forces: bounded waits against slow-client exhaustion; TimeoutError separates timeout from user abort.
- Decision: bound every awaited operation; configure server timeouts and never disable requestTimeout on an exposed server.
- Rejected: unbounded waits; disabling requestTimeout, no admitted source names a condition; the combined AbortSignal.any cannot name the first cause in MDN but Node sets the causing reason, so the two sources agree.

#### PIG-JS.CONTROL.BOUNDS.3 Abort listener hygiene
- Positions: remove listeners at the end (ASYNC-C30; SRC-055); events.addAbortListener in Node (RUNTIME-C34; SRC-081).
- Forces: leak avoidance against defeat by stopImmediatePropagation.
- Decision: remove at the end; use events.addAbortListener in Node.
- Rejected: signal.addEventListener for abort in Node, defeatable; no condition named.

#### PIG-JS.CONTROL.SCHEDULING.1 Ordering and timer precision
- Positions: setImmediate over nextTick (ASYNC-C36; SRC-071); no order dependence between setTimeout(0) and setImmediate (ASYNC-C37; SRC-071, SRC-067); clamps (ASYNC-C32; SRC-062, SRC-067).
- Forces: starvation of I/O against ease of reasoning.
- Decision: defer with setImmediate; never depend on timer-versus-immediate order outside I/O; know the clamps.
- Rejected: nextTick as general deferral, refuted (SRC-071), no condition named; zero-delay timers as immediate, refuted (SRC-062, SRC-067).

#### PIG-JS.CONTROL.SCHEDULING.2 Event-loop blocking
- Positions: bound callback cost (ASYNC-C39; SRC-080); synchronous core APIs block (ASYNC-C41; SRC-080, inferred); partition (ASYNC-C42; SRC-080); worker offload (see SCHEDULING.3).
- Forces: fairness among clients against implementation effort.
- Decision: bounded cost; keep synchronous blockers off server loops; partition only where work cannot move to a worker (inferred condition).
- Rejected: unbounded callback cost, no condition named; partitioning as the default, wins when a worker is not available (inferred).

#### PIG-JS.CONTROL.SCHEDULING.3 Workers
- Positions: workers for CPU only (ASYNC-C43; SRC-069, SRC-076); few workers (ASYNC-C44; SRC-063); clone or transfer (ASYNC-C45; SRC-069, SRC-076, SRC-063); handle error and exit (ASYNC-C46; SRC-069, SRC-063, SRC-076); resourceLimits (ASYNC-C47; SRC-069).
- Forces: CPU parallelism against startup and memory cost.
- Decision: CPU work only, sparingly, explicit transfer, both failure events handled, limits where untrusted input drives work.
- Rejected: workers for I/O, built-in async I/O is more efficient; many workers, heavy-weight (HTML Standard); no condition named for either.

#### PIG-JS.CONTROL.SCHEDULING.4 Async context
- Positions: AsyncLocalStorage, run over enterWith (ASYNC-C48; SRC-064); AsyncContext (ASYNC-C49; SRC-248, fact only).
- Forces: scoped state against leakage into later handlers.
- Decision: AsyncLocalStorage with run().
- Rejected: hand-built async_hooks layer, no condition named; enterWith, wins under strong reasons (SRC-064); AsyncContext, not in the language.

#### PIG-JS.CONTROL.FLOW.1 Backpressure
- Positions: stop on write false (RUNTIME-C01; SRC-196, SRC-184); no push when not asked (RUNTIME-C02; SRC-184); no bare data listener (RUNTIME-C03; SRC-184).
- Forces: memory bound against code simplicity.
- Decision: obey the return values and use pipe or pipeline.
- Rejected: write loops ignoring the return value; bare data listeners; no condition named.

#### PIG-JS.CONTROL.FLOW.2 Pipelines and iteration
- Positions: pipeline over pipe (RUNTIME-C05; SRC-196); finished with cleanup (RUNTIME-C08; SRC-196); early exit semantics (RUNTIME-C07; SRC-196, SRC-197, SRC-204).
- Forces: resource closure on error against the older, shorter pipe call.
- Decision: pipeline; cleanup: true when listeners must not dangle.
- Rejected: pipe(), leaks the destination on source error; no condition named.

#### PIG-JS.CONTROL.FLOW.3 Web Streams
- Positions: default pipeTo propagation (RUNTIME-C09; SRC-197); tee shares chunks (RUNTIME-C10; SRC-197); Node stability (RUNTIME-C11; SRC-204).
- Forces: interference between branches against copy cost (not measured).
- Decision: do not mutate chunks seen through tee.
- Rejected: mutation of shared chunks, no condition named (byte streams copy, per SRC-197).

#### PIG-JS.CONTROL.PROCESS.1 Unhandled rejections
- Positions: default throw (ASYNC-C04, RUNTIME-C40; SRC-082, SRC-068, SRC-079); browser event (ASYNC-C06; SRC-077, SRC-075); warn-only belief.
- Forces: visible failure against tolerance.
- Decision: rely on the throw default in Node; report through unhandledrejection in browsers.
- Rejected: warn-only, true only before Node 15 (SRC-068, history); the non-default modes (SRC-079) have no condition named by an admitted source.

#### PIG-JS.CONTROL.PROCESS.2 Uncaught exceptions
- Positions: sync cleanup then exit, supervisor restarts (RUNTIME-C37; SRC-082); monitor only logs (RUNTIME-C38; SRC-082); resume (rejected).
- Forces: undefined state against availability.
- Decision: exit after synchronous cleanup, restart from outside; log with the monitor.
- Rejected: resuming after uncaughtException, Node docs: not safe; no condition named.

#### PIG-JS.CONTROL.PROCESS.3 Exit
- Positions: exitCode over exit() (RUNTIME-C35; SRC-082); synchronous exit listeners (RUNTIME-C36; SRC-082).
- Forces: output completeness against immediacy.
- Decision: set exitCode and drain; synchronous exit listeners only.
- Rejected: process.exit() with pending writes; beforeExit as cleanup; no condition named.

#### PIG-JS.CONTROL.PROCESS.4 Shutdown
- Positions: listener must end the process (RUNTIME-C39; SRC-082); close then closeAllConnections last (RUNTIME-C41; SRC-190).
- Forces: graceful drain against bounded shutdown time.
- Decision: finish cleanup and end; close first, force last.
- Rejected: closeAllConnections first, race with new connections; a listener that cleans but never ends; no condition named.

#### PIG-JS.CONTROL.PROCESS.5 Owned handles
- Positions: close FileHandle in finally (RUNTIME-C17; SRC-188); clientError closes socket (RUNTIME-C43; SRC-190).
- Forces: deterministic release against reliance on collection.
- Decision: close on every path; a clientError listener closes or destroys the socket.
- Rejected: relying on garbage collection, emits a warning; no condition named.

Integration note (CONTROL): the claims ASYNC-C05 and RUNTIME-C37 sit in one merged row, CONTROL-078, on PIG-JS.CONTROL.PROCESS.2; the principle is held by CONTROL.LIFECYCLE.

### STRUCTURE

Each record: positions (claims, sources), forces, decision, rejected with the condition under which it
would win. A node with a single position states the alternative as the absence of the practice.

| node | positions | forces | decision | rejected (condition under which it wins) |
|---|---|---|---|---|
| PIG-JS.STRUCTURE.FORMAT.1 | Explicit marker (LANG-C59, STRUCT-C14; SRC-030) against syntax detection for unmarked .js (SRC-030 describes it) | Explicit serves locality because a file's meaning does not change with its content or a Node upgrade; detection saves one line of config | Explicit extension or type field | Syntax detection: wins for throwaway scripts that are never imported |
| PIG-JS.STRUCTURE.FORMAT.2 | Module scripts (LANG-C58; SRC-029) against classic scripts | Modules scope their names; classic scripts share one global scope | Module scripts | Classic scripts: win only where the code must run from file:// or in an engine without module support |
| PIG-JS.STRUCTURE.FORMAT.3 | Checker configured for the host (STRUCT-C37; SRC-094) against a default or unaligned setting | A mismatch makes the checker approve imports the host cannot resolve | Match the checker to the host | Default setting: wins when the host is a single known one the default already models |
| PIG-JS.STRUCTURE.FORMAT.4 | Module-only sharing (STRUCT-C27; SRC-244, Google TS position) against TypeScript namespaces | Namespaces add a second organising mechanism beside modules | Modules only | Namespaces: win for declaration files describing a global-script library, where no module exists (inferred, not stated by the source) |
| PIG-JS.STRUCTURE.NODE.1 | Full specifiers (STRUCT-C11, LANG-C60, TYPES-C06; SRC-030, SRC-038; Google JS position) against extensionless specifiers | Node ESM resolution does not search extensions, so extensionless specifiers fail | Always write extension and directory index | Extensionless: wins only inside a bundler that resolves it, at the price of leaving the Node-runnable subset |
| PIG-JS.STRUCTURE.NODE.2 | Module equivalents (STRUCT-C13, LANG-C62; SRC-030, SRC-028) against CommonJS globals | The globals do not exist in ES modules; JSON import needs the attribute | Module equivalents and the json attribute | CommonJS globals: win inside a file that is still CommonJS |
| PIG-JS.STRUCTURE.NODE.3 | require() of ESM without top-level await, import() otherwise (LANG-C61, STRUCT-C16; SRC-030, SRC-089) against the belief that CommonJS cannot load ESM | The belief forces dynamic import everywhere; the mechanism allows synchronous require for graphs without top-level await | Allow require only for graphs without top-level await, else dynamic import | Always dynamic import: wins when the graph may gain top-level await later, since ERR_REQUIRE_ASYNC_MODULE appears at run time |
| PIG-JS.STRUCTURE.NODE.4 | Default import of CommonJS (STRUCT-C15; SRC-030) against reliance on named imports | Named export detection is static analysis that does not always succeed | Default import for unusual export patterns | Named imports: win for patterns the Node docs list as detected |
| PIG-JS.STRUCTURE.NODE.5 | Assign module.exports (STRUCT-C17; SRC-089) against assigning exports | exports is a local alias that detaches on assignment | Assign module.exports | Property assignment to exports: wins when only adding properties |
| PIG-JS.STRUCTURE.LOADING.1 | No order reliance, run-once top level (STRUCT-C04, STRUCT-C05; SRC-087, SRC-029, SRC-089, SRC-256) against sequencing work by import order | Hoisting runs imported effects first; run-once means a second import repeats nothing | Never sequence by import order; export a function for repeatable work | Import-order sequencing: wins nowhere in ES modules (the mechanism contradicts it) |
| PIG-JS.STRUCTURE.LOADING.2 | Bare import named as side-effect module (STRUCT-C07; SRC-087) against bare imports of modules that also export | A bare import discards exports, so using it on a module with exports hides the dependency | Reserve bare imports for side effects | Bare import of exporting modules: wins nowhere |
| PIG-JS.STRUCTURE.LOADING.3 | Dynamic import for conditional loading (STRUCT-C20; SRC-087, SRC-256) against static imports plus conditional use | Static imports are unconditional, so the cost is paid even when unused | Dynamic import for conditional or deferred load | Static import: wins whenever the module is always needed, for static analysis |
| PIG-JS.STRUCTURE.LOADING.4 | Entry-point-only top-level await (STRUCT-C19, STRUCT-C18, LANG-C63; SRC-092, SRC-030, SRC-029) against top-level await anywhere (champions Borins and Startsev) | An await in a shared module makes every importer asynchronous, so a leaf change spreads upward; entry points have no importers | Entry points only | Anywhere: wins if a measurement shows the coordination hazard is negligible, or in scripts that nothing imports |
| PIG-JS.STRUCTURE.LOADING.6 | Avoid internal barrels (STRUCT-C29; SRC-315 T3 measurement, SRC-086) against barrels as a convenience (MDN documents aggregation, no recommendation) and the blanket removal position | A barrel couples each importer to every re-exported module; a public entry point is the one place aggregation earns its cost | Import from the defining module, aggregate at the public entry point only | Barrels everywhere: win where no measurement shows load cost and importers need many members; blanket removal wins if the public entry point is itself the problem |
| PIG-JS.STRUCTURE.SURFACE.1 | Named only (STRUCT-C24; SRC-239, SRC-244) against default for single-export modules (SRC-312) and MDN's neutral interop note (SRC-029) | A default export has no canonical name, so renames cannot be found mechanically | Named exports only | Default: wins when a framework or tool mandates a default export, or for CommonJS and AMD interop (the purpose MDN names) |
| PIG-JS.STRUCTURE.SURFACE.2 | Export only what is used (STRUCT-C25; SRC-244) against exporting everything for convenience | Each extra export is a name that others may start to depend on | Minimal export list | Export-all: wins in a package that is explicitly a toolbox whose members are its purpose |
| PIG-JS.STRUCTURE.SURFACE.3 | No mutation of exported state and no mutable exports (STRUCT-C01, STRUCT-C03; SRC-087, SRC-239, SRC-244, SRC-312) against exported mutable bindings with live updates | Live bindings let an exporter change what importers see, so state has hidden writers | No mutable exports; initialise once, change only through functions | Mutable live export: wins for a deliberate observable value owned by the exporter, if documented |
| PIG-JS.STRUCTURE.SURFACE.4 | No wildcard merge with possible collisions (STRUCT-C22, STRUCT-C23; SRC-086) against export * convenience | A collision silently drops the name; duplicates are a SyntaxError | Do not use export * where names may collide | export *: wins when the sources are known disjoint |
| PIG-JS.STRUCTURE.SURFACE.5 | Module as namespace (LANG-C15, STRUCT-C26; SRC-239, SRC-244) against static-method groupings (STRUCT-C54; SRC-261) | A module already namespaces and lets importers pick single functions | Export functions individually | Static-method groupings: win when designing a platform-style API where the host offers no module namespace (W3C TAG's setting, transfer inferred) |
| PIG-JS.STRUCTURE.DIRECTION.1 | No cycles (STRUCT-C09, LANG-C64; SRC-029, SRC-239, SRC-313) against tolerating cycles (SRC-089 documents partial exports as supported) | A cycle makes correctness depend on evaluation order; tolerance costs nothing until a binding is used early | No import cycles | Tolerate: wins where a cycle is deliberate in CommonJS legacy code and no fault is observed, or where the detection cost exceeds the benefit |
| PIG-JS.STRUCTURE.DIRECTION.2 | Enable the cycle lint rule with maxDepth (STRUCT-C10; SRC-313) against no automated check | Automation keeps the rule true; the rule is computationally expensive | Enable knowingly, bound with maxDepth | No check: wins in a small codebase with no cycle issue, as the rule's own documentation says |
| PIG-JS.STRUCTURE.PACKAGE.1 | Declare exports (STRUCT-C33, STRUCT-C34; SRC-090) against leaving every file reachable | Encapsulation lets internals change without breaking consumers | Declare the exports field | Leave open: wins for an existing package whose consumers deep-import, until a breaking release is acceptable |
| PIG-JS.STRUCTURE.PACKAGE.2 | Specific-to-general order, default last (STRUCT-C35; SRC-090) against any order | Earlier entries win, so a general key placed first shadows a specific one | Specific first, default last | Any order: wins nowhere |
| PIG-JS.STRUCTURE.PACKAGE.3 | imports field for internal aliases (STRUCT-C36; SRC-090) against path aliases configured only in a bundler or checker | The field is resolved natively and cannot collide with external names | Use the imports field | Tool-level path aliases: win only for code that never runs un-bundled and is checked by a tool that cannot read the field (inferred) |
| PIG-JS.STRUCTURE.PACKAGE.4 | Relative paths within a project (STRUCT-C28; SRC-244 position) against absolute or alias paths | Relative paths survive moving the project | Relative within a project | Aliases: win for deep trees where relative paths climb many levels, via the imports field (PACKAGE.3) |

### DEFENSE

One per defaults node holding a decision. Fields: positions, forces, decision, rejected with the condition under which each would win.

**PIG-JS.DEFENSE.INJECTION** Injection classes
- Positions: Document dangerous functionality and encode logs (ASVS 15.1.5, 16.4.1). Claims RUNSEC-C45, SRVSEC-C46, SRVSEC-C61.
- Forces: Review visibility against documentation effort.
- Decision: Document where deserialization, dynamic code, raw parsing and memory manipulation are used; encode data in every logging component.
- Rejected: No documentation of dangerous functionality: loses under ASVS Level 3 verification.

**PIG-JS.DEFENSE.DOM.1** Markup and attribute sinks
- Positions: Text-only insertion (OWASP, MDN, ASVS) against sanitizer-everywhere; setAttribute as safe construction (OWASP DOM XSS sheet) against setAttribute as a TrustedScript sink (MDN). Claims DOMSEC-C01, C02, C04, C05, C25.
- Forces: Safety against convenience of building markup from strings; encoding is context specific and unreliable in script and handler contexts.
- Decision: Insert text with textContent or built nodes, keep untrusted data out of HTML sinks, script, style and event-handler attributes, quote attributes, and never set event-handler attributes from untrusted data.
- Rejected: setAttribute as unconditionally safe (OWASP DOM XSS sheet): loses where the attribute name is an event handler, the condition inferred and to be read verbatim. Encoding into script contexts: rejected by OWASP itself as unreliable.

**PIG-JS.DEFENSE.DOM.3** Sanitizing HTML
- Positions: Native setHTML (MDN, HTML Standard) against sanitizer library (OWASP names DOMPurify) against hand-written filters. Claims DOMSEC-C08, C09, C11, C12, C14, C23.
- Forces: Safety against availability: setHTML is limited-availability, a library is a security-critical dependency with a bypass history.
- Decision: setHTML where available, a reputable library as fallback, sanitize last, never modify afterwards, treat Unsafe-suffixed methods as sinks.
- Rejected: Library-first: wins where the target browsers lack setHTML, which is the stated condition for the fallback. Hand-written sanitizing: rejected by OWASP as hard to get right.

**PIG-JS.DEFENSE.DOM.4** Trusted Types enforcement
- Positions: Enforce with named policies (MDN, W3C, DOMSEC-C15 and C17) against default policy as normal practice (Roth et al., USENIX 2024). Claims DOMSEC-C15, C16, C17, C18, C19, RUNSEC-C19, FW-C48.
- Forces: Strength of the gate against the cost of retrofitting third-party code that cannot pass typed values.
- Decision: Enforce require-trusted-types-for 'script', named policies, report-only rollout, trusted-types-eval in place of unsafe-eval, no sanitizer reuse for script sinks.
- Rejected: Default policy as normal practice: wins only for third-party code that cannot be changed, as MDN and web.dev already allow. Trusted Types as sanitizer: refuted by MDN.

**PIG-JS.DEFENSE.DOM.5** DOM clobbering
- Positions: Local variables and type checks (OWASP clobbering sheet, ASVS 3.2.3) against globals on window. Claims DOMSEC-C49, C50, C51.
- Forces: Safety against the habit of globals.
- Decision: No globals on window or document, instanceof checks, neutralize id and name when sanitizing.
- Rejected: Globals on window: wins nowhere once untrusted HTML is possible.

**PIG-JS.DEFENSE.ORIGIN.1** Cross-origin messages
- Positions: Verified origin by exact match, validated payload, exact target (MDN, HTML Standard, ASVS 3.5.5, OWASP). Claims DOMSEC-C30 to C34.
- Forces: Safety against open messaging between windows.
- Decision: No listener without need, exact origin match, validate syntax and type, exact targetOrigin for confidential data (MDN says always).
- Rejected: Substring or indexOf origin tests: rejected by OWASP as very insecure. Wildcard target: loses when any confidential data is sent.

**PIG-JS.DEFENSE.ORIGIN.2** Frames and window links
- Positions: Sandboxed iframe, separate origin, explicit noopener (MDN, OWASP) against implied noopener only (HTML Standard). Claims DOMSEC-C43 to C47.
- Forces: Containment strength against markup brevity.
- Decision: Sandbox untrusted content, separate origin, no allow-scripts with allow-same-origin, explicit rel=noopener noreferrer.
- Rejected: Implied noopener only (HTML Standard): wins on browsers that implement the default, so explicit rel is harmless extra. Sandbox without separate origin: loses if the content can be opened outside the frame.

**PIG-JS.DEFENSE.ORIGIN.3** Third-party and service worker code
- Positions: Pin and SRI, separate origin for vendor scripts, own-origin service workers (MDN, W3C, OWASP). Claims DOMSEC-C38 to C40, C42, C58.
- Forces: Integrity of third-party code against the convenience of unpinned vendor updates.
- Decision: Pin versions with SRI (sha384 or stronger plus crossorigin), do not treat a data layer as a sandbox, register service workers from own origin only.
- Rejected: Unpinned third-party scripts: wins nowhere for pages with authority over user data.

**PIG-JS.DEFENSE.ORIGIN.4** Web storage
- Positions: No secrets in Web Storage (OWASP, MDN, DOMSEC-C36) against tokens in storage for convenience. DOMSEC-C35 is owned by web_architecture.
- Forces: Safety against client-side session convenience.
- Decision: Web Storage holds no secrets; validate what is read from it and from messages.
- Rejected: Tokens in localStorage: rejected by OWASP session management as always readable by script.

**PIG-JS.DEFENSE.ORIGIN.5** CSP-ready code and policy handoff
- Positions: Strict-CSP-compatible code (CSP3, OWASP) against inline script and handlers; policy design is owned by web_architecture. Claims DOMSEC-C27, C28 and the deferred rows.
- Forces: Safety against inline-code convenience.
- Decision: No inline script, no inline handlers, no string eval, so the strict policy can be deployed.
- Rejected: Domain-allowlist CSP as XSS protection: refuted by a 2016 measurement of 94.72 percent bypassable policies; the nonce or hash policy itself belongs to web_architecture.

**PIG-JS.DEFENSE.INJECTION.2** OS commands
- Positions: spawn or execFile with an argument array against exec with a sanitized string (Node docs, OWASP, Synode). Claims RUNSEC-C23, C24.
- Forces: Safety against convenience of shell strings.
- Decision: Argument array, no shell string built from untrusted input (sanitized or not), no shell option with input; prefer built-in library functions. The sanitized-exec exclusion is stronger than Node's sentence and rests on OWASP's parameterization principle (inferred).
- Rejected: exec with escaped input: refused, because sanitizing does not remove the shell parse; where a shell feature is truly needed, an allowlist of the executable and arguments and least privilege apply.

**PIG-JS.DEFENSE.INJECTION.3** SQL and NoSQL queries
- Positions: Parameters (OWASP, ASVS 1.2.4, driver docs) against escaping (node-postgres pg-format for identifiers, OWASP discouraged); validated scalars for MongoDB. Claims SRVSEC-C16, C18, C20, C21, C24 to C27.
- Forces: Strength of the separation against the need for dynamic identifiers.
- Decision: Parameterized values always; identifiers by fixed allowlist or redesign; MongoDB scalar types, no client operators, no client server-side JavaScript.
- Rejected: pg-format escaping: wins only for names that are genuinely dynamic, such as DDL.

**PIG-JS.DEFENSE.PROTOTYPE.1** Key writes and reads
- Positions: Reject prototype keys, own-property reads, avoid __proto__ (MDN, OWASP, Node threat model). Claims RUNSEC-C02, C03, C07, C12.
- Forces: Safety against terse dynamic code.
- Decision: No untrusted nested writes or merges, Object.hasOwn, avoid __proto__ in new code.
- Rejected: hasOwnProperty on the instance: SUBSET owns the choice of Object.hasOwn.

**PIG-JS.DEFENSE.PROTOTYPE.2** Dictionaries for untrusted keys
- Positions: Map or Set first, Object.create(null) second, literal __proto__ null last (OWASP, MDN, ASVS 15.3.6). Claims RUNSEC-C04, C05, C13, TYPES-C50.
- Forces: Strength of the defence against keeping plain-object ergonomics.
- Decision: Map or Set for untrusted-keyed dictionaries; Object.create(null) when an object is required.
- Rejected: Plain object with filtered keys: weaker, allowed with key rejection.

**PIG-JS.DEFENSE.PROTOTYPE.3** Hardening and evidence
- Positions: Freeze app-owned configuration; lockdown only where tested (MDN, OWASP) against never modifying built-ins (SUBSET). Claims DOMSEC-C52, RUNSEC-C08, C09, C11.
- Forces: Hardening depth against breakage of polyfills and libraries.
- Decision: Freeze configuration (shallow), lock down only in high-sensitivity tested environments, never rely on --disable-proto alone.
- Rejected: Never freeze built-ins: wins for general code, loses in high-sensitivity code where lockdown is tested.

**PIG-JS.DEFENSE.SECRETS.1** Randomness
- Positions: CSPRNG with 128 bits (ASVS 11.5.1, MDN, OWASP) against Math.random. Claims SRVSEC-C01 to C04.
- Forces: Unpredictability against convenience.
- Decision: crypto.randomBytes, randomInt, randomUUID in Node; getRandomValues in browsers; version 4 UUIDs only.
- Rejected: Math.random: refuted by MDN. Version 1 UUIDs: embed time and MAC.

**PIG-JS.DEFENSE.SECRETS.2** Cryptographic APIs and tokens
- Positions: Review of SubtleCrypto designs (MDN); authenticated mode (OWASP only). Claims SRVSEC-C12, C13, C14.
- Forces: Safety against developer discretion on low-level crypto.
- Decision: Have a knowledgeable person review any SubtleCrypto design; encrypt only with authenticated modes (one source, flagged).
- Rejected: Self-reviewed crypto: refuted by MDN's warning.

**PIG-JS.DEFENSE.SECRETS.3** Password storage
- Positions: Argon2id first, scrypt, bcrypt, PBKDF2 for FIPS (OWASP Password Storage). Claims SRVSEC-C10, C11.
- Forces: Brute-force cost against compatibility constraints.
- Decision: Argon2id at 19 MiB, 2 iterations, parallelism 1, with the OWASP fallbacks by condition.
- Rejected: bcrypt, scrypt, PBKDF2: acceptable by OWASP's conditions, FIPS or legacy.

**PIG-JS.DEFENSE.SECRETS.4** Constant-time comparison
- Positions: timingSafeEqual on equal-length digests (Node docs, ASVS 11.2.4, CWE-208) against === comparison. Claims SRVSEC-C05 to C09, LANG-C34.
- Forces: Side-channel resistance against code simplicity.
- Decision: Use the built-in constant-time comparison and keep surrounding code branch-free on secrets; no hand-written constant-time JavaScript.
- Rejected: Ordinary comparison: leaks through timing.

**PIG-JS.DEFENSE.SECRETS.5** Secret handling
- Positions: No hardcoded secrets (OWASP, NDSS 2019 evidence) with environment variables as a weaker fallback. Claims RUNSEC-C47, C48.
- Forces: Safety against operational convenience.
- Decision: Secrets from a dedicated mechanism; environment variables only when nothing else is possible; detect before commit; rotate.
- Rejected: Environment variables as safe store: refuted as restricted by OWASP and by the Node threat model.

**PIG-JS.DEFENSE.SECRETS.6** Leakage through output and memory
- Positions: Generic errors, zero-filled buffers, protected reports, secure heap (ASVS 16.5.1, Node docs). Claims SRVSEC-C60, C63, RUNTIME-C13, C15, C52.
- Forces: Confidentiality against debuggability.
- Decision: Return generic error text, use Buffer.alloc, treat reports as sensitive, use --secure-heap on shared hosts.
- Rejected: Verbose errors to clients: rejected by ASVS.

**PIG-JS.DEFENSE.HOST.1** Permission model
- Positions: Seat belt (Node permissions docs, threat model) against containment of hostile dependencies (Node best-practices page). Claims RUNSEC-C38 to C40, SRVSEC-C54.
- Forces: Realism about guarantees against the appeal of a sandbox.
- Decision: Seat belt for trusted code only, narrow grants, patched Node, never the only control.
- Rejected: Permission model as sandbox: wins nowhere given the documented limits and CVEs.

**PIG-JS.DEFENSE.HOST.2** Inspector exposure
- Positions: Never public, never in production, no SIGUSR1 activation (Node docs). Claims RUNTIME-C51, SRVSEC-C40.
- Forces: Safety against live debugging.
- Decision: No exposed inspector; attach a SIGUSR1 listener to block activation.
- Rejected: Inspector on a public address: documented as insecure.

**PIG-JS.DEFENSE.HOST.3** HTTP parsing and smuggling
- Positions: Strict parser plus front-end normalization (Node best practices, CVE-2026-58044). Claims SRVSEC-C57, C58, C59.
- Forces: Strictness against interoperability with sloppy clients.
- Decision: Never set insecureHTTPParser; normalize at the front end; HTTP/2 end to end where possible.
- Rejected: Lenient parser: accepts requests the strict one rejects.

**PIG-JS.DEFENSE.HOST.4** Regex cost
- Positions: Bounded input and patterns, non-backtracking engine where available (OpenSSF, V8 blog, OWASP). Claims RUNSEC-C30 to C35, TYPES-C32.
- Forces: Availability against expressive patterns.
- Decision: Bound length and repetition, avoid nested quantifiers, anchor, prefer a non-backtracking engine where one exists.
- Rejected: Assuming V8 has a non-backtracking engine: restricted, experimental and flagged.

**PIG-JS.DEFENSE.HOST.5** Parser resource limits
- Positions: Parser limits (OWASP input validation) and a patched Node (CVE-2026-21717). Claims TYPES-C31, RUNSEC-C37.
- Forces: Availability against unlimited request bodies.
- Decision: Set size, depth and number limits; keep Node patched.
- Rejected: Unlimited parsing: wins nowhere for hostile input.

**PIG-JS.DEFENSE.HOST.6** Module load path
- Positions: Trusted module directories (Node best practices, threat model). Claim SRVSEC-C64.
- Forces: Integrity of the load path against deployment ease.
- Decision: Treat module directories as trusted and harden them.
- Rejected: Writable module directories: outside Node's vulnerability scope.

**PIG-JS.DEFENSE.DOM.2.1** Script URL sinks
- Positions: Allowlisted or Trusted script URLs (OWASP, MDN, DOMSEC-C24) against loading any URL a component computes.
- Forces: Safety against flexibility of plugin and worker loading.
- Decision: Pass only allowlisted or Trusted URLs to script and worker sinks.
- Rejected: Free-form script URLs: would win only for code that never receives input, where the question does not arise.

**PIG-JS.DEFENSE.DOM.2.2** Redirect targets
- Positions: Redirect only to an allowlist (ASVS 3.7.2) against redirect to any validated-looking URL. DOMSEC-C56.
- Forces: Safety against convenient return-URL parameters.
- Decision: Redirect automatically only to allowlisted destinations.
- Rejected: Denylist or syntax checks on the destination: would win never on safety, since encodings defeat them.

**PIG-JS.DEFENSE.DOM.6.1** Escape hatches
- Positions: Default encoding plus escape hatches as sinks (OWASP XSS sheet, consensus). Claims DOMSEC-C55, FW-C02.
- Forces: Safety against framework convenience.
- Decision: Treat every documented escape hatch as a sink that receives sanitized input.
- Rejected: Framework output as safe in all paths: refuted by the hatches the framework documentation itself names.

**PIG-JS.DEFENSE.INJECTION.1.1** Strings as code
- Positions: No code from strings (MDN, OWASP, CSP3, Synode study) against Google's code-loader exception and indirect eval as mitigation. Claims DOMSEC-C03, ASYNC-C33, RUNSEC-C15 to C18, LANG-C49.
- Forces: Safety against the few legitimate dynamic-evaluation uses.
- Decision: Never evaluate untrusted strings, JSON.parse for data, enforce no-eval, no-implied-eval and no-new-func.
- Rejected: Google's code-loader exception: wins for loaders the application itself writes. Indirect strict eval: only when evaluation is unavoidable, cuts scope exposure not injection.

**PIG-JS.DEFENSE.INJECTION.1.2** The vm module
- Positions: node:vm is not a security mechanism (Node vm docs, RUNSEC-C22).
- Forces: Safety against the misreading of separate contexts as isolation.
- Decision: Never run untrusted code in node:vm.
- Rejected: vm as sandbox: refuted by the module's own warning.

**PIG-JS.DEFENSE.INJECTION.4.1** Containment check
- Positions: Canonicalize then compare (CWE-22, Node docs on isAbsolute and normalize, Express root option). Claims RUNSEC-C27, C29, SRVSEC-C47, C48, C49, C51.
- Forces: Safety against lexical convenience.
- Decision: Resolve symlinks and normalize, then check containment; validate the result of fileURLToPath; set root in Express.
- Rejected: path.normalize or isAbsolute alone: refuted by the Node docs. Prefix-stripping sanitization: broken by the node-tar advisory.

**PIG-JS.DEFENSE.INJECTION.4.2** Archive extraction
- Positions: Ignore archive-supplied paths, reject symlinked archives (ASVS 5.3.3, 5.2.5, Zip Slip). Claims SRVSEC-C50, C52.
- Forces: Safety against extraction convenience.
- Decision: Compute destination paths yourself; refuse symlinks unless required, then allowlist.
- Rejected: Trusting entry names: refuted by Zip Slip.

**PIG-JS.DEFENSE.INJECTION.4.3** Check then use
- Positions: Open and handle the error (Node fs docs) against access-then-open. Claims RUNTIME-C18, SRVSEC-C53.
- Forces: Race freedom against a friendly pre-check.
- Decision: Open directly and handle the error.
- Rejected: Pre-check with fs.access: wins nowhere for a guard; allowed only to report, never to authorize.

**PIG-JS.DEFENSE.INJECTION.5.2** YAML and legacy serializers
- Positions: js-yaml 4 safe by default (changelog) against js-yaml 3 load and node-serialize. Claims SRVSEC-C41, C42.
- Forces: Safety against legacy compatibility.
- Decision: js-yaml 4 or later for untrusted YAML; node-serialize never for untrusted input.
- Rejected: js-yaml 3 or the js-types package: would win only for trusted input.

**PIG-JS.DEFENSE.INJECTION.6.1** Destination rules
- Positions: Allowlist (OWASP SSRF, ASVS 1.3.6) against deny-list fallback; WHATWG URL against url.parse (Node docs). Claims SRVSEC-C29, C31.
- Forces: Strength against the cases where destinations are not enumerable.
- Decision: Match hosts against an allowlist and parse with the WHATWG URL class.
- Rejected: OWASP minimum deny-list: only when an allowlist is impossible.

**PIG-JS.DEFENSE.INJECTION.6.2** Connection to the validated address
- Positions: Resolve once, validate, connect to that address (OWASP SSRF, Node dns and net docs). Claims SRVSEC-C33, C34, C39.
- Forces: Rebinding resistance against code simplicity.
- Decision: Resolve to an address, check it, connect to the address.
- Rejected: Hostname check alone: refuted by DNS rebinding.

**PIG-JS.DEFENSE.INJECTION.6.3** Redirect handling
- Positions: the rule (redirects off or revalidated, ASVS 15.3.2, OWASP SSRF) is owned by the node on Node fetch redirect semantics; this node records that the opaque-redirect response of manual mode is browser behaviour.
- Forces: One owner for a rule against two statements of it.
- Decision: no rule of its own.


**PIG-JS.DEFENSE.SECRETS.2.1** Token and JWT verification
- Positions: (a) the verifier fixes algorithm, key source, issuer, audience, validity and type (RFC 8725 3.1, 3.3, 3.8, 3.9; ASVS 9.1.2, 9.1.3, 9.2.1 to 9.2.3; OWASP JWT sheets); (b) trust the token's own alg and key hints. Claims SECGAP2-C01, C02, C04 to C09, C15, C17 (C16 deferred).
- Forces: Forgery resistance against the convenience of letting tokens describe themselves.
- Decision: (a), every check as a MUST, exp required on every token (stricter than ASVS 9.2.1); an unsecured token never; one call never accepts both symmetric and asymmetric algorithms for one key.
- Rejected: (b): refuted by the algorithm-confusion and alg-none attacks; wins under no grounded condition. Reading RFC 7519 section 8 alone as the algorithm policy: it states what libraries implement, not what a consumer accepts.

**PIG-JS.DEFENSE.SECRETS.2.2** Token library settings
- Positions: (a) pass an explicit algorithms list to jsonwebtoken verify and to jose jwtVerify; (b) rely on the per-key-type default (jsonwebtoken) or all algorithms applicable to the key (jose). Claims SECGAP2-C10 to C14.
- Forces: The caller-fixed allowlist rule of the node above against less code.
- Decision: (a); jsonwebtoken 9.0.0 or later; decode is never verification. C11 and C14 are inferred from the library defaults plus the allowlist rule, since no source tells the caller to always pass the option.
- Rejected: (b): wins only where the key type already fixes the single algorithm the application intends.

**PIG-JS.DEFENSE.INJECTION.1.3** Template injection
- Positions: (a) never build a template from untrusted input; (b) allow user templates in a trivial engine inside a sandbox (Kettle, T3); (c) isolation and allowlisted helpers (Handlebars guide). Claims SECGAP2-C30, C32, C38 (C31 on the philosophy node).
- Forces: Removal of the code-execution class against products that let users write templates.
- Decision: (a) as the MUST; (b) kept as acceptable-when user templates cannot be avoided, flagged as one T3 position that concedes execution may happen.
- Rejected: (b) as the rule: it accepts code execution and rests on one T3 author; wins when the product requires user-written templates. (c): kept as the Handlebars-specific rule of the next node.

**PIG-JS.DEFENSE.INJECTION.1.4** Handlebars and EJS
- Positions: engine documents and advisories: Handlebars (security page, CVE-2026-33937), EJS (security policy, CVE-2022-29078). Claims SECGAP2-C33 to C37 (C39 open).
- Forces: Exact vendor statements against the lack of guidance for other engines.
- Decision: each statement as a MUST on its engine; version floors as MUST. Engine facts about those two engines only.
- Rejected: Extending the rules to Pug, Nunjucks or others: no admitted T1 states them (C39); wins when such a source is admitted.

**PIG-JS.DEFENSE.INJECTION.4.5** Upload content checks
- Positions: (a) extension allowlist plus content check plus re-encoding or scanning (OWASP File Upload, ASVS 5.2.2, 5.4.3); (b) trust Content-Type or name. Claims SECGAP2-C40, C46 (C48 open).
- Forces: Server-side proof against client-supplied labels.
- Decision: (a). The JavaScript signature-check recipe is open (C48), so the rule is language-neutral.
- Rejected: (b): the client controls both; wins under no condition.

**PIG-JS.DEFENSE.INJECTION.4.6** Upload storage, names and limits
- Positions: (a) server-generated names, storage outside the web root, explicit limits, no global multer, decompression bounds, encoded served names (OWASP File Upload, ASVS 5.2.1, 5.2.3, 5.2.6, 5.3.1, 5.3.2, 5.4.1, 5.4.2, busboy and multer documentation); (b) library defaults. Claims SECGAP2-C41 to C45, C47.
- Forces: Containment and bounded cost against defaults of Infinity for file size, files and parts.
- Decision: (a), each as a MUST.
- Rejected: (b): the defaults are unbounded; wins under no grounded condition.

**PIG-JS.DEFENSE.INJECTION.5.4** XML and external entities
- Positions: (a) DTDs off, external entities and external DTDs off, partial hardening a failure, XSD over DTD (OWASP XXE and XML Security sheets, ASVS 1.5.1); (b) parser defaults. Claims SECGAP2-C19 to C21 (C18 on the philosophy node, C22 open).
- Forces: Safety against not knowing which Node parsers resolve entities (C22).
- Decision: (a); fast-xml-parser version floor and processEntities false as a separate denial-of-service rule.
- Rejected: (b): Node parser defaults are not grounded, so they cannot be relied on; wins when a source states a parser's defaults.

**PIG-JS.DEFENSE.HOST.3.1** Header field values
- Positions: (a) reject CR, LF and NUL, validate with Node's validators before reuse (setHeader throws on its own), reject application strings bound for other APIs (RFC 9110 5.5, Node http page, Node source, Node threat model, undici advisory, CWE-113). Claims SECGAP2-C24 to C28 (C23 on the philosophy node); (b) strip or replace characters silently.
- Forces: Rejection against repair; the application owns validation (C26).
- Decision: (a); a string is rejected, never repaired.
- Rejected: (b): RFC 9110 allows replacing with a space for a recipient, but a sender that repairs hides the injection; wins for a recipient that must tolerate legacy clients.

**PIG-JS.DEFENSE.HOST.3.2** Connection-specific fields
- Positions: (a) accept HTTP/2 and HTTP/3 requests only without CR, LF, CRLF and without connection-specific fields (ASVS 4.2.3, 4.2.4, Level 3); (b) no rule. Claim SECGAP2-C29.
- Forces: Downgrade and smuggling safety against compatibility.
- Decision: (a), flagged single-source.
- Rejected: (b): wins for HTTP/1.1-only services, where 4.2.4 does not apply.

**PIG-JS.DEFENSE.ORIGIN.2.1** Framing of the own page
- Positions: (a) frame-ancestors on every response as a header (ASVS 3.4.6, OWASP Clickjacking sheet, CSP3); (b) frame-ancestors and X-Frame-Options together (OWASP and MDN Clickjacking recommend both); (c) X-Frame-Options alone. Claims SECGAP2-C63, C64, C67, C68 (contested, C68).
- Forces: Coverage of older browsers against a second header that cannot express allowed framers.
- Decision (max rule): (a) plus a matching X-Frame-Options fallback where the policy is none or self; where other origins are allowed, omit it. The condition is inferred from the ALLOW-FROM support gap (C67).
- Rejected: frame-ancestors alone (ASVS requires the directive and is silent on a fallback; CSP3 and RFC 7034 hold that the directive supersedes): wins where every supported browser implements frame-ancestors. X-Frame-Options alone: ALLOW-FROM unsupported, loses to the directive.

**PIG-JS.DEFENSE.ORIGIN.2.2** Frame-busting and double clicks
- Positions: (a) no frame-busting reliance, server-enforced authorization for sensitive double-click actions (OWASP Clickjacking sheet). Claims SECGAP2-C65, C66; (b) a frame-busting script.
- Forces: A defence outside the attacker's frame context against a script inside it.
- Decision: (a).
- Rejected: (b): defeated by double framing, onBeforeUnload and the sandbox attribute; wins under no condition.

**PIG-JS.DEFENSE.ORIGIN.6.1** Primary defence
- Positions: OWASP and MDN both list a Fetch Metadata check among the primary CSRF defences (OWASP: its own section beside token-based mitigation, before the defence in depth techniques; MDN: the third primary-defence bullet); neither says it suffices alone and neither requires a token beside it. OWASP allows same-site only where sibling subdomains are trusted and makes the Origin or Referer fallback mandatory for browsers without the header. Claims SECGAP2-C55, C56, C58, C69, C92.
- Forces: Independence from browser support against one fewer mechanism.
- Decision (max rule): a synchronizer or signed double-submit token as the primary defence; the Sec-Fetch-Site check (same-origin, same-site only when the threat model trusts sibling subdomains) and the Origin or Referer fallback layered behind it; tokens unique per session, random, never in a URL, a GET request or a log, compared in constant time. Stricter than both sources, flagged in epistemic_state.
- Rejected: a Sec-Fetch-Site check as the only primary defence (listed as primary by MDN and OWASP): kept as acceptable-when every supported browser sends the header, a build judgment about the condition.

**PIG-JS.DEFENSE.ORIGIN.6.2** Methods and API endpoints
- Positions: (a) no state change through GET, HEAD or OPTIONS; preflight reliance only when no preflight-free request reaches the functionality (OWASP, MDN, ASVS 3.5.1 to 3.5.3). Claims SECGAP2-C57, C60.
- Forces: Safe methods and simple requests skip the cross-site protections.
- Decision: (a).
- Rejected: state change through a safe method: wins under no condition.

**PIG-JS.DEFENSE.ORIGIN.6.3** SameSite and CSRF libraries
- Positions: (a) SameSite as depth, per cookie purpose; csurf not for new code (archive notice, Express blog); (b) SameSite Lax as the defence; (c) csurf. Claims SECGAP2-C61, C62.
- Forces: Defence in depth against reliance on one cookie attribute; a maintained dependency against an archived one.
- Decision: (a).
- Rejected: (b): Lax withholds cookies only on cross-site requests with unsafe methods and does not cover client-side CSRF. (c): archived, no replacement named; wins under no condition for new code, and is a maintenance decision for existing code.

**PIG-JS.DEFENSE.DOM.2.3** URL validation by parsing
- Positions: (a) parse (the parsing rule is owned by INJECTION.6.1), compare parsed scheme, canonical host and effective port with an allowlist, reject userinfo, refuse javascript: and data:, use a parser that agrees with the consumer (URL Standard, OWASP Unvalidated Redirects sheet, ASVS 1.2.2); (b) substring or prefix tests; (c) legacy url.parse. Claims DOMSEC-C57, SECGAP2-C70 to C74 (C75 open).
- Forces: One parse, one verdict, against the cost of an allowlist.
- Decision: (a), composed from grounded steps; the former gap on the javascript: scheme is closed by C73.
- Rejected: (b): a prefix or suffix test accepts attacker hosts that begin or end with an allowed string. (c): see INJECTION.6.1. Specific parser differentials stay open (C75).

**PIG-JS.DEFENSE.INJECTION.5.3** v8.deserialize
- Positions: (a) apply the general deserialization rules to it: integrity check first, new object from validated fields (CWE-502, ASVS 15.1.5, SRVSEC-C45, RUNSEC-C44); (b) treat it as safe; (c) treat it as unsafe and forbid it. Claims SRVSEC-C44, SECGAP2-C83 to C85.
- Forces: Safety on an unstated question against forbidding a built-in on no evidence.
- Decision: (a). It claims no more than the sources: whether the function is safe for untrusted bytes stays open (C85).
- Rejected: (b): no source says so. (c): no source says so; wins if the Node or V8 documentation states that the format is unsafe.

**PIG-JS.DEFENSE.INJECTION.6.4** Node fetch redirect semantics
- Positions: (a) error when no redirect is expected, manual with revalidation otherwise, Node kept current, header stripping not relied on (undici code and advisories, MDN values, ASVS 15.3.2, OWASP SSRF); (b) follow redirects automatically. Claims SRVSEC-C35 to C37, SECGAP2-C86 to C91.
- Forces: Revalidation of each hop against transparent following; the advisories show header stripping has been incomplete.
- Decision: (a). The Fetch Standard gives manual mode an opaque-redirect response whose Location cannot be read (SRVSEC-C36), but undici's code returns the actual response (C91), so revalidating every Location target is workable in Node; Node's own pages are silent.
- Rejected: (b): wins only for known-trusted destinations.

**PIG-JS.DEFENSE.INJECTION.4.1** Containment check (slot 14 addition)
- Added: never a raw string-prefix comparison (CVE-2026-48049, claim SECGAP2-C76); path.resolve lets an absolute input replace the base (C78); isAbsolute and normalize facts merged into the rejected belief (C77, C79); Node leaves validation to the application (C80).

Integration note (DEFENSE): in the record of PIG-JS.DEFENSE.PROTOTYPE.1 the claim RUNSEC-C07 (Object.hasOwn) is held by PIG-JS.SUBSET.OBJECTS.6; the decision text above stays as the branch wrote it.

### DEPENDENCIES

One record per defaults node holding a decision. Positions come from the evidence (claim ids, source ids), forces name the purpose served and the cost, the decision is the max choice, rejected lists each other position with the condition under which it would win.

#### PIG-JS.DEPENDENCIES.INSTALL.1 (Frozen install)

- Positions: (a) npm install resolving from the manifest (the common default); (b) npm ci or the manager's frozen-lockfile equivalent: SUPPLY-C04 (SRC-150, SRC-078, SRC-154, SRC-155, consensus), QUALITY-C42 (SRC-173, re-read from the v12 page).
- Forces: Trust wants the tree that was reviewed to be the tree installed; (a) costs convenience of silent lockfile refresh, (b) costs one explicit update step.
- Decision: (b) in CI and production, with a lockfile required; the lockfile is committed (DEPENDENCIES.CHANGE.1). Grounds: four T1 sources agree; the 12_dissent folklore audit confirms 'commit the lockfile and install with npm ci'.
- Rejected: (a): would win only in the deliberate update step that regenerates the lockfile, never in CI or production.

#### PIG-JS.DEPENDENCIES.INSTALL.2 (Install scripts blocked)

- Positions: (a) block install scripts by default and approve reviewed packages through an exact-version allowlist: SUPPLY-C08 (SRC-153, SRC-151), SUPPLY-C10 (SRC-153, SRC-158, consensus); (b) disable scripts globally with --ignore-scripts and allowlist the few that need them: SUPPLY-C09 (SRC-078, SRC-155, SRC-288, consensus); (c) run all scripts, the pre-v12 npm default.
- Forces: Trust wants no code to run before review; the cost is a maintained allowlist and packages that legitimately build at install.
- Decision: (a): per-package approval pinned to the exact version, guard never disabled globally. Grounds: two independent bodies (npm docs, pnpm docs) and OWASP and Node guidance on the same risk; install scripts are a confirmed supply-chain risk (12_dissent).
- Rejected: (b): acceptable when the manager still runs scripts by default (npm before v12, SRC-078 restriction), with an allowlist. (c): rejected, no admitted source supports it; wins under no stated condition. Disabling the guard globally on a default-block manager: rejected by SUPPLY-C10.

#### PIG-JS.DEPENDENCIES.INSTALL.3 (Non-registry sources)

- Positions: (a) allow git and tarball dependencies freely; (b) allow them for the root project only; (c) refuse them: SUPPLY-C11 (SRC-151, SRC-152) states the npm 12 default refusal and 'root rather than all'.
- Forces: Trust wants every dependency to pass the registry's controls; the cost is projects that really need a fork or a pre-release.
- Decision: (b) when needed, over the refusal default of npm 12 (the most demanding the claim supports is the default itself, taken as is). Single-source and inferred.
- Rejected: (a) 'all': rejected by the claim; would win under no condition grounded in the register.

#### PIG-JS.DEPENDENCIES.INSTALL.4 (Owned scope for internal packages)

- Positions: (a) internal packages under unscoped names; (b) internal packages under an owned scope routed to the private registry in .npmrc: SUPPLY-C26 (SRC-155 OWASP, SRC-143 scope ownership, SRC-145 CVE-2021-24105 for the confusion class).
- Forces: A public package of the same name must not win resolution; the cost is a scope to own and one registry mapping.
- Decision: (b). Grounds: OWASP mitigation plus facts on scope ownership and the CVE class; SRC-143 alone states scope facts only and does not address confusion, so the normative step rests on SRC-155.
- Rejected: (a): wins under no grounded condition.

#### PIG-JS.DEPENDENCIES.UPDATE.1 (Release-age cooldown)

- Positions: (a) no cooldown, adopt versions at once; (b) tool-default cooldown: SUPPLY-C12 (T1 assertion SRC-078 §Mitigations; tool facts SRC-152, SRC-158, SRC-146) with security updates exempt (SUPPLY-C14); (c) a three-day cooldown as an OpenSSF position (QUALITY-C46, origin missing); (d) a longer custom duration: no source.
- Forces: Exposure window to a freshly hijacked release against lag in receiving fixes; effect unmeasured (SUPPLY-C13: one T1 assertion plus vendor figures from SRC-319).
- Decision: (b), with security updates outside the cooldown. The max rule picks the more demanding delay; the length stays at the tool default because (d) has no source (undecided child UPDATE.1.1). SUPPLY-C12's 'consensus' label is relabelled single-source. Grounds: one T1 assertion.
- Rejected: (a): wins for a version that fixes an exploited vulnerability, which is the security-update exemption. (c): not rejected as the body's position, but its effectiveness claim is not used as evidence until the origin is found. (d): undecided.

#### PIG-JS.DEPENDENCIES.UPDATE.2 (Supported runtime and toolchain)

- Positions: Runtime: (a) any Node release; (b) Active or Maintenance LTS only: TYPES-C45 (SRC-037); (c) Active LTS only (more demanding, no source). Toolchain: (d) float TypeScript and Node; (e) pin to the framework's compatibility table: FW-C24 (SRC-207, Angular 22) and FW-C26 (SRC-231, Vue typings may change in minors).
- Forces: Security fixes reach only supported lines; frameworks couple to narrow TypeScript ranges; the cost is staying inside the table.
- Decision: (b) and (e). (c) is more demanding but no admitted source says Maintenance LTS is insufficient. Two framework sources, independent, support (e).
- Rejected: (a) Current in production: wins under no grounded condition (SRC-037 labels Current non-LTS). (c): would win if a T1 source states that Maintenance LTS stops receiving fixes that matter. (d): wins only for a framework that publishes no compatibility table (none in the register).

#### PIG-JS.DEPENDENCIES.UPDATE.3 (Audit in CI)

- Positions: (a) run npm audit against the committed lockfile with audit-level: SUPPLY-C21 (SRC-149, SRC-152); (b) treat every finding as exploitable; (c) ignore audit as noise; (d) audit runtime dependencies only on the strength of the dependencies split.
- Forces: Known-vulnerability data is cheap and noisy: 68.28 percent of package-level impacts are unreachable (SUPPLY-C22, SRC-285, SRC-286).
- Decision: (a), findings read as triage input (DEPENDENCIES.EVIDENCE.2). Restriction check: SRC-149 grounds the behaviour (lockfile dependence, threshold), not audit accuracy, and no preference for npm over another tool is stated; the lockfile and triage rules are decisions on that ground; running npm audit as the check is acceptable-when, since no admitted source states it as a practice. Threshold value: undecided child UPDATE.3.1.
- Rejected: (b) and (c): refuted or unsupported by the two T2 studies (folklore refuted). (d): rejected by SUPPLY-C23 (28.2 percent of dev-configured dependencies were used in production). Audit without a lockfile: results differ per run (SUPPLY-C21).

#### PIG-JS.DEPENDENCIES.SCREEN.1 (Scorecard as per-check evidence)

- Positions: (a) Scorecard results as per-check evidence: SUPPLY-C35, QUALITY-C44 (SRC-161 §checks); (b) the aggregate score as a safety gate.
- Forces: Cheap automated signal against the risk of mistaking a score for safety; the cost is reading checks one by one.
- Decision: (a). SRC-161's restriction allows 'Scorecard rewards X', not that X is effective, and states 'a score is never evidence a package is safe'; the decision restates that limit and recommends nothing else.
- Rejected: (b): rejected by the source's own limit; wins under no condition.

#### PIG-JS.DEPENDENCIES.PUBLISH.1 (CI publishing credentials)

- Positions: (a) long-lived tokens in CI; (b) trusted publishing with OIDC and short-lived credentials: SUPPLY-C15 (SRC-160, SRC-141, SRC-155 OWASP, consensus); (c) stage-only tokens as the fallback (SUPPLY-C16, SRC-141).
- Forces: Trust wants no long-lived secret in CI; the cost is a supported CI provider and npm 11.5.1 or later with Node 22.14 or later (SRC-160).
- Decision: (b), provenance then generated automatically for public repositories (SUPPLY-C20). SUPPLY-C16 (token policy dates) is a dated fact, demoted from decision (SRC-141 restriction).
- Rejected: (a): legacy tokens are removed (Nov 2025) and direct publishing with a granular token ends (Jan 2027); it would win only where (b) is unavailable, then (c).

#### PIG-JS.DEPENDENCIES.PUBLISH.2 (Tarball contents)

- Positions: (a) publish what the directory holds; (b) review the file list before every publish with npm publish --dry-run, keep secrets out, least-privilege CI tokens: SUPPLY-C38 (SRC-155, SRC-156, SRC-161, consensus), SRVSEC-C62 (SRC-078).
- Forces: Accidental exposure is permanent once published; the cost is one review step.
- Decision: (b); unpublish on exposure (SRVSEC-C62). Grounds: three T1 sources.
- Rejected: (a): the default behaviour publishes all files unless excluded; wins under no condition.

#### PIG-JS.DEPENDENCIES.PUBLISH.3 (Ship JavaScript)

- Positions: (a) publish TypeScript source; (b) publish JavaScript: TYPES-C07 (SRC-038, inferred).
- Forces: Consumers' runtime must load the package; the cost is a build step.
- Decision: (b). Grounds: Node refuses to handle TypeScript files under node_modules (T1).
- Rejected: (a): would win only for code consumed outside node_modules by a build the project controls; inferred from the stated limitation.

#### PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 (Support window)

- Positions: (a) the main htmx docs site documents 2.x (2.0.11): SRC-213; (b) the security policy and release page show 4.x current with 2.x and 1.9.x supported: SRC-212, SRC-214 (FW-C21, FW-C22).
- Forces: Newest supported major gets fixes longest; docs lag the release line.
- Decision: Pin a supported major and read its own documentation set; a new adoption takes the newest supported major (4.x). Mechanism is not contested, only documentation currency (12_dissent topic 16). 4.0.0 release date is open.
- Rejected: (a) as the current line: wins for an existing project already on 2.x, while 2.x stays on the supported list. 1.9.x: same condition.

#### PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 (Measured usage)

- Positions: (a) rank candidates by measured usage; (b) use measured usage as context only: FW-C42, C43, C45, C49 (SRC-310, SRC-311, SRC-309).
- Forces: Usage figures come from one crawl with Wappalyzer detection and cover React, jQuery and platform features only.
- Decision: (b). The register's standing rule (popularity is not authority) and the measurement limits agree.
- Rejected: (a): would win only with an admitted per-candidate measurement and method (late candidate: HTTP Archive technology report read as data).

#### PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST (Framework short list)

- Positions: Candidates and their evidence are in the framework evidence matrix (build/research/10_frameworks/result.md, L3 full). Positions: (a) an earlier proposal: React, Angular, Vue, Lit, htmx, no framework as comparator; (b) this note: gates on trust evidence; (c) rank by popularity.
- Forces: Purpose is trust: third-party code with your privileges. The most demanding practice states what the code is, who maintains it and for how long it is patched, and adds the least third-party code. Framework documentation grounds facts about that framework only, so the gates are the build's judgment, recorded here.
- Decision: Gate A (mandatory): the candidate states which versions receive security fixes, as the guideline itself runs only supported versions (TYPES-C45, SUPPLY-C36, SUPPLY-C28). Gate B: a documented escape and sanitization model (framework evidence matrix, owned by DEFENSE). Gate C: stated governance or maintenance body. Pass A and at least one of B or C. Short list, unranked among frameworks because no admitted source can rank them: (1) the platform with Web Components and no framework, default; (2) htmx; (3) Lit; (4) Angular; (5) React. Matrix: React A yes (FW-C25), B yes, C yes (FW-C31, provisional); Angular A yes (FW-C23, strongest), B yes, C open (FW-C35); Lit A yes (FW-C28), B open (FW-C16), C yes (FW-C34); htmx A yes (FW-C21), B yes, C open (FW-C35); Vue A no (FW-C26), B yes, C partial (FW-C32); Svelte A no (FW-C27), B yes, C open; Solid A no (FW-C29, FW-C30), B no (FW-C15, FW-C16), C partial (FW-C33).
- Rejected: Vue: wins if an admitted source states a Vue security-fix window, and then names a legal entity or funding; it is the closest runner-up. Svelte: wins with a supported-versions statement and a governance source. Solid: wins with a support policy and a default-escaping description. (c) popularity: rejected, the standing rule; only React has a figure. 'A framework is always needed': wins when a requirement is not met by the platform (SUPPLY-C27 test). Left off for missing evidence, not for merit; reopen when sources appear.

#### PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 (Platform baseline)

- Positions: (a) the platform's custom elements, shadow DOM and templates with no library: FW-C46 (SRC-235 MDN), FW-C47 (SRC-211 HTML Standard); (b) adopt a framework by default.
- Forces: Zero third-party runtime code against the work a framework saves.
- Decision: (a) is the default and the first candidate (DEPENDENCIES.ADMISSION.1, SUPPLY-C27); custom element names carry a hyphen (T1).
- Rejected: (b): wins when a requirement exists that the platform does not meet and the SUPPLY-C27 isolation test confirms it.

#### PIG-JS.DEPENDENCIES.INSTALL.5 (Expected repository and inventory)

- Positions: (a) an inventory or SBOM that checks every component, direct and transitive, comes from its expected repository (ASVS 15.1.2, 15.2.4); (b) no inventory. Claim SECGAP2-C51.
- Forces: Repository provenance against the upkeep of an inventory.
- Decision: (a), flagged single-source (one ASVS pair, Levels 2 and 3). It states provenance, not a name-screening method.
- Rejected: (b): wins for a project with no third-party runtime dependencies.

### VERIFICATION

Format: Positions (claim ids, source ids) / Forces / Decision / Rejected with the condition under
which it would win. Where the admitted evidence holds a single position, the record says so
instead of inventing an alternative.

#### PIG-JS.VERIFICATION.LINT.1.1
- Positions: flat config at the root, `files` and `ignores`, later objects win (QUALITY-C01, C02; SRC-166). No competing position in admitted sources; the legacy eslintrc format is named only as not relied on (QUALITY-C28 note).
- Forces: predictability of what runs on which file (merge order is deterministic) against nothing; cost is one migration for old projects.
- Decision: one `eslint.config.js` (or .mjs or .cjs) at the root exporting an array, general objects first.
- Rejected: the legacy eslintrc format, because the admitted page documents only the flat format as current; it would win for a code base pinned to an ESLint version that predates flat config (condition inferred, no source).

#### PIG-JS.VERIFICATION.LINT.1.2
- Positions: recommended config as baseline (QUALITY-C03; SRC-167); typescript-eslint recommended as the drop-in TypeScript baseline, stylistic as separate opt-in (QUALITY-C04; SRC-054).
- Forces: correctness floor without hand-curation against over-reporting; the recommended set is maintained by the tool's authors.
- Decision: start from recommended, add typescript-eslint recommended for TypeScript; keep stylistic rules out of the correctness gate.
- Rejected: a hand-built rule list as the floor, because the rules index marks the maintained set; it wins only where a project needs a rule the set lacks, added on top. Suitability of the baseline is inferred (the sources define the marker, not its sufficiency).

#### PIG-JS.VERIFICATION.LINT.1.3
- Positions: strict only if a nontrivial share of developers is highly proficient, set may change outside major versions (QUALITY-C09; SRC-054).
- Forces: stronger checking against onboarding cost and churn in findings.
- Decision: the max practice is the strict set; it is taken when the proficiency condition, which the project itself states, holds.
- Rejected: strict for every team, because the project's own advice denies it; it would win once the team meets the condition. Recommended-only stays the floor (LINT.1.2).

#### PIG-JS.VERIFICATION.LINT.1.4
- Positions: typed linting through `parserOptions.projectService` for rules such as no-floating-promises (QUALITY-C10; SRC-181); cost is a whole-project TypeScript analysis before linting. TypeScript 7.0 has no API until 7.1 (TYPES-C44; SRC-034).
- Forces: defects invisible to syntax rules against lint time.
- Decision: enable typed linting in TypeScript projects and budget its time. No admitted figure for the cost (G-L20).
- Rejected: syntax-only linting, because no-floating-promises and similar rules need types; it wins where the project has no TypeScript project to analyze or where lint time is shown to block the workflow (inferred).

#### PIG-JS.VERIFICATION.LINT.2 (Enforcement)
- Positions: the lint job is a required check that may be skipped by the platform's rules (GitHub required status checks pass on successful, skipped or neutral conclusions, QUALITY-C43 held by js-philosophy VERIFICATION.ENFORCEMENT) against a lint job that always runs.
- Forces: a gate that can be skipped is not a gate; the cost is one always-running job.
- Decision: make the CI job that runs the lint gate always run. The rule is the platform fact applied to this node (added at stage 7 so the philosophy node stays platform-neutral).
- Rejected: a conditionally skipped lint job: wins nowhere for a required check.

#### PIG-JS.VERIFICATION.LINT.2.1
- Positions: `--max-warnings 0` so warnings change the exit status; default -1 means no limit (QUALITY-C05; SRC-165).
- Forces: no tolerated drift against the cost of cleaning up existing warnings first.
- Decision: CI runs with `--max-warnings 0`.
- Rejected: the default (warnings never fail), because the documented exit rule leaves them invisible to CI; it wins during a staged migration with a recorded end date (inferred).

#### PIG-JS.VERIFICATION.LINT.2.2
- Positions: exit 0 clean, 1 findings, 2 configuration or internal error (QUALITY-C06; SRC-165).
- Forces: a broken gate must not read as a pass or as code defects.
- Decision: CI scripts distinguish exit 2 from exit 1 and treat 2 as a broken tool.
- Rejected: any non-zero is one failure, because it hides a broken configuration behind a code-defect message; wins only for a throwaway script (inferred).

#### PIG-JS.VERIFICATION.LINT.2.3
- Positions: report unused disable directives, flag or severity variant, default warn (QUALITY-C07; SRC-165).
- Forces: stale exceptions hiding future errors against noise on first enabling.
- Decision: report unused directives; with LINT.2.1 the default warn binds.
- Rejected: leave them unreported, because obsolete suppressions then hide errors; it wins never as a default.

#### PIG-JS.VERIFICATION.LINT.2.4
- Positions: `--cache`, strategy `metadata` (default) or `content` (QUALITY-C08; SRC-165).
- Forces: gate speed against stale-cache risk on checkouts that reset modification times.
- Decision: use `--cache` and, where modification times change without content changes (fresh CI checkouts, inferred), `--cache-strategy content`.
- Rejected: no cache, because repeated runs relint unchanged files; wins when the cache directory cannot persist between runs (inferred).

#### PIG-JS.VERIFICATION.LINT.3
- Positions: eslint-plugin-security maintainers state it finds many false positives that need human triage (QUALITY-C45; SRC-164).
- Forces: catching injection leads against alert fatigue.
- Decision: findings are hotspots for human triage and are not verdicts. Whether to run the plugin at all has no admitted ground (boundary DEFENSE).
- Rejected: failing the build automatically on every plugin finding, because the maintainers say the findings over-report; it wins for a rule whose precision a team has measured (inferred).

#### PIG-JS.VERIFICATION.FORMAT.1
- Positions: dedicated formatter (QUALITY-C12; SRC-298, T2, the ESLint steering committee); formatting by ESLint core rules is deprecated (QUALITY-C11; SRC-298, SRC-167). Biome and Prettier documents agree layout is a separate concern (12_dissent, topic 14).
- Forces: consistency and review time against one more tool.
- Decision: a dedicated formatter owns layout; lint rules do not.
- Rejected: layout through ESLint core rules, deprecated because the team could not sustain them; the `@stylistic` plugin keeps formatting in ESLint and is a listed alternative under FORMAT.3.

#### PIG-JS.VERIFICATION.FORMAT.2
- Positions: check mode in CI, `prettier --check` exits 0, 1, 2; a pre-commit hook reduces failures (QUALITY-C16; SRC-176).
- Forces: formatting enforced without a reviewer against occasional CI failures.
- Decision: CI runs the formatter in check mode; the pre-commit hook is the documented option, not a requirement (the source says "you may be interested").
- Rejected: CI that rewrites files (write mode), because a gate that mutates its input checks nothing; wins for a bot that commits formatting by design (inferred).

#### PIG-JS.VERIFICATION.TESTS.2
- Positions: `node:assert/strict`; legacy `equal` and `deepEqual` compare with `==` (QUALITY-C25; SRC-171).
- Forces: no false pass against a one-line import change.
- Decision: import `node:assert/strict` in tests.
- Rejected: legacy mode, which can pass unequal values; folklore "assert.deepEqual is a safe equality check" refuted (12_dissent). It wins only where a test intends loose equality, to be stated.

#### PIG-JS.VERIFICATION.TESTS.3
- Positions: wait on a condition (54% of Async Wait flakes fixed with waitFor; QUALITY-C34; SRC-296) and Playwright's web-first assertions retry until true (SRC-175, tool fact).
- Forces: stable result against a possibly longer failing wait.
- Decision: condition waits, never fixed delays.
- Rejected: fixed sleeps, the largest flake category in the study (45% Async Wait, QUALITY-C33); wins never as a default. The study is Java-dominated; transfer is inferred.

#### PIG-JS.VERIFICATION.LINT.4
- Positions: ESLint with typescript-eslint, which has documented type-aware rules (no-floating-promises, SRC-181), a security plugin (SRC-164), flat config, recommended baselines and the rule documents other branches cite (SRC-166, SRC-167, SRC-054); Biome as one tool for lint and format whose type-aware rules run only when its scanner is enabled and whose unsafe fixes need manual review (SRC-162, QUALITY-C17). No source compares them.
- Forces: automation needs binding, scriptable findings (exit codes, max-warnings, unused-suppression reports, all documented for ESLint) and type-aware checks; Biome offers fewer moving parts. DEPENDENCIES' trust purpose: one tool is fewer packages, but ESLint's plugins are opt-in and pinned.
- Decision: ESLint with typescript-eslint. Basis is judgment on tool facts against the branch purpose; the documents ground the facts, not a preference (gate G5). Rows 020 to 029 are the grounds.
- Rejected: Biome. Wins when the project wants one tool and one dependency for lint and format and the rule set it ships covers the needed rules (type-aware rules, security leads, hand-reviewed unsafe fixes) without ESLint plugins (inferred).

#### PIG-JS.VERIFICATION.FORMAT.3
- Positions: Prettier (SRC-177, SRC-178, SRC-176, named first by SRC-298); dprint and @stylistic (named by SRC-298 only, no tool facts admitted); Biome formatter (SRC-162).
- Forces: a formatter that only prints cannot change meaning (SRC-178); its check mode has documented exit codes 0, 1, 2 (SRC-176); the integration with ESLint is documented (eslint-config-prettier, run apart). Biome would fold formatting into LINT.4's rejected tool.
- Decision: Prettier, run separately from ESLint, with eslint-config-prettier, checked in CI (FORMAT.2). Basis is judgment on facts, not a claim that Prettier's style is better.
- Rejected: Biome formatter, wins when Biome is the linter. @stylistic, wins when a team insists on a single lint pipeline and accepts the maintenance cost the ESLint team described (SRC-298). dprint, wins when an admitted source gives its behaviour and check mode; none does today.

#### PIG-JS.VERIFICATION.TESTS.1
- Positions: node:test, built in, stable from Node v20.0.0, exit code 1 on failure, coverage experimental (QUALITY-C24, SRC-172); Vitest, needs Vite 6.4+ and Node 22.12+, watch mode by default, V8 and Istanbul coverage (QUALITY-C26, C27, SRC-183, SRC-182); Jest, needs Babel or ts-jest to run TypeScript (QUALITY-C28, SRC-170).
- Forces: no extra dependency in the trust chain (DEPENDENCIES), CI-friendly exit status and no watch default, against stable coverage tooling and richer features elsewhere.
- Decision: node:test. Do not gate on its experimental coverage flag (consistent with D1: coverage is not a gate anyway).
- Rejected: Vitest, wins when the project already builds with Vite or needs stable coverage providers or its watch workflow. Jest, wins when a large existing Jest suite and its transforms are in place (migration cost, inferred).

### RUNTIME

Each record: positions, forces, decision, rejected with the condition under which each would
win. Positions marked "implicit" have no admitted source; they are the unstated alternative
and carry no claim id.

#### PIG-JS.RUNTIME.MEASURE.1

| element | content |
|---|---|
| Positions | (a) profile the running application first, then change code (RUNTIME-C20, SRC-195 T1); (b) implicit: change code from reading it. |
| Forces | (a) predictability of the outcome, cost of one profiling run; (b) no setup cost, risk of fixing the wrong place. |
| Decision | (a). The docs example shows the wrong place: the hot spot was a synchronous hash, not the code that looked slow. Figures are illustration only. |
| Rejected | (b): wins when the change is not a speed or memory change, for example a correctness fix. |

#### PIG-JS.RUNTIME.MEASURE.2

| element | content |
|---|---|
| Positions | (a) measurement first; engine tuning only on a measured cost (RUNTIME-C55 SRC-302 T2, RUNTIME-C63); (b) avoid the engine cost on mechanism, without measuring (STRUCT-C42 SRC-083 T1, STRUCT-C43 SRC-088 T1, both MDN, no figures; RUNTIME-C56 SRC-303 T2 mechanism only). |
| Forces | (a) serves measured behaviour, costs one measurement per candidate change; (b) cheap to apply, but V8 itself says the holey versus packed gap is usually unmeasurable and no T1 specifies engine performance. |
| Decision | (a), the max rule for measured behaviour: no engine-level restructuring without a measurement of the real workload. (b) is kept as acceptable-when. |
| Rejected | (b) on mechanism alone: wins when a profile shows closure creation or prototype deoptimisation on a hot path. Holey-array avoidance: wins only under a measurement; the belief is restricted in 12_dissent. |

#### PIG-JS.RUNTIME.MEASURE.3

| element | content |
|---|---|
| Positions | (a) callback file APIs where maximal time and memory-allocation performance is required, promises otherwise (RUNTIME-C16, SRC-188 T1); (b) implicit: callbacks everywhere for speed. |
| Forces | (a) keeps the promise style that CONTROL favours, pays only on a need; (b) lowest overhead, loses the shared async style. |
| Decision | (a), with the need established by measurement (the measurement gate is inferred from the branch rule; the docs say "when maximal performance is required"). |
| Rejected | (b): wins when a measurement of a file-heavy hot path shows the promise overhead matters. |

#### PIG-JS.RUNTIME.METHOD.1

| element | content |
|---|---|
| Positions | (a) many runs, significance test, two stars across many comparisons (RUNTIME-C58 SRC-304, SRC-307, SRC-305, three T2; RUNTIME-C59 SRC-304); (b) implicit: single timings. |
| Forces | (a) serves trust in a reported difference, costs runs; (b) fast, cannot separate signal from noise. |
| Decision | (a), with Node core's figures (30 runs, Welch t-test) as the concrete instance; the transfer of the principle from Java and C is inferred. |
| Rejected | (b): wins when the difference is orders of magnitude and a single run cannot plausibly be noise (not sourced, so recorded only as the condition). |

#### PIG-JS.RUNTIME.METHOD.2

| element | content |
|---|---|
| Positions | (a) isolation and performance mode (RUNTIME-C60, SRC-304 T2); (b) implicit: run on a shared machine at default scaling. |
| Forces | (a) removes frequency and neighbour noise at the cost of a dedicated machine; (b) convenient, adds noise. |
| Decision | (a). |
| Rejected | (b): wins when only a relative comparison on the same machine in the same session is needed and the noise is quantified by the significance test of METHOD.1. |

#### PIG-JS.RUNTIME.DIAGNOSE.1

| element | content |
|---|---|
| Positions | (a) record context, then choose the path by symptom (RUNTIME-C25, SRC-187 T1 Diagnostics Working Group guide); (b) implicit: start with a favourite tool. |
| Forces | (a) makes the investigation reproducible and routes memory to heap tools and latency to CPU tools; (b) saves the recording step. |
| Decision | (a). |
| Rejected | (b): wins for a problem reproduced in seconds on a developer machine. |

#### PIG-JS.RUNTIME.DIAGNOSE.2

| element | content |
|---|---|
| Positions | (a) measure with eventLoopUtilization and monitorEventLoopDelay, remove observers when done (RUNTIME-C23, C24, SRC-194 T1); (b) implicit: infer blocking from response times or from reading code. |
| Forces | (a) direct measure of the event loop at low, bounded overhead; (b) no instrumentation, guesses. |
| Decision | (a), grounded by the scheduling mechanism (RUNTIME-C19, SRC-080 mechanism only). |
| Rejected | (b): wins never as evidence; it is only the trigger for taking the measurement. |

#### PIG-JS.RUNTIME.DIAGNOSE.3

| element | content |
|---|---|
| Positions | (a) built-in --cpu-prof and --heap-prof (RUNTIME-C21, SRC-079, SRC-191 T1); (b) perf flame graphs through --perf-basic-prof (RUNTIME-C22, SRC-189 T1 restricted); (c) implicit: third-party profilers. |
| Forces | (a) no install, stable flags, V8-level frames; (b) native frames, extra flags and tooling; (c) features, new dependency in a process that runs with your privileges. |
| Decision | (a), the most demanding in dependencies: none added. |
| Rejected | (b): wins when native-level frames are wanted beyond V8 profiles (inferred). (c): wins when a needed view is absent from the built-in profilers (no admitted source names one). |

#### PIG-JS.RUNTIME.MEMORY.1

| element | content |
|---|---|
| Positions | (a) classify first: running out of memory versus inefficient use, then pick heap profiler, snapshot or GC traces (RUNTIME-C26, SRC-192 T1); (b) implicit: take a snapshot at once. |
| Forces | (a) picks the cheapest sufficient tool; (b) heavy capture before knowing the question. |
| Decision | (a). |
| Rejected | (b): wins when the process may crash harmlessly and the leak is already evident. |

#### PIG-JS.RUNTIME.MEMORY.2

| element | content |
|---|---|
| Positions | (a) read cheap signals first: listener warning, GC trace pattern (RUNTIME-C30 SRC-081, RUNTIME-C47 SRC-198, both T1); (b) raise the listener limit to silence the warning (the position C30 warns against). |
| Forces | (a) cheap and often decisive; (b) removes noise and hides a probable leak. |
| Decision | (a); raising the limit only for a justified fan-out. |
| Rejected | (b): wins when the fan-out is designed and its bound is known. |

#### PIG-JS.RUNTIME.MEMORY.3

| element | content |
|---|---|
| Positions | (a) two snapshots around the suspect path, compare, follow retainers (RUNTIME-C45, SRC-201 T1). |
| Forces | Isolates growth between two points at the cost of two stop-the-world snapshots. |
| Decision | (a); no competing admitted position. |
| Rejected | none in the evidence. |

#### PIG-JS.RUNTIME.MEMORY.4

| element | content |
|---|---|
| Positions | (a) sampling heap profiler in production, snapshots only where a crash is harmless, trigger never public (RUNTIME-C44 SRC-201, SRC-202; RUNTIME-C46 SRC-200, all T1); (b) near-heap-limit capture (RUNTIME-C50, SRC-079, SRC-202 T1); (c) belief that snapshots are infeasible on large heaps (RUNTIME-C57 SRC-306 T2, restricted belief). |
| Forces | (a) low overhead, availability protected, attack surface closed; (b) automatic capture at the moment of interest; (c) false since V8 fixes. |
| Decision | (a), the most demanding on availability and exposure. |
| Rejected | (b): wins when a snapshot is wanted at that moment. (c): wins on older V8 than 11.5.130. |

#### PIG-JS.RUNTIME.MEMORY.5

| element | content |
|---|---|
| Positions | (a) WeakMap or WeakSet for object-keyed metadata, avoid WeakRef and FinalizationRegistry, allocUnsafeSlow for long-retained chunks (RUNTIME-C29, C28 SRC-193, SRC-203; RUNTIME-C14 SRC-185; all T1); (b) use WeakRef and FinalizationRegistry for cleanup. |
| Forces | (a) deterministic release, independent of collection timing; (b) convenience, behaviour differs between engines and a callback may never run. |
| Decision | (a), the most demanding: the non-deterministic features are avoided. |
| Rejected | (b): wins when no deterministic release exists and a missed cleanup is harmless. |

#### PIG-JS.RUNTIME.MEMORY.6

| element | content |
|---|---|
| Positions | (a) read heap_size_limit, change --max-old-space-size only for a measured need (RUNTIME-C48 SRC-199, SRC-202, SRC-079 T1); (b) call global.gc() as a leak remedy (RUNTIME-C49 SRC-199 T1, rejected there); (c) hand-tune around GC behaviour (RUNTIME-C54 SRC-301 T2: marking is concurrent since Node 10). |
| Forces | (a) avoids unmeasured limits; (b) can hurt performance and does not fix retention; (c) the engine already does the work. |
| Decision | (a), no manual collection. |
| Rejected | (b) wins never as a leak remedy. (c) wins when a GC trace shows starvation (time between GCs below time in GC) and a measurement ties it to the setting. |

