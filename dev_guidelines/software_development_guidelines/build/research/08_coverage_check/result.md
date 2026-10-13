# Round-1 coverage check (slot 08)

Scope: reads slots 01 to 07 of round 1 (L1/L2 of each, L3 claim lines for ids and source tiers). Proposes no structure and judges no claim. Claim ids are as in each slot (`SRC`, `ADOPT`, `VERIFY`, `DELIVER`, `OPERATE`, `TRANS`, `MAINT`). Slot "01" to "07" = areas SRC to MAINT.

## L1 headline

Round 1 covers the mainstream of all six areas from T1/T2 sources, with 14 coverage gaps (one already known), heavy duplication between sourcing and adoption, and 56 distinct contested topics; the maintainer doctrine departs from the public slots on ten points (six opposed, four partial), and a spot-check of one T1/T2-grounded claim per slot (01 to 06) confirmed all six against the fetched source. Certainty: grounded for the counts and ids (read from the result files), grounded for the spot-check, inferred for the gap list where it rests on absence of a term in the results.

Pinned:
- Gaps: 14 (G1 external services and APIs is the known one; 13 new). Two topics have no slot mention at all: backup/restore/disaster recovery (G6), decommissioning and technical debt (G7).
- Contested topics: 56 distinct (48 across public slots 01 to 06; 8 more only in the maintainer slot 07), after merging duplicates across slots.
- Spot-check score: 6 of 6 confirmed (slots 01 to 06). No claim failed. Two had a sub-clause not on the fetched page: SRC-C31 (the rationale "hard dependencies multiply availabilities") and ADOPT-C15 ("fail if lock and manifest disagree" rests on a second source, not fetched here).
- Overlaps: 23 clusters of ids restating the same claim in two or more slots (L2 item 2).
- AI coding agents as contributors: 1 public claim (DELIVER-C49), 2 maintainer claims (MAINT-C62, MAINT-C63); sourcing and adoption slots are silent.

## L2 claims

### 1. Gaps (grounded: from the slots' own "not covered" lists, plus a term search over slots 01 to 06; "absent" claims are inferred from the search)

Within the six named areas, not covered or covered only from T3/T4 or from nothing read:
- G1 External services and APIs (known). Only SRC-C31, C32 and C34 stand on T1 (a cloud availability rule and two API deprecation policies); SRC-C33 is inferred (search summary only); SRC-C35 and ADOPT-C50 rest on T4 or no source read; ADOPT-C07 on one T2. Missing: contract and SLA terms, data portability, pricing risk, vendor assessment, consumed-API design. Grounded.
- G2 Evaluating tools and platforms that are not libraries (dev tools, CI and hosting services). SRC "not covered". Grounded.
- G3 Licence obligations (copyleft, compatibility). Only presence and clarity (SRC-C36). Grounded.
- G4 Data and database change management: one T2 claim (DELIVER-C45) plus DELIVER-C40; none on data migration or backfill. The maintainer slot has about twenty claims here with no public counterpart. Grounded (count), inferred (reading of absence).
- G5 Performance, load and capacity: VERIFY lists it as uncovered (only VERIFY-C29, T2), OPERATE lists capacity planning as uncovered. Grounded.
- G6 Backup, restore, disaster recovery, continuity: no slot has a claim. Inferred (term search).
- G7 Decommissioning or end-of-life of the team's own software; technical debt and refactoring policy: no slot has a claim. Inferred (term search).
- G8 Security beyond lifecycle process: security testing depth, security monitoring (SIEM; NIST 800-61 body unread), privacy and retention, ASVS/SAMM/BSIMM levels. Grounded (not-covered lists).
- G9 Regulated and compliance contexts: change management under regulation, audit trails in docs; the only regulation claim is ADOPT-C51 from a T3 copy of the text. Grounded.
- G10 Software that is not a hosted service: mobile and on-device release, data/ML pipelines and ML-system testing, infrastructure-as-code tooling. Grounded.
- G11 Test breadth: test data management, visual/snapshot, exploratory, accessibility, AI-generated tests, formal methods. Grounded.
- G12 Operational readiness: runbooks and playbooks (one T2 line in OPERATE-C35), production-readiness review, synthetic monitoring, telemetry cost, the "human error" view (source unreadable), incident tooling. Grounded.
- G13 Topics resting only on T3 (or T3 copies of T1 text). Chaos experiments: VERIFY-C41 and OPERATE-C28b, one T3 source (contested); characterization tests: VERIFY-C28; RED/USE: OPERATE-C18, C19; API-description lint and diff: TRANS-C12, C13; changelog and doc structure: TRANS-C25, C26 (and C17); selection process and score validity: SRC-C05, C18 (single studies); micro-packages and registry concentration: SRC-C21, C22 (npm only); innovation budget and tiny-code copying: ADOPT-C05, C26, C42; unofficial copies of T1 text: ADOPT-C12, C51; deploy freezes: DELIVER-C41. Grounded.
- G14 Canonical T2 books and a T1 body not read directly: Accelerate, Humble and Farley, Nygard, Living Documentation (secondary pages instead), NIST SP 800-61 (landing page only), NIST SSDF text partly extracted. Grounded.

### 2. Overlaps (same claim in two or more slots; grounded unless marked near)

Sourcing vs adoption (boundary tags are partial):
- SRC-C01 = ADOPT-C08 (necessity first; ADOPT-C01 near)
- SRC-C02 = ADOPT-C02 + ADOPT-C03 (reuse vs build)
- SRC-C04 = ADOPT-C11 (evaluate for intended use, repeat)
- SRC-C06 + SRC-C07 = ADOPT-C10 (activity, more than one maintainer)
- SRC-C09 = ADOPT-C39 (end-of-life plan)
- SRC-C10 near ADOPT-C38 (vulnerability status, ongoing)
- SRC-C12 = ADOPT-C09 (authenticity of source)
- SRC-C13 = ADOPT-C34 (provenance signals)
- SRC-C24 near ADOPT-C05 (boring technology budget)
- SRC-C27 = ADOPT-C12 (vetting depth scaled to risk)
- SRC-C35 near ADOPT-C40 + ADOPT-C50 (abstraction and exit)
- SRC-C36 near ADOPT-C11 (licence check)
Across areas:
- SRC-C14 = ADOPT-C29 = VERIFY-C26 (compatibility promise, Hyrum's Law)
- ADOPT-C13 = TRANS-C54 (declare dependencies, isolate; Twelve-Factor)
- ADOPT-C18 near DELIVER-C26 (reproducible builds)
- DELIVER-C35 = TRANS-C45 (config apart from code)
- DELIVER-C42 = TRANS-C55 (environment parity; Twelve-Factor)
- DELIVER-C50 = OPERATE-C35 (changes cause most outages)
- DELIVER-C46 = OPERATE-C36 (recovery time and change-fail rate)
- VERIFY-C41 = OPERATE-C28b (chaos experiments, same single T3 source)
- VERIFY-C42 near TRANS-C35 (policy per stage and risk, both from SSDF)
- VERIFY-C30/C31/C32 near DELIVER-C24 (flaky tests); VERIFY-C33 near DELIVER-C21/C22 (ten-minute feedback)
Maintainer vs public: MAINT-C44 near ADOPT-C01 and SRC-C24 (new layer must earn its cost).

### 3. Contested topics (deduplicated; forces in tension; grounded in each slot's L2 and claim agreement fields)

Sourcing and adoption
1. Build vs reuse vs rent (SRC-C02, ADOPT-C07, C43; MAINT-C46): security, delivery speed vs cost of ownership, control, exit risk.
2. Tiny dependencies: micro-packages vs copying (SRC-C21, ADOPT-C42): reuse and readability vs hidden chains, control.
3. Single-maintainer tolerance (SRC-C07): fit, footprint vs exit risk, continuity.
4. Boring-first vs staged novelty (SRC-C24, C25): cognitive load, reversibility vs delivery speed, learning.
5. Central allowlist vs team choice (SRC-C28): security, control vs delivery speed, cognitive load.
6. Vetting depth (SRC-C27): security vs speed.
7. Scores and popularity as gate vs input (SRC-C17, C19): automation vs decision correctness.
8. Exact pins vs ranges, and resolution rule (ADOPT-C19, C20, C17): reproducibility vs duplicate dependencies, consumer friction.
9. Update fast vs delayed (cooldown) (ADOPT-C22 to C24): known-vulnerability exposure vs malicious-release exposure.
10. Live at head vs pinned versions (ADOPT-C28): feedback speed, shared upgrade cost vs control.
11. Wrap vs accept lock-in (ADOPT-C40, C45 to C47): reversibility, exit risk vs cost of ownership, cognitive load.
12. Mirror, vendor or rebuild vs registry plus lockfile (ADOPT-C32, C36, C48): availability, control vs cost, update lag.
13. Trust in SemVer numbers (ADOPT-C29): delivery speed vs correctness.
Verification
14. Test-level shape: pyramid, honeycomb, trophy (VERIFY-C11): confidence, refactor-safety vs feedback speed, diagnosability.
15. Classical vs mockist doubles, and solitary vs sociable units (VERIFY-C15, C19): refactor-safety vs isolation, failure location.
16. TDD as rule (VERIFY-C22): feedback speed, design pressure vs cost, cognitive load.
17. Consumer-driven contracts vs provider schema (VERIFY-C24): autonomy, precision vs broker and per-consumer cost.
18. Coverage as target vs diagnostic (VERIFY-C34): visibility, a floor vs gaming.
19. Mutation testing as routine gate (VERIFY-C35): signal strength vs compute and noise.
20. Static types (VERIFY L2 debate): bug prevention, documentation vs annotation cost, friction.
21. Verification in production: testing in production, canary, chaos (VERIFY-C40, C41; OPERATE-C28b): fidelity, realism vs user impact, blast radius.
Delivery
22. Daily integration vs feature branches (DELIVER-C02): feedback speed vs isolation, low-commitment contributors.
23. Merge method (DELIVER-C07): legible history vs fidelity, per-commit bisect.
24. Monorepo vs multiple repositories (DELIVER-C09): one-version consistency vs access control, exit risk.
25. Structured vs free-form commit messages (DELIVER-C11): automation vs cognitive load.
26. Review mechanism (DELIVER-C14): confidence, knowledge sharing vs delivery speed, trust cost.
27. Presubmit scope (DELIVER-C22): confidence vs feedback speed.
28. Release cadence (DELIVER-C30): delivery speed vs predictability, multi-version support.
29. Manual approval gates (DELIVER-C33; MAINT-C26): speed, less toil vs control, regulation, reversibility.
30. Rollout strategy (DELIVER-C37): infrastructure cost vs complexity vs blast radius.
31. Rollback vs fix forward, written undo vs automatic down step (DELIVER-C39; MAINT-C24): reversibility, recovery time vs simplicity, data compatibility.
32. Environment parity (DELIVER-C42, TRANS-C52/C55, MAINT-C64): confidence and feedback vs cost, isolation and security of credentials, production-sized data.
33. Push CI deploy vs pull GitOps (DELIVER-C44): simplicity vs drift control, audit.
Operation
34. Telemetry store: three pillars vs wide events (OPERATE-C21): maturity, cost vs exploratory power.
35. Sampling (OPERATE-C27): cost, simplicity vs completeness, operational complexity.
36. Error-budget exhaustion: hard freeze vs self-regulation (OPERATE-C09): control, reliability vs speed, autonomy.
37. SLO target from current performance (OPERATE-C06): adoption speed vs locking in heroics.
38. Incident declaration threshold (OPERATE-C30): speed, shared load vs process cost.
39. Alert on causes vs symptoms (OPERATE-C12): early warning vs low noise.
Transverse
40. Documentation gate: merge, release or advisory (TRANS-C05, C28, C29): speed, cognitive load vs correctness.
41. Who verifies doc accuracy (TRANS-C19, C20): speed vs consistency.
42. How much to document, and mandatory unit headers (TRANS-C27; MAINT-C54): ownership cost vs reader confidence, durability.
43. Prose-style linting as a failing check (TRANS-C16): consistency vs friction.
44. Executable examples vs readable docs (TRANS-C10): correctness vs clarity.
45. Security findings block vs advise (TRANS-C37): security, confidence vs speed, developer trust.
46. Config and secret delivery: env vars, files, store API (TRANS-C46): simplicity vs security, live rotation.
47. Per-environment config: named bundles vs orthogonal values (TRANS-C47): reviewability vs scalability.
48. Development environment mechanism: container, pinned package set, manifests (TRANS-C56): onboarding, load vs byte-level reproducibility.
Maintainer slot only (public slots have no claim or no contest)
49. Tests on real data behind forced rollback vs isolated environments (MAINT-C01): confidence in real shapes vs isolation, blast radius.
50. Tests colocated with the unit vs separate tree (MAINT-C06): sync vs tooling convention.
51. Registry content deployed by script vs migration (MAINT-C30): authoring fit vs one delivery path.
52. Versioned vs coordinated interfaces (MAINT-C31): consumer independence vs cost, with few in-house consumers.
53. Function with signature vs view as stable interface (MAINT-C45): change absorption vs simplicity.
54. Scheduler inside the data store vs dedicated orchestrator (MAINT-C47): fit, atomicity vs exit risk.
55. Design for probable future use vs YAGNI (MAINT-C66): reversibility vs delivery speed.
56. Guidelines induced from practice vs deduced (MAINT-C59).

### 4. Central-decision candidates, merged (grounded: each slot's own L2 list; "slots" = which slots name it)

- A. Default stance: import, build or rent, and the necessity test. Slots 01 (D-SRC-1), 02 (D1), 07 (4).
- B. Selection: criteria set, depth by criticality, who may choose, novelty budget. Slots 01 (D-SRC-2, 3, 4), 02 (D1 in part).
- C. Dependency lifecycle: pin policy and lockfile contract, update cadence and delay, trust boundary, inventory. Slots 02 (D2, D3, D4, D6); 04 (5, artifact and provenance) touches it.
- D. Containment and exit: wrapper rule, exit and end-of-life, external-service requirements before a hard dependency. Slots 01 (D-SRC-5), 02 (D5, D7).
- E. Release model and integration discipline (branch lifetime, protection, versioning). Slots 04 (1, 2); 07 (2).
- F. What is releasable: test-level mix and unit definition, gate policy and time budget, double policy, static-analysis enforcement. Slots 03 (1, 2, 3, 5), 04 (4).
- G. Review mechanism and latency budget. Slot 04 (3).
- H. Rollout, rollback and production verification, with the error-budget consequence for releases. Slots 03 (6), 04 (6), 05 (D2), 07 (2).
- I. Environment set, parity, and how tests run safely. Slots 04 (7), 06 (10), 07 (1, 2).
- J. How service boundaries are verified and evolve. Slots 03 (4), 07 (3).
- K. Reliability targets: critical journeys, SLIs, SLO owner, error-budget policy. Slot 05 (D1, D2).
- L. Paging, on-call, severity, postmortem triggers and tracking. Slot 05 (D3, D5).
- M. Telemetry standard, storage model, sampling, retention. Slot 05 (D4).
- N. Documentation: taxonomy by sync mechanism, definition-of-done trigger, gate, ownership, who verifies, interface source of truth. Slot 06 (1 to 6).
- O. Security: anchoring framework, threat-model depth, block vs advise. Slot 06 (7, 8); 02 (D4) touches it.
- P. Secrets and configuration model. Slot 06 (9).
- Q. How delivery is measured. Slot 04 (8).
- R. TDD stance and replacement of coverage as health signal. Slot 03 (7).
- S. Derived-data correctness; what automation and AI agents may execute. Slot 07 only (5, 6).

### 5. Where the maintainer doctrine contradicts the public slots (by claim id; grounded in claim texts; "partial" = tension, not opposition)

- MAINT-C26 (manual production gate and manual lane) vs DELIVER-C36 (same automated process for every environment, any version on demand). It sits within the contested range of DELIVER-C33.
- MAINT-C64 (route environment differences) vs DELIVER-C42, TRANS-C55, and DELIVER-C36 (same process everywhere).
- MAINT-C66 (design for probable future use) vs ADOPT-C04 (no speculative building).
- MAINT-C31 (coordinated breaking changes deployed together) vs DELIVER-C48 and VERIFY-C23 (independent deployment); partial vs ADOPT-C30 and SRC-C14. Compatible with DELIVER-C12 for single-version services.
- MAINT-C30 (registry content by script, outside migrations) vs DELIVER-C45 (database changes in the same pipeline).
- MAINT-C01 (tests on shared real data behind rollback) vs VERIFY-C32 (isolate tests, double remote services); partial vs VERIFY-C40 (isolate test data).
- MAINT-C24 (written undo, no automatic down step) vs DELIVER-C39 (automated rollback); partial. Agrees with DELIVER-C40 (backward-compatible changes).
- MAINT-C54 (mandatory header with dated change log) vs TRANS-C09 and DELIVER-C10 (one canonical record; history in version control); partial. Agrees with TRANS-C07 on dating.
- MAINT-C34 (review escalated to named senior approvers) vs DELIVER-C20 (no per-change approval outside peer review); partial.
- MAINT-C67 (open: no automated regression run found), if confirmed, vs VERIFY-C02, VERIFY-C27, DELIVER-C21.
Not a contradiction despite the slot's own label: MAINT-C46 (built-in passed over only for a stated missing capability) matches ADOPT-C03 and SRC-C02 position (c). No public claim exists to contradict MAINT-C06, C45, C47, C59, C62, C63 (public slots silent).

### 6. Spot-check (grounded: sources fetched in this slot)

6 of 6 confirmed:
- 01: SRC-C31 vs AWS REL11-BP07: confirmed ("select dependencies with availability goals equal to or greater than the goals of your workload"); the "multiply availabilities" rationale is not on that page.
- 02: ADOPT-C15 vs Renovate pinning page: confirmed for the guarantee ("can no longer be guaranteed to lock anything"); the "fail on mismatch" part rests on a source not fetched here.
- 03: VERIFY-C31 vs Fowler, non-determinism: confirmed (separate suite, 8 tests, no longer than a week).
- 04: DELIVER-C17 vs Google review guide, small changes: confirmed (100 reasonable, 1000 too large; refactoring separate; tests with logic).
- 05: OPERATE-C34 vs SRE book (toil, on-call): confirmed (50% toil cap, 25% on-call, two incidents per 12-hour shift). The 1:1 alert ratio was not checked.
- 06: TRANS-C45 vs Twelve-Factor config: confirmed (config varies between deploys; open-source litmus test).

### 7. AI coding agents as contributors (recorded, not researched)

- Public: DELIVER-C49 only (keep batches small and commit often with AI-generated code; T2 DORA). Grounded.
- Maintainer: MAINT-C62 (one sanctioned, tool-enforced path for an agent), MAINT-C63 (agent writes the script, human runs high-blast-radius jobs); named as central decision 6 of slot 07. Contested positions: agent executes under approval (speed) vs writes only (control, audit). Grounded in the doctrine, no public source.
- Listed as not covered: AI-generated tests (VERIFY), AI-assisted doc-drift detection (TRANS, open), AIOps (OPERATE). Slots 01 and 02 have no mention (supply-chain and selection of agent-suggested packages not addressed; inferred from term search).

## L3 full

### Method (grounded)
- Read: brief_shared and the L1/L2 of slots 01 to 07 in full; L3 claim lines parsed by script for ids, claim text, cited source ids, tiers (from each register) and agreement. A claim counts as T3/T4-only when none of its cited sources is T1 or T2.
- Parsed claim counts: SRC 36, ADOPT 51, VERIFY 44, DELIVER 50, OPERATE 38, TRANS 58, MAINT 67.
- T3/T4-only claims by parse: SRC-C05, C18, C21, C22; ADOPT-C05, C12, C26, C42, C51; VERIFY-C28, C41; DELIVER-C41; OPERATE-C18, C19, C28b; TRANS-C12, C13, C17, C25, C26. VERIFY-C14 parsed with no source id, but its text cites S05 and S30 (parse artefact, not a gap).
- Term search over slots 01 to 06 (case-insensitive, hit counts): backup 0; disaster 1 (incidental, blue-green rehearsal); technical debt 0; decommission/sunset/retire 0; production readiness 0; privacy 1 (OPERATE, not covered list); accessibility 2 (VERIFY, not covered list); capacity 6 (all in not-covered or incidental lines); AI/agent: DELIVER-C49 and not-covered lines in VERIFY, TRANS, none in SRC, ADOPT.

### Overlap notes
- SRC claims tagged `boundary: ADOPT` (C02, C09, C12, C13, C35) are still recorded in both slots, so the "record once" rule of the brief was not applied there.
- DELIVER-C42 and TRANS-C55 cite the same Twelve-Factor page; ADOPT-C13 and TRANS-C54 likewise; VERIFY-C41 and OPERATE-C28b the same chaos source.

### Contested-topic count derivation
- Union of claim-level `contested` and each L2 "live debates", merged by topic. Public slots: 48. Maintainer only: 8 (items 49 to 56). Maintainer contested topics merged into public ones: MAINT-C24 (31), C26 (29), C46 (1), C54 (42), C64 (32).
- Debates listed in an L2 whose claim is marked majority (counted): SRC-C17, C19; ADOPT-C19, C20; VERIFY static types; OPERATE-C12; TRANS parity vs isolation, executable examples. Dropping those would reduce the public count.

### Spot-check evidence (sources fetched, quotes as returned by the fetch tool, which summarises pages)
- AWS Well-Architected REL11-BP07: "select dependencies with availability goals equal to or greater than the goals of your workload"; anti-pattern "Setting SLAs without taking into account for dependencies and their underlying SLA".
- Renovate, Dependency Pinning: "If a lock file gets out of sync with its package.json, it can no longer be guaranteed to lock anything"; apps pin all types, libraries keep ranges.
- Fowler, Eradicating Non-Determinism: quarantine suite separate; "only allow 8 tests in quarantine"; "no longer than a week".
- Google eng-practices, Small CLs: "100 lines is usually a reasonable size for a CL, and 1000 lines is usually too large"; refactoring separate; tests with logic.
- Google SRE book, Eliminating Toil and Being On-Call: toil below 50%; on-call no more than 25%; "2 per 12-hour on-call shift".
- Twelve-Factor, Config: config is "everything that is likely to vary between deploys"; open-source litmus test.
- Not checked: whether the cited T1/T2 pages are complete beyond these clauses; the one-source-per-slot sample cannot support a rate for the other claims.

### Open questions for the maintainer (inferred relevance)
- Which of G4 to G12 are in scope for the guideline (data change management and backup/recovery are the largest holes relative to the maintainer doctrine).
- Whether AI coding agents become a seventh area or a cross-cutting rule.
- Whether boundary claims duplicated across SRC and ADOPT should be merged before distillation.
