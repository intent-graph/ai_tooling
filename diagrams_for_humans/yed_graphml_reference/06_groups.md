# Group Nodes (Nested Graphs)

Group nodes create collapsible containers that hold child nodes and edges. They use `y:ProxyAutoBoundsNode` wrapping a `y:GroupNode`, plus a nested `<graph>` element. Requires the XML skeleton from [01_xml_skeleton.md](01_xml_skeleton.md).

## Table of Contents

1. [XML Structure](#xml-structure) _(Lines 22-22)_
   1. [Complete Group Node](#complete-group-node) _(Lines 25-78)_
   1. [Minimal Group (Open State Only)](#minimal-group-open-state-only) _(Lines 81-108)_
1. [Key Mechanisms](#key-mechanisms) _(Lines 111-111)_
   1. [foldertype Attribute](#foldertype-attribute) _(Lines 114-124)_
   1. [Realizers and State](#realizers-and-state) _(Lines 127-130)_
   1. [Insets](#insets) _(Lines 133-141)_
   1. [Node IDs](#node-ids) _(Lines 144-148)_
1. [Edges Crossing Group Boundaries](#edges-crossing-group-boundaries) _(Lines 151-169)_


---

## XML Structure
<!-- Lines 22-22 -->

### Complete Group Node
<!-- Lines 25-78 -->

```xml
<node id="grp1" yfiles.foldertype="group">
  <data key="d6">
    <y:ProxyAutoBoundsNode>
      <y:Realizers active="0">
        <!-- Index 0: OPEN state -->
        <y:GroupNode>
          <y:Geometry height="200.0" width="300.0" x="0.0" y="0.0"/>
          <y:Fill color="#F5F5F5" transparent="false"/>
          <y:BorderStyle color="#000000" type="dashed" width="1.0"/>
          <y:NodeLabel alignment="right" autoSizePolicy="node_width"
            fontFamily="Dialog" fontSize="15" fontStyle="bold"
            modelName="internal" modelPosition="t"
            textColor="#000000">Group Label</y:NodeLabel>
          <y:Shape type="roundrectangle"/>
          <y:State closed="false" innerGraphDisplayEnabled="false"/>
          <y:Insets bottom="15" left="15" right="15" top="15"/>
          <y:BorderInsets bottom="0" left="0" right="0" top="0"/>
        </y:GroupNode>

        <!-- Index 1: CLOSED state -->
        <y:GroupNode>
          <y:Geometry height="50.0" width="120.0" x="0.0" y="0.0"/>
          <y:Fill color="#F5F5F5" transparent="false"/>
          <y:BorderStyle color="#000000" type="dashed" width="1.0"/>
          <y:NodeLabel alignment="right" autoSizePolicy="node_width"
            fontFamily="Dialog" fontSize="15" fontStyle="bold"
            modelName="internal" modelPosition="t"
            textColor="#000000">Group Label</y:NodeLabel>
          <y:Shape type="roundrectangle"/>
          <y:State closed="true" innerGraphDisplayEnabled="false"/>
          <y:Insets bottom="15" left="15" right="15" top="15"/>
        </y:GroupNode>
      </y:Realizers>
    </y:ProxyAutoBoundsNode>
  </data>

  <!-- Child nodes live inside a nested graph -->
  <graph edgedefault="directed" id="grp1:">
    <node id="grp1::n0">
      <data key="d6">
        <y:ShapeNode>
          <y:Geometry height="30.0" width="80.0" x="0.0" y="0.0"/>
          <y:Fill color="#99CCFF"/>
          <y:NodeLabel>Child Node</y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>
  </graph>
</node>
```

### Minimal Group (Open State Only)
<!-- Lines 81-108 -->

For generation, you often only need the open state:

```xml
<node id="grp1" yfiles.foldertype="group">
  <data key="d6">
    <y:ProxyAutoBoundsNode>
      <y:Realizers active="0">
        <y:GroupNode>
          <y:Geometry height="200.0" width="300.0" x="0.0" y="0.0"/>
          <y:Fill color="#F5F5F5" transparent="false"/>
          <y:BorderStyle color="#000000" type="dashed" width="1.0"/>
          <y:NodeLabel>My Group</y:NodeLabel>
          <y:Shape type="roundrectangle"/>
          <y:State closed="false"/>
          <y:Insets bottom="15" left="15" right="15" top="15"/>
        </y:GroupNode>
      </y:Realizers>
    </y:ProxyAutoBoundsNode>
  </data>
  <graph edgedefault="directed" id="grp1:">
    <!-- child nodes here -->
  </graph>
</node>
```

---

## Key Mechanisms
<!-- Lines 111-111 -->

### foldertype Attribute
<!-- Lines 114-124 -->

The `yfiles.foldertype` attribute on `<node>` controls group behavior:

| Value | Behavior |
| ----- | -------- |
| `group` | Expandable/collapsible container (default for groups) |
| `folder` | Always collapsed |
| `leaf` | Normal node (default when attribute is absent) |

Without `yfiles.foldertype="group"`, a `<node>` with a nested `<graph>` does not behave as a collapsible group.

### Realizers and State
<!-- Lines 127-130 -->

- `y:Realizers active="0"` — the `active` attribute is a 0-based index selecting which child realizer is displayed. Index 0 = open, index 1 = closed.
- `y:State closed="false"` — controls whether the group renders as open (children visible) or closed.

### Insets
<!-- Lines 133-141 -->

```xml
<y:Insets bottom="15" left="15" right="15" top="15"/>
<y:BorderInsets bottom="0" left="0" right="0" top="0"/>
```

- `y:Insets` — padding between the group boundary and its child nodes
- `y:BorderInsets` — additional space around the group content area

### Node IDs
<!-- Lines 144-148 -->

Child node IDs must be globally unique. The `::` separator in IDs like `grp1::n0` is a convention, not a requirement — IDs are opaque strings to yEd. But using hierarchical IDs prevents collisions.

---

## Edges Crossing Group Boundaries
<!-- Lines 151-169 -->

Edges can connect any two nodes regardless of group nesting. Reference the full node ID:

```xml
<!-- Edge from top-level node to a node inside a group -->
<edge id="e0" source="n0" target="grp1::n0">
  <data key="d10">
    <y:PolyLineEdge>
      <y:LineStyle color="#000000" type="line" width="1.0"/>
      <y:Arrows source="none" target="standard"/>
      <y:BendStyle smoothed="false"/>
    </y:PolyLineEdge>
  </data>
</edge>
```

Edges crossing group boundaries are placed at the **outermost graph level** (the root `<graph>` element), not inside the nested `<graph>`. Edges between nodes within the same group can go inside that group's `<graph>`.

For edge syntax (arrows, line styles, labels), see [04_edges.md](04_edges.md). For label styling on group headers, see [05_labels.md](05_labels.md).
