# TOP batch result: ROOT update and seven L1 nodes

## L1 headline

`batch.yaml` holds 8 operations: 1 `node.set` on the existing ROOT, 7 `node.create` for OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE (children of ROOT, in that order). Dry run on a scratch copy of the real graph: 8 operations succeeded, validate 0 errors, 0 warnings. Scratch copy deleted; real graph untouched.

Pinned:
- Nodes created: 7 (OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE).
- Node updated: 1 (ROOT, via `node.set`: intent, epistemic_state, design_notes, constraints, impl_pointers; name kept).
- Dry-run validate: `nodes: 8, links: 0, errors: 0, warnings: 0`.

## L2 claims

- Source: `build/distill/03_judge/rollup/judged.md`, one record per node, transcribed without re-judging (grounded: verdicts are final).
- Field mapping (grounded, per `brief_build.md`):
  - `intent` = the record's Intent line.
  - `constraints` = the Constraints line split on semicolons, one MUST rule per entry.
  - `design_notes` = fields 1 to 7 (Decision, Grounds, Positions, Rejected, Context, Certainty, Flags) plus the Links line, verbatim.
  - `impl_pointers` = one entry, `build/distill/03_judge/rollup/judged.md::<UID>`.
  - `history` not set.
  - No `examples` (records give none).
- `epistemic_state` per node (all roll-ups carry their own certainty):
  - ROOT: inferred as one claim; order and split grounded in MD-01 to MD-05; 41 open items kept at L2/L3. Marked inferred.
  - OWNERSHIP: inferred roll-up; open at 4 nodes. Marked inferred.
  - ASSURANCE: inferred roll-up; open at 8 places; carries `| unvalidated: awaiting maintainer` for the RULES.4 independent-automated-reviewer question (default applied). Marked inferred, with an unvalidated annotation.
  - CONSTRUCTION: inferred; open at 4 nodes. Marked inferred.
  - CHANGE_FLOW: inferred; open at 6 nodes. Marked inferred.
  - OPERATION: inferred; open at 9 nodes. Marked inferred.
  - EVOLUTION: inferred; open at INCREMENTAL.3; carries `| unvalidated` for the contested TECHNOLOGY.4 row (judge flag, no final-pass resolution). Marked inferred, with an unvalidated annotation.
  - TRANSVERSE: inferred; open at 8 nodes. Marked inferred.
- Decision: no node is marked undecided (grounded: the record says none).
- Inferred (mine): the epistemic_state strings are composed from each record's Certainty and Flags fields, since the records give prose, not a state keyword.
- Public-repo check: no absolute or home paths in `batch.yaml` (grep: 0 hits).
- Cross-unit links: none in this batch. The Links lines of the records (realizes, related) go to the linker as design_notes text only; I did not create links, as the brief scopes links to L2 batches and writes `cross_links.md` only for those units. Open: if the linker expects these L1-level links from TOP, say so.

## L3 full

Operations in `batch.yaml` (order = application order):

| # | op | uid | parent | constraints |
|---|----|-----|--------|-------------|
| 0 | node.set | ROOT | existing | 4 |
| 1 | node.create | OWNERSHIP | ROOT | 3 |
| 2 | node.create | ASSURANCE | ROOT | 4 |
| 3 | node.create | CONSTRUCTION | ROOT | 4 |
| 4 | node.create | CHANGE_FLOW | ROOT | 4 |
| 5 | node.create | OPERATION | ROOT | 4 |
| 6 | node.create | EVOLUTION | ROOT | 4 |
| 7 | node.create | TRANSVERSE | ROOT | 4 |

Names match `02_skeleton/tree_l2.md` and the records exactly; none contains a forbidden character.

Dry-run commands run (from the guideline root, scratch in this slot, deleted afterwards):
1. `cp intent_graphs/software_development_philosophy.ig.yaml <slot>/scratch.ig.yaml`
2. `ig-tool apply -g <scratch> --batch <slot>/batch.yaml -o <scratch> --role builder -m "dry build TOP"`: status success, 8 operations, ROOT fields set: intent, epistemic_state, design_notes, constraints, impl_pointers; issues 0, errors 0, warnings 0.
3. `ig-tool validate -g <scratch>`: status ok, nodes 8, links 0, errors 0, warnings 0.

Notes:
- The ROOT placeholder intent is replaced by the record's Intent; the intent text keeps the record's lower-case opening.
- Stack-neutral intents: grounds naming published frameworks (e.g. in TRANSVERSE) sit in `design_notes`, as the brief directs.
- Open items (41) are not duplicated here; they stay in each record's Certainty field inside design_notes and in the L2/L3 nodes' own units.
