"""Client of the tool server (design/tool_server_api.md): blobs, capabilities, generation, tools."""

from __future__ import annotations

import json
import re
import time
from collections.abc import Callable
from typing import Any

from virtual_unstaging.clients.http import Endpoint, EndpointError, request, request_json
from virtual_unstaging.domain import sha256_bytes

API_MAJOR = 1
POLL_SECONDS = 2.0  # first wait between polls of a job; it grows by a quarter each time, up to POLL_MAX_SECONDS
POLL_MAX_SECONDS = 5.0
_JOB_ID = re.compile(r"[0-9a-f]{32}")


class ToolServerClient:
    def __init__(self, endpoint: Endpoint) -> None:
        self.endpoint = endpoint
        self._checked = False
        self.sleep: Callable[[float], None] = time.sleep  # replaced in tests

    def health(self) -> dict[str, Any]:
        result: dict[str, Any] = request_json(self.endpoint, "GET", "/health")
        return result

    def capabilities(self) -> dict[str, Any]:
        caps: dict[str, Any] = request_json(self.endpoint, "GET", "/capabilities")
        major = int(str(caps.get("api_version", "0")).split(".")[0])
        if major != API_MAJOR:
            raise EndpointError("api_version", f"server API {caps.get('api_version')}, client expects {API_MAJOR}.x")
        self._checked = True
        return caps

    def ensure_blob(self, data: bytes, media_type: str) -> str:
        """Upload once: the server keeps blobs by hash for the life of the machine."""
        sha = sha256_bytes(data)
        try:
            status, _, _ = request(self.endpoint, "HEAD", f"/blobs/{sha}")
            if status == 200:
                return sha
        except EndpointError as error:
            if error.status != 404:
                raise
        request(self.endpoint, "PUT", f"/blobs/{sha}", data, media_type)
        return sha

    def get_blob(self, sha: str) -> bytes:
        _, data, _ = request(self.endpoint, "GET", f"/blobs/{sha}", accept="*/*")
        if sha256_bytes(data) != sha:
            raise EndpointError("hash_mismatch", f"blob {sha} came back with other bytes")
        return data

    def generate(self, payload: dict[str, object]) -> dict[str, Any]:
        self._check()
        return self._submit("/generate", payload)

    def run_tool(self, name: str, inputs: list[str], params: dict[str, object]) -> dict[str, Any]:
        self._check()
        return self._submit(f"/tools/{name}", {"inputs": inputs, "params": params})

    def _submit(self, path: str, payload: dict[str, object]) -> dict[str, Any]:
        """Post with `Prefer: respond-async` and poll the job: no request stays silent long enough for a proxy to cut it."""
        status, data, _ = request(
            self.endpoint, "POST", path, json.dumps(payload).encode("utf-8"), "application/json",
            extra_headers={"Prefer": "respond-async"},
        )
        answer = _json_object(path, data)
        if status != 202:  # a 1.0 server ignores the preference and answers at once
            return answer
        job_id = answer.get("job")
        if not isinstance(job_id, str) or not _JOB_ID.fullmatch(job_id):
            raise EndpointError("bad_response", f"{path}: the job id is missing or malformed")
        return self._await_job(job_id)

    def _await_job(self, job_id: str) -> dict[str, Any]:
        wait = POLL_SECONDS
        while True:
            job = _json_object(f"/jobs/{job_id}", request(self.endpoint, "GET", f"/jobs/{job_id}")[1])
            state = job.get("status")
            if state == "done" and isinstance(job.get("result"), dict):
                result: dict[str, Any] = job["result"]
                return result
            if state == "failed":
                reported = job.get("error")
                error: dict[str, Any] = reported if isinstance(reported, dict) else {}
                raise EndpointError(str(error.get("code", "bad_response")), str(error.get("message", "the job failed")))
            if state not in ("queued", "running"):
                raise EndpointError("bad_response", f"/jobs/{job_id}: unexpected job status {state!r}")
            self.sleep(wait)
            wait = min(wait * 1.25, POLL_MAX_SECONDS)

    def _check(self) -> None:
        if not self._checked:
            self.capabilities()


def _json_object(path: str, data: bytes) -> dict[str, Any]:
    try:
        value = json.loads(data)
    except json.JSONDecodeError as error:
        raise EndpointError("bad_response", f"{path}: not JSON ({error})") from None
    if not isinstance(value, dict):
        raise EndpointError("bad_response", f"{path}: expected a JSON object")
    return value
