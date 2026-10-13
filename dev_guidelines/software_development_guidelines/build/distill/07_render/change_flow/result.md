# Render result: CHANGE_FLOW

## L1 headline

CHANGE_FLOW is rendered in full: 43 of 43 nodes (1 L1, 8 L2, 34 L3) in four files, 617 lines in total, split by the 500-line rule (the single draft came to 496 lines before tables of contents and line comments, so it would have exceeded 500). `change_flow.md` is the thesis and index (49 lines); the three body files are `change_flow_integration_review.md` (157), `change_flow_delivery.md` (226) and `change_flow_data_and_measure.md` (185). md-structure-sync ran on all four and succeeded. The one open maintainer point (can an automated reviewer be the independent check) is shown inline in three places with its default applied.

Heads-up: because of the split, L3 anchors now live in the body files, not in `change_flow.md`. Sibling files that link `change_flow.md#<l3-slug>` will not resolve; they must link the body file (L2 and L3 slugs are the node-name slugs).

## L2 claims

- Files and lines (grounded, measured): `change_flow.md` 49; `change_flow_integration_review.md` 157 (Version Control and Integration, Review); `change_flow_delivery.md` 226 (Build and Pipeline, Release, Deployment, Rollback); `change_flow_data_and_measure.md` 185 (Data and Schema Change, Measuring Delivery). All under 300 lines.
- Coverage (grounded): every node's uid appears once as a backtick tag (43 tags counted); each L3 shows decided practice, MUST rules from `constraints` and "Best instead when" lines from the rejected-with-condition records.
- Open maintainer point (grounded): "can an automated reviewer be the independent check (ASSURANCE.RULES.4)" is shown at the Review section, Mechanism and Depth by Risk, and Automated and Second-Reviewer Layers; default applied: it may add a layer but never approves.
- Other inline "Open" lines (grounded as to what the graph records): repository layout winner, merge-method ranking, no-disclosure ruling, accuracy of an automated second reviewer, calendar versioning, concurrent-control rule, pull versus push reconcile, rollback decision rule, DATA_CHANGE single-source items, contested net effect of automation.
- Format (grounded): relative links only, link checker over all four files found 0 unresolved anchors; one Mermaid diagram (in `change_flow.md`); no dates, versions, absolute paths, ledger/register ids or `Lnnn` source ids (grep clean). Stack-neutral.
- Cross-file anchors to sibling files (inferred): links such as `assurance.md#independent-review-that-binds` assume sibling headings are the exact node names; I took the names from the graph but could not verify the siblings' files, which are written in parallel.
- Index nodes: the branch has none; no index-line rendering was needed (grounded, tree inspected).
- Judgement calls (inferred): a few `design_notes` rows (for example the unmerged release approval, DEPLOY.2 strategy list) were condensed into one "Best instead when" line each; position numbers P1.. were not cited. Two cross-links name a sibling section generically (behaviour section of `assurance.md`; the operation and construction files) where I did not have a confirmed anchor.

## L3 full

Files (all in `ai_tooling/dev_guidelines/software_development_guidelines/`):
- `change_flow.md` (49 lines): L1 thesis, four branch rules, certainty line, split note and index of the three body files, Map section (one Mermaid flowchart and a table linking the eight L2 sections).
- `change_flow_integration_review.md` (157): INTEGRATION.1 to .6, REVIEW.1 to .4.
- `change_flow_delivery.md` (226): BUILD.1 to .2, RELEASE.1 to .5, DEPLOY.1 to .4, ROLLBACK.1 to .3.
- `change_flow_data_and_measure.md` (185): DATA_CHANGE.1 to .8, MEASURE.1 to .2.

Method: read the brief; `ig-tool tree` for structure; a script iterating `ig-tool query --node` and `--links` over the 43 nodes, filtering `design_notes` to Decision, Positions, Rejected-with-condition and Context paragraphs. Graph not edited; nothing committed.

Rendering decisions:
- Each L2 intro takes the L2 `intent`; realizes/requires links to other branches shown as one phrase with a relative link; within-branch `requires`-type links shown inline where they change what the reader does.
- "Best instead when" lines come from the Rejected records only where a condition is named; "best never" cases kept as short rule lines.
- Open maintainer point: REVIEW (epistemic_state of REVIEW, REVIEW.1, REVIEW.4 all carry "awaiting maintainer"); also the L1 epistemic_state names it.
- Open gaps shown only where reader behaviour changes: INTEGRATION.1, .4; REVIEW.4; RELEASE.2; DEPLOY.4 (plus lighter notes on DEPLOY.2, ROLLBACK.1, DATA_CHANGE.1, .3, .4, .6, .7, .8, MEASURE.1).
- Numeric defaults flagged as team defaults: three active branches, review size 100 or 200 lines, migration time budgets (3 and 10 minutes, one second).
- Split: `md-structure-sync --toc add-always` on each file; in-file anchors rewritten to the file holding the target.

Status: md-structure-sync updated all four files without errors; link check 0 bad anchors among the four files; sibling anchors unverified (open).
