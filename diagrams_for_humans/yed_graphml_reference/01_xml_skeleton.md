# XML Skeleton

The required boilerplate that every yEd GraphML file must have. Without this structure, yEd either rejects the file or silently ignores all visual properties.

## Table of Contents

1. [Namespaces](#namespaces) _(Lines 20-48)_
1. [Key Declarations](#key-declarations) _(Lines 51-53)_
   1. [Required Keys](#required-keys) _(Lines 56-66)_
   1. [Optional Keys](#optional-keys) _(Lines 69-82)_
   1. [How Keys Connect to Data](#how-keys-connect-to-data) _(Lines 85-98)_
1. [Complete Boilerplate](#complete-boilerplate) _(Lines 101-130)_
1. [Related Modules](#related-modules) _(Lines 133-136)_


---

## Namespaces
<!-- Lines 20-48 -->

The `<graphml>` root element must declare these namespaces. The `y:` namespace is the critical one — all rendered visual elements live there.

```xml
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"
         xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java"
         xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0"
         xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:y="http://www.yworks.com/xml/graphml"
         xmlns:yed="http://www.yworks.com/xml/yed/3"
         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns
           http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
```

| Prefix | URI | Purpose |
| ------ | --- | ------- |
| _(default)_ | `http://graphml.graphdrawing.org/xmlns` | Core GraphML standard |
| `y:` | `http://www.yworks.com/xml/graphml` | All visual elements — shapes, labels, edges |
| `yed:` | `http://www.yworks.com/xml/yed/3` | yEd 3.x extensions |
| `xsi:` | `http://www.w3.org/2001/XMLSchema-instance` | Schema validation |
| `java:` | `http://www.yworks.com/xml/yfiles-common/1.0/java` | Java type serialization (for StyleProperties) |
| `sys:` | `http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0` | Primitive type markup |
| `x:` | `http://www.yworks.com/xml/yfiles-common/markup/2.0` | Common markup |

Without `y:`, yEd loads the graph topology but renders every node as a tiny default box with no label or color.

---

## Key Declarations
<!-- Lines 51-53 -->

Key declarations bridge GraphML `<data>` elements to yFiles visual realizers. They go between the opening `<graphml>` tag and the `<graph>` element.

### Required Keys
<!-- Lines 56-66 -->

These two are mandatory. Without them, yEd silently ignores all visual data.

```xml
<key for="node" id="d6" yfiles.type="nodegraphics"/>
<key for="edge" id="d10" yfiles.type="edgegraphics"/>
```

- The `id` values (`d6`, `d10`) are arbitrary strings — they just must match what you reference in `<data key="...">` on nodes and edges.
- The `yfiles.type` attribute is what tells yEd to parse the child XML as visual realizer data.

### Optional Keys
<!-- Lines 69-82 -->

Useful for metadata, descriptions, and port graphics. These are NOT displayed but are accessible via yEd's Properties panel.

```xml
<key attr.name="Description" attr.type="string" for="graph" id="d0"/>
<key for="port" id="d1" yfiles.type="portgraphics"/>
<key for="port" id="d2" yfiles.type="portgeometry"/>
<key for="port" id="d3" yfiles.type="portuserdata"/>
<key attr.name="url" attr.type="string" for="node" id="d4"/>
<key attr.name="description" attr.type="string" for="node" id="d5"/>
<key attr.name="url" attr.type="string" for="edge" id="d8"/>
<key attr.name="description" attr.type="string" for="edge" id="d9"/>
```

### How Keys Connect to Data
<!-- Lines 85-98 -->

```
<key for="node" id="d6" yfiles.type="nodegraphics"/>
                  ^^                                     <-- declares the key ID
                  ||
<node id="n0">    ||
  <data key="d6"> ^^  <-- references that same key ID
    <y:ShapeNode>...</y:ShapeNode>   <-- yEd parses this because yfiles.type="nodegraphics"
  </data>
</node>
```

---

## Complete Boilerplate
<!-- Lines 101-130 -->

Copy this as the starting point for any yEd GraphML file. Replace the `<!-- nodes -->` and `<!-- edges -->` comments with actual content.

```xml
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

  <graph edgedefault="directed" id="G">
    <!-- nodes -->
    <!-- edges -->
  </graph>

</graphml>
```

The `edgedefault` attribute controls whether edges without explicit direction are treated as `"directed"` or `"undirected"`. Most diagrams use `"directed"`.

---

## Related Modules
<!-- Lines 133-136 -->

- **Next step — add nodes**: [02_node_shapenode.md](02_node_shapenode.md) (basic shapes) or [03_node_genericnode.md](03_node_genericnode.md) (flowchart / modern / BPMN)
- **Next step — add edges**: [04_edges.md](04_edges.md)
- **Common mistakes with keys/namespaces**: [07_pitfalls.md](07_pitfalls.md#2-wrong-or-missing-key-declarations)
