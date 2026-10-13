# Result: branch DEPENDENCIES (step 5b, purpose: trust)

## L1 headline

The DEPENDENCIES branch is consolidated into 23 js-philosophy and 28 pig-js-defaults nodes that treat every dependency as fully trusted code, fix the tree by a committed lockfile installed frozen, block install scripts by default, and cut the framework choice to the platform plus htmx, Lit, Angular and React; certainty: grounded for the rules and the folklore rejections (single T1 or T2 sources, many restricted), inferred for the framework gates, which are the build's judgment, open for three undecided nodes and several framework evidence gaps.

Pinned:
- Claims in: 84; ledger rows out: 77 (84 claims placed exactly once, 7 rows merge 14 claims, 0 dropped, 0 duplicated). Roles: decision 31, fact 35, rejected 9, acceptable-when 1, deferred 1. Graphs: js-philosophy 31 rows, pig-js-defaults 46 rows.
- Nodes: js-philosophy 23 (L1 1, L2 6, L3 16); pig-js-defaults 28 (L1 1, L2 6, L3 19, L4 2); judge records 15.
- Decisions for review: 9 entries D1 to D9 in `decisions.md`; the weighty ones are the framework short list (D1), pinning (D2, contested), cooldown (D3, effect open), install scripts (D4), signed-only components (D5), htmx major (D6).
- Framework short list: the platform with Web Components and no framework (default), htmx, Lit, Angular, React, unranked among the four frameworks; Vue, Svelte and Solid left off for missing trust evidence, with the condition to reopen each.
- Undecided nodes: 3 (`PIG-JS.DEPENDENCIES.UPDATE.1.1` cooldown length, `UPDATE.3.1` audit failing severity, `PUBLISH.4` target SLSA level), each `undecided | missing: no admitted source`.
- Restriction demotions: 5 claims demoted to fact (SUPPLY-C42, SUPPLY-C16, SUPPLY-C20, FW-C07, FW-C13), SRC-154's range position demoted to acceptable-when inside SUPPLY-C06, framework type-configuration detail (FW-C36 to FW-C40) not adopted as rules; 3 restricted uses checked and kept (SUPPLY-C21, SUPPLY-C35 with QUALITY-C44, SUPPLY-C09 scoped to npm before v12).

## L2 claims

- Every dependency, direct or transitive, development or runtime, is trusted code with full privileges and no in-process boundary contains it; two beliefs refuted on this node (sandboxed dependencies, the devDependencies split) become rejected rows. Grounded (T1 Node documents, one T2 study per refuted belief).
- Compromise comes by takeover of maintainership or accounts, and package confusion has 13 mechanisms, not only typos; controls target those routes. Grounded; the 107-vector taxonomy behind layered controls is single T2 and inferred.
- Signals state what they checked: provenance and registry signatures are not safety verdicts, audit findings are triage, SLSA levels are graded; four refuted beliefs are rejected rows. Grounded, mostly single-source.
- Reproducibility: commit the lockfile, install with `npm ci` frozen, never rely on exact pins alone, lockfile semantics differ across managers. Grounded, consensus.
- Pinning is contested and decided: lockfile fixes the tree, direct dependencies of applications are exact, ranges acceptable for published libraries; the library scope is inferred and the collective-pinning warning (SRC-287) stays open. Grounded for the core, inferred for the library scope.
- Install scripts are blocked by default in npm 12 and pnpm 10 and later; approve per package at an exact version; global `--ignore-scripts` is acceptable only on managers that run scripts by default. Grounded.
- Release-age cooldown: enable the tool default, exempt security updates; effectiveness rests on one T1 assertion and vendor figures; the claim's consensus label is relabelled single-source. Grounded for tool facts, open for effect and duration.
- Publishing: trusted publishing over long-lived tokens, review the tarball with a dry run, ship JavaScript; token-policy dates and the provenance recipe are facts, the target SLSA level is open. Grounded.
- Framework evidence is thin and uneven: support window stated for React, Angular, Lit, htmx; governance for React, Vue, Solid, Lit; type support for all but htmx; usage only for React and platform features. Grounded for each fact, open for the listed gaps.
- Framework short list is a build judgment under the max rule over those facts: gate A (stated security-fix window) mandatory, plus one of documented security model or stated governance. Inferred; each exclusion carries its reopen condition.
- Boundary: FW-C44 deferred to web-architecture; FW-C07, FW-C13, FW-C45 kept as facts with planned boundary links; security-model facts of the matrix are owned by DEFENSE and are cited, not placed. Grounded.
- Folklore: 8 refuted beliefs of the branch are rejected rows (SUPPLY-C18, C19, C22, C23, C25, C40, RUNSEC-C41, STRUCT-C67); the confirmed ones (lockfile and `npm ci`, install scripts) are decisions. Grounded.

## L3 full

### What was read

- `build/distill/brief_distill.md` (Shared, Step 5b), `build/plan.md`, `build/distill/target_hierarchy.md`, `build/distill/branches/DEPENDENCIES/claims.md` (all 84 rows), `build/research/10_frameworks/result.md` (all, matrix in L3 full), the DEPENDENCIES-relevant parts of `build/research/12_dissent/result.md` (topics 12, 13, 16, tension X5, folklore table) and `build/research/11_coverage/result.md` (overlaps O09, O10, O11 to O13, boundary list), the register rows of every source the claims cite, the IntentGraph primers 00, 01 and 03A, and the uids of `python_kb_philosophy.yaml`.
- Not read: the cited source pages themselves (claims are taken as extracted); the security-model claims of slot 10 (FW-C01 to FW-C06, C08 to C12, C14, C18 to C20, C48), which are routed to DEFENSE and are cited from the matrix only.

### Counts

| item | value |
|---|---|
| claims routed in | 84 (SUPPLY 42, FW 33, QUALITY 3, TYPES 2, RUNSEC 2, STRUCT 1, SRVSEC 1) |
| ledger rows out | 77, claims placed 84, merged rows 7, dropped 0 |
| rows by role | decision 31, fact 35, rejected 9, acceptable-when 1, deferred 1 |
| nodes js-philosophy | 23: L1 1, L2 6, L3 16 |
| nodes pig-js-defaults | 28: L1 1, L2 6, L3 19, L4 2 |
| intentlinks | js-philosophy 10, pig-js-defaults 8, inter to js-philosophy 16, inter to python-kb-philosophy 4, proposed to other branches 11, planned boundary links to web-architecture 3 |
| judge records | 15 (one per defaults node holding a decision) |

### Method

- Graph assignment: language-swap test per statement. Rules naming npm, pnpm, a Node release, a framework or a tool setting went to `pig-js-defaults`; the rest to `js-philosophy`, where shared principles also link to `python-kb-philosophy` (DEFENSIVE, INTENTIONALITY, REPRODUCIBILITY) instead of copying.
- Max rule: for trust, the most demanding practice an admitted source supports: frozen lockfile install, exact direct pins, default-blocked scripts with an exact-version allowlist, trusted publishing, signed-only components, platform first. Where a more demanding practice had no source it is noted, not invented (Active-only LTS, a cooldown duration, an audit threshold, a SLSA target).
- Epistemic rule: one T1 ground or two independent T2 grounds is `known`; a single T2 ground is `known | unvalidated: single T2 source`. Demoted or restricted uses are listed below.
- Merges (overlap clusters of 11_coverage): O10 `npm ci` merged (SUPPLY-C04 with QUALITY-C42); O09 cooldown split by graph (principle facts SUPPLY-C13, QUALITY-C46 in js-philosophy; tool rule SUPPLY-C12 with SUPPLY-C14 in defaults); O13 trust of dependencies kept as three rows on two nodes (SUPPLY-C01, SUPPLY-C02, RUNSEC-C41, the last as the refuted belief). Scorecard (SUPPLY-C35 with QUALITY-C44) and publish-contents (SUPPLY-C38 with SRVSEC-C62) merged.
- Mild tension STRUCT-C67 against SUPPLY-C06 (minor releases break against pin or range): both sit on `DEPENDENCIES.CHANGE.2`, the first as a rejected belief.
- Labelling fix: SUPPLY-C12 is labelled consensus in the claim table; 12_dissent X5 shows its effect rests on one T1 assertion and vendor figures, so the row says single-source.

### Folklore rows (rejected)

| belief | claim | node |
|---|---|---|
| dependencies are sandboxed inside the Node process | RUNSEC-C41 | DEPENDENCIES.TRUST.2 |
| devDependencies never reach production | SUPPLY-C23 | DEPENDENCIES.TRUST.1 |
| typosquatting is just typing mistakes | SUPPLY-C25 | DEPENDENCIES.THREATS.2 |
| a package with provenance is safe | SUPPLY-C18 | DEPENDENCIES.EVIDENCE.1 |
| a signed package is a trustworthy package | SUPPLY-C19 | DEPENDENCIES.EVIDENCE.1 |
| every npm audit finding is an exploitable risk | SUPPLY-C22 | DEPENDENCIES.EVIDENCE.2 |
| lockfile semantics are the same across package managers | SUPPLY-C40 | DEPENDENCIES.CHANGE.1 |
| a minor or patch release of an npm dependency is non-breaking | STRUCT-C67 | DEPENDENCIES.CHANGE.2 |

A ninth rejected row, FW-C49 (rank candidates by usage), is a position and not a folklore belief.

### Restriction demotions and checks

| claim | register restriction | treatment |
|---|---|---|
| SUPPLY-C42 | SRC-158: facts about pnpm behaviour, the page's framing in favour of pnpm excluded | decision demoted to fact; no recommendation to rely on trustPolicy |
| SUPPLY-C16 | SRC-141: facts about token policy and dates, publisher side | decision demoted to fact; the advice rests on SUPPLY-C15 (OWASP, SRC-155) |
| SUPPLY-C20 | SRC-147, SRC-160: facts, no preference for npm | practice demoted to fact (recipe) |
| FW-C07, FW-C13 | SRC-209, SRC-225: disclosure and advisory facts; update policy is deployment | update advice dropped; kept as facts with boundary note; the advisory count is no comparison metric |
| SUPPLY-C06, ranges | SRC-154: archived 2023 position, items not superseded | ranges recorded as acceptable-when inside the decision, not as evidence |
| FW-C36 to FW-C40 | framework documentation grounds facts about that framework only; Q3 keeps framework coding rules out | kept as type-support facts; compiler options are not adopted as rules |
| QUALITY-C46 | SRC-163: body's position, the effectiveness claim needs its origin | recorded as position only, effectiveness not used |
| SUPPLY-C13 | SRC-319: vendor's own figures, single-source | used only to state that the effect is unmeasured |
| SUPPLY-C21 | SRC-149: behaviour, not audit accuracy | checked, kept as a decision; no accuracy or tool-preference claim made |
| SUPPLY-C35, QUALITY-C44 | SRC-161: a check grounds 'Scorecard rewards X', never that X is effective | checked, kept; the decision restates the source's stated limit only |
| SUPPLY-C09 | SRC-078, SRC-155: ignore-scripts advice applies to npm before v12 | kept as acceptable-when with that condition |
| SUPPLY-C41 | SRC-295: recommended actions are CISA's position | kept, attributed to CISA, single T2 |

### Framework short list (decision D1 in full)

Source of the facts: the comparison matrix in `build/research/10_frameworks/result.md` (L3 full). Security-model cells belong to DEFENSE and are cited by claim id.

| candidate | A support window | B security model | C governance | usage | type support | on the list |
|---|---|---|---|---|---|---|
| platform, no framework | not applicable (standards) | not applicable | not applicable | custom elements 7.8 percent (FW-C43) | not applicable | yes, default |
| htmx | yes: 4.x, 2.x, 1.9.x (FW-C21) | yes (FW-C18 to C20) | no source (FW-C35) | no source | no source (FW-C41) | yes |
| Lit | yes: latest two majors (FW-C28) | no default-escaping source (FW-C16) | yes: OpenJS Incubation (FW-C34) | platform features only | yes (FW-C40) | yes |
| Angular | yes: 24 months (FW-C23) | yes, strongest (FW-C01 to C04) | no source (FW-C35) | no source | yes (FW-C24) | yes |
| React | yes: security backports to all affected majors (FW-C25) | yes (FW-C02, C05 to C07) | yes, provisional (FW-C31) | 10 percent (FW-C42) | external types (FW-C36) | yes |
| Vue | no: no fixed cycle, no EOL (FW-C26) | yes (FW-C08 to C11) | partial (FW-C32) | no source | yes (FW-C37) | no, runner-up |
| Svelte | no (FW-C27) | yes (FW-C12 to C14) | no source (FW-C35) | no source | type-only default (FW-C38) | no |
| Solid | no (FW-C29, C30) | no (FW-C15, C16) | partial (FW-C33) | no source | yes (FW-C39) | no |

Difference from the slot 10 proposal (React, Angular, Vue, Lit, htmx, no framework as comparator): Vue is dropped for gate A and the platform becomes a candidate, the default; certainty inferred.

### Proposed links and boundaries

- Proposed to other branches (11): TRUST.1, TRUST.2, ADMISSION.4, PUBLISH.2 and the shortlist to DEFENSE; INSTALL.1, UPDATE.3, SCREEN.1 to VERIFICATION; UPDATE.2 to RUNTIME; PUBLISH.3 and the shortlist to CONTRACTS. Detail in `skeleton.md`.
- Boundary web-architecture (planned, not created): shortlist (rendering strategy), FRAMEWORK_EVIDENCE.4 (FW-C44 deferred, FW-C45), FRAMEWORK_EVIDENCE.5 (FW-C07, FW-C13).
- Claims tagged `boundary: 07_supply` that arrived from other slots (TYPES-C07, STRUCT-C67, RUNSEC-C21, RUNSEC-C41, QUALITY-C42, SRVSEC-C62) are placed here once; RUNSEC and RUNTIME siblings should link, not copy.
- Undecided nodes and what would settle each: `decisions.md`, section Undecided nodes.

### Checks run

- Own check in the generator: the 84 claim ids of `claims.md` are each placed exactly once (0 missing, 0 duplicated, 0 unknown) and every ledger row's node exists in `skeleton.md`. `check_ledger.py` itself needs the integrated `claims_ledger.md` and was not run here.
- No absolute or home paths and no private names appear in the written files.
