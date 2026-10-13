# Review: INTERACTION branch (J4 web-app-philosophy, J8 pig-web-defaults)

Adversarial review of `../J4_phil_interaction/` and `../J8_pig_interaction/` (result, records, questions) against the max rule (`../../target_hierarchy.md`), the maintainer decisions MD-01 to MD-03 (`../../maintainer_decisions.md`), the settled placements (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/questions.md`), the ledger (`../../02_skeleton/claims_ledger.md`), the research claims behind doubtful rows, the sibling verdicts where links cross (J3, J5, J6, J7), and two sources fetched during review.

Pinned:
- Findings: blocking 0, major 4, minor 8.
- Major: (M1) "a comment is never more visible than its target on any surface" is not true under the recorded read-visibility default, where reporting and operator roles that can SELECT the table see every comment (J4 COLLABORATE, J8 REALTIME.4, COLLABORATE.4); (M2) J4 ENVIRONMENT.6 says no token ever travels in a URL, but J7 PROCESS.6 serves files through short-lived signed URLs (J4 ENVIRONMENT.6 against J7); (M3) MD-02's "always in sync" and J4's compatibility window are applied to OpenAPI but not to the MCP tool surface J8 adds, and no sibling covers it (J8 AGENT.1); (M4) the automated-traffic row L652 is called "composed, neither has to lose", but its position (a) still wins for flows that hand out scarce goods, where per-agent quotas do not stop someone with many accounts (J4 AGENT, J4 questions).
- Verdicts against the maintainer doctrine: J4 0, J8 0. Confirmed: no verdict contradicts a MAINT row, and the max rule supports each verdict. J8 cites only L566 and leaves L525 and L523 (deletion doctrine) unweighed where it allows hard deletion for erasure (m6).
- Maintainer decisions: MD-01, MD-02 and MD-03 are applied faithfully; MD-02 is applied to one agent-facing interface only (M3).
- Questions: J4 0 and J8 0 new, confirmed. No decided node needs to become a question. The inherited read-visibility clause stays open in J4 COLLABORATE, J8 REALTIME.4 and COLLABORATE.4, with J1's stated default (each backend filters from one shared specification, with shared denial tests). M1 adds a consequence to feed into that question, not a new question. L652 needs a "wins when" condition, not a question.

## Findings

Severity: **blocking** stops graph building; **major** changes what a node states or creates a contradiction the graph would carry; **minor** is a wording, grounding or completeness fix.

### Major

**M1. Comment visibility "on any surface" does not hold under the recorded default for consumers that are not backends**
- Nodes: INTERACTION.COLLABORATE (J4, decision 7); PIG-WEB.INTERACTION.REALTIME.4 and COLLABORATE.4 (J8).
- Issue: J4 states that a comment is never more visible than its target "on any surface" (L687), exports included (L686). The recorded default for the open clause (A: each backend filters) only binds backends. J1 Q1 names the cost of A itself: "Any role with SELECT on the table, BI and operator roles included, sees every user's rows in the columns it is granted." So internal notes and narrow-audience replies are visible to reporting and operator roles, and also through counts and exports those roles produce. Neither unit says this. The principle is stated as absolute while its default realization breaks it.
- Evidence: `../J1_allocation/questions.md` Q1, position A costs; J3 LOGIC.SECURE ("per-role grants bound the damage"); J5 TRANSVERSE.SECURITY (reporting column grants exclude personal data by default); L686 ("including streams and exports"), L687.
- Fix: keep the clause open and keep default A. Add to the recorded default in all three nodes: "until Q1 is answered, reporting and operator roles get no SELECT on comment content or on comments with a narrower audience than their target; they read comments only through a projection limited to target-wide audiences, or not at all." Also add this as a named consequence to Q1's position A, so the maintainer sees that comments are affected. If that grant restriction is rejected, state the leak as a known limit of default A rather than claim "any surface".

**M2. "No credentials or tokens in URLs" contradicts the sibling verdict on file serving**
- Node: INTERACTION.ENVIRONMENT.6 (J4), against PIG-WEB.LOGIC.PROCESS.6 and .4 (J7).
- Issue: J4 states "credentials and tokens never travel in them". It marks this as generalized from L459, which is about WebSocket tokens. J7 serves every file by redirecting to "a short-lived signed URL for that one object" and states that "a presigned URL is a bearer token" (L422). J8 AGENT.2 also relies on OAuth redirects, which carry an authorization code in the URL. The graph would carry a principle that one of its own realizations breaks.
- Evidence: `../J4_phil_interaction/records.md` ENVIRONMENT.6; `../J7_pig_logic/records.md` PROCESS.4 (P4, L422) and PROCESS.6; L459.
- Fix: narrow the verdict. No session token, long-lived credential or reusable secret ever goes in a URL. A capability URL is acceptable when all of these hold: it is issued only after an authorization check, scoped to one object and one operation, short-lived, served from another origin, with the issuing response `no-store` and a referrer policy that does not leak it. One-time authorization codes bound by PKCE are acceptable under the identity placement. Mark the condition inferred.

**M3. MD-02 and the compatibility window do not reach the MCP tool surface**
- Node: PIG-WEB.INTERACTION.AGENT.1 (J8); also J4 ENVIRONMENT.3.
- Issue: J8 adds an MCP adapter as the default agent surface. It applies MD-02 ("always in sync", per-project origin, CI gate on drift) to the OpenAPI description only. The MCP tool names, input schemas and result shapes are a second interface description that agents the team does not deploy depend on. J4 ENVIRONMENT.3 already states that "the agent tools and their schemas" are contracts under the compatibility window, but J8 does not realize that. No sibling realizes it either: the grep of J7 EXPOSE.6, EXPOSE.7 and J9 CONTRACTS.1 finds no mention of MCP or tool schemas. As written, the tool surface can drift from the core and can break old agents at a deploy.
- Evidence: MD-02; `../J8_pig_interaction/records.md` AGENT.1 decision; `../J4_phil_interaction/records.md` ENVIRONMENT.3 (third bullet); J5 TRANSVERSE.CONTRACTS (expand, migrate, contract for every contract).
- Fix: add to AGENT.1 that the tool list and schemas have one origin. They are generated from the core description, or checked against it for conformance, with the same CI drift gate (hand-off to PIG-WEB.TRANSVERSE.CONTRACTS.1). They change additively. A breaking tool change goes expand, migrate, contract under the window J4 sets. Add the matching hand-off line to the CONTRACTS.1 judge.

**M4. L652 is a contested row whose position (a) still wins somewhere; "neither has to lose" overclaims**
- Node: INTERACTION.AGENT (J4, decision 7, and `questions.md`); carried into J8 AGENT.5.
- Issue: the ledger row states the trade-off itself: "serves business integrity against agent access". Position (a), denying non-human patterns, "wins for scarce-inventory or abuse-prone flows". J4's composition admits identified agents on harmful flows under per-agent quotas and owner approval, and denies only anonymous automation. Per-agent quotas and owner approval do not stop one party that runs many accounts, each with its own approved agent. That is the scalping and referral-abuse case (L034's flows). The composition resolves the default context, which has few scarce flows, but it is not true in general. The records say P9 wins "only for anonymous automation", which drops the ledger's own winning condition.
- Evidence: L652 (positions a and b with their conditions), L034; `../J4_phil_interaction/questions.md`.
- Fix: keep the composed default. Add under Rejected: "(a) wins on a flow that hands out scarce goods or rewards automation per account (limited stock, referral credit). There, completing the flow requires a human, or agents are excluded from it, whatever their identity." Name the list of such flows as a decision recorded per project. Reword the questions file: the contest is resolved per flow by a condition, not dissolved. No question is needed.

### Minor

**m1. ENVIRONMENT.3 still waits on a verdict that now exists** (J4 ENVIRONMENT.3)
- J5 TRANSVERSE.CONTRACTS is available. It names expand, migrate, contract as the sequence for any breaking change, says usage is known per consumer role, and rejects lockstep for browser clients. J4 offers "a versioned path or routing to the matching server" and keeps `gap: TRANSVERSE.CONTRACTS verdict not yet available`.
- Fix: align the record. Expand, migrate, contract is the sequence; a versioned path and routing to the matching server are the mechanisms that move old tabs during the migrate phase. Drop the gap and update the pinned gap count.

**m2. The "thread's opener may resolve" rule has no source** (J4 COLLABORATE decision 6; J8 COLLABORATE.2)
- L671 and its source (COLLAB-S25: "resolve if you opened the PR or have write access") name the target's author and users with write rights on the target. Nobody names the opener of the thread.
- Fix: use "the target's author" as the example decided from the row. Mark the thread-opener right as inferred, or drop it.

**m3. "Every form POSTs" contradicts navigable state in the URL** (J8 EDIT decision 1)
- Search and filter forms must be GET so their state lands in the URL (J8 VISUALIZE.2, J4 ENVIRONMENT.6, L292).
- Fix: "every state-changing form POSTs".

**m4. The 428 rule clashes with per-property fields, and 412/428 do not fit a hidden form field** (J8 EDIT decisions 2 and 3)
- 428 "on every endpoint editing such a record" conflicts with the record's own exception: per-property last-writer-wins fields are sent "without the record version". RFC 9110 defines 412 and 428 for conditional header fields. A version carried in a hidden form field that no longer matches is a conflict with current state, which J7 EXPOSE.2 maps to 409.
- Fix: exempt per-property updates from 428. For HTML forms, answer the stale write with 409 and the conflict form. Keep 412 and 428 for `If-Match` clients.

**m5. Stronger grounding for AA exists and was checked** (J8 VISUALIZE.4)
- Fetched during review: W3C, Understanding WCAG 2.2, Conformance. The AAA sentence J8 quotes is verbatim, and the page calls the choice of level "fundamentally a policy decision". Also fetched: the US Department of Justice ADA Title II web rule (2024) adopts WCAG 2.1 Level AA as the technical standard for state and local governments. That is a legal floor at AA in one jurisdiction. Moving from A to AA needs no outside knowledge, because AA contains A and the max rule picks the most demanding level every page can meet.
- Fix: register both sources. Replace "inferred from knowledge of the standard" with that argument from the max rule. Narrow the gap "legal mandates not read" to "other jurisdictions not read". Mark AA as grounded through the W3C page plus the max rule.

**m6. The deletion doctrine is not weighed** (J8 COLLABORATE.2, COLLABORATE.4)
- MAINT rows L525 (hard deletion only for rebuildable derived data, or after an archive copy in the same operation; no DELETE grants) and L523 (soft-delete cascades through functions) bear directly on "hard delete when erasure demands" and "remove only under a retention or legal rule". An archive copy defeats erasure, so there is a tension. "0 against the doctrine" still holds, because tombstones are updates, but the citation is incomplete.
- Fix: cite L525 and L523, record the erasure-versus-archive tension, and hand it to the deferred personal-data node (PIG-WEB.DATA.MAINTAIN.6).

**m7. Drafts in browser storage on sensitive pages** (J8 VISUALIZE.2, EDIT decision 6)
- Unsaved input is persisted to browser storage on page hide. On pages that show sensitive data, which J8 ENVIRONMENT.1 marks `no-store`, the drafts stay on shared devices after the session ends.
- Fix: on sensitive pages, drafts go to per-tab storage only or are not persisted, and are cleared on logout. Mark as inferred.

**m8. Two latency and availability costs of the Postgres wake-up path are unrecorded** (J8 REALTIME.5, REALTIME.2)
- First, a full notification queue makes committing transactions fail (L462). With `NOTIFY` issued from writer functions, one stuck listener can fail core writes. Second, the commit-safe cursor that J6 CONCURRENCY.5 realizes uses the `xid8` horizon, so one long transaction on the primary holds back every push and every catch-up.
- Fix: `NOTIFY` only from writer functions whose changes have live subscribers. Listener sessions under the idle-in-transaction timeout (J6, L202). Record the horizon stall as a known latency cost, monitored like the queue.

## Nodes found sound

J4 web-app-philosophy:
- INTERACTION (roll-up): sound, apart from M1, which reaches it through COLLABORATE.
- VISUALIZE: sound. The max choice is accessibility from the first design. The level is honestly handed off. `known` on one weak row is acceptable because the verdict also follows from PRESENT.1.
- COLLABORATE: sound on the cursor correction (L594 over L682, matching J6 CONCURRENCY.5), channel order, conflicts (GUARD.5), presence, comment entities and separate abilities. Findings M1 and m2 apply.
- AGENT: sound on tokens, scopes, tools, the three-capability rule, idempotency and audit. Finding M4 applies.
- ENVIRONMENT (roll-up): sound.
- ENVIRONMENT.1: sound; the HTML-first approach follows PRESENT.1.
- ENVIRONMENT.2: sound; the server arbitrates across tabs and client coordination is only a copy.
- ENVIRONMENT.3: sound in substance; m1 applies.
- ENVIRONMENT.4: sound; the owned-CDN condition is correctly marked inferred.
- ENVIRONMENT.5: sound.
- ENVIRONMENT.6: sound on stable URLs and state in the URL; M2 applies.
- ENVIRONMENT.7: sound. Escaping before CSP, CSRF independent of CORS, and the distinct registrable domain are each the strongest option.

J8 pig-web-defaults:
- INTERACTION, VISUALIZE, REALTIME, COLLABORATE, AGENT, ENVIRONMENT (roll-ups): sound; each states its children faithfully.
- VISUALIZE.1: sound; realizes PRESENT.1 and JS_SERVER; library choice correctly left open.
- VISUALIZE.2: sound; m7 applies.
- VISUALIZE.3: sound.
- VISUALIZE.4: sound verdict (AA on every page, AAA only per criterion, native first); m5 strengthens its grounding.
- EDIT: sound on 303, required preconditions, conflict shown with both versions, and one database API call per transaction (MD-03, DB_API); m3 and m4 apply.
- REALTIME.1: sound. SSE as the default holds because correctness does not depend on the channel; L437 is narrowed correctly by POSTGRES_FIRST.
- REALTIME.2: sound; m8 applies.
- REALTIME.3: sound; Redis only at a measured limit or when the framework requires it, matching POSTGRES_FIRST.
- REALTIME.4: sound on origin, cookie authentication, filtering per event, and payloads that carry only identifiers; M1 applies.
- REALTIME.5: sound; the wake-up role and the writer function as the issuer match MD-03; m8 applies.
- COLLABORATE.1: sound; recording the version "always" follows from GUARD.5 and ACT.4.
- COLLABORATE.2: sound; m2 and m6 apply.
- COLLABORATE.3: sound; a server-authoritative engine with the CRDT veto (L680) is the strongest option.
- COLLABORATE.4: sound on notifications as rows written by the writer function and on the recorded moderation; M1 and m6 apply.
- AGENT.1: sound on the layered surface and statelessness; M3 applies.
- AGENT.2: sound.
- AGENT.3: sound; binding tokens by consequence is a fair composition of L641; both identities reach the database (R1-3).
- AGENT.4: sound. The approval held on the server and checked by the writer function is a per-user write rule decidable from the row, so GUARD.3 and R1-1 assign it to that function.
- AGENT.5: sound; nested quotas.
- ENVIRONMENT.1: sound.
- ENVIRONMENT.2 and .3: deferred, recorded only, as planned.

Counts and ownership checked: J4 has 28 owned rows; J8 has 88 owned rows, 20 nodes with rows and 6 roll-ups; J8 proposes 28 links. All recount correctly.
