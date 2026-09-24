# ShapeNode (Basic Shapes)

`y:ShapeNode` is the simplest node realizer. It renders basic geometric shapes with fill, border, and label. For domain-specific shapes (flowchart, BPMN, ER, modern), see [03_node_genericnode.md](03_node_genericnode.md) instead. Requires the XML skeleton from [01_xml_skeleton.md](01_xml_skeleton.md).

## Table of Contents

1. [XML Structure](#xml-structure) _(Lines 23-23)_
   1. [Complete Example](#complete-example) _(Lines 26-44)_
   1. [Minimal (Still Renders Correctly)](#minimal-still-renders-correctly) _(Lines 47-64)_
1. [Child Elements](#child-elements) _(Lines 67-78)_
   1. [Geometry](#geometry) _(Lines 81-91)_
1. [Shape Types](#shape-types) _(Lines 94-114)_
1. [Fill and Border](#fill-and-border) _(Lines 117-117)_
   1. [Fill](#fill) _(Lines 120-130)_
   1. [Border](#border) _(Lines 133-143)_
   1. [Drop Shadow](#drop-shadow) _(Lines 146-153)_


---

## XML Structure
<!-- Lines 23-23 -->

### Complete Example
<!-- Lines 26-44 -->

```xml
<node id="n0">
  <data key="d6">
    <y:ShapeNode>
      <y:Geometry height="40.0" width="120.0" x="100.0" y="200.0"/>
      <y:Fill color="#FFCC00" color2="#FF9900" transparent="false"/>
      <y:BorderStyle color="#000000" type="line" width="1.0"/>
      <y:NodeLabel alignment="center" autoSizePolicy="content"
                    fontFamily="Dialog" fontSize="13" fontStyle="plain"
                    hasBackgroundColor="false" hasLineColor="false"
                    modelName="internal" modelPosition="c"
                    textColor="#000000" visible="true">My Label</y:NodeLabel>
      <y:Shape type="roundrectangle"/>
    </y:ShapeNode>
  </data>
</node>
```

### Minimal (Still Renders Correctly)
<!-- Lines 47-64 -->

```xml
<node id="n0">
  <data key="d6">
    <y:ShapeNode>
      <y:Geometry height="30.0" width="100.0"/>
      <y:Fill color="#FFCC00"/>
      <y:NodeLabel>My Label</y:NodeLabel>
      <y:Shape type="rectangle"/>
    </y:ShapeNode>
  </data>
</node>
```

When attributes are omitted, yEd uses sensible defaults (black border, centered label, position 0,0).

---

## Child Elements
<!-- Lines 67-78 -->

Elements must appear as children of `<y:ShapeNode>`. Order does not matter.

| Element | Required | What Gets Displayed |
| ------- | -------- | ------------------- |
| `y:Geometry` | No (defaults 0,0,30,30) | Position (x,y) and size (width,height) |
| `y:Fill` | Yes | Background color or gradient |
| `y:BorderStyle` | No | Border line around the shape |
| `y:NodeLabel` | No (0 or more) | Visible text on the node |
| `y:Shape` | Yes | Geometric shape outline |
| `y:DropShadow` | No | Shadow effect |

### Geometry
<!-- Lines 81-91 -->

```xml
<y:Geometry height="40.0" width="120.0" x="100.0" y="200.0"/>
```

- `x`, `y`: Top-left corner in screen coordinates (+x right, +y down)
- `width`, `height`: Node dimensions in pixels
- If omitted or set to `x="0" y="0"`, nodes stack at the origin. Run auto-layout in yEd after import.

---

## Shape Types
<!-- Lines 94-114 -->

Set via `<y:Shape type="..."/>`. This controls the geometric outline — the visual silhouette of the node.

| `type` value | Shape |
| ------------ | ----- |
| `rectangle` | Rectangle |
| `roundrectangle` | Rounded rectangle |
| `ellipse` | Ellipse / circle |
| `diamond` | Diamond / rhombus |
| `triangle` | Triangle |
| `parallelogram` | Parallelogram |
| `hexagon` | Hexagon |
| `octagon` | Octagon |
| `trapezoid` | Trapezoid |
| `trapezoid2` | Inverted trapezoid |
| `rectangle3d` | 3D rectangle |

An unknown `type` value falls back to a basic rectangle without error.

---

## Fill and Border
<!-- Lines 117-117 -->

### Fill
<!-- Lines 120-130 -->

```xml
<y:Fill color="#FFCC00" color2="#FF9900" transparent="false"/>
```

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `color` | Hex string | Primary fill color (`"#FFCC00"`) |
| `color2` | Hex string | Gradient second color (top-to-bottom gradient) |
| `transparent` | Boolean | If `"true"`, fill is invisible (outline-only node) |

### Border
<!-- Lines 133-143 -->

```xml
<y:BorderStyle color="#000000" type="line" width="1.0"/>
```

| Attribute | Values | Description |
| --------- | ------ | ----------- |
| `color` | Hex string | Border color |
| `type` | `line`, `dashed`, `dotted`, `dashed_dotted` | Line pattern |
| `width` | Double | Thickness in pixels |

### Drop Shadow
<!-- Lines 146-153 -->

```xml
<y:DropShadow color="#B3000000" offsetX="3" offsetY="3"/>
```

The `color` attribute supports alpha channel (`#AARRGGBB` format). `offsetX`/`offsetY` control the shadow displacement.

For label configuration, see [05_labels.md](05_labels.md).
