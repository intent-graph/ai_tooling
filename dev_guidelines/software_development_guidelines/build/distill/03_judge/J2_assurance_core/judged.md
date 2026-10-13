# J2_assurance_core: judge records

Unit: the L1 node ASSURANCE, its L2 nodes RULES, BEHAVIOUR, CONTRACTS and their 16 L3 nodes (20 records, tree order). Rows: ledger ids L001-L460, L1001-L1289, L1501-L1565; sources by register id (REG-nnn). The maintainer's codified practice is source MAINT-S01 (REG-181, not citable): it weighs as a strong position, never an automatic winner, and a decision resting only on it is marked inferred. Rules that bind: MD-01 (the best, not the average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact).

Reading note. Where a node holds several independent rows (BEHAVIOUR.7 above all), the Decision is a lead of one to three sentences followed by sub-decisions per row, each one sentence; the lead is the node's claim, the sub-decisions are the graph build's leaf constraints.

Pinned:
- Nodes judged: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3).
- Decisions marked undecided: none.
- Flags raised: 11 (F1 to F11, listed at the end with their status after the final pass; only F9 stays open on a node, plus the maintainer point in the Certainty of RULES.4).
- Settled decisions disagreed with: none (no wave-1 decision precedes this unit; maintainer decisions MD-01 to MD-07 are respected, MD-02 shapes the treatment of L122).

---

## ASSURANCE Assurance

Intent (sharpened): for each property that must hold, which mechanism at which stage guarantees it, running on every change so that it stays true; the common rules, behaviour and interface compatibility are decided here, the other six properties in their own units.

1. **Decision.** Every property that must hold is guaranteed by a named mechanism at a named stage that runs on every change, blocks when it fails, and has a trustworthy signal; no property rests on one mechanism or on the author's own judgement. For this unit: the signal is trustworthy (RULES.1), checks sit as low and early as they can (RULES.2), gates cannot be skipped (RULES.3), review is independent and binds the exact content (RULES.4), every change meets one bar with evidence (RULES.5), behaviour is pinned by self-testing code whose power is measured (BEHAVIOUR), and interface compatibility has a definition, a contract test and one source of description (CONTRACTS). Outcome: the design was good, the testing was good, the review was trustworthy, and what runs is what was reviewed (MD-02).
2. **Grounds.** Roll-up of the three L2 decisions below; each is grounded in the rows named there. The unifying claim "no single control is relied on, and a pass is believable" rests on L1538, L1550, L1558, L1562 and L1546.
3. **Positions.** None at this node: it holds no rows (roll-up).
4. **Rejected.** Not applicable (no rows). Rejected positions are recorded at the L3 nodes.
5. **Context.** None at this level; contexts that move a decision (change volume, criticality, number and reach of consumers, suite maturity) are on the L3 nodes that carry them.
6. **Certainty.** Inferred as a roll-up (own certainty, not carried up from children): every child decision is grounded or inferred, but the roll-up covers only three of the nine L2 nodes (DATA_INTEGRITY, DOCS_SYNC, SECURITY in J3; PERFORMANCE, AVAILABILITY, ARTIFACT in J4 are judged elsewhere).
7. **Flags.** F9: the L1 claim is complete only after J3 and J4 are judged; it must be re-rolled in wave 3.

Constraints: MUST every property have a mechanism, a stage and a recurring trigger. Links: children RULES, BEHAVIOUR, CONTRACTS (this unit); DATA_INTEGRITY, DOCS_SYNC, SECURITY (J3); PERFORMANCE, AVAILABILITY, ARTIFACT (J4); realized by CONSTRUCTION, CHANGE_FLOW, OPERATION.

---

## ASSURANCE.RULES Rules Common to Every Property

Intent (sharpened): where a check runs, what makes its signal trustworthy and fast, and what makes a gate or a review binding whoever authored the change.

1. **Decision.** A check is worth running only if its failure means a real defect (RULES.1), it runs as low and as early as it can catch the failure and returns in minutes (RULES.2), and the rule it enforces blocks the merge without possibility of being skipped (RULES.3); review of a change is independent, accountable and bound to the exact content (RULES.4); every change meets one bar and shows its completion by evidence (RULES.5). Outcome: a pass can be believed, a finding is acted on, and the review was trustworthy.
2. **Grounds.** Roll-up of RULES.1 to RULES.5 (31 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable (roll-up).
5. **Context.** None here; change volume moves RULES.2, risk moves RULES.4.
6. **Certainty.** Grounded as a roll-up for the principles (T1/T2 sources under each child); inferred for every numeric default.
7. **Flags.** none (see the children).

Links: children RULES.1 to RULES.5; used by BEHAVIOUR, CONTRACTS and every other property node.

### ASSURANCE.RULES.1 Trustworthy Signal

Intent (sharpened): a failing check means a real defect, so that a pass can be believed and a finding is acted on.

1. **Decision.** Prevent non-determinism at its cause (isolate each test: each test establishes the state it needs instead of relying on another test's clean-up; where rebuilding per test costs too much, the undo is done by the platform (a rolled-back transaction, a snapshot restore), never by hand-written clean-up code; wait on events or polling rather than bare sleeps, wrap the clock, double remote services, shrink large tests, and check a new test repeatedly when it is added). A flaky test that already exists is a defect of the pipeline: take it out of the blocking gate into a quarantine with an owner, a numeric cap and a time limit, then fix or delete it. A check blocks while its measured false-alarm rate (flaky-test rate, false-positive rate of static checks as developers perceive it) is within the budget the team states for it; a lower-confidence check is shown in review as advice, also under a budget; a check over budget in either mode is fixed or removed. Outcome: a failing check means a defect, so a pass can be believed.
2. **Grounds.** A test or finding that fails without a defect teaches people to ignore it (L109 consensus; REG-048, REG-054, REG-056; L147 REG-085). Causes of flakiness are known and preventable: asynchronous waits were 45% (74 of 161) of classified fixes, and 74% (14 of 19) of order-dependent flaky tests were fixed by cleaning shared state (L1559, L1560; REG-1570, T2, mostly Java; L111 REG-051, REG-054). Quarantine with a cap and deadline keeps the gate trustworthy while causes are found (L110; REG-054). A budget for static-check false positives is operated at scale (L086, L1132; REG-052, REG-1086, REG-1092, REG-1099; SSDF REG-004 asks for a human reviewing tool findings).
3. **Positions.** P1 quarantine with cap and limit (trust of the gate, delivery speed). P2 remove at once (trust, no tolerance). P3 rerun only marked-flaky tests (delivery speed, coverage kept). P4 classify, retry or disable during investigation (trust). P5 prevent the cause (trust of the result). P6 track flake rate, act near 1% (early warning). P7 false-positive budget for static checks (trust in findings). P8 hand-written clean-up of shared state (L1560).
4. **Rejected.** P2 immediate removal: it is quarantine with a zero time limit; best when the test is of low value or nobody will own the quarantine, in which case delete. P3 rerun marked tests: a rerun that turns red to green hides the defect; acceptable only as a recorded, capped part of quarantine, or for a failure traced to infrastructure. P4: folded into the decision as quarantine (temporary disable); "retry" alone is rejected for the reason given for P3. P6: kept as an example only; the 1% threshold and the 0.15% figure are one organisation's figures (L1561, single source REG-048, one organisation's figures, origin marked risky), not a standard; best as the budget when a team has no better data. P7: adopted as a budget; the 10% figure is one organisation's policy (L1132), so the value is the team's to state. P8: a bug in clean-up code shows up as a failure in another test (REG-054); best only where neither a rebuild nor a platform undo is available, and then each test checks its precondition at its start (inferred).
5. **Context.** none.
6. **Certainty.** Grounded for the principle and the causes (several T2 sources, one T1 reference); inferred for any numeric threshold (one organisation each) and for transfer of the Java-dominated studies to other languages.
7. **Flags.** none.

Constraints: MUST a check, blocking or advisory, have a stated false-alarm budget; MUST a check over its budget be fixed or removed; MUST a quarantined test have an owner, a cap and an end date; MUST NOT a rerun hide a failure. Links: holds the block-or-advise rule that BEHAVIOUR.2 and SECURITY.2 (J3) apply (X4); Conflicts BEHAVIOUR.7 (L265 against L111, resolved there); Required by BEHAVIOUR.1 (L1551 requires L1558).

### ASSURANCE.RULES.2 Placement and Feedback Speed

Intent (sharpened): at which stage and level a check runs so that feedback is fast and each failure is caught as low as it can be, with several kinds of check combined.

1. **Decision.** Place each check at the lowest level and the earliest stage that can catch the failure it exists for, and when a higher-level test finds a bug that no lower-level test caught, add the lower-level test. Keep blocking feedback to minutes (about ten), trigger the build on every commit, fix a broken build first, and record which analyses and tests run at which stage for which risk; combine different kinds of check (static, dynamic, negative tests) and rely on none alone. Outcome: failures are cheap, quickly located, and no single mechanism is the only line of defence.
2. **Grounds.** Lower is cheaper, faster and more precise (L091, L1183 consensus; REG-044, REG-072). Minutes-long feedback and a priority fix of a broken build are DORA capabilities and Google's practice (L112; REG-056, REG-057, REG-085). A recorded per-stage, per-risk policy is an SSDF practice (L121; REG-004). Dynamic checks found on average 49 problems per site that static analysis missed on over 200 sites (2015, dated; L1550; REG-1561, REG-1564); layering controls follows from a taxonomy of 107 attack vectors against 33 safeguards (L1538; REG-1554, T2, inferred); machines catch what people forget to look for (L1546).
3. **Positions.** P1 lowest level possible (cost, precision). P2 minutes of feedback, build on every commit (speed). P3 gate on the fast and reliable, run the slow after merge and roll back (speed, accepts some coverage loss). P4 staged pipeline, slower stages more thorough (confidence). P5 recorded policy per stage and risk. P6 combine kinds of check. P7 layer controls. P8 machines find forgotten defects.
4. **Rejected.** P3 and P4 are two answers to one question (what blocks the merge versus what runs later); neither is rejected, the choice depends on context (below). P7 and P8 are restatements of P6 at the level of principle, kept as grounds. Nothing is rejected outright.
5. **Context.** Change volume and rollback: with very high change volume, a build cop and automatic rollback, gate on what is fast and reliable and run slower tests after merge, with automatic revert on failure (P3, L145); with smaller volume, run later stages before release in a staged pipeline (P4, L145). In both cases what ships has passed the full set. DORA pitfall: blocking tests longer than ten minutes.
6. **Certainty.** Grounded for placement, speed and recorded policy (T1/T2, consensus); inferred for combining and layering (one T2 taxonomy, one dated study); the ten-minute figure is a DORA/Fowler default, not a measured optimum.
7. **Flags.** none (the numeric defaults, ten minutes and 95% presubmit pass, are stated as single-source or one organisation's figures in Certainty).

Constraints: MUST the blocking set return in minutes; MUST every higher-level miss produce a lower-level test; MUST a stage policy be recorded per risk. Links: Requires BEHAVIOUR.1 (L1550 requires L1552); uses RULES.3 for blocking; CHANGE_FLOW.BUILD realizes the pipeline.

### ASSURANCE.RULES.3 Gates That Cannot Be Skipped

Intent (sharpened): a rule that matters is enforced by an automated check that blocks the merge, always runs, and cannot be passed by being skipped.

1. **Decision.** A rule that matters is a blocking automated check, not a convention: module boundaries and fitness properties (performance, security, operability) are checked automatically, the gate always runs, and a skipped, neutral or missing required check counts as a failure, never a pass. Outcome: nothing a rule forbids reaches the mainline, whoever authored the change.
2. **Grounds.** A check changes behaviour only when failing it stops the merge; some platforms treat a skipped required check as passing (L1562; REG-114, T1, one platform's fact stated generally). Boundaries kept by tooling rather than convention (Shopify) and fitness functions that make fit explicit, non-functional properties included (L1216, L1234; REG-1117, REG-1119, REG-1134).
3. **Positions.** P1 enforce boundaries by automated checks (L1216). P2 fitness functions (L1234). P3 a gate always runs and a skip is not a pass (L1562).
4. **Rejected.** Convention or review alone for a mechanizable rule: best only when the rule cannot be expressed as a check (judgement on whether a design is appropriate), and then it belongs to review (RULES.4). Small increments in P2 (L1234) is an evolution practice: its first clause is indexed to EVOLUTION.INCREMENTAL (MD-03).
5. **Context.** none.
6. **Certainty.** Grounded for the platform fact (one T1 source) and the principle that an unenforced rule is not a rule; inferred for fitness functions as the mechanism (REG-1117 plus REG-1119, majority).
7. **Flags.** none (the skipped-check fact rests on one platform, REG-114, stated in Certainty; the principle holds regardless).

Constraints: MUST a required check fail closed (skipped or missing = failed); MUST NOT a blocking check be a noisy one (RULES.1). Links: Required by BEHAVIOUR.1 and BEHAVIOUR.2 (L1547, L1551 require L1562); CHANGE_FLOW.INTEGRATION and ARTIFACT.2 realize protection of the mainline.

### ASSURANCE.RULES.4 Independent Review That Binds

Intent (sharpened): a review is a trustworthy signal only when the reviewer is independent of the author, a named person or role is accountable, and the approval binds the exact content that ships.

1. **Decision.** Every change to mainline is checked before integration by a party other than whoever authored, pushed or requested it, working from its own context: a person or an automated reviewer; for a change the team's risk tier marks high, the reviewer is of a different kind from the author; the check is recorded on the development platform; only a tier the team defines in advance (changes that follow an established pattern, an unremarkable fix, documentation), in a team whose mainline is kept releasable by automated gates and fast revert, may be checked after merge; a named person or role stays accountable for each change, approves it and is able to defend it, and an approval binds the exact final content, so a new commit that changes the diff voids earlier approvals. Per-change approval by an external board is not used; separation of duties is met by peer review, automated testing and monitoring, with the form of review set by the risk of the change. Outcome: the review was trustworthy and what ships is what was approved.
2. **Grounds.** Independent check as a feature of the platform record (L136; REG-083, REG-094, REG-098, REG-115, REG-116). Approver differs from the author, and approval binds to content (L1046, L1047; REG-1036, REG-114, T1). Accountability attaches to the submitter, not the tool (L1043; REG-1035, REG-1037, REG-1040). DORA found no correlation of external review with lower failure rates and a negative effect on delivery performance (L143; REG-094).
3. **Positions.** P1 independent check on every change (dissent: Ship, Show, Ask, review only the uncertain). P2 no external board. P3 named accountability. P4 approver differs from author. P5 approval binds to the final content.
4. **Rejected.** Review only for uncertain changes (P1 dissent): it leaves the classification to the author at the moment of the change; a tier defined in advance removes that discretion (inferred); best, in a post-merge "show" form, for the tier of the Decision (consistent with L143 "by risk"). "Ship" with no review at all: best never under this node, since every change gets an independent check before or after merge. External approval board: best where a regulation requires one; regulated contexts are deferred (MD-05) and whether a given regulation still requires a board was not read (open).
5. **Context.** Risk: the default is blocking pre-merge review; the post-merge tier of the Decision applies only where gates and revert are automatic (L136, L143; the tier's conditions are grounded in REG-098, one practitioner source fetched in review).
6. **Certainty.** Grounded for independence, binding to content and the board finding (T1 and T2, DORA); the tier conditions are grounded in REG-098 (one practitioner source, fetched in review) and the reason for rejecting review of uncertain changes only is inferred; the regulatory exception is open; open: awaiting the maintainer's answer on whether an automated reviewer can be the independent check (the independence of the reviewer's context, not of its kind, is the default applied, inferred).
7. **Flags.** none on the record; the one open maintainer point (can an automated reviewer be the independent check) is held in Certainty, with its default applied in the Decision.

Constraints: MUST the approver differ from the author; MUST an approval lapse when the diff changes; MUST a named person or role be accountable. Links: index CHANGE_FLOW.REVIEW (how review is carried out); realized for the mainline by ARTIFACT.2 (L131, L1063); mechanism terms GitHub (stack pointer L1046, L1047).

### ASSURANCE.RULES.5 One Bar and Evidence for Every Change

Intent (sharpened): every change meets the same bar for design, testing and review, and shows its completion by evidence that does not depend on the author.

1. **Decision.** Every change, whatever its author, meets the same bar for design, testing and review; before a change is produced, its intent, scope, interfaces, out-of-scope items and acceptance check are fixed (in proportion to its size). Every change comes with an executable pass-or-fail check independent of the author's judgement that it is done, and completion is shown as evidence (test output, command and result, screenshot), not asserted; tests and the code under test come from independent contexts where practicable. Outcome: the design was good, the testing was good, and "done" is demonstrated.
2. **Grounds.** Same bar, no exemption (L1042; REG-1035, REG-1036, REG-1040, T1, consensus). Executable check and evidence over assertion (L1051, L1052; REG-1038, one T1 vendor guide; consistent with L123 and L269 on recorded, self-reporting results). Fixing intent and acceptance first (L1045; REG-1038, REG-1041; a vendor guide plus one DORA capability). Independent contexts so one set of assumptions does not validate itself (L1053; REG-1038, inferred).
3. **Positions.** P1 same bar. P2 intent and acceptance fixed first. P3 executable check. P4 evidence. P5 independent contexts for tests and code.
4. **Rejected.** No competing practice recorded. Exemption for generated or trusted-author change: best never; the bar is a property of the change.
5. **Context.** Cost and speed of producing a change: the cheaper and faster production, the more necessary it is to fix the acceptance check first (L1045).
6. **Certainty.** Grounded for P1 (REG-1035, REG-1036, REG-1040, T1, consensus); P3 and P4 grounded in one T1 vendor source (REG-1038), no consensus claim (L1052 is recorded single-source); inferred for P2 (vendor and one DORA capability) and P5 (a vendor recommendation, no study of effect).
7. **Flags.** none.

Constraints: MUST every change carry an executable check; MUST completion be shown by evidence; MUST NOT a change be exempt by its author. Links: Requires RULES.1, RULES.4; refined by BEHAVIOUR.1; "evidence" realized in CHANGE_FLOW.REVIEW.

---

## ASSURANCE.BEHAVIOUR Behaviour

Intent (sharpened): which tests, types and static checks, at which level and stage, guarantee that the software does what is intended.

1. **Decision.** The software is self-testing: an automated suite runs on every change and a pass means no substantial defects (BEHAVIOUR.1), types and static checks form the cheapest blocking layer (BEHAVIOUR.2), the mix of test levels is chosen for confidence per unit of time (BEHAVIOUR.3), tests observe behaviour and are built as production code (BEHAVIOUR.4), tests are triggered by change events (BEHAVIOUR.5), the suite's power is measured rather than assumed (BEHAVIOUR.6), no test leaves a durable effect on data (BEHAVIOUR.7), and defect classes that survive review are caught on production-shaped data (BEHAVIOUR.8). Outcome: the testing was good.
2. **Grounds.** Roll-up of BEHAVIOUR.1 to BEHAVIOUR.8 (61 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable (roll-up).
5. **Context.** Criticality and suite maturity (BEHAVIOUR.1, .6), where complexity lives (BEHAVIOUR.3).
6. **Certainty.** Grounded as a roll-up for BEHAVIOUR.1 to .4; inferred for .6 effect claims, .7 and .8 (maintainer-only support).
7. **Flags.** none (F3, F4, F5 settled in the final pass).

Links: children BEHAVIOUR.1 to .8; Requires RULES.1 to RULES.3; ARTIFACT, DATA_INTEGRITY (J3), SECURITY (J3) and PERFORMANCE (J4) hold the property-specific tests.

### ASSURANCE.BEHAVIOUR.1 What the Suite Must Promise

Intent (sharpened): what an automated suite must let a team conclude, who is accountable for it, and what is recorded.

1. **Decision.** Code is self-testing: the automated suite can be run at any time, on every change, and a pass means no substantial defects; without that there is no continuous integration. Everything the team does not want to break has a test, with the strict form (every behaviour, performance, accessibility and security property tested) where criticality is high or consumers are many and "enough tests to change the code confidently, scaled to risk" otherwise; the team keeps a written test policy (new functionality and every fix come with automated tests); the evidence that it is followed is the tests in each change, visible in its review, with no separate artefact; and the suite is judged by what it detects, not what it executes. The suite has an accountable owner and its results, root causes and triage are recorded in the team's workflow. Outcome: the testing was good, and change is safe and fast.
2. **Grounds.** L081 consensus (REG-056, REG-057, REG-063); L080 purpose of tests is safe change and speed, bug-catching secondary (REG-048, REG-063); L083 a pass does not prove reliability, a failure proves its absence (REG-067); strict and weak forms scaled by criticality (L082; REG-048, REG-064); written policy, with the tests in each change as its evidence, and adequacy by detection (L1551, L1552; REG-1563, T1 criteria; a separate evidence artefact would be the most demanding reading, not the best); recorded results (L123; REG-004). L122 (who writes acceptance tests) is restated as an outcome per MD-02: someone is accountable for each suite and its upkeep; exploratory and usability testing cannot be automated and complement it.
3. **Positions.** P1 self-testing code. P2 strict (Google) against weaker (Fowler) coverage of "everything not to break". P3 tests first for safe change. P4 written policy, the tests in each change as evidence. P5 developers own acceptance tests, testers explore. P6 maintainer: no stated trigger or regression catch.
4. **Rejected.** P6 (the maintainer's doctrine states how a test is built and run but not who runs it, when, on what trigger; practice appears to be on-demand runs): not best; it contradicts L081, L106 and L144, and an on-demand suite does not guard change; it would be adequate only for one-off code that is never changed again. P5 as a rule about who writes tests: outside the principles (MD-02); only the outcome (owner, upkeep, exploratory complement) is kept. The strict form of P2 for every team: best only under high criticality or many consumers (L082), else the weaker form.
5. **Context.** Criticality and number of consumers: strict "everything not to break has a test" where criticality is high or consumers are many; scaled to risk otherwise (L082).
6. **Certainty.** Grounded for self-testing, the purpose and the written policy (T1, T2 consensus); inferred for the strict/weak split (single formulation per form); P6 is open (inferred absence, not confirmed).
7. **Flags.** none (the decision does not depend on whether the maintainer's practice has an automated trigger, L331: self-testing code on every change is consensus, L081, L106, L144).

Constraints: MUST the suite run on every change and be runnable in the language's standard way; MUST a written test policy exist (new functionality and every fix come with automated tests); the evidence that it is followed is the tests in each change, visible in its review, with no separate artefact; MUST NOT a pass be read as proof of reliability. Links: Requires RULES.3 and RULES.1 (L1551 requires L1562 and L1558); realized in CHANGE_FLOW.BUILD.

### ASSURANCE.BEHAVIOUR.2 Static Layer

Intent (sharpened): which type, lint and analysis checks run on every change as the cheapest layer, and how strictly.

1. **Decision.** Type checking, linting and analysis form the first and cheapest test layer and run on every change; type checks, compiler warnings and the linter rules the team adopts block; analyses whose findings need judgement advise in review, as RULES.1 sets: build with warnings enabled and treated as errors, address every linter warning, and run at least one analyser beyond compiler warnings before a major release. Analysis is incremental (changed files), reports newly introduced issues first, appears in review, and offers automated fixes; the trend of warnings and complexity is watched against volume-driven drift. Types are enforced for large, long-lived code and introduced gradually on existing code (annotate incrementally, keep an escape hatch, no rewrite). Outcome: known classes of mistake never reach review.
2. **Grounds.** Types as first test layer (L084, majority; REG-047, REG-065, REG-075); gradual adoption (L085 consensus; REG-065, REG-075); warnings as errors and continuous analysis (L088; REG-004); linter MUST and analyser before release (L1548, L1549; REG-1563 T1 criteria); incremental, new-first analysis (L087; REG-052); trend watching (L1054; REG-1035, REG-1046, one observational study, practice inferred); type checks, warnings and adopted linter rules must block (L1547, requires RULES.3), judgement analyses advise under the budget of RULES.1 (X4).
3. **Positions.** P1 enforce types. P2 gradual typing. P3 tests alone suffice. P4 warnings as errors plus analysis. P5 incremental analysis in review. P6 gates and trend. P7 every project analyses code statically and acts on it.
4. **Rejected.** P3 tests alone: no source holds it strongly; best only for small, short-lived code where annotation cost exceeds the defects prevented (not evidenced by a row, stated as the condition). P1 against P2 are not rivals: strict enforcement is the end state for large long-lived code, gradual is the route on existing code.
5. **Context.** Existing versus new code: gradual with an escape hatch on existing code (L085); enforced from the start on new, large, long-lived code (L084).
6. **Certainty.** Grounded for warnings as errors and the linter MUST (REG-004, REG-1563, T1); inferred for "types as the first test layer" (REG-047, REG-065 are T3, REG-075 is tool documentation attesting gradual typing, not the layer claim); inferred for the trend practice (one observational study) and for tests-alone being rejected (absence of a source).
7. **Flags.** none.

Constraints: MUST type checks, compiler warnings and the adopted linter rules block, and analyses whose findings need judgement advise in review, each under the false-alarm budget of RULES.1; MUST a warning be fixed or suppressed with a reason. Links: Requires RULES.3 (L1547 requires L1562); stack pointer L085 (Python mypy, TypeScript, Flow gradual typing).

### ASSURANCE.BEHAVIOUR.3 Test Level Mix

Intent (sharpened): which proportion of small, integrated and end-to-end tests gives the confidence at the cost the team can bear.

1. **Decision.** The mix follows from RULES.2 (each check at the lowest level that catches its failure): where logic lives inside units this gives many small, fast tests and progressively fewer broader ones; where failures arise in interactions between services, the weight moves to integration tests; for user-interface code, to static checks plus integration tests. End-to-end tests stay few, on critical journeys, and the proportions are recorded as a team decision with the reason; exact ratios matter less than fast, reliable, meaningful-failure tests. Where complexity lives in interactions (microservices) shift weight to integration tests, and for user-interface applications to static plus integration (the more a test resembles use, the more confidence); add larger tests where fidelity matters (configuration, load, cross-service behaviour), choosing the system under test by fidelity against flakiness. Describe tests on two separate axes, size and scope. Outcome: confidence is chosen per unit of time and cost, with the mix recorded.
2. **Grounds.** Direction and the inverted-cone warning (L089, L1182 consensus; REG-044, REG-045, REG-048, REG-072); the three models agree numbers matter less than speed, reliability and meaningful failures (L090; REG-045, REG-046, REG-047, REG-048); end-to-end tests are slow, flaky and costly to debug (L092, L1188; REG-044, REG-045, REG-048, REG-072); hermetic single process wins on speed and determinism, shared environments on fidelity (L117; REG-051); size and scope are independent axes (L093; REG-048, REG-072).
3. **Positions.** P1 pyramid. P2 honeycomb. P3 trophy. P4 numbers matter less, record the mix. P5 minimal end-to-end (Fowler counter-note). P6 larger tests where fidelity matters. P7 describe on two axes.
4. **Rejected.** Fixed ratio 70/20/10 or 80/15/5 as a rule: team-specific, Google-like infrastructure (L1554, single source REG-048, REG-049: one organisation's position). Honeycomb or trophy as the general shape: best where complexity lives in interactions or the code is user-interface, per the row conditions. Minimal end-to-end: loses where high-level tests are fast, reliable and cheap to change (L092 counter-note, L1188).
5. **Context.** Where complexity lives, logic density, team size, environment speed (L090): logic-dense code, large teams and slow environments favour the pyramid; microservices the honeycomb; user-interface applications the trophy.
6. **Certainty.** Grounded for direction and the end-to-end cost (consensus, T2); inferred for which shape fits which context (each shape held by its own proponents, no comparison study) and for the mapping from RULES.2 to each shape.
7. **Flags.** none.

Constraints: MUST the mix be recorded; MUST end-to-end tests be few and for critical journeys unless fast, reliable and cheap. Links: shared with BEHAVIOUR.4 (L1554 ratio); CONTRACTS.2 for cross-service seams.

### ASSURANCE.BEHAVIOUR.4 Test Construction

Intent (sharpened): what a unit is, what a test observes, what stands in for collaborators, and how test code is kept readable and cheap to maintain.

1. **Decision.** A test observes behaviour through the public interface, one test per behaviour, and never changes unless requirements change; test code is production code (readable, descriptive over strictly DRY, no loops or conditionals, one condition per test, arrange-act-assert). Use real collaborators when fast, deterministic and simple, otherwise a fake owned by the team that owns the real thing, mocks and stubs last; prefer state verification to interaction verification except for state-changing calls that cannot be observed otherwise; run integration tests against a real backing service of the production kind (engine and version). The team states what a "unit" is (solitary or sociable) and where tests start and stop, and records its double style. The twelve properties of a good test (L100, REG-068) are kept as the aid for judging trade-offs between tests (no test needs all, some pairs conflict), without conflict with this decision. Outcome: tests survive refactoring and fail only for real defects.
   Sub-decisions of test construction (moved from BEHAVIOUR.7, final pass R22; inferred, maintainer practice only):
   - d5 (L269): a test reports its own verdict in a fixed, searchable shape carrying unit and scenario identity.
   - d6 (L270): tests live where they change together with the unit and are discoverable; colocated where the tooling has no test tree, in a separate mirrored tree where the language has a test runner.
   - d8 (L272): fixture values reused across a test are named and set once, not hard-coded per statement (platform mechanics are a stack pointer).
2. **Grounds.** Behaviour through public interfaces (L095; REG-046, REG-048, REG-049, REG-068); real implementations first, fakes, then mocks, because over-mocking produced tests costly to maintain and rarely finding bugs (L097; REG-049, REG-050); state verification (L096; REG-049, REG-050, REG-062); tests as code and DAMP (L099, L1189; REG-044, REG-049); real backing service of the production kind (L1184; REG-044, REG-1106, REG-1109; mocks or a different engine hide engine behaviour); twelve properties as trade-offs for judging a test (L100; REG-068). d5, d6 and d8 rest on maintainer practice (REG-181), public practice read as consensus or majority for d5 and contested for d6 (L270), not fetched; no public source cited, so inferred.
3. **Positions.** P1 team-defined unit. P2 observable behaviour. P3 classical. P4 mockist. P5 state over interaction verification. P6 real, then fake, then mock; 80/15/5 mix. P7 real backing service. P8 tests are code. P9 twelve properties. P10 self-reported verdict (d5). P11 colocated against mirrored tests (d6). P12 named fixture variables (d8).
4. **Rejected.** Mirrored test tree as the general rule (P11): best where the language has a test runner; colocated best where the tooling lacks a test tree. P9 (twelve properties) is not rejected: it is the judging aid named in the Decision. Mockist as the default (P4): contested, Fowler is a convinced classicist but many skilled practitioners prefer it; best when driving design from the outside in and collaborators are costly to build (L098, L096). Interaction verification as the default: best for state-changing calls not otherwise observable. In-memory or different-engine databases in integration tests: best only where the production engine cannot be run locally or in CI. The 80/15/5 mix as a rule: acceptable only with Google-like infrastructure (L1554, single source: one organisation's position, origin marked risky).
5. **Context.** Style of design: outside-in design with role interfaces favours the mockist double style; frequent refactoring and small object graphs favour classical (L098). Tooling (a test tree or not) moves d6.
6. **Certainty.** Inferred for d5, d6 and d8 (maintainer practice only). Grounded for behaviour-through-interface, real-before-mock and tests-as-code (T2, consensus or majority); the classical-versus-mockist choice is contested (grounded as a recorded decision, inferred as a default); inferred for the real-engine rule beyond databases (stated generally from a database case).
7. **Flags.** none.

Constraints: MUST the double style and the unit definition be recorded; MUST a test not change when only structure changes; MUST integration tests use the production kind of backing service. Links: stack pointers L1184 (origin stack postgres, restated neutral) and L272 (PostgreSQL, d8); BEHAVIOUR.3 holds the mix.

### ASSURANCE.BEHAVIOUR.5 Tests Driven by Change

Intent (sharpened): which events oblige a test to be written, and in which order.

1. **Decision.** Every reported defect becomes a test that fails first and passes after the fix; code that is poorly understood is pinned by characterization tests of its actual behaviour before it is changed; a scheduled job is tested before it is scheduled like any other unit, and its first runs on real data are bounded and inspected (for example a reduced-scope test mode). A gap found by an experiment in production (ASSURANCE.AVAILABILITY.3, REG-228) is such a defect and is handled here the same way (X13). Writing tests before code is a team decision by context, not a requirement: what is required is that the test exists, was seen to fail for the right reason where it guards a fix, and runs on every change. Outcome: the regression suite is built from operational experience and change is safe.
2. **Grounds.** Bug becomes a failing test (L106 consensus; REG-004, REG-067, REG-072); characterization before change (L107; REG-063, REG-073); test-first is contested: all agree on self-testing code and disagree on the ordering mechanics, and DORA's evidence is of test automation in general, not of test-first ordering (L101; REG-056, REG-063, REG-064); scheduled job tested before it is scheduled, first runs bounded (L316, maintainer-only: the outcome holds, the reduced-scope mode is one example; public practice read as majority, not fetched); a gap found in production becomes a test (REG-228, cited by AVAILABILITY.3).
3. **Positions.** P1 test-first is a team decision (Beck for it in some contexts; DHH against; Fowler contextual). P2 bug to failing test. P3 characterization tests. P4 maintainer's pre-schedule test.
4. **Rejected.** Mandatory test-first: best for compilers, API design and tangled interfaces (Beck, L101), where fast design feedback pays; not general because the evidence is of test automation, not ordering, and DHH names design damage in MVC web code. Never testing before the change for a fix: rejected, a fix without a failing test cannot show it fixes anything.
5. **Context.** Test-first ordering is best when writing compilers, designing an API, or untangling interfaces; elsewhere the order is free (L101).
6. **Certainty.** Grounded for P2 and P3 (T2, consensus or majority); the ordering question is contested and inferred; P4 is inferred (maintainer practice only).
7. **Flags.** none (L080 is a consensus row, not a maintainer row; it is read as "tests exist before the change is trusted", consistent with L101).

Constraints: MUST a fixed defect have a regression test; MUST a scheduled job pass its tests before it is scheduled. Links: holds "a gap found becomes a test" for AVAILABILITY.3 and AVAILABILITY.5 (J4, X13); Requires BEHAVIOUR.1; scheduled job placement in CONSTRUCTION.PARADIGM.

### ASSURANCE.BEHAVIOUR.6 Measuring Adequacy and Probing for Faults

Intent (sharpened): how the power of a suite to detect faults is measured and probed rather than assumed; this node is the one location for the coverage decision (MD-03).

1. **Decision.** Coverage is used to find code no test executes and is never a quality score, a merge gate or a target; this holds for security-relevant code too, where no numeric coverage floor (for example 80% of statements) applies, because the assurance wanted there is detection of faults, which a floor does not measure and invites inflating: for security-relevant code require instead fuzzing of input-handling code (continuously where possible), tests derived from threats and past bugs, and review of every unexecuted security-relevant branch that coverage reveals. The suite's detection power is probed directly: mutation testing, run diff-based on changed code in review with mutants filtered, where criticality is high and the suite is mature; property-based testing for code with a describable input range (generators following the real data distribution, failures shrunk). The principle that adequacy is judged by detection, not execution, is stated in BEHAVIOUR.1 (MD-03). Outcome: a team knows what its suite detects, not only what it executes.
2. **Grounds.** Correlation of coverage with effectiveness is low to moderate once suite size is controlled (31,000 suites, five large Java systems; L1553; REG-1565, T2); coverage is easy to inflate (L113; REG-048, REG-059, REG-074); Google reports that engineers treat 80% as a ceiling, not a floor (REG-048, fetched in review); mutation score measures what coverage cannot show and is applied incrementally at scale (L114, L1556; REG-058, REG-074, REG-1566, REG-1567); property-based testing exposes edge cases examples miss (L115, L1557; REG-060, REG-1568, REG-1569); fuzzing is required by frameworks for security-relevant code (L116; REG-004, REG-066).
3. **Positions.** P1 coverage as a diagnostic. P2 coverage floor. P3 OpenSSF suggests covering most or all branches. P4 mutation testing. P5 skip or run offline. P6 property-based testing. P7 fuzzing. P8 (from SECURITY.3, row L1126, held there as a position): a developer security floor with structural tests to at least 80% statement coverage (NIST SSDF-derived; REG-1081, REG-1086, REG-1094).
4. **Rejected.** A coverage threshold as a gate (P2) and the 80% statement floor in a security-testing floor (P8): neither measures detection, both reward inflation, and the evidence (REG-1565, REG-048) is against them; P2 is best, if at all, for low-trust or fast-growing teams as management visibility (inferred from the wording of REG-048); P8 is best as a conformance minimum when a security baseline or contract mandates the number, stated as conformance and not as a quality claim. The OpenSSF branch coverage suggestion (P3) is compatible with the decision and wins only for a project adopting those criteria. Skipping mutation testing (P5): best where compute or noise dominates, or the suite is immature (mutating a weak suite measures nothing useful).
5. **Context.** Criticality and suite maturity: mutation testing as a routine review signal for high-criticality code and mature suites; offline or skipped otherwise (L114). A mandated baseline: the number is met as conformance (P8).
6. **Certainty.** Grounded for the coverage finding (one T2 study on Java, transfer inferred) and for fuzzing (T1 SSDF); the rule for security-relevant code is inferred (follows from the study and Google's report, no source tests a floor on security code); inferred for mutation (abstract-level evidence, no effect size) and property-based testing (effectiveness not quantified); open: effect size of mutation testing.
7. **Flags.** none (F10 resolved: the 80% statement floor of SECURITY.3, row L1126, is decided here and J3 points here, X1; the residual on a mandated baseline is closed: NIST IR 8397, REG-1086, states 80% as a minimum standard, met as conformance where a baseline imposes it, and regulated contexts are deferred, MD-05).

Constraints: MUST NOT a coverage number gate a merge, set a quality target or serve as a security floor; MUST input-handling code of security relevance be fuzzed. Links: stack pointers L115 (Hypothesis, Python), L116 (OSS-Fuzz languages); dataflow to BEHAVIOUR.1 (adequacy by detection); security fuzz depth and the L1126 floor in SECURITY.3 (J3, points here).

### ASSURANCE.BEHAVIOUR.7 Tests Without Durable Effect on Data

Intent (sharpened): how tests are run so that no test leaves a durable effect on data others rely on, how their data and configuration are kept apart, and that re-runs behave identically.

1. **Decision.** A test never leaves a durable effect on data that anyone relies on. The default mechanism is a separate disposable data store per run, never the production one, with each test isolated; running on shared or production-sized data behind a boundary guaranteed to be undone is best only when the dataset cannot be cloned or its shapes cannot be synthesized and the platform can undo every effect of the test. Outcome: tests are safe to run anywhere and re-runs behave identically.
   Sub-decisions by row:
   - d1 (L1185, L265): as above; a rollback boundary is a second line of defence, and a functional test never runs against production data unless every durable effect (rows, sequences, notifications, external calls) is provably undone; load and locks are transient effects governed by the guardrails of ASSURANCE.AVAILABILITY.3, not by d1 (X5).
   - d2 (L266): default to synthetic fixtures or factories per test (explicit, hermetic); use a curated, catalogued set of real records selected by queryable attributes where shapes are rich and costly to fabricate; never invent rows or pick arbitrary production rows; real records are subject to the privacy rules held in TRANSVERSE.PRIVACY (index only, MD-03); a persistent new shape is feature work by a separate idempotent script.
   - d3 (L267): choose the execution vehicle by risk and by runner: read-only tests as plain queries; tests that can mutate or fail run, when automated, as one atomic unit that is rolled back; an open-transaction wrapper only for a human at the keyboard.
   - d4 (L268, stack pointer): the idiom that every outcome rolls back (a final error whose message is the verdict) is a realization of d3 on one platform; not a decision.
   - d5, d6, d8: moved to BEHAVIOUR.4 as sub-decisions of test construction (final pass R22).
   - d7 (L271): test configuration lives in a namespace disjoint from the production context and production code never reads it.
   - d9 (L273): shaping mutations are conditional on an actual change, so re-runs behave identically and write volume drops.
2. **Grounds.** Disposable store, per-test isolation (L1185; REG-1106, grounded) and no shared state, no risk to real data (L265 position a; test frameworks); rebuild state rather than clean up (L111; REG-051, REG-054). The maintainer's forced-rollback practice (L265 position b, REG-181) rests on realism and cost of cloning, and states its own condition (data large, shapes unsynthesizable, platform can undo every effect). d2, d3, d7 and d9 rest on maintainer practice (REG-181) with public practice read as consensus or majority for d7 and d9, not fetched; no public source cited, so inferred. The maintainer's rollback is the platform undo of RULES.1, under d1's own condition; "no durable effect anywhere" is the maintainer's own rule (L265), so this is not against the maintainer's practice.
3. **Positions.** P1 disposable store per run. P2 maintainer rollback on shared or production-sized data. P3 synthetic fixtures against curated real records. P4 vehicle by risk and runner. P5 final error as verdict. P8 disjoint test configuration. P10 conditional mutations. (P6 self-reported verdict, P7 colocated against mirrored tests, P9 named fixture variables moved to BEHAVIOUR.4 as P10, P11, P12.)
4. **Rejected.** P2 as the general rule: real shapes are a real need, but the practice puts every effect that a rollback cannot undo at risk and conflicts with rebuild-over-cleanup (L111); best exactly under its stated condition. Synthetic factories as the only source (P3): best where the domain is small and shapes easy to construct; curated real records win where shapes are rich.
5. **Context.** Size and cloneability of the data and the platform's ability to undo every effect move d1; richness of data shapes moves d2; a human at the keyboard moves d3.
6. **Certainty.** Grounded for the d1 default (REG-1106 is one framework's documentation plus the rebuild-state principle L111; consensus recorded, not several T1 sources); inferred for the rest (maintainer practice only, public practice read not fetched); d4 is a platform fact of one stack (stack pointer only).
7. **Flags.** none (F1 settled: the production question is settled by X5; F5 settled: real records route to TRANSVERSE.PRIVACY in d2, and d5, d6, d8 moved to BEHAVIOUR.4; d4 is a stack pointer only).

Constraints: MUST NOT a test commit a durable change to shared data; MUST NOT production code read the test namespace; MUST a mutating automated test on shared or production-sized data run as one rolled-back unit. Links: holds the durable-data rule for tests in production; ASSURANCE.AVAILABILITY.3 (J4) holds the guardrails every production test shares, and ASSURANCE.PERFORMANCE.4 points to it (X5); Conflicts RULES.1 (L265 against L111, resolved there); stack pointer L268 (PostgreSQL); TRANSVERSE.PRIVACY (real records, index).

### ASSURANCE.BEHAVIOUR.8 Defect Classes That Survive Review

Intent (sharpened): which classes of defect pass review and deployment and fail only at run time on real data, and which practices catch them.

1. **Decision.** Passing review, static analysis and deployment is not evidence that code works: code whose behaviour depends on the shape of the data (queries, parsing, conversions, code on platforms that coerce or truncate) is exercised on production-shaped data, its edge values included, before it ships; inputs are guarded at boundaries always, not only where null seems possible. Where a platform silently truncates or coerces, make the limit a hard rule with a check; where public documentation is unclear about a platform behaviour a design relies on, verify it empirically on a live instance and record the finding with its scope; keep a pitfall catalogue indexed by error code or symptom and add an entry after any defect found twice; never apply a blanket search-and-replace across a file that holds two syntactic contexts, anchor on context and re-check the dependants. Outcome: classes of defect that review cannot see are caught before users meet them.
2. **Grounds.** Dynamic checks find what static analysis misses (figure in RULES.2, L1550; REG-1561, REG-1564, dated 2015): this corroborates only that static checks miss a run-time class of defect and does not support the production-shaped-data practice itself; characterization tests of actual behaviour (L277 reads as the platform-level case of L107; REG-063, REG-073); "every branch" was a coverage target, which BEHAVIOUR.6 rejects, so the scope is L274's own defect classes; the rest is maintainer practice (L274 to L278; REG-181), public practice read as majority or consensus, not fetched; L275 corresponds to blameless post-mortem knowledge capture.
3. **Positions.** P1 static analysis and types catch part of the class against maintainer: they do not catch these. P2 pitfall catalogue. P3 no blanket search-and-replace. P4 verify platform behaviour empirically. P5 hard rule for silent truncation.
4. **Rejected.** Reliance on static analysis and types alone for these classes: best for the part they do catch (name errors, type errors), which is why they stay as the first layer (BEHAVIOUR.2); the decision combines both rather than choosing.
5. **Context.** none.
6. **Certainty.** Inferred: the lead claim is corroborated by one dated study (L1550); the five practices rest on maintainer practice alone.
7. **Flags.** none (F8 settled: both practices, the pitfall catalogue and no blanket search-and-replace, catch defect classes that review misses, which is the node's purpose; OPERATION.FEEDBACK links here rather than holding them).

Constraints: MUST data-dependent code be exercised on production-shaped data before it ships; MUST a platform limit that fails silently have a check; MUST a pitfall found twice be catalogued. Links: Requires BEHAVIOUR.2 (static layer first); stack pointers L278 (PostgreSQL identifiers over 63 bytes), L274 and L277 examples (PostgreSQL); routing objection L275 kept (not OPERATION.INCIDENTS).

---

## ASSURANCE.CONTRACTS Interfaces and Contracts

Intent (sharpened): which mechanism guarantees that an interface stays compatible for its consumers.

1. **Decision.** Compatibility has a definition (CONTRACTS.1), is verified between independently released components by contract tests rather than shared integrated environments (CONTRACTS.2), and each interface has one machine-readable source of description from which docs, stubs and tests derive, with an automated diff catching breaking changes (CONTRACTS.3). Outcome: a change to an interface cannot silently break a consumer.
2. **Grounds.** Roll-up of CONTRACTS.1 to .3 (18 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable (roll-up).
5. **Context.** Number and reach of consumers and the independence of release cadences move CONTRACTS.1 and .2.
6. **Certainty.** Grounded as a roll-up for the definition and the contract-test principle; inferred for the style choices.
7. **Flags.** none (F6 settled at CONTRACTS.1).

Links: children CONTRACTS.1 to .3; Requires RULES.3 (a blocking diff); CONSTRUCTION.BOUNDARY realizes contracts in code.

### ASSURANCE.CONTRACTS.1 What Counts as Compatible

Intent (sharpened): what the producer promises and which changes break it, so that compatibility has a definition to be checked against.

1. **Decision.** A producer declares its public interface precisely and defines compatibility: additive change is compatible, and removal, rename, type change, default change and behavioural change are breaking within a major version. A breaking change is never silent. This node holds which evolution policy a provider follows, by consumer reach and artifact kind: (a) few, in-house, reachable consumers: additive and backward-compatible by default, a breaking change coordinated with every consumer and deployed together, no version numbers, a dated change log per unit; (b) many, external or independently released consumers: for an installed artifact (library), semantic versioning with deprecation through at least one minor release before removal in a major; for a running service, a breaking change ships as a new major version served alongside the old one for a stated deprecation window; (c) for an infrastructure-like API with a large consumer base and the funds to carry old behaviour, an indefinitely compatible, date-pinned surface (L353 b). L353 is a row of this node; its (a) "few or controlled" is read as external consumers that are few or bound by contract, the explicit-major branch. The consumer side (read the promise, prefer stated notice, consume deprecation signals, pin the version) stays on OWNERSHIP.SERVICES.2. Because users depend on all observable behaviour (Hyrum's Law), automated tests detect new implicit dependencies but cannot remove them, so API change is planned accordingly. Outcome: a consumer can tell what will and will not break.
2. **Grounds.** Semantic versioning, precise public API, deprecation window (L060; REG-030); definition of breaking change (L352; REG-204); Hyrum's Law (L105; REG-071); the maintainer's additive-plus-coordination practice serves cost of ownership and wins with few reachable consumers (L295; REG-181), while explicit versioning serves consumer independence and exit risk (L295 alternative a); the service and infrastructure-API cases come from L353.
3. **Positions.** P1 semantic versioning with deprecation. P2 additive is compatible, the rest breaks. P3 Hyrum's Law. P4 explicit versioning (consumers choose when to move). P5 maintainer: additive, coordinated, no version numbers, dated change log. P6 (L353) the choice by consumer reach and artifact kind: major version served alongside the old for a running service, indefinitely compatible date-pinned surface for an infrastructure-like API.
4. **Rejected.** P5 as the general rule: it cannot hold when consumers release independently or are external, since a simultaneous deploy is then impossible (conflict with L102 and partial tension with L060); best, and chosen, for few in-house consumers reachable by review and conversation. P4 for every interface: best for many or external consumers; costly (multiple live versions) where consumers are few. The indefinitely compatible, date-pinned surface for every provider: best only with a large consumer base and the funds to carry old behaviour (L353 b).
5. **Context.** Number and reach of consumers and artifact kind (L295, L353): many, external or independently released consumers, explicit versioning with a deprecation window (semantic versioning for an installed artifact, a new major version served alongside the old for a running service); few, in-house, reachable consumers, additive evolution with coordinated deploy, no version numbers; an infrastructure-like API with a large consumer base and the funds, a date-pinned surface. A single-version service deployed as one unit is compatible with the maintainer's practice (L135, coverage check).
6. **Certainty.** Grounded for the definition of breaking change and deprecation (T1/T2 consensus); inferred for the consumer-count threshold (no numeric boundary in any row) and for the mapping of artifact kind to policy; P5 inferred (maintainer practice, public practice contested).
7. **Flags.** none (F6 settled: the maintainer's "no version numbers" holds for few, in-house, reachable consumers only).

Constraints: MUST the public interface be declared; MUST a breaking change be coordinated or deprecated, never silent. Links: OWNERSHIP.SERVICES.2 (J1) keeps only the consumer side and points here for the policies; EVOLUTION.DECOMMISSION.4 points here for the indefinitely compatible case (X7, which supersedes X3); Conflicts CONTRACTS.2 (L295 against L102; resolved by the consumer-reach context); CONSTRUCTION.BOUNDARY, OWNERSHIP.CONTAINMENT for the consumer side.

### ASSURANCE.CONTRACTS.2 Contract Tests

Intent (sharpened): how compatibility between independently released components, and between a test double and the real service, is verified.

1. **Decision.** Compatibility between independently released components is verified by contract tests, so teams deploy autonomously without relying on a shared integrated environment; every double of an external service is backed by a contract test against the real service, run on the rhythm of the supplier's changes (for example daily), whose failure triggers a realignment task and possibly a conversation with the supplier and need not break the build. Use consumer-driven contracts where a provider serves known consumers under internal control, and provider-side schema validation where consumers are unknown and a published specification is needed; the two answer different questions (a schema describes all possible states and catches provider drift, a consumer contract covers only what the consumer uses and is replayed against the provider), so a provider with known consumers uses both. Outcome: independent release is safe.
2. **Grounds.** Contract tests instead of shared integrated environments (L102, L1186; REG-044, REG-046, REG-053, REG-070); consumer-driven contracts' precision and the cost (hidden coupling made explicit, risk of eroding conceptual integrity) (L103, L1281; REG-044, REG-053, REG-1152); both for different questions (L1282; REG-053, REG-1157); contract tests on doubles on the supplier's rhythm (L104, L1283; REG-054, REG-070).
3. **Positions.** P1 contract tests instead of shared environments. P2 consumer-driven contracts. P3 provider schema validation. P4 use both. P5 single-team application: decide whether its own client and server interfaces need consumer-driven tests. P6 contract-test every double on the supplier's rhythm.
4. **Rejected.** P2 alone for unknown consumers: cannot know what they use; best where consumers are many and under internal control. P3 alone for known consumers: shows only possible drift, not whether this consumer still works; its lower setup cost and published spec win for unknown consumers (strongest version not independently sourced, open). Shared integrated environments for compatibility: best only when all consumers deploy together as one unit (the maintainer's single-version case, L295, L135).
5. **Context.** Number of consumers and independence of release cadences: the more consumers or independent cadences, the stronger the case for consumer-driven contracts (L1187); a single-team application whose client and server always deploy together, with no old client left in use, verifies its own seam with integration tests and the description diff of CONTRACTS.3, without consumer-driven contracts; where old clients stay in use after a server deploy (cached web clients, installed applications), client and server release independently in effect and the independent-release rule applies. Doubles of external services follow the contract-test rule in both cases.
6. **Certainty.** Grounded for P1 and P6 (T2, consensus or majority) and P4 (T1 vendor plus T2); inferred for P5 (L1187 open; the test that decides is whether an old client can stay live, which follows from the node's own principle); contested for the style choice, resolved by the context of known versus unknown consumers.
7. **Flags.** none (open point on single-team applications recorded in Certainty; decided, inferred).

Constraints: MUST a double of an external service have a contract test against the real service; MUST a contract-test failure create a realignment task. Links: Conflicts CONTRACTS.1 (L295 against L102; resolved there); BEHAVIOUR.3 (cross-service tests); OWNERSHIP.CONTAINMENT, OWNERSHIP.SERVICES for rented services.

### ASSURANCE.CONTRACTS.3 One Source of Description

Intent (sharpened): where the description of an interface originates so that documentation, stubs and tests derive from it and a breaking change is caught mechanically.

1. **Decision.** Each interface has one machine-readable description from which the reference documentation, client and server stubs, types and tests are derived, never hand-copied. The description is linted in CI against a team ruleset, and CI diffs it against the main-branch version and fails on incompatible change; since the diff covers the description only, behaviour and semantics still need contract tests. The description originates in a typed model (code-first, the generated description is a build artifact committed or checked and never hand-edited) when one team owns both ends, and is authored first (design-first) when independent consumers depend on it; the team records where the chain of types starts (storage schema, server models or the description file), using one class for table and validation in simple CRUD and separate storage, input and output models once the interface shape differs from storage. Outcome: docs, stubs and tests cannot drift from the interface.
2. **Grounds.** One description as single source (L220; REG-147, REG-164); lint (L221; REG-158); breaking-change diff (L222, L1284; REG-160, REG-1158); code-first with generated artifact (L1271; REG-1150, REG-1154) against design-first (Zalando, OpenAPI Initiative flag generated descriptions as incomplete); chain start and model separation (L1277; REG-1150, REG-1154, REG-1159, REG-1160).
3. **Positions.** P1 derive from one description, origin undecided. P2 code-first. P3 design-first. P4 choose and record the chain start; one class against separate models. P5 lint in CI. P6 diff in CI.
4. **Rejected.** Hand-maintained duplicates of the description: best never. Code-first for independent consumers: generated descriptions are flagged as incomplete; best for one team owning both ends. Design-first for one team owning both ends: authored description adds a second thing to keep in sync; best for independent consumers. One class for table and validation once the interface shape differs from storage: couples storage to the interface.
5. **Context.** Who owns both ends: one team, code-first; independent consumers, design-first (L1271). Complexity of the interface shape against storage moves the model separation (L1277).
6. **Certainty.** Grounded for one description (REG-147 T1 plus REG-164 T3); lint and the CI diff grounded as tool capability only (REG-158, REG-160, REG-1158, all T3 tool pages), "CI blocks" inferred; inferred for the origin condition (one row marked the condition inferred), the "should" of lint, and the "description only" limit; contested between code-first and design-first.
7. **Flags.** none.

Constraints: MUST the description have one source; MUST a generated description not be hand-edited; MUST CI block an incompatible change in the description. Links: stack pointers L220 (OpenAPI for HTTP), L221 (OpenAPI, AsyncAPI, Spectral), L222 (OpenAPI 3, openapi-diff), L1284, L1271, L1277 (restated neutral); TRANSVERSE.DOCS holds the authoring of reference documentation (MD-03); requires RULES.3.

---

## Flags raised (11), status after the final pass

- F1 (BEHAVIOUR.7, RULES.1): the maintainer's rollback on shared or production-sized data (L265) contradicts L111 (rebuild state, not clean up). Decided: disposable store by default, rollback boundary only under its stated condition; whether it must exclude production itself needs the maintainer. [settled: R15, R26, X5]
- F2 (RULES.4): L136 says "independent human check"; MD-02 says who does the work is not a principle. Decided as independence plus a named accountable person; no row covers a team of one. [maintainer point 1, default applied, open in the Certainty of RULES.4]
- F3 (BEHAVIOUR.1): the maintainer's practice may lack an automated trigger for the suite (L331, open); the decision, self-testing code on every change, contradicts it if confirmed. [settled: R28]
- F4 (BEHAVIOUR.5, BEHAVIOUR.1): L080 reads as test-first; L101 says ordering is contested. Decided: ordering by context, existence and fail-first for fixes required. [settled: R29]
- F5 (BEHAVIOUR.7): real records in test data can carry personal data, L266 is silent; L268 and L272 are PostgreSQL stack pointers and d8, d9 are realization practice inside an assurance node. [settled: R22]
- F6 (CONTRACTS.1): the maintainer's "no version numbers" (L295) holds only for few reachable in-house consumers; confirm it is not meant for external interfaces. [settled: R30, X7]
- F7 (RULES.2, RULES.1): numeric defaults (ten minutes, 1%, 10%, 95%) are one organisation's or one source's figures. [closed by review]
- F8 (BEHAVIOUR.8): L275 and L276 are learning and editing practices kept here by routing; may belong in OPERATION.FEEDBACK or CHANGE_FLOW. [settled: R31]
- F9 (ASSURANCE): the L1 claim covers three of nine L2 nodes; re-roll in wave 3 after J3 and J4. [still open: wave-3 re-roll, X2, R32]
- F10 (BEHAVIOUR.6, resolved): the 80% statement floor sits in SECURITY.3 (row L1126, P4), not SECURITY.4; J3 deferred it here and BEHAVIOUR.6 now decides it (no coverage floor, security code included; conformance minimum only where a baseline mandates it); residual for the maintainer: a mandated baseline. [settled: R21, X1]
- F11 (RULES.3): the claim "a skipped required check is a failure" rests on one platform fact (REG-114); other platforms may differ, the principle holds regardless. [closed by review]

## Review applied

Review fixes applied: 14 of 14. Flag findings R15 to R32 are not acted on (final Opus pass), except that R21 (F10) is settled by the coordinator's decision recorded in BEHAVIOUR.6.

- R01 applied: RULES.1 Grounds reworded (74% of order-dependent flaky tests were fixed by cleaning shared state; async waits 45%, 74 of 161 classified fixes).
- R02 applied: "T3" tier word removed for REG-048 in RULES.1 and BEHAVIOUR.4 (single source, one organisation's figures).
- R03 applied: the risk tier for post-merge review moved into the RULES.4 Decision; Context and Rejected aligned; tier conditions marked inferred.
- R04 applied: REG-1042 dropped for L1051; P3 and P4 certainty restated as one T1 vendor source (REG-1038), no consensus claim.
- R05 applied: "types as first test layer" marked inferred in BEHAVIOUR.2 Certainty; warnings and linter MUST stay grounded.
- R06 applied: BEHAVIOUR.3 outcome reworded (confidence chosen per unit of time and cost, mix recorded).
- R07 applied: BEHAVIOUR.4 names the twelve properties as the judging aid in Decision and Rejected.
- R08 applied: BEHAVIOUR.6 points to BEHAVIOUR.1 for "detection, not execution"; restated outcome clause removed.
- R09 applied: F10 now names SECURITY.3 (row L1126), in the node Flags and the end list.
- R10 applied: BEHAVIOUR.7 constraint scoped to mutating automated tests on shared or production-sized data.
- R11 applied: d2 points to TRANSVERSE.PRIVACY; Certainty states REG-1106 is one framework's documentation plus L111.
- R12 applied: BEHAVIOUR.8 Grounds say the study corroborates only that static checks miss a run-time class.
- R13 applied: BEHAVIOUR.8 points to RULES.2 for the 49-problems figure instead of restating it.
- R14 applied: CONTRACTS.3 Certainty restated (REG-147 T1; lint and diff as T3 tool capability; "CI blocks" inferred).
- Coordinator decision (R21, F10) applied: BEHAVIOUR.6 decides the coverage floor in full (none applies, security-relevant code included; the L1126 80% statement floor added as P8 and rejected, best as a conformance minimum where a baseline mandates it); deferral to J3 dropped; J3 points here.

## Final pass applied

Resolutions (final_pass/resolutions.md, section J2):
- R15, R26 (F1): applied. RULES.1 Decision, Positions P8 and Rejected P8 as stated; BEHAVIOUR.7 unchanged in substance, d1 per X5.
- R16: applied. RULES.4 tier sentence, Rejected first sentence ("Ship" with no review added), Certainty (tier conditions grounded in REG-098, rejection reason inferred).
- R17: applied. BEHAVIOUR.1 Decision and Constraint, with the evidence being the tests in each change.
- R18: applied through X4 (below).
- R19: applied. BEHAVIOUR.3 first sentence replaced; the rest unchanged (one repeated sentence about interactions and user-interface code left as it was, a redundancy only); Certainty names the inferred mapping.
- R20: applied. BEHAVIOUR.5 Decision clause and Constraint; the reduced-scope mode is one example.
- R21 (F10): applied, unchanged in substance. BEHAVIOUR.6 Flags cleared with the NIST IR 8397 ground and the MD-05 deferral recorded.
- R22 (F5, second half): applied. BEHAVIOUR.7 keeps d1, d2, d3, d7, d9 (d4 a stack pointer only); d5, d6, d8 moved to BEHAVIOUR.4 with their positions (P10 to P12), rejected line, context, stack pointer L272 and inferred certainty.
- R23: applied. BEHAVIOUR.8 first sentence and Constraint.
- R24: applied through X7 (below).
- R25: applied. CONTRACTS.2 Context second clause and Certainty.
- R27 (F2): applied as the maintainer default. RULES.4 Decision carries the default text merged with the R16 tier sentence; Certainty carries the open point.
- R28 (F3), R29 (F4), R30 (F6), R31 (F8): applied, unchanged in substance; flags cleared (R30: scope detail added by X7).
- R32 (F9): not applied, by design: the ASSURANCE re-roll is wave 3 (X2); F9 stays on the ASSURANCE node.
- Closed by the review (F7, F11): flags cleared.

Cross-unit lines (cross_unit_fixes.md, Units naming J2):
- X1: applied, nothing to change in this unit: BEHAVIOUR.6 already decides the coverage floor and states no deferral; J3 points to it.
- X2: not applied here: the ASSURANCE L1 node is re-rolled in wave 3 from all nine L2 nodes (F9 stays open).
- X3: superseded by X7; no change.
- X4: applied. RULES.1 holds the block-or-advise rule and its budget Constraints; BEHAVIOUR.2 Decision, Grounds and Constraint use the stated split. SECURITY.2 is J3's.
- X5: applied. BEHAVIOUR.7 d1 reads as stated and points to AVAILABILITY.3 for load and locks (a J4 node); Links record it.
- X7: applied. CONTRACTS.1 holds the policies by consumer reach and artifact kind, L353 as a row (P6), Context, Rejected, Certainty, Links. The edits in OWNERSHIP.SERVICES.2, EVOLUTION.DECOMMISSION.3 to .5 are other units'.
- X13: applied. BEHAVIOUR.5 holds "a gap found becomes a test" and points to REG-228 as cited by AVAILABILITY.3; AVAILABILITY edits are J4's.
- X14: applied. RULES.4 Rejected holds the reason (inferred); CHANGE_FLOW.REVIEW.1 points here (J6's edit).
- Lines not naming J2 (X6, X8 to X12): not in scope.

Nodes added: none (this unit's resolutions create no node).

Flags still open: F9 (ASSURANCE, wave-3 re-roll); the maintainer point on ASSURANCE.RULES.4 (can an automated reviewer be the independent check), default applied, open in its Certainty.
