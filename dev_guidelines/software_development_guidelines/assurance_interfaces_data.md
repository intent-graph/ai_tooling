# Assurance: Interfaces and Data Integrity

## Table of Contents

1. [Interfaces and Contracts](#interfaces-and-contracts) _(Lines 22-24)_
   1. [What Counts as Compatible](#what-counts-as-compatible) _(Lines 27-45)_
   1. [Contract Tests](#contract-tests) _(Lines 48-58)_
   1. [One Source of Description](#one-source-of-description) _(Lines 61-76)_
1. [Data Integrity Under Change](#data-integrity-under-change) _(Lines 79-81)_
   1. [Where Integrity Rules Live](#where-integrity-rules-live) _(Lines 84-93)_
   1. [Guarding Bulk and Destructive Operations](#guarding-bulk-and-destructive-operations) _(Lines 96-104)_
   1. [Layered Protection and Deletion Form](#layered-protection-and-deletion-form) _(Lines 107-118)_
   1. [Derived Data Sync and Staleness](#derived-data-sync-and-staleness) _(Lines 121-129)_
   1. [Checking Old Against New and Rolling Out Checks](#checking-old-against-new-and-rolling-out-checks) _(Lines 132-139)_

---

Part of [Assurance](assurance.md). How a change to an interface or to stored data is kept from breaking a consumer or corrupting data.

## Interfaces and Contracts
<!-- Lines 22-24 -->

Compatibility has a definition. It is verified between independently released components by contract tests, not by shared integrated environments. Each interface has one machine-readable source of description from which documentation, stubs and tests derive, and an automated diff catches breaking changes. So a change to an interface cannot silently break a consumer. `ASSURANCE.CONTRACTS`

### What Counts as Compatible
<!-- Lines 27-45 -->

A producer declares its public interface precisely and defines compatibility. Additive change is compatible. Removal, rename, type change, default change and behavioural change are breaking within a major version, and a breaking change is never silent. Users depend on all observable behaviour, so tests detect new implicit dependencies but cannot remove them; plan API change accordingly.

The evolution policy depends on consumer reach and artifact kind:

| Consumers | Policy |
|---|---|
| Few, in-house, reachable by conversation | Additive change plus a coordinated deploy; no version numbers |
| Many, external, or independently released | Explicit versioning with a deprecation window |
| Infrastructure-like API, large base, funds to carry old behaviour | An indefinitely compatible, date-pinned surface |

Rules:
- The public interface MUST be declared.
- A breaking change MUST be coordinated or deprecated, never silent.

Best instead when: coordination without versions fails when consumers release independently or are external (a simultaneous deploy is then impossible); explicit versioning is costly where consumers are few; the date-pinned surface only with a large base and the funds to carry old behaviour. A single-version service deployed as one unit fits the first row.

Open: no source gives a numeric boundary between "few" and "many" consumers. The consumer side of these policies is in [ownership.md](ownership.md). `ASSURANCE.CONTRACTS.1`

### Contract Tests
<!-- Lines 48-58 -->

Compatibility between independently released components is verified by contract tests, so teams deploy autonomously without a shared integrated environment. Every double of an external service is backed by a contract test against the real service, run on the rhythm of the supplier's changes. Its failure triggers a realignment task and need not break the build. Consumer-driven contracts serve a provider with known consumers under internal control; provider-side schema validation serves unknown consumers with a published specification; a provider with known consumers uses both (a schema catches drift; a consumer contract shows what this consumer still needs).

Rules:
- A double of an external service MUST have a contract test against the real service.
- A contract-test failure MUST create a realignment task.

A single-team application whose client and server always deploy together, with no old client in use, verifies its seam with integration tests and the description diff of [One Source of Description](#one-source-of-description). Where old clients stay in use after a server deploy, the independent-release rule applies. Open: this single-team rule is inferred; the deciding test is whether an old client can stay live.

Best instead when: a shared integrated environment, only when all consumers deploy together as one unit; consumer-driven contracts alone, only where consumers are many and under internal control. Serves the seams named in [Test Level Mix](assurance_behaviour.md#test-level-mix). `ASSURANCE.CONTRACTS.2`

### One Source of Description
<!-- Lines 61-76 -->

Each interface has one machine-readable description from which the reference documentation, client and server stubs, the types of every tier and the tests are derived, never hand-copied. The description is linted in CI against a team ruleset. CI diffs it against the main-branch version and fails on incompatible change; the diff covers the description only, so behaviour and semantics still need [contract tests](#contract-tests). The team records where the chain of types starts.

Rules:
- The description MUST have one source; a generated description MUST NOT be hand-edited.
- CI MUST block an incompatible change in the description.
- A type MUST NOT be hand-copied across tiers.

Best instead when:
- Code-first (description generated from a typed model): one team owns both ends.
- Design-first (description authored first): independent consumers depend on it.
- One class for storage and interface: only while the interface shape matches storage.
- Hand-maintained duplicates: never.

Open: "CI blocks" rests on tool capability, and code-first against design-first is contested. Requires [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped); documentation authoring is in [Documentation Practice](transverse_documentation.md#documentation-practice). `ASSURANCE.CONTRACTS.3`

## Data Integrity Under Change
<!-- Lines 79-81 -->

Stored data stays valid and in step through change. Integrity that must hold whatever writes the data is enforced where every write path converges. A change that can widen scope or destroy data states its scope and is recoverable by a tested restore. Derived data has a sync plan, with detection, before it exists. A new structure or invariant is checked against the old and brought into force observe-first when known violators exist. Procedures (batching, rehearsal) are in [Data and Schema Change](change_flow_data_and_measure.md#data-and-schema-change); backup practice is in [Backup, Restore and Disaster Recovery](operation_recovery_and_feedback.md#backup-restore-and-disaster-recovery). `ASSURANCE.DATA_INTEGRITY`

### Where Integrity Rules Live
<!-- Lines 84-93 -->

Rules that must hold whichever code writes (keys, not-null, foreign keys, row-local checks, atomic audit) are declared in the store, in addition to validation at the edge. Rules that change with product decisions (workflow, policy) live in the application. Migrations, administrative tools and ad-hoc statements bypass application code, so an invalid state must be unwritable by any path. The least powerful form that expresses a cross-writer rule wins: a declarative constraint is checked by the engine on every path; a procedural mechanism can be disabled or bypassed.

Rules:
- MUST declare in the store every invariant that must hold across writers, and MUST name constraints so a violation maps to a stable contract error ([Errors at the Boundary](construction.md#errors-at-the-boundary)).
- MUST validate at the edge as well ([Parse or Validate at the Edge](construction.md#parse-or-validate-at-the-edge)).
- MUST NOT put policy that changes with product decisions in the store.

Best instead when: application-layer invariants alone, when a single application owns the store ([Data Ownership by One Application](construction.md#data-ownership-by-one-application)); that condition rarely holds. Open: the split of the middle zone is inferred and contested. `ASSURANCE.DATA_INTEGRITY.1`

### Guarding Bulk and Destructive Operations
<!-- Lines 96-104 -->

Scope is stated, never inferred. A destructive or bulk operation of unbounded scope requires an explicit opt-in from its caller, plus validation of mandatory keys, key order and timestamp sanity. A schema change is linted in CI against unsafe operations and passes only with an explicit override assertion. Omitting a filter or running an unsafe migration cannot silently widen the effect.

Rules:
- MUST require the opt-in at the operation's interface, not in documentation.
- MUST record an override as an explicit, reviewable assertion in the change.

Best instead when: the schema lint alone suffices only where no application issues bulk writes. A gate with a visible override: [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped). `ASSURANCE.DATA_INTEGRITY.2`

### Layered Protection and Deletion Form
<!-- Lines 107-118 -->

Data is defended in layers because every single strategy eventually fails: deletion reversible for a stated window, backups, and early detection of corruption (see [Checking Old Against New and Rolling Out Checks](#checking-old-against-new-and-rolling-out-checks)). A destructive change (drop, delete, truncate) is not reversible by script; its undo is a restore prepared and tested before the change runs ([Proving Restore](assurance_performance_availability.md#proving-restore)). Where recovery or audit of deleted records is needed, the row is deleted and archived in the same transaction. A deleted flag is kept only when undelete is a user-facing feature whose costs are paid: every query excludes deleted rows by default, children of a deleted parent are handled explicitly.

Rules:
- MUST test the restore before a destructive change runs.
- MUST state the retention window.
- MUST keep a legally required purge possible.

Best instead when: a deleted flag as the default form, when undelete is a product feature; backups alone for the window, when deleted rows have no audit value and point-in-time restore is fast enough.

Retention of personal data and erasure in backups bound the layers: [Retention Periods](transverse_privacy.md#retention-periods), [Erasure and Deletion Mechanism](transverse_privacy.md#erasure-and-deletion-mechanism); backup retention and handling: [Backup Scope and Design](operation_recovery_and_feedback.md#backup-scope-and-design), [Backup Protection and Isolation](operation_recovery_and_feedback.md#backup-protection-and-isolation). Open: the choice of deletion form is inferred. `ASSURANCE.DATA_INTEGRITY.3`

### Derived Data Sync and Staleness
<!-- Lines 121-129 -->

No derived or denormalized data exists without a synchronisation plan, chosen from a ladder by cost and strength: documentation only, declared constraints, detection queries, scheduled refresh, same-transaction triggers. The choice follows the impact of divergence, change frequency and tolerable staleness. The plan states what, sync level, freshness target, how drift is found and fixed, and what alerts, and exists before the data does. Detection queries run on a schedule set by importance with a stated action on divergence.

Rules:
- MUST write the plan before the data exists.
- MUST state the freshness target and the alert; "eventual" without a stated window is unstated.

Best instead when: always-consistent (same transaction) when divergence is costly and writes are few; eventual with a monitored window when divergence is cheap. A plan written after the data exists is never the best. Scheduled detection is signalled by [Scheduled Work Signals](operation_objectives_and_signals.md#scheduled-work-signals). `ASSURANCE.DATA_INTEGRITY.4`

### Checking Old Against New and Rolling Out Checks
<!-- Lines 132-139 -->

Before an old structure is removed, the new data is validated against the old (side-by-side reads with an alert on mismatch, or validation jobs independent of application logic). Every convention ships with a check that finds its violations. A new invariant check is enforced at once when no known violator exists. When known violators exist in production, it runs observe-only first, recording findings with nothing raising, and is enforced once the open defects are removed.

Rules:
- MUST give observe-only mode an exit condition and an owner.
- MUST NOT remove the old structure before validation passes.

Best instead when: immediate enforcement when nothing known would trip it; observe-only without an owner or exit is never the best. Open: who owns observe-only mode is inferred (no source states it). These checks are the detection layer of [Layered Protection and Deletion Form](#layered-protection-and-deletion-form) and run inside the rehearsal and rollout of [Data and Schema Change](change_flow_data_and_measure.md#data-and-schema-change). `ASSURANCE.DATA_INTEGRITY.5`
