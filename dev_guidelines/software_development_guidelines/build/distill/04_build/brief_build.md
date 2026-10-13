# Build brief — shared by every graph-writing unit

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/software_development_guidelines/`;
your task message gives the absolute root and your unit.

## What you build

One `ig-tool` batch file that creates every node of your unit in the guideline's single graph,
plus the intentlinks whose two endpoints are both inside your unit. You do not apply it to the
real graph: the coordinator applies all batches in order, then a linker adds cross-unit links.

- `intent_graphs/software_development_philosophy.ig.yaml`: graph id
  `software-development-philosophy`, root uid `ROOT`. It holds only its root.
- **Your batch starts at your unit's L2 nodes.** The seven L1 nodes and the ROOT update are a
  separate batch (`04_build/TOP/`), built from `03_judge/rollup/judged.md` and applied first.
  Skip any L1 record your `judged.md` holds.

## Sources of truth, in order

1. `build/distill/maintainer_decisions.md`: MD-01 to MD-07 override everything.
2. `build/distill/03_judge/final_pass/resolutions.md` (your unit's section) and
   `build/distill/03_judge/cross_unit_fixes.md`: they override the judge record where they
   change it. A point marked for the maintainer keeps the judge's decision, with
   `epistemic_state` annotated `| unvalidated: awaiting maintainer, <one-line question>`.
3. The final judge records of your unit, `build/distill/03_judge/<unit>/judged.md` (including
   its "Review applied" section): the verdicts are final. Do not re-judge; transcribe
   faithfully into node fields.
4. `build/distill/02_skeleton/branches/<BRANCH>/branch.md`: uids, names, tree position, attached
   ledger rows, links. Use its uids and names unchanged (names must not contain
   `/ \ : * ? " < > | [ ] # ^`).
5. The three ledger parts under `build/distill/01_consolidate/` (`claims_ledger.md`,
   `part2/claims_ledger_part2.md`, `part3/claims_ledger_part3.md`): the `merges` column maps each
   ledger row to its original claims, for traceability.

## Field mapping (one node.create per node, breadth-first order)

- `name`: the skeleton name.
- `intent`: the decided practice, stated as what holds and why, in one to three sentences;
  self-sufficient (readable without children); a parent summarizes its children. Stack-neutral:
  no product, tool or language names (those go to `design_notes`).
- `epistemic_state`: from the record's certainty: `known` (grounded), `inferred: <why>`,
  `undecided: <the question>` (only the node marked undecided), plus pipe annotations for open
  parts (`| gap: ...`, `| unvalidated: ...`).
- `constraints`: the decision's MUST rules, one per entry.
- `design_notes`: the judge record, compressed but complete: positions considered (ledger ids),
  forces, grounds, each rejected position with the condition under which it would be the best,
  context conditions, maintainer decisions cited (MD-0n), where the maintainer's codified
  practice won or lost and why, evidence gaps. On an index node (MD-03): only the pointer.
- `examples`: only if the record gives concrete examples.
- `impl_pointers`: traceability, one pointer per entry:
  - the judge record: `build/distill/03_judge/<unit>/judged.md::<UID>`;
  - each original research claim behind the node's attached ledger rows:
    `build/research/<slot>/result.md::<CLAIM-ID>`, slot folder from the claim prefix (SRC 01,
    ADOPT 02, VERIFY 03, DELIVER 04, OPERATE 05, TRANS 06, MAINT 07, EXT 09, DATA 10, PERF 11,
    EVOL 12, AUTH 13, RECOV 14, SECD 15);
  - web guideline claims (prefix `WEB:`):
    `../web_architecture_guidelines/build/research/<slot>/result.md::<ID>`, slot as recorded in
    `01_consolidate/part2/claims_ledger_part2.md`;
  - JavaScript guideline principles (prefix `JS:`):
    `../javascript_guidelines/build/handoff/to_software_guideline/package.md::<JS node uid>`.
- Do not set `history`; provenance is automatic.

## Batch format and check

The batch format is documented only in
`../../../intent_graph/.claude/skills/ig-tool-graph-edit/SKILL.md` (path relative to this
guideline folder; it is in the sibling public `intent_graph` repository), section
"apply --batch — Atomic Multi-Operation": read it before writing. Ops are `node.create`,
`link.create` (dot notation).

Check your batch before returning, without touching the real graph:

```bash
cp intent_graphs/software_development_philosophy.ig.yaml <your slot>/scratch.ig.yaml
ig-tool apply -g <your slot>/scratch.ig.yaml --batch <your batch> -o <your slot>/scratch.ig.yaml --role builder -m "dry build <unit>"
ig-tool validate -g <your slot>/scratch.ig.yaml
```

First add a placeholder node for your L1 branch (uid = the branch, parent `ROOT`) to the scratch
copy only, with `ig-tool node create`. The check must pass with 0 errors. Delete
`scratch.ig.yaml` afterwards.

Links whose other endpoint is outside your unit are not in your batch: list them in
`<your slot>/cross_links.md` (source uid, target uid, link type, one-line intent sentence) for the
linker. Your slot is `build/distill/04_build/<unit>/`; your batch is `<your slot>/batch.yaml`.

## Rules

- Public repository: no absolute or home paths, no private names, in anything written.
- Never edit the real graph file, the judge records, the skeleton or the ledger. Never commit or
  push.
