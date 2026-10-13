# Assurance

## Table of Contents

1. [Map](#map) _(Lines 17-31)_
1. [Principles that hold in every file](#principles-that-hold-in-every-file) _(Lines 34-40)_
1. [Best instead when](#best-instead-when) _(Lines 43-46)_
1. [Still open](#still-open) _(Lines 49-51)_
1. [Realised in](#realised-in) _(Lines 54-55)_

---

Every property that must hold has a named mechanism, at a named stage, that runs on every change. The signal can be believed, the gates cannot be skipped, and review is independent and bound to the exact content. No property rests on one control or on the author's judgement. The aim: the design was good, the testing was good, the review was trustworthy, and what runs is what was reviewed. `ASSURANCE`

## Map
<!-- Lines 17-31 -->

One placement per property. Each row says where its practice is written.

| Property | What it guarantees | Where |
|---|---|---|
| Rules common to every property | A pass can be believed, gates always run, review is independent and binds, every change meets one bar | [assurance_rules.md](assurance_rules.md#rules-common-to-every-property) |
| Artifact integrity | What runs is built from reviewed source; the mainline binds every actor | [assurance_rules.md](assurance_rules.md#artifact-integrity) |
| Behaviour | A self-testing suite whose power is measured; no test leaves a durable effect on data | [assurance_behaviour.md](assurance_behaviour.md#behaviour) |
| Interfaces and contracts | A change to an interface cannot silently break a consumer | [assurance_interfaces_data.md](assurance_interfaces_data.md#interfaces-and-contracts) |
| Data integrity | Stored data is valid and in step after any change, a mistaken one included | [assurance_interfaces_data.md](assurance_interfaces_data.md#data-integrity-under-change) |
| Documentation in sync | Documentation cannot drift from what it describes | [assurance_docs_security.md](assurance_docs_security.md#documentation-in-sync) |
| Security | Checked on every change at a depth proportioned to risk; limits enforced in tooling | [assurance_docs_security.md](assurance_docs_security.md#security) |
| Performance | Speed and capacity hold under the real workload; a regression is caught on its change | [assurance_performance_availability.md](assurance_performance_availability.md#performance) |
| Availability and recovery | The system keeps serving when a dependency fails; recovery is proven, not assumed | [assurance_performance_availability.md](assurance_performance_availability.md#availability-and-recovery) |

## Principles that hold in every file
<!-- Lines 34-40 -->

- **Mechanism, stage, trigger.** Every property has a mechanism, a stage and a recurring trigger.
- **False-alarm budget.** Every check, blocking or advisory, has a stated false-alarm budget against which its measured rate is held ([Trustworthy Signal](assurance_rules.md#trustworthy-signal)).
- **No skippable gate.** A skipped or missing required check counts as a failure ([Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped)).
- **Approval binds content.** Every approval binds the exact content that ships ([Independent Review That Binds](assurance_rules.md#independent-review-that-binds)).
- **Untested is absent.** A mode, backup, plan or check that was never exercised is treated as absent.

## Best instead when
<!-- Lines 43-46 -->

- **One assurance practice per lifecycle stage** (instead of one placement per property) is the better view for pipeline design: see [change_flow.md](change_flow_delivery.md#build-and-pipeline), which carries the practices out.
- **A single global quality gate** is the floor, not the whole: [One Bar and Evidence for Every Change](assurance_rules.md#one-bar-and-evidence-for-every-change) sets it, and a gap in one stage would otherwise stay invisible.

## Still open
<!-- Lines 49-51 -->

- Open points that change what a reader does are shown inline in the node where they arise: effect size of mutation testing, the cadence of restore tests, the period of penetration tests, the frequency of production recovery drills, the content of release archiving, and the coverage of the single-team seam rule.

## Realised in
<!-- Lines 54-55 -->

[construction.md](construction.md), [change_flow.md](change_flow.md), [operation.md](operation.md) and [transverse.md](transverse.md) operate these properties; [ownership.md](ownership.md) holds the consumer side of interfaces and the dependency inventory.
