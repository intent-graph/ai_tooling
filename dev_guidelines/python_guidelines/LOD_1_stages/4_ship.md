# 4 Ship

> Package, validate quality, deploy.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 50-52)_
   1. [Why Shipping Matters](#why-shipping-matters) _(Lines 55-57)_
   1. [What Happens Here](#what-happens-here) _(Lines 60-66)_
   1. [Entry Criteria](#entry-criteria) _(Lines 69-74)_
   1. [Exit Criteria](#exit-criteria) _(Lines 77-89)_
1. [Packaging Phase](#packaging-phase) _(Lines 92-94)_
   1. [pyproject.toml](#pyprojecttoml) _(Lines 97-139)_
   1. [Dependency Management](#dependency-management) _(Lines 142-167)_
   1. [Build Backends](#build-backends) _(Lines 170-179)_
   1. [Building and Publishing](#building-and-publishing) _(Lines 182-196)_
   1. [Versioning](#versioning) _(Lines 199-230)_
1. [Quality Phase](#quality-phase) _(Lines 233-235)_
   1. [The Quality Pipeline](#the-quality-pipeline) _(Lines 238-252)_
   1. [Pre-commit Hooks](#pre-commit-hooks) _(Lines 255-282)_
   1. [CI Pipeline](#ci-pipeline) _(Lines 285-325)_
   1. [Quality Gates](#quality-gates) _(Lines 328-339)_
   1. [Automated Releases](#automated-releases) _(Lines 342-372)_
1. [Deployment Phase](#deployment-phase) _(Lines 375-377)_
   1. [Environment Configuration](#environment-configuration) _(Lines 380-399)_
   1. [Containerization](#containerization) _(Lines 402-438)_
   1. [Health Checks](#health-checks) _(Lines 441-462)_
   1. [Monitoring Setup](#monitoring-setup) _(Lines 465-487)_
1. [Stage Checklist](#stage-checklist) _(Lines 490-492)_
   1. [Packaging Checklist](#packaging-checklist) _(Lines 495-503)_
   1. [Quality Checklist](#quality-checklist) _(Lines 506-512)_
   1. [Deployment Checklist](#deployment-checklist) _(Lines 515-521)_
   1. [Quick Verification](#quick-verification) _(Lines 524-539)_
1. [Navigation](#navigation) _(Lines 542-548)_











---

## Stage Overview
<!-- Lines 50-52 -->

The Ship stage prepares code for **distribution and production**. This is where code becomes a product—installable, verifiable, deployable.

### Why Shipping Matters
<!-- Lines 55-57 -->

Code that only runs on your machine isn't useful. Shipping transforms your work into something others can use reliably.

### What Happens Here
<!-- Lines 60-66 -->

This stage has three phases:

1. **Packaging (4.1):** Making code installable
2. **Quality (4.2):** Automated validation via CI
3. **Deployment (4.3):** Getting code to production

### Entry Criteria
<!-- Lines 69-74 -->

You enter this stage when:
- Code is implemented and tested (from Stage 3)
- Ready to share with others or deploy
- Preparing a release

### Exit Criteria
<!-- Lines 77-89 -->

You exit this stage when:
- Package is installable (`pip install mypackage`)
- CI pipeline passes
- Code is deployed (if applicable)
- Version is tagged

**Philosophy connections:**
- [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) — Reproducible builds and deployments
- [0.8 Defensive Design](../LOD_0_philosophy/0.8_defensive_design.md) — Quality gates catch problems early

---

## Packaging Phase
<!-- Lines 92-94 -->

Packaging makes code **installable and distributable**.

### pyproject.toml
<!-- Lines 97-139 -->

Modern Python packaging centers on `pyproject.toml`:

```toml
[project]
name = "myproject"
version = "1.0.0"
description = "A useful project"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.11"
authors = [
    {name = "Your Name", email = "you@example.com"}
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = [
    "httpx>=0.24",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
    "mypy>=1.0",
]

[project.scripts]
myproject = "myproject.cli:main"

[project.urls]
Homepage = "https://github.com/you/myproject"
Documentation = "https://myproject.readthedocs.io"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Dependency Management
<!-- Lines 142-167 -->

**Specify dependencies carefully:**

```toml
dependencies = [
    # Pin major version, allow minor/patch updates
    "httpx>=0.24,<1.0",

    # Exact pin for known-sensitive packages
    "cryptography==41.0.0",

    # Allow any compatible version
    "click>=8.0",
]
```

**Generate lock files for applications:**

```bash
# Using pip-tools
pip-compile pyproject.toml -o requirements.lock

# Using pip freeze
pip freeze > requirements.lock
```

### Build Backends
<!-- Lines 170-179 -->

Choose a build backend:

| Backend | Best For | Notes |
|---------|----------|-------|
| hatchling | Modern projects | Fast, minimal config |
| setuptools | Legacy projects | Most compatible |
| flit | Simple packages | Minimal features |
| poetry-core | Poetry users | Used with poetry |

### Building and Publishing
<!-- Lines 182-196 -->

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Check the package
twine check dist/*

# Upload to PyPI (or TestPyPI first)
twine upload dist/*
```

### Versioning
<!-- Lines 199-230 -->

Use Semantic Versioning:

- **MAJOR.MINOR.PATCH** (e.g., 2.1.3)
- **MAJOR:** Breaking changes
- **MINOR:** New features, backward compatible
- **PATCH:** Bug fixes

Maintain a changelog:

```markdown
# Changelog

## [1.1.0] - 2024-01-15
<!-- Lines 217-216 -->
### Added
<!-- Lines 219-220 -->
- New export feature

### Fixed
<!-- Lines 223-224 -->
- Bug in user lookup

## [1.0.0] - 2024-01-01
<!-- Lines 227-233 -->
- Initial release
```

**Cross-ref:** → [4.1 Packaging](../LOD_2_phases/4.1_packaging.md) for detailed guidance

---

## Quality Phase
<!-- Lines 233-235 -->

Quality automation ensures **consistent code standards**.

### The Quality Pipeline
<!-- Lines 238-252 -->

Every commit should pass:

```
Code Change
    │
    ├── Lint (ruff)
    ├── Format Check (ruff format)
    ├── Type Check (mypy)
    └── Tests (pytest)
    │
    ▼
✓ Ready to Merge
```

### Pre-commit Hooks
<!-- Lines 255-282 -->

Catch issues before commit:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [pydantic]
```

```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

### CI Pipeline
<!-- Lines 285-325 -->

Automate quality checks in CI:

```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          pip install -e ".[dev]"

      - name: Lint
        run: ruff check .

      - name: Format check
        run: ruff format --check .

      - name: Type check
        run: mypy src/

      - name: Test
        run: pytest --cov=myproject
```

### Quality Gates
<!-- Lines 328-339 -->

Set minimum standards:

| Check | Threshold |
|-------|-----------|
| Linting | Zero errors |
| Type checking | Zero errors |
| Test coverage | 80% minimum |
| All tests | Must pass |

Fail CI if thresholds aren't met.

### Automated Releases
<!-- Lines 342-372 -->

Automate releases from tags:

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: python -m build

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          password: ${{ secrets.PYPI_API_TOKEN }}
```

**Cross-ref:** → [4.2 Quality](../LOD_2_phases/4.2_quality.md) for detailed guidance

---

## Deployment Phase
<!-- Lines 375-377 -->

Deployment gets code to production.

### Environment Configuration
<!-- Lines 380-399 -->

Configure for different environments:

```python
# config.py
import os
from enum import Enum

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

ENV = Environment(os.environ.get("ENVIRONMENT", "development"))

# Environment-specific settings
DEBUG = ENV == Environment.DEVELOPMENT
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"
```

### Containerization
<!-- Lines 402-438 -->

Docker for consistent deployment:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (caching)
COPY requirements.lock .
RUN pip install --no-cache-dir -r requirements.lock

# Copy application
COPY src/ ./src/

# Run
CMD ["python", "-m", "myproject"]
```

Multi-stage for smaller images:

```dockerfile
# Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip wheel --no-cache-dir --wheel-dir /wheels .

# Runtime stage
FROM python:3.11-slim
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY src/ ./src/
CMD ["python", "-m", "myproject"]
```

### Health Checks
<!-- Lines 441-462 -->

Verify application health:

```python
# health.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """Liveness probe."""
    return {"status": "healthy"}

@app.get("/ready")
def readiness_check():
    """Readiness probe - checks dependencies."""
    # Check database connection
    # Check required services
    return {"status": "ready"}
```

### Monitoring Setup
<!-- Lines 465-487 -->

Export metrics and logs:

```python
import logging
import structlog

# Structured logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

logger = structlog.get_logger()
logger.info("application_started", version="1.0.0")
```

**Cross-ref:** → [4.3 Deployment](../LOD_2_phases/4.3_deployment.md) for detailed guidance

---

## Stage Checklist
<!-- Lines 490-492 -->

Before leaving the Ship stage, verify:

### Packaging Checklist
<!-- Lines 495-503 -->

- [ ] `pyproject.toml` is complete and valid
- [ ] Dependencies are specified with version constraints
- [ ] Package builds successfully (`python -m build`)
- [ ] Package installs correctly (`pip install dist/*.whl`)
- [ ] Entry points work (if applicable)
- [ ] Version is updated
- [ ] Changelog is updated

### Quality Checklist
<!-- Lines 506-512 -->

- [ ] Pre-commit hooks are configured
- [ ] CI pipeline is set up
- [ ] All quality checks pass (lint, format, type, test)
- [ ] Coverage meets threshold
- [ ] Automated release is configured (if publishing)

### Deployment Checklist
<!-- Lines 515-521 -->

- [ ] Environment configuration is documented
- [ ] Dockerfile works (if containerized)
- [ ] Health endpoints exist
- [ ] Logging is configured
- [ ] Deployment pipeline works

### Quick Verification
<!-- Lines 524-539 -->

```bash
# Build
python -m build
pip install dist/*.whl

# Quality
pre-commit run --all-files

# Docker (if applicable)
docker build -t myproject .
docker run myproject
```

---

## Navigation
<!-- Lines 542-548 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ↑ Philosophy: [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md)
- ← Previous Stage: [3 Build](3_build.md)
- → Next Stage: [5 Operate](5_operate.md)
- ↓ Child Phases: [4.1 Packaging](../LOD_2_phases/4.1_packaging.md), [4.2 Quality](../LOD_2_phases/4.2_quality.md), [4.3 Deployment](../LOD_2_phases/4.3_deployment.md)
