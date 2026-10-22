# clutter_pairs — aids for the judges

What else a judge could be given besides the images and the spec (segmentation, detection, a mask made readable,
ready-made knowledge), which failure each aid targets, what it costs, and how to tell whether it helps.
Explores the owner's idea of 2026-10-22: "provide the judge with more info, like segmentation, object detection
etc."; "giving ready-made knowledge about what is movable or not might help, as text".

> **Status:** brainstorm; nothing decided except the knowledge text, which is implemented. Grounds: the first
> rental's stored findings (2026-10-22, one A100, FLUX.2 klein 4B; Qwen3-VL-8B, then Qwen3.8-27B as judge) and
> virtual_unstaging's tool server and survey.

## Table of Contents

1. [N0](#n0) _(Lines 27-36)_
1. [What failed](#what-failed) _(Lines 39-51)_
1. [The aids](#the-aids) _(Lines 54-66)_
1. [Forms and costs](#forms-and-costs) _(Lines 69-79)_
1. [What changes in the data model](#what-changes-in-the-data-model) _(Lines 82-91)_
1. [Measuring an aid: the judge bench](#measuring-an-aid-the-judge-bench) _(Lines 94-106)_
1. [Proposed order](#proposed-order) _(Lines 109-117)_
1. [Open](#open) _(Lines 120-124)_

---

## N0
<!-- Lines 27-36 -->

- The judges failed in two ways on the first rental: they reported things that are not problems (fixed elements as
  movable, acceptable placements as violations), and they located items too loosely for the explained-change test.
  Neither is a failure of the images.
- The cheapest aids need no model: ready-made knowledge as text (done), and the change mask's components drawn and
  numbered so the judge assigns each to an item instead of drawing boxes. Model-based aids (open-vocabulary
  detection and segmentation, semantic class changes) already exist as tools of virtual_unstaging's tool server.
- Whether an aid helps is measured without generating anything: stored iterations are judged again with and without
  it and compared with the owner's marks (the judge bench, below).

## What failed
<!-- Lines 39-51 -->

Clutter iterations with the 27B judge (dataset of the first rental, 149 iterations, 113 judged), blocking codes:

| Code | Iterations | What the stored comments show |
|---|---|---|
| `unexplained_change` (pixels) | 81 | the judge's boxes miss part of an item or its shadow; small changes along frames |
| `clutter_off_spec` (judge) | 75 | many marked minor by the judge itself ("acceptable"); now split into a `_minor` twin |
| `scene_changed` | 50 | often real: an unlisted mirror, a window turned into a door, a dark patch on a wall |
| `placement_violation` | 46 | rules misread or applied to acceptable placements; now split |
| `global_repaint` (pixels) | 32 | colour shift of the edit; a threshold for the owner |

With Qwen3-VL-8B the clean judge also rejected built-in fireplaces and radiators listed as fixed.

## The aids
<!-- Lines 54-66 -->

| Aid | For | Targets | How it is made |
|---|---|---|---|
| **A1 Knowledge, as text** | both judges | fixed elements taken for movable; movable ones missed (logs in a hearth) | a versioned file, `data/knowledge/fixed_and_movable.md`: the test (does it leave with the occupants?), the two lists, ambiguous cases ruled. **Implemented** |
| **A2 Numbered components** | pair judge | loose boxes, `unexplained_change` | the change mask's connected components, outlined and numbered on the cluttered image; the judge answers, per component, the item it is or "not an item" (a scene change). No model; a pure function of stored images |
| **A3 Component crops** | pair judge | small changes missed or invented; `scene_changed` | per component, the clean and cluttered crops side by side, enlarged; vision-language models are weak at spotting differences between two whole images (survey: VDiff-Bench, MMVP) |
| **A4 Detection of the listed items** | pair judge | `item_missing`, `clutter_off_spec` | `segment_elements` (Grounding DINO then SAM 2.1) on the cluttered image with the items' labels; given as a list (label, score, box) or drawn |
| **A5 Detection of movable things** | clean judge | `not_empty` missed or invented | `segment_elements` on the clean image with the movable labels of A1's list; an empty result is evidence the room is empty |
| **A6 Semantic class change** | pair judge | `scene_changed` outside the items (a window become a door) | `class_diff` (ADE20K classes) of clean and cluttered images, restricted to what changed outside the components assigned to items |

A2 also changes the explained-change test: instead of comparing components with boxes, it reads the judge's
assignment; a component assigned to no item is a scene change, by the judge's own answer.

## Forms and costs
<!-- Lines 69-79 -->

| Form | Example | Cost to the judge | Risk |
|---|---|---|---|
| text | A1; A4's detections as lines | a few hundred tokens | a detector's false positives read as facts |
| overlay on an existing image | A2's numbered outlines | none extra (replaces the mask image) | marks hide what they cover |
| extra images | A3's crops | one image each (Qwen-VL: about a thousand tokens per megapixel) | many components, many images: cap at the largest few |

Model-based aids (A4 to A6) run on the tool server beside the generator (`ProjectPlan.tools`, a by-name list, today
empty for clutter_pairs). Their memory beside klein 4B (20 GB) and the 27B judge (44 GB) is *inferred* to fit in
80 GB; not measured. Their seconds per image are not measured either.

## What changes in the data model
<!-- Lines 82-91 -->

- **A1:** nothing: the knowledge file is an `instruction` part, recorded and recomposed like the others.
- **A2, A3:** an image derived from stored images by a pure function (outline and numbers, crops) is a new source of
  a part: the function's name and version, and the images it was computed from, so `audit` can recompute it, as it
  re-renders a spec today. The pair judge's schema gains a component assignment; `located_item` keeps the boxes or
  gives way to an assignment table.
- **A4 to A6:** a tool run is a call that the data model does not have yet: `model_call` roles cover write, generate,
  edit, judge, revise and distill. A tool run needs its request and answer recorded the same way (P8, P9): a new
  role, or a table of its own.

## Measuring an aid: the judge bench
<!-- Lines 94-106 -->

The images of every iteration are stored, so a judge variant can be tried without generating anything:

1. **Ground truth:** the owner marks the verdicts on a sample of stored iterations (S4: 20 to 30 pairs, through
   `cpairs decide mark`), both stages, both accepted and rejected ones.
2. **Re-judge:** each variant (judge model, instruction version, aid) judges the same stored iterations again; its
   calls are recorded like any other, under a run of their own.
3. **Compare:** per variant, agreement with the owner's marks on accept or reject, false rejections, false
   acceptances, per code; seconds per judgment.

Cost: judge calls only, about 20 s each with the 27B judge; 50 iterations times 4 variants is about an hour of judge
time on one rental, less in parallel. This needs a `rejudge` command, and the owner's marks first.

## Proposed order
<!-- Lines 109-117 -->

*Proposal*, cheapest and most targeted first:

1. A1 (done) and the code split (done): measure on the next rental.
2. A2, numbered components: no model, aims at the largest blocker, makes the explained-change test exact.
3. The judge bench, with the owner's marks: from then on every aid is measured before it is kept.
4. A3 crops for `scene_changed`, if the bench shows missed or invented changes.
5. A4 to A6, if a gap remains that only a detector closes; then the data model's tool-run record first.

## Open
<!-- Lines 120-124 -->

- Which aids to build, in which order (owner).
- The owner's marks for the judge bench: when, on which sample.
- Whether the writers should get A1 too (the clean writer kept naming logs and hearths).
- A tool run's record: a `model_call` role or its own table.
