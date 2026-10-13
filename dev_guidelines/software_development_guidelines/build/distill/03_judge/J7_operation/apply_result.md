# Apply result: unit J7_operation

## L1 headline

J7_operation is final: all 11 resolutions (R-08 to R-18) and the 3 cross-unit lines naming J7 (X8, X11, X12) are applied (grounded: edits made and re-read); none not applied. Nodes added: OPERATION.TELEMETRY.7 Vantage Points and OPERATION.TELEMETRY.8 Scheduled Work Signals. Flags still open: none. One reading call: R-10 says "second and fourth sentences" but the record's fourth is the failover sentence, so the standby and fallback sentences (two and three) were replaced (inferred).

## L2 claims

- Resolutions applied (grounded): R-08 ALERTING.2; R-09 TELEMETRY.6; R-10 RECOVERY.4; R-11 INCIDENTS.1; R-12 TELEMETRY.1; R-13 RELIABILITY.2 (via X11); R-14 RELIABILITY.1 (via X11); R-15 RECOVERY.2 (via X8); R-16 RECOVERY.5; R-17 RECOVERY.3; R-18 CAPACITY.3. Resolutions not applied: none.
- Cross-unit lines applied (grounded): X8 (RECOVERY.2 holds the retention clause, RECOVERY.3 points to RECOVERY.2 and TRANSVERSE.PRIVACY.3), X11 (RELIABILITY.1 holds the percentile rule, RELIABILITY.2 unchanged), X12 (TELEMETRY.1 split). Cross-unit lines not applied: none for J7; the other units' halves (DATA_INTEGRITY.3, DECOMMISSION.6, PERFORMANCE.1, DATA_INTEGRITY.4, PARADIGM.2 pointers) belong to J3, J4, J5, J8 and were left to them. X1 to X7, X9, X10, X13, X14 do not name J7.
- Nodes added (grounded): OPERATION.TELEMETRY.7 Vantage Points (L189, L1176, L453, L454; MUSTs: outside probe per critical user route, secure probe credentials); OPERATION.TELEMETRY.8 Scheduled Work Signals (L313; MUST monitor duration, failure, backlog, missed runs). Branch now 41 nodes (31 L3), 109 rows unchanged.
- Flags still open: none. F1 to F11 removed from every record's Flags (settled by resolutions, or closed by review for F3, F6, F7, F10, F11); the Flags raised list is kept as history with a note.
- Interpretation calls (inferred): R-10 sentence numbering (above), and the clause "active/active does not remove the need for backups" kept inside the replaced text; the TELEMETRY.8 log-and-re-raise habit sits in the decision with no separate MUST, as in the old record.
- Maintainer point ASSURANCE.RULES.4: J2 only, not applicable.

## L3 full

Edits by record (all in judged.md, which also carries a closing section "Final pass applied", one line per resolution and cross-unit line):

- Header: node count 41 (31 L3); F1 note and "Flags raised" line updated; DATA_INTEGRITY.4 bound to TELEMETRY.8.
- OPERATION L1, RELIABILITY L2, TELEMETRY L2, INCIDENTS L2, CAPACITY L2, READINESS, RECOVERY L2 and the L3 records: flags set to none.
- RELIABILITY.1 (R-14, X11): grounds say the percentile rule is held here and that PERFORMANCE.1 points here; Links add that PERFORMANCE.1 points here, PERFORMANCE.5 keeps its own rule.
- RELIABILITY.2 (R-13, X11): text unchanged; flag F1 removed.
- ALERTING.2 (R-08): decision now "where no objective exists, simple threshold alerts on the symptom are enough; where traffic is too low for a burn rate to be meaningful, use the source's remedies (synthetic traffic, combining services under one objective) rather than simple thresholds"; rejected thresholds line now "best where no objective exists"; context drops service size; grounds mention the fetched source.
- TELEMETRY L2 (X12): roll-up of .1 to .8; DATA_INTEGRITY.4 requirement via TELEMETRY.8.
- TELEMETRY.1 (R-12, X12): retitled "What Is Measured: Service and Resource Signals"; first sentence replaced as stated; keeps the four signals, the resource view (USE), per-statement statistics; its constraint is only the four signals; vantage-point and job content moved out.
- TELEMETRY.7 and .8 (X12): new records with the seven rows each (intent, decision, grounds, positions, rejected, context, certainty, flags, constraints, links). Certainty: .7 grounded, real-user inferred (T4 only); .8 grounded (single maintainer source, public agrees in direction).
- TELEMETRY.6 (R-09): per-service bound is a recommendation (SHOULD, inferred); label cardinality MUST kept.
- INCIDENTS.1 (R-11): Rejected P3 replaced: not a declaration rule (unsourced; REG-127 prefers early activation), tiny teams scale the response instead of raising the bar.
- CAPACITY.3 (R-18): the full-cycle MUST kept, marked inferred with the reason.
- RECOVERY.2 (R-15, X8): retention sentence added (tiered by age, L1092; oldest copy at least as long as undetected corruption (DATA_INTEGRITY.5) and legal retention require, no longer than TRANSVERSE.PRIVACY.2 allows, no number); links point to PRIVACY.2 and .3.
- RECOVERY.3 (R-17, X8): dual-authorisation replaced by "no single credential or person can delete every copy or shorten its retention: dual authorisation, or retention enforced as immutable by the platform", constraint likewise; pointers to RECOVERY.2 (retention) and TRANSVERSE.PRIVACY.3 (erasure, immutable lock); Links add ASSURANCE.SECURITY.6.
- RECOVERY.4 (R-10): replaced the standby and fallback sentences with the exercised-path text (convert to failover or remove); failover trigger and failback sentences kept; constraint and grounds aligned (REG-1075, REG-1055).
- RECOVERY.5 (R-16): certainty replaced as stated.
- RECOVERY.6 (X12): link now applies TELEMETRY.8.

Verification (grounded): every replacement asserted on a unique match; no record carries a flag other than none; 31 L3 headings counted. Not independently reviewed by a second agent.
