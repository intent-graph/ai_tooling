# Fix plan for the stage-7 review findings

Decisions by the orchestrator on each finding of `result.md` (same folder). Finding ids F01 to
F21 refer to its `## L2 claims`; their evidence is in its `## L3 full`.

## Principle for every fix

The maintainer's standing rule: max, not average; the build may choose. Two consequences:
- A source that suggests a practice ("consider X") grounds the practice; choosing its strict
  form (MUST) is allowed. The weakness is made visible in `epistemic_state`, never hidden.
- A restricted holder's position may choose between positions when no other position exists;
  the node then says so in `epistemic_state`.

## Decisions per finding

- **F01** fix: MUST NOT build a shell command string from untrusted input, sanitized or not;
  argument arrays only. Ground it on OWASP OS Command Injection (SRC-136) only if a claim cites
  it; otherwise keep Node's claim and mark `unvalidated: stronger form inferred`.
- **F02** keep MUST on STRICT.2, STRICT.3, SECRETS.5; add `unvalidated: source says consider`.
- **F03** keep the framework short list; restate its gates as the node's constraints (not only in
  design notes) and set `epistemic_state` to `risky | unvalidated: gates are the build's
  judgment, no admitted source states them`.
- **F04** add `unvalidated: Node crypto text read in v6 docs only`. Try once to read the current
  `crypto.timingSafeEqual` entry through the Playwright browser tools if they are available to
  you (`mcp__playwright__browser_navigate` then `browser_snapshot`); if it confirms, drop the
  flag and record the URL read.
- **F05** apply one rule to every node of both graphs: a decision resting on an inferred or open
  claim, or on single-source claims only, carries `unvalidated: <why>` in `epistemic_state`
  (keep any `conflict:`). Use the claim tables' `certainty` and `agreement` columns, by script.
- **F06** keep the MUSTs; add `unvalidated: holder position only (<holder>)`.
- **F07** not fixed here: security classes with no admitted source go to the maintainer (a
  possible second gap round). Add them to `intent_graphs/README.md` under a "Not covered"
  heading, one line each.
- **F08** type layer: `epistemic_state` `risky | conflict: JSDoc-checked JavaScript, none |
  unvalidated: decided by the build on T1 mechanism facts and one T2 holder`; replace the
  circular constraint with the decision and a condition table (when TypeScript, when
  JSDoc-checked JavaScript would win).
- **F09, F21** engineer-facing fields hold rules only: move "Integration note", "Merged" and
  similar bookkeeping out of `constraints` and `design_notes` into the build (a log file in
  `build/assemble/`); drop the "MUST hold:" prefix; facts that are not rules move from
  `constraints` to `design_notes`.
- **F10** AEAD: MUST use authenticated encryption modes, `unvalidated: single source`.
- **F11** MUST NOT leave a catch block empty without a comment stating why.
- **F12** coverage: SHOULD NOT gate on a coverage number; show the OpenSSF T1 position (cover
  most branches) in the design notes as the rejected position and its condition.
- **F13** soften THREATS.1 to what the incidents show; ground or demote the npm audit MUST.
- **F14** align ESCAPE.6 with LINT.1.2: name the typescript-eslint rule configuration that
  enforces ESCAPE.6, so lint and rule agree.
- **F15** add the missing constraints; word the YAML rule as "if js-yaml, version 4 or later".
- **F16** framework-specific and dated facts move from constraints to design notes as dated
  evidence; constraints stay framework-neutral where the plan requires it.
- **F17** claims with no quote or a paraphrase marker behind a decision: the decision node gets
  `unvalidated: quote not obtained`.
- **F18** correct the quotes in the claim tables of `build/research/` named in L3 (the wording,
  not the meaning), and the SRC-341 URL note in the register is left as is but recorded in your
  result.
- **F19** move JavaScript and tool names out of philosophy intents and constraints into the
  defaults graph (or a link to it).
- **F20** done by the orchestrator (caches removed, plan updated).

## How

Fix upstream, then rebuild: edit `build/distill/skeleton.md`, `build/distill/claims_ledger.md`,
`build/distill/decisions_for_review.md`, and the build scripts in `build/assemble/` where a fix
is a transformation; then rebuild with `python3 build/assemble/build_batches.py`,
`zsh build/assemble/build_graphs.sh`, `python3 build/assemble/check_complete.py`, and gate on
`python3 build/distill/check_ledger.py` and `ig-tool validate -g <graph> -m
intent_graphs/intent_resources.yaml` (0 errors each).
