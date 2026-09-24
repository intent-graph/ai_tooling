# HTML Visualization Usage Guide

## Quick Start
<!-- Lines 5-5 -->

### Generate HTML visualization for any documentation tree
<!-- Lines 8-18 -->

```bash
cd md_structure_viz

# Generate HTML for your project
python -m md_structure_viz.cli /path/to/your/docs --format html --output visualization.html

# Open in browser
open visualization.html
```

### Example: my_project Documentation
<!-- Lines 21-30 -->

```bash
python -m md_structure_viz.cli /path/to/my_project/docs \
  --format html \
  --output my_project_manifest.html

# Then open in browser
open my_project_manifest.html
```

## What You'll See
<!-- Lines 33-35 -->

The visualization has three sections:

### 1. Left Panel: File Tree
<!-- Lines 38-43 -->
- Shows your documentation structure as an expandable tree
- Green files are "hubs" (referenced by 5+ other files)
- Gray files are "orphans" (not referenced by anything)
- Click any file to inspect it on the right
- Expand/collapse folders with the arrow icons

### 2. Center Panel: Graph Visualization
<!-- Lines 46-54 -->
- Each circle is a documentation file
- Arrows show how files reference each other
- Node size and color indicate importance:
  - **Orange**: Hub files (frequently referenced)
  - **Blue**: Normal files
  - **Gray**: Orphaned files
- Hover over nodes to see highlights
- Nodes are interactive and can be dragged

### 3. Right Panel: File Inspector
<!-- Lines 57-64 -->
- Shows details about the selected file:
  - File path
  - Title (from `# Heading`)
  - Number of sections
  - Files it references
  - Files that reference it
  - Classification (hub/normal/orphan)

## Statistics Display
<!-- Lines 67-74 -->

The header shows at a glance:
- Total files
- Total sections/headings
- Total cross-references
- Maximum nesting depth
- Generation timestamp

## Interaction Guide
<!-- Lines 77-86 -->

| Action | Result |
|--------|--------|
| Click a file in the tree | Selects it, shows inspector |
| Click a node in the graph | Same as above |
| Hover over a node | Highlights connected nodes |
| Expand/collapse folders | Shows/hides files in folder |
| Drag a node | Repositions it in the graph |
| Type in search box | Filters tree (future feature) |

## Use Cases
<!-- Lines 89-89 -->

### Find Most-Referenced Files
<!-- Lines 92-95 -->
1. Look for **orange nodes** in the graph (largest/brightest)
2. Or look for **green file icons** in the tree
3. These are documentation hubs that many files reference

### Find Orphaned Documentation
<!-- Lines 98-101 -->
1. Look for **gray nodes** in the graph
2. Or scroll through tree for **gray file icons**
3. These files aren't referenced by anything (might need linking)

### Understand File Relationships
<!-- Lines 104-108 -->
1. Select a file from the tree
2. Right panel shows all incoming/outgoing references
3. Graph highlights connected nodes
4. This helps find related documentation clusters

### Navigate Large Documentation
<!-- Lines 111-115 -->
Instead of scrolling a huge Markdown file with 400+ nodes, you can:
1. Expand only the folders you care about
2. See the graph layout with force-directed spacing
3. Jump between related files by clicking connections

## Command Line Options
<!-- Lines 118-135 -->

```bash
# Basic usage
md-doc-tree-full /path/to/docs --format html

# Specify output file
md-doc-tree-full /path/to/docs --format html --output custom_name.html

# Ignore certain directories (default behavior includes common patterns)
md-doc-tree-full /path/to/docs --format html --no-ignore-default

# Respect .gitignore patterns
md-doc-tree-full /path/to/docs --format html --respect-gitignore

# Just show stats (--format flow avoids the default manifest format's --output requirement)
md-doc-tree-full /path/to/docs --stats --format flow
```

## Performance
<!-- Lines 138-148 -->

| Files | Generation Time | File Size | Browser Load |
|-------|-----------------|-----------|--------------|
| 10 | < 50ms | ~20KB | Instant |
| 50 | ~100ms | ~50KB | Instant |
| 93 | ~100ms | ~75KB | 1-2s |
| 287 | ~300ms | ~150KB | 2-3s |
| 500+ | ~500ms | ~300KB+ | May need optimization |

For very large documentation (500+), the browser layout stabilization takes 2-5 seconds but is still interactive.

## Troubleshooting
<!-- Lines 151-151 -->

### Graph doesn't show any nodes
<!-- Lines 154-156 -->
- **Check:** Do you have markdown files with cross-references?
- **Solution:** If no `.md` files reference each other, graph will be empty. Try with a project that has cross-references.

### Nodes are all bunched up
<!-- Lines 159-162 -->
- **Wait:** Give the force simulation ~5 seconds to stabilize
- **Drag:** Manually drag nodes apart to help it settle
- **Refresh:** Browser back button and reload page

### File takes forever to load
<!-- Lines 165-167 -->
- **Check:** Is it a very large project (500+ files)?
- **Solution:** Works fine up to ~300 files; above that may need optimization

### Some files are missing
<!-- Lines 170-172 -->
- **Check:** Are they being ignored by default patterns?
- **Solution:** Use `--no-ignore-default` to include venv, node_modules, etc.

## Advanced: Customization
<!-- Lines 175-184 -->

The HTML is self-contained, so you can:

1. **Edit styling** directly in the HTML file (CSS section)
2. **Change colors** in the CSS or JavaScript
3. **Adjust force simulation** parameters (strength, distance)
4. **Modify node sizes** based on different metrics

Edit the `html_template.html` file to make changes for all future generations.

## Next Steps
<!-- Lines 187-187 -->

### Basic Usage
<!-- Lines 190-193 -->
1. ✅ Generate HTML visualization
2. ✅ Browse your documentation structure
3. ✅ Identify hubs and orphans

### Advanced Analysis
<!-- Lines 196-200 -->
- Filter to specific folders
- Export graph as image
- Track changes over time (re-generate regularly)
- Dark mode theme

## File Reference
<!-- Lines 203-215 -->

- **Generated file:** Single `.html` file with all data embedded
- **No external files needed:** Just open in browser
- **Can be hosted:** Works on HTTP servers
- **Can be shared:** Email it around or commit to git
- **Data is static:** Re-generate whenever you update docs

---

**Questions?** Examine the source code:
- Generator: `src/md_structure_viz/html_generator.py`
- Template: `src/md_structure_viz/html_template.html`
- CLI: `src/md_structure_viz/cli.py`
