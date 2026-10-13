# Re-judge of 24 rules under "best, not most demanding"

Paths are relative to the guideline folder. Certainty words: grounded (a named source states it), inferred (follows from grounded facts, not stated), open (no admitted source settles it).

## L1 headline

Of the 24 rules, 13 stay as they were (KEEP) and 11 are relaxed to the form the existing evidence best supports (RELAX); the graphs were rebuilt and every gate passes. Certainty: grounded for the counts and the gates (I ran them); inferred for each verdict, since a verdict is a judgment on positions and no new source was read.

Pinned:
- Counts: KEEP 13, RELAX 11 (24 in all). No node, link or claim added or removed; claims placed 700, missing 0, duplicated 0.
- Relaxed, by uid: PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST, PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1, PIG-JS.SUBSET.OBJECTS.4, PIG-JS.CONTRACTS.STRICT.2, PIG-JS.CONTRACTS.STRICT.3, PIG-JS.CONTRACTS.ESCAPE.6, PIG-JS.STRUCTURE.LOADING.6, PIG-JS.STRUCTURE.PACKAGE.4, PIG-JS.DEFENSE.SECRETS.5, PIG-JS.DEFENSE.SECRETS.2.1, PIG-JS.DEFENSE.ORIGIN.6.1.
- Kept: PIG-JS.SUBSET.CONVERSION.2 (the `== null` decision, a close call), PIG-JS.SUBSET.OBJECTS.3, PIG-JS.SUBSET.EVOLUTION.5, PIG-JS.CONTRACTS.MODEL.5, PIG-JS.STRUCTURE.FORMAT.4, PIG-JS.STRUCTURE.SURFACE.1, SURFACE.2, SURFACE.3, SURFACE.5, PIG-JS.STRUCTURE.DIRECTION.2, PIG-JS.DEFENSE.INJECTION.5.3, PIG-JS.DEFENSE.INJECTION.6.1, PIG-JS.VERIFICATION.LINT.2.
- validate js-philosophy: nodes: 56, links: 20, inter_links: 11, issues: 0, errors: 0, warnings: 0, status: ok.
- validate pig-js-defaults: nodes: 287, links: 162, inter_links: 68, issues: 0, errors: 0, warnings: 0, status: ok.
- check_ledger.py: `claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0` and `ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343` (0 errors).
- check_complete.py: `FAILS: 0` (js-philosophy 56 nodes, 20 intra, 11 inter, 22 constraints; pig-js-defaults 287 nodes, 162 intra, 68 inter, 381 constraints).

## L2 claims

Rule after, then the reason. The stricter form of each RELAX is now a rejected position in the judge record, with the condition under which it would be best.

- PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST: RELAX. The list is the candidates that show gate A and one of B or C today; another framework joins on the same evidence. Reason: gate A has a grounded ancestor (run only supported versions, TYPES-C45, SUPPLY-C36); the absence of Vue, Svelte and Solid is a gap in the admitted sources, not a finding about them, so a closed list claimed too much (inferred).
- PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1: RELAX. Platform first; adopt a framework when a requirement is unmet; isolation-test what is adopted. Reason: SUPPLY-C27 says ask whether existing components suffice, then test the adopted dependency in isolation; the build had made the test a gate on adoption (grounded in the claim, inferred in the reading).
- PIG-JS.SUBSET.CONVERSION.2: KEEP. Forbid every `==`, the null check included. Reason: the mechanism is a tie (exact), the audit calls it stylistic, so the branch purpose decides: no exception for the reader to recall; the old reason "more demanding" is withdrawn. Close call, inferred; overrule to allow `== null` through lint if preferred.
- PIG-JS.SUBSET.OBJECTS.3: KEEP. `#` fields wherever privacy must hold. Reason: already conditional, consensus mechanism facts (MDN, TC39), the one dissent is a compile-target cost already recorded (grounded).
- PIG-JS.SUBSET.OBJECTS.4: RELAX. Accessors only as cheap, side-effect-free views of stored state; work is a method. Reason: the sole ground is Google's reason (a read that runs code surprises); it supports limiting accessors that do work, not banning a cheap read; the ban stays as acceptable-when (inferred boundary, one holder).
- PIG-JS.SUBSET.EVOLUTION.5: KEEP. Semicolons and braces everywhere. Reason: equal in predictability to the no-semicolon style only when formatter and hazard lint both run; the semicolon is free under the mandated formatter and tool-independent; braces need a lint rule (VERIFICATION-035); one holder, no hazard extracted (inferred, flagged).
- PIG-JS.CONTRACTS.STRICT.2: RELAX. SHOULD enable for new code; off where friction exceeds defects found. Reason: sources say consider and typescript-eslint documents the friction; a MUST over a documented cost exceeds them (grounded).
- PIG-JS.CONTRACTS.STRICT.3: RELAX. SHOULD enable for new code; off where dependency typings assign undefined. Reason: source says consider, mechanism only, cost not stated in any admitted source (grounded for the wording, inferred for the condition).
- PIG-JS.CONTRACTS.ESCAPE.6: RELAX. Ban ts-ignore and ts-nocheck; ts-expect-error only with a description; the recommended lint setting, no override. Reason: one T2 holder bans all three and nothing ranks them; the three differ in what they hide, and a self-reporting suppression also serves type-level tests (inferred; TypeScript's behaviour and the recommended setting are in no extracted claim, open).
- PIG-JS.CONTRACTS.MODEL.5: KEEP. Interface for object types, alias for what an interface cannot express. Reason: not a strict-versus-lenient choice; the only ranking is Google's, no dissent admitted, no argument for either form in the evidence; weak, flagged (inferred).
- PIG-JS.STRUCTURE.FORMAT.4: KEEP. Modules only, no namespaces. Reason: a second organising mechanism beside the language's modules costs locality; the declaration-file exception is already stated (inferred, one holder).
- PIG-JS.STRUCTURE.LOADING.6: RELAX. SHOULD NOT use large internal barrels; small ones where no cost is measured; aggregate at the public entry point. Reason: the one measurement (T3, one machine) shows cost growing with module count, so it supports "not large barrels", not "no internal barrel" (grounded for the scaling, inferred for the scope).
- PIG-JS.STRUCTURE.SURFACE.1: KEEP. Named exports only. Reason: the cause is a language fact (importer picks the name), two guides give it, the exceptions are conditional, the dissent carries no reason (grounded mechanism, holder positions).
- PIG-JS.STRUCTURE.SURFACE.2: KEEP. Export only what is used outside. Reason: each export is a name others depend on; Parnas's principle (T2, not a JavaScript rule) points the same way beyond the one holder (inferred).
- PIG-JS.STRUCTURE.SURFACE.3: KEEP. No mutable exports, no write to an import. Reason: first half a T1 mechanism, second the agreeing positions of three guides; the observable-value use is served by a function at no loss for locality (grounded, inferred).
- PIG-JS.STRUCTURE.SURFACE.5: KEEP. Module as namespace, no static-only classes. Reason: a module already namespaces (MDN, T1), both Google guides agree, W3C TAG's opposite targets platform APIs without modules (grounded, transfer inferred).
- PIG-JS.STRUCTURE.DIRECTION.2: KEEP. Enable the cycle lint rule knowingly, bound with maxDepth. Reason: the duty to automate follows from the no-cycle rule and the guideline's own principle that machines check; the T3 source supplies the tool and its cost, and the rule already says "knowingly" (inferred, single T3).
- PIG-JS.STRUCTURE.PACKAGE.4: RELAX. SHOULD use relative paths in a project; an imports-field alias where a path climbs several levels. Reason: an unconditional rule contradicted PACKAGE.3 (the imports field as the alias form, T1, consensus); the stated reason covers moving the project, not moving a file inside it (grounded PACKAGE.3, inferred the rest).
- PIG-JS.DEFENSE.SECRETS.5: RELAX. SHOULD detect secrets before commit; SHOULD rotate regularly. Reason: OWASP says consider enabling detection; rotation has no quote and lies outside the register's listed scope of that source (grounded).
- PIG-JS.DEFENSE.SECRETS.2.1: RELAX (one row of nine). Require exp where tokens grant API access, not on every token. Reason: the claim SECGAP2-C07 scopes it so and ASVS 9.2.1 checks validity only if present; the other eight decision rows mirror quoted RFC 8725 or ASVS text or a named attack (grounded).
- PIG-JS.DEFENSE.ORIGIN.6.1: RELAX. At least one primary defence, a token or a Sec-Fetch-Site check with an Origin or Referer fallback; token preferred and layered. Reason: OWASP and MDN list the check among primary defences and require no token beside it; token-first was the build's own (grounded, the preference inferred).
- PIG-JS.DEFENSE.INJECTION.5.3: KEEP. No untrusted buffer to `v8.deserialize` without a verified integrity check; copy from validated fields. Reason: applies the class-level mitigations, claims nothing about the function (open, C85); V8 says it reads what ValueSerializer wrote, the alternative is cheap, and no safety statement is not a safety statement (inferred).
- PIG-JS.DEFENSE.INJECTION.6.1: KEEP. Allowlist, WHATWG URL class, deny-list as the weaker fallback. Reason: the rules mirror Node's own text and a consensus OWASP and ASVS claim; not stricter than the sources (grounded).
- PIG-JS.VERIFICATION.LINT.2: KEEP. The CI job that runs the lint gate always runs. Reason: the platform fact is a T1 quote (skipped counts as passing) and the practice is the claim's own; the flag "no claim of its own" was wrong and is corrected (grounded fact, inferred practice).

## L3 full

### Method

1. Read the corrected rule (`build/distill/target_hierarchy.md`, "Selection rule") and the editing rules (`build/patch/brief_patch.md`); `integrate.py` was not run.
2. For each of the 24 nodes (the `== null` decision, `PIG-JS.SUBSET.CONVERSION.2`, is among them): read the node in the graph, its rows in `build/distill/skeleton.md` and `build/distill/claims_ledger.md`, its entry in `build/distill/decisions_for_review.md`, the cited claims in `build/research/<slot>/result.md` and the register rows in `build/audit/source_register.md` for the restrictions.
3. Weighed the positions on existing evidence only; tested each strict form against three questions: does the strongest argument in the evidence establish it, does it serve the branch purpose better than the weaker form, and is it stricter than the sources only because it was stricter. KEEP where the strict form is the best, RELAX where a weaker form is.
4. Edited the three integrated files (never `integrate.py`), then ran `apply_flags.py`, `build_batches.py`, `build_graphs.sh`, `check_complete.py`, `check_ledger.py`, `ig-tool validate` on both graphs, and `intent_graphs/export_to_obsidian.sh`.

Findings that shaped the verdicts:
- Rows that mirror a quoted source stay (INJECTION.6.1, LINT.2, eight of the nine token rows); rows that exceed their own claim are the ones relaxed (the exp row against SECGAP2-C07; the barrel MUST NOT against a measurement that scales with count).
- "Source says consider" became SHOULD, never MUST (STRICT.2, STRICT.3, SECRETS.5); the MUST is best only where a stated condition holds, recorded as the rejected form.
- Where two decided nodes disagreed, the relaxation removes the contradiction (PACKAGE.4 against PACKAGE.3; ESCAPE.6 against the recommended lint set).
- Kept rules that rest on one holder are kept for an argument beyond the holder: a language fact (SURFACE.1), a principle (SURFACE.2), a mechanism (SURFACE.3, SURFACE.5, FORMAT.4), or because the relaxed form is already a conditional exception in the same node (OBJECTS.3, EVOLUTION.5).

### Per rule (rule before, rule after, grounds, condition for the stricter form)

RELAX

1. `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`. Before: admit a framework only if it states security-fix versions (gate A) and has a documented escape model (B) or a governance body (C); the list was the set a team may choose among. After: same gates, but the list is a snapshot of what the admitted sources show; another framework joins on the same evidence; absence is not a rejection. Grounds: gate A follows from the supported-versions rule (TYPES-C45, SUPPLY-C36, SUPPLY-C28; inferred); B and C remain the build's judgment (flagged, node stays `risky`). Stricter form (a fixed approved list) is best where an organisation wants a list for audit; that is a policy, not a trust finding (inferred).
2. `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1`. Before: platform first; adopt a framework only when a requirement is unmet and an isolation test confirms it. After: platform first; adopt one when a requirement is unmet; test the adopted framework in isolation for unexpected indirect dependencies (SUPPLY-C27). Grounds: SUPPLY-C27 (single-source) asks whether existing components suffice and then isolates what is adopted. Flag now names SUPPLY-C27 as the inferred ground instead of "no claim".
3. `PIG-JS.SUBSET.OBJECTS.4`. Before: no getter or setter properties. After: accessors only as cheap, side-effect-free views of stored state on a data-like object; behaviour that does work is a method; the blanket ban is an acceptable-when row (row SUBSET-069, edited). Grounds: the only source is Google JS (one T2 holder, position) and its reason. Inferred boundary. The row needed one edit in `build/assemble/build_batches.py` (its `ACCEPT` entry), a tooling change, not graph content.
4. `PIG-JS.CONTRACTS.STRICT.2`. Before: MUST enable `noUncheckedIndexedAccess`. After: SHOULD for new code; off where friction exceeds the defects found. Grounds: TYPES-C13 (TypeScript documentation, typescript-eslint: consider, friction often unwieldy). MUST would be best where a team measured that unchecked index reads cause its defects.
5. `PIG-JS.CONTRACTS.STRICT.3`. Before: MUST enable `exactOptionalPropertyTypes`. After: SHOULD for new code; off where dependency typings assign undefined. Grounds: TYPES-C14 (single source, consider, mechanism only). MUST would be best where the typings come from controlled code and absent-versus-undefined causes defects (inferred).
6. `PIG-JS.CONTRACTS.ESCAPE.6`. Before: ban all three directives; lint override of the recommended set. After: ban `ts-ignore` and `ts-nocheck`; `ts-expect-error` only with a description; `ban-ts-comment` at its recommended setting; node renamed "No silent suppression directives"; row VERIFICATION-021 (`PIG-JS.VERIFICATION.LINT.1.2`) no longer names an override. Grounds: Google TS (one T2 holder) is the only ban; the reasoning on what each directive hides is inferred and open for verification (see Open). Stricter form is best where no type-level tests exist and zero directives is wanted.
7. `PIG-JS.STRUCTURE.LOADING.6`. Before: MUST NOT use barrels to aggregate a package's internals. After: SHOULD NOT once they re-export many modules; small barrels where the project's own measurement shows no cost; the public entry point aggregates. Grounds: SRC-315 (T3, synthetic, one machine: 0.15 s for 500, 48.44 s for 50,000) and MDN on eager loading (T1). Stricter form is best where the package is large enough for the measured cost to apply.
8. `PIG-JS.STRUCTURE.PACKAGE.4`. Before: MUST use relative paths within a project. After: SHOULD, with an imports-field alias where a relative path climbs several directory levels. Grounds: Google TS position and its reason (project can move); PACKAGE.3 (T1, consensus) already decides the imports field as the alias form. Aliases everywhere are best where most files sit deep and cross-directory imports are the norm (inferred).
9. `PIG-JS.DEFENSE.SECRETS.5`. Before: MUST detect before commit and rotate. After: SHOULD detect before commit, SHOULD rotate regularly. Grounds: RUNSEC-C48 quote says "Consider enabling secrets detection"; the register lists the scope of SRC-138 as no hardcoded secrets, environment variables as the weaker option, pre-commit detection (rotation absent). MUST would be best for a repository that can become public or holds production credentials (inferred).
10. `PIG-JS.DEFENSE.SECRETS.2.1`. Before: every check a MUST, exp required on every token. After: unchanged except the validity row (DEFENSE-196): require exp where tokens grant API access. Grounds: SECGAP2-C07 wording; ASVS 9.2.1 checks validity only if present. The key-source, token-type and memorizable-password rows rest on one source each (SECGAP2-C04, C08, C15) but state RFC 8725 or ASVS text, so they stay. Requiring exp always would be best for tokens from an issuer the deployment does not control.
11. `PIG-JS.DEFENSE.ORIGIN.6.1`. Before: token as the primary defence, Sec-Fetch-Site check and Origin or Referer fallback layered behind it, "never with a Sec-Fetch-Site check alone". After: at least one primary defence (token, or Sec-Fetch-Site check with the Origin or Referer fallback); token preferred and the other layered behind it where browsers may not send the header; token hygiene rules apply wherever a token is used; acceptable-when row now concerns a check without the fallback. Grounds: SECGAP2-C55, C56, C69 (consensus, OWASP and MDN). The token preference is the build's own and is flagged.

KEEP

12. `PIG-JS.SUBSET.CONVERSION.2`. Kept: forbid every `==`. The former reason ("more demanding of two grounded options") is withdrawn. New reason: both forms are exact (ECMA-262 7.2.13); the dissent audit calls the dispute stylistic and says "choose per code base"; with the mechanism tied, the branch purpose (an expression's meaning follows from its text, SUBSET.VISIBLE) decides for no exception; ESLint's default and Airbnb agree; the cost is two comparisons. Flag now says: a stylistic tie, reader-cost argument, inferred. Maintainer may overrule.
13. `PIG-JS.SUBSET.OBJECTS.3`. Kept; already best, not strictest (applies where privacy must hold; consensus facts).
14. `PIG-JS.SUBSET.EVOLUTION.5`. Kept; equal predictability only with tooling, free under the mandated formatter; braces need lint (VERIFICATION-035); no hazard extracted, so the flag stays.
15. `PIG-JS.CONTRACTS.MODEL.5`. Kept; sole ranking, no dissent, rule already routes non-object forms to aliases; weak, flagged.
16. `PIG-JS.STRUCTURE.FORMAT.4`. Kept; one mechanism for sharing.
17. `PIG-JS.STRUCTURE.SURFACE.1`. Kept; language-fact reason, conditional exceptions recorded.
18. `PIG-JS.STRUCTURE.SURFACE.2`. Kept; information hiding (SRC-257, T2, principle only).
19. `PIG-JS.STRUCTURE.SURFACE.3`. Kept; T1 mechanism and three agreeing guides.
20. `PIG-JS.STRUCTURE.SURFACE.5`. Kept; module as namespace (MDN, T1), TAG scoped to platform APIs.
21. `PIG-JS.STRUCTURE.DIRECTION.2`. Kept; the duty to automate follows from DIRECTION.1 and VERIFICATION; the T3 source gives tool and cost; stays `risky`.
22. `PIG-JS.DEFENSE.INJECTION.5.3`. Kept; asymmetric cost under an open fact (C85); would relax if Node or V8 states the function is safe for hostile bytes.
23. `PIG-JS.DEFENSE.INJECTION.6.1`. Kept; flag corrected: the allowlist claim SRVSEC-C28 is held on the philosophy node DEFENSE.
24. `PIG-JS.VERIFICATION.LINT.2`. Kept; flag corrected: QUALITY-C43 is held on the philosophy node VERIFICATION.ENFORCEMENT.

### Files changed

- `build/distill/claims_ledger.md`: rows DEPENDENCIES-078, DEPENDENCIES-079, SUBSET-047, SUBSET-069, CONTRACTS-025, CONTRACTS-026, CONTRACTS-034, STRUCTURE-031, STRUCTURE-048, DEFENSE-115, DEFENSE-196, DEFENSE-249, DEFENSE-250, DEFENSE-252, DEFENSE-253, VERIFICATION-021. No row added or removed; claim ids unchanged.
- `build/distill/skeleton.md`: node rows (intent, epistemic state, one name) and judge records of the 24 nodes; a line in the conventions list.
- `build/distill/decisions_for_review.md`: new section "Re-judged under best (24 rules)" and "Superseded" pointers in the earlier entries it overrides.
- `build/assemble/build_batches.py`: the `ACCEPT` entry of SUBSET-069 (tooling, noted in the section above).
- `intent_graphs/`: both graphs rebuilt, vault re-exported; `intent_graphs/README.md` unchanged (its epistemic counts, 76 / 179 / 18 / 4 / 10, were re-run and still hold).

### Open

- ESCAPE.6: the recommended setting of `ban-ts-comment` and the self-reporting behaviour of `ts-expect-error` are in no extracted claim; read the typescript-eslint rule page and the TypeScript handbook before relying on the wording.
- CONVERSION.2 is a close call; the alternative (allow `== null` through lint) loses no grounding.
- Thresholds "many modules" (LOADING.6) and "several directory levels" (PACKAGE.4) are unstated by design: no admitted source gives a number.
- Other judge records still use "max rule" or "most demanding" wording (nodes outside the 24, for example the STRICT parent and several RUNTIME and DEPENDENCIES records). Not re-judged; the maintainer decides whether to apply the same pass.

### Gate outputs (verbatim)

```
python3 build/distill/check_ledger.py
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'deferred': 77, 'decision': 368, 'fact': 162, 'rejected': 57, 'acceptable-when': 35}; skeleton nodes: 343

python3 build/assemble/check_complete.py   (last line)
FAILS: 0

ig-tool validate js_philosophy: nodes: 56 links: 20 inter_links: 11 issues: 0 errors: 0 warnings: 0 status: ok
ig-tool validate js_defaults:   nodes: 287 links: 162 inter_links: 68 issues: 0 errors: 0 warnings: 0 status: ok
```
