"""Stage 6, step 2b: lay down the tree of the defaults graph (uid, name, intent, parent) with the IntentGraph library.

Why this exists: `ig-tool node create` and `apply --batch` check a child's uid against the parent's
(`models/node.py::validate_uid_format`): under a root whose uid is not exactly `ROOT`, `PIG-JS.SUBSET`
fails ("must start with parent prefix PIG-JS.ROOT."), as does every L2 keyword node. The brief fixes
the uids `PIG-JS.*` (as `PIG-PY.*` in the Python defaults graph), so the attach step skips that one
check, the same switch `lens apply` uses for reparenting (`attach(..., skip_uid_validation=True)`).
Everything else (content, links) is applied with `ig-tool apply --batch` and `ig-tool link create`.

Run with the interpreter of the installed ig-tool; usage: apply_tree.py GRAPH_IN GRAPH_OUT TREE_JSON
"""
import argparse
import json
import sys

from ig_agents.cli.common import _load_graph, _save_graph

graph_in, graph_out, tree_json = sys.argv[1:4]
graph = _load_graph(graph_in)
tree = json.load(open(tree_json))
for n in tree:
    graph.add_node(n["uid"], n["name"], n["intent"])
    if n["parent"]:
        graph.attach(n["parent"], n["uid"], skip_uid_validation=True)
_save_graph(graph, graph_out, argparse.Namespace(role="assembler", message="tree of the defaults graph from the integrated skeleton (uid check skipped on attach)"))
print(f"nodes: {len(tree)}")
