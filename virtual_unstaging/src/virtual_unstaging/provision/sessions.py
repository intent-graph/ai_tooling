"""The session log: append-only JSON Lines in the user's state folder; sessions, hours and cost are folds over it."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field, replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

LOG_NAME = "gpu_sessions.jsonl"
SESSION_MARK = "# unstage gpu session "


def to_iso(moment: datetime) -> str:
    return moment.astimezone(UTC).isoformat(timespec="seconds")


def from_iso(text: str | None) -> datetime | None:
    return datetime.fromisoformat(text) if text else None


def append(folder: Path, event: str, session: str, at: datetime, **fields: Any) -> None:
    """One line per event, flushed; an event is never rewritten."""
    folder.mkdir(parents=True, exist_ok=True)
    record = {"ts": to_iso(at), "event": event, "session": session, **fields}
    descriptor = os.open(folder / LOG_NAME, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(descriptor, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()


def read(folder: Path) -> list[dict[str, Any]]:
    path = folder / LOG_NAME
    if not path.is_file():
        return []
    events: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except ValueError:
            continue  # a torn line must not lock every command out
        if isinstance(record, dict) and "event" in record and "session" in record and "ts" in record:
            events.append(record)
    return events


@dataclass(frozen=True)
class Session:
    id: str
    project: str
    provider: str
    machine_name: str
    gpu: str
    gpu_count: int
    limit_seconds: int
    requested_at: datetime
    deadline: datetime
    estimated_price_per_hour: float
    key_file: str = ""
    session_file: str = ""
    machine_id: str = ""
    datacenter: str = ""
    price_per_hour: float = 0.0
    created_at: datetime | None = None
    ready_at: datetime | None = None
    ended_at: datetime | None = None
    end_reason: str = ""
    failure: str = ""
    measurements: dict[str, Any] = field(default_factory=dict)

    @property
    def live(self) -> bool:
        return self.ended_at is None

    @property
    def state(self) -> str:
        if self.ended_at:
            return f"ended ({self.end_reason})"
        if self.failure:
            return "failed"
        if self.ready_at:
            return "ready"
        return "starting" if self.created_at else "requested"

    def hours(self, at: datetime) -> float:
        """Rented hours: from the machine's creation to its end, or to `at` while it lives."""
        if self.created_at is None:
            return 0.0
        end = self.ended_at or at
        return max(0.0, (end - self.created_at).total_seconds() / 3600.0)

    def cost(self, at: datetime) -> float:
        """An estimate (list price times wall time); the provider's own billing is the truth."""
        rate = self.price_per_hour or self.estimated_price_per_hour
        return round(self.hours(at) * rate, 2)


def fold(events: list[dict[str, Any]]) -> list[Session]:
    sessions: dict[str, Session] = {}
    for event in events:
        sid, kind = str(event["session"]), event["event"]
        at = from_iso(event["ts"])
        assert at is not None
        if kind == "requested":
            sessions[sid] = Session(
                id=sid,
                project=str(event.get("project", "")),
                provider=str(event.get("provider", "")),
                machine_name=str(event.get("machine_name", "")),
                gpu=str(event.get("gpu", "")),
                gpu_count=int(event.get("gpu_count", 1)),
                limit_seconds=int(event.get("limit_seconds", 0)),
                requested_at=at,
                deadline=from_iso(event.get("deadline")) or at,
                estimated_price_per_hour=float(event.get("estimated_price_per_hour", 0.0)),
                key_file=str(event.get("key_file", "")),
                session_file=str(event.get("session_file", "")),
            )
            continue
        current = sessions.get(sid)
        if current is None:
            continue
        if kind == "created":
            sessions[sid] = replace(
                current,
                machine_id=str(event.get("machine_id", "")),
                datacenter=str(event.get("datacenter", "")),
                price_per_hour=float(event.get("price_per_hour", 0.0)),
                created_at=at,
            )
        elif kind == "ready":
            sessions[sid] = replace(current, ready_at=at, measurements={**current.measurements, **event.get("measurements", {})})
        elif kind == "failed":
            sessions[sid] = replace(current, failure=str(event.get("reason", "unknown")))
        elif kind == "ended" and current.ended_at is None:
            sessions[sid] = replace(current, ended_at=at, end_reason=str(event.get("by", "unknown")))
    return sorted(sessions.values(), key=lambda s: s.requested_at)


def load(folder: Path) -> list[Session]:
    return fold(read(folder))
