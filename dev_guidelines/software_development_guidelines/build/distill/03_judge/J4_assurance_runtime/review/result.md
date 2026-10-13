# Result: review of unit J4_assurance_runtime

## L1 headline

The unit is sound: all 15 records hold up, with no averaging, no author rules and no rejected position left without a condition. Six small defects need the judge's fix; seven subtle points go to the Opus pass. Marks: grounded.

Pinned:
- Records reviewed: 15 (ASSURANCE.PERFORMANCE, .1 to .5; ASSURANCE.AVAILABILITY, .1 to .5; ASSURANCE.ARTIFACT, .1, .2), 53 rows.
- Findings fix: 6 (fix-1 AVAILABILITY.3 certainty, fix-2 AVAILABILITY.1 client throttling missing, fix-3 AVAILABILITY.2 SDK rule missing, fix-4 PERFORMANCE.3 scheduling ground, fix-5 PERFORMANCE.4 decision lacks its exception, fix-6 PERFORMANCE.5 row L1563 uncited).
- Findings flag: 7 (flag-1 L265 against production tests, flag-2 and flag-3 duplication, flag-4 build-provenance floor, flag-5 game-day sequencing, flag-6 internals rule and warm-up narrowing, flag-7 breaker with long timeouts).
- Sources fetched and confirmed: 13 fetched, 13 confirm what the record cites, 3 with qualifications (REG-185, REG-1064, REG-242).

## L2 claims

Marks: G grounded, I inferred, O open.

Method
- G: all eight checks run on 15 records; checks 4 (rejected without condition) and 5 (author rules) found nothing; check 1 (averaging) found nothing: the split of PERFORMANCE.3 and the ladder of AVAILABILITY.5 are the rows' own conditional positions, not blends.
- G: 13 sources fetched: REG-226, REG-185, REG-1064, REG-086, REG-1053, REG-228, REG-220, REG-114, REG-209, REG-1056, REG-251, REG-242, REG-239. All 13 say what the record cites. Qualified: REG-185 (breaker may not protect against long timeouts), REG-1064 (no "once proven" ordering for game days), REG-242 (remedy is quieter infrastructure, not scheduling).
- G: row coverage: 52 of 53 rows cited; L1563 (node intent, no claim) is not (fix-6).

Fixes (the judge can apply)
- fix-1 AVAILABILITY.3 (G): REG-228, T1 and already cited, supports "pre-production by default, production after safeguards"; the record calls it unsourced.
- fix-2 AVAILABILITY.1 (G): L442's "throttle on the client" appears nowhere in .1 or .2; REG-220 states it.
- fix-3 AVAILABILITY.2 (G): L336's positive rule (use the provider's tested client, verify its retry defaults) is only in Rejected.
- fix-4 PERFORMANCE.3 (G): REG-242 read; it grounds "do not gate on a noisy signal", not "noisy tests go on a schedule"; F5 closes.
- fix-5 PERFORMANCE.4 (G): the Decision says "add production tests" without the exception that its own Context gives.
- fix-6 PERFORMANCE.5 (G): cite L1563.

Flags (for the Opus pass)
- flag-1 (I): J2's BEHAVIOUR.7 says no test touches production unless every effect is provably undone; PERFORMANCE.4 and AVAILABILITY.3 say only "test data isolated". Needs a joint wording.
- flag-2, flag-3 (G on the duplication, I on the remedy): production guardrails stated in PERFORMANCE.4 and AVAILABILITY.3; "gaps become tests" in AVAILABILITY.3 and .5 (MD-03).
- flag-4 (I): L2 floor for every deployed artifact is the stricter of two rows; the cost argument is uncited.
- flag-5 (I): game days "once proven" has no source; production-drill cadence is "regularly" only.
- flag-6 (I): internals-advice rule is one T2 body; the warm-up restriction has no row.
- flag-7 (I): the breaker trigger "long timeouts" meets REG-185's caution that a shorter timeout is the remedy.

The judge's F1 to F8: F1, F5, F8 settled by fetch; F6 settled, with the real gap in fix-2; F2, F3, F4, F7 carried as flag-4, flag-1, flag-6, flag-5.

## L3 full

Pinned, word for word:
- Records reviewed: 15 (ASSURANCE.PERFORMANCE, .1 to .5; ASSURANCE.AVAILABILITY, .1 to .5; ASSURANCE.ARTIFACT, .1, .2), 53 rows.
- Findings fix: 6 (fix-1 AVAILABILITY.3 certainty, fix-2 AVAILABILITY.1 client throttling missing, fix-3 AVAILABILITY.2 SDK rule missing, fix-4 PERFORMANCE.3 scheduling ground, fix-5 PERFORMANCE.4 decision lacks its exception, fix-6 PERFORMANCE.5 row L1563 uncited).
- Findings flag: 7 (flag-1 L265 against production tests, flag-2 and flag-3 duplication, flag-4 build-provenance floor, flag-5 game-day sequencing, flag-6 internals rule and warm-up narrowing, flag-7 breaker with long timeouts).
- Sources fetched and confirmed: 13 fetched, 13 confirm what the record cites, 3 with qualifications (REG-185, REG-1064, REG-242).

Per-finding lines, with node uid, check number, proposed correction and quoted evidence: `findings.md` in this folder (all 13 findings and the assessment of F1 to F8).

Per-check results on the 15 records
- Check 1 averaging (G): none. PERFORMANCE.2 to .5 and AVAILABILITY.2 pick conditional bests whose conditions are the rows' own (L422, L424, L427, L432, L338). ARTIFACT.1 takes the stricter floor: flag-4 (I).
- Check 2 grounding (G): 13 sources read. Exact confirmations: REG-226 (percentile thresholds, per-layer budgets, environment fidelity by criticality, real third-party calls, baseline refresh, hypothesis tests for high-impact changes, production guardrails); REG-1064 (tabletop, dry run, production drill, surprise game days, measured times as planning minimum, production drills can cause severe failures); REG-1053 (restore test criteria, integrity, measured time against RTO, same procedure as real recovery, automation); REG-086 (L2 and L3 definitions); REG-114 (admin bypass is off by default, so "bind every actor" needs the explicit setting); REG-220 (per-request and per-client retry caps, client throttling, degraded responses); REG-1056 (production failover regularly, few recovery paths); REG-251 (restore independent of migration tooling); REG-239 (coordinated omission mechanism); REG-209 (breaker for blocked threads and many callers, state changes logged); REG-185 (when not to use: dead-letter queues, platform breaking, retries sufficient); REG-228 (ladder, gaps into tests, fallbacks); REG-242 (noise). Defects: fix-1, fix-4.
- Check 3 missed positions (G): fix-2, fix-3, fix-6.
- Check 4 rejected without condition (G): none; every Rejected entry has a condition or a stated "best never".
- Check 5 author rules (G): none.
- Check 6 context creep (I): flag-5, flag-6 (conditions or sequencing no row states). All other contexts trace to a row.
- Check 7 consistency (G for fix-5, I for flag-1): fix-5 inside PERFORMANCE.4; flag-1 against J2 BEHAVIOUR.7. No contradiction with the decided nodes elsewhere in the unit: the AVAILABILITY.1 to .2 retry-cap split and the PERFORMANCE.3 placement rule (ASSURANCE.RULES.2) read consistently.
- Check 8 duplication (G): flag-2, flag-3. ARTIFACT.2 and AVAILABILITY.4 are properly index-linked to their realization nodes (MD-03).

Not done (O): the SSDF names (REG-004), HTTP semantics (REG-184), the Google SRE canary and workbook pages (REG-104, REG-203, REG-222), and the two measurement papers (REG-1578, REG-1579) were not fetched; the records already mark these inferred or single-source.
