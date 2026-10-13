# DELIVER research result: version control, review, CI, build/release, deploy, rollback, environments

## L1 headline

Best practice for delivery is well settled on its core (one mainline, small batches integrated at least daily, automated and identical deploys, progressive rollout with automated rollback, peer review instead of external approval boards) and still contested where it depends on context (review mechanism, merge method, release cadence, manual gates, monorepo, environment parity, rollback versus fix forward). Certainty: grounded for the core, which rests on T2 sources that agree (DORA, Fowler, Google, Amazon); inferred where the sources are silent (merge method, rollback versus fix forward, calendar versioning).

Pinned:
- Sources: 44 (T1: 8, T2: 32, T3: 4, T4: 0).
- Claims: 50.
- Contested topics: merge method (squash, merge commit, rebase); monorepo versus multiple repositories; Conventional Commits versus free-form messages; review mechanism (mandatory async pull request, pairing, ship/show/ask); presubmit scope (all tests versus fast tests only); release cadence (continuous, release train, explicit versions); manual approval gates in the pipeline; progressive rollout strategy (blue-green, canary, waves); rollback versus fix forward; environment parity versus testing in production; push versus pull (GitOps) deployment; daily integration versus feature branches.
- Failed fetches on T1 sources: none. Thin fetch: NIST SP 800-218 page returned only practice names (PS.1, PS.2, PS.3, PW.7, PW.8), not their text. One T2 fetch failed (DORA code-review capability page, HTTP 404); no replacement read.

## L2 claims

### Clusters

1. Everything the system needs lives in version control, and mainline is integrated at least daily through short-lived branches. Agreement: majority (contested for feature-branch and open-source contexts). Certainty: grounded. C01, C02, C03, C04, C05, C06.
2. Mainline is protected and history is kept legible (branch protection, atomic commits with what and why). Agreement: consensus on protection and commit hygiene; contested on merge method, commit format, monorepo. Certainty: grounded on rules, inferred on merge-method winner. C07, C08, C09, C10, C11, C12.
3. Every change gets human review, but review must be fast, small and focused on design and understanding; external approval boards hurt. Agreement: consensus on principle, contested on mechanism. Certainty: grounded. C13 to C20.
4. CI: every push builds and runs self-testing automated checks in a reference environment, in minutes; a broken mainline outranks everything. Agreement: consensus (contested on presubmit scope). Certainty: grounded. C21 to C25.
5. Builds are scripted, hermetic and reproducible; build, release and run are separate; releases are immutable, identified, and promoted unchanged. Agreement: consensus. Certainty: grounded. C26, C27, C34, C35.
6. Build integrity is a graded, risk-based target (SLSA levels, SSDF). Agreement: consensus on the need, level choice is a decision. Certainty: grounded on SLSA, thin on SSDF. C28, C29.
7. Release cadence: small frequent releases, with release decoupled from deploy by flags that are treated as inventory with an expiry. Agreement: majority. Certainty: grounded. C30, C31, C32, C33.
8. Deployment is automated, identical in every environment including production, and on demand. Agreement: consensus. Certainty: grounded. C36, C45.
9. Changes cause most outages, so roll out progressively, judge against a control, roll back automatically, and keep changes backward compatible so rollback is possible. Agreement: majority (strategy contested). Certainty: grounded. C37 to C41, C50.
10. Environments: production parity for backing services; infrastructure replaced, not patched; desired state declarative and versioned. Agreement: majority. Certainty: grounded. C42, C43, C44.
11. Delivery is measured with five DORA metrics; speed and stability move together only when supporting practices exist. Agreement: consensus on metrics, qualified on the claim. Certainty: grounded. C46, C47, C48, C49.

### Live debates (forces in tension)

- Daily integration to trunk versus feature branches with a merge at completion: feedback speed and integration risk versus isolation, low commitment contributors, control (C02, C03).
- Squash versus merge commit versus rebase: legible history and easy revert versus fidelity of history and per-commit bisect (C07).
- Monorepo versus multiple repositories: one-version consistency and atomic change versus compliance, access control, exit risk (C09).
- Mandatory asynchronous review versus pairing versus ship/show/ask: confidence and shared knowledge versus delivery speed and trust cost (C14).
- Run all tests before merge versus only fast reliable ones with the rest after: confidence versus speed of feedback (C22).
- Continuous release per commit versus scheduled release train versus explicit versions: delivery speed versus predictability for consumers and support of several versions (C30).
- Fully hands-off pipeline versus human authorization gates: speed and reduced toil versus control and regulation (C33).
- Blue-green versus canary versus wave rollout: cost of ownership (double infrastructure) versus operational complexity (several versions live) versus blast radius (C37).
- Automated rollback versus fix forward: reversibility and recovery time versus simplicity and risk of data incompatibility (C39).
- Environment parity and staging versus testing in production through canary: confidence before release versus cost of ownership and fidelity (C42).
- Push-based CI deploy versus pull-based GitOps reconciliation: simplicity versus drift control, security and auditability (C44).
- Structured commit messages for automation versus free-form: automation and changelog versus team cognitive load (C11).

### Candidate central decisions (each team must make first, others depend on them)

1. Release model: continuous deployment, scheduled train, or explicitly versioned releases with several versions supported. It sets branching model, cadence, versioning scheme and rollback strategy (C03, C12, C30).
2. Integration discipline: maximum branch lifetime and the mainline protection rules (C02, C05, C08).
3. Review mechanism and its latency budget (C14, C16, C20).
4. What counts as "releasable": CI gates, presubmit scope, test time budget (C21, C22, C23).
5. Artifact and provenance policy: build once, immutable, which SLSA level (C27, C28).
6. Rollout and rollback strategy by criticality and consumer count (C37, C39, C40).
7. Environment set and parity policy (C42, C43).
8. How delivery is measured (C46).

### Not covered

- Calendar versioning, release notes tooling, stacked pull requests tooling, merge queues beyond a mention, mobile or on-device release (app store review), regulated change management (ITIL, SOX) beyond DORA's statement, data and ML pipelines, infrastructure-as-code tooling choices, Kubernetes-specific deploy tools.
- Test content and test strategy (VERIFY), alerting and SLO design (OPERATE), secrets and configuration (TRANS), dependency pinning and supply-chain scanning (ADOPT).
- The Humble and Farley book and Accelerate were not read directly; the DORA pages and Fowler pages were read instead.

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| DELIVER-S01 | T2 | Continuous Integration | Martin Fowler | https://martinfowler.com/articles/continuousIntegration.html | CI practices, integration styles |
| DELIVER-S02 | T2 | Trunk Based Development | Paul Hammant and contributors | https://trunkbaseddevelopment.com/ | trunk model, scale, release branches |
| DELIVER-S03 | T2 | Capabilities: Trunk-based Development | DORA | https://dora.dev/capabilities/trunk-based-development/ | thresholds, pitfalls |
| DELIVER-S04 | T2 | The Standard of Code Review | Google Engineering Practices | https://google.github.io/eng-practices/review/reviewer/standard.html | review approval standard |
| DELIVER-S05 | T2 | The Twelve-Factor App, V. Build, release, run | Adam Wiggins | https://12factor.net/build-release-run | stage separation, immutable releases |
| DELIVER-S06 | T2 | SRE book, ch. 8 Release Engineering | Google | https://sre.google/sre-book/release-engineering/ | hermetic builds, self-service release, branching |
| DELIVER-S07 | T2 | Software Engineering at Google, ch. 9 Code Review | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch09.html | review at scale |
| DELIVER-S08 | T2 | Software Engineering at Google, ch. 24 Continuous Delivery | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch24.html | velocity, flags, progressive rollout |
| DELIVER-S09 | T2 | Software Engineering at Google, ch. 23 Continuous Integration | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch23.html | presubmit, flakes, build cop |
| DELIVER-S10 | T1 | SLSA v1.0 Build track levels | OpenSSF / SLSA | https://slsa.dev/spec/v1.0/levels | build provenance levels |
| DELIVER-S11 | T2 | Blue Green Deployment | Martin Fowler | https://martinfowler.com/bliki/BlueGreenDeployment.html | blue-green and DB caveat |
| DELIVER-S12 | T2 | Canary Release | Danilo Sato, on martinfowler.com | https://martinfowler.com/bliki/CanaryRelease.html | canary definition and caveats |
| DELIVER-S13 | T2 | Feature Toggles | Pete Hodgson, on martinfowler.com | https://martinfowler.com/articles/feature-toggles.html | toggle categories and cost |
| DELIVER-S14 | T3 | A successful Git branching model (with 2020 note) | Vincent Driessen | https://nvie.com/posts/a-successful-git-branching-model/ | git-flow and its own scope limit |
| DELIVER-S15 | T1 | GitHub flow | GitHub Docs | https://docs.github.com/en/get-started/using-github/github-flow | PR-based lightweight flow |
| DELIVER-S16 | T2 | Capabilities: Continuous Integration | DORA | https://dora.dev/capabilities/continuous-integration/ | CI practice and metrics |
| DELIVER-S17 | T2 | Capabilities: Deployment Automation | DORA | https://dora.dev/capabilities/deployment-automation/ | deployment automation |
| DELIVER-S18 | T2 | DORA software delivery metrics guide | DORA | https://dora.dev/guides/dora-metrics/ | five metrics, speed and stability |
| DELIVER-S19 | T2 | Capabilities: Streamlining Change Approval | DORA | https://dora.dev/capabilities/streamlining-change-approval/ | CAB versus peer review |
| DELIVER-S20 | T2 | Capabilities: Version Control | DORA | https://dora.dev/capabilities/version-control/ | what goes into version control |
| DELIVER-S21 | T2 | Capabilities: Working in Small Batches | DORA | https://dora.dev/capabilities/working-in-small-batches/ | batch size |
| DELIVER-S22 | T2 | Capabilities: Continuous Delivery | DORA | https://dora.dev/capabilities/continuous-delivery/ | CD definition, enabling practices, J-curve |
| DELIVER-S23 | T2 | Ship / Show / Ask | Rouan Wilsenach, on martinfowler.com | https://martinfowler.com/articles/ship-show-ask.html | alternatives to mandatory review |
| DELIVER-S24 | T1 | NIST SP 800-218 SSDF v1.1 | NIST | https://csrc.nist.gov/pubs/sp/800/218/final | secure development practices (page gave practice names only) |
| DELIVER-S25 | T2 | Speed of Code Reviews | Google Engineering Practices | https://google.github.io/eng-practices/review/reviewer/speed.html | review latency |
| DELIVER-S26 | T2 | Small CLs | Google Engineering Practices | https://google.github.io/eng-practices/review/developer/small-cls.html | change size |
| DELIVER-S27 | T1 | OpenGitOps principles v1.0.0 | OpenGitOps (CNCF working group) | https://opengitops.dev/ | GitOps definition |
| DELIVER-S28 | T1 | Semantic Versioning 2.0.0 | Tom Preston-Werner | https://semver.org/ | version number semantics |
| DELIVER-S29 | T3 | Conventional Commits 1.0.0 | conventionalcommits.org | https://www.conventionalcommits.org/en/v1.0.0/ | commit message convention |
| DELIVER-S30 | T2 | Twelve-Factor, X. Dev/prod parity | Adam Wiggins | https://12factor.net/dev-prod-parity | parity gaps |
| DELIVER-S31 | T2 | SRE Workbook, Canarying Releases | Google | https://sre.google/workbook/canarying-releases/ | canary evaluation |
| DELIVER-S32 | T2 | Parallel Change | Danilo Sato, on martinfowler.com | https://martinfowler.com/bliki/ParallelChange.html | expand-migrate-contract |
| DELIVER-S33 | T2 | Software Engineering at Google, ch. 16 Version Control and Branch Management | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch16.html | one-version, monorepo, branches |
| DELIVER-S34 | T1 | SLSA v1.0 About | OpenSSF / SLSA | https://slsa.dev/spec/v1.0/about | SLSA scope and limits |
| DELIVER-S35 | T2 | Deployment Pipeline | Martin Fowler | https://martinfowler.com/bliki/DeploymentPipeline.html | pipeline stages |
| DELIVER-S36 | T3 | Expectations, Outcomes, and Challenges of Modern Code Review | Bacchelli and Bird, Microsoft Research (peer-reviewed) | https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/ | empirical purpose of review |
| DELIVER-S37 | T1 | About merge methods on GitHub | GitHub Docs | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github | merge, squash, rebase effects |
| DELIVER-S38 | T2 | Feature Branch | Martin Fowler | https://martinfowler.com/bliki/FeatureBranch.html | feature branch costs |
| DELIVER-S39 | T2 | Immutable Server | Kief Morris, on martinfowler.com | https://martinfowler.com/bliki/ImmutableServer.html | drift and immutable replacement |
| DELIVER-S40 | T2 | Frequency Reduces Difficulty | Martin Fowler | https://martinfowler.com/bliki/FrequencyReducesDifficulty.html | rationale for frequent releases |
| DELIVER-S41 | T2 | SRE book, Introduction | Google | https://sre.google/sre-book/introduction/ | change causes about 70% of outages |
| DELIVER-S42 | T1 | About protected branches | GitHub Docs | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | branch protection controls |
| DELIVER-S43 | T3 | Automating safe, hands-off deployments | Amazon Builders' Library | https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments (the aws.amazon.com/builders-library URL redirected here) | one-box, waves, bake, auto rollback |
| DELIVER-S44 | T2 | On Pair Programming | Birgitta Boeckeler and Nina Siessegger, on martinfowler.com | https://martinfowler.com/articles/on-pair-programming.html | pairing versus review |

Note: the fetches returned model-condensed page content; quotes below are as returned. Author attributions of the Fowler-hosted articles other than Fowler are from my knowledge, not from the fetched text (inferred).

### Claims

**DELIVER-C01**
- claim: Keep everything needed to build, deploy and restore the system (source, scripts, infrastructure and application configuration, dependencies) in version control, so a clean machine can obtain and build everything from the repository alone.
- level: principle
- stack: neutral
- sources: S01 (Put Everything in Version-Controlled Mainline), S20 (Recommended Practices), S17 (store scripts and configuration in version control)
- agreement: consensus
- certainty: grounded

**DELIVER-C02**
- claim: Integrate into a single shared mainline at least once per day, with any branch living hours to at most a couple of days; prefer this over feature branches merged at completion when the team is full-time and has strong automated tests.
- level: decision
- stack: neutral
- sources: S01 (Commit to Mainline Daily; Integration Styles), S03 (Thresholds), S16, S38 (short versus long cycles), S02
- agreement: contested
- positions:
  - Daily integration to trunk. Strongest argument: many small integrations reduce conflict complexity and give early feedback; DORA correlates it with delivery performance (three or fewer active branches, merge daily, branch lifetime hours). Held by Fowler (S01), DORA (S03, S16), Google (S33). Force: speed of feedback, confidence. Wins: committed full-time team, good automated tests, continuously deployed product.
  - Feature branches merged when complete. Strongest argument: defers integration risk, isolates unfinished work, suits sparse contributors. Held by Fowler's own account of open source (S01 "open-source projects with sparse contributors typically benefit more from feature-branching"), S38 (works when the cycle is 1-2 days). Force: control, low coordination cost for part-time contributors. Wins: open source with many untrusted or part-time contributors; features of one to two days.
- certainty: grounded

**DELIVER-C03**
- claim: Choose the branching model from the release model: trunk or GitHub flow when delivering continuously; add release branches (and git-flow style) only when software is explicitly versioned or several versions must be supported in the field.
- level: decision
- stack: neutral
- sources: S14 (2020 note), S15 (Important Context), S02 (Release Branches), S33 (Release Branches)
- agreement: majority
- positions: continuous delivery to one live version fits trunk or GitHub flow (Driessen himself, S14; GitHub, S15; Google, S33). Multi-version or explicitly versioned products still fit git-flow (S14). Forces: delivery speed and low cognitive load versus support of several versions (control). Wins: depends on number of versions in the field.
- certainty: grounded

**DELIVER-C04**
- claim: Cut a release branch only when needed, just in time, fix defects on mainline and cherry-pick into the release branch, and delete it after release; do not merge release branches back.
- level: practice
- stack: neutral
- sources: S06 (Branching and Cherry-Picking), S02 (Release Branches), S33 (Release Branches)
- agreement: majority
- positions: with continuous deployment, no release branch at all, redeploy a fix from trunk (S33, S02 "fix forward"). Force: simplicity. Wins: release cycle of hours.
- certainty: grounded

**DELIVER-C05**
- claim: Avoid long-lived development branches; they make merges, regression isolation and large-scale changes costlier.
- level: principle
- stack: neutral
- sources: S33 (Trunk-Based Development), S38 (Critical Drawbacks), S03
- agreement: consensus
- certainty: grounded

**DELIVER-C06**
- claim: Integrate unfinished work into mainline hidden behind feature flags, dark launches, keystones or branch by abstraction rather than holding it on a branch.
- level: practice
- stack: neutral
- sources: S01 (Hide Work-in-Progress), S13 (Release Toggles), S21 (Implementation Techniques), S02
- agreement: majority
- positions: hide in mainline (all cited). Counter-force is toggle testing burden and carrying cost (S13, see C32); wins when work spans more than the integration interval.
- certainty: grounded

**DELIVER-C07**
- claim: Decide and record one merge method (merge commit, squash, rebase) per repository; the choice trades readable history against fidelity, and a linear-history setting can enforce it.
- level: decision
- stack: neutral (described in GitHub terms)
- sources: S37 (all three methods), S42 (Linear History)
- agreement: contested
- positions:
  - Squash: one commit per change, streamlined history, simple revert; loses when the individual changes were made (S37). Force: team cognitive load, reversibility. Wins: small changes, one logical unit per pull request.
  - Rebase: linear history, commits kept individually; new SHAs, loses signature verification on GitHub (S37). Force: bisect granularity, history fidelity. Wins: well-structured atomic commits.
  - Merge commit: complete branch history, shows when integrated; non-linear (S37). Force: fidelity, audit. Wins: need to trace integration events.
- certainty: grounded on effects; no source read ranks the methods (open on a winner)

**DELIVER-C08**
- claim: Protect the mainline mechanically: required status checks and required review before merge, no force push, restricted push rights; add signed commits where provenance of authorship is required.
- level: practice
- stack: GitHub terms (pointer); neutral in principle
- sources: S42 (all settings), S19 (peer review captured in platform), S15 (branch protection)
- agreement: consensus
- boundary: TRANS (signed commits as security practice)
- certainty: grounded

**DELIVER-C09**
- claim: Decide monorepo or multiple repositories explicitly; whichever is chosen, a single version of each shared component at any time keeps dependencies consistent.
- level: decision
- stack: neutral
- sources: S33 (The One-Version Rule; Monorepo versus Multiple Repositories)
- agreement: contested
- positions:
  - Monorepo: one-version is trivial to hold, atomic cross-project change. Held by Google (S33). Force: correctness, speed of change. Wins: one organization, tooling investment, many interdependent projects.
  - Multiple repositories: legal, compliance or security separation. Force: control, security. Wins: regulated or access-segmented work.
  - Virtual monorepo (submodules or Bazel) to keep one-version across repositories (S33).
- boundary: ADOPT (the one-version rule is a dependency rule)
- certainty: grounded (single T2 source for the debate; the other positions are only sketched there)

**DELIVER-C10**
- claim: Commit atomic, complete changes with a message that says what changed and why; keep unrelated changes in separate branches or pull requests.
- level: practice
- stack: neutral
- sources: S15 (Make changes; Key Recommendations), S07 (Documentation of change descriptions)
- agreement: consensus
- certainty: grounded

**DELIVER-C11**
- claim: Use a structured commit message format only if release notes or version bumps are generated from history; otherwise a free-form message that states what and why suffices.
- level: decision
- stack: neutral
- sources: S29 (Specification, benefits), S28 (mapping), S07
- agreement: contested
- positions: Conventional Commits: automated changelog, semantic version bump, build triggers (S29); force: automation, speed of release. Free-form (Google review guidance: describe what and why, S07); force: cognitive load. Wins for structured: libraries with many consumers and automated releases. Source for the free-form position is review guidance, not a rule against structure (inferred).
- certainty: grounded on the spec's claims; the choice rule is inferred

**DELIVER-C12**
- claim: Version an artifact with Semantic Versioning only when it has a declared public API consumed by others; deployed services with a single live version need a release identifier (build number or timestamp), not a compatibility promise.
- level: decision
- stack: neutral
- sources: S28 (Prerequisites, 0.y.z), S05 (release IDs)
- agreement: majority
- positions: SemVer for libraries and APIs (force: consumer trust, exit risk reduction). Monotonic release ID for services (S05). Calendar versioning not read (open).
- certainty: grounded for SemVer and release IDs; the service rule is inferred from S28 plus S05

**DELIVER-C13**
- claim: Every change to mainline gets an independent human check (second reviewer, pair, or equivalent) at or before integration; the check is a feature of the development platform's record, not an out-of-band approval.
- level: principle
- stack: neutral
- sources: S07 (How Google does it), S19 (Key Recommendations), S43 (Code Review as Final Human Gate), S44
- agreement: majority
- positions: see C14 for the mechanism; the only source dissent on the principle is Ship/Show/Ask (S23), which keeps review for uncertain changes only.
- certainty: grounded

**DELIVER-C14**
- claim: Choose a review mechanism per team and change risk: mandatory asynchronous pull-request approval, synchronous review or pairing, or ship/show/ask, and record the choice.
- level: decision
- stack: neutral
- sources: S07, S43, S03 (synchronous review), S44, S23, S19
- agreement: contested
- positions:
  - Mandatory approval by another engineer on every change (Google S07, Amazon S43, GitHub required reviews S42). Argument: confidence, knowledge sharing, an audit trail. Wins: larger or less-trusting teams, regulated change control, many contributors.
  - Synchronous review or pairing (DORA S03: "perform synchronous code review"; S44: "pair by default", PR review for exceptions). Argument: immediacy, no review queue, no context switching, no sunk-cost deadlock. Force: speed of feedback. Wins: small collocated or remote-pairing teams with trust.
  - Ship / Show / Ask (S23): merge without approval for routine changes, show after checks, ask when uncertain. Argument: approvals are a band-aid for missing trust and bottleneck the team. Force: delivery speed. Wins: high trust, strong CI/CD, mainline always releasable; more asking for juniors and new techniques.
  - DORA warns against heavy review requiring several approvals (S03 pitfalls).
- certainty: grounded

**DELIVER-C15**
- claim: Approve a change when it definitely improves overall code health, even if imperfect; technical facts and data overrule preference, and optional suggestions are marked as such.
- level: practice
- stack: neutral
- sources: S04 (Core Approval Standard, Key Insight on Polish)
- agreement: consensus (one T2 source, no opposing source found)
- certainty: grounded

**DELIVER-C16**
- claim: Respond to a review request within one business day at most, and prefer quick individual responses over a fast whole process; optimize team throughput, not one author's speed.
- level: practice
- stack: neutral
- sources: S25 (Response Time Standard), S07 (Review Latency: 24 working hours)
- agreement: consensus
- certainty: grounded

**DELIVER-C17**
- claim: Keep changes small, about 100 lines being typical and 1000 too large, with refactoring in separate changes and tests in the same change as the logic they cover.
- level: practice
- stack: neutral
- sources: S26 (Size Thresholds, Separating Refactoring, Tests), S07 (about 200 lines), S21 (hours to a couple of days of work)
- agreement: consensus
- certainty: grounded (thresholds differ between sources: 100, 200 lines)

**DELIVER-C18**
- claim: Let automation (format, lint, tests, build) run before human review so reviewers spend their attention on design and logic.
- level: practice
- stack: neutral
- sources: S07 (Automation Focus), S09 (Presubmit)
- agreement: consensus
- certainty: grounded

**DELIVER-C19**
- claim: Treat review as a tool for understanding and knowledge transfer as well as defect finding, and require that changes be understandable to a second reader.
- level: principle
- stack: neutral
- sources: S36 (Primary Motivation vs Actual Outcomes), S07 (Comprehension, Knowledge Sharing)
- agreement: consensus
- certainty: grounded

**DELIVER-C20**
- claim: Do not rely on an external change approval board for per-change approval; meet segregation of duties through peer review, automated testing and monitoring, and treat changes by their risk rather than uniformly.
- level: decision
- stack: neutral
- sources: S19 (all)
- agreement: majority
- positions: external CAB (traditional, regulated settings) versus peer review plus automation (DORA, which found no correlation of external review with lower failure rates and a negative effect on delivery performance). Force: control and regulation versus delivery speed. Whether a specific regulation still requires a board was not read (open); DORA says to shift the board to an advisory role.
- certainty: grounded for DORA; open for regulation

**DELIVER-C21**
- claim: Run an automated build and a self-testing test suite on every push to mainline in a reference environment, not only on developer machines.
- level: principle
- stack: neutral
- sources: S01 (Make the Build Self-Testing; Trigger Automated Build), S16 (Core Practices)
- agreement: consensus
- boundary: VERIFY (what the tests contain)
- certainty: grounded

**DELIVER-C22**
- claim: Keep integration feedback to minutes (build around ten minutes, automated tests in a few minutes) and decide explicitly which tests gate a merge and which run after.
- level: decision
- stack: neutral
- sources: S01 (Keep Builds Fast), S16 (pitfall: tests over 10 minutes), S09 (Presubmit Strategy), S35 (increasing confidence at cost of time)
- agreement: contested
- positions:
  - Gate on everything that is fast and reliable, run slower tests after merge and roll back on failure; accepts some loss of coverage (Google S09; about 95% of changes pass presubmit). Force: speed of feedback. Wins: very high change volume, a build cop, automatic rollback.
  - Staged pipeline where later stages are slower but more thorough and parallelized (S35, S01). Force: confidence. Wins: smaller change volume.
  - DORA pitfall: tests over ten minutes (S16).
- certainty: grounded

**DELIVER-C23**
- claim: A broken mainline is the highest-priority work; revert the faulty change to restore it, and name someone responsible for restoring it.
- level: practice
- stack: neutral
- sources: S01 (Fix Broken Builds Immediately), S16, S09 (Build Cop, Automatic rollbacks)
- agreement: consensus
- certainty: grounded

**DELIVER-C24**
- claim: Treat flaky tests as defects of the pipeline: classify, retry or disable temporarily during investigation, because flakes erode trust as broken tests do.
- level: practice
- stack: neutral
- sources: S09 (Flaky Tests Challenge)
- agreement: consensus (one source)
- boundary: VERIFY
- certainty: grounded

**DELIVER-C25**
- claim: Make build and pipeline state, and the flow of changes, visible to the whole team, with an audit trail.
- level: practice
- stack: neutral
- sources: S01 (Ensure Visibility), S16, S35 (Visibility and Collaboration)
- agreement: consensus
- certainty: grounded

**DELIVER-C26**
- claim: Make builds scripted, repeatable and hermetic: the same revision built on different machines yields the same result, with no dependence on machine-specific state.
- level: principle
- stack: neutral
- sources: S06 (Hermetic Builds), S01 (Automate the Build), S31 (reproducible builds)
- agreement: consensus
- certainty: grounded

**DELIVER-C27**
- claim: Separate build, release and run stages; make every release immutable and uniquely identified; deploy the same built artifact to every environment, with environment-specific configuration kept outside it.
- level: principle
- stack: neutral
- sources: S05 (all), S17 (any version of the artifact to any environment; config separate), S06 (Packaging)
- agreement: consensus
- certainty: grounded for separation, immutability, release ID, config split; "build once, promote the same artifact" is inferred from S05 and S17 (S35 does not state it)

**DELIVER-C28**
- claim: Set a target build-integrity level by risk: at least provenance (SLSA Build L1), hosted build platform with signed provenance (L2) for anything distributed, and hardened isolated builds (L3) where insider or credential-compromise risk matters.
- level: decision
- stack: neutral
- sources: S10 (L0-L3), S34 (limits: no transitive trust)
- agreement: consensus on the ladder; the level per project is the team's decision
- boundary: ADOPT (supply chain)
- certainty: grounded; which level a given team needs is inferred

**DELIVER-C29**
- claim: Protect code and its release integrity and archive releases, as required by secure development frameworks (SSDF practices PS.1 protect code, PS.2 release integrity, PS.3 archive, PW.7 review code, PW.8 test).
- level: principle
- stack: neutral
- sources: S24 (practice names only; text of practices not retrieved)
- agreement: consensus
- boundary: TRANS
- certainty: grounded on the names; open on the exact content (fetch returned names only)

**DELIVER-C30**
- claim: Release in small, frequent batches; decide cadence from the release model: every merge, a regular train, or explicit versions.
- level: decision
- stack: neutral
- sources: S08 (Velocity, Release Cadence), S40 (all), S06 (High Velocity), S22 (release on demand), S18, S14
- agreement: contested
- positions:
  - Continuous: release each merge; "faster is safer", frequency reduces difficulty (S08, S40, S22, S06). Force: delivery speed, reversibility, small blast radius. Wins: one live version, automation in place, strong tests.
  - Scheduled train (Google Search "every other day"; missed train means wait for the next, S08). Force: predictability, low pressure. Wins: many components, coordination across teams.
  - Explicit versions with several supported (S14). Force: consumer control. Wins: shipped products and libraries.
  - DORA warning: more frequency without supporting practices raises failure rate and burnout (S22).
- certainty: grounded

**DELIVER-C31**
- claim: Decouple release (making a feature available) from deployment (shipping code) with flags, so a feature can be turned off without redeploying.
- level: practice
- stack: neutral
- sources: S08 (Feature Flags), S13 (Release and Ops Toggles), S21 (dark launching)
- agreement: majority
- positions: alternative is no flags with small, immediately released batches (S40 style); cost of flags is testing burden (C32). Force: reversibility versus cost of ownership.
- certainty: grounded

**DELIVER-C32**
- claim: Treat feature toggles as inventory with a carrying cost: classify them (release, experiment, ops, permission), give release toggles an expiry, and test the relevant toggle states.
- level: practice
- stack: neutral
- sources: S13 (Lifetime; Testing and Inventory Costs)
- agreement: consensus (one source)
- certainty: grounded

**DELIVER-C33**
- claim: Build the path to production as one automated pipeline of stages with increasing confidence; decide per stage whether it needs human authorization.
- level: decision
- stack: neutral
- sources: S35 (all), S43 (hands-off), S17, S06 (Enforcement of Policies)
- agreement: contested
- positions:
  - Hands-off: code review is the last manual gate, the rest automated and driven by alarms (Amazon S43). Force: delivery speed, reduced error. Wins: mature automation and monitoring.
  - Human authorization gates for some stages (S35). Force: control. Wins: high criticality, regulation, low confidence in automation.
  - Access control on who may release stays in either (S06).
- certainty: grounded

**DELIVER-C34**
- claim: Restrict by policy who can perform release operations, while keeping release itself self-service for teams.
- level: practice
- stack: neutral
- sources: S06 (Self-Service Model; Enforcement of Policies)
- agreement: consensus (one source)
- certainty: grounded

**DELIVER-C35**
- claim: Keep environment-specific configuration separate from the deployable package.
- level: practice
- stack: neutral
- sources: S17 (Key Practices)
- agreement: consensus
- boundary: TRANS (configuration and secrets)
- certainty: grounded

**DELIVER-C36**
- claim: Automate deployment with the same process for every environment, production included; any authorized person can deploy any version on demand; steps are idempotent and order-independent; scripts are versioned.
- level: principle
- stack: neutral
- sources: S17 (Key Practices), S01 (Automate Deployment), S06 (Deployment)
- agreement: consensus
- certainty: grounded

**DELIVER-C37**
- claim: Choose a rollout strategy by blast radius and cost: blue-green for instant switch and rollback, canary for gradual exposure with evaluation, wave or one-box rollout for many regions.
- level: decision
- stack: neutral
- sources: S11, S12, S43 (One-box, Waves, Bake Time), S31, S08 (Progressive Rollouts)
- agreement: contested
- positions:
  - Blue-green: switch the router back to roll back; doubles as disaster-recovery rehearsal; costs a second production environment and missed-transaction handling (S11). Force: reversibility, speed of recovery. Wins: stateful downtime-sensitive apps with budget for two environments.
  - Canary: expose a small share first, observe real traffic, no separate test environment for capacity; costs several live versions and schema coordination; do not conflate with A/B tests (S12). Force: confidence, security of blast radius. Wins: high traffic, good metrics.
  - One-box then waves with bake time of hours (S43). Force: blast radius across regions. Wins: multi-region services.
  - Google: stage rollouts to growing percentages and canary even for the release itself (S08).
- certainty: grounded

**DELIVER-C38**
- claim: Evaluate a canary against a concurrent control group on a small set of metrics tied to user impact (not before/after comparison), run one canary at a time, and size population and duration to velocity and traffic.
- level: practice
- stack: neutral
- sources: S31 (Population Size and Duration; Metric Selection)
- agreement: consensus (one source)
- boundary: OPERATE
- certainty: grounded

**DELIVER-C39**
- claim: Automate detection of bad releases and rollback from alarms, and decide in advance when rolling back is preferable to fixing forward.
- level: decision
- stack: neutral
- sources: S41, S43 (Automated Rollback), S31 (Rollback Criteria), S02 (fix forward), S33 (redeploy fixes from trunk), S26 (small changes roll back simply)
- agreement: contested
- positions:
  - Automated rollback on alarm (Google S41 and S31, Amazon S43). Force: reversibility, recovery time. Wins: any change that is backward compatible (see C40).
  - Fix forward from trunk (TBD S02, S33 under continuous deployment). Force: simplicity, no release branch. Wins: very fast pipeline, changes not reversible by redeploy (data migrations).
  - No source read states the decision rule between them; the wins-when conditions are inferred.
- certainty: grounded on positions; the rule is inferred

**DELIVER-C40**
- claim: Make each change backward compatible with the previous version (parallel change: expand, migrate, contract; schema changes separate from application releases) so rollback, mixed fleets and independent release are safe.
- level: practice
- stack: neutral
- sources: S32 (all), S11 (Database Caveats), S43 (Backward Compatibility Testing), S12 (Database Challenges)
- agreement: consensus
- certainty: grounded

**DELIVER-C41**
- claim: Block deployments during active incidents and outside the hours when responders are available.
- level: practice
- stack: neutral
- sources: S43 (Bake Time and Blocking)
- agreement: consensus (one T3 source, not cross-checked)
- certainty: grounded

**DELIVER-C42**
- claim: Keep production and pre-production alike in type and version of backing services, operating system and libraries, and keep developers close to deployment; decide how much pre-production to maintain versus relying on progressive rollout in production.
- level: decision
- stack: neutral
- sources: S30 (all), S01 (Test in Production-Clone Environments), S12 (Production-Like Testing), S17 (identical process)
- agreement: contested
- positions:
  - Production parity in all environments, including local backing services (S30, S01). Force: confidence, correctness. Wins: stateful systems where adapters hide incompatibilities.
  - Reduce pre-production, test in production with a canary and a safe rollback (S12). Force: cost of ownership, fidelity of real traffic. Wins: high traffic, strong monitoring, fast rollback.
  - Gap in time and personnel also matters: code reaches production in hours, developers deploy (S30).
- certainty: grounded

**DELIVER-C43**
- claim: Replace deployed instances rather than modifying them; manage base images and infrastructure as versioned code to avoid configuration drift.
- level: practice
- stack: neutral (infrastructure with image-based provisioning)
- sources: S39 (Immutable Server), S05 (immutable releases), S20 (script infrastructure provisioning)
- agreement: majority
- positions: immutable replacement (force: consistency, reversibility; needs external config, separate data persistence, fast provisioning) versus managed mutable servers with configuration tools (drift risk, S39). Wins for mutable: stateful hosts where replacement is costly (inferred).
- certainty: grounded

**DELIVER-C44**
- claim: Where the platform supports it, hold desired state declaratively and immutably in version control and have agents pull and continuously reconcile it, rather than pushing deploys from CI.
- level: decision
- stack: neutral in principle; realized with orchestrators that reconcile desired state
- sources: S27 (four principles), S17 (deployment automation)
- agreement: contested
- positions: pull and reconcile (S27). Argument: drift is corrected and history is auditable. Force: control, security. Push from CI (S17, S01): a simple scripted deploy; force: cost of ownership. No source read compares them (open); wins-when is inferred.
- certainty: grounded on the principles; the comparison is open

**DELIVER-C45**
- claim: Manage database changes as part of the same pipeline as application changes.
- level: practice
- stack: neutral
- sources: S22 (Key Technical Practices: database change management), S11, S32
- agreement: majority
- certainty: grounded on the listing; detail in S11 and S32
- boundary: VERIFY (test data management)

**DELIVER-C46**
- claim: Measure delivery with the five DORA metrics: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate; use them to guide improvement, not to rank people.
- level: principle
- stack: neutral
- sources: S18 (Five Metrics)
- agreement: consensus
- certainty: grounded on the metrics; "not to rank people" is inferred (not stated in the fetched text)

**DELIVER-C47**
- claim: Treat speed and stability as correlated rather than traded off, but only with supporting practices; raising deployment frequency alone yields failures and burnout.
- level: principle
- stack: neutral
- sources: S18 (Speed vs Stability), S22 (Common Pitfalls, J-curve)
- agreement: majority
- positions: DORA: top performers are good on all five; Farley: the trade is better faster versus worse slower. Qualified by S22. The conventional view (speed versus stability) is what S18 argues against; no source read defends it.
- certainty: grounded

**DELIVER-C48**
- claim: Design services so they can be deployed independently, without orchestrated lock-step upgrades; loose coupling is among the strongest predictors of continuous delivery.
- level: principle
- stack: neutral
- sources: S22 (Key Technical Practices), S17 (Key Practices; Pitfalls: dependencies)
- agreement: consensus
- boundary: application architecture (out of scope; recorded as a pointer)
- certainty: grounded

**DELIVER-C49**
- claim: With AI-generated code, keep batches small and commit frequently, because high code volume can lead to oversized changes and delayed commits that remove the safety net of history.
- level: practice
- stack: neutral
- sources: S20 (Pitfalls), S21 (Common Pitfalls)
- agreement: consensus (one program, two pages)
- certainty: grounded

**DELIVER-C50**
- claim: Assume most outages come from changes to a live system, and therefore spend automation on progressive rollout, fast detection and safe rollback.
- level: principle
- stack: neutral
- sources: S41 ("roughly 70% of outages are due to changes in a live system")
- agreement: consensus (one T2 source)
- certainty: grounded

### Gaps (open)

- Merge method (C07), rollback versus fix forward rule (C39), push versus pull deploy comparison (C44), calendar versioning (C12): no source read ranks the alternatives.
- Regulation requiring change boards (C20): not read.
- SSDF content (C29): only practice identifiers retrieved.
- Mobile or client-installed software releases: S12 mentions the difficulty only.
- Merge queues, stacked pull requests, and release tooling (GitHub Actions, GitLab CI, Jenkins): not read; stack pointers for stack guidelines.
- Empirical evidence on review effectiveness beyond one study (S36); evidence on the numerical thresholds (100 versus 200 lines) is absent.
- Humble and Farley, Accelerate (books): not read directly.
- Authors of Fowler-hosted articles not written by Fowler were not in the fetched text (inferred).
