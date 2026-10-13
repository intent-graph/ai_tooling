# Decisions: branch STRUCTURE

Purpose of the branch: locality of change. Max rule: the most demanding practice that serves that
purpose and that an admitted source supports. Restricted style-guide positions decide a node only as
the holder's position and are never counted as evidence. Ledger row ids refer to `ledger.md`.

## Decisions that settled a contested topic

### D1. Module cycles: forbid (PIG-JS.STRUCTURE.DIRECTION.1; STRUCTURE-040, STRUCTURE-041)
- Decision: create no import cycle between modules, in ESM or CommonJS. Status `known | conflict | unvalidated`.
- Rejected, tolerate cycles (Node CommonJS docs, SRC-089: documented as a supported mechanism through partial exports, no recommendation). Wins where a cycle is deliberate in CommonJS legacy code with no observed fault, or where the detection cost exceeds the benefit.
- Rejected, folklore "cyclic imports always crash" (row 041): refuted by SRC-029 and SRC-089; it is a different question from whether to forbid.
- Grounds: MDN advice (SRC-029, via LANG-C64 in slot 01 where the register row is unrestricted; in slot 04 the same sentence is restricted to a position), Google JS position (SRC-239), plugin maintainers' position (SRC-313, never evidence). The mechanism (a cycle fails only when a binding is used before it is initialised) is T1 but only shows that correctness can depend on evaluation order. No admitted source measures a defect cost.
- Review point: the decision is the demanding one for locality; its evidence is thin. Alternative is to demote it to `acceptable-when: tolerate`.

### D2. Top-level await: entry points only (PIG-JS.STRUCTURE.LOADING.4; STRUCTURE-027, STRUCTURE-028)
- Decision: use it only in application entry points, never in a module that others import or that may be require()d.
- Rejected, allowed anywhere (champions Borins and Startsev in the TC39 record: education suffices, deadlocks already exist). Wins if a measurement shows the hazard negligible, or in scripts nothing imports.
- Grounds: T1 mechanism (SRC-092, SRC-030, SRC-029): every importer waits, a never-resolving await ends Node with status 13, require() of the graph fails with ERR_REQUIRE_ASYNC_MODULE. The scope "entry points" is inferred from that mechanism (a leaf change turns every ancestor asynchronous). No source measures the hazard.

### D3. Default versus named exports: named only (PIG-JS.STRUCTURE.SURFACE.1; STRUCTURE-032)
- Decision: named exports in all code.
- Rejected, default for single-export modules (Airbnb, SRC-312): wins when a framework or tool mandates a default export. Acceptable-when: interoperating with CommonJS or AMD consumers (the purpose MDN names, SRC-029, neutral).
- Grounds: holder position of Google JS and Google TS (one holder, so one position); the guides' reason (a default has no canonical name, so rename refactors cannot find uses) is their own. The mechanism that importers choose their own name is language fact.

### D4. Paradigm and defects: no paradigm mandate (STRUCTURE.PARADIGM; STRUCTURE-011, STRUCTURE-012)
- Decision: choose per problem by intent; no source supports an object-oriented or functional rule inside JavaScript on defect evidence.
- Rejected, "functional lowers defects" (Ray et al. 2014, SRC-251, restricted). Wins only if a study scoped to JavaScript paradigms shows an effect; the three papers compare languages on one GitHub dataset, with a dispute over the analysis (SRC-258, SRC-314).
- Grounds: the absence of scoped evidence, inferred (C64). The restriction on SRC-251, SRC-258 forbids using them as a ground for a paradigm choice, so they are used only to show that none exists.

## Weighty choices and single-source decisions

### D5. Barrel files: aggregate only at a public entry point (PIG-JS.STRUCTURE.LOADING.6; STRUCTURE-031)
- Decision: import from the defining module; keep re-exporting modules to a package's public entry point.
- Rejected, blanket "get rid of all barrel files" (Hagemeister, SRC-315): the register restricts that source to its synthetic measurement (one machine, 500 to 50,000 modules); the blanket is his position and is not adopted. Would win if the public entry point itself shows the load cost in the project's own measurement.
- Rejected, barrels as a convenience everywhere (MDN documents aggregation, no recommendation): wins where no measurement shows a cost and importers need many members.
- Grounds: single T3 source for the magnitude, mechanism (eager loading of everything re-exported) from MDN (SRC-086). The narrowing to "public entry point only" is inferred. The plan says T3 alone cannot make a node `known`; the brief's format would, so the node is `known | unvalidated: single T3 source`. Review point.

### D6. Static-only container classes: module is the namespace (PIG-JS.STRUCTURE.SURFACE.5; STRUCTURE-038, STRUCTURE-039)
- Decision: export functions and constants individually. Holder position of Google JS and Google TS.
- Rejected, W3C TAG (SRC-261): a class is shaped for state, stateless groupings are static methods. Wins when designing a platform-style API where the host offers no module namespace; the source's setting is web platform APIs and transfer to module code is inference.

### D7. Exported state: read-only (PIG-JS.STRUCTURE.SURFACE.3; STRUCTURE-034, STRUCTURE-035)
- Decision: never write to an import and export no mutable binding (no export let); mutate exported state only through functions.
- Rejected, exported mutable live binding: wins for a deliberate observable value owned by the exporter, if documented.
- Grounds: mechanism T1 (live bindings are read-only to importers, SRC-087, SRC-029, SRC-086) for the first half; the strongest form rests on holder positions of Google JS, Google TS and Airbnb.

### D8. Naming (STRUCTURE.NAMING.1 to .3; STRUCTURE-008, -009, -010)
- Decision: whole words; one concept one word; derive names from concepts.
- Grounds: SRC-260 (72 professional C# developers, T2, 19 percent), SRC-254 (T2); both single-source with transfer to JavaScript inferred. NAMING.2 rests on holder positions only. No admitted source covers casing, file naming or boundaries between naming schemes (thin per `11_coverage`).
- Rejected, short names: wins nowhere in the evidence (no significant difference between letters and abbreviations).

### D9. Philosophy decisions resting on one T2 principle source
- STRUCTURE.HIDING.1 (Parnas, SRC-257), HIDING.2 (Cook, SRC-259), STATE.1 (Codd, SRC-252): language-agnostic principles, each flagged `single T2 source`. SRC-257 is a principle only, never a JavaScript rule; SRC-259 gives no evidence for choosing either style; SRC-252 transfer to application state is inference.
- STRUCTURE.HIDING.3 (minimal surface at three levels) is inferred as a shared form across one T2 principle and T1 mechanisms in SRC-090 and SRC-091.

### D10. Holder-position-only decisions (flag `holder position only`)
- FORMAT.4 (no TypeScript namespaces, SRC-244), SURFACE.2 (export only what is used, SRC-244), PACKAGE.4 (relative paths within a project, SRC-244), NAMING.2 (SRC-239, SRC-244, SRC-261, SRC-312). Each wins under the max rule because no weaker admitted practice serves locality better; none has a T1 mechanism behind the rule.

### D11. Folklore rows (STRUCTURE-020, STRUCTURE-041)
- "CommonJS cannot load ES modules": restricted by SRC-089 and SRC-030 (works for graphs without top-level await). "Cyclic imports always crash": refuted by SRC-029 and SRC-089.

### D12. Deferred to a sibling branch, no node here
- Cycle-lint severity in CI and layering enforcement gates: VERIFICATION. Choice of ES modules over CommonJS for new code: SUBSET (LANG-C57, STRUCT-C21); proposed link FORMAT.1 to SUBSET.

## Undecided nodes

### U1. Declared layering (STRUCTURE.DIRECTION.2 in js-philosophy, PIG-JS.STRUCTURE.DIRECTION.3 in pig-js-defaults)
- State: `undecided | missing: no admitted source grounds a layering principle`.
- Why: STRUCT-C60 (open) cites SRC-085 (ESLint no-restricted-imports) and SRC-257 (Parnas). The register restricts SRC-085 to the mechanism ("grounds no layering principle"); the rule's own text gives environment fit and standardisation as reasons; SRC-257 supports hiding, not layering. STRUCT-C60 was therefore demoted to a `fact`, STRUCT-C61 kept as the mechanism fact.
- Evidence that would settle it: an admitted T1 source, or two independent T2 sources, stating a rule on which module kinds may import which, with grounds; or an empirical study linking dependency direction or layer violations to cost of change. `11_coverage` gap G-M10 and the "second T2 lead not yet audited" in STRUCT-C60's mechanism column point to the candidate to audit.

## Open gaps recorded as notes, not nodes
- Application state design (G-M10): STRUCTURE.STATE has one principle source (Codd) and one mechanism (exported objects); no admitted source on state design in applications.
- Composition versus inheritance (G-L04): no admitted claim.
- Naming conventions of casing and file names: no admitted claim.
