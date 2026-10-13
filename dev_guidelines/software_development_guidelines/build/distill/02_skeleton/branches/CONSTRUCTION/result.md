# Branch CONSTRUCTION: result

Files beside this one: `branch.md` (tree and one record per node, the full content), `check_branch.py` (the proof). Each of the three sections below can be read alone.

## L1 headline

The CONSTRUCTION branch is cut below its ten L2 nodes into 38 L3 nodes, and all 87 routed rows are attached, each to exactly one node, with the competing positions listed and no verdict (grounded: the script proves coverage, uids and links).

- Nodes: 49 (L1 1, L2 10, L3 38).
- Rows attached: 87; unattached: 0.
- Script: PASS: branch CONSTRUCTION: 49 nodes, 87 rows each attached once, 0 unattached, uids and links valid.
- Routing objections: 5 (L1535, L1536, L1286, L1265, L1235); no row was moved.
- Rows flagged as not language-neutral: 4 (L1501, L1518, L1514, L1288).
- Where the judges will find real disagreement (inferred from the rows, not a ruling): parse once versus validate everywhere (BOUNDARY.1), cut by business concept versus by layer (HIDING.2 against HIDING.3), normalize versus denormalize (STATE.2), logic in the application versus the database (PARADIGM.2), views versus functions as a stable interface (BOUNDARY.4 against BOUNDARY.5), independent deployment versus coordinated breaking changes (SYSTEM_SHAPE.3).
- Weakest grounding (open): declared layering (DEPENDENCY_DIRECTION.2), the contract-document format question (BOUNDARY.3 position on L1287), two clauses of L1532 and L1535 that no source grounds.

## L2 claims

Pin (same at every level): Nodes: 49 (L1 1, L2 10, L3 38). Rows attached: 87; unattached: 0. Script: PASS: branch CONSTRUCTION: 49 nodes, 87 rows each attached once, 0 unattached, uids and links valid. Routing objections: 5. Rows flagged as not language-neutral: 4.

Certainty marks are on the claim "the node is cut and attached as stated and its positions are the ones the rows record"; the rows' own certainty is carried in `branch.md` per position. Cuts are my reading of each node's intent (inferred); coverage is proven by the script (grounded). Row counts per L2 node equal `tree_l2.md`.

| L2 node | rows | L3 cut | claim | mark |
|---|---|---|---|---|
| CONSTRUCTION.DESIGN | 5 | 4: derivation order; effort and timing on costly decisions; properties first then constraints; growth horizon | Four separate design questions; only the derivation order (maintainer row L329) has a recorded rival (test-first or emergent design). The others are single-practice rows. | cut inferred, rows grounded |
| CONSTRUCTION.SYSTEM_SHAPE | 10 | 4: initial shape; distribution premium and reversal; placing boundaries; teams and structure | Monolith-first is the majority position with services-first recorded as the unread opposite; the one direct contradiction is independent deployability (L171) against coordinated breaking changes (L295, routed elsewhere). Context variables: team size, system complexity, operating cost per service, each quoted from its row. | cut inferred, rows grounded |
| CONSTRUCTION.HIDING | 11 | 4: cut by hidden decision; by business concept or layer; presentation, domain, data access; one owner per schema | The roll-up row L1511 sits on the node itself. Rows L1215 (cut by concept, not by layer) and L1220 (separate layers) pull on the same axis; no row says which wins. | cut inferred, rows mostly grounded, single-source for the Parnas and Cook rows |
| CONSTRUCTION.BOUNDARY | 24 | 6: parse or validate; what counts as valid; what a contract states; contract over stored data; call shape; errors | Largest node. Maintainer rows L309 (signature over shape-bound), L315 (errors) are named positions. Parse-once (L1274) and validate-at-every-boundary (L1505) differ in wording and possibly outcome; no row settles it. The database-as-contract question is contested and carries two row-quoted context variables. | cut inferred, rows grounded, L1287 open |
| CONSTRUCTION.STATE | 13 | 5: one place per fact; normal form; shared derived state; value precision and mutability; load-time effects | Normalize by default (L1263) against denormalize where measured performance requires (L1265) is the one stated competition; precision and mutability rows are single-source. | cut inferred, rows grounded, L1502 preference open |
| CONSTRUCTION.DEPENDENCY_DIRECTION | 3 | 2: no cycles; declared layering | Node-level row L1519 plus two children. Cycles are tolerated by one documentation page (no recommendation); layering has no admitted ground. | open for layering, inferred for cycles |
| CONSTRUCTION.NAMING | 4 | 3: whole words; one concept one name; names derived from concepts | Node-level row L1522 plus three one-row children; the evidence is two experiments and four style-guide positions, language of one experiment is C#. | grounded for the experiments, inferred for transfer |
| CONSTRUCTION.PARADIGM | 4 | 2: paradigm by intent; placement of domain logic | Paradigm by intent rests on absence of evidence plus a contested language-effect study; application-first against database logic is contested with the database side not found at T1 or T2. Context variable: team comfort with SQL (L1260). | inferred (paradigm), contested (placement) |
| CONSTRUCTION.DATA_NOT_CODE | 10 | 5: code and commands; queries; paths and destinations; structured payloads; secrets and tokens | Roll-up rows L1527 and L1528 on the node. Mostly consensus on T1 sources; rejected positions recorded (escaping as primary defence, non-SQL immunity, denylisting). Two rows are objected (L1535, L1536). | cut inferred, rows grounded, two clauses open |
| CONSTRUCTION.PROCESS | 3 | 3: fast start and graceful stop; fail fast under supervision; stateless processes | Three single-practice rows, no recorded rival. | grounded |

Objections (rows stay where routed): L1535 to TRANSVERSE.CONFIG; L1536 to TRANSVERSE.SECURITY; L1286 and L1265 to ASSURANCE.DATA_INTEGRITY; L1235 to EVOLUTION.INCREMENTAL.

Language-neutrality flags: L1501 and L1518 (scoped by their own text to languages with binary floating point or load-time module code), L1514 (presumes abstract data types and objects), L1288 (names Postgres, Python, TypeScript). Technology-bound but language-independent rows (SQL, relational, HTTP, XML, schema formats) are listed in `branch.md`, not counted.

## L3 full

Pin (same at every level): Nodes: 49 (L1 1, L2 10, L3 38). Rows attached: 87; unattached: 0. Script: PASS: branch CONSTRUCTION: 49 nodes, 87 rows each attached once, 0 unattached, uids and links valid. Routing objections: 5. Rows flagged as not language-neutral: 4.

Attachments by node (row ids; the positions, forces, conditions and source ids are in `branch.md`). Mark: coverage grounded (script); the cut inferred.

- CONSTRUCTION (L1): none.
- CONSTRUCTION.DESIGN: none at node; .1 L329 (MAINT position named); .2 L1206, L1209; .3 L1226; .4 L1235 (objection to EVOLUTION.INCREMENTAL).
- CONSTRUCTION.SYSTEM_SHAPE: none at node; .1 L1210, L1211, L1214, L1218; .2 L1212, L1219; .3 L171, L1213; .4 L1221, L1222.
- CONSTRUCTION.HIDING: node L1511; .1 L1512, L1513, L1514 (flagged), L1515; .2 L1215, L1217; .3 L1220, L1223, L1224; .4 L1225.
- CONSTRUCTION.BOUNDARY: node L1503; .1 L1504, L1505, L1274, L1275, L1280; .2 L1506, L1507, L1508; .3 L1268, L1269, L1270, L1288 (flagged), L1289, L1287; .4 L1285, L1286 (objection to ASSURANCE.DATA_INTEGRITY); .5 L309 (MAINT position named), L1509, L1272, L1279, L1278; .6 L315 (MAINT position named), L1273.
- CONSTRUCTION.STATE: none at node; .1 L1516, L1517, L1276; .2 L1263, L1264, L1265 (objection to ASSURANCE.DATA_INTEGRITY), L1266, L1267; .3 L1204, L1205; .4 L1501 (flagged), L1502; .5 L1518 (flagged).
- CONSTRUCTION.DEPENDENCY_DIRECTION: node L1519; .1 L1520; .2 L1521 (open).
- CONSTRUCTION.NAMING: node L1522; .1 L1523; .2 L1524; .3 L1525.
- CONSTRUCTION.PARADIGM: none at node; .1 L1526; .2 L1259, L1260, L1261.
- CONSTRUCTION.DATA_NOT_CODE: node L1527, L1528; .1 L1529, L1530; .2 L1531; .3 L1532, L1534; .4 L1533, L1536 (objection to TRANSVERSE.SECURITY); .5 L1535 (objection to TRANSVERSE.CONFIG).
- CONSTRUCTION.PROCESS: none at node; .1 L1202; .2 L1510; .3 L1203.

Per-claim certainty, the rows' own certainty as recorded (the judges re-examine):

- Grounded (consensus, T1 or T2): SYSTEM_SHAPE rows L1211 to L1214, L1221, L1222; HIDING L1220, L1223, L1225; BOUNDARY L1268 to L1270 (units and invariants synthesis inferred), L1505 to L1507, L1274; STATE L1263, L1264, L1267; DATA_NOT_CODE L1529 (rule), L1531, L1533, L1534; PROCESS L1202, L1203.
- Grounded but single-source: L1274, L1508, L1513, L1514, L1517 (for shared data only), L1523, L1525, L1530, L1510, L1536, L1533 (signing clause).
- Inferred: L1501 (positive statement), L1518, L1520, L1509 (as a general principle), L1515, L1205, L1535 and L1532 (their ungrounded clauses are open), roll-up rows L1503, L1504, L1511, L1512, L1516, L1519, L1522, L1527, L1528.
- Open: L1521 (no admitted ground for layering), L1287 (no source says whether the contract format applies to an application database), L1502 (no preference between immutability and read-only is derived), the "checked after resolution, used without a race" clause of L1532, the "audited mechanisms" clause of L1535.
- Contested: L1259 (application against database logic), L1285 (database as contract), L1526 (paradigm effect on defects, contested fact), L1210 (monolith first; services-first side not read).

Context variables added, each from a row's own words (MD-02): team size and system complexity (SYSTEM_SHAPE.1, L1218, L1211); services against operating cost (SYSTEM_SHAPE.2, L1219); coercion per boundary kind (BOUNDARY.1, L1280); data leaving the application for a platform team (BOUNDARY.3, L1287); consumers and privilege separation (BOUNDARY.4, L1285); measured performance (STATE.2, L1265); team comfort with SQL (PARADIGM.2, L1260). No node carries a context variable the rows do not state.

Rows judged earlier in the JavaScript guideline (L1501 to L1536, 36 rows) keep that verdict as one position labelled "prior verdict" and are not inherited; the origin's dropped JavaScript-specific parts stay dropped. Rows flagged but kept: a flag marks that the statement as written does not hold for every language (the maintainer's ruling); the judges decide whether to scope or rewrite it.
