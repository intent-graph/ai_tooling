# 0 Details Index

> Edge cases and deep specifics — the leaf nodes of the knowledge tree. Minimal files, read only when needed.

## Table of Contents

1. [Overview](#overview) _(Lines 23-32)_
1. [Detail Index by Parent Practice](#detail-index-by-parent-practice) _(Lines 35-35)_
   1. [1.2 Design Details](#12-design-details) _(Lines 38-44)_
   1. [3.1 Implementation Details](#31-implementation-details) _(Lines 47-78)_
   1. [3.2 Testing Details](#32-testing-details) _(Lines 81-87)_
   1. [4.x Ship Details](#4x-ship-details) _(Lines 90-97)_
   1. [5.x Operate Details](#5x-operate-details) _(Lines 100-114)_
1. [Navigation](#navigation) _(Lines 117-120)_




---

## Overview
<!-- Lines 23-32 -->

LOD_5 contains **55 detail files** — the deepest leaves of the knowledge tree. These cover edge cases, tool-specific configurations, and deep specifics that only matter when you're working at that exact level.

**When to Use LOD_5:**
- LOD_4 gave the pattern but you need a specific edge case
- You need tool-specific details (e.g. "how does ParamSpec work exactly?")
- You're debugging a subtle issue (e.g. "mutable defaults fix")

---

## Detail Index by Parent Practice
<!-- Lines 35-35 -->

### 1.2 Design Details
<!-- Lines 38-44 -->

| Detail | File | Topic |
|--------|------|-------|
| 1.2.1.2.1 | [1.2.1.2.1_pydantic.md](1.2.1.2.1_pydantic.md) | Pydantic Patterns |
| 1.2.1.2.2 | [1.2.1.2.2_custom_validators.md](1.2.1.2.2_custom_validators.md) | Custom Validators |
| 1.2.1.2.3 | [1.2.1.2.3_boundaries.md](1.2.1.2.3_boundaries.md) | Validation Boundaries |

### 3.1 Implementation Details
<!-- Lines 47-78 -->

| Detail | File | Topic |
|--------|------|-------|
| 3.1.1.1.1 | [3.1.1.1.1_naming_prefixes.md](3.1.1.1.1_naming_prefixes.md) | Naming Prefixes |
| 3.1.1.1.2 | [3.1.1.1.2_naming_antipatterns.md](3.1.1.1.2_naming_antipatterns.md) | Naming Anti-patterns |
| 3.1.1.1.3 | [3.1.1.1.3_context_names.md](3.1.1.1.3_context_names.md) | Context-Dependent Names |
| 3.1.1.1.4 | [3.1.1.1.4_abbreviations.md](3.1.1.1.4_abbreviations.md) | Abbreviation Policy |
| 3.1.1.2.1 | [3.1.1.2.1_verb_patterns.md](3.1.1.2.1_verb_patterns.md) | Verb Patterns |
| 3.1.2.1.1 | [3.1.2.1.1_optional.md](3.1.2.1.1_optional.md) | Optional Type |
| 3.1.2.1.2 | [3.1.2.1.2_union.md](3.1.2.1.2_union.md) | Union Types |
| 3.1.2.2.1 | [3.1.2.2.1_typevar.md](3.1.2.2.1_typevar.md) | TypeVar |
| 3.1.2.2.2 | [3.1.2.2.2_paramspec.md](3.1.2.2.2_paramspec.md) | ParamSpec |
| 3.1.2.3.1 | [3.1.2.3.1_protocol_examples.md](3.1.2.3.1_protocol_examples.md) | Protocol Examples |
| 3.1.3.1.1 | [3.1.3.1.1_positional_only.md](3.1.3.1.1_positional_only.md) | Positional-Only Params |
| 3.1.3.1.2 | [3.1.3.1.2_keyword_only.md](3.1.3.1.2_keyword_only.md) | Keyword-Only Params |
| 3.1.3.1.3 | [3.1.3.1.3_defaults.md](3.1.3.1.3_defaults.md) | Default Values |
| 3.1.3.2.1 | [3.1.3.2.1_side_effects.md](3.1.3.2.1_side_effects.md) | Identifying Side Effects |
| 3.1.4.2.1 | [3.1.4.2.1_nested_comps.md](3.1.4.2.1_nested_comps.md) | Nested Comprehensions |
| 3.1.4.3.1 | [3.1.4.3.1_yield_from.md](3.1.4.3.1_yield_from.md) | yield from |
| 3.1.5.1.1 | [3.1.5.1.1_slots.md](3.1.5.1.1_slots.md) | \_\_slots\_\_ Detail |
| 3.1.5.1.2 | [3.1.5.1.2_frozen.md](3.1.5.1.2_frozen.md) | Frozen Dataclasses |
| 3.1.5.1.3 | [3.1.5.1.3_field_factories.md](3.1.5.1.3_field_factories.md) | Field Factories |
| 3.1.5.2.1 | [3.1.5.2.1_abc.md](3.1.5.2.1_abc.md) | Abstract Base Classes |
| 3.1.5.2.2 | [3.1.5.2.2_mixin.md](3.1.5.2.2_mixin.md) | Mixin Patterns |
| 3.1.6.1.1 | [3.1.6.1.1_contextlib.md](3.1.6.1.1_contextlib.md) | contextlib Utilities |
| 3.1.6.2.1 | [3.1.6.2.1_functools.md](3.1.6.2.1_functools.md) | functools Decorators |
| 3.1.7.1.1 | [3.1.7.1.1_exception_chaining.md](3.1.7.1.1_exception_chaining.md) | Exception Chaining |
| 3.1.7.1.2 | [3.1.7.1.2_context_exception.md](3.1.7.1.2_context_exception.md) | Exceptions in Context Managers |
| 3.1.7.3.1 | [3.1.7.3.1_message_templates.md](3.1.7.3.1_message_templates.md) | Error Message Templates |
| 3.1.8.1.1 | [3.1.8.1.1_json_encoder.md](3.1.8.1.1_json_encoder.md) | Custom JSON Encoders |
| 3.1.9.1.1 | [3.1.9.1.1_mutable_fix.md](3.1.9.1.1_mutable_fix.md) | Fixing Mutable Defaults |

### 3.2 Testing Details
<!-- Lines 81-87 -->

| Detail | File | Topic |
|--------|------|-------|
| 3.2.1.2.1 | [3.2.1.2.1_mock_examples.md](3.2.1.2.1_mock_examples.md) | Mock Examples |
| 3.2.1.2.2 | [3.2.1.2.2_patch_targets.md](3.2.1.2.2_patch_targets.md) | Patch Targets |
| 3.2.3.1.1 | [3.2.3.1.1_conftest.md](3.2.3.1.1_conftest.md) | conftest.py Patterns |

### 4.x Ship Details
<!-- Lines 90-97 -->

| Detail | File | Topic |
|--------|------|-------|
| 4.2.1.1.1 | [4.2.1.1.1_ruff_rules.md](4.2.1.1.1_ruff_rules.md) | Ruff Rule Selection |
| 4.2.3.1.1 | [4.2.3.1.1_mypy_strictness.md](4.2.3.1.1_mypy_strictness.md) | mypy Strictness Levels |
| 4.3.2.1.1 | [4.3.2.1.1_python_images.md](4.3.2.1.1_python_images.md) | Python Docker Images |
| 4.3.2.1.2 | [4.3.2.1.2_dependency_caching.md](4.3.2.1.2_dependency_caching.md) | Docker Dependency Caching |

### 5.x Operate Details
<!-- Lines 100-114 -->

| Detail | File | Topic |
|--------|------|-------|
| 5.1.4.1.1 | [5.1.4.1.1_gil.md](5.1.4.1.1_gil.md) | The GIL Explained |
| 5.1.4.2.1 | [5.1.4.2.1_executor_patterns.md](5.1.4.2.1_executor_patterns.md) | Executor Patterns |
| 5.1.5.1.1 | [5.1.5.1.1_pool_patterns.md](5.1.5.1.1_pool_patterns.md) | Pool Patterns |
| 5.1.6.1.1 | [5.1.6.1.1_event_loop.md](5.1.6.1.1_event_loop.md) | Event Loop Details |
| 5.1.6.1.2 | [5.1.6.1.2_gather_wait.md](5.1.6.1.2_gather_wait.md) | gather vs wait |
| 5.1.6.2.1 | [5.1.6.2.1_async_context.md](5.1.6.2.1_async_context.md) | Async Context Managers |
| 5.1.6.2.2 | [5.1.6.2.2_async_iterators.md](5.1.6.2.2_async_iterators.md) | Async Iterators |
| 5.2.3.1.1 | [5.2.3.1.1_sql_injection.md](5.2.3.1.1_sql_injection.md) | SQL Injection Prevention |
| 5.2.3.1.2 | [5.2.3.1.2_command_injection.md](5.2.3.1.2_command_injection.md) | Command Injection Prevention |
| 5.2.6.1.1 | [5.2.6.1.1_hashing.md](5.2.6.1.1_hashing.md) | Secure Hashing |
| 5.2.6.1.2 | [5.2.6.1.2_encryption.md](5.2.6.1.2_encryption.md) | Encryption Patterns |

## Navigation
<!-- Lines 117-120 -->

**Cross-refs:**
- ↑ Parent: [LOD_4 Practices](../LOD_4_practices/0_index.md)
- → Related: [../README.md](../README.md)
