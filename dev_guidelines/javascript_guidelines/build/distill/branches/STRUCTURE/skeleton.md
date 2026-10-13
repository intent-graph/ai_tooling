# Skeleton: branch STRUCTURE

Purpose of the branch: locality of change, so that a change touches one place. Both graphs share the
L1 node `STRUCTURE`. In the epistemic_state cells `\|` stands for the pipe of the multi-issue
convention (`base \| issue: text`). Ledger rows are in `ledger.md`. A dash in the last column marks
a parent summary or a node derived from its children and links.

## js-philosophy

### Nodes, breadth-first

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| STRUCTURE | Structure for locality of change | Organize code so that a change touches one place: decisions hidden behind module boundaries, each piece of state in one place, importing free of hidden effects, dependencies that flow one way, names that carry their concept, paradigm chosen by intent. | known \| gap: layering principle undecided (STRUCTURE.DIRECTION.2) | - |
| STRUCTURE.HIDING | Hide likely-to-change decisions | Put each difficult or likely-to-change decision behind one module boundary and expose as little of it as possible. | known | - |
| STRUCTURE.STATE | State in one place | Keep each piece of state in one place and make shared state visible as shared. | known | - |
| STRUCTURE.PURITY | Effect-free importing | Make importing a module safe in any order by giving its top level no effect beyond defining its own exports. | known \| unvalidated: practice inferred from T1 mechanisms, no source states the rule | STRUCTURE-006 |
| STRUCTURE.DIRECTION | Dependencies flow one way | Let dependencies between modules flow in one direction so that a change propagates predictably. | known \| gap: layering undecided | - |
| STRUCTURE.NAMING | Names carry the concept | Choose names that let a reader recover the concept without the author. | known \| unvalidated: transfer from experiments to JavaScript is inference | - |
| STRUCTURE.PARADIGM | Paradigm by intent | Pick the programming paradigm per problem by what the problem is, not by a defect-rate claim. | known \| conflict: a paradigm lowers defects, Ray et al. 2014 (modest effect, restricted) \| unvalidated: inferred from the absence of evidence scoped to JavaScript | STRUCTURE-011, STRUCTURE-012 |
| STRUCTURE.HIDING.1 | Decompose by hidden decisions | Decompose a system by the decisions most likely to change, each hidden in one module, rather than by processing steps. | known \| unvalidated: single T2 source (Parnas), principle only | STRUCTURE-001 |
| STRUCTURE.HIDING.2 | Abstract data type versus object | Know which of the two hiding styles an interface offers, because they hide differently and mixing them blurs what may change. | known \| unvalidated: single T2 source (Cook), conceptual distinction without effect evidence | STRUCTURE-002 |
| STRUCTURE.HIDING.3 | Minimal public surface | Expose from each module only what other modules need, at every level where a name can be exposed. | known \| unvalidated: cross-level rule is inferred from one T2 principle and T1 mechanisms at two levels | STRUCTURE-003 |
| STRUCTURE.STATE.1 | One place per piece of state | Hold each piece of state once and derive the rest, so copies cannot drift apart. | known \| unvalidated: single T2 source (Codd), transfer to application state is inference | STRUCTURE-004 |
| STRUCTURE.STATE.2 | Exported state is shared state | Treat anything a module exports as state shared by all importers, and freeze it or hide it when sharing is not intended. | known \| unvalidated: quote tool-extracted | STRUCTURE-005 |
| STRUCTURE.DIRECTION.1 | No cycles between modules | Do not let modules depend on each other in a cycle, so that load order never decides whether code works. | known \| conflict: cycles are a supported mechanism, Node CommonJS docs (no recommendation) \| unvalidated: derived from PIG-JS.STRUCTURE.DIRECTION.1, no source measures the cost | - |
| STRUCTURE.DIRECTION.2 | Declared layering | Declare which kinds of module may import which kinds and enforce it mechanically. | undecided \| missing: no admitted source grounds a layering principle (the only mechanism source documents environment fit) | STRUCTURE-007 |
| STRUCTURE.NAMING.1 | Whole words | Name with whole words, not single letters or abbreviations, because readers find defects faster. | known \| unvalidated: single T2 experiment on C#, transfer to JavaScript inferred | STRUCTURE-008 |
| STRUCTURE.NAMING.2 | One concept one word | Give one concept one name made of common descriptive words, used consistently. | known \| unvalidated: holder positions only (Google, W3C TAG, Airbnb) | STRUCTURE-009 |
| STRUCTURE.NAMING.3 | Name from the concept | Derive a name from the concepts it covers, one word per concept, then compose; do not expect two people to coin the same name. | known \| unvalidated: single T2 source, language of the experiments not checked | STRUCTURE-010 |

### Intentlinks inside the branch (js-philosophy)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | STRUCTURE.HIDING.3 | STRUCTURE.HIDING.1 | requires | A decision stays hidden only if the surface that exposes the module stays minimal. |
| 2 | STRUCTURE.STATE.2 | STRUCTURE.HIDING.3 | requires | Exported state is part of a module's surface, so sharing it widens the surface that must stay minimal. |
| 3 | STRUCTURE.PURITY | STRUCTURE.DIRECTION.1 | refines | A module with no import-time effects cannot trip over an uninitialised binding in a cycle, which lowers the cost of a cycle that slips in (inferred from the cycle mechanism). |
| 4 | STRUCTURE.PARADIGM | STRUCTURE.HIDING.2 | requires | Choosing a paradigm per problem presupposes knowing what each hides: objects hide by procedural interface, data types by operations over a hidden representation. |

### Inter links to python-kb-philosophy (uids as in `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | STRUCTURE | python-kb-philosophy:STRUCTURE | refines | Structure precedes implementation; here it is specialised to the JavaScript module graph, where a change must stay inside one module. |
| 2 | STRUCTURE.HIDING | python-kb-philosophy:STRUCTURE | refines | Information hiding is the module-level form of structure primacy. |
| 3 | STRUCTURE.STATE | python-kb-philosophy:DATACENTRICITY | refines | Keeping state in one place is the data-stability principle applied to application state (inferred). |
| 4 | STRUCTURE.NAMING | python-kb-philosophy:COMMUNICATION | refines | Names are a reader-facing interface; the experiments here give the reason for the Python naming rules. |
| 5 | STRUCTURE.PARADIGM | python-kb-philosophy:POLYGLOT | refines | Right paradigm for the right problem: the defect-rate evidence supports no paradigm mandate, which matches the intent-based choice. |

### Proposed links to other branches (the integrator resolves them to uids)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | STRUCTURE.STATE.2 | SUBSET | requires | Freezing is shallow and does not make nested data immutable; the freeze mechanics are owned by SUBSET (group freeze-shallow). |
| 2 | STRUCTURE.STATE.2 | DEFENSE | requires | Freezing as a hardening step (group freeze-hardening) shares the mechanism and has a scope tension with patching built-ins. |
| 3 | STRUCTURE.PURITY | SUBSET | refines | SUBSET states that an ES module runs once however often it is imported (LANG-C57); the effect-free rule builds on it. P5 merge candidate for the integrator. |

## pig-js-defaults

### Nodes, breadth-first

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.STRUCTURE | JavaScript structure defaults | Concrete JavaScript and Node rules that keep a change inside one module or one package boundary: module format, import-time behaviour, exposed surface, dependency direction, package entry points. | known \| gap: layering rule undecided (PIG-JS.STRUCTURE.DIRECTION.3) | - |
| PIG-JS.STRUCTURE.FORMAT | Module format and host | State which module system and which host load each file, so that a specifier means one thing wherever the code runs. | known | - |
| PIG-JS.STRUCTURE.NODE | Node ESM and CommonJS interop | Write module code for Node so that it loads the same under both module systems, without relying on detection or on globals that do not exist. | known | - |
| PIG-JS.STRUCTURE.LOADING | Import-time behaviour | Make what happens when a module is imported predictable: once, hoisted, effect-free, asynchronous only at the edge. | known | - |
| PIG-JS.STRUCTURE.SURFACE | Exposed surface of a module | Expose from a module only the names others need, in a form that cannot be silently mutated or merged ambiguously. | known | - |
| PIG-JS.STRUCTURE.DIRECTION | Dependency direction | Keep the import graph acyclic and, where a source supports it, layered, so that a change flows one way. | known \| gap: layering undecided | - |
| PIG-JS.STRUCTURE.PACKAGE | Package entry points and internal addressing | Declare a package's public entry points and its internal aliases so that consumers and tools see one stable interface. | known | - |
| PIG-JS.STRUCTURE.FORMAT.1 | Explicit module format | Mark each file's module format with an extension or the package type field instead of letting Node guess from syntax. | known \| unvalidated: practice inferred from the detection order \| unvalidated: quote tool-extracted | STRUCTURE-013 |
| PIG-JS.STRUCTURE.FORMAT.2 | Browser module scripts | Load browser code with module scripts so that import and export work under CORS and same-origin rules. | known \| unvalidated: quote tool-extracted | STRUCTURE-014 |
| PIG-JS.STRUCTURE.FORMAT.3 | Resolution matches the host | Configure the type checker to resolve specifiers as the host that runs the code does, since ECMAScript leaves resolution to the host. | known \| unvalidated: quote tool-extracted | STRUCTURE-015 |
| PIG-JS.STRUCTURE.FORMAT.4 | Modules as the only sharing mechanism | Share code between files only through module import and export, never through namespaces. | known \| unvalidated: holder position only (Google TS) | STRUCTURE-016 |
| PIG-JS.STRUCTURE.NODE.1 | Full specifiers | Write the file extension and the directory index on every relative specifier in Node ESM. | known \| unvalidated: quote tool-extracted | STRUCTURE-017 |
| PIG-JS.STRUCTURE.NODE.2 | Module equivalents of CommonJS globals | Replace the CommonJS wrapper globals with their module equivalents and import JSON with the type attribute. | known \| unvalidated: quote tool-extracted | STRUCTURE-018 |
| PIG-JS.STRUCTURE.NODE.3 | Loading ESM from CommonJS | Load an ES module from CommonJS through require only when its graph has no top-level await, otherwise through dynamic import. | known \| unvalidated: quote tool-extracted | STRUCTURE-019, STRUCTURE-020 |
| PIG-JS.STRUCTURE.NODE.4 | Importing CommonJS from ESM | Use the default import of a CommonJS module and do not depend on detected named exports of unusual export patterns. | known \| unvalidated: quote tool-extracted | STRUCTURE-021 |
| PIG-JS.STRUCTURE.NODE.5 | CommonJS export assignment | Assign module.exports, never the exports shortcut, to replace what a CommonJS module exports. | known \| unvalidated: quote tool-extracted | STRUCTURE-022 |
| PIG-JS.STRUCTURE.LOADING.1 | Imports run once and hoisted | Never use import order to sequence work; run repeatable work by exporting a function. | known | STRUCTURE-023, STRUCTURE-024 |
| PIG-JS.STRUCTURE.LOADING.2 | Side-effect-only imports | Reserve bare imports for a module's side effect and name the module as such. | known \| unvalidated: quote tool-extracted | STRUCTURE-025 |
| PIG-JS.STRUCTURE.LOADING.3 | Dynamic import for conditional loading | Load conditionally or lazily with dynamic import, because static imports are top-level, hoisted and unconditional. | known \| unvalidated: quote tool-extracted | STRUCTURE-026 |
| PIG-JS.STRUCTURE.LOADING.4 | Top-level await confined to entry points | Use top-level await only where no other module imports or requires the file, because it makes every importer wait. | known \| conflict: top-level await is acceptable anywhere, champions in the TC39 proposal (education suffices) \| unvalidated: scope of the rule inferred from the mechanism, no measurement of the hazard | STRUCTURE-027, STRUCTURE-028 |
| PIG-JS.STRUCTURE.LOADING.5 | Static structure for dropping unused code | Keep import and export static so that tools can drop unused code, and give a bundler the hints it needs where import does more than export. | known \| gap: no decision row, facts and one acceptable-when only | STRUCTURE-029, STRUCTURE-030 |
| PIG-JS.STRUCTURE.LOADING.6 | Barrel files | Import from the defining module and keep re-exporting modules to a package's public entry point. | known \| unvalidated: single T3 source, one synthetic measurement on one machine \| conflict: barrels are a documented use of aggregation, MDN (no recommendation) | STRUCTURE-031 |
| PIG-JS.STRUCTURE.SURFACE.1 | Named exports | Export by name only, so every importer uses the exporter's name. | known \| conflict: default export for single-export modules, Airbnb \| unvalidated: rule rests on holder positions (Google JS and TS, one holder) | STRUCTURE-032 |
| PIG-JS.STRUCTURE.SURFACE.2 | Minimal exported surface | Export only the symbols used outside the module. | known \| unvalidated: holder position only (Google TS) | STRUCTURE-033 |
| PIG-JS.STRUCTURE.SURFACE.3 | Read-only exported state | Never write to an import and export no mutable bindings, so state has one owner. | known \| unvalidated: strongest form (no mutable export) rests on holder positions, mechanism is T1 | STRUCTURE-034, STRUCTURE-035 |
| PIG-JS.STRUCTURE.SURFACE.4 | Unambiguous re-exports | Do not merge modules by wildcard re-export when names may collide, because a collision silently drops the name. | known \| unvalidated: quote tool-extracted | STRUCTURE-036, STRUCTURE-037 |
| PIG-JS.STRUCTURE.SURFACE.5 | No static-only container classes | Use the module as the namespace and export functions and constants individually. | known \| conflict: stateless groupings as static methods, W3C TAG \| unvalidated: holder position only (Google JS and TS, one holder) | STRUCTURE-038, STRUCTURE-039 |
| PIG-JS.STRUCTURE.DIRECTION.1 | No import cycles | Create no import cycle between modules, in ESM or CommonJS. | known \| conflict: cycles are a supported mechanism, Node CommonJS docs (no recommendation) \| unvalidated: single T1 ground (MDN advice, used from its slot-01 claim where the register leaves it unrestricted), quote tool-extracted; other holders are positions only, no source measures the cost | STRUCTURE-040, STRUCTURE-041 |
| PIG-JS.STRUCTURE.DIRECTION.2 | Mechanical cycle detection | Detect cycles with a lint rule, enabled knowingly and with its cost bounded. | known \| unvalidated: single T3 source (the rule's own documentation) | STRUCTURE-042 |
| PIG-JS.STRUCTURE.DIRECTION.3 | Declared layering | Declare which module kinds may import which and enforce it mechanically. | undecided \| missing: no admitted source grounds a layering rule (the restriction-by-pattern rule documents environment fit only) | STRUCTURE-043 |
| PIG-JS.STRUCTURE.PACKAGE.1 | Exports field | Declare a package's public entry points with the exports field so that every other subpath is encapsulated. | known \| unvalidated: quote tool-extracted | STRUCTURE-044, STRUCTURE-045 |
| PIG-JS.STRUCTURE.PACKAGE.2 | Conditional export order | Order conditional export keys from most to least specific with default last. | known \| unvalidated: quote tool-extracted | STRUCTURE-046 |
| PIG-JS.STRUCTURE.PACKAGE.3 | Internal aliases by imports field | Express package-internal aliases with the imports field, which Node resolves natively. | known \| unvalidated: quote tool-extracted | STRUCTURE-047 |
| PIG-JS.STRUCTURE.PACKAGE.4 | Relative paths within a project | Import files of one logical project by relative path so the project can move. | known \| unvalidated: holder position only (Google TS) | STRUCTURE-048 |

### Intentlinks inside the branch (pig-js-defaults)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.STRUCTURE.DIRECTION.2 | PIG-JS.STRUCTURE.DIRECTION.1 | requires | Mechanical detection is how the no-cycle rule is kept true after the first commit. |
| 2 | PIG-JS.STRUCTURE.NODE.3 | PIG-JS.STRUCTURE.LOADING.4 | requires | require() of an ES module fails with ERR_REQUIRE_ASYNC_MODULE when any module in the graph uses top-level await. |
| 3 | PIG-JS.STRUCTURE.NODE.3 | PIG-JS.STRUCTURE.LOADING.3 | requires | Dynamic import is the route from CommonJS to ES modules that use top-level await. |
| 4 | PIG-JS.STRUCTURE.LOADING.6 | PIG-JS.STRUCTURE.SURFACE.4 | requires | Barrel files are built from wildcard re-exports, so the collision rule applies to them. |
| 5 | PIG-JS.STRUCTURE.PACKAGE.1 | PIG-JS.STRUCTURE.SURFACE.2 | refines | The exports field is the package-level form of the minimal exported surface. |
| 6 | PIG-JS.STRUCTURE.PACKAGE.2 | PIG-JS.STRUCTURE.PACKAGE.1 | refines | Conditional exports are keys inside the exports field. |
| 7 | PIG-JS.STRUCTURE.LOADING.6 | PIG-JS.STRUCTURE.PACKAGE.1 | requires | The one place a re-exporting module remains is the package's public entry point. |
| 8 | PIG-JS.STRUCTURE.DIRECTION.3 | PIG-JS.STRUCTURE.DIRECTION.1 | refines | Layering would constrain the direction of imports beyond acyclicity. |

### Links from pig-js-defaults to js-philosophy (inter, same branch)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.STRUCTURE.LOADING.1 | js-philosophy:STRUCTURE.PURITY | refines | Hoisting and run-once are the JavaScript mechanisms that make import order and repetition invisible only when the top level is effect-free. |
| 2 | PIG-JS.STRUCTURE.LOADING.5 | js-philosophy:STRUCTURE.PURITY | requires | Tools can drop unused code only when importing has no effect beyond exporting. |
| 3 | PIG-JS.STRUCTURE.SURFACE.1 | js-philosophy:STRUCTURE.HIDING.3 | refines | A named export is one exposed name; a default export lets each importer rename it. |
| 4 | PIG-JS.STRUCTURE.SURFACE.2 | js-philosophy:STRUCTURE.HIDING.3 | refines | Module-level form of the minimal public surface. |
| 5 | PIG-JS.STRUCTURE.PACKAGE.1 | js-philosophy:STRUCTURE.HIDING.3 | refines | Package-level form of the minimal public surface. |
| 6 | PIG-JS.STRUCTURE.SURFACE.3 | js-philosophy:STRUCTURE.STATE.2 | refines | Read-only live bindings and no mutable exports are how JavaScript keeps shared state with one owner. |
| 7 | PIG-JS.STRUCTURE.SURFACE.5 | js-philosophy:STRUCTURE.HIDING.2 | refines | A class of static members is a procedural namespace pretending to be an object (inferred). |
| 8 | PIG-JS.STRUCTURE.DIRECTION.1 | js-philosophy:STRUCTURE.DIRECTION.1 | refines | The JavaScript rule behind the principle of one-way dependencies. |
| 9 | PIG-JS.STRUCTURE.DIRECTION.3 | js-philosophy:STRUCTURE.DIRECTION.2 | refines | The JavaScript rendering of declared layering, undecided in both graphs. |

### Proposed links to other branches (the integrator resolves them to uids)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.STRUCTURE.FORMAT.1 | SUBSET | requires | These format rules presuppose that ES modules are the chosen format, which SUBSET decides (LANG-C57, STRUCT-C21); this branch holds no rule for ES modules versus CommonJS in new code. |
| 2 | PIG-JS.STRUCTURE.FORMAT.3 | CONTRACTS | requires | The type checker's module-resolution setting must match the host; the setting is a CONTRACTS decision. |
| 3 | PIG-JS.STRUCTURE.FORMAT.4 | CONTRACTS | requires | The TypeScript namespace ban belongs with the type-layer rules. |
| 4 | PIG-JS.STRUCTURE.NODE.1 | CONTRACTS | requires | Importing with the .ts extension under Node type stripping is a type-layer rule (TYPES-C06 sits here by routing). |
| 5 | PIG-JS.STRUCTURE.SURFACE.2 | CONTRACTS | refines | Google TS export visibility is a typed-API rule at the boundary with CONTRACTS. |
| 6 | PIG-JS.STRUCTURE.SURFACE.3 | SUBSET | requires | Freeze mechanics (shallow freeze, group freeze-shallow) are owned by SUBSET. |
| 7 | PIG-JS.STRUCTURE.SURFACE.3 | DEFENSE | requires | Freezing as hardening (group freeze-hardening) shares the mechanism; scope tension with patching built-ins. |
| 8 | PIG-JS.STRUCTURE.SURFACE.5 | SUBSET | requires | Class design rules (classes, this, private members) are owned by SUBSET. |
| 9 | PIG-JS.STRUCTURE.LOADING.1 | SUBSET | refines | LANG-C57 in SUBSET states the same run-once fact; P5 merge candidate for the integrator. |
| 10 | PIG-JS.STRUCTURE.LOADING.4 | CONTROL | requires | A never-resolving top-level await ends the process with status 13, which belongs with process-lifecycle rules. |
| 11 | PIG-JS.STRUCTURE.LOADING.5 | VERIFICATION | requires | Bundling and tree-shaking configuration is a build gate (boundary 08 QUALITY). |
| 12 | PIG-JS.STRUCTURE.DIRECTION.2 | VERIFICATION | requires | The severity of the cycle lint rule in CI is a gate decision owned by VERIFICATION. |
| 13 | PIG-JS.STRUCTURE.DIRECTION.3 | VERIFICATION | requires | If a layering rule is ever grounded, its enforcement is a lint-gate decision. |
| 14 | PIG-JS.STRUCTURE.PACKAGE.1 | DEPENDENCIES | requires | A package's public entry points are the interface that consumers and the supply chain see (boundary 07 SUPPLY). |

## Judge records (one per defaults node holding a decision)

Each record: positions (claims, sources), forces, decision, rejected with the condition under which it
would win. A node with a single position states the alternative as the absence of the practice.

| node | positions | forces | decision | rejected (condition under which it wins) |
|---|---|---|---|---|
| PIG-JS.STRUCTURE.FORMAT.1 | Explicit marker (LANG-C59, STRUCT-C14; SRC-030) against syntax detection for unmarked .js (SRC-030 describes it) | Explicit serves locality because a file's meaning does not change with its content or a Node upgrade; detection saves one line of config | Explicit extension or type field | Syntax detection: wins for throwaway scripts that are never imported |
| PIG-JS.STRUCTURE.FORMAT.2 | Module scripts (LANG-C58; SRC-029) against classic scripts | Modules scope their names; classic scripts share one global scope | Module scripts | Classic scripts: win only where the code must run from file:// or in an engine without module support |
| PIG-JS.STRUCTURE.FORMAT.3 | Checker configured for the host (STRUCT-C37; SRC-094) against a default or unaligned setting | A mismatch makes the checker approve imports the host cannot resolve | Match the checker to the host | Default setting: wins when the host is a single known one the default already models |
| PIG-JS.STRUCTURE.FORMAT.4 | Module-only sharing (STRUCT-C27; SRC-244, Google TS position) against TypeScript namespaces | Namespaces add a second organising mechanism beside modules | Modules only | Namespaces: win for declaration files describing a global-script library, where no module exists (inferred, not stated by the source) |
| PIG-JS.STRUCTURE.NODE.1 | Full specifiers (STRUCT-C11, LANG-C60, TYPES-C06; SRC-030, SRC-038; Google JS position) against extensionless specifiers | Node ESM resolution does not search extensions, so extensionless specifiers fail | Always write extension and directory index | Extensionless: wins only inside a bundler that resolves it, at the price of leaving the Node-runnable subset |
| PIG-JS.STRUCTURE.NODE.2 | Module equivalents (STRUCT-C13, LANG-C62; SRC-030, SRC-028) against CommonJS globals | The globals do not exist in ES modules; JSON import needs the attribute | Module equivalents and the json attribute | CommonJS globals: win inside a file that is still CommonJS |
| PIG-JS.STRUCTURE.NODE.3 | require() of ESM without top-level await, import() otherwise (LANG-C61, STRUCT-C16; SRC-030, SRC-089) against the belief that CommonJS cannot load ESM | The belief forces dynamic import everywhere; the mechanism allows synchronous require for graphs without top-level await | Allow require only for graphs without top-level await, else dynamic import | Always dynamic import: wins when the graph may gain top-level await later, since ERR_REQUIRE_ASYNC_MODULE appears at run time |
| PIG-JS.STRUCTURE.NODE.4 | Default import of CommonJS (STRUCT-C15; SRC-030) against reliance on named imports | Named export detection is static analysis that does not always succeed | Default import for unusual export patterns | Named imports: win for patterns the Node docs list as detected |
| PIG-JS.STRUCTURE.NODE.5 | Assign module.exports (STRUCT-C17; SRC-089) against assigning exports | exports is a local alias that detaches on assignment | Assign module.exports | Property assignment to exports: wins when only adding properties |
| PIG-JS.STRUCTURE.LOADING.1 | No order reliance, run-once top level (STRUCT-C04, STRUCT-C05; SRC-087, SRC-029, SRC-089, SRC-256) against sequencing work by import order | Hoisting runs imported effects first; run-once means a second import repeats nothing | Never sequence by import order; export a function for repeatable work | Import-order sequencing: wins nowhere in ES modules (the mechanism contradicts it) |
| PIG-JS.STRUCTURE.LOADING.2 | Bare import named as side-effect module (STRUCT-C07; SRC-087) against bare imports of modules that also export | A bare import discards exports, so using it on a module with exports hides the dependency | Reserve bare imports for side effects | Bare import of exporting modules: wins nowhere |
| PIG-JS.STRUCTURE.LOADING.3 | Dynamic import for conditional loading (STRUCT-C20; SRC-087, SRC-256) against static imports plus conditional use | Static imports are unconditional, so the cost is paid even when unused | Dynamic import for conditional or deferred load | Static import: wins whenever the module is always needed, for static analysis |
| PIG-JS.STRUCTURE.LOADING.4 | Entry-point-only top-level await (STRUCT-C19, STRUCT-C18, LANG-C63; SRC-092, SRC-030, SRC-029) against top-level await anywhere (champions Borins and Startsev) | An await in a shared module makes every importer asynchronous, so a leaf change spreads upward; entry points have no importers | Entry points only | Anywhere: wins if a measurement shows the coordination hazard is negligible, or in scripts that nothing imports |
| PIG-JS.STRUCTURE.LOADING.6 | Avoid internal barrels (STRUCT-C29; SRC-315 T3 measurement, SRC-086) against barrels as a convenience (MDN documents aggregation, no recommendation) and the blanket removal position | A barrel couples each importer to every re-exported module; a public entry point is the one place aggregation earns its cost | Import from the defining module, aggregate at the public entry point only | Barrels everywhere: win where no measurement shows load cost and importers need many members; blanket removal wins if the public entry point is itself the problem |
| PIG-JS.STRUCTURE.SURFACE.1 | Named only (STRUCT-C24; SRC-239, SRC-244) against default for single-export modules (SRC-312) and MDN's neutral interop note (SRC-029) | A default export has no canonical name, so renames cannot be found mechanically | Named exports only | Default: wins when a framework or tool mandates a default export, or for CommonJS and AMD interop (the purpose MDN names) |
| PIG-JS.STRUCTURE.SURFACE.2 | Export only what is used (STRUCT-C25; SRC-244) against exporting everything for convenience | Each extra export is a name that others may start to depend on | Minimal export list | Export-all: wins in a package that is explicitly a toolbox whose members are its purpose |
| PIG-JS.STRUCTURE.SURFACE.3 | No mutation of exported state and no mutable exports (STRUCT-C01, STRUCT-C03; SRC-087, SRC-239, SRC-244, SRC-312) against exported mutable bindings with live updates | Live bindings let an exporter change what importers see, so state has hidden writers | No mutable exports; initialise once, change only through functions | Mutable live export: wins for a deliberate observable value owned by the exporter, if documented |
| PIG-JS.STRUCTURE.SURFACE.4 | No wildcard merge with possible collisions (STRUCT-C22, STRUCT-C23; SRC-086) against export * convenience | A collision silently drops the name; duplicates are a SyntaxError | Do not use export * where names may collide | export *: wins when the sources are known disjoint |
| PIG-JS.STRUCTURE.SURFACE.5 | Module as namespace (LANG-C15, STRUCT-C26; SRC-239, SRC-244) against static-method groupings (STRUCT-C54; SRC-261) | A module already namespaces and lets importers pick single functions | Export functions individually | Static-method groupings: win when designing a platform-style API where the host offers no module namespace (W3C TAG's setting, transfer inferred) |
| PIG-JS.STRUCTURE.DIRECTION.1 | No cycles (STRUCT-C09, LANG-C64; SRC-029, SRC-239, SRC-313) against tolerating cycles (SRC-089 documents partial exports as supported) | A cycle makes correctness depend on evaluation order; tolerance costs nothing until a binding is used early | No import cycles | Tolerate: wins where a cycle is deliberate in CommonJS legacy code and no fault is observed, or where the detection cost exceeds the benefit |
| PIG-JS.STRUCTURE.DIRECTION.2 | Enable the cycle lint rule with maxDepth (STRUCT-C10; SRC-313) against no automated check | Automation keeps the rule true; the rule is computationally expensive | Enable knowingly, bound with maxDepth | No check: wins in a small codebase with no cycle issue, as the rule's own documentation says |
| PIG-JS.STRUCTURE.PACKAGE.1 | Declare exports (STRUCT-C33, STRUCT-C34; SRC-090) against leaving every file reachable | Encapsulation lets internals change without breaking consumers | Declare the exports field | Leave open: wins for an existing package whose consumers deep-import, until a breaking release is acceptable |
| PIG-JS.STRUCTURE.PACKAGE.2 | Specific-to-general order, default last (STRUCT-C35; SRC-090) against any order | Earlier entries win, so a general key placed first shadows a specific one | Specific first, default last | Any order: wins nowhere |
| PIG-JS.STRUCTURE.PACKAGE.3 | imports field for internal aliases (STRUCT-C36; SRC-090) against path aliases configured only in a bundler or checker | The field is resolved natively and cannot collide with external names | Use the imports field | Tool-level path aliases: win only for code that never runs un-bundled and is checked by a tool that cannot read the field (inferred) |
| PIG-JS.STRUCTURE.PACKAGE.4 | Relative paths within a project (STRUCT-C28; SRC-244 position) against absolute or alias paths | Relative paths survive moving the project | Relative within a project | Aliases: win for deep trees where relative paths climb many levels, via the imports field (PACKAGE.3) |
