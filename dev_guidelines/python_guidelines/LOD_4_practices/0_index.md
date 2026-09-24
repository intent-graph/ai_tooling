# 0 Practices Index

> Specific patterns and how-to guides organized by parent domain — short, actionable files.

## Table of Contents

1. [Overview](#overview) _(Lines 28-37)_
1. [Practice Index by Domain](#practice-index-by-domain) _(Lines 40-40)_
   1. [1.1 Requirements Domains](#11-requirements-domains) _(Lines 43-52)_
   1. [1.2 Design Domains](#12-design-domains) _(Lines 55-73)_
   1. [2.1 Environment Domains](#21-environment-domains) _(Lines 76-84)_
   1. [2.2 Project Structure Domains](#22-project-structure-domains) _(Lines 87-98)_
   1. [3.1 Implementation Domains](#31-implementation-domains) _(Lines 101-135)_
   1. [3.2 Testing Domains](#32-testing-domains) _(Lines 138-151)_
   1. [3.3 Documentation Domains](#33-documentation-domains) _(Lines 154-161)_
   1. [4.x Ship Domains](#4x-ship-domains) _(Lines 164-180)_
   1. [5.x Operate Domains](#5x-operate-domains) _(Lines 183-207)_
   1. [6.x Evolve Domains](#6x-evolve-domains) _(Lines 210-220)_
1. [Navigation](#navigation) _(Lines 223-227)_




---

## Overview
<!-- Lines 28-37 -->

LOD_4 contains **95 practice files** — short, actionable pattern guides. Each is a child of a LOD_3 domain and expands on a specific technique or tool.

**When to Use LOD_4:**
- You need a concrete how-to for a specific pattern (e.g. "how to use dataclasses")
- LOD_3 gave the rules but you need step-by-step guidance
- You want to drill to LOD_5 for edge cases

---

## Practice Index by Domain
<!-- Lines 40-40 -->

### 1.1 Requirements Domains
<!-- Lines 43-52 -->

| Practice | File | Topic |
|----------|------|-------|
| 1.1.1.1 | [1.1.1.1_problem_statement.md](1.1.1.1_problem_statement.md) | Problem Statement |
| 1.1.1.2 | [1.1.1.2_stakeholder_analysis.md](1.1.1.2_stakeholder_analysis.md) | Stakeholder Analysis |
| 1.1.2.1 | [1.1.2.1_capability_tree.md](1.1.2.1_capability_tree.md) | Capability Tree |
| 1.1.2.2 | [1.1.2.2_flow_mapping.md](1.1.2.2_flow_mapping.md) | Flow Mapping |
| 1.1.3.1 | [1.1.3.1_mvp_definition.md](1.1.3.1_mvp_definition.md) | MVP Definition |
| 1.1.4.1 | [1.1.4.1_acceptance_criteria.md](1.1.4.1_acceptance_criteria.md) | Acceptance Criteria |

### 1.2 Design Domains
<!-- Lines 55-73 -->

| Practice | File | Topic |
|----------|------|-------|
| 1.2.1.1 | [1.2.1.1_entity_identification.md](1.2.1.1_entity_identification.md) | Entity Identification |
| 1.2.1.2 | [1.2.1.2_validation.md](1.2.1.2_validation.md) | Validation Patterns |
| 1.2.1.3 | [1.2.1.3_relationships.md](1.2.1.3_relationships.md) | Entity Relationships |
| 1.2.1.4 | [1.2.1.4_normalization.md](1.2.1.4_normalization.md) | Data Normalization |
| 1.2.1.5 | [1.2.1.5_type_as_schema.md](1.2.1.5_type_as_schema.md) | Type as Schema |
| 1.2.2.1 | [1.2.2.1_layered.md](1.2.2.1_layered.md) | Layered Architecture |
| 1.2.2.2 | [1.2.2.2_hexagonal.md](1.2.2.2_hexagonal.md) | Hexagonal Architecture |
| 1.2.2.3 | [1.2.2.3_pipeline.md](1.2.2.3_pipeline.md) | Pipeline Architecture |
| 1.2.3.1 | [1.2.3.1_function_signatures.md](1.2.3.1_function_signatures.md) | Function Signatures |
| 1.2.3.2 | [1.2.3.2_protocols.md](1.2.3.2_protocols.md) | Protocols (Structural Subtyping) |
| 1.2.4.1 | [1.2.4.1_mermaid_flows.md](1.2.4.1_mermaid_flows.md) | Mermaid Flow Diagrams |
| 1.2.5.1 | [1.2.5.1_exception_hierarchy.md](1.2.5.1_exception_hierarchy.md) | Exception Hierarchy |
| 1.2.5.2 | [1.2.5.2_error_propagation.md](1.2.5.2_error_propagation.md) | Error Propagation |
| 1.2.6.1 | [1.2.6.1_env_vars.md](1.2.6.1_env_vars.md) | Environment Variables |
| 1.2.6.2 | [1.2.6.2_config_files.md](1.2.6.2_config_files.md) | Config File Patterns |

### 2.1 Environment Domains
<!-- Lines 76-84 -->

| Practice | File | Topic |
|----------|------|-------|
| 2.1.1.1 | [2.1.1.1_pyenv.md](2.1.1.1_pyenv.md) | pyenv Usage |
| 2.1.2.1 | [2.1.2.1_venv.md](2.1.2.1_venv.md) | venv Module |
| 2.1.2.2 | [2.1.2.2_virtualenv.md](2.1.2.2_virtualenv.md) | virtualenv Tool |
| 2.1.3.1 | [2.1.3.1_uv.md](2.1.3.1_uv.md) | uv Tool |
| 2.1.3.2 | [2.1.3.2_pip.md](2.1.3.2_pip.md) | pip Advanced Usage |

### 2.2 Project Structure Domains
<!-- Lines 87-98 -->

| Practice | File | Topic |
|----------|------|-------|
| 2.2.1.1 | [2.2.1.1_src_layout.md](2.2.1.1_src_layout.md) | src Layout |
| 2.2.1.2 | [2.2.1.2_flat_layout.md](2.2.1.2_flat_layout.md) | Flat Layout |
| 2.2.1.3 | [2.2.1.3_monorepo.md](2.2.1.3_monorepo.md) | Monorepo Structure |
| 2.2.2.1 | [2.2.2.1_init_patterns.md](2.2.2.1_init_patterns.md) | \_\_init\_\_.py Patterns |
| 2.2.2.2 | [2.2.2.2_import_structure.md](2.2.2.2_import_structure.md) | Import Structure |
| 2.2.3.1 | [2.2.3.1_pyproject_sections.md](2.2.3.1_pyproject_sections.md) | pyproject.toml Sections |
| 2.2.4.1 | [2.2.4.1_cli_entry.md](2.2.4.1_cli_entry.md) | CLI Entry Points |
| 2.2.4.2 | [2.2.4.2_main_module.md](2.2.4.2_main_module.md) | \_\_main\_\_.py |

### 3.1 Implementation Domains
<!-- Lines 101-135 -->

| Practice | File | Topic |
|----------|------|-------|
| 3.1.1.1 | [3.1.1.1_variable_naming.md](3.1.1.1_variable_naming.md) | Variable Naming |
| 3.1.1.2 | [3.1.1.2_function_naming.md](3.1.1.2_function_naming.md) | Function Naming |
| 3.1.1.3 | [3.1.1.3_class_naming.md](3.1.1.3_class_naming.md) | Class Naming |
| 3.1.1.4 | [3.1.1.4_module_naming.md](3.1.1.4_module_naming.md) | Module Naming |
| 3.1.1.5 | [3.1.1.5_constant_naming.md](3.1.1.5_constant_naming.md) | Constant Naming |
| 3.1.2.1 | [3.1.2.1_basic_types.md](3.1.2.1_basic_types.md) | Basic Type Hints |
| 3.1.2.2 | [3.1.2.2_generics.md](3.1.2.2_generics.md) | Generics |
| 3.1.2.3 | [3.1.2.3_protocols_typing.md](3.1.2.3_protocols_typing.md) | Protocols in Typing |
| 3.1.2.4 | [3.1.2.4_overloads.md](3.1.2.4_overloads.md) | @overload Patterns |
| 3.1.3.1 | [3.1.3.1_parameters.md](3.1.3.1_parameters.md) | Parameter Design |
| 3.1.3.2 | [3.1.3.2_pure_functions.md](3.1.3.2_pure_functions.md) | Pure Functions |
| 3.1.3.3 | [3.1.3.3_return_values.md](3.1.3.3_return_values.md) | Return Value Patterns |
| 3.1.4.1 | [3.1.4.1_loops.md](3.1.4.1_loops.md) | Loop Patterns |
| 3.1.4.2 | [3.1.4.2_comprehensions.md](3.1.4.2_comprehensions.md) | Comprehensions |
| 3.1.4.3 | [3.1.4.3_generators.md](3.1.4.3_generators.md) | Generators |
| 3.1.5.1 | [3.1.5.1_dataclasses.md](3.1.5.1_dataclasses.md) | Dataclasses |
| 3.1.5.2 | [3.1.5.2_inheritance.md](3.1.5.2_inheritance.md) | Inheritance Patterns |
| 3.1.5.3 | [3.1.5.3_composition.md](3.1.5.3_composition.md) | Composition |
| 3.1.5.4 | [3.1.5.4_protocols_impl.md](3.1.5.4_protocols_impl.md) | Protocol Implementation |
| 3.1.6.1 | [3.1.6.1_context_managers.md](3.1.6.1_context_managers.md) | Context Managers |
| 3.1.6.2 | [3.1.6.2_decorators.md](3.1.6.2_decorators.md) | Decorators |
| 3.1.6.3 | [3.1.6.3_eafp_lbyl.md](3.1.6.3_eafp_lbyl.md) | EAFP vs LBYL |
| 3.1.7.1 | [3.1.7.1_try_except.md](3.1.7.1_try_except.md) | try/except Patterns |
| 3.1.7.2 | [3.1.7.2_custom_exceptions.md](3.1.7.2_custom_exceptions.md) | Custom Exceptions |
| 3.1.7.3 | [3.1.7.3_error_messages.md](3.1.7.3_error_messages.md) | Error Messages |
| 3.1.8.1 | [3.1.8.1_json.md](3.1.8.1_json.md) | JSON Handling |
| 3.1.8.2 | [3.1.8.2_yaml_toml.md](3.1.8.2_yaml_toml.md) | YAML & TOML |
| 3.1.8.3 | [3.1.8.3_binary.md](3.1.8.3_binary.md) | Binary Serialization |
| 3.1.9.1 | [3.1.9.1_mutable_defaults.md](3.1.9.1_mutable_defaults.md) | Mutable Default Arguments |
| 3.1.9.2 | [3.1.9.2_late_binding.md](3.1.9.2_late_binding.md) | Late Binding Closures |
| 3.1.9.3 | [3.1.9.3_circular_imports.md](3.1.9.3_circular_imports.md) | Circular Imports |

### 3.2 Testing Domains
<!-- Lines 138-151 -->

| Practice | File | Topic |
|----------|------|-------|
| 3.2.1.1 | [3.2.1.1_test_structure.md](3.2.1.1_test_structure.md) | Test Structure (AAA) |
| 3.2.1.2 | [3.2.1.2_mocking.md](3.2.1.2_mocking.md) | Mocking Patterns |
| 3.2.1.3 | [3.2.1.3_parametrize.md](3.2.1.3_parametrize.md) | Parametrized Tests |
| 3.2.2.1 | [3.2.2.1_database_tests.md](3.2.2.1_database_tests.md) | Database Testing |
| 3.2.2.2 | [3.2.2.2_api_tests.md](3.2.2.2_api_tests.md) | API Testing |
| 3.2.3.1 | [3.2.3.1_fixture_scopes.md](3.2.3.1_fixture_scopes.md) | Fixture Scopes |
| 3.2.3.2 | [3.2.3.2_factories.md](3.2.3.2_factories.md) | Test Factories |
| 3.2.4.1 | [3.2.4.1_coverage_config.md](3.2.4.1_coverage_config.md) | Coverage Configuration |
| 3.2.5.1 | [3.2.5.1_test_naming.md](3.2.5.1_test_naming.md) | Test Naming |
| 3.2.6.1 | [3.2.6.1_hypothesis.md](3.2.6.1_hypothesis.md) | Hypothesis Library |

### 3.3 Documentation Domains
<!-- Lines 154-161 -->

| Practice | File | Topic |
|----------|------|-------|
| 3.3.3.1 | [3.3.3.1_google_style.md](3.3.3.1_google_style.md) | Google Style Docstrings |
| 3.3.3.2 | [3.3.3.2_numpy_style.md](3.3.3.2_numpy_style.md) | NumPy Style Docstrings |
| 3.3.4.1 | [3.3.4.1_sphinx.md](3.3.4.1_sphinx.md) | Sphinx |
| 3.3.4.2 | [3.3.4.2_mkdocs.md](3.3.4.2_mkdocs.md) | MkDocs |

### 4.x Ship Domains
<!-- Lines 164-180 -->

| Practice | File | Topic |
|----------|------|-------|
| 4.1.2.1 | [4.1.2.1_requirements_txt.md](4.1.2.1_requirements_txt.md) | requirements.txt |
| 4.1.2.2 | [4.1.2.2_lock_files.md](4.1.2.2_lock_files.md) | Lock Files |
| 4.1.2.3 | [4.1.2.3_optional_deps.md](4.1.2.3_optional_deps.md) | Optional Dependencies |
| 4.1.5.1 | [4.1.5.1_semver.md](4.1.5.1_semver.md) | Semantic Versioning |
| 4.1.5.2 | [4.1.5.2_changelog.md](4.1.5.2_changelog.md) | Changelog Maintenance |
| 4.2.1.1 | [4.2.1.1_ruff_config.md](4.2.1.1_ruff_config.md) | Ruff Configuration |
| 4.2.2.1 | [4.2.2.1_black_config.md](4.2.2.1_black_config.md) | Black Configuration |
| 4.2.3.1 | [4.2.3.1_mypy_config.md](4.2.3.1_mypy_config.md) | mypy Configuration |
| 4.2.4.1 | [4.2.4.1_hook_ordering.md](4.2.4.1_hook_ordering.md) | Pre-commit Hook Ordering |
| 4.2.5.1 | [4.2.5.1_github_actions.md](4.2.5.1_github_actions.md) | GitHub Actions |
| 4.3.2.1 | [4.3.2.1_dockerfile.md](4.3.2.1_dockerfile.md) | Dockerfile Patterns |
| 4.3.2.2 | [4.3.2.2_multi_stage.md](4.3.2.2_multi_stage.md) | Multi-stage Builds |
| 4.3.3.1 | [4.3.3.1_prometheus.md](4.3.3.1_prometheus.md) | Prometheus Metrics |

### 5.x Operate Domains
<!-- Lines 183-207 -->

| Practice | File | Topic |
|----------|------|-------|
| 5.1.2.1 | [5.1.2.1_cprofile.md](5.1.2.1_cprofile.md) | cProfile Usage |
| 5.1.2.2 | [5.1.2.2_line_profiler.md](5.1.2.2_line_profiler.md) | line_profiler |
| 5.1.2.3 | [5.1.2.3_memory_profiler.md](5.1.2.3_memory_profiler.md) | memory_profiler |
| 5.1.3.1 | [5.1.3.1_caching.md](5.1.3.1_caching.md) | Caching Patterns |
| 5.1.3.2 | [5.1.3.2_lazy_evaluation.md](5.1.3.2_lazy_evaluation.md) | Lazy Evaluation |
| 5.1.4.1 | [5.1.4.1_threading.md](5.1.4.1_threading.md) | Threading |
| 5.1.4.2 | [5.1.4.2_concurrent_futures.md](5.1.4.2_concurrent_futures.md) | concurrent.futures |
| 5.1.5.1 | [5.1.5.1_multiprocessing.md](5.1.5.1_multiprocessing.md) | multiprocessing |
| 5.1.6.1 | [5.1.6.1_asyncio_basics.md](5.1.6.1_asyncio_basics.md) | asyncio Basics |
| 5.1.6.2 | [5.1.6.2_async_patterns.md](5.1.6.2_async_patterns.md) | Async Patterns |
| 5.1.7.1 | [5.1.7.1_slots.md](5.1.7.1_slots.md) | \_\_slots\_\_ |
| 5.1.7.2 | [5.1.7.2_generators_memory.md](5.1.7.2_generators_memory.md) | Generators for Memory |
| 5.2.2.1 | [5.2.2.1_env_secrets.md](5.2.2.1_env_secrets.md) | Environment Secrets |
| 5.2.2.2 | [5.2.2.2_secret_stores.md](5.2.2.2_secret_stores.md) | Secret Stores |
| 5.2.3.1 | [5.2.3.1_sanitization.md](5.2.3.1_sanitization.md) | Input Sanitization |
| 5.2.4.1 | [5.2.4.1_pip_audit.md](5.2.4.1_pip_audit.md) | pip-audit |
| 5.2.5.1 | [5.2.5.1_injection_prevention.md](5.2.5.1_injection_prevention.md) | Injection Prevention |
| 5.3.1.1 | [5.3.1.1_pdb.md](5.3.1.1_pdb.md) | pdb Debugger |
| 5.3.1.2 | [5.3.1.2_breakpoints.md](5.3.1.2_breakpoints.md) | IDE Breakpoints |
| 5.3.2.1 | [5.3.2.1_logging_config.md](5.3.2.1_logging_config.md) | Logging Configuration |
| 5.3.2.2 | [5.3.2.2_structured_logging.md](5.3.2.2_structured_logging.md) | Structured Logging |

### 6.x Evolve Domains
<!-- Lines 210-220 -->

| Practice | File | Topic |
|----------|------|-------|
| 6.1.1.1 | [6.1.1.1_extract_function.md](6.1.1.1_extract_function.md) | Extract Function |
| 6.1.1.2 | [6.1.1.2_rename_refactoring.md](6.1.1.2_rename_refactoring.md) | Rename Refactoring |
| 6.1.3.1 | [6.1.3.1_deprecation_warnings.md](6.1.3.1_deprecation_warnings.md) | Deprecation Warnings |
| 6.2.1.1 | [6.2.1.1_review_checklist.md](6.2.1.1_review_checklist.md) | Review Checklist |
| 6.2.2.1 | [6.2.2.1_commit_messages.md](6.2.2.1_commit_messages.md) | Commit Messages |
| 6.2.2.2 | [6.2.2.2_branching.md](6.2.2.2_branching.md) | Branching Strategy |
| 6.2.3.1 | [6.2.3.1_adrs.md](6.2.3.1_adrs.md) | Architecture Decision Records |

## Navigation
<!-- Lines 223-227 -->

**Cross-refs:**
- ↑ Parent: [LOD_3 Domains](../LOD_3_domains/0_index.md)
- ↓ Children: [LOD_5 Details](../LOD_5_details/0_index.md) (55 files)
- → Related: [../README.md](../README.md)
