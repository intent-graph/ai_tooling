# Result: review of the INTERACTION branch (J4 and J8)

## L1 headline

The INTERACTION verdicts of both units hold up under adversarial review: none blocks graph building, none goes against the maintainer doctrine, and MD-01 to MD-03 are applied faithfully. Four major fixes are needed before the graphs are built: one absolute claim the recorded default cannot keep, one contradiction with a sibling verdict, one surface the sync decision misses, and one contested row whose losing side still wins somewhere. The read-visibility question stays open with J1's stated default in every node it reaches. Neither unit needs a new question.

Pinned:
- Findings: blocking 0, major 4, minor 8.
- Major: (M1) "a comment is never more visible than its target on any surface" is not true under the recorded read-visibility default, where reporting and operator roles that can SELECT the table see every comment (J4 COLLABORATE, J8 REALTIME.4, COLLABORATE.4); (M2) J4 ENVIRONMENT.6 says no token ever travels in a URL, but J7 PROCESS.6 serves files through short-lived signed URLs (J4 ENVIRONMENT.6 against J7); (M3) MD-02's "always in sync" and J4's compatibility window are applied to OpenAPI but not to the MCP tool surface J8 adds, and no sibling covers it (J8 AGENT.1); (M4) the automated-traffic row L652 is called "composed, neither has to lose", but its position (a) still wins for flows that hand out scarce goods, where per-agent quotas do not stop someone with many accounts (J4 AGENT, J4 questions).
- Verdicts against the maintainer doctrine: J4 0, J8 0. Confirmed: no verdict contradicts a MAINT row, and the max rule supports each verdict. J8 cites only L566 and leaves L525 and L523 (deletion doctrine) unweighed where it allows hard deletion for erasure (m6).
- Maintainer decisions: MD-01, MD-02 and MD-03 are applied faithfully; MD-02 is applied to one agent-facing interface only (M3).
- Questions: J4 0 and J8 0 new, confirmed. No decided node needs to become a question. The inherited read-visibility clause stays open in J4 COLLABORATE, J8 REALTIME.4 and COLLABORATE.4, with J1's stated default (each backend filters from one shared specification, with shared denial tests). M1 adds a consequence to feed into that question, not a new question. L652 needs a "wins when" condition, not a question.

## L2 claims

- **Major fixes** (each changes what a node states):
  - M1, comment visibility: keep default A and add a grant restriction to it. Until the question is answered, reporting and operator roles get no SELECT on comment content or on comments with a narrower audience than their target. Name this consequence in the open question's position A.
  - M2, URLs: narrow J4's rule to "no session token, long-lived credential or reusable secret in a URL". Accept a capability URL when it is issued after an authorization check, scoped to one object, short-lived, served from another origin and `no-store`. One-time authorization codes bound by PKCE are also acceptable.
  - M3, MCP tools: one origin, generated from or checked against the core description, the same CI drift gate, additive change, and expand, migrate, contract for a breaking change. Add the hand-off to the stack contracts node.
  - M4, L652: add "(a) wins on flows that hand out scarce goods or reward automation per account: a human is required there, or agents are excluded", with the flow list as a per-project decision.
- **Minor fixes**: (m1) align ENVIRONMENT.3 with the now-available contracts verdict; (m2) the thread-opener resolve right has no source, use the target's author; (m3) "every state-changing form POSTs", not every form; (m4) exempt per-property fields from 428, and answer stale hidden-field versions with 409; (m5) register the W3C conformance page and the US ADA Title II rule (WCAG 2.1 AA), both fetched during review; AA over A follows from the max rule; (m6) weigh L525 and L523 on erasure; (m7) no drafts in persistent storage on sensitive pages; (m8) record that a full notification queue fails commits and that one long transaction holds back the commit-safe cursor.
- **Sound**: every other part of the 12 J4 nodes and the 26 judged J8 nodes, one line each in `review.md`. The cursor correction (L594 over L682), SSE by default, no Redis by default, the server-authoritative text engine, approval held on the server and checked by the writer function, AA with AAA per criterion, and one database API call per transaction are each the strongest option and consistent with J1, J6 and J7.
- **Doctrine and decisions**: no verdict against the doctrine in either unit; MD-01 (no row security), MD-02 (OpenAPI always in sync, origin per project) and MD-03 (writer functions, one call per transaction) are applied as decided.

Pinned:
- Findings: blocking 0, major 4, minor 8.
- Major: (M1) "a comment is never more visible than its target on any surface" is not true under the recorded read-visibility default, where reporting and operator roles that can SELECT the table see every comment (J4 COLLABORATE, J8 REALTIME.4, COLLABORATE.4); (M2) J4 ENVIRONMENT.6 says no token ever travels in a URL, but J7 PROCESS.6 serves files through short-lived signed URLs (J4 ENVIRONMENT.6 against J7); (M3) MD-02's "always in sync" and J4's compatibility window are applied to OpenAPI but not to the MCP tool surface J8 adds, and no sibling covers it (J8 AGENT.1); (M4) the automated-traffic row L652 is called "composed, neither has to lose", but its position (a) still wins for flows that hand out scarce goods, where per-agent quotas do not stop someone with many accounts (J4 AGENT, J4 questions).
- Verdicts against the maintainer doctrine: J4 0, J8 0. Confirmed: no verdict contradicts a MAINT row, and the max rule supports each verdict. J8 cites only L566 and leaves L525 and L523 (deletion doctrine) unweighed where it allows hard deletion for erasure (m6).
- Maintainer decisions: MD-01, MD-02 and MD-03 are applied faithfully; MD-02 is applied to one agent-facing interface only (M3).
- Questions: J4 0 and J8 0 new, confirmed. No decided node needs to become a question. The inherited read-visibility clause stays open in J4 COLLABORATE, J8 REALTIME.4 and COLLABORATE.4, with J1's stated default (each backend filters from one shared specification, with shared denial tests). M1 adds a consequence to feed into that question, not a new question. L652 needs a "wins when" condition, not a question.

## L3 full

The full findings (node, issue, evidence, proposed fix) and the one-line soundness list are in `review.md` (this folder). This section gives the basis and the verdict on each check.

### Basis

- Read: the target hierarchy and selection rule; MD-01 to MD-03; the allocation matrix and J1's open question in full; J4 and J8 result, records and questions in full.
- Sibling verdicts checked where links cross: J3 LOGIC.SECURE (read-visibility default), J5 TRANSVERSE.CONTRACTS, J6 DATA.CONCURRENCY.5 (commit-safe cursor), J7 PROCESS.4 and .6 (signed URLs), EXPOSE.2 (status codes).
- Ledger rows read for the doubtful claims: L005, L006, L009, L010, L011, L014, L017, L018, L024 to L028, L034, L127, L258, L260, L291 to L294, L300, L301, L435 to L437, L443 to L446, L451, L457, L459 to L463, L465, L582, L583, L594, L640, L642, L645, L648, L652, L664 to L680, L682, L683, L686, L687, L689; the MAINT rows that touch this branch.
- Research checked: the collaboration slot's claims C08, C26 and C32, with the source note behind the resolve rule.
- Fetched: W3C "Understanding WCAG 2.2: Conformance" (the AAA sentence is verbatim; the level is "fundamentally a policy decision"); the US ADA Title II web rule page (adopts WCAG 2.1 Level AA).

### Verdict on each check

- (a) Hedging or averaging: none found. Each contested row is decided with "acceptable when" conditions. The only overclaim is M4, which calls a per-flow resolution a dissolved contest.
- (b) Grounding and certainty words: honest overall; inferred parts are marked. Gaps: m2 (ungrounded example), m5 (stronger grounding available).
- (c) Consistency:
  - with J1: no placement re-decided;
  - with the maintainer decisions: faithful (M3 extends MD-02's reach);
  - between the units: J8 never contradicts J4, apart from J4's unrealized agent-tool window (M3);
  - with siblings: M2 (against J7), m1 (J5 now available), m4 (J7's 409);
  - within J8: m3 and m4.
- (d) Stronger evidence missed: m5 (legal AA floor), m6 (deletion doctrine).
- (e) Against the doctrine: none; the max rule supports each verdict.
- (f) Questions: zero new is correct. The read-visibility clause is kept open with J1's default in every node it reaches, and is not re-decided. No decided node should be a question.

Pinned:
- Findings: blocking 0, major 4, minor 8.
- Major: (M1) "a comment is never more visible than its target on any surface" is not true under the recorded read-visibility default, where reporting and operator roles that can SELECT the table see every comment (J4 COLLABORATE, J8 REALTIME.4, COLLABORATE.4); (M2) J4 ENVIRONMENT.6 says no token ever travels in a URL, but J7 PROCESS.6 serves files through short-lived signed URLs (J4 ENVIRONMENT.6 against J7); (M3) MD-02's "always in sync" and J4's compatibility window are applied to OpenAPI but not to the MCP tool surface J8 adds, and no sibling covers it (J8 AGENT.1); (M4) the automated-traffic row L652 is called "composed, neither has to lose", but its position (a) still wins for flows that hand out scarce goods, where per-agent quotas do not stop someone with many accounts (J4 AGENT, J4 questions).
- Verdicts against the maintainer doctrine: J4 0, J8 0. Confirmed: no verdict contradicts a MAINT row, and the max rule supports each verdict. J8 cites only L566 and leaves L525 and L523 (deletion doctrine) unweighed where it allows hard deletion for erasure (m6).
- Maintainer decisions: MD-01, MD-02 and MD-03 are applied faithfully; MD-02 is applied to one agent-facing interface only (M3).
- Questions: J4 0 and J8 0 new, confirmed. No decided node needs to become a question. The inherited read-visibility clause stays open in J4 COLLABORATE, J8 REALTIME.4 and COLLABORATE.4, with J1's stated default (each backend filters from one shared specification, with shared denial tests). M1 adds a consequence to feed into that question, not a new question. L652 needs a "wins when" condition, not a question.
