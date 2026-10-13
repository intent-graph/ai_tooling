# Final pass result (MD-06)

## L1 headline

Every point the reviewers flagged as subtle has a final verdict, and only one goes to the maintainer:
whether an automated reviewer can be the independent check on a change (grounded: each verdict is in
`resolutions.md`; the maintainer question is open).
- flags read: 94 review flags (J1 12, J2 18, J3 7, J4 7, J5 9, J6 9, J7 11, J8 13, J9 8), plus 31 judge flags and notes the reviews had closed, checked
- settled: 77 review flags; 30 of the 31 closed judge flags confirmed
- cross-unit: 16 review flags and the J5 seam note, in 11 new lines X4 to X14 (X7 supersedes X3; J2 R32 is already X2)
- maintainer: 1 point (can an automated reviewer be the independent check, ASSURANCE.RULES.4); 20 lines "settled against your practice"
- decisions changed: 69 records change their decision, constraint or rejected text, plus 2 new nodes (OPERATION.TELEMETRY.7, .8); 12 records change grounds or certainty only
- sources fetched: 6 pages, 5 confirmed the point, 1 held only part of it (no SLSA level on the GitHub how-to page; the concepts page confirmed it)

The judged records can now be built into the IntentGraph once each unit's applier applies its section
of `resolutions.md` and the lines X4 to X14 (inferred: no applier has run yet).

## L2 claims

Pinned:
- flags read: 94 review flags (J1 12, J2 18, J3 7, J4 7, J5 9, J6 9, J7 11, J8 13, J9 8), plus 31 judge flags and notes the reviews had closed, checked
- settled: 77 review flags; 30 of the 31 closed judge flags confirmed
- cross-unit: 16 review flags and the J5 seam note, in 11 new lines X4 to X14 (X7 supersedes X3; J2 R32 is already X2)
- maintainer: 1 point (can an automated reviewer be the independent check, ASSURANCE.RULES.4); 20 lines "settled against your practice"
- decisions changed: 69 records change their decision, constraint or rejected text, plus 2 new nodes (OPERATION.TELEMETRY.7, .8); 12 records change grounds or certainty only
- sources fetched: 6 pages, 5 confirmed the point, 1 held only part of it (no SLSA level on the GitHub how-to page; the concepts page confirmed it)

Claims:
1. **Most flags were settled by giving a weaker practice its condition, not by picking a side**
   (grounded in the rows' own conditions). Examples: updating on need while tests are weak, recorded as
   debt (OWNERSHIP.LIFECYCLE.3); the interface form chosen by who composes the result
   (CONSTRUCTION.BOUNDARY.5); the risky database class decided by a criterion that includes table size,
   instead of a blanket manual rule (CHANGE_FLOW.DATA_CHANGE.3).
2. **Several MUSTs were rewritten as outcomes so they hold whoever does the work** (inferred, MD-02):
   no single credential or person can destroy every backup (dual authorisation or immutable retention);
   a high-blast-radius job is triggered by the accountable person through the guarded path; a deprecated
   item is marked where tools see it.
3. **Eleven cross-unit lines put each shared fact in one place** (grounded in MD-03): block-or-advise in
   RULES.1; production-test guardrails in AVAILABILITY.3; provider-side interface evolution in
   CONTRACTS.1 (supersedes X3); backup retention and erasure split across RECOVERY.2, PRIVACY.2 and
   PRIVACY.3; token acceptance moved to BOUNDARY.2; TELEMETRY.1 split into three nodes.
4. **Two judge "undecided" or "confirm" points were decided on the node's purpose** (inferred): the debt
   inventory lives where the team plans its work, with code markers as pointers; the significance test
   for decision records needs no second bar for large teams.
5. **One question is the maintainer's** (open): whether an automated reviewer in its own context can be
   the independent check, which decides how a team of one meets the review rule. Default if unanswered:
   yes, with a named person accountable and a reviewer of a different kind for high-risk changes.
6. **Twenty decisions go against the maintainer's codified practice and are listed for objection**
   (grounded: each line names the row and the reason); the largest are automatic delivery of ordinary
   database changes, the narrowed "no version numbers", and the narrowed signature-over-view preference.
7. **Five fetched sources closed flags that turned on what a source says** (grounded): SLSA Build L2 is
   one workflow step on a hosted platform (ARTIFACT.1 floor confirmed); NIST IR 8397 adds "built-in
   checks and protections" to the security floor; the C++ initialisation-order hazard makes STATE.5 a
   cross-language principle; OWASP grounds error-detail scoping; the strangler fig article removes "no
   seam exists" as a rewrite condition.

## L3 full

Pinned:
- flags read: 94 review flags (J1 12, J2 18, J3 7, J4 7, J5 9, J6 9, J7 11, J8 13, J9 8), plus 31 judge flags and notes the reviews had closed, checked
- settled: 77 review flags; 30 of the 31 closed judge flags confirmed
- cross-unit: 16 review flags and the J5 seam note, in 11 new lines X4 to X14 (X7 supersedes X3; J2 R32 is already X2)
- maintainer: 1 point (can an automated reviewer be the independent check, ASSURANCE.RULES.4); 20 lines "settled against your practice"
- decisions changed: 69 records change their decision, constraint or rejected text, plus 2 new nodes (OPERATION.TELEMETRY.7, .8); 12 records change grounds or certainty only
- sources fetched: 6 pages, 5 confirmed the point, 1 held only part of it (no SLSA level on the GitHub how-to page; the concepts page confirmed it)

### What was read (grounded)

The rules (`maintainer_decisions.md`, `target_hierarchy.md`), both briefs, `cross_unit_fixes.md`
(X1 to X3), the flag lines of the nine `review/findings.md`, the "Flags raised" and "Review applied"
sections of the nine `judged.md`, every record a flag concerns, and the ledger rows L295, L296, L309,
L353, L416, L417, L1004, L1017, L1092, L1126, L1560 in full. Reviewers' fetched quotes were used as
recorded; where a flag turned on a source no reviewer had read, it was fetched here.

### Verdicts by unit (grounded: `resolutions.md`)

| unit | review flags | settle | cross-unit | maintainer | closed judge flags checked |
|---|---|---|---|---|---|
| J1_ownership | 12 | 11 | 1 (X10) | 0 | 3 |
| J2_assurance_core | 18 | 14 | 3 (X4, X7, X2) | 1 | 2 |
| J3_assurance_integrity | 7 | 6 | 1 (X6) | 0 | 0 |
| J4_assurance_runtime | 7 | 5 | 2 (X5, X13) | 0 | 4 |
| J5_construction | 9 | 9 | 0 (seam note to X7) | 0 | 3 |
| J6_change_flow | 9 | 8 | 1 (X6) | 0 | 8 |
| J7_operation | 11 | 7 | 4 (X8, X11, X11, X12) | 0 | 5 |
| J8_evolution | 13 | 11 | 2 (X7, X8) | 0 | 3 |
| J9_transverse | 8 | 6 | 2 (X8, X9) | 0 | 3 |
| total | 94 | 77 | 16 | 1 | 31 |

### Records whose text changes (grounded: list derived from `resolutions.md`)

- J1 (11): STANCE.1, STANCE.2, SELECTION.2, LIFECYCLE.2, LIFECYCLE.3, CONTAINMENT.1, CONTAINMENT.2,
  SERVICES.1, SERVICES.2 (X7), SERVICES.5, LICENCE.2.
- J2 (11): RULES.1, RULES.4, BEHAVIOUR.1, BEHAVIOUR.2 (X4), BEHAVIOUR.3, BEHAVIOUR.4, BEHAVIOUR.5,
  BEHAVIOUR.7, BEHAVIOUR.8, CONTRACTS.1 (X7), CONTRACTS.2.
- J3 (5): DATA_INTEGRITY.3, DOCS_SYNC.2, SECURITY.2, SECURITY.3, SECURITY.6.
- J4 (5): PERFORMANCE.1 (X11), PERFORMANCE.4, AVAILABILITY.2, AVAILABILITY.3, AVAILABILITY.5.
- J5 (6): DESIGN.1, DESIGN.4, BOUNDARY.2 (X9), BOUNDARY.4, BOUNDARY.5, PARADIGM.2.
- J6 (5): REVIEW.1 (X14), DEPLOY.3, ROLLBACK.3, DATA_CHANGE.3, DATA_CHANGE.8.
- J7 (7, plus new TELEMETRY.7 and .8): ALERTING.2, TELEMETRY.1, TELEMETRY.6, INCIDENTS.1, RECOVERY.2,
  RECOVERY.3, RECOVERY.4.
- J8 (14): DECISIONS.2, INCREMENTAL.2, INCREMENTAL.3, INCREMENTAL.4, INCREMENTAL.6, DEBT.2, DEBT.3,
  DECOMMISSION.1, DECOMMISSION.4, DECOMMISSION.5, DECOMMISSION.6, TECHNOLOGY.1, TECHNOLOGY.2,
  TECHNOLOGY.3.
- J9 (5): SECURITY.1, PRIVACY.2, PRIVACY.3, CONFIG.1, CONFIG.2.
- Grounds or certainty only (12): DATA_INTEGRITY.1, ARTIFACT.1, PERFORMANCE.5, STATE.2, STATE.5,
  BOUNDARY.6, RELEASE.5, RECOVERY.5, CAPACITY.3, SECURITY_MONITORING.1, DOCS.5, ENVIRONMENTS.2.
  Links only: DATA_INTEGRITY.4, RECOVERY.6 (X12), DECOMMISSION.3 (X7).

### Decisions of note, with their certainty

- **Clean-up versus rebuild** (J2 R15, R26): each test establishes its own state; where rebuilding costs
  too much the platform undoes (transaction, snapshot), never hand-written clean-up. Grounded (REG-054;
  REG-1570 read as "the state must be clean", not "clean-up code is better"). The maintainer's rollback
  is that platform undo, so not against practice.
- **Tests in production** (X5): load and locks are transient effects governed by production-test
  guardrails; durable effects fall under BEHAVIOUR.7; test data in production is isolated, marked and
  removed. Inferred (reconciles L265 with L119 and L432).
- **Risky database changes** (X6, J6 FL1, FL2): an authorization stage of the one pipeline, triggered by a
  named qualified group on the exact script; a terminal run only where no pipeline reaches the target or
  supervised ramping is needed; volume enters through the classification criterion. Grounded for the
  pipeline stage (REG-107, REG-245); inferred for the criterion.
- **Provider-side evolution** (X7): three regimes in CONTRACTS.1 (few in-house: coordinate, no versions;
  many or external: library semver or service side-by-side majors with a window; infrastructure-like:
  indefinitely compatible). Grounded for the regimes (L295, L353, REG-030); inferred for the artifact-kind
  split.
- **Backups and erasure** (X8): tiered retention bounded below by detection reach and legal minimum and
  above by privacy periods; erased data in a backup is put beyond use, with an erasure log re-applied on
  any restore, immutable copies included. Grounded for "beyond use" (one regulator, REG-1069); inferred
  for the erasure log.
- **Secrets channel** (J9 T8): mounted files or store API by default; environment variables only where
  nothing else exists or the environment is shown not to leak. Grounded (REG-166, fetched in review).
- **Rewrites** (J8 R17): "no seam exists" removed as a condition; seams are inserted (REG-033, fetched
  here). Grounded.
- **SLSA L2 floor** (J4 flag-4): kept; one workflow step on a hosted platform (GitHub docs, fetched
  here). Grounded for one platform, inferred in general.
- **Penetration-test frequency** (J3 R14): triggered by significant change plus a recorded cycle; no
  period in any source. Open for the number.

### The maintainer point (open)

Whether an automated reviewer in its own context can be the independent check on a change
(ASSURANCE.RULES.4). Options, costs, recommendation and default are in `maintainer_points.md`, point 1.
Default applied if unanswered: yes, a named person stays accountable and approves, and for high-risk
changes the reviewer is of a different kind from the author (inferred; no source addresses a team of
one).

### Sources fetched in this pass (grounded)

| source | result |
|---|---|
| GitHub docs, artifact attestations concepts page | confirmed: "Artifact attestations by itself provides SLSA v1.0 Build Level 2." |
| GitHub docs, using artifact attestations how-to page | setup confirmed; no SLSA level stated (partial) |
| NIST IR 8397 (REG-1086) | confirmed: built-in checks and protections (2.5); at least 80 % coverage (2.7) |
| isocpp FAQ, static initialization order | confirmed: the hazard in C++ |
| OWASP Error Handling Cheat Sheet | confirmed: details logged server side, not returned to the user |
| Fowler, Strangler Fig Application (REG-033) | confirmed: seams are inserted into the system |

### Limits (open)

- No applier has run: the changes exist as text in `resolutions.md` and lines X4 to X14 only.
- X3 is marked settled in `cross_unit_fixes.md` and could not be edited (append only); X7 states that it
  supersedes X3.
- The ASSURANCE L1 re-roll (X2) and the wave-3 roll-ups of the realization branches are outside this pass.
