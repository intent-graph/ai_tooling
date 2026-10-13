# Result: PIG-WEB.INTERACTION batch (unit J8, graph pig-web-defaults)

## L1 headline

`batch.yaml` holds 28 `node.create` (the branch PIG-WEB.INTERACTION, 26 judged nodes and 2 deferred) and 0 `link.create`; every link touching the branch has an endpoint outside it and is listed in `links_out.md`. **The batch does not apply to the real graph as it stands**: `ig-tool` refuses an L1 uid `PIG-WEB.INTERACTION` under the root `PIG-WEB.ROOT` ("Child node UID must start with parent prefix: expected 'PIG-WEB.ROOT.<keyword-or-number>'"), the same skeleton-wide uid-scheme problem the allocation unit reported. On a variant (root renamed `ROOT`, branch uid `PIG-WEB-INTERACTION`, descendants prefixed to match) the dry run applied 28 of 28 operations and `ig-tool validate` returned 0 errors, 0 warnings. Skeleton uids are kept unchanged in the batch; the coordinator decides the uid scheme before applying. Scratch files deleted.

## L2 claims

Nodes created, breadth-first (epistemic_state verbatim from the judge records; undecided clause inherited from the authorization placement on the nodes the record marks):
- PIG-WEB.INTERACTION Browser and Agent Surface (parent PIG-WEB.ROOT): known, inherited undecided read-visibility clause.
- PIG-WEB.INTERACTION.VISUALIZE Browser Rendering, EDIT Editing Without Loss, REALTIME Real-Time Channels, COLLABORATE Comments and Collaboration, AGENT Agent Surface, ENVIRONMENT Browser Environment (L2).
- VISUALIZE.1 Rendering Technique, .2 Client State, .3 Page Performance, .4 Accessibility.
- REALTIME.1 Channel Choice, .2 Channel Operation, .3 Long-Lived Connection Servers, .4 Channel Security (inherited undecided clause), .5 Database Notifications.
- COLLABORATE.1 Comment Anchoring, .2 Threads and Comment Lifecycle, .3 Collaborative Text Editing, .4 Notifications and Moderation (inherited undecided clause).
- AGENT.1 Surface and Protocol, .2 Discovery and Registration, .3 Identity and Delegation, .4 Approval and Injection Defense, .5 Agent-Shaped Responses and Limits.
- ENVIRONMENT.1 Capability and Page Lifecycle; ENVIRONMENT.2 Offline and Installable Apps and ENVIRONMENT.3 Internationalization, both `epistemic_state: deferred: scope out, recorded and not judged (deferred by the judge plan); requires <placement>`.

## L3 notes

- Source: the judge records (final, with the review fixes applied; the result file's revision subsections were read and their changes are already in the records). Each node's `constraints` are the decision rules of its record, one per line; roll-ups and deferred nodes carry none. `design_notes` carry the record's decides, rows, positions, forces, decision (roll-ups in full), rejected options with their winning conditions, open points, realizes and hand-offs; the root node also carries the inherited read-visibility clause with its stated default and consequence, the maintainer decisions applied (MD-01 to MD-03), the contested rows and how they were composed, the seven evidence gaps, and the review fixes. `intent` is written from the record's decision, stack-named, one to three sentences.
- `impl_pointers`: the judge record plus every original research claim behind the owned and cited ledger rows (the `merges` column), slot taken from the claim prefix; collaboration claims use `build/research/20_collaboration/result.md::C<nn>`. Roll-ups and deferred nodes own no rows and carry the record pointer only. Ledger rows cited without a `merges` entry: none found.
- Name change: the skeleton names ENVIRONMENT.2 and ENVIRONMENT.3 end in a marker "[deferred]"; brackets are forbidden in node names, so the batch uses "Offline and Installable Apps" and "Internationalization"; the deferral is in `epistemic_state`.
- `examples` left empty: the records give no concrete examples. `history` not set. No "Authority/Copies/Forbidden" lines: the unit has no placement nodes.
- Not transcribed as fields: the records' "Basis" and "Judgments the L2 compresses" sections (result file) are folded only through the root node's design notes; the questions file is empty (none).
- Left open by the records, not invented: the fragment-swap and island libraries (VISUALIZE.1), the author edit window value (COLLABORATE.4), the NOTIFY threshold (REALTIME.3, .5), the per-project list of scarce-goods flows (AGENT.5).
- Links: 0 created; 2 skeleton intra-graph, 9 skeleton inter-graph, 6 refines counterparts and 30 judge-proposed links are in `links_out.md`.
