# Operation: Recovery and Feedback

## Table of Contents

1. [Backup, Restore and Disaster Recovery](#backup-restore-and-disaster-recovery) _(Lines 21-28)_
   1. [Recovery Objectives](#recovery-objectives) _(Lines 31-46)_
   1. [Backup Scope and Design](#backup-scope-and-design) _(Lines 49-69)_
   1. [Backup Protection and Isolation](#backup-protection-and-isolation) _(Lines 72-93)_
   1. [Recovery Strategy, Failover and Failback](#recovery-strategy-failover-and-failback) _(Lines 96-113)_
   1. [Recoverability of Recovery Itself](#recoverability-of-recovery-itself) _(Lines 116-136)_
   1. [Ownership, Monitoring, Roles and Plan Upkeep](#ownership-monitoring-roles-and-plan-upkeep) _(Lines 139-158)_
1. [Feedback into Development](#feedback-into-development) _(Lines 161-170)_


---

Part of [Operation](operation.md). Recovery designed from objectives, and delivery measures fed back from production.

## Backup, Restore and Disaster Recovery
<!-- Lines 21-28 -->

Recovery is designed backward from stated recovery objectives per workload: backups that the
failure or attacker threatening production cannot take, a strategy and failover rule chosen by
tier against cost, a recovery that does not depend on what failed, and an owner and plan kept
current. The system can be restored within its objectives, and the proof that it can
([Availability and Recovery](assurance_performance_availability.md#availability-and-recovery)) has stated criteria to test
against. `OPERATION.RECOVERY`

### Recovery Objectives
<!-- Lines 31-46 -->

Set a recovery time objective and a recovery point objective per workload or data class, from the
impact of downtime and data loss, grouped in criticality tiers; never arbitrary, zero or stricter
than needed, and compatible with those of dependencies and dependants. Define disaster, major
disruption and small incident by impact, with thresholds built into monitoring. Data recovery (how
much may be lost, whether intact) and service recovery (how fast it runs) are separate objectives.
Set like a reliability objective ([Objective Level and Starting Point](operation_objectives_and_signals.md#objective-level-and-starting-point));
these are the criteria the restore proof is fixed against ([Proving Restore](assurance_performance_availability.md#proving-restore)).

- MUST set both objectives per workload or data class, derived from impact.
- MUST state data recovery and service recovery separately.

Best never: one organisation-wide objective, an objective of zero, or objectives set by the
mechanism available instead of impact. Open: the dependency-compatibility rule rests on one
source; the two-objective framing is inferred. `OPERATION.RECOVERY.1`

### Backup Scope and Design
<!-- Lines 49-69 -->

Replication and redundancy are availability measures, not recovery: keep versioned or
point-in-time copies, because replication propagates damage. Classify all data sources and back up
what cannot be recreated; a reproducible source instead has a tested reproduction path meeting the
recovery time objective. Back up everything needed to rebuild the service, and the cryptographic
keys, on storage independent of the encrypted data. Frequency follows the recovery point, locality
the recovery time; retention is tiered by age and bounded by undetected-corruption windows
([Checking Old Against New and Rolling Out Checks](assurance_interfaces_data.md#checking-old-against-new-and-rolling-out-checks)),
legal retention and privacy periods ([Retention Periods](transverse_privacy.md#retention-periods),
[Erasure and Deletion Mechanism](transverse_privacy.md#erasure-and-deletion-mechanism)). Back up platform
state that is the source of truth, and test its restore.

- MUST keep point-in-time or versioned copies.
- MUST test the reproduction path where backup is skipped.
- MUST back up keys separately from the data they protect.
- MUST back up platform state where it is the source of truth.

Best never: replication as backup, or skipping backup of reproducible data without a tested path
that meets the objective. A logical dump alone cannot provide point-in-time recovery.
`OPERATION.RECOVERY.2`

### Backup Protection and Isolation
<!-- Lines 72-93 -->

Keep at least one backup copy outside the failure and attack domain of production. An attacker
already holding production credentials is in the threat model, so a backup reachable with
production credentials is not independent. Choose the isolation form by the stated threat and the
restore-speed requirement. Encrypt backups with restricted rights. No single credential or person
can delete every copy or shorten its retention, which carries out
[Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access).
Erasure inside backups, including an immutable copy, is governed by
[Erasure and Deletion Mechanism](transverse_privacy.md#erasure-and-deletion-mechanism).

- Isolation forms: separate account, region or provider; platform-enforced immutable retention; offline copy.
- Example of platform-enforced immutable retention: object-storage compliance modes (one that even the account owner cannot override, one that privileged users can).
- MUST keep one copy independent of production credentials; MUST state the threat model and who can delete backups or shorten retention.
- MUST encrypt backups.
- MUST ensure no single credential or person can delete every copy or shorten retention (dual authorisation, or immutable retention).

Best instead when: offline-only fits a destructive adversary when restore time allows; immutability
fits where the platform account is protected; 3-2-1 alone fits hardware, site or operator error
(not destructive attack); a separate provider for every system fits when vendor-level loss is in the
threat model. A copy reachable with production credentials counted as independent is best never.
Open: the 3-2-1-1-0 extension is vendor-originated. `OPERATION.RECOVERY.3`

### Recovery Strategy, Failover and Failback
<!-- Lines 96-113 -->

Choose the strategy per tier from the ladder (backup and restore, pilot light, warm standby,
active/active) by the objectives against cost and complexity, never a rung stricter than needed.
Every recovery path relied on is exercised ([Exercising Recovery](assurance_performance_availability.md#exercising-recovery));
a standby that cannot be exercised realistically is converted to failover (both paths carrying
traffic continuously) where the objectives justify it, or removed. The rung is read against
[Recovery Objectives](#recovery-objectives), and the restore path it relies on is proven by
[Proving Restore](assurance_performance_availability.md#proving-restore).

- Failover started by a person through an automated push-button procedure: where a false alarm costs availability or data.
- Automatic failover on health signals, with trained oversight and tuned thresholds: only where the objective is shorter than a human can meet.
- MUST choose the rung by tier; MUST state the failover trigger rule; MUST plan failback separately.

Best instead when: active/active chosen for resilience alone is best only where its cost is
justified by the objectives. An unexercised standby, automatic failover with untuned thresholds,
and failback treated as failover reversed are best never. Open: the reconciliation of a maintained
standby against a single production path is inferred. `OPERATION.RECOVERY.4`

### Recoverability of Recovery Itself
<!-- Lines 116-136 -->

Recovery is independent of what failed: operations kept simple and available, pre-provisioned
capacity, and recovery tooling, runbooks, credentials, certificates, pipelines and contact paths
placed where the failure cannot take them away, with offline copies for the worst case.
Infrastructure and environment are defined as code and can be rebuilt from source on a clean
machine or account (relies on [Instance Replacement and Desired State](change_flow_delivery.md#instance-replacement-and-desired-state)),
and the restore path stays independent of schema tooling
([Proving Restore](assurance_performance_availability.md#proving-restore)). The recovered environment is held to the
production security baseline, with the root cause addressed first.

- MUST keep recovery tooling and credentials outside the failure domain.
- MUST be able to rebuild from source.
- MUST hold the recovered environment to the production baseline.
- MUST state the hardening-against-speed decision per system; the default accepts slower recovery for rare events.

Best instead when: favouring speed over hardening applies when the objective cannot be met by the
hardened path, and then the objective or the design is revisited (inferred). Recovery tooling
stored inside the system it recovers, and recovering into a weaker environment to fix later, are
best never. Open: no source argues the speed-first default; the hardening default is inferred, so
the stated per-system decision is the rule. `OPERATION.RECOVERY.5`

### Ownership, Monitoring, Roles and Plan Upkeep
<!-- Lines 139-158 -->

A named owner answers for data durability, including keeping the restore proof current
([Proving Restore](assurance_performance_availability.md#proving-restore)). Backup and restore jobs are scheduled work,
monitored on the signals of [Scheduled Work Signals](operation_objectives_and_signals.md#scheduled-work-signals), and failure alerts
are routed over a path that is itself verified. The recovery plan, runbooks and contact lists are
hand-written documents under the owner, date and review rule of
[Ownership, Freshness and Single Source](assurance_docs_security.md#ownership-freshness-and-single-source); keep them current and
accessible when production is down, reviewed periodically and on every change to the system or
organisation and after every test or incident. Assign recovery roles ahead of time; declare the end
of recovery by stated criteria.

- MUST name the owner of durability.
- MUST verify the alert path of backup failures.
- MUST review the plan on every change to the system, the organisation, a test or an incident.
- MUST assign recovery roles beforehand.

Best never: counting a completed backup job as success, a calendar-only plan review, or assigning
roles at the time of recovery. Open: the owner and monitoring clauses come from cases, not
measurement. `OPERATION.RECOVERY.6`

## Feedback into Development
<!-- Lines 161-170 -->

Failed-deployment recovery time and change failure rate are tracked as production feedback on
delivery, at the level of one service and shared across development and operations. They are never
made targets, because targets invite gaming and the signal must stay honest.

- MUST measure per service and share across development and operations.
- MUST NOT set targets on these measures.

Best never on the evidence read: targets on these measures. Open: the contrary view is argued in no
source read, so the condition under which it would be best is unknown. `OPERATION.FEEDBACK`
