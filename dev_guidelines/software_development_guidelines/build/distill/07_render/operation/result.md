# Render result: OPERATION branch

## L1 headline

OPERATION rendered in full: 41 of 41 nodes (L1, 9 L2, 31 L3) into 4 files totalling 657 lines, split by L2 groups because one file came to 634 lines (over 500). Files: `operation.md` (37, thesis, hard rules, index), `operation_objectives_and_signals.md` (251), `operation_response_and_readiness.md` (212), `operation_recovery_and_feedback.md` (157). Open maintainer points ("awaiting maintainer") in the branch: none. Open evidence gaps that change what a reader does are shown inline as "Open:" lines. md-structure-sync ran on all four files, status ok. Graph untouched, nothing committed.

## L2 claims

- Files written (grounded, wc -l): operation.md 37; operation_objectives_and_signals.md 251 (Reliability Targets, Alerting, Telemetry); operation_response_and_readiness.md 212 (Incidents, Capacity, Operational Readiness, Runbooks and Playbooks); operation_recovery_and_feedback.md 157 (Recovery, Feedback).
- Nodes rendered (grounded, uid count by grep): 41 of 41. L1 as thesis plus hard rules from its constraints; L2 as `##` sections with intro; L3 as `###` subsections (claim, grouped rules, "Best instead when" lines, uid last).
- Split (grounded): the single-file render measured 634 lines after TOC and line comments; split by L2 groups per the brief, `operation.md` is the intro and index with one line per L2 and a link.
- Open maintainer points (grounded): none found; grep for "awaiting maintainer" hits no OPERATION node.
- Open gaps shown inline (grounded as shown): error budget minority view, burn-rate single authority, telemetry cost no governed-budget source, incident declaration bar, risk-management integration, on-call figures for small teams, headroom numeric, readiness reviewer and cadence, runbook automation risk, 3-2-1-1-0, hardening default, feedback targets.
- Links (grounded): realizes/requires links to other branches rendered as relative links to anchors computed as slugs of sibling node names (ownership.md, assurance.md, construction.md, change_flow.md, transverse.md). Those anchors are inferred to resolve; sibling files were being written in parallel and not checked.
- Format (grounded): no dates, no absolute paths, no ledger or register ids, no mermaid diagram (none carried structure better than prose). Stack names kept to W3C `traceparent` / `tracestate`, which the graph's intent names as a standard.
- md-structure-sync (grounded): run with `--toc add-always --max-level 2` on each file, rc 0, "Updated" or "Unchanged".

## L3 full

Method: a script walked `ig-tool query --node` over OPERATION and every descendant (41 nodes) plus `--links` per node; intents, constraints, examples, epistemic gaps and the "Rejected positions" part of design_notes were read; the full graph was never loaded. Hard rules of the L1 node were lifted into `operation.md`.

Choices of height:
- L3 nodes at claim: one decided practice paragraph, constraints grouped (conditional alternatives written as bullets or one table for Alert Basis), then one "Best instead when" or "Best never" line, then "Open:" where the epistemic gap changes the reader's action.
- Illustrative figures in the graph (20 percent in four weeks; 1,000 traces per second; on-call figures) kept labelled as illustration or one model's default, as the graph states.
- Index nodes: none in this branch.
- Links within the branch written as in-file or cross-file relative links (an in-file link is rewritten to the sibling file when the target section lives in another file of the split).

Cross-branch links rendered: ASSURANCE.AVAILABILITY (and .1, .4, .5), ASSURANCE.SECURITY.6 and .7, ASSURANCE.DOCS_SYNC.3, ASSURANCE.DATA_INTEGRITY.5, OWNERSHIP.CONTAINMENT, CONSTRUCTION.DESIGN.4, CONSTRUCTION.PROCESS, CHANGE_FLOW.RELEASE, CHANGE_FLOW.DEPLOY.4, TRANSVERSE.PRIVACY.1, .2, .3, TRANSVERSE.SECURITY_MONITORING.4. ASSURANCE.PERFORMANCE (related to the L1 node) is not linked separately; availability link covers the proof.

Not done: no README or CLAUDE.md (other writer); sibling anchors not verified; no review pass by a second agent.
