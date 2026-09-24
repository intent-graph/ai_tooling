# 5 Operate

> Optimize performance, secure the system, debug issues.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 41-43)_
   1. [Why Operations Matter](#why-operations-matter) _(Lines 46-48)_
   1. [What Happens Here](#what-happens-here) _(Lines 51-57)_
   1. [Entry Criteria](#entry-criteria) _(Lines 60-67)_
   1. [Exit Criteria](#exit-criteria) _(Lines 70-82)_
1. [Performance Phase](#performance-phase) _(Lines 85-87)_
   1. [The Performance Mindset](#the-performance-mindset) _(Lines 90-99)_
   1. [Profiling](#profiling) _(Lines 102-126)_
   1. [Optimization Strategies](#optimization-strategies) _(Lines 129-153)_
   1. [Concurrency and Parallelism](#concurrency-and-parallelism) _(Lines 156-182)_
1. [Security Phase](#security-phase) _(Lines 185-187)_
   1. [The Security Mindset](#the-security-mindset) _(Lines 190-196)_
   1. [Input Validation](#input-validation) _(Lines 199-219)_
   1. [Secrets Management](#secrets-management) _(Lines 222-243)_
   1. [Dependency Security](#dependency-security) _(Lines 246-265)_
   1. [Common Vulnerabilities](#common-vulnerabilities) _(Lines 268-286)_
1. [Debugging Phase](#debugging-phase) _(Lines 289-291)_
   1. [The Debugging Mindset](#the-debugging-mindset) _(Lines 294-300)_
   1. [Debugging Strategies](#debugging-strategies) _(Lines 303-315)_
   1. [Logging](#logging) _(Lines 318-345)_
   1. [Structured Logging](#structured-logging) _(Lines 348-359)_
   1. [Tracing](#tracing) _(Lines 362-379)_
1. [Stage Checklist](#stage-checklist) _(Lines 382-384)_
   1. [Performance Checklist](#performance-checklist) _(Lines 387-393)_
   1. [Security Checklist](#security-checklist) _(Lines 396-402)_
   1. [Debugging Checklist](#debugging-checklist) _(Lines 405-411)_
   1. [Quick Verification](#quick-verification) _(Lines 414-428)_
1. [Navigation](#navigation) _(Lines 431-437)_


---

## Stage Overview
<!-- Lines 41-43 -->

The Operate stage addresses the **runtime concerns** of software: making it fast, keeping it secure, and fixing it when things go wrong. Unlike previous stages that focus on building correctly, this stage focuses on running correctly—under load, under attack, and under pressure.

### Why Operations Matter
<!-- Lines 46-48 -->

Code that works isn't enough. Code that works *well*—quickly, safely, observably—is the goal. Operations concerns are often deferred until problems appear, but proactive attention here prevents crisis-mode debugging later.

### What Happens Here
<!-- Lines 51-57 -->

This stage has three phases:

1. **Performance (5.1):** Making code fast and efficient
2. **Security (5.2):** Protecting code and data from threats
3. **Debugging (5.3):** Finding and fixing problems

### Entry Criteria
<!-- Lines 60-67 -->

You enter this stage when:
- Code is deployed and running (from Stage 4)
- Performance issues are reported or suspected
- Security audit is required
- Production bugs need investigation
- System needs optimization

### Exit Criteria
<!-- Lines 70-82 -->

You exit this stage when:
- Performance meets requirements
- Security posture is acceptable
- Debugging capabilities are in place
- Monitoring shows healthy operation

**Philosophy connections:**
- [0.8 Defensive Design](../LOD_0_philosophy/0.8_defensive_design.md) — Fail-fast, security mindset
- [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md) — Premature optimization avoidance

---

## Performance Phase
<!-- Lines 85-87 -->

Performance is about **making code fast enough**—not maximally fast, but appropriately fast.

### The Performance Mindset
<!-- Lines 90-99 -->

Performance optimization follows a strict protocol:

1. **Define "fast enough"** — What are the requirements?
2. **Measure first** — Profile before optimizing
3. **Optimize bottlenecks** — Focus on what matters
4. **Measure again** — Verify improvement

Optimizing without measuring is guessing. Guessing wastes time and often makes things worse.

### Profiling
<!-- Lines 102-126 -->

Before optimizing, understand where time goes:

```python
# Basic timing
import time
start = time.perf_counter()
result = expensive_operation()
elapsed = time.perf_counter() - start
print(f"Took {elapsed:.3f}s")

# cProfile for detailed analysis
python -m cProfile -s cumtime script.py

# Line profiler for line-by-line analysis
@profile
def my_function():
    ...
```

**Profile types:**
- **CPU profiling:** Where does compute time go?
- **Memory profiling:** Where does memory go?
- **I/O profiling:** What's waiting on external resources?

### Optimization Strategies
<!-- Lines 129-153 -->

Once you've identified bottlenecks:

**Algorithmic improvements:**
- Better data structures (dict vs list for lookups)
- Better algorithms (O(n) vs O(n²))
- Caching computed results

**Python-specific optimizations:**
- List comprehensions over loops
- `__slots__` for memory-heavy classes
- Generator expressions for large sequences
- Built-in functions over custom loops

```python
# Slow: Manual loop
result = []
for item in items:
    if predicate(item):
        result.append(transform(item))

# Fast: Comprehension
result = [transform(item) for item in items if predicate(item)]
```

### Concurrency and Parallelism
<!-- Lines 156-182 -->

**Concurrency** (doing multiple things by switching):
- `asyncio` for I/O-bound tasks
- Useful for network requests, file I/O

**Parallelism** (doing multiple things simultaneously):
- `multiprocessing` for CPU-bound tasks
- Bypasses the GIL

```python
# Async for I/O-bound
async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        return await asyncio.gather(*tasks)

# Multiprocessing for CPU-bound
from multiprocessing import Pool

with Pool(4) as pool:
    results = pool.map(cpu_heavy_function, data)
```

**Cross-ref:** → [5.1 Performance](../LOD_2_phases/5.1_performance.md) for detailed guidance

---

## Security Phase
<!-- Lines 185-187 -->

Security is about **protecting code, data, and users** from threats—both intentional and accidental.

### The Security Mindset
<!-- Lines 190-196 -->

Security isn't a feature; it's a property of the entire system. Assume:
- All input is malicious until validated
- All secrets will leak unless protected
- All dependencies contain vulnerabilities
- All systems will be attacked

### Input Validation
<!-- Lines 199-219 -->

Never trust external input:

```python
from pydantic import BaseModel, EmailStr, constr

class UserInput(BaseModel):
    """Validated user input."""
    email: EmailStr
    username: constr(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')

# Validates or raises
user = UserInput.model_validate(request_json)
```

**Validate at boundaries:**
- API endpoints
- File uploads
- Database queries (use parameterized queries)
- External service responses

### Secrets Management
<!-- Lines 222-243 -->

Never commit secrets:

```python
# Wrong: Hardcoded
API_KEY = "sk-12345abcde"

# Right: Environment variable
import os
API_KEY = os.environ["API_KEY"]

# Better: Secrets manager
from my_secrets import get_secret
API_KEY = get_secret("api-key")
```

**Secrets hygiene:**
- Use `.env` files locally, never commit them
- Use secrets managers in production
- Rotate secrets regularly
- Audit access logs

### Dependency Security
<!-- Lines 246-265 -->

Dependencies are attack vectors:

```bash
# Audit for known vulnerabilities
pip-audit

# Check for outdated packages
pip list --outdated

# Use lock files for reproducibility
pip-compile --generate-hashes
```

**Dependency hygiene:**
- Keep dependencies minimal
- Update regularly
- Pin versions in production
- Review before adding new dependencies

### Common Vulnerabilities
<!-- Lines 268-286 -->

Watch for:
- **SQL Injection:** Use parameterized queries
- **XSS:** Escape output, use template engines
- **Path Traversal:** Validate file paths
- **Command Injection:** Avoid shell commands with user input

```python
# Vulnerable to SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Safe: Parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

**Cross-ref:** → [5.2 Security](../LOD_2_phases/5.2_security.md) for detailed guidance

---

## Debugging Phase
<!-- Lines 289-291 -->

Debugging is the **systematic process of finding and fixing defects**.

### The Debugging Mindset
<!-- Lines 294-300 -->

Debugging is detective work. Good debuggers:
- Form hypotheses and test them
- Isolate variables systematically
- Trust data over intuition
- Document findings

### Debugging Strategies
<!-- Lines 303-315 -->

**Scientific method for bugs:**
1. Reproduce the bug reliably
2. Form a hypothesis about the cause
3. Design an experiment to test it
4. Execute and observe
5. Iterate until root cause found

**Isolation techniques:**
- Binary search (disable half the code)
- Minimal reproduction (smallest failing case)
- Environment comparison (works here, fails there)

### Logging
<!-- Lines 318-345 -->

Effective logging is proactive debugging:

```python
import logging

logger = logging.getLogger(__name__)

def process_order(order_id: str) -> Order:
    logger.info("Processing order", extra={"order_id": order_id})
    try:
        order = fetch_order(order_id)
        logger.debug("Fetched order", extra={"order": order})
        result = validate_and_fulfill(order)
        logger.info("Order processed", extra={"order_id": order_id, "status": "success"})
        return result
    except OrderError as e:
        logger.error("Order failed", extra={"order_id": order_id, "error": str(e)})
        raise
```

**Logging levels:**
- **DEBUG:** Detailed diagnostic information
- **INFO:** Normal operation events
- **WARNING:** Unexpected but handled situations
- **ERROR:** Failures that need attention
- **CRITICAL:** System-level failures

### Structured Logging
<!-- Lines 348-359 -->

In production, use structured logging for searchability:

```python
import structlog

logger = structlog.get_logger()

logger.info("order_processed", order_id=order_id, customer_id=customer_id, total=total)
# Outputs: {"event": "order_processed", "order_id": "123", "customer_id": "456", "total": 99.99}
```

### Tracing
<!-- Lines 362-379 -->

For distributed systems, use tracing to follow requests:

```python
# OpenTelemetry example
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("process_order") as span:
    span.set_attribute("order_id", order_id)
    # ... processing
```

**Cross-ref:** → [5.3 Debugging](../LOD_2_phases/5.3_debugging.md) for detailed guidance

---

## Stage Checklist
<!-- Lines 382-384 -->

Before leaving the Operate stage, verify:

### Performance Checklist
<!-- Lines 387-393 -->

- [ ] Performance requirements are defined
- [ ] Critical paths are profiled
- [ ] Bottlenecks are identified and addressed
- [ ] Async/parallel patterns used where appropriate
- [ ] No premature optimizations

### Security Checklist
<!-- Lines 396-402 -->

- [ ] All inputs are validated
- [ ] No hardcoded secrets
- [ ] Dependencies are audited
- [ ] SQL queries are parameterized
- [ ] Sensitive data is protected

### Debugging Checklist
<!-- Lines 405-411 -->

- [ ] Logging is configured
- [ ] Log levels are appropriate
- [ ] Structured logging in production
- [ ] Tracing is set up (if distributed)
- [ ] Error messages are informative

### Quick Verification
<!-- Lines 414-428 -->

```bash
# Performance
python -m cProfile script.py

# Security
pip-audit
bandit -r src/

# Logging
python -c "import logging; logging.basicConfig(level=logging.DEBUG)"
```

---

## Navigation
<!-- Lines 431-437 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ↑ Philosophy: [0.8 Defensive Design](../LOD_0_philosophy/0.8_defensive_design.md), [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md)
- ← Previous Stage: [4 Ship](4_ship.md)
- → Next Stage: [6 Evolve](6_evolve.md)
- ↓ Child Phases: [5.1 Performance](../LOD_2_phases/5.1_performance.md), [5.2 Security](../LOD_2_phases/5.2_security.md), [5.3 Debugging](../LOD_2_phases/5.3_debugging.md)
