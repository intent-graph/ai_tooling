# Change Flow: Integration and Review

How changes are sourced into the mainline and independently reviewed before they integrate. Part of [Change Flow](change_flow.md), which holds the thesis and the index.

## Table of Contents

1. [Version Control and Integration](#version-control-and-integration) _(Lines 24-26)_
   1. [Repository Content and Shape](#repository-content-and-shape) _(Lines 29-41)_
   1. [Integration Frequency and Branch Life](#integration-frequency-and-branch-life) _(Lines 44-54)_
   1. [Branching Model and Release Branches](#branching-model-and-release-branches) _(Lines 57-65)_
   1. [Merge Method and Commit Practice](#merge-method-and-commit-practice) _(Lines 68-80)_
   1. [Mainline Health and Batch Size](#mainline-health-and-batch-size) _(Lines 83-87)_
   1. [Change Attribution and Actor Rules](#change-attribution-and-actor-rules) _(Lines 90-103)_
1. [Review](#review) _(Lines 106-110)_
   1. [Mechanism and Depth by Risk](#mechanism-and-depth-by-risk) _(Lines 113-126)_
   1. [Unit of Review and Response Speed](#unit-of-review-and-response-speed) _(Lines 129-136)_
   1. [What the Reviewer Reads and Approves](#what-the-reviewer-reads-and-approves) _(Lines 139-145)_
   1. [Automated and Second-Reviewer Layers](#automated-and-second-reviewer-layers) _(Lines 148-158)_

---

## Version Control and Integration
<!-- Lines 24-26 -->

Everything needed to build, deploy and restore lives in version control, and work reaches one mainline in small, frequent, attributable changes. A broken mainline is fixed before anything else. Realizes the mainline gates of [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped) and [Protected Mainline Binds Every Actor](assurance_rules.md#protected-mainline-binds-every-actor). `CHANGE_FLOW.INTEGRATION`

### Repository Content and Shape
<!-- Lines 29-41 -->

The repository holds everything needed to build, deploy and restore, so a clean machine rebuilds the system from it alone through the build of [Scripted, Hermetic, Visible Build on Every Push](change_flow_delivery.md#scripted-hermetic-visible-build-on-every-push). Each deployable has one codebase; code shared across applications is a versioned library; one version of each shared component holds at any time, whatever the layout. The one-version rule is a case of [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle).

- The repository MUST hold source, scripts, infrastructure and application configuration, and dependency declarations.
- One version of each shared component MUST hold at any time.

Best instead when:
- Monorepo: one organization with tooling investment and many interdependent projects.
- Multiple repositories: regulated or access-segmented work (the invariant stays).
- Virtual monorepo: separate repositories are required and one version must still hold.

Open: which layout wins in general is not decided; the layout debate rests on one practitioner source. `CHANGE_FLOW.INTEGRATION.1`

### Integration Frequency and Branch Life
<!-- Lines 44-54 -->

Work is integrated into the mainline at least daily; a branch lives hours to a couple of days. Unfinished work that spans longer is merged hidden (flag, dark launch, keystone, branch by abstraction), not held in a branch. Deferred integration costs more in conflicts, isolation and late feedback. Hidden work uses the flags of [Separating Release From Deployment](change_flow_delivery.md#separating-release-from-deployment).

- A branch MUST be merged or deleted within days (the limit is the team's; default a couple of days).
- Unfinished work on the mainline MUST be hidden, and its toggle MUST carry an owner and an expiry.
- Default bound: three or fewer active branches; a default, not a rule.

Best instead when:
- Feature branches merged when complete: open source with many untrusted or part-time contributors, or features of one to two days.
- Daily integration is best preceded by trust in the tests ([Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed)); without them it multiplies unchecked merges. `CHANGE_FLOW.INTEGRATION.2`

### Branching Model and Release Branches
<!-- Lines 57-65 -->

The branching model follows the release model. One continuously delivered live version uses short branches off one mainline and fixes go forward. Explicitly versioned or multi-version software cuts a release branch just in time, fixes on the mainline, copies each fix into the release branch and deletes it after release. A branch exists only as long as a version needs separate fixes. Cadence follows the same model ([Cadence and Batch Size](change_flow_delivery.md#cadence-and-batch-size)); without a release branch, fix forward as chosen in [Detecting and Deciding to Roll Back](change_flow_delivery.md#detecting-and-deciding-to-roll-back).

- A release branch, when it exists, MUST receive fixes copied from the mainline, not by merge back.

Best instead when:
- Standing release branches: only when several versions are in the field.
- No release branch at all: only when the release cycle is hours; for a supported-versions product a fix to an old version has nowhere to land. `CHANGE_FLOW.INTEGRATION.3`

### Merge Method and Commit Practice
<!-- Lines 68-80 -->

A change is one logical unit that can be read and reverted as one; each commit is atomic and says what changed and why; unrelated changes go in separate branches or pull requests. One merge method is chosen and recorded per repository: squash for small single-unit changes (the default when changes stay small, see [Mainline Health and Batch Size](#mainline-health-and-batch-size)), rebase when well-structured atomic commits are worth keeping, merge commit when integration events must be traced. A structured message format is used only where tools generate releases from history.

- One merge method MUST be recorded per repository.
- A commit MUST be atomic and say what and why.

Best instead when:
- Rebase: commits are well structured and bisect granularity matters.
- Merge commit: integration events must be traced (audit).
- Structured message format: history is parsed by automation; without a generator it costs every author and serves nobody.

Open: no source ranks the three merge methods; the squash default is inferred. `CHANGE_FLOW.INTEGRATION.4`

### Mainline Health and Batch Size
<!-- Lines 83-87 -->

A broken mainline is the highest-priority work: the faulty change is reverted and a named person owns the fix. Batches stay small, commits frequent and rollback routine, more so as change volume rises, so version control remains the safety net whoever or whatever produces the change. Small batches keep the unit of [Unit of Review and Response Speed](#unit-of-review-and-response-speed) readable; routine rollback needs the compatibility of [Reversible by Design](change_flow_delivery.md#reversible-by-design).

- A broken mainline MUST be reverted or fixed before new work merges. Waiting for the author is best never: every later integration is blind. `CHANGE_FLOW.INTEGRATION.5`

### Change Attribution and Actor Rules
<!-- Lines 90-103 -->

Every change carries a recorded trail of its author, its approver and, for an automated author, the tool and session. Automation uses identities distinct from human ones; a change not attributable to a person needs approval by a named accountable person. The bar is the same whatever the origin of a change, so no disclosure rule is needed. The trail feeds [Mechanism and Depth by Risk](#mechanism-and-depth-by-risk) and carries out [Protected Mainline Binds Every Actor](assurance_rules.md#protected-mainline-binds-every-actor), [Independent Review That Binds](assurance_rules.md#independent-review-that-binds) and [One Bar and Evidence for Every Change](assurance_rules.md#one-bar-and-evidence-for-every-change).

- An automated author MUST use an identity distinct from a human one.
- An unattributed change MUST be approved by a named person.
- The bar MUST NOT depend on who authored.

Best instead when:
- Mandatory disclosure of tool use on top of the trail: reviewer time is scarce and intake is public (open contribution), where disclosure lets a reviewer calibrate depth.
- Shared human-and-bot identities: best never, attribution is lost.

Open: the no-disclosure choice rests on one maintainer ruling and one inference. `CHANGE_FLOW.INTEGRATION.6`


## Review
<!-- Lines 106-110 -->

Review carries out the independent, accountable review bound to the exact content decided in [Independent Review That Binds](assurance_rules.md#independent-review-that-binds). The mechanism follows team and risk, depth follows risk and evidence of understanding, units are small and answered quickly, and automation runs first while a second automated reviewer only assists. Review stays trustworthy and review capacity does not become the constraint.

A person other than the author is the independent check by default; an automated reviewer is the independent check only for the low-risk tier the team declares in advance, and a named person approves every change (see [Automated and Second-Reviewer Layers](#automated-and-second-reviewer-layers)). `CHANGE_FLOW.REVIEW`

### Mechanism and Depth by Risk
<!-- Lines 113-126 -->

Every change meets the one bar of [One Bar and Evidence for Every Change](assurance_rules.md#one-bar-and-evidence-for-every-change) and the independent check before integration of [Independent Review That Binds](assurance_rules.md#independent-review-that-binds). The mechanism (asynchronous approval, synchronous review or pairing, post-merge show for the defined low-risk tier) is chosen per team and recorded. Depth rises with risk and wherever the submitter's understanding cannot be assumed (public intake, high volume, many contributors); a high-blast-radius change is approved by named approvers qualified for that class.

- A high-blast-radius change MUST name its approvers.
- Depth MUST NOT be reduced because the author is trusted or automated.

Best instead when:
- Pairing as the review: a small trusted team that pairs, with the second person recorded.
- Mandatory asynchronous approval: larger or less-trusting teams, regulated change control, many contributors.
- Post-merge show: low-risk change with automatic gates and revert, as a tier only.
- Seniority as the qualification: a small trusted senior group and few critical changes.

`CHANGE_FLOW.REVIEW.1`

### Unit of Review and Response Speed
<!-- Lines 129-136 -->

A unit of review is small enough to be read meaningfully in one sitting, with refactoring in separate changes and tests beside the logic they cover. A reviewer answers within a bounded time. When production volume rises, review capacity is the binding constraint, so reviews must stay real and waiting must stay bounded.

- A unit of review MUST be small enough to be read in one sitting.
- A reviewer MUST answer within the team's stated bound.
- Size thresholds in sources differ (100 and 200 lines); treat any number as a team default.
- Large reviews approved by skim are best never: the review signal then proves nothing. `CHANGE_FLOW.REVIEW.2`

### What the Reviewer Reads and Approves
<!-- Lines 139-145 -->

A change is approved when it definitely improves overall code health even if imperfect; facts overrule preference; a second reader must be able to understand it. Review is guided by an owned, freshness-checked catalog of defect patterns, read by type of change, which doubles as an audit list. The catalog relies on the defect classes that survive review (see the behaviour section of [assurance.md](assurance.md)).

- A second reader MUST be able to understand the change.
- The catalog MUST have an owner; an ownerless catalog misdirects review.
- Perfection as the approval bar slows delivery for no gain in health. `CHANGE_FLOW.REVIEW.3`

### Automated and Second-Reviewer Layers
<!-- Lines 148-158 -->

Format, lint, tests and build run before the human reviewer so attention goes to design and logic; these are the checks of [Scripted, Hermetic, Visible Build on Every Push](change_flow_delivery.md#scripted-hermetic-visible-build-on-every-push), placed per [Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed). A second automated reviewer may be added as an extra layer and never as the approving party: a named person approves every change. It is the independent check only for the tier of low-risk changes the team declares in advance; every other change is checked by a person other than its author.

- Automated checks MUST run before the reviewer is asked.
- An automated reviewer MUST NOT be the approving party.
- An automated reviewer MUST NOT be the independent check outside the declared low-risk tier.

Best instead when:
- The second reviewer is the independent check: only for the declared low-risk tier, with a named person still approving. Outside that tier the person's check stays in force and governs approval.

Open: no study read on the accuracy of an automated second reviewer. `CHANGE_FLOW.REVIEW.4`
