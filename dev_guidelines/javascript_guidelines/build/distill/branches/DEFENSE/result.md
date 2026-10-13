# Result: step 5b, branch DEFENSE

## L1 headline

All 195 DEFENSE claims are consolidated into 182 ledger rows (0 dropped) under six children cut by what hostile data becomes or attacks (DOM, ORIGIN, INJECTION, PROTOTYPE, SECRETS, HOST), with 4 undecided nodes, 12 contested topics decided by the max rule and 7 restriction demotions; certainty: grounded for the counts and the checker output, inferred for the cut, the graph placement and the choices at contested topics.

Pinned:
- Claims in 195 (SRVSEC 63, DOMSEC 60, RUNSEC 44, FW 16, RUNTIME 5, TYPES 3, ASYNC 2, LANG 2); ledger rows out 182 (13 merged rows hold 26 claims, 169 single rows): every claim placed exactly once, 0 dropped, 0 duplicated, 0 unknown.
- Ledger roles: decision 107, fact 39, rejected 18, acceptable-when 10, deferred 8. Graphs: js-philosophy 25 rows, pig-js-defaults 157 rows.
- Nodes: js-philosophy 21 (L1 1, L2 6, L3 14); pig-js-defaults 58 (L1 1, L2 6, L3 32, L4 19); 39 judge records.
- Decisions for review: 12 contested topics (B1 to B12), 4 convention decisions (A1 to A4) in `decisions.md`.
- Undecided nodes: 4 (`PIG-JS.DEFENSE.DOM.2.3`, `.INJECTION.4.4`, `.INJECTION.5.3`, `.INJECTION.6.4`).
- Restriction demotions: 7 overstepping claims (DOMSEC-C07, C14, C21, C28, RUNSEC-C11, SRVSEC-C11, SRVSEC-C13) and 12 vendor-document claims held at fact (FW-C01, C03, C05, C06, C08, C09, C10, C11, C12, C18, C19, C20).
- Checker: `python3 build/distill/check_ledger.py DEFENSE` reports claims in 195, placed 195, missing 0, duplicated 0, unknown 0.

## L2 claims

- Grounded: the branch holds 195 claims (slot 05: 60, slot 06: 44, slot 13: 63, slot 10 frameworks: 16, slot 09: 5, slot 02: 3, slot 03: 2, slot 01: 2); `claims.md` has 195 rows and the checker places all 195.
- Inferred: the cut by what hostile data becomes (A1 in `decisions.md`) serves safety better than browser versus server, because five of six classes cross that line; claims per child: INJECTION 61, DOM 48, ORIGIN 27, SECRETS 23, HOST 22, PROTOTYPE 14. INJECTION is the heaviest (31 percent) and is itself cut into six classes at L3.
- Inferred: graph placement follows the extraction level, with facts and API-specific rules in the defaults graph (A2); 25 philosophy rows against 157 defaults rows.
- Grounded: every folklore belief that `12_dissent` refutes and that falls in DEFENSE has a `rejected` row (12 refuted beliefs: DOMSEC-C10, C13, C16, C28, C42, C48, RUNSEC-C01, C08, C16, C22, C27, C32), plus the restricted JSON.parse belief (RUNSEC-C13), two position rejections (SRVSEC-C19, C41) and three slot-13 tags `12_dissent` never audited (SRVSEC-C01, C04, C23; inferred).
- Grounded: the 9 claims routed with `boundary: web-architecture` are held outside the guideline (8 `deferred` rows, DOMSEC-C28 kept as a rejected-belief row) and listed as planned boundary links; DOMSEC-C15 and FW-C48 are merged into one decision whose code half stays here.
- Grounded: five claims state a gap, not a practice: SRVSEC-C14, C37, C44, C55 and DOMSEC-C57 (inferred rule); they are `fact` rows on a node (or the open note on `SECRETS.4`) and four of them head undecided nodes.
- Grounded: 13 merges (26 claims) remove duplicated statements across slots: ReDoS input bounds, eval from strings and string timers, Trusted Types enforcement, escape hatches, inspector exposure, secure random, TOCTOU, dangerous-functionality documentation, serialization integrity, event-loop regex risk, parser-resource limits (see L3).
- Inferred: contested decisions by max rule: named Trusted Types policies, event-handler attributes never from untrusted data, explicit `rel=noopener noreferrer`, permission model as seat belt only, allowlist mapping for SQL identifiers, native `setHTML` first, lockdown of built-ins only where tested.
- Grounded: seven demotions for overstepping restrictions and twelve vendor-fact holds (L1 pinned; reasons in `decisions.md` Part C).
- Open: four undecided nodes (URL validation by parsing, Node path containment recipe, `v8.deserialize` and structured clone safety for untrusted input, Node `fetch` redirect semantics); also open: current Node crypto documentation (SRVSEC-C14), the verbatim MDN condition for `setAttribute` (DOMSEC-C25), current status of V8's non-backtracking engine (RUNSEC-C33).
- Inferred: 39 judge records, one per defaults node holding a decision plus `INJECTION.1.2`, whose decision is stated as a rejection.
- Grounded: no absolute or home paths, no private names in the four files; nothing committed, nothing pushed.

## L3 full

### Method

1. Read the brief (Shared and 5b), `target_hierarchy.md`, `build/plan.md` (goal, boundary, admission policy, claim format, target graphs, maintainer decisions), the three IntentGraph primers (P2, P4, P5, UID rules, node-name safety) and the Python philosophy graph uids.
2. Read all 195 rows of `claims.md` in full; the folklore audit and the topic sections of `12_dissent` that touch DEFENSE; the `11_coverage` overlaps (O05, O06, O11, O12, O14 to O16, O18), boundary list and gap rows G-H1 to G-H5; the 124 register rows for the sources the claims cite, checking each claim against the row's restriction.
3. Designed the cut, assigned each claim a node and a role, merged duplicates, wrote the rows, nodes, links and judge records as data, generated `ledger.md` and `skeleton.md` from it, wrote `decisions.md`, ran `check_ledger.py DEFENSE` (exit 0).

### Cut and counts per child

| child | what hostile data becomes or attacks | L3 children in defaults | claims |
|---|---|---|---|
| DOM | live markup, script, navigation in the page | markup sinks, URL sinks, sanitizing, Trusted Types, clobbering, framework escape hatches | 48 |
| ORIGIN | what crosses origins | messages, frames, third-party code and service workers, web storage, CSP-ready code | 27 |
| INJECTION | instruction or location outside the page | code from strings and vm, OS commands, SQL and NoSQL, paths and archives, deserialization, outbound requests | 61 |
| PROTOTYPE | keys that rewrite the object model | key writes and reads, dictionaries, hardening | 14 |
| SECRETS | randomness, crypto, secrets, leakage | randomness, crypto API, passwords, constant-time, secret handling, leakage | 23 |
| HOST | the Node process under hostile input | permission model, inspector, HTTP parsing, regex cost, parser limits, module load path | 22 |

Philosophy graph: DOM has 3 children (sources and sinks, a verdict holds only for its parse, script tags are not the only way in), INJECTION 6 (one per class), PROTOTYPE 2, HOST 3; ORIGIN and SECRETS stay leaves at L2 (one principle each: DOMSEC-C41 and RUNSEC-C46), which is a coarser view by design.

### Merges (claim ids sharing one row)

RUNSEC-C44 with SRVSEC-C45 (sign and populate a new object); ASYNC-C40 with RUNSEC-C36 (regex blocks the thread); DOMSEC-C15 with FW-C48 (enforce Trusted Types); DOMSEC-C55 with FW-C02 (escape hatches); RUNSEC-C45 with SRVSEC-C46 (document dangerous functionality); DOMSEC-C03 with ASYNC-C33 (no code from strings, timers); SRVSEC-C16 with C20 (driver parameter channel); SRVSEC-C24 with C27 (MongoDB operator control); RUNTIME-C18 with SRVSEC-C53 (no access-then-open); RUNSEC-C13 with TYPES-C50 (parsed `__proto__`); SRVSEC-C02 with C03 (CSPRNG calls); RUNTIME-C51 with SRVSEC-C40 (inspector); RUNSEC-C30 with TYPES-C32 (bound regex input).

### Overlaps with other branches (not merged here, linked)

SUBSET holds the own-property test (LANG-C55) and shallow freeze (LANG-C38); STRUCTURE holds exported mutable state (STRUCT-C01 to C03); DEPENDENCIES holds RUNSEC-C41 (no in-process isolation), SUPPLY-C01 and the framework choice evidence; VERIFICATION holds the lint rule set and secret detection gates; CONTRACTS holds boundary parsing; CONTROL holds event-loop blocking; RUNTIME holds Buffer speed. Proposed links are in `skeleton.md` (15 cross-branch proposals, 16 intra-defaults links, 4 intra-philosophy links, 26 inter links to philosophy, 2 inter links to `python-kb-philosophy:DEFENSIVE`), plus 5 planned boundary links to web_architecture.

### Judgement calls to check first

- Graph placement of API-specific `js-principle` claims (A2); a different rule moves roughly twenty rows between graphs without changing any decision.
- DOMSEC-C35 deferred while its code-level mechanism (DOMSEC-C36) stays here (A4).
- SRVSEC-C16, C20 and C47 kept as decisions although their sources are vendor documentation admitted for facts: they render a rule already set by OWASP principles and prefer no product.
- INJECTION holds 31 percent of the claims; the integrator may split it into two L2 nodes (code and commands against data stores, paths and destinations) without moving any row.

### Files

All under `build/distill/branches/DEFENSE/`: `ledger.md` (182 rows), `skeleton.md` (79 nodes, links, judge records), `decisions.md` (A1 to A4, B1 to B12, demotions, single-source list, undecided table), `result.md` (this file).
