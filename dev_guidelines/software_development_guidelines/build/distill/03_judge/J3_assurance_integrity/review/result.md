# Review result: unit J3_assurance_integrity

## L1 headline

Pin: records reviewed 19; findings fix 8 (R1, R2, R3, R4, R6, R7, R8, R9); findings flag 7 (R5, R10, R11, R12, R13, R14, R15); sources fetched 4, confirmed 3 (1 partial).

The unit is sound in structure: no missed positions, no author rule beyond the SECURITY.6 wording, no averaging beyond the DOCS_SYNC.2 gate-plus-waiver synthesis. The clear defects are grounding slips (one misused row, L239) and unsupported context conditions; the one contradiction is in SECURITY.3 (regular penetration testing). The most important flag: F2's premise is false, since the T2 source REG-250 already states the case for soft deletion. (grounded)

## L2 claims

Pin: records reviewed 19; findings fix 8 (R1, R2, R3, R4, R6, R7, R8, R9); findings flag 7 (R5, R10, R11, R12, R13, R14, R15); sources fetched 4, confirmed 3 (1 partial).

- Grounding: R1 L239 is a follow-up for a missing review, not a documentation waiver; R3 and R6 misstate ledger certainty. (grounded, source and ledger read)
- Context creep: R4 non-relational stores, R7 owner, R8 view or default scope have no row. (grounded, ledger read)
- Consistency: R9 SECURITY.3 decision vs its own rejection of regular penetration tests for all; R2 outcome overclaims in DOCS_SYNC. (grounded)
- Flags for Opus: R5 deletion form (judge's "not read at T2" is wrong); R10 gate with waiver and no waiver authority; R15 author wording of SECURITY.6; R11, R12, R13, R14 judge flags F1, F3, F4, F7 carried as they are. (R5, R10 grounded; R11 open, REG-1143 not fetched; R15 inferred)
- F4 reconciled with J2 BEHAVIOUR.6 by exclusion. (grounded)
- Missed positions: none; rejected-without-condition: none beyond stated "best never". (grounded)

## L3 full

Pin: records reviewed 19 (3 L2 roll-ups, 16 L3); findings fix 8 (R1, R2, R3, R4, R6, R7, R8, R9); findings flag 7 (R5, R10, R11, R12, R13, R14, R15); sources fetched 4, confirmed 3 (1 partial).

Sources fetched: REG-153 GitLab documentation workflow (T2): partial, confirms follow-up issue and non-blocking writer review, refutes the L239-as-waiver use (R1). REG-1145 Brandur (T3): confirmed (four costs; deleted_record archive with jsonb copy in one transaction). REG-250 Google SRE data integrity (T2): confirmed for layers and tested recovery, and it states soft deletion as primary defense, contradicting the F2 premise (R5). REG-170 GitHub push protection (T1): confirmed (three bypass reasons, two close, one stays open; logged; default write access may bypass).

Judge flags assessed: F1 carried (R11). F2 carried with new evidence (R5). F3 carried (R12). F4 settled as consistent with J2, carried low (R13). F5 carried with the waiver-authority gap (R10). F6 carried with rewording proposal (R15). F7 carried, dissolves once R9 is applied (R14).

Details, evidence and proposed corrections per finding: `findings.md` in this folder. Not checked: REG-1143, REG-1139, REG-1086, REG-1092, REG-1094 contents; REG-181 is not citable. (open)
