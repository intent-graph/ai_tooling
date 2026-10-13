# Discovery result: slot 09_runtime, area RUNTIME (Node runtime behaviour and performance)

## L1 headline

Authoritative sources cover the operational half of RUNTIME well (streams and backpressure, memory diagnosis, process lifecycle, profiling tooling all have primary Node.js docs), but the "performance claims that hold" half has no T1 source and rests on V8-team writing and benchmarking papers; certainty: grounded for the 35 candidates listed (each fetched, with the limits noted in L3), inferred for the tier proposals, which the auditor decides.

Pinned:
- Number of candidates by proposed tier: T1 26, T2 8, T3 1 (total 35); T3 K35 is `expect-restricted`.
- Sub-topics with no T1 candidate: "performance claims that hold" has none for engine-level JavaScript micro-optimization claims (hidden classes, elements kinds, GC cost of allocation patterns; T2 only: K27 to K31) and none for benchmarking methodology (T2 only: K32, K33, K34). Also no T1 for "memory leaks" as an empirical/prevalence question (no T2 study found either; searched ICSE/FSE/ASE/ISSTA phrasing).
- Failed fetches on a T1 candidate: none failed outright. Partial reads: K26 (ECMA-262 section 9.9, the fetch returned a structural summary, not the full text of the non-normative notes, so its wording is unverified; K25 MDN carries the same caution verbatim). Ten Node.js "learn" pages (K02, K08 to K12, K17, K18, K20, K23) show no date on the page; the version or date is recorded as "undated learn page".

## L2 claims

Sub-topics (each line: best candidates, T1 present?). All lines grounded unless marked.

- Streams and backpressure: K01 (T1), K02 (T1, measured: about 88 MB vs about 1.5 GB RSS on a 9 GB compression test), K03 (T1, WHATWG), K04 (T1); T1 present. Grounded.
- Memory leaks and diagnosis: K08, K09, K10, K11, K12, K13 (all T1), K24 and K25 (T1, reachability and WeakRef caution), K21 (T1, Buffer pool retention), K07 (T1, listener-leak warning); T1 present. Grounded. Heap snapshot cost (pauses the main thread, can double heap) is stated by K10 and K13, grounded.
- GC and heap mechanism: K27, K28, K29 (T2, V8 team); T1 for the usable surface only (K09, K12, K14). T1 present for operation, T2 for mechanism. Grounded.
- Process lifecycle and signals: K05 (T1: `exit` is sync-only, `uncaughtException` "last resort", `exitCode` over `exit()`, stdout writes may be async), K06 (T1: `close`, `closeAllConnections`, timeouts; behaviour changed in v19), K15 (T1, diagnostic report triggers); T1 present. Grounded. No normative source for the supervisor side (SIGTERM grace period, SIGKILL): only K35 (T3, restricted). Inferred gap.
- Profiling: K17 (T1, `--prof` with before/after numbers), K14 (T1, `--cpu-prof`, `--heap-prof`), K16 (T1), K18 (T1, content partly dated), K19 (T1, `monitorEventLoopDelay`, `eventLoopUtilization`), K20 (T1, symptom-to-tool map by the Diagnostics Working Group); T1 present. Grounded.
- Performance claims that hold: no T1 for engine-level claims. K30, K31 (T2, mechanism; K31 states the packed vs holey difference is "usually too small to matter or even be measurable", a folklore correction), K29 and K28 (T2, measured). T1 does ground a few runtime-level claims with measurements: K17 (sync vs async crypto, about 4x), K02, K22 (callback fs APIs preferable to promise APIs for maximal performance, the doc's own statement). Grounded.
- Benchmarking methodology: K32 (T2, Welch t-test, 30 runs default in Node core), K33, K34 (T2, peer-reviewed measurement-bias and statistical-rigour papers). No T1. Grounded for K32 and K33; K34 inferred (see L3 fetch note).
- Process-level concerns that sit with siblings: K23 (event-loop blocking, boundary ASYNC), K03/K04 (boundary: browser streams are `web_architecture_guidelines` only for tier ownership, code-level here).

Disagreements between admissible candidates:
- None between authorities on a substantive position. Version drift inside T1 to carry as conditions: `server.close()` semantics changed at v19 (K06); `Buffer.poolSize` default changed from 8192 to 65536 at v26.3.0 (K21); K18 keeps Node 8.x and 10+ branches.
- Internal tension, same source: K31 recommends avoiding holey arrays and elements-kind transitions, then states the holey difference is rarely measurable. Later stages should take the measured statement, not the tip.

Gaps (searched, nothing admissible found, or not opened):
- Performance of `AsyncLocalStorage`, `async_hooks` and `EventEmitter` as measured costs: K25-type docs (async_context) say "performant and memory safe" without numbers; no source with measurements found. Open.
- `cluster` and `child_process` lifecycle and `process.on('warning')`: not opened. Open.
- Container memory limits and heap sizing: only K09 (a snippet on `heap_size_limit`); no source states the container/cgroup interaction. Open.
- Empirical study of Node.js memory leaks or stream-misuse: not found at a T2 venue. Open.
- Kalibera and Jones, "Rigorous Benchmarking in Reasonable Time" (ISMM 2013): confirmed by search only, never opened; left out until fetched.

## L3 full

### Candidate table

Fetch notes: the fetch tool returns a model-made summary of the page, not raw text; each field below is what the summary showed. Node.js API pages carry the stamp "Node.js v26.11.1" (Current line; the releases page lists v24 and v22 as LTS, v20 EOL). "undated learn page" means the page shows no date.

| id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RUNTIME-K01 | Stream | Node.js project | official runtime documentation | https://nodejs.org/api/stream.html | yes | v26.11.1 | official-doc | T1 | G1-G6 pass; G2 current | streams, backpressure, `highWaterMark`, `pipeline`, `finished`, destroy, async iteration | none |
| RUNTIME-K02 | Backpressuring in Streams | OpenJS Foundation and Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/modules/backpressuring-in-streams | yes | undated learn page | official-doc | T1 | G3 measured (RSS, GC rate; modified-binary experiment); G2 unsure: numbers are from an unstated Node version | backpressure, memory, GC cost | none |
| RUNTIME-K03 | Streams Standard | WHATWG | living standard | https://streams.spec.whatwg.org/ | yes | Living Standard, 18 Aug 2026 | spec | T1 | G1-G6 pass; editors not shown in the fetched summary | backpressure model, queuing strategies, `pipeTo`, `tee`, byte streams | web_architecture_guidelines (tier ownership) |
| RUNTIME-K04 | Web Streams API (Node) | Node.js project | official runtime documentation | https://nodejs.org/api/webstreams.html | yes | v26.11.1; Stability 2 | official-doc | T1 | pass | web streams in Node, queuing strategies | none |
| RUNTIME-K05 | Process | Node.js project | official runtime documentation | https://nodejs.org/api/process.html | yes | v26.11.1 | official-doc | T1 | pass | signal events, `exit`, `beforeExit`, `uncaughtException` caveat, `exitCode`, stdout async writes, `memoryUsage`, `hrtime` | ASYNC (`unhandledRejection`) |
| RUNTIME-K06 | HTTP | Node.js project | official runtime documentation | https://nodejs.org/api/http.html | yes | v26.11.1 | official-doc | T1 | pass | graceful shutdown (`close`, `closeAllConnections`), keep-alive and request timeouts, `Agent` pooling | none |
| RUNTIME-K07 | Events | Node.js project | official runtime documentation | https://nodejs.org/api/events.html | yes | v26.11.1 | official-doc | T1 | pass | listener leak warning, `captureRejections`, `once` pitfalls | ASYNC (rejections) |
| RUNTIME-K08 | Memory (diagnostics) | OpenJS Foundation and Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/memory | yes | undated learn page | official-doc | T1 | pass; short orientation page | leak vs inefficiency symptoms, links to four sub-pages | none |
| RUNTIME-K09 | Understanding and Tuning Memory | Avivi Keller (Node.js website contributor) and Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/memory/understanding-and-tuning-memory | yes | undated learn page | official-doc | T1 | G1 unsure: author's standing is a contributor credit only; G3 explains generations and flags | V8 heap, young/old generation, `--max-old-space-size`, `heap_size_limit`, GC flags | none |
| RUNTIME-K10 | Using Heap Snapshot | Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/memory/using-heap-snapshot | yes | undated learn page | official-doc | T1 | pass | snapshot methods, cost warning (main thread stops, may double heap), leak finding by comparison | none |
| RUNTIME-K11 | Using Heap Profiler | Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/memory/using-heap-profiler | yes | undated learn page | official-doc | T1 | pass | allocation timeline (not for production) vs sampling profiler (low overhead) | none |
| RUNTIME-K12 | Tracing Garbage Collection | Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/memory/using-gc-traces | yes | undated learn page | official-doc | T1 | pass | `--trace-gc` reading, scavenge vs mark-sweep, health indicators | none |
| RUNTIME-K13 | V8 (module) | Node.js project | official runtime documentation | https://nodejs.org/api/v8.html | yes | v26.11.1 | official-doc | T1 | pass | `getHeapStatistics`, `writeHeapSnapshot` (about 2x heap, blocks), near-heap-limit snapshots | none |
| RUNTIME-K14 | Command-line options | Node.js project | official runtime documentation | https://nodejs.org/api/cli.html | yes | v26.11.1 | official-doc | T1 | pass; fetch summary left several defaults unstated, the later stage must read the page | `--cpu-prof`, `--heap-prof`, `--max-old-space-size`, heapsnapshot flags, `--report-on-signal`, `--trace-gc` | none |
| RUNTIME-K15 | Diagnostic report | Node.js project | official runtime documentation | https://nodejs.org/api/report.html | yes | v26.11.1; Stability 2 | official-doc | T1 | pass | report contents and triggers (fatal error, uncaught exception, signal, timeout) | none |
| RUNTIME-K16 | Inspector | Node.js project | official runtime documentation | https://nodejs.org/api/inspector.html | yes | v26.11.1; Stability 2 | official-doc | T1 | pass | programmatic CPU and heap profiling; warning against binding inspector to a public address | RUNSEC (inspector exposure) |
| RUNTIME-K17 | Profiling Node.js Applications | Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/getting-started/profiling | yes | undated learn page | official-doc | T1 | G3 measured (5.33 to 19.46 req/s, sync vs async pbkdf2); G2 unsure: Node version of the example not shown | `--prof`, `--prof-process`, bottom-up reading | ASYNC (event-loop blocking) |
| RUNTIME-K18 | Flame Graphs | Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/diagnostics/flame-graphs | yes | undated learn page | official-doc | T1 | G2 unsure: carries Node 8.x and 10 era branches; later stage must keep only what current docs reconfirm | flame graphs with `perf`, `0x`, `--interpreted-frames-native-stack` | none |
| RUNTIME-K19 | Performance measurement APIs | Node.js project | official runtime documentation | https://nodejs.org/api/perf_hooks.html | yes | v26.11.1; Stability 2 | official-doc | T1 | pass | `performance.now`, `timerify`, `monitorEventLoopDelay`, `eventLoopUtilization`, observer overhead | ASYNC (event-loop delay as a measure) |
| RUNTIME-K20 | Diagnostics: User Journey | Node.js Diagnostics Working Group and Node.js website team | working group of the project | https://nodejs.org/en/learn/diagnostics/user-journey | yes | undated learn page | official-doc | T1 | pass | symptom to tool mapping, what to record before diagnosing | none |
| RUNTIME-K21 | Buffer | Node.js project | official runtime documentation | https://nodejs.org/api/buffer.html | yes | v26.11.1 | official-doc | T1 | pass | `allocUnsafe` pool, retention caveat, `allocUnsafeSlow`, `poolSize` default change | RUNSEC (uninitialized memory) |
| RUNTIME-K22 | File system | Node.js project | official runtime documentation | https://nodejs.org/api/fs.html | yes | v26.11.1 | official-doc | T1 | pass | 64 KiB stream default, sync vs callback vs promise cost statement, threadpool and `UV_THREADPOOL_SIZE` | ASYNC |
| RUNTIME-K23 | Don't Block the Event Loop (or the Worker Pool) | OpenJS Foundation and Node.js contributors | official runtime documentation | https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop | yes | undated learn page | official-doc | T1 | pass | event loop vs worker pool, blocking core APIs, JSON and regex cost | ASYNC (owner: listed here once as boundary) |
| RUNTIME-K24 | Memory management | MDN | reference documentation | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management | yes | last modified 6 Apr 2026 | official-doc | T1 | pass | reachability, mark-and-sweep, `WeakMap`, `WeakRef` caveat | none |
| RUNTIME-K25 | WeakRef | MDN | reference documentation | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef | yes | last modified 10 Jul 2025 | official-doc | T1 | pass; caution quoted ("best avoided if possible", GC timing is implementation-dependent) | WeakRef and finalizer non-determinism | LANG |
| RUNTIME-K26 | ECMA-262, 9.9 Processing Model of WeakRef and FinalizationRegistry Targets | Ecma TC39 | specification | https://262.ecma-international.org/16.0/#sec-weak-ref-objects | partial: structural summary only, notes text not seen; alternative: K25 carries the same text | 16th edition, June 2025 | spec | T1 | G6 anchor for K24 and K25 | what the spec guarantees about collection | LANG |
| RUNTIME-K27 | Trash talk: the Orinoco garbage collector | Peter Marshall, V8 team | V8 team member writing on the V8 blog | https://v8.dev/blog/trash-talk | yes | 3 Jan 2019 | maintainer-writing | T2 | G2 unsure (2019, engine has changed); G3 measured (20-50% young-generation time) | generational, parallel, incremental, concurrent GC | none |
| RUNTIME-K28 | Concurrent marking in V8 | Ulan Degenbaev, Michael Lippautz, Hannes Payer, V8 team | authors of the implementation | https://v8.dev/blog/concurrent-marking | yes | 11 Jun 2018 | maintainer-writing | T2 | G2 unsure (2018); G3 measured (65%/70% main-thread marking reduction); states default in Node v10 | concurrent marking, effect on pauses | none |
| RUNTIME-K29 | Speeding up V8 heap snapshots | José Dapena Paz (Igalia) with Bloomberg engineers and V8 contributors | V8 contributors | https://v8.dev/blog/speeding-up-v8-heap-snapshots | yes | 27 Jul 2023 | maintainer-writing | T2 | G3 measured (10 min to 6 s in one case); G5 minor: consultancy and company named as authors, facts only | heap snapshot cost and fixes | none |
| RUNTIME-K30 | Fast properties in V8 | Camillo Bruni, V8 team | V8 team member | https://v8.dev/blog/fast-properties | yes | 30 Aug 2017 | maintainer-writing | T2 | G2 unsure (2017); G3 mechanism, no measurements | hidden classes, dictionary mode, inline caches | LANG |
| RUNTIME-K31 | Elements kinds in V8 | Mathias Bynens, V8 team | V8 team member | https://v8.dev/blog/elements-kinds | yes | 12 Sep 2017 | maintainer-writing | T2 | G2 unsure (2017); G3 mechanism plus one measurement; states holey vs packed gap is usually unmeasurable | arrays, elements kinds, performance tips and their limits | LANG |
| RUNTIME-K32 | How to write and run benchmarks in Node.js core | Node.js core contributors | project contributor guide | https://github.com/nodejs/node/blob/main/doc/contributing/writing-and-running-benchmarks.md | yes | main branch, undated | maintainer-writing | T2 | G3 states the method (Welch t-test, 30 runs default); contributor document, not API docs | benchmarking method used by the runtime itself | none |
| RUNTIME-K33 | Producing Wrong Data Without Doing Anything Obviously Wrong! | Todd Mytkowicz, Amer Diwan, Matthias Hauswirth, Peter F. Sweeney | ASPLOS 2009 paper | https://sape.inf.usi.ch/publications/asplos09 | yes (bibliographic page; paper PDF behind ACM) | 2009 | paper | T2 | G2 unsure: measured on C programs and 2009 hardware, general mechanism; G3 measured | measurement bias, setup randomization | none |
| RUNTIME-K34 | Statistically Rigorous Java Performance Evaluation | Andy Georges, Dries Buytaert, Lieven Eeckhout | OOPSLA 2007 paper, ACM SIGPLAN most-influential award | https://dri.es/files/oopsla07-georges.pdf | partial: PDF returned undecodable by the fetch tool; bibliographic facts from a search result; alternative copy not yet tried | 2007 | paper | T2 | G2 unsure: Java VMs, 2007, method generalizes to JIT runtimes; G4 origin | confidence intervals, JIT warm-up non-determinism | none |
| RUNTIME-K35 | The Twelve-Factor App, IX Disposability | Adam Wiggins | author of the document; Heroku co-founder (checkable) | https://12factor.net/disposability | yes | last updated 2017 | style-guide | T3, expect-restricted: positions only, never evidence | G3 weak: states a position (graceful SIGTERM shutdown, fast start) with little mechanism; G5: platform vendor origin | supervisor-side shutdown contract | web_architecture_guidelines |

Counts: T1 26 (K01 to K26), T2 8 (K27 to K34), T3 1 (K35).

### Dismissed on sight (tally, no URLs kept)

- Tutorial and blog posts on graceful shutdown (company blogs, course sites, a personal-site course): 7
- Memory-leak listicles and vendor blogs ("N causes of Node leaks"; one APM-vendor and one consultancy blog): 5
- Stream-leak and pipe-vs-pipeline blog posts, including one on a conference-training site: 2
- Packt cookbook chapter (book, no technical review shown): 1
- Aggregators and mirror/proxy copies of Node.js commits and tests: 3
- Language-translated re-posts of English tutorials: 3
- npm-package pages (`pump`, `0x`-style tools) as evidence: 2
- Academic items off-topic or not Node (Java leak study, 2017 client-side leak tool paper, Russian-language survey): 3
- Pointer Compression in V8 (considered, dropped): V8 team, mechanism and 43% saving are for Chrome's 4 GB cage, article itself says Node may need larger heaps; no claim reaches Node: 1
- Node.js TSC/working-group charter pages, release-policy page, `diagnostics_channel` and `async_context` API pages, `cluster`: opened or considered and dropped as thin or outside the area: 5
- Chrome DevTools "Fix memory problems" (Google, Kayce Basques, 2024): browser tool, redundant with K10 and K11; dropped: 1
- V8 `profile` doc and `memory-leaks` doc (d8 and gdb oriented), V8 `react-cliff` and `JSON.stringify` posts: considered, dropped as narrower than K27 to K31: 4
- Kalibera and Jones (ISMM 2013): found by search, not opened, left out: 1

### Searches run

- Producing wrong data without doing anything obviously wrong Mytkowicz ASPLOS 2009
- Statistically rigorous Java performance evaluation Georges Buytaert Eeckhout OOPSLA 2007
- empirical study memory leaks JavaScript Node.js paper ICSE OR FSE OR ASE OR ISSTA
- Node.js graceful shutdown SIGTERM server.close official documentation OR Node.js TSC member
- Node.js stream pipeline vs pipe error handling destroy leak Node.js core maintainer Matteo Collina streams
- Kalibera Jones "Rigorous benchmarking in reasonable time" ISMM 2013
- Direct fetches (no search): the Node.js API and learn pages above, the V8 blog and docs indexes, the WHATWG Streams page, MDN pages, ECMA-262 section 9.9, the POSIX `signal` page (opened, gave no default-action text, dropped), the Node.js releases page, the Node.js Diagnostics Working Group repository page.
- Corrected URL: the V8 heap-snapshot post is at `/blog/speeding-up-v8-heap-snapshots`; `/blog/heap-snapshots` returned 404 (not a T1 candidate).
