# Discovery result: slot 08 QUALITY (static checks, tests, CI gates)

## L1 headline

Linting and CI-gate mechanics are well covered by T1 tool and OpenSSF documentation; testing strategy, formatting choice, property-based testing and coverage-as-quality rest on T2 papers and T3 tool docs only. Certainty: grounded for what I fetched, inferred for tier proposals (the auditor decides).

Pinned:
- Candidates by proposed tier: T1: 11, T2: 9, T3: 14 (34 in total; T4: none listed).
- Sub-topics with no T1 candidate: formatting (formatter choice and settings; K02 only states that ESLint's own formatting rules are deprecated); testing strategy (pyramid, test size, flakiness, behaviour over implementation); property-based tests; browser and component test runners (only `node:test` has a T1). Coverage has a T1 only for the mechanism (K06), none for coverage as a quality target.
- Failed fetches on a T1 candidate: none. (Failed on non-T1: ACM DOI page for K14 returned 403, read the author-hosted PDF instead; ResearchGate for K13 returned 403, read the university-hosted PDF instead.)

## L2 claims

Per sub-topic (best candidates, T1 present?). All lines grounded unless marked.

- Linting rule sets: K01, K02, K04, K05 (T1), K12 (T2), K19, K20 (T2). T1 present. Grounded.
- Linting in typed code: K04 (configs, "strict" only if the team is proficient), K05 (typed linting costs a TypeScript build). T1 present. Grounded. Boundary TYPES.
- Formatting: K12 (T2, ESLint TSC member: formatting rules deprecated, Prettier or dprint advised), K21, K22, K23 (T3, Prettier docs), K24 (T3). No T1. Grounded that none exists under the policy's T1 list; Prettier is a tool maintainers' doc, T3.
- Testing runners: K06, K07 (T1, Node built-in runner, stable, mocking, coverage, `--test-randomize`; strict assert recommended); K25, K27, K28 (T3, Vitest, Jest, Playwright). T1 for Node only. Grounded.
- Testing strategy: K17, K18 (T2, Google engineers, book), K16 (T2, flaky-test study), K29 (T3, restricted). No T1. Grounded.
- Property-based tests: K13 (T2, origin: QuickCheck paper), K30 (T3, fast-check docs). No T1. Grounded; K13 year (2000) is inferred from knowledge, not on the fetched text.
- Coverage: K06 (T1, how Node collects it), K26 (T3, V8 vs Istanbul provider accuracy), K14 (T2, coverage is a weak effectiveness signal; Java systems only), K15 (T2, mutation testing at scale), K31 (T3). T1 only for mechanism. Grounded.
- CI gates: K03 (T1, exit codes, `--max-warnings`, `--report-unused-disable-directives`), K08, K09, K10 (T1, OpenSSF), K11 (T1, `npm ci`), K23 (T3, `prettier --check`), K33 (T3, restricted vendor facts). T1 present. Grounded.

Disagreements (both positions kept for later stages):
- Formatting inside or beside the linter: K12 and K02 (ESLint deprecates formatting rules, points to formatters or a community stylistic plugin) vs K24 (Biome ships linter and formatter in one tool); K22 (Prettier: do not run Prettier as a lint rule) vs the ESLint-plugin route. Grounded.
- Coverage as a target: K14 ("should not be used as a quality target") vs K09 (OpenSSF criteria: tests should cover most branches) and K08 (Scorecard rewards presence of CI tests). K14 studied Java suites: transfer to JavaScript is inferred.
- Test mix: K17/K18 (about 80 percent unit, 15 integration, 5 end to end) vs K28 and K29 (user-behaviour tests as the confidence source). Grounded.
- Style guides: K19 (Google JS, formatting by clang-format, 80 columns, discontinued in favour of TypeScript) vs K32 (Airbnb, different rules) vs Prettier defaults (K21). Positions only.

Gaps:
- OpenSSF npm best-practices guide named in the plan: only an archived repository (K-none, archived 2023) turned up; the published guide location is not confirmed. Open. Belongs mainly to slot 07 SUPPLY.
- No T1 or T2 source found for numeric coverage thresholds. Searched: Node docs, Vitest docs, K14, K26. Open.
- Fuzzing for JavaScript (Scorecard lists it as a check, K08): no JavaScript-specific authoritative source fetched. Open.
- Snapshot testing and mocking policy: only tool docs (K06, K25) seen. Open.
- ESLint pages show a version (v10.12.0) but no last-updated date; dates recorded as versions.

## L3 full

Fields per row: title; author or body; standing; url; fetched; date or version; kind; proposed tier; gates; covers; boundary. Fetch was by WebFetch; PDFs were read from the saved copy with pdftotext. Gate notes: G1 to G6 as in the plan, unsure gates named.

### T1

- **QUALITY-K01** ESLint: Configuration Files. ESLint project (OpenJS Foundation project docs). Standing: official docs of the linter. https://eslint.org/docs/latest/use/configure/configuration-files. fetched: yes. version v10.12.0, no page date. kind official-doc. T1. gates: G1 to G6 pass; G2 current (flat config). covers: linting rule sets, config structure. boundary: none.
- **QUALITY-K02** ESLint: Rules Reference. ESLint project. Standing: official docs. https://eslint.org/docs/latest/rules/. fetched: yes. v10.12.0. official-doc. T1. gates pass. covers: rule categories, recommended set, formatting rules deprecated (partial formatting). boundary: none.
- **QUALITY-K03** ESLint: Command Line Interface. ESLint project. https://eslint.org/docs/latest/use/command-line-interface. fetched: yes. v10.12.0. official-doc. T1. gates pass. covers: CI gates (exit codes, max-warnings, unused disable directives, cache). boundary: none.
- **QUALITY-K04** typescript-eslint: Shared Configs. typescript-eslint project. Standing: maintainers' official docs, named in the plan's T1 list. https://typescript-eslint.io/users/configs. fetched: yes. v8.71.2. official-doc. T1. gates pass. covers: rule-set choice (recommended, strict, stylistic, type-checked). boundary: TYPES.
- **QUALITY-K05** typescript-eslint: Linting with Type Information. same body. https://typescript-eslint.io/getting-started/typed-linting. fetched: yes. v8.71.2. official-doc. T1. gates pass. covers: typed linting and its cost in CI. boundary: TYPES.
- **QUALITY-K06** Node.js: Test runner (`node:test`). Node.js project. Standing: official runtime docs, named in plan T1 list. https://nodejs.org/api/test.html. fetched: yes. Node v26.11.1, Stability 2 (Stable). official-doc. T1. gates pass; the coverage flag is still named experimental, check at audit. covers: runners, mocking, coverage mechanism, reporters, randomized order. boundary: none.
- **QUALITY-K07** Node.js: Assert. Node.js project. https://nodejs.org/api/assert.html. fetched: yes. v26.11.1, Stable. official-doc. T1. gates pass. covers: assertion style (strict mode recommended, legacy mode uses `==`). boundary: LANG (equality).
- **QUALITY-K08** OpenSSF Scorecard: Checks. OpenSSF. Standing: OpenSSF project documentation, named in plan T1 list. https://github.com/ossf/scorecard/blob/main/docs/checks.md. fetched: yes. no date seen (main branch). official-doc. T1. gates: G5 unsure (a scoring tool describing its own checks; use as facts about the checks). covers: CI gates (CI-Tests, SAST, Fuzzing, Branch-Protection, Token-Permissions, Pinned-Dependencies). boundary: SUPPLY.
- **QUALITY-K09** OpenSSF Best Practices Badge criteria (passing). OpenSSF (LF Projects). https://www.bestpractices.dev/en/criteria/0. fetched: yes. no date seen. official-doc. T1. gates pass; G3 partly criteria not mechanisms. covers: automated test suite, tests for new features, static analysis, warning flags. boundary: none.
- **QUALITY-K10** Concise Guide for Developing More Secure Software. OpenSSF Best Practices WG. https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software. fetched: yes. 2023-06-14 on page. official-doc. T1. gates: G3 unsure (recommendations are short). covers: static analysis in CI, negative tests. boundary: SUPPLY (dependency cooldown), RUNSEC.
- **QUALITY-K11** npm CLI: `npm ci`. npm project docs. https://docs.npmjs.com/cli/v11/commands/npm-ci. fetched: yes. npm v11 docs, no date. official-doc. T1. gates pass. covers: reproducible CI install. boundary: SUPPLY.

### T2

- **QUALITY-K12** Deprecation of formatting rules. Nicholas C. Zakas, ESLint TSC. https://eslint.org/blog/2023/10/deprecating-formatting-rules/. fetched: yes. 2023-10-26. maintainer-writing. T2. gates: G2 ok (rules still present through v10). covers: formatting vs linting, reasons. boundary: none.
- **QUALITY-K13** QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs. Koen Claessen, John Hughes (Chalmers). Standing: authors of the origin of property-based testing. https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf (university-hosted copy). fetched: yes (ACM and ResearchGate copies failed, 403). date: ICFP 2000 (inferred, not on fetched page). paper. T2. gates: G2 unsure (Haskell, 2000, concept not tooling); G4 pass (origin). covers: property-based tests. boundary: none.
- **QUALITY-K14** Coverage Is Not Strongly Correlated with Test Suite Effectiveness. Laura Inozemtseva, Reid Holmes (Waterloo). https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf. fetched: yes (author-hosted PDF; ACM DOI 403). ICSE 2014 (per search results, distinguished paper award). paper. T2. gates: G2 unsure (2014), G3 pass (31,000 suites, five Java systems). covers: coverage as quality target. boundary: none.
- **QUALITY-K15** Practical Mutation Testing at Scale: A View from Google. Goran Petrovic, Marko Ivankovic, Gordon Fraser, Rene Just. https://arxiv.org/abs/2102.11378. fetched: yes (abstract page). arXiv Feb 2021; IEEE TSE 2021 per search results. paper. T2. gates: G5 unsure (company-internal evidence, authors include academics). covers: mutation testing beyond coverage. boundary: none.
- **QUALITY-K16** An Empirical Analysis of Flaky Tests. Qingzhou Luo, Farah Hariri, Lamyaa Eloussi, Darko Marinov (UIUC). https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf (course mirror). fetched: yes (ACM copy not tried). FSE 2014 (per search results). paper. T2. gates: G2 unsure (2014, 51 projects, mostly Java and C); G4 pass. covers: flaky-test causes, testing strategy. boundary: ASYNC (async wait causes).
- **QUALITY-K17** Software Engineering at Google, ch. 11 Testing Overview. Adam Bender (author), Tom Manshreck (editor). https://abseil.io/resources/swe-book/html/ch11.html. fetched: yes. book edition 2020, no date on page. book. T2. gates: G3 pass (stated reasons), G1 pass; named technical review not checked. covers: test sizes, pyramid ratios, flakiness. boundary: none.
- **QUALITY-K18** Software Engineering at Google, ch. 12 Unit Testing. Same book. https://abseil.io/resources/swe-book/html/ch12.html. fetched: yes. T2. gates as K17. covers: test behaviours, brittle tests, DAMP vs DRY. boundary: none.
- **QUALITY-K19** Google JavaScript Style Guide. Google. https://google.github.io/styleguide/jsguide.html. fetched: yes. page says no longer updated; migrate to TypeScript. style-guide. T2. gates: G2 unsure (discontinued, ES2015+ era but frozen). covers: linting and formatting positions, tooling. boundary: LANG, STRUCT.
- **QUALITY-K20** Google TypeScript Style Guide. Google. https://google.github.io/styleguide/tsguide.html. fetched: yes. no date on page. style-guide. T2. gates pass; opinion recorded as holder's. covers: tooling rules (no `@ts-ignore`), formatting positions. boundary: TYPES.

### T3

- **QUALITY-K21** Prettier: Rationale. Prettier project. Standing: formatter maintainers' docs. https://prettier.io/docs/rationale. fetched: yes. no date. official-doc. T3. gates: G5 unsure (tool's own docs). covers: formatting. boundary: none.
- **QUALITY-K22** Prettier: Integrating with Linters. Prettier project. https://prettier.io/docs/integrating-with-linters. fetched: yes. no date. T3. gates as K21. covers: formatter and linter split. boundary: none.
- **QUALITY-K23** Prettier: CLI (`--check`, `--write`). Prettier project. https://prettier.io/docs/cli#--check. fetched: yes. T3. covers: CI format gate, exit codes. boundary: none.
- **QUALITY-K24** Biome: Linter. Biome project. https://biomejs.dev/linter/. fetched: yes. v2.x docs, 568 rules. official-doc. T3. gates: G5 unsure (alternative tool, vendor-like). covers: single-tool lint and format alternative. boundary: none.
- **QUALITY-K25** Vitest: Getting Started. Vitest contributors (VoidZero Inc.). https://vitest.dev/guide/. fetched: yes. v5.0.4. T3. gates: G5 unsure (backed by a company). covers: runner choice. boundary: none.
- **QUALITY-K26** Vitest: Coverage. same. https://vitest.dev/guide/coverage.html. fetched: yes. v5.0.4. T3. covers: V8 vs Istanbul accuracy, thresholds. boundary: none.
- **QUALITY-K27** Jest: Getting Started. Jest, OpenJS Foundation. https://jestjs.io/docs/getting-started. fetched: yes. v30.5. T3. covers: runner choice. boundary: none.
- **QUALITY-K28** Playwright: Best Practices. Microsoft. https://playwright.dev/docs/best-practices. fetched: yes. no date. T3. expect-restricted: vendor documentation, facts about the tool; its normative advice is the vendor's position (G5). covers: end-to-end tests, isolation, CI. boundary: none.
- **QUALITY-K29** Testing Library: Guiding Principles. Kent C. Dodds and contributors. https://testing-library.com/docs/guiding-principles/. fetched: yes. page dated 2020-11-04. T3. expect-restricted: positions only; G3 unsure (opinion, no evidence). covers: testing strategy (user-visible behaviour). boundary: none.
- **QUALITY-K30** fast-check documentation and repository. Nicolas Dubien (maintainer). https://fast-check.dev/docs/introduction/ and https://github.com/dubzzz/fast-check. fetched: yes. docs page updated 2026-08-18; v5.x. T3. gates: G1 pass (maintainer-named), G5 pass. covers: property-based tests in JavaScript, shrinking. Seeds not on the introduction page; read other pages at extraction. boundary: none.
- **QUALITY-K31** StrykerJS introduction. Stryker team (Info Support). https://stryker-mutator.io/docs/stryker-js/introduction/. fetched: yes. no version on page. T3. gates: G5 unsure. covers: mutation testing tool. boundary: none.
- **QUALITY-K32** Airbnb JavaScript Style Guide. Airbnb. https://github.com/airbnb/javascript. fetched: yes. ES2015+ target, states reasons. style-guide. T3. expect-restricted: popular guide, admitted as that guide's position only, never as evidence (plan standing rule). gates: G3 partial, G2 unsure (last release date not seen). covers: linting rule-set positions. boundary: LANG.
- **QUALITY-K33** GitHub Docs: About protected branches. GitHub. https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches. fetched: yes. no date. T3. expect-restricted: vendor facts about its platform only (G5). covers: required status checks and reviews as CI gates. boundary: SUPPLY.
- **QUALITY-K34** eslint-plugin-security. eslint-community. https://github.com/eslint-community/eslint-plugin-security. fetched: yes. 16 rules, flat-config support. T3. expect-restricted: maintainers state it yields many false positives. covers: lint rules for security. boundary: RUNSEC (listed here once).

### Dismissed on sight (tally)

I built candidates from known origin URLs (tool docs, specs, papers) and ran only four web searches, all aimed at locating a specific paper. No search result page of general advice was opened, so the tally is small and is weak evidence that the filter ran:
- Search results seen and not opened: 0 listicles, 0 SEO tutorials, 0 Medium or dev.to posts (the searches were title-exact).
- Considered by name and not fetched: tutorial and course sites, Stack Overflow, "best testing libraries" listicles: dismissed without a count.
- Candidates considered and dropped for the area: a practical-test-pyramid article on a well-known engineer's site (derivative of earlier writing, G4), a GitHub code-scanning page (security SAST, sibling area), an archived package-manager best-practices repository (archived 2023-10, G2), GitHub Actions secure-use reference (sibling SUPPLY), StandardJS (second popular guide, same restriction as K32), a Google testing-blog coverage post (restates the book and mutation papers, G4).

### Searches run

- Inozemtseva Holmes "Coverage is not strongly correlated with test suite effectiveness" ICSE 2014 pdf
- Petrovic Ivankovic Fraser Just "Practical mutation testing at scale" Google ICSE
- Luo Hariri Eloussi Marinov "An empirical analysis of flaky tests" FSE 2014
- (fetches by URL, no query) ESLint, typescript-eslint, Prettier, Biome, Node.js, Vitest, Jest, Playwright, Testing Library, fast-check, Stryker, OpenSSF, npm, GitHub, Google style guides and book
