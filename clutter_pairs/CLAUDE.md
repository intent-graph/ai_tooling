# CLAUDE.md — clutter_pairs

- **English only**, in code, docs, comments and commit messages.
- Read [README.md](README.md) and [architecture.md](architecture.md) before working here. The architecture is the owner's;
  anything marked *proposal* in it is not decided.
- **Design, then code:** the high-level design ([design/README.md](design/README.md)) is agreed; slice 1's detailed
  design ([design/data_model.md](design/data_model.md), [design/loops.md](design/loops.md),
  [design/components.md](design/components.md)) is implemented, with the schema in
  [src/clutter_pairs/store/schema.sql](src/clutter_pairs/store/schema.sql). A change the code needs goes into the
  design first, and to the owner when it touches an agreed choice (C1 to C10) or property (P1 to P10).
- **Gates before handing back code:** `.venv/bin/pytest -q`, `.venv/bin/ruff check src tests`,
  `.venv/bin/mypy src/clutter_pairs`, `.venv/bin/lint-imports`. All SQL stays in `store/`; model instructions and
  every other prompt text stay in `data/` (P10).
- **virtual_unstaging** is imported, never copied. It may change only by adding modularity or override mechanisms
  (owner's rule): each defaults to its own behaviour and never names clutter_pairs. Its gates must pass after any
  change there, and the names relied on are the ones listed in design/components.md.
- The output contract is pairs (clean, cluttered) of the same view. Anything a consumer derives from them
  (labels, judge triplets, injected defects) belongs to the consumer, not here.
- Public repository: no reference to private projects, buildings or people; examples stay generic.
- Models are swappable; never hard-wire a model, a path or a GPU provider.
