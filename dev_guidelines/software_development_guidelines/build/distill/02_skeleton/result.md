# Result: the top two levels of the software-development philosophy graph, cut on the decided hierarchy

## L1 headline

The decided hierarchy (ROOT and seven L1 branches) holds all 814 ledger rows: 53 L2 nodes, every row routed to exactly one of them, none unrouted, and no row without a place. The cut came from each branch's role first; rows were routed after. Certainty: grounded for the counts and the coverage (a script re-reads the written files and the three ledger parts); inferred for the routing of each row (my reading of which node it grounds most directly, not checked against sources); open for the five boundary groups the maintainer or the L3 step may move (listed under L2 claims).

Pinned:
- L2 nodes per L1 branch: OWNERSHIP 6, ASSURANCE 9, CONSTRUCTION 10, CHANGE_FLOW 8, OPERATION 9, EVOLUTION 5, TRANSVERSE 6; total 53 (plus ROOT 1 and L1 7: 61 nodes).
- Rows routed per L1 branch: OWNERSHIP 134, ASSURANCE 243, CONSTRUCTION 87, CHANGE_FLOW 116, OPERATION 110, EVOLUTION 53, TRANSVERSE 71.
- Rows routed: 814 (part 1 460, part 2 289, part 3 65); unrouted: 0; routed twice: 0.
- Script (`check_routing.py`): `PASS: all 814 ledger rows routed exactly once to an existing L2 uid, 0 unrouted, uids follow the rules, counts agree with tree_l2.md`
- Rows the decided hierarchy has no place for: none. Rows placed on a weaker fit than the rest (flagged, not unplaced): design derivation (L329), system-shape rows (L1210 to L1214, L1218, L1219, L1221, L1222, L171) and relational normal form (L1263 to L1267) in CONSTRUCTION, which the decided CONSTRUCTION list does not name.

## L2 claims

Pinned:
- L2 nodes per L1 branch: OWNERSHIP 6, ASSURANCE 9, CONSTRUCTION 10, CHANGE_FLOW 8, OPERATION 9, EVOLUTION 5, TRANSVERSE 6; total 53 (plus ROOT 1 and L1 7: 61 nodes).
- Rows routed per L1 branch: OWNERSHIP 134, ASSURANCE 243, CONSTRUCTION 87, CHANGE_FLOW 116, OPERATION 110, EVOLUTION 53, TRANSVERSE 71.
- Rows routed: 814 (part 1 460, part 2 289, part 3 65); unrouted: 0; routed twice: 0.
- Script (`check_routing.py`): `PASS: all 814 ledger rows routed exactly once to an existing L2 uid, 0 unrouted, uids follow the rules, counts agree with tree_l2.md`
- Rows the decided hierarchy has no place for: none. Weaker fits flagged: L329, L1210 to L1214, L1218, L1219, L1221, L1222, L171, L1263 to L1267 (CONSTRUCTION).

Each line carries its certainty: grounded (I can name the file or script run that makes it true), inferred (my reading), open (not determined).

### Claims

1. **Coverage is complete.** All 814 rows of the three ledger parts route once each to an existing L2 uid; ids are exactly L001 to L460, L1001 to L1289, L1501 to L1565. (grounded: script run, output in L3)
2. **The L2 cut follows each branch's role, not the rows.** OWNERSHIP by the decisions the maintainer named (stance, selection, lifecycle, containment, external services) plus licences; ASSURANCE by the rules common to every property plus one placement node per property (behaviour, contracts, data integrity, documentation in sync, security, performance, availability and recovery) plus artifact integrity; the realization branches by the stages and topics `target_hierarchy.md` lists for them. (grounded for what was done; inferred that the cut is the right one)
3. **Four nodes exist beyond the decided lists, because rows needed them.** OWNERSHIP.LICENCE (10 rows) and ASSURANCE.ARTIFACT (8 rows, the outcome "what runs is what was reviewed"); CONSTRUCTION.DESIGN and CONSTRUCTION.SYSTEM_SHAPE hold design derivation and decomposition into deployable units, which the decided CONSTRUCTION list does not name. (grounded that the lists omit them; inferred that a node, not a deletion, is the right answer)
4. **Mechanism rows go to ASSURANCE, practice rows to the realization branch.** Applied as decided: a row that says which mechanism or stage guarantees a property is in ASSURANCE (for example branch protection to ARTIFACT, review independence and gates to RULES, scanning to SECURITY); a row that says how a practice is carried out is in its realization branch (review size and speed to REVIEW, backup design to RECOVERY). (grounded for the rule; inferred for each application, 141 boundary rows carry a one-clause reason in `routing.md`)
5. **Four topics span a decision and a realization node and each names its content holder.** Documentation (content ASSURANCE.DOCS_SYNC, index TRANSVERSE.DOCS), security (content ASSURANCE.SECURITY plus the two TRANSVERSE nodes without an assurance counterpart, index TRANSVERSE.SECURITY), data and schema change (content CHANGE_FLOW.DATA_CHANGE, index ASSURANCE.DATA_INTEGRITY), availability and recovery (content OPERATION.RECOVERY, index ASSURANCE.AVAILABILITY). (grounded for the table in `tree_l2.md`; inferred for which side holds more, from row counts)
6. **No default team context.** The provisional skeleton's nineteen default-context variables are dropped; the next step adds a context variable to a node only where a row itself says the best practice moves with it. Author-neutral rows (AI agents as contributors) are routed by what the outcome needs: review trust to ASSURANCE.RULES, limits on automation to ASSURANCE.SECURITY, attribution to CHANGE_FLOW.INTEGRATION. (grounded for what was dropped; inferred for the routing of the author-neutral rows)
7. **Part 3 follows the stated rule.** The 65 code-design rows route to CONSTRUCTION except dependency rows (OWNERSHIP.SELECTION, OWNERSHIP.LIFECYCLE), verification rows (ASSURANCE.BEHAVIOUR, ASSURANCE.RULES) and measurement rows (ASSURANCE.PERFORMANCE); L1538 (layered controls, in the JavaScript dependencies group) went to ASSURANCE.RULES as a placement rule. (grounded for the rule; inferred for the exceptions)
8. **Provisional "awaiting scope" is closed.** Backup and recovery, technical debt and decommissioning, and AI agents as contributors now have homes (OPERATION.RECOVERY with ASSURANCE.AVAILABILITY; EVOLUTION.DEBT and DECOMMISSION; author-neutral rows in RULES, SECURITY, INTEGRATION). (grounded: MD-04, MD-05)
9. **Rows with an arguable owner are listed, not hidden.** Five groups could sit in two places: dependency scanning and inventory (OWNERSHIP.LIFECYCLE or ASSURANCE.SECURITY), audit trail and history (TRANSVERSE.SECURITY_MONITORING or ASSURANCE.DATA_INTEGRITY), recovery objectives and tests (OPERATION.RECOVERY or ASSURANCE.AVAILABILITY), expand-migrate-contract (EVOLUTION.INCREMENTAL, CHANGE_FLOW.DATA_CHANGE, CHANGE_FLOW.ROLLBACK, same normative thing in L1011, L163, L383), and mainline protection (ASSURANCE.ARTIFACT or CHANGE_FLOW.INTEGRATION). Each row has one owner; one-location-per-fact (MD-03) is applied to content at L3. (inferred)

### Not done

- No L3, no judging, no positions, no context variables, no node created in an IntentGraph file, no ledger row edited or merged. (grounded: by construction)
- No row was re-read against its sources; routing rests on each row's statement (read in full for all 814 rows), not on its positions column. (open: a reviewer pass on a sample of nodes and on the boundary rows)

## L3 full

Pinned:
- L2 nodes per L1 branch: OWNERSHIP 6, ASSURANCE 9, CONSTRUCTION 10, CHANGE_FLOW 8, OPERATION 9, EVOLUTION 5, TRANSVERSE 6; total 53 (plus ROOT 1 and L1 7: 61 nodes).
- Rows routed per L1 branch: OWNERSHIP 134, ASSURANCE 243, CONSTRUCTION 87, CHANGE_FLOW 116, OPERATION 110, EVOLUTION 53, TRANSVERSE 71.
- Rows routed: 814 (part 1 460, part 2 289, part 3 65); unrouted: 0; routed twice: 0.
- Script (`check_routing.py`): `PASS: all 814 ledger rows routed exactly once to an existing L2 uid, 0 unrouted, uids follow the rules, counts agree with tree_l2.md`
- Rows the decided hierarchy has no place for: none. Weaker fits flagged: L329, L1210 to L1214, L1218, L1219, L1221, L1222, L171, L1263 to L1267 (CONSTRUCTION).

### Files

- `tree_l2.md`: ROOT, the seven L1 nodes, the 53 L2 nodes (uid, name, one-line intent, rows), and the split-topic table (content holder and index per MD-03).
- `routing.md`: one line per ledger row, in ledger order: row id, L2 uid, and a one-clause reason on the 141 boundary rows.
- `check_routing.py`: reads the three ledger parts, `tree_l2.md` and `routing.md`; proves coverage, uid rules, counts; prints one PASS or FAIL line. Exit code 0 on PASS.
- `result.md`: this file.
- `superseded_provisional/`: the four provisional files cut before the maintainer decisions (skeleton, judge plan, check script, result), kept unchanged.

### Method

- Read: `target_hierarchy.md` and `maintainer_decisions.md` (they bind), the provisional skeleton's partition rationale and tree, all 814 ledger statements, the UID rules.
- Cut L2 from the branch roles in the decided hierarchy; wrote the node table before routing.
- Routing: the provisional routing of part-1 rows was the starting default, then 22 part-1 rows moved on the new rules (mechanism to ASSURANCE, practice to its realization branch, the three provisional gaps closed); all part-2 and part-3 rows routed from their statements. A generator (not kept) refused to write unless every row was routed once to an existing L2; the kept script re-proves this from the written files.
- Dropped from the provisional skeleton: the default-context table, the awaiting-scope list, the judge plan, the stack-pointer tags.

### Nodes and rows per L2

| L2 node | rows |
|---|---|
| OWNERSHIP.STANCE | 13 |
| OWNERSHIP.SELECTION | 39 |
| OWNERSHIP.LIFECYCLE | 32 |
| OWNERSHIP.CONTAINMENT | 14 |
| OWNERSHIP.SERVICES | 26 |
| OWNERSHIP.LICENCE | 10 |
| ASSURANCE.RULES | 31 |
| ASSURANCE.BEHAVIOUR | 61 |
| ASSURANCE.CONTRACTS | 18 |
| ASSURANCE.DATA_INTEGRITY | 19 |
| ASSURANCE.DOCS_SYNC | 24 |
| ASSURANCE.SECURITY | 37 |
| ASSURANCE.PERFORMANCE | 22 |
| ASSURANCE.AVAILABILITY | 23 |
| ASSURANCE.ARTIFACT | 8 |
| CONSTRUCTION.DESIGN | 5 |
| CONSTRUCTION.SYSTEM_SHAPE | 10 |
| CONSTRUCTION.HIDING | 11 |
| CONSTRUCTION.BOUNDARY | 24 |
| CONSTRUCTION.STATE | 13 |
| CONSTRUCTION.DEPENDENCY_DIRECTION | 3 |
| CONSTRUCTION.NAMING | 4 |
| CONSTRUCTION.PARADIGM | 4 |
| CONSTRUCTION.DATA_NOT_CODE | 10 |
| CONSTRUCTION.PROCESS | 3 |
| CHANGE_FLOW.INTEGRATION | 18 |
| CHANGE_FLOW.REVIEW | 11 |
| CHANGE_FLOW.BUILD | 5 |
| CHANGE_FLOW.RELEASE | 10 |
| CHANGE_FLOW.DEPLOY | 9 |
| CHANGE_FLOW.ROLLBACK | 6 |
| CHANGE_FLOW.DATA_CHANGE | 52 |
| CHANGE_FLOW.MEASURE | 5 |
| OPERATION.RELIABILITY | 12 |
| OPERATION.ALERTING | 6 |
| OPERATION.TELEMETRY | 36 |
| OPERATION.INCIDENTS | 9 |
| OPERATION.CAPACITY | 7 |
| OPERATION.READINESS | 5 |
| OPERATION.RUNBOOKS | 3 |
| OPERATION.RECOVERY | 31 |
| OPERATION.FEEDBACK | 1 |
| EVOLUTION.DECISIONS | 12 |
| EVOLUTION.INCREMENTAL | 11 |
| EVOLUTION.DEBT | 13 |
| EVOLUTION.DECOMMISSION | 11 |
| EVOLUTION.TECHNOLOGY | 6 |
| TRANSVERSE.DOCS | 8 |
| TRANSVERSE.SECURITY | 14 |
| TRANSVERSE.SECURITY_MONITORING | 17 |
| TRANSVERSE.PRIVACY | 13 |
| TRANSVERSE.CONFIG | 15 |
| TRANSVERSE.ENVIRONMENTS | 4 |

### Script output

```text
ledger rows: 814 (part 1 460, part 2 289, part 3 65)
routed: 814; unrouted: 0; routed twice: 0; unknown ids: 0
nodes: ROOT 1, L1 7, L2 53 (total 61)
  OWNERSHIP    L2 nodes  6, rows 134
  ASSURANCE    L2 nodes  9, rows 243
  CONSTRUCTION L2 nodes 10, rows  87
  CHANGE_FLOW  L2 nodes  8, rows 116
  OPERATION    L2 nodes  9, rows 110
  EVOLUTION    L2 nodes  5, rows  53
  TRANSVERSE   L2 nodes  6, rows  71
PASS: all 814 ledger rows routed exactly once to an existing L2 uid, 0 unrouted, uids follow the rules, counts agree with tree_l2.md
```

### Open, for the maintainer or the L3 step

1. Small L2 nodes: OPERATION.FEEDBACK holds 1 row, and DEPENDENCY_DIRECTION, PROCESS and RUNBOOKS 3 each. Recommendation: keep, since each is named in the decided hierarchy; merge into a sibling only if L3 finds nothing more to say.
2. CONSTRUCTION.DESIGN and CONSTRUCTION.SYSTEM_SHAPE are not in the decided CONSTRUCTION list. Recommendation: accept them as L2 nodes of CONSTRUCTION; the alternative is to treat system shape as out of scope (it concerns hosted services, which MD-05 keeps in scope).
3. The split-topic content holders (security and data in particular) follow row counts, not a maintainer ruling. Recommendation: accept; the L3 step must state each fact in one node only (MD-03).
4. Boundary rows (141) are listed with their reason in `routing.md`; the L3 judges may move a row, but must keep it routed once.
