# Critique of the two built IntentGraphs (web-app-philosophy, pig-web-defaults)

This is an IntentGraph critique (ig-critic role, product and PIG review modules) of `intent_graphs/web_app_philosophy.ig.yaml` (79 nodes) and `intent_graphs/web_defaults.ig.yaml` (132 nodes), before the human-readable guideline is rendered from them. It checks structure, semantics and faithfulness to `build/distill/target_hierarchy.md`, `build/distill/maintainer_decisions.md` (MD-01 to MD-03) and the final judge records `build/distill/03_judge/J*/records.md`. It does not re-judge any verdict. Read-only: no graph was modified.

Paths are relative to the guideline folder. In the commands, `$PHIL` = `intent_graphs/web_app_philosophy.ig.yaml` and `$PIG` = `intent_graphs/web_defaults.ig.yaml`. Every mutating command takes `-o` set to the same file, plus `--role critic-fix -m "<why>"`. They are left out below for brevity. PIG uids are written without the `PIG-WEB-` prefix where the graph is obvious.

Pinned:
- Issues: 26 in all: 2 blocking, 12 major, 12 minor.
  - Blocking: B1, the hosting-model clause "awaiting maintainer" is missing on the nodes that J9 Q1 says depend on it (TOPOLOGY.3, TOPOLOGY.4, SECURITY.4). B2, a link intent says "Functions and views are the interface", against the verdict that views are never contract objects.
  - Major: M1 SameSite clause without the shared token; M2 parent states that drop their children's open clauses (phil ROOT has no state); M3 ROW_SECURITY authority line contradicts GUARD.3 R2; M4 all 131 PIG judge-record pointers unresolvable; M5 build-process ids in constraints; M6 cross-cutting rules restated across peers; M7 missing intentlinks; M8 no philosophy node for the database function API; M9 stack-neutral decisions held only in the PIG; M10 the PIG-WEB-INTERACTION roll-up drops 4 of 6 children; M11 request-context rule housed under "Row Security Policies"; M12 "transaction-local setting" in philosophy constraints.
- By type: epistemic_gap 3, faithfulness_drift 2, conflict 1, traceability 1, intent_quality 4, duplication 2, missing_link 1, under_decomposition 1, pig_quality 1, rollup 2, projection_hints 3, link_kind 1, stale_annotation 1, format_artifact 3.
- Validation: both graphs `ig-tool validate -m intent_graphs/intent_resources.yaml`: 0 errors, 0 warnings. 42 + 21 intra links and 15 + 119 inter links all resolve (T1, T3 hold).
- Faithfulness:
  - Epistemic states: 211 of 211 compared mechanically with the record's State line. All match verbatim apart from format artifacts (m1) and the uid notation from `04_build/uid_mapping.md`.
  - Intent and constraints: 29 nodes compared in full with their record's Decision, plus 3 targeted checks, across every L1 branch of both graphs. All are faithful transcriptions, apart from B2, M10 and the inherited inconsistency M3.
- Awaiting-maintainer clauses:
  - Read visibility: present on all 28 nodes where the records put the token (9 philosophy, 19 PIG), plus phil ALLOCATION.RULES.4, which records it as a conflict.
  - Deletion default: present on MAINTAIN.2 and both of its PIG ancestors.
  - SameSite: present as `undecided: SameSite …`, without the `awaiting maintainer` token (M1).
  - Hosting model: absent as a clause; only "unvalidated: hosting assumption (Q1)" on TOPOLOGY.3 (B1).
- Language swap: no product name (Postgres, Python, Django, Redis…) in philosophy intent or constraints. Mechanism leaks: M12 and m3.
- Node names: 211 of 211 free of `/ \ : * ? " < > | [ ] # ^`. The five philosophy names the link batch had overwritten with python-kb ids were restored (`04_build/links/fix_names.yaml`); the current names are clean.
- impl_pointers: 1,894 resolved mechanically.
  - Research claims: 1,685 of 1,685 resolve.
  - Philosophy judge records: 78 of 78 resolve.
  - PIG judge records: 0 of 131 resolve (M4).
  - Manual spot-check: 20 random pointers, 20 of 20 exist and support their node.

## Blocking

**B1. Hosting-model clause missing (epistemic_gap).** Nodes: PIG `TRANSVERSE.TOPOLOGY.3`, `TRANSVERSE.TOPOLOGY.4`, `TRANSVERSE.SECURITY.4`, and their ancestors `TRANSVERSE.TOPOLOGY`, `TRANSVERSE.SECURITY`, `PIG-WEB-TRANSVERSE`, `ROOT`.
- Evidence: J9's question file (`03_judge/J9_pig_transverse/questions.md`, Q1) says the hosting model is "awaiting maintainer" and that three defaults depend on it: process replication (TOPOLOGY.3), static files (TOPOLOGY.4) and secrets (SECURITY.4). J9's own How-to-read defines `| undecided: awaiting maintainer, X` as "a clause of a decided node that waits on an open maintainer question; the same token in every unit, so the graph builder finds every node the answer changes". J9's State lines leave the token out, and the graph copies them:
  - TOPOLOGY.3 has only `unvalidated: hosting assumption (Q1)`;
  - SECURITY.4 mentions "the assumed hosting";
  - TOPOLOGY.4 says nothing.
- Effect: a renderer, or a reader searching for the open maintainer questions, finds three of the four and presents hosting-dependent defaults as settled.
- Proposed edit (states otherwise unchanged):
  - `ig-tool node set -g $PIG --uid PIG-WEB-TRANSVERSE.TOPOLOGY.3 --epistemic-state "known | conflict: L157 contested, settled by hosting model | undecided: awaiting maintainer, hosting model of the default context (J9 Q1; recorded default: one or a few self-managed hosts without a container orchestrator) | unvalidated: roles per kind of process"`
  - `ig-tool node set -g $PIG --uid PIG-WEB-TRANSVERSE.TOPOLOGY.4 --epistemic-state "known | undecided: awaiting maintainer, hosting model of the default context (J9 Q1; recorded default: the proxy on the application host serves static files) | unvalidated: cumulative asset store across the compatibility window; CDN threshold (L165)"`
  - `ig-tool node set -g $PIG --uid PIG-WEB-TRANSVERSE.SECURITY.4 --epistemic-state "known | conflict: L350 contested (environment variables against a managed store), reconciled by authority and delivery | undecided: awaiting maintainer, hosting model of the default context (J9 Q1; recorded default: the file fallback is in force until a managed store is added) | unvalidated: the reconciliation; credentials per consumer role"`
  - Roll-ups: append `| undecided (child): awaiting maintainer, hosting model (TOPOLOGY.3, .4, SECURITY.4)` to `TRANSVERSE.TOPOLOGY`, `TRANSVERSE.SECURITY` and `PIG-WEB-TRANSVERSE` (see M2 for ROOT).

**B2. A link intent contradicts the function-API verdict (faithfulness_drift).** Link `pig-web-defaults:PIG-WEB-DATA.INTERFACE.1 → web-app-philosophy:ALLOCATION.RECORD.2` (shape `realizes`).
- Evidence: the link intent reads "Functions and views are the interface through which consumers reach data." Three sources say the opposite:
  - RECORD.2: "Forbidden: … views as contract";
  - DB_API: "views are never contract objects";
  - INTERFACE.1's own record: "Views are never contract objects (L516; DB_API)", with P5 "views as contract" rejected.
- The node name "Functions and Views" comes from the skeleton; the link sentence turned it into a claim.
- Proposed edit: `ig-tool link set -g $PIG --uid "pig-web-defaults:PIG-WEB-DATA.INTERFACE.1_web-app-philosophy:ALLOCATION.RECORD.2" --intent "The database functions in the API schema are the interface through which consumers reach data; views are never part of it."` If `link set` does not reach inter links, `link remove` the link and `link create` it again with the same qualified endpoints and `--shape '{"type":"realizes"}'`, as the link builder did.

## Major

**M1. SameSite clause without the shared token, and its dependant unmarked (epistemic_gap).** Nodes: PIG `LOGIC.SECURE.2`, `LOGIC.SECURE.3`, `LOGIC.SECURE`, `PIG-WEB-LOGIC`.
- Evidence: J7's questions file says that, if unanswered, the guideline "records the recommendation as the default, marked as awaiting the maintainer". The State lines (and the graph) read `undecided: SameSite on the session cookie (raised; …)`, so a search for `awaiting maintainer` misses it. SECURE.3 (CSRF) uses "the session cookie's explicit SameSite value (SECURE.2) as a second layer", yet its state is plain `known`.
- Proposed edit:
  - SECURE.2: replace `undecided: SameSite on the session cookie (raised; …)` with `undecided: awaiting maintainer, SameSite value of the session cookie (J7 question; recorded default Lax plus a cross-site navigation check, Strict for operator consoles)`.
  - SECURE.3: `ig-tool node set -g $PIG --uid PIG-WEB-LOGIC.SECURE.3 --epistemic-state "known | undecided: awaiting maintainer, SameSite value of the session cookie (inherited from SECURE.2; this node holds whatever value is chosen as the second layer) | unvalidated: the cookie and bearer endpoints kept apart (inferred)"`.
  - SECURE and PIG-WEB-LOGIC: use the same token in their `undecided: SameSite …` clause.
  - Add the link of M7(b).

**M2. Parent epistemic states drop their children's open clauses; phil ROOT has none (epistemic_gap, P3, LOD invariant 2).**
- Evidence:
  - Phil `ROOT` has no `epistemic_state` (the primer reads that as "unassessed").
  - These roll-ups say `known` while a child carries `undecided: awaiting maintainer`:
    - phil `ALLOCATION` (GUARD), `DATA` (DATA.GUARD), `TRANSVERSE` (SECURITY, OPERABILITY.2), `TRANSVERSE.OPERABILITY` (OPERABILITY.2);
    - PIG `ROOT` (four open questions below it), `LOGIC.ENFORCE` (ENFORCE.3), `LOGIC.PROCESS` (PROCESS.6), `PIG-WEB-TRANSVERSE`, `TRANSVERSE.SECURITY` (SECURITY.1), `TRANSVERSE.OPERABILITY` (OPERABILITY.5).
  - Other roll-ups do carry the clause (phil LOGIC, INTERACTION, ALLOCATION.GUARD; PIG DATA, LOGIC, INTERACTION, ALLOCATION).
  - So the graph is faithful to each record but inconsistent as a whole: a reader at L1 or ROOT cannot see that maintainer questions remain.
  - Separately, PIG `PIG-WEB-ALLOCATION` carries the read-visibility clause although none of its children does (m8).
- Proposed edit:
  - Phil ROOT: `ig-tool node set -g $PHIL --uid ROOT --epistemic-state "known (roll-up) | undecided (in children): awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (ALLOCATION.GUARD.3)"`.
  - PIG ROOT: `ig-tool node set -g $PIG --uid ROOT --epistemic-state "known (roll-up) | undecided (in children): awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (PIG-WEB-LOGIC.SECURE.1, PIG-WEB-DATA.GUARD) | undecided (in children): awaiting maintainer, default deletion for user-facing transactional data (PIG-WEB-DATA.MAINTAIN.2) | undecided (in children): awaiting maintainer, SameSite value of the session cookie (PIG-WEB-LOGIC.SECURE.2) | undecided (in children): awaiting maintainer, hosting model of the default context (PIG-WEB-TRANSVERSE.TOPOLOGY.3)"`.
  - Each listed roll-up: append `| undecided (in children): awaiting maintainer, <clause> (<child uid>)`.

**M3. ROW_SECURITY's authority line contradicts GUARD.3 revision R2 (conflict).** Node: PIG `ALLOCATION.ROW_SECURITY`; link `ROW_SECURITY → web-app-philosophy:ALLOCATION.GUARD.3`.
- Evidence: the intent says "authorization stays a backend decision with per-role database privileges as the second gate". The constraint says "Authority: Python backends per user; Postgres per role". The link says "the default placement is per-role grants plus backend checks".
  - J1's GUARD.3, revision R2, moved per-user write rules decidable from the row to the column's writer function. Its constraint reads "Authority: writer function for per-user write rules …; backend for product policy …; database per consumer role".
  - The ROW_SECURITY record (also J1) still carries the pre-R2 MD-01 wording, so the graph transcribes an inconsistency inside J1's own records.
  - MD-01 itself says "the allocation verdict for authorization stands", and that verdict is GUARD.3.
- Proposed edit: align with GUARD.3 R2 (question 3 below). Pass the full constraint list with the Authority line replaced by `'Authority: writer functions for per-user write rules decidable from the row and the actor; Python backends for product policy not stored in the data and for identity; Postgres per consumer role (GUARD.3)'`; replace the intent's first clause with "authorization follows GUARD.3's layers (writer functions, backend policy, per-role privileges)"; `link set` the inter link to "Row-level policies are not the default way to place authorization; the default is GUARD.3's layers: writer functions, backend policy checks and per-role grants."

**M4. Every PIG judge-record pointer is unresolvable (traceability).** Nodes: all 131 non-root PIG nodes.
- Evidence: each PIG node's first pointer is `build/distill/03_judge/J<n>_<unit>/records.md::PIG-WEB-<AREA>…` (built uid), while every record heading uses `PIG-WEB.<AREA>…` (`04_build/uid_mapping.md`: "Judge records and the skeleton keep the original notation"). 0 of 131 resolve; all 78 philosophy record pointers and all 1,685 research-claim pointers resolve. A verifier applying the grounding check (PRIMER_04 §Critique) would classify all 131 as hallucinated.
- Proposed edit: one `apply --batch` with a `node.set` op per PIG node whose `impl_pointers` is the current list with the first entry's symbol rewritten `PIG-WEB-<AREA>` → `PIG-WEB.<AREA>` (`--impl-pointer` and the batch field replace the whole list; run `--dry-run` first). Example: `ig-tool node set -g $PIG --uid PIG-WEB-ALLOCATION.ROW_SECURITY --impl-pointer "build/distill/03_judge/J1_allocation/records.md::PIG-WEB.ALLOCATION.ROW_SECURITY"` (this node has a single pointer).

**M5. Build-process references inside constraints (intent_quality, regenerability).** Both graphs, mostly PIG.
- Evidence: the brief makes `constraints` "the verdict's MUST rules, one per line", with evidence and provenance in `design_notes`. Counted in intent and constraints:
  - PIG: 610 ledger-row ids `L###` in 73 nodes; 108 judge-unit ids (`J1`…`J9`) in 51 nodes; 41 review or fix ids (`R1-4`, `X2`, `M3`, `m6`) in 23 nodes; 5 `SRC-` ids.
  - Phil: ledger ids in 19 nodes, judge-unit ids in 4, review or fix ids in 7.
  - Build narrative shows up as constraint text, for example:
    - DATA.MAINTAIN.2 "(changed after review, M3)" and "(changed after review, M2: it was a check in the writer functions only)";
    - CONCURRENCY.2 "console tooling handed to J9";
    - TOPOLOGY.3 "questions.md, Q1";
    - phil DATA.GUARD "The default isolation level belongs to J6";
    - AGENT.1 "J4 AGENT", "J4 ENVIRONMENT.3", where a philosophy uid is meant.
  - These render into the guideline as noise or dangling references.
- Proposed edit (mechanical, no meaning change), one `apply --batch` per graph of `node.set` ops with full constraint lists:
  - remove parenthesised ledger, source, judge and review ids from constraints (they stay in `design_notes` and `impl_pointers`);
  - replace `J<n> <UID>` with the qualified uid (`web-app-philosophy:INTERACTION.ENVIRONMENT.3`);
  - delete the "changed after review" and "handed to" clauses;
  - keep `MD-0n` only where the maintainer decision is the reason, and define MD-01 to MD-03 once in each ROOT's `design_notes`.

**M6. Cross-cutting rules restated across peers instead of stated once and linked (duplication, P5).**
- Evidence:
  - "One business operation is one database function call in its own transaction; backends never compose calls" is stated in 9 nodes (phil ACT.1, RULES.5, DATA.GUARD, LOGIC, LOGIC.ENFORCE; PIG DB_API, DATA.INTERFACE.1, INTERACTION.EDIT, TRANSVERSE.EVOLUTION.2), and in EDIT it is plainly outside the node's scope.
  - The read-visibility recorded default (shared written specification, denial suite, fallback, SELECT consequence) is written out in 12 nodes.
  - MD-01's three conditions are restated in full in phil GUARD.3 and in PIG ROW_SECURITY and DATA.GUARD.3; DATA.ORGANIZE.6 and phil DATA.GUARD refer to them.
  - The foreign-mutation rule (worker behind 202, in-request only within about 1 s with the intent recorded first) is restated in ACT.2 and ACT.3.
  - Saving unsaved input on page hide is stated in three PIG leaves (EDIT, ENVIRONMENT.1, VISUALIZE.2), beside its philosophy owner ENVIRONMENT.2 and the PIG roll-up ENVIRONMENT.
  - The cookie attributes (HttpOnly, Secure, SameSite, opaque id) are stated in phil GUARD.4 and ENVIRONMENT.7.
  - Root cause: `03_judge/cross_branch_fixes.md` says "apply verbatim in every branch". That is right for records, wrong for a normalized graph.
- Proposed edit: keep each rule at its owner and replace the copies with a one-line reference plus an intentlink.

  | Rule | Owner | Copies |
  |---|---|---|
  | One call per operation | phil RULES.5; PIG DATA.INTERFACE.1 | the rest |
  | Read-visibility default | phil GUARD.3 | others keep only the `undecided` token and "see ALLOCATION.GUARD.3" |
  | MD-01 conditions | phil GUARD.3; PIG ROW_SECURITY | the rest |
  | Foreign mutations | phil ACT.2 | ACT.3 keeps "except ACT.2's in-request phase" |
  | Page-hide saving | PIG ENVIRONMENT.1 | EDIT, VISUALIZE.2 |
  | Cookie attributes | phil GUARD.4 | the rest |

  Example: drop EDIT's last constraint ("Transactions (P5 under MD-03) …") and its last intent clause, then `ig-tool link create -g $PIG --src PIG-WEB-INTERACTION.EDIT --dst PIG-WEB-DATA.INTERFACE.1 --intent "Each edit is one call of the function API, in its own transaction." --shape '{"type":"requires"}'`.

**M7. Missing intentlinks (missing_link).** The tree is linked only tier → placement.
- (a) Philosophy: there are 0 links among ALLOCATION nodes, although the placements apply the rules and forces by name. Create, each with `--shape '{"type":"requires"}'` unless noted:
  - `ALLOCATION.ACT.1 → ALLOCATION.RULES.5` ("each operation is one transaction");
  - `ALLOCATION.ACT.3 → ALLOCATION.ACT.2` ("defers foreign mutations under the side-effect placement's rule");
  - `ALLOCATION.GUARD.1 → ALLOCATION.RULES.1` ("early validators are tested copies");
  - `ALLOCATION.GUARD.3 → ALLOCATION.RULES.3`;
  - `ALLOCATION.DERIVE.3 → ALLOCATION.RULES.1`;
  - `ALLOCATION.RECORD.2 → ALLOCATION.RULES.4`;
  - `ALLOCATION.RULES.2 → ALLOCATION.FORCES.1` and `ALLOCATION.RULES.3 → ALLOCATION.FORCES.2` (`refines`: "the first two rules are the correctness and security vetoes", from the RULES intent).
- Philosophy tier links that records name but that are absent:
  - `LOGIC.ENFORCE → ALLOCATION.RULES.5`;
  - `LOGIC.EXPOSE.2 → ALLOCATION.GUARD.4` (its recorded tension);
  - `LOGIC.EXPOSE.3 → ALLOCATION.PRESENT.1` (its state: "browser half (PRESENT.1)");
  - `TRANSVERSE.OPERABILITY.2 → ALLOCATION.GUARD.2` and `→ ALLOCATION.GUARD.3` (concurrency tests and denial tests, from its state);
  - `TRANSVERSE.SECURITY → ALLOCATION.GUARD.3`;
  - `TRANSVERSE.EVOLUTION.3 → ALLOCATION.RECORD.2`.
- (b) PIG tier to tier: there are 0 such links. These carry the stack's main dataflows:
  - `LOGIC.SECURE.3 → LOGIC.SECURE.2` (SameSite second layer; needed for M1);
  - `LOGIC.ENFORCE.2 → DATA.CONCURRENCY.1` (whole-call retry on serialization failure);
  - `LOGIC.ENFORCE.3 → DATA.INTERFACE.1` (typed wrappers of API functions);
  - `INTERACTION.REALTIME.2 → DATA.CONCURRENCY.5` (commit-safe cursor);
  - `INTERACTION.REALTIME.4 → LOGIC.SECURE.2` (session cookie authenticates the channel);
  - `TRANSVERSE.OPERABILITY.1 → DATA.MAINTAIN.3` (trace id on history rows);
  - `LOGIC.PROCESS.6 → LOGIC.PROCESS.5` (serve only available files);
  - `LOGIC.PROCESS.7 → LOGIC.PROCESS.2` and `→ LOGIC.SECURE.6` (its intent says it inherits them);
  - `LOGIC.SECURE.6 → TRANSVERSE.TOPOLOGY.1` (proxy-layer limits);
  - `LOGIC.EXPOSE.7 → LOGIC.SECURE.2` (window bound = absolute session timeout).
- (c) PIG to philosophy:
  - `LOGIC.EXPOSE.7 → web-app-philosophy:INTERACTION.ENVIRONMENT.3`;
  - `TRANSVERSE.TOPOLOGY.4 → web-app-philosophy:INTERACTION.ENVIRONMENT.3` (assets kept for the compatibility window);
  - `TRANSVERSE.CONTRACTS.2 → web-app-philosophy:ALLOCATION.RECORD.3` (`conflicts` is not right here: use `requires`, "rejects L564's direction because RECORD.3 makes the schema the origin");
  - `LOGIC.SECURE.3 → web-app-philosophy:INTERACTION.ENVIRONMENT.7`.
- The link builder skipped (a) and (b) deliberately as "citations, not links" (`04_build/links/result.md`). The primer counts them as dependencies (PRIMER_01, misreading 5). Batch them: intra with `apply --batch` `link.create`; inter one by one with `ig-tool link create`.

**M8. No philosophy node for the database function API (under_decomposition; faithfulness to the target hierarchy).** Node: phil `DATA`.
- Evidence: `target_hierarchy.md`: "A contract sits with the role that offers it (the database's function API under DATA, the backend's interface under LOGIC)". MD-03 makes it "the default contract to the data". The philosophy DATA branch has organize, guard, maintain and derive, but no node offering the contract. DATA's state records the gap; J2 proposed `DATA.INTERFACE` ("judged as a realization of J1's verdicts because it would own no row"); the skeleton declined ("inventing one would add a node without grounds"); the link builder skipped its links. LOGIC has its interface node (LOGIC.EXPOSE) and DATA does not, so the rendered philosophy is asymmetric on the very point MD-03 decides.
- Proposed edit (question 1): `ig-tool node create -g $PHIL --uid DATA.INTERFACE --parent DATA --name "Offered Contract" --intent "<J2's proposal: the database offers every consumer a function API owned by the database owner, one business operation per call, one role per consumer, evolving additively (realization of RECORD.2 and the database share of ACT.1)>" --epistemic-state "known: realization of J1 RECORD.2 and ACT.1 under MD-03 | gap: owns no ledger row" --impl-pointer "build/distill/03_judge/J2_phil_data/records.md::DATA"`. Then link it `realizes` to `ALLOCATION.RECORD.2` and `ALLOCATION.ACT.1`, link `PIG-WEB-DATA.INTERFACE` to it (`refines`), and drop "RECORD.2, the database share of ACT.1" from DATA's gap clause.

**M9. Stack-neutral product decisions live only in the PIG (pig_quality; reverse language-swap).**
- Evidence: under the language-swap test these clauses survive any stack change, yet they exist only in projection nodes, so a second PIG (another stack) would silently lose them:
  - INTERACTION.EDIT: "a stale write is shown as a conflict with both versions and is never merged silently";
  - INTERACTION.AGENT.4: irreversible or external effects need the owning user's approval, on the application's own page, checked by the effect's writer;
  - INTERACTION.COLLABORATE.4: mentions notify only recipients who may see the target; a report queue whenever outsiders read comments;
  - LOGIC.PROCESS.5: no file readable before a clean scan;
  - LOGIC.SECURE.7: server-side fetches cannot reach internal addresses;
  - DATA.MAINTAIN.5: point-in-time recovery, with backups that count only once a restore has been rehearsed.
- The philosophy tier nodes cover their neighbourhood only in general terms (for example INTERACTION.AGENT: "harmful flows are protected by name").
- Proposed edit (question 2): lift each stack-neutral clause, word for word, as one constraint on the existing philosophy tier node, citing the PIG record in its design_notes, with no re-judging:
  - EDIT's clause → INTERACTION.COLLABORATE, or a new INTERACTION.EDIT if the maintainer wants the target hierarchy's "edit" verb filled;
  - AGENT.4 → INTERACTION.AGENT;
  - COLLABORATE.4 → INTERACTION.COLLABORATE;
  - PROCESS.5 → LOGIC.PROCESS;
  - SECURE.7 → LOGIC.SECURE;
  - MAINTAIN.5 → DATA.MAINTAIN (which also narrows DATA's "data lifecycle has no principle row" gap).
- Otherwise, record each clause as `| gap: stack-neutral rule held only in pig-web-defaults (<uid>)` on the philosophy node.

**M10. The PIG-WEB-INTERACTION roll-up drops four of its six children (rollup, P2/T4).** Node: PIG `PIG-WEB-INTERACTION`; also the PIG roll-ups without constraints.
- Evidence: J8's record rolls up all six children (Visualize, Edit, Real time, Collaborate, Agent, Environment), one line each. The graph intent keeps the general sentence plus rendering and agents; Edit, Real time, Collaborate and Environment are absent, and the node has no constraints, so it cannot be read alone (PRIMER_01 "test for correct parent").
  - The J6 and J8 roll-ups (PIG-WEB-DATA and its six L2 parents; PIG-WEB-INTERACTION and its five L2 parents) carry no constraints.
  - The philosophy roll-ups and the other PIG roll-ups carry one constraint per child.
- Proposed edit: `ig-tool node set -g $PIG --uid PIG-WEB-INTERACTION` with `--constraints`, one per child, copying the six record bullets word for word ("Visualize: per-request HTML from Python, …", "Edit: POST, then 303; …", "Real time: …", "Collaborate: …", "Agent: …", "Environment: …"). Do the same, from their records' Decision bullets, for the J6 and J8 L2 roll-ups.

**M11. The request-context rule is housed under "Row Security Policies" (intent_quality: scope beyond the name).** Node: PIG `DATA.GUARD.3`.
- Evidence: two of its four constraints and half its intent cover how the acting user (and the person an agent acts for) travels as transaction-local settings, which writer functions and audit triggers require "row security or not". That rule is used by GUARD.2, INTERFACE.2, ENFORCE.2, MAINTAIN.3 and OPERABILITY.1, and the inter link `DATA.GUARD.3 → ALLOCATION.ACT.4` exists only because of it. A reader of the rendered guideline skips "Row Security Policies" as not applicable (row security is off by default) and misses an always-on rule. Faithful to J6; the problem is the home, not the text.
- Proposed edit, either option:
  - (cheapest) `ig-tool node set -g $PIG --uid PIG-WEB-DATA.GUARD.3 --name "Request Context and Row Security"`, with the intent reordered so request context comes first;
  - or create a sibling `PIG-WEB-DATA.GUARD.5` ("Request Context"), move the two constraints and the ACT.4 link there, and leave GUARD.3 with MD-01.

**M12. A database mechanism named in philosophy constraints (projection_hints).** Nodes: phil `ALLOCATION.GUARD.3`, `ALLOCATION.GUARD.4`, `LOGIC.SECURE`.
- Evidence: "Functions read the acting user from a transaction-local setting", "the actor a backend asserts in a transaction-local setting", "the backend sets the acting user … (transaction-local …)". Transaction-local settings (`SET LOCAL`, `set_config(…, true)`) are the Postgres realization; the PIG records them as such (DATA.GUARD.3). The stack-neutral requirement is that the actor is passed with the transaction, scoped to it, from the verified identity, never from a client-supplied id.
- Proposed edit: in the three constraint lists (full-list `node set`), replace "in a transaction-local setting" with "scoped to the transaction"; the mechanism stays in PIG DATA.GUARD.3 or M11's node.

## Minor

**m1. Formatting artifacts in epistemic states (format_artifact).**
- Every phil TRANSVERSE state ends in a stray "`." (13 nodes, for example `known`.` on TRANSVERSE.EVOLUTION.1).
- Every PIG TRANSVERSE state ends in "." (27 nodes, so `known.` is not `known` to a token match).
- Edit: strip the trailing characters (`node set --epistemic-state` with the record's State text).

**m2. Judge's first-person voice in states (format_artifact).**
- "is mine", "my choice", "my reading", "my link", "ranking mine" appear in phil ALLOCATION.FORCES, ALLOCATION.RULES, ALLOCATION.GUARD.1, ALLOCATION.DERIVE.1 and ALLOCATION.ACT.3, and in PIG DATA.ORGANIZE.1, DATA.ORGANIZE.7 and LOGIC.SECURE.4.
- In the graph "my" has no referent. Edit: "the judge's synthesis (J1)" or simply "inferred".

**m3. Lesser mechanism leaks in philosophy (projection_hints).**
- SQL privilege keywords `SELECT`, `EXECUTE` and "superuser" in ALLOCATION.GUARD.3, ALLOCATION.RECORD.2, DATA.GUARD, LOGIC.PROCESS, LOGIC.SECURE and INTERACTION.COLLABORATE. Use "read", "call" and "all-powerful role", or state once at ROOT that the database is relational, with roles, functions and transactions.
- "JSON" fixed as the program interface's format in LOGIC, LOGIC.ENFORCE, LOGIC.EXPOSE, LOGIC.EXPOSE.2, LOGIC.EXPOSE.3 and INTERACTION.ENVIRONMENT.3. Use "structured-data interface".
- An MCP example sits inside a LOGIC.EXPOSE constraint; move it to `examples`.
- "JavaScript-readable storage" in GUARD.4 should read "storage readable by page script".

**m4. The product graph names projection uids (projection_hints, P4 direction).**
- Phil INTERACTION.COLLABORATE: constraint "Realization: PIG-WEB-DATA.CONCURRENCY.5".
- Phil LOGIC.EXPOSE.3: "(L266, owned by PIG-WEB)".
- Phil TRANSVERSE.CONTRACTS: state "counted at PIG-WEB-DATA.INTERFACE.1".
- Product should not point into a projection. Move these to `design_notes`, or express them as inter links from the PIG side (`PIG-WEB-DATA.CONCURRENCY.5 → INTERACTION.COLLABORATE`, `PIG-WEB-DATA.INTERFACE.1 → TRANSVERSE.CONTRACTS`); neither link exists yet.

**m5. Link kinds misused (link_kind).**
- `conflicts` is used for "the security event log and the business audit trail must be kept apart" (phil `TRANSVERSE.OPERABILITY.1 → ALLOCATION.ACT.4`; PIG `TRANSVERSE.OPERABILITY.4 → ALLOCATION.ACT.4`). The two records are complementary, not mutually exclusive alternatives (PRIMER_01 "Conflicts"). Use `constrains`.
- `refines` is used for `TRANSVERSE.SECURITY → ALLOCATION.RULES.3`, whose sentence says "rest on". Use `requires`.
- Edit: `ig-tool link set … --shape '{"type":"constrains"}'` or `'{"type":"requires"}'`.

**m6. Hedged link intent (faithfulness_drift).**
- `DATA.MAINTAIN → ALLOCATION.RECORD.3` says "Keeps the database structure as the origin of shapes when the placement makes it the origin". RECORD.3 makes the schema the origin of stored facts unconditionally; only interface-only facts vary per project (MD-02).
- Edit: "Keeps the database structure, changed only by migration, as the origin of every stored fact and of the function API's contract."

**m7. Stale annotations (stale_annotation).**
- Phil DATA's state says no philosophy node realizes ACT.4 or the per-role layer of GUARD.3, yet the links `DATA.MAINTAIN → ACT.4` and `DATA.GUARD → GUARD.3` now exist. Trim the gap to "RECORD.2, the database share of ACT.1" (or remove it with M8).
- DATA.MAINTAIN's design_notes say "Link proposed, not created … no philosophy link (gap 1)".
- PIG LOGIC.PROCESS.2's state says the ACT.2 / ACT.3 tension is "routed to J1's owner". J1's revision R3 resolved it (ACT.2 and ACT.3 now agree), so it should read "resolved in J1 R3".

**m8. Roll-ups that omit a child or hold a clause no child holds (rollup).**
- Phil ALLOCATION.GUARD's intent does not mention concurrency control (GUARD.5) or duplicate suppression (GUARD.6).
- PIG PIG-WEB-ALLOCATION's intent does not mention the type chain (TYPE_CHAIN).
- PIG-WEB-ALLOCATION carries the read-visibility clause while no child does. Point it at the philosophy owner ("via web-app-philosophy ALLOCATION.GUARD.3"), or put the clause on ROW_SECURITY.

**m9. Placement nodes state their Forbidden list twice (duplication).**
- Phil ALLOCATION.GUARD.4, ALLOCATION.ACT.2 and ALLOCATION.PRESENT.1 (and other placements) carry a `Forbidden: …` constraint and then repeat the same items as plain constraints, for example "Forbidden: business rules in browser code" and "Business rules never live in browser code".
- Keep the `Forbidden:` line and drop the repeats.

**m10. Constraints or scope at the wrong level (intent_quality).**
- Phil INTERACTION, a roll-up, holds the COLLABORATE-local constraint "A comment is never more visible than its target"; a local constraint descends to the child (PRIMER_01).
- Phil INTERACTION.VISUALIZE ("Perceivable Interface") adds locale and time-zone formatting, which is the PRESENT.2 placement already linked from it. Reduce it to a reference.

**m11. An epistemic statement written as a constraint (intent_quality).**
- Phil ALLOCATION.FORCES.5: "Treat the premise as speculative until a primary source or a measurement exists." The node's `speculative` state already says this.
- Drop the constraint.

**m12. Style and duplicate gap (format_artifact).**
- Only the phil TRANSVERSE branch writes constraints as "MUST …"; the other branches state the rule directly. Pick one form before rendering.
- The open gap "proxy-to-app re-encryption across a network hop (L140)" is carried by both PIG TRANSVERSE.SECURITY.2 and TRANSVERSE.TOPOLOGY.1. Keep it on SECURITY.2 and link TOPOLOGY.1 to it.

## Questions, with recommendations

1. **Add philosophy `DATA.INTERFACE` (M8)?** Recommendation: yes. The target hierarchy places the function API under DATA, MD-03 makes it the default contract, and J2 already proposed it as a realization node owning no row, so it re-decides nothing. If nothing is done, the philosophy guideline states the default contract only as a placement (RECORD.2), with no tier node realizing it.
2. **Lift stack-neutral clauses from the PIG into the philosophy (M9)?** Recommendation: lift them word for word, as constraints on existing philosophy tier nodes, citing the PIG record; add INTERACTION.EDIT only if the maintainer wants the "edit" verb. If nothing is done, mark each clause as a gap on the philosophy node, so that a second stack's PIG knows to carry it.
3. **ROW_SECURITY's authority line (M3): align with GUARD.3 R2?** Recommendation: yes. It is the later revision of the same unit, and MD-01 defers to the authorization verdict. If nothing is done, the rendered PIG says per-user authorization is a backend decision while the philosophy says the writer function decides per-user write rules.

## Method and samples

- Role: ig-critic (`intent_graph/.claude/agents/ig-critic-agent.md`, `ig-critic-review-pig.md`, `ig-agent-common-protocol.md`), with primers 00, 01 and 04 and the compressed tools primer. Graphs were read only through `ig-tool` (`validate`, `validate -m`, `tree`, `query --structure`, `--overview`, `--node`, `--links`). Two narrow greps of the graph files counted link `shape.type` values and located the B2 link; no graph was loaded whole.
- Mechanical checks over all 211 nodes, run on `ig-tool` output:
  - epistemic state against the record State line;
  - name safety;
  - stack terms and process ids in intent and constraints;
  - field shape;
  - resolution of all 1,894 `impl_pointers`.
- Read in full: every intent of both graphs, for parent self-sufficiency, child scope (T4) and peer overlap (P5); every intra and inter link intent, with its kind from `04_build/links/*.yaml`.
- Nodes compared with their record (intent and constraints against Decision and Placement), 29 in all:
  - philosophy (16): ALLOCATION, ALLOCATION.FORCES.5, ALLOCATION.RECORD.2, ALLOCATION.GUARD.3, ALLOCATION.GUARD.4, ALLOCATION.PRESENT.1, DATA, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE, LOGIC, LOGIC.EXPOSE.2, INTERACTION, INTERACTION.ENVIRONMENT.6, TRANSVERSE.CONTRACTS, TRANSVERSE.EVOLUTION.3;
  - pig (13): ROOT, ALLOCATION.ROW_SECURITY, ALLOCATION.DB_API, DATA.GUARD.3, DATA.MAINTAIN.2, LOGIC.SECURE.2, LOGIC.SECURE.3, LOGIC.EXPOSE.7, PIG-WEB-INTERACTION, INTERACTION.EDIT, INTERACTION.AGENT.1, TRANSVERSE.TOPOLOGY.3, TRANSVERSE.CONTRACTS.2.
- Targeted clause checks (3): PIG DATA.INTERFACE.1 (views), LOGIC.PROCESS.2 (ACT.2 / ACT.3 tension), TRANSVERSE.SECURITY.4 (hosting).
- Read without a record (3): phil ROOT, ALLOCATION.ACT.2, ALLOCATION.ACT.3.
- Pointer spot-check (20, random, seed 13): each claim found and read; all support the node's topic.
  - phil: INTERACTION.VISUALIZE ← UI-C34; LOGIC.EXPOSE.3 ← ALLOC-C34; DATA.GUARD ← DATA-C12 and CONS-C09; INTERACTION.ENVIRONMENT.3 ← OPS-C40; ALLOCATION.RECORD.1 ← ALLOC-C28; INTERACTION.ENVIRONMENT.1 ← CV-C03; ALLOCATION.PRESENT.1 ← API-C01; ALLOCATION.FORCES.3 ← ALLOC-C11;
  - pig: VISUALIZE.2 ← C11 and UI-C07; TOPOLOGY.2 ← TOPO-C22; SECURE.3 ← SEC-C29; OPERABILITY.1 ← OPS-C02; SECURITY.2 ← TOPO-C14; REALTIME.2 ← CONS-C20; REALTIME.5 ← C25; OPERABILITY.4 ← THIN-C13; REALTIME.1 ← RT-C01; EXPOSE.4 ← WEB-C09.
