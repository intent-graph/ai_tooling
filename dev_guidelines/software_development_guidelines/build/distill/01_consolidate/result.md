# Consolidation of the research claims into one ledger and one source register

## L1 headline

The ten claim-bearing research results (482 claims, 296 source ids) are merged into one claims ledger (460 rows) and one deduplicated source register (264 sources) with no claim dropped and none unplaced, so that a later step can attach them to a structure the maintainer has not fixed yet. Certainty: grounded for the counts and the id coverage (a script reads the ten results and proves them), inferred for the 21 merge decisions (they rest on my reading that the origins state the same thing).

Pinned:
- Claims in: 482 original claims from 10 research results (SRC 36, ADOPT 51, VERIFY 44, DELIVER 50, OPERATE 38, TRANS 58, MAINT 67, EXT 51, DATA 43, PERF 44).
- Rows out: 460 ledger rows, of which 21 merged rows merge 43 originals; 439 rows hold one original each.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id appears exactly once, none dropped, none unplaced, every cited source resolves`
- Distinct sources: 264 from 296 original source ids; by tier T1 106, T2 103, T3 50, T4 4, maintainer 1 (MAINT-S01, not citable).

## L2 claims

Pinned:
- Claims in: 482 original claims from 10 research results (SRC 36, ADOPT 51, VERIFY 44, DELIVER 50, OPERATE 38, TRANS 58, MAINT 67, EXT 51, DATA 43, PERF 44).
- Rows out: 460 ledger rows, of which 21 merged rows merge 43 originals; 439 rows hold one original each.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id appears exactly once, none dropped, none unplaced, every cited source resolves`
- Distinct sources: 264 from 296 original source ids; by tier T1 106, T2 103, T3 50, T4 4, maintainer 1 (MAINT-S01, not citable).

Each line carries its certainty: grounded (I can name the file or the script run that makes it true), inferred (my reading), open (not determined).

### Claims of this consolidation

- Every original claim id of the 10 results appears in exactly one ledger row; none is dropped, none sits in a row without its origin area. (grounded (script run, output in L3))
- The ledger is ordered by origin area (SRC, ADOPT, VERIFY, DELIVER, OPERATE, TRANS, MAINT, EXT, DATA, PERF) and carries no hierarchy, no owner, no judgement; rows per area: SRC 36, ADOPT 43, VERIFY 44, DELIVER 50, OPERATE 36, TRANS 55, MAINT 67, EXT 47, DATA 41, PERF 41. (grounded)
- 21 rows merge 43 originals (20 rows of two, 1 row of three); the 21 are listed with their origins in L3. Positions of each origin are kept, labelled by origin id; statements of merged rows are either the wording of the fuller origin or a union of non-conflicting origin sentences; no position is averaged. (grounded for the list, inferred for each merge decision)
- Merge criterion: the origins state the same normative thing, one possibly with an extra clause that does not conflict. Not merged when an origin adds an independent claim (for example SRC-C04 and ADOPT-C11, where ADOPT-C11 adds four criteria) or when the imperatives differ though they share a source (SRC-C14, ADOPT-C29 and VERIFY-C26, all Hyrum's Law). (inferred (a judgement call; the near pairs are kept apart and cross-referenced so it can be reversed))
- Of the 23 overlap clusters of the coverage check (section 2), 12 are merged here in whole or in part; the others are kept apart and cross-referenced in the `positions` column as `see also`: SRC-C14 / ADOPT-C29 / VERIFY-C26, SRC-C06 and C07 / ADOPT-C10, SRC-C04 / ADOPT-C11, SRC-C10 / ADOPT-C38, SRC-C35 / ADOPT-C40 and C50, SRC-C36 / ADOPT-C11, ADOPT-C18 / DELIVER-C26, DELIVER-C46 / OPERATE-C36, VERIFY-C42 / TRANS-C35, the flaky-test and ten-minute-feedback groups, MAINT-C44 / ADOPT-C01 and SRC-C24. (grounded for the list, inferred for the reading of each)
- Round-2 overlaps found beyond the coverage check (which covered round 1 only): 9 merges link an EXT, DATA or PERF claim to an earlier one (12 merges come from the coverage check, 9 from round 2; ids in L3); further near pairs kept apart: PERF-C34 / OPERATE-C34, DATA-C03 / MAINT-C22 and C23, SRC-C35 / EXT-C32. (grounded for the list (a text-similarity scan plus reading), inferred for the readings)
- The maintainer's 67 claims stay 67 separate rows except one: MAINT-C28 and DATA-C34 state the same schema-version gate (merged, both ids kept). Three DATA claims (DATA-C35 to C37) record that no public counterpart was found for a maintainer practice, and DATA-C38 is the nearest public form of MAINT-C16; all four are kept as their own rows, not merged with the MAINT rows, because an absence record or a nearest form is not the same claim. (grounded for the counts, inferred for the reading of DATA-C35 to C38)
- The maintainer-versus-research relations of the coverage check section 5 (10 maintainer claims, with 6 more recorded as having no public counterpart) are written into the `positions` column of the maintainer row and of the public rows concerned, with ledger ids, as recorded there; MAINT-C46 is noted as matching, not contradicting. I made no new judgement of contradiction. (grounded)
- The source register has 264 rows for 296 original ids (32 absorbed): 27 rows replace two or more ids, found by identical normalised URL plus two pairs the URL test misses (Scorecard checks raw and rendered, NIST SP 800-218 PDF and landing page). Tier is the highest of the origin tiers; it rises for 3 rows (REG-009, REG-012, REG-013). (grounded for the counts, inferred that near-identical titles at different URLs (none found) would be separate sources)
- Tier counts of the distinct sources: T1 106, T2 103, T3 50, T4 4, maintainer 1. Three rows record no page read (two T4 search-result sources, one T2 book chapter not fetched). (grounded)
- Agreement as recorded by the origins, over 460 rows: consensus 183, majority 130, maintainer rows 67, contested 66, not assessable 6, mixed (merged origins differ) 5, n/a 3. Certainty as recorded: grounded 429, inferred 16, not stated by origin 7, open 8. Level: principle 104, decision 122, practice 233, open 1. (grounded (counted from the ledger))
- Seven origin claims record no certainty field (VERIFY-C11, C19, C22, C24, C34, C35, C41); the ledger says `not stated by origin (sources cited)` rather than assigning one. Six origin claims have agreement `not assessable` (ADOPT-C50, EXT-C15, C17, C38, C48, C51) and three have `n/a` (DATA-C36, C37, PERF-C44; MAINT-C67 too, as a maintainer row); they keep that wording. (grounded)
- Source ids inside `positions` and `certainty` texts were rewritten from slot-local tags (S05) to register ids (REG-nnn), because a merged row mixes slots; the claim wording itself is untouched except for the same rewrite where a claim sentence cited a source. (grounded)

### Not done

- The origin claims were not re-checked against their sources; certainty is as recorded by each slot (grounded in the origin, not by me). (open: spot-check of the coverage check covered six claims of round 1 only)
- No structure, grouping, owner, judgement of which position wins, or deletion of any claim; this is the maintainer's later step. (grounded: by construction)
- Cross-references to near rows are my reading, not a check of equality; the `see also` notes are an aid to the merge decisions of the later step. (inferred)
- Contested topics are not re-counted here; the coverage check lists 56 and the ledger keeps each origin's agreement and positions. (grounded)

## L3 full

Pinned:
- Claims in: 482 original claims from 10 research results (SRC 36, ADOPT 51, VERIFY 44, DELIVER 50, OPERATE 38, TRANS 58, MAINT 67, EXT 51, DATA 43, PERF 44).
- Rows out: 460 ledger rows, of which 21 merged rows merge 43 originals; 439 rows hold one original each.
- Dropped: 0. Unplaced: 0.
- Script: `PASS: every original claim id appears exactly once, none dropped, none unplaced, every cited source resolves`
- Distinct sources: 264 from 296 original source ids; by tier T1 106, T2 103, T3 50, T4 4, maintainer 1 (MAINT-S01, not citable).

### Files

- `claims_ledger.md`: one row per merged claim, columns id, statement, merges, areas, level, stack, agreement, positions, certainty, sources.
- `sources.md`: one row per distinct source, with every original source id it replaces and the highest tier.
- `check_ledger.py`: reads the ten results, the ledger and the register; proves id coverage, area placement, tier choice and that every cited source resolves; prints one PASS or FAIL line.
- `result.md`: this file.

### Method

- Claim blocks were parsed from the `### Claims` section of each result (several layouts across the slots: single-line fields, one field per line, prose with `Level:` and `Agreement:` labels, bullet variants); parse failures were checked by counting ids per slot against the first and last id of each run (SRC 36, ADOPT 51, VERIFY 44, DELIVER 50, OPERATE 38 including OPERATE-C28b, TRANS 58, MAINT 67, EXT 51, DATA 43, PERF 44).
- Sources: registers parsed (tables, and the DATA bullet list); one distinct source per normalised URL, plus two manual pairs; tier is the minimum tier number. Claim citations are read from `sources`, `positions`, `agreement` and `certainty` fields and mapped to register ids; the script re-reads the whole claim block, not only those fields, and requires each cited source to appear on the row.
- Merge candidates: the coverage check section 2, then a pairwise text-similarity scan of all 482 statements across slots (cosine over weighted words, threshold 0.35) read by hand; round 2 was not covered by the coverage check.

### The merged rows

| ledger id | origins | agreement of the origins | what the merge keeps apart or adds |
|---|---|---|---|
| L001 | SRC-C01, ADOPT-C08 | consensus | ADOPT-C08 states the same necessity test in one clause; SRC-C01 adds the rationale (attack surface and ownership cost). |
| L002 | SRC-C02, ADOPT-C02, ADOPT-C03 | contested (SRC-C02); majority (ADOPT-C02); consensus (ADOPT-C03) | ADOPT-C02 (reuse well-vetted components) and ADOPT-C03 (build only what third-party components cannot better meet) are the two ends of the decision SRC-C02 states; ADOPT-C02 lists its own three positions. |
| L009 | SRC-C09, ADOPT-C39 | consensus | Same check; ADOPT-C39 words it as tracking maintenance status and end of life. |
| L012 | SRC-C12, ADOPT-C09 | consensus | ADOPT-C09 states the authenticity check without the signed-package and name-check details SRC-C12 adds. |
| L013 | SRC-C13, ADOPT-C34 | majority | Statement is the union of the two origin sentences; they do not conflict. SRC-C13 adds the rebuild clause, ADOPT-C34 the integrity checks and its two positions. |
| L024 | SRC-C24, ADOPT-C05 | contested (SRC-C24); majority (ADOPT-C05) | Union of the two origin sentences; same source family (innovation tokens). SRC-C24 adds the staged-novelty position. |
| L027 | SRC-C27, ADOPT-C12 | contested (SRC-C27); consensus (ADOPT-C12) | Union of the two origin sentences; SRC-C27 is contested, ADOPT-C12 states the scaling rule as consensus. |
| L032 | SRC-C32, EXT-C09 | consensus | Union of the two origin sentences; EXT-C09 names SRC-C32 as the same stance and adds the degraded-mode design and exercise. |
| L034 | SRC-C34, EXT-C21 | consensus | Union of the two origin sentences; EXT-C21 cites SRC-C34 as the round-1 version. |
| L043 | ADOPT-C13, TRANS-C54 | consensus | TRANS-C54 words the same rule with 'completely and exactly' and the one-command onboarding test. |
| L073 | ADOPT-C45, EXT-C27 | majority | Union of the two origin sentences; both rest on the same Fowler essay (ADOPT-C45 on S11, EXT-C27 on S23). |
| L075 | ADOPT-C47, EXT-C28 | contested | Union of the two origin sentences; the positions of both origins are kept apart (EXT-C28 adds the regulated-exit position). |
| L120 | VERIFY-C41, OPERATE-C28b | contested | Same single T3 source (chaos principles) in both origins. |
| L158 | DELIVER-C35, TRANS-C45 | consensus | Union of the two origin sentences; both rest on the Twelve-Factor config rule. |
| L165 | DELIVER-C42, TRANS-C55 | contested (DELIVER-C42); majority (TRANS-C55) | Union of the two origin sentences; both rest on Twelve-Factor dev/prod parity. DELIVER-C42 adds the pre-production-versus-rollout decision; positions of both origins are kept apart. |
| L168 | DELIVER-C45, DATA-C01 | majority (DELIVER-C45); consensus (DATA-C01) | DELIVER-C45 states the same pipeline rule in one clause; DATA-C01 adds the framing as primary delivery risk and the exclusion of a separate manual track. |
| L173 | DELIVER-C50, OPERATE-C35 | consensus | Union of the two origin sentences. OPERATE-C35 adds the playbook clause. |
| L177 | OPERATE-C04, PERF-C02 | consensus | Union of the two origin sentences. |
| L189 | OPERATE-C16, PERF-C35 | consensus | Union of the two origin sentences; same SRE source. |
| L200 | OPERATE-C27, PERF-C41 | contested | PERF-C41 restates the same decision from the same OpenTelemetry page, adding a cost source and the above-1000-traces-per-second hint. |
| L292 | MAINT-C28, DATA-C34 | maintainer decision (single source); public practice read as majority (MAINT-C28); majority (DATA-C34) | MAINT-C28 and DATA-C34 state the same gate; DATA-C34 records that public sources support only the order (schema first, then application), not an explicit version gate. |

### Near pairs kept apart (cross-referenced in the ledger)

- L014 (SRC-C14), L059 (ADOPT-C29), L105 (VERIFY-C26): compatibility promise and Hyrum's Law; the coverage check lists them as one claim, kept apart here because each states a different imperative.
- L006 (SRC-C06), L007 (SRC-C07), L041 (ADOPT-C10): activity and number of maintainers; ADOPT-C10 states both in one sentence.
- L004 (SRC-C04), L042 (ADOPT-C11): evaluate in the context of intended use; ADOPT-C11 adds four criteria (tests, API documentation, secure defaults, licence).
- L010 (SRC-C10), L067 (ADOPT-C38): vulnerability status of a component, at selection time and over its life.
- L035 (SRC-C35), L068 (ADOPT-C40), L078 (ADOPT-C50), L359 (EXT-C32): exit, portability and abstraction.
- L036 (SRC-C36), L042 (ADOPT-C11): licence check.
- L048 (ADOPT-C18), L149 (DELIVER-C26): reproducible builds.
- L169 (DELIVER-C46), L208 (OPERATE-C36): recovery time and change fail rate.
- L121 (VERIFY-C42), L244 (TRANS-C35): policy per stage and risk (analysis and test types versus code review), both from SSDF.
- L109 (VERIFY-C30), L110 (VERIFY-C31), L111 (VERIFY-C32), L147 (DELIVER-C24): flaky tests.
- L112 (VERIFY-C33), L144 (DELIVER-C21), L145 (DELIVER-C22): ten-minute feedback and self-testing build on every push.
- L308 (MAINT-C44), L037 (ADOPT-C01), L024 (SRC-C24): a new layer or technology must earn its cost.
- L002 (SRC-C02), L071 (ADOPT-C43): ADOPT-C43 restates position (b) of SRC-C02 as its own contested claim.
- L411 (DATA-C35), L294 (MAINT-C30): DATA-C35 records that no public counterpart was found for the practice MAINT-C30 states.
- L412 (DATA-C36), L306 (MAINT-C42): DATA-C36 records that no public counterpart was found for the practice MAINT-C42 states.
- L413 (DATA-C37), L301 (MAINT-C37), L302 (MAINT-C38): DATA-C37 records that no public counterpart was found for the practice MAINT-C37 and MAINT-C38 state.
- L414 (DATA-C38), L280 (MAINT-C16): DATA-C38 is the nearest public form of MAINT-C16 (explicit opt-in for operations whose scope can widen).
- L380 (DATA-C03), L286 (MAINT-C22), L287 (MAINT-C23): migration history record and never editing an applied migration.
- L452 (PERF-C34), L207 (OPERATE-C34): on-call load limit of about 25 percent.
- L310 (MAINT-C46), L002 (ADOPT-C03), L002 (SRC-C02): coverage check section 5: matches, not a contradiction.

### Maintainer versus research relations written into the ledger (coverage check section 5)

- L290 (MAINT-C26): contradicts L159 (DELIVER-C36); inside the contested range of L156 (DELIVER-C33).
- L328 (MAINT-C64): contradicts L165 (DELIVER-C42); contradicts L165 (TRANS-C55); contradicts L159 (DELIVER-C36).
- L330 (MAINT-C66): contradicts L038 (ADOPT-C04).
- L295 (MAINT-C31): contradicts L171 (DELIVER-C48); contradicts L102 (VERIFY-C23); partial tension with L060 (ADOPT-C30); partial tension with L014 (SRC-C14); compatible with, for single-version services, L135 (DELIVER-C12).
- L294 (MAINT-C30): contradicts L168 (DELIVER-C45).
- L265 (MAINT-C01): contradicts L111 (VERIFY-C32); partial tension with L119 (VERIFY-C40).
- L288 (MAINT-C24): partial tension with L162 (DELIVER-C39); agrees with L163 (DELIVER-C40).
- L318 (MAINT-C54): partial tension with L218 (TRANS-C09); partial tension with L133 (DELIVER-C10); agrees on dating with L216 (TRANS-C07).
- L298 (MAINT-C34): partial tension with L143 (DELIVER-C20).
- L331 (MAINT-C67): if the open gap is confirmed, contradicts L081 (VERIFY-C02); if confirmed, contradicts L106 (VERIFY-C27); if confirmed, contradicts L144 (DELIVER-C21).
- No public claim exists to contradict or support: L270 (MAINT-C06), L309 (MAINT-C45), L311 (MAINT-C47), L323 (MAINT-C59), L326 (MAINT-C62), L327 (MAINT-C63).

### Source register: distinct sources replacing several ids

| reg | tier | replaces |
|---|---|---|
| REG-001 | T1 | SRC-S01, ADOPT-S07 |
| REG-003 | T1 | SRC-S03, ADOPT-S08 |
| REG-004 | T1 | SRC-S04, ADOPT-S05, VERIFY-S24, DELIVER-S24, TRANS-S23 |
| REG-009 | T1 | SRC-S09, EXT-S27 |
| REG-011 | T2 | SRC-S11, ADOPT-S01 |
| REG-012 | T2 | SRC-S12, ADOPT-S02 |
| REG-013 | T2 | SRC-S13, ADOPT-S28 |
| REG-014 | T2 | SRC-S14, ADOPT-S06, TRANS-S28 |
| REG-023 | T1 | ADOPT-S04, DELIVER-S34 |
| REG-026 | T2 | ADOPT-S11, EXT-S23 |
| REG-030 | T1 | ADOPT-S15, DELIVER-S28 |
| REG-057 | T2 | VERIFY-S14, DELIVER-S16 |
| REG-069 | T3 | VERIFY-S27, OPERATE-S24 |
| REG-077 | T2 | DELIVER-S01, PERF-S16 |
| REG-086 | T1 | DELIVER-S10, EXT-S20 |
| REG-087 | T2 | DELIVER-S11, DATA-S03 |
| REG-093 | T2 | DELIVER-S18, OPERATE-S21 |
| REG-103 | T2 | DELIVER-S30, TRANS-S27 |
| REG-104 | T2 | DELIVER-S31, PERF-S14 |
| REG-105 | T2 | DELIVER-S32, DATA-S02 |
| REG-113 | T2 | DELIVER-S41, OPERATE-S16 |
| REG-119 | T1 | OPERATE-S03, PERF-S26 |
| REG-124 | T2 | OPERATE-S08, PERF-S07 |
| REG-125 | T2 | OPERATE-S09, EXT-S25, PERF-S09 |
| REG-130 | T2 | OPERATE-S14, PERF-S10 |
| REG-131 | T2 | OPERATE-S15, PERF-S08 |
| REG-203 | T2 | EXT-S24, PERF-S04 |

### Script output (check_ledger.py)

```
claims in: 482 from 10 results
rows out: 460; merged rows: 21 merging 43 originals
dropped: 0; unplaced: 0; claims in more than one row: 0; unknown ids: 0
sources: 296 original ids -> 264 distinct; citations checked in origin claims: 1186; distinct sources cited by the ledger: 262
PASS: every original claim id appears exactly once, none dropped, none unplaced, every cited source resolves
```

