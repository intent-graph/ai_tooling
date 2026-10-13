# CHANGE_FLOW branch: tree and node records

Realization branch: how a change travels from version control to production and back. Cut top-down from the L2 intents of `../../tree_l2.md`, then the 117 rows routed to this branch (`../../routing.md`) were attached, each to exactly one L3 node. No verdict, no ranking: positions are listed for the judges. "Wins when" states the condition under which a position would be the best, as the row records it. Rules applied: MD-01 (best for the node's purpose, so conditions are kept), MD-02 (no default team: context variables only where a row says the practice moves with it, row id quoted), MD-03 (data and schema change: this branch holds procedures; guarantees stay in `ASSURANCE.DATA_INTEGRITY`).

Row sources: ledger ids L001-L460, L1001-L1289, L1501-L1565; `REG-n` are source register ids; `MAINT` rows carry source REG-181 (not citable) and appear as named positions. Links: `Realizes` to decision nodes, `Requires`, `Conflicts`, `Refines` where a row states it, `Related` where a row cross-references another node.

## Tree

```text
CHANGE_FLOW  Change Flow
CHANGE_FLOW.INTEGRATION  Version Control and Integration
CHANGE_FLOW.INTEGRATION.1  Repository Content and Shape
CHANGE_FLOW.INTEGRATION.2  Integration Frequency and Branch Life
CHANGE_FLOW.INTEGRATION.3  Branching Model and Release Branches
CHANGE_FLOW.INTEGRATION.4  Merge Method and Commit Practice
CHANGE_FLOW.INTEGRATION.5  Mainline Health and Batch Size
CHANGE_FLOW.INTEGRATION.6  Change Attribution and Actor Rules
CHANGE_FLOW.REVIEW  Review
CHANGE_FLOW.REVIEW.1  Mechanism and Depth by Risk
CHANGE_FLOW.REVIEW.2  Unit of Review and Response Speed
CHANGE_FLOW.REVIEW.3  What the Reviewer Reads and Approves
CHANGE_FLOW.REVIEW.4  Automated and Second-Model Layers
CHANGE_FLOW.BUILD  Build and Pipeline
CHANGE_FLOW.BUILD.1  Scripted, Hermetic, Visible Build on Every Push
CHANGE_FLOW.BUILD.2  Build Once, Promote One Artifact
CHANGE_FLOW.RELEASE  Release
CHANGE_FLOW.RELEASE.1  Cadence and Batch Size
CHANGE_FLOW.RELEASE.2  Version Identity
CHANGE_FLOW.RELEASE.3  Separating Release From Deployment
CHANGE_FLOW.RELEASE.4  Staged Pipeline and Human Gates
CHANGE_FLOW.RELEASE.5  Who May Release and When
CHANGE_FLOW.DEPLOY  Deployment
CHANGE_FLOW.DEPLOY.1  Automated Deployment Path
CHANGE_FLOW.DEPLOY.2  Rollout Strategy and Canary Evaluation
CHANGE_FLOW.DEPLOY.3  Environment Parity
CHANGE_FLOW.DEPLOY.4  Instance Replacement and Desired State
CHANGE_FLOW.ROLLBACK  Rollback
CHANGE_FLOW.ROLLBACK.1  Detecting and Deciding to Roll Back
CHANGE_FLOW.ROLLBACK.2  Reversible by Design
CHANGE_FLOW.ROLLBACK.3  Undoing a Data Change
CHANGE_FLOW.DATA_CHANGE  Data and Schema Change
CHANGE_FLOW.DATA_CHANGE.1  Form and Source of a Change
CHANGE_FLOW.DATA_CHANGE.2  Migration History and Immutability
CHANGE_FLOW.DATA_CHANGE.3  Delivery Path and Gating of Database Change
CHANGE_FLOW.DATA_CHANGE.4  Order and Compatibility With Running Code
CHANGE_FLOW.DATA_CHANGE.5  Locks and Online Schema Change
CHANGE_FLOW.DATA_CHANGE.6  Bulk and Backfill Design
CHANGE_FLOW.DATA_CHANGE.7  Rehearsal and Time Budget
CHANGE_FLOW.DATA_CHANGE.8  Running and Watching a Production Data Job
CHANGE_FLOW.MEASURE  Measuring Delivery
CHANGE_FLOW.MEASURE.1  Outcomes That Judge Delivery
CHANGE_FLOW.MEASURE.2  Independent Baselines and Preconditions
```

## Routing objections

Three were raised; each is resolved in `../../objections/resolution.md` and all three are kept where routed (listed with the reason). Inferred, not checked against the sources.

- L1062 (distinct automation identities, added approval for unattributed changes): would go to `ASSURANCE.SECURITY`, whose intent names enforced limits on automation. Kept at `CHANGE_FLOW.INTEGRATION.6`: attribution is that node's subject, and the enforced limits there are sandbox and credential limits, not attribution.
- L141 (automation runs before human review): would go to `ASSURANCE.RULES`, whose intent is where a check runs and what makes a gate binding. Kept at `CHANGE_FLOW.REVIEW.4`: that node's intent is the checks that run before the reviewer, and ASSURANCE.RULES holds no position on it to merge with.
- L409 second clause (database access behind a clear layer in code): would go to `CONSTRUCTION.HIDING`; the first clause (compatibility layer during a transition) belongs here. Kept at `CHANGE_FLOW.DATA_CHANGE.4`: a row is not split, and the first clause leads and carries the contested positions.

## CHANGE_FLOW Change Flow

- Intent: how a change travels from version control to production and back: integration, review, build, release, deploy, rollback, data and schema change, measurement.
- Rows: none (roll-up of its L2 nodes)
- Links: Realizes ASSURANCE (all eight L2 nodes link back to the decision nodes named below).

## CHANGE_FLOW.INTEGRATION Version Control and Integration

- Intent: how work is held in version control and merged into one mainline: branching, merge method, mainline protection, commit practice, change attribution.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.RULES

### CHANGE_FLOW.INTEGRATION.1 Repository Content and Shape

- Intent: what the repository must contain so the system can be rebuilt from it, and how repositories are cut, so that a single version of each shared component holds.
- Rows: L124, L1190, L132 (3)
- Positions:
  - P1 Keep everything needed to build, deploy and restore (source, scripts, infrastructure and application configuration, dependencies) in version control; a clean machine builds from the repository alone. Argument: reproducibility and recovery from one place. Wins always per the row (consensus; no competing position recorded). L124; REG-077, REG-092, REG-095.
  - P2 One codebase per application in version control, many deploys; code shared across applications becomes a library. Force: clear ownership of what is deployed. No competing position recorded. L1190; REG-1109.
  - P3 Monorepo. Argument: one version of each shared component is trivial to hold; atomic cross-project change (Google). Force: correctness, speed of change. Wins when one organization, tooling investment, many interdependent projects. L132; REG-106.
  - P4 Multiple repositories. Force: control, security. Wins for regulated or access-segmented work. L132; REG-106.
  - P5 Virtual monorepo (submodules or a build tool) to keep one version across several repositories. L132; REG-106. Row-level note: whichever of P3-P5 is chosen, one version of each shared component at any time keeps dependencies consistent; the debate rests on a single T2 source.
- Context variables: ACCESS_SEGMENTATION (L132: regulated or access-segmented work moves the choice to multiple repositories).
- Links: Related OWNERSHIP.LIFECYCLE (L132 boundary: the one-version rule is a dependency rule).

### CHANGE_FLOW.INTEGRATION.2 Integration Frequency and Branch Life

- Intent: how often work is merged into the mainline and how long a branch may live, and how unfinished work is kept from blocking that.
- Rows: L125, L128, L129 (3)
- Positions:
  - P1 Integrate into one mainline at least once a day, branches living hours to a couple of days (DORA: three or fewer active branches, merge daily). Argument: many small integrations reduce conflict complexity and give early feedback. Force: speed of feedback, confidence. Wins for a committed full-time team with good automated tests and a continuously deployed product. L125; REG-057, REG-077, REG-078, REG-079, REG-106.
  - P2 Feature branches merged when complete. Argument: defers integration risk, isolates unfinished work, suits sparse contributors (Fowler on open source; works when the cycle is one to two days). Force: control, low coordination cost for part-time contributors. Wins for open source with many untrusted or part-time contributors, and features of one to two days. L125; REG-077, REG-110.
  - P3 Avoid long-lived development branches: merges, regression isolation and large-scale changes cost more. Consensus. L128; REG-079, REG-106, REG-110.
  - P4 Integrate unfinished work into the mainline hidden behind flags, dark launches, keystones or branch by abstraction. Counter-force: toggle testing burden and carrying cost. Wins when the work spans more than the integration interval. L129; REG-077, REG-078, REG-089, REG-096.
- Context variables: CONTRIBUTOR_MODEL (L125: full-time team versus sparse or untrusted contributors); TEST_MATURITY (L125: P1 wins with good automated tests).
- Links: Related CHANGE_FLOW.RELEASE.3 (L129: flags, see L154 and L155 there).

### CHANGE_FLOW.INTEGRATION.3 Branching Model and Release Branches

- Intent: which branching model the release model calls for, and whether and how a release branch exists.
- Rows: L126, L127 (2)
- Positions:
  - P1 Trunk or GitHub flow when delivering continuously to one live version (Driessen himself, GitHub, Google). Force: delivery speed, low cognitive load. L126; REG-078, REG-090, REG-091, REG-106.
  - P2 Release branches (git-flow style) when software is explicitly versioned or several versions are supported in the field. Force: control, support of several versions. Wins by the number of versions in the field. L126; REG-090.
  - P3 Cut a release branch only just in time, fix defects on the mainline and cherry-pick into the release branch, delete it after release, never merge it back. L127; REG-078, REG-082, REG-106.
  - P4 No release branch: redeploy a fix from trunk (fix forward). Force: simplicity. Wins when the release cycle is hours. L127; REG-078, REG-106.
- Context variables: RELEASE_MODEL (L126: continuous delivery of one live version versus several supported versions).
- Links: Related CHANGE_FLOW.RELEASE.1 (L126, L153 both start from the release model); Related CHANGE_FLOW.ROLLBACK.1 (fix forward, L127).

### CHANGE_FLOW.INTEGRATION.4 Merge Method and Commit Practice

- Intent: how changes are merged and how a commit states what it holds, so history serves reading, reversal and automation.
- Rows: L130, L133, L134 (3)
- Positions:
  - P1 Squash merge: one commit per change, simple revert; loses the individual changes as made. Force: team cognitive load, reversibility. Wins for small changes, one logical unit per pull request. L130; REG-109, REG-114.
  - P2 Rebase merge: linear history, commits kept individually; new SHAs, loses signature verification on one hosting platform. Force: bisect granularity, history fidelity. Wins for well-structured atomic commits. L130; REG-109.
  - P3 Merge commit: complete branch history, shows when integration happened; non-linear. Force: fidelity, audit. Wins when integration events must be traced. L130; REG-109. Row-level note: decide and record one method per repository; no source read ranks the three (open on a winner); a linear-history setting can enforce the choice.
  - P4 Atomic, complete commits with a message saying what changed and why; unrelated changes in separate branches or pull requests. Consensus. L133; REG-083, REG-091. Coverage check: L318 (maintainer, mandatory unit header with dated change log) is in partial tension with L133; L318 is routed elsewhere.
  - P5 Structured commit messages (Conventional Commits) only if release notes or version bumps are generated from history. Force: automation, speed of release. Wins for libraries with many consumers and automated releases. L134; REG-030, REG-102.
  - P6 Free-form message stating what and why. Force: cognitive load. The source is review guidance, not a rule against structure (inferred). L134; REG-083.
- Context variables: none stated by a row as moving the practice beyond the "wins when" conditions above.
- Stack pointers: L130 is described in GitHub terms.

### CHANGE_FLOW.INTEGRATION.5 Mainline Health and Batch Size

- Intent: what keeps the mainline usable and the batches small, so version control remains the safety net as volume rises.
- Rows: L146, L172, L1057 (3)
- Positions:
  - P1 A broken mainline is the highest-priority work: revert the faulty change to restore it and name someone responsible. Consensus. L146; REG-057, REG-077, REG-085.
  - P2 Keep batches small, commit frequently and keep rollback routine; at high production volume version control is the safety net. Majority (one program plus the maintainer's input). L1057; REG-1041, REG-181.
  - P3 The same rule stated for AI-generated code: high code volume leads to oversized changes and delayed commits that remove the safety net of history. L172; REG-095, REG-096. L1057 and L172 state the same normative thing (kept apart because part 1 is read-only).
  - No competing position recorded for any of the three.
- Context variables: none.
- Links: Related CHANGE_FLOW.REVIEW.2 (L1048 and L172: small units protect review), Related CHANGE_FLOW.ROLLBACK.2 (L1057: routine rollback).

### CHANGE_FLOW.INTEGRATION.6 Change Attribution and Actor Rules

- Intent: how each change stays attributable to an author and an approver, and which actors may do what, whoever authored the change.
- Rows: L1061, L1062, L1076, L1077 (4)
- Positions:
  - P1 Each change carries an attributable record: who or what authored it, who approved it, which tool and session produced it. Majority. L1061; REG-1036, REG-1040, REG-114.
  - P2 Automation identities distinct from human ones; changes not attributed to a person need an additional approval. Majority (one vendor). L1062; REG-1036.
  - P3 State which actors (human, bot, agent) may do what in the change flow and which boundaries apply, so ambiguity does not become risk. Majority; grounded for the DORA capability, the author-neutral phrasing is inferred. L1076; REG-1035, REG-1037, REG-1041.
  - P4 Mandatory or recorded disclosure of tool use on a change. Force: reviewer calibration, provenance. Wins where reviewer time is scarce and intake is public. L1077 (a); REG-1036, REG-1040.
  - P5 No disclosure rule, the same bar for everyone (maintainer ruling). Force: simplicity. Wins where the bar and gates are enforced regardless of origin. L1077 (b); REG-1035. Row-level note: a platform-recorded trail (L1061) gives P4's benefit without relying on declarations.
- Context variables: INTAKE_AND_REVIEWER_CAPACITY (L1077: reviewer time scarce and public intake versus enforced gates).
- Links: Related ASSURANCE.SECURITY (L1062, see routing objections); Related CHANGE_FLOW.REVIEW.1.
- Stack pointers: L1062 mechanism is one hosting platform's.

## CHANGE_FLOW.REVIEW Review

- Intent: how review is carried out: mechanism per risk, size, speed, depth, what the reviewer reads.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.RULES

### CHANGE_FLOW.REVIEW.1 Mechanism and Depth by Risk

- Intent: which review mechanism applies to a change and how deep it goes, set by risk and by evidence that the submitter understands the change.
- Rows: L137, L1044, L298 (3)
- Positions:
  - P1 Mandatory asynchronous approval by another engineer on every change. Argument: confidence, knowledge sharing, an audit trail. Wins for larger or less-trusting teams, regulated change control, many contributors. L137; REG-083, REG-114, REG-115.
  - P2 Synchronous review or pairing (pair by default, pull-request review for exceptions). Argument: immediacy, no review queue, no context switching. Force: speed of feedback. Wins for small collocated or remote-pairing teams with trust. L137; REG-079, REG-116.
  - P3 Ship / Show / Ask: merge routine changes without approval, show after checks, ask when uncertain. Argument: approvals are a band-aid for missing trust and bottleneck the team. Force: delivery speed. Wins with high trust, strong CI/CD, an always-releasable mainline; more asking for juniors and new techniques. L137; REG-098. DORA warns against heavy review requiring several approvals (REG-079).
  - P4 One uniform bar, depth set only by risk (maintainer ruling). Force: simplicity, fairness. Wins when the bar is already high and enforced. L1044 (a); REG-1035.
  - P5 Depth scaled by the share of the change produced automatically, restated author-neutral as depth tracking evidence that the submitter understands. Force: correctness, placement of review effort. Wins when submitter understanding cannot be assumed (high volume, many contributors, public intake). L1044 (b); REG-1040, REG-1043, REG-1044.
  - P6 Escalate by risk, not by size: any change holding locks, running longer than about five minutes or affecting availability needs named senior approvers, and production runs are restricted to the same group (maintainer). Force: safety, review effort where it pays. Wins with a small trusted senior group and few critical changes. L298; REG-181. Coverage check: partial tension with L143 (no per-change approval outside peer review), routed elsewhere.
- Context variables: TEAM_SIZE_AND_TRUST (L137: wins conditions differ for large or less-trusting teams, small trusted teams); CRITICALITY (L298: wins with few critical changes; L137: regulated change control); SUBMITTER_UNDERSTANDING (L1044: P5 wins when it cannot be assumed).
- Links: Related CHANGE_FLOW.INTEGRATION.6; Related CHANGE_FLOW.DATA_CHANGE.8 (L298 and L303 both name senior review of locking or long changes).

### CHANGE_FLOW.REVIEW.2 Unit of Review and Response Speed

- Intent: how big a unit of review may be and how fast a reviewer answers, so review capacity does not become the constraint.
- Rows: L140, L1048, L139 (3)
- Positions:
  - P1 Small changes: about 100 lines typical, 1000 too large; refactoring in separate changes; tests in the same change as the logic they cover. Consensus; thresholds differ between sources (100, 200). L140; REG-083, REG-096, REG-100.
  - P2 Keep the unit of review small enough for a meaningful review and treat review capacity as the constraint when production volume rises. Majority. Some sources argue verification capacity is the binding constraint (REG-1047); REG-1041 argues small batches turn AI from neutral into positive; no source read argues the reverse; the causal reading is inferred. L1048; REG-1041, REG-1042, REG-1047, REG-181.
  - P3 Respond to a review request within one business day at most; prefer quick individual responses over a fast whole process; optimise team throughput, not one author's speed. Consensus. L139; REG-083, REG-099.
  - No competing position recorded.
- Context variables: none.
- Links: Related CHANGE_FLOW.INTEGRATION.5 (L172, L1057).

### CHANGE_FLOW.REVIEW.3 What the Reviewer Reads and Approves

- Intent: the standard a change is approved against and what material the reviewer reads.
- Rows: L138, L142, L297 (3)
- Positions:
  - P1 Approve a change when it definitely improves overall code health, even if imperfect; technical facts and data overrule preference; optional suggestions are marked as such. Consensus (one T2 source, no opposing source found). L138; REG-080.
  - P2 Review serves understanding and knowledge transfer as well as defect finding; require that a second reader can understand the change. Consensus. L142; REG-083, REG-108.
  - P3 Review uses a maintained anti-pattern catalog read by type of change (table, function, query, JSON, index), then the guideline for that change; the catalog doubles as an audit list. Maintainer decision; read as majority public practice (review checklists). Cost noted: a catalog not kept current misdirects review (it is stale against its modules). L297; REG-181.
  - No competing position recorded.
- Context variables: none.

### CHANGE_FLOW.REVIEW.4 Automated and Second-Model Layers

- Intent: which checks run before the human reviewer and whether a second automated reviewer is added, while accountable review stays with an independent responsible party.
- Rows: L141, L1049 (2)
- Positions:
  - P1 Automation (format, lint, tests, build) runs before human review so reviewers spend attention on design and logic. Consensus. L141; REG-083, REG-085.
  - P2 A second model reviewing in a fresh context as an extra layer, with accountable review still done by an independent responsible party. Force: speed of feedback, review capacity. Wins when volume exceeds human capacity and risk is low or human review stays in force. L1049 (a); REG-1038.
  - P3 Human-only gate for approval. Force: independence of failure modes, accountability. Wins when risk is high. L1049 (b); REG-1036, REG-1040. Open: no study read on AI-reviewer accuracy; vendor statements only.
- Context variables: CRITICALITY (L1049: P3 wins when risk is high); SCALE (L1049: P2 wins when volume exceeds human capacity).
- Links: Related ASSURANCE.RULES (L141, see routing objections); Related CHANGE_FLOW.BUILD.1.

## CHANGE_FLOW.BUILD Build and Pipeline

- Intent: how the build is scripted, hermetic and visible, and what runs on every push.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.ARTIFACT

### CHANGE_FLOW.BUILD.1 Scripted, Hermetic, Visible Build on Every Push

- Intent: what every build is, so the same revision gives the same result anywhere and the whole team sees the state of the pipeline.
- Rows: L144, L148, L149 (3)
- Positions:
  - P1 Run an automated build and a self-testing test suite on every push to the mainline in a reference environment, not only on developer machines. Consensus. L144; REG-057, REG-077. Coverage check: if the maintainer doctrine truly has no automated regression run (L331, routed elsewhere), it contradicts L144.
  - P2 Builds scripted, repeatable and hermetic: the same revision on different machines yields the same result, with no machine-specific state. Consensus. L149; REG-077, REG-082, REG-104.
  - P3 Make build and pipeline state and the flow of changes visible to the whole team, with an audit trail. Consensus. L148; REG-057, REG-077, REG-107.
  - No competing position recorded.
- Context variables: none.
- Links: Related ASSURANCE.BEHAVIOUR (L144 boundary: what the tests contain); Related OWNERSHIP.LIFECYCLE (L149 and L048: reproducible builds).

### CHANGE_FLOW.BUILD.2 Build Once, Promote One Artifact

- Intent: how build, release and run are separated so what is promoted through the environments is the one thing that was built.
- Rows: L150, L1191 (2)
- Positions:
  - P1 Separate build, release and run stages; releases are immutable and uniquely identified; build once and promote the same artifact to every environment, with environment-specific configuration kept outside it. Consensus. "Build once, promote the same artifact" is inferred from REG-081 and REG-092 (REG-107 does not state it). L150; REG-081, REG-082, REG-092, REG-107. L1191 states the same normative thing (REG-082, REG-107, REG-1109).
  - P2 Rebuild per environment: named in L1191 as the practice that building once replaces; no row gives an argument for it.
- Context variables: none.
- Links: Realizes ASSURANCE.ARTIFACT; Related CHANGE_FLOW.RELEASE.2 (release identifier); Related TRANSVERSE.CONFIG (configuration outside the artifact).

## CHANGE_FLOW.RELEASE Release

- Intent: how a build becomes a release: cadence, versioning, flags, staged pipeline, who may release.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.RULES

### CHANGE_FLOW.RELEASE.1 Cadence and Batch Size

- Intent: how often a release is made and how big it is.
- Rows: L1200, L153 (2)
- Positions:
  - P1 Continuous: release each merge; "faster is safer", frequency reduces difficulty. Force: delivery speed, reversibility, small blast radius. Wins with one live version, automation in place, strong tests. L153; REG-082, REG-084, REG-097, REG-112.
  - P2 Scheduled train (one search product releases every other day; a missed train waits for the next). Force: predictability, low pressure. Wins with many components and coordination across teams. L153; REG-084.
  - P3 Explicit versions with several supported. Force: consumer control. Wins for shipped products and libraries. L153; REG-090.
  - P4 Prefer small, frequent releases over large infrequent ones (the principle across P1-P3). Consensus. L1200; REG-082, REG-1110. DORA warning attached to L153: more frequency without supporting practices raises failure rate and burnout (REG-097, REG-093).
- Context variables: RELEASE_MODEL (L153: every merge, a regular train, or explicit versions).
- Links: Related CHANGE_FLOW.INTEGRATION.3; Related CHANGE_FLOW.MEASURE.1 (L170: frequency alone yields failures).

### CHANGE_FLOW.RELEASE.2 Version Identity

- Intent: what identifier a release carries and what promise that identifier makes.
- Rows: L135 (1)
- Positions:
  - P1 Semantic Versioning only for an artifact with a declared public API consumed by others. Force: consumer trust, exit risk reduction. L135; REG-030.
  - P2 A release identifier (build number or timestamp), not a compatibility promise, for a deployed service with a single live version. L135; REG-081. The service rule is inferred from REG-030 plus REG-081.
  - P3 Calendar versioning: not read in any source (open). L135.
- Context variables: RELEASE_MODEL (L135: single live version versus consumed public API).
- Links: Related CHANGE_FLOW.BUILD.2.

### CHANGE_FLOW.RELEASE.3 Separating Release From Deployment

- Intent: whether a feature is made available separately from shipping code, and what that costs.
- Rows: L1201, L154, L155 (3)
- Positions:
  - P1 Decouple release from deployment with flags so a feature can be turned off without redeploying. Force: reversibility. Majority. L154; REG-084, REG-089, REG-096, REG-112. L1201 states it with "where needed" (REG-089).
  - P2 No flags: small batches released immediately (the REG-112 style). Force: cost of ownership. L154.
  - P3 Treat toggles as inventory with a carrying cost: classify (release, experiment, ops, permission), give release toggles an expiry and a removal task created at introduction, test the relevant toggle states. Consensus (single source, no dissent found). L155, L1201; REG-089.
- Context variables: none.
- Links: Related CHANGE_FLOW.INTEGRATION.2 (L129); Related EVOLUTION.DECOMMISSION (L155 toggle expiry).

### CHANGE_FLOW.RELEASE.4 Staged Pipeline and Human Gates

- Intent: how the path to production is staged and which stages need a person's authorization.
- Rows: L1199, L156 (2)
- Positions:
  - P1 One automated pipeline of stages, early stages fast feedback and later stages more thorough confidence. Consensus. L1199; REG-107, REG-1110. Same normative thing as the staging half of L156.
  - P2 Hands-off: code review is the last manual gate, the rest automated and driven by alarms (Amazon). Force: delivery speed, reduced error. Wins with mature automation and monitoring. L156; REG-115.
  - P3 Human authorization gates for some stages. Force: control. Wins at high criticality, regulation, low confidence in automation. L156; REG-107. Access control on who may release stays in either (REG-082).
  - Cross-reference: the maintainer's manual production lane for database changes (L290, at `CHANGE_FLOW.DATA_CHANGE.3`) sits inside the contested range of L156.
- Context variables: CRITICALITY and REGULATION (L156: P3 wins at high criticality or regulation); TEST_MATURITY (L156: P2 wins with mature automation and monitoring, P3 when confidence in automation is low).
- Links: Related CHANGE_FLOW.DATA_CHANGE.3; Related CHANGE_FLOW.DEPLOY.1.

### CHANGE_FLOW.RELEASE.5 Who May Release and When

- Intent: who is permitted to perform release operations and when deployment is blocked.
- Rows: L157, L164 (2)
- Positions:
  - P1 Restrict by policy who can perform release operations, while keeping release itself self-service for teams. Consensus (one source). L157; REG-082.
  - P2 Block deployments during active incidents and outside the hours when responders are available. One T3 source, not cross-checked. L164; REG-115.
  - No competing position recorded.
- Context variables: none.
- Links: Related OPERATION.INCIDENTS (L164).

## CHANGE_FLOW.DEPLOY Deployment

- Intent: how a release reaches production: automation, rollout strategy, environment parity, instance replacement.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.AVAILABILITY

### CHANGE_FLOW.DEPLOY.1 Automated Deployment Path

- Intent: how deployment is automated and which processes run as the application does.
- Rows: L159, L1198 (2)
- Positions:
  - P1 Automate deployment with the same process for every environment, production included; any authorized person can deploy any version on demand; steps idempotent and order-independent; scripts versioned. Consensus. L159; REG-077, REG-082, REG-092. Coverage check: the maintainer's L290 and L328 (at `CHANGE_FLOW.DATA_CHANGE.3`) contradict L159.
  - P2 Run one-off admin processes (migrations included) with the same code, environment and dependency isolation as the application; ship admin code with the application. Consensus. L1198; REG-1109.
- Context variables: none.
- Links: Conflicts CHANGE_FLOW.DATA_CHANGE.3 (L290, L328 versus L159); Related CHANGE_FLOW.DATA_CHANGE.1 (L1196: migrations through the same process).

### CHANGE_FLOW.DEPLOY.2 Rollout Strategy and Canary Evaluation

- Intent: how a release is exposed to production traffic by blast radius and cost, and how a canary is judged.
- Rows: L160, L161, L118, L173 (4)
- Positions:
  - P1 Blue-green: switch the router back to roll back; doubles as a disaster-recovery rehearsal; costs a second production environment and missed-transaction handling. Force: reversibility, speed of recovery. Wins for stateful, downtime-sensitive applications with budget for two environments. L160; REG-087.
  - P2 Canary: expose a small share first, observe real traffic, no separate test environment for capacity; costs several live versions and schema coordination; not to be conflated with A/B tests. Force: confidence, blast radius. Wins with high traffic and good metrics. L160; REG-088.
  - P3 One-box then waves with bake time of hours. Force: blast radius across regions. Wins for multi-region services. L160; REG-115. Google stages rollouts to growing percentages, canary even for the release itself (REG-084).
  - P4 Evaluate a canary against a concurrent control group on a few metrics tied to user impact (not before/after comparison), one canary at a time, population and duration sized to velocity and traffic. Consensus (one source). L161; REG-104.
  - P5 Compare old and new versions on identical traffic (A/B diff) and use canary analysis to catch regressions before full rollout. Majority. Moved here from ASSURANCE.AVAILABILITY; the canary evaluation of P4 is the same family. L118; REG-051, REG-067.
  - P6 Assume most outages come from changes to a live system: automate progressive rollout, fast detection and safe rollback; use playbooks, which one operator reports improve time to repair about threefold. Consensus (one T2 source). L173; REG-113.
- Context variables: none stated beyond the "wins when" conditions of P1-P3 (L160).
- Links: Related CHANGE_FLOW.ROLLBACK.1; Realizes ASSURANCE.AVAILABILITY; Related OPERATION.RUNBOOKS (L173 playbook clause).

### CHANGE_FLOW.DEPLOY.3 Environment Parity

- Intent: how alike production and the earlier environments are kept, and how much pre-production is maintained against relying on progressive rollout.
- Rows: L165, L1194 (2)
- Positions:
  - P1 Production parity in all environments, local backing services included: the same type and version of backing services, operating system and libraries; a short time from commit to deploy; authors take part in deploying; do not rely on adapters to hide differences. Argument: tests pass on a lighter database and still fail in production. Force: confidence, correctness. Wins for stateful systems where adapters hide incompatibilities, and where backing-service behaviour matters. L165, L1194; REG-077, REG-092, REG-103, REG-1109.
  - P2 Reduce pre-production; test in production with a canary and a safe rollback. Force: cost of ownership, fidelity of real traffic. Wins with high traffic, strong monitoring, fast rollback. L165; REG-088.
  - P3 Lightweight stand-ins in development for speed and low resource use (the source argues against it; its merit is inferred). Force: speed of feedback, cost. Wins when the adapter surface is narrow and production-like tests exist elsewhere in the pipeline. L165.
  - P4 Maintainer: accept divergence, document known environment differences (data volume, permissions, missing schemas, performance) and route the change to a manual environment-specific migration or conditional SQL. Force: cost of ownership. Wins when production-sized data is unaffordable to replicate. L328 (attached at `CHANGE_FLOW.DATA_CHANGE.3`; contradicts L165 and L159 per the coverage check).
  - Row-level note: parity does not extend to production credentials or access.
- Context variables: none stated beyond the "wins when" conditions above (L165, L328).
- Links: Conflicts CHANGE_FLOW.DATA_CHANGE.3 (L328 versus L165); Related TRANSVERSE.ENVIRONMENTS.

### CHANGE_FLOW.DEPLOY.4 Instance Replacement and Desired State

- Intent: whether running instances are replaced or modified, and whether deploys are pushed or reconciled from declared state.
- Rows: L166, L167 (2)
- Positions:
  - P1 Replace deployed instances rather than modify them; manage base images and infrastructure as versioned code. Force: consistency, reversibility; needs external configuration, separate data persistence, fast provisioning. Majority. L166; REG-081, REG-095, REG-111.
  - P2 Managed mutable servers with configuration tools (drift risk). Wins for stateful hosts where replacement is costly (inferred). L166; REG-111.
  - P3 Hold desired state declaratively and immutably in version control; agents pull and continuously reconcile. Argument: drift is corrected and history is auditable. Force: control, security. L167; REG-101.
  - P4 Push deploys from CI: a simple scripted deploy. Force: cost of ownership. No source read compares P3 and P4 (open; wins-when inferred). L167; REG-077, REG-092.
- Context variables: none.
- Stack pointers: L166 is tagged to infrastructure with image-based provisioning; L167 is realised with orchestrators that reconcile desired state.

## CHANGE_FLOW.ROLLBACK Rollback

- Intent: how a change is undone: decision to roll back, backward compatibility, reversible by version control.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.AVAILABILITY

### CHANGE_FLOW.ROLLBACK.1 Detecting and Deciding to Roll Back

- Intent: whether a bad release is rolled back automatically from alarms or fixed forward, decided in advance.
- Rows: L162 (1)
- Positions:
  - P1 Automate detection of bad releases and roll back from alarms (Google, Amazon). Force: reversibility, recovery time. Wins for any change that is backward compatible. L162; REG-104, REG-113, REG-115.
  - P2 Fix forward from trunk under continuous deployment. Force: simplicity, no release branch. Wins with a very fast pipeline and changes not reversible by redeploy (data migrations). L162; REG-078, REG-106. No source read states the decision rule between them; the wins-when conditions are inferred.
- Context variables: none.
- Links: Conflicts CHANGE_FLOW.ROLLBACK.3 (L288 in partial tension with L162); Related CHANGE_FLOW.DEPLOY.2.

### CHANGE_FLOW.ROLLBACK.2 Reversible by Design

- Intent: how a change is made so that going back is safe: compatible with the previous version, reversible through version control.
- Rows: L163, L1072 (2)
- Positions:
  - P1 Make each change backward compatible with the previous version (parallel change: expand, migrate, contract; schema changes separate from application releases) so rollback, mixed fleets and independent release are safe. Consensus; the maintainer's L288 agrees. L163; REG-087, REG-088, REG-105, REG-115.
  - P2 Every automated change reversible through version control; tool-level checkpoints are not a substitute. Majority. L1072; REG-1038, REG-1041.
  - No competing position recorded.
- Context variables: none.
- Links: Related CHANGE_FLOW.DATA_CHANGE.4 (the expand-migrate-contract procedure for data, L382 and L383, is held there, this node holds the generic rule); Related CHANGE_FLOW.INTEGRATION.5.

### CHANGE_FLOW.ROLLBACK.3 Undoing a Data Change

- Intent: what undoes a failed data change, decided before it ships.
- Rows: L288, L387, L390 (3)
- Positions:
  - P1 A written reverse for every migration. Held by two migration-tool vendors. Force: reversibility, downgrade after a vulnerability. Wins for regulated or packaged software with many installed versions. L387 (a); REG-244, REG-251, REG-252, REG-255.
  - P2 Backward compatibility plus roll-forward plus restore, no generated undo. Held by Fowler/Sadalage and Redgate. Force: cost of ownership (undo scripts are untested code), honesty about data loss. Wins for continuously deployed services with one production. L387 (b); REG-244, REG-251, REG-252, REG-255.
  - P3 Maintainer: forward-only with a documented undo section prepared ahead, the ticket named, no migration-opened transaction (a documented reverse change, not an automatic down step). Force: control, honesty about irreversible data changes. Wins when data changes dominate. L288, L387 (c); REG-181. The row also records automatic down migrations (one-command reversal; wins for reversible schema changes) as the common-practice alternative.
  - P4 The last reversible point is the state before the old structure is removed and before reads move irreversibly; after new-only data accumulates, going back loses it. Majority. L390; REG-087, REG-260.
- Context variables: DISTRIBUTION (L387: regulated or packaged software with many installed versions versus a continuously deployed service with one production).
- Links: Conflicts CHANGE_FLOW.ROLLBACK.1 (L288 partial tension with L162); Realizes ASSURANCE.DATA_INTEGRITY; Related CHANGE_FLOW.DATA_CHANGE.4.

## CHANGE_FLOW.DATA_CHANGE Data and Schema Change

- Intent: how schema, data and bulk changes are written, ordered, rehearsed, run and watched. Holds the procedures of the data split topic (MD-03); the guarantees stay in `ASSURANCE.DATA_INTEGRITY`.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.DATA_INTEGRITY

### CHANGE_FLOW.DATA_CHANGE.1 Form and Source of a Change

- Intent: in what form a schema or data change is written and what its source of truth is, so no change is applied by hand.
- Rows: L379, L286, L1196, L381, L289, L1197, L385, L406 (8)
- Positions:
  - P1 Every schema and data change is a migration script in version control, ordered by a unique sequence, applied by automation, never by hand-typed ad-hoc SQL. Consensus. L379; REG-244, REG-245, REG-253.
  - P2 Maintainer: schema, function and data changes ship as ordered, once-only, version-tracked migration files recorded in a history table; never apply changes manually; the stated reason is the earlier state of inconsistent environments and untracked manual changes. L286; REG-181.
  - P3 Versioned, automated migration scripts kept with the application, run by the same process in every environment as an explicit step of the release. Consensus. L1196; REG-244, REG-1109, REG-1110.
  - P4 Source of truth is the desired schema state (declarative). Force: developer cognitive load, fast iteration. Wins for fast local loops and when CI can reach the database. L381 (a); REG-253.
  - P5 Source of truth is the ordered change scripts (versioned). Force: auditability, determinism, offline CI. Wins under compliance, many instances, packaged software. L381 (b); REG-253. Hybrid (develop declaratively, generate versioned files for review and deploy) is the vendor recommendation; one vendor source, T2 position not found.
  - P6 Write DDL idempotently "as if it will be run twice", except one-time data migrations or where the operation must fail if its precondition does not hold (maintainer). Force: resilience of partially applied scripts; once-only tooling already serves that, so this is defence in depth at the cost of verbosity. L289; REG-181.
  - P7 Keep each database change as small as possible so errors are quick to spot. Consensus. L1197, L385; REG-244, REG-257.
  - P8 Keep urgent data fixes in a separate migration folder with its own tracking, apart from feature-driven schema migrations. Majority (one T2 source). L406; REG-244.
- Context variables: COMPLIANCE_AND_DISTRIBUTION (L381: P5 wins under compliance, many instances, packaged software).
- Links: Related CHANGE_FLOW.DEPLOY.1 (L1196 and L159); Related CHANGE_FLOW.DATA_CHANGE.2.
- Stack pointers: L289 (SQL form); L1196 origin stack tag was a relational database (statement generic).

### CHANGE_FLOW.DATA_CHANGE.2 Migration History and Immutability

- Intent: how the state of applied migrations is recorded and why an applied migration is not rewritten.
- Rows: L380, L287, L418 (3)
- Positions:
  - P1 Keep a per-database record of which migrations ran and do not edit an applied one; correct with a new migration. Strict, checksum-enforced immutability serves correctness and reproducibility; one tool allows editing after rolling the changeset back. The strict form wins wherever more than one environment has applied the change. Majority; the "never edit" form is inferred from REG-252 and REG-253. L380; REG-245, REG-252, REG-253.
  - P2 Maintainer: never edit an applied migration; if it failed, fix and rerun; if it succeeded but was wrong, add a new one; a recorded checksum enforces this; forced replay is rare and administrator-only. L287; REG-181.
  - P3 Track migration state in the target database itself so the pipeline can tell which instance is at which version; keep sample or reference data with the migrations so every environment is consistent. Consensus. L418; REG-244, REG-245.
- Context variables: none.
- Stack pointers: L287 is shaped to one migration tool's model.

### CHANGE_FLOW.DATA_CHANGE.3 Delivery Path and Gating of Database Change

- Intent: through which path and gate a database change reaches production, and which changes go through a person.
- Rows: L168, L290, L410, L291, L294, L411, L328, L408 (8)
- Positions:
  - P1 Treat database change as a primary delivery risk and manage it in the same pipeline as application change, not as a separate manual track. Majority/consensus. L168; REG-087, REG-097, REG-105, REG-244, REG-245.
  - P2 Fully automated: every change applies through the pipeline. Argument: small frequent changes are safer and measured better (DORA). Force: delivery speed, consistency. Wins with small, fast, compatible, reversible changes, staged rollouts and high deploy frequency. L290 (a), L410; REG-244, REG-245, REG-255.
  - P3 Maintainer: split by risk. Ordinary changes apply automatically on the integration branch to development; changes that run over about five minutes, take locks, are environment-specific, cannot run in a transaction or need monitoring are manual migrations outside the automatic path; production is applied manually by a small authorized group. Force: reversibility, control. Wins at large data volume and low downtime tolerance. L290 (b), L410 (gate long or locking changes behind a person, recording the criterion); REG-181. The public "never manual" rule bans hand-typed SQL, not a human-triggered automated run (L410).
  - P4 Maintainer delivery path: feature branch carrying the ticket key, migration, manual test on development, pull request with approval, automatic apply on development, verification on staging, a release pull request approved but not merged, manual production run by authorized people, then application deploy. Agrees in shape with common practice, extends it with the unmerged release approval. L291; REG-181.
  - P5 Configuration-like registry content goes through the same migration pipeline (one audited path; force: control). L294 (a).
  - P6 Maintainer: such content has an idempotent authoring script as source of truth, deployed by running it; a migration may mirror the change as audit trail but is not the vehicle. Force: delivery speed, avoids stale embedded copies. Wins when the content is data-like and small. L294 (b), L411 (no public counterpart found; open); REG-181, REG-244. Contradicts L168 per the coverage check.
  - P7 Maintainer: document known environment differences and route the change to a manual, environment-specific migration or conditional SQL rather than pursue identical environments. Force: cost of ownership. Wins when production-sized data is unaffordable to replicate. Counter-position, dev/prod parity: failures found early, wins when environments are cheap to make alike. L328; REG-181.
  - P8 Involve the people who manage the production database before a risky change; make pending changes visible across teams and environments. Consensus. L408; REG-245.
- Context variables: SCALE_AND_DOWNTIME_TOLERANCE (L290: P3 wins at large data volume and low tolerance for downtime); CRITICALITY (L410: gating wins at high criticality and large tables).
- Links: Conflicts CHANGE_FLOW.DEPLOY.1 (L290, L328 contradict L159); Conflicts CHANGE_FLOW.DEPLOY.3 (L328 contradicts L165); Related CHANGE_FLOW.RELEASE.4 (L290 inside the contested range of L156); Related CHANGE_FLOW.REVIEW.1 (L298).

### CHANGE_FLOW.DATA_CHANGE.4 Order and Compatibility With Running Code

- Intent: the order in which schema and application change, and how a structure changes while old and new code run against the same data.
- Rows: L382, L383, L384, L386, L292, L409, L419 (7)
- Positions:
  - P1 Deploy schema changes separately from, and before, the application version that needs them; the first schema step supports both old and new application versions. Consensus. L382; REG-087, REG-244, REG-245.
  - P2 Make a backward-incompatible change (rename, type change, split, move) as expand, migrate, contract: add the new structure beside the old, move writers and readers, backfill, then remove the old. Consensus. L383; REG-105, REG-245, REG-257, REG-260.
  - P3 Schedule and own the contract step; an unfinished contract leaves a state worse than the start, and the migrate phase carries two structures and dual-path code. Consensus (no source argues against). L384; REG-105, REG-260.
  - P4 Old and new versions run against the same data over the deploy window, so every stored-data change must be readable and writable by both across it. Consensus; the framing is inferred (REG-264 unread). L386; REG-087, REG-105.
  - P5 Maintainer: gate an application deploy on the schema state it needs: a declared minimum schema version is checked before rollout and the deploy fails if the target database history lacks it. Public sources support the order (schema first), not an explicit version gate (open). L292; REG-087, REG-181.
  - P6 Before dropping a column or table, first stop the application reading it (and any framework cache of it), then drop in a later deploy. Consensus; tool-specific, the generalisation is inferred. L419; REG-258.
  - P7 When a shared structure must change, support old and new access patterns during a transition behind a stable compatibility layer, with database access behind a clear layer in code. Contested: views or triggers as the compatibility surface plus a code-side access layer (Fowler/Sadalage; ease, cost of ownership; wins when consumers read shape); a function with a signature as the stable interface (maintainer MAINT-C45; absorbs change; no public source; wins when consumers are many and diverse); versioned interfaces apply to remote APIs (REG-105). L409; REG-105, REG-244.
- Context variables: CONSUMERS (L409: views win when consumers read shape; a function interface when consumers are many and diverse).
- Links: Realizes ASSURANCE.DATA_INTEGRITY; Related CHANGE_FLOW.ROLLBACK.2 (generic rule L163); Related ASSURANCE.CONTRACTS; Related CONSTRUCTION.HIDING (L409, see routing objections).
- Stack pointers: L419 is tagged to one web framework (generalisation neutral).

### CHANGE_FLOW.DATA_CHANGE.5 Locks and Online Schema Change

- Intent: how a schema change is made without blocking the shared database.
- Rows: L392, L393, L394, L395, L397, L304 (6)
- Positions:
  - P1 Know the lock a statement takes before running it on a shared database: most ALTER TABLE forms take the strongest lock and block all access; rewriting forms need extra disk and are not MVCC-safe. Consensus. L392; REG-246, REG-247, REG-249.
  - P2 Run migrations with a per-session lock timeout (not set globally) and retry on timeout, so a blocked DDL statement does not queue and starve the table. Majority; the starvation reason is inferred. L393; REG-246, REG-248, REG-255.
  - P3 Prefer the non-blocking form of each change: add constraints as not-yet-validated then validate separately, build indexes concurrently, add columns without volatile defaults, request metadata-only or in-place algorithms with an explicit no-lock clause. Consensus. L394; REG-247, REG-249, REG-258, REG-259.
  - P4 Run operations that cannot execute inside a transaction (concurrent index builds) in their own non-transactional step, apart from transactional changes. Consensus. L395; REG-255, REG-258.
  - P5 For large tables where in-place DDL blocks, use an online schema change tool that copies and swaps. Trigger-based tools are simpler and older but add write overhead and cannot pause; log-based (triggerless, pausable) tools serve control and low impact and win on high-write masters; native online DDL wins when the operation is metadata-only. Majority. L397; REG-245, REG-246, REG-249, REG-256.
  - P6 Do not shard schema changes (they need whole-object locks): use the platform's concurrent variant in a manual migration and shard only data changes (maintainer). Consensus. L304, L397; REG-181.
- Context variables: TABLE_SIZE_AND_WRITE_RATE (L397: tool choice follows write rate and whether the operation is metadata-only).
- Links: Related CHANGE_FLOW.DATA_CHANGE.6 (L304, L397: sharding applies to data changes only).
- Stack pointers: L392 (Postgres, MySQL), L393 (Postgres), L394 (Postgres, MySQL), L395 (Postgres), L397 (MySQL tools, Postgres equivalents), L304 (PostgreSQL).

### CHANGE_FLOW.DATA_CHANGE.6 Bulk and Backfill Design

- Intent: how a change over very large data is cut into batches that can be re-run, and where it runs.
- Rows: L299, L300, L398, L399, L401, L307, L407 (7)
- Positions:
  - P1 Maintainer: run a single statement over very large data (order of ten million to a billion rows) as a four-decision procedure in order: batching key (indexed key part, then numeric range, modulo last), work list generated from the data, fan-out by workers, observe and recover; if one statement finishes in minutes, run it as a migration. One long transaction serves simplicity and costs locks, bloat and an hours-long open transaction; sharding serves control; the size gate decides. L299; REG-181.
  - P2 Bounded batches with throttling pauses, in their own step, never inside a long DDL transaction. Consensus. L398; REG-255, REG-257, REG-258.
  - P3 Maintainer: every batch re-runnable in isolation; prefer a self-limiting predicate (the data is its own ledger) to external bookkeeping; non-idempotent updates made absolute; one logical unit in one statement; no automatic retries with non-idempotent batches. Consensus. L300; REG-181.
  - P4 Make each backfill batch re-runnable with the same result: upsert not insert, partition by a fixed key, never read "latest" data inside the job. Majority; transfer from scheduled tasks to data migrations is inferred. L399; REG-254.
  - P5 Decide where a backfill runs, and record why: inside a migration step with a time budget (simplicity, one delivery path; wins for minutes of work), as an application background job triggered by a migration (production safety; wins for long work), or offline from a snapshot (zero load on production; wins for very large multi-table moves with analytic tooling). Contested; each held by a different T3 source. L401; REG-255, REG-257, REG-258.
  - P6 Maintainer: compose standard command-line tools (a parallel runner, a terminal multiplexer, the database client) rather than a framework; verify each part in isolation, then compose at one worker on the lower environment. A framework serves repeatability and costs ownership; wins when the job recurs. L307; REG-181.
  - P7 Keep data migrations apart from schema migrations in transaction and timing: schema steps stay fast, data steps are batched. Majority. L407; REG-255, REG-258.
- Context variables: DATA_VOLUME (L299: the size gate between a plain migration and the four-decision procedure; L401: duration of the work picks the place it runs).
- Links: Related CHANGE_FLOW.DATA_CHANGE.8; Related CHANGE_FLOW.DATA_CHANGE.5 (L304).
- Stack pointers: L299 (PostgreSQL client and GNU parallel named in the doctrine), L398 (examples from one web framework and Postgres), L399 (source is a pipeline scheduler), L307.

### CHANGE_FLOW.DATA_CHANGE.7 Rehearsal and Time Budget

- Intent: on what data and against what budget a data change is rehearsed before production.
- Rows: L293, L402, L403, L404, L405 (5)
- Positions:
  - P1 Rehearse on production-sized or production-shaped data (to measure time, locks, plan). Held by GitLab, Postgres.ai, Neon (vendor sources are interested parties). Force: confidence, realistic timing. Wins for large tables and where plans or lock duration depend on volume; cost is cloning and personal-data risk. L403 (a); REG-244, REG-255, REG-261, REG-262.
  - P2 Developer-owned databases with versioned sample data (Fowler/Sadalage). Force: isolation, speed, no exposure. Wins for small data and early feedback. L403 (b); REG-244.
  - P3 Rehearsal inside a rolled-back transaction on shared real data (maintainer, MAINT-C01): no public source. Pointer from L403; the row itself is routed elsewhere.
  - P4 Maintainer: on every change request a workflow restores a dump of development data and applies every migration, manual ones included; a migration that cannot work on the partial dump carries a skip marker with its reason and still runs on the real environments. Agrees with migration CI on a representative dataset. L293; REG-181.
  - P5 Measure migration duration and lock behaviour on a rehearsal copy before production and keep the measure with the change. Majority. L405; REG-255, REG-256, REG-261.
  - P6 Give migrations a time budget by class so the long ones are identified before deploy (one team: regular up to 3 minutes, post-deployment up to 10, queries under 1 second; the maintainer uses about 5 minutes). Majority (one T3 source). L402; REG-255.
  - P7 When production data is copied for tests, mask personal data before it leaves production and block side effects (mail, analytics) in the copy. Majority (single vendor source). L404; REG-262.
- Context variables: DATA_VOLUME (L403: P1 wins for large tables, P2 for small data).
- Links: Related TRANSVERSE.PRIVACY (L404: masking here, retention there); Related ASSURANCE.BEHAVIOUR (L293 boundary: test data management).

### CHANGE_FLOW.DATA_CHANGE.8 Running and Watching a Production Data Job

- Intent: how a production data job is started, ramped, watched, stopped and declared done.
- Rows: L301, L302, L303, L305, L306, L400, L412, L413 (8)
- Positions:
  - P1 Maintainer: "done" for a bulk change is a written convergence query that returns zero remaining work, not the job process returning; a non-zero result means skipped or silently failed batches, and re-runs must strictly decrease it. Extends common practice. L301; REG-181. L413 records that no public counterpart was found for this practice and for the ramp ladder (open; nearest REG-257 shadow comparison, REG-256 controls, REG-254 idempotence).
  - P2 Maintainer: ramp concurrency, never guess it: one batch by hand with its plan inspected, then one worker, then a modest default, higher only with a reason and a metric; on the first production run halt on the first failure; keep a ledger of batches with exit codes and separate error and progress streams; detach the job from the operator's session; bound workers by connections, headroom and replica lag; compute total time from batch time before blaming the worker count. Agrees with progressive rollout, extends with the ledger and halt rules. L302; REG-181.
  - P3 Maintainer: do not start a production bulk job until a checklist holds: ticket exists with its key in the statement text; full development run at one worker, then a few; batch predicate index-backed, verified by a plan; every batch idempotent or the predicate convergent; convergence query written; job detached with a ledger; change is a manual migration; senior review if it holds locks or runs long; a stop plan names what to cancel and whether partial completion is acceptable. L303; REG-181.
  - P4 Make a long data job pausable and pace it on the target system's health, replica lag first, with mid-run adjustment of batch size and lag limit. Majority (single T3 source plus a sleep between batches in REG-258). L400; REG-256, REG-258.
  - P5 Maintainer: watch the target system, not only the job's shell: lock waits, per-batch runtime climbing (a sign the predicate is not index-backed), dead-tuple growth, replica lag as the governing signal for concurrency; escalate (reduce workers, stop) on those signals. Agrees with common practice. L305; REG-181.
  - P6 Maintainer: put the change's ticket key in a comment inside long-running statements so it appears in activity views and logs and identifies the job during an incident. Agrees with query tagging and trace correlation. L306; REG-181. L412 records that no public counterpart was found (open).
- Context variables: none stated by a row.
- Links: Related OPERATION.TELEMETRY (L305); Related OPERATION.INCIDENTS (L306); Related CHANGE_FLOW.REVIEW.1 (L303 senior review); Related CHANGE_FLOW.DATA_CHANGE.6.
- Stack pointers: L305 names target-system signals of one relational database (dead tuples) alongside neutral ones; L400 source is a MySQL tool.

## CHANGE_FLOW.MEASURE Measuring Delivery

- Intent: how delivery is measured and which outcomes judge it.
- Rows: none (roll-up)
- Links: Realizes ASSURANCE.RULES; Related OPERATION.FEEDBACK

### CHANGE_FLOW.MEASURE.1 Outcomes That Judge Delivery

- Intent: which outcome measures judge the change flow, and how speed and stability relate.
- Rows: L169, L170, L1058 (3)
- Positions:
  - P1 Measure with the five DORA metrics (change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate); use them to guide improvement, not to rank people (the "not rank people" part is inferred). Consensus. L169; REG-093.
  - P2 Treat speed and stability as correlated, not traded off, but only with supporting practices; raising deployment frequency alone yields failures and burnout. Majority. The conventional view (speed versus stability) is what REG-093 argues against; no source read defends it. L170; REG-093, REG-097.
  - P3 Judge change flow by delivery outcomes (stability, lead time, failures), not by the volume of code or pull requests produced. Contested on the net effect of automation: (a) it raises throughput and satisfaction, instability a fixable side effect (REG-1041); (b) gains vanish at organisation level (REG-1047) or are negative for experienced developers in mature code (REG-1043, 16 developers). Force: delivery speed versus stability. (a) wins in teams with the foundation practices, (b) elsewhere; sample and vendor caveats apply. L1058; REG-1041, REG-1042, REG-1043, REG-1047.
- Context variables: FOUNDATION_PRACTICES (L1058: (a) wins in teams with version control, small batches, testing, platform, clear policy; (b) elsewhere).
- Links: Related OPERATION.RELIABILITY (L169 and L208: recovery time, change fail rate); Related CHANGE_FLOW.RELEASE.1.

### CHANGE_FLOW.MEASURE.2 Independent Baselines and Preconditions

- Intent: how a measured gain is trusted and what must hold before automation is expected to help.
- Rows: L1059, L1060 (2)
- Positions:
  - P1 Do not rely on self-reported speed or security gains from automation; measure them against an independent baseline. Majority; grounded for findings from small samples, the principle is inferred. L1059; REG-1043, REG-1044, REG-1050.
  - P2 Treat the delivery system's fundamentals (version control, small batches, testing, platform, clear policy) as preconditions: automation magnifies existing strengths and weaknesses. Majority. L1060; REG-1041, REG-1042.
  - No competing position recorded.
- Context variables: none.
