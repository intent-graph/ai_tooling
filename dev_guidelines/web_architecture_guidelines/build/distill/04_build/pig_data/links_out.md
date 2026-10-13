# Links touching the PIG-WEB-DATA nodes, not created by this batch

The batch creates 36 nodes and 0 intentlinks: no skeleton intentlink has both endpoints inside the unit (or at the root). All links below are for the linker.
Notation: `pig-web-defaults` nodes are bare `PIG-WEB.*` uids; nodes of the philosophy graph are written `web-app-philosophy:<uid>`.

## A. Intra `pig-web-defaults` (tier to placement), source: skeleton.md, "Tier to placement, intra pig-web-defaults"

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB-DATA.INTERFACE.1 | PIG-WEB-ALLOCATION.DB_API | realizes | writes the functions and views the database API placement calls for |
| PIG-WEB-DATA.ORGANIZE | PIG-WEB-ALLOCATION.TYPE_CHAIN | realizes | supplies the schema the type chain starts from or follows |
| PIG-WEB-DATA.GUARD.3 | PIG-WEB-ALLOCATION.ROW_SECURITY | realizes | writes the row policies the placement calls for |
| PIG-WEB-DATA.DERIVE.2 | PIG-WEB-ALLOCATION.CACHE_STORE | realizes | holds cache tables when the placement keeps caches in Postgres |

## B. Inter, `pig-web-defaults` to `web-app-philosophy`, stack tier realizes a stack-neutral placement; source: skeleton.md, "Stack tier nodes realize stack-neutral placements"

| src | dst | kind | intent |
|---|---|---|---|
| PIG-WEB-DATA.GUARD.1 | web-app-philosophy:ALLOCATION.GUARD.2 | realizes | declares the invariants the placement gives the database |
| PIG-WEB-DATA.GUARD.4 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | keeps trigger logic within what the business-rules placement allows the database |
| PIG-WEB-DATA.CONCURRENCY | web-app-philosophy:ALLOCATION.GUARD.5 | realizes | implements the concurrency control the placement gives the database |
| PIG-WEB-DATA.CONCURRENCY.4 | web-app-philosophy:ALLOCATION.GUARD.6 | realizes | makes mutations idempotent statements |
| PIG-WEB-DATA.CONCURRENCY.6 | web-app-philosophy:ALLOCATION.ACT.1 | realizes | orders state transitions written by their single authoritative writer |
| PIG-WEB-DATA.MAINTAIN.3 | web-app-philosophy:ALLOCATION.ACT.4 | realizes | writes history where the audit placement says |
| PIG-WEB-DATA.MAINTAIN.4 | web-app-philosophy:ALLOCATION.ACT.3 | realizes | runs bulk data work as the deferred-work placement allows |
| PIG-WEB-DATA.DERIVE.1 | web-app-philosophy:ALLOCATION.DERIVE.1 | realizes | keeps denormalized copies in sync as the placement sets |

## C. Inter, same-branch counterparts (kind `refines`), source: skeleton.md, "Same-branch counterparts"

| src | dst |
|---|---|
| PIG-WEB-DATA | web-app-philosophy:DATA |
| PIG-WEB-DATA.ORGANIZE | web-app-philosophy:DATA.ORGANIZE |
| PIG-WEB-DATA.GUARD | web-app-philosophy:DATA.GUARD |
| PIG-WEB-DATA.CONCURRENCY | web-app-philosophy:DATA.GUARD |
| PIG-WEB-DATA.MAINTAIN | web-app-philosophy:DATA.MAINTAIN |
| PIG-WEB-DATA.DERIVE | web-app-philosophy:DATA.DERIVE |

PIG-WEB-DATA.INTERFACE has no same-branch counterpart: the philosophy graph holds no database-interface node (J2 proposed `DATA.INTERFACE` to the skeleton owner; judge gap 3).

## D. Proposed by the judge, not in the skeleton (source: J6 records.md, "Realizes" of the node, and result.md, "Skeleton owner")

| src | dst | kind | note |
|---|---|---|---|
| PIG-WEB-DATA.GUARD.2 | web-app-philosophy:ALLOCATION.GUARD.3 | realizes | proposed, not created by the judge |
| PIG-WEB-DATA.GUARD.2 | PIG-WEB-ALLOCATION.DB_API | realizes | proposed, not created by the judge |
| PIG-WEB-DATA.CONCURRENCY.5 | web-app-philosophy:ALLOCATION.ACT.2 | realizes | proposed, not created by the judge |

## E. Other "Realizes" statements in the records (informal, no skeleton row; for the linker to accept or ignore)

Verbatim "Realizes" line of each record.

- PIG-WEB-DATA: refines web-app-philosophy:DATA (skeleton link). Through its children: RECORD.1, RECORD.2, RECORD.3, GUARD.2, GUARD.3 (per-role layer), GUARD.5, GUARD.6, ACT.1, ACT.3, ACT.4, DERIVE.1, DERIVE.3, and the stack placements DB_API, TYPE_CHAIN, ROW_SECURITY, CACHE_STORE.
- PIG-WEB-DATA.ORGANIZE: PIG-WEB-ALLOCATION.TYPE_CHAIN (supplies the schema the type chain starts from: stored facts originate here). Refines web-app-philosophy:DATA.ORGANIZE.
- PIG-WEB-DATA.GUARD: refines web-app-philosophy:DATA.GUARD; through its children ALLOCATION.GUARD.2, GUARD.3 (per-role layer), ACT.1, ACT.4, ROW_SECURITY.
- PIG-WEB-DATA.CONCURRENCY: web-app-philosophy:ALLOCATION.GUARD.5 (concurrency control the placement gives the database); refines web-app-philosophy:DATA.GUARD.
- PIG-WEB-DATA.MAINTAIN: refines web-app-philosophy:DATA.MAINTAIN; through its children ALLOCATION.RECORD.3, ACT.3, ACT.4.
- PIG-WEB-DATA.DERIVE: refines web-app-philosophy:DATA.DERIVE; ALLOCATION.DERIVE.1, DERIVE.3, PIG-WEB-ALLOCATION.CACHE_STORE through its children.
- PIG-WEB-DATA.INTERFACE: PIG-WEB-ALLOCATION.DB_API; ALLOCATION.RECORD.2. Gap (J2's gap 1): no philosophy node holds the database interface; J2 proposed `DATA.INTERFACE` to the skeleton owner; until then this node has no same-branch refines link.
- PIG-WEB-DATA.ORGANIZE.1: J2 DATA.ORGANIZE; TYPE_CHAIN through the parent.
- PIG-WEB-DATA.ORGANIZE.2: J2 DATA.ORGANIZE; TYPE_CHAIN; supports GUARD.6 (client identifiers). MD-01's composite-key condition for row security is met by this shape where a scope exists, without implying row security.
- PIG-WEB-DATA.ORGANIZE.3: J2 DATA.ORGANIZE and DATA.GUARD (precise structure, L485); ALLOCATION.PRESENT.2 (canonical storage); ALLOCATION.DERIVE.2 (collation, open).
- PIG-WEB-DATA.ORGANIZE.4: TYPE_CHAIN (generated models inherit these names); J2 DATA.MAINTAIN (forward-only conventions).
- PIG-WEB-DATA.ORGANIZE.5: J2 DATA.GUARD (precise structure); TYPE_CHAIN (document schemas are stored facts of the contract).
- PIG-WEB-DATA.ORGANIZE.6: PIG-WEB-ALLOCATION.DB_API (the API schema); PIG-WEB-ALLOCATION.ROW_SECURITY (tenancy without row security by default). Multi-tenancy is in light scope (skeleton).
- PIG-WEB-DATA.ORGANIZE.7: ALLOCATION.DERIVE.2 (the database reduces rows set-based, which needs these indexes); CONCURRENCY.2.
- PIG-WEB-DATA.GUARD.1: web-app-philosophy:ALLOCATION.GUARD.2 (declares the invariants the placement gives the database); J2 DATA.GUARD.
- PIG-WEB-DATA.GUARD.2: ALLOCATION.GUARD.3 (database layer per consumer role); ALLOCATION.RECORD.2 and PIG-WEB-ALLOCATION.DB_API (EXECUTE as the contract's access); ALLOCATION.ACT.4 (session role names the consumer). Links proposed, not created: GUARD.2 realizes GUARD.3 and DB_API.
- PIG-WEB-DATA.GUARD.3: PIG-WEB-ALLOCATION.ROW_SECURITY; ALLOCATION.GUARD.3 (actor claim and pairing); ALLOCATION.ACT.4 (actor recorded).
- PIG-WEB-DATA.GUARD.4: web-app-philosophy:ALLOCATION.ACT.1 (keeps trigger logic within what the placement allows the database); ALLOCATION.ACT.4; ALLOCATION.GUARD.2.
- PIG-WEB-DATA.CONCURRENCY.1: ALLOCATION.GUARD.2 (hand-off: default isolation) and ALLOCATION.GUARD.5; J2 DATA.GUARD.
- PIG-WEB-DATA.CONCURRENCY.2: ALLOCATION.GUARD.5; ALLOCATION.GUARD.2.
- PIG-WEB-DATA.CONCURRENCY.3: ALLOCATION.GUARD.5; ALLOCATION.ACT.3 (queue claiming, with JOB_HOST).
- PIG-WEB-DATA.CONCURRENCY.4: web-app-philosophy:ALLOCATION.GUARD.6 (mutations as idempotent statements); ALLOCATION.ACT.3 (batch jobs).
- PIG-WEB-DATA.CONCURRENCY.5: ALLOCATION.ACT.2 (outbox relay reads, with J7's PROCESS.2); ALLOCATION.DERIVE.1 (cache workers); ALLOCATION.GUARD.5. Link proposed, not created: CONCURRENCY.5 realizes ALLOCATION.ACT.2.
- PIG-WEB-DATA.CONCURRENCY.6: web-app-philosophy:ALLOCATION.ACT.1 (orders transitions written by their single authoritative writer); J2 DATA.DERIVE (L597 cited there).
- PIG-WEB-DATA.MAINTAIN.1: ALLOCATION.RECORD.3 (structure as the origin of stored facts; via J2 DATA.MAINTAIN); PIG-WEB-ALLOCATION.DB_API (function changes ship as migrations).
- PIG-WEB-DATA.MAINTAIN.2: ALLOCATION.ACT.4 (archive and history kept in the database); J2 DATA.MAINTAIN (gap 3: lifecycle at stack level only). Personal-data erasure (deferred MAINTAIN.6, L526 recorded as input) must reach soft-deleted rows, archives and history; noted, not judged.
- PIG-WEB-DATA.MAINTAIN.3: web-app-philosophy:ALLOCATION.ACT.4 (writes history where the audit placement says). Conflicts link of PIG-WEB-TRANSVERSE.OPERABILITY.4 (security log apart) respected.
- PIG-WEB-DATA.MAINTAIN.4: web-app-philosophy:ALLOCATION.ACT.3 (bulk data work as the deferred-work placement allows).
- PIG-WEB-DATA.MAINTAIN.5: ALLOCATION.RECORD.1 (the system of record survives loss). High availability is deferred (MAINTAIN.7).
- PIG-WEB-DATA.DERIVE.1: web-app-philosophy:ALLOCATION.DERIVE.1 (keeps denormalized copies in sync as the placement sets); J2 DATA.DERIVE.
- PIG-WEB-DATA.DERIVE.2: PIG-WEB-ALLOCATION.CACHE_STORE (holds cache tables when the placement keeps caches in Postgres); ALLOCATION.DERIVE.3; ALLOCATION.ACT.3 (scheduled refresh, with JOB_HOST).
- PIG-WEB-DATA.INTERFACE.1: PIG-WEB-ALLOCATION.DB_API (writes the functions and views the placement calls for); ALLOCATION.RECORD.2; ALLOCATION.ACT.1 (operations as functions); ALLOCATION.GUARD.5, GUARD.6 (parameters).
- PIG-WEB-DATA.INTERFACE.2: PIG-WEB-ALLOCATION.DB_API (how consumers reach the API); ALLOCATION.RECORD.2 (one role per consumer, bounded). Topology of the pooler belongs to J9 (TRANSVERSE.TOPOLOGY).
