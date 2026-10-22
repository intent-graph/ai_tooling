"""The generic generator adapter: a recipe maps a request's roles onto a diffusers pipeline's arguments."""

from __future__ import annotations

import importlib
import threading
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol

import numpy as np
from PIL import Image

from virtual_unstaging.domain import JsonScalar, sha256_text
from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.errors import ApiError
from virtual_unstaging.serve.pixels import dilate_square
from virtual_unstaging.serve.recipe import (
    ADAPTER_SETTINGS,
    CONDITION_SIDE_SETTING,
    OUTPUT_ASPECT_SETTING,
    OUTPUT_SIDE_SETTING,
    UNPINNED,
    Recipe,
)
from virtual_unstaging.serve.timing import Stopwatch, measure

NOT_LOADED, LOADING, READY, FAILED = "not_loaded", "loading", "ready", "failed"


@dataclass(frozen=True)
class ImageInput:
    role: str
    image: Image.Image  # RGB for photos, L for masks


@dataclass(frozen=True)
class GenerationJob:
    prompt: str
    seed: int
    settings: Mapping[str, JsonScalar]  # already merged with the recipe's defaults and validated
    images: tuple[ImageInput, ...]  # in the order the orchestrator chose


@dataclass(frozen=True)
class GenerationResult:
    png: bytes
    width: int
    height: int
    gpu_seconds: float
    load_seconds: float = 0.0
    peak_gpu_gb: float | None = None  # this process's peak GPU memory during the call; None without CUDA


@dataclass(frozen=True)
class CallPlan:
    """What the pipeline is called with, except the seeded random generator: arguments, output size."""

    arguments: dict[str, Any]
    width: int
    height: int
    seed: int


class Generator(Protocol):
    recipe: Recipe

    def profile(self) -> dict[str, Any]: ...

    def state(self) -> str: ...

    def warm(self) -> None: ...

    def unload(self) -> None: ...

    def generate(self, job: GenerationJob) -> GenerationResult: ...


def check_request(recipe: Recipe, roles: list[str], requested: Mapping[str, JsonScalar]) -> dict[str, JsonScalar]:
    """Roles and settings together; returns the settings merged with the recipe's defaults."""
    check_roles(recipe, roles)
    if roles and OUTPUT_ASPECT_SETTING in requested:
        raise ApiError("bad_request", f"{OUTPUT_ASPECT_SETTING} applies only without images: an output keeps its original's aspect ratio")
    return recipe.settings_for(requested)


def check_roles(recipe: Recipe, roles: list[str]) -> None:
    """The request's image roles against the recipe: known roles, a count within bounds, one original (or no image at
    all, from text alone, when the recipe allows it), mask rules."""
    if not roles:
        if not recipe.text_only:
            raise ApiError("bad_request", f"recipe {recipe.name} does not generate from text alone: send an image with the role 'original'")
        return
    for role in roles:
        if role not in recipe.roles:
            raise ApiError("bad_request", f"role {role!r} is not accepted by recipe {recipe.name} ({', '.join(recipe.roles)})")
    if len(roles) > recipe.max_images:
        raise ApiError("bad_request", f"{len(roles)} images sent, recipe {recipe.name} takes at most {recipe.max_images}")
    if roles.count("original") != 1:
        raise ApiError("bad_request", "exactly one image must have the role 'original'")
    if recipe.native_mask and "removal_mask" in roles:
        if roles.count("removal_mask") > 1:
            raise ApiError("bad_request", "at most one image can have the role 'removal_mask'")
        limit = recipe.max_images_with_native_mask
        if limit is not None and len(roles) - 1 > limit:
            raise ApiError(
                "bad_request",
                f"recipe {recipe.name} takes the mask as an argument and then at most {limit} image(s) besides it",
            )


def plan_call(recipe: Recipe, job: GenerationJob) -> CallPlan:
    """Map the job onto the pipeline's arguments: images in request order, a native mask on its own argument; from
    text alone, no image argument at all and the requested aspect ratio."""
    original = next((item.image for item in job.images if item.role == "original"), None)
    side = int(job.settings.get(OUTPUT_SIDE_SETTING, recipe.output_side))
    if original is None:
        shape = (round(float(job.settings.get(OUTPUT_ASPECT_SETTING, 1.0)) * 1000), 1000)
    else:
        shape = original.size
    width, height = imaging.output_size(shape, side, recipe.output_multiple)
    reduce_to = int(job.settings.get(CONDITION_SIDE_SETTING, 0))  # a speed version: fewer tokens per condition image
    seen = shape
    if original is not None and reduce_to:
        seen = imaging.reduce_area(original, reduce_to).size
    condition: list[Image.Image] = []
    mask: Image.Image | None = None
    for item in job.images:
        if item.role == "removal_mask" and recipe.native_mask:
            resized = item.image.convert("L").resize(seen, Image.Resampling.NEAREST)
            mask = imaging.mask_image(imaging.to_mask(resized))
        else:
            image = item.image.convert("RGB")
            nearest = item.role.endswith("_mask")
            condition.append(imaging.reduce_area(image, reduce_to, nearest) if reduce_to else image)
    arguments: dict[str, Any] = {
        recipe.prompt_argument: job.prompt,
        recipe.width_argument: width,
        recipe.height_argument: height,
    }
    if condition:
        single = recipe.image_passing == "single_when_one" and len(condition) == 1
        arguments[recipe.image_argument] = condition[0] if single else condition
    if mask is not None:
        arguments[recipe.mask_argument] = mask
    for name, value in job.settings.items():
        if name not in ADAPTER_SETTINGS:
            arguments[name] = value
    return CallPlan(arguments, width, height, job.seed)


class DiffusersGenerator:
    """Loads the recipe's diffusers pipeline on first use and keeps it resident; one call at a time (the caller's lock)."""

    def __init__(self, recipe: Recipe) -> None:
        self.recipe = recipe
        self._pipeline: Any = None
        self._state = NOT_LOADED
        self._load_lock = threading.Lock()
        self.load_seconds = 0.0
        self.error = ""
        self.peak_gpu_gb: float | None = None

    def profile(self) -> dict[str, Any]:
        profile = {**self.recipe.profile(), "state": self._state}
        if self._state == FAILED and self.error:
            profile["error"] = self.error
        if self.peak_gpu_gb is not None:
            profile["peak_gpu_gb"] = self.peak_gpu_gb
        return profile

    def state(self) -> str:
        return self._state

    def warm(self) -> None:
        self._load()

    def unload(self) -> None:
        """Release the pipeline and the GPU memory it held, so another recipe can load in this process."""
        with self._load_lock:
            self._pipeline = None
            self._state = NOT_LOADED
            self.peak_gpu_gb = None
        import gc

        gc.collect()
        _release_cached_memory()

    def _load(self) -> Any:
        with self._load_lock:
            if self._pipeline is not None:
                return self._pipeline
            self._state = LOADING
            watch = Stopwatch()
            try:
                with measure(watch):
                    import torch  # heavy: only here
                    diffusers = importlib.import_module("diffusers")

                    pipeline_class = getattr(diffusers, self.recipe.pipeline_class)
                    revision = None if self.recipe.revision == UNPINNED else self.recipe.revision
                    dtype = getattr(torch, self.recipe.dtype)
                    pipeline = pipeline_class.from_pretrained(self.recipe.repository, revision=revision, dtype=dtype)
                    if self.recipe.scheduler:
                        config = {**pipeline.scheduler.config, **self.recipe.scheduler}
                        pipeline.scheduler = type(pipeline.scheduler).from_config(config)
                    lora = self.recipe.lora
                    if lora is not None:  # fused, then the adapter layers dropped: plain weights from here on
                        pipeline.load_lora_weights(lora.repository, weight_name=lora.weight_name, revision=lora.revision,
                                                   adapter_name="recipe")
                        pipeline.fuse_lora(lora_scale=lora.scale)
                        pipeline.unload_lora_weights()
                    for component in self.recipe.fp8_storage:  # weights kept in FP8, each layer computed in dtype
                        getattr(pipeline, component).enable_layerwise_casting(
                            storage_dtype=torch.float8_e4m3fn, compute_dtype=dtype
                        )
                    if self.recipe.placement == "model_cpu_offload":
                        pipeline.enable_model_cpu_offload()
                    else:
                        pipeline = pipeline.to("cuda")
            except Exception as error:
                self._state = FAILED
                self.error = f"{type(error).__name__}: {str(error)[:300]}"
                raise ApiError("generator_unavailable", f"cannot load {self.recipe.repository}: {self.error}") from error
            self._pipeline = pipeline
            self._state = READY
            self.load_seconds = watch.seconds
            self.error = ""
            return pipeline

    def generate(self, job: GenerationJob) -> GenerationResult:
        pipeline = self._load()
        plan = plan_call(self.recipe, job)
        watch = Stopwatch()
        try:
            import torch

            arguments = dict(plan.arguments)
            arguments[self.recipe.seed_argument] = torch.Generator(device="cuda").manual_seed(plan.seed)
            cuda = torch.cuda.is_available()
            if cuda:
                torch.cuda.reset_peak_memory_stats()
            with measure(watch):
                output = pipeline(**arguments)
            if cuda:
                self.peak_gpu_gb = round(torch.cuda.max_memory_allocated() / 1e9, 2)
            image = output.images[0]
            png = imaging.encode_png(image.convert("RGB"))
        except ApiError:
            raise
        except Exception as error:
            _release_cached_memory()
            raise ApiError("generator_failed", f"{type(error).__name__}: {str(error)[:300]}") from error
        return GenerationResult(png, image.width, image.height, watch.seconds, self.load_seconds, self.peak_gpu_gb)


def _release_cached_memory() -> None:
    import sys

    torch = sys.modules.get("torch")
    if torch is not None and torch.cuda.is_available():
        torch.cuda.empty_cache()


@dataclass
class FakeGenerator:
    """Needs no torch: the original with the removal mask filled by the colour around it, plus a faint seeded pattern;
    from text alone, a flat colour set by prompt and seed, with a faint grain."""

    recipe: Recipe
    calls: list[CallPlan] = field(default_factory=list)

    def profile(self) -> dict[str, Any]:
        return {**self.recipe.profile(), "state": READY}

    def state(self) -> str:
        return READY

    def warm(self) -> None:
        return None

    def unload(self) -> None:
        return None

    def generate(self, job: GenerationJob) -> GenerationResult:
        plan = plan_call(self.recipe, job)
        self.calls.append(plan)
        watch = Stopwatch()
        with measure(watch):
            noise = np.random.default_rng(int(sha256_text(job.prompt)[:8], 16) ^ job.seed)
            original = next((item.image for item in job.images if item.role == "original"), None)
            if original is None:
                colour = noise.integers(40, 216, size=3)
                grain = noise.normal(0, 2.0, size=(plan.height, plan.width, 3))
                pixels = np.clip(colour + grain, 0, 255).astype(np.uint8)
            else:
                output = original.convert("RGB").resize((plan.width, plan.height), Image.Resampling.LANCZOS)
                pixels = np.asarray(output).copy()
                masks = [item.image for item in job.images if item.role == "removal_mask"]
                if masks:
                    mask = imaging.to_mask(masks[0], (plan.width, plan.height))
                    ring = dilate_square(mask, 8) & ~mask
                    fill = pixels[ring].mean(axis=0) if ring.any() else pixels.reshape(-1, 3).mean(axis=0)
                    pixels[mask] = np.clip(fill + noise.normal(0, 2.0, size=(int(mask.sum()), 3)), 0, 255).astype(np.uint8)
            png = imaging.encode_png(Image.fromarray(pixels))
        return GenerationResult(png, plan.width, plan.height, watch.seconds)


def build_generator(recipe: Recipe) -> Generator:
    return FakeGenerator(recipe) if recipe.adapter == "fake" else DiffusersGenerator(recipe)
