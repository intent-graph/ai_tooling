# CONTRACTS branch result (step 5b)

## L1 headline

CONTRACTS is consolidated into 47 nodes (10 philosophy, 37 defaults) with all 52 routed claims placed once in 52 ledger rows, deciding TypeScript with strict checking as the type layer and leaving no node undecided; certainty: grounded for placement and counts (checker run), inferred for the type-layer preference, which rests on T1 mechanism facts plus one T2 holder.

Pinned: claims in 52, ledger rows out 52 (0 dropped: 50 claim rows holding 52 ids, two rows each merging a pair of claims, plus 2 folklore rows with claim_ids `-`); nodes js-philosophy 10 (L1 1, L2 3, L3 6), pig-js-defaults 37 (L1 1, L2 6, L3 30); roles decision 37, fact 11, rejected 3, deferred 1; undecided 0 (the former three, MODEL.4 type predicates, MODEL.5 object type declaration, BOUNDARY.5 schema library, are decided, each flagged weak); restriction demotions 8 (listed in L2); type layer TypeScript, `known | conflict: JSDoc-checked JavaScript, none`; checker output: `claims in: 52; placed: 52; missing 0; duplicated 0; unknown 0`.

## L2 claims

Placement (grounded, checker run: `python3 build/distill/check_ledger.py CONTRACTS`):
- 52 claims in, all placed once; 0 missing, 0 duplicated, 0 unknown. 52 rows: 10 js-philosophy, 42 pig-js-defaults. Roles: decision 37, fact 11, rejected 3, deferred 1.
- Merged: RUNSEC-C06 and TYPES-C30 (same group, one schema rule) in CONTRACTS-047; TYPES-C36 and TYPES-C37 (schemas that infer the static type) in CONTRACTS-050. Folklore rows CONTRACTS-002 and CONTRACTS-018 carry claim_ids `-` so TYPES-C02 and TYPES-C03 are counted once (integrator may prefer merging each pair).

Tree (grounded):
- js-philosophy: CONTRACTS with STATIC (2 children: types attest nothing at run time; a passing check is evidence, not proof), BOUNDARY (4: validate at every trust boundary, positive rule, meaning as well as form, recognizer) and SHAPE (leaf: calls carry meaning by name).
- pig-js-defaults: PIG-JS.CONTRACTS with LAYER (6), STRICT (4), ESCAPE (6), MODEL (5), SIGNATURE (4), BOUNDARY (5).
- Links: 3 intra and 3 inter-to-python-kb in philosophy, 12 intra and 7 inter-to-philosophy in defaults, 19 proposed cross-branch links (SUBSET, STRUCTURE, CONTROL, DEFENSE, DEPENDENCIES, VERIFICATION, plus one planned web-architecture boundary link).

Decisions for review (details in `decisions.md`):
- D1 type layer TypeScript (inferred preference; grounded mechanism): rejected JSDoc-checked JavaScript (wins with no compile or type-check step; kept as fallback LAYER.2) and none (no admitted holder; wins on no evidence).
- D2 noUncheckedIndexedAccess and exactOptionalPropertyTypes enabled on a mechanism-only ground (inferred; no source mandates them).
- D3 suppression directives banned on one T2 holder, with a slot-asymmetric restriction on the same position (inferred risk; may become undecided).
- D4 options object, D5 pinned compiler, D6 optional chaining only on nullable types: each inferred from T1 rationale plus at most one T2 position.
- D11 the three former undecided nodes, each decided with a judge record.
- D3 scoping: SRC-244 is unrestricted for the quality slot, so QUALITY-C18 grounds the rule; kept.
- D7 erasable-syntax-only kept conditional on Node type stripping; widening is open.

Undecided nodes: none. Former undecided nodes decided on the coordinator's instruction (max rule, a missing ranking is no reason to abstain), all flagged weak (D11): MODEL.4 type predicates held to assertion standard (inferred; no admitted source says the compiler skips the body, searched handbook and typescript-eslint pages); MODEL.5 interface for object types (one T2 position plus the handbook extension fact); BOUNDARY.5 class-level rule that the schema infers the static type, no library named (vendor facts only).

Restriction demotions (grounded against `audit/source_register.md`):
- TYPES-C26 (SRC-244, position only): not demoted; used as a position to choose among positions, flagged single T2.
- TYPES-C25 (SRC-244, position only in the types slot): decision to fact; QUALITY-C18 carries the decision (SRC-244 unrestricted for the quality slot).
- TYPES-C35, C38 (Ajv, Standard Schema; facts only): practice or decision to fact. TYPES-C36, C37 (Zod, Valibot): decision only at the class level (schema infers the type), no library preferred.
- TYPES-C42 (SRC-034, SRC-036, SRC-044 vendor facts): practice to fact; "avoid" is inferred.
- TYPES-C43 (SRC-033, SRC-034): practice to fact; "list explicitly" is inferred.
- TYPES-C46 (SRC-243, SRC-042): status only; "do not plan on it" is inferred, never a forecast.
- RUNSEC-C42: SRC-053 ground dropped (its 06_runsec scope covers regex safety only); the claim stands on SRC-140 and SRC-135.
- STRUCT-C47: the rule default of 3 not recorded (SRC-084 restriction).
- STRUCT-C48 to C52: SRC-261 and SRC-093 positions kept as positions, scoped to declared APIs; transfer to application APIs is inference.

Open (grounded as gaps): no admitted source on whether the compiler verifies type predicate bodies; none on overloads whose return type depends on the argument type; none comparing schema libraries independently; type layer "none" has no holder (G-M05 of `11_coverage`).

## L3 full

Files in this folder: `claims.md` (input, 52 rows), `ledger.md` (52 rows), `skeleton.md` (both node tables, intentlinks, proposed cross-branch links, inter links, 30 judge records), `decisions.md` (D1 to D10 and the undecided nodes).

Reading done: the brief sections Shared and Step 5b; `build/plan.md` (goal, boundary, admission policy, claim format, target graphs, maintainer decisions); `build/distill/target_hierarchy.md`; the CONTRACTS claims; `12_dissent` (Topic 4, folklore table, Q1, the checked-not-a-tension note on TYPES-C25 and QUALITY-C18); `11_coverage` (boundary tables, gaps G-M05 and G-M06, flags on TYPES-C29 and STRUCT-C50 to C54); the register rows of the 37 cited sources; the IntentGraph primers 00 and 01 (and 03A for editing rules); the python-kb-philosophy uids (ROOT, INTENTIONALITY, STRUCTURE, ROUGHTOFINE, DATACENTRICITY, COMMUNICATION, REPRODUCIBILITY, POLYGLOT, DEFENSIVE). ECMA-262 and the HTML standard are not used by this branch.

Partition logic (inferred): the L2 split of the defaults follows what the purpose "checkability" needs in order: which checker and how it runs (LAYER), how hard it checks (STRICT), where it is bypassed (ESCAPE), how data is modelled so it proves more (MODEL), how call shapes are declared (SIGNATURE), and how run-time data earns its type (BOUNDARY). Six children, within the two to six bound. The philosophy side holds only the language-neutral boundary and shape principles and the two JavaScript-distinct facts (no run-time types; unsound and partial checker).

Cross-branch notes for the integrator:
- Overlaps to merge under P5: RUNSEC-C06, RUNSEC-C42 and TYPES-C34 (validation allowlists) with DEFENSE; QUALITY-C18 and TYPES-C25 are one position (merged here on ESCAPE.6); TYPES-C32 (ReDoS) is routed elsewhere.
- Possible untagged boundary: STRUCT-C50 to C52 are TypeScript signature shapes, not HTTP API contracts, so no web-architecture link is proposed; `11_coverage` flagged them as a candidate.
- Naming: node names avoid the forbidden characters; JSON.parse in a name contains a dot only.
- Public repository: the files contain no absolute or home paths and no private names. Nothing was committed or pushed; only this folder was written.
