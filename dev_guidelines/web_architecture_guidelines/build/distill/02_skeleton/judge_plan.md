# Judge plan: units, order and reading lists

The judges choose, node by node, the most demanding practice that best serves the node's purpose (the max rule and the judge record of `../target_hierarchy.md`: positions, forces, decision, rejected). They judge on `skeleton.md` (this folder) and read the ledger rows listed here in full from `claims_ledger.md`; sources resolve through `sources.md`. MAINT rows (source MAINT-S01) weigh as a strong position, not an automatic winner. `undecided` is kept for genuine trade-offs between forces the node serves; those go to the maintainer.

Pinned:
- Units: 9. Order: J1 (ALLOCATION) first; then J2 to J5 (philosophy DATA, LOGIC, INTERACTION, TRANSVERSE) in parallel; then J6 to J9 (pig-web-defaults, same branches) in parallel, each after its philosophy counterpart.
- Units by size (nodes, rows owned): J1 47, 101; J2 5, 12; J3 8, 28; J4 12, 28; J5 14, 44; J6 36, 138; J7 31, 133; J8 28, 88; J9 28, 116. No unit exceeds 60 nodes, so none is split.

## Order

1. J1 ALLOCATION, both graphs: the placements decide which tier does what; every tier unit reads their verdicts. Inside J1, judge FORCES, CONTEXT and RULES first, then the five families, then the 7 PIG-WEB placements against their stack-neutral counterparts.
2. J2 to J5, the philosophy tier branches and TRANSVERSE, in parallel: each reads the J1 verdicts of the placements its nodes link to.
3. J6 to J9, the pig-web-defaults branches, in parallel: each reads the J1 verdicts it links to and the verdicts of the philosophy nodes it refines.

## Units

### J1 ALLOCATION, both graphs

Nodes (47): ALLOCATION Allocation of Responsibilities; ALLOCATION.FORCES Allocation Forces; ALLOCATION.FORCES.1 Correctness; ALLOCATION.FORCES.2 Security; ALLOCATION.FORCES.3 Performance; ALLOCATION.FORCES.4 Latency; ALLOCATION.FORCES.5 Scalability; ALLOCATION.FORCES.6 Changeability; ALLOCATION.CONTEXT Allocation Context; ALLOCATION.RULES Allocation Rules; ALLOCATION.RULES.1 Authority and Copies; ALLOCATION.RULES.2 End-to-End Placement; ALLOCATION.RULES.3 Trust Boundary; ALLOCATION.RULES.4 One Core for Every Client; ALLOCATION.RULES.5 Atomicity Ends at the Transaction; ALLOCATION.RECORD Data Authority Placements; ALLOCATION.RECORD.1 System of Record; ALLOCATION.RECORD.2 Data Access Interface; ALLOCATION.RECORD.3 Type and Contract Definitions; ALLOCATION.GUARD Guarding Placements; ALLOCATION.GUARD.1 Validation; ALLOCATION.GUARD.2 Invariants; ALLOCATION.GUARD.3 Authorization; ALLOCATION.GUARD.4 Identity and Session State; ALLOCATION.GUARD.5 Concurrency Control and Conflict Resolution; ALLOCATION.GUARD.6 Duplicate Suppression; ALLOCATION.ACT Acting Placements; ALLOCATION.ACT.1 Business Rules and State Transitions; ALLOCATION.ACT.2 Side Effects and Integrations; ALLOCATION.ACT.3 Deferred and Scheduled Work; ALLOCATION.ACT.4 Audit and History; ALLOCATION.DERIVE Derivation Placements; ALLOCATION.DERIVE.1 Derived Data and Aggregation; ALLOCATION.DERIVE.2 Filtering, Sorting, Paging and Search; ALLOCATION.DERIVE.3 Caching; ALLOCATION.PRESENT Presentation Placements; ALLOCATION.PRESENT.1 Rendering; ALLOCATION.PRESENT.2 Formatting and Localization; ALLOCATION.PRESENT.3 UI and Ephemeral State; PIG-WEB.ALLOCATION Stack Allocation; PIG-WEB.ALLOCATION.POSTGRES_FIRST Postgres First for Backing Roles; PIG-WEB.ALLOCATION.DB_API Database Function API; PIG-WEB.ALLOCATION.TYPE_CHAIN Type Definition Chain; PIG-WEB.ALLOCATION.ROW_SECURITY Row Security Placement; PIG-WEB.ALLOCATION.JOB_HOST Job and Schedule Host; PIG-WEB.ALLOCATION.CACHE_STORE Cache Store; PIG-WEB.ALLOCATION.JS_SERVER JavaScript Server Tier.

Rows owned, read in full (101): L012, L013, L016, L019, L020, L022, L040-L042, L044, L045, L049, L051, L066, L070-L072, L097, L125-L127, L187, L214, L215, L252-L255, L272, L281, L288, L302, L313-L316, L318-L321, L406, L417, L468, L471-L473, L475, L477-L482, L484, L486, L515, L518, L527, L528, L534, L548, L549, L582, L584, L596, L601, L604, L606-L613, L615-L633, L644, L658, L674, L678, L681, L684, L688.

Rows owned elsewhere that the placement records cite, also read in full (73): L003, L010, L086, L128, L176, L208, L212, L226, L233, L234, L237, L246, L260, L265, L266, L269-L271, L285, L290-L292, L297, L305, L306, L310, L311, L392, L407-L410, L413-L416, L419, L420, L457, L474, L485, L488, L495, L516, L517, L532, L535, L536, L541, L545, L546, L553, L555, L556, L566, L568, L570, L587-L590, L599, L600, L602, L605, L614, L634, L650, L655, L659, L677, L679, L680.

Output: one judge record per node; for each placement also the authority tier, permitted copies, forbidden tiers and the context that would move it (`../target_hierarchy.md`, placements).

### J2 web-app-philosophy DATA

Nodes (5): DATA Durable Data; DATA.ORGANIZE Organized Facts; DATA.GUARD Guarded Consistency; DATA.MAINTAIN Maintained Over Time; DATA.DERIVE Derived, Not Stored.

Rows owned, read in full (12): L037-L039, L043, L046, L047, L469, L470, L474, L476, L485, L488.

Verdicts to read first (5): ALLOCATION.RECORD.1, ALLOCATION.RECORD.3, ALLOCATION.GUARD.2, ALLOCATION.GUARD.5, ALLOCATION.DERIVE.1.

### J3 web-app-philosophy LOGIC

Nodes (8): LOGIC Business Logic Tier; LOGIC.SECURE Secured Entry; LOGIC.ENFORCE Business Core; LOGIC.PROCESS Processing Model; LOGIC.EXPOSE Backend Interface; LOGIC.EXPOSE.1 Protocol Semantics; LOGIC.EXPOSE.2 Self-Contained Requests; LOGIC.EXPOSE.3 Hypermedia Controls.

Rows owned, read in full (28): L021, L023, L031-L034, L050, L052-L055, L059-L065, L067, L086-L094.

Verdicts to read first (8): ALLOCATION.RULES.4, ALLOCATION.RECORD.2, ALLOCATION.GUARD.1, ALLOCATION.GUARD.3, ALLOCATION.GUARD.4, ALLOCATION.GUARD.6, ALLOCATION.ACT.1, ALLOCATION.DERIVE.3.

### J4 web-app-philosophy INTERACTION

Nodes (12): INTERACTION Interaction; INTERACTION.VISUALIZE Perceivable Interface; INTERACTION.COLLABORATE Collaboration on Data; INTERACTION.AGENT Agent Access; INTERACTION.ENVIRONMENT Web Environment; INTERACTION.ENVIRONMENT.1 Uncontrolled Client Runtime; INTERACTION.ENVIRONMENT.2 Unstable Page Lifecycle; INTERACTION.ENVIRONMENT.3 Non-Atomic Deployment; INTERACTION.ENVIRONMENT.4 Caches Beyond Reach; INTERACTION.ENVIRONMENT.5 Unreliable Network; INTERACTION.ENVIRONMENT.6 URL as Public Interface; INTERACTION.ENVIRONMENT.7 Hostile Page Script.

Rows owned, read in full (28): L002-L011, L014, L017, L018, L024-L028, L435, L640, L642, L645, L648, L652, L664, L682, L686, L687.

Verdicts to read first (11): ALLOCATION.RULES.3, ALLOCATION.RULES.4, ALLOCATION.GUARD.3, ALLOCATION.GUARD.5, ALLOCATION.GUARD.6, ALLOCATION.ACT.4, ALLOCATION.DERIVE.3, ALLOCATION.PRESENT.1, ALLOCATION.PRESENT.2, ALLOCATION.PRESENT.3, TRANSVERSE.CONTRACTS.

### J5 web-app-philosophy TRANSVERSE

Nodes (14): TRANSVERSE Transverse Concerns; TRANSVERSE.SECURITY Security Across Tiers; TRANSVERSE.PERFORMANCE Measured Performance; TRANSVERSE.CONTRACTS Standards and Contracts; TRANSVERSE.OPERABILITY Operability; TRANSVERSE.OPERABILITY.1 Whole-Path Observability; TRANSVERSE.OPERABILITY.2 Proportioned Testing; TRANSVERSE.OPERABILITY.3 Reproducible Delivery; TRANSVERSE.EVOLUTION Deliberate Evolution; TRANSVERSE.EVOLUTION.1 Explicit Decisions; TRANSVERSE.EVOLUTION.2 Incremental Change; TRANSVERSE.EVOLUTION.3 Deployable Boundaries; TRANSVERSE.EVOLUTION.4 Few Mature Technologies; TRANSVERSE.EVOLUTION.5 Team-Shaped Structure.

Rows owned, read in full (44): L015, L029, L030, L035, L036, L048, L056-L058, L068, L069, L073-L085, L095, L096, L098-L112, L303, L483, L487.

Verdicts to read first (5): ALLOCATION.FORCES.3, ALLOCATION.FORCES.4, ALLOCATION.RULES.3, ALLOCATION.RECORD.3, ALLOCATION.ACT.4.

### J6 pig-web-defaults PIG-WEB.DATA

Nodes (36): PIG-WEB.DATA Postgres Data Tier; PIG-WEB.DATA.ORGANIZE Schema Organization; PIG-WEB.DATA.ORGANIZE.1 Tables and Normalization; PIG-WEB.DATA.ORGANIZE.2 Keys; PIG-WEB.DATA.ORGANIZE.3 Column Types; PIG-WEB.DATA.ORGANIZE.4 Naming; PIG-WEB.DATA.ORGANIZE.5 JSON Documents; PIG-WEB.DATA.ORGANIZE.6 Schemas and Tenancy; PIG-WEB.DATA.ORGANIZE.7 Indexes; PIG-WEB.DATA.GUARD Declared Integrity; PIG-WEB.DATA.GUARD.1 Constraints; PIG-WEB.DATA.GUARD.2 Roles and Privileges; PIG-WEB.DATA.GUARD.3 Row Security Policies; PIG-WEB.DATA.GUARD.4 Triggers; PIG-WEB.DATA.CONCURRENCY Concurrency Mechanics; PIG-WEB.DATA.CONCURRENCY.1 Default Concurrency Strategy; PIG-WEB.DATA.CONCURRENCY.2 Isolation Mechanics; PIG-WEB.DATA.CONCURRENCY.3 Locks; PIG-WEB.DATA.CONCURRENCY.4 Atomic Statements; PIG-WEB.DATA.CONCURRENCY.5 Sequences and Commit Order; PIG-WEB.DATA.CONCURRENCY.6 State Transition Order; PIG-WEB.DATA.MAINTAIN Data Maintenance; PIG-WEB.DATA.MAINTAIN.1 Migrations; PIG-WEB.DATA.MAINTAIN.2 Deletion, Retention and Partitioning; PIG-WEB.DATA.MAINTAIN.3 History Tables; PIG-WEB.DATA.MAINTAIN.4 Bulk Data Jobs; PIG-WEB.DATA.MAINTAIN.5 Backup and Recovery; PIG-WEB.DATA.MAINTAIN.6 Personal Data Erasure [deferred]; PIG-WEB.DATA.MAINTAIN.7 High Availability and Replication [deferred]; PIG-WEB.DATA.DERIVE Derived Data in Postgres; PIG-WEB.DATA.DERIVE.1 Denormalization and Sync; PIG-WEB.DATA.DERIVE.2 Cache Tables; PIG-WEB.DATA.DERIVE.3 Search [deferred]; PIG-WEB.DATA.INTERFACE Database Interface; PIG-WEB.DATA.INTERFACE.1 Functions and Views; PIG-WEB.DATA.INTERFACE.2 Connections and Pooling.

Rows owned, read in full (138): L128, L168-L186, L188-L213, L216-L223, L309-L311, L420, L489-L514, L516, L517, L519-L526, L529-L533, L535-L545, L566, L568-L581, L585-L588, L591-L595, L597, L598, L676, L685.

Verdicts to read first (16): ALLOCATION.GUARD.2, ALLOCATION.GUARD.5, ALLOCATION.GUARD.6, ALLOCATION.ACT.1, ALLOCATION.ACT.3, ALLOCATION.ACT.4, ALLOCATION.DERIVE.1, DATA, DATA.ORGANIZE, DATA.GUARD, DATA.MAINTAIN, DATA.DERIVE, PIG-WEB.ALLOCATION.DB_API, PIG-WEB.ALLOCATION.TYPE_CHAIN, PIG-WEB.ALLOCATION.ROW_SECURITY, PIG-WEB.ALLOCATION.CACHE_STORE.

### J7 pig-web-defaults PIG-WEB.LOGIC

Nodes (31): PIG-WEB.LOGIC Python Application Tier; PIG-WEB.LOGIC.SECURE Backend Security; PIG-WEB.LOGIC.SECURE.1 Access Control Enforcement; PIG-WEB.LOGIC.SECURE.2 Sessions; PIG-WEB.LOGIC.SECURE.3 CSRF Defense; PIG-WEB.LOGIC.SECURE.4 Federated Login and Tokens; PIG-WEB.LOGIC.SECURE.5 Passwords and Login Throttling; PIG-WEB.LOGIC.SECURE.6 Abuse and Rate Limits; PIG-WEB.LOGIC.SECURE.7 Server-Side Fetch; PIG-WEB.LOGIC.ENFORCE Business Logic Realization; PIG-WEB.LOGIC.ENFORCE.1 Use-Case Layer; PIG-WEB.LOGIC.ENFORCE.2 Transactions; PIG-WEB.LOGIC.ENFORCE.3 Data Access; PIG-WEB.LOGIC.ENFORCE.4 Concurrency Model; PIG-WEB.LOGIC.ENFORCE.5 Framework Choice; PIG-WEB.LOGIC.PROCESS Processing and Side Effects; PIG-WEB.LOGIC.PROCESS.1 Background and Scheduled Jobs; PIG-WEB.LOGIC.PROCESS.2 Side Effects and Delivery; PIG-WEB.LOGIC.PROCESS.3 Resilience; PIG-WEB.LOGIC.PROCESS.4 File Upload Path; PIG-WEB.LOGIC.PROCESS.5 File Scanning and Storage; PIG-WEB.LOGIC.PROCESS.6 File Serving; PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery [deferred]; PIG-WEB.LOGIC.EXPOSE HTTP Interface; PIG-WEB.LOGIC.EXPOSE.1 Contract Style and Resources; PIG-WEB.LOGIC.EXPOSE.2 Status Codes and Errors; PIG-WEB.LOGIC.EXPOSE.3 Retries and Asynchronous Operations; PIG-WEB.LOGIC.EXPOSE.4 Response Caching; PIG-WEB.LOGIC.EXPOSE.5 Origin and CORS; PIG-WEB.LOGIC.EXPOSE.6 Payload Schemas; PIG-WEB.LOGIC.EXPOSE.7 API Evolution.

Rows owned, read in full (133): L224-L246, L256, L257, L259, L261-L271, L273-L280, L305-L308, L312, L317, L322-L333, L338-L349, L358-L368, L407-L416, L418, L419, L421-L434, L546, L547, L550-L558, L589, L590, L599, L600, L602, L603, L605, L614, L655, L662.

Verdicts to read first (16): ALLOCATION.GUARD.1, ALLOCATION.GUARD.4, ALLOCATION.GUARD.6, ALLOCATION.ACT.1, ALLOCATION.ACT.2, ALLOCATION.ACT.3, ALLOCATION.DERIVE.2, LOGIC, LOGIC.SECURE, LOGIC.ENFORCE, LOGIC.PROCESS, LOGIC.EXPOSE, PIG-WEB.ALLOCATION.TYPE_CHAIN, PIG-WEB.ALLOCATION.ROW_SECURITY, PIG-WEB.ALLOCATION.JOB_HOST, PIG-WEB.ALLOCATION.CACHE_STORE.

### J8 pig-web-defaults PIG-WEB.INTERACTION

Nodes (28): PIG-WEB.INTERACTION Browser and Agent Surface; PIG-WEB.INTERACTION.VISUALIZE Browser Rendering; PIG-WEB.INTERACTION.VISUALIZE.1 Rendering Technique; PIG-WEB.INTERACTION.VISUALIZE.2 Client State; PIG-WEB.INTERACTION.VISUALIZE.3 Page Performance; PIG-WEB.INTERACTION.VISUALIZE.4 Accessibility; PIG-WEB.INTERACTION.EDIT Editing Without Loss; PIG-WEB.INTERACTION.REALTIME Real-Time Channels; PIG-WEB.INTERACTION.REALTIME.1 Channel Choice; PIG-WEB.INTERACTION.REALTIME.2 Channel Operation; PIG-WEB.INTERACTION.REALTIME.3 Long-Lived Connection Servers; PIG-WEB.INTERACTION.REALTIME.4 Channel Security; PIG-WEB.INTERACTION.REALTIME.5 Database Notifications; PIG-WEB.INTERACTION.COLLABORATE Comments and Collaboration; PIG-WEB.INTERACTION.COLLABORATE.1 Comment Anchoring; PIG-WEB.INTERACTION.COLLABORATE.2 Threads and Comment Lifecycle; PIG-WEB.INTERACTION.COLLABORATE.3 Collaborative Text Editing; PIG-WEB.INTERACTION.COLLABORATE.4 Notifications and Moderation; PIG-WEB.INTERACTION.AGENT Agent Surface; PIG-WEB.INTERACTION.AGENT.1 Surface and Protocol; PIG-WEB.INTERACTION.AGENT.2 Discovery and Registration; PIG-WEB.INTERACTION.AGENT.3 Identity and Delegation; PIG-WEB.INTERACTION.AGENT.4 Approval and Injection Defense; PIG-WEB.INTERACTION.AGENT.5 Agent-Shaped Responses and Limits; PIG-WEB.INTERACTION.ENVIRONMENT Browser Environment; PIG-WEB.INTERACTION.ENVIRONMENT.1 Capability and Page Lifecycle; PIG-WEB.INTERACTION.ENVIRONMENT.2 Offline and Installable Apps [deferred]; PIG-WEB.INTERACTION.ENVIRONMENT.3 Internationalization [deferred].

Rows owned, read in full (88): L258, L260, L282-L287, L289-L294, L297-L301, L436-L467, L583, L634-L639, L641, L643, L646, L647, L649-L651, L653, L654, L656, L657, L659-L661, L663, L665-L673, L675, L677, L679, L680, L683, L689.

Verdicts to read first (15): ALLOCATION.RECORD.1, ALLOCATION.GUARD.3, ALLOCATION.GUARD.4, ALLOCATION.GUARD.5, ALLOCATION.GUARD.6, ALLOCATION.ACT.2, ALLOCATION.PRESENT.2, ALLOCATION.PRESENT.3, INTERACTION, INTERACTION.VISUALIZE, INTERACTION.COLLABORATE, INTERACTION.AGENT, INTERACTION.ENVIRONMENT, PIG-WEB.ALLOCATION.POSTGRES_FIRST, PIG-WEB.ALLOCATION.JS_SERVER.

### J9 pig-web-defaults PIG-WEB.TRANSVERSE

Nodes (28): PIG-WEB.TRANSVERSE Transverse Defaults; PIG-WEB.TRANSVERSE.SECURITY Security Defaults; PIG-WEB.TRANSVERSE.SECURITY.1 Security Requirement Catalogue; PIG-WEB.TRANSVERSE.SECURITY.2 Transport Security; PIG-WEB.TRANSVERSE.SECURITY.3 Security Headers and CSP; PIG-WEB.TRANSVERSE.SECURITY.4 Secrets; PIG-WEB.TRANSVERSE.SECURITY.5 Supply Chain; PIG-WEB.TRANSVERSE.PERFORMANCE Page Experience Targets; PIG-WEB.TRANSVERSE.CONTRACTS Contract Verification and Meaning; PIG-WEB.TRANSVERSE.CONTRACTS.1 Contract Verification; PIG-WEB.TRANSVERSE.CONTRACTS.2 Contract Meaning and Ownership; PIG-WEB.TRANSVERSE.OPERABILITY Operations; PIG-WEB.TRANSVERSE.OPERABILITY.1 Tracing and Logs; PIG-WEB.TRANSVERSE.OPERABILITY.2 Client Telemetry; PIG-WEB.TRANSVERSE.OPERABILITY.3 Monitoring; PIG-WEB.TRANSVERSE.OPERABILITY.4 Security Event Log; PIG-WEB.TRANSVERSE.OPERABILITY.5 Testing; PIG-WEB.TRANSVERSE.OPERABILITY.6 Delivery and Configuration; PIG-WEB.TRANSVERSE.OPERABILITY.7 Incident Response [deferred]; PIG-WEB.TRANSVERSE.TOPOLOGY Runtime Topology; PIG-WEB.TRANSVERSE.TOPOLOGY.1 Reverse Proxy Edge; PIG-WEB.TRANSVERSE.TOPOLOGY.2 Application Server; PIG-WEB.TRANSVERSE.TOPOLOGY.3 Process Placement; PIG-WEB.TRANSVERSE.TOPOLOGY.4 Static Assets and CDN; PIG-WEB.TRANSVERSE.EVOLUTION Evolution Defaults; PIG-WEB.TRANSVERSE.EVOLUTION.1 Deployables; PIG-WEB.TRANSVERSE.EVOLUTION.2 Modular Monolith; PIG-WEB.TRANSVERSE.EVOLUTION.3 Decision Records.

Rows owned, read in full (116): L113-L124, L129-L167, L247-L251, L295, L296, L304, L334-L337, L350-L357, L369-L405, L559-L565, L567.

Verdicts to read first (9): ALLOCATION.ACT.4, LOGIC.PROCESS, TRANSVERSE, TRANSVERSE.SECURITY, TRANSVERSE.PERFORMANCE, TRANSVERSE.CONTRACTS, TRANSVERSE.OPERABILITY, TRANSVERSE.EVOLUTION, PIG-WEB.ALLOCATION.JS_SERVER.

## Judge record (reminder)

Per node: positions (ledger and source ids), forces each serves and at what cost, the max decision with grounds, each rejected position with its reason and the condition under which it would win. Nodes owning no row (roll-ups, the two forces without rows) are judged as the roll-up of their children or marked open. Deferred nodes are not judged.
