# Patch result: slot 14_secgap2 (second security gap round) folded into the two graphs

## L1 headline

All 90 claims of slot 14_secgap2 are placed once in the ledger (0 dropped), 17 defaults nodes were added, three undecided nodes were decided (`PIG-JS.DEFENSE.DOM.2.3`, `PIG-JS.DEFENSE.INJECTION.5.3`, `PIG-JS.DEFENSE.INJECTION.6.4`, each as a composed rule marked `known | unvalidated: inferred from <claims>`), one stays undecided (`PIG-JS.DEFENSE.INJECTION.4.4`, with the grounded pieces moved to `INJECTION.4.1`), and both graphs were rebuilt and re-validated with 0 errors. Certainty: grounded for the build and every check (run by script); inferred for the placement of new topics under the six-child limit and for the three composed rules (judgment on claims that are individually grounded).

Pinned:
- Claims placed: 90 of 90 in `build/distill/claims_ledger.md`, 0 dropped (`check_ledger.py`: `claims in: 698; placed: 698; missing 0; duplicated 0; unknown 0`). Rows 601 to 691 (90 new rows; 6 existing rows rewritten or extended); philosophy 7 claims (rows on 6 existing nodes plus one merge), defaults 83.
- Nodes added: 17, all in `pig-js-defaults`, none in `js-philosophy`: `PIG-JS.DEFENSE.SECRETS.2.1`, `.2.2`; `PIG-JS.DEFENSE.INJECTION.1.3`, `.1.4`, `.4.5`, `.4.6`, `.5.4`; `PIG-JS.DEFENSE.HOST.3.1`, `.3.2`; `PIG-JS.DEFENSE.ORIGIN.2.1`, `.2.2`, `.6`, `.6.1`, `.6.2`, `.6.3`; `PIG-JS.DEPENDENCIES.INSTALL.5`, `PIG-JS.DEPENDENCIES.SCREEN.3` (the last is `undecided`).
- Nodes resolved from undecided: 3 (`PIG-JS.DEFENSE.DOM.2.3`, `PIG-JS.DEFENSE.INJECTION.5.3`, `PIG-JS.DEFENSE.INJECTION.6.4`). Kept undecided: `PIG-JS.DEFENSE.INJECTION.4.4`. Undecided in defaults: 12 before, 10 after.
- Decisions added: 7 entries (G1 to G7) in `build/distill/decisions_for_review.md` under `## Slot 14_secgap2`, including the two contested topics decided by the max rule (X-Frame-Options beside frame-ancestors; Sec-Fetch-Site alone for CSRF); ledger roles after: decision 421 (was 356), acceptable-when 37 (was 35), rejected 60 (was 55), fact 162 (was 145), deferred 11 (was 10).
- Validate, js-philosophy: `nodes: 108, links: 48, inter_links: 23, issues: 0, errors: 0, warnings: 0`. Validate, pig-js-defaults: `nodes: 287, links: 162, inter_links: 111, issues: 0, errors: 0, warnings: 0` (both with `-m intent_graphs/intent_resources.yaml`).
- `check_ledger.py`: `claims in: 698; placed: 698; missing 0; duplicated 0; unknown 0` and `ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 570}; by role: {'rejected': 60, 'fact': 162, 'decision': 421, 'acceptable-when': 37, 'deferred': 11}; skeleton nodes: 395`. `check_complete.py`: `FAILS: 0` (constraints 75 + 383, was 71 + 320; ledger rows 121 + 570).
- Not covered (kept): Node XML parser defaults for external entities; a typosquatting screening procedure; template-engine rules beyond Handlebars and EJS and a JavaScript upload signature check; URL parser differential examples; the Node path-containment recipe; whether `v8.deserialize` is safe for untrusted bytes; Node's own statement on `fetch` redirect modes and the bundled undici version. Removed from "Not covered": the seven security classes of the earlier README list (now rules).
- Touched outside the three integrated files, by necessity: the claim-id pattern in `build/assemble/build_batches.py`, `build/assemble/apply_flags.py` and `build/distill/check_ledger.py` (letters only before `-C`, so `SECGAP2-C01` was invisible); recorded in decision G6.

## L2 claims

Placement (grounded, by `check_ledger.py` and `check_complete.py`)
- Grounded: 90 of 90 claims placed exactly once, 0 dropped; 5 philosophy rows on existing nodes (C03 `DEFENSE.SECRETS`, C18 `DEFENSE.INJECTION.5`, C23 `DEFENSE.HOST.3`, C31 `DEFENSE.INJECTION.1`, C59 `DEFENSE.ORIGIN`), 1 on `DEPENDENCIES.THREATS.2` (C49), 1 merge into an existing philosophy row (C81 with RUNSEC-C28); defaults rows for the other 83 claims, with merges C77 and C79 into the rejected-belief row of `INJECTION.4.1` and C82 into the row of `INJECTION.4.4`, C90 into the decision row of `INJECTION.6.4`.
- Grounded: 4 claim-less `rejected` rows (folklore beliefs of C02, C12, C62, C65; C17 is a `rejected` row with its claim) and one claim-less `acceptable-when` row (Sec-Fetch-Site alone, MDN's position, condition stated); the build's judgment, flagged by `apply_flags.py`.
- Grounded: no new philosophy node; philosophy intents of `DEFENSE.SECRETS`, `DEFENSE.INJECTION.5`, `DEFENSE.HOST.3` gained one clause each; philosophy rows name no JavaScript tool.

Nodes (grounded for structure, inferred for the cut)
- Inferred: no new L2 under `PIG-JS.DEFENSE` (already six, the limit of I4 and A1); topics sit under the nearest parent with room. Weakest fits: tokens under `SECRETS.2`, CSRF as the sixth child `ORIGIN.6`. A seventh L2 would be cleaner by topic and wins if the maintainer accepts seven.
- Grounded: tokens `SECRETS.2.1` (policy) and `.2.2` (jsonwebtoken and jose settings); template injection `INJECTION.1.3` and `.1.4` (Handlebars and EJS); uploads `INJECTION.4.5` (content checks) and `.4.6` (storage, names, limits); XML `INJECTION.5.4`; headers `HOST.3.1` and `.3.2` (HTTP/2 and HTTP/3); clickjacking `ORIGIN.2.1` and `.2.2`; CSRF `ORIGIN.6` with `.6.1` (primary defence), `.6.2` (methods and APIs), `.6.3` (SameSite and csurf); `DEPENDENCIES.INSTALL.5` (repository inventory) and `SCREEN.3` (typosquatting, undecided).
- Grounded: defaults nodes 270 to 287 (DEFENSE 58 to 73, DEPENDENCIES 28 to 30); defaults links 146 to 162 intentlinks (12 within, 4 across), inter links 90 to 111; planned boundary links 10 to 13 (frame-ancestors header deployment, SameSite and session design, token revocation).
- Grounded: epistemic counts, defaults before then after (287 nodes): known alone 73 then 79; known with unvalidated or conflict 163 then 176; known with another issue 18 then 18; risky 4 then 4; undecided 12 then 10. Philosophy unchanged at 45, 53, 7, 2, 1.

Resolved from undecided (inferred: composed rules)
- Inferred: `DOM.2.3` decided, `known | unvalidated: inferred from DOMSEC-C57, SECGAP2-C70, C71, C73 and C74`: parse with the WHATWG URL API, compare scheme, host and port with an allowlist, reject userinfo, refuse `javascript:` and `data:` (C73 closes the old gap); parser differential examples stay open (C75).
- Inferred: `INJECTION.5.3` decided on the general deserialization rules only (integrity check first, new object from validated fields); no source says whether `v8.deserialize` is safe (C85), so no ban and no safe label.
- Inferred: `INJECTION.6.4` decided: `redirect: 'error'` or `'manual'` with revalidation, undici kept current, header stripping not relied on (C86 to C90); the semantics of `manual` in Node are carried over from the Fetch Standard by inference.
- Open: `INJECTION.4.4` stays undecided: no source for the symlink-resolving Node call or for the separator-aware comparison; never-a-raw-prefix (C76), resolve lets an absolute input replace the base (C78), isAbsolute and normalize (C77, C79) are placed on `INJECTION.4.1`. The task named SRVSEC-C44 to C46 among the containment grounds; they are the deserialization claims and ground `5.3`.

Contested topics (inferred, max rule)
- Inferred: X-Frame-Options beside frame-ancestors (C68): frame-ancestors on every response plus an `X-Frame-Options` fallback only where it states the same policy; `known | conflict: frame-ancestors alone, ASVS 3.4.6 and CSP3 with RFC 7034`.
- Inferred: Sec-Fetch-Site alone for CSRF (C69): a token is the primary defence, Sec-Fetch-Site and Origin or Referer are layers; MDN's position kept as `acceptable-when`; `known | conflict: a Sec-Fetch-Site check alone is a primary defence, MDN`.

Open or left out
- Open: Node XML parser defaults (C22), screening procedure (C54), URL parser differentials (C75), containment recipe (C82), `v8.deserialize` safety (C85), other template engines (C39), upload signature check (C48).
- Open: no independent review pass was run on the new rules (the global rule sends review to a separate Opus agent); nothing committed, nothing pushed, `integrate.py` not run.

## L3 full

### What was changed, by file

- `build/distill/claims_ledger.md`: 90 new rows (DEFENSE-185 to DEFENSE-268, DEPENDENCIES-085 to DEPENDENCIES-090) and 6 existing rows changed: DEFENSE-015 (claim C81 added), DEFENSE-139 (fact to decision, statement made a rule), DEFENSE-161 (C77 and C79 added, statement extended), DEFENSE-169 (C82 added, text updated, still a fact on the undecided node), DEFENSE-173 (fact to decision), DEFENSE-182 (C90 added, fact to decision). Header count: 691 rows, 698 claim ids.
- `build/distill/skeleton.md`: 17 node rows, 5 node rows with new text (`DOM.2.3` name unchanged, intent and state; `INJECTION.4.4` state; `INJECTION.5.3` intent and state; `INJECTION.6.4` intent and state; `INJECTION.4.1` intent), parent intents extended (`SECRETS.2`, `HOST.3`, `ORIGIN`, `ORIGIN.2`, `INJECTION.4`, philosophy `DEFENSE.SECRETS`, `DEFENSE.INJECTION.5`, `DEFENSE.HOST.3`), the ledger-rows column regenerated (26 nodes changed, all expected), 16 intentlinks and 21 inter links added, 3 planned boundary links, 18 new judge records (one per new or newly decided decision node) and an addendum to the `INJECTION.4.1` record, one conventions line.
- `build/distill/decisions_for_review.md`: section `Slot 14_secgap2` (G1 to G7), the undecided table (three rows removed, `INJECTION.4.4` revised, `SCREEN.3` added).
- `intent_graphs/`: both graphs rebuilt, README counts, certainty line, "Not covered", planned links (13), build note.
- `build/patch/14_secgap2/apply_patch.py` (one-time, stops on a second run) and this file.
- `build/assemble/build_batches.py`, `build/assemble/apply_flags.py`, `build/distill/check_ledger.py`: claim-id pattern `[A-Z]+\d*-C\d+`; `build_batches.py::claim_slots` also reads slot 14's claim table, because the frozen `claims_index.md` has no slot 14 rows. `claims_index.py`, `routing.md` and the branch folders were not touched.

### Rebuild and gates (verbatim)

Order: `apply_patch.py`, `apply_flags.py`, `build_batches.py`, `build_graphs.sh`, `check_complete.py`, `check_ledger.py`, `ig-tool validate -m`. `apply_flags.py` printed `{'noquote': 4, 'single': 5, 'weak': 4, 'nosource': 1} nodes changed: 11`. `build_batches.py`: `problems: []`, `decision_nodes_without_record: []`, `judge_records: 211`, `planned: 13`.

```
check_ledger.py
claims in: 698; placed: 698; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 570}; by role: {'rejected': 60, 'fact': 162, 'decision': 421, 'acceptable-when': 37, 'deferred': 11}; skeleton nodes: 395

check_complete.py
js-philosophy: nodes 108, intra 48, inter 23, ledger_rows 121, claims_in_pointers 118, impl_pointers 118, constraints 75
pig-js-defaults: nodes 287, intra 162, inter 111, ledger_rows 570, claims_in_pointers 580, impl_pointers 580, constraints 383
FAILS: 0

ig-tool validate -g intent_graphs/js_philosophy.ig.yaml -m intent_graphs/intent_resources.yaml
nodes: 108  links: 48  inter_links: 23  issues: 0  errors: 0  warnings: 0

ig-tool validate -g intent_graphs/js_defaults.ig.yaml -m intent_graphs/intent_resources.yaml
nodes: 287  links: 162  inter_links: 111  issues: 0  errors: 0  warnings: 0
```

(`check_complete.py` prints a JSON report; the lines above restate its figures. Its last line is `FAILS: 0`.)

### The new nodes, one line each (state as built, flags added by script not repeated)

- `SECRETS.2.1` Token and JWT verification: `known`; MUST rules from RFC 8725 and ASVS: caller-fixed algorithm allowlist, no alg none, trusted pre-configured keys, issuer, audience, validity, type, no mixed symmetric and asymmetric algorithms, no password as MAC key; rejected beliefs (valid-looking header, RFC 7519 section 8 as policy); revocation deferred (C16).
- `SECRETS.2.2` Token library settings: jsonwebtoken 9.0.0 or later, explicit `algorithms` for verify and for jose, decode is not verification; C11 and C14 inferred.
- `INJECTION.1.3` Template injection: never a template from untrusted input; user-supplied expression content sanitized; Kettle's trivial-engine-and-sandbox position as `acceptable-when` (one T3 source, flagged).
- `INJECTION.1.4` Handlebars and EJS: the engine statements and version floors; other engines open (C39).
- `INJECTION.4.5` Upload content checks: extension allowlist, no trusted Content-Type, re-encode or scan; signature recipe open (C48).
- `INJECTION.4.6` Upload storage, names and limits: server-generated names, outside the web root, explicit limits (busboy and multer default to Infinity), no global multer, decompression bounds, encoded served names.
- `INJECTION.5.4` XML and external entities: configuration failure on missing hardening, XSD over DTD, fast-xml-parser floor; Node parser defaults open (C22). The DTD-off rule is on philosophy `DEFENSE.INJECTION.5`.
- `HOST.3.1` Header field values and `HOST.3.2` Connection-specific fields: CR, LF, NUL rule on philosophy `DEFENSE.HOST.3`; setHeader throw plus validation functions, writeEarlyHints misuse, undici host advisory, accept-known-good; HTTP/2 and HTTP/3 rule (ASVS Level 3).
- `ORIGIN.2.1` Framing of the own page and `ORIGIN.2.2` Frame-busting and double clicks: see the contested decision; no frame-busting reliance; transaction authorization for double-click actions.
- `ORIGIN.6` Cross-site request forgery with `.6.1` Primary defence, `.6.2` Methods and API endpoints, `.6.3` SameSite and CSRF libraries: see the contested decision; no state change by safe methods; preflight reliance only when no preflight-free request can reach the function; SameSite as depth; csurf not for new code. XSS defeating CSRF defences is on philosophy `DEFENSE.ORIGIN`.
- `DEPENDENCIES.INSTALL.5` Expected repository and inventory: ASVS 15.1.2 and 15.2.4, single-source. `DEPENDENCIES.SCREEN.3` Typosquatting screening: `undecided | missing: no admitted T1 source states a screening procedure ...`, facts C50, C52, C53, C54; the 61 percent figure (C49) is a fact on philosophy `DEPENDENCIES.THREATS.2`.

### Judgment calls and why

- Six-child limit (G1, inferred). The brief says two to six children per parent and `PIG-JS.DEFENSE` has six. Recorded as a decision with the rejected alternative.
- Composed rules (grounded steps, inferred composition). For `DOM.2.3`, `5.3` and `6.4` every step of the rule is a claim; the composition is marked as asked. For `4.4` the symlink-resolving Node call and the separator-aware test have no claim (C82), so the node stays undecided; this differs from `5.3` because `5.3` applies an already-grounded general rule to a named API, while `4.4` asks for specifics (an API and a comparison) that no source states.
- `v8.deserialize` rule is the conservative direction (integrity check first). It is a build judgment, flagged; if the maintainer prefers the node undecided, revert the DEFENSE-173 row to a fact.
- Language-neutral practice claims (stack `principle`, level `practice`: C28, C40, C42, C45, C46, C57) went to the defaults graph by the extraction level (rule A2), not to the philosophy graph; the philosophy graph received principle-level claims only.
- Claims tagged `boundary: web_architecture_guidelines` (C61, C63, C64, C16): C63, C64 and C61 are code-level rules here with planned boundary links; C16 (revocation) is `deferred`.
- Quote flags: C65's quote is a paraphrase marker, so `ORIGIN.2.2` carries `unvalidated: quote not obtained`; every quote in the slot is tool-extracted (the slot's own L1 says so), which the flags do not repeat.

### Not done

- No independent review of the new rules; no `obsidian export` check; `claims_index.md`, `routing.md` and the branch folders were left as history. Slot 14's late candidates LC-01 to LC-03 (hapi fix commit, two undici fix commits) are not register sources; LC-01 would settle `INJECTION.4.4` and LC-02, LC-03 would ground the header-stripping facts in code.
- Nothing committed, nothing pushed.
