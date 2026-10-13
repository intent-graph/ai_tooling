# J1_ownership: judge records (OWNERSHIP, 29 L3 nodes, 6 L2 nodes, 1 L1 node)

Binding: MD-01 (best, not average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-05 (scope). Positions are numbered as in `02_skeleton/branches/OWNERSHIP/branch.md`. Row ids Lnnn are ledger ids; REG-nnn are source register ids; REG-181 is the maintainer's codified practice (MAINT, not citable). No decided unit precedes J1, so there is no settled input.

Forces of the branch: control, time to value, cost of ownership over time, exit risk, security exposure, fit.

Certainty words: grounded = named sources support the decision; inferred = follows from them; open = what is missing is stated.

---

## OWNERSHIP (L1)

Intent: For each capability, the team writes it, adopts it or rents it only when a stated reason outweighs the ongoing cost, and keeps the choice reversible in proportion to what it would cost to be wrong.
Rolled-up decision: every external capability enters through a recorded, per-need decision; once in, it is declared, locked, watched and updated as a managed liability; the effect of each dependency is bounded and its exit is priced, not assumed; a rented service is chosen on commitments, exit terms, contract and vendor posture; the licence obligations are known before the code is used. This is a roll-up of the six L2 records below; it states no fact of its own (MD-03).
Certainty: grounded for the lifecycle and licence mechanics and the rented-service checks (consensus rows); inferred for the proportionality scaling (criticality, switching likelihood), which no source states as a formula.
Constraints: no dependency, layer or service is adopted without a recorded reason; no adopted artifact is installed from anything but the lock; no rented service is adopted without a tested way out proportional to its criticality.
Links: realized by `EVOLUTION` (decommissioning, technology count), `CHANGE_FLOW`, `TRANSVERSE.CONFIG`.
Flags: none; F1 to F6 are settled by the final pass (see `## Final pass applied`).

---

## OWNERSHIP.STANCE (L2): Necessity and Default Stance

Intent: Whether a capability is needed at all, and, absent a specific reason, whether to write, adopt or rent; what a new layer or dependency must earn.
Rolled-up decision: the default is not to add; a dependency or layer is added when a stated reason outweighs its lasting cost; write, adopt or rent is decided per need on coreness, security criticality and size; carried code stays tied to its origin; build for today's need and make change cheap, except where a structural choice is costly to reverse.
Certainty: grounded for the cost-of-ownership default; inferred for the reconciliation on `STANCE.4`.
Links: children `STANCE.1` to `STANCE.4`.

### OWNERSHIP.STANCE.1 What a New Dependency or Layer Must Earn

Intent: A new dependency or layer is justified by necessity before its quality is looked at, and the justification outweighs its lasting cost.
Rows: L001, L037, L308.
1. Decision: Justify a new dependency or layer by a stated reason before assessing its quality, and treat it as a lasting liability (maintenance, upgrades, security exposure, platform shifts), not a one-time saving; the default is not to add it, and a layer is created only when at least one strong reason outweighs its cost (for example reuse across consumers, hiding internals behind a business-level verb, keeping a query tunable by its owner, enforcing integrity once). Outcome: every added moving part has a recorded reason that can be tested later.
2. Grounds: L001 and L037 (consensus; REG-003, REG-011, REG-012): the cost is attack surface and ownership beyond the effort saved. L308 (MAINT, REG-181) states the same test for layers and agrees with public practice (build-versus-not discipline); it is the best formulation for layers because it names the reasons that count.
3. Positions: P1 justify by necessity first (cost of ownership, security exposure). P2 MAINT: create a layer only against a strong reason; the row's competing position is to default to the layer (database-centric; fit, a single place for logic).
4. Rejected: default to the layer: no source in the branch argues its cost is lower; it would be best only where the layer's reasons (integrity once, reuse) already hold, which is the P2 condition, not a default.
5. Context: none.
6. Certainty: grounded for the dependency half (L001, L037); the layer reasons are the maintainer's formulation (L308), inferred as general.
7. Flags: none.
Constraints: the reason is written before the quality evaluation starts (see `SELECTION.1`).
Links: related `SELECTION.2` (L024), `SELECTION.1` (L1537).

### OWNERSHIP.STANCE.2 Write, Adopt or Rent per Need

Intent: Each need is decided per need between writing, adopting a component, using a platform built-in or renting a service; no default either way.
Rows: L002, L040, L310.
1. Decision: Decide each need explicitly: a capability the platform already in use provides (a built-in) is preferred over both new code and a new dependency when it meets the stated need, because it adds no new owner (the lowest-ownership case of the cost test); a vetted component or service is preferred for complex or security-critical domains (cryptography, protocols) and for non-core, well-understood functions; write it in-house only for core functions that carry competitive advantage, for needs no third-party option meets better, and for small stable functionality whose dependency cost exceeds its code cost. Renting is adoption with the same cost test plus the control cost, so core functions are built or kept under control and non-core ones are rented. When custom code is chosen over a built-in, record the missing capability and revisit if the need shrinks to what the built-in does. Outcome: each need has a recorded basis for its ownership mode.
2. Grounds: L002 (SRC-C02 contested, ADOPT-C02 majority, ADOPT-C03 consensus; NIST PW.4.2, Google SWE ch. 21, REG-004, REG-011, REG-012, REG-020, REG-027): P1, P2 and P3 each win under a stated condition and P4 is the source's own reconciliation, so the decision is a conditional, not an average. L040 (REG-027, REG-026): rent non-core. L310 (MAINT, REG-181): the built-in rule is the lowest-ownership case of the same rule and the maintainer's custom exception (granularity, per-entry strategies) is the stated condition; coverage check shows no contradiction with L002.
3. Positions: P1 reuse by default (security, speed, cost, correctness). P2 minimise dependencies (cost of ownership, control, exit risk). P3 build the core (control, differentiation). P4 build only what third parties cannot better meet. P5 rent: (a) non-core only (control, differentiation); (b) rent broadly and accept lock-in (speed, cost). P6 MAINT built-in over custom.
4. Rejected: reuse as an unconditional default and minimise as an unconditional default: each is best only under its condition (security-critical or non-core, versus small stable long-lived); rent broadly (P5b): best where the lock-in pay-off is commensurate, handled by `CONTAINMENT.1`.
5. Context: CORENESS (L002 ADOPT-C02 b, L040): whether the function carries competitive advantage moves it from adopt or rent toward write.
6. Certainty: grounded for L002 and L310; inferred for the built-in preference (from L001 and L037, cost of ownership and consensus; the maintainer's L310 agrees) and for renting (L040 inferred: sources address SaaS only through outsourcing).
7. Flags: none.
Constraints: custom code chosen over a built-in or a vetted component carries a recorded reason.
Links: related `STANCE.3`, `SERVICES.3` (L1112 see also L040).

### OWNERSHIP.STANCE.3 Bringing Code Inside: Copy, Vendor, Upstream

Intent: When needed code is copied or vendored rather than depended on, and how carried code stays tied to its origin.
Rows: L070, L071, L072.
1. Decision: Copy or reimplement only a tiny used surface of non-security-critical code; for cryptography and protocols depend on the vetted component even then. Consume from a registry with a lock by default; vendor (or use a monorepo) when the team has the tooling to carry it or needs the copy for availability (`LIFECYCLE.4`). Whatever is carried keeps a record of its origin and version, and fixes go upstream instead of living in a private fork. Outcome: carried code can be traced to its source and does not silently diverge from upstream fixes.
2. Grounds: L070 (REG-012 for the tiny surface, REG-004 PW.4 for cryptography; the opposing arguments, lost upstream fixes REG-011, are inferred, so the crypto exception is the safer side where the row is contested). L071 (REG-011 monorepo; REG-031, REG-037 registry with lock). L072 (majority; REG-011, REG-035, REG-040): no opposing position recorded.
3. Positions: P1 copy a tiny surface (attack surface, exit risk). P2 depend even then (correctness, upstream fixes). P3 vendor or monorepo (control, visibility). P4 registry with lock (cost of ownership). P5 upstream, no private forks.
4. Rejected: copy everywhere: loses upstream fixes beyond the tiny, non-critical case; vendor as default: needs tooling and large-codebase scale (condition stated); P2 as absolute: cost of a dependency for a handful of lines exceeds the saving (REG-012).
5. Context: none beyond the conditions above (used surface size, security criticality, tooling), which are in the decision.
6. Certainty: grounded for P1 and P5; inferred for the crypto exception's scope and the vendoring condition.
7. Flags: none.
Links: related `STANCE.2`, `LIFECYCLE.4`.

### OWNERSHIP.STANCE.4 Speculative Building and Probable Use

Intent: Build for today's needs, make change cheap, and spend design effort on probable future use only where a structural choice is costly to reverse.
Rows: L038, L330, L1208.
1. Decision: Do not build functionality, or a substitute for a dependency, for presumed future needs; invest instead in making the software easy to modify (tests, refactoring, continuous delivery). Where a structural choice is costly to reverse (the shape of a very large stored data set), the probable use is part of today's requirement and is weighed in the choice, without speculative optimisation. Outcome: the cost of change stays low where it can, and a costly-to-reverse structure is not chosen blind.
2. Grounds: L038 (consensus; REG-026, REG-034: four distinct costs), L1208 (consensus; REG-034: same claim plus the enabling investment). L330 (MAINT, REG-181) contradicts L038 on its face (coverage check section 5), but L330 states the condition itself (build only for today wins when change is cheap; probable use wins when changes to structure are costly, a very large relational store); the two are one rule with that reversibility condition, not a blend. The reconciliation rests on L330's own condition only.
3. Positions: P1 no speculative functionality (speed, cost). P2 MAINT: design for probable use (reversibility; large relational store). P3 no presumed features, invest in modifiability (reversibility, cost).
4. Rejected: P2 as a general rule: speculation is usually wrong and carries complexity (REG-034); it is the best when reversal is costly, which the decision states. P1 as stated without the enabling investment: leaves change expensive.
5. Context: COST_OF_STRUCTURAL_CHANGE moves the answer: cheap change, build for today; costly change, weigh probable use.
6. Certainty: inferred for the reconciliation (the maintainer's condition is one source); grounded for the two halves taken singly.
7. Flags: none.
Links: `CONSTRUCTION.DESIGN` points here (L330), `EVOLUTION.INCREMENTAL`.

---

## OWNERSHIP.SELECTION (L2): Finding, Profiling and Selecting

Intent: How a candidate library, tool or technology is found, profiled and chosen, and how deep the vetting goes.
Rolled-up decision: a candidate is judged against explicit criteria in its intended context and the reason is recorded; fit comes first; novelty is spent sparingly; health, weight and provenance signals are inputs to judgment, weighted by how critical and replaceable the component is; vetting depth scales with criticality and exposure.
Certainty: grounded for the criteria; inferred for the scaling.
Links: children `SELECTION.1` to `SELECTION.6`.

### OWNERSHIP.SELECTION.1 Evaluation Process and Admission Gate

Intent: Every dependency is evaluated against explicit criteria in context, recorded, and enters through a gate.
Rows: L003, L004, L005, L028, L029, L030, L042, L1537, L1539.
1. Decision: Judge each candidate against an explicit written criteria set (design and documentation, code quality, tests that run and pass, bug handling, maintenance, usage, security exposure and secure defaults, licence, transitive dependencies) in the context of its intended use, and repeat when the use changes substantially. Record the reason for each non-trivial selection (alternatives, criteria, accepted risks) where later maintainers find it. A dependency enters only through a gate: a central sanctioned list with provenance data where many teams or regulated or high-criticality software are involved; otherwise a reviewed proposal with light visibility. Aggregators serve discovery and first screening only. Outcome: every dependency has a recorded, reviewable basis and a known introducer.
2. Grounds: L003, L004, L042 (consensus; REG-003, REG-004, REG-011, REG-012): no competing position. L005 (one study REG-017, recommendation inferred) and L029 (majority; REG-004, REG-013, REG-017): written selection. L028 (REG-004, REG-011, REG-013): the two admission modes are each best under a stated condition. L030 (majority): aggregators change or stop, so they never substitute for criteria. L1537, L1539 (judged in the JavaScript guideline, node intents, no own claim): consistent, adopted as framing only.
3. Positions: P1 explicit criteria in context. P2 systematic, written selection. P3 written reason per selection. P4 (a) central sanctioned list (security, control, consistency); (b) team choice (speed, cognitive load); a reviewed proposal as a third mode. P5 aggregators for discovery. P6 prior JavaScript framing.
4. Rejected: team choice with light visibility is best for small teams with low regulation; central list best for regulated or high-criticality contexts and many teams; both are kept as the stated condition. Ad hoc selection: rejected by L005's evidence.
5. Context: REGULATION_AND_SCALE moves the gate (above).
6. Certainty: grounded for P1; inferred for P2 and P3 (single study, synthesis).
7. Flags: none.
Constraints: the written reason is stored as a decision record (`EVOLUTION.DECISIONS`).
Links: related `STANCE.1`.

### OWNERSHIP.SELECTION.2 Fit, Maturity and Novelty

Intent: A candidate fits the real requirements; the default is proven technology and novelty is spent only where it pays.
Rows: L023, L024, L025, L312, L1227, L1228, L1230.
1. Decision: Select for fit to the actual requirements and constraints, not features or fashion (a core technology is chosen by problem fit, not dogma). Default to proven technology the team already operates, because its failure modes are known; spend novelty only where the business needs it (what differentiates the product, not infrastructure) and the existing tool demonstrably cannot solve the problem, after documenting why. An organisation with standing capacity for experiments and tolerance for churn may run a standing trial ring (assess, trial, adopt, hold) and spend more novelty, still through the staged, reversible entry; a small, operations-heavy or long-lived system stays at the default. When novelty is spent, introduce it in stages (trial in limited production use, then adopt or hold) with an exit or migration plan, and weigh its perpetual operating cost rather than the convenience of adoption. Outcome: new technology enters rarely, deliberately, and reversibly.
2. Grounds: L023 (consensus; REG-003, REG-013, REG-017), L312 (MAINT, public practice consensus, agrees with L023). L024, L1227, L1228 (REG-004, REG-011, REG-013, REG-1022, REG-1132): the boring-first default is supported by cost-of-ownership arguments and REG-013 itself admits the exit-plan exception. The staged mechanism (L024 b, L025; REG-013, REG-015 Thoughtworks Radar) does not oppose the default; it is the form novelty takes when spent. REG-013 is cited only for documenting why existing tools cannot solve the need and for the commitment to migrate old functionality to the new system; that REG-013 admits an exit plan from the new tool is not supported (the page says to commit to migrating). A reversible entry (stages, exit path) is inferred from the reversibility force of P2 and P3. L1230 (majority; REG-1022): perpetual cost.
3. Positions: P1 fit. P2 boring first (cognitive load, operational cost, reversibility). P3 staged novelty (learning, speed through better tools). P4 weigh perpetual cost, talk to others.
4. Rejected: standing assess/trial/adopt rings as the default for every team: best where capacity for experiments and tolerance for churn exist (stated as condition); the row (L025) notes no source opposes it, but L024 a discourages novelty at all, so the ring practice is kept as the how, not the default.
5. Context: EXPERIMENT_CAPACITY: organisations with capacity for experiments may run standing rings and spend more novelty; small, operations-heavy or long-lived systems stay at the default.
6. Certainty: grounded (T2 and T3 sources, aligned on cost); the staged-versus-boring reconciliation is inferred.
7. Flags: none.
Links: related `STANCE.1`; paradigm half of L312 is held in `CONSTRUCTION.PARADIGM`.

### OWNERSHIP.SELECTION.3 Project Health and Compatibility Signals

Intent: Which observable signs of a candidate's health and stability count, and how much weight each carries.
Rows: L006, L007, L008, L011, L014, L015, L016, L017, L018, L019, L041.
1. Decision: Treat health signals as inputs to judgment, never as the verdict: recent commits and releases within about twelve months and visible communication; responsiveness (open bugs, resolution speed, security backports or long-term-support versions); a vulnerability-disclosure policy and reporting channel; the candidate's compatibility promise (none, source, binary, automated migration), because it sets the cost of every update; interfaces stable and secure by default. Require several maintainers from several organisations when the component is on a critical path or hard to replace; tolerate a single-author project when it is small, stable and easily replaced or vendorable; a single-maintainer component outside that case needs a recorded compensating reason or an exit plan (L007). A 0.x or alpha label is evidence of a weak stability promise to be checked against release history and compatibility policy, not an automatic reject. A popularity or aggregate score is a weak proxy and never proof of quality or fit. Outcome: health claims in a selection rest on observed signs weighed by criticality.
2. Grounds: L006, L041 (consensus; REG-001, REG-003, REG-011, REG-012, REG-017); L007 (contested; REG-001, REG-003, REG-012, REG-018): the two positions each win under the stated replaceability condition. L008, L011, L014, L015 (REG-001, REG-003, REG-011, REG-012): no competing position. L016 (OpenSSF REG-003): label guidance; the counter (many mature tools stay 0.x) is inferred, so the label is evidence, not a gate. L017 (Scorecard's own documentation says input not verdict, REG-001, REG-002), L018 (one study REG-016: process scores explain 9 to 12 percent of vulnerability outcomes, replication not checked), L019 (REG-003, REG-011, REG-012, REG-013, REG-017): all support input-not-verdict.
3. Positions: P1 activity. P2 several maintainers (exit risk, security, continuity). P3 tolerate small (cost, fit). P4 responsiveness and disclosure. P5 compatibility promise. P6 (a) avoid 0.x (correctness, reversibility); (b) labels not uniform (fit). P7 (a) score as input; (b) score as a gate (consistency, speed at scale). P8 (a) popularity weak proxy; (b) popularity as hype.
4. Rejected: P6a as a rule: no source read shows labels are uniform, and mature tools stay 0.x; best as a prompt to check, not a gate. P7b gate on score: not argued in any source read, and the low explanatory power (L018) undermines it; it would be best only at a scale where per-package review is impossible, and then as a screen. P2 as a universal requirement: best only when the component is critical or hard to replace.
5. Context: REPLACEABILITY moves the maintainer-diversity requirement (above).
6. Certainty: grounded for P1, P4, P5, P7a, P8a; inferred for the 0.x stance and the screen-at-scale remark.
7. Flags: none.
Links: related `LIFECYCLE.2` (L014 see also L059).

### OWNERSHIP.SELECTION.4 Dependency Weight

Intent: What a candidate drags in with it: indirect dependencies, tiny packages and the trust surface of its registry.
Rows: L020, L021, L022.
1. Decision: Count transitive dependencies as part of the cost and prefer candidates with few unnecessary indirect ones. Inline trivial functionality the team can own in a few lines instead of taking a package for it; take a small package when it carries non-trivial, tested behaviour. Count the registry's maintainer-account concentration as part of the exposure. Outcome: the trust surface of a selection is measured, not assumed.
2. Grounds: L020 (consensus; REG-003, REG-012, REG-018, REG-019). L021 (Kula et al., Pike; REG-018, REG-019, REG-020): the case for avoiding trivial packages rests on supply-chain exposure evidence; the counter (reuse and tested readability) is open, not read in a source. L022 (npm evidence; REG-003, REG-005, REG-018): the registry-wide principle is inferred.
3. Positions: P1 count transitive. P2 (a) avoid or inline trivial packages (control, security, cost); (b) small shared packages (reuse, speed). P3 registry concentration.
4. Rejected: P2b: best where reuse of a tested small package avoids a real error risk (cryptographic or parsing helpers), but no source argues it as a rule.
5. Context: none.
6. Certainty: grounded for P1; inferred for generalisation beyond the npm evidence (L021, L022).
7. Flags: none.
Stack pointers: L021, L022 (npm evidence, generalisable).

### OWNERSHIP.SELECTION.5 Authenticity, Provenance and Known Vulnerabilities at Adoption

Intent: What is checked before adoption about a candidate's identity, origin and known flaws.
Rows: L010, L012, L013, L1056, L1541.
1. Decision: Before adoption, reject or defer a candidate whose current version has known unfixed vulnerabilities for the intended deployment; verify authenticity (official source over a secure link, signed packages where available, the name checked against look-alikes and compromised forks, and, for a name that was generated or suggested, that it resolves to the intended vetted package); and obtain provenance per component (SBOM, source composition, signatures, signed releases, hosting-platform protections) and apply integrity checks. Provenance is required for high-criticality use; elsewhere it is a preferred selection signal. Where binary provenance cannot be confirmed, the rebuild rule of `LIFECYCLE.4` applies. Outcome: what is adopted is the thing that was vetted.
2. Grounds: L010 (consensus; REG-001, REG-003, REG-004, REG-005), L012 (REG-001, REG-003, REG-004, REG-005, REG-025), L1056 (majority; REG-1035, REG-1045), L1541 (JavaScript guideline, three T1 sources REG-1555, REG-003, REG-1556): no competing position. L013 (majority; REG-001, REG-004, REG-035): (a) require for all (security; best for high criticality) and (b) preferred signal (cost; ecosystem coverage partial, inferred) are each stated with a condition.
3. Positions: P1 reject known unfixed vulnerabilities. P2 verify authenticity and name resolution. P3 (a) require provenance (security); (b) preferred signal (cost).
4. Rejected: requiring provenance for every component: best only at high criticality, because ecosystem coverage is partial.
5. Context: criticality moves provenance from preferred to required (above).
6. Certainty: grounded for P1 and P2; inferred for the ecosystem-coverage claim.
7. Flags: none.
Links: `LIFECYCLE.4` (channels and rebuild), `LIFECYCLE.5` (ongoing check).

### OWNERSHIP.SELECTION.6 Vetting Depth and Delegated Audit

Intent: How deep hands-on vetting of a candidate goes and who does it.
Rows: L027, L077, L1540, L1542.
1. Decision: Scale vetting depth to criticality and exposure, judging risk as cost times probability of each bad outcome: metadata and scores for low-criticality replaceable parts; for components that handle untrusted input, credentials or cryptography, run the candidate's tests, sandboxed behaviour tests and code review for install scripts, exfiltration, obfuscation and unfinished security gaps. Reuse audits by trusted organisations and review only version differences instead of auditing everything. Test a candidate in isolation for unexpected indirect dependencies, and treat example code shipped with a package as untrusted until reviewed. Outcome: audit effort goes where the damage would be.
2. Grounds: L027 (contested SRC-C27, consensus ADOPT-C12; REG-003, REG-004, REG-012, REG-040; scaling rule inferred) with the two depths each best under a stated condition. L077 (majority; REG-004, REG-038). L1540, L1542 (single-source, REG-003, REG-1556; JavaScript guideline, adopted as practice since consistent with L027).
3. Positions: P1 (a) metadata only; (b) deep review. P2 delegate audit. P3 isolation test and untrusted examples.
4. Rejected: full manual audit of every dependency: too much work (L077); best never as a rule, only for P1b components.
5. Context: CRITICALITY_AND_EXPOSURE (above).
6. Certainty: inferred (scaling rule), grounded for the individual checks.
7. Flags: none.
Stack pointers: L077 (cargo-vet), L1540, L1542.

---

## OWNERSHIP.LIFECYCLE (L2): Dependency Lifecycle

Intent: How an adopted dependency is declared, locked, obtained, updated, inventoried and watched over its life.
Rolled-up decision: every environment gets the same verified artifacts from a complete manifest and a lock; versions are constrained according to whether the artifact is a deployable or a library; updates are frequent, small, tested and automated with security fixes urgent; artifacts come through controlled channels with an answer to upstream disappearance; the team knows what it depends on and watches it until end of life.
Certainty: grounded (consensus rows), with the cooldown and the range-edge testing for library consumers inferred.
Links: children `LIFECYCLE.1` to `LIFECYCLE.5`.

### OWNERSHIP.LIFECYCLE.1 Declare and Lock

Intent: Every dependency is declared completely and exactly and locked so every environment obtains the same artifacts.
Rows: L043, L044, L045, L046, L1241.
1. Decision: Declare all dependencies completely and exactly in a manifest and run in an isolated environment, never relying on implicitly installed packages. Commit a lock recording the exact resolved tree, direct and transitive; install in CI and production from the lock only and fail when lock and manifest disagree; verify artifacts by a cryptographic hash recorded in the lock, covering transitive dependencies, with a require-hashes mode in deploys where the tool supports it. Outcome: what runs is what was tested, on every machine.
2. Grounds: L043 (consensus; REG-014), L044 (consensus; REG-031, REG-037), L045 (REG-028, REG-031; the guarantee is grounded, the generalisation inferred), L046 and L1241 (REG-025, REG-031, REG-032, REG-037, REG-1135). No competing position in any row.
3. Positions: P1 complete manifest. P2 committed lock. P3 install from lock only. P4 hash verification.
4. Rejected: none competing.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: new developer needs only the runtime, the dependency manager and one command; lock-versus-manifest mismatch fails the build.
Stack pointers: named tools in L043 to L046.

### OWNERSHIP.LIFECYCLE.2 Version Constraints and Resolution

Intent: Versions are constrained and resolved so the tested set is what is installed, and a version number is trusted only as far as tests bear it out.
Rows: L047, L049, L050, L051, L059, L061.
1. Decision: Applications and services nobody else installs pin all dependency types exactly (with an update bot so each bump is a reviewable change); libraries consumed by others declare ranges and test the range edges in their own CI; a lock never replaces constraints, so the manifest range still excludes known-broken versions. Treat a version number as an estimate of compatibility and tests as the evidence (Hyrum's Law): trust the range more as the API is narrow and well declared. The guarantee does not depend on the resolution rule: whichever rule the ecosystem's tool applies, a version changes only through an explicit, reviewable change to the lock. The rule matters only where ranges are resolved without the team's lock, that is for a library's consumers: there the library tests both the lowest and the newest versions its ranges admit, so a consumer resolving by either rule (minimal version selection or newest compatible) gets a tested set. A diamond conflict is resolved by moving versions forward or backward or patching locally. Outcome: the installed set equals the tested set and drift is visible.
2. Grounds: L049 (majority; REG-001, REG-028, REG-031): the lock-only alternative only delays a bad range (REG-028). L050 (majority; REG-011, REG-028): exact pins in libraries are defended by no source (open). L051 (consensus; REG-028). L059 (REG-011, REG-030): (b) is the stronger argument and (a) stays as a condition. L047 (REG-011, REG-028, REG-031, REG-037; both resolution rules, each with its condition), L061 (consensus; REG-011); the resolution-rule neutrality follows from L047, L049 and L051 and from the node's own test of the range edges.
3. Positions: P1 (a) minimal version selection (correctness); (b) newest-compatible plus lock (speed). P2 (a) exact pins plus bot (confidence, security); (b) ranges plus lock (low noise). P3 libraries declare ranges. P4 lock does not replace constraints. P5 (a) SemVer is a usable contract (speed); (b) SemVer is an estimate, tests the evidence. P6 diamond resolution.
4. Rejected: P2b: best when review capacity is scarce, but it only delays a bad range. P5a: best when the API is narrow and well declared, stated as the condition. Exact pins in libraries: no source defends it. Ranking the two resolution rules: the rule comes with the ecosystem, not from the team, and testing both range edges makes either safe.
5. Context: ARTIFACT_KIND (deployable versus library) moves pin versus range.
6. Certainty: grounded for pins, ranges and L051; inferred for the test-the-edges half and for the resolution-rule neutrality (the lock, not the rule, carries the guarantee).
7. Flags: none.
Stack pointers: L047 (Go MVS), L049 (npm).
Links: related `SELECTION.3` (L059 see also L014).

### OWNERSHIP.LIFECYCLE.3 Updating

Intent: How and how fast an adopted dependency moves to newer versions, and how a compromise is answered.
Rows: L052, L053, L054, L055, L056, L057, L058, L1543, L1544.
1. Decision: Update in small, frequent, automated, grouped increments, each gated by the project's own tests (including integration tests for the team's usage) and release-note or diff review, and deployed through staged rollouts; where verification is weak or deployment costly, update on need (security fixes, end of life, a needed change) rather than routinely, and record the weak verification as debt to repay (`EVOLUTION.DEBT`): the low cadence is a consequence of missing tests, never a policy. Apply fixes for known vulnerabilities urgently, bypassing any scheduled delay, and keep security updates separate from feature updates. Hold routine (non-security) updates of deployables for a release-age cooldown of at least seven days, never for security fixes; the cooldown complements lock, hashes and review and replaces none of them. Its benefit rests on one analysis of ten attacks (eight of ten malicious versions removed within a week, nine within fourteen days) and is otherwise unmeasured: inferred. After a worm-style supply-chain compromise, treat every developer credential as exposed, review the lockfiles and pin to versions published before the incident; the revocation, rotation and investigation of the exposed credentials are held by `TRANSVERSE.CONFIG.6`. Outcome: updates arrive fast enough to carry fixes and slowly enough to be vetted, and the pipeline detects a bad one.
2. Grounds: L052 (REG-001, REG-011, REG-012, REG-025, REG-035): small frequent updates win when tests are trustworthy; "update only when needed" wins when verification is weak, which is a condition on the tests, so the decision fixes the cause. L053 (consensus; REG-001, REG-012, REG-029, REG-035, REG-043), L055 (consensus), L056 (consensus; REG-012), L057 (consensus; REG-025), L1543 (majority). L054 (contested; REG-029, REG-035, REG-036, REG-043): the cooldown costs only the staleness of fixes that ship as ordinary releases, which the security bypass removes; update-immediately wins when most updates are security fixes. L058 (REG-011, REG-028, REG-030). L1544 (CISA, single T2 source REG-1558; JavaScript guideline). Final pass: the cooldown length rests on REG-036 (recommends seven days minimum, "not a panacea") and L1543 (benefit unmeasured); the interim cadence follows L052's own condition ("strengthen first" had no row and cannot happen at once).
3. Positions: P1 (a) frequent automated (security, cost); (b) only when needed (control, stability). P2 automate and group. P3 urgent security fixes. P4 (a) cooldown; (b) immediate. P5 review and re-test. P6 staged rollout. P7 (a) live at head (speed of feedback); (b) pinned SemVer (control). P8 post-compromise response.
4. Rejected: P1b: best while verification is weak or deployment costly and exposure is lower than the risk of change, as a temporary state (now in the Decision). P4b: best when most updates are security fixes or the pipeline detects malicious content itself. P7a: best in a monorepo with provider-run downstream tests at organisation scale.
5. Context: TEST_TRUST_AND_EXPOSURE moves the cadence and the cooldown (above).
6. Certainty: grounded for P2, P3, P5, P6; inferred for the cooldown (one T3 analysis of 10 attacks REG-036, vendor figures; stated as inferred in the Decision), for the interim cadence under weak verification and for the post-compromise trigger (single source).
7. Flags: none.
Stack pointers: L054, L055, L1543, L1544 (named tools and ecosystem).
Links: related `LIFECYCLE.1`; credential rotation after a compromise: see `TRANSVERSE.CONFIG.6`.

### OWNERSHIP.LIFECYCLE.4 Channels, Mirrors and Supply-Chain Integrity

Intent: Through which channels artifacts are obtained, what is kept as a fallback, and how the supply chain of the team's own tooling and packages is protected.
Rows: L062, L064, L065, L076, L1074, L1243, L1545, L263.
1. Decision: Obtain artifacts only through controlled, trusted channels (authenticity checks are in `SELECTION.5`), with lock and hashes. Add an internal repository or mirror of sanctioned components in larger or regulated organisations and for production-critical builds, which also covers upstream unavailability; a small team may pull from the public registry with lock and hashes. Apply provenance verification recursively and address a removed upstream separately by a mirror, cache or vendored copy. Rebuild every deployed open-source artifact from source in the team's own infrastructure only for critical infrastructure or supply-chain-targeted organisations, and rebuild from verified source any artifact whose binary provenance cannot be confirmed (this is the single statement of the rebuild rule). The automation's own tools, plugins and descriptors, and build tools and compilers, are pinned, vetted, changed only through audited change management and not auto-updated without review, while staying on versions that still receive security fixes. Two-factor authentication protects publishing accounts of any registry, and phishing-resistant multi-factor authentication protects developer accounts after compromises. Outcome: the supply chain of what is shipped, and of what builds it, is controlled and recoverable.
2. Grounds: L062 (REG-004, REG-031, REG-032, REG-035, REG-037) and L1243 (consensus; REG-025): the two channel modes are each best under an organisation-size condition. L064 (consensus; REG-022, REG-023). L065 (REG-031, REG-032, REG-035, REG-037): large engineering effort, so conditional. L076 (majority; REG-022, REG-035, REG-037). L1074 (majority; REG-1034, REG-1037; pinning rule inferred), L263 (majority; REG-004, REG-014, REG-178; the pinned versus up-to-date tension is inferred). L1545 (consensus; REG-1557, REG-1556, REG-1562, REG-1558; JavaScript guideline).
3. Positions: P1 (a) controlled channel with mirror (control, availability); (b) direct with lock and hashes (cost). P2 (a) rebuild everything (security, control); (b) prebuilt verified artifacts (cost). P3 provenance is recursive and does not address removal. P4 (a) cache, mirror or vendor (availability); (b) immutable public proxy (cost). P5 own tooling pinned. P6 publishing-account protection. P7 build tools pinned and changed under change management.
4. Rejected: P1b for larger or regulated organisations and production-critical builds; P2a for everyone else (large effort); P4b where the registry does guarantee immutability and builds are not production-critical.
5. Context: ORGANISATION_SIZE_AND_CRITICALITY (above).
6. Certainty: grounded for the channel rule and P3; inferred for the tooling pinning rule and the account-protection scope beyond the cited sources.
7. Flags: none.
Links: related `SELECTION.5`.

### OWNERSHIP.LIFECYCLE.5 Inventory, Watching and End of Life

Intent: The team knows what it depends on, hears of flaws and abandonment, and meets legal duties for it.
Rows: L009, L066, L067, L079, L1242.
1. Decision: Keep a machine-generated inventory (SBOM, direct and transitive, and where each is deployed) and scan it continuously against vulnerability databases for as long as the software is in service, with a triage and update plan. For each component confirm it is maintained and not at end of life and keep a plan for components that stop being maintained. Where law applies (for example the EU Cyber Resilience Act), due diligence on third-party components, an SBOM and reporting component vulnerabilities to their maintainers are duties, not options. Outcome: a disclosed flaw or an abandonment maps to the systems affected in hours, not days.
2. Grounds: L066 and L1242 (consensus; REG-001, REG-012, REG-025, REG-035, REG-042, REG-1135), L067 (consensus; REG-004, REG-024, REG-025), L009 (consensus; REG-004, REG-005, REG-011, REG-018), L079 (REG-040; primary text not read, wording inferred).
3. Positions: P1 inventory. P2 continuous monitoring. P3 end-of-life check. P4 legal duty.
4. Rejected: none competing.
5. Context: JURISDICTION: whether such a law applies (L079).
6. Certainty: grounded for P1 to P3; inferred for P4's exact wording.
7. Flags: none.
Links: related `SELECTION.5`.

---

## OWNERSHIP.CONTAINMENT (L2): Containment and Exit

Intent: How the effect of a dependency or external system is bounded and how the team leaves it.
Rolled-up decision: exit capability is bought only up to where insurance is cheaper than the expected loss (a tested exit for critical or regulated functions); a thin adapter isolates substitutable, volatile or foreign-model dependencies and none is built for stable standard ones; external systems are attached resources; third-party responses are untrusted and risky dependencies are isolated at runtime.
Certainty: grounded for the containment mechanisms; inferred for the proportionality.
Links: children `CONTAINMENT.1` to `CONTAINMENT.4`.

### OWNERSHIP.CONTAINMENT.1 How Much Reversibility to Buy

Intent: How much lock-in is acceptable and how much exit capability is worth paying for.
Rows: L073, L074, L075, L078.
1. Decision: Treat lock-in as a spectrum and price it by two quantities, the cost of switching and the likelihood of switching: accept lock-in when it buys a commensurate pay-off and reduce switching cost only to where the insurance is cheaper than the expected loss; portability beyond that point raises total cost. For a rented service define the exit path (data export, replacement candidate, contract notice) before adopting it, in proportion to its criticality, and require a tested exit and an alternative where regulation requires them (for example EU financial entities; primary text not read) and for critical functions, where the expected loss of being unable to leave exceeds the cost of testing the exit (inferred from the pricing rule above). Outcome: exit risk is a priced, recorded choice.
2. Grounds: L073 (majority; REG-011, REG-012, REG-026), L074 (REG-026), L075 (REG-012, REG-026, REG-039, REG-187, REG-216): (a) accept priced lock-in wins when switching likelihood is low and unique utility high; (b) minimise wins for long-lived systems and critical services; (c) a tested exit wins for regulated and critical functions: one rule with the likelihood and criticality as its condition. L078 (inferred, not assessable; REG-004, REG-026).
3. Positions: P1 spectrum. P2 two quantities. P3 (a) accept priced lock-in; (b) minimise by wrapping and open standards; (c) tested exit for regulated and critical. P4 exit path before adopting.
4. Rejected: minimise portability everywhere (elaborate multi-cloud forfeits the platform and creates new lock-in, REG-026); best for long-lived or regulated systems and critical rented services.
5. Context: SWITCHING_LIKELIHOOD_AND_REGULATION (above).
6. Certainty: grounded for P1 to P3; inferred for P4's proportionality (the EU exit-strategy requirement is known only from summaries).
7. Flags: none.
Links: related `SERVICES.3` (L078 see also L359), `CONTAINMENT.2`.

### OWNERSHIP.CONTAINMENT.2 Adapter Between Code and Dependency

Intent: A thin boundary separates the team's code from a dependency or external system whose model it does not control, where that pays.
Rows: L035, L068, L342, L344, L345.
1. Decision: Put a thin wrapper, containing only what the project needs, between the code and a dependency or external system when substitution is plausible, or the dependency is volatile, security-sensitive or single-vendor, or its model differs from the domain (an anti-corruption layer that keeps business rules out); a rented service reached through a proprietary interface falls under these conditions, while a backing service reached through a stable standard interface (SQL, SMTP) is an attached resource (`CONTAINMENT.3`) and gets no wrapper of its own. Keep external types and parsing of the external payload inside the wrapper, in one place. Use a stable standard interface directly when switching is unlikely and the dependency is core. Key the team's own data and public interfaces on its own identifiers and types: a vendor's identifier is stored only as an attribute of the team's entity that refers out (that attribute is the mapping the team owns), never as the key of the team's data or as a type in its public interface. Outcome: a swap or a vendor change touches one place.
2. Grounds: L068 (REG-012, REG-026, REG-034, REG-039): wrap wins for volatile, security-sensitive or single-vendor and external services; not wrapping wins when switching probability is low and the interface standard (REG-026, REG-034: speculative abstraction costs). L344 (REG-026, REG-186): same condition for the domain-versus-foreign-model case. L035 (T4 plus one T2, inferred), L342 (majority; REG-186, REG-208), L345 (inferred, no source states it as a rule). Final pass: L068's own condition (not wrapping wins for a stable, standard interface); REG-186 fetched in review ("might not be suitable when ... no significant semantic differences"); L343 for attached resources. REG-186 states translation at the boundary, not a storage rule; the defensible core is that the foreign model stays out of the team's keys and interfaces, while storing an external reference is unavoidable and is itself the owned mapping.
3. Positions: P1 (a) wrap, keep exit path; (b) use directly for speed. P2 (a) wrap; (b) do not wrap. P3 (a) mandatory anti-corruption layer; (b) call directly. P4 one boundary object for parsing. P5 no vendor types in own data without a mapping.
4. Rejected: the layer as mandatory for every dependency: it adds latency and something to operate, and is best for multi-stage migrations, differing semantics, critical-path or uncertain vendors; direct use best when the service is core, stable and switching unlikely.
5. Context: SWITCH_PROBABILITY_AND_VOLATILITY (above).
6. Certainty: grounded for the conditional wrap decision; inferred for the identifier rule (P5).
7. Flags: none.
Constraints: where a wrapper exists, MUST NOT let a vendor type cross the team's public interface (inferred).
Links: related `CONTAINMENT.1`; `CONSTRUCTION.BOUNDARY` for converting input to a precise type.

### OWNERSHIP.CONTAINMENT.3 External Systems as Attached Resources

Intent: A database, queue, cache or third-party service is a resource reached through configuration.
Rows: L343, L1195.
1. Decision: The location and credentials of a backing or third-party service are configuration, and the code makes no distinction between local and third-party instances, so an instance is swapped by changing configuration; where the semantics of a vendor's proprietary model differ, the difference is modelled honestly, in the adapter of `CONTAINMENT.2`. Outcome: the same build runs against any instance.
2. Grounds: L343 (majority; REG-186, REG-207): stated for services with standard interfaces (SMTP, SQL); (b) the distinction is real when semantics differ. L1195 (consensus; REG-1109).
3. Positions: P1 (a) attached resource; (b) real distinction when semantics differ. P2 same for backing services.
4. Rejected: code that branches on local versus third-party: best only where the semantics genuinely differ.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Links: where configuration lives is decided in `TRANSVERSE.CONFIG`, not here.

### OWNERSHIP.CONTAINMENT.4 Bounding Runtime Effect and Untrusted Responses

Intent: The damage a dependency or a third-party response can do at runtime is bounded.
Rows: L069, L340.
1. Decision: Isolate risky dependencies at runtime (sandbox, least privilege) so a bug or compromise has bounded effect, and treat every third-party response as untrusted input: validate and sanitise before use, use TLS, follow redirects only to an allowlist of targets, and cap the resources spent on a response. Outcome: a failing or hostile dependency cannot exceed a known blast radius.
2. Grounds: L069 (majority; practicality open; REG-003, REG-012), L340 (consensus; REG-186, REG-194).
3. Positions: P1 isolate. P2 untrusted input rules.
4. Rejected: none competing.
5. Context: none.
6. Certainty: grounded for P2; inferred for the scope of P1 (practicality is open: the extent of sandboxing is not sourced, so it applies where it is practical for the ecosystem).
7. Flags: none.

---

## OWNERSHIP.SERVICES (L2): External Services

Intent: What to require of a rented service or hosted tool: availability fit, API stability, switching terms, contract and vendor assessment.
Rolled-up decision: choose a service whose commitments compose with the team's own target and read the SLA as a commercial instrument; depend on an API only with a stated stability promise and defences against its removal; verify data export and switching terms before dependence; know the price and licence risk and the processor contract; assess the vendor in proportion to criticality; treat CI and hosting as supply chain.
Certainty: grounded for most (consensus rows); inferred where noted.
Links: children `SERVICES.1` to `SERVICES.6`.

### OWNERSHIP.SERVICES.1 Availability Fit and Commitments

Intent: A rented service's availability commitment fits what the team promises, and its worth is read honestly.
Rows: L031, L033, L346, L347, L348, L349, L350.
1. Decision: Pick a service whose availability target is at least the team's own, because hard dependencies multiply availabilities. Read an SLA as a commercial instrument (measured uptime, a credit scale, a claim procedure, exclusions, credits as the sole remedy), not a promise; compare the remedy to the team's loss and, where credits cannot cover it, mitigate by design (fallback, redundancy) (inferred, L347). The team owns its availability target and design; the provider owns only what its published SLA defines. Keep the internal SLO tighter than the SLA signed or advertised, plan from the dependency's observed behaviour as well as its stated target, and monitor reachability, latency and errors of each service as part of adopting it (inferred, L033 has no source). Outcome: the team's promise is not larger than what its dependencies can honestly support.
2. Grounds: L031 (consensus; REG-007, mathematically general), L346 (consensus; REG-125, REG-197), L348 (consensus; REG-197, REG-201), L349 (consensus; REG-125), L350 (majority; REG-125), L347 (inferred, not assessable; REG-197, REG-201), L033 (consensus, inferred, no source id). Final pass: the two inline-marked sentences follow from a grounded rule of this node but none is sourced. No competing position in any row.
3. Positions: P1 target at least yours. P2 SLA as commercial instrument. P3 remedy versus loss. P4 own your availability. P5 SLO tighter than SLA. P6 observed behaviour. P7 monitor.
4. Rejected: none competing.
5. Context: none.
6. Certainty: grounded for P1, P2, P4, P5; inferred for P3, P6 (majority) and P7 (no source id).
7. Flags: none.
Links: mechanisms that guarantee availability and the monitoring practice sit in `ASSURANCE.AVAILABILITY` and `OPERATION`; this node holds only what to require when renting (MD-03).

### OWNERSHIP.SERVICES.2 API Stability and Deprecation

Intent: What the team requires of a service API's stability promise and how it protects itself against removal.
Rows: L034, L351, L354, L355 (L353 is a row of `ASSURANCE.CONTRACTS.1`).
1. Decision: Before depending on a service API, read its stability tiers and deprecation policy and prefer providers that publish a minimum notice and keep two versions working side by side during a transition. Consume machine-readable deprecation signals (Deprecation and Sunset headers) and route them to an alert, pin the API version where the provider allows it and upgrade deliberately, and treat a published deprecation window as a goal, not a guarantee. Outcome: the removal of an API is detected and absorbed before it breaks the service. Which evolution policy a provider follows, and when each is best, is held by `ASSURANCE.CONTRACTS.1`; any stated promise is acceptable to depend on.
2. Grounds: L034 (consensus; REG-008, REG-009, REG-021; practice in the wild is weaker), L351 (consensus; REG-182, REG-183; that consumers act on signals is open), L354 (majority; REG-009, REG-213), L355 (majority, inferred; REG-021, REG-182, REG-183).
3. Positions: P1 read policy, prefer notice. P2 consume deprecation headers. P3 provider evolution policies (held by `ASSURANCE.CONTRACTS.1`). P4 pin the version. P5 real notice is shorter than the policy.
4. Rejected: none here; the policies and their conditions are in `ASSURANCE.CONTRACTS.1`.
5. Context: none for the consumer decision.
6. Certainty: grounded for P1 and P4; inferred for P5; open for whether consumers act on the signals.
7. Flags: none.
Stack pointers: L034 (Kubernetes, Google APIs), L351 (HTTP).
Links: see `ASSURANCE.CONTRACTS.1` (provider-side evolution policies, L353).

### OWNERSHIP.SERVICES.3 Data Export and Switching Terms

Intent: The team can take its data and integration logic out of a rented service, on known terms.
Rows: L356, L357, L359, L1112.
1. Decision: At selection verify that the service can export all the team's data in a commonly used machine-readable format through an open interface, and test the export once before depending on it. Require from a cloud or data-processing provider a contract that covers switching (notice and transition terms, data return, no punitive egress charges). Keep an independent copy of critical data held in a service, and keep credentials and integration logic exportable, so exit does not depend on the provider's cooperation. For managed services and SaaS, assume the provider is responsible for its infrastructure and the customer for its own data, verify what the provider's backups cover and for whose recovery, and keep an independent copy of what the team cannot afford to lose. Outcome: leaving does not depend on the provider's goodwill.
2. Grounds: L356 (consensus; REG-187, REG-198; the legal duty is grounded via a secondary page, the test is inferred), L357 (consensus; REG-187; exact figures open; EU egress and switching charges disappear from 12 January 2027), L359 (majority, inferred; REG-026, REG-187, REG-216), L1112 (consensus on one source; REG-1060, REG-1070). No competing position.
3. Positions: P1 export verified and tested. P2 switching contract. P3 independent copy. P4 shared responsibility and backup verification.
4. Rejected: none competing.
5. Context: JURISDICTION: where law applies (EU rights), elsewhere the practice stands without the legal duty.
6. Certainty: grounded for the responsibility split and the export requirement; inferred for the independent-copy advice and backup consequence.
7. Flags: none.
Links: related `CONTAINMENT.1`, `STANCE.2`; recovery practice is in `OPERATION.RECOVERY`.

### OWNERSHIP.SERVICES.4 Commercial and Contract Terms

Intent: The contract and price model state the cost and legal position of renting, and someone owns them.
Rows: L358, L360, L361.
1. Decision: Where a service processes personal data, require a written processor contract (documented instructions only, confidentiality, security measures, authorised sub-processors, assistance with data-subject rights, deletion or return at the end, audit rights) and choose processors giving sufficient guarantees. Treat price risk as part of selection: understand the pricing model, unit economics and egress, give cost an owner and expect unmetered cost exposure from usage-based services. For each critical open-source or hosted dependency record who controls its licence and decide in advance what to do if terms change; prefer foundation-governed or multi-vendor projects when the team builds services that could be read as competitive or must outlive the vendor, and accept a single-vendor project for non-competitive end-user use with a credible rationale. Outcome: the legal and cost position of a rented service is known before dependence.
2. Grounds: L358 (consensus; EU GDPR; unofficial copy of the text; REG-198), L360 (majority; no T1 or T2 source on contractual price caps, open; REG-185, REG-187, REG-214), L361 (REG-212, REG-215; the rule is inferred): (a) wins for end-user use, (b) wins for competitive or outliving use.
3. Positions: P1 processor contract. P2 price risk in selection. P3 (a) single-vendor acceptable (speed, features); (b) foundation or multi-vendor (exit risk, control).
4. Rejected: P3a as a default: best for non-competitive end-user use; P3b as a default: best where the dependency may be read as competitive or must outlive the vendor (T4 source).
5. Context: JURISDICTION: the processor contract is stated for the EU (GDPR), apply the local equivalent where one applies.
6. Certainty: grounded for P1; inferred for P2 (no T1 or T2 source on price caps) and P3's rule.
7. Flags: none.

### OWNERSHIP.SERVICES.5 Vendor Assessment

Intent: A vendor is assessed before and during dependence, to a depth that matches the stakes.
Rows: L363, L364, L365, L378.
1. Decision: Assess a vendor's security and supply-chain posture before depending on it (authentication options, evidence of intrusion with logs retained at least six months, SBOM and open-source governance, vulnerability disclosure policy and CVE practice, patch support). Scale the depth to criticality and data sensitivity and repeat it through the contract life, not only at selection; a small team without capacity to triage uses the uniform baseline checklist for every vendor. Treat third-party assurance reports (SOC 2, ISO/IEC 27001) as evidence of a vendor's controls, not proof of fit: read scope, period and exceptions (inferred, L365 has no source). Evaluate non-library tools and platforms (dev tools, CI service, hosting) with the same criteria as services (inferred, composed, L378). Outcome: the vendor's posture is known and re-checked, to the depth the damage would justify.
2. Grounds: Final pass: the two inline-marked sentences each follow from a grounded rule of this node (the SLA is a commercial instrument; CI and hosting are supply chain, `SERVICES.6`) but none is sourced. L363 (consensus; REG-194, REG-196, REG-199), L364 (REG-196, REG-199; lifecycle grounded, scaling inferred), L365 (open, not assessable, no source id), L378 (open, composed; REG-086, REG-195, REG-200).
3. Positions: P1 baseline posture. P2 (a) depth by criticality (speed, cost); (b) uniform baseline (simplicity, fairness). P3 reports are evidence. P4 same criteria for tools and platforms.
4. Rejected: P2b as a general rule: best for small teams without capacity to triage; P2a best when vendors are many and most low-risk.
5. Context: CRITICALITY_AND_DATA_SENSITIVITY (above).
6. Certainty: grounded for P1; inferred for P2's scaling; open for P3 and P4 (no source, composed).
7. Flags: none.

### OWNERSHIP.SERVICES.6 CI and Hosting Services as Supply Chain

Intent: The build, CI and hosting services that execute with the team's secrets and produce what it ships are held to supply-chain standards.
Rows: L366, L367, L368.
1. Decision: Treat a CI or hosting service as part of the supply chain: pin third-party CI components to an immutable identifier (a full commit hash from the official repository, not a fork), audit their source, set the default token permission to read-only and raise it per job, and do not run self-hosted runners on untrusted code such as public repositories, since they are not guaranteed ephemeral and clean. Outcome: a compromised third-party action or runner cannot reach the team's secrets or artifacts.
2. Grounds: L366, L367, L368 (consensus; REG-195, REG-200). No competing position.
3. Positions: P1 supply-chain view. P2 pin and least privilege. P3 no self-hosted runners on untrusted code.
4. Rejected: none competing.
5. Context: none.
6. Certainty: grounded (one platform's guidance, REG-195; the generalisation to other CI services is a stack pointer, inferred).
7. Flags: none.
Stack pointers: L367, L368 (one CI platform; pointer for equivalents).

---

## OWNERSHIP.LICENCE (L2): Licences

Intent: Which licence obligations a dependency brings and how the team classifies, decides and declares them.
Rolled-up decision: the licence is read and classified by what the team does with the code before adoption; a written class policy with a named decider governs; network copyleft is decided separately; the team's own files declare their licence machine-readably.
Certainty: grounded for the reading rules; open for the linking boundary.
Links: children `LICENCE.1` to `LICENCE.4`.

### OWNERSHIP.LICENCE.1 Reading and Classifying Licences

Intent: A dependency's licence is read and classified against what the team does with the code.
Rows: L036, L362, L370, L371, L372.
1. Decision: Before adoption, check that the licence is present, clear and acceptable for the intended use, and classify the dependency by licence family and by the team's distribution model, because obligations are triggered by what is done with the code (ship, link, modify, run as a service). Treat compatibility as directional and pair-specific, distinguish the "or later" variants and exceptions and state them with SPDX expressions, and do not treat a source-available licence with a field-of-use restriction as open source. Outcome: no dependency's obligations surprise the team after use.
2. Grounds: L036 (consensus; REG-001, REG-003, REG-012, REG-017), L370 (consensus; REG-188, REG-189, REG-210), L371 (consensus; REG-188, REG-202; the FSF list could not be fetched), L372 (consensus; REG-191), L362 (consensus on the OSI definition, application to a named licence inferred; REG-190, REG-212). No competing position.
3. Positions: P1 present and acceptable. P2 obligations by use. P3 directional compatibility. P4 "or later" variants and SPDX. P5 source-available is not open source.
4. Rejected: none competing.
5. Context: DISTRIBUTION_MODEL is the input of the classification itself, not a condition on the decision.
6. Certainty: grounded; compatibility analysis itself is not covered by L036 and relies on L371.
7. Flags: none.

### OWNERSHIP.LICENCE.2 Policy and Process

Intent: Which licence classes are allowed and who decides, and the process that keeps compliance working.
Rows: L373, L377.
1. Decision: Write down the licence classes (allowed, notice-only, review-needed, prohibited) by distribution model with a named decider. Where the team ships client or embedded software or holds code it must keep closed, the classes are conservative; one organisation's published policy is the example (notice licences allowed, strong copyleft only server-side or internal, network copyleft, SSPL and non-commercial licences prohibited), not a standard. Teams hosting only, or publishing their own code under compatible terms, may allow copyleft where obligations are understood and met. Run a defined compliance process with identified roles and a way to keep it working over time; ISO/IEC 5230 (OpenChain) is the standard and can be self-certified. Outcome: licence acceptance is a recorded policy applied by a known person.
2. Grounds: L373 (contested; REG-188, REG-189, REG-210; the conservative example is one organisation's choice, (b) inferred), L377 (majority; REG-193; summary grounded, details inferred).
3. Positions: P1 (a) conservative class policy (control of own source, audit cost); (b) allow copyleft with understood obligations (speed, reuse). P2 compliance process.
4. Rejected: neither policy is rejected; the distribution model selects it.
5. Context: DISTRIBUTION_MODEL moves the policy (above).
6. Certainty: grounded for P1a; inferred for P1b and the process details.
7. Flags: none.
Links: related `LICENCE.1`.

### OWNERSHIP.LICENCE.3 Network Copyleft and Separate Components

Intent: Network-copyleft code and separately run copyleft services are treated explicitly.
Rows: L374, L375.
1. Decision: Decide network-copyleft code (AGPL) separately from GPL: modifying it and letting users interact with it over a network triggers a source offer. Treat an unmodified copyleft service run as a separate network component as a different question from linking it into the program: the question is the interface, not the proximity, and is settled with legal review where the boundary matters. Pipes, sockets and command-line arguments are normally communication between separate programs, while intimate exchange of complex internal data structures may make one combined work (REG-188). Outcome: network copyleft is never accepted by default and a separate-component claim is never assumed.
2. Grounds: L374 (majority; REG-188, REG-189, REG-210). L375 (REG-188, fetched at review: pipes, sockets and command-line arguments are normally between separate programs; intimate exchange of complex internal data structures may make one combined work; grounded in part).
3. Positions: P1 AGPL special case. P2 separate component differs from linking.
4. Rejected: none competing.
5. Context: none.
6. Certainty: grounded for P1; grounded in part for P2 (the interface test by REG-188), the application to a given case stays with legal review.
7. Flags: none.

### OWNERSHIP.LICENCE.4 Declaring the Team's Own Licence

Intent: Licence and copyright of the team's own files are declared so compliance can be checked mechanically.
Rows: L376.
1. Decision: Declare the licence and copyright of every file machine-readably (SPDX identifiers in headers, licence texts in a licences directory) so tools can check compliance. Outcome: compliance of the team's own output is checkable by tool.
2. Grounds: L376 (majority; REG-191, REG-192). No competing position.
3. Positions: P1 machine-readable declaration.
4. Rejected: none.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.

## Review applied

- R01: applied (removed "a published contract" from STANCE.4).
- R02: applied (STANCE.4 grounds reworded to rest on L330's own condition; F1 marked settled).
- R03: applied (SELECTION.2: REG-013 cited only for documenting and migration commitment; reversible entry marked inferred).
- R04: applied (SELECTION.3: single-maintainer outside the small, stable, replaceable case needs a compensating reason or exit plan).
- R05: applied (SERVICES.2: L353 kept here as a consumer-facing question with P3a and P3b each best under its condition; pointer to ASSURANCE.CONTRACTS dropped; F3 settled).
- R06: applied (LICENCE.3: interface test grounded in part by REG-188; legal review kept; F4 settled).
- R07: applied (SELECTION.5 keeps authenticity and provenance and points to LIFECYCLE.4 for the rebuild rule; LIFECYCLE.4 keeps channel, mirror, recursion, removal and states the rebuild rule once; garbled sentence rewritten).

## Final pass applied

Resolutions (`final_pass/resolutions.md`, J1 section):
- R08, R19 (F5): applied (CONTAINMENT.2: conditions sentence and identifier sentence replaced, Constraint added, grounds added, F5 removed). The original clauses "keep external types and parsing ... in one place" and "use a stable standard interface directly when switching is unlikely and the dependency is core" are kept as their own sentences, since the resolution replaces only the first and third sentences.
- R09: applied (LIFECYCLE.3: "update on need" wording with the debt pointer; Rejected P1b reworded).
- R10 (F6): applied (LIFECYCLE.2: resolution-rule sentence replaced; ranking rejected added; F6 removed).
- R11 (F2): applied (LIFECYCLE.3: cooldown of at least seven days, marked inferred; F2 removed).
- R12: applied (STANCE.2: built-in preference, no ranking across modes).
- R13: applied (STANCE.1: layer reasons are examples; Certainty split).
- R14: applied (LICENCE.2: conservative classes stated as one organisation's example, not a standard).
- R15: applied (SERVICES.1: two sentences marked inferred; SERVICES.5: two sentences marked inferred).
- R16: applied (CONTAINMENT.1: tested exit where regulation requires and for critical functions by expected loss).
- R17: applied via X10.
- R18: applied (SELECTION.2: standing trial ring sentence after the default sentence).
- F1 (STANCE.4): applied as "settle, unchanged": the Decision is unchanged and the flag line is removed, since the resolution states no maintainer confirmation is needed.
- Review flags F3 and F4 (settled by review, confirmed by the final pass): flag lines removed (SERVICES.2 also changes through X7).
- Not applied: none.

Cross-unit lines (`cross_unit_fixes.md`):
- X3: not applied separately; superseded by X7 (SERVICES.2 keeps the consumer side only).
- X7: applied (SERVICES.2: provider-side policies and L353 moved out, pointer to `ASSURANCE.CONTRACTS.1`, consumer side kept, any stated promise acceptable). The content record is ASSURANCE.CONTRACTS.1 in J2; this unit holds only the pointer.
- X10: applied (LIFECYCLE.3 keeps the supply-chain trigger and points to `TRANSVERSE.CONFIG.6` for the rotation; Links line updated).
- X1, X2, X4 to X6, X8, X9, X11 to X14: do not name J1.

Nodes added: none (the final pass creates no node in J1).
Flags still open: none.

Review pass (earlier): R01 to R07 stay as recorded in `## Review applied`.
