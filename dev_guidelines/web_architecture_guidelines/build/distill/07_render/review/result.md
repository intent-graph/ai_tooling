# Render review result

## L1

Render review: 21 findings (3 high, 10 medium, 8 low). Coverage is 204 of 205 non-deferred nodes (`PIG-WEB-TRANSVERSE` has no uid). The README lists all 4 open maintainer questions. In the 60-node sample, most nodes are faithful at claim level. Gates fail: `stack_defaults_logic.md` has 645 lines, and syncing `stack_defaults_interaction.md` takes it over 500. The files disagree on whether reporting and operator roles may read comments.

## L2

1. HIGH `stack_defaults_logic.md` has 645 lines, over the 500 maximum; split it into security plus core (about 370 lines) and processing plus HTTP interface (about 280 lines).
2. HIGH `stack_defaults_interaction.md` has a stale TOC, no `<!-- Lines -->` comments and no purpose statement after its title; syncing it gives 501 lines (H2 only) or 544 (H3); move Agent Surface into its own file.
3. HIGH Reporting and operator access to comments contradicts across files: README:76, allocation:261 and data:191 say these roles see every row, "comments included"; philosophy:212 and interaction:345-352 say they get no SELECT on comments until the question is answered. The graph holds both (`PIG-WEB-DATA.GUARD.2` against `COLLABORATE`).
4. MEDIUM README:76, question 1, gives a recommendation "not stored in the graph", attributed to "the allocation judge", an internal label; store it in `ALLOCATION.GUARD.3` or remove it.
5. MEDIUM At least 19 uids cannot be queried: short forms in the interaction file (`GUARD.4`, `ACT.2`, `MAINTAIN.6`, `PERFORMANCE`) and uids that do not exist (`ALLOCATION.JS_SERVER`, `ALLOCATION.TYPE_CHAIN`, `ALLOCATION.POSTGRES_FIRST`); `GUARD.2` and `GUARD.3` point to different graphs.
6. MEDIUM Coverage: the `PIG-WEB-TRANSVERSE` roll-up is rendered without its uid (transverse:35-39).
7. MEDIUM Departures from the maintainer's practice are not marked: data:102 (key width), data:121 (no `updated_at` on append-only tables), philosophy:58 (CHECK constraints required); allocation:248 shows the expected form.
8. MEDIUM The logic file allows "two credentials in a URL" (lines 92, 438, 474); the philosophy and the allocation allow one signed-file-URL exception, and graph node `PROCESS.4` says "the one kind".
9. MEDIUM The `SECURE.6` rule to send IETF `RateLimit` and `RateLimit-Policy` fields is rendered as a remark (logic:243-244).
10. MEDIUM "So the fallback may well win" (logic:126-127) is not in the graph and leans on an open maintainer question.
11. MEDIUM About 70 cross-file links have no section anchor; "Refines abuse in allocation.md" (logic:229) and "see Secure / Agent / Interface" (transverse:80, 371, 375) point to sections that do not exist; README questions 2-4 link to whole files.
12. MEDIUM No glossary: writer function, state column, outbox, expand-migrate-contract, island, ADR, ASVS, SLSA, LCP, DPoP, MCP and BFF are used before they are defined.
13. MEDIUM The interaction file uses build vocabulary ("the performance node", "the deferred delivery node", "the record") with no section link.
14. LOW Certainty markers are dropped for about 50 nodes with `unvalidated` clauses: for example, the order of the forces and of the rules are syntheses and the rejecting-copy rule is inferred, with no marker on any of them.
15. LOW Rules lost in sampled nodes: `ORGANIZE.2` (deterministic public UUID; no auto-number for composite keys), `DATA.GUARD.2` (personal human login roles), `MAINTAIN.2`, `SECURE.1`, `SECURE.5`, `EXPOSE.2`, `ACT.2`, `SECURITY.2`.
16. LOW HSTS preload is rendered as "Acceptable … only if"; the graph makes it the target under its condition (transverse:99-101).
17. LOW "Owned and reviewed by the teams the data tier names" (transverse:441-442) points nowhere useful; the graph names the workflow-owning team and the owner role as reviewer.
18. LOW The row-security condition is worded three ways (README:35, allocation:258 "leads the composite primary key", data:204); align them on MD-01.
19. LOW Format drift: the logic file uses sentence-case headings, puts the uid at the start of each section, has no `---` after the TOC and writes open clauses unmarked; TOC depth varies by file; the interaction tier's open clause omits the fallback.
20. LOW Three lines in the data file are garbled or misuse a marker: 398 ("Parameters placements require"), 400 (a condition under "Acceptable when"), 411 ("Unchecked:" is not a README marker).
21. LOW The Server-Timing audience is "authorised" at transverse:161 and "authenticated only" at :241; the difference starts in the graph.

Full findings with evidence and fixes: [review.md](review.md).
