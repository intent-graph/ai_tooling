# Transverse

Each cross-cutting concern is an owned, recorded practice whose guarantee is held elsewhere:
documentation sized by its readers, security anchored in a published framework with one
vulnerability loop and protected event logs, personal data minimised and retained on a schedule,
configuration and secrets kept out of code and artifact, and development environments treated as
code and separated from production. The guarantees [assurance](assurance.md) decides thus have a
practice that can be carried out and checked. `TRANSVERSE`

Hard rules of the branch:

- Configuration and secrets MUST NOT be held in code or in the artifact.
- An exposed secret MUST NOT be treated as safe.
- Personal data MUST NOT be kept without a recorded purpose and period.
- A development environment MUST NOT be able to reach production by accident.

Each concern states only what [assurance](assurance.md) does not: verification and enforcement
live there, the practice lives here.

## Map
<!-- Lines 22-30 -->

| Section | Practice in one line |
|---|---|
| [Documentation Practice](transverse_documentation.md#documentation-practice) | Documentation sized by its readers, organised by need, written in layers, with a recorded basis |
| [Security Practice](transverse_security.md#security-practice) | A published framework, design-time risk modelling, owned responsibility, one vulnerability loop |
| [Security Monitoring and Audit Trail](transverse_security.md#security-monitoring-and-audit-trail) | Security events logged, protected, detected on; business audit trail kept apart |
| [Privacy and Retention](transverse_privacy.md#privacy-and-retention) | Personal data minimised, classified, retained on a schedule, erasable |
| [Configuration and Secrets](transverse_config_environments.md#configuration-and-secrets) | One artifact for every environment; secrets in custody, short-lived, audited |
| [Development Environments](transverse_config_environments.md#development-environments) | Separated from production, defined as code, hardened |
