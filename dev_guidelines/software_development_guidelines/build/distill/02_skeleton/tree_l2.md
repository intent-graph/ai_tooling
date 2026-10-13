# Tree to level 2: ROOT, seven L1 branches, 53 L2 nodes

Cut top-down from each branch's role in `../target_hierarchy.md`, before any row was routed. Rows per node are the counts of `routing.md` (the script checks them). No default team context: context variables are for the next step and only where a row says they move the best practice (MD-02). No L3, no verdict, no positions.

UID rules (`PRIMER_01_SEMANTICS.md`, UID Format Convention): ROOT is exactly `ROOT`; L1 matches `^[A-Z][A-Z0-9_]*$`; L2 is `{L1}.{KEYWORD}` with a keyword of the same pattern; L3 and deeper (next step) are numeric suffixes only.

## ROOT

| uid | name | intent | rows |
|---|---|---|---|
| `ROOT` | Software Development Philosophy | A team delivers, and keeps delivering, a system that does what is intended, at a cost it can sustain. | - |

## OWNERSHIP Ownership

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `OWNERSHIP` | Ownership | Decision: for each capability, does the team write it, adopt it (a library or tool it runs) or rent it (an external service or API), and how is that choice kept reversible. | 133 | L1 branch |
| `OWNERSHIP.STANCE` | Necessity and Default Stance | Is the capability needed at all, and absent a specific reason is the default to write, adopt or rent; what a new layer or dependency must earn. | 12 |  |
| `OWNERSHIP.SELECTION` | Finding, Profiling and Selecting | How a candidate library, tool or technology is found, profiled and chosen, with how deep the vetting goes. | 39 |  |
| `OWNERSHIP.LIFECYCLE` | Dependency Lifecycle | How an adopted dependency is declared, locked, obtained, updated, inventoried and watched over its life. | 33 |  |
| `OWNERSHIP.CONTAINMENT` | Containment and Exit | How the effect of a dependency or an external system is bounded and how the team leaves it. | 13 |  |
| `OWNERSHIP.SERVICES` | External Services | What to require of a rented service or hosted tool: availability fit, API stability, switching terms, contract, vendor assessment. | 26 |  |
| `OWNERSHIP.LICENCE` | Licences | Which licence obligations a dependency brings and how the team classifies, decides and declares them. | 10 |  |

## ASSURANCE Assurance

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `ASSURANCE` | Assurance | Decision: for each property that must hold, which mechanism at which stage guarantees it, and runs on every change so that it stays true; the design was good, the testing was good, the review was trustworthy, what runs is what was reviewed. | 241 | L1 branch |
| `ASSURANCE.RULES` | Rules Common to Every Property | Where a check runs, what makes its signal trustworthy and fast, and what makes a review or a gate binding whoever authored the change. | 31 |  |
| `ASSURANCE.BEHAVIOUR` | Behaviour | Which tests, types and static checks, at which level and stage, guarantee that the software does what is intended. | 61 |  |
| `ASSURANCE.CONTRACTS` | Interfaces and Contracts | Which mechanism guarantees that an interface stays compatible for its consumers: contract tests, schema checks, one source of description. | 18 |  |
| `ASSURANCE.DATA_INTEGRITY` | Data Integrity Under Change | Which mechanism guarantees stored data stays valid and in sync through change, including the checks during a data change. | 19 | split topic data: guarantees here, procedures in CHANGE_FLOW.DATA_CHANGE |
| `ASSURANCE.DOCS_SYNC` | Documentation in Sync | Which mechanism keeps documentation true to the system: same-change delivery, gates, owners, executable examples, link checks. | 22 | split topic documentation: holds the content |
| `ASSURANCE.SECURITY` | Security | Which verification and enforcement mechanism, at which stage, guarantees security: design review, analysis, tests, scanning, enforced limits on automation. | 37 | split topic security: holds verification and enforcement |
| `ASSURANCE.PERFORMANCE` | Performance | Which tests, measurements and budgets guarantee that speed and capacity hold under the real workload. | 22 |  |
| `ASSURANCE.AVAILABILITY` | Availability and Recovery | Which design mechanisms and exercised procedures guarantee the system stays available under dependency failure and can be recovered. | 22 | split topic recovery: holds the proof (restore tests, exercises); practice in OPERATION.RECOVERY |
| `ASSURANCE.ARTIFACT` | Artifact Integrity | Which mechanism guarantees that what runs is what was reviewed and built from reviewed source. | 9 |  |

## CONSTRUCTION Construction

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `CONSTRUCTION` | Construction | Realization: how code is structured, in its language-neutral form, so that it is correct and stays changeable. | 87 | L1 branch |
| `CONSTRUCTION.DESIGN` | Design Derivation | How design is derived before code and where design effort is spent. | 5 |  |
| `CONSTRUCTION.SYSTEM_SHAPE` | System Shape | How the system is divided into deployable units and how that division follows teams and domain. | 10 |  |
| `CONSTRUCTION.HIDING` | Information Hiding and Modularity | How code is cut into modules so that each difficult or changing decision lives behind one boundary. | 11 |  |
| `CONSTRUCTION.BOUNDARY` | Boundary Contracts and Call Shape | What a boundary states and how a call is shaped: precise types, parsing at the edge, null versus absent, error contents. | 24 |  |
| `CONSTRUCTION.STATE` | State, Values and Load-Time Effects | Each fact held in one place, values that state their precision and mutability, modules without load-time effects. | 13 |  |
| `CONSTRUCTION.DEPENDENCY_DIRECTION` | Dependency Direction | Dependencies between modules flow one way, never in a cycle, under declared layering. | 3 |  |
| `CONSTRUCTION.NAMING` | Naming | How names are chosen so that a reader recovers the concept without the author. | 4 |  |
| `CONSTRUCTION.PARADIGM` | Paradigm and Placement of Logic | How the programming paradigm and the place of logic (application, database, scheduler) are chosen by intent. | 5 |  |
| `CONSTRUCTION.DATA_NOT_CODE` | Keeping Data From Becoming Code | How untrusted data is kept from being interpreted as code, query, path, destination or object. | 9 |  |
| `CONSTRUCTION.PROCESS` | Process Lifecycle | How a process starts, stops, fails and holds state so that it can be replaced and scaled. | 3 |  |

## CHANGE_FLOW Change Flow

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `CHANGE_FLOW` | Change Flow | Realization: how a change travels from version control to production and back: integration, review, build, release, deploy, rollback, data and schema change, measurement. | 117 | L1 branch |
| `CHANGE_FLOW.INTEGRATION` | Version Control and Integration | How work is held in version control and merged into one mainline: branching, merge method, mainline protection, commit practice, change attribution. | 18 |  |
| `CHANGE_FLOW.REVIEW` | Review | How review is carried out: mechanism per risk, size, speed, depth, what the reviewer reads. | 11 |  |
| `CHANGE_FLOW.BUILD` | Build and Pipeline | How the build is scripted, hermetic and visible, and what runs on every push. | 5 |  |
| `CHANGE_FLOW.RELEASE` | Release | How a build becomes a release: cadence, versioning, flags, staged pipeline, who may release. | 10 |  |
| `CHANGE_FLOW.DEPLOY` | Deployment | How a release reaches production: automation, rollout strategy, environment parity, instance replacement. | 10 |  |
| `CHANGE_FLOW.ROLLBACK` | Rollback | How a change is undone: decision to roll back, backward compatibility, reversible by version control. | 6 |  |
| `CHANGE_FLOW.DATA_CHANGE` | Data and Schema Change | How schema, data and bulk changes are written, ordered, rehearsed, run and watched. | 52 | split topic data: holds the procedures; guarantees in ASSURANCE.DATA_INTEGRITY |
| `CHANGE_FLOW.MEASURE` | Measuring Delivery | How delivery is measured and which outcomes judge it. | 5 |  |

## OPERATION Operation

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `OPERATION` | Operation | Realization: how the running system is kept within its reliability targets and recovered when it fails. | 109 | L1 branch |
| `OPERATION.RELIABILITY` | Reliability Targets | How reliability is defined and traded against release speed: indicators, objectives, error budget. | 12 |  |
| `OPERATION.ALERTING` | Alerting | When a human is paged and how alerts are built. | 6 |  |
| `OPERATION.TELEMETRY` | Telemetry | What is measured, logged and traced, how it is correlated, and what it costs. | 36 |  |
| `OPERATION.INCIDENTS` | Incidents | How an incident is declared, run and learned from, and how on-call load is bounded. | 9 |  |
| `OPERATION.CAPACITY` | Capacity | How capacity is planned, headroom decided and storage health kept. | 7 |  |
| `OPERATION.READINESS` | Operational Readiness | What must hold before a workload is launched and how that review is kept current. | 5 |  |
| `OPERATION.RUNBOOKS` | Runbooks and Playbooks | How operating procedures are written, owned, validated and automated. | 3 |  |
| `OPERATION.RECOVERY` | Backup, Restore and Disaster Recovery | How backups are designed and protected, objectives set, strategy chosen and failover and failback carried out. | 30 | split topic recovery: holds the practice; proof in ASSURANCE.AVAILABILITY |
| `OPERATION.FEEDBACK` | Feedback into Development | How production signals about delivery return to the people who change the system. | 1 |  |

## EVOLUTION Evolution

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `EVOLUTION` | Evolution | Realization over time: how the system and its decisions change: records, incremental change, debt, decommissioning, a small set of technologies. | 53 | L1 branch |
| `EVOLUTION.DECISIONS` | Decision Records | How decisions and their reasons are recorded, kept and revisited. | 12 |  |
| `EVOLUTION.INCREMENTAL` | Incremental Change | How change is made in steps that keep the system working, including migrations and replacement. | 11 |  |
| `EVOLUTION.DEBT` | Technical Debt and Refactoring | What counts as debt, when to take and repay it, and how to refactor. | 13 |  |
| `EVOLUTION.DECOMMISSION` | Decommissioning | How code, interfaces and systems are deprecated, switched off and removed. | 11 |  |
| `EVOLUTION.TECHNOLOGY` | Keeping Technologies Few | How the set of technologies in use is kept small and its standing positions recorded. | 6 |  |

## TRANSVERSE Transverse

| uid | name | intent | rows | note |
|---|---|---|---|---|
| `TRANSVERSE` | Transverse | Practices that cut across every branch: documentation, security, privacy, configuration and secrets, development environments. | 74 | L1 branch |
| `TRANSVERSE.DOCS` | Documentation Practice | How documentation is organised, written and budgeted. | 10 | split topic documentation: index of ASSURANCE.DOCS_SYNC plus authoring practice |
| `TRANSVERSE.SECURITY` | Security Practice | How a security programme is anchored, risk modelled, responsibility owned and vulnerabilities handled. | 14 | split topic security: index of ASSURANCE.SECURITY plus programme practice |
| `TRANSVERSE.SECURITY_MONITORING` | Security Monitoring and Audit Trail | What security-relevant events are logged, protected, detected and kept as an audit trail. | 17 |  |
| `TRANSVERSE.PRIVACY` | Privacy and Retention | How personal data is minimised, classified, retained and erased. | 14 |  |
| `TRANSVERSE.CONFIG` | Configuration and Secrets | How configuration and secrets reach the running software and are kept apart from code. | 16 |  |
| `TRANSVERSE.ENVIRONMENTS` | Development Environments | How development, build and test environments are defined, separated and hardened. | 3 |  |

## Split topics (MD-03)

A topic that spans a decision node and a realization node is stated once. The decision node holds which mechanism guarantees the property; the realization node holds how the practice is carried out; the one that holds less is mostly an index (a one-line intent and links, no restated content). Rows are routed to exactly one of the two; where one fact could sit in both, the content holder below takes it.

| topic | decision node | realization node | holds the content | is the index |
|---|---|---|---|---|
| documentation | ASSURANCE.DOCS_SYNC | TRANSVERSE.DOCS | ASSURANCE.DOCS_SYNC (mechanisms, gates, owners, executable examples) | TRANSVERSE.DOCS (keeps only authoring and organisation practice) |
| security | ASSURANCE.SECURITY | TRANSVERSE.SECURITY, TRANSVERSE.SECURITY_MONITORING, TRANSVERSE.PRIVACY | ASSURANCE.SECURITY (verification, enforcement) and, for logging, detection and retention, the two TRANSVERSE nodes that have no assurance counterpart | TRANSVERSE.SECURITY (programme practice; links the verification mechanisms) |
| data and schema change | ASSURANCE.DATA_INTEGRITY | CHANGE_FLOW.DATA_CHANGE | CHANGE_FLOW.DATA_CHANGE (procedures, batching, rehearsal) | ASSURANCE.DATA_INTEGRITY (holds the which-mechanism rows: integrity placement, derived-data sync, audits; links the procedures) |
| availability and recovery | ASSURANCE.AVAILABILITY | OPERATION.RECOVERY | OPERATION.RECOVERY (backup, objectives, strategy, failover) | ASSURANCE.AVAILABILITY (holds the proof: restore tests and exercises; links the practice) |

The realization branches (CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE) carry out what OWNERSHIP and ASSURANCE decide and link back to the decision node; they do not re-decide it.

