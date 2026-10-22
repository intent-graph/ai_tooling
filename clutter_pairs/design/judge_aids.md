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

1. [N0](#n0) _(Lines 30-41)_
1. [What failed](#what-failed) _(Lines 44-56)_
1. [The aids](#the-aids) _(Lines 59-71)_
1. [A2 and openings in detail](#a2-and-openings-in-detail) _(Lines 74-127)_
1. [Forms and costs](#forms-and-costs) _(Lines 130-140)_
1. [What changes in the data model](#what-changes-in-the-data-model) _(Lines 143-155)_
1. [Measuring an aid: the judge bench](#measuring-an-aid-the-judge-bench) _(Lines 158-176)_
1. [Proposed order](#proposed-order) _(Lines 179-186)_
1. [Open](#open) _(Lines 189-193)_


---

## N0
<!-- Lines 30-41 -->

- The judges failed in two ways on the first rental: they reported things that are not problems (fixed elements as
  movable, acceptable placements as violations), and they located items too loosely for the explained-change test.
  Neither is a failure of the images.
- The cheapest aids need no model: ready-made knowledge as text, and the change mask's regions drawn and numbered
  so the judge assigns each to an item instead of drawing boxes (both implemented). An invented or changed opening
  is the worst defect a pair can carry (owner, 2026-10-22): the judge answers a checklist of openings before anything
  else, and any change in it blocks the pair. Model-based aids (open-vocabulary
  detection and segmentation, semantic class changes) already exist as tools of virtual_unstaging's tool server.
- Whether an aid helps is measured without generating anything: stored iterations are judged again with and without
  it and compared with the owner's marks (the judge bench, below).

## What failed
<!-- Lines 44-56 -->

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
<!-- Lines 59-71 -->

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
<!-- Lines 74-127 -->

Owner, 2026-10-22: "A2 seems to be OK"; "I think the recurring issue I saw was inventing openings. this is the
biggest no no"; after an independent review, "fix all". The first rental's stored comments show it in this package
too: the editor turned a window into a door. A pair that carries it teaches a decluttering model to change openings,
in either direction.

**Regions.** A pure function of the stored change mask (its alpha at 255, so `audit` recomputes it exactly): each
piece of the mask is dilated by `region_group_px` (16), so pieces less than about twice that apart (an item and its
shadow, split by the threshold) are one region; a region with fewer than `region_min_px` (250) mask pixels is a
speck, left unnumbered; the others are numbered by size, largest first. At most `max_regions` (12, the answer
schema's limit; a test keeps them equal) are drawn; a region past the cap is unexplained. Specks together may cover
at most `max_speck_share` (0.5 %) of the mask, otherwise `unexplained_change`. Calibration on the first rental's 150
stored masks: median 3 regions per image, 90th percentile 7, maximum 11; specks a median 0.0 % of the mask, 0.1 % at
the 90th percentile. Every iteration whose regions were computed has a region set: the thresholds used, the
drawing's version and the speck pixels, even when no region was numbered.

**The image the judge reads** replaces the bare mask: the cluttered image with each region outlined just outside its
pixels (yellow on a black halo, never over a mask pixel) and its number in a black box outside the region, centred on its topmost pixel: above
its box, else below, left or right, the first place that covers no mask pixel and no other number (else the one that
covers the fewest). The digits come from a built-in bitmap, so the pixels do not depend on a font installed on the
machine. It is stored as the iteration's `regions` image; `audit` redraws it from the stored composite and region
set and compares the pixels.

**The judge's answer** ([schema](../src/clutter_pairs/data/schemas/pair_judgment.json)), in this order, which the
constrained decoding enforces, so the model answers the openings before anything else:
1. `openings`: every door, window and passage of the clean image, each with its kind, where it is, its status in
   the cluttered image (`unchanged`, `partly_hidden` behind an added item, `changed` in place, size or kind,
   `vanished`) and the regions it falls in;
2. `appeared`: every door, window or passage of the cluttered image that the clean image does not have;
3. `regions`: per numbered region, the listed items it holds (an item's shadow and reflection belong to it), and
   `other_change`: whether it also holds a change that is not a listed item;
4. `findings` and `guidance`, as before; a finding cites the regions it concerns.

**Openings:** the code derives one `opening_changed` finding (blocking, never a `_minor` twin) for each opening
`changed` or `vanished` and each one that `appeared`, recorded in the judge's assessment with the regions it cites;
the judge cannot write that code itself, so the checklist is its only channel. The placement rules keep openings
visible (furniture never in front of a door, a window or a radiator; nothing on a wall across a door or a window):
a wholly hidden opening would teach a decluttering model to invent one. The placement "hanging on a door" is
removed from the taxonomy (owner, 2026-10-22, "remove"): asked for where the clean image showed no door, the
editor drew one. In the first rental, 14 of the 30 iterations with such an item had a door invented or a window
turned into one by the judge's comments, against 8 of the 122 without. For the same reason the clutter writer and
reviser see the clean image ([loops](loops.md)): a writer that cannot see the room was told to anchor items under a
window or on a hearth that may not exist.

**Explained change:** a region is explained when the judge answers it once, assigns it at least one item, and says
it holds no other change. A region with no answer, two answers, no item or another change is an
`unexplained_change` (blocking), whatever finding cites it: inside the mask, every change must be a specified item
(P1, checked on every numbered region and bounded on the specks). The measure `regions_unanswered` counts regions
the judge left out or answered twice.

**Limits:** a judge that answers every region with every item and no other change passes the region test; the
judge bench measures how often the judge's answers are right, and the share of regions holding every item is
recorded for it. A numbered label or an outline hides a few pixels next to a region, never in it.

## Forms and costs
<!-- Lines 130-140 -->

| Form | Example | Cost to the judge | Risk |
|---|---|---|---|
| text | A1; A4's detections as lines | a few hundred tokens | a detector's false positives read as facts |
| overlay on an existing image | A2's numbered outlines | none extra (replaces the mask image) | marks hide what they cover |
| extra images | A3's crops | one image each (Qwen-VL: about a thousand tokens per megapixel) | many components, many images: cap at the largest few |

Model-based aids (A4 to A6) run on the tool server beside the generator (`ProjectPlan.tools`, a by-name list, today
empty for clutter_pairs). Their memory beside klein 4B (20 GB) and the 27B judge (44 GB) is *inferred* to fit in
80 GB; not measured. Their seconds per image are not measured either.

## What changes in the data model
<!-- Lines 143-155 -->

- **A1:** nothing: the knowledge file is an `instruction` part, recorded and recomposed like the others.
- **A2 (implemented, schema version 2):** the iteration image role `regions`; `region_set` (per iteration: the
  thresholds, the drawing's version, the speck pixels) and `mask_region` (its numbered regions: box and mask pixels);
  `region_answer` (the judge's answer per region: `other_change`) and `region_item` (the items it assigns) replace
  `located_item`; `finding_region` (the regions a finding cites). The openings checklist is read from the stored
  answer; its consequences are the derived `opening_changed` findings. A store of version 1 is refused by this code;
  the judge bench, when it re-judges the first rental's iterations through the package, needs a migration.
- **A3:** crops derived by a pure function, recorded the same way as A2's image.
- **A4 to A6:** a tool run is a call that the data model does not have yet: `model_call` roles cover write, generate,
  edit, judge, revise and distill. A tool run needs its request and answer recorded the same way (P8, P9): a new
  role, or a table of its own.

## Measuring an aid: the judge bench
<!-- Lines 158-176 -->

The images of every iteration are stored, so a judge variant can be tried without generating anything:

1. **Ground truth:** the owner marks the verdicts on a sample of stored iterations (S4: 20 to 30 pairs, through
   `cpairs decide mark`), both stages, both accepted and rejected ones.
2. **Re-judge:** each variant (judge model, instruction version, aid) judges the same stored iterations again; its
   calls are recorded like any other, under a run of their own.
3. **Compare:** per variant, agreement with the owner's marks on accept or reject, false rejections, false
   acceptances, per code; seconds per judgment.

Cost: judge calls only, about 20 s each with the 27B judge; 50 iterations times 4 variants is about an hour of judge
time on one rental, less in parallel. This needs a `rejudge` command, and the owner's marks first.

**First measurement, before the bench exists:** at the start of the second rental, the iterations of the first one
in which the 27B judge described a changed opening (27) and about as many in which no judge mentioned one are judged
again with the openings checklist, by a one-off script kept with the run's results that stores each request and
answer. It gives the checklist's rate of catching known changed openings; the iterations without a mention are only
weak negatives until the owner marks them.

## Proposed order
<!-- Lines 179-186 -->

*Proposal*, cheapest and most targeted first:

1. A1, the code split, A2 and `opening_changed` (all implemented): measure on the next rental.
2. The judge bench, with the owner's marks: from then on every aid is measured before it is kept.
3. A3 crops for `scene_changed`, if the bench shows missed or invented changes.
4. A4 to A6, if a gap remains that only a detector closes; then the data model's tool-run record first.

## Open
<!-- Lines 189-193 -->

- Which aids to build after A2, in which order (owner).
- The owner's marks for the judge bench: when, on which sample.
- Whether the writers should get A1 too (the clean writer kept naming logs and hearths).
- A tool run's record: a `model_call` role or its own table.
