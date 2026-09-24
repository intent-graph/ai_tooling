"""Export CodeGraph to yEd-compatible GraphML.

Uses yWorks XML extensions (y:ShapeNode, y:PolyLineEdge,
y:ProxyAutoBoundsNode) so yEd renders proper colors, shapes,
labels, collapsible groups, and edge arrows.

After opening in yEd:
  1. Layout > Hierarchical (or Organic) to auto-arrange
  2. Tools > Fit Node to Label to auto-size

Node styling by kind:
  - package  → collapsible group, light indigo
  - module   → collapsible group, light blue
  - class    → amber rectangle
  - function → green rounded rectangle
  - method   → teal rounded rectangle

Edge styling by kind:
  - contains  → grey dashed (hidden — expressed via group nesting)
  - calls     → blue solid
  - imports   → purple dotted
  - inherits  → red solid, hollow arrowhead
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from codemap.graph import CodeGraph, CodeNode

# -- Visual style tables ------------------------------------------------------

_NODE_STYLE: dict[str, dict[str, str]] = {
    "package":  {"fill": "#E8EAF6", "border": "#5C6BC0", "shape": "roundrectangle"},
    "module":   {"fill": "#E3F2FD", "border": "#1E88E5", "shape": "roundrectangle"},
    "class":    {"fill": "#FFF8E1", "border": "#FFA000", "shape": "rectangle"},
    "function": {"fill": "#E8F5E9", "border": "#43A047", "shape": "roundrectangle"},
    "method":   {"fill": "#E0F2F1", "border": "#00897B", "shape": "roundrectangle"},
    "database": {"fill": "#F3E5F5", "border": "#8E24AA", "shape": "roundrectangle"},
    "db_schema": {"fill": "#EDE7F6", "border": "#5E35B1", "shape": "roundrectangle"},
    "db_table": {"fill": "#FCE4EC", "border": "#D81B60", "shape": "roundrectangle"},
}

_EDGE_STYLE: dict[str, dict[str, str]] = {
    "contains": {"color": "#BDBDBD", "type": "dashed", "width": "1.0", "arrow": "delta"},
    "calls":    {"color": "#1565C0", "type": "line",   "width": "1.5", "arrow": "standard"},
    "imports":  {"color": "#7B1FA2", "type": "dotted", "width": "1.0", "arrow": "standard"},
    "inherits": {"color": "#C62828", "type": "line",   "width": "2.0", "arrow": "white_delta"},
}

_GRAPHML_HEADER = """\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java"
         xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0"
         xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:y="http://www.yworks.com/xml/graphml"
         xmlns:yed="http://www.yworks.com/xml/yed/3"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
           http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">

  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <key attr.name="depth" attr.type="int" for="node" id="d_depth"/>
  <key attr.name="kind" attr.type="string" for="node" id="d_kind"/>
  <key attr.name="qualified_name" attr.type="string" for="node" id="d_qname"/>

  <graph edgedefault="directed" id="G">
"""

_GRAPHML_FOOTER = """\
  </graph>

</graphml>"""


# -- Public API ---------------------------------------------------------------


def export_graphml(
    graph: CodeGraph,
    output_path: str | Path,
    *,
    flat: bool = False,
) -> Path:
    """Export a CodeGraph to yEd-compatible GraphML.

    When flat=False (default), the containment hierarchy is expressed as
    nested group nodes (collapsible in yEd) and CONTAINS edges are omitted.

    When flat=True, every node is a plain shape node at the top level.
    CONTAINS edges are still omitted — use the layout algorithms in yEd
    to discover structure.

    Returns the Path of the written file.
    """
    output = Path(output_path)
    display_labels = _build_display_labels(graph)

    if flat:
        node_xml = "\n".join(
            _leaf_node_xml(
                node,
                _node_depth(node, graph),
                display_labels[node.qualified_name],
            )
            for node in sorted(
                graph.nodes.values(), key=lambda n: n.qualified_name
            )
        )
    else:
        children_map = _build_children_map(graph)
        group_qnames = _find_groups(graph, children_map)
        top_level = _find_top_level(graph, children_map)
        node_xml = "\n".join(
            _build_node_tree(
                node,
                graph,
                children_map,
                group_qnames,
                display_labels,
            )
            for node in top_level
        )

    node_qnames = set(graph.nodes.keys())
    edge_parts: list[str] = []
    for edge in graph.edges:
        if edge.kind.value == "contains" and not flat:
            continue  # grouped mode expresses containment via nesting
        if edge.source not in node_qnames or edge.target not in node_qnames:
            continue
        edge_parts.append(
            _edge_xml(len(edge_parts), edge.source, edge.target, edge.kind.value)
        )
    edge_xml = "\n".join(edge_parts)

    graphml = _GRAPHML_HEADER + node_xml + "\n" + edge_xml + "\n" + _GRAPHML_FOOTER
    output.write_text(graphml, encoding="utf-8")
    return output


# -- Node XML generators -----------------------------------------------------


def _build_node_tree(
    node: CodeNode,
    graph: CodeGraph,
    children_map: dict[str | None, list[CodeNode]],
    group_qnames: set[str],
    display_labels: dict[str, str],
) -> str:
    """Recursively generate XML for a node and its children."""
    depth = _node_depth(node, graph)
    if node.qualified_name in group_qnames:
        children = children_map.get(node.qualified_name, [])
        children_xml = "\n".join(
            _build_node_tree(child, graph, children_map, group_qnames, display_labels)
            for child in children
        )
        return _group_node_xml(node, children_xml, depth, display_labels[node.qualified_name])
    return _leaf_node_xml(node, depth, display_labels[node.qualified_name])


def _leaf_node_xml(node: CodeNode, depth: int = 0, label_text: str | None = None) -> str:
    style = _NODE_STYLE.get(node.kind.value, _NODE_STYLE["function"])
    label = escape(label_text if label_text is not None else node.name)
    nid = _safe_id(node.qualified_name)
    return (
        f'<node id="{nid}">\n'
        f'  <data key="d_depth">{depth}</data>\n'
        f'  <data key="d_kind">{node.kind.value}</data>\n'
        f'  <data key="d_qname">{escape(node.qualified_name)}</data>\n'
        f'  <data key="d6">\n'
        f'    <y:ShapeNode>\n'
        f'      <y:Geometry height="30.0" width="120.0" x="0.0" y="0.0"/>\n'
        f'      <y:Fill color="{style["fill"]}" transparent="false"/>\n'
        f'      <y:BorderStyle color="{style["border"]}" type="line" width="1.0"/>\n'
        f'      <y:NodeLabel alignment="center" autoSizePolicy="content"\n'
        f'        fontFamily="Dialog" fontSize="12" fontStyle="plain"\n'
        f'        hasBackgroundColor="false" hasLineColor="false"\n'
        f'        modelName="internal" modelPosition="c"\n'
        f'        textColor="#333333">{label}</y:NodeLabel>\n'
        f'      <y:Shape type="{style["shape"]}"/>\n'
        f'    </y:ShapeNode>\n'
        f'  </data>\n'
        f'</node>'
    )


def _group_node_xml(
    node: CodeNode,
    children_xml: str,
    depth: int = 0,
    label_text: str | None = None,
) -> str:
    style = _NODE_STYLE.get(node.kind.value, _NODE_STYLE["function"])
    label = escape(label_text if label_text is not None else node.name)
    nid = _safe_id(node.qualified_name)
    return (
        f'<node id="{nid}" yfiles.foldertype="group">\n'
        f'  <data key="d_depth">{depth}</data>\n'
        f'  <data key="d_kind">{node.kind.value}</data>\n'
        f'  <data key="d_qname">{escape(node.qualified_name)}</data>\n'
        f'  <data key="d6">\n'
        f'    <y:ProxyAutoBoundsNode>\n'
        f'      <y:Realizers active="0">\n'
        f'        <y:GroupNode>\n'
        f'          <y:Geometry height="100.0" width="200.0" x="0.0" y="0.0"/>\n'
        f'          <y:Fill color="{style["fill"]}" transparent="false"/>\n'
        f'          <y:BorderStyle color="{style["border"]}" type="dashed" width="1.5"/>\n'
        f'          <y:NodeLabel alignment="right" autoSizePolicy="node_width"\n'
        f'            fontFamily="Dialog" fontSize="13" fontStyle="bold"\n'
        f'            modelName="internal" modelPosition="t"\n'
        f'            textColor="#333333">{label}</y:NodeLabel>\n'
        f'          <y:Shape type="roundrectangle"/>\n'
        f'          <y:State closed="false" innerGraphDisplayEnabled="false"/>\n'
        f'          <y:Insets bottom="15" left="15" right="15" top="15"/>\n'
        f'        </y:GroupNode>\n'
        f'        <y:GroupNode>\n'
        f'          <y:Geometry height="50.0" width="120.0" x="0.0" y="0.0"/>\n'
        f'          <y:Fill color="{style["fill"]}" transparent="false"/>\n'
        f'          <y:BorderStyle color="{style["border"]}" type="dashed" width="1.5"/>\n'
        f'          <y:NodeLabel alignment="right" autoSizePolicy="node_width"\n'
        f'            fontFamily="Dialog" fontSize="13" fontStyle="bold"\n'
        f'            modelName="internal" modelPosition="t"\n'
        f'            textColor="#333333">{label}</y:NodeLabel>\n'
        f'          <y:Shape type="roundrectangle"/>\n'
        f'          <y:State closed="true" innerGraphDisplayEnabled="false"/>\n'
        f'          <y:Insets bottom="5" left="5" right="5" top="5"/>\n'
        f'        </y:GroupNode>\n'
        f'      </y:Realizers>\n'
        f'    </y:ProxyAutoBoundsNode>\n'
        f'  </data>\n'
        f'  <graph edgedefault="directed" id="{nid}:">\n'
        f'{children_xml}\n'
        f'  </graph>\n'
        f'</node>'
    )


# -- Edge XML generator -------------------------------------------------------


def _edge_xml(eid: int, source_qname: str, target_qname: str, kind: str) -> str:
    style = _EDGE_STYLE.get(kind, _EDGE_STYLE["calls"])
    sid = _safe_id(source_qname)
    tid = _safe_id(target_qname)
    return (
        f'<edge id="e{eid}" source="{sid}" target="{tid}">\n'
        f'  <data key="d10">\n'
        f'    <y:PolyLineEdge>\n'
        f'      <y:LineStyle color="{style["color"]}" type="{style["type"]}" '
        f'width="{style["width"]}"/>\n'
        f'      <y:Arrows source="none" target="{style["arrow"]}"/>\n'
        f'      <y:BendStyle smoothed="true"/>\n'
        f'    </y:PolyLineEdge>\n'
        f'  </data>\n'
        f'</edge>'
    )


# -- Internal helpers ----------------------------------------------------------


def _safe_id(qname: str) -> str:
    """Convert a qualified name to a valid XML ID."""
    return qname.replace(".", "__")


def _build_display_labels(graph: CodeGraph) -> dict[str, str]:
    """Build yEd labels; disambiguate duplicate short names with qnames."""
    name_counts: dict[str, int] = {}
    for node in graph.nodes.values():
        name_counts[node.name] = name_counts.get(node.name, 0) + 1

    labels: dict[str, str] = {}
    for node in graph.nodes.values():
        if name_counts[node.name] > 1:
            labels[node.qualified_name] = node.qualified_name
        else:
            labels[node.qualified_name] = node.name
    return labels


def _node_depth(node: CodeNode, graph: CodeGraph) -> int:
    """Count hops from root to this node in the containment hierarchy."""
    return len(graph.ancestors_of(node.qualified_name))


def _build_children_map(graph: CodeGraph) -> dict[str | None, list[CodeNode]]:
    """Map each parent qname to its sorted children."""
    children: dict[str | None, list[CodeNode]] = {}
    for node in graph.nodes.values():
        parent = node.parent
        if parent not in children:
            children[parent] = []
        children[parent].append(node)
    for k in children:
        children[k].sort(key=lambda n: n.qualified_name)
    return children


def _find_groups(
    graph: CodeGraph, children_map: dict[str | None, list[CodeNode]]
) -> set[str]:
    """Nodes that have children and exist in the graph → rendered as groups."""
    return (set(children_map.keys()) - {None}) & set(graph.nodes.keys())


def _find_top_level(
    graph: CodeGraph, children_map: dict[str | None, list[CodeNode]]
) -> list[CodeNode]:
    """Nodes with no parent, or whose parent doesn't exist in the graph."""
    top = children_map.get(None, [])
    orphans = [
        n for n in graph.nodes.values()
        if n.parent is not None and n.parent not in graph.nodes
    ]
    return sorted(set(top + orphans), key=lambda n: n.qualified_name)
