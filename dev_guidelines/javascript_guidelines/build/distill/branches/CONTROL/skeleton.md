# CONTROL branch skeleton

Purpose of the branch: explicit failure. Make time, failure and resources explicit. Both graphs
below share the L1 keyword `CONTROL`; philosophy holds the why, defaults the JavaScript rules.
In epistemic_state cells the multi-issue separator is written `\|` so the table stays valid.

## Graph js-philosophy

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| CONTROL | Explicit control of time, failure and resources | Behaviour under delay, error and load stays predictable because every asynchronous operation, failure and resource of a JavaScript program has an owner, a bound and a defined end. | known \| rolls up its five children | - |
| CONTROL.FAILURE | Failure has an owner | A failure in JavaScript travels one of two channels, synchronous throw or asynchronous rejection or event, and a failure nobody observes is lost or escalated by the host; every failure therefore has a named owner who handles it, passes it on with its origin, or lets the program end. Fail fast and never swallow silently are shared with Python and held by the inter link, not copied. | known \| rolls up PIG-JS.CONTROL.PROMISES and PIG-JS.CONTROL.ERRORS; the asynchronous channel rests on one consensus fact | CONTROL-001 |
| CONTROL.BOUNDS | Every wait and every task has a bound and a stopper | Waiting has a time limit and running work has a party that can stop it, because a promise cannot be cancelled and an unbounded wait or task holds resources for as long as its slowest peer. | known \| rolls up PIG-JS.CONTROL.BOUNDS | CONTROL-002, CONTROL-003 |
| CONTROL.SCHEDULING | One shared cooperative thread | All work of a program shares one thread that nothing preempts, with a fixed order between immediate continuations and later tasks and with time only as a lower bound; long work delays every other client, so code states what it needs and never relies on order or precision. | known \| rolls up PIG-JS.CONTROL.SCHEDULING | CONTROL-004, CONTROL-005, CONTROL-006, CONTROL-007, CONTROL-008 |
| CONTROL.FLOW | Producers pace to consumers | Data moves only as fast as its slowest consumer can take it; a buffer threshold is a signal to stop, not a memory bound, so unpaced production costs memory, collection time and latency. | known \| rolls up PIG-JS.CONTROL.FLOW; the cost fact is an illustration from one demo | CONTROL-009, CONTROL-010 |
| CONTROL.LIFECYCLE | Process end is designed | After a failure the program cannot repair, its state is undefined: it records the failure, releases what it owns and ends, and restarting is the job of something outside it. | known \| unvalidated: single T1 source for the placed row; rolls up PIG-JS.CONTROL.PROCESS | CONTROL-011 |

### Intentlinks inside js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | CONTROL.FAILURE | CONTROL.LIFECYCLE | dataflow | A failure no owner can repair flows to the lifecycle, which decides how the process ends. |
| 2 | CONTROL.SCHEDULING | CONTROL.BOUNDS | requires | A shared thread turns unbounded work into a failure for every client, so bounds on time and work are the remedy. |
| 3 | CONTROL.FLOW | CONTROL.BOUNDS | refines | Pacing is the bound that stream production has against consumption. |
| 4 | CONTROL.BOUNDS | CONTROL.FAILURE | dataflow | Timeouts and cancellation end operations with a failure value (an abort or timeout reason) that needs an owner. |

### Inter links to python-kb-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | CONTROL.FAILURE | python-kb-philosophy:DEFENSIVE | refines | Fail fast, no silent swallowing and visible errors are the shared principle; this node adds the two JavaScript failure channels. |
| 2 | CONTROL.LIFECYCLE | python-kb-philosophy:DEFENSIVE | refines | Ending on an unrepairable failure is fail fast applied to the process. |

## Graph pig-js-defaults

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.CONTROL | Explicit control in JavaScript code | JavaScript code makes time, failure and resources explicit through the host's own mechanisms: promises and async functions, error values, abort signals, scheduling choices, streams and process hooks. | known \| rolls up six children | - |
| PIG-JS.CONTROL.PROMISES | Promises and async functions | Every promise is created correctly, chained without loss, observed by someone and combined so that failure and ordering stay visible. | known \| rolls up six children | - |
| PIG-JS.CONTROL.ERRORS | Error values and their channels | Failures are Error objects with an origin, identified by a stable code, handled or rethrown with their cause, and routed through the channel the caller can observe. | known \| rolls up four children | - |
| PIG-JS.CONTROL.BOUNDS | Cancellation, timeouts and caps | Every asynchronous wait ends by a signal, a timeout or a configured cap, and the party that starts the work can stop it. | known \| rolls up three children | - |
| PIG-JS.CONTROL.SCHEDULING | Event loop, timers and threads | Code states the ordering and timing it needs, keeps callbacks short, moves CPU work to workers and carries request state explicitly. | known \| rolls up four children | - |
| PIG-JS.CONTROL.FLOW | Streams and backpressure | Streams move data at the pace of the consumer, are composed so that errors close every stage, and never rely on a buffer size as a memory limit. | known \| rolls up three children | - |
| PIG-JS.CONTROL.PROCESS | Process lifecycle and handles | Unobserved failures end the process visibly, exit and shutdown finish their work, and handles are closed by the code that owns them. | known \| rolls up five children | - |
| PIG-JS.CONTROL.PROMISES.1 | Chaining without loss | Every promise started inside a chain is returned into it, so later steps wait for the work they depend on. | known \| unvalidated: single T2 source for the forked-chain case; single T1 editorial position for flat chains | CONTROL-012, CONTROL-013, CONTROL-014, CONTROL-015 |
| PIG-JS.CONTROL.PROMISES.2 | Constructing promises | Promises are constructed only when no promise exists yet, and every constructed promise settles once on every path. | known \| unvalidated: single T1 rule document for the executor rule (quote tool-extracted); T2 papers sharing a co-author for the others | CONTROL-016, CONTROL-017, CONTROL-018 |
| PIG-JS.CONTROL.PROMISES.3 | Every promise observed | No promise is dropped, silenced or misread: each is awaited, returned or given a rejection handler. | known \| unvalidated: single T1 rule documentation for the void and condition rules (quote tool-extracted) | CONTROL-019, CONTROL-020, CONTROL-021, CONTROL-022 |
| PIG-JS.CONTROL.PROMISES.4 | Combining and ordering async work | Independent work runs concurrently, started promises are combined before awaiting, and shared state is guarded across suspension points. | known \| unvalidated: single T1 source for the early-rejection and stale-read rules (quote tool-extracted) \| gap: concurrency limits not covered | CONTROL-023, CONTROL-024, CONTROL-025, CONTROL-026, CONTROL-027 |
| PIG-JS.CONTROL.PROMISES.4.1 | Concurrency limits, retry and backoff | How many operations run at once, and when a failed operation is retried with what delay. | undecided \| missing: no admitted source | - |
| PIG-JS.CONTROL.PROMISES.5 | Async functions without waste | Asynchronous code adds no promise that does no work. | known \| unvalidated: single T2 source (DrAsync sample); return await inside try/catch not covered | CONTROL-028, CONTROL-030 |
| PIG-JS.CONTROL.PROMISES.6 | Async functions over then chains | Asynchronous code is written with async functions and await by default, so failure travels one visible path; explicit chains remain where kept flat. | known \| unvalidated: single T2 source, V8 team position of 2018 (restricted to history, dated); chain exception inferred from the MDN position | CONTROL-029, CONTROL-086 |
| PIG-JS.CONTROL.ERRORS.1 | Error values | Thrown and rejected values are Error instances identified by a stable code. | known \| unvalidated: single T1 source for the code rule (quote tool-extracted) | CONTROL-031, CONTROL-032 |
| PIG-JS.CONTROL.ERRORS.2 | Catching | A catch acts on the failure; caught values are unknown until narrowed, and failures of asynchronous callbacks go through a channel the caller observes. | known \| unvalidated: single T1 sources; the no-silent-catch rule rests on one style-guide position, demoted to acceptable-when, and on the inter link to python DEFENSIVE | CONTROL-033, CONTROL-034, CONTROL-035 |
| PIG-JS.CONTROL.ERRORS.2.1 | Operational versus programmer errors | How a program tells expected failures from defects, and what error detail reaches callers. | undecided \| missing: no admitted source | - |
| PIG-JS.CONTROL.ERRORS.3 | Rethrowing with a cause | A rethrown failure keeps the original as its cause and states what failed at this level. | known \| unvalidated: single T1 source for the one-site rule | CONTROL-036, CONTROL-037 |
| PIG-JS.CONTROL.ERRORS.4 | Emitter failures | An event emitter's error event always has a listener, and rejections of async listeners reach it. | known \| unvalidated: single T1 source for captureRejections and events.once | CONTROL-038, CONTROL-039, CONTROL-040 |
| PIG-JS.CONTROL.BOUNDS.1 | Abort signals | Cancellable operations accept a signal, check it first, reject with its reason, and use one controller per operation. | known \| unvalidated: single T1 source for the pipeline signal | CONTROL-041, CONTROL-042, CONTROL-043, CONTROL-044 |
| PIG-JS.CONTROL.BOUNDS.2 | Timeouts | Waits are bounded by a timeout signal, a cancellable timer or a configured server timeout. | known \| unvalidated: single T1 source for timers and server timeouts; do-not-disable rule inferred | CONTROL-045, CONTROL-046, CONTROL-047 |
| PIG-JS.CONTROL.BOUNDS.3 | Abort listener hygiene | Listeners on signals are removed at the end of the operation and registered through the Node API that cannot be defeated. | known \| unvalidated: single T1 source each (quote tool-extracted) | CONTROL-048, CONTROL-049 |
| PIG-JS.CONTROL.SCHEDULING.1 | Ordering and timer precision | Code does not rely on the order of timers and immediates or on exact delays, and defers work in the way that cannot starve I/O. | known \| unvalidated: single T1 source for the nextTick rule | CONTROL-050, CONTROL-051, CONTROL-052, CONTROL-053, CONTROL-054 |
| PIG-JS.CONTROL.SCHEDULING.2 | Event-loop blocking | Callback cost stays bounded by input size and synchronous blockers stay off the server's event loop. | known \| unvalidated: single T1 source, mechanism only (restricted); the concrete API list is not admitted | CONTROL-055, CONTROL-056, CONTROL-057, CONTROL-058 |
| PIG-JS.CONTROL.SCHEDULING.2.1 | Yielding to the main thread in browsers | How browser code splits long tasks. | undecided \| missing: no admitted source recommends a method (the scheduler APIs are a draft, Node exposes only experimental ones) | - |
| PIG-JS.CONTROL.SCHEDULING.3 | Workers | CPU-bound work moves to a few workers whose messages, failures and resources are explicit. | known \| unvalidated: single T1 source for sparing use and resource limits | CONTROL-059, CONTROL-060, CONTROL-061, CONTROL-062, CONTROL-063 |
| PIG-JS.CONTROL.SCHEDULING.4 | Async context | Request-scoped state is carried by the platform's scoped store, not by hand-built hooks. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-064, CONTROL-065 |
| PIG-JS.CONTROL.FLOW.1 | Backpressure | Writers stop when told to stop and resume when told to resume. | known \| unvalidated: single T1 source, mechanism only (restricted), for push and data-listener rules | CONTROL-066, CONTROL-067, CONTROL-068 |
| PIG-JS.CONTROL.FLOW.2 | Pipelines and iteration | Streams are composed with the function that closes every stage on failure, and early exit semantics are known. | known \| unvalidated: single T1 source for pipeline and finished rules | CONTROL-069, CONTROL-070, CONTROL-071 |
| PIG-JS.CONTROL.FLOW.3 | Web Streams | Web Streams propagate errors by default and share chunk objects across tee branches. | known \| unvalidated: single T1 source each | CONTROL-072, CONTROL-073, CONTROL-074 |
| PIG-JS.CONTROL.PROCESS.1 | Unhandled rejections | An unhandled rejection is treated as a defect that ends the process in Node and is reported in browsers. | known | CONTROL-075, CONTROL-076, CONTROL-077 |
| PIG-JS.CONTROL.PROCESS.2 | Uncaught exceptions | Uncaught exceptions end the process after synchronous cleanup and a supervisor outside it restarts it. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-078, CONTROL-079 |
| PIG-JS.CONTROL.PROCESS.3 | Exit | Exit lets pending writes drain and does cleanup only in synchronous exit listeners. | known \| unvalidated: single T1 source (quote tool-extracted) | CONTROL-080, CONTROL-081 |
| PIG-JS.CONTROL.PROCESS.4 | Shutdown | A signal listener finishes cleanup and ends the process; servers close gracefully before connections are forced. | known \| unvalidated: single T1 source; the must-exit rule is inferred \| gap: shutdown contract owned by the web-architecture sibling | CONTROL-082, CONTROL-083 |
| PIG-JS.CONTROL.PROCESS.5 | Owned handles | The code that opens or takes over a handle or socket closes it on every path. | known \| unvalidated: single T1 source; the FileHandle wording comes from a digest, not verbatim | CONTROL-084, CONTROL-085 |

### Intentlinks inside pig-js-defaults

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.CONTROL.PROMISES.3 | PIG-JS.CONTROL.PROCESS.1 | dataflow | A promise nobody observes becomes an unhandled rejection that the host escalates, so the observation rules feed the rejection policy. |
| 2 | PIG-JS.CONTROL.BOUNDS.2 | PIG-JS.CONTROL.BOUNDS.1 | requires | A timeout is expressed as an abort signal and ends an operation through the signal protocol. |
| 3 | PIG-JS.CONTROL.FLOW.2 | PIG-JS.CONTROL.BOUNDS.1 | requires | Cancelling a pipeline passes an abort signal to it. |
| 4 | PIG-JS.CONTROL.ERRORS.4 | PIG-JS.CONTROL.PROCESS.2 | dataflow | An emitter error without a listener is thrown and reaches the uncaught-exception path. |
| 5 | PIG-JS.CONTROL.SCHEDULING.3 | PIG-JS.CONTROL.ERRORS.4 | dataflow | A worker's uncaught exception surfaces only as error and exit events, which are emitter failures. |
| 6 | PIG-JS.CONTROL.SCHEDULING.2 | PIG-JS.CONTROL.SCHEDULING.3 | dataflow | CPU work that blocks the event loop is moved to a worker; partitioning on the loop is the weaker alternative. |
| 7 | PIG-JS.CONTROL.PROMISES.1 | PIG-JS.CONTROL.PROMISES.3 | refines | A promise that a chain fails to return is a floating promise, the case this node narrows. |
| 8 | PIG-JS.CONTROL.PROCESS.4 | PIG-JS.CONTROL.PROCESS.2 | requires | A shutdown handler must end the process itself, as the uncaught-exception path does. |

### Inter links from pig-js-defaults to js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.CONTROL.PROMISES | js-philosophy:CONTROL.FAILURE | refines | The promise rules apply failure ownership to the asynchronous channel. |
| 2 | PIG-JS.CONTROL.ERRORS | js-philosophy:CONTROL.FAILURE | refines | The error rules apply failure ownership to values, causes and emitters. |
| 3 | PIG-JS.CONTROL.BOUNDS | js-philosophy:CONTROL.BOUNDS | refines | Signals, timeouts and caps are the JavaScript form of the bound. |
| 4 | PIG-JS.CONTROL.SCHEDULING | js-philosophy:CONTROL.SCHEDULING | refines | The scheduling rules apply the shared-thread principle. |
| 5 | PIG-JS.CONTROL.FLOW | js-philosophy:CONTROL.FLOW | refines | The stream rules apply pacing to Node and Web Streams. |
| 6 | PIG-JS.CONTROL.PROCESS | js-philosophy:CONTROL.LIFECYCLE | refines | The process rules apply the designed end to Node hooks and handles. |

### Proposed links to other branches (the integrator resolves them)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.CONTROL.PROMISES.3 | VERIFICATION | requires | Lint rules that report floating and misused promises enforce these rules (rule documents are cited as positions only). |
| 2 | PIG-JS.CONTROL.ERRORS.2 | CONTRACTS | requires | Typing caught values as unknown belongs with the type layer's strictness settings. |
| 3 | PIG-JS.CONTROL.SCHEDULING.2 | DEFENSE | dataflow | Event-loop blocking by long computation, JSON or regular expressions is a denial-of-service lever. |
| 4 | PIG-JS.CONTROL.BOUNDS.2 | DEFENSE | dataflow | HTTP server timeouts drop slow or idle connections, the defence against slow-request exhaustion. |
| 5 | PIG-JS.CONTROL.FLOW | RUNTIME | dataflow | Unpaced streams cost memory and collection time, whose diagnosis lives in the runtime branch. |
| 6 | PIG-JS.CONTROL.PROCESS.4 | web-architecture (planned boundary) | requires | The Node side of shutdown (signal listener, server close) serves the shutdown contract that the sibling guideline owns; the same holds for the external supervisor of PROCESS.2. |
| 7 | PIG-JS.CONTROL.PROMISES.5 | SUBSET | dataflow | Edition years of promise and error features feed the modern-feature baseline. |
| 8 | PIG-JS.CONTROL.BOUNDS.1 | STRUCTURE | requires | A signal option on async APIs is part of declared API shape (coverage flags STRUCT-C50 to C54 as the API-shape cluster). |

## Judge records

One per defaults node holding a decision. Each lists positions (claim ids, source ids), forces,
the decision and the rejected positions with the condition under which each would win. "No
admitted source names a condition" means exactly that, not that none exists.

### PIG-JS.CONTROL.PROMISES.1 Chaining without loss
- Positions: return or await the inner promise (ASYNC-C01; SRC-075, SRC-245, SRC-072); return the promise p.then produced (ASYNC-C14; SRC-245); flat chains (ASYNC-C15; SRC-075) against nesting; leave the inner promise unreturned (folklore).
- Forces: predictability of order at no cost; flatness serves readability and catch scope.
- Decision: always return or await; return the then result; keep chains flat and nest only to confine a catch.
- Rejected: unreturned inner promise, refuted (SRC-075, SRC-072), never wins; returning p, loses the continuation, never wins; nesting by default, wins when a catch must cover only the inner scope (SRC-075).

### PIG-JS.CONTROL.PROMISES.2 Constructing promises
- Positions: async executor in new Promise (ASYNC-C11; SRC-059); wrapping an existing promise or hand-written promisification (ASYNC-C12; SRC-245, SRC-246); promise that may never settle or settle twice (ASYNC-C13; SRC-245).
- Forces: rejections must not be lost; one settlement per promise.
- Decision: no async executor; return the existing promise and use util.promisify; settle exactly once on every path.
- Rejected: async executor, drops the thrown error, no admitted source names a condition; wrapper pattern, drops inner rejections, no condition named; hand-written promisification, no condition named.

### PIG-JS.CONTROL.PROMISES.3 Every promise observed
- Positions: floating promise (ASYNC-C02; SRC-072, SRC-082, SRC-077); void as handling (ASYNC-C03; SRC-072); async function as void callback (ASYNC-C16; SRC-073, SRC-081); promise as condition (ASYNC-C17; SRC-073).
- Forces: explicit failure against convenience; each rule closes one way a rejection is lost.
- Decision: await, return or handle every promise; void is not handling; catch inside handlers; await before testing.
- Rejected: floating promises, void-as-handling, async handlers and promise conditions, each no condition named by an admitted source. The rule documents are positions of the rule's holder, not a preference for that tool.

### PIG-JS.CONTROL.PROMISES.4 Combining and ordering async work
- Positions: sequential awaiting of started promises (ASYNC-C08; SRC-056); Promise.all against allSettled (ASYNC-C09; SRC-075, SRC-056, SRC-028); concurrent against sequential (ASYNC-C10; SRC-056, SRC-246, SRC-075); unguarded read-modify-write across await (ASYNC-C54; SRC-060).
- Forces: early rejection reporting and speed against ordering needs.
- Decision: combine started promises first; allSettled when every operation must finish; concurrent by default; guard shared state across suspension.
- Rejected: sequential awaiting wins when a later operation depends on an earlier result (ASYNC-C10); Promise.all wins when failing fast is wanted and the remaining outcomes are not needed (inferred from SRC-075); unguarded state, no condition named.

### PIG-JS.CONTROL.PROMISES.5 Async functions without waste
- Positions: remove promises that do no work (ASYNC-C53; SRC-246).
- Forces: fewer allocations and simpler flow against a refactor cost the paper samples (65 of 80 sampled instances refactorable).
- Decision: avoid async functions without await, awaits on returned values and Promise.resolve().then(f). A return await inside try/catch is not evaluated by the source (open): the rule does not cover it.
- Rejected: keeping flagged promises, no condition named.

### PIG-JS.CONTROL.PROMISES.6 Async functions over then chains
- Positions: async functions and await over hand-written promise code (ASYNC-C52; SRC-249, V8 team, 2018, dated position); flat then chains, nested only to confine a catch (ASYNC-C15; SRC-075, MDN editorial position); async functions turn every uncaught exception into a rejection (ASYNC-C07; SRC-056, SRC-245, SRC-075); await is slower than chains (folklore).
- Forces: explicit failure: one syntax in which a thrown error and a rejection both leave through the function's promise and try/catch (inferred from ASYNC-C07) against the new traps of await (ASYNC-C08, C10, C54, handled by PROMISES.4); speed, no admitted current measurement.
- Decision: async functions and await by default; chains are acceptable when kept flat (inferred from ASYNC-C15). Maximum demanded here is the only direction any admitted position takes.
- Rejected: hand-written chains as the default, wins when a flat chain is the whole function body or nesting must confine a catch (MDN position, inferred); the slower-await belief, refuted for 2018 only (SRC-249, history), a present-day gap would win only if an admitted current measurement showed one (open).

### PIG-JS.CONTROL.ERRORS.1 Error values
- Positions: throw only Error instances (ASYNC-C18, LANG-C45; SRC-074, SRC-239); throw any value; identify errors by code (ASYNC-C24; SRC-065) against by message.
- Forces: Error records origin; code is stable, message is not.
- Decision: Error instances only; match on error.code.
- Rejected: strings and plain objects, no admitted source names a condition; matching on error.message, unstable across versions.

### PIG-JS.CONTROL.ERRORS.2 Catching
- Positions: caught value unknown and narrowed (TYPES-C12; SRC-052); callback throws routed through a channel (ASYNC-C22; SRC-065); empty catch with a reason (ASYNC-C21; SRC-239, position only).
- Forces: a thrown value need not be an Error; try/catch cannot see asynchronous callbacks.
- Decision: unknown plus narrowing; route callback failures through rejection, error-first argument or emitter event. A catch that does nothing is acceptable only with its reason in a comment.
- Rejected: any-typed catch variable, no condition named; empty catch without a reason, no condition named.

### PIG-JS.CONTROL.ERRORS.3 Rethrowing with a cause
- Positions: wrap and pass cause (ASYNC-C19; SRC-058, SRC-070, SRC-065); cause for one site, aggregate for several (ASYNC-C20; SRC-058).
- Forces: keeping origin against message clarity.
- Decision: wrap with a specific message and pass the original as cause; one site per cause.
- Rejected: dropping the original, no condition named; assuming cause is an Error, wrong by spec; cause for several failures, use an aggregate.

### PIG-JS.CONTROL.ERRORS.4 Emitter failures
- Positions: listener on every emitter (ASYNC-C23, RUNTIME-C31; SRC-081, SRC-065, SRC-078); captureRejections (RUNTIME-C32; SRC-081); sequential events.once (RUNTIME-C33; SRC-081).
- Forces: an emitted error without a listener ends the process (also a denial-of-service lever).
- Decision: always attach the listener; enable captureRejections; await same-turn events together.
- Rejected: no listener, no condition named; sequential events.once for same-turn events, loses events.

### PIG-JS.CONTROL.BOUNDS.1 Abort signals
- Positions: signal option rejecting with reason (ASYNC-C26, STRUCT-C53; SRC-057, SRC-055, SRC-066, SRC-261); throwIfAborted first (ASYNC-C27; SRC-055, SRC-066); one controller per operation (ASYNC-C29; SRC-055, SRC-066); signal to pipeline (RUNTIME-C06; SRC-196).
- Forces: a single platform primitive for cancellation against ad hoc tokens.
- Decision: AbortSignal everywhere cancellation is offered, with the four rules.
- Rejected: reusing one aborted controller, the signal is one-shot; assuming promises cancel (see CONTROL.BOUNDS).

### PIG-JS.CONTROL.BOUNDS.2 Timeouts
- Positions: AbortSignal.timeout and any (ASYNC-C28; SRC-055, SRC-066, SRC-057); timers/promises with signal, unref (ASYNC-C34; SRC-067); server timeouts (ASYNC-C55, RUNTIME-C42; SRC-078, SRC-190).
- Forces: bounded waits against slow-client exhaustion; TimeoutError separates timeout from user abort.
- Decision: bound every awaited operation; configure server timeouts and never disable requestTimeout on an exposed server.
- Rejected: unbounded waits; disabling requestTimeout, no admitted source names a condition; the combined AbortSignal.any cannot name the first cause in MDN but Node sets the causing reason, so the two sources agree.

### PIG-JS.CONTROL.BOUNDS.3 Abort listener hygiene
- Positions: remove listeners at the end (ASYNC-C30; SRC-055); events.addAbortListener in Node (RUNTIME-C34; SRC-081).
- Forces: leak avoidance against defeat by stopImmediatePropagation.
- Decision: remove at the end; use events.addAbortListener in Node.
- Rejected: signal.addEventListener for abort in Node, defeatable; no condition named.

### PIG-JS.CONTROL.SCHEDULING.1 Ordering and timer precision
- Positions: setImmediate over nextTick (ASYNC-C36; SRC-071); no order dependence between setTimeout(0) and setImmediate (ASYNC-C37; SRC-071, SRC-067); clamps (ASYNC-C32; SRC-062, SRC-067).
- Forces: starvation of I/O against ease of reasoning.
- Decision: defer with setImmediate; never depend on timer-versus-immediate order outside I/O; know the clamps.
- Rejected: nextTick as general deferral, refuted (SRC-071), no condition named; zero-delay timers as immediate, refuted (SRC-062, SRC-067).

### PIG-JS.CONTROL.SCHEDULING.2 Event-loop blocking
- Positions: bound callback cost (ASYNC-C39; SRC-080); synchronous core APIs block (ASYNC-C41; SRC-080, inferred); partition (ASYNC-C42; SRC-080); worker offload (see SCHEDULING.3).
- Forces: fairness among clients against implementation effort.
- Decision: bounded cost; keep synchronous blockers off server loops; partition only where work cannot move to a worker (inferred condition).
- Rejected: unbounded callback cost, no condition named; partitioning as the default, wins when a worker is not available (inferred).

### PIG-JS.CONTROL.SCHEDULING.3 Workers
- Positions: workers for CPU only (ASYNC-C43; SRC-069, SRC-076); few workers (ASYNC-C44; SRC-063); clone or transfer (ASYNC-C45; SRC-069, SRC-076, SRC-063); handle error and exit (ASYNC-C46; SRC-069, SRC-063, SRC-076); resourceLimits (ASYNC-C47; SRC-069).
- Forces: CPU parallelism against startup and memory cost.
- Decision: CPU work only, sparingly, explicit transfer, both failure events handled, limits where untrusted input drives work.
- Rejected: workers for I/O, built-in async I/O is more efficient; many workers, heavy-weight (HTML Standard); no condition named for either.

### PIG-JS.CONTROL.SCHEDULING.4 Async context
- Positions: AsyncLocalStorage, run over enterWith (ASYNC-C48; SRC-064); AsyncContext (ASYNC-C49; SRC-248, fact only).
- Forces: scoped state against leakage into later handlers.
- Decision: AsyncLocalStorage with run().
- Rejected: hand-built async_hooks layer, no condition named; enterWith, wins under strong reasons (SRC-064); AsyncContext, not in the language.

### PIG-JS.CONTROL.FLOW.1 Backpressure
- Positions: stop on write false (RUNTIME-C01; SRC-196, SRC-184); no push when not asked (RUNTIME-C02; SRC-184); no bare data listener (RUNTIME-C03; SRC-184).
- Forces: memory bound against code simplicity.
- Decision: obey the return values and use pipe or pipeline.
- Rejected: write loops ignoring the return value; bare data listeners; no condition named.

### PIG-JS.CONTROL.FLOW.2 Pipelines and iteration
- Positions: pipeline over pipe (RUNTIME-C05; SRC-196); finished with cleanup (RUNTIME-C08; SRC-196); early exit semantics (RUNTIME-C07; SRC-196, SRC-197, SRC-204).
- Forces: resource closure on error against the older, shorter pipe call.
- Decision: pipeline; cleanup: true when listeners must not dangle.
- Rejected: pipe(), leaks the destination on source error; no condition named.

### PIG-JS.CONTROL.FLOW.3 Web Streams
- Positions: default pipeTo propagation (RUNTIME-C09; SRC-197); tee shares chunks (RUNTIME-C10; SRC-197); Node stability (RUNTIME-C11; SRC-204).
- Forces: interference between branches against copy cost (not measured).
- Decision: do not mutate chunks seen through tee.
- Rejected: mutation of shared chunks, no condition named (byte streams copy, per SRC-197).

### PIG-JS.CONTROL.PROCESS.1 Unhandled rejections
- Positions: default throw (ASYNC-C04, RUNTIME-C40; SRC-082, SRC-068, SRC-079); browser event (ASYNC-C06; SRC-077, SRC-075); warn-only belief.
- Forces: visible failure against tolerance.
- Decision: rely on the throw default in Node; report through unhandledrejection in browsers.
- Rejected: warn-only, true only before Node 15 (SRC-068, history); the non-default modes (SRC-079) have no condition named by an admitted source.

### PIG-JS.CONTROL.PROCESS.2 Uncaught exceptions
- Positions: sync cleanup then exit, supervisor restarts (RUNTIME-C37; SRC-082); monitor only logs (RUNTIME-C38; SRC-082); resume (rejected).
- Forces: undefined state against availability.
- Decision: exit after synchronous cleanup, restart from outside; log with the monitor.
- Rejected: resuming after uncaughtException, Node docs: not safe; no condition named.

### PIG-JS.CONTROL.PROCESS.3 Exit
- Positions: exitCode over exit() (RUNTIME-C35; SRC-082); synchronous exit listeners (RUNTIME-C36; SRC-082).
- Forces: output completeness against immediacy.
- Decision: set exitCode and drain; synchronous exit listeners only.
- Rejected: process.exit() with pending writes; beforeExit as cleanup; no condition named.

### PIG-JS.CONTROL.PROCESS.4 Shutdown
- Positions: listener must end the process (RUNTIME-C39; SRC-082); close then closeAllConnections last (RUNTIME-C41; SRC-190).
- Forces: graceful drain against bounded shutdown time.
- Decision: finish cleanup and end; close first, force last.
- Rejected: closeAllConnections first, race with new connections; a listener that cleans but never ends; no condition named.

### PIG-JS.CONTROL.PROCESS.5 Owned handles
- Positions: close FileHandle in finally (RUNTIME-C17; SRC-188); clientError closes socket (RUNTIME-C43; SRC-190).
- Forces: deterministic release against reliance on collection.
- Decision: close on every path; a clientError listener closes or destroys the socket.
- Rejected: relying on garbage collection, emits a warning; no condition named.
