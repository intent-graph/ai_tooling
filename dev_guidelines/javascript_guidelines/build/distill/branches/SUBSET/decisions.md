# Decisions for review: branch SUBSET

Each decision settles a contested topic, a weighty choice, or rests on a single source. The max rule
(most demanding practice an admitted source supports) decided each; the maintainer may overrule any.
Epistemic labels: grounded, inferred or open.

## A. Contested topics (decided by the max rule)

### A1. `== null`: forbid every `==` (node PIG-JS.SUBSET.CONVERSION.2, rows SUBSET-016, 017)
- Decision (grounded as a choice, inferred as the max reading): forbid all `==`, including the null check; write `x === null || x === undefined`. Lint: ESLint `eqeqeq` default `always`.
- Rejected: `== null` as the one allowed `==` (Google JS guide, eqeqeq option `null: ignore`). It would win where a code base already encodes the exception in lint and prefers brevity over uniformity; the mechanism is exact (ECMA-262 7.2.13), so it is a style loss, not a defect risk.
- Grounds: eqeqeq (SRC-002, T1) default forbids it; Airbnb (SRC-312) forbids it as a position; MDN (SRC-011) describes the behaviour. Note: the stage-4 dissent slot recommended allowing the exception; this branch chose the more demanding option because predictability means the reader needs no special case. Flagged for the maintainer.

### A2. Implicit coercion shorthands (node CONVERSION.4, rows SUBSET-019 to 022)
- Decision: write `Boolean()`, `Number()`, `String()`; enable `no-implicit-coercion`; state the rule as a readability convention and make no claim that it prevents defects.
- Rejected: allow `!!x`, `+x`, `'' + x`. It wins where a team does not adopt the lint rule; the only measurement (Pradel and Sen, 2015 corpus, SRC-238) finds 98.85 percent of implicit coercions likely harmless.
- Grounds: positions only (SRC-003 T1 restricted, rationale is readability; SRC-239 and SRC-312 positions). No mechanism evidence supports forbidding; this is the weakest-grounded decision of the branch and the one most likely to be overruled. Epistemic: `known | unvalidated: positions only, no mechanism evidence | conflict: Pradel and Sen`.

### A3. Private-member marking (node OBJECTS.3, rows SUBSET-043 to 046)
- Decision: hash private fields wherever privacy must hold; an underscore never counts as privacy.
- Rejected: TypeScript `private` instead of hash fields (Google TS guide, SRC-244, reason stated: emit size and performance when down-levelled): wins on down-levelled targets where the cost is measured. Optional trailing underscore (Google JS, SRC-239) and underscore convention in general: never privacy (MDN, SRC-091). No-underscore rule (Airbnb, SRC-312): agrees on the mechanism, adds no ground.
- Grounds: MDN private elements (SRC-091) and classes (SRC-008), TC39 class fields (SRC-024): the mechanism is undisputed, the dispute is only the compile target.

## B. Weighty choices on thin or restricted grounds

### B1. Strict mode everywhere (node STRICTNESS.1, LANG-C02)
- The preference is inferred from MDN's three reasons (LANG-C02 is marked inferred); the mechanism (modules and classes strict by construction) is ECMA-262 11.2.2, grounded. Rejected: sloppy mode, wins only for code that cannot be edited. Epistemic: `known | unvalidated: practice inferred; quote tool-extracted`.

### B2. Only TC39 stage 4 features (node EVOLUTION.1, LANG-C54)
- Decision on one source (SRC-028, T1, restricted to status facts); the rule is inferred from the definition of stage 4. Rejected: earlier stages with a transpiler; no admitted source states target guarantees for them. Epistemic: `known | unvalidated: single T1 source restricted to status facts; rule inferred`.

### B3. `Object.hasOwn` over `hasOwnProperty` (node OBJECTS.6, LANG-C55)
- The reason (shadowing, null-prototype objects) is quoted from Airbnb, a position that may not serve as evidence, and the stage-4 status is a restricted status fact. The choice is corroborated by RUNSEC-C07 in DEFENSE (consensus, overlap O15), whose sources this agent did not re-read. Follow-up check: RUNSEC-C07 (consensus, DEFENSE) is grounded on SRC-139 (MDN prototype pollution, T1, unrestricted) and SRC-078 (Node security best practices, T1, unrestricted for 06_runsec); it states Object.hasOwn for untrusted-keyed reads. LANG-C55 is confirmed for that case by two T1 sources; extending it to all own-property tests is inferred from the same mechanism. Kept as the decision; `hasOwnProperty` stays as acceptable-when on targets without `Object.hasOwn` (STRUCT-C45, MDN). Epistemic: `known | unvalidated: grounded for untrusted keys by two T1 sources via RUNSEC-C07, extension to all reads inferred`.

### B4. Temporal adoption (node EVOLUTION.2, LANG-C43)
- Decision: adopt only after every target is verified or covered by a polyfill. The availability figures (Firefox 139, Chrome 144, Node.js 26; MDN not Baseline) are dated facts as of the MDN page date and must be rechecked before citing (SRC-019 restriction).

### B5. `for-in` on arrays (node OBJECTS.6, LANG-C26)
- Decision on one T2 source (DLint, SRC-237, restricted to evidence that the practice occurs and causes visible bugs on 2015 sites). Within the restriction as evidence, but the rule wording is the paper's. Epistemic: single T2.

## C. Style-guide positions demoted (restriction: positions only, never evidence)

No admitted source other than a restricted style guide supports these four; each is kept as `acceptable-when` (a team convention) and none is a decision. The maintainer may promote any by choosing it as a convention. STRUCT-C46 and QUALITY-C19 were demoted in the first pass and are now decisions on a position alone (section E).

| claim | position | holder | node | would be promoted by |
|---|---|---|---|---|
| LANG-C07 | arrow functions over bind(this) and self = this | Google JS | OBJECTS.1 | a T1 statement of the reason; the mechanism is already in LANG-C06 |
| LANG-C08 | this only in class code and arrows | Google JS | OBJECTS.1 | a T1 or second independent T2 ground |
| LANG-C14 | no direct prototype work, use class | Google JS | OBJECTS.5 | MDN class-over-prototype statement (STRUCT-C43 in RUNTIME) read as a rule |
| LANG-C16 | never call new on primitive wrappers | Google JS | CONVERSION.4 | ECMA-262 wrapper-object semantics or ESLint no-new-wrappers docs |

## D. Single-source decisions (T1 unless marked)

LANG-C02 (MDN strict mode), LANG-C09 (MDN classes), LANG-C20 (MDN equality sameness), LANG-C23 (MDN Number), LANG-C26 (T2), LANG-C41 (MDN sort), LANG-C44 (MDN structuredClone), LANG-C50 (MDN nullish coalescing), LANG-C54 (TC39 finished proposals), LANG-C55 (see B3). Each carries `unvalidated: quote tool-extracted` or the single-source label in its node; none is contested.

## E. Former undecided nodes, now decided on a position (flagged)

No node of this branch is undecided. Both were decided because an admitted position exists; each is the weakest-grounded kind of decision (one T2 restricted position, no mechanism evidence), labelled `known | unvalidated`.

### E1. Statement termination (node PIG-JS.SUBSET.EVOLUTION.5, rows SUBSET-068, 070)
- Decision: a semicolon on every statement and braces on every control structure; never rely on automatic semicolon insertion. By predictability: explicit termination makes statement boundaries independent of line breaks and of the next token.
- Rejected: reliance on insertion (no-semicolon style). It wins where a formatter and lint rules that catch insertion hazards both run in CI and the team adopts that style; no admitted source states that condition.
- Grounds: Google JS (SRC-239, T2, position only, QUALITY-C19). Searched: every claim table, the register and the coverage report; no claim states the insertion hazards (slot 01 records that no mechanism was read, G-M02), so the coordinator's note that MDN documents them is not backed by an extracted claim. Would strengthen it: ECMA-262 automatic insertion rules and the MDN lexical-grammar page, extracted as claims.

### E2. Accessor properties (node PIG-JS.SUBSET.OBJECTS.4, rows SUBSET-047, 069)
- Decision: no getter or setter properties; behaviour that does work is a method. By predictability: a read that runs code hides cost and side effects.
- Rejected: accessors. They win for a cheap, side-effect-free view of stored state on a data-like object (inferred, no source).
- Grounds: Google JS (SRC-239, T2, position only, STRUCT-C46); its compiler-support reason is a Closure tooling point and is not carried. Searched: all claim tables, register and coverage (G-L14); the only other hits are LANG-C13 (class-field Define semantics) and LANG-C42, unrelated. Would strengthen it: MDN Using classes (LC-02) and ECMA-262 accessor semantics.

## F. Gaps noted, no node created (no claim of this branch touches them)

G-M01 exact decimal and money arithmetic (TC39 decimal repository LC-01); G-M02 remainder (typeof, instanceof and realms, Symbol, iterators and generators, destructuring and spread); G-M03 dates, time zones, Unicode, Intl; G-M29 immutability as a design preference (kept as a gap on SUBSET.STATE); G-L01 parseInt radix. These stay for the integrator and the maintainer: no practice is invented for them.
