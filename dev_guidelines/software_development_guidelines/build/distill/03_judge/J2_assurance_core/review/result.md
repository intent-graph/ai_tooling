# J2_assurance_core review: result

## L1 headline

The unit is sound in its main decisions and not ready to build unchanged: fourteen clear defects need fixing (mostly overstated grounds and tiers, two internal contradictions) and eighteen subtle points go to the Opus pass. Certainty: grounded for the fixes (each rests on a fetched source or a register row), inferred for the flags.

Pin:
- Records reviewed: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3).
- Findings `fix`: 14 (R01 to R14).
- Findings `flag`: 18 (R15 to R32, including the judge's F1, F2, F3, F4, F6, F8, F9 carried, F10 as R21, F5 second half as R22).
- Sources fetched: 14; confirmed as cited: 11; partly confirmed: 2 (REG-1570, REG-098); not confirmed: 1 (REG-1042).

Headline points:
- F10 is mislabelled and circular: the 80% coverage floor is in J3 SECURITY.3, not SECURITY.4; J3 declines it and defers to BEHAVIOUR.6, which defers back (grounded).
- F7 and F11 are settled and need no flag (grounded: fetched GitHub documentation confirms a skipped required check passes).
- F9 carried as flag, no text proposed, as planned.

## L2 claims

Pin:
- Records reviewed: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3).
- Findings `fix`: 14 (R01 to R14).
- Findings `flag`: 18 (R15 to R32).
- Sources fetched: 14; confirmed as cited: 11; partly confirmed: 2 (REG-1570, REG-098); not confirmed: 1 (REG-1042).

Claims, each marked:
- No record averages, and no rule about who writes the code survives (checks 1, 5): inferred, from reading all 20 records against the skeleton positions; three soft spots only (R19 pyramid as default, R17 policy MUST, R24 semver joined with explicit versioning).
- Every skeleton position and MAINT row is placed (check 3): grounded, compared position by position; one gap (BEHAVIOUR.4 P9, R07) and one missing record of a competing fix (cleanup against rebuild, R15).
- Every Rejected entry has a condition (check 4): grounded; RULES.5 and RULES.2 record none by design.
- Grounds overstate in six places (check 2): grounded. R01 (74% is a fix rate, not a cause), R02 (REG-048 is T2, not T3), R04 (REG-1042 does not support L1051; REG-1038 is one vendor source), R05 (types rest on T3), R12 (DLint does not support production-shaped data), R14 (CONTRACTS.3 lint and diff are T3).
- Two internal contradictions (check 7): grounded. R03 (RULES.4 "at or before integration" against "after merge"), R10 (BEHAVIOUR.7 "MUST roll back" against the disposable-store default). Cross-unit tension: R18 (static checks all block here, only high-confidence ones block in J3 SECURITY.2): inferred.
- Context without a row (check 6): R16 (post-merge review condition), R25 (single-team contract tests), R20 (scheduled job mechanism): grounded that the rows do not say it; whether it is wrong is for the Opus pass.
- Duplication (check 8): R08 and R13 are fixes; R22 (BEHAVIOUR.7 d5 to d9 mix decision and realization) is a flag.
- F10 (R21): the contradiction is not between SECURITY.4 and BEHAVIOUR.6. The 80% statement coverage floor is row L1126, P4 of SECURITY.3; J3 does not adopt it and points to BEHAVIOUR.6, which points back; the position is placed in neither Positions nor Rejected (grounded).
- Judge's flags: F7 and F11 settled; F1, F2, F3, F4, F6, F8, F9, F10 carried; F5 split (privacy pointer fixed in R11, decision-versus-realization mix flagged in R22).
- Source check: 11 of 14 fetched sources confirm the cited claim (REG-114, REG-094, REG-048, REG-1565, REG-052, REG-1564, REG-054, REG-1038, REG-1035, REG-204, REG-030); REG-1570 and REG-098 confirm the facts but not the judge's reading; REG-1042 does not support L1051.

## L3 full

Pin:
- Records reviewed: 20 (ASSURANCE; RULES, RULES.1 to RULES.5; BEHAVIOUR, BEHAVIOUR.1 to BEHAVIOUR.8; CONTRACTS, CONTRACTS.1 to CONTRACTS.3).
- Findings `fix`: 14 (R01 to R14).
- Findings `flag`: 18 (R15 to R32).
- Sources fetched: 14; confirmed as cited: 11; partly confirmed: 2 (REG-1570, REG-098); not confirmed: 1 (REG-1042).

The full finding lines, with proposed corrections and evidence, are in `findings.md` beside this file. Summary per node, by finding id:

- ASSURANCE (L1): R32 (F9, planned re-roll, no text).
- RULES.1: R01, R02 fix; R15, R26 flag. Quarantine with owner, cap and time limit, no bare sleeps and the rebuild argument are confirmed by REG-054 (grounded). The 74% figure is a fix rate (grounded, REG-1570 F.10).
- RULES.2: R13 fix (restatement of L1550). Placement, minutes of feedback and the P3 against P4 context are supported by L145 (grounded); numeric defaults are marked as such (F7 settled).
- RULES.3: no finding; F11 settled (grounded: REG-114 says required checks may be "successful, skipped, or neutral").
- RULES.4: R03 fix; R16, R27 flag. DORA finding on external boards confirmed (REG-094: "no evidence ... lower change fail rates", "negative impact"). The GitHub mechanisms are optional platform settings (REG-114).
- RULES.5: R04 fix. Same bar and accountability confirmed (REG-1035); executable check and evidence confirmed in REG-1038 only (single vendor source).
- BEHAVIOUR (L2): no finding of its own; inherits R17 to R23.
- BEHAVIOUR.1: R17, R28 flag.
- BEHAVIOUR.2: R05 fix; R18 flag.
- BEHAVIOUR.3: R02, R06 fix; R19 flag.
- BEHAVIOUR.4: R02, R07 fix.
- BEHAVIOUR.5: R20, R29 flag.
- BEHAVIOUR.6: R08, R09 fix; R21 flag. Coverage study confirmed (REG-1565: 31,000 suites, five systems, "low to moderate correlation ... when the number of test cases in the suite is controlled for"); Google "80% like a floor ... ceiling" confirmed (REG-048).
- BEHAVIOUR.7: R10, R11 fix; R15, R22, R26 flag.
- BEHAVIOUR.8: R12, R13 fix; R23, R31 flag.
- CONTRACTS (L2): no finding of its own.
- CONTRACTS.1: R24, R30 flag. Semantic versioning and AIP-180 confirmed (REG-030, REG-204).
- CONTRACTS.2: R25 flag.
- CONTRACTS.3: R14 fix.

F10, stated precisely (inferred nothing, all grounded in the two judged files and the skeleton):
1. J2 names SECURITY.4; the 80% statement-coverage floor is row L1126, position P4 of SECURITY.3.
2. J3 SECURITY.3 Decision contains no coverage target; its Rejected line leaves a numeric structural-coverage target to ASSURANCE.BEHAVIOUR.6; its flag F4 asks for a consistency check with J2.
3. J2 BEHAVIOUR.6 Flags says "J3 must reconcile". The two units each defer to the other; the NIST position (T1, REG-1081, REG-1086, REG-1094) appears in neither Positions nor Rejected.
4. BEHAVIOUR.6 Constraints: "MUST NOT a coverage number gate a merge as a quality target"; adopting the L1126 floor would contradict it.
Open for the Opus pass: whether BEHAVIOUR.6 lists the L1126 floor under Rejected with its condition.

Sources fetched (14), each with outcome:
- Confirmed as cited (11): REG-114, REG-094, REG-048, REG-1565, REG-052, REG-1564, REG-054, REG-1038, REG-1035, REG-204, REG-030.
- Partly confirmed (2): REG-1570 (numbers right, reading wrong), REG-098 (conditions differ).
- Not confirmed (1): REG-1042 as support for L1051.
