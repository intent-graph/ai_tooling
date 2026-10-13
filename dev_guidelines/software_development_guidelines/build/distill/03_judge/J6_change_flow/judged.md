# J6_change_flow: judge records

Unit: the eight L2 nodes of CHANGE_FLOW (INTEGRATION, REVIEW, BUILD, RELEASE, DEPLOY, ROLLBACK, DATA_CHANGE, MEASURE) and their 34 L3 nodes: 42 records in tree order. The L1 node CHANGE_FLOW is rolled up from its judged children in wave 3 and is not judged here. Rows: ledger ids L001-L460, L1001-L1289, L1501-L1565; sources by register id (REG-nnn). The maintainer's codified practice is source MAINT-S01 (REG-181, not citable): a strong position, never an automatic winner; a decision resting only on it is marked inferred. Rules that bind: MD-01 (the best, not the average), MD-02 (outcomes, whoever does the work), MD-03 (this branch holds procedures; guarantees stay in the decision nodes).

Decided inputs read (settled, not re-decided): ASSURANCE.RULES.1 to .5 (J2): blocking checks that fail closed, review independent and bound to content with a named accountable person and a defined low-risk post-merge tier, one bar for every change with evidence; ASSURANCE.CONTRACTS.1 (J2): compatibility defined by consumer reach; ASSURANCE.DATA_INTEGRITY.1 to .5 (J3): store-side invariants, explicit scope for bulk and destructive operations, a destructive change is undone by a prepared and tested restore, a sync plan for derived data, observe-first for new checks; ASSURANCE.SECURITY.6 (J3): limits enforced in tooling, and a large-blast-radius job either runs under enforced guards or is run by a person from a reviewed script; ASSURANCE.AVAILABILITY.3 to .5 and ASSURANCE.ARTIFACT.1, .2 (J4): progressive and tested resilience, proven restore, verified provenance, a mainline that binds every actor. Cross-unit fixes read: X1 to X3 (none touches this unit).

Pinned:
- Nodes judged: 42 (CHANGE_FLOW.INTEGRATION and .1 to .6; REVIEW and .1 to .4; BUILD and .1, .2; RELEASE and .1 to .5; DEPLOY and .1 to .4; ROLLBACK and .1 to .3; DATA_CHANGE and .1 to .8; MEASURE and .1, .2).
- Decisions marked undecided: none.
- Flags raised: 13 (F1 to F13), all settled in the final pass; none remains (see the section at the end).
- Settled decisions disagreed with: none.

Reading note. Where a node holds several independent rows, the Decision is a lead of one to three sentences and may be followed by sub-decisions; the lead is the node's claim. "Context" is filled only where a row shows the best differs with a condition. Tier words follow the ledger (T1 first-party or standard, T2 practitioner or research, T3 single practitioner or vendor).

---

## CHANGE_FLOW.INTEGRATION Version Control and Integration

Intent: how work is held in version control and merged into one mainline: repository content, branch life, merge method, mainline health, attribution.

1. **Decision.** Everything needed to build, deploy and restore lives in version control; work is integrated into one mainline in small, frequent, attributable changes, and a broken mainline is fixed before anything else. Outcome: the repository alone rebuilds the system, history serves reading and reversal, and each change has a known author and approver.
2. **Grounds.** Roll-up of INTEGRATION.1 to .6 (18 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable (roll-up).
5. **Context.** None here; contributor model moves .2, release model moves .3.
6. **Certainty.** Inferred as a roll-up (own certainty); principles grounded in the children, numeric defaults inferred.
7. **Flags.** none.

Links: Realizes ASSURANCE.RULES (mechanism for RULES.3 and RULES.4 on the mainline is ARTIFACT.2).

### CHANGE_FLOW.INTEGRATION.1 Repository Content and Shape

Intent: what the repository holds so the system can be rebuilt from it, and how repositories are cut so that one version of each shared component holds.

1. **Decision.** Keep everything needed to build, deploy and restore (source, scripts, infrastructure and application configuration, dependency declarations) in version control; a clean machine builds from the repository alone. Each deployable application has one codebase and many deploys; code shared across applications is a versioned library, and whatever repository layout is chosen keeps one version of each shared component at any time. Outcome: reproducible rebuild and recovery from one place, and consistent dependencies.
2. **Grounds.** Consensus on content (L124; REG-077, REG-092, REG-095) and on one codebase per deployable (L1190; REG-1109). The one-version invariant is what L132 states for every layout (REG-106, single T2 source for the layout debate).
3. **Positions.** P1 everything in version control (reproducibility). P2 one codebase per application (ownership). P3 monorepo (atomic cross-project change). P4 multiple repositories (control, security). P5 virtual monorepo (one version across repositories).
4. **Rejected.** No layout is rejected as such: the layout is a means to the invariant. Monorepo is best for one organization with tooling investment and many interdependent projects; multiple repositories are best for regulated or access-segmented work; a virtual monorepo is best when separate repositories are required and one version still must hold. A repository that omits scripts, configuration or infrastructure needed to rebuild: best never.
5. **Context.** Access segmentation (L132): regulated or access-segmented work moves the layout to multiple repositories; the invariant stays.
6. **Certainty.** Grounded for P1 and P2 (consensus); inferred that a monorepo holds "one codebase per application" as one unit per deployable with its own build and deploy; the layout debate rests on one T2 source (open on which layout wins in general).
7. **Flags.** none.

Constraints: MUST a clean checkout build and deploy without machine-specific state; MUST one version of each shared component hold at any time. Links: Related OWNERSHIP.LIFECYCLE (the one-version rule is a dependency rule).

### CHANGE_FLOW.INTEGRATION.2 Integration Frequency and Branch Life

Intent: how often work is merged into the mainline, how long a branch may live, and how unfinished work is kept from blocking that.

1. **Decision.** Integrate into one mainline at least daily; a branch lives hours to a couple of days, and long-lived development branches are avoided. Work that spans more than the integration interval is merged hidden behind a flag, dark launch, keystone or branch by abstraction, not held in a branch. Outcome: early feedback, small conflicts, and a mainline that always holds the latest integrated work.
2. **Grounds.** Many small integrations reduce conflict cost and give early feedback (L125; REG-057, REG-077, REG-078, REG-079, REG-106); long-lived branches cost more in merges, regression isolation and large-scale change (L128, consensus; REG-079, REG-106, REG-110); hiding unfinished work keeps integration continuous (L129; REG-077, REG-078, REG-089, REG-096). The strongest argument is the cost curve of deferred integration; the opposing position is a condition, not a rival.
3. **Positions.** P1 daily integration, short branches (feedback). P2 feature branches merged when complete (control, low coordination cost). P3 avoid long-lived branches. P4 hide unfinished work in the mainline (carrying cost of toggles).
4. **Rejected.** P2 as the general rule: it defers integration risk rather than removing it. Best for open source with many untrusted or part-time contributors, and for features of one to two days (L125; REG-110). Daily integration without good automated tests: it only multiplies conflict-free merges of unchecked code; best preceded by the trust signal of RULES.1.
5. **Context.** Contributor model (full-time team versus sparse or untrusted contributors) and test maturity (L125): sparse contributors and short features keep a feature branch merged when complete; full-time teams with good tests integrate daily.
6. **Certainty.** Grounded (consensus on avoiding long-lived branches, majority on daily merge, DORA); the "three or fewer active branches" figure is a DORA default, inferred as a bound.
7. **Flags.** none.

Constraints: MUST a branch be merged or deleted within days (the limit is the team's, default a couple of days); MUST unfinished work on the mainline be hidden and its toggle carry an owner and an expiry (RELEASE.3). Links: Related RELEASE.3 (flags), ASSURANCE.RULES.2 (small feedback loops).

### CHANGE_FLOW.INTEGRATION.3 Branching Model and Release Branches

Intent: which branching model the release model calls for, and whether and how a release branch exists.

1. **Decision.** Follow the release model. For one live version delivered continuously: trunk-based flow with short-lived branches and no release branch; a defect is fixed on the mainline and redeployed (fix forward). Where software is explicitly versioned or several versions are supported in the field: a release branch, cut only just in time, defects fixed on the mainline and cherry-picked into it, deleted after release and never merged back. Outcome: one place where change happens, and a branch that exists only for as long as a version needs separate fixes.
2. **Grounds.** Trunk or GitHub flow for continuous delivery, including its originator's own retraction for that case (L126; REG-078, REG-090, REG-091, REG-106); release branches by the number of versions in the field (L126; REG-090); just-in-time cut, cherry-pick, delete (L127; REG-078, REG-082, REG-106).
3. **Positions.** P1 trunk or GitHub flow (speed, low cognitive load). P2 release branches git-flow style (control, several versions). P3 just-in-time release branch. P4 no release branch, fix forward (simplicity).
4. **Rejected.** Standing release branches for a single live version: they add merge cost for no version to support; best only when versions are in the field. P4 for a supported-versions product: a fix to an old version has nowhere to land; best when the release cycle is hours.
5. **Context.** Release model (L126): continuous single live version versus several supported versions. P3 is how P2 is done, not a rival to it.
6. **Certainty.** Grounded for the split by release model (T1/T2 sources, the originator's own statement); inferred that P3 is the form P2 takes.
7. **Flags.** none.

Constraints: MUST a release branch (when it exists) receive fixes by cherry-pick from the mainline, not by merge back. Links: Related RELEASE.1, ROLLBACK.1 (fix forward).

### CHANGE_FLOW.INTEGRATION.4 Merge Method and Commit Practice

Intent: how changes are merged and how a commit states what it holds, so history serves reading, reversal and automation.

1. **Decision.** The unit of integration is one logical change that can be read and reverted as one unit; each commit is atomic and complete, and its message says what changed and why; unrelated changes go in separate branches or pull requests. One merge method is chosen per repository and recorded: squash for small one-logical-unit changes (the default when changes are kept small, INTEGRATION.5 and REVIEW.2), rebase when commits are well-structured atomic commits worth keeping, merge commit when integration events must be traced. A structured message format (Conventional Commits) is used only when release notes or version bumps are generated from history. Outcome: history that can be read, bisected, reverted and, where needed, read by tools.
2. **Grounds.** Atomic commits with what and why (L133, consensus; REG-083, REG-091); the three methods each trade fidelity against simplicity (L130; REG-109, REG-114); structured messages serve automation only when automation exists (L134; REG-030, REG-102). No source ranks the three methods; the squash default follows from small units and simple revert and is inferred.
3. **Positions.** P1 squash (cognitive load, reversibility). P2 rebase (bisect granularity). P3 merge commit (fidelity, audit). P4 atomic commits with what and why. P5 Conventional Commits when releases are generated. P6 free-form what and why.
4. **Rejected.** Each method is best under its row's condition (above). A mandatory structured format without a generator: it costs every author and serves nobody. Several methods mixed in one repository without record: the history then has no reading rule; best never.
5. **Context.** Whether integration events must be traced (merge commit), whether commits are well structured (rebase), whether history is parsed by automation (structured message).
6. **Certainty.** Grounded for atomic commits and the structured-message condition; inferred for the squash default; open on a winner among the three methods (no source read ranks them). The maintainer's mandatory unit header with a dated change log (L318, routed elsewhere) is in partial tension with free-form messages and is not decided here.
7. **Flags.** none.

Constraints: MUST one merge method be recorded per repository; MUST a commit be atomic and say what and why. Links: stack pointer L130 (GitHub terms); Related INTEGRATION.5.

### CHANGE_FLOW.INTEGRATION.5 Mainline Health and Batch Size

Intent: what keeps the mainline usable and the batches small so version control stays the safety net as volume rises.

1. **Decision.** A broken mainline is the highest-priority work: the faulty change is reverted to restore it and a named person owns the fix. Batches stay small, commits frequent and rollback routine, and the rule tightens as change volume rises, whoever or whatever produces the change. Outcome: the mainline is always releasable and any change can be undone cheaply.
2. **Grounds.** Fix or revert a broken build first (L146; consensus, REG-057, REG-077, REG-085); small batches and routine rollback at volume (L1057; REG-1041, REG-181) and the same rule for generated code (L172; REG-095, REG-096), merged here as one author-neutral rule.
3. **Positions.** P1 broken mainline first (consensus). P2 small batches, frequent commits, routine rollback (majority). P3 the same for generated code.
4. **Rejected.** No competing position recorded. Letting a broken mainline wait for the author: best never, since every later integration is blind.
5. **Context.** none.
6. **Certainty.** Grounded for P1 (consensus); grounded as majority for P2 (one program plus the maintainer); the causal link volume to oversized batches is inferred.
7. **Flags.** none.

Constraints: MUST a broken mainline be reverted or fixed before new work merges. Links: Related REVIEW.2 (small units protect review), ROLLBACK.2 (routine rollback).

### CHANGE_FLOW.INTEGRATION.6 Change Attribution and Actor Rules

Intent: how each change stays attributable to an author and an approver, and which actors may do what, whoever authored the change.

1. **Decision.** Every change carries a platform-recorded trail: who or what authored it, who approved it, and, for an automated author, which tool and session. Automation uses identities distinct from human ones; a change not attributable to a person needs an additional approval by a named, accountable person; the actors (human, bot, agent) and what each may do in the change flow are stated. No disclosure rule is needed: the same bar and the same gates apply to every change, and the recorded trail gives the benefit of disclosure without relying on declarations. Outcome: any change is traceable to an accountable party, and the bar does not depend on origin.
2. **Grounds.** Attributable record (L1061; REG-1036, REG-1040, REG-114), distinct identities and added approval (L1062; REG-1036, one vendor, platform-specific mechanism), stated actor boundaries (L1076; REG-1035, REG-1037, REG-1041); one bar for everyone is ASSURANCE.RULES.5 (L1042) and a named accountable person is ASSURANCE.RULES.4 (L1043). The row-level note that a platform trail gives P4's benefit is the deciding argument against a declaration rule.
3. **Positions.** P1 attributable record. P2 distinct identities, added approval. P3 stated actor boundaries. P4 mandatory disclosure of tool use (reviewer calibration, provenance). P5 no disclosure rule, same bar (simplicity).
4. **Rejected.** P4 as the general rule: declarations can be omitted and add friction; best where reviewer time is scarce and intake is public (open contribution), where it lets a reviewer calibrate depth (L1077 a). Shared human-and-bot identities: best never, attribution is lost.
5. **Context.** Reviewer capacity and public intake (L1077): scarce reviewers with public intake favour a recorded disclosure on top of the trail.
6. **Certainty.** Grounded for the trail and distinct identities (majority, vendor documentation, mechanism platform-specific); inferred for the author-neutral phrasing of L1076 and for the choice of P5 over P4 (one maintainer ruling, one inference).
7. **Flags.** none.

Constraints: MUST an automated author use an identity distinct from a human one; MUST an unattributed change be approved by a named person; MUST NOT the bar depend on who authored. Links: Related ASSURANCE.SECURITY.6 and ARTIFACT.2 (limits and mainline binding), REVIEW.1; stack pointer L1062 (one hosting platform's mechanism).

---

## CHANGE_FLOW.REVIEW Review

Intent: how review is carried out: mechanism and depth by risk, unit size, speed, standard, and what runs before the reviewer.

1. **Decision.** Review realizes ASSURANCE.RULES.4: independent, accountable, bound to the exact content. The mechanism (asynchronous approval, synchronous review or pairing, show-after-merge for the low-risk tier) follows team and risk; depth follows risk and evidence of understanding; units are small and answered quickly; automation runs first and a second model assists but never approves. Outcome: the review was trustworthy and review capacity is not the constraint.
2. **Grounds.** Roll-up of REVIEW.1 to .4 (11 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable (roll-up).
5. **Context.** Team size and trust, criticality, scale (on the children).
6. **Certainty.** Inferred as a roll-up; grounded in the settled RULES.4 and the children.
7. **Flags.** none.

Links: Realizes ASSURANCE.RULES.

### CHANGE_FLOW.REVIEW.1 Mechanism and Depth by Risk

Intent: which review mechanism applies to a change and how deep it goes, set by risk and by evidence that the submitter understands the change.

1. **Decision.** One bar for every change (RULES.5), an independent party checks each change before integration (RULES.4); the mechanism is chosen per team and recorded: mandatory asynchronous approval, or synchronous review or pairing recorded on the platform, with show-after-merge allowed only for the low-risk tier RULES.4 defines. Depth is set by risk and by evidence that the submitter understands the change, and rises where that cannot be assumed. A change with a large blast radius (it holds locks, runs longer than the team's time budget, or can affect availability) is approved by named approvers qualified for that class; who may run it is held at DATA_CHANGE.3 and RELEASE.5. Outcome: review effort sits where it pays and no high-blast change is approved by someone unqualified for it.
2. **Grounds.** Mandatory approval gives confidence, knowledge sharing and a trail (L137; REG-083, REG-114, REG-115); synchronous review removes the queue (L137; REG-079, REG-116); Ship, Show, Ask is the post-merge tier under strong gates (L137; REG-098), which RULES.4 already admits; depth by evidence of understanding (L1044 b; REG-1040, REG-1043, REG-1044); escalation by risk with named senior approvers (L298, maintainer; agrees with common practice, REG-181).
3. **Positions.** P1 mandatory asynchronous approval. P2 synchronous review or pairing. P3 Ship, Show, Ask. P4 one uniform bar, depth by risk. P5 depth by evidence of understanding. P6 escalate by risk with named senior approvers.
4. **Rejected.** P3 as the general rule: settled against at RULES.4, which holds the reason; best as the post-merge tier for low-risk change with automatic gates and revert. P1 in a small trusted team that pairs: pairing satisfies independence when the second person is recorded; best for larger or less-trusting teams, regulated change control, many contributors. P2 where reviewers are distributed or contributors many. P4 and P5 are one rule seen from two sides (a bar that does not move, an effort that does). "Senior" as a title in P6: restated as a named approver qualified for the class; the title form is best with a small trusted senior group and few critical changes (L298).
5. **Context.** Team size and trust (mechanism); criticality (depth); whether submitter understanding can be assumed (P5): public intake, high volume and many contributors make the deeper review the default.
6. **Certainty.** Grounded for independence and the mechanism conditions (consensus, DORA warns against heavy multi-approval review); inferred for the author-neutral form of L1044 b and for the escalation criterion (maintainer practice agreeing with common practice).
7. **Flags.** none.

Constraints: MUST a high-blast change name its approvers; MUST NOT depth be reduced because the author is trusted or automated. Links: Related INTEGRATION.6, DATA_CHANGE.3 and .8 (L298 and L303 name senior review of locking or long changes), ASSURANCE.RULES.4, RULES.5.

### CHANGE_FLOW.REVIEW.2 Unit of Review and Response Speed

Intent: how big a review unit may be and how fast a reviewer answers, so review capacity does not become the constraint.

1. **Decision.** Keep each unit of review small enough to be read meaningfully (about 100 lines typical, around 1000 too large; the thresholds are the team's), with refactoring in separate changes and tests in the same change as the logic they cover; treat review capacity as the binding constraint when production volume rises. Respond to a review request within one business day at most, preferring quick individual responses and optimising team throughput over one author's speed. Outcome: reviews are real, and waiting is bounded.
2. **Grounds.** Small changes (L140, consensus; REG-083, REG-096, REG-100), review capacity as constraint when volume rises (L1048; REG-1041, REG-1042, REG-1047), response within a business day (L139, consensus; REG-083, REG-099).
3. **Positions.** P1 small changes with thresholds. P2 review capacity as constraint, small units. P3 respond within one business day.
4. **Rejected.** No competing position recorded. Large reviews approved by skim: best never, the review signal then proves nothing (RULES.1).
5. **Context.** none.
6. **Certainty.** Grounded for P1 and P3 (consensus; thresholds differ between sources, 100 and 200 lines, so numbers are inferred defaults); P2 majority, the causal reading inferred.
7. **Flags.** none.

Constraints: MUST a unit of review be small enough to be read in one sitting; MUST a reviewer answer within the team's stated bound. Links: Related INTEGRATION.5 (L172, L1057).

### CHANGE_FLOW.REVIEW.3 What the Reviewer Reads and Approves

Intent: the standard a change is approved against and the material the reviewer reads.

1. **Decision.** Approve a change when it definitely improves overall code health, even if imperfect; technical facts and data overrule preference, and optional suggestions are marked as such. Review also serves understanding: a second reader must be able to understand the change. Review is guided by a maintained catalog of defect patterns read by type of change (table, function, query, index and so on), and the catalog has an owner and is checked for staleness; it doubles as an audit list. Outcome: approvals mean the change is understandable and better, and recurring defect classes are looked for deliberately.
2. **Grounds.** Improve code health, facts over preference (L138; REG-080, one T2 source, no opposing source found); review as understanding and knowledge transfer (L142, consensus; REG-083, REG-108); catalog read by change type (L297, maintainer; read as majority public practice via review checklists; REG-181). The cost noted by the row, a catalog not kept current misdirects review, is the reason for the owner and the freshness check.
3. **Positions.** P1 improve code health. P2 understanding and knowledge transfer. P3 maintained anti-pattern catalog by change type.
4. **Rejected.** No competing position recorded. A catalog without an owner: best never (it then misdirects review). Perfection as the approval bar: slows delivery for no gain in health (P1).
5. **Context.** none.
6. **Certainty.** Grounded for P1 and P2 (consensus, one T2 source for P1); inferred for P3 (maintainer practice; public checklists not fetched).
7. **Flags.** none.

Constraints: MUST a second reader be able to understand the change; MUST the catalog have an owner. Links: Related ASSURANCE.BEHAVIOUR.8 (defect classes that survive review).

### CHANGE_FLOW.REVIEW.4 Automated and Second-Model Layers

Intent: which checks run before the human reviewer and whether a second automated reviewer is added, while accountable review stays with an independent responsible party.

1. **Decision.** Format, lint, tests and build run before human review so the reviewer spends attention on design and logic. A second model reviewing in a fresh context may be added as an extra layer, never as the approver: the accountable approval stays with an independent responsible party, and the extra layer substitutes for no part of it at high risk. Outcome: the human review is spent where machines cannot judge, and approval stays accountable.
2. **Grounds.** Automation first (L141, consensus; REG-083, REG-085); second reviewer as added layer under human accountability (L1049 a; REG-1038); human gate for approval for independence of failure modes (L1049 b; REG-1036, REG-1040); RULES.4 settled that a machine may assist but is never the accountable party.
3. **Positions.** P1 automation first. P2 second model as extra layer. P3 human-only gate for approval.
4. **Rejected.** A second model as the approving party: best never under RULES.4 (accountability attaches to a person or role). P2 as a replacement for part of the human review: best when volume exceeds human capacity and risk is low, and only as a layer (the human review stays in force); where risk is high P3 alone governs approval.
5. **Context.** Scale (volume beyond human capacity favours the extra layer) and criticality (high risk keeps the human gate sole).
6. **Certainty.** Grounded for P1; inferred for P2 (vendor statements only; no study read on AI-reviewer accuracy: open).
7. **Flags.** none.

Constraints: MUST automated checks run before the reviewer is asked; MUST NOT an automated reviewer be the approving party. Links: Related ASSURANCE.RULES.2 and RULES.4, BUILD.1.

---

## CHANGE_FLOW.BUILD Build and Pipeline

Intent: how the build is scripted, hermetic and visible, and what runs on every push.

1. **Decision.** The build is scripted, repeatable and hermetic, runs with a self-testing suite on every push in a reference environment, is visible to the whole team, and produces one artifact that is promoted unchanged to every environment. Outcome: the same revision gives the same result anywhere, and what is promoted is what was built.
2. **Grounds.** Roll-up of BUILD.1 and .2 (5 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** none.
6. **Certainty.** Inferred as a roll-up; children grounded (consensus).
7. **Flags.** none.

Links: Realizes ASSURANCE.ARTIFACT (provenance and the mainline are decided there).

### CHANGE_FLOW.BUILD.1 Scripted, Hermetic, Visible Build on Every Push

Intent: what every build is, so the same revision gives the same result anywhere and the whole team sees the state of the pipeline.

1. **Decision.** Run an automated build and a self-testing suite on every push to the mainline in a reference environment, not only on developer machines. Builds are scripted, repeatable and hermetic: the same revision on different machines yields the same result, with no machine-specific state. Build and pipeline state and the flow of changes are visible to the whole team, with an audit trail. Outcome: a pass is reproducible and its state is public.
2. **Grounds.** Automated build and suite on every push (L144, consensus; REG-057, REG-077); hermetic repeatable builds (L149, consensus; REG-077, REG-082, REG-104); visibility and audit trail (L148, consensus; REG-057, REG-077, REG-107).
3. **Positions.** P1 build and suite on every push in a reference environment. P2 scripted hermetic builds. P3 visible pipeline with audit trail.
4. **Rejected.** No competing position recorded. A build only on developer machines: best never (not reproducible).
5. **Context.** none.
6. **Certainty.** Grounded (consensus, several sources).
7. **Flags.** none.

Constraints: MUST every push to the mainline trigger the build and suite; MUST a build depend on no machine-specific state. Links: Related ASSURANCE.BEHAVIOUR.1 (what the tests contain), OWNERSHIP.LIFECYCLE (L149, L048 reproducible builds).

### CHANGE_FLOW.BUILD.2 Build Once, Promote One Artifact

Intent: how build, release and run are separated so what is promoted is the one thing that was built.

1. **Decision.** Separate build, release and run stages; releases are immutable and uniquely identified; build once and promote the same artifact to every environment, with environment-specific configuration kept outside it, and verify its provenance before use (ARTIFACT.1). Outcome: what runs in production is the artifact that was tested and reviewed.
2. **Grounds.** L150 and L1191 (consensus; REG-081, REG-082, REG-092, REG-107, REG-1109). "Build once, promote the same artifact" is inferred from REG-081 and REG-092 (REG-107 does not state it); it is what makes ARTIFACT.1 (provenance match to source) checkable per environment.
3. **Positions.** P1 build once, promote. P2 rebuild per environment (named in L1191 as what P1 replaces; no row argues for it).
4. **Rejected.** P2: each rebuild is a different artifact, so tests on one do not cover another; best never for "what runs is what was reviewed".
5. **Context.** none.
6. **Certainty.** Grounded for stage separation and immutable releases; inferred for the promotion rule's wording.
7. **Flags.** none.

Constraints: MUST an artifact be promoted by identity, not rebuilt; MUST configuration live outside the artifact. Links: Realizes ASSURANCE.ARTIFACT; Related RELEASE.2 (release identifier), TRANSVERSE.CONFIG.

---

## CHANGE_FLOW.RELEASE Release

Intent: how a build becomes a release: cadence, identity, flags, staged pipeline, who may release.

1. **Decision.** Releases are small and frequent, identified by what the identifier promises, separable from deployment by flags where needed, passed through one staged automated pipeline with human gates only where the change class needs them, and performed by an authorized group when responders are available. Outcome: a release is small, identifiable, reversible, and not performed blind.
2. **Grounds.** Roll-up of RELEASE.1 to .5 (10 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** Release model moves .1, .2; criticality and test maturity move .4.
6. **Certainty.** Inferred as a roll-up; children grounded or inferred as stated.
7. **Flags.** none.

Links: Realizes ASSURANCE.RULES.

### CHANGE_FLOW.RELEASE.1 Cadence and Batch Size

Intent: how often a release is made and how big it is.

1. **Decision.** Prefer small, frequent releases over large infrequent ones. The cadence follows the release model: one release per merge for one live version with automation and strong tests; a regular train for many components coordinated across teams; explicit versions for shipped products and libraries with several supported. Frequency is raised only together with the supporting practices. Outcome: small blast radius, easy reversal and lower difficulty per release.
2. **Grounds.** Small and frequent (L1200, consensus; REG-082, REG-1110); continuous (L153; REG-082, REG-084, REG-097, REG-112), train (REG-084), explicit versions (REG-090); DORA warning that more frequency without supporting practices raises failure rate and burnout (REG-097, REG-093).
3. **Positions.** P1 continuous (speed, reversibility). P2 scheduled train (predictability). P3 explicit versions (consumer control). P4 the principle across the three.
4. **Rejected.** Large infrequent releases: best never as a goal; a long interval is accepted only as the consequence of P2 or P3. Continuous without tests and automation: raises failure and burnout; best preceded by those practices.
5. **Context.** Release model (L153): every merge, a regular train, or explicit versions.
6. **Certainty.** Grounded for the principle (consensus); the cadence per model rests on a few sources (majority).
7. **Flags.** none.

Constraints: MUST the batch size per release be kept as small as the model allows. Links: Related INTEGRATION.3, MEASURE.1 (L170).

### CHANGE_FLOW.RELEASE.2 Version Identity

Intent: what identifier a release carries and what promise that identifier makes.

1. **Decision.** An identifier promises only what is true: Semantic Versioning only for an artifact with a declared public API consumed by others; for a deployed service with one live version a release identifier (build number or timestamp) that makes no compatibility promise. Outcome: a consumer can trust what a version number says, and a service carries no false promise.
2. **Grounds.** Semantic Versioning for consumed public API (L135; REG-030); build identifier for a single live version (REG-081); the service rule is inferred from REG-030 plus REG-081, and fits CONTRACTS.1 (explicit versioning where consumers are many, external or independent).
3. **Positions.** P1 Semantic Versioning for public API. P2 release identifier for a single live service. P3 calendar versioning (not read in any source).
4. **Rejected.** Semantic Versioning on an internal service nobody consumes by version: it promises a compatibility nobody checks; best when consumers choose when to move. P3: no source read; open, not rejected.
5. **Context.** Release model (L135): single live version versus consumed public API.
6. **Certainty.** Grounded for P1; inferred for P2; open for P3.
7. **Flags.** none.

Constraints: MUST every release have a unique identifier; MUST a version number that promises compatibility be backed by a declared public interface. Links: Related BUILD.2, ASSURANCE.CONTRACTS.1.

### CHANGE_FLOW.RELEASE.3 Separating Release From Deployment

Intent: whether a feature is made available separately from shipping code, and what that costs.

1. **Decision.** Where a feature needs to be turned off without redeploying, or work spans more than the integration interval, decouple release from deployment with flags. Every toggle is inventory with a carrying cost: classified (release, experiment, ops, permission), a release toggle created with an expiry and a removal task at introduction, and the relevant toggle states tested. Outcome: a feature is reversible without a deploy, and toggles do not accumulate.
2. **Grounds.** Flags decouple release from deployment (L154, majority; REG-084, REG-089, REG-096, REG-112; L1201 "where needed", REG-089); toggles as inventory (L155, L1201; REG-089, single source, no dissent found).
3. **Positions.** P1 flags (reversibility). P2 no flags, small batches released immediately (cost of ownership). P3 toggles as inventory.
4. **Rejected.** P2 as a universal: best when batches are small, rollback by redeploy is fast and no work spans the integration interval. Flags without expiry: best never, every toggle then adds a state to test forever.
5. **Context.** none stated beyond "where needed" above.
6. **Certainty.** Grounded for P1 (majority); P3 single source (REG-089), inferred as the general rule.
7. **Flags.** none.

Constraints: MUST a release toggle carry an expiry and a removal task; MUST the states that can occur in production be tested. Links: Related INTEGRATION.2 (L129), EVOLUTION.DECOMMISSION (toggle expiry).

### CHANGE_FLOW.RELEASE.4 Staged Pipeline and Human Gates

Intent: how the path to production is staged and which stages need a person's authorization.

1. **Decision.** One automated pipeline of stages: early stages give fast feedback, later stages more confidence. Authorization after a reviewed merge is automated by default; a human authorization gate sits on a stage only where the change class warrants it: low confidence in automation or monitoring, high criticality or regulation, or a change not reversible by redeploy (the risky class of data change, DATA_CHANGE.3). Access control on who may release applies in either case. Outcome: speed where automation can be trusted and a person where being wrong is irreversible.
2. **Grounds.** One pipeline of staged confidence (L1199, consensus; REG-107, REG-1110; same as the staging half of L156); hands-off with review the last manual gate wins with mature automation and monitoring (L156; REG-115); human gates win at high criticality, regulation, low confidence (L156; REG-107; REG-082 for access control).
3. **Positions.** P1 one staged pipeline. P2 hands-off (speed, reduced error). P3 human gates on some stages (control).
4. **Rejected.** A manual gate on every stage: it makes the gate a ritual and removes the speed argument; best under regulation that requires it. Fully hands-off for irreversible classes: best never where a mistake cannot be rolled back.
5. **Context.** Criticality and regulation, and test maturity (L156): P3 at high criticality, regulation or low confidence; P2 with mature automation and monitoring.
6. **Certainty.** Grounded for P1; grounded for the conditions of P2 and P3 (single contested row, T1 and T3 sources); inferred for placing the irreversible data class under P3.
7. **Flags.** none.

Constraints: MUST every gate state its criterion; MUST NOT a gate be skippable by a person with a different route to production (RULES.3). Links: Related DATA_CHANGE.3 (the maintainer's manual lane sits inside the contested range of L156), DEPLOY.1.

### CHANGE_FLOW.RELEASE.5 Who May Release and When

Intent: who is permitted to perform release operations and when deployment is blocked.

1. **Decision.** Restrict by policy who can perform release operations while keeping release itself self-service for the teams that own the system. Deployment proceeds only when someone able to respond is available; during an active incident only a change that remediates it is deployed, through a stated exception path. Outcome: no release is made by someone unauthorized or blind.
2. **Grounds.** Restrict operations, keep self-service (L157, consensus, one source; REG-082); block during incidents and outside responder hours (L164; REG-115, one T3 source, not cross-checked).
3. **Positions.** P1 restrict by policy, self-service. P2 block during incidents and off-hours.
4. **Rejected.** A fixed off-hours blackout where automated rollback and round-the-clock response exist: best only where nobody can respond. A deployment freeze that also blocks the remediation of the incident itself: best never.
5. **Context.** none.
6. **Certainty.** Grounded for P1 (one source); inferred: one T3 source (REG-115), plus the argument that a change needs someone able to respond to its failure. The MUST on the incident exception path stays: without it the block would stop the remediation itself.
7. **Flags.** none.

Constraints: MUST the set of release-permitted people be a recorded policy; MUST an incident exception path exist. Links: Related OPERATION.INCIDENTS.

---

## CHANGE_FLOW.DEPLOY Deployment

Intent: how a release reaches production: automation, rollout strategy, environment parity, instance replacement.

1. **Decision.** Deployment is automated by the same process in every environment, exposes a release progressively by blast radius with a canary judged against a concurrent control, keeps environments alike in kind and documents the differences that cannot be removed, and replaces instances rather than modifying them. Outcome: a deployment is repeatable, bounded in blast radius and observable.
2. **Grounds.** Roll-up of DEPLOY.1 to .4 (10 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** On the children (traffic, state, regions, scale).
6. **Certainty.** Inferred as a roll-up; children grounded or inferred as stated.
7. **Flags.** none.

Links: Realizes ASSURANCE.AVAILABILITY.

### CHANGE_FLOW.DEPLOY.1 Automated Deployment Path

Intent: how deployment is automated and which processes run as the application does.

1. **Decision.** Automate deployment with the same process for every environment, production included: any authorized person can deploy any version on demand, steps are idempotent and order-independent, scripts are versioned. One-off administrative processes (migrations included) run with the same code, environment and dependency isolation as the application, and their code ships with it. "The same process" means the same scripts and the same tooling; a human authorization or a human trigger on a stage for a risky class of change (RELEASE.4, DATA_CHANGE.3) is a gate within that process, not a different process. Outcome: what is deployed to production was exercised by the process that deployed it earlier, and no step depends on one person's memory.
2. **Grounds.** Same process, on demand, idempotent, versioned (L159, consensus; REG-077, REG-082, REG-092); admin processes as the application (L1198; REG-1109). The coverage check's contradiction by L290 and L328 dissolves once "automatic" and "same process" are separated: the maintainer's lane is a human-triggered run of the same tooling for a risky class (DATA_CHANGE.3), which L159 permits ("any authorized person can deploy on demand").
3. **Positions.** P1 same automated process in every environment. P2 admin processes isolated like the application.
4. **Rejected.** A different or hand-driven process for production: best never; it makes production the one environment never exercised. A fully hand-typed production step: banned by L286 and L159 alike.
5. **Context.** none.
6. **Certainty.** Grounded (consensus); inferred that the maintainer's manual lane is compatible with it (reasoned, see DATA_CHANGE.3).
7. **Flags.** none.

Constraints: MUST production be deployed by the same scripted process as every other environment; MUST deployment scripts be versioned; MUST admin code ship with the application. Links: Related RELEASE.4, DATA_CHANGE.1 (L1196), DATA_CHANGE.3 (resolved there); no remaining conflict.

### CHANGE_FLOW.DEPLOY.2 Rollout Strategy and Canary Evaluation

Intent: how a release is exposed to production traffic by blast radius and cost, and how a canary is judged.

1. **Decision.** Expose each release progressively, sized by blast radius and the cost of the strategy, and judge a canary against a concurrent control group on a few metrics tied to user impact, not by a before-and-after comparison; one canary at a time, population and duration sized to traffic and velocity, with automatic detection and rollback. Outcome: a regression is caught on a small share of users, and the call to proceed is based on evidence.
2. **Grounds.** Blue-green for stateful, downtime-sensitive applications with budget for two environments (L160; REG-087); canary for high traffic with good metrics (REG-088); one-box then waves with bake time for multi-region (REG-115, REG-084); concurrent control and few user-impact metrics (L161, one source; REG-104); identical-traffic comparison to catch regressions (L118, majority; REG-051, REG-067); most outages come from changes to a live system, so progressive rollout, fast detection and safe rollback (L173; REG-113).
3. **Positions.** P1 blue-green. P2 canary. P3 one-box then waves. P4 canary against a concurrent control. P5 old versus new on identical traffic. P6 progressive rollout plus fast detection plus playbooks.
4. **Rejected.** No strategy is rejected: each is best under its row's condition (above). Exposing a release to all traffic at once: best only with no live traffic to protect or where the change cannot be split. A canary judged by before-and-after metrics: best never, drift in traffic mix is read as a regression or hides one. The "threefold faster repair with playbooks" is one operator's figure, kept as an example, not a standard.
5. **Context.** Statefulness and downtime tolerance, traffic volume and metric quality, number of regions (L160).
6. **Certainty.** Grounded for the strategies and for the control-group rule (one source, REG-104, inferred as general); grounded for P6 as principle (one T2 source).
7. **Flags.** none.

Constraints: MUST a rollout have an automatic halt or rollback criterion; MUST a canary compare with a concurrent control. Links: Realizes ASSURANCE.AVAILABILITY; Related ROLLBACK.1, OPERATION.RUNBOOKS (playbook clause of L173), ASSURANCE.AVAILABILITY.3.

### CHANGE_FLOW.DEPLOY.3 Environment Parity

Intent: how alike production and earlier environments are kept, and how much pre-production is maintained against relying on progressive rollout.

1. **Decision.** Keep every environment alike production in kind: same type and version of backing services, operating system and libraries, a short time from commit to deploy, authors taking part in deploying; do not rely on adapters or lightweight stand-ins to hide differences. Parity does not extend to production credentials or access. Where parity of scale, data volume, permissions or external or shared schemas present only in production cannot be afforded, record the known differences as a list, and route every change whose behaviour depends on them (time, locks, plan, permission) to a rehearsal on production-shaped data (DATA_CHANGE.7) and to the gated lane (DATA_CHANGE.3). Outcome: a pass in an earlier environment means what it says, and each place where it cannot is known and covered.
2. **Grounds.** Tests pass on a lighter database and still fail in production (L165, L1194; REG-077, REG-092, REG-103, REG-1109); the same row says "as alike as practical", which admits residual divergence. The maintainer's rule (L328, REG-181) documents and routes the divergence that cannot be removed; it contradicts parity only where it is read as abandoning parity of kind. The two apply to different axes (kind and version against scale and data), which is why they are kept together.
3. **Positions.** P1 production parity in all environments (confidence, correctness). P2 reduce pre-production, test in production with canary and safe rollback (cost, real traffic). P3 lightweight stand-ins in development (speed, cost). P4 maintainer: accept divergence, document it, route to manual environment-specific migration.
4. **Rejected.** P3: the source argues against it and no row supports its merit; best when the adapter surface is narrow and production-like tests exist elsewhere in the pipeline. P2 as the answer for stateful data change: a canary does not make a schema change safe; best with high traffic, strong monitoring and fast rollback for stateless change. P4 stated as "rather than pursuing identical environments" across the board: best only for the axes it names (data volume, permissions, missing schemas, performance) when production-sized data is unaffordable to replicate.
5. **Context.** Affordability of production-sized data (L328); traffic, monitoring and rollback maturity for P2 (L165).
6. **Certainty.** Grounded for P1 (Twelve-Factor and DORA); inferred for the split by axis (reasoned from the rows, not stated by a source); P4 is maintainer practice, single source.
7. **Flags.** none.

Constraints: MUST backing-service type and version match production in every environment; MUST the list of known environment differences be written down and referenced by the changes it affects; MUST NOT parity extend to production credentials. Links: Related TRANSVERSE.ENVIRONMENTS, DATA_CHANGE.3 and .7.

### CHANGE_FLOW.DEPLOY.4 Instance Replacement and Desired State

Intent: whether running instances are replaced or modified, and whether deploys are pushed or reconciled from declared state.

1. **Decision.** Replace deployed instances rather than modify them, and keep the declared state of images and infrastructure as versioned code, so the running system equals what is declared and drift cannot persist. Two forms serve this: agents that pull and continuously reconcile declared state, or a scripted push deploy from CI with drift detection; no source compares them, so no switch between them is decided. Outcome: what runs matches what was declared, and a bad instance is replaced, not repaired.
2. **Grounds.** Replace, do not modify; immutable images (L166, majority; REG-081, REG-095, REG-111); pull-based reconcile corrects drift and leaves an auditable history (L167; REG-101); scripted push is the cheap form (REG-077, REG-092). No source compares pull and push.
3. **Positions.** P1 replace instances (consistency, reversibility). P2 managed mutable servers (stateful hosts, drift risk). P3 declarative desired state with pull reconcile (control, security). P4 push from CI (cost of ownership).
4. **Rejected.** P2: best for stateful hosts where replacement is costly (inferred), with drift detection. P4 without drift detection: it cannot correct drift; no source says when push or pull is best (open).
5. **Context.** none; pull versus push is open.
6. **Certainty.** Grounded for P1 (majority); open for pull versus push (no source compares).
7. **Flags.** none.

Constraints: MUST declared state be in version control; MUST NOT an instance be modified in place without the change recorded back into the declared state. Links: Stack pointers L166 (image-based provisioning), L167 (orchestrators).

---

## CHANGE_FLOW.ROLLBACK Rollback

Intent: how a change is undone: the decision to roll back, backward compatibility, reversibility through version control, and undoing a data change.

1. **Decision.** The way back is decided before the change ships: roll back from alarms where a change is reversible by redeploy, fix forward where it is not, every change is made backward compatible with the previous version and reversible through version control, and a data change names its undo. Outcome: going back is a rehearsed move, not an improvisation.
2. **Grounds.** Roll-up of ROLLBACK.1 to .3 (6 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** On the children (reversibility; distribution).
6. **Certainty.** Inferred as a roll-up.
7. **Flags.** none.

Links: Realizes ASSURANCE.AVAILABILITY; ROLLBACK.3 realizes ASSURANCE.DATA_INTEGRITY.

### CHANGE_FLOW.ROLLBACK.1 Detecting and Deciding to Roll Back

Intent: whether a bad release is rolled back automatically from alarms or fixed forward, decided in advance.

1. **Decision.** Detect bad releases automatically and decide in advance, per change class, between the two: a change that is backward compatible and reversible by redeploy is rolled back automatically from alarms; a change that is not reversible by redeploy (a data migration past its last reversible point) is fixed forward, with the undo decided at ROLLBACK.3. Outcome: recovery time is short and the choice is not made under stress.
2. **Grounds.** Automated rollback on alarm (L162; REG-104, REG-113, REG-115); fix forward under continuous deployment with a very fast pipeline (REG-078, REG-106). No source states the decision rule; the rule by reversibility is inferred from both wins-when conditions, which fit together.
3. **Positions.** P1 automatic rollback from alarms (reversibility, recovery time). P2 fix forward (simplicity).
4. **Rejected.** P2 for a reversible change when a rollback is available and faster: best with a very fast pipeline, and for changes not reversible by redeploy. P1 for a change whose redeploy cannot restore the data: best never; rolling back code against changed data can corrupt.
5. **Context.** Reversibility by redeploy (backward compatible or not).
6. **Certainty.** Grounded for both positions; inferred for the decision rule (no source states it).
7. **Flags.** none.

Constraints: MUST the rollback-or-fix-forward choice be decided per change class before shipping. Links: Related DEPLOY.2; conflicts with none: the recorded partial tension with L288 is resolved at ROLLBACK.3.

### CHANGE_FLOW.ROLLBACK.2 Reversible by Design

Intent: how a change is made so that going back is safe.

1. **Decision.** Make each change backward compatible with the previous version (parallel change: expand, migrate, contract; schema changes separate from application releases) so rollback, mixed fleets and independent release are safe. Every automated change is reversible through version control; tool-level checkpoints are not a substitute. Outcome: any release can be undone without data or compatibility breakage.
2. **Grounds.** Backward compatibility (L163, consensus; REG-087, REG-088, REG-105, REG-115; the maintainer's L288 agrees); reversibility through version control (L1072, majority; REG-1038, REG-1041).
3. **Positions.** P1 backward compatible parallel change. P2 every automated change reversible through version control.
4. **Rejected.** No competing position recorded. A tool checkpoint as the only way back: best never; it is not reviewed or versioned.
5. **Context.** none.
6. **Certainty.** Grounded.
7. **Flags.** none.

Constraints: MUST a change be compatible with the version it replaces during the deploy window. Links: Related DATA_CHANGE.4 (the procedure for data is held there, this is the generic rule), INTEGRATION.5.

### CHANGE_FLOW.ROLLBACK.3 Undoing a Data Change

Intent: what undoes a failed data change, decided before it ships.

1. **Decision.** Before a data or schema change ships, its undo is decided and recorded in the change: a backward-compatible expand step is undone by rolling the application back and leaving the structure; a change whose reversal by script is faster than a restore (a data correction on few rows with its prior values saved, a metadata-only change) carries a written reverse prepared ahead and rehearsed with the forward script (DATA_CHANGE.7); a reverse that was not rehearsed does not count as the undo; otherwise the recorded undo is a roll-forward fix or the tested restore; a change that destroys or can lose data is undone by the tested restore of ASSURANCE.DATA_INTEGRITY.3. The last reversible point is named: the state before the old structure is removed and before reads move irreversibly; after new-only data accumulates, going back loses it. Outcome: no data change ships without a known, tested way back or an honest statement that there is none.
2. **Grounds.** Reverse for every migration versus compatibility plus roll-forward plus restore (L387; REG-244, REG-251, REG-252, REG-255); the maintainer's forward-only with a prepared undo (L288, L387 c; REG-181); last reversible point (L390; REG-087, REG-260). The strongest argument is that an automatic undo is untested code that cannot restore lost data and hides data loss, while a prepared, documented undo and a tested restore are exercised and honest; DATA_INTEGRITY.3 (settled) already treats a destructive change as undone by restore only.
3. **Positions.** P1 written reverse for every migration (reversibility, downgrade after a vulnerability). P2 compatibility plus roll-forward plus restore (cost of ownership, honesty). P3 maintainer: forward-only with documented undo prepared ahead. P4 last reversible point.
4. **Rejected.** P1 as the default: best for regulated or packaged software with many installed versions, where a customer must downgrade (DISTRIBUTION). Automatic down migrations as the common alternative: best for pure schema changes with no data to lose, where one command reverses; best never for a change that loses data. A written reverse for every change: reverse migrations are not worth writing all the time (REG-244) and work poorly for data changes (REG-251); best for packaged software with many installed versions (DISTRIBUTION).
5. **Context.** Distribution (L387): packaged software with many installed versions needs a written reverse for every migration; a continuously deployed service with one production uses the decision as stated.
6. **Certainty.** Grounded for P2 and P4 (majority, several sources); inferred for P3 as the general form (maintainer practice, single source); the choice among undo forms is inferred, and so is the faster-than-restore condition.
7. **Flags.** none.

Constraints: MUST every data change record its undo before it ships; MUST the last reversible point be named; MUST a destructive change rely on a tested restore. Links: Realizes ASSURANCE.DATA_INTEGRITY; Conflicts none (L288 versus L162 resolved at ROLLBACK.1); Related DATA_CHANGE.4.

---

## CHANGE_FLOW.DATA_CHANGE Data and Schema Change

Intent: how schema, data and bulk changes are written, ordered, rehearsed, run and watched; this branch holds the procedures, the guarantees stay in ASSURANCE.DATA_INTEGRITY (MD-03).

1. **Decision.** Every schema and data change is a reviewed, versioned, once-only script tracked in the target's history and never applied by hand-typed SQL, delivered through one pipeline with a risk-based human trigger for the risky class, ordered before and compatibly with the code, made without blocking locks, bulk work done in re-runnable bounded batches, rehearsed on production-shaped data against a time budget, and run and watched against stated signals until a convergence query says it is done. Outcome: a data change that ships was reviewed, rehearsed and watched, and what runs in production is what was reviewed.
2. **Grounds.** Roll-up of DATA_CHANGE.1 to .8 (48 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** Scale and downtime tolerance (.3), data volume (.6, .7), table size and write rate (.5).
6. **Certainty.** Inferred as a roll-up; many children rest on maintainer practice (single source) with public practice read as agreeing.
7. **Flags.** none.

Links: Realizes ASSURANCE.DATA_INTEGRITY (the guarantees: .1 where rules live, .2 guarding bulk and destructive, .3 layered protection, .4 sync, .5 old against new).

### CHANGE_FLOW.DATA_CHANGE.1 Form and Source of a Change

Intent: in what form a schema or data change is written and what its source of truth is, so no change is applied by hand.

1. **Decision.** Every schema and data change is a migration script in version control, ordered by a unique sequence, applied once and recorded, run by automation (or the human-triggered run of DATA_CHANGE.3) and never by hand-typed ad-hoc SQL; migrations are kept with the application, run by the same process in every environment as an explicit step of the release, and each names its ticket. Each change is as small as possible so errors are quick to spot. The deployed artifact is the reviewed versioned script: where a declarative desired-state source is used for the developer loop, the generated script is what is reviewed and deployed. DDL is written so a re-run is safe wherever a step can be partially applied or the target's state may differ (steps outside a transaction, environments with known differences), except one-time data migrations and operations that must fail when their precondition does not hold. Where urgent data fixes are frequent and must not wait for the release train, keep them in their own stream, recorded in the same audit. Outcome: no change enters a database that was not reviewed, ordered and recorded.
2. **Grounds.** Migration script in version control, sequence, automation (L379, consensus; REG-244, REG-245, REG-253); the maintainer's reason, earlier inconsistent environments and untracked manual changes (L286; REG-181); same process in every environment as a release step (L1196; REG-244, REG-1109, REG-1110); small changes (L1197, L385; consensus; REG-244, REG-257); ordered scripts give auditability, determinism, offline CI and the exact SQL that runs (L381 b; REG-253), declarative gives a faster developer loop (L381 a; the vendor recommends a hybrid with generated versioned files, one source); idempotent DDL as defence in depth against partial application (L289, maintainer; once-only tooling already serves the transactional case; REG-181); separate stream for urgent data fixes (L406, one T2 source; REG-244). ASSURANCE.ARTIFACT.1 (settled) requires what runs to match reviewed source, which is why the generated script, not the declared state, is the deployed unit.
3. **Positions.** P1 migration in version control, ordered, automated. P2 maintainer: ordered, once-only, history-table tracked, never manual. P3 versioned scripts with the application, same process everywhere. P4 declarative desired state as source (cognitive load, iteration speed). P5 ordered change scripts as source (auditability, determinism). P6 idempotent DDL. P7 smallest possible change. P8 separate stream for urgent data fixes.
4. **Rejected.** P4 as the deployed unit: a plan computed at deploy time was not what was reviewed; best for fast local loops when CI can reach the database, and as the authoring form when the generated script is reviewed. P6 stated as a rule for every statement: for transactional all-or-nothing steps the once-only tool already serves and the cost is verbosity; best for steps that can be partially applied and for scripts run against environments known to differ. P8 as a default: a second stream is a second delivery truth to keep consistent; best when urgent fixes are frequent and must not wait for the release train.
5. **Context.** Compliance and distribution (L381): compliance, many instances or packaged software require the ordered scripts as source; a fast local loop may author declaratively.
6. **Certainty.** Grounded for P1 to P3 and P7 (consensus); inferred for P6 and P8 (maintainer and one T2 source, conditions reasoned); P4 versus P5: grounded as positions, the hybrid is one vendor's recommendation.
7. **Flags.** none.

Constraints: MUST every database change be a script in version control applied by tooling; MUST NOT a change be hand-typed; MUST each migration name its ticket; MUST the reviewed script be the deployed script. Links: Related DEPLOY.1, DATA_CHANGE.2; ASSURANCE.ARTIFACT.1 (deployed objects compared with source); stack pointers L289 (SQL form), L1196 (relational origin, statement generic).

### CHANGE_FLOW.DATA_CHANGE.2 Migration History and Immutability

Intent: how the state of applied migrations is recorded and why an applied migration is not rewritten.

1. **Decision.** Keep a per-database record, in the target database itself, of which migrations ran, and never edit an applied migration: if it failed, fix it and rerun; if it succeeded but was wrong, add a new one; a recorded checksum enforces this, and forced replay is rare and administrator-only. Sample and reference data are kept with the migrations so every environment is consistent. Outcome: any environment's state is knowable and reproducible, and history is not rewritten.
2. **Grounds.** Per-database record, correct with a new migration (L380; REG-245, REG-252, REG-253; the strict "never edit" form is inferred from REG-252 and REG-253); the maintainer's form with checksum (L287; REG-181); state in the target and reference data with migrations (L418, consensus; REG-244, REG-245). The strict form wins wherever more than one environment has applied the change, since an edit there makes the environments differ silently.
3. **Positions.** P1 record and no edit of applied. P2 maintainer: checksum-enforced immutability. P3 state in the target, reference data with migrations.
4. **Rejected.** Editing an applied migration after rolling it back (one tool allows it): best when only one environment has applied it. Unrecorded history: best never.
5. **Context.** none beyond "more than one environment".
6. **Certainty.** Grounded for the record and the new-migration rule (majority); inferred for the checksum as general mechanism (maintainer; the strict form is inferred).
7. **Flags.** none.

Constraints: MUST an applied migration not change; MUST the history live in the target database. Links: Stack pointer L287 (one migration tool's model); Related DATA_CHANGE.1.

### CHANGE_FLOW.DATA_CHANGE.3 Delivery Path and Gating of Database Change

Intent: through which path and gate a database change reaches production, and which changes go through a person.

1. **Decision.** Database change is a primary delivery risk and travels in the same pipeline as application change, as the same reviewed script with one history and one audit trail; it is not a separate manual track. The pipeline classifies each change by a recorded criterion (runs longer than the team's time budget, takes locks, is environment-specific, cannot run in a transaction, needs monitoring, is irreversible, touches a table above a size the team records, or has not had its duration measured on production-shaped data (DATA_CHANGE.7)). Ordinary changes apply automatically through every environment, production included. Changes in the risky class pass an authorization stage of the same pipeline: a named, qualified group approves the production run on the exact script and a member of it triggers the stage, which runs the script with the same tooling, credential scope and audit trail as every other change (never hand-typed SQL; principle at ASSURANCE.SECURITY.6). A run started outside the pipeline is allowed only where the pipeline cannot reach the target or the job needs supervised ramping (DATA_CHANGE.8), and is then recorded in the same history. The people who manage the production database are involved beforehand and pending changes are visible across teams and environments. Configuration-like registry content travels through the same one history; an idempotent authoring script may be its source where the run is recorded in that history. Outcome: what runs in production is what was reviewed and rehearsed, and a risky change is never started by an automatic merge.
2. **Grounds.** Database change as primary delivery risk in the same pipeline (L168; REG-087, REG-097, REG-105, REG-244, REG-245); automation of everything is safer when changes are small, fast, compatible, reversible and rolled out in stages (L290 a, L410; REG-244, REG-245, REG-255; DORA); a human gate serves reversibility and control for long, locking, irreversible changes (L290 b, L410; maintainer, REG-181), its volume condition carried per change by the criterion (a table above the recorded size, an unmeasured duration) instead of a blanket rule with no threshold; the authorization stage is a stage of the one pipeline that requires human authorization (REG-107, Fowler's deployment pipeline, fetched in review) and database change goes through automated, version-controlled scripts (REG-245, DORA, fetched in review); GitLab supports separating risky changes from the release train and a release manager's discretion over timing (REG-255), not a named-group trigger, which rests on the maintainer and the SECURITY.6 argument; the public "never manual" rule bans hand-typed SQL, not a human-triggered run of an automated script (L410); involving production-database owners and making pending changes visible (L408, consensus; REG-245); configuration-like content (L294, maintainer; L411 records no public counterpart, open). The deciding argument is that the guarantee needed is "what runs is what was reviewed" (ARTIFACT) and "a risky change does not start unwatched" (SECURITY.6 requires such a job to run under guards or from a reviewed script by a person); a risk-based gate delivers both while keeping automatic delivery for the changes it is safe for, whereas manual production for all changes adds delay and a path nobody exercises in routine, which is the failure L159 and the maintainer's own L286 give for manual change. Contradiction with L168, L159 and L156 (coverage check) is resolved: the manual lane is a gate inside the pipeline for a class (RELEASE.4), not a second track.
3. **Positions.** P1 same pipeline, database change as primary risk (majority/consensus). P2 fully automated, every change through the pipeline (speed, consistency). P3 maintainer: split by risk, production applied manually by a small group (reversibility, control). P4 maintainer path: feature branch with ticket key, migration, manual test on development, pull request approved, automatic apply on development, verification on staging, release pull request approved but not merged, manual production run, then application deploy. P5 configuration-like content through the same pipeline. P6 maintainer: such content has an idempotent authoring script as source of truth, deployed by running it. P7 maintainer: document environment differences and route to a manual or conditional migration. P8 involve production-database owners, make pending changes visible.
4. **Rejected.** P2 for the risky class: best with small, fast, compatible, reversible changes, staged rollouts and high deploy frequency; it is the default for the ordinary class. P3 as stated, production manual for every change: best where most tables exceed the recorded size, which the criterion already routes to the risky class change by change, so no separate rule is kept. P4's unmerged release approval: not a principle; it is a mechanism that keeps the mainline equal to what is applied in production, best when merging to the mainline triggers production deployment (inferred). P6 as a separate delivery truth: two paths mean two histories; best when the content is data-like, small and often re-authored, provided the run is recorded in the same history (inferred; L411 records no public counterpart, open). P7 is decided at DEPLOY.3.
5. **Context.** Data volume moves the classification: in a store where most tables exceed the recorded size, most changes fall in the risky class through the criterion, with no separate rule (L290 b, L410); criticality and table size move the gate.
6. **Certainty.** The authorization stage inside the one pipeline is grounded (REG-107, REG-245); the named, qualified group that approves and triggers it has no public source and is inferred. Grounded for P1, P8 and the ban on hand-typed SQL (consensus, T1 and T2 sources); grounded as maintainer practice (single source) for P3 and P4; inferred for the risk-based split as the general rule, for the size criterion, and for P6 (no public counterpart).
7. **Flags.** none.

Constraints: MUST the same reviewed script, not a retyped one, run in production; MUST the classification criterion be recorded; MUST NOT a risky-class change start from an automatic merge; MUST a production run of the risky class name who runs it and be approved on the exact script. Links: Realizes ASSURANCE.DATA_INTEGRITY; Related RELEASE.4, REVIEW.1 (L298), DEPLOY.1 and DEPLOY.3 (conflicts resolved), ASSURANCE.SECURITY.6.

### CHANGE_FLOW.DATA_CHANGE.4 Order and Compatibility With Running Code

Intent: the order in which schema and application change, and how a structure changes while old and new code run against the same data.

1. **Decision.** Deploy a schema change separately from, and before, the application version that needs it; the first schema step supports both old and new versions. A backward-incompatible change (rename, type change, split, move) is made as expand, migrate, contract: add the new structure beside the old, move writers and readers, backfill, then remove the old; the contract step is scheduled and owned (an unfinished contract leaves a state worse than the start). Old and new application versions run against the same data over the deploy window, so every stored-data change is readable and writable by both. Before dropping a column or table, stop the application reading it (and any framework cache of it) and drop in a later deploy. An application deploy is gated on the schema state it needs: a declared minimum schema version is checked before rollout and the deploy fails if the target history lacks it. When a shared structure must change, old and new access patterns are supported during the transition behind a stable compatibility surface, with database access behind a clear layer in code. Outcome: schema and code can change in either order of rollout without a window of failure, and the contract step is not forgotten.
2. **Grounds.** Schema first, supports both (L382; REG-087, REG-244, REG-245); expand, migrate, contract (L383; REG-105, REG-245, REG-257, REG-260); schedule and own the contract (L384; REG-105, REG-260); old and new on the same data (L386; REG-087, REG-105); stop reading before dropping (L419, tool-specific, generalisation inferred; REG-258); a minimum-schema-version gate (L292, maintainer; REG-087, REG-181; public sources support the order, not an explicit gate): it turns an ordering convention into a blocking check, the principle of RULES.3; compatibility layer (L409; REG-105, REG-244).
3. **Positions.** P1 schema first, separate. P2 expand, migrate, contract. P3 own the contract. P4 old and new on the same data. P5 maintainer: minimum-schema-version gate. P6 stop reading before dropping. P7 compatibility layer: views or triggers (Fowler and Sadalage), a function with a signature (maintainer), versioned interfaces for remote APIs (REG-105).
4. **Rejected.** Code and schema deployed together in one step for an incompatible change: best never in a deployment with rolling or rollback. P5 stated as a replacement for ordering: the gate checks the order, it does not substitute for it. P7 forms: views win when consumers read shape (declarative, plannable, read-only reporting with several consumers); a function interface wins when consumers are many and diverse (absorbs change; no public source, maintainer practice, L309); versioned interfaces apply to remote APIs, not to a database structure.
5. **Context.** Consumers of the shared structure (L409): their number and diversity pick the compatibility surface.
6. **Certainty.** Grounded for P1 to P4 (consensus); grounded for P6 as a tool fact, inferred as general; inferred for P5 as the general form (single maintainer source) and for the choice among P7 forms.
7. **Flags.** none.

Constraints: MUST schema change deploy before the code that needs it; MUST the contract step have an owner and a date; MUST an application deploy fail if the schema history lacks the minimum version it declares. Links: Realizes ASSURANCE.DATA_INTEGRITY; Related ROLLBACK.2 (generic rule L163), ASSURANCE.CONTRACTS, CONSTRUCTION.HIDING (second clause of L409); stack pointer L419 (one web framework).

### CHANGE_FLOW.DATA_CHANGE.5 Locks and Online Schema Change

Intent: how a schema change is made without blocking the shared database.

1. **Decision.** Know the lock a statement takes before running it on a shared database. Run migrations with a per-session lock timeout (not set globally) and retry on timeout so a blocked statement does not queue and starve the table; prefer the non-blocking form of each change (add a constraint unvalidated then validate separately, build indexes concurrently, add columns without volatile defaults, request metadata-only or in-place algorithms with an explicit no-lock clause); run operations that cannot execute in a transaction in their own non-transactional step; for large tables where in-place change blocks, use an online schema change tool that copies and swaps, chosen by write rate (log-based and pausable on high-write masters, trigger-based when simpler and writes are light, native when the operation is metadata-only). Do not shard schema changes: use the platform's concurrent variant in a manual migration and shard only data changes. Outcome: a schema change never holds a lock that blocks the database longer than a stated bound.
2. **Grounds.** Know the lock (L392, consensus; REG-246, REG-247, REG-249); lock timeout and retry (L393, majority; REG-246, REG-248, REG-255); non-blocking forms (L394, consensus; REG-247, REG-249, REG-258, REG-259); separate non-transactional step (L395, consensus; REG-255, REG-258); online schema change tools (L397, majority; REG-245, REG-246, REG-249, REG-256); do not shard schema changes (L304; maintainer, consensus per row; REG-181).
3. **Positions.** P1 know the lock. P2 session lock timeout and retry. P3 non-blocking forms. P4 non-transactional step apart. P5 online schema change tool: trigger-based, log-based, native. P6 do not shard schema changes.
4. **Rejected.** A global lock timeout: affects unrelated sessions; best never for migrations. A trigger-based tool on a high-write master: adds write overhead and cannot pause; best when writes are light and simplicity wins. In-place change on a large table where it blocks: best never.
5. **Context.** Table size and write rate, and whether the operation is metadata-only (L397).
6. **Certainty.** Grounded for P1, P3, P4 (consensus); grounded for P2 and P5 (majority; the starvation reason is inferred); P6 maintainer practice read as consensus.
7. **Flags.** none.

Constraints: MUST the lock taken by a statement be known before a run on a shared database; MUST a migration set a session-level lock timeout; MUST a statement that cannot run in a transaction run in its own step. Links: Related DATA_CHANGE.6 (sharding applies to data changes only); stack pointers L392 to L397, L304 (Postgres, MySQL names).

### CHANGE_FLOW.DATA_CHANGE.6 Bulk and Backfill Design

Intent: how a change over very large data is cut into batches that can be re-run, and where it runs.

1. **Decision.** If one statement finishes in minutes, run it as a migration. A change over data too large for that (order of ten million rows and more) is run as four decisions in order: the batching key (an indexed key part, then a numeric range, modulo last), a work list generated from the data, fan-out by workers, observe and recover. Batches are bounded, throttled, in their own step and never inside a long DDL transaction; every batch is re-runnable in isolation with the same result (a self-limiting predicate in preference to external bookkeeping, absolute not relative updates, upsert not insert, partition by a fixed key, never read "latest" data inside the job, one logical unit in one statement, no automatic retries of non-idempotent batches). Data steps stay apart from schema steps in transaction and timing. Where the backfill runs is decided and recorded: inside a migration step with a time budget for minutes of work, as an application background job triggered by a migration for long work, offline from a snapshot for very large multi-table moves with analytic tooling. Standard command-line tools composed and verified part by part suit a one-off job; a framework suits a job that recurs. Outcome: a large data change can be interrupted, repeated and verified without corruption.
2. **Grounds.** Four-decision procedure and size gate (L299, maintainer; REG-181); bounded throttled batches in their own step (L398, consensus; REG-255, REG-257, REG-258); re-runnable batches (L300, maintainer; L399, majority, transfer from scheduled tasks inferred; REG-254, REG-181); place by duration (L401, contested; each held by a different T3 source; REG-255, REG-257, REG-258); standard tools (L307, maintainer; REG-181); data apart from schema (L407, majority; REG-255, REG-258). One long transaction serves simplicity and costs locks, bloat and an open transaction of hours; the size gate decides.
3. **Positions.** P1 four-decision procedure with size gate. P2 bounded throttled batches. P3 batches re-runnable, self-limiting predicate. P4 re-runnable with upsert, fixed partition, no "latest". P5 place by duration: in-migration, background job, offline snapshot. P6 compose standard tools, not a framework. P7 data apart from schema.
4. **Rejected.** One long transaction over very large data: best when it finishes in minutes. A framework for a one-off job: best when the job recurs (repeatability against cost of ownership). External bookkeeping instead of a self-limiting predicate: best when the data cannot carry its own progress. An offline backfill: best only for very large multi-table moves (zero production load against a copy that must be reconciled). Each place in P5 is best at its duration (no single winner).
5. **Context.** Data volume (L299) and duration of the work (L401).
6. **Certainty.** Grounded for P2 and P7 (consensus, majority); inferred for P1, P3 and P6 (maintainer practice, single source, public practice read as agreeing or extending); P5 contested, decided by duration (inferred).
7. **Flags.** none.

Constraints: MUST a bulk batch be re-runnable with the same result; MUST a batch not run inside a long DDL transaction; MUST the place a backfill runs be recorded with its reason. Links: Related DATA_CHANGE.5 (L304), DATA_CHANGE.8; ASSURANCE.DATA_INTEGRITY.2 (explicit scope for bulk operations); stack pointers L299 (named database client and parallel runner), L398, L399, L307.

### CHANGE_FLOW.DATA_CHANGE.7 Rehearsal and Time Budget

Intent: on what data and against what budget a data change is rehearsed before production.

1. **Decision.** Rehearse a data change before production on data whose size and shape make the measured time, lock behaviour and plan representative, and keep the measurements with the change; for small data, developer-owned databases with versioned sample data suffice. On every change request, restore a dump of development data and apply every migration of the request; a migration that cannot work on the partial dump carries a skip marker with its reason and is rehearsed on production-shaped data before its production run. Migrations have a time budget by class (the budget is the team's, the same value as the gate criterion of DATA_CHANGE.3) so long ones are identified before deploy. When production data is copied for a rehearsal, personal data is masked before the copy leaves production and side effects (mail, analytics) are blocked in the copy. Outcome: duration, locks and plan are known before production, and no skipped rehearsal is left unrehearsed.
2. **Grounds.** Production-sized or production-shaped data (L403 a; GitLab, Postgres.ai, Neon: vendor sources are interested parties; REG-244, REG-255, REG-261, REG-262) against developer-owned data with sample data for small data (L403 b; REG-244); the maintainer's restore of a dump on every request (L293; agrees with migration CI on a representative dataset; REG-181); measure and keep (L405, majority; REG-255, REG-256, REG-261); time budget (L402, majority, one T3 source; REG-255); mask and block side effects (L404, single vendor; REG-262). A skip marker that would leave a migration never rehearsed fails the guarantee of the rehearsal; the added condition closes it.
3. **Positions.** P1 production-sized or production-shaped data. P2 developer-owned databases with sample data. P3 rehearsal in a rolled-back transaction on shared real data (maintainer, no public source; pointer from L403, row routed elsewhere). P4 maintainer: restored dump of development data on every request, skip marker. P5 measure and keep. P6 time budget by class. P7 mask and block side effects.
4. **Rejected.** P1 for small data: costs cloning and personal-data risk for no gain; best for large tables and where plans or lock duration depend on volume. P2 for large tables: timings do not transfer. P3: decided against as the general rule at BEHAVIOUR.7 (disposable store by default; the rollback boundary only where data cannot be cloned and every effect can be undone). Figures in P6 (3, 10 minutes, one second): one team's; the maintainer's five minutes is a value of the same kind.
5. **Context.** Data volume (L403): P1 for large tables, P2 for small data.
6. **Certainty.** Grounded for P1, P2, P5 (several sources, vendor caveat); inferred for P4 as general (maintainer, agrees with common practice) and for the condition on skipped migrations; P6 numbers inferred; P3 undecided here, settled in J2.
7. **Flags.** none.

Constraints: MUST measure duration and lock behaviour on a rehearsal copy before production and keep the figures with the change; MUST a migration with a skip marker be rehearsed elsewhere; MUST personal data be masked in a copy of production. Links: Related TRANSVERSE.PRIVACY (L404), ASSURANCE.BEHAVIOUR.7 (test data management), DATA_CHANGE.3 (budget as gate criterion).

### CHANGE_FLOW.DATA_CHANGE.8 Running and Watching a Production Data Job

Intent: how a production data job is started, ramped, watched, stopped and declared done.

1. **Decision.** A bulk change is declared done by a written convergence query that returns zero remaining work, not by the job process returning; a non-zero result means skipped or silently failed batches, and re-runs must strictly decrease it. Who triggers a production run of the risky class is held at DATA_CHANGE.3, which points to ASSURANCE.SECURITY.6; this node holds how the job runs once started. A production bulk job does not start until a checklist holds: a ticket exists and long-running statements are identifiable to it; a full development run at one worker, then a few; the batch predicate is index-backed (verified by a plan); every batch idempotent or the predicate convergent; the convergence query written; the job detached with a ledger; senior review (a qualified approver, REVIEW.1) if it holds locks or runs long; a stop plan naming what to cancel and whether partial completion is acceptable. Concurrency is never guessed and is raised only with a reason and a metric; the recommended ramp is one batch by hand with its plan inspected, one worker, a modest default; on the first production run halt on the first failure, keep a ledger of batches with exit codes and separate error and progress streams, bound workers by connections, headroom and replica lag. The job is pausable and paced on the target system's health, replica lag first, with mid-run adjustment of batch size and lag limit; watch the target (lock waits, per-batch runtime climbing, dead-tuple growth, replica lag) and escalate on those signals. A long-running statement is identifiable to its change in activity views and logs during an incident (for example the ticket key in a comment). The procedure scales with blast radius; a job that finishes in minutes is a plain migration (DATA_CHANGE.6). Outcome: a production data job is started only when it can be stopped and finished only when proven complete.
2. **Grounds.** Convergence query (L301, maintainer, extends common practice; no public counterpart found, L413 open; nearest REG-257 shadow comparison, REG-254 idempotence; REG-181); ramp and halt rules (L302, maintainer; agrees with progressive rollout, extends it; REG-181); the checklist (L303; REG-181); pausable, paced on replica lag (L400, majority, single T3 source plus a sleep between batches in REG-258; REG-256, REG-258); watch the target (L305; agrees with common practice; REG-181); identifiability of statements to their change (L306, inferred: the outcome query tagging serves; no public counterpart found, L412 open; REG-181). The strongest argument for the convergence query is that a returning process proves only that the process finished.
3. **Positions.** P1 convergence query as done. P2 ramp, halt, ledger, detach. P3 pre-start checklist. P4 pausable, health-paced. P5 watch the target system. P6 ticket key in the statement.
4. **Rejected.** "Done" when the job returns: best never; it cannot see skipped batches. Guessing concurrency: best never. Watching only the job's shell: misses lock waits and lag. The full checklist for a job of minutes: best only at large blast radius; the size gate decides.
5. **Context.** none stated by a row beyond blast radius (the size gate of DATA_CHANGE.6).
6. **Certainty.** Grounded as maintainer practice (single source) for P1 to P3, P5, P6, inferred as best practice (public practice agrees or extends; no counterpart found for P1, P2, P6); grounded as majority for P4 (one T3 source).
7. **Flags.** none.

Constraints: MUST a convergence query be written before the job starts; MUST the first production run halt on the first failure; MUST a bulk job keep a ledger; MUST a long-running statement be identifiable to its change in activity views and logs (for example the ticket key in a comment). Links: Related OPERATION.TELEMETRY (L305), OPERATION.INCIDENTS (L306), REVIEW.1 (L303), DATA_CHANGE.3 (authorization stage, run outside the pipeline), DATA_CHANGE.6, ASSURANCE.SECURITY.6 (a large-blast-radius job is a reviewed script, its run authorized and triggered by the accountable group through the guarded path); stack pointers L305 (dead tuples), L400 (a MySQL tool).

---

## CHANGE_FLOW.MEASURE Measuring Delivery

Intent: how delivery is measured and which outcomes judge it.

1. **Decision.** Delivery is judged by outcomes (lead time, deployment frequency, recovery time, change fail rate, rework), used to guide improvement not to rank people, never by volume of code produced; a measured gain from automation is verified against an independent baseline, and the fundamentals of the delivery system are treated as preconditions. Outcome: delivery performance is measured by what reaches users and holds, not by output.
2. **Grounds.** Roll-up of MEASURE.1 and .2 (5 rows).
3. **Positions.** None here (roll-up).
4. **Rejected.** Not applicable.
5. **Context.** Foundation practices (on MEASURE.1).
6. **Certainty.** Inferred as a roll-up.
7. **Flags.** none.

Links: Realizes ASSURANCE.RULES; Related OPERATION.FEEDBACK.

### CHANGE_FLOW.MEASURE.1 Outcomes That Judge Delivery

Intent: which outcome measures judge the change flow, and how speed and stability relate.

1. **Decision.** Measure with the five DORA metrics (change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate) and use them to guide improvement, not to rank people. Treat speed and stability as correlated, not traded off, but only with supporting practices: raising frequency alone yields failures and burnout. Judge the change flow by delivery outcomes, not by the volume of code or pull requests produced; the net effect of automation on those outcomes depends on the foundation practices and is not settled by the sources. Outcome: a team improves what reaches users, and no measure becomes a target that distorts it.
2. **Grounds.** Five metrics (L169, consensus; REG-093; "not to rank people" inferred); speed and stability correlated with supporting practices (L170, majority; REG-093, REG-097); outcomes, not volume (L1058; REG-1041, REG-1042, REG-1043, REG-1047). The contested net effect: automation raises throughput and satisfaction with instability a fixable side effect (REG-1041), or gains vanish at organisation level or are negative for experienced developers in mature code (REG-1043, sixteen developers, REG-1047); sample and vendor caveats apply.
3. **Positions.** P1 five DORA metrics. P2 speed and stability correlated with supporting practices. P3 outcomes, not volume; net effect contested (a) positive, (b) vanishes or negative.
4. **Rejected.** Output volume (code, pull requests) as the measure: best never, it measures activity. The conventional speed-versus-stability trade-off: no source read defends it. The net effect is not decided: (a) is best in teams with version control, small batches, testing, a platform and a clear policy; (b) elsewhere (L1058).
5. **Context.** Foundation practices (L1058): present means (a), absent means (b).
6. **Certainty.** Grounded for P1 and P2; grounded for the outcome-not-volume principle; open on the net effect of automation (contested, small samples, vendor sources).
7. **Flags.** none.

Constraints: MUST delivery be judged on the outcome measures; MUST NOT the metrics be used to rank individuals. Links: Related OPERATION.RELIABILITY (L169, L208), RELEASE.1.

### CHANGE_FLOW.MEASURE.2 Independent Baselines and Preconditions

Intent: how a measured gain is trusted and what must hold before automation is expected to help.

1. **Decision.** Do not rely on self-reported speed or security gains from automation: measure them against an independent baseline. Treat the delivery system's fundamentals (version control, small batches, testing, platform, clear policy) as preconditions: automation magnifies existing strengths and weaknesses. Outcome: a claimed gain is a measured gain, and automation is added where it will help.
2. **Grounds.** Independent baseline (L1059; REG-1043, REG-1044, REG-1050; findings from small samples, principle inferred); fundamentals as preconditions (L1060, majority; REG-1041, REG-1042).
3. **Positions.** P1 independent baseline. P2 preconditions.
4. **Rejected.** No competing position recorded. Self-reported gain as evidence: best never for a decision about adoption.
5. **Context.** none.
6. **Certainty.** Grounded for P2 (majority); inferred for P1 as principle (small samples).
7. **Flags.** none.

Constraints: MUST a claimed gain be measured against a baseline not produced by the claimant. Links: Related MEASURE.1, RELEASE.1.

---

## Flags raised (13), settled

F1 to F13 were settled in the final pass (see Final pass applied); none remains open and every record's Flags reads none.

## Review applied

Review fixes applied: 6 of 6. Flag findings FL1 to FL9 are not acted on (final Opus pass).

- FX1 applied: DATA_CHANGE.3 Decision states that configuration-like content uses the same one history, an authoring script allowed where the run is recorded; L294, L411 added to Grounds.
- FX2 applied: DATA_CHANGE.3 Grounds reworded (GitLab supports separating risky changes and release-manager timing; the named-group trigger rests on the maintainer and SECURITY.6); Certainty says the gate form has no public source.
- FX3 applied: DATA_CHANGE.1 Decision conditions the separate urgent-fix stream on frequent urgent fixes.
- FX4 applied: REVIEW.1 keeps approval by qualified named approvers only and points to DATA_CHANGE.3 and RELEASE.5 for who runs; the MUST on the production run removed.
- FX5 applied: DEPLOY.4 Decision names pull-reconcile and scripted push with drift detection as two forms with no switch; Context "none; pull versus push is open"; Rejected and Certainty aligned.
- FX6 applied: the eight L2 roll-ups list their children's flag ids (DATA_CHANGE now includes F13).

## Final pass applied

Resolutions (J6 section of the final pass):
- FL1 (DATA_CHANGE.3), cross-unit X6: applied. Decision replaced by the authorization-stage wording; Grounds add REG-107 and REG-245; Certainty splits grounded stage from inferred named group.
- FL2 (DATA_CHANGE.3): applied. Large-volume sentence deleted; criterion extended with the recorded table size and the unmeasured duration; Context replaced. Consequential edits in the same record, without re-judging: Rejected P3 and Grounds (L290 b) reworded to say the volume condition is carried by the criterion; Certainty names the size criterion instead of the large-volume condition.
- FL3 (DEPLOY.3): applied. "schema" replaced by "external or shared schemas present only in production".
- FL4 (ROLLBACK.3): applied. Reversible-form clause replaced; the P2 rejection line deleted; the rejection of a written reverse for every change added with REG-244, REG-251; Certainty marks the faster-than-restore condition inferred.
- FL5 (F1, DATA_CHANGE.3): applied as closed by FL2; F1 removed from Flags.
- FL6 (F4, DEPLOY.3): applied, record unchanged; F4 removed from Flags.
- FL7 (F11, BUILD.1): applied, record unchanged; F11 removed from Flags.
- FL8 (F12, RELEASE.5): applied. Certainty reworded as stated; decision and MUST unchanged; F12 removed from Flags.
- FL9 (F13, DATA_CHANGE.8): applied. MUST on the ticket key replaced by identifiability; checklist and incident sentence aligned; ramp steps a recommendation, concurrency MUST kept; Grounds adjusted; F13 removed.
- Judge flags F2, F3, F5, F6, F7, F8, F9, F10 (confirmed by the review): applied as settled, records unchanged; flags removed. F5 and F10 go against the maintainer's practice and are listed there by the final pass.

Cross-unit lines:
- X6: applied. DATA_CHANGE.3 holds the database procedure and points to ASSURANCE.SECURITY.6; DATA_CHANGE.8 points to both (new sentence and Links).
- X14: applied. REVIEW.1 Rejected P3 points to RULES.4 for the reason, without restating it (MD-03); the author-is-the-worst-judge wording is gone.
- X1 to X5, X7 to X13: not applied here, no J6 record named (units column does not list J6).

Nodes added: none. Maintainer point (ASSURANCE.RULES.4): J2 only, not applicable. Flags still open: none (F1 to F13 settled; every Flags line reads none, including the eight L2 roll-ups).
