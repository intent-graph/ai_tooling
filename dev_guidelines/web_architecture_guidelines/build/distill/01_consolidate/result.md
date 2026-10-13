# Distillation step 01: consolidation of the research claims

## L1 headline

The 682 research and maintainer-doctrine claims are consolidated into one normalized ledger of 605 rows, every original placed exactly once and none dropped, and partitioned into two proposed skeletons. The 41-node philosophy graph has seven branches, each answering one question (environment, trust, data, contract, structure, operation, evolution), with the web-distinct core concentrated in ENVIRONMENT. The 140-node PIG-WEB graph is organised by the part of the system a decision configures. Round 3 gave consistency and data contracts an owner in both graphs and deepened the Postgres tier from the maintainer's codified practice. Twenty-four decisions stay undecided and go to the maintainer as questions; the five points where the doctrine contradicts the research are stated doctrine first, with the research position and the condition for each, for the maintainer to confirm. Certainty: grounded on counts and placement (checked by script), inferred on the partition and the recommendations, open on the PIG-WEB uid convention until `ig-tool validate` runs.

Pinned:
- Claims: 682 original claims in (544 from rounds 1 and 2, 138 from round 3: MAINT 74, CONS 37, DCON 27), 605 ledger rows out (133 philosophy, 472 PIG-WEB); 56 merged rows absorb 133 originals; 0 dropped; 0 unplaced.
- Nodes: web-app-philosophy 41 (L0 1, L1 7, L2 33); pig-web-defaults 140 (L0 1, L1 10, L2 63, L3 66).
- Maintainer questions: 24 (one per undecided node: 1 philosophy, 23 PIG-WEB), in 9 batches.
- Maintainer-doctrine contradictions: 5, each turned into a question that states the doctrine first: MAINT-C17 in C2, MAINT-C44 in C2, MAINT-C41 in C3, MAINT-C43 in C3, MAINT-C18 in D2.
- Original claims that could not be placed: none.
- Sources: 446 original source ids (445 public, 1 maintainer) deduplicated into 358 public register entries (T1 192, T2 85, T3 70, T4 11) plus MAINT-S01, kept apart as not citable.

## L2 claims

Pinned:
- Claims: 682 original claims in (544 from rounds 1 and 2, 138 from round 3: MAINT 74, CONS 37, DCON 27), 605 ledger rows out (133 philosophy, 472 PIG-WEB); 56 merged rows absorb 133 originals; 0 dropped; 0 unplaced.
- Nodes: web-app-philosophy 41 (L0 1, L1 7, L2 33); pig-web-defaults 140 (L0 1, L1 10, L2 63, L3 66).
- Maintainer questions: 24 (one per undecided node: 1 philosophy, 23 PIG-WEB), in 9 batches.
- Maintainer-doctrine contradictions: 5, each turned into a question that states the doctrine first: MAINT-C17 in C2, MAINT-C44 in C2, MAINT-C41 in C3, MAINT-C43 in C3, MAINT-C18 in D2.
- Original claims that could not be placed: none.
- Sources: 446 original source ids (445 public, 1 maintainer) deduplicated into 358 public register entries (T1 192, T2 85, T3 70, T4 11) plus MAINT-S01, kept apart as not citable.

## Delta round 3

1. **New claims placed, old ids stable.** The 138 round-3 claims are new rows L468-L605 and all 467 round-2 ids are unchanged.
   - Twelve round-2 rows moved to a clearly better owner: L043, L066, L168, L233, L234, L260, L270, L272, L401, L402, L409, L410.
   - Four rows the coordinator named stay put, each with a reason in `skeleton.md`: L045, L127, L228-L232, L467.
   - *Grounded* (script check: missing 0, duplicated 0, frozen ids lost 0).
2. **Consistency has an owner in both graphs.**
   - Philosophy `DATA.CONSISTENCY` (10 rows): consistency model per operation, one atomic write path, inside the request versus deferred, at-least-once effects.
   - PIG-WEB gets a tenth L1, `CONSISTENCY` (42 rows), the third cross-tier concern beside SEC and OPS. Its children: CONTROL (isolation, default strategy, locks), EDITS (double submit, concurrent edits), ATOMICITY, ORDERING (sequences, incremental readers, single writer and write order), DELIVERY (outbox, idempotent consumers, post-commit hooks) and BOUNDARY (request versus deferred work).
   - *Inferred* (design); the mechanics are *grounded* in T1 PostgreSQL pages.
3. **Data contracts have an owner in both graphs.**
   - Philosophy `CONTRACT.DATA` (5 rows) sits under the contract L1, renamed Tier Contracts with its uid kept.
   - PIG-WEB `CONTRACT.DATA` (21 rows) has four children: type source of truth, boundary parsing, contract verification, meaning and ownership.
   - The database-as-API position stays at `PIG-WEB.DATA.ACCESS.2`: it is a choice about how consumers reach Postgres, question C3 already sits there, and `CONTRACT.DATA` links to it.
   - *Inferred* (no source states the whole type chain).
4. **PIG-WEB.DATA deepened from the doctrine.**
   - Four new nodes: naming (`DATA.SCHEMA.4`), JSONB contracts (`DATA.SCHEMA.5`), derived data and caches with drift guards (`DATA.DERIVED`), bulk jobs (`DATA.BULK`).
   - Keys and key sizing, foreign keys and ON DELETE, constraints, temporal columns, permission layering and deletion add rows to existing nodes.
   - Scheduled work fills `MECH.SCHEDULED`, now known for in-database work and still deferred for email.
   - *Grounded* in the doctrine's text only (single source, not checked against the running system).
5. **The maintainer doctrine is a separate authority.**
   - Its 74 claims (31 agree, 38 extend, 5 contradict, as its slot counted) are new rows beside the research rows they compare with, agreement `maintainer decision (single source)`.
   - The five contradictions are not settled. Each sits in an undecided node whose question states the doctrine first, then the research position and the condition for each: MAINT-C17 and MAINT-C44 in C2, MAINT-C41 and MAINT-C43 in C3, MAINT-C18 in D2.
   - D1 is rewritten around the doctrine's key rule; C1 notes the doctrine's support for Postgres first.
   - Philosophy `DATA.OWNERSHIP` and `DATA.INTEGRITY` carry a `conflict` annotation pointing to C3 and C2.
6. **Four new questions.**
   - H1, the default concurrency control. Recommendation: selected locks and constraints, optimistic versions for edited forms, Serializable for named cases; the T1 PostgreSQL docs favour Serializable everywhere.
   - H2, incremental-reader ordering: queue-style claiming, else the xid8 horizon.
   - I1, the type source of truth: code-first from Python models for one team, with the doctrine's database-first chain named for the maintainer.
   - I2, contract tests for one team: schema checks plus a few consumer tests.
   - *Inferred*, marked per question.
7. **Sources.** 31 new register entries (SRC-328 to SRC-358); 13 existing entries absorbed a round-3 id (for example the PostgreSQL SELECT and constraints pages, the outbox pattern, Google AIP-151); MAINT-S01 is listed in its own section, outside the public register. *Grounded.*
8. **Open.**
   - The doctrine's six internal tensions (its own record) are not resolved here.
   - The doctrine-first recommendations rest on one private source.
   - The PIG-WEB uid convention still needs `ig-tool validate`.

## L2 claims, round-2 baseline

The claims below were written at round 2; their counts (467 rows, 157 nodes, 20 questions, nine PIG-WEB areas) are superseded by the pins and the delta above.

Claims:

1. **Complete placement.** Each of the 544 original ids appears exactly once in `claims_ledger.md`, alone or in a merged row, and owned by one node; 7 nodes are deferred, of which only `PIG-WEB.UI.OFFLINE` owns a claim (CV-C08). *Grounded* (script check: missing 0, duplicated 0, unknown owner 0).
2. **Philosophy partition by question, not by tier or distinctness.** The seven L1 branches each answer one question a designer must answer about the whole application. Distinct and shared principles sit together in the branch their subject belongs to, tagged per row; overlap with the Python philosophy is carried by 14 inter links, not copies. *Inferred* (design judgment; alternatives and reasons in `skeleton.md`).
3. **The distinct core is the environment.** All 17 ENVIRONMENT principles are web-distinct; TRUST is split (8 web-distinct, 10 shared-backend); DATA, STRUCTURE, OPERATION and EVOLUTION are mostly shared. Principle tags over all rows: web-distinct 40, shared-backend 44, shared-data 12, shared-all 22. *Grounded* for the counts; *inferred* for each classification.
4. **PIG-WEB partition by what a decision configures.** Nine areas: SHAPE, TOPOLOGY, DATA, APP, CONTRACT, UI, SEC, OPS, MECH. MECH keeps cross-tier mechanisms (jobs, caching, uploads, real-time) whole instead of scattering them over four tiers. Nine L1 nodes exceed the usual six because a grouping level would push keyword uids to L3, where only numbers are allowed. *Inferred.*
5. **Twenty undecided nodes, one question each.** Every recommendation is argued from the sources and the "classic website" scope. Grounded recommendations: session cookie or BFF over browser tokens (RFC 10017, OWASP), split logic placement (Fowler), ORM models as the domain for CRUD (Cosmic Python), managed secret injection (OWASP). Inferred: server-rendered HTML as the default contract, Postgres-first backing services, SSE before WebSocket, no API versioning while the client is first-party, bigint identity keys, and the rest. If nobody answers, every node stays undecided with its positions. *Mixed, marked per question.*
6. **The coverage check's overlaps are resolved.** Postgres-as-queue becomes one undecided node; configuration and secrets split into two nodes; hypermedia versus SPA becomes one node; monolith-first is relabelled majority; RLS becomes one decision node with the data mechanics merged; the duplicate clusters are merged into single rows; idempotency is kept as two linked nodes (server side, client side). *Grounded* in the ledger rows named in `skeleton.md`.
7. **Source register deduplicated.** 47 entries replace several original ids; four multi-page works count as one document each (Twelve-Factor, Fielding's dissertation, SRE book, Resilient Web Design). Seven tiers were set where slots disagreed or a draft was ranked T1 (the two Internet-Drafts became T2, nginx and PgBouncer T1, React docs T3, ASGI T1). *Grounded.*
8. **Routing exceptions are few and named.** Six principle-level rows sit in PIG-WEB because each serves one decision. Seventeen rows are re-levelled, mostly practices merged into the principle they restate. Four contested-labelled rows sit on non-undecided nodes for stated reasons. *Grounded* for the lists; *inferred* for each judgment.
9. **Open points to settle before any node is created.**
   - The PIG-WEB uid convention follows the `PIG-PY.*` precedent as brief_distill fixes. PRIMER_01 states a root exactly `ROOT` and an L1 pattern `PIG-{SEMANTIC}-{COMPONENT}`. Run `ig-tool validate` on the first nodes. *Open.*
   - The ledger file is 588 lines, above the documentation standard's 500, because it is a data table.
   - Quotes in the research were tool-extracted, not byte-verified (inherited from the slots).

## L3 full

Pinned:
- Claims: 682 original claims in (544 from rounds 1 and 2, 138 from round 3: MAINT 74, CONS 37, DCON 27), 605 ledger rows out (133 philosophy, 472 PIG-WEB); 56 merged rows absorb 133 originals; 0 dropped; 0 unplaced.
- Nodes: web-app-philosophy 41 (L0 1, L1 7, L2 33); pig-web-defaults 140 (L0 1, L1 10, L2 63, L3 66).
- Maintainer questions: 24 (one per undecided node: 1 philosophy, 23 PIG-WEB), in 9 batches.
- Maintainer-doctrine contradictions: 5, each turned into a question that states the doctrine first: MAINT-C17 in C2, MAINT-C44 in C2, MAINT-C41 in C3, MAINT-C43 in C3, MAINT-C18 in D2.
- Original claims that could not be placed: none.
- Sources: 446 original source ids (445 public, 1 maintainer) deduplicated into 358 public register entries (T1 192, T2 85, T3 70, T4 11) plus MAINT-S01, kept apart as not citable.

## Delta round 3

### Method

1. Read the three round-3 results in full (L1, L2, L3): maintainer doctrine (74 MAINT claims, source MAINT-S01), consistency and ordering (37 CONS claims, 25 sources), data contracts (27 DCON claims, 19 sources).
2. Extended the parser to the three formats (doctrine table with a `vs research` column, CONS bullets, DCON bullets with inline positions).
3. Froze the round-2 ledger and register ids before rebuilding. Existing rows keep their L id, matched by the set of claims they merge; new rows get L468 onward in tree order. Existing register groups keep their SRC id; new documents get SRC-328 onward. The build fails if a frozen id disappears or a group spans two frozen ids.
4. Placed every new claim. MAINT claims are always their own rows, never merged into research rows, so the maintainer's authority stays separable. CONS and DCON claims were not merged either: each states itself as new or extending.
5. Re-ran all checks: placement, uid depth rules, name safety, tier conflicts, principle tags, link endpoints (92 link rows, 0 mismatches), question citations (all ids resolve to the node named).

### Figures after round 3

- Rows by merge size: 549 single, 40 of two, 12 of three, 3 of four, 1 of five.
- Levels: philosophy 133 principle; PIG-WEB 157 decision, 307 practice, 8 principle.
- Agreement: 398 consensus, 92 majority, 38 contested, 3 open, 74 maintainer decision (single source).
- Certainty (leading word): 552 grounded, 50 inferred, 3 open.
- Principle tags: web-distinct 40, shared-backend 56, shared-data 21, shared-all 24.
- Undecided nodes added: PIG-WEB.CONSISTENCY.CONTROL.1, CONSISTENCY.ORDERING.2, CONTRACT.DATA.1, CONTRACT.DATA.3. Deferred: 6 nodes, plus MECH.SCHEDULED partly deferred.

### Placement decisions (for review)

- **Doctrine principles to the philosophy graph:**
  - MAINT-C24 and C71 to DATA.SHAPE.
  - MAINT-C39 and C45 to DATA.INTEGRITY.
  - MAINT-C54 to STRUCTURE.STATE.
  - MAINT-C59 to DATA.CONSISTENCY.
  - MAINT-C70 to TRUST.AUTHORITY.
  - MAINT-C74 to DATA.MIGRATION.
- **Postgres-specific principles in PIG-WEB:** CONS-C03 (snapshot isolation) and CONS-C18 (sequence semantics) are principle-level but Postgres mechanics, so they sit with the PIG-WEB decisions they serve (L577, L591).
- **Contradicting doctrine rows sit in the undecided nodes of their question:** MAINT-C17 and C44 at DATA.LOGIC; MAINT-C41 and C43 at DATA.ACCESS.2; MAINT-C18 at DATA.LIFECYCLE.1.
- **MAINT-C23 (erasure sketch)** is owned by the deferred node DATA.LIFECYCLE.4 as input.
- **CONS-C23 (Helland)** is a conditional dissent on the known DATA.CONSISTENCY node, appendix of `maintainer_questions.md`.
- **Two round-2 rows changed status by note, not by edit:** L270 is grounded by CONS-C24; L272 is contested by DCON-C06.
- **Node intents updated where rows moved:** APP.TRANSACTIONS, CONTRACT.HTTP, CONTRACT.RETRIES, CONTRACT.EVOLUTION, MECH.JOBS, OPS.TESTING, DATA.SCHEMA, MECH.SCHEDULED; the contract L1 of both graphs was renamed Tier Contracts with its uid kept.

### Gaps after round 3

- **Doctrine not verified:** the doctrine was not checked against the running system it codifies.
- **Doctrine's internal tensions:** its six tensions (key choice tied to soft delete, the DELETE grant, views, where validation runs, where async work runs, row-by-row cache refresh) are recorded in its slot and not resolved.
- **No public source on:** JSONB contracts, database-first type generation, and the whole cross-tier type chain.
- **Thin sources:** double-submit form tokens rest on T4; the incremental-reader hazard on one T3 source.

## L3 full, round-2 baseline

The sections below were written at round 2; their counts are superseded by the pins and the delta above.

### Files

| file | content |
|---|---|
| `claims_ledger.md` | 467 rows in tables per L1 branch: id, statement, merged originals, owner, level, tag, agreement, positions, certainty, sources; then an index from every original id to its row; dropped: none |
| `sources.md` | 327 register entries by tier: id, tier, title, body, URL, original ids replaced, note (multi-page works, tier changes, draft status) |
| `skeleton.md` | design rationale, both trees with owned ledger ranges, node tables (uid, name, intent, epistemic_state, owned rows), candidate intentlinks (16 intra philosophy, 22 intra PIG-WEB, 14 inter to `python-kb-philosophy`, 20 inter PIG-WEB to philosophy), deferred nodes, conventions to check |
| `maintainer_questions.md` | 20 questions in 7 batches, each with decision, recommendation, default if unanswered, positions with source ids; appendix of contested-labelled rows not raised |

### Method

1. Read `brief_distill.md`, `brief_shared.md`, PRIMER_00, 01, 03A, LOD `DRILL_DOWN.md`, the two Python graphs (`ig-tool tree`, `ig-tool query` on DEFENSIVE, PIG-PY.IMPL.ERR, PIG-PY.ROOT and the philosophy YAML in full), the coverage check, and every round-1 and round-2 result in full (L1, L2, L3).
2. Parsed every claim and every source-register row of the 13 results into structured data (544 claims, 401 sources; each slot's claim format, bullets, tables or blocks, was parsed on its own) and spot-checked the parse.
3. Designed both partitions on the claims, then assigned every claim to a node, merging only true duplicates (the coverage check's item 16 clusters plus duplicates found while reading: progressive enhancement, PRG, CORS allowlist, NOTIFY as signal, outbox, idempotent consumers, login throttling, RLS caveats, attached resources, configuration separation).
4. Generated the ledger, register and trees with a script that fails on: a missing, duplicated or unknown claim id; an unknown owner; a merged row without its own statement, level, agreement or certainty; a principle without a tag or a tag on a non-principle; a uid not matching the depth rules; a node name with a forbidden character; an unresolved tier conflict. The final run passed all checks.
5. Wrote the questions and the rationale by hand, then checked by script that every ledger id they cite belongs to the node or link endpoints named (0 mismatches).

### Ledger figures

- Rows by merge size: 411 single, 40 of two, 12 of three, 3 of four, 1 of five (PRG: API-C06, UI-C17, THIN-C37, THIN-C39, THIN-C40).
- Levels: philosophy 112 principle; PIG-WEB 116 decision, 233 practice, 6 principle.
- Agreement: philosophy 92 consensus, 17 majority, 3 contested; PIG-WEB 256 consensus, 69 majority, 28 contested, 2 open (API-C25, API-C32).
- Certainty (leading word): 420 grounded, 45 inferred, 2 open.
- Originals by owning graph: philosophy 143, PIG-WEB 401.

### Judgment calls made here (for review)

- **Thesis at the root.** L001 (ARCH-C45, WEB-C27) is contested in the sources. It is recorded as `known: maintainer decision | unvalidated`, not asked, because brief_distill already fixed the two-graph shape.
- **Monolith first as majority.** SHAPE.DEPLOYABLES.1 holds the Tilkov dissent as a conflict, following the counter-voices slot's own relabel.
- **SEC-C12 relabelled.** "Never localStorage" moved from consensus to majority, as the counter-voices slot recommends.
- **CV-C24 as an open gap.** It is labelled contested, but no source opposes it.
- **Tier harmonization.** Seven register tiers were changed (see `sources.md` notes). Slot-local source ids inside positions and certainty texts were rewritten to register ids.
- **TOPO-C15 kept separate from SEC-C17.** They share only the Secure attribute; TOPO-C15 adds the no-mixed-content rule.
- **Two nodes for idempotency.** Server side and client side stay apart, linked.
- **Audit logging split.** The security event log goes to OPS and the business audit trail to DATA, following THIN-C13.
- **Distinctness tags are my classification** against one criterion: the principle exists because of the web environment (browser, untrusted client, URLs, intermediary caches). Accessibility and perceived-latency principles are tagged web-distinct because the four-value scale has no "UI-shared" value.

### Gaps and limits

- **PIG-WEB uids not validated.** The trees were not passed through `ig-tool validate` because no graph file may be created in this step; only the uid depth rules were checked by script.
- **Quotes not verified.** Research quotes were read as the slots recorded them; no source was re-fetched here.
- **Recommendations without T1/T2 backing.** A1, A4, A5, C1, C3, D1, G1, G2 and G3 rest on synthesis, and each is marked inferred in its question.
- **Topics not placed.** The coverage check's "repository layout" topic has no claims and no node; it was neither in the brief's scope list nor researched.
