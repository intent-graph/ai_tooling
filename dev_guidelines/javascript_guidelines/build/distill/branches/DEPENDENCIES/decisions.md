# Decisions for review: branch DEPENDENCIES (purpose: trust)

Selection rule: max, not average (`../../target_hierarchy.md`). Each entry gives the decision, the rejected positions with the condition under which each would win, the grounds and the epistemic state, so the maintainer can overrule. Uids are in `skeleton.md`, rows in `ledger.md`.

## Decisions

### D1. Framework short list (weighty choice, build judgment)

- Decision: the short list is (1) the platform with Web Components and no framework, the default and first candidate; (2) htmx; (3) Lit; (4) Angular; (5) React. The four frameworks are unranked: no admitted source can rank them, and framework documentation grounds facts about that framework only. Node `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST`, rows DEPENDENCIES-048 to DEPENDENCIES-077 (evidence and platform baseline) and the judge record in `skeleton.md`.
- Gates, derived from the guideline's own trust rules: A (mandatory) the candidate states which versions receive security fixes, because the guideline runs only supported versions (TYPES-C45, SUPPLY-C36, SUPPLY-C28); B a documented escape and sanitization model (slot 10 matrix, owned by DEFENSE); C stated governance or maintenance body. A and at least one of B or C. The gates are the build's judgment; no admitted source states them.
- Matrix result: React A yes, B yes, C yes (provisional); Angular A yes (strongest, 24 months), B yes, C no source; Lit A yes, B no source, C yes; htmx A yes, B yes, C no source; Vue A no, B yes, C partial; Svelte A no, B yes, C no source; Solid A no, B no, C partial.
- Rejected, with the condition under which each would win:
  - Keep Vue, as the slot 10 proposal does (holder: slot 10 L2, inferred): wins if an admitted source states a Vue security-fix window and a legal entity or funding. Closest runner-up.
  - Keep Svelte: wins with a supported-versions statement (FW-C27 states none) and a governance source.
  - Keep Solid: wins with a support policy (FW-C29, FW-C30) and a default-escaping description (FW-C15, FW-C16).
  - Rank or choose by popularity: rejected by the register's standing rule; only React (10 percent) has a measured figure (FW-C42, FW-C49). Wins if an admitted per-candidate measurement with method exists (HTTP Archive technology data read as data).
  - Always adopt a framework: wins when a requirement exists that the platform does not meet and the SUPPLY-C27 isolation test confirms it.
- Grounds: T1-restricted facts from each framework's own documentation (single-source each), MDN and the HTML Standard for the platform (T1). Epistemic: known | unvalidated: build judgment over single-source facts | conflict: keep Vue.
- Open: the choice among the four frameworks for a given application depends on rendering strategy, owned by web-architecture, and on the type-layer decision, owned by CONTRACTS.

### D2. Dependency pinning (contested, SUPPLY-C06)

- Decision: the committed lockfile fixes the whole tree and CI installs it frozen; direct dependencies of an application are declared at exact versions so every change is a reviewed diff; versions move only by deliberate update (cooldown, audit triage, lockfile diff review). Node `DEPENDENCIES.CHANGE.2`, row DEPENDENCIES-024, with `STRUCT-C67` rejecting the belief that minor and patch releases are safe.
- Positions: exact pin of a specific immutable version (Node security guide, SRC-078); verified version through the lockfile (OWASP supply-chain sheet, SRC-156); minimum-to-latest range (OpenSSF npm guide v1.1, SRC-154, archived 2023); direct pinning can raise exposure to malicious updates in larger graphs, prefer collective ecosystem pinning (SRC-287, T2).
- Rejected: ranges only (SRC-154): acceptable for a published library whose consumers inherit its declarations, with the lockfile still committed for applications; this scope is inferred from 12_dissent, not stated by a source. Collective ecosystem pinning (SRC-287): a registry-level measure, not actionable by one project; its warning that pinning alone is no defence is kept as fact in SUPPLY-C05.
- Grounds: lockfile committed is confirmed by four T1 sources; exact direct pins by SRC-078 (T1 restricted) and CISA's pre-incident pin (SUPPLY-C41); 44 percent of manifesting breaking changes arrived in minor and patch releases (STRUCT-C67, T2).
- Epistemic: known | conflict: ranges only, SRC-154; collective ecosystem pinning, SRC-287 | unclear: library scope inferred. For review: whether SRC-287's finding should weaken the exact-pin part; the build kept the more demanding practice.

### D3. Release-age cooldown (single T1 assertion, effect open)

- Decision: enable the tool's cooldown where one exists (npm min-release-age from v11.10.0, pnpm minimumReleaseAge default 1440 minutes, Dependabot default 3 days), and keep security updates outside it. Node `PIG-JS.DEPENDENCIES.UPDATE.1`, row DEPENDENCIES-037.
- Rejected: no cooldown (wins for a version fixing an exploited vulnerability, which the security exemption covers); a three-day figure as evidence (OpenSSF concise guide, QUALITY-C46, origin not found: recorded as the body's position only); a longer custom duration (no source, undecided node UPDATE.1.1).
- Grounds: SRC-078 mitigations (one T1 assertion); tool facts SRC-152, SRC-158, SRC-146. SUPPLY-C12 is labelled consensus by the claim table and is relabelled single-source (12_dissent X5). No peer-reviewed measurement exists (SUPPLY-C13; vendor figures SRC-319).
- Epistemic: known | gap: effectiveness unmeasured.

### D4. Install scripts blocked by default, per-package exact-version allowlist

- Decision: keep the default block (npm 12, pnpm 10 and later) and approve reviewed packages by allowlist pinned to the exact version, never disabling the guard globally. Node `PIG-JS.DEPENDENCIES.INSTALL.2`.
- Rejected: global `--ignore-scripts` plus allowlist is acceptable only where the manager still runs scripts by default (npm before v12); running all scripts has no support.
- Grounds: SRC-153 and SRC-158 (manager docs), SRC-078 and SRC-155 (Node and OWASP), SRC-288 (eslint-scope postmortem). Epistemic: known.

### D5. Accept only signed components and generate SBOMs (very demanding, single T1)

- Decision: validate signatures before use, accept only signed components, generate and consume SBOMs in CI. Node `DEPENDENCIES.EVIDENCE.1`, row DEPENDENCIES-018.
- Why flagged: the claim rests on one T1 source (OWASP supply-chain sheet, SRC-156) and no admitted source measures how many npm packages carry signatures a consumer can validate; registry signatures detect mirror tampering only (SUPPLY-C19). Read it as the guideline's ceiling, applied where signatures exist.
- Rejected: reading a signature or provenance as a safety verdict (folklore refuted, SUPPLY-C18, SUPPLY-C19). Epistemic: known.

### D6. htmx major version (contested by scope, FW-C22)

- Decision: pin a supported major and read the documentation of that major; a new adoption takes the newest supported major (4.x). Node `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1`.
- Rejected: 2.x as the current line (the main docs site, SRC-213): wins for an existing 2.x project while 2.x stays supported; same for 1.9.x. The htmx 4.0.0 release year is open (the release page gave the fetch tool no reliable year).
- Epistemic: known | conflict: main docs site documents 2.x | unvalidated: 4.0.0 release date open.

### D7. Production on Active or Maintenance LTS of Node (single T1)

- Decision: production Node.js on an Active or Maintenance LTS only (TYPES-C45, SRC-037). Node `PIG-JS.DEPENDENCIES.UPDATE.2`, with the toolchain pinned to the framework's compatibility table (FW-C24, FW-C26).
- Rejected: Active LTS only is more demanding but no admitted source says Maintenance LTS is insufficient (wins if a T1 source states it); Current in production has no support. Epistemic: known.

### D8. Measured usage is context, never a selection ground

- Decision: usage figures (jQuery 74 to 75 percent, React 10 percent, custom elements 7.8 percent, shadow DOM 2.5 percent, 2024) are context only. Node `PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.4`, rejected row FW-C49. Rejected: ranking by usage; wins only with per-candidate admitted data. Epistemic: known.

### D9. Single-source or inferred decisions that carry the branch (low blast radius each)

- Single T2 ground: SUPPLY-C32 (layered controls, inferred), SUPPLY-C41 (CISA's incident response, recorded as the body's position), SUPPLY-C30 (expired domains, fact), SUPPLY-C23, SUPPLY-C25, STRUCT-C67 (folklore refuted by one study each: `known | unvalidated: single T2 source`).
- Single T1 ground: SUPPLY-C07 (lockfile diff review, inferred from an attack-vector list), SUPPLY-C11 (npm 12 git and tarball defaults, inferred), SUPPLY-C27, SUPPLY-C39, SUPPLY-C33, SUPPLY-C37, TYPES-C07, TYPES-C45, SUPPLY-C21, SUPPLY-C26.

## Undecided nodes

### PIG-JS.DEPENDENCIES.UPDATE.1.1: cooldown length beyond the tool defaults
- State: undecided | missing: no admitted source gives a measured duration.
- Settled by: a peer-reviewed or primary measurement of time-to-removal of malicious package releases, or the origin of the OpenSSF three-day figure (QUALITY-C46).

### PIG-JS.DEPENDENCIES.UPDATE.3.1: failing severity of the audit gate
- State: undecided | missing: no admitted source names a level.
- Settled by: an authoritative statement of which `audit-level` to fail on, or a study linking advisory severity to reachability (SUPPLY-C22 measures noise, not a threshold).

### PIG-JS.DEPENDENCIES.PUBLISH.4: target assurance level of a published package
- State: undecided | missing: no admitted source recommends a SLSA Build level for an npm package; SLSA v1.2 defines levels only (SUPPLY-C33).
- Settled by: a recommendation of a target level by SLSA, OpenSSF or npm, or npm documentation stating the level reached by trusted publishing with provenance.

## Open facts that bound decisions (not nodes)

- Governance has no source for Angular, Svelte, htmx (FW-C35); support policy none for Svelte, Solid, Vue (FW-C27, FW-C29, FW-C30, FW-C26); type support none for htmx (FW-C41); default escaping none for Solid and Lit (FW-C16); measured usage none for six candidates (FW-C49).
- Late candidates that would close them are listed in the slot 10 result: Lit templates documentation, Solid JSX documentation, HTTP Archive technology data, the TypeScript handbook JSX page, the htmx 4.0.0 release page.
