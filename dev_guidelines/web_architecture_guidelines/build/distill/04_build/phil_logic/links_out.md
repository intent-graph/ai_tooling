# phil_logic: links touching the LOGIC nodes that this batch does not create

The batch creates no link: every skeleton link of the LOGIC branch has its other endpoint outside the branch (a placement, a PIG-WEB node or a python-kb-philosophy node). Source of each: `build/distill/02_skeleton/skeleton.md`, section Intentlinks, unless marked otherwise. Philosophy uids are bare; other graphs are prefixed.

## Tier to placement, intra `web-app-philosophy` (kind, intent from the skeleton)

| src | dst | kind | intent |
|---|---|---|---|
| LOGIC.SECURE | ALLOCATION.GUARD.1 | realizes | performs the boundary checks the validation placement gives the backend |
| LOGIC.SECURE | ALLOCATION.GUARD.3 | realizes | enforces the access decisions the authorization placement gives the backend |
| LOGIC.SECURE | ALLOCATION.GUARD.4 | realizes | holds sessions and credentials as the identity placement sets |
| LOGIC.ENFORCE | ALLOCATION.ACT.1 | realizes | holds the business rules and transitions the placement gives the backend |
| LOGIC.ENFORCE | ALLOCATION.RULES.4 | requires | one business core serves every client |
| LOGIC.PROCESS | ALLOCATION.GUARD.4 | constrains | stateless processes keep session state in a backing service |
| LOGIC.PROCESS | ALLOCATION.DERIVE.3 | constrains | process memory holds no cache shared beyond one request |
| LOGIC.EXPOSE | ALLOCATION.RECORD.2 | realizes | offers the interface through which consumers reach data when the placement routes them through the backend (judge note: the text predates MD-03; under MD-03 the backend interface is the route for browsers and agents, and for an outside consumer needing deploys independent of the database; the intent text could say so) |
| LOGIC.EXPOSE | ALLOCATION.GUARD.6 | realizes | gives repeated requests safe method semantics |

## To another graph

| src | dst | kind | intent | source |
|---|---|---|---|---|
| LOGIC.EXPOSE | python-kb-philosophy:COMMUNICATION | refines | the interface is designed for its readers | skeleton, Inter `web-app-philosophy` to `python-kb-philosophy` |

## From `pig-web-defaults` (kind refines, same-branch counterparts; intent not given by the skeleton)

| src | dst | source |
|---|---|---|
| PIG-WEB-LOGIC | web-app-philosophy:LOGIC | skeleton, Inter `pig-web-defaults` to `web-app-philosophy` |
| PIG-WEB-LOGIC.SECURE | web-app-philosophy:LOGIC.SECURE | same |
| PIG-WEB-LOGIC.ENFORCE | web-app-philosophy:LOGIC.ENFORCE | same |
| PIG-WEB-LOGIC.PROCESS | web-app-philosophy:LOGIC.PROCESS | same |
| PIG-WEB-LOGIC.EXPOSE | web-app-philosophy:LOGIC.EXPOSE | same |
| PIG-WEB-TRANSVERSE.TOPOLOGY | web-app-philosophy:LOGIC.PROCESS | same (topology refines the process model) |

## Proposed by the judge, not in the skeleton (for the linker to decide)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| LOGIC.PROCESS | ALLOCATION.ACT.2 | realizes | the backend delivers side effects from the outbox | judge result, Notes for the graph builder |
| LOGIC.PROCESS | ALLOCATION.ACT.3 | realizes | workers execute deferred work | same |

LOGIC.EXPOSE.2 and LOGIC.EXPOSE.3 have no skeleton link; their records name the placements they follow (GUARD.4; PRESENT.1, RECORD.3), recorded in design_notes only.
