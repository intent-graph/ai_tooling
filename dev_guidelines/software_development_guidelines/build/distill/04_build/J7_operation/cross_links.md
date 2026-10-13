# Cross links of unit J7_operation

Links with one endpoint outside this unit, for the linker. Columns: source uid, target uid, link type, intent sentence. Direction: the source depends on, refines, realizes or relates to the target. Sources: the Links lines of the final judge records and cross-unit lines X8, X11, X12. The L1 node OPERATION and its links (realizes ASSURANCE.AVAILABILITY and ASSURANCE.PERFORMANCE) belong to the TOP batch.

| source uid | target uid | link type | intent |
|---|---|---|---|
| OPERATION.RELIABILITY | ASSURANCE.AVAILABILITY | realizes | The objectives and budget are what the availability proof is read against. |
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY | refines | Test targets refine the production reliability objective. |
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY.1 | related | PERFORMANCE.1 keeps its threshold on a percentile and points to the percentile rule held in RELIABILITY.1 (X11). |
| ASSURANCE.PERFORMANCE.1 | OPERATION.RELIABILITY.2 | related | A provisional start for a test target from measured history follows RELIABILITY.2 (X11). |
| OPERATION.RELIABILITY.1 | ASSURANCE.PERFORMANCE.5 | related | PERFORMANCE.5 keeps its own run-to-run distribution rule beside the production percentile rule. |
| OPERATION.ALERTING | ASSURANCE.PERFORMANCE | realizes | Alerts are built on the objective that performance assurance tests against. |
| OPERATION.TELEMETRY | ASSURANCE.PERFORMANCE | realizes | The signals (including per-statement statistics) that performance assurance measures are enabled here. |
| ASSURANCE.DATA_INTEGRITY.4 | OPERATION.TELEMETRY.8 | requires | The integrity of derived data requires the four scheduled-work signals (X12). |
| CONSTRUCTION.PARADIGM.2 | OPERATION.TELEMETRY.8 | requires | The monitoring of scheduled work required by the construction practice is held in TELEMETRY.8 (X12). |
| OPERATION.TELEMETRY.1 | ASSURANCE.PERFORMANCE.3 | related | Signals read here feed the performance measurements held in PERFORMANCE.3. |
| OPERATION.TELEMETRY.1 | ASSURANCE.PERFORMANCE.5 | related | Service signals are the production counterpart of the measure-before-optimising rule. |
| OPERATION.TELEMETRY.2 | ASSURANCE.SECURITY.7 | related | SECURITY.7 probes that detection works; TELEMETRY.2 applies the same idea to the telemetry pipeline. |
| OPERATION.TELEMETRY.3 | OWNERSHIP.CONTAINMENT | related | Libraries depend on the instrumentation API only, a boundary with library wrapping and dependency practice. |
| OPERATION.TELEMETRY.4 | TRANSVERSE.PRIVACY | related | TRANSVERSE.PRIVACY holds the rule on personal data in the propagated context (one location). |
| OPERATION.INCIDENTS | ASSURANCE.AVAILABILITY.5 | realizes | Incident learning realizes the corrective actions that recovery exercises demand. |
| OPERATION.INCIDENTS | ASSURANCE.SECURITY.7 | realizes | Incident defects change the process, as SECURITY.7 requires. |
| OPERATION.INCIDENTS.2 | ASSURANCE.SECURITY.7 | related | SECURITY.7 holds fix, change the process, preclude the class. |
| OPERATION.INCIDENTS.2 | TRANSVERSE.SECURITY_MONITORING | related | Incident lessons are fed back into detection. |
| OPERATION.CAPACITY | ASSURANCE.PERFORMANCE.2 | realizes | Capacity consumes the tested breaking point and its early-warning metrics. |
| OPERATION.CAPACITY.1 | ASSURANCE.PERFORMANCE.2 | related | Planning uses the breaking point held in PERFORMANCE.2. |
| OPERATION.CAPACITY.2 | ASSURANCE.PERFORMANCE.2 | realizes | Headroom is derived from the tested breaking point. |
| OPERATION.CAPACITY.2 | ASSURANCE.AVAILABILITY.1 | realizes | Overload behaviour is what the availability design decision requires. |
| OPERATION.READINESS | ASSURANCE.AVAILABILITY | realizes | The readiness review checks failure modes and recovery proof. |
| OPERATION.READINESS.1 | CHANGE_FLOW.RELEASE | related | The readiness gate sits at launch, in the release flow. |
| OPERATION.RUNBOOKS | ASSURANCE.DOCS_SYNC.3 | related | Owner, date and review for every hand-written document apply to every runbook. |
| OPERATION.RUNBOOKS.1 | ASSURANCE.DOCS_SYNC.3 | related | RUNBOOKS.1 applies DOCS_SYNC.3 and adds validation by another person. |
| OPERATION.RECOVERY | ASSURANCE.AVAILABILITY | realizes | AVAILABILITY holds the proof of restore and exercises; RECOVERY holds the practice (MD-03). |
| ASSURANCE.DATA_INTEGRITY.3 | OPERATION.RECOVERY | requires | The second layer of integrity defence is backups, held here. |
| OPERATION.RECOVERY | TRANSVERSE.PRIVACY | related | Retention and erasure of personal data in backups. |
| OPERATION.RECOVERY.1 | ASSURANCE.AVAILABILITY.4 | related | The objectives are the criteria the restore proof is fixed against. |
| OPERATION.RECOVERY.2 | OWNERSHIP.SERVICES | related | What to verify of a rented service's backups is held in OWNERSHIP.SERVICES. |
| OPERATION.RECOVERY.2 | TRANSVERSE.PRIVACY.2 | related | Backup retention is bounded above by the privacy periods (X8). |
| OPERATION.RECOVERY.2 | TRANSVERSE.PRIVACY.3 | related | Erasure of personal data in backups is held in PRIVACY.3 (X8). |
| OPERATION.RECOVERY.2 | ASSURANCE.DATA_INTEGRITY.5 | related | The oldest backup is kept at least as long as corruption may go undetected; detection is held in DATA_INTEGRITY.5 (X8). |
| ASSURANCE.DATA_INTEGRITY.3 | OPERATION.RECOVERY.2 | related | The first-layer copy's purge and retention point to RECOVERY.2 (X8). |
| EVOLUTION.DECOMMISSION.6 | OPERATION.RECOVERY.2 | related | Backups of a retired system follow the retention rules, neither shorter nor longer (X8). |
| OPERATION.RECOVERY.3 | TRANSVERSE.SECURITY | related | The protection of backups sits on the boundary with security. |
| OPERATION.RECOVERY.3 | ASSURANCE.SECURITY.6 | related | No single credential or person can delete every copy; SECURITY.6 holds the large-blast-radius job principle. |
| OPERATION.RECOVERY.3 | OWNERSHIP.SERVICES | related | A backup held by a rented service is verified under OWNERSHIP.SERVICES. |
| OPERATION.RECOVERY.3 | TRANSVERSE.PRIVACY.3 | related | Erasure in backups, including a copy locked as immutable, is held in PRIVACY.3 (X8). |
| ASSURANCE.DATA_INTEGRITY.3 | OPERATION.RECOVERY.3 | related | Its second-layer copy is handled as RECOVERY.3 and PRIVACY.3 set (X8). |
| OPERATION.RECOVERY.4 | ASSURANCE.AVAILABILITY.5 | related | Every recovery path relied on is exercised, as AVAILABILITY.5 fixes. |
| OPERATION.RECOVERY.4 | ASSURANCE.AVAILABILITY.4 | related | Restore tests prove the restore path that the strategy relies on. |
| OPERATION.RECOVERY.5 | CHANGE_FLOW | related | Rebuild from source rests on infrastructure as code in the change flow. |
| OPERATION.RECOVERY.5 | TRANSVERSE.SECURITY | related | The recovered environment is held to the production security baseline. |
| OPERATION.RECOVERY.5 | ASSURANCE.AVAILABILITY.4 | related | The restore path is independent of schema tooling. |
| OPERATION.RECOVERY.6 | ASSURANCE.AVAILABILITY.4 | related | Regular restore testing is the proof of recovery. |
| OPERATION.RECOVERY.6 | ASSURANCE.DOCS_SYNC.3 | related | The recovery plan is a hand-written document under the owner, date and review rule. |
| OPERATION.FEEDBACK | CHANGE_FLOW.MEASURE | related | Delivery measures held in MEASURE return to developers as feedback here. |
