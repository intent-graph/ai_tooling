# Pitfalls and Validation

Common mistakes when generating yEd GraphML, and a reference for what yEd actually displays versus what it treats as metadata.

## Table of Contents

1. [Common Pitfalls](#common-pitfalls) _(Lines 24-24)_
   1. [1. Missing Visual Realizer](#1-missing-visual-realizer) _(Lines 27-45)_
   1. [2. Wrong or Missing Key Declarations](#2-wrong-or-missing-key-declarations) _(Lines 48-52)_
   1. [3. Labels in Standard GraphML Data (Not Displayed)](#3-labels-in-standard-graphml-data-not-displayed) _(Lines 55-76)_
   1. [4. All Nodes Stacked at Origin](#4-all-nodes-stacked-at-origin) _(Lines 79-83)_
   1. [5. Node Too Small for Label](#5-node-too-small-for-label) _(Lines 86-90)_
   1. [6. Missing `y:` Namespace Prefix](#6-missing-y-namespace-prefix) _(Lines 93-97)_
   1. [7. Group Node Without foldertype](#7-group-node-without-foldertype) _(Lines 100-104)_
   1. [8. Unknown GenericNode Configuration](#8-unknown-genericnode-configuration) _(Lines 107-113)_
1. [Displayed vs Metadata](#displayed-vs-metadata) _(Lines 116-140)_
1. [Debugging Workflow](#debugging-workflow) _(Lines 143-155)_


---

## Common Pitfalls
<!-- Lines 24-24 -->

### 1. Missing Visual Realizer
<!-- Lines 27-45 -->

**Symptom**: Node appears as a tiny default box with no label, no color.

```xml
<!-- WRONG: bare node without visual data -->
<node id="n0"/>

<!-- CORRECT: node with visual realizer -->
<node id="n0">
  <data key="d6">
    <y:ShapeNode>
      <y:Fill color="#FFCC00"/>
      <y:NodeLabel>My Node</y:NodeLabel>
      <y:Shape type="rectangle"/>
    </y:ShapeNode>
  </data>
</node>
```

### 2. Wrong or Missing Key Declarations
<!-- Lines 48-52 -->

**Symptom**: All visual data silently ignored. Every node renders as default.

The `<key>` with `yfiles.type="nodegraphics"` must exist, and its `id` must match the `<data key="...">` on every node. Same for edges with `yfiles.type="edgegraphics"`. See [01_xml_skeleton.md](01_xml_skeleton.md#key-declarations) for the correct declarations.

### 3. Labels in Standard GraphML Data (Not Displayed)
<!-- Lines 55-76 -->

**Symptom**: Nodes have no visible text despite having label data.

```xml
<!-- NOT DISPLAYED -->
<node id="n0">
  <data key="label">My Label</data>
</node>

<!-- DISPLAYED -->
<node id="n0">
  <data key="d6">
    <y:ShapeNode>
      <y:NodeLabel>My Label</y:NodeLabel>
      ...
    </y:ShapeNode>
  </data>
</node>
```

Workaround after import: `Edit > Properties Mapper` in yEd can map a custom data attribute to the visual label. But it's better to generate `y:NodeLabel` directly. See [05_labels.md](05_labels.md) for the full label attribute reference.

### 4. All Nodes Stacked at Origin
<!-- Lines 79-83 -->

**Symptom**: Everything looks like a single node. Nodes are all at (0,0).

Fix: Run `Layout > Hierarchical` (or any algorithm) in yEd after opening.

### 5. Node Too Small for Label
<!-- Lines 86-90 -->

**Symptom**: Text overflows the node boundary.

Fix: Use `autoSizePolicy="content"` on `y:NodeLabel` (see [05_labels.md](05_labels.md#sizing-attributes)), or run `Tools > Fit Node to Label` in yEd.

### 6. Missing `y:` Namespace Prefix
<!-- Lines 93-97 -->

**Symptom**: Nodes render as defaults despite having XML content.

`<ShapeNode>` without the prefix is not in the yWorks namespace. Always use `<y:ShapeNode>`. See [01_xml_skeleton.md](01_xml_skeleton.md#namespaces) for the required namespace declarations.

### 7. Group Node Without foldertype
<!-- Lines 100-104 -->

**Symptom**: A node with a nested `<graph>` doesn't behave as a collapsible group.

Must set `yfiles.foldertype="group"` on the `<node>` element. See [06_groups.md](06_groups.md).

### 8. Unknown GenericNode Configuration
<!-- Lines 107-113 -->

**Symptom**: Shape renders as a plain rectangle instead of the expected flowchart symbol.

yEd falls back to a default shape for unrecognized `configuration` strings. No error. Double-check spelling against the tables in [03_node_genericnode.md](03_node_genericnode.md).

---

## Displayed vs Metadata
<!-- Lines 116-140 -->

| Element | Displayed? | Notes |
| ------- | ---------- | ----- |
| `y:ShapeNode` / `y:GenericNode` children | **YES** | Shape, fill, border all rendered |
| `y:NodeLabel` text content | **YES** | Visible text on the node |
| `y:Geometry` x/y/width/height | **YES** | Position and size |
| `y:Fill` color | **YES** | Background color |
| `y:BorderStyle` | **YES** | Border line |
| `y:Shape` / `configuration` | **YES** | Shape outline |
| `y:StyleProperties` | **YES** | Shadow, orientation, BPMN sub-types |
| `y:PolyLineEdge` children | **YES** | Line, arrows, bends |
| `y:EdgeLabel` text content | **YES** | Text along edge |
| `y:Arrows` source/target | **YES** | Arrowheads |
| `y:LineStyle` | **YES** | Edge line appearance |
| `y:Path` bend points | **YES** | Edge routing |
| `y:BendStyle smoothed` | **YES** | Angular vs curved |
| Standard `<data>` attributes | **NO** | Stored as custom properties, not rendered |
| Node `id` attribute | **NO** | Internal identifier only |
| Edge `id` attribute | **NO** | Internal identifier only |
| `y:UserData` | **NO** | Application state, not rendered |

**Rule of thumb**: If it's inside a `y:` visual realizer element, it's displayed. If it's a standard GraphML `<data>` element with `attr.name`, it's metadata only.

---

## Debugging Workflow
<!-- Lines 143-155 -->

When a generated file doesn't look right in yEd:

1. **Open in yEd** — does it load without errors? If it fails to load, check XML well-formedness.
2. **Check node appearance** — if nodes are default gray boxes, the visual realizer is missing or the key declaration is wrong. See pitfalls 1 and 2.
3. **Check labels** — if nodes have no text, labels are probably in `<data>` instead of `y:NodeLabel`. See pitfall 3.
4. **Check layout** — if everything is stacked, positions are all (0,0). Run `Layout > Hierarchical`.
5. **Check shapes** — if flowchart nodes render as rectangles, the `configuration` string is wrong. See pitfall 8.
6. **Validate programmatically** — parse the XML yourself and check:
   - Every `<node>` has a `<data>` child referencing the nodegraphics key
   - Every `<edge>` has a `<data>` child referencing the edgegraphics key
   - All edge `source`/`target` reference existing node IDs
   - No duplicate node IDs
