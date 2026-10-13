# Assurance: Rules and Artifact Integrity

## Table of Contents

1. [Rules Common to Every Property](#rules-common-to-every-property) _(Lines 21-23)_
   1. [Trustworthy Signal](#trustworthy-signal) _(Lines 26-45)_
   1. [Placement and Feedback Speed](#placement-and-feedback-speed) _(Lines 48-60)_
   1. [Gates That Cannot Be Skipped](#gates-that-cannot-be-skipped) _(Lines 63-73)_
   1. [Independent Review That Binds](#independent-review-that-binds) _(Lines 76-93)_
   1. [One Bar and Evidence for Every Change](#one-bar-and-evidence-for-every-change) _(Lines 96-105)_
1. [Artifact Integrity](#artifact-integrity) _(Lines 108-110)_
   1. [Build Provenance and Match to Source](#build-provenance-and-match-to-source) _(Lines 113-126)_
   1. [Protected Mainline Binds Every Actor](#protected-mainline-binds-every-actor) _(Lines 129-139)_

---

Part of [Assurance](assurance.md). The five rules every property obeys, and the two mechanisms that tie what runs to what was reviewed.

## Rules Common to Every Property
<!-- Lines 21-23 -->

A check is worth running only if its failure means a real defect, and it runs as low and as early as it can catch that failure. A rule that matters is enforced by a gate that cannot be skipped. Review is independent, accountable and bound to the exact content, and every change meets one bar and shows completion by evidence. Numeric defaults below are one organisation's or one source's figures: the team states its own. `ASSURANCE.RULES`

### Trustworthy Signal
<!-- Lines 26-45 -->

A failing check must mean a real defect, so a pass can be believed and a finding is acted on.

- Prevent non-determinism at its cause: each test establishes the state it needs. Where rebuilding per test costs too much, the platform does the undo (a rolled-back transaction, a snapshot restore), never hand-written clean-up code.
- A flaky test that already exists is a defect of the pipeline: take it out of the blocking gate into a quarantine, then fix or delete it.
- A check blocks while its measured false-alarm rate is within the budget the team states; a lower-confidence check is shown in review as advice, also under a budget.

Rules:
- A check, blocking or advisory, MUST have a stated false-alarm budget; over budget, it MUST be fixed or removed.
- A quarantined test MUST have an owner, a numeric cap and an end date.
- A rerun MUST NOT hide a failure.

Best instead when:
- Immediate removal: the test is of low value or nobody will own the quarantine.
- Rerun of marked tests: only as a recorded, capped part of quarantine, or for a failure traced to infrastructure.
- Hand-written clean-up of shared state: neither a rebuild nor a platform undo is available; then each test checks its precondition at its start.
- A flake-rate threshold near 1 percent: as the budget only when the team has no better data of its own.

This node holds the rule; [Static Layer](assurance_behaviour.md#static-layer) and [Stage Placement and Blocking Policy](assurance_docs_security.md#stage-placement-and-blocking-policy) apply it. The rebuild-over-clean-up rule meets the rollback on shared data of [Tests Without Durable Effect on Data](assurance_behaviour.md#tests-without-durable-effect-on-data): the rollback is read as the platform undo, valid under that node's condition. `ASSURANCE.RULES.1`

### Placement and Feedback Speed
<!-- Lines 48-60 -->

Each check runs at the lowest level and the earliest stage that can catch its failure. A defect that a higher-level test finds and no lower-level test caught produces the lower-level test. Blocking feedback returns in minutes (about ten), the build runs on every commit, a broken build is fixed first, and the policy of which analyses and tests run at which stage for which risk is recorded. Kinds of check are combined; none is the only line of defence.

Rules:
- The blocking set MUST return in minutes.
- Every higher-level miss MUST produce a lower-level test.
- A stage policy MUST be recorded per risk.

Best instead when:
- Very high change volume, a build owner and automatic rollback: gate on what is fast and reliable, run slower tests after merge, revert automatically on failure. Otherwise run the later stages before release in a staged pipeline. In both, what ships has passed the full set.

The ten-minute figure is a default, not a measured optimum. Requires [What the Suite Must Promise](assurance_behaviour.md#what-the-suite-must-promise) and [Gates That Cannot Be Skipped](#gates-that-cannot-be-skipped); the pipeline itself is in [change_flow.md](change_flow_delivery.md#build-and-pipeline). `ASSURANCE.RULES.2`

### Gates That Cannot Be Skipped
<!-- Lines 63-73 -->

A rule that matters is a blocking automated check, not a convention. Module boundaries and fitness properties (performance, security, operability) are checked automatically. The gate always runs, and nothing a rule forbids reaches the mainline, whoever authored the change.

Rules:
- A required check MUST fail closed: skipped, neutral or missing counts as failed.
- A blocking check MUST NOT be a noisy one ([Trustworthy Signal](#trustworthy-signal)).

Best instead when: convention or review alone is the better tool only for a rule that cannot be expressed as a check (is this design appropriate); that belongs to review ([Independent Review That Binds](#independent-review-that-binds)).

Carried out for the mainline by [Protected Mainline Binds Every Actor](#protected-mainline-binds-every-actor) and [change_flow.md](change_flow_integration_review.md#version-control-and-integration). `ASSURANCE.RULES.3`

### Independent Review That Binds
<!-- Lines 76-93 -->

Every change to mainline is checked before integration by a party other than whoever authored, pushed or requested it, working from its own context. The check is recorded on the development platform. The reviewer is a person other than the author by default; an automated reviewer working from its own context is the independent check only for a tier of low-risk changes the team declares in advance. A named person stays accountable for each change, approves it and is able to defend it. An approval binds the exact final content: a new commit that changes the diff voids earlier approvals.

Rules:
- The approver MUST differ from the author.
- An approval MUST lapse when the diff changes.
- A named person MUST be accountable and MUST approve every change.
- An automated reviewer MUST NOT be the independent check outside the declared low-risk tier.
- Only a tier the team defines in advance, in a team whose mainline is kept releasable by automated gates and fast revert, may be checked after merge. The default is blocking review before merge.
- Per-change approval by an external board is not used.

Best instead when:
- Review of uncertain changes only: it leaves the classification to the author at the moment of the change. A tier defined in advance removes that discretion; in post-merge form it is the best for that tier.
- No review at all: never; every change gets an independent check before or after merge.
- An external approval board: where a regulation requires one (whether a given regulation still does was not checked).

How review is carried out: [Review](change_flow_integration_review.md#review). Realised for the mainline by [Protected Mainline Binds Every Actor](#protected-mainline-binds-every-actor). `ASSURANCE.RULES.4`

### One Bar and Evidence for Every Change
<!-- Lines 96-105 -->

Every change, whatever its author, meets the same bar for design, testing and review. Before a change is produced, its intent, scope, interfaces, out-of-scope items and acceptance check are fixed, in proportion to its size. Every change comes with an executable pass-or-fail check independent of the author's judgement that it is done, and completion is shown as evidence (test output, command and result, screenshot), not asserted. Tests and the code under test come from independent contexts where practicable.

Rules:
- Every change MUST carry an executable check.
- Completion MUST be shown by evidence.
- A change MUST NOT be exempt by its author, whether generated or from a trusted author.

The cheaper and faster a change is produced, the more it matters to fix the acceptance check first. The independent-contexts clause rests on a recommendation, not on a study of its effect. Requires [Trustworthy Signal](#trustworthy-signal) and [Independent Review That Binds](#independent-review-that-binds); refined by [What the Suite Must Promise](assurance_behaviour.md#what-the-suite-must-promise); evidence is realised in [Review](change_flow_integration_review.md#review). `ASSURANCE.RULES.5`

## Artifact Integrity
<!-- Lines 108-110 -->

What runs is what was reviewed and built from reviewed source. Two mechanisms do it, which the other branches only operate: a protected mainline that binds every actor, and verifiable build provenance checked before the artifact is used. Operated in [change_flow.md](change_flow_delivery.md#build-and-pipeline), [change_flow.md](change_flow_integration_review.md#version-control-and-integration) and [Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code). `ASSURANCE.ARTIFACT`

### Build Provenance and Match to Source
<!-- Lines 113-126 -->

Every deployed or distributed artifact is produced by a hosted build platform that emits signed provenance, and that provenance is verified before the artifact is used. Executable objects deployed without a build artifact are compared mechanically with their source, and each release is archived with its provenance.

Rules:
- MUST produce provenance from a hosted build platform and MUST verify it before use.
- MUST declare the level reached and the gap to the stated floor where below it.
- MUST detect drift of objects that bypass the build.

Level by risk: the second level of a published build-integrity framework is the floor (on a hosted platform it costs one step; whoever runs a build can produce first-level provenance). Raise to hardened, isolated builds where insider or credential-compromise risk matters or the software is distributed to others. Bit-identical reproducible builds with independent rebuild belong only to the highest assurance.

Best instead when: first-level provenance only, where no hosted build platform is in use (declare the gap); drift comparison applies where deployed definitions can change outside the pipeline.

Open: the second-level floor is grounded for one platform and inferred for others; what a release archive must contain is inferred. Related: [Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code); the build service as supply chain is in [ownership.md](ownership.md). `ASSURANCE.ARTIFACT.1`

### Protected Mainline Binds Every Actor
<!-- Lines 129-139 -->

The mainline is protected mechanically by required review and required status checks before merge, no force push and restricted push rights. These rules bind every actor, bots and administrators included. Automation pushes only to a restricted, non-protected target and cannot bypass the rules through the access it holds. So what is merged was reviewed and checked, whoever pushed it.

Rules:
- MUST enforce review and checks by the platform, not by convention.
- MUST apply them to bots and administrators.
- MUST restrict automation to a non-protected target.

Best instead when: advisory review, or checks an administrator or bot can bypass, are never the best for the guarantee that what runs is what was reviewed. Add signed commits where provenance of authorship is required.

Carries out [Gates That Cannot Be Skipped](#gates-that-cannot-be-skipped), [Independent Review That Binds](#independent-review-that-binds) and the limits of [Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access); carried out in [Version Control and Integration](change_flow_integration_review.md#version-control-and-integration). `ASSURANCE.ARTIFACT.2`
