# CHANGE_FLOW branch refinement: result

## L1 headline

The CHANGE_FLOW branch is cut below its 8 L2 nodes into 34 L3 nodes, and all 116 routed rows are attached, each to one L3 node, with the competing positions listed and no verdict (grounded: the script ran and passed).

- Pins: 43 nodes (1 L1, 8 L2, 34 L3). 116 rows attached, 0 unattached. Script line: `PASS: all routed rows attached once, uids valid, links resolve`. 3 routing objections (L1062, L141, L409), none moved.
- Where the judges will spend effort (grounded, from the rows): `DATA_CHANGE` holds 52 rows in 8 nodes, with the maintainer's manual production lane and environment-divergence rules (L290, L328) contradicting the public same-process-everywhere rules (L159, L165); review depth (L1044), merge method (L130), rollout strategy (L160) and rollback style (L387, L288 against L162) are contested with stated conditions.
- Open (inferred or unsettled in the rows): the winner among merge methods, push against pull deploys, calendar versioning, AI-reviewer accuracy, and the public counterpart of several maintainer data-job rules (L411, L412, L413).
- Files: `branch.md` (tree and node records), `check_branch.py`, this file.

## L2 claims

Each claim marked grounded (read from the rows), inferred (my cut or reading) or open (rows leave it unsettled). Pins repeated: 43 nodes (1 L1, 8 L2, 34 L3); 116 rows attached, 0 unattached; script line `PASS: all routed rows attached once, uids valid, links resolve`; 3 routing objections.

- `CHANGE_FLOW.INTEGRATION` (18 rows, 6 L3 nodes): holds the repository, integration cadence, branching model, merge and commit practice, mainline health, and change attribution. Grounded: positions are contested on cadence (daily trunk against feature branches, L125), merge method (L130, no source ranks them: open) and disclosure (L1077); consensus elsewhere. The attribution cluster (L1061, L1062, L1076, L1077) is the author-neutral part of MD-02; I would move L1062 to `ASSURANCE.SECURITY` (objection).
- `CHANGE_FLOW.REVIEW` (11 rows, 4 L3 nodes): holds mechanism and depth by risk, unit and speed, the approval standard, and automated layers. Grounded: the mechanism (L137) and the depth rule (L1044) are contested, the maintainer's named-senior escalation (L298) is a named position. Objection: L141 would sit in `ASSURANCE.RULES`.
- `CHANGE_FLOW.BUILD` (5 rows, 2 L3 nodes): holds what every build is and build-once promotion. Grounded: consensus, no competing position except rebuilding per environment, which no row argues for. Inferred: the "same artifact" clause of L150 (the row says so).
- `CHANGE_FLOW.RELEASE` (10 rows, 5 L3 nodes): holds cadence, version identity, flags, staged pipeline with human gates, and who may release. Grounded: cadence (L153) and gates (L156) are contested with stated conditions. Open: calendar versioning (L135).
- `CHANGE_FLOW.DEPLOY` (9 rows, 4 L3 nodes): holds the automated path, rollout strategy and canary evaluation, environment parity, and instance replacement. Grounded: parity (L165) and rollout strategy (L160) are contested; the maintainer's L290 and L328 (attached in `DATA_CHANGE.3`) contradict L159 and L165 per the coverage check. Open: pull against push deploys (L167).
- `CHANGE_FLOW.ROLLBACK` (6 rows, 3 L3 nodes): holds the decision to roll back, reversibility by design, and undoing a data change. Grounded: rollback against fix forward (L162) has no decision rule in any source (inferred conditions); undoing a data change has three positions (L387 a, b, and the maintainer's hybrid L288). Inferred: the generic expand-migrate-contract rule (L163) overlaps `DATA_CHANGE.4`; stated once there for data, once here as the generic rule.
- `CHANGE_FLOW.DATA_CHANGE` (52 rows, 8 L3 nodes): holds the procedures of the data split topic (MD-03): form, history, delivery path, order, locks, bulk design, rehearsal, running a job. Grounded: 18 of the 52 rows are maintainer rows (MAINT, source REG-181), each a named position; contested nodes are the delivery path (`.3`), declarative against versioned source (`.1`), compatibility layer (`.4`), backfill location and rehearsal data (`.6`, `.7`). Open: L411, L412, L413 (no public counterpart found).
- `CHANGE_FLOW.MEASURE` (5 rows, 2 L3 nodes): holds the outcomes that judge delivery and how a measured gain is trusted. Grounded: the five metrics (L169) are consensus; the net effect of automation (L1058) is contested. Inferred: "not to rank people" (L169).

## L3 full

Format per node: uid, name; rows; the positions in one line each, with the condition each is recorded to win under; certainty. Positions, sources and conditions in full are in `branch.md`. Pins repeated: 43 nodes (1 L1, 8 L2, 34 L3); 116 rows attached, 0 unattached; script line `PASS: all routed rows attached once, uids valid, links resolve`; 3 routing objections; 142 positions, 70 links in the records.

### INTEGRATION

- `.1` Repository Content and Shape; L124, L1190, L132. Everything to build and restore in version control (consensus); one codebase per app; monorepo against multiple repositories against virtual monorepo, by access segmentation (L132). Grounded; the repository debate rests on one T2 source.
- `.2` Integration Frequency and Branch Life; L125, L128, L129. Daily trunk (full-time team, strong tests) against feature branches merged when complete (open source, sparse contributors); avoid long-lived branches; hide unfinished work behind flags. Grounded.
- `.3` Branching Model and Release Branches; L126, L127. Trunk or GitHub flow for one live version against git-flow when several versions are supported; release branch just in time against none. Grounded.
- `.4` Merge Method and Commit Practice; L130, L133, L134. Squash, rebase, merge commit (no source ranks them: open); atomic commits; structured messages only if generated from history against free-form. Grounded on effects, open on the winner.
- `.5` Mainline Health and Batch Size; L146, L172, L1057. Revert a broken mainline first; small batches with routine rollback (L172 and L1057 state the same thing). Grounded; no competing position.
- `.6` Change Attribution and Actor Rules; L1061, L1062, L1076, L1077. Attributable record, distinct automation identities, stated actor boundaries; disclosure of tool use against one bar for all (reviewer capacity and intake). Grounded; the contest in L1077 is inferred.

### REVIEW

- `.1` Mechanism and Depth by Risk; L137, L1044, L298. Mandatory approval, pairing, ship/show/ask; uniform bar against depth scaled by understanding; maintainer escalation to named seniors. Grounded.
- `.2` Unit of Review and Response Speed; L140, L1048, L139. About 100 lines, review capacity as the constraint, one-business-day response. Grounded; the causal reading of L1048 is inferred.
- `.3` What the Reviewer Reads and Approves; L138, L142, L297. Approve on net code-health improvement; review as knowledge transfer; maintained anti-pattern catalog (stale catalog misdirects). Grounded.
- `.4` Automated and Second-Model Layers; L141, L1049. Automation first; second model as extra layer against human-only gate by risk. Grounded as vendor statements; open on AI-reviewer accuracy.

### BUILD

- `.1` Scripted, Hermetic, Visible Build on Every Push; L144, L148, L149. Self-testing build on every push, hermetic builds, visible state with audit trail. Grounded; if L331 (elsewhere) is confirmed it contradicts L144.
- `.2` Build Once, Promote One Artifact; L150, L1191. Separate build, release, run; immutable releases; one artifact to every environment; rebuild per environment is the unargued alternative. Grounded except the promote clause (inferred per the row).

### RELEASE

- `.1` Cadence and Batch Size; L1200, L153. Continuous, scheduled train, explicit versions, by release model; DORA warning on frequency without supporting practices. Grounded.
- `.2` Version Identity; L135. Semantic Versioning for consumed public APIs; release identifier for single-live-version services; calendar versioning open. Grounded and inferred (service rule).
- `.3` Separating Release From Deployment; L1201, L154, L155. Flags against no flags with small batches; toggles as inventory with expiry. Grounded (single source for the inventory rule).
- `.4` Staged Pipeline and Human Gates; L1199, L156. Staged pipeline; hands-off against human gates (criticality, regulation, confidence in automation). Grounded.
- `.5` Who May Release and When; L157, L164. Restrict release operations, keep release self-service; block deploys during incidents and outside responder hours. Grounded (single sources).

### DEPLOY

- `.1` Automated Deployment Path; L159, L1198. Same process everywhere; admin processes run as the app does. Grounded; contradicted by the maintainer's L290 and L328.
- `.2` Rollout Strategy and Canary Evaluation; L160, L161, L173. Blue-green, canary, one-box and waves; concurrent-control canary evaluation; assume outages come from change. Grounded.
- `.3` Environment Parity; L165, L1194. Full parity against reduced pre-production with canary against lightweight stand-ins; maintainer divergence-and-route (L328). Grounded; contested.
- `.4` Instance Replacement and Desired State; L166, L167. Replace instances against managed mutable servers; pull-and-reconcile against push from CI. Grounded; open on the comparison.

### ROLLBACK

- `.1` Detecting and Deciding to Roll Back; L162. Automated rollback on alarm against fix forward. Grounded positions; decision rule inferred.
- `.2` Reversible by Design; L163, L1072. Backward-compatible changes; every automated change reversible through version control. Grounded.
- `.3` Undoing a Data Change; L288, L387, L390. Written reverse; compatibility plus roll-forward plus restore; maintainer forward-only with documented undo; last reversible point. Grounded.

### DATA_CHANGE

- `.1` Form and Source of a Change; L379, L286, L1196, L381, L289, L1197, L385, L406. Migration scripts applied by automation; declarative against versioned source of truth; idempotent DDL as defence in depth; smallest change; separate folder for urgent fixes. Grounded; hybrid recommendation from one vendor.
- `.2` Migration History and Immutability; L380, L287, L418. History record, never edit an applied migration, state tracked in the target database. Grounded; the "never edit" form partly inferred.
- `.3` Delivery Path and Gating of Database Change; L168, L290, L410, L291, L294, L411, L328, L408. Same pipeline; fully automated against the maintainer's risk-split manual lane; unmerged release approval; registry content by script against by migration; divergence-and-route against parity; involve production DB owners. Grounded; contested; L411 open.
- `.4` Order and Compatibility With Running Code; L382, L383, L384, L386, L292, L409, L419. Schema before application; expand, migrate, contract; own the contract step; both versions on the same data; declared minimum schema version (explicit gate open); stop reads before drop; compatibility layer (views, access layer, function interface). Grounded; L409 contested.
- `.5` Locks and Online Schema Change; L392, L393, L394, L395, L397, L304. Know the lock; session lock timeout with retry; non-blocking forms; non-transactional step; copy-and-swap tools by write rate; do not shard schema changes. Grounded; mostly stack-tagged (Postgres, MySQL).
- `.6` Bulk and Backfill Design; L299, L300, L398, L399, L401, L307, L407. Four-decision procedure with a size gate; bounded throttled batches; re-runnable batches; backfill location by duration (migration, background job, offline snapshot); compose standard tools against a framework; data apart from schema. Grounded; L399 transfer inferred.
- `.7` Rehearsal and Time Budget; L293, L402, L403, L404, L405. Production-shaped against developer sample data; dump-restore workflow with skip markers; measure on a copy; time budget by class; mask personal data. Grounded; vendor sources are interested parties.
- `.8` Running and Watching a Production Data Job; L301, L302, L303, L305, L306, L400, L412, L413. Convergence query as "done"; ramp ladder with halt on first failure and a ledger; pre-start checklist; pause and pace on replica lag; watch the target system; ticket key in statements. Grounded as maintainer practice; L412 and L413 open (no public counterpart).

### MEASURE

- `.1` Outcomes That Judge Delivery; L169, L170, L1058. Five DORA metrics; speed and stability correlated given supporting practices; outcomes not volume, with a contested net effect of automation. Grounded; "not to rank people" inferred.
- `.2` Independent Baselines and Preconditions; L1059, L1060. Measure against an independent baseline; fundamentals as preconditions. Grounded for findings (small samples), inferred for the principles.

### Routing objections (3)

- L1062 to `ASSURANCE.SECURITY` (enforced limits on automation). Inferred.
- L141 to `ASSURANCE.RULES` (where a check runs before review). Inferred.
- L409, second clause (database access behind a code layer), to `CONSTRUCTION.HIDING`. Inferred.
