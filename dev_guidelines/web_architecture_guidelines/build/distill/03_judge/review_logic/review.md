# LOGIC branch (J3 philosophy, J7 stack): adversarial review

This review checks the judged LOGIC branch before the graphs are built from it:
- `../J3_phil_logic/` (8 nodes of `web-app-philosophy`);
- `../J7_pig_logic/` (31 nodes of `pig-web-defaults`, 30 judged).

It reads them against the selection rule (`../../target_hierarchy.md`), the maintainer decisions MD-01 to MD-03 (`../../maintainer_decisions.md`, not under review: checked for faithful application) and the settled placements (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`). Evidence ids `Lnnn` resolve in `../../02_skeleton/claims_ledger.md`.

Certainty: **grounded** = I read it (ledger row, record, or the source fetched); **inferred** = it follows from the records or from Postgres or HTTP behaviour, but no ledger row states it.

Checked and found correct: owned-row counts (28 LOGIC, 133 PIG-WEB.LOGIC, counted in the ledger); the inherited read-visibility default matches J1's Q1 wording; MD-01 (no row security, backend checks kept), MD-02 (description always in sync, origin per project, CI gate) and MD-03 (one function call per operation, actor asserted, multi-table work in the database) are applied as written in both units.

Pinned:
- Findings: blocking 0, major 7, minor 12.
- Major: M1 read-visibility fallback B dropped (J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6); M2 autocommit reads cannot carry the actor read functions need (J7 ENFORCE.2); M3 concurrent-duplicate rule wrong for multi-phase keyed operations (J7 EXPOSE.3 against PROCESS.2); M4 foreign mutation inside the request against ACT.3's forbidden column, inherited from ACT.2 (J7 PROCESS.2); M5 SameSite=Lax decided on a force the branch says it does not serve (J7 SECURE.2); M6 MFA required but never verified on delegated logins (J7 SECURE.4, SECURE.5); M7 MAINT row L530 missed: error codes and the override flag for blockable rules (J7 EXPOSE.2, SECURE.1).
- Verdicts against the doctrine: J3 0 and J7 0, both confirmed; none contradicts a MAINT row; J7 under-weighs L530 (M7) and does not cite L587, which supports its EXPOSE.3.
- Questions: J3 none, agreed. J7 none: agreed on framework, login delegation, upload path, version location and limiter state; disagreed on SameSite (decide by max or raise it, M5). Inherited read-visibility question: kept open with J1's default in both units, but without J1's fallback B (M1).
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully in both units; J1 placements realized, except the ACT.3 tension in M4, which J1 itself carries.

## Major findings

### M1 Read visibility: J1's fallback B is dropped, and the verdicts that flip with Q1 are not marked

**Nodes**: J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6.

**Issue.** J1's stated default for the unanswered question has three parts: A provisional (each backend filters, shared specification, shared denial tests), **B as "acceptable when a per-user read rule must hold for two or more backends"**, and GUARD.3's clause `undecided`. Both units record A and "awaiting maintainer" but never B. J1 recommends B to the maintainer. If the maintainer answers B, these verdicts change, and none of them says so:
- ENFORCE.3: "simple reads on base tables under SELECT grants" (tables with per-user rules lose direct SELECT under B);
- SECURE.1 step 4 and PROCESS.6: the per-user read rule moves from the backend's statement into a read function;
- ENFORCE.2: those reads then need the actor in a transaction (M2).

**Evidence** (grounded): `../J1_allocation/questions.md`, Q1 "If unanswered, the graph records: A as the provisional default …; B as 'acceptable when …'"; `../J1_allocation/records.md` GUARD.3 "Moved by: … Q1's answer (read visibility into read functions)".

**Fix**: in J3 LOGIC.SECURE and J7 SECURE.1, add B's "acceptable when" line as J1 words it. In ENFORCE.3, SECURE.1 and PROCESS.6, add one line: "under Q1-B: the read goes through the read function; the table loses direct SELECT". Note for J1's owner: B's condition, "two or more backends", already holds in MD-03's default context. A reader will take this as B winning by default, so J1 should reword it.

### M2 Reads "in autocommit" cannot carry the actor that read functions need

**Node**: J7 ENFORCE.2 (step 3), with ENFORCE.3.

**Issue.** ENFORCE.2 runs reads in autocommit and gives only the write transaction the actor setting. DB_API (and ENFORCE.3) also require "read functions where a read must apply a rule". L566 (MAINT) and L311 say functions read the acting user from a **transaction-local** setting. In autocommit, a `set_config(…, true)` call is its own transaction, so it is gone before the next statement. A read function that needs the actor therefore sees none. It then fails, or filters nothing if written leniently. Under Q1-B (M1) every per-user read takes this path.

**Evidence**: L566, L311 (grounded); DB_API in `../J1_allocation/records.md` ("read functions where a read must apply a rule"); Postgres scoping of `SET LOCAL` and `set_config(…, true)` to the current transaction (inferred from Postgres behaviour, not in the ledger).

**Fix**: "Plain reads run in autocommit. A read that calls a read function, or under Q1-B any per-user read, runs in a short read-only transaction that sets the actor and makes the one read call. It goes through the same generated wrapper as writes." Read functions refuse a missing actor, as writer functions do (GUARD.3, R1-3).

### M3 The concurrent-duplicate rule is wrong for multi-phase keyed operations

**Node**: J7 EXPOSE.3 (steps 3 and Rejected), against J7 PROCESS.2 (step 3).

**Issue.** EXPOSE.3 makes a concurrent duplicate wait on the key's unique index and then get the replay. It rejects the 409 answer, which it says is only for requests that hold a transaction long, "which one-call transactions exclude". PROCESS.2 step 3 runs the operations that most need keys, payment-like creates, as **atomic phases**: several commits, a recovery point after each, a foreign call between them (L589). There the key row is committed in the first phase, long before any final outcome exists. A duplicate arriving mid-flight finds a key with no outcome to replay, and EXPOSE.3 does not say what happens next. Re-executing from the recovery point runs the foreign call twice in parallel. Only the foreign system's key then prevents a double charge.

**Evidence** (grounded): L589 (atomic phases, recovery points, key passed to the foreign system); L546 (a retry while the first is running gets 409, or is serialized behind a locked key row, SRC-267); EXPOSE.3's own text.

**Fix**: split by operation shape. For a single-call operation, keep EXPOSE.3's rule (wait on the unique index, then replay). For a multi-phase operation, the key row carries the recovery point and a lock with an expiry. A duplicate that finds the key locked gets 409 with `Retry-After`. After completion it gets the replay. A duplicate that finds an expired lock is resumed by the completer (L589). Then narrow the rejection of 409 to single-call operations.

### M4 A foreign mutation inside the request goes against ACT.3's forbidden column

**Node**: J7 PROCESS.2 (step 3), PROCESS.3 (request-path retries); pinned "Conflicts with J1 placements: 0".

**Issue.** PROCESS.2 runs "foreign mutations the user waits for (a payment)" as atomic phases in the request, following J1's ACT.2 text. J1's ACT.3 placement lists "foreign effects inside the request" as **forbidden** and puts foreign effects among deferred work. J1 contradicts itself here, and J7 inherits the contradiction without recording it. The resolution that satisfies both placements is the 202 path that EXPOSE.3 already builds: the atomic phases run in a worker behind a status resource. It is also J7's own argument against holding synchronous workers on slow I/O (PROCESS.4, ENFORCE.4).

**Evidence** (grounded): `../J1_allocation/records.md` ACT.2 ("A foreign mutation the user waits for (a payment) runs as atomic phases …") and ACT.3 ("Forbidden: deferring core writes; foreign effects inside the request"; "Deferred: foreign effects …").

**Fix**: in PROCESS.2 step 3, foreign mutations run as atomic phases in a worker. The request writes the intent with its key through the API function and answers 202 with a status resource (EXPOSE.3). In-request phases are "acceptable when the user must see the foreign outcome in the same response and the call fits ACT.3's 1 s budget". Record the ACT.2/ACT.3 tension in the pinned conflicts line and route it to J1's owner.

### M5 `SameSite=Lax` is decided on a force the branch says it does not serve

**Node**: J7 SECURE.2 (and the SameSite entry of J7 `questions.md`).

**Issue.** SECURE.2 lists as a force "the session's own purpose, carrying a login across every navigation", and picks Lax because Strict "defeats the session's purpose". That is a usability argument. J3's `questions.md` and J7's SECURE roll-up both say login usability is not a force this branch serves, and on that ground they made MFA required. Either the force counts in both places or in neither. The security half of the argument is also incomplete. J7 says Strict's extra protection "covers only safe requests, which change nothing". But under Lax, cross-site top-level navigations still carry the session. The cookie draft calls Lax "only a speedbump" against attacker-opened windows and navigations. Reflected script injection or cross-site leaks reached through a link then run with the user's session (inferred).

**Evidence**: L324 (Lax or Strict both admitted), L331 (Lax allows top-level GET navigations), grounded. draft-ietf-httpbis-rfc6265bis, fetched: "Attackers can still pop up new windows or trigger top-level navigations … which is only a speedbump along the road to exploitation". J3 `questions.md` on MFA: "login usability is not a force the secured-entry node serves".

**Fix**: apply the doctrine's own test. If holding the login across arrivals is a force SECURE.2 serves (I think it is: it is what a session is for), this is a genuine trade-off and goes to the maintainer as a question. My recommendation would be Lax, plus a Fetch Metadata check that refuses cross-site navigations to authenticated pages that are not entry points (inferred), with Strict acceptable for operator consoles. If the force is not served, the max is Strict, with Lax as "acceptable when users must arrive from other sites' links already logged in". Either way, remove the claim that Strict protects only safe requests that change nothing.

### M6 MFA is required, but a delegated login never checks that it happened

**Nodes**: J7 SECURE.4, SECURE.5 (realizing J3 LOGIC.SECURE's "MFA required by default").

**Issue.** Login is delegated to an OpenID Connect provider, and SECURE.5 becomes "the bar the chosen identity provider must meet". The backend validates issuer, audience, expiry and nonce, but nothing checks how the user authenticated. A provider policy change or misconfiguration silently drops MFA while every check still passes. That is "deciding on the caller's word", which J3 LOGIC.SECURE forbids. The stronger position is in the protocol itself.

**Evidence**: OpenID Connect Core 1.0, fetched: `acr` and `amr` claims; `acr_values` request parameter; "If the acr Claim was requested, the Client SHOULD check that the asserted Claim Value is appropriate". Not in the ledger. J7 SECURE.4 step 2 lists the ID-token checks without `acr` or `amr`.

**Fix**: in SECURE.4, the backend requests the required authentication context (`acr_values`, or the provider's MFA policy that yields a known `amr`). It refuses a login whose ID token lacks it. For sensitive operations it requires a fresh, sufficient context (step-up, `max_age`). In SECURE.5, the provider bar includes emitting these claims. Mark the step inferred from OIDC Core.

### M7 MAINT row L530 missed: function error codes and the override flag for blockable rules

**Nodes**: J7 EXPOSE.2, SECURE.1, ENFORCE.1; pinned doctrine line.

**Issue.** L530 is a maintainer row, owned by DATA but with direct interface consequences: function errors "name the function and carry stable custom codes, with an explicit override flag for blockable business rules". J7 misses both halves:
- EXPOSE.2 marks "the mapping of constraints and function errors to problem types" as inferred from L495, but L530 grounds it.
- No node says who may set the **override flag**. As written, a use case could pass it through from client input, and any caller could then bypass a blockable rule. Deciding who may override is product policy, which GUARD.3 gives the backend.

**Evidence** (grounded): L530, "maintainer decision (single source)", MAINT-S01, "agrees L052; extends".

**Fix**:
- EXPOSE.2: ground the mapping on L530 (function code → problem `type`); a blockable-rule error maps to a distinct type that names the override.
- SECURE.1: setting the override is an action the policy module authorizes per actor. It never comes from client input unchecked, and the override is audited with the actor (ACT.4).
- ENFORCE.1: the use case, not the adapter, decides whether to set it.
- Pinned doctrine line: list L530 (and L566, L587) among the rows applied.

## Minor findings

| id | node | issue | evidence | fix |
|---|---|---|---|---|
| m1 | J7 ENFORCE.2 step 6 | Retry made conditional on the DATA judge choosing Serializable; deadlocks (40P01) occur at every isolation level, and serialization failures (40001) under Repeatable Read too | Postgres error behaviour (inferred, not in the ledger) | The wrapper always retries 40001 and 40P01 for the whole one-call transaction, within PROCESS.3's caps |
| m2 | J7 PROCESS.4, PROCESS.5 | L023's checks (allowlisted type, **actual signature**) are not in the post-arrival path; a POST policy's "exact content type" binds the declared header, not the bytes | L023 via J3 LOGIC.SECURE P2; L423 | PROCESS.5: before availability, verify the file signature against an allowlist and set the stored type from it |
| m3 | J7 SECURE.6 step 5 | "challenge before block" puts a challenge (CAPTCHA-like) in front of agents, who are intended users | L652; J3 LOGIC.SECURE step 5 | Challenge only on human-only flows named by L034; agents get 429 with RateLimit fields |
| m4 | J7 EXPOSE.6 with EXPOSE.7 | Request models are closed to unknown fields, while the skew window lets a new island send a new field to an old server instance mid-deploy: 422 | L557, L278 | EXPOSE.7: a new request field is sent by clients only once every server instance accepts it (server first, then client) |
| m5 | J7 EXPOSE.7 | "No version while additive" and then "URL-path major for a break" leaves unversioned paths beside `/v2`; the URL-path source mandates `v1` from the start | L276 (Google: MUST `v1`) | Serve the JSON interface under `/v1` from the start; "no version" stays acceptable for HTML routes |
| m6 | J7 PROCESS.1 step 2 | The claim "marks the job running" without saying who writes it; job status is a state column | L596 (MAINT) | Claim, outcome and expiry go through the job table's writer functions (claim with `SKIP LOCKED` inside the function) |
| m7 | J7 ENFORCE.3, ENFORCE.5, EXPOSE.6 | "SQLAlchemy Core" named under a Django default; the Pydantic and OpenAPI production under Django is unread, yet MD-02's gate depends on it; Pydantic for forms beside Django forms is unstated | L242 gap; fetched: Django Ninja builds on Pydantic and generates an OpenAPI schema (version not stated on its front page) | Name one read layer (Django ORM or SQL through the wrappers); record Django Ninja as the candidate to verify (OpenAPI 3.1 output, Pydantic v2) in ENFORCE.5's gap |
| m8 | J7 SECURE.1 step 1 | "Calls the module for each object it reads" applied to lists filters after loading: short pages, leaked counts | DERIVE.2; ENFORCE.3 | The policy module emits a query predicate for collection reads; per-object checks for single objects |
| m9 | J3 LOGIC.EXPOSE.3 | Server-computed allowed actions for agents (the agent analogue of the browser's previewed actions, a permitted copy in ACT.1) not considered; gap acknowledged | ACT.1 copies; L661 | Add as a candidate under the gap, for INTERACTION.AGENT's judge; no change to the decision |
| m10 | J7 SECURE.2 vs EXPOSE.4 | SECURE.2's "every response that sets or carries the session is no-store" can read as every authenticated response, which contradicts EXPOSE.4's personalised `private, no-cache` | L327 | Word both: "responses that set or contain a session identifier" |
| m11 | J7 SECURE.4 | The own-store fallback condition ("no provider fits cost or data residency") ignores a self-run OIDC server, which removes both | L338 | State that delegation includes a self-run OIDC server; narrow the fallback to "no OIDC server can be used or run" |
| m12 | J7 EXPOSE.3 step 1 | Natural idempotence first is grounded by L587 (MAINT, absolute assignments, upserts) but cited only from L655 | L587; J1 GUARD.6 cites it | Cite L587 as the doctrine's max |

## Nodes found sound

J3 (web-app-philosophy):
- LOGIC: correct roll-up; the backend decides nothing the database owns (MD-03, ACT.1).
- LOGIC.SECURE: sound, apart from M1; MFA required by default is the max under the doctrine.
- LOGIC.ENFORCE: sound; L063 and L066 narrowed with reasons, as tensions, not hidden.
- LOGIC.PROCESS: sound; the missing links to ACT.2 and ACT.3 are rightly proposed.
- LOGIC.EXPOSE: sound; RECORD.2's backend half under MD-03 is correctly stated.
- LOGIC.EXPOSE.1: sound; the RFC 9110 wording is a cosmetic gap.
- LOGIC.EXPOSE.2: sound; L054's strict reading rightly yields to GUARD.4.
- LOGIC.EXPOSE.3: sound, apart from m9; MD-02 is a fair ground for level-2 JSON.

J7 (pig-web-defaults):
- PIG-WEB.LOGIC, SECURE, ENFORCE, PROCESS, EXPOSE: roll-ups faithful to their children and to J3.
- SECURE.3: sound; every CSRF layer, with bearer-only endpoints the one exemption.
- SECURE.7: sound; making the egress proxy required is a correct use of the max rule.
- ENFORCE.1: sound; Active Record narrowed by DB_API with the right condition.
- ENFORCE.4: sound.
- PROCESS.3: sound; one retrying layer, with caps.
- EXPOSE.1: sound; transitions as custom methods mapped to writer functions is a good inference.
- EXPOSE.4: sound, apart from m10's wording.
- EXPOSE.5: sound.
- PROCESS.6: sound, apart from M1's flip line.
- PROCESS.7: deferred, out of scope.
