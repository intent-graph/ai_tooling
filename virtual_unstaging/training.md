# Training the prompts

The offline layer of [architecture.md](architecture.md#base-instructions--offline-optimization) is a machine-learning
project: instead of training to find the right weights of a model, we train to find the right prompts of the
models in use. It faces the classical questions: training data, a performance measure, and an efficient way
to explore the solution space and converge.

> **Status:** the framing and the three questions are the owner's, as is the need for a synthetic benchmark,
> built as a separate project ([clutter_pairs](../clutter_pairs/README.md)). Everything marked *proposal* is the
> assistant's and not decided.

## Table of Contents

1. [Parameters](#parameters) _(Lines 25-33)_
1. [Training data](#training-data) _(Lines 36-48)_
1. [Performance measure](#performance-measure) _(Lines 51-66)_
1. [Exploring the solution space](#exploring-the-solution-space) _(Lines 69-85)_
1. [Train the judge first](#train-the-judge-first) _(Lines 88-96)_
1. [Generalization](#generalization) _(Lines 99-104)_

---

## Parameters
<!-- Lines 25-33 -->

- **Trained:** the base instruction set of each model role, per model (generator, judge, and when they are
  models, reviewer and rewriter).
- *Proposal* — **hyperparameters**, discrete and searched alongside: number and choice of reference images,
  guide types offered to the generator, which tools the judge may call, per-photo budget, stopping rule.
- *Proposal* — the judge's guiding instructions are a **learned optimizer**: loop 1 optimizes one photo at
  run time, the offline training optimizes how loop 1 optimizes. This is the meta-learning pattern; it
  means the judge is scored both on its verdicts and on how fast its guidance converges.

## Training data
<!-- Lines 36-48 -->

- A **synthetic benchmark** with known ground truth: pairs of the same view, clean and cluttered, produced by
  a separate project, [clutter_pairs](../clutter_pairs/architecture.md). Its contract is the pair only.
- *Proposal* — **derived here, not there:**
  - labels of the clean image (per-pixel classes, depth), from the judge's tool library;
  - **judge triplets** (original, candidate, typed defects with regions): run a generator on the cluttered
    image and label its output against the clean one where the structure differs;
  - **injected defects**: from a correct pair, inject one typed defect at a known region (paste a door,
    erase a radiator, shift the viewpoint or the colour, leave an object); exact labels, cheap, balanced
    across defect types, to be checked against the generator's own failures.
- *Proposal:* **real reviewed photos** (typed human reviews from actual tasks) as a held-out test set only,
  to measure the gap between synthetic and real; never tuned on.

## Performance measure
<!-- Lines 51-66 -->

*Proposal.* Several measures, each at the height of what it judges; one index to optimize at the top.

| Level | Measure | Against |
|---|---|---|
| system (the index) | share of photos delivered without a blocking defect, within budget; cost per accepted photo; fallback rate | ground truth or typed review |
| generator, inside the removed region | **structural** agreement with the true empty view: same class per pixel (wall stays wall, no door where there is none), same depth plane | ground-truth segmentation and depth |
| generator, outside the region | preservation: perceptual distance to the original, optical-flow drift | original |
| judge, as a classifier | recall and precision per defect type | defect labels |
| judge, as a guide | iterations and compute for loop 1 to reach acceptance | system index |

- Pixel equality with the ground truth inside the removed region is **not** a goal: invention is allowed if it
  is structurally right (a plain wall where the truth is a plain wall).
- Measures stay **per defect type** (a Pareto front) during the search; they are reduced to one number only
  for the final index.

## Exploring the solution space
<!-- Lines 69-85 -->

*Proposal.* There is no numeric gradient on a prompt; its analogues:

- **Textual gradient:** a critique of the failures, aggregated by defect type, says in which direction to
  change the instructions. Loop 2b of the architecture is already one such step. TextGrad formalizes it
  (https://arxiv.org/abs/2406.07496).
- **Reflective evolution with Pareto selection:** GEPA (https://arxiv.org/abs/2507.19457).
- **LLM as optimizer over a scored history of candidates:** OPRO (https://arxiv.org/abs/2309.03409).
- **Bayesian search over instruction and example candidates:** the DSPy optimizers (MIPROv2,
  https://dspy.ai).
- **Efficiency:** minibatches; cheap proxies (fewer diffusion steps, lower resolution) for early rounds;
  successive halving across candidates; caching generator outputs whenever only the judge changes; several
  seeds per evaluation, since generators are stochastic and a difference smaller than the seed noise is no
  signal.

None of these has been evaluated here.

## Train the judge first
<!-- Lines 88-96 -->

*Proposal.* The two trainings do not cost the same:
- the **judge** can be trained on fixed, cached triplets (original, candidate, defect labels): no generator
  call, cheap;
- the **generator** needs generations at every evaluation: expensive.

So: train and calibrate the judge first on labelled triplets; then use the calibrated judge as the loss for
the generator's instructions, checking it against ground truth on a sample.

## Generalization
<!-- Lines 99-104 -->

*Proposal.*
- Split by building or scene, never by photo: photos of one room share walls, light and furniture.
- Regularize: shorter instructions at equal score; no instruction that names a specific building.
- The real held-out set is the final check; a base that gains on synthetic data and loses on real photos is
  not released.
