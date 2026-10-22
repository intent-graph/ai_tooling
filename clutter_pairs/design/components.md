# clutter_pairs — components and use of virtual_unstaging

What clutter_pairs takes from virtual_unstaging and on which of its names it relies, how its own package is layered,
what a dataset folder holds, and the command line. Refines [C7](README.md#c7-model-serving) and
[C10](README.md#c10-loop-code) of the design.

> **Status:** *proposal* for slice 1, revised after review; not accepted.

## Table of Contents

1. [Use of virtual_unstaging](#use-of-virtual_unstaging) _(Lines 21-42)_
1. [Components and layering](#components-and-layering) _(Lines 45-58)_
1. [The dataset folder](#the-dataset-folder) _(Lines 61-69)_
1. [Command line](#command-line) _(Lines 72-86)_


---

## Use of virtual_unstaging
<!-- Lines 21-42 -->

Imported as a package (path dependency), never copied. The owner's rule: virtual_unstaging changes only by adding
modularity or override mechanisms that keep its own behaviour by default and never name clutter_pairs; text-to-image
is the one exception the owner accepted.

| Need | Taken from virtual_unstaging | Extension point it relies on |
|---|---|---|
| rent one GPU with a deadline, serving the generator and the judge | `provision.lifecycle` (`up`, `down`), with a plan built from clutter_pairs' configuration; the session file lands in the dataset folder | `Context.plan_source`; `ProjectPlan.tools = ()` (no segmentation models loaded) |
| make a clean image from text, edit it | `clients.toolserver.ToolServerClient`, `clients.generators.ToolServerGenerator`, the packaged recipes | recipe `text_only` (tool server API 1.2; the accepted exception) |
| judge, write, revise, distill | `clients.openai_compatible.chat_json` (streamed, JSON-schema answers; free text through a one-field schema; the sampling seed through its `extra` argument) | none |
| record every exchange as sent | — | `clients.http.Endpoint.observer` (what it raises fails the call) |
| the loop's policy and resume | — | `engines.SearchEngine[Problem, Candidate, Evaluation]`, `engines.replay`, `ReplayMismatch` |
| images, hashes, store plumbing, secrets | `imaging`, `domain.sha256_text` and `canonical_json`, `store.blobs.BlobStore`, `store.db.connect` and `transaction`, `config.Secret` | none |
| tests | `clients.fakes.FakeGenerator` (also from text alone) | none |

Not used: virtual_unstaging's project configuration, store schema, runner, judge, registry, review and command line.

**The surface relied on is declared on both sides.** The names above are the whole surface: virtual_unstaging's
design lists them as the names a program that imports it may rely on, without naming any such program; the
repository's instructions say that a change to virtual_unstaging also runs clutter_pairs' tests. A name used here and
missing from that list is a defect of this page.

## Components and layering
<!-- Lines 45-58 -->

One package, `clutter_pairs`, layered like virtual_unstaging and checked the same way (`lint-imports`):

| Layer | Modules |
|---|---|
| presentation | `cli` |
| application | `run` (waves, the driver around `engines.replay`), `plan` (sampling into target cells, arms), `export`, `audit`, `report`, `gpu` (provisioning glue) |
| adapters | `models` (generator, judge and writer callers), `recorder` (the observer: exchanges, image bytes, wire hashes), `store` (schema, queries, views) |
| pure core | `compose` (composers and spec rendering), `pairs` (size check, correction, mask, composite, explained change), `lessons` (validity, selection by scope), `engine` (the reviser's policy and stop rule), `space` (ontology, taxonomy, targets) |
| domain | the types |

Data files ship in the package: `instructions/`, `composers/`, `schemas/`, `space/`, `reasons.toml`,
`decision_rules/`.

## The dataset folder
<!-- Lines 61-69 -->

Outside the package, one per dataset:

- `clutter_pairs.toml`: models (generator recipe, judge model, each with its family), the GPU plan, the run's pair
  target, loop settings (maximum iterations, wave width, lessons per request, share of the `off` arm), file
  overrides. Secrets only by key file or key command (`config.Secret`); endpoints from the session file the rental
  writes.
- `store.sqlite`, `images/`, `exports/`, and the rental's session file while a GPU is up.

## Command line
<!-- Lines 72-86 -->

Name `cpairs`, provisional. Per the repository's CLI guidelines: data on stdout, messages on stderr, `--json` on every
report, no interactivity required, distinct exit codes for usage errors, an unreachable endpoint, a reached deadline.

| Command | Does |
|---|---|
| `init <folder>` | writes `clutter_pairs.toml` with the default space and models |
| `plan` | samples scenes and clutter specs into the thinnest target cells, draws the arms |
| `gpu up --limit <h>` / `gpu down` | rents and releases the GPU through virtual_unstaging's provisioning; up shows the price and the deadline |
| `run [--smoke]` | runs waves of loops until the pair target or the deadline; `--smoke` runs the smoke wave only |
| `report` | coverage, iteration curve, carry-forward under its decision rule, cost per accepted pair |
| `audit [<pair>]` | every check of the data model; with a pair, its lineage tree |
| `decide` | records the owner's acts: thresholds, review marks |
| `lessons [retire|promote]` | lists the lessons with their validity and use; retires or promotes one |
| `export <name>` | writes a dataset version: images, manifest, splits by building |
