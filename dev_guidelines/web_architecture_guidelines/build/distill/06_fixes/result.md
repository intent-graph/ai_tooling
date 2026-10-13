# Critique fixes applied to the two built IntentGraphs

Paths are relative to the guideline folder. Graphs: `intent_graphs/web_app_philosophy.ig.yaml` (`$PHIL`, now 80 nodes, 60 intra and 15 inter links) and `intent_graphs/web_defaults.ig.yaml` (`$PIG`, 132 nodes, 43 intra and 132 inter links). All edits went through `ig-tool` (`apply --batch` and `link set` / `link create`), role `steward`, with `-m` messages. Nothing was committed or pushed.

## L1 headline

- Applied: all 26 issues. Blocking 2 of 2, major 12 of 12, minor 12 of 12. Skipped: none. Two minors are applied in part (m3 keeps generic `SQL` and the HTTP verbs `UPDATE`/`DELETE`; m9 removes only the repeats that restate an item of the `Forbidden:` line). No verdict was changed.
- Validate: `ig-tool validate -g <graph> -m intent_graphs/intent_resources.yaml`: philosophy 80 nodes, 60 links, 0 errors, 0 warnings; defaults 132 nodes, 43 links, 0 errors, 0 warnings. All 250 intra and inter link endpoints exist.
- impl_pointers: 1,898 of 1,901 resolve against a record heading or a research claim: philosophy 816 of 816, defaults 1,082 of 1,085. The 3 others are the deferred nodes `PIG-WEB-DATA.MAINTAIN.6`, `MAINTAIN.7` and `DERIVE.3`, which their record lists as bullets under "Deferred nodes (not judged)", not as headings; counting that bullet form, 1,901 of 1,901. PIG judge-record pointers: 128 of 131 by heading, 131 of 131 with the bullet form (was 0 of 131).
- Node-name safety: 212 of 212 names free of `/ \ : * ? " < > | [ ] # ^`.
- Residual check: 0 ledger, judge-unit, review or source ids (`L###`, `J#`, `R#-#`, `X#`, `M#`, `m#`, `SRC-#`, `Q#`, `P#`, `C##`) left in any intent, constraint or example of either graph.

## L2 claims

Blocking
- B1: applied. TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 carry `undecided: awaiting maintainer, hosting model of the default context (recorded default ...)`; TOPOLOGY, SECURITY and PIG-WEB-TRANSVERSE carry `undecided (in children): awaiting maintainer, hosting model (...)`; ROOT lists it.
- B2: applied. The link intent now reads "The database functions in the API schema are the interface through which consumers reach data; views are never part of it." (`link set`, shape `realizes` kept).

Major
- M1: applied. SECURE.2 state uses `undecided: awaiting maintainer, SameSite value of the session cookie`; SECURE.3 carries the same token with its inheritance note; SECURE and PIG-WEB-LOGIC carry it as `undecided (in children)`; link SECURE.3 to SECURE.2 added (M7b).
- M2: applied. Phil ROOT now has a state; every roll-up above an open maintainer clause carries `undecided (in children): awaiting maintainer, <topic> (<child uids>)`. A programmatic check finds no ancestor missing the clause of any descendant, in either graph. PIG-WEB-DATA and DATA.MAINTAIN used the older "open child" wording; it was normalized to the same token.
- M3: applied. ROW_SECURITY's Authority line and intent now follow ALLOCATION.GUARD.3 (writer functions for per-user write rules, backends for product policy and identity, Postgres per consumer role); its inter link intent is aligned; the PIG-WEB-ALLOCATION roll-up intent says "product-policy authorization".
- M4: applied. All 131 PIG judge-record pointers use the record headings' notation `PIG-WEB.<AREA>...` (see L1 for the 3 bullet-form entries).
- M5: applied. Ledger, judge-unit, review and source ids and build narrative (changed after review, handed to, questions file) were removed from the intents and constraints of 100 nodes (21 philosophy, 79 defaults); `J<n> <UNIT>` became the qualified node uid; where a removed clause carried a fact it was appended to that node's design_notes as "Build narrative moved out of the constraints". MD-01 to MD-03 are defined once in each ROOT's design_notes (the defaults ROOT gained a design_notes). Citations that were a bare ledger id were rewritten from the ledger row text so the constraint still states the rule.
- M6: applied. One-call rule owned by phil RULES.5 and PIG DATA.INTERFACE.1, copies reduced to one-line references with intentlinks (ACT.1, DATA.GUARD, LOGIC.ENFORCE and its PIG node, EVOLUTION.5, EVOLUTION.2, DB_API, EDIT); read-visibility default owned by phil GUARD.3 (philosophy) and PIG-WEB-LOGIC.SECURE.1 (stack), others keep the token and a pointer; MD-01 conditions owned by phil GUARD.3 and PIG ROW_SECURITY (DATA.GUARD.3 refers); foreign mutations owned by ACT.2 (ACT.3 keeps "except ACT.2's in-request phase"); page-hide saving owned by PIG ENVIRONMENT.1 (EDIT, VISUALIZE.2 refer); cookie attributes owned by phil GUARD.4 (ENVIRONMENT.7 and PIG REALTIME.4 refer).
- M7: applied. Philosophy: 18 intra links (placements to rules and forces, tier to placement, DATA.INTERFACE). Defaults: 22 intra links (tier to tier, EDIT and VISUALIZE.2 to ENVIRONMENT.1, links to rule owners) and 13 inter links (M7c, m4, M8, M9). `conflicts` was not used for any of them.
- M8: applied (question 1: yes). Philosophy node `DATA.INTERFACE` ("Offered Contract") created under DATA, stack-neutral, owning no ledger row, realizing ALLOCATION.RECORD.2 and ALLOCATION.ACT.1; refined by PIG-WEB-DATA.INTERFACE; DATA and DATA.MAINTAIN gaps narrowed to "data lifecycle (retention)".
- M9: applied (question 2: yes). The six stack-neutral clauses are lifted as one constraint each into INTERACTION.COLLABORATE (stale write shown with both versions, merged in the existing stale-write constraint; report queue), INTERACTION.AGENT (approval by the owning user), LOGIC.PROCESS (no file readable before a clean scan), LOGIC.SECURE (server-side fetch), DATA.MAINTAIN (recovery to a chosen moment); the defaults nodes keep the stack realization and now refine the philosophy node by link. No new INTERACTION.EDIT node (not requested).
- M10: applied. PIG-WEB-INTERACTION and PIG-WEB-DATA carry six constraints each from the record bullets; the 11 other L2 roll-ups of the DATA and INTERACTION branches (ORGANIZE, GUARD, CONCURRENCY, MAINTAIN, DERIVE, INTERFACE, VISUALIZE, REALTIME, COLLABORATE, AGENT, ENVIRONMENT) carry one constraint per judged child.
- M11: applied (cheapest option). PIG-WEB-DATA.GUARD.3 renamed "Request Context and Row Security"; intent and constraints reordered so request context comes first; row-security conditions refer to ROW_SECURITY; the link to ALLOCATION.ACT.4 is kept.
- M12: applied. "Transaction-local" replaced by "scoped to the transaction" in phil GUARD.3, GUARD.4 and LOGIC.SECURE; the mechanism stays in PIG-WEB-DATA.GUARD.3.

Minor
- m1: applied. Trailing "`." and "." stripped from 40 states.
- m2: applied. First-person voice removed from 8 states ("a synthesis", "a reading", "the ranking is inferred").
- m3: applied in part. `SELECT`, `EXECUTE`, `superuser`, "JavaScript-readable", the JSON-fixed interface format and the MCP example (moved to `examples`) are neutral in philosophy; generic `SQL` and the HTTP verbs were left.
- m4: applied. The three PIG uids moved from philosophy constraints and state to design_notes; inter links PIG-WEB-DATA.CONCURRENCY.5 to INTERACTION.COLLABORATE and PIG-WEB-DATA.INTERFACE.1 to TRANSVERSE.CONTRACTS created.
- m5: applied. `conflicts` changed to `constrains` on both OPERABILITY to ACT.4 links; `refines` changed to `requires` on TRANSVERSE.SECURITY to ALLOCATION.RULES.3.
- m6: applied. DATA.MAINTAIN to ALLOCATION.RECORD.3 link intent now unconditional.
- m7: applied. DATA's gap, DATA.MAINTAIN's design_notes and PIG LOGIC.PROCESS.2's state ("resolved ... in J1 R3") updated.
- m8: applied. ALLOCATION.GUARD intent adds concurrency and duplicate suppression; PIG-WEB-ALLOCATION intent adds the type chain and its read-visibility clause now points at the philosophy owner.
- m9: applied in part. Repeats of `Forbidden:` items removed in RECORD.1, GUARD.2, GUARD.4, GUARD.5, ACT.1, ACT.2, ACT.3, ACT.4, DERIVE.1, DERIVE.2, DERIVE.3, PRESENT.1, PRESENT.2, PRESENT.3; positive restatements that add a how were kept.
- m10: applied. The COLLABORATE-local constraint left INTERACTION; VISUALIZE's locale clause reduced to a reference to PRESENT.2.
- m11: applied. FORCES.5's epistemic constraint dropped.
- m12: applied. Constraints of the TRANSVERSE branch and one DATA.ORGANIZE clause rewritten in the direct form (no "MUST"); the proxy-to-app re-encryption gap kept on SECURITY.2 and TOPOLOGY.1 now links to it.

### Re-check fixes

Batches `12_recheck_pig.yaml` (18 ops) and `12_recheck_phil.yaml` (2 ops), role `steward`; both graphs validate with the manifest, 0 errors, 0 warnings; pointers still 1,898 of 1,901. Rewrites were copied from the ledger rows (L188, L199, L494, L508, L521 to L524, L531, L540 to L544, L296) and then compressed.
- R-M1: REALTIME.1 last constraint now says the buffering risk "motivates the WebSocket-first position".
- R-M2: link EXPOSE.7 to SECURE.2 now reads "The compatibility window lasts at least as long as the absolute session timeout, so a page open with a valid session keeps working."
- R-M3: MAINTAIN.2 restates the full soft-delete rules (deleted_at, read filter, partial indexes, exempt constraints, explicit cascade deviations, idempotent polyvalent functions with confirmation flag, creation-time check, wrapper only where a cascade exists); MAINTAIN.4 states the whole sharding rule (10^7 to 10^9 rows, batching key and keyset paging, work list against skew, fan-out and ramp, per-batch recovery with job log and convergence query, never DDL); ORGANIZE.5 restores the JSONB limits (no core entities, no queried fields, three levels, no binary, bounded size); GUARD.1 lists the CHECK cases (ranges, lengths, either-or exclusivity, conditional requirements, time ordering).
- R-M4: INTERFACE.2 attributes the pool rule of thumb (cores x 2 plus effective spindles) to one practitioner source; INTERFACE.1 says "the platform's view rules".
- R-M5: SECURE.1 gains the consequence constraint (reporting and operator roles that may SELECT see every row, change table, comments and notification rows included; grants bound tables and columns, not users' rows).
- r1: "(agree)" dropped in MAINTAIN.2; ", a" dropped in AGENT.5; ORGANIZE.6 names the access-need rule; CONTRACTS.1 names the consumer-driven-tests question.
- r2: ENVIRONMENT.1 marks draft storage, clearing and the per-tab rule inferred, in the constraint and the state; VISUALIZE.2 and EDIT states no longer annotate moved text.
- r3: phil GUARD.3 says the backend asserted the actor from its verified identity and the functions treat it as a claim.
- r4: phil AGENT keeps the lifted approval constraint; the other two mentions are now a reference and a dropped clause.
- r5: PERFORMANCE names the performance-budget guide's sample numbers (past device baseline) as not adopted.
- r6: ENFORCE.2 carries `transaction.atomic(durable=True)` asserting it is outermost.
- r7: DERIVE.1 says "Of the three legitimate reasons to denormalize".

### Render-review fixes

Batches `13_render_phil.yaml` (4 ops) and `13_render_pig.yaml` (11 ops), role `steward`; both graphs validate with the manifest, 0 errors, 0 warnings.
- Finding 3: the decided consequence is stated in full at its owners, phil ALLOCATION.GUARD.3 (constraint and design_notes) and PIG-WEB-LOGIC.SECURE.1: until the maintainer answers, the reporting role gets no SELECT on comment content or narrower-audience comments (target-wide projection or nothing); the operator role (all-powerful by the maintainer's model) sees every row; any other role that may SELECT base tables sees every row unless its own role is restricted. Aligned as short references: PIG-WEB-DATA.GUARD.2, PIG-WEB-INTERACTION.COLLABORATE.4, PIG-WEB-INTERACTION.REALTIME.4 and phil INTERACTION.COLLABORATE.
- Finding 4: ALLOCATION.GUARD.3 state and design_notes now carry the recommendation (database read functions that receive the verified actor, for data with per-user visibility; each backend filtering acceptable for data without per-user rules) beside the recorded default. SECURE.2 (SameSite) and TOPOLOGY.3 (hosting) carry "recommendation: ...; recorded default: the same"; TOPOLOGY.4 and SECURITY.4 carry both too (SECURITY.4's recommendation, a managed store with the file fallback until one exists, is taken from its node text, so worth a glance).
- Finding 17: phil TRANSVERSE.EVOLUTION.5 and TRANSVERSE.EVOLUTION say the workflow-owning team owns the cross-schema function and the database owner role reviews; PIG EVOLUTION.2 names the same reviewer.
- Finding 21: both Server-Timing constraints (PERFORMANCE, OPERABILITY.1) now read "authenticated and authorised audiences only", which joins the two judge-record wordings.

### Maintainer answers MD-04 to MD-07

Batches `14_answers_phil.yaml` (14 ops), `14_answers_pig.yaml` (35), `15_cleanup_phil.yaml` (5) and `15_cleanup_pig.yaml` (6), role `steward`. Both graphs validate with the manifest, 0 errors, 0 warnings. `grep -c "awaiting maintainer"`: philosophy 0 (was 22), defaults 0 (was 58); "recorded default" survives only in design_notes as "former recorded default (superseded)"; pointers unchanged at 1,898 of 1,901.
- States: every "undecided ... awaiting maintainer" clause (holders and roll-ups, both roots) removed; holders become `known: MD-0n` (appended to an existing `known: MD-0x`), unrelated annotations kept.
- MD-04 (deletion): PIG-WEB-DATA.MAINTAIN.2 now decides: per-table design choice, default basic soft delete (deleted_at, no primary key change, deleted rows excluded by every consumer), two kinds of soft delete, hard delete plus same-transaction archive as the acceptable-when with its two weaknesses (scale cost, schema sync), foreign keys always, functions or triggers where foreign keys are not enough; kept: deletion through functions, partial unique indexes on active rows, constraint trigger refusing active children of deleted parents; added: propagation down hierarchies. State: `known: MD-04 | conflict resolved: L520 ... in favour of the doctrine`. Roll-ups (MAINTAIN, DATA) and COLLABORATE.2 name the default.
- MD-05 (reads): owners phil ALLOCATION.GUARD.3 and PIG-WEB-LOGIC.SECURE.1 state the rule in full (simple reads direct; sensitive, complex, high-impact, function-built or shared reads through database functions; per-user visibility rules are sensitive) and the decided comment rule (reporting role only through functions, operator sees every row, other roles see every row unless restricted). Aligned: phil LOGIC.SECURE, INTERACTION.COLLABORATE, TRANSVERSE.SECURITY, ALLOCATION.RULES.4 (its conflict annotation resolved); PIG ENFORCE.3, PROCESS.6, REALTIME.4, COLLABORATE and COLLABORATE.4, SECURITY.1, OPERABILITY.5, DATA.GUARD.2, DATA.INTERFACE.1.
- MD-06 (hosting): TOPOLOGY.3 states hosting as a per-project recorded choice, prototype on the fastest secure path, orchestration when reliability and scaling are needed, self-managed hosts as one acceptable route; TOPOLOGY.4 and SECURITY.4 keep their self-managed defaults as that route and say what changes on an orchestrated platform (the orchestrated clause for static assets is inferred and marked so).
- MD-07 (SameSite): SECURE.2, SECURE.3 and SECURE state Lax plus a cross-site navigation check, Strict for operator consoles, as decided.
- design_notes: owners and both ROOTs cite MD-04 to MD-07; older notes say "decided by MD-0n" in place of "awaiting maintainer".

## L3 full

Batches in this folder, applied in this order (op counts): 01_states_phil (22) and 01_states_pig (40): states (m1, m2, B1, M1, M2, m8); 02_links_phil (3): link kinds and m6; 02_row_security_pig (2): M3; 03_phil_content (50, one `node.create`): M6, M8, M9, M12, m3, m4, m9, m10, m11, m12; 04_phil_links_misc (20): M7a, DATA.INTERFACE links, m7, m8; 05_pig_content (30): M6, M10, M11, m7, m8, m12; 06_pig_links_intra (21): M7b and owner links; 07_clean_phil (21) and 07_clean_pig (79): M5; 08_phil_last_id (1); 08_pig_pointers (131): M4; 09_pig_root_notes (1); 10_pig_enforce1 (2); 11_phil_wording (4).

Edits made by single commands instead of a batch (inter links are not dispatched by `apply --batch`):
- `ig-tool link set -g $PIG --uid "pig-web-defaults:PIG-WEB-DATA.INTERFACE.1_web-app-philosophy:ALLOCATION.RECORD.2" --intent "..."` (B2).
- `ig-tool link set -g $PIG --uid "pig-web-defaults:PIG-WEB-ALLOCATION.ROW_SECURITY_web-app-philosophy:ALLOCATION.GUARD.3" --intent "..."` (M3).
- `ig-tool link set -g $PIG --uid "pig-web-defaults:PIG-WEB-TRANSVERSE.OPERABILITY.4_web-app-philosophy:ALLOCATION.ACT.4" --shape '{"type":"constrains"}'` (m5).
- 13 `ig-tool link create -g $PIG --src pig-web-defaults:... --dst web-app-philosophy:...` calls, listed with intent and shape in `06_pig_links_inter.yaml`.

Choices and assumptions (a reader may want to redirect):
- Token form. One open-maintainer token everywhere: `undecided: awaiting maintainer, <topic>` on the node that holds the question, `undecided (in children): awaiting maintainer, <topic> (<child uids>)` on every ancestor. The critic offered two parenthesis wordings (`child` and `in children`); `in children` was kept. Topics: read visibility of rows with per-user rules when several backends share the database; default deletion for user-facing transactional data; hosting model of the default context; SameSite value of the session cookie. The recorded-default text was shortened in states to "(see ... ALLOCATION.GUARD.3)" where the owner holds it, and the "J9 Q1" prefix of the critic's B1 text was dropped from the states.
- Link kinds for new links: `requires` for rule and tier dependencies, `refines` for tier-to-tier and PIG-to-philosophy lifts, `realizes` for placement realizations, `dataflow` for the trace id on history rows. TRANSVERSE.CONTRACTS.2 to ALLOCATION.RECORD.3 is `requires`, as the critic proposed.
- M9 wording: the lifted clauses are the PIG roll-up or record phrasing in stack-neutral words ("writer function", "client hint", "private, loopback or link-local addresses"). Each carries a design_notes line and an added `impl_pointers` entry pointing at the PIG judge record it came from. EDIT's stale-write clause was merged into COLLABORATE's existing stale-write constraint rather than added as a duplicate.
- M5: the automatic id removal deleted a parenthetical only when it held ids and separators alone; 84 constraints with ids inside prose were rewritten by hand with the rule kept and the citation replaced by what the cited ledger row says. A few citations became "the doctrine's ..." or "the philosophy's ..." references where the row text is not repeated. States keep their ledger ids (they are transcribed from the records and were out of the issue's scope). Deferred nodes' intents no longer say "round 2".
- M10: where the record gave one sentence for a roll-up, it was split at the child references (".1", ".2", ...) and each part labelled with the child's name.
- Not done: a new philosophy `INTERACTION.EDIT` node (only if the maintainer wants the "edit" verb filled); a ROOT statement that the database is relational (m3 alternative).

Propagation checklist on what changed: T4 (parent and children coherent) holds for the 13 roll-ups that gained constraints and for the philosophy DATA, which now lists its fifth child; T3 (links valid) holds, 250 of 250 endpoints exist and `validate` reports 0 errors; P5 (no restatement across peers) holds for the six rules of M6, checked by searching the repeated phrases in both graphs; P4 (projection detail routed to the projection graph) holds, philosophy names defaults uids only in design_notes; P2 (refinement adds precision, not scope) holds, no verdict, option or "acceptable when" condition was changed; epistemic: every open clause appears on all ancestors.

Residual risks: the 84 hand-rewritten constraints and the other wording changes were read by the author only; the critic's checks (faithfulness of intent and constraints against the records) were not re-run on them. A separate review pass is advisable before the guideline is rendered.
