# J2_assurance_core: final pass applied

## L1 headline

J2 `judged.md` is final: all 16 resolutions of the J2 section and the cross-unit lines X1, X4, X5, X7, X13, X14 are applied (grounded: each edit matched exactly one place in the file); R32 and X2 (the ASSURANCE re-roll) are not applied by design, X3 is superseded by X7. No node was added. Open: flag F9 (wave-3 re-roll) and the maintainer point on ASSURANCE.RULES.4, whose default is written and marked open in its Certainty.

## L2 claims

Resolutions applied (grounded, `judged.md` section "Final pass applied" lists each):
- R15, R26 (F1): applied. RULES.1 Decision, P8 in Positions and Rejected; BEHAVIOUR.7 unchanged in substance.
- R16: applied. RULES.4 tier sentence, Rejected, Certainty (tier conditions grounded in REG-098; rejection reason inferred).
- R17: applied. BEHAVIOUR.1 Decision and Constraint (evidence = the tests in each change).
- R18: applied through X4.
- R19: applied. BEHAVIOUR.3 first sentence replaced (mapping inferred).
- R20: applied. BEHAVIOUR.5 clause and Constraint ("MUST a scheduled job pass its tests before it is scheduled").
- R21 (F10): applied, unchanged in substance. Flag cleared.
- R22 (F5): applied. d5, d6, d8 moved from BEHAVIOUR.7 to BEHAVIOUR.4 (inferred); d4 a stack pointer only.
- R23: applied. BEHAVIOUR.8 first sentence and Constraint.
- R24: applied through X7.
- R25: applied. CONTRACTS.2 Context second clause (inferred, L1187 open).
- R27 (F2): applied as the maintainer default, merged with R16 text in the RULES.4 Decision.
- R28 (F3), R29 (F4), R30 (F6), R31 (F8): applied, unchanged in substance; flags cleared.
- R32 (F9): not applied, by design (wave-3 re-roll, X2).
- F7, F11 (closed by the review): flags cleared.

Cross-unit lines:
- Applied: X1 (already in place in BEHAVIOUR.6, nothing to change), X4 (RULES.1 holds block-or-advise; BEHAVIOUR.2 uses it), X5 (BEHAVIOUR.7 d1, pointer to AVAILABILITY.3), X7 (CONTRACTS.1 policies, L353 as a row), X13 (BEHAVIOUR.5), X14 (RULES.4 holds the reason).
- Not applied: X2 (wave 3, F9 stays open); X3 superseded by X7. X6, X8 to X12 do not name J2.

Nodes added: none (inferred: no J2 resolution creates a node; none is listed).

Flags still open (grounded): F9 on ASSURANCE; the RULES.4 maintainer point ("open: awaiting the maintainer's answer on whether an automated reviewer can be the independent check"), default applied.

## L3 full

### Resolutions applied (grounded unless marked)

- R15, R26 (F1): RULES.1 Decision now "isolate each test: each test establishes the state it needs instead of relying on another test's clean-up; where rebuilding per test costs too much, the undo is done by the platform (a rolled-back transaction, a snapshot restore), never by hand-written clean-up code". Positions add P8 (L1560); Rejected adds P8 (REG-054; best only where neither rebuild nor platform undo exists, each test then checking its precondition at its start, inferred). BEHAVIOUR.7 kept; its Grounds now state that the rollback is the platform undo and that "no durable effect anywhere" is the maintainer's own rule (L265).
- R16: RULES.4 Decision: only a tier defined in advance (established pattern, unremarkable fix, documentation), in a team whose mainline is kept releasable by automated gates and fast revert, may be checked after merge. Rejected: review only for uncertain changes leaves the classification to the author at the moment of the change, a tier defined in advance removes that discretion (inferred); "Ship" with no review: best never under this node. Certainty: tier conditions grounded in REG-098 (one practitioner source, fetched in review).
- R17: BEHAVIOUR.1 Decision, Grounds, Position P4 and Constraint now say: a written test policy exists (new functionality and every fix come with automated tests); the evidence that it is followed is the tests in each change, visible in its review, with no separate artefact.
- R19: BEHAVIOUR.3 Decision starts "The mix follows from RULES.2 ... where logic lives inside units many small fast tests ...; where failures arise in interactions between services, the weight moves to integration tests; for user-interface code, to static checks plus integration tests. End-to-end tests stay few ... proportions recorded as a team decision with the reason". The rest is unchanged, so one later sentence repeats the interaction and user-interface clause (redundancy only, left as the resolution said "rest unchanged"). Certainty: the mapping is inferred.
- R20: BEHAVIOUR.5 Decision: "a scheduled job is tested before it is scheduled like any other unit, and its first runs on real data are bounded and inspected (for example a reduced-scope test mode)"; Constraint: "MUST a scheduled job pass its tests before it is scheduled". Grounds: L316 is maintainer-only, outcome holds, mechanism one example.
- R21 (F10): unchanged in substance. BEHAVIOUR.6 Flags cleared; the NIST IR 8397 (REG-1086) ground for a mandated minimum and the MD-05 deferral are recorded in the Flags line.
- R22 (F5, second half): BEHAVIOUR.7 keeps d1, d2, d3, d7, d9; d4 stays a stack pointer; d5 (self-reported verdict), d6 (where tests live), d8 (named fixture values) are now sub-decisions of BEHAVIOUR.4 with positions P10 to P12, the mirrored-tree rejected line, the d6 context, stack pointer L272 and certainty inferred (maintainer practice only). BEHAVIOUR.7 Intent, Grounds, Positions, Rejected, Context, Certainty, Links adjusted accordingly.
- R23: BEHAVIOUR.8 Decision first sentence: data-dependent code (queries, parsing, conversions, coercing or truncating platforms) is exercised on production-shaped data, edge values included, before it ships; inputs guarded at boundaries always. Constraint: "MUST data-dependent code be exercised on production-shaped data before it ships". Grounds note "every branch" was a coverage target BEHAVIOUR.6 rejects.
- R25: CONTRACTS.2 Context second clause replaced by the text of the resolution (single-team application whose client and server always deploy together verifies its own seam with integration tests and the CONTRACTS.3 diff; where old clients stay in use the independent-release rule applies; doubles of external services follow the contract-test rule in both cases). Certainty: inferred, L1187 open.
- R27 (F2): RULES.4 Decision now reads the maintainer default: a party other than whoever authored, pushed or requested the change, "working from its own context: a person or an automated reviewer; for a change the team's risk tier marks high, the reviewer is of a different kind from the author"; a named person or role stays accountable, approves and can defend it. Certainty (inferred, marked open): "open: awaiting the maintainer's answer on whether an automated reviewer can be the independent check". Flags field: none (the point lives in Certainty).
- R28, R29, R30, R31: records unchanged in substance; flags F3, F4, F6, F8 removed with the settlement reason in a short parenthesis.
- F7, F11: flags cleared (closed by the review).

### Resolution not applied

- R32 (F9): ASSURANCE re-roll belongs to wave 3 (X2); the F9 flag stays on ASSURANCE.

### Cross-unit lines

- X1 applied (no change needed): BEHAVIOUR.6 already decides the floor (no coverage floor, security code included; conformance minimum where a baseline mandates it). J3's pointer is J3's edit.
- X2 not applied: wave-3 roll-up from all nine L2 nodes.
- X3 superseded by X7; no change.
- X4 applied: RULES.1 Decision, Constraints (blocking or advisory check has a budget; over budget is fixed or removed) and Links; BEHAVIOUR.2 Decision ("type checks, compiler warnings and the linter rules the team adopts block; analyses whose findings need judgement advise in review, as RULES.1 sets"), Grounds and Constraint. SECURITY.2 is J3's.
- X5 applied: BEHAVIOUR.7 d1 reads "a functional test never runs against production data unless every durable effect (rows, sequences, notifications, external calls) is provably undone; load and locks are transient effects governed by the guardrails of ASSURANCE.AVAILABILITY.3"; Links point to AVAILABILITY.3 and PERFORMANCE.4 (J4's edits).
- X7 applied: CONTRACTS.1 Decision holds the policies by consumer reach and artifact kind (few in-house reachable; library: semantic versioning with deprecation through at least one minor release; running service: new major version served alongside the old for a stated window; infrastructure-like API: indefinitely compatible date-pinned surface, L353 b); L353 is a row (P6); its (a) is read as the explicit-major branch; the consumer side stays on OWNERSHIP.SERVICES.2. Context, Rejected, Certainty (mapping of artifact kind to policy inferred), Links updated. OWNERSHIP.SERVICES.2 and EVOLUTION.DECOMMISSION edits are other units'.
- X13 applied: BEHAVIOUR.5 holds "a gap found becomes a test"; Grounds cite REG-228 as cited by AVAILABILITY.3; AVAILABILITY edits are J4's.
- X14 applied: RULES.4 Rejected holds the reason (inferred); the CHANGE_FLOW.REVIEW.1 pointer is J6's edit.
- X6, X8 to X12 do not name J2: not in scope.

### Nodes added

None.

### Flags still open

- F9 (ASSURANCE): the L1 claim covers three of nine L2 nodes; re-roll in wave 3 (X2).
- Maintainer point on ASSURANCE.RULES.4: can an automated reviewer be the independent check? Default (option A, with a different kind of reviewer for high-risk changes) applied; certainty inferred; open in the Certainty of the record.
- All other flags (F1 to F8, F10, F11) are cleared; `judged.md` lists each with its status in the "Flags raised" section.

### File changes

`judged.md`: 72 exact replacements, a status line on each flag in the closing list, a Pinned line, and the new closing section "Final pass applied". No absolute or home path was written.
