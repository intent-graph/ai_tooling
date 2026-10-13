# Decisions for review (stage 5c)

The maintainer can overrule any of these; each states the decision, the rejected positions with the condition under
which each would win, and the grounds. Order: decisions made at integration, then the eight branches' decisions in
branch order, then the undecided nodes with the evidence that would settle each. The branch texts are unchanged except
that headings are prefixed with the branch keyword (the branches reuse `D1`, `D2`).

## Decisions made at integration

These are the choices made while joining the eight branches. Rows named in the branch texts below as `CONTROL-011` and
`DEFENSE-091` now live in `CONTROL-078` and `SUBSET-051` (I1, I2). Provenance of every link: `5c_integrate/link_resolution.md`.

### I1. Process-end principle: one row, principle kept as intent (P5 merge, flagged by CONTROL)

- Decision: the rows `CONTROL-011` (ASYNC-C05, philosophy node `CONTROL.LIFECYCLE`) and `CONTROL-078` (RUNTIME-C37, defaults node
  `PIG-JS.CONTROL.PROCESS.2`) state one principle (overlap O02: after an uncaught exception the state is undefined, so clean up
  synchronously, end, and let a supervisor restart). They are merged into `CONTROL-078` with both claim ids. `CONTROL.LIFECYCLE` keeps the
  language-neutral principle as intent and no row of its own; `PIG-JS.CONTROL.PROCESS.2` now states only the Node rendering and links up
  with a `refines` inter link.
- Rejected: leaving both rows (the principle is stated twice); putting the merged row on `CONTROL.LIFECYCLE` (the statement names the Node
  hooks, so it fails the language-swap test). Wins: the second, if the maintainer wants every principle node to carry its own evidence;
  then move `CONTROL-078` to `CONTROL.LIFECYCLE` and restore the old intent of `PROCESS.2`.
- Grounds: both claims cite the same single T1 source (SRC-082, unrestricted). Epistemic state unchanged: `known | unvalidated: single T1 source`.

### I2. Own-property read: one rule on the owner node (P5 merge, found at integration)

- Decision: `SUBSET-051` (LANG-C55) and `DEFENSE-091` (RUNSEC-C07) both decide `Object.hasOwn` over `hasOwnProperty` and no `for...in` on
  untrusted keys (overlap O15, owner LANG-C55). Merged into `SUBSET-051` on `PIG-JS.SUBSET.OBJECTS.6` with both claim ids and
  agreement `consensus` (RUNSEC-C07 has two T1 grounds, SRC-078 unrestricted for slot 06 and SRC-139). `PIG-JS.DEFENSE.PROTOTYPE.1` keeps the
  nested-write, merge and `__proto__` rules and links to `OBJECTS.6` with `requires`.
- Rejected: keeping the rule in both nodes; moving it to DEFENSE (SUBSET also applies it to trusted keys). Wins: DEFENSE as owner if the
  guideline is read as two standalone documents; then restore `DEFENSE-091` and drop the merge.

### I3. Shared facts linked, not merged (P5 by link)

- Held once, linked from the other node: the run-once fact of ES modules (`PIG-JS.SUBSET.STRICTNESS.2`, linked from
  `PIG-JS.STRUCTURE.LOADING.1`); the shallow-freeze fact (hub `PIG-JS.SUBSET.MUTATION.1`, linked from `PIG-JS.STRUCTURE.SURFACE.3` and
  `PIG-JS.DEFENSE.PROTOTYPE.3`); framework security facts (held in `PIG-JS.DEFENSE.DOM.6`, linked from
  `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE` and `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`, as the CONTROL, DEFENSE and DEPENDENCIES
  branches proposed); secrets in package contents (`PIG-JS.DEPENDENCIES.PUBLISH.2` requires `PIG-JS.DEFENSE.SECRETS.5`); the single shared
  thread (`DEFENSE.HOST.1` requires `CONTROL.SCHEDULING`); type check as evidence not proof (`CONTRACTS.STATIC.2` refines
  `VERIFICATION.STATIC_BASELINE.3`).
- Kept as a conflict, not merged: built-ins (`PIG-JS.SUBSET.OBJECTS.5` conflicts `PIG-JS.DEFENSE.PROTOTYPE.3`): two purposes (predictable
  language, hardening) disagree on one practice, scope separates them.
- Rule applied: merge when two nodes state the same intent; link when two nodes share a fact. The rows are evidence and stay in place.
- Residue at statement level, left as written: `DEFENSE-097` repeats the refuted deep-freeze belief that `SUBSET-056` rejects, and
  `STRUCTURE-024` repeats the run-once fact of `SUBSET-006` inside a rule about repeatable work.
- Cross-branch text similarity of the 589 branch rows peaks at 0.22 (token Jaccard): no other duplicated statement exists.

### I4. DEFENSE.INJECTION is not split

- Decision: `DEFENSE.INJECTION` (philosophy) and `PIG-JS.DEFENSE.INJECTION` (defaults) stay one L2 node each, six L3 classes below.
- Why the split is not clean: the natural cut is INSTRUCTION (strings as code, commands, queries, serialized data: 34 claims, plus 3 on the
  defaults L3 node) against LOCATION (paths, destinations: 24 claims). It would make DEFENSE seven L2 children in both graphs, over the
  limit of six; renumber the nodes of 61 claims, the INJECTION inter links, three undecided uids (`INJECTION.4.4`, `.5.3`, `.6.4`) and the judge records; and class 5 (serialized data)
  sits on the boundary (revived behaviour, but also a format that crosses a boundary). No class is large: claims per class are 10, 4, 13, 12, 7, 12.
- Rejected: the split. Wins: if the maintainer folds PROTOTYPE (14 claims) into one of the two halves to stay at six L2 children, or accepts seven.
- Grounds: grounded for the counts (ledger), inferred for the cleanliness judgment.

### I5. T3 relabel and what was checked

- Relabelled `known | unvalidated: single T3 source` to `risky | unvalidated: single T3 source`: `PIG-JS.STRUCTURE.LOADING.6` (barrel files,
  SRC-315 measurement; the T1 MDN page documents aggregation and recommends nothing), `PIG-JS.STRUCTURE.DIRECTION.2` (SRC-313, the rule's
  own documentation), `VERIFICATION.TEST_SUITE.3` (SRC-321), `VERIFICATION.TEST_STABILITY.3` (SRC-320).
- Checked against `build/audit/source_register.md` (11 T3 sources) and not relabelled, because a T1 or T2 ground sits beside the T3 one:
  `PIG-JS.DEFENSE.DOM.2.2` (ASVS requirement is T1, only the mechanism is T3), `PIG-JS.DEFENSE.ORIGIN.4`, `PIG-JS.STRUCTURE.SURFACE.3`,
  `STRUCTURE.NAMING.2` (T2 grounds), `PIG-JS.DEFENSE.INJECTION.4.2`, the SUBSET nodes that cite Airbnb beside MDN or ESLint.
- The tension the STRUCTURE branch noted (the plan says T3 alone never makes a node `known`, the brief's format would allow it) is closed by the
  5c rule: the four nodes are `risky`.

### I6. Cross-branch links: 101 proposals resolved

- 72 retargeted to a uid, 10 flipped (the sentence made the proposer the dependent), 2 retyped (CONTRACTS Q11 and Q12, `refines` and `requires`
  became `dataflow`), 9 mirror proposals folded into another link, 6 dropped as moot, 2 turned into planned boundary links. 83 links result from them
  (13 philosophy, 68 defaults, 2 defaults-to-philosophy); 3 more were added at integration (2 philosophy, 1 defaults-to-philosophy: I1, I3).
- Corrections to proposals that rested on a wrong premise: CONTRACTS Q6 (SUBSET lists no enum or namespaces), Q13 (DEFENSE lists no
  mass-assignment node), CONTROL 8 (the API-shape cluster is in `PIG-JS.CONTRACTS.SIGNATURE`, not in STRUCTURE).
- Open, grounded as gaps in the target trees: VERIFICATION defaults hold no tool-neutral gate node, so the type-check, audit, secret-scan and bundling
  gates all point at `PIG-JS.VERIFICATION.LINT.2` (coarse); RUNTIME holds no node on the Node release lifecycle; no DEFENSE node on mass assignment.

### I7. Shape of the trees

- Every node has zero or two to six children, except the two roots (eight L1 branches, given) and seven defaults nodes with a single child:
  `PIG-JS.CONTROL.PROMISES.4`, `PIG-JS.CONTROL.ERRORS.2`, `PIG-JS.CONTROL.SCHEDULING.2`, `PIG-JS.DEPENDENCIES.UPDATE.1`,
  `PIG-JS.DEPENDENCIES.UPDATE.3`, `PIG-JS.RUNTIME.MEMORY.6` (each holds an undecided sub-question as its only child, kept visible on purpose) and
  `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` (its one child is the platform baseline; the four frameworks sit in the parent's decision).
- Decision: kept as written. Alternative for the assembly step: one node per short-list candidate under `FRAMEWORK_SHORTLIST`, grounded in
  rows DEPENDENCIES-048 to DEPENDENCIES-075.

### I8. Conventions normalized

- DEFENSE and DEPENDENCIES wrote the IG separator as a bare `|` in epistemic cells and DEFENSE abbreviated ledger rows (`028-034`): cells
  rejoined with `\|`, the ledger-rows column derived from the merged ledger for every node (the branch columns agreed with the ledger everywhere).
- Link ids that looked like node uids (`P1`, `Q1`, `X1`, `I1`) are plain numbers; the checker would count them as nodes. RUNTIME's `graph:uid`
  prefix on link sources is dropped; defaults-to-philosophy targets all carry `js-philosophy:`.
- Judge records are copied in the layout each branch used (bold records, headed records, tables); only headings are demoted.

### I9. Stage 7 review fixes (decisions of the maintainer's orchestrator, applied to ledger, skeleton and graphs)

The maintainer's standing rule is max, not average; a source that suggests a practice grounds the practice, its strict form may be chosen,
and the weakness is shown in `epistemic_state`. What changed:

- `PIG-JS.DEFENSE.INJECTION.2`: no shell command string from untrusted input, sanitized or not (argument arrays only); stronger than Node's sentence, flagged inferred.
- `PIG-JS.CONTRACTS.STRICT.2`, `STRICT.3`, `PIG-JS.DEFENSE.SECRETS.5`: MUST kept, flagged "source says consider".
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`: the gates A, B, C and the platform-first default are now constraints (rows added), state `risky`, flagged as the build's judgment. The gates remain without an admitted source.
- `PIG-JS.DEFENSE.SECRETS.4`: flagged (Node crypto text read in v6 docs only; the current page could not be re-read).
- `PIG-JS.CONTRACTS.LAYER.1`: decision stated as a condition table (TypeScript when a build or type-check step can be adopted; JSDoc-checked JavaScript otherwise), state `risky`.
- `PIG-JS.DEFENSE.SECRETS.2` (authenticated encryption) and `PIG-JS.CONTROL.ERRORS.2` (empty catch) move from acceptable-when to MUST, flagged single-source or holder position.
- `VERIFICATION.TEST_SUITE.2`: SHOULD NOT gate on a coverage number; the OpenSSF position (cover most branches) is recorded as the rejected position.
- `DEPENDENCIES.THREATS.1` softened to what four incidents show; `PIG-JS.DEPENDENCIES.UPDATE.3`: the lockfile and triage rules stay MUST, running npm audit as the check is acceptable-when.
- `PIG-JS.CONTRACTS.ESCAPE.6` and `PIG-JS.VERIFICATION.LINT.1.2` agree: ban-ts-comment is the one override of the recommended set.
- `PIG-JS.DEFENSE.INJECTION.5.2` (node-serialize rule, "if js-yaml" wording) and `INJECTION.6.1` (allowlist constraint) completed.
- Framework-specific and dated facts moved from rules to dated-evidence rows (DOM.6.1, UPDATE.2, FRAMEWORK_EVIDENCE.1, DOM.4, EVOLUTION.2).
- Philosophy rows tool-neutral (VERIFICATION.ENFORCEMENT, DEPENDENCIES.CHANGE.2, DEPENDENCIES.EVIDENCE.1, DEFENSE.INJECTION.1, CONTRACTS.STATIC.2); the names moved to linked defaults nodes.
- Every node whose rules rest on inferred or open claims, on single-source claims only, on no claim, or on a claim with no obtained quote carries `unvalidated:` (script `build/assemble/apply_flags.py`).
- Re-judged under the corrected rule (best, not most demanding): `STRICT.2`, `STRICT.3`, `SECRETS.5`, `ESCAPE.6` and `FRAMEWORK_SHORTLIST` above were relaxed; the decisions above that name them are superseded by section "Re-judged under best (24 rules)".

## Slot 14_secgap2: second security gap round (90 claims folded by patch)

Folded by `build/patch/14_secgap2/apply_patch.py` (never by `integrate.py`). Every claim is placed once: 92 of 92, 0 dropped (90 at the fold, C91 and C92 added at the review fixes). Rules
follow the fix conventions: constraints are rules only, facts go to design notes, single-source, inferred or open grounds carry
`unvalidated:`, and the philosophy graph names no JavaScript tools. Where every step of a rule is grounded by a claim, the rule is composed
and marked `known | unvalidated: inferred from <claims>`; where a step has no ground the node stays `undecided` with what is missing.

### G1. Placement under the six-child limit (weighty, inferred)

- Decision: no new L2 node under `PIG-JS.DEFENSE` (it already has six: DOM, ORIGIN, INJECTION, PROTOTYPE, SECRETS, HOST; I4 and A1 hold that
  seven is over the limit). The new topics sit under the nearest existing parent that has room: tokens under `SECRETS.2` (`.2.1`, `.2.2`),
  template injection under `INJECTION.1` (`.1.3`, `.1.4`), uploads under `INJECTION.4` (`.4.5`, `.4.6`, the sixth child is now full), XML
  under `INJECTION.5` (`.5.4`), header injection under `HOST.3` (`.3.1`, `.3.2`), clickjacking under `ORIGIN.2` (`.2.1`, `.2.2`), CSRF as the sixth
  child `ORIGIN.6` with three children, typosquatting under `DEPENDENCIES.SCREEN` (`.3`) and the repository inventory under `INSTALL` (`.5`).
  Philosophy: no new node; principle-level claims (C03, C18, C23, C31, C49, C59) became rows of `DEFENSE.SECRETS`, `DEFENSE.INJECTION.5`,
  `DEFENSE.HOST.3`, `DEFENSE.INJECTION.1`, `DEPENDENCIES.THREATS.2` and `DEFENSE.ORIGIN`, whose intents gained one clause where the new row needed it. At the review fixes the defaults intents of `INJECTION.1` (template engines) and `INJECTION.5` (XML external entities) were widened the same way, and `SECRETS.2` was renamed "Cryptographic APIs and tokens" with its intent widened to token verification, so the children no longer extend their parents.
- Rejected: a seventh L2 `DEFENSE` child (for example `PROTOCOL`) holding tokens, headers and CSRF: cleaner by topic, but over the limit and
  it would split the tree again. Wins if the maintainer accepts seven L2 children or folds PROTOTYPE (3 children) elsewhere.
- Grounds: inferred (a judgment on cohesion). Placement of tokens under `SECRETS` and CSRF under `ORIGIN` is the weakest fit.

### G2. Nodes resolved from `undecided` (three decided, one kept)

- `PIG-JS.DEFENSE.DOM.2.3` (URL validation): decided. Steps all grounded: parse with the WHATWG URL API (C70, DOMSEC-C57), compare parsed scheme, host and port
  with an allowlist and reject userinfo and prefix matching (C71), refuse javascript: and data: (C73, which closes the former gap), parser agreement (C74, inferred). Marked
  `known | unvalidated: inferred from DOMSEC-C57, SECGAP2-C70, C71, C73 and C74`. Open: parser differential examples (C75).
- `PIG-JS.DEFENSE.INJECTION.5.3` (v8.deserialize): decided on the general rule only. No source says whether the function is safe (C85), so the rule applies the
  deserialization principle (integrity check first, new object from validated fields; SRVSEC-C45, RUNSEC-C44, which stay on the philosophy node `DEFENSE.INJECTION.5` and are reached through the link between the two) and claims nothing more. The MUST NOT is the strict form of sources that say could or if available (CWE-502, OWASP), flagged `unvalidated`. Rejected: a ban (no source), a safe label (no source).
- `PIG-JS.DEFENSE.INJECTION.6.4` (fetch redirects): decided: redirect `error` or `manual` with revalidation, Node kept current (the built-in fetch bundles undici), header stripping not relied on (C86 to C91, SRVSEC-C35 to C37).
  Review fix: the Fetch Standard gives `manual` an opaque-redirect response whose Location cannot be read, so the first basis (inference from the Standard) pointed the wrong way; undici's code returns the actual response for `manual` (C91, SRC-402), which makes revalidating each Location target workable in Node. The opaque response is browser behaviour (stated on `INJECTION.6.3`). Flagged: single-source code facts at an unpinned commit; Node documents none of it. The redirect rule now has one owner, `INJECTION.6.4` (it absorbed SRVSEC-C35 and C36); `INJECTION.6.3` keeps the browser-behaviour fact only.
- `PIG-JS.DEFENSE.INJECTION.4.4` (Node containment recipe): stays undecided. The steps with a ground (never a raw prefix test, resolve lets an absolute input replace the base, normalize is lexical,
  canonicalize before comparing) are placed on `INJECTION.4.1`; the symlink-resolving Node call and the separator-aware test have none (C82; the Node fs `realpath` and `O_NOFOLLOW`
  entries could not be read). Settled by: a readable Node fs `realpath` entry plus a source stating the comparison, for example the hapi fix commit (late candidate LC-01).
  Note: the task named SRVSEC-C44 to C46 among the containment grounds; they are the deserialization claims and ground node 5.3, not 4.4.

### G3. Contested topic: X-Frame-Options beside frame-ancestors (C68; node `ORIGIN.2.1`)

- Decision (max rule): `frame-ancestors` on every response as a header, plus an `X-Frame-Options` fallback (`DENY` or `SAMEORIGIN`) only where it states the same policy; omit it where other origins are allowed.
- Positions: OWASP Clickjacking sheet: frame-ancestors preferred, X-Frame-Options also listed for older browsers; MDN Clickjacking (SRC-378): send X-Frame-Options as well, for browsers without frame-ancestors; ASVS 3.4.6: requires frame-ancestors and is silent on a fallback; CSP3 and RFC 7034: the directive supersedes the header.
- Rejected: frame-ancestors alone, which wins where every supported browser implements the directive; X-Frame-Options alone, which loses to the directive and cannot name allowed framers (ALLOW-FROM unsupported, C67).
- Epistemic: `known | conflict: frame-ancestors alone (ASVS requires the directive and is silent on a fallback; CSP3 with RFC 7034 hold that the directive supersedes) | unvalidated: matching-policy condition inferred from C67`. The max rule is supported by OWASP and MDN.

### G4. CSRF primary defence (C69; node `ORIGIN.6.1`), no longer a contested topic

- Decision (max rule): a synchronizer or signed double-submit token is the primary defence; the Sec-Fetch-Site check (same-origin; same-site only when the threat model trusts sibling subdomains, OWASP) and the Origin or Referer fallback are layers behind it; the token is unique per session, random, never in a URL, a GET request or a log (C92), compared in constant time.
- Positions (corrected at the review fixes): OWASP and MDN both list a Fetch Metadata check among the primary defences (OWASP: its own section before "Defense In Depth Techniques"; MDN: the third primary-defence bullet); neither says it suffices alone and neither requires a token beside it. The earlier record that OWASP layers it as defence in depth was a misreading, so there is no conflict between the sources.
- Rejected: Sec-Fetch-Site alone, kept as an `acceptable-when` row (every supported browser sends the header; the condition is the build's judgment, row without a claim). The consensus claim C55 (at least one primary defence) is the floor.
- Epistemic: `known | unvalidated: token-first and the layering are stricter than both sources`.
- Superseded (RELAX): at least one primary defence, token preferred and layered; see section "Re-judged under best".

### G5. Other decisions

- Tokens (`SECRETS.2.1`, `.2.2`): every RFC 8725 and ASVS check is a MUST (consensus on the core); `jsonwebtoken` and `jose` settings are `.2.2`, with C11 and C14 inferred (no source says to always pass `algorithms`). Revocation (C16) is deferred to web_architecture, planned boundary link added.
- Template injection (`INJECTION.1.3`, `.1.4`): "never build a template from untrusted input" is the MUST; Kettle's trivial-engine-and-sandbox position (C32, one T3 source) is an `acceptable-when` row so the node does not become `risky`; engine rules exist for Handlebars and EJS only (C39 open).
- XML (`INJECTION.5.4`): DTDs off is on the philosophy node (principle level); the defaults node holds the three practice rules and records that no Node parser default is grounded (C22 open). fast-xml-parser's advisory is a denial of service by entity expansion, not an external-entity read.
- Uploads (`INJECTION.4.5`, `.4.6`): language-neutral rules (level `practice`, stack `principle`) are placed in the defaults graph by the extraction level, as in A2; the JavaScript signature-check recipe is open (C48).
- Header injection (`HOST.3.1`, `.3.2`): the CR, LF, NUL rule (C23, principle) is on `DEFENSE.HOST.3`; Node facts are rows of `.3.1`; the HTTP/2 and HTTP/3 rule is a separate leaf (ASVS Level 3, not a general HTTP/1.1 rule).
- Typosquatting: `DEPENDENCIES.SCREEN.3` stays `undecided` (no T1 screening procedure; one T3 paper and one T3 preprint are facts); the repository-provenance rule (C51) is decided on `INSTALL.5`; the philosophy node `THREATS.2` gained the 61 percent figure as a fact.
- `csurf` (C62) and the folklore beliefs C02, C12, C17, C62, C65 are rejected rows; clickjacking and `SameSite` rows tagged for web_architecture stay as code-level rules, with planned boundary links for the header deployment, the cookie attributes and token revocation.
- Merges (all claim ids kept): C81 into the philosophy row on `DEFENSE.INJECTION.4` (same ASVS 5.3.2 requirement as RUNSEC-C28); C77 and C79 into the rejected belief row on `INJECTION.4.1` (same Node pages as RUNSEC-C27).

### G6. Tooling touched (not graph content)

- `build/assemble/build_batches.py`, `build/assemble/apply_flags.py`, `build/distill/check_ledger.py`: the claim id pattern accepted letters only before `-C`, so `SECGAP2-C01` was invisible to them; it now accepts digits (`[A-Z]+\d*-C\d+`). `build_batches.py` also reads slot 14's claim table directly for the pointer path, because `claims_index.md` (frozen, 608 claims) has no slot 14 rows. `claims_index.py`, `routing.md` and the branch folders are history and were not touched.

### G7. Open after this slot

- Node XML parser defaults (C22), typosquatting screening procedure (C54), URL parser differential examples (C75), Node containment recipe (C82), whether `v8.deserialize` is safe (C85), SSTI rules for other engines (C39), a JavaScript upload signature check (C48). Late candidates LC-01 to LC-03 are in the slot's result file, not register sources.

### G8. Review fixes (patch review of this slot, findings F01 to F17)

- Claims: C56 and C69 corrected, C88 reconciled with the register restriction of SRC-368 (Proxy-Authorization only), C68 given the MDN position; C91 (undici `manual` returns the actual response) and C92 (CSRF token requirements) added.
- Constraints are rules only again: facts, CVE notes and version ranges of `INJECTION.1.4`, `INJECTION.5.4`, `INJECTION.6.4`, `SECRETS.2.2` and `HOST.3.1` moved to claim-less `fact` rows (design notes); `HOST.3.1` rejects instead of sanitizing; `SECRETS.2.1` requires `exp` on every token (stricter than ASVS 9.2.1, flagged).
- One owner per rule: redirects on `INJECTION.6.4`, URL parsing on `INJECTION.6.1` (`DOM.2.3` keeps the allowlist comparison, row DEFENSE-139 is now a rejected substring-test row), client file names on constraint 1 of `INJECTION.4.6`.

## Re-judged under best (24 rules)

The maintainer corrected the selection rule: "it's nto the most demanding thing, it's the best thing. The core idea is to not default to average. it's a very generic principle, based on the aggregation of sources, the collective intelligence theory." Best is the practice the strongest arguments across all sources establish for the branch's purpose; not the average, not the most common answer, not a blend, and not automatically the strictest (`target_hierarchy.md`, "Selection rule"). The 24 rules below were chosen because their epistemic state says the build went stricter than its sources or decided on one holder's position alone. Each was weighed again on the existing evidence only (no new source); the full judge record of each is in `skeleton.md` (line "Re-judged under best"), the per-rule reasoning in `build/review/rejudge_best/result.md`.

Result: 13 KEEP (the strict form is the best, reason recorded) and 11 RELAX (a weaker form is the best; the stricter form is a rejected position with the condition under which it would be best). No node, link or claim was added or removed; every claim stays placed once.

| node | verdict | rule after | stricter form is best when |
|---|---|---|---|
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | RELAX | the list is the candidates that show gate A and one of B or C today; another framework joins on the same evidence | an organisation wants a fixed approved list for audit (a policy, not a trust finding) |
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 | RELAX | platform first, adopt a framework when a requirement is unmet, isolation-test what is adopted (SUPPLY-C27) | not applicable: the isolation test was never a gate on adoption in its source |
| PIG-JS.SUBSET.CONVERSION.2 | KEEP | forbid every `==`, on the reader-cost argument (the reason "more demanding" is withdrawn) | the code base already encodes `null: ignore` and values brevity |
| PIG-JS.SUBSET.OBJECTS.3 | KEEP | `#` fields wherever privacy must hold | (relaxed form already recorded: TypeScript `private` on measured down-levelled targets) |
| PIG-JS.SUBSET.OBJECTS.4 | RELAX | accessors only as cheap, side-effect-free views of stored state; work is a method | a team wants a rule a linter checks without judging cost (no accessors at all) |
| PIG-JS.SUBSET.EVOLUTION.5 | KEEP | semicolons and braces everywhere | (relaxed form already recorded: no-semicolon style with formatter and hazard lint) |
| PIG-JS.CONTRACTS.STRICT.2 | RELAX | SHOULD enable for new code; off where friction exceeds defects found | a team measured that unchecked index reads cause its defects (MUST) |
| PIG-JS.CONTRACTS.STRICT.3 | RELAX | SHOULD enable for new code; off where dependency typings assign undefined | typings come from controlled code and absent-versus-undefined causes defects (MUST) |
| PIG-JS.CONTRACTS.ESCAPE.6 | RELAX | ban ts-ignore and ts-nocheck; ts-expect-error only with a description; no override of the recommended lint set | no type-level tests and a wish for zero directives (ban all three) |
| PIG-JS.CONTRACTS.MODEL.5 | KEEP | interface for object types, alias for what an interface cannot express | an admitted source shows accidental declaration merging causes defects (alias) |
| PIG-JS.STRUCTURE.FORMAT.4 | KEEP | modules only, no namespaces | (relaxed form already recorded: declaration files for global-script libraries) |
| PIG-JS.STRUCTURE.LOADING.6 | RELAX | SHOULD NOT use large internal barrels; small ones where no cost is measured; public entry point aggregates | the package is large enough for the measured cost to apply (no internal barrels at all) |
| PIG-JS.STRUCTURE.SURFACE.1 | KEEP | named exports only | (relaxed form already recorded: a tool mandates a default, CommonJS or AMD interop) |
| PIG-JS.STRUCTURE.SURFACE.2 | KEEP | export only what is used outside | (relaxed form already recorded: a toolbox package) |
| PIG-JS.STRUCTURE.SURFACE.3 | KEEP | no mutable exports, no write to an import | (relaxed form already recorded: a documented observable value owned by the exporter) |
| PIG-JS.STRUCTURE.SURFACE.5 | KEEP | module as namespace, no static-only classes | (relaxed form already recorded: platform-style API without module namespace) |
| PIG-JS.STRUCTURE.DIRECTION.2 | KEEP | enable the cycle lint rule knowingly, bound with maxDepth | (relaxed form already recorded: small code base with no cycle issue) |
| PIG-JS.STRUCTURE.PACKAGE.4 | RELAX | SHOULD use relative paths in a project; imports-field alias where a relative path climbs several levels | most files sit deep and cross-directory imports are the norm (aliases everywhere) |
| PIG-JS.DEFENSE.SECRETS.5 | RELAX | SHOULD detect secrets before commit, SHOULD rotate regularly | a repository that can become public or holds production credentials (MUST) |
| PIG-JS.DEFENSE.SECRETS.2.1 | RELAX | one row: require exp where tokens grant API access (was: every token); the other nine decision rows keep their strength | tokens from an issuer under no control of the deployment (require exp always) |
| PIG-JS.DEFENSE.ORIGIN.6.1 | RELAX | at least one primary defence, token or Sec-Fetch-Site check with Origin or Referer fallback; token preferred, layered | browsers may not send the header, or high-value actions (token required beside the check) |
| PIG-JS.DEFENSE.INJECTION.5.3 | KEEP | no untrusted buffer to v8.deserialize without a verified integrity check; copy from validated fields | (relaxes if Node or V8 states the function is safe for hostile bytes) |
| PIG-JS.DEFENSE.INJECTION.6.1 | KEEP | allowlist, WHATWG URL class, deny-list as the weaker fallback | (relaxed form already recorded: deny-list when no allowlist is possible) |
| PIG-JS.VERIFICATION.LINT.2 | KEEP | the CI job that runs the lint gate always runs | (none: a skippable required check is no gate) |

Consequences outside the 24 (consistency, no new judgment):
- `PIG-JS.VERIFICATION.LINT.1.2` (row VERIFICATION-021) said the one override of the recommended lint set is `ban-ts-comment`; with ESCAPE.6 relaxed to the recommended setting no override remains, and the row now says so.
- Tooling touched (not graph content): `build/assemble/build_batches.py`, the `ACCEPT` entry of row SUBSET-069, so that the acceptable-when constraint of `PIG-JS.SUBSET.OBJECTS.4` states the stricter form instead of the former narrow condition.
- `PIG-JS.CONTRACTS.ESCAPE.6` was renamed "No silent suppression directives" (the uid is unchanged).
- Epistemic flags corrected on KEEP nodes where the flag was wrong: `PIG-JS.VERIFICATION.LINT.2` and `PIG-JS.DEFENSE.INJECTION.6.1` (a rule marked "no claim of its own" has its claim held on a philosophy node), `PIG-JS.SUBSET.CONVERSION.2` (the reason now recorded).
- Other judge records still use "max rule" or "most demanding" wording (nodes that were not among the 24: for example the STRICT parent, UPDATE.1, the RUNTIME and DEPENDENCIES tables). They were not re-judged; their wording predates the correction. Open for the maintainer: re-judge them the same way, or only the ones whose state says stricter than the source.

Open after this pass:
- `PIG-JS.CONTRACTS.ESCAPE.6`: the recommended setting of `ban-ts-comment` and the self-reporting behaviour of `ts-expect-error` are in no extracted claim; read them from the typescript-eslint rule page and the TypeScript handbook before relying on the text.
- `PIG-JS.SUBSET.CONVERSION.2` is a close call (stylistic tie): the maintainer may overrule to `== null` allowed through lint with no loss of grounding.
- The threshold "many modules" (LOADING.6) and "several directory levels" (PACKAGE.4) are deliberately unstated: no admitted source gives a number.

## Decisions by branch

### SUBSET


Each decision settles a contested topic, a weighty choice, or rests on a single source. The max rule
(most demanding practice an admitted source supports) decided each; the maintainer may overrule any.
Epistemic labels: grounded, inferred or open.

#### SUBSET: A. Contested topics (decided by the max rule)

##### SUBSET: A1. `== null`: forbid every `==` (node PIG-JS.SUBSET.CONVERSION.2, rows SUBSET-016, 017)
- Decision (grounded as a choice, inferred as the max reading): forbid all `==`, including the null check; write `x === null || x === undefined`. Lint: ESLint `eqeqeq` default `always`.
- Rejected: `== null` as the one allowed `==` (Google JS guide, eqeqeq option `null: ignore`). It would win where a code base already encodes the exception in lint and prefers brevity over uniformity; the mechanism is exact (ECMA-262 7.2.13), so it is a style loss, not a defect risk.
- Grounds: eqeqeq (SRC-002, T1) default forbids it; Airbnb (SRC-312) forbids it as a position; MDN (SRC-011) describes the behaviour. Note: the stage-4 dissent slot recommended allowing the exception; this branch chose the more demanding option because predictability means the reader needs no special case. Flagged for the maintainer. Re-judged under best (KEEP): the reason "more demanding" is withdrawn, the reader-cost argument carries the decision; see section "Re-judged under best".

##### SUBSET: A2. Implicit coercion shorthands (node CONVERSION.4, rows SUBSET-019 to 022)
- Decision: write `Boolean()`, `Number()`, `String()`; enable `no-implicit-coercion`; state the rule as a readability convention and make no claim that it prevents defects.
- Rejected: allow `!!x`, `+x`, `'' + x`. It wins where a team does not adopt the lint rule; the only measurement (Pradel and Sen, 2015 corpus, SRC-238) finds 98.85 percent of implicit coercions likely harmless.
- Grounds: positions only (SRC-003 T1 restricted, rationale is readability; SRC-239 and SRC-312 positions). No mechanism evidence supports forbidding; this is the weakest-grounded decision of the branch and the one most likely to be overruled. Epistemic: `known | unvalidated: positions only, no mechanism evidence | conflict: Pradel and Sen`.

##### SUBSET: A3. Private-member marking (node OBJECTS.3, rows SUBSET-043 to 046)
- Decision: hash private fields wherever privacy must hold; an underscore never counts as privacy.
- Rejected: TypeScript `private` instead of hash fields (Google TS guide, SRC-244, reason stated: emit size and performance when down-levelled): wins on down-levelled targets where the cost is measured. Optional trailing underscore (Google JS, SRC-239) and underscore convention in general: never privacy (MDN, SRC-091). No-underscore rule (Airbnb, SRC-312): agrees on the mechanism, adds no ground.
- Grounds: MDN private elements (SRC-091) and classes (SRC-008), TC39 class fields (SRC-024): the mechanism is undisputed, the dispute is only the compile target.

#### SUBSET: B. Weighty choices on thin or restricted grounds

##### SUBSET: B1. Strict mode everywhere (node STRICTNESS.1, LANG-C02)
- The preference is inferred from MDN's three reasons (LANG-C02 is marked inferred); the mechanism (modules and classes strict by construction) is ECMA-262 11.2.2, grounded. Rejected: sloppy mode, wins only for code that cannot be edited. Epistemic: `known | unvalidated: practice inferred; quote tool-extracted`.

##### SUBSET: B2. Only TC39 stage 4 features (node EVOLUTION.1, LANG-C54)
- Decision on one source (SRC-028, T1, restricted to status facts); the rule is inferred from the definition of stage 4. Rejected: earlier stages with a transpiler; no admitted source states target guarantees for them. Epistemic: `known | unvalidated: single T1 source restricted to status facts; rule inferred`.

##### SUBSET: B3. `Object.hasOwn` over `hasOwnProperty` (node OBJECTS.6, LANG-C55)
- The reason (shadowing, null-prototype objects) is quoted from Airbnb, a position that may not serve as evidence, and the stage-4 status is a restricted status fact. The choice is corroborated by RUNSEC-C07 in DEFENSE (consensus, overlap O15), whose sources this agent did not re-read. Follow-up check: RUNSEC-C07 (consensus, DEFENSE) is grounded on SRC-139 (MDN prototype pollution, T1, unrestricted) and SRC-078 (Node security best practices, T1, unrestricted for 06_runsec); it states Object.hasOwn for untrusted-keyed reads. LANG-C55 is confirmed for that case by two T1 sources; extending it to all own-property tests is inferred from the same mechanism. Kept as the decision; `hasOwnProperty` stays as acceptable-when on targets without `Object.hasOwn` (STRUCT-C45, MDN). Epistemic: `known | unvalidated: grounded for untrusted keys by two T1 sources via RUNSEC-C07, extension to all reads inferred`.

##### SUBSET: B4. Temporal adoption (node EVOLUTION.2, LANG-C43)
- Decision: adopt only after every target is verified or covered by a polyfill. The availability figures (Firefox 139, Chrome 144, Node.js 26; MDN not Baseline) are dated facts as of the MDN page date and must be rechecked before citing (SRC-019 restriction).

##### SUBSET: B5. `for-in` on arrays (node OBJECTS.6, LANG-C26)
- Decision on one T2 source (DLint, SRC-237, restricted to evidence that the practice occurs and causes visible bugs on 2015 sites). Within the restriction as evidence, but the rule wording is the paper's. Epistemic: single T2.

#### SUBSET: C. Style-guide positions demoted (restriction: positions only, never evidence)

No admitted source other than a restricted style guide supports these four; each is kept as `acceptable-when` (a team convention) and none is a decision. The maintainer may promote any by choosing it as a convention. STRUCT-C46 and QUALITY-C19 were demoted in the first pass and are now decisions on a position alone (section E).

| claim | position | holder | node | would be promoted by |
|---|---|---|---|---|
| LANG-C07 | arrow functions over bind(this) and self = this | Google JS | OBJECTS.1 | a T1 statement of the reason; the mechanism is already in LANG-C06 |
| LANG-C08 | this only in class code and arrows | Google JS | OBJECTS.1 | a T1 or second independent T2 ground |
| LANG-C14 | no direct prototype work, use class | Google JS | OBJECTS.5 | MDN class-over-prototype statement (STRUCT-C43 in RUNTIME) read as a rule |
| LANG-C16 | never call new on primitive wrappers | Google JS | CONVERSION.4 | ECMA-262 wrapper-object semantics or ESLint no-new-wrappers docs |

#### SUBSET: D. Single-source decisions (T1 unless marked)

LANG-C02 (MDN strict mode), LANG-C09 (MDN classes), LANG-C20 (MDN equality sameness), LANG-C23 (MDN Number), LANG-C26 (T2), LANG-C41 (MDN sort), LANG-C44 (MDN structuredClone), LANG-C50 (MDN nullish coalescing), LANG-C54 (TC39 finished proposals), LANG-C55 (see B3). Each carries `unvalidated: quote tool-extracted` or the single-source label in its node; none is contested.

#### SUBSET: E. Former undecided nodes, now decided on a position (flagged)

No node of this branch is undecided. Both were decided because an admitted position exists; each is the weakest-grounded kind of decision (one T2 restricted position, no mechanism evidence), labelled `known | unvalidated`.

##### SUBSET: E1. Statement termination (node PIG-JS.SUBSET.EVOLUTION.5, rows SUBSET-068, 070)
- Decision: a semicolon on every statement and braces on every control structure; never rely on automatic semicolon insertion. By predictability: explicit termination makes statement boundaries independent of line breaks and of the next token.
- Rejected: reliance on insertion (no-semicolon style). It wins where a formatter and lint rules that catch insertion hazards both run in CI and the team adopts that style; no admitted source states that condition.
- Grounds: Google JS (SRC-239, T2, position only, QUALITY-C19). Searched: every claim table, the register and the coverage report; no claim states the insertion hazards (slot 01 records that no mechanism was read, G-M02), so the coordinator's note that MDN documents them is not backed by an extracted claim. Would strengthen it: ECMA-262 automatic insertion rules and the MDN lexical-grammar page, extracted as claims.

##### SUBSET: E2. Accessor properties (node PIG-JS.SUBSET.OBJECTS.4, rows SUBSET-047, 069)
- Superseded (RELAX): accessors only as cheap, side-effect-free views; see section "Re-judged under best". The decision below is the former one.
- Decision: no getter or setter properties; behaviour that does work is a method. By predictability: a read that runs code hides cost and side effects.
- Rejected: accessors. They win for a cheap, side-effect-free view of stored state on a data-like object (inferred, no source).
- Grounds: Google JS (SRC-239, T2, position only, STRUCT-C46); its compiler-support reason is a Closure tooling point and is not carried. Searched: all claim tables, register and coverage (G-L14); the only other hits are LANG-C13 (class-field Define semantics) and LANG-C42, unrelated. Would strengthen it: MDN Using classes (LC-02) and ECMA-262 accessor semantics.

#### SUBSET: F. Gaps noted, no node created (no claim of this branch touches them)

G-M01 exact decimal and money arithmetic (TC39 decimal repository LC-01); G-M02 remainder (typeof, instanceof and realms, Symbol, iterators and generators, destructuring and spread); G-M03 dates, time zones, Unicode, Intl; G-M29 immutability as a design preference (kept as a gap on SUBSET.STATE); G-L01 parseInt radix. These stay for the integrator and the maintainer: no practice is invented for them.

### CONTRACTS


Selection rule: max, grounded (see `../../target_hierarchy.md`). Each decision lists the choice,
the rejected positions with the condition under which each would win, and the grounds. Node
uids are in `skeleton.md`, rows in `ledger.md`.

#### CONTRACTS: D1. Type layer is TypeScript (PIG-JS.CONTRACTS.LAYER.1, rows CONTRACTS-011, CONTRACTS-012)

Decision: TypeScript with strict checking and a separate type check (LAYER.3). Epistemic state:
`known | conflict: JSDoc-checked JavaScript, none`. This is maintainer question Q1 of `12_dissent`
(recommendation there: the same).

Rejected positions:
- JSDoc-checked JavaScript. Wins where no compile step and no type-check step can be adopted.
  Kept as a fallback (LAYER.2) with its limits: open-ended object literals, all parameters
  optional, any for null and empty-array initialisers (TYPES-C40); no run-time import of
  tags and silent no-op of unlisted tags (TYPES-C41); TypeScript 7.0 drops enum tags,
  Closure-style function types, standalone question mark and postfix bang (TYPES-C42).
- None. Wins on no admitted evidence: no admitted holder argues for it (TYPES-C01, G-M05 of
  `11_coverage`); SRC-240 only measures that types detect 15 percent of public bugs.
- Waiting for native type annotations in JavaScript. A Stage 1 proposal, last presented 2023-09
  (TYPES-C46). Never a basis; status is a grounded fact, "do not plan on it" is inferred.

Grounds and their strength (honest account):
- Mechanism, T1: the TypeScript checker sees more in TypeScript files than in checked JavaScript
  (SRC-047, restricted to facts up to 6.x; SRC-052 for the checkers' modes). These are the tool's
  own documentation, so they ground facts about checking strength, not "prefer this tool".
- Advocacy, T2, one holder: the Google JS guide (frozen, recommends migrating) and the Google TS
  guide are one organisation counted once, and both are restricted to "positions", never evidence.
- Measurement, T2: SRC-240 (2017, Flow 0.30 and TypeScript 2.0, 15 percent of 400 public bugs,
  conservative by the authors' words; not current strict TypeScript).
- The step from "checker sees more" to "choose TypeScript" is the max rule's judgment (inferred).
  Node type stripping (SRC-038) removes the build step that was the usual reason to avoid
  TypeScript (inferred, as in `12_dissent` Topic 4).

#### CONTRACTS: D2. Flags beyond strict: enable (PIG-JS.CONTRACTS.STRICT.2 and .3, rows CONTRACTS-025, CONTRACTS-026)

Decision: enable noUncheckedIndexedAccess and exactOptionalPropertyTypes for new code.
The source claims say only "consider" and give the mechanism; no admitted source mandates the
flags. The max rule picks the more checkable setting, marked `unvalidated: mechanism only`. Superseded (RELAX): both flags are SHOULD for new code; see section "Re-judged under best".

Rejected: leaving them off. Wins where index-heavy or untyped-dependency code makes the friction
exceed the defects found; typescript-eslint calls the first flag often unwieldy (SRC-026, T1).
The condition is inferred. Review ask: confirm that a mechanism-only ground suffices for a
mandate, or demote both to acceptable-when.

#### CONTRACTS: D3. No suppression directives (PIG-JS.CONTRACTS.ESCAPE.6, rows CONTRACTS-034, CONTRACTS-035)

Decision: ban ts-ignore, ts-expect-error and ts-nocheck; allow a lint suppression only with a
comment saying why. Epistemic state `known | unvalidated: single T2 source`. Superseded (RELAX): ts-ignore and ts-nocheck are banned, ts-expect-error is allowed with a description; see section "Re-judged under best".

Weakness to review: the ground is one T2 holder (Google TS guide). The same position appears twice
(QUALITY-C18, TYPES-C25). The register leaves SRC-244 unrestricted for the quality slot but
restricts it in the types slot to "positions only, never evidence". I used the quality-slot claim
as the decision ground and demoted the types-slot claim to a fact row. If the maintainer reads the
restriction as applying to the topic and not the slot, this node becomes undecided, with TYPES-C25
and QUALITY-C18 as acceptable-when.

Rejected: allowing directives with a reason. Wins for a third-party typing bug that cannot be
fixed locally (inferred). No admitted holder takes that position.

#### CONTRACTS: D4. Options object (PIG-JS.CONTRACTS.SIGNATURE.1, rows CONTRACTS-041, CONTRACTS-042)

Decision: options object when several arguments are optional or same-typed primitives.
Grounds: ESLint's stated rationale (order and types must be memorised, SRC-084, T1 restricted:
the default of 3 is a configuration default, not evidence) and the W3C TAG position for web
platform APIs (SRC-261, T2 restricted). No admitted source states it for application code: the
claim is inferred (STRUCT-C49), epistemic state `known | unvalidated: inferred`.
Rejected: positional lists, which win for one to three required distinct-typed arguments.
The philosophy node CONTRACTS.SHAPE holds only the language-neutral part (STRUCT-C47).

#### CONTRACTS: D5. Compiler pinned (PIG-JS.CONTRACTS.STRICT.4, rows CONTRACTS-027, CONTRACTS-028)

Decision: pin the TypeScript version and upgrade deliberately. The tsconfig reference says future
versions may add checks under strict (T1, single source); the pin is inferred. Rejected:
floating versions, which win never for applications; the library-publishing case belongs to
DEPENDENCIES (proposed link Q4).

#### CONTRACTS: D6. Optional chaining only on nullable types (PIG-JS.CONTRACTS.MODEL.3, row CONTRACTS-038)

Decision as in the claim; preference inferred from the typescript-eslint rule plus MDN
(`known | unvalidated: preference inferred`). Rejected: defensive optional chaining everywhere;
wins on untyped boundary data, which BOUNDARY handles by parsing instead.

#### CONTRACTS: D7. Erasable syntax scope (PIG-JS.CONTRACTS.LAYER.4, row CONTRACTS-019)

Decision follows the claim: erasable syntax only when Node strips types. The max rule could widen
it to every TypeScript project (so the code always runs unbuilt), but no admitted source says so,
so the widening is open, not decided. Review ask: widen or keep conditional.

#### CONTRACTS: D8. Folklore rows with empty claim ids (CONTRACTS-002, CONTRACTS-018)

The two beliefs of `12_dissent` concerning this branch (types protect at run time; Node
type-checks what it runs) become `rejected` rows. Their refuting claims (TYPES-C02, TYPES-C03) sit
in their own decision rows, and the brief places each claim once, so the rejected rows carry
claim_ids `-`. Review ask for the integrator: keep this convention or merge each pair into one row.

#### CONTRACTS: D9. Deferred claim (CONTRACTS-006)

TYPES-C29 (client-side validation is never a security control; validation at a trusted service
layer) is architecture owned by the web-architecture guideline per `11_coverage`: ledger role
`deferred` on CONTRACTS.BOUNDARY.1, with a planned boundary link (P5 in the skeleton).

#### CONTRACTS: D10. Philosophy and defaults split

Language-swap test applied claim by claim. To js-philosophy: TYPES-C27, C28, C33, C48, C29
(language-neutral boundary principles), STRUCT-C47 (parameter memorisation), TYPES-C02, C23, C47
(JavaScript-distinct: the language has no run-time types; the checker is unsound and measured).
Everything naming a compiler option, tool, API or library is in pig-js-defaults.

#### CONTRACTS: D11. Former undecided nodes, now decided (rows CONTRACTS-039, CONTRACTS-040, CONTRACTS-050 to CONTRACTS-052)

Per the standing max rule, a missing independent ranking is not a reason to abstain; each node is
decided where admitted positions or facts exist. All three are weak on grounds and flagged.
- MODEL.4 type predicates are assertions (TYPES-C20). Decision: held to the standard of a type
  assertion (explicit run-time check in the body; built-in narrowing or schema parse preferred).
  Grounds: TYPES-C19 and TYPES-C23 (T1 handbook and typescript-eslint). The specific statement that
  the compiler does not verify a predicate body is in no admitted source (searched: handbook
  narrowing page, typescript-eslint pages; a digest asserted it, a verbatim re-ask did not).
  Epistemic: `known | unvalidated: inferred`. Rejected: trust as written, which wins for a
  one-line test of an already validated discriminant (inferred).
- MODEL.5 interface for object types (TYPES-C26). Decision: interface; alias for what an interface
  cannot express (inferred). Ground: the Google TS guide position, one T2 holder, plus the handbook
  fact that interfaces extend and re-open. The register restricts the source to position only; the
  position is used to choose among positions, not as evidence. Rejected: alias everywhere, which
  wins where accidental declaration merging must be impossible (inferred). The const enum half is
  settled by LAYER.4.
- BOUNDARY.5 schema infers the static type (TYPES-C36, C37, with C38 and C35 as facts). Decision at
  the class level: a library whose schema is the single source of the static type, Standard Schema
  V1 compliant where tools must accept it, schemas never compiled from untrusted input. No library
  is named: all sources are vendor documentation, admitted for facts only, and none ranks Zod
  against Valibot. Rejected: JSON Schema with Ajv, which wins where the schema is a language-neutral
  contract shared with non-TypeScript code (inferred). Review ask: name a default library or keep
  the class-level rule.

#### CONTRACTS: D3 scoping note

The register restriction on SRC-244 is scoped per slot: unrestricted for the quality slot, so
QUALITY-C18 may ground the rule; the decision stands. TYPES-C25 remains a fact row.


### CONTROL


No contested topic of `12_dissent` (16 topics) concerns CONTROL; the weighty choices below are
judgement calls under the max rule, each overridable by the maintainer. Certainty tags: grounded,
inferred, open.

#### CONTROL: A. Weighty choices

**D1. A failure the program cannot repair ends the process; nothing resumes (rows CONTROL-011, 075, 078, 079).**
Decision: unhandled rejections throw by default in Node; uncaughtException is for synchronous
cleanup, then exit, then an external supervisor restarts; the monitor hook only logs.
Rejected: resuming after uncaughtException (Node docs: not safe), wins under no condition named by an
admitted source; the non-default `--unhandled-rejections` modes (SRC-079), no condition named.
Grounds: SRC-082, SRC-068 (history), SRC-079; grounded, single T1 source for C05, C37, C38.

**D2. Every promise is observed (019 to 022).** Decision: await, return or handle each promise;
void is not handling; no async callback where a void callback is expected; no promise as a condition.
Rejected: floating promises and void-as-handling, no condition named. Grounds: SRC-072, SRC-073
(typescript-eslint rule documents, restricted to what the rules report and their rationale; they do not
ground a preference for that tool), SRC-082, SRC-077, SRC-081; grounded, single T1 for the void and
condition rules.

**D3. Throw only Error instances (031).** Merges ASYNC-C18 and LANG-C45 (Google's position, used as a
position only). Rejected: strings and plain objects, no condition named. Grounds: SRC-074 (T1
restricted rationale), SRC-239 (T2 position); grounded.

**D4. Empty catch demoted to acceptable-when (035).** ASYNC-C21 rests only on Google's style-guide
position (SRC-239, "never evidence"). The no-silent-swallow rule itself is carried by the inter link to
python DEFENSIVE and by TYPES-C12 plus the channel rule C22, not by a decision row. Rejected: empty
catch with no reason; wins nowhere. Certainty: grounded as a position, the demotion is a judgement.

**D5. AbortSignal is the one cancellation and timeout primitive (041 to 049).** Rejected: assuming promises
cancel (refuted, row 003); reusing one controller (one-shot). AbortSignal.any: MDN says the combined
signal cannot say which source fired, Node sets the reason of the source that aborted; the sources are
compatible, not contested (noted in the claim). Grounds: SRC-057, SRC-055, SRC-066, SRC-261 (position
only); grounded, consensus.

**D6. Concurrent by default (025).** Rejected: sequential loops of awaits, wins when a later operation
depends on an earlier result (the claim's own condition). Concurrency limits, retry and backoff: no
admitted source (undecided node PROMISES.4.1). Grounds: SRC-056, SRC-246, SRC-075 (MDN's position); grounded.

**D7. setImmediate over process.nextTick (050).** Rejected: nextTick for general deferral (refuted by
Node docs). Single T1 source (SRC-071, "we recommend setImmediate in all cases"); grounded, single-source.

**D8. CPU work to workers; partitioning only as the weaker alternative (057, 059).** The condition for
partitioning (work that cannot move to a worker) is inferred: SRC-080's offloading recommendations are
excluded by its restriction, so the choice between them rests on SRC-069 and the restriction, not on
SRC-080. Certainty: inferred for the ordering of the two.

**D9. Server timeouts configured, requestTimeout never disabled on an exposed server (047).** The
do-not-disable rule is inferred from "0 disables"; default values read through a digest, not verbatim.
Rejected: unbounded slow connections, no condition named. Certainty: inferred for the rule, grounded
for the mechanism.

**D10. pipeline over pipe (069).** Rejected: pipe(), leaks the destination when the source errors; no
condition named. Single T1 source (SRC-196); grounded, single-source.

**D11. Duplicate and overlap handling (from 11_coverage).** Merged into one row each: O01
(ASYNC-C04 with RUNTIME-C40, SRC-082 alone suffices, SRC-079 text unreliable per G-L15), O03
(ASYNC-C23 with RUNTIME-C31), O04 (ASYNC-C55 with RUNTIME-C42), O07 (ASYNC-C18 with LANG-C45; TYPES-C12
kept as its own row), O17 (ASYNC-C26 with STRUCT-C53). O02 is split on purpose: ASYNC-C05 states the
principle on CONTROL.LIFECYCLE, RUNTIME-C37 states the Node rule on PROCESS.2; the integrator may merge
them under P5 if it prefers one row.

**D12. Folklore (9 beliefs, all refuted, all grounded):** missing return harmless (015), unhandled
rejections only warn (077), Promise.all cancels (027), promises cancellable (003), setTimeout(0) exact
(007), 0 ms timers (054), then on a resolved promise runs now (005), nextTick for deferral (053),
async/await slower (086, T2 history only, the present-day gap open). The 12_dissent confirmed and
restricted beliefs concerning other branches are not placed here.

**D14. Async functions over then chains (029, 086), single T2, dated.** Searched: claims of slot 03 and the register for style-guide positions, MDN guidance, lint-rule documents and ASYNC-C52. Positions found: V8 team 2018 advice to favour async functions and await (SRC-249, T2, restricted to history, used here as a dated position); MDN flat chains (SRC-075); async functions convert exceptions to rejections (SRC-056 via ASYNC-C07). No admitted source advocates chains over async functions. Decision: async/await by default; flat chains acceptable. Winning condition of the rejected position: a flat chain as the whole body, or a nested chain confining a catch (inferred from MDN); the speed belief wins only on an admitted current measurement (open). Certainty: grounded for the positions, inferred for the explicit-failure argument and the condition. ASYNC-C52 moved from `rejected` on PROMISES.5 to `decision`; the belief is a claim-less rejected row.

**D13. Shutdown contract left to the sibling (082, 083).** `boundary: web-architecture` per routing.
The Node API side stays here (11_coverage: "the Node API side stays"); proposed planned boundary link
P6. If the integrator prefers `deferred`, change both rows' role.

#### CONTROL: B. Single-source decisions

Each decision row below rests on one source (one T1 page, or one T2 paper); the epistemic state of its
node says `unvalidated`. 39 decision rows plus 2 acceptable-when, 8 fact and 2 rejected rows are
single-source. Decision rows, with the ledger row and claim:

| row | claim | source and tier | note |
|---|---|---|---|
| 011 | ASYNC-C05 | SRC-082 T1 | hooks are last resort |
| 014 | ASYNC-C15 | SRC-075 T1 restricted | MDN editorial position |
| 016 | ASYNC-C11 | SRC-059 T1 restricted | rule behaviour |
| 018 | ASYNC-C13 | SRC-245 T2 restricted | formal model |
| 020, 022 | ASYNC-C03, C17 | SRC-072, SRC-073 T1 restricted | rule documents; truthiness of objects is language semantics, not stated in the digest |
| 023 | ASYNC-C08 | SRC-056 T1 | |
| 026 | ASYNC-C54 | SRC-060 T1 restricted | detection heuristic |
| 028 | ASYNC-C53 | SRC-246 T2 restricted | 20-repository sample |
| 029 | ASYNC-C52 | SRC-249 T2 restricted | 2018 position of the V8 team, dated |
| 032 | ASYNC-C24 | SRC-065 T1 | |
| 033 | TYPES-C12 | SRC-052 T1 | |
| 037 | ASYNC-C20 | SRC-058 T1 | |
| 039, 040 | RUNTIME-C32, C33 | SRC-081 T1 | |
| 044 | RUNTIME-C06 | SRC-196 T1 | |
| 046 | ASYNC-C34 | SRC-067 T1 | |
| 047 | ASYNC-C55, RUNTIME-C42 | SRC-078, SRC-190 T1 | do-not-disable inferred |
| 048 | ASYNC-C30 | SRC-055 T1 | |
| 049 | RUNTIME-C34 | SRC-081 T1 | |
| 050 | ASYNC-C36 | SRC-071 T1 | |
| 055, 056 | ASYNC-C39, C41 | SRC-080 T1 restricted | mechanism only; C41 inferred |
| 060, 063 | ASYNC-C44, C47 | SRC-063, SRC-069 T1 | |
| 064 | ASYNC-C48 | SRC-064 T1 | |
| 067, 068 | RUNTIME-C02, C03 | SRC-184 T1 restricted | mechanism only |
| 069, 070, 073 | RUNTIME-C05, C08, C10 | SRC-196, SRC-197 T1 | |
| 078, 079, 080, 081 | RUNTIME-C37, C38, C35, C36 | SRC-082 T1 | |
| 082, 083 | RUNTIME-C39, C41 | SRC-082, SRC-190 T1 | C39 must-exit rule inferred |
| 084, 085 | RUNTIME-C17, C43 | SRC-188, SRC-190 T1 | C17 wording from digest |

Evidence that would validate them: a second independent T1 or T2 source per claim; none is
required by the max rule, only the epistemic tag.


### STRUCTURE


Purpose of the branch: locality of change. Max rule: the most demanding practice that serves that
purpose and that an admitted source supports. Restricted style-guide positions decide a node only as
the holder's position and are never counted as evidence. Ledger row ids refer to `ledger.md`.

#### STRUCTURE: Decisions that settled a contested topic

##### STRUCTURE: D1. Module cycles: forbid (PIG-JS.STRUCTURE.DIRECTION.1; STRUCTURE-040, STRUCTURE-041)
- Decision: create no import cycle between modules, in ESM or CommonJS. Status `known | conflict | unvalidated`.
- Rejected, tolerate cycles (Node CommonJS docs, SRC-089: documented as a supported mechanism through partial exports, no recommendation). Wins where a cycle is deliberate in CommonJS legacy code with no observed fault, or where the detection cost exceeds the benefit.
- Rejected, folklore "cyclic imports always crash" (row 041): refuted by SRC-029 and SRC-089; it is a different question from whether to forbid.
- Grounds: MDN advice (SRC-029, via LANG-C64 in slot 01 where the register row is unrestricted; in slot 04 the same sentence is restricted to a position), Google JS position (SRC-239), plugin maintainers' position (SRC-313, never evidence). The mechanism (a cycle fails only when a binding is used before it is initialised) is T1 but only shows that correctness can depend on evaluation order. No admitted source measures a defect cost.
- Review point: the decision is the demanding one for locality; its evidence is thin. Alternative is to demote it to `acceptable-when: tolerate`.

##### STRUCTURE: D2. Top-level await: entry points only (PIG-JS.STRUCTURE.LOADING.4; STRUCTURE-027, STRUCTURE-028)
- Decision: use it only in application entry points, never in a module that others import or that may be require()d.
- Rejected, allowed anywhere (champions Borins and Startsev in the TC39 record: education suffices, deadlocks already exist). Wins if a measurement shows the hazard negligible, or in scripts nothing imports.
- Grounds: T1 mechanism (SRC-092, SRC-030, SRC-029): every importer waits, a never-resolving await ends Node with status 13, require() of the graph fails with ERR_REQUIRE_ASYNC_MODULE. The scope "entry points" is inferred from that mechanism (a leaf change turns every ancestor asynchronous). No source measures the hazard.

##### STRUCTURE: D3. Default versus named exports: named only (PIG-JS.STRUCTURE.SURFACE.1; STRUCTURE-032)
- Decision: named exports in all code.
- Rejected, default for single-export modules (Airbnb, SRC-312): wins when a framework or tool mandates a default export. Acceptable-when: interoperating with CommonJS or AMD consumers (the purpose MDN names, SRC-029, neutral).
- Grounds: holder position of Google JS and Google TS (one holder, so one position); the guides' reason (a default has no canonical name, so rename refactors cannot find uses) is their own. The mechanism that importers choose their own name is language fact.

##### STRUCTURE: D4. Paradigm and defects: no paradigm mandate (STRUCTURE.PARADIGM; STRUCTURE-011, STRUCTURE-012)
- Decision: choose per problem by intent; no source supports an object-oriented or functional rule inside JavaScript on defect evidence.
- Rejected, "functional lowers defects" (Ray et al. 2014, SRC-251, restricted). Wins only if a study scoped to JavaScript paradigms shows an effect; the three papers compare languages on one GitHub dataset, with a dispute over the analysis (SRC-258, SRC-314).
- Grounds: the absence of scoped evidence, inferred (C64). The restriction on SRC-251, SRC-258 forbids using them as a ground for a paradigm choice, so they are used only to show that none exists.

#### STRUCTURE: Weighty choices and single-source decisions

##### STRUCTURE: D5. Barrel files: aggregate only at a public entry point (PIG-JS.STRUCTURE.LOADING.6; STRUCTURE-031)
- Superseded in strength (RELAX): SHOULD NOT for large internal barrels; see section "Re-judged under best".
- Decision: import from the defining module; keep re-exporting modules to a package's public entry point.
- Rejected, blanket "get rid of all barrel files" (Hagemeister, SRC-315): the register restricts that source to its synthetic measurement (one machine, 500 to 50,000 modules); the blanket is his position and is not adopted. Would win if the public entry point itself shows the load cost in the project's own measurement.
- Rejected, barrels as a convenience everywhere (MDN documents aggregation, no recommendation): wins where no measurement shows a cost and importers need many members.
- Grounds: single T3 source for the magnitude, mechanism (eager loading of everything re-exported) from MDN (SRC-086). The narrowing to "public entry point only" is inferred. The plan says T3 alone cannot make a node `known`; the brief's format would, so the node is `known | unvalidated: single T3 source`. Review point.

##### STRUCTURE: D6. Static-only container classes: module is the namespace (PIG-JS.STRUCTURE.SURFACE.5; STRUCTURE-038, STRUCTURE-039)
- Decision: export functions and constants individually. Holder position of Google JS and Google TS.
- Rejected, W3C TAG (SRC-261): a class is shaped for state, stateless groupings are static methods. Wins when designing a platform-style API where the host offers no module namespace; the source's setting is web platform APIs and transfer to module code is inference.

##### STRUCTURE: D7. Exported state: read-only (PIG-JS.STRUCTURE.SURFACE.3; STRUCTURE-034, STRUCTURE-035)
- Decision: never write to an import and export no mutable binding (no export let); mutate exported state only through functions.
- Rejected, exported mutable live binding: wins for a deliberate observable value owned by the exporter, if documented.
- Grounds: mechanism T1 (live bindings are read-only to importers, SRC-087, SRC-029, SRC-086) for the first half; the strongest form rests on holder positions of Google JS, Google TS and Airbnb.

##### STRUCTURE: D8. Naming (STRUCTURE.NAMING.1 to .3; STRUCTURE-008, -009, -010)
- Decision: whole words; one concept one word; derive names from concepts.
- Grounds: SRC-260 (72 professional C# developers, T2, 19 percent), SRC-254 (T2); both single-source with transfer to JavaScript inferred. NAMING.2 rests on holder positions only. No admitted source covers casing, file naming or boundaries between naming schemes (thin per `11_coverage`).
- Rejected, short names: wins nowhere in the evidence (no significant difference between letters and abbreviations).

##### STRUCTURE: D9. Philosophy decisions resting on one T2 principle source
- STRUCTURE.HIDING.1 (Parnas, SRC-257), HIDING.2 (Cook, SRC-259), STATE.1 (Codd, SRC-252): language-agnostic principles, each flagged `single T2 source`. SRC-257 is a principle only, never a JavaScript rule; SRC-259 gives no evidence for choosing either style; SRC-252 transfer to application state is inference.
- STRUCTURE.HIDING.3 (minimal surface at three levels) is inferred as a shared form across one T2 principle and T1 mechanisms in SRC-090 and SRC-091.

##### STRUCTURE: D10. Holder-position-only decisions (flag `holder position only`)
- Re-judged under best: FORMAT.4 and SURFACE.2 KEEP; PACKAGE.4 RELAX (relative paths by default, imports-field alias where a path climbs several levels); see section "Re-judged under best".
- FORMAT.4 (no TypeScript namespaces, SRC-244), SURFACE.2 (export only what is used, SRC-244), PACKAGE.4 (relative paths within a project, SRC-244), NAMING.2 (SRC-239, SRC-244, SRC-261, SRC-312). Each wins under the max rule because no weaker admitted practice serves locality better; none has a T1 mechanism behind the rule.

##### STRUCTURE: D11. Folklore rows (STRUCTURE-020, STRUCTURE-041)
- "CommonJS cannot load ES modules": restricted by SRC-089 and SRC-030 (works for graphs without top-level await). "Cyclic imports always crash": refuted by SRC-029 and SRC-089.

##### STRUCTURE: D12. Deferred to a sibling branch, no node here
- Cycle-lint severity in CI and layering enforcement gates: VERIFICATION. Choice of ES modules over CommonJS for new code: SUBSET (LANG-C57, STRUCT-C21); proposed link FORMAT.1 to SUBSET.

#### STRUCTURE: Open gaps recorded as notes, not nodes
- Application state design (G-M10): STRUCTURE.STATE has one principle source (Codd) and one mechanism (exported objects); no admitted source on state design in applications.
- Composition versus inheritance (G-L04): no admitted claim.
- Naming conventions of casing and file names: no admitted claim.

### DEFENSE


Every decision below settled a contested topic or a weighty choice, or rests on a single source. The selection rule is max, grounded: the most demanding practice that serves safety and that an admitted source supports (`../../target_hierarchy.md`). Each entry names the decision, the rejected positions with the condition under which each would win, and the grounds. Claim ids point to `claims.md` in this folder; ledger rows are in `ledger.md`. Certainty words follow the build rule: grounded, inferred, open.

#### DEFENSE: Part A. The cut and the conventions (decided by this agent, to be confirmed)

**A1. The partition of DEFENSE (weighty, inferred).** Six children, cut by what hostile data becomes or attacks, not by browser versus server: `DOM` (markup, script and navigation in the page), `ORIGIN` (boundaries between origins), `INJECTION` (instruction or location for an interpreter outside the page, six classes), `PROTOTYPE` (keys that rewrite the object model), `SECRETS` (randomness, crypto, secrets, leakage), `HOST` (the Node process under hostile input). Why not browser versus server: five of the six classes cross it (code from strings, prototype pollution, ReDoS, URL validation, secrets), so a browser or server cut would place one principle twice and break P5. Why not one node per slot: slot 13 is a gap round, its nine topics belong with the topics of slots 05 and 06 they complete. Rejected cut: attack-surface only (browser, server, supply): would win if the guideline had separate browser and Node readers; the language-swap test and P5 favour the injection-class cut. Certainty: inferred.

**A2. Graph placement rule (inferred).** The extraction `level` decides the graph: `principle` and `js-principle` statements go to `js-philosophy`, `practice` and `decision` statements to `pig-js-defaults`, with these exceptions: demoted or mechanism-only claims become `fact` rows in the defaults graph; API-specific rules tagged `js-principle` (RUNSEC-C02, C13, C16, C22, C23, C27, C31, C35, SRVSEC-C39, C43, C53, C64; SRVSEC-C56 stays in the philosophy graph as a parser-differential principle) sit in the defaults graph; refuted beliefs sit where the belief lives. Rejected rule: the language-swap test applied sentence by sentence: would win for an editor who prefers a minimal philosophy graph, at the cost of moving about twenty hazard statements out of it.

**A3. One role per claim (certainty: grounded as a constraint of the ledger format).** A claim that is both a practice and a refutation of a belief carries one role; where the claim states the node's choice or its condition it keeps that role and the belief appears in the statement (RUNSEC-C47, C33, C09 and DOMSEC-C47); where its main content is the refutation it is a `rejected` row (18 rows). Folklore tags of slot 13 (SRVSEC-C01, C04, C23) were not audited by `12_dissent`, so those three rejected rows are inferred.

**A4. Deferred to web_architecture (grounded by routing notes).** DOMSEC-C26, C29, C59, C60, FW-C04, FW-C14, SRVSEC-C38 and DOMSEC-C35 are `deferred` with planned boundary links. DOMSEC-C28 stays as a `rejected` row (the belief that an allowlist CSP stops XSS) because the guideline states what not to believe, while the nonce policy itself is the sibling's. DOMSEC-C35 conflicts mildly with the register: SRC-111 is restricted to a code-level rule, yet routing marks the claim web-architecture; resolved by deferring the claim and keeping its code-level mechanism as a decision (DOMSEC-C36, no secrets in Web Storage). Overrule if the maintainer wants the token rule stated here.

#### DEFENSE: Part B. Contested topics decided by the max rule

**B1. Trusted Types default policy (DOMSEC-C17; node `PIG-JS.DEFENSE.DOM.4`).** Decision: named policies; the default policy only for migrating legacy code and for third-party code that cannot be changed. Positions: MDN and web.dev (SRC-120, SRC-267): transitional or last resort; Roth et al., USENIX 2024 (SRC-269, T2): with third-party code only a default policy works in practice. Rejected: default policy as normal practice, wins when the page loads third-party code that cannot pass typed values, which the decision already allows as the stated exception. Grounds: mechanism that a default policy is invoked implicitly for every string reaching a sink (grounded). Epistemic state: `known | conflict`.

**B2. setAttribute (DOMSEC-C25, with C04; `DOM.1`).** Decision: never set event-handler attributes from untrusted data; setAttribute is not unconditionally safe. Rejected: OWASP DOM XSS sheet (SRC-108, T1 restricted) says setAttribute is a safe construction method; it wins for attribute names that are not event handlers and whose values are not script, a condition not read verbatim in MDN. Grounds: DOMSEC-C04 (OWASP, consensus) and the MDN Trusted Types sinks list. Certainty: grounded for the positions, open for the MDN condition, which must be read verbatim before the final wording. Epistemic state carries `unvalidated: MDN TrustedScript condition inferred`.

**B3. target=_blank (DOMSEC-C47; `ORIGIN.2`).** Decision: write `rel="noopener noreferrer"` explicitly. Rejected: HTML Standard (SRC-103): noopener is implied unless `rel=opener`; wins on browsers implementing the default and for links where the Referer may be sent. The max rule takes the explicit form as harmless and covering older browsers (inferred, condition not read from a source).

**B4. Permission model (RUNSEC-C38; `HOST.1`).** Decision: a seat belt for trusted code, narrow grants, patched Node, never the only control. Positions: permissions API and threat model (SRC-128, SRC-140, T1): no guarantees against malicious code; best-practices page (SRC-078, T1 restricted): can help contain compromised dependencies. Rejected: containment of hostile dependencies by the model: wins only if Node later documents guarantees; CVE-2025-55130 and CVE-2026-58043 show over-grants. The inconsistency inside Node's own pages is carried forward, not hidden. Stability labels differ between the permissions page and the CLI page (open).

**B5. SQL identifiers (SRVSEC-C18; `INJECTION.3`).** Decision: allowlist mapping or query redesign. Rejected: escaping with pg-format (node-postgres docs, SRC-335), kept as `acceptable-when` for names that are genuinely dynamic, such as DDL; OWASP calls escaping fragile (SRVSEC-C19).

**B6. Native Sanitizer API against a sanitizer library (DOMSEC-C08, C11; `DOM.3`).** Decision: `setHTML` where available, a reputable library as the fallback, sanitize last. Rejected: library first, wins where target browsers lack `setHTML`, which is the stated fallback condition. The OWASP and MDN grounds for naming DOMPurify are not independent (OWASP is cited by MDN), and the register forbids grounding a DOMPurify preference on its own README or advisories. The advice to keep it current is inferred and was demoted to a fact (see Part C).

**B7. Freezing built-ins against never modifying them (RUNSEC-C09, X1 of the dissent audit; `PROTOTYPE.3`).** Decision: freeze application-owned configuration (shallow); lock down built-ins only in high-sensitivity code tested for breakage. Rejected: never freeze built-ins (SUBSET, LANG-C14): wins for general code, because freezing blocks later polyfills (inferred). Conflict link proposed to SUBSET.

**B8. Null-prototype forms (RUNSEC-C05, X3).** Decision: Map or Set first, `Object.create(null)` second as `acceptable-when`; the literal `{ __proto__: null }` is the weaker form (OWASP: last resort; MDN lists both).

**B9. Environment variables for secrets (RUNSEC-C47).** Decision: a weaker channel, acceptable only when no dedicated mechanism is possible. OWASP's passage is written in a container context; process-wide read access is inferred from the threat model. Agreement is majority.

**B10. Non-backtracking regex engine (RUNSEC-C33).** Decision: prefer one where available, do not assume V8 offers one. Status is as of 2021 (V8 blog); the current status was not checked and is open.

**B11. Dynamic evaluation (RUNSEC-C14 to C18, LANG-C49).** Decision: never evaluate untrusted strings. Rejected: Google's code-loader exception (a style-guide position, not evidence), `acceptable-when` for loaders the application itself writes; indirect strict eval, `acceptable-when` only when evaluation is unavoidable, since it reduces scope exposure and removes no injection risk.

**B12. SSRF: allowlist against deny-list (SRVSEC-C28, C31).** Decision: allowlist, request built by the server. Rejected: OWASP's minimum deny-list, `acceptable-when` an allowlist is impossible; deny-lists miss encodings and new ranges.

#### DEFENSE: Part C. Restriction demotions (grounded against `build/audit/source_register.md`)

Seven claims overstepped a restriction and were demoted; twelve more rest on vendor documentation admitted for facts only and are held at `fact`.

- DOMSEC-C07 (SRC-316, T3, catalogue facts only; its advice is not a ground): decision to `fact`.
- DOMSEC-C14 (SRC-098, SRC-099, facts only, no advice): the update advice is inferred; row is `fact`.
- DOMSEC-C21 (SRC-265, Mozilla's position as that vendor's): `fact`.
- DOMSEC-C28 (SRC-263, 2016 measurement of allowlist bypasses, deployment policy is web-architecture): `rejected` belief, not a decision.
- RUNSEC-C11 (SRC-273, prevalence evidence only, not a recommendation): `fact`.
- SRVSEC-C13 (SRC-342 restricted to CSPRNG principles and the listed Node functions; algorithm advice is outside): `acceptable-when`, one position only.
- SRVSEC-C11 (SRC-336 requires a verbatim read of each crypto section; scrypt defaults came through a v10 digest): `fact`, inferred.
- Held at `fact` as vendor documentation: FW-C01, C03, C05, C06, C08, C09, C10, C11, C12, C18, C19, C20.
- Judgement calls kept as decisions, listed so the maintainer can overrule: SRVSEC-C16 and C20 (driver facts rendered as the parameter channel, no preference between drivers), SRVSEC-C47 (Express `root` option), SRVSEC-C22 (least privilege from SRC-345, not in the register's list of principles but of the same kind), SRVSEC-C30 and C31 (SRC-346 principles, the CIDR list is OWASP's content), SRVSEC-C41 (rejection derived from advisory facts), DOMSEC-C56 (ASVS requirement, mechanism from a T3 catalogue).

#### DEFENSE: Part D. Decisions resting on a single source

Each carries `unvalidated` in the node's epistemic state where the rule says so. DOMSEC-C05 (SRC-097), C18 (SRC-267), C19 (inferred, T2), C37 (inferred, T2 and T3), C45, C46, C56, C58; RUNSEC-C12, C24 to C26, C29 (T2, recipe inferred), C34, C35, C37 (T2, Node TSC author), C40 (inferred); SRVSEC-C05 to C09, C10 (OWASP position, language-neutral), C12, C22, C26, C27, C28, C29, C30, C32, C33 (synthesis of three rows), C42, C47, C49, C50, C52, C53, C56 to C58, C60, C61, C63, C64; RUNTIME-C13, C15, C18 (inferred), C51, C52 (inferred); TYPES-C31. The weightiest: SRVSEC-C10 (password-hashing parameters, an OWASP position nothing else measures) and SRVSEC-C33 (pinned connection, a synthesis no admitted source states).


### DEPENDENCIES


Selection rule: max, not average (`../../target_hierarchy.md`). Each entry gives the decision, the rejected positions with the condition under which each would win, the grounds and the epistemic state, so the maintainer can overrule. Uids are in `skeleton.md`, rows in `ledger.md`.

#### DEPENDENCIES: Decisions

##### DEPENDENCIES: D1. Framework short list (weighty choice, build judgment)

- Superseded in part (RELAX): the list is a snapshot of the evidence, not a closed set; see section "Re-judged under best".
- Decision: the short list is (1) the platform with Web Components and no framework, the default and first candidate; (2) htmx; (3) Lit; (4) Angular; (5) React. The four frameworks are unranked: no admitted source can rank them, and framework documentation grounds facts about that framework only. Node `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`, rows DEPENDENCIES-048 to DEPENDENCIES-077 (evidence and platform baseline) and the judge record in `skeleton.md`.
- Status after the stage 7 review: the gates and the platform-first default are the build's judgment, not stated by any admitted source (flagged `risky | unvalidated` on the node).
- Gates, derived from the guideline's own trust rules: A (mandatory) the candidate states which versions receive security fixes, because the guideline runs only supported versions (TYPES-C45, SUPPLY-C36, SUPPLY-C28); B a documented escape and sanitization model (slot 10 matrix, owned by DEFENSE); C stated governance or maintenance body. A and at least one of B or C. The gates are the build's judgment; no admitted source states them.
- Matrix result: React A yes, B yes, C yes (provisional); Angular A yes (strongest, 24 months), B yes, C no source; Lit A yes, B no source, C yes; htmx A yes, B yes, C no source; Vue A no, B yes, C partial; Svelte A no, B yes, C no source; Solid A no, B no, C partial.
- Rejected, with the condition under which each would win:
  - Keep Vue, as the slot 10 proposal does (holder: slot 10 L2, inferred): wins if an admitted source states a Vue security-fix window and a legal entity or funding. Closest runner-up.
  - Keep Svelte: wins with a supported-versions statement (FW-C27 states none) and a governance source.
  - Keep Solid: wins with a support policy (FW-C29, FW-C30) and a default-escaping description (FW-C15, FW-C16).
  - Rank or choose by popularity: rejected by the register's standing rule; only React (10 percent) has a measured figure (FW-C42, FW-C49). Wins if an admitted per-candidate measurement with method exists (HTTP Archive technology data read as data).
  - Always adopt a framework: wins when a requirement exists that the platform does not meet and the SUPPLY-C27 isolation test confirms it.
- Grounds: T1-restricted facts from each framework's own documentation (single-source each), MDN and the HTML Standard for the platform (T1). Epistemic: known | unvalidated: build judgment over single-source facts | conflict: keep Vue.
- Open: the choice among the four frameworks for a given application depends on rendering strategy, owned by web-architecture, and on the type-layer decision, owned by CONTRACTS.

##### DEPENDENCIES: D2. Dependency pinning (contested, SUPPLY-C06)

- Decision: the committed lockfile fixes the whole tree and CI installs it frozen; direct dependencies of an application are declared at exact versions so every change is a reviewed diff; versions move only by deliberate update (cooldown, audit triage, lockfile diff review). Node `DEPENDENCIES.CHANGE.2`, row DEPENDENCIES-024, with `STRUCT-C67` rejecting the belief that minor and patch releases are safe.
- Positions: exact pin of a specific immutable version (Node security guide, SRC-078); verified version through the lockfile (OWASP supply-chain sheet, SRC-156); minimum-to-latest range (OpenSSF npm guide v1.1, SRC-154, archived 2023); direct pinning can raise exposure to malicious updates in larger graphs, prefer collective ecosystem pinning (SRC-287, T2).
- Rejected: ranges only (SRC-154): acceptable for a published library whose consumers inherit its declarations, with the lockfile still committed for applications; this scope is inferred from 12_dissent, not stated by a source. Collective ecosystem pinning (SRC-287): a registry-level measure, not actionable by one project; its warning that pinning alone is no defence is kept as fact in SUPPLY-C05.
- Grounds: lockfile committed is confirmed by four T1 sources; exact direct pins by SRC-078 (T1 restricted) and CISA's pre-incident pin (SUPPLY-C41); 44 percent of manifesting breaking changes arrived in minor and patch releases (STRUCT-C67, T2).
- Epistemic: known | conflict: ranges only, SRC-154; collective ecosystem pinning, SRC-287 | unclear: library scope inferred. For review: whether SRC-287's finding should weaken the exact-pin part; the build kept the more demanding practice.

##### DEPENDENCIES: D3. Release-age cooldown (single T1 assertion, effect open)

- Decision: enable the tool's cooldown where one exists (npm min-release-age from v11.10.0, pnpm minimumReleaseAge default 1440 minutes, Dependabot default 3 days), and keep security updates outside it. Node `PIG-JS.DEPENDENCIES.UPDATE.1`, row DEPENDENCIES-037.
- Rejected: no cooldown (wins for a version fixing an exploited vulnerability, which the security exemption covers); a three-day figure as evidence (OpenSSF concise guide, QUALITY-C46, origin not found: recorded as the body's position only); a longer custom duration (no source, undecided node UPDATE.1.1).
- Grounds: SRC-078 mitigations (one T1 assertion); tool facts SRC-152, SRC-158, SRC-146. SUPPLY-C12 is labelled consensus by the claim table and is relabelled single-source (12_dissent X5). No peer-reviewed measurement exists (SUPPLY-C13; vendor figures SRC-319).
- Epistemic: known | gap: effectiveness unmeasured.

##### DEPENDENCIES: D4. Install scripts blocked by default, per-package exact-version allowlist

- Decision: keep the default block (npm 12, pnpm 10 and later) and approve reviewed packages by allowlist pinned to the exact version, never disabling the guard globally. Node `PIG-JS.DEPENDENCIES.INSTALL.2`.
- Rejected: global `--ignore-scripts` plus allowlist is acceptable only where the manager still runs scripts by default (npm before v12); running all scripts has no support.
- Grounds: SRC-153 and SRC-158 (manager docs), SRC-078 and SRC-155 (Node and OWASP), SRC-288 (eslint-scope postmortem). Epistemic: known.

##### DEPENDENCIES: D5. Accept only signed components and generate SBOMs (very demanding, single T1)

- Decision: validate signatures before use, accept only signed components, generate and consume SBOMs in CI. Node `DEPENDENCIES.EVIDENCE.1`, row DEPENDENCIES-018.
- Why flagged: the claim rests on one T1 source (OWASP supply-chain sheet, SRC-156) and no admitted source measures how many npm packages carry signatures a consumer can validate; registry signatures detect mirror tampering only (SUPPLY-C19). Read it as the guideline's ceiling, applied where signatures exist.
- Rejected: reading a signature or provenance as a safety verdict (folklore refuted, SUPPLY-C18, SUPPLY-C19). Epistemic: known.

##### DEPENDENCIES: D6. htmx major version (contested by scope, FW-C22)

- Decision: pin a supported major and read the documentation of that major; a new adoption takes the newest supported major (4.x). Node `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1`.
- Rejected: 2.x as the current line (the main docs site, SRC-213): wins for an existing 2.x project while 2.x stays supported; same for 1.9.x. The htmx 4.0.0 release year is open (the release page gave the fetch tool no reliable year).
- Epistemic: known | conflict: main docs site documents 2.x | unvalidated: 4.0.0 release date open.

##### DEPENDENCIES: D7. Production on Active or Maintenance LTS of Node (single T1)

- Decision: production Node.js on an Active or Maintenance LTS only (TYPES-C45, SRC-037). Node `PIG-JS.DEPENDENCIES.UPDATE.2`, with the toolchain pinned to the framework's compatibility table (FW-C24, FW-C26).
- Rejected: Active LTS only is more demanding but no admitted source says Maintenance LTS is insufficient (wins if a T1 source states it); Current in production has no support. Epistemic: known.

##### DEPENDENCIES: D8. Measured usage is context, never a selection ground

- Decision: usage figures (jQuery 74 to 75 percent, React 10 percent, custom elements 7.8 percent, shadow DOM 2.5 percent, 2024) are context only. Node `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4`, rejected row FW-C49. Rejected: ranking by usage; wins only with per-candidate admitted data. Epistemic: known.

##### DEPENDENCIES: D9. Single-source or inferred decisions that carry the branch (low blast radius each)

- Single T2 ground: SUPPLY-C32 (layered controls, inferred), SUPPLY-C41 (CISA's incident response, recorded as the body's position), SUPPLY-C30 (expired domains, fact), SUPPLY-C23, SUPPLY-C25, STRUCT-C67 (folklore refuted by one study each: `known | unvalidated: single T2 source`).
- Single T1 ground: SUPPLY-C07 (lockfile diff review, inferred from an attack-vector list), SUPPLY-C11 (npm 12 git and tarball defaults, inferred), SUPPLY-C27, SUPPLY-C39, SUPPLY-C33, SUPPLY-C37, TYPES-C07, TYPES-C45, SUPPLY-C21, SUPPLY-C26.

#### DEPENDENCIES: Open facts that bound decisions (not nodes)

- Governance has no source for Angular, Svelte, htmx (FW-C35); support policy none for Svelte, Solid, Vue (FW-C27, FW-C29, FW-C30, FW-C26); type support none for htmx (FW-C41); default escaping none for Solid and Lit (FW-C16); measured usage none for six candidates (FW-C49).
- Late candidates that would close them are listed in the slot 10 result: Lit templates documentation, Solid JSX documentation, HTTP Archive technology data, the TypeScript handbook JSX page, the htmx 4.0.0 release page.

### VERIFICATION


Purpose of the branch: automation. Max rule: the most demanding practice that serves automation
and that an admitted source supports. Each entry gives the decision, rejected positions with the
condition under which each would win, and the grounds. Conditions marked (inferred) come from
reasoning, not from a source. Node uids refer to `skeleton.md`, rows to `ledger.md`.

#### VERIFICATION: Decisions

##### VERIFICATION: D1. Coverage is reported, never a target (VERIFICATION.TEST_SUITE.2; rows 006, 007)
- Decision: use coverage to find code no test executes; set no coverage percentage as a quality target or CI gate. Known | conflict.
- Rejected: (a) gate on a high percentage (the folklore "high coverage means effective tests"; also the maximal reading of OpenSSF's suggestion to cover most or all branches). Wins if a study on JavaScript suites, controlling for suite size, found coverage tracking fault detection; none is admitted. (b) OpenSSF passing criteria, SRC-174, T1: it SUGGESTS covering most or all branches and inputs; compatible with this decision if coverage is read as a finding tool, not a gate.
- Grounds: the Inozemtseva and Holmes study (SRC-297, T2, named in the claim table): correlation with effectiveness is low to moderate once suite size is controlled (31,000 suites, five Java systems). The decision is language-neutral, so it sits in `js-philosophy`; transfer to JavaScript is inferred. Matches 12_dissent topic 15 and question Q10.
- Max reading: the demanding practice here is not "more coverage" but measuring detection power directly (D6).

##### VERIFICATION: D2. A dedicated formatter owns layout, checked in CI (FORMAT.1, FORMAT.2; rows 031, 032, 033)
- Decision: layout is produced by a dedicated formatter, not by lint rules, and CI runs it in check mode so unformatted code fails the build. Known | unvalidated: single T2 source (FORMAT.1); known (FORMAT.2, T1 facts about the Prettier CLI).
- Rejected: layout through ESLint core formatting rules, deprecated by the ESLint team (SRC-298, SRC-167); wins never for new code. The `@stylistic` plugin, which keeps formatting in ESLint, remains an acceptable option under FORMAT.3 (D15). CI that writes files, wins only for a bot that commits formatting by design (inferred).
- Grounds: ESLint technical steering committee (SRC-298, T2) names the position; Prettier and Biome documents agree layout is separate (12_dissent topic 14, "checked and not a tension").
- Partial demotion: the pre-commit hook in QUALITY-C16 is Prettier's optional suggestion ("you may be interested"), kept as an option in the statement, not a requirement.

##### VERIFICATION: D3. Warnings fail CI (LINT.2.1; row 025)
- Decision: `--max-warnings 0`. Known (T1, documented exit-status rule).
- Rejected: ESLint's default of no limit, under which warnings never change the exit status. Wins during a staged migration that has a recorded end date (inferred).
- Weighty because it is the most demanding setting for a gate; the claim's certainty is inferred from the documented exit rule and the default of -1.

##### VERIFICATION: D4. Typed linting is on in TypeScript projects (LINT.1.4; rows 023, 024)
- Decision: enable typed linting (`parserOptions.projectService`) and budget its cost. Known | gap: no cost figure (G-L20 of 11_coverage).
- Rejected: syntax-only linting; wins where there is no TypeScript project to analyze, or where measured lint time blocks work (inferred). Tool-dependency risk: TypeScript 7.0 ships no API, a different one is expected in 7.1 (SRC-034); the consequence for tools is inferred.
- Grounds: typescript-eslint docs (SRC-181, T1).

##### VERIFICATION: D5. Strict type-aware config only for proficient teams (LINT.1.3; row 022)
- Decision: strict set when a nontrivial share of the team is highly proficient in TypeScript; otherwise the recommended set (LINT.1.2). Known (T1, the project's own position, unrestricted for this slot).
- Rejected: strict for all (the project itself denies it); wins once the team meets the condition. Churn: the set may change outside major versions.

##### VERIFICATION: D6. Mutation testing, incrementally, on changed code (VERIFICATION.FAULT_DETECTION.1; rows 011, 012)
- Decision: where mutation testing is adopted, run it on changed code during review and filter mutants. Known | unvalidated: single T2 source, abstract-level.
- Rejected: mutating the whole code base on every run (the source runs mutation incrementally on changed code instead); wins on a small code base where a full run is cheap (inferred). Whether to REQUIRE mutation testing has no admitted source and is not decided (open, see O1 in `result.md`).
- Grounds: the Google mutation-testing paper (SRC-299, T2 restricted: abstract-level facts only until the full text is read). Definitions: SRC-179 (StrykerJS facts) and the same abstract.

##### VERIFICATION: D7. Flakiness is prevented at its causes (TEST_STABILITY.1 and .2, TESTS.3; rows 016, 017, 043)
- Decision: probe new tests extensively when added, clean shared state between tests, wait on conditions not delays. Known | unvalidated: single T2 source, transfer inferred.
- Rejected: fixed delays in asynchronous tests, the largest flake category in the study (45% Async Wait); they win never as a default. No admitted source discusses retry-on-failure; not claimed.
- Grounds: the empirical flaky-test study (SRC-296, T2, 201 commits, 51 mostly Java projects). The Playwright half of row 043 is a tool fact (SRC-175, restricted).

##### VERIFICATION: D8. Static analysis is a baseline and not the only mechanism (STATIC_BASELINE.1 to .3; rows 001 to 004)
- Decision: a linter or safe mode is on and its warnings addressed; one analyzer beyond compiler warnings runs before major releases; several checks run together with negative tests. .1 and .2 known (SRC-174, T1 MUST). .3 known | unvalidated: single T2 evidence plus one working-group position.
- Rejected: lint alone as the verification mechanism; DLint found 49 problems per site that static analysis missed on average (2015, SRC-237, evidence of occurrence only, no current-language claim). Wins never.
- Restriction handling: SRC-163 is admitted for the OpenSSF Best Practices Working Group's positions; row 004 is kept as that position with the holder named, which the restriction allows.

##### VERIFICATION: D9. The gate job must always run (ENFORCEMENT; row 019)
- Decision: a required check that can be skipped is a hole; make the gate job run on every change. Known | unvalidated: practice inferred from a platform fact.
- Rejected: relying on conditional jobs as required checks (GitHub counts skipped and neutral as passing, SRC-169); wins nowhere on GitHub. Other hosts: no admitted source (open).
- Sits in `js-philosophy` by the language-swap test even though the grounds are GitHub's.

##### VERIFICATION: D10. Property-based testing uses real-data distributions (FAULT_DETECTION.2; rows 013, 014, 015)
- Decision: custom generators whose distribution follows actual data. Known | unvalidated: single T2 source.
- Demoted: row 015 (properties beside the code as documentation) is the QuickCheck authors' practice, outside the method for which SRC-300 is admitted; kept as acceptable-when. Row 013: shrinking rests on fast-check's docs only (SRC-168), not on the paper. No admitted source says property-based tests beat example tests (SRC-168 restriction); not claimed.

##### VERIFICATION: D11. ESLint practices are stated, the linter family is not (LINT.1.1, 1.2, 2.x; rows 020 to 028)
- Decision: the practices (flat config, recommended baseline, warnings fail, exit codes, stale suppressions, cache) are decided as ESLint practices because the admitted tool documents ground them. Each rests on one T1 ground, so each is known.
- Rejected: none at this node. The linter-family choice is D14, a judgment on tool facts, not a claim by any tool document that ESLint is better.

#### VERIFICATION: Single T1 ground, known, no weighty alternative

Rows 002, 003, 005, 020, 021, 026, 027, 028, 029, 041 each rest on one T1 document and carry no
contested position. Listed so the reviewer can overrule any without searching: SRC-174 (C20, C21,
C22), SRC-166 and SRC-167 and SRC-054 (C01 to C04), SRC-165 (C06, C07, C08), SRC-164 (C45),
SRC-171 (C25).

#### VERIFICATION: Decisions added after the maintainer's standing decision

The coordinator applied "max(all sources), pick the best" to the five nodes first left undecided.
Tool documents ground facts about each tool; the choice among tools is judgment against the
branch purpose, automation, recorded with each rejected tool's winning condition (judge records
in `skeleton.md`).

##### VERIFICATION: D12. Test design (js-philosophy VERIFICATION.TEST_SUITE.3; rows 008, 009, 010)
- Decision: test behaviours through the public interface, one test per behaviour, DAMP over DRY; prefer real collaborators when they are fast and deterministic. Known | unvalidated: single T3 source, Google position.
- Searched: the branch claims, 12_dissent (topics, tensions, folklore) and 11_coverage (gaps G-L, overlaps) for any other position on test scope, mocking or test mix; only SRC-320 and SRC-321 (Google, T3, restricted to Google's position) exist.
- Restriction override, flagged: the register says "Google's positions, never as evidence". I recorded the position as the decision because it is the only admitted position and the maintainer rule forbids abstaining; the epistemic state says so. Reviewer may revert rows 008 and 009 to acceptable-when.
- Rejected: per-method tests and mock-everything (the positions Google's text contrasts with); win when real collaborators are slow or nondeterministic (the source's own condition). The 80/15/5 mix (row 010) stays acceptable-when for organizations with Google-like test infrastructure: a size ratio is Google's own, not a rule.

##### VERIFICATION: D13. Flake rate (js-philosophy VERIFICATION.TEST_STABILITY.3; row 018)
- Decision: track the flake rate and act as it approaches 1%. Known | unvalidated: single T3 source, Google figures (0.15% reported, value lost near 1%).
- Searched: same corpus as D12; no other threshold exists.
- Restriction override, flagged as in D12: figures are Google's; the threshold is theirs, adopted as the only admitted one. Reviewer may revert row 018 to acceptable-when.
- Rejected: no tracking, rejected by the T2 flaky-test study's finding that tests are flaky from the first run (D7); a different threshold wins when the organization measures its own.

##### VERIFICATION: D14. Linter family: ESLint with typescript-eslint (PIG-JS.VERIFICATION.LINT.4)
- Decision: ESLint with typescript-eslint. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: documented type-aware rules and no-floating-promises (SRC-181), documented exit codes and warning gates (SRC-165), security plugin (SRC-164), flat config and baselines (SRC-166, SRC-167, SRC-054), and every other branch cites ESLint rule documents.
- Rejected: Biome; wins when one tool and one dependency for lint and format is wanted and its shipped rules cover the project's needs (inferred). Its unsafe fixes need manual review (row 030).

##### VERIFICATION: D15. Formatter: Prettier (PIG-JS.VERIFICATION.FORMAT.3)
- Decision: Prettier, run apart from ESLint, eslint-config-prettier to disable conflicts, check mode in CI. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: prints only and never transforms code (SRC-178), check-mode exit codes 0, 1, 2 (SRC-176), documented ESLint integration (SRC-177); named first by the ESLint steering committee (SRC-298), not as a ranking.
- Rejected: Biome formatter (wins when Biome is the linter); @stylistic (wins if a team wants one lint pipeline and accepts the sustaining cost ESLint's team named); dprint (no admitted behaviour facts; wins when a source gives them).
- Restriction check: SRC-178 and SRC-177 never ground "Prettier is better"; the choice rests on automation fit (documented check mode and integration), stated as judgment.

##### VERIFICATION: D16. Runner: node:test (PIG-JS.VERIFICATION.TESTS.1)
- Decision: node:test; no gate on its experimental coverage flag. Known | unvalidated: chosen by judgment on tool facts, no independent ranking source.
- Grounds: built into Node, stable from v20.0.0, exit code 1 on failure (SRC-172); no added dependency, which serves DEPENDENCIES' trust purpose. Vitest requires Vite and a recent Node and defaults to watch mode (SRC-183); Jest needs Babel or ts-jest for TypeScript (SRC-170).
- Rejected: Vitest (wins with an existing Vite build, or when stable coverage providers matter, SRC-182); Jest (wins for a large existing suite and its transforms).


### RUNTIME


Each decision settled a contested or weighty choice, or rests on a single source. Nodes are
named by uid in `skeleton.md`, rows by id in `ledger.md`. Rejected positions carry the
condition under which they would win, so the maintainer can overrule.

#### RUNTIME: Decisions

##### RUNTIME: D1. Measurement first outranks unmeasured micro-optimization

- Nodes: `PIG-JS.RUNTIME.MEASURE.2` (rows RUNTIME-007 to RUNTIME-012), `RUNTIME.MEASURE` (RUNTIME-001).
- Decision: no engine-level restructuring (holey arrays, hidden classes, nested function creation, prototype mutation) without a measurement of the real workload.
- Rejected: restructuring on mechanism alone, held by MDN's closure and `setPrototypeOf` warnings (STRUCT-C42 on SRC-083, STRUCT-C43 on SRC-088, T1, no figures); wins when a profile shows the cost on a hot path. Belief "holey arrays must be avoided for speed": wins only under a measurement.
- Grounds: V8 states the holey versus packed difference is usually too small to matter or even be measurable (SRC-302, T2, single); no T1 specifies engine performance (RUNTIME-C63, inferred from register restrictions); the profile-first workflow (SRC-195, T1); cross-slot tension X4 of 12_dissent, a difference of scope, not counted contested.
- Weakness: no source states the measurement-first rule itself in normative form; it is inferred from SRC-195, SRC-302, SRC-305 and SRC-307. Engine claims rest on T2 only, so the measured statement is `unvalidated: single T2 source`. Evidence that would settle it: an independent T2 on engine performance (gap G-M31) or a T1 statement.
- Cross-branch: the STRUCTURE branch must not restate STRUCT-C42 and C43 as decisions (both are placed here); proposed link 1 of `skeleton.md` asks the integrator to gate any speed-motivated structure rule.

##### RUNTIME: D2. Two MDN performance warnings placed as acceptable-when (restriction check)

- Rows RUNTIME-009 (STRUCT-C42) and RUNTIME-010 (STRUCT-C43).
- SRC-083 admits "closure mechanism and the performance note only", so RUNTIME-009 does not overstep its restriction; its role follows the max rule (D1). SRC-088 admits "mechanism facts", so the directive form "set the prototype at creation" of RUNTIME-010 is a demotion from practice to acceptable-when with the mechanism as fact.
- Would win: a profile on the real workload showing the cost.

##### RUNTIME: D3. Promise file APIs by default, callbacks on a measured need

- Node `PIG-JS.RUNTIME.MEASURE.3`, row RUNTIME-013. Single T1 source (SRC-188), quote tool-extracted.
- Decision: promises by default (shared async style, owned by CONTROL), callbacks only where measurement shows the need. The docs say callbacks are preferable "when maximal performance is required"; the measurement gate and the default are inferred from the branch rule.
- Rejected: callbacks everywhere; wins when a file-heavy hot path measures the promise overhead as significant.
- Boundary: slot 03 owns promise style; proposed link 2.

##### RUNTIME: D4. Benchmark method placed in both graphs

- Nodes `RUNTIME.METHOD` (philosophy, RUNTIME-002) and `PIG-JS.RUNTIME.METHOD.1`, `.2` (defaults, RUNTIME-014, RUNTIME-015).
- Split by the language-swap test: C61 and C62 (distribution, confidence intervals, setup variation) hold for any runtime and rest on two independent T2 (SRC-307, SRC-305), so `known`. C58, C59, C60 carry Node core's figures and settings (SRC-304 T2) and stay in defaults.
- Weakness: SRC-307 is about Java and SRC-305 about SPEC CPU C programs; transfer to JavaScript is inferred (C58 certainty inferred). SRC-304 is the only JavaScript-runtime ground, single T2. Restrictions respected: abstract-level only for SRC-305, no Java numbers from SRC-307.
- Rejected: single timings; wins when the difference is so large that noise is implausible (condition, unsourced).

##### RUNTIME: D5. WeakRef and FinalizationRegistry avoided

- Node `PIG-JS.RUNTIME.MEMORY.5`, row RUNTIME-028 (C28, C29, C14, three T1 pages from MDN and Node docs; the two MDN pages count as one ground).
- Decision: weak collections for object-keyed metadata, no weak references, `try...finally` for release, `allocUnsafeSlow` for long-retained small Buffers.
- Rejected: WeakRef and FinalizationRegistry for cleanup; wins when no deterministic release exists and a missed cleanup is harmless.
- Weakness: the ECMA-262 processing-model notes were not read (gap G-M04, G-L10).
- Merge note: three claims in one row because they share one purpose, retaining only what is intended; split if the integrator prefers one decision per source.

##### RUNTIME: D6. Production capture and near-limit capture

- Node `PIG-JS.RUNTIME.MEMORY.4`, rows RUNTIME-024 to RUNTIME-027. All T1 except C57 (T2).
- Decision: sampling heap profiler in production; snapshots only where a crash is harmless; trigger never public (boundary: DEFENSE, proposed link 4).
- Acceptable-when: `--heapsnapshot-near-heap-limit` (RUNTIME-025) when a snapshot is wanted at that moment.
- Rejected: belief that snapshots are infeasible on large heaps; wins on V8 older than 11.5.130. The Node version carrying the fix is open (not stated in SRC-306).

##### RUNTIME: D7. Heap limit changed only for a measured need

- Node `PIG-JS.RUNTIME.MEMORY.6`, rows RUNTIME-029 to RUNTIME-031.
- The only-for-measured-need rule is inferred (C48 certainty inferred); manual `global.gc()` as a leak remedy is rejected on SRC-199 (T1). Concurrent marking (C54) is a dated V8 fact, not a prescription.
- Rejected: `global.gc()` as remedy, never; hand-tuning the collector, wins when a GC trace shows starvation and a measurement ties it to the setting.

##### RUNTIME: D8. Folklore rows without claim ids

- Rows RUNTIME-004, RUNTIME-011, RUNTIME-012, RUNTIME-027 carry `-` as claim_ids: the refuted or restricted belief has no claim of its own (its claim is the decision row of the same node). Placing the claim twice would break the exactly-once rule. The integrator may keep `-` or fold the rows into their decision rows.
- Beliefs: circular references cause leaks (refuted, RUNTIME-004); holey arrays must be avoided for speed (restricted, RUNTIME-012); heap snapshots infeasible on large heaps (restricted, RUNTIME-027).

##### RUNTIME: D9. Epistemic markers beyond the brief's list

- The brief lists `unvalidated: quote tool-extracted` for the only T1 ground. Used as written where the sole T1 quote is tool-extracted. Where a claim records no quote (RUNTIME-C23 and C48 on T1, C60 on T2) the node says what is missing instead (for example `C23 no quote recorded`). Judgment call, for review.

##### RUNTIME: D10. No philosophy node for diagnosis

- Diagnosis has no language-neutral claim in the branch (C25 is Node-specific), so the philosophy graph holds three L2 nodes (MEASURE, METHOD, MEMORY) and the defaults node `PIG-JS.RUNTIME.DIAGNOSE` links to `RUNTIME.MEASURE`. Not invented; no source supports a separate principle.


## Undecided nodes

Every node whose epistemic state is `undecided`, with the evidence that would settle it (copied from the branch).

Undecided nodes in the skeleton: `PIG-JS.CONTROL.ERRORS.2.1`, `PIG-JS.CONTROL.PROMISES.4.1`, `PIG-JS.CONTROL.SCHEDULING.2.1`, `PIG-JS.DEFENSE.INJECTION.4.4`, `PIG-JS.DEPENDENCIES.PUBLISH.4`, `PIG-JS.DEPENDENCIES.SCREEN.3`, `PIG-JS.DEPENDENCIES.UPDATE.1.1`, `PIG-JS.DEPENDENCIES.UPDATE.3.1`, `PIG-JS.RUNTIME.MEMORY.6.1`, `PIG-JS.STRUCTURE.DIRECTION.3`, `STRUCTURE.DIRECTION.2` (13).

### SUBSET

None.

### CONTRACTS


None. Remaining open items, not nodes: whether the compiler verifies type predicate bodies (no
admitted source); an independent ranking of schema libraries (none admitted); overloads whose
return type depends on the argument type (not stated by the handbook page read).

### CONTROL


PROMISES.6 is decided (D14); three nodes remain undecided.

| node | question | evidence that would settle it |
|---|---|---|
| PIG-JS.CONTROL.PROMISES.4.1 | Concurrency limits, retry, backoff | An admitted T1 or two T2 sources on bounded concurrency and retry with jitter (11_coverage G-M08: LC-10 RFC 9110 Retry-After, a T1 candidate; LC-11 Amazon Builders' Library is T3 and cannot make a node known) |
| PIG-JS.CONTROL.ERRORS.2.1 | Operational versus programmer errors, detail shown to callers | An admitted source on error classification (11_coverage G-M07: LC-08 Pacheco not located; G-M16 for disclosure, owned by DEFENSE) |
| PIG-JS.CONTROL.SCHEDULING.2.1 | Yielding to the main thread in browsers | An admitted browser-support statement for scheduler.yield (11_coverage G-M09: LC-12 MDN Scheduler.yield is a T1 candidate, not admitted) |

Open notes (not nodes): return await inside try/catch is not evaluated by SRC-246 (ASYNC-C53);
ECMA-262 and HTML Standard clause text were not read by the extraction slots (11_coverage G-M04), so
mechanism cells rest on MDN and Node docs; async iteration and structured concurrency (G-L02) have no
claim.

### STRUCTURE


##### STRUCTURE: U1. Declared layering (STRUCTURE.DIRECTION.2 in js-philosophy, PIG-JS.STRUCTURE.DIRECTION.3 in pig-js-defaults)
- State: `undecided | missing: no admitted source grounds a layering principle`.
- Why: STRUCT-C60 (open) cites SRC-085 (ESLint no-restricted-imports) and SRC-257 (Parnas). The register restricts SRC-085 to the mechanism ("grounds no layering principle"); the rule's own text gives environment fit and standardisation as reasons; SRC-257 supports hiding, not layering. STRUCT-C60 was therefore demoted to a `fact`, STRUCT-C61 kept as the mechanism fact.
- Evidence that would settle it: an admitted T1 source, or two independent T2 sources, stating a rule on which module kinds may import which, with grounds; or an empirical study linking dependency direction or layer violations to cost of change. `11_coverage` gap G-M10 and the "second T2 lead not yet audited" in STRUCT-C60's mechanism column point to the candidate to audit.


### DEFENSE


| node | question | evidence that would settle it |
|---|---|---|
| `PIG-JS.DEFENSE.INJECTION.4.4` | What is the Node recipe for path containment (SRVSEC-C55, RUNSEC-C29, SECGAP2-C82)? The grounded pieces moved to `INJECTION.4.1` in the slot 14 patch; missing: the symlink-resolving Node call and the separator-aware test | A readable Node `fs.realpath` entry and a source stating the comparison, for example the hapi fix commit (late candidate LC-01) |

Open points that did not become nodes: SRVSEC-C14 (current Node documentation of `timingSafeEqual` and `randomBytes`, `randomInt`, `randomUUID`, not grounded; fix by reading the current crypto page in full, filed as a `fact` row on `SECRETS.4`); the MDN condition for `setAttribute` (B2); the current status of V8's non-backtracking engine (B10); the stability labels of the permission model (B4).

### DEPENDENCIES


##### DEPENDENCIES: PIG-JS.DEPENDENCIES.SCREEN.3: typosquatting screening procedure
- State: undecided | missing: no admitted T1 source states a screening procedure for adding a dependency (SECGAP2-C54); one T3 paper (C52) and one T3 preprint (C53) describe name-similarity methods.
- Settled by: a T1 statement of a screening procedure (npm, OpenSSF or a registry operator), or a measurement of such a method's precision at T2.

##### DEPENDENCIES: PIG-JS.DEPENDENCIES.UPDATE.1.1: cooldown length beyond the tool defaults
- State: undecided | missing: no admitted source gives a measured duration.
- Settled by: a peer-reviewed or primary measurement of time-to-removal of malicious package releases, or the origin of the OpenSSF three-day figure (QUALITY-C46).

##### DEPENDENCIES: PIG-JS.DEPENDENCIES.UPDATE.3.1: failing severity of the audit gate
- State: undecided | missing: no admitted source names a level.
- Settled by: an authoritative statement of which `audit-level` to fail on, or a study linking advisory severity to reachability (SUPPLY-C22 measures noise, not a threshold).

##### DEPENDENCIES: PIG-JS.DEPENDENCIES.PUBLISH.4: target assurance level of a published package
- State: undecided | missing: no admitted source recommends a SLSA Build level for an npm package; SLSA v1.2 defines levels only (SUPPLY-C33).
- Settled by: a recommendation of a target level by SLSA, OpenSSF or npm, or npm documentation stating the level reached by trusted publishing with provenance.


### VERIFICATION


None. The five nodes first left undecided (LINT.4, FORMAT.3, TESTS.1, TEST_SUITE.3, TEST_STABILITY.3) are decided in D12 to D16, each marked `unvalidated` where it rests on judgment or a single T3 source. Open: whether to require mutation testing (O1 in `result.md`), which no admitted source addresses and no node claims.

### RUNTIME


| uid | graph | what is missing | evidence that would settle it |
|---|---|---|---|
| PIG-JS.RUNTIME.MEMORY.6.1 | pig-js-defaults | Behaviour of the default heap limit and of `--max-old-space-size` under a container or cgroup memory limit; the docs read state none (C48). Gap G-M22 of 11_coverage, candidate LC-36 not located. | A Node.js documentation page or T2 study on default heap limits in containers (candidate LC-36), then a rule for sizing the limit against the container limit. |

Noted gaps with no node (low priority or owned elsewhere): AsyncLocalStorage cost and
`diagnostics_channel` stability (G-L10, G-L17, LC-33), leak prevalence studies (G-L10), browser
long tasks (G-M09, CONTROL), supervisor-side shutdown (G-M23, boundary web architecture).

