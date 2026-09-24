# Graph Visualizer

Given a structured description of a graph, generates a valid yEd GraphML file for visual inspection.

## Table of Contents

1. [Quick Start Template](#quick-start-template) _(Lines 20-69)_
1. [Module Index](#module-index) _(Lines 72-84)_
1. [Agent Instructions](#agent-instructions) _(Lines 87-89)_
   1. [Decision Tree: Which Node Type?](#decision-tree-which-node-type) _(Lines 92-108)_
   1. [Generation Rules](#generation-rules) _(Lines 111-120)_
   1. [Validation Checklist](#validation-checklist) _(Lines 123-137)_
1. [Sub-Agent](#sub-agent) _(Lines 140-151)_


---

## Quick Start Template
<!-- Lines 20-69 -->

Minimal valid yEd file with one styled node and one directed edge. Copy this skeleton, then consult individual modules for customization.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:y="http://www.yworks.com/xml/graphml"
         xmlns:yed="http://www.yworks.com/xml/yed/3"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
           http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">

  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>

  <graph edgedefault="directed" id="G">

    <node id="n0">
      <data key="d6">
        <y:ShapeNode>
          <y:Geometry height="40.0" width="120.0" x="0.0" y="0.0"/>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content"
            fontFamily="Dialog" fontSize="12" fontStyle="plain"
            textColor="#000000" modelName="internal"
            modelPosition="c">Start</y:NodeLabel>
          <y:Shape type="roundrectangle"/>
        </y:ShapeNode>
      </data>
    </node>

    <edge id="e0" source="n0" target="n0">
      <data key="d10">
        <y:PolyLineEdge>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>

  </graph>
</graphml>
```

After opening in yEd, run `Layout > Hierarchical` (or any layout algorithm) to arrange nodes, then `Tools > Fit Node to Label` to auto-size.

---

## Module Index
<!-- Lines 72-84 -->

| Module | ~Lines | Topics | When to Read |
|--------|--------|--------|--------------|
| [01. XML Skeleton](yed_graphml_reference/01_xml_skeleton.md) | 120 | Namespaces, key declarations, file boilerplate | Every time (required structure) |
| [02. ShapeNode](yed_graphml_reference/02_node_shapenode.md) | 150 | Basic shapes: rectangle, ellipse, diamond, etc. | Simple geometric nodes |
| [03. GenericNode](yed_graphml_reference/03_node_genericnode.md) | 250 | Flowchart (28), Modern (8), ER, BPMN shapes | Flowchart diagrams, styled nodes |
| [04. Edges](yed_graphml_reference/04_edges.md) | 170 | PolyLineEdge, arrows, line styles, bend points | Any edge styling |
| [05. Labels](yed_graphml_reference/05_labels.md) | 130 | NodeLabel + EdgeLabel: fonts, placement, sizing | Text display control |
| [06. Groups](yed_graphml_reference/06_groups.md) | 130 | Nested graphs, collapsible groups | Hierarchical grouping |
| [07. Pitfalls](yed_graphml_reference/07_pitfalls.md) | 120 | Common mistakes, displayed-vs-metadata table | Debugging / validation |

---

## Agent Instructions
<!-- Lines 87-89 -->

These instructions are for a sub-agent generating yEd GraphML files programmatically.

### Decision Tree: Which Node Type?
<!-- Lines 92-108 -->

```
Need a node shape?
  |
  +-- Basic geometry (rectangle, ellipse, diamond, triangle)?
  |     --> y:ShapeNode  (see 02_node_shapenode.md)
  |
  +-- Flowchart symbol (process, decision, database, document)?
  |     --> y:GenericNode configuration="com.yworks.flowchart.*"  (see 03_node_genericnode.md)
  |
  +-- Modern/glossy look (bevel, shiny plate)?
  |     --> y:GenericNode configuration="BevelNode*" / "ShinyPlateNode*"  (see 03_node_genericnode.md)
  |
  +-- Collapsible container with children?
        --> y:ProxyAutoBoundsNode + nested <graph>  (see 06_groups.md)
```

### Generation Rules
<!-- Lines 111-120 -->

1. **Always include** the two required `<key>` declarations (`nodegraphics` + `edgegraphics`) — see [01_xml_skeleton.md](yed_graphml_reference/01_xml_skeleton.md)
2. **Every node must have** a `<data key="d6">` block with either `y:ShapeNode` or `y:GenericNode` — bare `<node>` elements render as invisible dots
3. **Every edge must have** a `<data key="d10">` block with `y:PolyLineEdge` — bare `<edge>` elements render as invisible lines
4. **Labels go inside the visual realizer** as `y:NodeLabel` / `y:EdgeLabel` — standard GraphML `<data>` attributes are metadata only and are NOT displayed
5. **Set positions to (0,0)** unless you compute a layout — the user will run auto-layout in yEd
6. **Use `autoSizePolicy="content"`** on labels so yEd can size nodes to fit text
7. **Node IDs must be unique** across the entire file, including inside nested group graphs
8. **All `y:` elements require the namespace prefix** — `<ShapeNode>` without `y:` is silently ignored

### Validation Checklist
<!-- Lines 123-137 -->

Before emitting a GraphML file, verify:

- [ ] XML declaration and all required namespaces present — see [01_xml_skeleton.md](yed_graphml_reference/01_xml_skeleton.md)
- [ ] `<key>` for `nodegraphics` and `edgegraphics` declared — see [01_xml_skeleton.md](yed_graphml_reference/01_xml_skeleton.md#key-declarations)
- [ ] Every `<node>` has a `<data key="...">` child with a visual realizer — see [02_node_shapenode.md](yed_graphml_reference/02_node_shapenode.md) or [03_node_genericnode.md](yed_graphml_reference/03_node_genericnode.md)
- [ ] Every `<edge>` has a `<data key="...">` child with `y:PolyLineEdge` — see [04_edges.md](yed_graphml_reference/04_edges.md)
- [ ] All `source`/`target` attributes on edges reference existing node IDs
- [ ] Group nodes have `yfiles.foldertype="group"` and a nested `<graph>` — see [06_groups.md](yed_graphml_reference/06_groups.md)
- [ ] No duplicate node IDs

For common mistakes and debugging, see [07_pitfalls.md](yed_graphml_reference/07_pitfalls.md).

---

## Sub-Agent
<!-- Lines 140-151 -->

The **Diagram Agent** automates the workflow above. Given a graph description (YAML, JSON, natural language, or minimal topology like `A -> B`), it reads the relevant reference modules, selects the right node realizers, generates valid XML, validates it, and writes a `.graphml` file.

**Agent file:** [`.claude/agents/diagram-agent.md`](../.claude/agents/diagram-agent.md)

**Invocation:**
```
Task(subagent_type="diagram-agent", description="Diagram Agent: create yEd file",
     prompt="Generate a .graphml file from this graph: [description]. Output path: [path]")
```

**Post-generation:** Open the file in yEd, run `Layout > Hierarchical`, then `Tools > Fit Node to Label`.
