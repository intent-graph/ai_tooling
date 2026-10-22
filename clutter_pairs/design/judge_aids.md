# clutter_pairs — aids for the judges

What else a judge could be given besides the images and the spec (segmentation, detection, a mask made readable,
ready-made knowledge), which failure each aid targets, what it costs, and how to tell whether it helps.
Explores the owner's idea of 2026-10-22: "provide the judge with more info, like segmentation, object detection
etc."; "giving ready-made knowledge about what is movable or not might help, as text".

> **Status:** brainstorm, except two aids decided by the owner and implemented: the knowledge text (A1) and the
> numbered regions (A2, "A2 seems to be OK", 2026-10-22), with a rule for openings. Grounds: the first
> rental's stored findings (2026-10-22, one A100, FLUX.2 klein 4B; Qwen3-VL-8B, then Qwen3.8-27B as judge) and
> virtual_unstaging's tool server and survey.

## Table of Contents

1. [N0](#n0) _(Lines 30-40)_
1. [What failed](#what-failed) _(Lines 43-55)_
1. [The aids](#the-aids) _(Lines 58-70)_
1. [A2 and openings in detail](#a2-and-openings-in-detail) _(Lines 73-112)_
1. [Forms and costs](#forms-and-costs) _(Lines 115-125)_
1. [What changes in the data model](#what-changes-in-the-data-model) _(Lines 128-138)_
1. [Measuring an aid: the judge bench](#measuring-an-aid-the-judge-bench) _(Lines 141-153)_
1. [Proposed order](#proposed-order) _(Lines 156-163)_
1. [Open](#open) _(Lines 166-170)_


---

## N0
<!-- Lines 30-40 -->

- The judges failed in two ways on the first rental: they reported things that are not problems (fixed elements as
  movable, acceptable placements as violations), and they located items too loosely for the explained-change test.
  Neither is a failure of the images.
- The cheapest aids need no model: ready-made knowledge as text, and the change mask's regions drawn and numbered
  so the judge assigns each to an item instead of drawing boxes (both implemented). An invented or changed opening
  is the worst defect a pair can carry (owner, 2026-10-22): it has its own blocking code. Model-based aids (open-vocabulary
  detection and segmentation, semantic class changes) already exist as tools of virtual_unstaging's tool server.
- Whether an aid helps is measured without generating anything: stored iterations are judged again with and without
  it and compared with the owner's marks (the judge bench, below).

## What failed
<!-- Lines 43-55 -->

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
<!-- Lines 58-70 -->

| Aid | For | Targets | How it is made |
|---|---|---|---|
| **A1 Knowledge, as text** | both judges | fixed elements taken for movable; movable ones missed (logs in a hearth) | a versioned file, `data/knowledge/fixed_and_movable.md`: the test (does it leave with the occupants?), the two lists, ambiguous cases ruled. **Implemented** |
| **A2 Numbered regions** | pair judge | loose boxes, `unexplained_change`, openings changed beside an item | the change mask's regions, outlined and numbered on the cluttered image; the judge answers, per region, the items it holds, or none (a scene change). No model; a pure function of stored images. **Implemented**, [below](#a2-and-openings-in-detail) |
| **A3 Component crops** | pair judge | small changes missed or invented; `scene_changed` | per component, the clean and cluttered crops side by side, enlarged; vision-language models are weak at spotting differences between two whole images (survey: VDiff-Bench, MMVP) |
| **A4 Detection of the listed items** | pair judge | `item_missing`, `clutter_off_spec` | `segment_elements` (Grounding DINO then SAM 2.1) on the cluttered image with the items' labels; given as a list (label, score, box) or drawn |
| **A5 Detection of movable things** | clean judge | `not_empty` missed or invented | `segment_elements` on the clean image with the movable labels of A1's list; an empty result is evidence the room is empty |
| **A6 Semantic class change** | pair judge | `scene_changed` outside the items (a window become a door) | `class_diff` (ADE20K classes) of clean and cluttered images, restricted to what changed outside the components assigned to items |

A2 also changes the explained-change test: instead of comparing components with boxes, it reads the judge's
assignment; a region assigned to no item is a scene change, by the judge's own answer.

## A2 and openings in detail
<!-- Lines 73-112 -->

Owner, 2026-10-22: "A2 seems to be OK"; "I think the recurring issue I saw was inventing openings. this is the
biggest no no". The first rental's stored comments show it in this package too: the editor turned a window into a
door. A pair that carries it teaches a decluttering model to change openings, in either direction.

**Regions.** A pure function of the stored change mask (its alpha at 255, so `audit` recomputes it exactly):
the mask's pieces closer than `region_group_px` (16) are grouped into one region, so an item and its shadow, split by
the threshold, are one number; a region with fewer than `region_min_px` (500) mask pixels is a speck, left unnumbered
and measured (`speck_share`); the others are numbered by size, largest first, up to `max_regions` (12); a region past
the cap is unexplained. Calibration on the first rental's 150 stored masks: median 3 regions per image, 90th
percentile 5, maximum 8; specks a median 0.1 % of the mask, 0.3 % at the 90th percentile. With no grouping and the
rental's 2,000-pixel floor: median 3, maximum 11, specks up to 3.1 % of the mask.

**The image the judge reads** replaces the bare mask: the cluttered image with each region's outline drawn and its
number in a black box on its first pixel (topmost row, then leftmost), drawn with a built-in digit font so the bytes do not depend on a font
installed on the machine. It is stored as the iteration's `regions` image; the drawing's version is recorded as the
measure `region_drawing`; `audit` redraws it from the stored composite and mask and compares the pixels.

**The judge's answer** ([schema](../src/clutter_pairs/data/schemas/pair_judgment.json)): per numbered region, the
listed items it holds (an item's shadow and reflection belong to it), possibly none; findings as before, each
citing the regions it concerns. The pair judge's instruction puts openings first: before anything else, compare
every door, window and passage of the two images.

**Explained change:** a region is explained when the judge assigns at least one item to it. A region with no item,
or with no answer, is an `unexplained_change` (blocking), whatever finding cites it: inside the mask, every change
must be a specified item (P1). A finding that cites it gives the reason.

**Openings:** the code `opening_changed` (blocking, never a `_minor` twin): a door, window or passage appeared,
vanished, moved, changed size or changed kind (a window became a door) between the clean and the cluttered image;
an opening partly hidden behind an added item is not a change. It catches the case the region test cannot: an
opening changed inside a region that also holds an item, since grouping can join them. The placement rules keep
openings visible (furniture never in front of a door, a window or a radiator; nothing on a wall across a door or a
window): a wholly hidden opening would teach a decluttering model to invent one. The placement "hanging on a door"
is removed from the taxonomy (owner, 2026-10-22, "remove"): asked for where the clean image
showed no door, the editor drew one. In the first rental, 14 of the 30 iterations with such an item had a door
invented or a window turned into one by the judge's comments, against 8 of the 122 without.

**Limits:** a judge that assigns an item to a region holding a scene change and reports nothing passes it; the
judge bench measures that. Region numbers drawn on the image hide a few pixels under them.

## Forms and costs
<!-- Lines 115-125 -->

| Form | Example | Cost to the judge | Risk |
|---|---|---|---|
| text | A1; A4's detections as lines | a few hundred tokens | a detector's false positives read as facts |
| overlay on an existing image | A2's numbered outlines | none extra (replaces the mask image) | marks hide what they cover |
| extra images | A3's crops | one image each (Qwen-VL: about a thousand tokens per megapixel) | many components, many images: cap at the largest few |

Model-based aids (A4 to A6) run on the tool server beside the generator (`ProjectPlan.tools`, a by-name list, today
empty for clutter_pairs). Their memory beside klein 4B (20 GB) and the 27B judge (44 GB) is *inferred* to fit in
80 GB; not measured. Their seconds per image are not measured either.

## What changes in the data model
<!-- Lines 128-138 -->

- **A1:** nothing: the knowledge file is an `instruction` part, recorded and recomposed like the others.
- **A2 (implemented, schema version 2):** the iteration image role `regions`; `mask_region` (the numbered regions
  of an iteration: box and mask pixels); `region_item` (the judge's assignment) replaces `located_item`;
  `finding_region` (the regions a finding cites); the drawing's version as a measure. A store of version 1 is
  refused by this code; the judge bench, when it re-judges the first rental's iterations, needs a migration.
- **A3:** crops derived by a pure function, recorded the same way as A2's image.
- **A4 to A6:** a tool run is a call that the data model does not have yet: `model_call` roles cover write, generate,
  edit, judge, revise and distill. A tool run needs its request and answer recorded the same way (P8, P9): a new
  role, or a table of its own.

## Measuring an aid: the judge bench
<!-- Lines 141-153 -->

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
<!-- Lines 156-163 -->

*Proposal*, cheapest and most targeted first:

1. A1, the code split, A2 and `opening_changed` (all implemented): measure on the next rental.
2. The judge bench, with the owner's marks: from then on every aid is measured before it is kept.
3. A3 crops for `scene_changed`, if the bench shows missed or invented changes.
4. A4 to A6, if a gap remains that only a detector closes; then the data model's tool-run record first.

## Open
<!-- Lines 166-170 -->

- Which aids to build after A2, in which order (owner).
- The owner's marks for the judge bench: when, on which sample.
- Whether the writers should get A1 too (the clean writer kept naming logs and hearths).
- A tool run's record: a `model_call` role or its own table.
