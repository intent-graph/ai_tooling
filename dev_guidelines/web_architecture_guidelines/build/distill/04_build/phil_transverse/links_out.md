# Links touching the TRANSVERSE nodes of web-app-philosophy that this batch does not create

The batch creates 0 links: every link below has an endpoint outside the 14 nodes (and none joins two of them or one of them to the root). Source for all rows: `build/distill/02_skeleton/skeleton.md`, section Intentlinks, unless stated.

## Within web-app-philosophy (dst created by another unit)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| TRANSVERSE.SECURITY | ALLOCATION.RULES.3 | refines | cross-tier security properties rest on the trust-boundary rule | skeleton, Tier to placement intra web-app-philosophy |
| TRANSVERSE.PERFORMANCE | ALLOCATION.FORCES.3 | dataflow | field measurement supplies the evidence that performance-driven placements need | same |
| TRANSVERSE.PERFORMANCE | ALLOCATION.FORCES.4 | dataflow | field measurement supplies the latency evidence placements weigh | same |
| TRANSVERSE.CONTRACTS | ALLOCATION.RECORD.3 | requires | explicit contracts derive from the origin definition the placement names | same |
| TRANSVERSE.OPERABILITY.1 | ALLOCATION.ACT.4 | conflicts | the security event log and the business audit trail are kept apart | same |
| INTERACTION.ENVIRONMENT.3 | TRANSVERSE.CONTRACTS | requires | version skew between client and server needs compatible contract evolution | same (src belongs to the INTERACTION unit) |

## From pig-web-defaults (inter-graph, `refines`: stack node refines the philosophy node)

| src | dst | kind | source |
|---|---|---|---|
| PIG-WEB-TRANSVERSE | web-app-philosophy:TRANSVERSE | refines | skeleton, Inter pig-web-defaults to web-app-philosophy |
| PIG-WEB-TRANSVERSE.SECURITY | web-app-philosophy:TRANSVERSE.SECURITY | refines | same |
| PIG-WEB-TRANSVERSE.PERFORMANCE | web-app-philosophy:TRANSVERSE.PERFORMANCE | refines | same |
| PIG-WEB-TRANSVERSE.CONTRACTS | web-app-philosophy:TRANSVERSE.CONTRACTS | refines | same |
| PIG-WEB-TRANSVERSE.OPERABILITY | web-app-philosophy:TRANSVERSE.OPERABILITY | refines | same |
| PIG-WEB-TRANSVERSE.EVOLUTION | web-app-philosophy:TRANSVERSE.EVOLUTION | refines | same |

## To python-kb-philosophy (inter-graph)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| TRANSVERSE.CONTRACTS | python-kb-philosophy:COMMUNICATION | refines | contracts are explicit, readable artifacts | skeleton, Inter web-app-philosophy to python-kb-philosophy |
| TRANSVERSE.OPERABILITY.2 | python-kb-philosophy:DEFENSIVE | refines | tests catch failures at the lowest level | same |
| TRANSVERSE.OPERABILITY.3 | python-kb-philosophy:REPRODUCIBILITY | refines | one build promoted through every environment | same |
| TRANSVERSE.EVOLUTION.1 | python-kb-philosophy:INTENTIONALITY | refines | the costly decisions are named and recorded with their reasons | same |
| TRANSVERSE.EVOLUTION.2 | python-kb-philosophy:ROUGHTOFINE | refines | the system grows from a thin whole in increments | same |
| TRANSVERSE.EVOLUTION.4 | python-kb-philosophy:POLYGLOT | conflicts | few technologies on purpose, against the right paradigm per problem | same |

## Not links in the skeleton, noted by the judge records (for the linker's judgment, not required)

- Realized-by cross-references in the judge records (no skeleton link): TRANSVERSE.OPERABILITY.2 rests on FORCES.6, GUARD.2, GUARD.3, ACT.1, ACT.4; TRANSVERSE.OPERABILITY.3 on RECORD.2, RECORD.3; TRANSVERSE.EVOLUTION.1 on the allocation placements; TRANSVERSE.EVOLUTION.3 on RECORD.1, RECORD.2; TRANSVERSE.EVOLUTION.4 on PIG-WEB-ALLOCATION.POSTGRES_FIRST, CACHE_STORE, JOB_HOST; TRANSVERSE.EVOLUTION.5 on RECORD.2, ACT.1. These are cited in each node's design_notes only.
- The skeleton's placement records list the same inbound links for ALLOCATION.RECORD.3 (from TRANSVERSE.CONTRACTS) and ALLOCATION.ACT.4 (from TRANSVERSE.OPERABILITY.1); they are the rows above.
