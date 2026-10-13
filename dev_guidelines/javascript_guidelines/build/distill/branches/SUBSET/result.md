# Step 5b result: branch SUBSET

## L1 headline

All 61 SUBSET claims are placed once in 70 ledger rows (0 dropped) under 42 nodes in two graphs (js-philosophy 7, pig-js-defaults 35), with 34 decisions, 0 undecided nodes and 4 style-guide positions demoted from evidence; certainty: grounded for counts and the checker run, inferred for the max-rule choices on three contested topics (`== null`, implicit coercion shorthands, private marking) and for the maintainer-facing flags below.

Pinned:
- Claims in 61 (LANG 51, STRUCT 8, TYPES 1, QUALITY 1) and ledger rows out 70: 59 rows carry the 61 claims (one merged row holds three), 11 rows with claim_ids `-` carry rejected or acceptable-when positions from the folklore audit; claims missing 0, duplicated 0, unknown 0 (`check_ledger.py SUBSET` exit 0).
- Nodes: js-philosophy 7 (L1 1, L2 6); pig-js-defaults 35 (L1 1, L2 6, L3 28); 28 judge records.
- Roles: decision 34, fact 17, acceptable-when 13, rejected 6.
- Decisions for review: `== null` forbidden outright (against the dissent slot's recommendation), implicit-coercion rule on positions only, hash private fields over TypeScript `private`, stage 4 only, `Object.hasOwn`, strict mode everywhere (inferred); see `decisions.md`.
- Undecided: none. Accessors (OBJECTS.4) and statement termination (EVOLUTION.5) are decided on one Google position each, flagged `unvalidated`; LANG-C55 is confirmed by RUNSEC-C07 (two T1 sources) for untrusted keys.
- Restriction demotions: to acceptable-when LANG-C07, C08, C14, C16 (Google JS position only); to fact only LANG-C13, C25, C27; flagged but kept LANG-C22, C54, STRUCT-C46, QUALITY-C19 (decisions on a position alone).

## L2 claims

- Grounded: every one of the 61 routed claims is in `ledger.md` exactly once; the branch checker reports `claims in: 61; placed: 61; missing 0; duplicated 0; unknown 0`, 42 skeleton nodes, no row naming an absent node.
- Grounded: tree. js-philosophy `SUBSET` has six principle children (VISIBLE, FAILURE, NUMBERS, STATE, BINDING, MATURITY), all passing the language-swap test; pig-js-defaults `PIG-JS.SUBSET` has six L2 children (STRICTNESS 4 leaves, CONVERSION 6, NUMBERS 4, OBJECTS 6, MUTATION 3, EVOLUTION 5), each within the two-to-six limit.
- Grounded: only two claims are language-neutral (LANG-C29 tolerance is no cure, STRUCT-C66 immutability versus read-only), so js-philosophy holds two rows; its other principles are inferred roll-ups of pig nodes and are marked so.
- Grounded: folklore. The three beliefs `12_dissent` refutes on this branch are rejected rows: const makes a value constant (SUBSET-010), freeze is deeply immutable (SUBSET-056), underscore means private (SUBSET-045). The restricted beliefs on the branch (BigInt replaces Number, JSON round trip, logical OR default, built-in extension) are rejected or acceptable-when rows with the condition.
- Inferred: `== null` decided as forbid-all (SUBSET-016) because the max rule picks the more demanding of two exact options; the dissent slot recommended the opposite, so the choice is the likeliest to be overruled together with the coercion-shorthand rule (SUBSET-019), whose grounds are positions only.
- Inferred: contested private marking (LANG-C12, STRUCT-C41, merged in SUBSET-043) decided as hash fields everywhere, with TypeScript `private` as acceptable-when on down-levelled targets.
- Grounded: restrictions. Google JS guide and Airbnb are positions only, so four Google-only claims are not decisions (two more, STRUCT-C46 and QUALITY-C19, are decisions on a position alone, flagged); SRC-024 restricts semantics to ECMA-262 and MDN, so LANG-C13 is a fact only; SRC-237 and SRC-238 are evidence of occurrence and harm, never rules, so LANG-C25 and C27 are facts.
- Grounded: LANG-C55 (`Object.hasOwn`) is confirmed: RUNSEC-C07 in DEFENSE (consensus) rests on MDN prototype pollution (SRC-139) and Node security best practices (SRC-078), both T1 unrestricted for that slot, and states Object.hasOwn for untrusted keys; extension to all reads is inferred.
- Inferred: accessors (no getters or setters) and statement termination (semicolons, braces) are decided on one Google position each, by predictability; no mechanism evidence exists in the claim base (G-L14, G-M02), and what would strengthen each is named in `decisions.md`.
- Grounded: cross-branch overlap handled by proposed links, not copies: own-property (O15) and freezing (O16, X1) to DEFENSE and STRUCTURE, prototype modification (O19, X1) to DEFENSE and RUNTIME, JSON and BigInt (O14) to CONTRACTS and DEFENSE, module facts to STRUCTURE, lint gates to VERIFICATION.
- Convention to align at 5c: skeleton epistemic cells write the IG separator ` | ` as `\|`; a node may hold several `decision` rows when one topic yields several rules; ledger rows with claim_ids `-` carry folklore and position rows that no single claim states.

## L3 full

### Method
Read the brief (Shared, Step 5b), `plan.md` (goal, boundary, admission policy, claim format, target graphs, maintainer decisions), `target_hierarchy.md`, the IntentGraph primers 00, 01 and 03A, `branches/SUBSET/claims.md` in full, the `12_dissent` topics 1 to 3 and the folklore table, the `11_coverage` overlap rows O14 to O16, O19, gaps G-M01, G-M02, G-M29, G-L14 and the tension rows, the 5a route result, the Python philosophy graph uids, and the register rows of every source the 61 claims cite. Role assignment: a rule an admitted source supports is `decision`; a mechanism it rests on is `fact`; the weaker practice is `acceptable-when`; a refuted or restricted belief is `rejected`. Then the tree was cut by the branch purpose (predictability): six capabilities (strict scope, conversion, numbers, objects, mutation, evolution), claims attached afterwards.

### Counts
| item | js-philosophy | pig-js-defaults |
|---|---|---|
| L1 nodes | 1 | 1 |
| L2 nodes | 6 | 6 |
| L3 nodes | 0 | 28 |
| ledger rows | 2 | 68 |
| intentlinks inside the branch | 1 | 11 |
| inter links out | 3 (to python-kb-philosophy) | 10 (to js-philosophy) |
| proposed links to other branches | 3 | 14 |
| judge records | 0 | 28 |

Ledger roles: decision 34, fact 17, acceptable-when 13, rejected 6. Rows labelled contested: 6 (SUBSET-016, 017, 019, 022, 043, 046); the rest are consensus, single-source or `-`.

### Restriction audit (register rows checked)
| source | restriction | outcome |
|---|---|---|
| SRC-239 Google JS | positions only, never evidence, per slot | LANG-C07, C08, C14, C16 demoted to acceptable-when; STRUCT-C46 and QUALITY-C19 decided on a position alone, flagged; its == null position recorded as acceptable-when |
| SRC-312 Airbnb | positions only | never a ground alone; LANG-C55 reason flagged |
| SRC-244 Google TS | positions with reasons, never evidence | TypeScript private as acceptable-when per target |
| SRC-003 no-implicit-coercion | rule and options only, rationale is a position | decision SUBSET-019 labelled positions only |
| SRC-024 class fields | semantics from ECMA-262 and MDN | LANG-C13 fact only |
| SRC-028 finished proposals | status facts only | LANG-C54 flagged, rule inferred |
| SRC-019 and SRC-025 Temporal | dated availability | LANG-C43 labelled dated |
| SRC-023 BigInt proposal | motivation only, semantics from MDN | claims also cite MDN: no demotion |
| SRC-029 modules guide | cycle advice is an editorial position | not used by this branch's rows |
| SRC-088 inheritance guide | mechanism facts only | STRUCT-C44 and STRUCT-C45 are mechanism facts: kept |
| SRC-236, 237, 238 | no JS rule; evidence of occurrence; never a rule | LANG-C29 in the philosophy graph; LANG-C25 and C27 facts; LANG-C26 decision flagged single T2 |
| SRC-253 | taxonomy, no effect evidence | STRUCT-C66 as a distinction only |

### Files
- `ledger.md`: 70 rows, 61 claims.
- `skeleton.md`: both subtrees, links, judge records.
- `decisions.md`: sections A to F.
- This file.
