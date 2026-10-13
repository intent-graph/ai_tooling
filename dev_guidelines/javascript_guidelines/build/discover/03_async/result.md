# Discovery result: slot 03 ASYNC (async, concurrency, errors)

## L1 headline

Authoritative sources cover all seven sub-topics of ASYNC with at least one T1 each (36 candidates, 29 of them T1), grounded for existence, authorship and coverage, but two T1 reads were partial and must be re-read in full at extraction; the weakest ground is the "operational vs programmer errors" distinction, which no fetched T1 source states.

Pinned:
- Candidates by proposed tier: T1 = 29, T2 = 7 (one of them `expect-restricted`), T3 = 0. Total 36.
- Sub-topics with no T1 candidate: none (all 7 have a T1). Narrow gap inside "error types and causes": no T1 candidate states the operational-vs-programmer error distinction (Node errors page checked, does not state it).
- Failed fetches on a T1 candidate: none failed outright. Two partial reads, to be re-read in full: ASYNC-K01 (ECMA-262 single-page view truncated before the Promise, Async Function and Await sections, so section presence is unconfirmed by fetch) and ASYNC-K09 (Node CLI `--unhandled-rejections`: one read gave default `warn`, which contradicts the Node `process` page and the known Node 15 change to `throw`; a second read was truncated before the entry). Non-T1 fetch failures: ACM page of the ASE 2017 Node.js concurrency-bug study (HTTP 403, paper not listed), Node.js project Medium post on the promise-reject survey (HTTP 403, not listed).

## L2 claims

Sub-topics (best candidates, T1 present?). All lines grounded unless marked.

- Promises and async/await: K01 (T1, partial read), K19, K20 (T1), K34, K35 (T2 studies of promise bugs), K30 (T2, V8 mechanism). T1 present. Grounded for K19, K20; K01 existence grounded, section content inferred.
- Unhandled rejections: K02 (HTML, T1), K08 (Node process, T1), K09 (Node CLI, T1, partial), K24 (MDN event, T1), K25, K26 (typescript-eslint, T1). T1 present. Grounded, except the Node default mode: open (see disagreements).
- Cancellation: K05 (DOM, T1), K14 (Node globals, T1), K21 (MDN, T1), K13, K16 (Node timers and events accept `signal`, T1). T1 present. Grounded.
- Timeouts: K05 (`AbortSignal.timeout`, `TimeoutError`), K03 (HTML timers, nesting clamp), K13 (Node timers), K18 (Node HTTP server timeouts, boundary RUNSEC). T1 present. Grounded.
- Error types and causes: K06 (error-cause, stage 4), K22 (MDN cause), K15 (Node errors), K27, K28, K29 (lint rules with stated reasons), K36 (T2, restricted). T1 present. Grounded; operational-vs-programmer distinction: open (gap).
- Event-loop blocking: K10 (Node, T1), K11 (Node event loop, T1), K02 (HTML event loop, T1), K33 (T2, USENIX Security 2018, boundary RUNSEC), K32 (T2 draft, scheduling). T1 present. Grounded.
- Workers: K04 (HTML, T1), K12 (Node worker_threads, T1), K23 (MDN, T1), K17 (Node async_context worker pool, T1). T1 present. Grounded.

Disagreements and tensions between candidates:
- Node default for unhandled rejections: K08 says an unhandled rejection is raised as an uncaught exception by default; one fetched read of K09 said default `warn`. Inferred to be a fetch-summary error (Node 15 changed the default to `throw`), not a real authority split; re-read K09 verbatim at extraction. Open.
- Sequential `await` in loops: the ESLint `no-await-in-loop` rule (checked, not listed as a candidate) advises parallelism, while its page lists legitimate serial uses (rate limits, dependencies). Not a conflict between authorities; recorded as a rule with stated exceptions. Grounded.
- `process.nextTick` vs `setImmediate`: K11 recommends `setImmediate` as "easier to reason about" (a recommendation, not mechanism), while the same page documents `nextTick` use cases. Grounded.
- K36 (Google JS guide) requires only Error objects thrown; consistent with K27 and K28. No dissent found.

Gaps:
- Operational vs programmer errors: no T1 states it (searched: Node errors page; not found). Open.
- Concurrency limiting, retry and backoff patterns: no authoritative source found; not searched beyond the pages above. Open, may be out of scope.
- ECMA-262 section content (Promise, Async Function, Await, HostPromiseRejectionTracker): existence of the document grounded; section text not confirmed by fetch. Open until full read.
- Authors of Node `learn` pages and MDN last-modified dates: not shown by fetch; date recorded as version where available. Open.
- Leads not verified, so not listed: a 2017 ASE study of Node.js concurrency bugs (fetch 403), and a Node.js project post on the promise-reject survey (fetch 403).

## L3 full

### Candidate table

Common to all rows unless stated: fetched via a page fetch tool that returns a model summary of the page, not the raw text; authors of Node and MDN pages are the project and its contributors. "Date" is what the fetch showed.

| id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ASYNC-K01 | ECMAScript Language Specification (Promise Objects, Async Function Objects, Await, HostPromiseRejectionTracker, Error cause) | Ecma TC39 | the normative language specification, maintained by TC39 | https://tc39.es/ecma262/ | partial: page loaded (header "ECMAScript 2027"), truncated before the relevant sections; alternate https://262.ecma-international.org/ loaded (header "ECMAScript 2026"); section anchors not confirmed | draft 2027 header, no date shown; published 2026 edition | spec | T1 | G1 to G6 pass by nature; G2 date not shown | promises, async/await, unhandled rejections hook, error cause | none |
| ASYNC-K02 | HTML Standard: event loops, microtasks, unhandled promise rejections | WHATWG | normative web platform standard, adopted by browsers | https://html.spec.whatwg.org/multipage/webappapis.html | yes (section list confirmed: 8.1.4.7 style "Unhandled promise rejections", HostPromiseRejectionTracker, event loop processing model); microtask checkpoint detail truncated | living standard, 12 Oct 2026 | spec | T1 | all pass | unhandled rejections, event-loop blocking, promises (microtask timing) | none |
| ASYNC-K03 | HTML Standard: timers | WHATWG | as K02 | https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html | yes | living standard, 12 Oct 2026 | spec | T1 | all pass | timeouts (nesting clamp to 4 ms after 5 levels) | none |
| ASYNC-K04 | HTML Standard: Web Workers | WHATWG | as K02 | https://html.spec.whatwg.org/multipage/workers.html | yes | living standard, 12 Oct 2026 | spec | T1 | all pass | workers (dedicated, shared, terminate, error events, structured clone and transfer) | none |
| ASYNC-K05 | DOM Standard: aborting ongoing activities (AbortController, AbortSignal) | WHATWG | normative standard for cancellation | https://dom.spec.whatwg.org/#aborting-ongoing-activities | yes | living standard, 9 Oct 2026 | spec | T1 | all pass | cancellation, timeouts (`AbortSignal.timeout`, `any`, `reason`, `throwIfAborted`) | none |
| ASYNC-K06 | proposal-error-cause (Error cause) | TC39; champions Chengzhong Wu, Hemanth HM | champions of the stage 4 proposal, in ES2022 | https://github.com/tc39/proposal-error-cause | yes | stage 4, ES2022 | spec | T1 | all pass; G4 origin of the feature | error causes | none |
| ASYNC-K07 | TC39 finished proposals list (Promise.try, Promise.withResolvers, Array.fromAsync, Error.isError, Atomics.waitAsync, top-level await, Explicit Resource Management) | TC39 | official register of stage 4 proposals with champions and ES year | https://github.com/tc39/proposals/blob/main/finished-proposals.md | yes | as of fetch (Oct 2026) | spec | T1 | pass; used as a register of facts, each feature later grounded in K01 or its proposal repo | promises, error types, workers (Atomics.waitAsync) | none |
| ASYNC-K08 | Node.js `process` API: events `unhandledRejection`, `rejectionHandled` | Node.js project | official runtime docs | https://nodejs.org/api/process.html | yes | Node v26.11.1 docs | official-doc | T1 | all pass | unhandled rejections | none |
| ASYNC-K09 | Node.js CLI: `--unhandled-rejections=mode` | Node.js project | official runtime docs | https://nodejs.org/api/cli.html | partial: one read listed modes throw, strict, warn, none, warn-with-error-code and claimed default `warn`; second read truncated before the entry. Re-read in full | Node v26.11.1 docs | official-doc | T1 | G6 unsure: default-mode statement conflicts with K08 and prior knowledge | unhandled rejections | none |
| ASYNC-K10 | Don't Block the Event Loop (or the Worker Pool) | Node.js project, `learn` section | official guide on the Node threading model, event loop and worker pool | https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop | yes; author and date not shown | not shown | official-doc | T1 | G2 unsure (some advice, e.g. third-party modules like `node-webworker-threads`, may be dated); G3 pass (mechanism and measurements) | event-loop blocking, workers | RUNSEC (ReDoS, JSON DoS) |
| ASYNC-K11 | The Node.js Event Loop (phases, `nextTick`, `setImmediate`) | Node.js project, `learn` section | official docs | https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick | yes; date not shown | not shown | official-doc | T1 | pass; recommendations ("use setImmediate") must be recorded as the project's guidance | event-loop blocking, promises (microtask vs nextTick order) | RUNTIME (event loop internals) |
| ASYNC-K12 | Node.js `worker_threads` | Node.js project | official runtime docs | https://nodejs.org/api/worker_threads.html | yes | Node v26.11.1 docs; Worker stable since v10.5.0 | official-doc | T1 | all pass | workers (transfer, SharedArrayBuffer, `resourceLimits`) | none |
| ASYNC-K13 | Node.js timers, `timers/promises` | Node.js project | official runtime docs | https://nodejs.org/api/timers.html | yes | Node v26.11.1 docs | official-doc | T1 | all pass | timeouts, cancellation (`signal` option), `unref` | none |
| ASYNC-K14 | Node.js globals: AbortController and AbortSignal | Node.js project | official runtime docs | https://nodejs.org/api/globals.html | yes | Node v26.11.1 docs; AbortSignal.any since v20.3.0 | official-doc | T1 | all pass; the "best practices" list in the fetch summary must be checked against the page at extraction (inferred) | cancellation, timeouts | none |
| ASYNC-K15 | Node.js errors (Error `cause`, error-first callbacks, error codes, `ABORT_ERR`) | Node.js project | official runtime docs | https://nodejs.org/api/errors.html | yes | Node v26.11.1 docs | official-doc | T1 | all pass | error types and causes | none |
| ASYNC-K16 | Node.js events (`captureRejections`, `once`/`on` with signal, unhandled `'error'` event) | Node.js project | official runtime docs | https://nodejs.org/api/events.html | yes | Node v26.11.1 docs | official-doc | T1 | all pass | unhandled rejections, error types, cancellation | none |
| ASYNC-K17 | Node.js asynchronous context tracking (`AsyncLocalStorage`, `AsyncResource`, worker pool example) | Node.js project | official runtime docs | https://nodejs.org/api/async_context.html | yes | Node v26.11.1 docs; stable since v16.4.0 | official-doc | T1 | all pass | workers (pools), promises (context across await) | none |
| ASYNC-K18 | Node.js security best practices (HTTP server timeouts, slowloris, socket error handling) | Node.js project, security working group contributors (names listed on the page) | official guide | https://nodejs.org/en/learn/getting-started/security-best-practices | yes; date not shown; the page does NOT cover event-loop blocking, ReDoS or workers | not shown | official-doc | T1 | pass | timeouts (HTTP server timeouts) | RUNSEC |
| ASYNC-K19 | Using promises (MDN guide) | MDN contributors (Mozilla and community) | MDN is a T1 class by policy | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises | yes; last-modified not shown | not shown | official-doc | T1 | G4 caveat: MDN is a reference not the origin of promise semantics (K01); cite K01 for semantics | promises, unhandled rejections, error handling, microtask timing | none |
| ASYNC-K20 | async function (MDN reference) | MDN contributors | as K19 | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function | yes; Baseline widely available (April 2017) | not shown | official-doc | T1 | as K19 | promises and async/await, sequential vs concurrent, error handling | none |
| ASYNC-K21 | AbortSignal (MDN reference) | MDN contributors | as K19 | https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal | yes; Baseline since April 2018 | not shown | official-doc | T1 | as K19; origin is K05 | cancellation, timeouts (`TimeoutError` vs `AbortError`) | none |
| ASYNC-K22 | Error: cause (MDN reference) | MDN contributors | as K19 | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause | yes; Baseline since September 2021 | not shown | official-doc | T1 | as K19; origin is K06 and K01 | error causes (also AggregateError, SuppressedError contrast) | none |
| ASYNC-K23 | Using Web Workers (MDN guide) | MDN contributors | as K19 | https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers | yes | not shown | official-doc | T1 | as K19; origin is K04 | workers | none |
| ASYNC-K24 | `unhandledrejection` event (MDN reference) | MDN contributors | as K19 | https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event | yes | not shown | official-doc | T1 | as K19; origin is K02 | unhandled rejections (browser; cross-origin note) | none |
| ASYNC-K25 | typescript-eslint rule `no-floating-promises` | typescript-eslint project | official rule docs, T1 by policy | https://typescript-eslint.io/rules/no-floating-promises/ | yes | docs v8.71.2 | official-doc | T1 | G3 pass (rationale stated); G5 pass | unhandled rejections, promises | QUALITY (lint configuration) |
| ASYNC-K26 | typescript-eslint rule `no-misused-promises` | typescript-eslint project | as K25 | https://typescript-eslint.io/rules/no-misused-promises/ | yes | docs v8.71.2 | official-doc | T1 | as K25 | promises, unhandled rejections | QUALITY |
| ASYNC-K27 | typescript-eslint rule `only-throw-error` | typescript-eslint project | as K25 | https://typescript-eslint.io/rules/only-throw-error/ | yes | docs v8.71.2 | official-doc | T1 | as K25 | error types | QUALITY |
| ASYNC-K28 | ESLint rule `no-async-promise-executor` | ESLint project | official rule docs | https://eslint.org/docs/latest/rules/no-async-promise-executor | yes; in the recommended config (per fetch) | rule since ESLint v5.3.0 | official-doc | T1 | as K25 | promises (lost errors in async executors) | QUALITY |
| ASYNC-K29 | ESLint rule `require-atomic-updates` | ESLint project | official rule docs | https://eslint.org/docs/latest/rules/require-atomic-updates | yes; recommended status not stated by fetch | rule since ESLint v5.3.0 | official-doc | T1 | as K25 | promises, concurrency (race after `await`) | QUALITY |
| ASYNC-K30 | V8 blog: Faster async functions and promises | Maya Armyanova and Benedikt Meurer (V8 team engineers, authors of the change) | V8 engine maintainers describing their own implementation | https://v8.dev/blog/fast-async | yes | 12 November 2018 | maintainer-writing | T2 | G2 unsure (2018, engine internals; mechanism claims about await ticks must match K01 spec change); G3 pass | promises and async/await (await cost, microtask ticks, async stack traces) | RUNTIME (performance claims) |
| ASYNC-K31 | proposal-async-context (AsyncContext) | TC39; champions Andreu Botella, Chengzhong Wu, Justin Ridgewell | champions of the proposal | https://github.com/tc39/proposal-async-context | yes | stage 2 (the TC39 proposals list shows 2.7 for it: stages disagree between pages, inferred a lag in one) | spec | T2 (a stage 2 proposal is not T1 by policy) | G6 n/a; record only as "not yet in the language" | promises (context across await) | none |
| ASYNC-K32 | Prioritized Task Scheduling (`scheduler.postTask`, `yield`, TaskController) | WICG; editor Scott Haseley (Google) | community group draft by an implementer | https://wicg.github.io/scheduling-apis/ | yes | W3C Community Group Draft Report, 30 May 2025 | spec | T2 (draft, not a W3C standard) | G2 unsure (support not in all browsers: Safari missing per page); G5 pass | event-loop blocking (yielding in the browser), cancellation (TaskController) | none |
| ASYNC-K33 | Freezing the Web: A Study of ReDoS Vulnerabilities in JavaScript-based Web Servers | Cristian-Alexandru Staicu, Michael Pradel (TU Darmstadt) | USENIX Security 2018 paper; 25 new vulnerabilities, 339 of 2,846 sites affected | https://www.usenix.org/conference/usenixsecurity18/presentation/staicu | yes | August 2018 | paper | T2 | G2 unsure (2018 measurements); G3 pass (evidence) | event-loop blocking (impact of one blocked request) | RUNSEC (ReDoS) |
| ASYNC-K34 | A Model for Reasoning About JavaScript Promises | Magnus Madsen, Ondrej Lhotak, Frank Tip | OOPSLA 2017, Proc. ACM Program. Lang. 1 (publication record; PDF read, first page checked) | https://plg.uwaterloo.ca/~olhotak/pubs/oopsla17b.pdf | yes (first page rendered; DOI 10.1145/3133910) | October 2017 | paper | T2 | G2 unsure (ES6-era model, but promise semantics unchanged); G3 pass | promises (formal semantics, bug classes via StackOverflow-derived case study) | none |
| ASYNC-K35 | DrAsync: Identifying and Visualizing Anti-Patterns in Asynchronous JavaScript | Alexi Turcotte, Michael D. Shah, Mark W. Aldrich, Frank Tip | ICSE 2022 technical track, Best Artifact Award | https://conf.researchr.org/details/icse-2022/icse-2022-papers/61/DrAsync-Identifying-and-Visualizing-Anti-Patterns-in-Asynchronous-JavaScript | yes (abstract page); full paper not read | ICSE 2022 | paper | T2 | G3 pass (8 anti-patterns, about 2,500 instances in 20 repositories, per page); full text to be read at extraction | promises (anti-patterns) | QUALITY |
| ASYNC-K36 | Google JavaScript Style Guide (error handling: throw only Errors, empty catch) | Google | large engineering organization style guide | https://google.github.io/styleguide/jsguide.html | yes | page states no longer updated, recommends TypeScript | style-guide | T2, `expect-restricted`: positions only, never evidence; async content is minimal | G2 unsure (not updated); G3 mixed (some rules give reasons) | error types | none |

### Dismissed-on-sight tally

From the results of 6 web searches (not from a wider sweep):
- Unattributed Medium or dev.to posts: 3 (one Medium by an individual, one dev.to repost, one betterprogramming member story).
- Company tutorial or marketing blogs (news-style release write-ups, tutorial sites, course pages): 6 (This Dot, IBM release blog, SD Times, i-Programmer, codefinity course, leyaa.ai).
- Aggregators, mirrors and translations: 2 (habr, zenn).
- Vendor detector or product docs: 1 (a static-analysis vendor page on "missing await"; G5).
- Personal blog restatements: 2 (advancedweb.hu, a paper summary blog; G4, the paper itself was listed instead).
- Package-bundled "agent skills" markdown: 1.
- Unrelated results (older general concurrency studies of MySQL, Apache, Mozilla and similar, not JavaScript): 5; Scribd and mailing-list excerpt: 2.
- Not searched for: Stack Overflow, listicles; none appeared in these queries.

### Searches run

1. Wang et al. Node.js concurrency bugs ASE 2017 study (paper existence confirmed by search only; fetch of the ACM page returned HTTP 403, so not listed)
2. Freezing the Web ReDoS USENIX Security 2018 Staicu Pradel
3. Madsen "Model for Reasoning About JavaScript Promises" OOPSLA 2017
4. empirical study promises async/await misuse unhandled rejections ICSE FSE ASE
5. "comprehensive study on real world concurrency bugs in Node.js" pdf (no usable copy found)
6. Node.js unhandled rejections throw by default Node 15 (only secondary sources returned; Node project post failed with HTTP 403)
