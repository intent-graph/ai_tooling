# Discovery result: slot 04_struct (code organization and APIs)

## L1 headline

Authoritative sources cover the mechanics of this area well (ES modules, cycles, side effects, classes, private state, function signatures) and its design rationale poorly (dependency direction, paradigm choice, naming, state structure); certainty: grounded for what was fetched, inferred for sub-topic coverage beyond each page's headings.

Pinned:
- Number of candidates by proposed tier: T1 = 16, T2 = 11, T3 = 8 (of which 6 expect-restricted: K30 to K35). Total 35. T4 not listed; dismissal tally in L3.
- Sub-topics with no T1 candidate: dependency direction (layering between modules; only T2 K21 and the enforcement mechanism K16), paradigm choice (OOP vs FP vs imperative; T2 only: K22, K25), naming (T2 only: K17, K19, K23, K24), state structure and design (T1 covers only the language mechanics: live bindings, closures, private fields; state-structure design has T2 K26 and restricted T3 K34, K35 only).
- Failed fetches on a T1 candidate: none. Partial: K01 (ECMA-262) returned only its table of contents, so section 16 is confirmed to exist but its subsection titles and numbers are unverified (a full read is the extraction stage's job). Three PDFs (K21, K22, K23) were not readable by the fetch tool; I read their first page from the saved file.

## L2 claims

Sub-topics (each: best candidates by id and tier; T1 present or not). Marks: grounded = fetched and checked, inferred = from headings or snippets only, open = nothing found.

- ES modules (syntax, live bindings, default vs named, resolution, packages): K01 T1, K02 T1, K03 T1, K04 T1, K05 T1, K06 T1, K10 T1; has T1. grounded.
- Dependency direction (cycles, layering, barrel files): cycles have T1: K02 (documents cyclic imports and cycle-elimination moves), K01 (inferred, Cyclic Module Records), K07 (CommonJS cycles). Layering rule has no T1: K21 T2 (information hiding, 1972, not JS), K16 T1 as mechanism only, K30 T3 (cycles "dangerous anti-pattern" is the maintainers' stance), K28 T3 (barrel-file measurements). Cycles grounded; layering open as a principle.
- Side-effect-free imports: K03 T1 (side-effect-only import form), K02 T1 (top-level execution), K08 T1 (top-level await ordering), K05 T1, K07 T1 (require executes and caches), K09 T1 (side-effect imports in TS), K29 T3 (sideEffects flag; bundler convention not in Node docs: K06 says so). Has T1 for the language fact; the "sideEffects" convention is T3 only. grounded.
- Paradigm choice: K22 T2 (objects vs abstract data types, essay), K25 T2 (language and defects, effect sizes tiny; reproduction), K33 T3 restricted (authors' rebuttal), K13 T1 (JS has prototypes; classes are sugar), K14 T1 (closures). No T1 for the choice itself. grounded for facts, open for guidance.
- Naming: K23 T2 (words beat letters and abbreviations, 72 C# developers), K24 T2 (developers rarely choose the same name; 334 subjects), K17 and K19 T2 (conventions with stated rationale), K19 T2 (W3C TAG naming). K32 T3 restricted. No T1. grounded.
- Function API design: K11 T1 (TypeScript do's and don'ts, with a "why" per rule), K15 T1 (max-params, with rationale), K19 T2 (options dictionaries, optional arguments), K17 T2 (destructuring, rest, defaults), K27 T2 (breaking changes in minor and patch releases, 44%). Has T1. grounded.
- Object API design (classes, encapsulation, extension): K12 T1 (hard privacy), K13 T1 (never extend built-ins; setPrototypeOf cost), K14 T1 (closure privacy), K19 T2 (constructors only when state exists), K18 T2. Has T1. grounded.
- State: language mechanics K02, K03, K04 (live bindings), K07 (module cache as singleton), K12, K14 T1; K18 and K17 T2 (no mutating exports); K26 T2 (immutability support, interviews); K34, K35 T3 restricted (framework state rules). No T1 for state-structure design. grounded for mechanics, open for design.

Disagreements between candidates (list all positions):
- Default exports: K18 (Google TS) forbids them with a stated reason (no canonical name); K17 (Google JS) forbids them; K32 (Airbnb rule 10.6) prefers a default export for a single-export module; K04 (MDN) takes no side. Later stages need all four.
- Barrel files and aggregating modules: K02 (MDN) presents aggregating as a normal technique; K28 (measurements) says remove all barrel files; K20 (V8) recommends small fine-grained modules; K32 (Airbnb 10.3) bans exporting directly from an import.
- Private-member convention: K32 forbids leading and trailing underscores; K17 allows a trailing underscore for private methods; K12 (MDN) says `#` is the only hard privacy.
- Module format for new packages: K31 (Sorhus) advises pure ESM even after Node 22 `require(esm)`; K07 and K05 (Node docs) document `require(esm)` as supported for synchronous modules.
- Paradigm evidence: K25 reports tiny effects for language and defects; K33 (original authors) says the reproduction largely agrees with them and their conclusion holds. Positions differ on interpretation, not data.
- Cycles: K02 shows cycles can work when bindings are used lazily; K30 and K17 treat them as always to be removed.

Gaps (what I searched):
- Dependency direction / layering as a principle: no T1 or JS-specific T2; searched empirical JS cyclic dependency studies and found none peer-reviewed (one CommonJS bloat preprint, dismissed). open.
- Naming in JavaScript specifically: both empirical naming studies use other languages (K23 C#; K24 language not stated in the abstract). inferred transferability.
- State design: no TC39 or runtime document gives a state-structure rule; only vendor guides. open.
- Paradigm choice for JavaScript: no JS-specific empirical study found. open.
- Spec subsection detail for K01 not seen (see Pinned).

## L3 full

### Candidates

Format per row: id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary.

**Proposed T1 (16)**

- STRUCT-K01 | ECMAScript Language Specification, section 16 (Scripts and Modules) | Ecma TC39 | the normative standard | https://tc39.es/ecma262/ (also the multipage section page) | yes, table of contents only; module subsections not fully seen | ECMAScript 2027 draft, no update date shown | spec | T1 | G1 to G6 pass; G6 is the reference itself; unsure only that subsection numbers are unchecked | module evaluation order, cyclic module records, import bindings | LANG
- STRUCT-K02 | JavaScript modules (guide) | MDN contributors | MDN reference page (T1 by policy); no named author | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules | yes | last modified 2026-08-21 | official-doc | T1 | pass; G1 holds by policy (MDN page), no individual author | default vs named exports, aggregating modules, cyclic imports, top-level await, dynamic import, module-scope singletons | none
- STRUCT-K03 | import statement | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import | yes | last modified 2026-09-11 | official-doc | T1 | pass | side-effect-only import, live bindings, hoisting, import attributes | none
- STRUCT-K04 | export statement | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export | yes | last modified 2026-09-15 | official-doc | T1 | pass | default vs named exports (neutral), re-exporting, live bindings | none
- STRUCT-K05 | Node.js API: ECMAScript modules | Node.js project | official runtime docs | https://nodejs.org/api/esm.html | yes | v26.11.1, stability 2 | official-doc | T1 | pass | ESM in Node, `exports`, top-level await, CommonJS interop | none
- STRUCT-K06 | Node.js API: Modules, packages | Node.js project | official runtime docs | https://nodejs.org/api/packages.html | yes | v26.11.1 | official-doc | T1 | pass | `exports` encapsulation, `type` field, dual-package pointer; confirms `sideEffects` is not a Node field | package boundaries and public surface | SUPPLY (once)
- STRUCT-K07 | Node.js API: Modules, CommonJS | Node.js project | official runtime docs | https://nodejs.org/api/modules.html | yes | v26.11.1 | official-doc | T1 | pass; G2 holds because it documents `require(esm)` for current Node | cycles in CommonJS, module cache as singleton, execution on require, `require(esm)` | none
- STRUCT-K08 | Top-level await proposal | TC39; champions Myles Borins and Yulia Startsev | stage 4, in ES2022 | https://github.com/tc39/proposal-top-level-await | yes | stage 4, ES2022 | spec | T1 | pass | module ordering semantics, async initialization, footgun critique | ASYNC
- STRUCT-K09 | TSConfig reference: verbatimModuleSyntax, isolatedModules | TypeScript team | TypeScript tsconfig reference (T1 by policy) | https://www.typescriptlang.org/tsconfig/ | yes | no date shown | official-doc | T1 | pass; G5 neutral (compiler docs) | import type, side-effect imports, import preservation | TYPES
- STRUCT-K10 | TypeScript handbook: Modules, theory | TypeScript team; contributors Andrew Branch, Rob Palmer, Max Schwenk, Filip Sodic | handbook | https://www.typescriptlang.org/docs/handbook/modules/theory.html | yes | updated 2026-10-12 | official-doc | T1 | pass | scripts vs modules, ESM and CJS interop, resolution is host-defined | TYPES
- STRUCT-K11 | TypeScript handbook: Do's and Don'ts | TypeScript team | handbook | https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html | yes | updated 2026-10-12 | official-doc | T1 | pass; written for declaration files, so scope to API shape is inferred | overloads vs optional parameters, callback arity, unions over overloads | TYPES
- STRUCT-K12 | Private elements | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements | yes | last modified 2025-07-08 | official-doc | T1 | pass | hard privacy, no inheritance of private elements | LANG
- STRUCT-K13 | Inheritance and the prototype chain | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain | yes | no date captured | official-doc | T1 | pass; G2: documents ES5-era constructor functions next to classes, read with care | classes as sugar, never extend built-ins, setPrototypeOf cost | LANG
- STRUCT-K14 | Closures | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures | yes | no date captured | official-doc | T1 | G2 unsure: examples use `var` and IIFE, a pattern the policy flags; use for the mechanism only | closure-based private state, factory functions | LANG
- STRUCT-K15 | ESLint rule: max-params | ESLint team | ESLint rule docs (T1 by policy) | https://eslint.org/docs/latest/rules/max-params | yes | rule since v0.0.9; default max 3 | official-doc | T1 | G3 pass (reason: memorizing order and types); the threshold of 3 is a default, not evidence | parameter count | QUALITY
- STRUCT-K16 | ESLint rule: no-restricted-imports | ESLint team | ESLint rule docs | https://eslint.org/docs/latest/rules/no-restricted-imports | yes | since v2.0.0-alpha-1 | official-doc | T1 | pass; grounds the mechanism for enforcing import direction, not the principle | enforcing import rules by path and pattern | QUALITY

**Proposed T2 (11)**

- STRUCT-K17 | Google JavaScript Style Guide | Google | large engineering organization stating reasons | https://google.github.io/styleguide/jsguide.html | yes | no date shown; page says it is no longer maintained | style-guide | T2 | G2 unsure: not maintained, still permits goog.module and a prototype fallback; G3 mixed (rules are stated as enforceable conventions, few reasons) | named exports only, no mutated exports, naming, classes, parameters | none
- STRUCT-K18 | Google TypeScript Style Guide | Google | same | https://google.github.io/styleguide/tsguide.html | yes | no date shown | style-guide | T2 | pass; G3 pass (states why: default exports have no canonical name, mutable exports hurt re-exports) | default vs named exports, no namespaces, interface vs type, destructured options | TYPES
- STRUCT-K19 | Web Platform Design Principles | W3C TAG; editors Jeffrey Yasskin and former editors Martin Thomson, Lea Verou, Sangwhan Moon, Domenic Denicola, Travis Leithead | W3C Group Note | https://www.w3.org/TR/design-principles/ | yes | Group Note, 2026-09-14 | spec | T2 (a Note is not normative) | pass; G3 pass | options dictionaries, optional arguments, naming, constructors only for stateful objects, errors | ASYNC (promises and AbortSignal sections)
- STRUCT-K20 | JavaScript modules (V8 feature page) | Addy Osmani and Mathias Bynens (V8 and Chrome team) | V8 team writing | https://v8.dev/features/modules | yes | 2018-06-18 | maintainer-writing | T2 | G2 unsure: eight years old, adoption figures stale; use for the mechanism and the bundling advice only | fine-grained modules, deferred module scripts, bundling advice | none
- STRUCT-K21 | On the Criteria To Be Used in Decomposing Systems into Modules | D. L. Parnas, Communications of the ACM 15(12) | foundational paper on information hiding | https://www.cse.sc.edu/~mgv/csce590f20/ParnasCriteria.pdf | yes, first page via saved file | 1972 | paper | T2 | G2: pre-ES2015 and not about JavaScript, so it grounds a principle, not a JS rule; G3 pass | what a module hides, decomposition criterion | none
- STRUCT-K22 | On Understanding Data Abstraction, Revisited | William R. Cook, University of Texas at Austin | OOPSLA 2009 essay; Cook is a programming-languages researcher | https://www.cs.utexas.edu/~wcook/Drafts/2009/essay.pdf | yes, first page via saved file (draft copy; a published copy should be sought) | 2009 | paper | T2 | G2 unsure (language-agnostic); G3 pass | objects vs abstract data types, paradigm choice | none
- STRUCT-K23 | Shorter Identifier Names Take Longer to Comprehend | Hofmeister, Siegmund, Holt, SANER 2017 | peer-reviewed | https://www.se.cs.uni-saarland.de/publications/docs/HoSeHo17.pdf | yes, first page via saved file | 2017 | paper | T2 | G2 unsure: 72 professional C# developers, not JavaScript; G3 pass | identifier naming | none
- STRUCT-K24 | How Developers Choose Names | Dror G. Feitelson and co-authors, IEEE Transactions on Software Engineering | peer-reviewed | https://arxiv.org/abs/2103.07487 | yes (abstract page; the journal copy not fetched) | 2021 preprint, TSE volume 48 (2022) | paper | T2 | G2 unsure (language not stated in the abstract) | naming process, name agreement of 6.9% | none
- STRUCT-K25 | On the Impact of Programming Languages on Code Quality: A Reproduction Study | Berger, Hollenbeck, Maj, Vitek, Vitek, TOPLAS | peer-reviewed reproduction of Ray et al. | https://arxiv.org/abs/1901.10220 | yes (abstract page) | 2019 | paper | T2 | pass; the abstract does not mention JavaScript or paradigms, coverage to check in extraction | evidence on language vs defects | none
- STRUCT-K26 | Exploring Language Support for Immutability | Coblenz, Sunshine, Aldrich, Myers, Weber, Shull, ICSE 2016 | peer-reviewed | https://www.cs.cmu.edu/~jssunshi/assets/pdf/coblenz2016exploring.pdf | yes (fetch tool returned title, venue and topic only; the method and findings in this row come from search snippets) | 2016 | paper | T2 | G2 unsure (Java-oriented); G3 pass | immutability, restricting state change | LANG
- STRUCT-K27 | I Depended on You and You Broke Me | Venturini, Cogo, Polato, Gerosa, Wiese, TOSEM 2023 | peer-reviewed, npm ecosystem | https://arxiv.org/abs/2301.04563 | yes (abstract page) | 2023 | paper | T2 | pass | breaking changes in minor and patch releases (44%), why API surface stability matters | SUPPLY

**Proposed T3 (8)**

- STRUCT-K28 | The barrel file debacle | Marvin Hagemeister | personal blog with measurements; his standing (Preact core team) was not shown on the fetched page | https://marvinh.dev/blog/speeding-up-javascript-ecosystem-part-7/ | yes | 2023-10-08 | maintainer-writing | T3 | G1 unsure; G3 pass (module-count timings); G6 unsure | barrel files, module graph size | none
- STRUCT-K29 | Tree shaking guide | webpack project | tooling docs | https://webpack.js.org/guides/tree-shaking/ | yes | no date shown | official-doc | T3 | G5: bundler docs, admit for facts; the `sideEffects` flag is a bundler convention not in Node docs | side-effect-free modules, `sideEffects` flag, pure annotations | none
- STRUCT-K30 | eslint-plugin-import, rule no-cycle | import-js organization | plugin docs | https://github.com/import-js/eslint-plugin-import/blob/main/docs/rules/no-cycle.md | yes | no date shown | official-doc | T3, expect-restricted: positions only ("always a dangerous anti-pattern" is the maintainers' opinion, no evidence given) | G3 weak | cycle ban | QUALITY
- STRUCT-K31 | Pure ESM package | Sindre Sorhus | prolific package maintainer, not a spec or runtime role | https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c | yes | updated 2026-10-11 | maintainer-writing | T3, expect-restricted: opinion; G2 unsure against K05 and K07 | G3 weak | publishing as pure ESM | SUPPLY
- STRUCT-K32 | Airbnb JavaScript Style Guide | Airbnb | popular style guide | https://github.com/airbnb/javascript | yes (raw README) | no date captured | style-guide | T3, expect-restricted: positions only, never evidence; stars do not count | G3 mixed ("Why?" notes on many rules) | default export preference (10.6), no export-from, naming, no underscores | none
- STRUCT-K33 | Rebuttal to Berger et al., TOPLAS 2019 | Baishakhi Ray, Prem Devanbu, Vladimir Filkov | authors of the original study | https://arxiv.org/pdf/1911.07393 | yes, first page via saved file | 2019 | paper | T3, expect-restricted: the authors' position; not peer-reviewed as far as I could see | G1 pass | the other side of K25 | none
- STRUCT-K34 | Choosing the state structure | React team | framework docs | https://react.dev/learn/choosing-the-state-structure | yes | no date shown | official-doc | T3, expect-restricted: React-specific facts; G5 | G3 mixed | state grouping, redundancy, duplication, flat shape | FRAMEWORKS
- STRUCT-K35 | Redux style guide | Redux maintainers | library docs | https://redux.js.org/style-guide/ | yes | no date shown | style-guide | T3, expect-restricted: Redux-specific positions; G5 | G3 mixed | do not mutate state, normalize, derive instead of store | FRAMEWORKS

Tier count check: T1 K01 to K16 = 16; T2 K17 to K27 = 11; T3 K28 to K35 = 8; total 35. Of the T3, expect-restricted: K30, K31, K32, K33, K34, K35 (six).

### Dismissed on sight (tally of what my searches returned)

- Unattributed or personal blog posts on default exports, circular dependencies and module patterns (dev.to 1, ilikekillnerds 1, hackernoon 1, atomicobject 1, bryanbraun 1, javascriptweekly link 1): 6
- Course pages (educative 1, devpath 1): 2
- Vendor detector docs (xygeni cyclic-dependency detector): 1
- Slide decks and paper summaries (slideshare 1, neverworkintheory 1): 2
- Mailing-list threads and bug archives (esdiscuss 2, tc39 bugzilla 2, W3C list 1): 5, not examined, opinion threads
- Preprint outside the area (CommonJS bloated dependencies, arXiv 2405.17939): 1, not peer reviewed, belongs to SUPPLY
- Stack Overflow: 0 appeared; none sought

### Searches run

- Hofmeister Siegmund Holt shorter identifier names SANER 2017
- Berger reproduction study programming languages code quality TOPLAS
- Parnas criteria decomposing systems into modules 1972 CACM
- empirical study JavaScript circular dependencies ES modules npm
- empirical study JavaScript API design breaking changes npm semantic versioning
- empirical study immutability programmer productivity Coblenz Glacier
- Feitelson How Developers Choose Names TSE 2021
- Cook On Understanding Data Abstraction Revisited OOPSLA 2009
- Coblenz Exploring Language Support for Immutability ICSE 2016
- TC39 or Node writing on default exports harmful, rationale
- Direct fetches (no search) of the MDN, Node, TypeScript, ESLint, Google, W3C, V8, webpack, Rollup (dropped from the list as weaker than webpack's page), typescript-eslint naming-convention (dropped: rule is frozen), StandardJS (dropped: no named maintainers, restricted-only), React, Redux and Airbnb pages
