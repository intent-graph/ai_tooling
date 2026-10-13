# CLAUDE.md: JavaScript Guidelines

Read [README.md](README.md) first. Then:

- **The graphs are the guideline.** `intent_graphs/js_defaults.ig.yaml` (rules) and
  `intent_graphs/js_philosophy.ig.yaml` (principles). Never read a graph file whole: use
  `ig-tool tree --show-intent` and `ig-tool query --node <UID>`. IntentGraph rules:
  `../../../intent_graph/CLAUDE.md`.
- **Answering a JavaScript question**: find the branch, query the node, cite its constraints and
  its epistemic state; an `unvalidated:` flag or an `undecided` node must be passed on, not hidden.
- **Changing the guideline**: edit the integrated files in `build/distill/` (`skeleton.md`,
  `claims_ledger.md`, `decisions_for_review.md`), then rebuild and gate as
  `build/patch/brief_patch.md` step 5 says. Never run `build/distill/5c_integrate/integrate.py`:
  it rebuilds from the branch folders and would undo the review fixes (it refuses without a flag).
- **New evidence** goes through the same gates: discover, audit by another agent, extract, then
  patch (`build/discover/brief_discover.md`, `build/audit/brief_audit.md`,
  `build/research/brief_extract.md`). Only sources in `build/audit/source_register.md` may be cited.
- **The Obsidian vault** is generated: `intent_graphs/export_to_obsidian.sh`; never edit it by hand.
- Public repository: no absolute or home paths, no private names. Never `git push`.
