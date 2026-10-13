# Skeleton of the stack-neutral software-development philosophy graph (round 2, no node created)

Proposed tree for one IntentGraph, cut on `../target_hierarchy_proposal.md` (provisional: the maintainer has not ratified it). Every ledger row of `../01_consolidate/claims_ledger.md` is attached to exactly one node. This file structures the graph and lists the competing positions per node; it states no verdict and judges no claim. Rows weigh as recorded by the ledger (a maintainer row, source MAINT-S01, is one position among others).

Pinned:
- Nodes: 170 (ROOT 1; OWNERSHIP 39; ASSURANCE 53; CHANGE_FLOW 32; OPERATION 23; TRANSVERSE 22). By level: L1 5, L2 36, L3 128.
- Rows attached: 460 of 460; unattached: 0; attached twice: 0.
- Rows by branch: OWNERSHIP 119, ASSURANCE 151, CHANGE_FLOW 99, OPERATION 61, TRANSVERSE 30.
- Decision nodes with positions (OWNERSHIP and ASSURANCE): 78. Stack-pointer rows (stack not neutral in the ledger): 39, tagged on their node.
- Awaiting scope (rows touching topics without a node, each also attached above): backup and recovery 8, technical debt and decommissioning 7, AI agents as contributors 3.

## How to read

- A node record gives uid, name, the question it decides (never its answer), the ledger rows it owns, the positions in the evidence with ledger ids, the forces in tension, the context variables that move the choice, and the decision nodes it carries out (`Realizes`).
- `P1, P2...` are competing positions recorded in the ledger; the word "against" separates alternatives; no position is marked as winning. "No competing position recorded" means the ledger holds one practice for the row.
- `Rows: -` means the node is a roll-up of its children. `Lnnn-Lmmm` means every row in the range. A row listed under Positions of a node but owned elsewhere is cited, not owned.
- Default team context is not set. `Context` lists variables from the table below; the max rule of the later judging step will need a default for them (open for the maintainer).
- Stack-specific rows stay attached and carry a `Stack pointers` line: they are pointers for stack guidelines, not stack-neutral claims.

## Partition rationale

### The cut

- L0 and the five L1 branches are the proposal, in its order: OWNERSHIP and ASSURANCE are decision branches (first, judged first); CHANGE_FLOW and OPERATION are realization branches that link back to the decision nodes they carry out; TRANSVERSE holds cross-cutting practice.
- L2 is cut top-down from each branch's role, then rows were attached. OWNERSHIP: the five decisions the maintainer named (STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES) plus LICENCE (extension: eleven rows, L036, L362, L370-L377, form one decision that no other node holds). ASSURANCE: RULES (how guarantees are placed and kept trustworthy) and one placement node per property (BEHAVIOUR, CONTRACTS, DATA_INTEGRITY, DOCS_SYNC, SECURITY, PERFORMANCE, AVAILABILITY) plus ARTIFACT (extension: L048, L151, L152 guarantee that what runs is what was built from reviewed source, a property none of the seven holds).
- Each ASSURANCE property node states the mechanisms and stages that compete to guarantee it, the way the web guideline's allocation placements state competing tiers. L3 nodes are the sub-decisions inside a property (for example the test-level mix inside BEHAVIOUR).
- CHANGE_FLOW L2: INTEGRATION, REVIEW, BUILD, RELEASE, DEPLOY, ROLLBACK, MEASURE and DATA_CHANGE (its rows come from the data-change research and the maintainer migration doctrine, enough for a node group of its own). OPERATION L2: RELIABILITY, ALERTING, TELEMETRY, INCIDENTS, CAPACITY, READINESS, RUNBOOKS, FEEDBACK. TRANSVERSE L2: DOCS, SECURITY, CONFIG, ENVIRONMENTS, DESIGN.

### Routing rules

1. One owner per row: the node whose decision the row grounds most directly. Positions cite rows owned elsewhere by id.
2. A row that says which mechanism or stage guarantees a property goes to the ASSURANCE node of that property; a row that says how a change is carried out goes to the realization branch, which links back with `Realizes`.
3. A row about adopting, choosing, keeping or leaving a component, library, tool or service goes to OWNERSHIP, including the service-call rows that shape the boundary (CONTAINMENT.2) but not the rows that guarantee availability (ASSURANCE.AVAILABILITY.1).
4. Stack-specific rows stay attached where their subject sits and are tagged as stack pointers; none is dropped or moved to a stack branch here.
5. Rows touching the three topics outside the maintainer's six (backup and recovery, technical debt, AI agents as contributors) get no node of their own: each stays attached to the node of its subject and is also listed under Awaiting scope.
6. Where a row states several things, it is owned by the node of its first claim; merged ledger rows keep their ledger placement.

### Mapping of the coverage check's central-decision candidates

- A, B, C, D (default stance, selection, lifecycle, containment and exit): OWNERSHIP.STANCE, SELECTION, LIFECYCLE, CONTAINMENT; external-service requirements of D are OWNERSHIP.SERVICES.
- F (what is releasable): ASSURANCE.BEHAVIOUR.1 to .6 and ASSURANCE.RULES. J (service boundaries): ASSURANCE.CONTRACTS. R (TDD stance, coverage): ASSURANCE.BEHAVIOUR.4 and .6.
- H (rollout, rollback, production verification, error budget): ASSURANCE.AVAILABILITY.4 with CHANGE_FLOW.DEPLOY.3, ROLLBACK.1 and OPERATION.RELIABILITY.2. I (environment set, parity, how tests run safely): CHANGE_FLOW.DEPLOY.2, ASSURANCE.BEHAVIOUR.9, TRANSVERSE.ENVIRONMENTS.
- E, G, Q (release model and integration, review, delivery measures): CHANGE_FLOW.INTEGRATION, RELEASE, REVIEW, MEASURE. K, L, M (reliability targets, paging and incidents, telemetry): OPERATION.RELIABILITY, ALERTING, INCIDENTS, TELEMETRY.
- N (documentation) and O (security): decision part ASSURANCE.DOCS_SYNC and ASSURANCE.SECURITY, practice part TRANSVERSE.DOCS and TRANSVERSE.SECURITY. P (secrets and configuration): TRANSVERSE.CONFIG. S (what agents may execute): spread over ASSURANCE.SECURITY.6 and CHANGE_FLOW.DATA_CHANGE.6, awaiting the scope answer.

### Where the evidence does not fit the proposal

- Overlap inside the proposal: documentation in sync and security appear under both ASSURANCE and TRANSVERSE, and candidate K under both ASSURANCE and OPERATION. Resolved by splitting decision (ASSURANCE: which mechanism, at which stage) from practice (TRANSVERSE, OPERATION), with `Realizes` links. The maintainer may prefer one home.
- Data and schema change: the proposal lists it under CHANGE_FLOW, and "data integrity under change" is a property in ASSURANCE. Split the same way: ASSURANCE.DATA_INTEGRITY holds the guarantee mechanisms, CHANGE_FLOW.DATA_CHANGE the procedures (it carries 51 rows, the largest L2 of CHANGE_FLOW).
- Design and structure practice has no branch: L308 (a new layer must earn its cost), L310 to L312 (built-in against custom, where scheduled work runs, technology by fit), L330 (probable use against YAGNI), L329 (derive before coding), L324 (decision records state accepted costs). Placed in OWNERSHIP.STANCE, SELECTION.6, TRANSVERSE.DOCS.3 and a provisional TRANSVERSE.DESIGN.
- Two extension nodes were needed: OWNERSHIP.LICENCE and ASSURANCE.ARTIFACT (reasons above).
- Rows with an arguable owner: boundary rows between selection and lifecycle (L009, L010, L012, L013), between dependency scanning and security (L063, L067), and between availability and external services (L031 to L033). Each is attached once; the judging step may move them.

### Tensions the judges will meet (pointers, no verdict; from the coverage check, section 5)

- Manual production gate and manual lane (L290) against one automated process for every environment (L159, L328 against L165): CHANGE_FLOW.DATA_CHANGE.6, RELEASE.4, DEPLOY.1, DEPLOY.2.
- Probable-use design (L330) against no speculative building (L038): OWNERSHIP.STANCE.3.
- Coordinated breaking changes (L295) against independent deployment and contract tests (L171, L102): ASSURANCE.CONTRACTS.1 and .2.
- Registry content by script (L294) against database change in the same pipeline (L168): CHANGE_FLOW.DATA_CHANGE.6 and .7.
- Tests on shared real data behind rollback (L265) against isolated tests (L111, L119): ASSURANCE.BEHAVIOUR.9, RULES.2, AVAILABILITY.4.
- Written undo and no automatic down step (L288) against automated rollback (L162): CHANGE_FLOW.ROLLBACK.1 and .2.
- Mandatory unit header with dated change log (L318) against one canonical record (L218, L133): ASSURANCE.DOCS_SYNC.6.
- Review escalated to named senior approvers (L298) against no per-change approval outside peer review (L143): CHANGE_FLOW.REVIEW.1.
- Open gap: no automated regression run found in the doctrine (L331); if confirmed it contradicts L081, L106, L144: ASSURANCE.BEHAVIOUR.7.

## Context variables

Default team context is not set. Each node lists the variables that move its choice; the judging step needs a default or a per-variable rule (open for the maintainer). The three the proposal names (team size, criticality, regulation) and two more from it (shared database, AI coding agents) are in the list; the rest come from the evidence.

| variable | meaning |
|---|---|
| TEAM_SIZE | number of people and teams, co-located or not, trust between them |
| CRITICALITY | cost of failure: data loss, safety, money, reputation |
| REGULATION | regulated or audited context (finance, health, EU rules) |
| EXPOSURE | untrusted input, internet exposure, sensitive or personal data |
| DISTRIBUTION | library for others, hosted service with one live version, binary shipped to customers, open source |
| LIFETIME | expected life of the system and of its parts |
| CONSUMERS | number and visibility of consumers of an interface, in-house or external |
| SHARED_STORE | several writers, backends or tools share one database |
| AI_AGENTS | AI coding agents as contributors or operators |
| SCALE | data volume, traffic and change volume |
| TEST_MATURITY | trustworthiness and speed of the automated tests, monitoring and rollback in place |
| PLATFORM | language, ecosystem, managed platform or own infrastructure |
| SKILLS | team skills and capacity to learn new tools |
| RELEASE_MODEL | one live version, several versions in the field, or explicit versions |
| BUDGET | compute, tooling and attention available |
| DIFFERENTIATION | the capability carries competitive advantage (core) or is commodity |
| SWITCH_LIKELIHOOD | probability that the dependency will have to be replaced |
| CHANGE_COST | cost of changing structure or an interface later |
| SYSTEM_SHAPE | monolith, services, UI application, data pipeline |

## Awaiting scope

Topics outside the six the maintainer named. They get no node; each row below is attached to the node of its subject above and listed here so the scope answer can place it. The round-1 coverage check found no claim on backup and recovery or on technical debt; the rows below are round-2 or maintainer rows that touch them.

- backup and recovery: L124, L359, L388, L389, L390, L416, L440, L451. (restore from version control, independent data copy, restore-as-undo, restore tests, last reversible point, soft-delete then restore, failover capacity, exercised recovery)
- technical debt and decommissioning: L009, L039, L155, L217, L296, L384, L419. (end-of-life plan, incremental replacement, toggle expiry, removing obsolete documents, deprecated items kept, unfinished contract step, dropping a column)
- AI agents as contributors: L172, L326, L327. (small batches with AI-generated code, one sanctioned tool-enforced path, agent writes the script and the human runs it)

## Tree

```text
ROOT  Software Development Philosophy  (-)
    OWNERSHIP  Ownership  (-)
        OWNERSHIP.STANCE  Necessity and Default Stance  (-)
            OWNERSHIP.STANCE.1  Necessity Test  (L001, L037, L308)
            OWNERSHIP.STANCE.2  Write, Adopt or Rent  (L002, L040, L310, L311)
            OWNERSHIP.STANCE.3  Speculative Building  (L038, L330)
            OWNERSHIP.STANCE.4  Source Form of a Small Surface  (L070-L072)
        OWNERSHIP.SELECTION  Selection of a Candidate  (-)
            OWNERSHIP.SELECTION.1  Criteria and Written Record  (L003-L005, L023, L029, L030, L042)
            OWNERSHIP.SELECTION.2  Health Signals of a Candidate  (L006-L009, L011, L022, L041)
            OWNERSHIP.SELECTION.3  Scores and Popularity  (L017-L019)
            OWNERSHIP.SELECTION.4  Vetting Depth and Authenticity  (L010, L012, L013, L027, L077)
            OWNERSHIP.SELECTION.5  Shape of the Candidate  (L014-L016, L020, L021)
            OWNERSHIP.SELECTION.6  Technology Fit and Novelty Budget  (L024-L026, L312)
            OWNERSHIP.SELECTION.7  Who May Introduce a Dependency  (L028)
        OWNERSHIP.LIFECYCLE  Dependency Lifecycle  (-)
            OWNERSHIP.LIFECYCLE.1  Declaration, Lock and Install Contract  (L043-L047)
            OWNERSHIP.LIFECYCLE.2  Pin or Range  (L049-L051)
            OWNERSHIP.LIFECYCLE.3  Update Cadence and Delay  (L052-L057)
            OWNERSHIP.LIFECYCLE.4  Versioning Promises and Trust in Them  (L058, L059, L061)
            OWNERSHIP.LIFECYCLE.5  Trusted Channels, Mirror and Rebuild  (L062, L064, L065, L076)
            OWNERSHIP.LIFECYCLE.6  Inventory, Scanning and Legal Duties  (L063, L066, L067, L079)
        OWNERSHIP.CONTAINMENT  Containment and Exit  (-)
            OWNERSHIP.CONTAINMENT.1  Adapter or Direct Use  (L035, L068)
            OWNERSHIP.CONTAINMENT.2  Boundary with an External System  (L340-L345)
            OWNERSHIP.CONTAINMENT.3  Runtime Isolation of Risky Dependencies  (L069)
            OWNERSHIP.CONTAINMENT.4  Lock-in Pricing  (L073-L075)
            OWNERSHIP.CONTAINMENT.5  Exit Path and Replacement  (L039, L078)
        OWNERSHIP.SERVICES  External Services  (-)
            OWNERSHIP.SERVICES.1  Availability Fit  (L031, L033, L346-L350)
            OWNERSHIP.SERVICES.2  API Stability and Deprecation  (L034, L351, L353-L355)
            OWNERSHIP.SERVICES.3  Exit and Switching Terms  (L356, L357, L359)
            OWNERSHIP.SERVICES.4  Commercial and Legal Terms  (L358, L360, L361)
            OWNERSHIP.SERVICES.5  Vendor Assessment  (L363-L365)
            OWNERSHIP.SERVICES.6  Tools, CI and Hosting as Rented Services  (L366-L369, L378)
        OWNERSHIP.LICENCE  Licence Obligations  (-)
            OWNERSHIP.LICENCE.1  Presence and Classification  (L036, L362, L370-L372)
            OWNERSHIP.LICENCE.2  Policy and Process  (L373, L377)
            OWNERSHIP.LICENCE.3  Network Copyleft and Separate Components  (L374, L375)
            OWNERSHIP.LICENCE.4  Declaring the Team's Own Licence  (L376)
    ASSURANCE  Assurance  (-)
        ASSURANCE.RULES  Rules Common to Every Property  (-)
            ASSURANCE.RULES.1  Placement by Stage and Risk  (L091, L121)
            ASSURANCE.RULES.2  Trustworthy Signal  (L086, L109-L111, L147)
            ASSURANCE.RULES.3  Feedback Speed and Gate Membership  (L112, L145)
        ASSURANCE.BEHAVIOUR  Behaviour  (L081-L083)
            ASSURANCE.BEHAVIOUR.1  Test-Level Mix and Unit Definition  (L089, L090, L092-L094)
            ASSURANCE.BEHAVIOUR.2  Test Doubles and What a Test Observes  (L095-L098)
            ASSURANCE.BEHAVIOUR.3  Test Quality  (L099, L100)
            ASSURANCE.BEHAVIOUR.4  Test-First  (L080, L101)
            ASSURANCE.BEHAVIOUR.5  Types and Static Analysis  (L084, L085, L087, L088)
            ASSURANCE.BEHAVIOUR.6  Test Strength Beyond Examples  (L113-L117)
            ASSURANCE.BEHAVIOUR.7  Regression and Legacy Code  (L106, L107, L331)
            ASSURANCE.BEHAVIOUR.8  Ownership of Acceptance Testing  (L122, L123)
            ASSURANCE.BEHAVIOUR.9  Tests on Real or Shared Data  (L265-L273, L316)
            ASSURANCE.BEHAVIOUR.10  Platform Pitfalls and Live Verification  (L274-L278)
        ASSURANCE.CONTRACTS  Interfaces and Contracts  (-)
            ASSURANCE.CONTRACTS.1  Verification of Service Boundaries  (L102-L104)
            ASSURANCE.CONTRACTS.2  Evolution of a Shared Interface  (L060, L105, L171, L295, L296, L309, L352)
            ASSURANCE.CONTRACTS.3  Interface Description as Source  (L220-L222)
            ASSURANCE.CONTRACTS.4  Failure Semantics of an Interface  (L315)
        ASSURANCE.DATA_INTEGRITY  Data Integrity Under Change  (-)
            ASSURANCE.DATA_INTEGRITY.1  Where Integrity Is Enforced  (L279, L417)
            ASSURANCE.DATA_INTEGRITY.2  Derived Data Stays in Sync  (L281, L282, L313, L314)
            ASSURANCE.DATA_INTEGRITY.3  Self-Auditing Rules  (L283-L285)
            ASSURANCE.DATA_INTEGRITY.4  Checks During a Data Change  (L280, L391, L396, L414, L415)
            ASSURANCE.DATA_INTEGRITY.5  Reversibility and Restore  (L388, L389, L416)
        ASSURANCE.DOCS_SYNC  Documentation in Sync  (-)
            ASSURANCE.DOCS_SYNC.1  Same Change, Docs as Code  (L210, L211, L230, L238)
            ASSURANCE.DOCS_SYNC.2  Trigger and Gate Strength  (L212-L214, L226, L237, L239)
            ASSURANCE.DOCS_SYNC.3  Mechanical Checks of Content  (L219, L223, L224)
            ASSURANCE.DOCS_SYNC.4  Who Verifies Accuracy  (L215, L227-L229)
            ASSURANCE.DOCS_SYNC.5  Freshness Over Time  (L216, L217, L319)
            ASSURANCE.DOCS_SYNC.6  Single Source per Fact  (L218, L318, L320)
        ASSURANCE.SECURITY  Security  (-)
            ASSURANCE.SECURITY.1  Design-Time Security Review  (L243)
            ASSURANCE.SECURITY.2  Review, Analysis and Test by Stage  (L244, L245, L247)
            ASSURANCE.SECURITY.3  Block or Advise  (L246)
            ASSURANCE.SECURITY.4  Secure Defaults  (L248)
            ASSURANCE.SECURITY.5  Secret Scanning and Compromise Response  (L251, L252)
            ASSURANCE.SECURITY.6  Access Enforcement and Automation Limits  (L325, L326)
        ASSURANCE.PERFORMANCE  Performance  (-)
            ASSURANCE.PERFORMANCE.1  Targets, Budgets and Optimisation Stance  (L420, L421, L434, L435)
            ASSURANCE.PERFORMANCE.2  Test Environment and Realism  (L422-L425)
            ASSURANCE.PERFORMANCE.3  Test Types and When They Run  (L108, L426-L429)
            ASSURANCE.PERFORMANCE.4  Measurement Validity  (L430, L431)
            ASSURANCE.PERFORMANCE.5  Production Tests for Performance  (L432, L433)
        ASSURANCE.AVAILABILITY  Availability  (-)
            ASSURANCE.AVAILABILITY.1  Remote-Call Discipline  (L332-L339)
            ASSURANCE.AVAILABILITY.2  Degraded Modes and Overload  (L032, L442)
            ASSURANCE.AVAILABILITY.3  Resilience Experiments  (L120)
            ASSURANCE.AVAILABILITY.4  Verification in Production  (L118, L119)
        ASSURANCE.ARTIFACT  Artifact Integrity  (L048, L151, L152)
    CHANGE_FLOW  Change Flow  (-)
        CHANGE_FLOW.INTEGRATION  Version Control and Integration  (-)
            CHANGE_FLOW.INTEGRATION.1  Branch Lifetime and Release Branches  (L125-L129)
            CHANGE_FLOW.INTEGRATION.2  Protecting the Mainline  (L131, L146)
            CHANGE_FLOW.INTEGRATION.3  Repository Layout  (L124, L132)
            CHANGE_FLOW.INTEGRATION.4  History, Merge Method and Commits  (L130, L133, L134)
        CHANGE_FLOW.REVIEW  Review  (-)
            CHANGE_FLOW.REVIEW.1  Review Mechanism and Who Approves  (L136, L137, L143, L298)
            CHANGE_FLOW.REVIEW.2  Review Standard and Latency  (L138, L139, L142)
            CHANGE_FLOW.REVIEW.3  Change Size and Prior Automation  (L140, L141, L172, L297)
        CHANGE_FLOW.BUILD  Build and Pipeline  (L144, L148-L150)
        CHANGE_FLOW.RELEASE  Release  (-)
            CHANGE_FLOW.RELEASE.1  Versioning and Identification  (L135)
            CHANGE_FLOW.RELEASE.2  Cadence and Batch Size  (L153)
            CHANGE_FLOW.RELEASE.3  Release Decoupled from Deployment  (L154, L155)
            CHANGE_FLOW.RELEASE.4  Approval Gates and Who May Release  (L156, L157, L164)
        CHANGE_FLOW.DEPLOY  Deployment  (-)
            CHANGE_FLOW.DEPLOY.1  Deploy Mechanism  (L159, L166, L167)
            CHANGE_FLOW.DEPLOY.2  Environment Set and Parity  (L165)
            CHANGE_FLOW.DEPLOY.3  Rollout Strategy  (L160, L161, L173)
        CHANGE_FLOW.ROLLBACK  Rollback and Recovery of a Change  (-)
            CHANGE_FLOW.ROLLBACK.1  Detection and Rollback or Fix Forward  (L162, L163)
            CHANGE_FLOW.ROLLBACK.2  Undoing a Data Change  (L288, L387, L390)
        CHANGE_FLOW.MEASURE  Measuring Delivery  (L169, L170)
        CHANGE_FLOW.DATA_CHANGE  Data and Schema Change  (-)
            CHANGE_FLOW.DATA_CHANGE.1  Migrations as Versioned Scripts  (L286, L287, L289, L379-L381, L418)
            CHANGE_FLOW.DATA_CHANGE.2  Compatible Change Sequence  (L292, L382-L386, L409, L419)
            CHANGE_FLOW.DATA_CHANGE.3  Locks and Online Change  (L304, L392-L395, L397, L402)
            CHANGE_FLOW.DATA_CHANGE.4  Backfills and Bulk Jobs  (L299-L303, L305-L307, L398-L401, L412, L413)
            CHANGE_FLOW.DATA_CHANGE.5  Rehearsal Data  (L293, L403-L405)
            CHANGE_FLOW.DATA_CHANGE.6  Who Applies a Change, by Risk  (L168, L290, L291, L327, L328, L408, L410)
            CHANGE_FLOW.DATA_CHANGE.7  Separate Tracks for Urgent, Data and Registry Changes  (L294, L406, L407, L411)
    OPERATION  Operation  (-)
        OPERATION.RELIABILITY  Reliability Targets  (-)
            OPERATION.RELIABILITY.1  Targets and Indicators  (L174-L179)
            OPERATION.RELIABILITY.2  Error Budget and Its Policy  (L180-L183)
        OPERATION.ALERTING  Alerting  (L184-L188)
        OPERATION.TELEMETRY  Telemetry  (-)
            OPERATION.TELEMETRY.1  Signals to Collect  (L189-L193, L195)
            OPERATION.TELEMETRY.2  Storage Model and Sampling  (L194, L200)
            OPERATION.TELEMETRY.3  Instrumentation Standards  (L196-L199, L201)
            OPERATION.TELEMETRY.4  Synthetic and Real-User Monitoring  (L453-L455)
            OPERATION.TELEMETRY.5  Telemetry Cost Budget  (L456-L460)
        OPERATION.INCIDENTS  Incidents  (-)
            OPERATION.INCIDENTS.1  Running an Incident  (L202-L204, L209)
            OPERATION.INCIDENTS.2  Postmortems  (L205, L206)
            OPERATION.INCIDENTS.3  Human Cost of Operation  (L207, L452)
        OPERATION.CAPACITY  Capacity  (-)
            OPERATION.CAPACITY.1  Capacity Planning  (L436-L441)
            OPERATION.CAPACITY.2  Data Store Health  (L317)
        OPERATION.READINESS  Operational Readiness  (L443-L447)
        OPERATION.RUNBOOKS  Runbooks and Recovery Practice  (-)
            OPERATION.RUNBOOKS.1  Runbooks and Playbooks  (L448-L450)
            OPERATION.RUNBOOKS.2  Exercising Recovery  (L451)
        OPERATION.FEEDBACK  Feedback into Development  (L208)
    TRANSVERSE  Transverse Practice  (-)
        TRANSVERSE.DOCS  Documentation Practice  (-)
            TRANSVERSE.DOCS.1  Taxonomy, Size and Structure  (L233, L234, L321, L322)
            TRANSVERSE.DOCS.2  How Much to Document and the Budget  (L231, L236)
            TRANSVERSE.DOCS.3  Decision Records  (L232, L324)
            TRANSVERSE.DOCS.4  Changelog  (L235)
            TRANSVERSE.DOCS.5  Prose Style Rules  (L225)
            TRANSVERSE.DOCS.6  How Guidelines Are Authored  (L323)
        TRANSVERSE.SECURITY  Security Practice  (-)
            TRANSVERSE.SECURITY.1  Responsibility and Training  (L249)
            TRANSVERSE.SECURITY.2  Framework and Requirements Catalogue  (L240, L250)
            TRANSVERSE.SECURITY.3  Threat Modelling Practice  (L241, L242)
            TRANSVERSE.SECURITY.4  Vulnerability Response Loop  (L253)
            TRANSVERSE.SECURITY.5  Hardening the Toolchain  (L264)
        TRANSVERSE.CONFIG  Configuration and Secrets  (-)
            TRANSVERSE.CONFIG.1  Configuration Apart from Code  (L158, L261)
            TRANSVERSE.CONFIG.2  Delivery of Configuration and Secrets  (L254-L256)
            TRANSVERSE.CONFIG.3  Secret Management  (L257-L259)
        TRANSVERSE.ENVIRONMENTS  Development Environments  (-)
            TRANSVERSE.ENVIRONMENTS.1  Development Environment as Code  (L262, L263)
            TRANSVERSE.ENVIRONMENTS.2  Separation of Environments  (L260)
        TRANSVERSE.DESIGN  Design Derivation (provisional)  (L329)
```

## Nodes

#### ROOT Software Development Philosophy

Decides: A team delivers, and keeps delivering, a system that does what is intended, at a cost it can sustain.
Rows: -
Context: see children

### Branch OWNERSHIP

#### OWNERSHIP Ownership

Decides: For each capability, does the team write it, adopt it (a library or tool it runs) or rent it (an external service or API), and how is that choice kept reversible?
Rows: -
Forces in tension: control, time to value, cost of ownership over time, exit risk, security exposure, fit
Context: TEAM_SIZE, CRITICALITY, REGULATION, DIFFERENTIATION, LIFETIME

#### OWNERSHIP.STANCE Necessity and Default Stance

Decides: Is the capability needed at all, and absent a specific reason, is the default to write, adopt or rent?
Rows: -
Context: see children

#### OWNERSHIP.STANCE.1 Necessity Test

Decides: Which test must a new dependency, layer or moving part pass before its quality is even assessed?
Rows: L001, L037, L308 (3)
Positions in the evidence (no verdict):
- P1 Justify every dependency by necessity first: it adds attack surface and ownership cost beyond the effort it saves; it is an ongoing liability, not a one-time saving (L001, L037).
- P2 The same test for any new layer or moving part: create it only when at least one strong reason outweighs write, test, maintain, evolve and onboard costs; the maintainer defaults to not creating the layer and accepts a wide band once justified, against a default of building the layer (database-centric) (L308).
Forces in tension: cost of ownership, attack surface, cognitive load
Context: LIFETIME, TEAM_SIZE, SKILLS, CRITICALITY

#### OWNERSHIP.STANCE.2 Write, Adopt or Rent

Decides: Absent a reason either way, which of the three is the default for a capability, and which exceptions are stated?
Rows: L002, L040, L310, L311 (4)
Positions in the evidence (no verdict):
- P1 Reuse well-secured existing software by default, strongest for cryptography and protocols and for non-core, well-understood, widely used functions (L002 a).
- P2 Minimise dependencies: an internal code problem is cheaper than a dependency problem you do not control; copy or rewrite when only a tiny part is needed (L002 b, c).
- P3 Build or keep control for a core business function that carries competitive advantage (L002, L040).
- P4 Rent (SaaS, hosted API) is an adoption decision with the same cost test plus a control cost: rent non-core and keep core, against renting broadly and accepting lock-in where the pay-off is commensurate (L040).
- P5 A platform built-in over custom code unless it lacks a stated capability, against custom code where granularity or per-entry strategy is needed; the coverage check records this as matching, not contradicting, L002 (L310).
- P6 Scheduled work run inside the data store (atomicity with the data, one system to observe) against a dedicated external orchestrator (retries, dependencies, backfills, cross-system visibility); the maintainer holds the first, public practice the second (L311).
Forces in tension: control, differentiation, cost of ownership, delivery speed, security
Context: DIFFERENTIATION, CRITICALITY, EXPOSURE, LIFETIME, SCALE, PLATFORM
Stack pointers: L311 (PostgreSQL in-database scheduler (stack-tagged p...)

#### OWNERSHIP.STANCE.3 Speculative Building

Decides: Is anything built, or a structure shaped, for use that does not exist yet?
Rows: L038, L330 (2)
Positions in the evidence (no verdict):
- P1 Build nothing speculative: building, delaying other work, carrying complexity and repairing wrong guesses are four distinct costs, also for a substitute written 'in case' (L038).
- P2 Shape the structure for probable future usage, not only today's ticket, while avoiding speculative optimisation; wins where structural change is costly (a very large store) (L330). The coverage check records L330 as contradicting L038.
Forces in tension: delivery speed, reversibility, cost of ownership
Context: CHANGE_COST, SCALE, LIFETIME

#### OWNERSHIP.STANCE.4 Source Form of a Small Surface

Decides: When the used surface is small or the upstream is unsuitable, is the code copied, vendored, forked or depended on?
Rows: L070-L072 (3)
Positions in the evidence (no verdict):
- P1 Copy or reimplement the needed code for a tiny used surface (attack surface, exit risk) against depending on it, notably for cryptography (L070).
- P2 Prefer source-control problems to dependency-management problems: vendor or monorepo, against consuming from a registry with a lock (L071).
- P3 Upstream fixes rather than carry private forks; report vulnerabilities to the maintainer (L072).
Forces in tension: attack surface, exit risk, control, cost of ownership
Context: SCALE, TEAM_SIZE, EXPOSURE, DISTRIBUTION

#### OWNERSHIP.SELECTION Selection of a Candidate

Decides: How is a specific library, tool or service found, judged and approved once the stance says adopt?
Rows: -
Context: see children

#### OWNERSHIP.SELECTION.1 Criteria and Written Record

Decides: Which criteria are applied, in which context of use, and where is the outcome recorded?
Rows: L003-L005, L023, L029, L030, L042 (7)
Positions in the evidence (no verdict):
- P1 Judge against an explicit criteria set (design, docs, code quality, tests, bug handling, maintenance, security exposure, licence, transitive dependencies) and record the result (L003, L042).
- P2 Practitioners mostly select ad hoc and over two dozen factors then decide (one study) (L005).
- P3 Evaluate in the context of the intended use and repeat when the use changes (L004); select for fit to actual requirements, not features or fashion (L023).
- P4 Write the reasons, alternatives and accepted risks where later maintainers find them (L029); use aggregators for discovery only, and expect them to change (L030).
Forces in tension: fit, confidence, cost of the selection process
Context: CRITICALITY, TEAM_SIZE, REGULATION

#### OWNERSHIP.SELECTION.2 Health Signals of a Candidate

Decides: Which signals of maintenance and community count, and what does a weak signal require?
Rows: L006-L009, L011, L022, L041 (7)
Positions in the evidence (no verdict):
- P1 Require maintainer diversity (single point of failure for fixes and account takeover), against tolerating small projects, since narrow finished tools legitimately have one author (L007, L041).
- P2 Recent activity and releases; long inactivity is a risk (L006, L041); check responsiveness and backported security fixes (L008).
- P3 Confirm the component is maintained and not at end of life; keep a plan for components that stop being maintained (L009).
- P4 Prefer a published vulnerability-disclosure policy (L011); count the reachable trust surface of the registry, not only the repository (L022, npm evidence).
Forces in tension: exit risk, continuity, fit, minimal footprint
Context: CRITICALITY, LIFETIME, EXPOSURE
Stack pointers: L022 (npm evidence (registry-wide principle inferred))

#### OWNERSHIP.SELECTION.3 Scores and Popularity

Decides: What weight do aggregate scores and adoption carry in the decision?
Rows: L017-L019 (3)
Positions in the evidence (no verdict):
- P1 Aggregate scores as an input to judgment only (Scorecard's own documentation), against a gate at a threshold via automation, which no source read argues and which is inferred as large-scale practice (L017).
- P2 Process scores predict vulnerability outcomes poorly: low explanatory power in one study (L018).
- P3 Popularity as a weak proxy for scrutiny and help, against popularity as hype that says nothing about fit (L019).
Forces in tension: correctness of the decision, consistency, speed of review
Context: SCALE, TEAM_SIZE

#### OWNERSHIP.SELECTION.4 Vetting Depth and Authenticity

Decides: How deep is a candidate examined, and how is its origin verified, before adoption?
Rows: L010, L012, L013, L027, L077 (5)
Positions in the evidence (no verdict):
- P1 Metadata and scores only (fast, cheap), against hands-on tests and code review for components that handle untrusted input, credentials or cryptography; the scaling rule is inferred (L027).
- P2 Require provenance for every dependency (audit or enforce tiers), against provenance as a preferred signal only (L013).
- P3 Delegate audit effort: reuse trusted organisations' audits and review only version differences (L077; one tool source).
- P4 Reject or defer candidates with known unfixed vulnerabilities, and re-check over life (L010); official sources, signed packages, look-alike names (L012).
Forces in tension: security, confidence, delivery speed, cost
Context: CRITICALITY, EXPOSURE, REGULATION, TEAM_SIZE
Stack pointers: L077 (Rust cargo-vet realisation; concept neutral)

#### OWNERSHIP.SELECTION.5 Shape of the Candidate

Decides: Which structural properties of a candidate (version maturity, interface stability, size of its dependency tree) disqualify or weigh against it?
Rows: L014-L016, L020, L021 (5)
Positions in the evidence (no verdict):
- P1 Treat 0.x, alpha or beta as incomplete software accepted only knowingly, against the view that labels are not uniform and many mature tools stay 0.x (L016).
- P2 Avoid or inline trivial packages (long chains, supply-chain exposure), against small shared packages giving reuse; the second is not read in a source (L021, npm evidence).
- P3 Count transitive dependencies as cost (L020); read the compatibility promise (L014); prefer stable, secure-by-default interfaces (L015).
Forces in tension: exit risk, cost of ownership, correctness, reversibility
Context: LIFETIME, EXPOSURE, PLATFORM
Stack pointers: L021 (JavaScript/npm evidence (generalisable))

#### OWNERSHIP.SELECTION.6 Technology Fit and Novelty Budget

Decides: How much new technology is taken on, in which steps, and with how many tools per problem?
Rows: L024-L026, L312 (4)
Positions in the evidence (no verdict):
- P1 Boring first: proven technology, innovation tokens spent only where the business needs it and the existing tool demonstrably cannot solve the problem (L024 a).
- P2 Staged novelty: assess, trial, adopt rings, with hold for tools that burned you (L024 b, L025).
- P3 Hold the number of tools solving the same problem down and plan migration of the replaced one (L026).
- P4 Choose the core technology by problem fit, not dogma, and the paradigm per part by intent (maintainer) (L312).
Forces in tension: team cognitive load, reversibility, delivery speed, learning
Context: TEAM_SIZE, SKILLS, LIFETIME, BUDGET

#### OWNERSHIP.SELECTION.7 Who May Introduce a Dependency

Decides: Who may add a dependency: any developer, a reviewed proposal, or only from a sanctioned list?
Rows: L028 (1)
Positions in the evidence (no verdict):
- P1 Central sanctioned repository and approved-component list with provenance data (NIST SSDF), against team-level choice with light visibility; the contrast is inferred (L028).
Forces in tension: security, control, consistency, delivery speed
Context: TEAM_SIZE, REGULATION, CRITICALITY

#### OWNERSHIP.LIFECYCLE Dependency Lifecycle

Decides: How is an adopted dependency declared, pinned, updated, trusted and watched while the system is in service?
Rows: -
Context: see children

#### OWNERSHIP.LIFECYCLE.1 Declaration, Lock and Install Contract

Decides: What is declared, what records the resolved tree, and what is installed in CI and production?
Rows: L043-L047 (5)
Positions in the evidence (no verdict):
- P1 Declare all dependencies completely and exactly, run them isolated, new developer needs only runtime, manager and one command (L043); commit a lockfile with the exact resolved tree (L044); install from the lock only (L045); verify artifacts by hash (L046).
- P2 Resolution rule: minimal version selection (upgrades explicit), against newest-compatible resolution plus a lock (L047, Go evidence).
Forces in tension: correctness, confidence, delivery speed
Context: PLATFORM, TEAM_SIZE, DISTRIBUTION
Stack pointers: L045 (npm `npm ci`, generalises); L046 (pip `--require-hashes`, npm integrity, Go checks...); L047 (Go (MVS), contrasts with newest-compatible resol...)

#### OWNERSHIP.LIFECYCLE.2 Pin or Range

Decides: Are versions pinned exactly or declared as ranges?
Rows: L049-L051 (3)
Positions in the evidence (no verdict):
- P1 Exact pins plus an update bot for applications nobody else installs, against ranges plus lockfile only when review capacity is scarce (L049).
- P2 Libraries declare ranges; exact pins in libraries have no source defending them (open) (L050).
- P3 A lockfile does not replace constraints: the manifest must still exclude known-broken versions (L051).
Forces in tension: confidence, low noise, consumer cognitive load
Context: DISTRIBUTION, TEAM_SIZE, TEST_MATURITY

#### OWNERSHIP.LIFECYCLE.3 Update Cadence and Delay

Decides: How often, how fast and how delayed are dependency updates applied?
Rows: L052-L057 (6)
Positions in the evidence (no verdict):
- P1 Update continuously in small automated steps, against upgrading only when there is need, when verification is weak or deployments costly (L052).
- P2 Release-age cooldown of days to two weeks for routine updates (most observed attacks were detected within a week; one author's analysis of 10 attacks), against updating immediately (L054).
- P3 Known-vulnerability fixes bypass any delay (L053); group automated update proposals (L055); read notes and rerun tests including usage-specific integration tests (L056); roll updates out in stages (L057).
Forces in tension: security (known-vulnerability exposure against malicious-release exposure), control, stability
Context: TEST_MATURITY, CRITICALITY, EXPOSURE, TEAM_SIZE

#### OWNERSHIP.LIFECYCLE.4 Versioning Promises and Trust in Them

Decides: How far is a version number trusted, and how are incompatible shared dependencies resolved?
Rows: L058, L059, L061 (3)
Positions in the evidence (no verdict):
- P1 Live at head with provider-run downstream tests (monorepo scale), against version-pinned SemVer consumption for external consumers (L058).
- P2 SemVer ranges are a usable contract, against SemVer as an estimate with tests as the evidence (L059).
- P3 Diamond dependency options: move versions forward or backward, or patch locally (L061).
Forces in tension: feedback speed, shared upgrade cost, control, correctness
Context: CONSUMERS, SCALE, TEST_MATURITY, DISTRIBUTION

#### OWNERSHIP.LIFECYCLE.5 Trusted Channels, Mirror and Rebuild

Decides: Where do artifacts come from, and how much of the supply chain does the team hold itself?
Rows: L062, L064, L065, L076 (4)
Positions in the evidence (no verdict):
- P1 Managed repository or mirror of sanctioned components, against direct pull from the public registry with lock and hashes (L062).
- P2 Rebuild every deployed open-source artifact from source in own infrastructure, against consuming prebuilt verified artifacts (L065).
- P3 Mirror or vendor for production-critical builds, against relying on an immutable public proxy (L076).
- P4 Provenance protects what a producer built, not its dependencies or their removal: verify recursively, address unavailability separately (L064).
Forces in tension: control, availability, cost of ownership, update lag
Context: CRITICALITY, REGULATION, TEAM_SIZE, EXPOSURE

#### OWNERSHIP.LIFECYCLE.6 Inventory, Scanning and Legal Duties

Decides: What is known about every dependency in service, and what is watched?
Rows: L063, L066, L067, L079 (4)
Positions in the evidence (no verdict):
- P1 No competing position recorded (agreement: consensus): inventory of every dependency, transitive included, with where it is deployed (L066); scan for vulnerabilities, licence, end of life and, at higher maturity, malware (L063); monitor vulnerability databases for the life of the software (L067).
- P2 Where law applies (for example the EU Cyber Resilience Act), due diligence, SBOM and vulnerability reporting are duties; primary text unread (L079).
Forces in tension: security, compliance, cost of ownership
Context: REGULATION, DISTRIBUTION, CRITICALITY

#### OWNERSHIP.CONTAINMENT Containment and Exit

Decides: How far does a dependency reach into the code, and how would it be replaced?
Rows: -
Context: see children

#### OWNERSHIP.CONTAINMENT.1 Adapter or Direct Use

Decides: Is a thin adapter placed between the code and a dependency?
Rows: L035, L068 (2)
Positions in the evidence (no verdict):
- P1 Wrap with an adapter containing only what the project needs and keep external types inside out: for volatile, security-sensitive or single-vendor dependencies and rented services (L068 a, L035 a).
- P2 Use the dependency directly: investment in reducing lock-in can raise total cost and a speculative abstraction carries cost; wins when switching probability is low and the interface is a stable standard (L068 b, L035 b).
Forces in tension: reversibility, exit risk, testability, cost of ownership, cognitive load
Context: SWITCH_LIKELIHOOD, CRITICALITY, DISTRIBUTION, REGULATION

#### OWNERSHIP.CONTAINMENT.2 Boundary with an External System

Decides: How is data from, and the model of, an external system kept from shaping the inside?
Rows: L340-L345 (6)
Positions in the evidence (no verdict):
- P1 Tolerant reader (parse only needed fields, ignore unknown ones), against strict schema validation of everything received; a synthesis is inferred (L341, L342).
- P2 Mandatory anti-corruption layer for a model you do not control, against calling the service directly when it is core, stable and switching unlikely (L344).
- P3 Treat a third-party service as an attached resource with no local/third-party distinction, against the view that the distinction is real when vendor semantics differ (L343).
- P4 Treat every third-party response as untrusted input; never expose vendor types in own data or interfaces without an owned mapping (L340, L345).
Forces in tension: evolution without breakage, security, reversibility, cost of ownership
Context: EXPOSURE, SWITCH_LIKELIHOOD, CRITICALITY

#### OWNERSHIP.CONTAINMENT.3 Runtime Isolation of Risky Dependencies

Decides: Is a risky dependency isolated at run time to bound the damage?
Rows: L069 (1)
Positions in the evidence (no verdict):
- P1 Sandbox and least privilege (majority); practicality open (L069).
Forces in tension: security, cost of ownership
Context: EXPOSURE, CRITICALITY, PLATFORM

#### OWNERSHIP.CONTAINMENT.4 Lock-in Pricing

Decides: How much lock-in is accepted, and how much insurance is bought against it?
Rows: L073-L075 (3)
Positions in the evidence (no verdict):
- P1 Accept lock-in that buys a commensurate pay-off; portability beyond the optimum raises total cost (L075 a).
- P2 Minimise by wrapping and open standards for long-lived, regulated or critical rented services (L075 b).
- P3 Regulated or critical functions need a tested exit and an alternative (DORA exit strategy, EU switching right; DORA known from summaries) (L075 c).
- P4 Judge by two quantities, cost to switch and likelihood of switching, across eight lock-in dimensions (L073, L074).
Forces in tension: delivery speed, cost of ownership, exit risk, regulatory duty
Context: REGULATION, CRITICALITY, SWITCH_LIKELIHOOD, LIFETIME

#### OWNERSHIP.CONTAINMENT.5 Exit Path and Replacement

Decides: Is an exit path defined before adoption, and how is a component replaced?
Rows: L039, L078 (2)
Positions in the evidence (no verdict):
- P1 Replace incrementally behind the existing interface, against a big-bang rewrite, for which no source argued (open) (L039).
- P2 Define the exit path (data export, replacement candidate, contract notice) before adopting a rented service, in proportion to criticality (not assessable) (L078).
Forces in tension: reversibility, delivery speed
Context: CRITICALITY, LIFETIME, CONSUMERS

#### OWNERSHIP.SERVICES External Services

Decides: What must hold about a provider and its contract before the team makes a hard dependency of it?
Rows: -
Context: see children

#### OWNERSHIP.SERVICES.1 Availability Fit

Decides: Does the provider's availability and remedy fit the availability the team promises?
Rows: L031, L033, L346-L350 (7)
Positions in the evidence (no verdict):
- P1 No competing position recorded (agreement: consensus, mostly one source each): pick a target at least equal to your own, since hard dependencies multiply availabilities (L031); read the SLA as a commercial instrument (L346); compare remedy to loss and mitigate by design where credit cannot cover it (L347); own your target (L348); keep an internal SLO tighter than the signed one (L349); plan from observed, not stated, behaviour (L350); monitor reachability, latency and errors (L033, inferred).
Forces in tension: availability, cost, control
Context: CRITICALITY, REGULATION, SCALE

#### OWNERSHIP.SERVICES.2 API Stability and Deprecation

Decides: What does the provider promise about change, and what is pinned and watched?
Rows: L034, L351, L353-L355 (5)
Positions in the evidence (no verdict):
- P1 Explicit major versions with a bounded deprecation window, against an indefinitely compatible date-pinned surface (L353).
- P2 Read stability tiers and deprecation policy; prefer providers with minimum notice and two versions side by side (L034); consume Deprecation and Sunset signals (L351); pin the API version and upgrade deliberately (L354).
- P3 Real-world notice is shorter and less reliable than the policy suggests; a published window is not a guarantee (L355).
Forces in tension: consumer stability, provider speed, trust
Context: CONSUMERS, LIFETIME, CRITICALITY
Stack pointers: L351 (HTTP)

#### OWNERSHIP.SERVICES.3 Exit and Switching Terms

Decides: Can the data and the integration leave with the team, and on what terms?
Rows: L356, L357, L359 (3)
Positions in the evidence (no verdict):
- P1 Verify at selection that all data can be exported in a machine-readable format, and test the export once (L356).
- P2 Contract covers switching: notice, data return, no punitive egress charges (EU rules) (L357).
- P3 Mirror or retain an independent copy of critical data, with credentials and integration logic exportable (majority) (L359).
Forces in tension: exit risk, control, regulatory duty
Context: REGULATION, CRITICALITY, LIFETIME

#### OWNERSHIP.SERVICES.4 Commercial and Legal Terms

Decides: Which price, licence and data-processing terms are accepted?
Rows: L358, L360, L361 (3)
Positions in the evidence (no verdict):
- P1 Single-vendor-controlled projects acceptable for non-competitive use, against preferring foundation-governed or multi-vendor projects because relicensing creates stranded code (L361).
- P2 Where personal data is processed, a written processor contract is mandatory (L358).
- P3 Price risk belongs in selection: understand pricing, unit economics, egress; give cost an owner (L360).
Forces in tension: delivery speed, exit risk, control, cost
Context: REGULATION, DISTRIBUTION, BUDGET, LIFETIME

#### OWNERSHIP.SERVICES.5 Vendor Assessment

Decides: How is a vendor's security and supply-chain posture assessed, and how deeply?
Rows: L363-L365 (3)
Positions in the evidence (no verdict):
- P1 Depth by criticality and data sensitivity, repeated over the contract life, against a uniform baseline checklist for every vendor (L364).
- P2 Assess authentication options, intrusion evidence, SBOM and open-source governance (L363); certificates (SOC 2, ISO/IEC 27001) are evidence of controls, not proof of fit (L365).
Forces in tension: speed, cost of review, simplicity and fairness of process, security
Context: CRITICALITY, EXPOSURE, REGULATION, TEAM_SIZE

#### OWNERSHIP.SERVICES.6 Tools, CI and Hosting as Rented Services

Decides: How are build, CI and hosting services chosen and constrained, given they execute with the team's secrets?
Rows: L366-L369, L378 (5)
Positions in the evidence (no verdict):
- P1 Prefer a build service on dedicated hosted infrastructure with signed provenance, run isolation and signing material away from user steps (L369).
- P2 Pin third-party CI components to immutable identifiers, restrict default token permissions (L367); no self-hosted runners on untrusted code (L368).
- P3 Evaluate non-library tools and platforms with the same criteria as services (L378); a CI or hosting service is part of the supply chain (L366).
Forces in tension: security, control, cost of ownership
Context: EXPOSURE, CRITICALITY, PLATFORM
Stack pointers: L367 (GitHub Actions (pointer for equivalents on other...); L368 (GitHub Actions)

#### OWNERSHIP.LICENCE Licence Obligations

Decides: Which licence terms are accepted for what is adopted, and how are the team's own terms stated? (extension: eleven rows form their own decision)
Rows: -
Context: see children

#### OWNERSHIP.LICENCE.1 Presence and Classification

Decides: How are licences read and classified against what the team does with the code?
Rows: L036, L362, L370-L372 (5)
Positions in the evidence (no verdict):
- P1 No competing position recorded: licence present and clear (L036); obligations triggered by use, so classify by family and distribution model (L370); compatibility is directional and pair-specific (L371); use SPDX expressions (L372); source-available licences with field-of-use limits are not open source (L362).
Forces in tension: compliance, exit risk
Context: DISTRIBUTION, REGULATION

#### OWNERSHIP.LICENCE.2 Policy and Process

Decides: Which licence classes are allowed, and who decides?
Rows: L373, L377 (2)
Positions in the evidence (no verdict):
- P1 Conservative class policy (notice licences allowed, copyleft reviewed or prohibited by distribution model), against allowing copyleft where obligations are understood and met (L373).
- P2 A defined open-source compliance process with roles; ISO/IEC 5230 can be self-certified (L377).
Forces in tension: control of own source, cost of audit, delivery speed, reuse
Context: DISTRIBUTION, TEAM_SIZE, REGULATION

#### OWNERSHIP.LICENCE.3 Network Copyleft and Separate Components

Decides: How are network-copyleft and separately run copyleft services treated?
Rows: L374, L375 (2)
Positions in the evidence (no verdict):
- P1 No competing position recorded: decide AGPL separately from GPL (L374); an unmodified copyleft service as a separate network component is not linking, the question is the interface (L375).
Forces in tension: compliance, reuse
Context: DISTRIBUTION

#### OWNERSHIP.LICENCE.4 Declaring the Team's Own Licence

Decides: How are licence and copyright of the team's own files declared?
Rows: L376 (1)
Positions in the evidence (no verdict):
- P1 SPDX identifiers in headers and licence texts in a licences directory, so tools can check compliance (L376).
Forces in tension: compliance, automation
Context: DISTRIBUTION

### Branch ASSURANCE

#### ASSURANCE Assurance

Decides: For each property that must hold, which mechanism, at which stage, guarantees it and runs on every change so that it stays true?
Rows: -
Forces in tension: speed of feedback, realism of the confidence, cost to build and maintain, flakiness, cognitive load
Context: CRITICALITY, TEST_MATURITY, TEAM_SIZE, REGULATION, SYSTEM_SHAPE

#### ASSURANCE.RULES Rules Common to Every Property

Decides: Which rules govern where a guarantee is placed and whether its signal can be trusted?
Rows: -
Context: see children

#### ASSURANCE.RULES.1 Placement by Stage and Risk

Decides: At which stage does each check run, and who records the policy?
Rows: L091, L121 (2)
Positions in the evidence (no verdict):
- P1 Push each check as low and early as it can go; when a higher-level test finds a bug no lower one caught, add the lower test (L091).
- P2 Decide per stage and per risk which analyses and tests run, and record the policy (L121; near L244 for security).
Forces in tension: speed of feedback, cost, realism
Context: CRITICALITY, TEST_MATURITY

#### ASSURANCE.RULES.2 Trustworthy Signal

Decides: How are flaky and noisy checks handled so that a failure keeps meaning something?
Rows: L086, L109-L111, L147 (5)
Positions in the evidence (no verdict):
- P1 Quarantine non-deterministic tests outside the deployment gate with a numeric cap and time limit, then fix or delete (L110; Google reruns only tests marked flaky), against removing them immediately (strict school).
- P2 Classify flaky tests as pipeline defects; retry or disable temporarily during investigation (L147).
- P3 A failure must mean a real defect; about 1% flakiness destroys value (L109); remove causes: isolation, polling, wrapped clocks, doubled remote services (L111; opposed by L265).
- P4 Static checks keep a false-positive rate under 10% (Google about 5%); a noisy check is removed or fixed (L086).
Forces in tension: trust, speed of feedback, cost, flakiness
Context: TEST_MATURITY, TEAM_SIZE, SCALE

#### ASSURANCE.RULES.3 Feedback Speed and Gate Membership

Decides: How fast must feedback be, and which checks gate a merge?
Rows: L112, L145 (2)
Positions in the evidence (no verdict):
- P1 Gate on everything fast and reliable; run slower tests after merge and roll back on failure (about 95% of changes pass presubmit at Google) (L145).
- P2 Staged pipeline with slower, more thorough, parallelised later stages (L145).
- P3 Developer feedback in under ten minutes; build on every commit; broken build first (L112).
Forces in tension: speed of feedback, confidence
Context: SCALE, TEST_MATURITY, TEAM_SIZE

#### ASSURANCE.BEHAVIOUR Behaviour

Decides: Which mechanisms at which stages guarantee that the system does what is intended?
Rows: L081-L083 (3)
Positions in the evidence (no verdict):
- Mechanisms in competition, by stage: type and static checks at edit and build (.5); tests by level at commit and merge (.1 to .3, .6); test-first mechanics (.4); regression and characterization tests (.7); tests on real data (.9); review (CHANGE_FLOW.REVIEW); production verification (ASSURANCE.AVAILABILITY.4).
- P1 Self-testing code as the precondition of integration (L081); everything the team does not want to break gets a test, strict form (Beyonce rule), against Fowler's weaker form, enough tests to change confidently (L082); passing tests do not prove reliability, failing tests prove its absence (L083).
Forces in tension: speed of feedback, realism of confidence, cost, cognitive load
Context: TEST_MATURITY, SYSTEM_SHAPE, CRITICALITY, TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.1 Test-Level Mix and Unit Definition

Decides: How are tests distributed across levels, and what is a unit?
Rows: L089, L090, L092-L094 (5)
Positions in the evidence (no verdict):
- P1 Pyramid, unit-heavy (Google, Fowler); P2 honeycomb, integration-heavy (Spotify); P3 trophy, static plus integration widest (Dodds) (L090); all agree on many small fast tests over few slow broad ones (L089).
- P4 Keep end-to-end tests to a minimum, against Fowler's note that fast, reliable, cheap high-level tests make lower ones unnecessary (L092).
- P5 Solitary against sociable units, team-defined (L094); describe tests by size and scope axes (L093).
Forces in tension: speed of feedback, confidence, diagnosability, refactor safety
Context: SYSTEM_SHAPE, TEST_MATURITY, TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.2 Test Doubles and What a Test Observes

Decides: What does a test verify and how are collaborators replaced?
Rows: L095-L098 (4)
Positions in the evidence (no verdict):
- P1 Classical (real objects unless awkward) against mockist (mock every collaborator with behaviour) (L098).
- P2 State verification over interaction verification, except for unobservable state-changing calls; mockists hold interaction verification drives design (L096).
- P3 Real implementation if fast and deterministic, else a fake owned by the team that owns the real thing; mocks last (L097); test behaviour through public interfaces (L095).
Forces in tension: refactor safety, isolation, failure location, maintenance cost
Context: SYSTEM_SHAPE, CHANGE_COST, TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.3 Test Quality

Decides: By which properties is a test judged and written?
Rows: L099, L100 (2)
Positions in the evidence (no verdict):
- P1 No competing position recorded: DAMP over DRY, no loops or conditionals, one condition per test (L099); trade-offs among twelve test properties, with conflicts such as predictive against fast (L100).
Forces in tension: cognitive load, maintenance cost
Context: TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.4 Test-First

Decides: Is test-first a rule or a team choice?
Rows: L080, L101 (2)
Positions in the evidence (no verdict):
- P1 Context decides (Beck: compilers, API design); overprescriptive, with test-induced design damage in MVC web apps (DHH); valuable in some contexts, over-testing is a tuning problem (Fowler); DORA evidence supports test automation, not test-first ordering (L101).
- P2 Tests written first make change safe and speed iteration; bug-catching is secondary (L080).
Forces in tension: feedback speed, design pressure, cost, cognitive load
Context: SYSTEM_SHAPE, SKILLS, TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.5 Types and Static Analysis

Decides: How strongly are types and analysis enforced as the cheapest layer?
Rows: L084, L085, L087, L088 (4)
Positions in the evidence (no verdict):
- P1 Enforce types (large, long-lived code bases), P2 optional or gradual (existing code, adoption), P3 tests alone suffice, an unrepresented minority, open (L084).
- P4 Adopt typing gradually with an escape hatch rather than rewrite (L085; Python, TypeScript pointers).
- P5 Analysis incremental, new issues first, in review, with automated fixes (L087); warnings as errors in a clean build (L088).
Forces in tension: bug prevention, documentation value, annotation cost, adoption friction
Context: LIFETIME, SCALE, PLATFORM, SKILLS
Stack pointers: L085 (Python (mypy), TypeScript/Flow (gradual))

#### ASSURANCE.BEHAVIOUR.6 Test Strength Beyond Examples

Decides: How is the strength of the suite measured and widened?
Rows: L113-L117 (5)
Positions in the evidence (no verdict):
- P1 Coverage as a diagnostic only, against a floor or threshold for visibility (L113).
- P2 Mutation testing as a routine gate or review signal (diff-based at scale), against skipping or running offline; benefit evidence open (L114).
- P3 Hermetic single-process larger tests (speed, determinism) against multimachine or shared environments (fidelity, flakiness) (L117).
- P4 Property-based tests for describable input ranges (L115); fuzz input-handling code (L116; language pointers).
Forces in tension: signal strength, compute and noise, fidelity, flakiness
Context: CRITICALITY, TEST_MATURITY, BUDGET
Stack pointers: L116 (C/C++, Rust, Go, Python, JVM, JS, Lua (OSS-Fuzz))

#### ASSURANCE.BEHAVIOUR.7 Regression and Legacy Code

Decides: How are past defects and poorly understood code held in place by tests?
Rows: L106, L107, L331 (3)
Positions in the evidence (no verdict):
- P1 Every reported bug becomes a test that fails first (L106); characterization tests before changing poorly understood code (L107).
- P2 Open: the doctrine states how a function test is built and run but not who runs the suite, when or on what trigger; practice appears to be on demand; if confirmed, it contradicts L081, L106 and L144 (L331).
Forces in tension: confidence, cost
Context: LIFETIME, TEST_MATURITY

#### ASSURANCE.BEHAVIOUR.8 Ownership of Acceptance Testing

Decides: Who writes and runs acceptance tests, and where are results kept?
Rows: L122, L123 (2)
Positions in the evidence (no verdict):
- P1 No competing position recorded: developers own automated acceptance tests, testers add exploratory and usability testing (L122); record results and triage in the workflow (L123).
Forces in tension: ownership, feedback
Context: TEAM_SIZE

#### ASSURANCE.BEHAVIOUR.9 Tests on Real or Shared Data

Decides: Do tests that need real data run in isolated environments or against real data inside a boundary that is always undone? (maintainer doctrine, database-centred)
Rows: L265-L273, L316 (10)
Positions in the evidence (no verdict):
- P1 Isolated disposable environment per run (small data or cheap cloning), against running on real data behind a forced rollback because real shapes exist only there and the data is too large to clone (L265; coverage check: contradicts L111).
- P2 Synthetic fixtures (explicit, hermetic) against a curated, catalogued real corpus (L266).
- P3 Vehicle by risk: plain queries when read-only, one atomic unit when mutating, interactive wrapper when a human supervises (L267, L268).
- P4 Tests colocated with the unit against a separate mirrored tree (L270); test configuration disjoint from production context (L271); named fixture variables (L272); conditional, no-op-safe mutations (L273); self-reporting verdict (L269); scheduled job tested directly first (L316).
Forces in tension: confidence in real shapes, isolation, blast radius, speed
Context: SHARED_STORE, SCALE, EXPOSURE, PLATFORM
Stack pointers: L268 (PostgreSQL anonymous blocks (stack-tagged pointe...); L272 (PostgreSQL custom configuration parameters (stac...)

#### ASSURANCE.BEHAVIOUR.10 Platform Pitfalls and Live Verification

Decides: What catches the class of defects that survive review and deployment and fail at run time?
Rows: L274-L278 (5)
Positions in the evidence (no verdict):
- P1 Static analysis and types catch part of the class (speed), against the maintainer's position that tests on production-shaped data are required (L274).
- P2 Verify unclear platform behaviour empirically on a live instance and record scope (L277; agrees with characterization tests); pitfall catalog indexed by symptom (L275); context-anchored edits (L276); hard rule plus check for silent truncation (L278, PostgreSQL pointer).
Forces in tension: correctness, speed of feedback
Context: PLATFORM, SHARED_STORE
Stack pointers: L278 (PostgreSQL (stack-tagged pointer: names over 63...)

#### ASSURANCE.CONTRACTS Interfaces and Contracts

Decides: Which mechanisms guarantee that producers and consumers of an interface stay compatible while both change?
Rows: -
Context: see children

#### ASSURANCE.CONTRACTS.1 Verification of Service Boundaries

Decides: How is compatibility between independently released services verified?
Rows: L102-L104 (3)
Positions in the evidence (no verdict):
- P1 Contract tests instead of shared integrated environments so teams deploy autonomously (L102; the coverage check records L295 as contradicting it).
- P2 Consumer-driven contracts (precision, safe evolution; many consumers under internal control) against provider-side schema validation (published spec for unknown consumers; strongest version not independently sourced) (L103).
- P3 Every double of an external service backed by a contract test against the real service on its own cadence; failure triggers coordination, need not break the build (L104).
Forces in tension: autonomy, precision, setup cost, broker cost
Context: CONSUMERS, TEAM_SIZE, SYSTEM_SHAPE

#### ASSURANCE.CONTRACTS.2 Evolution of a Shared Interface

Decides: How does an interface change: additively and versioned, or coordinated with every consumer?
Rows: L060, L105, L171, L295, L296, L309, L352 (7)
Positions in the evidence (no verdict):
- P1 Explicit versioning so consumers choose when to move (many or external consumers), against additive change plus coordinated breaking changes deployed together (few in-house consumers) (L295, maintainer; contradicts L171 and L102 for public interfaces).
- P2 Design services for independent deployment without lock-step upgrades (L171).
- P3 Views as a stable read interface (declarative, plannable), against a function with a signature that absorbs change (L309, maintainer, contradicts common practice).
- P4 Retroactive rename for consistency, against forward-only conventions with deprecated items marked and kept (L296).
- P5 Declare the public API, start at 0.1.0, deprecate through a minor release before removal (L060); additive is compatible, removal, rename, type, default and behaviour changes are breaking (L352); every observable behaviour gets depended upon, tests detect but cannot remove implicit dependencies (L105).
Forces in tension: consumer independence, cost, trust, exit risk
Context: CONSUMERS, RELEASE_MODEL, TEAM_SIZE, SHARED_STORE

#### ASSURANCE.CONTRACTS.3 Interface Description as Source

Decides: Is there one machine-readable description from which docs, stubs and tests derive, and what checks it?
Rows: L220-L222 (3)
Positions in the evidence (no verdict):
- P1 One machine-readable description (for example OpenAPI) feeds rendered docs, stubs and tests, against hand-copied reference; no source argues the latter (L220).
- P2 Lint the description in CI against a team ruleset (L221); diff versions in CI and fail on incompatible change (L222); OpenAPI pointers.
Forces in tension: correctness, drift avoidance
Context: CONSUMERS, PLATFORM
Stack pointers: L221 (OpenAPI, AsyncAPI, JSON/YAML (Spectral)); L222 (OpenAPI 3 (openapi-diff; others exist))

#### ASSURANCE.CONTRACTS.4 Failure Semantics of an Interface

Decides: How does an interface report failure?
Rows: L315 (1)
Positions in the evidence (no verdict):
- P1 No competing position recorded: errors name the component and offending values with stable custom codes; mandatory inputs validated first; failure explicit, not silent (L315, maintainer).
Forces in tension: diagnosability
Context: CONSUMERS

#### ASSURANCE.DATA_INTEGRITY Data Integrity Under Change

Decides: Which mechanisms guarantee that stored data stays correct while code, schema and volume change? The realization of changes sits in CHANGE_FLOW.DATA_CHANGE.
Rows: -
Context: see children

#### ASSURANCE.DATA_INTEGRITY.1 Where Integrity Is Enforced

Decides: At which layer are invariants enforced?
Rows: L279, L417 (2)
Positions in the evidence (no verdict):
- P1 Invariants in the application domain layer (one place for logic), against integrity at the store (declared constraints, referential links, validation near the data) because migrations, admin tools and ad-hoc access bypass the application (L279).
- P2 Defend in layers that fall back to one another, since every single strategy eventually fails (L417).
Forces in tension: correctness across writers, cognitive load
Context: SHARED_STORE, CONSUMERS, CRITICALITY

#### ASSURANCE.DATA_INTEGRITY.2 Derived Data Stays in Sync

Decides: Which mechanism keeps denormalized or derived data consistent with its source?
Rows: L281, L282, L313, L314 (4)
Positions in the evidence (no verdict):
- P1 Ladder by cost and strength: documentation only, declared constraints, detection queries, scheduled reconciliation, same-transaction consistency; same-transaction costs write latency and coupling, eventual consistency with a stated window costs less (L281).
- P2 Scheduled detection queries set by importance, with a stated action on divergence (L282).
- P3 Staleness is a designed property: timestamps, freshness target, monitoring built before first production use (L314); monitor duration, failure, backlog and missed runs (L313).
Forces in tension: correctness, write latency, cost, delivery speed
Context: CRITICALITY, SCALE, SHARED_STORE

#### ASSURANCE.DATA_INTEGRITY.3 Self-Auditing Rules

Decides: How are conventions and deployed definitions kept honest?
Rows: L283-L285 (3)
Positions in the evidence (no verdict):
- P1 Enforce a new invariant immediately, against observe-only first (audit on every change, dry-run autofix, a kill-switch default of observe) when known violators exist (L284).
- P2 Every rule ships with a query or script that finds its violations (L283); compare deployed definitions with repository source mechanically (L285).
Forces in tension: correctness, reversibility, delivery speed
Context: SHARED_STORE, TEAM_SIZE

#### ASSURANCE.DATA_INTEGRITY.4 Checks During a Data Change

Decides: Which checks run while data or structure is being changed?
Rows: L280, L391, L396, L414, L415 (5)
Positions in the evidence (no verdict):
- P1 Lint migrations in CI against a list of unsafe operations, with an explicit assertion to override (L396, L414; Postgres, Rails tool pointers).
- P2 Explicit opt-in flag plus validation for destructive or bulk operations of unbounded scope (L280, maintainer).
- P3 Run old and new paths side by side before cutting reads and alert on mismatch (L391); validate new data against old before removal; continuous out-of-band validation jobs (L415).
Forces in tension: correctness, speed, cost
Context: SCALE, CRITICALITY
Stack pointers: L396 (Postgres, Rails); L414 (Rails, Postgres tools)

#### ASSURANCE.DATA_INTEGRITY.5 Reversibility and Restore

Decides: What returns the data after an irreversible step?
Rows: L388, L389, L416 (3)
Positions in the evidence (no verdict):
- P1 Soft deletion or a retention window as first defence, restore as the last (L416).
- P2 Destructive changes are not reversible by script; undo is a restore, prepared and tested before the run (L388); define a backup by whether it restores, test restores regularly, keep the restore path independent of schema tooling (L389).
Forces in tension: recoverability, cost
Context: CRITICALITY, REGULATION, SCALE

#### ASSURANCE.DOCS_SYNC Documentation in Sync

Decides: Which mechanism, at which stage, keeps documentation true as the system changes? Authoring and structure sit in TRANSVERSE.DOCS.
Rows: -
Context: see children

#### ASSURANCE.DOCS_SYNC.1 Same Change, Docs as Code

Decides: When and where is documentation changed relative to the code?
Rows: L210, L211, L230, L238 (4)
Positions in the evidence (no verdict):
- P1 Same pull request as the code (no window of disagreement), against a separate pull request on a release branch so docs ship only when the feature ships (L211).
- P2 Plain text in version control, reviewed, in the repository of the thing documented (L210); reuse the existing workflow (L230); reduced pipeline for docs-only changes (L238).
Forces in tension: correctness, control, delivery speed
Context: RELEASE_MODEL, TEAM_SIZE, DISTRIBUTION

#### ASSURANCE.DOCS_SYNC.2 Trigger and Gate Strength

Decides: Which changes need documentation, and how hard is the gate?
Rows: L212-L214, L226, L237, L239 (6)
Positions in the evidence (no verdict):
- P1 Hard merge gate (does not rely on goodwill), against reviewer-enforced with waiver and a tracked follow-up (L214).
- P2 Gate at release against gate at merge against advisory (L237).
- P3 State a definition-of-done trigger (L213); docs check in code review (L212); automate review chores as CI rules (L226); open a follow-up issue when merged without the reviewer (L239).
Forces in tension: correctness, confidence, delivery speed, team load
Context: REGULATION, RELEASE_MODEL, TEAM_SIZE, DISTRIBUTION

#### ASSURANCE.DOCS_SYNC.3 Mechanical Checks of Content

Decides: Which parts of documentation are checked by machine?
Rows: L219, L223, L224 (3)
Positions in the evidence (no verdict):
- P1 Execute code examples in CI, against keeping them readable rather than obscure test cases (L219).
- P2 Documentation build fails on warnings and unresolved references (L223; Sphinx pointer); check links in CI and on a schedule (L224).
Forces in tension: correctness, clarity
Context: PLATFORM, TEST_MATURITY
Stack pointers: L223 (Sphinx (-W, -n); equivalent flags in other gener...)

#### ASSURANCE.DOCS_SYNC.4 Who Verifies Accuracy

Decides: Who checks that documentation is accurate, and who owns it?
Rows: L215, L227-L229 (4)
Positions in the evidence (no verdict):
- P1 Engineers and code reviewers verify accuracy, writers review non-blocking, against writers approving significant changes (L228).
- P2 Engineers write docs for what they build; writers focus on cross-API-boundary documents (L229); named owner per document (L215); owner mapping by code-owners file (L227, GitHub pointer).
Forces in tension: speed, consistency, quality
Context: TEAM_SIZE, DISTRIBUTION
Stack pointers: L227 (GitHub CODEOWNERS (GitLab and others have equiva...)

#### ASSURANCE.DOCS_SYNC.5 Freshness Over Time

Decides: How does documentation stay true after the change that wrote it?
Rows: L216, L217, L319 (3)
Positions in the evidence (no verdict):
- P1 No competing position recorded: freshness dates tracked as bugs so review is scheduled (L216); remove or mark obsolete documents (L217); date-stamp verification against the live system and point fast-moving topics to a tracker (L319, maintainer).
Forces in tension: correctness over time, cost of ownership
Context: LIFETIME, TEAM_SIZE

#### ASSURANCE.DOCS_SYNC.6 Single Source per Fact

Decides: Where does each fact live, and which copies are derived?
Rows: L218, L318, L320 (3)
Positions in the evidence (no verdict):
- P1 Self-documenting code with history in version control, against a mandatory header with change log in every unit (maintainer; partial tension with L218 and L133) (L318).
- P2 One canonical document per topic (L218); a derived document is read-only and never copied back into the source (L320).
Forces in tension: cost of ownership, reader confidence, durability
Context: CONSUMERS, SHARED_STORE

#### ASSURANCE.SECURITY Security

Decides: Which mechanism at which stage guarantees that the system resists misuse and carries no known weakness? Practice sits in TRANSVERSE.SECURITY; dependency scanning in OWNERSHIP.LIFECYCLE.6.
Rows: -
Context: see children

#### ASSURANCE.SECURITY.1 Design-Time Security Review

Decides: Who reviews a design for security before implementation proceeds?
Rows: L243 (1)
Positions in the evidence (no verdict):
- P1 A qualified person or automated processes in the toolchain, against the risk model (L243); no competing position recorded.
Forces in tension: security, confidence
Context: CRITICALITY, EXPOSURE

#### ASSURANCE.SECURITY.2 Review, Analysis and Test by Stage

Decides: Which security checks run at which pipeline stage?
Rows: L244, L245, L247 (3)
Positions in the evidence (no verdict):
- P1 Human review for backdoors and malicious content, against automation for continuous coverage; the framework treats them as complements (L244).
- P2 Each check at the earliest stage where it can run: secrets and lint before commit; static, composition and infrastructure scanning at build; dynamic tests later (L245).
- P3 Test security features functionally and find vulnerabilities, test types by stage (L247).
Forces in tension: confidence, delivery speed
Context: CRITICALITY, TEST_MATURITY, EXPOSURE

#### ASSURANCE.SECURITY.3 Block or Advise

Decides: Do pipeline security findings block the change or only advise?
Rows: L246 (1)
Positions in the evidence (no verdict):
- P1 Blocking gate (the only guarantee; push protection for secrets); P2 advisory in the developer's workflow (adoption and trust; noisy analyses); P3 blocking with an audited waiver (bypass categories) (L246).
Forces in tension: security, confidence, delivery speed, cognitive load
Context: TEAM_SIZE, REGULATION, TEST_MATURITY

#### ASSURANCE.SECURITY.4 Secure Defaults

Decides: What does the software ship configured as?
Rows: L248 (1)
Positions in the evidence (no verdict):
- P1 A defined secure baseline configuration as default, with the defaults tested (L248); no competing position recorded.
Forces in tension: security
Context: DISTRIBUTION, EXPOSURE

#### ASSURANCE.SECURITY.5 Secret Scanning and Compromise Response

Decides: Where are secrets caught, and what follows a finding?
Rows: L251, L252 (2)
Positions in the evidence (no verdict):
- P1 Layered scanning in editor or pre-commit, at push as a blocking check, and in CI; blocking before history is preferred to alerting after (L251).
- P2 A found secret is compromised: revoke, rotate by automation, remove, keep audit logs (L252).
Forces in tension: security, speed
Context: EXPOSURE, TEAM_SIZE

#### ASSURANCE.SECURITY.6 Access Enforcement and Automation Limits

Decides: At which layer is access enforced, and how are automated actors confined?
Rows: L325, L326 (2)
Positions in the evidence (no verdict):
- P1 Enforce access at the lowest layer every path passes through (least privilege by role), against application-only authorization (speed, misses direct paths) (L325, maintainer).
- P2 One sanctioned path to the data system for an AI agent or other automation, with limits enforced in tooling (single statement, read-only on production, timeout, audit log), not by instruction (L326, maintainer; no public counterpart).
Forces in tension: security, speed, auditability
Context: SHARED_STORE, AI_AGENTS, CRITICALITY

#### ASSURANCE.PERFORMANCE Performance

Decides: Which mechanisms at which stages guarantee that performance holds as code and load change? Capacity planning sits in OPERATION.CAPACITY.
Rows: -
Context: see children

#### ASSURANCE.PERFORMANCE.1 Targets, Budgets and Optimisation Stance

Decides: What are the targets, and when is optimisation applied?
Rows: L420, L421, L434, L435 (4)
Positions in the evidence (no verdict):
- P1 Measure first and optimise the critical few, against estimating and testing from design onward so architectural bottlenecks surface early; both agree on measuring before tuning (L434).
- P2 Targets from user needs and the SLO, with pass/fail thresholds (L420); split budgets across layers (L421); enforce size and timing budgets in the build for client-delivered software (L435, front-end pointer).
Forces in tension: cost of ownership, delivery speed, avoided rework
Context: SCALE, SYSTEM_SHAPE, CRITICALITY
Stack pointers: L435 (web front end (budget metrics such as Time to In...)

#### ASSURANCE.PERFORMANCE.2 Test Environment and Realism

Decides: How faithful is the environment and the load?
Rows: L422-L425 (4)
Positions in the evidence (no verdict):
- P1 Production-identical environment (critical workloads), P2 scaled-down (non-critical), P3 test in production with guardrails (L422).
- P4 Real third-party calls (realism), against mocked external dependencies (repeatability; providers may forbid load) (L424).
- P5 Whole workload end to end (L423); test to the breaking point, not a small safety factor (L425); representative mix and data (L424).
Forces in tension: confidence, fidelity, cost of ownership
Context: CRITICALITY, BUDGET, PLATFORM

#### ASSURANCE.PERFORMANCE.3 Test Types and When They Run

Decides: Which load test types run on which trigger?
Rows: L108, L426-L429 (5)
Positions in the evidence (no verdict):
- P1 Every change gated in the pipeline (feedback, regression traced to one change), against scheduled or event-driven runs for long, expensive or noisy tests (L427).
- P2 Several test types matched to risk, widened with experience (L426); baseline comparison for regression and drift (L428); hypothesis test for high-impact changes (L429); performance regression tests and production-side configuration checks (L108).
Forces in tension: speed of feedback, cost, noise
Context: TEST_MATURITY, SCALE, BUDGET

#### ASSURANCE.PERFORMANCE.4 Measurement Validity

Decides: Is the load test measuring what users experience?
Rows: L430, L431 (2)
Positions in the evidence (no verdict):
- P1 Generate load open-loop or correct for coordinated omission (L430; one T3 source); measure goodput, not only server throughput (L431).
Forces in tension: correctness of the measurement
Context: SCALE

#### ASSURANCE.PERFORMANCE.5 Production Tests for Performance

Decides: Is performance also tested in production?
Rows: L432, L433 (2)
Positions in the evidence (no verdict):
- P1 Pre-production only (user safety, reversibility), against controlled production tests (off-peak, ramped, rollback ready) for what only production reveals (L432).
- P2 Synthetic load misses state coverage, so complement with canary analysis on organic traffic (L433).
Forces in tension: safety, realism
Context: CRITICALITY, REGULATION, PLATFORM

#### ASSURANCE.AVAILABILITY Availability

Decides: Which mechanisms at which stages guarantee the service stays available through dependency failure, overload, change and incident?
Rows: -
Positions in the evidence (no verdict):
- Mechanisms by stage, spread over the tree: design (remote-call discipline .1, degraded modes .2); pre-production (resilience experiments .3, load tests PERFORMANCE.2); deploy (rollout DEPLOY.3, rollback ROLLBACK.1); production (SLOs and alerts OPERATION.RELIABILITY and ALERTING, synthetic probes OPERATION.TELEMETRY.4, verification .4); recovery (OPERATION.RUNBOOKS); readiness (OPERATION.READINESS).
Context: see children

#### ASSURANCE.AVAILABILITY.1 Remote-Call Discipline

Decides: How is every call to a dependency bounded so that its failure does not become the team's outage?
Rows: L332-L339 (8)
Positions in the evidence (no verdict):
- P1 Circuit breaker with half-open probing plus fallback (slow-failing synchronous dependencies with many callers); P2 retry budget alone (simple, few callers); P3 neither: queue and dead-letter (event-driven designs) (L338).
- P4 Timeouts sized from measured latency percentile (L332); retry only transient failures with capped backoff and jitter, at one layer (L333); retry non-reads only when idempotent or keyed (L334); honour throttle signals (L335); use the provider's client (L336); process-wide retry budget (L337); propagate deadlines (L339).
Forces in tension: protection of own resources, simplicity, decoupling, fast failure
Context: SYSTEM_SHAPE, SCALE, CRITICALITY

#### ASSURANCE.AVAILABILITY.2 Degraded Modes and Overload

Decides: What does the system do when a dependency or capacity is missing?
Rows: L032, L442 (2)
Positions in the evidence (no verdict):
- P1 Loosely coupled design with a degraded mode (cached or default result, reduced feature) for each non-essential dependency, exercised regularly (L032).
- P2 Design and test overload behaviour: reject early, degrade before error, cap retries per request and client, throttle client-side (L442).
Forces in tension: availability, user experience, cost
Context: CRITICALITY, SCALE

#### ASSURANCE.AVAILABILITY.3 Resilience Experiments

Decides: Are resilience experiments run, and where?
Rows: L120 (1)
Positions in the evidence (no verdict):
- P1 Automated, ideally continuous experiments on production traffic with a steady-state hypothesis and bounded blast radius (authenticity; needs observability and rollback), against pre-production only (safety; regulated or low-recovery systems, inferred and unsourced) (L120; one T3 source).
Forces in tension: realism, safety
Context: TEST_MATURITY, REGULATION, CRITICALITY

#### ASSURANCE.AVAILABILITY.4 Verification in Production

Decides: Which checks run on live traffic to catch what pre-production missed?
Rows: L118, L119 (2)
Positions in the evidence (no verdict):
- P1 A/B diff on identical traffic and canary analysis before full rollout (L118).
- P2 Testing in production is valuable and risky: findings already affect users, test data can become visible; limit blast radius and isolate test data (L119; partial tension with L265).
Forces in tension: fidelity, user impact
Context: TEST_MATURITY, SCALE, EXPOSURE

#### ASSURANCE.ARTIFACT Artifact Integrity

Decides: Which mechanism guarantees that what runs is what was reviewed and built from the source? (extension: the evidence shows a property distinct from the seven named)
Rows: L048, L151, L152 (3)
Positions in the evidence (no verdict):
- P1 Reproducible builds so any party can verify a binary by bit-identical rebuild (high-assurance or widely distributed artifacts), against trusting signed provenance without rebuild (most teams) (L048).
- P2 Target build-integrity level by risk: provenance at least; hosted platform with signed provenance for anything distributed; hardened isolated builds where insider or credential risk exists (L151).
- P3 Protect code and release integrity, archive releases, as secure-development frameworks require (L152).
Forces in tension: security, control, build discipline cost
Context: CRITICALITY, DISTRIBUTION, REGULATION

### Branch CHANGE_FLOW

#### CHANGE_FLOW Change Flow

Decides: How does a change travel from idea to production and back out again? Realization branch: it carries out the guarantees decided in ASSURANCE and the lifecycle decided in OWNERSHIP.
Rows: -
Context: RELEASE_MODEL, TEAM_SIZE, SCALE, REGULATION

#### CHANGE_FLOW.INTEGRATION Version Control and Integration

Decides: How is work held in version control and merged into the shared line?
Rows: -
Context: see children

#### CHANGE_FLOW.INTEGRATION.1 Branch Lifetime and Release Branches

Decides: How long does work live apart from the mainline?
Rows: L125-L129 (5)
Positions in the evidence (no verdict):
- P1 Daily integration to trunk, branches of hours (DORA, Google, Fowler), against feature branches merged when complete for sparse or untrusted contributors (L125).
- P2 Trunk or GitHub flow for continuous delivery; release branches (git-flow) when several versions live in the field (L126); with continuous deployment no release branch at all (L127).
- P3 Avoid long-lived development branches (L128); hide unfinished work in mainline behind flags or branch by abstraction (L129).
Forces in tension: speed of feedback, control, simplicity
Context: RELEASE_MODEL, TEAM_SIZE, TEST_MATURITY
Realizes: ASSURANCE.RULES.3

#### CHANGE_FLOW.INTEGRATION.2 Protecting the Mainline

Decides: How is the shared line protected and restored when broken?
Rows: L131, L146 (2)
Positions in the evidence (no verdict):
- P1 No competing position recorded: required status checks and review, no force push, restricted push rights, signed commits where authorship provenance is required (L131, GitHub pointer); a broken mainline is top-priority work, revert to restore, name a responsible person (L146).
Forces in tension: integrity, speed
Context: TEAM_SIZE, REGULATION
Realizes: ASSURANCE.ARTIFACT, ASSURANCE.SECURITY.2
Stack pointers: L131 (GitHub terms (pointer); neutral in principle)

#### CHANGE_FLOW.INTEGRATION.3 Repository Layout

Decides: What lives in version control, and in one repository or several?
Rows: L124, L132 (2)
Positions in the evidence (no verdict):
- P1 Monorepo (one-version trivial, atomic cross-project change), against multiple repositories (legal, security or access separation), against a virtual monorepo (L132).
- P2 Everything needed to build, deploy and restore lives in version control so a clean machine can rebuild (L124).
Forces in tension: correctness, speed of change, control, security
Context: SCALE, REGULATION, TEAM_SIZE
Realizes: OWNERSHIP.LIFECYCLE.1

#### CHANGE_FLOW.INTEGRATION.4 History, Merge Method and Commits

Decides: What does the history look like, and what do commits say?
Rows: L130, L133, L134 (3)
Positions in the evidence (no verdict):
- P1 Squash (one commit per change), rebase (linear, individual commits) or merge commit (fidelity); one method per repository, recorded (L130).
- P2 Conventional Commits where release notes or version bumps are generated, against free-form what-and-why (L134).
- P3 Atomic complete changes with a message of what and why (L133; maintainer's mandatory header is in partial tension, see ASSURANCE.DOCS_SYNC.6).
Forces in tension: legible history, fidelity, bisect granularity, automation, cognitive load
Context: TEAM_SIZE, DISTRIBUTION

#### CHANGE_FLOW.REVIEW Review

Decides: Who checks a change before it enters the mainline, and how fast?
Rows: -
Context: see children

#### CHANGE_FLOW.REVIEW.1 Review Mechanism and Who Approves

Decides: Which review mechanism applies, and is approval per change or by risk?
Rows: L136, L137, L143, L298 (4)
Positions in the evidence (no verdict):
- P1 Mandatory asynchronous approval on every change (confidence, audit trail), P2 synchronous review or pairing, P3 Ship / Show / Ask (L137); principle of an independent human check, dissent only from Ship / Show / Ask (L136).
- P4 Peer review plus automation with segregation of duties, against an external change approval board (L143).
- P5 Escalate review by risk to named senior approvers for changes that hold locks, run over about five minutes or affect availability (L298, maintainer; partial tension with L143).
Forces in tension: confidence, knowledge sharing, delivery speed, trust cost
Context: TEAM_SIZE, REGULATION, CRITICALITY, TEST_MATURITY
Realizes: ASSURANCE.BEHAVIOUR

#### CHANGE_FLOW.REVIEW.2 Review Standard and Latency

Decides: What counts as approvable, and how fast must a review come?
Rows: L138, L139, L142 (3)
Positions in the evidence (no verdict):
- P1 No competing position recorded: approve when the change definitely improves code health; facts over preference (L138); respond within one business day, optimising team throughput (L139); review is understanding and knowledge transfer (L142).
Forces in tension: code health, throughput, knowledge sharing
Context: TEAM_SIZE

#### CHANGE_FLOW.REVIEW.3 Change Size and Prior Automation

Decides: How big is a reviewed change, and what runs before a human looks?
Rows: L140, L141, L172, L297 (4)
Positions in the evidence (no verdict):
- P1 No competing position recorded: about 100 lines typical, 1000 too large, refactoring separate, tests with the logic (L140); automation (format, lint, tests, build) before human review (L141); small batches and frequent commits with AI-generated code (L172, DORA); maintained anti-pattern catalog read by change type (L297, maintainer).
Forces in tension: review quality, throughput
Context: TEAM_SIZE, AI_AGENTS
Realizes: ASSURANCE.BEHAVIOUR.5

#### CHANGE_FLOW.BUILD Build and Pipeline

Decides: How is a change built and exercised in a reference environment?
Rows: L144, L148-L150 (4)
Positions in the evidence (no verdict):
- P1 No competing position recorded: automated build and self-testing suite on every push to mainline in a reference environment (L144); pipeline state and flow visible to all with an audit trail (L148); scripted, repeatable, hermetic builds (L149); separate build, release and run, immutable uniquely identified releases, same artifact to every environment (L150).
Forces in tension: repeatability, visibility
Context: TEAM_SIZE, TEST_MATURITY
Realizes: ASSURANCE.RULES.3, ASSURANCE.ARTIFACT

#### CHANGE_FLOW.RELEASE Release

Decides: How is a built change made available to users?
Rows: -
Context: see children

#### CHANGE_FLOW.RELEASE.1 Versioning and Identification

Decides: How is a released artifact named?
Rows: L135 (1)
Positions in the evidence (no verdict):
- P1 Semantic Versioning for libraries and APIs (consumer trust), a monotonic release identifier for services with one live version; calendar versioning not read (open) (L135).
Forces in tension: consumer trust, simplicity
Context: DISTRIBUTION, CONSUMERS

#### CHANGE_FLOW.RELEASE.2 Cadence and Batch Size

Decides: How often is a release made?
Rows: L153 (1)
Positions in the evidence (no verdict):
- P1 Continuous, each merge ('faster is safer'; one live version, strong tests), against a scheduled train (predictability, many components) (L153).
Forces in tension: delivery speed, predictability, blast radius
Context: RELEASE_MODEL, TEST_MATURITY

#### CHANGE_FLOW.RELEASE.3 Release Decoupled from Deployment

Decides: Is shipping code separated from making a feature available?
Rows: L154, L155 (2)
Positions in the evidence (no verdict):
- P1 Feature flags decouple release from deployment, against no flags with small, immediately released batches (L154).
- P2 Flags are inventory with carrying cost: classify, expiry for release toggles, test relevant states (L155).
Forces in tension: reversibility, cost of ownership
Context: RELEASE_MODEL, TEAM_SIZE

#### CHANGE_FLOW.RELEASE.4 Approval Gates and Who May Release

Decides: Which stages of the path need human authorization, and who may perform release operations?
Rows: L156, L157, L164 (3)
Positions in the evidence (no verdict):
- P1 Hands-off: code review the last manual gate, rest automated and alarm-driven (mature automation), against human authorization gates for some stages (high criticality, regulation) (L156; maintainer L290 contradicts L159).
- P2 Restrict who performs release operations by policy while keeping release self-service for teams (L157); block deployments during active incidents and outside responder hours (L164).
Forces in tension: delivery speed, control, reversibility
Context: CRITICALITY, REGULATION, TEST_MATURITY, AI_AGENTS
Realizes: ASSURANCE.RULES.1

#### CHANGE_FLOW.DEPLOY Deployment

Decides: How does a release reach production?
Rows: -
Context: see children

#### CHANGE_FLOW.DEPLOY.1 Deploy Mechanism

Decides: How is deployment automated and how is state held?
Rows: L159, L166, L167 (3)
Positions in the evidence (no verdict):
- P1 Same automated process for every environment, any authorized person, any version on demand (L159; contradicted by maintainer L290 and L328).
- P2 Immutable replacement of instances, against managed mutable servers with configuration tools (L166).
- P3 Declarative desired state pulled and reconciled by agents, against push from CI (L167).
Forces in tension: consistency, reversibility, drift control, cost of ownership
Context: PLATFORM, REGULATION, TEAM_SIZE
Realizes: ASSURANCE.ARTIFACT

#### CHANGE_FLOW.DEPLOY.2 Environment Set and Parity

Decides: How alike are production and the other environments?
Rows: L165 (1)
Positions in the evidence (no verdict):
- P1 Production parity in all environments, including local backing services, against reducing pre-production and testing in production with a canary and safe rollback (L165).
- P2 Accept divergence and route the change to an environment-specific manual path (maintainer, L328; contradicts L165).
Forces in tension: confidence, cost of ownership, fidelity
Context: SCALE, BUDGET, CRITICALITY
Realizes: ASSURANCE.PERFORMANCE.2

#### CHANGE_FLOW.DEPLOY.3 Rollout Strategy

Decides: How is a new version exposed to traffic?
Rows: L160, L161, L173 (3)
Positions in the evidence (no verdict):
- P1 Blue-green (instant switch and rollback, second environment), P2 canary (gradual exposure, several live versions), P3 one-box then waves (many regions) (L160).
- P4 Evaluate a canary against a concurrent control on a few user-impact metrics, one canary at a time (L161).
- P5 Most outages come from changes to a live system, so automate progressive rollout, detection and rollback; playbooks cut repair time (L173).
Forces in tension: reversibility, confidence, infrastructure cost, blast radius
Context: SCALE, CRITICALITY, TEST_MATURITY, PLATFORM
Realizes: ASSURANCE.AVAILABILITY.4

#### CHANGE_FLOW.ROLLBACK Rollback and Recovery of a Change

Decides: How is a bad change undone?
Rows: -
Context: see children

#### CHANGE_FLOW.ROLLBACK.1 Detection and Rollback or Fix Forward

Decides: Is a bad release rolled back automatically or fixed forward?
Rows: L162, L163 (2)
Positions in the evidence (no verdict):
- P1 Automated detection and rollback on alarm (any backward-compatible change), against fix forward from trunk (very fast pipeline, changes not reversible by redeploy); no source states the decision rule (L162).
- P2 Make each change backward compatible with the previous version (parallel change; schema separate from application) so rollback, mixed fleets and independent release are possible (L163; maintainer L288 agrees).
Forces in tension: reversibility, recovery time, simplicity
Context: CRITICALITY, TEST_MATURITY, SCALE
Realizes: ASSURANCE.AVAILABILITY

#### CHANGE_FLOW.ROLLBACK.2 Undoing a Data Change

Decides: What undoes a failed data change?
Rows: L288, L387, L390 (3)
Positions in the evidence (no verdict):
- P1 A written reverse for every migration (reversibility, downgrade after a vulnerability; regulated or packaged software), against backward compatibility plus roll-forward plus restore, with no generated undo (undo scripts are untested code) (L387).
- P2 Maintainer: forward-only with a documented undo section prepared ahead, ticket named, no migration-opened transaction (L288; partial tension with automated rollback L162).
- P3 The last reversible point is before the old structure is removed and reads move irreversibly (L390).
Forces in tension: reversibility, cost of ownership, honesty about irreversible changes
Context: REGULATION, DISTRIBUTION, SCALE
Realizes: ASSURANCE.DATA_INTEGRITY.5

#### CHANGE_FLOW.MEASURE Measuring Delivery

Decides: How is delivery measured so that it improves without becoming a target?
Rows: L169, L170 (2)
Positions in the evidence (no verdict):
- P1 Five DORA metrics to guide improvement, not to rank people (L169); speed and stability correlate, but only with supporting practices; deployment frequency alone yields failures and burnout; the conventional speed-against-stability view has no source defending it (L170); production side L208 in OPERATION.FEEDBACK.
Forces in tension: improvement without gaming
Context: TEAM_SIZE

#### CHANGE_FLOW.DATA_CHANGE Data and Schema Change

Decides: How is a change to structure or stored data carried out safely? Realizes the guarantees of ASSURANCE.DATA_INTEGRITY.
Rows: -
Context: see children

#### CHANGE_FLOW.DATA_CHANGE.1 Migrations as Versioned Scripts

Decides: What is the unit of change, and what is the source of truth?
Rows: L286, L287, L289, L379-L381, L418 (7)
Positions in the evidence (no verdict):
- P1 Declarative desired state, against ordered versioned change scripts, against a hybrid (develop declaratively, generate versioned files); the evidence is a tool vendor, no T2 position found (L381).
- P2 Strict immutability of an applied migration, checksum-enforced (the strict form wins wherever more than one environment applied it), against editing after rolling the changeset back (L380; maintainer L287).
- P3 Ordered, once-only, version-tracked files recorded in a history table, never applied by hand (L286, L379); tracked in the target database (L418); idempotent DDL except one-time data migrations (L289).
Forces in tension: auditability, determinism, developer load, iteration speed
Context: REGULATION, DISTRIBUTION, SHARED_STORE, PLATFORM
Realizes: ASSURANCE.DATA_INTEGRITY

#### CHANGE_FLOW.DATA_CHANGE.2 Compatible Change Sequence

Decides: In what order do structure and code change so both versions work across the deployment window?
Rows: L292, L382-L386, L409, L419 (8)
Positions in the evidence (no verdict):
- P1 Expand, migrate, contract for incompatible changes; schema deploys before and separately from the application, first step supporting both versions (L382, L383, L386); small changes (L385); schedule and own the contract step (L384); stop reads before dropping (L419, Rails pointer).
- P2 Gate the application deploy on a declared minimum schema version (maintainer L292; public sources support only the order, no explicit gate).
- P3 Compatibility surface during a transition: views or triggers plus a code-side access layer, against a function with a signature as stable interface (maintainer, no public source), against versioned interfaces for remote APIs (L409).
Forces in tension: correctness during the window, reversibility, cost
Context: CONSUMERS, SHARED_STORE, RELEASE_MODEL
Realizes: ASSURANCE.CONTRACTS.2, ASSURANCE.DATA_INTEGRITY
Stack pointers: L419 (Rails (the generalization is neutral and follows...)

#### CHANGE_FLOW.DATA_CHANGE.3 Locks and Online Change

Decides: How is structure changed on a live, shared store without blocking it?
Rows: L304, L392-L395, L397, L402 (7)
Positions in the evidence (no verdict):
- P1 Trigger-based online schema tools (simple, older, write overhead, cannot pause), log-based tools (control, high-write masters), native online DDL (metadata-only operations) (L397; MySQL and Postgres tool pointers).
- P2 Know the lock a statement takes (L392); per-session lock timeout with retry (L393); non-blocking forms of each change (L394); non-transactional step for concurrent index builds (L395); time budget by class, maintainer about five minutes (L402); do not shard schema changes (L304).
Forces in tension: availability, simplicity, control
Context: SCALE, PLATFORM, CRITICALITY
Realizes: ASSURANCE.AVAILABILITY
Stack pointers: L304 (PostgreSQL (stack-tagged pointer)); L392 (Postgres, MySQL (general idea neutral)); L393 (Postgres); L394 (Postgres, MySQL); L395 (Postgres (Rails tool as source)); L397 (MySQL (gh-ost, pt-online-schema-change), Postgre...)

#### CHANGE_FLOW.DATA_CHANGE.4 Backfills and Bulk Jobs

Decides: How is a very large data change run?
Rows: L299-L303, L305-L307, L398-L401, L412, L413 (14)
Positions in the evidence (no verdict):
- P1 Where a backfill runs: inside a migration step (minutes), as an application background job (long work), or offline from a snapshot (very large, multi-table) (L401).
- P2 One long transaction (simple, locks and bloat) against sharding, decided by a size gate (L299, maintainer).
- P3 Bounded, throttled, pausable batches, re-runnable with the same result, paced by replica lag (L398, L399, L400, L300).
- P4 Done means a convergence query returns zero; ramp concurrency, halt on first failure; checklist before production; watch the target system; tag the ticket key in the statement; compose standard tools (L301, L302, L303, L305, L306, L307; public counterpart not found for L301, L302, L306: L412, L413).
Forces in tension: production safety, simplicity, zero load, control
Context: SCALE, CRITICALITY, PLATFORM, AI_AGENTS
Realizes: ASSURANCE.DATA_INTEGRITY.4

#### CHANGE_FLOW.DATA_CHANGE.5 Rehearsal Data

Decides: On what data is a migration rehearsed?
Rows: L293, L403-L405 (4)
Positions in the evidence (no verdict):
- P1 Production-shaped data (realistic timing and plans; large tables; cloning and personal-data cost), against developer-owned databases with versioned sample data (isolation, speed, no exposure) (L403).
- P2 Mask personal data before it leaves production and block side effects in the copy (L404); measure duration and locks on a rehearsal copy and keep the measure (L405); restore a dump of development data and apply every migration on each change request (L293, maintainer).
Forces in tension: confidence, isolation, speed, no exposure
Context: SCALE, REGULATION, EXPOSURE

#### CHANGE_FLOW.DATA_CHANGE.6 Who Applies a Change, by Risk

Decides: Which data changes apply automatically and which are run by named people?
Rows: L168, L290, L291, L327, L328, L408, L410 (7)
Positions in the evidence (no verdict):
- P1 Automate fully through the pipeline (small, fast, compatible changes; DORA), against gating long or locking changes behind a person and a manual lane (high criticality, large tables; maintainer) (L410, L290; contradicts L159).
- P2 Database change in the same pipeline as application change, not a separate manual track (L168; contradicted by maintainer L294 for registry content).
- P3 An AI agent writes the script, work-list query and convergence query for a high-blast-radius job but does not execute it; the human runs it (L327, maintainer; no public counterpart).
- P4 Route environment-specific changes to a manual migration (L328); involve production database managers early, make pending changes visible (L408); ticket-keyed delivery path (L291).
Forces in tension: delivery speed, consistency, reversibility, control, audit
Context: SCALE, CRITICALITY, REGULATION, AI_AGENTS, SHARED_STORE
Realizes: CHANGE_FLOW.RELEASE.4, ASSURANCE.SECURITY.6

#### CHANGE_FLOW.DATA_CHANGE.7 Separate Tracks for Urgent, Data and Registry Changes

Decides: Which changes run on their own track?
Rows: L294, L406, L407, L411 (4)
Positions in the evidence (no verdict):
- P1 Every change through the same migration pipeline (single audited path), against idempotent authoring script as source of truth for configuration-like registry content, deployed by running it, with a migration as optional audit mirror (L294; no public counterpart L411; contradicts L168).
- P2 Separate folder with its own tracking for urgent data fixes (L406); keep data migrations apart from schema migrations in transaction and timing (L407).
Forces in tension: control, delivery speed, single audit path
Context: SHARED_STORE, TEAM_SIZE

### Branch OPERATION

#### OPERATION Operation

Decides: How is the running system observed, kept within its reliability target, and fed back into development? Realization branch: it carries out ASSURANCE.AVAILABILITY and ASSURANCE.PERFORMANCE in production.
Rows: -
Context: TEAM_SIZE, CRITICALITY, SCALE, REGULATION

#### OPERATION.RELIABILITY Reliability Targets

Decides: What reliability is promised and how is it traded against change?
Rows: -
Context: see children

#### OPERATION.RELIABILITY.1 Targets and Indicators

Decides: How are SLOs and SLIs chosen?
Rows: L174-L179 (6)
Positions in the evidence (no verdict):
- P1 Set targets from user need, not from history (L179 a), against starting with what is measurable and cheap, then iterating (L179 b); both are Google, reconciled by start-then-review.
- P2 Below 100% by choice (L174); SLIs from the user's point of view (L175); anchored on critical user journeys (L176); latency as percentiles (L177); few SLOs (L178).
Forces in tension: reliability fit, adoption speed, avoiding heroics
Context: CRITICALITY, TEAM_SIZE, REGULATION
Realizes: ASSURANCE.AVAILABILITY

#### OPERATION.RELIABILITY.2 Error Budget and Its Policy

Decides: What does consuming the budget do to releases?
Rows: L180-L183 (4)
Positions in the evidence (no verdict):
- P1 Hard freeze of changes except P0 and security fixes (many consumers, strict SLAs, weak safety culture), against self-regulation by the team (small, high-trust teams) (L182).
- P2 An error budget as shared objective mechanism trading velocity against reliability; no source for a no-budget minority, open (L180); written policy agreed by product and operations (L181); postmortem triggers from budget consumption (L183).
Forces in tension: control, reliability, speed, autonomy
Context: TEAM_SIZE, CRITICALITY, CONSUMERS
Realizes: CHANGE_FLOW.RELEASE.4

#### OPERATION.ALERTING Alerting

Decides: What pages a human, and what does not?
Rows: L184-L188 (5)
Positions in the evidence (no verdict):
- P1 Symptom-only paging (low noise, limited on-call capacity), plus white-box cause alerts for imminent failures (early warning) (L185).
- P2 Simple threshold alerts (small services), against multiwindow multi-burn-rate alerts (when an SLO exists and false pages are costly) (L187).
- P3 Page only urgent, actionable, user-visible conditions (L184); every page needs human judgment (L186); remove rarely exercised rules (L188).
Forces in tension: early warning, low noise, cognitive load
Context: TEAM_SIZE, SCALE, CRITICALITY
Realizes: ASSURANCE.AVAILABILITY

#### OPERATION.TELEMETRY Telemetry

Decides: What is collected, how is it stored and standardised, and what does it cost?
Rows: -
Context: see children

#### OPERATION.TELEMETRY.1 Signals to Collect

Decides: Which signals are collected and who is proficient in them?
Rows: L189-L193, L195 (6)
Positions in the evidence (no verdict):
- P1 Monitoring and observability as complements (L193), against replacing the pillars model (see .2).
- P2 White-box monitoring combined with black-box probing (L189); latency, traffic, errors, saturation (L190); minimal rate, errors, duration per service (L191); USE as a quick first check only (L192); observability a shared responsibility (L195).
Forces in tension: diagnosability, shared ownership
Context: TEAM_SIZE, SYSTEM_SHAPE
Realizes: ASSURANCE.AVAILABILITY

#### OPERATION.TELEMETRY.2 Storage Model and Sampling

Decides: Pillars or wide events, and what is sampled?
Rows: L194, L200 (2)
Positions in the evidence (no verdict):
- P1 Separate metrics, logs and traces (standard, mature, cheap aggregated alerting), against wide structured events as the single store (exploratory power; held by a vendor) (L194).
- P2 Head sampling (cost, simplicity), tail sampling (completeness of error traces, operationally heavy), or no sampling (low volume or regulation) (L200).
Forces in tension: cost, maturity, exploratory power, completeness
Context: SCALE, BUDGET, REGULATION

#### OPERATION.TELEMETRY.3 Instrumentation Standards

Decides: Which instrumentation API and conventions are used?
Rows: L196-L199, L201 (5)
Positions in the evidence (no verdict):
- P1 Vendor-neutral instrumentation API and semantic conventions (exit risk, interoperability), against a vendor SDK or agent (less setup, deeper features) (L196).
- P2 Logs as an unbuffered stream to standard output, routed by the platform, against logging libraries writing to files or collectors outside container contexts (L201).
- P3 Zero-code plus code-based instrumentation (L197); libraries depend on the API only (L198); W3C trace context (L199); OpenTelemetry and HTTP pointers.
Forces in tension: exit risk, interoperability, setup cost
Context: PLATFORM, SCALE
Stack pointers: L197 (OpenTelemetry); L198 (OpenTelemetry); L199 (HTTP)

#### OPERATION.TELEMETRY.4 Synthetic and Real-User Monitoring

Decides: How are failures detected before users report them?
Rows: L453-L455 (3)
Positions in the evidence (no verdict):
- P1 Synthetic monitoring (detects with no traffic) and real-user monitoring (experienced performance) together (L453).
- P2 Checks along real customer routes from several vantage points with payload validation (L454); monitor the monitoring (L455; one line, one source).
Forces in tension: early detection, realism
Context: SCALE, CRITICALITY
Realizes: ASSURANCE.AVAILABILITY, ASSURANCE.PERFORMANCE.5

#### OPERATION.TELEMETRY.5 Telemetry Cost Budget

Decides: How is the cost of telemetry bounded?
Rows: L456-L460 (5)
Positions in the evidence (no verdict):
- P1 No competing position recorded (agreement: majority, single vendor or tool sources): volume and cardinality are a cost to design (L456); bounded label cardinality (L457); filter low-value telemetry, coarsen buckets (L458); instrument broadly, except hot paths (L459); explicit per-service telemetry budget (L460). Prometheus and Grafana pointers.
Forces in tension: cost, granularity
Context: SCALE, BUDGET
Stack pointers: L457 (Prometheus-style metrics systems (numbers are th...); L458 (Grafana and Prometheus-style tooling); L459 (Prometheus client libraries (numbers are that to...)

#### OPERATION.INCIDENTS Incidents

Decides: How are incidents run, learned from, and survived by the people on call?
Rows: -
Context: see children

#### OPERATION.INCIDENTS.1 Running an Incident

Decides: How is an incident declared and commanded?
Rows: L202-L204, L209 (4)
Positions in the evidence (no verdict):
- P1 Early, low-threshold declaration with written conditions (shared load, faster response), against a high bar reserved for severe events (lower process cost in tiny teams; not found in a read source, open) (L203).
- P2 Named roles and a live incident document, only the operations lead changes the system (L202); severity levels defined and rehearsed (L204); integration with risk management (L209).
Forces in tension: speed, shared load, process cost
Context: TEAM_SIZE, CRITICALITY, REGULATION

#### OPERATION.INCIDENTS.2 Postmortems

Decides: What is learned and who owns the follow-up?
Rows: L205, L206 (2)
Positions in the evidence (no verdict):
- P1 No competing position recorded: blameless postmortems for significant incidents with written triggers (L205); every action item with owner, priority and tracker entry, published within days (L206).
Forces in tension: learning, prevention
Context: TEAM_SIZE

#### OPERATION.INCIDENTS.3 Human Cost of Operation

Decides: How much operational load is a person given?
Rows: L207, L452 (2)
Positions in the evidence (no verdict):
- P1 Toil capped at 50%, on-call about 25% and two incidents per 12-hour shift; the numbers assume dedicated teams of 6 to 8 per site (L207, L452); small teams where developers own operations must decide their own limit.
Forces in tension: cognitive load, retention
Context: TEAM_SIZE, SCALE

#### OPERATION.CAPACITY Capacity

Decides: How much resource is provisioned for expected and unexpected load, and how is the data store's health watched?
Rows: -
Context: see children

#### OPERATION.CAPACITY.1 Capacity Planning

Decides: How is capacity planned and how much headroom is held?
Rows: L436-L441 (6)
Positions in the evidence (no verdict):
- P1 Pre-provision for peak and failover (hard peaks, long scale-up, critical systems), against autoscaling with tested limits (variable load, fast scale-up); neither source fixes a headroom number (L440).
- P2 Replace spreadsheet plans with declared requirements from which allocations are computed when service count makes manual plans brittle (L441).
- P3 Plan before predicted changes and periodically (L436); model in resources, not requests per second (L437); derive from requirements (L438); pair with load testing and overload behaviour (L439).
Forces in tension: reliability, cost, performance
Context: SCALE, BUDGET, CRITICALITY, PLATFORM
Realizes: ASSURANCE.PERFORMANCE, ASSURANCE.AVAILABILITY.2

#### OPERATION.CAPACITY.2 Data Store Health

Decides: Which store-level health signals are watched?
Rows: L317 (1)
Positions in the evidence (no verdict):
- P1 Find unused indexes by usage counters and drop them, watch index and table bloat, rebuild concurrently (L317, maintainer; PostgreSQL pointer).
Forces in tension: performance, storage cost
Context: SCALE, PLATFORM
Realizes: ASSURANCE.PERFORMANCE
Stack pointers: L317 (PostgreSQL (stack-tagged pointer))

#### OPERATION.READINESS Operational Readiness

Decides: What must be true before launch, and who certifies it?
Rows: L443-L447 (5)
Positions in the evidence (no verdict):
- P1 Independent reviewing team (control, quality, knowledge transfer), against a self-service checklist the owning team certifies (scale across decentralised teams); relative effectiveness: no evidence read, open (L444).
- P2 Launch only against a checklist covering architecture, capacity, failure modes, monitoring, emergency response, change management, rollout (L443); built from own incidents, short, tiered (L445); re-run over the lifecycle (L446); convert repeated findings to automated guardrails (L447).
Forces in tension: control, delivery speed, scalability of review
Context: TEAM_SIZE, CRITICALITY, REGULATION
Realizes: ASSURANCE.AVAILABILITY

#### OPERATION.RUNBOOKS Runbooks and Recovery Practice

Decides: How are response procedures written, matured and exercised?
Rows: -
Context: see children

#### OPERATION.RUNBOOKS.1 Runbooks and Playbooks

Decides: How are procedures written and matured?
Rows: L448-L450 (3)
Positions in the evidence (no verdict):
- P1 Versioned step-by-step runbooks with owner, tools, permissions, escalation, validated by another team member (L448); mature text toward scripts and auto-remediation starting with short, frequent, low-risk ones (L449, single vendor); separate playbooks (investigate) from runbooks (mitigate), linked from the alert (L450).
Forces in tension: repeatability, speed of repair
Context: TEAM_SIZE, SCALE

#### OPERATION.RUNBOOKS.2 Exercising Recovery

Decides: Are recovery procedures exercised under realistic conditions?
Rows: L451 (1)
Positions in the evidence (no verdict):
- P1 Exercise manual runbooks, failover and failback, tabletop exercises, and turn gaps into tests (L451).
Forces in tension: recoverability, confidence
Context: CRITICALITY, REGULATION
Realizes: ASSURANCE.AVAILABILITY

#### OPERATION.FEEDBACK Feedback into Development

Decides: Which production measures return to the team that ships?
Rows: L208 (1)
Positions in the evidence (no verdict):
- P1 Track failed deployment recovery time and change fail rate per service, shared across development and operations, never as targets; DORA warns targets invite gaming (L208).
Forces in tension: improvement without gaming
Context: TEAM_SIZE
Realizes: CHANGE_FLOW.MEASURE

### Branch TRANSVERSE

#### TRANSVERSE Transverse Practice

Decides: Which practices cut across every branch: documentation authoring, security practice, configuration and secrets, development environments. Decisions on how each is guaranteed sit in ASSURANCE.
Rows: -
Context: TEAM_SIZE, REGULATION, DISTRIBUTION

#### TRANSVERSE.DOCS Documentation Practice

Decides: How is documentation structured, written and budgeted? Carries out ASSURANCE.DOCS_SYNC.
Rows: -
Context: see children

#### TRANSVERSE.DOCS.1 Taxonomy, Size and Structure

Decides: How is documentation divided and organised for the reader?
Rows: L233, L234, L321, L322 (4)
Positions in the evidence (no verdict):
- P1 No competing position recorded: small modular documents (L233); organised by reader need (tutorial, how-to, reference, explanation) and improved in small increments (L234); a router set of guidelines with an index by role and situation and size-capped modules (L321, maintainer); layered detail and diagrams at three zoom levels (L322, maintainer).
Forces in tension: reader confidence, updateability
Context: TEAM_SIZE, DISTRIBUTION
Realizes: ASSURANCE.DOCS_SYNC

#### TRANSVERSE.DOCS.2 How Much to Document and the Budget

Decides: How much is documented, and is upkeep budgeted?
Rows: L231, L236 (2)
Positions in the evidence (no verdict):
- P1 Minimal, conversation first; P2 living documentation generated from code and tests; P3 full docs-as-code with owners and gates (L236).
- P4 Invest in documentation quality as a delivery capability and budget upkeep (L231; one research programme).
Forces in tension: cost of ownership, correctness, delivery speed
Context: TEAM_SIZE, LIFETIME, DISTRIBUTION
Realizes: ASSURANCE.DOCS_SYNC

#### TRANSVERSE.DOCS.3 Decision Records

Decides: How are decisions and their rationale kept?
Rows: L232, L324 (2)
Positions in the evidence (no verdict):
- P1 Immutable numbered records with status, a changed decision a new record, against mutable living documents kept current by CI and ownership; to be assigned per document type (L232).
- P2 A decision record states the costs it accepts as the other half of the decision (L324, maintainer).
Forces in tension: history is never wrong, rationale durability
Context: LIFETIME, TEAM_SIZE
Realizes: OWNERSHIP.SELECTION.1

#### TRANSVERSE.DOCS.4 Changelog

Decides: What tells a user what changed?
Rows: L235 (1)
Positions in the evidence (no verdict):
- P1 Human-written changelog per release grouped by change type with an Unreleased section (L235); no competing position recorded.
Forces in tension: reader confidence
Context: DISTRIBUTION

#### TRANSVERSE.DOCS.5 Prose Style Rules

Decides: Is editorial style checked by machine?
Rows: L225 (1)
Positions in the evidence (no verdict):
- P1 Style encoded as CI rules with error severity failing the build (consistency across many authors), against human writing review (clarity and audience cannot be linted); the linter targets consistency, not correctness (L225).
Forces in tension: consistency, quality, friction
Context: TEAM_SIZE

#### TRANSVERSE.DOCS.6 How Guidelines Are Authored

Decides: Are guidelines induced from observed practice or deduced from principles?
Rows: L323 (1)
Positions in the evidence (no verdict):
- P1 Induced from analysis of real production code and updated as practice evolves (mature codebase), against deduced from principles first (maintainer's philosophy asks for structure before implementation); internal tension recorded (L323).
Forces in tension: cost of ownership, correctness, consistency
Context: LIFETIME

#### TRANSVERSE.SECURITY Security Practice

Decides: How is secure development organised across the lifecycle? Carries out ASSURANCE.SECURITY.
Rows: -
Context: see children

#### TRANSVERSE.SECURITY.1 Responsibility and Training

Decides: Who owns security, and how are people trained?
Rows: L249 (1)
Positions in the evidence (no verdict):
- P1 Explicit, top-owned responsibility: roles defined, role-based training, management commitment, producer ownership of customer security outcomes (L249); no competing position recorded.
Forces in tension: ownership
Context: TEAM_SIZE, REGULATION
Realizes: ASSURANCE.SECURITY

#### TRANSVERSE.SECURITY.2 Framework and Requirements Catalogue

Decides: Which published framework and requirements list anchor the practice?
Rows: L240, L250 (2)
Positions in the evidence (no verdict):
- P1 Anchor practice in a published framework (NIST SSDF, OWASP SAMM) as a list of outcomes, not tool prescriptions (L240); a verifiable requirements catalogue (ASVS for web applications; other platforms have equivalents not read) as requirements list and test basis (L250).
Forces in tension: coverage, testability
Context: REGULATION, DISTRIBUTION, PLATFORM
Realizes: ASSURANCE.SECURITY.2
Stack pointers: L250 (web applications (ASVS); other platforms have eq...)

#### TRANSVERSE.SECURITY.3 Threat Modelling Practice

Decides: How and how often is risk modelled?
Rows: L241, L242 (2)
Positions in the evidence (no verdict):
- P1 Continuous, lightweight, per iteration (Threat Modeling Manifesto), against deeper risk-triggered assessment for high-risk areas only (SSDF) (L241).
- P2 Four questions: what are we working on, what can go wrong, what do we do about it, did we do a good enough job; track risks and mitigations (L242).
Forces in tension: correctness over time, cost of ownership
Context: CRITICALITY, EXPOSURE, TEAM_SIZE
Realizes: ASSURANCE.SECURITY.1

#### TRANSVERSE.SECURITY.4 Vulnerability Response Loop

Decides: How are vulnerabilities identified, remediated and learned from?
Rows: L253 (1)
Positions in the evidence (no verdict):
- P1 Identify and confirm (monitoring databases and reports, disclosure policy), assess, prioritise, remediate, analyse root causes (L253); no competing position recorded.
Forces in tension: security, learning
Context: EXPOSURE, REGULATION
Realizes: OWNERSHIP.LIFECYCLE.6

#### TRANSVERSE.SECURITY.5 Hardening the Toolchain

Decides: How are development endpoints and toolchain hardened?
Rows: L264 (1)
Positions in the evidence (no verdict):
- P1 Approved hardening guides, least functionality and privilege, continuous posture monitoring (L264); no competing position recorded.
Forces in tension: security
Context: EXPOSURE, CRITICALITY
Realizes: OWNERSHIP.SERVICES.6

#### TRANSVERSE.CONFIG Configuration and Secrets

Decides: How are configuration and secrets separated, delivered and protected?
Rows: -
Context: see children

#### TRANSVERSE.CONFIG.1 Configuration Apart from Code

Decides: What is configuration and where does it live?
Rows: L158, L261 (2)
Positions in the evidence (no verdict):
- P1 Strict separation from code and the deployable package: could the codebase be open-sourced at any moment without exposing credentials (L158, Twelve-Factor).
- P2 Configuration as code lives in a least-privilege repository with attributable changes; secrets stay out (L261).
Forces in tension: portability, security
Context: PLATFORM, REGULATION
Realizes: CHANGE_FLOW.BUILD

#### TRANSVERSE.CONFIG.2 Delivery of Configuration and Secrets

Decides: How do configuration and secrets reach the running software?
Rows: L254-L256 (3)
Positions in the evidence (no verdict):
- P1 Environment variables (simple, portable), against files or a store API for secrets (env vars leak to process listings and cannot be updated live) (L254).
- P2 Orthogonal granular values per deployment (many deploys), against named environment bundles (reviewable in one place, few fixed environments) (L255).
- P3 Keep secrets apart from non-secret configuration (L256).
Forces in tension: simplicity, security, live rotation, reviewability
Context: SCALE, PLATFORM, EXPOSURE
Realizes: ASSURANCE.SECURITY.5

#### TRANSVERSE.CONFIG.3 Secret Management

Decides: How are secrets stored, issued and rotated?
Rows: L257-L259 (3)
Positions in the evidence (no verdict):
- P1 Dynamic short-lived credentials with TTL (many services, high criticality), against static secrets rotated on a schedule (few services, low criticality) (L258).
- P2 One managed secrets solution with least privilege and lifecycle automation (L257); federated short-lived tokens (OIDC) for CI and deployment (L259).
Forces in tension: security, blast radius, infrastructure cost, cognitive load
Context: EXPOSURE, CRITICALITY, PLATFORM, SCALE
Realizes: ASSURANCE.SECURITY.5

#### TRANSVERSE.ENVIRONMENTS Development Environments

Decides: How are development and other environments defined and separated?
Rows: -
Context: see children

#### TRANSVERSE.ENVIRONMENTS.1 Development Environment as Code

Decides: Which mechanism defines the development environment and toolchain?
Rows: L262, L263 (2)
Positions in the evidence (no verdict):
- P1 Dev container (mixed-skill teams, cloud IDEs), P2 pinned package set such as Nix (byte-level reproducibility, learning cost), P3 dependency manifests only (single-language, no native dependencies) (L262).
- P4 Pin build tools and compilers, changed through change management that validates authenticity and integrity (L263).
Forces in tension: onboarding speed, reproducibility, cognitive load
Context: SKILLS, PLATFORM, TEAM_SIZE
Realizes: OWNERSHIP.LIFECYCLE.1
Stack pointers: L262 (tool-specific per option)

#### TRANSVERSE.ENVIRONMENTS.2 Separation of Environments

Decides: How are environments isolated from each other?
Rows: L260 (1)
Positions in the evidence (no verdict):
- P1 Development, build, test and production separated and protected, secrets isolated, non-production minimising production data (L260); no competing position recorded; parity position in CHANGE_FLOW.DEPLOY.2.
Forces in tension: security, isolation
Context: EXPOSURE, REGULATION
Realizes: CHANGE_FLOW.DEPLOY.2

#### TRANSVERSE.DESIGN Design Derivation (provisional)

Decides: In what order is a design derived before code? Placed here because no proposed branch holds design practice.
Rows: L329 (1)
Positions in the evidence (no verdict):
- P1 Design first (usage, data flow, schema, system design, implementation strategy, then code) against emergent design (maintainer; differs from test-first or emergent design) (L329).
Forces in tension: correctness, reversibility, speed of feedback
Context: CHANGE_COST, SYSTEM_SHAPE, SKILLS

