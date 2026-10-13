# Result: step 5b, branch RUNTIME

## L1 headline

The 34 RUNTIME claims are consolidated into a 6-node subtree in js-philosophy and a 20-node subtree in pig-js-defaults under one rule, measurement before belief, so no engine-level tuning is prescribed without a measurement of the real workload; certainty: grounded on the placement (checker clean), inferred on the measurement-first rule itself, which no admitted source states normatively and which rests on T2 for engine claims.

Pinned:
- Claims in 34, ledger rows out 31 (claims placed 34, 0 dropped, 0 duplicated; 4 rows carry `-` for a rejected belief with no claim of its own).
- Nodes: js-philosophy 6 (L1 1, L2 3, L3 2); pig-js-defaults 20 (L1 1, L2 4, L3 14, L4 1).
- Decisions for review: 10 (D1 to D10); undecided nodes: 1 (`PIG-JS.RUNTIME.MEMORY.6.1`, container heap limit).
- Restriction demotions: 1 (STRUCT-C43 to acceptable-when), 1 checked and not overstepping (STRUCT-C42), 1 open (RUNTIME-C22 flag part).

## L2 claims

- Placement: all 34 claims placed once; `check_ledger.py RUNTIME` reports claims in 34, placed 34, missing 0, duplicated 0, unknown 0. grounded.
- Roles: 18 decision, 5 rejected, 4 fact, 4 acceptable-when across 31 rows (5 philosophy rows, 26 defaults rows). grounded.
- Central decision: measurement first outranks unmeasured micro-optimization; STRUCT-C42 and C43 (MDN, T1, no figures) become acceptable-when, with the condition "a profile shows the cost". grounded on placement, inferred on the rule (decision D1).
- Engine-level claims rest on T2 only (SRC-302, SRC-303, SRC-301, SRC-306); the measured statement of `PIG-JS.RUNTIME.MEASURE.2` is `unvalidated: single T2 source`. grounded.
- 12_dissent folklore for this branch is three beliefs: circular references leak (refuted), holey arrays (restricted), snapshots infeasible on large heaps (restricted); each is a rejected row. grounded.
- Most nodes rest on one T1 page with a tool-extracted quote and carry `unvalidated: quote tool-extracted`; two T2 independent grounds (SRC-307, SRC-305) make `RUNTIME.METHOD` plain `known`, with the Java and C to JavaScript transfer inferred. grounded.
- Benchmark claims split by the language-swap test: C61 and C62 to philosophy, C58 to C60 (Node core figures) to defaults. inferred (judgment).
- Restriction checks: SRC-195 figures kept as illustration only; SRC-080 used for mechanism only; SRC-302, 303, 301, 308, 305, 307 used within their stated scope; SRC-088 directive form of C43 demoted; SRC-189 flag `--interpreted-frames-native-stack` not reconfirmed in the CLI docs as cited. grounded except the last, open.
- One undecided node: the default heap limit under a container or cgroup limit, no admitted source (gap G-M22). open.
- Six proposed cross-branch links (STRUCTURE, CONTROL three times, DEFENSE, SUBSET); two inter links to python-kb-philosophy (INTENTIONALITY, REPRODUCIBILITY), inferred. inferred.

## L3 full

### Claims in, rows out

Claims routed to RUNTIME: 34 (32 of slot 09_runtime, 2 of slot 04_struct: STRUCT-C42 and
STRUCT-C43). Groups (25 claims): benchmark-method (5), built-in-profilers (2),
engine-optimisation-warnings (5, two from slot 04), event-loop-diagnosis (3), heap-limit (2),
heap-snapshots (4), v8-gc-mechanism (2), weak-references (2); 9 claims ungrouped (`-`).

Ledger `ledger.md`: 31 rows. Philosophy RUNTIME-001 to RUNTIME-005; defaults RUNTIME-006 to
RUNTIME-031. Rows with `-` as claim_ids: RUNTIME-004, 011, 012, 027 (four); the five rejected
rows are these four plus RUNTIME-030 (C49, a claim). Merged rows (several
claims, one statement): RUNTIME-002 (C61, C62), 014 (C58, C59), 017 (C23, C24), 022 (C30, C47),
024 (C44, C46), 028 (C28, C29, C14).

Checker output (`python3 build/distill/check_ledger.py RUNTIME`):

```
claims in: 34; placed: 34; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 5, 'pig-js-defaults': 26}; by role: {'decision': 18, 'rejected': 5, 'fact': 4, 'acceptable-when': 4}; skeleton nodes: 26
```

### Subtree

Philosophy (`RUNTIME`): MEASURE (measurement before belief), METHOD (measurement method),
MEMORY with two children (reachability decides leaks; bounded long-lived state).

Defaults (`PIG-JS.RUNTIME`): MEASURE (profile first; engine-level tuning needs a measurement;
callback file APIs on a measured need), METHOD (statistics; quiet environment), DIAGNOSE
(context and symptom; event loop health; built-in profilers), MEMORY (classify; leak signals;
snapshot comparison; production capture; intended retention; heap limit and collector, with the
undecided container child). Links: 2 intra in philosophy, 9 intra in defaults, 9 defaults to
philosophy, 6 proposed to other branches, 2 to python-kb-philosophy. 14 judge records, one per
defaults node holding a decision.

### Decisions for review

D1 measurement first versus unmeasured micro-optimization (the weightiest); D2 restriction
placement of the MDN warnings; D3 promise file APIs by default; D4 benchmark method split
across graphs; D5 weak references avoided; D6 production capture; D7 heap limit; D8 folklore
rows with `-` claim ids; D9 epistemic markers beyond the brief's list; D10 no philosophy
diagnosis node. Details, rejected positions and their winning conditions: `decisions.md`.

### Undecided nodes

`PIG-JS.RUNTIME.MEMORY.6.1` Heap limit inside a container: `undecided | missing: no admitted
source`. Checked: SRC-199, SRC-202 and SRC-079 as cited by C48 state no container or cgroup
behaviour; LC-36 (Node documentation on default heap limit in containers) was not located by
stage 4. Would settle it: that page or a T2 study.

### Restriction demotions

| claim | source | restriction | outcome |
|---|---|---|---|
| STRUCT-C43 | SRC-088 | mechanism facts: classes over prototypes, `setPrototypeOf` warning | directive form demoted to acceptable-when (RUNTIME-010) |
| STRUCT-C42 | SRC-083 | closure mechanism and the performance note only | not overstepped; acceptable-when comes from the max rule (RUNTIME-009) |
| RUNTIME-C22 | SRC-189 | only what current docs reconfirm, such as the `--perf-basic-prof` flags | flag part `--interpreted-frames-native-stack` not reconfirmed in what was read; acceptable-when and open (RUNTIME-020); the CLI page could not be re-fetched in this session |
| RUNTIME-C20 | SRC-195 | figures only as illustration | figures stated as illustration, not as grounds (RUNTIME-006) |
| RUNTIME-C19 | SRC-080 | mechanism only, offloading advice excluded | stated as fact, advice not used (RUNTIME-018) |
| RUNTIME-C56, C54, C53, C55 | SRC-303, 301, 308, 302 | mechanism and dated figures, no prescriptions without measurement | placed as facts or as the measurement-first decision; no prescription drawn from SRC-303 |
| RUNTIME-C61, C62 | SRC-307, SRC-305 | method only, no Java numbers; abstract-level only | no numbers transferred; abstract-level claims only |

### Judgment calls to confirm

1. Claims C28, C29 and C14 share one decision row (RUNTIME-028); split on request.
2. `-` claim_ids on four rejected rows (D8).
3. Philosophy holds only language-neutral or engine-neutral statements (C61, C62, C63, C27, C53); the V8 and Node mechanism claims stay in defaults, although the plan allows JavaScript-distinct philosophy nodes.
4. Node uid for the undecided child sits at L4 under `PIG-JS.RUNTIME.MEMORY.6`.

Files: `ledger.md`, `skeleton.md`, `decisions.md`, `result.md` in this folder.
