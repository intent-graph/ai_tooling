# Judged records: unit J9_transverse

Nodes: 36 (the L1 node TRANSVERSE, 6 L2 roll-ups, 29 L3), in tree order: TRANSVERSE; TRANSVERSE.DOCS (.1-.5); TRANSVERSE.SECURITY (.1-.6); TRANSVERSE.SECURITY_MONITORING (.1-.5); TRANSVERSE.PRIVACY (.1-.4); TRANSVERSE.CONFIG (.1-.6); TRANSVERSE.ENVIRONMENTS (.1-.3).
Binding: MD-01 (best, not average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-05 (regulated contexts deferred), MD-06 (flags go to the Opus pass).
Decided input read: `J3_assurance_integrity/judged.md` (final after review): ASSURANCE.DOCS_SYNC.1-.4, ASSURANCE.SECURITY.1, .2, .5, .6, .7, ASSURANCE.DATA_INTEGRITY.1, .3. Their verdicts are treated as settled; nothing here re-decides them.
Decisions marked undecided: none.
Settled decisions disagreed with: none. (Two maintainer-codified rows are decided against in part, with the condition under which they would be best: L318 change log in the header, TRANSVERSE.DOCS.3; L321 hand-kept line-number tables of contents, TRANSVERSE.DOCS.2. They are positions under MD-01, not settled decisions.)
Flags raised by the judge (all settled in the final pass; none remains open as a flag; open certainty items stay at their nodes): (T1) DOCS.3 mandatory dated change log in the header rejected against a maintainer row; (T2) DOCS.4 condition under which a generated changelog is best, open (narrowed); (T3) SECURITY.2 no evidence that maturity scores reduce incidents, open; (T4) SECURITY.6 bounty yield open; (T5) MON.1 logging of security events set regardless of the verification level of the standard, inferred; (T6) PRIVACY.3 how a locked backup is put beyond use, open, and erasure reaching copies contested; (T7) CONFIG.1 the token-acceptance clause of L1535 is not a configuration rule and sits on the wrong node, relocation proposed; (T8) CONFIG.2 the split of custody from delivery channel is this judge's reconciliation of two contested rows, inferred.
Index nodes (MD-03): TRANSVERSE.DOCS and TRANSVERSE.SECURITY hold only what ASSURANCE.DOCS_SYNC and ASSURANCE.SECURITY do not; where a row's content is already decided there, the record points to it and adds nothing.
Rows cited by ledger id, sources by register id (REG). MAINT rows (REG-181) are not citable and weigh as a strong position.

---

## TRANSVERSE Transverse

Intent: practices that cut across every branch: documentation practice, security programme, security monitoring, privacy and retention, configuration and secrets, development environments.
Decision (rolled up): each cross-cutting concern is carried out as an owned, recorded practice whose guarantee is held elsewhere (documentation sync and security verification in ASSURANCE): documentation is sized, structured and written for its readers; security is anchored in a framework, modelled at design time, owned, logged, detected on and answered; personal data is minimised, classified, retained on a recorded schedule and erasable; configuration and secrets are kept out of the code and artifact and delivered through custody that is least-privilege, short-lived and audited; development environments are defined as code, separated from production and hardened. Outcome: the guarantees ASSURANCE decides have a practice that can be carried out and checked.
Certainty: inferred (roll-up of grounded components; no source states the set).
Flags: none of its own.
Links: Realizes ASSURANCE.DOCS_SYNC, ASSURANCE.SECURITY.

---

## TRANSVERSE.DOCS Documentation Practice

Intent: how documentation is organised, written and budgeted so that it is read and kept up; the mechanisms that keep it true are in ASSURANCE.DOCS_SYNC (MD-03).
Decision (rolled up): the amount of documentation is a recorded choice sized by consumers, life and turnover; documents are small, organised by reader need and navigable from an index; text is layered by depth and audience, with the durable explanation of a unit kept with the unit; release changes are recorded for the reader. Outcome: documentation is found, read at the depth the reader needs, and cheap enough to keep current.
Certainty: inferred (roll-up).
Flags: none.
Links: Realizes ASSURANCE.DOCS_SYNC; mechanisms (same-change delivery, gates, owners, executable examples, one canonical document per topic) are stated only there.

### TRANSVERSE.DOCS.1 Documentation Budget

Intent: how much documentation to produce and maintain, as a deliberate and budgeted choice.
1. Decision: The amount of documentation is a recorded decision, and upkeep is budgeted as part of delivery, not left to goodwill. The level follows the system: minimal and conversation-first where the team is small, co-located and the system short-lived; living documentation generated or extracted from code and tests where the domain knowledge is already in the code; full docs-as-code with owners and gates (ASSURANCE.DOCS_SYNC) where consumers are many, life is long and people turn over. Whatever the level, effort is allocated so that accuracy-critical text is written by someone who knows the system and specialist writing effort goes to documents that cross interface boundaries and to shared guidance. Outcome: the volume of documentation is one the team can keep true, and the readers who pay most for its absence are covered first.
2. Grounds: documentation quality is read as a driver of delivery capability (L231; REG-152; correlational survey data, causality inferred); three levels each win under a stated condition, context mapping marked inferred by the ledger (L236; REG-150, REG-155, REG-164); allocation of effort (L229; REG-150, REG-152), restated as an outcome per MD-02 and consistent with the audience-review rule of ASSURANCE.DOCS_SYNC.2.
3. Positions: P1 invest and budget (delivery capability, cost of ownership). P2 minimal, conversation first (cost, speed). P3 living documentation (no manual sync). P4 full docs-as-code with owners and gates (confidence, newcomer load). P5 engineers write, writers focus on cross-boundary documents and guidelines.
4. Rejected: P2 as a universal default: best for small co-located teams and short-lived systems. P3 as a universal default: best where the knowledge is in the code; it cannot hold why, context or decisions. P4 as a universal default: best with many consumers, long life, turnover; costs more than a small system can keep up. P5 as a rule about who writes: not stated as a rule (MD-02); kept as the allocation outcome.
5. Context: scope and life of the system (many consumers, long life, turnover against a small co-located team, short-lived system); the single variable L236 shows moving the answer.
6. Certainty: grounded for the positions and their conditions; the context mapping and the causal reading of P1 are inferred.
7. Flags: none.
Constraints: MUST record the chosen level; MUST record the upkeep budget.
Links: Requires ASSURANCE.DOCS_SYNC (P4 relies on its owners and gates); see ASSURANCE.DOCS_SYNC.3 (derived documents are read-only).

### TRANSVERSE.DOCS.2 Organisation and Structure

Intent: how documents are cut and arranged so that they are small enough to be updated and found by the reader who needs them.
1. Decision: Documents are small and modular, each organised by one reader need (tutorial, how-to, reference, explanation), reached from an index by role and situation, with cross-references kept and the index updated in the same change as the documents. The set is improved in small increments published at once, never by one large restructuring. Where a formal model exists, each guideline links to the model node it derives from. Size caps are enforced mechanically; a line-number table of contents or line count is acceptable only if generated and checked by a tool, never kept by hand. Outcome: a reader finds the one document for their need, and each document is small enough that its owner updates it.
2. Grounds: small documents get updated, large ones do not (L233; REG-150, REG-154); organisation by reader need and incremental improvement (L234; REG-157; one framework read, other taxonomies not); router set with index by role and situation, size cap and links to the model (L321; MAINT, REG-181). The three are facets of one structure (size, axis of organisation, navigation), not rivals; no sentence here blends competing answers. The ledger notes that line counts and tables of contents rot, which is why they are admitted only when checked by a machine (ASSURANCE.DOCS_SYNC.4).
3. Positions: P1 small modular documents (keeping documents current). P2 organise by reader need, increments (reader fit). P3 router set with size cap and tables of contents (maintainer; navigation).
4. Rejected: hand-kept line-number tables of contents and line counts: best never, they rot unchecked; best when generated and verified by a tool. One large specification: best never for living documentation (it is not updated).
5. Context: none.
6. Certainty: grounded for P1 and P2 (one taxonomy source for P2); P3 grounded as maintainer practice agreeing with common practice; the generated-only condition is inferred.
7. Flags: none.
Constraints: MUST keep an index updated in the change that adds or moves a document; MUST NOT keep line-number annotations by hand.
Links: see ASSURANCE.DOCS_SYNC.3 (one canonical document per topic), ASSURANCE.DOCS_SYNC.4 (mechanical checks).

### TRANSVERSE.DOCS.3 Layered Writing and Audience Split

Intent: how a document, including the explanation inside code, is written for readers at different depth and background.
1. Decision: Write at layered depth (one sentence, one paragraph, then full what, why and how) with diagrams at three zoom levels (macro, flow, detail), so that a non-engineer can take the why and an engineer the how, with technical vocabulary confined to the internal part. In code, the durable explanation of a unit lives with the unit: inline comments carry only why, invariant or gotcha, never what the next line does; a unit consumed by many callers carries a structured header (summary, parameters, returns, notes, examples with expected output) because its readers will not read its body; long logic gets short step banners mirrored in the header. History is not kept in the header: version control holds it, except where readers cannot see the repository history. Outcome: each reader stops at the depth they need, and the explanation of a unit cannot drift into a second, divergent source of history.
2. Grounds: layering and audience split (L322; MAINT, REG-181; agrees with common practice per the ledger); one durable explanation per unit and why-only inline comments (L318; MAINT, REG-181, the ledger reads public practice as contested); the header change log and its dating duplicate version history (partial tension with L133 and L218 per the ledger, agreement on dating with L216), so history is not duplicated in the header (one origin per fact, L218; ASSURANCE.DOCS_SYNC.3). Final pass: settled unchanged; one origin per fact (MD-03, ASSURANCE.DOCS_SYNC.3) and commits carrying what and why (L133) put history in version control; the maintainer's own condition (L318: readers who cannot see the repository history) is honoured, and covers definitions read where they are deployed, such as a function read from a database catalogue (inferred). Listed under "Settled against your practice" for code read inside the repository.
3. Positions: P1 layered detail and audience split (maintainer). P2 mandatory structured header, why-only inline comments, step banners (cognitive load, durability). P3 self-documenting code, history in version control (cost of ownership).
4. Rejected: mandatory header on every unit: best when the unit is called by many consumers and lives apart from its history; for a private helper P3 is best. Dated change log in the header: best only where readers cannot see repository history. Self-documenting code as the whole answer: best when the unit is small, local and its contract is obvious from its name and types; fails on why and on invariants.
5. Context: whether the unit is called by many consumers and lives apart from its history (the row's own condition).
6. Certainty: grounded for P1 (maintainer, agrees with common practice); inferred for the choice against the header change log (rests on L133, L216, L218 tension, one maintainer row).
7. Flags: none.
Constraints: MUST NOT state in an inline comment what the next line does; MUST NOT hold change history in two places; MUST give an interface consumed by many callers a structured header.
Links: see ASSURANCE.DOCS_SYNC.3 (one canonical document, dated verification), ASSURANCE.DOCS_SYNC.4 (executed examples), CHANGE_FLOW.INTEGRATION (history in commits).

### TRANSVERSE.DOCS.4 Release Changelog

Intent: how the record of what changed in each release is kept for its readers.
1. Decision: Each release has a changelog written for its readers, grouped by change type, with an "Unreleased" section filled as changes land, so the release note is assembled from entries made in the change itself (presence enforced by the chore rule in ASSURANCE.DOCS_SYNC.4). A list generated from commit messages may seed the draft but is not the record, because commit logs are noisy and document the evolution of the source, while a changelog tells readers the noteworthy differences (REG-162). Outcome: a reader sees what changed for them, per release, without reading history.
2. Grounds: human-written, grouped by type, Unreleased section (L235; REG-161, REG-162); entry-present chore rule (ASSURANCE.DOCS_SYNC.4, L226). The reason against the generated list is grounded in REG-162: commit log diffs are full of noise; commits document the evolution of the source, a changelog tells readers the noteworthy differences.
3. Positions: P1 human-written per release (reader fit). P2 generated from commit conventions (cost of ownership; recorded, not read).
4. Rejected: P2 as the record: best when every commit is held to a convention written for readers and the readers are the developers of the same code (the condition is inferred).
5. Context: none shown by a row.
6. Certainty: grounded for the rule and for the reason against the generated record (REG-162); the condition under which P2 would be best is inferred and open.
7. Flags: none (the open condition under which a generated changelog is best stays in Certainty).
Constraints: MUST fill the Unreleased section in the change that introduces the entry.
Links: see CHANGE_FLOW.RELEASE; ASSURANCE.DOCS_SYNC.4.

### TRANSVERSE.DOCS.5 Basis and Evolution of Guidelines

Intent: from what a guideline is derived and how it is updated, so that a new rule states which earlier rule it overrides.
1. Decision: Every rule records its basis: observed practice, with the evidence, or a principle, with the outcome it guarantees. In a mature codebase rules are induced from analysis of real production code and updated as practice evolves; where there is no mature practice yet, they are deduced from principles and marked as such until practice confirms them. A rule that overrides an earlier one states which rule and for which objects. Outcome: a reader can tell why a rule exists, how much evidence stands behind it, and what it replaced.
2. Grounds: induced from real code, overrides stated (L323; MAINT, REG-181; wins in a mature codebase; the ledger records an internal tension with deduction and no public claim for or against). The override note is common to both bases and is the grounded core.
3. Positions: P1 induced from practice (what works and is adopted; cost). P2 deduced from principles (correctness, consistency).
4. Rejected: P1 in an immature codebase: it codifies habits, not good practice. P2 as the only basis: best when no practice exists to observe; it never tests the rule against reality.
5. Context: maturity of the codebase (L323: wins in a mature codebase).
6. Certainty: grounded for the override note (L323); the basis record and the 'deduced, unconfirmed' marker are inferred from the guideline's own method: a rule without a stated basis cannot be re-judged (MD-01).
7. Flags: inferred parts noted.
Constraints: MUST state the basis of each rule; MUST state the overridden rule and its objects.
Links: see EVOLUTION.DECISIONS (records of an overriding rule).

---

## TRANSVERSE.SECURITY Security Practice

Intent: how a security programme is anchored, risk modelled, responsibility owned and vulnerabilities handled; verification and enforcement are in ASSURANCE.SECURITY (MD-03).
Decision (rolled up): the programme is anchored in a published framework chosen by the question asked, risk is modelled at design time at a depth set by risk, responsibility is explicit and owned from the top, and every reported or found vulnerability follows one loop with a published intake. Outcome: security work is covered across the lifecycle, owned, and learns from each finding.
Certainty: inferred (roll-up).
Flags: none.
Links: Realizes ASSURANCE.SECURITY; verification depth, blocking, tests, scanning and limits on automation are stated only there.

### TRANSVERSE.SECURITY.1 Anchor Framework

Intent: which published framework anchors the secure-development practice, chosen by the question the team needs answered.
1. Decision: The practice is anchored in a published framework used as a list of outcomes to cover across the lifecycle, not as a prescription of tools, and the framework is chosen by the question: a requirements standard (ASVS) to specify and verify the technical requirements of an application or a supplier, selected by level from the application's risk; a prescriptive maturity model (SAMM) to assess and plan a programme across many teams, with an outcome framework (SSDF) as the list of outcomes the programme covers (P1); a descriptive benchmark (BSIMM) only as evidence of what peers do, never as the rule for what to do. Outcome: the anchor answers a real question and no practice is adopted because peers have it.
2. Grounds: outcome list, not tools (L240; REG-004, REG-171); the choice by question (L1120, inferred synthesis of what each source says it is for; REG-1078, REG-1084, REG-1085, REG-171, REG-180); verifiable catalogue serving requirements and testing (L250; REG-180); common practice is not best practice for the benchmark (L1120 on BSIMM). Final pass: L1120 places only SAMM in the assess-and-plan role; L240 treats SSDF as an outcome list. ASVS level shares (about 20%, 50%, 30%; L1121, REG-1078) are reference facts, not decision content.
3. Positions: P1 outcome list (coverage). P2 requirements standard (correctness, control). P3 prescriptive maturity model (programme at scale). P4 descriptive benchmark (comparison).
4. Rejected: P2 as the programme anchor for many teams: best for one application or a supplier contract. P3 for one application: best with many teams. P4 as a decision rule: best only to justify investment to a sponsor.
5. Context: scope of the programme (single application or supplier contract against many teams), shown by L1120.
6. Certainty: grounded for what each framework is for; inferred for the mapping by question (marked inferred by the ledger); open: ASVS level definitions were not read (L250).
7. Flags: none.
Constraints: MUST name the anchor framework and the question it answers; MUST NOT use a descriptive benchmark as the verdict on what to adopt.
Links: Requires ASSURANCE.SECURITY.1 (depth set per application from risk selects the ASVS level); see TRANSVERSE.SECURITY.2.

### TRANSVERSE.SECURITY.2 Maturity Targets and Cycle

Intent: how a maturity model is used and how far its scores can be trusted.
1. Decision: A maturity model is run as a cycle: assess current practice, set a target per practice from context (a high level in one practice does not require it in the others), build a roadmap, take the model's prescriptive activities. Descriptive benchmark data is evidence of what peers do, not the verdict. A maturity score or an ASVS level measures programme activity and requirements coverage, not security outcomes, so it is paired with outcome measures (time to detect, a managed figure in TRANSVERSE.SECURITY_MONITORING.4; defects found per stage and closed findings, inferred) and is not reported as evidence that the system is safer. Outcome: effort goes where context needs it, and no score is read as more than it measures.
2. Grounds: target per practice (L1123; REG-1084); cycle (L1125; REG-1084, REG-171); benchmark as evidence (L1124; REG-1085; inferred consequence); no source shows higher scores reduce incidents (L1162; REG-1078, REG-1084, REG-1085, REG-171; open). Pairing with outcome measures follows from L1162 and is inferred; ASSURANCE.SECURITY.7 holds only that effectiveness is itself tested.
3. Positions: P1 target per practice. P2 cycle. P3 benchmark as evidence.
4. Rejected: one uniform level across all practices: best never as a policy (spends where context does not need it). Score as proof of security: best never on current evidence.
5. Context: none shown by a row.
6. Certainty: grounded for P1 and P2; inferred for P3 and for the pairing with outcome measures; open: whether maturity or level raises outcomes.
7. Flags: none (that no source read shows maturity scores or ASVS levels reduce incidents stays in Certainty).
Constraints: MUST set targets per practice; MUST NOT present a score as an outcome measure.
Links: see TRANSVERSE.SECURITY.1; TRANSVERSE.SECURITY_MONITORING.4 (time to detect); ASSURANCE.SECURITY.7 (effectiveness is itself tested).

### TRANSVERSE.SECURITY.3 Design-Time Risk Modelling

Intent: how security risk is modelled during design and how the findings are tracked.
1. Decision: Security risk is modelled during design and again whenever a design change touches data sensitivity, authentication, access control, credentials or a trust boundary; the depth is set by risk: lightweight per change by default, deeper assessment for the high-risk areas and under criticality or regulation. Each model answers four questions (what are we working on, what can go wrong, what are we going to do about it, did we do a good enough job), and its risks and mitigations are tracked in the team's workflow. Outcome: the model is not stale at the next change and effort sits where the cost of error is.
2. Grounds: a one-off model is stale at the next change (L241 position a; REG-004, REG-165); effort proportioned to risk (L241 position b, SSDF); the ledger states the two are compatible and the choice is trigger and cadence, which this decision sets as design change and risk; four questions and tracking (L242; REG-004, REG-165). The trigger wording is inferred.
3. Positions: P1 continuous, lightweight (correctness over time, feedback speed). P2 deeper, risk-triggered (cost). P3 four questions, tracked.
4. Rejected: P1 alone for high-risk areas: best for fast-changing products with an engaged team where risk is moderate. P2 alone: best under criticality or regulation, but a model refreshed only on a risk trigger goes stale on the lower-risk changes between.
5. Context: criticality or regulation sets the depth (L241).
6. Certainty: grounded for the positions and the four questions; inferred for the trigger rule.
7. Flags: none.
Constraints: MUST track mitigations in the team's workflow; MUST remodel on a design change that touches a trust boundary.
Links: see ASSURANCE.SECURITY.1 (design reviewed against the risk model before implementation proceeds; the model output selects tests).

### TRANSVERSE.SECURITY.4 Responsibility and Training

Intent: who owns security outcomes and how the owners are prepared.
1. Decision: Security responsibility is explicit and owned from the top: roles and responsibilities are defined, training is role-based, management commits, and the producer takes ownership of the security outcomes its customers experience. Outcome: every security outcome has a named owner who has been prepared for it.
2. Grounds: L249 (REG-004, REG-172); consensus, single framework family, no counter-position found.
3. Positions: P1 explicit responsibility owned from the top.
4. Rejected: none competes. Responsibility by goodwill: best never.
5. Context: none.
6. Certainty: grounded (consensus, one family of sources).
7. Flags: none.
Constraints: MUST name an owner per security outcome.
Links: none.

### TRANSVERSE.SECURITY.5 Vulnerability Response Loop

Intent: how a vulnerability, once reported or found, is confirmed, assessed, fixed and learned from.
1. Decision: A reported or discovered vulnerability, in own or consumed code, follows one loop: identify and confirm (monitored databases and reports, the disclosure policy), assess, prioritize by a stated rule, remediate within a stated time, then analyse root causes and fix the process as well as the instance (the change to the process and the class-precluding approach are held in ASSURANCE.SECURITY.7). Outcome: no known vulnerability sits unassigned, and each one improves the process.
2. Grounds: L253 (REG-004); the stated rule and time are inferred from L1141 (the response and fix times) and from the need for an auditable loop; the learning step is the same decision as ASSURANCE.SECURITY.7 (L1139), stated there once (MD-03).
3. Positions: P1 response loop.
4. Rejected: fixing the instance only: best never. Handling in operation only: incident handling is in OPERATION.INCIDENTS; this loop covers the vulnerability, not the live incident.
5. Context: none.
6. Certainty: grounded for the loop (single source); inferred for the stated prioritization rule and time.
7. Flags: none.
Constraints: MUST state the prioritization rule and the remediation time.
Links: see TRANSVERSE.SECURITY.6 (intake), ASSURANCE.SECURITY.7, OPERATION.INCIDENTS.

### TRANSVERSE.SECURITY.6 Disclosure Policy and Bounty

Intent: how outsiders report a vulnerability to the team and whether the team pays for reports.
1. Decision: Any system reachable by outsiders publishes a disclosure policy: how to report, a private channel, an acknowledgement within a stated time, a fix of known medium-or-higher vulnerabilities within a stated time, and the contact in a standard place (security.txt with Contact and Expires). The day counts are the team's own commitments, with 14 days to answer and 60 to fix as one project's reference values. A paid bounty is added only after weighing cost, competence and maturity, when triage is mature and the attack surface wide; a periodic penetration test alone is best only when the system cannot be exposed to outside researchers. Outcome: a finder knows where to report and what to expect, and the team can meet what it promised.
2. Grounds: publish how to report, private channel, times, standard place (L1141; REG-1094, REG-1097, REG-1098); policy first, bounty after weighing (L1142; REG-1094, REG-1097). No source compares bounty yield.
3. Positions: P1 content of the policy: channel, times, security.txt (L1141; finder clarity, control). P2 disclosure policy without a bounty (L1142; cost, control; the default of the Decision). P3 policy plus paid bounty (speed of finding). P4 penetration test alone (control, scope).
4. Rejected: P3 as default: best with mature triage and a wide attack surface. P4: best when the system cannot be exposed to outside researchers. P2 is the Decision's default, not rejected.
5. Context: triage capacity and attack surface (L1142).
6. Certainty: grounded for the policy; open for the commercial case for a bounty (only vendor documentation surfaced, not read).
7. Flags: none (that no source read compares bounty yield stays in Certainty).
Constraints: MUST state response and fix times only the team can meet; MUST publish a private reporting channel.
Links: see TRANSVERSE.SECURITY.5.

---

## TRANSVERSE.SECURITY_MONITORING Security Monitoring and Audit Trail

Intent: what security-relevant events are logged, protected, detected and kept as an audit trail.
Decision (rolled up): security-relevant events are logged with enough content to reconstruct who did what, when and where; logs are protected and free of what must not be in them; detection and escalation exist for active attacks and for logging stopping; the business audit trail is a separate artifact from the security event log. Outcome: an attack is seen in time, can be reconstructed, and a change to data can be accounted for.
Certainty: inferred (roll-up).
Flags: none.
Links: Realizes ASSURANCE.SECURITY (verification that detection works is ASSURANCE.SECURITY.7); see OPERATION.TELEMETRY, OPERATION.ALERTING.

### TRANSVERSE.SECURITY_MONITORING.1 Events Logged

Intent: which security-relevant events are recorded, including actions by automation.
1. Decision: Log security-relevant events: authentication successes and failures, authorization failures, input and output validation failures, session management failures, administrative actions, sensitive data access, use of higher-risk functionality, application errors, and security control failures and bypass attempts. Every action taken by an automated actor (command, tool call, plan change) is logged in a reviewable audit trail. Data-change events are logged per need, as part of the business audit trail (.5), not as security events. Outcome: attacks and misuse leave a record, and automation can be reconstructed.
2. Grounds: event list (L1143; REG-1079, REG-1089, REG-1090); automation audit trail (L1073; REG-1034, REG-1036, REG-1037); logging is the precondition for detection (L1146) and for breach determination (PRIVACY.4, inferred link). The note that ASVS 5.0 requires these only at levels 2 and 3 is a fact about what the standard verifies, not about what to log.
3. Positions: P1 security event list (detection, reconstruction). P2 log every automated action (accountability).
4. Rejected: logging only what the verification level of the standard requires: best never; an application at level 1 still needs the record to detect and to bound a breach.
5. Context: none shown by a row.
6. Certainty: grounded for the lists; grounded for setting logging independently of the ASVS level: the OWASP Logging Cheat Sheet, fetched in review, says to log these events without levels; ASVS levels set what is verified, not what is needed; ASSURANCE.SECURITY.1 (depth by risk) governs verification depth, not whether security events are recorded.
7. Flags: none.
Constraints: MUST log authentication, authorization and validation failures; MUST log automation actions to a trail a person can review.
Links: see ASSURANCE.SECURITY.1 (the assurance target); OPERATION.TELEMETRY.

### TRANSVERSE.SECURITY_MONITORING.2 Entry Content, Time and Format

Intent: what each log entry contains and how entries from many systems are ordered and read together.
1. Decision: Every entry records who, what, when and where (timestamp, application and address, source address and authenticated identity, event type, severity, affected object, result and reason). One event vocabulary (category prefix plus action) and one format are used across systems, timestamps are ISO 8601 in UTC or with an explicit UTC offset, server clocks are synchronized, an inventory states what is logged at each layer, and logs go only to documented destinations. Where clocks cannot be synchronized (remote clients), the server's receipt time is recorded as well (inferred). Outcome: events from many systems can be sequenced, and monitoring can key on stable terms.
2. Grounds: who, what, when, where, inventory, UTC, common format, documented destinations (L1144; REG-1079, REG-1089); vocabulary and ISO 8601 (L1245; REG-1136); synchronized server time, impossible for remote clients (L1248; REG-1089); receipt time is this judge's inference from that limit.
3. Positions: P1 entry content and inventory. P2 vocabulary and timestamps. P3 time synchronization.
4. Rejected: none competes; three parts of one entry design. Free-text entries: best never where monitoring must key on the terms.
5. Context: none.
6. Certainty: grounded; the receipt-time clause inferred.
7. Flags: none.
Constraints: MUST use UTC-anchored ISO 8601 timestamps; MUST keep one event vocabulary.
Links: see ASSURANCE.SECURITY.7; OPERATION.TELEMETRY.

### TRANSVERSE.SECURITY_MONITORING.3 Log Protection and Sanitising

Intent: how logs are kept trustworthy and free of what must not be in them.
1. Decision: Logs are protected at rest and in transit: encoded against log injection, protected from modification (an early copy made beyond reach of the writer, for example read-only media), access restricted and recorded, the origin of logs received from outside verified, and logs shipped to a logically separate system for analysis, detection and alerting. Where there is no central collector, logs are kept apart from application data at the least (a separate partition or a write-only account with very restrictive permissions). Passwords, tokens, keys, connection strings, payment data and session identifiers are never logged (a hash of the identifier where tracking is needed); personal data is not logged without need or legal justification (pseudonymisation of investigation logs is held in TRANSVERSE.PRIVACY.1); events arriving from clients are treated as untrusted input, validated and sanitized against CR, LF and delimiters, and encoded for the output format; logging follows the data's protection level. Outcome: logs cannot be altered by the party they record, cannot be used to attack the reader, and do not become a store of secrets.
2. Grounds: protection (L1145; REG-1079, REG-1089, REG-1090, REG-1093); separation (L1247; REG-1089); never-log list and sanitising (L1151; REG-1079, REG-1089, REG-1136); client events untrusted (L1254; REG-1089, REG-1090). L1151 and L1254 share the injection clause; it is stated once here.
3. Positions: P1 protect at rest and in transit. P2 keep apart from application data. P3 never log secrets and personal data. P4 client events untrusted.
4. Rejected: logs in the application's own store with application permissions: best never as protection. Separate partition or write-only account without a central collector: the minimum, best on a small single-host system.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST NOT log secrets or session identifiers; MUST sanitize client-supplied text before writing; MUST keep the log writer unable to modify what it has written.
Links: see TRANSVERSE.PRIVACY.1 (classification and pseudonymisation), TRANSVERSE.PRIVACY.2 (retention).

### TRANSVERSE.SECURITY_MONITORING.4 Detection and Escalation

Intent: how attacks are detected and escalated, and how long detection may take.
1. Decision: Logging without alerting and response is a failure: active attacks are detected and escalated in near real time, and the stopping of logging is itself detected. Time to detect is a managed figure with a target, because months of delay raise the damage; the figure is measured on the team's own exercises and incidents, not taken from a quoted average. Where the detection platform may change, detection rules are kept in a tool-neutral format so they survive a platform exit. Outcome: an attack is escalated while it is happening and the team knows how long it takes to see one.
2. Grounds: alerting is part of logging, gap noted that the leading standard does not verify alerting (L1146; REG-1079, REG-1089, REG-1090), which is why ASSURANCE.SECURITY.7 requires a known probe to raise an alert; dwell time is the cost to manage (L1147; REG-1082, REG-1093; about 200 days is a dated figure, open as a current value); tool-neutral rules (L1149; REG-1100; one T3 source, exit-risk argument inferred).
3. Positions: P1 alert and escalate in near real time. P2 time to detect as the managed cost. P3 tool-neutral rules (exit risk).
4. Rejected: tool-native rules only: best when the platform is a stable, deliberate dependency and the rule set is small (inferred). Logging with review after the fact only: best never.
5. Context: whether the detection platform may change (P3).
6. Certainty: grounded for P1; grounded as quoted for P2 (dated); inferred for P3.
7. Flags: none.
Constraints: MUST detect when logging stops; MUST be able to show a known probe raises an alert (ASSURANCE.SECURITY.7).
Links: Requires ASSURANCE.SECURITY.7; see OPERATION.ALERTING (escalation), OWNERSHIP.CONTAINMENT (exit from a tool).

### TRANSVERSE.SECURITY_MONITORING.5 Business Audit Trail

Intent: how the history of changes is kept for accountability and queries, apart from the security event log.
1. Decision: The security event log (who tried what, for detection) and the business audit trail (what changed, for accountability and queries) are two artifacts, designed apart because they differ in storage, integrity needs and retention. The audit record is written in the same transaction as the audited change, so both commit or roll back together; a high-value transaction has an audit trail with integrity controls against tampering or deletion (append-only storage) and tamper detection; entries carry the actual date and the record date. The history mechanism follows how tightly history is queried: an audit log by default, temporal properties or objects when integrated temporal queries are frequent. Outcome: every change to important data can be accounted for, and the account itself cannot be silently altered.
2. Grounds: the split (L1252; inferred, no source states it; REG-1089, REG-1090, REG-1142); tamper-resistant trail for high-value transactions (L1246; REG-1089, REG-1090); two dates (L1249; REG-1142); mechanism by query frequency (L1250; REG-1142); same transaction (L1251; REG-1090, REG-1140; grounded for the mechanism, inferred for the audit use, restated stack-neutral from a PostgreSQL origin), and the atomic audit declared in the store is already ASSURANCE.DATA_INTEGRITY.1.
3. Positions: P1 two artifacts. P2 integrity-controlled trail for high-value transactions. P3 two dates. P4a audit log, P4b temporal model. P5 same-transaction write.
4. Rejected: one log for both purposes: best never (conflicting retention and integrity). Temporal model as default: best when history is queried tightly and integrated with current data. Audit written after commit by a separate process: best never where the account must match the change.
5. Context: how tightly history is queried (L1250).
6. Certainty: inferred for the split; grounded for the rest, same-transaction audit grounded for the mechanism and inferred for the use.
7. Flags: none.
Constraints: MUST write the audit record in the transaction of the change; MUST give a high-value trail append-only integrity and tamper detection.
Links: see ASSURANCE.DATA_INTEGRITY.1 (atomic audit in the store), TRANSVERSE.PRIVACY.3 (deleting history follows the reason the data is kept).

---

## TRANSVERSE.PRIVACY Privacy and Retention

Intent: how personal data is minimised, classified, retained and erased.
Decision (rolled up): personal data is collected only for stated purposes, classified with safeguards per level, retained on a recorded schedule per purpose and deleted by mechanism, with an inventory of where copies live so that erasure can reach them; privacy is managed as a risk, assessed before high-risk processing and answered when a breach occurs. Outcome: the team holds only the personal data it needs, for as long as it needs it, and can show what happened when something goes wrong.
Certainty: inferred (roll-up; EU legal text restated neutral, regulated contexts deferred under MD-05).
Flags: none.
Links: Realizes ASSURANCE.SECURITY; see OPERATION.RECOVERY (backup retention).

### TRANSVERSE.PRIVACY.1 Minimisation, Classification and Design-In

Intent: how little personal data is collected and how what is held is classified and protected from the start.
1. Decision: Only the personal data necessary for each stated purpose is collected and processed, by default. Sensitive data, in its encoded forms too, is classified into protection levels with the safeguards documented per level (encryption, integrity, retention, logging, database security, privacy). Data protection is built into design and defaults with measures scaled to the state of the art, cost, and the nature, scope, context and risk of the processing. Where logs support investigation but not identification, identifiers are pseudonymised. Personal or sensitive data never goes into propagated trace context and trace identifiers are never seeded from user-identifiable data. Outcome: what is not collected cannot leak, and what is held has stated protection.
2. Grounds: minimisation (L1153; REG-1095; legal basis EU, practice stated neutral); pseudonymised investigation (L1152; REG-1093); classification (L1155; REG-1080); design and defaults scaled by risk (L1156; REG-1080, REG-1095); trace context (L1171; REG-122; restated neutral; how trace context is propagated is in OPERATION.TELEMETRY).
3. Positions: P1 minimisation. P2 pseudonymised logs. P3 classification with safeguards per level. P4 protection by design and default. P5 no personal data in trace context.
4. Rejected: none competes. Collect now, decide purpose later: best never.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST state the purpose for each personal data field collected; MUST NOT put personal data in trace context.
Links: see TRANSVERSE.SECURITY_MONITORING.3 (never-log list), TRANSVERSE.PRIVACY.2 (classification fixes the retention class), OPERATION.TELEMETRY.

### TRANSVERSE.PRIVACY.2 Retention Periods

Intent: how long data, logs included, is kept and how that period is decided and recorded.
1. Decision: Retention is a recorded decision per purpose and data class: long enough for the purpose, investigation included, and no longer than the legal, regulatory, contractual or purpose limit; deletion is automated by retention class and runs on schedule; the periods hold for personal data in backup copies too (OPERATION.RECOVERY.2 keeps a backup no longer than they allow). For logs that hold personal data, retain the legal minimum and delete; for logs that can be pseudonymised, where dwell time is long, retain longer and tier by age. Outcome: nothing is kept without a stated reason and nothing is deleted before its stated need.
2. Grounds: per purpose, delete on schedule, automate by class (L1154; REG-1080, REG-1095); recorded decision, two log positions with their conditions (L1150; REG-1089, REG-1093, REG-1095); neither source gives a number, both agree the period is recorded and bounded.
3. Positions: P1 legal minimum then delete (privacy, cost). P2 retain long, tier by age (investigation power). P3 per purpose with scheduled, automated deletion.
4. Rejected: P1 for logs that are pseudonymised and have long dwell time: P2 is best there. P2 for logs holding personal data: best never. Keep everything indefinitely: best never.
5. Context: whether logs hold personal data and how long dwell time is (L1150).
6. Certainty: grounded for the rule and conditions; open: no source gives a period.
7. Flags: none.
Constraints: MUST record the period and its reason per class; MUST automate deletion by class.
Links: see TRANSVERSE.PRIVACY.1, TRANSVERSE.PRIVACY.3, TRANSVERSE.CONFIG.4 (access-audit retention).

### TRANSVERSE.PRIVACY.3 Erasure and Deletion Mechanism

Intent: how data is actually deleted or put beyond use, in live systems, copies and backups.
1. Decision: Deletion is decided per entity from the reason the data is kept, and the choice is recorded: no need, hard delete; recovery or audit of deleted records, form per ASSURANCE.DATA_INTEGRITY.3; queryable past values, temporal model; time-bounded bulk expiry, drop or detach time partitions rather than bulk delete. The team keeps an inventory of where each personal data field has copies (caches, logs, derived stores, third parties, backups) and states for each class how an erasure request reaches it. Backups follow a retention schedule (OPERATION.RECOVERY.2). Erased data in a backup is put beyond use: no other use or access, no restore without re-applying every erasure recorded since the backup was taken (an erasure log kept outside the backup), deletion when the copy expires on schedule; a copy locked as immutable (OPERATION.RECOVERY.3) is handled the same way, the lock's expiry being its schedule. The data subject is told what happens to the backup. Outcome: an erasure request has a defined path to every copy, and deletion is by a mechanism chosen for the reason, not by habit.
2. Grounds: per entity from the reason (L1258; REG-1137, REG-1138, REG-1142, REG-1145; inferred synthesis, consistent with ASSURANCE.DATA_INTEGRITY.3 which prefers delete plus same-transaction archive over a flag); partition drop (L1257; REG-1137; restated neutral); copies are an open decision (L1157; REG-1095); backups beyond use (L1114; REG-1069; ICO, one regulator; the erasure log is inferred), text held here for the backup rule (cross-unit X8; ASSURANCE.DATA_INTEGRITY.3, OPERATION.RECOVERY.3 and EVOLUTION.DECOMMISSION.6 point here).
3. Positions: P1 decide per reason. P2 partition drop for time-bounded data. P3 erasure reaches copies (open, contested). P4 backups beyond use until the copy expires on schedule.
4. Rejected: the form for recovery and audit cases is decided in ASSURANCE.DATA_INTEGRITY.3, not here. Bulk DELETE of time-bounded data: best on small tables where partitioning costs more than it saves (inferred). Treating erasure as complete after the live system: best never.
5. Context: none beyond the reasons of P1.
6. Certainty: inferred for P1; grounded for P2 on mechanism and for P4 on one regulator (ICO); the erasure log and the handling of a locked backup (expiry of the lock as its schedule) are inferred; open: whether erasure must reach logs and every copy on request (contested; no source read settles it).
7. Flags: none.
Constraints: MUST record the deletion choice per entity; MUST tell the data subject what happens to backups; MUST keep a legally required purge possible (ASSURANCE.DATA_INTEGRITY.3).
Links: see TRANSVERSE.PRIVACY.2, OPERATION.RECOVERY, CHANGE_FLOW.DATA_CHANGE (batching a bulk change), TRANSVERSE.SECURITY_MONITORING.5.

### TRANSVERSE.PRIVACY.4 Privacy Risk, Impact Assessment and Breach

Intent: how privacy is managed as a risk, assessed before high-risk processing and answered when a breach occurs.
1. Decision: Privacy is managed as a risk through a framework, not as compliance alone. A privacy impact assessment is run before high-risk processing, covering the processing and its purposes, necessity and proportionality, risks to individuals and mitigating measures. The team can determine within a short stated clock what a breach touched, and records every breach with facts, effects and remedial action (EU reference: notification to the authority within 72 hours where feasible). Outcome: high-risk processing is examined before it starts, and a breach can be bounded and accounted for.
2. Grounds: risk framework (L1161; REG-1096; grounded as to purpose, open as to detail); assessment (L1158; REG-1095; EU text, inferred as neutral practice); breach determination and record (L1159; REG-1095; link to logging and classification inferred).
3. Positions: P1 privacy as risk through a framework. P2 impact assessment before high-risk processing. P3 breach determination and record within a clock.
4. Rejected: compliance-only: best never as a substitute for risk management; sufficient where only a legal minimum is demanded and the processing is low risk.
5. Context: whether regulation applies (L1158); legal obligations themselves are out of scope (MD-05).
6. Certainty: grounded as to purpose; inferred for the neutral restatement and for the link to logging and classification; open: framework body not read.
7. Flags: none.
Constraints: MUST assess before high-risk processing starts; MUST record every breach.
Links: see TRANSVERSE.SECURITY_MONITORING.2 and TRANSVERSE.PRIVACY.1 (the data to answer a breach), OPERATION.INCIDENTS.

---

## TRANSVERSE.CONFIG Configuration and Secrets

Intent: how configuration and secrets reach the running software and are kept apart from code.
Decision (rolled up): configuration and secrets stay out of the code and the artifact; secrets sit in central custody with least privilege, short lifetime and an audit of every access, and reach the process by a channel chosen for their criticality; pipelines and automation hold short-lived federated credentials; an exposed secret is treated as compromised. Outcome: the same artifact runs in every environment, and a leaked repository or log does not expose a working credential.
Certainty: inferred (roll-up).
Flags: none.
Links: Realizes ASSURANCE.SECURITY (secret scanning, ASSURANCE.SECURITY.5, is held there); see CHANGE_FLOW.BUILD.

### TRANSVERSE.CONFIG.1 Separation of Configuration from Code and Secrets

Intent: what stays out of the codebase and the package, and what stays apart from plain configuration.
1. Decision: Configuration is kept strictly separate from code and from the deployable package: configuration varies across deployments and code does not, and the test is that the codebase could be open-sourced at any moment without exposing a credential. Secrets are never hardcoded in source or committed configuration, and are kept apart from non-secret configuration; confidential data is not held in a plain configuration object. Configuration expressed as code lives in a repository with least-privilege access and tracked, attributable changes, as source does; secrets stay out of it. Outcome: no credential is recoverable from the source, history or artifact, and configuration changes are attributable.
2. Grounds: separation and open-source test (L158 and L1192, the same normative thing kept apart by the ledger; REG-092, REG-166, REG-167, REG-174, REG-082, REG-1109); secrets apart from configuration (L256; REG-173, REG-174); configuration as code (L261; REG-004, REG-167); secrets clause of L1535 (REG-166, REG-1551, REG-1552, REG-1553, judged in the JavaScript guideline; its first clause is L158; the prior verdict is one position, here re-examined and confirmed for the two grounded constraints). The second half of L1535 (token acceptance) is held in CONSTRUCTION.BOUNDARY.2 (cross-unit X9).
3. Positions: P1 strict separation (L158, L1192). P2 secrets apart from configuration. P3 configuration as code with least-privilege access. P4 L1535: no hardcoded secrets, secrets only through audited mechanisms (the token-acceptance half is held in CONSTRUCTION.BOUNDARY.2).
4. Rejected: configuration baked into the artifact per environment: best never (the artifact would differ from what was reviewed). Secrets in a private repository: best never (a private repository is not custody).
5. Context: none.
6. Certainty: grounded for the separation, the secrets rules and the first clause of P4 (L1535); open for the clause "drawn, compared, stored and logged only through audited platform mechanisms", which no claim grounds except in part: audit of every access is held in CONFIG.4 (L1239) and the never-log rule in SECURITY_MONITORING.3.
7. Flags: none.
Constraints: MUST NOT commit a secret to source or configuration; MUST keep one build for every environment.
Links: Requires CHANGE_FLOW.INTEGRATION (repository access and tracked changes); see ASSURANCE.SECURITY.5 (scanning), TRANSVERSE.CONFIG.4, CONSTRUCTION.BOUNDARY.2 (token acceptance).

### TRANSVERSE.CONFIG.2 Delivery Channel to the Running Software

Intent: how configuration and secrets reach the running process, and why that channel was chosen.
1. Decision: Non-secret configuration is versioned and reviewed (CONFIG.1) and applied at deploy as environment values or files, so the artifact is the same in every environment. Secrets live in a managed store (CONFIG.4) and reach the process by runtime injection as mounted files or through the store API; an environment variable is used only where the platform offers neither, or where the process environment is shown not to leak (no child process inherits it, no diagnostics or dumps include it) and a restart suffices to rotate. The channel and the reason are recorded. Outcome: a secret reaches the process without entering the artifact, and its channel is as strong as its criticality.
2. Grounds: environment variables are universal, simple, portable, not committed by accident (L254, L1238, L1193; REG-166, REG-167, REG-173, REG-174, REG-082, REG-1109); files or store API allow subscription to change, OWASP is cautious about environment variables (L254, L1238; REG-166, REG-173, REG-174; process-listing and child-process leak vectors inferred, not read); reviewed versioned non-secret configuration promoted with the release (L1193; REG-082, REG-1109; the reconciliation is inferred by the ledger).
3. Positions: P1 environment variables (portability, simplicity). P2 mounted files or store API (security, rotation, audit). P3 non-secret configuration in source control with strict review, packaged with binaries, or in an external store for dynamic values.
4. Rejected: P1 "environment variables as the default channel for secrets": they are "generally accessible to all processes and may be included in logs or system dumps" (REG-166, OWASP, fetched in review); best only under the condition above. P3 "configuration packaged per environment with the binary": best never (the artifact would differ per environment); non-secret configuration of every environment packaged with the binary and selected at deploy: best where it must change and roll back atomically with the code that reads it (L1193; condition inferred), the artifact staying one.
5. Context: criticality of the secret and platform and team size (L254, L1238).
6. Certainty: grounded for the positions; inferred for the leak vectors and for the separation of custody from channel.
7. Flags: none.
Constraints: MUST record the channel and its reason; MUST NOT deliver a secret inside the artifact.
Links: see TRANSVERSE.CONFIG.1, TRANSVERSE.CONFIG.4; Realized by OPERATION and CHANGE_FLOW.DEPLOY.

### TRANSVERSE.CONFIG.3 Shape of Per-Environment Configuration

Intent: how configuration differs from one deployment to the next.
1. Decision: Per-environment configuration is a set of independent granular values. With many deployments (previews, per tenants) each deployment takes its own values; with a few fixed environments a named environment may be kept as one reviewed file of those values, so that the whole of it is read in one place. Code never branches on an environment name. Outcome: adding a deployment does not multiply configuration, and a fixed environment remains reviewable.
2. Grounds: independent values scale with deployments (L255; REG-167, REG-174, Twelve-Factor); named bundles reviewable in one place, the source calls it the traditional approach, argument inferred (L255); the no-branching constraint is inferred from the combinatorial harm of bundles.
3. Positions: P1 granular values (scalability, cost). P2 named bundles (reviewability, control).
4. Rejected: P1 alone for a handful of fixed environments: P2 is best there. P2 for many deployments: best never (combinatorial growth).
5. Context: number of deployments (L255).
6. Certainty: grounded for P1; inferred for the argument for P2 and for the no-branching rule.
7. Flags: none.
Constraints: MUST NOT branch application code on environment name.
Links: none.

### TRANSVERSE.CONFIG.4 Central Secret Custody and Lifecycle

Intent: where secrets are stored and how access and lifecycle are controlled.
1. Decision: Secrets are centralized and standardized in one managed secrets solution, with fine-grained least-privilege access per service and automated handling of creation, rotation, revocation and expiry; short-lived dynamic secrets are preferred (CONFIG.5); every access is audited, the logs queryable for a recorded period (one source: at least 90 days, with longer cold storage) set under TRANSVERSE.PRIVACY.2; a platform default store is hardened, not trusted as is. Outcome: one place answers who holds which secret, who read it and when it expires.
2. Grounds: L257 (REG-166, REG-173) and L1239 (REG-166), the same normative thing kept apart by the ledger; stated once here. The 90 days queryable with longer cold storage is one source's figure (CI/CD tooling context); the period itself falls under the retention decision of PRIVACY.2, where no source gives a number.
3. Positions: P1 central managed solution with lifecycle (L257). P2 central, per-service least privilege, dynamic secrets, audited access (L1239).
4. Rejected: secrets per application or per team in ad hoc stores: best never at scale; best on a single small service, where the platform's own store is the managed store.
5. Context: none.
6. Certainty: grounded (one family of sources, consensus).
7. Flags: none.
Constraints: MUST audit every access; MUST NOT share one credential across services.
Links: see TRANSVERSE.SECURITY_MONITORING.2 (access audit entries), TRANSVERSE.PRIVACY.2.

### TRANSVERSE.CONFIG.5 Credential Lifetime and Pipeline Identity

Intent: how long credentials live and how pipelines and automation authenticate.
1. Decision: Credentials are short-lived and issued dynamically with a time to live and automatic revocation where the platform supports it; static secrets rotated on a schedule are acceptable for few services of low criticality or where dynamic issue is unavailable. Every non-human identity (CI and deployment workflows, automated authors) authenticates with federated short-lived tokens (OIDC) rather than long-lived credentials stored in the pipeline, holds only the permissions its job needs, is scoped per environment, and is kept out of the environment that executes generated or untrusted code; no secret appears in pipeline output; the CI/CD system is treated as production. Outcome: a leaked credential expires by itself, and a compromised pipeline reaches only its own scope.
2. Grounds: short-lived dynamic credentials, blast radius contained by revoking a lease prefix (L258; REG-166, REG-175; the merit of static secrets inferred); federated tokens, least permissions (L259; REG-176, REG-177); CI/CD as production (L1240; REG-025, REG-166); automation credentials (L1069; REG-1037). The limit on what automation may do is stated once, in ASSURANCE.SECURITY.6.
3. Positions: P1 dynamic short-lived (security, blast radius). P2 static rotated (cost, load). P3 OIDC federation. P4 narrowly scoped automation credentials outside the code-executing environment. P5 CI/CD as production.
4. Rejected: P1 where the platform cannot issue dynamic credentials or services are few and low criticality: P2 is best. Long-lived credentials duplicated into the CI system: best never.
5. Context: number of services and criticality; platform support (L258).
6. Certainty: grounded; static secrets' merit inferred.
7. Flags: none.
Constraints: MUST NOT store a long-lived cloud credential in the CI system where federation is available; MUST scope credentials per environment.
Links: see TRANSVERSE.CONFIG.4, CHANGE_FLOW.BUILD, ASSURANCE.SECURITY.6.

### TRANSVERSE.CONFIG.6 Response to a Leaked Secret

Intent: what is done when a secret is found exposed.
1. Decision: A secret found in code, history or logs is treated as compromised: it is revoked at once, rotated through an automated process, removed from the exposed locations, and the audit logs are used to investigate what it was used for between exposure and revocation. Revocation does not wait for cleanup of the exposed copy. Outcome: the window in which an exposed credential works is as short as the revocation path.
2. Grounds: L252 (REG-166), single source, no counter-position found; investigation use of audit logs follows the stated purpose of keeping them; ASSURANCE.SECURITY.5 states that a secret found in history is rotated.
3. Positions: P1 treat as compromised, revoke, rotate, remove, keep audit logs.
4. Rejected: cleaning the history and keeping the secret: best never.
5. Context: none.
6. Certainty: grounded (single source).
7. Flags: none.
Constraints: MUST revoke before cleaning; MUST be able to rotate without manual steps.
Links: see TRANSVERSE.CONFIG.4, TRANSVERSE.SECURITY.5, ASSURANCE.SECURITY.5, OWNERSHIP.LIFECYCLE.3 (supply-chain trigger; rotation is held here).

---

## TRANSVERSE.ENVIRONMENTS Development Environments

Intent: how development, build and test environments are defined, separated and hardened.
Decision (rolled up): environments are separated from production in instance and credentials while matching it in kind and version; the development environment is itself versioned code, defined by the cheapest mechanism that gives the reproducibility needed; development endpoints and the toolchain are hardened as an attack surface. Outcome: a developer or a build cannot reach production by accident, and every machine builds the same way.
Certainty: inferred (roll-up).
Flags: none.
Links: see CHANGE_FLOW.DEPLOY (environment parity), ASSURANCE.BEHAVIOUR.

### TRANSVERSE.ENVIRONMENTS.1 Separation and Isolation

Intent: how far environments are kept apart and what each may reach.
1. Decision: Development, build, test and production are separated and protected from each other; production and development secrets are isolated; non-production minimizes use of production services; human access to build services is minimized and audited. Parity with production is of kind and version, isolation is of instance and credentials. Outcome: an action in a lower environment cannot affect production and a lower environment cannot read a production secret.
2. Grounds: L260 (REG-004, REG-103, REG-166); the parity-versus-isolation synthesis is inferred by the ledger.
3. Positions: P1 separation and isolation with minimal human access.
4. Rejected: shared credentials or instances for convenience: best never.
5. Context: none. Scope note: production data in lower environments is outside the rows.
6. Certainty: grounded; the parity reconciliation inferred.
7. Flags: none.
Constraints: MUST NOT share a credential across environments.
Links: tension with environment parity resolved as above; see CHANGE_FLOW.DEPLOY.

### TRANSVERSE.ENVIRONMENTS.2 Definition Mechanism

Intent: how the development environment is itself defined as versioned code.
1. Decision: The development environment is defined as versioned code and is reproducible by anyone, on a clean machine, from that definition, so that toolchain versions match across machines (and CI where the mechanism allows). The mechanism is the cheapest that gives the reproducibility needed: dependency manifests with language-level isolation for a single-language project with no native dependencies; a container definition (Dev Container) for mixed-skill teams, cloud IDEs and native dependencies; a pinned package set (Nix) where byte-level control of package versions across machines and CI is required and the team accepts the learning cost. Outcome: a new machine builds and runs the project the same way as every other.
2. Grounds: three mechanisms, each with its winning condition (L262; REG-014, REG-168, REG-178); the ordering by cost is inferred from the stated costs (comparative costs inferred by the ledger; limits of the Nix pin on host OS and kernel not stated).
3. Positions: P1 container definition (onboarding speed, load). P2 pinned package set (reproducibility, control). P3 manifests only (lowest cost; system tools vendored).
4. Rejected: P3 with native dependencies or mixed languages: best only for single-language projects with no native dependencies. P2 for a team without the need for byte-level control: best when reproducibility is that strict. P1 as universal: best for mixed-skill teams and cloud IDEs.
5. Context: team skill mix and project languages (L262).
6. Certainty: grounded for the features; inferred for the comparative costs and the ladder.
7. Flags: none.
Constraints: MUST keep the definition in version control; MUST be able to rebuild from a clean machine.
Links: see OWNERSHIP.LIFECYCLE (pinning), CHANGE_FLOW.BUILD.

### TRANSVERSE.ENVIRONMENTS.3 Toolchain Control and Hardening

Intent: how development endpoints are kept trustworthy; pinning and changing the build tools is in OWNERSHIP.LIFECYCLE.
1. Decision: Development endpoints and the toolchain are an attack surface: hardened to an approved hardening guide, with least functionality and least privilege, and monitored continuously for posture. Outcome: a compromised developer endpoint or tool does not become a path into the build or production.
2. Grounds: L264 (REG-004); single source, no counter-position found.
3. Positions: P1 harden and monitor.
4. Rejected: treating developer machines as trusted by default: best never.
5. Context: none.
6. Certainty: grounded (single source).
7. Flags: none.
Constraints: MUST apply least functionality and least privilege on development endpoints.
Links: see OWNERSHIP.LIFECYCLE, CHANGE_FLOW.BUILD, ASSURANCE.ARTIFACT.

## Review applied

- F01 applied: time to detect now points to TRANSVERSE.SECURITY_MONITORING.4; ASSURANCE.SECURITY.7 kept only for "effectiveness is itself tested"; defects per stage and closed findings marked inferred.
- F02 applied: SECURITY.6 positions restated (P1 policy content, P2 policy without bounty as the default, P3 bounty, P4 penetration test alone); invented P2 rejection and proviso dropped.
- F03 applied: DOCS.3 grounds no longer cite dated verification in a header.
- F04 applied: DOCS.4 reason against commit-generated lists grounded in REG-162; T2 narrowed to the condition under which P2 would be best.
- F05 applied: SECURITY_MONITORING.3 keeps the never-log list; pseudonymisation points to TRANSVERSE.PRIVACY.1.
- F06 applied: PRIVACY.3 keeps only temporal model and partition drop; recovery and audit form points to ASSURANCE.DATA_INTEGRITY.3.
- F07 applied: CONFIG.4 audit-log period reworded (one source, queryable 90 days plus cold storage), set under PRIVACY.2.
- F08 applied: DOCS.1 constraint on generated output removed, pointer to ASSURANCE.DOCS_SYNC.3 added.
- F09 applied: "and in what time" removed from PRIVACY.3.
- F10 applied: ENVIRONMENTS.1 "not decided" sentence removed; scope note added.
- Flags T1, T5, T6, T7, T8, F11, F12, F13 not acted on (final Opus pass).

## Final pass applied

Resolutions (final_pass/resolutions.md, J9):
- T1 applied: DOCS.3 settled unchanged; grounds extended with the one-origin and L133 argument, the honoured maintainer condition and the deployed-definition case (inferred); T1 flag removed.
- T2, T3, T4 applied: review closed them, confirmed; their flag lines removed from DOCS.4, SECURITY.2, SECURITY.6 and the roll-ups; the open certainty items stay in Certainty (generated-changelog condition, maturity effect, bounty yield).
- T5 applied: SECURITY_MONITORING.1 certainty raised to grounded (OWASP Logging Cheat Sheet; ASSURANCE.SECURITY.1); flag removed.
- T6 applied (cross-unit X8): PRIVACY.3 backup text replaced by the erasure-in-backups text; flag removed. The sentence telling the data subject what happens to the backup is kept as its own sentence, since X8 text does not remove it and its constraint stands.
- T7 applied (cross-unit X9): the token-acceptance clause removed from CONFIG.1 (constraint, P4, flag); see-link added.
- T8 applied: CONFIG.2 second sentence replaced; rejected P1 and P3 replaced as stated; the earlier rejection "P2 for a small service on a platform that injects from a managed store: P1 channel is best" dropped because the new decision supersedes it; flag removed.
- F11 applied: DOCS.5 certainty and flags line as stated.
- F12 applied: ENVIRONMENTS.2 unchanged (certainty stays inferred).
- F13 applied: SECURITY.1 decision and grounds as stated.

Cross-unit lines naming J9:
- X8 applied: PRIVACY.2 gains "backup copies included" (periods hold for backups, pointer to OPERATION.RECOVERY.2); PRIVACY.3 holds the erasure text. The pointing records (J3, J7, J8) are not in this unit; not edited here.
- X9 applied: the receiving text in CONSTRUCTION.BOUNDARY.2 belongs to J5; here only CONFIG.1 drops it and points. The text itself is not copied here.
- X10 applied: CONFIG.6 already holds revocation, rotation and investigation; no text change needed; link to OWNERSHIP.LIFECYCLE.3 added there. The J1 side is not edited here.

Nodes added: none. Flags still open: none (open certainty items remain at PRIVACY.3, DOCS.4, SECURITY.2, SECURITY.6, CONFIG.1).
