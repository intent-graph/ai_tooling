# Links touching the INTERACTION nodes, not created by this batch

The batch creates no link: every link below has an endpoint outside this unit (placements, TRANSVERSE, pig-web graph). For the linker. Kinds are the skeleton's.

## Skeleton, tier to placement, intra `web-app-philosophy` (source: `build/distill/02_skeleton/skeleton.md`, table "Tier to placement")

| src | dst | kind | intent |
|---|---|---|---|
| INTERACTION.VISUALIZE | ALLOCATION.PRESENT.1 | realizes | renders what the rendering placement gives the browser |
| INTERACTION.VISUALIZE | ALLOCATION.PRESENT.2 | realizes | formats values for the reader where the placement says |
| INTERACTION.COLLABORATE | ALLOCATION.GUARD.5 | realizes | surfaces conflicts with the policy the concurrency placement chose |
| INTERACTION.COLLABORATE | ALLOCATION.PRESENT.3 | realizes | keeps presence and other ephemeral state where the placement says |
| INTERACTION.COLLABORATE | ALLOCATION.GUARD.3 | requires | comment visibility follows the authorization placement |
| INTERACTION.AGENT | ALLOCATION.RULES.4 | requires | the agent surface is one more adapter on the same core |
| INTERACTION.AGENT | ALLOCATION.GUARD.3 | requires | agents never decide access; the authorization authority does |
| INTERACTION.AGENT | ALLOCATION.GUARD.6 | requires | agent retries are absorbed by the duplicate-suppression placement |
| INTERACTION.AGENT | ALLOCATION.ACT.4 | requires | agent actions are recorded where the audit placement writes history |
| INTERACTION.ENVIRONMENT.7 | ALLOCATION.RULES.3 | constrains | script in the page has the application's privileges, so the browser cannot hold deciding checks |
| INTERACTION.ENVIRONMENT.4 | ALLOCATION.DERIVE.3 | constrains | copies in caches the team does not own cannot be recalled |
| INTERACTION.ENVIRONMENT.3 | TRANSVERSE.CONTRACTS | requires | version skew between client and server needs compatible contract evolution |

## Proposed by the judge beyond the skeleton (inferred; source: `build/distill/03_judge/J4_phil_interaction/records.md`, "Realizes" of each node, and `result.md` L2)

| src | dst | kind | intent |
|---|---|---|---|
| INTERACTION.ENVIRONMENT.2 | ALLOCATION.PRESENT.3 | realizes | in-progress state in the browser, durable state in the database |
| INTERACTION.ENVIRONMENT.2 | ALLOCATION.GUARD.5 | realizes | the server arbitrates concurrent writes across tabs |
| INTERACTION.ENVIRONMENT.2 | ALLOCATION.GUARD.6 | realizes | background work repeated by several tabs is absorbed by the keys |
| INTERACTION.ENVIRONMENT.5 | ALLOCATION.GUARD.6 | requires | safe retries depend on the duplicate-suppression placement |
| INTERACTION.ENVIRONMENT.6 | ALLOCATION.PRESENT.3 | realizes | the URL is the authority for shareable view state |
| INTERACTION.ENVIRONMENT.7 | ALLOCATION.GUARD.4 | realizes | credentials are kept out of script reach |

The kind of the proposed links is not stated by the judge beyond "realizes" for the first, second, third, fifth, sixth rows (records, Realizes lines); ENVIRONMENT.5 to GUARD.6 is written "safe retries depend on" (read as requires).

## Roll-up INTERACTION: records list "Realizes, through its children" (no separate link; the children carry them)

## Cross-graph counterparts, kind `refines` (source: skeleton, "Same-branch counterparts")

| src (pig-web-defaults) | dst (web-app-philosophy) |
|---|---|
| PIG-WEB-INTERACTION | INTERACTION |
| PIG-WEB-INTERACTION.VISUALIZE | INTERACTION.VISUALIZE |
| PIG-WEB-INTERACTION.REALTIME | INTERACTION.COLLABORATE |
| PIG-WEB-INTERACTION.COLLABORATE | INTERACTION.COLLABORATE |
| PIG-WEB-INTERACTION.AGENT | INTERACTION.AGENT |
| PIG-WEB-INTERACTION.ENVIRONMENT | INTERACTION.ENVIRONMENT |
