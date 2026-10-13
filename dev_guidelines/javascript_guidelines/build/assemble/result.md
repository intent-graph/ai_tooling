# Stage 6 result: the two IntentGraphs of the JavaScript guideline

## L1 headline

Both graphs are built with `ig-tool`, validate with 0 errors and 0 warnings, and pass a completeness check against the integrated skeleton and ledger (0 failures); one tool limit forced one library step (tree of the defaults graph), and no skeleton node, ledger claim or link is missing. Certainty: grounded, checked by script and by `ig-tool validate -m` on the manifest.

Pinned:
- Nodes and links, js-philosophy: 108 nodes, 48 intentlinks (33 within branches, 15 across branches), 23 inter links to python-kb-philosophy.
- Nodes and links, pig-js-defaults: 270 nodes, 146 intentlinks (78 within branches, 68 across branches), 90 inter links to js-philosophy. Total 378 nodes, 307 links.
- Validate summary, js-philosophy: `graph: intent_graphs/js_philosophy.ig.yaml, nodes: 108, links: 48, inter_links: 23, issues: 0, errors: 0, warnings: 0` (with `-m intent_graphs/intent_resources.yaml`).
- Validate summary, pig-js-defaults: `graph: intent_graphs/js_defaults.ig.yaml, nodes: 270, links: 146, inter_links: 90, issues: 0, errors: 0, warnings: 0` (with `-m intent_graphs/intent_resources.yaml`).
- Not built: the 10 planned boundary links to `web-app-philosophy` and `pig-web-defaults` (their graphs do not exist; listed in `intent_graphs/README.md`); the `examples` field of every node (skeleton and ledger carry no separate case, the concrete cases stay inside the constraint sentences). Nothing else.
- Open for the owner: `ig-tool` rejects the brief's `PIG-JS.*` uids under the root `PIG-JS.ROOT`; the tree was laid with the IntentGraph library, not the CLI (L2, L3).

## L2 claims

Build
- Grounded: `intent_graphs/js_philosophy.ig.yaml` was built by `ig-tool init --root`, `ig-tool apply --batch` (nodes with parents, constraints, design notes, impl pointers, epistemic states, 48 intentlinks) and 23 `ig-tool link create` calls; every command carried `--role assembler` and a `-m` note. Hand-written YAML: none.
- Grounded: `intent_graphs/js_defaults.ig.yaml` was built by `ig-tool init`, one library step for the tree (270 nodes, uid, name, intent, parent), `ig-tool apply --batch` (`node.set` content for all 270 nodes, 146 intentlinks) and 90 `ig-tool link create` calls.
- Grounded: `intent_graphs/intent_resources.yaml` lists product `js-philosophy`, product `python-kb-philosophy` (relative path to the Python philosophy file), projection target `javascript` with `pig-js-defaults`. `intent_graphs/README.md` follows the shape of the Python one and lists the 10 planned links.
- Grounded: re-runnable from scratch: `python3 build/assemble/build_batches.py`, then `zsh build/assemble/build_graphs.sh` (about 40 s), then `python3 build/assemble/check_complete.py`, all from the guideline root.

Counts
- Grounded: ledger coverage. 587 rows, 608 claims: js-philosophy 114 rows and 111 claims, pig-js-defaults 473 rows and 497 claims. The 608 claims are exactly the 608 `impl_pointers` (111 + 497), form `build/research/<slot>/result.md::<CLAIM-ID>`, slot read from `claims_index.md`.
- Grounded: constraints, 384 in all (71 + 313) = 349 `decision` rows (MUST or MUST NOT, or `MUST hold:` when the row is a statement or opens with a context clause) + 35 `acceptable-when` rows ("Acceptable only when <condition>: <practice>"). 28 claim-less rows: the folklore `rejected` ones are "Rejected beliefs" lines of `design_notes` with their row id, none is in `impl_pointers`; the claim-less `acceptable-when` rows are constraints without a pointer.
- Grounded: judge records, 192 keyed by node (three grouped records of the CONTRACTS branch, `ESCAPE.1 to .4`, `MODEL.1 to .3`, `SIGNATURE.2 to .4`, are copied onto each node of the group, marked "Shared record"); every defaults node holding a decision has one. The three integration notes are appended to the nodes they name. The skeleton has no judge records for philosophy nodes, so their `design_notes` hold rows, sources and rejected beliefs only.
- Grounded: skeleton fidelity. Every node's name, intent and epistemic state equals the skeleton (the escaped separator `\|` is written ` | `; none left), parents follow the uid, all 307 links match skeleton endpoints, type (as `shape.type`) and sentence; inter endpoints are `graph_id:node_uid` on both sides.
- Grounded: planned links absent. Neither graph names `web-app-philosophy` or `pig-web-defaults`.
- Grounded: public-repository hygiene. No absolute or home path and no private name in anything under `intent_graphs/` or `build/assemble/` (scripted scan, in `check_complete.py`).

Findings about the tool
- Grounded: `ig-tool node create` and `apply --batch` refuse `PIG-JS.SUBSET` under `PIG-JS.ROOT` ("Child node UID must start with parent prefix: expected 'PIG-JS.ROOT.<keyword-or-number>'"), and batch `node.reparent` runs the same check. The rule (`models/node.py::validate_uid_format`) lets a child of any root other than `ROOT` take only `<root>.<number>`, a keyword only below an L1 node whose parent is `ROOT`, and `PIG-<A>-<B>` only directly under `ROOT`.
- Grounded: the workaround stays small. `IntentGraph.attach(..., skip_uid_validation=True)`, the switch `lens apply` already uses for reparenting, lays the tree (`build/assemble/apply_tree.py`, 270 nodes); the history is stamped by the same save boundary as the CLI (`agent:assembler`). `ig-tool validate` accepts the result.
- Inferred: the Python defaults graph (`PIG-PY.*` under `PIG-PY.ROOT`, validates with 0 errors) predates the uid rule or was written by hand; I did not check its history.
- Grounded: batch `link.create` does not dispatch qualified endpoints ("Source node 'pig-js-defaults:PIG-JS.A' does not exist"); the CLI `ig-tool link create` does. The 113 inter links therefore go through the CLI, one call each.
- Grounded: `ig-tool validate -m` checks inter endpoints: a deliberately wrong target uid in a scratch copy gave 1 error naming it; the real graphs give 0.
- Recommendation: relax `validate_uid_format` for a root with a `PIG-<X>.ROOT` uid, or add a flag to `node create`, so projection graphs with the documented `PIG-<X>.*` scheme can be built by the CLI alone.

Open
- Open: the `MUST` sentences are mechanical. A verb-first row becomes `MUST <verb> ...` and a row opening with a context clause (In, When, With, After, A, The, ...) becomes `MUST hold: <row text>`; 64 of the 384 constraints are in the second form. A reviewer may prefer them rewritten.
- Open: `design_notes` also carries the `fact`, `deferred` and `rejected`-with-claims rows ("Fact [row; agreement]: ...", "Rejected [...]: ...", "Deferred [...]: ..."), a superset of what the brief lists; nothing the brief lists is missing. Drop them in `build_batches.py::node_content` if the notes should be shorter.
- Open: no independent review pass was run; nothing committed, nothing pushed.

## L3 full

### Files written

Under `intent_graphs/`:
- `js_philosophy.ig.yaml`: graph `js-philosophy`, product, root `ROOT`; 108 nodes (ROOT 1, L1 8, L2 40, L3 59), 48 intentlinks, 23 inter links.
- `js_defaults.ig.yaml`: graph `pig-js-defaults`, projection, root `PIG-JS.ROOT`; 270 nodes (root 1, L1 8, L2 43, L3 185, L4 33), 146 intentlinks, 90 inter links.
- `intent_resources.yaml`, `README.md`.

Under `build/assemble/`:
- `build_batches.py`: parses `build/distill/skeleton.md` and `claims_ledger.md`, writes `gen/`.
- `gen/`: `js_philosophy_batch.yaml` (node.create and link.create), `js_defaults_tree.json`, `js_defaults_batch.yaml` (node.set and link.create), `js_philosophy_inter.sh`, `js_defaults_inter.sh`, `planned_links.json`, `model.json`, `js_philosophy_root.json`.
- `apply_tree.py`: the one library step, with its reason in the docstring.
- `build_graphs.sh`: init, tree step, batch apply, inter links, for both graphs.
- `check_complete.py`: the completeness check; last run: `FAILS: 0`.

### Validate output (verbatim, both with `-m intent_graphs/intent_resources.yaml`)

```
graph: intent_graphs/js_philosophy.ig.yaml
nodes: 108
links: 48
inter_links: 23
issues: 0
errors: 0
warnings: 0

graph: intent_graphs/js_defaults.ig.yaml
nodes: 270
links: 146
inter_links: 90
issues: 0
errors: 0
warnings: 0
```

### Per branch (philosophy nodes / defaults nodes)

SUBSET 7 / 35, CONTRACTS 10 / 37, CONTROL 6 / 35, STRUCTURE 17 / 34, DEFENSE 21 / 58, DEPENDENCIES 23 / 28, VERIFICATION 17 / 22, RUNTIME 6 / 20, plus the two roots (108 = 1 + 107, 270 = 1 + 269).

### Completeness check, by script (`check_complete.py`)

Per graph, js-philosophy then pig-js-defaults: nodes 108 and 270; intentlinks 48 and 146; inter links 23 and 90; ledger rows 114 and 473; claims found in `impl_pointers` 111 and 497; constraints 71 and 313.

What it asserts, all holding:
- every skeleton node exists with equal name, intent and epistemic state, and a treearc to the parent given by its uid;
- every claim of every ledger row is an `impl_pointers` entry of the row's node, and the pointers of a node are exactly its claims (no extra, no dash entry);
- constraint count equals the node's `decision` plus `acceptable-when` rows, each opening `MUST` or `Acceptable only when`;
- every claim-less `rejected` row is a "Rejected beliefs" line carrying its row id;
- every defaults node with a decision row has a "Judge record" in its notes;
- the set of intentlinks (source, target, type, sentence) and of inter links equals the skeleton's;
- no planned boundary link was created; no absolute or home path in any file written.

### Skeleton elements not built

- 10 planned boundary links (`PIG-JS.DEFENSE.DOM.4`, `DEFENSE.ORIGIN.4`, `DEFENSE.ORIGIN.5`, `DEFENSE.INJECTION.6.1`, `DEFENSE.HOST.3`, `DEPENDENCIES.FRAMEWORK_SHORTLIST`, `DEPENDENCIES.FRAMEWORK_EVIDENCE.4`, `.5`, `CONTRACTS.BOUNDARY.1`, `PIG-JS.CONTROL.PROCESS.4`), because the web-architecture graphs do not exist; kept as a table in `intent_graphs/README.md`.
- The `examples` field: the skeleton has no examples column and the brief asks for one only where a concrete case is given; the cases that exist (for example the number list in the sort rule) are inside the constraint sentences.
- Nothing else: 378 of 378 nodes, 307 of 307 links, 608 of 608 claims.

### Decisions of form taken at assembly

- Link ids: ig-tool derives `SRC_DST`; no source and target pair occurs twice in either graph, so no `tag` was needed (0 tagged links). Inter link ids are `<graph>:<src>_<graph>:<dst>`, as in the Python defaults graph.
- Link type is stored as `shape: {type: requires|dataflow|refines|conflicts}`.
- `design_notes` order: judge record; rejected beliefs; rejected rows with claims; deferred rows; fact rows; the row list with roles and agreement; integration notes; sources cited (every `SRC-nnn` found in the node's rows and record).
- The graph meta name is the graph id (`js-philosophy`, `pig-js-defaults`) with a description; the manifest ids are the same.
- Philosophy root: `ig-tool init --root` with the skeleton's root name and intent, then `node.set` of its epistemic state.

### Tool behaviour found while building (details of the L2 findings)

- Observed error 1 (node create under `PIG-JS.ROOT`, and batch reparent): "Child node UID must start with parent prefix: expected 'PIG-JS.ROOT.<keyword-or-number>', got 'PIG-JS.A'".
- Observed: orphan nodes cannot stand in for a later attach, since batch reparent validates as create does; read in code (`serial/json_yaml.py`, not run): a saved graph with hierarchical uids and no treearc fails at save. So the tree has to be laid in one step with the check skipped.
- Observed: batch `node.reparent` takes `child:` and `under:` (the skill file's `uid:` form is rejected).
- Observed: batch `link.create` with a qualified endpoint; CLI `link create` with both endpoints qualified creates the inter link.
- Not checked: whether `obsidian export` of the two graphs works (no export folder was asked for in the brief and none was created).
