# VERIFY — how a team knows it works at each level and keeps working

## L1 headline

Best practice on verification agrees on direction (automated, fast, self-testing suites; many cheap narrow tests, few expensive broad ones; flaky tests intolerable; every bug becomes a test) but stays contested on the shape of the mix, on mocking, on TDD and on contract-test style; certainty is high on the consensus claims (grounded in T1/T2 sources read in full or in the relevant section) and medium on proportions, which sources give as team-dependent.

Pinned:
- Sources by tier: T1: 7, T2: 19, T3: 8, T4: 0 (34 in total; one T1, OWASP WSTG, was read but yielded no usable claim).
- Claims: 44.
- Contested topics: test-level shape (pyramid vs honeycomb vs trophy); classical vs mockist test doubles; TDD as mandatory practice; consumer-driven contracts vs provider schema; coverage as target vs diagnostic; mutation testing as routine gate.
- Failed T1 fetches: NIST SP 800-218 landing page gave metadata only (the PDF from the same site was then read in full via local text extraction); OWASP WSTG page gave no SDLC claims (not recovered). Non-T1 failures: UCL copy of the Gao et al. paper (403) and a connection error on a second host (the paper was read from a third copy); an O'Reilly page for Feathers (403, replaced by his own essay on characterization tests); Fowler's microservice-testing article returned only its agenda (not used).

## L2 claims

Clusters (agreement, certainty, ids):
1. Tests exist to make change safe, not only to catch bugs; self-testing code is the base of CI and CD. Consensus, grounded. VERIFY-C01, C02, C03, C04.
2. Static analysis and type checking are the cheapest, earliest verification layer; adopt gradually, keep false positives low, show results in review. Majority (types contested in magnitude), grounded. C05, C06, C07, C08, C09.
3. Use a mix of test levels, many narrow/fast and few broad/slow; exact proportions are team-specific and the shape is debated. Consensus on direction, contested on shape, grounded. C10, C11, C12, C13, C14, C15.
4. Test observable behavior through public interfaces; prefer real collaborators, then fakes, mocks last; keep tests readable (DAMP). Majority, grounded. C16, C17, C18, C19, C20, C21, C22.
5. Contracts at service boundaries: verify consumer/provider agreement by test, not by end-to-end environments; verify doubles against the real thing. Majority, grounded. C23, C24, C25, C26.
6. Regression: every escaped bug becomes a test; legacy code gets characterization tests before change. Consensus, grounded. C27, C28, C29.
7. Suite health: fast, deterministic, isolated; quarantine flakes with a bound; coverage is a diagnostic, mutation testing the stronger signal. Consensus on flakes, contested on coverage and mutation. Grounded. C30, C31, C32, C33, C34, C35.
8. Beyond example-based tests: property-based testing and fuzzing find what authors do not imagine; required by security frameworks for input-handling code. Majority, grounded. C36, C37.
9. Verification continues in production (large tests for fidelity, canary, A/B diff, config checks, chaos experiments) because pre-production cannot reach full fidelity. Majority, grounded. C38, C39, C40, C41.
10. Verification practice is a risk-scaled choice recorded by the team (which test types, at what stage, by what policy). Principle, inferred from SSDF PW.7/PW.8, Beck desiderata, Fowler. C42, C43, C44.

Live debates (forces in tension):
- Pyramid vs honeycomb vs trophy: confidence and refactor-safety (integration-heavy) against speed of feedback and diagnosability (unit-heavy).
- Classical vs mockist doubles: refactor-safety and integration confidence against isolation, precise failure location and outside-in design pressure.
- TDD as mandatory vs optional: speed of feedback and design pressure against cost of ownership (indirection, "test-induced design damage") and team cognitive load.
- Consumer-driven contracts vs provider schema: team autonomy and precision of what is used against the cost of running a broker and tests per consumer.
- Coverage as target vs diagnostic: management visibility and a floor against gaming; mutation testing: stronger signal against compute and noise cost.
- Types: bug-prevention (15% of public JS bugs in one study) and documentation against annotation cost and friction on dynamic code.
- Testing in production: fidelity against user impact and test-data pollution.

Candidate central decisions (others depend on them):
1. The target mix of test levels and what counts as a "unit" (solitary or sociable), recorded per system.
2. Policy on test doubles: real, fake, mock; who owns fakes.
3. Gate policy: what must pass before merge and before release, and the time budget (about ten minutes is the cited ceiling); flaky-test quarantine rules.
4. How service boundaries are verified: consumer-driven contracts, provider schema, or shared-environment end-to-end.
5. Whether and how static types and static analysis are enforced (blocking vs advisory, false-positive threshold).
6. What is verified in production and with what blast radius (canary, A/B diff, chaos).
7. Whether TDD is a team rule, a tool, or left open; what replaces coverage as the health signal.

Not covered: accessibility, performance and load testing in depth, security testing beyond SSDF and fuzzing (sibling TRANS and DELIVER own the rest), formal methods, model checking, visual/snapshot regression, test data management, AI-generated tests, ML-system testing, exploratory testing practice, OWASP WSTG content, microservice testing detail from Fowler (agenda only), stack-specific runners.

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| VERIFY-S01 | T2 | The Practical Test Pyramid | published on martinfowler.com | https://martinfowler.com/articles/practical-test-pyramid.html | test levels, duplication rules, contract tests, E2E cost |
| VERIFY-S02 | T3 | Just Say No to More End-to-End Tests | Google Testing Blog | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | 70/20/10 mix, E2E feedback cost |
| VERIFY-S03 | T3 | Testing of Microservices (honeycomb) | Spotify Engineering | https://engineering.atspotify.com/2018/01/testing-of-microservices | integration-heavy mix for microservices |
| VERIFY-S04 | T3 | The Testing Trophy and Testing Classifications | Kent C. Dodds | https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications | trophy, confidence vs investment |
| VERIFY-S05 | T2 | Software Engineering at Google, ch. 11 Testing Overview | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch11.html | why test, size vs scope, 80/15/5, flakiness, coverage |
| VERIFY-S06 | T2 | SWE at Google, ch. 12 Unit Testing | same | https://abseil.io/resources/swe-book/html/ch12.html | behavior tests, state vs interaction, DAMP |
| VERIFY-S07 | T2 | SWE at Google, ch. 13 Test Doubles | same | https://abseil.io/resources/swe-book/html/ch13.html | real > fake > mock, fidelity, ownership of fakes |
| VERIFY-S08 | T2 | SWE at Google, ch. 14 Larger Testing | same | https://abseil.io/resources/swe-book/html/ch14.html | fidelity, SUT options, A/B diff, canary, testing in production |
| VERIFY-S09 | T2 | SWE at Google, ch. 20 Static Analysis | same | https://abseil.io/resources/swe-book/html/ch20.html | Tricorder principles, false-positive threshold |
| VERIFY-S10 | T1 | Pact documentation | Pact Foundation | https://docs.pact.io/ | consumer-driven contract testing as designed |
| VERIFY-S11 | T2 | Eradicating Non-Determinism in Tests | martinfowler.com | https://martinfowler.com/articles/nonDeterminism.html | causes and remedies of flaky tests, quarantine |
| VERIFY-S12 | T3 | Flaky Tests at Google and How We Mitigate Them | Google Testing Blog | https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html | mitigation practice; fetch returned mostly reader comments, used only for corroboration, no claim rests on it |
| VERIFY-S13 | T2 | DORA capability: Test automation | DORA research program | https://dora.dev/capabilities/test-automation/ | evidence-backed test automation practices |
| VERIFY-S14 | T2 | DORA capability: Continuous integration | DORA | https://dora.dev/capabilities/continuous-integration/ | build and test on every commit, broken build priority |
| VERIFY-S15 | T3 | State of Mutation Testing at Google | Google Research | https://research.google/pubs/state-of-mutation-testing-at-google/ | mutation testing at scale (abstract read) |
| VERIFY-S16 | T2 | Test Coverage | Fowler, bliki | https://martinfowler.com/bliki/TestCoverage.html | coverage as diagnostic |
| VERIFY-S17 | T1 | Hypothesis documentation | Hypothesis maintainers | https://hypothesis.readthedocs.io/en/latest/index.html | property-based testing (overview page only) |
| VERIFY-S18 | T2 | Unit Test | Fowler, bliki | https://martinfowler.com/bliki/UnitTest.html | solitary vs sociable, definition |
| VERIFY-S19 | T2 | Mocks Aren't Stubs | Fowler | https://martinfowler.com/articles/mocksArentStubs.html | classical vs mockist |
| VERIFY-S20 | T2 | Self Testing Code | Fowler, bliki | https://martinfowler.com/bliki/SelfTestingCode.html | self-testing code, relation to CI |
| VERIFY-S21 | T2 | Is TDD Dead? | DHH, Beck, Fowler | https://martinfowler.com/articles/is-tdd-dead/ | the TDD debate from its principals |
| VERIFY-S22 | T3 | To Type or Not to Type: Quantifying Detectable Bugs in JavaScript | Gao, Bird, Barr, ICSE 2017 | https://janvitek.org/events/NEU/7575/pubs/no-type.pdf (text extracted locally) | empirical bug detection by static types |
| VERIFY-S23 | T1 | OSS-Fuzz documentation | Google / OSS-Fuzz | https://google.github.io/oss-fuzz/ | continuous fuzzing, results |
| VERIFY-S24 | T1 | NIST SP 800-218 SSDF v1.1 | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf (PW.6, PW.7, PW.8 read) | code analysis and executable testing as normative practices |
| VERIFY-S25 | T2 | SRE Book, Testing for Reliability | Google SRE | https://sre.google/sre-book/testing-reliability/ | test taxonomy, regression, canary, MTTR |
| VERIFY-S26 | T2 | Test Desiderata | Kent Beck | https://testdesiderata.com/ (redirect from the GitHub pages URL) | twelve properties of valuable tests and their trade-offs |
| VERIFY-S27 | T3 | Principles of Chaos Engineering | chaos engineering community (originated at a streaming company) | https://principlesofchaos.org/ | production experiments |
| VERIFY-S28 | T2 | Contract Test | Fowler, bliki | https://martinfowler.com/bliki/ContractTest.html | verifying doubles of external services |
| VERIFY-S29 | T2 | Hyrum's Law | Hyrum Wright | https://www.hyrumslaw.com/ | implicit interface, role of testing |
| VERIFY-S30 | T2 | Test Pyramid | Fowler, bliki | https://martinfowler.com/bliki/TestPyramid.html | pyramid, naming confusion, exceptions |
| VERIFY-S31 | T3 | Characterization Testing | Michael Feathers | https://michaelfeathers.silvrback.com/characterization-testing | tests that document actual behavior |
| VERIFY-S32 | T1 | PIT mutation testing | PIT maintainers | https://pitest.org/ | mutation vs line coverage |
| VERIFY-S33 | T1 | mypy documentation | mypy project | https://mypy.readthedocs.io/en/stable/index.html | gradual typing (Python) |
| VERIFY-S34 | T1 | OWASP Web Security Testing Guide | OWASP | https://owasp.org/www-project-web-security-testing-guide/ | read; page gave project info only, no claim drawn |

### Claims

**Purpose and base**

- id: VERIFY-C01
  claim: Tests should be written first to make change safe and speed iteration; bug-catching is secondary.
  level: principle; stack: neutral; sources: S05 (Why Test); S20 (confidence to change); agreement: consensus; certainty: grounded.
- id: VERIFY-C02
  claim: Code should be self-testing: a team must be able to run an automated suite at any time and trust that passing means free of substantial defects; without it there is no real continuous integration.
  level: principle; stack: neutral; sources: S20; S14; S13 ("when tests pass we should be confident the software is releasable"); agreement: consensus; certainty: grounded.
- id: VERIFY-C03
  claim: Everything the team does not want to break (behavior, performance, accessibility, security) should have a test (the Beyoncé rule).
  level: principle; stack: neutral; sources: S05 (Beyoncé Rule); agreement: majority (single formulation, other sources consistent); certainty: grounded.
  positions: stated as a rule at Google; Fowler's weaker form is "enough tests if you can confidently change the code" (S21), which scales it to risk; context where the strict form wins: high criticality, many consumers.
- id: VERIFY-C04
  claim: Passing tests do not prove reliability; failing tests prove its absence, so tests are a filter that blocks bugs before production (zero repair time for what is caught).
  level: principle; stack: neutral; sources: S25 (Mean Time to Repair); agreement: consensus; certainty: grounded.

**Static analysis and types**

- id: VERIFY-C05
  claim: Treat type checking and linting as the first, cheapest test layer, run on every change.
  level: decision; stack: neutral; sources: S04 (static tier); S22 (15% of sampled public bugs detectable by Flow or TypeScript on code that had survived tests and review; the paper calls this a conservative lower bound); S33; agreement: majority; certainty: grounded.
  positions: (a) enforce types (Gao et al., Dodds; serves correctness, documentation; wins where the code base is large and long-lived); (b) optional or gradual (mypy; serves delivery speed and adoption on existing code); (c) tests alone suffice (no source read holding this strongly; recorded as the unrepresented minority, open).
- id: VERIFY-C06
  claim: Adopt static typing gradually where code already exists: annotate incrementally and keep an escape hatch rather than rewriting.
  level: practice; stack: Python (mypy), TypeScript/Flow (gradual); sources: S33; S22 (gradual systems); agreement: consensus within gradual-typing tools; certainty: grounded.
- id: VERIFY-C07
  claim: Static-analysis checks must have a low effective false-positive rate (below 10% at Google, about 5% achieved), where a false positive is any finding the developer does not act on; a noisy check is removed or fixed.
  level: practice; stack: neutral; sources: S09 (Tricorder); agreement: majority (one large-scale source; SSDF S24 PW.7.2 ex. 4 requires a human reviewing tool findings, consistent); certainty: grounded.
- id: VERIFY-C08
  claim: Analysis should be incremental (changed files), report newly introduced issues first, appear in code review, and offer automated fixes.
  level: practice; stack: neutral; sources: S09 (Scalability, Usability, Code review is a sweet spot, Fix suggestions); agreement: majority; certainty: grounded. boundary: DELIVER (code review).
- id: VERIFY-C09
  claim: Build and compile with warnings enabled and treated as errors ("clean build"); use analysis tools to find unsafe practices continuously.
  level: practice; stack: neutral (compiler specifics vary); sources: S24 (PW.6.2 ex. 2; PW.7.2 ex. 4, 6); agreement: majority; certainty: grounded. boundary: DELIVER.

**Test level mix**

- id: VERIFY-C10
  claim: Prefer many small, fast, narrow tests and progressively fewer, broader, slower ones; avoid the inverted "ice-cream cone".
  level: principle; stack: neutral; sources: S01 (Where to test); S02; S05; S30; agreement: consensus on direction; certainty: grounded.
- id: VERIFY-C11
  claim: The proportions of the mix are a decision each team records; the named references differ.
  level: decision; stack: neutral; sources: S02 (70/20/10, "the exact mix will be different for each team"); S05 (80/15/5); S03; S04; agreement: contested.
  positions: (a) pyramid, unit-heavy (Google, Fowler): speed of feedback, precise failure location; wins with logic-dense code, large teams, slow environments. (b) honeycomb, integration-heavy, few implementation-detail tests, ideally no integrated tests (Spotify): refactor-safety, database migrations or refactors without test edits, at the cost of seconds instead of milliseconds; wins for microservices where complexity lives in interactions. (c) trophy, static plus integration widest (Dodds): "the more tests resemble how software is used, the more confidence", return = confidence per unit time; wins for UI/front-end applications. All three say the exact numbers matter less than fast, reliable, meaningful-failure tests.
- id: VERIFY-C12
  claim: When a higher-level test finds a bug that no lower-level test caught, add the lower-level test; push each check as low as it can go.
  level: practice; stack: neutral; sources: S01 (Avoiding Test Duplication); S30 (second line of defense); agreement: consensus; certainty: grounded.
- id: VERIFY-C13
  claim: Keep end-to-end tests to a bare minimum because they are slow, flaky and delay feedback; keep a few that cover critical user journeys.
  level: decision; stack: neutral; sources: S01; S02; S30; S05 (5%); agreement: majority; certainty: grounded.
  positions: Fowler (S30) also states that if high-level tests are fast, reliable and cheap to change, lower-level tests are unnecessary; so E2E-minimal wins when E2E is slow or flaky, and loses where it is cheap and stable.
- id: VERIFY-C14
  claim: Describe tests on separate axes: size (resources: process, machine) and scope (code paths verified); "end-to-end", "UI" and "customer-facing" are independent characteristics, not synonyms.
  level: practice; stack: neutral; sources: S05 (Test Size vs Scope); S30 (naming confusion); agreement: consensus; certainty: grounded.
- id: VERIFY-C15
  claim: "Unit" is team-defined; the team should state whether units are solitary (collaborators doubled) or sociable (real collaborators) and where tests start and stop.
  level: decision; stack: neutral; sources: S18; S03 (terminology of integrated vs integration); agreement: contested (see C19); certainty: grounded.

**Test design**

- id: VERIFY-C16
  claim: Test observable behavior through public interfaces, not implementation details; the ideal test never changes unless requirements change.
  level: principle; stack: neutral; sources: S06 (public API, unchanging test); S05 (Behaviors, Not Methods); S26 (structure-insensitive); S03; agreement: consensus; certainty: grounded.
- id: VERIFY-C17
  claim: Prefer state verification over interaction verification, except to check state-changing calls that cannot be observed otherwise.
  level: practice; stack: neutral; sources: S06 (State vs Interaction); S07; S19; agreement: majority; certainty: grounded. positions: mockists (S19) hold interaction verification promotes need-driven design and isolates failures.
- id: VERIFY-C18
  claim: Use real implementations when fast, deterministic and simple; otherwise a fake owned and maintained by the team owning the real thing; mocks and stubs last, because over-mocking produced tests that were easy to write, costly to maintain and rarely found bugs.
  level: decision; stack: neutral; sources: S07 (real first choice; fakes; risks of over-mocking); S06; agreement: majority; certainty: grounded.
- id: VERIFY-C19
  claim: Choose and record a double style: classical (real objects unless awkward) or mockist (mock every collaborator with behavior).
  level: decision; stack: neutral; sources: S19; S18; S07; agreement: contested.
  positions: classical (Fowler, Google): catches integration errors, does not couple to implementation, survives refactors; wins where refactoring is frequent and object graphs are small. Mockist: failures are local to the buggy unit, simpler fixtures, outside-in design with role interfaces, Tell-Don't-Ask; wins when drives design from outside in and collaborators are costly to build. Fowler: "convinced classicist", but notes many skilled practitioners prefer mockist.
- id: VERIFY-C20
  claim: Tests are code: keep them readable and DAMP (descriptive, meaningful phrases) rather than strictly DRY; no loops or conditionals in tests; one condition per test; arrange, act, assert.
  level: practice; stack: neutral; sources: S06 (DAMP, No Logic); S01 (Clean Test Code); agreement: consensus; certainty: grounded.
- id: VERIFY-C21
  claim: Judge a test by trade-offs among twelve properties (isolated, composable, deterministic, fast, writable, readable, behavioral, structure-insensitive, automated, specific, predictive, inspiring); no test needs all, and some pairs conflict (predictive vs fast).
  level: principle; stack: neutral; sources: S26; agreement: majority (single author, reflected elsewhere); certainty: grounded.
- id: VERIFY-C22
  claim: Whether TDD is required is a team decision; all principals agree on self-testing code and disagree on whether test-first mechanics deliver it.
  level: decision; stack: neutral; sources: S21; S13 (DORA recommends developers writing unit tests before production code); S20 ("TDD is one way to achieve self-testing code"); agreement: contested.
  positions: Beck: context decides, wins for compilers, API design, tangled interfaces, gives rapid design feedback. DHH: overprescriptive, induces indirection and "test-induced design damage" for MVC web apps; serves cost of ownership. Fowler: valuable in some contexts, over-testing is a tuning problem. DORA (S13): practice recommended, evidence is of test automation in general, not of test-first ordering specifically (inferred from page text).

**Contracts and boundaries**

- id: VERIFY-C23
  claim: Between services with independent release, verify compatibility with contract tests so teams can deploy autonomously, instead of relying on shared integrated environments.
  level: decision; stack: neutral; sources: S01 (Contract tests, autonomous teams); S10; S03 (integrated tests to be avoided); agreement: majority; certainty: grounded.
- id: VERIFY-C24
  claim: Contract style is a decision: consumer-driven (contracts generated by consumer tests, provider free to change what no consumer uses) or provider-side schema validation.
  level: decision; stack: neutral (Pact is a tool); sources: S10 (Pact vs OpenAPI-style specs; provider-only testing "does not provide test-based assurance that consumers call the provider correctly"); S01; agreement: contested.
  positions: consumer-driven (Pact, Fowler): precision on what is used, safe evolution, wins with many consumers under internal control. Provider schema: lower setup cost, a published spec for unknown consumers (inferred; the Pact source is the party arguing against it, so the strongest version of this side is not independently sourced: open).
- id: VERIFY-C25
  claim: Every double of an external service should be backed by a contract test against the real service on its own cadence (for example daily); such a failure triggers coordination with the supplier and need not break the build.
  level: practice; stack: neutral; sources: S28; S11 (Remote Services); agreement: majority; certainty: grounded.
- id: VERIFY-C26
  claim: Because users depend on all observable behavior (Hyrum's Law), broad automated tests can detect new implicit dependencies but cannot remove them; plan API change accordingly.
  level: principle; stack: neutral; sources: S29; agreement: consensus (widely cited, one source read); certainty: grounded. boundary: ADOPT (living with dependencies).

**Regression and legacy**

- id: VERIFY-C27
  claim: Convert every reported bug into a test that fails first and passes after the fix, building the regression suite from operational experience.
  level: practice; stack: neutral; sources: S25 (Bug-as-Test); S24 (PW.8.2 ex. 3: tests for previously reported vulnerabilities); S30; agreement: consensus; certainty: grounded.
- id: VERIFY-C28
  claim: Before changing poorly understood code, pin down its actual behavior with characterization tests; production code is its own specification.
  level: practice; stack: neutral; sources: S31; agreement: majority (one primary source, consistent with S20 on legacy fear); certainty: grounded.
- id: VERIFY-C29
  claim: Include performance regression tests and production-side configuration checks so slow drift and misconfiguration do not pass unnoticed.
  level: practice; stack: neutral; sources: S25 (Performance, Configuration tests); S08 (configuration changes among top outage causes at Google); agreement: majority; certainty: grounded.

**Suite health**

- id: VERIFY-C30
  claim: A test failure must mean a real defect; flaky tests are not tolerated: at about 1% flakiness tests lose value (Google holds about 0.15%).
  level: principle; stack: neutral; sources: S13; S05 (Flaky Tests); S11; agreement: consensus; certainty: grounded.
- id: VERIFY-C31
  claim: Quarantine non-deterministic tests in a separate suite outside the deployment gate, with a numeric cap and a time limit (the source example: 8 tests, one week), and fix or delete them.
  level: practice; stack: neutral; sources: S11 (Quarantine Strategy); S12 (marking flaky tests, selective reruns); agreement: majority; certainty: grounded. positions: Google runs reruns only for tests marked flaky (S12, from commenters, weak); the strict school removes them immediately (inferred from S13 "do not tolerate").
- id: VERIFY-C32
  claim: Remove the causes of flakiness: isolate tests and rebuild state instead of cleaning up, poll or use callbacks instead of bare sleeps, wrap the clock, double remote services, and shrink the scope of large tests.
  level: practice; stack: neutral; sources: S11; S08 (Flaky Large Tests); agreement: consensus; certainty: grounded.
- id: VERIFY-C33
  claim: Keep the automated suite fast: developers should get feedback in under ten minutes; a build should trigger on every commit; fixing a broken build takes priority.
  level: practice; stack: neutral; sources: S13; S14; agreement: consensus; certainty: grounded. boundary: DELIVER (CI).
- id: VERIFY-C34
  claim: Use coverage to find untested code, not as a target or quality score.
  level: decision; stack: neutral; sources: S16; S05 (Code Coverage); S32 (coverage only identifies code definitely not tested); agreement: contested.
  positions: diagnostic only (Fowler, Google, PIT): coverage is easy to inflate with low-quality tests; wins when teams are mature. A floor/threshold (Google notes coverage as "floor" in the sense of a minimum, not goal): serves management visibility; wins in low-trust or fast-growing teams (inferred from S05 wording).
- id: VERIFY-C35
  claim: Mutation testing gives a stronger measure than coverage of whether tests detect faults; at scale apply it diff-based and selectively.
  level: decision; stack: neutral (tools per language, PIT for JVM); sources: S15 (diff-based, about 30% of diffs with coverage, shown in mandatory review); S32; agreement: contested.
  positions: routine gate or review signal (Google, PIT): serves correctness, wins with high-criticality code and mature suites; skip or run offline (inferred): serves cost, wins where compute or noise dominates. The Google abstract gives no effect-size, so evidence of benefit is open.

**Beyond example tests**

- id: VERIFY-C36
  claim: Use property-based testing for code with a describable input range to expose edge cases examples miss.
  level: practice; stack: neutral (Hypothesis in Python; equivalents elsewhere); sources: S17 (overview page only); agreement: majority; certainty: grounded for the definition; the effectiveness claim is inferred (page does not quantify it).
- id: VERIFY-C37
  claim: Fuzz input-handling code, continuously where possible; frameworks require it for security-relevant code.
  level: practice; stack: C/C++, Rust, Go, Python, JVM, JS, Lua (OSS-Fuzz); sources: S23 (over 10,000 vulnerabilities and 36,000 bugs, 1,000 projects, as of August 2023); S24 (PW.8.2 ex. 5); agreement: majority; certainty: grounded.

**Production and fidelity**

- id: VERIFY-C38
  claim: Add larger tests where fidelity matters (configuration, load, cross-service behavior), choosing the system-under-test option (single process to production) by the fidelity versus flakiness cost.
  level: decision; stack: neutral; sources: S08 (Fidelity, SUT Options); agreement: majority; certainty: grounded. positions: hermetic single-process wins on speed and determinism; multimachine/shared environments win on fidelity at the cost of flakiness and conflicts.
- id: VERIFY-C39
  claim: Compare old and new versions on identical traffic (A/B diff) and use canary analysis to catch regressions before full rollout.
  level: practice; stack: neutral; sources: S08; S25 (canary); agreement: majority; certainty: grounded. boundary: DELIVER (rollout), OPERATE.
- id: VERIFY-C40
  claim: Testing in production is valuable and risky: issues found there already affect users, and test data can become visible; limit blast radius and isolate test data.
  level: decision; stack: neutral; sources: S08 (Testing in Production, Webdriver Torso incident); S27 (minimize blast radius); agreement: majority; certainty: grounded.
- id: VERIFY-C41
  claim: For distributed systems, run automated experiments against a steady-state hypothesis, preferably on production traffic, with the blast radius minimized.
  level: decision; stack: neutral; sources: S27; agreement: contested (source states production preference; not corroborated by a T1/T2 source here).
  positions: production experiments (chaos principles): authenticity; wins with mature observability and rollback. Pre-production only: serves safety; wins in regulated or low-recovery systems (inferred, unsourced: open).

**Risk-scaled policy**

- id: VERIFY-C42
  claim: Decide, per stage and per risk, which analysis and test types are performed, and record the policy.
  level: principle; stack: neutral; sources: S24 (PW.7.1, PW.8.1: determine whether and which testing, by stage and policy); agreement: consensus; certainty: grounded.
- id: VERIFY-C43
  claim: Developers primarily own authoring and maintaining automated acceptance tests; testers add exploratory and usability testing and curate suites.
  level: practice; stack: neutral; sources: S13 (Who Writes Tests); agreement: majority; certainty: grounded.
- id: VERIFY-C44
  claim: Record test results, root causes and triage of findings in the team's workflow; take the target production stack into account in test plans.
  level: practice; stack: neutral; sources: S24 (PW.7.2, PW.8.2 ex. 4, 7, 8); agreement: consensus within the framework; certainty: grounded.

### Gaps

- Open: strongest source-grounded case for "types optional" or "tests instead of types" (no T1-T3 source read argues it directly).
- Open: strongest case for provider-schema contracts and for non-production-only chaos.
- Open: evidence that mutation testing improves outcomes (Google abstract reports adoption, not effect).
- Open: quantitative flakiness data from the Google flaky-tests post (fetch returned comments, not the post).
- Open: Fowler microservice-testing article (levels incl. component tests) not read beyond its agenda; level naming "component test" is thus not sourced.
- Not covered: see L2 "Not covered".
