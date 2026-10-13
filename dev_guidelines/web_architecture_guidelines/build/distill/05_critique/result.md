# Result: critique of the two built IntentGraphs

## L1 headline

The two graphs are faithful transcriptions of the final judge records and pass validation. Before rendering they still need two blocking fixes and twelve major ones; none of them re-judges a verdict.

Blocking:
- The hosting-model question is not marked "awaiting maintainer" on the three nodes that depend on it (PIG TOPOLOGY.3, TOPOLOGY.4, SECURITY.4).
- One link sentence says "functions and views are the interface", against the verdict that views are never contract objects.

Major, in short:
- SameSite lacks the shared "awaiting maintainer" token.
- Parent states, and both roots, hide their children's open questions.
- All 131 PIG judge-record pointers are unresolvable.
- Constraints are full of build ids.
- Cross-cutting rules are copied across peers instead of being linked.
- The graph has no links between placements and none between PIG tiers.
- Structure is missing: no philosophy node for the database function API; stack-neutral rules held only in the PIG; the PIG interaction roll-up drops four children; the request-context rule sits under "Row Security Policies".
- A Postgres mechanism ("transaction-local setting") appears in philosophy constraints.

Pinned:
- Issues: 26 = 2 blocking, 12 major, 12 minor. Details and proposed `ig-tool` edits: `critique.md`.
- By type: epistemic_gap 3, faithfulness_drift 2, conflict 1, traceability 1, intent_quality 4, duplication 2, missing_link 1, under_decomposition 1, pig_quality 1, rollup 2, projection_hints 3, link_kind 1, stale_annotation 1, format_artifact 3.
- Nodes sampled: 29 compared in full with their record plus 3 targeted checks, across every L1 branch of both graphs. All 211 epistemic states were compared mechanically, and all 211 intents read.
- Pointers: 1,894 resolved mechanically.
  - Research claims: 1,685 of 1,685 resolve.
  - Philosophy record pointers: 78 of 78 resolve.
  - PIG record pointers: 0 of 131 resolve.
  - Manual spot-check: 20 of 20 found and supporting their node.
- Questions: 3, each with a recommendation (add philosophy DATA.INTERFACE; lift stack-neutral PIG rules into the philosophy; align ROW_SECURITY with GUARD.3 R2).

### Re-check after fixes

All 26 findings are resolved as intended, and none reopened. The rewriting introduced 12 new issues: 0 blocking, 5 major, 7 minor (`recheck.md`). The 5 major ones:
- One rewrite inverts which position the buffering risk motivates: PIG REALTIME.1 now says "the SSE-only position" where the record has WebSocket-first.
- One new link turns a floor into a ceiling: EXPOSE.7 → SECURE.2 says "bounded by" the session timeout, where the record says "at least as long as".
- Four citation-to-prose rewrites keep only part of the cited rule while reading as complete: MAINTAIN.2, MAINTAIN.4, ORGANIZE.5, GUARD.1.
- Two grounds are attributed to the wrong source: a T3 heuristic called "the pooler's documented formula", and a research row called "the doctrine's".
- PIG SECURE.1, the new owner of the read-visibility default, lacks the consequence its four copies now defer to.

Pinned:
- Issues: 12 = 0 blocking, 5 major, 7 minor.
- By type: faithfulness_drift 6, lost_content 2, stale_annotation 1, format_artifact 1, intent_quality 1, duplication 1.
- Changed text read in full: 160 nodes, old beside new.
- Changed nodes checked against record or ledger: 38 (plus the unchanged owner RULES.5).
- Open-question tokens: on every ancestor of every holder (39, 4, 7 and 5 holders).
- Pointers: 1,898 of 1,901 resolve; the 3 others are the deferred-node bullets.
- Residual process ids in intent, constraints or examples: 0.

## L2 claims

Pinned:
- Issues: 26 = 2 blocking, 12 major, 12 minor (`critique.md`).
- Nodes sampled: 32 against their records (29 in full, 3 targeted); all 211 states compared mechanically; all intents and all 197 link intents read.
- Pointers checked: 1,894; 1,763 resolve. The 131 that fail are all PIG judge-record pointers, a uid-notation mismatch. Manual spot-check: 20 of 20.

What holds:
- Validation and faithfulness:
  - Both graphs validate against the manifest with 0 errors; every intra and inter link resolves (T1, T3).
  - Node names are all safe.
  - All 211 epistemic states equal their record's State line, apart from trailing-character artifacts.
  - The 29 full comparisons found intent and constraints transcribed faithfully, mostly word for word.
- Open clauses:
  - The read-visibility clause is on all 28 nodes where the records put it.
  - The deletion-default clause is on PIG MAINTAIN.2 and its ancestors.
- Language swap: no product name leaks into philosophy intent or constraints.

Blocking:
- **B1, epistemic_gap**:
  - J9's question 1 says the hosting model awaits the maintainer and that TOPOLOGY.3, TOPOLOGY.4 and SECURITY.4 depend on it.
  - J9's own convention requires the `undecided: awaiting maintainer` token on such nodes. The records omit it and so does the graph; TOPOLOGY.4 shows nothing at all.
  - Fix: add the clause to the three nodes and roll it up.
- **B2, faithfulness_drift**:
  - The inter link PIG DATA.INTERFACE.1 → phil RECORD.2 reads "Functions and views are the interface". RECORD.2, DB_API and INTERFACE.1 all forbid views as contract.
  - Fix: `link set` with a corrected sentence.

Major:
- **M1**: SameSite on PIG SECURE.2 reads "undecided … raised", without the "awaiting maintainer" token J7's question file asks for. SECURE.3 depends on it and is marked plain `known`.
- **M2**: phil ROOT has no epistemic state. Phil ALLOCATION, DATA, TRANSVERSE and TRANSVERSE.OPERABILITY, and PIG ROOT, LOGIC.ENFORCE, LOGIC.PROCESS and three TRANSVERSE roll-ups say `known` over children with open maintainer clauses, while other roll-ups carry them.
- **M3**: PIG ROW_SECURITY says per-user authorization is the backend's. J1's later GUARD.3 revision R2 gives per-user write rules to the writer function. This is an inconsistency inside J1's records, carried over.
- **M4**: every PIG node's judge-record pointer uses the built uid (`PIG-WEB-DATA…`), while the record headings use `PIG-WEB.DATA…`, so 0 of 131 resolve.
- **M5**: constraints carry build ids and narrative. In the PIG: 610 ledger ids, 108 judge-unit ids and 41 review ids, plus clauses such as "changed after review, M3" and "handed to J9". These belong in design_notes.
- **M6**: cross-cutting rules are copied across peers.
  - "One operation = one function call" sits in 9 nodes.
  - The read-visibility recorded default is written out in 12 nodes.
  - Also: MD-01's conditions, the foreign-mutation rule, page-hide saving and the cookie attributes.
  - Cause: the cross-branch fixes said "apply verbatim in every branch".
- **M7**: no intentlinks among ALLOCATION placements, rules and forces; none between PIG tiers. Several links that records name are absent; the strongest is SECURE.3 → SECURE.2.
- **M8**: the target hierarchy puts the database's function API under DATA, but the philosophy graph has no such node. J2 proposed DATA.INTERFACE; the skeleton declined it.
- **M9**: stack-neutral decisions exist only in the PIG: edit conflicts shown with both versions; owner approval of irreversible agent effects; mention visibility and report queue; scan before read; server-side-fetch guard; rehearsed point-in-time recovery.
- **M10**: the PIG-WEB-INTERACTION roll-up drops Edit, Real time, Collaborate and Environment, which its record rolls up. The J6 and J8 roll-ups have no constraints.
- **M11**: PIG DATA.GUARD.3 ("Row Security Policies") holds the always-on rule for passing the acting user.
- **M12**: philosophy GUARD.3, GUARD.4 and LOGIC.SECURE name "transaction-local setting", a Postgres mechanism.

Minor (12): trailing "`." or "." artifacts on 40 TRANSVERSE states; the judge's first person in 8 states; SQL, JSON, MCP and JavaScript wording in philosophy; product text naming PIG uids; two `conflicts` and one `refines` used for the wrong relation; one hedged link sentence; stale gap annotations; roll-ups that omit a child; Forbidden lists stated twice; a local constraint on a roll-up; an epistemic statement written as a constraint; mixed "MUST" style and a duplicated gap.

Questions, each with a recommendation:
1. Add philosophy DATA.INTERFACE as a realization node owning no row. Recommendation: yes.
2. Lift the stack-neutral PIG clauses into the philosophy tier nodes, word for word. Recommendation: yes; otherwise record each as a gap.
3. Align ROW_SECURITY's authority line with GUARD.3 R2. Recommendation: yes.

### Re-check after fixes

Pinned:
- Issues: 12 = 0 blocking, 5 major, 7 minor (`recheck.md`). Original findings: 26 of 26 resolved; 0 reopened.
- Sample:
  - 38 changed nodes checked against their judge record or ledger row, over the data, logic, interaction and transverse branches of both graphs.
  - All 160 nodes with changed intent, constraints or examples read old beside new.
  - All 72 changed states diffed clause by clause.
- Pointers: 1,901 checked, 1,898 resolve. The 3 others are the deferred nodes that J6 lists as bullets. All 1,685 research pointers resolve.

What the fixes got right:
- Open-question clauses:
  - B1 and M1: the hosting and SameSite clauses are now on their nodes with the shared token and their recorded defaults.
  - M2: a programmatic check finds no ancestor missing a descendant's clause in either graph.
- Links and pointers:
  - B2 and M3: the views link and ROW_SECURITY's authority line now follow the verdicts.
  - M4: the PIG record pointers resolve.
- Text cleaned and moved:
  - M5: no process ids remain in intents, constraints or examples. Most citation-to-prose rewrites state the ledger row faithfully: L581, L540, L491, L498, L504, L529, L535, L537, L643, L646.
  - M6: the six rules each sit with one owner; the copies are references with links. The nine m9 removals are covered by their Forbidden lines.
  - M7: 18 + 22 + 13 new links, every sentence right except one (R-M2); kinds sensible, no `conflicts`.
- New and restructured nodes:
  - M8: DATA.INTERFACE is faithful to J2's proposal and linked both ways.
  - M9: the five lifted clauses match their PIG sources.
  - M10: the roll-up constraints are the record roll-ups, word for word.
  - M11: the rename was applied. M12: the transaction wording is stack-neutral.

New issues, major:
- **R-M1** (PIG INTERACTION.REALTIME.1): "the buffering risk that motivates the SSE-only position"; J8's P2 is WebSocket-first, so the sentence inverts the record.
- **R-M2** (link EXPOSE.7 → SECURE.2): "bounded by the absolute session timeout"; the record and the node say "at least as long as" that timeout. My critique's "window bound" wording invited it.
- **R-M3**: four rewrites keep only part of the cited rows:
  - MAINTAIN.2 drops parts of L521 to L524 (reads filter on the marker, partial unique indexes, bulk confirmation flag, deletion time not before creation);
  - MAINTAIN.4 keeps L541's headline and drops L542 to L544;
  - ORGANIZE.5 drops L508's limits;
  - GUARD.1's "for the listed cases" lists nothing (L494's cases are gone).
- **R-M4**:
  - INTERFACE.2 calls L199's T3 rule of thumb "the pooler's documented formula";
  - INTERFACE.1 calls L188, a research row, "the doctrine's view rules".
- **R-M5** (PIG LOGIC.SECURE.1): it now owns the read-visibility default for the stack but lacks the X1 consequence (roles that may read base tables see every row) that SECURITY.1, OPERABILITY.5, REALTIME.4 and COLLABORATE.4 defer to.

New issues, minor:
- r1: four garbled or dangling phrases left by id removal: "(agree)", ", a)", "the 'access need' criterion", "the open question".
- r2: ENVIRONMENT.1 received the draft-storage rules without their "inferred" marker, while VISUALIZE.2 and EDIT keep annotating them.
- r3: phil GUARD.3 reads as if the database verifies the actor.
- r4: phil INTERACTION.AGENT states owner approval three times.
- r5: SRC-174 (web.dev, T1) is called "a vendor article".
- r6: Django's `atomic(durable=True)` was lost in the EDIT move.
- r7: L531's reasons to denormalize are relabelled "reasons for JSON documents".

## L3 full

The full issue list, with node uids, evidence and proposed `ig-tool` operations, the three questions with what happens if unanswered, and the method and sample lists, is in `critique.md` in this folder. Summary of each issue at claim level:

Pinned:
- Issues: 26 = 2 blocking, 12 major, 12 minor; by type as in L1.
- Nodes sampled:
  - Philosophy (16): ALLOCATION, ALLOCATION.FORCES.5, ALLOCATION.RECORD.2, ALLOCATION.GUARD.3, ALLOCATION.GUARD.4, ALLOCATION.PRESENT.1, DATA, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE, LOGIC, LOGIC.EXPOSE.2, INTERACTION, INTERACTION.ENVIRONMENT.6, TRANSVERSE.CONTRACTS, TRANSVERSE.EVOLUTION.3.
  - PIG (13): ROOT, ALLOCATION.ROW_SECURITY, ALLOCATION.DB_API, DATA.GUARD.3, DATA.MAINTAIN.2, LOGIC.SECURE.2, LOGIC.SECURE.3, LOGIC.EXPOSE.7, PIG-WEB-INTERACTION, INTERACTION.EDIT, INTERACTION.AGENT.1, TRANSVERSE.TOPOLOGY.3, TRANSVERSE.CONTRACTS.2.
  - Targeted checks (3): DATA.INTERFACE.1, LOGIC.PROCESS.2, TRANSVERSE.SECURITY.4.
  - Plus all 211 states compared mechanically and all intents read.
- Pointers: 1,894 checked; 1,685 of 1,685 research and 78 of 78 philosophy-record pointers resolve; 0 of 131 PIG-record pointers resolve; manual spot-check 20 of 20.

| Id | Sev | Type | Nodes | Claim |
|---|---|---|---|---|
| B1 | blocking | epistemic_gap | PIG TOPOLOGY.3, .4, SECURITY.4 (+ roll-ups) | Hosting-model clause "awaiting maintainer" missing where J9 Q1 says these defaults depend on it |
| B2 | blocking | faithfulness_drift | link PIG DATA.INTERFACE.1 → RECORD.2 | "Functions and views are the interface" contradicts "views never contract" |
| M1 | major | epistemic_gap | PIG SECURE.2, SECURE.3, SECURE, LOGIC | SameSite clause without the shared token; the dependent CSRF node unmarked |
| M2 | major | epistemic_gap | phil ROOT, ALLOCATION, DATA, TRANSVERSE(.OPERABILITY); PIG ROOT, ENFORCE, PROCESS, TRANSVERSE(.SECURITY, .OPERABILITY) | Roll-up states hide children's open clauses; phil ROOT has no state |
| M3 | major | conflict | PIG ROW_SECURITY (+ its link) | "Python backends per user" authority vs GUARD.3 R2 writer functions |
| M4 | major | traceability | 131 PIG nodes | Record pointers use the built uid; the record headings use the original notation |
| M5 | major | intent_quality | 73 PIG and 19 phil nodes | Ledger, judge and review ids and build narrative inside constraints |
| M6 | major | duplication | 9 + 12 + 3 + 2 + 3 + 2 nodes | One-call rule, read-visibility default, MD-01 conditions, foreign mutations, page-hide saving and cookie attributes copied across peers |
| M7 | major | missing_link | ALLOCATION internals; PIG tiers; 4 inter | No placement-to-rule or tier-to-tier links; SECURE.3 → SECURE.2 the most needed |
| M8 | major | under_decomposition | phil DATA | No node for the database function API that the target hierarchy places under DATA |
| M9 | major | pig_quality | PIG EDIT, AGENT.4, COLLABORATE.4, PROCESS.5, SECURE.7, MAINTAIN.5 | Stack-neutral rules held only in the projection |
| M10 | major | rollup | PIG-WEB-INTERACTION; J6 and J8 roll-ups | Roll-up drops 4 of 6 children present in its record; no constraints |
| M11 | major | intent_quality | PIG DATA.GUARD.3 | Always-on request-context rule under a "row security" name |
| M12 | major | projection_hints | phil GUARD.3, GUARD.4, LOGIC.SECURE | "Transaction-local setting" is a Postgres mechanism |
| m1 | minor | format_artifact | 13 phil + 27 PIG TRANSVERSE states | Trailing "`." or "." |
| m2 | minor | format_artifact | 8 states | Judge's first person ("mine", "my choice") |
| m3 | minor | projection_hints | ~12 phil nodes | SQL keywords, fixed JSON, MCP example, "JavaScript-readable" |
| m4 | minor | projection_hints | phil COLLABORATE, EXPOSE.3, CONTRACTS | Product text names PIG uids |
| m5 | minor | link_kind | 2 conflicts, 1 refines | Complementary logs marked conflicts; "rests on" marked refines |
| m6 | minor | faithfulness_drift | link DATA.MAINTAIN → RECORD.3 | Hedged "when the placement makes it the origin" |
| m7 | minor | stale_annotation | phil DATA, DATA.MAINTAIN; PIG PROCESS.2 | Gaps and tension notes overtaken by created links and J1 R3 |
| m8 | minor | rollup | phil ALLOCATION.GUARD; PIG ALLOCATION | Children omitted; a clause no child holds |
| m9 | minor | duplication | placement nodes | Forbidden list stated twice |
| m10 | minor | intent_quality | phil INTERACTION, INTERACTION.VISUALIZE | Local constraint on a roll-up; formatting duplicated from PRESENT.2 |
| m11 | minor | intent_quality | phil ALLOCATION.FORCES.5 | Epistemic statement as a constraint |
| m12 | minor | format_artifact | phil TRANSVERSE; PIG SECURITY.2, TOPOLOGY.1 | "MUST" style in one branch; duplicated gap |

Method: the ig-critic role with its PIG module; graphs read only through `ig-tool` (validate with manifest, tree, structure, overview, node and links queries) plus two narrow greps of the graph files for link kinds; read-only comparison scripts over the `ig-tool` outputs and the records. Nothing outside this folder was written.
