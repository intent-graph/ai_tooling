# Re-audit under MD-08: web-app-philosophy and PIG-WEB-ALLOCATION

Scope: every node of `intent_graphs/web_app_philosophy.ig.yaml` (80) and the 8 nodes of the
PIG-WEB-ALLOCATION branch of `intent_graphs/web_defaults.ig.yaml`. Each node was read whole with
`ig-tool query --node` (scripted), and the judge records were read where a node was a candidate
(J1, J2, J3, J4, J5 records; the J1, logic, data and transverse reviews). Rule applied: MD-08,
"max" is the best practice for the node's purpose, not the most demanding one. MD-01 to MD-07
are settled and were not re-audited. Read-only: no graph or other file was changed.

## L1 headline

- Nodes read: 88 (philosophy 80, PIG-WEB-ALLOCATION 8).
- Flagged: 5. LOGIC.SECURE (high), DATA.ORGANIZE (medium), ALLOCATION.ACT.3 (low), ALLOCATION.DERIVE.2 (low), TRANSVERSE.SECURITY (low).
- Codified-practice overrides in this scope: 2 of 6 are here, and "best" still supports both: CHECK constraints required (ALLOCATION.GUARD.2, DATA.GUARD), and expand, migrate, contract for breaking function-API changes (RECORD.2, RECORD.3, DATA.MAINTAIN, TRANSVERSE.CONTRACTS, DB_API). The other four are in PIG-WEB-DATA, outside this scope.
- Most verdicts were decided by purpose and stay. In this scope, MD-08 most often favours the simpler option the judges had already chosen: POSTGRES_FIRST, JOB_HOST, CACHE_STORE, JS_SERVER, LOGIC.EXPOSE.3.

## L2 claims

- **LOGIC.SECURE**: current verdict: MFA required on every human account by default. Strictness decided it: the record says "requiring it is the most demanding form", and the judge kept login usability out of the forces. Proposed: offer MFA on every human account, phishing-resistant authenticators preferred; require it on privileged accounts and at step-up before sensitive operations; whether every account must use it follows the security level the project chooses by risk. Confidence: high.
- **DATA.ORGANIZE**: current verdict: when a Boyce-Codd decomposition loses a dependency, a constraint trigger enforces it under Serializable or a lock. Strictness decided it: the review chose the option that "keeps both" properties, "under the max rule". Proposed: keep the dependency-preserving third-normal-form design and enforce every dependency declaratively, with a composite foreign key to the owning pair. A trigger is used only where no declarative form exists. Confidence: medium.
- **ALLOCATION.ACT.3**: current verdict: defer work that would push the response past a 1 s budget. Strictness decided it: of L601's two rules of thumb (1 s and 10 s), the judge took the tighter one, with no ground ("my choice"). Proposed: defer work expected to last more than a few seconds, or longer than the request timeout; 1 s stays the design target for interactive responses, not the deferral cut-off. ACT.2's in-request exception changes to match. Confidence: low.
- **ALLOCATION.DERIVE.2**: current verdict: every collection pages by keyset behind an opaque continuation, and the stack node forbids offset for HTML lists. Strictness decided it: an API-guideline consensus row (L266) was extended to every surface without weighing the human list. Proposed: keyset paging for the structured-data and agent interfaces and for large or growing sets; offset with page numbers is acceptable for a human HTML list over a bounded result. Confidence: low.
- **TRANSVERSE.SECURITY**: current verdict: a threat model per placement and per critical flow. Strictness decided it: the review "takes the stronger position", and "per placement" goes beyond the OWASP A06 text it cites. Proposed: a threat model per critical flow and trust boundary, revisited when a placement on that flow changes, with misuse-case tests per tier. Confidence: low.

## L3 full

### LOGIC.SECURE (Secured Entry): MFA required by default

**Positions** (J3 record):
- P5: credential stuffing is defended in layers: MFA first, then breached-password checks, then device fingerprinting and CAPTCHA, which are spoofable; never IP blocking alone (L033).
- L033 orders the layers. It does not say that MFA is required.
- Rejected, with an inferred condition: "MFA optional for human accounts: acceptable when the application's audience cannot practically be required to use a second factor".

**Evidence of the tie-break:**
- J3 record, decision 6: "Max applied: MFA is required by default on human accounts (inferred: L033 orders MFA first; requiring it is the most demanding form)."
- J3 `questions.md`: "login usability is not a force the secured-entry node serves, so the max rule decides (required by default)".
- Logic review, result: "MFA is decided by the max rule, because usability is not the LOGIC role's force; its cost lands on INTERACTION".
- The same review (M5) found the branch inconsistent. It decided SameSite on usability and MFA against it. MD-07 then adopted the usability-weighted SameSite choice. MD-07 does not touch MFA.

**Why this is not "best" in the default context:**
- The default context is a classic website (documents, forms, CRUD) with humans and agents as users. MD-06 adds that a prototype takes the fastest secure path.
- The best practice is risk-proportioned:
  - MFA is offered on every account, with passkeys and WebAuthn preferred because they resist phishing.
  - MFA is mandatory where compromise is costly: operator, owner and administrator accounts, and step-up before sensitive operations.
  - The rest follows the risk level the project chooses. TRANSVERSE.SECURITY already states every property "at a level chosen by risk".
- Mandatory MFA on every account adds sign-up and recovery cost, plus support load, on low-risk accounts. The remaining layers of L033 already cover those accounts: breached-password checks and per-account throttling.
- Certainty: inferred. I did not read the ASVS 5.0 MFA requirement for this audit. If the chosen ASVS level mandates MFA for all users, the per-project level decides, and the proposal below defers to it.

**Proposed intent** (unchanged except the last clause): "... bounds consumption at two depths, and requires a second factor where the account or the operation warrants it."

**Proposed constraint**, replacing "Defend logins in layers ... Max applied ...": "Defend logins in layers: MFA first, then breached-password checks, then device signals and challenges known to be spoofable; never IP blocking alone. Offer MFA on every human account, phishing-resistant authenticators (passkeys, WebAuthn) preferred. Require it on privileged accounts (operator, owner, administrator) and before sensitive operations (step-up). Whether it is required on every account follows the security level the project chooses by risk (TRANSVERSE.SECURITY)."

**Proposed rejected lines:**
- "MFA required on every human account: acceptable when the project's chosen risk level requires it, or when exposure of one account is severe."
- "MFA optional on privileged accounts: never."

**Proposed state:** `known | unvalidated: MFA scope by account privilege and by the project's risk level (inferred from L033 and TRANSVERSE.SECURITY)`.

**Propagates to:**
- PIG-WEB-LOGIC.SECURE.4: request and check the MFA authentication context (`acr` or `amr`) for privileged accounts and step-up, not for every login.
- PIG-WEB-LOGIC.SECURE.5: change "MFA required" to "offered; required by privilege and risk level". Its rule "minimum 8 with MFA, 15 without" already covers both kinds of account.
- PIG-WEB-LOGIC.SECURE: roll-up.
- J7 records: they cite J3's MFA verdict.

### DATA.ORGANIZE (Organized Facts): a lost Boyce-Codd dependency enforced by trigger

**Positions:**
- P1: third normal form is the floor (L037, L469 MAINT).
- P2: third normal form as the ceiling (L039). Rejected, and rightly, as a general ceiling.
- After review M4, the decision adds: where a Boyce-Codd decomposition loses a dependency, the dependency is enforced by a constraint trigger under DATA.GUARD's rule.
- No position weighed the alternative for this case: keep that relation dependency-preserving and enforce the dependency declaratively.

**Evidence of the tie-break:**
- Data review M4, fix: "where a Boyce-Codd decomposition loses a dependency, the lost dependency is enforced by a constraint trigger ... Under the max rule that keeps both 'each fact once' and 'every rule enforced'."
- J2 record: "enforcing it by trigger keeps both ... which is the max under the selection rule."
- The same review measured the cost and called it "an integrity cost, a rule moving from a declarative key to a procedural cross-table check".

**Why this is not "best":**
- The node's purpose is integrity. The branch's own rule ranks declarative enforcement first:
  - GUARD.2: "a partial unique index or an exclusion constraint first"; "only declarative constraints bind every writer".
  - DATA.GUARD: the same.
- Take the overlapping-key case, the review's "nearest shop" example. Use a third-normal-form table (person, shop type, shop), unique on (person, shop type), and add a composite foreign key from (shop, shop type) to the shop table's unique (shop, type). Both dependencies are then enforced declaratively, at any isolation level, for every writer, owner role included. The repeated type value cannot diverge, so it needs no sync plan.
- The trigger route needs these, and gains no integrity for them:
  - Serializable isolation or a lock on every write to either table;
  - a concurrent test (OPERABILITY.2);
  - procedural code.
- Certainty: inferred from standard relational theory, as the original verdict was. Not in the ledger.

**Proposed constraint**, replacing the third: "Where a Boyce-Codd decomposition would lose a dependency, keep the dependency-preserving third-normal-form design and enforce every dependency declaratively: the repeated determinant is covered by a composite foreign key to the table that owns the pair, so it cannot diverge and needs no sync plan. A constraint trigger under DATA.GUARD's rule (Serializable isolation or a lock) only where no declarative form exists."

**Proposed state:** `known | unvalidated: the Boyce-Codd claim, the declarative form for a lost dependency, the co-presence CHECK and the MD-03 consequence are inferred | gap: collation choice has no row (handed to J6)`.

**Propagates to:**
- DATA.GUARD: the list in its second constraint changes to "dependencies lost by a Boyce-Codd decomposition when no declarative form exists".
- PIG-WEB-DATA.ORGANIZE.1: inherited clause.
- PIG-WEB-DATA.GUARD.4: trigger list item.
- TRANSVERSE.OPERABILITY.2: fewer procedural invariants to test concurrently.

### ALLOCATION.ACT.3 (Deferred and Scheduled Work): the 1 s deferral threshold

**Positions:**
- P1: inside the request goes what the user sees next. Defer foreign effects, and "work expected to last more than a few seconds (rules of thumb: 1 s per L271, 10 s in SRC-203)" (L601).
- L271 records that its sources disagree: "thresholds differ (1 s vs 10 s)".

**Evidence of the tie-break:**
- J1 record, state: "the 1 s threshold is my choice between L601's two rules of thumb". No ground is given for taking the tighter one.
- L013 gives 1 s as the limit that keeps the flow of thought and 10 s as the attention limit. That is a design budget for responses. It does not make 1 s the point at which work must leave the request.

**Why this is not "best":**
- L601's own wording, "a few seconds", is the best-grounded threshold.
- With 1 s as the cut-off, a classic forms site sends routine 1 to 3 s operations through a worker, a 202 response and a status page. That costs one more page, polling or refresh, and more states for users and the team, for work the user waits for anyway.
- The force that argues for a low threshold is synchronous worker capacity on slow I/O (J7 PROCESS.4, ENFORCE.4). It is a capacity force, so it moves the threshold when it is measured. It is not a default.

**Proposed constraint** (deferred list): "Deferred: foreign effects, fan-out, derived data, and work expected to last more than a few seconds or past the request timeout; about 1 s stays the design target for interactive responses (FORCES.4), not the cut-off for deferral; a lower cut-off follows measured worker capacity."

**Proposed state:** `known | unvalidated: the few-seconds threshold follows L601; a lower cut-off needs measured worker capacity`.

**Propagates to:**
- ALLOCATION.ACT.2: the in-request exception becomes "when the user waits for the outcome in the same response and the call is expected to finish within a few seconds, under the request timeout"; intent recorded first, unchanged. Foreign mutations still default to a worker, which is grounded in L601.
- PIG-WEB-LOGIC.PROCESS.2: "fits ACT.3's 1 s budget".
- PIG-WEB-LOGIC.EXPOSE.3.

### ALLOCATION.DERIVE.2 (Filtering, Sorting, Paging and Search): keyset paging on every surface

**Positions:**
- P1: reduce the data with the data, set-based (L613, L614).
- The paging method was taken from L265 (maximum page size), L266 (server-issued continuation instead of offset; consensus of JSON API guidelines) and L541 (keyset for bulk jobs, MAINT).
- No position weighs human-facing HTML lists.

**Evidence of the tie-break:**
- J1 record: "The server enforces a maximum page size and pages by keyset behind an opaque continuation (L265, L266, L541)". It cites rows about API collections and bulk jobs for every surface.
- The stack refinement (PIG-WEB-LOGIC.EXPOSE.1) makes it absolute: "HTML lists page the same way" and "Forbidden: offset and limit for client-facing collections".

**Why this is not "best":**
- Keyset is best where it is grounded:
  - API and agent collections: stable continuation, no skipped rows under concurrent inserts;
  - large or growing sets: no deep-offset cost;
  - bulk work (L541).
- For a classic website, a human list over a bounded, filtered result often needs page numbers and jumps. Offset gives that at lower cost, and its weaknesses (deep pages, rows that shift under concurrent writes) are small at that size.
- Certainty: inferred. No ledger row argues for either method on HTML lists.

**Proposed constraint**, replacing the second: "Enforce a maximum page size. Structured-data and agent collections, and any list over a large or growing set, page by keyset behind an opaque continuation. A human-facing HTML list over a bounded result may page by offset with page numbers; offset never for deep pages or bulk work."

**Propagates to:**
- PIG-WEB-LOGIC.EXPOSE.1: the HTML-list line and the "Forbidden: offset" line.
- PIG-WEB-DATA.MAINTAIN.4: L541 is unchanged.

### TRANSVERSE.SECURITY (Security Across Tiers): a threat model per placement

**Positions:**
- P3: the OWASP Top 10 as an awareness map, each category with an owning tier.
- For A06, the transverse review (M4) replaced "the allocation decisions" with a threat model and misuse-case tests. That replacement is right, and it was purpose-driven.

**Evidence of the tie-break:**
- Transverse review M4: "OWASP's A06 prevention is more demanding: threat modelling for authentication, access control, business logic and key flows ... The max rule takes the stronger position."
- Its fix then widens the scope beyond the cited text: "a threat model per placement and per critical flow".

**Why this is not "best":**
- OWASP names flows: authentication, access control, business logic, key flows.
- A model per placement, 26 placements per project, mostly repeats the flow models and the allocation records, which are the model's input. It adds effort and no coverage.

**Proposed intent clause:** "insecure design is answered by a threat model per critical flow and trust boundary, with misuse-case tests".

**Proposed constraint:** "Answer insecure design with a threat model per critical flow and trust boundary (authentication, access control, business operations, agent access), revisited when a placement on that flow changes, and misuse-case tests per tier."

**Propagates to:**
- J5's children's claims line;
- PIG-WEB-TRANSVERSE.SECURITY.1, if it repeats the wording.

### Verdicts examined closely and kept

Codified-practice overrides in this scope:
- **ALLOCATION.GUARD.2, DATA.GUARD: CHECK constraints required.** Best still supports it. A declarative constraint binds every writer at any isolation level, at almost no cost. The doctrine made CHECK optional because the functions were the only write path. Under MD-03 that no longer holds: owner-run migrations and data jobs, and the single-table direct-write exception, bypass the functions. Product policy that changes often stays in the backend (GUARD.3), so this does not freeze policy into constraints.
- **RECORD.2, RECORD.3, DATA.MAINTAIN, TRANSVERSE.CONTRACTS, INTERACTION.ENVIRONMENT.3, DB_API: expand, migrate, contract for breaking function-API changes.** Best still supports it. Under MD-03 consumers deploy separately, and this is the only route that keeps every running version working. Lockstep stays acceptable when every consumer ships with the migration. The new function name is the expand step, which matches L512. The departure is counted at PIG-WEB-DATA.INTERFACE.1, outside this scope.
- The other four overrides (trigger-maintained `updated_at`, 8-byte keys unless bounded, declared self-referencing parent keys, append-only tables without `updated_at`) are in PIG-WEB-DATA nodes, outside this scope.

Other verdicts examined:
- **ALLOCATION.GUARD.2, default isolation.** Kept here. The philosophy states "Serializable with retry, or a lock", and the judge's concurrence with Serializable as the default is a hand-off. The default itself is PIG-WEB-DATA.CONCURRENCY.1's verdict, which the data review called "the max for integrity". That auditor should check it.
- **ALLOCATION.ACT.2, foreign mutations in a worker behind 202.** Kept. Grounded in L601 ("defer work with foreign side effects") and in synchronous-worker capacity. Only the threshold, owned by ACT.3, is flagged.
- **TRANSVERSE.OPERABILITY.2 and LOGIC.ENFORCE, a concurrent test per procedural invariant in the default suite.** Kept. The test follows from GUARD.2's correctness depending on concurrency, so it is purpose-driven. Possible trim if cost shows: concurrent tests where correctness depends on taking a lock, and an isolation assertion plus one retry-path test where it depends on Serializable. The DATA.ORGANIZE change also reduces their number.
- **TRANSVERSE.PERFORMANCE, whole-path join to database time** (marked "max"). Kept. The ground is purpose: the work MD-03 places in functions is invisible to page metrics. The cost is low, because OPERABILITY.1 already carries the correlation id.
- **ALLOCATION.GUARD.3 and ACT.4, actor treated as a claim with a role-to-actor pairing check.** Kept. A security purpose, and inferred. The cost is one pairing table.
- **ALLOCATION.RULES.5 and ACT.1, no backend transaction around several API calls.** Kept. One owner of the transaction boundary under MD-03.
- **ALLOCATION.GUARD.4, opaque server session, never stateless.** Kept. Revocation (L022) is the security purpose.
- **ALLOCATION.GUARD.6, keys required on agent mutations.** Kept. L051; retries by automated callers.
- **INTERACTION.VISUALIZE, accessibility from the first design with users involved early.** Kept. L005 consensus; the only rejected option is a retrofit.
- **INTERACTION.ENVIRONMENT.7, uploads on a distinct registrable domain.** Kept. L028 majority, and the purpose is containing script. An object store on a provider domain meets it at low cost (inferred).
- **INTERACTION.ENVIRONMENT.3, a compatibility window of days.** Kept. L009 consensus; open tabs hold old code.
- **INTERACTION.AGENT, narrowest scopes.** Kept. Coarser scopes are already acceptable for first-party agents (L642).
- **INTERACTION.COLLABORATE and INTERACTION.AGENT, the report queue and owner-approval clauses.** Lifted from PIG-WEB-INTERACTION. Those verdicts are their records', and they were not re-audited here.
- **DATA.ORGANIZE one-to-one rule (L470), DATA.DERIVE (L488), DATA.MAINTAIN (L046, L474).** Kept. Doctrine and purpose agree.
- **PIG-WEB-ALLOCATION.POSTGRES_FIRST, JOB_HOST, CACHE_STORE, JS_SERVER.** Kept. Each already takes the simpler option until a measured limit, which is MD-08's own direction.
- **Settled by maintainer decisions, not re-audited:**
  - GUARD.3 read visibility and LOGIC.SECURE per-user reads (MD-05);
  - RECORD.3 and TYPE_CHAIN origin (MD-02);
  - ROW_SECURITY (MD-01);
  - RECORD.2, ACT.1, DB_API, DATA.INTERFACE (MD-03);
  - SameSite (MD-07);
  - hosting (MD-06).
