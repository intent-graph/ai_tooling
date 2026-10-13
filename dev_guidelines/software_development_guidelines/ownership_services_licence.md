# Ownership: Services and Licences

## Table of Contents

1. [External Services](#external-services) _(Lines 24-29)_
   1. [Availability Fit and Commitments](#availability-fit-and-commitments) _(Lines 32-45)_
   1. [API Stability and Deprecation](#api-stability-and-deprecation) _(Lines 48-62)_
   1. [Data Export and Switching Terms](#data-export-and-switching-terms) _(Lines 65-81)_
   1. [Commercial and Contract Terms](#commercial-and-contract-terms) _(Lines 84-101)_
   1. [Vendor Assessment](#vendor-assessment) _(Lines 104-123)_
   1. [CI and Hosting Services as Supply Chain](#ci-and-hosting-services-as-supply-chain) _(Lines 126-138)_
1. [Licences](#licences) _(Lines 141-145)_
   1. [Reading and Classifying Licences](#reading-and-classifying-licences) _(Lines 148-158)_
   1. [Policy and Process](#policy-and-process) _(Lines 161-175)_
   1. [Network Copyleft and Separate Components](#network-copyleft-and-separate-components) _(Lines 178-189)_
   1. [Declaring the Team's Own Licence](#declaring-the-teams-own-licence) _(Lines 192-197)_

---

What to check before renting a service, and how licences are read, classified and declared. Back to the branch index: [Ownership](ownership.md).

## External Services
<!-- Lines 24-29 -->

A rented service is chosen on commitments that compose with the team's own target, a stated API
stability promise with defences against its removal, verified export and switching terms, a
known price and contract position, and a vendor assessment matched to criticality. CI and
hosting services count as supply chain. `OWNERSHIP.SERVICES`

### Availability Fit and Commitments
<!-- Lines 32-45 -->

A rented service's availability target must be at least the team's own, because hard
dependencies multiply availabilities. Its SLA is a commercial instrument, not a promise.
`OWNERSHIP.SERVICES.1`

- A service's availability target MUST be at least the team's own.
- Where SLA credits cannot cover the team's loss, the team MUST mitigate by design (fallback,
  redundancy): [Tolerating a Degraded Dependency](assurance_performance_availability.md#tolerating-a-degraded-dependency).
- The internal objective MUST be tighter than the SLA signed or advertised.
- Reachability, latency and errors of each service MUST be monitored as part of adopting it.

Inferred: the remedy-versus-loss mitigation, planning from observed behaviour and per-service
monitoring have no source.

### API Stability and Deprecation
<!-- Lines 48-62 -->

Before depending on a service API, the team reads its stability tiers and deprecation policy and
prefers providers that publish a minimum notice and keep two versions side by side.
`OWNERSHIP.SERVICES.2`

- The stability tiers and deprecation policy MUST be read before depending on the API.
- Machine-readable deprecation signals MUST be consumed and routed to an alert.
- The API version MUST be pinned where the provider allows it, and upgraded deliberately.
- Any stated promise is acceptable to depend on; a published deprecation window is a goal, not a
  guarantee. This section holds the consumer side only; provider policies are in
  [What Counts as Compatible](assurance_interfaces_data.md#what-counts-as-compatible).

Open: whether consumers actually act on deprecation signals is not established; real notice is
inferred to be shorter than the stated policy.

### Data Export and Switching Terms
<!-- Lines 65-81 -->

The team can take its data and integration logic out of a rented service on known terms; leaving
does not depend on the provider's goodwill. `OWNERSHIP.SERVICES.3`

- Export of all the team's data in a commonly used machine-readable format through an open
  interface MUST be verified at selection and tested once before depending on the service.
- A cloud or data-processing provider's contract MUST cover switching (notice and transition
  terms, data return, no punitive egress charges).
- An independent copy of critical data held in a service MUST be kept, and credentials and
  integration logic MUST be kept exportable.
- For managed services and SaaS, what the provider's backups cover, and for whose recovery, MUST
  be verified.
- Feeds the exit price of [How Much Reversibility to Buy](ownership_lifecycle_containment.md#how-much-reversibility-to-buy).

Where law gives export rights (the EU), they add to this; elsewhere the practice stands without
the legal duty. Inferred: the independent-copy advice and the backup consequence.

### Commercial and Contract Terms
<!-- Lines 84-101 -->

The legal and cost position of renting is known before dependence. `OWNERSHIP.SERVICES.4`

- Where a service processes personal data, a written processor contract MUST be in place
  (documented instructions only, confidentiality, security measures, authorised sub-processors,
  assistance with data-subject rights, deletion or return at the end, audit rights), with
  processors giving sufficient guarantees; see [Privacy and Retention](transverse_privacy.md#privacy-and-retention).
  Stated for the EU; apply the local equivalent elsewhere.
- Cost MUST have an owner, and the pricing model, unit economics and egress MUST be understood
  as part of selection.
- For each critical open-source or hosted dependency, who controls its licence MUST be recorded
  and the response to changed terms decided in advance.

Best instead when: a single-vendor project is acceptable for non-competitive end-user use; a
foundation or multi-vendor project is best where the dependency may be read as competitive or
must outlive the vendor. Inferred: price-risk handling (no source on contractual price caps) and
the single-vendor governance rule.

### Vendor Assessment
<!-- Lines 104-123 -->

A vendor's security and supply-chain posture is assessed before depending on it, to a depth that
scales with criticality and data sensitivity, and repeated through the contract life.
`OWNERSHIP.SERVICES.5`

- Assess before depending: authentication options, intrusion evidence with logs retained at
  least six months, bill of materials and open-source governance, vulnerability disclosure
  policy and CVE practice, patch support.
- The assessment MUST be repeated through the contract life, not only at selection.
- A small team without capacity to triage MUST use the uniform baseline checklist for every
  vendor.
- Extends the adoption checks of [Authenticity, Provenance and Known Vulnerabilities at Adoption](ownership_stance_selection.md#authenticity-provenance-and-known-vulnerabilities-at-adoption).

Best instead when: depth scaled by criticality is best when vendors are many and most low-risk;
the uniform baseline is best for small teams without capacity to triage.

Open: how to read third-party assurance reports (evidence of controls, not proof of fit) and
applying the same criteria to non-library tools and platforms have no source; both are
composed. The six-month retention figure is one checklist's.

### CI and Hosting Services as Supply Chain
<!-- Lines 126-138 -->

Build, CI and hosting services execute with the team's secrets and produce what it ships, so
they are held to supply-chain standards. `OWNERSHIP.SERVICES.6`

- Third-party CI components MUST be pinned to an immutable identifier from their official
  source, not a fork, and their source audited (where components are repositories, a full commit
  hash).
- The default token permission MUST be read-only and raised per job; this applies the pipeline
  identity rules of [Credential Lifetime and Pipeline Identity](transverse_config_environments.md#credential-lifetime-and-pipeline-identity).
- Self-hosted runners MUST NOT run untrusted code such as public repositories.

Inferred: the guidance comes from one platform and is generalised to equivalents.

## Licences
<!-- Lines 141-145 -->

A licence is read and classified by what the team does with the code before adoption, a written
class policy with a named decider governs, and network copyleft is decided separately. The
team's own files declare their licence machine-readably. `OWNERSHIP.LICENCE`

### Reading and Classifying Licences
<!-- Lines 148-158 -->

Obligations are triggered by what is done with the code (ship, link, modify, run as a service),
so the licence is read against that. `OWNERSHIP.LICENCE.1`

- The licence MUST be present, clear and acceptable for the intended use before adoption.
- A dependency MUST be classified by licence family and by the team's distribution model.
- Licence variants (the "or later" forms, exceptions) MUST be stated with standard
  machine-readable licence expressions.
- A source-available licence with a field-of-use restriction MUST NOT be treated as open source.
- Compatibility is directional and pair-specific.

### Policy and Process
<!-- Lines 161-175 -->

Licence classes (allowed, notice-only, review-needed, prohibited) are written down by
distribution model with a named decider. `OWNERSHIP.LICENCE.2`

- Classes MUST be written down by distribution model with a named decider, following the
  classification above.
- A defined compliance process with identified roles MUST exist and be kept working over time.

Best instead when: the distribution model picks the policy. Conservative where the team ships
client or embedded software or must keep code closed (for example notice licences allowed,
strong copyleft only server-side or internal, network copyleft, source-available
commercial-restriction and non-commercial licences prohibited); looser, allowing copyleft with
understood obligations, for teams that only host. Inferred: the host-only policy and the process
details.

### Network Copyleft and Separate Components
<!-- Lines 178-189 -->

Network-copyleft code is decided separately from other copyleft, since modifying it and letting
users interact with it over a network triggers a source offer. `OWNERSHIP.LICENCE.3`

- It MUST be decided separately from other copyleft and MUST NOT be accepted by default.
- A separate-component claim MUST NOT be assumed; where the boundary matters it MUST be settled
  with legal review. Pipes, sockets and command-line arguments are normally communication
  between separate programs; intimate exchange of complex internal data structures may make one
  combined work.

Open: applying the interface test to a given case rests with legal review.

### Declaring the Team's Own Licence
<!-- Lines 192-197 -->

The licence and copyright of every file of the team's own output are declared machine-readably,
so tools can check compliance. `OWNERSHIP.LICENCE.4`

- The licence and copyright of every file MUST be declared machine-readably (identifiers in file
  headers, licence texts in a licences directory).
