# Stage 7 fixes: JavaScript guideline graphs

## L1 headline

Of the 21 findings, 18 are fixed, 1 is partly fixed (F04), 1 is not fixed here by decision (F07, listed under "Not covered" in `intent_graphs/README.md`) and 1 belongs to the orchestrator (F20, a stray `__pycache__` I created and removed is the only trace). Both graphs were rebuilt and re-validated: 0 errors, 0 warnings each; `check_ledger.py` and `check_complete.py` pass (0 failures). Certainty: grounded for the build and checks (run by script), inferred for the wording quality of about 70 rewritten rules (read, not independently reviewed).

Pinned:
- Findings: fixed 18 (F01, F02, F03, F05, F06, F08 to F19, F21), partly fixed 1 (F04), not fixed 1 (F07), not mine 1 (F20).
- epistemic_state, js-philosophy before then after (108 nodes): known alone 54 then 45; known with unvalidated or conflict 43 then 53; known with another issue (gap, missing, roll-up note) 8 then 7; risky 2 then 2; undecided 1 then 1; deferred 0 then 0.
- epistemic_state, pig-js-defaults before then after (270 nodes): known alone 99 then 73; known with unvalidated or conflict 136 then 163; known with another issue 21 then 18; risky 2 then 4 (FRAMEWORK_SHORTLIST, CONTRACTS.LAYER.1 added); undecided 12 then 12; deferred 0 then 0 (one node carries a `deferred` issue, unchanged).
- Validate, js-philosophy: `nodes: 108, links: 48, inter_links: 23, issues: 0, errors: 0, warnings: 0`. Validate, pig-js-defaults: `nodes: 270, links: 146, inter_links: 90, issues: 0, errors: 0, warnings: 0` (both with `-m intent_graphs/intent_resources.yaml`).
- `check_ledger.py`: `claims in: 608; placed: 608; missing 0; duplicated 0; unknown 0`; rows by graph js-philosophy 115, pig-js-defaults 486 (601 in all, was 587); roles rejected 55, fact 145, decision 356, acceptable-when 35, deferred 10; skeleton nodes 378. `check_complete.py`: `FAILS: 0` (constraints 71 + 320, was 71 + 313).
- F04: the current `crypto.timingSafeEqual` entry could not be read: the Playwright navigate call gave no answer (aborted after about 30 minutes), two fetch-tool reads were truncated before the section, a direct download was refused. The node keeps its flag.
- F18: SRC-341 URL note left as is in the register (recorded below).

## L2 claims

One line per finding (grounded = checked in the built graph or tables, inferred = judgment not independently reviewed):
- F01 fixed (grounded): INJECTION.2 now MUST NOT build a shell string from untrusted input, sanitized or not; argument arrays; state flags the stronger form as inferred from OWASP parameterization (RUNSEC-C24 cites SRC-136), Node's sentence kept as claim.
- F02 fixed (grounded): MUST kept on STRICT.2, STRICT.3, SECRETS.5; each says `unvalidated: source says consider`.
- F03 fixed (grounded): gates A, B, C and the platform-first default are constraints (rows added on FRAMEWORK_SHORTLIST and .1); state `risky | unvalidated: gates are the build's judgment, no admitted source states them`; decision log notes it.
- F04 partly fixed (grounded): flag `unvalidated: Node crypto text read in v6 docs only` added; the re-read failed (see L1), so the flag stays and no URL is recorded as read.
- F05 fixed (grounded): one rule applied by script to every node with a rule (`apply_flags.py`): weak claims, single-source rows, no claim, no quote; 102 nodes gained an issue (72 single-source, 32 no quote, 15 inferred or open, 4 no claim; some nodes more than one).
- F06 fixed (grounded): the 15 holder-position nodes carry `unvalidated: holder position only (<holder>)`; MUSTs kept as decided.
- F07 not fixed here (grounded): by decision; seven classes listed under "Not covered" in `intent_graphs/README.md`.
- F08 fixed (grounded): LAYER.1 `risky | conflict: JSDoc-checked JavaScript, none | unvalidated: decided by the build ...`; circular constraint replaced by MUST TypeScript when a build or type-check step can be adopted, plus an acceptable-when row for JSDoc-checked JavaScript; condition table in the node's notes.
- F09 fixed (grounded) with a limit: "Integration note", "Merged", row lists, row ids, gap ids and slot labels are out of constraints and design notes (log in `build/assemble/bookkeeping_log.md`); source and claim ids stay in design notes as evidence pointers.
- F10 fixed (grounded): SECRETS.2 MUST use authenticated encryption modes, `unvalidated: single source`.
- F11 fixed (grounded): ERRORS.2 MUST NOT leave a catch block empty without a comment stating why.
- F12 fixed (grounded): TEST_SUITE.2 SHOULD NOT gate on a coverage number; the OpenSSF position is a rejected-position note with its condition.
- F13 fixed (grounded for the text, inferred for the weight): THREATS.1 intent and constraint soften to what four incidents show; UPDATE.3 keeps lockfile and triage as MUST, npm audit as acceptable-when.
- F14 fixed (grounded): ESCAPE.6 names the ban-ts-comment configuration; LINT.1.2 names it as the one override.
- F15 fixed (grounded): INJECTION.5.2 holds a node-serialize MUST and "use js-yaml 4 or later if js-yaml parses untrusted YAML"; INJECTION.6.1 holds the allowlist MUST.
- F16 fixed for the named nodes (grounded), not exhaustive (inferred): DOM.6.1, UPDATE.2 (both rules), FRAMEWORK_EVIDENCE.1, DOM.4, EVOLUTION.2 are framework-neutral and undated; the facts are rows in design notes. Other versioned figures in rules (for example DIAGNOSE.3, PROCESS.4, INSTALL.2) were not touched.
- F17 fixed (grounded): 32 nodes whose rules rest on a claim with no quote or a paraphrase marker carry `unvalidated: quote not obtained (<claims>)`.
- F18 fixed (grounded for what the fetch tool returned): quotes corrected in RUNSEC-C37, RUNSEC-C35, SRVSEC-C27, SRVSEC-C07 (QUALITY-C35 also states 14 of 19); SRC-341 URL note left as is.
- F19 fixed (grounded): the five philosophy nodes no longer name JavaScript tools or platforms in intents or constraints; the names moved to rows of linked defaults nodes (LINT.2, PUBLISH.1, STRICT).
- F20 not mine: I created a `__pycache__` during my own runs and removed it (`find . -name __pycache__` is empty).
- F21 fixed (grounded): all 64 "MUST hold:" constraints are verb-first rules or facts in notes; 4 "MUST expect/know" rules rewritten; "74%" states 14 of 19.

## L3 full

### What was changed, by file

- `build/distill/claims_ledger.md`: statements rewritten for about 70 rows (64 former "MUST hold:" rows, plus F01, F10, F11, F12, F13, F14, F15, F16, F19, F21 rows), roles changed for DEFENSE-104 and CONTROL-035 (to decision) and DEFENSE-171 (rejected to decision), 14 rows added (FRAMEWORK_SHORTLIST gates and default, LAYER.1 acceptable-when, UPDATE.3 acceptable-when, INJECTION.6.1 allowlist, TEST_SUITE.2 OpenSSF position, dated-evidence facts, LINT.2 CI rule, PUBLISH.1 SLSA fact, STRICT unsoundness fact). Header row count updated (601).
- `build/distill/skeleton.md`: epistemic cells (F01 to F06, F08, F10, F11, F13, and the by-script flags), two intents (LAYER.1, SECRETS.2, THREATS.1, DOM.6.1: four in all), judge records (INJECTION.2, SECRETS.2, ERRORS.2, LAYER.1, UPDATE.3, FRAMEWORK_SHORTLIST wording, UPDATE.1 sentence; new record for LINT.2), ledger-rows column regenerated, a stage 7 line in the conventions.
- `build/distill/decisions_for_review.md`: new section I9 (the fixes) and a status line before the framework gates.
- `build/research/{06_runsec,08_quality,13_srvsec}/result.md`: quote corrections only: RUNSEC-C37 ("about half a minute" in claim mechanism and quote), RUNSEC-C35 (claim states the entire-value rule; the `$` trailing-newline statement marked inferred, not on the cited page; certainty "grounded for the entire-value rule; inferred for the $ statement"), SRVSEC-C27 (full operator sentence, digest flagged), SRVSEC-C07 (SRC-078 cited for the principle only), QUALITY-C35 (14 of 19). `check_claims.py`: errors 0.
- `build/assemble/`: new `apply_review_fixes.py`, `apply_review_fixes_2.py` (one-time edits with assertions; they stop on a second run), `apply_flags.py` (F05 and F17, idempotent), `epistemic_counts.py` with `epistemic_counts_before.json` and `epistemic_counts_after.json`, `bookkeeping_log.md`; changed `build_batches.py` (SHOULD pass-through, a problem raised for any "MUST hold:", design-note scrub of row ids, gap ids, merge notes and slot labels, no row lists or integration notes in notes) and `check_complete.py` (SHOULD allowed, scrub-aware rejected-belief check).
- `intent_graphs/`: both graphs rebuilt; `README.md` has new certainty counts and rule, a "Not covered" section (F07), the row count, and the build scripts.
- Rebuild order used: `apply_review_fixes.py`, `apply_review_fixes_2.py`, `apply_flags.py`, then `build_batches.py`, `build_graphs.sh`, `check_complete.py`, `check_ledger.py`, `ig-tool validate -m`.

### Per-finding detail and judgment calls

- F01: Node's own claim (RUNSEC-C23) is the unsanitized form; RUNSEC-C24 cites SRC-136 §Parameterization, so the stronger form has an OWASP principle behind it, yet no claim states "sanitized or not"; so it is flagged inferred.
- F03: the gates still have no admitted source; the fix makes them visible rules and marks the node risky. The platform-first default is carried by claim-less rows (no claim states it).
- F04: Playwright `browser_navigate` gave no response and was aborted by the tool timeout; WebFetch returned "section not included" for both nodejs.org/api/crypto.html and the raw markdown; a curl download was refused by the permission system. Not confirmed, so the flag stays. A reader with a working browser should read the `crypto.timingSafeEqual(a, b)` entry and drop the flag.
- F05: rule of `apply_flags.py`. An issue is added only when the node's existing `unvalidated:` text does not already say it, so some nodes keep a single, older issue. The "tool-extracted" suffix noted in the review (62 nodes) was left: it is accurate and not part of the decision.
- F06: SURFACE.1 to .3, .5, FORMAT.4, PACKAGE.4, LOADING.6, DIRECTION.2, OBJECTS.4, EVOLUTION.5, ESCAPE.6, MODEL.5, NAMING.2, philosophy TEST_SUITE.3 and TEST_STABILITY.3.
- F09/F21 limit: inline caveats such as "(inferred)" and "holder position of Google TS" remain in a few constraints; they are attribution, not build bookkeeping. 28 claim-less folklore rows still appear as "Rejected beliefs" lines.
- F12: the added fact row states the OpenSSF position's winning condition as "a project that adopts those criteria", my wording (inferred).
- F13: the incident list (event-stream 2018 and others) stays in the THREATS.1 constraint as evidence; the weight against code flaws is flagged unmeasured.
- F16: the dated Node LTS line and Angular table are rows in UPDATE.2 notes; "dated" is said in the row, the reading date is not recorded (not known to me).
- F18: only the four quotes of the review's L3 were changed; the corrected wording of RUNSEC-C37 was read through the fetch tool's digest of the Node blog page; the SRVSEC-C27 ellipsis is the review digest's, flagged. TYPES-C13 and C14 (tsconfig digest) were not touched. SRC-341 lists one chapter URL for five chapters: left as is in `build/audit/source_register.md`, recorded here.
- F19: the five named nodes only. Other philosophy rows still mention TypeScript or npm where the principle itself is language-bound; not checked beyond the five.
- Not done, open: no independent review of the rewritten rules (the global rule sends review to a separate Opus agent); the seven "Not covered" security classes; the F04 re-read; F16 beyond the named nodes.
