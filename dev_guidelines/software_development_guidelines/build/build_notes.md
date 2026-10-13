# Build notes — what this run changed in the procedure

This guideline was built with the procedure of
[../../web_architecture_guidelines/build/RECIPE.md](../../web_architecture_guidelines/build/RECIPE.md).
These notes record what differed and what to do next time. Decisions of the maintainer are in
[distill/maintainer_decisions.md](distill/maintainer_decisions.md).

## Pipeline as run
<!-- Lines 10-21 -->

1. Research: 15 slots in three rounds (`research/01` to `15`), plus a coverage check (`08`).
2. Consolidation: one ledger in three parts (research; round 3 with the web guideline's generic
   evidence; the JavaScript guideline's language-general principles), 814 rows, checked by script.
3. Hierarchy fixed with the maintainer before any judging (`distill/target_hierarchy.md`).
4. Skeleton in two passes: one agent cut L2 and routed every row; one agent per branch cut L3 and
   listed positions; one agent resolved the routing objections.
5. Judging in two waves (decision branches first), each unit reviewed adversarially, clear fixes
   applied by the judge, subtle points settled by one Opus final pass.
6. Roll-up of ROOT and the L1 nodes, then one graph batch per unit, a linker, a critic, a second
   Opus pass on the critic's subtle points, and the render.

## Lessons
<!-- Lines 24-48 -->

- **"Max" means best, not most demanding.** The maintainer corrected the wording; the rule is to
  not default to the average of sources. State it this way in every brief.
- **No default team.** Judging against principles and outcomes, with context only where the best
  practice differs, removed the default-context question that cost the web run a re-judge.
- **Cut the skeleton in two passes.** Routing 800 rows to L2 in one agent, then refining each
  branch in parallel, scaled where a single skeleton agent would have truncated.
- **Sonnet for the bulk, Opus for the flags.** Reviewers sort findings into `fix` (applied by
  the judge) and `flag` (one Opus pass over all units); about 0.75M of the run's roughly 12M agent
  tokens were Opus.
- **Check every path in a shared brief resolves** from the folder the brief says it is relative
  to; one wrong prefix left three research slots without the decided hierarchy.
- **Give every agent its own scratch folder.** Agents sharing the session scratchpad overwrote
  each other's helper files; validation catches malformed batches, not misplaced content, so
  check that each node points to its own unit's record.
- **Check the top of the tree after the build.** The L1 batch writer copied the scope
  descriptions instead of the roll-up decisions; a scan for lowercase or short intents caught it.
- **Fix node names and link types before the build, not after.** Name the link types in the
  writer brief (realizes, requires, refines, constrains, dataflow, conflicts) and forbid
  `/ \ : * ? " < > | [ ] # ^` in names; loose "see" links had to be retyped or dropped.
- **Repair cross-file links after a parallel render.** Branch files split independently, so
  links guessed before the split break;
  [distill/07_render/check_links.py](distill/07_render/check_links.py) repoints each to the one
  file holding its anchor.

## Known residue
<!-- Lines 51-55 -->

- `construction.md` is slightly over the 500-line ceiling; a split would move anchors that other
  files link to.
- 41 open items (cadences and thresholds no source gives, one-source minority views) are kept as
  gaps in their nodes; the rendered files show those that change what a reader does.
