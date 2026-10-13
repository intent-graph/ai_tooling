# CONTRACTS decisions for review

Selection rule: max, grounded (see `../../target_hierarchy.md`). Each decision lists the choice,
the rejected positions with the condition under which each would win, and the grounds. Node
uids are in `skeleton.md`, rows in `ledger.md`.

## D1. Type layer is TypeScript (PIG-JS.CONTRACTS.LAYER.1, rows CONTRACTS-011, CONTRACTS-012)

Decision: TypeScript with strict checking and a separate type check (LAYER.3). Epistemic state:
`known | conflict: JSDoc-checked JavaScript, none`. This is maintainer question Q1 of `12_dissent`
(recommendation there: the same).

Rejected positions:
- JSDoc-checked JavaScript. Wins where no compile step and no type-check step can be adopted.
  Kept as a fallback (LAYER.2) with its limits: open-ended object literals, all parameters
  optional, any for null and empty-array initialisers (TYPES-C40); no run-time import of
  tags and silent no-op of unlisted tags (TYPES-C41); TypeScript 7.0 drops enum tags,
  Closure-style function types, standalone question mark and postfix bang (TYPES-C42).
- None. Wins on no admitted evidence: no admitted holder argues for it (TYPES-C01, G-M05 of
  `11_coverage`); SRC-240 only measures that types detect 15 percent of public bugs.
- Waiting for native type annotations in JavaScript. A Stage 1 proposal, last presented 2023-09
  (TYPES-C46). Never a basis; status is a grounded fact, "do not plan on it" is inferred.

Grounds and their strength (honest account):
- Mechanism, T1: the TypeScript checker sees more in TypeScript files than in checked JavaScript
  (SRC-047, restricted to facts up to 6.x; SRC-052 for the checkers' modes). These are the tool's
  own documentation, so they ground facts about checking strength, not "prefer this tool".
- Advocacy, T2, one holder: the Google JS guide (frozen, recommends migrating) and the Google TS
  guide are one organisation counted once, and both are restricted to "positions", never evidence.
- Measurement, T2: SRC-240 (2017, Flow 0.30 and TypeScript 2.0, 15 percent of 400 public bugs,
  conservative by the authors' words; not current strict TypeScript).
- The step from "checker sees more" to "choose TypeScript" is the max rule's judgment (inferred).
  Node type stripping (SRC-038) removes the build step that was the usual reason to avoid
  TypeScript (inferred, as in `12_dissent` Topic 4).

## D2. Flags beyond strict: enable (PIG-JS.CONTRACTS.STRICT.2 and .3, rows CONTRACTS-025, CONTRACTS-026)

Decision: enable noUncheckedIndexedAccess and exactOptionalPropertyTypes for new code.
The source claims say only "consider" and give the mechanism; no admitted source mandates the
flags. The max rule picks the more checkable setting, marked `unvalidated: mechanism only`.

Rejected: leaving them off. Wins where index-heavy or untyped-dependency code makes the friction
exceed the defects found; typescript-eslint calls the first flag often unwieldy (SRC-026, T1).
The condition is inferred. Review ask: confirm that a mechanism-only ground suffices for a
mandate, or demote both to acceptable-when.

## D3. No suppression directives (PIG-JS.CONTRACTS.ESCAPE.6, rows CONTRACTS-034, CONTRACTS-035)

Decision: ban ts-ignore, ts-expect-error and ts-nocheck; allow a lint suppression only with a
comment saying why. Epistemic state `known | unvalidated: single T2 source`.

Weakness to review: the ground is one T2 holder (Google TS guide). The same position appears twice
(QUALITY-C18, TYPES-C25). The register leaves SRC-244 unrestricted for the quality slot but
restricts it in the types slot to "positions only, never evidence". I used the quality-slot claim
as the decision ground and demoted the types-slot claim to a fact row. If the maintainer reads the
restriction as applying to the topic and not the slot, this node becomes undecided, with TYPES-C25
and QUALITY-C18 as acceptable-when.

Rejected: allowing directives with a reason. Wins for a third-party typing bug that cannot be
fixed locally (inferred). No admitted holder takes that position.

## D4. Options object (PIG-JS.CONTRACTS.SIGNATURE.1, rows CONTRACTS-041, CONTRACTS-042)

Decision: options object when several arguments are optional or same-typed primitives.
Grounds: ESLint's stated rationale (order and types must be memorised, SRC-084, T1 restricted:
the default of 3 is a configuration default, not evidence) and the W3C TAG position for web
platform APIs (SRC-261, T2 restricted). No admitted source states it for application code: the
claim is inferred (STRUCT-C49), epistemic state `known | unvalidated: inferred`.
Rejected: positional lists, which win for one to three required distinct-typed arguments.
The philosophy node CONTRACTS.SHAPE holds only the language-neutral part (STRUCT-C47).

## D5. Compiler pinned (PIG-JS.CONTRACTS.STRICT.4, rows CONTRACTS-027, CONTRACTS-028)

Decision: pin the TypeScript version and upgrade deliberately. The tsconfig reference says future
versions may add checks under strict (T1, single source); the pin is inferred. Rejected:
floating versions, which win never for applications; the library-publishing case belongs to
DEPENDENCIES (proposed link Q4).

## D6. Optional chaining only on nullable types (PIG-JS.CONTRACTS.MODEL.3, row CONTRACTS-038)

Decision as in the claim; preference inferred from the typescript-eslint rule plus MDN
(`known | unvalidated: preference inferred`). Rejected: defensive optional chaining everywhere;
wins on untyped boundary data, which BOUNDARY handles by parsing instead.

## D7. Erasable syntax scope (PIG-JS.CONTRACTS.LAYER.4, row CONTRACTS-019)

Decision follows the claim: erasable syntax only when Node strips types. The max rule could widen
it to every TypeScript project (so the code always runs unbuilt), but no admitted source says so,
so the widening is open, not decided. Review ask: widen or keep conditional.

## D8. Folklore rows with empty claim ids (CONTRACTS-002, CONTRACTS-018)

The two beliefs of `12_dissent` concerning this branch (types protect at run time; Node
type-checks what it runs) become `rejected` rows. Their refuting claims (TYPES-C02, TYPES-C03) sit
in their own decision rows, and the brief places each claim once, so the rejected rows carry
claim_ids `-`. Review ask for the integrator: keep this convention or merge each pair into one row.

## D9. Deferred claim (CONTRACTS-006)

TYPES-C29 (client-side validation is never a security control; validation at a trusted service
layer) is architecture owned by the web-architecture guideline per `11_coverage`: ledger role
`deferred` on CONTRACTS.BOUNDARY.1, with a planned boundary link (P5 in the skeleton).

## D10. Philosophy and defaults split

Language-swap test applied claim by claim. To js-philosophy: TYPES-C27, C28, C33, C48, C29
(language-neutral boundary principles), STRUCT-C47 (parameter memorisation), TYPES-C02, C23, C47
(JavaScript-distinct: the language has no run-time types; the checker is unsound and measured).
Everything naming a compiler option, tool, API or library is in pig-js-defaults.

## D11. Former undecided nodes, now decided (rows CONTRACTS-039, CONTRACTS-040, CONTRACTS-050 to CONTRACTS-052)

Per the standing max rule, a missing independent ranking is not a reason to abstain; each node is
decided where admitted positions or facts exist. All three are weak on grounds and flagged.
- MODEL.4 type predicates are assertions (TYPES-C20). Decision: held to the standard of a type
  assertion (explicit run-time check in the body; built-in narrowing or schema parse preferred).
  Grounds: TYPES-C19 and TYPES-C23 (T1 handbook and typescript-eslint). The specific statement that
  the compiler does not verify a predicate body is in no admitted source (searched: handbook
  narrowing page, typescript-eslint pages; a digest asserted it, a verbatim re-ask did not).
  Epistemic: `known | unvalidated: inferred`. Rejected: trust as written, which wins for a
  one-line test of an already validated discriminant (inferred).
- MODEL.5 interface for object types (TYPES-C26). Decision: interface; alias for what an interface
  cannot express (inferred). Ground: the Google TS guide position, one T2 holder, plus the handbook
  fact that interfaces extend and re-open. The register restricts the source to position only; the
  position is used to choose among positions, not as evidence. Rejected: alias everywhere, which
  wins where accidental declaration merging must be impossible (inferred). The const enum half is
  settled by LAYER.4.
- BOUNDARY.5 schema infers the static type (TYPES-C36, C37, with C38 and C35 as facts). Decision at
  the class level: a library whose schema is the single source of the static type, Standard Schema
  V1 compliant where tools must accept it, schemas never compiled from untrusted input. No library
  is named: all sources are vendor documentation, admitted for facts only, and none ranks Zod
  against Valibot. Rejected: JSON Schema with Ajv, which wins where the schema is a language-neutral
  contract shared with non-TypeScript code (inferred). Review ask: name a default library or keep
  the class-level rule.

## D3 scoping note

The register restriction on SRC-244 is scoped per slot: unrestricted for the quality slot, so
QUALITY-C18 may ground the rule; the decision stands. TYPES-C25 remains a fact row.

## Undecided nodes

None. Remaining open items, not nodes: whether the compiler verifies type predicate bodies (no
admitted source); an independent ranking of schema libraries (none admitted); overloads whose
return type depends on the argument type (not stated by the handbook page read).
