# J1_ownership: cross links for the linker

Links with one endpoint outside J1_ownership. Source uid, target uid, link type (all `related`, the type used by the skeleton and the judge records), one-line intent sentence. Each follows a Links line of the judge record or a cross-unit line of `03_judge/cross_unit_fixes.md`. Targets outside J1 are named as the judge records name them; the linker confirms each uid exists in the graph after all batches are applied. Links whose other endpoint is the L1 node (`OWNERSHIP` realized by `EVOLUTION`, `CHANGE_FLOW`, `TRANSVERSE.CONFIG`) belong to the TOP batch, not here.

| # | Source uid | Target uid | Type | Intent sentence |
|---|---|---|---|---|
| 1 | OWNERSHIP.STANCE.4 | EVOLUTION.INCREMENTAL | related | Building for today and making change cheap is the same practice as incremental change. |
| 2 | CONSTRUCTION.DESIGN | OWNERSHIP.STANCE.4 | related | Design for probable use only where a structural choice is costly to reverse; the rule is held in STANCE.4 (L330). |
| 3 | OWNERSHIP.SELECTION.1 | EVOLUTION.DECISIONS | related | The written reason for each selection is stored as a decision record. |
| 4 | OWNERSHIP.LIFECYCLE.3 | EVOLUTION.DEBT | related | Updating on need because verification is weak is recorded as debt to repay. |
| 5 | OWNERSHIP.LIFECYCLE.3 | TRANSVERSE.CONFIG.6 | related | After a supply-chain compromise, revocation, rotation and investigation of exposed credentials are held there (X10). |
| 6 | OWNERSHIP.CONTAINMENT.2 | CONSTRUCTION.BOUNDARY | related | Converting external input to a precise type is held there; the wrapper keeps foreign types out of the team's interface. |
| 7 | OWNERSHIP.CONTAINMENT.3 | TRANSVERSE.CONFIG | related | Where configuration of a backing service lives is decided there, not here. |
| 8 | OWNERSHIP.SERVICES.1 | ASSURANCE.AVAILABILITY | related | The mechanisms that guarantee availability sit there; this node holds only what to require when renting. |
| 9 | OWNERSHIP.SERVICES.1 | OPERATION | related | The monitoring practice for a service's reachability, latency and errors sits there. |
| 10 | OWNERSHIP.SERVICES.2 | ASSURANCE.CONTRACTS.1 | related | Which evolution policy a provider follows, and when each is best, is held there (X7). |
| 11 | OWNERSHIP.SERVICES.3 | OPERATION.RECOVERY | related | Recovery practice for data held in a service is held there. |

Inbound links named by cross-unit lines, owned by other units (listed so the linker does not miss the J1 endpoint):

| Source uid | Target uid | Type | Intent sentence | Origin |
|---|---|---|---|---|
| EVOLUTION.DECOMMISSION.3 | OWNERSHIP.SERVICES.2 | related | See the consumer side of API stability and deprecation (changed from "realizes" to "see"). | X7 |
| EVOLUTION.DECOMMISSION.5 | OWNERSHIP.SERVICES.2 | related | See the consumer side of API stability and deprecation (changed from "realizes" to "see"). | X7 |
