# Operation


The running system is held to a stated reliability objective below 100 percent, measured as users
experience it and governed by an agreed rule. A human is paged only for what needs a human now.
Every service exposes the signals that show user harm and resource strain, capacity is planned
against a measured breaking point, and procedures are owned documents that a responder who did not
write them can follow. Incidents follow written conditions and named roles, workloads launch after
a readiness review, and recovery is designed from stated objectives and proven before it is needed.
The system stays within its objectives and, when it fails, is restored within them. `OPERATION`

Hard rules of the branch:

- A page MUST NOT be sent unless a human action is needed now.
- A workload MUST NOT be launched without a readiness review.
- A backup, plan or restore MUST NOT be treated as present until tested (the proof is in
  [Availability and Recovery](assurance_performance_availability.md#availability-and-recovery)).
- A target MUST NOT be set on the delivery measures that production feeds back to development.

This branch holds the practice; the assurance branch holds the proof that the practice works
(one location per fact). Related: [Minimisation, Classification and Design-In](transverse_privacy.md#minimisation-classification-and-design-in)
(backup retention) and [Detection and Escalation](transverse_security.md#detection-and-escalation) (security monitoring).

Files of this branch (sections in order):

- [Objectives and Signals](operation_objectives_and_signals.md): Reliability objective and error budget, paging, and the telemetry that shows user harm and resource strain.
  - [Reliability Targets](operation_objectives_and_signals.md#reliability-targets): objective, indicators, error budget and its consequence.
  - [Alerting](operation_objectives_and_signals.md#alerting): what pages a human, and on what basis.
  - [Telemetry](operation_objectives_and_signals.md#telemetry): the signals, their correlation, sampling, cost and vantage points.
- [Response and Readiness](operation_response_and_readiness.md): Incident handling, capacity planning, the launch gate, and owned procedures.
  - [Incidents](operation_response_and_readiness.md#incidents): declaring, running and learning from them; the human load.
  - [Capacity](operation_response_and_readiness.md#capacity): planning method, headroom and overload, storage health.
  - [Operational Readiness](operation_response_and_readiness.md#operational-readiness): the launch gate and keeping it true.
  - [Runbooks and Playbooks](operation_response_and_readiness.md#runbooks-and-playbooks): owned, validated procedures and their automation.
- [Recovery and Feedback](operation_recovery_and_feedback.md): Recovery designed from objectives, and delivery measures fed back from production.
  - [Backup, Restore and Disaster Recovery](operation_recovery_and_feedback.md#backup-restore-and-disaster-recovery): objectives, backups, strategy, upkeep.
  - [Feedback into Development](operation_recovery_and_feedback.md#feedback-into-development): delivery measures from production, never targets.
