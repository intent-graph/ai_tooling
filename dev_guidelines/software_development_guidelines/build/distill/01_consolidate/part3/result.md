# Part 3 of the claims ledger: language-general principles sent by the JavaScript guideline

## L1 headline

The JavaScript guideline's package of language-general principles (65 sent nodes: 56 sent whole, 9 general parts) is imported as a separate part 3 of the claims ledger: 65 rows in which each principle is stated so that it holds for every language, the JavaScript mechanisms and examples are dropped and listed per row, the origin's rejected and contested positions are kept, and every row is marked `origin: judged in the JavaScript guideline` so that the judge here re-examines it. Nothing is judged, owned or dropped silently. Certainty: grounded for the counts and the id and source coverage (a script reads the package, the JavaScript research results and register, and part 1, and proves them); inferred for the language-neutral wording of each statement and for the same-versus-adjacent reading of the links to part 1 (my reading).

Pinned:
- Nodes in: 65 sent nodes of the JavaScript guideline's package (Part A 56 sent whole, Part B 9 general parts of nodes that stay narrowed).
- Rows out: 65 ledger rows, L1501 to L1565, one per node. Not imported: 0 nodes (no sent node lacks a language-neutral form; 5 borderline nodes are imported with their condition stated).
- Claim ids in the rows: 72, each in exactly one row (70 carried in the package's claim tables, 2 named by the origin's epistemic state for CONTROL.LIFECYCLE: ASYNC-C05, RUNTIME-C37). Dropped: 0.
- See also to part 1: 41 rows carry at least one reference, 76 references in all (20 marked same, 56 marked adjacent); part 1 is untouched.
- Sources: 79 new rows REG-1501 to REG-1579; 7 JavaScript-register sources reused from part 1 (REG-001, REG-003, REG-048, REG-049, REG-114, REG-166, REG-184).
- Script: `PASS: every sent node of the package (Part A and Part B) is a row or listed as not imported exactly once, every claim is in one row, every cited source resolves`

## L2 claims

Pinned:
- Nodes in: 65 sent nodes of the JavaScript guideline's package (Part A 56 sent whole, Part B 9 general parts of nodes that stay narrowed).
- Rows out: 65 ledger rows, L1501 to L1565, one per node. Not imported: 0 nodes (no sent node lacks a language-neutral form; 5 borderline nodes are imported with their condition stated).
- Claim ids in the rows: 72, each in exactly one row (70 carried in the package's claim tables, 2 named by the origin's epistemic state for CONTROL.LIFECYCLE: ASYNC-C05, RUNTIME-C37). Dropped: 0.
- See also to part 1: 41 rows carry at least one reference, 76 references in all (20 marked same, 56 marked adjacent); part 1 is untouched.
- Sources: 79 new rows REG-1501 to REG-1579; 7 JavaScript-register sources reused from part 1 (REG-001, REG-003, REG-048, REG-049, REG-114, REG-166, REG-184).
- Script: `PASS: every sent node of the package (Part A and Part B) is a row or listed as not imported exactly once, every claim is in one row, every cited source resolves`

Each line carries its certainty: grounded (I can name the file or the script run that makes it true), inferred (my reading), open (not determined).

### Claims of this import

- Every one of the 65 sent nodes of the package (Part A and Part B) is the `JS:` uid of exactly one row; the "Not imported" list is empty, and no uid is in both. (grounded: script run, output in L3)
- Every claim id of the package's claim tables (70) is in exactly one row, and every claim id in a row (72) is defined in the JavaScript research results; every JavaScript source those claims cite has a register row (79 new, 7 reused from part 1), carries the same url as the JavaScript source register, and appears in the row's `sources`. (grounded: script run)
- Every row states the node's general intent in language-neutral form and lists, in its `positions`, the JavaScript-specific fragments it dropped (38 rows have such a list; the others had none to drop). That each statement really holds for every language is my reading of the origin's intent and constraints; the judge here is asked to re-examine it. (grounded for the lists, inferred for the neutrality)
- Rejected alternatives and contested points are kept with the origin's wording, and where the origin states no condition under which the alternative would be best, the row says so: SUBSET.NUMBERS (fixed tolerance), CONTRACTS.BOUNDARY.2 (denylisting), STRUCTURE.DIRECTION.1 (cycles are a supported mechanism), STRUCTURE.PARADIGM (defect-rate studies contested), DEFENSE.INJECTION.3 (escaping as primary defence; non-SQL stores immune), VERIFICATION.TEST_SUITE.2 (coverage; the OpenSSF branch-coverage suggestion wins for a project adopting those criteria), RUNTIME.MEASURE (mechanism-only restructuring). STRUCTURE.DIRECTION.2 (declared layering) stays undecided and open. (grounded: read from the package)
- Two rows state more in their intent than their claims ground, so the row marks that part open: DEFENSE.INJECTION.4 (checked after resolution and used without a race) and DEFENSE.SECRETS (audited primitives for drawing, comparing, storing and logging). Two more carry an open part: SUBSET.STATE (no preference derived) and DEPENDENCIES.CHANGE.4 (cooldown effectiveness unmeasured). (grounded: I compared intent and claims)
- Row certainty over 65 rows: grounded 39, inferred 25, open 1 by the first word of the certainty cell; rows with a mixed cell are counted by their first word and state the split in the cell. Parent rows (no claim of their own) are inferred, because a rolled-up claim has its own certainty. (grounded: counted)
- CONTROL.LIFECYCLE has no claim table in the package: its origin cites a merged row of the JavaScript rule graph that absorbs ASYNC-C05 and RUNTIME-C37; both are read from the JavaScript research results (single-source, one Node.js documentation page, text names Node hooks) and listed in `merges`. (grounded)
- Part 1 has no row on module structure, naming, hiding, state in one place, the injection classes, secrets in code, or the measurement method as such; its nearest rows are the maintainer's L309 and L312, and rows on dependency admission, updates, test design, flakiness, coverage and mutation, which overlap several verification and dependency nodes. 41 rows carry `see also`; "same" means the part 1 row states the same thing, "adjacent" a neighbouring point; none is merged. (grounded for the references, inferred for the same-versus-adjacent split; the absence of other overlaps is by my reading of all 460 part 1 statements)
- The JavaScript guideline restored four of the sent nodes with a JavaScript emphasis (SUBSET.NUMBERS, SUBSET.STATE, CONTRACTS.BOUNDARY, and DEFENSE.INJECTION.1 as DEFENSE.CODE); under the maintainer's rule the general statement belongs here, so the four are imported, and two claims it re-placed there (RUNSEC-C14, SECGAP2-C31) stay in row L1529. (grounded: read from the package's companion file)
- Two sources are in part 1's register at a different tier than in the JavaScript register (the two chapters of one engineering book, T3 there and T2 here); the row cites the part 1 id and says so. One reused id (REG-184) is scoped in part 1 to a different section of the same document. (grounded)

### Not done

- No judgement, owner, hierarchy position or merge into part 1; no node of the target hierarchy was assigned. (grounded: by construction)
- Source urls were not re-read and claims were not re-checked against their sources: tier, verdict, restriction and certainty are as audited and recorded in the JavaScript guideline. (open: not spot-checked)
- Wording of the 65 statements is mine; it compresses each node's intent and constraints, and a statement may have lost a nuance the origin kept in a constraint. (open: no second reader; the review step in the maintainer's decisions is the place for it)
- The target hierarchy has no node yet for some imported topics (for example publishing a package as a supplier); the rows are not placed. (grounded: stated in the inputs file)

## L3 full

Pinned:
- Nodes in: 65 sent nodes of the JavaScript guideline's package (Part A 56 sent whole, Part B 9 general parts of nodes that stay narrowed).
- Rows out: 65 ledger rows, L1501 to L1565, one per node. Not imported: 0 nodes (no sent node lacks a language-neutral form; 5 borderline nodes are imported with their condition stated).
- Claim ids in the rows: 72, each in exactly one row (70 carried in the package's claim tables, 2 named by the origin's epistemic state for CONTROL.LIFECYCLE: ASYNC-C05, RUNTIME-C37). Dropped: 0.
- See also to part 1: 41 rows carry at least one reference, 76 references in all (20 marked same, 56 marked adjacent); part 1 is untouched.
- Sources: 79 new rows REG-1501 to REG-1579; 7 JavaScript-register sources reused from part 1 (REG-001, REG-003, REG-048, REG-049, REG-114, REG-166, REG-184).
- Script: `PASS: every sent node of the package (Part A and Part B) is a row or listed as not imported exactly once, every claim is in one row, every cited source resolves`

### Files

- `claims_ledger_part3.md`: the 65 rows (columns as part 1: id, statement, merges, areas, level, stack, agreement, positions, certainty, sources), the "Not imported" section (empty, with the borderline cases), and the row rule.
- `sources_part3.md`: 79 new sources REG-1501 to REG-1579 (JavaScript register id in `replaces` as `JS-SRC-nnn`), and a table of the 7 reused part 1 ids.
- `check_part3.py`: the proof script; it reads the package, the JavaScript research results and register, and part 1 read-only, and writes nothing.
- Origin of everything: the JavaScript guideline's package (`../../../../../javascript_guidelines/build/handoff/to_software_guideline/package.md`), its research results and its source register.

### Script run

```
package nodes: 65 (Part A 56, Part B 9); rows: 65; not imported: 0
nodes in a row: 65; unknown node uids: 0
claims in package tables: 70; claim ids in rows: 72 (2 named by the origin, not in a package table); in more than one row: 0; dropped: 0; undefined in research results: 0
sources: 79 new, 7 reused from part 1; package sources resolved: 82; claim-source citations checked: 109
see also references to part 1: 76
PASS: every sent node of the package (Part A and Part B) is a row or listed as not imported exactly once, every claim is in one row, every cited source resolves
```

### Nodes in, rows out

Row ids in order of the package's outline (branch, with the Part B general part first where a branch has one). Part B rows are the general parts of nodes that stay narrowed in the JavaScript guideline.

| row | node | part | name in the package | claims carried |
|---|---|---|---|---|
| L1501 | JS:SUBSET.NUMBERS | A | Stated numeric limits | LANG-C29 |
| L1502 | JS:SUBSET.STATE | A | Distinguished immutability | STRUCT-C66 |
| L1503 | JS:CONTRACTS | B | Contracts | - |
| L1504 | JS:CONTRACTS.BOUNDARY | A | Boundary contract | - |
| L1505 | JS:CONTRACTS.BOUNDARY.1 | A | Validate at every trust boundary | TYPES-C27, TYPES-C29 |
| L1506 | JS:CONTRACTS.BOUNDARY.2 | A | Accept by positive rule | TYPES-C28 |
| L1507 | JS:CONTRACTS.BOUNDARY.3 | A | Check meaning as well as form | TYPES-C33 |
| L1508 | JS:CONTRACTS.BOUNDARY.4 | A | Input handling is a recognizer | TYPES-C48 |
| L1509 | JS:CONTRACTS.SHAPE | A | Shape of calls | STRUCT-C47 |
| L1510 | JS:CONTROL.LIFECYCLE | A | Process end is designed | - |
| L1511 | JS:STRUCTURE | B | Structure for locality of change | - |
| L1512 | JS:STRUCTURE.HIDING | A | Hide likely-to-change decisions | - |
| L1513 | JS:STRUCTURE.HIDING.1 | A | Decompose by hidden decisions | STRUCT-C58 |
| L1514 | JS:STRUCTURE.HIDING.2 | A | Abstract data type versus object | STRUCT-C62 |
| L1515 | JS:STRUCTURE.HIDING.3 | A | Minimal public surface | STRUCT-C59 |
| L1516 | JS:STRUCTURE.STATE | B | State in one place | - |
| L1517 | JS:STRUCTURE.STATE.1 | A | One place per piece of state | STRUCT-C65 |
| L1518 | JS:STRUCTURE.PURITY | A | Effect-free importing | STRUCT-C06 |
| L1519 | JS:STRUCTURE.DIRECTION | A | Dependencies flow one way | - |
| L1520 | JS:STRUCTURE.DIRECTION.1 | A | No cycles between modules | - |
| L1521 | JS:STRUCTURE.DIRECTION.2 | A | Declared layering | STRUCT-C60 |
| L1522 | JS:STRUCTURE.NAMING | A | Names carry the concept | - |
| L1523 | JS:STRUCTURE.NAMING.1 | A | Whole words | STRUCT-C55 |
| L1524 | JS:STRUCTURE.NAMING.2 | A | One concept one word | STRUCT-C56 |
| L1525 | JS:STRUCTURE.NAMING.3 | A | Name from the concept | STRUCT-C57 |
| L1526 | JS:STRUCTURE.PARADIGM | A | Paradigm by intent | STRUCT-C64, STRUCT-C63 |
| L1527 | JS:DEFENSE | B | Defense | - |
| L1528 | JS:DEFENSE.INJECTION | A | Data becoming instruction or location | - |
| L1529 | JS:DEFENSE.INJECTION.1 | A | Strings never become code | RUNSEC-C14, SECGAP2-C31 |
| L1530 | JS:DEFENSE.INJECTION.2 | A | Commands are not built from input | RUNSEC-C25, RUNSEC-C26 |
| L1531 | JS:DEFENSE.INJECTION.3 | A | Queries keep code and data apart | SRVSEC-C15, SRVSEC-C17, SRVSEC-C19, SRVSEC-C22, SRVSEC-C23 |
| L1532 | JS:DEFENSE.INJECTION.4 | A | Paths stay inside their base | RUNSEC-C28, SECGAP2-C81 |
| L1533 | JS:DEFENSE.INJECTION.5 | A | Serialized data carries no behaviour | RUNSEC-C43, RUNSEC-C44, SRVSEC-C45, SECGAP2-C18 |
| L1534 | JS:DEFENSE.INJECTION.6 | A | Destinations are chosen by the server | SRVSEC-C28, SRVSEC-C30, SRVSEC-C32 |
| L1535 | JS:DEFENSE.SECRETS | A | Secrets and cryptographic primitives | RUNSEC-C46, SECGAP2-C03 |
| L1536 | JS:DEFENSE.HOST.3 | B | Two parsers must agree | SECGAP2-C23 |
| L1537 | JS:DEPENDENCIES | B | Dependencies | - |
| L1538 | JS:DEPENDENCIES.TRUST.3 | A | Layered controls | SUPPLY-C32 |
| L1539 | JS:DEPENDENCIES.ADMISSION | B | Admission | - |
| L1540 | JS:DEPENDENCIES.ADMISSION.1 | A | Existing components first | SUPPLY-C27 |
| L1541 | JS:DEPENDENCIES.ADMISSION.3 | A | Identity of the package | SUPPLY-C24 |
| L1542 | JS:DEPENDENCIES.ADMISSION.4 | A | Documentation examples are untrusted | SUPPLY-C39 |
| L1543 | JS:DEPENDENCIES.CHANGE.4 | A | Updates | SUPPLY-C36, SUPPLY-C13, QUALITY-C46 |
| L1544 | JS:DEPENDENCIES.CHANGE.5 | A | Incident response | SUPPLY-C41 |
| L1545 | JS:DEPENDENCIES.PUBLISH | A | Publishing | SUPPLY-C17 |
| L1546 | JS:VERIFICATION | B | Verification | - |
| L1547 | JS:VERIFICATION.STATIC_BASELINE | A | Static analysis baseline | - |
| L1548 | JS:VERIFICATION.STATIC_BASELINE.1 | A | Analysis switched on | QUALITY-C20 |
| L1549 | JS:VERIFICATION.STATIC_BASELINE.2 | A | Analysis beyond the compiler | QUALITY-C21 |
| L1550 | JS:VERIFICATION.STATIC_BASELINE.3 | A | Checks complement each other | LANG-C56, QUALITY-C23 |
| L1551 | JS:VERIFICATION.TEST_SUITE | A | Test suite | - |
| L1552 | JS:VERIFICATION.TEST_SUITE.1 | A | Tests for new functionality | QUALITY-C22 |
| L1553 | JS:VERIFICATION.TEST_SUITE.2 | A | Coverage finds, it does not judge | QUALITY-C36 |
| L1554 | JS:VERIFICATION.TEST_SUITE.3 | A | Test design | QUALITY-C29, QUALITY-C30, QUALITY-C31 |
| L1555 | JS:VERIFICATION.FAULT_DETECTION | A | Fault detection power | - |
| L1556 | JS:VERIFICATION.FAULT_DETECTION.1 | A | Mutation testing | QUALITY-C37, QUALITY-C38 |
| L1557 | JS:VERIFICATION.FAULT_DETECTION.2 | A | Property-based testing | QUALITY-C39, QUALITY-C40, QUALITY-C41 |
| L1558 | JS:VERIFICATION.TEST_STABILITY | A | Test stability | - |
| L1559 | JS:VERIFICATION.TEST_STABILITY.1 | A | New tests are probed | QUALITY-C33 |
| L1560 | JS:VERIFICATION.TEST_STABILITY.2 | A | Shared state is cleaned | QUALITY-C35 |
| L1561 | JS:VERIFICATION.TEST_STABILITY.3 | A | Flake rate tracked | QUALITY-C32 |
| L1562 | JS:VERIFICATION.ENFORCEMENT | A | Enforcement at the merge | QUALITY-C43 |
| L1563 | JS:RUNTIME | B | Runtime behaviour | - |
| L1564 | JS:RUNTIME.MEASURE | A | Measurement before belief | RUNTIME-C63 |
| L1565 | JS:RUNTIME.METHOD | A | Measurement method | RUNTIME-C61, RUNTIME-C62 |

### Not imported, with reasons

None. Reasons the borderline nodes were imported (each row states the condition):
- JS:SUBSET.NUMBERS (L1501): the limits of one numeric type are JavaScript's; the principle (limits decide what travels in the type; no ad-hoc tolerance) holds for any language with binary floating point.
- JS:STRUCTURE.PURITY (L1518): holds for any language that runs module code at load time.
- JS:DEFENSE.HOST.3 (L1536): protocol-level (HTTP), language-neutral.
- JS:STRUCTURE.DIRECTION.2 (L1521): language-neutral but undecided in the origin; imported as open.
- JS:CONTROL.LIFECYCLE (L1510): language-neutral; grounded by two claims the package names but does not carry.

### Decisions I took (for the reviewer)

- One row per sent node, parents included (65), because the proof requires every node uid to be a row or listed, and a parent's intent is a rolled-up claim with its own certainty. Rows sit in the order of the package's outline, grouped by origin branch.
- The statement of a row is the origin's intent narrowed to its language-neutral form; where the origin's constraints carry the rule (for example the thresholds of a study), the figures stay as evidence in the statement or positions, because they are not JavaScript-specific. Tool names, API names, ecosystem facts and example attacks are dropped and listed.
- Origin links between two sent nodes are kept as row ids in `positions`; links to nodes that stay in the JavaScript guideline are named as such. The Python-guideline links are kept as "shared with the Python guideline".
- The sibling web-architecture deferral on CONTRACTS.BOUNDARY.1 (TYPES-C29) travels with its row unjudged.
- A `see also` is added only where I read a part 1 row; "same" is used sparingly (20 references), "adjacent" for neighbours.
- REG ids: a JavaScript source is reused from part 1 only when it is the same document at the same url (7); everything else is new and keeps the JavaScript register's tier, verdict and restriction.
