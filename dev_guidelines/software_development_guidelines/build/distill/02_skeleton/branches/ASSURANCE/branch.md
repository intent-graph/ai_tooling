# Branch ASSURANCE: tree and node records

Refinement of the L1 branch ASSURANCE of the skeleton, below its nine L2 nodes (`../../tree_l2.md`). Rules that bind: `../../../target_hierarchy.md` and `../../../maintainer_decisions.md` (MD-01 to MD-07). No verdict, no ranking, no merging or editing of ledger rows: every record lists the competing positions for the judges. Rows are attached to the L3 node of their cluster; an L2 node with L3 children holds `Rows: -` (roll-up). Rows are cited by ledger id (L001-L460, L1001-L1289, L1501-L1565) and sources by register id (REG-nnn). The maintainer's codified practice (source MAINT-S01, REG-181, not citable) appears as a named position `Maintainer` on its node. Rows marked `origin: judged in the JavaScript guideline` keep their prior verdict as one position, never as the decision.

Pinned:
- Nodes: 54 (L1 1, L2 9, L3 44).
- Rows attached: 241 of 241; unattached: 0; attached twice: 0.
- Routing objections: 3 (listed at the end; 7 were raised, 4 resolved by moving the row, see `../../objections/resolution.md`).
- Context variables: added only where a row itself says the best practice moves with them, each quoting the row id (MD-02).

## Tree

```text
ASSURANCE Assurance
ASSURANCE.RULES Rules Common to Every Property
  ASSURANCE.RULES.1 Trustworthy Signal
  ASSURANCE.RULES.2 Placement and Feedback Speed
  ASSURANCE.RULES.3 Gates That Cannot Be Skipped
  ASSURANCE.RULES.4 Independent Review That Binds
  ASSURANCE.RULES.5 One Bar and Evidence for Every Change
ASSURANCE.BEHAVIOUR Behaviour
  ASSURANCE.BEHAVIOUR.1 What the Suite Must Promise
  ASSURANCE.BEHAVIOUR.2 Static Layer
  ASSURANCE.BEHAVIOUR.3 Test Level Mix
  ASSURANCE.BEHAVIOUR.4 Test Construction
  ASSURANCE.BEHAVIOUR.5 Tests Driven by Change
  ASSURANCE.BEHAVIOUR.6 Measuring Adequacy and Probing for Faults
  ASSURANCE.BEHAVIOUR.7 Tests Without Durable Effect on Data
  ASSURANCE.BEHAVIOUR.8 Defect Classes That Survive Review
ASSURANCE.CONTRACTS Interfaces and Contracts
  ASSURANCE.CONTRACTS.1 What Counts as Compatible
  ASSURANCE.CONTRACTS.2 Contract Tests
  ASSURANCE.CONTRACTS.3 One Source of Description
ASSURANCE.DATA_INTEGRITY Data Integrity Under Change
  ASSURANCE.DATA_INTEGRITY.1 Where Integrity Rules Live
  ASSURANCE.DATA_INTEGRITY.2 Guarding Bulk and Destructive Operations
  ASSURANCE.DATA_INTEGRITY.3 Layered Protection and Deletion Form
  ASSURANCE.DATA_INTEGRITY.4 Derived Data Sync and Staleness
  ASSURANCE.DATA_INTEGRITY.5 Checking Old Against New and Rolling Out Checks
ASSURANCE.DOCS_SYNC Documentation in Sync
  ASSURANCE.DOCS_SYNC.1 Delivery with the Change
  ASSURANCE.DOCS_SYNC.2 Gates and Review of Documentation
  ASSURANCE.DOCS_SYNC.3 Ownership, Freshness and Single Source
  ASSURANCE.DOCS_SYNC.4 Mechanical Documentation Checks
ASSURANCE.SECURITY Security
  ASSURANCE.SECURITY.1 Verification Depth and Design Review
  ASSURANCE.SECURITY.2 Stage Placement and Blocking Policy
  ASSURANCE.SECURITY.3 Verification Techniques
  ASSURANCE.SECURITY.4 Static and Scheduled Analysis Practice
  ASSURANCE.SECURITY.5 Secrets and Consumed Code
  ASSURANCE.SECURITY.6 Enforced Limits on Automation and Access
  ASSURANCE.SECURITY.7 Closing the Loop on Findings
ASSURANCE.PERFORMANCE Performance
  ASSURANCE.PERFORMANCE.1 Targets and Budgets
  ASSURANCE.PERFORMANCE.2 Load Test Design
  ASSURANCE.PERFORMANCE.3 When Tests Run and Baselines
  ASSURANCE.PERFORMANCE.4 Testing in Production for Performance
  ASSURANCE.PERFORMANCE.5 Measurement Before Optimization
ASSURANCE.AVAILABILITY Availability and Recovery
  ASSURANCE.AVAILABILITY.1 Tolerating a Degraded Dependency
  ASSURANCE.AVAILABILITY.2 Protecting Remote Calls
  ASSURANCE.AVAILABILITY.3 Verifying Resilience Under Real Conditions
  ASSURANCE.AVAILABILITY.4 Proving Restore
  ASSURANCE.AVAILABILITY.5 Exercising Recovery
ASSURANCE.ARTIFACT Artifact Integrity
  ASSURANCE.ARTIFACT.1 Build Provenance and Match to Source
  ASSURANCE.ARTIFACT.2 Protected Mainline Binds Every Actor
```

## How to read a record

`Rows` are attached here and nowhere else. `P1, P2...` are competing practices as the rows record them; the order is not a ranking. A position lists its strongest argument, the force it serves, and the condition under which the rows say it wins, with row and register ids. "No competing position recorded" means the rows hold one practice. `Links` carry only what a row states (`Requires`, `Conflicts`, `Refines`) plus the index links of the split topics (MD-03).

---

## ASSURANCE Assurance

Intent: for each property that must hold, which mechanism at which stage guarantees it, and runs on every change so that it stays true; the design was good, the testing was good, the review was trustworthy, what runs is what was reviewed.
Rows: - (roll-up of nine L2 nodes, 241 rows)
Forces in tension: speed of feedback, realism of the confidence, cost to build and maintain, flakiness, cognitive load (`../../../target_hierarchy.md`).

---

## ASSURANCE.RULES Rules Common to Every Property

Intent: where a check runs, what makes its signal trustworthy and fast, and what makes a review or a gate binding whoever authored the change.
Rows: - (roll-up, 31 rows)

### ASSURANCE.RULES.1 Trustworthy Signal

Intent: a failing check must mean a real defect, so that a pass can be believed and a finding is acted on.
Rows: L086, L109, L110, L111, L147, L1132, L1558, L1559, L1560, L1561 (10)
Positions (no verdict):
- P1 Quarantine non-deterministic tests in a separate suite outside the deployment gate, with a numeric cap and a time limit (source example: 8 tests, one week), then fix or delete. Argument: keeps the gate trustworthy while causes are found. Force: trust of the gate, delivery speed. Wins: flaky tests already exist. (L110; REG-054)
- P2 Remove flaky tests at once, no tolerance (the strict school, inferred from "do not tolerate"). Argument: a test that fails without a defect already destroys trust. Force: trust. Wins: not stated by the row. (L110, L109; REG-056)
- P3 Rerun only tests marked flaky (Google, from commenters, recorded as weak). Argument: keeps coverage while the flake is known. Force: delivery speed. (L110; REG-055)
- P4 Classify, retry or disable temporarily during investigation, treating flakes as pipeline defects. Argument: flakes erode trust as broken tests do. (L147; REG-085)
- P5 Prevent the cause rather than retry it away: isolate tests and rebuild state, poll or use callbacks instead of bare sleeps, wrap the clock, double remote services, shrink large tests; check new tests extensively when added (45% of studied fixes were asynchronous waits); clean shared state between tests (74%, 14 of 19, of order-dependent flakes in the study). Argument: nondeterminism has identifiable causes. Force: trust of the result. Origin: judged in the JavaScript guideline, prior position known, single T2 source, studies mostly Java. (L111, L1558, L1559, L1560; REG-051, REG-054, REG-1570)
- P6 Track the flaky rate and act when it approaches about 1% (one organisation holds about 0.15%; tests lose value near 1%; the only admitted threshold). Origin: judged in the JavaScript guideline, prior position risky, single T3 source. (L109, L1561; REG-048, REG-054, REG-056)
- P7 Keep the effective false-positive rate of static checks under a stated budget (below 10% at Google, about 5% achieved; a false positive is any finding the developer does not act on); remove or fix a noisy check. The row records the 10% as one organisation's policy, not a standard. SSDF asks for a human reviewing tool findings, consistent. (L086, L1132; REG-004, REG-052, REG-1086, REG-1092, REG-1099)
Links: Conflicts ASSURANCE.BEHAVIOUR.7 (coverage check: L265 contradicts L111).

### ASSURANCE.RULES.2 Placement and Feedback Speed

Intent: at which stage and level a check runs so that feedback is fast and each failure is caught as low as it can be, with several kinds of check combined.
Rows: L091, L121, L145, L112, L1183, L1538, L1546, L1550 (8)
Positions (no verdict):
- P1 Push each check as low as it can go; when a higher-level test finds a bug no lower-level test caught, add the lower-level test. Argument: cheaper, faster, precise location. (L091, L1183; REG-044, REG-072)
- P2 Keep feedback to minutes (about ten), trigger the build on every commit, fix a broken build first. (L112; REG-056, REG-057)
- P3 Gate on everything fast and reliable; run slower tests after merge and roll back on failure; accepts some loss of coverage (Google, about 95% of changes pass presubmit). Force: speed of feedback. Wins: very high change volume, a build cop, automatic rollback. (L145; REG-085)
- P4 Staged pipeline, later stages slower but more thorough and parallelized. Force: confidence. Wins: smaller change volume. DORA pitfall: tests over ten minutes. (L145; REG-057, REG-077, REG-107)
- P5 Decide per stage and per risk which analysis and test types are performed, and record the policy. (L121; REG-004)
- P6 Combine several kinds of check and never rely on one mechanism; write negative tests; dynamic checks find what static analysis misses (28 dynamic checkers found on average 49 problems per site over 200 sites in 2015, dated evidence). Origin: judged in the JavaScript guideline, prior position known, single-source. (L1550; REG-1561, REG-1564)
- P7 Layer controls so that no single control is relied on. Origin: judged in the JavaScript guideline, prior position inferred (single T2 source, a taxonomy). (L1538; REG-1554)
- P8 Defects people forget to look for are found by machines on every change, with a blocking result people trust. Origin: judged in the JavaScript guideline, part carved out at the split, prior position inferred. (L1546; no register id)
Context variables: change volume, build cop, automatic rollback (L145: P3 "wins: very high change volume, a build cop, automatic rollback"; P4 "wins: smaller change volume").
Links: Requires ASSURANCE.BEHAVIOUR.1 (L1550 requires L1552).

### ASSURANCE.RULES.3 Gates That Cannot Be Skipped

Intent: a rule that matters is enforced by an automated check that blocks the change, always runs and cannot be passed by being skipped.
Rows: L1216, L1234, L1562 (3)
Positions (no verdict):
- P1 Enforce module boundaries with automated checks, not convention alone (Shopify tooling; fitness functions). Certainty recorded: inferred. (L1216; REG-1117, REG-1119, REG-1134)
- P2 Build and evolve in small increments and make fit explicit as automated fitness functions, including performance, security and operability. (L1234; REG-1119, REG-1134)
- P3 A check changes behaviour only when failing it stops the merge: the gate always runs, and a skipped required check must not let a merge through (some platforms treat a skipped required check as passing). Origin: judged in the JavaScript guideline, prior position known, practice inferred from a platform fact. (L1562; REG-114)
Links: none from rows beyond the following. Required by ASSURANCE.BEHAVIOUR.2 and ASSURANCE.BEHAVIOUR.1 (L1547 and L1551 require L1562).

### ASSURANCE.RULES.4 Independent Review That Binds

Intent: a review is a trustworthy signal only when the reviewer is independent, someone is accountable, and the approval binds the exact content that ships.
Rows: L136, L143, L1043, L1046, L1047 (5)
Positions (no verdict):
- P1 Every change to mainline gets an independent human check (second reviewer, pair or equivalent) at or before integration, recorded on the platform. Dissent: Ship, Show, Ask keeps review for uncertain changes only. (L136; REG-083, REG-094, REG-098, REG-115, REG-116)
- P2 No external change approval board for per-change approval; meet segregation of duties through peer review, automated testing and monitoring, and treat changes by risk (DORA: no correlation of external review with lower failure rates, a negative effect on delivery speed). Against it: the external board of traditional regulated settings. Force: control and regulation against delivery speed. Whether a given regulation still requires a board was not read (open). (L143; REG-094)
- P3 A named person or role stays accountable for each change and able to explain and defend it; accountability attaches to the submitter, not to the tool. (L1043; REG-1035, REG-1037, REG-1040)
- P4 The approver is a different party from whoever authored, pushed or requested the change (mechanism recorded: GitHub). (L1046; REG-1036, REG-114)
- P5 An approval binds to the exact final content: new commits that change the diff invalidate earlier approvals (mechanism recorded: GitHub). (L1047; REG-114)
Links: index link CHANGE_FLOW.REVIEW (the practice of carrying out review).
Stack pointers: L1046, L1047 (GitHub).

### ASSURANCE.RULES.5 One Bar and Evidence for Every Change

Intent: every change meets the same bar for design, testing and review, and its completion is shown by evidence independent of the author.
Rows: L1042, L1045, L1051, L1052, L1053 (5)
Positions (no verdict):
- P1 Every change, whatever its author, meets the same bar for design, testing and review; generated change gets no exemption. (L1042; REG-1035, REG-1036, REG-1040)
- P2 Fix intent, scope, interfaces, out-of-scope items and the acceptance check before a change is produced. Certainty recorded: vendor guide and one DORA capability. (L1045; REG-1038, REG-1041)
- P3 Every change comes with an executable pass or fail check that does not depend on the author's own judgement. (L1051; REG-1038, REG-1042)
- P4 Completion is shown as evidence (test output, command and result, screenshot), not asserted. (L1052; REG-1038; single source)
- P5 Tests and the code they check come from independent contexts where practicable, so one set of assumptions does not validate itself. Certainty recorded: inferred, a vendor recommendation. (L1053; REG-1038)
Context variables: cost and speed of producing a change (L1045: "especially when production is cheap and fast").

---

## ASSURANCE.BEHAVIOUR Behaviour

Intent: which tests, types and static checks, at which level and stage, guarantee that the software does what is intended.
Rows: - (roll-up, 61 rows)

### ASSURANCE.BEHAVIOUR.1 What the Suite Must Promise

Intent: what an automated suite must let a team conclude, who owns it, and what is recorded.
Rows: L080, L081, L082, L083, L122, L123, L331, L1551, L1552 (9)
Positions (no verdict):
- P1 Self-testing code: the suite can be run at any time and a pass means no substantial defects; without it there is no real continuous integration. (L081; REG-056, REG-057, REG-063)
- P2 Everything the team does not want to break (behaviour, performance, accessibility, security) has a test (the strict form, Google). Fowler's weaker form: enough tests to change the code confidently, scaled to risk. Force: confidence. Wins (strict): high criticality, many consumers. (L082; REG-048, REG-064)
- P3 Tests are written first to make change safe and speed iteration, bug-catching secondary; passing tests do not prove reliability, failing tests prove its absence. (L080, L083; REG-048, REG-063, REG-067)
- P4 Keep a written policy that new major functionality gets automated tests, evidence that recent changes followed it, and a suite invocable in the language's standard way; adequacy is judged by what tests detect, not what they execute. Origin: judged in the JavaScript guideline, prior position known, single-source (OpenSSF criteria). (L1551, L1552; REG-1563)
- P5 Developers own authoring and maintaining automated acceptance tests; testers add exploratory and usability testing and curate suites. Record results, root causes and triage in the workflow; account for the target production stack in test plans. (L122, L123; REG-056, REG-004)
- P6 Maintainer: the doctrine states how a function test is built and run but not who runs the suite, when, on what trigger, nor how regressions are caught across changes; the practice in force appears to be on-demand runs by a human or agent. Recorded open (inferred absence); if confirmed it contradicts L081, L106 and L144 (the last is outside this branch). (L331; REG-181)
Context variables: criticality and number of consumers (L082: where the strict form wins).
Links: Requires ASSURANCE.RULES.3 and ASSURANCE.RULES.1 (L1551 requires L1562 and L1558).

### ASSURANCE.BEHAVIOUR.2 Static Layer

Intent: which type, lint and analysis checks run on every change as the cheapest layer, and how strictly.
Rows: L084, L085, L087, L088, L1054, L1547, L1548, L1549 (8)
Positions (no verdict):
- P1 Enforce types as the first test layer (Gao et al., Dodds). Force: correctness, documentation. Wins: large, long-lived code bases. (L084; REG-047, REG-065, REG-075)
- P2 Optional or gradual typing (mypy): annotate incrementally, keep an escape hatch, no rewrite. Force: delivery speed, adoption on existing code. (L084, L085; REG-065, REG-075)
- P3 Tests alone suffice (no source read holds it strongly; recorded as the unrepresented minority, open). (L084)
- P4 Build with warnings enabled and treated as errors, use analysis tools continuously (majority); enable a linter or safe language mode and address its warnings (OpenSSF passing criteria MUST); run at least one analyser beyond compiler warnings before a major release. Origin of the last two: judged in the JavaScript guideline, prior position known, single-source. (L088, L1548, L1549; REG-004, REG-1563)
- P5 Analysis incremental (changed files), new issues first, shown in code review, with automated fixes. Force: adoption, fast feedback. (L087; REG-052)
- P6 Static and complexity gates on every change with the trend of warnings and complexity watched, against volume-driven drift. Certainty recorded: one observational study, practice inferred. (L1054; REG-1035, REG-1046)
- P7 Every project analyses its code without running it and acts on what is reported. Origin: judged in the JavaScript guideline, prior position known. (L1547; no register id)
Links: Requires ASSURANCE.RULES.3 (L1547 requires L1562).
Stack pointers: L085 (Python mypy, TypeScript and Flow gradual typing).

### ASSURANCE.BEHAVIOUR.3 Test Level Mix

Intent: which proportion of small, integrated and end-to-end tests gives the confidence at the cost the team can bear.
Rows: L089, L090, L092, L093, L117, L1182, L1188 (7)
Positions (no verdict):
- P1 Pyramid, unit-heavy (Google, Fowler): many small fast tests, some coarser, very few high-level; example ratio 70/20/10, team-specific. Force: speed of feedback, precise failure location. Wins: logic-dense code, large teams, slow environments. (L089, L090, L1182; REG-044, REG-045, REG-048, REG-072)
- P2 Honeycomb, integration-heavy (Spotify): few implementation-detail tests, ideally no integrated tests. Force: refactor-safety, migrations without test edits; cost: seconds instead of milliseconds. Wins: microservices where complexity lives in interactions. (L090; REG-045, REG-046)
- P3 Trophy, static plus integration widest (Dodds): the more tests resemble use, the more confidence. Force: confidence per unit time. Wins: UI and front-end applications. (L090; REG-047)
- P4 All three agree the exact numbers matter less than fast, reliable, meaningful-failure tests; the proportions are a decision each team records. (L090)
- P5 End-to-end tests to a bare minimum, a few on critical journeys, because slow, flaky and costly to debug. Counter-note: if high-level tests are fast, reliable and cheap to change, lower-level tests are unnecessary (Fowler). Wins (minimal): E2E slow or flaky; loses where cheap and stable. (L092, L1188; REG-044, REG-045, REG-048, REG-072)
- P6 Add larger tests where fidelity matters (configuration, load, cross-service behaviour); system under test from hermetic single process (speed, determinism) to multimachine or shared environments (fidelity, at flakiness and conflict cost). (L117; REG-051)
- P7 Describe tests on separate axes, size and scope; end-to-end, UI and customer-facing are independent characteristics. (L093; REG-048, REG-072)
Context variables: where complexity lives, code logic density, team size, environment speed (L090).

### ASSURANCE.BEHAVIOUR.4 Test Construction

Intent: what a unit is, what a test observes, what stands in for collaborators, and how test code is kept readable and cheap to maintain.
Rows: L094, L095, L096, L097, L098, L099, L100, L1184, L1189, L1554 (10)
Positions (no verdict):
- P1 "Unit" is team-defined: state whether units are solitary (collaborators doubled) or sociable (real collaborators) and where tests start and stop. Contested. (L094; REG-046, REG-061)
- P2 Test observable behaviour through public interfaces, one test per behaviour; the ideal test never changes unless requirements change. (L095, L1554; REG-046, REG-048, REG-049, REG-068)
- P3 Classical: real objects unless awkward; catches integration errors, survives refactors. Wins: frequent refactoring, small object graphs. Fowler is a convinced classicist but many skilled practitioners prefer the other. (L098; REG-050, REG-061)
- P4 Mockist: mock every collaborator with behaviour; failures local to the unit, simpler fixtures, outside-in design with role interfaces. Wins: when driving design from outside in and collaborators are costly to build. (L098, L096; REG-062)
- P5 State verification over interaction verification except for state-changing calls not otherwise observable; the mockists hold interaction verification promotes need-driven design and isolates failures. (L096; REG-049, REG-050, REG-062)
- P6 Real implementations when fast, deterministic and simple, otherwise a fake owned by the team owning the real thing, mocks and stubs last (over-mocking: tests easy to write, costly to maintain, rarely finding bugs). An 80/15/5 mix of unit, integration and end-to-end is acceptable only with Google-like test infrastructure. Origin of the mix: judged in the JavaScript guideline, prior position risky, single T3 source. (L097, L1554; REG-049, REG-050, REG-048)
- P7 Integration tests run against a real backing service of the production kind (engine and version), not mocks or a different engine. (L1184; REG-044, REG-1106, REG-1109)
- P8 Tests are code: readable and DAMP over strictly DRY, no loops or conditionals, one condition per test, arrange-act-assert; the same care as production code. (L099, L1189; REG-044, REG-049)
- P9 Judge a test by trade-offs among twelve properties; no test needs all, some pairs conflict (predictive against fast). (L100; REG-068)
Stack pointers: L1184 (origin stack postgres, restated neutral).

### ASSURANCE.BEHAVIOUR.5 Tests Driven by Change

Intent: which events oblige a test to be written, and in which order.
Rows: L101, L106, L107, L316 (4)
Positions (no verdict):
- P1 Whether test-first is required is a team decision; all principals agree on self-testing code and disagree on whether test-first mechanics deliver it. Beck: context decides, wins for compilers, API design, tangled interfaces. DHH: over-prescriptive, "test-induced design damage", serves cost of ownership. Fowler: valuable in some contexts. DORA: evidence is of test automation in general, not test-first ordering (inferred). Contested. (L101; REG-056, REG-063, REG-064)
- P2 Convert every reported bug into a test that fails first and passes after the fix, building the regression suite from operational experience. (L106; REG-004, REG-067, REG-072)
- P3 Before changing poorly understood code, pin its actual behaviour with characterization tests. (L107; REG-063, REG-073)
- P4 Maintainer: test a scheduled job before scheduling it by calling its unit directly and in a reduced test mode, then inspect the data. (L316; REG-181)

### ASSURANCE.BEHAVIOUR.6 Measuring Adequacy and Probing for Faults

Intent: how the power of a suite to detect faults is measured and probed rather than assumed.
Rows: L113, L114, L115, L116, L1553, L1555, L1556, L1557 (8)
Positions (no verdict):
- P1 Coverage finds untested code and is not a target or quality score (Fowler, Google, PIT); easy to inflate. Wins: mature teams. One study (31,000 suites, five large Java systems) finds correlation with suite effectiveness low to moderate once size is controlled. Origin of the study row: judged in the JavaScript guideline, prior position known, transfer inferred. (L113, L1553; REG-048, REG-059, REG-074, REG-1565)
- P2 A coverage floor or threshold (a minimum, not a goal). Force: management visibility. Wins: low-trust or fast-growing teams (inferred from wording). (L113; REG-048)
- P3 The OpenSSF passing criteria suggest covering most or all branches, as a suggestion not a numeric target; wins for a project adopting those criteria; compatible with using coverage to locate unexecuted code. (L1553; REG-1563)
- P4 Mutation testing as the stronger measure, applied diff-based and selectively at scale (incrementally on changed code during review, mutants filtered): routine gate or review signal. Force: correctness. Wins: high-criticality code, mature suites. Evidence of benefit open (no effect size). (L114, L1556, L1555; REG-058, REG-074, REG-1566, REG-1567)
- P5 Skip mutation testing or run it offline (inferred). Force: cost. Wins: compute or noise dominates. (L114; REG-058)
- P6 Property-based testing for code with a describable input range; random inputs, shrinking, generators following the actual data distribution; properties beside the code only when a team wants them. Effectiveness inferred (no quantification). Origin: judged in the JavaScript guideline, prior position known, single T2 source. (L115, L1557; REG-060, REG-1568, REG-1569)
- P7 Fuzz input-handling code, continuously where possible; frameworks require it for security-relevant code. (L116; REG-004, REG-066)
Context variables: criticality and suite maturity (L114: "wins with high-criticality code and mature suites").
Stack pointers: L115 (Hypothesis in Python, equivalents elsewhere), L116 (OSS-Fuzz languages: C and C++, Rust, Go, Python, JVM, JavaScript, Lua).

### ASSURANCE.BEHAVIOUR.7 Tests Without Durable Effect on Data

Intent: how tests are run so that no test leaves a durable effect on shared or production-sized data, and how their data, configuration and verdicts are kept apart and self-reporting.
Rows: L265, L266, L267, L268, L269, L270, L271, L272, L273, L1185 (10)
Positions (no verdict):
- P1 A separate disposable data store per test run, never the production one, each test isolated (for example a transaction per test, rolled back). Argument: no shared state, no risk to real data. Force: isolation, speed of feedback. Wins: small dataset or cheap cloning. (L1185, L265; REG-1106)
- P2 Maintainer: run on shared or production-sized data behind a boundary guaranteed to be undone, reshaping data inside it and never committing, on any environment. Argument: real shapes exist only in real data and the dataset is too large to clone. Force: realism of confidence, cost of ownership. Wins: large, complex data whose shapes cannot be synthesized and a platform that can undo every effect. Coverage check: contradicts L111, partial tension with L119. (L265; REG-181)
- P3 Fixtures: synthetic fixtures or factories per test (explicit, hermetic; wins when the domain is small and shapes are easy to construct) against Maintainer: a curated, catalogued set of real records selected by queryable attributes, never invented rows or arbitrary production rows; a persistent new shape is feature work by a separate idempotent script. Force: confidence. (L266; REG-181)
- P4 Maintainer: choose the execution vehicle by risk and runner: read-only tests as plain queries; tests that can mutate run, when automated, as one atomic unit rolled back; an interactive open-transaction wrapper only for a human at the keyboard (readability; wins when a human supervises). (L267; REG-181)
- P5 Maintainer: where a normally completing block commits, a mutating test ends by raising an error whose message is the verdict, so every outcome rolls back. No competing position in the doctrine. (L268; REG-181)
- P6 Maintainer: a test reports its own verdict in a fixed, searchable shape carrying unit and scenario identity. (L269; REG-181)
- P7 Colocated tests beside the unit, one single-statement case each (change together, discoverable; wins when the tooling lacks a test tree) against a separate mirrored test tree (clean production artifacts, tooling support; wins when the language has a test runner). Maintainer holds the first. (L270; REG-181)
- P8 Maintainer: test configuration lives in a namespace disjoint from production context; production code never reads it. (L271; REG-181)
- P9 Maintainer: fixture values reused across a multi-statement test are named session-scoped variables set once at the top (less duplication; cost: untyped text, a footgun in one-statement contexts). (L272; REG-181)
- P10 Maintainer: make mutations conditional on an actual change so re-runs behave identically and write volume drops. (L273; REG-181)
Links: Conflicts ASSURANCE.RULES.1 (coverage check: L265 contradicts L111).
Stack pointers: L268, L272 (PostgreSQL anonymous blocks and custom configuration parameters).

### ASSURANCE.BEHAVIOUR.8 Defect Classes That Survive Review

Intent: which classes of defect pass review and deployment and fail only at run time, and which practices catch them.
Rows: L274, L275, L276, L277, L278 (5)
Positions (no verdict):
- P1 Static analysis and types catch part of the class (speed of feedback) against Maintainer: they do not catch these (name resolution deferred to execution, rare-data branches, range-checked narrowing casts, aggregates returning wider types, array functions fed null), so exercise every branch with production-shaped data and guard inputs always. Force: correctness. (L274; REG-181)
- P2 Maintainer: keep a pitfall catalogue indexed by error code or symptom, add an entry after any defect found twice. (L275; REG-181)
- P3 Maintainer: no blanket search-and-replace across a file with two syntactic contexts; anchor on context and re-check dependants. (L276; REG-181)
- P4 Maintainer: where public documentation is unclear about a platform behaviour a design relies on, verify empirically on a live instance and record the finding with its scope. (L277; REG-181)
- P5 Maintainer: where a platform silently truncates or coerces, make the limit a hard rule with a check. (L278; REG-181)
Stack pointers: L278 (PostgreSQL identifiers over 63 bytes); L274 and L277 examples are PostgreSQL.

---

## ASSURANCE.CONTRACTS Interfaces and Contracts

Intent: which mechanism guarantees that an interface stays compatible for its consumers.
Rows: - (roll-up, 18 rows)

### ASSURANCE.CONTRACTS.1 What Counts as Compatible

Intent: what the producer promises and which changes break it, so that compatibility has a definition to be checked against.
Rows: L060, L105, L295, L352 (4)
Positions (no verdict):
- P1 Declare the public API precisely, start at 0.1.0, deprecate through at least one minor release before removal in a major (semantic versioning). (L060; REG-030)
- P2 Additive change is compatible; removal, rename, type change, default change and behavioural change are breaking within a major version. (L352; REG-204)
- P3 Users depend on all observable behaviour (Hyrum's Law): broad automated tests detect new implicit dependencies but cannot remove them; plan API change accordingly. (L105; REG-071)
- P4 Explicit versioning: consumers choose when to move. Force: consumer independence, exit risk. Wins: many or external consumers. (L295 alternative a; REG-181)
- P5 Maintainer: evolve additively and backward-compatibly by default (new units, new parameters with defaults), coordinate breaking changes with every consumer and deploy together, no version numbers, a dated change log per unit. Force: cost of ownership. Wins: few in-house consumers reachable by review and conversation. Coverage check: contradicts L102, partial tension with L060. (L295; REG-181)
Context variables: number and reach of consumers (L295).
Links: Conflicts ASSURANCE.CONTRACTS.2 (coverage check: L295 contradicts L102).

### ASSURANCE.CONTRACTS.2 Contract Tests

Intent: how compatibility between independently released components and against test doubles is verified.
Rows: L102, L103, L104, L1186, L1187, L1281, L1282, L1283 (8)
Positions (no verdict):
- P1 Verify compatibility between independently released services with contract tests so teams deploy autonomously, instead of relying on shared integrated environments. (L102, L1186; REG-044, REG-046, REG-053, REG-070)
- P2 Consumer-driven contracts (contracts generated by consumer tests, the provider free to change what no consumer uses): precision on what is used, safe evolution. Wins: many consumers under internal control; fits a single enterprise or closed community; makes hidden coupling explicit without removing it and risks consumer demands eroding the service's conceptual integrity. (L103, L1281, L1186; REG-044, REG-053, REG-1152)
- P3 Provider-side schema validation: lower setup cost, a published specification for unknown consumers (inferred; the strongest version is not independently sourced, open). (L103; REG-044, REG-053)
- P4 Use both, for different questions: a schema describes all possible states, a consumer contract covers only what the consumer uses and is replayed against the provider. (L1282; REG-053, REG-1157)
- P5 For a single-team application, decide whether its own client and server interfaces need consumer-driven tests or whether schema checks plus a few such tests suffice (seams: client to server, calls to external services). Open: no source addresses a single-team monolith directly. (L1187; REG-053, REG-070, REG-1152)
- P6 Back every double of an external service with a contract test against the real service on the rhythm of the supplier's changes (for example daily), not on every commit; a failure triggers a realignment task and possibly a conversation with the supplier, and need not break the build. (L104, L1283; REG-054, REG-070)
Context variables: number of consumers and independence of release cadences (L1187: "the more consumers or independent release cadences, the stronger the case").
Links: Conflicts ASSURANCE.CONTRACTS.1 (coverage check: L295 contradicts L102).

### ASSURANCE.CONTRACTS.3 One Source of Description

Intent: where the description of an interface originates so that documentation, stubs and tests derive from it and a breaking change is caught mechanically.
Rows: L220, L221, L222, L1271, L1277, L1284 (6)
Positions (no verdict):
- P1 Derive interface reference from one machine-readable description so rendered docs, stubs and tests share a single source; whether it is written first or generated is deliberately not decided. (L220; REG-147, REG-164)
- P2 Code-first: a typed model is the source and the generated description is a build artifact committed or checked, never hand-edited (derived schema, less duplication). Wins: one team owning both ends. (L1271; REG-1150, REG-1154)
- P3 Design-first: the description is authored (Zalando, OpenAPI Initiative flag generated descriptions as incomplete). Wins: independent consumers. (L1271)
- P4 Choose and record where the chain of types starts (database schema, server models or the description file); one class for table and validation (simple CRUD) against separate table, input and output models (once the interface shape differs from storage). Contested, inferred. (L1277; REG-1150, REG-1154, REG-1159, REG-1160)
- P5 Lint the description in CI against a team ruleset. Certainty: capability grounded, "should" inferred. (L221; REG-158)
- P6 Diff the description between versions in CI and fail on incompatible changes; the diff covers the description only, so behaviour and semantics still need contract tests. (L222, L1284; REG-160, REG-1158)
Stack pointers: L220 (OpenAPI for HTTP), L221 (OpenAPI, AsyncAPI; Spectral), L222 (OpenAPI 3; openapi-diff), L1284 (HTTP; OpenAPI 3.0 and 3.1, restated neutral), L1271 and L1277 (Python and JavaScript examples, restated neutral).

---

## ASSURANCE.DATA_INTEGRITY Data Integrity Under Change

Intent: which mechanism guarantees stored data stays valid and in sync through change, including the checks during a data change.
Rows: - (roll-up, 19 rows)
Links: index link CHANGE_FLOW.DATA_CHANGE holds the procedures (batching, rehearsal); this node holds the which-mechanism rows (MD-03).

### ASSURANCE.DATA_INTEGRITY.1 Where Integrity Rules Live

Intent: which tier enforces the rules that must hold whatever writes the data.
Rows: L279, L1262, L1286 (3)
Positions (no verdict):
- P1 Invariants in the application domain layer: one place for logic, a richer language. Force: team cognitive load. Wins: a single application owns the store. (L279 alternative a)
- P2 Maintainer: integrity where all write paths converge (declared constraints, referential links, validation near the data) in addition to validation at the edge, because migrations, administrative tools and ad-hoc statements bypass application code; invalid states unrepresentable, failing fast. Force: correctness across several writers. Wins: several consumers and ad-hoc access. (L279; REG-181)
- P3 Split by kind: rules that must hold whatever application writes (keys, NOT NULL, foreign keys, row-local checks, atomic audit) in the database; workflow, policy and rules that change with product decisions in the application. The middle zone (triggers, functions, views) is where sources and database-first practitioners disagree. Contested, inferred. (L1262; REG-1139, REG-1140, REG-1143)
- P4 Constraints are the contract half that holds whichever code writes: mirror the application model's constraints against them, and name constraints explicitly so the application can map a violation to a stable contract error. Consensus; the semantics are grounded, the mirror and naming advice inferred. Moved here from `CONSTRUCTION.BOUNDARY`; see also L279 and L1262 (same node). (L1286; REG-1139)

### ASSURANCE.DATA_INTEGRITY.2 Guarding Bulk and Destructive Operations

Intent: how an operation whose scope can silently widen is stopped from doing so.
Rows: L280, L396, L414 (3)
Positions (no verdict):
- P1 Maintainer: a destructive or bulk operation with unbounded scope requires an explicit opt-in flag from its caller, plus validation of mandatory keys, key order and timestamp sanity. (L280; REG-181)
- P2 Lint migrations in CI against a rule list of unsafe operations and require an explicit assertion to override a rule. Argument: blocks DDL that locks or destroys. (L396, L414; REG-258, REG-259; T3, tools in the same niche)
Note: L414 states P2 as the nearest public form of P1; the row records it inferred, since the maintainer rule covers application-level bulk operations and the tools cover DDL.
Stack pointers: L396 (Postgres, Rails), L414 (Rails, Postgres tools).

### ASSURANCE.DATA_INTEGRITY.3 Layered Protection and Deletion Form

Intent: which layers protect data against destructive change, and in which form data is deleted so that recovery and integrity both hold.
Rows: L388, L416, L417, L1092, L1255, L1256 (6)
Positions (no verdict):
- P1 Defend in layers, because every single strategy eventually fails: a first layer that makes deletion reversible (soft deletion with a retention delay), a second of backups with tiered retention and locality, a third of early detection of corruption. (L417, L1092, L416; REG-250, REG-1051)
- P2 Treat destructive changes (drop, delete, truncate) as not reversible by script; their undo is a restore, so prepare and test it before running them. (L388; REG-250, REG-251, REG-252)
- P3 Soft deletion or a retention window as the first defence, restore last. Consensus. (L416; REG-250)
- P4 Soft deletion with a deleted_at flag has costs to weigh: the predicate leaks into every query, foreign keys no longer enforce consistency between deleted parent and children, a legally required purge gets harder, undelete is rarely used. Grounded in one T3 (practitioner experience); the soft-deletion side was not read at T1 or T2 (open); the usual argument is recoverability and history. (L1255; REG-1142, REG-1145)
- P5 Hard delete plus an archive written in the same transaction (a deleted-record table holding table name, id and a copy of the row) when recovery or audit is needed, so foreign keys keep working. (L1256; REG-1142, REG-1145)
Note: L1255 records a possible tension with L416.
Links: index link OPERATION.RECOVERY (backup practice).

### ASSURANCE.DATA_INTEGRITY.4 Derived Data Sync and Staleness

Intent: how derived or denormalized data is kept in step with its source and its divergence found.
Rows: L281, L282, L314 (3)
Positions (no verdict):
- P1 Maintainer: every piece of derived data needs a synchronisation plan before it exists, chosen from a ladder by cost and strength (documentation only, declared constraints, detection queries, scheduled refresh, same-transaction triggers), by impact of divergence, change frequency and tolerable staleness; answer up front what, sync level, freshness target, change frequency, impact, how drift is found and fixed, what alerts. (L281; REG-181)
- P2 Always consistent (same transaction): serves correctness, costs write latency and coupling. (L281)
- P3 Eventual with a stated window: serves delivery speed and cost. (L281)
- P4 Maintainer: scheduled detection queries by importance (daily, weekly, quarterly) with a stated action on divergence (manual fix or reconciliation job). (L282; REG-181)
- P5 Maintainer: staleness is a designed property: store timestamps, state the freshness target up front, build the sync mechanism and its monitoring hooks before first production use; "no invalidation" and "no monitoring" are defects. (L314; REG-181)
Context variables: impact of divergence, change frequency, tolerable staleness (L281: "wins by context: criticality, change rate").

### ASSURANCE.DATA_INTEGRITY.5 Checking Old Against New and Rolling Out Checks

Intent: how a new structure or a new invariant is verified against the old one and brought into force without breaking production.
Rows: L283, L284, L391, L415 (4)
Positions (no verdict):
- P1 Before cutting reads to a new structure, run old and new paths side by side and alert on mismatch (shadow read comparison). Single T3 source. (L391; REG-257, REG-260)
- P2 Validate the new data against the old before removing the old structure; continuous out-of-band validation jobs find corruption early, independent of application logic. (L415; REG-250, REG-257, REG-260)
- P3 Maintainer: make conventions self-auditing: each rule ships with, or can be checked by, a query or script that finds its violations; a catalogue of anti-patterns serves as the audit list. (L283; REG-181)
- P4 Enforce a new invariant check immediately. Force: correctness. (L284 alternative)
- P5 Maintainer: roll out in observe-only mode first: the audit runs on every change and records findings, autofix is a dry run, nothing raises; a kill-switch default of observe makes known defects tolerable and is not the fix; enforcement is switched on after open defects are removed. Force: reversibility, delivery speed. Wins: known violators exist in production. (L284; REG-181)

---

## ASSURANCE.DOCS_SYNC Documentation in Sync

Intent: which mechanism keeps documentation true to the system: same-change delivery, gates, owners, executable examples, link checks.
Rows: - (roll-up, 22 rows)
Links: index link TRANSVERSE.DOCS (authoring and organisation practice); this node holds the mechanism content (MD-03).

### ASSURANCE.DOCS_SYNC.1 Delivery with the Change

Intent: where and when documentation travels relative to the change it describes.
Rows: L210, L211, L230, L238 (4)
Positions (no verdict):
- P1 Documentation as code: plain text in version control, changed through review, in the repository of the thing it documents. (L210; REG-150, REG-153, REG-156)
- P2 Documentation delivered in the same pull or merge request as the code (Google; GitLab encourages, mandatory in some teams). Argument: no window where docs and code disagree. Force: correctness, confidence. Wins: continuously deployed products, small teams. (L211; REG-148, REG-150, REG-153)
- P3 Documentation in a separate pull request on a release branch (Kubernetes): docs ship only when the feature ships, a docs team works in parallel. Force: control, delivery speed for code. Wins: many contributors, release trains, a dedicated docs team; GitLab records the timing cost of splitting. (L211; REG-148, REG-153)
- P4 Reuse the existing developer workflow (tracker, review, CI) rather than a parallel process. (L230; REG-150, REG-156)
- P5 Documentation-only changes run a reduced, faster pipeline so updating docs is cheap. Single source; motivation inferred. (L238; REG-153)
Stack pointers: L238 (GitLab realisation by branch name).

### ASSURANCE.DOCS_SYNC.2 Gates and Review of Documentation

Intent: which changes need documentation, who checks it, and whether a missing document blocks the change or the release.
Rows: L212, L213, L214, L227, L228, L237, L239 (7)
Positions (no verdict):
- P1 State which changes require documentation (a definition-of-done trigger): user or admin-visible features, UI or API changes, changed workflows, deprecation and removal; internal-only changes exempt. (L213; REG-150, REG-151, REG-153)
- P2 Code review includes a documentation check: README, guides and generated reference updated; docs of deleted or deprecated code removed. (L212; REG-151, REG-153)
- P3 Hard merge gate when documentation is missing: the only mechanism that does not rely on goodwill (Write the Docs, some GitLab teams). Force: correctness, confidence. Wins: documentation is a user-facing contract or regulated. (L214; REG-153, REG-156)
- P4 Encouraged and reviewer-enforced, with waiver and follow-up issue (GitLab). Force: delivery speed, team load. Wins: release timing dominates and the follow-up is reliably tracked. (L214; REG-153)
- P5 Gate at release: a feature without documentation does not ship, the release gate may remove it from the milestone (Kubernetes). Force: control, confidence. Wins: release-train projects with many contributors. (L237; REG-148)
- P6 When documentation merges without the required reviewer, open a follow-up review issue at once, assigned to author and reviewer, so the debt is tracked. (L239; REG-150, REG-153)
- P7 Map documentation paths to owners with a code-owners file and require owner review by branch protection. (L227; REG-145)
- P8 Three kinds of review (technical, audience, writing), the team deciding who does each: engineers and code reviewers verify accuracy and writers review non-blocking (GitLab; wins with a small writer team and many changes) against writers approving significant changes (wins for cross-boundary or customer-facing docs). (L228; REG-150, REG-153)
Stack pointers: L227 (GitHub code-owners file; equivalents not read).

### ASSURANCE.DOCS_SYNC.3 Ownership, Freshness and Single Source

Intent: who answers for a document, how its truth is dated and checked, and how one explanation per topic is kept.
Rows: L215, L216, L217, L218, L319, L320 (6)
Positions (no verdict):
- P1 Every document has a named owner; unowned documents go stale. (L215; REG-150)
- P2 Documents carry freshness dates and are tracked as bugs so review is scheduled; remove or mark obsolete a document that no longer serves a purpose. (L216, L217; REG-150, REG-154)
- P3 Maintainer: date-stamp verification against the live system ("verified live on a date"), point fast-moving topics to the more current tracker, record open known violations with status and mitigation, never presenting a mitigation as a fix. Coverage check: agrees on dating with L216. (L319; REG-181)
- P4 One canonical document per topic; consolidate competing copies into the primary source. (L218; REG-150)
- P5 Maintainer: a generated or derived document is read-only and never copied back into the source of truth; an expanded copy written into a registry that resolves references can silently shadow its source. (L320; REG-181)

### ASSURANCE.DOCS_SYNC.4 Mechanical Documentation Checks

Intent: which documentation properties are checked by machine so that drift fails a build rather than rotting silently.
Rows: L219, L223, L224, L225, L226 (5)
Positions (no verdict):
- P1 Execute code examples in documentation in CI so a broken example fails a build; keep them readable. Cost: exact-output fragility. Force: confidence, speed of feedback. (L219; REG-143, REG-144)
- P2 The documentation build fails on warnings and unresolved references. (L223; REG-146)
- P3 Check links automatically in CI and on a schedule, because external links break without any commit (reason inferred). (L224; REG-146, REG-159)
- P4 Editorial style as rules failing CI: consistency across many authors without reviewer effort (Vale; force: speed of feedback). Wins: many authors. (L225; REG-149, REG-150)
- P5 Human writing review: judgement of clarity and audience cannot be linted (Google; force: quality). Wins: few authors or high-stakes docs. Vale itself says it targets consistency, not correctness. (L225; REG-149, REG-150)
- P6 Automate repetitive documentation review chores (changelog entry present when source changed, docs touched when API files changed) as CI rules that comment or fail. Limit: path rules detect the absence of an edit, not inaccuracy. (L226; REG-161)
Stack pointers: L219 (doctest, rustdoc), L223 (Sphinx), L224 (lychee, Sphinx linkcheck), L225 (Vale), L226 (Danger).

---

## ASSURANCE.SECURITY Security

Intent: which verification and enforcement mechanism, at which stage, guarantees security: design review, analysis, tests, scanning, enforced limits on automation.
Rows: - (roll-up, 37 rows)
Links: index link TRANSVERSE.SECURITY (programme practice); this node holds verification and enforcement (MD-03).

### ASSURANCE.SECURITY.1 Verification Depth and Design Review

Intent: how deep security verification goes for each application and when its design is reviewed.
Rows: L243, L1119, L1122, L1127, L1128 (5)
Positions (no verdict):
- P1 Review the design for security by a qualified person or by automated processes against the risk model before implementation proceeds. Single source. (L243; REG-004)
- P2 Set verification depth per application from its risk profile, not uniformly; write the assurance target down and revisit it when risk changes (the revisit trigger is inferred). (L1119, L1122; REG-1078, REG-1083, REG-1084)
- P3 A verification floor is a lower bar, not best practice; the concrete process is tailored to product, language, toolchain and lifecycle. (L1127; REG-1086)
- P4 Threat modelling output selects test cases and the code that gets focused review, not standing alone. (L1128; REG-1086)
Context variables: application risk profile (L1119: "depth set per application from its risk profile"); new personal data or regulatory scope as a revisit trigger (L1122).

### ASSURANCE.SECURITY.2 Stage Placement and Blocking Policy

Intent: at which pipeline stage each security check runs and whether its finding blocks the change.
Rows: L244, L245, L246, L1131 (4)
Positions (no verdict):
- P1 Decide by policy when code is reviewed by a person, analysed by tools, or both, by stage and risk; record and triage findings in the normal workflow; tool findings best reviewed by a human who remediates. Human review for backdoors and malicious content against automation for continuous coverage; the framework treats them as complements. Force: confidence against delivery speed. (L244; REG-004)
- P2 Place each check at the earliest stage where it can run: secrets and lint before commit; static, composition and infrastructure scanning at build; dynamic and interactive testing against a running instance; compliance audit after deployment. Stage list grounded, the finer tool mapping inferred. (L245; REG-004, REG-169)
- P3 Blocking gate: the only guarantee (push protection for secrets). Force: security, confidence. Wins: high-confidence, low-noise checks; regulated contexts. (L246, L1131; REG-004, REG-170, REG-179)
- P4 Advisory in the developer's workflow: adoption and trust, engineers fix by choice (Google). Force: delivery speed, cognitive load. Wins: noisy analyses. Variant: block on a curated high-confidence set and advise on the rest (Google, NIST must-fix list), which wins when noise is nonzero. (L246, L1131; REG-052, REG-1086, REG-1092)
- P5 Blocking with an audited waiver (platform bypass categories: "used in tests" and "false positive" close the alert, "I'll fix it later" stays open). Force: control and speed together. Wins: bypass is rare and reviewed. (L246; REG-170, REG-179)
- P6 Block on confirmed exploitable findings above a severity, applied at release (OpenSSF). Force: security. Wins: public-facing or regulated software. (L1131; REG-1094)
- P7 Leave placement to the team (OWASP DevSecOps). Force: team cognitive load; costs consistency. (L1131; REG-169)
Open recorded: the false-positive threshold that makes a check blockable was not found (L246). The two decision rows L246 and L1131 state the same decision.

### ASSURANCE.SECURITY.3 Verification Techniques

Intent: which kinds of test and manual testing are used to find vulnerabilities and to verify security requirements.
Rows: L247, L248, L1055, L1126, L1133, L1134, L1136, L1137 (8)
Positions (no verdict):
- P1 Test executable code to find vulnerabilities and verify security requirements, including functional tests of the security features, test types chosen by stage, in a sandboxed environment where appropriate. (L247; REG-004)
- P2 Ship a defined secure baseline configuration as the default and test the defaults. (L248; REG-004)
- P3 Apply security testing to every change on the assumption that produced code may carry vulnerabilities, not only to changes known to be generated. (L1055; REG-1035, REG-1044, REG-1048)
- P4 A developer floor for every change (threat model, static scan for top bugs, search for hardcoded secrets, run with built-in checks, black-box tests from specifications and threats, structural tests to at least 80% statement coverage, tests from past bugs, a fuzzer, a web application scanner for web services). Force: confidence at low cost. Against: fuller programmes (SAMM levels 2 and 3: application-specific automation, regular penetration tests), serving higher assurance, which win under high criticality or regulation. (L1126; REG-1081, REG-1086, REG-1094)
- P5 Fuzz continuously or at least pre-release, on components and the whole system: finds input-handling bugs tests miss and denies attackers the same tool. (L1133; REG-1086, REG-1092)
- P6 If the software serves a web interface, run a dynamic scanner or interactive tool against a running instance (OpenSSF marks dynamic analysis suggested at the base level, must at a higher badge level). (L1134; REG-1086, REG-1094, REG-169)
- P7 Combine automated testing (scalable baseline) with manual expert testing (business logic depth); automation frees experts for complex attack vectors. (L1136; REG-1081, REG-1091)
- P8 Direct manual security testing first at the highest-risk components, and let regular penetration testing follow as the practice matures (inferred; no source gives frequency). (L1137; REG-1081)
Context variables: criticality or regulation (L1126: fuller programmes "win under high criticality or regulation").
Stack pointers: L1134 (web), L1126 (scanner item for web services).

### ASSURANCE.SECURITY.4 Static and Scheduled Analysis Practice

Intent: when static and slow dynamic analyses run and how their blind spots and noise are handled.
Rows: L1129, L1130, L1135 (3)
Positions (no verdict):
- P1 Run static analysis as soon as code is written and repeat it automatically, per commit or in code review (Google). Force: speed of feedback. (L1129; REG-052)
- P2 Run slow whole-system or sanitizer analyses nightly or at least daily. Force: cost of ownership. (L1129, L1135; REG-1092, REG-1094)
- P3 Static analysis has blind spots and false positives: standardise on tools, keep a must-fix list, triage and suppress deliberately, use more than one analyser where weakness classes differ. (L1130; REG-1086, REG-1092)
Note: P1 and P2 are held by the same sources for different tool speeds (L1129).
Stack pointers: L1135 (sanitizers: C and C++ named).

### ASSURANCE.SECURITY.5 Secrets and Consumed Code

Intent: how secrets are kept out of history and how consumed artifacts are verified like own code.
Rows: L063, L251, L1140 (3)
Positions (no verdict):
- P1 Scan consumed artifacts for known vulnerabilities, licence and end-of-life status, and at higher maturity for malware, before and after integration. The inventory stays in the dependency lifecycle node. (L063; REG-004, REG-024, REG-035)
- P2 Apply the same verification to included libraries, packages and services as to own code. (L1140; REG-1086)
- P3 Layer secret scanning: editor or pre-commit, a blocking check at push time, and CI; blocking before the secret reaches history is preferred to alerting after. Cost: bypass paths. Force: speed of feedback, security. (L251; REG-166, REG-170)
Stack pointers: L251 (GitHub push protection and pre-commit detectors as realisations).

### ASSURANCE.SECURITY.6 Enforced Limits on Automation and Access

Intent: which limits on automation and on data access are enforced in tooling, not by instruction, and which jobs an automated author may execute.
Rows: L325, L326, L327, L1050, L1064, L1065, L1066, L1067, L1068, L1071, L1075 (11)
Positions (no verdict):
- P1 Enforce limits in the tooling (sandbox, scoped credentials, deny rules, deterministic hooks; for the data system a single sanctioned path with single statement, read-only on production, statement timeout, audit log), not by instruction in a prompt. (L1066, L326; REG-1033, REG-1037, REG-1038, REG-181)
- P2 Per-action human approval is not the only control on automation, because attention fades; pair with enforced boundaries. (L1050; REG-1037, REG-1038, REG-1044)
- P3 Give automation the least functionality, permissions and autonomy its task needs; default to a scoped workspace and no network egress, opened per need. (L1065, L1067; REG-1033, REG-1034, REG-1036, REG-1037, REG-1039)
- P4 In one session do not combine all three of untrusted input, access to sensitive systems or data, and the ability to change state or communicate externally without a human gate. Single T3 source for the statement; generalisation inferred. (L1068; REG-1033, REG-1036, REG-1049)
- P5 Treat any text an automated author reads (issues, comments, web pages, tool output) as untrusted instructions-bearing input. (L1075; REG-1033, REG-1036, REG-1037, REG-1039)
- P6 Version and review files that steer an automated author (instruction files, prompts, hooks, tool configuration) like code, read-only to the author where possible. (L1064; REG-1034, REG-1037 to REG-1039)
- P7 Maintainer: enforce data access at the lowest layer every path passes through (least privilege by role, separate from application permissions), one standard owner for all objects with a catalogue query that finds violations. Application-only authorization serves speed and misses direct paths. (L325; REG-181)
- P8 For a job with a large blast radius, decide and record whether an agent may execute it under enforced guards (classifier or sandbox; delivery speed; wins when guards can be applied and effects are reversible) or may only write it for a person to run (control and audit; wins when guards cannot be applied or effects are irreversible). Maintainer holds the second: the agent writes the script and queries but does not execute them, since execution bypasses the tooling's guards. (L327, L1071; REG-181, REG-1033, REG-1037)
Context variables: blast radius and reversibility of the job (L1071, L327).
Stack pointers: L325 (PostgreSQL roles in the doctrine).
Note: L327 and L1071 state the same decision.

### ASSURANCE.SECURITY.7 Closing the Loop on Findings

Intent: how verification is itself verified and what a found defect changes in the process.
Rows: L1138, L1139, L1160 (3)
Positions (no verdict):
- P1 Security tests also check that detection works: penetration tests and scans that raise no alert indicate a monitoring failure. (L1138; REG-1090)
- P2 Fix the bugs a verification step finds, change the process to catch that class earlier, and where possible choose an approach that precludes the class. (L1139; REG-1086)
- P3 Run a regular process to test, assess and evaluate the effectiveness of security measures, including the ability to restore availability and access to personal data. (L1160; REG-1095)

---

## ASSURANCE.PERFORMANCE Performance

Intent: which tests, measurements and budgets guarantee that speed and capacity hold under the real workload.
Rows: - (roll-up, 22 rows)

### ASSURANCE.PERFORMANCE.1 Targets and Budgets

Intent: what a performance target is derived from and how it is divided and enforced.
Rows: L420, L421, L435 (3)
Positions (no verdict):
- P1 Define targets from user needs and the SLO, translate into measurable test objectives with explicit pass or fail thresholds (for example p95 under a stated latency); never from current performance. (L420; REG-125, REG-226)
- P2 Split performance and error budgets across layers so a failing test identifies the layer to optimize. Single T1 source. (L421; REG-226)
- P3 For client-delivered software enforce budgets on artefact size and timing metrics in the build pipeline; when exceeded optimize, remove or block the addition. Single T3 source. (L435; REG-240)
Stack pointers: L435 (web front end; pointer for the JavaScript and web guidelines).

### ASSURANCE.PERFORMANCE.2 Load Test Design

Intent: what a load test must resemble and which kinds are run so that its result predicts real behaviour.
Rows: L422, L423, L424, L425, L426, L430, L431 (7)
Positions (no verdict):
- P1 Production-identical test environment for mission-critical workloads (compute, scaling, caching, network, dependencies). Force: confidence, fidelity. Wins: high criticality and when results gate capacity spend; cloud elasticity lowers its cost. (L422; REG-226, REG-229)
- P2 Scaled-down production-like environment. Force: cost of ownership. Wins: load behaviour scales predictably and criticality is low. (L422; REG-226)
- P3 Test in production. Force: highest realism, at user impact. Wins: only production has the data and dependencies, with guardrails. (L422; REG-203, REG-226)
- P4 Load test the whole workload end to end, not isolated components. (L423; REG-228, REG-229, REG-230)
- P5 Representative request mix and realistic data (synthetic or sanitized), including edge cases such as large payloads and high concurrency; include real third-party calls (realism; wins when the dependency is critical and the provider permits tests) against mocking them (repeatability, speed, hides problems; wins when the provider limits tests or to isolate own code). Contested. (L424; REG-104, REG-226, REG-229, REG-230)
- P6 Test past expected load to the breaking point and far beyond, not to a small safety factor, so failure modes and early-warning metrics are known. (L425; REG-203, REG-225, REG-229, REG-230, REG-238)
- P7 Several test types matched to risk (smoke, average load, stress, spike, soak, breakpoint); begin with basic load tests and widen as risks and experience grow. (L426; REG-226, REG-238)
- P8 Generate load open-loop (constant arrival rate) or correct for coordinated omission, since a generator waiting for each response under-reports tail latency. Grounded in one T3 source, so the normative rule is inferred. (L430; REG-239)
- P9 Measure client-perceived outcomes (goodput) rather than server-side throughput alone when testing overload. Single T2 source. (L431; REG-225)
Context variables: criticality of the workload (L422: choice "by criticality"); provider testing policy (L424).

### ASSURANCE.PERFORMANCE.3 When Tests Run and Baselines

Intent: at which moments performance tests run and against what a result is compared.
Rows: L108, L427, L428, L429 (4)
Positions (no verdict):
- P1 Performance regression tests and production-side configuration checks, so slow drift and misconfiguration do not pass unnoticed. (L108; REG-051, REG-067)
- P2 Every change gated in the pipeline (smoke on code change, load against thresholds): speed of feedback, regression traced to one change. Wins: a stable, low-variance harness and fast tests. (L427; REG-226, REG-230)
- P3 Scheduled or event-driven runs (soak and spike before anticipated events or after large changes, breakpoint occasionally): cost, low noise. Wins: tests long, expensive or noisy. Early testing needs dedicated infrastructure and expertise. (L427; REG-238, REG-242)
- P4 Record a baseline of normal performance, compare each run against it for regression and slow drift, refresh baselines after architectural or scaling changes. (L428; REG-226, REG-230)
- P5 Validate performance changes as hypotheses (prediction, same load test on baseline and variant, compare), reserved for high-impact changes. Single T1 source. (L429; REG-226)
Context variables: harness stability and test cost (L427).

### ASSURANCE.PERFORMANCE.4 Testing in Production for Performance

Intent: what only production reveals about performance and under which guardrails it is tested there.
Rows: L432, L433 (2)
Positions (no verdict):
- P1 Pre-production only. Force: user safety, reversibility. Wins: high-impact or regulated systems with faithful replicas. (L432)
- P2 Supplement with controlled production tests (off-peak, ramped from a small share, extra capacity reserved, rollback ready); real-traffic tests are higher fidelity and higher user risk. Force: realism of data, network, third parties. Wins: a faithful replica is unaffordable. (L432; REG-104, REG-203, REG-226, REG-229)
- P3 Synthetic load maximizes code coverage but not state coverage (caches, cookies, request affinity); complement with canary analysis on organic traffic. Single T2 source. (L433; REG-104)
Context variables: impact class of the system and affordability of a faithful replica (L432).

### ASSURANCE.PERFORMANCE.5 Measurement Before Optimization

Intent: that speed is established by measurement of the real workload, never by belief, and how a measurement is made trustworthy.
Rows: L434, L1178, L1179, L1563, L1564, L1565 (6)
Positions (no verdict):
- P1 Measure first, optimize the critical few; iterative and data-driven. Force: cost of ownership, delivery speed. (L434, L1178; REG-1105, REG-138, REG-241)
- P2 Estimate resources and test from design onward so architectural bottlenecks are found before they are costly. Force: avoided rework. Wins: architecture hard to change and load high. Both positions agree on measurement before tuning. (L434; REG-224, REG-226)
- P3 Prioritize with field (real-user) data; use lab data to test changes before release and to find opportunities. (L1179; REG-1105)
- P4 A performance or memory belief becomes a rule only through measurement on the real workload; advice resting on implementation internals is dated evidence that may describe a mechanism but cannot prescribe. Conflict kept from the origin: restructuring for speed on mechanism alone, as the MDN pages on closures and inheritance describe the mechanism. Origin: judged in the JavaScript guideline, prior position known, single T2 body, rule inferred. (L1563, L1564; REG-1571 to REG-1577)
- P5 A measurement is trustworthy only as a distribution: start-up and steady state separately across several fresh invocations with several iterations, confidence intervals not one number, varied setup. Transfer from Java and C measurements inferred. Origin: judged in the JavaScript guideline, prior position known. (L1565; REG-1578, REG-1579)
Links: Requires (within the node) L1565 by L1564; no cross-node link.

---

## ASSURANCE.AVAILABILITY Availability and Recovery

Intent: which design mechanisms and exercised procedures guarantee the system stays available under dependency failure and can be recovered.
Rows: - (roll-up, 22 rows)
Links: index link OPERATION.RECOVERY holds the practice (backup, objectives, strategy, failover); this node holds the proof (restore tests, exercises) (MD-03).

### ASSURANCE.AVAILABILITY.1 Tolerating a Degraded Dependency

Intent: that the system keeps serving when a non-essential dependency is slow or down, and that overload degrades before it fails.
Rows: L032, L442 (2)
Positions (no verdict):
- P1 Prefer loosely coupled designs that tolerate a degraded dependency: fewer dependencies raise availability; turn hard dependencies into soft ones; design a degraded mode (cached or default result, reduced feature) for each non-essential external dependency and exercise it regularly. Grounded for one source, graceful-degradation detail inferred. (L032; REG-007, REG-185, REG-203, REG-209)
- P2 Design and test overload behaviour: reject early when out of quota or capacity, serve degraded responses before errors, cap client retries (per-request and per-client budgets), throttle on the client. The row places verification of the behaviour here and its design in application architecture. (L442; REG-220, REG-225, REG-228)

### ASSURANCE.AVAILABILITY.2 Protecting Remote Calls

Intent: how each call to a remote dependency is bounded so that one failing dependency cannot take the caller down or be amplified by it.
Rows: L332, L333, L334, L335, L336, L337, L338, L339 (8)
Positions (no verdict):
- P1 A connection timeout and a request timeout on every remote call, sized from the dependency's measured latency percentile and an accepted false-timeout rate; propagate a deadline across calls and do not start work for a caller that gave up. (L332, L339; REG-194, REG-203, REG-211)
- P2 Retry only transient failures, capped exponential backoff with jitter, a per-request attempt cap, retries at one layer only. REG-211 states retries are "selfish": the caller buys success with the provider's capacity. (L333; REG-203, REG-205, REG-211)
- P3 Retry a non-read operation only when idempotent by contract or protected by an idempotency key; agreement on principle, contested on mechanism (header not standardised). (L334; REG-184, REG-205, REG-206, REG-211)
- P4 Honour explicit throttling and wait signals (429, 503, Retry-After) rather than retrying blind. Inferred in part. (L335; REG-184, REG-185)
- P5 Use the provider's well-tested client or SDK for timeout and retry, and verify what it retries by default. (L336; REG-201, REG-211)
- P6 Bound the whole system's retry volume with a retry budget so retries cannot amplify an outage. (L337; REG-203, REG-211)
- P7 Circuit breaker with half-open probing, logged state changes and fallback: protection of own resources, fast failure. Wins: slow-failing synchronous dependencies with many callers. (L338; REG-185, REG-209)
- P8 Retry budget alone: simplicity, cognitive load. Wins: the dependency tolerates retries and callers are few. (L338; REG-203, REG-211)
- P9 Neither: queue and dead-letter, in event-driven designs; or the platform or mesh already breaks circuits. (L338; REG-185)
Context variables: dependency failure mode and number of callers (L338: "slow-failing synchronous dependencies with many callers").
Stack pointers: L335 (HTTP).

### ASSURANCE.AVAILABILITY.3 Verifying Resilience Under Real Conditions

Intent: how resilience is verified against real traffic without harming users; the canary analysis of regressions before full rollout is held in `CHANGE_FLOW.DEPLOY`.
Rows: L119, L120 (2)
Positions (no verdict):
- P1 Testing in production is valuable and risky: issues found there already affect users, test data can become visible; limit blast radius and isolate test data. Coverage check: partial tension with L265. (L119; REG-051, REG-069)
- P2 Verify resilience of distributed systems with automated, ideally continuous experiments on a steady-state hypothesis over measurable outputs, preferably on production traffic with minimized blast radius (chaos principles). Force: authenticity of confidence. Wins: mature observability and rollback. Single T3 source. (L120; REG-069)
- P3 Pre-production only (inferred, unsourced, open). Force: safety. Wins: regulated or low-recovery systems, low maturity, safety-critical. (L120)
Context variables: observability and rollback maturity, regulation, safety criticality (L120).

### ASSURANCE.AVAILABILITY.4 Proving Restore

Intent: that a backup is defined by whether it restores, and that the restore is proven by test against criteria fixed beforehand.
Rows: L389, L1078, L1097, L1098, L1099, L1100 (6)
Positions (no verdict):
- P1 Define a backup by whether it restores, not by whether it was taken; test restores regularly; keep the restore path independent of schema-change tooling; design and judge the backup system by recovery. (L389, L1078; REG-250, REG-251, REG-1053, REG-1073)
- P2 Test recovery end to end on a regular schedule, automated, from the same procedures used in a real recovery; an untested backup, restore path or plan is an assumption. (L1097; REG-250, REG-1053, REG-1059, REG-1060, REG-1061, REG-1064, REG-1065)
- P3 A restore test checks against criteria fixed beforehand that data is present, uncorrupted, accessible and within the RPO, and that restore completes within the RTO with enough resources and without hidden external dependencies. (L1098; REG-250, REG-1053)
- P4 Verify backup integrity before restoring and restored assets before declaring service restored. (L1099; REG-1053, REG-1060)
- P5 Exercise every recovery path you rely on and keep the number of paths small, because the only recovery that works is the one tested frequently; check drift in the recovery site (capacity, quotas, images, configuration). (L1100; REG-250, REG-1056, REG-1058)

### ASSURANCE.AVAILABILITY.5 Exercising Recovery

Intent: how recovery procedures are exercised, where, how often, and how measured times feed back.
Rows: L451, L1102, L1103, L1104 (4)
Positions (no verdict):
- P1 Exercise recovery under realistic conditions (manual runbooks, failover and failback, tabletop exercises) and turn gaps found into tests. (L451; REG-222, REG-228)
- P2 Exercise failover in production regularly for complex or critical paths (AWS): realism of confidence. Wins: a staged environment cannot reproduce load or quotas. (L1102; REG-1056, REG-1058)
- P3 Test in non-production first to validate safety, then production-level drills (Azure): production drills can themselves cause severe failures. Wins: a failed drill's blast radius is high or the procedure is new. (L1102; REG-1064)
- P4 Both as a ladder (tabletop, dry run, production-level) combined with unannounced game days. (L1102, L1103; REG-1059, REG-1064)
- P5 A ladder of exercises (discussion-based tabletop, functional exercise, full test), run periodically and after changes to the system or plan, with an after-action report whose corrective actions update the plan. (L1103; REG-1059, REG-1064)
- P6 Measure restore or failover time and achieved recovery point in every test, compare with the objectives, and use measured times, not estimates, as the planning minimum. (L1104; REG-250, REG-1053, REG-1064)
Context variables: complexity and criticality of the recovery path, blast radius of a failed drill, novelty of the procedure (L1102).

---

## ASSURANCE.ARTIFACT Artifact Integrity

Intent: which mechanism guarantees that what runs is what was reviewed and built from reviewed source.
Rows: - (roll-up, 9 rows)

### ASSURANCE.ARTIFACT.1 Build Provenance and Match to Source

Intent: how a built artifact is shown to correspond to its source, and how strongly.
Rows: L048, L151, L152, L285, L369, L1244 (6)
Positions (no verdict):
- P1 Reproducible builds so any party can verify by bit-identical rebuild. Force: security, control. Wins: high-assurance or widely distributed artifacts; costs build discipline. (L048; REG-035, REG-041)
- P2 Trust signed provenance without rebuild. Force: cost of ownership. Wins: most teams. (L048; REG-023)
- P3 Set a target build-integrity level by risk: at least provenance (SLSA Build L1), a hosted build platform with signed provenance (L2) for anything distributed, hardened isolated builds (L3) where insider or credential-compromise risk matters; the level per project is the team's decision. (L151; REG-023, REG-086)
- P4 Produce verifiable build provenance, at least from a hosted platform with signed provenance (Build L2), and verify it before use. (L1244; REG-086, REG-1135)
- P5 Protect code and its release integrity and archive releases as secure development frameworks require (SSDF PS.1, PS.2, PS.3, PW.7, PW.8). Grounded on the names; exact content open. (L152; REG-004)
- P6 Prefer a build service on dedicated hosted infrastructure that produces signed provenance, isolates runs from each other and keeps signing material away from user-defined steps (SLSA Build L2 and L3); levels: provenance only (cost, low), hosted and signed (L2), hardened (L3; control and security; wins for software distributed to others or high-value builds); the target level is a team choice. Consensus on the levels. Moved here from `OWNERSHIP.SERVICES`; same levels as P3 and P4. (L369; REG-086)
- P7 Maintainer: compare the deployed definitions of executable database objects against their source mechanically (export, parse both sides, compare signature and body after normalization, report by severity), because the two drift. Public practice read as majority (drift detection). (L285; REG-181)
Context variables: risk of insider or credential compromise, and how widely the artifact is distributed (L151, L048, L369).
Stack pointers: L285 (PostgreSQL tool).

### ASSURANCE.ARTIFACT.2 Protected Mainline Binds Every Actor

Intent: that required reviews and checks bind every actor, including bots and administrators, and restrict where automation may write.
Rows: L131, L1063, L1070 (3)
Positions (no verdict):
- P1 Protect the mainline mechanically: required status checks and required review before merge, no force push, restricted push rights; add signed commits where provenance of authorship is required. (L131; REG-091, REG-094, REG-114)
- P2 Required reviews, checks and signed-commit rules bind every actor, including bots and administrators. (L1063; REG-1037, REG-114)
- P3 Automation pushes only to a restricted, non-protected target (one branch), never directly to protected branches, by tag or by deletion, and repository rules are not bypassable by the access automation holds. (L1070; REG-1036, REG-1037)
Stack pointers: L131, L1063, L1070 (GitHub terms; neutral in principle).

---

## Routing objections

Seven were raised; each is resolved in `../../objections/resolution.md`. Moved (row now sits on the target branch, no longer listed): L118 to `CHANGE_FLOW.DEPLOY`, L229 and L318 to `TRANSVERSE.DOCS`, L313 to `OPERATION.TELEMETRY`. Kept (listed, with the reason): the three rows below. Inferred, not checked against the sources.

| row | now attached to | would route to | reason | resolution |
|---|---|---|---|---|
| L131 | ASSURANCE.ARTIFACT.2 | CHANGE_FLOW.INTEGRATION | its intent lists mainline protection as how integration is carried out; the row states the practice, while L1063 states the outcome that binds every actor | kept: the row, L1063 and L1070 are one cluster of positions on which mechanism guarantees that what runs was reviewed; the decision node holds it (MD-03) and CHANGE_FLOW.INTEGRATION holds no node on mainline protection to receive it |
| L238 | ASSURANCE.DOCS_SYNC.1 | CHANGE_FLOW.BUILD | a reduced pipeline for documentation-only changes is a pipeline-shape practice | kept: it is a lever on whether documentation travels with the change (cheap update, not postponed), beside L211; CHANGE_FLOW.BUILD (what every build is) has no place for a change-type-dependent pipeline |
| L275 | ASSURANCE.BEHAVIOUR.8 | OPERATION.INCIDENTS | a symptom-indexed pitfall catalogue grown after any defect found twice is learning from incidents (the row's origin area is operate) | kept: its trigger is any defect, not a production incident, and it sits beside the same maintainer's defect-class rows L274 to L278; OPERATION.INCIDENTS is the review of incidents |
