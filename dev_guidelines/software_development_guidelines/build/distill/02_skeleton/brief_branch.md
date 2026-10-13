# Branch brief — shared by the seven branch agents

Paths are relative to `build/distill/` in the guideline folder; your task message gives the
absolute root and your L1 branch.

## Goal

Refine one L1 branch of the skeleton below its L2 nodes: cut L3 where a node holds several
decisions, attach every row routed to your branch to exactly one node, and list the competing
positions per node **without any verdict**, so judges can then decide node by node.

## Read

- `target_hierarchy.md` and `maintainer_decisions.md`: the decided rules. They bind; cite MD
  numbers.
- `02_skeleton/tree_l2.md`: the L1 and L2 tree, each node's intent, and the table of split
  topics (which node holds the content, which is the index).
- `02_skeleton/routing.md`: which rows are routed to your L2 nodes (your rows, only those).
- The rows themselves, in full (statement and positions): `01_consolidate/claims_ledger.md`
  (L001-L460), `01_consolidate/part2/claims_ledger_part2.md` (L1001-L1289),
  `01_consolidate/part3/claims_ledger_part3.md` (L1501-L1565).
- Format model only: `02_skeleton/superseded_provisional/skeleton.md`, one node record (any
  OWNERSHIP node) to see the record layout.
- UID rules: `intent_graph/agents/compressed/PRIMER_01_SEMANTICS.md`, section "UID Format
  Convention", in the sibling public repository (path given in your task message).

## Rules

- Keep the L2 nodes as `tree_l2.md` names them. If a row clearly belongs to another branch, do
  not move it: list it under "Routing objections" with the node you would route it to.
- Cut L3 top-down from the L2 node's intent, then attach rows. L3 uids are `<L2 uid>.<n>`.
  Typically two to six children per node; none where the node is one decision.
- **One location per fact (MD-03).** On an index node (per the split-topics table), write a
  one-line intent and links to the content node; attach only rows that do not restate the
  content node.
- **No default team (MD-02).** Add a context variable to a node only where a row itself says
  the best practice moves with it, quoting the row id.
- Per node record: uid, name, one-line intent (what and why, never how; no tool names),
  attached row ids, positions (each competing practice, its strongest argument, the force it
  serves, the condition under which it would be the best, with row and source ids), context
  variables (only as above), links to other nodes (`Realizes <uid>` for realization branches to
  decision nodes; `Requires`, `Conflicts`, `Refines` where a row states it), stack pointers for
  rows tagged with a stack.
- Rows marked `origin: judged in the JavaScript guideline` keep their prior verdict as one
  position among others, never as the decision.
- Every MAINT row (maintainer's codified practice, source MAINT-S01, not citable) appears as a
  named position on its node.
- No verdict, no ranking, no merging or editing of ledger rows.

## Output

In `02_skeleton/branches/<BRANCH>/` (your branch's L1 uid):

- `branch.md`: the branch tree (uids and names) at the top, then one record per node.
- `check_branch.py`: proves every row routed to your branch is attached to exactly one of your
  nodes, every uid follows the rules, every link target exists in `tree_l2.md` or your branch.
- `result.md` with `## L1 headline`, `## L2 claims`, `## L3 full`, each readable alone, each
  claim marked grounded / inferred / open. Pin, word for word at every level: node count, rows
  attached and unattached (must be 0), the script's pass/fail line, the number of routing
  objections.

Public repository: no absolute or home paths, no private names. Write only in your branch
folder. Never commit or push.
