# Discovery result: slot 02 TYPES (static types and boundary validation)

Fetched 2026-10-12. Note on method: the fetch tool returns a model-written digest of each page, not raw text. Dates, versions and quotes below are as that digest reported them and are marked `digest` where the page itself showed no date. Stage 2 should re-read T1 pages in full.

## L1 headline

Authoritative coverage is strong for the TypeScript and JSDoc-checked options, `any`/`unknown`, strictness, Node type stripping and boundary-validation principles (grounded: 17 T1 pages fetched), but thin for the "no static types" option, the TypeScript 6.0/7.0 roadmap and schema-validation tooling, which rest on T2/T3 only (certainty: grounded on fetched digests; tier proposals are inferred and left to the audit).

Pinned:
- Candidates by proposed tier: 33 total = 17 T1, 11 T2, 5 T3.
- Sub-topics with no T1 candidate: (a) type layer "none, no static types"; (b) schema-validation tooling for boundary parsing (Standard Schema, Zod, Valibot, Ajv, JSON Schema); (c) TypeScript 6.0/7.0 roadmap and TS 7 JSDoc-checking changes; (d) the TC39 type-annotations proposal text itself (T1 only for its Stage 1 status via TYPES-K04).
- Failed fetches on a T1 candidate: none failed outright; partial on TYPES-K05 (digest omitted `erasableSyntaxOnly`, `verbatimModuleSyntax`, `checkJs`) and TYPES-K26 (JSON.parse section text not shown). Non-T1 failures: TYPES-K20 origin PDF (`ECONNREFUSED`, then `403` on the repository copy) and IEEE page (empty).

## L2 claims

Sub-topics, best candidates, T1 present? (ids are TYPES-Knn)

- Type layer: TypeScript, strict checking and config: K05, K08, K09, K10 (T1); K11, K12, K13 (T2). T1 yes. Grounded.
- Type layer: JSDoc-checked JavaScript: K06, K07 (T1); K13 (T2, TS 7.0 reworks JSDoc checking); K33 (T3 project rationale, expect-restricted). T1 yes. Grounded.
- Type layer: none (no static types): K20 (T2, about 15% of public bugs detectable by Flow or TypeScript; origin PDF not fetched); K33 (T3). T1 **no**. Grounded for what is cited; the choice itself has no normative source (inferred).
- Strictness: K05 (T1: `strict` family, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `useUnknownInCatchVariables`), K19 (T1); K12, K13 (T2: `strict` default true from 6.0, confirmed in 7.0). T1 yes. Grounded.
- `any` and `unknown`: K08, K09, K17, K18, K19 (T1); K16 (T2). T1 yes. Grounded.
- Assertions and guards give no runtime check: K08 (T1, quoted), K10 (T1); K16 (T2). T1 yes. Grounded. K10 does not discuss predicate unsoundness (open: no source found).
- Runtime parsing of untrusted data, principles: K21, K22, K23 (T1); K24 (T2, LangSec). T1 yes. Grounded.
- What JavaScript gives at the boundary (no schema): K25, K26 (T1). T1 yes. Grounded (K26 partial).
- Schema-validation tooling: K29 (T2); K28, K30, K31, K32 (T3, expect-restricted). T1 **no**. Grounded.
- Node.js native type stripping: K01, K27 (T1); K11 (T2). T1 yes. Grounded. Status: stable since v25.2.0 and v24.12.0, default-on since v23.6.0 / v22.18.0, `--experimental-transform-types` removed in v26.0.0, docs v26.11.1; v24 is Active LTS, v26 Current (digest).
- TC39 type annotations proposal: K04 (T1, status only); K02, K03, K14 (T2). T1 for the text **no**. Grounded. Status: Stage 1, champions Rosenwasser, Cintra, Palmer; last meeting notes 2023-09; README says not updated regularly (digest).
- TypeScript compiler roadmap: K12, K13, K15 (T2). T1 **no**. Grounded. Status: 6.0 released 2026-03-23, 7.0 released 2026-07-08 (Go-native, strict default, JSDoc rework), typescript-go repo archived as completed (digest).

Pinned:
- Candidates by proposed tier: 33 total = 17 T1, 11 T2, 5 T3.
- Sub-topics with no T1 candidate: (a) type layer "none, no static types"; (b) schema-validation tooling for boundary parsing (Standard Schema, Zod, Valibot, Ajv, JSON Schema); (c) TypeScript 6.0/7.0 roadmap and TS 7 JSDoc-checking changes; (d) the TC39 type-annotations proposal text itself (T1 only for its Stage 1 status via TYPES-K04).
- Failed fetches on a T1 candidate: none failed outright; partial on TYPES-K05 (digest omitted `erasableSyntaxOnly`, `verbatimModuleSyntax`, `checkJs`) and TYPES-K26 (JSON.parse section text not shown). Non-T1 failures: TYPES-K20 origin PDF (`ECONNREFUSED`, then `403` on the repository copy) and IEEE page (empty).

Disagreements and tensions (every position kept for later stages):
- K16 says `const enum` must not be used, use plain `enum`; K01 and K11 (type stripping, `erasableSyntaxOnly`) exclude enums altogether. Grounded.
- K33 and K07 (JSDoc-typed JavaScript, for libraries) versus K16 and K05 (TypeScript, strict): different positions on the type layer; K33 says JSDoc is less beneficial for apps (secondhand, via a trade article, primary not fetched). Grounded/inferred.
- K13 removes `@enum` handling and Closure-style syntax in JSDoc checking while K07 still lists `@enum`: handbook page may lag the release. Inferred; re-read.
- K29 (language-neutral JSON Schema validate) versus K30, K31 (schema as TypeScript types, parse and infer). Grounded.
- K19 recommends `recommended` for most teams and `strict` for TypeScript-proficient ones, while K05 and K12 make `strict` the compiler default. Grounded.

Gaps:
- No T1 or T2 source for "no static types" as a deliberate choice beyond K20's measurement (searched: ICSE and effect studies, Svelte, Turbo). Maintainer primaries (Svelte interview and forum comment, Turbo) were reached only through derivatives. Open.
- No source on user-defined type guard unsoundness, nor on `JSON.parse` returning `any` in TypeScript lib typings. Open.
- No peer-reviewed study on runtime validation libraries versus none. Open.
- Deno and Bun native TypeScript: named only per decision Q2, not researched.
- LangSec report K24 is a technical report; a peer-reviewed version was not fetched. Open.

## L3 full

Pinned (verbatim at every level):
- Candidates by proposed tier: 33 total = 17 T1, 11 T2, 5 T3.
- Sub-topics with no T1 candidate: (a) type layer "none, no static types"; (b) schema-validation tooling for boundary parsing (Standard Schema, Zod, Valibot, Ajv, JSON Schema); (c) TypeScript 6.0/7.0 roadmap and TS 7 JSDoc-checking changes; (d) the TC39 type-annotations proposal text itself (T1 only for its Stage 1 status via TYPES-K04).
- Failed fetches on a T1 candidate: none failed outright; partial on TYPES-K05 (digest omitted `erasableSyntaxOnly`, `verbatimModuleSyntax`, `checkJs`) and TYPES-K26 (JSON.parse section text not shown). Non-T1 failures: TYPES-K20 origin PDF (`ECONNREFUSED`, then `403` on the repository copy) and IEEE page (empty).

Tier by id: T1 = K01, K04-K10, K17-K19, K21-K23, K25-K27. T2 = K02, K03, K11-K16, K20, K24, K29. T3 = K28, K30-K33 (all five expect-restricted; K16 is T2 expect-restricted).

Gate abbreviations: G1 authority, G2 currency, G3 grounds, G4 primary, G5 conflict of interest, G6 consistency with T1.

### Candidate table

| id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TYPES-K01 | Modules: TypeScript (type stripping) | Node.js project, official API docs | Official runtime docs, listed T1 | https://nodejs.org/api/typescript.html | yes | docs v26.11.1; stripping Stability 2 (stable) since v25.2.0 and v24.12.0 | official-doc | T1 | G1-G6 pass; G2 ok (current) | type stripping, erasable syntax, tsconfig ignored, `verbatimModuleSyntax` | none |
| TYPES-K02 | proposal-type-annotations (repo) | TC39; champions D. Rosenwasser, R. Cintra, R. Palmer | TC39 delegates, proposal champions | https://github.com/tc39/proposal-type-annotations | yes | Stage 1; last meeting notes 2023-09; README says not updated regularly | maintainer-writing | T2 | G3 mechanism ok; G2 unsure (stalled); not normative | TC39 type annotations, status | none |
| TYPES-K03 | Types as Comments (spec draft) | TC39 proposal editors | Same as K02 | https://tc39.es/proposal-type-annotations/ | yes | no build date shown (digest) | spec | T2 | Stage 1 draft, not normative; G2 unsure | proposal syntax rules | none |
| TYPES-K04 | ECMAScript proposals: stage 1 list | TC39 | The standards committee's own registry | https://raw.githubusercontent.com/tc39/proposals/main/stage-1-proposals.md (and https://github.com/tc39/proposals) | yes | Type Annotations listed Stage 1, last presented 2023-09; no type feature in stage 3 list seen | official-doc | T1 (for status facts only) | G1-G6 pass for status | TC39 proposal status | none |
| TYPES-K05 | TSConfig Reference | TypeScript team (Microsoft) | Handbook and tsconfig reference, listed T1 | https://www.typescriptlang.org/tsconfig/ | yes, partial | covers 5.7+; no page date (digest) | official-doc | T1 | G1-G6 pass; digest omitted `erasableSyntaxOnly`, `verbatimModuleSyntax`, `checkJs` (re-read) | strictness, `strict` family, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes` | none |
| TYPES-K06 | Type Checking JavaScript Files | TypeScript team | Handbook, T1 list | https://www.typescriptlang.org/docs/handbook/type-checking-javascript-files.html | yes | page footer Oct 12, 2026 (digest) | official-doc | T1 | G1-G6 pass; G2 check vs TS 7.0 JS changes | JSDoc-checked JS, how JS differs from TS checking | none |
| TYPES-K07 | JSDoc Reference | TypeScript team | Handbook, T1 list | https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html | yes | footer Oct 12, 2026 (digest) | official-doc | T1 | G1-G6 pass; G6 vs K13 on `@enum` (re-read) | supported JSDoc tags, `@import`, `@satisfies` | none |
| TYPES-K08 | Everyday Types | TypeScript team | Handbook, T1 list | https://www.typescriptlang.org/docs/handbook/2/everyday-types.html | yes | footer Oct 12, 2026 (digest) | official-doc | T1 | G1-G6 pass | `any`, `noImplicitAny`, assertions have no runtime check | none |
| TYPES-K09 | More on Functions (Other Types to Know About) | TypeScript team | Handbook, T1 list | https://www.typescriptlang.org/docs/handbook/2/functions.html | yes | footer Oct 12, 2026 (digest) | official-doc | T1 | G1-G6 pass | `unknown` vs `any` | none |
| TYPES-K10 | Narrowing | TypeScript team | Handbook, T1 list | https://www.typescriptlang.org/docs/handbook/2/narrowing.html | yes | footer Oct 12, 2026 (digest) | official-doc | T1 | G1-G6 pass; does not discuss `unknown` or guard unsoundness | narrowing, type predicates, discriminated unions, exhaustiveness | none |
| TYPES-K11 | Announcing TypeScript 5.8 | D. Rosenwasser, TypeScript team | Principal PM of the TypeScript team | https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/ | yes | 2025-02-28 | maintainer-writing | T2 | G1 ok; G3 mechanism; G5 vendor but facts | `--erasableSyntaxOnly` and Node type stripping | none |
| TYPES-K12 | Announcing TypeScript 6.0 | D. Rosenwasser | Same | https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/ | yes | 2026-03-23 | maintainer-writing | T2 | G1-G6 pass for facts; G5 facts only | `strict` default true, `types` default `[]`, deprecations | none |
| TYPES-K13 | Announcing TypeScript 7.0 | D. Rosenwasser | Same | https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/ | yes | 2026-07-08 | maintainer-writing | T2 | G1-G6 pass for facts; G5 facts only | Go-native compiler, defaults, JS/JSDoc checking rework, no API until 7.1 | none |
| TYPES-K14 | A proposal for type syntax in JavaScript | D. Rosenwasser (proposal champion) | Champion of the proposal | https://devblogs.microsoft.com/typescript/a-proposal-for-type-syntax-in-javascript/ | yes | 2022-03-09 | maintainer-writing | T2 | G1 ok; G2 unsure (2022); G5 vendor position | rationale for types as comments | none |
| TYPES-K15 | microsoft/typescript-go (archived) | Microsoft TypeScript team | Staging repo of the 7.0 native port | https://github.com/microsoft/typescript-go | yes | archived; "native port completed" (digest) | maintainer-writing | T2 | facts only; G5 vendor facts | TS 7 status, declaration emit differences | none |
| TYPES-K16 | Google TypeScript Style Guide | Google | Large engineering organisation, states reasons (listed T2) | https://google.github.io/styleguide/tsguide.html | yes | no date shown (digest) | style-guide | T2 expect-restricted: positions of one organisation, not evidence | G3 partly: reasons stated for most rules; G2 unsure (no date) | `any`/`unknown`, assertions, enums, interface vs type | none |
| TYPES-K17 | typescript-eslint rule: no-explicit-any | typescript-eslint project | Rule docs listed T1 | https://typescript-eslint.io/rules/no-explicit-any | yes | docs v8.71.2 | official-doc | T1 | G1-G6 pass | `any` ban, `fixToUnknown` | QUALITY (08) |
| TYPES-K18 | typescript-eslint rule: no-unsafe-assignment | typescript-eslint project | Same | https://typescript-eslint.io/rules/no-unsafe-assignment | yes | docs v8.71.2 | official-doc | T1 | G1-G6 pass | `any` leaking from untyped sources | QUALITY (08) |
| TYPES-K19 | typescript-eslint shared configs | typescript-eslint project | Same | https://typescript-eslint.io/users/configs/ | yes | no date (digest) | official-doc | T1 | G1-G6 pass | strict vs recommended presets | QUALITY (08) |
| TYPES-K20 | To Type or Not to Type: Quantifying Detectable Bugs in JavaScript | Z. Gao, C. Bird, E. T. Barr; ICSE 2017 | Peer-reviewed, ICSE (listed venue); authors at UCL and Microsoft Research | https://blog.acolyer.org/2017/09/19/to-type-or-not-to-type-quantifying-detectable-bugs-in-javascript (derivative, metadata only). Origin: http://ttendency.cs.ucl.ac.uk/projects/type_study/documents/type_study.pdf and https://ieeexplore.ieee.org/document/7985711 | failed: origin PDF `ECONNREFUSED`; repository copy https://discovery-pp.ucl.ac.uk/id/eprint/10064729/1/typestudy.pdf `403`; IEEE page empty. Stage 2 must retrieve the paper itself | 2017; tools Flow 0.30, TypeScript 2.0 | paper | T2 | G1 ok; G2 unsure (TS 2.0 era, 400 bugs); G4 origin not yet read | effect of static types (about 15% of public bugs detectable) | none |
| TYPES-K21 | Input Validation Cheat Sheet | OWASP Cheat Sheet Series | Listed T1 | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | yes | no date shown (digest) | official-doc | T1 | G1-G6 pass; not JavaScript-specific | allowlists, syntactic vs semantic validation, trust boundaries, JSON schema advice | RUNSEC (06) |
| TYPES-K22 | OWASP ASVS 5.0.0, chapter V2 Validation and Business Logic | OWASP; leaders D. Cuthbert, J. Grossman, E. Lang | Listed T1 | https://raw.githubusercontent.com/OWASP/ASVS/master/5.0/en/0x11-V2-Validation-and-Business-Logic.md (project: https://github.com/OWASP/ASVS) | yes | v5.0.0, May 2025 | spec | T1 | G1-G6 pass; requirements 2.2.1, 2.2.2, 2.2.3 | structure validation, server-side enforcement | RUNSEC (06) |
| TYPES-K23 | Mass Assignment Cheat Sheet | OWASP Cheat Sheet Series | Listed T1 | https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html | yes | no date (digest) | official-doc | T1 | G1-G6 pass; Node/Mongoose section examples dated style, check G2 | allowlisted DTOs at boundaries | RUNSEC (06) |
| TYPES-K24 | Security Applications of Formal Language Theory (Dartmouth TR2011-709) | L. Sassaman, M. L. Patterson, S. Bratus, M. E. Locasto, A. Shubina | Authors with LangSec publication record; technical report, not peer reviewed | https://sergey.cs.dartmouth.edu/langsec/papers/langsec-tr.pdf | yes (title, authors, abstract read via local PDF text; full text not read) | 2011-11-25 | paper | T2 | G1 ok; G3 mechanism; G2 unsure (2011, protocol focus, not JS) | input handling as recognizers; rationale for parse-not-validate | RUNSEC (06) |
| TYPES-K25 | MDN: JSON.parse() | MDN contributors | Listed T1 | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse | yes | last modified 2025-07-20 | official-doc | T1 | G1-G6 pass; no validation guidance on page | `JSON.parse` result untyped, `SyntaxError`, `__proto__`, precision loss | RUNSEC (06) |
| TYPES-K26 | ECMAScript Language Specification, JSON.parse | Ecma TC39 | Normative spec | https://tc39.es/ecma262/#sec-json.parse | yes, partial (digest did not show section text; draft titled ECMAScript 2027) | living draft | spec | T1 | G1-G6 pass; section text must be re-read | JSON grammar has no schema; value returned | LANG (01) |
| TYPES-K27 | Node.js previous releases | Node.js project | Official release policy | https://nodejs.org/en/about/previous-releases | yes | v26 Current (released 2026-05-05), v24 Active LTS (digest) | official-doc | T1 | G1-G6 pass | which lines carry stable type stripping | SUPPLY (07) |
| TYPES-K28 | Standard Schema | `standard-schema` GitHub organisation (individuals not named on page) | Interop spec adopted by schema libraries (adoption not verified from page) | https://github.com/standard-schema/standard-schema | yes | spec v1; MIT; no date on page | maintainer-writing | T3 expect-restricted: facts about the interface only | G1 unsure (authors not named on page); G2 ok | boundary-validation tooling interop | none |
| TYPES-K29 | JSON Schema specification (2020-12) | JSON Schema Organization | Spec publisher; not an IETF publication | https://json-schema.org/specification | yes | version 2020-12 (digest) | spec | T2 (draft until published) | G1 ok; editors not shown on page; G2 unsure (2020-12 current per page) | language-neutral boundary schemas | none |
| TYPES-K30 | Zod documentation | Colin McDonnell (maintainer) | Author of the tool | https://zod.dev/ | yes | Zod 4 stable, v4.6 (digest) | official-doc | T3 expect-restricted: documents its own tool; no normative claims for it (G5) | G5 flagged | parse, `safeParse`, type inference | none |
| TYPES-K31 | Valibot documentation | Fabian Hiller (maintainer) | Author of the tool | https://valibot.dev/guides/introduction/ | yes | no version shown (digest) | official-doc | T3 expect-restricted: same as K30 (G5) | G5 flagged; size claims are vendor claims | `parse`, `safeParse`, `is` | none |
| TYPES-K32 | Ajv documentation | Evgeny Poberezkin (maintainer) | Author of the tool | https://ajv.js.org/ | yes | v8 (digest) | official-doc | T3 expect-restricted: same as K30 (G5) | G5 flagged; has a security section on untrusted schemas | JSON Schema validation in JS | RUNSEC (06) |
| TYPES-K33 | sveltejs/svelte pull request 8569, "TS to JSDoc Conversion" | Svelte maintainers (PR author and discussion) | Maintainers of a major framework | https://github.com/sveltejs/svelte/pull/8569 | yes | closed 2023-05-19, folded into PR 8480 | maintainer-writing | T3 expect-restricted: one project's stated rationale (G5 framework); not evidence for general advice | G3 reasons stated; G1 individual maintainer names not on page; G2 unsure (2023) | JSDoc option rationale | none |

### Dismissed on sight (T4 tally, not listed)

- Opinion and drama coverage of TypeScript/JSDoc moves (trade press, podcasts, forum threads, video-podcast pages, Reddit-style summaries): 11
- Third-party blog or newsletter summaries of the ICSE paper and of Svelte/Turbo decisions (derivatives): 6
- Unattributed Medium or dev.to "TypeScript vs JavaScript" posts and "TypeScript best practices" listicles: 9
- Mirror copies of typescript-eslint docs under unrelated shop or site `node_modules` paths: 5
- News-aggregator and SEO rewrites of the TypeScript 7.0 release (visualstudiomagazine, adtmag, linuxiac, tech-insider, skillbox, for.you.com, InfoQ): 7 (InfoQ and trade press dated 7.0 as 2026-08-03; origin blog says 2026-07-08, origin kept)
- Wikipedia pages: 2
- Academia.edu copy of LangSec report (origin kept): 1

### Searches run

- TypeScript 7.0 native compiler release status
- TypeScript 6.0 release announcement devblogs.microsoft.com
- "To Type or Not to Type: Quantifying Detectable Bugs in JavaScript" ICSE 2017
- Standard Schema specification standardschema.dev TypeScript validation libraries
- Security Applications of Formal Language Theory LangSec Sassaman Patterson Bratus Shubina IEEE Systems Journal
- typescript-eslint no-explicit-any no-unsafe-assignment strict-type-checked configs docs
- Svelte moved from TypeScript to JSDoc Rich Harris Turbo 8 drops TypeScript DHH JSDoc type checking
- Svelte Rich Harris "JSDoc" sveltejs github "TypeScript" source conversion explanation .js files types
- DHH "Open Source Hooliganism and the TypeScript Meltdown"

Direct fetches also covered the Node TypeScript page, TC39 proposal repos and registry, TypeScript handbook and blog, typescript-eslint, OWASP, MDN, ECMA-262, Node release page, Svelte docs, Zod, Valibot, Ajv, JSON Schema. Svelte's TypeScript docs page (https://svelte.dev/docs/svelte/typescript) was fetched and not listed: it says nothing on JSDoc as an alternative.
