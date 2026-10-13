# Re-check of the two IntentGraphs after the critique fixes

This re-check covers `intent_graphs/web_app_philosophy.ig.yaml` (now 80 nodes) and `intent_graphs/web_defaults.ig.yaml` (132 nodes) after the steward applied the 26 findings of `critique.md` (report: `build/distill/06_fixes/result.md`). Its focus is the text nobody but its author had read: the 84 hand-rewritten constraints, the M5 and M6 moves, the new philosophy node DATA.INTERFACE, the lifted M9 clauses, the M10 roll-up constraints and the M11 rename. Read-only; same format and conventions as `critique.md` (`$PHIL`, `$PIG`, `-o` set to the same file plus `--role critic-fix -m "<why>"` on every command, left out below).

Method in one line:
- I dumped every node with `ig-tool query --node` before and after the fixes.
- I read every changed intent, constraint and example, old beside new, in full: 160 nodes, a 1,502-line diff.
- I checked each rewrite that replaced a citation with prose against the cited ledger row (`02_skeleton/claims_ledger.md`) or judge record.
- I re-ran the mechanical sweeps: tokens on ancestors, residual ids, duplication, language swap, link kinds, pointers.

Pinned:
- Issues: 12 = 0 blocking, 5 major, 7 minor. New issues introduced by the fixes: all 12 (none is a leftover of the 26).
- By type: faithfulness_drift 6 (R-M1, R-M2, R-M3, R-M4, r5, r7), lost_content 2 (R-M5, r6), stale_annotation 1 (r2), format_artifact 1 (r1), intent_quality 1 (r3), duplication 1 (r4).
- The 26 original findings:
  - Resolved as intended: 2 of 2 blocking, 12 of 12 major (M6 with one gap, R-M5), 12 of 12 minor (m3 and m9 in part, as the steward reported).
  - Reopened: none.
- Faithfulness:
  - 38 changed nodes (plus the unchanged owner ALLOCATION.RULES.5) were checked against their judge record or ledger row (list at the end).
  - The other changed nodes are id strippings that I read old beside new, with no rule changed.
- Mechanical:
  - Every holder of the four open questions has the clause on all its ancestors (read visibility 39 nodes, deletion 4, hosting 7, SameSite 5).
  - 0 process ids left in any intent, constraint or example.
  - 212 of 212 node names safe.
  - Pointers: 1,898 of 1,901 resolve. The 3 that do not are the deferred nodes listed as bullets, not headings, in the J6 record.
  - New links: 18 philosophy intra, 22 PIG intra, 13 inter. Kinds: requires, refines, realizes, dataflow; no `conflicts`.

## Blocking

None.

## Major

**R-M1. A rewrite inverts which position the buffering risk motivates (faithfulness_drift).** Node: PIG `INTERACTION.REALTIME.1`.
- Evidence: the record (J8, REALTIME.1) says "The buffering risk that motivates P2 is contained", and P2 is "WebSocket first (… SSE can be buffered by proxies and CDNs)". The rewrite reads "The buffering risk that motivates the SSE-only position is contained". SSE is the chosen default (P1 and P3), not the position the risk motivates. A reader of the guideline would take the buffering risk as an argument for SSE.
- Proposed edit: full-list `node set --constraints` with the last constraint reading "The buffering risk that motivates the WebSocket-first position is contained, not ignored: …" (rest unchanged).

**R-M2. A new link turns a minimum into a maximum (faithfulness_drift).** Link: PIG `LOGIC.EXPOSE.7 → LOGIC.SECURE.2` (M7b).
- Evidence: the link intent says "The compatibility window is bounded by the absolute session timeout." The record (J7, EXPOSE.7, decision 4) and the node's own constraint say changes stay additive "across a window at least as long as a page can live with a valid session (the absolute session timeout)". The session timeout is the window's floor, not its bound. My critique's shorthand ("window bound = absolute session timeout") invited this reading.
- Proposed edit: `ig-tool link set -g $PIG --uid <EXPOSE.7→SECURE.2 link uid> --intent "The compatibility window lasts at least as long as the absolute session timeout, so a page open with a valid session keeps working."`

**R-M3. Citation-to-prose rewrites that keep only part of the cited rule while reading as complete (faithfulness_drift, loss).**
- Evidence (cited row against new text):
  - PIG `DATA.MAINTAIN.2`:
    - The old text was "L521 to L524 apply whole". The new text: "the doctrine's soft-delete rules apply whole (a nullable timestamptz deleted_at, constraints that exempt deleted rows, cascades that follow the foreign-key graph in dedicated functions, idempotent soft-delete functions)".
    - Dropped from those rows: every read filters on `deleted_at` and partial indexes cover active rows (L521); uniqueness is a partial unique index over active rows (L522); deviations from the native cascade are explicit and justified (L523); bulk deletion needs an explicit confirmation flag, a deletion time earlier than creation is rejected, and wrappers exist only where a cascade or rule exists (L524).
  - PIG `DATA.MAINTAIN.4`:
    - "per L541 to L544" became only L541's headline, "a sharded job of four decisions in order: batching key, work list, fan-out, observe and recover".
    - Dropped: the batching-key preference and keyset paging (L541); the work list generated from the data against skew (L542); the batch-level recovery design with a job log and idempotent retries (L543, partly kept); workers on disjoint rows, pool sized by connection, IO and lag headroom, a gradual ramp, and never sharding DDL (L544).
  - PIG `DATA.ORGANIZE.5`: "L508's list" became its positive half. L508's limits are dropped: no deep nesting beyond three levels, no binary content, bounded size for indivisible objects.
  - PIG `DATA.GUARD.1`: "for L494's list" became "for the listed cases", and no list follows. L494's CHECK cases (ranges, lengths, either-or exclusivity, conditional requirements, time ordering) are gone from the graph text.
- Proposed edit: one `apply --batch` of `node.set` ops with full constraint lists, restoring each dropped clause from the ledger row's statement in plain words (no ids). For example, GUARD.1: "CHECK: row-local and immutable, paired with NOT NULL, for ranges, lengths, either-or exclusivity, conditional requirements and time ordering; …".

**R-M4. Grounds attributed to the wrong source (faithfulness_drift).**
- PIG `DATA.INTERFACE.2`:
  - "Pool size from the pooler's documented formula". L199 gives the rule of thumb "cores x 2 plus effective spindles", and its note says "the formula is a heuristic from one T3 source; PostgreSQL docs only describe the settings". No pooler documents it.
  - Edit: "Pool size from the rule of thumb of cores x 2 plus effective spindles as a starting point, measured on the workload (a heuristic from one practitioner source)".
- PIG `DATA.INTERFACE.1`:
  - "the doctrine's view rules apply". L188 (owner/invoker rights, `security_invoker`, `security_barrier`) is a research row (DATA-C21, SRC-140), not maintainer doctrine. Calling it "the doctrine's" gives it a weight the max rule reserves for MAINT rows.
  - Edit: "the platform's view rules apply (…)".

**R-M5. The PIG owner of the read-visibility default lacks the consequence its copies now defer to (lost_content, P5 follow-through).** Node: PIG `LOGIC.SECURE.1`; affected: PIG `TRANSVERSE.SECURITY.1`, `TRANSVERSE.OPERABILITY.5`, `INTERACTION.REALTIME.4`, `INTERACTION.COLLABORATE.4`.
- Evidence: M6 made SECURE.1 the stack owner of the read-visibility default, and the four nodes now say "see PIG-WEB-LOGIC.SECURE.1". SECURE.1's constraints carry the default and the fallback but not the X1 consequence: "roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted". That sentence is now only in SECURE.1's design_notes, in phil GUARD.3, and, for the reporting role, in PIG DATA.GUARD.2.
  - SECURITY.1 now reads "no access-control requirement is marked met on a stronger guarantee than that default gives", without saying what the default gives.
  - REALTIME.4 lost "the change table … included".
  - `cross_branch_fixes.md` X1 asks that the consequence be stated "everywhere it matters".
- Proposed edit: add to SECURE.1's constraint list (full-list `node set`): "Consequence, stated so no line claims more: roles that may SELECT the base tables (reporting, operator) see every row, the change table, comments and notification rows included, unless their own role is restricted; per-role grants bound tables and columns, not users' rows."

## Minor

**r1. Garbled or dangling phrases left by id removal (format_artifact).**
- PIG `DATA.MAINTAIN.2`: "Per table, recorded (agree):", from "(P2, P3 agree)". Edit to "Per table, recorded:".
- PIG `INTERACTION.AGENT.5`: "(web-app-philosophy:INTERACTION.AGENT, a)", from "L652 a". Drop ", a".
- PIG `DATA.ORGANIZE.6`: "under the 'access need' criterion", which nothing defines (it was L513's). Edit: "under the doctrine's rule that a schema is justified by a business domain or an access need".
- PIG `TRANSVERSE.CONTRACTS.1`: "this settles the open question for the default context", whose question is no longer named. Edit: "this settles, for the default context, whether consumer-driven tests add value beyond schema checks for the team's own browser client".

**r2. A certainty marker lost in a move, and states left pointing at moved text (stale_annotation).**
- PIG `INTERACTION.ENVIRONMENT.1` now holds the draft-storage rules from VISUALIZE.2 and EDIT (per-tab or per-origin storage, clearing at submit or logout, per-tab only on sensitive pages) without their "(inferred)" marker. Its state does not mention them.
- VISUALIZE.2's state ("draft storage, its clearing and the per-tab rule for sensitive pages inferred") and EDIT's ("the per-tab draft rule inferred") still annotate text they no longer hold.
- Edit:
  - append "(storage choice, clearing and the per-tab rule inferred)" to the ENVIRONMENT.1 constraint;
  - add `| unvalidated: draft storage, clearing and the per-tab rule for sensitive pages (inferred)` to its state;
  - drop those clauses from the VISUALIZE.2 and EDIT states.

**r3. A rewrite reads as if the database verifies the actor (intent_quality).**
- Phil `ALLOCATION.GUARD.3`: "Functions read the acting user from a value scoped to the transaction, taken from the verified identity, refuse a write …".
- To the database the actor is a claim (J1 R1-3; the same constraint ends with "the claimed actor"); the backend is the one that took it from a verified identity.
- Edit: "Functions read the acting user that the backend asserted for the transaction from its verified identity, treat it as a claim, refuse a write …".

**r4. Owner approval stated three times in one node (duplication).**
- Phil `INTERACTION.AGENT` now has the lifted M9 constraint ("Irreversible or external effects require approval by the owning user …"), plus "consequential or external effects go through the approval design", plus "approval by the owning user for irreversible effects" inside the harmful-flows constraint.
- Edit: keep the lifted constraint; reduce the other two to "… go through the approval of irreversible or external effects above" and drop the clause from the flows line.

**r5. A T1 source called "a vendor article" (faithfulness_drift).**
- PIG `TRANSVERSE.PERFORMANCE`: "The budget numbers of a vendor article on performance budgets are not adopted."
- SRC-174 is web.dev's "Performance budgets 101", a T1 source. L296 rejects its sample numbers as tied to a past device baseline, not because of who wrote it.
- Edit: "The sample budget numbers of the performance-budget guide (tied to a past device baseline) are not adopted; the budget metrics are Core Web Vitals."

**r6. A stack detail dropped with the M6 move (lost_content).**
- PIG `INTERACTION.EDIT` handed its transaction rule to DATA.INTERFACE.1. Django's `atomic(durable=True)`, which asserts that the per-operation transaction is outermost, is now in no node; ENFORCE.2 has `transaction.atomic` without it.
- Edit: in ENFORCE.2's constraint, "(`transaction.atomic(durable=True)` around those two statements, asserting it is outermost, `ATOMIC_REQUESTS` off)".

**r7. L531's reasons relabelled (faithfulness_drift).**
- PIG `DATA.DERIVE.1`: "Of the reasons for JSON documents, the indivisible object and the flexible periphery are organizing choices …; only the derived summary is a copy". L531 lists three reasons to denormalize, of which the derived summary is not a JSON case.
- Edit: "Of the three legitimate reasons to denormalize, …".

## Confirmed after the fixes

Blocking and major findings of `critique.md`:
- **B1**:
  - TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 carry `undecided: awaiting maintainer, hosting model of the default context (recorded default …)`. Each recorded default matches J9 Q1: self-managed hosts; the proxy serves static files; the file fallback until a store is added.
  - TOPOLOGY, SECURITY, PIG-WEB-TRANSVERSE and ROOT carry it as `undecided (in children)`.
- **B2**: the link reads "…; views are never part of it.", kind `realizes` kept.
- **M1**:
  - SECURE.2 and SECURE.3 carry `undecided: awaiting maintainer, SameSite value of the session cookie`, with SECURE.3's inheritance note; SECURE and LOGIC carry it in children.
  - Link SECURE.3 → SECURE.2 created (`requires`).
- **M2**:
  - Phil ROOT state is `known (roll-up) | undecided (in children): …`.
  - Programmatic check: no ancestor of any holder lacks its clause in either graph (39, 4, 7 and 5 holders); one token form throughout.
- **M3**:
  - ROW_SECURITY's Authority line follows GUARD.3 R2 ("writer functions for per-user write rules …; Python backends for product policy … and identity; Postgres per consumer role"), and so does its intent.
  - Its inter link names the three layers; its "where used" mechanics are delegated to DATA.GUARD.3, which keeps all of them.
- **M4**: 131 of 131 PIG record pointers use the record notation; 128 resolve to headings, 3 to the deferred-node bullets.
- **M5**:
  - 0 ledger, judge, review, source or position ids in intents, constraints or examples.
  - The rewrites are faithful except R-M1, R-M3, R-M4, r5 and r7. Correct expansions include L581 (advisory-lock key), L540 (about 10^7 rows), L491 (junction tables), L498, L504 (UUID reasons), L529 ("code-written" `updated_at`), L535 and L537 (cache classification), L643 and L646.
- **M6**:
  - Owners hold the rules:
    - phil RULES.5 holds the one-call rule including cross-domain composition through published functions, so the ACT.1, LOGIC.ENFORCE and EVOLUTION.5 references resolve;
    - phil GUARD.3 holds the read-visibility default, fallback and consequence;
    - phil GUARD.3 and PIG ROW_SECURITY hold MD-01's conditions;
    - phil ACT.2 holds the foreign-mutation rule;
    - PIG ENVIRONMENT.1 holds page-hide saving;
    - phil GUARD.4 holds the cookie attributes.
  - Copies are one-line references with links. Gap: R-M5.
  - The m9 removals in 9 placements are all covered by their `Forbidden:` lines (ACT.4, DERIVE.1–.3, GUARD.2, GUARD.5, PRESENT.2, PRESENT.3, RECORD.1).
- **M7**:
  - 18 philosophy intra links, 22 PIG intra links and 13 inter links. Every sentence states the relation correctly, except R-M2.
  - Kinds are sensible: `requires` for dependencies, `refines` for RULES.2 → FORCES.1 and RULES.3 → FORCES.2, `realizes` for DATA.INTERFACE, `dataflow` for the trace id on history rows; no `conflicts`.
- **M8**:
  - `DATA.INTERFACE` ("Offered Contract") states J2's proposal faithfully. Its intent and constraints restate the RECORD.2 verdict at realization level with references, not copies.
  - Its state is `known: realization of … | gap: owns no ledger row`.
  - Links: `realizes` to RECORD.2 and ACT.1; PIG-WEB-DATA.INTERFACE refines it. DATA's intent and constraints list the fifth child, and DATA's gap is narrowed.
- **M9**: the five lifted clauses match their PIG sources.
  - COLLABORATE: stale write shown with both versions (EDIT); report queue (COLLABORATE.4, L689).
  - AGENT: approval by the owning user on the application's own page, with the agent host's dialog only a hint (AGENT.4).
  - PROCESS: no file readable before a clean scan (PROCESS.5).
  - SECURE: private, loopback and link-local addresses unreachable (SECURE.7).
  - MAINTAIN: recovery to a chosen moment, with restores rehearsed (MAINTAIN.5).
  - Each has a refining inter link back from the PIG node.
- **M10**: the roll-up constraints of PIG-WEB-INTERACTION, PIG-WEB-DATA, CONCURRENCY, DERIVE and REALTIME are the record roll-up text, split per child, word for word.
- **M11**: DATA.GUARD.3 is "Request Context and Row Security", with request context first and the MD-01 conditions delegated to ROW_SECURITY.
- **M12**: phil GUARD.3, GUARD.4 and LOGIC.SECURE say "scoped to the transaction"; the mechanism stays in PIG DATA.GUARD.3.

Minor findings m1 to m12:
- m1 and m2: 0 trailing artifacts, 0 first-person states.
- m3: philosophy keeps "JavaScript" (the browser platform) and generic "SQL", as reported.
- m4: no PIG uid in philosophy intent, state or constraints.
- m5: kinds changed (`constrains` ×2, `requires` ×1).
- m6: unconditional link sentence.
- m7: DATA, DATA.MAINTAIN and PROCESS.2 annotations updated.
- m8: GUARD's intent names concurrency and duplicate suppression; PIG-WEB-ALLOCATION names the type chain.
- m10: local constraint removed from INTERACTION.
- m11: dropped.
- m12: no "MUST"; TOPOLOGY.1 links its gap to SECURITY.2.
- Epistemic states: the 72 changed states differ from the pre-fix states only by the token normalization, the artifact and voice fixes, and the gaps that M8 and M9 closed.

## Sample checked against records or ledger (38 changed nodes, plus ALLOCATION.RULES.5)

- **Against the ledger row**:
  - PIG DATA: CONCURRENCY.3 (L581), MAINTAIN.4 (L540–L544), MAINTAIN.2 (L521–L524), INTERFACE.2 (L199), INTERFACE.1 (L188), GUARD.1 (L491, L494), GUARD.4 (L529), ORGANIZE.2 (L504), ORGANIZE.3 (L498), ORGANIZE.5 (L508), DERIVE.1 (L531), DERIVE.2 (L535, L537).
  - PIG elsewhere: INTERACTION.AGENT.3 (L643), INTERACTION.AGENT.4 (L646), TRANSVERSE.OPERABILITY.3 (L605), TRANSVERSE.PERFORMANCE (L296, SRC-174).
- **Against the judge record**:
  - PIG: INTERACTION.REALTIME.1 (J8 P2); INTERACTION.EDIT and LOGIC.SECURE.1 (J8, J7); ALLOCATION.ROW_SECURITY (J1 and GUARD.3 R2); DATA.GUARD.3 (J6); TRANSVERSE.SECURITY.1, OPERABILITY.5 (J9); INTERACTION.REALTIME.4, COLLABORATE.4 (J8).
  - Phil: LOGIC.EXPOSE.3 (J3 P1, P3); ALLOCATION.GUARD.3 and ALLOCATION.RULES.5 (J1); DATA.INTERFACE (J2's proposal in DATA).
  - PIG roll-ups: PIG-WEB-INTERACTION, PIG-WEB-DATA, DATA.CONCURRENCY, DATA.DERIVE, INTERACTION.REALTIME (record roll-ups).
- **Lifted clauses against their PIG source** (M9): phil INTERACTION.COLLABORATE, INTERACTION.AGENT, LOGIC.PROCESS, LOGIC.SECURE, DATA.MAINTAIN.
