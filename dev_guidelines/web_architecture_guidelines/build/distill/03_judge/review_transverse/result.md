# Result: review of the TRANSVERSE branch (J5 philosophy, J9 stack)

## L1 headline

The TRANSVERSE verdicts mostly hold, but they need one blocking fix and six major ones before the graphs are built:
- **Blocking**: J9's module rule would make the backend compose cross-domain operations from several calls, which ACT.1 and MD-03 forbid.
- **Major**:
  - the departure from L517 is counted, and its lockstep exception worded, differently in four judges;
  - J5's "every database test never commits" contradicts J9's committing concurrency tests;
  - "one backend deployable" is not reconciled with MD-03's several backends;
  - the OWASP map misreads A08 and under-weighs A06;
  - SLSA stops at Build L2 although its source targets L3;
  - HSTS preload is made a default, which the preload list's operators advise against.

The maintainer decisions are applied faithfully except at those two MD-03 points. The read-visibility question stays open with its stated default. The one question (J9, hosting model) is genuine.

Pinned:
- Findings: 14. Blocking 1, major 6, minor 7.
- Blocking: B1 PIG-WEB.TRANSVERSE.EVOLUTION.2 forbids a module from calling another domain's database functions, which forces cross-domain business operations to be composed of several API calls in the backend, against ACT.1 and MD-03.
- Major: M1 the departure from L517 is counted 0, 1 and 1 by J9, J5 and J6, and the lockstep exception has three different conditions across J2, J5 and J6. M2 J5 OPERABILITY.2 says every database test is a never-committing transaction; J9 OPERABILITY.5, which refines it, requires committing tests, and the concurrency testing that GUARD.2 needs is left as a gap. M3 J5 EVOLUTION.3 and J9 EVOLUTION.1 say "one backend deployable" without reconciling it with MD-03's several backends. M4 the OWASP tier map in TRANSVERSE.SECURITY misreads A08 and misses the threat modelling and misuse-case tests that A06 prescribes. M5 J9 SECURITY.5 stops at SLSA Build L2, although its own source says Build L3 is intended for most releases. M6 J9 SECURITY.2 makes HSTS preload the default end state, which the operators of the preload list advise against.
- Minor: m1 ASVS Level 2 can be grounded (the ASVS 5.0 text says most applications should strive for it). m2 J9 PERFORMANCE overstates the gap on a server latency target (L297, L013 and ACT.3's 1 s already bound it). m3 J9 TOPOLOGY.2's sync workers ignore blocking calls made in the request (the OIDC code exchange of GUARD.4). m4 J5 OPERABILITY.1 keeps every data-change event out of the security log, including privilege and credential changes. m5 J5 EVOLUTION.5 leaves cross-schema functions without an owner. m6 J9 SECURITY.4 calls the environment fallback "not the default", but its own assumed hosting triggers it. m7 the pending read-visibility clause has three notations across judges (`undecided:`, `awaiting maintainer:`, `open:`), and J5 OPERABILITY.2's state omits it.
- Verdicts against the doctrine: J5 TRANSVERSE.CONTRACTS against L517 "deployed together" is upheld: the max rule is on its side, and the maintainer's own L512 (new named version, gradual migration) supports it; count it once, at its owner. J9's "0 against the doctrine" holds only as "0 new": J9 realizes the same departure, and the "new function name" it credits to L517 is J5's expand step, not L517's text. J9's adoptions of L567, L545 and L566 are upheld; committing tests in a disposable database do not breach L567, which governs shared environments.
- Questions: J5 has none, which is upheld; no decided node should become a question (M3 is a reconciliation, not a trade-off). J9 Q1 on the hosting model is a genuine context check, self-contained and fairly framed; keep it, and add that under the recommended option the managed secret store holds only if one is added. Both units keep J1's read-visibility question open with its stated default (each backend filters, shared specification, shared denial tests), word for word with J1 Q1's "if unanswered".
- Maintainer decisions: MD-01 and MD-02 are applied faithfully in both units. MD-03 is applied everywhere except at two points: the "one backend" default (M3) and the module rule (B1).

## L2 claims

Full findings with evidence and proposed fixes: `review.md`. One line each:

- **B1, blocking, PIG-WEB.TRANSVERSE.EVOLUTION.2**: "never through another module's functions" leaves two choices for a cross-domain operation, two transactions or one wrapping transaction, and ACT.1 forbids the second. Fix: the boundary forbids only other domains' tables; a cross-domain operation is one database function.
- **M1, major, CONTRACTS (J5), CONTRACTS.2 and OPERABILITY.6 (J9)**, crossing to J2 and J6: one L517 departure is counted 0, 1, 1 and 0, under three lockstep conditions; J6's is weaker than the principle. Fix: count it once at PIG-WEB.DATA.INTERFACE.1, use J5's condition everywhere, and cite L512 as the maintainer's own precedent.
- **M2, major, OPERABILITY.2 (J5), OPERABILITY.5 (J9)**: the parent requires every database test to be a never-committing transaction; the child correctly adds committing concurrency tests. Fix: rewrite the parent; require a concurrent test for every invariant GUARD.2 enforces procedurally.
- **M3, major, EVOLUTION.3 (J5), EVOLUTION.1 (J9)**: say that the other backends of MD-03 are other products, teams or languages, and the team's own product is one deployable; weigh that the shared data seam lowers the cost of a later split.
- **M4, major, TRANSVERSE.SECURITY (J5)**: A08 means untrusted code and data, not database constraints; A06 calls for threat modelling and misuse-case tests per tier; A04 also covers transport and data at rest.
- **M5, major, SECURITY.5 (J9)**: SRC-242 says Build L3 is "intended for most software releases". Fix: L3 is the target, L2 acceptable when the build platform cannot harden runs; remove the gap.
- **M6, major, SECURITY.2 (J9)**: preload only when the team controls the registrable domain and commits every subdomain, internal ones included, recorded as an ADR; the default end state is HSTS with includeSubDomains on the application's host.
- **Minor**:
  - m1 ground ASVS Level 2 from the ASVS 5.0 text;
  - m2 derive a server budget from L297, L013 and ACT.3;
  - m3 threaded or ASGI workers for blocking calls made in the request (the OIDC exchange);
  - m4 security-relevant data changes belong in the security log;
  - m5 an owner for cross-schema functions;
  - m6 the secrets default under the assumed hosting;
  - m7 one notation for the pending read-visibility clause.
- **Doctrine**: J5's CONTRACTS verdict against L517 is upheld under the max rule. J9's adoptions of L567, L545 and L566 are upheld. J9's "0 against the doctrine" holds only as "0 new".
- **Questions**: J5's "none" is upheld. J9 Q1 is kept, with the secrets consequence added. J1 Q1 stays open with its stated default in both units.
- **Sound**: 9 of J5's 14 nodes; 20 of J9's 27 judged nodes, some with small updates after the fixes. Listed one per line in `review.md`.

Pinned:
- Findings: 14. Blocking 1, major 6, minor 7.
- Blocking: B1 PIG-WEB.TRANSVERSE.EVOLUTION.2 forbids a module from calling another domain's database functions, which forces cross-domain business operations to be composed of several API calls in the backend, against ACT.1 and MD-03.
- Major: M1 the departure from L517 is counted 0, 1 and 1 by J9, J5 and J6, and the lockstep exception has three different conditions across J2, J5 and J6. M2 J5 OPERABILITY.2 says every database test is a never-committing transaction; J9 OPERABILITY.5, which refines it, requires committing tests, and the concurrency testing that GUARD.2 needs is left as a gap. M3 J5 EVOLUTION.3 and J9 EVOLUTION.1 say "one backend deployable" without reconciling it with MD-03's several backends. M4 the OWASP tier map in TRANSVERSE.SECURITY misreads A08 and misses the threat modelling and misuse-case tests that A06 prescribes. M5 J9 SECURITY.5 stops at SLSA Build L2, although its own source says Build L3 is intended for most releases. M6 J9 SECURITY.2 makes HSTS preload the default end state, which the operators of the preload list advise against.
- Minor: m1 ASVS Level 2 can be grounded (the ASVS 5.0 text says most applications should strive for it). m2 J9 PERFORMANCE overstates the gap on a server latency target (L297, L013 and ACT.3's 1 s already bound it). m3 J9 TOPOLOGY.2's sync workers ignore blocking calls made in the request (the OIDC code exchange of GUARD.4). m4 J5 OPERABILITY.1 keeps every data-change event out of the security log, including privilege and credential changes. m5 J5 EVOLUTION.5 leaves cross-schema functions without an owner. m6 J9 SECURITY.4 calls the environment fallback "not the default", but its own assumed hosting triggers it. m7 the pending read-visibility clause has three notations across judges (`undecided:`, `awaiting maintainer:`, `open:`), and J5 OPERABILITY.2's state omits it.
- Verdicts against the doctrine: J5 TRANSVERSE.CONTRACTS against L517 "deployed together" is upheld: the max rule is on its side, and the maintainer's own L512 (new named version, gradual migration) supports it; count it once, at its owner. J9's "0 against the doctrine" holds only as "0 new": J9 realizes the same departure, and the "new function name" it credits to L517 is J5's expand step, not L517's text. J9's adoptions of L567, L545 and L566 are upheld; committing tests in a disposable database do not breach L567, which governs shared environments.
- Questions: J5 has none, which is upheld; no decided node should become a question (M3 is a reconciliation, not a trade-off). J9 Q1 on the hosting model is a genuine context check, self-contained and fairly framed; keep it, and add that under the recommended option the managed secret store holds only if one is added. Both units keep J1's read-visibility question open with its stated default (each backend filters, shared specification, shared denial tests), word for word with J1 Q1's "if unanswered".
- Maintainer decisions: MD-01 and MD-02 are applied faithfully in both units. MD-03 is applied everywhere except at two points: the "one backend" default (M3) and the module rule (B1).

## L3 full

### Scope and method

- Under review: `../J5_phil_transverse/` and `../J9_pig_transverse/` (`result.md`, `records.md`, `questions.md` each), all read in full.
- Yardsticks read in full: `../../target_hierarchy.md`, `../../maintainer_decisions.md`, `../J1_allocation/allocation_matrix.md`, `../J1_allocation/questions.md` (Q1).
- Cross-branch reads, on the L517 point and the notation only: `../J2_phil_data/records.md`, `../J6_pig_data/records.md` and `result.md`, `../J3_phil_logic/records.md` (notation); `../J1_allocation/records.md` (default context, access paths, state notation).
- Ledger rows read for this review: L009, L013, L015, L029, L036, L044, L047 to L049, L056, L058, L068, L073, L098, L099, L111, L116, L117, L127, L140, L147, L148, L153, L157, L295, L297, L303, L304, L310, L350, L351, L357, L369, L376, L385, L389, L400, L402, L405, L483, L487, L512, L513, L515 to L517, L519, L545, L560, L564 to L567, L619, L620, L622, L633, L658, L688. Sources resolved in `../../02_skeleton/sources.md`: SRC-016, SRC-077, SRC-113, SRC-115, SRC-120, SRC-227, SRC-242.
- Sources fetched where the stakes were high:
  - the OWASP Top 10:2025 pages for A08 and A06 (M4);
  - the SLSA v1.0 levels page (M5);
  - hstspreload.org (M6);
  - the ASVS 5.0 "What is the ASVS" chapter at tag v5.0.0 (m1).

  The research claim behind L304 (`../../research/05_identity_security/result.md`, SEC-C60) confirms the earlier fetch failure that left the levels unread.
- Checks per node: (a) hedging or averaging; (b) grounding and certainty words; (c) consistency with J1, the MD decisions, between the two units and with sibling branches; (d) stronger positions missed; (e) verdicts against the doctrine; (f) questions.

### What holds

- **No averaging found.** Where positions compete, both units pick the more demanding one and keep the weaker as "acceptable when":
  - field truth over lab data;
  - expand, migrate, contract over lockstep;
  - a managed secret store over the environment;
  - keeping every trace, then tail sampling, over head sampling;
  - strict CSP over an allowlist.

  The exceptions are M5 and M6, where the stronger position was missed or the default overshoots its condition.
- **Grounding is honest.** Inferences are marked `unvalidated`, and the gap lists are real, apart from three:
  - SLSA (M5), where the cited source already holds the answer;
  - ASVS (m1), now readable;
  - server latency (m2), derivable from grounded rows.
- **J1 placements are realized, not re-decided**, with one exception: B1 contradicts ACT.1.
- **MD-01**: no row security by default; its three conditions become a per-project ADR (J5 EVOLUTION.1, J9 EVOLUTION.3).
- **MD-02**: always-in-sync gate, origin per project (J5 CONTRACTS, J9 CONTRACTS.1, OPERABILITY.6).
- **MD-03**: applied throughout (roles per consumer, the function API as contract, audit and the actor in the database, tests on the real engine), except M3 and B1.
- **The read-visibility clause stays open** in J5 SECURITY and OPERABILITY.2 and in J9 SECURITY.1 and OPERABILITY.5. Each records J1 Q1's "if unanswered" default without deciding it.

### Why B1 is blocking and the others are not

B1 writes into the stack graph a rule whose only compliant execution breaks a settled placement (ACT.1) and a maintainer decision (MD-03). Once built into the graph, it would propagate into the stack's module design. The major findings are:
- inconsistencies across judges (M1, M2, M3);
- a misread or under-weighed source (M4, M5);
- an over-reaching default (M6).

Each needs an edit before the graphs are built, but none forces a contradiction in what a project would build.

### Ownership of the fixes

| finding | edits | owner of the change |
|---|---|---|
| B1 | J9 EVOLUTION.2 (and its roll-up) | J9 |
| M1 | J9 pin, CONTRACTS.2; J5 pin; J2 and J6 pins and the lockstep condition | J6 owns L517; J2, J5, J9 cite |
| M2 | J5 OPERABILITY.2 (decision and state) | J5 |
| M3 | J5 EVOLUTION.3; J9 EVOLUTION.1 and roll-ups | J5, then J9 |
| M4 | J5 TRANSVERSE.SECURITY and pins | J5 |
| M5, M6 | J9 SECURITY.5, SECURITY.2, EVOLUTION.3, SECURITY roll-up | J9 |
| m1 to m7 | as listed in `review.md` | J5 (m4, m5, m7), J9 (m1, m2, m3, m6, m7) |

### Not checked

- The J6, J7 and J8 stack records beyond the L517 point and the hand-offs J9 names (the pool budget, the trace-id namespace, the proxy limits, the ASGI process type): consistent as stated by J9, not verified in those units.
- The research claims behind rows not in doubt: not opened.

Pinned:
- Findings: 14. Blocking 1, major 6, minor 7.
- Blocking: B1 PIG-WEB.TRANSVERSE.EVOLUTION.2 forbids a module from calling another domain's database functions, which forces cross-domain business operations to be composed of several API calls in the backend, against ACT.1 and MD-03.
- Major: M1 the departure from L517 is counted 0, 1 and 1 by J9, J5 and J6, and the lockstep exception has three different conditions across J2, J5 and J6. M2 J5 OPERABILITY.2 says every database test is a never-committing transaction; J9 OPERABILITY.5, which refines it, requires committing tests, and the concurrency testing that GUARD.2 needs is left as a gap. M3 J5 EVOLUTION.3 and J9 EVOLUTION.1 say "one backend deployable" without reconciling it with MD-03's several backends. M4 the OWASP tier map in TRANSVERSE.SECURITY misreads A08 and misses the threat modelling and misuse-case tests that A06 prescribes. M5 J9 SECURITY.5 stops at SLSA Build L2, although its own source says Build L3 is intended for most releases. M6 J9 SECURITY.2 makes HSTS preload the default end state, which the operators of the preload list advise against.
- Minor: m1 ASVS Level 2 can be grounded (the ASVS 5.0 text says most applications should strive for it). m2 J9 PERFORMANCE overstates the gap on a server latency target (L297, L013 and ACT.3's 1 s already bound it). m3 J9 TOPOLOGY.2's sync workers ignore blocking calls made in the request (the OIDC code exchange of GUARD.4). m4 J5 OPERABILITY.1 keeps every data-change event out of the security log, including privilege and credential changes. m5 J5 EVOLUTION.5 leaves cross-schema functions without an owner. m6 J9 SECURITY.4 calls the environment fallback "not the default", but its own assumed hosting triggers it. m7 the pending read-visibility clause has three notations across judges (`undecided:`, `awaiting maintainer:`, `open:`), and J5 OPERABILITY.2's state omits it.
- Verdicts against the doctrine: J5 TRANSVERSE.CONTRACTS against L517 "deployed together" is upheld: the max rule is on its side, and the maintainer's own L512 (new named version, gradual migration) supports it; count it once, at its owner. J9's "0 against the doctrine" holds only as "0 new": J9 realizes the same departure, and the "new function name" it credits to L517 is J5's expand step, not L517's text. J9's adoptions of L567, L545 and L566 are upheld; committing tests in a disposable database do not breach L567, which governs shared environments.
- Questions: J5 has none, which is upheld; no decided node should become a question (M3 is a reconciliation, not a trade-off). J9 Q1 on the hosting model is a genuine context check, self-contained and fairly framed; keep it, and add that under the recommended option the managed secret store holds only if one is added. Both units keep J1's read-visibility question open with its stated default (each backend filters, shared specification, shared denial tests), word for word with J1 Q1's "if unanswered".
- Maintainer decisions: MD-01 and MD-02 are applied faithfully in both units. MD-03 is applied everywhere except at two points: the "one backend" default (M3) and the module rule (B1).
