# Skeleton: branch RUNTIME

Purpose of the branch: measured behaviour. Subtree in both graphs, breadth-first, the L1 node
first. In the `epistemic_state` cells a pipe is written `\|` so that the table keeps five cells.
`ledger rows` names the rows of `ledger.md` placed on the node; `see` marks rows placed
elsewhere that also ground the node.

## Graph js-philosophy (L1 `RUNTIME`)

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| RUNTIME | Runtime behaviour | Code stays well behaved under load and over time because its speed and memory behaviour are established by measurement of the real workload, never by belief or by engine folklore. | known \| unvalidated: most grounds are single-source | - |
| RUNTIME.MEASURE | Measurement before belief | A performance or memory belief becomes a rule only through a measurement on the real workload; advice that rests on engine internals is dated evidence that may describe a mechanism but does not prescribe. | known \| conflict: restructuring for speed on mechanism alone, MDN (SRC-083, SRC-088) \| unvalidated: the rule is inferred from SRC-195 and SRC-302, no source states it normatively; C63 single T2 body | RUNTIME-001; see RUNTIME-006, RUNTIME-007, RUNTIME-009, RUNTIME-010 |
| RUNTIME.METHOD | Measurement method | A measurement is trustworthy only when it treats performance as a distribution: separated start-up and steady state, confidence intervals and a varied setup, so that noise and setup bias cannot flip the conclusion. | known \| unvalidated: transfer from Java and C measurements to JavaScript is inferred | RUNTIME-002; see RUNTIME-014 |
| RUNTIME.MEMORY | Memory model | Memory behaviour follows from what the collector can reach and from how long state lives; this model, not folklore about references, decides what counts as a leak and what bounds it. | known \| unvalidated: both children rest on single T1 pages with tool-extracted quotes | - |
| RUNTIME.MEMORY.1 | Reachability decides leaks | A leak is an object kept reachable from a root by a retainer; unreachable objects are collected whatever their mutual references, so cycles alone are not leaks. | known \| unvalidated: quote tool-extracted | RUNTIME-003, RUNTIME-004 |
| RUNTIME.MEMORY.2 | Bounded long-lived state | State that lives long is promoted into the collector's costlier region, so caches, sessions and other long-lived state carry an explicit bound. | known \| unvalidated: bounding advice inferred, quote tool-extracted | RUNTIME-005 |

### Intentlinks inside the branch (js-philosophy)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | RUNTIME.MEASURE | RUNTIME.METHOD | requires | A measurement that turns a belief into a rule is only as good as the method that produced it. |
| 2 | RUNTIME.MEMORY.2 | RUNTIME.MEMORY.1 | requires | Bounding long-lived state presumes the reachability model of what counts as retained. |

### Inter links to python-kb-philosophy (inferred)

Uids read in `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | js-philosophy:RUNTIME.MEASURE | python-kb-philosophy:INTENTIONALITY | refines | A speed or memory change must answer why this and not something else, and the answer is a measurement. |
| 2 | js-philosophy:RUNTIME.METHOD | python-kb-philosophy:REPRODUCIBILITY | refines | A measurement counts when the same setup and process reproduce it, with its variation reported. |

## Graph pig-js-defaults (L1 `PIG-JS.RUNTIME`)

Breadth-first: L1, L2, L3, L4.

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.RUNTIME | Runtime behaviour in JavaScript | In Node and the browser, speed and memory choices are made from measurements taken with the runtime's own tools and a sound method, and a running process is diagnosed from symptom to cause with those tools. | known \| unvalidated: 83 percent of the branch claims are single-source | - |
| PIG-JS.RUNTIME.MEASURE | Measure before changing | Code is changed for speed or memory only after a measurement of the real workload shows where the cost is; engine-level tuning and speed-motivated API swaps are hypotheses until measured. | known \| conflict: unmeasured micro-optimization advice, MDN (SRC-083, SRC-088) | - |
| PIG-JS.RUNTIME.METHOD | Benchmark method | Benchmarks follow a statistical method in a controlled environment, so that a reported difference is a real one. | known \| unvalidated: figures rest on one T2 harness document | - |
| PIG-JS.RUNTIME.DIAGNOSE | Diagnosis of a running process | A running Node process is diagnosed from its symptom to its cause with built-in tools, context recorded first. | known \| unvalidated: single T1 pages, quotes tool-extracted | - |
| PIG-JS.RUNTIME.MEMORY | Memory diagnosis and retention | Memory problems are classified, signalled, localized and handled with the engine's own diagnostics, with production-safe capture and no unintended retention. | known \| unvalidated: single T1 pages, quotes tool-extracted; container sizing open | - |
| PIG-JS.RUNTIME.MEASURE.1 | Profile before optimizing | The cost is located with the V8 profiler on the running application before any code is changed. | known \| unvalidated: quote tool-extracted; the rule is inferred from the docs workflow | RUNTIME-006 |
| PIG-JS.RUNTIME.MEASURE.2 | Engine-level tuning needs a measurement | Array element kinds, hidden classes, closure creation and prototype mutation are tuned only where a measurement shows the cost; mechanism alone does not justify restructuring. | known \| conflict: restructuring on mechanism alone, MDN (SRC-083, SRC-088) \| unvalidated: single T2 source for the measured statement (SRC-302) | RUNTIME-007, RUNTIME-008, RUNTIME-009, RUNTIME-010, RUNTIME-011, RUNTIME-012 |
| PIG-JS.RUNTIME.MEASURE.3 | Callback file APIs only on a measured need | File system calls use the promise API unless a measurement shows the callback API's lower time or allocation cost is needed. | known \| unvalidated: quote tool-extracted; the measurement gate is inferred from the docs wording | RUNTIME-013 |
| PIG-JS.RUNTIME.METHOD.1 | Compare runs statistically | Comparisons use many runs and a significance test, with a stricter threshold when many comparisons are made. | known \| unvalidated: Node figures single T2 source, JavaScript transfer of the principle inferred | RUNTIME-014 |
| PIG-JS.RUNTIME.METHOD.2 | Quiet measurement environment | Benchmarks run in isolation on a machine whose CPU frequency scaling is set to performance mode. | known \| unvalidated: single T2 source | RUNTIME-015 |
| PIG-JS.RUNTIME.DIAGNOSE.1 | Context and symptom first | The environment, symptoms, reproduction steps and recent changes are recorded before investigating, and the diagnostic path is chosen by symptom: behaviour, memory, or latency and CPU. | known \| unvalidated: quote tool-extracted | RUNTIME-016 |
| PIG-JS.RUNTIME.DIAGNOSE.2 | Event loop health in production | Event loop health is measured in production, not guessed, and each measurement observer is removed when done. | known \| unvalidated: C23 no quote recorded, C24 quote tool-extracted | RUNTIME-017, RUNTIME-018 |
| PIG-JS.RUNTIME.DIAGNOSE.3 | Built-in profilers | CPU and heap profiles come from the profilers built into Node; no third-party tool is needed to capture them. | known \| unvalidated: quote tool-extracted, the no-third-party step is inferred; perf flags partly unreconfirmed | RUNTIME-019, RUNTIME-020 |
| PIG-JS.RUNTIME.MEMORY.1 | Classify the memory problem | A memory problem is first classed as running out of memory or as inefficient use, which selects the tool. | known \| unvalidated: quote tool-extracted | RUNTIME-021 |
| PIG-JS.RUNTIME.MEMORY.2 | Leak signals | Cheap signals, the emitter listener warning and the GC trace pattern, are read before anything is captured. | known \| unvalidated: quote tool-extracted, the advice to justify raising the listener limit is inferred | RUNTIME-022 |
| PIG-JS.RUNTIME.MEMORY.3 | Leak localization by snapshot comparison | A leak is localized by comparing two heap snapshots taken around the suspect path and following large positive deltas to their retainers. | known \| unvalidated: quote tool-extracted | RUNTIME-023 |
| PIG-JS.RUNTIME.MEMORY.4 | Production capture | In production the sampling heap profiler runs and snapshots are taken only where a crash is harmless and the trigger is never public. | known \| unvalidated: quote tool-extracted; snapshot cost on current Node versions unmeasured here | RUNTIME-024, RUNTIME-025, RUNTIME-026, RUNTIME-027 |
| PIG-JS.RUNTIME.MEMORY.5 | Intended retention | Only intended state stays reachable: weak collections for object-keyed metadata, no weak references, unpooled Buffers for long-retained chunks. | known \| unvalidated: quote tool-extracted; the ECMA-262 processing notes for WeakRef were not read | RUNTIME-028 |
| PIG-JS.RUNTIME.MEMORY.6 | Heap limit and the collector | The heap limit is read from the runtime and changed only for a measured need, and the collector is left to run itself. | known \| unvalidated: the measured-need rule is inferred; no quote recorded for the limit statement | RUNTIME-029, RUNTIME-030, RUNTIME-031 |
| PIG-JS.RUNTIME.MEMORY.6.1 | Heap limit inside a container | How the default heap limit and the limit flag behave under a container or cgroup memory limit. | undecided \| missing: no admitted source | - |

### Intentlinks inside the branch (pig-js-defaults)

Direction: for `requires`, `from` depends on `to`; for `dataflow`, `from` produces what `to`
consumes.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.RUNTIME.DIAGNOSE.3 | PIG-JS.RUNTIME.MEASURE.1 | dataflow | Profiles captured with the built-in profilers are what the profile-before-optimizing step reads. |
| 2 | PIG-JS.RUNTIME.MEASURE.2 | PIG-JS.RUNTIME.METHOD.1 | requires | The measurement that justifies an engine-level change must follow the statistical method. |
| 3 | PIG-JS.RUNTIME.MEASURE.3 | PIG-JS.RUNTIME.MEASURE.1 | requires | Swapping to the callback file API needs the measurement that shows the cost. |
| 4 | PIG-JS.RUNTIME.DIAGNOSE.1 | PIG-JS.RUNTIME.MEMORY.1 | dataflow | A symptom classed as memory hands over to the memory classification. |
| 5 | PIG-JS.RUNTIME.MEMORY.1 | PIG-JS.RUNTIME.MEMORY.2 | dataflow | The class of problem selects which cheap signals to read. |
| 6 | PIG-JS.RUNTIME.MEMORY.2 | PIG-JS.RUNTIME.MEMORY.3 | dataflow | A leak signal triggers the snapshot comparison. |
| 7 | PIG-JS.RUNTIME.MEMORY.3 | PIG-JS.RUNTIME.MEMORY.4 | requires | Taking snapshots on a live process presumes the production capture rules. |
| 8 | PIG-JS.RUNTIME.MEMORY.4 | PIG-JS.RUNTIME.MEMORY.6 | dataflow | The limit read from the runtime sets when near-limit capture fires. |
| 9 | PIG-JS.RUNTIME.MEMORY.6.1 | PIG-JS.RUNTIME.MEMORY.6 | refines | The container case would specialize the heap limit rule once a source exists. |

### Inter links, defaults to philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | pig-js-defaults:PIG-JS.RUNTIME.MEASURE.1 | js-philosophy:RUNTIME.MEASURE | refines | Profiling is the first concrete way a belief becomes a measurement. |
| 2 | pig-js-defaults:PIG-JS.RUNTIME.MEASURE.2 | js-philosophy:RUNTIME.MEASURE | refines | Engine-level advice is held as a hypothesis until measured. |
| 3 | pig-js-defaults:PIG-JS.RUNTIME.MEASURE.3 | js-philosophy:RUNTIME.MEASURE | refines | A speed-motivated API swap waits for a measured need. |
| 4 | pig-js-defaults:PIG-JS.RUNTIME.METHOD.1 | js-philosophy:RUNTIME.METHOD | refines | Many runs and a significance test make the distribution explicit. |
| 5 | pig-js-defaults:PIG-JS.RUNTIME.METHOD.2 | js-philosophy:RUNTIME.METHOD | refines | A controlled environment removes setup noise. |
| 6 | pig-js-defaults:PIG-JS.RUNTIME.DIAGNOSE | js-philosophy:RUNTIME.MEASURE | refines | Diagnosis gathers the evidence that belief is not allowed to replace. |
| 7 | pig-js-defaults:PIG-JS.RUNTIME.MEMORY.2 | js-philosophy:RUNTIME.MEMORY.1 | refines | Leak signals are read against the reachability model. |
| 8 | pig-js-defaults:PIG-JS.RUNTIME.MEMORY.5 | js-philosophy:RUNTIME.MEMORY.1 | refines | Weak collections change what counts as reachable through a key. |
| 9 | pig-js-defaults:PIG-JS.RUNTIME.MEMORY.6 | js-philosophy:RUNTIME.MEMORY.2 | refines | The heap limit and the collector are the concrete setting of the bound on long-lived state. |

### Proposed links to other branches (the integrator resolves the uids)

Direction as above; the other branch is named by its keyword.

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | STRUCTURE | PIG-JS.RUNTIME.MEASURE.2 | requires | Any structure rule motivated by speed (nested functions, prototype changes) needs the measurement gate. |
| 2 | PIG-JS.RUNTIME.MEASURE.3 | CONTROL | refines | The speed-motivated exception to the promise-by-default choice of file APIs. |
| 3 | PIG-JS.RUNTIME.DIAGNOSE.2 | CONTROL | dataflow | Event loop utilization and delay measurements feed the event-loop blocking rules. |
| 4 | PIG-JS.RUNTIME.MEMORY.4 | DEFENSE | requires | A snapshot trigger endpoint must never be reachable by untrusted callers. |
| 5 | PIG-JS.RUNTIME.MEMORY.5 | SUBSET | refines | Avoiding WeakRef and FinalizationRegistry is an instance of the features-to-avoid rule. |
| 6 | PIG-JS.RUNTIME.MEMORY.2 | CONTROL | requires | The emitter listener warning belongs with emitter error and listener handling. |

## Judge records (one per defaults node holding a decision)

Each record: positions, forces, decision, rejected with the condition under which each would
win. Positions marked "implicit" have no admitted source; they are the unstated alternative
and carry no claim id.

### PIG-JS.RUNTIME.MEASURE.1

| element | content |
|---|---|
| Positions | (a) profile the running application first, then change code (RUNTIME-C20, SRC-195 T1); (b) implicit: change code from reading it. |
| Forces | (a) predictability of the outcome, cost of one profiling run; (b) no setup cost, risk of fixing the wrong place. |
| Decision | (a). The docs example shows the wrong place: the hot spot was a synchronous hash, not the code that looked slow. Figures are illustration only. |
| Rejected | (b): wins when the change is not a speed or memory change, for example a correctness fix. |

### PIG-JS.RUNTIME.MEASURE.2

| element | content |
|---|---|
| Positions | (a) measurement first; engine tuning only on a measured cost (RUNTIME-C55 SRC-302 T2, RUNTIME-C63); (b) avoid the engine cost on mechanism, without measuring (STRUCT-C42 SRC-083 T1, STRUCT-C43 SRC-088 T1, both MDN, no figures; RUNTIME-C56 SRC-303 T2 mechanism only). |
| Forces | (a) serves measured behaviour, costs one measurement per candidate change; (b) cheap to apply, but V8 itself says the holey versus packed gap is usually unmeasurable and no T1 specifies engine performance. |
| Decision | (a), the max rule for measured behaviour: no engine-level restructuring without a measurement of the real workload. (b) is kept as acceptable-when. |
| Rejected | (b) on mechanism alone: wins when a profile shows closure creation or prototype deoptimisation on a hot path. Holey-array avoidance: wins only under a measurement; the belief is restricted in 12_dissent. |

### PIG-JS.RUNTIME.MEASURE.3

| element | content |
|---|---|
| Positions | (a) callback file APIs where maximal time and memory-allocation performance is required, promises otherwise (RUNTIME-C16, SRC-188 T1); (b) implicit: callbacks everywhere for speed. |
| Forces | (a) keeps the promise style that CONTROL favours, pays only on a need; (b) lowest overhead, loses the shared async style. |
| Decision | (a), with the need established by measurement (the measurement gate is inferred from the branch rule; the docs say "when maximal performance is required"). |
| Rejected | (b): wins when a measurement of a file-heavy hot path shows the promise overhead matters. |

### PIG-JS.RUNTIME.METHOD.1

| element | content |
|---|---|
| Positions | (a) many runs, significance test, two stars across many comparisons (RUNTIME-C58 SRC-304, SRC-307, SRC-305, three T2; RUNTIME-C59 SRC-304); (b) implicit: single timings. |
| Forces | (a) serves trust in a reported difference, costs runs; (b) fast, cannot separate signal from noise. |
| Decision | (a), with Node core's figures (30 runs, Welch t-test) as the concrete instance; the transfer of the principle from Java and C is inferred. |
| Rejected | (b): wins when the difference is orders of magnitude and a single run cannot plausibly be noise (not sourced, so recorded only as the condition). |

### PIG-JS.RUNTIME.METHOD.2

| element | content |
|---|---|
| Positions | (a) isolation and performance mode (RUNTIME-C60, SRC-304 T2); (b) implicit: run on a shared machine at default scaling. |
| Forces | (a) removes frequency and neighbour noise at the cost of a dedicated machine; (b) convenient, adds noise. |
| Decision | (a). |
| Rejected | (b): wins when only a relative comparison on the same machine in the same session is needed and the noise is quantified by the significance test of METHOD.1. |

### PIG-JS.RUNTIME.DIAGNOSE.1

| element | content |
|---|---|
| Positions | (a) record context, then choose the path by symptom (RUNTIME-C25, SRC-187 T1 Diagnostics Working Group guide); (b) implicit: start with a favourite tool. |
| Forces | (a) makes the investigation reproducible and routes memory to heap tools and latency to CPU tools; (b) saves the recording step. |
| Decision | (a). |
| Rejected | (b): wins for a problem reproduced in seconds on a developer machine. |

### PIG-JS.RUNTIME.DIAGNOSE.2

| element | content |
|---|---|
| Positions | (a) measure with eventLoopUtilization and monitorEventLoopDelay, remove observers when done (RUNTIME-C23, C24, SRC-194 T1); (b) implicit: infer blocking from response times or from reading code. |
| Forces | (a) direct measure of the event loop at low, bounded overhead; (b) no instrumentation, guesses. |
| Decision | (a), grounded by the scheduling mechanism (RUNTIME-C19, SRC-080 mechanism only). |
| Rejected | (b): wins never as evidence; it is only the trigger for taking the measurement. |

### PIG-JS.RUNTIME.DIAGNOSE.3

| element | content |
|---|---|
| Positions | (a) built-in --cpu-prof and --heap-prof (RUNTIME-C21, SRC-079, SRC-191 T1); (b) perf flame graphs through --perf-basic-prof (RUNTIME-C22, SRC-189 T1 restricted); (c) implicit: third-party profilers. |
| Forces | (a) no install, stable flags, V8-level frames; (b) native frames, extra flags and tooling; (c) features, new dependency in a process that runs with your privileges. |
| Decision | (a), the most demanding in dependencies: none added. |
| Rejected | (b): wins when native-level frames are wanted beyond V8 profiles (inferred). (c): wins when a needed view is absent from the built-in profilers (no admitted source names one). |

### PIG-JS.RUNTIME.MEMORY.1

| element | content |
|---|---|
| Positions | (a) classify first: running out of memory versus inefficient use, then pick heap profiler, snapshot or GC traces (RUNTIME-C26, SRC-192 T1); (b) implicit: take a snapshot at once. |
| Forces | (a) picks the cheapest sufficient tool; (b) heavy capture before knowing the question. |
| Decision | (a). |
| Rejected | (b): wins when the process may crash harmlessly and the leak is already evident. |

### PIG-JS.RUNTIME.MEMORY.2

| element | content |
|---|---|
| Positions | (a) read cheap signals first: listener warning, GC trace pattern (RUNTIME-C30 SRC-081, RUNTIME-C47 SRC-198, both T1); (b) raise the listener limit to silence the warning (the position C30 warns against). |
| Forces | (a) cheap and often decisive; (b) removes noise and hides a probable leak. |
| Decision | (a); raising the limit only for a justified fan-out. |
| Rejected | (b): wins when the fan-out is designed and its bound is known. |

### PIG-JS.RUNTIME.MEMORY.3

| element | content |
|---|---|
| Positions | (a) two snapshots around the suspect path, compare, follow retainers (RUNTIME-C45, SRC-201 T1). |
| Forces | Isolates growth between two points at the cost of two stop-the-world snapshots. |
| Decision | (a); no competing admitted position. |
| Rejected | none in the evidence. |

### PIG-JS.RUNTIME.MEMORY.4

| element | content |
|---|---|
| Positions | (a) sampling heap profiler in production, snapshots only where a crash is harmless, trigger never public (RUNTIME-C44 SRC-201, SRC-202; RUNTIME-C46 SRC-200, all T1); (b) near-heap-limit capture (RUNTIME-C50, SRC-079, SRC-202 T1); (c) belief that snapshots are infeasible on large heaps (RUNTIME-C57 SRC-306 T2, restricted belief). |
| Forces | (a) low overhead, availability protected, attack surface closed; (b) automatic capture at the moment of interest; (c) false since V8 fixes. |
| Decision | (a), the most demanding on availability and exposure. |
| Rejected | (b): wins when a snapshot is wanted at that moment. (c): wins on older V8 than 11.5.130. |

### PIG-JS.RUNTIME.MEMORY.5

| element | content |
|---|---|
| Positions | (a) WeakMap or WeakSet for object-keyed metadata, avoid WeakRef and FinalizationRegistry, allocUnsafeSlow for long-retained chunks (RUNTIME-C29, C28 SRC-193, SRC-203; RUNTIME-C14 SRC-185; all T1); (b) use WeakRef and FinalizationRegistry for cleanup. |
| Forces | (a) deterministic release, independent of collection timing; (b) convenience, behaviour differs between engines and a callback may never run. |
| Decision | (a), the most demanding: the non-deterministic features are avoided. |
| Rejected | (b): wins when no deterministic release exists and a missed cleanup is harmless. |

### PIG-JS.RUNTIME.MEMORY.6

| element | content |
|---|---|
| Positions | (a) read heap_size_limit, change --max-old-space-size only for a measured need (RUNTIME-C48 SRC-199, SRC-202, SRC-079 T1); (b) call global.gc() as a leak remedy (RUNTIME-C49 SRC-199 T1, rejected there); (c) hand-tune around GC behaviour (RUNTIME-C54 SRC-301 T2: marking is concurrent since Node 10). |
| Forces | (a) avoids unmeasured limits; (b) can hurt performance and does not fix retention; (c) the engine already does the work. |
| Decision | (a), no manual collection. |
| Rejected | (b) wins never as a leak remedy. (c) wins when a GC trace shows starvation (time between GCs below time in GC) and a measurement ties it to the setting. |
