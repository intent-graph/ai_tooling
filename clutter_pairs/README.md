# clutter_pairs

Generate pairs of images of the same view, clean and cluttered, as ground-truth data for decluttering tools
(for instance [virtual_unstaging](../virtual_unstaging/README.md)).

> **Status:** design stage: high-level design agreed, slice 1's detailed design proposed; no code yet. Read
> [architecture.md](architecture.md) (the contract: only pairs are required; two routes, generation preferred;
> room ontology, clutter taxonomy, pipeline, quality checks, risks, prior work), then
> [design/README.md](design/README.md) (data flow, stored data, the choices, agreed; slice 1's detailed design).

## Files
<!-- Lines 13-16 -->

- [`architecture.md`](architecture.md) — the architecture and its open questions.
- [`CLAUDE.md`](CLAUDE.md) — agent entry point for this folder.

## Sub-folders
<!-- Lines 19-22 -->

- [`design/`](design/README.md) — the agreed high-level design and slice 1's detailed design: data model and
  `schema.sql`, loops (composition and recording, pixel tests, composite, lessons and their measurement), components
  (use of virtual_unstaging, layering, command line).
