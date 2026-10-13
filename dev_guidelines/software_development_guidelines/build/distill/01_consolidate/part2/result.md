# Consolidation part 2: round-3 research and the generic evidence of the web guideline added to the ledger

## L1 headline

The four round-3 research results (evolution, change authors, recovery, security depth: 162 claims) and the generic evidence of the web architecture guideline (174 claims in scope, 144 imported, 30 skipped as web-specific) are added to the claims ledger as a separate part 2 of 289 rows (L1001 to L1289) and 160 new sources, so that the skeleton step can attach every row next to the 460 rows of part 1; no claim is dropped, none is unplaced, part 1 is untouched and receives 382 see-also pointers. Certainty: grounded for the counts and the id coverage (a script reads the results and proves them), inferred for the 16 merges, the stack-neutral restatements, the skip decisions and the see-also readings (my reading, not a check of equality).

Pinned:
- Claims in: 162 original claims from 4 round-3 results (EVOL 41, AUTH 36, RECOV 41, SECD 44); web guideline: 174 claims in scope (OPS 53, ARCH 45, SEC-C50 to SEC-C58 9, THIN 40, DCON 27).
- Rows out: 289 ledger rows (L1001 to L1289; by earliest origin: EVOL 41, AUTH 36, RECOV 41, SECD 44, WEB:OPS 43, WEB:ARCH 32, WEB:SEC 7, WEB:THIN 23, WEB:DCON 22), of which 16 merged rows merge 33 originals; 273 rows hold one original each.
- See-also links to part 1: 382 links to 195 distinct part-1 rows (32 state the same normative thing as a part-1 row, 345 related, 5 possible tension); 200 links between part-2 rows. Part 1 is unchanged.
- Web claims: imported 144 (OPS 45, ARCH 40, SEC 8, THIN 28, DCON 23), of which 33 restated stack-neutral; skipped 30 as web-specific (OPS 8, ARCH 5, SEC 1, THIN 12, DCON 4); SEC-C01 to SEC-C49, SEC-C59, SEC-C60 (51 claims) outside the restriction, not examined.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id of the four slots and every imported web claim id appears exactly once, none dropped, every in-scope web claim imported or skipped, every cited source resolves in part 1 or part 2`
- Sources: 118 source ids of the 4 round-3 results plus 98 web source ids cited by imported claims, replaced by 160 new rows (REG-1001 to REG-1160; T1 70, T2 46, T3 38, T4 6) and 49 ids mapped to existing part-1 rows (including AUTH-S21, mapped to the maintainer source REG-181, not citable, no tier).

## L2 claims

Pinned:
- Claims in: 162 original claims from 4 round-3 results (EVOL 41, AUTH 36, RECOV 41, SECD 44); web guideline: 174 claims in scope (OPS 53, ARCH 45, SEC-C50 to SEC-C58 9, THIN 40, DCON 27).
- Rows out: 289 ledger rows (L1001 to L1289; by earliest origin: EVOL 41, AUTH 36, RECOV 41, SECD 44, WEB:OPS 43, WEB:ARCH 32, WEB:SEC 7, WEB:THIN 23, WEB:DCON 22), of which 16 merged rows merge 33 originals; 273 rows hold one original each.
- See-also links to part 1: 382 links to 195 distinct part-1 rows (32 state the same normative thing as a part-1 row, 345 related, 5 possible tension); 200 links between part-2 rows. Part 1 is unchanged.
- Web claims: imported 144 (OPS 45, ARCH 40, SEC 8, THIN 28, DCON 23), of which 33 restated stack-neutral; skipped 30 as web-specific (OPS 8, ARCH 5, SEC 1, THIN 12, DCON 4); SEC-C01 to SEC-C49, SEC-C59, SEC-C60 (51 claims) outside the restriction, not examined.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id of the four slots and every imported web claim id appears exactly once, none dropped, every in-scope web claim imported or skipped, every cited source resolves in part 1 or part 2`
- Sources: 118 source ids of the 4 round-3 results plus 98 web source ids cited by imported claims, replaced by 160 new rows (REG-1001 to REG-1160; T1 70, T2 46, T3 38, T4 6) and 49 ids mapped to existing part-1 rows (including AUTH-S21, mapped to the maintainer source REG-181, not citable, no tier).

Each line carries its certainty: grounded (I can name the file or the script run that makes it true), inferred (my reading), open (not determined).

### Claims of this consolidation

- Every original claim id of the four round-3 results (162) appears in exactly one ledger row of part 2, alone or inside a merged row; none is dropped, none sits in a row without its origin area. Every in-scope web claim (174) is either imported once or listed once in the skipped table. Part 1 is read-only and untouched. (grounded (script run, output in L3))
- Rows: 289 = 162 round-3 claims + 144 imported web claims - 17 (the 16 merged rows merge 33 originals: 1 row of three, 15 rows of two). Rows are ordered by origin area (EVOL, AUTH, RECOV, SECD, then the web areas OPS, ARCH, SEC, THIN, DCON) and carry no hierarchy, no owner, no judgement. (grounded)
- Merge criterion: the origins state the same normative thing, one possibly with an extra clause that does not conflict; every position and source of both origins is kept, labelled by origin id. All 16 merges involve a web claim: they are mostly the overlaps between the web guideline and the round-3 slots (decision records, log content and protection, expand-migrate-contract, incremental replacement) and between web slots (twelve-factor config, backing services, dev/prod parity, schema migration). The 16 are listed with origins in L3; near pairs are kept apart and cross-linked. (grounded for the list, inferred for each merge decision (a judgement call; the near pairs are kept apart so it can be reversed))
- A new claim is never merged into a part-1 row: it carries `see also Lnnn`. 382 links reach 195 of the 460 part-1 rows; 32 are marked as stating the same normative thing as the part-1 row (the clearest overlaps, for example W3C trace propagation, the four golden signals, the build-release-run split, the unbuffered log stream, the backup that must restore, the blocking-or-advising decision on security findings), 345 as related, 5 as possible tension (soft deletion costs, THIN-C21 and THIN-C22, against the part-1 rule to use soft deletion first, L416; opportunistic refactoring, EVOL-C26, against refactoring in separate changes, L140; do not build ahead, ARCH-C03, against designing for probable future use, L330; application-first domain logic, THIN-C27, against integrity enforced at the write path, L279). (grounded for the counts, inferred for each relation (found by a lexical scan of all 306 claims plus a hand read of the 460 part-1 statements; not a check of equality, and recall is not guaranteed))
- Web claims were imported only when they hold for any stack: 111 imported unchanged (origin stack neutral), 33 restated stack-neutral (28 whose origin stack was http, js, python or postgres, 5 neutral claims whose wording named the web or a tool). The restated row shows the origin stack in its stack column and keeps the origin wording in `positions`, so the restatement can be reversed. (grounded for the counts, inferred that each restated principle holds for any stack)
- 30 web claims were skipped as specific to the web, a framework, an engine or a tool (browser telemetry and vitals, HTTP caching headers, redirect after POST, the REST constraints, engine-version features, JSON-schema and library mechanics). Each is listed with its origin stack and reason at the end of `claims_ledger_part2.md` and stays readable in the web results; the skeleton step may re-import any of them. (grounded for the list, inferred that each is web-specific (my call at the boundary: for example the REST statelessness constraint is skipped because the generic form is OPS-C46))
- From the web identity and security result only the secrets and supply-chain claims (SEC-C50 to SEC-C58) were taken, as the inputs note restricts; SEC-C01 to SEC-C49, SEC-C59 and SEC-C60 (51 claims) were not examined. (grounded)
- Slot 13 counted three maintainer claims (MAINT-C62, MAINT-C63, DELIVER-C49) as an internal source AUTH-S21: it is mapped to the existing maintainer source REG-181 (not citable, no tier), appears in the sources of the five AUTH rows that cite it, and every such row says so. (grounded)
- Sources: 160 new rows replace the round-3 source ids and the cited web source ids that part 1 does not hold (same normalised URL means the same source, tier is the highest origin tier); 49 original ids resolve to a row of part 1, found by identical normalised URL plus two pairs the URL test misses (the Kubernetes deprecation policy under its redirected path, NIST SP 800-61 Rev. 3 as PDF and landing page) and AUTH-S21. Part-1 tiers are kept where an origin tier is higher (2 cases, noted in `sources_part2.md`). (grounded for the counts, inferred for the two manual pairs)
- Agreement as recorded by the origins over 289 rows: consensus 201, majority 54, contested 33, open 1. Certainty as recorded (first word): grounded 254, inferred 26, not stated 5, open 3, other 1. Level: practice 120, principle 98, decision 71. Five RECOV claims record no certainty field (RECOV-C11, C24, C25, C29, C30): the ledger says `not stated by origin (sources cited)` rather than assigning one. (grounded (counted from the ledger))
- Source ids inside the claim texts were rewritten from slot-local tags (S05) to register ids; local claim references (for example C33) were rewritten to the full origin id; references to the web ledger inside web claim texts are written WLnnn so they cannot be mistaken for ledger rows; the claim wording is otherwise untouched. (grounded)

### Not done

- The origin claims were not re-checked against their sources; certainty is as recorded by each slot (grounded in the origin, not by me). (open)
- No structure, grouping, owner, judgement of which position wins, or deletion of any claim; this is the skeleton step. (grounded: by construction)
- See-also coverage is not exhaustive: part-1 rows not linked from a part-2 row may still be related; the relation words (same, related, possible tension) are my reading. (open for recall, inferred for each reading)
- Web sources are registered only when an imported claim cites them; sources of skipped web claims are not in the register. (grounded)
- No new research, no web claim outside the five named results, no edit of part 1, the web guideline or the maintainer files. (grounded)

## L3 full

Pinned:
- Claims in: 162 original claims from 4 round-3 results (EVOL 41, AUTH 36, RECOV 41, SECD 44); web guideline: 174 claims in scope (OPS 53, ARCH 45, SEC-C50 to SEC-C58 9, THIN 40, DCON 27).
- Rows out: 289 ledger rows (L1001 to L1289; by earliest origin: EVOL 41, AUTH 36, RECOV 41, SECD 44, WEB:OPS 43, WEB:ARCH 32, WEB:SEC 7, WEB:THIN 23, WEB:DCON 22), of which 16 merged rows merge 33 originals; 273 rows hold one original each.
- See-also links to part 1: 382 links to 195 distinct part-1 rows (32 state the same normative thing as a part-1 row, 345 related, 5 possible tension); 200 links between part-2 rows. Part 1 is unchanged.
- Web claims: imported 144 (OPS 45, ARCH 40, SEC 8, THIN 28, DCON 23), of which 33 restated stack-neutral; skipped 30 as web-specific (OPS 8, ARCH 5, SEC 1, THIN 12, DCON 4); SEC-C01 to SEC-C49, SEC-C59, SEC-C60 (51 claims) outside the restriction, not examined.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id of the four slots and every imported web claim id appears exactly once, none dropped, every in-scope web claim imported or skipped, every cited source resolves in part 1 or part 2`
- Sources: 118 source ids of the 4 round-3 results plus 98 web source ids cited by imported claims, replaced by 160 new rows (REG-1001 to REG-1160; T1 70, T2 46, T3 38, T4 6) and 49 ids mapped to existing part-1 rows (including AUTH-S21, mapped to the maintainer source REG-181, not citable, no tier).

### Files

- `claims_ledger_part2.md`: one row per merged claim (columns id, statement, merges, areas, level, stack, agreement, positions, certainty, sources), then the table of skipped web claims.
- `sources_part2.md`: new sources REG-1001 and up (one row per distinct source, with every original id it replaces and the highest tier) and the table of original ids that resolve to a part-1 row.
- `check_part2.py`: reads the four round-3 results, the five web results, part 1 and part 2; proves id coverage, area placement, the import-or-skip accounting of the web claims, tier choice, that every cited source resolves in part 1 or part 2, that every see-also link resolves, and that the files hold no absolute or home path; prints one PASS or FAIL line.
- `result.md`: this file.

### Method

- Claim blocks were parsed from the `### Claims` section of each result (single-line, one-field-per-line and table layouts); counts were checked per slot against the first and last id of each run (EVOL 41, AUTH 36, RECOV 41, SECD 44; web OPS 53, ARCH 45, THIN 40, DCON 27, SEC-C50 to SEC-C58 9).
- Web scope came from the inputs note: slots 06_operations, 07_architecture_styles, 14_thin_spots, 17_data_contracts in full and 05_identity_security restricted to secrets and supply chain. A claim with origin stack neutral was imported; a claim with another stack was imported restated only when its substance is a generic principle, otherwise skipped with a reason. Stack-neutral claims whose wording named the web or a tool were restated too.
- Merges: a pairwise lexical scan (weighted word cosine) over all 306 imported or round-3 claims, then a hand read of every pair above a low threshold plus the topical overlaps the scan misses (for example the decision-record and log claims phrased differently).
- See-also: a lexical scan of every part-2 claim against the 460 part-1 statements, then a hand read of all 460 part-1 statements to add the topical links the scan misses and to drop false matches.
- Sources: original ids grouped by identical normalised URL across the four slots and the cited web sources; a group touching a part-1 URL maps to that part-1 row, otherwise it becomes one new row; tier is the highest origin tier.

### The merged rows

| ledger id | origins | agreement of the origins | what the merge keeps apart or adds |
|---|---|---|---|
| L1002 | EVOL-C02, WEB:ARCH-C39 | consensus (EVOL-C02); majority (WEB:ARCH-C39) | Union of the two origin sentences; WEB:ARCH-C39 adds the confidence statement and that writing it clarifies group thinking. |
| L1003 | EVOL-C03, WEB:ARCH-C37 | consensus | Union of the two origin sentences; both state in-repository, numbered, plain-text records. WEB:ARCH-C37 names the directories (doc/adr, doc/arch). |
| L1004 | EVOL-C04, WEB:ARCH-C35 | majority (EVOL-C04); consensus (WEB:ARCH-C35) | WEB:ARCH-C35 states position (a) of EVOL-C04 (record every significant decision, as short records of one to two pages) as a consensus decision; EVOL-C04 adds the threshold question and the other two positions. |
| L1005 | EVOL-C05, WEB:ARCH-C38 | contested (EVOL-C05); consensus (WEB:ARCH-C38) | WEB:ARCH-C38 states the immutable rule as consensus; EVOL-C05 records the contested position (a mutable living document with dated additions) and the status-machine note. |
| L1011 | EVOL-C11, WEB:OPS-C40 | consensus | Union of the two origin sentences: EVOL-C11 generalises to code interfaces, remote APIs and schemas and adds the contract-step rationale; WEB:OPS-C40 states the database-schema form and the rollback rationale. |
| L1017 | EVOL-C17, WEB:ARCH-C42 | contested (EVOL-C17); consensus (WEB:ARCH-C42) | WEB:ARCH-C42 (strangler fig, consensus) is position (c) of EVOL-C17 (contested); EVOL-C17 adds positions (a) never rewrite and (b) rewrite under conditions. EVOL-C17 itself cites the strangler-fig source as sibling evidence. |
| L1143 | SECD-C25, WEB:THIN-C01 | consensus | Union of the two origin sentences. SECD-C25 adds the note that ASVS 5.0 requires these only from level 2; WEB:THIN-C01 adds that data-change events are optional. |
| L1144 | SECD-C26, WEB:THIN-C02 | consensus | Union of the two origin sentences; WEB:THIN-C03 (event vocabulary, ISO 8601 timestamps) and WEB:THIN-C09 (time synchronisation) are kept apart. |
| L1145 | SECD-C27, WEB:THIN-C08 | consensus (SECD-C27); consensus (single source, no dissent) (WEB:THIN-C08) | Union of the two origin sentences; WEB:THIN-C06 (keep logs apart from application data) is kept apart. |
| L1150 | SECD-C32, WEB:THIN-C07 | contested (SECD-C32); consensus (single source, no dissent) (WEB:THIN-C07) | WEB:THIN-C07 states the same decision as consensus; SECD-C32 adds the contested positions (retain for the legal minimum, or retain long and tier by age). |
| L1151 | SECD-C33, WEB:OPS-C05, WEB:THIN-C04 | consensus | Union of the three origin sentences; they do not conflict. WEB:OPS-C05 adds the injection clause (also held alone by WEB:THIN-C20 and, for log protection, by SECD-C27); WEB:THIN-C04 adds hashing and pseudonymisation; SECD-C33 adds the protection-level rule. |
| L1187 | WEB:OPS-C29, WEB:DCON-C19 | consensus not established (WEB:OPS-C29); contested (WEB:DCON-C19) | WEB:DCON-C19 extends WEB:OPS-C29 (its own text says so): the same open question, with the Pact documentation position added to the inferred answer of WEB:OPS-C29. Positions of both are kept. |
| L1192 | WEB:OPS-C34, WEB:SEC-C50 | consensus | Both origins state the same open-source litmus test from the Twelve-Factor config rule; WEB:SEC-C50 states it for secrets, WEB:OPS-C34 for config. |
| L1194 | WEB:OPS-C36, WEB:ARCH-C28 | consensus | WEB:ARCH-C28 states the dev/prod parity rule in one clause; WEB:OPS-C36 adds the backing-service clause and the adapter warning. Both rest on the Twelve-Factor dev/prod parity factor. |
| L1195 | WEB:OPS-C37, WEB:ARCH-C27 | consensus | WEB:ARCH-C27 adds 'keep config in the environment'; where config lives is the contested question of WEB:OPS-C35 and is not decided here. |
| L1196 | WEB:OPS-C38, WEB:ARCH-C21 | consensus | WEB:ARCH-C21 states the first half (evolve the schema with the code, versioned migrations in the repository); WEB:OPS-C38 adds the same-process-in-every-environment and release-step clauses. |

### Clearest overlaps with part 1 (states the same normative thing; kept apart because part 1 is read-only)

- L1038 (EVOL-C38) and L026 (SRC-C26)
- L1057 (AUTH-C16) and L172 (DELIVER-C49)
- L1071 (AUTH-C30) and L327 (MAINT-C63)
- L1078 (RECOV-C01) and L389 (DATA-C12)
- L1120 (SECD-C02) and L240 (TRANS-C31)
- L1131 (SECD-C13) and L246 (TRANS-C37)
- L1132 (SECD-C14) and L086 (VERIFY-C07)
- L1133 (SECD-C15) and L116 (VERIFY-C37)
- L1148 (SECD-C30) and L209 (OPERATE-C37)
- L1164 (WEB:OPS-C02) and L199 (OPERATE-C26)
- L1166 (WEB:OPS-C04) and L201 (OPERATE-C28)
- L1168 (WEB:OPS-C07) and L197 (OPERATE-C24)
- L1169 (WEB:OPS-C09) and L200 (OPERATE-C27, PERF-C41)
- L1172 (WEB:OPS-C12) and L190 (OPERATE-C17)
- L1173 (WEB:OPS-C13) and L177 (OPERATE-C04, PERF-C02)
- L1175 (WEB:OPS-C15) and L184 (OPERATE-C11)
- L1176 (WEB:OPS-C16) and L189 (OPERATE-C16, PERF-C35)
- L1183 (WEB:OPS-C25) and L091 (VERIFY-C12)
- L1188 (WEB:OPS-C30) and L092 (VERIFY-C13)
- L1191 (WEB:OPS-C33) and L150 (DELIVER-C27)
- L1192 (WEB:OPS-C34, WEB:SEC-C50) and L158 (DELIVER-C35, TRANS-C45)
- L1194 (WEB:OPS-C36, WEB:ARCH-C28) and L165 (DELIVER-C42, TRANS-C55)
- L1195 (WEB:OPS-C37, WEB:ARCH-C27) and L343 (EXT-C13)
- L1196 (WEB:OPS-C38, WEB:ARCH-C21) and L379 (DATA-C02)
- L1197 (WEB:OPS-C39) and L385 (DATA-C08)
- L1199 (WEB:OPS-C42) and L156 (DELIVER-C33)
- L1200 (WEB:OPS-C43) and L153 (DELIVER-C30)
- L1239 (WEB:SEC-C52) and L257 (TRANS-C49)
- L1243 (WEB:SEC-C57) and L012 (SRC-C12, ADOPT-C09)
- L1278 (WEB:DCON-C14) and L341 (EXT-C11)
- L1283 (WEB:DCON-C20) and L104 (VERIFY-C25)
- L1284 (WEB:DCON-C21) and L222 (TRANS-C13)

### Possible tensions with part 1

- L1026 (EVOL-C26) and L140 (DELIVER-C17)
- L1208 (WEB:ARCH-C03) and L330 (MAINT-C66)
- L1255 (WEB:THIN-C21) and L416 (DATA-C40)
- L1256 (WEB:THIN-C22) and L416 (DATA-C40)
- L1259 (WEB:THIN-C27) and L279 (MAINT-C15)

### Near pairs kept apart inside part 2 (each listed once)

- L1001 (EVOL-C01) and L1009 (EVOL-C09)
- L1006 (EVOL-C06) and L1233 (WEB:ARCH-C36)
- L1006 (EVOL-C06) and L1289 (WEB:DCON-C27)
- L1009 (EVOL-C09) and L1233 (WEB:ARCH-C36)
- L1010 (EVOL-C10) and L1011 (EVOL-C11, WEB:OPS-C40)
- L1010 (EVOL-C10) and L1017 (EVOL-C17, WEB:ARCH-C42)
- L1011 (EVOL-C11, WEB:OPS-C40) and L1012 (EVOL-C12)
- L1016 (EVOL-C16) and L1281 (WEB:DCON-C17)
- L1017 (EVOL-C17, WEB:ARCH-C42) and L1235 (WEB:ARCH-C41)
- L1018 (EVOL-C18) and L1020 (EVOL-C20)
- L1020 (EVOL-C20) and L1207 (WEB:ARCH-C02)
- L1020 (EVOL-C20) and L1237 (WEB:ARCH-C44)
- L1028 (EVOL-C28) and L1041 (EVOL-C41)
- L1034 (EVOL-C34) and L1114 (RECOV-C37)
- L1034 (EVOL-C34) and L1154 (SECD-C36)
- L1035 (EVOL-C35) and L1041 (EVOL-C41)
- L1038 (EVOL-C38) and L1229 (WEB:ARCH-C31)
- L1038 (EVOL-C38) and L1039 (EVOL-C39)
- L1038 (EVOL-C38) and L1040 (EVOL-C40)
- L1040 (EVOL-C40) and L1229 (WEB:ARCH-C31)
- L1048 (AUTH-C07) and L1200 (WEB:OPS-C43)
- L1054 (AUTH-C13) and L1129 (SECD-C11)
- L1055 (AUTH-C14) and L1126 (SECD-C08)
- L1056 (AUTH-C15) and L1140 (SECD-C22)
- L1056 (AUTH-C15) and L1243 (WEB:SEC-C57)
- L1057 (AUTH-C16) and L1200 (WEB:OPS-C43)
- L1069 (AUTH-C28) and L1239 (WEB:SEC-C52)
- L1073 (AUTH-C32) and L1252 (WEB:THIN-C13)
- L1073 (AUTH-C32) and L1143 (SECD-C25, WEB:THIN-C01)
- L1074 (AUTH-C33) and L1243 (WEB:SEC-C57)
- L1075 (AUTH-C34) and L1254 (WEB:THIN-C20)
- L1090 (RECOV-C13) and L1145 (SECD-C27, WEB:THIN-C08)
- L1092 (RECOV-C15) and L1255 (WEB:THIN-C21)
- L1092 (RECOV-C15) and L1256 (WEB:THIN-C22)
- L1092 (RECOV-C15) and L1258 (WEB:THIN-C26)
- L1095 (RECOV-C18) and L1146 (SECD-C28)
- L1095 (RECOV-C18) and L1138 (SECD-C20)
- L1097 (RECOV-C20) and L1160 (SECD-C42)
- L1109 (RECOV-C32) and L1191 (WEB:OPS-C33)
- L1114 (RECOV-C37) and L1157 (SECD-C39)
- L1114 (RECOV-C37) and L1154 (SECD-C36)
- L1120 (SECD-C02) and L1162 (SECD-C44)
- L1124 (SECD-C06) and L1162 (SECD-C44)
- L1138 (SECD-C20) and L1146 (SECD-C28)
- L1140 (SECD-C22) and L1242 (WEB:SEC-C56)
- L1140 (SECD-C22) and L1243 (WEB:SEC-C57)
- L1143 (SECD-C25, WEB:THIN-C01) and L1159 (SECD-C41)
- L1143 (SECD-C25, WEB:THIN-C01) and L1252 (WEB:THIN-C13)
- L1144 (SECD-C26, WEB:THIN-C02) and L1245 (WEB:THIN-C03)
- L1144 (SECD-C26, WEB:THIN-C02) and L1248 (WEB:THIN-C09)
- L1145 (SECD-C27, WEB:THIN-C08) and L1247 (WEB:THIN-C06)
- L1145 (SECD-C27, WEB:THIN-C08) and L1254 (WEB:THIN-C20)
- L1150 (SECD-C32, WEB:THIN-C07) and L1154 (SECD-C36)
- L1151 (SECD-C33, WEB:OPS-C05, WEB:THIN-C04) and L1254 (WEB:THIN-C20)
- L1151 (SECD-C33, WEB:OPS-C05, WEB:THIN-C04) and L1155 (SECD-C37)
- L1151 (SECD-C33, WEB:OPS-C05, WEB:THIN-C04) and L1152 (SECD-C34)
- L1165 (WEB:OPS-C03) and L1167 (WEB:OPS-C06)
- L1165 (WEB:OPS-C03) and L1253 (WEB:THIN-C19)
- L1165 (WEB:OPS-C03) and L1170 (WEB:OPS-C10)
- L1165 (WEB:OPS-C03) and L1171 (WEB:OPS-C11)
- L1167 (WEB:OPS-C06) and L1253 (WEB:THIN-C19)
- L1169 (WEB:OPS-C09) and L1170 (WEB:OPS-C10)
- L1169 (WEB:OPS-C09) and L1171 (WEB:OPS-C11)
- L1184 (WEB:OPS-C26) and L1185 (WEB:OPS-C27)
- L1186 (WEB:OPS-C28) and L1281 (WEB:DCON-C17)
- L1186 (WEB:OPS-C28) and L1282 (WEB:DCON-C18)
- L1186 (WEB:OPS-C28) and L1283 (WEB:DCON-C20)
- L1193 (WEB:OPS-C35) and L1238 (WEB:SEC-C51)
- L1196 (WEB:OPS-C38, WEB:ARCH-C21) and L1197 (WEB:OPS-C39)
- L1196 (WEB:OPS-C38, WEB:ARCH-C21) and L1198 (WEB:OPS-C41)
- L1208 (WEB:ARCH-C03) and L1236 (WEB:ARCH-C43)
- L1215 (WEB:ARCH-C10) and L1216 (WEB:ARCH-C11)
- L1216 (WEB:ARCH-C11) and L1234 (WEB:ARCH-C40)
- L1225 (WEB:ARCH-C20) and L1285 (WEB:DCON-C22)
- L1227 (WEB:ARCH-C29) and L1232 (WEB:ARCH-C34)
- L1228 (WEB:ARCH-C30) and L1232 (WEB:ARCH-C34)
- L1229 (WEB:ARCH-C31) and L1232 (WEB:ARCH-C34)
- L1234 (WEB:ARCH-C40) and L1284 (WEB:DCON-C21)
- L1241 (WEB:SEC-C55) and L1242 (WEB:SEC-C56)
- L1241 (WEB:SEC-C55) and L1243 (WEB:SEC-C57)
- L1241 (WEB:SEC-C55) and L1244 (WEB:SEC-C58)
- L1245 (WEB:THIN-C03) and L1248 (WEB:THIN-C09)
- L1246 (WEB:THIN-C05) and L1252 (WEB:THIN-C13)
- L1250 (WEB:THIN-C11) and L1252 (WEB:THIN-C13)
- L1255 (WEB:THIN-C21) and L1256 (WEB:THIN-C22)
- L1255 (WEB:THIN-C21) and L1258 (WEB:THIN-C26)
- L1256 (WEB:THIN-C22) and L1258 (WEB:THIN-C26)
- L1257 (WEB:THIN-C23) and L1258 (WEB:THIN-C26)
- L1259 (WEB:THIN-C27) and L1260 (WEB:THIN-C28)
- L1259 (WEB:THIN-C27) and L1261 (WEB:THIN-C29)
- L1259 (WEB:THIN-C27) and L1262 (WEB:THIN-C31)
- L1262 (WEB:THIN-C31) and L1286 (WEB:DCON-C23)
- L1262 (WEB:THIN-C31) and L1275 (WEB:DCON-C10)
- L1263 (WEB:THIN-C32) and L1265 (WEB:THIN-C34)
- L1264 (WEB:THIN-C33) and L1265 (WEB:THIN-C34)
- L1271 (WEB:DCON-C06) and L1284 (WEB:DCON-C21)
- L1271 (WEB:DCON-C06) and L1277 (WEB:DCON-C12)
- L1272 (WEB:DCON-C07) and L1273 (WEB:DCON-C08)
- L1274 (WEB:DCON-C09) and L1280 (WEB:DCON-C16)
- L1274 (WEB:DCON-C09) and L1275 (WEB:DCON-C10)

### Web claims restated stack-neutral

| web claim | origin stack | ledger row |
|---|---|---|
| WEB:OPS-C02 | http | L1164 |
| WEB:OPS-C10 | http | L1170 |
| WEB:OPS-C11 | http | L1171 |
| WEB:OPS-C18 | postgres | L1177 |
| WEB:OPS-C23 | neutral | L1181 |
| WEB:OPS-C26 | postgres | L1184 |
| WEB:OPS-C27 | python | L1185 |
| WEB:OPS-C29 | neutral | L1187 |
| WEB:OPS-C51 | python | L1204 |
| WEB:ARCH-C05 | neutral | L1210 |
| WEB:ARCH-C19 | python | L1224 |
| WEB:ARCH-C20 | postgres | L1225 |
| WEB:ARCH-C21 | postgres | L1196 |
| WEB:ARCH-C22 | http | L1226 |
| WEB:ARCH-C34 | postgres | L1232 |
| WEB:SEC-C55 | python | L1241 |
| WEB:THIN-C12 | postgres | L1251 |
| WEB:THIN-C21 | postgres | L1255 |
| WEB:THIN-C22 | postgres | L1256 |
| WEB:THIN-C23 | postgres | L1257 |
| WEB:DCON-C02 | http | L1269 |
| WEB:DCON-C03 | http | L1270 |
| WEB:DCON-C06 | python | L1271 |
| WEB:DCON-C07 | python | L1272 |
| WEB:DCON-C08 | python | L1273 |
| WEB:DCON-C10 | neutral | L1275 |
| WEB:DCON-C11 | neutral | L1276 |
| WEB:DCON-C12 | python, js, postgres | L1277 |
| WEB:DCON-C15 | http | L1279 |
| WEB:DCON-C16 | python | L1280 |
| WEB:DCON-C21 | http | L1284 |
| WEB:DCON-C22 | postgres | L1285 |
| WEB:DCON-C23 | postgres | L1286 |

### Web claims skipped

| web claim | origin stack | reason |
|---|---|---|
| WEB:OPS-C08 | js | browser-side OpenTelemetry maturity (js, web-specific) |
| WEB:OPS-C17 | http | Server-Timing response header (http, web-specific) |
| WEB:OPS-C21 | js | Core Web Vitals thresholds (page experience, web-specific) |
| WEB:OPS-C47 | http | Cache-Control on every HTTP response (http caching, web-specific) |
| WEB:OPS-C48 | http | fingerprinted static assets and cache headers (http caching, web-specific) |
| WEB:OPS-C49 | http | private or no-store for personalized HTTP responses (http caching, web-specific) |
| WEB:OPS-C50 | http | Vary header (http caching, web-specific) |
| WEB:OPS-C52 | python | page-level cache variance on cookie state (framework and web-specific) |
| WEB:ARCH-C23 | http | client-server separation as a web constraint (web-specific) |
| WEB:ARCH-C24 | http | stateless request as a REST constraint (web-specific; stateless processes are held by OPS-C46) |
| WEB:ARCH-C25 | http | intermediaries and caches as REST layered-system constraint (web-specific) |
| WEB:ARCH-C26 | js | where rendering happens (web-specific) |
| WEB:ARCH-C45 | neutral | synthesis about a web app as a whole (web-specific, inferred by its origin) |
| WEB:SEC-C53 | python | framework signing secret of one web framework (stack-specific) |
| WEB:THIN-C14 | js | browser global error handlers (js, web-specific) |
| WEB:THIN-C15 | js | sendBeacon from visibilitychange (js, web-specific) |
| WEB:THIN-C16 | http | Reporting API and Reporting-Endpoints header (http, web-specific) |
| WEB:THIN-C17 | js | web-vitals field measurement (js, web-specific) |
| WEB:THIN-C18 | js | PerformanceObserver (js, web-specific) |
| WEB:THIN-C24 | postgres | PostgreSQL 18 application-time constraints (engine and version-specific) |
| WEB:THIN-C25 | postgres | absence of SQL:2011 system-versioned tables in PostgreSQL (engine-specific) |
| WEB:THIN-C30 | postgres | PostgreSQL trigger timing semantics (engine-specific; the general split is THIN-C31) |
| WEB:THIN-C37 | http | Post/Redirect/Get with 303 (http, web-specific) |
| WEB:THIN-C38 | http | meaning of HTTP 303 (http, web-specific) |
| WEB:THIN-C39 | http | 303 versus 307 and 302 (http, web-specific) |
| WEB:THIN-C40 | python | framework redirect after POST (python and web-specific) |
| WEB:DCON-C04 | python, http | one schema dialect across OpenAPI and Pydantic (tool-specific) |
| WEB:DCON-C05 | python | request and response schema modes of one library (tool-specific) |
| WEB:DCON-C13 | js | TypeScript types generated from OpenAPI are runtime-free (js, web-specific) |
| WEB:DCON-C24 | postgres | PostgreSQL domains and NULL pitfalls (engine-specific) |

### Source register: new rows replacing several original ids

| reg | tier | replaces |
|---|---|---|
| REG-1016 | T2 | EVOL-S19, WEB:ARCH-S03 |
| REG-1022 | T3 | EVOL-S29, WEB:ARCH-S04 |
| REG-1089 | T1 | SECD-S15, WEB:OPS-S18, WEB:THIN-S01 |
| REG-1090 | T1 | SECD-S16, WEB:THIN-S03 |
| REG-1109 | T2 | WEB:OPS-S19, WEB:ARCH-S07 |
| REG-1139 | T1 | WEB:THIN-S06, WEB:DCON-S04 |

### Script output (check_part2.py)

```
claims in (four slots): EVOL 41, AUTH 36, RECOV 41, SECD 44; total 162
web claims in scope: 174 (OPS 53, ARCH 45, SEC 9, THIN 40, DCON 27); imported 144; skipped 30
rows out: 289; merged rows: 16 merging 33 originals
see also links: 382 to part 1 (195 distinct part-1 rows), 200 within part 2
dropped: 0; unplaced: 0; claims in more than one row: 0; unknown ids: 0
sources: 118 original ids of the four slots (+ 98 cited web ids) -> 160 new rows and 49 ids mapped to part 1; citations checked in origin claims: 792; distinct sources cited by the ledger: 200
PASS: every original claim id of the four slots and every imported web claim id appears exactly once, none dropped, every in-scope web claim imported or skipped, every cited source resolves in part 1 or part 2
```
