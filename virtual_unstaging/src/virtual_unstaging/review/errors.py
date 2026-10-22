"""Stable error codes of the review page: every refused request carries a status and a code, never a stack."""

from __future__ import annotations


class ReviewError(Exception):
    """A refusal at the edge of the review page. `code` is stable and documented in design/review_page.md."""

    def __init__(self, status: int, code: str, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
