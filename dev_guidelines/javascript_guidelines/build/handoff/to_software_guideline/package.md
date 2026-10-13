# Package for the software development guideline: principles sent from the JavaScript guideline

This file is self-contained. It carries every principle that the JavaScript guideline's philosophy graph held and that
is not specific to JavaScript, with its grounds, so the software development guideline (or any other language guideline)
can take it up without reading the JavaScript guideline.

## How to read this package

- **Origin.** The JavaScript guideline keeps its principles in an IntentGraph named `js-philosophy` (108 nodes before the
  split, 52 after). Each node has a name, an intent (the why), constraints (rules, as MUST or MUST NOT sentences),
  design notes (facts, rejected beliefs, deferred items), an epistemic state, and claims. Node ids such as
  `STRUCTURE.HIDING.3` are given for traceability only.
- **Decision.** The maintainer decided: "if they are core to js , keep them, else, send them to the other session". Rule per
  node: KEEP if it follows from what JavaScript is (its semantics, runtime, ecosystem or threat surface); SEND if it holds
  unchanged for any language; SPLIT if both, the general part being in this package.
- **Two kinds of entry.** Part A: the 56 nodes that were sent whole. Part B: the 9 general parts carved out of nodes that
  stay in the JavaScript guideline in narrowed form.
- **Claims.** A claim is a statement grounded in sources. `level` is `principle` (holds for any language),
  `js-principle` (follows from JavaScript), `decision` (a choice with alternatives) or `practice` (a rule under a decision);
  `stack` is the area it was read in (language, browser, node, typescript, tooling). `agreement` is consensus, majority,
  contested or single-source among admitted sources; `certainty` is grounded (a named source states or shows it), inferred
  (follows from grounded claims) or open. Claim ids are stable names (for example `SRVSEC-C15`).
- **Sources.** Every source passed an admission audit: tier T1 (normative or primary: standards, official documentation,
  OWASP, OpenSSF), T2 (recognized authority: peer-reviewed research, named maintainers, large-organization style guides that
  state reasons), T3 (reputable practice). T4 (community) is never admitted. Verdict `admit` means the source may ground any
  claim it supports; `admit-restricted` means it may ground only what its restriction states (for example a vendor's
  facts about its own tool, or one guide's position, never evidence). The list of sources is at the end.
- **Epistemic state.** `known` means the node was decided on admitted sources; `| unvalidated: <why>` marks a rule that rests on
  single-source, inferred or open claims, or on a quote that was not obtained; `| conflict: <positions>` names a contested point;
  `| gap:` or `| missing:` names what no admitted source states; `risky` means decided on one weak source; `undecided` means no
  position was chosen. An epistemic state in a sent node describes the node as it was in the JavaScript guideline.
- **Placed as.** The role the claim had on its node: `decision` (a rule), `acceptable-when` (a rule that holds under a
  condition), `fact`, `rejected` (a belief the evidence refutes), `deferred` (owned elsewhere).
- **KEEP, SEND, SPLIT in link lines.** Where a line names a principle with a tag, the tag says what became of it in the split:
  KEEP stays in the JavaScript guideline, SEND is in this package whole, SPLIT stays there narrowed and its general part is in
  Part B.
- **Defaults nodes.** `pig-js-defaults` is the JavaScript guideline's rule graph (one concrete rule per node). "Relied on it"
  lists the rules whose link to the principle was removed or moved; their fate is stated. The software guideline may link to
  them, or hold the general rule that they render in JavaScript.
- **Python links.** `python-kb-philosophy` is the Python guideline's eight principles (DEFENSIVE, DATACENTRICITY, STRUCTURE,
  COMMUNICATION, POLYGLOT, REPRODUCIBILITY, INTENTIONALITY and a root); a link says that the JavaScript principle specialises
  that shared principle, which is the evidence that the principle is shared.

Counts: SEND 56 nodes (69 claims in 68 rows); SPLIT 9 nodes (general parts below; 1 claim in 1 row on the node that stays).

## Outline of what is sent

- `SUBSET` Predictable subset (kept)
  - `SUBSET.NUMBERS` Stated numeric limits (sent)
  - `SUBSET.STATE` Distinguished immutability (sent)
- `CONTRACTS` Contracts (split)
  - `CONTRACTS.BOUNDARY` Boundary contract (sent)
    - `CONTRACTS.BOUNDARY.1` Validate at every trust boundary (sent)
    - `CONTRACTS.BOUNDARY.2` Accept by positive rule (sent)
    - `CONTRACTS.BOUNDARY.3` Check meaning as well as form (sent)
    - `CONTRACTS.BOUNDARY.4` Input handling is a recognizer (sent)
  - `CONTRACTS.SHAPE` Shape of calls (sent)
- `CONTROL` Explicit control of time, failure and resources (kept)
  - `CONTROL.LIFECYCLE` Process end is designed (sent)
- `STRUCTURE` Structure for locality of change (split)
  - `STRUCTURE.HIDING` Hide likely-to-change decisions (sent)
    - `STRUCTURE.HIDING.1` Decompose by hidden decisions (sent)
    - `STRUCTURE.HIDING.2` Abstract data type versus object (sent)
    - `STRUCTURE.HIDING.3` Minimal public surface (sent)
  - `STRUCTURE.STATE` State in one place (split)
    - `STRUCTURE.STATE.1` One place per piece of state (sent)
  - `STRUCTURE.PURITY` Effect-free importing (sent)
  - `STRUCTURE.DIRECTION` Dependencies flow one way (sent)
    - `STRUCTURE.DIRECTION.1` No cycles between modules (sent)
    - `STRUCTURE.DIRECTION.2` Declared layering (sent)
  - `STRUCTURE.NAMING` Names carry the concept (sent)
    - `STRUCTURE.NAMING.1` Whole words (sent)
    - `STRUCTURE.NAMING.2` One concept one word (sent)
    - `STRUCTURE.NAMING.3` Name from the concept (sent)
  - `STRUCTURE.PARADIGM` Paradigm by intent (sent)
- `DEFENSE` Defense (split)
  - `DEFENSE.INJECTION` Data becoming instruction or location (sent)
    - `DEFENSE.INJECTION.1` Strings never become code (sent)
    - `DEFENSE.INJECTION.2` Commands are not built from input (sent)
    - `DEFENSE.INJECTION.3` Queries keep code and data apart (sent)
    - `DEFENSE.INJECTION.4` Paths stay inside their base (sent)
    - `DEFENSE.INJECTION.5` Serialized data carries no behaviour (sent)
    - `DEFENSE.INJECTION.6` Destinations are chosen by the server (sent)
  - `DEFENSE.SECRETS` Secrets and cryptographic primitives (sent)
  - `DEFENSE.HOST` The process under hostile input (kept)
    - `DEFENSE.HOST.3` Two parsers must agree (split)
- `DEPENDENCIES` Dependencies (split)
  - `DEPENDENCIES.TRUST` Dependencies are trusted code (kept)
    - `DEPENDENCIES.TRUST.3` Layered controls (sent)
  - `DEPENDENCIES.ADMISSION` Admission (split)
    - `DEPENDENCIES.ADMISSION.1` Existing components first (sent)
    - `DEPENDENCIES.ADMISSION.3` Identity of the package (sent)
    - `DEPENDENCIES.ADMISSION.4` Documentation examples are untrusted (sent)
  - `DEPENDENCIES.CHANGE` Controlled change (kept)
    - `DEPENDENCIES.CHANGE.4` Updates (sent)
    - `DEPENDENCIES.CHANGE.5` Incident response (sent)
  - `DEPENDENCIES.PUBLISH` Publishing (sent)
- `VERIFICATION` Verification (split)
  - `VERIFICATION.STATIC_BASELINE` Static analysis baseline (sent)
    - `VERIFICATION.STATIC_BASELINE.1` Analysis switched on (sent)
    - `VERIFICATION.STATIC_BASELINE.2` Analysis beyond the compiler (sent)
    - `VERIFICATION.STATIC_BASELINE.3` Checks complement each other (sent)
  - `VERIFICATION.TEST_SUITE` Test suite (sent)
    - `VERIFICATION.TEST_SUITE.1` Tests for new functionality (sent)
    - `VERIFICATION.TEST_SUITE.2` Coverage finds, it does not judge (sent)
    - `VERIFICATION.TEST_SUITE.3` Test design (sent)
  - `VERIFICATION.FAULT_DETECTION` Fault detection power (sent)
    - `VERIFICATION.FAULT_DETECTION.1` Mutation testing (sent)
    - `VERIFICATION.FAULT_DETECTION.2` Property-based testing (sent)
  - `VERIFICATION.TEST_STABILITY` Test stability (sent)
    - `VERIFICATION.TEST_STABILITY.1` New tests are probed (sent)
    - `VERIFICATION.TEST_STABILITY.2` Shared state is cleaned (sent)
    - `VERIFICATION.TEST_STABILITY.3` Flake rate tracked (sent)
  - `VERIFICATION.ENFORCEMENT` Enforcement at the merge (sent)
- `RUNTIME` Runtime behaviour (split)
  - `RUNTIME.MEASURE` Measurement before belief (sent)
  - `RUNTIME.METHOD` Measurement method (sent)

(Branches shown only where something is sent or split; kept nodes appear only as parents of those.)

## Part A: nodes sent whole

### Branch SUBSET: Predictable subset

#### Stated numeric limits

- Origin: node `SUBSET.NUMBERS`, child of `SUBSET` ("Predictable subset", KEEP). Verdict SEND: Holds unchanged for any language with binary floating point (claim level: principle, Goldberg); the JavaScript limits live in PIG-JS.SUBSET.NUMBERS.
- Intent: The precision and range of the numeric type decide which values may travel in it; values beyond them use an exact representation, and rounding is never papered over by an ad-hoc tolerance.
- Constraints: none (no decision row of its own).
- Design notes: 
  - Rejected [single-source]: Reject a fixed tolerance as the general cure for float equality: choosing the tolerance is arbitrary and the relation differs-by-less-than-tolerance is not transitive (Goldberg).
- Epistemic state: known | unvalidated: single T2 source on the tolerance point; limits grounded in PIG-JS.SUBSET.NUMBERS

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| LANG-C29 | A fixed tolerance E is not a general cure for exact-equality problems with floats: choosing E is arbitrary and the relation 'differs by less than E' is not transitive. | rejected (single-source) | principle, language | single-source, grounded | SRC-236 §Systems Aspects [T2, admit-restricted, restricted to: Floating-point mechanism (rounding error, NaN, signed zero, epsilon) from the 1991 paper; not the reprinter's added sections; no JavaScript-specific rule] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.SUBSET.NUMBERS` "Numbers with stated limits" (refines): Binary64 precision, the safe-integer range and BigInt are the concrete numeric limits. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Distinguished immutability

- Origin: node `SUBSET.STATE`, child of `SUBSET` ("Predictable subset", KEEP). Verdict SEND: Immutability versus read-only restriction is a language-neutral taxonomy (claim level: principle); const and freeze facts live in the defaults.
- Intent: Whether a value cannot change at all or may be changed only by some holders is a distinction the code states, and a language mechanism is chosen for the one it actually gives.
- Constraints: none (no decision row of its own).
- Design notes: 
  - Fact [single-source]: Separate immutability (nobody can change the state) from read-only restriction (only some clients may); the source is a taxonomy and shows no effect evidence, so no preference between them is derived.
- Epistemic state: known | unvalidated: single T2 source | gap: no admitted source states immutability as a design preference (G-M29)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C66 | Separate immutability (no one can change state) from read-only restriction (only some clients may); language support for both is long argued by practitioners, but this paper shows no effect evidence. | fact (single-source) | principle, language | single-source, grounded | SRC-253 §Abstract [T2, admit-restricted, restricted to: taxonomy of immutability and read-only mechanisms and expert-interview requirements (Java-oriented); no effect evidence; not a JS rule] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.SUBSET.MUTATION.1` "Shallow freeze" (refines): Object.freeze is the language mechanism whose reach (own keys only) must be known. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `SUBSET.FAILURE` "Loud failure" (KEEP): A lock on state protects only as far as a write to it fails loudly.
- requires from `STRUCTURE.STATE.2` "Exported state is shared state" (KEEP): Freezing is shallow and does not make nested data immutable; the freeze mechanics are owned by SUBSET (group freeze-shallow).

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch CONTRACTS: Contracts

#### Boundary contract

- Origin: node `CONTRACTS.BOUNDARY`, child of `CONTRACTS` ("Contracts", SPLIT). Verdict SEND: Parse every datum at a trust boundary holds unchanged for any language (OWASP input validation); the JavaScript bridge (erased types) stays on STATIC.1.
- Travels with: `CONTRACTS.BOUNDARY.1` (Validate at every trust boundary), `CONTRACTS.BOUNDARY.2` (Accept by positive rule), `CONTRACTS.BOUNDARY.3` (Check meaning as well as form), `CONTRACTS.BOUNDARY.4` (Input handling is a recognizer).
- Intent: Parse every datum that crosses a trust boundary into the shape the program expects before use, so that code past the boundary may rely on that shape
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.CONTRACTS.BOUNDARY` "Parse at the boundary" (refines): Parsing at the boundary realises the boundary contract Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `SUBSET.VISIBLE` "Visible conversion" (KEEP): What an expression does follows from the declared kind of its operands; for data from outside, that kind is established by parsing at the boundary.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:DEFENSIVE`: Validate at boundaries and trust after validation: the shared principle, here with the JavaScript-distinct fact that the language has no run-time types

#### Shape of calls

- Origin: node `CONTRACTS.SHAPE`, child of `CONTRACTS` ("Contracts", SPLIT). Verdict SEND: Cap positional parameters: readability rule for any language (an ESLint default is the only ground).
- Intent: A call carries its meaning by name and not by position, because argument order must otherwise be memorised by every reader and writer
- Constraints: 
  - MUST cap positional parameters: numerous parameters are hard to read and write because each parameter, its type and its order must be memorised (the rule default of 3 is a configuration default, not evidence)
- Design notes: none.
- Epistemic state: known | unvalidated: quote tool-extracted | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C47 | ESLint documents the reason to cap positional parameters: numerous parameters are hard to read and write because each parameter, its type and its order must be memorised. | decision (single-source) | practice, tooling | single-source, grounded | SRC-084 §Rule details [T1, admit-restricted, restricted to: rule behaviour and stated rationale (memorising order and types); the default of 3 is a configuration default, not evidence] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.CONTRACTS.SIGNATURE` "Function shapes" (refines): Declared signatures realise shape of calls Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- refines to `STRUCTURE.NAMING` "Names carry the concept" (SEND): Call shapes are the smallest unit of the interface design STRUCTURE governs

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:COMMUNICATION`: An interface is user experience: call sites that say what they mean

#### Validate at every trust boundary

- Origin: node `CONTRACTS.BOUNDARY.1`, child of `CONTRACTS.BOUNDARY` ("Boundary contract", SEND). Verdict SEND: Validate at every trust boundary: language-neutral (claim level: principle); server-side authority is architecture.
- Intent: All data crossing a trust boundary is validated before use, including data from internal services, queues and stored records; the server side is the authority
- Constraints: 
  - MUST validate all data crossing a trust boundary, including data from internal APIs, queues and stored records, before the application uses it
- Design notes: 
  - Deferred: Server-side validation as a trusted service layer, never client-side validation as a security control: the architecture half is owned by the web-architecture guideline
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| TYPES-C27 | Validate all data crossing a trust boundary, including from internal APIs, queues and stored records, before the application uses it. | decision (consensus) | principle, node | consensus, grounded | SRC-053 §Goals, Validate at boundaries [T1, admit-restricted, restricted to: unrestricted for 02_types; 06_runsec: Regex-safety statements only (bound length, non-backtracking engine or timeout, timeout as failure), each cross-checked against K20]; SRC-039 §2.2.1 [T1, admit, unrestricted] |
| TYPES-C29 | Enforce validation at a trusted service layer; never rely on client-side validation as a security control. | deferred (consensus) | principle, browser | consensus, grounded | SRC-039 §2.2.2 [T1, admit, unrestricted]; SRC-053 §Server-side validation [T1, admit-restricted, restricted to: unrestricted for 02_types; 06_runsec: Regex-safety statements only (bound length, non-backtracking engine or timeout, timeout as failure), each cross-checked against K20] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `CONTRACTS.STATIC.1` "Types attest nothing at run time" (KEEP): Because a type layer attests nothing about arriving data, the boundary check is what gives the types their truth
- requires from `CONTRACTS.STATIC.2` "A passing check is evidence, not proof" (KEEP): Since a passing check is not proof, run-time validation stays in place even in fully typed code
- requires from `DEFENSE` "Defense" (SPLIT): Treating every input as hostile in DEFENSE presupposes that inputs are parsed at the boundary here

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Accept by positive rule

- Origin: node `CONTRACTS.BOUNDARY.2`, child of `CONTRACTS.BOUNDARY` ("Boundary contract", SEND). Verdict SEND: Positive (allowlist) validation: language-neutral (claim level: principle).
- Intent: State what is valid and reject the rest, instead of enumerating what is bad
- Constraints: 
  - MUST use positive validation (allowlist of values, patterns, ranges, or comparison to an expected structure) rather than denylisting bad input
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| TYPES-C28 | Use positive validation (an allowlist of values, patterns and ranges, or comparison to an expected structure) rather than denylisting bad input. | decision (consensus) | principle, node | consensus, grounded | SRC-039 §2.2.1 [T1, admit, unrestricted]; SRC-053 §Allowlist [T1, admit-restricted, restricted to: unrestricted for 02_types; 06_runsec: Regex-safety statements only (bound length, non-backtracking engine or timeout, timeout as failure), each cross-checked against K20] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- refines to `CONTRACTS.BOUNDARY.4` "Input handling is a recognizer" (SEND): A positive rule is a recognizer for a simple input language; complex languages need a real parser, not a pattern list
- refines from `DEFENSE.INJECTION` "Data becoming instruction or location" (SEND): Positive validation is the language-neutral form of the allowlist stance DEFENSE takes toward sinks and injection

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Check meaning as well as form

- Origin: node `CONTRACTS.BOUNDARY.3`, child of `CONTRACTS.BOUNDARY` ("Boundary contract", SEND). Verdict SEND: Check meaning as well as form: language-neutral (claim level: principle).
- Intent: A well-formed value can still break a rule: related fields are checked together
- Constraints: 
  - MUST check syntax and semantics, including that combinations of related fields are reasonable (end date after start date)
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| TYPES-C33 | Check both syntax and semantics, including that combinations of related fields are reasonable (for example end date after start date). | decision (consensus) | principle, node | consensus, grounded | SRC-053 §Validation approach [T1, admit-restricted, restricted to: unrestricted for 02_types; 06_runsec: Regex-safety statements only (bound length, non-backtracking engine or timeout, timeout as failure), each cross-checked against K20]; SRC-039 §2.2.3 [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Input handling is a recognizer

- Origin: node `CONTRACTS.BOUNDARY.4`, child of `CONTRACTS.BOUNDARY` ("Boundary contract", SEND). Verdict SEND: Input handling as a recognizer: language-neutral (claim level: principle).
- Intent: Accept only what the input language defines, and keep that language simple enough to be recognized completely before anything is computed from it
- Constraints: 
  - MUST make input handling a recognizer of valid inputs and keep input languages simple; do not hand-write ad-hoc recognizers (regex allow or deny lists) for complex input languages, which are unreliable (Sassaman et al., position of a 2011 technical report).
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| TYPES-C48 | Sassaman et al. hold that a system's input handling acts as a recognizer of valid inputs, hand-written ad-hoc recognizers (regex allow or deny lists) are unreliable for complex input languages, and input languages should be kept simple. | decision (single-source) | principle, language | single-source, grounded | SRC-242 §Input handling, Principles of Secure Design [T2, admit-restricted, restricted to: The recognizer-before-processing principle as a mechanism and as the authors' position; not JavaScript-specific] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- refines from `CONTRACTS.BOUNDARY.2` "Accept by positive rule" (SEND): A positive rule is a recognizer for a simple input language; complex languages need a real parser, not a pattern list

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch CONTROL: Explicit control of time, failure and resources

#### Process end is designed

- Origin: node `CONTROL.LIFECYCLE`, child of `CONTROL` ("Explicit control of time, failure and resources", KEEP). Verdict SEND: Designing the process end after an unrepairable failure (fail fast, external supervisor) holds unchanged for any language; the Node hooks live in PIG-JS.CONTROL.PROCESS.
- Intent: After a failure the program cannot repair, its state is undefined: it records the failure, releases what it owns and ends, and restarting is the job of something outside it.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known | unvalidated: single T1 source; grounded by the merged row CONTROL-078 on PIG-JS.CONTROL.PROCESS.2 (P5 merge); rolls up PIG-JS.CONTROL.PROCESS

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.CONTROL.PROCESS` "Process lifecycle and handles" (refines): The process rules apply the designed end to Node hooks and handles. Fate: retargeted here to js-philosophy:CONTROL.
- `PIG-JS.CONTROL.PROCESS.2` "Uncaught exceptions" (refines): Node's uncaughtException and uncaughtExceptionMonitor hooks render the designed process end; the principle and its single evidence row (CONTROL-078) are held once. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- dataflow from `CONTROL.FAILURE` "Failure has an owner" (KEEP): A failure no owner can repair flows to the lifecycle, which decides how the process ends.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:DEFENSIVE`: Ending on an unrepairable failure is fail fast applied to the process.

### Branch STRUCTURE: Structure for locality of change

#### Hide likely-to-change decisions

- Origin: node `STRUCTURE.HIDING`, child of `STRUCTURE` ("Structure for locality of change", SPLIT). Verdict SEND: Information hiding by module boundary (Parnas) holds unchanged for any language.
- Travels with: `STRUCTURE.HIDING.1` (Decompose by hidden decisions), `STRUCTURE.HIDING.2` (Abstract data type versus object), `STRUCTURE.HIDING.3` (Minimal public surface).
- Intent: Put each difficult or likely-to-change decision behind one module boundary and expose as little of it as possible.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:STRUCTURE`: Information hiding is the module-level form of structure primacy.

#### Effect-free importing

- Origin: node `STRUCTURE.PURITY`, child of `STRUCTURE` ("Structure for locality of change", SPLIT). Verdict SEND: Effect-free importing holds for any language with import-time execution; hoisting, run-once and tree-shaking facts live in PIG-JS.STRUCTURE.LOADING.
- Intent: Make importing a module safe in any order by giving its top level no effect beyond defining its own exports.
- Constraints: 
  - MUST keep a module's top level free of effects other than initialising its own exports, so that importing it is safe in any order and unused code can be dropped by tools.
- Design notes: none.
- Epistemic state: known | unvalidated: practice inferred from T1 mechanisms, no source states the rule | unvalidated: rests on single-source claims only | unvalidated: quote not obtained (STRUCT-C06)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C06 | Keep module top level free of side effects other than initialising its own exports, so that importing it is safe in any order and unused code can be dropped by tools. | decision (single-source) | practice, language | single-source, inferred | SRC-087 §Side-effect-only imports [T1, admit, unrestricted]; SRC-095 §The sideEffects field [T1, admit-restricted, restricted to: webpack's own behaviour for the sideEffects field and pure annotations; not a language or Node rule (Node ignores the field, STRUCT-K06); never a ground for preferring webpack]; SRC-089 §Caching [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.STRUCTURE.LOADING.1` "Imports run once and hoisted" (refines): Hoisting and run-once are the JavaScript mechanisms that make import order and repetition invisible only when the top level is effect-free. Fate: removed from the graph, planned link to this node.
- `PIG-JS.STRUCTURE.LOADING.5` "Static structure for dropping unused code" (requires): Tools can drop unused code only when importing has no effect beyond exporting. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- refines to `STRUCTURE.DIRECTION.1` "No cycles between modules" (SEND): A module with no import-time effects cannot trip over an uninitialised binding in a cycle, which lowers the cost of a cycle that slips in (inferred from the cycle mechanism).

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Dependencies flow one way

- Origin: node `STRUCTURE.DIRECTION`, child of `STRUCTURE` ("Structure for locality of change", SPLIT). Verdict SEND: One-way dependencies between modules: language-neutral.
- Travels with: `STRUCTURE.DIRECTION.1` (No cycles between modules), `STRUCTURE.DIRECTION.2` (Declared layering).
- Intent: Let dependencies between modules flow in one direction so that a change propagates predictably.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known | gap: layering undecided

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Names carry the concept

- Origin: node `STRUCTURE.NAMING`, child of `STRUCTURE` ("Structure for locality of change", SPLIT). Verdict SEND: Names carry the concept: language-neutral (experiments on C# and others).
- Travels with: `STRUCTURE.NAMING.1` (Whole words), `STRUCTURE.NAMING.2` (One concept one word), `STRUCTURE.NAMING.3` (Name from the concept).
- Intent: Choose names that let a reader recover the concept without the author.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known | unvalidated: transfer from experiments to JavaScript is inference

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- refines from `CONTRACTS.SHAPE` "Shape of calls" (SEND): Call shapes are the smallest unit of the interface design STRUCTURE governs

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:COMMUNICATION`: Names are a reader-facing interface; the experiments here give the reason for the Python naming rules.

#### Paradigm by intent

- Origin: node `STRUCTURE.PARADIGM`, child of `STRUCTURE` ("Structure for locality of change", SPLIT). Verdict SEND: Paradigm by intent: language-neutral; the defect-rate studies compare languages, not JavaScript.
- Intent: Pick the programming paradigm per problem by what the problem is, not by a defect-rate claim.
- Constraints: 
  - MUST choose the paradigm per problem by intent: no admitted source supports choosing an object-oriented or a functional style inside JavaScript on defect-rate evidence.
- Design notes: 
  - Fact [contested]: Whether a paradigm lowers defects is contested and the studies compare languages, not paradigms inside one language: a modest language effect (Ray et al.), four of eleven languages significant with exceedingly small effects (reproduction), results largely replicated (rebuttal).
- Epistemic state: known | conflict: a paradigm lowers defects, Ray et al. 2014 (modest effect, restricted) | unvalidated: inferred from the absence of evidence scoped to JavaScript | unvalidated: rests on single-source claims only | unvalidated: quote not obtained (STRUCT-C64)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C64 | Choose the paradigm per problem by intent; no admitted source supports choosing an object-oriented or functional style inside JavaScript on defect-rate evidence. | decision (single-source) | decision, language | single-source, inferred | SRC-251 §Abstract [T2, admit-restricted, restricted to: the original finding that language design has a modest effect (functional somewhat better than procedural, strong over weak typing) dominated by process factors; contested by STRUCT-K25]; SRC-258 §Abstract [T2, admit-restricted, restricted to: language-to-defect associations in GitHub data are small or absent; cited only together with STRUCT-K25o and K33; never a ground for a paradigm choice inside JavaScript]; SRC-259 §3.10 [T2, admit-restricted, restricted to: the conceptual distinction between objects and abstract data types; no evidence for choosing either in JavaScript] |
| STRUCT-C63 | Whether a paradigm (functional, procedural, object-oriented) lowers defects is contested: Ray et al. report a modest language effect with functional somewhat better than procedural, the reproduction finds only four of eleven languages significant with exceedingly small effects, and the original authors answer that the reproduction largely replicated them. | fact (contested) | decision, language | contested, grounded | SRC-251 §Abstract [T2, admit-restricted, restricted to: the original finding that language design has a modest effect (functional somewhat better than procedural, strong over weak typing) dominated by process factors; contested by STRUCT-K25]; SRC-258 §Abstract [T2, admit-restricted, restricted to: language-to-defect associations in GitHub data are small or absent; cited only together with STRUCT-K25o and K33; never a ground for a paradigm choice inside JavaScript]; SRC-314 §Abstract [T3, admit-restricted, restricted to: the original authors' position in their dispute with STRUCT-K25; not peer-reviewed] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `STRUCTURE.HIDING.2` "Abstract data type versus object" (SEND): Choosing a paradigm per problem presupposes knowing what each hides: objects hide by procedural interface, data types by operations over a hidden representation.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:POLYGLOT`: Right paradigm for the right problem: the defect-rate evidence supports no paradigm mandate, which matches the intent-based choice.

#### Decompose by hidden decisions

- Origin: node `STRUCTURE.HIDING.1`, child of `STRUCTURE.HIDING` ("Hide likely-to-change decisions", SEND). Verdict SEND: Decompose by hidden decisions (Parnas): language-neutral (claim level: principle).
- Intent: Decompose a system by the decisions most likely to change, each hidden in one module, rather than by processing steps.
- Constraints: 
  - MUST decompose a system into modules by listing the design decisions that are difficult or likely to change and hiding each one inside one module, not by the steps of processing.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source (Parnas), principle only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C58 | Decompose a system into modules by listing difficult or likely-to-change design decisions and hiding each in one module, not by the steps of processing. | decision (single-source) | principle, language | single-source, grounded | SRC-257 §Decomposition criteria [T2, admit-restricted, restricted to: information hiding as the decomposition criterion, as a language-agnostic principle; never a JS-specific rule] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires from `STRUCTURE.HIDING.3` "Minimal public surface" (SEND): A decision stays hidden only if the surface that exposes the module stays minimal.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Abstract data type versus object

- Origin: node `STRUCTURE.HIDING.2`, child of `STRUCTURE.HIDING` ("Hide likely-to-change decisions", SEND). Verdict SEND: Abstract data type versus object (Cook): language-neutral (claim level: principle).
- Intent: Know which of the two hiding styles an interface offers, because they hide differently and mixing them blurs what may change.
- Constraints: 
  - MUST distinguish an abstract data type (representation hidden behind operations) from an object (procedural interface, information hidden by procedural abstraction), and do not conflate the two when designing an API.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source (Cook), conceptual distinction without effect evidence

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C62 | An abstract data type hides a representation behind operations; an object exports a procedural interface and hides information by procedural abstraction; the two differ and should not be conflated when designing a JavaScript API. | decision (single-source) | principle, language | single-source, grounded | SRC-259 §2.6 Summary [T2, admit-restricted, restricted to: the conceptual distinction between objects and abstract data types; no evidence for choosing either in JavaScript]; SRC-259 §3.10 Summary [T2, admit-restricted, restricted to: the conceptual distinction between objects and abstract data types; no evidence for choosing either in JavaScript] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.STRUCTURE.SURFACE.5` "No static-only container classes" (refines): A class of static members is a procedural namespace pretending to be an object (inferred). Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `STRUCTURE.PARADIGM` "Paradigm by intent" (SEND): Choosing a paradigm per problem presupposes knowing what each hides: objects hide by procedural interface, data types by operations over a hidden representation.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Minimal public surface

- Origin: node `STRUCTURE.HIDING.3`, child of `STRUCTURE.HIDING` ("Hide likely-to-change decisions", SEND). Verdict SEND: Minimal public surface: language-neutral principle; the three JavaScript exposure levels live in PIG-JS.STRUCTURE.SURFACE and .PACKAGE.
- Intent: Expose from each module only what other modules need, at every level where a name can be exposed.
- Constraints: 
  - MUST keep each module's public surface minimal at every level at which JavaScript can expose a name: named exports of a module, the package entry points, and class members.
- Design notes: none.
- Epistemic state: known | unvalidated: cross-level rule is inferred from one T2 principle and T1 mechanisms at two levels | unvalidated: rests on single-source claims only | unvalidated: quote not obtained (STRUCT-C59)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C59 | Keep each module's public surface minimal at all three levels: named exports of an ES module, the package "exports" field, and `#` class members. | decision (single-source) | principle, language | single-source, inferred | SRC-257 §Decomposition criteria [T2, admit-restricted, restricted to: information hiding as the decomposition criterion, as a language-agnostic principle; never a JS-specific rule]; SRC-244 §Export visibility [T2, admit-restricted, restricted to: unrestricted for 08_quality; 02_types: Positions of Google's TS guide only, never evidence; 04_struct: Google's positions with their stated reasons (default exports have no canonical name; export let banned; namespaces banned; interfaces over type literals), never evidence]; SRC-090 §exports field [T1, admit, unrestricted]; SRC-091 §Definition [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.STRUCTURE.SURFACE.1` "Named exports" (refines): A named export is one exposed name; a default export lets each importer rename it. Fate: removed from the graph, planned link to this node.
- `PIG-JS.STRUCTURE.SURFACE.2` "Minimal exported surface" (refines): Module-level form of the minimal public surface. Fate: removed from the graph, planned link to this node.
- `PIG-JS.STRUCTURE.PACKAGE.1` "Exports field" (refines): Package-level form of the minimal public surface. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `STRUCTURE.HIDING.1` "Decompose by hidden decisions" (SEND): A decision stays hidden only if the surface that exposes the module stays minimal.
- requires from `STRUCTURE.STATE.2` "Exported state is shared state" (KEEP): Exported state is part of a module's surface, so sharing it widens the surface that must stay minimal.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### One place per piece of state

- Origin: node `STRUCTURE.STATE.1`, child of `STRUCTURE.STATE` ("State in one place", SPLIT). Verdict SEND: One place per piece of state (Codd): language-neutral (claim level: principle).
- Intent: Hold each piece of state once and derive the rest, so copies cannot drift apart.
- Constraints: 
  - MUST keep each piece of state in one place: state kept in several places can become inconsistent, consistency being whether the value satisfies declared constraints. Transfer from shared data banks to application state is inference.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source (Codd), transfer to application state is inference

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C65 | State kept in more than one place can become inconsistent: Codd defines a state as consistent or inconsistent according as its value satisfies declared constraint statements, and treats redundancy and consistency together. | decision (single-source) | principle, language | single-source, grounded | SRC-252 §2 Redundancy and consistency [T2, admit-restricted, restricted to: normal form and the redundancy and consistency problem for shared data, as a principle; transfer to in-memory JavaScript application state is inference] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### No cycles between modules

- Origin: node `STRUCTURE.DIRECTION.1`, child of `STRUCTURE.DIRECTION` ("Dependencies flow one way", SEND). Verdict SEND: No cycles between modules: language-neutral (no own claim; Node CommonJS conflict note stays in the defaults).
- Intent: Do not let modules depend on each other in a cycle, so that load order never decides whether code works.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known | conflict: cycles are a supported mechanism, Node CommonJS docs (no recommendation) | unvalidated: derived from PIG-JS.STRUCTURE.DIRECTION.1, no source measures the cost

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.STRUCTURE.DIRECTION.1` "No import cycles" (refines): The JavaScript rule behind the principle of one-way dependencies. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- refines from `STRUCTURE.PURITY` "Effect-free importing" (SEND): A module with no import-time effects cannot trip over an uninitialised binding in a cycle, which lowers the cost of a cycle that slips in (inferred from the cycle mechanism).

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Declared layering

- Origin: node `STRUCTURE.DIRECTION.2`, child of `STRUCTURE.DIRECTION` ("Dependencies flow one way", SEND). Verdict SEND: Declared layering: language-neutral and undecided (no admitted ground).
- Intent: Declare which kinds of module may import which kinds and enforce it mechanically.
- Constraints: none (no decision row of its own).
- Design notes: 
  - Fact [single-source]: Demoted to fact: a lint rule can forbid imports by path or pattern, which makes mechanical enforcement of import direction possible; the claim that layer direction should be declared and enforced has no admitted ground (the rule documents environment fit, not layering), so the principle stays undecided.
- Epistemic state: undecided | missing: no admitted source grounds a layering principle (the only mechanism source documents environment fit)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C60 | Dependency direction between layers (which module kinds may import which) should be declared and enforced mechanically, with ESLint no-restricted-imports as one mechanism. | fact (single-source) | practice, tooling | single-source, open | SRC-085 §Why restrict imports [T1, admit-restricted, restricted to: the mechanism for forbidding imports by name or pattern; grounds no layering principle]; SRC-257 §Decomposition criteria [T2, admit-restricted, restricted to: information hiding as the decomposition criterion, as a language-agnostic principle; never a JS-specific rule] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.STRUCTURE.DIRECTION.3` "Declared layering" (refines): The JavaScript rendering of declared layering, undecided in both graphs. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Whole words

- Origin: node `STRUCTURE.NAMING.1`, child of `STRUCTURE.NAMING` ("Names carry the concept", SEND). Verdict SEND: Whole words: language-neutral (experiment on C# developers).
- Intent: Name with whole words, not single letters or abbreviations, because readers find defects faster.
- Constraints: 
  - MUST name identifiers with whole words, not single letters or letter-deleting abbreviations: words gave about 19 percent faster defect finding than letters or abbreviations in an experiment with 72 professional C# developers, with no significant difference between letters and abbreviations. Transfer to JavaScript is inference.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 experiment on C#, transfer to JavaScript inferred

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C55 | Name identifiers with whole words, not single letters or abbreviations: in an experiment with 72 professional C# developers, words gave about 19 percent faster comprehension in finding defects than letters or abbreviations, with no significant difference between letters and abbreviations. | decision (single-source) | practice, language | single-source, grounded | SRC-260 §Abstract [T2, admit-restricted, restricted to: experimental effect of naming style (72 professional C# developers; words about 19% faster than letters or abbreviations); transfer to JS is inference] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### One concept one word

- Origin: node `STRUCTURE.NAMING.2`, child of `STRUCTURE.NAMING` ("Names carry the concept", SEND). Verdict SEND: One concept one word: language-neutral (holder positions of style guides).
- Intent: Give one concept one name made of common descriptive words, used consistently.
- Constraints: 
  - MUST give one concept one word, made of common words and descriptive: holder positions of Google JS, Google TS, W3C TAG and Airbnb agree. Holder positions only, not evidence.
- Design notes: none.
- Epistemic state: known | unvalidated: holder position only (Google JS, Google TS, W3C TAG, Airbnb)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C56 | Guides hold that names are descriptive and not abbreviated by deleting letters (Google JS and Google TS), consistent and made of common words (W3C TAG), and descriptive (Airbnb). | decision (single-source) | practice, language | single-source, grounded | SRC-239 §6.1 [T2, admit-restricted, restricted to: 01_lang: Positions of the Google JS guide only, as frozen; where the Google TS guide (TYPES-K16) covers the same point, cite that one; 03_async: Google's positions only (throw only Error objects; a no-op catch must explain why in a comment), never evidence; 04_struct: Google's positions only (no default exports, no cycles between ES modules, exports not mutated after initialisation, optional trailing underscore for @private), never evidence; 08_quality: Google's positions as of the guide's freeze only; not for tooling choices (clang-format, Closure); superseded where the TS guide differs]; SRC-244 §Naming [T2, admit-restricted, restricted to: unrestricted for 08_quality; 02_types: Positions of Google's TS guide only, never evidence; 04_struct: Google's positions with their stated reasons (default exports have no canonical name; export let banned; namespaces banned; interfaces over type literals), never evidence]; SRC-261 §12.1 [T2, admit-restricted, restricted to: W3C TAG positions for web platform API design (options dictionaries, optional arguments, naming, constructors only for stateful classes, Promises and AbortSignal); transfer to library and application APIs is inference]; SRC-261 §12.5 [T2, admit-restricted, restricted to: W3C TAG positions for web platform API design (options dictionaries, optional arguments, naming, constructors only for stateful classes, Promises and AbortSignal); transfer to library and application APIs is inference]; SRC-312 §23.1 [T3, admit-restricted, restricted to: 01_lang: Positions of the Airbnb guide only, never evidence (policy standing rule on popular guides); 04_struct: Airbnb's positions only (10.3 no export directly from an import, 10.6 prefer default export, 23.4 no leading or trailing underscores), never evidence; 08_quality: Positions of the Airbnb guide only, never evidence; its shareable config is not a current tooling route] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Name from the concept

- Origin: node `STRUCTURE.NAMING.3`, child of `STRUCTURE.NAMING` ("Names carry the concept", SEND). Verdict SEND: Name from the concept: language-neutral (naming experiments).
- Intent: Derive a name from the concepts it covers, one word per concept, then compose; do not expect two people to coin the same name.
- Constraints: 
  - MUST derive a name by selecting the concepts, choosing words per concept, then composing the name; expect two developers to pick the same name only rarely (median 6.9 percent over 47 instances) but a chosen name to be understood.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source, language of the experiments not checked

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| STRUCT-C57 | Expect two developers to pick the same name for a thing only rarely (median 6.9 percent over 47 instances), but a chosen name is usually understood; name by selecting concepts, choosing words per concept, then composing the name. | decision (single-source) | practice, language | single-source, grounded | SRC-254 §Abstract [T2, admit-restricted, restricted to: the name-agreement finding (median 6.9% over 47 instances, 334 subjects) and the three-step naming model; language of the experiments not yet checked] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch DEFENSE: Defense

#### Data becoming instruction or location

- Origin: node `DEFENSE.INJECTION`, child of `DEFENSE` ("Defense", SPLIT). Verdict SEND: Data becoming code, command, query, path, destination or serialized object: injection classes hold unchanged for any language.
- Travels with: `DEFENSE.INJECTION.1` (Strings never become code), `DEFENSE.INJECTION.2` (Commands are not built from input), `DEFENSE.INJECTION.3` (Queries keep code and data apart), `DEFENSE.INJECTION.4` (Paths stay inside their base), `DEFENSE.INJECTION.5` (Serialized data carries no behaviour), `DEFENSE.INJECTION.6` (Destinations are chosen by the server).
- Intent: Hostile data must not become an instruction or a location for an interpreter outside the page: code, shell command, query, file path, network destination or serialized object.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION` "Injection classes" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- refines to `CONTRACTS.BOUNDARY.2` "Accept by positive rule" (SEND): Positive validation is the language-neutral form of the allowlist stance DEFENSE takes toward sinks and injection
- requires from `DEPENDENCIES.TRUST.1` "Every dependency is trusted code" (KEEP): Injection sinks that dependencies carry (eval, exec) are the subject of DEFENSE.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:DEFENSIVE`: Boundary validation and fail-fast apply to every interpreter the data can reach.

#### Secrets and cryptographic primitives

- Origin: node `DEFENSE.SECRETS`, child of `DEFENSE` ("Defense", SPLIT). Verdict SEND: Secrets never committed, audited primitives, token verification on the recipient's terms: hold unchanged for any language.
- Intent: Secrets are never committed and are drawn, compared, stored and logged only through audited platform mechanisms, since hand-rolled randomness, comparison or storage leaks them in ways nobody sees. A token is accepted only on the recipient's terms, never on the token's own.
- Constraints: 
  - MUST NOT hardcode secrets in source code or committed configuration files.
  - MUST reject the entire JWT if any cryptographic operation in it fails to validate, and reject it if any validation step of the token specification fails.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNSEC-C46 | Never hardcode secrets in source code or committed configuration files. | decision (consensus) | principle, node | consensus, grounded | SRC-138 §General secrets management [T1, admit-restricted, restricted to: Language-neutral principles only (no hardcoded secrets, env variables as weaker option, pre-commit detection); no JavaScript-specific claim]; SRC-275 §Abstract [T2, admit-restricted, restricted to: Language-neutral evidence with year (over 100,000 repositories, 2019)] |
| SECGAP2-C03 | Reject the entire JWT if any cryptographic operation in it fails to validate, and reject it if any RFC 7519 section 7.2 validation step fails. | decision (consensus) | principle, node | consensus, grounded | SRC-377 §3.3 [T1, admit, unrestricted]; SRC-376 §7.2 [T1, admit-restricted, restricted to: Claims definitions and the section 7.2 validation steps; the section 8 requirement to implement none is read only together with RFC 8725 (K01), which updates it] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.SECRETS` "Secrets and cryptography defaults" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.SECRETS.5` "Secret handling" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.SECRETS.2.1` "Token and JWT verification" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.SECRETS.2.2` "Token library settings" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Strings never become code

- Origin: node `DEFENSE.INJECTION.1`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: Never build code from strings: holds for any language with dynamic evaluation; the JavaScript sinks live in PIG-JS.DEFENSE.INJECTION.1.
- Intent: Data is never compiled or evaluated as code, whatever the API that offers it.
- Constraints: 
  - MUST NOT build code from strings: dynamic code evaluation executes attacker-influenced input as code with the caller's privileges, whatever API offers it.
- Design notes: 
  - Fact [single-source]: Template injection is a server-side code-execution class, unlike XSS: it reaches server internals and can give remote code execution; one published case study reached arbitrary command execution through a template context (T3 research evidence).
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNSEC-C14 | Never build code from strings: eval, new Function and string arguments to setTimeout or setInterval execute attacker-influenced input as code with the caller's privileges. | decision (consensus) | principle, language | consensus, grounded | SRC-123 §Warning [T1, admit, unrestricted]; SRC-124 §Warning [T1, admit, unrestricted]; SRC-134 §eval, Function, and with [T1, admit, unrestricted]; SRC-135 §Dangerous functions [T1, admit-restricted, restricted to: Statements on Node core API risks only (eval, child_process.exec, ReDoS, path traversal); its third-party npm package recommendations are excluded] |
| SECGAP2-C31 | Template injection is a server-side code execution class, unlike XSS; the Jade (Pug) case study reached arbitrary command execution through the template context. | fact (single-source) | js-principle, node | single-source, grounded | SRC-411 §What Template Injection Is [T3, admit-restricted, restricted to: Mechanism and the Jade case study as research evidence; the three defences (trivial engine such as Mustache, sandbox, container) as the author's positions; no tool claim]; SRC-408 §Summary [T2, admit-restricted, restricted to: Detection mechanism (plaintext against code context) for Jinja2, Twig and FreeMarker only; no JavaScript engine, no remediation section] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.1` "No code from strings" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.1.3` "Template injection" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.1.4` "Handlebars and EJS" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `DEFENSE.INJECTION.5` "Serialized data carries no behaviour" (SEND): Reviving types or functions from serialized data is building code from strings, so the code rule must hold first.
- dataflow from `DEFENSE.PROTOTYPE.2` "Pollution can be code execution" (KEEP): A polluted shared prototype feeds gadgets that compile or run attacker-shaped values, ending in code execution.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Commands are not built from input

- Origin: node `DEFENSE.INJECTION.2`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: No shell, no input-chosen programs: command injection holds for any language.
- Intent: A process is started without a shell and without input-chosen programs, so arguments stay arguments.
- Constraints: 
  - MUST prefer built-in library functions to invoking OS commands at all; they cannot be manipulated into other tasks.
  - MUST allowlist the executable and the arguments and run the process with the least privilege required when an OS command is unavoidable.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNSEC-C25 | Prefer built-in library functions over invoking OS commands at all; they cannot be manipulated into other tasks. | decision (single-source) | principle, node | single-source, grounded | SRC-136 §Primary defense [T1, admit-restricted, restricted to: Principles only (avoid shell, parameterize, allowlist); examples are Java, .NET, PHP] |
| RUNSEC-C26 | When an OS command is unavoidable, allowlist the executable and the arguments, and run the process with the least privilege required. | decision (single-source) | principle, node | single-source, grounded | SRC-136 §Defense option 3 and additional defenses [T1, admit-restricted, restricted to: Principles only (avoid shell, parameterize, allowlist); examples are Java, .NET, PHP] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.2` "OS commands" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Queries keep code and data apart

- Origin: node `DEFENSE.INJECTION.3`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: Parameterized queries: SQL and NoSQL injection hold for any language.
- Intent: A query reaches its engine as fixed text plus separately passed values, in every store, SQL or not.
- Constraints: 
  - MUST build queries with parameters passed separately from the query text; never concatenate or template untrusted values into it, because the database must receive code and data separately.
  - MUST bind variables carry values only: identifiers, keywords and sort order never come from input; redesign the query or map the input through a fixed allowlist.
  - MUST run the application's database account with least privilege as a second layer behind parameterization and validation.
- Design notes: 
  - Rejected [single-source]: Rejected: escaping all user input as the primary defence against SQL injection. OWASP calls it strongly discouraged, fragile, and not guaranteed to stop all injections.
  - Rejected [consensus]: Belief rejected: NoSQL stores are immune to injection. A BSON query is an object, so string injection does not apply, but client-supplied objects used as field values inject query operators such as { $ne: "" }.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SRVSEC-C15 | Build SQL with parameterized queries (prepared statements) and pass values separately; never concatenate or template untrusted values into the query text. | decision (consensus) | principle, node | consensus, grounded | SRC-345 §Defense Option 1 [T1, admit-restricted, restricted to: Principles: prepared statements, stored procedures, allow-list mapping for identifiers, escaping "STRONGLY DISCOURAGED" and fragile; no JavaScript content]; SRC-335 §Parameterized query [T1, admit-restricted, restricted to: Facts about `pg`: parameters go to the server unaltered; no parameters for identifiers; `pg-format` named for identifiers]; SRC-341 §1.2.4 [T1, admit-restricted, restricted to: 13_srvsec: Verification requirements only, and only these ids with the topic their text states: 1.2.4 (database queries parameterized), 1.3.6 (SSRF allowlist), 5.2.5 (symlinks in archives), 5.3.2 (file paths from trusted data), 5.3.3 (decompression ignores user path info), 11.2.4 (constant-time operations), 11.5.1 (CSPRNG, 128 bits), 15.1.5 (dangerous functionality documented; deserialization named only in the section introduction), 15.3.2 (no redirects followed by backend), 16.5.1 and 16.4.1 (error exposure, log encoding). Not for deserialization via 15.1.1, not for path containment via 5.2.3, not for SSRF via 5.3.2; 14_secgap2: Adds to SRC-341 (same applies to SRC-132 on the tree URL) these ids, checklist items only, each with its stated topic: 1.2.2, 1.3.5 (scriptable template language content, not SSTI), 1.3.7, 1.5.1, 5.1.1, 5.2.1, 5.2.2, 5.2.3 (archive uncompressed size, not path containment), 5.2.4, 5.2.6, 5.3.1, 5.4.1, 5.4.2, 5.4.3, 15.1.2, 15.2.4; the V1, V5 and V15 files are also admitted as K12, K27 and K36]; SRC-352 §Mitigations [T2, admit-restricted, restricted to: Name, definition and the generic parameterized-statement mitigation]; SRC-347 §queryRaw [T1, admit-restricted, restricted to: Facts about `$queryRaw` (tagged template, prepared statements), `$queryRawUnsafe` and `Prisma.raw` (injection when concatenated); never a preference for Prisma] |
| SRVSEC-C17 | Bind variables cannot stand in for identifiers (table, column, database names), SQL keywords or sort order; for those, redesign the query or map the input through a fixed allow-list. | decision (consensus) | principle, node | consensus, grounded | SRC-345 §Defense Option 3 [T1, admit-restricted, restricted to: Principles: prepared statements, stored procedures, allow-list mapping for identifiers, escaping "STRONGLY DISCOURAGED" and fragile; no JavaScript content]; SRC-335 §Parameterized query [T1, admit-restricted, restricted to: Facts about `pg`: parameters go to the server unaltered; no parameters for identifiers; `pg-format` named for identifiers]; SRC-347 §queryRaw [T1, admit-restricted, restricted to: Facts about `$queryRaw` (tagged template, prepared statements), `$queryRawUnsafe` and `Prisma.raw` (injection when concatenated); never a preference for Prisma] |
| SRVSEC-C19 | Do not rely on escaping all user input as the primary defense against SQL injection: OWASP calls it strongly discouraged, fragile compared with other defenses, and not guaranteed to stop all injections. | rejected (single-source) | principle, node | single-source, grounded | SRC-345 §Defense Option 4 [T1, admit-restricted, restricted to: Principles: prepared statements, stored procedures, allow-list mapping for identifiers, escaping "STRONGLY DISCOURAGED" and fragile; no JavaScript content] |
| SRVSEC-C22 | Use least privilege for the database account of the application as a second layer behind parameterization and validation. | decision (single-source) | principle, node | single-source, grounded | SRC-345 §Additional Defenses [T1, admit-restricted, restricted to: Principles: prepared statements, stored procedures, allow-list mapping for identifiers, escaping "STRONGLY DISCOURAGED" and fragile; no JavaScript content] |
| SRVSEC-C23 | NoSQL stores are not immune to injection: a BSON query is an object, so classic string injection does not apply, yet client-supplied objects used as field values inject query operators (for example { $ne: "" }). | rejected (consensus) | principle, node | consensus, grounded | SRC-332 §Injection FAQ [T1, admit-restricted, restricted to: Facts about MongoDB: queries are BSON; `$where`, `mapReduce`, `$accumulator`, `$function` run JavaScript; `--noscripting`; `$where` cannot use indexes]; SRC-343 §Operator injection [T1, admit-restricted, restricted to: Principles: validate scalar types before building a filter, objects as field values enable operator injection, `$where` runs untrusted JavaScript, disable server-side JavaScript; quotes come from a summary, extractor reads verbatim]; SRC-355 §Summary [T2, admit-restricted, restricted to: Mechanism of `$where` JavaScript injection and the CPU exhaustion example; testing guidance, not remediation; version 4.1 page]; SRC-354 §Description [T2, admit-restricted, restricted to: Name and definition; observed examples name MongoDB and Mongoose (the discoverer found none)] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.3` "SQL and NoSQL queries" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Paths stay inside their base

- Origin: node `DEFENSE.INJECTION.4`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: Path containment: path traversal holds for any language.
- Intent: A file location chosen from input is confined to a base directory, checked after resolution and used without a race.
- Constraints: 
  - MUST build file paths from internally generated or trusted names, not user-submitted filenames; where user filenames are unavoidable, apply strict allowlist validation.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNSEC-C28 | Build file paths from internally generated or trusted names, not user-submitted filenames; if user filenames must be used, apply strict allowlist validation and sanitization. | decision (consensus) | principle, node | consensus, grounded | SRC-132 §5.3.2 [T1, admit-restricted, restricted to: Verification requirements only; read: 5.3.2 (file paths), 5.4.1, 15.3.6 (prototype pollution, Set or Map), 15.1.5 (dangerous functionality incl. deserialization); mechanisms come from another T1]; SRC-272 §Potential mitigations [T2, admit-restricted, restricted to: Taxonomy and language-neutral mitigations (canonicalize, allowlist) only]; SRC-135 §Path traversal [T1, admit-restricted, restricted to: Statements on Node core API risks only (eval, child_process.exec, ReDoS, path traversal); its third-party npm package recommendations are excluded] |
| SECGAP2-C81 | Build file paths from internally generated or trusted data, and where user-submitted file names or metadata must be used, apply strict validation and sanitization. | decision (consensus) | practice, node | single-source, grounded | SRC-391 §5.3.2 [T1, admit-restricted, restricted to: Checklist items, ids 5.1.1 to 5.4.3 each with its stated topic; 5.2.3 is archive uncompressed size and file count, not path containment; 5.3.2 is file path construction; mechanisms from other T1] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.4` "File paths and archives" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.4.5` "Upload content checks" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.4.6` "Upload storage, names and limits" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Serialized data carries no behaviour

- Origin: node `DEFENSE.INJECTION.5`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: Serialized data carries no behaviour, XML external entities off: hold for any language.
- Intent: Data crossing a trust boundary is a pure data format, integrity-checked, and never revived into executable structures. Its parser loads nothing from outside the data.
- Constraints: 
  - MUST exchange data across a trust boundary in a pure data format such as JSON, never in formats that carry types or code, and never deserialize untrusted data into executable structures.
  - MUST sign serialized data and verify before deserializing (an HMAC where feasible) when the set of expected messages is known; populate a new object from validated fields instead of deserializing into the application's own types. Language-neutral grounds only.
  - MUST disable document type definitions (reject DOCTYPE) when parsing untrusted XML; where DTDs are required, disable external entity resolution and external DTD loading and limit entity expansion.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNSEC-C43 | Prefer a pure data format such as JSON over formats that can carry types or code when exchanging data across a trust boundary, and never deserialize untrusted data into executable structures. | decision (consensus) | principle, node | consensus, grounded | SRC-133 §General principles [T1, admit-restricted, restricted to: Language-neutral principles only; JavaScript not covered (PHP, Python, Java, .NET)]; SRC-132 §15.1.5 [T1, admit-restricted, restricted to: Verification requirements only; read: 5.3.2 (file paths), 5.4.1, 15.3.6 (prototype pollution, Set or Map), 15.1.5 (dangerous functionality incl. deserialization); mechanisms come from another T1]; SRC-134 §eval, Function, and with [T1, admit, unrestricted] |
| RUNSEC-C44 | Sign serialized messages when the set of expected messages is known, and verify before deserializing. | decision (single-source) | principle, node | single-source, grounded | SRC-133 §Integrity checks [T1, admit-restricted, restricted to: Language-neutral principles only; JavaScript not covered (PHP, Python, Java, .NET)] |
| SRVSEC-C45 | When deserializing, populate a new object from validated fields instead of deserializing straight into the application's own object types, and use integrity checks (for example an HMAC) on serialized data where feasible. | decision (single-source) | principle, node | single-source, grounded | SRC-351 §Potential Mitigations [T2, admit-restricted, restricted to: Name, definition, generic mitigations; examples are Java and Python only] |
| SECGAP2-C18 | Disable DTDs (reject DOCTYPE) when parsing untrusted XML; where DTDs are required, disable external entity resolution and external DTD loading and limit entity expansion. | decision (consensus) | principle, node | consensus, grounded | SRC-399 §General Guidance [T1, admit-restricted, restricted to: General guidance only: disable DTDs, reject DOCTYPE, disable external entity resolution and limit entity expansion; it has no Node or JavaScript section (headings read: C/C++, ColdFusion, Java, .NET, iOS, PHP, Python, Semgrep)]; SRC-400 §External Entity Processing [T1, admit-restricted, restricted to: Language-neutral: use XSD not DTD, disable external entity processing, bound occurrences, HTTPS for remote schemas; no JavaScript content]; SRC-388 §1.5.1 [T1, admit-restricted, restricted to: Checklist items, ids 1.2.2 (URL encoding and safe protocols), 1.3.5 (sanitize or disable scriptable template language content such as Markdown, CSS or XSL; not SSTI), 1.3.7 (templates not built from untrusted input), 1.5.1 (XML parsers restrictive, no external entities); ids 1.2.6 (LDAP), 1.2.7 (XPath), 1.3.12 (ReDoS) are not this slot's topics] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.5` "Deserialization" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.5.4` "XML and external entities" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.5.3` "v8.deserialize" (refines): The default applies the principle's integrity-check and new-object rules, whose claims are held on the principle, to v8.deserialize. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `DEFENSE.INJECTION.1` "Strings never become code" (SEND): Reviving types or functions from serialized data is building code from strings, so the code rule must hold first.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Destinations are chosen by the server

- Origin: node `DEFENSE.INJECTION.6`, child of `DEFENSE.INJECTION` ("Data becoming instruction or location", SEND). Verdict SEND: Server-chosen destinations (SSRF): holds for any language.
- Intent: A server fetches only destinations it allows, checked at the address it will actually connect to.
- Constraints: 
  - MUST match the host of an outbound request against an allowlist and build the request yourself when the destination is known.
  - MUST NOT accept complete URLs from users when avoidable: URLs are hard to validate and the parser can be abused; accept validated hosts or addresses instead.
  - MUST validate the resolved destination addresses against the permitted networks and make the client connect only to the validated addresses; a hostname check alone is not enough.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SRVSEC-C28 | When the destination of an outbound request is known, match the host against an allow-list and build the request yourself; do not take a full URL from the user. | decision (consensus) | principle, node | consensus, grounded | SRC-346 §Case 1 [T1, admit-restricted, restricted to: Principles: allowlist over denylist, validate resolved IPs and connect only to validated addresses, disable redirects, IMDSv2; the npm library `ip-address` it names never grounds a tool choice]; SRC-341 §1.3.6 [T1, admit-restricted, restricted to: 13_srvsec: Verification requirements only, and only these ids with the topic their text states: 1.2.4 (database queries parameterized), 1.3.6 (SSRF allowlist), 5.2.5 (symlinks in archives), 5.3.2 (file paths from trusted data), 5.3.3 (decompression ignores user path info), 11.2.4 (constant-time operations), 11.5.1 (CSPRNG, 128 bits), 15.1.5 (dangerous functionality documented; deserialization named only in the section introduction), 15.3.2 (no redirects followed by backend), 16.5.1 and 16.4.1 (error exposure, log encoding). Not for deserialization via 15.1.1, not for path containment via 5.2.3, not for SSRF via 5.3.2; 14_secgap2: Adds to SRC-341 (same applies to SRC-132 on the tree URL) these ids, checklist items only, each with its stated topic: 1.2.2, 1.3.5 (scriptable template language content, not SSTI), 1.3.7, 1.5.1, 5.1.1, 5.2.1, 5.2.2, 5.2.3 (archive uncompressed size, not path containment), 5.2.4, 5.2.6, 5.3.1, 5.4.1, 5.4.2, 5.4.3, 15.1.2, 15.2.4; the V1, V5 and V15 files are also admitted as K12, K27 and K36] |
| SRVSEC-C30 | Do not accept complete URLs from users when avoidable, because URLs are hard to validate and the parser can be abused; accept validated hosts or addresses instead. | decision (single-source) | principle, node | single-source, grounded | SRC-346 §Validation [T1, admit-restricted, restricted to: Principles: allowlist over denylist, validate resolved IPs and connect only to validated addresses, disable redirects, IMDSv2; the npm library `ip-address` it names never grounds a tool choice] |
| SRVSEC-C32 | Validate the resolved destination IP addresses against the permitted networks, and make the HTTP client connect only to the validated addresses; a hostname check alone is not enough. | decision (single-source) | principle, node | single-source, grounded | SRC-346 §DNS validation [T1, admit-restricted, restricted to: Principles: allowlist over denylist, validate resolved IPs and connect only to validated addresses, disable redirects, IMDSv2; the npm library `ip-address` it names never grounds a tool choice] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.INJECTION.6` "Outbound requests" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.INJECTION.6.4` "Node fetch redirect semantics" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch DEPENDENCIES: Dependencies

#### Publishing

- Origin: node `DEPENDENCIES.PUBLISH`, child of `DEPENDENCIES` ("Dependencies", SPLIT). Verdict SEND: Hardening publishing accounts of any registry: language-neutral (two-factor authentication).
- Intent: A project that publishes a package is itself a dependency of others, and its publishing accounts are the takeover route into them.
- Constraints: 
  - MUST enable two-factor authentication on registry publishing accounts; phishing-resistant MFA on developer accounts is the response CISA recommends after account compromises.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C17 | Enable two-factor authentication on registry publishing accounts; phishing-resistant MFA on developer accounts is the response CISA recommends after account compromises. | decision (consensus) | practice, node | consensus, grounded | SRC-154 §2FA [T1, admit-restricted, restricted to: items not superseded by npm 12 docs (K05 to K08), recorded as archived 2023 guidance; shrinkwrap items excluded; no provenance coverage]; SRC-155 §Enable 2FA [T1, admit-restricted, restricted to: mitigation items not superseded by npm 12 docs; named tools (Snyk, LavaMoat, Verdaccio) never ground a tool choice; ignore-scripts advice applies to npm before v12]; SRC-288 §Root cause [T2, admit-restricted, restricted to: incident facts only (password reuse, no 2FA, postinstall token theft, eslint-scope 3.7.2)]; SRC-295 §Recommended actions [T2, admit-restricted, restricted to: incident facts (Shai-Hulud, 500+ packages, credential-harvesting worm); its recommended actions recorded as CISA's position] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEPENDENCIES.PUBLISH.1` "CI publishing credentials" (refines): Short-lived CI credentials harden the publishing route. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEPENDENCIES.PUBLISH.2` "Tarball contents" (refines): Reviewing tarball contents keeps secrets out of what consumers receive. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEPENDENCIES.PUBLISH.3` "Ship JavaScript" (refines): Shipping runnable JavaScript is part of being a good dependency. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `DEPENDENCIES.THREATS.1` "Takeover of maintainership" (KEEP): Publishing accounts are the takeover route that has to be hardened.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Layered controls

- Origin: node `DEPENDENCIES.TRUST.3`, child of `DEPENDENCIES.TRUST` ("Dependencies are trusted code", KEEP). Verdict SEND: Layered controls (defence in depth, attack trees): language-neutral (claim level: principle).
- Intent: No single control is relied on; controls stack across the routes of attack.
- Constraints: 
  - MUST layer controls rather than rely on one: attack trees list 107 vectors from code contribution to distribution, mapped to 33 safeguards.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source, claim is inferred from a taxonomy

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C32 | Layer controls rather than rely on one: attack trees list 107 vectors across code contribution to distribution, mapped to 33 safeguards. | decision (single-source) | principle, node | single-source, inferred | SRC-291 §abstract [T2, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires from `DEPENDENCIES.TRUST.2` "No containment inside the process" (KEEP): With no containment inside the process, protection can only come from stacked controls.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Existing components first

- Origin: node `DEPENDENCIES.ADMISSION.1`, child of `DEPENDENCIES.ADMISSION` ("Admission", SPLIT). Verdict SEND: Existing components first is sourcing (what to build versus take): owned by the software guideline.
- Intent: A dependency must earn its trust cost against what the platform and the current code already provide.
- Constraints: 
  - MUST ask whether existing components suffice before adding a dependency, and test the candidate in isolation for unexpected indirect dependencies in production.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C27 | Before adding a dependency, ask whether existing components suffice, and test it in isolation for unexpected indirect dependencies in production. | decision (single-source) | practice, node | single-source, grounded | SRC-144 §Initial Assessment [T1, admit, unrestricted]; SRC-144 §Practical Testing [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` "Framework short list" (refines): The framework is the largest case of a dependency earning its trust cost. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1` "Platform baseline" (refines): The platform is the existing component that suffices first. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `DEPENDENCIES.TRUST.1` "Every dependency is trusted code" (KEEP): Because every dependency is trusted code, each addition must first earn its trust cost.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:INTENTIONALITY`: Every artifact, a dependency included, exists for an articulated reason.

#### Identity of the package

- Origin: node `DEPENDENCIES.ADMISSION.3`, child of `DEPENDENCIES.ADMISSION` ("Admission", SPLIT). Verdict SEND: Identity of a package (typosquatting, look-alike) is judging libraries: sourcing, any registry.
- Intent: Before adoption, the name is confirmed to be the package intended and the package to be authentic.
- Constraints: 
  - MUST check a package's name for typos and for a more popular look-alike before adding it, and verify that it exists and is authentic.
- Design notes: none.
- Epistemic state: known

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C24 | Check dependency names for typos and for a more popular look-alike before adding a package, and verify the package exists and is authentic. | decision (consensus) | practice, node | consensus, grounded | SRC-078 §Mitigations [T1, admit-restricted, restricted to: unrestricted for 03_async, 06_runsec; 07_supply: attack-vector list and mitigations not superseded by npm 12 docs; ignore-scripts advice applies to npm before v12 only; the Socket mention never grounds a tool choice]; SRC-144 §Adoption and Licensing [T1, admit, unrestricted]; SRC-155 §Typosquatting and Slopsquatting [T1, admit-restricted, restricted to: mitigation items not superseded by npm 12 docs; named tools (Snyk, LavaMoat, Verdaccio) never ground a tool choice; ignore-scripts advice applies to npm before v12] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEPENDENCIES.INSTALL.4` "Owned scope for internal packages" (refines): An owned scope closes the namespace route that the identity check covers by hand. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEPENDENCIES.SCREEN.3` "Typosquatting screening" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `DEPENDENCIES.THREATS.2` "Confusion is many mechanisms" (KEEP): Confusion mechanisms are what the identity check has to cover.
- dataflow from `DEPENDENCIES.EVIDENCE.1` "Provenance and signatures" (KEEP): Origin evidence supports the authenticity check without replacing it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Documentation examples are untrusted

- Origin: node `DEPENDENCIES.ADMISSION.4`, child of `DEPENDENCIES.ADMISSION` ("Admission", SPLIT). Verdict SEND: Documentation examples are untrusted: holds for any language and ecosystem.
- Intent: Example code shipped with a package's documentation is untrusted until reviewed.
- Constraints: 
  - MUST NOT copy README examples into production without a security review.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C39 | Do not copy README examples into production without a security review. | decision (single-source) | practice, node | single-source, grounded | SRC-155 §Verify Documentation Examples [T1, admit-restricted, restricted to: mitigation items not superseded by npm 12 docs; named tools (Snyk, LavaMoat, Verdaccio) never ground a tool choice; ignore-scripts advice applies to npm before v12] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `DEFENSE.DOM.1` "Sources and sinks" (KEEP): README examples that reach DOM or injection sinks are reviewed under DEFENSE rules.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Updates

- Origin: node `DEPENDENCIES.CHANGE.4`, child of `DEPENDENCIES.CHANGE` ("Controlled change", KEEP). Verdict SEND: Automated updates, security updates separated, cooldown tradeoff: language-neutral supply-chain practice.
- Intent: Updates flow through an automated mechanism that separates security from feature updates; how long to wait before adopting a fresh release is a tradeoff whose benefit is unmeasured.
- Constraints: 
  - MUST run an automated dependency-update and vulnerability-alert mechanism, with security updates enabled and kept separate from feature updates, because bundled fixes hinder adoption.
- Design notes: 
  - Fact [single-source]: The effectiveness of a release-age cooldown rests on one T1 assertion and vendor figures; no peer-reviewed measurement of time-to-removal was found.
  - Fact [single-source]: The OpenSSF concise guide recommends a cooldown of about three days and says it counters most malicious releases; the origin of that figure is not found, so it is recorded as the body's position and never used as evidence.
- Epistemic state: known | gap: cooldown effectiveness unmeasured, one T1 assertion and vendor figures | unvalidated: rests on claims marked inferred or open (QUALITY-C46, SUPPLY-C13, SUPPLY-C36)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C36 | Run an automated dependency-update and vulnerability-alert mechanism, with security updates enabled and kept separate from feature updates, because bundled fixes hinder adoption. | decision (majority) | practice, tooling | majority, inferred | SRC-154 §Audit [T1, admit-restricted, restricted to: items not superseded by npm 12 docs (K05 to K08), recorded as archived 2023 guidance; shrinkwrap items excluded; no provenance coverage]; SRC-161 §Dependency-Update-Tool [T1, admit-restricted, restricted to: 07_supply: facts about what each check detects and its stated limits (GitHub-only checks, false negatives); a score is never evidence a package is safe; 08_quality: Facts about what Scorecard checks and how it rates risk; presence of a check grounds "Scorecard rewards X", not that X is effective]; SRC-295 §Recommended actions [T2, admit-restricted, restricted to: incident facts (Shai-Hulud, 500+ packages, credential-harvesting worm); its recommended actions recorded as CISA's position]; SRC-281 §abstract [T2, admit, unrestricted] |
| SUPPLY-C13 | The effectiveness of a release-age cooldown rests on one T1 assertion and vendor figures; no peer-reviewed measurement of time-to-removal was found. | fact (single-source) | decision, tooling | single-source, open | SRC-078 §Mitigations [T1, admit-restricted, restricted to: unrestricted for 03_async, 06_runsec; 07_supply: attack-vector list and mitigations not superseded by npm 12 docs; ignore-scripts advice applies to npm before v12 only; the Socket mention never grounds a tool choice]; SRC-319 §incident figures [T3, admit-restricted, restricted to: GitHub's incident-window figures (21 incidents pulled within hours, about 6,500 npm malware advisories in a year) as the vendor's own analysis, single-source; behaviour facts come from K40o] |
| QUALITY-C46 | The OpenSSF concise guide recommends a dependency-update cooldown of about three days, saying cooldowns counter most malicious package releases; the origin of that figure is not yet found, so do not use it as evidence. | fact (single-source) | decision, tooling | single-source, open: position of the body, origin of the effectiveness claim missing (register restriction) | SRC-163 §Dependency cooldown [T1, admit-restricted, restricted to: OpenSSF Best Practices WG recommendations as that body's positions; the claim that a ~3-day cooldown counters most malicious releases needs its origin before use] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEPENDENCIES.UPDATE.1` "Release-age cooldown" (refines): The cooldown is the tool form of the update tradeoff. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- dataflow from `DEPENDENCIES.EVIDENCE.2` "Audit findings" (KEEP): Triaged findings feed the update mechanism, which keeps security updates separate.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Incident response

- Origin: node `DEPENDENCIES.CHANGE.5`, child of `DEPENDENCIES.CHANGE` ("Controlled change", KEEP). Verdict SEND: Incident response after a supply-chain compromise (lockfile, credentials, pins): language-neutral practice.
- Intent: After a worm-style compromise the lockfile, the credentials and the pinned versions are the three things re-established first.
- Constraints: 
  - MUST review lockfiles, rotate all developer credentials and pin to versions published before the incident date after a worm-style compromise (CISA's position).
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source, recorded as CISA's position

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SUPPLY-C41 | After a worm-style compromise, CISA's position is to review lockfiles, rotate all developer credentials and pin to versions published before the incident date. | decision (single-source) | practice, node | single-source, grounded | SRC-295 §Recommended actions [T2, admit-restricted, restricted to: incident facts (Shai-Hulud, 500+ packages, credential-harvesting worm); its recommended actions recorded as CISA's position] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `DEPENDENCIES.CHANGE.1` "Reproducible tree" (KEEP): Pinning to pre-incident versions presupposes a tree fixed by the lockfile.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch VERIFICATION: Verification

#### Static analysis baseline

- Origin: node `VERIFICATION.STATIC_BASELINE`, child of `VERIFICATION` ("Verification", SPLIT). Verdict SEND: Static analysis baseline: language-neutral (claims level: principle).
- Travels with: `VERIFICATION.STATIC_BASELINE.1` (Analysis switched on), `VERIFICATION.STATIC_BASELINE.2` (Analysis beyond the compiler), `VERIFICATION.STATIC_BASELINE.3` (Checks complement each other).
- Intent: Every project analyzes its code without running it, and acts on what the analysis reports, so that known classes of mistake never reach review.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND): An analysis finding is acted on only when the gate blocks the change that carries it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:DEFENSIVE`: Machine-run static analysis is how errors become visible early, for any language.

#### Test suite

- Origin: node `VERIFICATION.TEST_SUITE`, child of `VERIFICATION` ("Verification", SPLIT). Verdict SEND: Test suite policy: language-neutral.
- Travels with: `VERIFICATION.TEST_SUITE.1` (Tests for new functionality), `VERIFICATION.TEST_SUITE.2` (Coverage finds, it does not judge), `VERIFICATION.TEST_SUITE.3` (Test design).
- Intent: Behaviour is pinned by automated tests that exist for all new functionality, and whose adequacy is judged by what they detect, not by what they execute.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires to `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND): A test policy has effect only when a failing suite stops the merge.
- requires to `VERIFICATION.TEST_STABILITY` "Test stability" (SEND): A suite is a trusted signal only while its failures mean defects.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Fault detection power

- Origin: node `VERIFICATION.FAULT_DETECTION`, child of `VERIFICATION` ("Verification", SPLIT). Verdict SEND: Fault detection power: language-neutral.
- Travels with: `VERIFICATION.FAULT_DETECTION.1` (Mutation testing), `VERIFICATION.FAULT_DETECTION.2` (Property-based testing).
- Intent: A suite is worth the faults it would catch, so that power is measured directly and probed with generated inputs, not assumed.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Test stability

- Origin: node `VERIFICATION.TEST_STABILITY`, child of `VERIFICATION` ("Verification", SPLIT). Verdict SEND: Test stability: language-neutral (studies mostly of Java projects).
- Travels with: `VERIFICATION.TEST_STABILITY.1` (New tests are probed), `VERIFICATION.TEST_STABILITY.2` (Shared state is cleaned), `VERIFICATION.TEST_STABILITY.3` (Flake rate tracked).
- Intent: A test result is a usable signal only while a failure means a defect, so nondeterminism is prevented at the cause rather than retried away.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: known

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires from `VERIFICATION.TEST_SUITE` "Test suite" (SEND): A suite is a trusted signal only while its failures mean defects.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:REPRODUCIBILITY`: A flaky test is a failure of same inputs same outputs, so its result carries no information.

#### Enforcement at the merge

- Origin: node `VERIFICATION.ENFORCEMENT`, child of `VERIFICATION` ("Verification", SPLIT). Verdict SEND: The merge gate must not be skippable: language-neutral (platform fact).
- Intent: A check changes behaviour only when failing it stops the merge, so the gate itself must not be skippable.
- Constraints: 
  - MUST make the merge gate always run: a skipped required check must not let a merge through.
- Design notes: none.
- Epistemic state: known | unvalidated: practice inferred from a platform fact | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C43 | Remember that GitHub required status checks pass on successful, skipped or neutral; make the gate job always run so a skipped check cannot let a merge through. | decision (single-source) | practice, tooling | single-source, grounded for the platform fact; the practice is inferred | SRC-169 §Require status checks [T1, admit-restricted, restricted to: Facts about GitHub's own platform (required status checks, required reviews)] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.VERIFICATION.LINT.2` "Enforcement" (refines): CI exit status is how a lint finding blocks the merge in JavaScript. Fate: retargeted here to js-philosophy:VERIFICATION.
- `PIG-JS.DEPENDENCIES.SCREEN.1` "Scorecard as per-check evidence" (requires): Scorecard checks (tests before merge, review, branch protection) overlap CI gates. Fate: retargeted here to js-philosophy:VERIFICATION.

Links to other principles of the same graph:

- requires from `VERIFICATION.STATIC_BASELINE` "Static analysis baseline" (SEND): An analysis finding is acted on only when the gate blocks the change that carries it.
- requires from `VERIFICATION.TEST_SUITE` "Test suite" (SEND): A test policy has effect only when a failing suite stops the merge.
- requires from `CONTRACTS.STATIC.1` "Types attest nothing at run time" (KEEP): A type layer is a contract only while a tool checks it in the build and in CI, which VERIFICATION gates
- requires to `DEPENDENCIES.CHANGE.1` "Reproducible tree" (KEEP): The gate job includes the reproducible install step that DEPENDENCIES decides (QUALITY-C42 is routed there).

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Analysis switched on

- Origin: node `VERIFICATION.STATIC_BASELINE.1`, child of `VERIFICATION.STATIC_BASELINE` ("Static analysis baseline", SEND). Verdict SEND: Enable a linter or safe mode: language-neutral (OpenSSF criteria).
- Intent: A linter or safe language mode is enabled and its warnings are addressed, because unread warnings protect nothing.
- Constraints: 
  - MUST enable a linter or a safe language mode and address its warnings; the OpenSSF passing criteria make this a MUST.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C20 | Enable a linter or safe language mode and address its warnings; the OpenSSF passing criteria make this a MUST. | decision (single-source) | principle, tooling | single-source, grounded: T1 criteria text | SRC-174 §warnings [T1, admit, unrestricted]; SRC-174 §warnings_fixed [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.VERIFICATION.LINT.1.2` "Baseline rule set" (refines): The recommended rule set is the switched-on analysis for JavaScript. Fate: retargeted here to js-philosophy:VERIFICATION.

Links to other principles of the same graph:

- dataflow from `SUBSET` "Predictable subset" (KEEP): SUBSET defines the safe subset; the linter that is switched on is the mechanism that enforces it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Analysis beyond the compiler

- Origin: node `VERIFICATION.STATIC_BASELINE.2`, child of `VERIFICATION.STATIC_BASELINE` ("Static analysis baseline", SEND). Verdict SEND: Analysis beyond the compiler: language-neutral (OpenSSF criteria).
- Intent: Before a major release at least one static-analysis tool beyond compiler warnings has run, because compilers answer a narrower question than analyzers.
- Constraints: 
  - MUST apply at least one static-analysis tool beyond compiler warnings and safe modes to every proposed major production release before it ships.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C21 | Apply at least one static-analysis tool beyond compiler warnings to every proposed major production release. | decision (single-source) | principle, tooling | single-source, grounded | SRC-174 §static_analysis [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Checks complement each other

- Origin: node `VERIFICATION.STATIC_BASELINE.3`, child of `VERIFICATION.STATIC_BASELINE` ("Static analysis baseline", SEND). Verdict SEND: Checks complement each other: language-neutral (2015 web measurement, OpenSSF).
- Intent: Several kinds of check run together and none is the only mechanism, with negative tests for what must not happen, because each class finds defects the others miss.
- Constraints: 
  - MUST combine several analysis tools in CI but never as the only mechanism, and write negative tests (what must not happen does not) so a passing suite means shipping. Held as the OpenSSF Best Practices Working Group's position.
- Design notes: 
  - Fact [single-source]: Dynamic checks find bad practices that static lint misses: on 200+ web sites in 2015, 28 dynamic checkers detected on average 49 problems per site that static analysis missed. Evidence of occurrence in 2015, not a current-language claim.
- Epistemic state: known | unvalidated: single T2 evidence, 2015 sites

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| LANG-C56 | Dynamic checks find bad practices that static lint misses and the two complement each other: 28 checkers detected on average 49 problems per site that static analysis missed, on over 200 sites in 2015. | fact (single-source) | principle, tooling | single-source, grounded | SRC-237 §Abstract and introduction [T2, admit-restricted, restricted to: Evidence that the named practices occur and cause visible bugs on 200+ sites in 2015; the 28 checkers must be read in the paper; no current-language claim] |
| QUALITY-C23 | Combine several analysis tools in CI, but not as the only mechanism, and write negative tests (what should not happen does not) so that passing the suite means shipping. | decision (single-source) | principle, tooling | single-source, grounded as the OpenSSF Best Practices WG's position | SRC-163 §Automated tests [T1, admit-restricted, restricted to: OpenSSF Best Practices WG recommendations as that body's positions; the claim that a ~3-day cooldown counters most malicious releases needs its origin before use]; SRC-163 §Static analysis [T1, admit-restricted, restricted to: OpenSSF Best Practices WG recommendations as that body's positions; the claim that a ~3-day cooldown counters most malicious releases needs its origin before use] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.VERIFICATION.LINT.3` "Security findings triage" (refines): Security lint output is one analysis class among several, never the sole mechanism. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `VERIFICATION.TEST_SUITE.1` "Tests for new functionality" (SEND): Static analysis is never the only mechanism, so the test policy must exist beside it.
- refines from `CONTRACTS.STATIC.2` "A passing check is evidence, not proof" (KEEP): A passing type check is evidence, not proof: the type layer is the instance of the rule that several kinds of check run together and none is the only mechanism.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Tests for new functionality

- Origin: node `VERIFICATION.TEST_SUITE.1`, child of `VERIFICATION.TEST_SUITE` ("Test suite", SEND). Verdict SEND: Tests for new functionality: language-neutral (OpenSSF criteria).
- Intent: A written policy requires automated tests for new major functionality, evidence shows it is followed, and the suite runs in the language's standard way, so that a change cannot ship unverified.
- Constraints: 
  - MUST keep a policy that new major functionality gets automated tests, keep evidence that recent major changes followed it, and make the suite invocable in the language's standard way.
- Design notes: none.
- Epistemic state: known | unvalidated: rests on single-source claims only

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C22 | Keep a policy that new major functionality gets automated tests, and keep evidence that recent major changes followed it; make the suite invocable in the language's standard way. | decision (single-source) | principle, tooling | single-source, grounded | SRC-174 §test_policy [T1, admit, unrestricted]; SRC-174 §tests_are_added [T1, admit, unrestricted]; SRC-174 §test_invocation [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- requires from `VERIFICATION.STATIC_BASELINE.3` "Checks complement each other" (SEND): Static analysis is never the only mechanism, so the test policy must exist beside it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Coverage finds, it does not judge

- Origin: node `VERIFICATION.TEST_SUITE.2`, child of `VERIFICATION.TEST_SUITE` ("Test suite", SEND). Verdict SEND: Coverage finds, it does not judge: language-neutral (study of Java suites).
- Intent: Coverage locates code no test executes; it is never a quality target, because executing code is not detecting its faults.
- Constraints: 
  - SHOULD NOT gate on a coverage number or use one as a quality target; use coverage to find under-tested code. Study: correlation with suite effectiveness is low to moderate once suite size is controlled (31,000 suites, five large Java systems); transfer to JavaScript inferred.
- Design notes: 
  - Rejected beliefs: Folklore rejected (restricted verdict, the dissent audit): high coverage means effective tests. Coverage finds code no test executes; it does not show that tests would detect a fault.
  - Fact [-]: Rejected position (OpenSSF passing criteria, T1): cover most or all branches, as a suggestion and not a numeric target; it would win for a project that adopts those criteria, and it is compatible with using coverage to locate code no test executes.
- Epistemic state: known | conflict: OpenSSF passing criteria suggest covering most or all branches, as a suggestion rather than a numeric target | unvalidated: study on Java, transfer inferred

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C36 | Do not use a coverage percentage as a quality target; use coverage to find under-tested code, because its correlation with suite effectiveness is low to moderate once suite size is controlled. | decision (contested) | decision, tooling | contested, grounded for the study (31,000 suites, five large Java systems); transfer to JavaScript inferred | SRC-297 §Abstract [T2, admit-restricted, restricted to: The study's finding for five large Java systems (31,000 suites); transfer to JavaScript recorded as inferred]; SRC-174 §test_most [T1, admit, unrestricted] |

Rows without a claim id (folklore audit or build rows):

- fact: Rejected position (OpenSSF passing criteria, T1): cover most or all branches, as a suggestion and not a numeric target; it would win for a project that adopts those criteria, and it is compatible with using coverage to locate code no test executes.
- rejected: Folklore rejected (restricted verdict, 12_dissent): high coverage means effective tests. Coverage finds code no test executes; it does not show that tests would detect a fault.

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- dataflow from `VERIFICATION.FAULT_DETECTION.1` "Mutation testing" (SEND): The mutation score supplies the adequacy evidence that coverage cannot give.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Test design

- Origin: node `VERIFICATION.TEST_SUITE.3`, child of `VERIFICATION.TEST_SUITE` ("Test suite", SEND). Verdict SEND: Test design: language-neutral (Google testing guidance).
- Intent: Tests exercise behaviour through the public interface, one test per behaviour, with real collaborators wherever they are fast and deterministic, so that tests fail for defects and not for refactoring.
- Constraints: 
  - MUST test behaviours through the public API, one test per behaviour rather than per method, DAMP over DRY. Google's position (T3, single source), taken as the decision for lack of any other admitted position.
  - MUST prefer real objects over mocks when they are fast and deterministic, because brittle tests fail on unrelated changes. Google's position (T3, single source), taken as the decision for lack of any other admitted position.
  - Acceptable only when an organization with Google-like test infrastructure sets a mix: a test mix of about 80% narrow unit tests, 15% medium integration tests and 5% end-to-end (Google's stated practice, not a general rule).
- Design notes: none.
- Epistemic state: risky | unvalidated: holder position only (Google), single T3 source

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C29 | Test behaviours through the public API, one test per behaviour rather than per method, and keep tests DAMP (descriptive and meaningful phrases) over DRY. | decision (single-source) | practice, tooling | single-source, grounded as Google's position, T3, never evidence | SRC-321 §Unit testing [T3, admit-restricted, restricted to: Google's positions (test via public APIs, test behaviours, DAMP over DRY) as Google's, never as evidence] |
| QUALITY-C30 | Prefer real objects over mocks when they are fast and deterministic, because brittle tests fail on unrelated changes that introduce no bug. | decision (single-source) | practice, tooling | single-source, grounded as Google's position only | SRC-321 §Unit testing [T3, admit-restricted, restricted to: Google's positions (test via public APIs, test behaviours, DAMP over DRY) as Google's, never as evidence] |
| QUALITY-C31 | Google's recommended test mix is about 80% narrow unit tests, 15% medium integration tests, 5% end-to-end; it is Google's position, not a general rule. | acceptable-when (single-source) | decision, tooling | single-source, grounded as Google's stated practice | SRC-320 §Test mix [T3, admit-restricted, restricted to: Google's stated practice and its own reported figures (80/15/5 mix, flakiness ~0.15%, value lost near 1%), recorded as Google's position, never as general evidence] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Mutation testing

- Origin: node `VERIFICATION.FAULT_DETECTION.1`, child of `VERIFICATION.FAULT_DETECTION` ("Fault detection power", SEND). Verdict SEND: Mutation testing: language-neutral (claims level: principle, decision).
- Intent: Detection power is measured by seeding small faults and counting how many tests kill, and the cost stays bounded by mutating only changed code at review.
- Constraints: 
  - MUST run mutation testing incrementally on changed code during code review and filter mutants, instead of mutating the whole code base, when adopting it at scale. Abstract-level source, Google setting (24,000+ developers, 1,000+ projects).
- Design notes: 
  - Fact [consensus]: A mutation score is the share of injected faults that tests kill: mutation analysis measures whether tests detect small seeded changes, which coverage cannot show.
- Epistemic state: known | unvalidated: single T2 source, abstract-level

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C37 | Read a mutation score as the share of injected faults that tests kill: mutation analysis measures whether tests detect small seeded changes, which coverage cannot show. | fact (consensus) | principle, tooling | consensus, grounded for definitions (T1 restricted tool facts plus T2 abstract) | SRC-179 §Introduction [T1, admit-restricted, restricted to: Facts about StrykerJS's own behaviour only; its coverage analogy (docs root) is a position, not evidence]; SRC-299 §Abstract [T2, admit-restricted, restricted to: Abstract-level facts only (incremental mutation at code review, filtering, 24,000+ developers, 1,000+ projects) until the full text is read; Google setting] |
| QUALITY-C38 | When adopting mutation testing at scale, run it incrementally on changed code during code review and filter mutants, instead of mutating the whole code base. | decision (single-source) | decision, tooling | single-source, grounded at abstract level only, Google setting (24,000+ developers, 1,000+ projects) | SRC-299 §Abstract [T2, admit-restricted, restricted to: Abstract-level facts only (incremental mutation at code review, filtering, 24,000+ developers, 1,000+ projects) until the full text is read; Google setting] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to other principles of the same graph:

- dataflow to `VERIFICATION.TEST_SUITE.2` "Coverage finds, it does not judge" (SEND): The mutation score supplies the adequacy evidence that coverage cannot give.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Property-based testing

- Origin: node `VERIFICATION.FAULT_DETECTION.2`, child of `VERIFICATION.FAULT_DETECTION` ("Fault detection power", SEND). Verdict SEND: Property-based testing: language-neutral (QuickCheck authors).
- Intent: Behaviour is also probed with generated inputs against stated properties, with data distributions that follow real data.
- Constraints: 
  - MUST control the distribution of generated test data with custom generators: random testing is most effective when the distribution follows actual data, and a uniform distribution is often a poor default.
  - Acceptable only when a team wants properties beside the code: write properties in the same module as the functions they test, as checkable documentation (the QuickCheck authors' practice, outside the method the source is admitted for).
- Design notes: 
  - Fact [consensus]: Property-based testing replaces hand-picked inputs with generated ones: a property is a checkable statement, inputs are generated at random, failures are shrunk to the smallest reproducing input (shrinking is fast-check's, absent from the QuickCheck paper).
- Epistemic state: known | unvalidated: single T2 source | unvalidated: rests on claims marked inferred or open (QUALITY-C41)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C39 | Property-based testing replaces hand-picked inputs with generated ones: a property is a checkable statement, inputs are generated at random, and failures are shrunk to the smallest reproducing input (shrinking is fast-check's, not in the QuickCheck paper). | fact (consensus) | principle, tooling | consensus, grounded for the concept; shrinking only on SRC-168 | SRC-168 §Introduction [T1, admit-restricted, restricted to: Facts about fast-check's own behaviour (generation, shrinking, seed and path replay); never grounds that property-based testing beats example tests]; SRC-300 §Abstract and Introduction [T2, admit-restricted, restricted to: Origin of the concept and method of property-based testing (properties, random generation, custom generators) only; not shrinking (absent from this paper), not JavaScript tooling] |
| QUALITY-C40 | Control the distribution of generated test data with custom generators: random testing is most effective when the distribution follows actual data, and a uniform distribution is often a poor default. | decision (single-source) | practice, tooling | single-source, grounded | SRC-300 §Introduction [T2, admit-restricted, restricted to: Origin of the concept and method of property-based testing (properties, random generation, custom generators) only; not shrinking (absent from this paper), not JavaScript tooling] |
| QUALITY-C41 | Properties double as checkable documentation, so write them beside the code they test. | acceptable-when (single-source) | practice, tooling | single-source, grounded for the authors' practice, T2; JavaScript use inferred | SRC-300 §Introduction [T2, admit-restricted, restricted to: Origin of the concept and method of property-based testing (properties, random generation, custom generators) only; not shrinking (absent from this paper), not JavaScript tooling] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### New tests are probed

- Origin: node `VERIFICATION.TEST_STABILITY.1`, child of `VERIFICATION.TEST_STABILITY` ("Test stability", SEND). Verdict SEND: Probe new tests: language-neutral.
- Intent: A new test is run many times when added, because flakiness shows from the first run and arises mostly from waits, concurrency and order.
- Constraints: 
  - MUST check new tests extensively when they are added: flaky tests come mostly from async waits (45% of studied fixes), concurrency and test-order dependency, and are flaky from the first run. Study of 201 commits in 51 mostly Java projects; transfer inferred.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source, transfer inferred

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C33 | Expect flaky tests to come mostly from async waits, concurrency and test-order dependency, and to be flaky from the first run, so check new tests extensively when they are added. | decision (single-source) | principle, tooling | single-source, grounded for 201 commits in 51 mostly Java projects; transfer to JavaScript inferred | SRC-296 §Findings F.1 F.2 [T2, admit-restricted, restricted to: Root-cause taxonomy and fix strategies from 201 commits in 51 Apache projects (mostly Java); transfer to JavaScript inferred] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.VERIFICATION.TESTS.3` "Condition waits" (refines): Condition waits remove the largest flake category in asynchronous JavaScript tests (inferred transfer). Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Shared state is cleaned

- Origin: node `VERIFICATION.TEST_STABILITY.2`, child of `VERIFICATION.TEST_STABILITY` ("Test stability", SEND). Verdict SEND: Clean shared state between tests: language-neutral.
- Intent: Tests do not leak state to each other, because order dependence is the second flake cause and cleaning the state is its usual fix.
- Constraints: 
  - MUST clean the shared state between tests: 74% (14 of 19) of order-dependent flaky tests in the study were fixed that way. Java-dominated study; transfer inferred.
- Design notes: none.
- Epistemic state: known | unvalidated: single T2 source, transfer inferred

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C35 | Clean the shared state between tests, because 74% (14 of 19) of order-dependent flaky tests in the study were fixed that way. | decision (single-source) | practice, tooling | single-source, grounded for the study; transfer to JavaScript inferred | SRC-296 §Finding F.10 [T2, admit-restricted, restricted to: Root-cause taxonomy and fix strategies from 201 commits in 51 Apache projects (mostly Java); transfer to JavaScript inferred] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

#### Flake rate tracked

- Origin: node `VERIFICATION.TEST_STABILITY.3`, child of `VERIFICATION.TEST_STABILITY` ("Test stability", SEND). Verdict SEND: Track the flake rate: language-neutral (Google figures).
- Intent: The flake rate is measured, and a suite approaching 1% flakiness is treated as losing its value and repaired before more is built on it.
- Constraints: 
  - MUST track the flaky-test rate: Google reports about 0.15% and says tests begin to lose value near 1% flakiness; treat approaching 1% as the point to act. Google's figures (T3, single source), the only admitted threshold.
- Design notes: none.
- Epistemic state: risky | unvalidated: holder position only (Google figures), single T3 source

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| QUALITY-C32 | Track the flaky-test rate: Google reports about 0.15% and says tests begin to lose value near 1% flakiness. | decision (single-source) | practice, tooling | single-source, grounded as Google's figures only | SRC-320 §Flaky tests [T3, admit-restricted, restricted to: Google's stated practice and its own reported figures (80/15/5 mix, flakiness ~0.15%, value lost near 1%), recorded as Google's position, never as general evidence] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Branch RUNTIME: Runtime behaviour

#### Measurement before belief

- Origin: node `RUNTIME.MEASURE`, child of `RUNTIME` ("Runtime behaviour", SPLIT). Verdict SEND: Measurement before belief: holds for any language and engine (claim level: principle).
- Intent: A performance or memory belief becomes a rule only through a measurement on the real workload; advice that rests on engine internals is dated evidence that may describe a mechanism but does not prescribe.
- Constraints: 
  - MUST treat performance advice that rests on engine internals as dated single-body evidence that can describe a mechanism but cannot prescribe (no T1 specifies engine performance); make a performance belief a rule only through a measurement of the real workload.
- Design notes: none.
- Epistemic state: known | conflict: restructuring for speed on mechanism alone, MDN (SRC-083, SRC-088) | unvalidated: the rule is inferred from SRC-195 and SRC-302, no source states it normatively; C63 single T2 body | unvalidated: quote not obtained (RUNTIME-C63)

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNTIME-C63 | Treat engine-internals performance advice from V8 posts (2017 to 2019) as dated single-body evidence: it rests on one team, is restricted by date, and no T1 specifies engine internals. | decision (single-source) | principle, node | single-source, inferred | SRC-301 §Concurrent marking [T2, admit-restricted, restricted to: Mechanism and 65%/70% marking-time reduction as of 2018 (default since Node.js v10)]; SRC-302 §Elements kinds [T2, admit-restricted, restricted to: Mechanism plus its measured statement that the holey vs packed difference is "usually too small to matter or even be measurable"; the tips are the holder's opinion]; SRC-303 §Fast properties [T2, admit-restricted, restricted to: Mechanism (hidden classes, dictionary mode, inline caches) as of 2017; no performance prescriptions, since no measurement is given]; SRC-308 §Orinoco [T2, admit-restricted, restricted to: GC mechanism and the 20-50% young-generation figure as of 2019] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.RUNTIME.MEASURE.1` "Profile before optimizing" (refines): Profiling is the first concrete way a belief becomes a measurement. Fate: removed from the graph, planned link to this node.
- `PIG-JS.RUNTIME.MEASURE.2` "Engine-level tuning needs a measurement" (refines): Engine-level advice is held as a hypothesis until measured. Fate: removed from the graph, planned link to this node.
- `PIG-JS.RUNTIME.MEASURE.3` "Callback file APIs only on a measured need" (refines): A speed-motivated API swap waits for a measured need. Fate: removed from the graph, planned link to this node.
- `PIG-JS.RUNTIME.DIAGNOSE` "Diagnosis of a running process" (refines): Diagnosis gathers the evidence that belief is not allowed to replace. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires to `RUNTIME.METHOD` "Measurement method" (SEND): A measurement that turns a belief into a rule is only as good as the method that produced it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:INTENTIONALITY`: A speed or memory change must answer why this and not something else, and the answer is a measurement.

#### Measurement method

- Origin: node `RUNTIME.METHOD`, child of `RUNTIME` ("Runtime behaviour", SPLIT). Verdict SEND: Performance as a distribution: language-neutral (measurements on Java and C, transfer inferred).
- Intent: A measurement is trustworthy only when it treats performance as a distribution: separated start-up and steady state, confidence intervals and a varied setup, so that noise and setup bias cannot flip the conclusion.
- Constraints: 
  - MUST measure performance as a distribution, not a number: report start-up and steady state separately across several fresh VM invocations with several iterations each, give confidence intervals, and vary the experimental setup, because an innocuous setup change can bias results and flip conclusions.
- Design notes: none.
- Epistemic state: known | unvalidated: transfer from Java and C measurements to JavaScript is inferred

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| RUNTIME-C61 | Report start-up and steady-state performance separately, using several fresh VM invocations with several iterations each, and give confidence intervals instead of one number. | decision (single-source (two independent T2)) | practice, tooling | single-source, grounded | SRC-307 §Abstract [T2, admit-restricted, restricted to: Method (confidence intervals; separate start-up and steady-state measurement across VM invocations and iterations); no Java numbers transferred]; SRC-307 §Statistically rigorous methodology [T2, admit-restricted, restricted to: Method (confidence intervals; separate start-up and steady-state measurement across VM invocations and iterations); no Java numbers transferred] |
| RUNTIME-C62 | Vary the experimental setup (setup randomization) when comparing performance, because an innocuous setup change can bias results and flip conclusions. | decision (single-source (two independent T2)) | practice, tooling | single-source, grounded | SRC-305 §Abstract [T2, admit-restricted, restricted to: Abstract-level claims only (measurement bias from setup, setup randomization); measured on SPEC CPU2006 C programs] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.RUNTIME.METHOD.1` "Compare runs statistically" (refines): Many runs and a significance test make the distribution explicit. Fate: removed from the graph, planned link to this node.
- `PIG-JS.RUNTIME.METHOD.2` "Quiet measurement environment" (refines): A controlled environment removes setup noise. Fate: removed from the graph, planned link to this node.

Links to other principles of the same graph:

- requires from `RUNTIME.MEASURE` "Measurement before belief" (SEND): A measurement that turns a belief into a rule is only as good as the method that produced it.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:REPRODUCIBILITY`: A measurement counts when the same setup and process reproduce it, with its variation reported.

## Part B: general parts of nodes that stay narrowed

### Contracts (general part)

- Origin: general part of node `CONTRACTS` ("Contracts"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): the build-time type layer of a language without run-time types stays; boundary parsing and call shape go.
- Travels with: `CONTRACTS.BOUNDARY` (Boundary contract), `CONTRACTS.SHAPE` (Shape of calls).
- Intent: Make intent checkable at run time by parsing untrusted data at every trust boundary, and in the shape of functions and objects, so that a violated expectation is reported where it arises and not discovered downstream.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Structure for locality of change (general part)

- Origin: general part of node `STRUCTURE` ("Structure for locality of change"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): only the exported-state part is JavaScript-specific; hiding, purity, direction, naming and paradigm go.
- Travels with: `STRUCTURE.HIDING` (Hide likely-to-change decisions), `STRUCTURE.PURITY` (Effect-free importing), `STRUCTURE.DIRECTION` (Dependencies flow one way), `STRUCTURE.NAMING` (Names carry the concept), `STRUCTURE.PARADIGM` (Paradigm by intent).
- Intent: Organize code so that a change touches one place: decisions hidden behind module boundaries, each piece of state in one place, importing free of hidden effects, dependencies that flow one way, names that carry their concept, paradigm chosen by intent.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known | gap: layering principle undecided (STRUCTURE.DIRECTION.2)`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### State in one place (general part)

- Origin: general part of node `STRUCTURE.STATE` ("State in one place"), which stays in the JavaScript guideline in narrowed form. Why split: Keeps the JavaScript part (what a module exports is state shared by all importers); the general part (one place per piece of state) goes.
- Travels with: `STRUCTURE.STATE.1` (One place per piece of state).
- Intent: Keep each piece of state in one place.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- refines `python-kb-philosophy:DATACENTRICITY`: Keeping state in one place is the data-stability principle applied to application state (inferred).

### Defense (general part)

- Origin: general part of node `DEFENSE` ("Defense"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): the page, origin, prototype and process parts follow from JavaScript's runtime; the injection family and secrets go.
- Travels with: `DEFENSE.INJECTION` (Data becoming instruction or location), `DEFENSE.SECRETS` (Secrets and cryptographic primitives).
- Intent: Every sink that interprets data as code, query, path, destination or serialized object is dangerous, secrets are drawn, compared, stored and logged only through audited mechanisms, hostile data is narrowed at each sink, and what slips through is contained by a second layer.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE` "Defense defaults" (refines): The default renders the principle in JavaScript. Fate: kept on the narrowed node.

Links to other principles of the same graph:

- requires to `CONTRACTS.BOUNDARY.1` "Validate at every trust boundary" (SEND): Treating every input as hostile in DEFENSE presupposes that inputs are parsed at the boundary here

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Two parsers must agree (general part)

- Origin: general part of node `DEFENSE.HOST.3` ("Two parsers must agree"), which stays in the JavaScript guideline in narrowed form. Why split: Keeps the runtime's position (spec-consistent parsing is not its flaw, claim level: js-principle); the parser-differential and CR, LF, NUL rule (claim level: principle) goes.
- Intent: Where a proxy and a server read the same bytes, any disagreement is an attack; the defence belongs at both parsers. A control character in a header value is such a disagreement.
- Constraints: 
  - MUST NOT let CR, LF or NUL reach an HTTP field value: they are invalid and dangerous, and a recipient must reject the message or replace each with a space.
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known | unvalidated: rests on single-source claims only`

Claims:

| id | claim text | placed as | level, stack | agreement, certainty | sources (register tier, verdict, restriction) |
|---|---|---|---|---|---|
| SECGAP2-C23 | Never let CR, LF or NUL reach an HTTP field value: they are invalid and dangerous, and a recipient must reject the message or replace each with a space. | decision (single-source) | principle, node | single-source, grounded | SRC-374 §5.5 [T1, admit, unrestricted] |

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- `PIG-JS.DEFENSE.HOST.3` "HTTP parsing and smuggling" (refines): The default renders the principle in JavaScript. Fate: kept on the narrowed node.
- `PIG-JS.DEFENSE.HOST.3.1` "Header field values" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.
- `PIG-JS.DEFENSE.HOST.3.2` "Connection-specific fields" (refines): The default renders the principle in JavaScript. Fate: removed from the graph, planned link to this node.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Dependencies (general part)

- Origin: general part of node `DEPENDENCIES` ("Dependencies"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): the npm graph as attack surface stays; sourcing hygiene, updates and publishing hardening go.
- Travels with: `DEPENDENCIES.PUBLISH` (Publishing).
- Intent: Each dependency is a trust decision: few in number, adopted only after need and identity are checked, updated through an automated mechanism, and the accounts that publish one's own packages are hardened.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Admission (general part)

- Origin: general part of node `DEPENDENCIES.ADMISSION` ("Admission"), which stays in the JavaScript guideline in narrowed form. Why split: Keeps maintenance and install-time behaviour (npm facts); need, identity and documentation checks are sourcing and go.
- Travels with: `DEPENDENCIES.ADMISSION.1` (Existing components first), `DEPENDENCIES.ADMISSION.3` (Identity of the package), `DEPENDENCIES.ADMISSION.4` (Documentation examples are untrusted).
- Intent: A package enters only when its need, its identity and its documentation have each been checked, and existing components are considered first.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Verification (general part)

- Origin: general part of node `VERIFICATION` ("Verification"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): only the tie between the checked subset, the type layer and the merge gate is JavaScript-specific; everything else goes.
- Travels with: `VERIFICATION.STATIC_BASELINE` (Static analysis baseline), `VERIFICATION.TEST_SUITE` (Test suite), `VERIFICATION.FAULT_DETECTION` (Fault detection power), `VERIFICATION.TEST_STABILITY` (Test stability), `VERIFICATION.ENFORCEMENT` (Enforcement at the merge).
- Intent: Defects that people forget to look for are found by machines, on every change, with a result that blocks the change and that people trust.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

### Runtime behaviour (general part)

- Origin: general part of node `RUNTIME` ("Runtime behaviour"), which stays in the JavaScript guideline in narrowed form. Why split: Shared cut (L1): the memory model of the collector stays; measurement before belief and method go.
- Travels with: `RUNTIME.MEASURE` (Measurement before belief), `RUNTIME.METHOD` (Measurement method).
- Intent: Code stays well behaved under load because its speed is established by measurement of the real workload, never by belief or by engine folklore.
- Constraints: none (no decision row of its own).
- Design notes: none.
- Epistemic state: inferred (a part carved out at the split); the node it came from was `known | unvalidated: most grounds are single-source`

Claims:

_No claim of its own._

Defaults nodes (`pig-js-defaults`, the JavaScript rules) that relied on it:

- none.

Links to the Python guideline's principles (`python-kb-philosophy`):

- none.

## Removed links between a sent node and a node that stays

These principle-to-principle links (type, from, to, sentence) were removed from the JavaScript guideline because one end left. Each is a candidate link from the software guideline's node to the JavaScript guideline's remaining node.

- requires `SUBSET.STATE` "Distinguished immutability" (SEND) to `SUBSET.FAILURE` "Loud failure" (KEEP): A lock on state protects only as far as a write to it fails loudly.
- requires `CONTRACTS.BOUNDARY.1` "Validate at every trust boundary" (SEND) to `CONTRACTS.STATIC.1` "Types attest nothing at run time" (KEEP): Because a type layer attests nothing about arriving data, the boundary check is what gives the types their truth
- refines `CONTRACTS.BOUNDARY.2` "Accept by positive rule" (SEND) to `CONTRACTS.BOUNDARY.4` "Input handling is a recognizer" (SEND): A positive rule is a recognizer for a simple input language; complex languages need a real parser, not a pattern list
- requires `CONTRACTS.STATIC.2` "A passing check is evidence, not proof" (KEEP) to `CONTRACTS.BOUNDARY.1` "Validate at every trust boundary" (SEND): Since a passing check is not proof, run-time validation stays in place even in fully typed code
- dataflow `CONTROL.FAILURE` "Failure has an owner" (KEEP) to `CONTROL.LIFECYCLE` "Process end is designed" (SEND): A failure no owner can repair flows to the lifecycle, which decides how the process ends.
- requires `STRUCTURE.HIDING.3` "Minimal public surface" (SEND) to `STRUCTURE.HIDING.1` "Decompose by hidden decisions" (SEND): A decision stays hidden only if the surface that exposes the module stays minimal.
- requires `STRUCTURE.STATE.2` "Exported state is shared state" (KEEP) to `STRUCTURE.HIDING.3` "Minimal public surface" (SEND): Exported state is part of a module's surface, so sharing it widens the surface that must stay minimal.
- refines `STRUCTURE.PURITY` "Effect-free importing" (SEND) to `STRUCTURE.DIRECTION.1` "No cycles between modules" (SEND): A module with no import-time effects cannot trip over an uninitialised binding in a cycle, which lowers the cost of a cycle that slips in (inferred from the cycle mechanism).
- requires `STRUCTURE.PARADIGM` "Paradigm by intent" (SEND) to `STRUCTURE.HIDING.2` "Abstract data type versus object" (SEND): Choosing a paradigm per problem presupposes knowing what each hides: objects hide by procedural interface, data types by operations over a hidden representation.
- requires `DEFENSE.INJECTION.5` "Serialized data carries no behaviour" (SEND) to `DEFENSE.INJECTION.1` "Strings never become code" (SEND): Reviving types or functions from serialized data is building code from strings, so the code rule must hold first.
- dataflow `DEFENSE.PROTOTYPE.2` "Pollution can be code execution" (KEEP) to `DEFENSE.INJECTION.1` "Strings never become code" (SEND): A polluted shared prototype feeds gadgets that compile or run attacker-shaped values, ending in code execution.
- requires `DEPENDENCIES.TRUST.1` "Every dependency is trusted code" (KEEP) to `DEPENDENCIES.ADMISSION.1` "Existing components first" (SEND): Because every dependency is trusted code, each addition must first earn its trust cost.
- requires `DEPENDENCIES.TRUST.2` "No containment inside the process" (KEEP) to `DEPENDENCIES.TRUST.3` "Layered controls" (SEND): With no containment inside the process, protection can only come from stacked controls.
- requires `DEPENDENCIES.THREATS.2` "Confusion is many mechanisms" (KEEP) to `DEPENDENCIES.ADMISSION.3` "Identity of the package" (SEND): Confusion mechanisms are what the identity check has to cover.
- dataflow `DEPENDENCIES.EVIDENCE.2` "Audit findings" (KEEP) to `DEPENDENCIES.CHANGE.4` "Updates" (SEND): Triaged findings feed the update mechanism, which keeps security updates separate.
- requires `DEPENDENCIES.CHANGE.5` "Incident response" (SEND) to `DEPENDENCIES.CHANGE.1` "Reproducible tree" (KEEP): Pinning to pre-incident versions presupposes a tree fixed by the lockfile.
- requires `DEPENDENCIES.PUBLISH` "Publishing" (SEND) to `DEPENDENCIES.THREATS.1` "Takeover of maintainership" (KEEP): Publishing accounts are the takeover route that has to be hardened.
- dataflow `DEPENDENCIES.EVIDENCE.1` "Provenance and signatures" (KEEP) to `DEPENDENCIES.ADMISSION.3` "Identity of the package" (SEND): Origin evidence supports the authenticity check without replacing it.
- requires `VERIFICATION.STATIC_BASELINE` "Static analysis baseline" (SEND) to `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND): An analysis finding is acted on only when the gate blocks the change that carries it.
- requires `VERIFICATION.TEST_SUITE` "Test suite" (SEND) to `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND): A test policy has effect only when a failing suite stops the merge.
- requires `VERIFICATION.TEST_SUITE` "Test suite" (SEND) to `VERIFICATION.TEST_STABILITY` "Test stability" (SEND): A suite is a trusted signal only while its failures mean defects.
- dataflow `VERIFICATION.FAULT_DETECTION.1` "Mutation testing" (SEND) to `VERIFICATION.TEST_SUITE.2` "Coverage finds, it does not judge" (SEND): The mutation score supplies the adequacy evidence that coverage cannot give.
- requires `VERIFICATION.STATIC_BASELINE.3` "Checks complement each other" (SEND) to `VERIFICATION.TEST_SUITE.1` "Tests for new functionality" (SEND): Static analysis is never the only mechanism, so the test policy must exist beside it.
- requires `RUNTIME.MEASURE` "Measurement before belief" (SEND) to `RUNTIME.METHOD` "Measurement method" (SEND): A measurement that turns a belief into a rule is only as good as the method that produced it.
- requires `SUBSET.VISIBLE` "Visible conversion" (KEEP) to `CONTRACTS.BOUNDARY` "Boundary contract" (SEND): What an expression does follows from the declared kind of its operands; for data from outside, that kind is established by parsing at the boundary.
- requires `DEFENSE` "Defense" (SPLIT) to `CONTRACTS.BOUNDARY.1` "Validate at every trust boundary" (SEND): Treating every input as hostile in DEFENSE presupposes that inputs are parsed at the boundary here
- refines `DEFENSE.INJECTION` "Data becoming instruction or location" (SEND) to `CONTRACTS.BOUNDARY.2` "Accept by positive rule" (SEND): Positive validation is the language-neutral form of the allowlist stance DEFENSE takes toward sinks and injection
- requires `CONTRACTS.STATIC.1` "Types attest nothing at run time" (KEEP) to `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND): A type layer is a contract only while a tool checks it in the build and in CI, which VERIFICATION gates
- refines `CONTRACTS.SHAPE` "Shape of calls" (SEND) to `STRUCTURE.NAMING` "Names carry the concept" (SEND): Call shapes are the smallest unit of the interface design STRUCTURE governs
- requires `STRUCTURE.STATE.2` "Exported state is shared state" (KEEP) to `SUBSET.STATE` "Distinguished immutability" (SEND): Freezing is shallow and does not make nested data immutable; the freeze mechanics are owned by SUBSET (group freeze-shallow).
- requires `DEPENDENCIES.TRUST.1` "Every dependency is trusted code" (KEEP) to `DEFENSE.INJECTION` "Data becoming instruction or location" (SEND): Injection sinks that dependencies carry (eval, exec) are the subject of DEFENSE.
- requires `DEPENDENCIES.ADMISSION.4` "Documentation examples are untrusted" (SEND) to `DEFENSE.DOM.1` "Sources and sinks" (KEEP): README examples that reach DOM or injection sinks are reviewed under DEFENSE rules.
- requires `VERIFICATION.ENFORCEMENT` "Enforcement at the merge" (SEND) to `DEPENDENCIES.CHANGE.1` "Reproducible tree" (KEEP): The gate job includes the reproducible install step that DEPENDENCIES decides (QUALITY-C42 is routed there).
- dataflow `SUBSET` "Predictable subset" (KEEP) to `VERIFICATION.STATIC_BASELINE.1` "Analysis switched on" (SEND): SUBSET defines the safe subset; the linter that is switched on is the mechanism that enforces it.
- refines `CONTRACTS.STATIC.2` "A passing check is evidence, not proof" (KEEP) to `VERIFICATION.STATIC_BASELINE.3` "Checks complement each other" (SEND): A passing type check is evidence, not proof: the type layer is the instance of the rule that several kinds of check run together and none is the only mechanism.

## Planned link to the web-architecture guideline that moves with a sent node

- From `CONTRACTS.BOUNDARY.1` to `web-app-philosophy`: server-side authority for validation is architecture owned by the web-architecture guideline (row CONTRACTS-006, deferred)

## Sources cited above

| src | tier | verdict | title | url | restriction |
|---|---|---|---|---|---|
| SRC-039 | T1 | admit | OWASP ASVS 5.0.0, V2 Validation and Business Logic | https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/en/0x11-V2-Validation-and-Business-Logic.md | - |
| SRC-053 | T1 | admit-restricted | OWASP Input Validation Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | unrestricted for 02_types; 06_runsec: Regex-safety statements only (bound length, non-backtracking engine or timeout, timeout as failure), each cross-checked against K20 |
| SRC-078 | T1 | admit-restricted | Node.js Security Best Practices (supply chain section) | https://nodejs.org/en/learn/getting-started/security-best-practices | unrestricted for 03_async, 06_runsec; 07_supply: attack-vector list and mitigations not superseded by npm 12 docs; ignore-scripts advice applies to npm before v12 only; the Socket mention never grounds a tool choice |
| SRC-084 | T1 | admit-restricted | ESLint rule max-params | https://eslint.org/docs/latest/rules/max-params | rule behaviour and stated rationale (memorising order and types); the default of 3 is a configuration default, not evidence |
| SRC-085 | T1 | admit-restricted | ESLint rule no-restricted-imports | https://eslint.org/docs/latest/rules/no-restricted-imports | the mechanism for forbidding imports by name or pattern; grounds no layering principle |
| SRC-087 | T1 | admit | import statement (MDN reference) | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import | - |
| SRC-089 | T1 | admit | Node.js CommonJS modules | https://nodejs.org/api/modules.html | - |
| SRC-090 | T1 | admit | Node.js packages | https://nodejs.org/api/packages.html | - |
| SRC-091 | T1 | admit | Private elements (MDN reference) | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements | - |
| SRC-095 | T1 | admit-restricted | webpack Tree Shaking guide | https://webpack.js.org/guides/tree-shaking/ | webpack's own behaviour for the sideEffects field and pure annotations; not a language or Node rule (Node ignores the field, STRUCT-K06); never a ground for preferring webpack |
| SRC-123 | T1 | admit | eval() (MDN) | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval | - |
| SRC-124 | T1 | admit | Function() constructor (MDN) | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function | - |
| SRC-132 | T1 | admit-restricted | OWASP ASVS 5.0 | https://github.com/OWASP/ASVS/tree/master/5.0/en | Verification requirements only; read: 5.3.2 (file paths), 5.4.1, 15.3.6 (prototype pollution, Set or Map), 15.1.5 (dangerous functionality incl. deserialization); mechanisms come from another T1 |
| SRC-133 | T1 | admit-restricted | OWASP Deserialization Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html | Language-neutral principles only; JavaScript not covered (PHP, Python, Java, .NET) |
| SRC-134 | T1 | admit | OWASP JavaScript and TypeScript Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/JavaScript_and_TypeScript_Security_Cheat_Sheet.html | - |
| SRC-135 | T1 | admit-restricted | OWASP NodeJS Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html | Statements on Node core API risks only (eval, child_process.exec, ReDoS, path traversal); its third-party npm package recommendations are excluded |
| SRC-136 | T1 | admit-restricted | OWASP OS Command Injection Defense Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html | Principles only (avoid shell, parameterize, allowlist); examples are Java, .NET, PHP |
| SRC-138 | T1 | admit-restricted | OWASP Secrets Management Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | Language-neutral principles only (no hardcoded secrets, env variables as weaker option, pre-commit detection); no JavaScript-specific claim |
| SRC-144 | T1 | admit | Concise Guide for Evaluating Open Source Software | https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software | - |
| SRC-154 | T1 | admit-restricted | OpenSSF npm Best Practices Guide v1.1 | https://github.com/ossf/package-manager-best-practices/blob/main/published/npm.md | items not superseded by npm 12 docs (K05 to K08), recorded as archived 2023 guidance; shrinkwrap items excluded; no provenance coverage |
| SRC-155 | T1 | admit-restricted | OWASP NPM Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html | mitigation items not superseded by npm 12 docs; named tools (Snyk, LavaMoat, Verdaccio) never ground a tool choice; ignore-scripts advice applies to npm before v12 |
| SRC-161 | T1 | admit-restricted | OpenSSF Scorecard checks | https://github.com/ossf/scorecard/blob/main/docs/checks.md | 07_supply: facts about what each check detects and its stated limits (GitHub-only checks, false negatives); a score is never evidence a package is safe; 08_quality: Facts about what Scorecard checks and how it rates risk; presence of a check grounds "Scorecard rewards X", not that X is effective |
| SRC-163 | T1 | admit-restricted | Concise Guide for Developing More Secure Software | https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software | OpenSSF Best Practices WG recommendations as that body's positions; the claim that a ~3-day cooldown counters most malicious releases needs its origin before use |
| SRC-168 | T1 | admit-restricted | fast-check documentation and repository | https://fast-check.dev/docs/introduction/ | Facts about fast-check's own behaviour (generation, shrinking, seed and path replay); never grounds that property-based testing beats example tests |
| SRC-169 | T1 | admit-restricted | GitHub Docs: About protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | Facts about GitHub's own platform (required status checks, required reviews) |
| SRC-174 | T1 | admit | OpenSSF Best Practices Badge criteria (passing) | https://www.bestpractices.dev/en/criteria/0 | - |
| SRC-179 | T1 | admit-restricted | StrykerJS introduction | https://stryker-mutator.io/docs/stryker-js/introduction/ | Facts about StrykerJS's own behaviour only; its coverage analogy (docs root) is a position, not evidence |
| SRC-236 | T2 | admit-restricted | Goldberg, What Every Computer Scientist Should Know About Floating-Point Arithmetic (ACM Computing Surveys, March 1991) | https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html | Floating-point mechanism (rounding error, NaN, signed zero, epsilon) from the 1991 paper; not the reprinter's added sections; no JavaScript-specific rule |
| SRC-237 | T2 | admit-restricted | Gong, Pradel, Sridharan, Sen, DLint: Dynamically Checking Bad Coding Practices in JavaScript (ISSTA 2015) | https://www2.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-5.html | Evidence that the named practices occur and cause visible bugs on 200+ sites in 2015; the 28 checkers must be read in the paper; no current-language claim |
| SRC-239 | T2 | admit-restricted | Google JavaScript Style Guide | https://google.github.io/styleguide/jsguide.html | 01_lang: Positions of the Google JS guide only, as frozen; where the Google TS guide (TYPES-K16) covers the same point, cite that one; 03_async: Google's positions only (throw only Error objects; a no-op catch must explain why in a comment), never evidence; 04_struct: Google's positions only (no default exports, no cycles between ES modules, exports not mutated after initialisation, optional trailing underscore for @private), never evidence; 08_quality: Google's positions as of the guide's freeze only; not for tooling choices (clang-format, Closure); superseded where the TS guide differs |
| SRC-242 | T2 | admit-restricted | Sassaman et al., Security Applications of Formal Language Theory (Dartmouth TR2011-709) | https://sergey.cs.dartmouth.edu/langsec/papers/langsec-tr.pdf | The recognizer-before-processing principle as a mechanism and as the authors' position; not JavaScript-specific |
| SRC-244 | T2 | admit-restricted | Google TypeScript Style Guide | https://google.github.io/styleguide/tsguide.html | unrestricted for 08_quality; 02_types: Positions of Google's TS guide only, never evidence; 04_struct: Google's positions with their stated reasons (default exports have no canonical name; export let banned; namespaces banned; interfaces over type literals), never evidence |
| SRC-251 | T2 | admit-restricted | A Large Scale Study of Programming Languages and Code Quality in Github (Ray, Posnett, Filkov, Devanbu) | https://cs.uwaterloo.ca/~m2nagapp/courses/CS846/1189/papers/ray_fse14.pdf | the original finding that language design has a modest effect (functional somewhat better than procedural, strong over weak typing) dominated by process factors; contested by STRUCT-K25 |
| SRC-252 | T2 | admit-restricted | A Relational Model of Data for Large Shared Data Banks (Codd) | https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf | normal form and the redundancy and consistency problem for shared data, as a principle; transfer to in-memory JavaScript application state is inference |
| SRC-253 | T2 | admit-restricted | Exploring Language Support for Immutability | https://www.cs.cmu.edu/~jssunshi/assets/pdf/coblenz2016exploring.pdf | taxonomy of immutability and read-only mechanisms and expert-interview requirements (Java-oriented); no effect evidence; not a JS rule |
| SRC-254 | T2 | admit-restricted | How Developers Choose Names | https://arxiv.org/abs/2103.07487 | the name-agreement finding (median 6.9% over 47 instances, 334 subjects) and the three-step naming model; language of the experiments not yet checked |
| SRC-257 | T2 | admit-restricted | On the Criteria To Be Used in Decomposing Systems into Modules | https://www.cse.sc.edu/~mgv/csce590f20/ParnasCriteria.pdf | information hiding as the decomposition criterion, as a language-agnostic principle; never a JS-specific rule |
| SRC-258 | T2 | admit-restricted | On the Impact of Programming Languages on Code Quality: A Reproduction Study | https://arxiv.org/abs/1901.10220 | language-to-defect associations in GitHub data are small or absent; cited only together with STRUCT-K25o and K33; never a ground for a paradigm choice inside JavaScript |
| SRC-259 | T2 | admit-restricted | On Understanding Data Abstraction, Revisited | https://www.cs.utexas.edu/~wcook/Drafts/2009/essay.pdf | the conceptual distinction between objects and abstract data types; no evidence for choosing either in JavaScript |
| SRC-260 | T2 | admit-restricted | Shorter Identifier Names Take Longer to Comprehend | https://www.se.cs.uni-saarland.de/publications/docs/HoSeHo17.pdf | experimental effect of naming style (72 professional C# developers; words about 19% faster than letters or abbreviations); transfer to JS is inference |
| SRC-261 | T2 | admit-restricted | Web Platform Design Principles | https://www.w3.org/TR/design-principles/ | W3C TAG positions for web platform API design (options dictionaries, optional arguments, naming, constructors only for stateful classes, Promises and AbortSignal); transfer to library and application APIs is inference |
| SRC-272 | T2 | admit-restricted | CWE-22: Path Traversal | https://cwe.mitre.org/data/definitions/22.html | Taxonomy and language-neutral mitigations (canonicalize, allowlist) only |
| SRC-275 | T2 | admit-restricted | How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories | https://www.ndss-symposium.org/ndss-paper/how-bad-can-it-git-characterizing-secret-leakage-in-public-github-repositories/ | Language-neutral evidence with year (over 100,000 repositories, 2019) |
| SRC-281 | T2 | admit | A Qualitative Study of Dependency Management and Its Security Implications | https://research.vu.nl/en/publications/a-qualitative-study-of-dependency-management-and-its-security-imp/ | - |
| SRC-288 | T2 | admit-restricted | Postmortem for Malicious Packages Published on July 12th, 2018 | https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes | incident facts only (password reuse, no 2FA, postinstall token theft, eslint-scope 3.7.2) |
| SRC-291 | T2 | admit | Taxonomy of Attacks on Open-Source Software Supply Chains | https://arxiv.org/abs/2204.04008 | - |
| SRC-295 | T2 | admit-restricted | Widespread Supply Chain Compromise Impacting npm Ecosystem (CISA alert) | https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem | incident facts (Shai-Hulud, 500+ packages, credential-harvesting worm); its recommended actions recorded as CISA's position |
| SRC-296 | T2 | admit-restricted | An Empirical Analysis of Flaky Tests | https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf | Root-cause taxonomy and fix strategies from 201 commits in 51 Apache projects (mostly Java); transfer to JavaScript inferred |
| SRC-297 | T2 | admit-restricted | Coverage Is Not Strongly Correlated with Test Suite Effectiveness | https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf | The study's finding for five large Java systems (31,000 suites); transfer to JavaScript recorded as inferred |
| SRC-299 | T2 | admit-restricted | Practical Mutation Testing at Scale: A View from Google | https://arxiv.org/abs/2102.11378 | Abstract-level facts only (incremental mutation at code review, filtering, 24,000+ developers, 1,000+ projects) until the full text is read; Google setting |
| SRC-300 | T2 | admit-restricted | QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs | https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf | Origin of the concept and method of property-based testing (properties, random generation, custom generators) only; not shrinking (absent from this paper), not JavaScript tooling |
| SRC-301 | T2 | admit-restricted | Concurrent marking in V8 | https://v8.dev/blog/concurrent-marking | Mechanism and 65%/70% marking-time reduction as of 2018 (default since Node.js v10) |
| SRC-302 | T2 | admit-restricted | Elements kinds in V8 | https://v8.dev/blog/elements-kinds | Mechanism plus its measured statement that the holey vs packed difference is "usually too small to matter or even be measurable"; the tips are the holder's opinion |
| SRC-303 | T2 | admit-restricted | Fast properties in V8 | https://v8.dev/blog/fast-properties | Mechanism (hidden classes, dictionary mode, inline caches) as of 2017; no performance prescriptions, since no measurement is given |
| SRC-305 | T2 | admit-restricted | Producing Wrong Data Without Doing Anything Obviously Wrong! | https://sape.inf.usi.ch/publications/asplos09 | Abstract-level claims only (measurement bias from setup, setup randomization); measured on SPEC CPU2006 C programs |
| SRC-307 | T2 | admit-restricted | Statistically Rigorous Java Performance Evaluation | https://dri.es/files/oopsla07-georges.pdf | Method (confidence intervals; separate start-up and steady-state measurement across VM invocations and iterations); no Java numbers transferred |
| SRC-308 | T2 | admit-restricted | Trash talk: the Orinoco garbage collector | https://v8.dev/blog/trash-talk | GC mechanism and the 20-50% young-generation figure as of 2019 |
| SRC-312 | T3 | admit-restricted | Airbnb JavaScript Style Guide | https://github.com/airbnb/javascript | 01_lang: Positions of the Airbnb guide only, never evidence (policy standing rule on popular guides); 04_struct: Airbnb's positions only (10.3 no export directly from an import, 10.6 prefer default export, 23.4 no leading or trailing underscores), never evidence; 08_quality: Positions of the Airbnb guide only, never evidence; its shareable config is not a current tooling route |
| SRC-314 | T3 | admit-restricted | Rebuttal to Berger et al., TOPLAS 2019 | https://arxiv.org/pdf/1911.07393 | the original authors' position in their dispute with STRUCT-K25; not peer-reviewed |
| SRC-319 | T3 | admit-restricted | The case for a cooldown: why Dependabot now waits before issuing version updates | https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/ | GitHub's incident-window figures (21 incidents pulled within hours, about 6,500 npm malware advisories in a year) as the vendor's own analysis, single-source; behaviour facts come from K40o |
| SRC-320 | T3 | admit-restricted | Software Engineering at Google, ch. 11 Testing Overview | https://abseil.io/resources/swe-book/html/ch11.html | Google's stated practice and its own reported figures (80/15/5 mix, flakiness ~0.15%, value lost near 1%), recorded as Google's position, never as general evidence |
| SRC-321 | T3 | admit-restricted | Software Engineering at Google, ch. 12 Unit Testing | https://abseil.io/resources/swe-book/html/ch12.html | Google's positions (test via public APIs, test behaviours, DAMP over DRY) as Google's, never as evidence |
| SRC-332 | T1 | admit-restricted | MongoDB manual: FAQ on query injection and $where | https://www.mongodb.com/docs/manual/faq/fundamentals/ | Facts about MongoDB: queries are BSON; `$where`, `mapReduce`, `$accumulator`, `$function` run JavaScript; `--noscripting`; `$where` cannot use indexes |
| SRC-335 | T1 | admit-restricted | node-postgres: Queries | https://node-postgres.com/features/queries | Facts about `pg`: parameters go to the server unaltered; no parameters for identifiers; `pg-format` named for identifiers |
| SRC-341 | T1 | admit-restricted | OWASP ASVS 5.0 chapters V1, V5, V11, V15, V16 | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x20-V11-Cryptography.md | 13_srvsec: Verification requirements only, and only these ids with the topic their text states: 1.2.4 (database queries parameterized), 1.3.6 (SSRF allowlist), 5.2.5 (symlinks in archives), 5.3.2 (file paths from trusted data), 5.3.3 (decompression ignores user path info), 11.2.4 (constant-time operations), 11.5.1 (CSPRNG, 128 bits), 15.1.5 (dangerous functionality documented; deserialization named only in the section introduction), 15.3.2 (no redirects followed by backend), 16.5.1 and 16.4.1 (error exposure, log encoding). Not for deserialization via 15.1.1, not for path containment via 5.2.3, not for SSRF via 5.3.2; 14_secgap2: Adds to SRC-341 (same applies to SRC-132 on the tree URL) these ids, checklist items only, each with its stated topic: 1.2.2, 1.3.5 (scriptable template language content, not SSTI), 1.3.7, 1.5.1, 5.1.1, 5.2.1, 5.2.2, 5.2.3 (archive uncompressed size, not path containment), 5.2.4, 5.2.6, 5.3.1, 5.4.1, 5.4.2, 5.4.3, 15.1.2, 15.2.4; the V1, V5 and V15 files are also admitted as K12, K27 and K36 |
| SRC-343 | T1 | admit-restricted | OWASP NoSQL Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/NoSQL_Security_Cheat_Sheet.html | Principles: validate scalar types before building a filter, objects as field values enable operator injection, `$where` runs untrusted JavaScript, disable server-side JavaScript; quotes come from a summary, extractor reads verbatim |
| SRC-345 | T1 | admit-restricted | OWASP SQL Injection Prevention Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html | Principles: prepared statements, stored procedures, allow-list mapping for identifiers, escaping "STRONGLY DISCOURAGED" and fragile; no JavaScript content |
| SRC-346 | T1 | admit-restricted | OWASP SSRF Prevention Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html | Principles: allowlist over denylist, validate resolved IPs and connect only to validated addresses, disable redirects, IMDSv2; the npm library `ip-address` it names never grounds a tool choice |
| SRC-347 | T1 | admit-restricted | Prisma Client: Raw queries | https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries | Facts about `$queryRaw` (tagged template, prepared statements), `$queryRawUnsafe` and `Prisma.raw` (injection when concatenated); never a preference for Prisma |
| SRC-351 | T2 | admit-restricted | CWE-502: Deserialization of Untrusted Data | https://cwe.mitre.org/data/definitions/502.html | Name, definition, generic mitigations; examples are Java and Python only |
| SRC-352 | T2 | admit-restricted | CWE-89: SQL Injection | https://cwe.mitre.org/data/definitions/89.html | Name, definition and the generic parameterized-statement mitigation |
| SRC-354 | T2 | admit-restricted | CWE-943: Improper Neutralization of Special Elements in Data Query Logic | https://cwe.mitre.org/data/definitions/943.html | Name and definition; observed examples name MongoDB and Mongoose (the discoverer found none) |
| SRC-355 | T2 | admit-restricted | OWASP WSTG: Testing for NoSQL Injection | https://wstg.owasp.org/v4.1/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection/ | Mechanism of `$where` JavaScript injection and the CPU exhaustion example; testing guidance, not remediation; version 4.1 page |
| SRC-374 | T1 | admit | HTTP Semantics (RFC 9110), section 5.5 field values | https://www.rfc-editor.org/rfc/rfc9110.html | - |
| SRC-376 | T1 | admit-restricted | JSON Web Token (RFC 7519) | https://www.rfc-editor.org/rfc/rfc7519.html | Claims definitions and the section 7.2 validation steps; the section 8 requirement to implement none is read only together with RFC 8725 (K01), which updates it |
| SRC-377 | T1 | admit | JSON Web Token Best Current Practices (RFC 8725, BCP 225) | https://www.rfc-editor.org/rfc/rfc8725.html | - |
| SRC-388 | T1 | admit-restricted | OWASP ASVS 5.0, V1 Encoding and Sanitization | https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/en/0x10-V1-Encoding-and-Sanitization.md | Checklist items, ids 1.2.2 (URL encoding and safe protocols), 1.3.5 (sanitize or disable scriptable template language content such as Markdown, CSS or XSL; not SSTI), 1.3.7 (templates not built from untrusted input), 1.5.1 (XML parsers restrictive, no external entities); ids 1.2.6 (LDAP), 1.2.7 (XPath), 1.3.12 (ReDoS) are not this slot's topics |
| SRC-391 | T1 | admit-restricted | OWASP ASVS 5.0, V5 File Handling | https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/en/0x14-V5-File-Handling.md | Checklist items, ids 5.1.1 to 5.4.3 each with its stated topic; 5.2.3 is archive uncompressed size and file count, not path containment; 5.3.2 is file path construction; mechanisms from other T1 |
| SRC-399 | T1 | admit-restricted | OWASP XML External Entity Prevention Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html | General guidance only: disable DTDs, reject DOCTYPE, disable external entity resolution and limit entity expansion; it has no Node or JavaScript section (headings read: C/C++, ColdFusion, Java, .NET, iOS, PHP, Python, Semgrep) |
| SRC-400 | T1 | admit-restricted | OWASP XML Security Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html | Language-neutral: use XSD not DTD, disable external entity processing, bound occurrences, HTTPS for remote schemas; no JavaScript content |
| SRC-408 | T2 | admit-restricted | OWASP WSTG: Testing for Server-side Template Injection (v4.2) | https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server-side_Template_Injection | Detection mechanism (plaintext against code context) for Jinja2, Twig and FreeMarker only; no JavaScript engine, no remediation section |
| SRC-411 | T3 | admit-restricted | Server-Side Template Injection: RCE for the modern web app (J. Kettle) | https://portswigger.net/research/server-side-template-injection | Mechanism and the Jade case study as research evidence; the three defences (trivial engine such as Mustache, sandbox, container) as the author's positions; no tool claim |
