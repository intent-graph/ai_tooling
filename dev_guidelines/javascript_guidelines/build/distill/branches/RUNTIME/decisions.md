# Decisions for review: branch RUNTIME

Each decision settled a contested or weighty choice, or rests on a single source. Nodes are
named by uid in `skeleton.md`, rows by id in `ledger.md`. Rejected positions carry the
condition under which they would win, so the maintainer can overrule.

## Decisions

### D1. Measurement first outranks unmeasured micro-optimization

- Nodes: `PIG-JS.RUNTIME.MEASURE.2` (rows RUNTIME-007 to RUNTIME-012), `RUNTIME.MEASURE` (RUNTIME-001).
- Decision: no engine-level restructuring (holey arrays, hidden classes, nested function creation, prototype mutation) without a measurement of the real workload.
- Rejected: restructuring on mechanism alone, held by MDN's closure and `setPrototypeOf` warnings (STRUCT-C42 on SRC-083, STRUCT-C43 on SRC-088, T1, no figures); wins when a profile shows the cost on a hot path. Belief "holey arrays must be avoided for speed": wins only under a measurement.
- Grounds: V8 states the holey versus packed difference is usually too small to matter or even be measurable (SRC-302, T2, single); no T1 specifies engine performance (RUNTIME-C63, inferred from register restrictions); the profile-first workflow (SRC-195, T1); cross-slot tension X4 of 12_dissent, a difference of scope, not counted contested.
- Weakness: no source states the measurement-first rule itself in normative form; it is inferred from SRC-195, SRC-302, SRC-305 and SRC-307. Engine claims rest on T2 only, so the measured statement is `unvalidated: single T2 source`. Evidence that would settle it: an independent T2 on engine performance (gap G-M31) or a T1 statement.
- Cross-branch: the STRUCTURE branch must not restate STRUCT-C42 and C43 as decisions (both are placed here); proposed link 1 of `skeleton.md` asks the integrator to gate any speed-motivated structure rule.

### D2. Two MDN performance warnings placed as acceptable-when (restriction check)

- Rows RUNTIME-009 (STRUCT-C42) and RUNTIME-010 (STRUCT-C43).
- SRC-083 admits "closure mechanism and the performance note only", so RUNTIME-009 does not overstep its restriction; its role follows the max rule (D1). SRC-088 admits "mechanism facts", so the directive form "set the prototype at creation" of RUNTIME-010 is a demotion from practice to acceptable-when with the mechanism as fact.
- Would win: a profile on the real workload showing the cost.

### D3. Promise file APIs by default, callbacks on a measured need

- Node `PIG-JS.RUNTIME.MEASURE.3`, row RUNTIME-013. Single T1 source (SRC-188), quote tool-extracted.
- Decision: promises by default (shared async style, owned by CONTROL), callbacks only where measurement shows the need. The docs say callbacks are preferable "when maximal performance is required"; the measurement gate and the default are inferred from the branch rule.
- Rejected: callbacks everywhere; wins when a file-heavy hot path measures the promise overhead as significant.
- Boundary: slot 03 owns promise style; proposed link 2.

### D4. Benchmark method placed in both graphs

- Nodes `RUNTIME.METHOD` (philosophy, RUNTIME-002) and `PIG-JS.RUNTIME.METHOD.1`, `.2` (defaults, RUNTIME-014, RUNTIME-015).
- Split by the language-swap test: C61 and C62 (distribution, confidence intervals, setup variation) hold for any runtime and rest on two independent T2 (SRC-307, SRC-305), so `known`. C58, C59, C60 carry Node core's figures and settings (SRC-304 T2) and stay in defaults.
- Weakness: SRC-307 is about Java and SRC-305 about SPEC CPU C programs; transfer to JavaScript is inferred (C58 certainty inferred). SRC-304 is the only JavaScript-runtime ground, single T2. Restrictions respected: abstract-level only for SRC-305, no Java numbers from SRC-307.
- Rejected: single timings; wins when the difference is so large that noise is implausible (condition, unsourced).

### D5. WeakRef and FinalizationRegistry avoided

- Node `PIG-JS.RUNTIME.MEMORY.5`, row RUNTIME-028 (C28, C29, C14, three T1 pages from MDN and Node docs; the two MDN pages count as one ground).
- Decision: weak collections for object-keyed metadata, no weak references, `try...finally` for release, `allocUnsafeSlow` for long-retained small Buffers.
- Rejected: WeakRef and FinalizationRegistry for cleanup; wins when no deterministic release exists and a missed cleanup is harmless.
- Weakness: the ECMA-262 processing-model notes were not read (gap G-M04, G-L10).
- Merge note: three claims in one row because they share one purpose, retaining only what is intended; split if the integrator prefers one decision per source.

### D6. Production capture and near-limit capture

- Node `PIG-JS.RUNTIME.MEMORY.4`, rows RUNTIME-024 to RUNTIME-027. All T1 except C57 (T2).
- Decision: sampling heap profiler in production; snapshots only where a crash is harmless; trigger never public (boundary: DEFENSE, proposed link 4).
- Acceptable-when: `--heapsnapshot-near-heap-limit` (RUNTIME-025) when a snapshot is wanted at that moment.
- Rejected: belief that snapshots are infeasible on large heaps; wins on V8 older than 11.5.130. The Node version carrying the fix is open (not stated in SRC-306).

### D7. Heap limit changed only for a measured need

- Node `PIG-JS.RUNTIME.MEMORY.6`, rows RUNTIME-029 to RUNTIME-031.
- The only-for-measured-need rule is inferred (C48 certainty inferred); manual `global.gc()` as a leak remedy is rejected on SRC-199 (T1). Concurrent marking (C54) is a dated V8 fact, not a prescription.
- Rejected: `global.gc()` as remedy, never; hand-tuning the collector, wins when a GC trace shows starvation and a measurement ties it to the setting.

### D8. Folklore rows without claim ids

- Rows RUNTIME-004, RUNTIME-011, RUNTIME-012, RUNTIME-027 carry `-` as claim_ids: the refuted or restricted belief has no claim of its own (its claim is the decision row of the same node). Placing the claim twice would break the exactly-once rule. The integrator may keep `-` or fold the rows into their decision rows.
- Beliefs: circular references cause leaks (refuted, RUNTIME-004); holey arrays must be avoided for speed (restricted, RUNTIME-012); heap snapshots infeasible on large heaps (restricted, RUNTIME-027).

### D9. Epistemic markers beyond the brief's list

- The brief lists `unvalidated: quote tool-extracted` for the only T1 ground. Used as written where the sole T1 quote is tool-extracted. Where a claim records no quote (RUNTIME-C23 and C48 on T1, C60 on T2) the node says what is missing instead (for example `C23 no quote recorded`). Judgment call, for review.

### D10. No philosophy node for diagnosis

- Diagnosis has no language-neutral claim in the branch (C25 is Node-specific), so the philosophy graph holds three L2 nodes (MEASURE, METHOD, MEMORY) and the defaults node `PIG-JS.RUNTIME.DIAGNOSE` links to `RUNTIME.MEASURE`. Not invented; no source supports a separate principle.

## Undecided nodes

| uid | graph | what is missing | evidence that would settle it |
|---|---|---|---|
| PIG-JS.RUNTIME.MEMORY.6.1 | pig-js-defaults | Behaviour of the default heap limit and of `--max-old-space-size` under a container or cgroup memory limit; the docs read state none (C48). Gap G-M22 of 11_coverage, candidate LC-36 not located. | A Node.js documentation page or T2 study on default heap limits in containers (candidate LC-36), then a rule for sizing the limit against the container limit. |

Noted gaps with no node (low priority or owned elsewhere): AsyncLocalStorage cost and
`diagnostics_channel` stability (G-L10, G-L17, LC-33), leak prevalence studies (G-L10), browser
long tasks (G-M09, CONTROL), supervisor-side shutdown (G-M23, boundary web architecture).
