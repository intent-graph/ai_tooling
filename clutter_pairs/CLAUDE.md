# CLAUDE.md — clutter_pairs

- **English only**, in code, docs, comments and commit messages.
- Read [README.md](README.md) and [architecture.md](architecture.md) before working here. The architecture is the owner's;
  anything marked *proposal* in it is not decided.
- **Design stage:** the owner agrees on the high-level design ([design/README.md](design/README.md): data flow,
  choices) before any implementation. Do not write code until the owner accepts it.
- The output contract is pairs (clean, cluttered) of the same view. Anything a consumer derives from them
  (labels, judge triplets, injected defects) belongs to the consumer, not here.
- Public repository: no reference to private projects, buildings or people; examples stay generic.
- Models are swappable; never hard-wire a model, a path or a GPU provider.
