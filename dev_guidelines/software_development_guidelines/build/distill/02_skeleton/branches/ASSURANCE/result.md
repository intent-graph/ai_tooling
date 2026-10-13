# Result: ASSURANCE branch refinement

Files beside this one: `branch.md` (tree and 54 node records with positions, no verdict), `check_branch.py` (the proof). Each section below reads alone. Certainty words: grounded (a row or the script states it), inferred (my reading), open (undecided or unknown, with what was checked).

## L1 headline

Pinned: Nodes: 54 (L1 1, L2 9, L3 44). Rows attached: 241 of 241; unattached: 0; attached twice: 0. Routing objections: 3. check_branch.py: PASS.

- The ASSURANCE branch is cut below its nine L2 nodes into 44 L3 nodes, each holding one cluster of rows with the competing practices listed and no verdict (grounded: the script proves coverage, one location per row, uid rules and link targets).
- Most positions are real contests the judges must settle: test-level mix, documentation gates, security blocking policy, test environment fidelity, recovery drill placement, versioning against additive change (grounded in the contested rows). The maintainer's codified practice is a named position on every node where it has rows (grounded).
- Seven rows look misplaced and stay where routed, listed as objections (inferred: my reading of the sources, not checked against them).

## L2 claims

Pinned: Nodes: 54 (L1 1, L2 9, L3 44). Rows attached: 241 of 241; unattached: 0; attached twice: 0. Routing objections: 3. check_branch.py: PASS.

- ASSURANCE.RULES (31 rows, 5 L3): trust in a signal rests on five things: a failure means a defect, the check sits as low and as fast as it can, a skipped gate cannot pass, review is independent and binds the exact content, one bar and evidence apply whoever authored the change. Grounded for the positions; the cut into five is inferred. Open: whether an external approval board is still needed under a given regulation (L143: not read).
- ASSURANCE.BEHAVIOUR (61 rows, 8 L3): the largest node, cut by decision type: what the suite promises, the static layer, the level mix, test construction, tests driven by change, measuring adequacy, tests without durable effect on data (maintainer doctrine, 10 rows), and run-time-only defect classes. Grounded for positions; the cut is inferred. Contested: level mix (pyramid, honeycomb, trophy), classical against mockist, test-first, coverage floor, mutation testing. Open: whether the maintainer has any regression run in CI (L331, checked in the doctrine files by the ledger and found none).
- ASSURANCE.CONTRACTS (18 rows, 3 L3): three decisions: what counts as compatible, how contract tests are run (consumer-driven or provider schema), where the description comes from. Grounded. The maintainer's additive evolution without version numbers conflicts with contract tests between services (the coverage check on L295 against L102).
- ASSURANCE.DATA_INTEGRITY (19 rows, 5 L3): where rules live, guarding bulk operations, layered protection and deletion form, derived-data sync, checking old against new. Grounded; the node is mostly maintainer rows (L279 to L284, L313, L314). Contested: soft deletion against hard delete with archive (one T3 source for the critique; the other side was not read, open).
- ASSURANCE.DOCS_SYNC (24 rows, 4 L3): delivery with the change, gates and review, ownership and freshness, mechanical checks. Grounded. Contested: same pull request against a release branch, hard merge gate against reviewer-enforced, style as a CI check against human review. This node holds the content; TRANSVERSE.DOCS is the index (MD-03).
- ASSURANCE.SECURITY (37 rows, 7 L3): verification depth, stage placement and blocking, techniques, static and scheduled analysis, secrets and consumed code, enforced limits on automation, closing the loop. Grounded. The blocking decision appears twice (L246, L1131) and the agent-execution decision twice (L327, L1071): same decision, kept as separate rows. Open: the false-positive threshold that makes a check blockable (L246: not found).
- ASSURANCE.PERFORMANCE (22 rows, 5 L3): targets, load test design, when tests run and baselines, production testing, measurement before optimization. Grounded; several rows rest on a single T1 to T3 source. Contested: test environment fidelity by criticality, gating every change against scheduled runs.
- ASSURANCE.AVAILABILITY (23 rows, 5 L3): tolerating a degraded dependency, protecting remote calls, verifying resilience, proving restore, exercising recovery. Grounded. Contested: breaker against retry budget against neither, drills in production against non-production first. Proof of recovery is here; practice stays in OPERATION.RECOVERY (MD-03).
- ASSURANCE.ARTIFACT (8 rows, 2 L3): build provenance and match to source; a protected mainline that binds every actor. Grounded. Contested: reproducible rebuild against trusting signed provenance.
- Routing objections (7, inferred): L131 to CHANGE_FLOW.INTEGRATION; L118 to CHANGE_FLOW.DEPLOY; L238 to CHANGE_FLOW.BUILD; L229 and L318 to TRANSVERSE.DOCS; L313 to OPERATION.TELEMETRY; L275 to OPERATION.INCIDENTS.

## L3 full

Pinned: Nodes: 54 (L1 1, L2 9, L3 44). Rows attached: 241 of 241; unattached: 0; attached twice: 0. Routing objections: 3. check_branch.py: PASS.

Method (grounded): rows read in full one L2 node at a time; L3 cut from each node's intent, then rows attached; rows carry their positions from the ledger; MAINT rows (source MAINT-S01, REG-181, not citable) are named positions; rows marked as judged in the JavaScript guideline keep their prior verdict as one position. No verdict, no ranking, no editing of rows.

ASSURANCE.RULES
- RULES.1 Trustworthy Signal (10: L086, L109, L110, L111, L147, L1132, L1558 to L1561): flake handling splits into quarantine, remove at once, rerun marked tests, classify and retry, prevent at the cause; false-positive budget under 10% is one organisation's policy. Grounded; thresholds single-source.
- RULES.2 Placement and Feedback Speed (8: L091, L112, L121, L145, L1183, L1538, L1546, L1550): low-level placement, minutes of feedback, gate-fast-run-slow-after against staged pipeline (contested), per-stage policy, combined checks. Grounded; L1538, L1546 inferred by the origin.
- RULES.3 Gates That Cannot Be Skipped (3: L1216, L1234, L1562): automated boundary checks and fitness functions; a skipped required check must not pass. Required by BEHAVIOUR.1 and BEHAVIOUR.2. Inferred for L1216 and L1562.
- RULES.4 Independent Review That Binds (5: L136, L143, L1043, L1046, L1047): independent human check, no external board, named accountable person, different approver, approval bound to final content. Grounded; one dissent (Ship, Show, Ask); regulation open.
- RULES.5 One Bar and Evidence for Every Change (5: L1042, L1045, L1051, L1052, L1053): same bar, intent fixed before production, executable check, evidence, independent test contexts. Grounded except L1053 (inferred).

ASSURANCE.BEHAVIOUR
- BEHAVIOUR.1 What the Suite Must Promise (9): self-testing, strict or weak "test everything", policy, ownership, and the maintainer's open gap on who runs the suite (L331). Grounded; L331 open.
- BEHAVIOUR.2 Static Layer (8): enforce types against gradual against tests alone (open minority), warnings as errors, incremental analysis, complexity gates. Grounded.
- BEHAVIOUR.3 Test Level Mix (7): pyramid, honeycomb, trophy with conditions; end-to-end minimal; larger tests by fidelity. Contested, grounded.
- BEHAVIOUR.4 Test Construction (10): solitary or sociable, classical or mockist, state or interaction, real implementation before fake before mock, real backing service, DAMP. Grounded; classical against mockist contested.
- BEHAVIOUR.5 Tests Driven by Change (4): test-first as team decision (Beck, DHH, Fowler), bug to failing test, characterization, scheduled job in test mode. Grounded.
- BEHAVIOUR.6 Measuring Adequacy and Probing for Faults (8): coverage diagnostic or floor, mutation gate or offline (benefit open), property-based, fuzzing. Contested; mutation benefit open (no effect size).
- BEHAVIOUR.7 Tests Without Durable Effect on Data (10): disposable store per run against the maintainer's forced rollback on real data; fixtures synthetic against curated real corpus; execution vehicle by risk; colocated tests. Grounded; the maintainer contradicts common practice and conflicts with RULES.1 (L265 against L111).
- BEHAVIOUR.8 Defect Classes That Survive Review (5): all maintainer rows: run-time-only defects, pitfall catalogue, no blanket replace, empirical platform checks, silent truncation. Grounded as the maintainer's doctrine; no competing public position.

ASSURANCE.CONTRACTS
- CONTRACTS.1 What Counts as Compatible (4: L060, L105, L295, L352): explicit versioning against the maintainer's additive evolution with coordinated breaks; condition: number of consumers. Grounded; conflicts with CONTRACTS.2.
- CONTRACTS.2 Contract Tests (8): contract tests over shared environments, consumer-driven against provider schema against both, single-team case open, doubles checked on the supplier's cadence. Grounded; L1187 open.
- CONTRACTS.3 One Source of Description (6): one machine-readable description, code-first against design-first, where the type chain starts (inferred), lint and breaking-change diff in CI. Grounded; L1277 inferred.

ASSURANCE.DATA_INTEGRITY
- DATA_INTEGRITY.1 Where Integrity Rules Live (2): application layer, the maintainer's store-level integrity, split by kind with a contested middle zone. Grounded; L1262 inferred.
- DATA_INTEGRITY.2 Guarding Bulk and Destructive Operations (3): explicit opt-in flag (maintainer) and migration linting, the latter its nearest public form (inferred).
- DATA_INTEGRITY.3 Layered Protection and Deletion Form (6): layered defence, undo is a restore, soft deletion, its costs, hard delete plus archive. Contested; one T3 source for the critique.
- DATA_INTEGRITY.4 Derived Data Sync and Staleness (4): the maintainer's sync ladder against always-consistent against eventual; scheduled detection; staleness as design; four monitoring signals (objection: L313).
- DATA_INTEGRITY.5 Checking Old Against New and Rolling Out Checks (4): shadow reads, validation before removal, self-auditing conventions, observe-only rollout against immediate enforcement.

ASSURANCE.DOCS_SYNC
- DOCS_SYNC.1 Delivery with the Change (4): docs as code, same pull request against release branch, workflow reuse, reduced pipeline (objection: L238).
- DOCS_SYNC.2 Gates and Review of Documentation (8): trigger rule, merge gate against encouraged against release gate (contested), follow-up issue, owners, three review kinds, who writes (objection: L229).
- DOCS_SYNC.3 Ownership, Freshness and Single Source (7): owner, dates, one canonical document, the maintainer's header comment against self-documenting code (objection: L318), read-only derived documents.
- DOCS_SYNC.4 Mechanical Documentation Checks (5): executable examples, build fails on warnings, link checks including scheduled, style as CI against human review, automated chores.

ASSURANCE.SECURITY
- SECURITY.1 Verification Depth and Design Review (5): design review against the risk model, depth per application, floor is a lower bar, threat model selects tests.
- SECURITY.2 Stage Placement and Blocking Policy (4): policy by stage and risk, earliest stage, block against advise against audited waiver against team choice. Contested; threshold open.
- SECURITY.3 Verification Techniques (8): security tests, secure defaults, every change, developer floor against fuller programmes, fuzzing, dynamic scan, manual plus automated.
- SECURITY.4 Static and Scheduled Analysis Practice (3): per commit against nightly, same sources for different tool speeds; blind spots and triage.
- SECURITY.5 Secrets and Consumed Code (3): scanning consumed artifacts, same verification as own code, layered secret scanning.
- SECURITY.6 Enforced Limits on Automation and Access (11): limits in tooling not prompts, least privilege, no session combining untrusted input, sensitive access and ungated change (single T3), untrusted input, steering files reviewed, the maintainer's lowest-layer access, agent executes under guards against writes only (contested).
- SECURITY.7 Closing the Loop on Findings (3): detection is tested, fix and change the process, regular effectiveness review.

ASSURANCE.PERFORMANCE
- PERFORMANCE.1 Targets and Budgets (3), PERFORMANCE.2 Load Test Design (7), PERFORMANCE.3 When Tests Run and Baselines (4), PERFORMANCE.4 Testing in Production for Performance (2), PERFORMANCE.5 Measurement Before Optimization (6): fidelity by criticality (identical, scaled down, production), gate every change against scheduled runs, pre-production only against controlled production tests. Grounded; contested as listed; L430 inferred as a rule.

ASSURANCE.AVAILABILITY
- AVAILABILITY.1 Tolerating a Degraded Dependency (2), AVAILABILITY.2 Protecting Remote Calls (8): timeouts, retries, idempotency, budgets, breaker against budget against neither (contested).
- AVAILABILITY.3 Verifying Resilience Under Real Conditions (3): canary and A/B diff (objection: L118), testing in production, production experiments against pre-production only (counter-position unsourced, open).
- AVAILABILITY.4 Proving Restore (6), AVAILABILITY.5 Exercising Recovery (4): restore defines backup, criteria fixed beforehand, exercise ladder, drills in production against non-production first (contested), measured times as planning minimum.

ASSURANCE.ARTIFACT
- ARTIFACT.1 Build Provenance and Match to Source (5): reproducible rebuild against signed provenance, level by risk, framework requirements (content open), maintainer's deployed-against-source comparison.
- ARTIFACT.2 Protected Mainline Binds Every Actor (3): mainline protection (objection: L131), rules bind bots and administrators, restricted automation target.

Routing objections (7, inferred): L131, L118, L238, L229, L318, L313, L275; targets and reasons in `branch.md`.
