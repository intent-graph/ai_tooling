# Result: PIG-WEB.ALLOCATION batch (unit J1, graph pig-web-defaults)

## L1 headline

`batch.yaml` holds 9 operations: 8 `node.create` (the branch PIG-WEB.ALLOCATION and its 7 placements) and 1 `node.set` on PIG-WEB.ROOT; 0 `link.create`. **The batch does not apply to the real graph as it stands**: `ig-tool` refuses an L1 uid `PIG-WEB.ALLOCATION` under the root `PIG-WEB.ROOT` ("Child node UID must start with parent prefix: expected 'PIG-WEB.ROOT.<keyword-or-number>'"); its uid rule recognises only a root named `ROOT`, and an L1 child of `ROOT` must be a single keyword or match `PIG-X-Y`. A variant with the root renamed `ROOT` and the L1 uid `PIG-WEB-ALLOCATION` (children `PIG-WEB-ALLOCATION.<KEYWORD>`) applied and validated with 0 errors, 0 warnings (9 nodes). The coordinator must decide the uid scheme for the whole graph (a skeleton-wide issue) before applying any pig-web-defaults batch. Skeleton uids are kept unchanged in the batch.

## L2 claims

Nodes created (epistemic_state verbatim from the judge records):
- PIG-WEB.ALLOCATION (Stack Allocation, parent PIG-WEB.ROOT): `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (GUARD.3, Q1)`.
- PIG-WEB.ALLOCATION.POSTGRES_FIRST: `known | unvalidated: ...`.
- PIG-WEB.ALLOCATION.DB_API: `known: MD-03 | conflict: views as contract ...`.
- PIG-WEB.ALLOCATION.TYPE_CHAIN: `known: MD-02 | unvalidated: ...`.
- PIG-WEB.ALLOCATION.ROW_SECURITY: `known: MD-01 | conflict: L619, L688 ...`.
- PIG-WEB.ALLOCATION.JOB_HOST: `known | unvalidated: the contention threshold is open (L126)`.
- PIG-WEB.ALLOCATION.CACHE_STORE: `known | unvalidated: ...`.
- PIG-WEB.ALLOCATION.JS_SERVER: `known | gap: no source weighs the extra tier's operational cost (L288)`.
- PIG-WEB.ROOT: node.set, intent summarising the graph, epistemic_state `known`.

No node in this branch is deferred, so none carries a deferral reason.

## L3 notes

- Judge records read at their latest revision (3, per the result file); X2 wording is included in DB_API.
- impl_pointers: the judge record, plus every original research claim behind the ledger rows the record owns or cites (merges column), by the slot of the claim prefix; L688 maps to `build/research/20_collaboration/result.md::C33`. The branch roll-up owns no ledger row and carries only the judge-record pointer.
- Placement nodes carry Authority, Copies and Forbidden rules in constraints where the record states them. The records give no "Copies" line for these nodes, so none is invented; permitted copies appear only inside the decision text (for example backend checks kept under row security).
- `examples` left empty: the records give no concrete examples. `history` not set.
- Links: none created (no intra-branch link in the skeleton); all 11 intra-graph and 9 inter-graph links touching these nodes are in `links_out.md`.
- Possible inconsistency for the coordinator: the ALLOCATION roll-up state cites "GUARD.3, Q1" (philosophy-graph names) verbatim from the record; they are not uids of this graph.
- Dry-run on the real uid scheme: failed at operation 0 with the error above (0 of 9 applied). Dry-run on the variant: passed; validate: 0 errors. Scratch files deleted.
