"""Runpod provider: pods on the secure cloud through the REST API v2 (https://api.runpod.io/v2), standard library only."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
from collections.abc import Callable, Iterable
from importlib import resources
from typing import Any

from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.provider import (
    FAILED,
    GONE,
    RUNNING,
    STARTING,
    STOPPED,
    GpuOffer,
    Machine,
    MachineSpec,
)
from virtual_unstaging.provision.transport import Response, Transport, urllib_transport

API_BASE = "https://api.runpod.io/v2"
POD_ID = re.compile(r"^[A-Za-z0-9_-]{4,64}$")
_STATUS = {
    "PROVISIONING": STARTING,
    "STARTING": STARTING,
    "RUNNING": RUNNING,
    "EXITED": STOPPED,
    "ERROR": FAILED,
    "TERMINATED": GONE,
}
MAX_PAGES = 50


class RunpodProvider:
    name = "runpod"
    guard_class = "RunpodSelfDelete"

    def __init__(
        self,
        api_key: str,
        transport: Transport = urllib_transport,
        sleep: Callable[[float], None] = time.sleep,
        base: str = API_BASE,
    ) -> None:
        self._key = api_key
        self._transport = transport
        self._sleep = sleep
        self._base = base.rstrip("/")
        self._guard_source: str | None = None

    @property
    def guard_source(self) -> str:
        if self._guard_source is None:
            self._guard_source = resources.files("virtual_unstaging.provision").joinpath("runpod_guard.py").read_text("utf-8")
        return self._guard_source

    # -- plumbing ---------------------------------------------------------------------------------------

    def _call(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, str] | None = None,
        body: dict[str, Any] | None = None,
        allow: Iterable[int] = (),
        scrub: Iterable[str] = (),
    ) -> tuple[int, Any]:
        url = self._base + path
        if query:
            url += "?" + urllib.parse.urlencode(query)
        headers = {"Authorization": f"Bearer {self._key}", "Accept": "application/json"}
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")
        # A 5xx after a POST may hide a created machine: only idempotent calls are retried on it.
        # A 429 means the request was not processed, so any call may be retried.
        idempotent = method in ("GET", "DELETE", "PUT")
        reply = Response(0, b"")
        for attempt in range(4):
            reply = self._transport(method, url, headers, data, 60.0)
            if (reply.status == 429 or (reply.status >= 500 and idempotent)) and attempt < 3:
                self._sleep(2.0 ** (attempt + 1))
                continue
            break
        payload: Any = None
        if reply.body.strip():
            try:
                payload = json.loads(reply.body)
            except ValueError:
                payload = None  # an edge's HTML error page
        if 200 <= reply.status < 300 or reply.status in set(allow):
            return reply.status, payload
        raise self._error(method, path, reply.status, payload, reply.body, list(scrub))

    @staticmethod
    def _error(method: str, path: str, status: int, payload: Any, raw: bytes, scrub: list[str]) -> ProvisionError:
        where = f"Runpod {method} {path}"
        if status in (401, 403):
            if isinstance(payload, dict):
                return ProvisionError("provider_auth", f"{where}: HTTP {status}: key rejected or not allowed",
                                      "check the Runpod API key (read and write access to pods)")
            return ProvisionError("provider_error", f"{where}: HTTP {status} from the edge, not from the API")
        detail = ""
        if isinstance(payload, dict):
            parts = [payload.get("title"), payload.get("detail"), *(payload.get("errors") or [])]
            detail = "; ".join(str(part) for part in parts if part)
        for secret in scrub:
            if len(secret) >= 8:
                detail = detail.replace(secret, "[hidden]")
        detail = f": {detail[:400]}" if detail else ""
        if status == 402:
            return ProvisionError("provider_balance", f"{where}: HTTP 402{detail}", "add credit to the Runpod account")
        if method == "POST" and path == "/pods" and status == 400:
            # The API gives capacity and rule errors the same status: the caller tries the next candidate.
            return ProvisionError("provider_refused", f"{where}: HTTP 400{detail}")
        return ProvisionError("provider_error", f"{where}: HTTP {status}{detail}")

    @staticmethod
    def _check_id(machine_id: str) -> str:
        if not POD_ID.fullmatch(machine_id):
            raise ProvisionError("provider_error", "refusing an identifier of an unexpected form")
        return machine_id

    @staticmethod
    def _machine(pod: dict[str, Any], fallback_dc: str = "") -> Machine:
        return Machine(
            id=str(pod.get("id", "")),
            name=str(pod.get("name", "")),
            status=_STATUS.get(str(pod.get("status", "")), STARTING),
            price_per_hour=float(pod.get("cost") or 0.0),
            datacenter=str(pod.get("dataCenterId") or fallback_dc),
        )

    # -- the provider interface -------------------------------------------------------------------------

    def offers(self, min_cuda: str | None = None) -> list[GpuOffer]:
        query = {"include": "AVAILABILITY", "product": "POD", "cloud": "SECURE"}
        if min_cuda:
            query["minCudaVersion"] = min_cuda
        _, payload = self._call("GET", "/catalog/gpus", query=query)
        offers = []
        for gpu in (payload or {}).get("gpus", []):
            price = (gpu.get("price") or {}).get("secure")
            if not gpu.get("secure") or price is None:
                continue
            centers = tuple(
                (str(c["id"]), str(c.get("availability", "NONE"))) for c in gpu.get("dataCenters") or [] if "id" in c
            )
            offers.append(
                GpuOffer(
                    gpu_id=str(gpu["id"]),
                    name=str(gpu.get("name", gpu["id"])),
                    memory_gb=int(gpu.get("memory", 0)),
                    price_per_hour=float(price),
                    stock=str(gpu.get("availability", "NONE")),
                    datacenters=centers,
                )
            )
        return offers

    def create(self, spec: MachineSpec) -> Machine:
        gpu: dict[str, Any] = {"id": spec.gpu_id, "count": spec.gpu_count}
        if spec.min_cuda:
            gpu["minCudaVersion"] = spec.min_cuda
        body: dict[str, Any] = {
            "name": spec.name,
            "image": spec.image,
            "cloud": "SECURE",
            "gpu": gpu,
            "dataCenterIds": [spec.datacenter],
            "entrypoint": list(spec.entrypoint),
            "disk": spec.disk_gb,
            "ports": [f"{port}/http" for port in spec.ports],
            "env": dict(spec.env),
        }
        _, pod = self._call("POST", "/pods", body=body, scrub=list(spec.env.values()))
        if not isinstance(pod, dict) or not pod.get("id"):
            raise ProvisionError("provider_error", "Runpod created a machine but did not say which")
        return self._machine(pod, spec.datacenter)

    def get(self, machine_id: str) -> Machine | None:
        status, pod = self._call("GET", f"/pods/{self._check_id(machine_id)}", allow=(404,))
        if status == 404 or not isinstance(pod, dict):
            return None
        return self._machine(pod)

    def _pods(self) -> list[dict[str, Any]]:
        pods: list[dict[str, Any]] = []
        cursor: str | None = None
        for _ in range(MAX_PAGES):
            _, page = self._call("GET", "/pods", query={"cursor": cursor} if cursor else None)
            page = page or {}
            pods += [p for p in page.get("pods", []) if isinstance(p, dict)]
            cursor = (page.get("pagination") or {}).get("nextCursor")
            if not cursor:
                break
        return pods

    def list_machines(self, name_prefix: str) -> list[Machine]:
        return [
            self._machine(pod)
            for pod in self._pods()
            if str(pod.get("name", "")).startswith(name_prefix) and pod.get("status") != "TERMINATED"
        ]

    def find(self, name: str) -> Machine | None:
        found = [m for m in self.list_machines(name) if m.name == name]
        return found[0] if found else None

    def delete(self, machine_id: str) -> None:
        self._call("DELETE", f"/pods/{self._check_id(machine_id)}", allow=(404,))

    def url(self, machine_id: str, port: int) -> str:
        return f"https://{self._check_id(machine_id)}-{int(port)}.proxy.runpod.net"
