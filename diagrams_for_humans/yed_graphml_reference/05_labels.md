# Labels (NodeLabel and EdgeLabel)

The text content of `<y:NodeLabel>` and `<y:EdgeLabel>` is what yEd renders as visible text. Both elements share the same attribute set for fonts, colors, and sizing. `y:NodeLabel` goes inside [ShapeNode](02_node_shapenode.md) or [GenericNode](03_node_genericnode.md); `y:EdgeLabel` goes inside [PolyLineEdge](04_edges.md).

## Table of Contents

1. [Core Rule](#core-rule) _(Lines 23-34)_
1. [Font and Color Attributes](#font-and-color-attributes) _(Lines 37-52)_
   1. [Minimal Label](#minimal-label) _(Lines 55-61)_
   1. [Styled Label](#styled-label) _(Lines 64-72)_
1. [Sizing Attributes](#sizing-attributes) _(Lines 75-87)_
1. [NodeLabel Placement Models](#nodelabel-placement-models) _(Lines 90-102)_
   1. [Most Common: Internal Centered](#most-common-internal-centered) _(Lines 105-109)_
   1. [Custom Placement (SmartNodeLabelModel)](#custom-placement-smartnodelabelmodel) _(Lines 112-131)_
1. [EdgeLabel Placement Models](#edgelabel-placement-models) _(Lines 134-146)_
   1. [Most Common: Centered](#most-common-centered) _(Lines 149-154)_


---

## Core Rule
<!-- Lines 23-34 -->

Labels defined as standard GraphML `<data>` attributes are **NOT displayed**:

```xml
<!-- THIS DOES NOT DISPLAY IN yEd -->
<data key="label">My Label</data>
```

Only `y:NodeLabel` inside a visual realizer (`y:ShapeNode` or `y:GenericNode`) and `y:EdgeLabel` inside `y:PolyLineEdge` are rendered. See [07_pitfalls.md](07_pitfalls.md#3-labels-in-standard-graphml-data-not-displayed) for details on this common mistake.

---

## Font and Color Attributes
<!-- Lines 37-52 -->

These attributes are shared by both `y:NodeLabel` and `y:EdgeLabel`:

| Attribute | Values | What It Controls |
| --------- | ------ | ---------------- |
| `fontFamily` | Any font string | Font face (`"Dialog"`, `"Arial"`, `"Courier New"`) |
| `fontSize` | Integer | Font size in points |
| `fontStyle` | `plain`, `bold`, `italic`, `bolditalic` | Font weight and style |
| `textColor` | Hex string | Text color (`"#000000"`) |
| `backgroundColor` | Hex string | Label background color |
| `hasBackgroundColor` | Boolean | Whether to paint the label background |
| `lineColor` | Hex string | Label border color |
| `hasLineColor` | Boolean | Whether to paint a border around the label |
| `underlinedText` | Boolean | Underline the text |
| `visible` | Boolean | Whether the label is shown at all |

### Minimal Label
<!-- Lines 55-61 -->

```xml
<y:NodeLabel>Just the text</y:NodeLabel>
```

yEd applies defaults: Dialog font, 12pt, plain, black text, centered, no background.

### Styled Label
<!-- Lines 64-72 -->

```xml
<y:NodeLabel fontFamily="Arial" fontSize="14" fontStyle="bold"
  textColor="#FFFFFF" backgroundColor="#336699"
  hasBackgroundColor="true" hasLineColor="false">Styled</y:NodeLabel>
```

---

## Sizing Attributes
<!-- Lines 75-87 -->

| Attribute | Values | Description |
| --------- | ------ | ----------- |
| `autoSizePolicy` | `content`, `node_width`, `node_height` | How the label box sizes itself |
| `alignment` | `center`, `left`, `right` | Text alignment within the label box |
| `width` | Double | Explicit label width (overrides auto-size) |
| `height` | Double | Explicit label height (overrides auto-size) |
| `rotationAngle` | Double | Rotation in degrees |

**Recommendation**: Always use `autoSizePolicy="content"` when generating programmatically. This lets yEd size the label to fit its text. Combined with `Tools > Fit Node to Label` in yEd, nodes will auto-resize to their labels.

---

## NodeLabel Placement Models
<!-- Lines 90-102 -->

Set via `modelName` and `modelPosition` attributes on `y:NodeLabel`.

| `modelName` | Description | Valid `modelPosition` values |
| ----------- | ----------- | ---------------------------- |
| `internal` | Inside the node | `c`, `t`, `b`, `l`, `r`, `tl`, `tr`, `bl`, `br` |
| `corners` | At node corners | `nw`, `ne`, `sw`, `se` |
| `sandwich` | Above or below | `n`, `s` |
| `sides` | On sides | `n`, `s`, `e`, `w` |
| `eight_pos` | 8 compass positions around | `n`, `ne`, `e`, `se`, `s`, `sw`, `w`, `nw` |
| `free` | Free positioning | `anywhere` |
| `custom` | Custom (needs child elements) | — |

### Most Common: Internal Centered
<!-- Lines 105-109 -->

```xml
<y:NodeLabel modelName="internal" modelPosition="c">Center</y:NodeLabel>
```

### Custom Placement (SmartNodeLabelModel)
<!-- Lines 112-131 -->

For fine-grained control, use `modelName="custom"` with nested elements:

```xml
<y:NodeLabel modelName="custom" textColor="#000000">Label Text
  <y:LabelModel>
    <y:SmartNodeLabelModel distance="4.0"/>
  </y:LabelModel>
  <y:ModelParameter>
    <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0"
      nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0"
      upX="0.0" upY="-1.0"/>
  </y:ModelParameter>
</y:NodeLabel>
```

This is what yEd exports when you manually position a label. For generation, `modelName="internal"` with `modelPosition="c"` covers most cases.

---

## EdgeLabel Placement Models
<!-- Lines 134-146 -->

Set via `modelName` and `modelPosition` attributes on `y:EdgeLabel`.

| `modelName` | Valid `modelPosition` values | Description |
| ----------- | ---------------------------- | ----------- |
| `centered` | `center` | Single center position |
| `two_pos` | `head`, `tail` | Near source or target end |
| `three_center` | `center`, `head`, `tail` | Three positions along center line |
| `six_pos` | `head`, `tail`, `shead`, `stail`, `thead`, `ttail` | Six positions (3 on each side) |
| `center_slider` | `center`, `anywhere` | Freely movable along center |
| `side_slider` | `anywhere` | Freely movable along side |
| `free` | `anywhere` | Free positioning |

### Most Common: Centered
<!-- Lines 149-154 -->

```xml
<y:EdgeLabel modelName="centered" modelPosition="center">label</y:EdgeLabel>
```

The `distance` attribute on `y:EdgeLabel` controls how far the label sits from the edge line (default `2.0`).
