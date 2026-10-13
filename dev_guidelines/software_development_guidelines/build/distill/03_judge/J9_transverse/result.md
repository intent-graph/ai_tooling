# Result: unit J9_transverse

## L1 headline

J9_transverse judged 36 nodes (the L1 node TRANSVERSE, 6 L2 roll-ups, 29 L3): TRANSVERSE.DOCS (.1-.5), TRANSVERSE.SECURITY (.1-.6), TRANSVERSE.SECURITY_MONITORING (.1-.5), TRANSVERSE.PRIVACY (.1-.4), TRANSVERSE.CONFIG (.1-.6), TRANSVERSE.ENVIRONMENTS (.1-.3), reading the settled ASSURANCE.DOCS_SYNC, SECURITY and DATA_INTEGRITY records of J3 as input (grounded).
Decisions marked undecided: none. Settled decisions disagreed with: none (two maintainer-codified rows are decided against in part with their winning condition: the dated change log in the code header, DOCS.3, and hand-kept line-number tables of contents, DOCS.2; inferred).
Flags raised (8): (T1) DOCS.3 mandatory header change log kept only where repository history is invisible; (T2) DOCS.4 condition under which a generated changelog is best, open (narrowed); (T3) SECURITY.2 no source shows maturity scores or ASVS levels reduce incidents, open; (T4) SECURITY.6 bounty yield open; (T5) SECURITY_MONITORING.1 security events logged regardless of the ASVS level, inferred; (T6) PRIVACY.3 how a locked backup is put beyond use and whether erasure must reach logs and backups, open and contested; (T7) CONFIG.1 the token-acceptance clause of L1535 is a boundary rule on the wrong node, relocation proposed; (T8) CONFIG.2 custody separated from delivery channel, this judge's reconciliation, inferred.
Review fixes applied: 10 of 10 (F01 to F10); flags T1, T5, T6, T7, T8 and F11 to F13 left to the Opus pass; T2 narrowed to the condition under which a generated changelog is best (open).
Shape of the answer: the two index nodes (DOCS, SECURITY) add only authoring, programme and intake practice, everything else points to ASSURANCE (MD-03); most "positions" are layers of one practice, with context stated only where a row shows it moves the answer.

## L2 claims

Each claim is marked grounded, inferred or open. Full records: `judged.md`.

Documentation (index of ASSURANCE.DOCS_SYNC)
- DOCS.1 Documentation volume is a recorded, budgeted choice sized by consumers, life and turnover (minimal; living; docs-as-code with gates); writer effort goes to cross-boundary documents and shared guidance, stated as an outcome, not a rule on who writes (grounded for positions, inferred for the context mapping and for the causal reading; generated-output rule now a pointer to ASSURANCE.DOCS_SYNC.3).
- DOCS.2 Small modular documents by reader need, reached from an index, improved in small increments; line-number tables of contents only if tool-generated and checked (grounded; the machine-only condition is inferred).
- DOCS.3 Layered depth and audience split; why-only inline comments; structured header only for units with many callers; history stays in version control except where it is invisible (grounded for layering; inferred for the header change-log decision, flag T1).
- DOCS.4 Human-written reader-facing changelog by change type, Unreleased filled in the change; commit-generated list may seed, not be the record because commit logs are noisy (grounded, REG-162; only the condition where a generated list is best is open, flag T2 narrowed).
- DOCS.5 Every rule records its basis; induced from real code in a mature codebase, deduced from principles otherwise; an overriding rule states what it overrides (inferred, single maintainer source).

Security programme (index of ASSURANCE.SECURITY)
- SECURITY.1 Anchor a published framework as an outcome list, chosen by the question: ASVS for requirements and verification, SAMM or SSDF for a programme, BSIMM only as peer evidence (grounded for roles, inferred for the mapping).
- SECURITY.2 Maturity model run as a cycle with per-practice targets; scores measure activity, not outcomes, so pair with outcome measures, time to detect held in MON.4 (grounded for cycle and targets, inferred for the pairing, open on whether scores reduce incidents, flag T3).
- SECURITY.3 Model risk at design and on every design change touching sensitive data, authentication, access control, credentials or a trust boundary; depth by risk; four questions; tracked (grounded; the trigger is inferred).
- SECURITY.4 Explicit security responsibility, owned from the top, role-based training (grounded, one source family).
- SECURITY.5 One loop for every found vulnerability: confirm, assess, prioritize, remediate in a stated time, learn (learning stated once in ASSURANCE.SECURITY.7) (grounded, single source; the stated rule and time are inferred).
- SECURITY.6 Publish a disclosure policy (without bounty by default) with channel, response and fix times and security.txt; bounty only with mature triage and wide attack surface; penetration test alone only when outsiders cannot reach the system (grounded; bounty yield open, flag T4).

Security monitoring and audit trail
- MON.1 Log the listed security events and every automated action; data changes belong to the audit trail; log regardless of the assurance level (grounded for lists, inferred for the last, flag T5).
- MON.2 Who, what, when, where on every entry; one vocabulary and format; ISO 8601 UTC; synchronized server clocks; receipt time for client events (grounded; receipt time inferred).
- MON.3 Protect logs (injection, tamper, access, separate system), never log secrets or unneeded personal data (pseudonymisation held in PRIVACY.1), treat client events as untrusted (grounded).
- MON.4 Alert and escalate in near real time, detect logging stopping, manage time to detect with a measured target, keep detection rules tool-neutral where the platform may change (grounded for alerting, inferred for tool-neutral rules).
- MON.5 Security event log and business audit trail are separate; audit written in the same transaction, tamper-resistant for high-value transactions, two dates, mechanism by query frequency (inferred for the split, grounded for the rest).

Privacy and retention
- PRIVACY.1 Minimise by purpose, classify with safeguards per level, protect by design, pseudonymise investigation logs, no personal data in trace context (grounded).
- PRIVACY.2 Retention is a recorded decision per purpose and class, automated deletion; legal minimum for logs holding personal data, longer tiered retention for pseudonymised logs with long dwell time (grounded; no source gives a period, open).
- PRIVACY.3 Deletion by the reason the data is kept (recovery and audit form per ASSURANCE.DATA_INTEGRITY.3; temporal model and partition drop held here); an inventory of copies with an erasure path per class; backups put beyond use until overwritten, subject told (inferred for the rule, open for locked backups, flag T6).
- PRIVACY.4 Privacy as risk through a framework; assessment before high-risk processing; breach determination and record within a stated clock (grounded as to purpose, inferred for the neutral restatement).

Configuration and secrets
- CONFIG.1 Configuration apart from code and package, secrets apart from configuration, one build for every environment; the token-rejection clause of L1535 carried but proposed for relocation (grounded; flag T7).
- CONFIG.2 Non-secret configuration versioned and reviewed, applied at deploy; secrets from a managed store, injected as environment values when the environment is not exposed, as files or API for high criticality or live rotation (grounded for positions, inferred for the split, flag T8).
- CONFIG.3 Granular independent values; a named environment bundle only for a few fixed environments; code never branches on environment name (grounded for granular, inferred for the rest).
- CONFIG.4 One managed secrets solution, least privilege per service, automated lifecycle, every access audited with a recorded log period set under PRIVACY.2 (grounded; 90 days queryable is one source's figure).
- CONFIG.5 Short-lived dynamic credentials where supported; every pipeline and automated identity federated, scoped per environment and outside code-executing environments (grounded).
- CONFIG.6 A leaked secret is compromised: revoke first, rotate automatically, remove, investigate from audit logs (grounded, single source).

Development environments
- ENV.1 Separate and isolate environments in instance and credentials, match in kind and version (grounded; parity reconciliation inferred).
- ENV.2 Environment defined as versioned code, reproducible from a clean machine; cheapest mechanism that gives the needed reproducibility (grounded for features, inferred for the ladder).
- ENV.3 Development endpoints and toolchain hardened and monitored as an attack surface (grounded, single source).

Pinned (word for word). Nodes judged: 36, listed in L1. Decisions marked undecided: none. Flags raised: T1 to T8 as in L1. Settled decisions disagreed with: none. Review fixes applied: 10 of 10.

## L3 full

Pinned (word for word). Nodes judged: TRANSVERSE; TRANSVERSE.DOCS (.1-.5); TRANSVERSE.SECURITY (.1-.6); TRANSVERSE.SECURITY_MONITORING (.1-.5); TRANSVERSE.PRIVACY (.1-.4); TRANSVERSE.CONFIG (.1-.6); TRANSVERSE.ENVIRONMENTS (.1-.3). Decisions marked undecided: none. Flags raised: (T1) DOCS.3; (T2) DOCS.4; (T3) SECURITY.2; (T4) SECURITY.6; (T5) SECURITY_MONITORING.1; (T6) PRIVACY.3; (T7) CONFIG.1; (T8) CONFIG.2. Settled decisions disagreed with: none. Review fixes applied: 10 of 10.

The full records (decision, grounds with row and register ids, positions, rejected with winning conditions, context, certainty, flags, constraints, links) are in `judged.md` beside this file, one record per node in tree order. This level adds the reasoning behind the choices that need it.

Method (grounded). Rows in full were read for all 74 routed ledger rows (L158 to L1535 as listed in the branch record); decided input from J3: ASSURANCE.DOCS_SYNC.1-.4, SECURITY.1, .2, .5, .6, .7, DATA_INTEGRITY.1, .3. Under MD-03 the two index nodes were judged only for what ASSURANCE does not hold: authoring, organisation and budget for DOCS; anchor, modelling, ownership and vulnerability intake for SECURITY. Duplicated rows kept apart by the ledger (L158 with L1192; L257 with L1239) are decided once.

Why most positions are layers, not rivals (inferred). In DOCS.2, SECURITY.1, MON.3, MON.5 and CONFIG.5 the listed positions answer different questions or sit at different layers; the decision states each layer once and the condition only where a row shows the answer moves (DOCS.1 life of the system; SECURITY.1 scope; SECURITY.3 criticality; SECURITY.6 triage and surface; PRIVACY.2 personal data in logs and dwell time; CONFIG.2 criticality; CONFIG.3 number of deployments; CONFIG.5 services and criticality; ENV.2 skill mix and languages). Where two positions genuinely compete, one is chosen with the other's winning condition (DOCS.3 header; PRIVACY.2 log retention; CONFIG.3 bundles).

The choices that need defending.
- DOCS.3 (T1, inferred): the maintainer row wants a mandatory change log in every header. The ledger records partial tension with version control (L133), one canonical source (L218) and agreement with dating (L216). The record keeps the structured header only for units with many callers and keeps history in version control except where readers cannot see it: the row's own winning condition.
- DOCS.2 (inferred): hand-kept line counts and line-number tables of contents rot according to the ledger, so they are allowed only if a tool generates and checks them (ASSURANCE.DOCS_SYNC.4 holds the check).
- DOCS.4 (T2, narrowed): REG-162 grounds the reason against commit-generated lists (noise; commits document source evolution); only the condition under which they would be best is inferred and open.
- DOCS.5 (inferred): the override note is the grounded core common to induced and deduced bases; the choice of basis follows the row's only condition, maturity of the codebase.
- SECURITY.2 (T3, open): no source read shows maturity scores or ASVS levels reduce incidents; the record states what a score measures and pairs it with outcome measures.
- SECURITY.6 (T4, open): the day counts (14 and 60) are one project's criteria, kept as reference values; no source compares bounty yield.
- MON.1 (T5, inferred): the ASVS note says an application held to level 1 is not required to log security events; the record separates what the standard verifies from what to log, on the link from logging to detection (L1146) and breach determination (L1159, inferred).
- MON.4 (inferred): about 200 days average dwell time is a dated figure; the record asks for a measured, own figure.
- PRIVACY.2 (open): neither source gives a retention period; both agree it is a recorded decision bounded by a legal, regulatory, contractual or purpose limit.
- PRIVACY.3 (T6, open and contested): the per-reason deletion rule (L1258) is an inferred synthesis consistent with ASSURANCE.DATA_INTEGRITY.3 (archive over flag unless undelete is a feature); how erasure reaches logs and backups is open in the ledger, and how a locked backup is put beyond use is addressed by no source read.
- CONFIG.1 (T7): L1535 is a JavaScript-guideline row; its secrets half equals L158, its token-rejection half is a verification rule at the boundary (grounded by two T1 sources) that does not belong to configuration. The clause "audited platform mechanisms" has no grounding of its own; audit of access is in CONFIG.4 and never-log in MON.3. The prior JavaScript verdict was treated as one position and re-examined.
- CONFIG.2 (T8, inferred): the sources contest env variables against a store or files, and Google packages configuration with the binary. The record separates custody (always the managed store, CONFIG.4) from the last-metre channel (variable or file), and keeps non-secret configuration out of the artifact so that one build serves every environment. The leak vectors of environment variables are inferred in the ledger, not read.
- ENV.2 (inferred): the cheapest mechanism that meets the reproducibility needed is a ladder from the stated costs and winning conditions; Nix host and kernel limits are inferred, not stated.

Scope notes (grounded). Regulated contexts are deferred (MD-05): the EU text in PRIVACY.1 to .4 is restated as neutral practice and legal obligation itself is not decided. The L1 node TRANSVERSE was judged here because J9 is the only unit of its branch; its roll-up and the ROOT roll-up are left to wave 3 for review.

Stack pointers kept out of decisions (grounded): ASVS level shares 20%, 50%, 30% (L1121); Kubernetes ConfigMap and Secret, Vault leases, GitHub Actions OIDC, Dev Container, Nix; PostgreSQL trigger and partition detail restated neutral (L1251, L1257).
