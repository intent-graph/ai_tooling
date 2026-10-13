# Obsidian export — web architecture IntentGraphs

One Obsidian vault (this folder), one sub-folder per IntentGraph:

| Folder | IntentGraph | Source file |
|--------|-------------|-------------|
| **web_app_philosophy/** | Web App Philosophy (stack-neutral principles) | `../web_app_philosophy.ig.yaml` |
| **web_defaults/** | Web defaults for JavaScript + Python + Postgres (`PIG-WEB-*`) | `../web_defaults.ig.yaml` |

**Export** — one liner (from the guideline folder or `intent_graphs/`):

```bash
./intent_graphs/export_to_obsidian.sh
```

The script runs `ig-tool obsidian export` for both graphs with `--vault-root obsidian_export/`.
Requires `ig-tool`. Each export creates `nodes/*.md`, `edges.yaml` and `viz/*.canvas` under its
folder. The exported files are generated: regenerate them after any graph edit instead of
editing them; to bring vault edits back into a graph, use `ig-tool obsidian merge`.
