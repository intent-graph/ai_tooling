# Review result: unit J7_operation

## L1 headline

J7_operation is sound: decisions are conditional-best, not averaged, and consistent with the settled J3 and J4 records (grounded). Seven clear defects need a judge edit, mostly misreadings of sources and one omission in the L1 roll-up (grounded); eleven subtle points go to the Opus pass (inferred).

Pin:
- Records reviewed: 39 (1 L1, 9 L2, 29 L3), against 109 ledger rows, the OPERATION skeleton records, J3, J4 and cross_unit_fixes.
- Findings fix: 7 (R-01 to R-07).
- Findings flag: 11 (R-08 to R-18).
- Sources fetched and how many confirmed: 14 fetched (T1 and T2); 9 confirmed in full, 5 confirmed in part.

## L2 claims

Pin (same words as L1):
- Records reviewed: 39 (1 L1, 9 L2, 29 L3).
- Findings fix: 7 (R-01 to R-07).
- Findings flag: 11 (R-08 to R-18).
- Sources fetched and how many confirmed: 14 fetched; 9 confirmed in full, 5 confirmed in part.

Claims:
1. No averaging, no missed positions, no author rules (checks 1, 3, 5): grounded. Every skeleton position and all 109 rows are placed; one soft blend (four golden signals against the three-signal set) is flagged R-12.
2. Consistency with settled records: grounded. No contradiction with J3 (DATA_INTEGRITY.3, .4, DOCS_SYNC.3, SECURITY.7), J4 (PERFORMANCE.1, .2, .5, AVAILABILITY.4, .5) or cross_unit_fixes. Two cross-unit wording points go to Opus (R-13 current-performance wording, R-14 percentile rule stated in J4 and J7) and one gap (R-15: no backup retention rule in OPERATION.RECOVERY though DATA_INTEGRITY.3 asks for tiered retention; open).
3. Grounding holds with three source misreadings (fix): grounded. R-01 (on-call familiarity: the operating team's own engineers, not builders), R-02 (incident system changes belong to the operations lead and team, not one operator), R-07 (agreement on the budget policy is in REG-134, not REG-133).
4. Duplication and boundary (fix): grounded. R-03 (L1 roll-up omits FEEDBACK), R-04 (personal-data rule belongs to TRANSVERSE.PRIVACY), R-05 (completed-job rejection restated; TELEMETRY.1 link missing), R-06 (RELIABILITY lacks its realize link to AVAILABILITY).
5. Flags for Opus (inferred): R-08 small-service threshold claim not in the source; R-09 a MUST on the unsourced telemetry budget; R-10 standby versus single path rests on a source about code-level fallback; R-11 high-bar incident declaration rejected for a condition it is never applied to; R-12 TELEMETRY.1 blend and split; R-16, R-17, R-18 certainty of F5, F8, F9 points.
6. Judge flags: F1, F2, F4, F5, F8, F9 carried; F3, F6, F7, F10, F11 settled and accepted.

## L3 full

Pin (same words again):
- Records reviewed: 39 (1 L1, 9 L2, 29 L3), checked against the nine ledger-row groups of the OPERATION skeleton branch, the judged records of J3 and J4, and cross_unit_fixes (X1 to X3, none touches J7).
- Findings fix: 7 (R-01 to R-07).
- Findings flag: 11 (R-08 to R-18).
- Sources fetched and how many confirmed: 14 fetched; 9 confirmed in full, 5 confirmed in part.

Sources, by register id, with node and result:
- REG-122 (W3C Trace Context, TELEMETRY.4, .5): confirmed in full (traceparent and tracestate; untrusted caller can overwhelm tracing; no personal data in headers).
- REG-231 (AWS operational readiness review, READINESS.1 to .3): confirmed in full (periodic re-run, yearly subset in the example, about thirty items, checklist from incidents, guardrails, self-service certification, executive sponsor).
- REG-134 (Implementing SLOs, RELIABILITY.1 to .3): confirmed in full (journeys, five or fewer indicators, start from existing data and iterate, stakeholders must agree).
- REG-1055 (AWS recovery strategies, RECOVERY.4): confirmed in full (ladder, never more stringent than needed, push-button manual failover, failback is data re-synchronisation, active/active only when requirements demand it).
- REG-129 and REG-113 (SRE toil and introduction, INCIDENTS.3): confirmed in full (50 percent cap on aggregate operational work, about two events per shift).
- REG-235 (Prometheus instrumentation, TELEMETRY.6): confirmed in full (bound cardinality, instrument everything, care above about 100k calls per second).
- REG-1074 (Meta outage, RECOVERY.5): confirmed in full (trade-off between day-to-day security and slower recovery; tools broken by the failure).
- REG-128 (Embracing Risk, RELIABILITY.2, .4): confirmed in full (100 percent wrong target; release halt on exhaustion; product team self-polices).
- REG-133 (error budget policy, RELIABILITY.3, .4): confirmed in part (freeze except P0 and security fixes, escalation to an executive, 20 percent in four weeks postmortem; no statement that product and operations must agree: R-07).
- REG-132 (alerting on SLOs, ALERTING.2): confirmed in part (precision, recall, reset time, page for fast burn and ticket for slow; says nothing that small services favour thresholds: R-08).
- REG-130 (Being On-Call, INCIDENTS.3): confirmed in part (25 percent on-call, two incidents per 12-hour shift, eight engineers single-site, 1:1 ratio; the familiarity sentence concerns the rotation's own engineers: R-01).
- REG-127 (Managing Incidents, INCIDENTS.1): confirmed in part (roles and declaration criteria; changes by the operations team, not one person: R-02).
- REG-1075 (avoiding fallback, RECOVERY.4): confirmed in part (rarely run fallback is a latent bug; the case is request-time code, not disaster-recovery standby: R-10).

Findings: the full list, with evidence, is in findings.md beside this file (R-01 to R-18, then the F1 to F11 assessments and the checks with no finding). Method note: fetched pages were read through a summarising fetch tool, so quotes are as returned; each corrective finding rests on a quoted passage.

Not done: REG-124, REG-125, REG-131, REG-1061 to REG-1063, REG-1067, REG-1072, REG-1073 were not fetched; claims resting only on them stay marked as the judge left them (inferred or grounded by ledger notes).
