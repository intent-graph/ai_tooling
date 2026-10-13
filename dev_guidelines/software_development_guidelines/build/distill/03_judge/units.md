# Judge units and order

Each unit covers the listed L2 nodes and every L3 node below them, plus, for the first unit of a
branch, the L1 node itself. Records are in `02_skeleton/branches/<BRANCH>/branch.md`.

## Wave 1: decision branches (in parallel)

| Unit | Branch | L2 nodes |
|---|---|---|
| `J1_ownership` | OWNERSHIP | STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES, LICENCE |
| `J2_assurance_core` | ASSURANCE | RULES, BEHAVIOUR, CONTRACTS |
| `J3_assurance_integrity` | ASSURANCE | DATA_INTEGRITY, DOCS_SYNC, SECURITY |
| `J4_assurance_runtime` | ASSURANCE | PERFORMANCE, AVAILABILITY, ARTIFACT |

`J2_assurance_core` also judges the L1 node ASSURANCE; `J1_ownership` the L1 node OWNERSHIP.

## Wave 2: realization branches (in parallel, after wave 1 and its reviews)

Each reads the wave-1 `judged.md` of the decision nodes its nodes `Realize`.

| Unit | Branch | L2 nodes | Reads decided units |
|---|---|---|---|
| `J5_construction` | CONSTRUCTION | all ten | J2, J3 |
| `J6_change_flow` | CHANGE_FLOW | all eight | J2, J3, J4 |
| `J7_operation` | OPERATION | all nine | J4, J3 |
| `J8_evolution` | EVOLUTION | all five | J1, J2 |
| `J9_transverse` | TRANSVERSE | all six | J3 |

## Wave 3: roll-up and final pass

- The ROOT node and the L1 intents of the realization branches, rolled up from their judged
  children.
- The Opus pass on every `flag` finding of every review (MD-06).
