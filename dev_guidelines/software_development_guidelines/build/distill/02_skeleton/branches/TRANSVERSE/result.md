# Result: TRANSVERSE branch refinement

Pinned at every level: 36 nodes (TRANSVERSE 1, L2 6, L3 29); rows attached 71 of 71, unattached 0; script line `PASS: 36 nodes, 71 of 71 rows attached once, 0 unattached, links and uids valid`; routing objections 3.

## L1 headline

TRANSVERSE is cut into 36 nodes (1 L1, 6 L2, 29 L3) with all 71 routed rows attached once, 0 unattached; `check_branch.py` prints `PASS: 36 nodes, 71 of 71 rows attached once, 0 unattached, links and uids valid`. Positions are listed per node without verdict; 3 routing objections (L263, L1257, L1159) are listed, no row moved. Certainty: the cut and coverage are grounded (script run); the L3 partition is inferred (my reading of each node's intent); the 3 objections are inferred.

## L2 claims

Pin: 36 nodes; 71 of 71 rows attached, 0 unattached; `PASS: 36 nodes, 71 of 71 rows attached once, 0 unattached, links and uids valid`; 3 routing objections.

- `TRANSVERSE.DOCS` (8 rows, 5 L3): index node of `ASSURANCE.DOCS_SYNC` for authoring and organisation practice. Positions compete mainly on how much documentation to keep (minimal, living, full docs-as-code, L236) and on how guidelines are derived (induced from practice or deduced from principles, L323). Three rows are maintainer practice (L321 to L323, named positions). Certainty: grounded for the cut; the documentation-amount positions are grounded, their context mapping inferred (ledger).
- `TRANSVERSE.SECURITY` (14 rows, 6 L3): index node of `ASSURANCE.SECURITY` for programme practice. The contested points are the anchor framework (requirements standard, maturity model, descriptive benchmark, L1120), the trigger for threat modelling (continuous against risk-triggered, L241), and disclosure policy against bounty against penetration test alone (L1142). Open: no source shows higher maturity scores reduce incidents (L1162). Certainty: cut grounded; positions grounded; L1142 commercial position open.
- `TRANSVERSE.SECURITY_MONITORING` (17 rows, 5 L3): what is logged, protected, detected and kept. Mostly one practice per row; the one internal split is the security event log against the business audit trail (L1252, inferred, no source states it) and the history mechanism (audit log against temporal model, L1250). Certainty: grounded except L1147 figure (dated) and L1149 (inferred).
- `TRANSVERSE.PRIVACY` (13 rows, 4 L3): minimisation, retention, erasure, impact assessment and breach. Competing positions: retain the legal minimum against retain long and tier by age (L1150); how an erasure request reaches backups and logs is open (L1157) and in tension with immutable backups (L1114). Certainty: grounded for text; open on backups and logs.
- `TRANSVERSE.CONFIG` (15 rows, 6 L3): separation, delivery channel, per-environment shape, secret custody, credential lifetime, leak response. Contested: environment variables against files or a store API (L254, L1238, L1193), granular variables against named bundles (L255), short-lived dynamic against rotated static credentials (L258). Several rows restate one another and were kept apart by the ledger (L158 and L1192; L257 and L1239). Certainty: grounded for positions; the leak vectors of environment variables and the merits of the weaker positions are inferred (ledger).
- `TRANSVERSE.ENVIRONMENTS` (4 rows, 3 L3): separation, definition mechanism (container, pinned package set, manifests only, L262), toolchain control. Certainty: grounded for features, inferred for comparative costs (ledger).
- Context variables (MD-02) are added only where a row says the best practice moves: scope and life of the system (L236), programme scope (L1120), criticality and regulation (L241, L1158), triage capacity (L1142), criticality and platform (L254, L1238, L258), number of deployments (L255), query frequency over history (L1250), skill mix and languages (L262), codebase maturity (L323). No default team is set.
- Routing objections, rows left in place: L263 to `OWNERSHIP.LIFECYCLE`; L1257 to `CHANGE_FLOW.DATA_CHANGE`; L1159 to `OPERATION.INCIDENTS` (inferred).

## L3 full

Pin: 36 nodes (TRANSVERSE 1, L2 6, L3 29); rows attached 71 of 71, unattached 0; `PASS: 36 nodes, 71 of 71 rows attached once, 0 unattached, links and uids valid`; routing objections 3. Full records with positions: `branch.md` beside this file; check: `check_branch.py`.

### Nodes and rows (attachment)

| L3 node | rows | competing positions |
|---|---|---|
| `TRANSVERSE.DOCS.1` Documentation Budget | L231, L236 | 4 (invest; minimal; living; full docs-as-code) |
| `TRANSVERSE.DOCS.2` Organisation and Structure | L233, L234, L321 | 3 (small modules; by reader need; maintainer router set) |
| `TRANSVERSE.DOCS.3` Layered Writing and Audience Split | L322 | 1 (maintainer) |
| `TRANSVERSE.DOCS.4` Release Changelog | L235 | 2 (human-written; generated, alternative named only) |
| `TRANSVERSE.DOCS.5` Basis and Evolution of Guidelines | L323 | 2 (maintainer: induced; deduced) |
| `TRANSVERSE.SECURITY.1` Anchor Framework | L240, L250, L1120, L1121 | 4 (outcome list; ASVS; SAMM; BSIMM) |
| `TRANSVERSE.SECURITY.2` Maturity Targets and Cycle | L1123, L1124, L1125, L1162 | 3 plus 1 open point |
| `TRANSVERSE.SECURITY.3` Design-Time Risk Modelling | L241, L242 | 3 (continuous; risk-triggered; four questions) |
| `TRANSVERSE.SECURITY.4` Responsibility and Training | L249 | 1 |
| `TRANSVERSE.SECURITY.5` Vulnerability Response Loop | L253 | 1 |
| `TRANSVERSE.SECURITY.6` Disclosure Policy and Bounty | L1141, L1142 | 4 (published policy; policy only; bounty; pen test alone) |
| `TRANSVERSE.SECURITY_MONITORING.1` Events Logged | L1143, L1073 | 2 |
| `TRANSVERSE.SECURITY_MONITORING.2` Entry Content, Time and Format | L1144, L1245, L1248 | 3 |
| `TRANSVERSE.SECURITY_MONITORING.3` Log Protection and Sanitising | L1145, L1151, L1247, L1254 | 4 |
| `TRANSVERSE.SECURITY_MONITORING.4` Detection and Escalation | L1146, L1147, L1149 | 3 |
| `TRANSVERSE.SECURITY_MONITORING.5` Business Audit Trail | L1252, L1246, L1249, L1250, L1251 | 5 (P4 holds two mechanisms) |
| `TRANSVERSE.PRIVACY.1` Minimisation, Classification and Design-In | L1153, L1152, L1155, L1156 | 4 |
| `TRANSVERSE.PRIVACY.2` Retention Periods | L1150, L1154 | 3 |
| `TRANSVERSE.PRIVACY.3` Erasure and Deletion Mechanism | L1157, L1258, L1257, L1114 | 4 |
| `TRANSVERSE.PRIVACY.4` Privacy Risk, Impact Assessment and Breach | L1161, L1158, L1159 | 3 |
| `TRANSVERSE.CONFIG.1` Separation from Code and Secrets | L158, L1192, L256, L261 | 3 |
| `TRANSVERSE.CONFIG.2` Delivery Channel | L254, L1238, L1193 | 3 (environment variables; files or store API; versioned non-secret config) |
| `TRANSVERSE.CONFIG.3` Shape of Per-Environment Configuration | L255 | 2 (granular variables; named bundles) |
| `TRANSVERSE.CONFIG.4` Central Secret Custody and Lifecycle | L257, L1239 | 2 (same practice, kept apart by the ledger) |
| `TRANSVERSE.CONFIG.5` Credential Lifetime and Pipeline Identity | L258, L259, L1069, L1240 | 5 (dynamic; static rotated; federated tokens; automation; CI as production) |
| `TRANSVERSE.CONFIG.6` Response to a Leaked Secret | L252 | 1 |
| `TRANSVERSE.ENVIRONMENTS.1` Separation and Isolation | L260 | 1 |
| `TRANSVERSE.ENVIRONMENTS.2` Definition Mechanism | L262 | 3 (container; pinned package set; manifests) |
| `TRANSVERSE.ENVIRONMENTS.3` Toolchain Control and Hardening | L263, L264 | 2 |

### Certainty (each claim marked)

- Grounded (script run): every row of the 71 is attached to exactly one node, 0 unattached, 0 attached twice; uids follow the rules; links resolve; the three maintainer rows (L321, L322, L323) are named positions; L2 row counts equal the counts in `tree_l2.md`.
- Inferred: the L3 partition and node names (my reading of each L2 intent; no row states them); the linking to other nodes (all `see` links, except `Realizes` for the split-topic nodes, which follows the split-topics table of `tree_l2.md`); the three routing objections.
- Open, carried from the ledger: effect of maturity scores on incidents (L1162); the weaker positions' arguments marked inferred (L255 named bundles, L258 static rotation, L262 Nix limits, L254 leak vectors); erasure from backups and logs (L1157); the alternative changelog generated from commits (L235); the commercial bounty position (L1142).

### Notes for the judges (pointers, no verdict)

- Duplicate-statement rows kept apart by the ledger sit together: L158 with L1192 (`TRANSVERSE.CONFIG.1`), L257 with L1239 (`TRANSVERSE.CONFIG.4`), L240 with L1120 (`TRANSVERSE.SECURITY.1`), L1143 and L1073 near L1252.
- Index nodes (MD-03): `TRANSVERSE.DOCS` and `TRANSVERSE.SECURITY` carry only authoring, organisation and programme rows; I found no row that restates a mechanism held by `ASSURANCE.DOCS_SYNC` or `ASSURANCE.SECURITY` (checked against the statements of those nodes' routed rows).
- Single-row L3 nodes (DOCS.3, DOCS.4, DOCS.5, SECURITY.4, SECURITY.5, CONFIG.3, CONFIG.6, ENVIRONMENTS.1, ENVIRONMENTS.2): each is a distinct decision whose parent holds several; a judge may fold DOCS.3 to DOCS.5 or SECURITY.4 and SECURITY.5 into their neighbours.
- Objections: L263 (the row's own boundary note names adoption and delivery), L1257 (a bulk-removal procedure), L1159 (incident handling for a breach).
