# 7 Specialize

> Application-type-specific guidance.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 32-34)_
   1. [Why Specialization Matters](#why-specialization-matters) _(Lines 37-39)_
   1. [What Happens Here](#what-happens-here) _(Lines 42-46)_
   1. [Entry Criteria](#entry-criteria) _(Lines 49-55)_
   1. [Exit Criteria](#exit-criteria) _(Lines 58-60)_
   1. [Application Types Covered](#application-types-covered) _(Lines 63-75)_
1. [Scenarios Phase](#scenarios-phase) _(Lines 78-80)_
   1. [CLI Applications](#cli-applications) _(Lines 83-119)_
   1. [Web Applications](#web-applications) _(Lines 122-158)_
   1. [Data Pipelines](#data-pipelines) _(Lines 161-211)_
   1. [Libraries](#libraries) _(Lines 214-266)_
   1. [APIs](#apis) _(Lines 269-321)_
   1. [Scientific Computing](#scientific-computing) _(Lines 324-376)_
   1. [Automation Scripts](#automation-scripts) _(Lines 379-435)_
1. [Stage Checklist](#stage-checklist) _(Lines 438-440)_
   1. [General Checklist](#general-checklist) _(Lines 443-449)_
   1. [Per-Type Quick Checks](#per-type-quick-checks) _(Lines 452-462)_
   1. [Red Flags](#red-flags) _(Lines 465-473)_
1. [Navigation](#navigation) _(Lines 476-480)_


---

## Stage Overview
<!-- Lines 32-34 -->

The Specialize stage provides **application-type-specific guidance**. While Stages 1-6 apply universally, this stage addresses the unique patterns, tools, and considerations for different kinds of Python applications.

### Why Specialization Matters
<!-- Lines 37-39 -->

A CLI tool has different concerns than a web API. A data pipeline has different requirements than a scientific computing script. While core principles remain constant, their application varies by context.

### What Happens Here
<!-- Lines 42-46 -->

This stage has one phase with multiple scenarios:

1. **Scenarios (7.1):** Type-specific guidance for common application types

### Entry Criteria
<!-- Lines 49-55 -->

You enter this stage when:
- Building a specific type of application
- Core guidelines need domain-specific interpretation
- Looking for type-specific patterns and tools
- Evaluating framework choices

### Exit Criteria
<!-- Lines 58-60 -->

You apply relevant specializations to your project. This stage is reference material—return when building different application types.

### Application Types Covered
<!-- Lines 63-75 -->

| Type | Use Case |
|------|----------|
| CLI Applications | Command-line tools, scripts |
| Web Applications | Frontend + backend, full-stack |
| Data Pipelines | ETL, data processing |
| Libraries | Reusable packages |
| APIs | REST, GraphQL services |
| Scientific Computing | Research, numerical analysis |
| Automation Scripts | Task automation, DevOps |

---

## Scenarios Phase
<!-- Lines 78-80 -->

Each scenario provides patterns specific to that application type. All scenarios build on the universal guidelines—specialization adds, it doesn't replace.

### CLI Applications
<!-- Lines 83-119 -->

Command-line tools that accept arguments and produce output.

**Key concerns:**
- Argument parsing
- Output formatting (human vs machine)
- Exit codes
- Interactive vs non-interactive modes

**Recommended tools:**
- `click` or `typer` for argument parsing
- `rich` for formatted output
- `python-dotenv` for configuration

**Pattern example:**

```python
import click

@click.command()
@click.argument("filename")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def process(filename: str, verbose: bool) -> None:
    """Process FILENAME and produce output."""
    if verbose:
        click.echo(f"Processing {filename}...")
    # ... processing logic
    click.echo("Done.")

if __name__ == "__main__":
    process()
```

**Cross-ref:** → [7.1.1 CLI Applications](../LOD_3_domains/7.1.1_cli.md) <!-- INVALID: file '../LOD_3_domains/7.1.1_cli.md' not found -->

---

### Web Applications
<!-- Lines 122-158 -->

Full-stack applications with frontend and backend components.

**Key concerns:**
- Request/response cycle
- Template rendering
- Session management
- Static asset handling
- Authentication

**Recommended tools:**
- `Flask` or `Django` for framework
- `Jinja2` for templates
- `SQLAlchemy` for database

**Pattern example:**

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form["data"]
    result = process(data)
    return render_template("result.html", result=result)
```

**Cross-ref:** → [7.1.2 Web Applications](../LOD_3_domains/7.1.2_web.md) <!-- INVALID: file '../LOD_3_domains/7.1.2_web.md' not found -->

---

### Data Pipelines
<!-- Lines 161-211 -->

Extract-Transform-Load workflows and data processing.

**Key concerns:**
- Data validation at boundaries
- Idempotency
- Error handling and retries
- Monitoring and logging
- Batch vs streaming

**Recommended tools:**
- `pandas` for tabular data
- `dbt` for SQL transformations
- `Airflow` or `Prefect` for orchestration
- `Great Expectations` for validation

**Pattern example:**

```python
import pandas as pd
from pydantic import BaseModel

class InputRecord(BaseModel):
    id: int
    value: float

def extract(source: str) -> pd.DataFrame:
    """Extract data from source."""
    return pd.read_csv(source)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations."""
    return df.assign(
        processed_value=df["value"] * 2,
        processed_at=pd.Timestamp.now()
    )

def load(df: pd.DataFrame, target: str) -> None:
    """Load data to target."""
    df.to_parquet(target, index=False)

# Pipeline
df = extract("input.csv")
df = transform(df)
load(df, "output.parquet")
```

**Cross-ref:** → [7.1.3 Data Pipelines](../LOD_3_domains/7.1.3_data_pipelines.md)

---

### Libraries
<!-- Lines 214-266 -->

Reusable packages installed by other projects.

**Key concerns:**
- API design and stability
- Backward compatibility
- Minimal dependencies
- Documentation quality
- Versioning

**Recommended practices:**
- Semantic versioning strictly
- Extensive docstrings
- Type hints throughout
- No unnecessary dependencies

**Pattern example:**

```python
# Public API in __init__.py
from mylib.core import MyClass, my_function
from mylib.errors import MyError

__all__ = ["MyClass", "my_function", "MyError"]
__version__ = "1.2.3"

# Clear, stable public interface
class MyClass:
    """Main class for doing X.

    Example:
        >>> obj = MyClass()
        >>> result = obj.process(data)
    """

    def process(self, data: Input) -> Output:
        """Process data and return result.

        Args:
            data: Input data to process.

        Returns:
            Processed output.

        Raises:
            MyError: If processing fails.
        """
```

**Cross-ref:** → [7.1.4 Libraries](../LOD_3_domains/7.1.4_libraries.md)

---

### APIs
<!-- Lines 269-321 -->

HTTP services providing data and operations.

**Key concerns:**
- Request validation
- Response formatting
- Authentication/authorization
- Rate limiting
- Error responses
- Documentation (OpenAPI)

**Recommended tools:**
- `FastAPI` for modern APIs
- `Pydantic` for validation
- `httpx` for testing

**Pattern example:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items", response_model=ItemResponse)
def create_item(item: Item) -> ItemResponse:
    """Create a new item."""
    # Validation happens automatically via Pydantic
    created = db.create_item(item)
    return ItemResponse(id=created.id, **item.model_dump())

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    """Retrieve an item by ID."""
    item = db.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

**Cross-ref:** → [7.1.5 APIs](../LOD_3_domains/7.1.5_apis.md)

---

### Scientific Computing
<!-- Lines 324-376 -->

Research code, numerical analysis, simulations.

**Key concerns:**
- Numerical precision
- Reproducibility (seeds, versions)
- Performance (vectorization)
- Visualization
- Data provenance

**Recommended tools:**
- `numpy` for numerical computing
- `scipy` for scientific functions
- `matplotlib` for visualization
- `jupyter` for exploration

**Pattern example:**

```python
import numpy as np
from numpy.typing import NDArray

def simulate(
    n_particles: int,
    n_steps: int,
    seed: int = 42
) -> NDArray[np.float64]:
    """Run particle simulation.

    Args:
        n_particles: Number of particles.
        n_steps: Number of time steps.
        seed: Random seed for reproducibility.

    Returns:
        Position array of shape (n_steps, n_particles, 3).
    """
    rng = np.random.default_rng(seed)

    positions = np.zeros((n_steps, n_particles, 3))
    positions[0] = rng.random((n_particles, 3))

    for t in range(1, n_steps):
        # Vectorized update
        positions[t] = positions[t-1] + rng.normal(0, 0.1, (n_particles, 3))

    return positions
```

**Cross-ref:** → [7.1.6 Scientific Computing](../LOD_3_domains/7.1.6_scientific.md) <!-- INVALID: file '../LOD_3_domains/7.1.6_scientific.md' not found -->

---

### Automation Scripts
<!-- Lines 379-435 -->

Task automation, DevOps, system administration.

**Key concerns:**
- Error handling (partial failures)
- Idempotency
- Logging
- Configuration
- Dry-run mode

**Recommended tools:**
- `fabric` or `invoke` for task running
- `paramiko` for SSH
- `pathlib` for file operations

**Pattern example:**

```python
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def backup_files(
    source_dir: Path,
    target_dir: Path,
    dry_run: bool = False
) -> list[Path]:
    """Backup files from source to target.

    Args:
        source_dir: Directory containing files to backup.
        target_dir: Directory to copy files to.
        dry_run: If True, log actions without executing.

    Returns:
        List of backed up files.
    """
    backed_up = []

    for source_file in source_dir.glob("*"):
        target_file = target_dir / source_file.name

        if dry_run:
            logger.info(f"Would copy {source_file} to {target_file}")
        else:
            logger.info(f"Copying {source_file} to {target_file}")
            target_file.write_bytes(source_file.read_bytes())
            backed_up.append(target_file)

    return backed_up
```

**Cross-ref:** → [7.1.7 Automation Scripts](../LOD_3_domains/7.1.7_scripts.md) <!-- INVALID: file '../LOD_3_domains/7.1.7_scripts.md' not found -->

---

## Stage Checklist
<!-- Lines 438-440 -->

When building a specific application type:

### General Checklist
<!-- Lines 443-449 -->

- [ ] Core guidelines (Stages 1-6) are followed
- [ ] Application type is identified
- [ ] Type-specific patterns are applied
- [ ] Appropriate tools are selected
- [ ] Domain-specific concerns are addressed

### Per-Type Quick Checks
<!-- Lines 452-462 -->

| Type | Key Verification |
|------|------------------|
| CLI | Arguments parse correctly, exit codes are meaningful |
| Web | Routes work, templates render, sessions persist |
| Pipeline | Idempotent, monitored, handles failures |
| Library | API is stable, documented, typed |
| API | Validates input, formats output, handles errors |
| Scientific | Reproducible, vectorized, visualizable |
| Scripts | Idempotent, has dry-run, logs clearly |

### Red Flags
<!-- Lines 465-473 -->

Stop and reconsider if:
- **Generic patterns where specific exist** — Don't reinvent wheels
- **Missing type-specific validation** — Each type has unique concerns
- **Wrong tool for the job** — CLI framework for API, etc.
- **Ignoring domain conventions** — Each domain has expectations

---

## Navigation
<!-- Lines 476-480 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ← Previous Stage: [6 Evolve](6_evolve.md)
- ↓ Child Phase: [7.1 Scenarios](../LOD_2_phases/7.1_scenarios.md)
