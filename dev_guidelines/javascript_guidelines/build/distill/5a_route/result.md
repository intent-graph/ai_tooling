# Step 5a: route

## L1 headline

All 608 claims are routed exactly once to one of the eight branches in 145 groups, and the split script reports 0 errors; certainty: grounded for counts and checker output, inferred for the branch choices at the boundaries listed in L2 (judgement calls, not facts).

Pinned:
- Claims routed per branch: SUBSET 61, CONTRACTS 52, CONTROL 82, STRUCTURE 57, DEFENSE 195, DEPENDENCIES 84, VERIFICATION 43, RUNTIME 34 (sum 608).
- Number of groups: 145 (every group has 2 or more members and lies inside one branch).
- Split script final line per branch: `SUBSET: 61 claims`, `CONTRACTS: 52 claims`, `CONTROL: 82 claims`, `STRUCTURE: 57 claims`, `DEFENSE: 195 claims`, `DEPENDENCIES: 84 claims`, `VERIFICATION: 43 claims`, `RUNTIME: 34 claims`; ERROR count: 0 (exit code 0).

## L2 claims

- Grounded: the input has 608 claims (slots 01 to 10: 544; slot 13 SRVSEC: 64); `routing.md` has 608 rows; `claims_index.py split` was run on the final routing.md and printed no ERROR line.
- Grounded: 16 claims carry `boundary: web-architecture`: DOMSEC-C26, C28, C29, C35, C59, C60; TYPES-C29; RUNTIME-C39, C41; FW-C04, C07, C13, C14, C44, C45; SRVSEC-C38. Not tagged though 11_coverage lists them as split or staying here: DOMSEC-C15, FW-C48 (code half here, header half sibling), DOMSEC-C27 (stays).
- Inferred, heaviest branch: DEFENSE holds 195 claims (32 percent), because slots 05, 06 and 13 all land there plus the framework-security claims; the branch agent for DEFENSE will need the sub-partition SINKS/DOM, PROTOTYPE, EVAL, INJECTION (command, SQL, NoSQL), SSRF, PATHS, CRYPTO, DESERIALIZATION, SECRETS. Recommend 5b runs DEFENSE as two agents (browser DOM side: 05 and FW security; server side: 06 and 13) if one agent proves too large; this is a recommendation, not done here.
- Inferred, slot-to-branch splits applied as the brief says: slot 09 to CONTROL (streams C01-C12, C17, process lifecycle C31-C43) and RUNTIME (profiling, memory, GC, benchmarking: 34 claims) with 5 security ones to DEFENSE (C13, C15, C18, C51, C52); slot 04 to STRUCTURE (57 incl. modules and naming), CONTRACTS (C38, C47-C52), SUBSET (C21, C39-C41, C44-C46, C66), RUNTIME (C42, C43), DEPENDENCIES (C67), CONTROL (C53); slot 13 all to DEFENSE except SRVSEC-C62 (DEPENDENCIES); slot 10 frameworks: security-use rules to DEFENSE (16 claims), choice evidence to DEPENDENCIES (33).
- Inferred, judgement calls at the edge (each could go the other way): LANG-C58 to LANG-C64 and LANG-C15 to STRUCTURE (Node ESM and module facts, per O08); LANG-C57 and STRUCT-C21 stay in SUBSET (ES modules chosen over CommonJS); LANG-C53 to CONTRACTS; LANG-C45 and TYPES-C12 to CONTROL with ASYNC-C18; QUALITY-C19 (semicolons) to SUBSET; QUALITY-C18 to CONTRACTS with TYPES-C25; TYPES-C45 (Node LTS) to DEPENDENCIES although its tag says 09_runtime; SRVSEC-C60 and C61 (error text, log injection) to DEFENSE; QUALITY-C44 to DEPENDENCIES (with SUPPLY-C35 as score caveats); STRUCT-C43 to RUNTIME to sit with RUNTIME-C55 (tension X4).
- Grounded: overlap clusters of 11_coverage and where each landed: O01 unhandled-rejection (CONTROL), O02 uncaught-exception (CONTROL), O03 emitter-error-listener (CONTROL), O04 http-server-timeouts (CONTROL), O05 redos (DEFENSE), O06 eval-from-strings (DEFENSE), O07 throw-only-error (CONTROL), O08 four groups node-esm-extensions, node-esm-globals-json, require-esm, module-format-explicit and top-level-await (STRUCTURE), O09 release-cooldown (DEPENDENCIES), O10 lockfile-install (DEPENDENCIES), O11 trusted-types-enforce (DEFENSE), O12 framework-escape-hatches (DEFENSE), O13 deps-are-trusted-code (DEPENDENCIES), O14 json-parse-proto (DEFENSE; TYPES-C49 goes to SUBSET with LANG-C33 in json-bigint-precision), O17 abort-signal (CONTROL).
- Grounded, clusters that had to be split because a group may not span branches (the 5b agents of both branches must link them, the integrator merges): O15 own-property test (SUBSET group own-property-test: LANG-C55, STRUCT-C45; DEFENSE: RUNSEC-C07, no group), O16 freezing (SUBSET freeze-shallow: LANG-C38, C39; STRUCTURE exported-mutable-state: STRUCT-C01 to C03; DEFENSE freeze-hardening: DOMSEC-C52, RUNSEC-C09), O18 secrets (DEFENSE secrets-in-code: RUNSEC-C46 to C48; DEPENDENCIES publish-contents: SUPPLY-C38 with SRVSEC-C62), O19 prototype modification (SUBSET prototype-builtins: LANG-C14, STRUCT-C44; RUNTIME engine-optimisation-warnings holds STRUCT-C43; DEFENSE RUNSEC-C12 ungrouped), and LANG-C34 (DEFENSE group constant-time-code with SRVSEC-C07 to C09).
- Grounded, conflicts that 11_coverage marked as not contested are co-routed: LANG-C64 with STRUCT-C09 (STRUCTURE, group module-cycles); LANG-C12 with STRUCT-C41 (SUBSET, group private-members).
- Grounded: contested claims (17) landed as follows so each contested topic has one owner: LANG-C12 SUBSET, LANG-C19 SUBSET, LANG-C22 SUBSET, TYPES-C01 CONTRACTS, STRUCT-C09 STRUCTURE, STRUCT-C19 STRUCTURE, STRUCT-C24 STRUCTURE, STRUCT-C41 SUBSET, STRUCT-C63 STRUCTURE, DOMSEC-C17 DEFENSE, DOMSEC-C25 DEFENSE, DOMSEC-C47 DEFENSE, RUNSEC-C38 DEFENSE, SUPPLY-C06 DEPENDENCIES, QUALITY-C13 VERIFICATION, QUALITY-C36 VERIFICATION, FW-C22 DEPENDENCIES; plus SRVSEC-C18 (new, contested SQL identifiers) DEFENSE.
- Open: slot 13 claims that state a gap, not a practice (SRVSEC-C14, C37, C44, C55) were routed to DEFENSE with their topic; the DEFENSE agent must record them as undecided or notes, not decisions.
- Not done: no claim was dropped or duplicated; the 11_coverage tag spellings (`04_struct` and so on) were left untouched because the split script reads only columns 1 to 3.

## L3 full

### Method

1. Read the brief (Shared, Step 5a), `target_hierarchy.md`, the 608-row `claims_index.md` in full, `11_coverage/result.md` (all levels) and the `## L2 claims` of `12_dissent/result.md`; read `claims_index.py` to learn what `split` checks (each claim once, branch in the eight keywords, nothing routed but unknown, nothing unrouted).
2. Branch rule applied claim by claim: the branch is the purpose of the claim as the target hierarchy describes each branch (SUBSET predictability, CONTRACTS checkability, CONTROL explicit time and failure and resources, STRUCTURE locality of change, DEFENSE hostile input and sinks, DEPENDENCIES third-party trust and framework choice, VERIFICATION machine checks, RUNTIME measured performance and memory), with the slot as a prior only. The routing was generated by a script that holds the per-slot prior and a list of explicit overrides per claim (kept outside the repository), then validated: all 608 ids present, every group has at least two members, no group spans two branches, no claim is in two groups.
3. Groups: a label is shared by claims that state the same fact or answer the same question; 145 labels. The 19 overlap clusters of 11_coverage are among them, except where a group would span branches (see split list in L2). Labels are lowercase with hyphens.
4. Note column: `boundary: web-architecture` on 16 claims (list in L2); every other row has `-`.

### Counts

| branch | claims | groups |
|---|---|---|
| SUBSET | 61 | 17 |
| CONTRACTS | 52 | 12 |
| CONTROL | 82 | 20 |
| STRUCTURE | 57 | 16 |
| DEFENSE | 195 | 43 |
| DEPENDENCIES | 84 | 19 |
| VERIFICATION | 43 | 10 |
| RUNTIME | 34 | 8 |
| total | 608 | 145 |

### Branch composition by source slot (grounded, from the routing table)

- SUBSET (61): 01_lang 51 claims (strict mode, this, classes, equality and coercion, numbers, immutability, features to avoid, Temporal) plus STRUCT-C21, C39 to C41, C44 to C46, C66, QUALITY-C19, TYPES-C49.
- CONTRACTS (52): 02_types except C06, C07, C12, C31, C32, C44, C45, C49, C50; plus LANG-C53, STRUCT-C38 and C47 to C52, RUNSEC-C06 and C42, QUALITY-C18.
- CONTROL (82): 03_async except C33, C40; plus LANG-C45, TYPES-C12, STRUCT-C53, RUNTIME-C01 to C12, C17, C31 to C43.
- STRUCTURE (57): 04_struct modules, packages, naming, paradigm, state; LANG-C15, C58 to C64; TYPES-C06.
- DEFENSE (195): all 05_domsec, 06_runsec except C06, C21, C41, C42; 13_srvsec except C62; ASYNC-C33, C40; LANG-C34, C49; TYPES-C31, C32, C50; RUNTIME-C13, C15, C18, C51, C52; FW-C01 to C06, C08 to C12, C14, C18 to C20, C48.
- DEPENDENCIES (84): all 07_supply, FW choice evidence (release, governance, types, usage, advisories, reporting), TYPES-C07 and C45, STRUCT-C67, RUNSEC-C21 and C41, QUALITY-C42, C44, C46, SRVSEC-C62.
- VERIFICATION (43): 08_quality except C18, C19, C42, C44, C46; LANG-C56; TYPES-C44.
- RUNTIME (34): 09_runtime C14, C16, C19 to C30, C44 to C50, C53 to C63 (all in the slot not moved to CONTROL or DEFENSE), plus STRUCT-C42, C43.

### Groups per branch (labels)

SUBSET: this-binding, strict-mode, equality-operators, implicit-coercion, float-precision, safe-integers-bigint, json-bigint-precision, const-let-var, freeze-shallow, nullish-operators, feature-maturity, sort-order, legacy-syntax, private-members, prototype-builtins, own-property-test, esm-strict-scope.

CONTRACTS: node-type-stripping, ts-strict-family, ts-beyond-strict, any-vs-unknown, suppression-directives, type-unsoundness, jsdoc-checked-js, schema-libraries, options-object, ts-overload-guidance, validate-at-boundary, schema-additional-properties.

CONTROL: unhandled-rejection, uncaught-exception, emitter-error-listener, http-server-timeouts, abort-signal, floating-promises, promise-constructor, concurrent-promises, error-cause, timer-precision, deferral-scheduling, event-loop-blocking, worker-usage, async-context, stream-backpressure, stream-pipeline, web-streams, exit-handling, graceful-shutdown, throw-only-error.

STRUCTURE: module-cycles, node-esm-extensions, node-esm-globals-json, require-esm, module-format-explicit, top-level-await, exported-mutable-state, side-effect-free-imports, static-only-classes, public-surface-minimal, package-exports, tree-shaking-bundling, naming, dependency-direction, paradigm-defects, export-collisions.

DEFENSE: eval-from-strings, vm-sandbox, constant-time-code, csprng, timing-safe-compare, password-hashing, sql-parameterization, sql-identifiers, nosql-operator-injection, ssrf-allowlist, ssrf-resolved-ip, ssrf-redirects, deserialization-untrusted, document-dangerous-functionality, path-containment, toctou-file-check, request-smuggling, inspector-exposure, buffer-allocation, url-parsing-validation, redos, parser-resource-limits, json-parse-proto, proto-pollution-keys, null-prototype-dict, command-injection, secrets-in-code, permission-model, freeze-hardening, trusted-types-enforce, trusted-types-policy, framework-escape-hatches, csp-strict, vue-xss-rules, htmx-hardening, html-sanitizer, html-sinks, postmessage, web-storage, sri, third-party-script-isolation, iframe-sandbox, dom-clobbering.

DEPENDENCIES: lockfile-install, install-scripts, release-cooldown, deps-are-trusted-code, dependency-pinning, publishing-auth, provenance-and-signing, audit-triage, package-confusion, maintainer-takeover, publish-contents, scorecard-scores, framework-release-policy, framework-governance, framework-types, framework-usage-figures, framework-advisories, framework-vuln-reporting, htmx-versions.

VERIFICATION: eslint-config, lint-ci-gating, formatter-choice, typed-linting, static-analysis-requirement, mutation-testing, property-based-testing, flaky-tests, test-runner-facts, test-design.

RUNTIME: engine-optimisation-warnings, built-in-profilers, heap-snapshots, benchmark-method, weak-references, v8-gc-mechanism, heap-limit, event-loop-diagnosis.

(Sum 17 + 12 + 20 + 16 + 43 + 19 + 10 + 8 = 145.)

### Verbatim command output

```
SUBSET: 61 claims
CONTRACTS: 52 claims
CONTROL: 82 claims
STRUCTURE: 57 claims
DEFENSE: 195 claims
DEPENDENCIES: 84 claims
VERIFICATION: 43 claims
RUNTIME: 34 claims
```
No `ERROR` line; exit code 0. Files written by the script: `build/distill/branches/<BRANCH>/claims.md` for the eight branches.

### Things the next steps should know

- Open issues for 5b: CONTRACTS and VERIFICATION both touch TypeScript configuration (type layer decision lives in CONTRACTS; lint rule sets in VERIFICATION); DEPENDENCIES holds both package hygiene and the framework short list, the two largest sub-trees there.
- Folklore refuted by 12_dissent follows the claims it concerns (the claims' `folklore:` tags travel with the rows), so each branch agent owns its `rejected` rows; X1 to X5 tensions of 12_dissent land inside one branch except X1 (freeze: SUBSET and DEFENSE) and X4 (STRUCT-C43 and RUNTIME-C55 co-routed to RUNTIME to keep it in one place).
- Possible later cut: if DEFENSE is split into two agents, a natural line is the label set above (browser: html-sinks through dom-clobbering plus trusted-types, csp, framework labels; server: the rest).
