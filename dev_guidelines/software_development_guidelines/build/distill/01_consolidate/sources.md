# Source register: all sources of the research, deduplicated

One row per distinct source: 296 source ids of the 10 research registers (plus MAINT-S01) replaced by 264 rows. Two origin ids are the same source when they name the same page (same normalised URL), plus two pairs the URL test misses: the OpenSSF Scorecard checks page (raw and rendered copy) and NIST SP 800-218 (PDF and landing page). Tier is the highest among the origin ids; where origin tiers differ the notes column says so. `reg` ids (REG-nnn) are the ids the ledger cites; `replaces` lists every original id (`<AREA>-S<nn>`, as in each result's source register).

Tiers (brief_shared): T1 normative or official, T2 recognized authority, T3 reputable practice, T4 community (never the sole ground of a claim). `maintainer` is MAINT-S01, the maintainer's codified practice: not citable, no tier. Two T4 rows record search results only, with no page read (SRC-S21, EXT-S39); one T2 row (the Kleppmann chapter, DATA-S23) was not read either, only a search summary was seen: the notes column flags all three.

Distinct sources by tier: T1 106, T2 103, T3 50, T4 4, maintainer 1; total 264.


| reg | tier | title | author or body | url read | authoritative on | replaces (original ids) | notes |
|---|---|---|---|---|---|---|---|
| REG-001 | T1 | Scorecard checks | OpenSSF | https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md ; https://github.com/ossf/scorecard/blob/main/docs/checks.md | the check list, risk levels, caveats of automated project-health scoring / pinned dependencies, update tool, vulnerabilities, maintained, signed releases | SRC-S01, ADOPT-S07 | - |
| REG-002 | T1 | OpenSSF Scorecard README | OpenSSF | https://github.com/ossf/scorecard | stated purpose and limits of Scorecard for consumers | SRC-S02 | - |
| REG-003 | T1 | Concise Guide for Evaluating Open Source Software | OpenSSF Best Practices WG | https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software | evaluation criteria for choosing OSS, with rationale / adoption-time evaluation | SRC-S03, ADOPT-S08 | - |
| REG-004 | T1 | NIST SP 800-218, Secure Software Development Framework v1.1, practice PW.4 | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf ; https://csrc.nist.gov/pubs/sp/800/218/final | reuse of well-secured components, review in context, tracking unmaintained components / PW.4 reuse and verify third-party components / code analysis and executable testing as normative practices / secure development practices (page gave practice names only) / secure development practices PO, PS, PW, RV | SRC-S04, ADOPT-S05, VERIFY-S24, DELIVER-S24, TRANS-S23 | - |
| REG-005 | T1 | OWASP Top 10:2021 A06 Vulnerable and Outdated Components, How to Prevent | OWASP | https://top10.owasp.org/2021/A06_2021-Vulnerable_and_Outdated_Components | component inventory, official sources, removal of unused, unmaintained libraries | SRC-S05 | - |
| REG-006 | T1 | Criticality Score | OpenSSF | https://github.com/ossf/criticality_score | project-importance signals; notes public infrastructure stopped May 2026 | SRC-S06 | - |
| REG-007 | T1 | REL11-BP07 Architect your product to meet availability targets and uptime SLAs | AWS Well-Architected | https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_withstand_component_failures_service_level_agreements.html | dependency SLAs and availability when composing services (platform-official; AWS-specific wording, general principle) | SRC-S07 | - |
| REG-008 | T1 | Kubernetes Deprecation Policy | Kubernetes project | https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | alpha/beta/GA stability tiers and minimum support (tool-official; a worked example of a published policy) | SRC-S08 | - |
| REG-009 | T1 | AIP-185 API Versioning | Google API Improvement Proposals | https://google.aip.dev/185 | versioning, channels and deprecation periods of a service API (platform-official) / versions, stability, deprecation period | SRC-S09, EXT-S27 | origin tiers differ: SRC-S09 T1; EXT-S27 T2 |
| REG-010 | T1 | deps.dev documentation | Google Open Source Insights | https://docs.deps.dev/ | what a dependency-graph and advisory aggregator provides | SRC-S10 | - |
| REG-011 | T2 | Software Engineering at Google, ch. 21 Dependency Management | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch21.html | when to import, cost of dependencies, compatibility promises, Hyrum's Law, version strategies / cost of dependency, SemVer limits, Hyrum's Law, MVS, live at head, vendoring | SRC-S11, ADOPT-S01 | - |
| REG-012 | T2 | Our Software Dependency Problem | Russ Cox | https://research.swtch.com/deps | inspection checklist before adding a dependency / pre-adoption checks, options to reduce dependency risk | SRC-S12, ADOPT-S02 | origin tiers differ: SRC-S12 T2; ADOPT-S02 T3 |
| REG-013 | T2 | Choose Boring Technology | Dan McKinley | https://mcfunley.com/choose-boring-technology | innovation tokens, bias to proven technology / cost of each new technology | SRC-S13, ADOPT-S28 | origin tiers differ: SRC-S13 T2; ADOPT-S28 T3 |
| REG-014 | T2 | The Twelve-Factor App, II Dependencies | Adam Wiggins / Heroku | https://12factor.net/dependencies | explicit, complete dependency declaration and isolation / explicit declaration plus isolation / explicit declaration and isolation | SRC-S14, ADOPT-S06, TRANS-S28 | - |
| REG-015 | T2 | Technology Radar FAQ | Thoughtworks | https://www.thoughtworks.com/radar/faq | Adopt/Trial/Assess/Caution rings, how the radar is compiled | SRC-S15 | - |
| REG-016 | T3 | Do Software Security Practices Yield Fewer Vulnerabilities? | Zahan, Shohan, Harris, Williams (arXiv 2210.14884) | https://arxiv.org/abs/2210.14884 | empirical link between Scorecard scores and vulnerability counts (npm, PyPI) | SRC-S16 | - |
| REG-017 | T3 | Selecting Third-Party Libraries: The Practitioners' Perspective | Larios Vargas et al. (ESEC/FSE 2020; arXiv 2005.12574) | https://ar5iv.labs.arxiv.org/html/2005.12574 | what developers actually weigh when choosing a library (16 interviews, 115 survey responses) | SRC-S17 | - |
| REG-018 | T3 | Small World with High Risks: A Study of Security Threats in the npm Ecosystem | Zimmermann, Staicu, Tenny, Pradel (USENIX Security 2019; arXiv 1902.09217) | https://arxiv.org/abs/1902.09217 | maintainer concentration and unmaintained-vulnerable packages in npm | SRC-S18 | - |
| REG-019 | T3 | On the Impact of Micro-Packages: An Empirical Study of the npm JavaScript Ecosystem | Kula, Ouni, German, Inoue (arXiv 1709.04638) | https://arxiv.org/abs/1709.04638 | dependency chains and usage cost of micro-packages (abstract read, not full text) | SRC-S19 | - |
| REG-020 | T3 | Go Proverbs: "A little copying is better than a little dependency" | Rob Pike, Gopherfest 2015 | https://go-proverbs.github.io/ | the minority school favouring copying over small dependencies (proverb only, argument not read) | SRC-S20 | - |
| REG-021 | T4 | Vendor-lock-in and third-party API risk blog posts | various vendor blogs | search-result snippets only (truto.one, techconcepts.org, blog.apilayer.com), pages not fetched | live debate on API SLA, deprecation notice lengths and exit clauses; never sole ground | SRC-S21 | SRC-S21: no page read (search-result snippets only (truto.one, techconcepts.org, blog.apilayer.com), pages not fetched) |
| REG-022 | T1 | SLSA v1.0 threats overview | OpenSSF SLSA | https://slsa.dev/spec/v1.0/threats-overview | compromised or unavailable dependency threats | ADOPT-S03 | - |
| REG-023 | T1 | SLSA v1.0 about | OpenSSF SLSA | https://slsa.dev/spec/v1.0/about | scope: SLSA level independent of dependencies' levels / SLSA scope and limits | ADOPT-S04, DELIVER-S34 | - |
| REG-024 | T1 | OWASP Dependency-Check | OWASP | https://owasp.org/www-project-dependency-check/ | software composition analysis | ADOPT-S09 | - |
| REG-025 | T1 | OWASP Top 10:2025 A03 Software Supply Chain Failures | OWASP | https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures/ | prevention list for supply chain failures | ADOPT-S10 | - |
| REG-026 | T2 | Don't get locked up into avoiding lock-in | Gregor Hohpe, martinfowler.com | https://martinfowler.com/articles/oss-lockin.html | lock-in as spectrum, cost model / lock-in as priced trade-off | ADOPT-S11, EXT-S23 | - |
| REG-027 | T2 | In Defense of Not-Invented-Here Syndrome | Joel Spolsky | https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/ | build-own for core functions | ADOPT-S12 | - |
| REG-028 | T1 | Renovate docs, Dependency Pinning | Renovate maintainers | https://docs.renovatebot.com/dependency-pinning/ | pin apps, range libraries, lockfile limits | ADOPT-S13 | - |
| REG-029 | T1 | Dependabot options reference | GitHub | https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference | cooldown and groups | ADOPT-S14 | - |
| REG-030 | T1 | Semantic Versioning 2.0.0 | semver.org | https://semver.org/ | what SemVer promises / version number semantics | ADOPT-S15, DELIVER-S28 | - |
| REG-031 | T1 | npm package-lock.json | npm | https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json | lockfile purpose, commit, integrity | ADOPT-S16 | - |
| REG-032 | T1 | pip Secure installs | PyPA | https://pip.pypa.io/en/stable/topics/secure-installs/ | hash-checking mode | ADOPT-S17 | - |
| REG-033 | T2 | Strangler Fig Application | Martin Fowler | https://martinfowler.com/bliki/StranglerFigApplication.html | incremental replacement vs rewrite | ADOPT-S18 | - |
| REG-034 | T2 | Yagni | Martin Fowler | https://martinfowler.com/bliki/Yagni.html | costs of building what is not needed | ADOPT-S19 | - |
| REG-035 | T1 | Secure Supply Chain Consumption Framework (S2C2F) | OpenSSF | https://github.com/ossf/s2c2f/blob/main/specification/framework.md | consumption practices and maturity levels | ADOPT-S20 | - |
| REG-036 | T3 | We should all be using dependency cooldowns | William Woodruff | https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns | cooldown argument and data | ADOPT-S21 | - |
| REG-037 | T1 | Go Modules Reference | Go project | https://go.dev/ref/mod | MVS, go.sum, proxy immutability, vendoring | ADOPT-S22 | - |
| REG-038 | T1 | cargo-vet book | Mozilla | https://mozilla.github.io/cargo-vet/ | shared audits of dependencies | ADOPT-S23 | - |
| REG-039 | T2 | Hexagonal Architecture | Alistair Cockburn | https://alistair.cockburn.us/hexagonal-architecture/ | isolating the application from external technology | ADOPT-S24 | - |
| REG-040 | T3 | Cyber Resilience Act, Art. 13 as annotated | cyberresilienceact.eu | https://www.cyberresilienceact.eu/the-cyber-resilience-act/ | due diligence on third-party components (EUR-Lex fetch failed) | ADOPT-S25 | ADOPT-S25: tier recorded as "T3 (T1 content, unofficial copy)" |
| REG-041 | T1 | Reproducible Builds, Definition | reproducible-builds.org | https://reproducible-builds.org/docs/definition/ | verifying binaries against source | ADOPT-S26 | - |
| REG-042 | T1 | SBOM | CISA | https://www.cisa.gov/sbom | SBOM definition and use | ADOPT-S27 | - |
| REG-043 | T1 | Renovate, Minimum Release Age | Renovate maintainers | https://docs.renovatebot.com/key-concepts/minimum-release-age/ | delay of updates, security bypass | ADOPT-S29 | - |
| REG-044 | T2 | The Practical Test Pyramid | published on martinfowler.com | https://martinfowler.com/articles/practical-test-pyramid.html | test levels, duplication rules, contract tests, E2E cost | VERIFY-S01 | - |
| REG-045 | T3 | Just Say No to More End-to-End Tests | Google Testing Blog | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | 70/20/10 mix, E2E feedback cost | VERIFY-S02 | - |
| REG-046 | T3 | Testing of Microservices (honeycomb) | Spotify Engineering | https://engineering.atspotify.com/2018/01/testing-of-microservices | integration-heavy mix for microservices | VERIFY-S03 | - |
| REG-047 | T3 | The Testing Trophy and Testing Classifications | Kent C. Dodds | https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications | trophy, confidence vs investment | VERIFY-S04 | - |
| REG-048 | T2 | Software Engineering at Google, ch. 11 Testing Overview | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch11.html | why test, size vs scope, 80/15/5, flakiness, coverage | VERIFY-S05 | - |
| REG-049 | T2 | SWE at Google, ch. 12 Unit Testing | same | https://abseil.io/resources/swe-book/html/ch12.html | behavior tests, state vs interaction, DAMP | VERIFY-S06 | - |
| REG-050 | T2 | SWE at Google, ch. 13 Test Doubles | same | https://abseil.io/resources/swe-book/html/ch13.html | real > fake > mock, fidelity, ownership of fakes | VERIFY-S07 | - |
| REG-051 | T2 | SWE at Google, ch. 14 Larger Testing | same | https://abseil.io/resources/swe-book/html/ch14.html | fidelity, SUT options, A/B diff, canary, testing in production | VERIFY-S08 | - |
| REG-052 | T2 | SWE at Google, ch. 20 Static Analysis | same | https://abseil.io/resources/swe-book/html/ch20.html | Tricorder principles, false-positive threshold | VERIFY-S09 | - |
| REG-053 | T1 | Pact documentation | Pact Foundation | https://docs.pact.io/ | consumer-driven contract testing as designed | VERIFY-S10 | - |
| REG-054 | T2 | Eradicating Non-Determinism in Tests | martinfowler.com | https://martinfowler.com/articles/nonDeterminism.html | causes and remedies of flaky tests, quarantine | VERIFY-S11 | - |
| REG-055 | T3 | Flaky Tests at Google and How We Mitigate Them | Google Testing Blog | https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html | mitigation practice; fetch returned mostly reader comments, used only for corroboration, no claim rests on it | VERIFY-S12 | - |
| REG-056 | T2 | DORA capability: Test automation | DORA research program | https://dora.dev/capabilities/test-automation/ | evidence-backed test automation practices | VERIFY-S13 | - |
| REG-057 | T2 | DORA capability: Continuous integration | DORA | https://dora.dev/capabilities/continuous-integration/ | build and test on every commit, broken build priority / CI practice and metrics | VERIFY-S14, DELIVER-S16 | - |
| REG-058 | T3 | State of Mutation Testing at Google | Google Research | https://research.google/pubs/state-of-mutation-testing-at-google/ | mutation testing at scale (abstract read) | VERIFY-S15 | - |
| REG-059 | T2 | Test Coverage | Fowler, bliki | https://martinfowler.com/bliki/TestCoverage.html | coverage as diagnostic | VERIFY-S16 | - |
| REG-060 | T1 | Hypothesis documentation | Hypothesis maintainers | https://hypothesis.readthedocs.io/en/latest/index.html | property-based testing (overview page only) | VERIFY-S17 | - |
| REG-061 | T2 | Unit Test | Fowler, bliki | https://martinfowler.com/bliki/UnitTest.html | solitary vs sociable, definition | VERIFY-S18 | - |
| REG-062 | T2 | Mocks Aren't Stubs | Fowler | https://martinfowler.com/articles/mocksArentStubs.html | classical vs mockist | VERIFY-S19 | - |
| REG-063 | T2 | Self Testing Code | Fowler, bliki | https://martinfowler.com/bliki/SelfTestingCode.html | self-testing code, relation to CI | VERIFY-S20 | - |
| REG-064 | T2 | Is TDD Dead? | DHH, Beck, Fowler | https://martinfowler.com/articles/is-tdd-dead/ | the TDD debate from its principals | VERIFY-S21 | - |
| REG-065 | T3 | To Type or Not to Type: Quantifying Detectable Bugs in JavaScript | Gao, Bird, Barr, ICSE 2017 | https://janvitek.org/events/NEU/7575/pubs/no-type.pdf | empirical bug detection by static types | VERIFY-S22 | - |
| REG-066 | T1 | OSS-Fuzz documentation | Google / OSS-Fuzz | https://google.github.io/oss-fuzz/ | continuous fuzzing, results | VERIFY-S23 | - |
| REG-067 | T2 | SRE Book, Testing for Reliability | Google SRE | https://sre.google/sre-book/testing-reliability/ | test taxonomy, regression, canary, MTTR | VERIFY-S25 | - |
| REG-068 | T2 | Test Desiderata | Kent Beck | https://testdesiderata.com/ | twelve properties of valuable tests and their trade-offs | VERIFY-S26 | - |
| REG-069 | T3 | Principles of Chaos Engineering | chaos engineering community (originated at a streaming company) | https://principlesofchaos.org/ | production experiments / chaos engineering definition and principles | VERIFY-S27, OPERATE-S24 | - |
| REG-070 | T2 | Contract Test | Fowler, bliki | https://martinfowler.com/bliki/ContractTest.html | verifying doubles of external services | VERIFY-S28 | - |
| REG-071 | T2 | Hyrum's Law | Hyrum Wright | https://www.hyrumslaw.com/ | implicit interface, role of testing | VERIFY-S29 | - |
| REG-072 | T2 | Test Pyramid | Fowler, bliki | https://martinfowler.com/bliki/TestPyramid.html | pyramid, naming confusion, exceptions | VERIFY-S30 | - |
| REG-073 | T3 | Characterization Testing | Michael Feathers | https://michaelfeathers.silvrback.com/characterization-testing | tests that document actual behavior | VERIFY-S31 | - |
| REG-074 | T1 | PIT mutation testing | PIT maintainers | https://pitest.org/ | mutation vs line coverage | VERIFY-S32 | - |
| REG-075 | T1 | mypy documentation | mypy project | https://mypy.readthedocs.io/en/stable/index.html | gradual typing (Python) | VERIFY-S33 | - |
| REG-076 | T1 | OWASP Web Security Testing Guide | OWASP | https://owasp.org/www-project-web-security-testing-guide/ | read; page gave project info only, no claim drawn | VERIFY-S34 | - |
| REG-077 | T2 | Continuous Integration | Martin Fowler | https://martinfowler.com/articles/continuousIntegration.html | CI practices, integration styles / read for performance tests in pipeline: only dark launching mentioned; negative finding | DELIVER-S01, PERF-S16 | - |
| REG-078 | T2 | Trunk Based Development | Paul Hammant and contributors | https://trunkbaseddevelopment.com/ | trunk model, scale, release branches | DELIVER-S02 | - |
| REG-079 | T2 | Capabilities: Trunk-based Development | DORA | https://dora.dev/capabilities/trunk-based-development/ | thresholds, pitfalls | DELIVER-S03 | - |
| REG-080 | T2 | The Standard of Code Review | Google Engineering Practices | https://google.github.io/eng-practices/review/reviewer/standard.html | review approval standard | DELIVER-S04 | - |
| REG-081 | T2 | The Twelve-Factor App, V. Build, release, run | Adam Wiggins | https://12factor.net/build-release-run | stage separation, immutable releases | DELIVER-S05 | - |
| REG-082 | T2 | SRE book, ch. 8 Release Engineering | Google | https://sre.google/sre-book/release-engineering/ | hermetic builds, self-service release, branching | DELIVER-S06 | - |
| REG-083 | T2 | Software Engineering at Google, ch. 9 Code Review | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch09.html | review at scale | DELIVER-S07 | - |
| REG-084 | T2 | Software Engineering at Google, ch. 24 Continuous Delivery | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch24.html | velocity, flags, progressive rollout | DELIVER-S08 | - |
| REG-085 | T2 | Software Engineering at Google, ch. 23 Continuous Integration | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch23.html | presubmit, flakes, build cop | DELIVER-S09 | - |
| REG-086 | T1 | SLSA v1.0 Build track levels | OpenSSF / SLSA | https://slsa.dev/spec/v1.0/levels | build provenance levels / build platform requirements | DELIVER-S10, EXT-S20 | - |
| REG-087 | T2 | Blue Green Deployment | Martin Fowler | https://martinfowler.com/bliki/BlueGreenDeployment.html | blue-green and DB caveat / Schema deployed separately and before the application | DELIVER-S11, DATA-S03 | - |
| REG-088 | T2 | Canary Release | Danilo Sato, on martinfowler.com | https://martinfowler.com/bliki/CanaryRelease.html | canary definition and caveats | DELIVER-S12 | - |
| REG-089 | T2 | Feature Toggles | Pete Hodgson, on martinfowler.com | https://martinfowler.com/articles/feature-toggles.html | toggle categories and cost | DELIVER-S13 | - |
| REG-090 | T3 | A successful Git branching model (with 2020 note) | Vincent Driessen | https://nvie.com/posts/a-successful-git-branching-model/ | git-flow and its own scope limit | DELIVER-S14 | - |
| REG-091 | T1 | GitHub flow | GitHub Docs | https://docs.github.com/en/get-started/using-github/github-flow | PR-based lightweight flow | DELIVER-S15 | - |
| REG-092 | T2 | Capabilities: Deployment Automation | DORA | https://dora.dev/capabilities/deployment-automation/ | deployment automation | DELIVER-S17 | - |
| REG-093 | T2 | DORA software delivery metrics guide | DORA | https://dora.dev/guides/dora-metrics/ | five metrics, speed and stability / five delivery metrics incl. failed deployment recovery time | DELIVER-S18, OPERATE-S21 | - |
| REG-094 | T2 | Capabilities: Streamlining Change Approval | DORA | https://dora.dev/capabilities/streamlining-change-approval/ | CAB versus peer review | DELIVER-S19 | - |
| REG-095 | T2 | Capabilities: Version Control | DORA | https://dora.dev/capabilities/version-control/ | what goes into version control | DELIVER-S20 | - |
| REG-096 | T2 | Capabilities: Working in Small Batches | DORA | https://dora.dev/capabilities/working-in-small-batches/ | batch size | DELIVER-S21 | - |
| REG-097 | T2 | Capabilities: Continuous Delivery | DORA | https://dora.dev/capabilities/continuous-delivery/ | CD definition, enabling practices, J-curve | DELIVER-S22 | - |
| REG-098 | T2 | Ship / Show / Ask | Rouan Wilsenach, on martinfowler.com | https://martinfowler.com/articles/ship-show-ask.html | alternatives to mandatory review | DELIVER-S23 | - |
| REG-099 | T2 | Speed of Code Reviews | Google Engineering Practices | https://google.github.io/eng-practices/review/reviewer/speed.html | review latency | DELIVER-S25 | - |
| REG-100 | T2 | Small CLs | Google Engineering Practices | https://google.github.io/eng-practices/review/developer/small-cls.html | change size | DELIVER-S26 | - |
| REG-101 | T1 | OpenGitOps principles v1.0.0 | OpenGitOps (CNCF working group) | https://opengitops.dev/ | GitOps definition | DELIVER-S27 | - |
| REG-102 | T3 | Conventional Commits 1.0.0 | conventionalcommits.org | https://www.conventionalcommits.org/en/v1.0.0/ | commit message convention | DELIVER-S29 | - |
| REG-103 | T2 | Twelve-Factor, X. Dev/prod parity | Adam Wiggins | https://12factor.net/dev-prod-parity | parity gaps / time, personnel, tools gaps; backing service parity | DELIVER-S30, TRANS-S27 | - |
| REG-104 | T2 | SRE Workbook, Canarying Releases | Google | https://sre.google/workbook/canarying-releases/ | canary evaluation / canary metrics, limits of synthetic load | DELIVER-S31, PERF-S14 | - |
| REG-105 | T2 | Parallel Change | Danilo Sato, on martinfowler.com | https://martinfowler.com/bliki/ParallelChange.html | expand-migrate-contract / Expand, migrate, contract; drawbacks | DELIVER-S32, DATA-S02 | - |
| REG-106 | T2 | Software Engineering at Google, ch. 16 Version Control and Branch Management | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch16.html | one-version, monorepo, branches | DELIVER-S33 | - |
| REG-107 | T2 | Deployment Pipeline | Martin Fowler | https://martinfowler.com/bliki/DeploymentPipeline.html | pipeline stages | DELIVER-S35 | - |
| REG-108 | T3 | Expectations, Outcomes, and Challenges of Modern Code Review | Bacchelli and Bird, Microsoft Research (peer-reviewed) | https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/ | empirical purpose of review | DELIVER-S36 | - |
| REG-109 | T1 | About merge methods on GitHub | GitHub Docs | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github | merge, squash, rebase effects | DELIVER-S37 | - |
| REG-110 | T2 | Feature Branch | Martin Fowler | https://martinfowler.com/bliki/FeatureBranch.html | feature branch costs | DELIVER-S38 | - |
| REG-111 | T2 | Immutable Server | Kief Morris, on martinfowler.com | https://martinfowler.com/bliki/ImmutableServer.html | drift and immutable replacement | DELIVER-S39 | - |
| REG-112 | T2 | Frequency Reduces Difficulty | Martin Fowler | https://martinfowler.com/bliki/FrequencyReducesDifficulty.html | rationale for frequent releases | DELIVER-S40 | - |
| REG-113 | T2 | SRE book, Introduction | Google | https://sre.google/sre-book/introduction/ | change causes about 70% of outages / SRE tenets, monitoring outputs, playbooks, change as outage source | DELIVER-S41, OPERATE-S16 | - |
| REG-114 | T1 | About protected branches | GitHub Docs | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | branch protection controls | DELIVER-S42 | - |
| REG-115 | T3 | Automating safe, hands-off deployments | Amazon Builders' Library | https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments | one-box, waves, bake, auto rollback | DELIVER-S43 | - |
| REG-116 | T2 | On Pair Programming | Birgitta Boeckeler and Nina Siessegger, on martinfowler.com | https://martinfowler.com/articles/on-pair-programming.html | pairing versus review | DELIVER-S44 | - |
| REG-117 | T1 | Observability primer | OpenTelemetry | https://opentelemetry.io/docs/concepts/observability-primer/ | definitions of observability, telemetry, SLI, SLO, trace, span, log | OPERATE-S01 | - |
| REG-118 | T1 | Signals | OpenTelemetry | https://opentelemetry.io/docs/concepts/signals/ | signal set and stability (traces, metrics, logs, baggage, profiles) | OPERATE-S02 | - |
| REG-119 | T1 | Sampling | OpenTelemetry | https://opentelemetry.io/docs/concepts/sampling/ | head vs tail sampling, when to sample / sampling as cost control, head vs tail | OPERATE-S03, PERF-S26 | - |
| REG-120 | T1 | Semantic conventions | OpenTelemetry | https://opentelemetry.io/docs/concepts/semantic-conventions/ | common naming across signals | OPERATE-S04 | - |
| REG-121 | T1 | Instrumentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/instrumentation/ | zero-code vs code-based, library instrumentation | OPERATE-S05 | - |
| REG-122 | T1 | Trace Context | W3C (Recommendation, 2021) | https://www.w3.org/TR/trace-context/ | cross-vendor trace propagation headers | OPERATE-S06 | - |
| REG-123 | T1 | SP 800-61 Rev. 3, Incident Response Recommendations (landing page only) | NIST | https://csrc.nist.gov/pubs/sp/800/61/r3/final | incident response as part of risk management (CSF 2.0) | OPERATE-S07 | - |
| REG-124 | T2 | Monitoring Distributed Systems | Google SRE book | https://sre.google/sre-book/monitoring-distributed-systems/ | symptoms vs causes, golden signals, paging rules / black-box vs white-box, golden signals, percentiles | OPERATE-S08, PERF-S07 | - |
| REG-125 | T2 | Service Level Objectives | Google SRE book | https://sre.google/sre-book/service-level-objectives/ | SLI/SLO/SLA, target-setting / SLO versus SLA, actual versus stated / percentile targets, targets from user need | OPERATE-S09, EXT-S25, PERF-S09 | - |
| REG-126 | T2 | Postmortem Culture: Learning from Failure | Google SRE book | https://sre.google/sre-book/postmortem-culture/ | blameless postmortems, triggers | OPERATE-S10 | - |
| REG-127 | T2 | Managing Incidents | Google SRE book | https://sre.google/sre-book/managing-incidents/ | incident command roles, declaration, handoff | OPERATE-S11 | - |
| REG-128 | T2 | Embracing Risk | Google SRE book | https://sre.google/sre-book/embracing-risk/ | cost of reliability, error budgets | OPERATE-S12 | - |
| REG-129 | T2 | Eliminating Toil | Google SRE book | https://sre.google/sre-book/eliminating-toil/ | toil definition and 50% cap | OPERATE-S13 | - |
| REG-130 | T2 | Being On-Call | Google SRE book | https://sre.google/sre-book/being-on-call/ | on-call load, team size, alert/incident ratio / operational load limits, team size | OPERATE-S14, PERF-S10 | - |
| REG-131 | T2 | Practical Alerting from Time-Series Data | Google SRE book | https://sre.google/sre-book/practical-alerting/ | rule maintainability, black-box vs white-box / prober (synthetic checks), SLO alerting | OPERATE-S15, PERF-S08 | - |
| REG-132 | T2 | Alerting on SLOs | Google SRE workbook | https://sre.google/workbook/alerting-on-slos/ | burn-rate alerting strategies and thresholds | OPERATE-S17 | - |
| REG-133 | T2 | Example Error Budget Policy | Google SRE workbook | https://sre.google/workbook/error-budget-policy/ | budget exhaustion consequences | OPERATE-S18 | - |
| REG-134 | T2 | Implementing SLOs | Google SRE workbook | https://sre.google/workbook/implementing-slos/ | SLI specification vs implementation, journeys, windows | OPERATE-S19 | - |
| REG-135 | T2 | Postmortem Culture: Learning from Failure (workbook) | Google SRE workbook | https://sre.google/workbook/postmortem-culture/ | postmortem best practices and anti-patterns | OPERATE-S20 | - |
| REG-136 | T2 | Monitoring and observability capability | DORA | https://dora.dev/capabilities/monitoring-and-observability/ | monitoring vs observability, link to delivery performance | OPERATE-S22 | - |
| REG-137 | T2 | The Twelve-Factor App, XI. Logs | Heroku / Adam Wiggins | https://12factor.net/logs | logs as event streams | OPERATE-S23 | - |
| REG-138 | T3 | The USE Method | Brendan Gregg | https://www.brendangregg.com/usemethod.html | resource-level checks | OPERATE-S25 | - |
| REG-139 | T3 | The RED Method | Grafana Labs (Tom Wilkie) | https://grafana.com/blog/the-red-method-how-to-instrument-your-services/ | service-level standard metrics, on-call for code you did not write | OPERATE-S26 | - |
| REG-140 | T3 | Time to version observability (observability 2.0) | Honeycomb (Charity Majors) | https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes | wide-events position; a vendor-interested source | OPERATE-S27 | - |
| REG-141 | T3 | Rethinking observability (news report of Sigelman, Sridharan, Majors debate) | InfoQ | https://www.infoq.com/news/2019/02/rethinking-observability | the three-pillars critique and cost trade-off | OPERATE-S28 | - |
| REG-142 | T3 | Incident response documentation (landing page) | PagerDuty | https://response.pagerduty.com/ | role names and structure of a practiced process | OPERATE-S29 | - |
| REG-143 | T1 | doctest, Test interactive Python examples | Python Software Foundation | https://docs.python.org/3/library/doctest.html | executable docstring examples; limits of exact-output matching | TRANS-S01 | - |
| REG-144 | T1 | Documentation tests (rustdoc book) | Rust project | https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html | doc examples compiled and run by the test command | TRANS-S02 | - |
| REG-145 | T1 | About code owners | GitHub Docs | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | path-based reviewer assignment, required owner review | TRANS-S03 | - |
| REG-146 | T1 | sphinx-build options | Sphinx project | https://www.sphinx-doc.org/en/master/man/sphinx-build.html | fail-on-warning and nitpicky doc builds | TRANS-S04 | - |
| REG-147 | T1 | About Swagger Specification (OpenAPI 3.0) | SmartBear / OpenAPI tooling docs | https://swagger.io/docs/specification/v3_0/about/ | one machine-readable description driving docs, code, tests | TRANS-S05 | - |
| REG-148 | T1 | Documenting a feature for a release | Kubernetes project (SIG Docs) | https://kubernetes.io/docs/contribute/new-content/new-features/ | release-gated documentation process | TRANS-S06 | - |
| REG-149 | T1 | Vale documentation | Vale project | https://docs.vale.sh/ | prose linting as code, CI severity | TRANS-S07 | - |
| REG-150 | T2 | Software Engineering at Google, ch. 10 Documentation | Winters, Manshreck, Wright (Google) | https://abseil.io/resources/swe-book/html/ch10.html | docs as code, ownership, reviews, freshness | TRANS-S08 | - |
| REG-151 | T2 | Code Review Developer Guide, What to look for | Google eng-practices | https://google.github.io/eng-practices/review/reviewer/looking-for.html | reviewer duty on docs | TRANS-S09 | - |
| REG-152 | T2 | Documentation quality (capability) | DORA (Google Cloud) | https://dora.dev/capabilities/documentation-quality/ | documentation quality as amplifier of delivery capabilities | TRANS-S10 | - |
| REG-153 | T2 | Documentation workflow | GitLab Development handbook | https://docs.gitlab.com/development/documentation/workflow/ | docs in the MR, definition of done, roles, CI | TRANS-S11 | - |
| REG-154 | T2 | Documenting Architecture Decisions | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | short immutable decision records in the repo | TRANS-S12 | - |
| REG-155 | T2 | Principles behind the Agile Manifesto | Agile Alliance signatories | https://agilemanifesto.org/principles.html | minimal-documentation stance | TRANS-S13 | - |
| REG-156 | T3 | Docs as Code | Write the Docs | https://www.writethedocs.org/guide/docs-as-code/ | the docs-as-code philosophy | TRANS-S14 | - |
| REG-157 | T3 | Diátaxis (home and How to use Diátaxis) | Daniele Procida | https://diataxis.fr/ | structure by reader need; incremental workflow | TRANS-S15 | - |
| REG-158 | T3 | Spectral | Stoplight | https://github.com/stoplightio/spectral | linting API descriptions in CI | TRANS-S16 | - |
| REG-159 | T3 | lychee | lychee maintainers | https://github.com/lycheeverse/lychee | link checking and scheduled runs | TRANS-S17 | - |
| REG-160 | T3 | openapi-diff | OpenAPITools maintainers | https://github.com/OpenAPITools/openapi-diff | breaking-change detection with failing exit | TRANS-S18 | - |
| REG-161 | T3 | Danger | Danger maintainers | https://danger.systems/js/ | automating PR review chores | TRANS-S19 | - |
| REG-162 | T3 | Keep a Changelog 1.1.0 | Olivier Lacan | https://keepachangelog.com/en/1.1.0/ | changelog principles, Unreleased section | TRANS-S20 | - |
| REG-163 | T3 | Architectural Decision Records | ADR GitHub organization | https://adr.github.io/ | ADR practice, decision log | TRANS-S21 | - |
| REG-164 | T3 | Living Documentation, book review/interview (InfoQ Brazil) | Cyrille Martraire, via InfoQ | https://www.infoq.com/br/articles/book-review-living-documentation/ | living documentation (secondary: book not read) | TRANS-S22 | - |
| REG-165 | T2 | Threat Modeling Manifesto | practitioner authors (threatmodelingmanifesto.org) | https://www.threatmodelingmanifesto.org/ | threat modeling values, principles, four questions | TRANS-S24 | - |
| REG-166 | T1 | Secrets Management Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | secret centralization, lifecycle, detection, incident response | TRANS-S25 | - |
| REG-167 | T2 | The Twelve-Factor App, III. Config | Adam Wiggins et al. | https://12factor.net/config | config separation, env vars, no named environments | TRANS-S26 | - |
| REG-168 | T1 | Development Container Specification | containers.dev / Dev Container community | https://containers.dev/implementors/spec/ | devcontainer.json, features, lifecycle | TRANS-S29 | - |
| REG-169 | T1 | OWASP DevSecOps Guideline | OWASP | https://owasp.github.io/www-project-devsecops-guideline/latest | security testing stages in the pipeline | TRANS-S30 | - |
| REG-170 | T1 | About push protection | GitHub Docs | https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection | blocking secrets at push; bypass and audit | TRANS-S31 | - |
| REG-171 | T1 | OWASP SAMM model | OWASP | https://owaspsamm.org/model/ | maturity model: five functions, fifteen practices | TRANS-S32 | - |
| REG-172 | T1 | Secure by Design | CISA | https://www.cisa.gov/resources-tools/resources/secure-by-design | producer ownership, transparency, leadership | TRANS-S33 | - |
| REG-173 | T1 | Kubernetes Secrets | Kubernetes project | https://kubernetes.io/docs/concepts/configuration/secret/ | default-unencrypted caveat, hardening | TRANS-S34 | - |
| REG-174 | T1 | Kubernetes ConfigMaps | Kubernetes project | https://kubernetes.io/docs/concepts/configuration/configmap/ | config decoupled from images; consumption modes | TRANS-S35 | - |
| REG-175 | T1 | Vault, Lease, Renew, and Revoke | HashiCorp | https://developer.hashicorp.com/vault/docs/concepts/lease | dynamic secrets, TTL, revocation | TRANS-S36 | - |
| REG-176 | T1 | OpenID Connect in GitHub Actions | GitHub Docs | https://docs.github.com/en/actions/concepts/security/openid-connect | short-lived federated CI credentials | TRANS-S37 | - |
| REG-177 | T1 | Automatic token authentication (GITHUB_TOKEN) | GitHub Docs | https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication | least-privilege CI token | TRANS-S38 | - |
| REG-178 | T1 | Reproducible scripts (pinning Nixpkgs) | nix.dev | https://nix.dev/tutorials/first-steps/reproducible-scripts | pinned package set reproducibility | TRANS-S39 | - |
| REG-179 | T3 | Lessons from Building Static Analysis Tools at Google | Sadowski et al., CACM | https://research.google/pubs/lessons-from-building-static-analysis-tools-at-google/ | static analysis in developer workflow | TRANS-S40 | - |
| REG-180 | T1 | OWASP Application Security Verification Standard | OWASP | https://owasp.org/www-project-application-security-verification-standard/ | verifiable web-app security requirements (levels not read) | TRANS-S41 | - |
| REG-181 | maintainer | the maintainer's codified practice (guidelines, architecture notes, migration and delivery guide, validator readme, work-thinking philosophy) | maintainer | none (private files, not citable) | what this maintainer requires in verification, delivery, operation, tooling choice and documentation, and why | MAINT-S01 | - |
| REG-182 | T1 | RFC 9745 The Deprecation HTTP Response Header Field | IETF | https://www.rfc-editor.org/rfc/rfc9745.html | signalling resource deprecation | EXT-S01 | - |
| REG-183 | T1 | RFC 8594 The Sunset HTTP Header Field | IETF | https://www.rfc-editor.org/rfc/rfc8594.html | signalling retirement time | EXT-S02 | - |
| REG-184 | T1 | RFC 9110 HTTP Semantics (section 9.2.2 excerpt only) | IETF | https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods | idempotent methods and automatic retry | EXT-S03 | - |
| REG-185 | T1 | Circuit Breaker pattern | Microsoft Azure Architecture Center | https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker | breaker states, when not to use | EXT-S04 | - |
| REG-186 | T1 | Anti-Corruption Layer pattern | Microsoft Azure Architecture Center | https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer | isolating external systems | EXT-S05 | - |
| REG-187 | T1 | Data Act explained (Commission factpage; regulation text on EUR-Lex not read) | European Commission | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | cloud switching, egress charges, export format | EXT-S06 | - |
| REG-188 | T1 | GNU General Public License FAQ | Free Software Foundation | https://www.gnu.org/licenses/gpl-faq.html | GPL compatibility, linking, server use | EXT-S07 | - |
| REG-189 | T1 | GNU Affero General Public License v3 (section 13) | Free Software Foundation | https://www.gnu.org/licenses/agpl-3.0.html | network copyleft | EXT-S08 | - |
| REG-190 | T1 | The Open Source Definition | Open Source Initiative | https://opensource.org/osd | what counts as open source | EXT-S09 | - |
| REG-191 | T1 | SPDX specification 2.3.1, license expressions | SPDX / Linux Foundation | https://spdx.github.io/spdx-spec/v2.3.1/SPDX-license-expressions/ | machine-readable licence expression | EXT-S10 | - |
| REG-192 | T1 | REUSE specification 3.3 | FSFE | https://reuse.software/spec-3.3/ | per-file licence declaration | EXT-S11 | - |
| REG-193 | T1 | OpenChain ISO/IEC 5230 (project page, not the standard text) | OpenChain Project / ISO | https://www.openchainproject.org/license-compliance | open-source compliance programme | EXT-S12 | - |
| REG-194 | T1 | OWASP API Security Top 10 2023, API10 Unsafe Consumption of APIs | OWASP | https://api-security.owasp.org/editions/2023/en/0xaa-unsafe-consumption-of-apis | consuming third-party APIs safely | EXT-S13 | - |
| REG-195 | T1 | Security hardening for GitHub Actions | GitHub Docs | https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions | third-party actions, tokens, runners | EXT-S14 | - |
| REG-196 | T1 | NIST SP 800-161 Rev.1 C-SCRM (abstract page) | NIST | https://csrc.nist.gov/pubs/sp/800/161/r1/final | supplier risk management | EXT-S15 | - |
| REG-197 | T1 | Amazon EC2 Service Level Agreement | AWS | https://aws.amazon.com/compute/sla/ | structure of a cloud SLA | EXT-S16 | - |
| REG-198 | T1 | GDPR Article 28 (unofficial copy of the regulation text) | EU, via gdpr-info.eu | https://gdpr-info.eu/art-28-gdpr/ | processor contract terms | EXT-S17 | - |
| REG-199 | T1 | Secure by Demand Guide | CISA | https://www.cisa.gov/resources-tools/resources/secure-demand-guide | questions to put to software vendors | EXT-S18 | - |
| REG-200 | T1 | Supply chain compromise of third-party GitHub Action CVE-2025-30066 | CISA | https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066 | CI-service supply-chain incident | EXT-S19 | - |
| REG-201 | T1 | Reliability in Azure (shared responsibility, SLAs) | Microsoft | https://learn.microsoft.com/en-us/azure/architecture/best-practices/retry-service-specific | provider versus customer reliability duties | EXT-S21 | - |
| REG-202 | T1 | Apache License v2.0 and GPL compatibility | Apache Software Foundation | https://www.apache.org/licenses/GPL-compatibility.html | direction of Apache 2.0 / GPL compatibility | EXT-S22 | - |
| REG-203 | T2 | Addressing Cascading Failures, Google SRE book | Google | https://sre.google/sre-book/addressing-cascading-failures/ | retries, deadlines, load shedding / load testing to failure, limits of capacity planning | EXT-S24, PERF-S04 | - |
| REG-204 | T2 | AIP-180 Backwards compatibility | Google API Improvement Proposals | https://google.aip.dev/180 | what counts as breaking | EXT-S26 | - |
| REG-205 | T2 | AIP-194 Automatic retry configuration | Google API Improvement Proposals | https://google.aip.dev/194 | which errors are retryable | EXT-S28 | - |
| REG-206 | T2 | Idempotency-Key HTTP Header Field, Internet-Draft 07 (expired) | IETF httpapi WG | https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ | keyed retry of POST | EXT-S29 | - |
| REG-207 | T2 | The Twelve-Factor App, IV Backing services | Adam Wiggins / Heroku | https://12factor.net/backing-services | services as attached resources | EXT-S30 | - |
| REG-208 | T2 | Tolerant Reader | Martin Fowler | https://martinfowler.com/bliki/TolerantReader.html | consumer side of evolution | EXT-S31 | - |
| REG-209 | T2 | Circuit Breaker | Martin Fowler (crediting Nygard, Release It) | https://martinfowler.com/bliki/CircuitBreaker.html | breaker, monitoring, fallback | EXT-S32 | - |
| REG-210 | T2 | Third-party licenses policy | Google Open Source | https://opensource.google/documentation/reference/thirdparty/licenses | an organization's licence classes | EXT-S33 | - |
| REG-211 | T3 | Timeouts, retries and backoff with jitter | Amazon Builders' Library | https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter | retry practice, timeouts | EXT-S34 | - |
| REG-212 | T3 | HashiCorp adopts Business Source License | HashiCorp | https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license | a vendor's relicensing and rationale | EXT-S35 | - |
| REG-213 | T3 | APIs as infrastructure: future-proofing Stripe with versioning | Stripe | https://stripe.com/blog/api-versioning | date-based versions, long compatibility | EXT-S36 | - |
| REG-214 | T3 | FinOps principles | FinOps Foundation | https://www.finops.org/framework/principles/ | owning technology cost | EXT-S37 | - |
| REG-215 | T4 | OpenTofu Manifesto | OpenTofu signatories | https://opentofu.org/manifesto/ | the community side of the relicensing debate | EXT-S38 | - |
| REG-216 | T4 | Search-result summaries on SaaS lock-in assessment and DORA exit strategies (aggregator and vendor sites, pages not opened) | various | search results only | only to flag unread topics; never cited as ground | EXT-S39 | EXT-S39: no page read (search results only) |
| REG-217 | T2 | Launch Coordination Checklist (SRE book appendix) | Google SRE | https://sre.google/sre-book/launch-checklist/ | launch readiness checklist domains | PERF-S01 | - |
| REG-218 | T2 | Reliable Product Launches at Scale (SRE book) | Google SRE | https://sre.google/sre-book/reliable-product-launches/ | checklist design, rigor vs velocity, gradual rollout | PERF-S02 | - |
| REG-219 | T2 | Evolving SRE Engagement Model (SRE book, production readiness review) | Google SRE | https://sre.google/sre-book/evolving-sre-engagement-model/ | production readiness review | PERF-S03 | - |
| REG-220 | T2 | Handling Overload (SRE book) | Google SRE | https://sre.google/sre-book/handling-overload/ | capacity in resources, load shedding, retry budgets | PERF-S05 | - |
| REG-221 | T2 | Software Engineering in SRE (SRE book) | Google SRE | https://sre.google/sre-book/software-engineering-in-sre/ | capacity planning and intent-based planning | PERF-S06 | - |
| REG-222 | T2 | Emergency Response (SRE book) | Google SRE | https://sre.google/sre-book/emergency-response/ | preparation, rehearsal, testing response | PERF-S11 | - |
| REG-223 | T2 | Effective Troubleshooting (SRE book) | Google SRE | https://sre.google/sre-book/effective-troubleshooting/ | playbook linked from alert, investigation logs | PERF-S12 | - |
| REG-224 | T2 | Introducing Non-Abstract Large System Design (SRE Workbook ch. 12) | Google SRE | https://sre.google/workbook/non-abstract-design/ | resource planning from requirements and failure domains | PERF-S13 | - |
| REG-225 | T2 | Using load shedding to avoid overload (Amazon Builders' Library) | Amazon | https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload | overload tests, goodput | PERF-S15 | - |
| REG-226 | T1 | Architecture strategies for performance testing (PE:06), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/performance-test | performance test practice, budgets, types, production testing | PERF-S17 | - |
| REG-227 | T1 | Architecture strategies for capacity planning (PE:02), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/capacity-planning | capacity planning method | PERF-S18 | - |
| REG-228 | T1 | Designing a reliability testing strategy (RE:08), Azure Well-Architected | Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/reliability/reliability-test | load and scaling response, runbook validation, DR tests | PERF-S19 | - |
| REG-229 | T1 | REL07-BP04 Load test your workload, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_load_tested_adapt.html | load test anti-patterns | PERF-S20 | - |
| REG-230 | T1 | PERF05-BP04 Load test your workload, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html | load test steps, pipeline integration | PERF-S21 | - |
| REG-231 | T1 | OPS07-BP02 Ensure a consistent review of operational readiness, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_const_orr.html | operational readiness review | PERF-S22 | - |
| REG-232 | T1 | Operational Readiness Reviews (ORR) whitepaper, introduction only | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html | origin and purpose of ORR | PERF-S23 | - |
| REG-233 | T1 | OPS07-BP03 Use runbooks to perform procedures, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html | runbooks | PERF-S24 | - |
| REG-234 | T1 | OPS07-BP04 Use playbooks to investigate issues, AWS Well-Architected | AWS | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_playbooks.html | playbooks | PERF-S25 | - |
| REG-235 | T1 | Instrumentation practices, Prometheus documentation | Prometheus | https://prometheus.io/docs/practices/instrumentation/ | label cardinality, instrumentation overhead | PERF-S27 | - |
| REG-236 | T1 | CloudWatch Synthetics canaries, AWS documentation | AWS | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html | what synthetic monitors do (one tool) | PERF-S28 | - |
| REG-237 | T1 | Application Observability cost optimization, Grafana Cloud documentation | Grafana Labs | https://grafana.com/docs/grafana-cloud/monitor-applications/application-observability/optimize-costs/ | telemetry cost drivers and trade-offs (one tool) | PERF-S29 | - |
| REG-238 | T1 | Load test types, Grafana k6 documentation | Grafana Labs | https://grafana.com/docs/k6/latest/testing-guides/test-types/ | smoke, load, stress, spike, soak, breakpoint | PERF-S30 | - |
| REG-239 | T3 | Coordinated Omission (mechanical-sympathy group post) | G. Tene | https://groups.google.com/g/mechanical-sympathy/c/icNZJejUHfE/m/BfDekfBEs_sJ | coordinated omission in load measurement | PERF-S31 | - |
| REG-240 | T3 | Performance budgets 101 | web.dev (Google) | https://web.dev/articles/performance-budgets-101 | client-side performance budgets in CI | PERF-S32 | - |
| REG-241 | T3 | Revisiting Knuth's "Premature Optimization" Paper (secondary; the 1974 paper itself not read) | probablydance.com, via search summary | https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/ | context of the premature-optimization quote | PERF-S33 | - |
| REG-242 | T3 | Benchmarks in CI without noise (vendor blog), search summary only, page not fetched | CodSpeed | https://codspeed.io/blog/benchmarks-in-ci-without-noise | variance of benchmarks on shared CI runners | PERF-S34 | - |
| REG-243 | T4 | Synthetic vs real user monitoring (vendor pages), search summary only | SpeedCurve and others | https://www.speedcurve.com/web-performance-guide/synthetic-vs-real-user-monitoring/ | live debate and definitions of real-user monitoring | PERF-S35 | - |
| REG-244 | T2 | Evolutionary Database Design, Fowler and Sadalage | - | https://martinfowler.com/articles/evodb.html | Authoritative on: migrations as first-class artifacts, small changes, per-developer databases, transition phase, data-fix folder, reverse migrations stance | DATA-S01 | - |
| REG-245 | T1 | Database change management capability, DORA | - | https://dora.dev/capabilities/database-change-management/ | Version-controlled scripts, sequencing, online schema tools, parallel change, expert communication | DATA-S04 | - |
| REG-246 | T1 | Explicit Locking (PostgreSQL docs) | - | https://www.postgresql.org/docs/current/explicit-locking.html | ACCESS EXCLUSIVE semantics | DATA-S05 | - |
| REG-247 | T1 | ALTER TABLE (PostgreSQL docs) | - | https://www.postgresql.org/docs/current/sql-altertable.html | Rewrites, NOT VALID, lock levels | DATA-S06 | - |
| REG-248 | T1 | Client connection defaults: lock_timeout and statement_timeout (PostgreSQL docs) | - | https://www.postgresql.org/docs/current/runtime-config-client.html | - | DATA-S07 | - |
| REG-249 | T1 | InnoDB Online DDL operations (MySQL 8.4 docs) | - | https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html | - | DATA-S08 | - |
| REG-250 | T2 | Data Integrity: What You Read Is What You Wrote (Google SRE book ch. 26) | - | https://sre.google/sre-book/data-integrity/ | Defense in depth, restores, soft deletion, validation pipelines | DATA-S09 | - |
| REG-251 | T1 | Undo migrations (Flyway documentation, Redgate) | - | https://documentation.red-gate.com/flyway/flyway-concepts/migrations/undo-migrations | - | DATA-S10 | - |
| REG-252 | T1 | Rollback (Liquibase documentation) | - | https://docs.liquibase.com/concepts/changelogs/rollback.html | - | DATA-S11 | - |
| REG-253 | T1 | Declarative vs Versioned migrations (Atlas) | - | https://atlasgo.io/concepts/declarative-vs-versioned | - | DATA-S12 | - |
| REG-254 | T1 | Best Practices (Apache Airflow docs) | - | https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html | Idempotent, bounded tasks; pipeline stack | DATA-S13 | - |
| REG-255 | T3 | Migration style guide (GitLab development docs) | - | https://docs.gitlab.com/development/migration_style_guide/ | - | DATA-S14 | - |
| REG-256 | T3 | gh-ost: GitHub's online migration tool for MySQL (GitHub blog) | - | https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/ | - | DATA-S15 | - |
| REG-257 | T3 | Online migrations at scale (Stripe blog) | - | https://stripe.com/blog/online-migrations | - | DATA-S16 | - |
| REG-258 | T3 | Strong Migrations README (maintainer of the tool) | - | https://github.com/ankane/strong_migrations | Ruby on Rails with Postgres, MySQL | DATA-S17 | - |
| REG-259 | T3 | Squawk README | - | https://github.com/sbdchd/squawk | Postgres | DATA-S18 | - |
| REG-260 | T3 | Expand and contract pattern (Prisma Data Guide) | - | https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern | - | DATA-S19 | - |
| REG-261 | T3 | DBLab Engine docs (Postgres.ai) | - | https://postgres.ai/docs/database-lab | Vendor | DATA-S20 | - |
| REG-262 | T3 | Environments with masked production data (Neon blog) | - | https://neon.com/blog/environments-masked-production-data | Vendor | DATA-S21 | - |
| REG-263 | T2 | Database Refactoring (Ambler and Sadalage) | - | http://databaserefactoring.com/ | Definition and catalog only; the page did not discuss transition periods | DATA-S22 | - |
| REG-264 | T2 | Designing Data-Intensive Applications, ch. 4 | Kleppmann | none (O'Reilly fetch returned 403; search-result summary only) | not read; used for inferred pointers only (backward and forward compatibility during rolling upgrades) | DATA-S23 | DATA-S23: no page read (none (O'Reilly fetch returned 403; search-result summary only)) |
