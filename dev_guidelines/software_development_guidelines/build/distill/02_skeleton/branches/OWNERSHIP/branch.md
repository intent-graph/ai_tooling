# Branch OWNERSHIP: tree and node records (positions listed, no verdict)

Decided rules that bind: `../../../target_hierarchy.md` and `../../../maintainer_decisions.md` (MD-01 best-not-average, MD-02 no default team, MD-03 one location per fact, MD-05 scope). Nothing below is a decision: positions are listed for the judges, node by node (MD-01 is applied at judging, not here). Row ids are ledger ids (L001-L460 part 1, L1001-L1289 part 2, L1501-L1565 part 3); REG-nnn are source register ids; REG-181 is the maintainer's codified practice (source MAINT-S01, not citable), named as MAINT positions. Rows marked `origin: judged in the JavaScript guideline` appear as a position among others, never as the decision.

OWNERSHIP has no split topic in the table of `../../tree_l2.md`, so no node here is an index node; the six L2 nodes hold their content. Cross-branch overlaps are listed under "Routing objections" at the end; of the twelve raised, three rows were moved to other branches and nine kept (`../../objections/resolution.md`), and two rows were received from other branches.

## Branch tree

- `OWNERSHIP` Ownership
  - `OWNERSHIP.STANCE` Necessity and Default Stance
    - `OWNERSHIP.STANCE.1` What a New Dependency or Layer Must Earn
    - `OWNERSHIP.STANCE.2` Write, Adopt or Rent per Need
    - `OWNERSHIP.STANCE.3` Bringing Code Inside: Copy, Vendor, Upstream
    - `OWNERSHIP.STANCE.4` Speculative Building and Probable Use
  - `OWNERSHIP.SELECTION` Finding, Profiling and Selecting
    - `OWNERSHIP.SELECTION.1` Evaluation Process and Admission Gate
    - `OWNERSHIP.SELECTION.2` Fit, Maturity and Novelty
    - `OWNERSHIP.SELECTION.3` Project Health and Compatibility Signals
    - `OWNERSHIP.SELECTION.4` Dependency Weight
    - `OWNERSHIP.SELECTION.5` Authenticity, Provenance and Known Vulnerabilities at Adoption
    - `OWNERSHIP.SELECTION.6` Vetting Depth and Delegated Audit
  - `OWNERSHIP.LIFECYCLE` Dependency Lifecycle
    - `OWNERSHIP.LIFECYCLE.1` Declare and Lock
    - `OWNERSHIP.LIFECYCLE.2` Version Constraints and Resolution
    - `OWNERSHIP.LIFECYCLE.3` Updating
    - `OWNERSHIP.LIFECYCLE.4` Channels, Mirrors and Supply-Chain Integrity
    - `OWNERSHIP.LIFECYCLE.5` Inventory, Watching and End of Life
  - `OWNERSHIP.CONTAINMENT` Containment and Exit
    - `OWNERSHIP.CONTAINMENT.1` How Much Reversibility to Buy
    - `OWNERSHIP.CONTAINMENT.2` Adapter Between Code and Dependency
    - `OWNERSHIP.CONTAINMENT.3` External Systems as Attached Resources
    - `OWNERSHIP.CONTAINMENT.4` Bounding Runtime Effect and Untrusted Responses
  - `OWNERSHIP.SERVICES` External Services
    - `OWNERSHIP.SERVICES.1` Availability Fit and Commitments
    - `OWNERSHIP.SERVICES.2` API Stability and Deprecation
    - `OWNERSHIP.SERVICES.3` Data Export and Switching Terms
    - `OWNERSHIP.SERVICES.4` Commercial and Contract Terms
    - `OWNERSHIP.SERVICES.5` Vendor Assessment
    - `OWNERSHIP.SERVICES.6` CI and Hosting Services as Supply Chain
  - `OWNERSHIP.LICENCE` Licences
    - `OWNERSHIP.LICENCE.1` Reading and Classifying Licences
    - `OWNERSHIP.LICENCE.2` Policy and Process
    - `OWNERSHIP.LICENCE.3` Network Copyleft and Separate Components
    - `OWNERSHIP.LICENCE.4` Declaring the Team's Own Licence

## Records

Layout per record: uid and name; intent; rows; positions (P-numbered; strongest argument, force served, condition under which it would be the best, row and source ids); context variables; links; stack pointers. Forces of the branch: control, time to value, cost of ownership over time, exit risk, security exposure, fit.

### OWNERSHIP Ownership

Intent: For each capability, does the team write it, adopt it or rent it, and how is that choice kept reversible.
Rows: none directly (see children)
Positions: see children
Context: see children

#### OWNERSHIP.STANCE Necessity and Default Stance

Intent: Whether the capability is needed at all and, absent a specific reason, whether the default is to write, adopt or rent; what a new layer or dependency must earn.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.STANCE.1 What a New Dependency or Layer Must Earn

Intent: Whether a new dependency or layer is justified before its quality is looked at, and what it must outweigh.
Rows: L001, L037, L308
Positions:
- P1 Justify by necessity before assessing quality, and treat every dependency as an ongoing liability (maintenance, upgrade, security, platform shifts), not a one-time saving. Strongest argument: it adds attack surface and ownership cost beyond the development effort it saves. Force: cost of ownership, security exposure. Best when: stated as the first test with no contrary position recorded (L001, L037, both consensus; REG-003, REG-011, REG-012).
- P2 MAINT: a new layer or moving part is created only when at least one strong reason outweighs its cost (reuse across consumers, hiding internals behind a business-level verb, keeping a query tunable by its owner without redeploying consumers, enforcing integrity once); the maintainer defaults to not creating it, then accepts a wide band once justified (L308; MAINT-S01, REG-181, not citable). Competing in the row: default to the layer (database-centric). Force: cost of ownership, fit. Best when: the row names no condition beyond "once justified"; it reads public practice as agreeing (build-versus-not discipline).
Context: none
Links:
- Related `OWNERSHIP.SELECTION.2` (L308 and L037 see also L024: a new layer or technology must earn its cost; not merged)

##### OWNERSHIP.STANCE.2 Write, Adopt or Rent per Need

Intent: For each need, which of writing, adopting a component or renting a service, decided per need.
Rows: L002, L040, L310
Positions:
- P1 Reuse by default (L002, origins SRC-C02 a and ADOPT-C02 a; REG-004). Strongest argument: lowers cost, speeds delivery, avoids new vulnerabilities, especially cryptography and protocols. Force: security, delivery speed, cost of ownership, correctness. Best when: the domain is complex or security-critical and a vetted component exists, or the function is non-core, well understood and widely used.
- P2 Minimise dependencies: an internal code problem is cheaper than a dependency-management problem you do not control (L002, SRC-C02 b; Google SWE ch. 21, Cox, Pike; REG-011, REG-012, REG-020). Force: cost of ownership, control, exit risk. Best when: small stable functionality, long-lived products, weak upgrade incentives.
- P3 Build your own when it is a core business function (L002, ADOPT-C02 b; REG-027). Force: control, differentiation, quality. Best when: the function carries competitive advantage.
- P4 Build in-house only for needs third-party software cannot better meet; the reading that reconciles P1 and P2 (L002, SRC-C02 c; NIST PW.4.2, REG-004). Row agreement: contested (SRC-C02), majority (ADOPT-C02), consensus (ADOPT-C03).
- P5 Renting is an adoption decision with the same cost test plus a control cost. (a) Rent non-core, build or keep control for core (L040; REG-027). Force: control, differentiation. (b) Rent broadly and accept lock-in where the pay-off is commensurate (REG-026). Force: delivery speed, cost of ownership. Row certainty: inferred (the sources do not address SaaS directly beyond outsourcing).
- P6 MAINT: prefer a platform built-in over custom code unless it lacks a stated capability; when custom code is chosen, record the missing capabilities and revisit if the need shrinks to what the built-in does; the doctrine marks the built-in "not currently used" (L310; REG-181). (a) built-in: less code to own, supported behaviour; cost of ownership, exit risk; best when its model fits. (b) custom: control, fit; best when granularity or per-entry strategies are needed. Row: public practice read as contested; coverage check: matches L002, not a contradiction.
Context:
- CORENESS: whether the function carries competitive advantage moves write versus adopt versus rent (L002 ADOPT-C02 b: "wins when the function carries competitive advantage"; L040: "rent non-core, build or keep control for core")
Links:
- Related `OWNERSHIP.STANCE.3` (L002 see also L071: restates position P2 as its own contested claim)
Stack pointers: L310 (materialized views versus manual cache tables, neutral in the rule)

##### OWNERSHIP.STANCE.3 Bringing Code Inside: Copy, Vendor, Upstream

Intent: When a small needed piece is copied or the source is brought inside the boundary rather than depended on, and how carried code relates to its origin.
Rows: L070, L071, L072
Positions:
- P1 For a tiny used surface, copy or reimplement the needed code (L070; REG-012). Force: attack surface, exit risk. Best when: the used surface is tiny.
- P2 Depend even then, particularly for cryptography (L070, REG-004 PW.4; force correctness). Against copying: lost upstream fixes (REG-011 cost of forks), build only on core (REG-027); row marks the opposing arguments inferred. Row agreement: contested.
- P3 Prefer source-control problems over dependency-management problems: vendor or use a monorepo (L071; REG-011). Force: control, visibility. Best when: large codebases and the tooling to carry them.
- P4 Consume from a registry with a lock (L071; REG-031, REG-037). Force: cost of ownership.
- P5 Upstream rather than carry private forks: contribute fixes, report vulnerabilities found in a component to its maintainer (L072; majority; REG-011, REG-035, REG-040). No competing position recorded.
Context: none
Links:
- Related `OWNERSHIP.STANCE.2` (L071 see also L002)

##### OWNERSHIP.STANCE.4 Speculative Building and Probable Use

Intent: Whether to build for presumed future needs or only for today's, and how much to invest in making change cheap.
Rows: L038, L330, L1208
Positions:
- P1 Do not build speculative functionality: building, delaying other work, carrying complexity and repairing wrong guesses are four distinct costs; it applies to writing a substitute "in case" as much as to features (L038, consensus; REG-026, REG-034; the application to dependency substitution is inferred). Force: delivery speed, cost of ownership. Best when: change is cheap (the condition L330 gives for this side).
- P2 MAINT: design the structure for probable future usage, not only today's ticket (decide column versus table by whether a cardinality drift is plausible), while avoiding speculative optimisation (L330; REG-181). Force: reversibility. Best when: changes to structure are costly (a very large relational store). Row records the contradiction with YAGNI and with L038 (coverage check section 5).
- P3 Do not build for presumed future features, but invest in making the software easy to modify (tests, refactoring, continuous delivery) (L1208, consensus; REG-034). Force: reversibility, cost of ownership. Row records a possible tension with L330.
Context:
- COST_OF_STRUCTURAL_CHANGE: how costly a later change to the structure is moves build-for-today versus probable use (L330: "wins when changes to structure are costly")
Links: none

#### OWNERSHIP.SELECTION Finding, Profiling and Selecting

Intent: How a candidate library, tool or technology is found, profiled and chosen, with how deep the vetting goes.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.SELECTION.1 Evaluation Process and Admission Gate

Intent: How an evaluation is run, in what context and recorded where, and who may introduce a dependency.
Rows: L003, L004, L005, L028, L029, L030, L042, L1537, L1539
Positions:
- P1 Judge a candidate against an explicit criteria set (design and docs, code quality, tests, bug handling, maintenance, usage, security exposure, licence, transitive dependencies), in the context of its intended use, and repeat when the use changes substantially (L003, L004, L042; consensus; REG-003, REG-004, REG-011, REG-012); L042 adds tests that run and pass, clear API documentation, secure defaults and a compatible licence. No competing position recorded.
- P2 Make selection systematic and written, because practitioners mostly select ad hoc and over two dozen factors decide the outcome (L005; one study, REG-017; the recommendation is inferred).
- P3 Write the reason for each non-trivial selection (alternatives considered, criteria, accepted risks) where later maintainers will find it (L029; majority; inferred as a synthesis; REG-004, REG-013, REG-017).
- P4 Who may introduce a dependency (L028; REG-004, REG-011, REG-013; contrast inferred). (a) a central sanctioned list with provenance data (NIST SSDF; force security, control, consistency; best in regulated or high-criticality contexts and many teams); (b) team-level choice with light visibility (McKinley; force delivery speed, cognitive load; best for small teams, low regulation). The row statement also names a reviewed proposal as a third mode.
- P5 Use ecosystem aggregators for discovery and first screening and expect them to change or stop (L030; majority; REG-002, REG-006, REG-010, REG-017; tools are ecosystem-specific).
- P6 Prior framing from the JavaScript guideline (origin: judged in the JavaScript guideline, not inherited): a package enters only when its need, identity and documentation have each been checked and existing components are considered first (L1539); each dependency is a trust decision, few in number (L1537). Both rows are node intents with no claim of their own; certainty inferred (parts carved out of a node that stays narrowed); no source of their own.
Context:
- REGULATION_AND_SCALE: regulated or high-criticality contexts and many teams versus small teams with low regulation move who may introduce a dependency (L028)
Links:
- Related `OWNERSHIP.STANCE.1` (L1537 see also L037 and L001)

##### OWNERSHIP.SELECTION.2 Fit, Maturity and Novelty

Intent: Whether a candidate fits the real requirements and how much new technology the team takes on.
Rows: L023, L024, L025, L312, L1227, L1228, L1230
Positions:
- P1 Select for fit to the task's actual requirements and constraints, not features or fashion (L023, consensus; REG-003, REG-013, REG-017). MAINT: choose the core technology by problem fit, not dogma (a relational engine because it solves integrity and scale cleanly) (L312; REG-181; public practice read as consensus; its paradigm half is also held in `CONSTRUCTION.PARADIGM`, see objections).
- P2 Boring first: default to proven technology, prefer what the team already operates, spend novelty ("innovation tokens") only where the business needs it and the existing tool demonstrably cannot solve the problem, after documenting why (L024 a; ADOPT-C05; REG-004, REG-011, REG-013); prefer mature technology because its failure modes are known (L1228; REG-1022, REG-1132); spend novelty on what differentiates the product, not infrastructure (L1227; REG-1022). Force: team cognitive load, operational cost, reversibility. Best when: small teams, operations-heavy systems, long lifetimes.
- P3 Staged novelty: place candidates in assess, trial and adopt rings and try them where experience is gained; move a new tool through explicit stages (assess, trial in limited production use, adopt, hold) instead of switching in one step (L024 b; L025; REG-013, REG-015, Thoughtworks Radar). Force: learning, delivery speed through better tools. Best when: the organisation has capacity for experiments and tolerance for churn. Row L025: one framework, no source read opposes it, but L024 a discourages novelty at all.
- P4 Weigh the perpetual operating cost, not adoption convenience, and talk to others before adopting (L1230, majority; REG-1022). Within L024, adopt new where the need is real and an exit or migration plan exists (REG-013 itself admits).
Context:
- EXPERIMENT_CAPACITY: team size, operational load, system lifetime versus capacity for experiments (L024: "wins for small teams, operations-heavy systems, long lifetimes" against "wins for organisations with capacity for experiments and tolerance for churn")
Links:
- Related `OWNERSHIP.STANCE.1` (L024 see also L308, L037)

##### OWNERSHIP.SELECTION.3 Project Health and Compatibility Signals

Intent: Which observable signs of a candidate's health and stability promise count, and how much weight each carries.
Rows: L006, L007, L008, L011, L014, L015, L016, L017, L018, L019, L041
Positions:
- P1 Prefer recent commits, recent releases and visible communication; treat long inactivity as a risk; activity within 12 months (L006, L041; consensus; REG-001, REG-003, REG-011, REG-012, REG-017).
- P2 Require several maintainers from several organisations (L007 a, L041). Strongest argument: single point of failure for fixes and for account takeover. Force: exit risk, security, continuity. Best when: the component is on a critical path or hard to replace (REG-001, REG-003, REG-012, REG-018).
- P3 Tolerate small projects: low contributor scores are not definitive and narrow finished tools legitimately have one author (L007 b; REG-001). Force: cost of ownership, fit, minimal footprint. Best when: small, stable, easily replaced or vendorable components.
- P4 Check responsiveness: open bug count, resolution speed, security backports or long-term-support versions (L008; REG-003, REG-012). Prefer projects with a vulnerability-disclosure policy and a reporting channel (L011; REG-001, REG-003). No competing position recorded.
- P5 Read the candidate's compatibility promise (none, source-compatible, binary-compatible, automated migration) because it decides the cost of every future update (L014; REG-011); prefer interfaces stable and secure by default (L015; REG-003). No competing position recorded; coverage check records a partial tension of L295 (a maintainer row, not in this branch) with L014.
- P6 Version label: (a) avoid 0.x, alpha or beta in production (L016; OpenSSF; force correctness, reversibility); (b) labels are not uniform and many mature tools stay 0.x (force fit; open, inferred, no source read). REG-003, REG-008, REG-009.
- P7 Aggregate scores: (a) an input to judgment, not the verdict (L017; Scorecard's own documentation; force correctness of the decision); (b) a gate at a threshold via automation (inferred, not argued in any source read; force consistency, speed of review; best at large scale where per-package review is impossible). REG-001, REG-002, REG-016. Evidence recorded alongside: process scores had low explanatory power for vulnerability outcomes (R-squared 9 to 12 percent) and more reported vulnerabilities as the score rose (L018; one study, REG-016; replication not checked).
- P8 Popularity: (a) a weak proxy for scrutiny and community support (L019; force confidence); (b) can be hype and says nothing about fit (force suitability, reversibility). Row: never proof of quality or suitability. REG-003, REG-011, REG-012, REG-013, REG-017.
Context:
- REPLACEABILITY: whether the component is on a critical path or hard to replace moves the maintainer-diversity requirement (L007: "wins when the component is on a critical path or hard to replace" against "wins for small, stable, easily replaced or vendorable components")
Links:
- Related `OWNERSHIP.LIFECYCLE.2` (L014 see also L059: compatibility promise and Hyrum's Law; not merged)

##### OWNERSHIP.SELECTION.4 Dependency Weight

Intent: What a candidate drags in with it: indirect dependencies, tiny packages and the trust surface of its registry.
Rows: L020, L021, L022
Positions:
- P1 Count transitive dependencies as part of the cost and prefer candidates with few unnecessary indirect ones (L020, consensus; REG-003, REG-012, REG-018, REG-019). No competing position recorded.
- P2 Many tiny single-purpose packages (L021; evidence from JavaScript/npm, generalisable). (a) avoid or inline trivial packages (Kula et al., Pike; force control, security, cost of ownership; best where supply-chain exposure matters); (b) small shared packages give reuse and tested readability (open, not read in a source; force reuse, delivery speed). REG-018, REG-019, REG-020.
- P3 Account for ecosystem concentration: a few maintainer accounts reach most packages in a registry, so the reachable trust surface is the exposure (L022; npm evidence, registry-wide principle inferred; REG-003, REG-005, REG-018). No competing position recorded.
Context: none
Links: none
Stack pointers: L021 (JavaScript/npm evidence, generalisable); L022 (npm evidence)

##### OWNERSHIP.SELECTION.5 Authenticity, Provenance and Known Vulnerabilities at Adoption

Intent: What is checked before adoption about a candidate's identity, origin and known flaws.
Rows: L010, L012, L013, L1056, L1541
Positions:
- P1 Reject or defer candidates whose current version has known, unfixed vulnerabilities for the intended deployment, and re-check over the component's life (L010, consensus; REG-001, REG-003, REG-004, REG-005); the ongoing check sits in `OWNERSHIP.LIFECYCLE.5`.
- P2 Verify authenticity before adoption: official sources over secure links, prefer signed packages, check the name against look-alikes (typosquatting) and compromised forks (L012; REG-001, REG-003, REG-004, REG-005, REG-025); verify that the name resolves to the intended, vetted package, since a generated or suggested name is not evidence the package exists (L1056, majority; REG-1035, REG-1045); the same two checks as judged in the JavaScript guideline (L1541; origin: judged in the JavaScript guideline, not inherited; three T1 sources; REG-1555, REG-003, REG-1556). No competing position recorded.
- P3 Obtain and check provenance per component (SBOM, source composition, signatures, signed releases, hosting-platform protections), treat it as a selection signal, apply integrity checks and rebuild from verified source when binary provenance cannot be confirmed (L013, majority). (a) require provenance for all (REG-035; force security; best for high criticality); (b) provenance as a preferred signal only (REG-001; force cost of ownership; ecosystem coverage still partial, inferred). REG-001, REG-004, REG-035.
Context: none
Links:
- Related `OWNERSHIP.LIFECYCLE.4` (L012 and L013: channel rules, rebuild and mirror practice sit there; L1056 see also L062)
- Related `OWNERSHIP.LIFECYCLE.5` (L010 see also L067)

##### OWNERSHIP.SELECTION.6 Vetting Depth and Delegated Audit

Intent: How deep the hands-on vetting of a candidate goes and who does it.
Rows: L027, L077, L1540, L1542
Positions:
- P1 Scale vetting depth to criticality and exposure, judging risk as the sum over bad outcomes of cost times probability (L027; REG-003, REG-004, REG-012, REG-040; the scaling rule is inferred). (a) metadata and scores only (force delivery speed, cost; best for low-criticality, replaceable parts); (b) run the candidate's tests, sandboxed behaviour tests and code review for install scripts, exfiltration, obfuscation and TODO-marked security gaps (OpenSSF, Cox; force security, confidence; best for components handling untrusted input, credentials or cryptography). Row agreement: contested (SRC-C27), consensus (ADOPT-C12).
- P2 Delegate audit effort: reuse audits by trusted organisations and review only version differences, since a full manual audit of every dependency is too much work (L077, majority; REG-004, REG-038; concept neutral).
- P3 Prior framing from the JavaScript guideline (origin: judged in the JavaScript guideline, not inherited): before adding a dependency ask whether existing components suffice; test the candidate in isolation for unexpected indirect dependencies that would reach production (L1540; one T1 source, single-source; REG-003); example code shipped with a package's documentation is untrusted until reviewed (L1542; single-source; REG-1556).
Context:
- CRITICALITY_AND_EXPOSURE: "the same dependency can be acceptable in a hobby project and unacceptable in production" (L027); untrusted input, credentials or cryptography send it to hands-on review
Links: none
Stack pointers: L077 (Rust cargo-vet as the realisation); L1540, L1542 (origin stack node)

#### OWNERSHIP.LIFECYCLE Dependency Lifecycle

Intent: How an adopted dependency is declared, locked, obtained, updated, inventoried and watched over its life.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.LIFECYCLE.1 Declare and Lock

Intent: How an adopted dependency is declared completely and exactly and locked so that every environment obtains the same artifacts.
Rows: L043, L044, L045, L046, L1241
Positions:
- P1 Declare all dependencies completely and exactly in a manifest and run them in an isolated environment, never relying on implicitly installed system packages; a new developer needs only the language runtime, the dependency manager and one command (L043, consensus; REG-014). No competing position recorded.
- P2 Commit a lockfile recording the exact resolved tree, direct and transitive, so teammates, CI and deployment install identical dependencies (L044, consensus; REG-031, REG-037).
- P3 Install in CI and production from the lock only and fail if lock and manifest disagree (L045; the guarantee is grounded, the generalisation beyond one tool is inferred; REG-028, REG-031).
- P4 Verify downloaded artifacts by a cryptographic hash recorded in the lock, and enable a require-hashes mode for deploys where the tool supports it (L046; REG-031, REG-032, REG-037); hash verification must cover transitive dependencies (L1241; REG-025, REG-032, REG-1135).
Context: none
Links: none
Stack pointers: L043 (Bundler, pip with virtualenv named); L044 (npm, Cargo, Go go.sum, pip hashes as realisations); L045 (npm ci); L046 (pip --require-hashes, npm integrity, Go checksum database); L1241 (origin stack python, restated neutral)

##### OWNERSHIP.LIFECYCLE.2 Version Constraints and Resolution

Intent: How versions are constrained and resolved, and how far a version number is trusted as a compatibility promise.
Rows: L047, L049, L050, L051, L059, L061
Positions:
- P1 Resolution rule (L047; REG-011, REG-028, REG-031, REG-037). (a) a rule that keeps builds close to what the author tested, such as minimal version selection (force correctness, confidence; best when reproducibility matters more than automatic fixes, since upgrades become explicit); (b) newest-compatible resolution plus a lock (force delivery speed; best when a tool updates the lock automatically).
- P2 Pin all dependency types exactly in applications and services nobody else installs, so a faulty release shows as a reviewable change (L049, majority; REG-001, REG-028, REG-031). (a) exact pins plus an update bot (force confidence, security; best for deployables); (b) ranges plus lockfile only (force low noise; best when review capacity is scarce, but a lock only delays a bad range).
- P3 Libraries consumed by others declare ranges, not exact pins, and the library's own CI tests the range edges (L050, majority; REG-011, REG-028). Ranges: force consumer cognitive load, correctness of the shared graph. Exact pins in libraries: no source defends it (open). The test-range-edges half is inferred.
- P4 A lockfile does not replace constraints: the manifest range must still exclude known-broken versions (L051, consensus; REG-028).
- P5 Version number as compatibility (L059; REG-011, REG-030): (a) SemVer ranges are a usable contract (force delivery speed; best when the API is narrow and well declared); (b) SemVer is an estimate and tests are the evidence, with Hyrum's Law (force correctness, confidence; best as consumers and surface grow).
- P6 Diamond dependency: move versions forward or backward, or patch locally; tolerance differs by language (L061, consensus; REG-011).
Context:
- ARTIFACT_KIND: deployable application or service versus library consumed by others (L049: pin exactly "in applications and services that nobody else installs"; L050: libraries "should declare ranges")
Links:
- Related `OWNERSHIP.SELECTION.3` (L059 see also L014)
Stack pointers: L047 (Go minimal version selection); L049 (examples npm)

##### OWNERSHIP.LIFECYCLE.3 Updating

Intent: How and how fast an adopted dependency is moved to newer versions, and how a compromise is answered.
Rows: L052, L053, L054, L055, L056, L057, L058, L1543, L1544
Positions:
- P1 Cadence (L052; REG-001, REG-011, REG-012, REG-025, REG-035). (a) small, frequent, automated updates (force security, cost of ownership; best when tests are trustworthy); (b) upgrade only when there is need (force control, stability; best when verification is weak or deployments are costly and the risk of change exceeds the exposure).
- P2 Automate update proposals and group related ones; pinning raises pull-request volume, to be mitigated by scheduling, automerge of safe packages and grouping, not by abandoning pinning (L055, consensus; REG-001, REG-028, REG-029). JavaScript-guideline framing: an automated update and alert mechanism, security updates enabled and kept separate from feature updates because bundled fixes hinder adoption (L1543; origin: judged in the JavaScript guideline, not inherited; mechanism inferred, majority).
- P3 Apply fixes for known vulnerabilities urgently, bypassing any scheduled delay (L053, consensus; REG-001, REG-012, REG-029, REG-035, REG-043).
- P4 Routine (non-security) updates (L054; REG-029, REG-035, REG-036, REG-043). (a) a release-age cooldown of days to two weeks, since most observed attacks were detected within a week (force security; costs staleness of fixes that ship as ordinary releases; best when supply-chain exposure outweighs staleness, most deployables); (b) update immediately (force security through speed to patch; best when most updates are security fixes or the pipeline detects malicious content itself). The data in REG-036 is one author's analysis of 10 attacks (T3). L1543 records the cooldown benefit as unmeasured (one T1 assertion and vendor figures; an OpenSSF figure of about three days with no origin found; open).
- P5 Review release notes and diffs and rerun the project's tests, including integration tests specific to your usage (L056, consensus; REG-012).
- P6 Deploy dependency updates through staged rollouts rather than to every system at once (L057, consensus; REG-025).
- P7 "Live at Head" (L058; REG-011, REG-028, REG-030): (a) depend on the current version and make providers responsible for not breaking dependents, proven by dependents' tests (force speed of feedback, shared upgrade cost; best in a monorepo with provider-run downstream tests; organisation-scale); (b) version-pinned SemVer consumption (force control; best for external open-source consumption where dependents are invisible).
- P8 After a worm-style supply-chain compromise re-establish three things first: review the lockfiles, rotate all developer credentials, pin to versions published before the incident date (L1544; CISA's position, single T2 source, single-source; REG-1558; origin: judged in the JavaScript guideline, not inherited).
Context:
- TEST_TRUST_AND_EXPOSURE: how trustworthy the tests are, how costly deployments are, and the exposure to supply-chain attack (L052: "wins when tests are trustworthy" against "wins when verification is weak or deployments are costly"; L054: cooldown "wins when ... most deployables")
Links:
- Related `OWNERSHIP.LIFECYCLE.1` (L1544 see also L044 and L049)
Stack pointers: L054 and L055 (named update tools and cooldown settings); L1543 (origin stack tooling); L1544 (origin stack node)

##### OWNERSHIP.LIFECYCLE.4 Channels, Mirrors and Supply-Chain Integrity

Intent: Through which channels artifacts are obtained, what is kept as a fallback, and how the supply chain of the team's own tooling and packages is protected.
Rows: L062, L064, L065, L076, L1074, L1243, L1545, L263
Positions:
- P1 Obtain artifacts only through controlled, trusted channels (L062; REG-004, REG-031, REG-032, REG-035, REG-037): (a) a standardised package manager and an internal repository or mirror of sanctioned components, which also protects against upstream unavailability (force control, availability; best for larger organisations and regulated products); (b) direct pull from the public registry with lock and hashes (force cost of ownership; best for small teams). Also: official sources over secure links, prefer signed packages, deploy updates in staged or canary rollouts (L1243, consensus; REG-025).
- P2 For the highest assurance, rebuild every deployed open-source artifact from source in your own infrastructure, mirror source and be able to patch privately within days (L065; REG-031, REG-032, REG-035, REG-037). (a) rebuild everything (force security, control; best for critical infrastructure and supply-chain-targeted organisations; costs large engineering effort); (b) consume prebuilt verified artifacts (force cost of ownership).
- P3 Provenance protects the integrity of what a producer built but says nothing about the levels of its dependencies and does not address a dependency being removed: apply provenance verification recursively and address unavailability separately with a mirror or vendoring (L064, consensus; REG-022, REG-023).
- P4 Plan for an upstream package or version disappearing (L076, majority; REG-022, REG-035, REG-037): (a) keep a local cache, mirror or vendored copy (force availability; best for production-critical builds); (b) rely on an immutable public proxy or registry (force cost of ownership; best where the registry guarantees immutability).
- P5 The automation's own tool and plugin supply chain (extension servers, plugins, tool descriptors) is pinned, vetted and not auto-updated without review (L1074, majority; REG-1034, REG-1037; the pinning rule is inferred).
- P6 A project that publishes a package is itself a dependency of others and its publishing accounts are the takeover route: two-factor authentication on the publishing accounts of any registry; phishing-resistant multi-factor authentication on developer accounts after compromises (L1545, consensus; REG-1557, REG-1556, REG-1562, REG-1558; origin: judged in the JavaScript guideline, not inherited).
- P7 Build tools, compilers and interpreters are pinned and changed only through change management that audits unexpected changes and validates authenticity and integrity, while staying on versions that still receive security fixes (L263, majority; REG-004, REG-014, REG-178; moved here from `TRANSVERSE.ENVIRONMENTS`; grounded for the rule, the tension between "pinned" and "up to date" is inferred). Same family as P5 (the automation's own tooling).
Context:
- ORGANISATION_SIZE_AND_CRITICALITY: larger or regulated organisations, critical infrastructure and production-critical builds versus small teams (L062, L065, L076)
Links:
- Related `OWNERSHIP.SELECTION.5` (L1243 see also L012; L1056 see also L062)

##### OWNERSHIP.LIFECYCLE.5 Inventory, Watching and End of Life

Intent: How the team knows what it depends on, hears of flaws and abandonment, and meets legal duties for it.
Rows: L009, L066, L067, L079, L1242
Positions:
- P1 Maintain an inventory of every dependency, transitive included, and where it is deployed; generate the SBOM centrally (L066, consensus; REG-001, REG-012, REG-025, REG-035, REG-042); keep an SBOM over direct and transitive dependencies and scan it continuously against vulnerability databases (L1242, consensus; REG-025, REG-1135). No competing position recorded.
- P2 Continuously monitor vulnerability databases against the inventory for as long as the software is in service, with a plan for triage and update (L067, consensus; REG-004, REG-024, REG-025).
- P3 For each component confirm it is still maintained and not at end of life, and keep a plan of action for components that stop being maintained (L009, consensus; REG-004, REG-005, REG-011, REG-018).
- P4 Where law applies (for example the EU Cyber Resilience Act), due diligence on integrated third-party components, an SBOM and reporting component vulnerabilities to their maintainers are legal duties, not options (L079; primary text not read, wording inferred; REG-040).
Context:
- JURISDICTION: whether a law of this kind applies (L079: "where law applies", "jurisdiction EU")
Links:
- Related `OWNERSHIP.SELECTION.5` (L067 see also L010)

#### OWNERSHIP.CONTAINMENT Containment and Exit

Intent: How the effect of a dependency or an external system is bounded and how the team leaves it.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.CONTAINMENT.1 How Much Reversibility to Buy

Intent: How much lock-in is acceptable and how much exit capability is worth paying for.
Rows: L073, L074, L075, L078
Positions:
- P1 Treat lock-in as a spectrum across at least eight dimensions (vendor, product, version, architecture, platform, skills, legal, mental); avoiding one often creates another and open source removes only some (L073, majority; REG-011, REG-012, REG-026).
- P2 Evaluate lock-in by two separate quantities, cost to switch and likelihood of switching: high cost with low likelihood needs insurance only if worthwhile, low cost with high likelihood buys agility (L074, majority; REG-026).
- P3 Accept lock-in when it buys a commensurate pay-off and reduce switching cost only to where the insurance is cheaper than the expected loss (L075; REG-012, REG-026, REG-039, REG-187, REG-216). (a) accept priced lock-in, cheap portability only (force cost of ownership, delivery speed; best when switching likelihood is low and unique utility high); (b) minimise through wrapping and open standards (force exit risk, control; best for long-lived or regulated systems and critical rented services); (c) regulated or critical functions need a tested exit and an alternative (force exit risk, regulatory duty; best for financial entities and critical functions; the EU exit-strategy requirement is known only from summaries). Portability beyond the optimum raises total cost, and elaborate multi-cloud architectures forfeit the platform's benefit and create new lock-in.
- P4 For a rented service define the exit path before adopting (data export, replacement candidate, contract notice) in proportion to criticality (L078; inferred, "not assessable"; REG-004, REG-026).
Context:
- SWITCHING_LIKELIHOOD_AND_REGULATION: the likelihood and cost of switching and whether the function is regulated or critical move how much to insure (L074; L075: "wins when switching likelihood is low", "wins for financial entities and critical functions")
Links:
- Related `OWNERSHIP.SERVICES.3` (L078 see also L359: exit, portability and abstraction)
- Related `OWNERSHIP.CONTAINMENT.2` (L078 see also L035, L068)

##### OWNERSHIP.CONTAINMENT.2 Adapter Between Code and Dependency

Intent: Whether and how a thin boundary separates the team's code from a dependency or an external system whose model it does not control.
Rows: L035, L068, L342, L344, L345
Positions:
- P1 Assess exit and portability at selection time: keep credentials, data and integration logic exportable and put an abstraction between your code and the dependency (L035; REG-012, REG-021; inferred, T4 plus one T2 line). (a) wrap and keep an exit path (Cox; force exit risk, reversibility; best when the dependency is on a critical path or vendor behaviour is uncertain); (b) use directly and accept lock-in for speed (not sourced, inferred; force delivery speed; best when the dependency is core and stable).
- P2 Put a thin wrapper, containing only what the project needs, between your code and a dependency whose substitution is plausible, and keep external types out of the inside (L068; REG-012, REG-026, REG-034, REG-039). (a) wrap (force reversibility, exit risk, testability; best for volatile, security-sensitive or single-vendor dependencies and for external services); (b) do not wrap (a speculative abstraction carries cost, and the investment in reducing lock-in can raise total cost; force cost of ownership, cognitive load; best when switching probability is low and the dependency is a stable, standard interface).
- P3 Put an anti-corruption layer between your domain and an external system whose model you do not control, keeping business rules out of it (L344; REG-026, REG-186). (a) mandatory layer (force reversibility, design purity; best for multi-stage migrations, differing semantics, critical-path or uncertain vendors); (b) call the service directly (force cost of ownership, cognitive load; best when the service is core, stable and switching is unlikely). The layer adds latency and something to operate.
- P4 Encapsulate parsing of the external payload in one place (a boundary object) so the rest of the system is isolated from its shape (L342, majority; REG-186, REG-208).
- P5 Never expose a vendor's types or identifiers in your own stored data or public interfaces without a mapping you own (L345; inferred, "not assessable", no source states it as a rule; REG-026, REG-186).
Context:
- SWITCH_PROBABILITY_AND_VOLATILITY: how likely a swap is and how volatile, security-sensitive or single-vendor the dependency is (L068, L344)
Links:
- Related `OWNERSHIP.CONTAINMENT.1` (L035 and L068 see also L078, L359)

##### OWNERSHIP.CONTAINMENT.3 External Systems as Attached Resources

Intent: Whether a database, queue, cache or third-party service is treated as a resource reached through configuration, with no distinction in code between local and third-party.
Rows: L343, L1195
Positions:
- P1 Treat a third-party service as an attached resource: its location and credentials are configuration and the code makes no distinction between local and third-party services (L343, majority; REG-186, REG-207). (a) as stated (force reversibility, swap without code change; best when the service has a standard interface such as SMTP or SQL); (b) the distinction is real when semantics differ (force honest modelling; best when the vendor model is proprietary).
- P2 The same for the database and other backing services such as a queue or cache, swappable by changing configuration (L1195, consensus; REG-1109; origins WEB:OPS-C37 and WEB:ARCH-C27). Where configuration lives is a contested question of the origin (WEB:OPS-C35) and is not decided in the row.
Context: none
Links: none

##### OWNERSHIP.CONTAINMENT.4 Bounding Runtime Effect and Untrusted Responses

Intent: How the damage a dependency or a third-party response can do at runtime is bounded.
Rows: L069, L340
Positions:
- P1 Isolate risky dependencies at runtime (sandbox, least privilege) to bound the damage from bugs or compromise (L069, majority; practicality open; REG-003, REG-012).
- P2 Treat every third-party response as untrusted input: validate and sanitise before use, use TLS, do not follow redirects blindly (keep an allowlist of redirect targets) and cap the resources spent on a response (L340, consensus; REG-186, REG-194).
Context: none
Links: none

#### OWNERSHIP.SERVICES External Services

Intent: What to require of a rented service or hosted tool: availability fit, API stability, switching terms, contract and vendor assessment.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.SERVICES.1 Availability Fit and Commitments

Intent: Whether a rented service's availability commitment fits what the team itself promises, and what that commitment is worth.
Rows: L031, L033, L346, L347, L348, L349, L350
Positions:
- P1 Pick a service whose availability target is at least your own, since hard dependencies multiply availabilities, and set your own SLA with the dependencies' SLAs in view (L031, consensus; one T1 source, mathematically general; REG-007).
- P2 Read an SLA as a commercial instrument: a measured uptime percentage, a credit scale, a claim procedure with a deadline and evidence, exclusions, credits as the sole remedy; it does not promise the availability (L346, consensus; REG-125, REG-197; generalisation beyond the providers read is inferred).
- P3 Compare the remedy to your loss: if a service credit cannot cover what an outage costs you, mitigate by design (fallback, redundancy) (L347; inferred, "not assessable"; REG-197, REG-201).
- P4 Own your availability target and reliability design; the provider owns only what its published SLA defines, and tiers within one provider differ (L348, consensus; REG-197, REG-201).
- P5 Keep an internal SLO tighter than the SLA you sign or advertise (L349, consensus; REG-125).
- P6 Plan from a dependency's observed behaviour as well as its stated target, and do not assume it will over-deliver (L350, majority; REG-125).
- P7 Monitor reachability, latency and errors of every external service as part of adopting it (L033, consensus; inferred, not read in full; no source id).
No competing position recorded in any of the seven rows.
Context: none
Links:
- Related `ASSURANCE.AVAILABILITY` (routing note of L031: the mechanisms that guarantee availability sit there)

##### OWNERSHIP.SERVICES.2 API Stability and Deprecation

Intent: What the team requires of a service API's stability promise and how it protects itself against removal.
Rows: L034, L351, L353, L354, L355
Positions:
- P1 Before depending on a service API read its stability tiers and deprecation policy and prefer providers that publish a minimum notice and keep two versions working side by side during a transition (L034, consensus; REG-008, REG-009, REG-021; practice in the wild is weaker, T4 only).
- P2 Consume the machine-readable deprecation signals (the Deprecation and Sunset headers) and route them to an alert (L351, consensus; REG-182, REG-183; that consumers act on them is not sourced, open).
- P3 How an API evolves (L353; REG-009, REG-213): (a) explicit major versions with a bounded deprecation window (force provider speed, clean foundation; best when consumers are few or controlled); (b) an indefinitely compatible date-pinned surface (force consumer stability, trust; best for infrastructure-like APIs with a large consumer base and funds to carry old behaviour).
- P4 Pin the API version you integrate against when the provider allows it, and upgrade deliberately (L354, majority; REG-009, REG-213).
- P5 Expect real deprecation notice to be shorter and less reliable than policy documents suggest; do not treat a published window as a guarantee (L355, majority; inferred; REG-021, REG-182, REG-183).
Context: none
Links: none
Stack pointers: L034 (examples Kubernetes and Google APIs); L351 (HTTP)

##### OWNERSHIP.SERVICES.3 Data Export and Switching Terms

Intent: Whether the team can take its data and integration logic out of a rented service, and on what terms.
Rows: L356, L357, L359, L1112
Positions:
- P1 Verify at selection time that the service can export all your data in a commonly used, machine-readable format through an open interface, and test the export once before depending on it (L356, consensus; the legal duty is grounded via a secondary page, "test the export" is inferred; REG-187, REG-198).
- P2 Require from a cloud or data-processing provider a contract covering switching: notice and transition terms, data return, no punitive egress charges (in the EU, egress and switching charges must disappear from 12 January 2027) (L357, consensus; exact notice and switching figures open; REG-187).
- P3 Mirror or retain an independent copy of critical data held in a service and keep credentials and integration logic exportable, so exit does not depend on the provider's cooperation (L359, majority; inferred; REG-026, REG-187, REG-216).
- P4 For managed services and SaaS assume the provider is responsible for its infrastructure and the customer for its own data; verify what the provider's backups cover and for whose recovery, and keep an independent copy of what the team cannot afford to lose (L1112, consensus on one source; inferred: the split of responsibility is grounded, the backup consequence and the independent-copy advice are inferred; REG-1060, REG-1070). Moved here from `OPERATION.RECOVERY`; the independent copy is the same advice as P3, the backup verification is the new element.
No competing position recorded in any of the four rows.
Context:
- JURISDICTION: where law applies (L356: "where law applies; elsewhere inferred"; L357: "jurisdiction EU")
Links:
- Related `OWNERSHIP.CONTAINMENT.1` (L359 see also L035, L068, L078)
- Related `OWNERSHIP.STANCE.2` (L1112 see also L040)
Stack pointers: L1112 (REG-1070 describes one cloud provider)

##### OWNERSHIP.SERVICES.4 Commercial and Contract Terms

Intent: What the contract and the price model must say so that the cost and the legal position of renting are known and owned.
Rows: L358, L360, L361
Positions:
- P1 Where a service processes personal data a written processor contract is mandatory: documented instructions only, confidentiality, security measures, authorised sub-processors, assistance with data-subject rights, deletion or return at the end, audit rights; the controller chooses processors giving sufficient guarantees (L358, consensus; EU GDPR; unofficial copy of the text; REG-198). No competing position recorded.
- P2 Price risk belongs in selection: understand the pricing model, unit economics and egress, give cost an owner, expect unmetered cost exposure from usage-based services (L360, majority; no T1 or T2 source on contractual price caps, open; REG-185, REG-187, REG-214).
- P3 A dependency's licence or commercial terms can change unilaterally: record who controls the licence of each critical open-source or hosted dependency and decide in advance what to do if it changes (L361; REG-212, REG-215; the rule is inferred). (a) single-vendor-controlled projects are acceptable when use is non-competitive and the vendor's rationale credible (force delivery speed, features; best for end-user use); (b) prefer foundation-governed or multi-vendor projects, because relicensing creates legal doubt and stranded code (force exit risk, control; T4 source; best when you build services that could be read as competitive or must outlive the vendor).
Context:
- JURISDICTION: the processor contract is stated for the EU (L358: "jurisdiction EU (GDPR)", "where applicable")
Links: none

##### OWNERSHIP.SERVICES.5 Vendor Assessment

Intent: How a vendor is assessed before and during the dependence, and how deep the assessment goes.
Rows: L363, L364, L365, L378
Positions:
- P1 Assess a vendor's security and supply-chain posture before depending on it: authentication options, evidence of intrusion (logs retained, at least six months in the guide), SBOM and open-source governance, vulnerability disclosure policy and CVE practice, patch support (L363, consensus; REG-194, REG-196, REG-199). No competing position recorded.
- P2 Scale vendor assessment depth to criticality and data sensitivity and repeat it through the contract life, not only at selection (L364; REG-196, REG-199). (a) depth by criticality (force speed, cost of review; best when vendors are many and most are low-risk); (b) a uniform baseline checklist for every vendor (the six-area list; force simplicity and fairness of process; best for small teams without capacity to triage). Lifecycle grounded, scaling choice inferred.
- P3 Third-party assurance reports (SOC 2, ISO/IEC 27001) are evidence of a vendor's controls, not proof of fit; read scope, period and exceptions (L365; open, "not assessable", no source id).
- P4 Evaluate non-library tools and platforms (dev tools, CI service, hosting) with the same criteria as services: availability, deprecation promise, export of pipeline definitions and data, security posture, cost model, supply-chain exposure of the plugin ecosystem (L378; open, inferred composition; REG-086, REG-195, REG-200).
Context:
- CRITICALITY_AND_DATA_SENSITIVITY: moves how deep the assessment goes (L364: "scale vendor assessment depth to criticality and data sensitivity")
Links: none

##### OWNERSHIP.SERVICES.6 CI and Hosting Services as Supply Chain

Intent: What the team requires of the build, CI and hosting services that execute with its secrets and produce what it ships.
Rows: L366, L367, L368
Positions:
- P1 Treat a CI or hosting service as part of your supply chain: a compromise of a third-party action or service executes with your secrets (L366, consensus; REG-195, REG-200).
- P2 Pin third-party CI components to an immutable identifier (full commit SHA taken from the official repository, not a fork), audit their source, set the default token permission to read-only and raise it per job (L367, consensus; REG-195).
- P3 Do not run self-hosted CI runners on untrusted code (public repositories): they are not guaranteed ephemeral and clean and can be persistently compromised (L368, consensus; REG-195).
Context: none
Links: none
Stack pointers: L367 (GitHub Actions; pointer for equivalents on other CI services); L368 (GitHub Actions)

#### OWNERSHIP.LICENCE Licences

Intent: Which licence obligations a dependency brings and how the team classifies, decides and declares them.
Rows: none directly (see children)
Positions: see children
Context: see children

##### OWNERSHIP.LICENCE.1 Reading and Classifying Licences

Intent: How a dependency's licence is read and classified against what the team does with the code.
Rows: L036, L362, L370, L371, L372
Positions:
- P1 Check that the licence is present, clear and acceptable for the intended use; a project that will not state its licence is less likely to follow other good practices (L036, consensus; the compatibility analysis itself is not covered; REG-001, REG-003, REG-012, REG-017).
- P2 Obligations are triggered by what you do with the code (ship it, link it, modify it, run it as a service): classify each dependency by licence family and by your distribution model before adopting it (L370, consensus; REG-188, REG-189, REG-210).
- P3 Compatibility is directional and pair-specific (Apache-2.0 code may go into a GPLv3 work but not the reverse; the FSF does not accept Apache-2.0 as GPLv2-compatible) (L371, consensus; the FSF list could not be fetched; REG-188, REG-202).
- P4 Distinguish the "or later" variants and the exceptions and state them with SPDX expressions (L372, consensus; REG-191).
- P5 A source-available licence with a field-of-use restriction is not open source by the OSI definition, so it cannot be treated under open-source licence policy (L362, consensus on the definition; the application to a named licence is inferred; REG-190, REG-212).
No competing position recorded in any of the five rows.
Context:
- DISTRIBUTION_MODEL: what the team does with the code (L370: "obligations are triggered by what you do with the code")
Links: none

##### OWNERSHIP.LICENCE.2 Policy and Process

Intent: Which licence classes are allowed and who decides, and the process that keeps compliance working.
Rows: L373, L377
Positions:
- P1 A written class policy (allowed, notice-only, review-needed, prohibited, by distribution model, with a named decider) (L373; REG-188, REG-189, REG-210). (a) conservative: notice licences allowed, strong copyleft restricted to server-side or internal use, AGPL, SSPL and non-commercial licences prohibited (force control of own source, cost of audit; best for companies shipping client or embedded software or holding proprietary code); (b) allow copyleft where obligations are understood and met (force delivery speed, reuse; best for teams hosting only or publishing their own code under compatible terms). The conservative example is one organisation's choice, not a standard.
- P2 Run a defined open-source compliance process: identified roles, process locations and a way to keep it working over time; ISO/IEC 5230 (OpenChain) is the standard and can be self-certified (L377, majority; grounded for the summary, inferred for details; REG-193).
Context:
- DISTRIBUTION_MODEL: shipping client or embedded software or holding proprietary code versus hosting only (L373: "wins for companies shipping client or embedded software" against "wins for teams hosting only")
Links:
- Related `OWNERSHIP.LICENCE.1` (L373 policy classes follow the classification of L370)

##### OWNERSHIP.LICENCE.3 Network Copyleft and Separate Components

Intent: How network-copyleft code and separately run copyleft services are treated.
Rows: L374, L375
Positions:
- P1 Network-copyleft code (AGPL) is a special case: modifying it and letting users interact with it over a network triggers a source offer; decide it separately from GPL (L374, majority; REG-188, REG-189, REG-210). No competing position recorded.
- P2 Using an unmodified copyleft service as a separate network component is not the same as linking it into your program; the question is the interface, not the proximity (L375; open, "not assessable": the boundary between linking and separate programs was not read; REG-188). No competing position recorded.
Context: none
Links: none

##### OWNERSHIP.LICENCE.4 Declaring the Team's Own Licence

Intent: How licence and copyright of the team's own files are declared so that compliance can be checked mechanically.
Rows: L376
Positions:
- P1 Declare the licence and copyright of every file machine-readably (SPDX identifiers in headers, licence texts in a licences directory) so compliance can be checked by tools (L376, majority; REG-191, REG-192). No competing position recorded.
Context: none
Links: none

## Routing objections

Twelve were raised; each is resolved in `../../objections/resolution.md`. Moved (row now sits on the target branch, no longer listed): L311 and L341 to `CONSTRUCTION`, L369 to `ASSURANCE.ARTIFACT`. Received from other branches: L1112 (from OPERATION), L263 (from TRANSVERSE). Kept (listed, with the reason it stays).

| row | attached here | would route to | reason | confidence | resolution |
|---|---|---|---|---|---|
| L312 | `OWNERSHIP.SELECTION.2` | `CONSTRUCTION.PARADIGM` (paradigm half only) | the row's second half chooses the programming paradigm per part by intent; the first half (technology by problem fit) stays here | high | kept: a row is not split and the lead clause (technology by problem fit) agrees with L023 here; CONSTRUCTION.PARADIGM.1 already carries the paradigm by L1526 and points to L312 |
| L330 | `OWNERSHIP.STANCE.4` | `CONSTRUCTION.DESIGN` | designing for probable future usage is where design effort is spent; kept here only for its tension with L038 | medium | kept: it is the contrary position to L038 on one contested question (build speculatively or not); the judge needs both on one node, and DESIGN.2 already points to L330 |
| L1208 | `OWNERSHIP.STANCE.4` | `CONSTRUCTION.DESIGN` | investing in making software easy to modify is a design-effort statement, not an adopt-or-write one | medium | kept: it states the same do-not-build-speculatively claim as L038, and its tension with L330 is judged on this node |
| L342 | `OWNERSHIP.CONTAINMENT.2` | `CONSTRUCTION.BOUNDARY` | encapsulating payload parsing in one boundary object is parsing at the edge | medium | kept: the claim is isolation of the system from an external model (the adapter), with L344 and L345 on this node; BOUNDARY.1 is about converting input to a precise type |
| L358 | `OWNERSHIP.SERVICES.4` | `TRANSVERSE.PRIVACY` | a written processor contract for personal data is a privacy obligation | medium | kept: it is a contract term of renting a service (this node's subject); no TRANSVERSE.PRIVACY node holds contract terms |
| L367 | `OWNERSHIP.SERVICES.6` | `CHANGE_FLOW.BUILD` | pinning CI components and read-only default token permission are build-pipeline practice | low | kept: it belongs with L366 (a CI service is part of the supply chain) and L368; CHANGE_FLOW.BUILD has no node on pipeline security |
| L368 | `OWNERSHIP.SERVICES.6` | `CHANGE_FLOW.BUILD` | runner hygiene is build-pipeline practice | low | kept: same cluster as L366 and L367 |
| L1544 | `OWNERSHIP.LIFECYCLE.3` | `TRANSVERSE.SECURITY` | the response to a supply-chain compromise is vulnerability handling | low | kept: its content is lockfile review and pinning to earlier versions (dependency lifecycle), and the node intent names how a compromise is answered; the credential rotation part is held by L252 in TRANSVERSE.CONFIG |
| L1545 | `OWNERSHIP.LIFECYCLE.4` | `TRANSVERSE.SECURITY` | hardening the team's own publishing accounts is account security, not adoption of a dependency | medium | kept: the node intent covers the supply chain of the team's own packages, and no TRANSVERSE.SECURITY node (programme practice) holds account protection |
