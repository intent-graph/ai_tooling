# Links touching this branch that the batch does not create

Source of all rows: `build/distill/02_skeleton/skeleton.md`, section "Intentlinks". The batch creates no link: the skeleton gives none whose two endpoints are both inside this branch. Kinds as in the skeleton.

## Tier node to placement, within `pig-web-defaults` (other endpoint is created by another unit)

Section "Tier to placement, intra `pig-web-defaults`".

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB-DATA.INTERFACE.1 | PIG-WEB-ALLOCATION.DB_API | realizes | writes the functions and views the database API placement calls for |
| PIG-WEB-DATA.ORGANIZE | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | supplies the schema the type chain starts from or follows |
| PIG-WEB-LOGIC.EXPOSE.6 | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | publishes payload schemas in the place the type chain assigns |
| PIG-WEB-DATA.GUARD.3 | PIG-WEB-ALLOCATION.ROW_SECURITY | realizes | writes the row policies the placement calls for |
| PIG-WEB-LOGIC.SECURE.1 | PIG-WEB-ALLOCATION.ROW_SECURITY | realizes | keeps or drops backend checks as the placement sets |
| PIG-WEB-LOGIC.PROCESS.1 | PIG-WEB-ALLOCATION.JOB_HOST | realizes | runs jobs and schedules on the host the placement names |
| PIG-WEB-DATA.DERIVE.2 | PIG-WEB-ALLOCATION.CACHE_STORE | realizes | holds cache tables when the placement keeps caches in Postgres |
| PIG-WEB-LOGIC.EXPOSE.4 | PIG-WEB-ALLOCATION.CACHE_STORE | realizes | uses the cache store the placement names |
| PIG-WEB-INTERACTION.VISUALIZE.1 | PIG-WEB-ALLOCATION.JS_SERVER | realizes | renders with or without a JavaScript server as the placement sets |
| PIG-WEB-TRANSVERSE.TOPOLOGY.2 | PIG-WEB-ALLOCATION.JS_SERVER | constrains | a JavaScript server is one more runtime tier beside the Python server |
| PIG-WEB-INTERACTION.REALTIME.5 | PIG-WEB-ALLOCATION.POSTGRES_FIRST | requires | database notifications as wake-up depend on Postgres carrying the notification role |

## Inter-graph, `pig-web-defaults` to `web-app-philosophy` (kind `refines`; the skeleton gives no intent text)

Section "Inter, `pig-web-defaults` to `web-app-philosophy`".

| src | dst | kind |
|---|---|---|
| PIG-WEB-ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.DERIVE.3 | refines |
| PIG-WEB-ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.ACT.3 | refines |
| PIG-WEB-ALLOCATION.DB_API | web-app-philosophy:ALLOCATION.RECORD.2 | refines |
| PIG-WEB-ALLOCATION.TYPE_CHAIN | web-app-philosophy:ALLOCATION.RECORD.3 | refines |
| PIG-WEB-ALLOCATION.ROW_SECURITY | web-app-philosophy:ALLOCATION.GUARD.3 | refines |
| PIG-WEB-ALLOCATION.JOB_HOST | web-app-philosophy:ALLOCATION.ACT.3 | refines |
| PIG-WEB-ALLOCATION.CACHE_STORE | web-app-philosophy:ALLOCATION.DERIVE.3 | refines |
| PIG-WEB-ALLOCATION.JS_SERVER | web-app-philosophy:ALLOCATION.PRESENT.1 | refines |
| PIG-WEB-ALLOCATION | web-app-philosophy:ALLOCATION | refines |

Stack tier nodes that realize philosophy placements (not mine) are not listed: they do not touch this branch.
