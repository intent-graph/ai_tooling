# Step 5b: branch STRUCTURE

## L1 headline

All 57 STRUCTURE claims are placed once in 48 ledger rows and consolidated into 51 nodes (17 in js-philosophy, 34 in pig-js-defaults), with 25 judge records and one undecided topic (declared layering, two nodes); certainty: grounded for counts and the branch checker's output, inferred for the max-rule choices on thin evidence (listed for review).

Pinned:
- Claims in: 57; ledger rows out: 48 (12 js-philosophy, 36 pig-js-defaults); placed 57, missing 0, duplicated 0, unknown 0, dropped 0 (`python3 build/distill/check_ledger.py STRUCTURE`: "claims in: 57; placed: 57; missing 0; duplicated 0; unknown 0").
- Roles: decision 36, fact 8, rejected 3, acceptable-when 1.
- Nodes: js-philosophy L1 1, L2 6, L3 10 (17); pig-js-defaults L1 1, L2 6, L3 27 (34); ROOT nodes are the integrator's.
- Decisions for review: D1 cycles forbidden, D2 top-level await at entry points only, D3 named exports only, D4 no paradigm mandate, D5 barrels only at a public entry point, D6 no static-only container classes, D7 read-only exported state.
- Undecided: declared layering (STRUCTURE.DIRECTION.2 and PIG-JS.STRUCTURE.DIRECTION.3).
- Restriction demotions: STRUCT-C60 (decision to fact, node undecided), STRUCT-C32 (to acceptable-when), STRUCT-C29 (blanket position not adopted), STRUCT-C54 (to rejected).

## L2 claims

- Grounded: 57 claims routed (slots 01_lang 8, 02_types 1, 04_struct 48), each placed once; the branch checker reports 0 errors and 51 skeleton nodes.
- Grounded: tree. js-philosophy STRUCTURE has six children (HIDING, STATE, PURITY, DIRECTION, NAMING, PARADIGM); pig-js-defaults has six (FORMAT, NODE, LOADING, SURFACE, DIRECTION, PACKAGE). Philosophy holds language-neutral principles (Parnas, Cook, Codd, naming experiments, paradigm evidence, effect-free importing); defaults hold the JavaScript and Node module mechanics and rules, by the language-swap test.
- Grounded: 25 judge records, one per defaults node holding a decision; LOADING.5 holds facts and one acceptable-when and no decision, so no record.
- Grounded: folklore rows. "Cyclic imports always crash" (STRUCT-C08) and "CommonJS cannot load ES modules" (STRUCT-C16) are `rejected` rows on DIRECTION.1 and NODE.3. The other folklore beliefs on the STRUCT slot (C40 underscore privacy, C44 built-in prototypes, C67 semver) are routed to other branches.
- Inferred: D1 cycles. Forbidding cycles is the demanding practice for locality, but the grounds are MDN advice (one T1 ground, used from the slot-01 claim LANG-C64 where the register row is unrestricted; the same sentence is a position in slot 04), Google and plugin positions, and no admitted measurement. Node is `known | conflict | unvalidated`. Scoping call for review.
- Inferred: D2 top-level await at entry points only. Mechanism is T1; the scope is inferred from it.
- Inferred: D3, D6, D7 and four more nodes (FORMAT.4, SURFACE.2, PACKAGE.4, NAMING.2) rest on style-guide positions as holder's positions only, marked `holder position only`, never counted as evidence.
- Inferred: D4. "Choose the paradigm by intent" follows from the absence of JavaScript-scoped evidence (STRUCT-C64 is inferred); the restricted studies are used only to show that no ground exists.
- Inferred: D5 barrels. The narrowing to "aggregate only at a public entry point" is mine; the blanket position of the single T3 source is not adopted. Tension to review: the plan says T3 alone cannot make a node `known`, the brief's epistemic format would allow `known | unvalidated: single T3 source`; I followed the brief. Same tension on DIRECTION.2 (single T3, a fact about the lint rule).
- Open: declared layering has no admitted ground (STRUCT-C60 demoted to fact). Evidence that would settle it: a T1 source or two independent T2 sources stating a layering rule with grounds, or a study linking layer violations to cost of change; the second T2 lead noted in the claim is not yet audited.
- Open: gaps recorded as notes, not nodes: application state design, composition versus inheritance, casing and file naming. ES modules versus CommonJS for new code is decided in SUBSET (LANG-C57, STRUCT-C21), so FORMAT.1 carries a proposed link to SUBSET.
- Grounded: 15 nodes carry `unvalidated: quote tool-extracted` because their only T1 document's quote is tool-extracted (46 of 57 claims have a tool-extracted quote).
- Inferred: cross-branch overlaps for the integrator. P5 merge candidate: STRUCT-C05 and LANG-C57 (module runs once); freeze group split three ways (STRUCT-C01 to C03 here, LANG-C38 and C39 in SUBSET, DOMSEC-C52 and RUNSEC-C09 in DEFENSE); W3C TAG claims C54 and C56 may overlap the web-architecture API contract (11_coverage candidate, untagged).
- Grounded: 17 proposed links to other branches (14 from defaults: SUBSET 4, CONTRACTS 4, DEFENSE 1, CONTROL 1, VERIFICATION 3, DEPENDENCIES 1; 3 from philosophy: SUBSET 2, DEFENSE 1) and 5 inter links to python-kb-philosophy (STRUCTURE, STRUCTURE, DATACENTRICITY, COMMUNICATION, POLYGLOT); link 3 to python is inferred.

## L3 full

### Files written (all in `build/distill/branches/STRUCTURE/`)

`ledger.md` (48 rows), `skeleton.md` (both graphs, intentlinks, proposed links, 25 judge records), `decisions.md` (12 decisions, 1 undecided topic), this `result.md`.

### Method

1. Read the brief (Shared and Step 5b), `build/plan.md`, `target_hierarchy.md`, the primers P2, P4, P5, UID and name rules, the 57 claim rows, the STRUCT parts of `12_dissent` (topics 5 to 8, folklore rows) and `11_coverage` (O08, O15, O16, O19, tensions, gaps G-M10 and G-L04), `5a_route/result.md`, the register rows of every cited source (SRC-028, 029, 030, 038, 085 to 092, 094, 095, 239, 244, 251, 252, 254, 256 to 261, 312 to 315) and the uids of `python_kb_philosophy.yaml`.
2. Cut the branch by its purpose (locality of change): what to hide, where state lives, what importing does, which way dependencies flow, how things are named, which paradigm. Split each claim by the language-swap test: principle statements to js-philosophy, JavaScript and Node mechanics to pig-js-defaults. Contested decisions sit in pig-js-defaults so they carry a judge record.
3. For each node chose the most demanding practice an admitted source supports; a restricted position decides only as holder's position and the node's state says so. Single-claim rows for folklore and rejected positions; corroborating positions merged into the decision row of the claim they concur with.
4. Epistemic state: `known` on one T1 or two independent T2 grounds; `| unvalidated: single <tier> source`, `| conflict: <position, holder>`, `| unvalidated: quote tool-extracted` per the brief; `undecided | missing` where no ground exists.
5. Ran `python3 build/distill/check_ledger.py STRUCTURE`.

### Counts

| graph | L1 | L2 | L3 | total | undecided | nodes with `conflict` |
|---|---|---|---|---|---|---|
| js-philosophy | 1 | 6 | 10 | 17 | 1 (DIRECTION.2) | 2 (DIRECTION.1, PARADIGM) |
| pig-js-defaults | 1 | 6 | 27 | 34 | 1 (DIRECTION.3) | 5 (LOADING.4, LOADING.6, SURFACE.1, SURFACE.5, DIRECTION.1) |

Ledger rows by node group: js-philosophy HIDING 3, STATE 2, PURITY 1, DIRECTION 1, NAMING 3, PARADIGM 2; pig-js-defaults FORMAT 4, NODE 6, LOADING 9, SURFACE 8, DIRECTION 4, PACKAGE 5 (rows 013 to 048).

### Restriction demotions and restricted uses (checked against `build/audit/source_register.md`)

| claim | source and restriction | treatment |
|---|---|---|
| STRUCT-C60 | SRC-085: mechanism only, "grounds no layering principle"; SRC-257: principle of hiding only | decision demoted to `fact`, node undecided |
| STRUCT-C32 | SRC-256: bundling advice and module counts are a 2018 position | demoted to `acceptable-when` with its condition |
| STRUCT-C29 | SRC-315: his synthetic measurement only, "get rid of all barrel files" is his position | measurement and mechanism used; blanket position not adopted, decision narrowed |
| STRUCT-C54 | SRC-261: positions for platform API design, transfer is inference | `rejected` row with the condition under which it wins |
| STRUCT-C24, C03, C25, C26, LANG-C15, C27, C28, C56, C12 (inside row 017) | SRC-239, SRC-244, SRC-312, SRC-261: positions only, never evidence | used as holder's position; flagged in epistemic state; not counted as grounds |
| STRUCT-C09 | SRC-029: advice is MDN's position in slot 04; SRC-313: "always dangerous" is the maintainers' position; SRC-239 position | Google and plugin parts positions only; MDN advice counted once as T1 through LANG-C64 (slot-01 row unrestricted); flagged as a scoping judgement |
| STRUCT-C30 | SRC-095: webpack's own behaviour, never a ground for preferring webpack | kept as `fact` only |
| STRUCT-C63, C64 | SRC-251, SRC-258, SRC-314: never a ground for a paradigm choice in JavaScript | used only to show that no ground exists |
| STRUCT-C58, C62, C65, C55, C57 | SRC-257, 259, 252, 260, 254: principle or conceptual or experimental, transfer to JavaScript is inference | philosophy level only; flagged in epistemic state |
| STRUCT-C10, C61 | SRC-313 rule behaviour and cost, SRC-085 mechanism | within restriction, no demotion |

Not demoted, checked: SRC-029 mechanism uses (live bindings, cycles, hoisting, top-level await, aggregation) fall inside the 04_struct restriction; LANG-C58 and LANG-C64 are slot-01 uses where the row is unrestricted.

### Decisions for review

D1 cycles, D2 top-level await, D3 named exports, D4 paradigm, D5 barrels, D6 static-only classes, D7 exported state; D8 to D12 are weighty or single-source and listed in `decisions.md` with rejected positions and the condition under which each wins.

### Undecided nodes

STRUCTURE.DIRECTION.2 and PIG-JS.STRUCTURE.DIRECTION.3 (declared layering): see `decisions.md` U1.

### Not done

- No claim dropped, none duplicated; tag spellings in `claims.md` untouched (generated file).
- No YAML or ig-tool assembly (stage 6). No other branch folder touched, nothing committed or pushed.
