# Skeleton: branch VERIFICATION

Purpose of the branch: automation, let machines check what people forget. Two subtrees, breadth
first. Ledger rows are in `ledger.md`. Epistemic states follow the brief: one T1 or two
independent T2 grounds is `known`; less carries `unvalidated`; a decided contested topic carries
`conflict`; no ranking or no admitted source is `undecided | missing`.

## Graph js-philosophy

Language-swap test applied: each statement holds with another language in place of JavaScript.

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| VERIFICATION | Verification | Defects that people forget to look for are found by machines, on every change, with a result that blocks the change and that people trust. | known | - |
| VERIFICATION.STATIC_BASELINE | Static analysis baseline | Every project analyzes its code without running it, and acts on what the analysis reports, so that known classes of mistake never reach review. | known | - |
| VERIFICATION.TEST_SUITE | Test suite | Behaviour is pinned by automated tests that exist for all new functionality, and whose adequacy is judged by what they detect, not by what they execute. | known | - |
| VERIFICATION.FAULT_DETECTION | Fault detection power | A suite is worth the faults it would catch, so that power is measured directly and probed with generated inputs, not assumed. | known | - |
| VERIFICATION.TEST_STABILITY | Test stability | A test result is a usable signal only while a failure means a defect, so nondeterminism is prevented at the cause rather than retried away. | known | - |
| VERIFICATION.ENFORCEMENT | Enforcement at the merge | A check changes behaviour only when failing it stops the merge, so the gate itself must not be skippable. | known \| unvalidated: practice inferred from a platform fact | VERIFICATION-019 |
| VERIFICATION.STATIC_BASELINE.1 | Analysis switched on | A linter or safe language mode is enabled and its warnings are addressed, because unread warnings protect nothing. | known | VERIFICATION-002 |
| VERIFICATION.STATIC_BASELINE.2 | Analysis beyond the compiler | Before a major release at least one static-analysis tool beyond compiler warnings has run, because compilers answer a narrower question than analyzers. | known | VERIFICATION-003 |
| VERIFICATION.STATIC_BASELINE.3 | Checks complement each other | Several kinds of check run together and none is the only mechanism, with negative tests for what must not happen, because each class finds defects the others miss. | known \| unvalidated: single T2 evidence, 2015 sites | VERIFICATION-001, VERIFICATION-004 |
| VERIFICATION.TEST_SUITE.1 | Tests for new functionality | A written policy requires automated tests for new major functionality, evidence shows it is followed, and the suite runs in the language's standard way, so that a change cannot ship unverified. | known | VERIFICATION-005 |
| VERIFICATION.TEST_SUITE.2 | Coverage finds, it does not judge | Coverage locates code no test executes; it is never a quality target, because executing code is not detecting its faults. | known \| conflict: OpenSSF passing criteria suggest covering most or all branches, as a suggestion rather than a numeric target \| unvalidated: study on Java, transfer inferred | VERIFICATION-006, VERIFICATION-007 |
| VERIFICATION.TEST_SUITE.3 | Test design | Tests exercise behaviour through the public interface, one test per behaviour, with real collaborators wherever they are fast and deterministic, so that tests fail for defects and not for refactoring. | known \| unvalidated: single T3 source, Google position | VERIFICATION-008, VERIFICATION-009, VERIFICATION-010 |
| VERIFICATION.FAULT_DETECTION.1 | Mutation testing | Detection power is measured by seeding small faults and counting how many tests kill, and the cost stays bounded by mutating only changed code at review. | known \| unvalidated: single T2 source, abstract-level | VERIFICATION-011, VERIFICATION-012 |
| VERIFICATION.FAULT_DETECTION.2 | Property-based testing | Behaviour is also probed with generated inputs against stated properties, with data distributions that follow real data. | known \| unvalidated: single T2 source | VERIFICATION-013, VERIFICATION-014, VERIFICATION-015 |
| VERIFICATION.TEST_STABILITY.1 | New tests are probed | A new test is run many times when added, because flakiness shows from the first run and arises mostly from waits, concurrency and order. | known \| unvalidated: single T2 source, transfer inferred | VERIFICATION-016 |
| VERIFICATION.TEST_STABILITY.2 | Shared state is cleaned | Tests do not leak state to each other, because order dependence is the second flake cause and cleaning the state is its usual fix. | known \| unvalidated: single T2 source, transfer inferred | VERIFICATION-017 |
| VERIFICATION.TEST_STABILITY.3 | Flake rate tracked | The flake rate is measured, and a suite approaching 1% flakiness is treated as losing its value and repaired before more is built on it. | known \| unvalidated: single T3 source, Google figures | VERIFICATION-018 |

Philosophy counts: L1 1, L2 5, L3 11; total 17.

### Intentlinks inside js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | VERIFICATION.STATIC_BASELINE | VERIFICATION.ENFORCEMENT | requires | An analysis finding is acted on only when the gate blocks the change that carries it. |
| 2 | VERIFICATION.TEST_SUITE | VERIFICATION.ENFORCEMENT | requires | A test policy has effect only when a failing suite stops the merge. |
| 3 | VERIFICATION.TEST_SUITE | VERIFICATION.TEST_STABILITY | requires | A suite is a trusted signal only while its failures mean defects. |
| 4 | VERIFICATION.FAULT_DETECTION.1 | VERIFICATION.TEST_SUITE.2 | dataflow | The mutation score supplies the adequacy evidence that coverage cannot give. |
| 5 | VERIFICATION.STATIC_BASELINE.3 | VERIFICATION.TEST_SUITE.1 | requires | Static analysis is never the only mechanism, so the test policy must exist beside it. |

### Inter links from js-philosophy to python-kb-philosophy

Principles shared with any language, linked, not copied. Targets exist in
`../python_guidelines/intent_graphs/python_kb_philosophy.yaml`.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | VERIFICATION.STATIC_BASELINE | python-kb-philosophy:DEFENSIVE | refines | Machine-run static analysis is how errors become visible early, for any language. |
| 2 | VERIFICATION.TEST_STABILITY | python-kb-philosophy:REPRODUCIBILITY | refines | A flaky test is a failure of same inputs same outputs, so its result carries no information. |

### Proposed links to other branches (the integrator resolves them)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | VERIFICATION.ENFORCEMENT | DEPENDENCIES | requires | The gate job includes the reproducible install step that DEPENDENCIES decides (QUALITY-C42 is routed there). |
| 2 | VERIFICATION.STATIC_BASELINE.1 | SUBSET | dataflow | The linter is the mechanism that enforces the safe subset SUBSET defines. |

## Graph pig-js-defaults

Statements that break the language-swap test: ESLint, typescript-eslint, Prettier, Biome, node:test,
Vitest, Jest, Playwright and Node assertion modes are JavaScript tooling. Tool choices (LINT.4, FORMAT.3,
TESTS.1) are decided by judgment on admitted tool facts against the purpose, automation, with
each rejected tool's winning condition in its judge record.

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.VERIFICATION | Verification defaults | A JavaScript or TypeScript change merges only after lint, format and tests have run unattended and passed. | known | - |
| PIG-JS.VERIFICATION.LINT | Linting | Lint rules run on every change with a configuration that makes findings binding and reviewable, so that the safe subset is enforced by machine. | known | - |
| PIG-JS.VERIFICATION.FORMAT | Formatting | Layout is produced and checked by machine so that review never spends attention on it. | known | - |
| PIG-JS.VERIFICATION.TESTS | Test code | Test code in JavaScript is written so that a pass cannot hide a wrong comparison or a race. | known | - |
| PIG-JS.VERIFICATION.LINT.1 | Rule set | The configuration states which rules run on which files, from a maintained baseline upward. | known | - |
| PIG-JS.VERIFICATION.LINT.2 | Enforcement | A finding changes the exit status of the run, so CI can block on it, cheaply enough to run every time. | known | - |
| PIG-JS.VERIFICATION.LINT.3 | Security findings triage | Findings of security lint rules are leads for a human, because the rules over-report. | known | VERIFICATION-029 |
| PIG-JS.VERIFICATION.LINT.4 | Linter selection | ESLint with typescript-eslint runs the rules, because it is the family with documented type-aware rules, a security plugin and the rule documents the other branches cite. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source | VERIFICATION-030 |
| PIG-JS.VERIFICATION.FORMAT.1 | Dedicated formatter | Layout belongs to a formatter that sees the whole file, not to lint rules. | known \| unvalidated: single T2 source | VERIFICATION-031, VERIFICATION-032 |
| PIG-JS.VERIFICATION.FORMAT.2 | Formatting checked in CI | Unformatted code fails the build, so formatting needs no reviewer. | known | VERIFICATION-033 |
| PIG-JS.VERIFICATION.FORMAT.3 | Formatter selection | Prettier prints the code, run apart from the linter, because it only prints and its check mode has documented exit codes. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source | VERIFICATION-034, VERIFICATION-035, VERIFICATION-036 |
| PIG-JS.VERIFICATION.TESTS.1 | Runner selection | node:test runs the suite, because it ships with Node, is stable and adds no dependency to the code that is trusted with the build. | known \| unvalidated: chosen by judgment on tool facts, no independent ranking source | VERIFICATION-037, VERIFICATION-038, VERIFICATION-039, VERIFICATION-040 |
| PIG-JS.VERIFICATION.TESTS.2 | Strict assertions | Assertions compare with strict semantics, so unequal values never pass. | known | VERIFICATION-041, VERIFICATION-042 |
| PIG-JS.VERIFICATION.TESTS.3 | Condition waits | Asynchronous tests wait for a condition, never for elapsed time. | known \| unvalidated: single T2 source, transfer inferred | VERIFICATION-043 |
| PIG-JS.VERIFICATION.LINT.1.1 | Config file and scoping | One flat configuration file at the project root, with rules scoped to files and ordered general to specific. | known | VERIFICATION-020 |
| PIG-JS.VERIFICATION.LINT.1.2 | Baseline rule set | Every project starts from the tool's maintained recommended set, for TypeScript too, so that the floor is not hand-built. | known \| unvalidated: baseline suitability inferred | VERIFICATION-021 |
| PIG-JS.VERIFICATION.LINT.1.3 | Strict rule set | Teams with enough TypeScript proficiency take the stricter set, accepting that it changes between minor versions. | known | VERIFICATION-022 |
| PIG-JS.VERIFICATION.LINT.1.4 | Type-aware rules | Rules that need type information run, because the defects they find (a floating promise) are invisible to syntax-only rules. | known \| gap: no admitted figure for the cost, see G-L20 | VERIFICATION-023, VERIFICATION-024 |
| PIG-JS.VERIFICATION.LINT.2.1 | Warnings fail the run | Warnings count as failures in CI, so nothing is tolerated by default silence. | known | VERIFICATION-025 |
| PIG-JS.VERIFICATION.LINT.2.2 | Tool failure is not a finding | A broken configuration is told apart from lint findings in CI, so a broken gate is not read as a pass or as code defects. | known | VERIFICATION-026 |
| PIG-JS.VERIFICATION.LINT.2.3 | Stale suppressions reported | A suppression that no longer suppresses anything is flagged, so old exceptions cannot hide new errors. | known | VERIFICATION-027 |
| PIG-JS.VERIFICATION.LINT.2.4 | Repeat runs are cheap | Unchanged files are not re-linted, so the gate stays fast enough to run on every change. | known | VERIFICATION-028 |

Defaults counts: L1 1, L2 3, L3 10, L4 8; total 22.

### Intentlinks inside pig-js-defaults

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.VERIFICATION.LINT.2 | PIG-JS.VERIFICATION.LINT.1 | requires | Enforcement acts on the rules the configuration selects. |
| 2 | PIG-JS.VERIFICATION.LINT.2.3 | PIG-JS.VERIFICATION.LINT.2.1 | requires | A stale suppression is reported as a warning by default, so it binds only while warnings fail the run. |
| 3 | PIG-JS.VERIFICATION.LINT.1.2 | PIG-JS.VERIFICATION.FORMAT.1 | requires | The baseline can leave out layout rules only because a dedicated formatter owns layout. |
| 4 | PIG-JS.VERIFICATION.FORMAT.2 | PIG-JS.VERIFICATION.FORMAT.1 | requires | A check mode needs a formatter whose output is the reference layout. |
| 5 | PIG-JS.VERIFICATION.LINT.1.3 | PIG-JS.VERIFICATION.LINT.1.2 | refines | The strict set extends the recommended set for proficient teams. |
| 6 | PIG-JS.VERIFICATION.TESTS.2 | PIG-JS.VERIFICATION.TESTS.1 | requires | Assertion mode is chosen inside the runner that executes the tests. |

### Inter links from pig-js-defaults to js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.VERIFICATION.LINT.2 | js-philosophy:VERIFICATION.ENFORCEMENT | refines | CI exit status is how a lint finding blocks the merge in JavaScript. |
| 2 | PIG-JS.VERIFICATION.LINT.1.2 | js-philosophy:VERIFICATION.STATIC_BASELINE.1 | refines | The recommended rule set is the switched-on analysis for JavaScript. |
| 3 | PIG-JS.VERIFICATION.TESTS.3 | js-philosophy:VERIFICATION.TEST_STABILITY.1 | refines | Condition waits remove the largest flake category in asynchronous JavaScript tests (inferred transfer). |
| 4 | PIG-JS.VERIFICATION.LINT.3 | js-philosophy:VERIFICATION.STATIC_BASELINE.3 | refines | Security lint output is one analysis class among several, never the sole mechanism. |

### Proposed links to other branches (the integrator resolves them)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.VERIFICATION.LINT.1.1 | SUBSET | dataflow | The configuration is where SUBSET's lint-enforceable rules (equality, var, const) are written. |
| 2 | PIG-JS.VERIFICATION.LINT.1.4 | CONTRACTS | requires | Type-aware rules need the type layer CONTRACTS decides, and TYPES-C44 binds tool support to the TypeScript 7.1 API. |
| 3 | PIG-JS.VERIFICATION.LINT.1.4 | CONTROL | dataflow | The type-aware rule no-floating-promises enforces CONTROL's rule that promises are handled. |
| 4 | PIG-JS.VERIFICATION.LINT.3 | DEFENSE | dataflow | Security lint findings are leads that feed DEFENSE's injection and eval rules. |
| 5 | PIG-JS.VERIFICATION.TESTS.2 | SUBSET | refines | Strict assertions apply SUBSET's strict-equality rule to test code. |
| 6 | PIG-JS.VERIFICATION.LINT.2 | DEPENDENCIES | requires | The CI job that runs the gate installs dependencies by DEPENDENCIES' reproducible-install rule. |

## Judge records (pig-js-defaults nodes holding a decision)

Format: Positions (claim ids, source ids) / Forces / Decision / Rejected with the condition under
which it would win. Where the admitted evidence holds a single position, the record says so
instead of inventing an alternative.

### PIG-JS.VERIFICATION.LINT.1.1
- Positions: flat config at the root, `files` and `ignores`, later objects win (QUALITY-C01, C02; SRC-166). No competing position in admitted sources; the legacy eslintrc format is named only as not relied on (QUALITY-C28 note).
- Forces: predictability of what runs on which file (merge order is deterministic) against nothing; cost is one migration for old projects.
- Decision: one `eslint.config.js` (or .mjs or .cjs) at the root exporting an array, general objects first.
- Rejected: the legacy eslintrc format, because the admitted page documents only the flat format as current; it would win for a code base pinned to an ESLint version that predates flat config (condition inferred, no source).

### PIG-JS.VERIFICATION.LINT.1.2
- Positions: recommended config as baseline (QUALITY-C03; SRC-167); typescript-eslint recommended as the drop-in TypeScript baseline, stylistic as separate opt-in (QUALITY-C04; SRC-054).
- Forces: correctness floor without hand-curation against over-reporting; the recommended set is maintained by the tool's authors.
- Decision: start from recommended, add typescript-eslint recommended for TypeScript; keep stylistic rules out of the correctness gate.
- Rejected: a hand-built rule list as the floor, because the rules index marks the maintained set; it wins only where a project needs a rule the set lacks, added on top. Suitability of the baseline is inferred (the sources define the marker, not its sufficiency).

### PIG-JS.VERIFICATION.LINT.1.3
- Positions: strict only if a nontrivial share of developers is highly proficient, set may change outside major versions (QUALITY-C09; SRC-054).
- Forces: stronger checking against onboarding cost and churn in findings.
- Decision: the max practice is the strict set; it is taken when the proficiency condition, which the project itself states, holds.
- Rejected: strict for every team, because the project's own advice denies it; it would win once the team meets the condition. Recommended-only stays the floor (LINT.1.2).

### PIG-JS.VERIFICATION.LINT.1.4
- Positions: typed linting through `parserOptions.projectService` for rules such as no-floating-promises (QUALITY-C10; SRC-181); cost is a whole-project TypeScript analysis before linting. TypeScript 7.0 has no API until 7.1 (TYPES-C44; SRC-034).
- Forces: defects invisible to syntax rules against lint time.
- Decision: enable typed linting in TypeScript projects and budget its time. No admitted figure for the cost (G-L20).
- Rejected: syntax-only linting, because no-floating-promises and similar rules need types; it wins where the project has no TypeScript project to analyze or where lint time is shown to block the workflow (inferred).

### PIG-JS.VERIFICATION.LINT.2.1
- Positions: `--max-warnings 0` so warnings change the exit status; default -1 means no limit (QUALITY-C05; SRC-165).
- Forces: no tolerated drift against the cost of cleaning up existing warnings first.
- Decision: CI runs with `--max-warnings 0`.
- Rejected: the default (warnings never fail), because the documented exit rule leaves them invisible to CI; it wins during a staged migration with a recorded end date (inferred).

### PIG-JS.VERIFICATION.LINT.2.2
- Positions: exit 0 clean, 1 findings, 2 configuration or internal error (QUALITY-C06; SRC-165).
- Forces: a broken gate must not read as a pass or as code defects.
- Decision: CI scripts distinguish exit 2 from exit 1 and treat 2 as a broken tool.
- Rejected: any non-zero is one failure, because it hides a broken configuration behind a code-defect message; wins only for a throwaway script (inferred).

### PIG-JS.VERIFICATION.LINT.2.3
- Positions: report unused disable directives, flag or severity variant, default warn (QUALITY-C07; SRC-165).
- Forces: stale exceptions hiding future errors against noise on first enabling.
- Decision: report unused directives; with LINT.2.1 the default warn binds.
- Rejected: leave them unreported, because obsolete suppressions then hide errors; it wins never as a default.

### PIG-JS.VERIFICATION.LINT.2.4
- Positions: `--cache`, strategy `metadata` (default) or `content` (QUALITY-C08; SRC-165).
- Forces: gate speed against stale-cache risk on checkouts that reset modification times.
- Decision: use `--cache` and, where modification times change without content changes (fresh CI checkouts, inferred), `--cache-strategy content`.
- Rejected: no cache, because repeated runs relint unchanged files; wins when the cache directory cannot persist between runs (inferred).

### PIG-JS.VERIFICATION.LINT.3
- Positions: eslint-plugin-security maintainers state it finds many false positives that need human triage (QUALITY-C45; SRC-164).
- Forces: catching injection leads against alert fatigue.
- Decision: findings are hotspots for human triage and are not verdicts. Whether to run the plugin at all has no admitted ground (boundary DEFENSE).
- Rejected: failing the build automatically on every plugin finding, because the maintainers say the findings over-report; it wins for a rule whose precision a team has measured (inferred).

### PIG-JS.VERIFICATION.FORMAT.1
- Positions: dedicated formatter (QUALITY-C12; SRC-298, T2, the ESLint steering committee); formatting by ESLint core rules is deprecated (QUALITY-C11; SRC-298, SRC-167). Biome and Prettier documents agree layout is a separate concern (12_dissent, topic 14).
- Forces: consistency and review time against one more tool.
- Decision: a dedicated formatter owns layout; lint rules do not.
- Rejected: layout through ESLint core rules, deprecated because the team could not sustain them; the `@stylistic` plugin keeps formatting in ESLint and is a listed alternative under FORMAT.3.

### PIG-JS.VERIFICATION.FORMAT.2
- Positions: check mode in CI, `prettier --check` exits 0, 1, 2; a pre-commit hook reduces failures (QUALITY-C16; SRC-176).
- Forces: formatting enforced without a reviewer against occasional CI failures.
- Decision: CI runs the formatter in check mode; the pre-commit hook is the documented option, not a requirement (the source says "you may be interested").
- Rejected: CI that rewrites files (write mode), because a gate that mutates its input checks nothing; wins for a bot that commits formatting by design (inferred).

### PIG-JS.VERIFICATION.TESTS.2
- Positions: `node:assert/strict`; legacy `equal` and `deepEqual` compare with `==` (QUALITY-C25; SRC-171).
- Forces: no false pass against a one-line import change.
- Decision: import `node:assert/strict` in tests.
- Rejected: legacy mode, which can pass unequal values; folklore "assert.deepEqual is a safe equality check" refuted (12_dissent). It wins only where a test intends loose equality, to be stated.

### PIG-JS.VERIFICATION.TESTS.3
- Positions: wait on a condition (54% of Async Wait flakes fixed with waitFor; QUALITY-C34; SRC-296) and Playwright's web-first assertions retry until true (SRC-175, tool fact).
- Forces: stable result against a possibly longer failing wait.
- Decision: condition waits, never fixed delays.
- Rejected: fixed sleeps, the largest flake category in the study (45% Async Wait, QUALITY-C33); wins never as a default. The study is Java-dominated; transfer is inferred.

### PIG-JS.VERIFICATION.LINT.4
- Positions: ESLint with typescript-eslint, which has documented type-aware rules (no-floating-promises, SRC-181), a security plugin (SRC-164), flat config, recommended baselines and the rule documents other branches cite (SRC-166, SRC-167, SRC-054); Biome as one tool for lint and format whose type-aware rules run only when its scanner is enabled and whose unsafe fixes need manual review (SRC-162, QUALITY-C17). No source compares them.
- Forces: automation needs binding, scriptable findings (exit codes, max-warnings, unused-suppression reports, all documented for ESLint) and type-aware checks; Biome offers fewer moving parts. DEPENDENCIES' trust purpose: one tool is fewer packages, but ESLint's plugins are opt-in and pinned.
- Decision: ESLint with typescript-eslint. Basis is judgment on tool facts against the branch purpose; the documents ground the facts, not a preference (gate G5). Rows 020 to 029 are the grounds.
- Rejected: Biome. Wins when the project wants one tool and one dependency for lint and format and the rule set it ships covers the needed rules (type-aware rules, security leads, hand-reviewed unsafe fixes) without ESLint plugins (inferred).

### PIG-JS.VERIFICATION.FORMAT.3
- Positions: Prettier (SRC-177, SRC-178, SRC-176, named first by SRC-298); dprint and @stylistic (named by SRC-298 only, no tool facts admitted); Biome formatter (SRC-162).
- Forces: a formatter that only prints cannot change meaning (SRC-178); its check mode has documented exit codes 0, 1, 2 (SRC-176); the integration with ESLint is documented (eslint-config-prettier, run apart). Biome would fold formatting into LINT.4's rejected tool.
- Decision: Prettier, run separately from ESLint, with eslint-config-prettier, checked in CI (FORMAT.2). Basis is judgment on facts, not a claim that Prettier's style is better.
- Rejected: Biome formatter, wins when Biome is the linter. @stylistic, wins when a team insists on a single lint pipeline and accepts the maintenance cost the ESLint team described (SRC-298). dprint, wins when an admitted source gives its behaviour and check mode; none does today.

### PIG-JS.VERIFICATION.TESTS.1
- Positions: node:test, built in, stable from Node v20.0.0, exit code 1 on failure, coverage experimental (QUALITY-C24, SRC-172); Vitest, needs Vite 6.4+ and Node 22.12+, watch mode by default, V8 and Istanbul coverage (QUALITY-C26, C27, SRC-183, SRC-182); Jest, needs Babel or ts-jest to run TypeScript (QUALITY-C28, SRC-170).
- Forces: no extra dependency in the trust chain (DEPENDENCIES), CI-friendly exit status and no watch default, against stable coverage tooling and richer features elsewhere.
- Decision: node:test. Do not gate on its experimental coverage flag (consistent with D1: coverage is not a gate anyway).
- Rejected: Vitest, wins when the project already builds with Vite or needs stable coverage providers or its watch workflow. Jest, wins when a large existing Jest suite and its transforms are in place (migration cost, inferred).
