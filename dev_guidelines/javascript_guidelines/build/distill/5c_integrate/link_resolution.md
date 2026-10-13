# Cross-branch link resolution (stage 5c)

Every proposal of the eight branch skeletons, with its disposition. `how`: given (kept), flipped (direction reversed to
match the sentence), retargeted (branch keyword resolved to a uid), retyped (type changed), merged (a mirror proposal
folded into another link), dropped (reason), planned (boundary link to the web-architecture graphs).

| branch | graph | proposal | proposed from | proposed to | proposed type | disposition |
|---|---|---|---|---|---|---|
| SUBSET | defaults | 1 | SUBSET.STRICTNESS.2 | STRUCTURE | requires | flipped: PIG-JS.STRUCTURE.FORMAT.1 requires PIG-JS.SUBSET.STRICTNESS.2 |
| SUBSET | defaults | 2 | SUBSET.STRICTNESS | VERIFICATION | requires | retargeted: PIG-JS.SUBSET.STRICTNESS requires PIG-JS.VERIFICATION.LINT.1.1 |
| SUBSET | defaults | 3 | SUBSET.CONVERSION | VERIFICATION | requires | retargeted: PIG-JS.SUBSET.CONVERSION requires PIG-JS.VERIFICATION.LINT.1.1 |
| SUBSET | defaults | 4 | SUBSET.CONVERSION.5 | CONTRACTS | requires | retargeted: PIG-JS.SUBSET.CONVERSION.5 requires PIG-JS.CONTRACTS.BOUNDARY |
| SUBSET | defaults | 5 | SUBSET.CONVERSION.6 | CONTRACTS | requires | retargeted: PIG-JS.SUBSET.CONVERSION.6 requires PIG-JS.CONTRACTS.MODEL.3 |
| SUBSET | defaults | 6 | SUBSET.NUMBERS.4 | CONTRACTS | dataflow | retargeted: PIG-JS.SUBSET.NUMBERS.4 dataflow PIG-JS.CONTRACTS.BOUNDARY.1 |
| SUBSET | defaults | 7 | SUBSET.NUMBERS.4 | DEFENSE | requires | retargeted: PIG-JS.SUBSET.NUMBERS.4 requires PIG-JS.DEFENSE.PROTOTYPE.2 |
| SUBSET | defaults | 8 | SUBSET.MUTATION.1 | STRUCTURE | requires | flipped: PIG-JS.STRUCTURE.SURFACE.3 requires PIG-JS.SUBSET.MUTATION.1 |
| SUBSET | defaults | 9 | SUBSET.MUTATION.1 | DEFENSE | requires | flipped: PIG-JS.DEFENSE.PROTOTYPE.3 requires PIG-JS.SUBSET.MUTATION.1 |
| SUBSET | defaults | 10 | SUBSET.OBJECTS.5 | DEFENSE | conflicts | retargeted: PIG-JS.SUBSET.OBJECTS.5 conflicts PIG-JS.DEFENSE.PROTOTYPE.3 |
| SUBSET | defaults | 11 | SUBSET.OBJECTS.5 | RUNTIME | requires | retargeted: PIG-JS.SUBSET.OBJECTS.5 requires PIG-JS.RUNTIME.MEASURE.2 |
| SUBSET | defaults | 12 | SUBSET.OBJECTS.6 | DEFENSE | requires | flipped: PIG-JS.DEFENSE.PROTOTYPE.1 requires PIG-JS.SUBSET.OBJECTS.6 |
| SUBSET | defaults | 13 | SUBSET.EVOLUTION.5 | VERIFICATION | requires | retargeted: PIG-JS.SUBSET.EVOLUTION.5 requires PIG-JS.VERIFICATION.FORMAT.1 |
| SUBSET | defaults | 14 | SUBSET.EVOLUTION.1 | DEPENDENCIES | requires | retargeted: PIG-JS.SUBSET.EVOLUTION.1 requires PIG-JS.DEPENDENCIES.UPDATE.2 |
| SUBSET | philosophy | 1 | SUBSET.FAILURE | CONTROL | requires | flipped: CONTROL.FAILURE requires SUBSET.FAILURE |
| SUBSET | philosophy | 2 | SUBSET.VISIBLE | CONTRACTS | requires | retargeted: SUBSET.VISIBLE requires CONTRACTS.BOUNDARY |
| SUBSET | philosophy | 3 | SUBSET.MATURITY | DEPENDENCIES | requires | retargeted: SUBSET.MATURITY requires DEPENDENCIES.ADMISSION.2 |
| CONTRACTS | defaults | Q1 | CONTRACTS.LAYER.3 | VERIFICATION | requires | retargeted: PIG-JS.CONTRACTS.LAYER.3 requires PIG-JS.VERIFICATION.LINT.2 |
| CONTRACTS | defaults | Q2 | CONTRACTS.ESCAPE.2 | VERIFICATION | requires | retargeted: PIG-JS.CONTRACTS.ESCAPE.2 requires PIG-JS.VERIFICATION.LINT.1.4 |
| CONTRACTS | defaults | Q3 | CONTRACTS.ESCAPE.6 | VERIFICATION | requires | retargeted: PIG-JS.CONTRACTS.ESCAPE.6 requires PIG-JS.VERIFICATION.LINT.2.3 |
| CONTRACTS | defaults | Q4 | CONTRACTS.STRICT.4 | DEPENDENCIES | requires | retargeted: PIG-JS.CONTRACTS.STRICT.4 requires PIG-JS.DEPENDENCIES.UPDATE.2 |
| CONTRACTS | defaults | Q5 | CONTRACTS.LAYER.6 | STRUCTURE | refines | retargeted: PIG-JS.CONTRACTS.LAYER.6 refines PIG-JS.STRUCTURE.FORMAT |
| CONTRACTS | defaults | Q6 | CONTRACTS.LAYER.4 | SUBSET | refines | retargeted: PIG-JS.CONTRACTS.LAYER.4 refines PIG-JS.SUBSET.EVOLUTION |
| CONTRACTS | defaults | Q7 | CONTRACTS.MODEL.2 | SUBSET | refines | retargeted: PIG-JS.CONTRACTS.MODEL.2 refines PIG-JS.SUBSET.CONVERSION |
| CONTRACTS | defaults | Q8 | CONTRACTS.MODEL.3 | SUBSET | refines | merged: PIG-JS.SUBSET.CONVERSION.6 requires PIG-JS.CONTRACTS.MODEL.3 |
| CONTRACTS | defaults | Q9 | CONTRACTS.SIGNATURE.1 | STRUCTURE | refines | dropped: moot: function and object API design is owned by CONTRACTS (target hierarchy), so SIGNATURE has no STRUCTURE counterpart to link to |
| CONTRACTS | defaults | Q10 | CONTRACTS.BOUNDARY.1 | CONTROL | requires | retargeted: PIG-JS.CONTRACTS.BOUNDARY.1 requires PIG-JS.CONTROL.ERRORS.2 |
| CONTRACTS | defaults | Q11 | CONTRACTS.BOUNDARY.1 | DEFENSE | refines | retyped: PIG-JS.CONTRACTS.BOUNDARY.1 dataflow PIG-JS.DEFENSE.PROTOTYPE.2 |
| CONTRACTS | defaults | Q12 | CONTRACTS.BOUNDARY.2 | DEFENSE | requires | retyped: PIG-JS.CONTRACTS.BOUNDARY.2 dataflow PIG-JS.DEFENSE.PROTOTYPE.1 |
| CONTRACTS | defaults | Q13 | CONTRACTS.BOUNDARY.3 | DEFENSE | refines | retargeted: PIG-JS.CONTRACTS.BOUNDARY.3 refines PIG-JS.DEFENSE.PROTOTYPE.1 |
| CONTRACTS | defaults | Q14 | CONTRACTS.BOUNDARY.4 | DEFENSE | refines | flipped: PIG-JS.DEFENSE.INJECTION requires PIG-JS.CONTRACTS.BOUNDARY.4; merged: PIG-JS.DEFENSE.HOST.4 requires PIG-JS.CONTRACTS.BOUNDARY.4 |
| CONTRACTS | philosophy | P1 | CONTRACTS.BOUNDARY.1 | DEFENSE | requires | flipped: DEFENSE requires CONTRACTS.BOUNDARY.1 |
| CONTRACTS | philosophy | P2 | CONTRACTS.BOUNDARY.2 | DEFENSE | refines | flipped: DEFENSE.INJECTION refines CONTRACTS.BOUNDARY.2 |
| CONTRACTS | philosophy | P3 | CONTRACTS.STATIC.1 | VERIFICATION | requires | retargeted: CONTRACTS.STATIC.1 requires VERIFICATION.ENFORCEMENT |
| CONTRACTS | philosophy | P4 | CONTRACTS.SHAPE | STRUCTURE | refines | retargeted: CONTRACTS.SHAPE refines STRUCTURE.NAMING |
| CONTRACTS | philosophy | P5 | CONTRACTS.BOUNDARY.1 | web-architecture (planned, not created) | refines | planned: CONTRACTS.BOUNDARY.1 -> web-app-philosophy |
| CONTROL | defaults | 1 | CONTROL.PROMISES.3 | VERIFICATION | requires | retargeted: PIG-JS.CONTROL.PROMISES.3 requires PIG-JS.VERIFICATION.LINT.1.4 |
| CONTROL | defaults | 2 | CONTROL.ERRORS.2 | CONTRACTS | requires | retargeted: PIG-JS.CONTROL.ERRORS.2 requires PIG-JS.CONTRACTS.STRICT.1 |
| CONTROL | defaults | 3 | CONTROL.SCHEDULING.2 | DEFENSE | dataflow | retargeted: PIG-JS.CONTROL.SCHEDULING.2 dataflow PIG-JS.DEFENSE.HOST |
| CONTROL | defaults | 4 | CONTROL.BOUNDS.2 | DEFENSE | dataflow | retargeted: PIG-JS.CONTROL.BOUNDS.2 dataflow PIG-JS.DEFENSE.HOST |
| CONTROL | defaults | 5 | CONTROL.FLOW | RUNTIME | dataflow | retargeted: PIG-JS.CONTROL.FLOW dataflow PIG-JS.RUNTIME.MEMORY |
| CONTROL | defaults | 6 | CONTROL.PROCESS.4 | web-architecture (planned boundary) | requires | planned: PIG-JS.CONTROL.PROCESS.4 -> pig-web-defaults |
| CONTROL | defaults | 7 | CONTROL.PROMISES.5 | SUBSET | dataflow | retargeted: PIG-JS.CONTROL.PROMISES.5 dataflow PIG-JS.SUBSET.EVOLUTION.1 |
| CONTROL | defaults | 8 | CONTROL.BOUNDS.1 | STRUCTURE | requires | retargeted: PIG-JS.CONTROL.BOUNDS.1 requires PIG-JS.CONTRACTS.SIGNATURE |
| STRUCTURE | defaults | 1 | STRUCTURE.FORMAT.1 | SUBSET | requires | merged: PIG-JS.STRUCTURE.FORMAT.1 requires PIG-JS.SUBSET.STRICTNESS.2 |
| STRUCTURE | defaults | 2 | STRUCTURE.FORMAT.3 | CONTRACTS | requires | retargeted: PIG-JS.STRUCTURE.FORMAT.3 requires PIG-JS.CONTRACTS.LAYER.5 |
| STRUCTURE | defaults | 3 | STRUCTURE.FORMAT.4 | CONTRACTS | requires | retargeted: PIG-JS.STRUCTURE.FORMAT.4 requires PIG-JS.CONTRACTS.LAYER.4 |
| STRUCTURE | defaults | 4 | STRUCTURE.NODE.1 | CONTRACTS | requires | retargeted: PIG-JS.STRUCTURE.NODE.1 requires PIG-JS.CONTRACTS.LAYER.5 |
| STRUCTURE | defaults | 5 | STRUCTURE.SURFACE.2 | CONTRACTS | refines | dropped: no CONTRACTS node states export visibility; the rule stays in STRUCTURE.SURFACE.2 |
| STRUCTURE | defaults | 6 | STRUCTURE.SURFACE.3 | SUBSET | requires | retargeted: PIG-JS.STRUCTURE.SURFACE.3 requires PIG-JS.SUBSET.MUTATION.1 |
| STRUCTURE | defaults | 7 | STRUCTURE.SURFACE.3 | DEFENSE | requires | merged: PIG-JS.STRUCTURE.SURFACE.3 requires PIG-JS.SUBSET.MUTATION.1 |
| STRUCTURE | defaults | 8 | STRUCTURE.SURFACE.5 | SUBSET | requires | retargeted: PIG-JS.STRUCTURE.SURFACE.5 requires PIG-JS.SUBSET.OBJECTS |
| STRUCTURE | defaults | 9 | STRUCTURE.LOADING.1 | SUBSET | refines | retargeted: PIG-JS.STRUCTURE.LOADING.1 refines PIG-JS.SUBSET.STRICTNESS.2 |
| STRUCTURE | defaults | 10 | STRUCTURE.LOADING.4 | CONTROL | requires | retargeted: PIG-JS.STRUCTURE.LOADING.4 requires PIG-JS.CONTROL.PROCESS |
| STRUCTURE | defaults | 11 | STRUCTURE.LOADING.5 | VERIFICATION | requires | retargeted: PIG-JS.STRUCTURE.LOADING.5 requires PIG-JS.VERIFICATION.LINT.2 |
| STRUCTURE | defaults | 12 | STRUCTURE.DIRECTION.2 | VERIFICATION | requires | retargeted: PIG-JS.STRUCTURE.DIRECTION.2 requires PIG-JS.VERIFICATION.LINT.2 |
| STRUCTURE | defaults | 13 | STRUCTURE.DIRECTION.3 | VERIFICATION | requires | retargeted: PIG-JS.STRUCTURE.DIRECTION.3 requires PIG-JS.VERIFICATION.LINT.2 |
| STRUCTURE | defaults | 14 | STRUCTURE.PACKAGE.1 | DEPENDENCIES | requires | retargeted: PIG-JS.STRUCTURE.PACKAGE.1 requires PIG-JS.DEPENDENCIES.PUBLISH |
| STRUCTURE | philosophy | 1 | STRUCTURE.STATE.2 | SUBSET | requires | retargeted: STRUCTURE.STATE.2 requires SUBSET.STATE |
| STRUCTURE | philosophy | 2 | STRUCTURE.STATE.2 | DEFENSE | requires | dropped: no philosophy node of DEFENSE states a freeze or hardening principle; the defaults freeze hub (SUBSET.MUTATION.1) carries it |
| STRUCTURE | philosophy | 3 | STRUCTURE.PURITY | SUBSET | refines | dropped: no philosophy node of SUBSET states the module run-once fact; the defaults link STRUCTURE.LOADING.1 to SUBSET.STRICTNESS.2 carries it |
| DEFENSE | defaults | 1 | DEFENSE.PROTOTYPE.1 | SUBSET | refines | merged: PIG-JS.DEFENSE.PROTOTYPE.1 requires PIG-JS.SUBSET.OBJECTS.6 |
| DEFENSE | defaults | 2 | DEFENSE.PROTOTYPE.3 | SUBSET | conflicts | merged: PIG-JS.SUBSET.OBJECTS.5 conflicts PIG-JS.DEFENSE.PROTOTYPE.3 |
| DEFENSE | defaults | 3 | DEFENSE.PROTOTYPE.3 | STRUCTURE | refines | merged: PIG-JS.DEFENSE.PROTOTYPE.3 requires PIG-JS.SUBSET.MUTATION.1 |
| DEFENSE | defaults | 4 | DEFENSE.PROTOTYPE.3 | DEPENDENCIES | requires | retargeted: PIG-JS.DEFENSE.PROTOTYPE.3 requires PIG-JS.DEPENDENCIES.UPDATE |
| DEFENSE | defaults | 5 | DEFENSE.INJECTION.1.1 | VERIFICATION | requires | retargeted: PIG-JS.DEFENSE.INJECTION.1.1 requires PIG-JS.VERIFICATION.LINT.1 |
| DEFENSE | defaults | 6 | DEFENSE.SECRETS.5 | VERIFICATION | requires | retargeted: PIG-JS.DEFENSE.SECRETS.5 requires PIG-JS.VERIFICATION.LINT.2 |
| DEFENSE | defaults | 7 | DEFENSE.SECRETS.5 | DEPENDENCIES | refines | flipped: PIG-JS.DEPENDENCIES.PUBLISH.2 requires PIG-JS.DEFENSE.SECRETS.5 |
| DEFENSE | defaults | 8 | DEFENSE.SECRETS.6 | RUNTIME | refines | dropped: moot: the allocUnsafe claim (RUNTIME-C13) is placed in DEFENSE (row DEFENSE-117); RUNTIME holds no node on it |
| DEFENSE | defaults | 9 | DEFENSE.HOST.1 | DEPENDENCIES | refines | retargeted: PIG-JS.DEFENSE.HOST.1 refines js-philosophy:DEPENDENCIES.TRUST.2 |
| DEFENSE | defaults | 10 | DEFENSE.HOST.4 | CONTROL | requires | retargeted: PIG-JS.DEFENSE.HOST.4 requires PIG-JS.CONTROL.SCHEDULING.2 |
| DEFENSE | defaults | 11 | DEFENSE.HOST.5 | CONTRACTS | refines | retargeted: PIG-JS.DEFENSE.HOST.5 refines PIG-JS.CONTRACTS.BOUNDARY |
| DEFENSE | defaults | 12 | DEFENSE.HOST.6 | DEPENDENCIES | requires | retargeted: PIG-JS.DEFENSE.HOST.6 requires PIG-JS.DEPENDENCIES.INSTALL |
| DEFENSE | defaults | 13 | DEFENSE.INJECTION.4.3 | CONTROL | requires | retargeted: PIG-JS.DEFENSE.INJECTION.4.3 requires PIG-JS.CONTROL.ERRORS.2 |
| DEFENSE | defaults | 14 | DEFENSE.INJECTION.5 | CONTRACTS | requires | retargeted: PIG-JS.DEFENSE.INJECTION.5 requires PIG-JS.CONTRACTS.BOUNDARY |
| DEFENSE | defaults | 15 | DEFENSE.DOM.6 | DEPENDENCIES | dataflow | retargeted: PIG-JS.DEFENSE.DOM.6 dataflow PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE |
| DEPENDENCIES | defaults | 4 | DEPENDENCIES.INSTALL.1 | VERIFICATION | dataflow | merged: PIG-JS.VERIFICATION.LINT.2 requires PIG-JS.DEPENDENCIES.INSTALL.1 |
| DEPENDENCIES | defaults | 5 | DEPENDENCIES.UPDATE.3 | VERIFICATION | dataflow | retargeted: PIG-JS.DEPENDENCIES.UPDATE.3 dataflow PIG-JS.VERIFICATION.LINT.2 |
| DEPENDENCIES | defaults | 6 | DEPENDENCIES.SCREEN.1 | VERIFICATION | requires | retargeted: PIG-JS.DEPENDENCIES.SCREEN.1 requires js-philosophy:VERIFICATION.ENFORCEMENT |
| DEPENDENCIES | defaults | 7 | DEPENDENCIES.UPDATE.2 | RUNTIME | requires | dropped: moot: no RUNTIME node holds Node release lifecycle; the fact sits in PIG-JS.DEPENDENCIES.UPDATE.2 |
| DEPENDENCIES | defaults | 8 | DEPENDENCIES.PUBLISH.3 | CONTRACTS | requires | retargeted: PIG-JS.DEPENDENCIES.PUBLISH.3 requires PIG-JS.CONTRACTS.LAYER.1 |
| DEPENDENCIES | defaults | 9 | DEPENDENCIES.PUBLISH.2 | DEFENSE | requires | retargeted: PIG-JS.DEPENDENCIES.PUBLISH.2 requires PIG-JS.DEFENSE.SECRETS.5 |
| DEPENDENCIES | defaults | 10 | DEPENDENCIES.FRAMEWORK_SHORTLIST | DEFENSE | requires | retargeted: PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST requires PIG-JS.DEFENSE.DOM.6 |
| DEPENDENCIES | defaults | 11 | DEPENDENCIES.FRAMEWORK_SHORTLIST | CONTRACTS | requires | retargeted: PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST requires PIG-JS.CONTRACTS.LAYER.1 |
| DEPENDENCIES | philosophy | 1 | DEPENDENCIES.TRUST.1 | DEFENSE | requires | retargeted: DEPENDENCIES.TRUST.1 requires DEFENSE.INJECTION |
| DEPENDENCIES | philosophy | 2 | DEPENDENCIES.TRUST.2 | DEFENSE | requires | retargeted: DEPENDENCIES.TRUST.2 requires DEFENSE.HOST |
| DEPENDENCIES | philosophy | 3 | DEPENDENCIES.ADMISSION.4 | DEFENSE | requires | retargeted: DEPENDENCIES.ADMISSION.4 requires DEFENSE.DOM.1 |
| VERIFICATION | defaults | 1 | VERIFICATION.LINT.1.1 | SUBSET | dataflow | merged: PIG-JS.SUBSET.STRICTNESS requires PIG-JS.VERIFICATION.LINT.1.1 |
| VERIFICATION | defaults | 2 | VERIFICATION.LINT.1.4 | CONTRACTS | requires | retargeted: PIG-JS.VERIFICATION.LINT.1.4 requires PIG-JS.CONTRACTS.LAYER.1 |
| VERIFICATION | defaults | 3 | VERIFICATION.LINT.1.4 | CONTROL | dataflow | merged: PIG-JS.CONTROL.PROMISES.3 requires PIG-JS.VERIFICATION.LINT.1.4 |
| VERIFICATION | defaults | 4 | VERIFICATION.LINT.3 | DEFENSE | dataflow | retargeted: PIG-JS.VERIFICATION.LINT.3 dataflow PIG-JS.DEFENSE.INJECTION.1 |
| VERIFICATION | defaults | 5 | VERIFICATION.TESTS.2 | SUBSET | refines | retargeted: PIG-JS.VERIFICATION.TESTS.2 refines PIG-JS.SUBSET.CONVERSION.1 |
| VERIFICATION | defaults | 6 | VERIFICATION.LINT.2 | DEPENDENCIES | requires | retargeted: PIG-JS.VERIFICATION.LINT.2 requires PIG-JS.DEPENDENCIES.INSTALL.1 |
| VERIFICATION | philosophy | 1 | VERIFICATION.ENFORCEMENT | DEPENDENCIES | requires | retargeted: VERIFICATION.ENFORCEMENT requires DEPENDENCIES.CHANGE.1 |
| VERIFICATION | philosophy | 2 | VERIFICATION.STATIC_BASELINE.1 | SUBSET | dataflow | flipped: SUBSET dataflow VERIFICATION.STATIC_BASELINE.1 |
| RUNTIME | defaults | 1 | STRUCTURE | PIG-JS.RUNTIME.MEASURE.2 | requires | retargeted: PIG-JS.STRUCTURE.LOADING.6 requires PIG-JS.RUNTIME.MEASURE.2 |
| RUNTIME | defaults | 2 | RUNTIME.MEASURE.3 | CONTROL | refines | retargeted: PIG-JS.RUNTIME.MEASURE.3 refines PIG-JS.CONTROL.PROMISES.6 |
| RUNTIME | defaults | 3 | RUNTIME.DIAGNOSE.2 | CONTROL | dataflow | retargeted: PIG-JS.RUNTIME.DIAGNOSE.2 dataflow PIG-JS.CONTROL.SCHEDULING.2 |
| RUNTIME | defaults | 4 | RUNTIME.MEMORY.4 | DEFENSE | requires | retargeted: PIG-JS.RUNTIME.MEMORY.4 requires PIG-JS.DEFENSE.HOST.2 |
| RUNTIME | defaults | 5 | RUNTIME.MEMORY.5 | SUBSET | refines | retargeted: PIG-JS.RUNTIME.MEMORY.5 refines PIG-JS.SUBSET.EVOLUTION |
| RUNTIME | defaults | 6 | RUNTIME.MEMORY.2 | CONTROL | requires | retargeted: PIG-JS.RUNTIME.MEMORY.2 requires PIG-JS.CONTROL.ERRORS.4 |

Links added at integration, not proposed by a branch: CONTRACTS.STATIC.2 refines VERIFICATION.STATIC_BASELINE.3; DEFENSE.HOST.1 requires CONTROL.SCHEDULING; PIG-JS.CONTROL.PROCESS.2 refines js-philosophy:CONTROL.LIFECYCLE.

Notes on individual resolutions:

- `CONTROL.FAILURE` requires `SUBSET.FAILURE`: direction: the sentence makes CONTROL the dependent
- `SUBSET.VISIBLE` requires `CONTRACTS.BOUNDARY`: sentence sharpened to a dependency
- `DEFENSE` requires `CONTRACTS.BOUNDARY.1`: direction: the sentence makes DEFENSE the dependent
- `DEFENSE.INJECTION` refines `CONTRACTS.BOUNDARY.2`: direction: the allowlist stance specializes positive validation
- `SUBSET` dataflow `VERIFICATION.STATIC_BASELINE.1`: direction: SUBSET produces the rules the linter consumes
- `CONTRACTS.STATIC.2` refines `VERIFICATION.STATIC_BASELINE.3`: added at integration (P5 link between two statements of one idea)
- `DEFENSE.HOST.1` requires `CONTROL.SCHEDULING`: added at integration (P5 link, the premise is not restated)
- `PIG-JS.STRUCTURE.FORMAT.1` requires `PIG-JS.SUBSET.STRICTNESS.2`: direction: STRUCTURE builds on SUBSET
- `PIG-JS.STRUCTURE.LOADING.1` refines `PIG-JS.SUBSET.STRICTNESS.2`: P5 link: the run-once fact is held once
- `PIG-JS.STRUCTURE.SURFACE.3` requires `PIG-JS.SUBSET.MUTATION.1`: freeze hub: three nodes share the shallow-freeze fact, which is held once at MUTATION.1
- `PIG-JS.DEFENSE.PROTOTYPE.3` requires `PIG-JS.SUBSET.MUTATION.1`: freeze hub
- `PIG-JS.DEFENSE.PROTOTYPE.1` requires `PIG-JS.SUBSET.OBJECTS.6`: P5 merge: the rule lives on OBJECTS.6
- `PIG-JS.CONTRACTS.LAYER.3` requires `PIG-JS.VERIFICATION.LINT.2`: VERIFICATION defaults hold no tool-neutral gate node; LINT.2 (exit status blocks CI) stands in
- `PIG-JS.CONTRACTS.LAYER.4` refines `PIG-JS.SUBSET.EVOLUTION`: sentence corrected: the proposal said SUBSET lists enum and namespaces, it does not
- `PIG-JS.CONTRACTS.BOUNDARY.1` dataflow `PIG-JS.DEFENSE.PROTOTYPE.2`: type refines -> dataflow
- `PIG-JS.CONTRACTS.BOUNDARY.2` dataflow `PIG-JS.DEFENSE.PROTOTYPE.1`: type requires -> dataflow
- `PIG-JS.CONTRACTS.BOUNDARY.3` refines `PIG-JS.DEFENSE.PROTOTYPE.1`: the proposal named a DEFENSE injection class that DEFENSE does not list
- `PIG-JS.DEFENSE.INJECTION` requires `PIG-JS.CONTRACTS.BOUNDARY.4`: split in two: INJECTION and HOST.4
- `PIG-JS.CONTROL.BOUNDS.1` requires `PIG-JS.CONTRACTS.SIGNATURE`: retargeted from STRUCTURE: the API-shape cluster (STRUCT-C48 to C52) was routed to CONTRACTS.SIGNATURE
- `PIG-JS.STRUCTURE.LOADING.5` requires `PIG-JS.VERIFICATION.LINT.2`: coarse target: VERIFICATION defaults have no build-gate node
- `PIG-JS.STRUCTURE.LOADING.6` requires `PIG-JS.RUNTIME.MEASURE.2`: the proposal named no STRUCTURE node; LOADING.6 is the speed-motivated one
- `PIG-JS.DEFENSE.SECRETS.5` requires `PIG-JS.VERIFICATION.LINT.2`: coarse target: VERIFICATION defaults have no secret-scan gate node
- `PIG-JS.DEFENSE.DOM.6` dataflow `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE`: P5 link: framework security facts held once, in DEFENSE
- `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` requires `PIG-JS.DEFENSE.DOM.6`: P5 link: framework security facts held once, in DEFENSE
- `PIG-JS.DEPENDENCIES.UPDATE.3` dataflow `PIG-JS.VERIFICATION.LINT.2`: coarse target: VERIFICATION defaults have no tool-neutral gate node
- `PIG-JS.DEFENSE.HOST.1` refines `js-philosophy:DEPENDENCIES.TRUST.2`: no defaults node holds the trust principle; target is the philosophy node
- `PIG-JS.DEPENDENCIES.SCREEN.1` requires `js-philosophy:VERIFICATION.ENFORCEMENT`: Scorecard checks overlap the merge gate
- `PIG-JS.CONTROL.PROCESS.2` refines `js-philosophy:CONTROL.LIFECYCLE`: added at integration (P5 merge link)
