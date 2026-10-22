"""GPU timing without importing torch: synchronize the device only when torch is already loaded."""

from __future__ import annotations

import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager


def synchronize() -> None:
    torch = sys.modules.get("torch")
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


class Stopwatch:
    """Seconds elapsed inside a `with measure(watch):` block, the GPU drained at both ends."""

    def __init__(self) -> None:
        self.seconds = 0.0


@contextmanager
def measure(watch: Stopwatch) -> Iterator[Stopwatch]:
    synchronize()
    started = time.perf_counter()
    try:
        yield watch
    finally:
        synchronize()
        watch.seconds = time.perf_counter() - started
