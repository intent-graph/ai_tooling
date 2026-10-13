# Ownership: Stance and Selection

## Table of Contents

1. [Necessity and Default Stance](#necessity-and-default-stance) _(Lines 24-29)_
   1. [What a New Dependency or Layer Must Earn](#what-a-new-dependency-or-layer-must-earn) _(Lines 32-44)_
   1. [Write, Adopt or Rent per Need](#write-adopt-or-rent-per-need) _(Lines 47-67)_
   1. [Bringing Code Inside - Copy, Vendor, Upstream](#bringing-code-inside---copy-vendor-upstream) _(Lines 70-86)_
   1. [Speculative Building and Probable Use](#speculative-building-and-probable-use) _(Lines 89-102)_
1. [Finding, Profiling and Selecting](#finding-profiling-and-selecting) _(Lines 105-110)_
   1. [Evaluation Process and Admission Gate](#evaluation-process-and-admission-gate) _(Lines 113-130)_
   1. [Fit, Maturity and Novelty](#fit-maturity-and-novelty) _(Lines 133-148)_
   1. [Project Health and Compatibility Signals](#project-health-and-compatibility-signals) _(Lines 151-169)_
   1. [Dependency Weight](#dependency-weight) _(Lines 172-184)_
   1. [Authenticity, Provenance and Known Vulnerabilities at Adoption](#authenticity-provenance-and-known-vulnerabilities-at-adoption) _(Lines 187-206)_
   1. [Vetting Depth and Delegated Audit](#vetting-depth-and-delegated-audit) _(Lines 209-225)_

---

Whether to add a capability at all, how to decide between write, adopt and rent, and how a candidate is judged and admitted. Back to the branch index: [Ownership](ownership.md).

## Necessity and Default Stance
<!-- Lines 24-29 -->

The default is not to add. A dependency or layer enters only when a stated reason outweighs its
lasting cost, and each need is decided between writing, adopting and renting. Carried code stays
tied to its origin, and design effort goes to today's need except where a structural choice is
costly to reverse. `OWNERSHIP.STANCE`

### What a New Dependency or Layer Must Earn
<!-- Lines 32-44 -->

A new dependency or layer is justified by a stated reason before its quality is assessed. It is
a lasting liability (maintenance, upgrades, security exposure, platform shifts), not a one-time
saving. `OWNERSHIP.STANCE.1`

- The reason MUST be written before the quality evaluation starts.
- A layer MUST NOT be created unless at least one strong reason outweighs its cost. Reasons that
  can: reuse across consumers; hiding internals behind a business-level verb; keeping a query
  tunable by its owner; enforcing integrity once.

Best instead when: defaulting to a layer is right only where those reasons already hold (for
example integrity enforced once), which is the rule above, not a default.

### Write, Adopt or Rent per Need
<!-- Lines 47-67 -->

Each need is decided explicitly between a platform built-in, a vetted component, a rented
service and in-house code, with no default either way. `OWNERSHIP.STANCE.2`

- Built-in that meets the need: preferred, because it adds no new owner.
- Vetted component or rented service: for complex, security-critical or non-core needs
  (cryptography and protocols are the standing examples).
- In-house code: for core functions, needs no third party meets better, and small stable
  functionality.
- Custom code chosen over a built-in or a vetted component MUST carry a recorded reason. The
  missing capability MUST be recorded, and the choice revisited if the need shrinks to what the
  built-in does.
- Renting MUST pass the same cost test as adopting, plus the control cost; the export and
  switching terms are priced in [Data Export and Switching Terms](ownership_services_licence.md#data-export-and-switching-terms).

Best instead when: always reusing is best for security-critical or non-core needs; always
minimising is best for small, stable, long-lived functionality; renting broadly is best only
where the lock-in pay-off is commensurate (see [How Much Reversibility to Buy](ownership_lifecycle_containment.md#how-much-reversibility-to-buy)).
Coreness (does the function carry competitive advantage) moves a need from adopt or rent
toward write. Inferred: the built-in preference and the rule for renting.

### Bringing Code Inside - Copy, Vendor, Upstream
<!-- Lines 70-86 -->

Code is copied or reimplemented only for a tiny used surface of non-security-critical code.
Otherwise it is consumed from a registry with a lock, or vendored when the team has the tooling
to carry it. `OWNERSHIP.STANCE.3`

- Copied or vendored code MUST keep a record of its origin and version.
- Fixes MUST go upstream and MUST NOT live in a private fork, so carried code does not silently
  diverge.
- Cryptography and protocols MUST depend on the vetted component, not on a copy.
- Same decision as [Write, Adopt or Rent per Need](#write-adopt-or-rent-per-need): this is one
  mode of it.

Best instead when: vendoring is the default only with the tooling and the scale of a large
codebase; copying everywhere loses upstream fixes beyond the tiny, non-critical case; depending
absolutely, even for a handful of lines, costs more than it saves. Inferred: the scope of the
cryptography exception and the vendoring condition.

### Speculative Building and Probable Use
<!-- Lines 89-102 -->

Functionality, or a substitute for a dependency, is not built for presumed future needs; effort
goes into making change cheap (tests, refactoring, continuous delivery). Where a structural
choice is costly to reverse, probable use is part of today's requirement and is weighed in the
choice, without speculative optimisation. `OWNERSHIP.STANCE.4`

- Functionality MUST NOT be built for a presumed future need.
- A structural choice that is costly to reverse MUST be weighed against probable use when it is
  made. Example: the shape of a very large stored data set.

Best instead when: designing for probable use as a general rule is wrong because speculation is
usually wrong and adds complexity; it is best only where reversal is costly. Cheap change means
build for today. Inferred: the reconciliation of the two halves rests on one source.

## Finding, Profiling and Selecting
<!-- Lines 105-110 -->

A candidate is judged against explicit written criteria in its intended context, and the reason
is recorded. Fit comes first and novelty is spent sparingly. Health, weight and provenance
signals are inputs to judgment weighted by criticality and replaceability; vetting depth scales
with criticality and exposure. `OWNERSHIP.SELECTION`

### Evaluation Process and Admission Gate
<!-- Lines 113-130 -->

Every dependency is judged against an explicit written criteria set in the context of its
intended use, and the reason for each non-trivial selection is recorded. `OWNERSHIP.SELECTION.1`

- Criteria MUST be written and repeated when the use changes substantially.
- The reason (alternatives, criteria, accepted risks) MUST be stored as a decision record where
  later maintainers find it, see [Decision Records](evolution.md#decision-records).
- A dependency MUST enter only through the gate. Aggregator catalogues serve discovery and first
  screening only.
- Gate: a central sanctioned list where many teams, regulation or high criticality are involved;
  otherwise a reviewed proposal with light visibility.
- Carries out [What a New Dependency or Layer Must Earn](#what-a-new-dependency-or-layer-must-earn).

Best instead when: free team choice is best for small teams under low regulation; the central
list is best for regulated or high-criticality contexts and many teams. Ad hoc selection is not
a position worth keeping. Inferred: written selection and recorded reasons rest on one study
and a synthesis.

### Fit, Maturity and Novelty
<!-- Lines 133-148 -->

Selection is for fit to the real requirements. Proven technology the team already operates is
the default, because its failure modes are known. `OWNERSHIP.SELECTION.2`

- Before novelty is spent, why the existing tool cannot solve the problem MUST be documented.
- Novelty MUST be introduced in stages (limited production trial, then adopt or hold) with an
  exit or migration plan.
- The perpetual operating cost of a new technology MUST be weighed against the convenience of
  adoption.
- Narrows [What a New Dependency or Layer Must Earn](#what-a-new-dependency-or-layer-must-earn).

Best instead when: a standing trial ring (assess, trial, adopt, hold) is best for an
organisation with capacity for experiments and tolerance for churn; small, operations-heavy or
long-lived systems stay at the default. Inferred: the reconciliation of staging with
boring-first, and the reversible entry.

### Project Health and Compatibility Signals
<!-- Lines 151-169 -->

Observable health signals (recent activity, responsiveness, disclosure policy, compatibility
promise, maintainer diversity) are inputs to judgment, never the verdict, weighted by how
critical and how replaceable the component is. `OWNERSHIP.SELECTION.3`

- Several maintainers from several organisations MUST be required when the component is on a
  critical path or hard to replace.
- A single-maintainer component outside the small, stable, easily replaced case MUST carry a
  recorded compensating reason or an exit plan.
- A popularity or aggregate score MUST NOT be treated as proof of quality or fit.
- A pre-1.0 label is a prompt to check release history and compatibility policy, not an
  automatic rejection.
- Feeds the range and pin choices of [Version Constraints and Resolution](ownership_lifecycle_containment.md#version-constraints-and-resolution).

Best instead when: gating on a score is best only at a scale where per-package review is
impossible, and then as a screen; a multi-maintainer requirement for everything is wrong, it is
for critical or hard-to-replace components. Inferred: the pre-1.0 stance and the screen-at-scale
remark.

### Dependency Weight
<!-- Lines 172-184 -->

The weight a candidate drags in is part of its cost: transitive dependencies, tiny packages and
the concentration of maintainer accounts on its registry. `OWNERSHIP.SELECTION.4`

- Transitive dependencies MUST be counted as part of a candidate's cost.
- Trivial functionality the team can own in a few lines MUST be inlined instead of taken as a
  package.
- The registry's maintainer-account concentration MUST be counted as part of the exposure.

Best instead when: a small shared package is right where it carries non-trivial, tested
behaviour that avoids a real error risk (cryptographic or parsing helpers). Inferred: the
evidence comes from one ecosystem and is generalised.

### Authenticity, Provenance and Known Vulnerabilities at Adoption
<!-- Lines 187-206 -->

Before adoption, what is adopted is verified to be the thing that was vetted: no known unfixed
vulnerability for the intended deployment, authentic source and name, and provenance per
component. `OWNERSHIP.SELECTION.5`

- A candidate whose current version has known unfixed vulnerabilities for the intended
  deployment MUST be rejected or deferred.
- Authenticity MUST be verified: official source over a secure link, signatures where available,
  the name checked against look-alikes and compromised forks, and a generated or suggested name
  resolved to the intended vetted package.
- Provenance (bill of materials, source composition, signatures) MUST be obtained for
  high-criticality use, and integrity checks applied; elsewhere it is a preferred signal.
- Where binary provenance cannot be confirmed, the rebuild rule of
  [Channels, Mirrors and Supply-Chain Integrity](ownership_lifecycle_containment.md#channels-mirrors-and-supply-chain-integrity) applies.
- The state recorded here is the baseline kept current by
  [Inventory, Watching and End of Life](ownership_lifecycle_containment.md#inventory-watching-and-end-of-life).

Best instead when: requiring provenance for every component is best only at high criticality,
because ecosystem coverage is partial (inferred).

### Vetting Depth and Delegated Audit
<!-- Lines 209-225 -->

Hands-on vetting depth scales with criticality and exposure, risk being cost times probability
of each bad outcome. `OWNERSHIP.SELECTION.6`

- Low-criticality replaceable parts: metadata and score checks.
- Components that handle untrusted input, credentials or cryptography MUST get the candidate's
  tests run, sandboxed behaviour tests and code review for install scripts, exfiltration,
  obfuscation and unfinished security gaps.
- A candidate MUST be tested in isolation for unexpected indirect dependencies.
- Example code shipped with a package MUST be treated as untrusted until reviewed.
- Audits by trusted organisations are reused and only version differences reviewed.
- Carries out the rule that consumed code gets the same verification as own code:
  [Secrets and Consumed Code](assurance_docs_security.md#secrets-and-consumed-code).

Best instead when: a full manual audit of every dependency is never the rule; it is for the
high-criticality components only. Inferred: the scaling rule; the individual checks are
grounded.
