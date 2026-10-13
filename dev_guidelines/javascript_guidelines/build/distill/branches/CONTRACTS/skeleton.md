# CONTRACTS skeleton

Purpose of the branch: checkability. Both subtrees, breadth-first. Ledger rows refer to
`ledger.md`. Epistemic states follow the brief: `known` on one T1 or two independent T2 grounds;
`unvalidated` where a quote is tool-extracted on the only T1 ground, or a ground is inferred.

## Graph js-philosophy: node table

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| CONTRACTS | Contracts | Make intent checkable: at build time through a type layer, at run time by parsing untrusted data at every trust boundary, and in the shape of functions and objects, so that a violated expectation is reported where it arises and not discovered downstream | known | - |
| CONTRACTS.STATIC | Static contract | Express expectations as types that a tool checks before the program runs, while holding that a type layer is a build-time artefact of a language that has no types at run time | known | - |
| CONTRACTS.BOUNDARY | Boundary contract | Parse every datum that crosses a trust boundary into the shape the program expects before use, so that code past the boundary may rely on that shape | known | - |
| CONTRACTS.SHAPE | Shape of calls | A call carries its meaning by name and not by position, because argument order must otherwise be memorised by every reader and writer | known \| unvalidated: quote tool-extracted | CONTRACTS-010 |
| CONTRACTS.STATIC.1 | Types attest nothing at run time | Run-time data is checked only by run-time code: types and assertions are erased and say nothing about the values that arrive | known | CONTRACTS-001, CONTRACTS-002 |
| CONTRACTS.STATIC.2 | A passing check is evidence, not proof | The checker is intentionally unsound in places and detects a measured part of defects, so it complements run-time checks and tests and never replaces them | known \| unvalidated: quote tool-extracted; measurement single T2 source, 2017 | CONTRACTS-003, CONTRACTS-004 |
| CONTRACTS.BOUNDARY.1 | Validate at every trust boundary | All data crossing a trust boundary is validated before use, including data from internal services, queues and stored records; the server side is the authority | known | CONTRACTS-005, CONTRACTS-006 |
| CONTRACTS.BOUNDARY.2 | Accept by positive rule | State what is valid and reject the rest, instead of enumerating what is bad | known | CONTRACTS-007 |
| CONTRACTS.BOUNDARY.3 | Check meaning as well as form | A well-formed value can still break a rule: related fields are checked together | known | CONTRACTS-008 |
| CONTRACTS.BOUNDARY.4 | Input handling is a recognizer | Accept only what the input language defines, and keep that language simple enough to be recognized completely before anything is computed from it | known \| unvalidated: single T2 source | CONTRACTS-009 |

### js-philosophy intentlinks (inside the branch)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | CONTRACTS.BOUNDARY.1 | CONTRACTS.STATIC.1 | requires | Because a type layer attests nothing about arriving data, the boundary check is what gives the types their truth |
| 2 | CONTRACTS.BOUNDARY.2 | CONTRACTS.BOUNDARY.4 | refines | A positive rule is a recognizer for a simple input language; complex languages need a real parser, not a pattern list |
| 3 | CONTRACTS.STATIC.2 | CONTRACTS.BOUNDARY.1 | requires | Since a passing check is not proof, run-time validation stays in place even in fully typed code |

### js-philosophy proposed links to other branches (integrator resolves)

| # | from | to (branch) | type | sentence |
|---|---|---|---|---|
| P1 | CONTRACTS.BOUNDARY.1 | DEFENSE | requires | Treating every input as hostile in DEFENSE presupposes that inputs are parsed at the boundary here |
| P2 | CONTRACTS.BOUNDARY.2 | DEFENSE | refines | Positive validation is the language-neutral form of the allowlist stance DEFENSE takes toward sinks and injection |
| P3 | CONTRACTS.STATIC.1 | VERIFICATION | requires | A type layer is a contract only while a tool checks it in the build and in CI, which VERIFICATION gates |
| P4 | CONTRACTS.SHAPE | STRUCTURE | refines | Call shapes are the smallest unit of the interface design STRUCTURE governs |
| P5 | CONTRACTS.BOUNDARY.1 | web-architecture (planned, not created) | refines | Server-side authority for validation is architecture owned by the web-architecture guideline (ledger row CONTRACTS-006, deferred) |

### js-philosophy inter links to python-kb-philosophy

Target file `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`, uids read.

| # | from | to | type | sentence |
|---|---|---|---|---|
| I1 | CONTRACTS.BOUNDARY | python-kb-philosophy:DEFENSIVE | refines | Validate at boundaries and trust after validation: the shared principle, here with the JavaScript-distinct fact that the language has no run-time types |
| I2 | CONTRACTS.STATIC | python-kb-philosophy:DATACENTRICITY | refines | Make invalid states unrepresentable and let a schema be the constraint: the shared principle realised through a separate type layer |
| I3 | CONTRACTS.SHAPE | python-kb-philosophy:COMMUNICATION | refines | An interface is user experience: call sites that say what they mean |

## Graph pig-js-defaults: node table

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.CONTRACTS | Contracts defaults | Make JavaScript intent checkable with TypeScript at build time and schema parsing at run time, every escape from the checker being deliberate | known | - |
| PIG-JS.CONTRACTS.LAYER | Type layer | Choose the type layer and keep its check in the loop whatever runs the code | known | - |
| PIG-JS.CONTRACTS.STRICT | Checker strictness | Run the checker at its most demanding setting and keep that setting stable across upgrades | known | - |
| PIG-JS.CONTRACTS.ESCAPE | Escape hatches | Keep the escape hatches of the type system shut, and open one only deliberately and with a reason | known | - |
| PIG-JS.CONTRACTS.MODEL | Modelling and narrowing | Model variants and absence so that the checker can prove more, and narrow explicitly | known | - |
| PIG-JS.CONTRACTS.SIGNATURE | Function shapes | Declare function shapes that reject the calls the contract does not allow | known | - |
| PIG-JS.CONTRACTS.BOUNDARY | Parse at the boundary | Turn untrusted data into typed values by parsing at the boundary | known | - |
| PIG-JS.CONTRACTS.LAYER.1 | Type layer is TypeScript | Write JavaScript projects in TypeScript with strict checking; the type-layer choice is decided by the max rule with JSDoc-checked JavaScript and none as rejected positions | known \| conflict: JSDoc-checked JavaScript (no admitted advocate; wins where no compile or type-check step is acceptable), none (no admitted holder) | CONTRACTS-011, CONTRACTS-012 |
| PIG-JS.CONTRACTS.LAYER.2 | JSDoc-checked JavaScript as the no-compile-step fallback | Where no compile step can exist, check JavaScript with the same compiler through JSDoc, naming its weaker guarantees | known \| unvalidated: no admitted advocate; TypeScript 7.0 facts are vendor facts | CONTRACTS-013, CONTRACTS-014, CONTRACTS-015, CONTRACTS-016 |
| PIG-JS.CONTRACTS.LAYER.3 | Type check is a step of its own | Running TypeScript never counts as checking it: a separate type check with no emit runs wherever types are stripped | known \| unvalidated: quote tool-extracted | CONTRACTS-017, CONTRACTS-018 |
| PIG-JS.CONTRACTS.LAYER.4 | Only erasable syntax under type stripping | When Node strips types, the code uses only syntax that stripping can erase, enforced by the compiler option | known | CONTRACTS-019 |
| PIG-JS.CONTRACTS.LAYER.5 | Compiler options aligned with Node | The checker is configured as Node documents for type stripping, since Node ignores the configuration file at run time | known \| unvalidated: quote tool-extracted | CONTRACTS-020 |
| PIG-JS.CONTRACTS.LAYER.6 | Per-file transpilation safety | Where files are transpiled one at a time, code needing cross-file type information is reported by the checker | known \| unvalidated: quote tool-extracted | CONTRACTS-021 |
| PIG-JS.CONTRACTS.STRICT.1 | strict on | Enable the whole strict family and never turn a member off; noImplicitAny and strictNullChecks are its load-bearing members | known | CONTRACTS-022, CONTRACTS-023, CONTRACTS-024 |
| PIG-JS.CONTRACTS.STRICT.2 | Unchecked index access | Reads of undeclared keys are typed as possibly undefined | known \| unvalidated: mechanism only, no admitted source mandates the flag; conflict: friction cost (typescript-eslint) | CONTRACTS-025 |
| PIG-JS.CONTRACTS.STRICT.3 | Exact optional properties | An optional property means absent, not possibly undefined | known \| unvalidated: mechanism only, quote tool-extracted | CONTRACTS-026 |
| PIG-JS.CONTRACTS.STRICT.4 | Compiler version is pinned | The compiler version is pinned and upgraded deliberately, because defaults and strict-family checks change between releases | known \| unvalidated: pinning inferred from single T1 source | CONTRACTS-027, CONTRACTS-028 |
| PIG-JS.CONTRACTS.ESCAPE.1 | unknown, not any | A value of unknown shape is typed unknown and narrowed before use | known | CONTRACTS-029 |
| PIG-JS.CONTRACTS.ESCAPE.2 | Explicit any is a lint error | Explicit any is rejected by the linter, which is the check that closes the escape hatch | known | CONTRACTS-030 |
| PIG-JS.CONTRACTS.ESCAPE.3 | Leaked any is caught | Values typed any that enter from libraries and untyped sources are caught at assignment by type-aware lint | known | CONTRACTS-031 |
| PIG-JS.CONTRACTS.ESCAPE.4 | No Function type | Callable values carry a specific signature, never the Function type | known \| unvalidated: quote tool-extracted | CONTRACTS-032 |
| PIG-JS.CONTRACTS.ESCAPE.5 | Assertions need a reason | Type and non-null assertions appear only with an obvious reason, and an explicit run-time check is preferred | known | CONTRACTS-033 |
| PIG-JS.CONTRACTS.ESCAPE.6 | No suppression directives | Type errors are fixed and never silenced by directive; a lint suppression is allowed only with a comment saying why | known \| unvalidated: single T2 source | CONTRACTS-034, CONTRACTS-035 |
| PIG-JS.CONTRACTS.MODEL.1 | Discriminated unions with exhaustive switches | Variants are discriminated unions closed by a never assignment, so a new member breaks the build where it is unhandled | known \| unvalidated: quote tool-extracted | CONTRACTS-036 |
| PIG-JS.CONTRACTS.MODEL.2 | Explicit narrowing, not truthiness | Primitives are narrowed by explicit tests, because falsy values are legitimate data | known \| unvalidated: quote tool-extracted | CONTRACTS-037 |
| PIG-JS.CONTRACTS.MODEL.3 | Optional chaining only on nullable values | Optional chaining appears only where the type says the value can be absent | known \| unvalidated: preference inferred from rule behaviour | CONTRACTS-038 |
| PIG-JS.CONTRACTS.MODEL.4 | Type predicates are assertions | A user-defined type predicate is held to the standard of a type assertion: its body performs a real run-time check, and built-in narrowing or a schema parse is preferred | known \| unvalidated: inferred from assertion and unsoundness grounds; no admitted source states that the compiler does not verify the body | CONTRACTS-039 |
| PIG-JS.CONTRACTS.MODEL.5 | Object types by interface | Object types are declared by interface, which can be extended and re-opened; aliases are for what an interface cannot express | known \| unvalidated: single T2 source, position only; the alias exception is inferred | CONTRACTS-040 |
| PIG-JS.CONTRACTS.SIGNATURE.1 | Options object | Calls with several optional or same-typed primitive arguments take one named options object | known \| unvalidated: inferred, transfer to application APIs | CONTRACTS-041, CONTRACTS-042 |
| PIG-JS.CONTRACTS.SIGNATURE.2 | Optional trailing parameters, not overloads | A declared API expresses optional trailing arguments as optional parameters | known \| unvalidated: quote tool-extracted; declared APIs only | CONTRACTS-043 |
| PIG-JS.CONTRACTS.SIGNATURE.3 | Unions, not overloads | A declared API expresses a varying argument type as a union | known \| unvalidated: quote tool-extracted; declared APIs only | CONTRACTS-044 |
| PIG-JS.CONTRACTS.SIGNATURE.4 | Callback result and parameter types | An ignored callback result is void and callback parameters are never optional | known \| unvalidated: quote tool-extracted; declared APIs only | CONTRACTS-045 |
| PIG-JS.CONTRACTS.BOUNDARY.1 | JSON.parse yields unknown | The result of JSON.parse is unknown until validated | known | CONTRACTS-046 |
| PIG-JS.CONTRACTS.BOUNDARY.2 | Schema rejects unneeded properties | Untrusted structured input is checked against a schema that allows only the keys and types it names, before merge or lookup code sees it | known | CONTRACTS-047 |
| PIG-JS.CONTRACTS.BOUNDARY.3 | Bind to a dedicated allowlisted object | Request data binds to a purpose-built object with allowlisted fields and never to a domain model | known \| unvalidated: quote tool-extracted | CONTRACTS-048 |
| PIG-JS.CONTRACTS.BOUNDARY.4 | Validate before Node or language APIs | External input is validated by allowlist in application code before it reaches Node or language APIs | known | CONTRACTS-049 |
| PIG-JS.CONTRACTS.BOUNDARY.5 | Schema infers the static type | Boundary schemas are written in a library whose schema is the single source of the static type, so the parse and the type cannot drift; schemas are never built from untrusted input | known \| unvalidated: vendor documentation facts only; no admitted ranking between Zod and Valibot, so no library is named as the default | CONTRACTS-050, CONTRACTS-051, CONTRACTS-052 |

### pig-js-defaults intentlinks (inside the branch)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.CONTRACTS.LAYER.3 | PIG-JS.CONTRACTS.LAYER.1 | requires | TypeScript is a contract only while a separate check runs; execution alone checks nothing |
| 2 | PIG-JS.CONTRACTS.LAYER.4 | PIG-JS.CONTRACTS.LAYER.3 | requires | The erasable-syntax rule is enforced by the same compiler run that checks types |
| 3 | PIG-JS.CONTRACTS.LAYER.5 | PIG-JS.CONTRACTS.LAYER.4 | refines | The Node-aligned options include the option that enforces erasable syntax |
| 4 | PIG-JS.CONTRACTS.LAYER.2 | PIG-JS.CONTRACTS.LAYER.1 | conflicts | A project uses one type layer: JSDoc-checked JavaScript applies only where TypeScript cannot |
| 5 | PIG-JS.CONTRACTS.STRICT.1 | PIG-JS.CONTRACTS.LAYER.1 | requires | The strict family exists only inside the compiler that the type layer runs |
| 6 | PIG-JS.CONTRACTS.STRICT.4 | PIG-JS.CONTRACTS.STRICT.1 | refines | Pinning keeps the strict family from changing under the code between releases |
| 7 | PIG-JS.CONTRACTS.ESCAPE.3 | PIG-JS.CONTRACTS.ESCAPE.2 | refines | Leaked any catches what the explicit-any rule cannot see in code that never wrote the word |
| 8 | PIG-JS.CONTRACTS.ESCAPE.1 | PIG-JS.CONTRACTS.BOUNDARY.1 | dataflow | An unknown value is narrowed by the validation that BOUNDARY.1 and BOUNDARY.2 perform |
| 9 | PIG-JS.CONTRACTS.ESCAPE.5 | PIG-JS.CONTRACTS.BOUNDARY.2 | requires | The explicit run-time check preferred over an assertion is, at a boundary, the schema parse |
| 10 | PIG-JS.CONTRACTS.BOUNDARY.1 | PIG-JS.CONTRACTS.BOUNDARY.2 | dataflow | The unknown result of parsing text flows into schema validation |
| 11 | PIG-JS.CONTRACTS.BOUNDARY.5 | PIG-JS.CONTRACTS.BOUNDARY.2 | refines | A library is only a realisation of the schema rule |
| 12 | PIG-JS.CONTRACTS.MODEL.1 | PIG-JS.CONTRACTS.LAYER.1 | requires | Discriminated unions and never checks exist only in TypeScript, not in checked JavaScript with the weaker mode |

### pig-js-defaults proposed links to other branches (integrator resolves)

| # | from | to (branch) | type | sentence |
|---|---|---|---|---|
| Q1 | PIG-JS.CONTRACTS.LAYER.3 | VERIFICATION | requires | The no-emit type check is a CI gate |
| Q2 | PIG-JS.CONTRACTS.ESCAPE.2 | VERIFICATION | requires | The explicit-any, unsafe-assignment and directive rules are lint rules that VERIFICATION configures |
| Q3 | PIG-JS.CONTRACTS.ESCAPE.6 | VERIFICATION | requires | Suppression handling is a lint and review rule |
| Q4 | PIG-JS.CONTRACTS.STRICT.4 | DEPENDENCIES | requires | A pinned compiler is one case of the lockfile and update policy |
| Q5 | PIG-JS.CONTRACTS.LAYER.6 | STRUCTURE | refines | Type-only exports and import forms are module conventions that STRUCTURE owns |
| Q6 | PIG-JS.CONTRACTS.LAYER.4 | SUBSET | refines | The erasable-syntax rule excludes enum and namespaces, which SUBSET lists among features to avoid |
| Q7 | PIG-JS.CONTRACTS.MODEL.2 | SUBSET | refines | Explicit narrowing is the typed side of the equality and coercion rules |
| Q8 | PIG-JS.CONTRACTS.MODEL.3 | SUBSET | refines | Optional chaining and nullish operators are language features SUBSET constrains |
| Q9 | PIG-JS.CONTRACTS.SIGNATURE.1 | STRUCTURE | refines | Function and object API design |
| Q10 | PIG-JS.CONTRACTS.BOUNDARY.1 | CONTROL | requires | JSON.parse throws SyntaxError, which CONTROL's error propagation must handle |
| Q11 | PIG-JS.CONTRACTS.BOUNDARY.1 | DEFENSE | refines | A parsed object with an own proto key is harmless until merged; DEFENSE owns pollution |
| Q12 | PIG-JS.CONTRACTS.BOUNDARY.2 | DEFENSE | requires | The schema allowlist is the first defence against prototype pollution |
| Q13 | PIG-JS.CONTRACTS.BOUNDARY.3 | DEFENSE | refines | Mass assignment is an injection class DEFENSE lists |
| Q14 | PIG-JS.CONTRACTS.BOUNDARY.4 | DEFENSE | refines | Allowlisted input before Node APIs underlies the command, path and regex rules of DEFENSE |

### pig-js-defaults inter links (to js-philosophy)

| # | from | to | type | sentence |
|---|---|---|---|---|
| X1 | PIG-JS.CONTRACTS.LAYER | js-philosophy:CONTRACTS.STATIC | refines | The type layer realises the static contract |
| X2 | PIG-JS.CONTRACTS.STRICT | js-philosophy:CONTRACTS.STATIC.2 | refines | Maximum strictness is the answer to a check that is evidence and not proof |
| X3 | PIG-JS.CONTRACTS.ESCAPE | js-philosophy:CONTRACTS.STATIC.2 | refines | Each escape hatch is a place where the check proves nothing |
| X4 | PIG-JS.CONTRACTS.MODEL | js-philosophy:CONTRACTS.STATIC | refines | Modelling lets the checker prove more |
| X5 | PIG-JS.CONTRACTS.SIGNATURE | js-philosophy:CONTRACTS.SHAPE | refines | Declared signatures realise shape of calls |
| X6 | PIG-JS.CONTRACTS.BOUNDARY | js-philosophy:CONTRACTS.BOUNDARY | refines | Parsing at the boundary realises the boundary contract |
| X7 | PIG-JS.CONTRACTS.BOUNDARY.1 | js-philosophy:CONTRACTS.STATIC.1 | requires | Because types are erased, parsed data is typed only after run-time validation |

## Judge records (one per defaults node holding a decision)

Each record: Positions, Forces, Decision, Rejected (position, reason, condition under which it wins).

**PIG-JS.CONTRACTS.LAYER.1.** Positions: TypeScript (Google JS guide, frozen, recommends migrating, SRC-239; Google TS guide, SRC-244; TYPES-C01); JSDoc-checked JavaScript (no advocate; documented by SRC-047, SRC-044; weaker checks TYPES-C40; JSDoc forms removed in 7.0, TYPES-C42); none (no holder; only SRC-240 measuring 15 percent detection). Forces: checkability is served most by the position whose checker sees the most (full type syntax, unions, strict family); its cost is a compile or type-check step, which Node type stripping lowers (TYPES-C03, C04). Decision: TypeScript with strict. Rejected: JSDoc-checked JavaScript, because checking is weaker (open objects, optional parameters, any initialisers) and 7.0 drops forms; it wins where no build or type-check step can be adopted (LAYER.2). None, because no admitted holder argues for it and SRC-240 measures benefit; it wins on no admitted evidence. Native type syntax, because it is Stage 1 with no run-time enforcement.

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
