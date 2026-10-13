# Links touching PIG-WEB-INTERACTION nodes, not created by the batch

The batch holds 0 `link.create`: no skeleton intentlink and no judge-record link has both endpoints inside this unit. Every link below has one endpoint outside it, so the linker creates it. `PIG-WEB-ALLOCATION.*` nodes are in the same graph (`pig-web-defaults`); `web-app-philosophy:` nodes are in the other graph. Kinds and intents of the skeleton links are the skeleton's; "records" links are proposed by the judge record and marked as such there.

## Skeleton links, intra-graph (pig-web-defaults)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-INTERACTION.VISUALIZE.1 | PIG-WEB-ALLOCATION.JS_SERVER | realizes | renders with or without a JavaScript server as the placement sets | skeleton, intra-graph links |
| PIG-WEB-INTERACTION.REALTIME.5 | PIG-WEB-ALLOCATION.POSTGRES_FIRST | requires | database notifications as wake-up depend on Postgres carrying the notification role | skeleton, intra-graph links |

## Skeleton links, inter-graph (to web-app-philosophy)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| PIG-WEB-INTERACTION.VISUALIZE.2 | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | holds client state where the placement says | skeleton, inter-graph links |
| PIG-WEB-INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | shows conflicts the concurrency placement detects | skeleton |
| PIG-WEB-INTERACTION.EDIT | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | keeps the browser share of duplicate suppression | skeleton |
| PIG-WEB-INTERACTION.COLLABORATE.3 | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | merges long text where the conflict policy calls for an engine | skeleton |
| PIG-WEB-INTERACTION.COLLABORATE.4 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | creates and delivers notifications as side effects | skeleton |
| PIG-WEB-INTERACTION.AGENT.3 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | represents agent identity and delegation as the identity placement sets | skeleton |
| PIG-WEB-INTERACTION.AGENT.4 | web-app-philosophy:ALLOCATION.GUARD.3 | requires | approval designs never replace the authorization authority | skeleton |
| PIG-WEB-INTERACTION.ENVIRONMENT.2 | web-app-philosophy:ALLOCATION.RECORD.1 | requires | offline use depends on where the system of record is placed | skeleton (deferred node) |
| PIG-WEB-INTERACTION.ENVIRONMENT.3 | web-app-philosophy:ALLOCATION.PRESENT.2 | requires | translation follows the formatting placement | skeleton (deferred node) |

## Skeleton links, same-branch counterparts (kind refines, to web-app-philosophy)

| src | dst |
|---|---|
| PIG-WEB-INTERACTION | web-app-philosophy:INTERACTION |
| PIG-WEB-INTERACTION.VISUALIZE | web-app-philosophy:INTERACTION.VISUALIZE |
| PIG-WEB-INTERACTION.REALTIME | web-app-philosophy:INTERACTION.COLLABORATE |
| PIG-WEB-INTERACTION.COLLABORATE | web-app-philosophy:INTERACTION.COLLABORATE |
| PIG-WEB-INTERACTION.AGENT | web-app-philosophy:INTERACTION.AGENT |
| PIG-WEB-INTERACTION.ENVIRONMENT | web-app-philosophy:INTERACTION.ENVIRONMENT |

## Links proposed by the judge records (the "Realizes" lines), not in the skeleton

All sources are `build/distill/03_judge/J8_pig_interaction/records.md`, the node's "Realizes" line. Kind is `realizes` unless stated. The linker decides whether to create each; the skeleton did not draw them.

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB-INTERACTION.VISUALIZE.1 | web-app-philosophy:ALLOCATION.PRESENT.1 | realizes | HTML from the backend, islands only under the rendering placement's criteria |
| PIG-WEB-INTERACTION.VISUALIZE.2 | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | an island keeps the version it read so a write carries it |
| PIG-WEB-INTERACTION.VISUALIZE.2 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | no credentials in script-readable browser storage |
| PIG-WEB-INTERACTION.VISUALIZE.3 | web-app-philosophy:ALLOCATION.FORCES.4 | realizes | page techniques serve the latency force |
| PIG-WEB-INTERACTION.VISUALIZE.4 | web-app-philosophy:ALLOCATION.PRESENT.1 | realizes | native semantics come from server-rendered HTML |
| PIG-WEB-INTERACTION.EDIT | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | drafts and in-progress input live in the browser |
| PIG-WEB-INTERACTION.REALTIME.1 | PIG-WEB-ALLOCATION.POSTGRES_FIRST | realizes | no Redis by default; fan-out starts from a Postgres wake-up |
| PIG-WEB-INTERACTION.REALTIME.3 | PIG-WEB-ALLOCATION.POSTGRES_FIRST | realizes | Postgres carries the wake-up role until a measured limit |
| PIG-WEB-INTERACTION.REALTIME.3 | web-app-philosophy:ALLOCATION.RECORD.1 | realizes | the table is the source, push a copy |
| PIG-WEB-INTERACTION.REALTIME.4 | web-app-philosophy:ALLOCATION.GUARD.3 | requires | per-subscriber filtering follows the authorization placement, its open read clause included |
| PIG-WEB-INTERACTION.REALTIME.4 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | the session cookie authenticates the channel |
| PIG-WEB-INTERACTION.REALTIME.5 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | the staged intent in the function's transaction, delivered after commit |
| PIG-WEB-INTERACTION.COLLABORATE.1 | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | reuses the version every user-edited record carries |
| PIG-WEB-INTERACTION.COLLABORATE.1 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | reuses the history written with every change |
| PIG-WEB-INTERACTION.COLLABORATE.1 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | a comment is written by one writer function |
| PIG-WEB-INTERACTION.COLLABORATE.2 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | revisions are history written in the same transaction |
| PIG-WEB-INTERACTION.COLLABORATE.2 | web-app-philosophy:ALLOCATION.GUARD.3 | realizes | the resolve right follows the authorization placement |
| PIG-WEB-INTERACTION.COLLABORATE.3 | web-app-philosophy:ALLOCATION.RECORD.1 | realizes | the server stays the authority for shared text |
| PIG-WEB-INTERACTION.COLLABORATE.3 | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | presence on the real-time channel, never in tables |
| PIG-WEB-INTERACTION.COLLABORATE.4 | web-app-philosophy:ALLOCATION.GUARD.3 | requires | recipient visibility, open read clause included |
| PIG-WEB-INTERACTION.COLLABORATE.4 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | moderation history |
| PIG-WEB-INTERACTION.AGENT.1 | web-app-philosophy:ALLOCATION.RULES.4 | realizes | the agent adapter is one more adapter on the same core |
| PIG-WEB-INTERACTION.AGENT.1 | web-app-philosophy:ALLOCATION.RECORD.3 | realizes | the interface description is always in sync (MD-02) |
| PIG-WEB-INTERACTION.AGENT.1 | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | the description and the tool surface have one origin per project (MD-02) |
| PIG-WEB-INTERACTION.AGENT.2 | web-app-philosophy:ALLOCATION.GUARD.4 | realizes | agents hold their own revocable credentials |
| PIG-WEB-INTERACTION.AGENT.3 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | both identities in the audit |
| PIG-WEB-INTERACTION.AGENT.3 | web-app-philosophy:ALLOCATION.GUARD.3 | realizes | the actor assertion in the transaction |
| PIG-WEB-INTERACTION.AGENT.4 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | the effect's writer function checks the approval |
| PIG-WEB-INTERACTION.AGENT.5 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | rate-limited retries carry idempotency keys |
| PIG-WEB-INTERACTION.ENVIRONMENT.1 | web-app-philosophy:ALLOCATION.PRESENT.3 | realizes | in-progress state lives in the browser |

## Citations of philosophy-graph nodes in the records (informational)

The records' "Realizes" lines also cite the J4 verdicts on `web-app-philosophy:INTERACTION.*` (VISUALIZE, COLLABORATE, AGENT, ENVIRONMENT.1, .2, .3, .5, .6, .7); the node-level `refines` counterparts above carry them. Sub-node J4 citations (for example ENVIRONMENT.7 from REALTIME.4) are not proposed as links.

## Prose references to other pig-web nodes (hand-offs, not links)

The "Hand-offs" lines name nodes of PIG-WEB-DATA, LOGIC and TRANSVERSE (for example DATA.CONCURRENCY.2 and .5, LOGIC.EXPOSE.2, TRANSVERSE.OPERABILITY.3). They are responsibilities passed on, recorded in `design_notes`; the records do not propose them as links.
