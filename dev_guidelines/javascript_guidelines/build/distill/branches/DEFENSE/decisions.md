# Decisions for review: branch DEFENSE (step 5b)

Every decision below settled a contested topic or a weighty choice, or rests on a single source. The selection rule is max, grounded: the most demanding practice that serves safety and that an admitted source supports (`../../target_hierarchy.md`). Each entry names the decision, the rejected positions with the condition under which each would win, and the grounds. Claim ids point to `claims.md` in this folder; ledger rows are in `ledger.md`. Certainty words follow the build rule: grounded, inferred, open.

## Part A. The cut and the conventions (decided by this agent, to be confirmed)

**A1. The partition of DEFENSE (weighty, inferred).** Six children, cut by what hostile data becomes or attacks, not by browser versus server: `DOM` (markup, script and navigation in the page), `ORIGIN` (boundaries between origins), `INJECTION` (instruction or location for an interpreter outside the page, six classes), `PROTOTYPE` (keys that rewrite the object model), `SECRETS` (randomness, crypto, secrets, leakage), `HOST` (the Node process under hostile input). Why not browser versus server: five of the six classes cross it (code from strings, prototype pollution, ReDoS, URL validation, secrets), so a browser or server cut would place one principle twice and break P5. Why not one node per slot: slot 13 is a gap round, its nine topics belong with the topics of slots 05 and 06 they complete. Rejected cut: attack-surface only (browser, server, supply): would win if the guideline had separate browser and Node readers; the language-swap test and P5 favour the injection-class cut. Certainty: inferred.

**A2. Graph placement rule (inferred).** The extraction `level` decides the graph: `principle` and `js-principle` statements go to `js-philosophy`, `practice` and `decision` statements to `pig-js-defaults`, with these exceptions: demoted or mechanism-only claims become `fact` rows in the defaults graph; API-specific rules tagged `js-principle` (RUNSEC-C02, C13, C16, C22, C23, C27, C31, C35, SRVSEC-C39, C43, C53, C64; SRVSEC-C56 stays in the philosophy graph as a parser-differential principle) sit in the defaults graph; refuted beliefs sit where the belief lives. Rejected rule: the language-swap test applied sentence by sentence: would win for an editor who prefers a minimal philosophy graph, at the cost of moving about twenty hazard statements out of it.

**A3. One role per claim (certainty: grounded as a constraint of the ledger format).** A claim that is both a practice and a refutation of a belief carries one role; where the claim states the node's choice or its condition it keeps that role and the belief appears in the statement (RUNSEC-C47, C33, C09 and DOMSEC-C47); where its main content is the refutation it is a `rejected` row (18 rows). Folklore tags of slot 13 (SRVSEC-C01, C04, C23) were not audited by `12_dissent`, so those three rejected rows are inferred.

**A4. Deferred to web_architecture (grounded by routing notes).** DOMSEC-C26, C29, C59, C60, FW-C04, FW-C14, SRVSEC-C38 and DOMSEC-C35 are `deferred` with planned boundary links. DOMSEC-C28 stays as a `rejected` row (the belief that an allowlist CSP stops XSS) because the guideline states what not to believe, while the nonce policy itself is the sibling's. DOMSEC-C35 conflicts mildly with the register: SRC-111 is restricted to a code-level rule, yet routing marks the claim web-architecture; resolved by deferring the claim and keeping its code-level mechanism as a decision (DOMSEC-C36, no secrets in Web Storage). Overrule if the maintainer wants the token rule stated here.

## Part B. Contested topics decided by the max rule

**B1. Trusted Types default policy (DOMSEC-C17; node `PIG-JS.DEFENSE.DOM.4`).** Decision: named policies; the default policy only for migrating legacy code and for third-party code that cannot be changed. Positions: MDN and web.dev (SRC-120, SRC-267): transitional or last resort; Roth et al., USENIX 2024 (SRC-269, T2): with third-party code only a default policy works in practice. Rejected: default policy as normal practice, wins when the page loads third-party code that cannot pass typed values, which the decision already allows as the stated exception. Grounds: mechanism that a default policy is invoked implicitly for every string reaching a sink (grounded). Epistemic state: `known | conflict`.

**B2. setAttribute (DOMSEC-C25, with C04; `DOM.1`).** Decision: never set event-handler attributes from untrusted data; setAttribute is not unconditionally safe. Rejected: OWASP DOM XSS sheet (SRC-108, T1 restricted) says setAttribute is a safe construction method; it wins for attribute names that are not event handlers and whose values are not script, a condition not read verbatim in MDN. Grounds: DOMSEC-C04 (OWASP, consensus) and the MDN Trusted Types sinks list. Certainty: grounded for the positions, open for the MDN condition, which must be read verbatim before the final wording. Epistemic state carries `unvalidated: MDN TrustedScript condition inferred`.

**B3. target=_blank (DOMSEC-C47; `ORIGIN.2`).** Decision: write `rel="noopener noreferrer"` explicitly. Rejected: HTML Standard (SRC-103): noopener is implied unless `rel=opener`; wins on browsers implementing the default and for links where the Referer may be sent. The max rule takes the explicit form as harmless and covering older browsers (inferred, condition not read from a source).

**B4. Permission model (RUNSEC-C38; `HOST.1`).** Decision: a seat belt for trusted code, narrow grants, patched Node, never the only control. Positions: permissions API and threat model (SRC-128, SRC-140, T1): no guarantees against malicious code; best-practices page (SRC-078, T1 restricted): can help contain compromised dependencies. Rejected: containment of hostile dependencies by the model: wins only if Node later documents guarantees; CVE-2025-55130 and CVE-2026-58043 show over-grants. The inconsistency inside Node's own pages is carried forward, not hidden. Stability labels differ between the permissions page and the CLI page (open).

**B5. SQL identifiers (SRVSEC-C18; `INJECTION.3`).** Decision: allowlist mapping or query redesign. Rejected: escaping with pg-format (node-postgres docs, SRC-335), kept as `acceptable-when` for names that are genuinely dynamic, such as DDL; OWASP calls escaping fragile (SRVSEC-C19).

**B6. Native Sanitizer API against a sanitizer library (DOMSEC-C08, C11; `DOM.3`).** Decision: `setHTML` where available, a reputable library as the fallback, sanitize last. Rejected: library first, wins where target browsers lack `setHTML`, which is the stated fallback condition. The OWASP and MDN grounds for naming DOMPurify are not independent (OWASP is cited by MDN), and the register forbids grounding a DOMPurify preference on its own README or advisories. The advice to keep it current is inferred and was demoted to a fact (see Part C).

**B7. Freezing built-ins against never modifying them (RUNSEC-C09, X1 of the dissent audit; `PROTOTYPE.3`).** Decision: freeze application-owned configuration (shallow); lock down built-ins only in high-sensitivity code tested for breakage. Rejected: never freeze built-ins (SUBSET, LANG-C14): wins for general code, because freezing blocks later polyfills (inferred). Conflict link proposed to SUBSET.

**B8. Null-prototype forms (RUNSEC-C05, X3).** Decision: Map or Set first, `Object.create(null)` second as `acceptable-when`; the literal `{ __proto__: null }` is the weaker form (OWASP: last resort; MDN lists both).

**B9. Environment variables for secrets (RUNSEC-C47).** Decision: a weaker channel, acceptable only when no dedicated mechanism is possible. OWASP's passage is written in a container context; process-wide read access is inferred from the threat model. Agreement is majority.

**B10. Non-backtracking regex engine (RUNSEC-C33).** Decision: prefer one where available, do not assume V8 offers one. Status is as of 2021 (V8 blog); the current status was not checked and is open.

**B11. Dynamic evaluation (RUNSEC-C14 to C18, LANG-C49).** Decision: never evaluate untrusted strings. Rejected: Google's code-loader exception (a style-guide position, not evidence), `acceptable-when` for loaders the application itself writes; indirect strict eval, `acceptable-when` only when evaluation is unavoidable, since it reduces scope exposure and removes no injection risk.

**B12. SSRF: allowlist against deny-list (SRVSEC-C28, C31).** Decision: allowlist, request built by the server. Rejected: OWASP's minimum deny-list, `acceptable-when` an allowlist is impossible; deny-lists miss encodings and new ranges.

## Part C. Restriction demotions (grounded against `build/audit/source_register.md`)

Seven claims overstepped a restriction and were demoted; twelve more rest on vendor documentation admitted for facts only and are held at `fact`.

- DOMSEC-C07 (SRC-316, T3, catalogue facts only; its advice is not a ground): decision to `fact`.
- DOMSEC-C14 (SRC-098, SRC-099, facts only, no advice): the update advice is inferred; row is `fact`.
- DOMSEC-C21 (SRC-265, Mozilla's position as that vendor's): `fact`.
- DOMSEC-C28 (SRC-263, 2016 measurement of allowlist bypasses, deployment policy is web-architecture): `rejected` belief, not a decision.
- RUNSEC-C11 (SRC-273, prevalence evidence only, not a recommendation): `fact`.
- SRVSEC-C13 (SRC-342 restricted to CSPRNG principles and the listed Node functions; algorithm advice is outside): `acceptable-when`, one position only.
- SRVSEC-C11 (SRC-336 requires a verbatim read of each crypto section; scrypt defaults came through a v10 digest): `fact`, inferred.
- Held at `fact` as vendor documentation: FW-C01, C03, C05, C06, C08, C09, C10, C11, C12, C18, C19, C20.
- Judgement calls kept as decisions, listed so the maintainer can overrule: SRVSEC-C16 and C20 (driver facts rendered as the parameter channel, no preference between drivers), SRVSEC-C47 (Express `root` option), SRVSEC-C22 (least privilege from SRC-345, not in the register's list of principles but of the same kind), SRVSEC-C30 and C31 (SRC-346 principles, the CIDR list is OWASP's content), SRVSEC-C41 (rejection derived from advisory facts), DOMSEC-C56 (ASVS requirement, mechanism from a T3 catalogue).

## Part D. Decisions resting on a single source

Each carries `unvalidated` in the node's epistemic state where the rule says so. DOMSEC-C05 (SRC-097), C18 (SRC-267), C19 (inferred, T2), C37 (inferred, T2 and T3), C45, C46, C56, C58; RUNSEC-C12, C24 to C26, C29 (T2, recipe inferred), C34, C35, C37 (T2, Node TSC author), C40 (inferred); SRVSEC-C05 to C09, C10 (OWASP position, language-neutral), C12, C22, C26, C27, C28, C29, C30, C32, C33 (synthesis of three rows), C42, C47, C49, C50, C52, C53, C56 to C58, C60, C61, C63, C64; RUNTIME-C13, C15, C18 (inferred), C51, C52 (inferred); TYPES-C31. The weightiest: SRVSEC-C10 (password-hashing parameters, an OWASP position nothing else measures) and SRVSEC-C33 (pinned connection, a synthesis no admitted source states).

## Undecided nodes and the evidence that would settle each

| node | question | evidence that would settle it |
|---|---|---|
| `PIG-JS.DEFENSE.DOM.2.3` | Is URL validation by parsing plus scheme and origin allowlist the rule, and what of `javascript:` URLs (DOMSEC-C57, inferred)? | An admitted normative page on the `javascript:` scheme as a sink (HTML Standard navigation or MDN `URL` and `location` pages) and an OWASP URL-validation source |
| `PIG-JS.DEFENSE.INJECTION.4.4` | What is the Node recipe for path containment (SRVSEC-C55, RUNSEC-C29)? | A verbatim read of the Node `fs.realpath` and `path.resolve` pages, or an OWASP Node source stating the recipe |
| `PIG-JS.DEFENSE.INJECTION.5.3` | Is `v8.deserialize()` safe for untrusted buffers, and is `structuredClone` safe for untrusted input (SRVSEC-C44, C43)? | A Node or V8 statement on trust of serialized buffers, or an advisory; the Node v8 page has none |
| `PIG-JS.DEFENSE.INJECTION.6.4` | How does Node's built-in `fetch` treat `redirect: "manual"` and redirect limits (SRVSEC-C37)? | The undici documentation, not in the register; an audit of that page |

Open points that did not become nodes: SRVSEC-C14 (current Node documentation of `timingSafeEqual` and `randomBytes`, `randomInt`, `randomUUID`, not grounded; fix by reading the current crypto page in full, filed as a `fact` row on `SECRETS.4`); the MDN condition for `setAttribute` (B2); the current status of V8's non-backtracking engine (B10); the stability labels of the permission model (B4).
