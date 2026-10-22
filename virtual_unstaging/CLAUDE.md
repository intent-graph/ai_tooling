# CLAUDE.md — virtual_unstaging

- **English only**, in code, docs, comments and commit messages for this tool.
- Read [README.md](README.md) and [architecture.md](architecture.md) before working here. The architecture is the owner's;
  anything marked *proposal* in it is not decided.
- **Design, then implementation:** the owner has opened the design and implementation stage. Detailed design
  comes before code; the architecture stays the reference, and a change to it is proposed to the owner first.
  The detailed design is in `design/` (a *proposal* until the owner accepts it); the schema in `src/virtual_unstaging/store/schema.sql`.
- **Gates before handing back code:** `.venv/bin/pytest -q`, `.venv/bin/ruff check src tests`, `.venv/bin/mypy src/virtual_unstaging`,
  `.venv/bin/lint-imports` (the declared layering). All SQL stays in `store/`; `serve/` imports only `domain`.
- Structure before code: a change to stages, entities or the defect taxonomy goes into `architecture.md` first.
- This folder is in a public repository: no reference to the private projects the tool is tested on (no
  paths, names, photos, or figures that identify a building or a person). Examples stay generic.
- Models are swappable; never hard-wire a model, a path or a GPU provider.
