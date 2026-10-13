# J2_assurance_core: result

Full records: `judged.md` in this folder; the review's fix findings R01 to R14 and the coverage-floor decision are applied there (section Review applied).

## L1 headline

Unit J2_assurance_core judged: the L1 node ASSURANCE and its L2 nodes RULES, BEHAVIOUR and CONTRACTS with their 16 L3 nodes. Headline (inferred as a roll-up, grounded in the child decisions): a property is guaranteed when a mechanism runs on every change, blocks on failure and gives a signal people believe (failures mean defects, gates fail closed, review is independent and binds the exact content, completion is shown by evidence); behaviour is pinned by self-testing code whose detection power is measured rather than assumed (coverage finds untested code, it is not a score); and interface compatibility has a definition, a contract test and one machine-readable source of description.

Pin:
- Nodes judged: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3).
- Decisions marked undecided: none.
- Flags raised: 11 (F1 to F11): F1 maintainer rollback-on-real-data (L265) against rebuild-not-clean-up (L111), settled by condition, maintainer to confirm production is excluded; F2 "independent human check" (L136) against MD-02, settled as independence plus a named accountable person, no row for a team of one; F3 the maintainer's practice may lack an automated suite trigger (L331); F4 test-first (L080) against contested ordering (L101); F5 real records in tests and personal data, plus stack-specific rows inside BEHAVIOUR.7; F6 maintainer "no version numbers" (L295) limited to few reachable in-house consumers; F7 numeric defaults are single-source; F8 L275 and L276 may be misrouted; F9 the L1 claim covers three of nine L2 nodes; F10 the 80% statement floor (SECURITY.3, row L1126) is now decided in BEHAVIOUR.6: no coverage floor applies, security-relevant code included, a conformance minimum only where a baseline mandates it (J3 points here); F11 fail-closed skipped checks rests on one platform fact.
- Settled decisions disagreed with: none.
- Review fixes applied: 14 of 14.

## L2 claims

Marks: G grounded, I inferred, O open. Each claim is also the L2 or L3 decision in `judged.md`.

Pin (word for word, as at L1): Nodes judged: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3). Decisions marked undecided: none. Flags raised: 11 (F1 to F11), listed under L3. Settled decisions disagreed with: none. Review fixes applied: 14 of 14.

ASSURANCE
- [I] Every property rests on a named mechanism at a named stage that runs on every change, blocks, and has a trustworthy signal; no property rests on one mechanism or the author's judgement. Partial: three of nine L2 nodes (F9).

RULES (common rules)
- [G] RULES.1 Trustworthy signal: prevent non-determinism at its cause; quarantine existing flakes outside the gate with owner, cap and time limit, then fix or delete; every blocking check has a stated false-alarm budget (numbers are one organisation's: I).
- [G] RULES.2 Placement and speed: lowest level and earliest stage that can catch the failure, minutes of blocking feedback, recorded policy per stage and risk, several kinds of check (combining: I). Context: very high volume with automatic rollback gates the fast and runs slow checks after merge; otherwise staged before release.
- [G] RULES.3 Gates: a rule that matters is a blocking automated check; skipped, neutral or missing counts as failed; boundaries and fitness properties are checked automatically (fitness functions: I).
- [G] RULES.4 Review: before integration, independent of the author, a named accountable person, approval bound to the exact content, no per-change external board; only a pre-defined low-risk tier may be reviewed after merge (tier: I; regulatory exception: O).
- [G] RULES.5 One bar: same bar for design, testing and review whatever the author (G); executable check and evidence (one T1 vendor source); acceptance fixed first and independent test contexts (I).

BEHAVIOUR
- [G] BEHAVIOUR.1 The code is self-testing on every change; strict "everything not to break has a test" under high criticality or many consumers, risk-scaled otherwise; written policy and evidence; suite judged by detection; the maintainer's missing trigger (O) is rejected.
- [G] BEHAVIOUR.2 Types, lint and analysis are the first blocking layer (types as first layer: I); warnings as errors; an analyser beyond the compiler before major release; types enforced for large long-lived code, gradual on existing code (trend watching: I).
- [G] BEHAVIOUR.3 Many small, few broad, few end-to-end; proportions recorded; integration-heavy for interaction-dense systems, static plus integration for user-interface applications (which shape fits which context: I).
- [G] BEHAVIOUR.4 Observable behaviour through public interfaces; tests are production code; real, then fake, then mock; state over interaction verification; integration against the production kind of backing service; record unit definition and double style (classical against mockist: contested, I).
- [G] BEHAVIOUR.5 Every reported defect becomes a fail-first test; characterization tests before changing poorly understood code; scheduled job tested at unit level before scheduling (I); test-first ordering is context, not a rule (I).
- [G] BEHAVIOUR.6 Coverage finds unexecuted code, never a quality gate or target, and no coverage floor applies to security-relevant code either (it needs fuzzing, threat-derived tests and review of unexecuted branches; a numeric floor only as conformance where a baseline mandates it, I); mutation testing diff-based for high criticality and mature suites (I); property-based testing (I); fuzzing of input handling, required for security-relevant code (G).
- [I] BEHAVIOUR.7 No test leaves a durable effect on data others rely on: disposable store per run by default, rollback boundary only when data cannot be cloned and every effect is undoable; plus eight maintainer-based sub-decisions on fixtures, vehicle, verdict shape, placement, configuration namespace, fixture variables, conditional mutations.
- [I] BEHAVIOUR.8 Exercise every branch with production-shaped data and guard inputs; hard check on silent truncation; verify unclear platform behaviour on a live instance; symptom-indexed pitfall catalogue; no blanket search-and-replace across mixed contexts.

CONTRACTS
- [G] CONTRACTS.1 Additive is compatible, removal, rename, type, default or behaviour change breaks; never silent: explicit versioning with deprecation window for many, external or independent consumers, additive plus coordinated deploy for few reachable in-house ones (threshold: I).
- [G] CONTRACTS.2 Contract tests, not shared integrated environments, between independently released parts; every double of an external service backed by a contract test on the supplier's rhythm; consumer-driven where consumers are known, schema validation where unknown, both for different questions (single-team application: I, O at source).
- [G] CONTRACTS.3 One machine-readable description from which docs, stubs, types and tests derive; linted and diffed in CI, fail on incompatible change (tool capability at T3, CI blocking: I); code-first for one owner of both ends, design-first for independent consumers (origin condition: I).

## L3 full

Pin (word for word): Nodes judged: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3). Decisions marked undecided: none. Flags raised: 11 (F1 to F11). Settled decisions disagreed with: none. Review fixes applied: 14 of 14.

Per node: decision, grounds with row and register ids, rejected with the condition under which each would be best, context, certainty, flags. The complete seven-field records, constraints and links are in `judged.md`; they are repeated here in condensed form so that this level stands alone.

### ASSURANCE
- Decision: each property that must hold has a mechanism at a stage that runs on every change, blocks on failure and has a trustworthy signal; outcome: design, testing and review were good and what runs is what was reviewed (MD-02).
- Grounds: roll-up of RULES, BEHAVIOUR, CONTRACTS; L1538, L1550, L1558, L1562, L1546.
- Rejected: none (no rows). Context: none. Certainty: inferred, partial roll-up. Flags: F9.

### RULES (31 rows)
- Decision: a check is worth running only if its failure means a defect, it runs low and early and returns in minutes, its rule blocks and cannot be skipped; review is independent and binds content; one bar and evidence for all change.
- Certainty: grounded principles, inferred numeric defaults. Flags: none at this node.

### RULES.1 Trustworthy Signal
- Decision: prevent non-determinism at its cause (isolated state, no bare sleeps, wrapped clock, doubled remote services, small tests, repeated check of new tests); quarantine existing flakes outside the gate with owner, cap and time limit, then fix or delete; state a false-alarm budget per blocking check and fix or remove a check above it.
- Grounds: L109, L110, L111, L147, L086, L1132, L1558, L1559, L1560; REG-048, REG-051, REG-052, REG-054, REG-056, REG-085, REG-1570, REG-004.
- Rejected: P2 remove at once (quarantine with zero time; best when no one will own a quarantine); P3 rerun marked tests (hides defects; acceptable as a capped part of quarantine or for infrastructure failures); P4 retry-only (same); P6 1% threshold as a rule (one T3 source, origin risky; best as a default budget when the team has no data); 10% false-positive figure (one organisation's policy).
- Context: none. Certainty: grounded for principle and causes, inferred for thresholds and transfer from Java studies. Flags: F1, F7.

### RULES.2 Placement and Feedback Speed
- Decision: lowest level, earliest stage that catches the failure; a higher-level miss yields a lower-level test; blocking feedback in minutes (about ten), build on every commit, broken build first; recorded policy per stage and risk; several kinds of check, none relied on alone.
- Grounds: L091, L1183, L112, L121, L145, L1550, L1538, L1546; REG-044, REG-072, REG-056, REG-057, REG-085, REG-004, REG-1561, REG-1564, REG-1554.
- Rejected: nothing outright; P3 (gate the fast, run slow after merge with rollback) is best at very high change volume with a build cop and automatic rollback, P4 (staged pipeline) at smaller volume.
- Context: change volume and rollback. Certainty: grounded for placement and speed, inferred for layering. Flags: F7.

### RULES.3 Gates That Cannot Be Skipped
- Decision: a rule that matters is a blocking automated check; the gate always runs and a skipped, neutral or missing required check counts as failed; module boundaries and fitness properties are automated.
- Grounds: L1562 (REG-114), L1216, L1234 (REG-1117, REG-1119, REG-1134).
- Rejected: convention or review alone for a mechanizable rule (best when the rule needs judgement, then it is review, RULES.4); small increments clause of L1234 is indexed to EVOLUTION (MD-03).
- Context: none. Certainty: grounded for the platform fact and the principle, inferred for fitness functions. Flags: F11.

### RULES.4 Independent Review That Binds
- Decision: every change to mainline is checked by a party other than the author, pusher or requester, on the platform record; a named person or role is accountable; approval binds the exact content and a changed diff voids it; no external per-change board, separation of duties met by peer review, automation and monitoring.
- Grounds: L136, L143, L1043, L1046, L1047; REG-083, REG-094, REG-098, REG-114, REG-115, REG-116, REG-1035, REG-1036, REG-1037, REG-1040.
- Rejected: review only the uncertain (Ship, Show, Ask; best as post-merge review of low-risk change where gates and revert are automatic); external board (best where a regulation requires one, regulated contexts deferred, MD-05).
- Context: risk sets the form of review. Certainty: grounded, risk-tiering inferred, regulation open. Flags: F2.

### RULES.5 One Bar and Evidence for Every Change
- Decision: same bar for design, testing and review whatever the author; intent, scope, interfaces, out-of-scope and acceptance fixed before the change is produced; executable independent pass or fail check; completion shown by evidence; tests and code from independent contexts where practicable.
- Grounds: L1042, L1045, L1051, L1052, L1053; REG-1035, REG-1036, REG-1038, REG-1040, REG-1041, REG-1042.
- Rejected: exemption for generated or trusted-author change (never best). Context: cost and speed of producing change (acceptance first matters more). Certainty: grounded for P1, P3, P4; inferred for P2, P5. Flags: none.

### BEHAVIOUR (61 rows)
- Decision: self-testing code on every change, types and static checks as the cheapest layer, a mix by confidence per unit time, behaviour-observing tests built as production code, change-driven tests, measured adequacy, no durable effect on data, production-shaped data for classes that survive review. Certainty: grounded for .1 to .4, inferred for .6 to .8. Flags: F3, F4, F5.

### BEHAVIOUR.1 What the Suite Must Promise
- Decision: suite runnable at any time on every change, a pass means no substantial defects; everything not to break has a test (strict under high criticality or many consumers, risk-scaled otherwise); written policy and evidence; judged by detection; accountable owner; results and triage recorded.
- Grounds: L080, L081, L082, L083, L122 (restated as outcome, MD-02), L123, L1551, L1552; REG-048, REG-056, REG-057, REG-063, REG-064, REG-067, REG-004, REG-1563.
- Rejected: P6 maintainer's absent trigger (L331, open; best for never-changed one-off code only); who-writes-tests rule (outside principles); strict form for every team (best under high criticality).
- Context: criticality, consumers. Certainty: grounded, strict/weak split inferred, P6 open. Flags: F3.

### BEHAVIOUR.2 Static Layer
- Decision: types, lint and analysis are the first blocking layer; warnings as errors; address linter warnings; one analyser beyond the compiler before major release; incremental, new-issues-first analysis in review; trend of warnings and complexity watched; types enforced for large long-lived code, gradual with an escape hatch on existing code.
- Grounds: L084, L085, L087, L088, L1054, L1547, L1548, L1549; REG-047, REG-065, REG-075, REG-004, REG-052, REG-1563, REG-1035, REG-1046.
- Rejected: tests alone (no source holds it; best for small short-lived code where annotation costs more than it prevents). Context: existing against new code. Certainty: grounded, trend inferred. Flags: none.

### BEHAVIOUR.3 Test Level Mix
- Decision: many small fast tests, fewer broad, few end-to-end on critical journeys; proportions recorded as a team decision; interaction-dense systems weight integration, user-interface applications static plus integration; larger tests where fidelity matters; describe tests on size and scope.
- Grounds: L089, L090, L092, L093, L117, L1182, L1188; REG-044, REG-045, REG-046, REG-047, REG-048, REG-051, REG-072.
- Rejected: fixed ratios 70/20/10 or 80/15/5 (team-specific, Google-like infrastructure); honeycomb or trophy as general shape (best by their contexts); minimal end-to-end where high-level tests are fast, reliable, cheap.
- Context: where complexity lives, logic density, team size, environment speed. Certainty: grounded for direction, inferred for shape-by-context. Flags: none.

### BEHAVIOUR.4 Test Construction
- Decision: observe behaviour through public interfaces, one test per behaviour; tests are production code (readable, DAMP, no logic, arrange-act-assert); real collaborators, else owned fakes, mocks last; state over interaction verification except for unobservable state-changing calls; integration against the production kind of backing service; record unit definition and double style.
- Grounds: L094, L095, L096, L097, L098, L099, L100, L1184, L1189, L1554; REG-044, REG-046, REG-048, REG-049, REG-050, REG-061, REG-062, REG-068, REG-1106, REG-1109.
- Rejected: mockist as default (best for outside-in design with costly collaborators); in-memory or different-engine backing store (best only where the production engine cannot run locally or in CI); 80/15/5 as a rule.
- Context: design style. Certainty: grounded, double style contested. Flags: none.

### BEHAVIOUR.5 Tests Driven by Change
- Decision: every reported defect becomes a fail-first test; characterization tests before changing poorly understood code; scheduled jobs tested at unit level and in reduced mode before scheduling; test-first ordering is a team decision by context.
- Grounds: L101, L106, L107, L316; REG-004, REG-056, REG-063, REG-064, REG-067, REG-072, REG-073, REG-181.
- Rejected: mandatory test-first (best for compilers, API design, tangled interfaces); fixing without a failing test (never).
- Context: ordering by problem type. Certainty: grounded for P2, P3; ordering contested, inferred; P4 inferred. Flags: F4.

### BEHAVIOUR.6 Measuring Adequacy and Probing for Faults
- Decision: coverage finds unexecuted code, no quality score, target or numeric gate, and no coverage floor for security-relevant code either (there: fuzzing, threat-derived tests, review of unexecuted branches); mutation testing diff-based for high-criticality code and mature suites; property-based testing where the input range is describable; fuzz input-handling code, required for security-relevant code.
- Grounds: L113, L114, L115, L116, L1553, L1555, L1556, L1557; REG-048, REG-058, REG-059, REG-060, REG-066, REG-074, REG-1563, REG-1565, REG-1566, REG-1567, REG-1568, REG-1569.
- Rejected: coverage floor as quality (best, inferred, for low-trust fast-growing teams as visibility); the 80% statement floor of SECURITY.3 row L1126 (best as a conformance minimum where a baseline mandates it); skip or offline mutation (best where compute or noise dominates).
- Context: criticality, suite maturity. Certainty: grounded for coverage finding (Java) and fuzzing, inferred for mutation and property tests, open for mutation effect size. Flags: F10 (resolved here).

### BEHAVIOUR.7 Tests Without Durable Effect on Data
- Decision: no durable effect on data others rely on; disposable store per run by default; rollback on shared or production-sized data only when cloning is impossible and every effect is undoable. d2 synthetic fixtures by default, curated real records where shapes are costly to fabricate; d3 vehicle by risk and runner; d4 platform idiom is a stack pointer; d5 self-reported verdict with unit and scenario identity; d6 tests where they change with the unit (colocated without a test tree, mirrored with a runner); d7 disjoint test configuration; d8 named fixture values set once; d9 conditional mutations.
- Grounds: L1185, L265, L111, L266 to L273; REG-1106, REG-051, REG-054, REG-181 (maintainer, not citable).
- Rejected: maintainer rollback as general rule (best under its stated condition); synthetic-only fixtures where shapes are rich; mirrored tree where tooling lacks a test tree.
- Context: data size and undoability, shape richness, tooling, human supervision. Certainty: grounded for d1 default, inferred for the rest. Flags: F1, F5.

### BEHAVIOUR.8 Defect Classes That Survive Review
- Decision: exercise every branch with production-shaped data and guard inputs always; hard check where a platform silently truncates or coerces; verify unclear platform behaviour on a live instance and record its scope; symptom-indexed pitfall catalogue, entry after any defect found twice; no blanket search-and-replace across mixed contexts.
- Grounds: L274 to L278 (REG-181), L1550 (REG-1561, REG-1564), L107.
- Rejected: static analysis and types alone (best for the part they catch, kept as BEHAVIOUR.2).
- Context: none. Certainty: inferred (maintainer practice, one dated corroborating study). Flags: F8.

### CONTRACTS (18 rows)
- Decision: compatibility has a definition, is verified by contract tests, and each interface has one machine-readable description with an automated breaking-change diff. Certainty: grounded for definition and principle, inferred for style choices. Flags: F6.

### CONTRACTS.1 What Counts as Compatible
- Decision: precise public interface; additive is compatible, removal, rename, type, default and behaviour change break; breaking change never silent: explicit versioning with at least one minor of deprecation for many, external or independent consumers, additive evolution with coordinated deploy and dated change log for few reachable in-house consumers; plan for implicit dependencies (Hyrum's Law).
- Grounds: L060 (REG-030), L352 (REG-204), L105 (REG-071), L295 (REG-181).
- Rejected: maintainer's no-version rule as general (cannot hold with independent release; chosen for few reachable consumers); explicit versioning for every interface (costly where consumers are few).
- Context: number and reach of consumers. Certainty: grounded for definition, inferred for the threshold. Flags: F6.

### CONTRACTS.2 Contract Tests
- Decision: contract tests, not shared integrated environments, between independently released components; every external-service double backed by a contract test on the supplier's rhythm, failure creates a realignment task and need not break the build; consumer-driven contracts for known consumers, schema validation for unknown ones, both for different questions.
- Grounds: L102, L103, L104, L1186, L1187, L1281, L1282, L1283; REG-044, REG-046, REG-053, REG-054, REG-070, REG-1152, REG-1157.
- Rejected: consumer-driven alone for unknown consumers; schema alone for known consumers (cheaper setup and published spec win for unknown ones, strongest version not independently sourced); shared integrated environments (best when all consumers deploy together).
- Context: number of consumers and independence of cadences. Certainty: grounded for P1, P4, P6; single-team case inferred and open at source. Flags: none.

### CONTRACTS.3 One Source of Description
- Decision: one machine-readable description from which docs, stubs, types and tests derive; linted against a ruleset and diffed against main in CI, failing on incompatible change; the diff covers description only so contract tests remain; code-first when one team owns both ends, design-first for independent consumers; record where the chain of types starts.
- Grounds: L220, L221, L222, L1271, L1277, L1284; REG-147, REG-158, REG-160, REG-164, REG-1150, REG-1154, REG-1158, REG-1159, REG-1160.
- Rejected: hand-copied descriptions (never); code-first for independent consumers (generated descriptions flagged incomplete); design-first for one owner of both ends (a second artifact to sync).
- Context: who owns both ends; shape against storage. Certainty: grounded for single source, lint, diff; origin condition inferred and contested. Flags: none.

### Flags raised (11)
- F1 (BEHAVIOUR.7, RULES.1): L265 against L111; decided by condition; confirm that production itself is excluded.
- F2 (RULES.4): "independent human check" against MD-02; decided as independence plus a named accountable person; no row for a team of one.
- F3 (BEHAVIOUR.1): maintainer's practice may lack an automated suite trigger (L331, open).
- F4 (BEHAVIOUR.5, BEHAVIOUR.1): L080 tests first against contested L101.
- F5 (BEHAVIOUR.7): real records in tests and personal data; stack-specific L268 and L272, practice-level d8 and d9 in an assurance node.
- F6 (CONTRACTS.1): "no version numbers" (L295) limited to few reachable in-house consumers.
- F7 (RULES.2, RULES.1): numeric defaults are single-source.
- F8 (BEHAVIOUR.8): L275 and L276 may belong in OPERATION.FEEDBACK or CHANGE_FLOW.
- F9 (ASSURANCE): L1 claim covers three of nine L2 nodes; re-roll in wave 3.
- F10 (BEHAVIOUR.6, resolved): the 80% statement floor is in SECURITY.3 (L1126), decided here; J3 points to BEHAVIOUR.6.
- F11 (RULES.3): fail-closed skipped checks rests on one platform fact (REG-114).
