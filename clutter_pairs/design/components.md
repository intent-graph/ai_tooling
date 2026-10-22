# clutter_pairs — components and use of virtual_unstaging

What clutter_pairs takes from virtual_unstaging and on which of its names it relies, how its own package is layered,
what a dataset folder holds, and the command line. Refines [C7](README.md#c7-model-serving) and
[C10](README.md#c10-loop-code) of the design.

> **Status:** slice 1, implemented as written here; tested offline on stand-in models.

## Table of Contents

1. [Use of virtual_unstaging](#use-of-virtual_unstaging) _(Lines 21-43)_
1. [Components and layering](#components-and-layering) _(Lines 46-66)_
1. [The dataset folder](#the-dataset-folder) _(Lines 69-79)_
1. [Command line](#command-line) _(Lines 82-98)_


---

## Use of virtual_unstaging
<!-- Lines 21-43 -->

Imported as a package (editable path dependency), never copied. The owner's rule: virtual_unstaging changes only by
adding modularity or override mechanisms that keep its own behaviour by default and never name clutter_pairs;
text-to-image is the one exception the owner accepted. Slice 1 changed no code there.

| Need | Taken from virtual_unstaging | Extension point it relies on |
|---|---|---|
| rent one GPU with a deadline, serving the generator and the judge | `provision.lifecycle` (`Context`, `up`, `down`, `SESSION_FILE`), `provision.plan` (`ProjectPlan`, `JudgePlan`, the `DEFAULT_*` machine settings), `provision.userfiles` (`config_dir`, `state_dir`), `provision.errors.ProvisionError`, `provision.switch.switch_judge` (another judge on the live machine); the session file lands in the dataset folder | `Context.plan_source`; `ProjectPlan.tools = ()` (no segmentation models loaded) |
| make a clean image from text, edit it | `clients.toolserver.ToolServerClient`, `clients.generators.ToolServerGenerator`, the packaged recipes | recipe `text_only` (tool server API 1.2; the accepted exception) |
| the clean image's size | `serve.images.output_size`: the tool server's sizing rule, so the image-size check uses the rule itself | none |
| judge, write, revise, distill | `clients.openai_compatible.chat_json` (streamed, JSON-schema answers; free text through a one-field schema; the sampling seed through its `extra` argument), `image_part`, `text_part` | none |
| record every exchange as sent | `clients.http` (`Endpoint`, `EndpointError`, `Exchange`) | `clients.http.Endpoint.observer` (what it raises fails the call) |
| the loop's policy and resume | — | `engines.SearchEngine[Problem, Candidate, Evaluation]`, `engines.replay`, `ReplayMismatch` |
| images, hashes, store plumbing, secrets | `imaging`, `domain.sha256_text`, `sha256_bytes`, `canonical_json` and the generator request types, `store.blobs.BlobStore`, `store.db.connect` and `transaction`, `config.Secret` | none |

Not used: virtual_unstaging's project configuration, store schema, runner, judge, registry, review and command line;
its `FakeGenerator` neither (clutter_pairs' stand-in serves both APIs over HTTP, below).

**The surface relied on is declared on both sides.** The names above are the whole surface: virtual_unstaging's
design lists them as the names a program that imports it may rely on, without naming any such program; the
repository's instructions say that a change to virtual_unstaging also runs clutter_pairs' tests. A name used here and
missing from that list is a defect of this page.

## Components and layering
<!-- Lines 46-66 -->

One package, `clutter_pairs`, layered like virtual_unstaging and checked the same way (`lint-imports`, contract in
`pyproject.toml`): each layer imports only from the layers below it; modules of one layer do not import each other.

| Layer | Modules |
|---|---|
| presentation | `cli` |
| application | `run` (waves, the loops, calls, the driver around `engines.replay`, lesson activation), `plan` (sampling into target cells), `export`, `audit`, `report`, `gpu` (provisioning glue) |
| dataset | `dataset`: opens a dataset (configuration, store, the data files in force recorded by hash, space, targets, reasons, the decision rule), shared by every command |
| adapters | `models` (generator and chat callers), `recorder` (the observer: exchanges, image bytes, wire hashes), `store` (schema, queries, views: the only module that holds SQL), `config`, `fakes` |
| pure core | `compose` (composers, renderers, answer parsing), `pairs` (correction, mask, composite, explained change), `lessons` (arms, selection by scope, the distiller's answer), `engine` (the reviser's policy and stop rule), `space` (ontology, taxonomy, targets, sampling, the image-size check) |
| domain | the types |

**The stand-in models** (`fakes`): one local HTTP server that speaks both the tool server's API (capabilities, blobs,
generate, from text alone and as an edit) and an OpenAI-compatible chat server (writer, judges, distiller, chosen by
the answer schema's title). It runs behind the real clients, so the tests exercise recording, composition and replay
as a rental would. Its landscape is scripted (design/loops.md: the carry-forward test); `cpairs run --fake` uses it.

Data files ship in the package (`data/`): `instructions/`, `composers/`, `schemas/`, `space/`, `reasons.toml`,
`decision_rules/`, and `config_template.toml` (what `init` writes).

## The dataset folder
<!-- Lines 69-79 -->

Outside the package, one per dataset:

- `clutter_pairs.toml`: the dataset's seed; the generator (recipe, family, licence, size multiple, condition-image
  limit) and the judge (model, revision, family, licence, temperatures, answer length); the run (pair target,
  `output_side`, maximum iterations, wave width, lessons per request, variants, the seconds a call is expected to take
  before the deadline); the pixel thresholds; `[files]` replacements of packaged data files; the GPU plan. Secrets
  only by key file or key command (`config.Secret`); endpoints from the session file the rental writes.
- `store.sqlite`, `images/<first two hex>/<sha256>` (virtual_unstaging's `BlobStore`), `exports/<name>/`, and the
  rental's session file (`gpu_session.toml`) while a GPU is up.

## Command line
<!-- Lines 82-98 -->

Name `cpairs`, provisional. Per the repository's CLI guidelines: data on stdout, messages on stderr, `--json` on every
report, no interactivity required (`gpu up --yes`), distinct exit codes: 0 done, 1 failure (an audit problem
included), 2 usage, 3 paused on an endpoint error (`run` again resumes), 4 stopped at the rental's deadline.
`--dataset <folder>` (default: the current folder) comes before the command.

| Command | Does |
|---|---|
| `init <folder>` | writes `clutter_pairs.toml` from the template and opens the store |
| `plan` | samples scenes and clutter specs into the target cells with the largest shortfall |
| `gpu up --limit <h>` / `gpu judge` / `gpu down` | rents and releases the GPU through virtual_unstaging's provisioning; up records the rental with its price and deadline; judge serves the judge `[judge]` names on the live machine |
| `run [--smoke] [--fake]` | on a rental's first run, the smoke wave only; then waves of loops until the pair target or the deadline; `--fake` runs on the stand-in models |
| `report` | coverage, iteration curve, carry-forward under its decision rule, cost per accepted pair |
| `audit [<pair>]` | every check of the data model; with a pair id, its lineage tree (JSON) |
| `decide threshold <name> <value>` / `decide mark <assessment> right\|wrong` | records the owner's acts (`decision` rows) |
| `lessons [list\|retire\|promote] [<id>]` | lists the lessons with their validity and use; retires or promotes one from the next wave on (promotion prints the text to add to the instruction file in force) |
| `export <name>` | writes a dataset version: images, manifest, splits by building |
