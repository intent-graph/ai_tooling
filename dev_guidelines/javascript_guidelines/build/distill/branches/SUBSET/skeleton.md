# Skeleton: branch SUBSET (purpose: predictability)

The subtree of the SUBSET branch in both graphs. Conventions: in `epistemic_state` cells the IG
issue separator ` | ` is written `\|` so the table survives; the integrator unescapes it. Ledger rows
are the ids of `ledger.md`. Branch-level links to other branches name the target by branch keyword and
note the topic; the integrator resolves them to uids. Intents of `js-philosophy` pass the language-swap
test (no JavaScript term); intents of `pig-js-defaults` may name JavaScript.

## Graph js-philosophy: SUBSET

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| SUBSET | Predictable subset | Code does what its text says: the team writes in a checked subset of a permissive language, so no hidden conversion, silent failure, ambient default or surprise mutation decides an outcome. | known \| unvalidated: principle inferred as the roll-up of the PIG-JS.SUBSET decisions | - |
| SUBSET.VISIBLE | Visible conversion | Comparison and conversion are stated where they happen, so what an expression does follows from the declared kind of its operands, not from their values or from a coercion table the reader must recall. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.CONVERSION | - |
| SUBSET.FAILURE | Loud failure | A mistake stops the program at the mistake: code runs in the strictest mode its language offers, in which a misspelt name, a write to a locked value or an unowned receiver raises an error instead of silently changing state. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.STRICTNESS.1, MUTATION.1 and OBJECTS.1 | - |
| SUBSET.NUMBERS | Stated numeric limits | The precision and range of the numeric type decide which values may travel in it; values beyond them use an exact representation, and rounding is never papered over by an ad-hoc tolerance. | known \| unvalidated: single T2 source on the tolerance point; limits grounded in PIG-JS.SUBSET.NUMBERS | SUBSET-001 |
| SUBSET.STATE | Distinguished immutability | Whether a value cannot change at all or may be changed only by some holders is a distinction the code states, and a language mechanism is chosen for the one it actually gives. | known \| unvalidated: single T2 source \| gap: no admitted source states immutability as a design preference (G-M29) | SUBSET-002 |
| SUBSET.BINDING | Enforced binding and access | A name's mutability and reach are declared and enforced by the language, not by naming convention or discipline: bindings are fixed by default, private means unreachable, and the receiver of a call is never implicit. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.STRICTNESS.3, STRICTNESS.4, OBJECTS.1 and OBJECTS.3 | - |
| SUBSET.MATURITY | Settled features | Code uses only language features whose meaning is settled and available on every target, retires deprecated ones, and leaves the language's built-in objects unaltered, because later growth of the language would change what the code means. | known \| unvalidated: inferred roll-up of PIG-JS.SUBSET.EVOLUTION and OBJECTS.5 | - |

### Intentlinks inside js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | SUBSET.STATE | SUBSET.FAILURE | requires | A lock on state protects only as far as a write to it fails loudly. |

### Inter links to python-kb-philosophy (shared principles, linked not copied)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | SUBSET.VISIBLE | python-kb-philosophy:DEFENSIVE | refines | Explicit over implicit and least surprise, applied to comparison and conversion. |
| 2 | SUBSET.FAILURE | python-kb-philosophy:DEFENSIVE | refines | Fail fast and never swallow errors, applied to the language's strict mode. |
| 3 | SUBSET.MATURITY | python-kb-philosophy:REPRODUCIBILITY | refines | The same code means the same on every target only if it uses settled features (inferred). |

### Proposed links to other branches (js-philosophy)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | SUBSET.FAILURE | CONTROL | requires | Loud failure at the language level is the base on which explicit error propagation and unhandled-rejection policy stand. |
| 2 | SUBSET.VISIBLE | CONTRACTS | requires | Visible conversion is the in-expression half of checking intent; boundary parsing of untrusted data is the other half. |
| 3 | SUBSET.MATURITY | DEPENDENCIES | requires | Settled features and a supported-runtime floor are the language-side counterpart of choosing a supported dependency set. |

## Graph pig-js-defaults: PIG-JS.SUBSET

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.SUBSET | Checked JavaScript subset | Make JavaScript behaviour predictable by narrowing the language: strict semantics, explicit comparison and conversion, stated numeric limits, visible mutation, enforced privacy, settled features only. | known | - |
| PIG-JS.SUBSET.STRICTNESS | Strict by construction | All code runs under strict semantics through ES modules, and every binding is block-scoped and fixed by default. | known | - |
| PIG-JS.SUBSET.CONVERSION | Explicit comparison and conversion | A comparison or conversion never depends on an implicit coercion the reader must predict. | known | - |
| PIG-JS.SUBSET.NUMBERS | Numbers with stated limits | Number carries only values within its precision and range; exactness beyond them is obtained by another representation. | known | - |
| PIG-JS.SUBSET.OBJECTS | Objects, classes and receivers | Object and class code fixes its receiver, its construction order, its privacy and its prototype chain at the language level. | known \| unvalidated: accessor rule rests on a position only | - |
| PIG-JS.SUBSET.MUTATION | Visible mutation | State changes happen where the code says they do: freezing is understood as shallow, copies are deep on purpose, sorting states whether it mutates. | known | - |
| PIG-JS.SUBSET.EVOLUTION | Settled features and retired legacy | New code uses only settled features checked against its targets and none of the retired or deprecated ones. | known \| unvalidated: statement-termination rule rests on a position only | - |
| PIG-JS.SUBSET.STRICTNESS.1 | Strict mode everywhere | Every file runs in strict mode, so a typo or an unowned receiver raises an error instead of creating a global or a hidden default. | known \| unvalidated: practice inferred from MDN's stated reasons; quote tool-extracted | SUBSET-003, SUBSET-004, SUBSET-005 |
| PIG-JS.SUBSET.STRICTNESS.2 | ES modules as the unit | Code is written as ES modules, which are strict, module-scoped, evaluated once and deferred. | known | SUBSET-006, SUBSET-007 |
| PIG-JS.SUBSET.STRICTNESS.3 | Fixed bindings by default | A binding is fixed unless the code reassigns it, and a fixed binding is not mistaken for an immutable value. | known | SUBSET-008, SUBSET-009, SUBSET-010 |
| PIG-JS.SUBSET.STRICTNESS.4 | No function-scoped declarations | Names are block-scoped, never function-scoped, hoisted or silently redeclarable. | known | SUBSET-011 |
| PIG-JS.SUBSET.CONVERSION.1 | Strict equality | Values are compared without type conversion; the comparison result follows from the operands alone. | known | SUBSET-012, SUBSET-013, SUBSET-014, SUBSET-015 |
| PIG-JS.SUBSET.CONVERSION.2 | Null and undefined checks | A check for absence names the values it tests, with no loose-equality exception. | known \| conflict: Google JS guide and ESLint option null ignore allow == null as the one exception | SUBSET-016, SUBSET-017 |
| PIG-JS.SUBSET.CONVERSION.3 | NaN test | NaN is detected by a dedicated test, since it is unequal to every value. | known | SUBSET-018 |
| PIG-JS.SUBSET.CONVERSION.4 | Explicit conversion | A conversion is written as a call that names its target type; a conversion hidden in an operator is flagged as a readability convention. | known \| unvalidated: positions only, no mechanism evidence \| conflict: Pradel and Sen (T2, 2015 corpus) found 98.85 percent of implicit coercions likely harmless | SUBSET-019, SUBSET-020, SUBSET-021, SUBSET-022 |
| PIG-JS.SUBSET.CONVERSION.5 | Number is not validation | Number conversion is never the test that an input is a valid number. | known \| unvalidated: quote tool-extracted | SUBSET-023 |
| PIG-JS.SUBSET.CONVERSION.6 | Nullish defaults and chains | A default replaces only absence, and optional chaining is used within its syntactic limits. | known \| unvalidated: quote tool-extracted | SUBSET-024, SUBSET-025, SUBSET-026, SUBSET-027 |
| PIG-JS.SUBSET.NUMBERS.1 | Rounded fractions | Fractional arithmetic is treated as approximate wherever results are compared or accumulated. | known \| gap: exact decimal and money arithmetic has no admitted source (G-M01) | SUBSET-028 |
| PIG-JS.SUBSET.NUMBERS.2 | Safe integer range | Integers stay within the safe range or change representation. | known | SUBSET-029 |
| PIG-JS.SUBSET.NUMBERS.3 | BigInt scope | BigInt appears only where values exceed the safe range, and never meets Number in one expression. | known | SUBSET-030, SUBSET-031, SUBSET-032 |
| PIG-JS.SUBSET.NUMBERS.4 | Integers across JSON | Integers that exceed the safe range cross JSON as strings or through an explicit codec. | known | SUBSET-033, SUBSET-034 |
| PIG-JS.SUBSET.OBJECTS.1 | Explicit receiver | The receiver of a call is never implicit: no code relies on the global this, and callbacks keep the outer receiver lexically. | known | SUBSET-035, SUBSET-036, SUBSET-037, SUBSET-038, SUBSET-039 |
| PIG-JS.SUBSET.OBJECTS.2 | Construction order | A class is declared before use and a derived class initialises its base before touching its own state. | known \| unvalidated: quote tool-extracted (class declaration rule) | SUBSET-040, SUBSET-041, SUBSET-042 |
| PIG-JS.SUBSET.OBJECTS.3 | Language-enforced privacy | Private means unreachable from outside, by a mechanism the language enforces. | known \| conflict: Google TS guide (TypeScript private, not hash fields), Google JS guide (optional trailing underscore), Airbnb (no underscores) | SUBSET-043, SUBSET-044, SUBSET-045, SUBSET-046 |
| PIG-JS.SUBSET.OBJECTS.4 | Accessor properties | Properties do not run code on access; behaviour that does work is an explicit method call. | known \| unvalidated: single T2 source, restricted position only, no mechanism evidence (G-L14) | SUBSET-047, SUBSET-069 |
| PIG-JS.SUBSET.OBJECTS.5 | Untouched built-ins | The language's built-in prototypes carry only what the language put there. | known | SUBSET-048, SUBSET-049, SUBSET-050 |
| PIG-JS.SUBSET.OBJECTS.6 | Own properties and enumeration | Own properties are tested and enumerated without visiting the prototype chain. | known \| unvalidated: for-in rule on arrays single T2 source; hasOwn preference grounded for untrusted keys by two T1 sources via RUNSEC-C07, extension to all reads inferred | SUBSET-051, SUBSET-052, SUBSET-053 |
| PIG-JS.SUBSET.MUTATION.1 | Shallow freeze | Freezing is relied on for one level only and only in strict code; deeper immutability is designed in. | known | SUBSET-054, SUBSET-055, SUBSET-056 |
| PIG-JS.SUBSET.MUTATION.2 | Deliberate deep copy | A deep copy uses the platform clone and knows what the clone drops. | known \| unvalidated: quote tool-extracted | SUBSET-057, SUBSET-058 |
| PIG-JS.SUBSET.MUTATION.3 | Sorting | Sorting states whether the original may change and never relies on the default order for numbers. | known \| unvalidated: quote tool-extracted (comparator rule) | SUBSET-059, SUBSET-060 |
| PIG-JS.SUBSET.EVOLUTION.1 | Finished proposals only | Production code uses only features that reached the final standardisation stage. | known \| unvalidated: single T1 source restricted to status facts; rule inferred | SUBSET-061 |
| PIG-JS.SUBSET.EVOLUTION.2 | Temporal adoption | The new date-time API is adopted only once every target is verified to ship it or a polyfill covers the gap. | known \| unvalidated: availability facts dated, recheck before citing | SUBSET-062, SUBSET-063 |
| PIG-JS.SUBSET.EVOLUTION.3 | No legacy syntax | Syntax that strict mode forbids or that blocks reasoning about names is not written. | known | SUBSET-064, SUBSET-065 |
| PIG-JS.SUBSET.EVOLUTION.4 | No deprecated features | Deprecated and browser-only legacy features are replaced by their listed successors in new code. | known | SUBSET-066, SUBSET-067 |
| PIG-JS.SUBSET.EVOLUTION.5 | Statement termination | Every statement is terminated explicitly and every control structure is braced, so no statement boundary or scope is left to automatic insertion or indentation. | known \| unvalidated: single T2 source, restricted position only; insertion hazards not extracted (G-M02) | SUBSET-068, SUBSET-070 |

### Intentlinks inside pig-js-defaults (branch SUBSET)

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

### Inter links from pig-js-defaults to js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.SUBSET.CONVERSION | js-philosophy:SUBSET.VISIBLE | refines | Strict equality, explicit conversion and nullish operators are the concrete rules of visible conversion. |
| 2 | PIG-JS.SUBSET.STRICTNESS.1 | js-philosophy:SUBSET.FAILURE | refines | Strict mode is the language's loud-failure mode. |
| 3 | PIG-JS.SUBSET.MUTATION.1 | js-philosophy:SUBSET.FAILURE | refines | A frozen write fails loudly only in strict code. |
| 4 | PIG-JS.SUBSET.NUMBERS | js-philosophy:SUBSET.NUMBERS | refines | Binary64 precision, the safe-integer range and BigInt are the concrete numeric limits. |
| 5 | PIG-JS.SUBSET.MUTATION.1 | js-philosophy:SUBSET.STATE | refines | Object.freeze is the language mechanism whose reach (own keys only) must be known. |
| 6 | PIG-JS.SUBSET.STRICTNESS.3 | js-philosophy:SUBSET.BINDING | refines | const and no var fix bindings by default. |
| 7 | PIG-JS.SUBSET.OBJECTS.3 | js-philosophy:SUBSET.BINDING | refines | Hash fields make privacy enforced instead of conventional. |
| 8 | PIG-JS.SUBSET.OBJECTS.1 | js-philosophy:SUBSET.BINDING | refines | An explicit receiver is the call-side half of enforced binding. |
| 9 | PIG-JS.SUBSET.EVOLUTION | js-philosophy:SUBSET.MATURITY | refines | Stage-4-only, retired legacy and untouched built-ins are the concrete settled-feature rules. |
| 10 | PIG-JS.SUBSET.OBJECTS.5 | js-philosophy:SUBSET.MATURITY | refines | Leaving built-ins unaltered keeps later language growth from changing the code's meaning. |

### Proposed links to other branches (pig-js-defaults)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.SUBSET.STRICTNESS.2 | STRUCTURE | requires | Module cycles, side-effect-free imports and the Node ESM facts build on ES modules as the unit (routing groups module-cycles and node-esm). |
| 2 | PIG-JS.SUBSET.STRICTNESS | VERIFICATION | requires | no-var and prefer-const are lint gates that enforce fixed, block-scoped bindings. |
| 3 | PIG-JS.SUBSET.CONVERSION | VERIFICATION | requires | eqeqeq and no-implicit-coercion are the lint gates that enforce the conversion rules. |
| 4 | PIG-JS.SUBSET.CONVERSION.5 | CONTRACTS | requires | Validation of numeric input belongs to boundary parsing, which this node says Number conversion is not. |
| 5 | PIG-JS.SUBSET.CONVERSION.6 | CONTRACTS | requires | Optional chaining is used only on values whose type can really be nullish (LANG-C53, routed to CONTRACTS). |
| 6 | PIG-JS.SUBSET.NUMBERS.4 | CONTRACTS | dataflow | Large integers cross a JSON boundary as strings; the boundary parser decodes them. |
| 7 | PIG-JS.SUBSET.NUMBERS.4 | DEFENSE | requires | JSON.parse of untrusted input has its own prototype-key hazard (RUNSEC-C13, overlap O14). |
| 8 | PIG-JS.SUBSET.MUTATION.1 | STRUCTURE | requires | Exported objects are shared mutable state that freeze alone does not protect deeply (STRUCT-C01 to C03). |
| 9 | PIG-JS.SUBSET.MUTATION.1 | DEFENSE | requires | Freezing as a hardening step has its own scope and cost (DOMSEC-C52, RUNSEC-C09). |
| 10 | PIG-JS.SUBSET.OBJECTS.5 | DEFENSE | conflicts | Freezing built-ins as hardening (RUNSEC-C09) is the sanctioned exception to leaving built-ins alone; scope separates them (tension X1). |
| 11 | PIG-JS.SUBSET.OBJECTS.5 | RUNTIME | requires | Setting a prototype at creation, not later, is an engine-optimisation fact held by RUNTIME (STRUCT-C43). |
| 12 | PIG-JS.SUBSET.OBJECTS.6 | DEFENSE | requires | Own-property tests and for-in avoidance on untrusted keys are the prototype-pollution defence (RUNSEC-C07, overlap O15). |
| 13 | PIG-JS.SUBSET.EVOLUTION.5 | VERIFICATION | requires | A formatter, not review, is what would enforce statement termination. |
| 14 | PIG-JS.SUBSET.EVOLUTION.1 | DEPENDENCIES | requires | Target runtime floor (Node LTS, browser Baseline) is the second input to the feature-maturity check. |

## Judge records (one per defaults node holding a decision)

Format: Positions (claim ids), Forces, Decision, Rejected (with the condition under which it would win).

### PIG-JS.SUBSET.STRICTNESS.1
- Positions: strict everywhere (LANG-C02, LANG-C01); sloppy mode left on in scripts (nobody holds it); use strict per file by hand (LANG-C02 for classic scripts).
- Forces: predictability gains loud failure (LANG-C03); cost is none in modules and classes, one directive in scripts.
- Decision: all code strict, via modules or classes, directive only in classic scripts.
- Rejected: sloppy mode in legacy scripts; would win only for code that cannot be edited.

### PIG-JS.SUBSET.STRICTNESS.2
- Positions: ES modules (LANG-C57, STRUCT-C21); classic scripts and globals (implicit alternative).
- Forces: module scope and single evaluation remove ambient globals; cost is a build or type=module loading.
- Decision: write ES modules.
- Rejected: classic scripts with a directive; would win for a single-file page with no tooling.

### PIG-JS.SUBSET.STRICTNESS.3
- Positions: const by default (LANG-C36); let everywhere; belief that const means constant value (LANG-C35).
- Forces: a fixed binding states intent at the declaration; cost none.
- Decision: const unless reassigned.
- Rejected: let-by-default (no ground); the belief, refuted by MDN.

### PIG-JS.SUBSET.STRICTNESS.4
- Positions: never var (LANG-C37); var in scripts for global export.
- Forces: block scope and no silent redeclaration; the global-property side effect of var is a hazard.
- Decision: never var.
- Rejected: var for a deliberate script global; would win never (use globalThis or a module export).

### PIG-JS.SUBSET.CONVERSION.1
- Positions: === everywhere (LANG-C17); == where the types are known (LANG-C27 measurement only).
- Forces: result follows from operands alone versus a measured fraction of redundant ==; cost none.
- Decision: === and !==; Object.is only for signed zero (acceptable-when, LANG-C20).
- Rejected: == with types known; would win never as a rule, since the types are not checked.

### PIG-JS.SUBSET.CONVERSION.2
- Positions: forbid all == (eqeqeq always, Airbnb); allow == null only (Google JS, eqeqeq null ignore).
- Forces: both are exact in mechanism (ECMA-262 7.2.13); one uniform rule asks nothing of the reader, the exception asks the reader to know the one exception.
- Decision: forbid every ==, the null check included. Max rule: the more demanding of two grounded options.
- Rejected: == null as the one exception; would win where the code base already encodes it in lint and values brevity over uniformity (recorded as acceptable-when, SUBSET-017).

### PIG-JS.SUBSET.CONVERSION.3
- Positions: Number.isNaN (LANG-C21); x === NaN, self-comparison.
- Forces: NaN is unequal to itself; the dedicated test is the only reading that cannot be wrong.
- Decision: Number.isNaN.
- Rejected: x === NaN, never correct (MDN, ECMA-262 7.2.14).

### PIG-JS.SUBSET.CONVERSION.4
- Positions: forbid shorthands with the lint rule (SRC-003, Google, Airbnb); allow them (Pradel and Sen: harm rare).
- Forces: conversion visible at the site versus a measured low defect rate; the rule is readability, not defect prevention.
- Decision: explicit Boolean(), Number(), String() and no-implicit-coercion, stated as a readability convention with no defect claim. Max rule on predictability of reading.
- Rejected: allowing shorthands; wins where a team does not adopt the rule (SUBSET-022). Grounds are positions only, flagged for review.

### PIG-JS.SUBSET.CONVERSION.5
- Positions: Number(x) as validation (rejected by LANG-C23); Number.isFinite or boundary parsing (not in this branch).
- Forces: Number() accepts null, empty and whitespace as 0.
- Decision: never use Number(x) as the validity test.
- Rejected: Number(x) with an isNaN check; would win never, as null and empty string pass as 0.

### PIG-JS.SUBSET.CONVERSION.6
- Positions: ?? for defaults (LANG-C50); logical OR for defaults (folklore).
- Forces: falsy-but-valid values (0, empty string, false) versus brevity.
- Decision: ?? whenever any falsy value is valid; parenthesise any mix (LANG-C51).
- Rejected: logical OR default; wins only if all falsy values are invalid (SUBSET-027).

### PIG-JS.SUBSET.NUMBERS.1
- Positions: treat fractions as rounded (LANG-C28); fixed tolerance as cure (rejected in js-philosophy by LANG-C29).
- Forces: binary64 cannot hold decimal fractions exactly; the tolerance relation is not transitive.
- Decision: treat all fraction arithmetic as approximate.
- Rejected: tolerance as general cure; wins never as a general rule.

### PIG-JS.SUBSET.NUMBERS.2
- Positions: Number inside the safe range with isSafeInteger, larger as BigInt or string (LANG-C30).
- Forces: exactness beyond 2^53 versus type friction.
- Decision: as stated.
- Rejected: Number for large ids; wins never (silent corruption).

### PIG-JS.SUBSET.NUMBERS.3
- Positions: BigInt only above 2^53 (LANG-C31); BigInt everywhere (folklore); mixed arithmetic (rejected by LANG-C32).
- Forces: exact arithmetic versus a separate type with no mixing.
- Decision: BigInt only where values exceed the safe range, never mixed with Number.
- Rejected: BigInt as default integer; wins never in everyday code.

### PIG-JS.SUBSET.NUMBERS.4
- Positions: ids as strings (LANG-C33, TYPES-C49); explicit replacer and reviver.
- Forces: JSON numbers are parsed to binary64 before any reviver; stringify throws on BigInt.
- Decision: strings or an explicit codec; never plain numbers beyond the safe range.
- Rejected: plain JSON numbers for 64-bit ids; wins never.

### PIG-JS.SUBSET.OBJECTS.1
- Positions: never rely on implicit this (LANG-C04); arrows for lexical this (LANG-C06); Google conventions (LANG-C07, C08, demoted).
- Forces: this set at call time makes detached methods fail; the Google conventions are stronger but grounded only by a position.
- Decision: never rely on an implicit global this; use arrows for lexical this in nested callbacks.
- Rejected: restricting this to class code (LANG-C08) and arrows over bind everywhere (LANG-C07) as rules; would win as a team convention (acceptable-when).

### PIG-JS.SUBSET.OBJECTS.2
- Positions: declare before use, super() first (LANG-C09, C10).
- Forces: TDZ and field-initialisation timing make order observable.
- Decision: as stated.
- Rejected: using a class before its declaration; wins never.

### PIG-JS.SUBSET.OBJECTS.3
- Positions: hash private fields (MDN, TC39); trailing underscore (Google JS); no underscores, they are public API (Airbnb); TypeScript private, no hash fields (Google TS).
- Forces: runtime-enforced privacy versus convention and emit-size cost on down-levelled output; the mechanism is undisputed.
- Decision: hash private fields wherever privacy must hold; an underscore never counts as privacy.
- Rejected: TypeScript private; wins on down-levelled targets where the emit cost is measured. Underscore convention; wins never as privacy.

### PIG-JS.SUBSET.OBJECTS.5
- Positions: leave built-ins alone (STRUCT-C44, MDN); never modify built-ins and no direct prototype work (LANG-C14, Google, demoted).
- Forces: a later language addition of the same name breaks the patch (SmooshGate).
- Decision: add nothing to built-in prototypes.
- Rejected: patching; wins only for backporting an already-specified feature.

### PIG-JS.SUBSET.OBJECTS.6
- Positions: Object.hasOwn (LANG-C55); hasOwnProperty (STRUCT-C45); for-in on arrays (rejected by LANG-C26).
- Forces: an inherited method can be shadowed or absent; for-in visits inherited keys.
- Decision: Object.hasOwn; arrays iterated by element, not for-in.
- Rejected: hasOwnProperty; wins on targets without Object.hasOwn.

### PIG-JS.SUBSET.MUTATION.1
- Positions: freeze is shallow (LANG-C38, C39); freeze as deep immutability (folklore).
- Forces: SetIntegrityLevel touches own keys only; strict-only throwing.
- Decision: rely on freeze for one level and in strict code; deep immutability by recursive freeze on acyclic graphs or an immutable design.
- Rejected: freeze as deep guarantee; wins never.

### PIG-JS.SUBSET.MUTATION.2
- Positions: structuredClone (LANG-C44); JSON round trip.
- Forces: cycles, typed arrays, prototypes versus JSON-safe simplicity.
- Decision: structuredClone for cloneable data.
- Rejected: JSON round trip; wins for JSON-safe data only (SUBSET-058).

### PIG-JS.SUBSET.MUTATION.3
- Positions: toSorted (LANG-C40); sort with a comparator (LANG-C41); default sort.
- Forces: sort mutates in place; default order is by string.
- Decision: toSorted when the original must stay; always a comparator for numbers.
- Rejected: default sort of numbers; wins never.

### PIG-JS.SUBSET.OBJECTS.4
- Positions: no accessor properties, use methods (STRUCT-C46, Google JS, position only); accessors allowed (implicit, no holder).
- Forces: a property read that runs code hides cost and side effects from the reader, which is the predictability purpose; cost is a call-style API.
- Decision: no getter or setter properties; behaviour is a method.
- Rejected: accessors; would win for a cheap, side-effect-free view of stored state on a data-like object (SUBSET-069, inferred). Grounds are one position, flagged for review.

### PIG-JS.SUBSET.EVOLUTION.1
- Positions: stage 4 only (LANG-C54, inferred); earlier stages with a transpiler (no admitted source).
- Forces: earlier stages can change or be dropped.
- Decision: stage 4 only.
- Rejected: stage 3 with transpiler; would win only with a source that states the maturity and target guarantees (none admitted).

### PIG-JS.SUBSET.EVOLUTION.2
- Positions: check support, polyfill (LANG-C43); adopt Temporal now; keep Date (no source states a rule).
- Forces: availability is a runtime fact, dated.
- Decision: adopt only after verifying every target or covering it by a polyfill.
- Rejected: adopting unchecked; wins never.

### PIG-JS.SUBSET.EVOLUTION.3
- Positions: no legacy octal, no with (LANG-C24, C46).
- Forces: strict-mode errors versus legacy code.
- Decision: neither is written.
- Rejected: legacy syntax in old files; wins never in new code.

### PIG-JS.SUBSET.EVOLUTION.4
- Positions: replace deprecated features (LANG-C47); no Annex B in new code (LANG-C48).
- Forces: Annex B is normative only for browsers and optional elsewhere.
- Decision: replace and avoid.
- Rejected: relying on Annex B; wins never for portable code.

### PIG-JS.SUBSET.EVOLUTION.5
- Positions: explicit semicolons and braces, no reliance on automatic insertion (QUALITY-C19, Google JS, position only); reliance on insertion with a formatter and lint (no holder in the claim base).
- Forces: explicit termination makes statement boundaries independent of the next token and of line breaks, the predictability purpose; cost is typing, which a formatter removes.
- Decision: semicolon on every statement, braces on every control structure.
- Rejected: reliance on automatic insertion; would win where a formatter and hazard-catching lint rules both run in CI and the team adopts that style (SUBSET-070). No admitted source documents the hazards (not extracted, G-M02): grounds are one position, flagged for review.
