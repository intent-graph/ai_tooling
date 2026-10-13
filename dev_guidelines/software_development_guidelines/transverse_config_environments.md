# Transverse: Configuration and Environments

How configuration and secrets are kept and delivered, and how development environments are separated and defined. Part of [Transverse](transverse.md).

## Table of Contents

1. [Configuration and Secrets](#configuration-and-secrets) _(Lines 20-28)_
   1. [Separation of Configuration from Code and Secrets](#separation-of-configuration-from-code-and-secrets) _(Lines 31-49)_
   1. [Delivery Channel to the Running Software](#delivery-channel-to-the-running-software) _(Lines 52-71)_
   1. [Shape of Per-Environment Configuration](#shape-of-per-environment-configuration) _(Lines 74-83)_
   1. [Central Secret Custody and Lifecycle](#central-secret-custody-and-lifecycle) _(Lines 86-99)_
   1. [Credential Lifetime and Pipeline Identity](#credential-lifetime-and-pipeline-identity) _(Lines 102-117)_
   1. [Response to a Leaked Secret](#response-to-a-leaked-secret) _(Lines 120-132)_
1. [Development Environments](#development-environments) _(Lines 135-141)_
   1. [Separation and Isolation](#separation-and-isolation) _(Lines 144-154)_
   1. [Definition Mechanism](#definition-mechanism) _(Lines 157-172)_
   1. [Toolchain Control and Hardening](#toolchain-control-and-hardening) _(Lines 175-184)_
## Configuration and Secrets
<!-- Lines 20-28 -->

Configuration and secrets stay out of the code and the artifact; secrets sit in central custody
with least privilege, short lifetime and an audit of every access, and reach the process by a
channel chosen for their criticality; pipelines hold short-lived federated credentials; an exposed
secret is treated as compromised. The same artifact runs in every environment and a leaked
repository or log exposes no working credential. Secret scanning is held in
[Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code), not here. Decides where the
configuration of a backing service lives for ownership. `TRANSVERSE.CONFIG`

### Separation of Configuration from Code and Secrets
<!-- Lines 31-49 -->

Configuration is kept strictly separate from code and from the deployable package, so one build
serves every environment. The test: the codebase could be open-sourced at any moment without
exposing a credential. Secrets are never hardcoded or committed and are kept apart from non-secret
configuration.

- MUST NOT commit a secret to source or configuration; a private repository is not custody.
- MUST keep configuration out of the deployable package; configuration baked in per environment
  means the artifact differs from what was reviewed.
- Configuration expressed as code lives in a repository with least-privilege access and tracked,
  attributable changes ([Version Control and Integration](change_flow_integration_review.md#version-control-and-integration)).
- Relies on [Central Secret Custody and Lifecycle](#central-secret-custody-and-lifecycle) and on the
  scanning of [Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code). Token acceptance
  is held in [What Counts as Valid](construction.md#what-counts-as-valid).

Open: the clause that secrets are drawn, compared, stored and logged only through audited platform
mechanisms is grounded only in part (access audit above, never-log in
[Log Protection and Sanitising](transverse_security.md#log-protection-and-sanitising)). `TRANSVERSE.CONFIG.1`

### Delivery Channel to the Running Software
<!-- Lines 52-71 -->

Non-secret configuration is versioned, reviewed and applied at deploy, so the artifact is the same
in every environment. Secrets live in a managed store and reach the process by runtime injection,
as mounted files or through the store interface.

- MUST record the channel and its reason.
- MUST NOT deliver a secret inside the artifact.
- An environment variable carries a secret only where the platform offers neither alternative, or
  where the process environment is shown not to leak (no child process inherits it, no diagnostics
  or dumps include it) and a restart suffices to rotate.

Best instead: environment variables are best for non-secret values and low-criticality secrets on
platforms that offer nothing else (universal, simple, portable); files or the store interface are
best where rotation without restart and audit matter. Non-secret configuration of every environment
packaged with the binary and selected at deploy is best where it must change and roll back
atomically with the code that reads it; the artifact stays one. Builds on
[Separation of Configuration from Code and Secrets](#separation-of-configuration-from-code-and-secrets)
and draws from [Central Secret Custody and Lifecycle](#central-secret-custody-and-lifecycle);
deployment applies it ([Deployment](change_flow_delivery.md#deployment)). `TRANSVERSE.CONFIG.2`

### Shape of Per-Environment Configuration
<!-- Lines 74-83 -->

Per-environment configuration is a set of independent granular values. With many deployments
(previews, per tenant) each takes its own values; with a few fixed environments a named
environment may be one reviewed file of values, read in one place.

- MUST NOT branch application code on environment name.

Best instead: named bundles are best for a handful of fixed environments; for many deployments
they grow combinatorially and are best never. `TRANSVERSE.CONFIG.3`

### Central Secret Custody and Lifecycle
<!-- Lines 86-99 -->

Secrets are centralized in one managed solution with fine-grained least-privilege access per
service and automated creation, rotation, revocation and expiry. Short-lived dynamic secrets are
preferred ([Credential Lifetime and Pipeline Identity](#credential-lifetime-and-pipeline-identity)).
Every access is audited, with logs queryable for a recorded period.

- MUST audit every access; entries follow [Entry Content, Time and Format](transverse_security.md#entry-content-time-and-format).
- MUST NOT share one credential across services.
- The audit period falls under [Retention Periods](transverse_privacy.md#retention-periods).
- A platform default store is hardened, not trusted as is.

Best instead: on a single small service the platform's own store is the managed store; ad hoc
stores per application or team are best never at scale. `TRANSVERSE.CONFIG.4`

### Credential Lifetime and Pipeline Identity
<!-- Lines 102-117 -->

Credentials are short-lived and issued dynamically where the platform supports it. Every non-human
identity (build and deployment workflows, automated authors) authenticates with federated
short-lived tokens, holds only the permissions its job needs, is scoped per environment, and is kept
out of the environment that runs untrusted or generated code. The build and deployment system is
treated as production.

- MUST NOT store a long-lived cloud credential in the build system where federation is available.
- MUST scope credentials per environment.
- No secret appears in pipeline output.
- Relies on [Central Secret Custody and Lifecycle](#central-secret-custody-and-lifecycle) and on
  [Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access).

Best instead: static secrets rotated on a schedule are best for few services of low criticality or
where the platform cannot issue dynamic credentials. `TRANSVERSE.CONFIG.5`

### Response to a Leaked Secret
<!-- Lines 120-132 -->

A secret found in code, history or logs is treated as compromised: revoked at once, rotated by an
automated process, removed from the exposed locations, and the audit logs are used to investigate
what it was used for between exposure and revocation.

- MUST revoke before cleaning; cleaning the history and keeping the secret is best never.
- MUST be able to rotate without manual steps.
- A leaked secret is one case of the [Vulnerability Response Loop](transverse_security.md#vulnerability-response-loop);
  investigation relies on the audit of [Central Secret Custody and Lifecycle](#central-secret-custody-and-lifecycle).
  A supply-chain compromise triggers it from [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle).

`TRANSVERSE.CONFIG.6`

## Development Environments
<!-- Lines 135-141 -->

Environments are separated from production in instance and credentials while matching it in kind
and version; the development environment is itself versioned code, defined by the cheapest
mechanism that gives the reproducibility needed; development endpoints and the toolchain are
hardened as an attack surface. A developer or a build cannot reach production by accident and every
machine builds the same way. `TRANSVERSE.ENVIRONMENTS`

### Separation and Isolation
<!-- Lines 144-154 -->

Development, build, test and production are separated and protected from each other: secrets are
isolated, non-production minimizes use of production services, and human access to build services
is minimized and audited. Isolation is of instance and credentials; parity with production, of kind
and version, is held in [Environment Parity](change_flow_delivery.md#environment-parity).

- MUST NOT share a credential across environments. Shared instances or credentials for convenience
  are best never.

Open: production data in lower environments is outside this practice. `TRANSVERSE.ENVIRONMENTS.1`

### Definition Mechanism
<!-- Lines 157-172 -->

The development environment is defined as versioned code and is reproducible by anyone on a clean
machine, using the cheapest mechanism that gives the reproducibility needed.

| Mechanism | Best when |
|---|---|
| Dependency manifests with language-level isolation | Single-language project, no native dependencies |
| Container definition | Mixed-skill teams, cloud IDEs, native dependencies |
| Pinned package set | Byte-level control of versions across machines and build is required and the team accepts the learning cost |

- MUST keep the definition in version control.
- MUST be able to rebuild from a clean machine.
- The build uses the same definition. Pinning relies on [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle).

`TRANSVERSE.ENVIRONMENTS.2`

### Toolchain Control and Hardening
<!-- Lines 175-184 -->

Development endpoints and the toolchain are an attack surface: hardened to an approved hardening
guide, run with least functionality and least privilege, and monitored continuously for posture.
Treating developer machines as trusted by default is best never.

- MUST apply least functionality and least privilege on development endpoints.
- Pinning and changing build tools is held in [Dependency Lifecycle](ownership_lifecycle_containment.md#dependency-lifecycle).

`TRANSVERSE.ENVIRONMENTS.3`

