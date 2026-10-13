# Decisions for review: branch VERIFICATION

Purpose of the branch: automation. Max rule: the most demanding practice that serves automation
and that an admitted source supports. Each entry gives the decision, rejected positions with the
condition under which each would win, and the grounds. Conditions marked (inferred) come from
reasoning, not from a source. Node uids refer to `skeleton.md`, rows to `ledger.md`.

## Decisions

### D1. Coverage is reported, never a target (VERIFICATION.TEST_SUITE.2; rows 006, 007)
- Decision: use coverage to find code no test executes; set no coverage percentage as a quality target or CI gate. Known | conflict.
- Rejected: (a) gate on a high percentage (the folklore "high coverage means effective tests"; also the maximal reading of OpenSSF's suggestion to cover most or all branches). Wins if a study on JavaScript suites, controlling for suite size, found coverage tracking fault detection; none is admitted. (b) OpenSSF passing criteria, SRC-174, T1: it SUGGESTS covering most or all branches and inputs; compatible with this decision if coverage is read as a finding tool, not a gate.
- Grounds: the Inozemtseva and Holmes study (SRC-297, T2, named in the claim table): correlation with effectiveness is low to moderate once suite size is controlled (31,000 suites, five Java systems). The decision is language-neutral, so it sits in `js-philosophy`; transfer to JavaScript is inferred. Matches 12_dissent topic 15 and question Q10.
- Max reading: the demanding practice here is not "more coverage" but measuring detection power directly (D6).

### D2. A dedicated formatter owns layout, checked in CI (FORMAT.1, FORMAT.2; rows 031, 032, 033)
- Decision: layout is produced by a dedicated formatter, not by lint rules, and CI runs it in check mode so unformatted code fails the build. Known | unvalidated: single T2 source (FORMAT.1); known (FORMAT.2, T1 facts about the Prettier CLI).
- Rejected: layout through ESLint core formatting rules, deprecated by the ESLint team (SRC-298, SRC-167); wins never for new code. The `@stylistic` plugin, which keeps formatting in ESLint, remains an acceptable option under FORMAT.3 (D15). CI that writes files, wins only for a bot that commits formatting by design (inferred).
- Grounds: ESLint technical steering committee (SRC-298, T2) names the position; Prettier and Biome documents agree layout is separate (12_dissent topic 14, "checked and not a tension").
- Partial demotion: the pre-commit hook in QUALITY-C16 is Prettier's optional suggestion ("you may be interested"), kept as an option in the statement, not a requirement.

### D3. Warnings fail CI (LINT.2.1; row 025)
- Decision: `--max-warnings 0`. Known (T1, documented exit-status rule).
- Rejected: ESLint's default of no limit, under which warnings never change the exit status. Wins during a staged migration that has a recorded end date (inferred).
- Weighty because it is the most demanding setting for a gate; the claim's certainty is inferred from the documented exit rule and the default of -1.

### D4. Typed linting is on in TypeScript projects (LINT.1.4; rows 023, 024)
- Decision: enable typed linting (`parserOptions.projectService`) and budget its cost. Known | gap: no cost figure (G-L20 of 11_coverage).
- Rejected: syntax-only linting; wins where there is no TypeScript project to analyze, or where measured lint time blocks work (inferred). Tool-dependency risk: TypeScript 7.0 ships no API, a different one is expected in 7.1 (SRC-034); the consequence for tools is inferred.
- Grounds: typescript-eslint docs (SRC-181, T1).

### D5. Strict type-aware config only for proficient teams (LINT.1.3; row 022)
- Decision: strict set when a nontrivial share of the team is highly proficient in TypeScript; otherwise the recommended set (LINT.1.2). Known (T1, the project's own position, unrestricted for this slot).
- Rejected: strict for all (the project itself denies it); wins once the team meets the condition. Churn: the set may change outside major versions.

### D6. Mutation testing, incrementally, on changed code (VERIFICATION.FAULT_DETECTION.1; rows 011, 012)
- Decision: where mutation testing is adopted, run it on changed code during review and filter mutants. Known | unvalidated: single T2 source, abstract-level.
- Rejected: mutating the whole code base on every run (the source runs mutation incrementally on changed code instead); wins on a small code base where a full run is cheap (inferred). Whether to REQUIRE mutation testing has no admitted source and is not decided (open, see O1 in `result.md`).
- Grounds: the Google mutation-testing paper (SRC-299, T2 restricted: abstract-level facts only until the full text is read). Definitions: SRC-179 (StrykerJS facts) and the same abstract.

### D7. Flakiness is prevented at its causes (TEST_STABILITY.1 and .2, TESTS.3; rows 016, 017, 043)
- Decision: probe new tests extensively when added, clean shared state between tests, wait on conditions not delays. Known | unvalidated: single T2 source, transfer inferred.
- Rejected: fixed delays in asynchronous tests, the largest flake category in the study (45% Async Wait); they win never as a default. No admitted source discusses retry-on-failure; not claimed.
- Grounds: the empirical flaky-test study (SRC-296, T2, 201 commits, 51 mostly Java projects). The Playwright half of row 043 is a tool fact (SRC-175, restricted).

### D8. Static analysis is a baseline and not the only mechanism (STATIC_BASELINE.1 to .3; rows 001 to 004)
- Decision: a linter or safe mode is on and its warnings addressed; one analyzer beyond compiler warnings runs before major releases; several checks run together with negative tests. .1 and .2 known (SRC-174, T1 MUST). .3 known | unvalidated: single T2 evidence plus one working-group position.
- Rejected: lint alone as the verification mechanism; DLint found 49 problems per site that static analysis missed on average (2015, SRC-237, evidence of occurrence only, no current-language claim). Wins never.
- Restriction handling: SRC-163 is admitted for the OpenSSF Best Practices Working Group's positions; row 004 is kept as that position with the holder named, which the restriction allows.

### D9. The gate job must always run (ENFORCEMENT; row 019)
- Decision: a required check that can be skipped is a hole; make the gate job run on every change. Known | unvalidated: practice inferred from a platform fact.
- Rejected: relying on conditional jobs as required checks (GitHub counts skipped and neutral as passing, SRC-169); wins nowhere on GitHub. Other hosts: no admitted source (open).
- Sits in `js-philosophy` by the language-swap test even though the grounds are GitHub's.

### D10. Property-based testing uses real-data distributions (FAULT_DETECTION.2; rows 013, 014, 015)
- Decision: custom generators whose distribution follows actual data. Known | unvalidated: single T2 source.
- Demoted: row 015 (properties beside the code as documentation) is the QuickCheck authors' practice, outside the method for which SRC-300 is admitted; kept as acceptable-when. Row 013: shrinking rests on fast-check's docs only (SRC-168), not on the paper. No admitted source says property-based tests beat example tests (SRC-168 restriction); not claimed.

### D11. ESLint practices are stated, the linter family is not (LINT.1.1, 1.2, 2.x; rows 020 to 028)
- Decision: the practices (flat config, recommended baseline, warnings fail, exit codes, stale suppressions, cache) are decided as ESLint practices because the admitted tool documents ground them. Each rests on one T1 ground, so each is known.
- Rejected: none at this node. The linter-family choice is D14, a judgment on tool facts, not a claim by any tool document that ESLint is better.

## Single T1 ground, known, no weighty alternative

Rows 002, 003, 005, 020, 021, 026, 027, 028, 029, 041 each rest on one T1 document and carry no
contested position. Listed so the reviewer can overrule any without searching: SRC-174 (C20, C21,
C22), SRC-166 and SRC-167 and SRC-054 (C01 to C04), SRC-165 (C06, C07, C08), SRC-164 (C45),
SRC-171 (C25).

## Decisions added after the maintainer's standing decision

The coordinator applied "max(all sources), pick the best" to the five nodes first left undecided.
Tool documents ground facts about each tool; the choice among tools is judgment against the
branch purpose, automation, recorded with each rejected tool's winning condition (judge records
in `skeleton.md`).

### D12. Test design (js-philosophy VERIFICATION.TEST_SUITE.3; rows 008, 009, 010)
- Decision: test behaviours through the public interface, one test per behaviour, DAMP over DRY; prefer real collaborators when they are fast and deterministic. Known | unvalidated: single T3 source, Google position.
- Searched: the branch claims, 12_dissent (topics, tensions, folklore) and 11_coverage (gaps G-L, overlaps) for any other position on test scope, mocking or test mix; only SRC-320 and SRC-321 (Google, T3, restricted to Google's position) exist.
- Restriction override, flagged: the register says "Google's positions, never as evidence". I recorded the position as the decision because it is the only admitted position and the maintainer rule forbids abstaining; the epistemic state says so. Reviewer may revert rows 008 and 009 to acceptable-when.
- Rejected: per-method tests and mock-everything (the positions Google's text contrasts with); win when real collaborators are slow or nondeterministic (the source's own condition). The 80/15/5 mix (row 010) stays acceptable-when for organizations with Google-like test infrastructure: a size ratio is Google's own, not a rule.

### D13. Flake rate (js-philosophy VERIFICATION.TEST_STABILITY.3; row 018)
- Decision: track the flake rate and act as it approaches 1%. Known | unvalidated: single T3 source, Google figures (0.15% reported, value lost near 1%).
- Searched: same corpus as D12; no other threshold exists.
- Restriction override, flagged as in D12: figures are Google's; the threshold is theirs, adopted as the only admitted one. Reviewer may revert row 018 to acceptable-when.
- Rejected: no tracking, rejected by the T2 flaky-test study's finding that tests are flaky from the first run (D7); a different threshold wins when the organization measures its own.

### D14. Linter family: ESLint with typescript-eslint (PIG-JS.VERIFICATION.LINT.4)
- Decision: ESLint with typescript-eslint. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: documented type-aware rules and no-floating-promises (SRC-181), documented exit codes and warning gates (SRC-165), security plugin (SRC-164), flat config and baselines (SRC-166, SRC-167, SRC-054), and every other branch cites ESLint rule documents.
- Rejected: Biome; wins when one tool and one dependency for lint and format is wanted and its shipped rules cover the project's needs (inferred). Its unsafe fixes need manual review (row 030).

### D15. Formatter: Prettier (PIG-JS.VERIFICATION.FORMAT.3)
- Decision: Prettier, run apart from ESLint, eslint-config-prettier to disable conflicts, check mode in CI. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: prints only and never transforms code (SRC-178), check-mode exit codes 0, 1, 2 (SRC-176), documented ESLint integration (SRC-177); named first by the ESLint steering committee (SRC-298), not as a ranking.
- Rejected: Biome formatter (wins when Biome is the linter); @stylistic (wins if a team wants one lint pipeline and accepts the sustaining cost ESLint's team named); dprint (no admitted behaviour facts; wins when a source gives them).
- Restriction check: SRC-178 and SRC-177 never ground "Prettier is better"; the choice rests on automation fit (documented check mode and integration), stated as judgment.

### D16. Runner: node:test (PIG-JS.VERIFICATION.TESTS.1)
- Decision: node:test; no gate on its experimental coverage flag. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: built into Node, stable from v20.0.0, exit code 1 on failure (SRC-172); no added dependency, which serves DEPENDENCIES' trust purpose. Vitest requires Vite and a recent Node and defaults to watch mode (SRC-183); Jest needs Babel or ts-jest for TypeScript (SRC-170).
- Rejected: Vitest (wins with an existing Vite build, or when stable coverage providers matter, SRC-182); Jest (wins for a large existing suite and its transforms).

## Undecided nodes

None. The five nodes first left undecided (LINT.4, FORMAT.3, TESTS.1, TEST_SUITE.3, TEST_STABILITY.3) are decided in D12 to D16, each marked `unvalidated` where it rests on judgment or a single T3 source. Open: whether to require mutation testing (O1 in `result.md`), which no admitted source addresses and no node claims.
