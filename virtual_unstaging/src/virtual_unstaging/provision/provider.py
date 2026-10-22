"""The provider interface: what a GPU rental service must offer so that `up`, `down`, `ls` and `price` run on it."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Protocol

STOCK_RANK = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "NONE": 0}

# Machine states, the same for every provider.
STARTING, RUNNING, STOPPED, FAILED, GONE = "starting", "running", "stopped", "failed", "gone"


@dataclass(frozen=True)
class GpuOffer:
    """One GPU type: its list price per GPU-hour and where it is in stock (data center, stock level)."""

    gpu_id: str
    name: str
    memory_gb: int
    price_per_hour: float
    stock: str
    datacenters: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class MachineSpec:
    """What to rent. The entrypoint and environment carry the on-machine bootstrap (see `machine.py`)."""

    name: str
    gpu_id: str
    gpu_count: int
    datacenter: str
    image: str
    disk_gb: int
    ports: tuple[int, ...]
    env: Mapping[str, str]
    entrypoint: tuple[str, ...]
    min_cuda: str | None = None


@dataclass(frozen=True)
class Machine:
    id: str
    name: str
    status: str
    price_per_hour: float
    datacenter: str


class Provider(Protocol):
    """Implement this and register the class in `providers.py` to plug another rental service in.

    Contract:
    - `create` is called once per attempt and is never retried blindly: after a lost answer the caller looks the
      machine up by its unique name with `find`.
    - `delete` is idempotent: a machine already gone is not an error.
    - Errors are `ProvisionError`s with the codes `provider_auth`, `provider_balance`, `provider_refused` (this
      candidate cannot be placed: try the next), `provider_unreachable`, `provider_error`.
    - `guard_source` is stdlib-only Python defining a subclass of the bootstrap's `SelfDelete`, named
      `guard_class`: how a machine deletes itself on that service.
    """

    name: str
    guard_class: str

    @property
    def guard_source(self) -> str: ...

    def offers(self, min_cuda: str | None = None) -> list[GpuOffer]: ...

    def create(self, spec: MachineSpec) -> Machine: ...

    def get(self, machine_id: str) -> Machine | None: ...

    def find(self, name: str) -> Machine | None: ...

    def list_machines(self, name_prefix: str) -> list[Machine]: ...

    def delete(self, machine_id: str) -> None: ...

    def url(self, machine_id: str, port: int) -> str: ...


def datacenters_by_stock(offer: GpuOffer) -> list[str]:
    """Data centers where the offer is in stock, best stocked first."""
    stocked = [(dc, level) for dc, level in offer.datacenters if STOCK_RANK.get(level, 0) > 0]
    return [dc for dc, _ in sorted(stocked, key=lambda item: -STOCK_RANK[item[1]])]
