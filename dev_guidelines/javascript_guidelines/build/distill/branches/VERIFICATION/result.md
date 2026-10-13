# Result: step 5b, branch VERIFICATION

## L1 headline

VERIFICATION is consolidated into 17 philosophy nodes and 22 defaults nodes with every one of its 43 claims placed once and none dropped; most decisions rest on one T1 ground, no node is undecided (the five first left open are decided by judgment or on a single T3 source, marked unvalidated), and four rows stay acceptable-when after restriction checks; certainty: grounded for placement (checker run, 0 errors), inferred for the node cut and the language-swap routing.

Pinned:
- Claims in: 43 (`claims.md`). Ledger rows out: 43 (19 js-philosophy, 24 pig-js-defaults), carrying 43 claim ids, 0 dropped, 0 duplicated; 2 of the rows are folklore `rejected` rows with `-` as claim id, and 2 rows merge two claims each.
- Roles: decision 28, fact 8, acceptable-when 4, rejected 3, deferred 0.
- Nodes, js-philosophy: L1 1, L2 5, L3 11, total 17. pig-js-defaults: L1 1, L2 3, L3 10, L4 8, total 22. Judge records: 16.
- Decisions for review: 16 (D1 to D16 in `decisions.md`); contested: coverage as a target (D1), the dedicated formatter (D2); tool choices by judgment: ESLint, Prettier, node:test (D14 to D16).
- Undecided nodes: 0. Decided after the maintainer's standing decision: LINT.4 ESLint, FORMAT.3 Prettier, TESTS.1 node:test (judgment on tool facts); TEST_SUITE.3 and TEST_STABILITY.3 on Google's T3 positions (single source, restriction override flagged).
- Restriction demotions: 4 rows stay acceptable-when (010, 015, 030, 034) and 1 partial (033, pre-commit hook an option). Restriction overrides, flagged: rows 008, 009, 018 (Google positions, T3, decided for lack of another position).
- Checker: `python3 build/distill/check_ledger.py VERIFICATION`: claims in 43, placed 43, missing 0, duplicated 0, unknown 0, skeleton nodes 39.

## L2 claims

- Grounded: all 43 claims are placed exactly once; the checker reports 0 errors in branch mode.
- Grounded: routing to the two graphs follows the language-swap test: 19 rows are language-neutral (static analysis, test suite, mutation and property testing, flakiness, gate), 24 name JavaScript tooling (ESLint, typescript-eslint, Prettier, Biome, node:test, Vitest, Jest, Node assertion modes).
- Inferred: the subtree cut. Philosophy splits into static baseline, test suite, fault detection, test stability, enforcement; defaults splits into lint, format, test code. The ground is the claim clusters and the branch purpose (automation), not a source taxonomy.
- Grounded: coverage is decided as a report, not a target (D1), `known | conflict` against OpenSSF's suggestion and the folklore belief; transfer from Java to JavaScript is inferred.
- Grounded: a dedicated formatter owns layout and CI checks it (D2); the single T2 ground makes FORMAT.1 `unvalidated`.
- Grounded: the most demanding supported lint settings are chosen: `--max-warnings 0`, typed linting, unused-suppression reporting, strict set for proficient teams (D3 to D5); each rests on one T1 document, so each is known.
- Inferred: no admitted source ranks linters, formatters or test runners (tool documents are G5-restricted); the three choices are made by judgment on tool facts against automation: ESLint with typescript-eslint, Prettier, node:test (D14 to D16), each rejected tool with its winning condition in the judge record. Marked `unvalidated`.
- Grounded: Google's testing positions (rows 008, 009, 018) are the only admitted position on test design and flake threshold; they are T3 and restricted to Google's position, so they are decided as `unvalidated: single T3 source` and the restriction override is flagged (D12, D13). Row 010 (80/15/5 mix) stays acceptable-when.
- Inferred: the flakiness decisions (rows 016, 017, 043) rest on one T2 study of mostly Java projects; transfer is inferred.
- Grounded: folklore rows written for the two beliefs 12_dissent attaches to this branch: `assert.deepEqual is a safe equality check` (refuted, row 042) and `high coverage means effective tests` (restricted, row 007).
- Open: whether to require mutation testing or a mutation-score gate has no admitted source (O1).
- Open: the gate-always-runs rule is grounded on GitHub only; no admitted source covers other CI hosts (O2).
- Open: no admitted figure for the cost of typed linting (G-L20 of 11_coverage, carried on LINT.1.4).
- Grounded: 8 proposed cross-branch links (SUBSET 3, CONTRACTS 1, CONTROL 1, DEFENSE 1, DEPENDENCIES 2), 2 inter links to `python-kb-philosophy` (DEFENSIVE, REPRODUCIBILITY), 4 inter links from defaults to philosophy.

## L3 full

### 1. What was read

Per the brief: `build/plan.md` (Goal, Boundary, Source admission policy, Claim format, Target
IntentGraphs, Maintainer decisions), `build/distill/target_hierarchy.md` (all), IntentGraph
primers `PRIMER_00_PHILOSOPHY` and `PRIMER_01_SEMANTICS` (`PRIMER_03A_EDITING` was not opened: UID
format and name safety come from the brief's Shared section, link types from `PRIMER_01`), `branches/VERIFICATION/claims.md` (all 43
rows), the 12_dissent parts on topics 14 and 15, X-tensions, the folklore table and the maintainer
questions Q9 and Q10, the 11_coverage lines on gaps G-L20, boundary lists and overlaps O09 and O10,
the 43 register rows cited by the claims, and the `python_kb_philosophy` uids and intents. Not read:
the full texts of the sources; claim rows carry the source quotes and I relied on them
(tool-extracted quotes in the claim tables, not re-verified).

### 2. Ledger placement (grounded)

| graph | rows | decision | fact | acceptable-when | rejected |
|---|---|---|---|---|---|
| js-philosophy | 19 | 13 | 3 | 2 | 1 |
| pig-js-defaults | 24 | 15 | 5 | 2 | 2 |
| total | 43 | 28 | 8 | 4 | 3 |

Merges: row 020 (QUALITY-C01 and C02, one document SRC-166, one node), row 021 (QUALITY-C03 and
C04, one node). Claims placed: 43; rows with a claim id: 41; folklore rows with `-`: 2. This `-`
convention is mine (see O3): the brief requires a `rejected` row for each refuted belief and the
same claim cannot be placed twice.

### 3. Node counts

| graph | L1 | L2 | L3 | L4 | total |
|---|---|---|---|---|---|
| js-philosophy | 1 | 5 | 11 | 0 | 17 |
| pig-js-defaults | 1 | 3 | 10 | 8 | 22 |

Children per node stay within two to six: philosophy STATIC_BASELINE 3, TEST_SUITE 3,
FAULT_DETECTION 2, TEST_STABILITY 3, ENFORCEMENT leaf (single decision, one cluster); defaults
LINT 4 (LINT.1 4, LINT.2 4), FORMAT 3, TESTS 3. The L1 VERIFICATION node has 5 children
(philosophy) and 3 (defaults).

### 4. Decisions for review (grounded; conditions marked inferred where they are)

Full text in `decisions.md`.
- D1 coverage not a target (contested, conflict marked); D2 dedicated formatter and check mode; D3 `--max-warnings 0`; D4 typed linting; D5 strict set conditional on proficiency; D6 incremental mutation testing; D7 flakiness prevented at the causes; D8 static analysis baseline, never the only mechanism; D9 gate job always runs; D10 property tests with real-data generators; D11 ESLint practices; added after the maintainer's standing decision: D12 test design, D13 flake rate (Google T3 positions), D14 ESLint, D15 Prettier, D16 node:test.

### 5. Undecided nodes

None. LINT.4, FORMAT.3 and TESTS.1 are decided by judgment on admitted tool facts against automation (and DEPENDENCIES' trust purpose for node:test); TEST_SUITE.3 and TEST_STABILITY.3 are decided on Google's positions, the only admitted ones (searched: branch claims, 12_dissent, 11_coverage). Rejected tools carry their winning condition in the judge records. LINT.4 remains a node I added to the tree (O4).

### 6. Restriction demotions (grounded against `build/audit/source_register.md`)

| rows | claims | source and restriction | treatment |
|---|---|---|---|
| 008, 009, 018 | QUALITY-C29, C30, C32 | SRC-320, SRC-321 (T3): Google's positions and figures, never as evidence | first pass acceptable-when; now decision `unvalidated: single T3 source` by the maintainer's standing decision (override flagged, D12, D13) |
| 010 | QUALITY-C31 | SRC-320: Google's own mix | acceptable-when |
| 015 | QUALITY-C41 | SRC-300: method only, the paper's own practice is outside it | acceptable-when |
| 034 | QUALITY-C13 | SRC-298, SRC-162: no ranking | alternatives to Prettier acceptable-when |
| 030 | QUALITY-C17 | SRC-162: facts about Biome only | acceptable-when Biome is the linter |
| 036 | QUALITY-C15 | SRC-177: Prettier's own position | decision, applied because Prettier is chosen (D15) |
| 033 | QUALITY-C16 | SRC-176: CLI facts | decision kept; the pre-commit hook is an option only (partial) |

Checked and not demoted: SRC-054 is unrestricted for 08_quality (C04, C09); SRC-163 is a T1
working-group position, kept as that position with the holder named (row 004); SRC-299 and SRC-297
used inside their stated scope (abstract-level facts; Java study, transfer marked inferred);
SRC-175, SRC-172, SRC-183, SRC-182, SRC-170, SRC-168, SRC-179 used for tool facts only; SRC-034
used for the no-API fact only.

### 7. Folklore (grounded)

Row 042: refuted, assert.deepEqual is a safe equality check (SRC-171). Row 007: restricted, high
coverage means effective tests (SRC-174 suggestion only, SRC-297 Java study). No other
12_dissent belief concerns this branch's nodes.

### 8. Open items

- O1: no admitted source on requiring mutation testing or a mutation-score threshold; not decided.
- O2: gate-always-runs grounded on GitHub; other CI hosts unsourced.
- O3: convention for folklore rows (`-` as claim id, source claim placed in its own row); the integrator may prefer another form.
- O4: LINT.4 (linter family) is my addition to the tree (now decided, D14); the integrator should confirm or fold it into the framework or tooling discussion.
- O5: the epistemic cells in `skeleton.md` write multi-issue states with an escaped pipe (`\|`) inside Markdown tables; the ledger has no pipes inside cells.
- O6: TypeScript type checking in CI (`tsc --noEmit`, TYPES-C03) is routed to CONTRACTS, so VERIFICATION has no node for it; the integrator should link the two.
- O7: QUALITY-C42 (`npm ci` in CI) and C46 (cooldown) are routed to DEPENDENCIES; linked as proposals only.
- Not read in full: source documents themselves; tool-extracted quotes in the claim tables were relied on.

### 9. Files

`ledger.md`, `skeleton.md`, `decisions.md`, `result.md` in `build/distill/branches/VERIFICATION/`.
Nothing outside that folder was written. No commit, no push.
