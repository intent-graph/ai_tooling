# virtual_unstaging

Empty a building's photos of their furniture and belongings with an image-editing model, steered by a judge
model and corrected by a second level of review, so the same photos show the empty building.

> **Status:** slice 1 implemented and tested offline: store, registry of dimensions, three search engines, judge
> contract, runner with resume, reports, delivery, the GPU tool server with generator recipes and tools, the review
> page, GPU provisioning with a self-delete deadline. Not yet run on a real model or a rented GPU. Read [architecture.md](architecture.md) for
> the stages and the judge, then [design/](design/README.md) for how they become this program.

## Table of Contents

1. [Install](#install) _(Lines 22-31)_
1. [Use](#use) _(Lines 34-52)_
1. [Develop](#develop) _(Lines 55-65)_
1. [Files](#files) _(Lines 68-81)_

---

## Install
<!-- Lines 22-31 -->

From this folder, with [uv](https://docs.astral.sh/uv/):

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e ".[dev]"     # the orchestrator: no GPU library
```

The GPU side (`unstage serve`) needs the `[serve]` extra, on the rented machine only.

## Use
<!-- Lines 34-52 -->

A project is a folder: its configuration, its database, its images by hash.

```bash
unstage --project my_flat init                     # writes project.toml: models, endpoints, budget
unstage --project my_flat import photos/           # one subfolder per room
unstage --project my_flat rules rules.toml         # [all] and [groups."<room>"]: fixed and movable elements
unstage --project my_flat masks masks/             # removal masks named like the photos, or: prepare
unstage --project my_flat run --engine single      # one attempt per photo: the baseline
unstage --project my_flat run --engine guided      # search led by the judge's findings
unstage --project my_flat report                   # accepted photos, attempts, GPU time, comparisons
unstage --project my_flat review                   # local review page: typed findings, blind comparisons
unstage --project my_flat deliver --run 2
unstage --project my_flat export out/
```

Secrets never go in `project.toml`: name a key file (mode 600) or a key command. To try the whole loop without a
GPU, set both `adapter` lines of `project.toml` to `"fake"`.

To try a variant without editing the project (another judge, a faster version of a model), put the changed keys
in an override file and name it before the command; files given later win:

```bash
unstage --project my_flat --override small_judge.toml gpu judge          # [judge] model, [gpu.judge] memory share
unstage --project my_flat --override small_judge.toml --override fast.toml run --engine single
```

```toml
# fast.toml: a faster judge request and a smaller generation
[judge]
image_side = 1024
image_format = "jpeg"
max_findings = 6
comment_chars = 100

[generator.settings]
output_side = 768
```

## Develop
<!-- Lines 55-65 -->

```bash
.venv/bin/pytest -q                        # offline, no GPU
.venv/bin/ruff check src tests
.venv/bin/mypy src/virtual_unstaging
.venv/bin/lint-imports                     # the declared layering, a blocking check
```

The schema is [`src/virtual_unstaging/store/schema.sql`](src/virtual_unstaging/store/schema.sql); the shipped
registry, defect taxonomy and base instructions are in [`src/virtual_unstaging/data/`](src/virtual_unstaging/data/).

## Files
<!-- Lines 68-81 -->

- [`architecture.md`](architecture.md) — the architecture and its open questions.
- [`design/`](design/README.md) — the detailed design: usage, required properties, system shape, components,
  decisions; [data model](design/data_model.md); [per-image loop](design/loop1.md) (registry, compile, judge
  contract, scoring, engines, first-slice experiment); [tool server API](design/tool_server_api.md);
  [review page](design/review_page.md); [provisioning](design/provisioning.md).
- [`training.md`](training.md) — the offline layer as machine learning on prompts: parameters, training data
  (pairs from [clutter_pairs](../clutter_pairs/README.md), and what is derived from them), performance measure,
  search methods.
- [`state_of_the_art.md`](state_of_the_art.md) — what exists per branch (paired data, removal, edit judges,
  critic-in-the-loop editors, prompt optimization) and what it changes for the open questions.
- [`src/virtual_unstaging/`](src/virtual_unstaging/) — the package; [`tests/`](tests/) — its tests;
  [`pyproject.toml`](pyproject.toml) — dependencies, the `unstage` command, lint and layering rules.
- [`CLAUDE.md`](CLAUDE.md) — agent entry point for this folder.
