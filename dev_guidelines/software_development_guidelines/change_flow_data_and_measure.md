# Change Flow: Data Change and Measurement

How schema and data changes travel the same path as code, and how delivery is judged. Part of [Change Flow](change_flow.md), which holds the thesis and the index.

## Table of Contents

1. [Data and Schema Change](#data-and-schema-change) _(Lines 24-28)_
   1. [Form and Source of a Change](#form-and-source-of-a-change) _(Lines 31-46)_
   1. [Migration History and Immutability](#migration-history-and-immutability) _(Lines 49-58)_
   1. [Delivery Path and Gating of Database Change](#delivery-path-and-gating-of-database-change) _(Lines 61-75)_
   1. [Order and Compatibility With Running Code](#order-and-compatibility-with-running-code) _(Lines 78-92)_
   1. [Locks and Online Schema Change](#locks-and-online-schema-change) _(Lines 95-107)_
   1. [Bulk and Backfill Design](#bulk-and-backfill-design) _(Lines 110-125)_
   1. [Rehearsal and Time Budget](#rehearsal-and-time-budget) _(Lines 128-140)_
   1. [Running and Watching a Production Data Job](#running-and-watching-a-production-data-job) _(Lines 143-157)_
1. [Measuring Delivery](#measuring-delivery) _(Lines 160-162)_
   1. [Outcomes That Judge Delivery](#outcomes-that-judge-delivery) _(Lines 165-177)_
   1. [Independent Baselines and Preconditions](#independent-baselines-and-preconditions) _(Lines 180-185)_

---

## Data and Schema Change
<!-- Lines 24-28 -->

Every schema and data change is a reviewed, versioned, once-only script tracked in the target's history and never hand-typed. It is delivered through one pipeline with a risk-based human trigger for the risky class, ordered compatibly with the code, made without blocking locks, with bulk work in re-runnable bounded batches, rehearsed on production-shaped data and watched until a convergence query says it is done. What runs in production is what was reviewed and rehearsed. Realizes [Data Integrity Under Change](assurance_interfaces_data.md#data-integrity-under-change). Scale and downtime tolerance move the gating; data volume moves bulk design and rehearsal.

Certainty: inferred; many nodes here rest on one maintainer practice that public practice is read as agreeing with or extending. `CHANGE_FLOW.DATA_CHANGE`

### Form and Source of a Change
<!-- Lines 31-46 -->

Every schema and data change is a migration script in version control, ordered, applied once, recorded, and run by the process of [Automated Deployment Path](change_flow_delivery.md#automated-deployment-path), never by hand-typed statements. Changes are as small as possible and the reviewed script is the script deployed ([Build Provenance and Match to Source](assurance_rules.md#build-provenance-and-match-to-source)). Once-only checks rely on the history of [Migration History and Immutability](#migration-history-and-immutability).

- Every database change MUST be a script in version control applied by tooling.
- A change MUST NOT be hand-typed.
- Each migration MUST name its ticket.
- The reviewed script MUST be the deployed script.

Best instead when:
- Declarative desired state as the deployed unit: never, a plan computed at deploy time was not what was reviewed; fine for fast local loops and as the authoring form when the generated script is reviewed.
- Ordered scripts as source are required by compliance, many instances or packaged software.
- Idempotent DDL on every statement: for steps that can be partially applied and environments known to differ; for transactional all-or-nothing steps the once-only tool already serves.
- A separate stream for urgent data fixes: when such fixes are frequent and must not wait for the release train; otherwise it is a second delivery truth.

Open: idempotent DDL as defence in depth and the urgent-fix stream rest on maintainer practice with reasoned conditions. `CHANGE_FLOW.DATA_CHANGE.1`

### Migration History and Immutability
<!-- Lines 49-58 -->

Each database records in itself which migrations ran, and an applied migration is never edited: a failed one is fixed and rerun, a wrong one is corrected by a new migration, and a recorded checksum enforces this. Reference data is kept with the migrations, so any environment's state is knowable and reproducible.

- An applied migration MUST NOT change.
- The history MUST live in the target database.

Best instead when:
- Editing an applied migration after rolling it back: only one environment has applied it.
- Unrecorded history: never. `CHANGE_FLOW.DATA_CHANGE.2`

### Delivery Path and Gating of Database Change
<!-- Lines 61-75 -->

Database change travels in the same pipeline as application change, as the reviewed script, with one history and one audit trail, not as a separate manual track. A recorded criterion classes each change. Ordinary changes apply automatically through every environment. The risky class passes an authorization stage where a named, qualified group approves the production run on the exact script and a member triggers it. This carries out the qualified approval of [Mechanism and Depth by Risk](change_flow_integration_review.md#mechanism-and-depth-by-risk), is the human gate of [Staged Pipeline and Human Gates](change_flow_delivery.md#staged-pipeline-and-human-gates) for the irreversible class, and applies the guarded start of [Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access).

- The classification criterion MUST be recorded (it takes the time budget of [Rehearsal and Time Budget](#rehearsal-and-time-budget) and the size of the data as inputs).
- A risky-class change MUST NOT start from an automatic merge.
- A production run of the risky class MUST name who runs it and be approved on the exact script.

Best instead when:
- Fully automated for the risky class: changes are small, fast, compatible and reversible, with staged rollouts and high deploy frequency (it is the default for the ordinary class).
- Production applied manually for every change: most tables exceed the recorded size; the criterion then routes most changes to the risky class on its own.
- Withholding the merge of the release approval until production is applied: keeps the mainline equal to what runs in production, needed when merging triggers production deployment (a mechanism, inferred).
- A separate idempotent authoring script for configuration-like content: the content is data-like, small and often re-authored, provided the run is recorded in the same history.

Open: the named qualified group and the risk-based split as a general rule are inferred (no public source); no public counterpart found for configuration-like content on its own path. `CHANGE_FLOW.DATA_CHANGE.3`

### Order and Compatibility With Running Code
<!-- Lines 78-92 -->

A schema change deploys separately from and before the code that needs it, because old and new code run against the same data during the deploy window. An incompatible structural change follows [Expand, Migrate, Contract](evolution.md#expand-migrate-contract), with a scheduled contract step. An application deploy is gated on the schema version it declares and fails if the history lacks it. Specialises [Reversible by Design](change_flow_delivery.md#reversible-by-design) to stored data; database access sits behind a clear layer in code ([construction.md](construction.md)); the compatibility surface follows consumer reach ([What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible)).

- A schema change MUST deploy before the code that needs it.
- The contract step MUST have a date (its owner is [Expand, Migrate, Contract](evolution.md#expand-migrate-contract)).
- An application deploy MUST fail if the schema history lacks the minimum version it declares. The gate checks the order; it does not replace it.

Best instead when (compatibility surface, by consumers of the shared structure):
- Views: consumers read shape (declarative, read-only reporting, several consumers).
- A function interface: consumers are many and diverse and the interface absorbs change (maintainer practice, no public source).
- Versioned interfaces: remote APIs, not database structure.
- Code and schema deployed together for an incompatible change: best never with rolling deploy or rollback.

Open: the minimum-schema-version gate as the general form rests on a single maintainer source. `CHANGE_FLOW.DATA_CHANGE.4`

### Locks and Online Schema Change
<!-- Lines 95-107 -->

The lock a statement takes is known before it runs on a shared database. Migrations use a per-session lock timeout with retry, prefer the non-blocking form of each change, run non-transactional operations in their own step, and use an online schema change tool on large tables where in-place change blocks. A schema change never holds a blocking lock longer than a stated bound. Sharding applies to data changes only, the batches of [Bulk and Backfill Design](#bulk-and-backfill-design).

- The lock taken by a statement MUST be known before a run on a shared database.
- A migration MUST set a session-level lock timeout (a global timeout affects unrelated sessions).
- A statement that cannot run in a transaction MUST run in its own step.

Best instead when:
- A trigger-based online tool on a high-write primary: never, it adds write overhead and cannot pause; best when writes are light and simplicity wins.
- In-place change on a large table where it blocks: never.

Context: table size, write rate and whether the operation is metadata-only decide the form. Open: the starvation reason for timeout-with-retry is inferred. `CHANGE_FLOW.DATA_CHANGE.5`

### Bulk and Backfill Design
<!-- Lines 110-125 -->

A change that finishes in minutes is a plain migration. A change over very large data is cut into bounded, throttled, re-runnable batches, decided by batching key, work list, fan-out and observe-and-recover, in their own step apart from schema steps. Where it runs is decided and recorded by duration, so it can be interrupted, repeated and verified without corruption. Bulk work is bounded by the explicit scope of the data-integrity rules ([Data Integrity Under Change](assurance_interfaces_data.md#data-integrity-under-change)).

- A bulk batch MUST be re-runnable with the same result.
- A batch MUST NOT run inside a long schema-change transaction.
- The place a backfill runs MUST be recorded with its reason.

Best instead when (place by duration, no single winner):
- In the migration: it finishes in minutes (one transaction).
- Background job: the work outlasts a deploy.
- Offline snapshot: very large multi-table moves, trading zero production load against a copy that must be reconciled.
- A framework: only when the job recurs; for a one-off job compose standard tools.
- External bookkeeping instead of a self-limiting predicate: the data cannot carry its own progress.

Open: the four-decision procedure and the standard-tools rule rest on one maintainer practice; place by duration is contested. `CHANGE_FLOW.DATA_CHANGE.6`

### Rehearsal and Time Budget
<!-- Lines 128-140 -->

A data change is rehearsed before production on data whose size and shape make the measured time, lock behaviour and plan representative, and the measurements are kept with the change. For small data a developer database with sample data suffices. Migrations have a time budget by class; personal data is masked and side effects blocked in any copy of production ([Privacy and Retention](transverse_privacy.md#privacy-and-retention)). The rehearsal data is one case of [Tests Without Durable Effect on Data](assurance_behaviour.md#tests-without-durable-effect-on-data). The time budget is the criterion of the risky class in [Delivery Path and Gating of Database Change](#delivery-path-and-gating-of-database-change).

- MUST measure duration and lock behaviour on a rehearsal copy before production and keep the figures with the change.
- A migration with a skip marker MUST be rehearsed elsewhere.
- Personal data MUST be masked in a copy of production.

Best instead when:
- Developer databases with sample data: small data (production-sized copies cost cloning and personal-data risk for no gain). For large tables timings do not transfer, so use production-shaped data.
- Rehearsal in a rolled-back transaction on shared real data: only where data cannot be cloned and every effect can be undone; not the general rule.

Open: the time-budget figures (3 and 10 minutes, one second) are one team's values, defaults to calibrate; restored-dump rehearsal on every request is inferred. `CHANGE_FLOW.DATA_CHANGE.7`

### Running and Watching a Production Data Job
<!-- Lines 143-157 -->

A production bulk job is declared done by a written convergence query that returns zero remaining work, not by the process returning. It does not start until a pre-start checklist holds: ticket, index-backed plan, idempotent batches, written convergence query, detached run with a ledger, qualified review where it holds locks, a stop plan. It is ramped with a halt on the first failure, paced on the target system's health, and watched on lock waits and replica lag (the service and resource signals of the operation section, [operation.md](operation.md)). Who triggers a risky run is held in [Delivery Path and Gating of Database Change](#delivery-path-and-gating-of-database-change); how batches are designed in [Bulk and Backfill Design](#bulk-and-backfill-design); the qualified approver follows [Mechanism and Depth by Risk](change_flow_integration_review.md#mechanism-and-depth-by-risk).

- A convergence query MUST be written before the job starts.
- The first production run MUST halt on the first failure.
- A bulk job MUST keep a ledger.
- A long-running statement MUST be identifiable to its change in activity views and logs (for example the ticket key in a comment).

Best instead when:
- "Done" when the job returns: never; it cannot see skipped batches. Guessing concurrency: never.
- The full checklist for a job of minutes: only at large blast radius; the size gate decides.

Open: no public counterpart found for the convergence query and for identifying a statement to its change. `CHANGE_FLOW.DATA_CHANGE.8`


## Measuring Delivery
<!-- Lines 160-162 -->

Delivery is judged by outcomes (lead time, deployment frequency, recovery time, change fail rate, rework), used to guide improvement and not to rank people, and never by the volume of code produced. A measured gain from automation is checked against an independent baseline, and the fundamentals of the delivery system are treated as preconditions. Delivery outcome measures are the evidence that judges whether the rules produce trustworthy delivery ([Rules Common to Every Property](assurance_rules.md#rules-common-to-every-property)); production feeds some of them back ([Feedback into Development](operation_recovery_and_feedback.md#feedback-into-development)). `CHANGE_FLOW.MEASURE`

### Outcomes That Judge Delivery
<!-- Lines 165-177 -->

Delivery is measured with five outcome metrics: change lead time, deployment frequency, failed-deployment recovery time, change fail rate, deployment rework rate. They are signals to guide improvement, not to rank people. The two that production feeds back (recovery time, change fail rate) are never made targets ([Feedback into Development](operation_recovery_and_feedback.md#feedback-into-development)). Speed and stability move together only with supporting practices; the change flow is judged by outcomes, never by the volume of code or changes produced.

- Delivery MUST be judged on the outcome measures.
- The metrics MUST NOT be used to rank individuals.
- Output volume (code, pull requests) as the measure is best never: it measures activity.

Best instead when (net effect of automation on outcomes):
- Positive: teams with version control, small batches, testing, a platform and a clear policy.
- Vanishing or negative: teams without those foundations.

Open: the net effect of automation on delivery outcomes is contested (small samples, vendor sources) and not decided. `CHANGE_FLOW.MEASURE.1`

### Independent Baselines and Preconditions
<!-- Lines 180-185 -->

A claimed gain from automation, in speed or security, is measured against a baseline not produced by the claimant. Version control, small batches, testing, a platform and a clear policy are preconditions, because automation magnifies existing strengths and weaknesses. The baseline checks the measures of [Outcomes That Judge Delivery](#outcomes-that-judge-delivery); frequency gains count only where the preconditions hold, which bounds how [Cadence and Batch Size](change_flow_delivery.md#cadence-and-batch-size) is judged.

- A claimed gain MUST be measured against a baseline not produced by the claimant. A self-reported gain is not evidence for an adoption decision.

Certainty: the independent baseline as a principle is inferred from small-sample findings. `CHANGE_FLOW.MEASURE.2`
