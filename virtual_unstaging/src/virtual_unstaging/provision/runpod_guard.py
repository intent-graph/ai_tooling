"""Runpod's self-delete, stdlib only, shipped to the machine after the bootstrap (it subclasses `SelfDelete`).

Never imported: the bootstrap defines `SelfDelete`, and this text is appended to it (see `machine.py`).

Runpod injects `RUNPOD_POD_ID` and a pod-scoped `RUNPOD_API_KEY` into every pod. The ways to end the pod, in order:
REST v2 terminate, REST v2 delete, GraphQL terminate (key as bearer, then as query parameter), then stop (the GPU is
released, the disk keeps billing). Runpod's documentation says the key is scoped to the pod; it does not say outright
that the key may end its pod, so that is the open point of a first live run (the probe, a read, is checked at start).
"""

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any

RUNPOD_API = "https://api.runpod.io/v2"
RUNPOD_GRAPHQL = "https://api.runpod.io/graphql"
# Cloudflare, in front of the API, refuses urllib's default User-Agent.
RUNPOD_HEADERS = {"Content-Type": "application/json", "User-Agent": "unstage-guard"}


def runpod_call(
    method: str, url: str, key: str, body: dict[str, Any] | None = None, key_in_query: bool = False, graphql: bool = False
) -> int:
    """HTTP status of one call, 0 on a network failure; a GraphQL answer with `errors` counts as 400."""
    if key_in_query:
        url += "?" + urllib.parse.urlencode({"api_key": key})
        headers = dict(RUNPOD_HEADERS)
    else:
        headers = {"Authorization": "Bearer " + key, **RUNPOD_HEADERS}
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as reply:
            if graphql and json.loads(reply.read() or b"{}").get("errors"):
                return 400
            return int(reply.status)
    except urllib.error.HTTPError as error:
        return int(error.code)
    except (OSError, ValueError):
        return 0


class RunpodSelfDelete(SelfDelete):  # type: ignore[name-defined, misc]  # noqa: F821 - defined by the bootstrap above
    def __init__(self, env: Mapping[str, str]) -> None:
        super().__init__(env)
        pod = env.get("RUNPOD_POD_ID", "")
        self.pod = pod if re.fullmatch(r"[A-Za-z0-9]{4,40}", pod) else ""
        self.key = env.get("RUNPOD_API_KEY", "")
        self.call: Callable[..., int] = runpod_call

    def probe(self) -> str | None:
        if not self.pod or not self.key:
            return None
        status = self.call("GET", f"{RUNPOD_API}/pods/{self.pod}", self.key)
        return "rest-v2" if 200 <= status < 300 else None

    def _first_success(self, attempts: list[Callable[[], int]]) -> bool:
        if not self.pod or not self.key:
            return False
        for attempt in attempts:
            status = attempt()
            if 200 <= status < 300 or status == 404:  # 404: the pod is already gone
                return True
        return False

    def terminate(self) -> bool:
        mutation = f'mutation {{ podTerminate(input: {{podId: "{self.pod}"}}) }}'
        return self._first_success(
            [
                lambda: self.call("POST", f"{RUNPOD_API}/pods/{self.pod}/action", self.key, {"action": "terminate"}),
                lambda: self.call("DELETE", f"{RUNPOD_API}/pods/{self.pod}", self.key),
                lambda: self.call("POST", RUNPOD_GRAPHQL, self.key, {"query": mutation}, graphql=True),
                lambda: self.call("POST", RUNPOD_GRAPHQL, self.key, {"query": mutation}, key_in_query=True, graphql=True),
            ]
        )

    def stop(self) -> bool:
        mutation = f'mutation {{ podStop(input: {{podId: "{self.pod}"}}) {{ id }} }}'
        return self._first_success(
            [
                lambda: self.call("POST", f"{RUNPOD_API}/pods/{self.pod}/action", self.key, {"action": "stop"}),
                lambda: self.call("POST", RUNPOD_GRAPHQL, self.key, {"query": mutation}, graphql=True),
            ]
        )
