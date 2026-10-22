# CLAUDE.md — clutter_pairs

- **English only**, in code, docs, comments and commit messages.
- Read [README.md](README.md) and [architecture.md](architecture.md) before working here. The architecture is the owner's;
  anything marked *proposal* in it is not decided.
- **Design stage:** the high-level design ([design/README.md](design/README.md)) is agreed; slice 1's detailed design
  ([design/data_model.md](design/data_model.md) with [design/schema.sql](design/schema.sql),
  [design/loops.md](design/loops.md), [design/components.md](design/components.md)) is a proposal. Code starts once the
  owner accepts it.
- **virtual_unstaging** is imported, never copied. It may change only by adding modularity or override mechanisms
  (owner's rule): each defaults to its own behaviour and never names clutter_pairs. Its gates must pass after any
  change there, and the names relied on are the ones listed in design/components.md.
- The output contract is pairs (clean, cluttered) of the same view. Anything a consumer derives from them
  (labels, judge triplets, injected defects) belongs to the consumer, not here.
- Public repository: no reference to private projects, buildings or people; examples stay generic.
- Models are swappable; never hard-wire a model, a path or a GPU provider.
