# Obsidian export: JavaScript guideline IntentGraphs

One vault, one folder per IntentGraph. The folders are generated and not committed
(`.gitignore`); this README is.

| Folder | IntentGraph | Source file |
|--------|-------------|-------------|
| **js_philosophy/** | JavaScript principles, product graph `js-philosophy` | `../js_philosophy.ig.yaml` |
| **js_defaults/** | JavaScript rules, projection graph `pig-js-defaults` (`PIG-JS.*`) | `../js_defaults.ig.yaml` |

## Export

From anywhere: `intent_graphs/export_to_obsidian.sh`. It runs `ig-tool obsidian export` for both
graphs with `--vault-root obsidian_export/` and `--force`, in the default grid layout, which writes
canvases only and never modifies the graph files. Requires `ig-tool`.

## Where to start

Open `obsidian_export/` as an Obsidian vault, then:

- `js_defaults/viz/__FT_ROOT.canvas`: the whole rule tree, root and the eight branches.
- `js_defaults/viz/_FT_PIG-JS.<BRANCH>.canvas`: one branch expanded (for example
  `_FT_PIG-JS.DEFENSE.canvas`).
- `js_philosophy/viz/__FT_ROOT.canvas`: the principles, same eight branches.
- `*/viz/<UID>.canvas`: one canvas per node that has children; `*/nodes/*.md`: one note per node,
  its fields in the frontmatter.

## Editing

The graph files are the source of truth. Edit them, re-export, and the vault follows. Edits made
in Obsidian can be brought back with `ig-tool obsidian diff` then `ig-tool obsidian merge`
(content fields only); see the `ig-tool-obsidian` skill in the IntentGraph repository.
