# Branch EVOLUTION: tree to level 3, rows attached, positions without verdict

Cut top-down from the L2 intents of `../../tree_l2.md`, then the 53 routed rows were attached, each to one node. Cut on `../../../target_hierarchy.md` and `../../../maintainer_decisions.md` (MD-01 best practice per node, MD-02 no default team, MD-03 one location per fact, MD-04 EVOLUTION is a top-level branch). This file states no verdict and ranks nothing; judges decide node by node. `check_branch.py` proves coverage.

## Tree

```text
EVOLUTION  Evolution
  EVOLUTION.DECISIONS  Decision Records
    EVOLUTION.DECISIONS.1  Content of a Record
    EVOLUTION.DECISIONS.2  Significance Threshold
    EVOLUTION.DECISIONS.3  Form and Storage
    EVOLUTION.DECISIONS.4  Changing an Accepted Record
    EVOLUTION.DECISIONS.5  Status, Ownership and Use in Review
    EVOLUTION.DECISIONS.6  Proposal Versus Record
  EVOLUTION.INCREMENTAL  Incremental Change
    EVOLUTION.INCREMENTAL.1  Step Size and Feedback
    EVOLUTION.INCREMENTAL.2  Expand, Migrate, Contract
    EVOLUTION.INCREMENTAL.3  Replacement Versus Rewrite
    EVOLUTION.INCREMENTAL.4  Mass Change and Migration Ownership
    EVOLUTION.INCREMENTAL.5  Lifespan, Consumers and Cost of Change
    EVOLUTION.INCREMENTAL.6  Conventions Applied Forward Only
  EVOLUTION.DEBT  Technical Debt and Refactoring
    EVOLUTION.DEBT.1  What Counts as Debt
    EVOLUTION.DEBT.2  Taking Debt Versus Investing in Quality
    EVOLUTION.DEBT.3  Finding and Inventorying Debt
    EVOLUTION.DEBT.4  Refactoring Step Size
    EVOLUTION.DEBT.5  Timing and Responsibility of Repayment
  EVOLUTION.DECOMMISSION  Decommissioning
    EVOLUTION.DECOMMISSION.1  Why Remove
    EVOLUTION.DECOMMISSION.2  Grounds to Retire
    EVOLUTION.DECOMMISSION.3  Announcing Retirement
    EVOLUTION.DECOMMISSION.4  Support Window Before Removal
    EVOLUTION.DECOMMISSION.5  Advisory or Compulsory Deprecation
    EVOLUTION.DECOMMISSION.6  Carrying Out the Retirement
  EVOLUTION.TECHNOLOGY  Keeping Technologies Few
    EVOLUTION.TECHNOLOGY.1  Adding as Replacing
    EVOLUTION.TECHNOLOGY.2  Standing Position per Technology
    EVOLUTION.TECHNOLOGY.3  How Firmly the Stack Is Held
    EVOLUTION.TECHNOLOGY.4  One General-Purpose Store for Several Roles
```

## How to read

- Record: uid, name, intent (what and why), rows, positions, context variables, links, stack pointers. Positions: `P1, P2...` are the competing practices the rows record, each with its strongest argument, the force it serves, the condition under which it would be the best (where the row gives one), and row and source ids. Nothing is marked as winning.
- "Single practice recorded" means the rows hold one practice and name no competitor; no competitor was invented.
- `Rows: -` on an L2 node means it is a roll-up of its children. No EVOLUTION node is an index node (no split topic in `tree_l2.md` lists one).
- Source ids are the REG ids of the rows. MAINT rows (L296, L324; source REG-181, the maintainer's codified practice, not citable) appear as a named position.
- Link types: `Realizes` (to a decision node of OWNERSHIP or ASSURANCE named by a row's "see also"), `See` (to a realization node, or an in-branch pair), `Conflicts` (where a row says possible tension). All inferred from the rows' see-also fields, not from the sources.
- Rows tagged with a stack: L1030 (HTTP header fields; the two-stage principle is neutral), L1032 and L1031 (the machine forms and numbers are Kubernetes and HTTP specific). Given as stack pointers on their node.

## Routing objections

Three were raised; each is resolved in `../../objections/resolution.md` and all three are kept where `routing.md` put them (listed with the reason).

- L1236 -> OWNERSHIP.STANCE : "build to learn" has L1208 (same origin cluster, near claim) there; kept in INCREMENTAL.1: its subject is step size and feedback, and L1208 is itself kept in OWNERSHIP.STANCE.4 with the build-or-not question.
- L1231 -> OPERATION.RELIABILITY : states simplicity as a reliability property; kept in DEBT.2 for the delete-code part: OPERATION.RELIABILITY holds indicators, objectives and the error budget, no node on simplicity.
- L1007 -> CHANGE_FLOW.REVIEW : consulting records during review is a review practice (L137, L140 related); kept in DECISIONS.5, whose intent names use in review, so the record's use sits with its status and ownership.

## Records

#### EVOLUTION Evolution

Intent: How the system and its decisions change over time, so that it keeps working and stays changeable at a cost the team can sustain: records, incremental change, debt, removal, few technologies.
Rows: -

#### EVOLUTION.DECISIONS Decision Records

Intent: How decisions and their reasons are recorded, kept and revisited, so that the motivation of past decisions is recoverable.
Rows: -

#### EVOLUTION.DECISIONS.1 Content of a Record

Intent: What a decision record must state so that a later reader can recover the reason and does not reopen the decision blindly.
Rows: L1001, L1002, L1009, L1233, L324
Positions (no verdict):
- P1 Record the reasons: forces, decision, consequences. Strongest argument: the motivation of past decisions is among the hardest things to recover, and without it a team obeys outdated decisions or reverses them blindly. Force: confidence, reversibility. Best when: no condition stated; consensus (L1001; REG-1011, REG-1012, REG-154).
- P2 Add serious alternatives with pros and cons, the confidence, and why rejected ones were rejected including dissent. Strongest argument: the same discussion is not reopened without new information; writing it clarifies group thinking. Force: confidence, team cognitive load (L1002; REG-1011, REG-1013, REG-1019, REG-1020, REG-1114).
- P3 A fixed template: title, context (forces, value-neutral), decision ("We will..."), status, consequences (positive, negative, neutral). Strongest argument: a common structure all records share. Force: cognitive load (L1233; REG-154).
- P4 Name the forces (technical, political, social, project-local) so that a change in them is visible and signals when to revisit. Strongest argument: the revisit trigger becomes explicit. Force: reversibility. Certainty in the row: inferred (L1009; REG-1019, REG-154).
- P5 Maintainer's codified practice (MAINT-S01): the record states the costs it accepts as the other half of the decision, so a strong reason has something concrete to outweigh. Strongest argument: costs stated give a counterweight. Force: confidence. Row reading: agrees with common practice (L324; REG-181).
Context variables: -
Links: Realizes OWNERSHIP.SELECTION (L1001, L1002, L1009 see also L029, related)

#### EVOLUTION.DECISIONS.2 Significance Threshold

Intent: Which decisions get their own record, so that records stay worth reading and writing.
Rows: L1004
Positions (no verdict):
- P1 Record every architecturally significant decision (structure, non-functional requirements, dependencies, interfaces, construction techniques), as short records. Strongest argument: later confidence and onboarding. Force: confidence; costs authoring time. Best when: many contributors or long life (L1004 a; REG-1011, REG-1114, REG-154, REG-163).
- P2 Record only when there is no existing basis for the decision or several options were weighed. Strongest argument: low overhead. Force: cost of ownership. Best when: small team and standards exist (L1004 b; REG-1012).
- P3 Skip workarounds and experiments (also limited-scope, temporary or already-policy decisions) (L1004 c; REG-1028, T4).
Context variables: CONTRIBUTORS_AND_LIFETIME (L1004: P1 "wins when many contributors or long life", P2 "when the team is small and standards exist")
Links: Realizes OWNERSHIP.SELECTION (L1004 see also L029, related)

#### EVOLUTION.DECISIONS.3 Form and Storage

Intent: How a record is shaped and where it lives, so that it is read, found and kept beside what it governs.
Rows: L1003
Positions (no verdict):
- P1 Short (one or two pages), one decision per record, numbered monotonically without reuse, lightweight text markup written as prose to a future reader, stored in version control in the source repository beside the code; mirrored to a wiki only for wider reach. Strongest argument: the record travels with the code and has history. Force: cognitive load, cost of ownership. Consensus; no competing practice recorded (L1003; REG-1012, REG-1013, REG-1024, REG-1028, REG-1114, REG-154).
Context variables: -

#### EVOLUTION.DECISIONS.4 Changing an Accepted Record

Intent: What happens to a record when the decision changes, so that history stays honest and the current picture stays accurate.
Rows: L232, L1005
Positions (no verdict):
- P1 Immutable log with supersession: a changed decision is a new record that supersedes the old one, which stays marked superseded. Strongest argument: history is never wrong, only superseded; honest audit. Force: audit, confidence. Best when: many readers rely on the record, or regulated review; for rationale documents (L232 a, L1005 a; REG-154, REG-163, REG-1011).
- P2 Mutable living document, with dated additions, kept current by CI and ownership. Strongest argument: an accurate current picture and less authoring friction ("immutability is ideal; in practice mutability has worked better for our teams", T4). Force: accuracy of current picture, cost of ownership. Best when: the record is the only place readers look and a few people own it; for how-to and reference documents (L232 b, L1005 b; REG-1028, REG-1012).
- Row note (inferred): in version control history survives edits, which narrows the cost of P2; P1 still keeps the status machine-readable (L1005). Two models, to be assigned per document type (L232). Agreement recorded: majority (L232), contested (L1005 EVOL-C05), consensus (L1005 WEB:ARCH-C38).
Context variables: DOCUMENT_TYPE (L232: "two models, to be assigned per document type": immutable for rationale, living for how-to and reference)
Links: See EVOLUTION.DECOMMISSION.2 (L1037 see also L232)

#### EVOLUTION.DECISIONS.5 Status, Ownership and Use in Review

Intent: How a record is owned, reviewed and used after it is written, so that accepted decisions are actually applied.
Rows: L1006, L1007
Positions (no verdict):
- P1 Give each record a status (proposed, accepted, rejected, superseded, deprecated), a named owner, and a review before acceptance. Force: confidence, accountability. Consensus; single practice recorded (L1006; REG-1011, REG-1013, REG-154).
- P2 Consult accepted records during code and design review; a reviewer who finds a change violating a record links it. Force: confidence. Consensus from a single source, no dissent found (L1007; REG-1011).
Context variables: -
Links: See CHANGE_FLOW.REVIEW (L1007 see also L137, related)

#### EVOLUTION.DECISIONS.6 Proposal Versus Record

Intent: Whether a decision on a change with many stakeholders is prepared in a separate proposal or in the record itself.
Rows: L1008
Positions (no verdict):
- P1 Separate the proposal (written before the decision: drawbacks, alternatives, unresolved questions, backward-compatibility section, a named decider) from the record (outcome and reason). Strongest argument: the deliberation and the outcome serve different readers. Force: confidence, speed. Best when: changes with many stakeholders (L1008; REG-1012, REG-1013, REG-1020).
- P2 One document serves both roles, as PEPs do. Strongest argument: fewer artifacts, history in version control. Force: cognitive load. Best when: open projects with many contributors (L1008 a; REG-1013).
- P3 A lightweight record only. Strongest argument: lowest overhead. Force: speed, cognitive load. Best when: small teams (L1008 b; REG-154, REG-1012).
Row certainty: inferred (the split is the origin's synthesis from two open-source projects).
Context variables: STAKEHOLDER_COUNT (L1008: P3 "wins for small teams", P2 "in open projects with many contributors")

#### EVOLUTION.INCREMENTAL Incremental Change

Intent: How change is made in steps that keep the system working, including migrations and replacement.
Rows: -

#### EVOLUTION.INCREMENTAL.1 Step Size and Feedback

Intent: How large a step may be, so that the system stays releasable and learning arrives early.
Rows: L1010, L1236
Positions (no verdict):
- P1 Change in steps that keep the system releasable at every step (an interface supporting both versions, an abstraction with two suppliers) rather than on a long-lived branch or in one switch-over. Force: delivery continuity, reversibility. Consensus; no competitor named beyond the long-lived branch and the one switch-over (L1010; REG-1004, REG-105).
- P2 Short feedback beats up-front analysis: only about a third of presumed features improved their target metrics, so build to learn. Force: delivery speed, evidence of value. Majority (L1236; REG-034).
Context variables: -
Links: See CHANGE_FLOW.INTEGRATION (L1010 see also L129, L128); See CHANGE_FLOW.ROLLBACK (L1010 see also L163); Realizes OWNERSHIP.STANCE (L1236 see also L1208, near claim)

#### EVOLUTION.INCREMENTAL.2 Expand, Migrate, Contract

Intent: How an incompatible interface or schema change is run, so that both versions are supported only as long as needed.
Rows: L1011, L1012
Positions (no verdict):
- P1 Expand, migrate, contract: support old and new together (for a schema, deploy one supporting both application versions, verify, then deploy the application), move consumers, then remove the old form; the contract step is part of the change. Strongest argument: supporting two versions is a recurring cost that only ends at removal, and expand-first keeps rollback possible. Force: reversibility, cost of ownership. Consensus (L1011; REG-087, REG-1004, REG-105, REG-244).
- P2 A migration without its removal step is debt in its own right; track it until the old form is gone. Force: cost of ownership. Row certainty: inferred (L1012; REG-1030, REG-105).
Context variables: -
Links: See CHANGE_FLOW.DATA_CHANGE (L1011 see also L383, L384, L382; L1012 see also L384, L383); See CHANGE_FLOW.ROLLBACK (L1011 see also L163); See EVOLUTION.DEBT.1 (L1012 states the debt framing)

#### EVOLUTION.INCREMENTAL.3 Replacement Versus Rewrite

Intent: Whether an adopted, home-grown or whole system is replaced piece by piece or all at once.
Rows: L039, L1017
Positions (no verdict):
- P1 Never rewrite; refactor in place. Strongest argument: delivery continuity and preserved hidden knowledge. Force: delivery continuity. Best when: the system is shipping and its behaviour is poorly specified (L1017 a; REG-1021, T3).
- P2 Rewrite when changing the old code costs more than new (rule of thumb "25 percent", unverified). Strongest argument: ability to change and removal of dead platforms. Force: cost of ownership, reversibility. Best when: the platform is obsolete and the old system keeps running in parallel (L1017 b; REG-1029, T4).
- P3 Replace incrementally while it keeps running, at seams and behind the existing interface (strangler fig); a full rewrite only under stated conditions with parallel running and slow migration. Strongest argument: serves both continuity and replacement. Force: reversibility, delivery speed; cost: two systems in the interim. Best when: behaviour is poorly specified and users cannot wait (L039, L1017 c; REG-033, REG-1004).
- P4 Big-bang wholesale rewrite: no source argued for it in these rows; open (L039).
Row certainty: positions grounded; open whether any wins in general (L1017). Agreement recorded: majority (L039), contested (L1017 EVOL-C17), consensus (L1017 WEB:ARCH-C42).
Context variables: -
Links: See OWNERSHIP.STANCE (L1017 see also L038; L039 routing note); See EVOLUTION.INCREMENTAL.1 (L1017 near claim L1010)

#### EVOLUTION.INCREMENTAL.4 Mass Change and Migration Ownership

Intent: How a change across many owners is split, owned and finished, so that it completes instead of stalling.
Rows: L1013, L1014
Positions (no verdict):
- P1 Generate mechanical changes by tools, split into independently testable and reviewable shards, then block the old pattern from reappearing. Strongest argument: the largest change that can be made atomically shrinks as codebase and contributor count grow. Force: delivery speed, cost of ownership. Best when: large shared codebase, many owners; small single-owner code can change in one step (L1013; REG-1003).
- P2 A central team (usually the one that wants the change) owns the migration with staffed capacity. Strongest argument: completion and low consumer load; an unfunded mandate stalls as organic migration. Force: completion, cost of ownership; costs central capacity. Best when: many consumers and mechanical changes (L1014 a; REG-1002, REG-1003).
- P3 Consumers migrate themselves (implicit in advisory deprecation). Strongest argument: autonomy. Best when: the replacement is transformatively better (L1014 b; REG-1002).
Context variables: CONSUMER_COUNT_AND_OWNER_COUNT (L1013: "context where it wins: large shared codebase, many owners"; L1014: P2 "wins with many consumers")
Links: Realizes OWNERSHIP.LIFECYCLE (L1013 see also L058, L052); See CHANGE_FLOW.INTEGRATION (L1013 see also L132); See EVOLUTION.DECOMMISSION.5 (L1014 points to origin claim EVOL-C33, which is L1033)

#### EVOLUTION.INCREMENTAL.5 Lifespan, Consumers and Cost of Change

Intent: How much changeability to invest in, given how long the system lives and how many depend on it.
Rows: L1015, L1016
Positions (no verdict):
- P1 Treat a system's life as a series of changes it must absorb; the expected lifespan decides how much to invest in changeability. Force: cost of ownership over time. Consensus (L1015; REG-1014, REG-1031 not read from the original).
- P2 The more consumers, the more observable behaviours are depended on, so the cost of change or removal grows with consumer count; counter with tests in CI that capture what consumers rely on, so infrastructure owners need not track consumers. Force: evolution without breakage, cost of ownership. Consensus (L1016; REG-1002, REG-1014).
Context variables: -
Links: Realizes ASSURANCE.CONTRACTS (L1016 see also L105, near claim L1281); Realizes OWNERSHIP.LIFECYCLE (L1016 see also L059, L058); Realizes OWNERSHIP.SELECTION (L1016 see also L014); Realizes OWNERSHIP.STANCE (L1015 see also L330)

#### EVOLUTION.INCREMENTAL.6 Conventions Applied Forward Only

Intent: How a new convention reaches existing objects, so that consistency is bought without forced churn.
Rows: L296
Positions (no verdict):
- P1 Maintainer's codified practice (MAINT-S01): a new convention applies to new objects and is not retroactive; existing objects are not forced to rename; a deprecated item is marked in its name, kept with documented deprecation and relationships during the transition, and removed by a later planned change. Strongest argument: cost and reversibility. Best when: the surface has many consumers. Row reading: agrees with public practice read as majority (L296; REG-181).
- P2 Retroactive rename. Strongest argument: consistency, at a cost of risk (L296).
Context variables: CONSUMER_COUNT (L296: forward-only "wins when the surface has many consumers")
Links: See EVOLUTION.DECOMMISSION.3 (L296 deprecated-item marking)

#### EVOLUTION.DEBT Technical Debt and Refactoring

Intent: What counts as debt, when to take and repay it, and how to refactor.
Rows: -

#### EVOLUTION.DEBT.1 What Counts as Debt

Intent: What the term covers, so that the right things are inventoried and weighed.
Rows: L1018, L1021
Positions (no verdict):
- P1 Debt is design or implementation constructs expedient in the short term that make future change more costly or impossible; a contingent liability limited to internal qualities (maintainability, evolvability), often incurred unintentionally. Consensus (L1018; REG-1001, REG-1005, REG-1006).
- P2 Debt is wider than code quality: the most significant debt comes from design trade-offs not visible in code metrics and covers migrations, documentation, tests, dead code, dependencies, team expertise and release process; inventory all of these. Row certainty: grounded for REG-1006, inferred for the full list (secondary source) (L1021; REG-1006, REG-1025, REG-1030).
Context variables: -
Links: See CHANGE_FLOW.DATA_CHANGE (L1021 see also L384)

#### EVOLUTION.DEBT.2 Taking Debt Versus Investing in Quality

Intent: Whether and when speed is bought with debt, so that debt is taken knowingly or not at all.
Rows: L1020, L1207, L1237, L1231
Positions (no verdict):
- P1 A little debt speeds development if repaid promptly: take it deliberately only for functionality below the point where good design pays off, repay promptly. Strongest argument: delivery speed now. Force: delivery speed. Best when: a short-lived or exploratory deliverable (L1020 a; REG-1005).
- P2 Quality is not a trade-off: the payoff arrives in weeks, so invest in internal quality from the start, beyond the smallest scope. Strongest argument: cost of change later; internal quality pays back in weeks, not months, and does not trade against speed. Force: cost of change. Best when: anything that will be changed. Fowler's caveat: no objective proof (L1020 b, L1207; REG-1007, REG-1001, REG-1120, REG-1121). Agreement: contested (L1020), consensus (L1207). Row certainty: inferred, the payoff point is unproven (L1020).
- P3 Distinguish prudent from reckless debt; take deliberate debt only knowingly (L1237; REG-1130; the sibling holds the quadrant).
- P4 Treat simplicity as a reliability property: delete code, keep APIs minimal, stay modular, release small and often (L1231; REG-1132).
Context variables: SCOPE_AND_LIFETIME (L1020: P1 "wins for a short-lived or exploratory deliverable", P2 "for anything that will be changed")
Links: Realizes OWNERSHIP.STANCE (L1231 see also L308)

#### EVOLUTION.DEBT.3 Finding and Inventorying Debt

Intent: How debt is made visible, so that repayment can be chosen with evidence.
Rows: L1022, L1023, L1027
Positions (no verdict):
- P1 Tool-detected smells, coupling, dependency analysis. Strongest argument: automation and trend tracking. Force: cost, visibility. Costs validity and misses design debt (L1022 a; REG-1006).
- P2 Periodic survey of engineers about hindrance, deliberate debt and investment in reduction. Strongest argument: validity, since no known automatic metric reliably predicts where debt hurts. Costs subjectivity and survey fatigue. Best when: no validated metric exists, as the primary signal with P1 as supplement for specific smells (L1022 b; REG-1025, REG-1030). Row certainty: inferred for the Google figures (T4 summary of an unread T3 paper).
- P3 Keep an inventory of debt items, each with cause, consequence, affected artefact and impact; manage by recognizing, analyzing, monitoring and measuring. Where items live: tracker (visible to planning), in-code marker (travels with the code, cheap), decision record (ties debt to a decision). Force: visibility versus authoring cost. Open: which place gets items repaid soonest. Row certainty: inferred, no source compares storage places (L1023; REG-1006, REG-1027, REG-1028, REG-1030).
- P4 Treat maintainability as measurable: searchability, time to change code in another team's area, duplicate and unused code, version consistency, length of dependency upgrade cycles. Consensus, single source (L1027; REG-1015).
Context variables: -
Links: Realizes OWNERSHIP.LIFECYCLE (L1027 see also L052; boundary ADOPT for dependency upgrades); See CHANGE_FLOW.MEASURE (L1027 see also L169)

#### EVOLUTION.DEBT.4 Refactoring Step Size

Intent: How large a refactoring step is, so that the system is never broken for long.
Rows: L1024
Positions (no verdict):
- P1 Refactor only in small behaviour-preserving steps, the system never broken for more than minutes and the checks green; larger rearrangement is restructuring and needs different controls. Force: reversibility, speed of feedback. Consensus; single practice recorded (L1024; REG-1008, REG-1009).
Context variables: -
Links: Realizes ASSURANCE.BEHAVIOUR (L1024 see also L081, L107; the check that detects behaviour change); See CHANGE_FLOW.REVIEW (L1024 see also L140)

#### EVOLUTION.DEBT.5 Timing and Responsibility of Repayment

Intent: When debt is repaid and by whom, so that repayment happens where it pays and is not crowded out.
Rows: L1019, L1025, L1026
Positions (no verdict):
- P1 Interest accrues only where code is changed: pay principal gradually in areas of high activity, leave crufty but stable areas alone. Valid while those areas stay stable; Beck's "never tidy" reason is the same (L1019; REG-1001, REG-1006).
- P2 Time each tidying by cost comparison: tidy first when tidying plus the behaviour change costs less than the change alone; tidy after, later or never otherwise, and never when the code will not change again. Majority; grounded for options and "never", inferred for the inequality (L1025; REG-1008, REG-1010).
- P3 Refactor opportunistically, by whoever touches the code, as ordinary work; dedicated scheduled refactoring is the exception. Strongest argument: flow, small risk. Best when: tests are strong and ownership is shared (L1026 a; REG-1008).
- P4 Opportunistic plus explicit capacity or programme for structural debt. Strongest argument: visibility and protection from feature pressure. Best when: debt is cross-team, so no one touches it in passing; Fowler allows "a day or two" for a gnarly lump (L1026 b; REG-1015, REG-1030, secondary).
Context variables: OWNERSHIP_OF_CODE_AND_TEST_STRENGTH (L1026: P3 "wins when tests are strong and ownership is shared", P4 "when debt is cross-team")
Links: Conflicts CHANGE_FLOW.REVIEW (L1026 "possible tension" with L140); See CHANGE_FLOW.REVIEW (L1025 see also L140)

#### EVOLUTION.DECOMMISSION Decommissioning

Intent: How code, interfaces and systems are deprecated, switched off and removed.
Rows: -

#### EVOLUTION.DECOMMISSION.1 Why Remove

Intent: Why removal is treated as engineering work, so that obsolete code and systems do not linger.
Rows: L1028, L1029, L1041
Positions (no verdict):
- P1 Code is a liability, not an asset: value lies in functionality, so aim for more functionality per unit of code; removing obsolete systems is one of the most efficient ways to improve the ratio. Consensus (L1028; REG-1002).
- P2 Do not leave code no longer intended for use on production systems: a regulator found missing controls against activating such code a contributing failure in an incident that lost over 460 million dollars in 45 minutes. Consensus from one T1 case; that removal prevents the class is inferred (L1029; REG-1017).
- P3 Removing obsolete code and systems is ordinary engineering work with a declared owner and budget, not leftover work after features. Majority; row certainty inferred, a synthesis no source states as one rule (L1041; REG-1002, REG-1003, REG-1006, REG-1008, REG-1021).
Context variables: -
Links: Realizes OWNERSHIP.STANCE (L1028 see also L037, L001); See CHANGE_FLOW.DEPLOY (L1029 see also L166)

#### EVOLUTION.DECOMMISSION.2 Grounds to Retire

Intent: On what grounds a retirement is decided, and how the decision is kept.
Rows: L1037
Positions (no verdict):
- P1 Retire on stated grounds (a replacement of comparable or better function exists, upkeep cost exceeds value, the technology is out of date, the strategy changed, or use is low), and record the decision like any other. Consensus; grounded for the grounds, inferred for recording the retirement decision (L1037; REG-1002, REG-1011, REG-1026, REG-154).
Context variables: -
Links: See EVOLUTION.DECISIONS.4 (L1037 see also L232)

#### EVOLUTION.DECOMMISSION.3 Announcing Retirement

Intent: How retirement is signalled to consumers, so that remaining users are found and warned without fatigue.
Rows: L1030, L1032
Positions (no verdict):
- P1 Announce in two distinct stages with distinct signals: deprecation (no longer recommended, still working) and sunset (will stop responding at a stated time), the sunset never earlier than the deprecation; for HTTP interfaces use the Deprecation and Sunset header fields. Force: consumer predictability. Consensus (L1030; REG-1026, REG-182, REG-183).
- P2 Warnings must be actionable and relevant, because excess causes alert fatigue; also expose them in machine-readable form (response warning header, audit annotation, a usage metric labelled with the removal release) so remaining users are found. Consensus (L1032; REG-008, REG-1002).
Context variables: -
Links: Realizes ASSURANCE.CONTRACTS (L1030 see also L060, L352); Realizes OWNERSHIP.SERVICES (L1030 see also L351, L034, L353, L355; L1032 see also L351)
Stack pointers: L1030 stack "HTTP APIs (the two-stage principle is neutral)"; L1032 "the machine forms are Kubernetes and HTTP"

#### EVOLUTION.DECOMMISSION.4 Support Window Before Removal

Intent: How long a retired form stays supported, so that consumers can plan and maintainers do not carry old forms forever.
Rows: L1031
Positions (no verdict):
- P1 Tiered fixed windows in a published policy by stability tier: stable interfaces deprecated but not removed within a major version; pre-release a fixed period (9 months or 3 releases, whichever is longer); experimental may go at any release; at least one minor release carrying the deprecation precedes removal in a major release. Strongest argument: consumer predictability. Force: reversibility, consumer friction; costs maintainers carrying old forms. Best when: many external consumers (L1031; REG-008, REG-030).
- P2 Case by case (implicit in REG-1026, which gives no durations). Strongest argument: speed. Best when: few known consumers (L1031; REG-1026).
Context variables: CONSUMER_COUNT (L1031: P1 "wins with many external consumers", P2 "with few known consumers")
Links: Realizes ASSURANCE.CONTRACTS (L1031 see also L060, L352); Realizes OWNERSHIP.SERVICES (L1031 see also L034, L353, L355)
Stack pointers: L1031 "neutral (the numbers are Kubernetes-specific)"

#### EVOLUTION.DECOMMISSION.5 Advisory or Compulsory Deprecation

Intent: Whether retirement is left to consumers' choice or forced by deadline, so that it completes at an acceptable load.
Rows: L1033
Positions (no verdict):
- P1 Advisory (no deadline). Strongest argument: consumer autonomy and no central load. Rarely completes unless the replacement is transformatively better. Best when: the replacement sells itself (L1033; REG-1002).
- P2 Compulsory: a firm deadline plus a staffed migration team. Strongest argument: completion and removal of the old cost. Risk: an unfunded mandate. Best when: the old form has real upkeep cost or risk (L1033; REG-1002).
Context variables: -
Links: Realizes OWNERSHIP.SERVICES (L1033 see also L353); See EVOLUTION.INCREMENTAL.4 (L1014 points to origin claim EVOL-C33, which is L1033)

#### EVOLUTION.DECOMMISSION.6 Carrying Out the Retirement

Intent: How a retirement is executed, so that nothing still used is cut off and nothing attached is left behind.
Rows: L1034, L1035, L1036
Positions (no verdict):
- P1 Before switching off, verify who or what still uses the system, restrict access reversibly for a period to flush out remaining users (controlled blackouts, restrictive controls with a way back), keep restorable backups and recorded metadata, then remove. Consensus (L1034; REG-1018, REG-1026).
- P2 An explicit project owner for whom removal is the primary objective, with measurable intermediate milestones (for example deleting key sub-components), not only the final removal. Consensus, single source (L1035; REG-1002).
- P3 Cover everything attached: licences, attached storage, DNS entries, domain membership, and entries in configuration, monitoring, automation and security tooling; check against compliance requirements. Consensus, single source (L1036; REG-1018).
Context variables: -
Links: See CHANGE_FLOW.DATA_CHANGE (L1034 see also L419; L1035 see also L384); See ASSURANCE.DATA_INTEGRITY (L1034 see also L388); See TRANSVERSE.PRIVACY (L1034 near claims L1114, L1154)

#### EVOLUTION.TECHNOLOGY Keeping Technologies Few

Intent: How the set of technologies in use is kept small and its standing positions recorded.
Rows: -

#### EVOLUTION.TECHNOLOGY.1 Adding as Replacing

Intent: Whether a new technology is added or replaces an older one, so that the long-term cost of an extra system is not accumulated.
Rows: L026, L1038, L1229
Positions (no verdict):
- P1 Hold the number of different tools solving the same problem down; plan migration of the replaced one when introducing another. Majority (L026; REG-013).
- P2 Add a technology as a replacement, not an addition: commit to replacing the older one and plan its retirement, since the long-term cost of keeping an extra system reliable exceeds the inconvenience of building with it. Majority; complements the sibling's choice claims, not the retirement (L1038; REG-013, REG-1002, REG-1022).
- P3 Keep the number of distinct technologies small; pick few tools that cover the whole domain so shared platform work benefits all. Majority (L1229; REG-1022).
- Note: L026 and L1038 state the same normative thing; kept as separate rows by the ledger.
Context variables: -
Links: Realizes OWNERSHIP.SELECTION (L1038 see also L024, L025; L1229 see also L026); See EVOLUTION.TECHNOLOGY.3 (L1038 near claim L1040)

#### EVOLUTION.TECHNOLOGY.2 Standing Position per Technology

Intent: How a team's standing stance on each technology is shared and recorded, so that it knows what to standardize on, evaluate and stop using.
Rows: L1039
Positions (no verdict):
- P1 Keep an explicit shared position per technology (adopt, trial, assess, hold) with a decision trail. Majority; grounded for the rings, inferred for the decision trail (stated in a search summary only) (L1039; REG-015, REG-1024).
Context variables: -
Links: Realizes OWNERSHIP.SELECTION (L1039 see also L025, L024); See EVOLUTION.DECISIONS.3 (the decision trail is a record, L1039)

#### EVOLUTION.TECHNOLOGY.3 How Firmly the Stack Is Held

Intent: How strongly the set of technologies is imposed, trading local fit against shared cost.
Rows: L1040
Positions (no verdict):
- P1 Mandate a small set. Strongest argument: low cognitive load, upgrade cost and shared operations. Force: cognitive load, cost of ownership. Costs local fit. Best when: many teams share platform and on-call (L1040 a; REG-106, REG-013).
- P2 Paved path: departures allowed but unsupported. Strongest argument: autonomy with a cheap default. Force: autonomy, delivery speed. Costs a tail of unsupported variants (L1040 b; REG-1023).
- P3 Polyglot freedom per component. Strongest argument: local fit and learning. Costs heterogeneity. Best when: few, independently operated components (L1040 c; REG-1016). Variant with multiple dependency versions is rejected by the one-version rule (REG-106; boundary ADOPT).
Agreement: contested (L1040).
Context variables: TEAMS_SHARING_PLATFORM (L1040: P1 "wins with many teams sharing platform and on-call", P3 "with few, independently operated components")
Links: See EVOLUTION.TECHNOLOGY.1 (L1040 see also L026, L1229); See CHANGE_FLOW.INTEGRATION (L1040 see also L132); Realizes OWNERSHIP.SELECTION (L1040 see also L024)

#### EVOLUTION.TECHNOLOGY.4 One General-Purpose Store for Several Roles

Intent: Whether one mature data store serves several roles until its limits are reached, so that the number of systems stays small.
Rows: L1232
Positions (no verdict):
- P1 Prefer one mature general-purpose data store for queue, cache, search and documents until its limits are actually reached, then add a specialised system. Strongest argument: fewer systems mean fewer failure points and less context switching; add tools "when you actually hit Postgres limits, not when you think you will", only while the store meets the need now with about 10x headroom (REG-1128, REG-1129, T4, one with commercial interest). Force: cost of ownership, cognitive load. Best when: small team, modest load (L1232; REG-1126, REG-1128, REG-1129).
- P2 Add a specialised system from the start. Strongest argument: the limits of the general store (sub-millisecond cache, large-scale search relevance, scale); the T1 source documents SKIP LOCKED for queue-like tables and states it is not suitable for general-purpose work (REG-1126). Best when: sub-millisecond cache or large-scale search are requirements (L1232).
Agreement: contested. Row certainty: inferred; the limits were not verified from primary sources; no T1 or T2 source states the "one database for everything" rule.
Context variables: LOAD_AND_TEAM_SIZE (L1232: "applies when: small team, modest load. Does not apply when: sub-millisecond cache or large-scale search are requirements")
Links: Realizes OWNERSHIP.STANCE (L1232 see also L308, L311); Realizes OWNERSHIP.SELECTION (L1232 see also L312, L024, L1227, L1228); See EVOLUTION.TECHNOLOGY.1 (L1232 near claims L1229)
Stack pointers: origin stack was postgres; restated stack-neutral by the ledger (L1232); boundary DATA.
