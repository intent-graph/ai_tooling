# J5_construction: review result

## L1 headline

Review of J5_construction: records reviewed: 48 (CONSTRUCTION, 10 L2, 37 L3). Findings `fix`: 16. Findings `flag`: 9. Sources fetched: 9, of which 6 confirmed and 3 partly (the pattern is stated, a cited condition or detail is not). The decisions are sound in direction and none is an average; the defects are mostly seams with the settled J2 records (type derivation, deprecation, input and output models, restated three times), two ungrounded or overstated clauses (a set-oriented rule with no row, a 10x figure written as a rule) and language mechanisms left in three places. The contested nodes: one deployable unit first passes against the strongest sources (grounded); interface by signature rests on the maintainer alone (flag); store as contract holds for privilege separation but its "several direct consumers" arm is weakly sourced and leans against the consensus on integration databases (flag). Claim certainty: grounded.

## L2 claims

Pinned: records reviewed: 48. Findings `fix`: 16. Findings `flag`: 9. Sources fetched: 9; confirmed 6, partly 3. Full list in `findings.md` (ids R01 to R25).

Clear defects (all `fix`, grounded in the records and the settled J2 text):
- Seams with settled records: BOUNDARY.3 and STATE.1 make the contract the origin of all types, contradicting CONTRACTS.3 (the team records where the chain starts) and restating it in three places (R01, R02); BOUNDARY.5 applies a deprecation window to every interface, while CONTRACTS.1 limits it to many, external or independent consumers (R03); BOUNDARY.5 restates the input and output model split of CONTRACTS.3 (R04); DESIGN.1 calls test-first "the best way" where BEHAVIOUR.5 leaves ordering to context (R09).
- Grounding: PARADIGM.2's set-oriented clause has no row and REG-1143 is silent on it (R16); DESIGN.4 writes a one-engineer heuristic as a rule (R10); STATE.2's Boyce-Codd rejection reason is wrong and REG-1144 lacks Boyce-Codd (R11); BOUNDARY.1's untrusted-check clause is grounded by REG-1503, settling F6 (R12); PROCESS.2's only source is one runtime's page (R13); SYSTEM_SHAPE.1 states a DHH-only criterion its own grounds disclaim and omits Fowler's team-experience condition (R06). Grounded for each (sources fetched or ledger searched).
- Naming: NAMING.1 constraint misses its own exception (R07, settles F8); NAMING.2 repeats NAMING.1 (R08).
- Language mechanisms (check L): "overloads" in BOUNDARY.5 (R05), bundler outcome in STATE.5 (R14), "large identifiers" in STATE.4 (R15). Grounded. The STATE.5 node itself is a flag (R23).

Subtle points for the Opus pass (`flag`):
- Signature over shape-bound (R17, F1): inferred. Not averaging, but nothing outside the maintainer supports it, and the argument is weaker than written.
- Store as contract (R18): inferred. The privilege-separation arm is sound; "several direct consumers" rests on one T3 tool page, against REG-1133.
- Placement of scheduled work, size trigger, team skill (R19, F2); lock-step reading (R20, F3); growth horizon against STANCE.4 (R21, F4); derivation order against deferral (R22); STATE.5 as stack pointer or conditional principle (R23, F5); Boyce-Codd clause (R24, F7); error audience scoping (R25, F9). Open or inferred.

MD-01 triggers: one deployable unit first: grounded, passes (Fowler, REG-1112, T2). Signature: inferred, flag. Store as contract: inferred, flag. No decision averages positions; no decision rests on the most demanding practice. Judge flags: F1, F2, F3, F4, F5, F7, F9 carried; F6 and F8 settled.

## L3 full

Pinned: records reviewed: 48. Findings `fix`: 16. Findings `flag`: 9. Sources fetched: 9; confirmed 6, partly 3.

The full per-finding lines (node, check, severity, error, correction, evidence) are in `findings.md`; each is one line, so they are not repeated here. Reading guide and method:

Method. All 48 records read against the skeleton positions and the MAINT rows (L295, L309, L311, L312, L315, L329, L330), the settled J2 records (CONTRACTS.1 to .3, RULES.3, BEHAVIOUR.5), J3 (DATA_INTEGRITY.1, .4), J1 STANCE.4, and cross_unit_fixes X1 to X3 (none touches CONSTRUCTION). Eight checks plus two: language mechanism (L) and the MD-01 trigger test (M). Grounded.

Sources fetched (9). Confirmed: REG-1118 ("design for ~10X growth, but plan to rewrite before ~100X", a quotation of one engineer); REG-1143 (maintainable first, profile, replace hot spots, team skill, in-memory tests; nothing on set-based or scheduled work); REG-1112 (monolith first; boundaries are hard to move; services-first viable for replacements and with team experience; no "one head" criterion); REG-1507 (undefined state; external monitor to restart); REG-1151 (parse at the boundary; shotgun parsing; no systematic treatment of internal sources); REG-1503 (validate internal APIs, queues and stored records at a trust boundary; allowlist; syntax and semantics; client-side bypassable). Partly: REG-1156 (views and stored procedures in a dedicated schema, backward compatibility, versioning; no conditions of non-need, no signature preference); REG-1144 (3NF, 4NF, "no obligation to fully normalize"; no Boyce-Codd); REG-1133 (integration databases should be avoided; no statement about ownership or acceptable sharing).

Test of the three triggers against MD-01.
- One deployable unit first: the strongest sources (REG-1112, REG-1113) agree, T2; the split triggers are inferred but follow the sources' own reasons; fixes R06 only.
- Interface by signature unless consumers compose reads: the trigger is a property (who composes the read), which is the right kind of condition; the default rests on one position; flag R17.
- Store as contract only for several direct consumers or privilege separation: the property test is right for privilege separation; the consumers arm needs the Opus pass (R18).
Neither contested decision is a compromise between the maintainer and the public view; both are the maintainer's own conditions made explicit, which is correct only if the maintainer's position is the strongest, and that is what the flags ask.

Language neutrality (check L). No finding for HIDING.1 (neutral statement used), STATE.4 (scope kept to types that round, one wording fix), DATA_NOT_CODE and STATE.2 (technology-bound, stated so). Findings R05, R14, R15; node-level flag R23. PROCESS.1 avoids the signal name; PROCESS.2's source is one runtime (R13).

Seams noted by the judge (SERVICES.2 against CONTRACTS.1): agreed to be roles, not a conflict; outside this unit's fixes.

No file other than this folder was written; `judged.md` untouched; nothing committed.
