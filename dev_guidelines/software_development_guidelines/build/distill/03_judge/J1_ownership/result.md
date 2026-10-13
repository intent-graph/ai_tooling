# J1_ownership result

## L1 headline

Judged: OWNERSHIP (L1), 6 L2 nodes (STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES, LICENCE) and 29 L3 nodes (STANCE.1-4, SELECTION.1-6, LIFECYCLE.1-5, CONTAINMENT.1-4, SERVICES.1-6, LICENCE.1-4); records in `judged.md`. Every node is decided with grounds, rejected positions and conditions.
- Pin, nodes judged: all 36 nodes of unit J1_ownership.
- Pin, decisions marked undecided: none.
- Pin, flags raised: F2 LIFECYCLE.3 (release-age cooldown rests on weak evidence), F5 CONTAINMENT.2 (no vendor types in own data: rule inferred, unsourced), F6 LIFECYCLE.2 (resolution rule left to the ecosystem tool); F1, F3 and F4 were settled by review.
- Pin, review fixes applied: n of 7 (n = 7: R01 to R07 applied, none rejected).
- Pin, settled decisions disagreed with: none (J1 has no decided input).
- Claim: ownership is a per-need, recorded decision whose cost is lasting and whose exit is priced in proportion to criticality (grounded for the mechanics, inferred for the proportionality).

## L2 claims

Pin, nodes judged: OWNERSHIP, STANCE, STANCE.1, STANCE.2, STANCE.3, STANCE.4, SELECTION, SELECTION.1 to SELECTION.6, LIFECYCLE, LIFECYCLE.1 to LIFECYCLE.5, CONTAINMENT, CONTAINMENT.1 to CONTAINMENT.4, SERVICES, SERVICES.1 to SERVICES.6, LICENCE, LICENCE.1 to LICENCE.4.
Pin, decisions marked undecided: none.
Pin, flags raised: F2 LIFECYCLE.3; F5 CONTAINMENT.2; F6 LIFECYCLE.2 (one line each in L3); F1 STANCE.4, F3 SERVICES.2 and F4 LICENCE.3 were settled by review.
Pin, review fixes applied: n of 7 (n = 7: R01 to R07 applied, none rejected).
Pin, settled decisions disagreed with: none.

- STANCE (grounded; the STANCE.4 reconciliation inferred): the default is not to add; a dependency or layer needs a stated reason that outweighs its lasting cost (STANCE.1, MAINT L308 agrees with L001, L037); write, adopt, use a built-in or rent is decided per need on coreness, security-criticality and size (STANCE.2, L002, L040, L310); copy only a tiny non-critical surface, depend for cryptography, upstream rather than fork (STANCE.3); build for today and make change cheap, weigh probable use only where a structure is costly to reverse (STANCE.4; MAINT L330 versus L038 reconciled on L330's own condition, inferred; no published-contract example).
- SELECTION (grounded; scaling inferred): explicit written criteria in context, reason recorded, a gate whose form depends on regulation and number of teams (SELECTION.1); fit first, proven technology by default, novelty only where it differentiates and in stages with a reversible entry (inferred; REG-013 supports only the migration commitment) (SELECTION.2); health signals, including maintainers, compatibility promise, version label and scores, are inputs to judgment weighted by replaceability, never verdicts, and a single-maintainer component outside the small, stable, replaceable case needs a recorded compensating reason or exit plan (SELECTION.3); count transitive weight and inline trivial packages (SELECTION.4); reject known unfixed vulnerabilities, verify authenticity and name, require provenance at high criticality, with the rebuild rule stated once in LIFECYCLE.4 (SELECTION.5); vetting depth scales with criticality and audits are delegated and diff-based (SELECTION.6).
- LIFECYCLE (grounded; cooldown inferred): complete manifest, committed lock, install from lock only, hashes (LIFECYCLE.1); pin exactly for deployables, ranges for libraries, number is an estimate and tests the evidence (LIFECYCLE.2); small automated tested updates, security fixes urgent, short cooldown for routine updates (LIFECYCLE.3, F2); controlled channels, mirror by size and criticality, own tooling pinned, publishing accounts protected (LIFECYCLE.4, which also holds the single rebuild rule); continuous inventory, scanning and end-of-life plans, legal duties where a law applies (LIFECYCLE.5).
- CONTAINMENT (grounded; proportionality inferred): buy exit capability only to where insurance beats expected loss, tested exit for critical or regulated functions (CONTAINMENT.1); thin adapter for volatile, substitutable or foreign-model dependencies, direct use for stable standard ones (CONTAINMENT.2, F5); backing services as attached resources (CONTAINMENT.3); isolate risky dependencies and treat third-party responses as untrusted (CONTAINMENT.4).
- SERVICES (grounded; price caps, assurance reports and vendor composition open or inferred): availability target at least your own, SLA as commercial instrument (SERVICES.1); read API stability policy, consume deprecation signals, pin the version, windows are not guarantees (SERVICES.2; the provider's evolution scheme L353 is kept here, major versions with a bounded window or a date-pinned surface each best under its condition); tested data export, switching contract, independent copy (SERVICES.3); processor contract, price owner, licence-control record (SERVICES.4); vendor assessment scaled to criticality, repeated (SERVICES.5); CI and hosting as supply chain, pin to full commit hash, read-only token, no self-hosted runners on untrusted code (SERVICES.6).
- LICENCE (grounded; the linking boundary grounded in part): classify by what is done with the code and by licence family, directional compatibility, SPDX (LICENCE.1); written class policy with a decider, conservative when shipping client or embedded or proprietary, copyleft allowed when hosting only, compliance process (LICENCE.2); AGPL decided separately, separate-component question open (LICENCE.3; the interface test is grounded in part by REG-188, legal review kept); machine-readable licence of own files (LICENCE.4).

## L3 full

Full records, one per node, in `judged.md` beside this file: decision, grounds with row and source ids, positions with forces, rejected positions with the condition under which each would be best, context, certainty, flags, constraints and links.

Pin, nodes judged: OWNERSHIP; STANCE (STANCE.1, STANCE.2, STANCE.3, STANCE.4); SELECTION (SELECTION.1 to SELECTION.6); LIFECYCLE (LIFECYCLE.1 to LIFECYCLE.5); CONTAINMENT (CONTAINMENT.1 to CONTAINMENT.4); SERVICES (SERVICES.1 to SERVICES.6); LICENCE (LICENCE.1 to LICENCE.4).
Pin, decisions marked undecided: none.
Pin, flags raised, in full:
- F1 STANCE.4: settled by review (R01, R02): reconciliation accepted on L330's own condition; maintainer confirmation stays a human step.
- F2 LIFECYCLE.3: the routine-update cooldown rests on one T3 analysis of 10 attacks (REG-036), vendor figures and an unsourced three-day figure; decided as a short cooldown that never delays security fixes (carried as review flag R11).
- F3 SERVICES.2: settled by review (R05): L353 kept on SERVICES.2 as a consumer-facing question, both schemes each best under their condition.
- F4 LICENCE.3: settled by review (R06): the interface test is grounded in part by REG-188; legal review kept.
- F5 CONTAINMENT.2: P5 (no vendor types or identifiers in own stored data or public interfaces without an owned mapping, L345) is inferred, no source states it as a rule (carried as review flag R19).
- F6 LIFECYCLE.2: the resolution rule (L047) is left to the ecosystem tool under the outcome "every upgrade is an explicit, reviewable change recorded in the lock" (carried as review flag R10).
Pin, review fixes applied: n of 7 (n = 7). R01 to R07 applied to `judged.md`, none rejected; see its section "Review applied".
Pin, settled decisions disagreed with: none (J1 has no decided input).
