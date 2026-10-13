# Render result: EVOLUTION

## L1 headline

Rendered the whole EVOLUTION branch to `evolution.md` (356 lines, no split needed): 33 of 33 nodes (1 L1, 5 L2, 27 L3). `md-structure-sync` ran clean. No "awaiting maintainer" point exists in this branch, so none is shown. Two open gaps are shown inline: replacement versus rewrite, and the one-general-purpose-store rule.

Pin:
- Files written: `evolution.md` (356 lines); this report.
- Nodes rendered: 33 of 33 in the branch.
- Open maintainer points shown: 0 (none in branch; `EVOLUTION.INCREMENTAL.6` carries a settled maintainer item, not shown by design).
- Open gaps shown inline: 2 (`EVOLUTION.INCREMENTAL.3`, `EVOLUTION.TECHNOLOGY.4`), plus 2 short "Open" lines on `EVOLUTION.DEBT.2` and `EVOLUTION.DECOMMISSION.4`.
- `md-structure-sync`: run on `evolution.md`, TOC and line ranges in place, second run "Unchanged".

## L2 claims

- Structure [grounded]: L1 thesis plus rules and certainty line and a map table; five H2 sections (Decision Records, Incremental Change, Technical Debt and Refactoring, Decommissioning, Keeping Technologies Few), each with a 2 to 4 line intro and its L3 nodes as H3 sections; each node ends with its uid.
- Node coverage [grounded]: all 33 uids present (checked against the `ig-tool tree` listing).
- Open maintainer points [grounded]: a search for "awaiting maintainer" over the branch's nodes returned nothing. The graph's seven hits are all in other branches.
- Open gaps shown [grounded]: INCREMENTAL.3 (no rewrite position wins in general); TECHNOLOGY.4 (contested single-store rule, default applied: one general store until a measured limit); DEBT.2 (payoff of quality over speed unproven); DECOMMISSION.4 (no general durations).
- Stack neutrality [grounded]: dropped the HTTP header and Kubernetes forms (DECOMMISSION.3), the named incident and loss figure (DECOMMISSION.1), the one project's window figures, the proponent's headroom figure and the rewrite rule of thumb. Kept the strangler pattern and the adopt/trial/assess/hold vocabulary, which the intent itself names.
- Private-material exclusion [grounded]: omitted the "maintainer's codified practice" and ledger, register and claim ids from design_notes. One remaining word "maintainer" means a software maintainer, not the guideline's maintainer.
- Cross-file links [inferred]: relative links to `ownership.md`, `assurance.md`, `change_flow.md`, `operation.md`, `transverse.md` use the slug of the target node name (for example `ownership.md#updating`, `change_flow.md#review`). They assume siblings use node names as headings; not verified because the siblings did not exist yet.
- Link choice [inferred]: only `realizes`/`requires`-type and behaviour-changing links are shown; `see`-type links between sibling nodes are kept where they change what a reader does (owner-and-capacity pointer to Why Remove, retention, risk-carrying debt routing).
- Condensing [inferred]: the "Best instead when" lines merge positions from design_notes; where the record names no condition, none was invented.

## L3 full

Files and sizes:
- `evolution.md`: 356 lines, under the 500 limit, so no `evolution_*.md` split.
- Report folder: `build/distill/07_render/evolution/result.md`.

Method:
- `ig-tool tree --root EVOLUTION` for the 33 uids; `ig-tool query --node` and `--links` over each uid via a loop into a scratch file (not the whole graph); then composed by hand.

Per-section render (uid, certainty as shown to the reader):
- DECISIONS (1-6): .1 grounded, forces-as-trigger inferred; .2 inferred (no numeric threshold); .3 grounded; .4 grounded, document-type assignment inferred; .5 grounded, review use inferred; .6 inferred.
- INCREMENTAL (1-6): .1, .2, .4, .5, .6 shown as grounded with their gaps (the .2 debt-ness of an unfinished migration, the .4 sharded-versus-single boundary and the .6 few-consumer exception stated as inferred); .3 shown with an inline open line.
- DEBT (1-5): .1 grounded, item list inferred; .2 open payoff shown; .3 inferred survey primacy; .4 grounded; .5 inferred.
- DECOMMISSION (1-6): .1 inferred as one rule; .2 to .6 grounded; .4 numbers open; .5 and .6 as in the graph.
- TECHNOLOGY (1-4): .1 and .2 grounded (trail inferred); .3 inferred, contested; .4 open, default applied.

Maintainer points: none awaiting in this branch. INCREMENTAL.6 refers to a settled item with no answer awaited; left out of the public file, as the brief forbids mention of the maintainer's practice.

Format checks:
- Single H1; no Mermaid (one allowed, none needed); no dates or version numbers; relative links only; no absolute or home paths.
- `md-structure-sync evolution.md`: first run updated, second run "Unchanged".

Open items for the caller:
- Verify cross-file anchors once all siblings exist (see L2).
- The constraints at L1 are shown as the four graph constraints verbatim.
