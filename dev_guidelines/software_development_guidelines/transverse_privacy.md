# Transverse: Privacy

How personal data is minimised, retained and erased. Part of [Transverse](transverse.md).

## Table of Contents

1. [Privacy and Retention](#privacy-and-retention) _(Lines 14-21)_
   1. [Minimisation, Classification and Design-In](#minimisation-classification-and-design-in) _(Lines 24-37)_
   1. [Retention Periods](#retention-periods) _(Lines 40-56)_
   1. [Erasure and Deletion Mechanism](#erasure-and-deletion-mechanism) _(Lines 59-84)_
   1. [Privacy Risk, Impact Assessment and Breach](#privacy-risk-impact-assessment-and-breach) _(Lines 87-104)_
## Privacy and Retention
<!-- Lines 14-21 -->

Personal data is collected only for stated purposes, classified with safeguards per level,
retained on a recorded schedule per purpose and deleted by mechanism, with an inventory of copies
so erasure can reach them. Privacy is managed as a risk, assessed before high-risk processing and
answered when a breach occurs. The team holds only the personal data it needs, for as long as it
needs it. Legal text is restated as neutral practice; regulated contexts are out of scope.
`TRANSVERSE.PRIVACY`

### Minimisation, Classification and Design-In
<!-- Lines 24-37 -->

Only the personal data necessary for each stated purpose is collected, by default. Sensitive data
is classified into protection levels with safeguards documented per level (encryption, integrity,
retention, logging, database security), and protection is built into design and defaults, scaled to
risk.

- MUST state the purpose for each personal data field collected. Collecting now and deciding the
  purpose later is best never.
- Where logs support investigation but not identification, pseudonymise identifiers.
- Never put personal or sensitive data in propagated trace context, nor seed trace identifiers from
  user-identifiable data (propagation: [Telemetry](operation_objectives_and_signals.md#telemetry)).

`TRANSVERSE.PRIVACY.1`

### Retention Periods
<!-- Lines 40-56 -->

Retention is a recorded decision per purpose and data class, long enough for the purpose and no
longer than the legal, contractual or purpose limit. Deletion is automated by class and runs on
schedule; the periods hold for backup copies too
([Backup Scope and Design](operation_recovery_and_feedback.md#backup-scope-and-design) keeps a backup no longer than they
allow).

- MUST record the period and its reason per class.
- MUST automate deletion by class.
- Periods are set per the classification of [Minimisation, Classification and Design-In](#minimisation-classification-and-design-in).

Best instead, for logs: those holding personal data keep the legal minimum, then delete; those that
can be pseudonymised, where dwell time is long, keep longer and tier by age. Keeping everything
indefinitely is best never.

Open: no source gives a retention period; each team sets its own. `TRANSVERSE.PRIVACY.2`

### Erasure and Deletion Mechanism
<!-- Lines 59-84 -->

Deletion is decided per entity from the reason the data is kept, and the choice is recorded. The
team keeps an inventory of where each personal data field has copies (caches, logs, derived
stores, third parties, backups) and how an erasure request reaches each. Treating erasure as
complete after the live system is best never.

| Reason the data is kept | Deletion form |
|---|---|
| No need | Hard delete |
| Recovery or audit of deleted records | As decided in [Layered Protection and Deletion Form](assurance_interfaces_data.md#layered-protection-and-deletion-form) |
| Queryable past values | Temporal model |
| Time-bounded bulk expiry | Drop or detach time partitions; bulk delete is best on small tables where partitioning costs more than it saves (inferred) |

- MUST record the deletion choice per entity.
- MUST tell the data subject what happens to backups.
- MUST keep a legally required purge possible.
- Erased data in a backup is put beyond use: no other use or access, no restore without
  re-applying every erasure recorded since (an erasure log kept outside the backup), deletion when
  the copy expires on schedule. A copy locked as immutable is handled the same way, its lock expiry
  being its schedule ([Backup Protection and Isolation](operation_recovery_and_feedback.md#backup-protection-and-isolation)).
- Applies the periods of [Retention Periods](#retention-periods); erasure in bulk is batched as in
  [Bulk and Backfill Design](change_flow_data_and_measure.md#bulk-and-backfill-design).

Open: whether erasure must reach logs and every copy on request is contested, no source read
settles it; the backup rule rests on one regulator. `TRANSVERSE.PRIVACY.3`

### Privacy Risk, Impact Assessment and Breach
<!-- Lines 87-104 -->

Privacy is managed as a risk through a framework, not as compliance alone. An impact assessment
(processing and purposes, necessity and proportionality, risks to individuals, mitigations) runs
before high-risk processing. The team can determine, within a short stated clock, what a breach
touched, and records every breach with facts, effects and remedial action.

- MUST assess before high-risk processing starts.
- MUST record every breach.
- Relies on [Incidents](operation_response_and_readiness.md#incidents) for breach handling, and on the classification of
  [Minimisation, Classification and Design-In](#minimisation-classification-and-design-in) and the
  log entries of [Entry Content, Time and Format](transverse_security.md#entry-content-time-and-format) to answer it.

Best instead: compliance alone is sufficient only where just a legal minimum is demanded and the
processing is low risk.

Open: the framework body was not read; the neutral restatement and the link to logging are
inferred. `TRANSVERSE.PRIVACY.4`

