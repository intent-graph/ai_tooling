# Stage 6, step 2: build both graphs with ig-tool from the generated inputs. Run from the guideline root:
#   zsh build/assemble/build_graphs.sh
# Needs: build/assemble/gen/ (python3 build/assemble/build_batches.py). Rebuilds from scratch (--force).
set -e
G=build/assemble/gen
OUT=intent_graphs
mkdir -p $OUT
IGPY=$(sed -n '1s/^#!//p' "$(command -v ig-tool)")

# ---- js-philosophy: every uid passes ig-tool's uid rules, so init + batch + inter links is pure ig-tool
ROOT_NAME=$(python3 -c "import json;print(json.load(open('$G/js_philosophy_root.json'))['name'])")
ROOT_INTENT=$(python3 -c "import json;print(json.load(open('$G/js_philosophy_root.json'))['intent'])")
ig-tool init -o $OUT/js_philosophy.ig.yaml --force --root --name js-philosophy \
  --description "Product graph of the JavaScript guideline: eight principles on a predictable language subset, contracts, control of time and failure, locality of change, defense, dependencies, verification and runtime behaviour." \
  --root-name "$ROOT_NAME" --root-intent "$ROOT_INTENT" --role assembler -m "init the js-philosophy product graph" > /dev/null
ig-tool apply -g $OUT/js_philosophy.ig.yaml --batch $G/js_philosophy_batch.yaml -o $OUT/js_philosophy.ig.yaml \
  --role assembler -m "nodes, constraints, design notes, impl pointers and links from the integrated skeleton and ledger"
zsh $G/js_philosophy_inter.sh

# ---- pig-js-defaults: tree by library (see apply_tree.py), content and links by ig-tool
ig-tool init -o $OUT/js_defaults.ig.yaml --force --name pig-js-defaults \
  --description "Projection graph of the JavaScript guideline: the concrete rules, one decision per node, rendering js-philosophy." \
  --role assembler -m "init the pig-js-defaults projection graph" > /dev/null
$IGPY build/assemble/apply_tree.py $OUT/js_defaults.ig.yaml $OUT/js_defaults.ig.yaml $G/js_defaults_tree.json
ig-tool apply -g $OUT/js_defaults.ig.yaml --batch $G/js_defaults_batch.yaml -o $OUT/js_defaults.ig.yaml \
  --role assembler -m "constraints, design notes, impl pointers, epistemic states and links from the integrated skeleton and ledger"
zsh $G/js_defaults_inter.sh
echo built
