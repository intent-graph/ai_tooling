# Step 5b result: branch CONTROL (explicit failure)

## L1 headline

All 82 CONTROL claims are placed once in 86 ledger rows (0 dropped) under a 6-node philosophy subtree and a 35-node defaults subtree, with decisions chosen by the max rule; certainty: grounded for counts and the checker run, inferred for the few demotions and conditions listed in L2.

Pinned:
- Claims in 82; ledger rows out 86, of which 77 carry claims (5 merges: ASYNC-C18 with LANG-C45, ASYNC-C23 with RUNTIME-C31, ASYNC-C26 with STRUCT-C53, ASYNC-C55 with RUNTIME-C42, ASYNC-C04 with RUNTIME-C40) and 9 are claim-less folklore `rejected` rows; claims dropped 0; `check_ledger.py CONTROL`: missing 0, duplicated 0, unknown 0.
- Nodes: js-philosophy 6 (L1 1, L2 5, L3 0); pig-js-defaults 35 (L1 1, L2 6, L3 25, L4 3); 25 judge records.
- Roles: decision 60, fact 15, rejected 9, acceptable-when 2, deferred 0; graph split 11 philosophy rows, 75 defaults rows.
- Decisions for review: 14 weighty (D1 to D14) and 39 single-source decision rows, in `decisions.md`.
- Undecided nodes: 3 (PROMISES.4.1 concurrency limits and retry, ERRORS.2.1 operational versus programmer errors, SCHEDULING.2.1 browser yielding). PROMISES.6 is decided: async functions and await by default (single T2, V8 team 2018, dated position), flat chains acceptable.
- Restriction demotions: ASYNC-C52 to a dated-position decision on PROMISES.6 (belief row rejected); ASYNC-C50, C49, C51 to fact; ASYNC-C21 to acceptable-when; RUNTIME-C12 figures illustration only; ASYNC-C15 kept as holder's position.

## L2 claims

- Grounded: the claim set is complete and exclusive: 82 claims in (ASYNC 53, RUNTIME 26, STRUCT-C53, LANG-C45, TYPES-C12), 82 placed, checker clean on `check_ledger.py CONTROL` (41 skeleton nodes found).
- Grounded: no contested topic of 12_dissent (16) falls in CONTROL; all 9 folklore beliefs that concern it are refuted and each is a `rejected` row: missing return, unhandled rejections only warn, Promise.all cancels, promises cancellable, setTimeout(0) exact, 0 ms timers, then on a resolved promise runs now, nextTick for deferral, async/await slower.
- Grounded: the cut is 5 philosophy principles (failure has an owner; bounds and stoppers; one shared cooperative thread; pacing; designed process end) and 6 defaults groups (promises, errors, bounds, scheduling, flow, process); philosophy rows are the language-level facts (C07, C25, C35, C31), the event-loop principle (C38), two stream facts and the uncaught-state principle (C05).
- Grounded: 39 of the decision rows rest on a single source and say so in the node state; 21 decision rows are consensus.
- Inferred: the max choices that no source states as a ranking: AbortSignal as the single cancellation primitive (D5), partition only as the weaker alternative to workers (D8), do-not-disable requestTimeout (D9), the must-exit rule for signal listeners (RUNTIME-C39).
- Inferred: ASYNC-C21 (Google position only, restricted to positions) is placed `acceptable-when`; the no-silent-catch rule is carried by an inter link to python DEFENSIVE, so the ERRORS.2 node is not grounded on that rule by evidence.
- Grounded: restriction checks: ASYNC-C52 (SRC-249, 2018) is a decision only as a dated position of one holder, its speed belief a `rejected` row; ASYNC-C50 (SRC-247), C49 (SRC-248) and C51 (SRC-028) are `fact` rows although the extractor labelled them decision or practice; RUNTIME-C12 keeps SRC-184 figures out of the statement as evidence; STRUCT-C53 (SRC-261, positions) only supports ASYNC-C26; SRC-080 offloading advice is not used.
- Open: three undecided nodes; return await inside try/catch is not covered by SRC-246; ECMA-262 and HTML Standard clause text unread (mechanism rests on MDN and Node docs); SRC-079 entry text unreliable (SRC-082 suffices).
- Open for the integrator: RUNTIME-C39 and C41 carry `boundary: web-architecture` and stay as Node-side decisions; O02 is split between philosophy (ASYNC-C05) and defaults (RUNTIME-C37) and may be merged; proposed links to VERIFICATION, CONTRACTS, DEFENSE, RUNTIME, SUBSET, STRUCTURE and the planned web-architecture graph are in `skeleton.md`; folklore rows with `-` in claim_ids reference their refuting row by number.

## L3 full

### Files

- `ledger.md`: 86 rows, format of the brief. Folklore rows have `-` in `claim_ids` because the refuting claim is placed on its own row .
- `skeleton.md`: both graphs, intentlinks (4 philosophy, 8 defaults), 2 inter links to python-kb-philosophy (DEFENSIVE), 6 inter links from defaults to philosophy, 8 proposed cross-branch links, 25 judge records.
- `decisions.md`: A weighty choices D1 to D13, B single-source decisions (table), C undecided nodes with settling evidence.

### Counts

| item | js-philosophy | pig-js-defaults |
|---|---|---|
| L1 nodes | 1 | 1 |
| L2 nodes | 5 | 6 |
| L3 nodes | 0 | 25 |
| L4 nodes | 0 | 3 (all undecided) |
| total nodes | 6 | 35 |
| ledger rows | 11 | 75 |

Rows by role: decision 60, fact 15, rejected 9, acceptable-when 2. Rows by agreement: consensus 35, single-source 50.

### Method

Read the brief (Shared, Step 5b), plan (goal, boundary, admission policy, claim format, targets,
maintainer decisions), the target hierarchy and judge record, the three IntentGraph primers, the python
philosophy uids, the 82 claim rows in full, 12_dissent (all levels), 11_coverage (overlaps O01 to O17,
gaps G-M07 to G-M09, G-L02) and the register rows for every cited source. Partition: by the branch
purpose (explicit failure) and by the failure or resource each rule keeps visible, not by slot. Language
swap: claims about what JavaScript is (language-level facts and the event-loop principle) went to
js-philosophy; host mechanisms, Node and browser APIs and version facts went to pig-js-defaults. Max rule:
each node states the most demanding practice an admitted source supports; weaker practices carry their
condition; where no source supports any position the node is undecided.

### Restriction demotions (detail)

- ASYNC-C52, SRC-249 (history of the await tick reduction, 2018): used as the V8 team's dated position for the PROMISES.6 decision, never as a performance figure; the speed belief is a `rejected` row and the present-day gap is open.
- ASYNC-C50, SRC-247 (API as drafted, never a cross-browser recommendation): `fact` (extractor level: decision).
- ASYNC-C49, SRC-248 (only the not-in-the-language fact): `fact` (extractor level: decision).
- ASYNC-C51, SRC-028 (register facts only): `fact` (extractor level: practice).
- ASYNC-C21, SRC-239 (Google's position, never evidence): `acceptable-when`.
- RUNTIME-C12, SRC-184 (figures only as illustration): `fact`, statement carries no figures.
- ASYNC-C15, SRC-075 (MDN editorial position) and ASYNC-C18 with LANG-C45, SRC-239: kept as decisions, recorded as positions; ASYNC-C18 is also grounded by the SRC-074 mechanism.
- ASYNC-C02, C03, C16, C17, C18, SRC-072 to SRC-074: rule behaviour and rationale only; no tool preference is stated.
- ASYNC-C39, C41, C42, SRC-080: mechanism only; the API list (as of Node 9) and offloading recommendations are not used.
- ASYNC-C11, C54, SRC-059 and SRC-060: rule behaviour; C54 detection is heuristic, noted in the node state.

### Checker output

`python3 build/distill/check_ledger.py CONTROL` from the guideline root:

```
claims in: 82; placed: 82; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 11, 'pig-js-defaults': 75}; by role: {'fact': 15, 'rejected': 9, 'decision': 60, 'acceptable-when': 2}; skeleton nodes: 41
```
