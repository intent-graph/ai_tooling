# Render review: rendered markdown against the two IntentGraphs

Adversarial review of `README.md`, `CLAUDE.md`, `allocation.md`, `philosophy.md` and the four
`stack_defaults_*.md` files against `intent_graphs/web_app_philosophy.ig.yaml` and
`intent_graphs/web_defaults.ig.yaml`, checked against `build/distill/07_render/brief_render.md`.
Paths are relative to the guideline folder. Verdict: 21 findings (3 high, 10 medium, 8 low).

## Method

- Graphs were read through `ig-tool tree` and one `ig-tool query --node` per uid (212 nodes),
  dumped to a scratch directory; never loaded whole.
- Coverage: a script matched every graph uid against backticked uids in the eight files.
- Faithfulness: 60 rendered nodes compared with their `intent`, `constraints` and
  `epistemic_state`: allocation 14, philosophy 7, stack allocation 3, data 6, logic 12,
  interaction 7, transverse 11. A second script checked every node whose epistemic state is
  below grounded for a matching marker in its rendered section.
- Open questions: every `undecided` clause in both graphs was listed and compared with the
  README.
- Format: `md-structure-sync --dry-run` on each file, then the same tool run on copies at
  heading depth 2, 3 and 4 to see what a sync would change; `wc -l`; a link-and-anchor resolver;
  a grep for absolute paths, home paths, private names, dates and version numbers.

## Results per check

| # | Check | Result |
|---|---|---|
| 1 | Faithfulness (60 nodes) | Most nodes are faithful at claim level. Findings 3, 5, 8, 9, 10, 15, 16, 17, 18 |
| 2 | Coverage | 204 of 205 non-deferred nodes are rendered; `PIG-WEB-TRANSVERSE` is missing (finding 6). All 7 deferred nodes are rendered and marked deferred |
| 3 | README open questions | Complete: the graphs hold exactly 4 distinct maintainer clauses and the README lists all 4. Question 1 has an internal label and content not in the graph, and leaves out the comment restriction (findings 3, 4) |
| 4 | Cross-file consistency | Findings 3, 8, 18, 21; 19 short or invalid uids (finding 5); links without anchors (finding 11). Every link and anchor resolves |
| 5 | Documentation standard | `stack_defaults_logic.md` has 645 lines; `stack_defaults_interaction.md` is not synced and goes over 500 once synced (findings 1, 2). The other files are synced at their TOC depth |
| 6 | Readability | Terms used before they are defined, no glossary, internal graph vocabulary (findings 12, 13) |
| 7 | Private names, paths, dates, versions | Pass. The only version strings (Postgres 18, TLS 1.3, ASVS 5.0, OpenAPI 3.1, SLSA Build L3) are technical requirements taken from the graph, not document versions |

## Findings

Severity: **high** means a gate fails or a reader acting on the text does the wrong thing on a
security or data point; **medium** means a brief rule is broken or a reader can be misled;
**low** is polish or a minor loss.

### 1. HIGH: logic file over the 500-line maximum
- **Where**: `stack_defaults_logic.md:1-645`
- **Issue**: the file has 645 lines. The documentation standard caps a guideline module at 500,
  and the brief says to split any file that would go over.
- **Evidence**: `wc -l` gives 645. The other limits hold: `allocation.md` 475,
  `stack_defaults_transverse.md` 464, `stack_defaults_data.md` 429, `philosophy.md` 421.
- **Fix**: split the file where its topics divide, for example `stack_defaults_logic.md` (tier-wide
  rules, Backend security, Business logic realization, about 370 lines) and
  `stack_defaults_logic_interface.md` (Processing and side effects, HTTP interface, about 280
  lines). Then update the file maps in README and CLAUDE.md and the sibling links.

### 2. HIGH: interaction file not synced, and over the limit once it is
- **Where**: `stack_defaults_interaction.md:1-13`, every `##` heading
- **Issue**: the TOC's line ranges are stale. For example "Browser Rendering" is listed at
  Lines 36-114 but the heading is on line 34. No section has a `<!-- Lines -->` comment, which
  the standard requires. The TOC comes before the purpose statement, and there are two blank
  lines before `---`. Running `md-structure-sync` takes the file to 501 lines at heading depth 2
  and 544 at depth 3, so the sync the brief requires pushes it over 500.
- **Evidence**: `md-structure-sync --dry-run` reports "would be updated", and the counts come
  from syncing copies. Every other file reports "Unchanged" at its own TOC depth.
- **Fix**: move Agent Surface (lines 358-463, about 105 lines) into `stack_defaults_agent.md`.
  Put a 1-3 sentence purpose statement right after the H1, then the TOC, then `---`. Run
  `md-structure-sync` on both files.

### 3. HIGH: files disagree on whether reporting and operator roles may read comments
- **Where**: `README.md:76`, `allocation.md:261`, `stack_defaults_data.md:191` against
  `philosophy.md:212` and `stack_defaults_interaction.md:345-352`
- **Issue**: the README, Authorization and Roles and Privileges say that roles that may read
  base tables "see every row, comments included, unless their own role is restricted". The
  collaboration sections say that until the read-visibility question is answered, those roles
  "get no SELECT on comment content or on comments with a narrower audience than their target".
  A DBA who sets up grants from the data file will grant reporting full SELECT on comments, which
  the recorded default forbids. The README's question 1, which the maintainer will decide from,
  never mentions the comment restriction.
- **Evidence**: the graph holds both statements. `PIG-WEB-DATA.GUARD.2` says "rows with per-user
  rules and comments included". `INTERACTION.COLLABORATE` and `PIG-WEB-INTERACTION.COLLABORATE.4`
  say "Until the read-visibility question is answered: reporting and operator roles get no read
  access to comment content…".
- **Fix**: correct the graph first. In `PIG-WEB-DATA.GUARD.2`, either add the comment-grant
  restriction or point to `COLLABORATE.4`. Then re-render. Add one sentence to README question 1,
  `allocation.md` Authorization and `stack_defaults_data.md` Roles and Privileges: "Until
  answered, these roles get no SELECT on comment content or on comments narrower than their
  target (a target-wide projection, or nothing); otherwise the leak is a stated known limit."

### 4. MEDIUM: README question 1 states a recommendation that is not in the graph
- **Where**: `README.md:76`
- **Issue**: "Recommendation (from the allocation judge and its review, not stored in the
  graph): read functions in the database…". This breaks the rule that the graphs are the source
  of truth: the markdown adds a position the graph does not hold. "Allocation judge" is an
  internal build label that a reader cannot follow. The other three questions take their
  recommendation from the graph.
- **Evidence**: the design notes of `ALLOCATION.GUARD.3` record the default, the fallback and
  the consequence, and no recommendation. `PIG-WEB-DATA.MAINTAIN.2` and
  `PIG-WEB-LOGIC.SECURE.2` do store theirs.
- **Fix**: write the recommendation into `ALLOCATION.GUARD.3` (epistemic state or design notes,
  following `MAINTAIN.2`), then render it as "Recommendation: …" with no source label. Otherwise
  remove it.

### 5. MEDIUM: at least 19 uid references cannot be queried
- **Where**: `stack_defaults_interaction.md:46, 81, 119, 129, 238, 259, 306, 307, 324, 351, 355,
  373, 423, 443`; `stack_defaults_interaction.md:94` (`PERFORMANCE`); `stack_defaults_logic.md:398`
  ("ACT.2 and ACT.3")
- **Issue**: shortened uids such as `GUARD.4`, `ACT.2`, `MAINTAIN.6`, `EXPOSE.2` and `PERFORMANCE`
  are not graph uids. `ALLOCATION.JS_SERVER`, `ALLOCATION.TYPE_CHAIN` and
  `ALLOCATION.POSTGRES_FIRST` do not exist; the real uids are `PIG-WEB-ALLOCATION.*`. Some short
  forms are also ambiguous: `GUARD.2` on line 351 means `PIG-WEB-DATA.GUARD.2`, while `GUARD.3`
  to `GUARD.6` elsewhere mean `ALLOCATION.GUARD.*`. Running `ig-tool query --node GUARD.4`
  fails.
- **Evidence**: the uid script flags 19 backticked tokens that match no node in either graph.
- **Fix**: write the full uid (`ALLOCATION.GUARD.4`, `PIG-WEB-ALLOCATION.JS_SERVER`,
  `PIG-WEB-DATA.MAINTAIN.6`, `PIG-WEB-LOGIC.EXPOSE.2`, `PIG-WEB-TRANSVERSE.PERFORMANCE`) or
  replace it with a section link.

### 6. MEDIUM: coverage gap, the transverse roll-up node has no uid
- **Where**: `stack_defaults_transverse.md:35-39`
- **Issue**: the file's intro renders the `PIG-WEB-TRANSVERSE` roll-up but does not end with its
  uid, so the coverage check fails for 1 of 205 non-deferred nodes. Every other tier roll-up
  (`PIG-WEB-DATA`, `PIG-WEB-LOGIC`, `PIG-WEB-INTERACTION`, `PIG-WEB-ALLOCATION`) carries its uid.
- **Evidence**: the coverage script reports `MISSING D PIG-WEB-TRANSVERSE`.
- **Fix**: add `` `PIG-WEB-TRANSVERSE` `` at the end of the intro paragraph (line 39).

### 7. MEDIUM: departures from the maintainer's own practice are not marked
- **Where**: `stack_defaults_data.md:102` (8-byte default key width), `stack_defaults_data.md:121`
  (no `updated_at` on append-only tables), `philosophy.md:58` (CHECK constraints "Required, not
  optional")
- **Issue**: the graph records each of these as a conflict with the maintainer's practice.
  `allocation.md:248` marks the same CHECK departure ("Departs from the maintainer's
  practice…"), but these three sections give no sign. The maintainer is a stated reader and
  cannot see where the guideline overrides their practice.
- **Evidence**: `PIG-WEB-DATA.ORGANIZE.2` has "conflict: partly against L503 (MAINT) on default
  key width". `PIG-WEB-DATA.ORGANIZE.3` has "conflict: partly against L498 (MAINT): no updated_at
  on append-only tables". `DATA.GUARD` has "conflict: against L471 (MAINT) on optional CHECK
  constraints".
- **Fix**: add one line to each: "Departs from the maintainer's practice: …", in the same form as
  `allocation.md:248`.

### 8. MEDIUM: logic file says two credentials may travel in a URL; elsewhere there is one exception
- **Where**: `stack_defaults_logic.md:92-93, 438, 474` against `philosophy.md:277`,
  `allocation.md:271`, `stack_defaults_interaction.md:224`
- **Issue**: the logic file calls the upload POST policy "one of the two credentials allowed in a
  URL or form target" and the download URL "the second allowed credential". The philosophy and
  the allocation state "the one exception: a short-lived, single-purpose, scope-limited signed
  URL for file delivery". The rendered text invents a count that the graph does not state.
- **Evidence**: `PIG-WEB-LOGIC.PROCESS.4` says "The signed policy is the one kind of credential
  allowed in a URL or form target". `INTERACTION.ENVIRONMENT.6` says "The one exception: … signed
  URL for file delivery".
- **Fix**: say "The signed upload policy and the signed download URL are both cases of the single
  signed-file-URL exception ([URL as Public Interface](philosophy.md#url-as-public-interface))".

### 9. MEDIUM: a rate-limit rule became a remark
- **Where**: `stack_defaults_logic.md:243-244`
- **Issue**: "IETF `RateLimit` fields are marked unstable (draft)" reads as an observation. The
  graph requires the backend to send them.
- **Evidence**: `PIG-WEB-LOGIC.SECURE.6` says "IETF `RateLimit` and `RateLimit-Policy` fields on the
  JSON interface and the agent surface, marked unstable until the draft is published."
- **Fix**: "Send IETF `RateLimit` and `RateLimit-Policy` fields on the JSON interface and the agent
  surface, documented as unstable until the draft is published."

### 10. MEDIUM: the logic file leans on an open maintainer question
- **Where**: `stack_defaults_logic.md:126-127`
- **Issue**: "That condition already holds in the default shared-database context, so the fallback
  may well win." The phrase "may well win" is not in the graph and steers the open question.
  CLAUDE.md rule 5 says never to settle a maintainer question.
- **Evidence**: `ALLOCATION.GUARD.3` and `PIG-WEB-LOGIC.SECURE.1` say only that the condition is
  always met, so the fallback is available wherever the shared-database default holds.
- **Fix**: replace with "That condition always holds in the default context, so the fallback is
  available; which applies awaits the maintainer."

### 11. MEDIUM: cross-file links without anchors, and pointers to sections that do not exist
- **Where**: `stack_defaults_logic.md` (26 file-only links), `stack_defaults_interaction.md` (29),
  `stack_defaults_transverse.md` (8), `stack_defaults_data.md` (6), `README.md:78, 80, 82`
- **Issue**: the brief asks that a refinement link go to the section in the other file. Many
  "Refines X in [allocation.md](allocation.md)" links open only the file. Some name a section
  that does not exist. `stack_defaults_logic.md:229` says "Refines abuse in allocation.md", but
  allocation has no abuse section. `stack_defaults_transverse.md:80, 371, 375` say "see Secure /
  Agent / Interface in …" but no section has those titles. The README's questions 2-4 link to
  whole files.
- **Evidence**: grep counts of `](allocation.md)`, `](philosophy.md)` and
  `](stack_defaults_*.md)`. The link resolver confirms these files exist but finds no anchors.
- **Fix**: add anchors, for example `allocation.md#authorization`,
  `philosophy.md#secured-entry`, `stack_defaults_logic.md#sessions`,
  `stack_defaults_data.md#deletion-retention-and-partitioning`,
  `stack_defaults_transverse.md#process-placement`. Point "abuse" at
  `philosophy.md#secured-entry`.

### 12. MEDIUM: key terms are used before they are defined, and there is no glossary
- **Where**: `README.md:76` ("writer function"); `allocation.md:159` ("state columns", "outbox");
  `allocation.md:210` ("expand, migrate, contract"); `allocation.md:188` ("islands", defined only
  at :382); `stack_defaults_transverse.md:63-82` (ASVS, ADR, never expanded); LCP, INP, CLS, SLSA,
  DPoP, MCP and BFF across the stack files
- **Issue**: the stated readers include an engineer who opens one file. These terms carry the
  rules, yet none is defined where it first appears. "Writer function" and "state column" are
  this guideline's own vocabulary, so the reader cannot look them up elsewhere.
- **Evidence**: a grep for the first occurrence of each term finds use with no definition.
- **Fix**: add a Terms section to the README, one line per term: function API, writer function,
  state column, actor (asserted, claimed), consumer role, owner role, outbox, staged intent,
  expand-migrate-contract, deployed together, island, copy versus authority, drift gate. Expand
  each acronym at its first use in each file and link the first use of a defined term to the
  glossary.

### 13. MEDIUM: internal graph vocabulary in the interaction file
- **Where**: `stack_defaults_interaction.md:74` ("the response-caching node"), `:93` ("the
  performance node"), `:305` ("the deferred personal-data node"), `:335` ("the deferred delivery
  node"), `:65, :214` ("the record"); `philosophy.md:405` ("this node")
- **Issue**: "node" and "the record" are build vocabulary. A reader can only act on them by
  querying the graph, and none of these phrases links to a section.
- **Fix**: name the section and link it, for example
  [Response caching](stack_defaults_logic.md#response-caching),
  [Page Experience Targets](stack_defaults_transverse.md#page-experience-targets),
  [Deferred Topics](stack_defaults_data.md#deferred-topics),
  [Email and push delivery](stack_defaults_logic.md#email-and-push-delivery). Replace "the
  record" with "this guideline".

### 14. LOW: certainty markers are dropped for about 50 nodes
- **Where**: across all files. Examples: `allocation.md:56-61` (the order of the forces is a
  synthesis), `allocation.md:127` (the order of the rules is a synthesis), `allocation.md:131-136`
  (the rule on rejecting copies is inferred), `allocation.md:381` (the rendering default is a
  judgment), `allocation.md:81-82` (the "no measured comparison" gap of `FORCES.5`),
  `philosophy.md:205-212` (the comment-grant restriction is inferred)
- **Issue**: the README promises that "Inferred, speculative, gap and tension recorded mark
  certainty below grounded". Of the nodes whose epistemic state carries an `unvalidated` clause,
  55 render with no marker; 13 conflicts and several substantive gaps also go unmarked. Many of
  these clauses are minor and a roll-up may rightly drop them, but the ones above qualify rules
  that a reader acts on.
- **Evidence**: the certainty script compared each node's `epistemic_state` with its rendered
  section. Excluded: roll-up gaps such as "owns no row", and departures from the maintainer's
  practice (finding 7).
- **Fix**: add an "Inferred: …" line where the inferred part is itself the rule (the orders of
  forces and rules, the rejecting-copy rule, the rendering default, the comment-grant
  restriction). Alternatively, soften the README's promise to "marks the main uncertainties;
  query the uid for the full epistemic state".

### 15. LOW: rules lost in the sampled nodes
- **Where and evidence**:
  - `stack_defaults_data.md:101-105`: missing "no auto-number for natural or composite keys" and
    "a deterministic UUID in a stored generated column serves a public identifier over a
    composite natural key" (`PIG-WEB-DATA.ORGANIZE.2`).
  - `stack_defaults_data.md:187-193`: missing "Humans have personal login roles, members of the
    operator or read roles; they assert only themselves as actor" (`PIG-WEB-DATA.GUARD.2`).
  - `stack_defaults_data.md:318`: missing "exist as a wrapper only where a cascade or business
    rule exists" (`PIG-WEB-DATA.MAINTAIN.2`).
  - `stack_defaults_logic.md:129-130`: the consequence leaves out "the change table, comments and
    notification rows" (`PIG-WEB-LOGIC.SECURE.1`).
  - `stack_defaults_logic.md:219-221`: missing "one-time-code endpoints count failures only"
    (`SECURE.5`).
  - `stack_defaults_logic.md:526-528`: missing "extensions are documented and ignored by clients
    that do not know them" (`EXPOSE.2`).
  - `allocation.md:182`: the Forbidden cell leaves out "third-party credentials in the browser"
    (`ALLOCATION.ACT.2`).
  - `stack_defaults_transverse.md:89`: missing "forwards only HTTPS-originated requests"
    (`SECURITY.2`).
- **Fix**: add each back as a clause in the existing bullet.

### 16. LOW: the HSTS preload framing is softened
- **Where**: `stack_defaults_transverse.md:99-101`
- **Issue**: the text renders preload as a rejected alternative ("Acceptable when: … only if").
  The graph makes it the target when its condition holds.
- **Evidence**: `PIG-WEB-TRANSVERSE.SECURITY.2` says "Preload is the target when the team controls
  the registrable domain and commits every subdomain… It is recorded as an ADR".
- **Fix**: "Changes when: the team controls the registrable domain and commits all its subdomains
  to HTTPS long term; preload is then the target, recorded as an ADR (slow to undo)."

### 17. LOW: the cross-domain function ownership pointer is vague and points to the wrong file
- **Where**: `stack_defaults_transverse.md:441-442`
- **Issue**: "owned and reviewed by the teams the data tier names". The data file names no teams,
  so a reader cannot act on this line.
- **Evidence**: `PIG-WEB-TRANSVERSE.EVOLUTION.2` says "owned by the team that owns that workflow,
  reviewed by the cross-schema owner role (web-app-philosophy:TRANSVERSE.EVOLUTION.5)".
- **Fix**: "owned by the team that owns the workflow and reviewed by the database owner role
  ([Team-Shaped Structure](philosophy.md#team-shaped-structure))."

### 18. LOW: the row-security condition is phrased three ways
- **Where**: `README.md:35` ("the scoping key is in every table"), `allocation.md:258` ("leads the
  composite primary key of every table"), `allocation.md:444` and `stack_defaults_data.md:204`
  ("present in every table … in practice composite primary keys led by that key")
- **Issue**: the same maintainer condition is worded three ways. `allocation.md:258` is stricter
  than the maintainer decision MD-01.
- **Evidence**: MD-01 in `build/distill/maintainer_decisions.md` says "present in every table the
  policy covers". `ALLOCATION.GUARD.3` itself uses "leads", so the drift starts in the graph.
- **Fix**: use the MD-01 wording plus "in practice composite primary keys led by that key"
  everywhere, and align `ALLOCATION.GUARD.3` in the graph first.

### 19. LOW: format inconsistencies between files
- **Where**: `stack_defaults_logic.md:1, 17-50` and every heading; `stack_defaults_logic.md:121,
  152`; `stack_defaults_interaction.md:28-32`; the TOC depth of every file
- **Issue**:
  - The logic file uses sentence-case headings and places the uid at the start of each section,
    while the README says "Each section ends with its graph uid".
  - It has no `---` after the TOC, and it writes open clauses as plain "Open maintainer question,"
    instead of the bold or block-quote "Open, awaiting maintainer" marker the other files use.
  - The TOC depth differs by file: H2 in allocation and interaction, H3 elsewhere.
  - The interaction tier's open clause gives the default without the fallback (database read
    functions, acceptable when two or more backends need the rule).
- **Fix**:
  - Use Title Case headings with the uid at the end of each section.
  - Add `---` after the TOC and use the shared open-clause marker.
  - Pick one TOC depth for all files.
  - Add the fallback sentence to the interaction tier's open clause.

### 20. LOW: three garbled or misused lines in the data file
- **Where**: `stack_defaults_data.md:398, 400, 411`
- **Issue**:
  - Line 398: "Parameters placements require:" is garbled.
  - Line 400: "Acceptable when: 'deployed together' applies only if…" uses the rejected-alternative
    marker for a condition.
  - Line 411: "Unchecked:" is not one of the README's markers.
- **Fix**:
  - Line 398: "Parameters the placements require:".
  - Line 400: "'Deployed together' only when every consumer…", with no marker.
  - Line 411: "Inferred: …" or "Open: …".

### 21. LOW: the audience of Server-Timing is stated two ways
- **Where**: `stack_defaults_transverse.md:161` ("authorised audiences") against `:241`
  ("authenticated audiences only")
- **Issue**: two different access conditions are given for the same header. The difference
  starts in the graph: `PIG-WEB-TRANSVERSE.PERFORMANCE` says one and `OPERABILITY.1` the other.
- **Fix**: choose one in the graph ("authenticated and authorized audiences only") and re-render
  both lines.
