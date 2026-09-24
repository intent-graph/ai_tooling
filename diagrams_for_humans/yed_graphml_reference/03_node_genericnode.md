# GenericNode (Flowchart / Modern / BPMN / ER)

`y:GenericNode` uses a `configuration` attribute to select the shape instead of `<y:Shape>`. Everything else (`y:Geometry`, `y:Fill`, `y:BorderStyle`, `y:NodeLabel`) is identical to [ShapeNode](02_node_shapenode.md). Requires the XML skeleton from [01_xml_skeleton.md](01_xml_skeleton.md).

## Table of Contents

1. [XML Structure](#xml-structure) _(Lines 24-24)_
   1. [Flowchart Process Node](#flowchart-process-node) _(Lines 27-42)_
   1. [Flowchart Decision Node](#flowchart-decision-node) _(Lines 45-62)_
1. [GenericNode vs ShapeNode](#genericnode-vs-shapenode) _(Lines 65-81)_
1. [Flowchart Configurations (28)](#flowchart-configurations-28) _(Lines 84-117)_
   1. [Flowchart StyleProperties](#flowchart-styleproperties) _(Lines 120-138)_
1. [Modern Node Configurations (8)](#modern-node-configurations-8) _(Lines 141-154)_
   1. [Modern StyleProperties](#modern-styleproperties) _(Lines 157-173)_
1. [Entity Relationship Configurations (4)](#entity-relationship-configurations-4) _(Lines 176-183)_
   1. [ER Label Configurations](#er-label-configurations) _(Lines 186-212)_
1. [BPMN Configurations (8)](#bpmn-configurations-8) _(Lines 215-246)_


---

## XML Structure
<!-- Lines 24-24 -->

### Flowchart Process Node
<!-- Lines 27-42 -->

```xml
<node id="n0">
  <data key="d6">
    <y:GenericNode configuration="com.yworks.flowchart.process">
      <y:Geometry height="40.0" width="120.0" x="100.0" y="200.0"/>
      <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
      <y:BorderStyle color="#000000" type="line" width="1.0"/>
      <y:NodeLabel alignment="center" autoSizePolicy="content"
        fontFamily="Dialog" fontSize="12" fontStyle="plain"
        textColor="#000000" visible="true">Process Step</y:NodeLabel>
    </y:GenericNode>
  </data>
</node>
```

### Flowchart Decision Node
<!-- Lines 45-62 -->

```xml
<node id="n1">
  <data key="d6">
    <y:GenericNode configuration="com.yworks.flowchart.decision">
      <y:Geometry height="60.0" width="80.0" x="300.0" y="190.0"/>
      <y:Fill color="#FFFFCC" color2="#FFFFAA" transparent="false"/>
      <y:BorderStyle color="#000000" type="line" width="1.0"/>
      <y:NodeLabel alignment="center" autoSizePolicy="content"
        fontFamily="Dialog" fontSize="12" fontStyle="plain"
        textColor="#000000" visible="true">Yes/No?</y:NodeLabel>
    </y:GenericNode>
  </data>
</node>
```

---

## GenericNode vs ShapeNode
<!-- Lines 65-81 -->

| Aspect | ShapeNode | GenericNode |
| ------ | --------- | ----------- |
| Shape selection | `<y:Shape type="rectangle"/>` | `configuration="com.yworks.flowchart.process"` |
| Shared elements | `y:Geometry`, `y:Fill`, `y:BorderStyle`, `y:NodeLabel` | Same (inherited from Node.type) |
| Extra elements | `y:Shape`, `y:DropShadow` | `y:StyleProperties`, `y:UserData` |
| Use case | Basic geometric shapes | Domain-specific shapes (flowchart, BPMN, ER, modern) |

GenericNode adds two elements ShapeNode does not have:

- **`y:StyleProperties`** — configuration-specific visual tuning (shadow, orientation, BPMN sub-types, corner radius)
- **`y:UserData`** — application-specific serialized state (rarely needed for generation)

If yEd encounters an unknown `configuration` string, it falls back to a basic rectangle. No error.

---

## Flowchart Configurations (28)
<!-- Lines 84-117 -->

All prefixed with `com.yworks.flowchart.`:

| Configuration suffix | Standard symbol |
| -------------------- | --------------- |
| `process` | Process rectangle |
| `decision` | Decision diamond |
| `start1` | Start/end oval (variant 1) |
| `start2` | Start/end oval (variant 2) |
| `terminator` | Terminator (stadium shape) |
| `predefinedProcess` | Predefined process (rectangle with side bars) |
| `document` | Document (wavy bottom) |
| `data` | Data / I-O (parallelogram) |
| `directData` | Direct data (cylinder on side) |
| `storedData` | Stored data (reverse D) |
| `sequentialData` | Sequential data (tape reel) |
| `dataBase` | Database (cylinder) |
| `internalStorage` | Internal storage (corner lines) |
| `manualInput` | Manual input (slanted top trapezoid) |
| `card` | Card (clipped corner rectangle) |
| `paperType` | Paper type (flag/fold) |
| `cloud` | Cloud shape |
| `delay` | Delay (half-circle right) |
| `display` | Display (pointed left) |
| `manualOperation` | Manual operation (inverted trapezoid) |
| `preparation` | Preparation (hexagon) |
| `loopLimit` | Loop limit (flat-bottom pentagon) |
| `loopLimitEnd` | Loop limit end (flat-top pentagon) |
| `onPageReference` | On-page connector (circle) |
| `offPageReference` | Off-page connector (pentagon arrow) |
| `annotation` | Annotation (bracket) |
| `userMessage` | User message (envelope variant) |
| `networkMessage` | Network message (envelope variant) |

### Flowchart StyleProperties
<!-- Lines 120-138 -->

Optional. Placed as a child of `<y:GenericNode>`:

```xml
<y:StyleProperties>
  <!-- Drop shadow -->
  <y:Property class="java.lang.Boolean"
    name="y.view.ShadowNodePainter.SHADOW_PAINTING" value="true"/>
  <!-- Orientation for asymmetric shapes: 0, 1, 2, 3, or 4 -->
  <y:Property class="java.lang.Byte"
    name="com.yworks.flowchart.style.orientation" value="0"/>
  <!-- Double border line -->
  <y:Property class="java.lang.Boolean"
    name="doubleBorder" value="true"/>
</y:StyleProperties>
```

---

## Modern Node Configurations (8)
<!-- Lines 141-154 -->

No prefix — just the configuration name directly on the `configuration` attribute.

| Configuration | Visual |
| ------------- | ------ |
| `BevelNode` | Beveled 3D rectangle |
| `BevelNode2` | Bevel variant 2 |
| `BevelNode3` | Bevel variant 3 |
| `BevelNodeWithShadow` | Beveled with drop shadow |
| `ShinyPlateNode` | Glossy plate rectangle |
| `ShinyPlateNode2` | Shiny plate variant 2 |
| `ShinyPlateNode3` | Shiny plate variant 3 |
| `ShinyPlateNodeWithShadow` | Shiny plate with shadow |

### Modern StyleProperties
<!-- Lines 157-173 -->

```xml
<y:StyleProperties>
  <y:Property class="java.lang.Boolean"
    name="ModernNodeShadow" value="true"/>
  <y:Property class="java.lang.Double"
    name="ModernNodeRadius" value="15.0"/>
</y:StyleProperties>
```

| Property | Class | Default | Description |
| -------- | ----- | ------- | ----------- |
| `ModernNodeShadow` | `java.lang.Boolean` | `false` | Enable shadow |
| `ModernNodeRadius` | `java.lang.Double` | `10.0` | Corner radius |

---

## Entity Relationship Configurations (4)
<!-- Lines 176-183 -->

| Configuration | Description |
| ------------- | ----------- |
| `com.yworks.entityRelationship.big_entity` | Entity with header + attributes area |
| `com.yworks.entityRelationship.small_entity` | Compact entity box |
| `com.yworks.entityRelationship.relationship` | Relationship diamond |
| `com.yworks.entityRelationship.attribute` | Attribute oval |

### ER Label Configurations
<!-- Lines 186-212 -->

ER nodes use a special `configuration` attribute on `y:NodeLabel` itself (not on the node):

```xml
<y:GenericNode configuration="com.yworks.entityRelationship.big_entity">
  <y:Geometry height="76.0" width="80.0" x="0.0" y="0.0"/>
  <y:Fill color="#E8EEF7" color2="#B7C9E3" transparent="false"/>
  <y:BorderStyle color="#000000" type="line" width="1.0"/>
  <!-- Header label -->
  <y:NodeLabel backgroundColor="#B7C9E3"
    configuration="com.yworks.entityRelationship.label.name"
    modelName="internal" modelPosition="t"
    fontSize="12" fontStyle="bold">users</y:NodeLabel>
  <!-- Attributes label -->
  <y:NodeLabel alignment="left"
    configuration="com.yworks.entityRelationship.label.attributes"
    modelName="custom" fontSize="12">id
name
email</y:NodeLabel>
</y:GenericNode>
```

- `com.yworks.entityRelationship.label.name` — renders as the header section with a background band
- `com.yworks.entityRelationship.label.attributes` — renders as the body section for listing fields

---

## BPMN Configurations (8)
<!-- Lines 215-246 -->

Each has a plain and `.withShadow` variant:

| Configuration | Description |
| ------------- | ----------- |
| `com.yworks.bpmn.Event` / `.withShadow` | Event circle |
| `com.yworks.bpmn.Activity` / `.withShadow` | Activity rectangle |
| `com.yworks.bpmn.Gateway` / `.withShadow` | Gateway diamond |
| `com.yworks.bpmn.Conversation` / `.withShadow` | Conversation hexagon |

BPMN nodes use the richest StyleProperties. Key properties:

```xml
<y:StyleProperties>
  <y:Property class="com.yworks.yfiles.bpmn.view.BPMNTypeEnum"
    name="com.yworks.bpmn.type" value="EVENT_TYPE_PLAIN"/>
  <y:Property class="com.yworks.yfiles.bpmn.view.EventCharEnum"
    name="com.yworks.bpmn.characteristic" value="EVENT_CHARACTERISTIC_START"/>
  <y:Property class="com.yworks.yfiles.bpmn.view.ActivityTypeEnum"
    name="com.yworks.bpmn.activityType" value="ACTIVITY_TYPE_TASK"/>
  <y:Property class="com.yworks.yfiles.bpmn.view.TaskTypeEnum"
    name="com.yworks.bpmn.taskType" value="TASK_TYPE_USER"/>
  <y:Property class="java.awt.Color"
    name="com.yworks.bpmn.icon.line.color" value="#000000"/>
  <y:Property class="java.awt.Color"
    name="com.yworks.bpmn.icon.fill" value="#ffffffe6"/>
  <y:Property class="java.awt.Color"
    name="com.yworks.bpmn.icon.fill2" value="#d4d4d4cc"/>
</y:StyleProperties>
```

For label configuration on any node type, see [05_labels.md](05_labels.md).
