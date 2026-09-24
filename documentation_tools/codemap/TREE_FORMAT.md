# Tree Format Specification

The YAML tree is the primary output of `cm.context()`, `cm.expand()`, `cm.collapse()`, `cm.include()`, and `cm.exclude()`. It is **valid YAML** — parseable by any YAML library.

## Structure
<!-- Lines 7-30 -->

```yaml
focus: package.module.Class.method        # full qualified name of focus node

package:  # package  package:1-1          # containment = YAML nesting
  module:  # module  package/module.py:1-50
    Class:  # [FOCUS]  class  class Class  "Docstring."  package/module.py:10-40
      method:  # method  def method(self) -> bool  package/module.py:20-30
        ~calls:
          - package.module.OtherClass
        ~called_by:
          - package.utils.helper_fn
      ~inherits:
        - package.base.BaseClass
      ~inherited_by:
        - package.ext.SubClass

database:  # database  data/app.db:1-1
  users:  # db_table  data/app.db:1-1
    ~columns:
      - id
      - email
```

## Rules
<!-- Lines 33-58 -->

**Nodes** are YAML mapping keys. The key is the **short name** (not the full qualified path — nesting encodes containment). Metadata sits in the `#` comment:

```
{indent}{name}:  # {[FOCUS]}  {kind}  {signature}  {"docstring"}  {path}:{start}-{end}
```

Fields after `kind` appear based on detail level: `NAMES_ONLY` omits signature/docstring, `SIGNATURE` adds signature, `FULL` adds both.

**Edges** use `~`-prefixed YAML keys with list values. The `~` prefix cannot start a Python identifier, so it never collides with a node name. Five keys exist:

| Key | Direction | Meaning |
|-----|-----------|---------|
| `~calls` | outgoing | This node calls the listed targets |
| `~called_by` | incoming | The listed sources call this node |
| `~inherits` | outgoing | This class inherits from the listed bases |
| `~inherited_by` | incoming | The listed subclasses inherit from this class |
| `~columns` | metadata | Column names for `db_table` nodes |

Edge targets/sources are **full qualified names** — copy-pasteable into API calls (`cm.context(...)`, `cm.source(...)`).

**Visibility rules:**
- Outgoing edges (`~calls`, `~inherits`) appear on any visible node
- Incoming edges (`~called_by`, `~inherited_by`) appear only on the **focus subtree** (focus node + its descendants)
- `contains` and `imports` edges are never rendered (containment is structural; imports are plumbing)

## Examples
<!-- Lines 61-66 -->

`cm.context()` output scales with focus depth: a root-package focus shows a top-level skeleton
with no edges, a module-level focus shows its classes and methods with `~calls`/`~called_by`, and
a class-level focus shows `~inherits`/`~inherited_by`. Run the CLI on your own project to see the
shape at each level.

## Worked Example
<!-- Lines 69-77 -->

`examples/self/` holds real output from running the CLI on codemap's own source
(`src/codemap/`):

- `context_codemap_build.yaml` — `codemap context src codemap.api.CodeMap.build`, a
  method-level focus showing signature, docstring, and `~calls`/`~called_by` edges across modules.
- `codemap_self.graphml` — `codemap export-yed src -o ...`, the same codebase as a yEd graph.

Regenerate both with `examples/self/generate.sh` (run from this folder).
