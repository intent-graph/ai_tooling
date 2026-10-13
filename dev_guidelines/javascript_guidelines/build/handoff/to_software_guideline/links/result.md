# Links to the software development guideline: result

## L1 headline

- Inter links created: **46** (4 `refines` from `js-philosophy`, the four restored nodes; 42 `refines` from `pig-js-defaults`), all to `software-development-philosophy`. Grounded: every target uid was read in the target graph with `ig-tool query` and a script over `package.md::` pointers; `ig-tool validate -m` finds 0 errors.
- Links still planned: **1** (`PIG-JS.DEPENDENCIES.PUBLISH.3`, "Ship JavaScript": no node of the software graph states it; reason in L3).
- Validate summaries, run with `-m intent_graphs/intent_resources.yaml`: `js-philosophy` nodes: 56, links: 20, errors: 0, warnings: 0; `pig-js-defaults` nodes: 287, links: 162, errors: 0, warnings: 0.
- `check_complete.py`: `FAILS: 0`. `check_ledger.py`: `claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0`.
- Inferred, needs the software maintainer's eye: 5 targets differ from the package pointer or the planned principle name (L2, L3); `OWNERSHIP.SELECTION.6` is the pointer home of "Existing components first" but its intent does not state it.
- Nothing written in the software guideline's folder; nothing committed or pushed.

## L2 claims

**What was done** (grounded, each re-run after the last edit)
- The 43 planned defaults links and the 4 planned `refines` links of the restored nodes were mapped to target uids. Method: the package outline gives the package uid of each principle; `grep -n 'package.md::'` on the target graph (read through a YAML parse, read-only) gives the node holding it; each target's intent was then read and compared with the sentence of the removed link.
- The skeleton (`build/distill/skeleton.md`) got two new tables, "Inter links from js-philosophy to software-development-philosophy" (4 rows) and "Inter links from pig-js-defaults to software-development-philosophy" (42 rows), parsed by `build_batches.py` exactly as the python-kb-philosophy table is: `ig-tool link create` with both endpoints qualified. `check_complete.py` compares every skeleton link with the built graph and passes.
- `intent_graphs/intent_resources.yaml` lists `software-development-philosophy` as a product graph, path `../../software_development_guidelines/intent_graphs/software_development_philosophy.ig.yaml` (relative, so inter links resolve).
- Graphs rebuilt with the brief's gate sequence (`apply_flags.py`, `build_batches.py`, `build_graphs.sh`); `integrate.py` was not run. Vault re-exported with `export_to_obsidian.sh`. README counts and section 3 updated.
- Ledger (optional step): 66 of the 67 `deferred` "Owned by the software development guideline" rows now end with `(software-development-philosophy:<UID>)`.

**Mapping shape** (grounded)
- Sentences: 38 of the 42 defaults links keep the removed link's sentence word for word; 4 were adjusted (`SECRETS`, `PUBLISH.2`, `FRAMEWORK_SHORTLIST.1`, `STRUCTURE.DIRECTION.3`), each because the target reads differently. The 4 restored-node links had no sentence of their own in the plan; they are drawn from the "why it matters more in JavaScript" text.
- Types: all `refines`, the type of every removed link.
- Targets, by group: `CONSTRUCTION.DATA_NOT_CODE` and its children .1 to .4, 14 links (injection family, uploads, header fields, XML, v8.deserialize, redirects); `ASSURANCE.PERFORMANCE.5` 6; `OWNERSHIP.*` 6; `CONSTRUCTION.HIDING.1` 4; `TRANSVERSE.CONFIG.1` 3; `CONSTRUCTION.STATE.4`, `.STATE.5` and `.BOUNDARY.2` 2 each; the other nine targets one each (L3 table).

**Decisions where the target is not the package pointer's node** (inferred, flagged for the software maintainer)
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` and `.1` ("Existing components first"): the package pointer places the principle on `OWNERSHIP.SELECTION.6`, whose intent covers vetting depth and the isolation test, not "existing components suffice". Linked to `OWNERSHIP.STANCE.1` (a dependency must earn its cost) and `OWNERSHIP.STANCE.2` (a built-in that meets the need is preferred), whose intents state it. Ledger row `DEPENDENCIES-010` keeps `SELECTION.6`, where the graph's pointer puts the claim.
- `PIG-JS.DEPENDENCIES.PUBLISH.2` (tarball contents): the principle sent as "Publishing" is two-factor authentication on publishing accounts; the sentence is about secrets in the shipped artifact, which `TRANSVERSE.CONFIG.1` states ("no credential is recoverable from source, history or artifact"). Linked there.
- `PIG-JS.DEFENSE.SECRETS.2.1` and `.2.2` (tokens): the package pointer says `DEFENSE.SECRETS` is on `TRANSVERSE.CONFIG.1`, but that node's own design notes record that token acceptance moved to `CONSTRUCTION.BOUNDARY.2`. Linked to `BOUNDARY.2`.
- `PIG-JS.DEFENSE.SECRETS` (root of the secrets defaults): linked to `TRANSVERSE.CONFIG.1` for its secrets-out-of-code part only; the target states nothing on randomness, comparison or password storage. The sentence says so.

**Still planned** (grounded for the reason, 1)
- `PIG-JS.DEPENDENCIES.PUBLISH.3`: no node states that a package ships in a form its consumers' runtime can load; the rule rests on one Node limitation (inferred). A target would be invented. The 12 links to the web-architecture graphs are outside this task and unchanged.

**Open**
- Whether `OWNERSHIP.SELECTION.6` should state "existing components first" (then `FRAMEWORK_SHORTLIST*` could retarget), and whether `TRANSVERSE.CONFIG.5` (short-lived credentials) should also take `PIG-JS.DEPENDENCIES.PUBLISH.1`, now linked to `OWNERSHIP.LIFECYCLE.4` as planned.
- `DEFENSE-185` (JWT acceptance, claim SECGAP2-C03) left bare in the ledger: the target graph points its claim at `TRANSVERSE.CONFIG.1` while the rule lives on `CONSTRUCTION.BOUNDARY.2`.
- Two claim-less ledger rows (`VERIFICATION-044`, `-007`, coverage) and `DEFENSE-187` (claim SECGAP2-C23, not a claim pointer in the target graph) were assigned by topic: `ASSURANCE.BEHAVIOUR.6` and `CONSTRUCTION.DATA_NOT_CODE.4` (inferred).
- The software graph is uncommitted and under review: a uid change there breaks these links; `ig-tool validate -m` will show it.

## L3 full

### Files written

- `build/distill/skeleton.md` (two link tables, one convention line), `build/distill/claims_ledger.md` (66 rows, one note), `intent_graphs/` (`js_philosophy.ig.yaml`, `js_defaults.ig.yaml` rebuilt, `intent_resources.yaml`, `README.md`, `obsidian_export/` re-exported), this file.
- Read only: the software guideline's graph and manifest.

### Pinned results (verbatim)

Inter links created: 46 (js-philosophy 4, pig-js-defaults 42; inter links in the graphs: js-philosophy 15 (11 + 4), pig-js-defaults 110 (68 + 42)). Links still planned: 1.

```
ig-tool validate -g intent_graphs/js_philosophy.ig.yaml -m intent_graphs/intent_resources.yaml
status: ok / command: validate / nodes: 56 / links: 20 / errors: 0 / warnings: 0

ig-tool validate -g intent_graphs/js_defaults.ig.yaml -m intent_graphs/intent_resources.yaml
status: ok / command: validate / nodes: 287 / links: 162 / errors: 0 / warnings: 0

python3 build/assemble/check_complete.py   (last line)
FAILS: 0

python3 build/distill/check_ledger.py
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343
```

`check_complete.py` report: js-philosophy nodes 56, intra 20, inter 15; pig-js-defaults nodes 287, intra 162, inter 110.

### Mapping table (grounded: the link exists in the built graph; sentence as stored)

Source and target are qualified by graph; target names are those of the software graph.

| source uid | target uid | type | sentence |
|---|---|---|---|
| js-philosophy:`SUBSET.NUMBERS` | `CONSTRUCTION.STATE.4` (Value Precision and Mutability) | refines | One 64-bit binary float serves counts, identifiers and amounts, so the general limit on a numeric type's exactness is stated here as what breaks first in JavaScript. |
| js-philosophy:`SUBSET.STATE` | `CONSTRUCTION.STATE.4` (Value Precision and Mutability) | refines | A fixed binding is not a frozen value and a freeze is shallow and silent outside strict code, so the general distinction between immutable and restricted is only as deep as the JavaScript mechanism. |
| js-philosophy:`CONTRACTS.BOUNDARY` | `CONSTRUCTION.BOUNDARY.1` (Parse or Validate at the Edge) | refines | Types are erased and outside data arrives with no run-time type, so the parse at the boundary is the only place a value earns its shape. |
| js-philosophy:`DEFENSE.CODE` | `CONSTRUCTION.DATA_NOT_CODE.1` (Code and Commands) | refines | JavaScript has many doors from a string to running code, which makes the general rule never to build code from strings matter more here. |
| pig-js-defaults:`PIG-JS.CONTRACTS.SIGNATURE` | `CONSTRUCTION.BOUNDARY.5` (Call Shape and Evolvable Interfaces) | refines | Declared signatures realise shape of calls |
| pig-js-defaults:`PIG-JS.STRUCTURE.LOADING.1` | `CONSTRUCTION.STATE.5` (Load-Time Effects) | refines | Hoisting and run-once are the JavaScript mechanisms that make import order and repetition invisible only when the top level is effect-free. |
| pig-js-defaults:`PIG-JS.STRUCTURE.LOADING.5` | `CONSTRUCTION.STATE.5` (Load-Time Effects) | refines | Tools can drop unused code only when importing has no effect beyond exporting. |
| pig-js-defaults:`PIG-JS.STRUCTURE.SURFACE.1` | `CONSTRUCTION.HIDING.1` (Cut by Hidden Decision) | refines | A named export is one exposed name; a default export lets each importer rename it. |
| pig-js-defaults:`PIG-JS.STRUCTURE.SURFACE.2` | `CONSTRUCTION.HIDING.1` (Cut by Hidden Decision) | refines | Module-level form of the minimal public surface. |
| pig-js-defaults:`PIG-JS.STRUCTURE.PACKAGE.1` | `CONSTRUCTION.HIDING.1` (Cut by Hidden Decision) | refines | Package-level form of the minimal public surface. |
| pig-js-defaults:`PIG-JS.STRUCTURE.SURFACE.5` | `CONSTRUCTION.HIDING.1` (Cut by Hidden Decision) | refines | A class of static members is a procedural namespace pretending to be an object (inferred). |
| pig-js-defaults:`PIG-JS.STRUCTURE.DIRECTION.1` | `CONSTRUCTION.DEPENDENCY_DIRECTION.1` (No Cycles) | refines | The JavaScript rule behind the principle of one-way dependencies. |
| pig-js-defaults:`PIG-JS.STRUCTURE.DIRECTION.3` | `CONSTRUCTION.DEPENDENCY_DIRECTION.2` (Declared Layering) | refines | The JavaScript rendering of declared layering; this rule is undecided here and the principle is only inferred in the target. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION` | `CONSTRUCTION.DATA_NOT_CODE` (Keeping Data From Becoming Code) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.SECRETS` | `TRANSVERSE.CONFIG.1` (Separation of Configuration from Code and Secrets) | refines | The default renders the principle in JavaScript; this link covers its secrets-kept-out-of-code part, the target holds no statement on randomness, comparison or password storage (inferred). |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.2` | `CONSTRUCTION.DATA_NOT_CODE.1` (Code and Commands) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.3` | `CONSTRUCTION.DATA_NOT_CODE.2` (Queries) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.4` | `CONSTRUCTION.DATA_NOT_CODE.3` (Paths and Destinations) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.5` | `CONSTRUCTION.DATA_NOT_CODE.4` (Structured Payloads) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.6` | `CONSTRUCTION.DATA_NOT_CODE.3` (Paths and Destinations) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.SECRETS.5` | `TRANSVERSE.CONFIG.1` (Separation of Configuration from Code and Secrets) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.INSTALL.4` | `OWNERSHIP.SELECTION.5` (Authenticity, Provenance and Known Vulnerabilities at Adoption) | refines | An owned scope closes the namespace route that the identity check covers by hand. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.UPDATE.1` | `OWNERSHIP.LIFECYCLE.3` (Updating) | refines | The cooldown is the tool form of the update tradeoff. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.PUBLISH.1` | `OWNERSHIP.LIFECYCLE.4` (Channels, Mirrors and Supply-Chain Integrity) | refines | Short-lived CI credentials harden the publishing route. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.PUBLISH.2` | `TRANSVERSE.CONFIG.1` (Separation of Configuration from Code and Secrets) | refines | Reviewing tarball contents keeps secrets out of what consumers receive: no credential is recoverable from the shipped artifact. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` | `OWNERSHIP.STANCE.1` (What a New Dependency or Layer Must Earn) | refines | The framework is the largest case of a dependency earning its trust cost. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1` | `OWNERSHIP.STANCE.2` (Write, Adopt or Rent per Need) | refines | The platform is the built-in that meets the need first, and the platform baseline is the default candidate. |
| pig-js-defaults:`PIG-JS.VERIFICATION.TESTS.3` | `ASSURANCE.RULES.1` (Trustworthy Signal) | refines | Condition waits remove the largest flake category in asynchronous JavaScript tests (inferred transfer). |
| pig-js-defaults:`PIG-JS.VERIFICATION.LINT.3` | `ASSURANCE.RULES.2` (Placement and Feedback Speed) | refines | Security lint output is one analysis class among several, never the sole mechanism. |
| pig-js-defaults:`PIG-JS.RUNTIME.MEASURE.1` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | Profiling is the first concrete way a belief becomes a measurement. |
| pig-js-defaults:`PIG-JS.RUNTIME.MEASURE.2` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | Engine-level advice is held as a hypothesis until measured. |
| pig-js-defaults:`PIG-JS.RUNTIME.MEASURE.3` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | A speed-motivated API swap waits for a measured need. |
| pig-js-defaults:`PIG-JS.RUNTIME.METHOD.1` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | Many runs and a significance test make the distribution explicit. |
| pig-js-defaults:`PIG-JS.RUNTIME.METHOD.2` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | A controlled environment removes setup noise. |
| pig-js-defaults:`PIG-JS.RUNTIME.DIAGNOSE` | `ASSURANCE.PERFORMANCE.5` (Measurement Before Optimization) | refines | Diagnosis gathers the evidence that belief is not allowed to replace. |
| pig-js-defaults:`PIG-JS.CONTROL.PROCESS.2` | `CONSTRUCTION.PROCESS.2` (Fail Fast Under Supervision) | refines | Node's uncaughtException and uncaughtExceptionMonitor hooks render the designed process end; the principle and its single evidence row (CONTROL-078) are held once. |
| pig-js-defaults:`PIG-JS.DEFENSE.SECRETS.2.1` | `CONSTRUCTION.BOUNDARY.2` (What Counts as Valid) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.SECRETS.2.2` | `CONSTRUCTION.BOUNDARY.2` (What Counts as Valid) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.4.5` | `CONSTRUCTION.DATA_NOT_CODE.3` (Paths and Destinations) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.4.6` | `CONSTRUCTION.DATA_NOT_CODE.3` (Paths and Destinations) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.5.4` | `CONSTRUCTION.DATA_NOT_CODE.4` (Structured Payloads) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.HOST.3.1` | `CONSTRUCTION.DATA_NOT_CODE.4` (Structured Payloads) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.HOST.3.2` | `CONSTRUCTION.DATA_NOT_CODE.4` (Structured Payloads) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.5.3` | `CONSTRUCTION.DATA_NOT_CODE.4` (Structured Payloads) | refines | The default applies the principle's integrity-check and new-object rules, whose claims are held on the principle, to v8.deserialize. |
| pig-js-defaults:`PIG-JS.DEFENSE.INJECTION.6.4` | `CONSTRUCTION.DATA_NOT_CODE.3` (Paths and Destinations) | refines | The default renders the principle in JavaScript. |
| pig-js-defaults:`PIG-JS.DEPENDENCIES.SCREEN.3` | `OWNERSHIP.SELECTION.5` (Authenticity, Provenance and Known Vulnerabilities at Adoption) | refines | The default renders the principle in JavaScript. |
### Still planned

| source uid | principle (package) | type | sentence of the removed link | reason it stays planned |
|---|---|---|---|---|
| `PIG-JS.DEPENDENCIES.PUBLISH.3` | Publishing | refines | Shipping runnable JavaScript is part of being a good dependency. | The principle sent as "Publishing" is two-factor authentication on registry publishing accounts, held by `OWNERSHIP.LIFECYCLE.4`; no node of the software graph states that a package ships in a form its consumers' runtime can load, and the rule rests on one Node limitation on TypeScript (inferred). Any target would be invented. |

### Adjusted sentences (4 of 42) and retargeted links

| source uid | target | what changed and why (inferred) |
|---|---|---|
| `PIG-JS.DEFENSE.SECRETS` | `TRANSVERSE.CONFIG.1` | Original "The default renders the principle in JavaScript." now says the link covers the secrets-out-of-code part; the target has no statement on randomness, comparison or password storage. |
| `PIG-JS.DEPENDENCIES.PUBLISH.2` | `TRANSVERSE.CONFIG.1` (planned: Publishing, `OWNERSHIP.LIFECYCLE.4`) | Sentence now ends "no credential is recoverable from the shipped artifact", the target's wording; two-factor authentication on accounts does not support the original sentence. |
| `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1` | `OWNERSHIP.STANCE.2` (planned: Existing components first) | Sentence now "The platform is the built-in that meets the need first, and the platform baseline is the default candidate." |
| `PIG-JS.STRUCTURE.DIRECTION.3` | `CONSTRUCTION.DEPENDENCY_DIRECTION.2` | "undecided in both graphs" became "undecided here and only inferred in the target", which is the target's epistemic state. |

Retargeted without a sentence change: `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` to `OWNERSHIP.STANCE.1`; `PIG-JS.DEFENSE.SECRETS.2.1` and `.2.2` to `CONSTRUCTION.BOUNDARY.2`.

### Ledger annotation (optional step)

66 of 67 rows with the prefix "Owned by the software development guideline:" end with `(software-development-philosophy:<UID>)`. Source of each uid: the claim's impl_pointer in the target graph where present (`DEFENSE-002`), otherwise the package section of the claim and the node holding that section. Assigned by topic (inferred): `DEFENSE-187`, `VERIFICATION-044`, `VERIFICATION-007`. Left bare: `DEFENSE-185` (see L2, Open).

### Method notes

- The README's planned-links table (43 rows) was the source of source uids, principle names and sentences.
- Building: `build_batches.py` takes a qualified `dst` as written, so the new tables name `software-development-philosophy:<UID>` explicitly.
- The four philosophy links sit in the product graph `js-philosophy` and point out to another product graph, as the python-kb-philosophy links do.
