# Research result: 12 DISSENT (disagreements and folklore audit)

## L1 headline

Admitted authorities genuinely disagree on a handful of style and tooling choices (16 contested topics, mostly style, none about language mechanism), while the folklore audit finds most popular JavaScript beliefs it can test refuted or restricted by T1 sources; certainty: grounded for each position and each verdict, inferred for the resolutions and recommendations, open where a source gave no verbatim condition.

Pinned: 16 contested topics (from the 17 contested claims the checker reports): private-member marking; `== null`; implicit coercion shorthands; type layer; module cycles; top-level await; default versus named exports; paradigm and defects; Trusted Types default policy; setAttribute safety; target=_blank noopener; permission model strength; dependency pinning; formatter choice; coverage target; htmx documentation version. Folklore: 60 beliefs, confirmed 10, restricted 13, refuted 37.

## L2 claims

Pinned: 16 contested topics (from the 17 contested claims the checker reports): private-member marking; `== null`; implicit coercion shorthands; type layer; module cycles; top-level await; default versus named exports; paradigm and defects; Trusted Types default policy; setAttribute safety; target=_blank noopener; permission model strength; dependency pinning; formatter choice; coverage target; htmx documentation version. Folklore: 60 beliefs, confirmed 10, restricted 13, refuted 37.

**Disagreements (16 topics; real = holders conflict, scope = conditions reconcile them).** Mechanism is never contested in any topic; only what to prefer is.

- Topic 1, Private-member marking: real among guides; scope by build target. Holders SRC-091 (MDN, `#`), SRC-239 (Google JS, optional trailing underscore), SRC-312 (Airbnb, no underscores), SRC-244 (Google TS, no `#`, TypeScript `private`). Claims LANG-C12; STRUCT-C41; STRUCT-C40. Certainty: grounded.
- Topic 2, `== null` shorthand: real, style. Holders SRC-239 allows it; SRC-002 default forbids, options allow; SRC-312 forbids. Claims LANG-C19. Certainty: grounded.
- Topic 3, Implicit coercion shorthands: scope: readability rule against a harm measurement. Holders SRC-003, SRC-239, SRC-312 forbid; SRC-238 finds 98.85% harmless. Claims LANG-C22. Certainty: grounded.
- Topic 4, Type layer: not a clash of holders: only TypeScript has advocates. Holders SRC-239 and SRC-244 (TypeScript); SRC-047, SRC-044 (JSDoc facts); SRC-240 (none, measurement only). Claims TYPES-C01. Certainty: grounded.
- Topic 5, Module cycles: real, none measures cost. Holders SRC-029 and SRC-239 (avoid), SRC-313 (always dangerous), SRC-089 (supported mechanism). Claims STRUCT-C09; STRUCT-C08. Certainty: grounded.
- Topic 6, Top-level await: real inside the proposal record, no measurement. Holders SRC-092 (critics against champions). Claims STRUCT-C19. Certainty: grounded.
- Topic 7, Default versus named exports: real. Holders SRC-239 and SRC-244 (named only), SRC-312 (default for single export), SRC-029 (neutral). Claims STRUCT-C24. Certainty: grounded.
- Topic 8, Paradigm and defects: scope: cross-language studies, one dataset, not JavaScript. Holders SRC-251, SRC-258, SRC-314. Claims STRUCT-C63; STRUCT-C64. Certainty: grounded.
- Topic 9, Trusted Types default policy: scope: legacy and third-party code. Holders SRC-120, SRC-267 (transitional); SRC-269 (only a default policy works with third-party code). Claims DOMSEC-C17. Certainty: grounded.
- Topic 10, setAttribute safety: real; reconciliation inferred. Holders SRC-108 (safe construction method); SRC-120 (TrustedScript sink); SRC-316 lists it among sinks. Claims DOMSEC-C25; DOMSEC-C07. Certainty: grounded for positions; condition inferred, verbatim not obtained.
- Topic 11, target=_blank noopener: scope: browser age. Holders SRC-103 (implied unless rel=opener); SRC-110 (explicit). Claims DOMSEC-C47. Certainty: grounded; condition inferred.
- Topic 12, Permission model strength: scope: trusted code against hostile code; one internal inconsistency. Holders SRC-128 and SRC-140 (seat belt, no guarantee against malice); SRC-078 (helps contain compromised dependencies). Claims RUNSEC-C38; RUNSEC-C41. Certainty: grounded.
- Topic 13, Dependency pinning: real; condition: graph size, library or application. Holders SRC-078 (pin exactly); SRC-156 (lockfile); SRC-154 (ranges); SRC-287 (pinning can raise exposure). Claims SUPPLY-C06; SUPPLY-C05; STRUCT-C67. Certainty: grounded.
- Topic 14, Formatter choice: real, unrankable: holders are the tools' own documents. Holders SRC-298 (Prettier, dprint or @stylistic); SRC-162 (Biome, one tool); SRC-177 (Prettier, run apart from linters). Claims QUALITY-C13; QUALITY-C12; QUALITY-C15. Certainty: grounded; no ranking source exists.
- Topic 15, Coverage target: scope: study on Java against a suggested criterion. Holders SRC-297 (no target); SRC-174 (suggests covering most branches). Claims QUALITY-C36. Certainty: grounded; transfer to JavaScript inferred.
- Topic 16, htmx documentation version: scope only: docs lag the release line, not a disagreement. Holders SRC-213 (2.x docs), SRC-212 and SRC-214 (4.x current, 2.x supported). Claims FW-C22. Certainty: grounded.

**Cross-slot tensions not marked contested (5, not counted in the pin; all inferred).**

- X1, Freezing built-ins as a hardening step against never modifying built-ins: RUNSEC-C09 against LANG-C14 and STRUCT-C44; scope: hardening versus patching; freezing blocks later polyfills, inferred.
- X2, Sanitizer library against the native Sanitizer API: DOMSEC-C11 against DOMSEC-C08; scope: availability; both can coexist (DOMSEC-C23).
- X3, Null-prototype object: `Object.create(null)` against the literal `{ __proto__: null }`: RUNSEC-C05 (OWASP last resort, MDN lists both); scope: strength of defence, already one claim.
- X4, Weight of prototype and array performance warnings: STRUCT-C43 (MDN warns of deoptimisation) against RUNTIME-C55 and RUNTIME-C63 (V8: rarely measurable); scope: warning without measurement against measurement-first rule.
- X5, Release-age cooldown labelled consensus while its effectiveness rests on one T1 assertion and vendor figures: SUPPLY-C12 against SUPPLY-C13 and QUALITY-C46; labelling inconsistency inside the claim base; consolidation should treat the effect as single-source.

**Folklore (60 beliefs: 44 from `folklore:` tags, counted once after merging 46 tagged rows, plus 16 added from sources that warn against or confirm a belief).**

- Refuted (37), grounded unless L3 says otherwise: const makes a value constant (LANG-C35); Object.freeze makes an object (or nested data) deeply immutable (LANG-C38); TypeScript types protect against bad data at runtime (TYPES-C02); Node.js type-checks the TypeScript it runs (TYPES-C03); a missing return in a then callback is harmless (ASYNC-C01); unhandled rejections only print a warning (ASYNC-C04); Promise.all or race cancels the losing operations (ASYNC-C09); promises can be cancelled (ASYNC-C25); setTimeout(fn, 0) runs at once or exactly on time (ASYNC-C31); 0 ms timers fire with no delay (ASYNC-C32); then on an already resolved promise runs immediately (ASYNC-C35); process.nextTick is the right general-purpose way to defer (ASYNC-C36); async/await is slower than promise chains (ASYNC-C52); cyclic imports always crash (STRUCT-C08); an underscore prefix keeps a member private (STRUCT-C40); innerHTML is safe because script tags inserted that way do not run (DOMSEC-C10); a string that passes an HTML filter is safe wherever it is later rendered (DOMSEC-C13); Trusted Types sanitizes input by itself (DOMSEC-C16); a CSP with a domain allowlist stops XSS (DOMSEC-C28); XSS needs script elements or event handlers (DOMSEC-C48); Node core will fix prototype pollution for you (RUNSEC-C01); --disable-proto fixes prototype pollution (RUNSEC-C08); new Function is a safe alternative to eval (RUNSEC-C16); node:vm is a sandbox for untrusted code (RUNSEC-C22); path.normalize or isAbsolute sanitizes user paths (RUNSEC-C27); a regex with a nested quantifier is necessarily vulnerable (RUNSEC-C32); a package with provenance is safe (SUPPLY-C18); a signed package is a trustworthy package (SUPPLY-C19); every npm audit finding is an exploitable risk (SUPPLY-C22); devDependencies never reach production (SUPPLY-C23); typosquatting is just typing mistakes (SUPPLY-C25); assert.deepEqual is a safe equality check (QUALITY-C25); circular references cause memory leaks in JavaScript (RUNTIME-C27); a minor or patch release of an npm dependency is non-breaking (STRUCT-C67); code in a Node process is isolated from the application (dependencies are sandboxed) (RUNSEC-C41); a tag-manager data layer sandboxes third-party tags (DOMSEC-C42); lockfile semantics are the same across package managers (SUPPLY-C40).
- Restricted (13), grounded unless L3 says otherwise: strict mode is just a stricter subset of the language (LANG-C02); BigInt should replace Number for large or everyday integers (LANG-C31); JSON.parse(JSON.stringify(x)) is the way to deep copy (LANG-C44); logical OR is the safe way to supply a default (LANG-C50); CommonJS cannot load ES modules (STRUCT-C16); built-in prototypes can be extended safely (tag text: never subclass built-ins) (STRUCT-C44); every target=_blank link needs rel=noopener added (DOMSEC-C47); JSON.parse of untrusted JSON is inherently safe (RUNSEC-C13); environment variables are a safe place for secrets (RUNSEC-C47); high coverage means effective tests (QUALITY-C36); holey arrays must be avoided for speed (RUNTIME-C55); heap snapshots are infeasible on large production heaps (RUNTIME-C57); V8 offers a non-backtracking regex engine for ReDoS defence (RUNSEC-C33).
- Confirmed (10), grounded unless L3 says otherwise: use === instead of == (LANG-C17); never use var (LANG-C37); never build code from strings (eval, new Function, string setTimeout) (RUNSEC-C14); never keep tokens or credentials in localStorage or sessionStorage (DOMSEC-C35); commit the lockfile and install with npm ci (SUPPLY-C03); innerHTML with untrusted data is an XSS sink (DOMSEC-C01); prefer unknown to any (TYPES-C15); for...in over untrusted-keyed objects is risky (RUNSEC-C07); a pathological regex can block a Node server for seconds (ReDoS) (ASYNC-C40); install scripts are a supply-chain risk (SUPPLY-C29).

**Maintainer questions (14, recommendations inferred).** Q1 type layer: TypeScript. Q2 pinning: lockfile committed and `npm ci`, ranges for libraries, exact pins for approved install scripts. Q3 private marking: `#` on native ES2022 targets. Q4 exports: named. Q5 `== null`: allow through lint config. Q6 coercion shorthands: do not forbid by rule. Q7 cycles: lint as warning. Q8 top-level await: allow in entry points. Q9 formatter: one dedicated formatter, unranked. Q10 coverage: report, never a target. Q11 Trusted Types: named policies, default only for third-party. Q12 permission model: seat belt only. Q13 noopener: keep explicit. Q14 setAttribute: forbid on event-handler attributes with untrusted data.

## L3 full

Pinned: 16 contested topics (from the 17 contested claims the checker reports): private-member marking; `== null`; implicit coercion shorthands; type layer; module cycles; top-level await; default versus named exports; paradigm and defects; Trusted Types default policy; setAttribute safety; target=_blank noopener; permission model strength; dependency pinning; formatter choice; coverage target; htmx documentation version. Folklore: 60 beliefs, confirmed 10, restricted 13, refuted 37.

Method. All 17 `agreement: contested` rows were extracted from the claim tables of slots 01 to 10 and read in full (positions, quote, mechanism). Cross-slot conflicts were searched by scanning every non-contested row for `positions:` tags and for style-guide sources, then reading the rows that plausibly overlap. The checker was run: 544 claims, 193 consensus, 326 single-source, 17 contested, 8 majority, 0 errors. Source tiers and restrictions come from the register. Nothing outside the register is cited.

### 1. Disagreements

The 17 contested claims group into 16 topics: LANG-C12 and STRUCT-C41 are the same question (private marking) and form topic 1. Each topic below gives every position, its holders, the condition under which it applies, and whether the disagreement is real or a difference of scope.

#### Topic 1. Private-member marking (LANG-C12, STRUCT-C41, with STRUCT-C40)

- MDN, SRC-091 and SRC-008, T1: `#` gives hard privacy enforced at runtime; applies wherever `#` is supported.
- TC39 class fields, SRC-024, T1 restricted: design rationale is no backdoor to private state; same condition.
- Google JS guide, SRC-239, T2 restricted: `@private` members may optionally end in a trailing underscore (guide position).
- Airbnb, SRC-312, T3 restricted: no leading or trailing underscores, since they are public API (guide position).
- Google TS guide, SRC-244, T2 restricted: do not use `#`; use TypeScript `private`, for emit size and performance when down-levelled (guide position, reason stated).
- Verdict: Real disagreement between style guides. The mechanism is undisputed: an underscore name is a public property, a `#` name is not a property. The condition that separates them is the compile target: native ES2022 output or not. Certainty: grounded.

#### Topic 2. Keep `== null` or forbid every `==` (LANG-C19)

- Google JS, SRC-239: `== null` is an allowed exception that catches null and undefined.
- ESLint eqeqeq, SRC-002, T1: default `always` forbids it; options `null: ignore` or `smart` allow it.
- Airbnb, SRC-312: always `===`.
- MDN, SRC-011: describes the null and undefined behaviour without a rule.
- Verdict: Real, purely stylistic. Mechanism: ECMA-262 7.2.13 makes `null == undefined` true and equal to nothing else. Condition: choose per code base and encode it in the lint configuration. Certainty: grounded.

#### Topic 3. Implicit coercion shorthands (LANG-C22)

- ESLint no-implicit-coercion, SRC-003, T1 restricted: flag `!!x`, `+x`, `'' + x`; rationale is readability, not mechanism.
- Google JS and Airbnb, SRC-239 and SRC-312: prefer `Boolean()`, `Number()`, `String()`.
- Pradel and Sen, SRC-238, T2 restricted: 80.42 percent of function executions coerce, 98.85 percent of coercions likely harmless, a small rare set harmful (2015 corpus).
- Verdict: A difference of evidence kind, not of fact: the rule rests on readability, the study on harm. They do not contradict each other. A guideline may adopt the rule as a readability convention without claiming it prevents defects. Certainty: grounded.

#### Topic 4. Type layer (TYPES-C01)

- TypeScript: Google JS guide (frozen, recommends migrating) and Google TS guide, SRC-239 and SRC-244; condition: any project with a build or type-check step.
- JSDoc-checked JavaScript: no admitted holder advocates it; SRC-047 and SRC-044 document it up to TypeScript 6.x, SRC-034 removes some JSDoc forms in 7.0 and SRC-036 lists known differences; condition: projects avoiding a compile step.
- None: no admitted holder; only SRC-240 (T2 restricted, 2017) measuring that Flow and TypeScript each detect 15 percent of 400 public bugs.
- Verdict: Not a conflict between holders but an imbalance of evidence: one position has advocates, one has tool facts, one has none. Node type stripping (SRC-038) makes TypeScript runnable without a build, which weakens the usual reason to avoid it (inferred). Certainty: grounded.

#### Topic 5. Module cycles (STRUCT-C09, with STRUCT-C08)

- MDN, SRC-029: usually avoid, error-prone.
- Google JS, SRC-239: do not create cycles though the spec allows them.
- eslint-plugin-import maintainers, SRC-313, T3 restricted: always a dangerous anti-pattern, no evidence given; the rule is documented as expensive (STRUCT-C10).
- Node CJS docs, SRC-089, T1: cycles are a supported loading mechanism through partial exports; no recommendation.
- Verdict: Real but thin: nobody measures the defect cost, and Node only documents behaviour. The refuted belief that cycles always crash (STRUCT-C08) is separate and settled by SRC-029 and SRC-089. Certainty: grounded.

#### Topic 6. Top-level await as a footgun (STRUCT-C19, with STRUCT-C18, STRUCT-C16)

- Critics recorded in the TC39 proposal, SRC-092, T1: coordination and deadlock surprises.
- Champions Borins and Startsev, same source: education suffices, deadlocks already exist, `import()` inside TLA costs the same.
- Verdict: Real inside one source, no measurement. Mechanism is agreed: TLA turns graph evaluation into an async dependency graph, and `require()` of such a graph throws ERR_REQUIRE_ASYNC_MODULE (STRUCT-C16). Certainty: grounded.

#### Topic 7. Default versus named exports (STRUCT-C24)

- Google JS and Google TS, SRC-239 and SRC-244: named only; a default export has no canonical name.
- Airbnb, SRC-312 10.6: prefer default when a module has a single export.
- MDN, SRC-029: neutral; names the CommonJS and AMD interoperation purpose.
- Verdict: Real, style, applies to application and library modules alike; the guides' tooling reason (rename refactors) is their own. Certainty: grounded.

#### Topic 8. Paradigm and defect rates (STRUCT-C63, STRUCT-C64)

- Ray et al. 2014, SRC-251, T2 restricted: modest language effect, functional somewhat better than procedural, process factors dominate.
- Berger et al. 2019, SRC-258, T2 restricted: reproduction finds four of eleven languages significant, exceedingly small effects.
- Ray, Devanbu, Filkov rebuttal, SRC-314, T3 restricted, not peer reviewed: largely replicated, effects small.
- Verdict: One GitHub dataset, three papers, a dispute over analysis. Scope: language-level comparison across languages, not paradigm inside JavaScript. A guideline should state no paradigm rule on defect evidence (STRUCT-C64, inferred). Certainty: grounded.

#### Topic 9. Trusted Types default policy (DOMSEC-C17)

- MDN SRC-120 and web.dev SRC-267 (spec editor's position): default policy only while transitioning legacy code, or as a last resort.
- Roth et al., SRC-269, T2, USENIX 2024: with third-party code only a default policy works in practice.
- Verdict: Mostly scope. Condition: code you control gets named policies; third-party code that cannot be changed may need the default policy. Mechanism: the default policy is invoked implicitly for every string reaching a sink. Certainty: grounded.

#### Topic 10. setAttribute safety (DOMSEC-C25, with DOMSEC-C07)

- OWASP DOM XSS sheet, SRC-108, T1 restricted: `setAttribute` is a safe way to build dynamic interfaces.
- MDN Trusted Types API, SRC-120: `setAttribute` value is a TrustedScript sink, presumably for event-handler attributes (inferred; the verbatim condition was not obtained).
- Web Security Academy, SRC-316, T3: lists `setAttribute` among DOM-based injection sinks, catalogue facts only.
- Verdict: Real as written, probably reconcilable by condition (event-handler and `href` or `src` attribute names). The reconciliation is inferred, so this topic stays open until the MDN condition is read verbatim. Certainty: grounded for the positions; open for the condition.

#### Topic 11. target=_blank noopener (DOMSEC-C47)

- HTML Standard, SRC-103, T1: noopener is implied for `_blank` unless `rel=opener` is present.
- OWASP HTML5 sheet, SRC-110: add `rel=noopener noreferrer` explicitly.
- Verdict: A difference of time and browser support, not of principle. Explicit rel stays harmless and covers older browsers (inferred). `noreferrer` additionally drops the Referer. Certainty: grounded; condition inferred.

#### Topic 12. Strength of the permission model (RUNSEC-C38, with RUNSEC-C41)

- Node permissions API, SRC-128, T1: seat belt for trusted code, no guarantees against malicious code.
- Node threat model, SRC-140, T1: not a boundary against intentional misuse or a compromised process.
- Node security best practices, SRC-078, T1 restricted: can help contain the impact of malicious or compromised dependencies.
- Verdict: Scope plus one real inconsistency inside the Node documentation: containment of hostile code against a seat belt for trusted code. The stability labels also differ (permissions page stable since v23.5.0 and v22.13.0, CLI page marks `--permission` Stability 1.1). Certainty: grounded.

#### Topic 13. Dependency pinning (SUPPLY-C06, with SUPPLY-C05, STRUCT-C67, SUPPLY-C08, SUPPLY-C41, SUPPLY-C35)

- Node best practices, SRC-078: pin to a specific immutable version, not a range.
- OWASP supply chain sheet, SRC-156: limit to a verified version through the lockfile.
- OpenSSF npm guide v1.1, SRC-154, T1 restricted (archived 2023): allow a minimum-to-latest range such as caret or tilde.
- He et al. 2025, SRC-287, T2: direct pinning can raise exposure to malicious updates in larger graphs; prefer collective ecosystem pinning.
- Related, not opposed: exact pins do not pin transitives, only the lockfile does (SUPPLY-C05); 44 percent of manifesting breaking changes came in minor and patch releases (STRUCT-C67, SRC-255, T2), which weighs against trusting ranges; CISA, SRC-295, pins to pre-incident versions after a compromise (SUPPLY-C41); npm 12 allowScripts wants exact versions (SUPPLY-C08); Scorecard rates Pinned-Dependencies medium risk (SUPPLY-C35).
- Verdict: Real. Condition: size of the dependency graph, and library (ranges, to avoid forcing duplicates on consumers, inferred) against application (lockfile). All agree the lockfile is committed (SUPPLY-C03). Certainty: grounded.

#### Topic 14. Formatter choice (QUALITY-C13, with QUALITY-C12, QUALITY-C15)

- ESLint technical steering committee, SRC-298, T2: Prettier, dprint or the @stylistic plugin.
- Biome documentation, SRC-162, T1 restricted: one tool whose formatter handles all formatting decisions beside the linter.
- Prettier documentation, SRC-177 and SRC-178, T1 restricted: run Prettier separately from linters; eslint-config-prettier only.
- Verdict: Real but unrankable: the holders are the tools' own documents (gate G5), so no admitted source can prefer one. The shared point is that layout belongs to a dedicated formatter, not lint rules. Certainty: grounded; no ranking source exists.

#### Topic 15. Coverage target (QUALITY-C36)

- Inozemtseva and Holmes, SRC-297, T2 restricted: coverage finds under-tested code, not a quality target; correlation low to moderate once suite size is controlled (31,000 suites, five Java systems).
- OpenSSF passing criteria, SRC-174, T1: suggested that suites cover most or all branches and inputs.
- Verdict: Scope: a study of Java suites against a SUGGESTED criterion that is not a numeric target. They are compatible if coverage is reported but not gated. Transfer to JavaScript is inferred. Certainty: grounded for each; transfer inferred.

#### Topic 16. htmx documentation version (FW-C22)

- htmx.org docs, SRC-213: document 2.x (2.0.11).
- htmx policy and 4.x docs, SRC-214 and SRC-212: 4.x current, 2.x and 1.9.x supported.
- Verdict: Scope only: documentation lags the release line; not a disagreement about what to do. Rule: pick the doc set that matches the pinned major. Certainty: grounded.

### 2. Cross-slot tensions not marked contested

Found by scanning non-contested rows for `positions:` tags and by pairing rows that cite the same guide or mechanism. None is a counted topic, because the conflict is a difference of scope. Certainty: inferred for all five.

| id | tension | claims | reading |
|---|---|---|---|
| X1 | Freezing built-ins as a hardening step against never modifying built-ins | RUNSEC-C09 against LANG-C14 and STRUCT-C44 | scope: hardening versus patching; freezing blocks later polyfills, inferred |
| X2 | Sanitizer library against the native Sanitizer API | DOMSEC-C11 against DOMSEC-C08 | scope: availability; both can coexist (DOMSEC-C23) |
| X3 | Null-prototype object: `Object.create(null)` against the literal `{ __proto__: null }` | RUNSEC-C05 (OWASP last resort, MDN lists both) | scope: strength of defence, already one claim |
| X4 | Weight of prototype and array performance warnings | STRUCT-C43 (MDN warns of deoptimisation) against RUNTIME-C55 and RUNTIME-C63 (V8: rarely measurable) | scope: warning without measurement against measurement-first rule |
| X5 | Release-age cooldown labelled consensus while its effectiveness rests on one T1 assertion and vendor figures | SUPPLY-C12 against SUPPLY-C13 and QUALITY-C46 | labelling inconsistency inside the claim base; consolidation should treat the effect as single-source |

Checked and not a tension: LANG-C45 with ASYNC-C18 (same rule, throw only Error); QUALITY-C12, C13 and C15 (consistent, one rule: dedicated formatter); LANG-C38 with DOMSEC-C52 (both say freeze is shallow); TYPES-C25 with QUALITY-C18 (same Google TS position cited twice, one holder).

### 3. Folklore audit

Selection. Beliefs enter only through an admitted source that addresses them. 44 distinct beliefs come from the `folklore:` tags (46 rows; ASYNC-C04 with RUNTIME-C40, and LANG-C38 with RUNSEC-C09, each pair is one belief). 16 more were added by this slot from rows whose admitted source corrects a belief (6, rows STRUCT-C67, RUNSEC-C41, DOMSEC-C42, RUNTIME-C57, SUPPLY-C40, RUNSEC-C33) or confirms a widely held rule (10); their belief wording is inferred from the claim text. No popularity evidence is cited anywhere. Verdict meaning: confirmed (the source supports the belief), restricted (true only under the stated condition), refuted (the source contradicts it). Where the only ground is T2, the row says so: that is a weaker ground than T1 under the plan's threshold.

Counts: 60 beliefs; confirmed 10, restricted 13, refuted 37. Of the 44 tagged beliefs: refuted 33, restricted 11, confirmed 0 (the tags record corrections by construction).

| belief | verdict | claim ids | T1 ground (or the ground that exists) | condition or correction | certainty | origin |
|---|---|---|---|---|---|---|
| const makes a value constant | refuted | LANG-C35 | SRC-009; SRC-015 | const fixes the binding; the object or array stays mutable | grounded | tag |
| Object.freeze makes an object (or nested data) deeply immutable | refuted | LANG-C38; RUNSEC-C09; DOMSEC-C52 | SRC-015; SRC-027 7.3.15; SRC-139; SRC-137 | Freeze is shallow: SetIntegrityLevel touches own keys only. Two tagged rows (LANG-C38, RUNSEC-C09) count as one belief | grounded | tag |
| TypeScript types protect against bad data at runtime | refuted | TYPES-C02 | SRC-043 | Types and assertions are erased; no runtime check exists. TypeScript handbook says so in terms | grounded | tag |
| Node.js type-checks the TypeScript it runs | refuted | TYPES-C03 | SRC-038 | Node strips types to whitespace; no checker runs, so run tsc --noEmit separately | grounded | tag |
| a missing return in a then callback is harmless | refuted | ASYNC-C01 | SRC-075; SRC-072 | The dependent promise fulfils with undefined and later handlers run before the inner work finishes | grounded | tag |
| unhandled rejections only print a warning | refuted | ASYNC-C04; RUNTIME-C40 | SRC-082; SRC-068; SRC-079 | Warn was the default before Node 15; since Node 15 the default mode is throw. Two tagged rows count as one belief | grounded | tag |
| Promise.all or race cancels the losing operations | refuted | ASYNC-C09 | SRC-075; SRC-056 | The other operations keep running, their outcomes unavailable | grounded | tag |
| promises can be cancelled | refuted | ASYNC-C25 | SRC-075; SRC-055; SRC-057 | Promise has no cancellation protocol; cancel the underlying operation with AbortController | grounded | tag |
| setTimeout(fn, 0) runs at once or exactly on time | refuted | ASYNC-C31 | SRC-062; SRC-067; SRC-071 | A delay is a lower bound; callbacks run as tasks when the loop is free | grounded | tag |
| 0 ms timers fire with no delay | refuted | ASYNC-C32 | SRC-062; SRC-067 | Browsers clamp nested timers (level above 5) to 4 ms; Node sets delays below 1 or NaN to 1 ms | grounded | tag |
| then on an already resolved promise runs immediately | refuted | ASYNC-C35 | SRC-075; SRC-071 | Reactions never run synchronously; they are microtasks after the current run | grounded | tag |
| process.nextTick is the right general-purpose way to defer | refuted | ASYNC-C36 | SRC-071 | Node docs: use setImmediate in all cases; recursive nextTick starves I/O | grounded | tag |
| async/await is slower than promise chains | refuted | ASYNC-C52 | SRC-249 (T2 restricted; no T1 ground) | V8 7.2 (2018) cut await to one tick and the V8 team advises async functions; no admitted current-engine measurement, so the present-day size of any gap is open | grounded for 2018, open for today | tag |
| cyclic imports always crash | refuted | STRUCT-C08 | SRC-029; SRC-089 | ESM throws only on use of an uninitialised binding; CJS returns a partial exports object. Whether to ban cycles is a separate, contested question (topic 5) | grounded | tag |
| an underscore prefix keeps a member private | refuted | STRUCT-C40 | SRC-091 | Underscore names are ordinary public properties; only # is enforced | grounded | tag |
| innerHTML is safe because script tags inserted that way do not run | refuted | DOMSEC-C10 | SRC-100; SRC-101; SRC-108 | Script execution is disabled but event-handler attributes still run; innerHTML stays on OWASP's sink list | inferred | tag |
| a string that passes an HTML filter is safe wherever it is later rendered | refuted | DOMSEC-C13 | SRC-102 8.6.6.4 (T1); SRC-266 (T2 restricted, mechanism) | Mutation XSS: the filter's parse and the browser's parse differ | grounded | tag |
| Trusted Types sanitizes input by itself | refuted | DOMSEC-C16 | SRC-097 | MDN: the API supplies no sanitizer, only the guarantee that your function ran | grounded | tag |
| a CSP with a domain allowlist stops XSS | refuted | DOMSEC-C28 | SRC-097 (T1, nonce guidance); SRC-263 (T2 restricted, 94.72 percent bypass, 2016) | The measurement is Google's 2016 corpus; boundary web-architecture | grounded | tag |
| XSS needs script elements or event handlers | refuted | DOMSEC-C48 | SRC-109; SRC-102 8.6.6.2; SRC-106 | DOM clobbering is HTML-only injection through id and name | grounded | tag |
| Node core will fix prototype pollution for you | refuted | RUNSEC-C01 | SRC-140; SRC-078 | Node trusts application input; pollution needing attacker input is not a core vulnerability | grounded | tag |
| --disable-proto fixes prototype pollution | refuted | RUNSEC-C08 | SRC-139; SRC-137; SRC-079 | constructor.prototype stays reachable | grounded | tag |
| new Function is a safe alternative to eval | refuted | RUNSEC-C16 | SRC-124; SRC-123 | Also an injection sink; differs only in global scope | grounded | tag |
| node:vm is a sandbox for untrusted code | refuted | RUNSEC-C22 | SRC-129 | Node docs: not a security mechanism | grounded | tag |
| path.normalize or isAbsolute sanitizes user paths | refuted | RUNSEC-C27 | SRC-127 | Node docs: isAbsolute is not safe for mitigating traversal; normalize is lexical | grounded | tag |
| a regex with a nested quantifier is necessarily vulnerable | refuted | RUNSEC-C32 | SRC-279 (T2 restricted; no T1 ground) | Anti-patterns are necessary but not sufficient signals | grounded | tag |
| a package with provenance is safe | refuted | SUPPLY-C18 | SRC-147 | npm docs: provenance does not guarantee absence of malicious code | grounded | tag |
| a signed package is a trustworthy package | refuted | SUPPLY-C19 | SRC-142; SRC-149 | Registry signatures detect tampering by mirrors and proxies, not a malicious publisher | grounded | tag |
| every npm audit finding is an exploitable risk | refuted | SUPPLY-C22 | SRC-285 and SRC-286 (T2; no T1 ground) | 68.28 percent of package-level impacts are unreachable noise | grounded | tag |
| devDependencies never reach production | refuted | SUPPLY-C23 | SRC-286 (T2; no T1 ground) | 28.2 percent of dev-configured dependencies were used in production in the studied projects | grounded | tag |
| typosquatting is just typing mistakes | refuted | SUPPLY-C25 | SRC-283 (T2; no T1 ground) | 13 confusion mechanisms, many semantic | grounded | tag |
| assert.deepEqual is a safe equality check | refuted | QUALITY-C25 | SRC-171 | Legacy mode compares with ==; use node:assert/strict | grounded | tag |
| circular references cause memory leaks in JavaScript | refuted | RUNTIME-C27 | SRC-193 | Engines use reachability (mark and sweep), not reference counting | grounded | tag |
| a minor or patch release of an npm dependency is non-breaking | refuted | STRUCT-C67 | SRC-255 (T2; no T1 ground) | 44 percent of manifesting breaking changes arrived in minor and patch releases; exact denominator unverified | grounded | added by this slot |
| code in a Node process is isolated from the application (dependencies are sandboxed) | refuted | RUNSEC-C41 | SRC-140; SRC-078 | Node trusts all code in the process; no in-process privilege boundary | grounded | added by this slot |
| a tag-manager data layer sandboxes third-party tags | refuted | DOMSEC-C42 | SRC-112 | OWASP: a data layer is not a sandbox | grounded | added by this slot |
| lockfile semantics are the same across package managers | refuted | SUPPLY-C40 | SRC-292 (T2); SRC-157 (T1, npm only) | Seven managers differ widely in generation and content | grounded | added by this slot |
| strict mode is just a stricter subset of the language | restricted | LANG-C02 | SRC-017 | MDN: strict mode changes silent errors into thrown errors, so the same code can behave differently; it is a variant with changed semantics, not only a syntax filter. Preference to use it is inferred from MDN's three reasons | inferred | tag |
| BigInt should replace Number for large or everyday integers | restricted | LANG-C31 | SRC-007; SRC-014 | True only where values above 2^53 are reasonably expected; MDN says to use BigInt only then | grounded | tag |
| JSON.parse(JSON.stringify(x)) is the way to deep copy | restricted | LANG-C44 | SRC-018 | Adequate only for JSON-safe data; structuredClone keeps cycles and typed arrays, drops prototypes, throws on functions and DOM nodes. The JSON side is inferred from what structuredClone adds | inferred | tag |
| logical OR is the safe way to supply a default | restricted | LANG-C50 | SRC-013 | Safe only if 0, empty string, NaN and false are all invalid values; otherwise use ?? | grounded | tag |
| CommonJS cannot load ES modules | restricted | STRUCT-C16 | SRC-089; SRC-030 | require(esm) works only when the graph has no top-level await, else ERR_REQUIRE_ASYNC_MODULE; no longer experimental as of Node 25.4.0 | grounded | tag |
| built-in prototypes can be extended safely (tag text: never subclass built-ins) | restricted | STRUCT-C44 | SRC-088 | MDN warns against patching built-in prototypes (SmooshGate); the only good reason it names is backporting. The admitted source does not address subclassing, so the tag's wording is not judged | grounded | tag |
| every target=_blank link needs rel=noopener added | restricted | DOMSEC-C47 | SRC-103; SRC-110 | HTML Standard implies noopener unless rel=opener; explicit rel is OWASP's advice and matters for browsers that predate the default (inferred). Also contested, topic 11 | grounded; condition inferred | tag |
| JSON.parse of untrusted JSON is inherently safe | restricted | RUNSEC-C13 | SRC-078; SRC-131 | Parsing creates an own __proto__ property harmlessly; pollution occurs when the result is merged or assigned | grounded | tag |
| environment variables are a safe place for secrets | restricted | RUNSEC-C47 | SRC-138; SRC-078 | OWASP: not recommended unless other methods are not possible (container context); every module in the process can read them. Agreement is majority | grounded | tag |
| high coverage means effective tests | restricted | QUALITY-C36 | SRC-174 (T1, suggestion only); SRC-297 (T2 restricted, Java) | Coverage finds under-tested code; not a quality target. Transfer from five Java systems to JavaScript is inferred; also contested, topic 15 | grounded for study; transfer inferred | tag |
| holey arrays must be avoided for speed | restricted | RUNTIME-C55 | SRC-302 (T2 restricted; no T1 ground) | V8: difference usually too small to matter; act only on a measurement | grounded | tag |
| heap snapshots are infeasible on large production heaps | restricted | RUNTIME-C57 | SRC-306 (T2; no T1 ground) | True before two V8 defects were fixed (V8 11.5.130); Node version carrying the fix not stated | grounded | added by this slot |
| V8 offers a non-backtracking regex engine for ReDoS defence | restricted | RUNSEC-C33 | SRC-121; SRC-271 (T2 restricted) | Experimental, behind a flag, no backreferences, lookarounds, u or i flags; status as of 2021, current status open | grounded | added by this slot |
| use === instead of == | confirmed | LANG-C17 | SRC-012; SRC-011 | Almost always correct; the == null exception is itself a contested style choice (topic 2) | grounded | added by this slot |
| never use var | confirmed | LANG-C37 | SRC-021; SRC-004 | Function scope, hoisting, redeclaration | grounded | added by this slot |
| never build code from strings (eval, new Function, string setTimeout) | confirmed | RUNSEC-C14; RUNSEC-C15; DOMSEC-C03 | SRC-123; SRC-124; SRC-108 | Consensus across MDN, OWASP; Trusted Types gives a gated path in browsers (RUNSEC-C19) | grounded | added by this slot |
| never keep tokens or credentials in localStorage or sessionStorage | confirmed | DOMSEC-C35; DOMSEC-C36 | SRC-111; SRC-110; SRC-117 | Readable by any script of the origin | grounded | added by this slot |
| commit the lockfile and install with npm ci | confirmed | SUPPLY-C03; SUPPLY-C04 | SRC-157; SRC-150; SRC-156 | Same tree on every install | grounded | added by this slot |
| innerHTML with untrusted data is an XSS sink | confirmed | DOMSEC-C01 | SRC-108; SRC-097 | Use a safe DOM API or a sanitizer | grounded | added by this slot |
| prefer unknown to any | confirmed | TYPES-C15; TYPES-C16 | SRC-045; SRC-048 | Nothing may be done with unknown until narrowed | grounded | added by this slot |
| for...in over untrusted-keyed objects is risky | confirmed | RUNSEC-C07 | SRC-139; SRC-078 | Visits inherited, possibly polluted, properties; use Object.hasOwn and Object.keys | grounded | added by this slot |
| a pathological regex can block a Node server for seconds (ReDoS) | confirmed | ASYNC-C40; TYPES-C32 | SRC-053; SRC-250 (T2) | A match cannot be chunked on the main thread | grounded | added by this slot |
| install scripts are a supply-chain risk | confirmed | SUPPLY-C29; SUPPLY-C09 | SRC-155; SRC-078 | Agreement is majority for the risk signal, consensus for disabling scripts; npm 12 blocks them by default (SUPPLY-C08) | grounded | added by this slot |

Beliefs with no T1 ground, resting on T2 alone: async/await slower (SRC-249), regex nested quantifier (SRC-279), audit findings (SRC-285, SRC-286), devDependencies (SRC-286), typosquatting (SRC-283), holey arrays (SRC-302), heap snapshots (SRC-306), semver minors (SRC-255), lockfile semantics (SRC-292 beyond npm). Their verdicts stand as the T2 holders' findings and are single-source.

### 4. Maintainer questions

Each recommendation is inferred; the build must not settle contested choices (plan: contested choices become `undecided` nodes). Topics 8 and 16 are not questions: the guideline states no paradigm rule, and htmx needs only the pin-the-major rule.

| id | question | recommendation (inferred) | if no decision |
|---|---|---|---|
| Q1 | Type layer: which of TypeScript, JSDoc-checked JavaScript, none does the guideline recommend by default? (TYPES-C01) | TypeScript with strict settings (Google TS, handbook; Node type stripping removes the build step); JSDoc-checked JS as a documented alternative with the 7.0 JSDoc removals; none: no admitted advocate. Language-semantics rules apply in every case (plan Q1). | Do nothing: the guideline lacks a headline decision. |
| Q2 | Dependency policy: exact pins, ranges, or lockfile only? (SUPPLY-C06) | Commit the lockfile, install with `npm ci`, ranges for libraries, exact versions only where a tool requires them (allowScripts), cooldown treated as single-source (X5). | Contested node stays undecided. |
| Q3 | Private members: `#`, underscore or TypeScript `private`? (LANG-C12, STRUCT-C41) | `#` on native ES2022 targets; never an underscore as privacy; TypeScript `private` only where the build down-levels `#` and the cost is measured (inferred). | Three positions with no rule. |
| Q4 | Exports: named only, or default allowed? (STRUCT-C24) | Named only for libraries and shared modules; allow default where a framework requires it (inferred). | No rule. |
| Q5 | `== null`: allow as the one `==`, or forbid all? (LANG-C19) | Allow, by `eqeqeq` option `null: ignore`, because the mechanism is exact; forbid every other `==`. | Lint default forbids it. |
| Q6 | Forbid `!!x`, `+x`, `'' + x`? (LANG-C22) | Do not forbid by default; state it as a readability option, since the only measurement finds harm rare. | Readability rule applied without grounds. |
| Q7 | Module cycles: ban or tolerate? (STRUCT-C09) | Warn via lint (cost noted), do not claim a measured defect rate. | Unmeasured ban. |
| Q8 | Top-level await: allowed? (STRUCT-C19) | Allow in application entry points, not in modules that may be `require()`d (STRUCT-C16). | No rule. |
| Q9 | Formatter: which? (QUALITY-C13) | Require one dedicated formatter, name Prettier, dprint and Biome as options without ranking; no admitted source ranks them. | No formatter rule. |
| Q10 | Coverage: gate or report? (QUALITY-C36) | Report to find untested code; no percentage gate. | Gate by folklore. |
| Q11 | Trusted Types: default policy allowed? (DOMSEC-C17) | Named policies; default policy only for third-party code that cannot change. | Open. |
| Q12 | Permission model: how is it described? (RUNSEC-C38) | Seat belt for trusted code only; never a sandbox, never the only control. | Inconsistent Node wording carried into the guideline. |
| Q13 | Link opener: require explicit `rel=noopener`? (DOMSEC-C47) | Keep it explicit; harmless and covers older browsers (inferred). | Rule omitted. |
| Q14 | setAttribute: safe or sink? (DOMSEC-C25) | Forbid untrusted data in event-handler attributes; confirm the MDN condition verbatim before the final wording (open). | Open. |

### 5. Gaps and checks left open

- Topic 10 and DOMSEC-C25: the verbatim MDN condition for `setAttribute` as a TrustedScript sink was not obtained by the extraction slot; open until read.
- No admitted T1 source measures module-cycle cost, top-level-await hazard, or any style-guide preference; those topics cannot be settled by authority (open).
- Popular-belief coverage is limited to what admitted sources address: beliefs about frameworks, bundlers and performance folklore beyond RUNTIME-C27, C55, C57 and ASYNC-C52 are absent because no admitted source addresses them, not because they are false.
- The checker's 491 restricted citations mean most positions above are guide positions, never evidence; where a verdict rests on a T2 source alone it is marked.
