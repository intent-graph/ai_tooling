# J8_evolution review: result

## L1 headline

J8_evolution is sound in its decisions: the five L2 branches hold up against the fetched sources and no decision needed reversing; what is wrong is mostly seams (contradictions with decided J1, J2 and J6 nodes, restated facts, missing conditions), which are fixable (grounded). Thirteen are clear fixes for the judge; thirteen subtle points go to the Opus pass (grounded for the fixes; the flags are open by nature). The one-version rule that TECHNOLOGY.3 relies on is decided in J6 CHANGE_FLOW.INTEGRATION.1, not in J1; TECHNOLOGY.3 should point there (grounded).

Pin:
- Records reviewed: 33 (27 L3, 5 L2, 1 L1) of unit J8_evolution.
- Findings fix: 13 (R01 to R13).
- Findings flag: 13 (R14 to R26).
- Sources fetched and confirmed: 13 fetched, 12 confirmed, 1 partly confirmed (REG-1012: triggers and storage confirmed, no "hard to reverse" and no skip list).

## L2 claims

Pin:
- Records reviewed: 33 (27 L3, 5 L2, 1 L1) of unit J8_evolution.
- Findings fix: 13 (R01 to R13).
- Findings flag: 13 (R14 to R26).
- Sources fetched and confirmed: 13 fetched, 12 confirmed, 1 partly confirmed (REG-1012: triggers and storage confirmed, no "hard to reverse" and no skip list).

Claims (details in `findings.md`):

- Grounding holds (grounded): the cited sources say what the records claim for the checked rows: Knight Capital order (loss, absence of controls against activating retired code), the deprecation chapter (liability, advisory vs compulsory, owners), the large-scale-change chapter, Kubernetes windows, the Sunset and Deprecation header rule, Fowler on debt, refactoring, the quadrant and YAGNI, the Nygard and AWS record practices. One ungrounded element: "hard to reverse" in DECISIONS.2 (R01).
- Contradictions with decided nodes (grounded): DEBT.5 constraint against DEBT.1, DECOMMISSION.1 and LIFECYCLE.3 (R09); DEBT.2 dangling reference to DEBT.3 (R07); TECHNOLOGY.3 relies on a rule J1 does not decide (R12); INCREMENTAL.1 and .2 give different conditions for the same alternative (R03); DECISIONS.2 constraint against its own decision (R01); DECISIONS.6 variant against its rejection (R02).
- Duplication, MD-03 (grounded): migration-as-debt three times (R04), characterization tests (R08), reliance tests (R06), the minor-release rule (R11); an owner-of-removal fact on five nodes is contestable (R18, flag).
- Missing condition, check 4 (grounded): INCREMENTAL.3 rejection of the big-bang rewrite (R05).
- Judge flags: F2 settled by J6 REVIEW.2, which decides refactoring in separate changes (R10, grounded); F7 closed, F4 closed; F1, F3, F5, F6 carried (R21, R23, R16, R17); F8 split: home found (R12), residual regime question carried (R26).
- Subtle points for the Opus pass (open): default significance bar is an intersection of two sources' bars (R14); name marker for deprecated items versus rename being breaking (R15); "repay promptly" against DEBT.5 and the quadrant source (R19); survey primacy resting on a secondary summary (R20); the SERVICES.2 date-pinned alternative and link type on DECOMMISSION.3 to .5 (R22); TECHNOLOGY.1 context against TECHNOLOGY.3 polyglot (R24); three registers (R25); TECHNOLOGY.3 mandate and paved path collapse (R26).
- Checks with no finding (grounded): missed positions (3) and author rules (5); X3 respected; X1 and X2 do not touch J8.

## L3 full

Pin:
- Records reviewed: 33 (27 L3, 5 L2, 1 L1) of unit J8_evolution.
- Findings fix: 13 (R01 to R13).
- Findings flag: 13 (R14 to R26).
- Sources fetched and confirmed: 13 fetched, 12 confirmed, 1 partly confirmed (REG-1012: triggers and storage confirmed, no "hard to reverse" and no skip list).

Method (grounded): read the brief, the maintainer decisions and target hierarchy, the whole judged.md of J8, the EVOLUTION skeleton records, the ledger rows cited for the nodes with findings, the J1, J2 and J6 records J8 realizes or touches, and cross_unit_fixes.md; fetched 13 cited sources and checked the quoted claims. Every line of findings.md carries node, check number, severity, defect, correction and evidence.

Findings by node (full lines in `findings.md`):

- DECISIONS: DECISIONS.2 R01 (fix), R14 (flag); DECISIONS.6 R02 (fix). DECISIONS.1, .3, .4, .5: no finding; grounds confirmed against REG-154 and REG-1011 (grounded). The accepted-record correction exception in DECISIONS.4 (a typo or broken link may edit a record) is stated by no fetched source and is marked inferred in the judge's record only for the document-type split; left as is (inferred).
- INCREMENTAL: .1 R03; .2 R04; .3 R05, R17; .5 R06; .6 R15, R16; .4 only R18 (owner fact shared with four other nodes). Checks on grounding for .1, .4 confirmed (REG-034 one third; REG-1003 sharding, blocking the old pattern, infrastructure ownership).
- DEBT: .2 R07, R19; .3 R20, R21; .4 R08; .5 R09, R10; .1 only R04. Grounding for interest-only-where-changed and weeks-not-months confirmed (REG-1001); opportunistic refactoring and "a day or two" confirmed (REG-1008); prudent vs reckless confirmed (REG-1130).
- DECOMMISSION: .4 R11, R22; .6 R23; .1 and .5 share R18; .1 grounding confirmed (REG-1017, REG-1002); .3 sunset not earlier than deprecation confirmed (RFC 9745); .2 no finding.
- TECHNOLOGY: .1 R24; .2 R25; .3 R12 (fix), R26 (flag); .4 R13.
- L1 and the four other L2 records: roll-ups state no fact of their own; no finding.

One-version rule (the question asked): J1 LIFECYCLE.2 does not state it, as the judge says (grounded: no hit in J1 or J2). It is decided in J6 CHANGE_FLOW.INTEGRATION.1 ("one version of each shared component at any time", from L132, REG-106). The source applies it to components an organisation shares, in a monorepo or not. J1 LIFECYCLE.2 (libraries declare ranges; diamond conflicts resolved by moving or patching) does not contradict it for third-party resolution, but TECHNOLOGY.3 should not use it to reject a polyglot variant (R12); the J6 record is also in a not-yet-reviewed unit, so the pointer should be rechecked after J6's review (inferred).

Judge flags: F1 R21 (open, genuine trade-off, recommendation sound); F2 R10 (settled); F3 R23 (open, cross-unit to J9); F4 closed (inferred, labelled); F5 R16 (open, maintainer); F6 R17 (open); F7 closed (REG-008 figures confirmed as one project's; not adopted); F8 R12 plus R26.

Consistency with cross_unit_fixes.md (grounded): X3 respected; the link type "realizes SERVICES.2" on the provider-side retirement nodes is a flag (R22). X1 and X2 are outside J8.

Limits (open): three fetched pages were read through a summarising fetcher, so quotes are as returned; the Knight order was read from the PDF text directly. REG-1007 (Design Stamina Hypothesis), REG-1004, REG-105, REG-1022 and REG-1015 were not fetched.
