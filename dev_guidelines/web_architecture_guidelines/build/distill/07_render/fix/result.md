# Render fix: result

Paths are relative to the guideline folder.

## L1 headline

The guideline is rendered again in one pass. All 21 review findings are applied and none is rejected; finding 18 is applied in the markdown only, because the graph text it depends on was not changed. All gates pass.
- **Files (lines)**: README.md 126, CLAUDE.md 22, glossary.md 71 (new), allocation.md 475, philosophy.md 386, stack_defaults_data.md 388, stack_defaults_logic_security.md 136 (new), stack_defaults_logic.md 280, stack_defaults_interaction.md 238, stack_defaults_agents.md 81 (new), stack_defaults_transverse.md 290. Every file is at most 500 lines.
- **Format**: the TOC depth is H2 in every file. Every file is synced with `md-structure-sync --max-level 2` and a dry run reports it unchanged (11 of 11). CLAUDE.md is a card with no sections, so it has no TOC.
- **Links and anchors**: 530 relative links checked, 0 broken. 0 cross-file links lack a section anchor.
- **uids**: all 212 nodes are cited (211 distinct uids; `ROOT` is shared by both graphs). That covers every non-deferred node and the deferred ones too. 0 cited uids are missing from the graphs, and 0 short uids remain in prose.
- **Hygiene scan**: 0 private names, 0 absolute or home paths, 0 ledger or build ids. The one date-like hit is the JSON Schema dialect name "2020-12". The 25 version-like hits are all technical requirements taken from the graph (TLS 1.3/1.2, ASVS 5.0, OpenAPI 3.1, WCAG 2.2, SLSA Build L2/L3, `/v1` and `/v2` paths, UUIDv7/v4, Pydantic v2, vitals thresholds). None is a document version.
- **Left for the graph owner**: `ALLOCATION.GUARD.3` still says the scoping key "leads" the composite primary key, against MD-01 (finding 18). Two epistemic and design-note passages in the graph still name the operator role as restricted on comments (see L3).

### Maintainer answers

The four answered questions (MD-04 deletion, MD-05 reads, MD-06 hosting, MD-07 SameSite) are re-rendered from the updated graph nodes. No "Open, awaiting maintainer" block, recorded default, fallback or interim comment rule remains. All gates pass again after this pass; the counts below supersede the ones above.
- **Files (lines)**: README.md 126, CLAUDE.md 22, glossary.md 71, allocation.md 473, philosophy.md 383, stack_defaults_data.md 385, stack_defaults_logic_security.md 137, stack_defaults_logic.md 277, stack_defaults_interaction.md 236, stack_defaults_agents.md 81, stack_defaults_transverse.md 284. Every file is at most 500 lines. A `md-structure-sync --max-level 2` dry run reports all 10 files that carry a TOC unchanged.
- **Gates**: 524 links, 0 broken, 0 cross-file links without an anchor. All 212 nodes are cited, 0 cited uids are unknown, 0 short uids appear in prose. "awaiting maintainer" occurs 0 times and "Open, awaiting" 0 times across all markdown files. The hygiene scan finds 0 private names, paths or build ids; the version-like hits are unchanged (technical requirements only).
- **README**: "Open Maintainer Questions" is replaced by "Maintainer Decisions": one paragraph per decision, MD-01 to MD-07, each saying what was decided and what it changes. One line says the six departures from the maintainer's codified practice stand as judged and are marked where they appear. The TOC is updated. The thesis now states the read rule from the new `ROOT` intent and points to the decisions.
- **Graph residuals**: the finding-18 residual is closed, since `ALLOCATION.GUARD.3` now uses MD-01's wording. Two passages still lag in the graph, and the markdown follows the decided constraints instead. In `INTERACTION.COLLABORATE`, the epistemic state still names the "comment-grant restriction for reporting and operator roles (inferred)". In `ALLOCATION.CONTEXT`, the design-note table still routes per-user reads to the old question.

## L2 claims

1. Applied: the logic file is split into stack_defaults_logic_security.md (backend security, 136 lines) and stack_defaults_logic.md (enforcement, processing, interface, 280 lines). README, CLAUDE.md and all links are updated.
2. Applied: the agent surface moved into stack_defaults_agents.md (81 lines). The interaction file now has its purpose statement after the H1, then TOC, `---` and line comments, and is synced (238 lines).
3. Applied from the updated graph: until the maintainer answers, the reporting role gets no SELECT on comment content or narrower-audience comments; the operator role sees every row; other roles see every row unless restricted. This is now stated in README Q1, Authorization, Roles and Privileges (data), Access Control Enforcement, Collaboration on Data and Notifications and Moderation.
4. Applied: README Q1 takes its recommendation from `ALLOCATION.GUARD.3`: read functions for data with per-user visibility, backend filtering acceptable for data without per-user rules. The "allocation judge" label is gone, and the same recommendation is added to the Authorization open clause.
5. Applied: every uid is written in full or replaced by a section link; 0 short or invalid uids remain.
6. Applied: `PIG-WEB-TRANSVERSE` closes the new Transverse Overview section.
7. Applied: departures from the maintainer's practice are marked in the allocation.md form at 10 places. In philosophy: CHECK constraints, and "deployed together" (normalized). In data: key width, `updated_at` on append-only tables, CHECK and hierarchies, the trigger-written `updated_at`, "deployed together", and the deletion recommendation.
8. Applied: the signed upload policy and the signed download URL are both described as cases of the single signed-file-URL exception, linked to URL as Public Interface.
9. Applied: "Send IETF `RateLimit` and `RateLimit-Policy` fields … documented as unstable until the draft is published."
10. Applied: "That condition always holds in the default context (inferred), so the fallback is available; which applies awaits the maintainer."
11. Applied: every cross-file link points to a section anchor; "abuse" points to Secured Entry; the "Secure / Agent / Interface" pointers point to real sections.
12. Applied: glossary.md has 53 one-line terms (27 guideline terms, 26 acronyms and standards), with explicit anchors. 176 links point to it, one per term at its first use in each file.
13. Applied: "the … node" and "the record" are replaced by section links or "this guideline"; philosophy's "this node" is reworded.
14. Applied with one marker, "(inferred)", after the clause it qualifies. 131 of the 137 nodes with an inferred or unvalidated clause carry it; 6 are left unmarked on purpose (L3). The README states the marker set and says the uid holds the full epistemic state.
15. Applied: all 8 lost rules are restored: the no-auto-number and deterministic-UUID rules, personal login roles, the wrapper-only rule, change table, comments and notification rows, one-time-code failures, problem-detail extensions, third-party credentials in the browser, and HTTPS-originated forwarding.
16. Applied: "Changes when: the team controls the registrable domain and commits all its subdomains … HSTS preload is then the target, recorded as an ADR."
17. Applied from the updated graph: the cross-domain function is owned by the team that owns the workflow and reviewed by the database owner role, linked to Team-Shaped Structure.
18. Applied in the markdown with MD-01's wording ("present in every table the policy covers, in practice composite primary keys led by that key") in README, Authorization, Row Security Placement and Request Context and Row Security. The graph text of `ALLOCATION.GUARD.3` still says "leads".
19. Applied: Title Case headings with the uid at the end of every section, `---` after every TOC, one open-clause marker (a quoted **Open, awaiting maintainer** block), one TOC depth (H2), and the interaction tier's open clause now gives its fallback.
20. Applied: "Parameters the placements require"; "'Deployed together' only when …" without a marker; "Unchecked" became "Gap".
21. Applied from the updated graph: both Server-Timing lines now read "authenticated and authorised audiences only".

### Maintainer answers

- **MD-04 (deletion)**: Deletion, Retention and Partitioning is rewritten from `PIG-WEB-DATA.MAINTAIN.2`. Deletion is a per-table choice. The default is basic soft delete, last-state or full-history, with foreign keys required. Hard delete plus a same-transaction archive becomes the "Acceptable" case, for some caches and for data consumers must be unable to reach, with its two weaknesses stated. A fourth inferred safeguard is added: propagation down soft-deleting hierarchies. The data overview and the `PIG-WEB-DATA.MAINTAIN` roll-up now say "basic soft delete by default". The thread-erasure clause in Threads and Comment Lifecycle names the default. The "recommendation departs from the maintainer's practice" mark is removed, because the conflict is resolved in favour of the practice.
- **MD-05 (reads)**: re-rendered from `ALLOCATION.GUARD.3`, `.GUARD`, `.RULES.4` and `PIG-WEB-LOGIC.SECURE.1`. Simple reads that carry no logic go to each backend directly; sensitive, complex, high-impact, function-built or shared reads go through database functions that receive the verified actor, and per-user visibility rules count as sensitive. The reporting role reads comment content and narrower-audience comments only through those functions; the operator role sees every row; other roles see every row unless restricted. This replaces every recorded default, fallback and interim comment rule in: the allocation overview, Context row, One Core rule, the matrix Authorization row (read functions added to the authority column, the open question removed from "Moved by"), the Guarding intro, Authorization, Stack Placements and the Row Security tension; philosophy Durable Data, Guarded Consistency, Secured Entry, Collaboration on Data, Security Across Tiers and Proportioned Testing; data Roles and Privileges and the Functions and Views ladder; Access Control Enforcement, Data Access and File Serving; the browser overview, Channel Security, Comments and Collaboration and Notifications and Moderation; the transverse overview, Security Requirement Catalogue and Testing.
- **MD-06 (hosting)**: re-rendered from `PIG-WEB-TRANSVERSE.TOPOLOGY.3`, `.TOPOLOGY.4`, `.SECURITY.4` and `.TOPOLOGY.1`. Hosting is a per-project choice recorded as an ADR; a prototype takes the fastest secure path. The self-managed defaults are one acceptable route, and each section says what changes on an orchestrator: the platform's secret store as the managed store; one server process per container, with the unprivileged supervisor, same-image and same-config rules kept; the platform edge or object store for built assets (inferred).
- **MD-07 (SameSite)**: re-rendered from `PIG-WEB-LOGIC.SECURE.2`, `.SECURE.3` and `.SECURE`. The cookie is `Lax` plus the Fetch Metadata navigation check (the check itself still marked inferred), and `Strict` for operator consoles. The rule now sits in Sessions next to the cookie rule, the CSRF second layer names the value, and the security overview states it.
- **README, CLAUDE.md, glossary**: the README is as in L1. CLAUDE.md now points to the seven decisions and says never to reopen one; **Open** marks only per-project or measured values. The glossary drops "Open maintainer clause" and "Recorded default" (their links are removed) and adds "Maintainer decision" and "Sensitive read". 29 first-use glossary links were restored or added where edited lines had held them.

## L3 full

### Decisions taken without asking

- **TOC depth H2 everywhere.** At H3 depth, allocation.md would have needed a further split, because its 38 subsections would each add a TOC line and a line comment (about 550 lines). H2 is what the documentation standard requires, and H3 is optional. The H3 line comments in philosophy.md (18) and stack_defaults_data.md (28) were removed. H3 anchors still work as link targets.
- **Single-branch files.** The security and agents files hold one graph branch each. Each starts with an "Overview" H2 carrying the branch roll-up uid, followed by one H2 per leaf, so the TOC is useful. Every stack file now opens with an "<X> Overview" H2 carrying its root uid.
- **File names and titles.** The new files use the task's names (`stack_defaults_agents.md`, not the review's `stack_defaults_agent.md`). The H1 titles are "Stack Defaults: Backend Security", "Python Application Tier", "Browser Surface", "Agent Surface" and "Transverse Concerns".
- **One line per paragraph.** The hard-wrapped files (logic, interaction, transverse) were rewritten with one line per paragraph or bullet, like the other files.
- **Markers.** The README defines one marker set: **Acceptable when**, **Changes when**, **Open, awaiting maintainer** (quoted block), **Open**, **(inferred)**, **Gap**, **Tension recorded**, **Departs from the maintainer's practice**, **Deferred**. "Speculative", "Known gap", "Unchecked", "To verify" and "Open (handed off)" are gone.
- **Uids and other files.** Uids of other files are no longer cited as "Refines `X`"; each refinement links the section by its title.
- **Superseded by the maintainer answers.** The **Open, awaiting maintainer** marker, the README's four open questions (Q4 included) and the recorded defaults no longer exist; see "Maintainer answers" in L1 and L2.
- **Glossary anchors.** The glossary uses explicit `<a id>` anchors, so that each term stays on one line.
- **Restored detail.** "Rotated by a scheduled task" (the secret file fallback) is kept in README Q4 and in Secrets: it is in the design notes of `PIG-WEB-TRANSVERSE.SECURITY.4`.

### Finding 14: what is not marked, and why

`ALLOCATION.DERIVE.2` already says "which collation is open". `ALLOCATION.GUARD.2` only routes the isolation level to the data tier. `LOGIC.EXPOSE.1` and `PIG-WEB-LOGIC.ENFORCE.2` carry source-quality notes, not inferred rules. `PIG-WEB-INTERACTION.AGENT` already says in words that its specifications are moving. `PIG-WEB-LOGIC.ENFORCE` is a roll-up whose framework clause is marked in Framework Choice and in the tier overview.

### Graph residuals, not editable in this scope

- Closed by the maintainer-answers graph update: `ALLOCATION.GUARD.3` now carries MD-01's wording. Before it, the constraint and the design notes said the scoping key "leads the composite primary key". MD-01 says "present in every table the policy covers, which in practice forces composite primary keys led by that key".
- Closed by the same update (the comment rule is decided under MD-05). Before it, in `ALLOCATION.GUARD.3`, the older design-note paragraph "Consequence, under either position: roles that may SELECT the base tables (reporting, operator) see every row, comments included" contradicted the newer constraint, which restricts the reporting role on comments.
- `INTERACTION.COLLABORATE`: the epistemic state still reads "the comment-grant restriction for reporting and operator roles (inferred)", while its constraint now restricts only the reporting role. The markdown follows the constraint.

### Checks run (scripts kept in the session scratchpad, not in the repository)

- **Link and anchor checker.** It resolves every relative markdown link outside code fences to an existing file. For a link with an anchor, it checks that the anchor exists, using GitHub heading slugs plus explicit `<a id>` anchors. Result: 530 links, 0 broken. A second pass counts links to sibling guideline files that have no anchor: 0.
- **uid check.** It dumped every node of both graphs with `ig-tool query --node` and compared them with the backticked uid tokens in all files. Results: 0 cited uids missing from the graphs; 0 uncited nodes, deferred or not; 0 bare short uids (such as `GUARD.4`) in prose.
- **Hygiene scan.** Regexes for private names, absolute and home paths, dates, version strings and ledger or build ids (L###, MD-##, J#, R#-#, X#, SRC-#, area claim ids, tiers, positions, review ids, question ids). Results as in L1.
- **Consistency sweep.** 0 leftover marker variants, 0 build-vocabulary phrases ("node" remains only where README and CLAUDE.md explain how to query the graph), 0 headings off Title Case.
- **Structure.** `md-structure-sync --max-level 2 --dry-run` reports every file unchanged. `wc -l`: the largest file is allocation.md at 475 lines.

### Files written

All in the guideline folder: README.md, CLAUDE.md, glossary.md, allocation.md, philosophy.md, stack_defaults_data.md, stack_defaults_logic_security.md, stack_defaults_logic.md, stack_defaults_interaction.md, stack_defaults_agents.md, stack_defaults_transverse.md, and this note. No graph or build file was edited. Nothing was committed or pushed.
