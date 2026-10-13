# Result: PIG-WEB.DATA batch (pig-web-defaults)

## L1 headline

`batch.yaml` holds 36 `node.create` operations (33 judged nodes, 3 deferred with `epistemic_state` deferred) and 0 `link.create`: no intentlink has both endpoints in the unit. The 18 skeleton links and 3 judge-proposed links touching these nodes are in `links_out.md` for the linker.

Dry-run outcome: the batch does NOT apply to the real graph as it stands. `ig-tool apply` rejects the first operation, `PIG-WEB.DATA` under `PIG-WEB.ROOT`: "Child node UID must start with parent prefix: expected 'PIG-WEB.ROOT.<keyword-or-number>'". The UID validator (`validate_uid_format`, intent_graph models/node.py) accepts an L1 child only under a root literally named `ROOT` (a `PIG-X-Y` form is tolerated there), and requires L2 keyword suffixes only under an L1 whose parent is `ROOT`. The skeleton's uids (`PIG-WEB.DATA`, `PIG-WEB.DATA.ORGANIZE`, ...) are used unchanged, as the brief demands, so every unit of this graph will hit the same rule. The existing `PIG-PY.*` graph has the same shape and `ig-tool validate` passes it, so it was presumably written without going through this check (inferred, not verified), so the coordinator needs either a validator change or a direct write for this graph.

Check that passed: on a scratch copy of the graph with root renamed `ROOT` and the prefix `PIG-WEB.` dropped from every uid (same fields, same order), `ig-tool apply --batch` succeeded with 36 operations and `ig-tool validate` reported 37 nodes, 0 links, 0 errors, 0 warnings. The scratch files were kept outside the real graph and the slot folder and are discarded.

## L2 nodes created (breadth-first, parent shown by uid prefix)

- PIG-WEB.DATA Postgres Data Tier: state `known`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.ORGANIZE Schema Organization: state `known`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.GUARD Declared Integrity: state `known`; 0 constraints; 4 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY Concurrency Mechanics: state `known`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.MAINTAIN Data Maintenance: state `known`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.DERIVE Derived Data in Postgres: state `known`; 0 constraints; 4 impl_pointers.
- PIG-WEB.DATA.INTERFACE Database Interface: state `known`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.1 Tables and Normalization: state `known`; 4 constraints; 8 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.2 Keys: state `known`; 6 constraints; 13 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.3 Column Types: state `known`; 7 constraints; 9 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.4 Naming: state `known`; 4 constraints; 8 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.5 JSON Documents: state `known`; 4 constraints; 8 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.6 Schemas and Tenancy: state `known`; 3 constraints; 5 impl_pointers.
- PIG-WEB.DATA.ORGANIZE.7 Indexes: state `known`; 4 constraints; 6 impl_pointers.
- PIG-WEB.DATA.GUARD.1 Constraints: state `known`; 10 constraints; 18 impl_pointers.
- PIG-WEB.DATA.GUARD.2 Roles and Privileges: state `known`; 10 constraints; 12 impl_pointers.
- PIG-WEB.DATA.GUARD.3 Row Security Policies: state `known`; 4 constraints; 12 impl_pointers.
- PIG-WEB.DATA.GUARD.4 Triggers: state `known`; 6 constraints; 10 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.1 Default Concurrency Strategy: state `known`; 6 constraints; 16 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.2 Isolation Mechanics: state `known`; 6 constraints; 12 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.3 Locks: state `known`; 5 constraints; 11 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.4 Atomic Statements: state `known`; 4 constraints; 8 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.5 Sequences and Commit Order: state `known`; 3 constraints; 9 impl_pointers.
- PIG-WEB.DATA.CONCURRENCY.6 State Transition Order: state `known`; 2 constraints; 4 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.1 Migrations: state `known`; 6 constraints; 14 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.2 Deletion, Retention and Partitioning: state `undecided`; 3 constraints; 19 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.3 History Tables: state `known`; 6 constraints; 18 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.4 Bulk Data Jobs: state `known`; 4 constraints; 20 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.5 Backup and Recovery: state `known`; 5 constraints; 7 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.6 Personal Data Erasure: state `deferred`; 0 constraints; 2 impl_pointers.
- PIG-WEB.DATA.MAINTAIN.7 High Availability and Replication: state `deferred`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.DERIVE.1 Denormalization and Sync: state `known`; 5 constraints; 9 impl_pointers.
- PIG-WEB.DATA.DERIVE.2 Cache Tables: state `known`; 6 constraints; 10 impl_pointers.
- PIG-WEB.DATA.DERIVE.3 Search: state `deferred`; 0 constraints; 1 impl_pointers.
- PIG-WEB.DATA.INTERFACE.1 Functions and Views: state `known`; 9 constraints; 11 impl_pointers.
- PIG-WEB.DATA.INTERFACE.2 Connections and Pooling: state `known`; 6 constraints; 12 impl_pointers.

## Transcription notes and what could not be transcribed

- Source: `build/distill/03_judge/J6_pig_data/records.md` (revision with review fixes B1, M1 to M3, m1 to m7, X1 to X4, X7 applied; `result.md` of the judge lists no later subsection). Maintainer decisions MD-01 to MD-03 are cited inside the records and carried through.
- `epistemic_state`: the record's State line verbatim, backticks removed, pipe annotations kept. It cites ledger ids (L471, L493, ...) as in the record.
- `intent`: written for this batch (one to three sentences per node, self-sufficient, roll-ups summarize their children); the judge records hold no intent field. Deferred nodes carry the skeleton's question plus the deferral.
- `constraints`: the decision bullets of each record, markup removed, one per entry. Roll-ups carry none (their decision is a summary). Bullets that are open points, not rules, are left out of `constraints` and stay in `design_notes`: ORGANIZE.2 (whether an internal key appears outside the system, J7's decision), ORGANIZE.3 (collation, open), ORGANIZE.5 (validator mechanism, open), MAINTAIN.2 (the awaiting-maintainer default).
- `design_notes`: question, positions, forces, the full decision with its grounds, awaiting-maintainer clauses, rejected options with their winning conditions, realized placements. The decision text appears in full here and its rule bullets again in `constraints` (deliberate: grounds stay with the rule).
- `impl_pointers`: the judge record, then one `build/research/<slot>/result.md::<CLAIM-ID>` per original claim behind every ledger row the record owns or cites (owned rows from the ledger owner column, cited rows from the ids in the record; ranges expanded). Collaboration claims written `C01`. Roll-up nodes own no row and cite none, so they carry the record pointer only (DATA.GUARD and DATA.DERIVE also cite a few rows in their text).
- `examples`, `history`: not set (the records give no concrete examples).
- Not transcribed: none of the 36 records was dropped. Open items stay open as recorded: MAINTAIN.2 `undecided: awaiting maintainer` (question 1), the read-visibility clause carried on DATA, GUARD, GUARD.2, GUARD.3, INTERFACE and INTERFACE.1, collation as a gap on ORGANIZE and ORGANIZE.3.
