# PIG-WEB-LOGIC: links not created by the batch

The batch creates 0 links: every link the skeleton gives for this branch has an endpoint outside the nodes the batch creates (placements in `PIG-WEB-ALLOCATION`, or nodes in `web-app-philosophy`). The branch's L1 node is created under `pig-web-defaults:ROOT` by tree parentage, not by an intentlink. For the linker, after all batches are applied.

Source of each link: `build/distill/02_skeleton/skeleton.md`, sections "Tier to placement, intra `pig-web-defaults`" (A), "Inter, `pig-web-defaults` to `web-app-philosophy`: stack tier nodes realize stack-neutral placements" (B), "Same-branch counterparts" (C); or `build/distill/03_judge/J7_pig_logic/result.md`, "Proposed intentlinks" (D, not in the skeleton, proposed by the judge).

## A. Intra `pig-web-defaults`

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-LOGIC.EXPOSE.6 | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | publishes payload schemas in the place the type chain assigns | A |
| PIG-WEB-LOGIC.SECURE.1 | PIG-WEB-ALLOCATION.ROW_SECURITY | realizes | keeps or drops backend checks as the placement sets | A |
| PIG-WEB-LOGIC.PROCESS.1 | PIG-WEB-ALLOCATION.JOB_HOST | realizes | runs jobs and schedules on the host the placement names | A |
| PIG-WEB-LOGIC.EXPOSE.4 | PIG-WEB-ALLOCATION.CACHE_STORE | realizes | uses the cache store the placement names | A |

## B. To `web-app-philosophy` (placements)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-LOGIC.SECURE.2 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | holds sessions as the identity placement sets | B |
| PIG-WEB-LOGIC.SECURE.4 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | handles tokens where the identity placement allows them | B |
| PIG-WEB-LOGIC.ENFORCE.1 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | holds the use cases the business-rules placement gives the backend | B |
| PIG-WEB-LOGIC.ENFORCE.3 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | pushes filtering and aggregation to the tier the placement names | B |
| PIG-WEB-LOGIC.PROCESS.2 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | stages and delivers side effects as the placement sets | B |
| PIG-WEB-LOGIC.EXPOSE.1 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | exposes paging and filtering in the contract | B |
| PIG-WEB-LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | expresses idempotency keys in the HTTP contract | B |
| PIG-WEB-LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | expresses deferred operations in the HTTP contract | B |
| PIG-WEB-LOGIC.EXPOSE.6 | web-app-philosophy:ALLOCATION.GUARD.1 | realizes | parses payloads at the boundary the validation placement names | B |

## C. Same-branch counterparts in `web-app-philosophy` (kind `refines`; the skeleton gives no intent text)

| src | dst | kind | intent (suggested) | source |
|---|---|---|---|---|
| PIG-WEB-LOGIC | web-app-philosophy:LOGIC | refines | the Python backend realizes the stack-neutral logic tier | C |
| PIG-WEB-LOGIC.SECURE | web-app-philosophy:LOGIC.SECURE | refines | backend security realizes the stack-neutral security role | C |
| PIG-WEB-LOGIC.ENFORCE | web-app-philosophy:LOGIC.ENFORCE | refines | business-logic realization refines the stack-neutral enforcement role | C |
| PIG-WEB-LOGIC.PROCESS | web-app-philosophy:LOGIC.PROCESS | refines | processing and side effects refine the stack-neutral process role | C |
| PIG-WEB-LOGIC.EXPOSE | web-app-philosophy:LOGIC.EXPOSE | refines | the HTTP interface refines the stack-neutral exposure role | C |

## D. Proposed by the judge (not in the skeleton; for the linker to accept or drop)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-LOGIC.SECURE.1 | web-app-philosophy:ALLOCATION.GUARD.3 | realizes | the backend's share of authorization | D |
| PIG-WEB-LOGIC.ENFORCE.2 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | one operation, one call, one transaction | D |
| PIG-WEB-LOGIC.PROCESS.5 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | the upload state has one writer function | D |
| PIG-WEB-LOGIC.EXPOSE.7 | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | the always-in-sync gate of MD-02 | D |
| PIG-WEB-LOGIC.PROCESS.2 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | foreign effects deferred to a worker | D |

## Links with a node of this branch as destination

None in the skeleton.
