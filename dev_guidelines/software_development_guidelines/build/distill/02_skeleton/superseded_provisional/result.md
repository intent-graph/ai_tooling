# Result: skeleton of the stack-neutral software-development philosophy graph (round 2)

## L1 headline

The proposed hierarchy (L0 and five L1 branches) holds all 460 ledger rows: a tree of 170 nodes in which every row is attached to exactly one node, the decision branches OWNERSHIP and ASSURANCE carry the competing positions per node without a verdict, and the realization branches link back to the decision nodes they carry out. Certainty: grounded for the counts and the coverage (a script re-reads the written files and the ledger); inferred for the routing of each row to its node (my reading of which decision it grounds); open for the cut itself, which the maintainer has not ratified.

Pinned:
- Node count per L1 branch: OWNERSHIP 39, ASSURANCE 53, CHANGE_FLOW 32, OPERATION 23, TRANSVERSE 22; plus ROOT 1, total 170 (L1 5, L2 36, L3 128).
- Rows attached: 460 of 460 (OWNERSHIP 119, ASSURANCE 151, CHANGE_FLOW 99, OPERATION 61, TRANSVERSE 30); unattached: 0; attached twice: 0.
- Script (`check_skeleton.py`): `PASS: all 460 ledger rows attached exactly once, 0 unattached, uids follow the rules, tree and records agree, judge plan covers every node and row`
- Where the evidence does not fit the proposal: documentation and security sit in both ASSURANCE and TRANSVERSE (split decision from practice); data and schema change sits in both CHANGE_FLOW and ASSURANCE (split the same way); design practice (L308, L310 to L312, L324, L329, L330) has no branch; two extension nodes needed (OWNERSHIP.LICENCE, ASSURANCE.ARTIFACT).
- Awaiting scope (no node, rows also attached): backup and recovery 8 rows, technical debt and decommissioning 7, AI agents as contributors 3.
- Decision nodes carrying competing positions: 78 (OWNERSHIP and ASSURANCE nodes with positions); stack-pointer rows tagged: 39. No verdict is stated anywhere.

## L2 claims

Pinned:
- Node count per L1 branch: OWNERSHIP 39, ASSURANCE 53, CHANGE_FLOW 32, OPERATION 23, TRANSVERSE 22; plus ROOT 1, total 170 (L1 5, L2 36, L3 128).
- Rows attached: 460 of 460 (OWNERSHIP 119, ASSURANCE 151, CHANGE_FLOW 99, OPERATION 61, TRANSVERSE 30); unattached: 0; attached twice: 0.
- Script (`check_skeleton.py`): `PASS: all 460 ledger rows attached exactly once, 0 unattached, uids follow the rules, tree and records agree, judge plan covers every node and row`
- Where the evidence does not fit the proposal: documentation and security sit in both ASSURANCE and TRANSVERSE (split decision from practice); data and schema change sits in both CHANGE_FLOW and ASSURANCE (split the same way); design practice (L308, L310 to L312, L324, L329, L330) has no branch; two extension nodes needed (OWNERSHIP.LICENCE, ASSURANCE.ARTIFACT).
- Awaiting scope (no node, rows also attached): backup and recovery 8 rows, technical debt and decommissioning 7, AI agents as contributors 3.
- Decision nodes carrying competing positions: 78 (OWNERSHIP and ASSURANCE nodes with positions); stack-pointer rows tagged: 39. No verdict is stated anywhere.

Each line carries its certainty: grounded (I can name the file or script run that makes it true), inferred (my reading), open (not determined).

### Claims

1. **Coverage is complete.** Every one of the 460 ledger rows is attached to exactly one node, and the tree block and the node records agree on uids and rows. (grounded: script run, output in L3)
2. **The structure follows the purpose, not the evidence.** L2 was cut top-down from each branch role before rows were attached: OWNERSHIP by the five decisions the maintainer named plus LICENCE; ASSURANCE by rules plus one placement node per property (behaviour, contracts, data integrity, documentation in sync, security, performance, availability) plus ARTIFACT; realization branches by the stages of the work. (grounded for what was done, inferred that the cut is the right one)
3. **Decision nodes list competing positions with ledger ids and no verdict.** 78 OWNERSHIP and ASSURANCE nodes carry positions, forces and context variables; contested rows keep the positions the ledger records, on the node that owns them. Weak or single-source positions keep the ledger's own marks (open, inferred, one study). (grounded for presence, inferred for the grouping of positions within a node)
4. **Realization branches link back instead of re-deciding.** CHANGE_FLOW, OPERATION and TRANSVERSE nodes carry a `Realizes` line naming decision nodes; every target resolves (script). Where a realization node holds a contested row, its positions are listed there with a pointer to the decision node. (grounded for the links, inferred for which decision node each realizes)
5. **The default team context is not set.** Nineteen context variables are defined once; each node lists the ones that move its choice. Which default the max rule will judge against is the maintainer's call. (grounded for the lists; open for the default)
6. **Stack-specific rows stay attached.** 39 rows are stack-tagged in the ledger (npm, pip, Go, PostgreSQL, Rails, GitHub, OpenTelemetry and others); each node shows them on a `Stack pointers` line. (grounded: read from the ledger stack column; the ledger records some Postgres-flavoured maintainer rows as neutral, and I kept its tags)
7. **Three topics get no node and list their rows.** Backup and recovery (8 rows), technical debt and decommissioning (7), AI agents as contributors (3); each row is attached to the node of its subject and listed under Awaiting scope. (grounded for the lists; inferred that these rows are the ones touching the topics: a reading, not a term search)
8. **Four places where the proposal and the evidence disagree.** (i) documentation and security appear in both ASSURANCE and TRANSVERSE, and candidate K in both ASSURANCE and OPERATION; (ii) data and schema change appears in CHANGE_FLOW while data integrity under change is an ASSURANCE property; (iii) design practice has no branch; (iv) licence obligations and artifact integrity are not in the named lists. I resolved (i) and (ii) by splitting decision from practice with links, put (iii) in provisional nodes, and added two extension nodes for (iv). (grounded that the overlaps exist in the proposal text; inferred that the resolution is the better one)
9. **Nine maintainer-versus-research tensions are pointed at, not settled.** Each sits on the node holding the contested row (list in `skeleton.md`, section Tensions). (grounded: from the coverage check section 5)
10. **Judge plan: ten units, decision branches first.** J1 and J2 (OWNERSHIP) and J3 to J5 (ASSURANCE) first, J6 to J9 (CHANGE_FLOW, OPERATION, TRANSVERSE) after the decision units they link to, J10 (roll-ups) last; each node is in exactly one unit and the units own all 460 rows (script). (grounded)

### Not done

- No row was re-read against its sources; positions are those the ledger records, regrouped by node. Truncation risk: I read the ledger statements in full and the positions column in part (contested and maintainer rows, first 380 to 420 characters, a few in full); positions on single-practice rows rest on the statement alone. (open: a reviewer pass on a sample of nodes)
- No verdict, no deletion, no merge of ledger rows, no node created in an IntentGraph file. (grounded: by construction)
- Boundary rows have one owner each; several could sit in two places (listed in `skeleton.md`, Partition rationale). (inferred)

## L3 full

Pinned:
- Node count per L1 branch: OWNERSHIP 39, ASSURANCE 53, CHANGE_FLOW 32, OPERATION 23, TRANSVERSE 22; plus ROOT 1, total 170 (L1 5, L2 36, L3 128).
- Rows attached: 460 of 460 (OWNERSHIP 119, ASSURANCE 151, CHANGE_FLOW 99, OPERATION 61, TRANSVERSE 30); unattached: 0; attached twice: 0.
- Script (`check_skeleton.py`): `PASS: all 460 ledger rows attached exactly once, 0 unattached, uids follow the rules, tree and records agree, judge plan covers every node and row`
- Where the evidence does not fit the proposal: documentation and security sit in both ASSURANCE and TRANSVERSE (split decision from practice); data and schema change sits in both CHANGE_FLOW and ASSURANCE (split the same way); design practice (L308, L310 to L312, L324, L329, L330) has no branch; two extension nodes needed (OWNERSHIP.LICENCE, ASSURANCE.ARTIFACT).
- Awaiting scope (no node, rows also attached): backup and recovery 8 rows, technical debt and decommissioning 7, AI agents as contributors 3.
- Decision nodes carrying competing positions: 78 (OWNERSHIP and ASSURANCE nodes with positions); stack-pointer rows tagged: 39. No verdict is stated anywhere.

### Files

- `skeleton.md`: partition rationale, context variables, awaiting scope, the tree, one record per node (decides, rows, positions, forces, context, realizes, stack pointers).
- `judge_plan.md`: ten judging units, order, rows owned and rows cited per unit, verdicts to read first.
- `check_skeleton.py`: reads the ledger, the skeleton and the judge plan; proves coverage, uid rules, link resolution; prints one PASS or FAIL line.
- `result.md`: this file.

### Method

- Read: the proposal, the ledger in full (statements) and its positions column for contested, majority and maintainer rows, the coverage check (contested topics, central-decision candidates, section 5), the web guideline's decided hierarchy, its skeleton and judge plan (format model), the UID rules.
- Cut L2 from the branch roles; assigned each of the 460 rows to one node by the routing rules in `skeleton.md`; wrote positions per node from the ledger; a generator (not kept) refused to write unless every row was attached once and every cited id existed; the kept script re-proves this from the written files.

### Nodes and rows per L2

| L2 node | nodes in subtree | rows in subtree |
|---|---|---|
| OWNERSHIP.STANCE Necessity and Default Stance | 5 | 12 |
| OWNERSHIP.SELECTION Selection of a Candidate | 8 | 32 |
| OWNERSHIP.LIFECYCLE Dependency Lifecycle | 7 | 25 |
| OWNERSHIP.CONTAINMENT Containment and Exit | 6 | 14 |
| OWNERSHIP.SERVICES External Services | 7 | 26 |
| OWNERSHIP.LICENCE Licence Obligations | 5 | 10 |
| ASSURANCE.RULES Rules Common to Every Property | 4 | 9 |
| ASSURANCE.BEHAVIOUR Behaviour | 11 | 45 |
| ASSURANCE.CONTRACTS Interfaces and Contracts | 5 | 14 |
| ASSURANCE.DATA_INTEGRITY Data Integrity Under Change | 6 | 17 |
| ASSURANCE.DOCS_SYNC Documentation in Sync | 7 | 23 |
| ASSURANCE.SECURITY Security | 7 | 10 |
| ASSURANCE.PERFORMANCE Performance | 6 | 17 |
| ASSURANCE.AVAILABILITY Availability | 5 | 13 |
| ASSURANCE.ARTIFACT Artifact Integrity | 1 | 3 |
| CHANGE_FLOW.INTEGRATION Version Control and Integration | 5 | 12 |
| CHANGE_FLOW.REVIEW Review | 4 | 11 |
| CHANGE_FLOW.BUILD Build and Pipeline | 1 | 4 |
| CHANGE_FLOW.RELEASE Release | 5 | 7 |
| CHANGE_FLOW.DEPLOY Deployment | 4 | 7 |
| CHANGE_FLOW.ROLLBACK Rollback and Recovery of a Change | 3 | 5 |
| CHANGE_FLOW.MEASURE Measuring Delivery | 1 | 2 |
| CHANGE_FLOW.DATA_CHANGE Data and Schema Change | 8 | 51 |
| OPERATION.RELIABILITY Reliability Targets | 3 | 10 |
| OPERATION.ALERTING Alerting | 1 | 5 |
| OPERATION.TELEMETRY Telemetry | 6 | 21 |
| OPERATION.INCIDENTS Incidents | 4 | 8 |
| OPERATION.CAPACITY Capacity | 3 | 7 |
| OPERATION.READINESS Operational Readiness | 1 | 5 |
| OPERATION.RUNBOOKS Runbooks and Recovery Practice | 3 | 4 |
| OPERATION.FEEDBACK Feedback into Development | 1 | 1 |
| TRANSVERSE.DOCS Documentation Practice | 7 | 11 |
| TRANSVERSE.SECURITY Security Practice | 6 | 7 |
| TRANSVERSE.CONFIG Configuration and Secrets | 4 | 8 |
| TRANSVERSE.ENVIRONMENTS Development Environments | 3 | 3 |
| TRANSVERSE.DESIGN Design Derivation (provisional) | 1 | 1 |

### Script output

```text
ledger rows: 460; attached: 460; unattached: 0; attached twice: 0
nodes: 170 (ROOT 1; OWNERSHIP 39; ASSURANCE 53; CHANGE_FLOW 32; OPERATION 23; TRANSVERSE 22)
by level: L1 5, L2 36, L3 128, deeper 0
awaiting-scope ids: 18 (all attached)
PASS: all 460 ledger rows attached exactly once, 0 unattached, uids follow the rules, tree and records agree, judge plan covers every node and row
```

### Awaiting scope (rows, also attached)

- backup and recovery: L124, L359, L388, L389, L390, L416, L440, L451. (restore from version control, independent data copy, restore-as-undo, restore tests, last reversible point, soft-delete then restore, failover capacity, exercised recovery)
- technical debt and decommissioning: L009, L039, L155, L217, L296, L384, L419. (end-of-life plan, incremental replacement, toggle expiry, removing obsolete documents, deprecated items kept, unfinished contract step, dropping a column)
- AI agents as contributors: L172, L326, L327. (small batches with AI-generated code, one sanctioned tool-enforced path, agent writes the script and the human runs it)

### Open, for the maintainer

1. Ratify or correct the cut: the five L1 branches and their order, the decision and practice split of documentation and security between ASSURANCE and TRANSVERSE, data and schema change split between ASSURANCE.DATA_INTEGRITY and CHANGE_FLOW.DATA_CHANGE, and the two extension nodes. Recommendation: accept; the alternative (one home each) mixes which-mechanism rows with how-to-practise rows in one node.
2. The default context for the max rule (team size, criticality, regulation, shared database, AI coding agents). Without it the judging step cannot rank, for example, a cooldown on updates or a hard documentation gate.
3. The three scope additions. A yes creates nodes for backup and recovery, technical debt and decommissioning, and AI agents as contributors, and a judging unit for each; a no leaves their rows where they are.
4. Whether OWNERSHIP and ASSURANCE are both first decisions (the proposal's recommendation) or ASSURANCE alone; this skeleton judges them in parallel.
