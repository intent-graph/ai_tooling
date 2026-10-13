# Patch brief: fold a gap-round slot into the built graphs

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`
unless stated. Your task message gives the absolute root and the slot to fold in.

## Why a patch, not a re-run

The stage-7 fixes edited the integrated files (`build/distill/skeleton.md`,
`build/distill/claims_ledger.md`, `build/distill/decisions_for_review.md`) directly. **Never run
`build/distill/5c_integrate/integrate.py`**: it rebuilds those files from the branch folders and
would silently undo the review fixes. The integrated files are now the source of truth; the
branch folders are history.

## Read first

- `build/distill/brief_distill.md`, section **Shared** (rules, ledger format, epistemic states,
  the max rule) and **Step 5b** (what a node, a judge record and a decision look like).
- `build/distill/target_hierarchy.md` (tree, max rule, judge record).
- `build/review/fixes/result.md`, `## L2 claims` (the conventions the fixes introduced:
  `unvalidated` flags, rules-only constraints, bookkeeping in `build/assemble/bookkeeping_log.md`)
  and `build/assemble/result.md`, `## L2 claims` (how the graphs are built and checked).
- The slot's claim table: `build/research/<slot>/result.md`, all levels.
- The nodes you touch, read through `ig-tool query -g intent_graphs/js_defaults.ig.yaml --node
  <UID>` (and the philosophy graph), and their rows in `skeleton.md` and `claims_ledger.md`.

## What to do

1. **Place every claim of the slot exactly once** in `claims_ledger.md` (ledger format of the
   brief), on the node that owns it: an existing node, a node the slot resolves (an `undecided`
   node becomes decided when the slot grounds a position), or a new node. New nodes follow the
   UID rules, two to six children per parent; add them to `skeleton.md` with intent, epistemic
   state and ledger rows, and a judge record when they hold a decision.
2. **Decide by the max rule** and record each new decision, and each undecided node now decided,
   in `decisions_for_review.md` under a new section named after the slot.
3. **Keep the fix conventions**: constraints are rules only; facts go to design notes;
   single-source, inferred or open grounds carry `unvalidated: <why>`; no bookkeeping in
   engineer-facing fields; JavaScript and tool names stay out of the philosophy graph.
4. **Links**: add intentlinks the new nodes need (inside and across branches, and to
   `js-philosophy`), in the skeleton's link tables.
5. **Rebuild and gate**, from the root: `python3 build/assemble/apply_flags.py`,
   `python3 build/assemble/build_batches.py`, `zsh build/assemble/build_graphs.sh`,
   `python3 build/assemble/check_complete.py` (0 failures), `python3 build/distill/check_ledger.py`
   (0 errors), and `ig-tool validate -g <graph> -m intent_graphs/intent_resources.yaml` for both
   graphs (0 errors).
6. **README**: update counts in `intent_graphs/README.md` and remove from "Not covered" what the
   slot now covers; keep what it does not.

## Result file

Write `build/patch/<slot>/result.md` with `## L1 headline`, `## L2 claims`, `## L3 full`, each
readable alone, items marked grounded, inferred or open. Pin, word for word at every level:
claims placed (0 dropped); nodes added and nodes resolved from undecided; decisions added;
validate summaries of both graphs; the outputs of `check_ledger.py` and `check_complete.py`;
what remains under "Not covered".

Write only `build/distill/` (the three integrated files), `build/assemble/` (logs, if needed),
`intent_graphs/` (rebuilt graphs and README) and `build/patch/<slot>/`. Public repository: no
absolute or home paths, no private names. Never commit, never `git push`.
