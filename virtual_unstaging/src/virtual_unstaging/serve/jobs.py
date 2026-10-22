"""Asynchronous jobs: work submitted with `Prefer: respond-async` runs in a thread, its outcome is polled by id."""

from __future__ import annotations

import logging
import re
import secrets
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from virtual_unstaging.serve.errors import ApiError

LOG = logging.getLogger("virtual_unstaging.serve")
KEEP_SECONDS = 3600.0  # a finished job stays pollable this long
_JOB_ID = re.compile(r"[0-9a-f]{32}")

QUEUED, RUNNING, DONE, FAILED = "queued", "running", "done", "failed"

# The work of one call: it takes a callback to run once it holds the GPU lock, and returns the response body.
Execute = Callable[[Callable[[], None]], dict[str, Any]]


def wants_async(prefer: str | None) -> bool:
    """True when a `Prefer` header lists the `respond-async` preference (RFC 7240: comma-separated tokens)."""
    if not prefer:
        return False
    tokens = (part.split(";")[0].split("=")[0].strip().lower() for part in prefer.split(","))
    return "respond-async" in tokens


@dataclass
class Job:
    job_id: str
    status: str = QUEUED
    result: dict[str, Any] | None = None
    error: dict[str, str] | None = None
    finished_at: float | None = None


class JobBoard:
    """Jobs in memory: one thread per job (it waits on the GPU lock like any call), forgotten after `keep_seconds`."""

    def __init__(self, keep_seconds: float = KEEP_SECONDS, clock: Callable[[], float] = time.monotonic) -> None:
        self._jobs: dict[str, Job] = {}
        self._lock = threading.Lock()
        self._keep = keep_seconds
        self._clock = clock

    def submit(self, execute: Execute, fallback_code: str) -> str:
        """Start `execute` in a thread and return the job's id; an error that is not an ApiError becomes `fallback_code`."""
        job = Job(secrets.token_hex(16))
        with self._lock:
            self._purge()
            self._jobs[job.job_id] = job
        threading.Thread(target=self._run, args=(job, execute, fallback_code), name=f"job-{job.job_id[:8]}", daemon=True).start()
        return job.job_id

    def get(self, job_id: str) -> dict[str, Any]:
        """The job as `GET /jobs/{id}` answers it; `not_found` for an unknown or expired id."""
        with self._lock:
            self._purge()
            job = self._jobs.get(job_id) if _JOB_ID.fullmatch(job_id) else None
            if job is None:
                raise ApiError("not_found", f"no job {job_id[:40]!r}")
            body: dict[str, Any] = {"job": job.job_id, "status": job.status}
            if job.status == DONE:
                body["result"] = job.result
            elif job.status == FAILED:
                body["error"] = job.error
            return body

    def active(self) -> int:
        """Jobs queued or running."""
        with self._lock:
            return sum(1 for job in self._jobs.values() if job.status in (QUEUED, RUNNING))

    def _set(self, job: Job, **changes: Any) -> None:
        with self._lock:
            for name, value in changes.items():
                setattr(job, name, value)

    def _run(self, job: Job, execute: Execute, fallback_code: str) -> None:
        try:
            result = execute(lambda: self._set(job, status=RUNNING))
        except ApiError as error:
            outcome: dict[str, Any] = {"status": FAILED, "error": {"code": error.code, "message": error.message}}
        except Exception as error:  # the call's own wrapping did not catch it: still a stable code, never a lost job
            LOG.exception("job %s failed", job.job_id)
            outcome = {"status": FAILED, "error": {"code": fallback_code, "message": f"{type(error).__name__}: {str(error)[:300]}"}}
        else:
            outcome = {"status": DONE, "result": result}
        self._set(job, finished_at=self._clock(), **outcome)

    def _purge(self) -> None:
        now = self._clock()
        expired = [key for key, job in self._jobs.items() if job.finished_at is not None and now - job.finished_at > self._keep]
        for key in expired:
            del self._jobs[key]
