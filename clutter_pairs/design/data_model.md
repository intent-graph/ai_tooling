# clutter_pairs — data model

The store of one dataset: what is declared, what is planned, what each loop made and why it was accepted or
rejected, what was sent to every model and what each request was built from. Refines
[Stored data](README.md#stored-data) of the high-level design.

> **Status:** *proposal* for slice 1, revised after review; not accepted. The DDL is [schema.sql](schema.sql): SQLite
> now; it avoids forward references and uses `BIGINT` and `DOUBLE PRECISION`, so moving to Postgres changes the ids
> only (`INTEGER PRIMARY KEY` here, an identity column there). Normalized to 3NF; the two denormalizations kept are
> named in the schema, each with the audit check that guards it.

## Table of Contents

1. [Principles](#principles) _(Lines 33-49)_
1. [Entities](#entities) _(Lines 52-84)_
1. [Schema](#schema) _(Lines 87-87)_
   1. [Declared files, texts, images](#declared-files-texts-images) _(Lines 90-115)_
   1. [The declared space and the targets](#the-declared-space-and-the-targets) _(Lines 118-162)_
   1. [Buildings, rooms, scenes, clutter specs](#buildings-rooms-scenes-clutter-specs) _(Lines 165-208)_
   1. [Rentals, runs, waves, loops, iterations](#rentals-runs-waves-loops-iterations) _(Lines 211-281)_
   1. [Models, calls, exchanges, and what each request was built from](#models-calls-exchanges-and-what-each-request-was-built-from) _(Lines 284-336)_
   1. [Assessments](#assessments) _(Lines 339-396)_
   1. [Lessons, decisions, and the parts of each request](#lessons-decisions-and-the-parts-of-each-request) _(Lines 399-476)_
   1. [Exports](#exports) _(Lines 479-507)_
1. [Views](#views) _(Lines 510-520)_
1. [Checks run by `audit`](#checks-run-by-audit) _(Lines 523-542)_


---

## Principles
<!-- Lines 33-49 -->

- **Facts once.** Every text a request is built from or answered with is stored once (`text_blob`, by hash); every
  declared file once (`source_file`); every image once (`image`; the bytes in the image store, by hash).
- **What was sent is stored, not rebuilt from code.** Each HTTP exchange of a model call is recorded from the
  endpoint's observer: the body with every embedded image replaced by its hash, the exact image bytes in the image
  store, and the hash of the bytes on the wire. Rebuilding a body is a substitution plus base64, independent of any
  library version (P8).
- **Axis values have a stable identity:** the natural key (axis name, value). A space version declares which values
  it allows; rooms, scenes, clutter specs, clutter items, lesson scopes and coverage targets point to the value, so
  coverage and lessons keep matching when the targets or the ontology change. A value an ontology drops stays in the
  registry, still pointed to by what used it; nothing new can use it.
- **Derived, not stored:** the pair, coverage, the iteration curve, the carry-forward comparison, costs are views.
- **Polymorphic references are avoided:** a row that can point to one of several kinds of source has one nullable
  foreign key per kind and a check that exactly the one matching its kind is set.
- **The dataset folder:** `store.sqlite`, `images/<first two hex>/<sha256>.<ext>`, `exports/<name>/`. Nothing in
  the package.

## Entities
<!-- Lines 52-84 -->

```mermaid
erDiagram
  SPACE_VERSION ||--o{ SPACE_VALUE : declares
  AXIS ||--o{ AXIS_VALUE : has
  AXIS_VALUE ||--o{ SPACE_VALUE : "declared by"
  SPACE_VERSION ||--o{ TARGET_SET : "targets over"
  TARGET_SET ||--o{ TARGET : wants
  SPACE_VERSION ||--o{ BUILDING : samples
  BUILDING ||--o{ ROOM : has
  ROOM ||--o{ SCENE : "seen from"
  SCENE ||--o{ CLUTTER_SPEC : "K variants"
  CLUTTER_SPEC ||--o{ CLUTTER_ITEM : lists
  RENTAL ||--o{ RUN : hosts
  RUN ||--o{ WAVE : "in order"
  WAVE ||--o{ LOOP_RUN : runs
  LOOP_RUN ||--o{ ITERATION : "n = 1, 2, ..."
  ITERATION ||--o{ ITERATION_IMAGE : made
  ITERATION ||--o{ MODEL_CALL : makes
  MODEL_CALL ||--o{ EXCHANGE : "sent as"
  MODEL_CALL ||--o{ COMPOSITION_PART : "built from"
  ITERATION ||--o{ ASSESSMENT : "assessed by"
  ASSESSMENT ||--o{ FINDING : lists
  ASSESSMENT ||--o{ LOCATED_ITEM : locates
  LESSON ||--o{ LESSON_EVIDENCE : "distilled from"
  EXPORT ||--o{ EXPORT_BUILDING : "splits by"
  EXPORT ||--o{ EXPORT_PAIR : contains
```

Left out of the diagram: the value tables, each linking its owner to one axis value per axis; `guidance`,
`measure`, `reason`, `model`, `decision`, and the files, texts and images every table points to.

## Schema

The DDL is [schema.sql](schema.sql): 42 tables in dependency order, loaded in SQLite and in Postgres 18. One line per
table here; each table's comments in the file carry its rules.

| Group | Table | Holds |
|---|---|---|
| declared files, texts, images | `source_file` | every declared file as read at first use: space, instructions, composers with their renderer, schemas, reasons, targets, configuration, decision rules |
| | `text_blob` | every text a request is built from or answered with, once |
| | `image` | image metadata; the bytes are in the image store |
| space and targets | `space_version` | one (ontology, taxonomy) pair; owns no axis, only declares values |
| | `axis`, `axis_value` | the registry of axes and values across versions: the natural key is the identity |
| | `space_value` | the values one space version allows |
| | `target_set`, `target`, `target_value` | a targets file over a space version; each target a cell (axis values) and a wanted count |
| hierarchy | `building`, `room`, `scene` | the owner's ids; a scene carries its seed |
| | `clutter_spec`, `clutter_item` | K variants per scene, each with its seed and its items |
| | `room_value`, `scene_value`, `clutter_spec_value`, `clutter_item_value` | one axis value per axis and owner |
| runs | `rental` | the GPU session: provider, GPU, hourly price, start, deadline |
| | `run` | its configuration, target set, pair target, rental |
| | `wave` | ordered across runs; the smoke wave flagged |
| | `loop_run` | stage, subject, the clean image a clutter loop received, the lessons arm, the engine and its stop rule, the stop reason |
| | `iteration`, `iteration_image` | the engine's action and the seed per iteration; the images it made by role; its verdict (a named denormalization) |
| calls | `model` | name, revision, family, licence |
| | `model_call` | role, model, composer, canonical request (the cache key), answer, output image, reuse, timings, error |
| | `exchange` | every HTTP exchange of a call as sent and answered: bodies with images by hash, the wire hash |
| | `composition_part` | the ordered parts of a request, each with its source: file, lesson, assessment, earlier call, image, setting, seed |
| assessments | `reason` | reason codes with their stage and fixed severity |
| | `assessment` | pixel, judge, detector or human; its verdict (a named denormalization) |
| | `finding`, `guidance`, `located_item` | the judge's findings (with its own severity recorded), its suggestions, the boxes of the items it located |
| | `measure` | pixel tests' values and the thresholds in force |
| lessons and decisions | `lesson`, `lesson_evidence`, `lesson_scope` | the text, the call that wrote it, what it replaces, the waves it is valid for, its evidence and scope |
| | `decision` | the owner's acts and every automatic rule's act |
| exports | `export`, `export_building`, `export_pair` | a named snapshot; the split per building; its pairs |

**Public ids.** The export never publishes store-local integers. A pair's id is the hash of its clean and cluttered
images' hashes; a scene's, a room's and a building's are the hash of their axis values and seeds (and, for a room
or a building, of their children's ids). They survive a rebuild of the store.

## Views
<!-- Lines 510-520 -->

| View | Gives | How |
|---|---|---|
| `clean_image` | accepted clean images, per scene (several when models are compared, S3) | the `generated` image of a clean loop's iteration with verdict `accept` |
| `pair` | one row per accepted pair: id (the accepted clutter iteration), building, room, scene, clutter spec; clean image (the loop's `input_image`), cluttered (`composite`), mask (`change_mask`); the clean generator's family and the editor's | the clutter loop's accepted iteration; the families from the call that made `input_image` and from the edit call |
| `coverage` | per target of a target set: pairs wanted, pairs accepted | relational division on (axis, value): pairs whose room, scene and clutter values include every value of the target, whatever the space version |
| `iteration_curve` | per stage, loops in wave order with their iterations and stop reason | descriptive only |
| `carry_forward` | per stage and arm (`on`, `off`): loops, accepted share, mean iterations to acceptance | loops in waves after the stage's first lesson became active, the lessons' evidence loops excluded; the decision rule is in [loops.md](loops.md#measuring-carry-forward) |
| `lesson_use` | per lesson: the loops whose first request cited it | `composition_part` rows of kind `lesson`; descriptive (per-lesson effects: slice 2) |
| `cost` | per run: rental price × wall clock; per stage and model: calls, wall seconds, generator GPU-seconds, reused calls; cost per accepted pair | `rental`, `model_call` |

## Checks run by `audit`
<!-- Lines 523-542 -->

Requests and records:
- **P9:** every request recomposes: the composer file, the call's model and the parts in order give the request
  stored under `request_sha`, byte for byte; every part's text is its source's rendering (an instruction part is its
  file, a lesson part its lesson, a spec part its loop subject's spec rendered by the composer's renderer).
- **P8:** every exchange's body rebuilds: its stored text with each image reference replaced by the base64 of the
  stored bytes, or its stored image, hashes to `wire_sha`.
- Every image hash has its bytes in the image store, and the bytes hash to it.

Denormalizations and rules:
- `iteration.verdict` and `assessment.verdict` equal the verdict rule applied to the findings and the reasons'
  severities; `stop_reason = 'accepted'` exactly when the loop has an iteration with verdict `accept`.
- A clutter loop's `input_image` is the `generated` image of an accepted iteration of a clean loop of the same scene.
- An image role fits its loop's stage (`generated` on clean loops only; the other roles on clutter loops only).

Space and exports:
- Every owner holds exactly one value for every axis that applies to its kind, and each value is declared by its
  building's space version (`space_value`).
- Every exported pair is an accepted clutter iteration, and its building has a split row in that export.
- **P1:** for every pair, clean and cluttered images are equal wherever the mask's alpha is 0.
