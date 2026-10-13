# Branch TRANSVERSE: tree and node records

Status: refinement of the L1 branch TRANSVERSE below its six L2 nodes (`../../tree_l2.md`), cut on `../../../target_hierarchy.md` and `../../../maintainer_decisions.md` (MD-01 to MD-07). It lists the competing positions per node and states no verdict, no ranking, no merge of ledger rows (MD-01: the judging step decides the best practice per node). Rows are the 74 routed to this branch in `../../routing.md`; `check_branch.py` proves coverage.

## How to read

- A node record gives uid, name, one-line intent, attached row ids, positions, context variables, links, stack pointers.
- Rows are attached at the L3 node; an L2 node with children holds `Rows: -` (roll-up of its children).
- `P1, P2...` are the competing practices recorded for the node. Each carries its strongest argument, the force it serves, the condition under which it would be the best, and row and source ids (REG-nnn; a source `REG-181` is the maintainer's codified practice, MAINT-S01, not citable). The order of positions carries no meaning.
- "No competing position recorded" means the ledger holds one practice for the point and no alternative was read.
- Context variables appear only where a row itself says the best practice moves with them (MD-02), the row id quoted.
- Two rows that state the same thing and were kept apart by the ledger (for example L158 and L1192) sit together on one node; they are not merged here.
- Index nodes (MD-03): `TRANSVERSE.DOCS` holds authoring and organisation practice, `TRANSVERSE.SECURITY` holds programme practice; the mechanisms that guarantee the property are in `ASSURANCE.DOCS_SYNC` and `ASSURANCE.SECURITY`, linked, not restated.

## Branch tree

- `TRANSVERSE` Transverse
  - `TRANSVERSE.DOCS` Documentation Practice
    - `TRANSVERSE.DOCS.1` Documentation Budget
    - `TRANSVERSE.DOCS.2` Organisation and Structure
    - `TRANSVERSE.DOCS.3` Layered Writing and Audience Split
    - `TRANSVERSE.DOCS.4` Release Changelog
    - `TRANSVERSE.DOCS.5` Basis and Evolution of Guidelines
  - `TRANSVERSE.SECURITY` Security Practice
    - `TRANSVERSE.SECURITY.1` Anchor Framework
    - `TRANSVERSE.SECURITY.2` Maturity Targets and Cycle
    - `TRANSVERSE.SECURITY.3` Design-Time Risk Modelling
    - `TRANSVERSE.SECURITY.4` Responsibility and Training
    - `TRANSVERSE.SECURITY.5` Vulnerability Response Loop
    - `TRANSVERSE.SECURITY.6` Disclosure Policy and Bounty
  - `TRANSVERSE.SECURITY_MONITORING` Security Monitoring and Audit Trail
    - `TRANSVERSE.SECURITY_MONITORING.1` Events Logged
    - `TRANSVERSE.SECURITY_MONITORING.2` Entry Content, Time and Format
    - `TRANSVERSE.SECURITY_MONITORING.3` Log Protection and Sanitising
    - `TRANSVERSE.SECURITY_MONITORING.4` Detection and Escalation
    - `TRANSVERSE.SECURITY_MONITORING.5` Business Audit Trail
  - `TRANSVERSE.PRIVACY` Privacy and Retention
    - `TRANSVERSE.PRIVACY.1` Minimisation, Classification and Design-In
    - `TRANSVERSE.PRIVACY.2` Retention Periods
    - `TRANSVERSE.PRIVACY.3` Erasure and Deletion Mechanism
    - `TRANSVERSE.PRIVACY.4` Privacy Risk, Impact Assessment and Breach
  - `TRANSVERSE.CONFIG` Configuration and Secrets
    - `TRANSVERSE.CONFIG.1` Separation of Configuration from Code and Secrets
    - `TRANSVERSE.CONFIG.2` Delivery Channel to the Running Software
    - `TRANSVERSE.CONFIG.3` Shape of Per-Environment Configuration
    - `TRANSVERSE.CONFIG.4` Central Secret Custody and Lifecycle
    - `TRANSVERSE.CONFIG.5` Credential Lifetime and Pipeline Identity
    - `TRANSVERSE.CONFIG.6` Response to a Leaked Secret
  - `TRANSVERSE.ENVIRONMENTS` Development Environments
    - `TRANSVERSE.ENVIRONMENTS.1` Separation and Isolation
    - `TRANSVERSE.ENVIRONMENTS.2` Definition Mechanism
    - `TRANSVERSE.ENVIRONMENTS.3` Toolchain Control and Hardening

## Node records

### `TRANSVERSE` Transverse

- Intent: practices that cut across every branch: documentation, security, privacy, configuration and secrets, development environments.
- Rows: - (roll-up of its L2 nodes).
- Links: Realizes `ASSURANCE.DOCS_SYNC`, `ASSURANCE.SECURITY` (through the nodes below).

### `TRANSVERSE.DOCS` Documentation Practice

- Intent: how documentation is organised, written and budgeted, so that it is read and kept up; the mechanisms that keep it true to the system are held by `ASSURANCE.DOCS_SYNC`.
- Rows: - (roll-up).
- Index: the content of the mechanisms (same-change delivery, gates, owners, executable examples) is stated once in `ASSURANCE.DOCS_SYNC`; this node holds only authoring and organisation practice (MD-03).
- Links: Realizes `ASSURANCE.DOCS_SYNC`.

### `TRANSVERSE.DOCS.1` Documentation Budget

- Intent: how much documentation to produce and maintain, as a deliberate choice, who writes it, and the budget for its upkeep.
- Rows: L231, L236, L229
- Positions:
  - P1 Invest in documentation quality as a delivery capability and budget for upkeep. Strongest argument: the research programme reads documentation quality as a driver of delivery capability (correlational survey data, causality inferred). Force: delivery capability, cost of ownership. Condition: none recorded. L231; REG-152.
  - P2 Minimal, conversation first. Strongest argument: least text to rot. Forces: cost of ownership, delivery speed. Best when: small co-located teams, short-lived systems. L236; REG-150, REG-155, REG-164.
  - P3 Living documentation generated or extracted from code and tests. Strongest argument: no manual sync. Forces: cost of ownership, correctness. Best when: domain knowledge is in the code. L236; REG-150, REG-155, REG-164.
  - P4 Full docs-as-code with owners and gates. Strongest argument: the reading cost is paid by many and documents outlive people. Forces: confidence, cognitive load for newcomers. Best when: many consumers, long life, turnover. L236; REG-150, REG-155, REG-164.
  - P5 Engineers write the docs for what they build; technical writers focus on documents that cross API boundaries and on guidelines and champions. Strongest argument: engineers see documentation as separate from programming and the tooling is poor, so writer effort goes where engineers cannot. Condition: none recorded. Decision, majority. L229; REG-150, REG-152. Moved here from `ASSURANCE.DOCS_SYNC`, which keeps who reviews (L228).
- Context variables: scope and life of the system (many consumers, long life, turnover against small co-located team, short-lived system), because L236 states "wins for small co-located teams, short-lived systems" for P2 and "wins with many consumers, long life, turnover" for P4 (the context mapping is marked inferred by the ledger).
- Links: see `ASSURANCE.DOCS_SYNC` (P4 relies on the owners and gates held there).

### `TRANSVERSE.DOCS.2` Organisation and Structure

- Intent: how documents are cut and arranged so that they are small enough to be updated and found by the reader who needs them.
- Rows: L233, L234, L321
- Positions:
  - P1 Small, modular documents. Strongest argument: small documents have a chance of being updated, large specifications do not. Force: keeping documents current. L233; REG-150, REG-154.
  - P2 Organise by reader need (tutorial, how-to, reference, explanation) and improve in small increments published immediately, never one big restructuring. Strongest argument: structure follows reader need, and the set is "always complete, never finished". Force not stated by the row. The structure comes from one framework; other taxonomies not read. L234; REG-157.
  - P3 Router set (maintainer's practice): an index by role and situation, modules under a size cap with line-number tables of contents, cross-references kept, indexes updated with every change, each guideline linked to the formal model node it derives from. Strongest argument and force: not stated by the row (single maintainer source). Agrees with common practice per the ledger; the ledger notes that line counts and tables of contents rot (measured, in the maintainer's disagreements record). L321 (MAINT, source MAINT-S01, not citable); REG-181.
  - Competing alternative recorded: none.
- Context variables: none stated by a row.
- Links: see `ASSURANCE.DOCS_SYNC` (one canonical document per topic, L218, is held there).

### `TRANSVERSE.DOCS.3` Layered Writing and Audience Split

- Intent: how a document, including the explanation inside code, is written for readers at different depth and background.
- Rows: L322, L318
- Positions:
  - P1 Layered detail (one sentence, one paragraph, then full what, why and how), diagrams at three zoom levels (macro, flow, detailed), audience split (a non-engineer understands the why, an engineer the how; technical vocabulary stays in the internal "engine room"). Strongest argument and force: not stated by the row (single maintainer source). Agrees with common practice per the ledger. L322 (MAINT, source MAINT-S01, not citable); REG-181.
  - P2 Keep one durable explanation per unit: a mandatory structured header comment (summary, parameters, returns, notes, change log, examples with expected output) is the only multi-line comment; inline comments carry only why, invariant or gotcha, never what the next line does, at most about three consecutive lines; complex logic gets compact step banners whose outline is mirrored in the header. Strongest argument: cognitive load and durability. Best when: the unit is called by many consumers and lives apart from its history, that is, readers cannot see the repository history. L318 (MAINT, source MAINT-S01, not citable); REG-181. Maintainer decision (single source); public practice read as contested.
  - P3 Self-documenting code with history in version control. Strongest argument: comments rot. Force: cost of ownership. L318 (alternative a; MAINT row, no source ids of its own). The ledger notes the mandatory header and dated change log partly contradict common practice and duplicate version control, with partial tension with L218 and L133.
  - No competing position recorded beyond P3.
- Context variables: none.
- Links: see `ASSURANCE.DOCS_SYNC` (L218, one canonical document per topic, and L216, dating, are held there).

### `TRANSVERSE.DOCS.4` Release Changelog

- Intent: how the record of what changed in each release is kept for its readers.
- Rows: L235
- Positions:
  - P1 Human-written changelog per release, grouped by change type, with an "Unreleased" section filled as changes land. Strongest argument: as stated by the row, a human-written record grouped by change type. Condition: none recorded. L235; REG-161, REG-162.
  - P2 Changelog generated from commit conventions. Recorded as the alternative, not read in the sources; the ledger marks the debate as open. L235 (alternative named, no source ids).
- Context variables: none.
- Links: see `CHANGE_FLOW.RELEASE` (a changelog belongs to a release; the node exists in `tree_l2.md`).

### `TRANSVERSE.DOCS.5` Basis and Evolution of Guidelines

- Intent: from what guidelines are derived and how they are updated, so that a new rule states which earlier rule it overrides.
- Rows: L323
- Positions:
  - P1 Induced from analysis of real production code (including observed queries), updated as practice evolves, with deliberate-evolution notes stating which earlier rule a new rule overrides and for which objects. Strongest argument: reflects what works and gets adopted. Force: cost of ownership. Best when: a mature codebase. L323 (MAINT, source MAINT-S01, not citable); REG-181.
  - P2 Deduced from principles first (the maintainer's philosophy asks structure before implementation). Force: correctness, consistency. Condition: not recorded. L323; REG-181. The ledger records an internal tension and no public claim to support or contradict the row.
- Context variables: maturity of the codebase (L323: "wins in a mature codebase").
- Links: see `EVOLUTION.DECISIONS` (records of an overriding rule).

### `TRANSVERSE.SECURITY` Security Practice

- Intent: how a security programme is anchored, risk modelled, responsibility owned and vulnerabilities handled; the verification and enforcement mechanisms are held by `ASSURANCE.SECURITY`.
- Rows: - (roll-up).
- Index: verification, scanning, tests and enforced limits on automation are stated once in `ASSURANCE.SECURITY`; this node keeps programme practice (MD-03).
- Links: Realizes `ASSURANCE.SECURITY`.

### `TRANSVERSE.SECURITY.1` Anchor Framework

- Intent: which published framework anchors the secure-development practice, chosen by the question the team needs answered.
- Rows: L240, L250, L1120, L1121
- Positions:
  - P1 Outcome list of a secure-development framework (SSDF, SAMM) used as outcomes to cover across the lifecycle, not a prescription of tools. Strongest argument: the framework is a list of outcomes, not a prescription of tools. Force: coverage across the lifecycle. L240; REG-004, REG-171. The ledger notes L240 and L1120 state the same normative thing in part.
  - P2 Requirements standard (ASVS): testable, level-graded requirements usable in procurement; one catalogue serves as the developers' requirement list and the basis for testing. Forces: correctness, control. Best when: a single application or a supplier contract. L1120, L250; REG-1078, REG-180. Stack: level definitions not read (L250 open); levels as roughly 20%, 50% (about 70% cumulative), 30% of requirements (L1121; REG-1078).
  - P3 Prescriptive maturity model (SAMM): measurable, actionable, versatile, with a roadmap. Force: delivery of a programme at organisation scale. Best when: many teams. L1120; REG-1084.
  - P4 Descriptive benchmark (BSIMM): documents actual practices of 100+ organisations. Force: comparison. Best when: a security group justifying investment; the row says it loses as a decision rule, since common practice is not best practice. L1120; REG-1085.
- Context variables: scope of the programme (a single application or supplier contract against many teams), L1120 ("wins for a single application or a supplier contract", "wins with many teams").
- Links: see `ASSURANCE.SECURITY` (L1119 there sets depth of verification per application).
- Stack pointers: L250 (web applications, ASVS); L1121 (web application and API).

### `TRANSVERSE.SECURITY.2` Maturity Targets and Cycle

- Intent: how a maturity model is used and how far its scores can be trusted.
- Rows: L1123, L1124, L1125, L1162
- Positions:
  - P1 Set a target maturity per practice from context; a higher level in one practice does not require it in the others. L1123; REG-1084. No competing position recorded.
  - P2 Use a maturity model as a cycle: assess current practice, set targets, build a roadmap, take prescriptive activity guidance. L1125; REG-1084, REG-171. No competing position recorded.
  - P3 Treat descriptive benchmark data as evidence of what peers do, not as the verdict on what to do. Marked inferred by the ledger. L1124; REG-1085.
  - Open point: no source read shows higher maturity scores or higher ASVS levels reduce incidents; the models measure programme activity and requirements coverage. The ledger marks this open (five sources checked; benchmark report data not read). L1162; REG-1078, REG-1084, REG-1085, REG-171.
- Context variables: none stated by a row.
- Links: see `TRANSVERSE.SECURITY.1` (the chosen framework).

### `TRANSVERSE.SECURITY.3` Design-Time Risk Modelling

- Intent: how security risk is modelled during design and how the findings are tracked.
- Rows: L241, L242
- Positions:
  - P1 Continuous, lightweight modelling per iteration. Strongest argument: a one-off model is stale at the next change (Threat Modeling Manifesto). Forces: correctness over time, speed of feedback. Best when: fast-changing products with an engaged team. L241; REG-004, REG-165.
  - P2 Deeper, risk-triggered assessment for high-risk areas only (SSDF). Strongest argument: effort goes where the cost of error is. Force: cost of ownership. Best when: criticality or regulation. L241; REG-004, REG-165. The ledger says the two are compatible; the choice is the trigger and cadence.
  - P3 Each threat model answers four questions (what are we working on, what can go wrong, what are we going to do about it, did we do a good enough job); risks and mitigations are tracked in the team's workflow. L242; REG-004, REG-165. No competing position recorded.
- Context variables: criticality and regulation, L241 ("wins under criticality or regulation").
- Links: see `ASSURANCE.SECURITY` (L243 there reviews the design against the risk model).

### `TRANSVERSE.SECURITY.4` Responsibility and Training

- Intent: who owns security outcomes and how the owners are prepared.
- Rows: L249
- Positions:
  - P1 Explicit responsibility owned from the top: roles defined, role-based training, management committing, the producer owning customer security outcomes. L249; REG-004, REG-172. No competing position recorded.
- Context variables: none.
- Links: none.

### `TRANSVERSE.SECURITY.5` Vulnerability Response Loop

- Intent: how a vulnerability, once reported or found, is confirmed, assessed, fixed and learned from.
- Rows: L253
- Positions:
  - P1 Response loop: identify and confirm (monitoring databases and reports, a disclosure policy), assess, prioritize, remediate, then analyze root causes and fix the process as well as the instance. Boundary noted by the row: incident handling and feedback from production sit in operation. L253; REG-004. No competing position recorded.
- Context variables: none.
- Links: see `TRANSVERSE.SECURITY.6` (the intake of reports), `OPERATION.INCIDENTS`.

### `TRANSVERSE.SECURITY.6` Disclosure Policy and Bounty

- Intent: how outsiders report a vulnerability to the team and whether the team pays for reports.
- Rows: L1141, L1142
- Positions:
  - P1 Publish how to report, a private channel, an answer within a stated time (OpenSSF: 14 days), a fix of known medium-or-higher vulnerabilities within a stated time (OpenSSF: 60 days), and the contact in a standard place (security.txt with Contact and Expires). The day counts are one project's criteria. L1141; REG-1094, REG-1097, REG-1098.
  - P2 Disclosure policy only (OMB). Forces: cost of ownership, control. Best when: triage capacity is small. L1142; REG-1094, REG-1097.
  - P3 Policy plus paid bounty, after weighing cost, competence and maturity (OMB allows it). Force: speed of finding. Best when: mature triage and wide attack surface. L1142; REG-1094, REG-1097. Commercial position open: only vendor documentation surfaced, not read; no source compares yield.
  - P4 Periodic penetration test alone. Forces: control, scope. Best when: the system cannot be exposed to outside researchers. L1142 (position named, no source ids of its own).
- Context variables: triage capacity and attack surface, L1142 ("wins when triage capacity is small", "wins with mature triage and wide attack surface").
- Links: none.

### `TRANSVERSE.SECURITY_MONITORING` Security Monitoring and Audit Trail

- Intent: what security-relevant events are logged, protected, detected and kept as an audit trail.
- Rows: - (roll-up).
- Links: Realizes `ASSURANCE.SECURITY` (the split-topics table of `tree_l2.md` assigns logging, detection and retention to this node); see `OPERATION.TELEMETRY`.

### `TRANSVERSE.SECURITY_MONITORING.1` Events Logged

- Intent: which security-relevant events are recorded, including actions by automation.
- Rows: L1143, L1073
- Positions:
  - P1 Log security-relevant events: authentication successes and failures, authorization failures, input and output validation failures, session management failures, administrative actions, sensitive data access, use of higher-risk functionality, application errors, security control failures and bypass attempts; data-change events optional, per need. Note: all such requirements are level 2 or 3 in ASVS 5.0, so an application held to level 1 is not required to log security events. L1143; REG-1079, REG-1089, REG-1090.
  - P2 Log every automated action (commands, tool calls, plan changes) in a reviewable audit trail. Boundary: operation. L1073; REG-1034, REG-1036, REG-1037.
  - No competing position recorded.
- Context variables: none stated by a row (the ASVS level note on L1143 is an assurance-level fact, not a context choice).
- Links: see `ASSURANCE.SECURITY` (the verification level there decides whether logging is required).

### `TRANSVERSE.SECURITY_MONITORING.2` Entry Content, Time and Format

- Intent: what each log entry contains and how entries from many systems are ordered and read together.
- Rows: L1144, L1245, L1248
- Positions:
  - P1 Record who, what, when and where on every entry (timestamp, application and address, source address and authenticated identity, event type, severity, affected object, result and reason); inventory of what is logged per layer; synchronised time (UTC); common format; documented destinations only. L1144; REG-1079, REG-1089.
  - P2 One consistent event vocabulary (category prefix plus action) and ISO 8601 timestamps with UTC offset so monitoring can key on the terms. L1245; REG-1136.
  - P3 Synchronize time across servers so events can be sequenced; often impossible for remote client applications. L1248; REG-1089.
  - No competing position recorded.
- Context variables: none.
- Links: none.

### `TRANSVERSE.SECURITY_MONITORING.3` Log Protection and Sanitising

- Intent: how logs are kept trustworthy and free of what must not be in them.
- Rows: L1145, L1151, L1247, L1254
- Positions:
  - P1 Protect logs at rest and in transit: encode against log injection, prevent modification (copy to read-only media early), restrict and record access, verify origin of logs from outside, ship to a logically separate system for analysis, detection and alerting. L1145; REG-1079, REG-1089, REG-1090, REG-1093.
  - P2 Keep logs apart from application data (separate partition or a write-only database account with very restrictive permissions; central collector, standard format, secure transport). L1247; REG-1089.
  - P3 Never log passwords, tokens, keys, connection strings, payment data or session identifiers (hash the identifier if tracking is needed), nor personal data without need or legal justification; pseudonymise where identity is not required; sanitize logged input against CR, LF and delimiter injection; apply logging by the data's protection level. L1151; REG-1079, REG-1089, REG-1136.
  - P4 Treat events from clients as untrusted input: validate and sanitize before writing, encode for the output format. Boundary: security. L1254; REG-1089, REG-1090.
  - No competing position recorded.
- Context variables: none.
- Links: see `TRANSVERSE.PRIVACY.1` (the privacy rule on personal data is L1153 there).

### `TRANSVERSE.SECURITY_MONITORING.4` Detection and Escalation

- Intent: how attacks are detected and escalated, and how long detection may take.
- Rows: L1146, L1147, L1149
- Positions:
  - P1 Logging without alerting and response is a failure: detect and escalate active attacks in near real time and detect when logging stops. Gap noted: the leading verification standard does not verify alerting. L1146; REG-1079, REG-1089, REG-1090.
  - P2 Time to detect (dwell time) is the cost to manage; delays of months raise damage (one source: about 200 days on average; dated, open as a current value). L1147; REG-1082, REG-1093.
  - P3 Where the detection platform may change, express detection rules in a tool-neutral format so they survive a platform exit. Marked inferred (one T3 source; the exit-risk argument is the researcher's). Force: exit risk. Best when: the platform may change. L1149; REG-1100.
- Context variables: none stated beyond P3's condition.
- Links: see `OPERATION.ALERTING` (escalation); see `OWNERSHIP.CONTAINMENT` (P3, exit from a tool).
- Stack pointers: L1149 (detection tooling).

### `TRANSVERSE.SECURITY_MONITORING.5` Business Audit Trail

- Intent: how the history of changes is kept for accountability and queries, apart from the security event log.
- Rows: L1252, L1246, L1249, L1250, L1251
- Positions:
  - P1 Keep two purposes apart in the design: the security event log (who tried what, for detection) and the business audit trail (what changed, for accountability and queries); they differ in storage, integrity needs and retention. Marked inferred; no source states the split. L1252; REG-1089, REG-1090, REG-1142.
  - P2 High-value transactions get an audit trail with integrity controls against tampering or deletion (such as append-only tables) plus tamper detection. L1246; REG-1089, REG-1090.
  - P3 Record both the actual date (event) and the record date (written). L1249; REG-1142.
  - P4a Audit log: simplest, non-intrusive, hard to read, poor for frequent integrated temporal queries. P4b Temporal properties or objects: cost in model complexity, integrate with queries. Choose by how tightly history is queried. L1250; REG-1142.
  - P5 Write the audit record in the same transaction as the audited change, so both commit or roll back together (database trigger variant: an AFTER trigger sees the final row value, a BEFORE trigger may not). Restated stack-neutral from a PostgreSQL origin. L1251; REG-1090, REG-1140.
- Context variables: frequency of integrated temporal queries over history, L1250 ("choose the history mechanism by how tightly history is queried").
- Links: see `TRANSVERSE.PRIVACY.3` (deletion of history follows the reason the data is kept, L1258); see `ASSURANCE.DATA_INTEGRITY`.
- Stack pointers: L1251 (restated from origin stack: postgres).

### `TRANSVERSE.PRIVACY` Privacy and Retention

- Intent: how personal data is minimised, classified, retained and erased.
- Rows: - (roll-up).
- Links: Realizes `ASSURANCE.SECURITY`; see `OPERATION.RECOVERY` (backup retention).

### `TRANSVERSE.PRIVACY.1` Minimisation, Classification and Design-In

- Intent: how little personal data is collected and how what is held is classified and protected from the start.
- Rows: L1153, L1152, L1155, L1156, L1171
- Positions:
  - P1 Collect and process only the personal data necessary for each stated purpose, by default (data minimisation). L1153 (legal basis EU); REG-1095.
  - P2 Where logs must support investigation but not identification, pseudonymise so investigators follow one user's timeline without learning who the user is. L1152; REG-1093.
  - P3 Identify and classify sensitive data into protection levels (including encoded forms) and document safeguards per level: encryption, integrity, retention, logging, database security, privacy. L1155; REG-1080.
  - P4 Build data protection into design and defaults, with measures scaled to the state of the art, cost, and the nature, scope, context and risk of processing. L1156; REG-1080, REG-1095.
  - P5 Never place personal or sensitive data in propagated trace context, nor seed trace identifiers from user-identifiable data. Consensus. L1171; REG-122. Moved here from `OPERATION.TELEMETRY`, which keeps how trace context is propagated (L1164).
  - No competing position recorded.
- Context variables: none.
- Links: none.
- Stack pointers: L1153 (legal basis EU, practice stated neutral); L1171 (origin stack HTTP, restated neutral by the ledger).

### `TRANSVERSE.PRIVACY.2` Retention Periods

- Intent: how long data, logs included, is kept and how that period is decided and recorded.
- Rows: L1150, L1154
- Positions:
  - P1 Retain for the legal minimum and delete (OWASP, GDPR). Forces: privacy, cost. Best when: logs hold personal data. L1150; REG-1089, REG-1093, REG-1095.
  - P2 Retain long, tier by age (Google). Force: investigation power. Best when: dwell time is long and logs can be pseudonymised. L1150; REG-1089, REG-1093, REG-1095. Neither source gives a number; both agree the period is a recorded decision, no shorter and no longer than the legal, regulatory, contractual or purpose limit.
  - P3 Define retention per purpose and delete on schedule (storage limitation); automate deletion by retention class. L1154; REG-1080, REG-1095. No competing position recorded.
- Context variables: whether logs hold personal data and how long dwell time is, L1150 ("wins when logs hold personal data", "wins when dwell time is long").
- Links: see `TRANSVERSE.PRIVACY.1` (classification fixes the retention class).

### `TRANSVERSE.PRIVACY.3` Erasure and Deletion Mechanism

- Intent: how data is actually deleted or put beyond use, in live systems, copies and backups.
- Rows: L1157, L1258, L1257, L1114
- Positions:
  - P1 Decide per entity from the reason the data is kept: no need (hard delete), legal or audit retention (archive table or append-only audit), user-visible recovery (archive or soft delete with an owner for the predicate), queryable past values (temporal model), bulk expiry (partition drop); record the choice. Marked inferred (synthesis of four sources). L1258; REG-1137, REG-1138, REG-1142, REG-1145.
  - P2 For time-bounded data partition by time and drop or detach old partitions instead of bulk DELETE (faster, no vacuum overhead; detach first to back up or aggregate; PostgreSQL: DROP TABLE takes an ACCESS EXCLUSIVE lock on the parent). L1257; REG-1137. Restated stack-neutral.
  - P3 Decide how an erasure request reaches copies: caches, logs, derived stores, third parties and backups. The ledger marks this open: backups and logs are not settled by any source read; agreement contested. L1157; REG-1095.
  - P4 Give backups a retention schedule; when personal data must be erased, erase from live systems and put backup copies beyond use until overwritten on schedule, and tell the data subject what happens to the backup (one UK regulator). Tension recorded: immutable retention of backups (open: how a locked backup is put beyond use is not addressed in the sources read). L1114; REG-1069.
- Context variables: none stated beyond L1258's reason-of-retention cases.
- Links: see `TRANSVERSE.PRIVACY.2`; see `OPERATION.RECOVERY` (backup design), `CHANGE_FLOW.DATA_CHANGE` (bulk change procedure).
- Stack pointers: L1257 (restated from origin stack: postgres); L1114 (UK regulator).

### `TRANSVERSE.PRIVACY.4` Privacy Risk, Impact Assessment and Breach

- Intent: how privacy is managed as a risk, assessed before high-risk processing and answered when a breach occurs.
- Rows: L1161, L1158, L1159
- Positions:
  - P1 Manage privacy as a risk through a framework (NIST Privacy Framework, voluntary, enterprise risk management) rather than as compliance alone. Grounded as to purpose, open as to detail (framework body not read). L1161; REG-1096.
  - P2 Run a data protection impact assessment before high-risk processing, with a description of processing and purposes, necessity and proportionality, risks to individuals, mitigating measures. Grounded for the EU text, inferred as a stack-neutral practice; applies where regulation applies. L1158; REG-1095.
  - P3 Be able to determine within a short, stated clock what a breach touched, and record every breach with facts, effects and remedial action (EU: notify the authority within 72 hours where feasible). The link to logging and classification is inferred. L1159; REG-1095.
- Context variables: regulation in force, L1158 ("applies where regulation applies").
- Links: see `TRANSVERSE.SECURITY_MONITORING.2` and `TRANSVERSE.PRIVACY.1` (the ledger links breach determination to logging and classification, L1159); see `OPERATION.INCIDENTS`.

### `TRANSVERSE.CONFIG` Configuration and Secrets

- Intent: how configuration and secrets reach the running software and are kept apart from code.
- Rows: - (roll-up).
- Links: see `ASSURANCE.SECURITY` (secret scanning, L251, is held there); see `CHANGE_FLOW.BUILD`.

### `TRANSVERSE.CONFIG.1` Separation of Configuration from Code and Secrets

- Intent: what stays out of the codebase and the package, and what stays apart from plain configuration.
- Rows: L158, L1192, L256, L261, L1535
- Positions:
  - P1 Keep configuration strictly separate from code and from the deployable package: config varies across deploys, code does not; test: the codebase could be open-sourced at any moment without exposing credentials; never hardcode secrets in source or committed config. L158 (consensus), L1192 (consensus); REG-092, REG-166, REG-167, REG-174, REG-082, REG-1109. The ledger notes the two rows state the same normative thing and were kept apart.
  - P2 Keep secrets apart from non-secret configuration; confidential data not in a plain configuration object. L256; REG-173, REG-174.
  - P3 Configuration expressed as code lives in a repository with least-privilege access and tracked, attributable changes like source code; secrets stay out of it. Boundary: delivery. L261; REG-004, REG-167.
  - P4 Secrets are never hardcoded in source code or committed configuration, and are drawn, compared, stored and logged only through audited platform mechanisms; a token is accepted only on the recipient's terms: the whole token is rejected if any cryptographic operation or any validation step of the token specification fails. Consensus; grounded for the two constraints (two T1 and T2 sources), open for the clause on audited mechanisms, which no claim grounds. L1535; REG-166, REG-1551, REG-1552, REG-1553. Origin: judged in the JavaScript guideline, its prior verdict (known) is one position here, not the decision. The first clause is the same claim as P1 (L158, L1192). Moved here from `CONSTRUCTION.DATA_NOT_CODE`.
  - No competing position recorded.
- Context variables: none.
- Links: see `CHANGE_FLOW.INTEGRATION` (repository access and tracked changes).
- Stack pointers: L256 (Kubernetes ConfigMap and Secret as example).

### `TRANSVERSE.CONFIG.2` Delivery Channel to the Running Software

- Intent: how configuration and secrets reach the running process, and why that channel was chosen.
- Rows: L254, L1238, L1193
- Positions:
  - P1 Environment variables. Strongest argument: universal, simple, language-neutral, portable, not committed by accident (Twelve-Factor). Forces: cognitive load, portability. Best when: small services and PaaS. L254, L1238, L1193; REG-166, REG-167, REG-173, REG-174, REG-082, REG-1109.
  - P2 Mounted files or a secret or configuration store API, runtime injection from a managed store. Strongest argument: environment variables leak into process listings and child processes and cannot be updated live (the leak vectors are inferred, not read); the API allows subscription to changes; OWASP is cautious about environment variables. Forces: security, rotation, access control, audit. Best when: high-criticality secrets. L254, L1238; REG-166, REG-167, REG-173, REG-174.
  - P3 Non-secret config in source control with strict review, packaged with binaries, as separate config packages or in an external store for dynamic values (Google SRE). Strongest argument: reviewed and promoted with the release. Reconciliation inferred: secrets never in the repository; non-secret config may be versioned if promoted with the release and reviewed. L1193; REG-082, REG-1109.
- Context variables: criticality of the secret (L254, "wins for high-criticality secrets"); team size and platform (L1238: "Choice depends on team size and platform").
- Links: P1 and P2 conflict as channels (L254, L1238); see `TRANSVERSE.CONFIG.1`.
- Stack pointers: L254 (Kubernetes realizes all three).

### `TRANSVERSE.CONFIG.3` Shape of Per-Environment Configuration

- Intent: how configuration differs from one deployment to the next.
- Rows: L255
- Positions:
  - P1 Orthogonal, independent granular variables per deployment (Twelve-Factor). Forces: scalability of environments, cost of ownership. Best when: many deployments (preview, per-tenant). L255; REG-167, REG-174.
  - P2 Named environment bundles (development, test, production). Strongest argument: the full set of an environment can be read and reviewed in one place (inferred; no source states it); the source calls this the traditional approach. Forces: reviewability, control. Best when: few fixed environments. L255; REG-167, REG-174.
- Context variables: number of deployments, L255 ("wins with many deploys", "wins with few fixed environments").
- Links: none.

### `TRANSVERSE.CONFIG.4` Central Secret Custody and Lifecycle

- Intent: where secrets are stored and how access and lifecycle are controlled.
- Rows: L257, L1239
- Positions:
  - P1 Centralize in one managed secrets solution, fine-grained least-privilege access, automated handling over the lifecycle (creation, rotation, revocation, expiry); a platform default store is hardened, not trusted as is. L257; REG-166, REG-173.
  - P2 Centralize and standardize secret storage, least privilege per service, short-lived dynamic secrets with automated rotation, audit every access (keep logs at least 90 days). L1239; REG-166. The ledger notes L1239 and L257 state the same normative thing and were kept apart.
  - No competing position recorded.
- Context variables: none.
- Links: see `TRANSVERSE.SECURITY_MONITORING.2` (access audit).
- Stack pointers: L257 (Kubernetes detail).

### `TRANSVERSE.CONFIG.5` Credential Lifetime and Pipeline Identity

- Intent: how long credentials live and how pipelines and automation authenticate.
- Rows: L258, L259, L1069, L1240
- Positions:
  - P1 Dynamic short-lived credentials with a time to live and automatic revocation where the platform supports it. Strongest argument: a leaked credential expires by itself; a compromise is contained by revoking a lease prefix. Forces: security, blast radius. Best when: many services, high criticality, available platform. L258; REG-166, REG-175.
  - P2 Static secrets rotated on a schedule. Strongest argument (inferred): lower infrastructure cost. Force: team cognitive load. Best when: few services and low criticality. L258; REG-166, REG-175.
  - P3 CI and deployment workflows authenticate with federated short-lived tokens (OIDC) rather than long-lived credentials duplicated into the CI system; the CI-issued token holds the least permissions needed. L259; REG-176, REG-177.
  - P4 Credentials available to automation short-lived, narrowly scoped, kept out of the environment that executes generated code. L1069; REG-1037. The limit on what automation may do is held by `ASSURANCE.SECURITY` (L1065).
  - P5 Treat CI/CD as production: least-privilege service accounts, secrets scoped per environment, no secrets in pipeline output. L1240; REG-025, REG-166.
- Context variables: number of services and criticality, L258 ("wins with many services, high criticality, available platform", "wins for few services and low criticality").
- Links: see `TRANSVERSE.CONFIG.4`; see `CHANGE_FLOW.BUILD`; see `ASSURANCE.SECURITY`.
- Stack pointers: L258 (Vault leases as realization); L259 (GitHub Actions OIDC and token permissions).

### `TRANSVERSE.CONFIG.6` Response to a Leaked Secret

- Intent: what is done when a secret is found exposed.
- Rows: L252
- Positions:
  - P1 Treat a secret found in code or logs as compromised: revoke at once, rotate through an automated process, remove it from the exposed locations, keep audit logs to investigate. Single source, no counter-position found. L252; REG-166.
- Context variables: none.
- Links: see `TRANSVERSE.CONFIG.4`, `TRANSVERSE.SECURITY.5`.

### `TRANSVERSE.ENVIRONMENTS` Development Environments

- Intent: how development, build and test environments are defined, separated and hardened.
- Rows: - (roll-up).
- Links: see `CHANGE_FLOW.DEPLOY` (environment parity), `ASSURANCE.BEHAVIOUR`.

### `TRANSVERSE.ENVIRONMENTS.1` Separation and Isolation

- Intent: how far environments are kept apart and what each may reach.
- Rows: L260
- Positions:
  - P1 Separate and protect development, build, test and production from each other; isolate production and development secrets; non-production minimizes use of production services; human access to build services minimized and audited. The ledger notes this limits dev/prod parity: parity of kind and version, isolation of instance and credentials (inferred synthesis). L260; REG-004, REG-103, REG-166.
- Context variables: none.
- Links: tension with environment parity noted by L260; see `CHANGE_FLOW.DEPLOY`.

### `TRANSVERSE.ENVIRONMENTS.2` Definition Mechanism

- Intent: how the development environment is itself defined as versioned code.
- Rows: L262
- Positions:
  - P1 Container definition (Dev Container): IDE and container integration, wraps existing formats. Forces: cognitive load, onboarding speed. Best when: mixed-skill teams and cloud IDEs. L262; REG-014, REG-168, REG-178.
  - P2 Pinned package set (Nix): byte-level control of package versions across machines and CI. Forces: reproducibility, control; costs: learning curve and Nix on hosts; limits (host OS and kernel outside the pin, availability of pinned sources) inferred, not stated. L262; REG-014, REG-168, REG-178.
  - P3 Dependency manifests with language-level isolation only: lowest cost, but system tools must be vendored. Best when: single-language projects with no native dependencies. L262; REG-014, REG-168, REG-178.
- Context variables: team skill mix and project languages, L262 ("wins for mixed-skill teams and cloud IDEs", "wins for single-language projects with no native dependencies").
- Links: see `OWNERSHIP.LIFECYCLE` (pinning).
- Stack pointers: L262 (tool-specific per option).

### `TRANSVERSE.ENVIRONMENTS.3` Toolchain Control and Hardening

- Intent: how development endpoints are kept trustworthy; pinning and changing the build tools themselves is held in `OWNERSHIP.LIFECYCLE`.
- Rows: L264
- Positions:
  - P1 Development endpoints and toolchain are an attack surface: hardened and monitored (approved hardening guides, least functionality, least privilege, continuous posture monitoring). Single source. L264; REG-004.
  - No competing position recorded.
- Context variables: none.
- Links: see `OWNERSHIP.LIFECYCLE`; see `CHANGE_FLOW.BUILD`.

## Routing objections

Three were raised; each is resolved in `../../objections/resolution.md`. Moved (row now sits on the target branch, no longer listed): L263 to `OWNERSHIP.LIFECYCLE`. Kept where `routing.md` put them (listed with the reason):

1. L1257 (partition by time and drop old partitions instead of bulk DELETE): would go to `CHANGE_FLOW.DATA_CHANGE`. Kept in `TRANSVERSE.PRIVACY.3`: L1258, on the same node, names the partition drop as the bulk-expiry choice of the retention reason, so the deletion mechanism is judged in one place; DATA_CHANGE.6 is how a large change is batched.
2. L1159 (determine what a breach touched, record each breach, notify within a stated time): would go to `OPERATION.INCIDENTS`. Kept in `TRANSVERSE.PRIVACY.4`: the notification obligation and the record sit with the impact assessment (L1158); OPERATION.INCIDENTS holds how an incident is declared and run, and PRIVACY.4 already links to it.
