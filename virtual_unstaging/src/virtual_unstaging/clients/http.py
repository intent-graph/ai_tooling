"""A small HTTP client on the standard library: bearer key, own User-Agent, timeouts, bounded retries."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field, replace
from typing import Any

from virtual_unstaging import __version__

USER_AGENT = f"virtual-unstaging/{__version__}"
RETRY_STATUSES = {429, 502, 503, 504}


class EndpointError(RuntimeError):
    """A failed call, with a stable code: the server's error code, or one of ours for transport failures."""

    def __init__(self, code: str, message: str, status: int | None = None) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code
        self.status = status


@dataclass(frozen=True)
class Exchange:
    """One attempt of one request, as sent and as answered; the bearer key is left out of the headers."""

    method: str
    url: str
    headers: Mapping[str, str]
    body: bytes | None
    status: int | None  # None when no answer came
    response: bytes
    content_type: str
    seconds: float
    error: str | None  # the error code of a failed attempt
    attempt: int  # 0 for the first, then one per retry


Observer = Callable[[Exchange], None]


@dataclass(frozen=True)
class Endpoint:
    base_url: str
    key: str | None
    timeout: float = 600.0
    retries: int = 3
    # Called after every attempt, success or failure, before the result is used: a caller that records each exchange
    # as sent. An exception it raises fails the call.
    observer: Observer | None = field(default=None, compare=False, repr=False)

    def url(self, path: str) -> str:
        return self.base_url.rstrip("/") + "/" + path.lstrip("/")


def request(
    endpoint: Endpoint,
    method: str,
    path: str,
    body: bytes | None = None,
    content_type: str | None = None,
    accept: str = "application/json",
    extra_headers: dict[str, str] | None = None,
) -> tuple[int, bytes, str]:
    """Send one request; retry transport failures and 429 / 502-504 with backoff. Returns status, body, type."""
    headers = {"User-Agent": USER_AGENT, "Accept": accept, **(extra_headers or {})}
    if endpoint.key:
        headers["Authorization"] = f"Bearer {endpoint.key}"
    if content_type:
        headers["Content-Type"] = content_type
    last: EndpointError | None = None
    for attempt in range(endpoint.retries + 1):
        if attempt:
            time.sleep(min(2.0**attempt, 30.0))
        req = urllib.request.Request(endpoint.url(path), data=body, method=method, headers=headers)
        sent = Exchange(method, endpoint.url(path), _without_key(headers), body, None, b"", "", 0.0, None, attempt)
        started = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=endpoint.timeout) as response:
                status, data, kind = response.status, response.read(), response.headers.get("Content-Type", "")
        except urllib.error.HTTPError as error:
            payload = error.read()
            last = _error_from(error.code, payload)
            kind = error.headers.get("Content-Type", "") if error.headers else ""
            _observe(endpoint, sent, started, error.code, payload, kind, last.code)
            if error.code not in RETRY_STATUSES or last.code == "deadline_reached":
                raise last from None
            continue
        except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
            last = EndpointError("endpoint_unreachable", f"{endpoint.url(path)}: {error}")
            _observe(endpoint, sent, started, None, b"", "", last.code)
            continue
        # Outside the try: whatever the observer raises fails the call, and is never taken for a transport failure.
        _observe(endpoint, sent, started, status, data, kind, None)
        return status, data, kind
    assert last is not None
    raise last


def _without_key(headers: Mapping[str, str]) -> dict[str, str]:
    return {name: value for name, value in headers.items() if name != "Authorization"}


def _observe(
    endpoint: Endpoint, sent: Exchange, started: float, status: int | None, data: bytes, kind: str, error: str | None
) -> None:
    if endpoint.observer is not None:
        endpoint.observer(replace(sent, status=status, response=data, content_type=kind,
                                  seconds=time.monotonic() - started, error=error))


def request_json(endpoint: Endpoint, method: str, path: str, payload: object | None = None) -> Any:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    _, data, _ = request(endpoint, method, path, body, "application/json" if body is not None else None)
    try:
        return json.loads(data)
    except json.JSONDecodeError as error:
        raise EndpointError("bad_response", f"{path}: not JSON ({error})") from None


def _error_from(status: int, payload: bytes) -> EndpointError:
    try:
        error = json.loads(payload)["error"]
        return EndpointError(str(error["code"]), str(error.get("message", "")), status)
    except (ValueError, KeyError, TypeError):
        text = payload[:300].decode("utf-8", "replace")
        code = "unauthorized" if status == 401 else "http_error"
        return EndpointError(code, f"HTTP {status}: {text}", status)
