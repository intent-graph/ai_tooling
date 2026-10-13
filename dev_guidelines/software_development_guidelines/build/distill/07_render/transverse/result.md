# Render result: TRANSVERSE

## L1 headline

TRANSVERSE rendered in full: 36 of 36 nodes (1 L1, 6 L2, 29 L3) in 5 files, 660 lines. Because the branch exceeded 500 lines (639 in one file), it was split by L2 group: `transverse.md` is the index (30 lines), with `transverse_documentation.md` (110), `transverse_security.md` (232), `transverse_privacy.md` (104), `transverse_config_environments.md` (184). Open maintainer points ("awaiting maintainer"): none exist in the branch, so none shown; 11 open evidence gaps that change a reader's action are shown inline as "Open:" lines. `md-structure-sync` ran on all five files, status ok. Two judgement calls for the caller are listed in L2.

## L2 claims

- Files and lines (grounded, `wc -l`): transverse.md 30; transverse_documentation.md 110; transverse_security.md 232; transverse_privacy.md 104; transverse_config_environments.md 184. All within 500.
- Split rule applied (grounded): single file was 639 lines after TOC sync; split by L2 groups, the index holds the L1 thesis, the four hard rules from the L1 constraints, and a map table linking each L2 section. Security and monitoring share a file (both security); config and environments share a file.
- Nodes rendered (grounded): all 36. L1 as thesis plus map; each L2 as intro; each L3 as `###` subsection with decided practice, MUST rules, "Best instead" lines, uid in backticks. L2 uids closed each intro; L1 uid closes the thesis.
- Maintainer points (grounded): grep of the branch dump for "awaiting maintainer" returned 0; the settled maintainer decisions (DOCS.2, DOCS.3, DOCS.5) are rendered as decided practice, not as open points.
- Open gaps shown inline (grounded): DOCS.4 (condition for a generated changelog), SECURITY.1 (framework-to-question mapping, level definitions unread), SECURITY.2 (no evidence that maturity raises outcomes), SECURITY.6 (no bounty-yield comparison), MONITORING.4 (dated dwell-time figure, number itself omitted), MONITORING.5 (the two-artifact split stated by no source), PRIVACY.2 (no source gives a period), PRIVACY.3 (whether erasure reaches logs and all copies is contested), PRIVACY.4 (framework body unread), CONFIG.1 (audited-mechanism clause partly ungrounded), ENVIRONMENTS.1 (production data in lower environments out of scope). Remaining gaps (inferred trigger rules, comparative costs) are left to the graph.
- Links (grounded): realizes/requires links to other branches rendered as relative links to anchors that are the slugs of the target node names (assurance.md, change_flow.md, operation.md, evolution.md, ownership.md, construction.md). Intra-branch links verified to resolve in the files. Anchors in sibling files are inferred from node names, not checked, since those files are written in parallel.
- Stack-neutral (grounded): framework names (requirements standard, maturity model, benchmark), tool names (container, package-set products), the federation protocol, the well-known contact file name and the example day counts and the 90-day audit figure were left out because the graph's intent fields do not name them; they live in design_notes only.
- Excluded by rule (grounded): no ledger, register or research claim ids; no dates; no absolute paths.
- Judgement call 1 (inferred): omitting reference numbers (14/60 days, 90 days, 72 hours, ~200 days) loses concrete anchors for the reader; the graph records them as one source's or project's values, not rules. Say if you want them restored as labelled reference values.
- Judgement call 2 (inferred): the L1 constraints are shown as "Hard rules of the branch" in the index, beyond the brief's thesis-plus-map minimum, because they are the branch's only unconditional rules.
- md-structure-sync (grounded): ran on each of the five files, "1/1 files updated" each, rc 0.

## L3 full

Source reading: `ig-tool tree --root TRANSVERSE` (36 nodes), then `query --node` and `query --links` for each, dumped to a scratch file; the graph was never loaded whole and never edited. No commit or push.

Files (all under `ai_tooling/dev_guidelines/software_development_guidelines/`):
- `transverse.md`: thesis, hard rules, map. 30 lines.
- `transverse_documentation.md`: DOCS (DOCS.1 to .5). 110 lines.
- `transverse_security.md`: SECURITY (.1 to .6), SECURITY_MONITORING (.1 to .5). 232 lines.
- `transverse_privacy.md`: PRIVACY (.1 to .4). 104 lines.
- `transverse_config_environments.md`: CONFIG (.1 to .6), ENVIRONMENTS (.1 to .3). 184 lines.

Rendering decisions per node type:
- L3 form: one-to-three-line decided practice from `intent`; MUST/MUST NOT lines from `constraints`, with unconstrained facts added only from the intent; "Best instead" lines from the rejected-positions part of `design_notes` where a condition is named; tables where a condition maps to a choice (documentation level, anchor framework, deletion form, definition mechanism).
- Index nodes DOCS and SECURITY (MD-03): their intro points to the assurance sections that hold verification (`assurance.md#documentation-in-sync`, `assurance.md#security`).
- Cross-unit moves respected: token acceptance linked to `construction.md#what-counts-as-valid`; supply-chain trigger for a leaked secret linked from `ownership.md#dependency-lifecycle`; environment parity linked to `change_flow.md#environment-parity`; erasure-in-backups text held once in PRIVACY.3 as in the graph.
- Frameworks: rendered generically ("requirements standard", "prescriptive maturity model", "outcome framework", "descriptive benchmark").

Open points not shown (kept in graph): inferred trigger wording for remodelling (SECURITY.3), inferred prioritization rule and remediation time (SECURITY.5), receipt-time clause (MONITORING.2), exit-risk argument for tool-neutral rules (MONITORING.4; shown only as "keep tool-neutral where the platform may change"), leak vectors and custody-versus-channel split (CONFIG.2), no-branching rule argument (CONFIG.3), merit of static secrets (CONFIG.5), comparative costs of definition mechanisms (ENVIRONMENTS.2).

Verification: a script checked every intra-branch anchor link and every cross-file link among the five files; all resolve. Sibling-file anchors unchecked.
