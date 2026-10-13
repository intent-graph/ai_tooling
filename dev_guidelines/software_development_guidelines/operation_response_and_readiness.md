# Operation: Response and Readiness

## Table of Contents

1. [Incidents](#incidents) _(Lines 28-35)_
   1. [Declaring and Running an Incident](#declaring-and-running-an-incident) _(Lines 38-55)_
   1. [Learning From Incidents](#learning-from-incidents) _(Lines 58-75)_
   1. [On-Call and Toil Load](#on-call-and-toil-load) _(Lines 78-94)_
1. [Capacity](#capacity) _(Lines 97-103)_
   1. [Planning Method](#planning-method) _(Lines 106-120)_
   1. [Headroom and Overload](#headroom-and-overload) _(Lines 123-136)_
   1. [Storage Health](#storage-health) _(Lines 139-148)_
1. [Operational Readiness](#operational-readiness) _(Lines 151-156)_
   1. [Launch Gate and Checklist](#launch-gate-and-checklist) _(Lines 159-171)_
   1. [Who Performs the Review](#who-performs-the-review) _(Lines 174-185)_
   1. [Keeping the Review Current](#keeping-the-review-current) _(Lines 188-198)_
1. [Runbooks and Playbooks](#runbooks-and-playbooks) _(Lines 201-205)_
   1. [Form, Ownership and Validation](#form-ownership-and-validation) _(Lines 208-222)_
   1. [Automation](#automation) _(Lines 225-235)_


---

Part of [Operation](operation.md). Incident handling, capacity planning, the launch gate, and owned procedures.

## Incidents
<!-- Lines 28-35 -->

Incidents are declared on written conditions, run by named roles and learned from by blameless
review with tracked actions; the human cost of operating is bounded and measured. An incident is
handled at low cost, repeats less, and the people handling it can sustain it. Incident learning
carries out the corrective actions that recovery exercises demand
([Exercising Recovery](assurance_performance_availability.md#exercising-recovery)), and incident defects change the process
([Closing the Loop on Findings](assurance_docs_security.md#closing-the-loop-on-findings)). `OPERATION.INCIDENTS`

### Declaring and Running an Incident
<!-- Lines 38-55 -->

Declare on clear written conditions (a second team is needed, the problem is customer-visible,
it is unresolved after an hour of focused analysis) and make declaring cheap. A major incident
runs with named roles (commander, operations, communications, planning or scribe) and a live
incident document kept by the commander; system changes are made only by the operations lead and
the team they direct. Severity levels and the response each gets are defined beforehand, rehearsed
until routine, and command is handed over explicitly. Playbooks serve investigation here
([Form, Ownership and Validation](#form-ownership-and-validation)).

- MUST write the declaration conditions.
- MUST name roles and who may change the system, forbidding changes from anyone else.
- MUST rehearse the incident process.

Best instead when: in a tiny team, cut the process cost by scaling the response (one person holds
several roles, a shorter incident document), not by raising the declaration bar. A high bar, or
declaring by individual judgment in the moment, is best never. Open: the position favouring a high
bar is unsourced; "declaring should be cheap" is inferred. `OPERATION.INCIDENTS.1`

### Learning From Incidents
<!-- Lines 58-75 -->

Write a blameless postmortem for every significant incident, whether or not it paged, on written
triggers: user-visible downtime, data loss, manual intervention, slow resolution, monitoring
failure, and the budget consumption level of the budget policy
([Error Budget as Trade Mechanism](operation_objectives_and_signals.md#error-budget-as-trade-mechanism)). Every action item has an
owner, a priority and a tracker entry, is measurable and preventative, and is published within
days; closeout is checked and rewarded. Tie incident response to the organisation's risk
management so lessons reach safeguards and detection as soon as identified
([Detection and Escalation](transverse_security.md#detection-and-escalation)).

- MUST set written postmortem triggers.
- MUST track every action item with an owner.
- MUST feed findings into detection and safeguards.

Best never: postmortems only for paged incidents, postmortems without tracked actions, or
blame-based review. Open: the risk-management integration is grounded at abstract level only.
`OPERATION.INCIDENTS.2`

### On-Call and Toil Load
<!-- Lines 78-94 -->

Bound the human cost of operating by stated, measured limits kept under review: operational work,
on-call time, incidents per shift and the alert-to-incident ratio. Size the rotation to meet them,
so each engineer is on call often enough to stay familiar with production. The limit on the
alert-to-incident ratio caps how many pages the rules of [Paging Criterion and Rule Hygiene](operation_objectives_and_signals.md#paging-criterion-and-rule-hygiene)
may produce.

- For a dedicated rotation the limits default to one model's figures: operational work at most half
  of an engineer's time, on-call about a quarter of time, about two incidents per twelve-hour shift,
  alert-to-incident ratio near one to one.
- Where developers own operations in a small team, the team sets and records its own limits with the same outcome.
- MUST state the load limits and measure against them.

Best instead when: the numbers as universal thresholds fit only dedicated rotations; for a small
team the principle is a stated, measured limit (inferred). No stated limit is best never.
`OPERATION.INCIDENTS.3`

## Capacity
<!-- Lines 97-103 -->

Capacity is planned in resources before predictable change, headroom is decided explicitly against
a measured breaking point, and the data store is kept healthy. The system does not run out of
resources unannounced. Capacity measurements supply the signal that sets the growth horizon
([Growth Horizon](construction.md#growth-horizon)), and capacity is added by adding processes
([Process Lifecycle](construction.md#process-lifecycle)). `OPERATION.CAPACITY`

### Planning Method
<!-- Lines 106-120 -->

Plan capacity before any predicted change in usage (design, launch, campaign, seasonal peak,
feature release) and periodically: from history for existing workloads, from pilots, expert
judgment and external data for new ones. Model directly in resources (CPU, memory, bandwidth,
storage), not requests per second; derive the resource proposal from requirements and designs,
iterated through scaling and failure domains.

- Many services and frequent change: hold declared requirements from which allocations are computed.
- Small team: a spreadsheet or dashboard forecast suffices.
- MUST plan before predicted change; MUST express capacity in resources.

Best instead when: request-rate models fit only where cost per request is uniform (inferred);
declared requirements are overhead for a few services; spreadsheets are brittle across many
fast-changing services. `OPERATION.CAPACITY.1`

### Headroom and Overload
<!-- Lines 123-136 -->

Decide headroom explicitly from the tested breaking point and its early-warning metrics, counting
scaling lag and the capacity of the failover environment. Pair planning with load tests and
defined overload behaviour, because planning cannot protect against infrastructure loss,
partitions or unexpected spikes (overload behaviour carries out
[Tolerating a Degraded Dependency](assurance_performance_availability.md#tolerating-a-degraded-dependency)).

- Pre-provision for peak and failover where peaks are hard, scale-up is slow or the system is critical.
- Autoscale within tested limits where load varies and scale-up is fast.
- MUST derive headroom from a tested breaking point; MUST count scaling lag and failover capacity; MUST test autoscale limits.

Best never: autoscaling with untested limits, or no stated headroom. Open: no source fixes a
numeric headroom. `OPERATION.CAPACITY.2`

### Storage Health
<!-- Lines 139-148 -->

Keep storage healthy by routine: find indexes never used from the engine's usage counters and
drop them, watch index and table bloat, and rebuild without blocking writes. The store does not
degrade through dead indexes and bloat.

- MUST drop unused indexes only on usage evidence covering a full workload cycle (an index backing a constraint is kept).
- MUST rebuild without blocking writes.

Keeping every index "just in case", or dropping on a short window, is best never. `OPERATION.CAPACITY.3`

## Operational Readiness
<!-- Lines 151-156 -->

A workload is launched only after a readiness review that shows its team can operate it, and the
review is kept true over the workload's life, so what launches is operable. The review checks
failure modes and recovery proof, which carries out the guarantees of
[Availability and Recovery](assurance_performance_availability.md#availability-and-recovery). `OPERATION.READINESS`

### Launch Gate and Checklist
<!-- Lines 159-171 -->

Gate a launch on a readiness check covering architecture, capacity, failure modes, monitoring,
emergency response, change management and rollout; a workload whose team cannot operate it is not
launched. Build the checklist from the team's own incidents and past launch failures, with
concrete, achievable items; start short (about thirty) and tier by risk, with a fast path for
low-risk launches. The check relies on [Capacity](#capacity), reads failure modes against
[Recovery Objectives](operation_recovery_and_feedback.md#recovery-objectives), and sits at launch in [Release](change_flow_delivery.md#release).

- MUST block launch of a workload whose team cannot operate it.
- MUST cover monitoring, failure modes, emergency response and rollout.

Best never: a generic long checklist as a start, or one bar for all launches. `OPERATION.READINESS.1`

### Who Performs the Review
<!-- Lines 174-185 -->

The review must be a trustworthy judgment that the workload is operable.

- Critical services, and wherever ownership passes to a separate operations team: an independent reviewer examines the service and negotiates improvements, with capacity to review every service that needs it.
- Many teams launching services, mature and sponsored culture: the owning team certifies against a self-service checklist.
- MUST name who can block a launch.

Best instead when: independent review of every launch fits only when reviewer capacity matches
service count (otherwise it becomes the bottleneck). Self-certification is best never for critical
services or an immature culture. Open: no source compares the two forms; the criticality condition
rests on the cost-of-error argument (inferred). `OPERATION.READINESS.2`

### Keeping the Review Current
<!-- Lines 188-198 -->

Re-run the review over the workload's life, a subset on a regular cadence, to catch drift and add
lessons. Findings that repeat are converted into automated guardrails and defaults so they stop
depending on the review.

- MUST re-run a subset of the review on a cadence.
- MUST convert repeated findings into guardrails.

A one-off launch review is best never for a changing workload. Open: no source fixes the cadence.
`OPERATION.READINESS.3`

## Runbooks and Playbooks
<!-- Lines 201-205 -->

Operating procedures exist as owned, validated documents, split by purpose, and move toward
automation, so a responder who did not write a procedure can follow it under stress.
`OPERATION.RUNBOOKS`

### Form, Ownership and Validation
<!-- Lines 208-222 -->

Each runbook is a versioned, step-by-step document with an owner, required tools and permissions,
error handling and escalation, validated by another team member running it and updated through
change management (it applies the owner, date and review rule of
[Ownership, Freshness and Single Source](assurance_docs_security.md#ownership-freshness-and-single-source) and adds validation by
another person). Keep playbooks (investigate and scope an incident) separate from runbooks
(mitigate a known cause); link the playbook from the alert; give each an escalation path for an
unknown cause.

- MUST have another person run each runbook before it is relied on.
- MUST link the playbook from its alert.

Best never: an unvalidated runbook (the author's own read proves nothing), or one document for
both investigation and mitigation. `OPERATION.RUNBOOKS.1`

### Automation
<!-- Lines 225-235 -->

Procedures mature from text toward scripts and then automatic remediation, starting with short,
frequently used, low-risk ones. A script is validated and exercised like any procedure before it
runs unattended. This carries out the rule of [Paging Criterion and Rule Hygiene](operation_objectives_and_signals.md#paging-criterion-and-rule-hygiene):
a page answerable by a mechanical response is automated.

- MUST start automation with short, frequent, low-risk procedures.

Best never: automating a long, rare or high-risk procedure first, or never automating frequent
routine work. Open: one vendor source; the cost and risk of automating a wrong runbook are
unexamined. `OPERATION.RUNBOOKS.2`
