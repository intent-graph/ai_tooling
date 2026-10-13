# Research result: 06_transverse (TRANS): documentation sync, security practice, configuration and secrets, development environments

Question researched: "how do we make sure the documentation is always up to date" (process, review rules, CI/CD). The design-first versus code-first question is out of scope by the maintainer's ruling. The rest of the slot (security practice across the lifecycle, configuration and secrets, reproducible development environments) was added in a second pass at the coordinator's request; supply chain stays with ADOPT.

## L1 headline

Best practice for the transverse concerns converges on one stance: treat each as code under review and CI, and shrink what can drift or leak by construction (documentation generated or executed, secrets short-lived and out of the repository, environments declared and pinned) while gating what remains; the live disagreements are where gates sit and whether findings block, how config and secrets are delivered, how a development environment is defined, and how much to document; certainty is medium-high on principles (T1/T2 read) and low on measured effectiveness (no empirical study read).

Pinned:
- Sources: 21 T1, 10 T2, 10 T3, 0 T4 (41 total).
- Claims: 58.
- Contested topics: where the documentation gate sits (merge-blocking vs encouraged vs release gate); who verifies accuracy (engineers vs technical writers); how much to document (minimal vs comprehensive docs-as-code); prose-style gating in CI vs human writing review; whether security findings block or only advise; how configuration and secrets reach the running software (environment variables vs files vs store API); named per-environment config bundles vs orthogonal variables; how the development environment is defined (dev container vs Nix vs manifests only).
- Failed fetch on a T1 source: the Kubernetes enhancements (KEP) README returned HTTP 503 (replaced by TRANS-S06); the nix.dev "reproducible environments" page returned 404 (replaced by TRANS-S39). Also: the first NIST SSDF page lacked the practice list (PDF used instead), and the CACM page of the Google static-analysis paper (T3) returned 403 (abstract page read).
- Caveat: pages were read through a fetch tool that returns a model-made extract; quotes are as returned, not checked against full page text. One extract of the SSDF PDF was wrong and was replaced by locally extracted PDF text.

## L2 claims

Clusters
1. Docs are code: same repo, version control, review, issue tracking, change together with the code they describe. Consensus, grounded. TRANS-C01, C21.
2. Sync is triggered by a stated rule: docs in the same change as the behaviour change, with an explicit definition-of-done trigger and a reviewer checklist item. Majority, grounded. TRANS-C02, C03, C04.
3. Gating: block the merge, block the release, or only encourage. Contested, grounded. TRANS-C05, C28, C29.
4. Ownership and lifecycle: every doc has an owner, one canonical source, freshness dates, docs tracked as bugs, stale docs removed or marked obsolete. Consensus, grounded (one primary source, Google). TRANS-C06, C07, C08, C09.
5. Shrink the drift surface: test the examples (doctest, rustdoc) and generate reference from a machine-readable description. Consensus on the idea, grounded; generation of reference is a decision. TRANS-C10, C11, C12, C13.
6. Mechanical CI checks on docs: build with warnings as errors, link check (also scheduled), bot rules for chores. Majority, grounded for tool capabilities, inferred for "scheduled". TRANS-C14, C15, C17, C16.
7. Review of docs: three review types, code-owner routing, writer role. Contested on who verifies accuracy. Grounded. TRANS-C18, C19, C20, C30.
8. Decision records and changelogs keep history current by construction (immutable, superseded, "Unreleased" section) instead of by editing. Majority, grounded. TRANS-C23, C26.
9. Keep docs small, modular, incrementally improved; structure by reader need. Majority, grounded. TRANS-C24, C25.
10. Why it pays: documentation quality amplifies delivery capabilities (DORA); upkeep is real work needing owners. Grounded (as extracted). TRANS-C22.
11. How much to document: minimal (conversation, working software), generated living documentation, or full docs-as-code. Contested, grounded. TRANS-C27.
12. Security is a lifecycle framework of outcomes (SSDF, SAMM) with explicit ownership from the top, training, secure defaults and a vulnerability-response loop. Consensus, grounded. TRANS-C31, C39, C40, C44.
13. Design-time security: threat or risk modelling early and repeatedly, depth set by risk, four questions, tracked mitigations, design review. Majority, grounded. TRANS-C32, C33, C34, C41.
14. Security checks sit at the earliest stage where each can run (pre-commit, build, test instance, post-deploy), with review and analysis chosen by policy; blocking versus advisory is contested. Majority/contested, grounded (stage mapping partly inferred). TRANS-C35, C36, C37, C38.
15. Secret scanning is layered (editor/pre-commit, push, CI) and a found secret is treated as compromised. Majority, grounded. TRANS-C42, C43.
16. Config is separated from code and secrets from config; delivery mechanism and per-environment modelling are contested. Consensus on separation, contested on mechanism, grounded. TRANS-C45, C46, C47, C48, C53.
17. Secrets live in one hardened store, are short-lived and dynamically issued where possible, CI uses federated tokens, and environments and their secrets are isolated. Majority, grounded. TRANS-C49, C50, C51, C52.
18. Development environments are declared as code: explicit dependency manifest plus isolation, pinned and audited toolchain, parity of kind and version with production but isolation of instance and credentials; the mechanism (dev container, Nix, manifests) is contested. Majority/contested, grounded. TRANS-C54, C55, C56, C57, C58.

Live debates (forces in tension)
- Merge gate vs soft encouragement vs release gate: delivery speed and team cognitive load against correctness of docs and confidence.
- Engineers verify accuracy and writers review non-blocking vs writers must approve: delivery speed against consistency and accuracy; depends on number of consumers and team size.
- Write less (less to rot) vs automate generation vs full docs-as-code: cost of ownership against reader confidence and exit risk.
- Prose-style linter as a failing CI check vs human style review: feedback speed and consistency against friction and false positives.
- Blocking vs advisory security findings: security and confidence against delivery speed and developer trust (blocking suits high-confidence, low-noise checks such as secrets; advisory suits noisy analyses).
- Environment variables vs files or a store API for config and secrets: simplicity and portability against security and live rotation.
- Named environment bundles vs orthogonal per-deploy variables: reviewability and control against scalability as deployments multiply.
- Dev container vs pinned Nix package set vs manifests only: onboarding speed and low cognitive load against byte-level reproducibility and control, with cost of ownership on both.
- Dev/prod parity vs environment isolation: confidence from production-like backing services against the security rule that non-production must not touch production services or credentials.
- Executable examples vs readable docs: doctest itself warns that obscure test cases make bad documentation (correctness against clarity).

Candidate central decisions (every team makes these first)
1. Documentation taxonomy by sync mechanism: generated (reference), executed (examples), human-written mutable (guides), immutable log (decision records, changelog). Every other choice hangs on this.
2. Definition-of-done trigger: which kinds of change must touch docs (user-facing, API, workflow, deprecation).
3. Where the gate sits: PR merge, release, or advisory; and who may waive it.
4. Ownership model: owner per doc or path (CODEOWNERS), canonical source, freshness cadence.
5. Who verifies accuracy and who verifies style (engineers, writers, bots).
6. Source of truth for interface docs: machine-readable description with lint and breaking-change diff in CI.
7. Which security framework anchors the practice (SSDF, SAMM, a verification standard) and the risk trigger that sets threat-modelling depth.
8. Which security checks block a change and which advise, and the waiver and audit rule for bypass.
9. The secrets model: one store, static versus short-lived credentials, how secrets are delivered, CI identity (federated tokens), per-environment isolation. Config-versus-code separation is the precondition.
10. How the development environment is defined as code (dev container, pinned package set, manifests only) and which toolchain pins are audited; this sets what "works on my machine" means for CI and every stack guideline.

Not covered
- Security: false-positive thresholds for blocking checks, ASVS levels, SAMM maturity levels, Microsoft SDL, BSIMM; no empirical evidence on tool placement.
- Config and secrets: configuration validation at startup, feature flags as config, comparison of secret managers.
- Dev environments: same definition used in CI and dev, reproducible builds (boundary DELIVER), evidence on Nix versus containers.
- Empirical evidence on documentation drift or on detection tools; AI-assisted drift detection; docs versioning per release; publishing and hosting pipelines; documentation in regulated settings (audit trails).
- The full text of Living Documentation (only a secondary interview read).

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| TRANS-S01 | T1 | doctest, Test interactive Python examples | Python Software Foundation | https://docs.python.org/3/library/doctest.html | executable docstring examples; limits of exact-output matching |
| TRANS-S02 | T1 | Documentation tests (rustdoc book) | Rust project | https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html | doc examples compiled and run by the test command |
| TRANS-S03 | T1 | About code owners | GitHub Docs | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | path-based reviewer assignment, required owner review |
| TRANS-S04 | T1 | sphinx-build options | Sphinx project | https://www.sphinx-doc.org/en/master/man/sphinx-build.html | fail-on-warning and nitpicky doc builds |
| TRANS-S05 | T1 | About Swagger Specification (OpenAPI 3.0) | SmartBear / OpenAPI tooling docs | https://swagger.io/docs/specification/v3_0/about/ | one machine-readable description driving docs, code, tests |
| TRANS-S06 | T1 | Documenting a feature for a release | Kubernetes project (SIG Docs) | https://kubernetes.io/docs/contribute/new-content/new-features/ | release-gated documentation process |
| TRANS-S07 | T1 | Vale documentation | Vale project | https://docs.vale.sh/ | prose linting as code, CI severity |
| TRANS-S08 | T2 | Software Engineering at Google, ch. 10 Documentation | Winters, Manshreck, Wright (Google) | https://abseil.io/resources/swe-book/html/ch10.html | docs as code, ownership, reviews, freshness |
| TRANS-S09 | T2 | Code Review Developer Guide, What to look for | Google eng-practices | https://google.github.io/eng-practices/review/reviewer/looking-for.html | reviewer duty on docs |
| TRANS-S10 | T2 | Documentation quality (capability) | DORA (Google Cloud) | https://dora.dev/capabilities/documentation-quality/ | documentation quality as amplifier of delivery capabilities |
| TRANS-S11 | T2 | Documentation workflow | GitLab Development handbook | https://docs.gitlab.com/development/documentation/workflow/ | docs in the MR, definition of done, roles, CI |
| TRANS-S12 | T2 | Documenting Architecture Decisions | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | short immutable decision records in the repo |
| TRANS-S13 | T2 | Principles behind the Agile Manifesto | Agile Alliance signatories | https://agilemanifesto.org/principles.html | minimal-documentation stance |
| TRANS-S14 | T3 | Docs as Code | Write the Docs | https://www.writethedocs.org/guide/docs-as-code/ | the docs-as-code philosophy |
| TRANS-S15 | T3 | Diátaxis (home and How to use Diátaxis) | Daniele Procida | https://diataxis.fr/ and https://diataxis.fr/how-to-use-diataxis/ | structure by reader need; incremental workflow |
| TRANS-S16 | T3 | Spectral | Stoplight | https://github.com/stoplightio/spectral | linting API descriptions in CI |
| TRANS-S17 | T3 | lychee | lychee maintainers | https://github.com/lycheeverse/lychee | link checking and scheduled runs |
| TRANS-S18 | T3 | openapi-diff | OpenAPITools maintainers | https://github.com/OpenAPITools/openapi-diff | breaking-change detection with failing exit |
| TRANS-S19 | T3 | Danger | Danger maintainers | https://danger.systems/js/ | automating PR review chores |
| TRANS-S20 | T3 | Keep a Changelog 1.1.0 | Olivier Lacan | https://keepachangelog.com/en/1.1.0/ | changelog principles, Unreleased section |
| TRANS-S21 | T3 | Architectural Decision Records | ADR GitHub organization | https://adr.github.io/ | ADR practice, decision log |
| TRANS-S22 | T3 | Living Documentation, book review/interview (InfoQ Brazil) | Cyrille Martraire, via InfoQ | https://www.infoq.com/br/articles/book-review-living-documentation/ | living documentation (secondary: book not read) |

New rows from the extension (security, configuration and secrets, development environments):

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| TRANS-S23 | T1 | NIST SP 800-218 Secure Software Development Framework (SSDF) 1.1 | NIST (Souppaya, Scarfone, Dodson) | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf (text extracted from the PDF) | secure development practices PO, PS, PW, RV |
| TRANS-S24 | T2 | Threat Modeling Manifesto | practitioner authors (threatmodelingmanifesto.org) | https://www.threatmodelingmanifesto.org/ | threat modeling values, principles, four questions |
| TRANS-S25 | T1 | Secrets Management Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | secret centralization, lifecycle, detection, incident response |
| TRANS-S26 | T2 | The Twelve-Factor App, III. Config | Adam Wiggins et al. | https://12factor.net/config | config separation, env vars, no named environments |
| TRANS-S27 | T2 | The Twelve-Factor App, X. Dev/prod parity | Adam Wiggins et al. | https://12factor.net/dev-prod-parity | time, personnel, tools gaps; backing service parity |
| TRANS-S28 | T2 | The Twelve-Factor App, II. Dependencies | Adam Wiggins et al. | https://12factor.net/dependencies | explicit declaration and isolation |
| TRANS-S29 | T1 | Development Container Specification | containers.dev / Dev Container community | https://containers.dev/implementors/spec/ | devcontainer.json, features, lifecycle |
| TRANS-S30 | T1 | OWASP DevSecOps Guideline | OWASP | https://owasp.github.io/www-project-devsecops-guideline/latest (the owasp.org URL redirects here) | security testing stages in the pipeline |
| TRANS-S31 | T1 | About push protection | GitHub Docs | https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection | blocking secrets at push; bypass and audit |
| TRANS-S32 | T1 | OWASP SAMM model | OWASP | https://owaspsamm.org/model/ | maturity model: five functions, fifteen practices |
| TRANS-S33 | T1 | Secure by Design | CISA | https://www.cisa.gov/resources-tools/resources/secure-by-design | producer ownership, transparency, leadership |
| TRANS-S34 | T1 | Kubernetes Secrets | Kubernetes project | https://kubernetes.io/docs/concepts/configuration/secret/ | default-unencrypted caveat, hardening |
| TRANS-S35 | T1 | Kubernetes ConfigMaps | Kubernetes project | https://kubernetes.io/docs/concepts/configuration/configmap/ | config decoupled from images; consumption modes |
| TRANS-S36 | T1 | Vault, Lease, Renew, and Revoke | HashiCorp | https://developer.hashicorp.com/vault/docs/concepts/lease | dynamic secrets, TTL, revocation |
| TRANS-S37 | T1 | OpenID Connect in GitHub Actions | GitHub Docs | https://docs.github.com/en/actions/concepts/security/openid-connect | short-lived federated CI credentials |
| TRANS-S38 | T1 | Automatic token authentication (GITHUB_TOKEN) | GitHub Docs | https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication | least-privilege CI token |
| TRANS-S39 | T1 | Reproducible scripts (pinning Nixpkgs) | nix.dev | https://nix.dev/tutorials/first-steps/reproducible-scripts | pinned package set reproducibility |
| TRANS-S40 | T3 | Lessons from Building Static Analysis Tools at Google | Sadowski et al., CACM | https://research.google/pubs/lessons-from-building-static-analysis-tools-at-google/ (abstract page only; CACM 403) | static analysis in developer workflow |
| TRANS-S41 | T1 | OWASP Application Security Verification Standard | OWASP | https://owasp.org/www-project-application-security-verification-standard/ | verifiable web-app security requirements (levels not read) |

Fetched but unusable: OpenAPI Initiative style guide (github.com/OAI/OpenAPI-Style-Guide) is a branding guide, nothing on sync; not registered.

### Claims

#### Documentation kept in sync

**TRANS-C01**
- claim: Documentation should be treated as code: plain text in version control, changed through review, in the repository of the thing it documents.
- level: principle | stack: neutral | sources: S08 (Documentation is like code; "should, as much as possible, be treated as code"), S14, S11 | agreement: consensus | certainty: grounded

**TRANS-C02**
- claim: Documentation for a behaviour change should be delivered in the same change (pull or merge request) as the code, so the two cannot diverge in time.
- level: decision | stack: neutral | sources: S08 ("change with the code it documents"), S11 (docs in the introducing MR or a separate one raised around the same time; splitting causes docs that merge before release or after), S06 (separate placeholder PR on a release branch) | agreement: majority
- positions: (a) same PR, strongest argument: no window where docs and code disagree; holds Google, GitLab (encouraged, mandatory in some teams); forces: correctness, confidence; wins for continuously deployed products and small teams. (b) separate PR on a release branch, strongest argument: docs ship only when the feature ships and a docs team can work in parallel; held by Kubernetes; forces: control, delivery speed for code; wins with many contributors, release trains, a dedicated docs team. GitLab records the timing cost of splitting.
- certainty: grounded

**TRANS-C03**
- claim: Code review should include a docs check: if a change alters how users build, test, interact with or release the software, reviewers verify that README, guides and generated reference are updated, and that deleted or deprecated code has its docs removed.
- level: practice | stack: neutral | sources: S09 (Documentation item); S11 (code reviewers check accuracy, not style) | agreement: consensus | certainty: grounded

**TRANS-C04**
- claim: A team should state which changes require documentation (a definition-of-done trigger), such as user or admin-visible features, UI or API changes, changed workflows, deprecation and removal; internal-only changes are exempt.
- level: decision | stack: neutral | sources: S11 (Definition of Done) | agreement: majority (one source states it explicitly; S08 and S09 imply it) | certainty: grounded for the rule, inferred for generality

**TRANS-C05**
- claim: The merge of a change that needs documentation should be blocked when the documentation is missing.
- level: decision | stack: neutral | sources: S14 ("block merging of new features if they don't include documentation"), S11 (some teams make it mandatory; writer review non-blocking; maintainers may merge as-is close to release with a follow-up issue) | agreement: contested
- positions: (a) hard merge gate, strongest argument: the only mechanism that does not rely on goodwill; held by Write the Docs, some GitLab teams; forces: correctness, confidence; wins when docs are user-facing contract or regulated. (b) encouraged, reviewer-enforced, with waiver and follow-up issue; held by GitLab; forces: delivery speed, team load; wins when release timing dominates and a follow-up is reliably tracked. See also C28.
- certainty: grounded

**TRANS-C06**
- claim: Every document should have a named owner; unowned documents go stale.
- level: principle | stack: neutral | sources: S08 ("Documents without owners become stale and difficult to maintain") | agreement: consensus | certainty: grounded

**TRANS-C07**
- claim: Documents should carry freshness dates and be tracked as bugs so that review is scheduled, not hoped for.
- level: practice | stack: neutral | sources: S08 (freshness dates; tracking documents as bugs) | agreement: consensus | certainty: grounded (one source; no counter-position found)

**TRANS-C08**
- claim: A document that no longer serves a purpose should be removed or marked obsolete, because stale documents actively mislead.
- level: practice | stack: neutral | sources: S08, S12 (superseded rather than deleted, for decisions) | agreement: consensus | certainty: grounded

**TRANS-C09**
- claim: Each topic should have one canonical document; competing copies should be consolidated into the primary source.
- level: principle | stack: neutral | sources: S08 (Canonical documentation) | agreement: consensus | certainty: grounded

**TRANS-C10**
- claim: Code examples in documentation should be executed in CI so that an example that stops working fails a build rather than rotting silently; keep them readable rather than turned into obscure test cases.
- level: practice | stack: neutral principle; tools Python doctest, Rust rustdoc tests (others exist, not read) | sources: S01 ("check that a module's docstrings are up-to-date"; exact-match limits; "obscure test cases make for bad documentation"), S02 ("makes sure that examples ... are up to date and working") | agreement: consensus | certainty: grounded
- note: forces: confidence, speed of feedback; cost: exact-output fragility (S01).

**TRANS-C11**
- claim: Interface reference should be derived from one machine-readable description (for example OpenAPI) so that rendered docs, client or server stubs and tests share a single source, instead of being hand-copied.
- level: decision | stack: neutral idea; OpenAPI for HTTP APIs | sources: S05, S22 (extract from source, single source of truth) | agreement: majority | certainty: grounded
- note: boundary: VERIFY (contracts). Whether the description is written first or generated from code is deliberately not decided here.

**TRANS-C12**
- claim: The machine-readable API description should be linted in CI against a team ruleset so that style and completeness rules are enforced mechanically.
- level: practice | stack: OpenAPI, AsyncAPI, JSON/YAML (Spectral) | sources: S16 | agreement: majority | certainty: grounded for capability, inferred for "should"

**TRANS-C13**
- claim: CI should diff the API description between versions and fail on incompatible changes, so that interface docs and consumers are never surprised.
- level: practice | stack: OpenAPI 3 (openapi-diff; others exist) | sources: S18 (fail-on-incompatible) | agreement: majority | certainty: grounded
- note: boundary: VERIFY.

**TRANS-C14**
- claim: The documentation build should fail on warnings and on unresolved references, so broken cross-references cannot be published.
- level: practice | stack: Sphinx (-W, -n); equivalent flags in other generators not read | sources: S04 | agreement: consensus | certainty: grounded

**TRANS-C15**
- claim: Links in documentation should be checked automatically in CI and also on a schedule, because external links break without any commit.
- level: practice | stack: neutral; lychee, Sphinx linkcheck | sources: S17 (CI action and scheduled runs), S04 (linkcheck builder named) | agreement: majority | certainty: grounded for capability; inferred for the reason (external links rot independently of commits)

**TRANS-C16**
- claim: Editorial style can be encoded as rules and enforced in CI, with error severity failing the build.
- level: decision | stack: neutral; Vale | sources: S07, S08 (writing review for consistency by humans) | agreement: contested
- positions: (a) style as failing CI check, strongest argument: consistency across many authors without reviewer effort; held by Vale; forces: speed of feedback, consistency; wins with many authors. (b) human writing review, strongest argument: judgment of clarity and audience cannot be linted; held by Google; forces: quality; wins with few authors or high-stakes docs. Vale itself says it targets consistency, not correctness.
- certainty: grounded

**TRANS-C17**
- claim: Repetitive review chores about documentation (changelog entry present when source changed, docs touched when API files changed) should be automated as CI rules that comment or fail on the pull request.
- level: practice | stack: neutral idea; Danger (JS/TS rules) | sources: S19 | agreement: majority | certainty: grounded for capability; inferred limit: path-based rules can detect absence of an edit, not inaccuracy

**TRANS-C18**
- claim: Documentation paths should be mapped to owners with a code-owners file, and review by an owner required by branch protection.
- level: practice | stack: GitHub CODEOWNERS (GitLab and others have equivalents, not read) | sources: S03 | agreement: majority | certainty: grounded
- note: any single listed owner suffices; the file itself needs an owner.

**TRANS-C19**
- claim: Documentation should receive three kinds of review: technical (accuracy), audience (clarity) and writing (consistency); the team must decide who does each.
- level: decision | stack: neutral | sources: S08, S11 | agreement: contested (on who)
- positions: (a) engineers and code reviewers verify accuracy, technical writers review non-blocking before or after merge, a follow-up issue is opened if merged without writer review (GitLab; forces: delivery speed; wins with a small writer team and many changes). (b) writers must approve significant changes (also GitLab, for significant ones; forces: consistency, quality; wins for cross-API-boundary or customer-facing docs).
- certainty: grounded

**TRANS-C20**
- claim: Engineers should write the docs for what they build; technical writers should focus on documents that cross API boundaries and on guidelines and champions, since engineers see docs as separate from programming and tooling is poor.
- level: decision | stack: neutral | sources: S08 (When technical writers are needed; why engineers dislike writing), S10 (writers, champions, guidelines) | agreement: majority | certainty: grounded

**TRANS-C21**
- claim: Documentation changes should reuse the existing developer workflow (bug tracker, code review, CI) rather than a parallel process.
- level: principle | stack: neutral | sources: S08 (TL;DR "Documentation changes should leverage the existing developer workflow"), S14 | agreement: consensus | certainty: grounded

**TRANS-C22**
- claim: Teams should invest in documentation quality as a delivery capability, and budget for upkeep: documentation needs active creation and maintenance, which takes work.
- level: principle | stack: neutral | sources: S10 (quality measured on clarity, findability, reliability; reported lifts in continuous delivery, continuous integration, trunk-based development and supply-chain security practices when quality is above average) | agreement: majority (one research program) | certainty: grounded for the DORA reading (percentages as extracted, not re-verified); causality inferred, correlational survey data

**TRANS-C23**
- claim: Decisions and their rationale should be kept as short, numbered, immutable records in the repository, with a status (proposed, accepted, deprecated, superseded); a changed decision is a new record that supersedes the old one, not an edit.
- level: decision | stack: neutral | sources: S12, S21 | agreement: majority | certainty: grounded
- positions: (a) immutable log, forgiving: history is never wrong, only superseded; wins for rationale documents. (b) mutable living documents kept current by CI and ownership (C01 to C18); wins for how-to and reference. Two models, to be assigned per document type (see central decision 1).

**TRANS-C24**
- claim: Documents should be small and modular, because small documents have a chance of being updated and large specifications do not.
- level: principle | stack: neutral | sources: S12 ("at least a chance at being updated"), S08 (keep documents focused on one purpose) | agreement: majority | certainty: grounded

**TRANS-C25**
- claim: Documentation should be organised by reader need (tutorial, how-to, reference, explanation) and improved in small increments published immediately, never as a big restructuring; it is "always complete, never finished".
- level: decision | stack: neutral | sources: S15 | agreement: majority | certainty: grounded
- note: structure is held by one framework in this pass; other taxonomies not read.

**TRANS-C26**
- claim: Each release should have a human-written changelog, grouped by change type, with an "Unreleased" section filled as changes land.
- level: practice | stack: neutral | sources: S20; S19 (changelog presence enforceable by bot) | agreement: majority | certainty: grounded for the rule; the alternative (changelog generated from commit conventions) was not read, so the debate is open

**TRANS-C27**
- claim: The amount of documentation is a choice to make deliberately: less to maintain, generated from the system, or comprehensive under docs-as-code.
- level: decision | stack: neutral | sources: S13 ("working software is the primary measure of progress"; face-to-face conversation preferred; simplicity), S22 (living documentation: evolves with the code, extracted by automation, minimal effort), S08 (documentation hugely important over time and scale; cost amortized over readers) | agreement: contested
- positions: (a) minimal, conversation first; strongest argument: least text to rot; forces: cost of ownership, delivery speed; wins for small co-located teams, short-lived systems. (b) living documentation, generated or extracted from code and tests; strongest argument: no manual sync; forces: cost of ownership, correctness; wins where domain knowledge is in the code. (c) full docs-as-code with owners and gates; strongest argument: reading cost is paid by many and docs outlive people; forces: confidence, team cognitive load for newcomers; wins with many consumers, long life, turnover.
- certainty: grounded for the positions; context mapping inferred

**TRANS-C28**
- claim: A feature without its documentation should not ship: the release gate may remove it from the milestone, and feature-gated functionality must appear in a reference page.
- level: decision | stack: neutral; Kubernetes process is one realization | sources: S06 (missing first draft by deadline can remove the feature from the release; feature gate documentation file required) | agreement: contested (against C05b soft gate) | certainty: grounded
- positions: gate at release (control, confidence; wins in release-train projects with many contributors) versus gate at merge (C05) versus advisory (delivery speed).

**TRANS-C29**
- claim: Documentation-only changes should run a reduced, faster pipeline so that updating docs is cheap and not postponed.
- level: practice | stack: neutral idea; GitLab realisation by branch name | sources: S11 (CI Checks) | agreement: majority (single source) | certainty: grounded for the practice; inferred for the motivation. boundary: DELIVER

**TRANS-C30**
- claim: When documentation merges without the required reviewer, a follow-up review issue should be opened at once and assigned to author and reviewer, so the debt is tracked.
- level: practice | stack: neutral | sources: S11 (Post-Merge Reviews); S08 (docs tracked as bugs) | agreement: majority | certainty: grounded



#### Security practice across the lifecycle

**TRANS-C31**
- claim: A team should anchor its secure-development practice in a published framework (NIST SSDF; OWASP SAMM) and use it as a list of outcomes to cover across the lifecycle, not as a prescription of tools.
- level: principle | stack: neutral | sources: S23 (SSDF 1.1 groups: Prepare the Organization PO, Protect the Software PS, Produce Well-Secured Software PW, Respond to Vulnerabilities RV; tasks are outcome statements with non-binding "notional implementation examples"), S32 (SAMM: five business functions Governance, Design, Implementation, Verification, Operations, fifteen practices) | agreement: consensus | certainty: grounded
- note: SSDF numbering was read from the PDF text; the first extract of the PDF returned by the fetch tool had wrong practice names and was discarded.

**TRANS-C32**
- claim: Security risk should be modelled during design, early and repeatedly, with depth set by risk: more rigorous assessment for sensitive data, authentication, access control and credential management.
- level: decision | stack: neutral | sources: S23 (PW.1.1 threat modeling, attack modeling, attack surface mapping; example 2 rigour for high-risk areas), S24 (early and frequent analysis; continuous refinement over a single deliverable; dialogue first, documents record) | agreement: majority
- positions: (a) continuous, lightweight, per iteration, strongest argument: a one-off model is stale at the next change; held by the Threat Modeling Manifesto; forces: correctness over time, speed of feedback; wins in fast-changing products with an engaged team. (b) deeper, risk-triggered assessment for high-risk areas only, strongest argument: effort goes where the cost of error is; held by SSDF; forces: cost of ownership; wins under criticality or regulation. The two are compatible; the choice is the trigger and cadence.
- certainty: grounded

**TRANS-C33**
- claim: Each threat model should answer four questions (what are we working on, what can go wrong, what are we going to do about it, did we do a good enough job) and its risks and mitigations should be tracked in the team's workflow.
- level: practice | stack: neutral | sources: S24 (four questions; anti-patterns: hero threat modeler, admiration for the problem), S23 (PW.1.2 track and maintain security requirements and risks) | agreement: consensus | certainty: grounded

**TRANS-C34**
- claim: The design should be reviewed for security by a qualified person or by automated processes in the toolchain, against the risk model, before implementation proceeds.
- level: practice | stack: neutral | sources: S23 (PW.2.1) | agreement: consensus | certainty: grounded (single source)

**TRANS-C35**
- claim: The team should decide by policy when code is reviewed by a person, analysed by tools, or both, by stage and risk; findings are recorded and triaged in the normal workflow, and tool findings are best reviewed by a human who remediates.
- level: decision | stack: neutral | sources: S23 (PW.7.1, PW.7.2 with examples: peer review, static analysis with human review, checklists, continuous automated checks at check-in, root cause of findings) | agreement: majority | certainty: grounded
- positions: human review for backdoors and malicious content (expert reviewers, example 2) versus automation for continuous coverage (example 6); the framework treats them as complements. Forces: confidence against delivery speed. boundary: DELIVER (code review).

**TRANS-C36**
- claim: Security checks should be placed at the earliest pipeline stage where each can run: secrets and lint before commit; static analysis, composition analysis and infrastructure scanning at build; dynamic and interactive testing against a running instance; compliance audit after deployment. The aim is to detect issues as fast as possible.
- level: decision | stack: neutral | sources: S30 (stages and test types listed; goal "detect security issues as fast as possible"), S23 (PW.8.1 choose testing methods by stage) | agreement: majority | certainty: grounded for the stage list; the finer mapping of each tool to a stage is inferred from the guideline's grouping
- note: boundary: VERIFY (static analysis, test levels); supply-chain scanning (composition analysis) belongs to ADOPT.

**TRANS-C37**
- claim: A team must decide whether security findings in the pipeline block the change or only advise, and should make blocking checks the ones developers trust.
- level: decision | stack: neutral | sources: S40 (abstract: static analysis at Google detects thousands of issues per day fixed by engineers "by their own choice" before check-in), S23 (PW.7.2 triage in the workflow), S31 (push protection blocks but allows an audited bypass with a reason) | agreement: contested
- positions: (a) blocking gate, strongest argument: the only guarantee; held by push protection for secrets; forces: security, confidence; wins for high-confidence, low-noise checks and regulated contexts. (b) advisory in the developer's workflow, strongest argument: adoption and trust, engineers fix by choice (Google); forces: delivery speed, team cognitive load; wins for noisy analyses. (c) blocking with audited waiver (GitHub bypass categories: "used in tests" and "false positive" close the alert, "I'll fix it later" stays open); forces: control and speed together; wins where bypass is rare and reviewed.
- certainty: grounded for positions; the false-positive threshold that makes a check blockable was NOT found (open)

**TRANS-C38**
- claim: Executable code should be tested to find vulnerabilities and verify security requirements, including functional tests of the security features themselves, with the test types chosen by stage and run in a sandboxed environment where appropriate.
- level: practice | stack: neutral | sources: S23 (PW.8.1, PW.8.2 example 1) | agreement: consensus | certainty: grounded. boundary: VERIFY

**TRANS-C39**
- claim: Software should ship with a defined secure baseline configuration as its default, and the default settings should be tested to confirm they work and do not break security.
- level: principle | stack: neutral | sources: S23 (PW.9.1, PW.9.2) | agreement: consensus | certainty: grounded

**TRANS-C40**
- claim: Security responsibility should be explicit and owned from the top: roles and responsibilities defined, role-based training provided, management committing, and the producer taking ownership of customer security outcomes.
- level: principle | stack: neutral | sources: S23 (PO.2.1 to PO.2.3), S33 (three principles: take ownership of customer security outcomes, radical transparency and accountability, lead from the top) | agreement: consensus | certainty: grounded

**TRANS-C41**
- claim: A catalogue of verifiable security requirements (for web applications, OWASP ASVS) should serve both as the requirements list for developers and as the basis for testing.
- level: practice | stack: web applications (ASVS); other platforms have equivalents not read | sources: S41 (requirements for secure development; basis for testing technical controls; machine-readable formats) | agreement: majority | certainty: grounded for intended uses; the level definitions (1 to 3) were not read: open

**TRANS-C42**
- claim: Secret scanning should be layered: in the developer's editor or pre-commit, at push time as a blocking check, and in CI; blocking before the secret reaches repository history is preferred to alerting after.
- level: practice | stack: neutral; GitHub push protection and pre-commit detectors are realizations | sources: S25 (detection tools in IDEs and CI/CD pipelines; never hardcode), S31 (blocks before they reach the repository; covers CLI, UI, file upload, API) | agreement: majority | certainty: grounded
- note: forces: speed of feedback, security; cost: bypass paths (see C37).

**TRANS-C43**
- claim: A secret found in code or logs should be treated as compromised: revoke at once, rotate through an automated process, remove it from the exposed locations, and keep audit logs to investigate.
- level: practice | stack: neutral | sources: S25 (incident response section) | agreement: consensus | certainty: grounded (single source; no counter-position found)

**TRANS-C44**
- claim: The lifecycle includes a response loop: identify and confirm vulnerabilities (monitoring databases and reports, a disclosure policy), assess, prioritize and remediate them, then analyze root causes and fix the process as well as the instance.
- level: principle | stack: neutral | sources: S23 (RV.1.1 to RV.1.3, RV.2.1, RV.2.2, RV.3.1 to RV.3.4; the content of RV.2 and RV.3 was read as headings and first examples only) | agreement: consensus | certainty: grounded
- note: boundary: OPERATE (incident handling, feedback from production).

#### Configuration and secrets

**TRANS-C45**
- claim: Configuration should be strictly separated from code: config varies across deploys, code does not. The test is whether the codebase could be open-sourced at any moment without exposing credentials.
- level: principle | stack: neutral | sources: S26 (Config), S35 (decouple environment-specific configuration from container images), S25 | agreement: consensus | certainty: grounded

**TRANS-C46**
- claim: A team must choose how configuration and secrets reach the running software: environment variables, mounted files, or an API of a configuration or secret store, and record why.
- level: decision | stack: neutral; K8s realizes all three | sources: S26 (env vars: hard to commit by accident, language and OS agnostic), S25 (use env vars only when necessary, managed by the orchestrator), S35 (four ways: command args, env vars, read-only volume files, Kubernetes API with updates), S34 (env vars or mounted files) | agreement: contested
- positions: (a) environment variables, strongest argument: universal and simple; held by Twelve-Factor; forces: team cognitive load, portability; wins for small services and PaaS. (b) files or store API for secrets, strongest argument: env vars leak into process listings and child processes and can't be updated live, whereas the API allows subscription to changes (S35); OWASP is cautious about env vars (S25); forces: security, rotation; wins for high-criticality secrets. The leak vectors of env vars in (b) are inferred, not read in a source.
- certainty: grounded for positions, inferred for the leak argument

**TRANS-C47**
- claim: Per-environment configuration should be modelled as independent granular values per deployment, not as named bundles such as development, test, production, which multiply combinatorially as deployments grow.
- level: decision | stack: neutral | sources: S26 (rejects named environment groups; env vars "granular controls, each fully orthogonal"), S35 (use ConfigMaps for configuration that varies per environment) | agreement: contested
- positions: (a) orthogonal granular variables per deploy (Twelve-Factor); forces: scalability of environments, cost of ownership; wins with many deploys (preview, per-tenant). (b) named environment bundles, strongest argument: the full set of an environment can be read and reviewed in one place; the source itself calls this the traditional approach; forces: reviewability, control; wins with few fixed environments. Argument for (b) is inferred; no source read states it.
- certainty: grounded for (a); inferred for (b)

**TRANS-C48**
- claim: Secrets must be kept apart from non-secret configuration, and confidential data must not go in a plain configuration object.
- level: principle | stack: neutral; Kubernetes ConfigMap and Secret as example | sources: S35 (ConfigMaps are non-confidential, not encrypted; use Secrets for sensitive data), S34 | agreement: consensus | certainty: grounded

**TRANS-C49**
- claim: Secrets should be centralized in one managed secrets solution with fine-grained, least-privilege access and automated handling over their lifecycle (creation, rotation, revocation, expiry); a platform default store should be hardened, not trusted as is.
- level: practice | stack: neutral; Kubernetes detail | sources: S25 (centralize; least privilege; lifecycle), S34 (Secrets are unencrypted in etcd by default; enable encryption at rest, restrict with RBAC, consider an external store provider; anyone who can create pods in a namespace can read its secrets) | agreement: consensus | certainty: grounded

**TRANS-C50**
- claim: Credentials should be short-lived and issued dynamically with a time to live and automatic revocation where the platform supports it, because a leaked credential then expires by itself and a compromise can be contained by revoking a lease prefix.
- level: practice | stack: neutral; Vault leases as realization | sources: S36 (leases, TTL, automatic revocation, revoke by prefix, shorter TTL cleans up resources earlier), S25 (rotate, dynamic secrets expire quickly) | agreement: majority | certainty: grounded
- positions: dynamic short-lived (security, blast radius; wins with many services, high criticality, available platform) versus static secrets rotated on a schedule (lower infrastructure cost, team cognitive load; wins for few services and low criticality). The static option's merit is inferred.

**TRANS-C51**
- claim: CI and deployment workflows should authenticate to cloud and other services with federated short-lived tokens (OIDC) rather than long-lived credentials duplicated into the CI system, and the CI-issued token itself should hold the least permissions required.
- level: practice | stack: neutral idea; GitHub Actions OIDC and GITHUB_TOKEN permissions | sources: S37 (no secret duplication, token valid for a single job, automatic rotation, trust conditions on workflow or repository), S38 (grant the token least required access via the permissions key) | agreement: majority | certainty: grounded. boundary: DELIVER

**TRANS-C52**
- claim: Development, build, test and production environments should be separated and protected from each other; production and development secrets are isolated; non-production should minimize use of production services; human access to build services is minimized and audited.
- level: practice | stack: neutral | sources: S23 (PO.5.1 examples 1 to 6), S25 (per-environment separation, reduced access to production) | agreement: consensus | certainty: grounded
- note: this limits dev/prod parity (C55): parity of kind and version, isolation of instance and credentials (inferred synthesis of S23 and S27).

**TRANS-C53**
- claim: Configuration expressed as code should live in a repository with access restricted by least privilege and with tracked, attributable changes, like source code; secrets stay out of it.
- level: practice | stack: neutral | sources: S23 (PS.1.1 stores all forms of code including configuration-as-code; examples 1 and 2), S26 | agreement: consensus | certainty: grounded. boundary: DELIVER

#### Reproducible development environments

**TRANS-C54**
- claim: A project should declare all of its dependencies completely and exactly in a manifest and run them in an isolated environment, never relying on implicitly installed system packages; a new developer should need only the language runtime and the dependency manager plus one command.
- level: principle | stack: neutral; Bundler, pip with virtualenv named | sources: S28 (explicit declaration and isolation, both required; vendor system tools the app shells out to) | agreement: consensus | certainty: grounded
- note: pinning and updating of third-party dependencies is boundary: ADOPT.

**TRANS-C55**
- claim: Development, CI and production should be kept as similar as practical: short time from commit to deploy, authors take part in deploying, and the same type and version of each backing service in every environment, even where an adapter library could hide the difference.
- level: decision | stack: neutral | sources: S27 (time, personnel and tools gaps; continuous deployment; same type and version of backing services; containers make parity cheap) | agreement: majority | certainty: grounded
- positions: (a) full parity of backing services, strongest argument: tests pass in a lighter database and still fail in production; held by Twelve-Factor; forces: confidence, correctness; wins when backing-service behaviour matters. (b) lightweight stand-ins in development for speed and low resource use; the source argues against it, so its merit is inferred; forces: speed of feedback, cost; wins when the adapter surface is narrow and production-like tests exist elsewhere in the pipeline. Parity does not extend to production credentials or access (C52).

**TRANS-C56**
- claim: The development environment should itself be defined as versioned code, and the team must choose the mechanism: a container definition (Dev Container), a pinned package set (Nix), or dependency manifests with language-level isolation only.
- level: decision | stack: tool-specific per option | sources: S29 (Dev Container spec: enriches containers with content and metadata, devcontainer.json in standard locations, "deterministically creates containers", features, ordered lifecycle scripts, works on top of Dockerfile, Compose or images), S39 (pinning a Nixpkgs commit: "exact same package versions, everywhere"), S28 (manifest and isolation) | agreement: contested
- positions: (a) dev container: IDE and container integration, wraps existing formats; forces: team cognitive load, onboarding speed; wins for mixed-skill teams and cloud IDEs. (b) Nix pinned set: byte-level control of package versions across machines and CI; forces: reproducibility, control; costs: learning curve and need for Nix on hosts; the limits (host OS and kernel outside the pin, dependency on pinned source availability) are inferred from the tutorial, not stated. (c) manifests only: lowest cost, but system tools must be vendored (S28); wins for single-language projects with no native dependencies.
- certainty: grounded for features, inferred for comparative costs

**TRANS-C57**
- claim: Build tools, compilers and interpreters should be pinned and changed only through change management that audits unexpected changes and validates authenticity and integrity, while staying on versions that still receive security fixes.
- level: practice | stack: neutral | sources: S23 (PW.6.1 examples 1 to 3: up-to-date versions; change management for updating tools; audit unexpected changes; validate authenticity and integrity), S28, S39 | agreement: majority | certainty: grounded for the rule; the tension between "pinned" and "up to date" is inferred
- note: boundary: ADOPT (pinning and updates) and DELIVER (reproducible builds).

**TRANS-C58**
- claim: Development endpoints and toolchain are an attack surface and should be hardened and monitored: approved hardening guides, least functionality, least privilege, continuous posture monitoring.
- level: practice | stack: neutral | sources: S23 (PO.5.2) | agreement: consensus | certainty: grounded (single source)

### Gaps

- open: no empirical study read on documentation drift rates or on which of these mechanisms measurably reduces drift (DORA is survey correlation only).
- open: changelog generation from commit conventions versus hand-written (positions not read).
- open: docs versioned per release and published from release branches; hosting pipelines.
- open: AI-assisted detection of code-doc inconsistency; commercial drift tools (T4 only, not read).
- open: Living Documentation read only as a secondary interview (T3); primary book not read.
- open: Kubernetes KEP README (T1) not read: HTTP 503.
- open (security): the false-positive threshold above which a check can block a change; empirical value of SAST/DAST placement; ASVS level definitions and SAMM maturity levels not read; Microsoft SDL, BSIMM and Google SAIF/Secure by Design papers not read; the Google static-analysis paper was read as abstract only (CACM page 403).
- open (config and secrets): no source read on configuration validation at startup, feature flags as configuration, or secret-manager comparison across providers; the leak vectors of environment variables are inferred.
- open (dev environments): no source read on using the same environment definition in CI as in development, on reproducible builds as an output property (boundary DELIVER), on Nix versus containers evidence, or on cost of onboarding; nix.dev "reproducible environments" page returned 404 (T1), replaced by the pinning tutorial.
- The first SSDF fetch (NIST landing page) lacked the practice list; the PDF was used. A model extract of that PDF contained wrong practice names (for example PS.1 given as "secure development environment"); the PDF text was extracted locally and the numbering checked against it.
