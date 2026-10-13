# Links touching the DATA nodes that this batch does not create

None of the links below has both endpoints inside this unit, so the batch holds no `link.create` (0 links). For the linker.

## Skeleton intentlinks (section "Intentlinks")

| src | dst | kind | intent | source |
|---|---|---|---|---|
| DATA.ORGANIZE | ALLOCATION.RECORD.1 | realizes | holds the durable facts in the form the system-of-record placement gives the database | skeleton, tier to placement |
| DATA.GUARD | ALLOCATION.GUARD.2 | realizes | enforces the invariants the placement gives the database | skeleton, tier to placement |
| DATA.GUARD | ALLOCATION.GUARD.5 | realizes | carries the concurrency control the placement gives the database | skeleton, tier to placement |
| DATA.DERIVE | ALLOCATION.DERIVE.1 | realizes | keeps derived values in the tier and freshness the placement sets | skeleton, tier to placement |
| DATA.MAINTAIN | ALLOCATION.RECORD.3 | realizes | keeps the database structure as the origin of shapes when the placement makes it the origin | skeleton, tier to placement |
| DATA.ORGANIZE | python-kb-philosophy:STRUCTURE | refines | the data model is designed before the code | skeleton, cross-graph |
| DATA.ORGANIZE | python-kb-philosophy:DATACENTRICITY | refines | facts are stored once, normalized | skeleton, cross-graph |
| DATA.MAINTAIN | python-kb-philosophy:REPRODUCIBILITY | refines | schema changes are versioned and applied by automation | skeleton, cross-graph |

## Proposed by the judge, not in the skeleton (judge records, "Realizes" and gap 1)

| src | dst | kind | intent | source |
|---|---|---|---|---|
| DATA.GUARD | ALLOCATION.GUARD.3 | realizes | database layer of authorization per consumer role (grants) | records.md::DATA.GUARD; needs the skeleton owner's decision |
| DATA.GUARD | ALLOCATION.RULES.5 | realizes | atomicity ends at the transaction | records.md::DATA.GUARD; needs the skeleton owner's decision |
| DATA.MAINTAIN | ALLOCATION.ACT.4 | realizes | audit and history kept in the database | records.md::DATA.MAINTAIN; needs the skeleton owner's decision |

## Placement "Realized or refined by" lines naming a DATA node

- ALLOCATION.RECORD.1: DATA.ORGANIZE (realizes)
- ALLOCATION.RECORD.3: DATA.MAINTAIN (realizes)
- ALLOCATION.GUARD.2 and GUARD.5: DATA.GUARD (realizes)
- ALLOCATION.DERIVE.1: DATA.DERIVE (realizes)

(These repeat the table above. The same lines also name defaults-graph nodes under the defaults branch PIG-WEB-DATA.*; those links belong to the defaults-graph units and the cross-graph linker.)

## Not created, proposed node

A node `DATA.INTERFACE` (realizes ALLOCATION.RECORD.2 and the database share of ALLOCATION.ACT.1; refined by the defaults graph's database interface node) is proposed by the judge for the skeleton owner. Not created here.
