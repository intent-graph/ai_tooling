# Edges (PolyLineEdge)

All edges in yEd use `y:PolyLineEdge` as their visual realizer. This controls line style, arrowheads, labels, and routing. Requires the XML skeleton from [01_xml_skeleton.md](01_xml_skeleton.md).

## Table of Contents

1. [XML Structure](#xml-structure) _(Lines 23-23)_
   1. [Complete Example](#complete-example) _(Lines 26-44)_
   1. [Minimal Edge](#minimal-edge) _(Lines 47-59)_
   1. [Child Elements](#child-elements) _(Lines 62-74)_
1. [Arrow Types](#arrow-types) _(Lines 77-106)_
1. [Line Types](#line-types) _(Lines 109-122)_
1. [Path and Bend Points](#path-and-bend-points) _(Lines 125-142)_
   1. [BendStyle](#bendstyle) _(Lines 145-156)_
1. [Edge Labels](#edge-labels) _(Lines 159-169)_
   1. [EdgeLabel Placement Models](#edgelabel-placement-models) _(Lines 172-183)_


---

## XML Structure
<!-- Lines 23-23 -->

### Complete Example
<!-- Lines 26-44 -->

```xml
<edge id="e0" source="n0" target="n1">
  <data key="d10">
    <y:PolyLineEdge>
      <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
      <y:LineStyle color="#000000" type="line" width="1.0"/>
      <y:Arrows source="none" target="standard"/>
      <y:EdgeLabel alignment="center" distance="2.0"
                    fontFamily="Dialog" fontSize="12" fontStyle="plain"
                    hasBackgroundColor="false" hasLineColor="false"
                    modelName="centered" modelPosition="center"
                    textColor="#000000" visible="true">triggers</y:EdgeLabel>
      <y:BendStyle smoothed="false"/>
    </y:PolyLineEdge>
  </data>
</edge>
```

### Minimal Edge
<!-- Lines 47-59 -->

```xml
<edge id="e0" source="n0" target="n1">
  <data key="d10">
    <y:PolyLineEdge>
      <y:LineStyle color="#000000" type="line" width="1.0"/>
      <y:Arrows source="none" target="standard"/>
      <y:BendStyle smoothed="false"/>
    </y:PolyLineEdge>
  </data>
</edge>
```

### Child Elements
<!-- Lines 62-74 -->

| Element | Required | What Gets Displayed |
| ------- | -------- | ------------------- |
| `y:Path` | No | Edge routing: source/target offsets + bend points |
| `y:LineStyle` | No | Line color, pattern, thickness |
| `y:Arrows` | Yes | Arrowhead shapes at each end |
| `y:EdgeLabel` | No (0 or more) | Visible text along the edge |
| `y:BendStyle` | Yes | Angular vs curved bends |

The `source` and `target` attributes on `<edge>` must reference existing node IDs. For nodes inside groups, use the full ID (e.g., `source="grp1::n0"`) — see [06_groups.md](06_groups.md#edges-crossing-group-boundaries).

---

## Arrow Types
<!-- Lines 77-106 -->

Set via `<y:Arrows source="..." target="..."/>`. Both attributes accept the same values.

| Value | Shape |
| ----- | ----- |
| `none` | No arrow |
| `standard` | Default arrowhead |
| `delta` | Filled triangle |
| `white_delta` | White-filled triangle |
| `diamond` | Diamond |
| `white_diamond` | White-filled diamond |
| `plain` | Simple arrow |
| `concave` | Concave arrowhead |
| `convex` | Convex arrowhead |
| `circle` | Circle |
| `transparent_circle` | Transparent circle |
| `dash` | Dash |
| `skewed_dash` | Skewed dash |
| `t_shape` | T-shaped |

Common combinations:

- **Directed edge**: `source="none" target="standard"`
- **Bidirectional**: `source="standard" target="standard"`
- **Undirected**: `source="none" target="none"`
- **Composition (UML)**: `source="diamond" target="none"`
- **Aggregation (UML)**: `source="white_diamond" target="none"`

---

## Line Types
<!-- Lines 109-122 -->

Set via `<y:LineStyle color="..." type="..." width="..."/>`.

| `type` value | Pattern |
| ------------ | ------- |
| `line` | Solid continuous line |
| `dashed` | Dashed line |
| `dotted` | Dotted line |
| `dashed_dotted` | Alternating dash-dot |

`color` is a hex string (`"#FF0000"`). `width` is a double in pixels (`"2.0"`).

---

## Path and Bend Points
<!-- Lines 125-142 -->

The `y:Path` element controls edge routing. If omitted, yEd draws a straight line between node centers.

```xml
<y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0">
  <y:Point x="150.0" y="300.0"/>
  <y:Point x="200.0" y="300.0"/>
</y:Path>
```

| Attribute | Description |
| --------- | ----------- |
| `sx`, `sy` | Source port offset from node center |
| `tx`, `ty` | Target port offset from node center |
| `y:Point` children | Intermediate bend points, in order |

Setting `sx="0" sy="0" tx="0" ty="0"` (the default) connects node centers. Non-zero offsets shift the connection point.

### BendStyle
<!-- Lines 145-156 -->

```xml
<y:BendStyle smoothed="false"/>
```

- `smoothed="false"` — angular bends (sharp corners at each `y:Point`)
- `smoothed="true"` — curved bends (smooth spline through bend points)

When generating programmatically, omit `y:Path` and set `smoothed="false"`. Let the user run auto-layout in yEd.

---

## Edge Labels
<!-- Lines 159-169 -->

Edge labels use `y:EdgeLabel` inside `y:PolyLineEdge`. The text content is what gets displayed.

```xml
<y:EdgeLabel alignment="center" distance="2.0"
  fontFamily="Dialog" fontSize="12" fontStyle="plain"
  hasBackgroundColor="false" hasLineColor="false"
  modelName="centered" modelPosition="center"
  textColor="#000000" visible="true">label text</y:EdgeLabel>
```

### EdgeLabel Placement Models
<!-- Lines 172-183 -->

| `modelName` | Valid `modelPosition` values | Description |
| ----------- | ---------------------------- | ----------- |
| `centered` | `center` | Single center position |
| `two_pos` | `head`, `tail` | Near source or target |
| `three_center` | `center`, `head`, `tail` | Three positions along center line |
| `six_pos` | `head`, `tail`, `shead`, `stail`, `thead`, `ttail` | Six positions (3 on each side) |
| `center_slider` | `center`, `anywhere` | Freely movable along center |
| `side_slider` | `anywhere` | Freely movable along side |
| `free` | `anywhere` | Free positioning |

For the full label attribute reference (fonts, colors, sizing), see [05_labels.md](05_labels.md).
