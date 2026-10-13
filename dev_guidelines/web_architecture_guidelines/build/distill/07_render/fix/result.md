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

### MD-08 and MD-09

The two decisions are applied. MD-08: "best practice for the purpose, never the average, not the most demanding". MD-09: seven verdicts corrected under that rule. Every changed node of the corrections list is re-rendered from the graph, along with the allocation-matrix row it touches. All gates pass; the counts below supersede the earlier ones.
- **Files (lines)**: README.md 136, CLAUDE.md 22, glossary.md 71, allocation.md 473, philosophy.md 383, stack_defaults_data.md 385, stack_defaults_logic_security.md 136, stack_defaults_logic.md 278, stack_defaults_interaction.md 236, stack_defaults_agents.md 84, stack_defaults_transverse.md 284. Every file is at most 500 lines. A `md-structure-sync --max-level 2` dry run reports all 10 files that carry a TOC unchanged.
- **Gates**: 538 links, 0 broken, 0 cross-file links without an anchor. All 212 nodes are cited, 0 cited uids are unknown, 0 short uids appear in prose. The hygiene scan finds 0 private names, paths or build ids, and the version-like hits are unchanged. "awaiting maintainer" occurs 0 times.
- **Selection rule**: no markdown file states it as "most demanding". The two remaining mentions (README line 20 and decision 8) say that "best" is not "most demanding". Two markers that leaned on the old rule are gone: "the strictest reading of the source" on MFA, and "the strongest reading of 'preferably'" on the egress proxy.
- **README**: "Maintainer Decisions" now lists nine decisions. Decision 8 states MD-08; decision 9 lists the seven corrections, each linked to its section. CLAUDE.md and the glossary now count nine.
- **Graph residual**: `PIG-WEB-TRANSVERSE.PERFORMANCE` was not in the MD-09 batch and still says "work over about 1 s is deferred (ACT.3, settled)". That contradicts the corrected `ALLOCATION.ACT.3` ("a few seconds or the request timeout; 1 s is the interactive target"). Page Experience Targets renders the node as it stands; the graph owner should align it. The two residuals from the previous pass are fixed in the graph (`INTERACTION.COLLABORATE` state, `ALLOCATION.CONTEXT` notes). `ALLOCATION.FORCES.4` shows no change in the dump, and its rendering (1 s as a latency budget) already matches.

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

### MD-08 and MD-09

- **MD-08 (selection rule)**: README decision 8 says that each decision takes the position the strongest arguments establish for the node's purpose: never the average, never a blend, not the strictest because it is strict. "What This Is" already carries the corrected rule.
- **MFA (correction 1)**, from `LOGIC.SECURE`, `PIG-WEB-LOGIC.SECURE`, `.SECURE.4` and `.SECURE.5`:
  - MFA is offered on every human account, phishing-resistant preferred, and required on privileged accounts and at step-up. Requiring it on every account follows the project's risk level (scope inferred), and that stricter option is now the "Acceptable when" alternative.
  - The authentication context is requested and refused for privileged accounts, and a fresh context is required for sensitive operations on every account.
  - The 8-character minimum loses "(default)"; the "optional MFA" alternative is removed.
  - Rendered in Secured Entry, the security overview, Federated Login and Tokens, and Passwords and Login Throttling.
- **Client-named fetches (2)**, from `.SECURE.7`: the helper is the required control, and timeout, size cap and worker stay. A network guard is preferred (an egress proxy with direct egress blocked, or outbound rules denying the private, loopback, link-local and metadata ranges). It is required when the network holds internal services or a token-less metadata endpoint (inferred); otherwise the helper is the guard. The old "Acceptable when no egress proxy" line is dropped, since the rule absorbs it.
- **Agent tokens (3)**, from `PIG-WEB-INTERACTION.AGENT.3`, `.AGENT.4` and `.AGENT`:
  - Binding by client capability: tokens are sender-constrained for every client that can hold a key.
  - A bearer-only client keeps consequential scopes only with short, narrow tokens, server-held revocation and the exact-action approval that the writer function checks (inferred). Approved results reach the approving user in the application (inferred).
  - The approval is stated as the gate for bearer-only clients.
  - The rejected "required for consequential scopes" is rendered as "Acceptable when" a closed or certified set of agents can hold keys, or a result must return to the token holder.
- **Normalization (4)**, from `DATA.ORGANIZE`, `DATA.GUARD` and `PIG-WEB-DATA.GUARD.4`: keep the dependency-preserving third-normal-form design, enforce the dependency with a composite foreign key (inferred), and use a trigger only where no declarative form exists. This is rendered in Organized Facts, Guarded Consistency and the data Triggers list.
- **Deferral (5)**, from `ALLOCATION.ACT.2`, `.ACT.3` and `PIG-WEB-LOGIC.PROCESS.2`:
  - In-request phases only when the call is expected to finish within a few seconds, under the request timeout.
  - Deferral for work beyond a few seconds or the request timeout; 1 s stays the interactive target (linked to Latency) and is not the cut-off.
  - Also updated: the Side Effects matrix row ("Moved by") and the in-request "Acceptable when" line of Side Effects and Delivery.
- **Paging (6)**, from `ALLOCATION.DERIVE.2`, `PIG-WEB-LOGIC.EXPOSE.1` and `.ENFORCE.3`:
  - Keyset for structured-data and agent collections and for large or growing sets; offset with page numbers allowed for a bounded human HTML list.
  - Offset is forbidden for structured-data and agent collections, deep pages and bulk work.
  - Rendered in the allocation section, Contract Style and Resources, and Data Access. The matrix row's cells did not change in the graph.
- **Threat modelling (7)**, from `TRANSVERSE.SECURITY`: a threat model per critical flow and trust boundary, revisited when a placement on the flow changes, with misuse-case tests per tier. This is rendered in the Security Across Tiers text and its table row.
- **Notes only**: `PIG-WEB-DATA.MAINTAIN.2`, `PIG-WEB-DATA`, `PIG-WEB-LOGIC.EXPOSE.3`, `ROOT` and `ALLOCATION.CONTEXT` changed only in their design notes, so no rendered text changed.
- **Glossary**: 3 first-use links restored on edited lines (MFA, OpenID Connect).

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
