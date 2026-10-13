# Apply result: unit J4_assurance_runtime

## L1 headline

J4 judged.md is final: all 7 resolutions (flag-1 to flag-7) and 3 of the 4 cross-unit lines naming J4 (X5, X11, X13) are applied; X2 (the ASSURANCE L1 re-roll, wave 3) is not applied here because it is outside this unit's records. Nodes added: none. Flags still open: none (grounded).

Pinned:
- Resolutions applied: flag-1, flag-2, flag-3, flag-4, flag-5, flag-6, flag-7. Not applied: none.
- Cross-unit lines applied: X5, X11, X13. Not applied: X2 (wave 3 roll-up).
- Nodes added: none.
- Flags still open: none. Open text kept in Certainty: restore-test cadence (AVAILABILITY.4) and production-drill frequency (AVAILABILITY.5) have no source number.

## L2 claims

- Production-test guardrails now live once, in ASSURANCE.AVAILABILITY.3 (steady state or abort criterion, proven rollback, bounded blast radius, test data isolated, marked and removed, other durable effects suppressed or undone); PERFORMANCE.4 points there and keeps off-peak, ramp, reserved capacity; its constraints read "MUST apply the production-test guardrails of AVAILABILITY.3; MUST, for load, run off-peak, ramp from a small share and reserve capacity". Applied by flag-1, flag-2, X5. Grounded.
- A gap an experiment finds is a defect handled by ASSURANCE.BEHAVIOUR.5; AVAILABILITY.3 cites REG-228 directly and L451 leaves its grounds; AVAILABILITY.5 keeps "corrective actions update the plan" and points to BEHAVIOUR.5 for tests (flag-3, X13). Grounded.
- PERFORMANCE.1 points to OPERATION.RELIABILITY.1 for percentiles, drops L177, and reads "never from current performance as a final value; a provisional start from measured history follows OPERATION.RELIABILITY.2" (X11). Grounded.
- ARTIFACT.1: decision unchanged; the uncited cost claim is replaced by the fetched GitHub fact (attestations alone give SLSA v1.0 Build Level 2); grounded for one platform, inferred in general (flag-4).
- AVAILABILITY.5: unannounced game days follow announced exercises (inferred, reason stated); cadence "regularly and after changes", no number in sources (REG-1056, REG-1064) (flag-5). Grounded for the sources, inferred for the ordering.
- PERFORMANCE.5: decision unchanged; certainty restated (instance of measure before optimising; warm-up separation a scope, inferred) (flag-6). Grounded / inferred as stated.
- AVAILABILITY.2: breaker trigger is slow failure or many callers; a long timeout is shortened first; a breaker does not protect against long timeouts (REG-185) (flag-7). Grounded.
- Flags: all F1 to F8 settled; every record's Flags is "none". Judge flags F1, F5, F6, F8 confirmed closed. Grounded.
- Not applied: X2, an L1 roll-up of all nine L2 nodes (J2, J3, J4) done at wave 3, not by a unit applier. Grounded.
- Out of scope, noted: X5's BEHAVIOUR.7 d1 text belongs to J2's record and is not edited here; J4 only points to it. Grounded.
- Maintainer point: none for J4. Grounded.

## L3 full

Files: judged.md updated in place (29 text edits plus the rewritten "Flags raised" outcome list and a new final section "Final pass applied"); this file.

Resolutions, one by one:
- flag-1 (F3), ASSURANCE.PERFORMANCE.4, AVAILABILITY.3, X5: applied. AVAILABILITY.3 decision lists the shared guardrails and points to BEHAVIOUR.7 for the durable-data rule; load and locks are transient effects governed by the guardrails, not by BEHAVIOUR.7's d1. Constraints of AVAILABILITY.3 expanded to one MUST per guardrail. Links updated both ways (PERFORMANCE.4 requires AVAILABILITY.3). F3 removed.
- flag-2, PERFORMANCE.4, AVAILABILITY.3: applied as the resolution words them; PERFORMANCE.4's "MUST isolate test data" and four-guardrail MUST replaced by the two MUSTs quoted in L2; the Rejected line points to the guardrails of AVAILABILITY.3.
- flag-3, AVAILABILITY.3, AVAILABILITY.5, X13: applied. AVAILABILITY.3 grounds: "REG-228 (T1, cited directly ...; L451 leaves this node's grounds and stays a row of AVAILABILITY.5)"; constraint "MUST convert findings into tests" became "MUST treat a gap found as a defect handled by BEHAVIOUR.5". AVAILABILITY.5 decision, links, grounds adjusted.
- flag-4 (F2), ARTIFACT.1: applied; decision unchanged; grounds text replaced with the fetched fact and the L2-floor reasoning (L3 and reproducible rebuilds stay conditional; L1 best only without a hosted build platform); certainty: grounded for one platform, inferred in general; F2 removed from ARTIFACT.1 and the ARTIFACT parent.
- flag-5 (F7), AVAILABILITY.5: applied with the replacement texts of the resolution; grounds gain REG-1056, REG-1064; F7 removed; the cadence stays marked open in Certainty (no production-drill number in sources).
- flag-6 (F4), PERFORMANCE.5: applied; decision unchanged; certainty replaced; F4 removed.
- flag-7, AVAILABILITY.2: applied; the breaker sentence replaced and the shorten-first sentence added.
- Judge flags F1, F5, F6, F8: confirmed closed, removed from Flags; AVAILABILITY.1 keeps a note that retry caps are stated once in AVAILABILITY.2.

Cross-unit lines naming J4:
- X2: not applied (wave 3 roll-up of the ASSURANCE L1 node; no J4 record changes).
- X5: applied (above).
- X11: applied. PERFORMANCE.1 decision, grounds (L177 dropped), rejected, constraint ("MUST NOT derive from current performance as a final value") and links. PERFORMANCE.5 keeps L177 for its own distribution rule. OPERATION.RELIABILITY.1 and .2 are J7's records, unchanged here.
- X13: applied (above).

Nodes added: none. Maintainer point: none for J4. Contradictions between resolutions: none found; no record left unchanged for that reason.

Flags still open: none. Certainty items still open by source gap: backup-restore cadence beyond "regular" (AVAILABILITY.4); production-drill frequency (AVAILABILITY.5).

Checks: no absolute or home paths in judged.md; only this unit's folder written; nothing committed or pushed.
