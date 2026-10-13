# Decisions of the intentlink completion

Every row of the nine `cross_links.md` lists (`J<n>-<k>`, the k-th row of unit J<n>'s list) and every existing link of the graph (`E<nnn>`, in graph order) has exactly one decision below. Types: realizes, requires, refines, conflicts, constrains, dataflow.

Rules applied:

- `realizes`: the source carries out a decision held by the target (the target decides what and why, the source how and where).
- `requires`: the source functions or holds only if the target's capability or rule exists.
- `refines`: the source specialises the target's rule to a narrower case.
- `constrains`: the source's rule bounds what the target may decide (arrow runs from the bounding rule to the bounded node, as in the sibling graph).
- `dataflow`: an output of the source is an input of the target.
- `conflicts`: two positions pull apart (the two existing ones kept).
- A pointer that only says where a topic is held, an analogy, a complementarity or a consistency note has no relation: dropped.
- One link per ordered pair; the inverse restatement of a kept link (same relation read from the other end) is merged into it.
- No link between a node and its ancestor or descendant (checked; none remain).
- An L1 branch endpoint is kept only where no finer link already lifts to it (lifted links are computed, never created by hand).
- A target is narrowed or an arrow reversed only where the record makes it unambiguous; each is listed in section 6.


## 1. Same ordered pair given by several rows (duplicates merged)

| pair | rows (type) | kept | why |
|---|---|---|---|
| ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.3 | J2-05 (realizes), J4-36 (see) | realizes (from J2-05) | stronger semantic type kept |
| ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.4 | J2-06 (realizes), J4-37 (see) | realizes (from J2-06) | stronger semantic type kept |
| ASSURANCE.AVAILABILITY.3 -> ASSURANCE.BEHAVIOUR.5 | J2-11 (see), J4-20 (requires) | requires (from J4-20) | stronger semantic type kept |
| ASSURANCE.AVAILABILITY.5 -> ASSURANCE.BEHAVIOUR.5 | J2-12 (see), J4-27 (see) | requires (from J4-27) | same type, one link kept |
| ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY | J3-07 (index), J7-28 (requires) | requires (from J7-28) | stronger semantic type kept |
| ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY.2 | J3-08 (see), J7-35 (related) | requires (from J7-35) | stronger semantic type kept |
| ASSURANCE.DATA_INTEGRITY.4 -> OPERATION.TELEMETRY.8 | J3-13 (requires), J7-08 (requires) | requires (from J3-13) | same type, one link kept |
| ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY | J4-01 (refines), J7-02 (refines) | refines (from J4-01) | same type, one link kept |
| ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.1 | J4-02 (see), J7-03 (related) | requires (from J4-02) | stronger semantic type kept |
| ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.2 | J4-03 (see), J7-04 (related) | requires (from J4-03) | stronger semantic type kept |
| ASSURANCE.PERFORMANCE.4 -> ASSURANCE.AVAILABILITY.3 | J2-15 (see), E003 (requires) | requires (from E003) | stronger semantic type kept |
| ASSURANCE.SECURITY.2 -> ASSURANCE.RULES.1 | J2-01 (requires), J3-32 (requires) | requires (from J2-01) | same type, one link kept |
| ASSURANCE.SECURITY.3 -> ASSURANCE.BEHAVIOUR.6 | J2-02 (see), J3-37 (see) | requires (from J2-02) | same type, one link kept |
| CHANGE_FLOW.BUILD -> ASSURANCE.ARTIFACT | J4-28 (realizes), J6-15 (realizes) | realizes (from J4-28) | same type, one link kept |
| CHANGE_FLOW.REVIEW.1 -> ASSURANCE.RULES.4 | J2-08 (see), J6-10 (related) | realizes (from J6-10) | stronger semantic type kept |
| CONSTRUCTION.BOUNDARY -> ASSURANCE.CONTRACTS | J2-26 (realizes), J5-25 (realizes) | realizes (from J2-26) | same type, one link kept |
| CONSTRUCTION.DESIGN -> OWNERSHIP.STANCE.4 | J1-02 (related), J5-07 (related) | realizes (from J1-02) | same type, one link kept |
| CONSTRUCTION.PARADIGM.2 -> OPERATION.TELEMETRY.8 | J5-51 (related), J7-09 (requires) | requires (from J7-09) | stronger semantic type kept |
| EVOLUTION.DECOMMISSION.3 -> OWNERSHIP.SERVICES.2 | J1-12 (related), J8-44 (see) | dataflow (from J8-44) | stronger semantic type kept |
| EVOLUTION.DECOMMISSION.4 -> ASSURANCE.CONTRACTS.1 | J2-23 (see), J8-45 (realizes) | realizes (from J8-45) | stronger semantic type kept |
| EVOLUTION.DECOMMISSION.5 -> OWNERSHIP.SERVICES.2 | J1-13 (related), J8-47 (see) | dataflow (from J8-47) | stronger semantic type kept |
| EVOLUTION.DECOMMISSION.6 -> OPERATION.RECOVERY.2 | J7-36 (related), J8-48 (see) | constrains (from J7-36) | stronger semantic type kept |
| OWNERSHIP.SERVICES.2 -> ASSURANCE.CONTRACTS.1 | J1-10 (related), J2-22 (see) | requires (from J2-22) | stronger semantic type kept |

## 2. Existing links retyped or reworded (same pair)

| id | pair | type | change |
|---|---|---|---|
| E004 | ASSURANCE.PERFORMANCE.2 -> ASSURANCE.PERFORMANCE.4 | see -> requires | retyped |
| E005 | ASSURANCE.AVAILABILITY.1 -> ASSURANCE.AVAILABILITY.2 | see -> requires | retyped |
| E006 | ASSURANCE.AVAILABILITY.1 -> ASSURANCE.AVAILABILITY.3 | see -> requires | retyped |
| E010 | ASSURANCE.DATA_INTEGRITY.5 -> ASSURANCE.DATA_INTEGRITY.3 | see -> realizes | retyped |
| E014 | ASSURANCE.SECURITY.3 -> ASSURANCE.SECURITY.1 | see -> requires | retyped |
| E015 | ASSURANCE.SECURITY.3 -> ASSURANCE.SECURITY.4 | see -> requires | retyped |
| E020 | OWNERSHIP.STANCE.2 -> OWNERSHIP.SERVICES.3 | (none) -> requires | retyped |
| E021 | OWNERSHIP.STANCE.3 -> OWNERSHIP.STANCE.2 | (none) -> refines | retyped |
| E023 | OWNERSHIP.SELECTION.1 -> OWNERSHIP.STANCE.1 | (none) -> realizes | retyped |
| E024 | OWNERSHIP.SELECTION.2 -> OWNERSHIP.STANCE.1 | (none) -> refines | retyped |
| E025 | OWNERSHIP.SELECTION.3 -> OWNERSHIP.LIFECYCLE.2 | (none) -> dataflow | retyped |
| E026 | OWNERSHIP.SELECTION.5 -> OWNERSHIP.LIFECYCLE.4 | (none) -> requires | retyped |
| E027 | OWNERSHIP.SELECTION.5 -> OWNERSHIP.LIFECYCLE.5 | (none) -> dataflow | retyped |
| E029 | OWNERSHIP.LIFECYCLE.3 -> OWNERSHIP.LIFECYCLE.1 | (none) -> requires | retyped |
| E034 | OWNERSHIP.CONTAINMENT.2 -> OWNERSHIP.CONTAINMENT.1 | (none) -> realizes | retyped |
| E035 | OWNERSHIP.SERVICES.3 -> OWNERSHIP.CONTAINMENT.1 | (none) -> dataflow | retyped |
| E037 | OWNERSHIP.LICENCE.2 -> OWNERSHIP.LICENCE.1 | (none) -> requires | retyped |
| E039 | TRANSVERSE.SECURITY.2 -> TRANSVERSE.SECURITY.1 | see -> requires | retyped |
| E042 | TRANSVERSE.SECURITY.6 -> TRANSVERSE.SECURITY.5 | see -> dataflow | retyped |
| E043 | TRANSVERSE.SECURITY_MONITORING.3 -> TRANSVERSE.PRIVACY.1 | see -> requires | retyped |
| E045 | TRANSVERSE.SECURITY_MONITORING.5 -> TRANSVERSE.PRIVACY.3 | see -> constrains | retyped |
| E048 | TRANSVERSE.PRIVACY.2 -> TRANSVERSE.PRIVACY.1 | see -> requires | retyped |
| E050 | TRANSVERSE.PRIVACY.2 -> TRANSVERSE.CONFIG.4 | see -> constrains | retyped |
| E051 | TRANSVERSE.PRIVACY.3 -> TRANSVERSE.PRIVACY.2 | see -> requires | retyped |
| E055 | TRANSVERSE.CONFIG.1 -> TRANSVERSE.CONFIG.4 | see -> requires | retyped |
| E056 | TRANSVERSE.CONFIG.2 -> TRANSVERSE.CONFIG.1 | see -> requires | retyped |
| E057 | TRANSVERSE.CONFIG.2 -> TRANSVERSE.CONFIG.4 | see -> requires | retyped |
| E058 | TRANSVERSE.CONFIG.4 -> TRANSVERSE.SECURITY_MONITORING.2 | see -> requires | retyped |
| E060 | TRANSVERSE.CONFIG.5 -> TRANSVERSE.CONFIG.4 | see -> requires | retyped |
| E061 | TRANSVERSE.CONFIG.6 -> TRANSVERSE.CONFIG.4 | see -> requires | retyped |
| E062 | TRANSVERSE.CONFIG.6 -> TRANSVERSE.SECURITY.5 | see -> refines | retyped |
| E064 | CONSTRUCTION.DESIGN.2 -> CONSTRUCTION.SYSTEM_SHAPE.3 | related -> constrains | retyped |
| E066 | CONSTRUCTION.SYSTEM_SHAPE.1 -> CONSTRUCTION.SYSTEM_SHAPE.3 | related -> requires | retyped |
| E067 | CONSTRUCTION.SYSTEM_SHAPE.1 -> CONSTRUCTION.SYSTEM_SHAPE.2 | related -> requires | retyped |
| E068 | CONSTRUCTION.SYSTEM_SHAPE.1 -> CONSTRUCTION.HIDING.2 | related -> requires | retyped |
| E070 | CONSTRUCTION.SYSTEM_SHAPE.4 -> CONSTRUCTION.SYSTEM_SHAPE.1 | related -> constrains | retyped |
| E072 | CONSTRUCTION.HIDING -> CONSTRUCTION.DEPENDENCY_DIRECTION | related -> requires | retyped |
| E080 | CONSTRUCTION.HIDING.4 -> CONSTRUCTION.BOUNDARY.4 | related -> requires | retyped |
| E081 | CONSTRUCTION.BOUNDARY.1 -> CONSTRUCTION.BOUNDARY.2 | related -> requires | retyped |
| E082 | CONSTRUCTION.BOUNDARY.1 -> CONSTRUCTION.STATE.1 | related -> dataflow | retyped |
| E085 | CONSTRUCTION.BOUNDARY.3 -> CONSTRUCTION.STATE.1 | related -> refines | retyped |
| E086 | CONSTRUCTION.BOUNDARY.4 -> CONSTRUCTION.BOUNDARY.5 | related -> requires | retyped |
| E091 | CONSTRUCTION.STATE.3 -> CONSTRUCTION.STATE.1 | related -> refines | retyped |
| E094 | CONSTRUCTION.DEPENDENCY_DIRECTION.1 -> CONSTRUCTION.HIDING.1 | related -> refines | retyped |
| E095 | CONSTRUCTION.DEPENDENCY_DIRECTION.1 -> CONSTRUCTION.DEPENDENCY_DIRECTION.2 | related -> refines | retyped |
| E097 | CONSTRUCTION.NAMING.3 -> CONSTRUCTION.DESIGN.1 | related -> refines | retyped |
| E100 | CONSTRUCTION.PROCESS.1 -> CONSTRUCTION.PROCESS.3 | related -> requires | retyped |
| E101 | CONSTRUCTION.PROCESS.2 -> CONSTRUCTION.PROCESS.1 | related -> requires | retyped |
| E113 | OPERATION.TELEMETRY.2 -> OPERATION.TELEMETRY.4 | related -> requires | retyped |
| E115 | OPERATION.TELEMETRY.5 -> OPERATION.TELEMETRY.6 | related -> realizes | retyped |
| E117 | OPERATION.READINESS.1 -> OPERATION.CAPACITY | related -> requires | retyped |
| E118 | OPERATION.READINESS.1 -> OPERATION.RECOVERY.1 | related -> requires | retyped |
| E123 | OPERATION.RUNBOOKS.2 -> OPERATION.ALERTING.1 | related -> realizes | retyped |
| E124 | OPERATION.RECOVERY.1 -> OPERATION.RELIABILITY.2 | related -> refines | retyped |
| E129 | EVOLUTION.DECOMMISSION.2 -> EVOLUTION.DECISIONS.4 | see -> requires | retyped |
| E130 | EVOLUTION.DECOMMISSION.2 -> EVOLUTION.DECISIONS.3 | see -> requires | retyped |
| E131 | EVOLUTION.DECISIONS.6 -> EVOLUTION.DECISIONS.1 | see -> requires | retyped |
| E132 | EVOLUTION.DECISIONS.6 -> EVOLUTION.DECISIONS.5 | see -> requires | retyped |
| E133 | EVOLUTION.INCREMENTAL.2 -> EVOLUTION.DEBT.1 | see -> refines | retyped |
| E134 | EVOLUTION.INCREMENTAL.3 -> EVOLUTION.INCREMENTAL.1 | see -> requires | retyped |
| E135 | EVOLUTION.INCREMENTAL.3 -> EVOLUTION.DECOMMISSION | see -> requires | retyped |
| E137 | EVOLUTION.INCREMENTAL.6 -> EVOLUTION.DECOMMISSION.3 | see -> requires | retyped |
| E139 | EVOLUTION.DEBT.2 -> EVOLUTION.DEBT.3 | see -> requires | retyped |
| E142 | EVOLUTION.DEBT.5 -> EVOLUTION.INCREMENTAL.4 | see -> requires | retyped |
| E143 | EVOLUTION.DECOMMISSION.5 -> EVOLUTION.INCREMENTAL.4 | see -> requires | retyped |
| E144 | EVOLUTION.DECOMMISSION.5 -> EVOLUTION.DECOMMISSION.3 | see -> requires | retyped |
| E146 | EVOLUTION.TECHNOLOGY.1 -> EVOLUTION.DECOMMISSION.2 | see -> requires | retyped |
| E147 | EVOLUTION.TECHNOLOGY.2 -> EVOLUTION.DECISIONS.3 | see -> requires | retyped |
| E148 | EVOLUTION.TECHNOLOGY.3 -> EVOLUTION.TECHNOLOGY.1 | see -> constrains | retyped |
| E149 | EVOLUTION.TECHNOLOGY.4 -> EVOLUTION.TECHNOLOGY.1 | see -> refines | retyped |
| E150 | CHANGE_FLOW.INTEGRATION.2 -> CHANGE_FLOW.RELEASE.3 | related -> requires | retyped |
| E151 | CHANGE_FLOW.INTEGRATION.3 -> CHANGE_FLOW.RELEASE.1 | related -> requires | retyped |
| E152 | CHANGE_FLOW.INTEGRATION.3 -> CHANGE_FLOW.ROLLBACK.1 | related -> requires | retyped |
| E153 | CHANGE_FLOW.INTEGRATION.4 -> CHANGE_FLOW.INTEGRATION.5 | related -> requires | retyped |
| E154 | CHANGE_FLOW.INTEGRATION.5 -> CHANGE_FLOW.REVIEW.2 | related -> constrains | retyped |
| E155 | CHANGE_FLOW.INTEGRATION.5 -> CHANGE_FLOW.ROLLBACK.2 | related -> requires | retyped |
| E156 | CHANGE_FLOW.INTEGRATION.6 -> CHANGE_FLOW.REVIEW.1 | related -> dataflow | retyped |
| E159 | CHANGE_FLOW.REVIEW.4 -> CHANGE_FLOW.BUILD.1 | related -> requires | retyped |
| E160 | CHANGE_FLOW.BUILD.2 -> CHANGE_FLOW.RELEASE.2 | related -> requires | retyped |
| E161 | CHANGE_FLOW.RELEASE.1 -> CHANGE_FLOW.MEASURE.1 | related -> requires | retyped |
| E163 | CHANGE_FLOW.RELEASE.4 -> CHANGE_FLOW.DEPLOY.1 | related -> requires | retyped |
| E166 | CHANGE_FLOW.DEPLOY.2 -> CHANGE_FLOW.ROLLBACK.1 | related -> requires | retyped |
| E167 | CHANGE_FLOW.DEPLOY.3 -> CHANGE_FLOW.DATA_CHANGE.3 | related -> requires | retyped |
| E168 | CHANGE_FLOW.DEPLOY.3 -> CHANGE_FLOW.DATA_CHANGE.7 | related -> requires | retyped |
| E170 | CHANGE_FLOW.ROLLBACK.3 -> CHANGE_FLOW.DATA_CHANGE.4 | related -> requires | retyped |
| E171 | CHANGE_FLOW.DATA_CHANGE.1 -> CHANGE_FLOW.DATA_CHANGE.2 | related -> requires | retyped |
| E172 | CHANGE_FLOW.DATA_CHANGE.5 -> CHANGE_FLOW.DATA_CHANGE.6 | related -> requires | retyped |
| E174 | CHANGE_FLOW.DATA_CHANGE.7 -> CHANGE_FLOW.DATA_CHANGE.3 | related -> dataflow | retyped |
| E175 | CHANGE_FLOW.DATA_CHANGE.8 -> CHANGE_FLOW.DATA_CHANGE.3 | related -> requires | retyped |
| E176 | CHANGE_FLOW.MEASURE.2 -> CHANGE_FLOW.MEASURE.1 | related -> requires | retyped |
| E177 | CHANGE_FLOW.MEASURE.2 -> CHANGE_FLOW.RELEASE.1 | related -> constrains | retyped |
| E188 | ASSURANCE.BEHAVIOUR.6 -> ASSURANCE.BEHAVIOUR.1 | dataflow -> refines | retyped |
| E195 | ASSURANCE.CONTRACTS.2 -> ASSURANCE.CONTRACTS.3 | see -> requires | retyped |
| E083 | CONSTRUCTION.DATA_NOT_CODE -> CONSTRUCTION.BOUNDARY.2 | refines -> refines | type kept, intent reworded |
| E084 | CONSTRUCTION.DATA_NOT_CODE -> CONSTRUCTION.BOUNDARY.1 | requires -> requires | type kept, intent reworded |
| E087 | CONSTRUCTION.BOUNDARY.5 -> CONSTRUCTION.NAMING | refines -> refines | type kept, intent reworded |
| E092 | CONSTRUCTION.STATE.5 -> CONSTRUCTION.DEPENDENCY_DIRECTION.1 | refines -> refines | type kept, intent reworded |
| E194 | ASSURANCE.CONTRACTS.1 -> ASSURANCE.CONTRACTS.2 | conflicts -> conflicts | type kept, intent reworded |

## 3. Existing links whose arrow was reversed (remove and create)

| id | was | now | type | note |
|---|---|---|---|---|
| E008 | ASSURANCE.AVAILABILITY.4 -> ASSURANCE.AVAILABILITY.5 | ASSURANCE.AVAILABILITY.5 -> ASSURANCE.AVAILABILITY.4 | see -> requires | removed and recreated: src and dst are immutable |
| E040 | TRANSVERSE.SECURITY.2 -> TRANSVERSE.SECURITY_MONITORING.4 | TRANSVERSE.SECURITY_MONITORING.4 -> TRANSVERSE.SECURITY.2 | see -> dataflow | removed and recreated: src and dst are immutable |
| E044 | TRANSVERSE.SECURITY_MONITORING.3 -> TRANSVERSE.PRIVACY.2 | TRANSVERSE.PRIVACY.2 -> TRANSVERSE.SECURITY_MONITORING.3 | see -> constrains | removed and recreated: src and dst are immutable |
| E053 | TRANSVERSE.PRIVACY.4 -> TRANSVERSE.SECURITY_MONITORING.2 | TRANSVERSE.SECURITY_MONITORING.2 -> TRANSVERSE.PRIVACY.4 | see -> dataflow | removed and recreated: src and dst are immutable |
| E054 | TRANSVERSE.PRIVACY.4 -> TRANSVERSE.PRIVACY.1 | TRANSVERSE.PRIVACY.1 -> TRANSVERSE.PRIVACY.4 | see -> dataflow | removed and recreated: src and dst are immutable |
| E065 | CONSTRUCTION.DESIGN.3 -> CONSTRUCTION.DEPENDENCY_DIRECTION.2 | CONSTRUCTION.DEPENDENCY_DIRECTION.2 -> CONSTRUCTION.DESIGN.3 | related -> realizes | removed and recreated: src and dst are immutable |
| E074 | CONSTRUCTION.HIDING -> CONSTRUCTION.PARADIGM | CONSTRUCTION.PARADIGM -> CONSTRUCTION.HIDING | related -> requires | removed and recreated: src and dst are immutable |
| E076 | CONSTRUCTION.HIDING.2 -> CONSTRUCTION.HIDING.3 | CONSTRUCTION.HIDING.3 -> CONSTRUCTION.HIDING.2 | related -> refines | removed and recreated: src and dst are immutable |
| E078 | CONSTRUCTION.HIDING.3 -> CONSTRUCTION.DEPENDENCY_DIRECTION.2 | CONSTRUCTION.DEPENDENCY_DIRECTION.2 -> CONSTRUCTION.HIDING.3 | related -> requires | removed and recreated: src and dst are immutable |
| E079 | CONSTRUCTION.HIDING.3 -> CONSTRUCTION.PARADIGM.2 | CONSTRUCTION.PARADIGM.2 -> CONSTRUCTION.HIDING.3 | related -> requires | removed and recreated: src and dst are immutable |
| E089 | CONSTRUCTION.STATE.1 -> CONSTRUCTION.STATE.2 | CONSTRUCTION.STATE.2 -> CONSTRUCTION.STATE.1 | related -> refines | removed and recreated: src and dst are immutable |
| E090 | CONSTRUCTION.STATE.3 -> CONSTRUCTION.PROCESS.3 | CONSTRUCTION.PROCESS.3 -> CONSTRUCTION.STATE.3 | related -> constrains | removed and recreated: src and dst are immutable |
| E110 | OPERATION.ALERTING.1 -> OPERATION.INCIDENTS.3 | OPERATION.INCIDENTS.3 -> OPERATION.ALERTING.1 | related -> constrains | removed and recreated: src and dst are immutable |
| E111 | OPERATION.TELEMETRY.1 -> OPERATION.TELEMETRY.7 | OPERATION.TELEMETRY.7 -> OPERATION.TELEMETRY.1 | related -> refines | removed and recreated: src and dst are immutable |
| E112 | OPERATION.TELEMETRY.1 -> OPERATION.TELEMETRY.8 | OPERATION.TELEMETRY.8 -> OPERATION.TELEMETRY.1 | related -> refines | removed and recreated: src and dst are immutable |
| E114 | OPERATION.TELEMETRY.4 -> OPERATION.TELEMETRY.5 | OPERATION.TELEMETRY.5 -> OPERATION.TELEMETRY.4 | related -> requires | removed and recreated: src and dst are immutable |
| E121 | OPERATION.RUNBOOKS.1 -> OPERATION.ALERTING.1 | OPERATION.ALERTING.1 -> OPERATION.RUNBOOKS.1 | related -> requires | removed and recreated: src and dst are immutable |
| E140 | EVOLUTION.DEBT.2 -> EVOLUTION.DECOMMISSION.1 | EVOLUTION.DECOMMISSION.1 -> EVOLUTION.DEBT.2 | see -> realizes | removed and recreated: src and dst are immutable |
| E141 | EVOLUTION.DEBT.2 -> EVOLUTION.INCREMENTAL.1 | EVOLUTION.INCREMENTAL.1 -> EVOLUTION.DEBT.2 | see -> realizes | removed and recreated: src and dst are immutable |
| E157 | CHANGE_FLOW.REVIEW.1 -> CHANGE_FLOW.DATA_CHANGE.3 | CHANGE_FLOW.DATA_CHANGE.3 -> CHANGE_FLOW.REVIEW.1 | related -> realizes | removed and recreated: src and dst are immutable |
| E158 | CHANGE_FLOW.REVIEW.1 -> CHANGE_FLOW.DATA_CHANGE.8 | CHANGE_FLOW.DATA_CHANGE.8 -> CHANGE_FLOW.REVIEW.1 | related -> requires | removed and recreated: src and dst are immutable |
| E162 | CHANGE_FLOW.RELEASE.4 -> CHANGE_FLOW.DATA_CHANGE.3 | CHANGE_FLOW.DATA_CHANGE.3 -> CHANGE_FLOW.RELEASE.4 | related -> realizes | removed and recreated: src and dst are immutable |
| E164 | CHANGE_FLOW.DEPLOY.1 -> CHANGE_FLOW.DATA_CHANGE.1 | CHANGE_FLOW.DATA_CHANGE.1 -> CHANGE_FLOW.DEPLOY.1 | related -> requires | removed and recreated: src and dst are immutable |
| E165 | CHANGE_FLOW.DEPLOY.1 -> CHANGE_FLOW.DATA_CHANGE.3 | CHANGE_FLOW.DATA_CHANGE.3 -> CHANGE_FLOW.DEPLOY.1 | related -> requires | removed and recreated: src and dst are immutable |
| E169 | CHANGE_FLOW.ROLLBACK.2 -> CHANGE_FLOW.DATA_CHANGE.4 | CHANGE_FLOW.DATA_CHANGE.4 -> CHANGE_FLOW.ROLLBACK.2 | related -> refines | removed and recreated: src and dst are immutable |
| E173 | CHANGE_FLOW.DATA_CHANGE.6 -> CHANGE_FLOW.DATA_CHANGE.8 | CHANGE_FLOW.DATA_CHANGE.8 -> CHANGE_FLOW.DATA_CHANGE.6 | related -> requires | removed and recreated: src and dst are immutable |
| E186 | ASSURANCE.BEHAVIOUR.3 -> ASSURANCE.CONTRACTS.2 | ASSURANCE.CONTRACTS.2 -> ASSURANCE.BEHAVIOUR.3 | see -> refines | removed and recreated: src and dst are immutable |

## 4. Dropped links (no relation, or covered)

| id | pair | old type | reason |
|---|---|---|---|
| E007 | ASSURANCE.AVAILABILITY.3 -> ASSURANCE.AVAILABILITY.5 | see | sibling kinship only ("related exercises"); neither node depends on the other |
| E012 | ASSURANCE.DOCS_SYNC.2 -> ASSURANCE.DOCS_SYNC.4 | see | complementarity only; inverse of E013, which already states the dependency |
| E022 | OWNERSHIP.STANCE.3 -> OWNERSHIP.LIFECYCLE.4 | (none) | kinship only; vendoring and mirrors are two answers to upstream unavailability, neither depends on the other |
| E046 | TRANSVERSE.PRIVACY.1 -> TRANSVERSE.SECURITY_MONITORING.3 | see | locator for the never-log list; the dependency is already stated by E043 |
| E063 | CONSTRUCTION.DESIGN.1 -> CONSTRUCTION.NAMING | related | coarse form of E097 (NAMING.3 is the naming half of DESIGN.1); no further relation |
| E069 | CONSTRUCTION.SYSTEM_SHAPE.4 -> CONSTRUCTION.HIDING.2 | related | mutual alignment ("designed together"), no direction or dependency stated |
| E071 | CONSTRUCTION.HIDING -> CONSTRUCTION.STATE | related | complementarity only ("complements"); neither node depends on the other |
| E073 | CONSTRUCTION.HIDING -> CONSTRUCTION.NAMING | related | kinship only (a name carries the hidden concept); no dependency stated |
| E077 | CONSTRUCTION.HIDING.3 -> CONSTRUCTION.STATE.1 | related | kinship only (each datum lives in one place); no dependency stated |
| E088 | CONSTRUCTION.BOUNDARY.6 -> CONSTRUCTION.BOUNDARY.1 | related | no relation stated; error content and parse-at-edge are separate decisions |
| E093 | CONSTRUCTION.DEPENDENCY_DIRECTION -> CONSTRUCTION.HIDING.3 | related | lift of E078 (DEPENDENCY_DIRECTION.2 requires HIDING.3), same relation at the parent level |
| E096 | CONSTRUCTION.NAMING.1 -> CONSTRUCTION.NAMING.2 | related | complementarity only; neither node depends on the other |
| E099 | CONSTRUCTION.DATA_NOT_CODE.2 -> CONSTRUCTION.BOUNDARY.1 | related | covered by E084 (DATA_NOT_CODE requires BOUNDARY.1) at the parent level, same relation |
| E105 | OPERATION.RELIABILITY.3 -> OPERATION.INCIDENTS.2 | refines | inverse of E106; the load-bearing dependency is the trigger's need for the budget policy, kept in E106 |
| E116 | OPERATION.INCIDENTS.1 -> OPERATION.RECOVERY.6 | related | analogy only (roles assigned alike); no dependency stated |
| E119 | OPERATION.READINESS.3 -> OPERATION.RECOVERY.6 | related | analogy only (both keep something current); no dependency stated |
| E120 | OPERATION.READINESS.3 -> OPERATION.RUNBOOKS.1 | related | analogy only (both keep documents true); no dependency stated |
| E122 | OPERATION.RUNBOOKS.1 -> OPERATION.RECOVERY.6 | related | analogy only (kept current together); no dependency stated |
| E126 | OPERATION.RECOVERY.3 -> OPERATION.RECOVERY.2 | related | division-of-labour note between siblings; no dependency stated |
| E185 | ASSURANCE.BEHAVIOUR.3 -> ASSURANCE.BEHAVIOUR.4 | see | co-decision of two siblings with no direction stated |
| J1-08 | OWNERSHIP.SERVICES.1 -> ASSURANCE.AVAILABILITY | related | locator pointer; says where availability mechanisms sit, states no relation |
| J1-09 | OWNERSHIP.SERVICES.1 -> OPERATION | related | locator pointer to an L1 branch; states no relation |
| J1-11 | OWNERSHIP.SERVICES.3 -> OPERATION.RECOVERY | related | locator pointer; says where recovery practice sits, states no relation |
| J2-07 | ASSURANCE.RULES.4 -> CHANGE_FLOW.REVIEW | see | inverse of J6-09 (REVIEW realizes RULES); locator for where review is carried out |
| J2-13 | CONSTRUCTION.PARADIGM -> ASSURANCE.BEHAVIOUR.5 | see | locator pointer; divides what PARADIGM and BEHAVIOUR.5 each hold, states no relation |
| J2-21 | OPERATION.FEEDBACK -> ASSURANCE.BEHAVIOUR.8 | see | locator pointer; FEEDBACK links to the catalogue rather than holding it |
| J2-24 | ASSURANCE.CONTRACTS.1 -> OWNERSHIP.CONTAINMENT | see | locator pointer; says where the consumer side is held, states no relation |
| J2-25 | ASSURANCE.CONTRACTS.1 -> CONSTRUCTION.BOUNDARY | see | inverse of J2-26 (BOUNDARY realizes CONTRACTS) |
| J2-27 | ASSURANCE.CONTRACTS.2 -> OWNERSHIP.SERVICES | see | locator pointer; says where doubles are backed, states no dependency |
| J2-28 | ASSURANCE.CONTRACTS.2 -> OWNERSHIP.CONTAINMENT | see | locator pointer; contract tests at a containment seam, states no dependency |
| J2-29 | ASSURANCE.CONTRACTS.3 -> TRANSVERSE.DOCS | see | locator pointer; says where reference-documentation authoring is held |
| J3-01 | ASSURANCE.DATA_INTEGRITY -> CHANGE_FLOW.DATA_CHANGE | index | inverse of J6-33 (DATA_CHANGE realizes DATA_INTEGRITY) |
| J3-02 | ASSURANCE.DATA_INTEGRITY -> OPERATION.RECOVERY | index | locator pointer, covered by J7-28 (DATA_INTEGRITY.3 requires RECOVERY) |
| J3-03 | ASSURANCE.DATA_INTEGRITY.1 -> CONSTRUCTION.BOUNDARY | requires | inverse of J5-27 (BOUNDARY.1 realizes DATA_INTEGRITY.1); edge validation is carried out by BOUNDARY.1 |
| J3-04 | ASSURANCE.DATA_INTEGRITY.1 -> CHANGE_FLOW.DATA_CHANGE | index | locator pointer; says where change procedures are held |
| J3-06 | ASSURANCE.DATA_INTEGRITY.2 -> CHANGE_FLOW.DATA_CHANGE | index | locator pointer; the dependency is stated by J6-40 (DI.2 constrains DATA_CHANGE.6) |
| J3-12 | ASSURANCE.DATA_INTEGRITY.3 -> TRANSVERSE.PRIVACY | requires | covered by J3-09 and J3-10, which name the privacy nodes concerned |
| J3-14 | ASSURANCE.DATA_INTEGRITY.4 -> CHANGE_FLOW.DATA_CHANGE | index | locator pointer; says where procedures for derived structures are held |
| J3-16 | ASSURANCE.DOCS_SYNC -> TRANSVERSE.DOCS | index | inverse of J9-03 (TRANSVERSE.DOCS realizes DOCS_SYNC) |
| J3-17 | ASSURANCE.DOCS_SYNC -> ASSURANCE.CONTRACTS.3 | see | covered by J3-24 (DOCS_SYNC.3 requires CONTRACTS.3), same relation at the parent level |
| J3-18 | ASSURANCE.DOCS_SYNC -> ASSURANCE.RULES.3 | see | covered by J3-21 (DOCS_SYNC.2 requires RULES.3), same relation at the parent level |
| J3-20 | ASSURANCE.DOCS_SYNC.1 -> TRANSVERSE.DOCS | index | locator pointer; says where authoring practice is held |
| J3-23 | ASSURANCE.DOCS_SYNC.2 -> TRANSVERSE.DOCS | see | locator pointer; says where authoring practice is held |
| J3-25 | ASSURANCE.DOCS_SYNC.3 -> OPERATION.RECOVERY | see | locator pointer; the dependency is stated by J7-48 |
| J3-26 | ASSURANCE.DOCS_SYNC.3 -> TRANSVERSE.DOCS | index | locator pointer; says where authoring practice is held |
| J3-27 | ASSURANCE.SECURITY -> TRANSVERSE.SECURITY | index | inverse of J9-14 (TRANSVERSE.SECURITY realizes ASSURANCE.SECURITY) |
| J3-28 | ASSURANCE.SECURITY -> ASSURANCE.RULES.3 | see | covered by J3-34 (SECURITY.2 requires RULES.3), same relation at the parent level |
| J3-29 | ASSURANCE.SECURITY -> ASSURANCE.RULES.5 | see | no relation stated beyond sharing the bar of RULES.5 |
| J3-30 | ASSURANCE.SECURITY -> ASSURANCE.ARTIFACT | see | complementarity only; artifact integrity and code verification do not depend on each other |
| J3-40 | ASSURANCE.SECURITY.5 -> TRANSVERSE.CONFIG | index | locator pointer; the realizing direction is stated by J9-37 (CONFIG realizes ASSURANCE.SECURITY) |
| J3-48 | ASSURANCE.SECURITY.7 -> ASSURANCE.BEHAVIOUR.8 | see | locator pointer; says where defect classes are held |
| J4-07 | ASSURANCE.PERFORMANCE.3 -> OPERATION.TELEMETRY.7 | see | locator pointer; says where synthetic monitoring is held |
| J4-11 | ASSURANCE.PERFORMANCE -> OPERATION.RELIABILITY | see | covered by J4-01 and the objective chain; the realizing direction is not stated |
| J4-12 | ASSURANCE.PERFORMANCE -> OPERATION.CAPACITY | see | covered by the dataflow links PERFORMANCE.2 to CAPACITY.1 and CAPACITY.2 |
| J4-22 | ASSURANCE.AVAILABILITY.3 -> CHANGE_FLOW.DEPLOY | see | covered by J6-26 and J6-27 (DEPLOY.2 realizes AVAILABILITY, requires AVAILABILITY.3) |
| J4-23 | ASSURANCE.AVAILABILITY.4 -> OPERATION.RECOVERY | see | locator pointer, covered by J7-30 and J7-43 |
| J4-25 | ASSURANCE.AVAILABILITY.5 -> OPERATION.RECOVERY | see | locator pointer, covered by J7-42 |
| J4-33 | ASSURANCE.ARTIFACT.1 -> OWNERSHIP.SERVICES.6 | see | locator pointer; says where the CI service as supply chain is held |
| J4-34 | ASSURANCE.ARTIFACT.1 -> ASSURANCE.SECURITY.5 | see | locator pointer; says where consumed code is treated |
| J5-01 | CONSTRUCTION -> ASSURANCE.CONTRACTS | realizes | L1 source; lifted from the branch-level links BOUNDARY to CONTRACTS (J2-26), not created manually |
| J5-02 | CONSTRUCTION -> ASSURANCE.DATA_INTEGRITY.1 | realizes | L1 source; lifted from J5-27 (BOUNDARY.1 realizes DATA_INTEGRITY.1) |
| J5-03 | CONSTRUCTION -> ASSURANCE.RULES.3 | realizes | L1 source; lifted from J5-43 (DEPENDENCY_DIRECTION.2 realizes RULES.3) |
| J5-04 | CONSTRUCTION -> ASSURANCE.SECURITY | related | L1 source; no relation stated ("relates to") |
| J5-05 | CONSTRUCTION -> TRANSVERSE.SECURITY | related | L1 source; no relation stated ("relates to") |
| J5-06 | CONSTRUCTION -> TRANSVERSE.CONFIG | related | L1 source; no relation stated ("relates to") |
| J5-08 | CONSTRUCTION.DESIGN -> EVOLUTION.INCREMENTAL | related | covered by J5-12 (DESIGN.4 requires INCREMENTAL.3), the node that decides replacement against rewrite |
| J5-10 | CONSTRUCTION.DESIGN.2 -> OWNERSHIP.STANCE.4 | related | consistency only ("consistent with"); no dependency stated |
| J5-15 | CONSTRUCTION.SYSTEM_SHAPE -> ASSURANCE.CONTRACTS.1 | realizes | same sentence as J5-20 at the parent level (SYSTEM_SHAPE.3 holds the boundary placement) |
| J5-16 | CONSTRUCTION.SYSTEM_SHAPE -> ASSURANCE.CONTRACTS.2 | realizes | same sentence as J5-21 at the parent level |
| J5-17 | CONSTRUCTION.SYSTEM_SHAPE -> OPERATION.RELIABILITY | related | no relation stated ("fault isolation and distribution cost") |
| J5-18 | CONSTRUCTION.SYSTEM_SHAPE.2 -> OPERATION.RELIABILITY | related | no node named for "failure handling"; RELIABILITY holds objectives, so the target is not unambiguous |
| J5-22 | CONSTRUCTION.SYSTEM_SHAPE.3 -> OWNERSHIP.SERVICES.2 | related | no relation stated; only names the consumer side of provider evolution |
| J5-26 | CONSTRUCTION.BOUNDARY -> ASSURANCE.DATA_INTEGRITY.1 | realizes | same sentence as J5-27 at the parent level |
| J5-34 | CONSTRUCTION.BOUNDARY.4 -> ASSURANCE.DATA_INTEGRITY.1 | related | no relation stated ("store constraints and the published layer") |
| J5-37 | CONSTRUCTION.BOUNDARY.6 -> OPERATION.INCIDENTS | related | locator pointer; says where failure detail goes, no unambiguous target |
| J5-38 | CONSTRUCTION.STATE -> ASSURANCE.DATA_INTEGRITY.4 | related | covered by J5-39, J5-40 and J5-41, which name the STATE nodes concerned |
| J5-42 | CONSTRUCTION.DEPENDENCY_DIRECTION -> ASSURANCE.RULES.3 | related | same sentence as J5-43 at the parent level |
| J5-45 | CONSTRUCTION.PARADIGM -> OWNERSHIP.SELECTION.2 | related | covered by J5-47 (PARADIGM.1 refines SELECTION.2), same relation at the parent level |
| J5-46 | CONSTRUCTION.PARADIGM -> ASSURANCE.DATA_INTEGRITY.1 | related | covered by J5-49, same relation at the parent level |
| J5-48 | CONSTRUCTION.PARADIGM.2 -> OWNERSHIP.STANCE | related | no relation stated; cites a ledger row only |
| J5-52 | CONSTRUCTION.DATA_NOT_CODE -> ASSURANCE.SECURITY.2 | related | no relation stated; only names security findings |
| J5-54 | CONSTRUCTION.DATA_NOT_CODE -> TRANSVERSE.SECURITY | related | no relation stated ("programme practice") |
| J5-55 | CONSTRUCTION.DATA_NOT_CODE.2 -> ASSURANCE.SECURITY | related | covered by J5-53 (least privilege), same relation at a less precise target |
| J5-57 | CONSTRUCTION.DATA_NOT_CODE.3 -> ASSURANCE.SECURITY | related | no relation stated |
| J5-58 | CONSTRUCTION.PROCESS -> CHANGE_FLOW.DEPLOY | related | covered by J5-60 (DEPLOY.4 requires PROCESS.1), same relation at the parent level |
| J5-61 | CONSTRUCTION.PROCESS.2 -> OPERATION.INCIDENTS | related | locator pointer; says where restart policy and crash-loop alerts belong |
| J6-05 | CHANGE_FLOW.INTEGRATION.6 -> ASSURANCE.SECURITY.6 | related | no relation beyond sitting beside; the dependency is stated by J3-42 |
| J6-28 | CHANGE_FLOW.DEPLOY.2 -> OPERATION.RUNBOOKS | related | locator pointer; says where a playbook clause lives |
| J6-44 | CHANGE_FLOW.DATA_CHANGE.8 -> OPERATION.INCIDENTS | related | locator pointer; says that a statement is identifiable during an incident |
| J7-05 | OPERATION.RELIABILITY.1 -> ASSURANCE.PERFORMANCE.5 | related | parallel rules (run-to-run distribution beside the production percentile); no dependency |
| J7-06 | OPERATION.ALERTING -> ASSURANCE.PERFORMANCE | realizes | the tie runs through the shared objective (E107, J4-01); no direct relation to PERFORMANCE |
| J7-12 | OPERATION.TELEMETRY.2 -> ASSURANCE.SECURITY.7 | related | analogy only (probing that detection works); no dependency stated |
| J7-14 | OPERATION.TELEMETRY.4 -> TRANSVERSE.PRIVACY | related | covered by J9-33 (PRIVACY.1 constrains TELEMETRY.4), same relation at a less precise source |
| J7-17 | OPERATION.INCIDENTS.2 -> ASSURANCE.SECURITY.7 | related | locator pointer, covered by J7-16 |
| J7-25 | OPERATION.RUNBOOKS -> ASSURANCE.DOCS_SYNC.3 | related | covered by J7-26 (RUNBOOKS.1 refines DOCS_SYNC.3), same relation at the parent level |
| J7-29 | OPERATION.RECOVERY -> TRANSVERSE.PRIVACY | related | covered by J7-32, J7-33 and J7-40, which name the privacy nodes concerned |
| J7-31 | OPERATION.RECOVERY.2 -> OWNERSHIP.SERVICES | related | locator pointer; says what to verify of a rented service's backups |
| J7-37 | OPERATION.RECOVERY.3 -> TRANSVERSE.SECURITY | related | no relation stated ("sits on the boundary") |
| J7-39 | OPERATION.RECOVERY.3 -> OWNERSHIP.SERVICES | related | locator pointer; says where verification of a rented service's backup is held |
| J8-02 | EVOLUTION.DECISIONS.1 -> OWNERSHIP.SELECTION.1 | realizes | same sentence as J8-01 at a finer source |
| J8-04 | EVOLUTION.DECISIONS.4 -> TRANSVERSE.DOCS | see | locator pointer; divides living documents from superseded records |
| J8-06 | EVOLUTION.DECISIONS.5 -> ASSURANCE.RULES.4 | see | consistency only ("matches"); no dependency stated |
| J8-17 | EVOLUTION.INCREMENTAL.4 -> OWNERSHIP.LIFECYCLE | realizes | analogy only (dependency-update analogue); no dependency stated |
| J8-25 | EVOLUTION.DEBT -> OWNERSHIP.LIFECYCLE | realizes | covered by J8-28 and J8-30, which name the DEBT nodes concerned |
| J8-26 | EVOLUTION.DEBT -> ASSURANCE.BEHAVIOUR | realizes | covered by J8-32 and J8-33, which name the DEBT node concerned |
| J8-27 | EVOLUTION.DEBT.1 -> CHANGE_FLOW.DATA_CHANGE | see | covered by E133 (INCREMENTAL.2 refines DEBT.1); the data migration is that case |
| J8-31 | EVOLUTION.DEBT.3 -> CHANGE_FLOW.MEASURE | see | locator pointer; "maintainability signals are measured trends" |
| J8-34 | EVOLUTION.DEBT.4 -> CHANGE_FLOW.REVIEW | see | no relation stated beyond "reviewed as changes" |
| J8-39 | EVOLUTION.DECOMMISSION -> OWNERSHIP.SERVICES | realizes | covered by the dataflow links DECOMMISSION.3, .4 and .5 to SERVICES.2 |
| J8-40 | EVOLUTION.DECOMMISSION -> ASSURANCE.CONTRACTS | realizes | covered by J8-43 and J8-45, which name the DECOMMISSION nodes concerned |
| J8-42 | EVOLUTION.DECOMMISSION.1 -> CHANGE_FLOW.DEPLOY | see | locator pointer; "retired code is not left on the production system" |
| J8-55 | EVOLUTION.TECHNOLOGY.1 -> OWNERSHIP.SELECTION | realizes | complementarity only ("complements the entry test"); covered by J8-53 |
| J8-57 | EVOLUTION.TECHNOLOGY.2 -> OWNERSHIP.SELECTION.1 | see | negative statement ("not the sanctioned list"); no link |
| J8-58 | EVOLUTION.TECHNOLOGY.2 -> OWNERSHIP.LIFECYCLE.5 | see | negative statement ("not the inventory"); no link |
| J9-01 | TRANSVERSE -> ASSURANCE.DOCS_SYNC | realizes | L1 source; lifted from J9-03 (TRANSVERSE.DOCS realizes DOCS_SYNC) |
| J9-02 | TRANSVERSE -> ASSURANCE.SECURITY | realizes | L1 source; lifted from J9-14, J9-20, J9-37 |
| J9-10 | TRANSVERSE.DOCS.3 -> CHANGE_FLOW.INTEGRATION | see | locator pointer; "history is held in commits" |
| J9-19 | TRANSVERSE.SECURITY.5 -> OPERATION.INCIDENTS | see | locator pointer; divides live incident handling from the vulnerability loop |
| J9-22 | TRANSVERSE.SECURITY_MONITORING -> OPERATION.ALERTING | see | covered by J9-28 (SECURITY_MONITORING.4 requires ALERTING), same relation at the parent level |
| J9-23 | TRANSVERSE.SECURITY_MONITORING.1 -> ASSURANCE.SECURITY.1 | see | negative statement ("depth does not set what is logged"); no link |
| J9-24 | TRANSVERSE.SECURITY_MONITORING.1 -> OPERATION.TELEMETRY | see | no relation beyond J9-21 |
| J9-25 | TRANSVERSE.SECURITY_MONITORING.2 -> ASSURANCE.SECURITY.7 | see | covered by J9-27 (SECURITY_MONITORING.4 requires SECURITY.7) |
| J9-26 | TRANSVERSE.SECURITY_MONITORING.2 -> OPERATION.TELEMETRY | see | no relation beyond J9-21 |
| J9-29 | TRANSVERSE.SECURITY_MONITORING.4 -> OWNERSHIP.CONTAINMENT | see | locator pointer; "exit from a detection tool", no unambiguous target |
| J9-31 | TRANSVERSE.PRIVACY -> ASSURANCE.SECURITY | realizes | the sentence says privacy goes "beyond security process", so no carry-out relation |
| J9-32 | TRANSVERSE.PRIVACY -> OPERATION.RECOVERY | see | covered by J7-32, J7-33 and J7-40 |
| J9-34 | TRANSVERSE.PRIVACY.3 -> OPERATION.RECOVERY | see | covered by J7-33 and J7-40 |
| J9-38 | TRANSVERSE.CONFIG -> CHANGE_FLOW.BUILD | see | locator pointer; "build and pipeline" |
| J9-41 | TRANSVERSE.CONFIG.1 -> CONSTRUCTION.BOUNDARY.2 | see | locator pointer; token acceptance was moved to BOUNDARY.2 |
| J9-44 | TRANSVERSE.CONFIG.5 -> CHANGE_FLOW.BUILD | see | locator pointer; "pipeline identity" |
| J9-50 | TRANSVERSE.ENVIRONMENTS.1 -> CHANGE_FLOW.DEPLOY | see | covered by J9-48 (ENVIRONMENTS realizes DEPLOY.3), same relation at a finer source |
| J9-54 | TRANSVERSE.ENVIRONMENTS.3 -> CHANGE_FLOW.BUILD | see | locator pointer; "build" |
| J9-55 | TRANSVERSE.ENVIRONMENTS.3 -> ASSURANCE.ARTIFACT | see | locator pointer; "artifact integrity" |

## 5. Merged links (duplicate pair or inverse restatement)

| id | pair | old type | merged into | reason |
|---|---|---|---|---|
| E009 | ASSURANCE.DATA_INTEGRITY.3 -> ASSURANCE.DATA_INTEGRITY.5 | see | into E010 (ASSURANCE.DATA_INTEGRITY.5 -> ASSURANCE.DATA_INTEGRITY.3, realizes) | inverse restatement of the same relation |
| E017 | OWNERSHIP.STANCE.1 -> OWNERSHIP.SELECTION.2 | (none) | into E024 (OWNERSHIP.SELECTION.2 -> OWNERSHIP.STANCE.1, refines) | inverse restatement of the same relation |
| E018 | OWNERSHIP.STANCE.1 -> OWNERSHIP.SELECTION.1 | (none) | into E023 (OWNERSHIP.SELECTION.1 -> OWNERSHIP.STANCE.1, realizes) | inverse restatement of the same relation |
| E019 | OWNERSHIP.STANCE.2 -> OWNERSHIP.STANCE.3 | (none) | into E021 (OWNERSHIP.STANCE.3 -> OWNERSHIP.STANCE.2, refines) | inverse restatement of the same relation |
| E028 | OWNERSHIP.LIFECYCLE.2 -> OWNERSHIP.SELECTION.3 | (none) | into E025 (OWNERSHIP.SELECTION.3 -> OWNERSHIP.LIFECYCLE.2, dataflow) | inverse restatement of the same relation |
| E030 | OWNERSHIP.LIFECYCLE.4 -> OWNERSHIP.SELECTION.5 | (none) | into E026 (OWNERSHIP.SELECTION.5 -> OWNERSHIP.LIFECYCLE.4, requires) | inverse restatement of the same relation |
| E031 | OWNERSHIP.LIFECYCLE.5 -> OWNERSHIP.SELECTION.5 | (none) | into E027 (OWNERSHIP.SELECTION.5 -> OWNERSHIP.LIFECYCLE.5, dataflow) | inverse restatement of the same relation |
| E032 | OWNERSHIP.CONTAINMENT.1 -> OWNERSHIP.SERVICES.3 | (none) | into E035 (OWNERSHIP.SERVICES.3 -> OWNERSHIP.CONTAINMENT.1, dataflow) | inverse restatement of the same relation |
| E033 | OWNERSHIP.CONTAINMENT.1 -> OWNERSHIP.CONTAINMENT.2 | (none) | into E034 (OWNERSHIP.CONTAINMENT.2 -> OWNERSHIP.CONTAINMENT.1, realizes) | inverse restatement of the same relation |
| E036 | OWNERSHIP.SERVICES.3 -> OWNERSHIP.STANCE.2 | (none) | into E020 (OWNERSHIP.STANCE.2 -> OWNERSHIP.SERVICES.3, requires) | inverse restatement of the same relation |
| E038 | TRANSVERSE.SECURITY.1 -> TRANSVERSE.SECURITY.2 | see | into E039 (TRANSVERSE.SECURITY.2 -> TRANSVERSE.SECURITY.1, requires) | inverse restatement of the same relation |
| E041 | TRANSVERSE.SECURITY.5 -> TRANSVERSE.SECURITY.6 | see | into E042 (TRANSVERSE.SECURITY.6 -> TRANSVERSE.SECURITY.5, dataflow) | inverse restatement of the same relation |
| E047 | TRANSVERSE.PRIVACY.1 -> TRANSVERSE.PRIVACY.2 | see | into E048 (TRANSVERSE.PRIVACY.2 -> TRANSVERSE.PRIVACY.1, requires) | inverse restatement of the same relation |
| E049 | TRANSVERSE.PRIVACY.2 -> TRANSVERSE.PRIVACY.3 | see | into E051 (TRANSVERSE.PRIVACY.3 -> TRANSVERSE.PRIVACY.2, requires) | inverse restatement of the same relation |
| E052 | TRANSVERSE.PRIVACY.3 -> TRANSVERSE.SECURITY_MONITORING.5 | see | into E045 (TRANSVERSE.SECURITY_MONITORING.5 -> TRANSVERSE.PRIVACY.3, constrains) | inverse restatement of the same relation |
| E059 | TRANSVERSE.CONFIG.4 -> TRANSVERSE.PRIVACY.2 | see | into E050 (TRANSVERSE.PRIVACY.2 -> TRANSVERSE.CONFIG.4, constrains) | inverse restatement of the same relation |
| E109 | OPERATION.ALERTING.1 -> OPERATION.RUNBOOKS.2 | related | into E123 (OPERATION.RUNBOOKS.2 -> OPERATION.ALERTING.1, realizes) | inverse restatement of the same relation |
| E128 | EVOLUTION.DECISIONS.4 -> EVOLUTION.DECOMMISSION.2 | see | into E129 (EVOLUTION.DECOMMISSION.2 -> EVOLUTION.DECISIONS.4, requires) | inverse restatement of the same relation |
| E136 | EVOLUTION.INCREMENTAL.4 -> EVOLUTION.DECOMMISSION.5 | see | into E143 (EVOLUTION.DECOMMISSION.5 -> EVOLUTION.INCREMENTAL.4, requires) | inverse restatement of the same relation |
| E138 | EVOLUTION.DEBT.1 -> EVOLUTION.INCREMENTAL.2 | see | into E133 (EVOLUTION.INCREMENTAL.2 -> EVOLUTION.DEBT.1, refines) | inverse restatement of the same relation |
| E145 | EVOLUTION.TECHNOLOGY.1 -> EVOLUTION.TECHNOLOGY.3 | see | into E148 (EVOLUTION.TECHNOLOGY.3 -> EVOLUTION.TECHNOLOGY.1, constrains) | inverse restatement of the same relation |
| J1-01 | OWNERSHIP.STANCE.4 -> EVOLUTION.INCREMENTAL | related | into J8-07 (EVOLUTION.INCREMENTAL -> OWNERSHIP.STANCE.4, realizes) | inverse restatement of the same relation (incremental change carries out the stance) |
| J1-03 | OWNERSHIP.SELECTION.1 -> EVOLUTION.DECISIONS | related | into J8-01 (EVOLUTION.DECISIONS -> OWNERSHIP.SELECTION.1, realizes) | inverse restatement of the same relation (the record practice carries out the written reason) |
| J1-06 | OWNERSHIP.CONTAINMENT.2 -> CONSTRUCTION.BOUNDARY | related | into J5-28 (OWNERSHIP.CONTAINMENT.2 -> CONSTRUCTION.BOUNDARY.1, realizes) | coarse form; the conversion to a precise type is held at BOUNDARY.1, so the link is stated there |
| J1-10 | OWNERSHIP.SERVICES.2 -> ASSURANCE.CONTRACTS.1 | related | into J2-22 (OWNERSHIP.SERVICES.2 -> ASSURANCE.CONTRACTS.1, requires) | same pair as J2-22 (requires is the stronger type) |
| J1-12 | EVOLUTION.DECOMMISSION.3 -> OWNERSHIP.SERVICES.2 | related | into J8-44 (EVOLUTION.DECOMMISSION.3 -> OWNERSHIP.SERVICES.2, dataflow) | same pair as J8-44 (dataflow is the stronger type) |
| J1-13 | EVOLUTION.DECOMMISSION.5 -> OWNERSHIP.SERVICES.2 | related | into J8-47 (EVOLUTION.DECOMMISSION.5 -> OWNERSHIP.SERVICES.2, dataflow) | same pair as J8-47 (dataflow is the stronger type) |
| J2-08 | CHANGE_FLOW.REVIEW.1 -> ASSURANCE.RULES.4 | see | into J6-10 (CHANGE_FLOW.REVIEW.1 -> ASSURANCE.RULES.4, realizes) | same pair as J6-10 (realizes is the stronger type) |
| J2-11 | ASSURANCE.AVAILABILITY.3 -> ASSURANCE.BEHAVIOUR.5 | see | into J4-20 (ASSURANCE.AVAILABILITY.3 -> ASSURANCE.BEHAVIOUR.5, requires) | same pair as J4-20 (requires is the stronger type) |
| J2-12 | ASSURANCE.AVAILABILITY.5 -> ASSURANCE.BEHAVIOUR.5 | see | into J4-27 (ASSURANCE.AVAILABILITY.5 -> ASSURANCE.BEHAVIOUR.5, requires) | same pair as J4-27 |
| J2-14 | ASSURANCE.BEHAVIOUR.7 -> ASSURANCE.AVAILABILITY.3 | see | into J4-21 (ASSURANCE.AVAILABILITY.3 -> ASSURANCE.BEHAVIOUR.7, requires) | inverse restatement of the same relation |
| J2-15 | ASSURANCE.PERFORMANCE.4 -> ASSURANCE.AVAILABILITY.3 | see | into E003 (ASSURANCE.PERFORMANCE.4 -> ASSURANCE.AVAILABILITY.3, requires) | same pair as existing E003 (requires is the stronger type) |
| J2-23 | EVOLUTION.DECOMMISSION.4 -> ASSURANCE.CONTRACTS.1 | see | into J8-45 (EVOLUTION.DECOMMISSION.4 -> ASSURANCE.CONTRACTS.1, realizes) | same pair as J8-45 (realizes is the stronger type) |
| J3-07 | ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY | index | into J7-28 (ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY, requires) | same pair as J7-28 (requires is the stronger type) |
| J3-08 | ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY.2 | see | into J7-35 (ASSURANCE.DATA_INTEGRITY.3 -> OPERATION.RECOVERY.2, requires) | same pair as J7-35 (requires is the stronger type) |
| J3-32 | ASSURANCE.SECURITY.2 -> ASSURANCE.RULES.1 | requires | into J2-01 (ASSURANCE.SECURITY.2 -> ASSURANCE.RULES.1, requires) | same pair as J2-01 |
| J3-37 | ASSURANCE.SECURITY.3 -> ASSURANCE.BEHAVIOUR.6 | see | into J2-02 (ASSURANCE.SECURITY.3 -> ASSURANCE.BEHAVIOUR.6, requires) | same pair as J2-02 |
| J3-44 | ASSURANCE.SECURITY.6 -> CHANGE_FLOW.DATA_CHANGE.3 | see | into J6-36 (CHANGE_FLOW.DATA_CHANGE.3 -> ASSURANCE.SECURITY.6, realizes) | inverse restatement of the same relation |
| J3-45 | ASSURANCE.SECURITY.6 -> CHANGE_FLOW.DATA_CHANGE.8 | see | into J6-45 (CHANGE_FLOW.DATA_CHANGE.8 -> ASSURANCE.SECURITY.6, realizes) | inverse restatement of the same relation |
| J3-46 | ASSURANCE.SECURITY.6 -> ASSURANCE.ARTIFACT.2 | see | into J4-38 (ASSURANCE.ARTIFACT.2 -> ASSURANCE.SECURITY.6, realizes) | inverse restatement of the same relation |
| J3-49 | ASSURANCE.SECURITY.7 -> OPERATION.INCIDENTS | see | into J7-16 (OPERATION.INCIDENTS -> ASSURANCE.SECURITY.7, realizes) | inverse restatement of the same relation |
| J4-13 | ASSURANCE.PERFORMANCE -> CHANGE_FLOW.DEPLOY | see | into J4-08 (CHANGE_FLOW.DEPLOY.2 -> ASSURANCE.PERFORMANCE.4, realizes) | same relation at the parent level; narrowed to DEPLOY.2, which holds canary evaluation |
| J4-14 | ASSURANCE.AVAILABILITY -> OPERATION.RECOVERY | see | into J7-27 (OPERATION.RECOVERY -> ASSURANCE.AVAILABILITY, realizes) | inverse restatement of the same relation |
| J4-15 | ASSURANCE.AVAILABILITY -> OPERATION.RELIABILITY | see | into J7-01 (OPERATION.RELIABILITY -> ASSURANCE.AVAILABILITY, realizes) | inverse restatement of the same relation |
| J4-16 | ASSURANCE.AVAILABILITY -> OPERATION.READINESS | see | into J7-23 (OPERATION.READINESS -> ASSURANCE.AVAILABILITY, realizes) | inverse restatement of the same relation |
| J4-24 | ASSURANCE.AVAILABILITY.4 -> ASSURANCE.DATA_INTEGRITY.3 | see | into J3-11 (ASSURANCE.DATA_INTEGRITY.3 -> ASSURANCE.AVAILABILITY.4, requires) | inverse restatement of the same relation |
| J4-26 | ASSURANCE.AVAILABILITY.5 -> OPERATION.INCIDENTS | see | into J7-15 (OPERATION.INCIDENTS -> ASSURANCE.AVAILABILITY.5, realizes) | inverse restatement of the same relation |
| J4-35 | ASSURANCE.ARTIFACT.2 -> CHANGE_FLOW.INTEGRATION | see | into J6-02 (CHANGE_FLOW.INTEGRATION -> ASSURANCE.ARTIFACT.2, realizes) | inverse restatement of the same relation |
| J4-36 | ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.3 | see | into J2-05 (ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.3, realizes) | same pair as J2-05 (realizes is the stronger type) |
| J4-37 | ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.4 | see | into J2-06 (ASSURANCE.ARTIFACT.2 -> ASSURANCE.RULES.4, realizes) | same pair as J2-06 (realizes is the stronger type) |
| J5-07 | CONSTRUCTION.DESIGN -> OWNERSHIP.STANCE.4 | related | into J1-02 (CONSTRUCTION.DESIGN -> OWNERSHIP.STANCE.4, realizes) | same pair as J1-02 (realizes is the stronger type) |
| J5-25 | CONSTRUCTION.BOUNDARY -> ASSURANCE.CONTRACTS | realizes | into J2-26 (CONSTRUCTION.BOUNDARY -> ASSURANCE.CONTRACTS, realizes) | same pair as J2-26 |
| J5-51 | CONSTRUCTION.PARADIGM.2 -> OPERATION.TELEMETRY.8 | related | into J7-09 (CONSTRUCTION.PARADIGM.2 -> OPERATION.TELEMETRY.8, requires) | same pair as J7-09 (requires is the stronger type) |
| J6-15 | CHANGE_FLOW.BUILD -> ASSURANCE.ARTIFACT | realizes | into J4-28 (CHANGE_FLOW.BUILD -> ASSURANCE.ARTIFACT, realizes) | same pair as J4-28 |
| J6-29 | CHANGE_FLOW.DEPLOY.3 -> TRANSVERSE.ENVIRONMENTS | related | into J9-48 (TRANSVERSE.ENVIRONMENTS -> CHANGE_FLOW.DEPLOY.3, realizes) | inverse restatement of the same relation |
| J7-02 | ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY | refines | into J4-01 (ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY, refines) | same pair as J4-01 |
| J7-03 | ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.1 | related | into J4-02 (ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.1, requires) | same pair as J4-02 |
| J7-04 | ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.2 | related | into J4-03 (ASSURANCE.PERFORMANCE.1 -> OPERATION.RELIABILITY.2, requires) | same pair as J4-03 |
| J7-08 | ASSURANCE.DATA_INTEGRITY.4 -> OPERATION.TELEMETRY.8 | requires | into J3-13 (ASSURANCE.DATA_INTEGRITY.4 -> OPERATION.TELEMETRY.8, requires) | same pair as J3-13 |
| J7-11 | OPERATION.TELEMETRY.1 -> ASSURANCE.PERFORMANCE.5 | related | into J4-10 (ASSURANCE.PERFORMANCE.5 -> OPERATION.TELEMETRY.1, requires) | inverse restatement of the same relation |
| J7-19 | OPERATION.CAPACITY -> ASSURANCE.PERFORMANCE.2 | realizes | into J4-04 (ASSURANCE.PERFORMANCE.2 -> OPERATION.CAPACITY, dataflow) | same pair as J4-04 reversed; the sentence describes consumption of an output, a dataflow |
| J7-49 | OPERATION.FEEDBACK -> CHANGE_FLOW.MEASURE | related | into J6-47 (CHANGE_FLOW.MEASURE -> OPERATION.FEEDBACK, dataflow) | inverse restatement of the same relation |
| J8-48 | EVOLUTION.DECOMMISSION.6 -> OPERATION.RECOVERY.2 | see | into J7-36 (OPERATION.RECOVERY.2 -> EVOLUTION.DECOMMISSION.6, constrains) | same pair as J7-36 |
| J9-47 | TRANSVERSE.CONFIG.6 -> OWNERSHIP.LIFECYCLE.3 | see | into J1-05 (OWNERSHIP.LIFECYCLE.3 -> TRANSVERSE.CONFIG.6, requires) | inverse restatement of the same relation |

## 6. Cross rows whose arrow was reversed or whose endpoint was narrowed

| id | row says | link is | change |
|---|---|---|---|
| J2-16 | ASSURANCE.BEHAVIOUR.7 -> TRANSVERSE.PRIVACY | TRANSVERSE.PRIVACY -> ASSURANCE.BEHAVIOUR.7 | reversed |
| J2-17 | ASSURANCE.BEHAVIOUR -> ASSURANCE.DATA_INTEGRITY | ASSURANCE.DATA_INTEGRITY -> ASSURANCE.BEHAVIOUR | reversed |
| J2-18 | ASSURANCE.BEHAVIOUR -> ASSURANCE.SECURITY | ASSURANCE.SECURITY -> ASSURANCE.BEHAVIOUR | reversed |
| J2-19 | ASSURANCE.BEHAVIOUR -> ASSURANCE.PERFORMANCE | ASSURANCE.PERFORMANCE -> ASSURANCE.BEHAVIOUR | reversed |
| J2-20 | ASSURANCE.BEHAVIOUR -> ASSURANCE.ARTIFACT | ASSURANCE.ARTIFACT -> ASSURANCE.BEHAVIOUR | reversed |
| J3-09 | ASSURANCE.DATA_INTEGRITY.3 -> TRANSVERSE.PRIVACY.2 | TRANSVERSE.PRIVACY.2 -> ASSURANCE.DATA_INTEGRITY.3 | reversed |
| J3-10 | ASSURANCE.DATA_INTEGRITY.3 -> TRANSVERSE.PRIVACY.3 | TRANSVERSE.PRIVACY.3 -> ASSURANCE.DATA_INTEGRITY.3 | reversed |
| J3-35 | ASSURANCE.SECURITY.2 -> CHANGE_FLOW.BUILD | CHANGE_FLOW.BUILD -> ASSURANCE.SECURITY.2 | reversed |
| J3-39 | ASSURANCE.SECURITY.5 -> OWNERSHIP.LIFECYCLE | ASSURANCE.SECURITY.5 -> OWNERSHIP.LIFECYCLE.5 | target narrowed |
| J3-42 | ASSURANCE.SECURITY.6 -> CHANGE_FLOW.INTEGRATION | ASSURANCE.SECURITY.6 -> CHANGE_FLOW.INTEGRATION.6 | target narrowed |
| J4-05 | ASSURANCE.PERFORMANCE.3 -> CHANGE_FLOW.BUILD | CHANGE_FLOW.BUILD -> ASSURANCE.PERFORMANCE.3 | reversed |
| J4-08 | ASSURANCE.PERFORMANCE.4 -> CHANGE_FLOW.DEPLOY | CHANGE_FLOW.DEPLOY.2 -> ASSURANCE.PERFORMANCE.4 | reversed and target narrowed |
| J4-18 | ASSURANCE.AVAILABILITY.2 -> OWNERSHIP.CONTAINMENT.2 | OWNERSHIP.CONTAINMENT.2 -> ASSURANCE.AVAILABILITY.2 | reversed |
| J5-12 | CONSTRUCTION.DESIGN.4 -> EVOLUTION.INCREMENTAL | CONSTRUCTION.DESIGN.4 -> EVOLUTION.INCREMENTAL.3 | target narrowed |
| J5-14 | CONSTRUCTION.DESIGN.4 -> OPERATION.CAPACITY | OPERATION.CAPACITY -> CONSTRUCTION.DESIGN.4 | reversed |
| J5-19 | CONSTRUCTION.SYSTEM_SHAPE.2 -> CHANGE_FLOW.DEPLOY | CONSTRUCTION.SYSTEM_SHAPE.2 -> CHANGE_FLOW.DEPLOY.1 | target narrowed |
| J5-23 | CONSTRUCTION.HIDING.1 -> OWNERSHIP.CONTAINMENT | OWNERSHIP.CONTAINMENT -> CONSTRUCTION.HIDING.1 | reversed |
| J5-24 | CONSTRUCTION.HIDING.4 -> ASSURANCE.DATA_INTEGRITY.1 | ASSURANCE.DATA_INTEGRITY.1 -> CONSTRUCTION.HIDING.4 | reversed |
| J5-28 | CONSTRUCTION.BOUNDARY.1 -> OWNERSHIP.CONTAINMENT.2 | OWNERSHIP.CONTAINMENT.2 -> CONSTRUCTION.BOUNDARY.1 | reversed |
| J5-29 | CONSTRUCTION.BOUNDARY.1 -> OWNERSHIP.CONTAINMENT.4 | OWNERSHIP.CONTAINMENT.4 -> CONSTRUCTION.BOUNDARY.1 | reversed |
| J5-36 | CONSTRUCTION.BOUNDARY.6 -> ASSURANCE.DATA_INTEGRITY.1 | ASSURANCE.DATA_INTEGRITY.1 -> CONSTRUCTION.BOUNDARY.6 | reversed |
| J5-59 | CONSTRUCTION.PROCESS -> OPERATION.CAPACITY | OPERATION.CAPACITY -> CONSTRUCTION.PROCESS | reversed |
| J5-60 | CONSTRUCTION.PROCESS.1 -> CHANGE_FLOW.DEPLOY | CHANGE_FLOW.DEPLOY.4 -> CONSTRUCTION.PROCESS.1 | reversed and target narrowed |
| J6-08 | CHANGE_FLOW.INTEGRATION.6 -> ASSURANCE.RULES.5 | ASSURANCE.RULES.5 -> CHANGE_FLOW.INTEGRATION.6 | reversed |
| J6-14 | CHANGE_FLOW.REVIEW.4 -> ASSURANCE.RULES.4 | ASSURANCE.RULES.4 -> CHANGE_FLOW.REVIEW.4 | reversed |
| J6-24 | CHANGE_FLOW.RELEASE.5 -> OPERATION.INCIDENTS | OPERATION.INCIDENTS -> CHANGE_FLOW.RELEASE.5 | reversed |
| J6-38 | CHANGE_FLOW.DATA_CHANGE.4 -> ASSURANCE.CONTRACTS | CHANGE_FLOW.DATA_CHANGE.4 -> ASSURANCE.CONTRACTS.1 | target narrowed |
| J6-39 | CHANGE_FLOW.DATA_CHANGE.4 -> CONSTRUCTION.HIDING | CHANGE_FLOW.DATA_CHANGE.4 -> CONSTRUCTION.HIDING.3 | target narrowed |
| J6-40 | CHANGE_FLOW.DATA_CHANGE.6 -> ASSURANCE.DATA_INTEGRITY.2 | ASSURANCE.DATA_INTEGRITY.2 -> CHANGE_FLOW.DATA_CHANGE.6 | reversed |
| J6-41 | CHANGE_FLOW.DATA_CHANGE.7 -> TRANSVERSE.PRIVACY | TRANSVERSE.PRIVACY -> CHANGE_FLOW.DATA_CHANGE.7 | reversed |
| J6-43 | CHANGE_FLOW.DATA_CHANGE.8 -> OPERATION.TELEMETRY | CHANGE_FLOW.DATA_CHANGE.8 -> OPERATION.TELEMETRY.1 | target narrowed |
| J7-18 | OPERATION.INCIDENTS.2 -> TRANSVERSE.SECURITY_MONITORING | OPERATION.INCIDENTS.2 -> TRANSVERSE.SECURITY_MONITORING.4 | target narrowed |
| J7-20 | OPERATION.CAPACITY.1 -> ASSURANCE.PERFORMANCE.2 | ASSURANCE.PERFORMANCE.2 -> OPERATION.CAPACITY.1 | reversed |
| J7-21 | OPERATION.CAPACITY.2 -> ASSURANCE.PERFORMANCE.2 | ASSURANCE.PERFORMANCE.2 -> OPERATION.CAPACITY.2 | reversed |
| J7-32 | OPERATION.RECOVERY.2 -> TRANSVERSE.PRIVACY.2 | TRANSVERSE.PRIVACY.2 -> OPERATION.RECOVERY.2 | reversed |
| J7-33 | OPERATION.RECOVERY.2 -> TRANSVERSE.PRIVACY.3 | TRANSVERSE.PRIVACY.3 -> OPERATION.RECOVERY.2 | reversed |
| J7-34 | OPERATION.RECOVERY.2 -> ASSURANCE.DATA_INTEGRITY.5 | ASSURANCE.DATA_INTEGRITY.5 -> OPERATION.RECOVERY.2 | reversed |
| J7-36 | EVOLUTION.DECOMMISSION.6 -> OPERATION.RECOVERY.2 | OPERATION.RECOVERY.2 -> EVOLUTION.DECOMMISSION.6 | reversed |
| J7-40 | OPERATION.RECOVERY.3 -> TRANSVERSE.PRIVACY.3 | TRANSVERSE.PRIVACY.3 -> OPERATION.RECOVERY.3 | reversed |
| J7-45 | OPERATION.RECOVERY.5 -> TRANSVERSE.SECURITY | TRANSVERSE.SECURITY -> OPERATION.RECOVERY.5 | reversed |
| J8-13 | EVOLUTION.INCREMENTAL.2 -> CHANGE_FLOW.DATA_CHANGE | CHANGE_FLOW.DATA_CHANGE -> EVOLUTION.INCREMENTAL.2 | reversed |
| J8-36 | EVOLUTION.DEBT.5 -> OWNERSHIP.LIFECYCLE.3 | OWNERSHIP.LIFECYCLE.3 -> EVOLUTION.DEBT.5 | reversed |
| J8-37 | EVOLUTION.DEBT.5 -> OWNERSHIP.LIFECYCLE.5 | OWNERSHIP.LIFECYCLE.5 -> EVOLUTION.DEBT.5 | reversed |
| J8-49 | EVOLUTION.DECOMMISSION.6 -> TRANSVERSE.PRIVACY.2 | TRANSVERSE.PRIVACY.2 -> EVOLUTION.DECOMMISSION.6 | reversed |
| J8-50 | EVOLUTION.DECOMMISSION.6 -> TRANSVERSE.PRIVACY.3 | TRANSVERSE.PRIVACY.3 -> EVOLUTION.DECOMMISSION.6 | reversed |
| J9-15 | TRANSVERSE.SECURITY.1 -> ASSURANCE.SECURITY.1 | ASSURANCE.SECURITY.1 -> TRANSVERSE.SECURITY.1 | reversed |
| J9-33 | TRANSVERSE.PRIVACY.1 -> OPERATION.TELEMETRY | TRANSVERSE.PRIVACY.1 -> OPERATION.TELEMETRY.4 | target narrowed |
| J9-35 | TRANSVERSE.PRIVACY.3 -> CHANGE_FLOW.DATA_CHANGE | TRANSVERSE.PRIVACY.3 -> CHANGE_FLOW.DATA_CHANGE.6 | target narrowed |
| J9-46 | TRANSVERSE.CONFIG.6 -> ASSURANCE.SECURITY.5 | ASSURANCE.SECURITY.5 -> TRANSVERSE.CONFIG.6 | reversed |
| J9-48 | TRANSVERSE.ENVIRONMENTS -> CHANGE_FLOW.DEPLOY | TRANSVERSE.ENVIRONMENTS -> CHANGE_FLOW.DEPLOY.3 | target narrowed |
| J9-49 | TRANSVERSE.ENVIRONMENTS -> ASSURANCE.BEHAVIOUR | ASSURANCE.BEHAVIOUR -> TRANSVERSE.ENVIRONMENTS | reversed |
| J9-52 | TRANSVERSE.ENVIRONMENTS.2 -> CHANGE_FLOW.BUILD | CHANGE_FLOW.BUILD -> TRANSVERSE.ENVIRONMENTS.2 | reversed |

## 7. Unresolved targets

- J4-17 ASSURANCE.AVAILABILITY.1 -> CONSTRUCTION: target is the L1 branch CONSTRUCTION; the record names no L3 holding the design of a degraded mode and no CONSTRUCTION node is unambiguous. Nearest candidates (CONSTRUCTION.PROCESS, CONSTRUCTION.BOUNDARY.6) do not hold the design of a degraded mode, so no link was invented. Recommendation: the maintainer names the node, or the link stays absent.

All other targets exist in the graph (checked by the dry run). The targets marked (new) or (check) in the lists exist, including TELEMETRY.7 and TELEMETRY.8.

