# JavaScript Guideline: Two-Graph Representation

This directory holds the **generic guideline IntentGraphs** for JavaScript, in the browser and in Node. Other
repositories reference them through their `intent_resources.yaml`; they do not keep local copies. The shape follows
the Python guideline ([../../python_guidelines/intent_graphs/README.md](../../python_guidelines/intent_graphs/README.md)):
product intent (what we believe) is kept apart from projection intent (how it is rendered in JavaScript), the
IntentGraph axiom P4.

Do not edit the graph files by hand. They are built by `ig-tool` from the build inputs (see the last section);
change the inputs and rebuild, or edit with `ig-tool node` / `ig-tool link`, which stamps provenance.

---

## 1. Philosophy graph (principles)

**File:** [js_philosophy.ig.yaml](js_philosophy.ig.yaml); graph id `js-philosophy`; root uid `ROOT`.

**Content:** 56 nodes in eight branches under one root ("Solid JavaScript"), kept to the principles core to JavaScript:
those that follow from its semantics, its runtime, its ecosystem or its threat surface, plus four general principles that
JavaScript makes matter more, stated as why (section 3 says what left, what came back and why). Each node states WHY: the principle, its force, what the evidence limits. Constraints hold the node's decision rows; design notes hold the sources
and rejected beliefs; impl pointers lead to the evidence.

| Branch uid | Principle | Nodes (philosophy / defaults) |
|---|---|---|
| SUBSET | Predictable subset | 7 / 35 |
| CONTRACTS | Contracts | 5 / 37 |
| CONTROL | Explicit control of time, failure and resources | 5 / 35 |
| STRUCTURE | Structure for locality of change | 3 / 34 |
| DEFENSE | Defense | 14 / 73 |
| DEPENDENCIES | Dependencies | 16 / 30 |
| VERIFICATION | Verification | 1 / 22 |
| RUNTIME | Runtime behaviour | 4 / 20 |

(The defaults count excludes the root; 1 + 286 = 287.)

**Links:** 13 within branches and 7 across branches (20 intentlinks); 11 inter links to the Python philosophy
(`python-kb-philosophy:*`), where a JavaScript principle specialises a shared one (for example `CONTROL.FAILURE`
refines `DEFENSIVE`). The `VERIFICATION` branch is a single node: its content is owned by the software development
guideline.

**Use when:** explaining why a JavaScript rule exists, resolving a conflict between two rules, or tracing a rule
back to a principle and its evidence.

---

## 2. Defaults graph (projection)

**File:** [js_defaults.ig.yaml](js_defaults.ig.yaml); graph id `pig-js-defaults`; root uid `PIG-JS.ROOT`; every
uid starts with `PIG-JS.` (as `PIG-PY.` in the Python defaults).

**Content:** 287 nodes in the same eight branches, one rule per leaf. Intents state the rule as intent (what and why,
not code). Constraints are the node's `decision` rows as MUST, MUST NOT or SHOULD NOT sentences, followed by its
`acceptable-when` rows as "Acceptable only when <condition>: <practice>". Design notes carry the judge record
(positions, forces, decision, rejected with the condition under which each would win).

**Links:** 90 within branches and 72 across branches (162 intentlinks); 111 inter links: 68 to `js-philosophy`
(each defaults node to the principle it renders, then cross-branch support) and 43 to `software-development-philosophy`
(each default to the principle, now owned by the software development guideline, that it renders in JavaScript). One
further link, to a principle in that guideline, is planned, not created (section 3).

**Use when:** writing or reviewing JavaScript, configuring linters, the type checker, the install and the CI gates,
or answering "how should we do X in JavaScript?".

**Certainty.** `epistemic_state` is carried from the skeleton. One rule for both graphs: a node whose rules rest on an inferred or open claim, on single-source claims only, on no claim of its own, or on a claim whose quote was not obtained carries `unvalidated: <why>`; a rule stronger than its source ("consider" kept as MUST, a holder position kept as MUST) says so there. Philosophy (56 nodes): 21 `known` alone, 30 `known` with `unvalidated` or `conflict`, 5 `known` with another issue (gap, missing, roll-up note), 0 `risky`, 0 `undecided` (the two `risky` nodes and the `undecided` one went to the software guideline). Defaults (287 nodes): 76 `known` alone, 179 `known` with `unvalidated` or `conflict`, 18 `known` with another issue, 4 `risky`, 10 `undecided` (the evidence that would settle each is named in [../build/distill/decisions_for_review.md](../build/distill/decisions_for_review.md)). Constraints are rules only (`MUST`, `MUST NOT`, `SHOULD NOT`, or "Acceptable only when"); facts, dated evidence and build bookkeeping are in design notes or in [../build/assemble/bookkeeping_log.md](../build/assemble/bookkeeping_log.md).

---

## 3. Sent to the software development guideline

The maintainer decided: "if they are core to js , keep them, else, send them to the other session". Rule per
philosophy node: KEEP if it follows from what JavaScript is (its semantics, runtime, ecosystem or threat surface);
SEND if it holds unchanged for any language; SPLIT if both, the JavaScript-specific part staying here. Of the 108 nodes
of the first build, 43 are kept, 56 sent and 9 split (the root and the eight branch nodes stay as the shared cut, their
intents narrowed where children left). The philosophy graph had 52 nodes after that cut. A second maintainer decision ("code-design should be part of the discussion, as long as it's true for all languages; if there are things specific to js or especially important in js, they can stay here") added a second criterion, *especially important in JavaScript* (JavaScript makes the principle matter more or fail differently); four of the sent principles meet it and came back as JavaScript-framed nodes (below). The philosophy graph has 56 nodes.

- **What went:** the general principles of contracts at run time (boundary parsing, call shape), structure (hiding,
  purity, direction, naming, paradigm), the injection family and secrets, the sourcing, update and publishing parts of
  dependencies, all of verification, and measurement method and measurement before belief; four of these came back as JavaScript-framed nodes (below).
- **Where it is:** [../build/handoff/to_software_guideline/package.md](../build/handoff/to_software_guideline/package.md)
  holds each sent node and each general part with its intent, constraints, design notes, epistemic state, claims (with
  sources, tier and restriction), the defaults rules that relied on it and its Python links. No claim was dropped: in
  `claims_ledger.md` the claims moved to a `deferred` row on the nearest kept node, the statement prefixed "Owned by the
  software development guideline:". The verdict of every node, with a reason, is in
  [../build/handoff/to_software_guideline/result.md](../build/handoff/to_software_guideline/result.md).
- **Links:** intentlinks inside the philosophy graph that touched a sent node were removed (35, of which 7 were re-created
  for the restored nodes); inter links from the defaults graph were retargeted to the nearest kept node where the sentence
  still holds (4) and otherwise removed (49, of which 6 were re-created to the restored nodes); inter links from sent nodes to
  the Python philosophy moved to the package (13, of which 1 was re-created).
- **Restored with JavaScript emphasis (4 nodes):** each states why the principle matters more in JavaScript, not the
  principle itself, which the software development guideline owns. Two claims moved back from `deferred` (RUNSEC-C14,
  SECGAP2-C31, both on `DEFENSE.CODE`); the language-general claims stay deferred. Everything else sent stays sent; the
  verdict of every sent or split item, with a reason, is in
  [../build/handoff/to_software_guideline/recheck/result.md](../build/handoff/to_software_guideline/recheck/result.md), and the list for
  the software guideline's session is [../build/handoff/to_software_guideline/kept_with_js_emphasis.md](../build/handoff/to_software_guideline/kept_with_js_emphasis.md).

| Restored node | Name | Why it matters more in JavaScript | Link (created): `refines` the principle in the software development guideline |
|---|---|---|---|
| `SUBSET.NUMBERS` | One number type, stated limits | one numeric type, a 64-bit binary float, for counts, identifiers and amounts | `CONSTRUCTION.STATE.4` (Value Precision and Mutability) |
| `SUBSET.STATE` | Immutability is stated, not assumed | a fixed binding is not a frozen value, a freeze is shallow and silent outside strict code, some array methods mutate | `CONSTRUCTION.STATE.4` |
| `CONTRACTS.BOUNDARY` | Boundary parse is the only attestation | types are erased, so the parse at the boundary is the only place a value earns its shape | `CONSTRUCTION.BOUNDARY.1` (Parse or Validate at the Edge) |
| `DEFENSE.CODE` | Strings become code in many ways | many doors from a string to running code (eval, Function, string timers, template engines, vm) | `CONSTRUCTION.DATA_NOT_CODE.1` (Code and Commands) |

- **Links to the software development guideline (created):** now that its graph `software-development-philosophy` has stable
  uids (it is listed in [intent_resources.yaml](intent_resources.yaml), path relative), 42 of the 43 defaults nodes that
  render a principle sent there link to the node that holds it, and the four restored nodes above `refines` theirs: 47 inter
  links, all of type `refines` (one default, the publishing-credentials rule, refines two targets: an
  ownership node and the short-lived-credentials node): the 42 defaults links keep the sentence of the removed link (4 adjusted to the target's
  wording), the 4 restored nodes get a sentence drawn from their "why it matters more" text. The links are in the skeleton
  tables "Inter links from ... to software-development-philosophy" ([../build/distill/skeleton.md](../build/distill/skeleton.md)); the
  mapping table, with the reason for each retargeting, is in
  [../build/handoff/to_software_guideline/links/result.md](../build/handoff/to_software_guideline/links/result.md).
- **Still planned (1, not created):**

| From | Rule | Principle in the package | Sentence of the removed link | Why no target |
|---|---|---|---|---|
| `PIG-JS.DEPENDENCIES.PUBLISH.3` | Ship JavaScript | Publishing | Shipping runnable JavaScript is part of being a good dependency. | the principle sent as Publishing is two-factor authentication on registry publishing accounts (OWNERSHIP.LIFECYCLE.4 holds it); no node of the software graph states that a package ships in a form its consumers' runtime can load, and the rule rests on one Node limitation on TypeScript (inferred), so any target would be invented |

---

## Mapping at a glance

| Build layer | IntentGraph | File |
|---|---|---|
| Distilled principles (`build/distill/skeleton.md`, js-philosophy part) | Philosophy (product) | [js_philosophy.ig.yaml](js_philosophy.ig.yaml) |
| Distilled rules (`build/distill/skeleton.md`, pig-js-defaults part) | Defaults (projection) | [js_defaults.ig.yaml](js_defaults.ig.yaml) |
| Claims ledger (`build/distill/claims_ledger.md`, 699 rows, 700 claims; 67 philosophy rows are `deferred` to the software development guideline) | `constraints`, `design_notes`, `impl_pointers` of the node each row names | both |
| Research slots (`build/research/<slot>/result.md`) | `impl_pointers`, one per claim: `build/research/<slot>/result.md::<CLAIM-ID>` | both |

Row roles map as follows: `decision` to a MUST constraint; `acceptable-when` to an "Acceptable only when" constraint;
`rejected` rows with claims to a "Rejected" line of `design_notes`, claim-less `rejected` (folklore) rows to a
"Rejected beliefs" line and never to `impl_pointers`; `fact` and `deferred` rows to "Fact" and "Deferred" lines. Every
claim of every row is listed in `impl_pointers`.

## Manifest

[intent_resources.yaml](intent_resources.yaml) lists the product graph `js-philosophy`, the projection target
`javascript` with `pig-js-defaults`, and `python-kb-philosophy` and `software-development-philosophy` (relative paths to
their graph files) so that the inter links resolve. The software graph belongs to a sibling guideline and is read only. Validate with the manifest:
`ig-tool validate -g js_defaults.ig.yaml -m intent_resources.yaml`.

## Obsidian view

`./export_to_obsidian.sh` exports both graphs into one vault, `obsidian_export/`, one folder per
graph; see [obsidian_export/README.md](obsidian_export/README.md). The vault is a generated,
read-only projection: edit the graph files, then re-export.

## Not covered

The second security gap round (token and JWT verification, XML external entities, header and CRLF injection, server-side template injection, file uploads, typosquatting, CSRF and clickjacking) is folded in, with rules where the admitted sources ground them. What the round could not ground stays open, as `undecided` nodes or as `Open:` fact rows:

- Which JavaScript XML parsers resolve external entities by default, and the options that turn this off (the rule is language-neutral; no Node parser default is grounded).
- A typosquatting screening procedure for adding a dependency (`PIG-JS.DEPENDENCIES.SCREEN.3` is `undecided`; the repository-provenance rule is decided).
- Injection rules for template engines other than Handlebars and EJS, and a JavaScript content-signature check for uploads.
- Specific URL parser differentials (the validation rule is decided without examples).
- The Node path-containment recipe (`PIG-JS.DEFENSE.INJECTION.4.4` is `undecided`: the symlink-resolving call and the separator-aware comparison have no admitted source; the grounded pieces are on `INJECTION.4.1`).
- Secrets that ship inside client-side script (bundles, source maps, build-time variable inlining): no admitted source states it, so the sent principle on secrets has no JavaScript-emphasis node here; a further research round would be needed to restore one.
- Whether `v8.deserialize` is safe for untrusted bytes (the rule applies the general deserialization rules and claims no more).
- Node's own documentation of how `fetch` handles `redirect: "manual"` (the rule rests on undici's code, which returns the actual response, not on a Node page; the Fetch Standard's opaque-redirect response is browser behaviour) and which undici version a release bundles (`process.versions.undici` gives it).

## Out of scope: the software development guideline

Concerns of any software project, whatever its language, belong to a separate software development guideline (planned): sourcing (what to build versus take, finding and judging libraries), application architecture, validating that the product works for its users, deploy, operations and monitoring, and the development process. This guideline holds only their JavaScript-specific rules (for example the dependency and framework nodes under `PIG-JS.DEPENDENCIES`, and the test tooling under `PIG-JS.VERIFICATION`). The language-general principles that its philosophy graph first held were sent to that guideline (section 3); its overlaps are inter links here (section 3), not copies.

## Planned boundary links (not created)

The web-architecture guideline owns content that these defaults nodes only touch. Its graphs `web-app-philosophy` and
`pig-web-defaults` do not exist yet, so the 12 links below are planned, with target uids to be chosen when they do.
They are not in either graph. (A thirteenth, from the philosophy node `CONTRACTS.BOUNDARY.1` on server-side validation authority, left with that node; it is in the package.)

| # | From | To graph | Content owned there |
|---|---|---|---|
| 1 | `PIG-JS.DEFENSE.DOM.4` | `pig-web-defaults` | code half here, CSP header and policy deployment in web_architecture (DOMSEC-C15, FW-C48) |
| 2 | `PIG-JS.DEFENSE.ORIGIN.4` | `pig-web-defaults` | token and session architecture in web_architecture (DOMSEC-C35) |
| 3 | `PIG-JS.DEFENSE.ORIGIN.5` | `pig-web-defaults` | CSP deployment, JSONP, CORS and framework CSP and CSRF options in web_architecture (DOMSEC-C26, C28, C29, C59, C60, FW-C04, FW-C14) |
| 4 | `PIG-JS.DEFENSE.INJECTION.6.1` | `pig-web-defaults` | cloud metadata service configuration in web_architecture (SRVSEC-C38) |
| 5 | `PIG-JS.DEFENSE.HOST.3` | `pig-web-defaults` | front-end proxy normalization is deployment, with the Node parser side kept here (SRVSEC-C58) |
| 6 | `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` | `pig-web-defaults` | rendering strategy (SPA, server HTML, hypermedia) decides which candidate fits; owned by web-architecture |
| 7 | `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4` | `pig-web-defaults` | FW-C44 (usage by rendering strategy, deferred) and FW-C45 (CSP and SRI prevalence) |
| 8 | `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5` | `pig-web-defaults` | FW-C07 and FW-C13 (framework advisories, update policy of server rendering) |
| 9 | `PIG-JS.CONTROL.PROCESS.4` | `pig-web-defaults` | the Node side of shutdown (signal listener, server close) and the external supervisor of PROCESS.2 serve the shutdown contract that the web-architecture guideline owns |
| 10 | `PIG-JS.DEFENSE.ORIGIN.2.1` | `pig-web-defaults` | response header deployment of frame-ancestors and the CSP policy around it in web_architecture (SECGAP2-C63, C64) |
| 11 | `PIG-JS.DEFENSE.ORIGIN.6.3` | `pig-web-defaults` | cookie attribute design and session architecture beside SameSite in web_architecture (SECGAP2-C61) |
| 12 | `PIG-JS.DEFENSE.SECRETS.2.1` | `pig-web-defaults` | token revocation, logout and session design in web_architecture (SECGAP2-C16) |

## How the graphs were built

Generated by `ig-tool` from the build inputs in `../build/assemble/` (the software-guideline split and the later restoration of four JavaScript-framed nodes edited `../build/distill/skeleton.md` and `../build/distill/claims_ledger.md` directly, then ran `apply_flags.py`, `build_batches.py`, `build_graphs.sh` and the checks): `build_batches.py` writes the batch files,
`build_graphs.sh` runs `ig-tool init`, `ig-tool apply --batch` and `ig-tool link create` (inter links are created one
by one, since batch `link.create` does not dispatch qualified endpoints), `apply_review_fixes.py`, `apply_review_fixes_2.py` and `apply_flags.py` record the one-time stage 7 corrections and the `unvalidated` flags, `../build/patch/14_secgap2/apply_patch.py` is the one-time fold of the second security gap round, and `check_complete.py` checks every skeleton
node, ledger claim and link against the result. One step uses the IntentGraph library instead of the CLI: the tree
of the defaults graph, because `ig-tool` rejects the `PIG-JS.*` uids under a root that is not `ROOT` (see the
docstring of `apply_tree.py`).
