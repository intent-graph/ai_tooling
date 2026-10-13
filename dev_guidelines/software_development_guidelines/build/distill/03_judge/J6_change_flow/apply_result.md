# J6_change_flow: final pass applied

## L1 headline

J6_change_flow is final: 9 resolutions (FL1 to FL9) and 2 cross-unit lines (X6, X14) applied, plus the eight confirmed judge flags settled; no node added, none not applied, no flag still open (grounded).

## L2 claims

- Resolutions applied: FL1, FL2, FL3, FL4, FL5, FL6, FL7, FL8, FL9, all nine (grounded: each checked against the record text). Resolutions not applied: none.
- Cross-unit lines applied: X6 (DATA_CHANGE.3 holds the procedure and points to ASSURANCE.SECURITY.6; DATA_CHANGE.8 points to both) and X14 (REVIEW.1 Rejected P3 points to RULES.4) (grounded). Cross-unit lines not applied: none; X1 to X5 and X7 to X13 do not name J6 (grounded).
- Nodes added: none (grounded). Maintainer point on RULES.4: J2 only, not applicable.
- Flags still open: none; F1 to F13 settled and every Flags line reads none (grounded).
- Substantive changes: DATA_CHANGE.3 risky class becomes an authorization stage of the one pipeline, with a size and measured-duration criterion replacing the large-volume rule; ROLLBACK.3 written reverse only when faster than a restore and rehearsed; DEPLOY.3 "schema" narrowed to production-only external or shared schemas; DATA_CHANGE.8 ticket-key MUST becomes identifiability and the ramp a recommendation; RELEASE.5 certainty reworded (grounded).
- Consequential edits not named in the resolutions (inferred necessary to avoid contradiction, not re-judging): DATA_CHANGE.3 Rejected P3, Grounds (L290 b) and Certainty reworded around the size criterion; DATA_CHANGE.3 Grounds clause "and is inferred" trimmed because REG-107 and REG-245 now ground the stage (inferred).

## L3 full

Applied to `judged.md` (a `## Final pass applied` section lists each line):

- FL1 (DATA_CHANGE.3, cross-unit X6): Decision sentence replaced by the stated authorization-stage wording, with a pointer to ASSURANCE.SECURITY.6. Grounds add REG-107 and REG-245. Certainty: the stage is grounded; the named qualified group is inferred. Applied.
- FL2 (DATA_CHANGE.3): large-volume sentence deleted; criterion extended ("is irreversible, touches a table above a size the team records, or has not had its duration measured on production-shaped data (DATA_CHANGE.7)"); Context replaced as stated. Applied; consequential edits in Rejected P3, Grounds and Certainty (see L2).
- FL3 (DEPLOY.3): "schema" replaced by "external or shared schemas present only in production". Applied.
- FL4 (ROLLBACK.3): reversible-form clause replaced; "P2 without the prepared undo" line deleted; rejection of a written reverse for every change added (REG-244, REG-251, best for packaged software with many installed versions); faster-than-restore condition marked inferred. Applied.
- FL5 (F1): closed by FL2; flag removed. Applied.
- FL6 (F4, DEPLOY.3): unchanged; flag removed. Applied.
- FL7 (F11, BUILD.1): unchanged; flag removed. Applied.
- FL8 (F12, RELEASE.5): decision unchanged; Certainty set to "inferred: one T3 source (REG-115), plus the argument that a change needs someone able to respond to its failure", with the MUST kept. Applied.
- FL9 (F13, DATA_CHANGE.8): convergence-query MUST kept; ticket-key MUST replaced by "MUST a long-running statement be identifiable to its change in activity views and logs (for example the ticket key in a comment)"; ramp steps recommended, "concurrency raised only with a reason and a metric" kept as MUST; checklist wording aligned. Applied.
- Confirmed judge flags F2, F3, F5, F6, F7, F8, F9, F10: records unchanged, flags removed. Applied. Open flags kept: none (an earlier note in F6, "pull versus push is open", stays in DEPLOY.4 Context, which is not a flag).
- X6: DATA_CHANGE.3 procedure in place; DATA_CHANGE.8 gets a sentence and Links entry pointing to DATA_CHANGE.3 and ASSURANCE.SECURITY.6. Applied.
- X14: REVIEW.1 Rejected P3 now cites RULES.4 and its reason. Applied.
- Not applied: none. Nodes added: none. Flags still open: none. The header "Flags raised" line and the closing flags section now say all settled.
- Note for readers: ASSURANCE.RULES.4 must carry the X14 reason text (J2's record); this unit only points to it (open until J2's applier writes it, inferred).
