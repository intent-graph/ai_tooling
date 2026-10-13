# Links touching PIG-WEB-TRANSVERSE nodes, not created by this batch

The batch creates no link: every link below has an endpoint outside the branch (another unit, or the other graph). The tree arcs (parent to child) are created by `node.create` itself.

## Skeleton intentlinks (source: `build/distill/02_skeleton/skeleton.md`, section Intentlinks)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-TRANSVERSE.TOPOLOGY.2 | PIG-WEB-ALLOCATION.JS_SERVER | constrains | a JavaScript server is one more runtime tier beside the Python server | skeleton, "Tier to placement, intra pig-web-defaults"; same pair in the J9 records ("constrains JS_SERVER") |
| PIG-WEB-TRANSVERSE.OPERABILITY.4 | web-app-philosophy:ALLOCATION.ACT.4 | conflicts | the security event log stays apart from the business audit trail | skeleton, "Stack tier nodes realize stack-neutral placements"; J9 records OPERABILITY.4 |
| PIG-WEB-TRANSVERSE | web-app-philosophy:TRANSVERSE | refines | same-branch counterpart | skeleton, "Same-branch counterparts" |
| PIG-WEB-TRANSVERSE.SECURITY | web-app-philosophy:TRANSVERSE.SECURITY | refines | same-branch counterpart | same |
| PIG-WEB-TRANSVERSE.PERFORMANCE | web-app-philosophy:TRANSVERSE.PERFORMANCE | refines | same-branch counterpart | same |
| PIG-WEB-TRANSVERSE.CONTRACTS | web-app-philosophy:TRANSVERSE.CONTRACTS | refines | same-branch counterpart | same |
| PIG-WEB-TRANSVERSE.OPERABILITY | web-app-philosophy:TRANSVERSE.OPERABILITY | refines | same-branch counterpart | same |
| PIG-WEB-TRANSVERSE.TOPOLOGY | web-app-philosophy:LOGIC.PROCESS | refines | same-branch counterpart (runtime topology refines the process model) | same |
| PIG-WEB-TRANSVERSE.EVOLUTION | web-app-philosophy:TRANSVERSE.EVOLUTION | refines | same-branch counterpart | same |

## Relations named in the judge records only (not skeleton intentlinks; for the linker to accept or drop)

Source: J9 `result.md`, table "Placements and philosophy verdicts realized", column "refines (philosophy)". Kind `refines`, dst in `web-app-philosophy`.

| src | dst |
|---|---|
| PIG-WEB-TRANSVERSE.SECURITY.1 to .5 | TRANSVERSE.SECURITY |
| PIG-WEB-TRANSVERSE.CONTRACTS.1, .2 | TRANSVERSE.CONTRACTS |
| PIG-WEB-TRANSVERSE.OPERABILITY.1 | TRANSVERSE.OPERABILITY.1 |
| PIG-WEB-TRANSVERSE.OPERABILITY.2, .3 | TRANSVERSE.OPERABILITY |
| PIG-WEB-TRANSVERSE.OPERABILITY.4 | TRANSVERSE.OPERABILITY.1 |
| PIG-WEB-TRANSVERSE.OPERABILITY.5 | TRANSVERSE.OPERABILITY.2 |
| PIG-WEB-TRANSVERSE.OPERABILITY.6 | TRANSVERSE.OPERABILITY.3 |
| PIG-WEB-TRANSVERSE.TOPOLOGY.1 to .4 | LOGIC.PROCESS |
| PIG-WEB-TRANSVERSE.EVOLUTION.1 | TRANSVERSE.EVOLUTION.3 |
| PIG-WEB-TRANSVERSE.EVOLUTION.2 | TRANSVERSE.EVOLUTION.2, TRANSVERSE.EVOLUTION.3, TRANSVERSE.EVOLUTION.5 |
| PIG-WEB-TRANSVERSE.EVOLUTION.3 | TRANSVERSE.EVOLUTION.1 |

The records also name "rests on" dependencies (placements and other stack nodes, for example GUARD.3, RECORD.2, DB_API, TYPE_CHAIN, ACT.1). They are citations, not decided links, and are not listed.
