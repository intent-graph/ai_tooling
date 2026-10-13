# Result: review of unit J9_transverse

## L1 headline

Pin: records reviewed 36 (TRANSVERSE, 6 L2 roll-ups, 29 L3); findings fix 10 (F01 to F10); findings flag 8 (T1, T5, T6, T7, T8, F11, F12, F13); sources fetched 6, confirmed 4 (2 in part).
The unit is sound in shape: no averaging found, no author rule, consistent with the J3 records and with `cross_unit_fixes.md` (grounded). The clear defects are small: a wrong pointer (SECURITY.2 to SECURITY.7), a misread position (SECURITY.6 P2), a grounding claimed as "not read" that a source states (DOCS.4), a number overstated (CONFIG.4, 90 days), and restated content that belongs in J3 (PRIVACY.3, SM.3, DOCS.1) (grounded). The Opus pass has the maintainer-row override (T1), the channel default and the "best never" on packaged config (T8), the token clause (T7), and four smaller points (inferred). Judge flags T2, T3, T4 are settled.

## L2 claims

Pin: records reviewed 36; findings fix 10; findings flag 8; sources fetched 6, confirmed 4 (2 in part).

Fix (the judge can apply; all grounded unless stated)
- F01 SECURITY.2: outcome measures are pointed at ASSURANCE.SECURITY.7, which holds none; time to detect is in SECURITY_MONITORING.4 (grounded).
- F02 SECURITY.6: "policy only" (L1142) means no bounty, not no response times; P1 and P2 are not rivals, and the rejection of P2 is a misreading (grounded: OMB says a bounty is "not required", to be weighed).
- F03 DOCS.3: Grounds say the header keeps dated verification; the Decision does not and the J3 rule is for documents (grounded).
- F04 DOCS.4: the reason against commit-generated changelogs is stated by REG-162, not only inferred (grounded: "full of noise").
- F05 SECURITY_MONITORING.3 and F06 PRIVACY.3 and F08 DOCS.1: content restated that is held elsewhere (pseudonymisation in PRIVACY.1; deletion form in ASSURANCE.DATA_INTEGRITY.3; read-only generated docs in DOCS_SYNC.3) (grounded).
- F07 CONFIG.4: the 90-day figure is one source's "queryable 90 days, longer in cold storage" for secret-usage logs; PRIVACY.2 says no source gives a period (grounded).
- F09 PRIVACY.3: "and in what time" has no row; F10 ENVIRONMENTS.1: a "not decided here" position no row carries (grounded).

Flag (Opus pass)
- T1 DOCS.3: the maintainer's mandatory header change log is rejected except where history is invisible; reasoned from the row's own condition, still an override of a maintainer row (inferred).
- T5 MONITORING.1: logging regardless of ASVS level rests on an inferred link; the ASVS-level premise was not in the fetched source (inferred; open for the premise).
- T6 PRIVACY.3: UK regulator confirms backups beyond use; locked backups and non-UK contexts stay open (open).
- T7 CONFIG.1: token clause is a constraint without a decision, relocation target not yet judged (inferred).
- T8 CONFIG.2: OWASP says env vars "not recommended unless other methods are not possible", which may invert the default; "best never" for packaged config overreaches L1193 (inferred).
- F11 DOCS.5, F12 ENVIRONMENTS.2, F13 SECURITY.1: small extensions beyond the row (inferred).

Settled judge flags: T2 (after F04), T3, T4 (grounded).

## L3 full

Pin: records reviewed 36; findings fix 10; findings flag 8; sources fetched 6, confirmed 4 (2 in part).

Method. Read the brief, `maintainer_decisions.md`, `target_hierarchy.md`, the 36 records of `judged.md`, the skeleton records of branch TRANSVERSE, the ledger rows cited, the J3 records the unit realizes (ASSURANCE.DOCS_SYNC.1-.4, SECURITY.1, .2, .5, .6, .7, DATA_INTEGRITY.1, .3) and `cross_unit_fixes.md` (X1 to X3, none touches J9). J7 backup records were read for the PRIVACY.3 tension.

Per-check result (grounded unless marked)
1. Averaging: none found. DOCS.1 levels and CONFIG.3, CONFIG.5, ENVIRONMENTS.2 each choose by a condition a row states. One reconciliation is the judge's (CONFIG.2, T8, inferred). SECURITY.6 mixes up two non-rival positions (F02).
2. Grounding: six sources fetched. Confirmed as cited: RFC 9116 (Contact and Expires must be present, file under the well-known path); Keep a Changelog 1.1.0 (commit logs are noise, Unreleased section, grouping by type); OMB M-20-32 (bounty "not required", weigh cost, competence, maturity; the 14 and 60 day counts belong to OpenSSF and were not in this memo); ICO erasure guidance (backups beyond use, tell the individual). Confirmed in part: OWASP Secrets Management (leak sequence revoke, rotate, delete matches CONFIG.6; env var caution is stronger than the record says; the 90-day figure has a narrower scope, F07); OWASP Logging (events, time sync, separate partition match; the ASVS-level note and "security control failures and bypass attempts" are not in it). Sources not fetched: REG-1078, 1079, 1090, 1093, 1095, 166 secondary quotes, REG-004, REG-168, REG-178, REG-167.
3. Missed positions: none; seven skeleton row ids absent from the record are link pointers only. F02 is an invented position, not a missed one.
4. Rejected without condition: "best never" is used throughout. Accepted where the reason is general (hardcoded secrets, shared credentials). Contestable for packaged config (T8) and for one log for both purposes (inferred, L1252: no source states it).
5. Author rules: none. DOCS.1 P5 is restated as an outcome.
6. Context creep: F09, F10; smaller: F11, F12.
7. Consistency: F01, F03, F06, F07. J3 pointers otherwise hold: DOCS_SYNC.4 carries the changelog-present chore; SECURITY.5 and CONFIG.6 agree on rotation; automation limits are stated once (SECURITY.6); atomic audit is in DATA_INTEGRITY.1 and SM.5 points to it.
8. Duplication: F05, F06, F08.

Judge flags, one by one
- T1 carried (flag): see findings.md.
- T2 settled with F04. T3 settled: the open point does not change the decision. T4 settled: the decision does not depend on bounty yield.
- T5 carried: premise unconfirmed in the fetched source; verify against ASVS (REG-1079) at the Opus pass, and weigh against J3 SECURITY.1 (depth by risk).
- T6 carried: ICO narrows the open point.
- T7 carried: J5 not judged, so the relocation cannot be checked.
- T8 carried with the two added points.

Open for the Opus pass: T1, T5, T6, T7, T8, F11, F12, F13. Applying F01 to F10 changes no decision, only wording, pointers and grounds.

Detail per finding with evidence quotes: `findings.md` in this folder.
