#!/usr/bin/env zsh
# Export both JavaScript guideline IntentGraphs to one Obsidian vault. Run from anywhere.
# Requires: ig-tool. Usage: ./export_to_obsidian.sh
# Grid layout (default): writes canvases only, never modifies the graph files.

set -e
cd "${0:A:h}"

ig-tool obsidian export -g js_philosophy.ig.yaml -o obsidian_export/js_philosophy/ --vault-root obsidian_export/ --force
ig-tool obsidian export -g js_defaults.ig.yaml -o obsidian_export/js_defaults/ --vault-root obsidian_export/ --force

echo "Exported to obsidian_export/js_philosophy/ and obsidian_export/js_defaults/"
echo "Open obsidian_export/ as a vault; start at js_defaults/viz/__FT_ROOT.canvas"
