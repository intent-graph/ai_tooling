"""Shared fixtures for CodeMap tests."""

from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_project_path() -> Path:
    """Path to the sample project fixture."""
    return FIXTURES_DIR / "sample_project"
