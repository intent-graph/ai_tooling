# clutter_pairs

Generate pairs of images of the same view, clean and cluttered, as ground-truth data for decluttering tools
(for instance [virtual_unstaging](../virtual_unstaging/README.md)).

> **Status:** slice 1 implemented and tested offline, on stand-in models: declared space, planner, both loops with
> lessons carried forward and a comparison arm, recording of every exchange, audit, reports, export, command line.
> Not yet run on a real model or a rented GPU. Read [architecture.md](architecture.md) (the contract: only pairs are
> required; two routes, generation preferred; room ontology, clutter taxonomy, pipeline, quality checks, risks, prior
> work), then [design/README.md](design/README.md) (data flow, stored data, the choices; slice 1's detailed design).

## Table of Contents

1. [Install](#install) _(Lines 24-32)_
1. [Use](#use) _(Lines 35-53)_
1. [Develop](#develop) _(Lines 56-69)_
1. [Files](#files) _(Lines 72-76)_
1. [Sub-folders](#sub-folders) _(Lines 79-83)_

---

## Install
<!-- Lines 24-32 -->

From this folder, with [uv](https://docs.astral.sh/uv/), beside a checkout of `virtual_unstaging` (imported as an
editable path dependency):

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e ".[dev]"
```

## Use
<!-- Lines 35-53 -->

A dataset is a folder: its configuration, its store, its images by hash, its exports.

```bash
cpairs init my_pairs                          # writes clutter_pairs.toml: models, run settings, thresholds, GPU
cpairs --dataset my_pairs plan                # scenes and clutter specs into the target cells
cpairs --dataset my_pairs run --fake --smoke  # a dry run on stand-in models, no GPU
cpairs --dataset my_pairs gpu up --limit 2h   # rents the GPU; shows the price and the deadline
cpairs --dataset my_pairs run                 # first the smoke wave; run again for the waves to the pair target
cpairs --dataset my_pairs report              # coverage, iteration curve, carry-forward, cost (--json)
cpairs --dataset my_pairs decide threshold max_shift_px 3
cpairs --dataset my_pairs audit               # every check; `audit <pair>` prints a pair's lineage
cpairs --dataset my_pairs export v1           # clean/, cluttered/, mask/, manifest.jsonl, splits by building
cpairs --dataset my_pairs gpu down
```

Exit codes: 0 done, 1 failure (an audit problem included), 2 usage, 3 paused on an endpoint error (`run` again
resumes), 4 stopped at the rental's deadline. The command name `cpairs` is provisional.

## Develop
<!-- Lines 56-69 -->

```bash
.venv/bin/pytest -q                        # offline: the stand-in model server runs on a local port
.venv/bin/ruff check src tests
.venv/bin/mypy src/clutter_pairs
.venv/bin/lint-imports                     # the declared layering, a blocking check
```

A change to `virtual_unstaging` also runs these. The schema is
[`src/clutter_pairs/store/schema.sql`](src/clutter_pairs/store/schema.sql); the model instructions, composers, answer
schemas, default space, reason codes and the carry-forward decision rule are the data files in
[`src/clutter_pairs/data/`](src/clutter_pairs/data/), each replaceable per dataset (`[files]` in
`clutter_pairs.toml`).

## Files
<!-- Lines 72-76 -->

- [`architecture.md`](architecture.md) — the architecture and its open questions.
- [`CLAUDE.md`](CLAUDE.md) — agent entry point for this folder.
- [`pyproject.toml`](pyproject.toml) — package, gates, and the declared layering.

## Sub-folders
<!-- Lines 79-83 -->

- [`design/`](design/README.md) — the agreed high-level design and slice 1's detailed design: data model, loops
  (composition and recording, pixel tests, composite, lessons and their measurement), components (use of
  virtual_unstaging, layering, command line); aids for the judges (exploration).
- [`src/clutter_pairs/`](src/clutter_pairs/) — the package; [`tests/`](tests/) — one test per property, on fakes.
