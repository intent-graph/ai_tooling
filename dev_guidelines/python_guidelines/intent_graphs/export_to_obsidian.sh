#!/usr/bin/env bash
# Export both Python KB IntentGraphs to Obsidian. Run from anywhere.
# Requires: ruby (YAML/JSON in stdlib), ig-tool. Usage: ./export_to_obsidian.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

yaml2json() {
  ruby -r yaml -r json -e 'File.write(ARGV[1], JSON.pretty_generate(YAML.load_file(ARGV[0])))' "$1" "$2"
}

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

yaml2json python_kb_philosophy.yaml "$TMP/philosophy.json"
yaml2json python_defaults.ig.yaml "$TMP/python_defaults.json"

ig-tool obsidian export -g "$TMP/philosophy.json" -o obsidian_export/philosophy/ --vault-root obsidian_export/ --force
ig-tool obsidian export -g "$TMP/python_defaults.json" -o obsidian_export/python_defaults/ --vault-root obsidian_export/ --force

echo "Exported to obsidian_export/philosophy/ and obsidian_export/python_defaults/"
