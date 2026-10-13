# Distillation brief: stage 5 (consolidate), in three steps

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`
unless stated. Your task message gives the absolute root and your step (5a, 5b with a branch,
or 5c). Read **Shared** and your step's section.

## Shared

### Read first

- `build/plan.md`: **Goal**, **Boundary with sibling guidelines**, **Source admission policy**,
  **Claim format**, **Target IntentGraphs**, **Maintainer decisions**.
- `build/distill/target_hierarchy.md`, all of it: the functional hierarchy, the **max**
  selection rule and the judge record. Maintainer decisions; do not reopen them. The maintainer's
  words: "I dont want you to bring me the internet average, aka avg(all sources). I want you to
  do max(all sources). It's ok to make choices and pick the best."
- IntentGraph rules (step 5b and 5c): `../../../intent_graph/agents/compressed/PRIMER_00_PHILOSOPHY.md`,
  `PRIMER_01_SEMANTICS.md` and `PRIMER_03A_EDITING.md` in the same folder: P2, P4 (language-swap
  test), P5 (no duplication across peers), UID format, node-name character safety
  (`/\:*?"<>|[]#^` forbidden in names).

### Rules

- **The tree is given.** L1 = the eight branches, same keywords in both graphs: `SUBSET`,
  `CONTRACTS`, `CONTROL`, `STRUCTURE`, `DEFENSE`, `DEPENDENCIES`, `VERIFICATION`, `RUNTIME`.
  Below L1, partition by the branch's purpose and the evidence, two to six children per node.
- **UIDs.** `js-philosophy`: root `ROOT`, L1 the keywords, L2 `<L1>.<KEYWORD>` or `<L1>.<n>`,
  L3 and deeper numeric only. `pig-js-defaults`: the same with the `PIG-JS.` prefix
  (`PIG-JS.ROOT`, `PIG-JS.DEFENSE`, `PIG-JS.DEFENSE.DOM`, `PIG-JS.DEFENSE.DOM.1`).
- **Language-swap test.** A statement that still holds with another language in place of
  JavaScript belongs to `js-philosophy`; otherwise to `pig-js-defaults`. Principles shared with
  any language become inter links to `python-kb-philosophy`
  (`../python_guidelines/intent_graphs/python_kb_philosophy.yaml`, read its uids), not copies.
- **Max, grounded.** Each decision is the most demanding practice that serves its branch's
  purpose **and that an admitted source supports**. The build decides contested topics itself,
  the type-layer choice and the framework short list included. Never invent a practice: a gap
  stays `undecided | missing: no admitted source` or a note on the nearest node. A missing
  independent ranking is **not** a reason to leave a node undecided: when admitted sources state
  positions or facts about the options (tool documentation included), choose among them against
  the branch's purpose and record the judge record.
- **Epistemic state.** Decision on one T1 or two independent T2 grounds: `known`. On one T2:
  `known | unvalidated: single T2 source`. On T3 alone (the plan: T3 alone never makes a node
  `known`): `risky | unvalidated: single T3 source`. A contested topic decided by the max rule:
  `known | conflict: <rejected position, holder>`. Only tool-extracted quotes on the only T1
  ground: add `| unvalidated: quote tool-extracted`. No admitted source: `undecided | missing:
  no admitted source`. Out of scope: `deferred`.
- **Restrictions.** Check every claim resting on a restricted source against its restriction in
  `build/audit/source_register.md` (scoped per slot when the row says so). A use that oversteps
  is demoted (style-guide position becomes `acceptable-when` or `rejected` evidence; vendor fact
  becomes `fact` only) and listed.
- **Folklore.** Every belief `12_dissent` refutes becomes a `rejected` row on the node it
  concerns, so the guideline states what not to believe and why.
- Public repository: no absolute or home paths, no private names. Never commit, never
  `git push`.

### Ledger format (steps 5b and 5c)

`| row | claim_ids | node | graph | statement | agreement | role |`, one row per line, `|`
never inside a cell. `row`: `<BRANCH>-<nnn>`. `claim_ids`: ids separated by `, `. `graph`:
`js-philosophy` or `pig-js-defaults`. `role`: `decision` (the max choice of its node),
`acceptable-when` (weaker practice and its condition), `rejected` (position or belief the node
rejects), `fact` (mechanism a decision rests on), `deferred` (out of scope or owned by a
sibling guideline). **Every claim routed to a branch is placed exactly once in its ledger.**

### Result files

Every step writes a `result.md` in its folder with `## L1 headline` (one sentence and its
certainty, then `Pinned:`), `## L2 claims` (one line per finding, marked grounded, inferred or
open), `## L3 full`, each readable alone.

## Step 5a: route

Read `build/distill/claims_index.md` (all 608 claims, compact), `build/research/11_coverage/result.md`
(overlaps and boundary items, all levels) and `build/research/12_dissent/result.md` (`## L2 claims`).

Write `build/distill/routing.md` with the table `| claim_id | branch | group | note |`, one row per
claim, every claim exactly once:
- `branch`: one of the eight keywords, by the target hierarchy's description of each branch,
  not by the slot the claim came from (slot 09 splits between CONTROL and RUNTIME, slot 04
  between STRUCTURE and CONTRACTS, slot 13 is mostly DEFENSE).
- `group`: a short label shared by claims that state the same fact or answer the same question
  (the 19 overlap clusters of `11_coverage` among them), so the branch agent merges them; `-`
  otherwise. A group never spans two branches.
- `note`: `boundary: web-architecture` for claims `11_coverage` says the sibling should hold, or
  `-`.

Then run `python3 build/distill/claims_index.py split` from the root and fix every ERROR until
it reports none; it writes `build/distill/branches/<BRANCH>/claims.md`. Result in
`build/distill/5a_route/result.md`; pin claims routed per branch and the number of groups.

## Step 5b: one branch

Your task message names the branch. Read `build/distill/branches/<BRANCH>/claims.md` (your
claims, full rows), the parts of `12_dissent` and `11_coverage` that concern your branch, and
the register rows your claims cite. Write in `build/distill/branches/<BRANCH>/`:

1. `ledger.md`: your claims in the ledger format, each placed once.
2. `skeleton.md`: your subtree in both graphs: node tables `| uid | name | intent |
   epistemic_state | ledger rows |`, the L1 node first (philosophy `<BRANCH>`, defaults
   `PIG-JS.<BRANCH>`), breadth-first; intentlinks inside your branch
   `| # | from | to | type | sentence |`; proposed links to other branches (by branch keyword,
   the integrator resolves them); inter links to `python-kb-philosophy` uids. Then one **judge
   record** per defaults node holding a decision.
3. `decisions.md`: every decision that settled a contested topic or a weighty choice, or rests
   on a single source: the decision, rejected positions with the condition under which each
   would win, the grounds. Then your `undecided` nodes, each with the evidence that would settle
   it.
4. `result.md`: pin claims in and ledger rows out (0 dropped), node counts per graph and level,
   decisions for review, undecided nodes, restriction demotions.

Write only in your branch folder.

## Step 5c: integrate

Read every `build/distill/branches/*/result.md` (`## L2 claims`), then the branch files as
needed. Write in `build/distill/`:
- `claims_ledger.md`: all branch ledgers in branch order, under one ledger header.
- `skeleton.md`: both graphs, root nodes first (`ROOT` and `PIG-JS.ROOT`, intents from the
  target hierarchy's L0), then the eight branch subtrees; all intentlinks with cross-branch
  proposals resolved to uids; inter links; planned boundary links to the web-architecture graphs
  listed as planned, not created; the judge records.
- `decisions_for_review.md`: the branch decisions merged, batched by branch, then the undecided
  nodes.
- Normalize across branches: two branches stating one principle (P5) are merged into one node
  and linked from the other.
- Re-label every node whose decision rests on T3 alone from `known | unvalidated: single T3
  source` to `risky | unvalidated: single T3 source` (branches written before this rule).
- Run `python3 build/distill/check_ledger.py` from the root and fix every ERROR.
- `result.md` in `build/distill/5c_integrate/`; pin claims in and ledger rows out (placed,
  merged, dropped: 0 dropped), node counts per graph and level, decisions for review, undecided
  nodes, restriction demotions, the checker's output.

Write only in `build/distill/`.
