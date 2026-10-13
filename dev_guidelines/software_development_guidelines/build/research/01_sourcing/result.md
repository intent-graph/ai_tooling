# Research result: 01_sourcing (area SRC)

## L1 headline

Best practice for sourcing libraries, tools and external services is a consensus on WHAT to look at (necessity, maintenance, security record, interface stability, transitive footprint, license, fit) but only a heuristic, self-disclaimed consensus on HOW to weigh it (scores predict outcomes poorly) and a genuine split on WHETHER to import at all, how novel a choice may be, and who decides; certainty is high for the criteria list (grounded in T1/T2), moderate for weighting, low for external services/APIs (only a few T1 stability and availability rules, rest T4).

Pinned:
- Sources by tier: T1 = 10, T2 = 5, T3 = 5, T4 = 1 (21 total).
- Claims: 36.
- Contested topics: reuse vs minimise dependencies; boring-first vs staged novelty; central allowlist vs team choice; micro-packages; single-maintainer tolerance.
- Failed fetches on T1 sources: none lost. NIST SSDF (SP 800-218) HTML page carried no practice text and the PDF fetch returned unreadable text, so the PDF was saved and read locally with a text extractor (PW.4 read in full); OWASP Top 10 A06 needed two redirect hops (read at the final host). Failed on non-T1: ACM Queue copy of Cox "Surviving Software Dependencies" (403), USENIX page for Zimmermann (404, read arXiv copy), CHAOSS metrics pages (no model content returned), OWASP GitHub raw page (404).

## L2 claims

Clusters (agreement; certainty; ids):
1. A new dependency is a standing cost, so necessity is the first test, before any quality test. consensus; grounded; SRC-C01, SRC-C02.
2. Evaluate against an explicit, written criteria set covering design, code, tests, bug handling, maintenance, usage, security, license, transitive dependencies; real teams do it ad hoc. consensus; grounded; SRC-C03, SRC-C04, SRC-C05.
3. Maintenance and sustainability signals (activity, release recency, maintainer diversity, responsiveness, end-of-life plan) are the dominant health signals. consensus (diversity tolerance contested); grounded; SRC-C06, SRC-C07, SRC-C08, SRC-C09.
4. Security signals: known vulnerabilities, disclosure policy, response, authenticity of source, provenance. consensus; grounded; SRC-C10, SRC-C11, SRC-C12, SRC-C13.
5. Interface stability and compatibility promise matter more than they look: they decide whether you can ever take updates. consensus; grounded; SRC-C14, SRC-C15, SRC-C16.
6. Aggregated health scores and popularity are inputs to judgment, never the verdict; Scorecard says so itself and an empirical study finds weak prediction. majority; grounded; SRC-C17, SRC-C18, SRC-C19.
7. Transitive footprint and ecosystem concentration are part of the candidate's cost. consensus (micro-packages contested); grounded; SRC-C20, SRC-C21, SRC-C22.
8. Fit to the task's profile: suitability over hype; re-evaluate when use changes; boring by default, novelty budgeted or staged. contested; grounded; SRC-C23, SRC-C24, SRC-C25, SRC-C26.
9. Vetting depth and gatekeeping: hands-on checking, sanctioned repositories and allowlists versus team autonomy. contested; mixed grounded/inferred; SRC-C27, SRC-C28, SRC-C29.
10. Discovery tooling exists (deps.dev, Scorecard, OSV, criticality score) but is volatile. majority; grounded; SRC-C30.
11. External services and APIs: pick dependencies whose availability and deprecation commitments meet yours, read the stability tier, plan exit. consensus on availability and tiers (T1), exit practice weakly sourced; SRC-C31, SRC-C32, SRC-C33, SRC-C34, SRC-C35, SRC-C36.

Live debates (forces in tension):
- Reuse well-secured third-party code (security, delivery speed) vs minimise dependencies (cost of ownership, control, exit risk): C02.
- Boring-first, few innovation tokens (team cognitive load, reversibility) vs staged novelty via assess/trial/adopt (delivery speed, learning): C24, C25.
- Central allowlist/sanctioned repository (security, control) vs team-chosen libraries (delivery speed, cognitive load): C28.
- Tolerate single-maintainer or small projects (fit, minimal footprint) vs require maintainer diversity (exit risk, continuity): C07.
- Micro-packages as reusable atoms (reuse, readability) vs hidden dependency chains and cost (control, security): C21.
- Score as gate (automation, security) vs score as input (correctness of the decision): C17.
- Popularity as proxy for scrutiny (confidence) vs popularity as hype (suitability): C19.
- Vetting depth, from metadata only to sandboxed behavior test and code review (security vs speed): C27.

Candidate central decisions of the area (others depend on them):
- D-SRC-1: Is import the default or the exception, and what necessity test must a candidate pass? (C01, C02)
- D-SRC-2: Which criteria set and thresholds apply, and does criticality scale their depth? (C03, C27)
- D-SRC-3: Who may choose: any developer, a reviewed proposal, or a sanctioned list? (C28)
- D-SRC-4: Novelty budget: how new may a tool be, and what staging (trial) precedes adoption? (C24, C25)
- D-SRC-5: For an external service: required availability, deprecation notice and exit path before it may be a hard dependency. (C31, C34, C35)

Not covered: CHAOSS metrics models (fetch returned no content), Libraries.io/SourceRank-style ranking, SaaS procurement frameworks (SOC 2, ISO 27001 supplier checks, NIST SP 800-161 body text), licence-compatibility detail, evaluation of dev tools and CI services as opposed to libraries, "Software Engineering at Google" chapters other than 21, Sonatype/Tidelift annual reports, books (Nygard, Humble and Farley) not fetchable.

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| SRC-S01 | T1 | Scorecard checks | OpenSSF | https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md | the check list, risk levels, caveats of automated project-health scoring |
| SRC-S02 | T1 | OpenSSF Scorecard README | OpenSSF | https://github.com/ossf/scorecard | stated purpose and limits of Scorecard for consumers |
| SRC-S03 | T1 | Concise Guide for Evaluating Open Source Software | OpenSSF Best Practices WG | https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software | evaluation criteria for choosing OSS, with rationale |
| SRC-S04 | T1 | NIST SP 800-218, Secure Software Development Framework v1.1, practice PW.4 | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf (PDF saved, text-extracted) | reuse of well-secured components, review in context, tracking unmaintained components |
| SRC-S05 | T1 | OWASP Top 10:2021 A06 Vulnerable and Outdated Components, How to Prevent | OWASP | https://top10.owasp.org/2021/A06_2021-Vulnerable_and_Outdated_Components | component inventory, official sources, removal of unused, unmaintained libraries |
| SRC-S06 | T1 | Criticality Score | OpenSSF | https://github.com/ossf/criticality_score | project-importance signals; notes public infrastructure stopped May 2026 |
| SRC-S07 | T1 | REL11-BP07 Architect your product to meet availability targets and uptime SLAs | AWS Well-Architected | https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_withstand_component_failures_service_level_agreements.html | dependency SLAs and availability when composing services (platform-official; AWS-specific wording, general principle) |
| SRC-S08 | T1 | Kubernetes Deprecation Policy | Kubernetes project | https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | alpha/beta/GA stability tiers and minimum support (tool-official; a worked example of a published policy) |
| SRC-S09 | T1 | AIP-185 API Versioning | Google API Improvement Proposals | https://google.aip.dev/185 | versioning, channels and deprecation periods of a service API (platform-official) |
| SRC-S10 | T1 | deps.dev documentation | Google Open Source Insights | https://docs.deps.dev/ | what a dependency-graph and advisory aggregator provides |
| SRC-S11 | T2 | Software Engineering at Google, ch. 21 Dependency Management | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch21.html | when to import, cost of dependencies, compatibility promises, Hyrum's Law, version strategies |
| SRC-S12 | T2 | Our Software Dependency Problem | Russ Cox | https://research.swtch.com/deps | inspection checklist before adding a dependency |
| SRC-S13 | T2 | Choose Boring Technology | Dan McKinley | https://mcfunley.com/choose-boring-technology | innovation tokens, bias to proven technology |
| SRC-S14 | T2 | The Twelve-Factor App, II Dependencies | Adam Wiggins / Heroku | https://12factor.net/dependencies | explicit, complete dependency declaration and isolation |
| SRC-S15 | T2 | Technology Radar FAQ | Thoughtworks | https://www.thoughtworks.com/radar/faq | Adopt/Trial/Assess/Caution rings, how the radar is compiled |
| SRC-S16 | T3 | Do Software Security Practices Yield Fewer Vulnerabilities? | Zahan, Shohan, Harris, Williams (arXiv 2210.14884) | https://arxiv.org/abs/2210.14884 | empirical link between Scorecard scores and vulnerability counts (npm, PyPI) |
| SRC-S17 | T3 | Selecting Third-Party Libraries: The Practitioners' Perspective | Larios Vargas et al. (ESEC/FSE 2020; arXiv 2005.12574) | https://ar5iv.labs.arxiv.org/html/2005.12574 | what developers actually weigh when choosing a library (16 interviews, 115 survey responses) |
| SRC-S18 | T3 | Small World with High Risks: A Study of Security Threats in the npm Ecosystem | Zimmermann, Staicu, Tenny, Pradel (USENIX Security 2019; arXiv 1902.09217) | https://arxiv.org/abs/1902.09217 | maintainer concentration and unmaintained-vulnerable packages in npm |
| SRC-S19 | T3 | On the Impact of Micro-Packages: An Empirical Study of the npm JavaScript Ecosystem | Kula, Ouni, German, Inoue (arXiv 1709.04638) | https://arxiv.org/abs/1709.04638 | dependency chains and usage cost of micro-packages (abstract read, not full text) |
| SRC-S20 | T3 | Go Proverbs: "A little copying is better than a little dependency" | Rob Pike, Gopherfest 2015 | https://go-proverbs.github.io/ | the minority school favouring copying over small dependencies (proverb only, argument not read) |
| SRC-S21 | T4 | Vendor-lock-in and third-party API risk blog posts | various vendor blogs | search-result snippets only (truto.one, techconcepts.org, blog.apilayer.com), pages not fetched | live debate on API SLA, deprecation notice lengths and exit clauses; never sole ground |

### Claims

**SRC-C01** | claim: Every new dependency should be justified by necessity before its quality is assessed, because it adds attack surface and ownership cost beyond the development effort it saves. | level: principle | stack: neutral | sources: S03 (Consider Necessity), S11 (When to Import a Dependency), S12 | agreement: consensus | certainty: grounded

**SRC-C02** | claim: Decide explicitly, per need, between reusing a third-party component and keeping or writing the capability in-house; do not default either way. | level: decision | stack: neutral | boundary: ADOPT | sources: S04 (PW.4 title and PW.4.1/PW.4.2), S11 ("prefer source control problems over dependency-management problems"), S12, S20 | agreement: contested | positions: (a) Reuse well-secured existing software rather than duplicate, strongest argument: lowers cost, speeds delivery and avoids new vulnerabilities, especially for cryptography and protocols (NIST SSDF PW.4; forces security, delivery speed; wins when the domain is complex or security-critical and a vetted component exists). (b) Minimise dependencies; all else equal an internal code problem is cheaper than a dependency-management problem you do not control (Google SWE ch. 21; Cox; Pike "a little copying"; forces cost of ownership, control, exit risk; wins for small, stable functionality, long-lived products, or when upgrade incentives are weak). (c) Build in-house only for needs third-party software cannot better meet (NIST PW.4.2 reconciles the two). | certainty: grounded

**SRC-C03** | claim: Judge a candidate against an explicit criteria set covering design and docs, code quality, tests, bug handling, maintenance, usage, security exposure, license and transitive dependencies, and record the result. | level: practice | stack: neutral | sources: S12 (inspection checklist), S03 (all sections), S11 (evaluation criteria) | agreement: consensus | certainty: grounded (the "record the result" part is inferred from NIST PW.4.1 ex. 5 approved lists and the ad-hoc finding in C05)

**SRC-C04** | claim: Evaluate the candidate in the context of its intended use, and repeat the evaluation when the use changes substantially. | level: principle | stack: neutral | sources: S04 (PW.4.1 example 1), S03 (Suitability), S12 ("will it process untrusted input") | agreement: consensus | certainty: grounded

**SRC-C05** | claim: Make the selection process systematic and written, because practitioners mostly select ad hoc and over two dozen technical, human and economic factors then decide the outcome. | level: practice | stack: neutral | sources: S17 (findings: ad-hoc selection; 26 factors; recommendations for practitioners) | agreement: consensus (one study; no contrary source found) | certainty: grounded for the finding, inferred for the recommendation

**SRC-C06** | claim: Prefer candidates with recent commits, recent releases and visible project communication; treat long inactivity as a risk. | level: practice | stack: neutral | sources: S03 (Activity Level, Communication, Release Recency), S01 (Maintained, risk High), S12 (Maintenance), S11 (maintenance track record), S17 | agreement: consensus | certainty: grounded

**SRC-C07** | claim: Prefer projects with several maintainers from several organisations; a single-maintainer project needs a compensating reason or an exit plan. | level: decision | stack: neutral | sources: S03 (Maintainer Diversity), S01 (Contributors, but caveat that single-contributor or narrow-scope projects may legitimately score low), S12 (how many maintainers), S18 (few maintainer accounts reach most packages) | agreement: contested | positions: (a) Require diversity: single point of failure for fixes and for account takeover (OpenSSF; Zimmermann et al.; forces exit risk, security, continuity; wins when the component is on a critical path or hard to replace). (b) Tolerate small projects: Scorecard itself says low contributor scores are not definitive and narrow, finished tools legitimately have one author (S01; forces cost of ownership, fit, minimal footprint; wins for small, stable, easily replaced or vendorable components). | certainty: grounded

**SRC-C08** | claim: Check responsiveness: how many bug reports are open and how fast they are resolved, and whether security fixes are backported or offered on long-term-support versions. | level: practice | stack: neutral | sources: S12 (Debugging), S03 (Security Response) | agreement: consensus | certainty: grounded

**SRC-C09** | claim: For each component, confirm it is still maintained and not at end of life, and keep a plan of action for components that stop being maintained. | level: practice | stack: neutral | boundary: ADOPT | sources: S04 (PW.4.4 examples 4 and 5), S05 (Monitor Unmaintained Libraries), S18 (unmaintained packages depend on long-known vulnerabilities) | agreement: consensus | certainty: grounded

**SRC-C10** | claim: Reject or defer candidates whose current version has known, unfixed vulnerabilities for the intended deployment, and re-check vulnerability status over the component's life. | level: practice | stack: neutral | sources: S03 (Vulnerability Status), S01 (Vulnerabilities, risk High), S04 (PW.4.4 examples 1 and 2), S05 (Inventory and Monitor, Use Automated Tools) | agreement: consensus | certainty: grounded

**SRC-C11** | claim: Prefer projects that publish a vulnerability-disclosure policy and a reporting channel. | level: practice | stack: neutral | sources: S03 (Vulnerability Reporting), S01 (Security-Policy, risk Medium) | agreement: consensus | certainty: grounded

**SRC-C12** | claim: Verify authenticity before adoption: obtain components only from official sources over secure links, prefer signed packages, and check name against look-alikes (typosquatting) and compromised forks. | level: practice | stack: neutral | boundary: ADOPT | sources: S03 (Verify Authenticity, Name Verification), S05 (Secure Component Sources), S04 (PW.4.4 example 6), S01 (Signed-Releases) | agreement: consensus | certainty: grounded

**SRC-C13** | claim: Treat provenance data (SBOM, signed releases, hosting-platform protections such as branch protection and review) as a selection signal, and rebuild from verified source when binary provenance cannot be confirmed. | level: practice | stack: neutral | boundary: ADOPT | sources: S04 (PW.4.1 examples 3 and 8), S01 (SBOM, Signed-Releases, Branch-Protection, Code-Review) | agreement: majority (T1 sources agree, no practitioner source read on cost) | certainty: grounded

**SRC-C14** | claim: Read the candidate's compatibility promise (none, source-compatible, binary-compatible, automated migration) because it decides how costly every future update will be. | level: principle | stack: neutral | sources: S11 (API Stability and Compatibility Promises: C++ standard library, Go, Abseil, Boost examples) | agreement: consensus | certainty: grounded

**SRC-C15** | claim: Prefer interfaces that are stable and secure by default; unstable APIs impede security updates and unsafe defaults hurt non-expert users. | level: practice | stack: neutral | sources: S03 (Interface Stability, Secure Defaults, Interface Design, Security Guidance) | agreement: consensus | certainty: grounded

**SRC-C16** | claim: Treat a 0.x, alpha or beta version label as a signal of incomplete or experimental software and accept it only knowingly. | level: practice | stack: neutral | sources: S03 (Version Stability), S08 (alpha may be removed without notice; beta gets 9 months or 3 releases), S09 (alpha-only features may be removed without notice) | agreement: majority | positions: (a) Avoid pre-1.0 in production (OpenSSF; force correctness, reversibility). (b) Version labels are not uniform across projects; many mature tools stay 0.x (inferred, no source read; force fit). | certainty: grounded for (a), open for (b)

**SRC-C17** | claim: Use aggregate health or security scores as an input to a judgment about individual behaviors, not as the verdict or a hard gate. | level: principle | stack: neutral | sources: S02 (Key limits: opinionated, false positives and negatives, aggregate hides detail), S01 (Scoring caveats: "not a definitive indication that the project is at risk"), S16 | agreement: majority | positions: (a) Input only: Scorecard's own documentation (force correctness of the decision; wins always for a single decision). (b) Gate at a threshold via automation (not argued in any source read; inferred as the practice of organisations that automate policy; forces consistency, speed of review; wins at large scale where per-package review is impossible). | certainty: grounded for (a), inferred for (b)

**SRC-C18** | claim: Do not expect process scores to predict vulnerability outcomes: the empirical study found low explanatory power (R-squared 9 to 12 percent) and, counterintuitively, more reported vulnerabilities as aggregate score rose. | level: principle | stack: neutral | sources: S16 | agreement: consensus (single study) | certainty: grounded (one study; replication not checked)

**SRC-C19** | claim: Use adoption and popularity as a weak proxy for scrutiny and community support, never as proof of quality or suitability. | level: practice | stack: neutral | sources: S03 (Adoption, Suitability: "avoid hype-driven choices"), S11 (how popular is the project), S12 (Usage), S17 (popularity among most cited factors), S13 | agreement: majority | positions: (a) Popular software is scrutinised more and has more help (OpenSSF, Google; force confidence). (b) Popularity can be hype and says nothing about fit (OpenSSF Suitability; McKinley; force suitability, reversibility). | certainty: grounded

**SRC-C20** | claim: Count the candidate's transitive dependencies as part of its cost and prefer candidates with few unnecessary indirect dependencies. | level: practice | stack: neutral | sources: S12 (Dependencies), S03 (Dependency Impact), S19, S18 | agreement: consensus | certainty: grounded

**SRC-C21** | claim: Be wary of many tiny single-purpose packages: they carry long dependency chains and as much usage cost as larger packages. | level: decision | stack: JavaScript/npm evidence (generalisable) | sources: S19 (abstract), S18 (small set of maintainers reach most packages), S20 | agreement: contested | positions: (a) Avoid or inline trivial packages (Kula et al.; Pike; forces control, security, cost of ownership; wins where supply-chain exposure matters). (b) Small shared packages give reuse and tested readability (not read in a source; open; forces reuse, delivery speed). | certainty: grounded for (a), open for (b)

**SRC-C22** | claim: Account for ecosystem concentration: a few maintainer accounts can reach most packages in a registry, so a candidate's reachable trust surface, not just its own repository, is the exposure. | level: principle | stack: npm evidence (registry-wide principle inferred) | sources: S18 | agreement: majority (single study; others point the same direction, S03, S05) | certainty: grounded for npm, inferred for other registries

**SRC-C23** | claim: Select for fit to the task's actual requirements and constraints, not for features or fashion. | level: principle | stack: neutral | sources: S03 (Suitability), S17 (fit for purpose is the most-cited factor), S13 (optimise globally, "least worst" tool across problems) | agreement: consensus | certainty: grounded

**SRC-C24** | claim: Default to proven technology and treat novelty as a budget: spend a limited number of innovation tokens only where the business needs it, after documenting why existing tools are inadequate. | level: decision | stack: neutral | sources: S13 (Innovation Tokens, When to Introduce New Technology) | agreement: contested | positions: (a) Boring first (McKinley; failure modes of proven tools are known; forces team cognitive load, operational cost, reversibility; wins for small teams, operations-heavy systems, long lifetimes). (b) Staged novelty: place candidates in assess, trial, adopt rings and try them where experience is gained (Thoughtworks Radar; force learning, delivery speed through better tools; wins for organisations with capacity for experiments and tolerance for churn). | certainty: grounded

**SRC-C25** | claim: Move a new tool through explicit stages (assess, then trial in limited production use, then adopt, with hold for those that burned you) instead of switching in one step. | level: practice | stack: neutral | sources: S15 (ring definitions) | agreement: majority (one framework; no source read opposes, but C24(a) discourages novelty at all) | certainty: grounded for the framework, inferred that it is a selection practice

**SRC-C26** | claim: Hold the number of different tools solving the same problem down, and plan migration of the replaced one when introducing another. | level: practice | stack: neutral | sources: S13 | agreement: majority (one source) | certainty: grounded

**SRC-C27** | claim: Scale vetting depth to criticality and exposure: metadata review for low-risk, running the candidate's tests, sandboxed behavior tests and code review (install scripts, exfiltration, obfuscation, TODO-marked security gaps) for high-risk or untrusted-input components. | level: decision | stack: neutral | sources: S03 (Practical Testing, Code Evaluation), S12 (Testing: "can you run them yourself", untrusted input), S04 (PW.4.4 example 7) | agreement: contested | positions: (a) Metadata and scores only (fast, cheap; forces delivery speed, cost; wins for low-criticality, replaceable parts). (b) Hands-on test and review (OpenSSF; Cox; forces security, confidence; wins for components handling untrusted input, credentials or cryptography). The scaling rule itself is inferred from S03 and S12, not stated by them. | certainty: inferred (scaling rule), grounded (the practices)

**SRC-C28** | claim: Decide who may introduce a dependency: any developer, a reviewed proposal, or a sanctioned repository and approved-component list with provenance data. | level: decision | stack: neutral | boundary: ADOPT | sources: S04 (PW.4.1 examples 4, 5, 6), S11 (organisational fit: designated maintainer), S13 (visibility and conversation before new tech) | agreement: contested | positions: (a) Central sanctioned list (NIST SSDF; forces security, control, consistency; wins in regulated or high-criticality contexts and many teams). (b) Team-level choice with light visibility (McKinley's conversation and documentation; forces delivery speed, cognitive load; wins for small teams, low regulation). No source read argues (b) against (a) directly; the contrast is inferred. | certainty: inferred (contrast), grounded (each position)

**SRC-C29** | claim: Write the reason for each non-trivial selection (alternatives considered, criteria, accepted risks) where later maintainers will find it. | level: practice | stack: neutral | sources: S13 ("document why"), S17 (ad-hoc selection), S04 (PW.4.1 approved lists) | agreement: majority | certainty: inferred (synthesis of S13, S17, S04)

**SRC-C30** | claim: Use ecosystem aggregators for discovery and first screening (dependency graph, advisories via OSV, Scorecard results, criticality ranking) and expect those services to change or stop. | level: practice | stack: neutral (tools are ecosystem-specific) | sources: S10, S02, S06 (public criticality-score infrastructure stopped May 2026), S17 (package managers as decision-support platforms) | agreement: majority | certainty: grounded

**SRC-C31** | claim: When choosing an external service, pick one whose availability target is at least your own, since hard dependencies multiply availabilities, and set your own SLA with the dependencies' SLAs in view. | level: principle | stack: neutral (AWS wording) | boundary: OPERATE | sources: S07 (Implementation guidance, anti-patterns) | agreement: consensus (one T1 source; mathematically general) | certainty: grounded

**SRC-C32** | claim: Fewer dependencies raise availability; prefer loosely coupled designs that tolerate a degraded dependency, turning hard dependencies into soft ones where possible. | level: principle | stack: neutral | boundary: OPERATE | sources: S07 (Reducing dependencies; loosely coupled designs); REL05-BP01 graceful degradation seen only as a search-result summary | agreement: consensus | certainty: grounded for S07, inferred for graceful-degradation detail

**SRC-C33** | claim: Monitor the reachability, latency and errors of every external service as part of adopting it. | level: practice | stack: neutral | boundary: OPERATE | sources: AWS OPS04-BP04 (dependency telemetry), known only from a search-result summary, page not fetched | agreement: consensus (one source) | certainty: inferred (not read in full)

**SRC-C34** | claim: Before depending on a service API, read its stability tiers and deprecation commitments (what may be removed without notice, minimum notice before removal) and prefer a service with a published policy. | level: practice | stack: neutral (examples are Kubernetes and Google APIs) | sources: S08 (alpha: removable without notice; beta: 9 months or 3 releases; GA: not removed within a major version), S09 (reasonable well-communicated deprecation; recommend 180 days for beta; alpha removable without notice), S21 (reported real-world notice anywhere from 30 days to 12 months, T4) | agreement: consensus among T1 sources, practice in the wild is weaker | certainty: grounded (S08, S09); the in-the-wild range is T4 only

**SRC-C35** | claim: Assess exit and portability at selection time: keep credentials, data and integration logic exportable and put an abstraction between your code and the dependency so it can be replaced. | level: decision | stack: neutral | boundary: ADOPT | sources: S12 (abstract interfaces to enable replacement), S21 (exit clauses, portable tokens; T4 only) | agreement: majority | positions: (a) Wrap and keep exit path (Cox; force exit risk, reversibility; wins when the dependency is on a critical path or vendor behaviour is uncertain). (b) Use the dependency directly and accept lock-in for speed (not sourced; inferred; force delivery speed; wins when the dependency is core and stable). | certainty: inferred (T4 plus one T2 line)

**SRC-C36** | claim: Check the licence is present, clear and acceptable for the intended use; a project that will not state its licence is less likely to follow other good practices. | level: practice | stack: neutral | sources: S03 (License Clarity), S12 (Licensing), S01 (License, risk Low), S17 (licensing factor) | agreement: consensus | certainty: grounded (licence compatibility analysis itself not covered)

### Gaps (open)

- CHAOSS metrics models: pages fetched returned no model definitions (17 models, 89 metrics reported on one page); not read. Open for health-metric taxonomies.
- Strongest argument for micro-packages (C21b) and for pre-1.0 maturity (C16b) not found in a source read.
- No T1/T2 source read on evaluating SaaS suppliers (SOC 2, ISO 27001, NIST SP 800-161 body); service-sourcing claims C31 to C35 rest on one AWS page, two API-policy pages and T4 blogs.
- No source read on sourcing development tools or CI services as distinct from libraries.
- Threshold values (how recent is recent, how many maintainers) are given by no source; any numeric rule must come from the judge or the maintainer's doctrine.
- Scorecard prediction result (C18) rests on one study on npm and PyPI; replication unchecked.
- Cox's ACM Queue follow-up and Fowler/Nygard books not read.
