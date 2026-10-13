# Change Flow: Build, Release, Deploy and Rollback

How one artifact is built once, released, deployed progressively and reversed when needed. Part of [Change Flow](change_flow.md), which holds the thesis and the index.

## Table of Contents

1. [Build and Pipeline](#build-and-pipeline) _(Lines 30-32)_
   1. [Scripted, Hermetic, Visible Build on Every Push](#scripted-hermetic-visible-build-on-every-push) _(Lines 35-41)_
   1. [Build Once, Promote One Artifact](#build-once-promote-one-artifact) _(Lines 44-50)_
1. [Release](#release) _(Lines 53-55)_
   1. [Cadence and Batch Size](#cadence-and-batch-size) _(Lines 58-72)_
   1. [Version Identity](#version-identity) _(Lines 75-85)_
   1. [Separating Release From Deployment](#separating-release-from-deployment) _(Lines 88-96)_
   1. [Staged Pipeline and Human Gates](#staged-pipeline-and-human-gates) _(Lines 99-110)_
   1. [Who May Release and When](#who-may-release-and-when) _(Lines 113-125)_
1. [Deployment](#deployment) _(Lines 128-130)_
   1. [Automated Deployment Path](#automated-deployment-path) _(Lines 133-140)_
   1. [Rollout Strategy and Canary Evaluation](#rollout-strategy-and-canary-evaluation) _(Lines 143-158)_
   1. [Environment Parity](#environment-parity) _(Lines 161-173)_
   1. [Instance Replacement and Desired State](#instance-replacement-and-desired-state) _(Lines 176-188)_
1. [Rollback](#rollback) _(Lines 191-193)_
   1. [Detecting and Deciding to Roll Back](#detecting-and-deciding-to-roll-back) _(Lines 196-206)_
   1. [Reversible by Design](#reversible-by-design) _(Lines 209-213)_
   1. [Undoing a Data Change](#undoing-a-data-change) _(Lines 216-226)_

---

## Build and Pipeline
<!-- Lines 30-32 -->

The build is scripted, repeatable and hermetic, runs a self-testing suite on every push in a reference environment, is visible to the whole team, and produces one artifact promoted unchanged to every environment. The same revision gives the same result anywhere, and what is promoted is what was built. Realizes [Artifact Integrity](assurance_rules.md#artifact-integrity) and carries out the check placement of [Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed). `CHANGE_FLOW.BUILD`

### Scripted, Hermetic, Visible Build on Every Push
<!-- Lines 35-41 -->

An automated build and self-testing suite runs on every push to the mainline in a reference environment, scripted and hermetic so the same revision gives the same result on any machine. Pipeline state and the flow of changes are visible to the whole team, with an audit trail. Every input comes from the repository content required by [Repository Content and Shape](change_flow_integration_review.md#repository-content-and-shape); reproducibility needs the pinned, declared dependencies of [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle). The environment definition is the one in [transverse.md](transverse.md).

- Every push to the mainline MUST trigger the build and suite.
- A build MUST depend on no machine-specific state. A build only on developer machines is best never.
- Security and performance checks sit in the pipeline stages at the placement the assurance rules decide. `CHANGE_FLOW.BUILD.1`

### Build Once, Promote One Artifact
<!-- Lines 44-50 -->

Build, release and run are separate stages. A release is immutable and uniquely identified, built once and promoted unchanged to every environment, with environment configuration kept outside it ([Separation of Configuration from Code and Secrets](transverse_config_environments.md#separation-of-configuration-from-code-and-secrets)) and its provenance verified before use ([Build Provenance and Match to Source](assurance_rules.md#build-provenance-and-match-to-source)). What runs in production is then the artifact that was tested and reviewed. The identifier is the one of [Version Identity](#version-identity).

- An artifact MUST be promoted by identity, not rebuilt.
- Per-environment rebuilds are best never for "what runs is what was reviewed": each rebuild is a different artifact, so tests on one do not cover another. `CHANGE_FLOW.BUILD.2`


## Release
<!-- Lines 53-55 -->

Releases are small and frequent, identified by what the identifier promises, separable from deployment by flags where needed, and passed through one staged automated pipeline with human gates only where the change class needs them, by an authorized group when responders are available. A release is small, identifiable, reversible and not performed blind. Each release is archived with its provenance ([Build Provenance and Match to Source](assurance_rules.md#build-provenance-and-match-to-source)); the staged pipeline is how the rules bind at release ([Rules Common to Every Property](assurance_rules.md#rules-common-to-every-property)). `CHANGE_FLOW.RELEASE`

### Cadence and Batch Size
<!-- Lines 58-72 -->

Prefer small, frequent releases over large infrequent ones; the cadence follows the release model. Frequency is raised only together with the supporting practices, because small batches cut blast radius and difficulty while frequency alone raises failures; cadence is judged by [Outcomes That Judge Delivery](change_flow_data_and_measure.md#outcomes-that-judge-delivery).

- The batch size per release MUST be kept as small as the model allows.

| Release model | Cadence |
|---|---|
| One live version, strong automation and tests | Every merge |
| Many components coordinated across teams | Regular train |
| Shipped products, libraries, several supported versions | Explicit versions |

Best instead when:
- Large infrequent releases: never as a goal; a long interval is accepted only as the consequence of a train or explicit versions.
- Continuous release without tests and automation: raises failure and burnout; precede it with those practices. `CHANGE_FLOW.RELEASE.1`

### Version Identity
<!-- Lines 75-85 -->

A release identifier promises only what is true. A compatibility-promising version scheme is used only for an artifact with a declared public interface consumed by others ([What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible)). A plain build or time identifier with no compatibility promise serves a deployed service with one live version. A consumer can then trust what a version number says.

- Every release MUST have a unique identifier.
- A version number that promises compatibility MUST be backed by a declared public interface.

Best instead when:
- Compatibility-promising versions on an internal service: consumers choose when to move.

Open: calendar versioning is not read in any source; open, not rejected. `CHANGE_FLOW.RELEASE.2`

### Separating Release From Deployment
<!-- Lines 88-96 -->

Where a feature must be turned off without redeploying, or work spans more than the integration interval, release is decoupled from deployment with flags. Each flag is inventory with a carrying cost: classified, created with an expiry and a removal task, and its production-reachable states tested. A flag's expiry is one case of [Decommissioning](evolution.md#decommissioning).

- A release toggle MUST carry an expiry and a removal task.
- The states that can occur in production MUST be tested. A flag without expiry adds a state to test forever.

Best instead when:
- No flags: batches are small, rollback by redeploy is fast and no work spans the integration interval. `CHANGE_FLOW.RELEASE.3`

### Staged Pipeline and Human Gates
<!-- Lines 99-110 -->

The path to production is one automated pipeline of stages, early ones giving fast feedback and later ones more confidence. Authorization after a reviewed merge is automatic by default. A human gate sits on a stage only where the change class warrants it: low confidence in automation or monitoring, high criticality or regulation, or a change not reversible by redeploy (including the irreversible data class of [Delivery Path and Gating of Database Change](change_flow_data_and_measure.md#delivery-path-and-gating-of-database-change)). Access control on who may release applies in either case. A gate is a stage within [Automated Deployment Path](#automated-deployment-path), not a different process.

- Every gate MUST state its criterion.
- A gate MUST NOT be skippable by a person with a different route to production.

Best instead when:
- A manual gate on every stage: regulation requires it; otherwise it becomes ritual and removes the speed argument.
- Fully hands-off: mature automation and monitoring; never for classes where a mistake cannot be rolled back.

Open: placing the irreversible data class under human gates is inferred. `CHANGE_FLOW.RELEASE.4`

### Who May Release and When
<!-- Lines 113-125 -->

Who may perform release operations is a recorded policy, while release itself stays self-service for the teams that own the system. Deployment proceeds only when someone able to respond is available. During an active incident only a change that remediates it ships, through a stated exception path ([Declaring and Running an Incident](operation_response_and_readiness.md#declaring-and-running-an-incident)).

- The set of release-permitted people MUST be a recorded policy.
- An incident exception path MUST exist.

Best instead when:
- A fixed off-hours blackout: only where nobody can respond; with automated rollback and round-the-clock response it is unnecessary.
- A freeze that blocks the incident's own remediation: best never.

Certainty: inferred; one practitioner source plus the argument that a change needs someone able to respond to its failure. `CHANGE_FLOW.RELEASE.5`


## Deployment
<!-- Lines 128-130 -->

Deployment is automated by the same process in every environment, exposes a release progressively by blast radius with a canary judged against a concurrent control, keeps environments alike in kind with unavoidable differences documented, and replaces instances rather than modifying them. A deployment is repeatable, bounded in blast radius and observable. Realizes [Availability and Recovery](assurance_performance_availability.md#availability-and-recovery); configuration reaches the one artifact through the delivery channel ([transverse.md](transverse.md)). `CHANGE_FLOW.DEPLOY`

### Automated Deployment Path
<!-- Lines 133-140 -->

Deployment uses the same automated, versioned, idempotent process for every environment, production included, and any authorized person can deploy any version on demand. One-off administrative processes run with the same code, environment and isolation as the application. A human trigger on a stage for a risky change class is a gate within the process, not a different process.

- Production MUST be deployed by the same scripted process as every other environment.
- Deployment scripts MUST be versioned.
- Admin code MUST ship with the application.
- A different or hand-driven production process is best never: it makes production the one environment never exercised. A fully hand-typed production step is banned. `CHANGE_FLOW.DEPLOY.1`

### Rollout Strategy and Canary Evaluation
<!-- Lines 143-158 -->

A release is exposed progressively, sized by blast radius and the cost of the strategy. A canary is judged against a concurrent control on a few user-impact metrics, not by before-and-after comparison, with automatic detection and halt or rollback. A regression is caught on a small share of users and the call to proceed rests on evidence. The halt criterion is the decision made in advance in [Detecting and Deciding to Roll Back](#detecting-and-deciding-to-roll-back); it carries out the production-side checks of the performance rules and shares guardrails with production experiments ([assurance.md](assurance_performance_availability.md#availability-and-recovery)).

- A rollout MUST have an automatic halt or rollback criterion.
- A canary MUST compare with a concurrent control.
- One canary at a time; population and duration sized to traffic and velocity.

Best instead when:
- Blue-green: stateful, downtime-sensitive applications with budget for two environments.
- Canary: high traffic and good metrics.
- One-box then waves with bake time: several regions.
- All traffic at once: only with no live traffic to protect or where the change cannot be split.
- Before-and-after canary judging: best never; traffic-mix drift reads as regression or hides one.

Open: the concurrent-control rule is general but rests on one source. `CHANGE_FLOW.DEPLOY.2`

### Environment Parity
<!-- Lines 161-173 -->

Every environment is kept alike production in kind (type and version of backing services, operating system, libraries), with a short commit-to-deploy time and no stand-ins that hide differences; credentials stay isolated per environment ([Separation and Isolation](transverse_config_environments.md#separation-and-isolation)). Differences that cannot be afforded (scale, data volume, permissions, production-only schemas) are written down, and changes that depend on them are routed to rehearsal on production-shaped data ([Rehearsal and Time Budget](change_flow_data_and_measure.md#rehearsal-and-time-budget)) and to the gated lane ([Delivery Path and Gating of Database Change](change_flow_data_and_measure.md#delivery-path-and-gating-of-database-change)).

- Backing-service type and version MUST match production in every environment.
- The list of known environment differences MUST be written down and referenced by the changes it affects.

Best instead when:
- Lightweight stand-ins in development: the adapter surface is narrow and production-like tests exist elsewhere in the pipeline.
- Test in production with canary and rollback instead of pre-production: high traffic, strong monitoring, fast rollback, stateless change only; a canary does not make a schema change safe.
- Accept divergence on scale, data volume and permissions: production-sized data is unaffordable.

Certainty: the split by axis (kind and version against scale and data) is reasoned, not stated by a source. `CHANGE_FLOW.DEPLOY.3`

### Instance Replacement and Desired State
<!-- Lines 176-188 -->

Running instances are replaced rather than modified, and the declared state of images and infrastructure is versioned code, so the running system equals what is declared and drift cannot persist. Either agents reconcile declared state continuously, or a scripted push is paired with drift detection. Replacement relies on [Fast Start and Graceful Stop](construction.md#fast-start-and-graceful-stop) so no work is lost.

- Declared state MUST be in version control.
- An instance MUST NOT be modified in place without the change recorded back into the declared state.

Best instead when:
- Managed mutable servers: stateful hosts where replacement is costly (inferred), always with drift detection.
- Push without drift detection: never; it cannot correct drift.

Open: pull-based reconcile versus scripted push with drift detection; no source compares them, so no switch is decided. `CHANGE_FLOW.DEPLOY.4`


## Rollback
<!-- Lines 191-193 -->

The way back is decided before a change ships: roll back automatically where redeploy reverses the change, fix forward where it does not, make every change backward compatible and reversible through version control, and give every data change a named undo. Going back is a rehearsed move, not an improvisation. Carries out resilience to a bad change ([Availability and Recovery](assurance_performance_availability.md#availability-and-recovery)); the data part also realizes [Data Integrity Under Change](assurance_interfaces_data.md#data-integrity-under-change). `CHANGE_FLOW.ROLLBACK`

### Detecting and Deciding to Roll Back
<!-- Lines 196-206 -->

Bad releases are detected automatically. Per change class and in advance, a change is either rolled back from alarms (backward compatible and reversible by redeploy) or fixed forward (not reversible by redeploy, such as a data migration past its last reversible point). Recovery time is short and the choice is not made under stress.

- The rollback-or-fix-forward choice MUST be decided per change class before shipping.

Best instead when:
- Fix forward for a reversible change: the pipeline is very fast; also when the change is not reversible by redeploy.
- Rolling code back against changed data: best never; it can corrupt.

Open: the decision rule by reversibility is inferred; no source states it. `CHANGE_FLOW.ROLLBACK.1`

### Reversible by Design
<!-- Lines 209-213 -->

Each change is backward compatible with the version it replaces, so rollback, mixed fleets and independent release are safe. An incompatible change keeps this through [Expand, Migrate, Contract](evolution.md#expand-migrate-contract), with schema changes released separately from application releases ([Order and Compatibility With Running Code](change_flow_data_and_measure.md#order-and-compatibility-with-running-code)). Every automated change is reversible through version control; a tool-level checkpoint is no substitute because it is neither reviewed nor versioned.

- A change MUST be compatible with the version it replaces during the deploy window. `CHANGE_FLOW.ROLLBACK.2`

### Undoing a Data Change
<!-- Lines 216-226 -->

Before a data or schema change ships, its undo is decided and recorded. Options, in the order tried: leave a backward-compatible expand step and roll the application back; carry a rehearsed written reverse where script reversal is faster than a restore; otherwise roll forward or use the restore. A change that can lose data falls back on the tested restore of [Layered Protection and Deletion Form](assurance_interfaces_data.md#layered-protection-and-deletion-form), and the last reversible point is named. The expand step relies on [Order and Compatibility With Running Code](change_flow_data_and_measure.md#order-and-compatibility-with-running-code).

- Every data change MUST record its undo before it ships.
- The last reversible point MUST be named.

Best instead when:
- A written reverse for every migration: packaged software with many installed versions, where a customer must downgrade; for a continuously deployed service with one production it is not worth writing every time and works poorly for data changes.
- Automatic down migrations: pure schema changes with no data to lose; never for a change that loses data.

Certainty: the choice among undo forms is inferred; recording the undo before shipping is grounded. `CHANGE_FLOW.ROLLBACK.3`
