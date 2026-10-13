# Cross links of J8_evolution (for the linker)

Links whose other endpoint is outside J8_evolution. Columns: source uid, target uid, link type, intent sentence. Source is always an EVOLUTION node. The L1 node EVOLUTION and its links belong to the TOP batch.

| source | target | type | intent |
|---|---|---|---|
| EVOLUTION.DECISIONS | OWNERSHIP.SELECTION.1 | realizes | The reason for a selection is stored as a decision record, which the decision-records branch defines. |
| EVOLUTION.DECISIONS.1 | OWNERSHIP.SELECTION.1 | realizes | The content a record must state is what lets the selection's reason be recovered. |
| EVOLUTION.DECISIONS.2 | OWNERSHIP.SELECTION | realizes | The significance test decides which selection decisions get a record. |
| EVOLUTION.DECISIONS.4 | TRANSVERSE.DOCS | see | Documents that describe the current state are living and are held by the documentation practice, not by record supersession. |
| EVOLUTION.DECISIONS.5 | CHANGE_FLOW.REVIEW | see | Accepted records are consulted during the review the change flow carries out. |
| EVOLUTION.DECISIONS.5 | ASSURANCE.RULES.4 | see | Consulting records matches the independent review that binds. |
| EVOLUTION.INCREMENTAL | OWNERSHIP.STANCE.4 | realizes | Incremental change carries the no-building-for-presumed-needs stance to the unit of change. |
| EVOLUTION.INCREMENTAL | OWNERSHIP.LIFECYCLE | realizes | Incremental change and migration carry out the lifecycle of what the team owns. |
| EVOLUTION.INCREMENTAL | ASSURANCE.CONTRACTS | realizes | Incremental change keeps the promises the contract decisions state. |
| EVOLUTION.INCREMENTAL.1 | CHANGE_FLOW.INTEGRATION | see | Releasable steps rest on the integration practice. |
| EVOLUTION.INCREMENTAL.1 | CHANGE_FLOW.ROLLBACK | see | Releasable steps keep rollback possible. |
| EVOLUTION.INCREMENTAL.1 | OWNERSHIP.STANCE.4 | realizes | Build to learn is the stance of not building for presumed needs, carried to the step. |
| EVOLUTION.INCREMENTAL.2 | CHANGE_FLOW.DATA_CHANGE | see | The mechanics of expand, migrate, contract for stored data are held in the data-change practice. |
| EVOLUTION.INCREMENTAL.2 | CHANGE_FLOW.ROLLBACK | see | Expanding first keeps rollback possible during the move. |
| EVOLUTION.INCREMENTAL.2 | ASSURANCE.CONTRACTS.1 | realizes | What counts as an incompatible change is decided by the provider-side evolution policy. |
| EVOLUTION.INCREMENTAL.3 | OWNERSHIP.STANCE | see | Replacing or rewriting weighs the cost of carrying one's own code. |
| EVOLUTION.INCREMENTAL.4 | OWNERSHIP.LIFECYCLE | realizes | A migration across many consumers has the dependency-update analogue in the lifecycle. |
| EVOLUTION.INCREMENTAL.4 | CHANGE_FLOW.INTEGRATION | see | Sharded mechanical changes stay reviewable and integrable in small units. |
| EVOLUTION.INCREMENTAL.5 | OWNERSHIP.STANCE.4 | realizes | Investment follows expected lifespan, the same stance as not building for presumed needs. |
| EVOLUTION.INCREMENTAL.5 | OWNERSHIP.LIFECYCLE | realizes | Cost of change over the life of what is owned. |
| EVOLUTION.INCREMENTAL.5 | OWNERSHIP.SELECTION | realizes | Lifespan and consumer count bear on what is selected. |
| EVOLUTION.INCREMENTAL.5 | ASSURANCE.CONTRACTS.1 | realizes | Reliance on observable behaviour grows with consumers. |
| EVOLUTION.INCREMENTAL.5 | ASSURANCE.CONTRACTS.2 | realizes | Reliance tests are the mechanism that lets shared infrastructure change. |
| EVOLUTION.DEBT | OWNERSHIP.STANCE | realizes | Debt is the cost-of-lasting-liability stance applied to change. |
| EVOLUTION.DEBT | OWNERSHIP.LIFECYCLE | realizes | Debt includes out-of-date dependencies and the upgrade cycle. |
| EVOLUTION.DEBT | ASSURANCE.BEHAVIOUR | realizes | Refactoring relies on checks that detect a behaviour change. |
| EVOLUTION.DEBT.1 | CHANGE_FLOW.DATA_CHANGE | see | An unfinished data migration is debt. |
| EVOLUTION.DEBT.1 | OWNERSHIP.LIFECYCLE.5 | see | Out-of-date dependencies are debt items. |
| EVOLUTION.DEBT.2 | OWNERSHIP.STANCE | realizes | Taking debt knowingly realizes the cost-of-lasting-liability stance. |
| EVOLUTION.DEBT.3 | OWNERSHIP.LIFECYCLE | realizes | The length of the dependency upgrade cycle is the debt-side view of lifecycle. |
| EVOLUTION.DEBT.3 | CHANGE_FLOW.MEASURE | see | Maintainability signals are measured trends. |
| EVOLUTION.DEBT.4 | ASSURANCE.BEHAVIOUR.5 | realizes | Behaviour not pinned by tests is pinned first, as the characterization rule requires. |
| EVOLUTION.DEBT.4 | ASSURANCE.BEHAVIOUR.1 | realizes | The check that detects a behaviour change is the behaviour check. |
| EVOLUTION.DEBT.4 | CHANGE_FLOW.REVIEW | see | Refactoring changes are reviewed as changes. |
| EVOLUTION.DEBT.5 | CHANGE_FLOW.REVIEW.2 | see | A tidy lands as its own change, as the review practice decides. |
| EVOLUTION.DEBT.5 | OWNERSHIP.LIFECYCLE.3 | see | Risk-carrying debt such as vulnerable dependencies follows the lifecycle rules, not the interest rule. |
| EVOLUTION.DEBT.5 | OWNERSHIP.LIFECYCLE.5 | see | Risk-carrying debt such as end-of-life dependencies follows the lifecycle rules, not the interest rule. |
| EVOLUTION.DECOMMISSION | OWNERSHIP.STANCE | realizes | Retirement carries out the liability stance. |
| EVOLUTION.DECOMMISSION | OWNERSHIP.SERVICES | realizes | Retirement of one's own forms meets the consumer side of services. |
| EVOLUTION.DECOMMISSION | ASSURANCE.CONTRACTS | realizes | Retirement follows the promise made to consumers. |
| EVOLUTION.DECOMMISSION.1 | OWNERSHIP.STANCE | realizes | Code is a liability whose value is its functionality. |
| EVOLUTION.DECOMMISSION.1 | CHANGE_FLOW.DEPLOY | see | Retired code is not left on the production system. |
| EVOLUTION.DECOMMISSION.3 | ASSURANCE.CONTRACTS.1 | realizes | Announcing deprecation and sunset is how the provider-side evolution policy is carried out. |
| EVOLUTION.DECOMMISSION.3 | OWNERSHIP.SERVICES.2 | see | The consumer side reads these signals and routes them to an alert. |
| EVOLUTION.DECOMMISSION.4 | ASSURANCE.CONTRACTS.1 | realizes | The support windows and the indefinitely compatible case are policies by consumer reach. |
| EVOLUTION.DECOMMISSION.4 | OWNERSHIP.SERVICES.2 | see | The consumer side reads the promise and pins the version. |
| EVOLUTION.DECOMMISSION.5 | OWNERSHIP.SERVICES.2 | see | The consumer side sees the deadline of a compulsory retirement. |
| EVOLUTION.DECOMMISSION.6 | OPERATION.RECOVERY.2 | see | Backups kept after retirement follow the backup retention. |
| EVOLUTION.DECOMMISSION.6 | TRANSVERSE.PRIVACY.2 | see | Backups after retirement are kept no longer than the retention periods allow. |
| EVOLUTION.DECOMMISSION.6 | TRANSVERSE.PRIVACY.3 | see | Erased data in a backup of a retired system is put beyond use. |
| EVOLUTION.DECOMMISSION.6 | CHANGE_FLOW.DATA_CHANGE | see | Metadata and data of a retired system are handled as a data change. |
| EVOLUTION.DECOMMISSION.6 | ASSURANCE.DATA_INTEGRITY | see | Backups kept after retirement stay restorable. |
| EVOLUTION.TECHNOLOGY | OWNERSHIP.SELECTION | realizes | Keeping technologies few carries out the selection rule over the whole estate. |
| EVOLUTION.TECHNOLOGY | OWNERSHIP.STANCE | realizes | Keeping technologies few is the stance against building or adding for presumed needs. |
| EVOLUTION.TECHNOLOGY.1 | OWNERSHIP.SELECTION | realizes | The replacement commitment complements the entry test of selection. |
| EVOLUTION.TECHNOLOGY.2 | OWNERSHIP.SELECTION | realizes | The register records the team's position on each selected technology. |
| EVOLUTION.TECHNOLOGY.2 | OWNERSHIP.SELECTION.1 | see | The register is not the sanctioned list of admitted dependencies. |
| EVOLUTION.TECHNOLOGY.2 | OWNERSHIP.LIFECYCLE.5 | see | The register is not the inventory of what is deployed. |
| EVOLUTION.TECHNOLOGY.3 | OWNERSHIP.SELECTION | realizes | The default set is held within the selection default. |
| EVOLUTION.TECHNOLOGY.3 | OWNERSHIP.LIFECYCLE.2 | see | The version choice for each dependency is decided there. |
| EVOLUTION.TECHNOLOGY.3 | CHANGE_FLOW.INTEGRATION.1 | see | One version of each shared component is decided there. |
| EVOLUTION.TECHNOLOGY.4 | OWNERSHIP.STANCE.4 | realizes | A specialised store is not added for presumed needs. |
| EVOLUTION.TECHNOLOGY.4 | OWNERSHIP.SELECTION | realizes | Adding a specialised store passes the entry test of selection. |
