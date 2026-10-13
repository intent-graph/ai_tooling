# Evolution

Significant decisions are recorded where the code lives and superseded, never rewritten. Change is made in steps that keep the system releasable, and every dual-support phase ends with a removal. Debt is an inventoried liability repaid where code changes, and obsolete forms are retired in two announced stages by an owner. The set of technologies stays small because each addition is a replacement, so the system keeps working while it changes and nothing old stays by neglect. `EVOLUTION`

Rules at this height:

- A significant decision MUST have a record that outlives its author.
- An incompatible change MUST have a removal step and an owner.
- A retirement MUST have verified usage and a stated deadline.
- A technology MUST NOT be added without the retirement of what it replaces, or a stated reason none exists.

Certainty: the decision record, expand-migrate-contract and staged retirement are well grounded. Debt-repayment timing, the conditions for a full rewrite and how firmly the technology set is held are inferred. Two points stay open, shown inline at [Replacement Versus Rewrite](#replacement-versus-rewrite) and [One General-Purpose Store for Several Roles](#one-general-purpose-store-for-several-roles). No maintainer decision is awaited in this branch.

Map:

| Section | What it decides |
|---|---|
| [Decision Records](#decision-records) | What is written down about a significant decision, where, and how it changes |
| [Incremental Change](#incremental-change) | How change proceeds without breaking the system, and who owns a migration |
| [Technical Debt and Refactoring](#technical-debt-and-refactoring) | What counts as debt, how it is found, and when it is repaid |
| [Decommissioning](#decommissioning) | How a form, interface or system is retired and removed |
| [Keeping Technologies Few](#keeping-technologies-few) | How the set of technologies is held small |

## Table of Contents

1. [Decision Records](#decision-records) _(Lines 63-65)_
   1. [Content of a Record](#content-of-a-record) _(Lines 68-75)_
   1. [Significance Threshold](#significance-threshold) _(Lines 78-87)_
   1. [Form and Storage](#form-and-storage) _(Lines 90-97)_
   1. [Changing an Accepted Record](#changing-an-accepted-record) _(Lines 100-107)_
   1. [Status, Ownership and Use in Review](#status-ownership-and-use-in-review) _(Lines 110-117)_
   1. [Proposal Versus Record](#proposal-versus-record) _(Lines 120-129)_
1. [Incremental Change](#incremental-change) _(Lines 132-134)_
   1. [Step Size and Feedback](#step-size-and-feedback) _(Lines 137-144)_
   1. [Expand, Migrate, Contract](#expand-migrate-contract) _(Lines 147-154)_
   1. [Replacement Versus Rewrite](#replacement-versus-rewrite) _(Lines 157-164)_
   1. [Mass Change and Migration Ownership](#mass-change-and-migration-ownership) _(Lines 167-174)_
   1. [Lifespan, Consumers and Cost of Change](#lifespan-consumers-and-cost-of-change) _(Lines 177-183)_
   1. [Conventions Applied Forward Only](#conventions-applied-forward-only) _(Lines 186-194)_
1. [Technical Debt and Refactoring](#technical-debt-and-refactoring) _(Lines 197-199)_
   1. [What Counts as Debt](#what-counts-as-debt) _(Lines 202-208)_
   1. [Taking Debt Versus Investing in Quality](#taking-debt-versus-investing-in-quality) _(Lines 211-218)_
   1. [Finding and Inventorying Debt](#finding-and-inventorying-debt) _(Lines 221-227)_
   1. [Refactoring Step Size](#refactoring-step-size) _(Lines 230-237)_
   1. [Timing and Responsibility of Repayment](#timing-and-responsibility-of-repayment) _(Lines 240-250)_
1. [Decommissioning](#decommissioning) _(Lines 253-255)_
   1. [Why Remove](#why-remove) _(Lines 258-265)_
   1. [Grounds to Retire](#grounds-to-retire) _(Lines 268-274)_
   1. [Announcing Retirement](#announcing-retirement) _(Lines 277-284)_
   1. [Support Window Before Removal](#support-window-before-removal) _(Lines 287-294)_
   1. [Advisory or Compulsory Deprecation](#advisory-or-compulsory-deprecation) _(Lines 297-303)_
   1. [Carrying Out the Retirement](#carrying-out-the-retirement) _(Lines 306-316)_
1. [Keeping Technologies Few](#keeping-technologies-few) _(Lines 319-321)_
   1. [Adding as Replacing](#adding-as-replacing) _(Lines 324-330)_
   1. [Standing Position per Technology](#standing-position-per-technology) _(Lines 333-339)_
   1. [How Firmly the Stack Is Held](#how-firmly-the-stack-is-held) _(Lines 342-348)_
   1. [One General-Purpose Store for Several Roles](#one-general-purpose-store-for-several-roles) _(Lines 351-356)_

---

## Decision Records
<!-- Lines 63-65 -->

A significant decision gets a short record stored beside the code, stating the forces, the alternatives, the decision and the costs it accepts. An accepted record is superseded, never rewritten. The reason: the motivation of past decisions is among the hardest things to recover, and its loss makes a team obey outdated decisions or reverse them blindly. Carries out [Evaluation Process and Admission Gate](ownership_stance_selection.md#evaluation-process-and-admission-gate), where the written reason for a selection is stored as a record. `EVOLUTION.DECISIONS`

### Content of a Record
<!-- Lines 68-75 -->

A record states the forces at play, the decision, the serious alternatives with why the rejected ones were rejected (dissent included), and the consequences including the costs it accepts, in one fixed structure shared by all records. A later reader can then tell why it was decided, what would have to change to revisit it, and whether new information justifies reopening. `EVOLUTION.DECISIONS.1`

- A record MUST state the decision and its reason.
- A record MUST state the alternatives rejected and the costs accepted.

Inferred: that naming the forces makes a change in them the trigger to revisit; one source states it and none tests it.

### Significance Threshold
<!-- Lines 78-87 -->

A decision gets its own record when it is architecturally significant (structure, non-functional requirements, dependencies, interfaces, construction techniques) and a later maintainer could not recover its reason from an existing policy or standard: several options were weighed, or no existing basis supplied the answer. `EVOLUTION.DECISIONS.2`

- A significant decision with no policy basis, or with options weighed, MUST have a record.
- A decision a recorded policy settles points to the policy.
- A workaround, an experiment or a policy-backed decision MUST NOT get a record of its own.
- A deliberate, temporary shortcut is recorded as a debt item ([Finding and Inventorying Debt](#finding-and-inventorying-debt)).

Scales without a second bar: with many contributors or a long life, more decisions meet the test, because what is obvious to the team today is not to a newcomer. Inferred: no source gives a numeric or structural threshold. Bounds which selections get a record, see [Finding, Profiling and Selecting](ownership_stance_selection.md#finding-profiling-and-selecting).

### Form and Storage
<!-- Lines 90-97 -->

A record is short (one or two pages), covers one decision, is numbered monotonically with no number reused, is written as prose to a future reader in lightweight text markup, and is stored in version control in the repository of the code it governs. So the record travels with the code, has history and is found by anyone who reads the code. `EVOLUTION.DECISIONS.3`

- Records MUST live in the repository of what they govern.
- A record number MUST NOT be reused.

Best instead when: a wiki is the source only where the records must be read and edited by people outside the repository, at the cost of drifting from the code. A wiki mirror for wider reach is fine; the repository stays the source.

### Changing an Accepted Record
<!-- Lines 100-107 -->

A changed decision is a new record that supersedes the old one, which stays in place marked superseded, so history is never wrong, only superseded. Only corrections that do not change the decision (a typo, a broken link) edit an accepted record. A document that describes the current state (how-to, reference) is living and is kept current by ownership and checks, see [Documentation Practice](transverse_documentation.md#documentation-practice). `EVOLUTION.DECISIONS.4`

- An accepted record MUST NOT be rewritten to change its decision.
- A superseded record MUST carry a link to its successor.

Best instead when: a mutable, dated document suits documents readers use as the current truth (how-to, reference), not decision records. Inferred: the assignment of the two models per document type.

### Status, Ownership and Use in Review
<!-- Lines 110-117 -->

Each record has a status (proposed, accepted, rejected, superseded, deprecated), a named owner accountable for its upkeep and a review before acceptance. During code and design review the accepted records are consulted; a change that violates one is linked to it and either conforms or arrives with a new record that supersedes it. `EVOLUTION.DECISIONS.5`

- Every record MUST have a status and a named owner.
- A change that contradicts an accepted record MUST cite it.

Consulted during the review described in [Change Flow](change_flow_integration_review.md#review). Inferred: consulting records in review rests on one source with no dissent found.

### Proposal Versus Record
<!-- Lines 120-129 -->

Where many stakeholders must be heard, the decision is prepared in a proposal written before it is made (drawbacks, alternatives, unresolved questions, a backward-compatibility section, a named decider), and the record keeps only the outcome and its reason, linking the proposal. Where few stakeholders are involved, the lightweight record alone is the whole practice. `EVOLUTION.DECISIONS.6`

- A proposal MUST name its decider.
- A decision made through a proposal MUST be linked to it from the record.

Best instead when: one document serving as both proposal and record is best where the proposal itself is the permanent versioned history and carries a final status, as in an open project with many contributors. Inferred: one source's synthesis of two projects; none measures either practice. The record keeps the content from [Content of a Record](#content-of-a-record).

---

## Incremental Change
<!-- Lines 132-134 -->

Change is made in steps that keep the system releasable and teach early, and every incompatible change runs as expand, migrate, contract, with the contract step part of the change. A system is replaced piece by piece behind its interface and rewritten only under stated conditions; a mass change has one accountable owner with capacity. Investment in changeability follows expected lifespan and consumer count, and a new convention applies forward only where many consumers depend on the surface. Carries out [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle) and [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible). `EVOLUTION.INCREMENTAL`

### Step Size and Feedback
<!-- Lines 137-144 -->

Change proceeds in steps that keep the system releasable at every step, using an interface that supports both versions or an abstraction with two suppliers, rather than a long-lived branch or one switch-over. Each step is released and its effect checked against the effect it was meant to have, because many presumed improvements do not move their metric. A wrong direction is found while it is cheap to reverse. `EVOLUTION.INCREMENTAL.1`

- Every step MUST leave the system releasable.
- A step's intended effect MUST be stated and checked after release.

Rests on [Version Control and Integration](change_flow_integration_review.md#version-control-and-integration) and keeps [Rollback](change_flow_delivery.md#rollback) possible. Carries [Speculative Building and Probable Use](ownership_stance_selection.md#speculative-building-and-probable-use) to the unit of change: build to learn, not for presumed needs; analysis proportional to the cost of being wrong stays. Best instead when: a single switch-over, see [Expand, Migrate, Contract](#expand-migrate-contract).

### Expand, Migrate, Contract
<!-- Lines 147-154 -->

An incompatible interface or schema change runs as expand, migrate, contract: first support old and new together (for stored data, in the deploy order of [Order and Compatibility With Running Code](change_flow_data_and_measure.md#order-and-compatibility-with-running-code)), then move consumers, then remove the old form. The removal step belongs to the change, because supporting two versions is a recurring cost that ends only at removal. Rollback stays possible during the move and the old form does not become permanent. `EVOLUTION.INCREMENTAL.2`

- The plan of an incompatible change MUST name its removal step and owner (owner and capacity: [Why Remove](#why-remove)).
- An unfinished migration is a debt item ([What Counts as Debt](#what-counts-as-debt)).

What counts as an incompatible change is decided in [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible); expanding first is the reversibility that [Rollback](change_flow_delivery.md#rollback) requires. Best instead when: a single coordinated switch-over, where one release unit contains every consumer and a short outage or lock is acceptable, at the price of no rollback during the switch.

### Replacement Versus Rewrite
<!-- Lines 157-164 -->

A system is replaced incrementally while it keeps running, at seams and behind its existing interface (the strangler pattern). A full rewrite is justified only when the old platform is obsolete, the old system runs in parallel until the new one is proven, and the migration is slow and verified. A big-bang cut-over is not a practice. Users keep a working system, the hidden knowledge in the old behaviour is preserved, and the old system is removed only once the new one is shown equivalent. `EVOLUTION.INCREMENTAL.3`

- A replacement MUST keep the old system serving until the new one is verified against the old behaviour.
- A full rewrite MUST carry a recorded reason that the platform is obsolete.

Open: whether any position wins in general is not settled; the conditions for a full rewrite are inferred, and the rewrite rule of thumb found in one source is unverified and not adopted. Best instead when: never rewrite, refactor in place, where the system ships, its behaviour is poorly specified and no replacement need exists; a big-bang rewrite, inferred, only where the system is small, every consumer sits in one release unit, equivalence is verified and a short outage is acceptable. A replaced system is retired through [Decommissioning](#decommissioning); the choice weighs the cost of carrying one's own code, see [Necessity and Default Stance](ownership_stance_selection.md#necessity-and-default-stance).

### Mass Change and Migration Ownership
<!-- Lines 167-174 -->

A mechanical change across a large codebase is generated with tools, split into independently testable and reviewable shards, with the old pattern blocked from reappearing; small single-owner code can change in one step. A migration across many consumers has one accountable owner, usually the party that wants the change, and a finish condition. The change completes and consumers carry little of the load. `EVOLUTION.INCREMENTAL.4`

- A migration MUST have a named owner and a finish condition.
- The old pattern MUST be blocked by a check once the migration is done (owner and capacity: [Why Remove](#why-remove)).

Shards stay reviewable and integrable, see [Version Control and Integration](change_flow_integration_review.md#version-control-and-integration). Best instead when: consumers migrate on their own where the replacement is transformatively better; a central owner with capacity is not needed where consumers are few and reachable; one atomic change suits small single-owner code. Inferred: the boundary between the sharded, owned form and a single step.

### Lifespan, Consumers and Cost of Change
<!-- Lines 177-183 -->

The life of a system is a series of changes it must absorb, so the investment in changeability is set by its expected lifespan. The cost of change and removal grows with the number of consumers, because they depend on observable behaviour; owners of shared infrastructure can change it without tracking each consumer only through reliance-capturing tests. `EVOLUTION.INCREMENTAL.5`

- The expected lifespan and the consumers of a shared interface MUST be stated where the investment is decided.

The mechanism is [Contract Tests](assurance_interfaces_data.md#contract-tests); reliance on observable behaviour is reasoned in [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible). Same stance as [Speculative Building and Probable Use](ownership_stance_selection.md#speculative-building-and-probable-use): investment follows probable use. Lifespan and consumer count also bound what is selected, see [Finding, Profiling and Selecting](ownership_stance_selection.md#finding-profiling-and-selecting). Best instead when: no fixed investment suits either a throwaway or a decades-long system.

### Conventions Applied Forward Only
<!-- Lines 186-194 -->

A new convention applies to new objects, and existing objects are not renamed where the surface has many consumers. A deprecated item is marked where its consumers and their tools see it, in machine-readable metadata of the item, and in its name only where renaming it breaks no consumer; it stays, with documented deprecation and its relationships, until a later planned removal. `EVOLUTION.INCREMENTAL.6`

- A deprecated item MUST be marked where its consumers and their tools see it, and remain until its planned removal.

The mark follows [Announcing Retirement](#announcing-retirement). Best instead when: consumers are few and reachable and the rename is mechanical and verified by tests, where one coordinated rename avoids a permanently split convention. Inferred: this few-consumer exception; no source states it.

---

## Technical Debt and Refactoring
<!-- Lines 197-199 -->

Debt is anything that makes future change more costly, wider than code quality, and it is inventoried. Speed is bought with debt only knowingly, for short-lived or exploratory work; debt is made visible mainly by engineers' reports, with tools as support. Refactoring runs in small behaviour-preserving steps, and repayment is timed by where code changes, with explicit capacity for debt no change touches. Carries out the liability stance of [Necessity and Default Stance](ownership_stance_selection.md#necessity-and-default-stance). `EVOLUTION.DEBT`

### What Counts as Debt
<!-- Lines 202-208 -->

Debt is any design or implementation choice, or unfinished piece of work, that makes future change more costly or impossible, whether taken knowingly or not. The inventory is wider than code quality: it includes design trade-offs invisible to code metrics, unfinished migrations, missing or stale documentation, missing tests, dead code, out-of-date dependencies, concentrated team expertise and a weak release process. Debt that hurts change is weighed even when no tool shows it. `EVOLUTION.DEBT.1`

- An unfinished migration and an out-of-date dependency MUST be counted as debt items when they raise the cost of change.

Out-of-date dependencies are found through the inventory and end-of-life watching of [Inventory, Watching and End of Life](ownership_lifecycle_containment.md#inventory-watching-and-end-of-life). Best instead when: debt limited to code structure is enough only where the aim is to talk about code structure; it omits debt that metrics cannot see. Inferred: the full list of items rests on a secondary source.

### Taking Debt Versus Investing in Quality
<!-- Lines 211-218 -->

Internal quality is invested in from the start for anything that will be changed, on the argument that good design pays back within weeks and does not trade against speed beyond the smallest scope. Debt is taken deliberately only for a short-lived or exploratory deliverable, knowingly, recorded, and then repaid as [Timing and Responsibility of Repayment](#timing-and-responsibility-of-repayment) sets, or dropped with the deliverable. The system is kept simple with minimal, modular interfaces and small releases; debt is a recorded choice with a repayment, not an accident. `EVOLUTION.DEBT.2`

- Deliberate debt MUST be recorded as an inventory item ([Finding and Inventorying Debt](#finding-and-inventorying-debt)), repaid as set there, or dropped with the deliverable.
- A deliverable that outlives its stated short life MUST be re-judged as a lasting one.

Open: the payoff point of quality over speed is unproven and the claim is contested; the decision is conditional on the lifetime of the work, not universal. Best instead when: a little debt for speed, repaid promptly, suits a short-lived or exploratory deliverable. Small releases are in [Step Size and Feedback](#step-size-and-feedback), deleting code in [Why Remove](#why-remove). Carries out [Necessity and Default Stance](ownership_stance_selection.md#necessity-and-default-stance).

### Finding and Inventorying Debt
<!-- Lines 221-227 -->

Debt is inventoried as items, each with cause, consequence, affected artefact and impact, and managed by recognising, analysing, monitoring and measuring. Because no validated automatic metric predicts where debt hinders, a periodic survey of engineers is the main signal of where it hurts, with tools (smells, coupling, dependency analysis) and measurable maintainability signals as trend tracking. The inventory is one list kept where the team plans its work, so repayment competes with features in the same plan. A code marker carries only the item's id as a pointer, and a decision record holds a debt item only where the debt came from a recorded decision. `EVOLUTION.DEBT.3`

- Every deliberate debt item and every unfinished migration MUST appear in the inventory.

Best instead when: where a validated metric exists for a kind of debt, it replaces the survey for that kind; tool-detected smells are the supplement, not the primary signal, since they miss design debt. The length of the dependency upgrade cycle is the debt-side view of [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle). Inferred: survey primacy, item fields and inventory placement; tool limits are grounded.

### Refactoring Step Size
<!-- Lines 230-237 -->

Refactoring proceeds only in small steps that preserve behaviour, with the checks green after each, so the system is never left broken for more than minutes of work. Behaviour not pinned by tests is pinned first, as [Tests Driven by Change](assurance_behaviour.md#tests-driven-by-change) requires. A larger rearrangement is restructuring and runs as an incremental change with its own controls. A refactoring can be stopped or reverted at any step and behaviour never changes unnoticed. `EVOLUTION.DEBT.4`

- Each refactoring step MUST leave the checks green.
- A refactoring MUST NOT change observable behaviour.

Relies on the check that detects a behaviour change, held in [What the Suite Must Promise](assurance_behaviour.md#what-the-suite-must-promise). Grounded.

### Timing and Responsibility of Repayment
<!-- Lines 240-250 -->

Maintainability debt is repaid where code is changed, because interest accrues only there: tidy before a change when tidying plus the change costs less than the change alone, tidy after, later or never otherwise, and never in code that will not change again. Refactoring is opportunistic and ordinary work where tests are strong and ownership is shared; structural debt that spans teams, which no one touches in passing, gets explicit capacity or a programme with an owner. A tidy lands as its own change, as decided in [Unit of Review and Response Speed](change_flow_integration_review.md#unit-of-review-and-response-speed). `EVOLUTION.DEBT.5`

- Maintainability debt in code that will not change again MUST NOT be repaid.
- Debt that carries risk (code left on production, vulnerable or end-of-life dependencies) MUST follow [Why Remove](#why-remove) and the rules of [Updating](ownership_lifecycle_containment.md#updating) and [Inventory, Watching and End of Life](ownership_lifecycle_containment.md#inventory-watching-and-end-of-life), not this rule.
- Cross-team debt MUST have a named owner and capacity, as a mass migration does ([Mass Change and Migration Ownership](#mass-change-and-migration-ownership)).

Best instead when: opportunistic repayment alone suits strong tests and shared ownership; a standing debt sprint for all debt is argued by no source and fits only as the explicit capacity for structural debt. Inferred: mostly single-author sources, and the cost inequality for tidy-first is unproven.

---

## Decommissioning
<!-- Lines 253-255 -->

Removal is planned engineering work with an owner and a budget. A retirement is decided on stated grounds and recorded, announced in two stages (deprecation, then sunset) with machine-readable, actionable warnings, and given a published support window where consumers are many. It has a deadline unless the replacement sells itself, and is executed by verifying use, restricting reversibly, then removing everything attached. Carries out [Necessity and Default Stance](ownership_stance_selection.md#necessity-and-default-stance), [API Stability and Deprecation](ownership_services_licence.md#api-stability-and-deprecation) (the consumer side) and [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible) (the provider side). `EVOLUTION.DECOMMISSION`

### Why Remove
<!-- Lines 258-265 -->

Code is a liability whose value lies in the functionality it provides, so the aim is more functionality per unit of code, and obsolete code is removed. Removal and migration work is ordinary engineering work with a named owner and capacity in the plan, planned alongside features and not left over after them, because without them it stalls. Code no longer meant to be used is not left on a production system, so it cannot be activated by accident. `EVOLUTION.DECOMMISSION.1`

- Removal and migration work MUST have a named owner and capacity in the plan.
- Code not intended to run on production MUST be removed from it.

This node holds the owner-and-capacity principle; the other sections of this file point here. Best instead when: dormant code is kept only where a recorded reuse is planned, with an owner. Inferred: removal as one rule with owner and budget (no source states it as one rule).

### Grounds to Retire
<!-- Lines 268-274 -->

A retirement is decided on stated grounds: a replacement of comparable or better function exists, the upkeep cost exceeds the value, the technology is out of date, the strategy has changed, or use is low. It is recorded as a decision record that supersedes the adoption record ([Changing an Accepted Record](#changing-an-accepted-record), [Form and Storage](#form-and-storage)). So a retirement has a reason that can be checked and that a later reader finds. `EVOLUTION.DECOMMISSION.2`

- A retirement MUST name its ground and be recorded.

Retirement by neglect or by the departure of the maintainer states no ground and is best never, since consumers cannot plan.

### Announcing Retirement
<!-- Lines 277-284 -->

A team retiring an interface or form it offers announces it in two stages with distinct signals: deprecation (no longer recommended, still working) and sunset (stops at a stated time). Warnings are actionable and relevant, since excess causes alert fatigue, and are exposed in machine-readable form so that remaining users are found. Every consumer can learn the state and the date by machine, and the owner can see who still uses the form. `EVOLUTION.DECOMMISSION.3`

- The sunset MUST NOT be earlier than the deprecation.
- A deprecation MUST be visible to a machine as well as a reader.

Realizes the provider-side policy of [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible); the consumer side reads and routes these signals as set in [API Stability and Deprecation](ownership_services_licence.md#api-stability-and-deprecation). Best instead when: a single "removed in a future release" notice suits an internal item with one reachable consumer, who is told directly.

### Support Window Before Removal
<!-- Lines 287-294 -->

Where consumers are many or external, a support policy is published by stability tier with fixed minimum windows: a stable interface is deprecated but not removed within a major version, a pre-release one has a fixed period, an experimental one may go at any release. Where consumers are few and known, the window is set case by case with them. Consumers can plan from a published rule and maintainers do not carry old forms without limit. `EVOLUTION.DECOMMISSION.4`

- A published window MUST state, per tier, how long a deprecated form stays.
- A form MUST NOT be removed before its stated window.

The indefinitely compatible, date-pinned surface has no window and is held in [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible); consumers pin their version against the promise, see [API Stability and Deprecation](ownership_services_licence.md#api-stability-and-deprecation). Best instead when: a case-by-case window suits few known consumers, where a conversation is faster than a policy. Open: no general durations are given; the concrete figures of one project are not adopted, so each team sets its own per tier.

### Advisory or Compulsory Deprecation
<!-- Lines 297-303 -->

When the old form is to be removed, the retirement is compulsory with a firm deadline, so the deprecation stage ends in a sunset ([Announcing Retirement](#announcing-retirement)). Advisory deprecation without a deadline is right only when the replacement sells itself or the old form is cheap to carry and no removal is intended. A retirement that is meant to happen does happen, at a known load on consumers. `EVOLUTION.DECOMMISSION.5`

- A compulsory retirement MUST have a firm deadline (owner and capacity: [Why Remove](#why-remove)).

A compulsory retirement is staffed through the owner and finish condition of [Mass Change and Migration Ownership](#mass-change-and-migration-ownership), which answers the risk of an unfunded mandate. Best instead when: advisory deprecation suits a replacement that is transformatively better.

### Carrying Out the Retirement
<!-- Lines 306-316 -->

Before switching a system off, who or what still uses it is verified, and access is restricted reversibly for a period to flush out remaining users. Restorable backups and recorded metadata are kept per the retention rules, neither shorter nor longer, and only then is it removed. Removal is the owner's primary objective, with measurable intermediate milestones, and everything attached is removed: licences, attached storage, DNS entries, domain membership, and entries in configuration, monitoring, automation and security tooling, checked against compliance requirements. Nothing used is cut off, nothing attached is left behind, and the retirement can be undone until it is final. `EVOLUTION.DECOMMISSION.6`

- Usage MUST be verified before switch-off.
- A retirement MUST list and remove its attachments.
- Backups kept after retirement MUST follow the retention rules, neither shorter nor longer (owner and capacity: [Why Remove](#why-remove)).

Retention is held in [Backup Scope and Design](operation_recovery_and_feedback.md#backup-scope-and-design) and [Retention Periods](transverse_privacy.md#retention-periods); erased data in a backup is put beyond use as [Erasure and Deletion Mechanism](transverse_privacy.md#erasure-and-deletion-mechanism) requires; backups stay restorable under [Data Integrity Under Change](assurance_interfaces_data.md#data-integrity-under-change). Metadata and data of the retired system are handled as a [data change](change_flow_data_and_measure.md#data-and-schema-change). Best instead when: immediate removal suits only something provably unused; an abrupt switch-off of a system with possible users is best never.

---

## Keeping Technologies Few
<!-- Lines 319-321 -->

A technology is added as a replacement, with the retirement of what it replaces planned and owned. The team keeps a shared register of the technologies in use, each with a position and a decision trail. How firmly the set is held follows how much platform and on-call is shared, and one mature general-purpose store serves several roles until a stated need exceeds it. Carries out [Finding, Profiling and Selecting](ownership_stance_selection.md#finding-profiling-and-selecting) over the whole estate and [Necessity and Default Stance](ownership_stance_selection.md#necessity-and-default-stance). `EVOLUTION.TECHNOLOGY`

### Adding as Replacing
<!-- Lines 324-330 -->

The number of different tools solving the same problem is held down: a new technology is introduced as a replacement, with the retirement of the older one planned and owned, because the long-term cost of keeping an extra system reliable exceeds the convenience of building with it. A few tools that cover the whole domain are preferred, so shared platform work benefits all. `EVOLUTION.TECHNOLOGY.1`

- Introducing a technology MUST record what it replaces, or why it replaces nothing, and the retirement owner.

Applies, to the whole estate, the entry rule of [Fit, Maturity and Novelty](ownership_stance_selection.md#fit-maturity-and-novelty); that rule holds the entry test, this node the replacement commitment. The replaced technology is retired as in [Grounds to Retire](#grounds-to-retire). How firmly this holds follows [How Firmly the Stack Is Held](#how-firmly-the-stack-is-held). Best instead when: adding alongside suits a problem the present technologies cannot solve, documented as the selection rule requires.

### Standing Position per Technology
<!-- Lines 333-339 -->

The team keeps a shared register of the technologies in use, each with a position (standard, being evaluated, held for retirement) and a decision trail linking its record ([Form and Storage](#form-and-storage)). Where the organisation has capacity for experiments, the four-ring vocabulary (adopt, trial, assess, hold) is used; a small or operations-heavy team keeps the register without the evaluation rings. The register holds technologies and the team's position on each. It is neither the sanctioned list of admitted dependencies (the gate, [Evaluation Process and Admission Gate](ownership_stance_selection.md#evaluation-process-and-admission-gate)) nor the inventory of what is deployed ([Inventory, Watching and End of Life](ownership_lifecycle_containment.md#inventory-watching-and-end-of-life)): position, admission and presence are three facts, each held once. `EVOLUTION.TECHNOLOGY.2`

- Each technology in use MUST have a position and a link to its record.

Best instead when: standing rings suit only a team with capacity for experiments and tolerance for churn; an implicit, unrecorded stance is best never, since newcomers cannot tell what is standard. Inferred: the decision trail; the register itself is grounded.

### How Firmly the Stack Is Held
<!-- Lines 342-348 -->

The set of technologies is held as firmly as the cost of a departure is shared. Wherever a platform or on-call is shared, a supported default set is kept. A departure whose whole operating cost stays with the team that chose it is permitted and unsupported (paved path); a departure whose cost would land on the shared platform or on-call needs a recorded decision naming who carries it (mandate). Where components run independently and nothing is shared, each is chosen by fit within the default of the selection rule. The cost of an extra technology is carried by whoever chooses it. `EVOLUTION.TECHNOLOGY.3`

- A departure from the default set whose operating cost would land on the shared platform or on-call MUST have a recorded decision naming who carries it.

The version choice for each dependency is in [Updating](ownership_lifecycle_containment.md#updating) and one version of each shared component in [Version Control and Integration](change_flow_integration_review.md#version-control-and-integration). Best instead when: a mandated small set for every case, or free polyglot choice per component, applies only where that cost allocation holds. Inferred: the claim is contested across sources.

### One General-Purpose Store for Several Roles
<!-- Lines 351-356 -->

One mature general-purpose data store is preferred for queue, cache, search and documents while it meets the need now with headroom. A specialised system is added when a stated requirement (very low latency cache, large-scale search relevance, scale) exceeds what the store delivers, shown by measurement or by a documented limit of the store, not by the team's expectation. There are fewer systems to operate, and each added system has a measured reason. `EVOLUTION.TECHNOLOGY.4`

- A specialised store MUST be added only with the requirement it meets and the measurement or documented limit showing the general store falls short.

Open: contested. The rule is inferred; it rests on sources from one project or with commercial interest, the store's limits were not verified from primary sources, and no later review settled it. Default applied: one general-purpose store until a measured limit shows otherwise. Best instead when: a specialised system from the start suits a requirement known at the start to exceed the general store (a sub-millisecond cache, large-scale search). A case of [Adding as Replacing](#adding-as-replacing) and of [Speculative Building and Probable Use](ownership_stance_selection.md#speculative-building-and-probable-use); passes the entry test of [Fit, Maturity and Novelty](ownership_stance_selection.md#fit-maturity-and-novelty).
