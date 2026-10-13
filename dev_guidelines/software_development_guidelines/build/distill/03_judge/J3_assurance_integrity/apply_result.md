# Apply result: J3_assurance_integrity

## L1 headline

J3 judged.md is final: all 7 resolutions (R5, R10, R11, R12, R13, R14, R15) and all 5 cross-unit lines naming J3 (X1, X4, X6, X8, X12) are applied (grounded: each checked against the record text). Nodes added: none. Flags still open: none; one open item remains in Certainty, the penetration-test period (SECURITY.3), for which no source gives a value (grounded). Resolutions not applied: none. Cross-unit lines not applied: none (X2, X3, X5, X7, X9, X10, X11, X13, X14 do not name J3). No maintainer point concerns J3.

## L2 claims

- Resolutions applied: R5 (DATA_INTEGRITY.3), R10 (DOCS_SYNC.2), R11 (DATA_INTEGRITY.1), R12 (SECURITY.2), R13 and R14 (SECURITY.3), R15 (SECURITY.6). Resolutions not applied: none. (grounded)
- Cross-unit lines applied: X1 (SECURITY.3 points to BEHAVIOUR.6, no coverage figure), X4 (SECURITY.2 points to RULES.1 and keeps release block, who may waive, REG-052 figure), X6 (SECURITY.6 holds the large-blast-radius principle, points to RULES.4 and CHANGE_FLOW.DATA_CHANGE.3 and .8), X8 (DATA_INTEGRITY.3 points to OPERATION.RECOVERY.2, TRANSVERSE.PRIVACY.2 and .3), X12 (DATA_INTEGRITY.4 points to OPERATION.TELEMETRY.8). Not applied: none. (grounded)
- Nodes added: none; OPERATION.TELEMETRY.8 belongs to J7 and is only linked. (grounded)
- Flags removed as settled: F1, F2, F3, F4, F5, F6, F7 and the roll-up flag lines; every record now reads "Flags: none". (grounded)
- Flags still open: none. Open in Certainty: penetration-test period, no source read gives one (grounded that none was found; the trigger rule itself is inferred).
- Two judgement calls inside the instructions (inferred to be faithful): R12's sentence is kept as a short statement with a pointer to RULES.1 rather than a full restatement, to honour X4 ("keeps only its own content"); the "(X8)" marker in R5's quoted clause is written as a pointer to TRANSVERSE.PRIVACY.2. (inferred)
- Observation, not changed: DATA_INTEGRITY.5 Decision contains a garbled fragment ("... removed. with an owner (inferred ..."); outside the final pass. (grounded)

## L3 full

Source of each change: `03_judge/final_pass/resolutions.md` section J3, `03_judge/cross_unit_fixes.md`, `03_judge/final_pass/maintainer_points.md` (no J3 point; item 7 of its second list restates X6 for SECURITY.6, consistent with the applied text).

Resolutions applied
- R5 (F2) DATA_INTEGRITY.3: decision first-layer clause now "reversible for a stated retention window, after which the kept copy is purged (periods for personal data: TRANSVERSE.PRIVACY.2)"; second layer reads "kept and erased as OPERATION.RECOVERY.2 and TRANSVERSE.PRIVACY.3 set" (X8); form sentence unchanged; Grounds replaced with the REG-250 / L1255 / L1256 text; Certainty "layer grounded (T2, consensus rows L416, L1092); form inferred"; Flags none; Links gain the three pointers.
- R10 (F5) DOCS_SYNC.2: waiver sentence replaced (explicit declaration, granted by the reviewer independent of the author per RULES.4, CI passes on it as on an override assertion per DATA_INTEGRITY.2); grounds sentence on the RULES.3 / DATA_INTEGRITY.2 pattern added; Flags none, also in the DOCS_SYNC roll-up.
- R11 (F1) DATA_INTEGRITY.1: least-powerful-form grounds added; decision and certainty unchanged; Flags none, also in the DATA_INTEGRITY roll-up.
- R12 (F3) SECURITY.2: block/advise sentence replaced by "follows ASSURANCE.RULES.1" with the budget rule, the REG-052 figure (about 10 percent not useful, one organisation) and explicit waiver configuration (REG-170); Certainty now says the threshold is the team's stated budget; Links add RULES.1; Flags none.
- R13 (F4) SECURITY.3: floor list gains "builds and test runs that enable the checks and protections the language, compiler and runtime provide"; grounds cite REG-1086 (NIST IR 8397, 2.5). The 80 percent item stays decided in BEHAVIOUR.6 (R21 confirmed).
- R14 (F7) SECURITY.3: penetration-test trigger (significant change to attack surface) and recorded cycle added; "no source read gives a period (open)"; certainty inferred for the trigger.
- R15 (F6) SECURITY.6: "automated author" becomes "automated actor" in Intent, Decision, and the steering-file sentence; Decision rewritten as lead principle plus (a) automation and (b) data access; no split; Flags none.

Cross-unit lines applied
- X1 SECURITY.3: Rejected now states no coverage figure and points to BEHAVIOUR.6 (no coverage floor, security-relevant code included; conformance minimum only where a baseline requires it); Links point to BEHAVIOUR.6.
- X4 SECURITY.2: see R12; keeps release-time block, who may waive, REG-052.
- X6 SECURITY.6: principle held here (automated actor does not itself execute a job whose guards cannot be applied or whose effects are irreversible; reviewed script; run authorized and triggered by the accountable person or named group, RULES.4, through the pipeline where it reaches the target; terminal run only where no pipeline reaches or supervised ramping is needed, recorded in the same history; the terminal is an example). Pointers to CHANGE_FLOW.DATA_CHANGE.3 and .8 and RULES.4.
- X8 DATA_INTEGRITY.3: see R5; no retention number stated.
- X12 DATA_INTEGRITY.4: Links now "Requires OPERATION.TELEMETRY.8 (Scheduled Work Signals ...)".

Not applied: none. Not for J3: X2, X3, X5, X7, X9, X10, X11, X13, X14.
Nodes added: none.
Flags still open: none. Open in Certainty: SECURITY.3 penetration-test period.
Edits to the record's own history: the "Review applied" last line now says R5, R10 to R15 were applied in the final pass; a "## Final pass applied" section closes judged.md.
Unchanged by design: DATA_INTEGRITY.5 garbled fragment (see L2); header text saying J2/J4 verdicts "not yet written" is stale but not part of the final pass.
Public-repo check: no absolute or home paths in judged.md (grep returned none).
