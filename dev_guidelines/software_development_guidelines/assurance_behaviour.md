# Assurance: Behaviour

## Table of Contents

1. [Behaviour](#behaviour) _(Lines 21-23)_
   1. [What the Suite Must Promise](#what-the-suite-must-promise) _(Lines 26-40)_
   1. [Static Layer](#static-layer) _(Lines 43-55)_
   1. [Test Level Mix](#test-level-mix) _(Lines 58-71)_
   1. [Test Construction](#test-construction) _(Lines 74-89)_
   1. [Tests Driven by Change](#tests-driven-by-change) _(Lines 92-102)_
   1. [Measuring Adequacy and Probing for Faults](#measuring-adequacy-and-probing-for-faults) _(Lines 105-118)_
   1. [Tests Without Durable Effect on Data](#tests-without-durable-effect-on-data) _(Lines 121-137)_
   1. [Defect Classes That Survive Review](#defect-classes-that-survive-review) _(Lines 140-150)_

---

Part of [Assurance](assurance.md). How a team shows that software does what it should, change after change.

## Behaviour
<!-- Lines 21-23 -->

The software is self-testing: an automated suite runs on every change and a pass means no substantial defects. Types and static checks are the cheapest blocking layer, the mix of test levels is chosen for confidence per unit of time, tests observe behaviour and are built as production code, and tests are triggered by change events. The suite's power is measured rather than assumed, no test leaves a durable effect on data, and defect classes that survive review are caught on production-shaped data. Tests run in the environments defined in [transverse.md](transverse.md). `ASSURANCE.BEHAVIOUR`

### What the Suite Must Promise
<!-- Lines 26-40 -->

Code is self-testing: the suite can be run at any time and on every change, and a pass means no substantial defects; without that there is no continuous integration. Everything the team does not want to break has a test, in the strict form where criticality is high or consumers are many, otherwise as enough tests to change the code confidently. The suite is judged by what it detects, not what it executes.

Rules:
- The suite MUST run on every change and be runnable in the language's standard way.
- A written test policy MUST exist: new functionality and every fix come with automated tests. The evidence is the tests in each change, visible in its review; no separate artefact.
- The suite MUST have an accountable owner and its results MUST be recorded.
- A pass MUST NOT be read as proof of reliability.

Best instead when:
- The strict form (every behaviour, performance, accessibility and security property tested): high criticality or many consumers.
- On-demand runs without an automatic trigger: only for one-off code never changed again.

Exploratory and usability testing cannot be automated and complement the suite. Open: whether a given team has an automated trigger today is for the team to check. Requires [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped) and [Trustworthy Signal](assurance_rules.md#trustworthy-signal); refines [One Bar and Evidence for Every Change](assurance_rules.md#one-bar-and-evidence-for-every-change); realised in [Build and Pipeline](change_flow_delivery.md#build-and-pipeline). `ASSURANCE.BEHAVIOUR.1`

### Static Layer
<!-- Lines 43-55 -->

Type checking, linting and analysis are the first and cheapest test layer and run on every change. Type checks, compiler warnings and the adopted linter rules block; analyses whose findings need judgement advise in review, each under the false-alarm budget of [Trustworthy Signal](assurance_rules.md#trustworthy-signal). Builds treat warnings as errors, and at least one analyser beyond compiler warnings runs before a major release. Analysis is incremental and reports newly introduced issues first.

Rules:
- Type checks, compiler warnings and adopted linter rules MUST block; judgement analyses MUST advise.
- A warning MUST be fixed or suppressed with a reason.

Types are enforced from the start for large long-lived code and introduced gradually on existing code (an escape hatch while migrating): two stages of one route, not rivals.

Best instead when: tests alone suffice for small, short-lived code where annotation cost exceeds the defects prevented.

Requires [Gates That Cannot Be Skipped](assurance_rules.md#gates-that-cannot-be-skipped); refined for security by [Static and Scheduled Analysis Practice](assurance_docs_security.md#static-and-scheduled-analysis-practice). `ASSURANCE.BEHAVIOUR.2`

### Test Level Mix
<!-- Lines 58-71 -->

The mix of small, integrated and end-to-end tests follows from placing each check at the lowest level that catches its failure. Where logic lives inside units: many small fast tests, progressively fewer broader ones. Where failures arise between services: weight on integration tests. For user-interface code: static checks plus integration tests. End-to-end tests stay few and on critical journeys. The proportions are recorded as a team decision with the reason; exact ratios matter less than fast, reliable tests with meaningful failures.

Rules:
- The mix MUST be recorded.
- End-to-end tests MUST be few and for critical journeys unless fast, reliable and cheap.

Best instead when:
- A fixed ratio such as 70/20/10: only with the infrastructure of the organisation that states it.
- A wider middle (interactions) or a heavy integration layer: complexity lives in interactions, or the code is user-interface.
- Many end-to-end tests: they are fast, reliable and cheap to change.

Larger tests are added where fidelity matters (configuration, load, cross-service behaviour). Follows from [Placement and Feedback Speed](assurance_rules.md#placement-and-feedback-speed); seams between services are served by [Contract Tests](assurance_interfaces_data.md#contract-tests). `ASSURANCE.BEHAVIOUR.3`

### Test Construction
<!-- Lines 74-89 -->

A test observes behaviour through the public interface, one test per behaviour, and changes only when requirements change. Test code is production code: readable and descriptive over strictly DRY, no loops or conditionals, one condition per test. Real collaborators are used when fast, deterministic and simple; otherwise a fake owned by the team that owns the real thing; mocks and stubs last. Integration tests run against a real backing service of the production kind. A test reports its own verdict in a fixed, searchable shape, lives where it changes together with its unit, and sets fixture values once by name.

Rules:
- The double style and the unit definition MUST be recorded.
- A test MUST NOT change when only structure changes.
- Integration tests MUST use the production kind of backing service.

Best instead when:
- Mockist style as default: outside-in design with costly collaborators.
- Interaction verification: state-changing calls not otherwise observable.
- A mirrored test tree: the language has a test runner; colocated tests where tooling lacks one.
- A lighter engine in integration tests: the production engine cannot run locally or in CI.

Open: the classical-versus-mockist default, the verdict shape and test location are inferred. A fake of an external service needs the contract test of [Contract Tests](assurance_interfaces_data.md#contract-tests). The mix is held in [Test Level Mix](#test-level-mix). `ASSURANCE.BEHAVIOUR.4`

### Tests Driven by Change
<!-- Lines 92-102 -->

Every reported defect becomes a test that fails first and passes after the fix. Poorly understood code is pinned by characterization tests of its actual behaviour before it is changed. A scheduled job is tested before it is scheduled like any other unit, and its first runs on real data are bounded and inspected. Writing tests before code is a team decision by context; what is required is that the test exists, was seen to fail for the right reason where it guards a fix, and runs on every change. A gap found by an experiment in production is such a defect ([Verifying Resilience Under Real Conditions](assurance_performance_availability.md#verifying-resilience-under-real-conditions)).

Rules:
- A fixed defect MUST have a regression test.
- A scheduled job MUST pass its tests before it is scheduled.

Best instead when: mandatory test-first for compilers, interface design and tangled interfaces, where fast design feedback pays; elsewhere the order is free.

Requires [What the Suite Must Promise](#what-the-suite-must-promise); where scheduled jobs sit is in [construction.md](construction.md). `ASSURANCE.BEHAVIOUR.5`

### Measuring Adequacy and Probing for Faults
<!-- Lines 105-118 -->

Coverage finds code no test executes. It is never a quality score, a merge gate or a target, and no numeric floor applies to security-relevant code either. For security-relevant code the requirement is fuzzing of input-handling code, tests derived from threats and past bugs, and review of every unexecuted security-relevant branch coverage reveals. Detection power is probed directly: mutation testing where criticality is high and the suite is mature, property-based testing for code with a describable input range. This node is the one location of the coverage decision.

Rules:
- A coverage number MUST NOT gate a merge, set a quality target or serve as a security floor.
- Input-handling code of security relevance MUST be fuzzed.

Best instead when:
- A coverage threshold: only as management visibility for low-trust or fast-growing teams.
- A fixed statement-coverage minimum: as conformance only, where a security baseline or contract mandates the number (not a quality claim).
- Skipping mutation testing: compute or noise dominates, or the suite is immature (mutating a weak suite measures nothing).

Open: the effect size of mutation and property-based testing is unmeasured; the rule for security-relevant code is inferred. The principle that adequacy is judged by detection is in [What the Suite Must Promise](#what-the-suite-must-promise); [Verification Techniques](assurance_docs_security.md#verification-techniques) states no coverage figure of its own. `ASSURANCE.BEHAVIOUR.6`

### Tests Without Durable Effect on Data
<!-- Lines 121-137 -->

A test never leaves a durable effect on data that anyone relies on. The default is a separate disposable data store per run, never the production one, with each test isolated. Running on shared or production-sized data is best only when the dataset cannot be cloned or its shapes synthesized and the platform can undo every effect of the test. No test, functional or experimental, runs against production data unless every durable effect is provably undone: its records isolated and marked apart from real data and removed after the run, other durable effects (sequences, notifications, external calls) suppressed or undone.

Rules:
- A test MUST NOT commit a durable change to shared data.
- A mutating automated test on shared or production-sized data MUST run as one rolled-back unit.
- A test on production data MUST isolate and mark its records and remove them after the run.
- Production code MUST NOT read the test namespace; test data and configuration are kept apart from production.
- Test records are synthetic and built per test by default; a curated, catalogued set of real records only where shapes are rich and costly to fabricate. Real records stay under [the privacy rules](transverse_privacy.md#privacy-and-retention).
- Choose the vehicle by risk: read-only tests as plain queries; tests that can mutate or fail, when automated, as one atomic rolled-back unit; an open-transaction wrapper only for a person at the keyboard. Shaping mutations are conditional on an actual change so re-runs behave identically.

Best instead when:
- Rollback on shared data as the general rule: exactly under its stated condition (data large, shapes unsynthesizable, platform can undo every effect).
- Synthetic records as the only source: small domain, easy shapes.

Load and locks are transient effects, governed by the guardrails of [Verifying Resilience Under Real Conditions](assurance_performance_availability.md#verifying-resilience-under-real-conditions), not by this node. Open: the choice of records, vehicle and conditional mutations are inferred. Meets [Trustworthy Signal](assurance_rules.md#trustworthy-signal): the rollback is the platform undo. `ASSURANCE.BEHAVIOUR.7`

### Defect Classes That Survive Review
<!-- Lines 140-150 -->

Passing review, static analysis and deployment is not evidence that code works. Code whose behaviour depends on the shape of the data (queries, parsing, conversions, platforms that coerce or truncate) is exercised on production-shaped data, edge values included, before it ships, beyond the parsing at the boundary held in [Parse or Validate at the Edge](construction.md#parse-or-validate-at-the-edge). A platform limit that fails silently has a check. Unclear platform behaviour a design relies on is verified empirically and recorded with its scope. A pitfall catalogue grows after any defect found twice. A blanket search-and-replace is never applied across a file that holds two syntactic contexts.

Rules:
- Data-dependent code MUST be exercised on production-shaped data before it ships.
- A platform limit that fails silently MUST have a check.
- A pitfall found twice MUST be catalogued.

Best instead when: static analysis and types alone are best for the part they catch (name and type errors), which is why they stay the first layer ([Static Layer](#static-layer)).

Open: the five practices rest on a single team's experience; one dated study shows only that static checks miss a run-time class of defect. `ASSURANCE.BEHAVIOUR.8`
