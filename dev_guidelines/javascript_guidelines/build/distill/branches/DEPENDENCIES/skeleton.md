# Skeleton: branch DEPENDENCIES (purpose: trust)

Subtree of the branch in both graphs, breadth-first, L1 node first. Philosophy uids `DEPENDENCIES.*`, defaults uids `PIG-JS.DEPENDENCIES.*`. Graph assignment follows the language-swap test statement by statement: a rule that still holds for another language and its package manager sits in `js-philosophy`; a rule that names npm, pnpm, a Node release, a framework or a tool setting sits in `pig-js-defaults`. Ledger rows of each node are in `ledger.md`; `-` means the node rolls up its children or is undecided.

## js-philosophy: nodes

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| DEPENDENCIES | Dependencies | Third-party code runs with the application's full privileges, so each dependency is a trust decision: few in number, vetted before adoption, installed reproducibly, changed deliberately, and judged by evidence whose limits are known. | known | - |
| DEPENDENCIES.TRUST | Dependencies are trusted code | Whatever enters the dependency graph acts with the application's authority and nothing inside the process contains it, so trust is granted by the act of adding. | known | - |
| DEPENDENCIES.THREATS | How trust is lost | Controls aim at the routes by which trusted code turns hostile: takeover of the people and accounts behind a package, and confusion about which package is meant. | known | - |
| DEPENDENCIES.ADMISSION | Admission | A package enters only when its need, its maintenance, its identity and its documentation have each been checked. | known | - |
| DEPENDENCIES.EVIDENCE | Evidence and its limits | Signals about a package (provenance, signatures, assurance levels, audit findings) are read for what they establish and no further; none is a verdict of safety. | known | - |
| DEPENDENCIES.CHANGE | Controlled change | The tree that was reviewed is the tree that runs, and it changes only by a deliberate, reviewable act. | known | conflict: see CHANGE.2 | - |
| DEPENDENCIES.PUBLISH | Publishing | A project that publishes a package is itself a dependency of others, and its publishing accounts are the takeover route into them. | known | DEPENDENCIES-031 |
| DEPENDENCIES.TRUST.1 | Every dependency is trusted code | Direct or transitive, development or runtime, every package acts with the application's privileges and is vetted as such. | known | unvalidated: dev-versus-runtime figures rest on a single T2 source | DEPENDENCIES-001, DEPENDENCIES-002, DEPENDENCIES-003 |
| DEPENDENCIES.TRUST.2 | No containment inside the process | The runtime offers no privilege boundary between application code and its dependencies, so no design relies on one. | known | DEPENDENCIES-004, DEPENDENCIES-005 |
| DEPENDENCIES.TRUST.3 | Layered controls | No single control is relied on; controls stack across the routes of attack. | known | unvalidated: single T2 source, claim is inferred from a taxonomy | DEPENDENCIES-006 |
| DEPENDENCIES.THREATS.1 | Takeover of maintainership | The recurring compromise is control of a maintainer account or of maintainership, so who maintains a package matters more than flaws in its code. | known | DEPENDENCIES-007, DEPENDENCIES-008 |
| DEPENDENCIES.THREATS.2 | Confusion is many mechanisms | Package confusion is a family of mechanisms, many semantic, so defences address the namespace and not only spelling. | known | unvalidated: single T2 source | DEPENDENCIES-009 |
| DEPENDENCIES.ADMISSION.1 | Existing components first | A dependency must earn its trust cost against what the platform and the current code already provide. | known | DEPENDENCIES-010 |
| DEPENDENCIES.ADMISSION.2 | Maintenance as a signal | Adoption weighs how many people maintain a package, how recently, and what it runs at install. | known | DEPENDENCIES-011, DEPENDENCIES-012 |
| DEPENDENCIES.ADMISSION.3 | Identity of the package | Before adoption, the name is confirmed to be the package intended and the package to be authentic. | known | DEPENDENCIES-013 |
| DEPENDENCIES.ADMISSION.4 | Documentation examples are untrusted | Example code shipped with a package's documentation is untrusted until reviewed. | known | DEPENDENCIES-014 |
| DEPENDENCIES.EVIDENCE.1 | Provenance and signatures | Provenance and signatures state origin and integrity; assurance is graded and consumed as such, never read as safety. | known | DEPENDENCIES-015, DEPENDENCIES-016, DEPENDENCIES-017, DEPENDENCIES-018, DEPENDENCIES-019 |
| DEPENDENCIES.EVIDENCE.2 | Audit findings | Vulnerability findings are triage input; reachability, not count, measures risk. | known | DEPENDENCIES-020 |
| DEPENDENCIES.CHANGE.1 | Reproducible tree | Every install resolves the same tree because the lockfile, not the manifest, fixes it; lockfile semantics are verified per manager, not assumed. | known | DEPENDENCIES-021, DEPENDENCIES-022, DEPENDENCIES-023 |
| DEPENDENCIES.CHANGE.2 | Pin policy | Which versions may enter is fixed deliberately: the lockfile fixes the tree, direct dependencies of an application are exact, and release type is no guarantee of compatibility. | known | conflict: ranges only, OpenSSF npm guide v1.1 (SRC-154, archived 2023); collective ecosystem pinning, SRC-287 | unclear: library scope is inferred | DEPENDENCIES-024, DEPENDENCIES-025 |
| DEPENDENCIES.CHANGE.3 | Lockfile review | A lockfile change is a code change and is reviewed like one. | known | unvalidated: claim is inferred from a listed attack vector | DEPENDENCIES-026 |
| DEPENDENCIES.CHANGE.4 | Updates | Updates flow through an automated mechanism that separates security from feature updates; how long to wait before adopting a fresh release is a tradeoff whose benefit is unmeasured. | known | gap: cooldown effectiveness unmeasured, one T1 assertion and vendor figures | DEPENDENCIES-027, DEPENDENCIES-028, DEPENDENCIES-029 |
| DEPENDENCIES.CHANGE.5 | Incident response | After a worm-style compromise the lockfile, the credentials and the pinned versions are the three things re-established first. | known | unvalidated: single T2 source, recorded as CISA's position | DEPENDENCIES-030 |

## pig-js-defaults: nodes

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.DEPENDENCIES | Dependencies (JavaScript defaults) | Concrete npm-era rules that keep third-party code trusted: deterministic installs, blocked install scripts, deliberate updates, screened evidence, safe publishing, and a framework choice made on trust evidence. | known | - |
| PIG-JS.DEPENDENCIES.INSTALL | Install | What is fetched and what runs at install is deterministic and reviewed. | known | - |
| PIG-JS.DEPENDENCIES.UPDATE | Update | Versions move on a schedule the project controls, on supported runtimes and toolchains, with findings triaged. | known | gap: cooldown length and audit threshold have no admitted source | - |
| PIG-JS.DEPENDENCIES.SCREEN | Screening evidence | Tool outputs about a package are read within the limits their authors state. | known | - |
| PIG-JS.DEPENDENCIES.PUBLISH | Publish | A published package leaves with short-lived credentials, reviewed contents and runnable JavaScript. | known | gap: target assurance level undecided | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE | Framework evidence | The facts that bear on trusting a front-end framework as the largest dependency, taken from each framework's own documentation and from measured usage, with every gap shown. | known | gap: governance, usage, support window, type support and default escaping missing for several candidates | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | Framework short list | The candidates a team may choose among, cut by trust evidence under the max rule: the platform first, then four frameworks. | known | unvalidated: build judgment over single-source facts; gates are not stated by any admitted source | conflict: keep Vue and drop the platform baseline, slot 10 proposal (inferred) | - |
| PIG-JS.DEPENDENCIES.INSTALL.1 | Frozen install | CI and production install exactly the committed lockfile and fail on any mismatch. | known | DEPENDENCIES-032 |
| PIG-JS.DEPENDENCIES.INSTALL.2 | Install scripts blocked | Code that runs at install time is approved package by package, never by default. | known | DEPENDENCIES-033, DEPENDENCIES-034 |
| PIG-JS.DEPENDENCIES.INSTALL.3 | Non-registry sources | Dependencies from git or tarball URLs bypass registry controls and enter only as named exceptions. | known | unvalidated: claim is inferred from npm 12 defaults | DEPENDENCIES-035 |
| PIG-JS.DEPENDENCIES.INSTALL.4 | Owned scope for internal packages | Internal package names cannot be shadowed by a public package. | known | DEPENDENCIES-036 |
| PIG-JS.DEPENDENCIES.UPDATE.1 | Release-age cooldown | A freshly published version is not installed at once, while security fixes are never delayed. | known | gap: effectiveness unmeasured; claim relabelled single-source | DEPENDENCIES-037 |
| PIG-JS.DEPENDENCIES.UPDATE.2 | Supported runtime and toolchain | Production runs on versions that still receive security fixes, and the toolchain is pinned to what the framework supports. | known | DEPENDENCIES-038, DEPENDENCIES-039 |
| PIG-JS.DEPENDENCIES.UPDATE.3 | Audit in CI | Known-vulnerability data is checked against the committed lockfile and read as triage. | known | DEPENDENCIES-040 |
| PIG-JS.DEPENDENCIES.SCREEN.1 | Scorecard as per-check evidence | Scorecard results inform adoption per check and never stand for safety. | known | unvalidated: single T1 restricted source, limits restated | DEPENDENCIES-041 |
| PIG-JS.DEPENDENCIES.SCREEN.2 | Publisher-trust downgrade check | A package manager may compare a version's publishing trust with earlier releases; availability is recorded, reliance is not recommended. | known | unvalidated: single T1 restricted source, tool fact only | DEPENDENCIES-042 |
| PIG-JS.DEPENDENCIES.PUBLISH.1 | CI publishing credentials | Publishing from CI uses short-lived, workflow-bound credentials, and provenance follows from it. | known | DEPENDENCIES-043, DEPENDENCIES-044, DEPENDENCIES-045 |
| PIG-JS.DEPENDENCIES.PUBLISH.2 | Tarball contents | What leaves in the tarball is reviewed before every publish, and secrets never enter it. | known | DEPENDENCIES-046 |
| PIG-JS.DEPENDENCIES.PUBLISH.3 | Ship JavaScript | Consumers receive code their runtime can load. | known | unvalidated: claim is inferred from one runtime limitation | DEPENDENCIES-047 |
| PIG-JS.DEPENDENCIES.PUBLISH.4 | Target assurance level | Which SLSA Build level a published package aims at. | undecided | missing: no admitted source recommends a target level | - |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | Support window | Whether a framework states which versions receive security fixes, and until when. | known | conflict: main htmx docs site documents 2.x as current (SRC-213) | unvalidated: htmx 4.0.0 release date open | gap: Svelte, Solid and Vue state no support window | DEPENDENCIES-048, DEPENDENCIES-049, DEPENDENCIES-050, DEPENDENCIES-051, DEPENDENCIES-052, DEPENDENCIES-053, DEPENDENCIES-054 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | Governance | Who owns and steers a framework, as stated by the project. | known | gap: no source for Angular, Svelte, htmx | DEPENDENCIES-055, DEPENDENCIES-056, DEPENDENCIES-057, DEPENDENCIES-058, DEPENDENCIES-059 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.3 | Type support | How each framework relates to the type layer. | known | gap: htmx has no source | DEPENDENCIES-060, DEPENDENCIES-061, DEPENDENCIES-062, DEPENDENCIES-063, DEPENDENCIES-064, DEPENDENCIES-065 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | Measured usage | What measured usage can and cannot support. | known | gap: figures exist for React, jQuery and platform features only | DEPENDENCIES-066, DEPENDENCIES-067, DEPENDENCIES-068, DEPENDENCIES-069, DEPENDENCIES-070 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | Vulnerability record | Advisories and reporting channels as facts about response, not as a ranking. | known | gap: Solid and Angular advisories lack affected versions or policy | DEPENDENCIES-071, DEPENDENCIES-072, DEPENDENCIES-073, DEPENDENCIES-074, DEPENDENCIES-075 |
| PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 | Platform baseline | Framework-free components are the default and the first candidate. | known | DEPENDENCIES-076, DEPENDENCIES-077 |
| PIG-JS.DEPENDENCIES.UPDATE.1.1 | Cooldown length beyond tool defaults | How long to wait when the tool default is not what the project wants. | undecided | missing: no admitted source gives a measured duration | - |
| PIG-JS.DEPENDENCIES.UPDATE.3.1 | Failing severity of the audit gate | Which severity fails the build. | undecided | missing: no admitted source names a level | - |

## Intentlinks inside the branch

### js-philosophy (intra)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | DEPENDENCIES.TRUST.1 | DEPENDENCIES.ADMISSION.1 | requires | Because every dependency is trusted code, each addition must first earn its trust cost. |
| 2 | DEPENDENCIES.TRUST.2 | DEPENDENCIES.TRUST.3 | requires | With no containment inside the process, protection can only come from stacked controls. |
| 3 | DEPENDENCIES.THREATS.1 | DEPENDENCIES.ADMISSION.2 | requires | The takeover route makes maintainer count and recency a vetting criterion. |
| 4 | DEPENDENCIES.THREATS.2 | DEPENDENCIES.ADMISSION.3 | requires | Confusion mechanisms are what the identity check has to cover. |
| 5 | DEPENDENCIES.EVIDENCE.2 | DEPENDENCIES.CHANGE.4 | dataflow | Triaged findings feed the update mechanism, which keeps security updates separate. |
| 6 | DEPENDENCIES.CHANGE.1 | DEPENDENCIES.CHANGE.2 | requires | A pin policy means something only once the lockfile fixes the tree. |
| 7 | DEPENDENCIES.CHANGE.3 | DEPENDENCIES.THREATS.1 | dataflow | Reviewing lockfile diffs surfaces poisoned resolutions, one of the routes of compromise. |
| 8 | DEPENDENCIES.CHANGE.5 | DEPENDENCIES.CHANGE.1 | requires | Pinning to pre-incident versions presupposes a tree fixed by the lockfile. |
| 9 | DEPENDENCIES.PUBLISH | DEPENDENCIES.THREATS.1 | requires | Publishing accounts are the takeover route that has to be hardened. |
| 10 | DEPENDENCIES.EVIDENCE.1 | DEPENDENCIES.ADMISSION.3 | dataflow | Origin evidence supports the authenticity check without replacing it. |

### pig-js-defaults (intra)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.DEPENDENCIES.INSTALL.1 | PIG-JS.DEPENDENCIES.INSTALL.2 | requires | Version-pinned script approvals bind only under a frozen install. |
| 2 | PIG-JS.DEPENDENCIES.UPDATE.3 | PIG-JS.DEPENDENCIES.UPDATE.1 | dataflow | Audit findings identify the security updates that bypass the cooldown. |
| 3 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | PIG-JS.DEPENDENCIES.UPDATE.2 | dataflow | The chosen framework supplies the compatibility table the toolchain is pinned to. |
| 4 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Stated support windows are gate A of the short list. |
| 5 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Stated governance is gate C of the short list. |
| 6 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.3 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Type support is carried as a fact of each candidate, not a gate. |
| 7 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Usage figures bound what the list may claim: context only. |
| 8 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | dataflow | Advisories and reporting channels are facts about response, carried per candidate. |

### pig-js-defaults to js-philosophy (inter)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.DEPENDENCIES.INSTALL.1 | js-philosophy:DEPENDENCIES.CHANGE.1 | refines | The frozen install realizes the reproducible tree. |
| 2 | PIG-JS.DEPENDENCIES.INSTALL.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Blocking install scripts acts on the install-script risk signal. |
| 3 | PIG-JS.DEPENDENCIES.INSTALL.4 | js-philosophy:DEPENDENCIES.ADMISSION.3 | refines | An owned scope closes the namespace route that the identity check covers by hand. |
| 4 | PIG-JS.DEPENDENCIES.INSTALL.3 | js-philosophy:DEPENDENCIES.CHANGE.3 | refines | Git and tarball sources are what a lockfile review has to explain. |
| 5 | PIG-JS.DEPENDENCIES.UPDATE.1 | js-philosophy:DEPENDENCIES.CHANGE.4 | refines | The cooldown is the tool form of the update tradeoff. |
| 6 | PIG-JS.DEPENDENCIES.UPDATE.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Running only maintained versions applies maintenance as a signal. |
| 7 | PIG-JS.DEPENDENCIES.UPDATE.3 | js-philosophy:DEPENDENCIES.EVIDENCE.2 | refines | The audit gate is the tool form of triaging findings. |
| 8 | PIG-JS.DEPENDENCIES.SCREEN.1 | js-philosophy:DEPENDENCIES.EVIDENCE.1 | refines | Scorecard is read within its stated limits like any other signal. |
| 9 | PIG-JS.DEPENDENCIES.SCREEN.2 | js-philosophy:DEPENDENCIES.EVIDENCE.1 | refines | A trust-downgrade check is one more graded signal. |
| 10 | PIG-JS.DEPENDENCIES.PUBLISH.1 | js-philosophy:DEPENDENCIES.PUBLISH | refines | Short-lived CI credentials harden the publishing route. |
| 11 | PIG-JS.DEPENDENCIES.PUBLISH.2 | js-philosophy:DEPENDENCIES.PUBLISH | refines | Reviewing tarball contents keeps secrets out of what consumers receive. |
| 12 | PIG-JS.DEPENDENCIES.PUBLISH.3 | js-philosophy:DEPENDENCIES.PUBLISH | refines | Shipping runnable JavaScript is part of being a good dependency. |
| 13 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | js-philosophy:DEPENDENCIES.ADMISSION.1 | refines | The framework is the largest case of a dependency earning its trust cost. |
| 14 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 | js-philosophy:DEPENDENCIES.ADMISSION.1 | refines | The platform is the existing component that suffices first. |
| 15 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | A stated support window is the maintenance signal for a framework. |
| 16 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.2 | js-philosophy:DEPENDENCIES.ADMISSION.2 | refines | Stated governance is the maintainer-count signal for a framework. |

## Inter links to python-kb-philosophy

Targets are uids of `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | DEPENDENCIES.TRUST.1 | python-kb-philosophy:DEFENSIVE | refines | Assume failure and hostility: here the hostile party can be a dependency. |
| 2 | DEPENDENCIES.ADMISSION.1 | python-kb-philosophy:INTENTIONALITY | refines | Every artifact, a dependency included, exists for an articulated reason. |
| 3 | DEPENDENCIES.CHANGE.1 | python-kb-philosophy:REPRODUCIBILITY | refines | Same inputs, same tree: lockfiles and version pinning. |
| 4 | DEPENDENCIES.CHANGE.2 | python-kb-philosophy:REPRODUCIBILITY | refines | Version pinning is a reproducibility rule with a contested scope. |

## Proposed links to other branches

The integrator resolves the branch keyword to a uid.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | DEPENDENCIES.TRUST.1 | DEFENSE | requires | Injection sinks that dependencies carry (eval, exec) are the subject of DEFENSE. |
| 2 | DEPENDENCIES.TRUST.2 | DEFENSE | requires | The permission model is a seat belt for trusted code, not containment of hostile dependencies (topic 12 of 12_dissent). |
| 3 | DEPENDENCIES.ADMISSION.4 | DEFENSE | requires | README examples that reach DOM or injection sinks are reviewed under DEFENSE rules. |
| 4 | PIG-JS.DEPENDENCIES.INSTALL.1 | VERIFICATION | dataflow | The frozen install is the CI install step that VERIFICATION gates on. |
| 5 | PIG-JS.DEPENDENCIES.UPDATE.3 | VERIFICATION | dataflow | The audit gate runs in CI under VERIFICATION. |
| 6 | PIG-JS.DEPENDENCIES.SCREEN.1 | VERIFICATION | requires | Scorecard checks (tests before merge, review, branch protection) overlap CI gates. |
| 7 | PIG-JS.DEPENDENCIES.UPDATE.2 | RUNTIME | requires | Node LTS status is the runtime-lifecycle side of supported versions (boundary 09_runtime). |
| 8 | PIG-JS.DEPENDENCIES.PUBLISH.3 | CONTRACTS | requires | The type-layer decision determines what is compiled before publishing. |
| 9 | PIG-JS.DEPENDENCIES.PUBLISH.2 | DEFENSE | requires | Secrets in code and tarballs are owned by the secrets rules of DEFENSE. |
| 10 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | DEFENSE | requires | The built-in security model of each candidate (escape hatches, Trusted Types) is owned there; this node cites it from the slot 10 matrix. |
| 11 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | CONTRACTS | requires | The type-support criterion depends on the type-layer decision. |

## Planned boundary links to web-architecture

Planned, not created; the claims carry `boundary: web-architecture` in routing.

| # | from | boundary content |
|---|---|---|
| 1 | PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST | rendering strategy (SPA, server HTML, hypermedia) decides which candidate fits; owned by web-architecture |
| 2 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 | FW-C44 (usage by rendering strategy, deferred) and FW-C45 (CSP and SRI prevalence) |
| 3 | PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.5 | FW-C07 and FW-C13 (framework advisories, update policy of server rendering) |

## Judge records

One record per defaults node holding a decision. Positions come from the evidence (claim ids, source ids), forces name the purpose served and the cost, the decision is the max choice, rejected lists each other position with the condition under which it would win.

### PIG-JS.DEPENDENCIES.INSTALL.1 (Frozen install)

- Positions: (a) npm install resolving from the manifest (the common default); (b) npm ci or the manager's frozen-lockfile equivalent: SUPPLY-C04 (SRC-150, SRC-078, SRC-154, SRC-155, consensus), QUALITY-C42 (SRC-173, re-read from the v12 page).
- Forces: Trust wants the tree that was reviewed to be the tree installed; (a) costs convenience of silent lockfile refresh, (b) costs one explicit update step.
- Decision: (b) in CI and production, with a lockfile required; the lockfile is committed (DEPENDENCIES.CHANGE.1). Grounds: four T1 sources agree; the 12_dissent folklore audit confirms 'commit the lockfile and install with npm ci'.
- Rejected: (a): would win only in the deliberate update step that regenerates the lockfile, never in CI or production.

### PIG-JS.DEPENDENCIES.INSTALL.2 (Install scripts blocked)

- Positions: (a) block install scripts by default and approve reviewed packages through an exact-version allowlist: SUPPLY-C08 (SRC-153, SRC-151), SUPPLY-C10 (SRC-153, SRC-158, consensus); (b) disable scripts globally with --ignore-scripts and allowlist the few that need them: SUPPLY-C09 (SRC-078, SRC-155, SRC-288, consensus); (c) run all scripts, the pre-v12 npm default.
- Forces: Trust wants no code to run before review; the cost is a maintained allowlist and packages that legitimately build at install.
- Decision: (a): per-package approval pinned to the exact version, guard never disabled globally. Grounds: two independent bodies (npm docs, pnpm docs) and OWASP and Node guidance on the same risk; install scripts are a confirmed supply-chain risk (12_dissent).
- Rejected: (b): acceptable when the manager still runs scripts by default (npm before v12, SRC-078 restriction), with an allowlist. (c): rejected, no admitted source supports it; wins under no stated condition. Disabling the guard globally on a default-block manager: rejected by SUPPLY-C10.

### PIG-JS.DEPENDENCIES.INSTALL.3 (Non-registry sources)

- Positions: (a) allow git and tarball dependencies freely; (b) allow them for the root project only; (c) refuse them: SUPPLY-C11 (SRC-151, SRC-152) states the npm 12 default refusal and 'root rather than all'.
- Forces: Trust wants every dependency to pass the registry's controls; the cost is projects that really need a fork or a pre-release.
- Decision: (b) when needed, over the refusal default of npm 12 (the most demanding the claim supports is the default itself, taken as is). Single-source and inferred.
- Rejected: (a) 'all': rejected by the claim; would win under no condition grounded in the register.

### PIG-JS.DEPENDENCIES.INSTALL.4 (Owned scope for internal packages)

- Positions: (a) internal packages under unscoped names; (b) internal packages under an owned scope routed to the private registry in .npmrc: SUPPLY-C26 (SRC-155 OWASP, SRC-143 scope ownership, SRC-145 CVE-2021-24105 for the confusion class).
- Forces: A public package of the same name must not win resolution; the cost is a scope to own and one registry mapping.
- Decision: (b). Grounds: OWASP mitigation plus facts on scope ownership and the CVE class; SRC-143 alone states scope facts only and does not address confusion, so the normative step rests on SRC-155.
- Rejected: (a): wins under no grounded condition.

### PIG-JS.DEPENDENCIES.UPDATE.1 (Release-age cooldown)

- Positions: (a) no cooldown, adopt versions at once; (b) tool-default cooldown: SUPPLY-C12 (T1 assertion SRC-078 §Mitigations; tool facts SRC-152, SRC-158, SRC-146) with security updates exempt (SUPPLY-C14); (c) a three-day cooldown as an OpenSSF position (QUALITY-C46, origin missing); (d) a longer custom duration: no source.
- Forces: Exposure window to a freshly hijacked release against lag in receiving fixes; effect unmeasured (SUPPLY-C13: one T1 assertion plus vendor figures from SRC-319).
- Decision: (b), with security updates outside the cooldown. The max rule picks the more demanding delay; the length stays at the tool default because (d) has no source (undecided child UPDATE.1.1). SUPPLY-C12's 'consensus' label is relabelled single-source (12_dissent X5). Grounds: one T1 assertion.
- Rejected: (a): wins for a version that fixes an exploited vulnerability, which is the security-update exemption. (c): not rejected as the body's position, but its effectiveness claim is not used as evidence until the origin is found. (d): undecided.

### PIG-JS.DEPENDENCIES.UPDATE.2 (Supported runtime and toolchain)

- Positions: Runtime: (a) any Node release; (b) Active or Maintenance LTS only: TYPES-C45 (SRC-037); (c) Active LTS only (more demanding, no source). Toolchain: (d) float TypeScript and Node; (e) pin to the framework's compatibility table: FW-C24 (SRC-207, Angular 22) and FW-C26 (SRC-231, Vue typings may change in minors).
- Forces: Security fixes reach only supported lines; frameworks couple to narrow TypeScript ranges; the cost is staying inside the table.
- Decision: (b) and (e). (c) is more demanding but no admitted source says Maintenance LTS is insufficient. Two framework sources, independent, support (e).
- Rejected: (a) Current in production: wins under no grounded condition (SRC-037 labels Current non-LTS). (c): would win if a T1 source states that Maintenance LTS stops receiving fixes that matter. (d): wins only for a framework that publishes no compatibility table (none in the register).

### PIG-JS.DEPENDENCIES.UPDATE.3 (Audit in CI)

- Positions: (a) run npm audit against the committed lockfile with audit-level: SUPPLY-C21 (SRC-149, SRC-152); (b) treat every finding as exploitable; (c) ignore audit as noise; (d) audit runtime dependencies only on the strength of the dependencies split.
- Forces: Known-vulnerability data is cheap and noisy: 68.28 percent of package-level impacts are unreachable (SUPPLY-C22, SRC-285, SRC-286).
- Decision: (a), findings read as triage input (DEPENDENCIES.EVIDENCE.2). Restriction check: SRC-149 grounds the behaviour (lockfile dependence, threshold), not audit accuracy, and no preference for npm over another tool is stated; kept as a decision for that reason. Threshold value: undecided child UPDATE.3.1.
- Rejected: (b) and (c): refuted or unsupported by the two T2 studies (folklore refuted). (d): rejected by SUPPLY-C23 (28.2 percent of dev-configured dependencies were used in production). Audit without a lockfile: results differ per run (SUPPLY-C21).

### PIG-JS.DEPENDENCIES.SCREEN.1 (Scorecard as per-check evidence)

- Positions: (a) Scorecard results as per-check evidence: SUPPLY-C35, QUALITY-C44 (SRC-161 §checks); (b) the aggregate score as a safety gate.
- Forces: Cheap automated signal against the risk of mistaking a score for safety; the cost is reading checks one by one.
- Decision: (a). SRC-161's restriction allows 'Scorecard rewards X', not that X is effective, and states 'a score is never evidence a package is safe'; the decision restates that limit and recommends nothing else.
- Rejected: (b): rejected by the source's own limit; wins under no condition.

### PIG-JS.DEPENDENCIES.PUBLISH.1 (CI publishing credentials)

- Positions: (a) long-lived tokens in CI; (b) trusted publishing with OIDC and short-lived credentials: SUPPLY-C15 (SRC-160, SRC-141, SRC-155 OWASP, consensus); (c) stage-only tokens as the fallback (SUPPLY-C16, SRC-141).
- Forces: Trust wants no long-lived secret in CI; the cost is a supported CI provider and npm 11.5.1 or later with Node 22.14 or later (SRC-160).
- Decision: (b), provenance then generated automatically for public repositories (SUPPLY-C20). SUPPLY-C16 (token policy dates) is a dated fact, demoted from decision (SRC-141 restriction).
- Rejected: (a): legacy tokens are removed (Nov 2025) and direct publishing with a granular token ends (Jan 2027); it would win only where (b) is unavailable, then (c).

### PIG-JS.DEPENDENCIES.PUBLISH.2 (Tarball contents)

- Positions: (a) publish what the directory holds; (b) review the file list before every publish with npm publish --dry-run, keep secrets out, least-privilege CI tokens: SUPPLY-C38 (SRC-155, SRC-156, SRC-161, consensus), SRVSEC-C62 (SRC-078).
- Forces: Accidental exposure is permanent once published; the cost is one review step.
- Decision: (b); unpublish on exposure (SRVSEC-C62). Grounds: three T1 sources.
- Rejected: (a): the default behaviour publishes all files unless excluded; wins under no condition.

### PIG-JS.DEPENDENCIES.PUBLISH.3 (Ship JavaScript)

- Positions: (a) publish TypeScript source; (b) publish JavaScript: TYPES-C07 (SRC-038, inferred).
- Forces: Consumers' runtime must load the package; the cost is a build step.
- Decision: (b). Grounds: Node refuses to handle TypeScript files under node_modules (T1).
- Rejected: (a): would win only for code consumed outside node_modules by a build the project controls; inferred from the stated limitation.

### PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1 (Support window)

- Positions: (a) the main htmx docs site documents 2.x (2.0.11): SRC-213; (b) the security policy and release page show 4.x current with 2.x and 1.9.x supported: SRC-212, SRC-214 (FW-C21, FW-C22).
- Forces: Newest supported major gets fixes longest; docs lag the release line.
- Decision: Pin a supported major and read its own documentation set; a new adoption takes the newest supported major (4.x). Mechanism is not contested, only documentation currency (12_dissent topic 16). 4.0.0 release date is open.
- Rejected: (a) as the current line: wins for an existing project already on 2.x, while 2.x stays on the supported list. 1.9.x: same condition.

### PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4 (Measured usage)

- Positions: (a) rank candidates by measured usage; (b) use measured usage as context only: FW-C42, C43, C45, C49 (SRC-310, SRC-311, SRC-309).
- Forces: Usage figures come from one crawl with Wappalyzer detection and cover React, jQuery and platform features only.
- Decision: (b). The register's standing rule (popularity is not authority) and the measurement limits agree.
- Rejected: (a): would win only with an admitted per-candidate measurement and method (late candidate: HTTP Archive technology report read as data).

### PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST (Framework short list)

- Positions: Candidates and their evidence are in the slot 10 matrix (build/research/10_frameworks/result.md, L3 full). Positions: (a) the slot 10 proposal: React, Angular, Vue, Lit, htmx, no framework as comparator; (b) this record: gates on trust evidence; (c) rank by popularity.
- Forces: Purpose is trust: third-party code with your privileges. The most demanding practice states what the code is, who maintains it and for how long it is patched, and adds the least third-party code. Framework documentation grounds facts about that framework only, so the gates are the build's judgment, recorded here.
- Decision: Gate A (mandatory): the candidate states which versions receive security fixes, as the guideline itself runs only supported versions (TYPES-C45, SUPPLY-C36, SUPPLY-C28). Gate B: a documented escape and sanitization model (slot 10 matrix, owned by DEFENSE). Gate C: stated governance or maintenance body. Pass A and at least one of B or C. Short list, unranked among frameworks because no admitted source can rank them: (1) the platform with Web Components and no framework, default; (2) htmx; (3) Lit; (4) Angular; (5) React. Matrix: React A yes (FW-C25), B yes, C yes (FW-C31, provisional); Angular A yes (FW-C23, strongest), B yes, C open (FW-C35); Lit A yes (FW-C28), B open (FW-C16), C yes (FW-C34); htmx A yes (FW-C21), B yes, C open (FW-C35); Vue A no (FW-C26), B yes, C partial (FW-C32); Svelte A no (FW-C27), B yes, C open; Solid A no (FW-C29, FW-C30), B no (FW-C15, FW-C16), C partial (FW-C33).
- Rejected: Vue: wins if an admitted source states a Vue security-fix window, and then names a legal entity or funding; it is the closest runner-up. Svelte: wins with a supported-versions statement and a governance source. Solid: wins with a support policy and a default-escaping description. (c) popularity: rejected, the standing rule; only React has a figure. 'A framework is always needed': wins when a requirement is not met by the platform (SUPPLY-C27 test). Left off for missing evidence, not for merit; reopen when sources appear.

### PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1 (Platform baseline)

- Positions: (a) the platform's custom elements, shadow DOM and templates with no library: FW-C46 (SRC-235 MDN), FW-C47 (SRC-211 HTML Standard); (b) adopt a framework by default.
- Forces: Zero third-party runtime code against the work a framework saves.
- Decision: (a) is the default and the first candidate (DEPENDENCIES.ADMISSION.1, SUPPLY-C27); custom element names carry a hyphen (T1).
- Rejected: (b): wins when a requirement exists that the platform does not meet and the SUPPLY-C27 isolation test confirms it.
