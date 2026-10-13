# Result: JavaScript philosophy graph cut to what is core to JavaScript, the rest packaged for the software development guideline

## L1 headline

The philosophy graph went from 108 to 52 nodes: 43 KEEP, 56 SEND, 9 SPLIT. Sent: all language-general principles (boundary parsing and call shape, structure hiding, purity, direction, naming and paradigm, the injection family and secrets, dependency sourcing, updates and publishing, the whole verification branch, measurement method). Kept: the permissive-language subset, the erased type layer, the promise and event-loop model, DOM, origin, prototype and process threats, the npm graph as attack surface, and the collector's memory model. The root and the eight branch nodes stay; nine branch or container nodes were narrowed and their general part is in the package. No claim was dropped, both graphs rebuilt and validate clean (certainty: the counts and gates are grounded; each verdict is inferred by the rule from claim levels and intents, with borderline calls open for the maintainer, listed in L2).

Pinned (grounded, counted by script or by the gates):
- Verdicts over the 108 philosophy nodes: KEEP 43, SEND 56, SPLIT 9.
- Philosophy node count after: 52 (108 before; the defaults graph stays at 287).
- Claims re-homed as `deferred`: 70 claim ids in 69 ledger rows (69 claims in 68 rows from the 56 sent nodes, plus 1 claim in 1 row from the general part of the split node `DEFENSE.HOST.3`); 2 of the 69 rows are claim-less (rejected beliefs). All 700 claims are still placed exactly once, 0 dropped.
- Links: inside the philosophy graph 35 removed (13 remain: 9 within branches, 4 across); inter links from the defaults graph 4 retargeted, 49 removed and planned as links to the software development guideline (62 of 111 remain); inter links to the Python philosophy 13 moved to the package (10 remain); 1 planned boundary link to the web-architecture guideline moved with its node (12 remain).
- Validate, js-philosophy: `nodes: 52  links: 13  inter_links: 10  issues: 0  errors: 0  warnings: 0`.
- Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 62  issues: 0  errors: 0  warnings: 0`.
- `python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 79, 'decision': 367, 'fact': 161, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 339
```
- `python3 build/assemble/check_complete.py`:
```
{
 "js-philosophy": {
  "nodes": 52,
  "intra": 13,
  "inter": 10,
  "ledger_rows": 121,
  "claims_in_pointers": 118,
  "impl_pointers": 118,
  "constraints": 21
 },
 "pig-js-defaults": {
  "nodes": 287,
  "intra": 162,
  "inter": 62,
  "ledger_rows": 578,
  "claims_in_pointers": 582,
  "impl_pointers": 582,
  "constraints": 381
 }
}
FAILS: 0
```

## L2 claims

- **Rule applied (grounded in the brief).** KEEP if the node follows from JavaScript's semantics, runtime, ecosystem or threat surface; SEND if it holds unchanged for any language; SPLIT if both. Evidence read: the claim `level` column (126 `js-principle`, 56 `principle`, 76 `decision`, 442 `practice` over the 700 claims), the node's intent, and the maintainer's three KEEP examples (a permissive language narrowed to a checked subset, a runtime shared with untrusted code, an npm graph that is part of the attack surface). Grounded as procedure; each application is inferred.
- **KEEP, 43 nodes (inferred).** The subset (`VISIBLE`, `FAILURE`, `BINDING`, `MATURITY`), the erased type layer (`STATIC`, `.1`, `.2`), the promise and event-loop model (`FAILURE`, `BOUNDS`, `SCHEDULING`, `FLOW`), exported state as shared state (`STATE.2`), DOM, origin, prototype and process-under-hostile-input threats, the npm graph (trust, threats, maintenance and install behaviour, evidence, lockfile and pin policy and review), the memory model, plus the root and `SUBSET`, `CONTROL`.
- **SEND, 56 nodes (inferred; claim level `principle` or neutral practice).** `SUBSET.NUMBERS`, `SUBSET.STATE`; `CONTRACTS.BOUNDARY` (+4), `CONTRACTS.SHAPE`; `CONTROL.LIFECYCLE`; `STRUCTURE.HIDING` (+3), `.STATE.1`, `.PURITY`, `.DIRECTION` (+2), `.NAMING` (+3), `.PARADIGM`; `DEFENSE.INJECTION` (+6), `DEFENSE.SECRETS`; `DEPENDENCIES.TRUST.3`, `.ADMISSION.1`, `.ADMISSION.3`, `.ADMISSION.4`, `.CHANGE.4`, `.CHANGE.5`, `.PUBLISH`; `VERIFICATION` branch (16 nodes); `RUNTIME.MEASURE`, `RUNTIME.METHOD`.
- **SPLIT, 9 nodes (inferred).** Eight branch nodes or containers whose intent mixed both and a leaf with mixed claims: `CONTRACTS`, `STRUCTURE`, `STRUCTURE.STATE`, `DEFENSE`, `DEFENSE.HOST.3`, `DEPENDENCIES`, `DEPENDENCIES.ADMISSION`, `VERIFICATION`, `RUNTIME`. Each keeps a narrowed JavaScript part (new wording flagged `unvalidated: intent narrowed at the split` in `epistemic_state`) and its general part is in Part B of the package. `VERIFICATION` stays as a leaf: its only JavaScript residue is that the checked subset and the type layer hold only while a tool checks them at the merge (inferred from two link sentences that were removed).
- **Claims (grounded).** The ledger rows of sent nodes moved to a `deferred` row on the nearest kept ancestor, statement prefixed "Owned by the software development guideline:"; the general part of `DEFENSE.HOST.3` (the CR, LF and NUL rule) is a deferred row on that node. Receivers: `VERIFICATION` 20 rows, `DEFENSE` 18, `STRUCTURE` 10, `CONTRACTS` 6, `DEPENDENCIES.CHANGE` 4, `DEPENDENCIES.ADMISSION` 3, `SUBSET` 2, `RUNTIME` 2, and 1 each on `STRUCTURE.STATE`, `DEFENSE.HOST.3`, `DEPENDENCIES.TRUST`, `DEPENDENCIES`.
- **Links (grounded as counts, inferred as to whether a sentence still holds).** Retargeted to the nearest kept ancestor: 4 (`PIG-JS.CONTROL.PROCESS` to `CONTROL`; `PIG-JS.VERIFICATION.LINT.2`, `PIG-JS.VERIFICATION.LINT.1.2` and `PIG-JS.DEPENDENCIES.SCREEN.1` to `VERIFICATION`). Removed because the sentence names the principle that left: 49, each listed as a planned link to the software guideline in `intent_graphs/README.md` section 3 and in the package. Removed from inside the philosophy graph: 35 (the package lists them, including the bridge between erased types and boundary validation).
- **Package (grounded).** `package.md` has 56 whole nodes in Part A and 9 general parts in Part B, each with intent, constraints, design notes, epistemic state, claims with source tier, verdict and restriction, the defaults rules that relied on it with their fate, and its Python links; 82 sources are listed at its end.
- **Open for the maintainer (inferred calls where the opposite is defensible).**
  - The injection family and secrets (`DEFENSE.INJECTION`, `DEFENSE.SECRETS`) were sent as language-general; the opposite view keeps them because the threat surface is Node. Largest single call (8 nodes, 18 rows).
  - `CONTRACTS.BOUNDARY` sent: the JavaScript bridge (erased types make the boundary parse the only run-time attestation) now lives only in `CONTRACTS.STATIC.1`, its links to the boundary nodes were removed.
  - `STRUCTURE.PURITY` sent (hoisting, run-once and tree-shaking facts stay in the defaults); `DEFENSE.HOST.2` and `RUNTIME.MEMORY.*` kept on their `js-principle` claim level though other languages share the mechanism.
  - Dependencies: `TRUST.1`, `CHANGE.1` to `.3` kept on npm-specific grounds; `PUBLISH` and `CHANGE.4` and `.5` sent as registry-neutral.
- **Side findings (grounded).** Before the rebuild `ig-tool validate` reported 1 error on the committed defaults graph (`PIG-JS.DEFENSE` present but ancestor `PIG-JS.ROOT` missing); the rebuild cleared it. The generated Obsidian vault was re-exported and its 67 stale philosophy files deleted. `decisions_for_review.md` and the research folders were not touched.

Pinned (grounded, counted by script or by the gates):
- Verdicts over the 108 philosophy nodes: KEEP 43, SEND 56, SPLIT 9.
- Philosophy node count after: 52 (108 before; the defaults graph stays at 287).
- Claims re-homed as `deferred`: 70 claim ids in 69 ledger rows (69 claims in 68 rows from the 56 sent nodes, plus 1 claim in 1 row from the general part of the split node `DEFENSE.HOST.3`); 2 of the 69 rows are claim-less (rejected beliefs). All 700 claims are still placed exactly once, 0 dropped.
- Links: inside the philosophy graph 35 removed (13 remain: 9 within branches, 4 across); inter links from the defaults graph 4 retargeted, 49 removed and planned as links to the software development guideline (62 of 111 remain); inter links to the Python philosophy 13 moved to the package (10 remain); 1 planned boundary link to the web-architecture guideline moved with its node (12 remain).
- Validate, js-philosophy: `nodes: 52  links: 13  inter_links: 10  issues: 0  errors: 0  warnings: 0`.
- Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 62  issues: 0  errors: 0  warnings: 0`.
- `python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 79, 'decision': 367, 'fact': 161, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 339
```
- `python3 build/assemble/check_complete.py`:
```
{
 "js-philosophy": {
  "nodes": 52,
  "intra": 13,
  "inter": 10,
  "ledger_rows": 121,
  "claims_in_pointers": 118,
  "impl_pointers": 118,
  "constraints": 21
 },
 "pig-js-defaults": {
  "nodes": 287,
  "intra": 162,
  "inter": 62,
  "ledger_rows": 578,
  "claims_in_pointers": 582,
  "impl_pointers": 582,
  "constraints": 381
 }
}
FAILS: 0
```

## L3 full

### Verdict table, all 108 philosophy nodes (inferred by the rule; reasons name the evidence)

KEEP stays whole. SEND leaves whole, with its descendants. SPLIT stays narrowed, its general part leaves. A node with any KEEP descendant stays.

| # | uid | name | verdict | reason |
|---|---|---|---|---|
| 1 | `ROOT` | Solid JavaScript | KEEP | Shared cut: root stays; intent already states the JavaScript stance (permissive language narrowed to a checked subset). |
| 2 | `SUBSET` | Predictable subset | KEEP | Shared cut (L1): the checked subset of a permissive language is the maintainer's own KEEP example; intent holds for the surviving children. |
| 3 | `SUBSET.VISIBLE` | Visible conversion | KEEP | Follows from JavaScript semantics: the coercion table of a permissive language. |
| 4 | `SUBSET.FAILURE` | Loud failure | KEEP | Follows from JavaScript semantics: strict mode is a language variant that turns silent failures into errors. |
| 5 | `SUBSET.NUMBERS` | Stated numeric limits | SEND | Holds unchanged for any language with binary floating point (claim level: principle, Goldberg); the JavaScript limits live in PIG-JS.SUBSET.NUMBERS. |
| 6 | `SUBSET.STATE` | Distinguished immutability | SEND | Immutability versus read-only restriction is a language-neutral taxonomy (claim level: principle); const and freeze facts live in the defaults. |
| 7 | `SUBSET.BINDING` | Enforced binding and access | KEEP | Follows from JavaScript semantics: fixed bindings by default, hash-private fields instead of underscore convention, implicit this. |
| 8 | `SUBSET.MATURITY` | Settled features | KEEP | Follows from JavaScript's evolution model and its alterable built-ins (settled features, untouched built-in objects). |
| 9 | `CONTRACTS` | Contracts | SPLIT | Shared cut (L1): the build-time type layer of a language without run-time types stays; boundary parsing and call shape go. |
| 10 | `CONTRACTS.STATIC` | Static contract | KEEP | Follows from JavaScript having no types at run time: the type layer is a separate build-time artefact. |
| 11 | `CONTRACTS.BOUNDARY` | Boundary contract | SEND | Parse every datum at a trust boundary holds unchanged for any language (OWASP input validation); the JavaScript bridge (erased types) stays on STATIC.1. |
| 12 | `CONTRACTS.SHAPE` | Shape of calls | SEND | Cap positional parameters: readability rule for any language (an ESLint default is the only ground). |
| 13 | `CONTRACTS.STATIC.1` | Types attest nothing at run time | KEEP | Follows from JavaScript semantics: types and assertions are erased before run time (claim level: js-principle). |
| 14 | `CONTRACTS.STATIC.2` | A passing check is evidence, not proof | KEEP | Follows from the checkers of JavaScript (TypeScript, Flow) being intentionally unsound; measured on JavaScript bugs (claim level: js-principle). |
| 15 | `CONTRACTS.BOUNDARY.1` | Validate at every trust boundary | SEND | Validate at every trust boundary: language-neutral (claim level: principle); server-side authority is architecture. |
| 16 | `CONTRACTS.BOUNDARY.2` | Accept by positive rule | SEND | Positive (allowlist) validation: language-neutral (claim level: principle). |
| 17 | `CONTRACTS.BOUNDARY.3` | Check meaning as well as form | SEND | Check meaning as well as form: language-neutral (claim level: principle). |
| 18 | `CONTRACTS.BOUNDARY.4` | Input handling is a recognizer | SEND | Input handling as a recognizer: language-neutral (claim level: principle). |
| 19 | `CONTROL` | Explicit control of time, failure and resources | KEEP | Shared cut (L1): the promise, event-loop and stream model is JavaScript's runtime; intent holds for the surviving children. |
| 20 | `CONTROL.FAILURE` | Failure has an owner | KEEP | Follows from JavaScript runtime semantics: two failure channels (throw, rejection or event) and host escalation of unobserved failures. |
| 21 | `CONTROL.BOUNDS` | Every wait and every task has a bound and a stopper | KEEP | Follows from JavaScript semantics: a promise has no cancellation protocol, so waits and tasks need an explicit stopper. |
| 22 | `CONTROL.SCHEDULING` | One shared cooperative thread | KEEP | Follows from the JavaScript runtime: one shared cooperative thread, microtask order, timers as lower bounds. |
| 23 | `CONTROL.FLOW` | Producers pace to consumers | KEEP | Follows from the Node and Web stream model: highWaterMark is a stop signal, not a memory bound (claims level: js-principle). |
| 24 | `CONTROL.LIFECYCLE` | Process end is designed | SEND | Designing the process end after an unrepairable failure (fail fast, external supervisor) holds unchanged for any language; the Node hooks live in PIG-JS.CONTROL.PROCESS. |
| 25 | `STRUCTURE` | Structure for locality of change | SPLIT | Shared cut (L1): only the exported-state part is JavaScript-specific; hiding, purity, direction, naming and paradigm go. |
| 26 | `STRUCTURE.HIDING` | Hide likely-to-change decisions | SEND | Information hiding by module boundary (Parnas) holds unchanged for any language. |
| 27 | `STRUCTURE.STATE` | State in one place | SPLIT | Keeps the JavaScript part (what a module exports is state shared by all importers); the general part (one place per piece of state) goes. |
| 28 | `STRUCTURE.PURITY` | Effect-free importing | SEND | Effect-free importing holds for any language with import-time execution; hoisting, run-once and tree-shaking facts live in PIG-JS.STRUCTURE.LOADING. |
| 29 | `STRUCTURE.DIRECTION` | Dependencies flow one way | SEND | One-way dependencies between modules: language-neutral. |
| 30 | `STRUCTURE.NAMING` | Names carry the concept | SEND | Names carry the concept: language-neutral (experiments on C# and others). |
| 31 | `STRUCTURE.PARADIGM` | Paradigm by intent | SEND | Paradigm by intent: language-neutral; the defect-rate studies compare languages, not JavaScript. |
| 32 | `STRUCTURE.HIDING.1` | Decompose by hidden decisions | SEND | Decompose by hidden decisions (Parnas): language-neutral (claim level: principle). |
| 33 | `STRUCTURE.HIDING.2` | Abstract data type versus object | SEND | Abstract data type versus object (Cook): language-neutral (claim level: principle). |
| 34 | `STRUCTURE.HIDING.3` | Minimal public surface | SEND | Minimal public surface: language-neutral principle; the three JavaScript exposure levels live in PIG-JS.STRUCTURE.SURFACE and .PACKAGE. |
| 35 | `STRUCTURE.STATE.1` | One place per piece of state | SEND | One place per piece of state (Codd): language-neutral (claim level: principle). |
| 36 | `STRUCTURE.STATE.2` | Exported state is shared state | KEEP | Follows from JavaScript module semantics: importers cannot rebind an export but can mutate it (claim level: js-principle). |
| 37 | `STRUCTURE.DIRECTION.1` | No cycles between modules | SEND | No cycles between modules: language-neutral (no own claim; Node CommonJS conflict note stays in the defaults). |
| 38 | `STRUCTURE.DIRECTION.2` | Declared layering | SEND | Declared layering: language-neutral and undecided (no admitted ground). |
| 39 | `STRUCTURE.NAMING.1` | Whole words | SEND | Whole words: language-neutral (experiment on C# developers). |
| 40 | `STRUCTURE.NAMING.2` | One concept one word | SEND | One concept one word: language-neutral (holder positions of style guides). |
| 41 | `STRUCTURE.NAMING.3` | Name from the concept | SEND | Name from the concept: language-neutral (naming experiments). |
| 42 | `DEFENSE` | Defense | SPLIT | Shared cut (L1): the page, origin, prototype and process parts follow from JavaScript's runtime; the injection family and secrets go. |
| 43 | `DEFENSE.DOM` | Hostile data in the document | KEEP | Follows from the browser runtime: hostile data reaching markup, script or navigation in the page. |
| 44 | `DEFENSE.ORIGIN` | Boundaries between origins | KEEP | A runtime shared with untrusted code: every script in a page holds the page's authority (the maintainer's own KEEP example). |
| 45 | `DEFENSE.INJECTION` | Data becoming instruction or location | SEND | Data becoming code, command, query, path, destination or serialized object: injection classes hold unchanged for any language. |
| 46 | `DEFENSE.PROTOTYPE` | Hostile keys and the shared object model | KEEP | Follows from JavaScript's object model: a hostile key rewrites what every object inherits. |
| 47 | `DEFENSE.SECRETS` | Secrets and cryptographic primitives | SEND | Secrets never committed, audited primitives, token verification on the recipient's terms: hold unchanged for any language. |
| 48 | `DEFENSE.HOST` | The process under hostile input | KEEP | Follows from the single-threaded runtime: one hostile input can stall the process (claims level: js-principle). |
| 49 | `DEFENSE.DOM.1` | Sources and sinks | KEEP | DOM XSS is a flow from DOM sources to DOM sinks: a browser-runtime threat surface (claim stack: browser). |
| 50 | `DEFENSE.DOM.2` | A verdict holds only for its parse | KEEP | Follows from HTML parsing and the innerHTML round trip (mutation XSS; claim level: js-principle). |
| 51 | `DEFENSE.DOM.3` | Script tags are not the only way in | KEEP | Follows from HTML and DOM semantics: handlers and DOM clobbering need no script element (claim level: js-principle). |
| 52 | `DEFENSE.INJECTION.1` | Strings never become code | SEND | Never build code from strings: holds for any language with dynamic evaluation; the JavaScript sinks live in PIG-JS.DEFENSE.INJECTION.1. |
| 53 | `DEFENSE.INJECTION.2` | Commands are not built from input | SEND | No shell, no input-chosen programs: command injection holds for any language. |
| 54 | `DEFENSE.INJECTION.3` | Queries keep code and data apart | SEND | Parameterized queries: SQL and NoSQL injection hold for any language. |
| 55 | `DEFENSE.INJECTION.4` | Paths stay inside their base | SEND | Path containment: path traversal holds for any language. |
| 56 | `DEFENSE.INJECTION.5` | Serialized data carries no behaviour | SEND | Serialized data carries no behaviour, XML external entities off: hold for any language. |
| 57 | `DEFENSE.INJECTION.6` | Destinations are chosen by the server | SEND | Server-chosen destinations (SSRF): holds for any language. |
| 58 | `DEFENSE.PROTOTYPE.1` | The application answers for keys | KEEP | Follows from JavaScript's object model and Node's threat model: the application validates keys, the runtime does not. |
| 59 | `DEFENSE.PROTOTYPE.2` | Pollution can be code execution | KEEP | Follows from JavaScript's shared prototypes: pollution reaches gadgets in core APIs and can end in code execution. |
| 60 | `DEFENSE.HOST.1` | One request can stall the process | KEEP | Follows from the single shared thread: an uninterruptible regular-expression match stalls every client (claims level: js-principle). |
| 61 | `DEFENSE.HOST.2` | Heuristics are not proofs | KEEP | Follows from the backtracking regular-expression engine of JavaScript runtimes (claim level: js-principle; borderline, ReDoS also affects other engines). |
| 62 | `DEFENSE.HOST.3` | Two parsers must agree | SPLIT | Keeps the runtime's position (spec-consistent parsing is not its flaw, claim level: js-principle); the parser-differential and CR, LF, NUL rule (claim level: principle) goes. |
| 63 | `DEPENDENCIES` | Dependencies | SPLIT | Shared cut (L1): the npm graph as attack surface stays; sourcing hygiene, updates and publishing hardening go. |
| 64 | `DEPENDENCIES.TRUST` | Dependencies are trusted code | KEEP | Follows from the npm ecosystem: every package acts with the application's authority and the runtime offers no containment. |
| 65 | `DEPENDENCIES.THREATS` | How trust is lost | KEEP | Follows from the npm ecosystem: routes by which trusted packages turn hostile. |
| 66 | `DEPENDENCIES.ADMISSION` | Admission | SPLIT | Keeps maintenance and install-time behaviour (npm facts); need, identity and documentation checks are sourcing and go. |
| 67 | `DEPENDENCIES.EVIDENCE` | Evidence and its limits | KEEP | Follows from npm provenance, signatures and audit semantics. |
| 68 | `DEPENDENCIES.CHANGE` | Controlled change | KEEP | Follows from npm lockfile and manifest semantics; intent holds for the surviving children. |
| 69 | `DEPENDENCIES.PUBLISH` | Publishing | SEND | Hardening publishing accounts of any registry: language-neutral (two-factor authentication). |
| 70 | `DEPENDENCIES.TRUST.1` | Every dependency is trusted code | KEEP | The npm dependency graph is part of the attack surface (the maintainer's own KEEP example); grounds are npm studies and Node's threat model. |
| 71 | `DEPENDENCIES.TRUST.2` | No containment inside the process | KEEP | Follows from the Node runtime: no privilege boundary inside the process (claim level: js-principle). |
| 72 | `DEPENDENCIES.TRUST.3` | Layered controls | SEND | Layered controls (defence in depth, attack trees): language-neutral (claim level: principle). |
| 73 | `DEPENDENCIES.THREATS.1` | Takeover of maintainership | KEEP | Four npm incidents and expired-domain takeover of npm packages (claim level: js-principle for the study). |
| 74 | `DEPENDENCIES.THREATS.2` | Confusion is many mechanisms | KEEP | Package confusion mechanisms measured on npm (claim level: js-principle). |
| 75 | `DEPENDENCIES.ADMISSION.1` | Existing components first | SEND | Existing components first is sourcing (what to build versus take): owned by the software guideline. |
| 76 | `DEPENDENCIES.ADMISSION.2` | Maintenance as a signal | KEEP | Maintainer count and recency measured on npm; install scripts are an npm lifecycle risk. |
| 77 | `DEPENDENCIES.ADMISSION.3` | Identity of the package | SEND | Identity of a package (typosquatting, look-alike) is judging libraries: sourcing, any registry. |
| 78 | `DEPENDENCIES.ADMISSION.4` | Documentation examples are untrusted | SEND | Documentation examples are untrusted: holds for any language and ecosystem. |
| 79 | `DEPENDENCIES.EVIDENCE.1` | Provenance and signatures | KEEP | npm provenance and registry signatures state origin, not safety (claims level: js-principle). |
| 80 | `DEPENDENCIES.EVIDENCE.2` | Audit findings | KEEP | npm audit findings measured as mostly unreachable (claim level: js-principle). |
| 81 | `DEPENDENCIES.CHANGE.1` | Reproducible tree | KEEP | npm lockfile versus manifest, and lockfile semantics differing per manager (claims level: js-principle). |
| 82 | `DEPENDENCIES.CHANGE.2` | Pin policy | KEEP | npm semver ranges and transitive resolution decide the pin policy (contested decision on npm facts). |
| 83 | `DEPENDENCIES.CHANGE.3` | Lockfile review | KEEP | Lockfile poisoning through resolved URLs and integrity hashes is an npm lockfile attack vector. |
| 84 | `DEPENDENCIES.CHANGE.4` | Updates | SEND | Automated updates, security updates separated, cooldown tradeoff: language-neutral supply-chain practice. |
| 85 | `DEPENDENCIES.CHANGE.5` | Incident response | SEND | Incident response after a supply-chain compromise (lockfile, credentials, pins): language-neutral practice. |
| 86 | `VERIFICATION` | Verification | SPLIT | Shared cut (L1): only the tie between the checked subset, the type layer and the merge gate is JavaScript-specific; everything else goes. |
| 87 | `VERIFICATION.STATIC_BASELINE` | Static analysis baseline | SEND | Static analysis baseline: language-neutral (claims level: principle). |
| 88 | `VERIFICATION.TEST_SUITE` | Test suite | SEND | Test suite policy: language-neutral. |
| 89 | `VERIFICATION.FAULT_DETECTION` | Fault detection power | SEND | Fault detection power: language-neutral. |
| 90 | `VERIFICATION.TEST_STABILITY` | Test stability | SEND | Test stability: language-neutral (studies mostly of Java projects). |
| 91 | `VERIFICATION.ENFORCEMENT` | Enforcement at the merge | SEND | The merge gate must not be skippable: language-neutral (platform fact). |
| 92 | `VERIFICATION.STATIC_BASELINE.1` | Analysis switched on | SEND | Enable a linter or safe mode: language-neutral (OpenSSF criteria). |
| 93 | `VERIFICATION.STATIC_BASELINE.2` | Analysis beyond the compiler | SEND | Analysis beyond the compiler: language-neutral (OpenSSF criteria). |
| 94 | `VERIFICATION.STATIC_BASELINE.3` | Checks complement each other | SEND | Checks complement each other: language-neutral (2015 web measurement, OpenSSF). |
| 95 | `VERIFICATION.TEST_SUITE.1` | Tests for new functionality | SEND | Tests for new functionality: language-neutral (OpenSSF criteria). |
| 96 | `VERIFICATION.TEST_SUITE.2` | Coverage finds, it does not judge | SEND | Coverage finds, it does not judge: language-neutral (study of Java suites). |
| 97 | `VERIFICATION.TEST_SUITE.3` | Test design | SEND | Test design: language-neutral (Google testing guidance). |
| 98 | `VERIFICATION.FAULT_DETECTION.1` | Mutation testing | SEND | Mutation testing: language-neutral (claims level: principle, decision). |
| 99 | `VERIFICATION.FAULT_DETECTION.2` | Property-based testing | SEND | Property-based testing: language-neutral (QuickCheck authors). |
| 100 | `VERIFICATION.TEST_STABILITY.1` | New tests are probed | SEND | Probe new tests: language-neutral. |
| 101 | `VERIFICATION.TEST_STABILITY.2` | Shared state is cleaned | SEND | Clean shared state between tests: language-neutral. |
| 102 | `VERIFICATION.TEST_STABILITY.3` | Flake rate tracked | SEND | Track the flake rate: language-neutral (Google figures). |
| 103 | `RUNTIME` | Runtime behaviour | SPLIT | Shared cut (L1): the memory model of the collector stays; measurement before belief and method go. |
| 104 | `RUNTIME.MEASURE` | Measurement before belief | SEND | Measurement before belief: holds for any language and engine (claim level: principle). |
| 105 | `RUNTIME.METHOD` | Measurement method | SEND | Performance as a distribution: language-neutral (measurements on Java and C, transfer inferred). |
| 106 | `RUNTIME.MEMORY` | Memory model | KEEP | Follows from the garbage collector of JavaScript engines: reachability and generations decide leaks. |
| 107 | `RUNTIME.MEMORY.1` | Reachability decides leaks | KEEP | Reachability decides leaks, cycles alone are not leaks: the engine fact behind a JavaScript folklore (claim level: js-principle). |
| 108 | `RUNTIME.MEMORY.2` | Bounded long-lived state | KEEP | Long-lived state promoted to the costlier region of the engine's collector (claim level: js-principle). |

### Intents narrowed at the split (inferred; the wording is the build's)

- `CONTRACTS` (Contracts): new intent (inferred): Make intent checkable at build time through a type layer, while holding that the layer is a build-time artefact of a language that has no types at run time, so that what the checker passes says nothing about the data that arrives and is never taken as proof.
- `STRUCTURE` (Structure for locality of change): new intent (inferred): Organize code so that a change touches one place: what a module exports is state shared by every importer, because an importer cannot rebind it but can change it, so the sharing is made visible instead of left implicit.
- `STRUCTURE.STATE` (State in one place): new intent (inferred): Make shared state visible as shared: an exported object is state held by every importer.
- `DEFENSE` (Defense): new intent (inferred): Input from outside the trust boundary is hostile; JavaScript sharpens this because a permissive language shares one runtime with untrusted code: hostile data must not become live markup in the page, code and content from another origin stays behind explicit boundaries, a hostile key must not rewrite what every object inherits, and one hostile input must not exhaust the single-threaded process.
- `DEFENSE.HOST.3` (Two parsers must agree): new intent (inferred): Where a proxy and the runtime's own HTTP parser read the same bytes, the runtime does not count spec-consistent behaviour as its own flaw, so the defence against any disagreement belongs at both parsers.
- `DEPENDENCIES` (Dependencies): new intent (inferred): Third-party code runs with the application's full privileges, so each dependency is a trust decision: weighed against the routes by which trust is lost, vetted for maintenance and install-time behaviour before adoption, installed reproducibly, changed deliberately, and judged by evidence whose limits are known.
- `DEPENDENCIES.ADMISSION` (Admission): new intent (inferred): A package's maintenance and what it runs at install are weighed before it enters.
- `VERIFICATION` (Verification): new intent (inferred): Defects that people forget to look for are found by machines on every change, with a result that blocks the change: the checked subset and the type layer hold only while a tool checks them there.
- `RUNTIME` (Runtime behaviour): new intent (inferred): Code stays well behaved over time because its memory behaviour follows from what the collector can reach and from how long state lives, not from belief or folklore about references.

`STRUCTURE.STATE` was also renamed "Shared state is visible". The epistemic state of each narrowed node gained `unvalidated: intent narrowed at the split by the build, the general part is owned by the software development guideline` (on `STRUCTURE` it replaced the gap on the layering node that left).

### Claims re-homed (grounded)

69 ledger rows changed role to `deferred` and node to the nearest kept ancestor (row ids and claim ids unchanged), listed with their old node in `build/handoff/to_software_guideline/package.md` (one block per sent node). By old role: 52 decision, 10 fact, 4 rejected, 2 acceptable-when, 1 already deferred. Constraints of the philosophy graph fell from 75 to 21 because decision rows left; `impl_pointers` still cover all 118 philosophy claim ids (`check_complete`).

### Links

Retargeted defaults inter links (4, inferred that the sentence still holds):

- `PIG-JS.CONTROL.PROCESS` "Process lifecycle and handles": `js-philosophy:CONTROL.LIFECYCLE` to `js-philosophy:CONTROL` (refines): The process rules apply the designed end to Node hooks and handles.
- `PIG-JS.VERIFICATION.LINT.2` "Enforcement": `js-philosophy:VERIFICATION.ENFORCEMENT` to `js-philosophy:VERIFICATION` (refines): CI exit status is how a lint finding blocks the merge in JavaScript.
- `PIG-JS.VERIFICATION.LINT.1.2` "Baseline rule set": `js-philosophy:VERIFICATION.STATIC_BASELINE.1` to `js-philosophy:VERIFICATION` (refines): The recommended rule set is the switched-on analysis for JavaScript.
- `PIG-JS.DEPENDENCIES.SCREEN.1` "Scorecard as per-check evidence": `js-philosophy:VERIFICATION.ENFORCEMENT` to `js-philosophy:VERIFICATION` (requires): Scorecard checks (tests before merge, review, branch protection) overlap CI gates.

Removed defaults inter links, now planned links to the software development guideline (49):

- `PIG-JS.SUBSET.NUMBERS` to "Stated numeric limits" (was `SUBSET.NUMBERS`)
- `PIG-JS.SUBSET.MUTATION.1` to "Distinguished immutability" (was `SUBSET.STATE`)
- `PIG-JS.CONTRACTS.SIGNATURE` to "Shape of calls" (was `CONTRACTS.SHAPE`)
- `PIG-JS.CONTRACTS.BOUNDARY` to "Boundary contract" (was `CONTRACTS.BOUNDARY`)
- `PIG-JS.STRUCTURE.LOADING.1` to "Effect-free importing" (was `STRUCTURE.PURITY`)
- `PIG-JS.STRUCTURE.LOADING.5` to "Effect-free importing" (was `STRUCTURE.PURITY`)
- `PIG-JS.STRUCTURE.SURFACE.1` to "Minimal public surface" (was `STRUCTURE.HIDING.3`)
- `PIG-JS.STRUCTURE.SURFACE.2` to "Minimal public surface" (was `STRUCTURE.HIDING.3`)
- `PIG-JS.STRUCTURE.PACKAGE.1` to "Minimal public surface" (was `STRUCTURE.HIDING.3`)
- `PIG-JS.STRUCTURE.SURFACE.5` to "Abstract data type versus object" (was `STRUCTURE.HIDING.2`)
- `PIG-JS.STRUCTURE.DIRECTION.1` to "No cycles between modules" (was `STRUCTURE.DIRECTION.1`)
- `PIG-JS.STRUCTURE.DIRECTION.3` to "Declared layering" (was `STRUCTURE.DIRECTION.2`)
- `PIG-JS.DEFENSE.INJECTION` to "Data becoming instruction or location" (was `DEFENSE.INJECTION`)
- `PIG-JS.DEFENSE.SECRETS` to "Secrets and cryptographic primitives" (was `DEFENSE.SECRETS`)
- `PIG-JS.DEFENSE.INJECTION.1` to "Strings never become code" (was `DEFENSE.INJECTION.1`)
- `PIG-JS.DEFENSE.INJECTION.2` to "Commands are not built from input" (was `DEFENSE.INJECTION.2`)
- `PIG-JS.DEFENSE.INJECTION.3` to "Queries keep code and data apart" (was `DEFENSE.INJECTION.3`)
- `PIG-JS.DEFENSE.INJECTION.4` to "Paths stay inside their base" (was `DEFENSE.INJECTION.4`)
- `PIG-JS.DEFENSE.INJECTION.5` to "Serialized data carries no behaviour" (was `DEFENSE.INJECTION.5`)
- `PIG-JS.DEFENSE.INJECTION.6` to "Destinations are chosen by the server" (was `DEFENSE.INJECTION.6`)
- `PIG-JS.DEFENSE.SECRETS.5` to "Secrets and cryptographic primitives" (was `DEFENSE.SECRETS`)
- `PIG-JS.DEPENDENCIES.INSTALL.4` to "Identity of the package" (was `DEPENDENCIES.ADMISSION.3`)
- `PIG-JS.DEPENDENCIES.UPDATE.1` to "Updates" (was `DEPENDENCIES.CHANGE.4`)
- `PIG-JS.DEPENDENCIES.PUBLISH.1` to "Publishing" (was `DEPENDENCIES.PUBLISH`)
- `PIG-JS.DEPENDENCIES.PUBLISH.2` to "Publishing" (was `DEPENDENCIES.PUBLISH`)
- `PIG-JS.DEPENDENCIES.PUBLISH.3` to "Publishing" (was `DEPENDENCIES.PUBLISH`)
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` to "Existing components first" (was `DEPENDENCIES.ADMISSION.1`)
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1` to "Existing components first" (was `DEPENDENCIES.ADMISSION.1`)
- `PIG-JS.VERIFICATION.TESTS.3` to "New tests are probed" (was `VERIFICATION.TEST_STABILITY.1`)
- `PIG-JS.VERIFICATION.LINT.3` to "Checks complement each other" (was `VERIFICATION.STATIC_BASELINE.3`)
- `PIG-JS.RUNTIME.MEASURE.1` to "Measurement before belief" (was `RUNTIME.MEASURE`)
- `PIG-JS.RUNTIME.MEASURE.2` to "Measurement before belief" (was `RUNTIME.MEASURE`)
- `PIG-JS.RUNTIME.MEASURE.3` to "Measurement before belief" (was `RUNTIME.MEASURE`)
- `PIG-JS.RUNTIME.METHOD.1` to "Measurement method" (was `RUNTIME.METHOD`)
- `PIG-JS.RUNTIME.METHOD.2` to "Measurement method" (was `RUNTIME.METHOD`)
- `PIG-JS.RUNTIME.DIAGNOSE` to "Measurement before belief" (was `RUNTIME.MEASURE`)
- `PIG-JS.CONTROL.PROCESS.2` to "Process end is designed" (was `CONTROL.LIFECYCLE`)
- `PIG-JS.DEFENSE.SECRETS.2.1` to "Secrets and cryptographic primitives" (was `DEFENSE.SECRETS`)
- `PIG-JS.DEFENSE.SECRETS.2.2` to "Secrets and cryptographic primitives" (was `DEFENSE.SECRETS`)
- `PIG-JS.DEFENSE.INJECTION.1.3` to "Strings never become code" (was `DEFENSE.INJECTION.1`)
- `PIG-JS.DEFENSE.INJECTION.1.4` to "Strings never become code" (was `DEFENSE.INJECTION.1`)
- `PIG-JS.DEFENSE.INJECTION.4.5` to "Paths stay inside their base" (was `DEFENSE.INJECTION.4`)
- `PIG-JS.DEFENSE.INJECTION.4.6` to "Paths stay inside their base" (was `DEFENSE.INJECTION.4`)
- `PIG-JS.DEFENSE.INJECTION.5.4` to "Serialized data carries no behaviour" (was `DEFENSE.INJECTION.5`)
- `PIG-JS.DEFENSE.HOST.3.1` to "Two parsers must agree (general part)" (was `DEFENSE.HOST.3`)
- `PIG-JS.DEFENSE.HOST.3.2` to "Two parsers must agree (general part)" (was `DEFENSE.HOST.3`)
- `PIG-JS.DEFENSE.INJECTION.5.3` to "Serialized data carries no behaviour" (was `DEFENSE.INJECTION.5`)
- `PIG-JS.DEFENSE.INJECTION.6.4` to "Destinations are chosen by the server" (was `DEFENSE.INJECTION.6`)
- `PIG-JS.DEPENDENCIES.SCREEN.3` to "Identity of the package" (was `DEPENDENCIES.ADMISSION.3`)

Removed intentlinks inside the philosophy graph (35; sentences in the package):

- requires `SUBSET.STATE` to `SUBSET.FAILURE`
- requires `CONTRACTS.BOUNDARY.1` to `CONTRACTS.STATIC.1`
- refines `CONTRACTS.BOUNDARY.2` to `CONTRACTS.BOUNDARY.4`
- requires `CONTRACTS.STATIC.2` to `CONTRACTS.BOUNDARY.1`
- dataflow `CONTROL.FAILURE` to `CONTROL.LIFECYCLE`
- requires `STRUCTURE.HIDING.3` to `STRUCTURE.HIDING.1`
- requires `STRUCTURE.STATE.2` to `STRUCTURE.HIDING.3`
- refines `STRUCTURE.PURITY` to `STRUCTURE.DIRECTION.1`
- requires `STRUCTURE.PARADIGM` to `STRUCTURE.HIDING.2`
- requires `DEFENSE.INJECTION.5` to `DEFENSE.INJECTION.1`
- dataflow `DEFENSE.PROTOTYPE.2` to `DEFENSE.INJECTION.1`
- requires `DEPENDENCIES.TRUST.1` to `DEPENDENCIES.ADMISSION.1`
- requires `DEPENDENCIES.TRUST.2` to `DEPENDENCIES.TRUST.3`
- requires `DEPENDENCIES.THREATS.2` to `DEPENDENCIES.ADMISSION.3`
- dataflow `DEPENDENCIES.EVIDENCE.2` to `DEPENDENCIES.CHANGE.4`
- requires `DEPENDENCIES.CHANGE.5` to `DEPENDENCIES.CHANGE.1`
- requires `DEPENDENCIES.PUBLISH` to `DEPENDENCIES.THREATS.1`
- dataflow `DEPENDENCIES.EVIDENCE.1` to `DEPENDENCIES.ADMISSION.3`
- requires `VERIFICATION.STATIC_BASELINE` to `VERIFICATION.ENFORCEMENT`
- requires `VERIFICATION.TEST_SUITE` to `VERIFICATION.ENFORCEMENT`
- requires `VERIFICATION.TEST_SUITE` to `VERIFICATION.TEST_STABILITY`
- dataflow `VERIFICATION.FAULT_DETECTION.1` to `VERIFICATION.TEST_SUITE.2`
- requires `VERIFICATION.STATIC_BASELINE.3` to `VERIFICATION.TEST_SUITE.1`
- requires `RUNTIME.MEASURE` to `RUNTIME.METHOD`
- requires `SUBSET.VISIBLE` to `CONTRACTS.BOUNDARY`
- requires `DEFENSE` to `CONTRACTS.BOUNDARY.1`
- refines `DEFENSE.INJECTION` to `CONTRACTS.BOUNDARY.2`
- requires `CONTRACTS.STATIC.1` to `VERIFICATION.ENFORCEMENT`
- refines `CONTRACTS.SHAPE` to `STRUCTURE.NAMING`
- requires `STRUCTURE.STATE.2` to `SUBSET.STATE`
- requires `DEPENDENCIES.TRUST.1` to `DEFENSE.INJECTION`
- requires `DEPENDENCIES.ADMISSION.4` to `DEFENSE.DOM.1`
- requires `VERIFICATION.ENFORCEMENT` to `DEPENDENCIES.CHANGE.1`
- dataflow `SUBSET` to `VERIFICATION.STATIC_BASELINE.1`
- refines `CONTRACTS.STATIC.2` to `VERIFICATION.STATIC_BASELINE.3`

Inter links to the Python philosophy moved to the package (13; sentences in the package):

- `CONTRACTS.BOUNDARY` refines `python-kb-philosophy:DEFENSIVE`
- `CONTRACTS.SHAPE` refines `python-kb-philosophy:COMMUNICATION`
- `CONTROL.LIFECYCLE` refines `python-kb-philosophy:DEFENSIVE`
- `STRUCTURE.HIDING` refines `python-kb-philosophy:STRUCTURE`
- `STRUCTURE.STATE` refines `python-kb-philosophy:DATACENTRICITY`
- `STRUCTURE.NAMING` refines `python-kb-philosophy:COMMUNICATION`
- `STRUCTURE.PARADIGM` refines `python-kb-philosophy:POLYGLOT`
- `DEFENSE.INJECTION` refines `python-kb-philosophy:DEFENSIVE`
- `DEPENDENCIES.ADMISSION.1` refines `python-kb-philosophy:INTENTIONALITY`
- `VERIFICATION.STATIC_BASELINE` refines `python-kb-philosophy:DEFENSIVE`
- `VERIFICATION.TEST_STABILITY` refines `python-kb-philosophy:REPRODUCIBILITY`
- `RUNTIME.MEASURE` refines `python-kb-philosophy:INTENTIONALITY`
- `RUNTIME.METHOD` refines `python-kb-philosophy:REPRODUCIBILITY`

Planned boundary link moved with its node (1): `CONTRACTS.BOUNDARY.1` to `web-app-philosophy` (server-side validation authority). The remaining 12 are in `intent_graphs/README.md`.

### Files written (grounded)

- `build/distill/skeleton.md`, `build/distill/claims_ledger.md`: edited in place; `python3 build/assemble/apply_flags.py` printed `{} nodes changed: 0`.
- `intent_graphs/js_philosophy.ig.yaml`, `intent_graphs/js_defaults.ig.yaml`: rebuilt with `build_batches.py` and `build_graphs.sh`; `intent_graphs/README.md` updated (counts, section 3, planned links); `intent_graphs/obsidian_export/` re-exported, stale philosophy files deleted.
- `build/assemble/gen/`: regenerated by `build_batches.py` (the rebuild step requires it; no other file of `build/assemble/` changed). `integrate.py` was not run.
- `build/handoff/to_software_guideline/package.md`, `result.md`.
- Not run: commit, push.

### Gate outputs (grounded)

`python3 build/assemble/build_batches.py` ended with `"problems": []`, `"decision_nodes_without_record": []`, `"judge_records": 211`, `"planned": 12`, `"ledger_rows": 699`.

Validate, js-philosophy: `nodes: 52  links: 13  inter_links: 10  issues: 0  errors: 0  warnings: 0` (status ok, 0 errors).
Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 62  issues: 0  errors: 0  warnings: 0` (status ok, 0 errors).

`check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 79, 'decision': 367, 'fact': 161, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 339
```

`check_complete.py`:
```
{
 "js-philosophy": {
  "nodes": 52,
  "intra": 13,
  "inter": 10,
  "ledger_rows": 121,
  "claims_in_pointers": 118,
  "impl_pointers": 118,
  "constraints": 21
 },
 "pig-js-defaults": {
  "nodes": 287,
  "intra": 162,
  "inter": 62,
  "ledger_rows": 578,
  "claims_in_pointers": 582,
  "impl_pointers": 582,
  "constraints": 381
 }
}
FAILS: 0
```
