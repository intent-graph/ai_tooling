# Result: skeletons of the two IntentGraphs on the maintainer's hierarchy (round 4)

## L1 headline

Both skeletons, `web-app-philosophy` and `pig-web-defaults`, are cut on the maintainer's hierarchy: ALLOCATION first, then DATA, LOGIC, INTERACTION and TRANSVERSE. Every claim is attached to exactly one node, and the 26 placement nodes carry the competing positions for the judges without a verdict. The counts and the coverage are grounded: a script re-parsed the written files to check them. The partition choices are inferred: they are my design and the maintainer can redirect them.

Pinned:
- Claim ids: 793 in (682 from rounds 1 to 3, 111 from round 4), 793 placed, 0 not placed.
- Ledger rows out: 689 (605 kept with ids unchanged, 84 new: L606-L689).
- Nodes: web-app-philosophy 79 (L0 1, L1 5, L2 25, L3 48); pig-web-defaults 132 (L0 1, L1 5, L2 29, L3 97).
- Placement nodes: 26 (web-app-philosophy 19, pig-web-defaults 7).
- Claims I could not place: none.

## L2 claims

Pinned:
- Claim ids: 793 in (682 from rounds 1 to 3, 111 from round 4), 793 placed, 0 not placed.
- Ledger rows out: 689 (605 kept with ids unchanged, 84 new: L606-L689).
- Nodes: web-app-philosophy 79 (L0 1, L1 5, L2 25, L3 48); pig-web-defaults 132 (L0 1, L1 5, L2 29, L3 97).
- Placement nodes: 26 (web-app-philosophy 19, pig-web-defaults 7).
- Claims I could not place: none.

Claims:
1. **Coverage is complete.** *Grounded: script on the written files.*
   - Every original claim id of slots 01 to 07 and 09 to 20 appears exactly once in the ledger's `merges` column.
   - Every one of the 689 rows has exactly one owner, and that owner is a node of `skeleton.md`.
   - The rows listed on each node in `skeleton.md` match the ledger owners (0 mismatches).
   - Every row id and source id that is cited resolves.
2. **Round 4 is integrated.** *Grounded.*
   - 111 claims gave 84 new rows (L606-L689).
   - 24 claims restate an existing row and joined it: 23 rows absorb them, L302 takes two.
   - 3 claims joined another new row: ALLOC-C24 into L609, COLLAB-C29 into L627, AGENT-C02 into L633.
   - Each merge carries a note in `positions` saying what it adds.
3. **The register is extended.** *Grounded.*
   - 56 new entries, SRC-359 to SRC-414: T1 21, T2 11, T3 21, T4 3.
   - The other 35 round-4 source ids were absorbed by 31 existing entries.
   - Result: 414 public entries (T1 213, T2 96, T3 91, T4 14), plus MAINT-S01 kept in its own section.
4. **ALLOCATION has 8 children.**
   - Their contents are grounded: they are what the file contains.
     - FORCES, with 6 children (one per force the maintainer named).
     - CONTEXT, a single node.
     - RULES, with 5 children: authority and copies, end-to-end placement, trust boundary, one core for every client, atomicity ends at the transaction.
     - Five placement families: RECORD, GUARD, ACT, DERIVE, PRESENT.
     - 19 stack-neutral placements: the 12 initial responsibilities plus 7 the evidence demanded (system of record, data access interface, type and contract definitions, identity and session state, duplicate suppression, deferred and scheduled work, rendering).
   - `PIG-WEB.ALLOCATION` holds the 7 stack placements where the stack offers competing mechanisms; each refines its stack-neutral placement.
   - The shape itself is inferred (my design).
5. **Routing rules decide which graph owns a row.** *The rule is inferred (my decision); the counts are grounded.*
   - A row about which tier holds a responsibility goes to a placement node.
     - If it is stated in tier terms, the node is in `web-app-philosophy`, whatever the row's level.
     - If it names a stack mechanism, the node is in `PIG-WEB.ALLOCATION`.
   - Tier branches keep the round-3 routing: principles in philosophy, decisions and practices in PIG-WEB.
   - Effect: 26 round-3 rows moved from pig-web-defaults to web-app-philosophy. 24 are placement rows; 2 are stack-neutral principles (L303, L435). None moved the other way.
6. **Tier branches hold realization only and link to the placements that give them work.** *Grounded counts.*
   - Intra web-app-philosophy: 31 links.
   - Intra pig-web-defaults: 11 links.
   - From pig-web-defaults to web-app-philosophy: 60 links (25 same-branch refines, 8 placement refines, 27 tier to placement).
   - To `python-kb-philosophy`: 15 links.
7. **Judge plan: 9 units, none above 60 nodes.** *Grounded.*
   - J1 is ALLOCATION across both graphs: 47 nodes, 101 owned rows, plus 73 rows owned elsewhere that the placement records cite.
   - J2 to J5 are the four philosophy branches; they run in parallel after J1.
   - J6 to J9 are the four PIG-WEB branches; each runs after its philosophy counterpart.
8. **7 deferred nodes are recorded.** *Grounded.* All are scope-out topics: erasure, high availability, search, email, offline, internationalisation, incident response.
   - The local-first row L302 is no longer deferred: it is a position of ALLOCATION.RECORD.1.
   - Scheduled jobs are no longer deferred.
9. **Open: gaps in the evidence.**
   - ALLOCATION.FORCES.1 (Correctness) and .2 (Security) own no row.
   - ALLOCATION.DERIVE.2 lists a position (filtering in the backend or the browser) that no row argues for.
   - ALLOCATION.PRESENT.2 has one grounded position only.
10. **Open: process caveats.**
    - `skeleton.md` is 1032 lines, above the 500-line documentation target; I kept it in one file as the brief specified.
    - No independent review pass was run on the placement records. I recommend one before judging.

## L3 full

Pinned:
- Claim ids: 793 in (682 from rounds 1 to 3, 111 from round 4), 793 placed, 0 not placed.
- Ledger rows out: 689 (605 kept with ids unchanged, 84 new: L606-L689).
- Nodes: web-app-philosophy 79 (L0 1, L1 5, L2 25, L3 48); pig-web-defaults 132 (L0 1, L1 5, L2 29, L3 97).
- Placement nodes: 26 (web-app-philosophy 19, pig-web-defaults 7).
- Claims I could not place: none.

### Files written (this folder)

- `claims_ledger.md`: the 689 rows.
  - Columns: `id`, `statement`, `merges`, `owner` (new skeleton), `was` (round-3 owner), `level`, `tag`, `agreement`, `positions`, `certainty`, `sources`.
  - Rows are grouped by graph and L1 branch, in tree order.
  - At the end: the round-4 merges list, the rows that changed graph, the index from each original claim to its ledger row (all 20 claim prefixes), and the dropped and unplaced claims (none).
- `sources.md`: the round-3 register with round-4 entries appended to their tier sections.
  - An absorbing entry lists the round-4 id in `replaces`.
  - Where the round-4 copy differed, a note says so: SRC-045, SRC-053, SRC-057, SRC-089, SRC-203, SRC-246.
- `skeleton.md`, in this order:
  - how to read the file;
  - partition rationale: the cut, ALLOCATION, routing rules, rejected alternatives, tensions for the judges;
  - for each graph: the tree, the node table (uid, name, what it decides, rows owned) and the placement records (positions with ledger ids, evidence on copies and forbidden tiers, forces in tension, context that moves it, tier nodes that realize it);
  - the intentlinks, the deferred nodes, and the conventions to check at creation.
- `judge_plan.md`: units J1 to J9, their order, their node lists, the rows each reads in full, and the verdicts each reads first.

### Method

- **Inputs.** I read:
  - the authority and brief: `../target_hierarchy.md`, `../brief_distill.md`, the shared research brief;
  - IntentGraph PRIMER_00, PRIMER_01 and PRIMER_03A, and the level-of-detail note on partitioning;
  - the round-3 ledger, whole (605 rows);
  - the register (its format, and every entry checked against the round-4 sources);
  - the three round-4 results, in full.
- **Rejected partition.** The round-3 `skeleton.md` was opened only for node wording and for the PIG uid convention.
- **Assignment.** Scripts parsed the ledger and the round-4 claims. The tree, the row ownership, the merges and the placement positions were written by hand in a data model; the files were generated from it.
- **Gates.** A separate script re-parsed the output files and checked:
  - 11 cells per row;
  - unique ids;
  - the 793 merge ids, which equal exactly the original ids of the old ledger plus the round-4 claims;
  - that every owner exists in the skeleton;
  - that skeleton and ledger owners agree;
  - that every cited row and source resolves;
  - that no absolute path or private name appears.
- **Graph files.** None were created or edited. `01_consolidate` was not modified. Nothing was committed or pushed.

### Placement nodes (26)

- `web-app-philosophy` (19):
  - RECORD.1 System of Record, RECORD.2 Data Access Interface, RECORD.3 Type and Contract Definitions;
  - GUARD.1 Validation, GUARD.2 Invariants, GUARD.3 Authorization, GUARD.4 Identity and Session State, GUARD.5 Concurrency Control and Conflict Resolution, GUARD.6 Duplicate Suppression;
  - ACT.1 Business Rules and State Transitions, ACT.2 Side Effects and Integrations, ACT.3 Deferred and Scheduled Work, ACT.4 Audit and History;
  - DERIVE.1 Derived Data and Aggregation, DERIVE.2 Filtering, Sorting, Paging and Search, DERIVE.3 Caching;
  - PRESENT.1 Rendering, PRESENT.2 Formatting and Localization, PRESENT.3 UI and Ephemeral State.
- `pig-web-defaults` (7): POSTGRES_FIRST, DB_API, TYPE_CHAIN, ROW_SECURITY, JOB_HOST, CACHE_STORE, JS_SERVER, all under `PIG-WEB.ALLOCATION`.

### Round-4 rows and merges

- **New rows.**
  - ALLOC: 27 rows (L606-L632). They are mostly owned by ALLOCATION; L614, L617, L618 and L619 are owned in PIG-WEB.
  - AGENT: 31 rows (L633-L663). The principles are owned by ALLOCATION.RULES.4, GUARD.3, ACT.4 and INTERACTION.AGENT; the decisions and practices by PIG-WEB.INTERACTION.AGENT.1 to .5, LOGIC.EXPOSE.3 and LOGIC.SECURE.7.
  - COLLAB: 26 rows (L664-L689). The principles are owned by INTERACTION.COLLABORATE, GUARD.5, PRESENT.3 and ACT.4; the decisions and practices by PIG-WEB.INTERACTION.COLLABORATE.1 to .4, EDIT, DATA.CONCURRENCY.2, DATA.MAINTAIN.3 and ALLOCATION.ROW_SECURITY.
- **Merged into existing rows (24 claims, 23 rows).**
  - L010 ALLOC-C29;
  - L019 ALLOC-C06;
  - L020 ALLOC-C07;
  - L031 AGENT-C21;
  - L042 ALLOC-C23;
  - L044 ALLOC-C20;
  - L051 AGENT-C28;
  - L120 ALLOC-C39;
  - L214 ALLOC-C32;
  - L215 ALLOC-C12;
  - L226 ALLOC-C33;
  - L260 COLLAB-C11;
  - L302 ALLOC-C38 and COLLAB-C21;
  - L339 AGENT-C07;
  - L359 AGENT-C24;
  - L366 AGENT-C22;
  - L437 COLLAB-C23;
  - L460 COLLAB-C24;
  - L462 COLLAB-C25;
  - L475 COLLAB-C14;
  - L527 ALLOC-C16;
  - L546 AGENT-C29;
  - L570 COLLAB-C13.
- **Statements of merged rows are unchanged.** What the round-4 claim adds is in `positions`, and its sources are appended.

### Rows that changed graph (26, all from pig-web-defaults to web-app-philosophy)

L214, L215, L527, L528, L534, L252, L253, L254, L255, L281, L302, L303, L313, L314, L315, L316, L318, L319, L320, L321, L582, L584, L596, L601, L406, L435.

### Judgment calls the maintainer may redirect (inferred)

1. **Stack-neutral placement rows go to the philosophy graph whatever their level.** These include decision rows (L214, L313, L252). As a result the philosophy graph now holds decisions, under ALLOCATION.
   - Alternative: keep level-based routing everywhere. The tier-level decisions would then sit in PIG-WEB, and philosophy placements would hold principles only.
2. **Placement families sit at L2.** The eight children of ALLOCATION are FORCES, CONTEXT, RULES, RECORD, GUARD, ACT, DERIVE and PRESENT.
   - Alternative: a literal FORCES, CONTEXT, RULES, PLACEMENT cut, which puts every placement at L4 under numeric uids.
3. **CONTEXT is one node.** It holds the variable list; the rows grounding each variable are owned by placements. FORCES, by contrast, has a child per force.
4. **PIG-WEB.ALLOCATION has 7 nodes, not 19.** Only placements with stack-specific competing mechanisms got a stack node.
5. **Runtime topology sits under PIG-WEB.TRANSVERSE.TOPOLOGY.** It refines philosophy LOGIC.PROCESS, which is named "Processing Model" because its rows are the process model.
6. **The philosophy graph has no node for edit or the database interface.** No principle-level row supports either; PIG-WEB holds both.

### Open

- ALLOCATION.FORCES.1 Correctness and .2 Security own no row. They are criteria the maintainer named, grounded only through the rules and placements that cite them.
- No row argues for filtering in the backend or the browser (ALLOCATION.DERIVE.2, position 3).
- Formatting placement rests on one capability source (L632).
- Inherited gaps from the round-4 results:
  - SPA-school primary sources;
  - measured comparisons of placements;
  - a primary source for database-tier scalability (L615);
  - OpenTelemetry agent spans;
  - the moderation law (DSA).
- `skeleton.md` exceeds the 500-line documentation target (1032 lines): there are 211 nodes, each shown once in its tree and once in its table, plus 26 placement records.
- No independent review pass: the placement positions and the routing are proposals for the judges and the maintainer.
