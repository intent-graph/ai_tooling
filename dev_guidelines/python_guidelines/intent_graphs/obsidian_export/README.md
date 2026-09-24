# Obsidian export — Python KB IntentGraphs

One folder per IG, explicit naming:

| Folder | IntentGraph | Source file |
|--------|-------------|-------------|
| **philosophy/** | Python KB Philosophy (8 principles) | `../python_kb_philosophy.yaml` |
| **python_defaults/** | Python projection defaults (PIG-PY.*) | `../python_defaults.ig.yaml` |

**Export** — one liner (from repo root or `intent_graphs/`):

```bash
./intent_graphs/export_to_obsidian.sh
```

The script converts YAML→JSON (Ruby), runs `ig-tool obsidian export` for both graphs with `--vault-root obsidian_export/`, and cleans up. Requires `ruby`, `ig-tool`.

Each export creates `nodes/*.md`, `edges.yaml`, and `viz/*.canvas` under that folder.
