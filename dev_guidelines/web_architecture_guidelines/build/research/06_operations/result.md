# Research result: OPS (Operations: observability, testing, delivery, performance)

## L1 headline

Best practice for operating a web app is mature and largely consensual (correlated logs, metrics and traces across tiers via W3C Trace Context; a test pyramid with a real database; build once and promote an immutable release; migrations as an automated, backward-compatible release step; explicit HTTP caching plus measure-first performance work), with one live disagreement (where config lives) and one maturity gap (browser-side OpenTelemetry is officially experimental); certainty is grounded for nearly all claims, inferred for the few that adapt generic sources to a three-tier JS + Python + Postgres app.

Pinned:
- Sources: 36 (T1: 18, T2: 16, T3: 2, T4: 0).
- Claims: 53 (OPS-C01 to OPS-C53).
- Contested topics: config storage (environment variables vs versioned config files).
- Failed T1 fetches: none. Caveat: the fetch tool returns a model-condensed rendering of each page, not raw text; quotes below are as returned and not byte-verified against the originals.

## L2 claims

Clusters (agreement, certainty, ids):

1. Observability is three correlated signals tied together by one trace context propagated browser to server to database-adjacent calls, with trace and span ids in every log record. Consensus, grounded. C01, C02, C03, C06, C07.
2. Logs are an event stream written to stdout and routed by the environment; they never contain secrets and are protected against injection. Consensus, grounded. C04, C05 (boundary SEC), C10, C11 (boundary SEC).
3. Browser tracing is the weak link: OpenTelemetry for the browser is officially experimental, so the browser-to-server correlation must not depend on it alone (Server-Timing and a propagated header are the stable bridges). Consensus on the status, inferred on the fallback. C08, C17 (boundary API).
4. Monitor from the user's side: four golden signals, percentiles not averages, few SLOs, pages only for actionable user-visible conditions, black-box plus white-box. Consensus, grounded. C12 to C16, C22.
5. Sampling is a decision: head sampling is simple, tail sampling is needed to keep errors and slow traces at scale. Majority (single authoritative source, no dissent), grounded. C09.
6. Performance work starts with measurement; field (real-user) data outranks lab data; Core Web Vitals at the 75th percentile are the default targets. Consensus, grounded. C19, C20, C21 (boundary UI), C18 (boundary DATA), C23.
7. Testing follows a pyramid: many fast low-level tests, a few integration tests against a real database like production, very few end-to-end tests on critical journeys, contract tests for the seams. Consensus, grounded; its application to a single-team three-tier app is inferred. C24 to C31 (C28, C29 boundary API).
8. Delivery: one codebase, many deploys; strict build/release/run separation; config separate from code; dev/prod parity including the same database engine; staged automated pipeline; small frequent releases; feature flags decouple deploy from release. Consensus, grounded. C32, C33, C34, C36, C37, C42, C43, C44.
9. Migrations are an automated, version-controlled, small, backward-compatible release step, applied by the same process in every environment (expand, migrate, contract). Consensus, grounded. C38, C39, C40 (boundary DATA), C41.
10. Processes are stateless, start fast and shut down gracefully so releases and scaling are cheap. Consensus, grounded. C45, C46 (boundary APP).
11. HTTP caching first: explicit Cache-Control on every response; fingerprinted assets cached for a year; HTML revalidated; personalized or authorized responses kept out of shared caches; Vary where representation differs. Consensus, grounded. C47 to C50 (C49 boundary SEC).
12. Application caches must be shared across processes, vary on auth state, and have an explicit expiry or invalidation plan. Consensus on the first two, inferred on the third. C51, C52, C53.

Live debates:
- Config storage: Twelve-Factor says environment variables only; Google SRE release engineering keeps config in reviewed source control, packaged or external (C35).
- Test mix: shape agreed, ratios are team-specific (70/20/10 is an example, not a rule); Fowler allows dropping lower tests if high-level tests are fast, reliable and cheap (C24).
- Browser tracing: standards-track but experimental; whether to adopt it now or rely on RUM libraries plus a correlation header is open (C08).
- Contract tests in a single-team monolith: sources target independently deployed services; value for one browser client plus one server is inferred only (C29).

Not covered (gaps, see L3): database-side trace correlation (SQL comment tagging), log retention and cost, incident response and on-call, load and performance testing methods, CDN and edge caching, security testing in the pipeline (SEC), infrastructure as code and container build practice, schema-migration locking behavior in Postgres (DATA), T4 debates (testing trophy, microservice testing styles).

## L3 full

### Source register

All URLs were read (fetched) in this session. Authority column says what the source is authoritative on.

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| OPS-S01 | T1 | Trace Context | W3C | https://www.w3.org/TR/trace-context/ | traceparent/tracestate headers, privacy and DoS considerations |
| OPS-S02 | T1 | Signals | OpenTelemetry | https://opentelemetry.io/docs/concepts/signals/ | the three signals and baggage |
| OPS-S03 | T1 | Context propagation | OpenTelemetry | https://opentelemetry.io/docs/concepts/context-propagation/ | propagators, W3C default |
| OPS-S04 | T1 | Logs specification | OpenTelemetry | https://opentelemetry.io/docs/specs/otel/logs/ | TraceId/SpanId in log records, log appenders |
| OPS-S05 | T1 | Sampling | OpenTelemetry | https://opentelemetry.io/docs/concepts/sampling/ | head vs tail sampling |
| OPS-S06 | T1 | JavaScript browser getting started | OpenTelemetry | https://opentelemetry.io/docs/languages/js/getting-started/browser/ | browser instrumentation maturity |
| OPS-S07 | T1 | Zero-code instrumentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/instrumentation/zero-code/ | automatic vs code-based instrumentation |
| OPS-S08 | T1 | General metric semantic conventions | OpenTelemetry | https://opentelemetry.io/docs/specs/semconv/general/metrics/ | consistent attribute naming (read, little usable content; no claim rests on it) |
| OPS-S09 | T1 | HTTP caching | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching | Cache-Control, validation, busting, Vary |
| OPS-S10 | T1 | RFC 9111 HTTP Caching | IETF | https://www.rfc-editor.org/rfc/rfc9111.html | cache semantics, Authorization, Vary, no-store |
| OPS-S11 | T1 | Web Vitals | web.dev (Google) | https://web.dev/articles/vitals | Core Web Vitals thresholds, 75th percentile |
| OPS-S12 | T1 | Lab and field data differences | web.dev | https://web.dev/articles/lab-and-field-data-differences | lab vs field (RUM) data |
| OPS-S13 | T1 | Prevent unnecessary network requests with the HTTP Cache | web.dev | https://web.dev/articles/http-cache | cache policy decision for versioned vs unversioned URLs |
| OPS-S14 | T1 | Testing in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/testing/overview/ | test database, transaction isolation |
| OPS-S15 | T1 | Django's cache framework | Django docs | https://docs.djangoproject.com/en/stable/topics/cache/ | cache levels, backends, local-memory caveat, vary |
| OPS-S16 | T1 | Server-Timing | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing | exposing server timings to the browser, exposure caution |
| OPS-S17 | T1 | pg_stat_statements | PostgreSQL docs | https://www.postgresql.org/docs/current/pgstatstatements.html | per-statement statistics |
| OPS-S18 | T1 | Logging Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | what to log, never log, log protection, correlation |
| OPS-S19 | T2 | The Twelve-Factor App (factors I codebase, III config, IV backing services, V build-release-run, VI processes, IX disposability, X dev/prod parity, XI logs, XII admin processes) | Wiggins et al. | https://12factor.net/ (pages /codebase /config /backing-services /build-release-run /processes /disposability /dev-prod-parity /logs /admin-processes) | delivery and runtime contract of a deployable app |
| OPS-S20 | T2 | The Practical Test Pyramid | Vocke, on martinfowler.com | https://martinfowler.com/articles/practical-test-pyramid.html | pyramid, lowest level, real local dependencies, CDC, e2e cost |
| OPS-S21 | T2 | Test Pyramid | Fowler | https://martinfowler.com/bliki/TestPyramid.html | pyramid origin, UI-test cost, caveat |
| OPS-S22 | T2 | Contract Test | Fowler | https://martinfowler.com/bliki/ContractTest.html | contract tests for test doubles and external services |
| OPS-S23 | T2 | Parallel Change | Fowler | https://martinfowler.com/bliki/ParallelChange.html | expand, migrate, contract |
| OPS-S24 | T2 | Blue Green Deployment | Fowler | https://martinfowler.com/bliki/BlueGreenDeployment.html | rollback and schema decoupling |
| OPS-S25 | T2 | Deployment Pipeline | Fowler | https://martinfowler.com/bliki/DeploymentPipeline.html | staged pipeline, fast feedback |
| OPS-S26 | T2 | Evolutionary Database Design | Fowler, Sadalage | https://martinfowler.com/articles/evodb.html | migrations as versioned scripts, small changes |
| OPS-S27 | T2 | Feature Toggles | Hodgson, on martinfowler.com | https://martinfowler.com/articles/feature-toggles.html | toggle categories, lifecycle |
| OPS-S28 | T2 | Monitoring Distributed Systems (SRE book ch. 6) | Google SRE | https://sre.google/sre-book/monitoring-distributed-systems/ | golden signals, alerting, black/white box |
| OPS-S29 | T2 | Service Level Objectives (SRE book ch. 4) | Google SRE | https://sre.google/sre-book/service-level-objectives/ | SLI/SLO, percentiles |
| OPS-S30 | T2 | Release Engineering (SRE book ch. 8) | Google SRE | https://sre.google/sre-book/release-engineering/ | hermetic builds, artifact promotion, config, small releases |
| OPS-S31 | T2 | DORA capabilities | DORA (Google Cloud) | https://dora.dev/capabilities/ | capability list: continuous delivery, test automation, observability, database change management |
| OPS-S32 | T2 | The USE Method | Gregg | https://www.brendangregg.com/usemethod.html | resource-first performance checklist |
| OPS-S33 | T2 | Knuth, "Structured Programming with go to Statements" (1974), passage read as reproduced in a blog post | Knuth; copy at probablydance.com | https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/ | premature optimization; identify critical code first. Primary paper not fetched; a T3 copy was read. |
| OPS-S34 | T2 | Two Hard Things | Fowler (attributing Karlton) | https://martinfowler.com/bliki/TwoHardThings.html | folklore only; supports "invalidation is hard", nothing normative |
| OPS-S35 | T3 | Just Say No to More End-to-End Tests | Google Testing Blog | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | e2e cost, 70/20/10 example mix |
| OPS-S36 | T3 | Pact documentation (introduction) | Pact Foundation (tool vendor, interested party) | https://docs.pact.io/ | consumer-driven contract testing |

### Claims

Format: id | claim | level | stack | sources (section) | agreement | certainty. `positions` only where agreement is not consensus.

**Observability**

- OPS-C01 | Treat logs, metrics and traces as complementary signals of one system, designed to be correlated, not as separate silos. | principle | neutral | S02 (signals), S04 | consensus | grounded
- OPS-C02 | Propagate one trace context across every tier boundary (browser, server, outbound calls) using the W3C `traceparent` header (`tracestate` for vendor data). | decision | http | S01 (headers), S03 (default propagator) | consensus | grounded
- OPS-C03 | Include trace id and span id in every log record so logs link to the trace of the same request. | practice | neutral | S04 (correlation) | consensus | grounded
- OPS-C04 | The app writes logs unbuffered to stdout as an event stream; routing and storage belong to the execution environment, not the app. | practice | neutral | S19 (XI logs), S04 (appenders bridge existing libraries) | consensus | grounded
- OPS-C05 | Never log passwords, session ids, access tokens, payment data, encryption keys or connection strings; sanitize logged input against CR/LF/delimiter injection. boundary: SEC | practice | neutral | S18 (never log, injection) | consensus | grounded
- OPS-C06 | Tag every event of one user interaction with a shared correlation identifier (the trace id serves) so incidents can be reconstructed. | practice | neutral | S18 (correlation), S04 | consensus | grounded
- OPS-C07 | Use zero-code (library) instrumentation for framework, HTTP and database client coverage and add code-based instrumentation only for business logic. | practice | neutral | S07 | consensus | grounded
- OPS-C08 | Do not depend on browser-side OpenTelemetry alone for browser-to-server correlation: it is officially experimental and mostly unspecified; plan a fallback (propagated header plus real-user-monitoring measurements). | decision | js | S06 (status warning), S12 (field data) | consensus on the status; fallback is inferred | inferred (status grounded in S06 as read; fallback is synthesis of S06, S12, S01)
- OPS-C09 | Choose a sampling strategy explicitly: head sampling is simple and cheap but cannot guarantee keeping error traces; tail sampling keeps errors and slow traces but is stateful and harder to operate. Start with head sampling; add tail sampling when volume makes it necessary. | decision | neutral | S05 | majority | positions: S05 (single source, no dissent) says tail sampling is "almost always necessary" in larger systems and a hybrid is common; "start with head" is inferred | grounded (description) / inferred (start-with-head)
- OPS-C10 | Do not blindly continue a caller's sampled trace on a public endpoint: untrusted callers can force tracing overhead. boundary: SEC | practice | http | S01 (security considerations) | consensus | grounded
- OPS-C11 | Never place personal or sensitive data in `traceparent` or `tracestate`, nor seed trace ids from user-identifiable data. boundary: SEC | practice | http | S01 (privacy considerations) | consensus | grounded
- OPS-C12 | For a user-facing system, monitor at least latency, traffic, errors and saturation. | practice | neutral | S28 (four golden signals), S32 (USE for resources) | consensus | grounded
- OPS-C13 | Measure latency with percentiles or histograms, never only averages. | practice | neutral | S28, S29 | consensus | grounded
- OPS-C14 | Define a handful of service level indicators from what users care about, with objectives set not merely from current performance. | decision | neutral | S29 | consensus | grounded
- OPS-C15 | Page a human only for conditions that are urgent, actionable and user-visible. | practice | neutral | S28 (alerting) | consensus | grounded
- OPS-C16 | Combine white-box monitoring (internal metrics, for imminent failures and causes) with black-box monitoring (external symptoms). | practice | neutral | S28 | consensus | grounded
- OPS-C17 | Surface server-side timing to the browser with the `Server-Timing` header, exposing only what the audience may see (for example only to authenticated users). boundary: API | practice | http | S16 | consensus | grounded
- OPS-C18 | Enable per-statement database statistics (`pg_stat_statements`, preloaded; requires a restart to enable) so slow queries can be found by measurement. boundary: DATA | practice | postgres | S17 | consensus | grounded

**Performance**

- OPS-C19 | Optimize only after measurement has identified the critical code or path; ignore small efficiencies elsewhere. | principle | neutral | S33 (passage), S32, S12 | consensus | grounded
- OPS-C20 | Prioritize performance work with field (real-user) data; use lab data to test changes before release and to find opportunities. | principle | neutral | S12 | consensus | grounded
- OPS-C21 | Adopt Core Web Vitals as default page-experience targets, judged at the 75th percentile of page loads: LCP at most 2.5 s, INP at most 200 ms, CLS at most 0.1. boundary: UI | decision | js | S11 | consensus | grounded
- OPS-C22 | When investigating a bottleneck, enumerate resources first and check utilization, saturation and errors for each. | practice | neutral | S32 | consensus | grounded
- OPS-C23 | Observability and testability are whole-system properties to design in across browser, server and database, not per-tier add-ons. boundary: ARCH | principle | neutral | S31 (capabilities: monitoring and observability, test automation), S02, S20 | consensus | inferred (synthesis)

**Testing**

- OPS-C24 | Shape the suite as a pyramid: many small fast tests, some coarser tests, very few high-level tests; exact ratios are team-specific (Google's example is 70/20/10). | principle | neutral | S20, S21, S35 | consensus | positions: ratios vary by team; Fowler (S21) notes that if high-level tests are fast, reliable and cheap, lower-level tests are less needed | grounded
- OPS-C25 | Test at the lowest level that can catch the failure; when a higher-level test finds a bug no lower-level test caught, add the lower-level test. | practice | neutral | S20 | consensus | grounded
- OPS-C26 | Run integration tests against a real database engine of the production kind, locally or in CI, not mocks or a different engine. | decision | postgres | S20 (narrow integration tests), S14 (same settings as production), S19 (X parity) | consensus | grounded for the principle; Postgres application inferred
- OPS-C27 | Give tests a separate disposable database, never the production one, and isolate each test (for example one transaction per test, rolled back). | practice | python | S14 | consensus | grounded
- OPS-C28 | Verify the assumptions behind test doubles and between independently deployed components with contract tests; prefer consumer-driven contracts where a provider team serves consumers. boundary: API | decision | neutral | S22, S20, S36 | consensus | grounded (S36 is a tool vendor, used only as corroboration)
- OPS-C29 | In a classic single-team app, the contract seams are browser client to server API and server to external services; schema-based API checks plus a few consumer-driven tests are likely enough. boundary: API | decision | neutral | derived from S22, S36; sources address independent services, not this case | consensus not established | inferred (open: no source read addresses a single-team monolith directly)
- OPS-C30 | Keep end-to-end tests few and limited to critical user journeys; they are slow, flaky and costly to debug. | practice | neutral | S20, S21, S35 | consensus | grounded
- OPS-C31 | Treat test code with the same care as production code. | practice | neutral | S20 | consensus | grounded

**Delivery**

- OPS-C32 | One codebase tracked in version control, many deploys; code shared across apps becomes a library. | principle | neutral | S19 (I codebase) | consensus | grounded
- OPS-C33 | Separate build, release and run strictly; releases are immutable (a change makes a new release); build once and promote the same artifact through environments instead of rebuilding per environment. | principle | neutral | S19 (V), S30 (artifact promotion, hermetic builds), S25 | consensus | grounded
- OPS-C34 | Keep config strictly separate from code; test: the codebase could be open-sourced at any moment without exposing credentials. | principle | neutral | S19 (III), S30 | consensus | grounded
- OPS-C35 | Where non-secret config is stored: environment variables only, or reviewed version-controlled config. | decision | neutral | S19 (III), S30 (configuration management) | contested | positions: Twelve-Factor says store config in environment variables (not committed by accident, language-neutral); Google SRE stores config in source control with strict review, packaged with binaries, as separate config packages, or in an external store for dynamic values. Reconciliation (inferred): secrets never in the repository; non-secret config may be versioned if it is promoted with the release and reviewed. | grounded (positions), inferred (reconciliation)
- OPS-C36 | Keep development, test and production similar, including the same type and version of backing services (same database engine); do not rely on adapters to hide differences. | principle | neutral | S19 (X) | consensus | grounded
- OPS-C37 | Treat the database and other backing services as attached resources, swappable by changing config, with no code distinction between local and third-party. | principle | neutral | S19 (IV) | consensus | grounded
- OPS-C38 | Apply schema changes as versioned, automated migration scripts stored with application code, run by the same process in every environment, as an explicit step of the release. | decision | neutral | S26, S19 (XII), S31 (database change management) | consensus | grounded
- OPS-C39 | Keep each database change as small as possible. | practice | neutral | S26 | consensus | grounded
- OPS-C40 | Make schema changes backward compatible (expand, migrate, contract): first deploy a schema that supports old and new app versions, verify, then deploy the app, and contract later; this keeps rollback possible. boundary: DATA | practice | neutral | S23, S24, S26 | consensus | grounded
- OPS-C41 | Run one-off admin processes (including migrations) with the same code, environment and dependency isolation as the app; ship admin code with the app. | practice | neutral | S19 (XII) | consensus | grounded
- OPS-C42 | Build the delivery path as an automated staged pipeline in which early stages give fast feedback and later stages give more thorough confidence. | decision | neutral | S25, S31 | consensus | grounded
- OPS-C43 | Prefer small, frequent releases over large infrequent ones. | principle | neutral | S30, S31 | consensus | grounded
- OPS-C44 | Decouple deploy from release with feature toggles where needed, and treat release toggles as short-lived inventory with a removal task created at introduction. | decision | neutral | S27 | consensus | grounded (single source, no dissent found)
- OPS-C45 | Processes start in seconds and shut down gracefully on SIGTERM (stop accepting requests, finish in-flight work, return jobs to the queue) so releases and scaling are cheap. | practice | neutral | S19 (IX) | consensus | grounded
- OPS-C46 | Processes are stateless and share nothing; no sticky sessions; session and durable state live in external stores. boundary: APP | principle | neutral | S19 (VI) | consensus | grounded

**HTTP and application caching**

- OPS-C47 | Set `Cache-Control` explicitly on every response; do not rely on heuristic caching, which stores responses even without headers. | practice | http | S09 (heuristic caching) | consensus | grounded
- OPS-C48 | Serve static assets under fingerprinted (versioned) URLs with `Cache-Control: max-age=31536000` (plus `immutable`); serve HTML and unversioned resources with `no-cache` (store, but revalidate with `ETag`). | decision | http | S09, S13 | consensus | grounded
- OPS-C49 | Mark personalized responses `private` (or `no-store` for sensitive data); a shared cache must not reuse a response to a request carrying `Authorization` unless the response explicitly permits it. boundary: SEC | practice | http | S09, S10 (3.5, 5.2), S13 | consensus | grounded
- OPS-C50 | Send `Vary` for every request header that changes the representation (for example `Accept-Language`). | practice | http | S09, S10 (4.1) | consensus | grounded
- OPS-C51 | Use an application cache that is shared across processes (Redis or Memcached) in multi-process production; per-process local memory is not suitable, and a cache is never permanent storage. | decision | python | S15 (backends, local-memory warning), S19 (VI) | consensus | grounded
- OPS-C52 | Page-level or view-level caches must vary on authentication, session and cookie state; the framework does not do it automatically. | practice | python | S15 (vary) | consensus | grounded
- OPS-C53 | Give every cache an explicit expiry or invalidation plan and version or prefix its keys, because invalidation is the hard part of caching. | practice | neutral | S15 (versioning, prefix), S34 (folklore only) | consensus | inferred (S34 is attribution of a proverb, not evidence)

### Gaps (open)

- Database-side trace correlation (for example tagging SQL with trace context) is not covered by any source read: open.
- Log retention, cost and cardinality control in metrics: S08 read yielded no usable cardinality rule, so no claim made: open.
- Load and performance testing methods (tools, workload models, budgets in CI): not researched.
- Incident response, on-call, post-mortems: out of researched scope.
- CDN and edge caching, `stale-while-revalidate`: only partly touched via S09; not claimed.
- Container build and infrastructure-as-code practice: not researched; Twelve-Factor predates containers on some points (S19 itself says lightweight local services are less compelling now).
- Lock behavior and safe patterns for Postgres migrations (DATA sibling) are not claimed here.
- T4 debates (testing trophy, integration-first testing) not read; the pyramid consensus here rests on T2/T3 sources and may be challenged.
- Source limitation: every page was read through a condensing fetch tool; the L3 wording is a faithful extract of what was returned, not a byte-checked quotation. Knuth is read via a reproduction, not the primary paper.
