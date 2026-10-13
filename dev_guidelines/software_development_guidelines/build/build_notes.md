# Build notes — what this run changed in the procedure

This guideline was built with the procedure of
[../../web_architecture_guidelines/build/RECIPE.md](../../web_architecture_guidelines/build/RECIPE.md).
These notes record what differed and what to do next time. Decisions of the maintainer are in
[distill/maintainer_decisions.md](distill/maintainer_decisions.md). The `build/` folder publishes
the research results drawn from public sources and their shared brief (13 slots and the coverage
check, `research/`), the target hierarchy, the maintainer decisions, the two input notes from the
sibling guidelines and the link checker (`distill/`), and these notes. The artifacts of the other
stages are not published: any research drawn from a private source, the consolidation, skeleton,
judging and review records, and the build and critique stages. The list below describes all
stages as a method.

## Pipeline as run
<!-- Lines 16-29 -->

1. Research: 14 slots in three rounds, numbered `01` to `15` (`08` is the coverage check). The
   result of the slot drawn from a private source is not published, so the published results are
   the other 13 slots and the coverage check.
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
<!-- Lines 32-63 -->

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
- **Only rules cross from a private setting, restated without attribution.** A rule
  ("soft delete is the default for user-facing data") may be recorded; a statement that the private system
  is in some state (what exists, what is missing, how many, what is broken or done today) may not,
  and neither may a marker that the guideline agrees with or differs from that setting. Keep the
  lesson as a rule or a synthetic example and drop the state; where the rule's only support is
  that setting, its provenance reads "a single practitioner source (not citable)" or "(inferred)".
  Check every brief and result for these before publishing.

## Known residue
<!-- Lines 66-70 -->

- `construction.md` is slightly over the 500-line ceiling; a split would move anchors that other
  files link to.
- 41 open items (cadences and thresholds no source gives, one-source minority views) are kept as
  gaps in their nodes; the rendered files show those that change what a reader does.
