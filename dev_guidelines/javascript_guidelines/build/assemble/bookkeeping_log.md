# Build bookkeeping moved out of the engineer-facing fields (stage 7)

Constraints and design notes of the graphs hold rules, their reasons and the evidence only. What the build did to reach them
is recorded here and in the ledger and skeleton.

- SUBSET-051 (PIG-JS.SUBSET.OBJECTS.6): removed from the rule text: Merged at integration (P5, overlap O15): LANG-C55 and RUNSEC-C07 state one rule.
- CONTROL-078 (PIG-JS.CONTROL.PROCESS.2): removed from the rule text: Merged at integration (P5, overlap O02): ASYNC-C05 and RUNTIME-C37 state one principle, which CONTROL.
- DEFENSE-023 (DEFENSE.HOST.1): removed from the rule text: Merged: one fact stated twice.
- DEFENSE-026 (PIG-JS.DEFENSE.INJECTION): removed from the rule text: Merged: one requirement stated twice.
- DEFENSE-041 (PIG-JS.DEFENSE.DOM.4): removed from the rule text: Merged: one decision stated twice, header deployment half belongs to web_architecture.
- DEFENSE-083 (PIG-JS.DEFENSE.INJECTION.3): removed from the rule text: Merged: two driver renderings of one rule, library facts only, no preference between drivers.
- DEFENSE-086 (PIG-JS.DEFENSE.INJECTION.3): removed from the rule text: Merged: both state the same operator-injection control.
- DEFENSE-100 (PIG-JS.DEFENSE.SECRETS.1): removed from the rule text: Merged: one rule for Node and browser.
- DEFENSE-125 (PIG-JS.DEFENSE.HOST.2): removed from the rule text: Merged: two statements of one exposure.
- DEFENSE-129 (PIG-JS.DEFENSE.HOST.4): removed from the rule text: Merged: TYPES-C32 states the same rule.
- DEFENSE-140 (PIG-JS.DEFENSE.DOM.6.1): removed from the rule text: Merged: FW-C02 holds the per-framework list of the same fact.
- DEFENSE-152 (PIG-JS.DEFENSE.INJECTION.1.1): removed from the rule text: Merged: the browser sink list and the timer detail of the same rule.
- DEFENSE-168 (PIG-JS.DEFENSE.INJECTION.4.3): removed from the rule text: Merged: one Node doc caveat stated twice.
- DEPENDENCIES-037 (PIG-JS.DEPENDENCIES.UPDATE.1): removed from the rule text: Claim SUPPLY-C12 is labelled consensus; its effect rests on one T1 assertion and is relabelled single-source (12_dissent X5).
- Integration notes of the skeleton (lines starting 'Integration note') no longer reach design_notes; they stay in build/distill/skeleton.md. build_batches.py skips them.
- The 'Rows:' line (ledger row ids with role and agreement) and the row ids inside 'Rejected', 'Fact' and 'Deferred' lines no longer reach design_notes; the ledger is the record.
- Quote wording corrected in the claim tables (F18): RUNSEC-C37 (about half a minute), RUNSEC-C35 (the $ statement is inferred, not on the cited page), SRVSEC-C27 (full operator sentence), SRVSEC-C07 (SRC-078 carries the principle only). QUALITY-C35 states 14 of 19. The SRC-341 URL note (one chapter URL for five chapters) is left as is in the source register.
- Design notes: row ids in brackets and '(see ROW)' references, gap ids (G-L20, G-M02), 'Merged: ...' sentences and the label 12_dissent are scrubbed by build_batches.py::scrub_notes when the graph is built (ledger and skeleton keep them). Judge record of FRAMEWORK_SHORTLIST: 'slot 10' wording replaced.
- Rules written as expectations ('Expect', 'Know') rewritten as verb-first rules: CONTRACTS-027, STRUCTURE-002, DEFENSE-067, VERIFICATION-016.
- Slot 14 review fixes (F01 to F17): DEFENSE-180 merged into DEFENSE-182 and DEFENSE-181 moved to PIG-JS.DEFENSE.INJECTION.6.4 (one owner for the redirect rule); DEFENSE-139 became a rejected row; DEFENSE-252 became a fact row; facts, CVE notes and version ranges moved out of constraints into the claim-less fact rows DEFENSE-270 to DEFENSE-277; DEFENSE-269 holds the new claim SECGAP2-C92; SECGAP2-C91 sits on DEFENSE-182. Claims SECGAP2-C56, C68, C69 and C88 corrected in the claim table.
