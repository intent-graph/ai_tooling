# virtual_unstaging — tool server API

The HTTP contract between the orchestrator and the tool server that runs on the rented GPU: blobs, generation,
tools, health. Both sides ship in one package and one release ([design](README.md#system-shape)); the server
reports its API version and the client refuses a different major version.

> **Status:** *proposal*, implemented in slice 1. The server's OpenAPI description, generated from its code, is
> the machine-readable form; this page is the human one.

## Table of Contents

1. [Conventions](#conventions) _(Lines 26-51)_
1. [Endpoints](#endpoints) _(Lines 54-69)_
1. [Generate](#generate) _(Lines 72-120)_
1. [Generator recipes](#generator-recipes) _(Lines 123-147)_
1. [Tools](#tools) _(Lines 150-173)_
1. [Asynchronous jobs](#asynchronous-jobs) _(Lines 176-199)_
1. [Deadline](#deadline) _(Lines 202-213)_



---

## Conventions
<!-- Lines 26-51 -->

- JSON bodies, UTF-8. Images are never inlined: they travel as blobs, addressed by the SHA-256 of their bytes,
  in lowercase hex. A request is parsed once, at the edge: an unknown field, a wrong type or an out-of-range value
  is `bad_request`.
- Every endpoint except `GET /health` requires `Authorization: Bearer <key>`; the key is read by the server at
  start from the file named by `--key-file`, or from the environment variable named by `--key-env` (the recorded
  exception for rented machines), and is at least 16 printable characters. The key is checked before anything else.
- Errors: HTTP status plus `{"error": {"code": "<stable_code>", "message": "<text>"}}`. Codes and statuses:

  | Code | Status | Meaning |
  |---|---|---|
  | `unauthorized` | 401 | missing or wrong key |
  | `not_found` | 404 | no such endpoint or blob |
  | `blob_missing` | 404 | a referenced blob is absent; the message lists the hashes |
  | `tool_unknown` | 404 | the server does not serve that tool |
  | `hash_mismatch` | 400 | uploaded bytes do not hash to the path |
  | `bad_request` | 400 | the request is not valid; the message names the field |
  | `generator_unavailable` | 503 | no generator configured, or its pipeline failed to load |
  | `generator_failed` | 500 | the pipeline raised while generating |
  | `generator_changed` | 409 | the generator was replaced (`PUT /generator`) after the request was accepted |
  | `tool_failed` | 500 | a tool raised or could not load its model |
  | `deadline_reached` | 503 | the deadline has passed; the client does not retry it |

- API version `1.x`; a server adds fields freely (clients ignore unknown fields), and removes or changes one
  only with a major version.

## Endpoints
<!-- Lines 54-69 -->

| Method and path | Request | Response |
|---|---|---|
| `GET /health` | — | `{"status": "ok", "api_version": "1.2", "deadline": "<ISO 8601 UTC>", "seconds_left": 1234, "busy": false, "jobs": 0, "models": {"generator": "ready", "tools": {"class_diff": "not_loaded"}}}`; `status` is `deadline_reached` past the deadline; a model is `not_loaded`, `loading`, `ready` or `failed` |
| `GET /capabilities` | — | `{"api_version", "server_version", "generator": {...} or null, "tools": [{"name", "version", "model", "inputs", "state"}]}` |
| `HEAD /blobs/{sha256}` | — | 200 if present, 404 otherwise |
| `PUT /blobs/{sha256}` | raw bytes, `Content-Type: image/png` or `image/jpeg` | 201 with `{"sha256", "bytes"}`; 400 `hash_mismatch` if the bytes do not hash to the path; 400 `bad_request` if the bytes are not the declared type, not a decodable image, or above 64 MiB |
| `GET /blobs/{sha256}` | — | the bytes, with their content type |
| `PUT /generator` | `{"recipe": "<packaged name>"}` | releases the generator and its GPU memory, then loads that recipe in the background (`/health` shows `loading`, `ready` or `failed`): one rental clocks or compares several generators |
| `POST /generate` | see [Generate](#generate) | see below; 202 with a job when the request carries `Prefer: respond-async` |
| `POST /tools/{name}` | see [Tools](#tools) | see below; 202 with a job when the request carries `Prefer: respond-async` |
| `GET /jobs/{id}` | — | the state of an [asynchronous job](#asynchronous-jobs) |

Blob addresses are 64 lowercase hexadecimal characters and nothing else; they alone build file paths. An upload
of a blob already stored answers 201 again.

## Generate
<!-- Lines 72-120 -->

The generator's capability profile, in `GET /capabilities`:

```json
{"model": "org/name", "revision": "commit-or-unpinned", "max_images": 4,
 "roles": ["original", "reference", "removal_mask", "protected_mask"],
 "native_mask": false, "text_only": false,
 "settings": {"num_inference_steps": 40, "true_cfg_scale": 4.0, "output_side": 1024},
 "licence": "…", "recipe": "name", "unverified": ["max_images"], "state": "not_loaded"}
```

`unverified` lists the recipe fields whose value was not checked against the model's source or card
([Generator recipes](#generator-recipes)). `max_images_with_native_mask` appears when the pipeline takes a mask
argument and then limits the other images. `text_only` says whether the generator also makes an image from the prompt
alone, a request with no image (API 1.2). `revision` names the weights as run: the commit, followed by
`+fp8:<components>` when the recipe stores components in FP8, so the client never mixes their images with the
full-precision model's.

`POST /generate` request and response:

```json
{"prompt": "…", "seed": 1234, "settings": {"num_inference_steps": 40},
 "images": [{"role": "original", "sha256": "…"}, {"role": "removal_mask", "sha256": "…"},
            {"role": "reference", "sha256": "…"}]}

{"output_sha256": "…", "media_type": "image/png", "width": 1024, "height": 768, "gpu_seconds": 21.4, "load_seconds": 0.0,
 "peak_gpu_gb": 23.8}
```

- Images are given in the order the orchestrator chose; the server's adapter maps roles to the model's inputs
  (a native mask argument when `native_mask`, otherwise the mask as a condition image in that order).
- Either exactly one image has the role `original`, the others take only roles the recipe lists, and no more than
  `max_images` in all; or there is no image at all (`images` empty or left out), a request **from text alone**,
  which only a `text_only` generator accepts: the pipeline is then called without its image argument. With a native
  mask, at most one `removal_mask`, and at most `max_images_with_native_mask` images besides it when the recipe sets
  that limit. A violation is `bad_request`.
- `settings` may name only the recipe's settings (the `settings` of the profile); a value must have the kind of its
  default and lie in a bounded range. `output_side` (256 to 2048) and `condition_side` (0, or 256 to 2048) are the
  adapter's own settings, never passed to the pipeline: the output has about `output_side` squared pixels; with
  `condition_side`, every condition image larger than about `condition_side` squared pixels is reduced to it (masks
  without blending, a native mask to the reduced original's size) before the pipeline sees it. A `text_only`
  generator has a third: `output_aspect` (width over height, 0.25 to 4, default 1.0), the shape of an output made
  from text alone; sent with an image, it is `bad_request`.
- Every referenced blob must be present: otherwise 404 `blob_missing` with the missing hashes in the message.
- The output keeps the original's aspect ratio, or has `output_aspect` from text alone (its sides are multiples of
  the recipe's size multiple, so the ratio holds to within a few percent); its blob is stored on the server for
  `GET /blobs/{sha256}`.
- `gpu_seconds` is the pipeline call only; `load_seconds` is the one-time load of the weights, 0 once resident.

## Generator recipes
<!-- Lines 123-147 -->

One generic adapter serves every diffusers pipeline; a TOML file per model, in `serve/recipes/` or given by path to
`--recipe`, says how that pipeline is loaded and fed. The file is parsed strictly at start: unknown keys, a revision
that is neither a 40-character commit nor `unpinned`, or a value outside its allowed set are refused; the class is
looked up in `diffusers` only.

| Field | Meaning |
|---|---|
| `pipeline.class`, `repository`, `revision`, `dtype`, `placement` | the diffusers class, the Hub repository, its pinned commit (or `unpinned`), the weights' dtype, `cuda` or `model_cpu_offload` |
| `pipeline.fp8_storage` (optional) | pipeline components (diffusers models, such as `transformer`) whose weights are stored in FP8 and computed layer by layer in `dtype`: how a 20B editor fits one 80 GB GPU beside the judge |
| `inputs.roles`, `max_images`, `max_images_with_native_mask` | the image roles accepted and their limits |
| `inputs.native_mask`, `mask_argument` | whether the pipeline has a mask argument, and its name |
| `inputs.text_only` (optional, default false) | the pipeline also generates from the prompt alone, called without its image argument |
| `inputs.image_argument`, `image_passing` | the argument for the image list; `list`, or `single_when_one` for pipelines that take one image as a plain image |
| `inputs.prompt_argument`, `seed_argument` | the prompt argument; the argument that takes the seeded torch generator |
| `output.side`, `multiple`, `width_argument`, `height_argument` | the output area and size multiple; the size is always passed, derived from the original |
| `settings.steps_argument`, `settings.defaults` | which default is the number of steps; every settable name with its default |
| `licence`, `unverified`, `notes` | recorded with the model; fields not verified; remarks for the operator |

The adapter loads the pipeline on first use (or at start, in a background thread, while `/health` shows its
state), keeps it resident, seeds a torch generator from the request's seed, passes the images in request order and
returns a PNG with the GPU seconds. Recipes shipped: `qwen_image_edit_2511`, `firered_image_edit_1_1`, `flux2_dev`,
`flux2_klein_9b`, `flux2_klein_4b`, `qwen_image_2_1`, `fibo_2_0_edit`, `fibo_2_0_dev_edit`, and `fake` (no torch:
fills the mask with the colour around it, for tests and dry runs).

## Tools
<!-- Lines 150-173 -->

`POST /tools/{name}` with `{"inputs": ["<sha256>", …], "params": {…}}` returns
`{"tool", "version", "outputs": {"<name>": "<sha256>"}, "measures": {…}, "summary": "<text>", "gpu_seconds"}`.
An unknown param is `bad_request`. `GET /capabilities` states each tool's `version` (code version plus its model)
and `model`; the orchestrator caches a tool run by tool, version, params and input hashes.

| Tool | Inputs | Params | Outputs and measures |
|---|---|---|---|
| `segment_elements` | `[image]` | `labels` (1 to 64 distinct element names: letters, digits, spaces, hyphens, apostrophes), `threshold` (default 0.3) | `mask` (union, white = found) and one `mask_<i>` per label, zero-based, in label order, always present; measures `found` (share of the frame per label), `detections` (boxes kept per label), `union_share`, `fell_back_to_boxes` (true when the masks are the detection boxes because the segmentation step failed) |
| `class_diff` | `[original, candidate, region_mask]` | `opening_classes` (default door, window, doorway; ADE20K names or those words), `min_share` (default 0.005) | `map` (colour map: red became an opening, blue stopped being one, yellow a class that appeared, cyan one that vanished; dimmed outside the region); measures `opening_share_of_region`, `opening_box`, `opening_share_outside`, `region_share`, and for `inside` and `outside` the classes `appeared` and `vanished` (class absent in one picture and at least `min_share` of the zone in the other) with `share` and `box` in [0, 1] |
| `change_map` | `[original, candidate, region_mask]` | `margin` (fraction of the long side kept clear around the region, default 0.02) | `heatmap` (red = the larger of a displacement of 1% of the long side and a colour difference of 10; the region and its margin are drawn apart); measures `displacement_median_pct`, `displacement_p95_pct` (optical flow outside the region, in % of the long side), `global_shift_px`, `delta_e_median`, `delta_e_p95` (CIE76), `outside_share` |

- The `summary` is one sentence the judge reads, for example "inside the removed region, 3.1% of pixels became
  door/windowpane, at (0.42, 0.30)-(0.55, 0.81)".
- A candidate of another size than the original is resized to it (`candidate_resized` in the measures); the tools
  compare at no more than 1024 pixels on the long side and say so (`compared_at`). Masks are read as white = true,
  threshold 128, resized with nearest neighbour.
- Models: `segment_elements` runs Grounding DINO for the labels' boxes and SAM 2.1 for their masks; `class_diff` runs
  SegFormer-B2 fine-tuned on ADE20K; `change_map` runs OpenCV's Farneback optical flow. All are loaded from
  `transformers` or OpenCV; none is loaded at import.

The orchestrator also runs cheap tools itself (mask dilation, region outline, a pixel-level change map), under
the same names and contract.

## Asynchronous jobs
<!-- Lines 176-199 -->

A proxy in front of a rented machine may cut a request that stays silent for about 100 seconds, and a generation can
last longer. API 1.1 therefore lets a call return at once and be polled; the synchronous behaviour of 1.0 stays for
a client that does not ask.

- A `POST /generate` or `POST /tools/{name}` carrying `Prefer: respond-async` (RFC 7240, a comma-separated list of
  tokens) is validated at once, exactly as a synchronous call (a bad request, a missing blob, an unknown tool answer
  with their usual error and create no job). If valid, it answers 202 `{"job": "<id>", "status": "queued"}` with
  `Preference-Applied: respond-async` and `Location: /jobs/<id>`; the work then runs under the GPU lock as a
  synchronous call does.
- `GET /jobs/{id}` (key required) answers 200 `{"job", "status"}` with `status` one of `queued` (waiting for the GPU
  lock), `running`, `done`, `failed`; plus `"result"`, the body the synchronous call returns, when `done`, and
  `"error": {"code", "message"}`, with the code a synchronous call would give (`generator_failed`, `tool_failed`,
  `deadline_reached` for a job that waited for the GPU past the deadline), when `failed`. An unknown, malformed or
  expired id is 404 `not_found`.
- Jobs live in the server's memory and are forgotten an hour after they finish; a restart loses them. A job id is 128
  random bits.
- The deadline refuses new submissions like any call, but `GET /jobs/{id}` keeps answering until the process exits;
  jobs queued or running count as calls in flight for the exit.
- The orchestrator's `ToolServerClient` always submits with the preference and polls `GET /jobs/{id}` every 2
  seconds, growing by a quarter each time up to 5 seconds, until `done` (it returns the result) or `failed` (it
  raises its `EndpointError` with the job's code). A poll is an ordinary request, retried on transport failures. A
  server that ignores the preference and answers 200 is read as a synchronous answer.

## Deadline
<!-- Lines 202-213 -->

The server refuses to start without `--deadline` (a duration such as `90m`, `2h`, `1h30m`, or an ISO 8601 time with
a UTC offset, in the future). Past it, every endpoint except `GET /health` answers 503 `deadline_reached`, the calls
and jobs in flight finish or fail (up to a grace of two minutes), and the process exits. Work that waited for the GPU lock past
the deadline is refused, not started. The machine's own self-delete is the provider's job
([design](README.md#model-services-and-provisioning)).

One lock serializes all GPU work: generation and tools run one at a time, in arrival order.

`--tools` lists the tools to serve (`segment_elements`, `class_diff`, `change_map`), or `fake` for stand-ins of all
three that need no torch and no weights; `--recipe` names a generator recipe or a TOML file, and without it the
server serves tools only.
