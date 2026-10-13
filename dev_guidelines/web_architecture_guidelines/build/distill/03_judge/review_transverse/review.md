# TRANSVERSE branch (J5 philosophy, J9 stack): adversarial review

This review checks the judged TRANSVERSE branch of both graphs before the graphs are built:
- `../J5_phil_transverse/` (14 nodes of `web-app-philosophy`): `result.md`, `records.md`, `questions.md`;
- `../J9_pig_transverse/` (27 judged nodes of `pig-web-defaults`): the same three files.

Yardsticks: the max rule and judge record format of `../../target_hierarchy.md`; the maintainer decisions MD-01 to MD-03 of `../../maintainer_decisions.md` (not under review, checked for faithful application); the settled placements of `../J1_allocation/allocation_matrix.md` and J1's open read-visibility question (`../J1_allocation/questions.md`, Q1). Where links cross, the sibling records of J2 and J6 were read on the point concerned. Evidence ids `Lnnn` resolve in `../../02_skeleton/claims_ledger.md`.

Certainty words: **grounded** means I read it (ledger row, record or source page fetched for this review); **inferred** means it follows from records, rows or known engine behaviour, but no read source states it.

Pinned:
- Findings: 14. Blocking 1, major 6, minor 7.
- Blocking: B1 PIG-WEB.TRANSVERSE.EVOLUTION.2 forbids a module from calling another domain's database functions, which forces cross-domain business operations to be composed of several API calls in the backend, against ACT.1 and MD-03.
- Major: M1 the departure from L517 is counted 0, 1 and 1 by J9, J5 and J6, and the lockstep exception has three different conditions across J2, J5 and J6. M2 J5 OPERABILITY.2 says every database test is a never-committing transaction; J9 OPERABILITY.5, which refines it, requires committing tests, and the concurrency testing that GUARD.2 needs is left as a gap. M3 J5 EVOLUTION.3 and J9 EVOLUTION.1 say "one backend deployable" without reconciling it with MD-03's several backends. M4 the OWASP tier map in TRANSVERSE.SECURITY misreads A08 and misses the threat modelling and misuse-case tests that A06 prescribes. M5 J9 SECURITY.5 stops at SLSA Build L2, although its own source says Build L3 is intended for most releases. M6 J9 SECURITY.2 makes HSTS preload the default end state, which the operators of the preload list advise against.
- Minor: m1 ASVS Level 2 can be grounded (the ASVS 5.0 text says most applications should strive for it). m2 J9 PERFORMANCE overstates the gap on a server latency target (L297, L013 and ACT.3's 1 s already bound it). m3 J9 TOPOLOGY.2's sync workers ignore blocking calls made in the request (the OIDC code exchange of GUARD.4). m4 J5 OPERABILITY.1 keeps every data-change event out of the security log, including privilege and credential changes. m5 J5 EVOLUTION.5 leaves cross-schema functions without an owner. m6 J9 SECURITY.4 calls the environment fallback "not the default", but its own assumed hosting triggers it. m7 the pending read-visibility clause has three notations across judges (`undecided:`, `awaiting maintainer:`, `open:`), and J5 OPERABILITY.2's state omits it.
- Verdicts against the doctrine: J5 TRANSVERSE.CONTRACTS against L517 "deployed together" is upheld: the max rule is on its side, and the maintainer's own L512 (new named version, gradual migration) supports it; count it once, at its owner. J9's "0 against the doctrine" holds only as "0 new": J9 realizes the same departure, and the "new function name" it credits to L517 is J5's expand step, not L517's text. J9's adoptions of L567, L545 and L566 are upheld; committing tests in a disposable database do not breach L567, which governs shared environments.
- Questions: J5 has none, which is upheld; no decided node should become a question (M3 is a reconciliation, not a trade-off). J9 Q1 on the hosting model is a genuine context check, self-contained and fairly framed; keep it, and add that under the recommended option the managed secret store holds only if one is added. Both units keep J1's read-visibility question open with its stated default (each backend filters, shared specification, shared denial tests), word for word with J1 Q1's "if unanswered".
- Maintainer decisions: MD-01 and MD-02 are applied faithfully in both units. MD-03 is applied everywhere except at two points: the "one backend" default (M3) and the module rule (B1).

## Findings

### B1 (blocking) The module rule forces backend-composed cross-domain operations

**Node**: PIG-WEB.TRANSVERSE.EVOLUTION.2 (J9).

**Issue.** The record says: "Each module calls the functions of its own domain schema ... Another module's data is reached through that module's interface, never through its tables or functions (inferred)."

Take one business operation that writes two domains, such as an order that also creates an invoice. MD-03 and ACT.1 settle it: "multi-table writes composed in a backend" are forbidden, as is "a backend transaction wrapping several API calls". Every business operation is one database function call in its own transaction.

Under J9's rule, the orders module may not call a function that lives in, or writes into, the billing schema. It must go through the billing module's Python interface. That leaves two calls, and only two ways to make them:
- two transactions: the operation loses atomicity;
- one wrapping transaction: forbidden by ACT.1.

The rule also creates an asymmetry. Under RECORD.2, a backend in another language may call any function its role is granted, while a module inside the team's own backend may not.

**Evidence**: grounded in the records. `../J9_pig_transverse/records.md`, EVOLUTION.2; `../J1_allocation/allocation_matrix.md`, ACT.1 ("multi-table writes composed in a backend; a backend transaction wrapping several API calls" under *forbidden*) and RECORD.2. MD-03: "Operations that change several tables as one business operation are the database's responsibility."

**Proposed fix**:
- The module boundary forbids reaching another domain's **tables** directly. The function API is reachable from every module, within its role's grants.
- A cross-domain business operation is one database function. It is called by the module that owns the workflow and owned by the cross-schema owner role of J5 EVOLUTION.5 (see m5).
- The Python module interface carries workflow and product policy, never a second path to another domain's data.
- Mark the rule `unvalidated` (inferred).

### M1 (major) One departure from L517, counted three ways, with three different exceptions

**Nodes**: TRANSVERSE.CONTRACTS (J5); PIG-WEB.TRANSVERSE.CONTRACTS.2, OPERABILITY.6 and the pinned doctrine count (J9). The link crosses to DATA.MAINTAIN (J2) and PIG-WEB.DATA.INTERFACE.1 (J6), which owns L517.

**Issue**:
- **Counting.** J2 reports "0 new" and flags a narrowing. J5 counts 1 partial. J6 counts 1 partial. J9 counts 0 and lists L517 as "adopted as the max choice (no version numbers: a new function name carries the change)". L517 says "a breaking change is coordinated with every consuming team and deployed together; there are no formal version numbers". The new-name step is J5's expand phase, not L517's text. J9 realizes the departure (CONTRACTS roll-up: "breaking changes follow J5's expand, migrate, contract"; OPERABILITY.6: "removals only in the contract phase") and reports none.
- **The lockstep exception differs between judges**:
  - J5: "every consumer of that contract ships in the same release and the release stops all old consumers before the change applies";
  - J2: "every consumer ... ships in the same deployment as the migration, or the change runs in a window where no old version is running";
  - J6: "every consumer of the changed function ships with the migration".

  J6's condition, at the stack node, is weaker than the principle it refines. "Ships with the migration" still leaves the rolling-deploy window that J5 cites as its ground (L009; backends roll out instance by instance). A PIG-WEB node accepting lockstep where the principle forbids it is the contradiction the target hierarchy rules out.

**Evidence**: grounded in the records. `../J2_phil_data/records.md` lines 9 and 103; `../J5_phil_transverse/records.md`, CONTRACTS *Rejected*; `../J6_pig_data/records.md` lines 9 and 545; `../J9_pig_transverse/result.md`, pinned "Verdicts against the maintainer doctrine: 0"; L517, L512 in the ledger.

**Proposed fix**:
- One departure, counted once at its owner: J6, PIG-WEB.DATA.INTERFACE.1. J2, J5 and J9 cite it as "realizes the L517 narrowing, counted at INTERFACE.1".
- One condition everywhere, J5's: no old version of any consumer is running when the change applies. J2's second clause is the same condition.
- J9 rewords its pin: "0 new; realizes the L517 narrowing (J5, J6)". It credits the new-name rule to J5 expand and L512, not to L517.
- Note in J5 and J6 that the maintainer's own L512 (a breaking contract change gets a new named version, the old one soft-deleted, consumers migrate gradually) already takes this route for stored contract schemas. The departure is narrower than "against the doctrine" suggests.

### M2 (major) The principle forbids the commit-time tests its refinement requires; concurrency testing left as a gap

**Nodes**: TRANSVERSE.OPERABILITY.2 (J5), PIG-WEB.TRANSVERSE.OPERABILITY.5 (J9).

**Issue**:
- J5 decides that the database tier's low-level tests "run on the real engine ..., **each** in a transaction that never commits (L400, L567)".
- J9, refining it, decides that serialisation failures and retries, lock waits, deferred constraints and the outbox "cannot be tested inside a rolled-back transaction" and are tested "with committing sessions in the disposable database". J9 is right, and it contradicts its parent's literal rule.
- J5 records concurrency testing only as a gap. Yet GUARD.2 (settled) forbids "a procedural check under Read Committed without a lock" and requires "Serializable with retry or a lock". A placement whose correctness depends on concurrent behaviour needs a test of that behaviour. Requiring the test invents no fact: it follows from GUARD.2 (inferred), and it is the max choice for the node's purpose, fidelity.

**Evidence**: grounded in the records (`../J5_phil_transverse/records.md`, OPERABILITY.2; `../J9_pig_transverse/records.md`, OPERABILITY.5; allocation matrix, GUARD.2). L400 itself gives the rolled-back transaction as an example ("for example one transaction per test, rolled back"), not as the only form. L567 applies to shared environments only.

**Proposed fix**:
- J5 OPERABILITY.2: "each test isolated: a rolled-back transaction by default; behaviour that only shows at commit or between sessions (serialization failures and retries, locks, deferred constraints, the outbox) is tested with concurrent committing sessions in a disposable database, never a shared one (L567)".
- Add the rule: every invariant that GUARD.2 enforces procedurally, under Serializable or a lock, has a concurrent test (inferred from GUARD.2).
- Keep the gap only for the missing source row: `known | unvalidated: concurrency tests required by GUARD.2 | gap: no row on concurrency testing`.

### M3 (major) "One backend deployable" is not reconciled with MD-03's several backends

**Nodes**: TRANSVERSE.EVOLUTION.3 (J5), PIG-WEB.TRANSVERSE.EVOLUTION.1 and the EVOLUTION roll-ups (J9).

**Issue.** The default context restated by J1 under MD-03 reads "the database is shared by several backends and by other consumers", with one team. J5 decides that "the system starts as one backend deployable" and J9 that there is "one Python backend deployable over the shared database".

Neither record says how the two defaults coexist. Are the other backends other products, teams or languages (L515's "backend of backends")? Or does the team's product split later? A reader of the graph sees two defaults that seem to contradict each other: one names several backends, the other one deployable.

The reconciliation also changes the weight of an argument. Monolith-first rests partly on avoiding a data split and the distribution premium (L074, L076). Under MD-03 the data seam is already shared through the function API. A second backend of the same team therefore costs less than the research rows assume, which J5 never weighs.

**Evidence**: grounded in the records (`../J1_allocation/records.md` line 17 and the matrix's default context; J5 EVOLUTION.3; J9 EVOLUTION.1; L515).

**Proposed fix**:
- State it in both records. The team's own product starts as one backend deployable. The other backends of MD-03 are other products, teams or languages that reach the data through the function API, each with its own role. MD-03 does not license splitting the team's product.
- Add that, because the data seam is already the function API, a later split of the team's product does not move data. Only deploy independence and the distribution premium of L074 remain (inferred).

### M4 (major) The OWASP tier map misreads A08 and misses A06's threat modelling

**Node**: TRANSVERSE.SECURITY (J5); the pins of J5 and J9 that repeat the map.

**Issue**:
- **A08 misread.** J5 assigns A08 (Software or Data Integrity Failures) to "the delivery pipeline (one immutable artifact, L101) and to the database's declarative constraints (GUARD.2)". The OWASP 2025 text defines the category as "code and infrastructure that does not protect against invalid or untrusted code or data being treated as trusted and valid". Its preventions are signatures, trusted repositories, review of code and configuration changes, CI/CD segregation, and no unsigned serialized data accepted from untrusted clients. Declarative constraints are not an A08 control. Insecure deserialization belongs to the parsing tier (GUARD.1).
- **A06 weaker than the source.** J5 assigns A06 (Insecure Design) to "the allocation decisions themselves, recorded with their forces". OWASP's A06 prevention is more demanding: threat modelling for authentication, access control, business logic and key flows, and tests of use-cases and misuse-cases for each tier. A record of allocation decisions is not a threat model. The max rule takes the stronger position.
- **A04 incomplete** (minor part). Assigned to the backend only, following L303. Transport (the proxy's TLS, the database connection TLS of J9 SECURITY.2) and data at rest also belong to it.

**Evidence**: grounded. The OWASP Top 10:2025 pages for A08 and A06 (SRC-115's site, fetched for this review: top10.owasp.org/2025/A08_2025-Software_or_Data_Integrity_Failures and /A06_2025-Insecure_Design). L303 states that its tier map is not in the source.

**Proposed fix**:
- A08: the pipeline (signed provenance, trusted sources, review of code and configuration, SECURITY.5) and the parsing tier for untrusted serialized input (GUARD.1). Drop the declarative constraints.
- A06: a threat model per placement and per critical flow (authentication, access control, business operations, agent access), with misuse-case tests per tier, which J5 OPERABILITY.2's denial tests already begin. The allocation records are the model's input, not the model.
- A04: the backend, the proxy, the database connections and storage at rest.
- Keep the whole map `unvalidated`.

### M5 (major) Supply chain stops at SLSA Build L2 although its own source targets L3

**Node**: PIG-WEB.TRANSVERSE.SECURITY.5 (J9).

**Issue.** J9 decides Build L2 and records "Build levels above L2 are not weighed by the evidence (gap)". L357 says "at least ... Build L2". Its source SRC-242, the SLSA v1.0 levels page, describes Build L3 (hardened builds: no influence across runs, signing secrets out of the build's reach) as "Intended for: Most software releases". It adds that L3 "usually requires significant changes to existing build platforms".

Under the max rule, L3 is the target for the node's purpose, the integrity of what runs. L2 stays "acceptable when the hosted build platform offers no hardened, isolated provenance generation". The gap does not exist: the evidence is in the cited source.

**Evidence**: grounded (slsa.dev/spec/v1.0/levels, fetched for this review; SRC-242 in `../../02_skeleton/sources.md`).

**Proposed fix**: the decision becomes "signed provenance at Build L3, verified before deploy; Build L2 acceptable when the build platform cannot isolate runs or keep the signing key from the build steps". Remove the gap.

### M6 (major) HSTS preload made the default end state

**Node**: PIG-WEB.TRANSVERSE.SECURITY.2 (J9).

**Issue.** J9 decides that the HSTS "end state is includeSubDomains and preload, reached by raising max-age in steps once every subdomain serves HTTPS". The preload list's operators say: "do not include the `preload` directive by default". They also say that removal "takes months" to reach users and that preloading applies to all subdomains of the base domain, "including internal subdomains that are not publicly accessible". The header must be served on the base domain.

A web application commonly runs on a subdomain of an organisation's domain that its team does not control. As written, the max end state commits that whole domain. Preload stays the most demanding protection of the first request (L148). But its condition is control of the registrable domain, plus a long-term HTTPS commitment for every subdomain including internal ones. That is a recorded decision, not a default.

**Evidence**: grounded (hstspreload.org, fetched for this review; L147 calls the scope "a commitment"; L148).

**Proposed fix**:
- Default end state: HSTS with a long max-age on the application's host, includeSubDomains once its subdomains serve HTTPS.
- Preload as "the target when the team controls the registrable domain and commits every subdomain, internal ones included, to HTTPS for the long term; recorded as an ADR (EVOLUTION.3) because removal takes months".
- Add it to J9 EVOLUTION.3's list of per-project ADRs.

### m1 (minor) ASVS Level 2 as the default can be grounded

**Node**: PIG-WEB.TRANSVERSE.SECURITY.1 (J9); L304.

**Issue.** J9 marks the Level 2 default as inferred and L304 as `open`, because the level definitions were not read. The ASVS 5.0 text (`0x03-What-is-the-ASVS.md` at tag v5.0.0) says: Level 1 "contains the minimum requirements ... a critical starting point"; Level 2: "Most applications should be striving to achieve this level of security"; Level 3 "should be the goal for applications looking to demonstrate the highest levels of security". It also says that an organisation "should analyze its risks and decide what level".

**Evidence**: grounded (fetched for this review from the OWASP ASVS repository at tag v5.0.0).

**Proposed fix**: ground the default (Level 2, "most applications should be striving"), keep "recorded per project by risk", and move L304's level part from `open` to grounded. "Level 1 never the default" is consistent with the source's "starting point".

### m2 (minor) The server latency gap is overstated

**Node**: PIG-WEB.TRANSVERSE.PERFORMANCE (J9).

**Issue.** J9 records "no server, database or agent-surface latency target in the evidence". The ledger already bounds the server's share:
- L297: TTFB is about 40% of LCP time, against L295's 2.5 s;
- L013: 0.1 s instantaneous, 1 s flow of thought;
- ACT.3 (settled): work over about 1 s is deferred.

A derived budget, about 1 s at most for the server's part of a page at the 75th percentile and well under 1 s for an interaction's request, is an inference from grounded rows, not an invention.

**Proposed fix**: state that derived budget as `unvalidated`. Keep the gap only for the agent surface and for a source-stated server target.

### m3 (minor) Sync workers versus blocking calls in the request

**Node**: PIG-WEB.TRANSVERSE.TOPOLOGY.2 (J9).

**Issue.** The record infers that sync workers fit the request path because "external calls run in workers through the outbox". ACT.2 and ACT.3 defer foreign **effects**, but some external calls stay in the request: the code-for-token exchange of GUARD.4's backend-for-frontend login, external reads, and model calls on an agent surface. L153 itself moves to threaded or async workers "for long blocking external calls".

**Proposed fix**: add the condition that routes making blocking external calls in the request (login through the identity provider included) run with threaded workers or on the ASGI process type, or carry a short timeout. Mark it inferred.

### m4 (minor) "Data-change events stay out" of the security log is too broad

**Node**: TRANSVERSE.OPERABILITY.1 (J5).

**Issue.** The decision says "Data-change events stay out of it". The rejected line is narrower: data-change events as the business history. Changes to privileges, roles, credentials, grants and actor pairings are data changes that L098 lists as security events ("use of higher-risk functionality"). J9 OPERABILITY.4 ships Postgres role changes to the security log, so the stack node already goes past the parent's wording.

**Proposed fix**: "business data changes stay out of it (ACT.4); security-relevant changes (privileges, roles, credentials, grants, the role-to-actor pairing) are security events".

### m5 (minor) Cross-schema functions have no owner

**Node**: TRANSVERSE.EVOLUTION.5 (J5); it touches RECORD.2.

**Issue.** When teams multiply, "each capability team owns its domain schema, its functions", and one owner role holds "conventions, roles and grants, review of the catalogue diff". MD-03 makes multi-table, and so often cross-domain, operations database functions, and nobody is named as their owner. RECORD.2 names a single "database owner"; the split is outside the default context (one team), so it reads as a "would move it", not as the default.

**Proposed fix**: assign cross-schema business functions to the team that owns the workflow, reviewed by the owner role. Mark the whole multi-team arrangement as the condition that refines RECORD.2's single owner (inferred). This also closes B1's ownership question.

### m6 (minor) The secrets fallback is "not the default" under hosting that triggers it

**Node**: PIG-WEB.TRANSVERSE.SECURITY.4 (J9); its Q1.

**Issue.** The fallback, a file or the environment with scheduled rotation, is "acceptable when no managed store exists on the platform and adding one is not budgeted". The record ends: "Under the assumed hosting this is the fallback, not the default". The assumed hosting (self-managed hosts, no orchestrator) is exactly the case without a platform store, and Q1 lists "a secret store the team may have to add" among its costs. As written, the default is undetermined.

**Proposed fix**: say plainly that under the assumed hosting the managed store is a technology to add (weighed under EVOLUTION.4), and that until it is added the file fallback is in force. Fold this into Q1 (see the question verdicts).

### m7 (minor) The pending read-visibility clause has three notations

**Nodes**: TRANSVERSE.SECURITY and OPERABILITY.2 (J5); SECURITY.1 and OPERABILITY.5 (J9).

**Issue.** J1 writes the pending clause as `undecided: ... (Q1, awaiting maintainer)`, and J2, J3 and J6 as `| awaiting maintainer: ...`. J5 and J9 write `| open: ... (awaiting maintainer)`, a token absent from their own "How to read" lists. J5 OPERABILITY.2 carries the clause in its decision but not in its state. The graph builder needs one token to find every node that Q1's answer will change.

**Proposed fix**: use J2, J3 and J6's `| awaiting maintainer: per-user read visibility across backends (J1 Q1; recorded default: each backend filters from a shared specification with shared denial tests)` on all four nodes, J5 OPERABILITY.2 included.

## Nodes found sound

J5 (`web-app-philosophy`):
- TRANSVERSE (roll-up): sound; update its children's claims after M2 and M4.
- TRANSVERSE.PERFORMANCE: sound. Field truth, lab gate and the whole-path join are correctly marked inferred.
- TRANSVERSE.CONTRACTS: sound in substance and upheld against L517; only its counting changes (M1).
- TRANSVERSE.OPERABILITY (roll-up): sound.
- TRANSVERSE.OPERABILITY.3: sound. Migrations inside the pipeline; database as its own codebase correctly inferred.
- TRANSVERSE.EVOLUTION (roll-up): sound once M3 is stated.
- TRANSVERSE.EVOLUTION.1: sound. Naming decisions early versus deciding them late is reconciled cleanly.
- TRANSVERSE.EVOLUTION.2: sound. The features-against-capacity split is marked inferred, and L111's single source is flagged.
- TRANSVERSE.EVOLUTION.4: sound. Scope reconciliation with POLYGLOT is marked inferred.

J9 (`pig-web-defaults`):
- PIG-WEB.TRANSVERSE and SECURITY (roll-ups): sound; update after M5 and M6.
- SECURITY.3: sound. Strict nonce CSP from the Python templates; nonce pages kept out of shared caches.
- CONTRACTS (roll-up): sound.
- CONTRACTS.1: sound. The function-API consumer suites and the BI-column gate are correctly marked inferred; settling L560 for own islands is supported by generated types and the skew diff.
- CONTRACTS.2: sound apart from the L517 attribution (M1). L564 is correctly rejected for stored facts under RECORD.3.
- OPERABILITY (roll-up): sound.
- OPERABILITY.1: sound. Keeping every trace, then tail sampling, is the max over L369's "start with head"; the trace id travels in L566's namespace.
- OPERABILITY.2: sound.
- OPERABILITY.3: sound. Per-role load from pg_stat_statements (it keys statistics by user) and the measured triggers of the Postgres-first placements.
- OPERABILITY.4: sound. Collector outside the application database; the database-side refusal carriers are marked inferred.
- OPERABILITY.5: sound, and correct where its parent is not (M2).
- OPERABILITY.6: sound. Migrations before dependent consumers; no backend runs schema changes (MD-03, L515).
- TOPOLOGY (roll-up), TOPOLOGY.1, TOPOLOGY.3, TOPOLOGY.4: sound. The hosting dependence is surfaced as Q1.
- EVOLUTION (roll-up): sound once B1 and M3 are fixed.
- EVOLUTION.1: sound apart from M3. Domain schemas for future services; no BFF; no micro frontends.
- EVOLUTION.3: sound. Add the HSTS preload ADR (M6).

## Questions

- **J5, none**: upheld. No decided node holds a trade-off between forces it serves that neither the evidence nor a maintainer decision settles. The CONTRACTS departure is correctly decided and flagged, not asked. M3 needs a sentence, not a question.
- **J9 Q1, hosting model**: genuine (a context variable the maintainer did not state), self-contained and fairly framed, with options, costs and the result if unanswered. Keep it. Add one line: under the recommended option, the managed-store authority of SECURITY.4 holds only if the team adds a store, otherwise the file fallback is in force (m6).
- **J1 Q1, read visibility**: kept open in both units with the stated default, matching J1 Q1's "if unanswered" text (A, each backend filters, with the shared specification and shared denial tests). Only the notation needs aligning (m7).
