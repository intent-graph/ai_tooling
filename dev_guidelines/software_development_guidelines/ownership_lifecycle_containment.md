# Ownership: Lifecycle and Containment

## Table of Contents

1. [Dependency Lifecycle](#dependency-lifecycle) _(Lines 23-29)_
   1. [Declare and Lock](#declare-and-lock) _(Lines 32-46)_
   1. [Version Constraints and Resolution](#version-constraints-and-resolution) _(Lines 49-65)_
   1. [Updating](#updating) _(Lines 68-91)_
   1. [Channels, Mirrors and Supply-Chain Integrity](#channels-mirrors-and-supply-chain-integrity) _(Lines 94-115)_
   1. [Inventory, Watching and End of Life](#inventory-watching-and-end-of-life) _(Lines 118-133)_
1. [Containment and Exit](#containment-and-exit) _(Lines 136-141)_
   1. [How Much Reversibility to Buy](#how-much-reversibility-to-buy) _(Lines 144-160)_
   1. [Adapter Between Code and Dependency](#adapter-between-code-and-dependency) _(Lines 163-182)_
   1. [External Systems as Attached Resources](#external-systems-as-attached-resources) _(Lines 185-197)_
   1. [Bounding Runtime Effect and Untrusted Responses](#bounding-runtime-effect-and-untrusted-responses) _(Lines 200-210)_

---

How an adopted dependency is declared, locked, updated, sourced and watched, and how its exit is priced and its effect bounded. Back to the branch index: [Ownership](ownership.md).

## Dependency Lifecycle
<!-- Lines 23-29 -->

Every environment gets the same verified artifacts from a complete manifest and a lock, and
versions are constrained by whether the artifact is deployed or consumed as a library. Updates
are small, frequent, tested and automated with security fixes urgent; artifacts arrive through
controlled channels; the team knows what it depends on and watches it until end of life.
`OWNERSHIP.LIFECYCLE`

### Declare and Lock
<!-- Lines 32-46 -->

Every dependency is declared completely and exactly in a manifest, and a committed lock records
the exact resolved tree with artifact hashes. What runs is what was tested.
`OWNERSHIP.LIFECYCLE.1`

- Dependencies MUST be declared completely and exactly in a manifest and run in an isolated
  environment, never relying on implicitly installed packages.
- A lock recording the exact resolved tree, direct and transitive, MUST be committed.
- CI and production MUST install from the lock only, and the build MUST fail when lock and
  manifest disagree.
- Artifacts MUST be verified by a cryptographic hash recorded in the lock, covering transitive
  dependencies; deploys use an install mode that rejects any artifact lacking a recorded hash
  where the tooling supports it.
- A new developer MUST need only the runtime, the dependency manager and one command.

### Version Constraints and Resolution
<!-- Lines 49-65 -->

Deployables nobody else installs pin all dependencies exactly, with an update bot; libraries
declare ranges and test the range edges. A lock never replaces constraints. A version number is
an estimate of compatibility and tests are the evidence. `OWNERSHIP.LIFECYCLE.2`

- Applications and services nobody else installs MUST pin all dependency types exactly, each
  bump being a reviewable change.
- Libraries MUST declare ranges and MUST test the lowest and newest versions their ranges admit
  in their own CI; the range MUST still exclude known-broken versions.
- A version MUST change only through an explicit, reviewable change to the lock.
- Whichever resolution rule the ecosystem applies, the installed set equals the tested set.

Best instead when: ranges plus a lock for a deployable are best when review capacity is scarce,
but this only delays a bad range; trusting semantic versions as a contract is best when the API
is narrow and well declared. Exact pins in libraries have no defender. Inferred: testing both
range edges, and neutrality toward the resolution rule.

### Updating
<!-- Lines 68-91 -->

Updates are small, frequent, automated, grouped and gated by the project's own tests, with
security fixes applied urgently and separately. `OWNERSHIP.LIFECYCLE.3`

- Each update MUST be gated by the project's own tests (including integration tests for the
  team's usage) and release-note or diff review, and deployed through staged rollouts.
- Fixes for known vulnerabilities MUST be applied urgently, bypassing any scheduled delay, and
  kept separate from feature updates.
- Routine non-security updates of deployables MUST be held for a release-age cooldown of at
  least seven days; security fixes MUST NOT be held.
- Where verification is weak or deployment costly, updating on need is a recorded debt, not a
  policy: see [Technical Debt and Refactoring](evolution.md#technical-debt-and-refactoring).
- After a worm-style supply-chain compromise, every developer credential MUST be treated as
  exposed, lockfiles reviewed and versions pinned to before the incident; rotation follows
  [Response to a Leaked Secret](transverse_config_environments.md#response-to-a-leaked-secret).
- Changes the lock only through the path of [Declare and Lock](#declare-and-lock).

Best instead when: updating only when needed is best as a temporary state while verification is
weak and exposure is lower than the risk of change; immediate updates beat the cooldown when
most updates are security fixes or the pipeline detects malicious content itself; living at head
is best in a monorepo with provider-run downstream tests at organisation scale. Inferred: the
cooldown length and benefit (one analysis), the interim cadence under weak verification, the
post-compromise trigger (one source).

### Channels, Mirrors and Supply-Chain Integrity
<!-- Lines 94-115 -->

Artifacts are obtained only through controlled, trusted channels with lock and hashes. The
supply chain of the team's own tooling is pinned, vetted and changed only through audited change
management. `OWNERSHIP.LIFECYCLE.4`

- Provenance verification MUST be applied recursively; a removed upstream MUST be addressed
  separately by a mirror, cache or vendored copy.
- Any artifact whose binary provenance cannot be confirmed MUST be rebuilt from verified source
  (the single statement of the rebuild rule). Critical infrastructure and supply-chain-targeted
  organisations MUST rebuild every deployed open-source artifact in their own infrastructure.
- The automation's own tools, plugins and descriptors, and build tools and compilers, MUST be
  pinned, vetted, changed only through audited change management, not auto-updated without
  review, and kept on versions that still receive security fixes.
- Two-factor authentication MUST protect publishing accounts of any registry; phishing-resistant
  multi-factor authentication MUST protect developer accounts after compromises.

Best instead when: a controlled channel with an internal mirror is for larger, regulated or
production-critical contexts, direct access with lock and hashes for the rest; rebuilding
everything is too much effort outside the cases above; an immutable public proxy is enough where
the registry guarantees immutability and builds are not production-critical. Inferred: the
tooling pinning rule and the account-protection scope.

### Inventory, Watching and End of Life
<!-- Lines 118-133 -->

The team keeps a machine-generated inventory of what it depends on, direct and transitive and
where deployed, so a disclosed flaw maps to the affected systems in hours.
`OWNERSHIP.LIFECYCLE.5`

- The inventory MUST be scanned continuously against vulnerability databases for as long as the
  software is in service, with a triage and update plan.
- Each component MUST be confirmed maintained and not at end of life, and a plan MUST exist for
  components that stop being maintained.
- Where law applies, due diligence on third-party components, an inventory and reporting of
  component vulnerabilities to their maintainers MUST be done (example: the EU Cyber Resilience
  Act). Inferred: the exact wording of the legal duty.
- Related: [Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code) keeps its
  inventory here; out-of-date and end-of-life dependencies are debt items, see
  [Technical Debt and Refactoring](evolution.md#technical-debt-and-refactoring).

## Containment and Exit
<!-- Lines 136-141 -->

Exit capability is bought only up to where insurance costs less than the expected loss, and a
thin adapter isolates substitutable, volatile or foreign-model dependencies while none is built
for stable standard ones. External systems are attached resources, third-party responses are
untrusted input, and risky dependencies are isolated at runtime. `OWNERSHIP.CONTAINMENT`

### How Much Reversibility to Buy
<!-- Lines 144-160 -->

Lock-in is a spectrum priced by the cost and the likelihood of switching. It is accepted when it
buys a commensurate pay-off, and switching cost is reduced only to where insurance is cheaper
than the expected loss. `OWNERSHIP.CONTAINMENT.1`

- The exit path of a rented service (data export, replacement candidate, contract notice) MUST
  be defined before adopting it, in proportion to its criticality.
- A tested exit and an alternative MUST be required where regulation requires them (example:
  EU financial entities) and for critical functions, where the expected loss of being unable to
  leave exceeds the cost of testing the exit.
- Fed by [Data Export and Switching Terms](ownership_services_licence.md#data-export-and-switching-terms); carried out by
  [Adapter Between Code and Dependency](#adapter-between-code-and-dependency).

Best instead when: minimising portability everywhere is best for long-lived or regulated
systems and critical rented services; elaborate multi-cloud otherwise forfeits the platform and
creates new lock-in. Inferred: the proportionality of the requirement.

### Adapter Between Code and Dependency
<!-- Lines 163-182 -->

A thin wrapper holding only what the project needs separates the code from a dependency or
external system when substitution is plausible or the dependency is volatile,
security-sensitive, single-vendor or modelled differently from the domain. None is built for a
stable standard interface (examples: SQL, SMTP). `OWNERSHIP.CONTAINMENT.2`

- Where a wrapper exists, a vendor type MUST NOT cross the team's public interface.
- External types and parsing of the external payload MUST stay inside the wrapper, in one place
  ([Parse or Validate at the Edge](construction.md#parse-or-validate-at-the-edge)).
- A vendor's identifier MUST be stored only as an attribute of the team's entity that refers
  out, never as the key of the team's data or as a type in its public interface. Inferred: this
  identifier rule.
- Timeouts and retries of remote-call protection are applied here:
  [Protecting Remote Calls](assurance_performance_availability.md#protecting-remote-calls). Carries out
  [Cut by Hidden Decision](construction.md#cut-by-hidden-decision) for dependencies.

Best instead when: a mandatory layer for every dependency adds latency and something to
operate; it is best for multi-stage migrations, differing semantics, critical-path or uncertain
vendors. Direct use is best when the service is core, stable and switching unlikely.

### External Systems as Attached Resources
<!-- Lines 185-197 -->

The location and credentials of a backing or third-party service are configuration, and code
makes no distinction between local and third-party instances, so an instance is swapped by
changing configuration. `OWNERSHIP.CONTAINMENT.3`

- Location and credentials MUST be configuration; where it lives is decided in
  [Configuration and Secrets](transverse_config_environments.md#configuration-and-secrets).
- Code MUST NOT branch on local versus third-party instances; where semantics genuinely differ,
  the difference MUST be modelled in the adapter above.

Best instead when: a real distinction in code is right only where the semantics genuinely
differ.

### Bounding Runtime Effect and Untrusted Responses
<!-- Lines 200-210 -->

The damage a dependency or a third-party response can do at runtime is bounded. `OWNERSHIP.CONTAINMENT.4`

- Every third-party response MUST be validated and sanitised before use, fetched over an
  encrypted channel, redirected only to an allowlist of targets, and capped in the resources
  spent on it ([Parse or Validate at the Edge](construction.md#parse-or-validate-at-the-edge)).
- Risky dependencies MUST be isolated at runtime (sandbox, least privilege) where practical for
  the ecosystem.

Open: how far runtime isolation is practical is not sourced, so the rule applies where
practical for the ecosystem; the response rules are grounded.
