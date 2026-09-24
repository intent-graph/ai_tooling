#!/bin/sh
# Regenerate this folder's example outputs by running codemap on codemap's own source.
# Run from documentation_tools/codemap/ (the tool folder).
set -eu

codemap context src codemap.api.CodeMap.build > examples/self/context_codemap_build.yaml
codemap export-yed src -o examples/self/codemap_self.graphml
