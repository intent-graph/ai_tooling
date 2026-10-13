# OWNERSHIP branch refinement: result

Full records, positions and links: `branch.md` beside this file. Check: `check_branch.py`. Rules: `../../brief_branch.md`.

## L1 headline

Pinned: 36 nodes (1 L1, 6 L2, 29 L3); 134 rows attached, 0 unattached; check_branch.py prints PASS; 12 routing objections.

- The OWNERSHIP branch is cut below its six L2 nodes into 29 L3 nodes, each holding the competing positions of one decision, listed without verdict. [grounded: the script proves the 134 routed rows are each attached once, below the L2 node they were routed to]
- Positions are the evidence's own: where a row records competing practices they are listed with force and best-when condition; where it records none, "no competing position recorded" says so. [grounded]
- Five maintainer rows (L308, L310, L311, L312, L330) appear as named MAINT positions; eight rows judged in the JavaScript guideline (L1537, L1539 to L1545) appear as one position among others. [grounded: the script checks the MAINT rows; the JavaScript-origin rows were read from the ledger]
- 12 rows may belong to other branches (mainly CONSTRUCTION and TRANSVERSE); none was moved. [inferred: my reading, not checked with the owners of those branches]

## L2 claims

Pinned: 36 nodes (1 L1, 6 L2, 29 L3); 134 rows attached, 0 unattached; check_branch.py prints PASS; 12 routing objections.

- `OWNERSHIP.STANCE` (13 rows, 4 L3): the open choices are whether the default is to reuse or to minimise dependencies (core versus non-core moves it), where to run scheduled work, and building for probable use versus today only (L038 against L330 is an explicit contradiction in the ledger). Context variables: CORENESS, COST_OF_STRUCTURAL_CHANGE, each quoted from a row. [grounded]
- `OWNERSHIP.SELECTION` (39 rows, 6 L3): most signals are uncontested practices (criteria, activity, transitive cost, authenticity). The contested ones are who may introduce a dependency, boring-first against staged novelty, maintainer diversity, score gating, popularity, tiny packages and vetting depth. Context variables: REGULATION_AND_SCALE, EXPERIMENT_CAPACITY, REPLACEABILITY, CRITICALITY_AND_EXPOSURE. [grounded for the listing; inferred where a row says a contrast is inferred (L028, L017 b, L035 b)]
- `OWNERSHIP.LIFECYCLE` (32 rows, 5 L3): declaring and locking is uncontested; contested are the resolution rule, exact pins against ranges, update cadence, cooldown, Live at Head, mirrors and rebuild-everything. Context variables: ARTIFACT_KIND, TEST_TRUST_AND_EXPOSURE, ORGANISATION_SIZE_AND_CRITICALITY, JURISDICTION. [grounded; cooldown benefit is open (L054, L1543)]
- `OWNERSHIP.CONTAINMENT` (14 rows, 4 L3): the open choice is how much reversibility to buy (accept priced lock-in against wrapping against a tested exit) and whether to put a wrapper or anti-corruption layer in. Context variables: SWITCHING_LIKELIHOOD_AND_REGULATION, SWITCH_PROBABILITY_AND_VOLATILITY. [grounded]
- `OWNERSHIP.SERVICES` (26 rows, 6 L3): mostly uncontested requirements; contested are the API evolution model (major versions against date-pinned), single-vendor against foundation-governed dependencies, and vendor assessment depth. Several rows are inferred or open (L347, L365, L378). Context variables: JURISDICTION, CRITICALITY_AND_DATA_SENSITIVITY, DISTRIBUTION_OF_BUILD_OUTPUT. [grounded for the listing; inferred or open for the rows named]
- `OWNERSHIP.LICENCE` (10 rows, 4 L3): classification rules are uncontested; the one contested decision is the class policy (conservative against allowing copyleft). L375 is open. Context variable: DISTRIBUTION_MODEL. [grounded; open for L375]
- Routing objections (12): L311, L312 to CONSTRUCTION.PARADIGM; L330, L1208 to CONSTRUCTION.DESIGN; L341, L342 to CONSTRUCTION.BOUNDARY; L358 to TRANSVERSE.PRIVACY; L369 to ASSURANCE.ARTIFACT; L367, L368 to CHANGE_FLOW.BUILD; L1544, L1545 to TRANSVERSE.SECURITY. [inferred]
- No split topic concerns OWNERSHIP in `tree_l2.md`, so no node is an index node. [grounded]

## L3 full

Pinned: 36 nodes (1 L1, 6 L2, 29 L3); 134 rows attached, 0 unattached; check_branch.py prints PASS; 12 routing objections.

Each line: node, rows, what is competing (full text in `branch.md`), context variable. Certainty at the end of the line is mine for the listing; row-level certainties are in `branch.md`.

STANCE
- `OWNERSHIP.STANCE.1` What a New Dependency or Layer Must Earn: L001, L037, L308. Necessity first and ongoing liability (no competitor) against the MAINT rule of defaulting to not creating a layer, with the database-centric default as the recorded alternative. No context variable. [grounded]
- `OWNERSHIP.STANCE.2` Write, Adopt or Rent per Need: L002, L040, L310, L311. Reuse by default, minimise dependencies, build core, build only what cannot be better met; rent non-core against rent broadly; MAINT built-in over custom; MAINT scheduling where the data lives against an external orchestrator. Context: CORENESS (L002, L040). [grounded; L040 inferred]
- `OWNERSHIP.STANCE.3` Bringing Code Inside: Copy, Vendor, Upstream: L070, L071, L072. Copy a tiny surface against depend (notably cryptography); vendor or monorepo against registry with lock; upstream instead of forks (no competitor). No context variable. [grounded; the opposing arguments of L070 inferred]
- `OWNERSHIP.STANCE.4` Speculative Building and Probable Use: L038, L330, L1208. No speculative functionality against MAINT probable-use design; a modifiability-investment variant with a recorded tension. Context: COST_OF_STRUCTURAL_CHANGE (L330). [grounded]

SELECTION
- `OWNERSHIP.SELECTION.1` Evaluation Process and Admission Gate: L003, L004, L005, L028, L029, L030, L042, L1537, L1539. Explicit criteria in context, systematic and written, recorded reasons, aggregators (no competitors); sanctioned list against team-level choice; JavaScript-guideline framing of the admission gate as a prior position. Context: REGULATION_AND_SCALE (L028). [grounded; L028 contrast inferred; L1537 and L1539 carry no claim of their own]
- `OWNERSHIP.SELECTION.2` Fit, Maturity and Novelty: L023, L024, L025, L312, L1227, L1228, L1230. Fit to requirements and MAINT problem fit; boring first with innovation tokens; staged novelty (assess, trial, adopt); perpetual operating cost. Context: EXPERIMENT_CAPACITY (L024). [grounded]
- `OWNERSHIP.SELECTION.3` Project Health and Compatibility Signals: L006, L007, L008, L011, L014, L015, L016, L017, L018, L019, L041. Several maintainers against tolerate small projects; version label avoid 0.x against not uniform; scores as input against threshold gate; popularity as proxy against hype; activity, responsiveness, disclosure policy, compatibility promise uncontested. Context: REPLACEABILITY (L007). [grounded; L016 b open; L017 b inferred]
- `OWNERSHIP.SELECTION.4` Dependency Weight: L020, L021, L022. Transitive cost and ecosystem concentration uncontested; tiny packages avoid or inline against reuse (b open). No context variable. [grounded for npm evidence, inferred for other registries in L022]
- `OWNERSHIP.SELECTION.5` Authenticity, Provenance and Known Vulnerabilities at Adoption: L010, L012, L013, L1056, L1541. Vulnerability check and authenticity (no competitor); provenance required for all against preferred signal only. No context variable. [grounded]
- `OWNERSHIP.SELECTION.6` Vetting Depth and Delegated Audit: L027, L077, L1540, L1542. Metadata only against hands-on test and review, scaled to criticality; delegated audit; JavaScript-guideline framing of isolation testing and untrusted example code. Context: CRITICALITY_AND_EXPOSURE (L027). [grounded; the scaling rule inferred]

LIFECYCLE
- `OWNERSHIP.LIFECYCLE.1` Declare and Lock: L043, L044, L045, L046, L1241. Manifest, lockfile, install from lock, hash verification; no competitor recorded. No context variable. [grounded; generalisation of L045 inferred]
- `OWNERSHIP.LIFECYCLE.2` Version Constraints and Resolution: L047, L049, L050, L051, L059, L061. Minimal version selection against newest-compatible plus lock; exact pins against ranges plus lock for applications; ranges for libraries; SemVer as contract against estimate; lock does not replace constraints; diamond dependency. Context: ARTIFACT_KIND (L049, L050). [grounded; L050 half inferred]
- `OWNERSHIP.LIFECYCLE.3` Updating: L052, L053, L054, L055, L056, L057, L058, L1543, L1544. Continuous against only on need; cooldown against immediate; Live at Head against pinned SemVer; urgent security fixes, automation, review, staged rollout and compromise response uncontested. Context: TEST_TRUST_AND_EXPOSURE (L052, L054). [grounded; cooldown benefit open]
- `OWNERSHIP.LIFECYCLE.4` Channels, Mirrors and Supply-Chain Integrity: L062, L064, L065, L076, L1074, L1243, L1545. Managed mirror against direct pull; rebuild everything against prebuilt verified; mirror or vendor against rely on immutable proxy; recursive provenance, tool supply chain and publishing-account hardening uncontested. Context: ORGANISATION_SIZE_AND_CRITICALITY (L062, L065, L076). [grounded; L1074 pinning rule inferred]
- `OWNERSHIP.LIFECYCLE.5` Inventory, Watching and End of Life: L009, L066, L067, L079, L1242. Inventory with SBOM, continuous vulnerability monitoring, end-of-life tracking, legal duty where law applies; no competitor recorded. Context: JURISDICTION (L079). [grounded; L079 wording inferred]

CONTAINMENT
- `OWNERSHIP.CONTAINMENT.1` How Much Reversibility to Buy: L073, L074, L075, L078. Lock-in as spectrum, cost against likelihood, accept priced lock-in against minimise against tested exit for regulated or critical functions, exit path before renting. Context: SWITCHING_LIKELIHOOD_AND_REGULATION (L074, L075). [grounded; L078 inferred]
- `OWNERSHIP.CONTAINMENT.2` Adapter Between Code and Dependency: L035, L068, L342, L344, L345. Wrap against use directly (L035, L068); mandatory anti-corruption layer against call directly (L344); one parsing boundary and no vendor types in own data (no competitor). Context: SWITCH_PROBABILITY_AND_VOLATILITY (L068, L344). [grounded; L035 and L345 inferred]
- `OWNERSHIP.CONTAINMENT.3` External Systems as Attached Resources: L343, L1195. As stated against distinction is real when semantics differ; same rule for backing services. No context variable. [grounded]
- `OWNERSHIP.CONTAINMENT.4` Bounding Runtime Effect and Untrusted Responses: L069, L340, L341. Runtime isolation, untrusted responses (no competitor); tolerant reader against strict validation, with an inferred synthesis. No context variable. [grounded; practicality of L069 open; synthesis of L341 inferred]

SERVICES
- `OWNERSHIP.SERVICES.1` Availability Fit and Commitments: L031, L033, L346, L347, L348, L349, L350. Seven uncontested requirements on target fit, SLA reading, remedy against loss, ownership, internal SLO, observed behaviour and monitoring. No context variable. [grounded; L033 and L347 inferred]
- `OWNERSHIP.SERVICES.2` API Stability and Deprecation: L034, L351, L353, L354, L355. Major versions with deprecation window against date-pinned compatibility; stability tiers, deprecation headers, pinning and unreliable notice uncontested. No context variable. [grounded; L351 consumer action open; L355 inferred]
- `OWNERSHIP.SERVICES.3` Data Export and Switching Terms: L356, L357, L359. Export check, switching contract terms, independent copy; no competitor recorded. Context: JURISDICTION (L356, L357). [grounded; test-the-export and L359 inferred; EU figures open]
- `OWNERSHIP.SERVICES.4` Commercial and Contract Terms: L358, L360, L361. Processor contract and price risk uncontested; single-vendor-controlled against foundation-governed dependencies. Context: JURISDICTION (L358). [grounded; L361 rule inferred; price caps open]
- `OWNERSHIP.SERVICES.5` Vendor Assessment: L363, L364, L365, L378. Posture checklist and non-library tools uncontested; depth by criticality against uniform baseline; assurance reports as evidence, not proof. Context: CRITICALITY_AND_DATA_SENSITIVITY (L364). [grounded for L363; L365 and L378 open]
- `OWNERSHIP.SERVICES.6` CI and Hosting Services as Supply Chain: L366, L367, L368, L369. CI as supply chain, pinning, no self-hosted runners on untrusted code (no competitor); build levels from provenance only to hardened. Context: DISTRIBUTION_OF_BUILD_OUTPUT (L369). [grounded]

LICENCE
- `OWNERSHIP.LICENCE.1` Reading and Classifying Licences: L036, L362, L370, L371, L372. Five uncontested rules: licence present, obligations by use, directional compatibility, SPDX expressions, source-available is not open source. Context: DISTRIBUTION_MODEL (L370). [grounded; L362 application inferred]
- `OWNERSHIP.LICENCE.2` Policy and Process: L373, L377. Conservative class policy against allow copyleft where obligations are met; defined compliance process. Context: DISTRIBUTION_MODEL (L373). [grounded; L377 details inferred]
- `OWNERSHIP.LICENCE.3` Network Copyleft and Separate Components: L374, L375. AGPL decided separately; a separate network component is not linking (L375 open). No context variable. [grounded for L374; open for L375]
- `OWNERSHIP.LICENCE.4` Declaring the Team's Own Licence: L376. Machine-readable declaration per file; no competitor recorded. No context variable. [grounded]
