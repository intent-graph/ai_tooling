# Cross links of J9_transverse

Links whose other endpoint lies outside the unit, for the linker. Direction is source to target; type is realizes, requires or see (the judge record's verbs). L1 node TRANSVERSE is built in the TOP batch, so its links are listed here too.

| source | target | type | intent |
|---|---|---|---|
| TRANSVERSE | ASSURANCE.DOCS_SYNC | realizes | Transverse realizes ASSURANCE.DOCS_SYNC: the cross-cutting practices below carry out the documentation-sync guarantee. |
| TRANSVERSE | ASSURANCE.SECURITY | realizes | Transverse realizes ASSURANCE.SECURITY: the cross-cutting practices below carry out the security guarantee. |
| TRANSVERSE.DOCS | ASSURANCE.DOCS_SYNC | realizes | Documentation Practice realizes ASSURANCE.DOCS_SYNC: authoring and organisation practice whose mechanisms are held there. |
| TRANSVERSE.DOCS.1 | ASSURANCE.DOCS_SYNC | requires | Documentation Budget requires ASSURANCE.DOCS_SYNC: the full docs-as-code level relies on the owners and gates held there. |
| TRANSVERSE.DOCS.1 | ASSURANCE.DOCS_SYNC.3 | see | Documentation Budget refers to ASSURANCE.DOCS_SYNC.3: derived documents are read-only. |
| TRANSVERSE.DOCS.2 | ASSURANCE.DOCS_SYNC.3 | see | Organisation and Structure refers to ASSURANCE.DOCS_SYNC.3: one canonical document per topic is held there. |
| TRANSVERSE.DOCS.2 | ASSURANCE.DOCS_SYNC.4 | see | Organisation and Structure refers to ASSURANCE.DOCS_SYNC.4: size caps and annotations are checked mechanically there. |
| TRANSVERSE.DOCS.3 | ASSURANCE.DOCS_SYNC.3 | see | Layered Writing and Audience Split refers to ASSURANCE.DOCS_SYNC.3: one canonical document and dated verification are held there. |
| TRANSVERSE.DOCS.3 | ASSURANCE.DOCS_SYNC.4 | see | Layered Writing and Audience Split refers to ASSURANCE.DOCS_SYNC.4: examples are executed there. |
| TRANSVERSE.DOCS.3 | CHANGE_FLOW.INTEGRATION | see | Layered Writing and Audience Split refers to CHANGE_FLOW.INTEGRATION: history is held in commits. |
| TRANSVERSE.DOCS.4 | CHANGE_FLOW.RELEASE | see | Release Changelog refers to CHANGE_FLOW.RELEASE: a changelog belongs to a release. |
| TRANSVERSE.DOCS.4 | ASSURANCE.DOCS_SYNC.4 | see | Release Changelog refers to ASSURANCE.DOCS_SYNC.4: the chore rule enforces the presence of an entry. |
| TRANSVERSE.DOCS.5 | EVOLUTION.DECISIONS | see | Basis and Evolution of Guidelines refers to EVOLUTION.DECISIONS: records of an overriding rule are held there. |
| TRANSVERSE.SECURITY | ASSURANCE.SECURITY | realizes | Security Practice realizes ASSURANCE.SECURITY: programme practice whose verification is held there. |
| TRANSVERSE.SECURITY.1 | ASSURANCE.SECURITY.1 | requires | Anchor Framework requires ASSURANCE.SECURITY.1: depth set per application from risk selects the requirement level. |
| TRANSVERSE.SECURITY.2 | ASSURANCE.SECURITY.7 | see | Maturity Targets and Cycle refers to ASSURANCE.SECURITY.7: effectiveness is itself tested there. |
| TRANSVERSE.SECURITY.3 | ASSURANCE.SECURITY.1 | see | Design-Time Risk Modelling refers to ASSURANCE.SECURITY.1: the design is reviewed against the risk model there. |
| TRANSVERSE.SECURITY.5 | ASSURANCE.SECURITY.7 | see | Vulnerability Response Loop refers to ASSURANCE.SECURITY.7: the process change and class-precluding approach are held there. |
| TRANSVERSE.SECURITY.5 | OPERATION.INCIDENTS | see | Vulnerability Response Loop refers to OPERATION.INCIDENTS: the live incident is handled there, this loop covers the vulnerability. |
| TRANSVERSE.SECURITY_MONITORING | ASSURANCE.SECURITY | realizes | Security Monitoring and Audit Trail realizes ASSURANCE.SECURITY: logging and detection practice whose verification is held there. |
| TRANSVERSE.SECURITY_MONITORING | OPERATION.TELEMETRY | see | Security Monitoring and Audit Trail refers to OPERATION.TELEMETRY: operational telemetry shares the logging pipeline. |
| TRANSVERSE.SECURITY_MONITORING | OPERATION.ALERTING | see | Security Monitoring and Audit Trail refers to OPERATION.ALERTING: escalation of detected attacks. |
| TRANSVERSE.SECURITY_MONITORING.1 | ASSURANCE.SECURITY.1 | see | Events Logged refers to ASSURANCE.SECURITY.1: the assurance target; verification depth does not set what is logged. |
| TRANSVERSE.SECURITY_MONITORING.1 | OPERATION.TELEMETRY | see | Events Logged refers to OPERATION.TELEMETRY: operational telemetry. |
| TRANSVERSE.SECURITY_MONITORING.2 | ASSURANCE.SECURITY.7 | see | Entry Content, Time and Format refers to ASSURANCE.SECURITY.7: verification that detection works. |
| TRANSVERSE.SECURITY_MONITORING.2 | OPERATION.TELEMETRY | see | Entry Content, Time and Format refers to OPERATION.TELEMETRY: operational telemetry. |
| TRANSVERSE.SECURITY_MONITORING.4 | ASSURANCE.SECURITY.7 | requires | Detection and Escalation requires ASSURANCE.SECURITY.7: a known probe must be shown to raise an alert. |
| TRANSVERSE.SECURITY_MONITORING.4 | OPERATION.ALERTING | see | Detection and Escalation refers to OPERATION.ALERTING: escalation. |
| TRANSVERSE.SECURITY_MONITORING.4 | OWNERSHIP.CONTAINMENT | see | Detection and Escalation refers to OWNERSHIP.CONTAINMENT: exit from a detection tool. |
| TRANSVERSE.SECURITY_MONITORING.5 | ASSURANCE.DATA_INTEGRITY.1 | see | Business Audit Trail refers to ASSURANCE.DATA_INTEGRITY.1: the atomic audit declared in the store. |
| TRANSVERSE.PRIVACY | ASSURANCE.SECURITY | realizes | Privacy and Retention realizes ASSURANCE.SECURITY: privacy practice beyond security process. |
| TRANSVERSE.PRIVACY | OPERATION.RECOVERY | see | Privacy and Retention refers to OPERATION.RECOVERY: backup retention. |
| TRANSVERSE.PRIVACY.1 | OPERATION.TELEMETRY | see | Minimisation, Classification and Design-In refers to OPERATION.TELEMETRY: how trace context is propagated. |
| TRANSVERSE.PRIVACY.3 | OPERATION.RECOVERY | see | Erasure and Deletion Mechanism refers to OPERATION.RECOVERY: backup design and retention. |
| TRANSVERSE.PRIVACY.3 | CHANGE_FLOW.DATA_CHANGE | see | Erasure and Deletion Mechanism refers to CHANGE_FLOW.DATA_CHANGE: batching a bulk change. |
| TRANSVERSE.PRIVACY.4 | OPERATION.INCIDENTS | see | Privacy Risk, Impact Assessment and Breach refers to OPERATION.INCIDENTS: incident handling. |
| TRANSVERSE.CONFIG | ASSURANCE.SECURITY | realizes | Configuration and Secrets realizes ASSURANCE.SECURITY: secrets practice; secret scanning is held there. |
| TRANSVERSE.CONFIG | CHANGE_FLOW.BUILD | see | Configuration and Secrets refers to CHANGE_FLOW.BUILD: build and pipeline. |
| TRANSVERSE.CONFIG.1 | CHANGE_FLOW.INTEGRATION | requires | Separation of Configuration from Code and Secrets requires CHANGE_FLOW.INTEGRATION: repository access and tracked, attributable changes. |
| TRANSVERSE.CONFIG.1 | ASSURANCE.SECURITY.5 | see | Separation of Configuration from Code and Secrets refers to ASSURANCE.SECURITY.5: secret scanning. |
| TRANSVERSE.CONFIG.1 | CONSTRUCTION.BOUNDARY.2 | see | Separation of Configuration from Code and Secrets refers to CONSTRUCTION.BOUNDARY.2: token acceptance, moved there. |
| CHANGE_FLOW.DEPLOY | TRANSVERSE.CONFIG.2 | realizes | CHANGE_FLOW.DEPLOY realizes TRANSVERSE.CONFIG.2: deploy applies configuration to the one artifact. |
| OPERATION | TRANSVERSE.CONFIG.2 | realizes | OPERATION realizes TRANSVERSE.CONFIG.2: operation delivers configuration and secrets to the running process. |
| TRANSVERSE.CONFIG.5 | CHANGE_FLOW.BUILD | see | Credential Lifetime and Pipeline Identity refers to CHANGE_FLOW.BUILD: pipeline identity. |
| TRANSVERSE.CONFIG.5 | ASSURANCE.SECURITY.6 | see | Credential Lifetime and Pipeline Identity refers to ASSURANCE.SECURITY.6: limits on what automation may do. |
| TRANSVERSE.CONFIG.6 | ASSURANCE.SECURITY.5 | see | Response to a Leaked Secret refers to ASSURANCE.SECURITY.5: a secret found in history is rotated. |
| TRANSVERSE.CONFIG.6 | OWNERSHIP.LIFECYCLE.3 | see | Response to a Leaked Secret refers to OWNERSHIP.LIFECYCLE.3: supply-chain trigger; rotation is held here. |
| TRANSVERSE.ENVIRONMENTS | CHANGE_FLOW.DEPLOY | see | Development Environments refers to CHANGE_FLOW.DEPLOY: environment parity. |
| TRANSVERSE.ENVIRONMENTS | ASSURANCE.BEHAVIOUR | see | Development Environments refers to ASSURANCE.BEHAVIOUR: tests run in these environments. |
| TRANSVERSE.ENVIRONMENTS.1 | CHANGE_FLOW.DEPLOY | see | Separation and Isolation refers to CHANGE_FLOW.DEPLOY: parity with production. |
| TRANSVERSE.ENVIRONMENTS.2 | OWNERSHIP.LIFECYCLE | see | Definition Mechanism refers to OWNERSHIP.LIFECYCLE: pinning. |
| TRANSVERSE.ENVIRONMENTS.2 | CHANGE_FLOW.BUILD | see | Definition Mechanism refers to CHANGE_FLOW.BUILD: the build uses the same definition. |
| TRANSVERSE.ENVIRONMENTS.3 | OWNERSHIP.LIFECYCLE | see | Toolchain Control and Hardening refers to OWNERSHIP.LIFECYCLE: pinning and changing build tools. |
| TRANSVERSE.ENVIRONMENTS.3 | CHANGE_FLOW.BUILD | see | Toolchain Control and Hardening refers to CHANGE_FLOW.BUILD: build. |
| TRANSVERSE.ENVIRONMENTS.3 | ASSURANCE.ARTIFACT | see | Toolchain Control and Hardening refers to ASSURANCE.ARTIFACT: artifact integrity. |
