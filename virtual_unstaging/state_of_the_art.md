# State of the art — virtual unstaging and clutter pairs

What exists for each branch of [architecture.md](architecture.md), [training.md](training.md) and
[clutter_pairs/architecture.md](../clutter_pairs/architecture.md): data, removal methods, edit judges, critic-in-the-loop
editors, prompt optimization; what it changes for the open questions.

> **Status:** a budgeted literature search (23 web searches, 8 primary pages read), then a second pass on existing
> pair benchmarks (8 searches, 10 pages read). Most per-paper facts come from search summaries and are marked
> *inferred*; open the paper before relying on a number.

## Table of Contents

1. [Summary](#summary) _(Lines 38-54)_
1. [Findings by branch](#findings-by-branch) _(Lines 57-57)_
   1. [A. Paired clean/cluttered data](#a-paired-cleancluttered-data) _(Lines 60-68)_
   1. [B. Defurnishing and object removal](#b-defurnishing-and-object-removal) _(Lines 71-75)_
   1. [C. Judging image edits](#c-judging-image-edits) _(Lines 78-83)_
   1. [D. Judge-guided refinement and tool-augmented agents](#d-judge-guided-refinement-and-tool-augmented-agents) _(Lines 86-90)_
   1. [E. Prompt optimization and free-text feedback](#e-prompt-optimization-and-free-text-feedback) _(Lines 93-103)_
1. [Detail](#detail) _(Lines 106-106)_
   1. [0. Method and plan (written before the first search)](#0-method-and-plan-written-before-the-first-search) _(Lines 109-123)_
   1. [1. Branch A. Paired clean/cluttered data](#1-branch-a-paired-cleancluttered-data) _(Lines 126-153)_
      1. [Existing pair benchmarks (second pass)](#existing-pair-benchmarks-second-pass) _(Lines 156-181)_
   1. [2. Branch B. Defurnishing and object removal](#2-branch-b-defurnishing-and-object-removal) _(Lines 184-210)_
   1. [3. Branch C. Judging image edits](#3-branch-c-judging-image-edits) _(Lines 213-235)_
   1. [4. Branch D. Judge-guided iterative refinement](#4-branch-d-judge-guided-iterative-refinement) _(Lines 238-257)_
   1. [5. Branch E. Prompt optimization and free-text feedback](#5-branch-e-prompt-optimization-and-free-text-feedback) _(Lines 260-279)_
   1. [6. Cross-branch implications (kept short)](#6-cross-branch-implications-kept-short) _(Lines 282-286)_
   1. [7. Search log](#7-search-log) _(Lines 289-354)_
   1. [8. Not checked, and why](#8-not-checked-and-why) _(Lines 357-371)_



---

## Summary
<!-- Lines 38-54 -->

The field has the parts but not the assembly. Nothing found does what the design does end to end (indoor removal, steered by a tool-using VLM judge, with prompts trained offline), and no public benchmark measures it. Every branch has usable building blocks:

- **A, paired data:** exact room-scale pairs exist only from 3D sources (Structured3D, ShanghaiTech-Kujiale, 3D-FRONT rendering, HSSD, Infinigen); real before/after pairs exist only at object scale (OBER-Test, Remove360), and ObjectDrop is not confirmed released. No existing benchmark fits the clutter_pairs contract (detail 1, "Existing pair benchmarks"). Generated pairs have a documented trap: editing models perturb pixels outside the edit, so a raw pixel test fails and a VAE-signature shortcut is plausible.
- **B, removal:** indoor defurnishing is a two-paper line (Matterport 2024, 2025) with no released code or data found; general removal has open models (ObjectClear, non-commercial) and benchmarks that confirm "one ground truth per hole" is ill-posed, which supports the structural measure of `training.md`.
- **C, judging:** open edit-reward models exist (EditScore, Apache-2.0 code); but VLMs are measurably bad at spotting small differences between two images, which matches the prototype's missed doors.
- **D, loops:** several 2025-2026 critic-in-the-loop editors with tool calls exist; one (ADE-CoT) answers the search-policy question directly.
- **E, prompt optimization:** GEPA is the strongest text-only method; no multimodal or image-editing-generator result found.
- **Generator licence:** Qwen-Image-Edit-2511 is Apache-2.0 (read on its model card); FLUX.1 Kontext [dev] is non-commercial (read).

> **PIN.**
> - Searches used: 23 of the 25 budgeted (A 7 of 8, B 5 of 5, C 4 of 5, D 4 of 4, E 3 of 3); plus 11 WebFetch calls (8 returned content, 3 returned HTTP 404). Second pass on existing pair benchmarks (A): 8 searches (one extended), 11 WebFetch calls (10 returned content, 1 refused).
> - Branches with no relevant work found: none came back empty; four sub-topics did: a public clutter or room taxonomy (A); an indoor defurnishing benchmark or released defurnishing code and data (B); an editing-specific study of VLM-judge bias and human agreement (C); prompt optimization against a VLM-judge objective for an image-editing generator (E).
> - Licence or release not verified that the design depends on: 3D-FRONT licence (official page unreachable); Structured3D Terms of Use text (linked, not read); Infinigen Indoors-specific licence and furniture-off pair rendering (docs unreachable; only the repository-level BSD-3-Clause was read); HSSD licence; PIPE, PIPE_Masks and paint-by-inpaint model licences; ObjectDrop data release; OmniEraser data and code release; ObjectClear weights release (licence NTU S-Lab 1.0, non-commercial, read); EditScore weights licence (code is Apache-2.0, read); BAGEL and Step1X-Edit licences; ADE-CoT code licence; the 2026 Qwen licence claims (secondary sites only); released code or data for the Matterport defurnishing papers and for the 3D-FRONT pair-rendering paper (arXiv 2512.17955, none linked on its abstract page).

---

## Findings by branch
<!-- Lines 57-57 -->

### A. Paired clean/cluttered data
<!-- Lines 60-68 -->
- Exact pairs come from 3D sources. Structured3D ships empty/simple/full configurations (inferred; 21,835 pairs over 3,500 scenes reported by a third paper) but data is gated by a Terms-of-Use form (grounded). 3D-FRONT has no pairs; render them with the recipe of arXiv 2512.17955 (BlenderProc, remove foreground furniture, same camera), whose data and code are not linked (grounded: absent on abstract page). Informs clutter_pairs open question "Which models and licences for a public dataset" and the simulation route.
- Infinigen is BSD-3-Clause at repository level (grounded); whether Indoors renders the same camera without furniture, and the licence of its assets, are unverified (docs unreachable).
- Real counterfactual pairs: ObjectDrop (~2,500 real before/after samples enough for removal, not for insertion; 350K bootstrapped) (inferred). Release not confirmed.
- "Add clutter" by an editing model has precedent: Paint by Inpaint (PIPE) builds pairs by removing objects first, then reverses them; PIPE data and models are on Hugging Face (inferred; licence unchecked). Informs "inpainting inside a mask vs free editing".
- Pair quality: editing models change pixels outside the edit (FLUX Kontext shown to); a fine-tuned mask estimator cut L1 error from 0.060 to 0.007 against plain pixel differencing (inferred). Informs clutter_pairs open question "pixel tolerance outside the mask": a fixed raw-difference threshold is the wrong test.
- Shortcut risk is real: inpainting detectors lean on global VAE-induced artifacts (INP-X, inferred). Informs the "shortcut cues" risk: give the clean image the same encode-decode round trip as the cluttered one (inferred proposal, untested).
- No public clutter taxonomy or tidiness dataset found; nearest is SpatialLM's 59 furniture categories (inferred).
- No existing benchmark to adopt (second pass): rendered panorama pairs (Structured3D, ShanghaiTech-Kujiale); a gated set of 15,471 empty, furnished, shadowed and staged bedroom images of unknown provenance and licence (ApplyDesign); small real before/after captures at object scale (Remove360, OBER-Test). Real empty rooms at scale: ZInD, academic use only (grounded). Informs clutter_pairs: building is justified; the ApplyDesign set is the one to inspect before designing.

### B. Defurnishing and object removal
<!-- Lines 71-75 -->
- Indoor defurnishing: "An Empty Room is All We Want" (Matterport, CVPRW 2024, Stable Diffusion inpainting on panoramas) and "Defurnishing with X-Ray Vision" (CVPRW 2025, mesh-derived depth/normal edges as ControlNet guide) (inferred). Code and data not found. A CoStar patent covers a diffusion defurnishing method (commercial context only). No 2026 indoor paper and no public indoor benchmark found.
- Removal measurement: PROVE (2026) argues one ground truth per hole is ill-posed and that common metrics disagree with perception; VOR-Bench scores completeness, mask-background consistency, logical plausibility (inferred). This supports the structural, per-defect measure of training.md and maps onto `movable_left`, `drift`, `surface_implausible`.
- Open removal model: ObjectClear (code, training code, OBER dataset public; NTU S-Lab License 1.0, non-commercial) (grounded). Usable as a baseline, not as the default generator.
- Default generator (design open question): Qwen-Image-Edit-2511 is Apache-2.0 (grounded); FLUX.1 Kontext [dev] model is under a non-commercial licence though outputs may be used commercially (grounded). BAGEL and Step1X-Edit unchecked.

### C. Judging image edits
<!-- Lines 78-83 -->
- Open edit judges exist: EditScore reward models 7B-72B (4B/8B Qwen3-VL variants), with EditReward-Bench; code Apache-2.0 (grounded), claims the largest model plus self-ensemble beats GPT-5 on its own benchmark (grounded as a claim); human-agreement numbers not read. Informs "judge model class".
- Standard judging recipe is VIEScore-style: original + instruction + result, scores for semantic consistency and perceptual quality, with GPT-4o/4.1 or Qwen2.5-VL-72B as judges in GEdit-Bench and ImgEdit-Bench (inferred).
- Small local changes are the weak spot: on VDiff-Bench 7-8B open MLLMs reach 8.7-33.3% on low-level changes and often answer "no difference" (inferred, secondary summary). This explains the prototype missing invented doors and argues for giving the judge a difference mask and crops.
- Edit-specific checks to borrow: SpotEdit hallucination split, GIE-Bench masked preservation after alignment (inferred).
- No editing-specific study of judge bias or agreement with human raters found.

### D. Judge-guided refinement and tool-augmented agents
<!-- Lines 86-90 -->
- Critic-in-the-loop editors with tools: IMAGAgent (plan, execute, reflect; retrieval, segmentation, detection tools), LOCI (locator-critic), an LLM-LVLM agent (feedback changes tool parameters), GenArtist (planning tree with self-correction), UniEdit-I (converges in 1-2 iterations on GEdit-Bench) (inferred).
- Search policy (design open question 1): ADE-CoT (CVPR 2026) allocates budget by estimated edit difficulty, prunes early with region-localization and caption checks, and stops depth-first at the first intent-aligned result; >2x faster than best-of-N on Step1X-Edit, BAGEL, FLUX Kontext; code public, licence unchecked (inferred).
- Tool library (open question 6): SAM 3 Agent pairs a VLM with SAM 3 as a tool; DepthLM reports frontier VLMs still weak at 3D from 2D, a reason to call a depth tool (inferred).
- No loop found that feeds the critic a removal mask plus protected fixed elements, and no ablation of which tool helps a judge most.

### E. Prompt optimization and free-text feedback
<!-- Lines 93-103 -->
- GEPA (ICLR 2026) beats MIPROv2 (+14 vs +7 aggregate gain) and GRPO on text tasks with natural-language reflection (inferred). No multimodal or image-editing-generator benchmark of GEPA or MIPRO found.
- Closest multimodal precedents are text-to-image prompt rewriters with a VLM judge (ConceptMix++, TextGrad-style, GPT-4o as judge and rewriter, 5 rounds; self-rewarding LVLM; VisualPrompter) (inferred).
- Judge tuning from reviewer comments (design 2b): practitioner sources describe a label-comments-rewrite loop with 100-200 gold labels and corrected cases as few-shot (vendor documentation, unverified). One 2026 paper finds strict judge feedback causes judge-specific overfitting (inferred). Informs "how big the calibration sample must be".

> **PIN.**
> - Searches used: 23 of the 25 budgeted (A 7 of 8, B 5 of 5, C 4 of 5, D 4 of 4, E 3 of 3); plus 11 WebFetch calls (8 returned content, 3 returned HTTP 404). Second pass on existing pair benchmarks (A): 8 searches (one extended), 11 WebFetch calls (10 returned content, 1 refused).
> - Branches with no relevant work found: none came back empty; four sub-topics did: a public clutter or room taxonomy (A); an indoor defurnishing benchmark or released defurnishing code and data (B); an editing-specific study of VLM-judge bias and human agreement (C); prompt optimization against a VLM-judge objective for an image-editing generator (E).
> - Licence or release not verified that the design depends on: 3D-FRONT licence (official page unreachable); Structured3D Terms of Use text (linked, not read); Infinigen Indoors-specific licence and furniture-off pair rendering (docs unreachable; only the repository-level BSD-3-Clause was read); HSSD licence; PIPE, PIPE_Masks and paint-by-inpaint model licences; ObjectDrop data release; OmniEraser data and code release; ObjectClear weights release (licence NTU S-Lab 1.0, non-commercial, read); EditScore weights licence (code is Apache-2.0, read); BAGEL and Step1X-Edit licences; ADE-CoT code licence; the 2026 Qwen licence claims (secondary sites only); released code or data for the Matterport defurnishing papers and for the 3D-FRONT pair-rendering paper (arXiv 2512.17955, none linked on its abstract page).

---

## Detail
<!-- Lines 106-106 -->

### 0. Method and plan (written before the first search)
<!-- Lines 109-123 -->

Strategy: one query per branch first, then fill named gaps; prefer a survey or benchmark over single papers; stop a branch when results repeat. Fetch only where a design decision hinges on a licence or a release.

Taxonomy of the field per branch, known works going in, and the question each search had to answer:

| Branch | Taxonomy | Known going in (not re-searched) | Questions the searches had to answer |
|---|---|---|---|
| A | (1) real counterfactual pairs; (2) 3D renders with furnished/empty configurations; (3) procedural interiors; (4) insertion / add-clutter generation; (5) room and clutter ontologies; (6) pair quality checks; (7) shortcut cues | Infinigen Indoors, Structured3D, 3D-FRONT pairs, Matterport defurnishing (design doc "Prior work"); ObjectDrop, InstructPix2Pix, MagicBrush, ProcTHOR, HSSD, Hypersim (memory) | Which render sources give pairs cheaply, and under what terms? Is any real counterfactual set released? Which models add objects and what do they break? Is a pixel test enough? Does a clutter taxonomy exist? Are shortcut cues documented? |
| B | (1) indoor defurnishing; (2) general object/effect removal; (3) removal benchmarks and metrics; (4) generator models and licences; (5) commercial context | Matterport pair (design doc); LaMa, SD inpainting, RORD (memory) | What happened after 2025 in defurnishing? Which metrics fit "structurally right, not pixel-equal"? Which generator has an open-source-compatible licence? |
| C | (1) edit-evaluation benchmarks; (2) VLM-as-judge recipes; (3) learned edit reward models; (4) hallucination and over-editing detection; (5) VLM weaknesses on image pairs; (6) human agreement | VIEScore, GEdit-Bench, ImgEdit, MLLM-as-a-Judge (memory) | Is there an open judge and what is its measured quality? Why does a VLM miss a small invented object? Is judge bias for edits measured? |
| D | (1) generator-critic loops; (2) tool-augmented VLM agents; (3) budget and stopping policy | GenArtist, ViperGPT, Visual Sketchpad (memory) | Which 2025-2026 loops exist? Which stopping/budget policy is published? Which tools were used and with what effect? |
| E | (1) text optimizers (textual gradient, evolution, Bayesian); (2) multimodal variants; (3) learning from free-text feedback; (4) judge calibration | TextGrad, GEPA, OPRO, MIPROv2 (named in training.md) | Any multimodal evidence? How much human feedback is needed? Does feedback style matter? |

Certainty note: the plan was written in the working notes before searching and is reproduced here.

### 1. Branch A. Paired clean/cluttered data
<!-- Lines 126-153 -->

| Work | Year | What it does | Relevance to our design | Availability and licence | Certainty |
|---|---|---|---|---|---|
| Structured3D, https://github.com/bertjiazheng/Structured3D (paper https://arxiv.org/abs/1908.00222) | 2019 | Rendered rooms under different lighting and furniture configurations; a third paper (https://arxiv.org/pdf/2307.09621) reports 21,835 unfurnished/furnished 360-degree pairs over 3,500 scenes; another (https://arxiv.org/pdf/2506.17707) says full, partial, empty versions | Exact pairs by construction; panoramas, depth and normals included; cropping perspective views from panoramas needed | Data: Structured3D Terms of Use, request via agreement form, not an open download. Code: MIT. Terms text not read | licence/access grounded; counts and configurations inferred |
| 3D-FRONT, https://openaccess.thecvf.com/content/ICCV2021/html/Fu_3D-FRONT_3D_Furnished_Rooms_With_layOuts_and_semaNTics_ICCV_2021_paper.html | 2021 | 18,968 furnished rooms in 6,813 houses; ships with a renderer; no paired images | Source for the simulation route; render same camera with and without furniture | Licence not verified (official page returned 404 from the URL tried) | inferred; licence open |
| Modular single-view 3D reconstruction, https://arxiv.org/abs/2512.17955 | 2025 | Pair recipe: BlenderProc render, remove visible foreground furniture, re-render with same camera; camera height 1.4-1.9 m, at least 3 m from any instance; 17,315 pairs at 1024 x 1024, instance maps as masks (second-pass search summary) | Ready-made recipe for the 3D-FRONT pairs | No data or code link on the abstract page | recipe inferred (snippet); non-release grounded |
| HSSD-200, https://arxiv.org/abs/2306.11290 | 2023/2024 | 211 houses, 18,656 objects, 466 categories; scenes are compositional so objects can be removed or added | Render-with-and-without source with semantic labels per object (which solves "movable vs fixed") | Licence not checked | inferred; licence open |
| Infinigen Indoors, https://github.com/princeton-vl/infinigen (paper https://arxiv.org/abs/2406.11824) | 2024 | Procedural indoor generator | Simulation route, proposed in design | Repository: BSD-3-Clause; some procedural code CC-0. Not read: Indoors asset terms; furniture-off pair rendering (docs URLs 404); pre-generated data "stay tuned" | repo licence grounded; rest open |
| ProcTHOR, ReplicaCAD, Hypersim | 2021-2022 | Procedural houses (ProcTHOR); arranged apartment scenes (ReplicaCAD); rendered indoor scenes (Hypersim) | Alternative 3D sources | not checked | inferred from memory; no URL verified, do not publish without checking |
| ObjectDrop, https://arxiv.org/abs/2403.18818 | 2024 | Real counterfactual capture: scene photographed before and after removing one object; about 2,500 samples enough for removal but not insertion; 350K insertion set bootstrapped from 700K images with removal | Only real counterfactual precedent; shows how small the real set can be for removal, and that bootstrapping with a removal model works | Data release not confirmed | inferred; release open |
| Paint by Inpaint (PIPE), https://arxiv.org/abs/2404.18212 | 2025 (CVPR) | Builds "add object" pairs by removing objects first, then swaps the direction; VLM describes the object, LLM writes instructions; targets from COCO and OpenImages | The "add clutter" step done through removal-first pair construction; precedent for model 2 | PIPE, PIPE_Masks and models on Hugging Face (https://huggingface.co/datasets/paint-by-inpaint/PIPE_Masks); licence not checked | inferred; licence open |
| Overpainting, https://arxiv.org/abs/2609.10811 | 2026 | Notes FLUX.1 Kontext makes small unintended changes outside the edit; fine-tuned mask estimator L1 0.007 vs 0.060 for thresholded pixel difference | Pixel test between clean and cluttered image must model this noise | not checked | inferred |
| FineEdit, https://arxiv.org/abs/2604.10954; GIE-Bench, https://arxiv.org/abs/2505.11493 | 2025-2026 | Filter pairs by overlap between change mask and detector box; align images before masked preservation metrics, review masks manually | Concrete pair-filter and metric recipes | not checked | inferred |
| INP-X, https://arxiv.org/abs/2602.00192; DiffusionPrint, https://arxiv.org/abs/2604.12443 | 2026 | Inpainting detectors rely on global spectral shifts from the VAE round trip (accuracy 91% to 55% when inpainted content is swapped); fingerprints of inpainting model localize edits | Documents the shortcut risk for generated pairs | not checked | inferred |
| SpatialLM, https://arxiv.org/abs/2506.07491 | 2025 | Structured indoor modelling with 59 object categories grouped by function | Nearest public category list; no clutter or movable/fixed attribute | not checked | inferred |

Gaps found:
- No public clutter or tidiness taxonomy; no dataset labelling movable vs fixed except per-object 3D sources (HSSD, 3D-FRONT categories). The clutter taxonomy and room ontology must be built here.
- No confirmed released real counterfactual set.
- No study I found measuring whether a decluttering model learns inpainting traces from synthetic pairs; INP-X is in the forensic setting.
- 7 of 8 searches used; the 8th held back because the last A results repeated known works.

Implications for the design (clutter_pairs):
- **Pixel tolerance outside the mask** (open question): a global threshold on raw differences is unsafe because editing models alter the whole image slightly. Evidence supports a learned or calibrated mask estimate, or alignment first, then masked metrics (inferred; to be measured on our own model 2).
- **Inpainting inside a mask vs free editing** (open question): inpainting passes the whole image through a VAE round trip too, so both choices leave a global signature; the sure fix is symmetric: run the clean image through the same round trip (null edit) before pairing (inferred proposal, untested). This is also the check for the shortcut-cue risk: train a detector to tell clean from cluttered image from non-mask pixels; chance level is the pass mark.
- **Simulation route**: Structured3D (gated, Terms), 3D-FRONT (licence open), HSSD (licence open), Infinigen (BSD for code). Licences of the data decide whether a public benchmark can ship renders or only a recipe; unresolved for all three.
- **Taxonomy granularity** (open question): no external source tells how many values per axis; HSSD's 466 categories and SpatialLM's 59 bracket the range.

#### Existing pair benchmarks (second pass)
<!-- Lines 156-181 -->

Question: does a benchmark of clean/cluttered pairs of the same view already exist, so that clutter_pairs could adopt or extend it? 8 searches (one extended, for 2026 work), 11 fetches.

| Work | What it holds | Fit to the clutter_pairs contract | Access and licence | Certainty |
|---|---|---|---|---|
| ApplyDesign "Autodesign" bedroom-dataset, https://huggingface.co/datasets/ApplyDesign/bedroom-dataset | 15,471 examples, each `empty_image`, `furniture_image`, `shadow_image`, `staged_image` and a caption; 210 Arrow shards, 117 GB | Closest in structure: the chain empty, furnished, shadowed, staged is the generation route's pipeline; bedrooms only, by its name; real or generated not stated | Gated (manual approval); no licence field; no provenance on the card; 7 downloads | grounded (card, Hub API); provenance open |
| ShanghaiTech-Kujiale Indoor 360°, https://svip-lab.github.io/dataset/indoor_360.html | 1,775 rooms, 3,550 rendered panoramas, each room with and without furniture; depth and layout | Exact pairs if the two share the camera (not stated); panoramas, perspective crops needed; furniture, not small clutter | Dropbox download; no licence or terms on the page | grounded (page); same viewpoint open |
| Remove360, https://arxiv.org/abs/2508.11431; data https://huggingface.co/datasets/simkoc/Remove360 | 11 real scenes (6 indoor, 5 outdoor), 4K video, 150 to 300 views before and about as many after removal; one, two or several objects, from a backpack to a sofa | Real, but before and after views are not stated to share poses: a novel-view benchmark, not pixel pairs | MIT on the Hugging Face card; not gated | grounded (paper HTML, Hub API) |
| Something's Missing Here, https://huggingface.co/datasets/Shay85Gil/somethings_missing_here | 559 pairs (with the object, after its removal), part aligned from Remove360 by SIFT and homography, part handheld re-shots | Real and partly aligned, but one missing object per pair; built to detect what is missing | CC-BY-NC-4.0 | grounded (card) |
| OBER (ObjectClear), https://arxiv.org/abs/2505.22636 | 2,715 camera-captured and 10,000 simulated training pairs with object and effect masks; OBER-Test 163 pairs with ground truth, OBER-Wild 302 without | Real pairs at object scale (an object with its shadow and reflection), not rooms | Gated, non-commercial (branch B) | inferred (search summary) |
| ZInD, https://github.com/zillow/zind | 67,448 panoramas of 1,575 real unfurnished homes, with layouts, doors and windows | Real clean images at scale for the "real empty photos" proposal; no cluttered side | ZInD Terms of Use: "academic use only", "not licensed for commercial purposes"; manual approval up to two weeks; about 40 GB; code Apache-2.0 | grounded (repository page) |
| Clutter Detection and Removal in 3D Scenes with View-Consistent Inpainting (Wei, Funkhouser, Rusinkiewicz, ICCV 2023), https://arxiv.org/abs/2304.03763 | Segments clutter on ScanNet and Matterport and removes it in 3D; evaluation moves clutter objects onto free regions so the original room is the ground truth | Nearest published definition of clutter; feeds the clutter taxonomy | No code or data link on the abstract page; category list not read | grounded (abstract); method detail inferred |
| Diminished-reality captures: Mori et al. 2016 (robot arm, sequences with and without objects), https://www.rm2c.ise.ritsumei.ac.jp/papers/2016/MTA_mori.pdf; Emptying, Refurnishing, and Relighting Indoor Spaces (SIGGRAPH Asia 2016), https://grail.cs.washington.edu/projects/emptying | Small real setups with ground truth | Precedent only | not checked | inferred |
| MRoom-30k (UML-CoT), https://arxiv.org/abs/2509.22628 | "a new benchmark of cluttered room-cleaning scenarios" | Messy-room images for the taxonomy's density axis, if released | Size, provenance and release not on the abstract page | open |
| Room Envelopes, https://arxiv.org/abs/2511.03970 | Synthetic RGB images, each with a visible-surface pointmap and a layout pointmap with fittings and fixtures removed | Geometry of the empty room, not its image | No dataset link on the abstract page | grounded (abstract) |
| An ICLR 2026 paper on learning an image editing model, https://proceedings.iclr.cc/paper_files/paper/2026/file/b4995cbd0b7f6a1a366ee65f9c4b02ac-Paper-Conference.pdf | Argues that synthetic training pairs made by pretrained editors propagate and magnify the editors' artifacts | Supports the shortcut-cue and same-family risks | not read | inferred (search summary) |

Gap: no benchmark of photographic, same-view clean/cluttered pairs across room types under open terms. The one with the right structure (ApplyDesign) has unknown provenance and terms.

Implications for clutter_pairs:
- Building is justified: nothing to adopt as is (8 searches, not exhaustive).
- Inspect the ApplyDesign set before designing: if generated, it is a direct precedent for the pipeline and a test of the quality checks; if real, a validation set. Access needs a request from an account.
- A real check set for the domain-gap risk exists only at object scale: Remove360 (MIT), its aligned derivative (non-commercial), OBER-Test (non-commercial).
- Real clean images at scale: ZInD, academic use only; a public dataset cannot ship them, a recipe can point to them.
- Exact rendered pairs to calibrate the pixel test: Structured3D, ShanghaiTech-Kujiale (terms unresolved for both).

### 2. Branch B. Defurnishing and object removal
<!-- Lines 184-210 -->

| Work | Year | What it does | Relevance to our design | Availability and licence | Certainty |
|---|---|---|---|---|---|
| An Empty Room is All We Want, https://arxiv.org/abs/2405.03682 | 2024 (CVPRW) | Matterport; Stable Diffusion inpainting on indoor panoramas with added context and fine-tuning, better blending; no room-layout estimation | The only indoor defurnishing prior | no code or dataset found; project page listed on arXiv | inferred |
| Defurnishing with X-Ray Vision, https://arxiv.org/abs/2506.05338 | 2025 (CVPRW) | Furniture removed from the mesh, planes extended, depth/normal edges guide ControlNet inpainting of panoramas, which texture the mesh | Supports the idea of geometry as a visual guide (our judge tool library: depth/normals as condition) | no code or dataset found | inferred |
| CoStar patent US 12,475,666 B2, https://patentsgazette.uspto.gov/week46/OG/html/1540-3/US12475666-20251118.html | 2025 | Latent diffusion defurnishing and furnishing, trained on unfurnished spaces then fine-tuned with artifacts | Commercial context; possible freedom-to-operate question for a public tool | patent | inferred (snippet) |
| ObjectClear, https://arxiv.org/abs/2505.22636 (repo https://github.com/zjx0101/ObjectClear) | 2025 | Object-effect attention separates foreground removal from background reconstruction; evaluated with PSNR, PSNR-BG, LPIPS, CLIP, ReMOVE on RORD-Val, OBER-Test, OBER-Wild | Strong open baseline for removal; ReMOVE as reference-free metric | Code, inference and training code public; OBER dataset gated; NTU S-Lab License 1.0, non-commercial only. Weights release not stated on page | grounded (repo page) |
| OmniEraser, https://arxiv.org/abs/2501.07397 | 2025 | Removes objects and shadows/reflections; Video4Removal, over 100K video-frame pairs; built on FLUX.1-dev | Source of pair-construction ideas (video frames as counterfactuals) | abstract says datasets, models, code "will be published"; release not confirmed; FLUX.1-dev base implies a non-commercial model licence | inferred |
| PROVE, https://arxiv.org/abs/2605.14534 | 2026 | Benchmark argues removal is ill-posed (several valid fills) and that standard metrics contradict perception | Supports training.md: no pixel-equality goal | not checked | inferred |
| VOR-Bench, https://arxiv.org/abs/2609.16878 | 2026 | Video removal; 1-5 scores for removal completeness, mask-background consistency, logical plausibility | Three criteria align with `movable_left`, `drift`, `surface_implausible` | not checked | inferred |
| Class-wise object-removal evaluation, https://arxiv.org/abs/2404.11104 | 2024 | CARLA vehicle/no-vehicle pairs as ground truth; FID*, U-IDS*; over 9K images needed for reliable assessment | Shows a simulated-pairs benchmark is feasible, and that distribution metrics are sample-hungry | not checked | inferred |
| ReMOVE (reference-free erasure metric; summary https://www.themoonlight.io/review/remove-a-reference-free-metric-for-object-erasure) | 2024 | Tracks LPIPS on real data and separates removal from unintended replacement better than CLIPScore | Candidate generator-side measure that needs no ground truth | not checked; primary page not opened | inferred (third-party summary) |
| Qwen-Image-Edit-2511, https://huggingface.co/Qwen/Qwen-Image-Edit-2511 | 2025 | Open image-editing model | Candidate default generator | Apache-2.0 (card: "Qwen-Image is licensed under Apache 2.0"); no commercial restriction mentioned | grounded |
| FLUX.1 Kontext [dev], https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev | 2025 | Open-weight image-editing model | Candidate generator, widely benchmarked | FLUX.1 [dev] Non-Commercial License; card says outputs may be used for personal, scientific and commercial purposes; training other models not addressed | grounded |
| Step1X-Edit, https://arxiv.org/abs/2504.17761; BAGEL | 2025 | Open editing models; GEdit-Bench introduced with Step1X-Edit | Candidate generators | licences not checked (memory says Apache-2.0, unverified) | inferred; licence open |
| Licence matrix blog, https://invideo.io/blog/open-source-image-models-licenses/ | 2026 | Secondary claims: Qwen-Image line through Dec 2025 Apache-2.0; 2026 Qwen generation API-only; Qwen-Image 2.1 research-only; FLUX 2 klein-4B Apache | Warns that newer Qwen releases may not stay permissive | commercial site, conflicts with other sources | inferred, low confidence |

Gaps found:
- No 2026 indoor defurnishing paper, no public defurnishing benchmark, no released defurnishing code or data. Real-estate products exist (commercial context only; no product page was searched, to save budget).
- Removal benchmarks are general or video; none targets "empty building, fixed elements kept".

Implications:
- **Default generator with an open-source-compatible licence** (open question): among models whose licence I read, Qwen-Image-Edit-2511 (Apache-2.0) fits; FLUX.1 Kontext [dev] weights are non-commercial, which is usable for research and for outputs but not for a tool that ships or redistributes the model; ObjectClear is non-commercial. BAGEL and Step1X-Edit unresolved.
- **Performance measure** (training.md): PROVE and the CARLA study support a structural, per-defect measure plus a reference-free score (ReMOVE) as a cross-check; FID-style measures need thousands of images.
- **Judge tool library**: X-Ray's use of depth/normals as a guide is the published precedent for the "guide" use of the depth tool.
- Defurnishing work is panorama and mesh based (Matterport has the mesh); perspective photos without a mesh, as in our case, are not covered by published work (inferred).

### 3. Branch C. Judging image edits
<!-- Lines 213-235 -->

| Work | Year | What it does | Relevance to our design | Availability and licence | Certainty |
|---|---|---|---|---|---|
| EditScore and EditReward-Bench, https://arxiv.org/abs/2509.23909 (repo https://github.com/VectorSpaceLab/EditScore) | 2025 | Reward models 7B-72B (and Qwen3-VL 4B/8B) for instruction editing; claims largest model with self-ensemble beats GPT-5 on its benchmark; claims even large open VLMs give no useful RL signal | Candidate open judge, cheaper than a frontier API; its benchmark is a template for our judge benchmark | Repo code Apache-2.0; weights licence not stated on the page; dataset card says apache-2.0 (search snippet) | grounded for repo/abstract; agreement numbers not read |
| Instruction-based image editing survey, https://arxiv.org/abs/2607.25642 | 2026 | Survey of data, models, evaluation; describes VIEScore (perceptual quality and semantic consistency, MLLM given original, instruction, result), ImgEdit-Bench (GPT-4o rubric 1-5), GEdit-Bench (606 real-world cases, 11 categories, Qwen2.5-VL-72B or GPT-4.1 judge) | Map of standard judging recipes and their judge models | not checked | inferred (snippet) |
| SpotEdit, https://arxiv.org/abs/2508.18159 | 2025 | Visually guided editing benchmark with a hallucination split (target absent: output should equal input); InternVL3-8B as binary checker; GPT-4o adds unintended edits | Hallucination as a first-class test | not checked | inferred |
| GIE-Bench, https://arxiv.org/abs/2505.11493 | 2025 | Grounded evaluation: align images, masked preservation metrics, reviewed masks | Preservation outside the region, the `drift` defect | not checked | inferred |
| BEAF, https://arxiv.org/abs/2407.13442 | 2024 | Edits images to remove objects, checks whether VLM answers change | Method analogy for testing a judge with known edits (our injected-defect idea) | not checked | inferred |
| VDiff-Bench, https://huggingface.co/papers/2609.06245 | 2026 | 1,756 multiple-choice questions on image pairs, 10 change categories; 7-8B open MLLMs score 52.5-70.6% on semantic changes, 8.7-33.3% on low-level changes, often saying "no difference" | Quantifies why a VLM judge misses subtle changes between original and candidate | not checked | inferred (HF listing and third-party summary) |
| Eyes Wide Shut (MMVP), https://cvpr.thecvf.com/virtual/2024/poster/30013 | 2024 | Visual pattern failures of multimodal LLMs, CLIP-blind pairs | Supports using non-VLM tools for perception | not checked | inferred |
| DepthLM, https://alphaxiv.org/abs/2509.25413 | 2025 | Reports frontier VLMs still weak at depth/3D from 2D | Reason for the depth tool | not checked | inferred |
| Judge prompt study (legal QA), https://arxiv.org/abs/2604.20726 | 2026 | Lenient judge feedback gives higher, more consistent optimization gains than strict feedback; strict judges overfit | Applies to judge-trained prompts (see E) | not checked | inferred; outside images |

Gaps found:
- No study found on VLM-judge bias or agreement with human raters specific to image editing (position, self-preference, over-editing). Agreement numbers for EditScore or VIEScore were not read.
- No judge benchmark for "invented content behind removed objects"; closest are SpotEdit (absent target) and GIE-Bench (preservation).
- 4 of 5 searches used; the last would have repeated agreement-study queries.

Implications:
- **Judge model class** (open question): an open judge exists (EditScore, 4B-72B) and the benchmark gives a template; whether it handles removal, not instruction following in general, is untested. Cost per image stays open.
- **Missed invented doors in the prototype**: VDiff-Bench-type evidence says whole-frame comparison by a mid-size VLM will miss local changes. Give the judge the removal mask, a difference map from the tool library and crops of the masked region (inferred; the design already points this way; testable on injected defects).
- **Hallucination detection**: SpotEdit's "target absent, output must equal input" is a ready test for the "views with nothing to remove" case of stage 0.

### 4. Branch D. Judge-guided iterative refinement
<!-- Lines 238-257 -->

| Work | Year | What it does | Relevance to our design | Availability and licence | Certainty |
|---|---|---|---|---|---|
| IMAGAgent, https://arxiv.org/abs/2603.29602 | 2026 | Multi-turn plan, execute, reflect; tool chain with retrieval, segmentation, detection, editing; central LLM merges VLM critiques | Closest to loop 1 with a tool library | not checked | inferred |
| LOCI, https://arxiv.org/abs/2608.30959 | 2026 | Locator plus critic checking generated crops, targeted feedback, refinement loop | Detection/verification split | not checked | inferred |
| LLM-LVLM iterative editing agent, https://arxiv.org/abs/2508.17435 | 2025 | LVLM scores compliance after each edit; below threshold, feedback to a planner that changes tool parameters, switches tool, or reorders sub-tasks | Matches "adjust the three inputs" | not checked | inferred |
| UniEdit-I, https://arxiv.org/abs/2508.03142 | 2025 (CVPR 2026) | Training-free understand-edit-verify loop inside a unified VLM; converges in 1-2 iterations on GEdit-Bench | Suggests iteration budgets of 1-3 are the norm | not checked | inferred |
| GenArtist, https://arxiv.org/abs/2407.05600 | 2024 (NeurIPS) | Multimodal LLM agent with planning tree, tool library, self-correction | Reference design for tool selection by an LLM | not checked | inferred; tool list not confirmed |
| ADE-CoT, https://arxiv.org/abs/2603.00141 (CVPR 2026) | 2026 | Search over noise seeds (prompt rewriting optional), not over instructions. (1) Budget per edit from the score of one first sample: N_a = N_min + ceil((N − N_min)(1 − S/S_max)^γ), γ = 0.15. (2) Early pruning on one-step previews of half-denoised latents (flow matching), scored by a general MLLM score plus an edited-region score (share of pixel change inside a Grounded-SAM2 mask of the expected region) and a CLIP score against an MLLM-written target caption; DINOv2 near-duplicates dropped. (3) Depth-first generation in early-score order, stop after 4 intent-aligned results, judged by 5 instance-specific yes/no questions written by the MLLM. More than 2× fewer denoising steps than best-of-N at comparable quality; misjudged pruning 235 → 86. Verifiers: Qwen-VL-MAX, Qwen2.5-VL-72B, Qwen3-VL-32B. Limits stated: MLLM cost, hallucinated verification | Ruled out as the loop-1 engine by the owner: it explores only the random seed, not the dimensions of the problem. Reusable on the judge side: its region score is our drift check, its instance-specific questions fit invented doors | no code link in the paper text | grounded (paper read in full) |
| Guideline-consistent segmentation, https://arxiv.org/abs/2509.04687 | 2025 | Worker-supervisor critique loop with a lightweight RL stop policy | Learned stopping rule | not checked | inferred |
| SAM 3 Agent (SAM 3 released 2025-11-19), https://www.latent.space/p/sam-3-the-eyes-for-ai-nikhila-and | 2025 | SAM 3 as a tool for multimodal LLMs | Candidate segmentation tool with concept prompts | not checked | inferred (interview page) |

Gaps found:
- No loop found where the critic knows the removed region and the protected fixed elements (our judge inputs); no published ablation of which tool (segmentation, detection, depth) helps a judge most; no loop with a recipe knowledge base across images.
- 4 of 4 searches used; the last two returned mostly known loops.

Implications:
- **Search policy of loop 1** (open question): published loops converge in about 1-2 iterations (UniEdit-I, a claim on a different benchmark); ADE-CoT's recipe (difficulty-based budget, cheap early pruning, stop at first accepted) fits the "best attempt kept, stop on no progress" design. Whether it transfers to removal is untested.
- **Tool library** (open question): tools as locators and measurers, VLM as decider, agrees with IMAGAgent and GenArtist; DepthLM-type results argue for keeping depth as an external tool. How the judge chooses a tool and what each call costs is not answered by the literature found.

### 5. Branch E. Prompt optimization and free-text feedback
<!-- Lines 260-279 -->

| Work | Year | What it does | Relevance to our design | Availability and licence | Certainty |
|---|---|---|---|---|---|
| GEPA, https://arxiv.org/abs/2507.19457 | 2025 (ICLR 2026) | Reflective prompt evolution from trajectories and natural-language feedback; beats GRPO by about 6% on average (v2, six tasks; v1 said 10% on four) and MIPROv2 (+14 vs +7 aggregate); text tasks (HotpotQA, IFBench, PUPA, HoVer) | Already named in training.md; this adds that all published tasks are text | not checked | inferred; version disagreement noted |
| TextGrad (https://arxiv.org/abs/2406.07496), OPRO (https://arxiv.org/abs/2309.03409), DSPy MIPROv2 (https://dspy.ai) | 2023-2024 | Named in training.md | not re-searched | not checked | as in training.md |
| ConceptMix++, https://arxiv.org/abs/2507.03275 | 2025 | TextGrad-style: GPT-4o as VLM judge and prompt rewriter from iteration history, fixed 5 iterations, text-to-image | Multimodal precedent for judge-driven rewriting | not checked | inferred |
| Self-rewarding LVLM prompt optimization, https://arxiv.org/abs/2505.16763 | 2025 (ACL Findings) | One LVLM rewrites prompts and scores them, with RL | Precedent; trains weights, not prompts | not checked | inferred |
| VisualPrompter, https://arxiv.org/abs/2506.23138 | 2026 (ICLR) | Training-free prompt optimization with visual feedback and self-reflection | Precedent | not checked | inferred |
| Judge prompt optimization from reviewer comments: Evidently, https://www.evidentlyai.com/blog/llm-judge-prompt-optimization; Potato, https://potatoannotator.readthedocs.io/en/latest/agent-evaluation/judge_alignment/ | 2025-2026 | Labels plus comments rewrite the judge prompt; score by agreement with human labels; Potato suggests 100-200 gold labels and uses human-corrected cases as few-shot; Evidently example 64% to 96% | Practice for 2b | vendor documentation, self-reported | inferred, low confidence |
| Legal QA with ProTeGi, https://arxiv.org/abs/2604.20726 | 2026 | Lenient judge feedback better than strict; strict feedback overfits judge | Caution for 2a/2b: critique style shapes what is learned | not checked | inferred |

Gaps found:
- No multimodal or image-generation benchmark of GEPA or MIPRO. No evidence on optimizing a generator's instructions against a noisy VLM-judge objective with stochastic outputs. training.md already says none was evaluated; this search confirms it.
- 3 of 3 searches used.

Implications:
- **Calibration sample size** (open question 2b): practitioner guidance of 100-200 labelled cases is the only figure found; weak evidence, to be measured on our own judge using bootstrap over the calibration set.
- **2a trigger and acceptance rule**: nothing published fixes a pilot size; GEPA's minibatch reflection plus Pareto selection is the closest, and its text-task gains do not guarantee transfer.
- **Reviewer comment style**: the legal-QA result suggests tracking whether strict reviewer comments over-narrow the judge, and measuring on held-out buildings.

### 6. Cross-branch implications (kept short)
<!-- Lines 282-286 -->

- Generator licence: Qwen-Image-Edit-2511 (Apache-2.0, read) is the only candidate verified as compatible; the others are unverified or non-commercial.
- The same VLM weakness (small differences) appears in C and in the prototype, and tools (D) are the published remedy.
- Pair construction by removal-first (PIPE) and counterfactual capture (ObjectDrop) are mirror images of our two projects: it suggests that a good removal model can seed the clutter project's insertion data, but also that circularity (same-family bias) needs the different-family rule already in the risks.

### 7. Search log
<!-- Lines 289-354 -->

Format: number, branch, query (short), purpose, yield. All searches in "standard" mode except 31 ("extended").

| # | Branch | Query (short) | Purpose | Yield |
|---|---|---|---|---|
| 1 | A | paired furnished/empty room images dataset 3D-FRONT Structured3D defurnishing | Find paired-data sources, verify the design's prior work | Structured3D pair counts (21,835 / 3,500 scenes); 3D-FRONT recipe from 2512.17955; no licence info |
| 2 | B | object removal benchmark survey 2025 hallucination indoor metrics | One benchmark or survey for removal | PROVE, VOR-Bench, ReMOVE, CARLA-based evaluation; nothing indoor-specific |
| 3 | C | image editing evaluation benchmark VLM judge human agreement reward model open weights | One benchmark or leaderboard for edit judging | EditScore, EditReward-Bench |
| 4 | D | VLM critic feedback loop iterative image editing tool-augmented agent | Find loops and tool agents | IMAGAgent, LOCI, LLM-LVLM agent, UniEdit-I, guideline segmentation |
| 5 | E | prompt optimization multimodal pipeline GEPA TextGrad VLM feedback | Multimodal precedents | ConceptMix++, self-rewarding LVLM, VisualPrompter; no multimodal GEPA |
| 6 | A | ObjectDrop counterfactual real photos; Paint by Inpaint PIPE | Real counterfactual datasets and insertion | ObjectDrop details; PIPE not covered (re-queried in 8) |
| 7 | B | defurnishing virtual unstaging 2025 2026 | Post-2024 indoor work, code/data | Only the 2024 paper and a CoStar patent; no 2026 work |
| 8 | C | image editing hallucination unintended changes over-editing judge bias | Hallucination detection and judge reliability | SpotEdit, BEAF; no bias study |
| 9 | E | prompt optimization from human free-text feedback, judge calibration | Learning from comments | Evidently, Potato, legal-QA ProTeGi paper |
| 10 | A | Paint by Inpaint PIPE dataset | Verify the PIPE release | PIPE, PIPE_Masks and models on Hugging Face |
| 11 | B | open-source editing models licence comparison | Generator licence candidates | Secondary matrix; Qwen Apache-2.0 claims; Flux/BAGEL/Step1X unverified (then fetched) |
| 12 | C | survey of editing evaluation benchmarks GEdit-Bench ImgEdit VIEScore | One survey | 2026 survey; VIEScore, GEdit-Bench, ImgEdit descriptions |
| 13 | D | GenArtist multimodal LLM agent tool library self-correction | Reference tool-agent | GenArtist (tool list not confirmed) |
| 14 | A | synthetic indoor scenes same camera with and without objects (ProcTHOR, HSSD, ReplicaCAD) | Procedural interiors with removable objects | HSSD-200; ProcTHOR mentioned; ReplicaCAD absent |
| 15 | A | synthetic paired editing data quality filtering, shortcut, traces | Pair quality checks | Overpainting, FineEdit, GIE-Bench; no shortcut study |
| 16 | B | Defurnishing with X-Ray | Verify the 2025 paper and release | Confirmed method; no code or data link |
| 17 | B | object removal diffusion 2025 open-source ObjectClear OmniEraser | Open removal models and datasets | ObjectClear, OmniEraser |
| 18 | C | MLLM fails to detect differences between two images | Why the judge misses changes | VDiff-Bench, MMVP |
| 19 | D | tool-augmented VLM agent SAM 3 depth verify generated images | Tool-use evidence | SAM 3 Agent, DepthLM; nothing on verifying generated images with RL |
| 20 | E | compound AI joint prompt optimization GEPA MIPRO multimodal | Multimodal GEPA evidence | GEPA numbers; no vision results |
| 21 | A | indoor clutter taxonomy dataset tidy vs cluttered movable fixed | Taxonomy resource | None; SpatialLM categories only |
| 22 | D | test-time scaling image editing verifier best-of-N budget | Search policy and stopping | ADE-CoT |
| 23 | A | inpainting forgery localization detectors shortcut traces | Shortcut-cue risk | INP-X, DiffusionPrint |
| 24 | A | furnished and empty room image pairs, same viewpoint, benchmark 2025 2026 | Existing pair benchmark (second pass) | 2512.17955 pair count; Structured3D; FurniScene and RoomEditor++ (no empty/furnished pairs) |
| 25 | A | virtual staging dataset, empty and furnished paired images | Staging pairs | ZInD as empty source; commercial tools only |
| 26 | A | real object removal dataset before/after, RORD, Remove360, OBER | Real counterfactual benchmarks | Remove360, OBER; Counterfactual and Video4Removal not public |
| 27 | A | diminished reality indoor furniture removal dataset | Diminished-reality ground truth | Kulshreshtha 2022, Pintore 2022, Mori 2016, Zhang 2016 |
| 28 | A | Zillow Indoor Dataset unfurnished homes licence | Real empty rooms | ZInD; licence conflict, resolved by fetch |
| 29 | A | Hugging Face empty and furnished room pairs, virtual staging | Community datasets | ApplyDesign bedroom-dataset |
| 30 | A | multi-object removal benchmark, cluttered scene, declutter | Multi-object ground truth | Wei 2023, Seeing Through Clutter, ICOREval (110 single-object), PROVE-H, OCID |
| 31 | A | synthetic paired empty/cluttered by editing model, decluttering benchmark 2026 | Newest work | ShanghaiTech-Kujiale, MRoom-30k, Room Envelopes, ICLR 2026 artifact caution; no 2026 benchmark |

WebFetch log (11 calls, 8 returned content):

| # | URL | Purpose | Yield |
|---|---|---|---|
| 1 | https://github.com/princeton-vl/infinigen | Infinigen licence | BSD-3-Clause; Indoors specifics and asset licence not on page; pre-generated data "stay tuned" |
| 2 | https://huggingface.co/Qwen/Qwen-Image-Edit-2511 | Generator licence | Apache-2.0 |
| 3 | https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev | Generator licence | Non-commercial model licence; outputs usable commercially |
| 4 | https://arxiv.org/abs/2509.23909 | EditScore release and agreement | Abstract and release pointer; no agreement numbers |
| 5 | https://github.com/bertjiazheng/Structured3D | Structured3D terms | Terms of Use form; code MIT; configurations not stated on page |
| 6 | https://github.com/zjx0101/ObjectClear | ObjectClear licence and release | NTU S-Lab License 1.0 non-commercial; OBER gated; inference and training code public |
| 7 | https://arxiv.org/abs/2512.17955 | Pair-rendering paper release | No data or code link |
| 8 | https://infinigen.org/docs/ | Infinigen Indoors capabilities | HTTP 404 |
| 9 | https://github.com/princeton-vl/infinigen/blob/main/docs/HelloRoom.md | Same | HTTP 404 |
| 10 | https://github.com/VectorSpaceLab/EditScore | EditScore licence and results | Code Apache-2.0; weights licence not stated; results only in an image |
| 11 | https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset | 3D-FRONT licence | Alibaba Cloud 404 page (URL wrong or gone) |
| 12 | https://huggingface.co/datasets/ApplyDesign/bedroom-dataset | Contents and licence | Four image states and a caption; no licence, no provenance |
| 13 | https://huggingface.co/api/datasets/ApplyDesign/bedroom-dataset | Same, from the Hub API | Gated (manual); 117 GB; no licence field |
| 14 | https://arxiv.org/html/2508.11431v1 | Remove360 capture | 11 scenes, video, before and after views |
| 15 | https://huggingface.co/api/datasets/simkoc/Remove360 | Remove360 licence | MIT, not gated |
| 16 | https://huggingface.co/datasets/Shay85Gil/somethings_missing_here | Contents and licence | 559 pairs, CC-BY-NC-4.0 |
| 17 | https://gfx.cs.princeton.edu/pubs/Wei_2023_CDA/clutter-supp.pdf | Clutter categories | Connection refused |
| 18 | https://arxiv.org/abs/2304.03763 | Same, abstract | Method; no code or data link |
| 19 | https://github.com/zillow/zind | ZInD terms | Academic use only; manual approval |
| 20 | https://arxiv.org/abs/2511.03970 | Room Envelopes | Pointmaps, no empty-room image; no data link |
| 21 | https://svip-lab.github.io/dataset/indoor_360.html | ShanghaiTech-Kujiale | 1,775 rooms with and without furniture; no terms |
| 22 | https://arxiv.org/abs/2509.22628 | MRoom-30k | One sentence only |

Stop rules applied: A stopped at 7 of 8 (results began repeating known pair-quality and synthetic-source works); C stopped at 4 of 5; D, E, B spent in full. Two searches of the 25 stayed unspent.

### 8. Not checked, and why
<!-- Lines 357-371 -->

- Full text of any paper: none was read; only abstract pages and repos (8 fetches). All per-paper numbers are from search summaries and are unverified. Reason: budget and the instruction to fetch only for decision-hinging facts.
- Licences listed as open in the pin: not reached or not worth a search; each needs one fetch of the official page before the design relies on it.
- Human-agreement figures for EditScore, VIEScore, GEdit-Bench judges: the repo shows them only as an image.
- Commercial virtual-unstaging products: not searched (context only; only a patent surfaced).
- Works known from memory and not verified, listed without URL: InstructPix2Pix, MagicBrush, ProcTHOR, ReplicaCAD, Hypersim, RORD, LaMa, ViperGPT, Visual Sketchpad, MLLM-as-a-Judge, VIEScore original paper, ImgEdit original paper.
- Content of the design docs' own prior work (Infinigen Indoors, Structured3D, 3D-FRONT pairs, Matterport pair): not re-read except for licence and release checks, as instructed.
- Public datasets of real photographs for the benchmark (consent, licence): not searched; the OBER dataset (gated, non-commercial) was noted but not assessed.
- Date caveat: several sources carry 2026 arXiv identifiers (26xx) that I could not cross-check beyond search results.
- Second pass, not checked: the ApplyDesign set's provenance (real or generated), resolution, room types and terms (gated, needs an access request); Wei 2023's clutter category list (project server refused the connection); MRoom-30k's content and release; data release of Room Envelopes and of 2512.17955; ShanghaiTech-Kujiale terms and whether its two panoramas share the camera; whether Remove360's before and after views share poses; the ICLR 2026 paper's title and argument.

> **PIN.**
> - Searches used: 23 of the 25 budgeted (A 7 of 8, B 5 of 5, C 4 of 5, D 4 of 4, E 3 of 3); plus 11 WebFetch calls (8 returned content, 3 returned HTTP 404). Second pass on existing pair benchmarks (A): 8 searches (one extended), 11 WebFetch calls (10 returned content, 1 refused).
> - Branches with no relevant work found: none came back empty; four sub-topics did: a public clutter or room taxonomy (A); an indoor defurnishing benchmark or released defurnishing code and data (B); an editing-specific study of VLM-judge bias and human agreement (C); prompt optimization against a VLM-judge objective for an image-editing generator (E).
> - Licence or release not verified that the design depends on: 3D-FRONT licence (official page unreachable); Structured3D Terms of Use text (linked, not read); Infinigen Indoors-specific licence and furniture-off pair rendering (docs unreachable; only the repository-level BSD-3-Clause was read); HSSD licence; PIPE, PIPE_Masks and paint-by-inpaint model licences; ObjectDrop data release; OmniEraser data and code release; ObjectClear weights release (licence NTU S-Lab 1.0, non-commercial, read); EditScore weights licence (code is Apache-2.0, read); BAGEL and Step1X-Edit licences; ADE-CoT code licence; the 2026 Qwen licence claims (secondary sites only); released code or data for the Matterport defurnishing papers and for the 3D-FRONT pair-rendering paper (arXiv 2512.17955, none linked on its abstract page).
