# Inputs from the web architecture guideline

What the web architecture guideline already holds that this guideline reuses or must align with.
Paths are relative to this file. The web guideline awaits the maintainer's review: read it, never
edit it.

## Evidence to merge into the ledger (public sources, already tiered)

Research results under `../../../web_architecture_guidelines/build/research/`, each with L1, L2
and L3 (source register and claims in L3):

- `06_operations/result.md`: testing strategy, delivery, observability, performance.
- `07_architecture_styles/result.md`: boring technology, evolutionary architecture, decision
  records, monolith versus services.
- `05_identity_security/result.md`: only its secrets and supply-chain claims.
- `14_thin_spots/result.md`: audit logging, client error reporting, deletion and history.
- `17_data_contracts/result.md`: contract as artifact, contract testing, schema diff in CI.

The web guideline's consolidated ledger and register: `../../../web_architecture_guidelines/build/distill/02_skeleton/claims_ledger.md`
and `sources.md`; the rows owned by TRANSVERSE nodes are the generic ones. Not yet merged into
`01_consolidate/claims_ledger.md`.

## Decisions to align with, or to state where this guideline differs

- Maintainer decision MD-02 in `../../../web_architecture_guidelines/build/distill/maintainer_decisions.md`:
  interface documentation is always in sync with the implementation, guaranteed by process (one
  origin per fact, the other side generated or checked, review rules, a CI/CD gate on drift);
  description-first or code-first is chosen per project with criteria. Generic, not web-specific.
- Philosophy graph `../../../web_architecture_guidelines/intent_graphs/web_app_philosophy.ig.yaml`,
  branch TRANSVERSE: OPERABILITY.1 (whole-path observability), OPERABILITY.2 (proportioned
  testing), OPERABILITY.3 (reproducible delivery), CONTRACTS (interface descriptions in sync by
  process), EVOLUTION.1 to .5 (explicit decision records, incremental change with fitness
  functions, deployable boundaries, few mature technologies, team-shaped structure).
- Stack graph `../../../web_architecture_guidelines/intent_graphs/web_defaults.ig.yaml`, branch
  PIG-WEB-TRANSVERSE: SECURITY.4 and .5, OPERABILITY.3, .5 and .6, EVOLUTION.3.
- Read nodes with `ig-tool query -g <file> --node <UID>`.

## Division of work once this guideline is stable

The web guideline links its TRANSVERSE nodes to this guideline's graph and keeps only its
web-specific realization (which test level catches what across database, backend and browser;
sourcing for its stack). It needs this guideline's folder name, graph id and graph file path once
they are stable.
