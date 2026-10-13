# Result: recheck of the sent and split principles for JavaScript emphasis

## L1 headline

Of the 56 principles sent to the software development guideline, 5 (in 4 restored nodes) meet the second criterion, "especially important in JavaScript", and came back as JavaScript-framed philosophy nodes linked to their general principle; the other 51 sent nodes and all 9 general parts stay sent. The philosophy graph has 56 nodes, both graphs validate clean and every gate passes. Certainty: counts and gates are grounded; each verdict is inferred by applying the criterion to claim level, node intent and the ledger rows of the defaults rules, and 7 borderline calls are open for the maintainer (listed in L2).

Pinned (grounded, counted by script or by the gates):
- Items restored with JavaScript emphasis: 5 of the 56 sent nodes, in 4 restored nodes: `SUBSET.NUMBERS` (Stated numeric limits), `SUBSET.STATE` (Distinguished immutability), `CONTRACTS.BOUNDARY` (Boundary contract, with `CONTRACTS.BOUNDARY.1` Validate at every trust boundary), `DEFENSE.CODE` (Strings never become code, formerly `DEFENSE.INJECTION.1`).
- Items left sent: 51 of the 56 sent nodes and all 9 general parts of split nodes (65 sent or split items checked; 4 nodes restored).
- Philosophy node count after: 56 (52 before this round; the defaults graph stays at 287).
- Claims moved back from `deferred`: 2 (`RUNSEC-C14` row `DEFENSE-007` as decision; `SECGAP2-C31` row `DEFENSE-188` as fact), both onto `DEFENSE.CODE`; 67 philosophy rows stay `deferred`; 700 claims, 700 placed, 0 dropped.
- Inter links re-created: 14 in all: 7 intentlinks inside `js-philosophy` (4 within branches, 3 across), 1 to `python-kb-philosophy` (`CONTRACTS.BOUNDARY` refines `DEFENSIVE`), 6 from the defaults graph (`PIG-JS.SUBSET.NUMBERS`, `PIG-JS.SUBSET.MUTATION.1`, `PIG-JS.CONTRACTS.BOUNDARY`, `PIG-JS.DEFENSE.INJECTION.1`, `.1.3`, `.1.4`). Planned links from the 4 restored nodes to the principles in the software development guideline: 5 principle names, listed in `intent_graphs/README.md` section 3 and in `kept_with_js_emphasis.md`; 43 other planned links stand.
- Validate, js-philosophy: `nodes: 56  links: 20  inter_links: 11  issues: 0  errors: 0  warnings: 0`.
- Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 68  issues: 0  errors: 0  warnings: 0`.
- `python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343
```
- `python3 build/assemble/check_complete.py`: `FAILS: 0` (js-philosophy: nodes 56, intra 20, inter 11, ledger_rows 121, claims_in_pointers 118, impl_pointers 118, constraints 22; pig-js-defaults: nodes 287, intra 162, inter 68, ledger_rows 578, claims_in_pointers 582, impl_pointers 582, constraints 381).

## L2 claims

- **Criterion applied (grounded as procedure, inferred per item).** An item is restored when JavaScript makes the principle matter more or fail differently, and the build holds a ground for that difference (a claim of level js-principle, or rows of the linked defaults rules). Language-general statements of the principle stay with the software guideline. Where no ground exists the item stays sent, even if the emphasis is plausible.
- **Restored, 4 nodes (inferred, grounded in rows named per node).** `SUBSET.NUMBERS`: one numeric type, a binary float, loses exactness silently (SUBSET-028 to -034, consensus). `SUBSET.STATE`: a binding is not a frozen value, a freeze is one level and silent outside strict code, sort mutates (SUBSET-009, -054, -055, -059, consensus). `CONTRACTS.BOUNDARY`: erased types make the boundary parse the only attestation (the maintainer's own example; the two sent nodes `CONTRACTS.BOUNDARY` and `.1` are covered by one node). `DEFENSE.CODE`: many string-to-code doors (RUNSEC-C14, consensus, MDN calls them injection sinks; SECGAP2-C31, single-source, template injection).
- **Stays sent (inferred).** 51 whole nodes and 9 general parts: positive validation, semantic checks, recognizer, shape of calls, process end, hiding, purity, direction, naming, paradigm, state in one place, injection classes other than code, secrets, sourcing and publishing, all of verification, measurement. Reasons per item are in L3.
- **Claims moved back (grounded).** `RUNSEC-C14` (level principle, but its text names the JavaScript sinks and its sources are MDN pages) and `SECGAP2-C31` (level js-principle) are placed on `DEFENSE.CODE`; the other deferred claims of the four principles (`LANG-C29`, `STRUCT-C66`, `TYPES-C27`, `TYPES-C29`) are language-general or web-architecture and stay deferred. `CONTRACTS.BOUNDARY`, `SUBSET.NUMBERS` and `SUBSET.STATE` therefore hold no claim of their own: they roll up their defaults rules (`unvalidated: inferred roll-up of ...`, same convention as the other roll-up nodes).
- **Epistemic state (grounded).** Each restored node carries `unvalidated: intent restated for JavaScript by the build, the general principle is owned by the software development guideline`. Parents `SUBSET`, `CONTRACTS` and `DEFENSE` had one clause added to their intent so the parent's boundary covers its new child; their epistemic states are unchanged.
- **Links (grounded as counts, inferred as to whether each sentence still holds).** Re-created with the original sentence where it still held: 7 intentlinks, 1 Python link, 6 defaults links (14). Not re-created: `DEFENSE.INJECTION.5` to `.1` and `DEPENDENCIES.TRUST.1` to `DEFENSE.INJECTION` (the other end stays sent), and the planned web-architecture link on server-side validation authority (that half stays deferred).
- **Open for the maintainer (inferred calls where the opposite is defensible).**
  - `CONTRACTS.SHAPE`: JavaScript has no named arguments, but no admitted claim says shape matters more here.
  - `STRUCTURE.PURITY`: tree shaking is a JavaScript-ecosystem driver, grounded only in one bundler's documented behaviour.
  - `DEFENSE.INJECTION.3`: operator injection through objects is a JavaScript-ecosystem failure; treated as covered by `CONTRACTS.BOUNDARY`.
  - `DEFENSE.SECRETS`: secrets shipped in client script would qualify, but no admitted source states it (gap named in the README).
  - `DEPENDENCIES.ADMISSION.1`, `VERIFICATION.STATIC_BASELINE.1`, `RUNTIME.MEASURE`: emphasis plausible, already carried by a kept node (`DEPENDENCIES.TRUST.1`, the narrowed `VERIFICATION`) or shared by every JIT-based language.
  - Restoring `RUNSEC-C14` here leaves the software guideline without it in the deferred list; the claim stays in its package for citing.
- **Files written (grounded).** `build/distill/skeleton.md` and `build/distill/claims_ledger.md` edited in place; `python3 build/assemble/apply_flags.py` printed `{} nodes changed: 0`; `intent_graphs/` rebuilt (`build_batches.py` ended with `"problems": []`), README updated, Obsidian vault re-exported with `export_to_obsidian.sh`; `kept_with_js_emphasis.md` and this file. `integrate.py` was not run; nothing in the software guideline's folder was written; no commit, no push.

Pinned (grounded, counted by script or by the gates):
- Items restored with JavaScript emphasis: 5 of the 56 sent nodes, in 4 restored nodes: `SUBSET.NUMBERS` (Stated numeric limits), `SUBSET.STATE` (Distinguished immutability), `CONTRACTS.BOUNDARY` (Boundary contract, with `CONTRACTS.BOUNDARY.1` Validate at every trust boundary), `DEFENSE.CODE` (Strings never become code, formerly `DEFENSE.INJECTION.1`).
- Items left sent: 51 of the 56 sent nodes and all 9 general parts of split nodes (65 sent or split items checked; 4 nodes restored).
- Philosophy node count after: 56 (52 before this round; the defaults graph stays at 287).
- Claims moved back from `deferred`: 2 (`RUNSEC-C14` row `DEFENSE-007` as decision; `SECGAP2-C31` row `DEFENSE-188` as fact), both onto `DEFENSE.CODE`; 67 philosophy rows stay `deferred`; 700 claims, 700 placed, 0 dropped.
- Inter links re-created: 14 in all: 7 intentlinks inside `js-philosophy` (4 within branches, 3 across), 1 to `python-kb-philosophy` (`CONTRACTS.BOUNDARY` refines `DEFENSIVE`), 6 from the defaults graph (`PIG-JS.SUBSET.NUMBERS`, `PIG-JS.SUBSET.MUTATION.1`, `PIG-JS.CONTRACTS.BOUNDARY`, `PIG-JS.DEFENSE.INJECTION.1`, `.1.3`, `.1.4`). Planned links from the 4 restored nodes to the principles in the software development guideline: 5 principle names, listed in `intent_graphs/README.md` section 3 and in `kept_with_js_emphasis.md`; 43 other planned links stand.
- Validate, js-philosophy: `nodes: 56  links: 20  inter_links: 11  issues: 0  errors: 0  warnings: 0`.
- Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 68  issues: 0  errors: 0  warnings: 0`.
- `python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343
```
- `python3 build/assemble/check_complete.py`: `FAILS: 0` (js-philosophy: nodes 56, intra 20, inter 11, ledger_rows 121, claims_in_pointers 118, impl_pointers 118, constraints 22; pig-js-defaults: nodes 287, intra 162, inter 68, ledger_rows 578, claims_in_pointers 582, impl_pointers 582, constraints 381).

## L3 full

### Verdict table, all 56 sent nodes (inferred by the criterion; the reason names the ground or its absence)

| uid | name in package.md | verdict | reason |
|---|---|---|---|
| `SUBSET.NUMBERS` | Stated numeric limits | restored | one numeric type, a binary float, for every count, identifier and amount; JSON round trips corrupt integers beyond the safe range (rows SUBSET-028 to SUBSET-034, consensus); node `SUBSET.NUMBERS`. |
| `SUBSET.STATE` | Distinguished immutability | restored | const fixes the binding not the value, freeze is one level and silent outside strict code, sort mutates in place (SUBSET-009, -054, -055, -059, consensus); node `SUBSET.STATE`. |
| `CONTRACTS.BOUNDARY` | Boundary contract | restored | types are erased, so the boundary parse is the only attestation (the maintainer's first example); node `CONTRACTS.BOUNDARY`, covers this node and `.1`. |
| `CONTRACTS.BOUNDARY.1` | Validate at every trust boundary | restored | same node `CONTRACTS.BOUNDARY`; the server-side authority half stays deferred to web-architecture. |
| `CONTRACTS.BOUNDARY.2` | Accept by positive rule | stays sent | allowlist validation is the same in any language; the JavaScript consequence (hostile keys, extra properties) sits on kept `DEFENSE.PROTOTYPE.1` and the defaults. |
| `CONTRACTS.BOUNDARY.3` | Check meaning as well as form | stays sent | semantic checks of related fields hold unchanged for any language. |
| `CONTRACTS.BOUNDARY.4` | Input handling is a recognizer | stays sent | recognizer theory is language-neutral; regular-expression stalls are on kept `DEFENSE.HOST.1` and `.2`. |
| `CONTRACTS.SHAPE` | Shape of calls | stays sent | open: JavaScript has no named arguments, but no admitted claim says arity or naming matters more here; the options-object rule is in `PIG-JS.CONTRACTS.SIGNATURE.1`. |
| `CONTROL.LIFECYCLE` | Process end is designed | stays sent | fail fast and an outside supervisor hold in any language; JavaScript failure channels are already on kept `CONTROL.FAILURE`, Node hooks in the defaults. |
| `STRUCTURE.HIDING` | Hide likely-to-change decisions | stays sent | Parnas information hiding, language-neutral. |
| `STRUCTURE.HIDING.1` | Decompose by hidden decisions | stays sent | language-neutral decomposition criterion. |
| `STRUCTURE.HIDING.2` | Abstract data type versus object | stays sent | conceptual distinction (Cook), source says no evidence for choosing in JavaScript. |
| `STRUCTURE.HIDING.3` | Minimal public surface | stays sent | the JavaScript emphasis (no privacy until hash-private fields) is already on kept `SUBSET.BINDING`; exposure levels are defaults rules. |
| `STRUCTURE.STATE.1` | One place per piece of state | stays sent | Codd redundancy and consistency, language-neutral. |
| `STRUCTURE.PURITY` | Effect-free importing | stays sent | open: import-time execution exists in other languages; the JavaScript part (tree shaking, `sideEffects`) rests on one bundler's behaviour the register forbids as ground. |
| `STRUCTURE.DIRECTION` | Dependencies flow one way | stays sent | language-neutral. |
| `STRUCTURE.DIRECTION.1` | No cycles between modules | stays sent | no own claim; the CommonJS partial-export behaviour is a defaults note, no ground that cycles matter more in JavaScript. |
| `STRUCTURE.DIRECTION.2` | Declared layering | stays sent | undecided, no admitted ground, language-neutral. |
| `STRUCTURE.NAMING` | Names carry the concept | stays sent | experiments on C# and others, language-neutral. |
| `STRUCTURE.NAMING.1` | Whole words | stays sent | experiment on C# developers. |
| `STRUCTURE.NAMING.2` | One concept one word | stays sent | holder positions of style guides. |
| `STRUCTURE.NAMING.3` | Name from the concept | stays sent | naming experiments, language not checked. |
| `STRUCTURE.PARADIGM` | Paradigm by intent | stays sent | defect-rate studies compare languages, not paradigms inside JavaScript. |
| `DEFENSE.INJECTION` | Data becoming instruction or location | stays sent | the family holds in any language; only its code-from-strings child meets the criterion and came back as `DEFENSE.CODE`. |
| `DEFENSE.INJECTION.1` | Strings never become code | restored | many string-to-code doors with the caller's privileges (RUNSEC-C14, SECGAP2-C31); node `DEFENSE.CODE`, new uid under `DEFENSE`. |
| `DEFENSE.INJECTION.2` | Commands are not built from input | stays sent | command injection is language-neutral; Node's `exec` facts are defaults. |
| `DEFENSE.INJECTION.3` | Queries keep code and data apart | stays sent | open: operator injection through objects is a type-confusion case that the restored `CONTRACTS.BOUNDARY` covers; parameterization is language-neutral. |
| `DEFENSE.INJECTION.4` | Paths stay inside their base | stays sent | path traversal is language-neutral. |
| `DEFENSE.INJECTION.5` | Serialized data carries no behaviour | stays sent | JSON is the safe default in JavaScript, so the principle matters less; pollution through keys is on kept `DEFENSE.PROTOTYPE`. |
| `DEFENSE.INJECTION.6` | Destinations are chosen by the server | stays sent | SSRF is language-neutral; undici redirect facts are defaults. |
| `DEFENSE.SECRETS` | Secrets and cryptographic primitives | stays sent | open: secrets shipped in client script would be a JavaScript emphasis, but no admitted source states it (listed under Not covered in the README). |
| `DEPENDENCIES.TRUST.3` | Layered controls | stays sent | defence in depth is language-neutral; the JavaScript reason (no containment) is on kept `DEPENDENCIES.TRUST.2`. |
| `DEPENDENCIES.ADMISSION.1` | Existing components first | stays sent | open: deep npm trees raise the cost, but that is the kept `DEPENDENCIES.TRUST.1` fact; sourcing is the software guideline's. |
| `DEPENDENCIES.ADMISSION.3` | Identity of the package | stays sent | typosquatting is registry-neutral; npm confusion mechanisms are on kept `DEPENDENCIES.THREATS.2`. |
| `DEPENDENCIES.ADMISSION.4` | Documentation examples are untrusted | stays sent | holds for any ecosystem. |
| `DEPENDENCIES.CHANGE.4` | Updates | stays sent | supply-chain practice, registry-neutral; cooldown evidence is single-source. |
| `DEPENDENCIES.CHANGE.5` | Incident response | stays sent | registry-neutral practice (CISA position). |
| `DEPENDENCIES.PUBLISH` | Publishing | stays sent | two-factor on any registry's publishing accounts; npm takeover facts are on kept `DEPENDENCIES.THREATS.1`. |
| `VERIFICATION.STATIC_BASELINE` | Static analysis baseline | stays sent | the JavaScript tie (a checked subset and a type layer hold only while a tool checks them) is already the intent of the narrowed `VERIFICATION`. |
| `VERIFICATION.TEST_SUITE` | Test suite | stays sent | language-neutral test policy. |
| `VERIFICATION.FAULT_DETECTION` | Fault detection power | stays sent | language-neutral. |
| `VERIFICATION.TEST_STABILITY` | Test stability | stays sent | studies mostly of Java projects. |
| `VERIFICATION.ENFORCEMENT` | Enforcement at the merge | stays sent | platform fact, language-neutral; the JavaScript tie is on `VERIFICATION`. |
| `VERIFICATION.STATIC_BASELINE.1` | Analysis switched on | stays sent | open: a linter is the only static pass JavaScript has by default, but that emphasis is already on `VERIFICATION` and on the `SUBSET` link to the defaults lint rules. |
| `VERIFICATION.STATIC_BASELINE.2` | Analysis beyond the compiler | stays sent | OpenSSF criterion, language-neutral. |
| `VERIFICATION.STATIC_BASELINE.3` | Checks complement each other | stays sent | 2015 web measurement and OpenSSF, language-neutral. |
| `VERIFICATION.TEST_SUITE.1` | Tests for new functionality | stays sent | OpenSSF criterion. |
| `VERIFICATION.TEST_SUITE.2` | Coverage finds, it does not judge | stays sent | study of Java suites. |
| `VERIFICATION.TEST_SUITE.3` | Test design | stays sent | Google testing guidance, single T3 source. |
| `VERIFICATION.FAULT_DETECTION.1` | Mutation testing | stays sent | language-neutral method. |
| `VERIFICATION.FAULT_DETECTION.2` | Property-based testing | stays sent | QuickCheck authors, language-neutral. |
| `VERIFICATION.TEST_STABILITY.1` | New tests are probed | stays sent | mostly Java studies; async waits are a general flake cause. |
| `VERIFICATION.TEST_STABILITY.2` | Shared state is cleaned | stays sent | Java-dominated study. |
| `VERIFICATION.TEST_STABILITY.3` | Flake rate tracked | stays sent | Google figures, single T3 source. |
| `RUNTIME.MEASURE` | Measurement before belief | stays sent | open: JIT engines make dated advice common, but any VM language shares this; the claim is about V8 posts as dated evidence, level principle. |
| `RUNTIME.METHOD` | Measurement method | stays sent | measured on Java and C, language-neutral. |

### Verdict table, the 9 general parts of split nodes (inferred)

| part | verdict | reason |
|---|---|---|
| Contracts (general part) | stays sent (parse half returned through `CONTRACTS.BOUNDARY`, call shape stays sent) | the part holds boundary parsing and call shape; the first returned as the node above, the second does not meet the criterion. |
| Structure for locality of change (general part) | stays sent | hiding, purity, direction, naming and paradigm: no item meets the criterion. |
| State in one place (general part) | stays sent | one place per piece of state is language-neutral. |
| Defense (general part) | stays sent (code half returned through `DEFENSE.CODE`) | injection family and secrets: only code from strings meets the criterion. |
| Two parsers must agree (general part) | stays sent | CR, LF and NUL in HTTP field values is a protocol rule, not a JavaScript one. |
| Dependencies (general part) | stays sent | sourcing, updates and publishing hardening are registry-neutral. |
| Admission (general part) | stays sent | need, identity and documentation checks are sourcing. |
| Verification (general part) | stays sent | everything except the tie to the checked subset, which the narrowed node holds. |
| Runtime behaviour (general part) | stays sent | measurement before belief and method are language-neutral. |

### What was written for each restored node (grounded)

| uid | parent | name | intent states | rows rolled up or placed | links created |
|---|---|---|---|---|---|
| `SUBSET.NUMBERS` | `SUBSET` | One number type, stated limits | one numeric type, a 64-bit binary float, shared by counts, identifiers and amounts; exactness beyond its limits from another representation | none of its own; rolls up `PIG-JS.SUBSET.NUMBERS` (SUBSET-028 to -034) | `PIG-JS.SUBSET.NUMBERS` refines it |
| `SUBSET.STATE` | `SUBSET` | Immutability is stated, not assumed | a value is locked only as far as its mechanism reaches; code states which guarantee it relies on | none of its own; rolls up `PIG-JS.SUBSET.MUTATION`, `PIG-JS.SUBSET.STRICTNESS.3` | requires `SUBSET.FAILURE`; required by `STRUCTURE.STATE.2`; `PIG-JS.SUBSET.MUTATION.1` refines it |
| `CONTRACTS.BOUNDARY` | `CONTRACTS` | Boundary parse is the only attestation | erased types and untyped outside data make the parse at every boundary the only place a value earns its shape | none of its own (`TYPES-C27`, `TYPES-C29` stay deferred); rolls up `PIG-JS.CONTRACTS.BOUNDARY` | requires `CONTRACTS.STATIC.1`; required by `CONTRACTS.STATIC.2`, `SUBSET.VISIBLE`, `DEFENSE`; refines `python-kb-philosophy:DEFENSIVE`; `PIG-JS.CONTRACTS.BOUNDARY` refines it |
| `DEFENSE.CODE` | `DEFENSE` | Strings become code in many ways | many doors from string to running code, all with the caller's privileges; a template is code | `DEFENSE-007` (decision, `RUNSEC-C14`), `DEFENSE-188` (fact, `SECGAP2-C31`) | `DEFENSE.PROTOTYPE.2` dataflow to it; `PIG-JS.DEFENSE.INJECTION.1`, `.1.3`, `.1.4` refine it |

Intent of parents widened by one clause: `SUBSET` ("silent loss of precision"), `CONTRACTS` ("only parsing that data at the trust boundary attests its shape"), `DEFENSE` ("or a string that is compiled and run").

### Planned links from restored nodes to the software development guideline (not created; graph not built yet)

`SUBSET.NUMBERS` refines "Stated numeric limits"; `SUBSET.STATE` refines "Distinguished immutability"; `CONTRACTS.BOUNDARY` refines "Boundary contract" and "Validate at every trust boundary"; `DEFENSE.CODE` refines "Strings never become code". Same list in `intent_graphs/README.md` section 3 and in `kept_with_js_emphasis.md`.

### Files and gates (grounded)

- Edited: `build/distill/skeleton.md` (4 node rows, 3 parent intents, 7 intentlinks, 1 Python link, 6 defaults inter links, a header note), `build/distill/claims_ledger.md` (2 rows, 2 header notes), `intent_graphs/README.md` (counts, section 3, planned table 49 to 43, Not covered, build note).
- Rebuilt: `intent_graphs/js_philosophy.ig.yaml`, `intent_graphs/js_defaults.ig.yaml`, `build/assemble/gen/` by `build_batches.py` and `build_graphs.sh`; vault `intent_graphs/obsidian_export/` re-exported.
- `python3 build/assemble/build_batches.py` ended with `"problems": []`, `"decision_nodes_without_record": []`, `"judge_records": 211`, `"planned": 12`, `"ledger_rows": 699`.
- Epistemic counts, philosophy (56 nodes): 21 `known` alone, 30 `known` with `unvalidated` or `conflict`, 5 `known` with another issue, 0 `risky`, 0 `undecided`.
- Not run: `integrate.py`, commit, push.

Pinned (grounded, counted by script or by the gates):
- Items restored with JavaScript emphasis: 5 of the 56 sent nodes, in 4 restored nodes: `SUBSET.NUMBERS` (Stated numeric limits), `SUBSET.STATE` (Distinguished immutability), `CONTRACTS.BOUNDARY` (Boundary contract, with `CONTRACTS.BOUNDARY.1` Validate at every trust boundary), `DEFENSE.CODE` (Strings never become code, formerly `DEFENSE.INJECTION.1`).
- Items left sent: 51 of the 56 sent nodes and all 9 general parts of split nodes (65 sent or split items checked; 4 nodes restored).
- Philosophy node count after: 56 (52 before this round; the defaults graph stays at 287).
- Claims moved back from `deferred`: 2 (`RUNSEC-C14` row `DEFENSE-007` as decision; `SECGAP2-C31` row `DEFENSE-188` as fact), both onto `DEFENSE.CODE`; 67 philosophy rows stay `deferred`; 700 claims, 700 placed, 0 dropped.
- Inter links re-created: 14 in all: 7 intentlinks inside `js-philosophy` (4 within branches, 3 across), 1 to `python-kb-philosophy` (`CONTRACTS.BOUNDARY` refines `DEFENSIVE`), 6 from the defaults graph (`PIG-JS.SUBSET.NUMBERS`, `PIG-JS.SUBSET.MUTATION.1`, `PIG-JS.CONTRACTS.BOUNDARY`, `PIG-JS.DEFENSE.INJECTION.1`, `.1.3`, `.1.4`). Planned links from the 4 restored nodes to the principles in the software development guideline: 5 principle names, listed in `intent_graphs/README.md` section 3 and in `kept_with_js_emphasis.md`; 43 other planned links stand.
- Validate, js-philosophy: `nodes: 56  links: 20  inter_links: 11  issues: 0  errors: 0  warnings: 0`.
- Validate, pig-js-defaults: `nodes: 287  links: 162  inter_links: 68  issues: 0  errors: 0  warnings: 0`.
- `python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343
```
- `python3 build/assemble/check_complete.py`: `FAILS: 0` (js-philosophy: nodes 56, intra 20, inter 11, ledger_rows 121, claims_in_pointers 118, impl_pointers 118, constraints 22; pig-js-defaults: nodes 287, intra 162, inter 68, ledger_rows 578, claims_in_pointers 582, impl_pointers 582, constraints 381).
