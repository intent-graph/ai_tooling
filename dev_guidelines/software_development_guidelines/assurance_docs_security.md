# Assurance: Documentation and Security

## Table of Contents

1. [Documentation in Sync](#documentation-in-sync) _(Lines 25-27)_
   1. [Delivery with the Change](#delivery-with-the-change) _(Lines 30-40)_
   1. [Gates and Review of Documentation](#gates-and-review-of-documentation) _(Lines 43-56)_
   1. [Ownership, Freshness and Single Source](#ownership-freshness-and-single-source) _(Lines 59-67)_
   1. [Mechanical Documentation Checks](#mechanical-documentation-checks) _(Lines 70-80)_
1. [Security](#security) _(Lines 83-85)_
   1. [Verification Depth and Design Review](#verification-depth-and-design-review) _(Lines 88-96)_
   1. [Stage Placement and Blocking Policy](#stage-placement-and-blocking-policy) _(Lines 99-109)_
   1. [Verification Techniques](#verification-techniques) _(Lines 112-131)_
   1. [Static and Scheduled Analysis Practice](#static-and-scheduled-analysis-practice) _(Lines 134-144)_
   1. [Secrets and Consumed Code](#secrets-and-consumed-code) _(Lines 147-156)_
   1. [Enforced Limits on Automation and Access](#enforced-limits-on-automation-and-access) _(Lines 159-174)_
   1. [Closing the Loop on Findings](#closing-the-loop-on-findings) _(Lines 177-182)_

---

Part of [Assurance](assurance.md). Documentation that cannot drift, and security checked on every change at a depth set by risk.

## Documentation in Sync
<!-- Lines 25-27 -->

Documentation cannot drift because each fact has one origin, documentation travels with the change it describes, and a change that needs documentation cannot merge or ship without it (a recorded waiver is the only exception). Machines check what they can, a reviewer verifies accuracy, and every hand-written document has an owner and a dated verification. Whether design or code comes first is not decided here: the origin of each fact is chosen per fact, only the guarantee is fixed. The residual risk, semantic drift in hand-written text, is owned and scheduled for review. Authoring and organisation: [Documentation Practice](transverse_documentation.md#documentation-practice). `ASSURANCE.DOCS_SYNC`

### Delivery with the Change
<!-- Lines 30-40 -->

Documentation is plain text in version control, in the repository of what it documents, changed through the same review and CI as code. A change that alters documented behaviour carries its documentation in the same change. Where documentation ships only with a release (release trains, many contributors, a documentation team working in parallel), it may travel separately, provided a release gate blocks any feature without it; there is then no window in time between a change and its documentation. A documentation-only change may run a reduced pipeline.

Rules:
- MUST keep documentation in version control beside the code.
- MUST NOT run a reduced pipeline over checks that execute documentation examples or verify references.

Best instead when: a separate request on a release branch, for a release train with a documentation team, with the release gate holding. A parallel documentation process outside tracker, review and CI is never the best.

Requires [Gates and Review of Documentation](#gates-and-review-of-documentation). `ASSURANCE.DOCS_SYNC.1`

### Gates and Review of Documentation
<!-- Lines 43-56 -->

The team states which changes require documentation (user- or admin-visible features, interface changes, changed workflows, deprecation and removal; internal-only changes exempt). Each change declares its documentation impact: updated, or not needed and why. A CI rule fails the merge when the trigger is met and no documentation changed. A reviewer able to verify it checks accuracy and that documentation of deleted or deprecated code is removed. A waiver is a declaration in the change, with a follow-up issue opened at once, granted by the reviewer who approves the change ([Independent Review That Binds](assurance_rules.md#independent-review-that-binds)), never a skipped check. A path rule detects the absence of an edit, not its accuracy.

Rules:
- MUST define the trigger.
- MUST make the waiver a visible recorded exception.
- MUST NOT let a check that only detects absence stand in for accuracy review.

Review split: accuracy review is blocking; audience and writing review are non-blocking by default and blocking for customer-facing or cross-boundary documentation. Documentation paths map to owners where the platform supports required owner review. On a release train, add the release gate.

Best instead when: encouragement plus reviewer enforcement as the whole policy, only where documentation is not part of the product contract and follow-up is reliably tracked; a release gate alone, only where release trains make merge-time gates impractical (then as an addition to the merge check).

A gate with a recorded, independently granted override is the pattern of [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped) and [Guarding Bulk and Destructive Operations](assurance_interfaces_data.md#guarding-bulk-and-destructive-operations). Open: sources split on hard versus soft gate; the combination (declared impact checked by CI, plus reviewer verification) is a synthesis. `ASSURANCE.DOCS_SYNC.2`

### Ownership, Freshness and Single Source
<!-- Lines 59-67 -->

Each fact has one canonical origin and is stated once; competing copies are consolidated into it. A derived or generated document is read-only and never copied back into its source. Every hand-written document has a named owner, a date and the target it was verified against, a scheduled review tracked as a bug, and removal or an obsolete mark when it no longer serves. Fast-moving topics point to the more current tracker. Open known violations are recorded with status and mitigation, and a mitigation is never presented as a fix.

Rules:
- MUST name an owner per document and state the verification date and target.
- MUST NOT edit a generated document or copy it back into its source.

A date states when someone last verified, not that the text is true; it is never the only mechanism ([Gates and Review of Documentation](#gates-and-review-of-documentation) and [Mechanical Documentation Checks](#mechanical-documentation-checks) exist for that). Interface descriptions: [One Source of Description](assurance_interfaces_data.md#one-source-of-description). Upkeep of recovery plans and runbooks sits in [operation.md](operation_recovery_and_feedback.md#backup-restore-and-disaster-recovery). `ASSURANCE.DOCS_SYNC.3`

### Mechanical Documentation Checks
<!-- Lines 70-80 -->

CI executes the code examples in documentation, fails the documentation build on warnings and unresolved references, checks links on every change and on a schedule, and runs rules for review chores (changelog entry present, documentation touched when interface files changed). Breakage a machine can see fails a build. Semantic drift is left to the reviewer gate; this node does not claim to catch it.

Rules:
- MUST keep executed examples readable.
- MUST run link checks on a schedule as well as on change (external links break without a commit).

Best instead when: editorial style as a CI rule only when many authors need consistency without reviewer effort; clarity and audience stay with human review. Human review as the only check on examples and references is never the best, since machines do these cheaply. Cost: executed examples are fragile to exact output.

Requires [Gates and Review of Documentation](#gates-and-review-of-documentation). `ASSURANCE.DOCS_SYNC.4`

## Security
<!-- Lines 83-85 -->

Verification depth is set per application from its risk and written down. Each check runs at the earliest stage it can; high-confidence, low-noise checks block with an audited waiver and the rest advise. Every change passes a floor of security testing whoever wrote it. Consumed code and secrets are verified like own code. Limits on automation and data access are enforced in tooling, not by instruction, and verification is itself verified. Security programme practice is in [Security Practice](transverse_security.md#security-practice). `ASSURANCE.SECURITY`

### Verification Depth and Design Review
<!-- Lines 88-96 -->

Depth is set per application from its risk profile. The assurance target is written down and revisited when risk changes (new personal data, new regulatory scope). The design is reviewed for security, by a qualified person or by automated processes against the risk model, before implementation proceeds. The threat-model output selects test cases and the code that gets focused review.

Rules:
- MUST record the assurance target.
- MUST review the design before implementation proceeds.

Best instead when: a uniform depth for all applications is never the best as a policy; the floor of [Verification Techniques](#verification-techniques) is the target only for low-risk applications. Open: what triggers a revisit is inferred. The depth selects the requirement level of the [Anchor Framework](transverse_security.md#anchor-framework). `ASSURANCE.SECURITY.1`

### Stage Placement and Blocking Policy
<!-- Lines 99-109 -->

A recorded policy states per stage and risk which security checks run and who reviews findings. Each check runs at the earliest stage it can: secrets and lint before commit; static, composition and infrastructure scanning at build; dynamic and interactive testing against a running instance; compliance audit after deployment. Whether a finding blocks or advises follows [Trustworthy Signal](assurance_rules.md#trustworthy-signal): it blocks only while its measured false-alarm rate is within the team's budget (one published operating figure: about 10 percent of findings judged not useful, one organisation's). Every block carries an audited waiver; who may waive is configured explicitly, since on common platforms anyone with write access can bypass by default. For public-facing or regulated software, confirmed exploitable findings above a set severity also block at release. Findings are triaged in the normal workflow, and a human reviews tool findings and remediates.

Rules:
- MUST record the policy and the waiver rule.
- MUST NOT make a check blocking before developers trust its output.

Best instead when: blocking for every check is best only for high-confidence, low-noise checks and regulated contexts; advisory for every check, for noisy analyses; leaving the policy to the team, only where one team owns the whole pipeline and still records its policy.

Requires [Trustworthy Signal](assurance_rules.md#trustworthy-signal), [Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed), [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped); realised in [Build and Pipeline](change_flow_delivery.md#build-and-pipeline). `ASSURANCE.SECURITY.2`

### Verification Techniques
<!-- Lines 112-131 -->

Every change passes a floor of security verification whoever produced it, assuming code may carry vulnerabilities:
- functional tests of the security features themselves, in a sandbox where appropriate, and tests of the secure default configuration;
- a static scan and a search for hardcoded secrets;
- tests derived from specifications, threats and past bugs;
- builds and test runs that enable the checks and protections the language, compiler and runtime provide;
- fuzzing of components that parse untrusted input (pre-release at minimum, continuous where practical);
- for a web interface, a dynamic or interactive scan against a running instance.

Automated testing is combined with manual expert testing aimed first at the highest-risk components. Penetration testing is regular where criticality or regulation is high, and triggered by a significant change to a high-risk component's attack surface.

Rules:
- MUST apply the floor to every change.
- MUST test the default configuration.
- No coverage figure is stated here: [Measuring Adequacy and Probing for Faults](assurance_behaviour.md#measuring-adequacy-and-probing-for-faults) decides it.

Best instead when: the fuller programme (application-specific automation, regular penetration tests) for all applications, under high criticality or regulation; the dynamic scan does not apply to non-web software.

Open: no source gives a penetration-test period, and none supports "as the practice matures" as a trigger; the manual-testing sequence is inferred. Test levels: [Test Level Mix](assurance_behaviour.md#test-level-mix); depth: [Verification Depth and Design Review](#verification-depth-and-design-review); static scan practice: [Static and Scheduled Analysis Practice](#static-and-scheduled-analysis-practice). `ASSURANCE.SECURITY.3`

### Static and Scheduled Analysis Practice
<!-- Lines 134-144 -->

Static analysis runs as soon as code is written and repeats automatically per commit or in review, so no new weakness goes unreported. An analysis too slow for that (whole-system analysis, sanitizers, run-time assertions) runs on a schedule, nightly or at least daily. Because static analysis has blind spots and false positives, the team standardises on tools, keeps a must-fix list, triages and suppresses deliberately, and uses more than one analyser where weakness classes differ.

Rules:
- MUST keep a must-fix list.
- MUST suppress a finding deliberately and visibly.

Best instead when: running slow analyses on every change, if cheap enough to give feedback inside the change; per-change only is never the best for sanitizers and whole-system runs.

Refines [Static Layer](assurance_behaviour.md#static-layer); whether a finding blocks follows [Stage Placement and Blocking Policy](#stage-placement-and-blocking-policy). `ASSURANCE.SECURITY.4`

### Secrets and Consumed Code
<!-- Lines 147-156 -->

Secret scanning is layered: editor or pre-commit, a blocking check at push time, and CI. Blocking before a secret reaches shared history is preferred to alerting after. Consumed libraries, packages and services receive the same verification as own code: scanned for known vulnerabilities, licence and end-of-life status, and at higher maturity for malware, before and after integration.

Rules:
- MUST layer secret scanning.
- A bypass MUST get the audited waiver of [Stage Placement and Blocking Policy](#stage-placement-and-blocking-policy).
- A secret found in history MUST be rotated: [Response to a Leaked Secret](transverse_config_environments.md#response-to-a-leaked-secret).

Best instead when: alert-after scanning only, where blocking is impossible on the platform; pre-commit alone is never the best (bypassable). The inventory of consumed components stays in [Inventory, Watching and End of Life](ownership_lifecycle_containment.md#inventory-watching-and-end-of-life). `ASSURANCE.SECURITY.5`

### Enforced Limits on Automation and Access
<!-- Lines 159-174 -->

Limits on what any actor can touch, a person, a script or an automated agent, are enforced in tooling at the lowest layer every path passes through, never by an instruction the actor is asked to follow. The condition that moves the rest: does the actor act without a person's judgement at the moment of action?

- Such an actor gets the least functionality, permission and autonomy its task needs (sandbox, scoped credentials, deny rules, deterministic hooks, scoped workspace, no outbound network by default). Any text it reads is untrusted input. Files that steer it are versioned and reviewed like code, and read-only to it where possible. Per-action human approval is paired with enforced boundaries, never the only control.
- Data access goes through one guarded path: single statements, read-only on production, a statement timeout, an audit log, least-privilege roles separate from application permissions.
- A job with a large blast radius: the decision to execute under guards or to write a reviewed script only is recorded. Execute under guards where they can be applied and effects are reversible; otherwise it is a reviewed script, authorized and triggered by the accountable person or named group ([Independent Review That Binds](assurance_rules.md#independent-review-that-binds)) through the guarded path (the pipeline wherever it reaches the target).

Rules:
- Limits MUST be enforced in tooling, never by instruction.
- An actor acting without a person's judgement MUST NOT combine untrusted input, access to sensitive systems and outward state change without a human gate.
- MUST record the execute-or-write-only decision for a large-blast-radius job.

Best instead when: application-only authorization, if the store is reachable only through that application; an agent executing under a classifier or sandbox, if guards can be applied and the effect is reversible.

Open: the three-condition rule's generalisation and the recorded-decision framing are inferred. Requires [Security Practice](transverse_security.md#security-practice) and [Change Attribution and Actor Rules](change_flow_integration_review.md#change-attribution-and-actor-rules); the database procedure is in [Delivery Path and Gating of Database Change](change_flow_data_and_measure.md#delivery-path-and-gating-of-database-change); bound on every actor by [Protected Mainline Binds Every Actor](assurance_rules.md#protected-mainline-binds-every-actor). `ASSURANCE.SECURITY.6`

### Closing the Loop on Findings
<!-- Lines 177-182 -->

Security verification is itself verified. A test or scan that raises no alert is treated as a detection failure, and a regular process evaluates the effectiveness of the measures, including the ability to restore availability and access to data. A defect found is fixed, the process is changed to catch its class earlier, and where possible an approach is chosen that precludes the class.

Rule: MUST test that a known probe raises an alert. Fixing the instance without changing the process is never the best.

Requires [Proving Restore](assurance_performance_availability.md#proving-restore); see [Defect Classes That Survive Review](assurance_behaviour.md#defect-classes-that-survive-review) and incident handling in [operation.md](operation.md). `ASSURANCE.SECURITY.7`
