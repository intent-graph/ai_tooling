# Result: build of INTERACTION in web-app-philosophy

## L1 headline

batch.yaml creates 12 nodes (INTERACTION and its 11 descendants) and 0 links; the dry build on a copy of the graph applied 12 operations with 0 errors, and `ig-tool validate` reports 13 nodes, 0 errors, 0 warnings. The 12 skeleton and proposed links all touch a node outside the unit and are listed in `links_out.md` for the linker.

## L2 nodes created (breadth-first, parent in brackets)

- INTERACTION [ROOT]: roll-up; state `known | undecided: awaiting maintainer, read visibility ...` (inherited).
- INTERACTION.VISUALIZE [INTERACTION]: accessibility from the first design, native HTML first; `known | unvalidated | gap: conformance level`.
- INTERACTION.COLLABORATE [INTERACTION]: push as hint over correct pull, comments as entities, visibility on every surface; inherited undecided clause, unvalidated parts, conflict L682/L594.
- INTERACTION.AGENT [INTERACTION]: agents as users through an adapter, bounded; `known | unvalidated | open: scarce-goods flow list per project`.
- INTERACTION.ENVIRONMENT [INTERACTION]: roll-up of seven properties; `known`.
- INTERACTION.ENVIRONMENT.1 [ENVIRONMENT]: HTML-first, enhanced in layers; `known`.
- INTERACTION.ENVIRONMENT.2 [ENVIRONMENT]: restore, save on hidden, server arbitrates across tabs; `known | unvalidated`.
- INTERACTION.ENVIRONMENT.3 [ENVIRONMENT]: compatibility window, expand-migrate-contract, interface descriptions in sync (MD-02); `known | unvalidated`.
- INTERACTION.ENVIRONMENT.4 [ENVIRONMENT]: cacheability declared per URL; `known | unvalidated`.
- INTERACTION.ENVIRONMENT.5 [ENVIRONMENT]: any request may fail or repeat; `known | unvalidated`.
- INTERACTION.ENVIRONMENT.6 [ENVIRONMENT]: stable URLs, no credential in a URL, signed file URL exception; `known | unvalidated`.
- INTERACTION.ENVIRONMENT.7 [ENVIRONMENT]: no credential readable by script, escaping then CSP, uploads on another domain; `known | unvalidated`.

## Transcription notes

- Source: the final `records.md` of J4, which already carries the review fixes M1 to M4, m1, m2 and cross-branch X1, X2, X6, X7; `result.md` of J4 checked, no later revision subsection changes the records. MD-01 to MD-03 are cited where the records cite them; none contradicts the records.
- `epistemic_state` is the judge's State line verbatim. `constraints` are the decision's MUST rules; `design_notes` compress positions, forces, grounds, rejected options with winning conditions, realizes, hand-offs, maintainer decisions and evidence gaps. `examples` left unset: the records give no concrete examples beyond those inside the rules.
- `impl_pointers`: the judge record plus the research claims behind every ledger row named in the node's record section (owned, cited and mentioned), resolved through the ledger `merges` column; slot folder from the claim prefix, `COLLAB-Cnn` as `20_collaboration/result.md::Cnn`.
- Nothing left out. Not transcribed as nodes or links: the 12 links listed in `links_out.md`, because their destination is outside the unit.
- The hand-offs to pig-web judges and the allocation judge (conformance level, commit-ordered cursor, comment grants for reporting and operator roles, naming comments in the read-visibility question) are carried in `design_notes`, not as links.
