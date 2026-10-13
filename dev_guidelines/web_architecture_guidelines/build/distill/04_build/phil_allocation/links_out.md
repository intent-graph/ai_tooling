# Links touching the ALLOCATION nodes of web-app-philosophy that this batch does not create

The batch creates no link: every link below has an endpoint outside the ALLOCATION branch (another tier branch, the other graph, or the python knowledge-base graph), and the linker adds it once both endpoints exist. Source of every row: the Intentlinks section of the skeleton (`build/distill/02_skeleton/skeleton.md`), under the heading given in the last column. Endpoints are written `graph:uid`.

Count: 71 links.

| src | dst | kind | intent | skeleton section |
|---|---|---|---|---|
| web-app-philosophy:DATA.ORGANIZE | web-app-philosophy:ALLOCATION.RECORD.1 | realizes | holds the durable facts in the form the system-of-record placement gives the database | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:DATA.GUARD | web-app-philosophy:ALLOCATION.GUARD.2 | realizes | enforces the invariants the placement gives the database | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:DATA.GUARD | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | carries the concurrency control the placement gives the database | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:DATA.DERIVE | web-app-philosophy:ALLOCATION.DERIVE.1 | realizes | keeps derived values in the tier and freshness the placement sets | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:DATA.MAINTAIN | web-app-philosophy:ALLOCATION.RECORD.3 | realizes | keeps the database structure as the origin of shapes when the placement makes it the origin | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.SECURE | web-app-philosophy:ALLOCATION.GUARD.1 | realizes | performs the boundary checks the validation placement gives the backend | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.SECURE | web-app-philosophy:ALLOCATION.GUARD.3 | realizes | enforces the access decisions the authorization placement gives the backend | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.SECURE | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | holds sessions and credentials as the identity placement sets | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.ENFORCE | web-app-philosophy:ALLOCATION.ACT.1 | realizes | holds the business rules and transitions the placement gives the backend | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.ENFORCE | web-app-philosophy:ALLOCATION.RULES.4 | requires | one business core serves every client | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.PROCESS | web-app-philosophy:ALLOCATION.GUARD.4 | constrains | stateless processes keep session state in a backing service | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.PROCESS | web-app-philosophy:ALLOCATION.DERIVE.3 | constrains | process memory holds no cache shared beyond one request | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.EXPOSE | web-app-philosophy:ALLOCATION.RECORD.2 | realizes | offers the interface through which consumers reach data when the placement routes them through the backend | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:LOGIC.EXPOSE | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | gives repeated requests safe method semantics | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.VISUALIZE | web-app-philosophy:ALLOCATION.PRESENT.1 | realizes | renders what the rendering placement gives the browser | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.VISUALIZE | web-app-philosophy:ALLOCATION.PRESENT.2 | realizes | formats values for the reader where the placement says | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.COLLABORATE | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | surfaces conflicts with the policy the concurrency placement chose | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.COLLABORATE | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | keeps presence and other ephemeral state where the placement says | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.COLLABORATE | web-app-philosophy:ALLOCATION.GUARD.3 | requires | comment visibility follows the authorization placement | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.AGENT | web-app-philosophy:ALLOCATION.RULES.4 | requires | the agent surface is one more adapter on the same core | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.AGENT | web-app-philosophy:ALLOCATION.GUARD.3 | requires | agents never decide access; the authorization authority does | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.AGENT | web-app-philosophy:ALLOCATION.GUARD.6 | requires | agent retries are absorbed by the duplicate-suppression placement | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.AGENT | web-app-philosophy:ALLOCATION.ACT.4 | requires | agent actions are recorded where the audit placement writes history | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.ENVIRONMENT.7 | web-app-philosophy:ALLOCATION.RULES.3 | constrains | script in the page has the application's privileges, so the browser cannot hold deciding checks | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:INTERACTION.ENVIRONMENT.4 | web-app-philosophy:ALLOCATION.DERIVE.3 | constrains | copies in caches the team does not own cannot be recalled | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:TRANSVERSE.SECURITY | web-app-philosophy:ALLOCATION.RULES.3 | refines | cross-tier security properties rest on the trust-boundary rule | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:TRANSVERSE.PERFORMANCE | web-app-philosophy:ALLOCATION.FORCES.3 | dataflow | field measurement supplies the evidence that performance-driven placements need | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:TRANSVERSE.PERFORMANCE | web-app-philosophy:ALLOCATION.FORCES.4 | dataflow | field measurement supplies the latency evidence placements weigh | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:TRANSVERSE.CONTRACTS | web-app-philosophy:ALLOCATION.RECORD.3 | requires | explicit contracts derive from the origin definition the placement names | Tier to placement, intra `web-app-philosophy` |
| web-app-philosophy:TRANSVERSE.OPERABILITY.1 | web-app-philosophy:ALLOCATION.ACT.4 | conflicts | the security event log and the business audit trail are kept apart | Tier to placement, intra `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.DERIVE.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.POSTGRES_FIRST | web-app-philosophy:ALLOCATION.ACT.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.DB_API | web-app-philosophy:ALLOCATION.RECORD.2 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.TYPE_CHAIN | web-app-philosophy:ALLOCATION.RECORD.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.ROW_SECURITY | web-app-philosophy:ALLOCATION.GUARD.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.JOB_HOST | web-app-philosophy:ALLOCATION.ACT.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.CACHE_STORE | web-app-philosophy:ALLOCATION.DERIVE.3 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION.JS_SERVER | web-app-philosophy:ALLOCATION.PRESENT.1 | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.GUARD.1 | web-app-philosophy:ALLOCATION.GUARD.2 | realizes | declares the invariants the placement gives the database | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.GUARD.4 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | keeps trigger logic within what the business-rules placement allows the database | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.CONCURRENCY | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | implements the concurrency control the placement gives the database | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.CONCURRENCY.4 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | makes mutations idempotent statements | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.CONCURRENCY.6 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | orders state transitions written by their single authoritative writer | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.MAINTAIN.3 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | writes history where the audit placement says | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.MAINTAIN.4 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | runs bulk data work as the deferred-work placement allows | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-DATA.DERIVE.1 | web-app-philosophy:ALLOCATION.DERIVE.1 | realizes | keeps denormalized copies in sync as the placement sets | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.SECURE.2 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | holds sessions as the identity placement sets | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.SECURE.4 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | handles tokens where the identity placement allows them | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.ENFORCE.1 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | holds the use cases the business-rules placement gives the backend | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.ENFORCE.3 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | pushes filtering and aggregation to the tier the placement names | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.PROCESS.2 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | stages and delivers side effects as the placement sets | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.EXPOSE.1 | web-app-philosophy:ALLOCATION.DERIVE.2 | realizes | exposes paging and filtering in the contract | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | expresses idempotency keys in the HTTP contract | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.EXPOSE.3 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | expresses deferred operations in the HTTP contract | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-LOGIC.EXPOSE.6 | web-app-philosophy:ALLOCATION.GUARD.1 | realizes | parses payloads at the boundary the validation placement names | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.VISUALIZE.2 | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | holds client state where the placement says | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | shows conflicts the concurrency placement detects | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | keeps the browser share of duplicate suppression | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.COLLABORATE.3 | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | merges long text where the conflict policy calls for an engine | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.COLLABORATE.4 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | creates and delivers notifications as side effects | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.AGENT.3 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | represents agent identity and delegation as the identity placement sets | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.AGENT.4 | web-app-philosophy:ALLOCATION.GUARD.3 | requires | approval designs never replace the authorization authority | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.ENVIRONMENT.2 | web-app-philosophy:ALLOCATION.RECORD.1 | requires | offline use depends on where the system of record is placed | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-INTERACTION.ENVIRONMENT.3 | web-app-philosophy:ALLOCATION.PRESENT.2 | requires | translation follows the formatting placement | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-TRANSVERSE.OPERABILITY.4 | web-app-philosophy:ALLOCATION.ACT.4 | conflicts | the security event log stays apart from the business audit trail | Inter, `pig-web-defaults` to `web-app-philosophy` |
| pig-web-defaults:PIG-WEB-ALLOCATION | web-app-philosophy:ALLOCATION | refines | (no intent given in the skeleton; kind implied by the table heading) | Inter, `pig-web-defaults` to `web-app-philosophy` |
| web-app-philosophy:ALLOCATION | python-kb-philosophy:POLYGLOT | refines | each responsibility goes to the tier whose paradigm fits it (set work in SQL, flow in the backend, rendering at the edge) | Inter, `web-app-philosophy` to `python-kb-philosophy` |
| web-app-philosophy:ALLOCATION.RULES.1 | python-kb-philosophy:DATACENTRICITY | refines | data is the enduring artifact and has one authority; every other copy is derived | Inter, `web-app-philosophy` to `python-kb-philosophy` |
| web-app-philosophy:ALLOCATION.RULES.3 | python-kb-philosophy:DEFENSIVE | refines | checks that decide run where they cannot be bypassed | Inter, `web-app-philosophy` to `python-kb-philosophy` |
| web-app-philosophy:ALLOCATION.GUARD.1 | python-kb-philosophy:DEFENSIVE | refines | input is checked at the boundary | Inter, `web-app-philosophy` to `python-kb-philosophy` |
| web-app-philosophy:ALLOCATION.GUARD.2 | python-kb-philosophy:DEFENSIVE | refines | invariants fail fast at the data | Inter, `web-app-philosophy` to `python-kb-philosophy` |

The placement records' lines 'Realized or refined by' in the skeleton list the same tier and stack counterparts; no link appears there that the tables lack.
