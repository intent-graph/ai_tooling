#!/usr/bin/env bash
# Export both web architecture IntentGraphs to one Obsidian vault. Run from anywhere.
# Requires: ig-tool (reads the YAML graphs directly). Usage: ./export_to_obsidian.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

ig-tool obsidian export -g web_app_philosophy.ig.yaml -o obsidian_export/web_app_philosophy/ --vault-root obsidian_export/ --force
ig-tool obsidian export -g web_defaults.ig.yaml -o obsidian_export/web_defaults/ --vault-root obsidian_export/ --force

echo "Exported to obsidian_export/web_app_philosophy/ and obsidian_export/web_defaults/"
