# Build brief — shared by every graph-writing unit

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/web_architecture_guidelines/`.

## What you build

One `ig-tool` batch file that creates every node of your unit in one of the two graphs, plus
the intentlinks whose two endpoints are both inside your unit. You do not apply it to the real
graph: the coordinator applies all batches in order, then a linker adds cross-unit and
cross-graph links.

- `intent_graphs/web_app_philosophy.ig.yaml` — graph id `web-app-philosophy`, root uid `ROOT`.
- `intent_graphs/web_defaults.ig.yaml` — graph id `pig-web-defaults`, root uid `PIG-WEB.ROOT`.
- Both currently hold only their root. Your unit's L1 node is created by your batch, with the
  root as parent.

## Sources of truth, in order

1. `build/distill/maintainer_decisions.md` — MD-01 to MD-03 override everything.
2. The final judge records of your unit (`build/distill/03_judge/<unit>/records.md`): the
   verdicts are final. Do not re-judge; transcribe faithfully into node fields.
3. `build/distill/02_skeleton/skeleton.md` — uids, names, tree position, owned ledger rows,
   intentlinks. Use its uids and names unchanged (names must not contain `/ \ : * ? " < > | [ ] # ^`).
4. `build/distill/02_skeleton/claims_ledger.md` — the `merges` column maps each ledger row to
   its original research claims, for traceability.

## Field mapping (one node.create per node, breadth-first order)

- `name` — skeleton name.
- `intent` — the decided practice, stated as what holds and why, in one to three sentences;
  self-sufficient (readable without children); roll-ups summarize their children. Philosophy
  nodes stay stack-neutral (no product names); PIG-WEB nodes name the stack choice.
- `epistemic_state` — the judge's proposed state, verbatim, including pipe annotations
  (`known`, `undecided: awaiting maintainer, ...`, `deferred: ...`, `speculative`, etc.).
- `constraints` — the verdict's MUST rules, one per line. For placement nodes: `Authority: ...`,
  `Copies: ...` (with purpose), `Forbidden: ...`, plus the decided rules.
- `design_notes` — the judge record, compressed but complete: positions considered (with
  ledger ids), forces, grounds of the decision, each rejected option with "acceptable when"
  or the condition under which it wins, maintainer decisions cited (MD-0n), tensions
  recorded, evidence gaps. For a placement, also "Would move it: ...".
- `examples` — only if the record gives concrete examples.
- `impl_pointers` — traceability, one pointer per entry:
  - the judge record: `build/distill/03_judge/<unit>/records.md::<UID>`;
  - each original research claim behind the node's owned and cited ledger rows:
    `build/research/<slot>/result.md::<CLAIM-ID>` (slot folder from the claim prefix; the
    collaboration slot's claims are written `C01` in its file and `COLLAB-C01` in the ledger:
    use `build/research/20_collaboration/result.md::C01`).
- Do not set `history`; provenance is automatic.

## Batch format and check

The batch format is documented only in
`../../../intent_graph/.claude/skills/ig-tool-graph-edit/SKILL.md`, section
"apply --batch — Atomic Multi-Operation": read it before writing. Ops are `node.create`,
`link.create` (dot notation).

Check your batch before returning, without touching the real graph:

```bash
cp intent_graphs/<graph file> <your slot>/scratch.ig.yaml
ig-tool apply -g <your slot>/scratch.ig.yaml --batch <your batch> -o <your slot>/scratch.ig.yaml --role builder -m "dry build <unit>"
ig-tool validate -g <your slot>/scratch.ig.yaml
```

The check must pass with 0 errors. Delete `scratch.ig.yaml` afterwards.

## Rules

- Public repository: no absolute or home paths, no private names, in anything written.
- Never edit the real graph files, the judge records, the skeleton or the ledger. Never commit
  or git push.
