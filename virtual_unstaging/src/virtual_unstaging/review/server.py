"""The review page's HTTP server: standard library, 127.0.0.1 only, one session token, strict requests."""

from __future__ import annotations

import hmac
import json
import logging
import re
import secrets
import sqlite3
import sys
from collections.abc import Callable
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib import resources
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from virtual_unstaging.review import parse, service
from virtual_unstaging.review.errors import ReviewError
from virtual_unstaging.store import review_queries as q
from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import connect

LOCAL_ADDRESS = "127.0.0.1"
LOCAL_NAMES = (LOCAL_ADDRESS, "localhost")
TOKEN_HEADER = "X-Review-Token"
_IMAGE_PATH = re.compile(r"/image/([0-9a-f]{64})")
_ATTEMPT_PATH = re.compile(r"/api/attempt/([0-9]{1,10})")
log = logging.getLogger("virtual_unstaging.review")


class ReviewServer(ThreadingHTTPServer):
    """Holds what every request needs: the database path, the blob store, the reviewer, the session token."""

    daemon_threads = True

    def __init__(self, db_path: Path, blobs: BlobStore, reviewer: str, port: int, token: str | None = None) -> None:
        self.db_path = db_path
        self.blobs = blobs
        self.reviewer = parse.check_reviewer(reviewer)
        self.token = token or secrets.token_urlsafe(32)
        self.page = resources.files("virtual_unstaging.review").joinpath("page.html").read_text(encoding="utf-8")
        super().__init__((LOCAL_ADDRESS, port), ReviewHandler)
        self.port = int(self.server_address[1])
        self.allowed_hosts = frozenset(f"{name}:{self.port}" for name in LOCAL_NAMES)

    @property
    def url(self) -> str:
        return f"http://{LOCAL_ADDRESS}:{self.port}/?token={self.token}"


class ReviewHandler(BaseHTTPRequestHandler):
    server: ReviewServer
    server_version = "unstage-review"
    sys_version = ""
    timeout = 30

    def do_GET(self) -> None:
        self._handle(write=False)

    def do_POST(self) -> None:
        self._handle(write=True)

    def log_message(self, format: str, *args: Any) -> None:
        log.debug("%s", format % args if args else format)  # the request line can hold the token: debug level only

    # --- Edge: refuse before anything is read or done ----------------------------------------------------------

    def _handle(self, write: bool) -> None:
        try:
            parts = urlsplit(self.path)
            self._check_host()
            self._check_token(parts.query)
            if write:
                self._check_same_origin()
                self._post(parts.path)
            else:
                self._get(parts.path, parts.query)
        except ReviewError as error:
            self._json(error.status, {"error": {"code": error.code, "message": error.message}})
        except sqlite3.Error:
            log.exception("database error")
            self._json(500, {"error": {"code": "database_error", "message": "the project database refused the request"}})
        except Exception:
            log.exception("unexpected error")
            self._json(500, {"error": {"code": "internal_error", "message": "unexpected error"}})

    def _check_host(self) -> None:
        """DNS rebinding: a page on another name that resolves to 127.0.0.1 still sends its own name as Host."""
        hosts = self.headers.get_all("Host") or []
        if len(hosts) != 1 or hosts[0].lower() not in self.server.allowed_hosts:
            raise ReviewError(403, "bad_host", "the Host header is not this page's local address and port")

    def _check_token(self, query: str) -> None:
        given = self.headers.get(TOKEN_HEADER)
        if given is None:
            given = parse.parse_query(query).get("token")
        if given is None:
            raise ReviewError(403, "missing_token", "the session token is required")
        if not hmac.compare_digest(given.encode(), self.server.token.encode()):
            raise ReviewError(403, "bad_token", "the session token is not valid")

    def _check_same_origin(self) -> None:
        """A write must come from this page: Fetch Metadata says same-origin, or Origin equals the page's origin."""
        site = self.headers.get("Sec-Fetch-Site")
        origin = self.headers.get("Origin")
        if site is None and origin is None:
            raise ReviewError(403, "cross_origin", "a write needs Sec-Fetch-Site or Origin from this page")
        if site is not None and site != "same-origin":
            raise ReviewError(403, "cross_origin", "the write does not come from this page")
        if origin is not None and origin.lower() != f"http://{(self.headers.get('Host') or '').lower()}":
            raise ReviewError(403, "cross_origin", "the Origin header is not this page's origin")
        if self.headers.get(TOKEN_HEADER) is None:
            raise ReviewError(403, "missing_token", f"a write sends the token in the {TOKEN_HEADER} header")

    # --- Routes ------------------------------------------------------------------------------------------------

    def _get(self, path: str, query: str) -> None:
        params = parse.parse_query(query)
        if path == "/":
            self._page()
        elif (match := _IMAGE_PATH.fullmatch(path)) is not None:
            self._image(match.group(1))
        elif path == "/api/meta":
            self._read(lambda conn: service.meta(conn, self.server.reviewer))
        elif path == "/api/review/queue":
            run_id = parse.query_id(params, "run")
            self._read(lambda conn: service.review_queue(conn, run_id, self.server.reviewer))
        elif (match := _ATTEMPT_PATH.fullmatch(path)) is not None:
            attempt_id = int(match.group(1))
            self._read(lambda conn: service.attempt_view(conn, attempt_id, self.server.reviewer))
        elif path == "/api/compare":
            run_a, run_b = parse.query_id(params, "run_a"), parse.query_id(params, "run_b")
            if run_a == run_b:
                raise ReviewError(400, "invalid_query", "run_a, run_b: two different runs are required")
            self._read(lambda conn: service.compare_view(conn, run_a, run_b, self.server.reviewer))
        elif path == "/api/delivery":
            self._read(lambda conn: service.delivery_view(conn, self.server.reviewer))
        else:
            raise ReviewError(404, "not_found", "no such page")

    def _post(self, path: str) -> None:
        reviewer = self.server.reviewer
        body = self._body()
        if path == "/api/review":
            with closing(connect(self.server.db_path)) as conn:
                known = {d.code for d in q.defect_rows(conn)}
                result = service.record_review(conn, reviewer, parse.parse_review(body, known))
        elif path == "/api/preference":
            with closing(connect(self.server.db_path)) as conn:
                result = service.record_preference(conn, reviewer, parse.parse_preference(body))
        elif path == "/api/delivery":
            with closing(connect(self.server.db_path)) as conn:
                result = service.record_delivery(conn, reviewer, parse.parse_delivery(body))
        else:
            raise ReviewError(404, "not_found", "no such endpoint")
        self._json(201, result)

    def _body(self) -> dict[str, Any]:
        if self.headers.get("Transfer-Encoding") is not None:
            raise ReviewError(411, "length_required", "chunked bodies are not accepted")
        kind = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        if kind != "application/json":
            raise ReviewError(415, "unsupported_media_type", "the body must be application/json")
        length = self.headers.get("Content-Length", "")
        if not length.isascii() or not length.isdigit():
            raise ReviewError(411, "length_required", "Content-Length is required")
        if int(length) > parse.MAX_BODY_BYTES:
            raise ReviewError(413, "payload_too_large", f"the body is limited to {parse.MAX_BODY_BYTES} bytes")
        return parse.parse_json_object(self.rfile.read(int(length)))

    # --- Responses ---------------------------------------------------------------------------------------------

    def _read(self, build: Callable[[sqlite3.Connection], dict[str, Any]]) -> None:
        with closing(connect(self.server.db_path)) as conn:
            self._json(200, build(conn))

    def _page(self) -> None:
        nonce = secrets.token_urlsafe(16)
        html = self.server.page.replace("__NONCE__", nonce).encode("utf-8")
        policy = (
            f"default-src 'none'; script-src 'nonce-{nonce}'; style-src 'nonce-{nonce}'; img-src 'self'; "
            "connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'"
        )
        self._send(200, html, "text/html; charset=utf-8", {"Content-Security-Policy": policy, "Cache-Control": "no-store"})

    def _image(self, sha: str) -> None:
        with closing(connect(self.server.db_path)) as conn:
            media_type = q.image_media_type(conn, sha)
        if media_type is None or not self.server.blobs.has(sha):
            raise ReviewError(404, "not_found", "no such image")
        try:
            data = self.server.blobs.get(sha)
        except ValueError:
            log.error("blob %s does not match its hash", sha)
            raise ReviewError(500, "blob_corrupted", "the stored image does not match its hash") from None
        self._send(200, data, media_type, {"Cache-Control": "private, max-age=3600"})

    def _json(self, status: int, payload: dict[str, Any]) -> None:
        self._send(status, json.dumps(payload).encode("utf-8"), "application/json", {"Cache-Control": "no-store"})

    def _send(self, status: int, body: bytes, content_type: str, headers: dict[str, str] | None = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Connection", "close")
        for name, value in (headers or {}).items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)


def start_review_server(
    db_path: Path, blobs: BlobStore, port: int, reviewer: str, token: str | None = None
) -> ReviewServer:
    """Bind 127.0.0.1 (port 0 picks a free one) and return the server, not yet serving."""
    return ReviewServer(db_path, blobs, reviewer, port, token)


def serve_review(db_path: Path, blobs: BlobStore, port: int, reviewer: str) -> None:
    """Serve the review page until interrupted; print the URL that carries this session's token."""
    server = start_review_server(db_path, blobs, port, reviewer)
    print(server.url, flush=True)
    print(f"review page for {reviewer!r}; the link works for this session only; Ctrl-C stops it", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
