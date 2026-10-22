"""One HTTP transport on the standard library, injectable so that every test runs without a network."""

from __future__ import annotations

import http.client
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass

from virtual_unstaging import __version__
from virtual_unstaging.provision.errors import ProvisionError

# Cloudflare, in front of GPU rental APIs and their proxies, refuses urllib's default User-Agent (HTTP 403).
USER_AGENT = f"virtual-unstaging/{__version__}"
# What a connection can raise between connecting and the last byte; urllib wraps only part of it.
NETWORK_ERRORS = (OSError, http.client.HTTPException)


@dataclass(frozen=True)
class Response:
    status: int
    body: bytes


# (method, url, headers, body, timeout seconds) -> Response
Transport = Callable[[str, str, dict[str, str], bytes | None, float], Response]


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """A redirect is returned as a response, never followed: the bearer key must not leave its host."""

    def redirect_request(self, *args: object, **kwargs: object) -> None:
        return None


_OPENER = urllib.request.build_opener(_NoRedirect)


def urllib_transport(method: str, url: str, headers: dict[str, str], body: bytes | None, timeout: float) -> Response:
    if urllib.parse.urlsplit(url).scheme != "https" and not _is_loopback(url):
        raise ProvisionError("insecure_url", "only https URLs are called", "the bearer key never travels in clear")
    request = urllib.request.Request(url, data=body, method=method, headers={"User-Agent": USER_AGENT, **headers})
    try:
        with _OPENER.open(request, timeout=timeout) as reply:
            return Response(reply.status, reply.read())
    except urllib.error.HTTPError as error:
        try:
            return Response(error.code, error.read())
        except NETWORK_ERRORS:
            return Response(error.code, b"")
    except NETWORK_ERRORS as error:
        path = urllib.parse.urlsplit(url).path
        raise ProvisionError("provider_unreachable", f"{method} {path}: {type(error).__name__}: {error}") from error


def _is_loopback(url: str) -> bool:
    return urllib.parse.urlsplit(url).hostname in ("127.0.0.1", "localhost")
