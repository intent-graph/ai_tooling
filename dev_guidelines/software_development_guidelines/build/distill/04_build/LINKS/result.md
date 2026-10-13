# Intentlink completion: result

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/software_development_guidelines/`. Files of this run, in `build/distill/04_build/LINKS/`: `batch.yaml`, `decisions.md`, `result.md`.

## L1 headline

The graph's links go from 196 (159 of them loosely typed `see` or `related`, or untyped) to 403, every one typed realizes, requires, refines, constrains, dataflow or conflicts, one per ordered pair, each with a one-line intent sentence. The batch (`batch.yaml`, 441 operations) passed a dry run on a scratch copy of the real graph (deleted): `status: ok, command: validate, nodes: 292, links: 403, errors: 0, warnings: 0`. The real graph is untouched; the coordinator applies the batch.

- Cross rows read: 405 (nine `cross_links.md` lists), plus the 196 existing links.
- Links added: 248 new links from cross rows; 27 existing links also had to be removed and recreated with the arrow reversed (src and dst are immutable), net zero.
- Existing links retyped: 120 (93 in place, 27 reversed); 5 reworded only, 30 unchanged, 41 removed (20 no relation, 21 merged duplicates).
- Links dropped: 133 (113 cross rows, 20 existing): pointers that only say where a topic is held, analogies, complementarity or consistency notes, and L1 links already carried by finer ones.
- Duplicates merged: 23 ordered pairs given by several rows (stronger type kept), plus 41 inverse or coarse restatements of a kept link: 64 rows merged in all (43 cross, 21 existing).
- Unresolved targets: 1 (J4-17, `ASSURANCE.AVAILABILITY.1` to the L1 branch `CONSTRUCTION`: the record names no node, and no L3 is unambiguous).
- Links per type after the batch: requires 204, realizes 97, refines 39, constrains 32, dataflow 29, conflicts 2 (total 403). Before: requires 29, refines 5, conflicts 2, dataflow 1, related 78, see 60, untyped 21 (total 196).
- Certainty: counts and the dry run grounded; each type choice and each drop inferred from the record sentences (a sample review by the maintainer is the open step).

## L2 claims

Each claim ends with its certainty: grounded (I ran it or can name the file), inferred (follows from record text, not independently checked), open (undecided or unknown).

1. The batch applies cleanly. Dry run on a scratch copy: 441 operations (68 `link.remove`, 98 `link.set`, 275 `link.create`), then `ig-tool validate` reports 0 errors, 0 warnings, 292 nodes, 403 links; the copy is deleted. Grounded.
2. The final set has one link per ordered pair (403 distinct pairs), none between a node and its own ancestor or descendant, and every link carries `shape.type` from the six-type vocabulary. Grounded (checked on the scratch copy and in the build script).
3. Type meanings follow the sibling web-architecture graph, which uses realizes, requires, refines, constrains, dataflow and conflicts: `realizes` = source carries out a decision held by the target; `requires` = source holds only if the target exists; `refines` = source specialises the target; `constrains` = source's rule bounds the target's decision (arrow from the bounding rule); `dataflow` = source output is target input. The reading of the sibling's arrows is grounded in its link sentences; applying them here is inferred.
4. Existing links all got a type: related, see and untyped links became requires (the dominant case), realizes, refines, constrains or dataflow, or were dropped. One existing link was mistyped (`BEHAVIOUR.6` to `BEHAVIOUR.1`, dataflow): it states an application of a principle, so it became refines. The two conflicts and the other requires/refines links were kept. Inferred.
5. Drops are recorded with a reason each (`decisions.md` section 4): 133 links. The commonest reasons are a locator pointer ("held there", 44), a restatement already carried by a finer or inverse link (43), and analogy, complementarity or consistency with no dependency. Pointers were dropped even where useful to readers, because the graph states dependencies, not reading hints. Inferred; the maintainer may overturn individual drops.
6. Duplicates and inverses: where the same ordered pair came from several rows the stronger type won (requires or realizes over see/related/index; dataflow over see for consumer-side signals), and where a pair appeared in both directions the load-bearing direction was kept and the other merged (`decisions.md` sections 1 and 5). Inferred.
7. L1 endpoints: Of the 12 rows with an L1 endpoint, 9 were dropped (their relation is lifted from finer links, which are never created by hand, or no relation is stated), 1 is unresolved and 2 are kept. The two kept L1 links have no finer link beneath them: `OPERATION.RECOVERY.5` requires `CHANGE_FLOW` and `OPERATION` realizes `TRANSVERSE.CONFIG.2`. Inferred.
8. Reversals and narrowings (`decisions.md` section 6): where the row's arrow put the dependent node as target, the link is stored dependent to depended-on (27 existing and 41 cross links reversed); 13 endpoints were narrowed from an L2 node to the L3 node the record's wording makes unambiguous (for example canary evaluation to `DEPLOY.2`). Inferred.
9. Open: J4-17 (`ASSURANCE.AVAILABILITY.1` to `CONSTRUCTION`, design of a degraded mode "held in code construction") has no unambiguous node; the maintainer names one or the link stays absent. Open.
10. Open: borderline typings, mainly realizes versus requires versus refines on practice-to-decision pairs (for example `EVOLUTION.INCREMENTAL.1` to `CHANGE_FLOW.ROLLBACK`, typed realizes) and the 22 cross-branch constrains links, are judgement calls on the record sentences. Open.

## L3 full

### Method

1. Read the primers (four link patterns; lifted links are never created by hand), the batch format (`link.create`; `link.set` takes `intent` and `shape`; `link.remove`) and the sibling graph's link vocabulary. The link type is stored as `shape.type`.
2. Loaded all 196 existing links of the graph (via `ig-tool query` and the file's `intentlinks` block, never the whole file) and the 405 rows of the nine lists (J1: 13, J2: 29, J3: 49, J4: 38, J5: 61, J6: 48, J7: 49, J8: 63, J9: 55). Union: 601 rows over 578 ordered pairs; 23 pairs were given by two rows.
3. One decision per row in three decision files (existing links, J1 to J4, J5 to J9), each of the form kept with a type and intent sentence, dropped with reason, merged into another row with reason, or unresolved. A script resolved arrows (reversal, narrowed endpoint), built the final set, and checked it: no collision, no tree-implied pair, no self link, no row left without a decision.
4. Generated `batch.yaml` in the order remove, set, create so that a reversed link's old uid is gone before the new one is created; link uids are auto-generated (`SRC_DST`).
5. Dry run on a copy of the real graph, then `ig-tool validate`; the copy was deleted.

### Accounts

| | rows | kept | dropped | merged | unresolved |
|---|---|---|---|---|---|
| existing links | 196 | 155 (30 unchanged, 5 reworded, 93 retyped, 27 reversed) | 20 | 21 | 0 |
| J1 ownership | 13 | 4 | 3 | 6 | 0 |
| J2 assurance core | 29 | 15 | 8 | 6 | 0 |
| J3 assurance integrity | 49 | 21 | 20 | 8 | 0 |
| J4 assurance runtime | 38 | 20 | 8 | 9 | 1 |
| J5 construction | 61 | 31 | 27 | 3 | 0 |
| J6 change flow | 48 | 43 | 3 | 2 | 0 |
| J7 operation | 49 | 32 | 10 | 7 | 0 |
| J8 evolution | 63 | 47 | 15 | 1 | 0 |
| J9 transverse | 55 | 35 | 19 | 1 | 0 |
| all cross rows | 405 | 248 | 113 | 43 | 1 |

Final graph: 403 links, 222 between different L1 branches and 181 inside one L1 branch. Cross-branch links by type: requires 88, realizes 84, constrains 22, dataflow 19, refines 9.

Operations: 68 `link.remove` (41 existing dropped or merged, 27 reversed), 98 `link.set` (93 retyped, 5 reworded), 275 `link.create` (248 new, 27 reversed).

### Type per kind of relation (how rows were mapped)

- A practice branch (CHANGE_FLOW, OPERATION, CONSTRUCTION, TRANSVERSE, EVOLUTION) carrying out a decision held in ASSURANCE or OWNERSHIP: realizes (the judge records' "realizes" rows, kept where the source really carries the decision out; for example build realizes placement of checks, protected mainline realizes the gate that cannot be skipped).
- "X is held in Y" where the source's rule only works with Y's rule: requires (for example security findings under the false-alarm budget of `RULES.1`).
- A rule applied to a narrower case: refines (for example static security analysis refines the static layer).
- A rule that limits a decision elsewhere: constrains, arrow from the limiter (retention periods bound backup retention, privacy rules bound test data, on-call load bounds paging).
- An output consumed elsewhere: dataflow (breaking point from a load test feeds capacity planning, deprecation announcements feed the consumer side of a service, time to detect feeds the maturity cycle).
- Conflicts: only the two already in the graph (`RULES.1` against `BEHAVIOUR.7`, `CONTRACTS.1` against `CONTRACTS.2`); the J6 conflicts the skeleton had are resolved in the judge records and carry no link.

### Where to read the detail

- `decisions.md`: section 1 same-pair duplicates and the type kept; 2 existing links retyped or reworded; 3 existing links reversed; 4 dropped, with reasons (133); 5 merged, with the surviving link (64); 6 arrows reversed or endpoints narrowed; 7 unresolved.
- `batch.yaml`: the operations; each `link.create` carries `shape: {type: ...}` and its intent sentence.

### Notes for the coordinator

- Apply with `ig-tool apply -g <graph> --batch batch.yaml -o <graph> --role builder -m "<message>"`, then `ig-tool validate`; the expected line is `nodes: 292, links: 403, errors: 0, warnings: 0` if the graph is unchanged since this run.
- Counts depend on the graph holding exactly the 196 links read; if other units added links meanwhile, the removes and sets target uids that may no longer exist and the apply would fail atomically.
- No link was created from L1 nodes except two (see L2 claim 7); lifted links are computed by the tool.
- Several scratch helper files were written to this session's scratch directory outside the guideline folder; none are part of the deliverable.
