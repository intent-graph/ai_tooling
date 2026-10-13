# Re-audit under MD-08: pig-web-defaults, INTERACTION and TRANSVERSE

Scope: the 56 nodes of `PIG-WEB-INTERACTION` (28) and `PIG-WEB-TRANSVERSE` (28) in
`intent_graphs/web_defaults.ig.yaml`, read one by one with `ig-tool query --node`, against the
judge records `03_judge/J8_pig_interaction/records.md` and `03_judge/J9_pig_transverse/records.md`
and the ledger `02_skeleton/claims_ledger.md`. Rule applied: MD-08 ("best for the node's purpose,
not the most demanding"); MD-01 to MD-07 treated as settled. Read-only: no graph or other file
changed.

## L1 headline

- Nodes read: 56 (INTERACTION 28, of which 2 deferred; TRANSVERSE 28, of which 1 deferred).
- Flagged: 1 — `PIG-WEB-INTERACTION.AGENT.3` (sender-constrained tokens required for consequential
  scopes: the stricter side of a contested row won, against the row's own condition and against
  the sibling `PIG-WEB-LOGIC.SECURE.4`).
- Kept: every other verdict. Three keep their verdict but state their grounds as "most demanding"
  or "maximum strictness" in live node text (`PIG-WEB-INTERACTION.EDIT`,
  `PIG-WEB-INTERACTION.VISUALIZE.4`, `PIG-WEB-TRANSVERSE.SECURITY.5`): wording to restate, verdict
  unchanged.
- Codified-practice check: the only override realized in scope is expand, migrate, contract for
  breaking function-API changes (against "deployed together"); "best" still supports it under
  MD-03.

## L2 claims

- `PIG-WEB-INTERACTION.AGENT.3` — current: consequential scopes (payments, transfers, deletions,
  bulk exports) require a DPoP or mutual-TLS token; bearer tokens there "win never". Why
  strictness decided it: the contested row L641 makes the choice by client capability ("where the
  client can hold a key"; bearer "wins for open agent ecosystems"). The judge swapped that
  condition for a stricter one (by consequence) and gave no ground for "never". The node's own
  sibling AGENT.4 already puts every consequential effect behind the owning user's exact-action
  approval, checked by the writer function. So the stricter rule adds only partial theft
  resistance. Its cost is that third-party agent hosts holding bearer tokens are shut out of the
  operations AGENT.1 opens an MCP adapter to serve. Proposed best choice: sender-constrain wherever
  the client can hold a key. A bearer-only client keeps consequential scopes, with a short
  lifetime, server-held revocation, and every consequential operation going through the AGENT.4
  approval. This is what PIG-WEB-LOGIC.SECURE.4 already states. Confidence: medium.

## L3 full

### PIG-WEB-INTERACTION.AGENT.3 Identity and Delegation

**Positions** (record, token-binding part): P4 short-lived, sender-constrained tokens (DPoP or
mutual TLS); P5 plain bearer tokens, short-lived and narrow (L641, contested). Related: P6 Rich
Authorization Requests for consequential operations (L643, inferred for agents).

**Evidence of the tie-break**
- Ledger L641: "Prefer short-lived access tokens and sender-constrain them (DPoP or mutual TLS)
  *where the client can hold a key*; plain bearer tokens are acceptable when lifetime is short and
  scope narrow." Positions column: "sender-constrained (RFC 9700) serves theft resistance, costs
  client complexity; bearer (MCP core) serves interoperability today; wins respectively for
  high-value APIs and for open agent ecosystems."
- Record, Forces: "P4 serves theft resistance at the cost of client complexity; P5 serves
  interoperability with today's agent clients." Both forces are named. The decision then composes
  them on an axis the row does not use: "Token binding by consequence (L641 composed, not split)
  ... scopes that allow consequential operations ... require a sender-constrained token."
- Record, Rejected: "P5 for consequential scopes: wins never." No reason is given. The row says
  bearer wins for open agent ecosystems, and the default context has agents the team does not
  build as users (AGENT.1: "agents as users, which means agents the team does not build").
- Same record, P6: when the authorization server lacks Rich Authorization Requests, "the
  exact-action approval of .4 binds the operation (inferred substitution)". The judge accepts the
  approval as a substitute for the stronger binding mechanism here, but not for token binding.
- AGENT.4 (decided): "the writer function that performs the effect refuses an agent-originated
  operation without a matching approval by the delegating user ... An approval dialog in the agent
  host is a client hint, never the gate." Every consequential effect is "the consequential list of
  .3", so all of them already sit behind a server-held approval.
- Sibling `PIG-WEB-LOGIC.SECURE.4` (J7): "access tokens sender-constrained (DPoP or mutual TLS)
  wherever supported", and "Bearer-only access tokens: acceptable when the provider or the agent
  host cannot sender-constrain, with a short lifetime and server-held revocation". Its state
  records "sender-constraining support across agent hosts not read". AGENT.3 is stricter than its
  own token-issuing node, and the support it requires was never checked.

**Why this is strictness, not purpose.** The node serves the user's ability, human or agent, to
work with the data, bounded by security. In the default context, a stolen bearer token can at most
create a pending operation. The owning user must still approve it, shown the exact action, in
their own authenticated session, and the writer function enforces that. Requiring sender-binding
on top shuts out every agent host that cannot hold a key from payments, deletions and exports,
even with the user's approval. MCP's core is bearer, per the row. The stricter rule therefore costs
the node's purpose and buys only residual protection. The record puts no number on that residual
protection and gives no source for it.

**Residual risk to state, not hide (inferred).** One case keeps value for binding: an effect whose
result goes back to the token holder, such as a bulk export downloaded by the agent. A thief
holding the bearer token could fetch a result the user approved for their own agent.

**Proposed intent** (node style):
> An agent has its own identity and acts for a user, with tokens carrying subject and actor so
> both are recorded in logs and in the database; agent-originated writes are marked as a class.
> Tokens are short-lived and audience-bound, sender-constrained wherever the client can hold a
> key, and every agent credential has an owner, is revocable and has a lifecycle; a bearer-only
> client reaches consequential operations only through the owning user's exact-action approval.

**Proposed constraint** (replaces "Token binding by consequence"):
- Token binding by client capability: tokens are short-lived and audience-bound for every scope.
  They are sender-constrained (DPoP or mutual TLS) for every client that can hold a key, and the
  authorization server issues bound tokens to every client that supports them. A client that can
  hold only bearer tokens keeps consequential scopes, under three conditions: its tokens are
  short-lived and narrow, revocation is held on the server, and every consequential operation it
  requests runs only through the exact-action approval of .4, which the writer function checks
  (composition of L641 with .4; inferred). For a bearer-only client, an approved effect whose
  result returns to the caller (a bulk export) is delivered to the approving user in the
  application, not to the token holder (inferred).

**Proposed rejected lines**:
- P4 required for consequential scopes: wins when every client that needs those scopes can hold a
  key (a closed or certified set of agents), or when an approved effect's result must return to
  the token holder and cannot be delivered in the application.
- P5 for consequential scopes without the server-held approval: wins never.

**Propagates to**
- `PIG-WEB-INTERACTION.AGENT` (roll-up constraint and decision: "sender-constrained tokens for
  consequential scopes" becomes "sender-constrained tokens wherever the client can hold a key;
  consequential operations of bearer-only clients only through server-held approval").
- `PIG-WEB-INTERACTION.AGENT.4`: no rule change. Its approval becomes the stated gate for
  bearer-only clients, so one line could say so.
- `PIG-WEB-LOGIC.SECURE.4`: none needed. The change removes the contradiction with its
  bearer-acceptable clause.
- Rendered doc `stack_defaults_agents.md` (the "Binding by consequence" line).
- The epistemic state of AGENT.3: drop "binding by consequence is a composition of L641"; add
  "bearer-only path through approval inferred; sender-constraining support across agent hosts not
  read" (shared gap with SECURE.4).

### Grounds to restate (verdict unchanged)

These verdicts are right for their purpose. Their live text, though, still says they won for being
the strictest, which MD-08 no longer uses as a ground.

- `PIG-WEB-INTERACTION.EDIT`. The constraint reads "The maximum strictness among the sources is
  adopted: the condition is required, not optional". Restate as: "the condition is required
  because every user-edited record is one where a lost update matters (L260's own condition for
  428); an optional precondition lets a client that omits it, an agent included, overwrite
  silently". The verdict (412 or 428 or 409, per-property updates exempt) stays.
- `PIG-WEB-INTERACTION.VISUALIZE.4`. The design notes read "P2 is the most demanding level that can
  be required of every full page ... under the max rule AA dominates A" and "P1: wins never ...
  (below the most demanding level every page can meet)". Restate on purpose: Level A leaves
  barriers that AA criteria remove for the people this node serves (contrast, resize, reflow,
  focus visibility, among others). AA is the level the one legal floor read sets, and W3C rules out
  only AAA site-wide. The AA verdict stays. Its state "AA grounded through the W3C conformance page
  plus the max rule" becomes "... plus the purpose".
- `PIG-WEB-TRANSVERSE.SECURITY.5`. The constraint reads "Under the max rule L3 is the target".
  Restate on the source's own recommendation: the SLSA levels page gives Build L3 as "Intended for:
  Most software releases" and Build L2 as the step for projects waiting on platform changes. L3
  stays the target, L2 under its condition. The cost "significant changes to existing build
  platforms" falls on platform operators, not on a team using a hosted build platform that already
  offers isolated, signed builds (inferred).

### Codified practice: does "best" still support the overrides in scope?

- Expand, migrate, contract for breaking function-API changes, against "deployed together" (L517).
  This is realized in `PIG-WEB-TRANSVERSE.CONTRACTS`, `.CONTRACTS.1`, `.CONTRACTS.2` and
  `.OPERABILITY.6`, and for the agent tool surface in `PIG-WEB-INTERACTION.AGENT.1`. It is counted
  at `PIG-WEB-DATA.INTERFACE.1`. "Best" still supports it. Under MD-03, BI, consoles, scripts and
  other backends deploy on their own cadence, so a lockstep breaking change breaks running
  consumers. That fails the integrity and availability the contract exists for. The lockstep path
  stays exactly where it works: every consumer of the changed object ships with the migration. The
  new-name route is also the maintainer's own route for stored contract schemas (L512).
  Confidence: high.
- The other five overrides (CHECK constraints, trigger-maintained `updated_at`, key width,
  declared parent keys, append-only tables without `updated_at`) belong to DATA nodes. In scope,
  `PIG-WEB-INTERACTION.COLLABORATE.2` uses a declared parent pointer and append-only revision rows,
  both in line with the codified practice. Nothing in scope overrides them.

### Verdicts examined closely and kept

- `PIG-WEB-INTERACTION.AGENT.1` (MCP adapter over the HTTP core by default): L635's own condition
  for layering, "both client kinds exist", holds, because the default has agents the team does not
  build. Purpose decided this, not completeness.
- `PIG-WEB-INTERACTION.AGENT.5` (nested rate-limit partitions): per-agent quota inside the user's
  allowance is the phil J4 decision 7, which is binding here. The per-client ceiling answers a
  failure case L651 names. Each single partition leaves a named failure open.
- `PIG-WEB-INTERACTION.AGENT.4` (server-held exact-action approval for irreversible or external
  effects): this is the L646 fit for irreversible, rare actions, and approvals are kept rare by
  scope.
- `PIG-WEB-INTERACTION.COLLABORATE.1` (target version always recorded): this moves L666 from "when"
  to "always" on a cost ground (the version and history already exist for every user-edited
  record), not on strictness. The column cost is near zero.
- `PIG-WEB-INTERACTION.COLLABORATE.2` (append-only revisions, tombstones): L673 itself says
  revisions win in business contexts, which is the default. Tombstones keep threads readable, a
  purpose ground.
- `PIG-WEB-INTERACTION.COLLABORATE.4` (report queue): this is conditional on outside readers, not
  a default.
- `PIG-WEB-INTERACTION.REALTIME.1` to `.5`: these take the simplest channel first (SSE, polling)
  and Postgres before Redis. Per-event authorization is settled by MD-05.
- `PIG-WEB-TRANSVERSE.SECURITY.1` (ASVS Level 2 default): this is grounded in the ASVS text ("most
  applications should be striving" for it), not in strictness. Level 3 is conditional.
- `PIG-WEB-TRANSVERSE.SECURITY.3` (strict nonce CSP): the server renders every page, so nonces cost
  little. The allowlist CSP is ranked below on bypass grounds.
- `PIG-WEB-TRANSVERSE.SECURITY.4` (managed store as authority): on self-managed hosting the file
  fallback is in force until a store is added on measured need, which already matches MD-06's
  fastest secure path.
- `PIG-WEB-TRANSVERSE.OPERABILITY.1` (keep every trace, tail sampling at volume): "keep all while
  volume allows" is head sampling at ratio 1, in line with L369's "start with head". Tail sampling
  arrives only when volume forces sampling, where the source calls it "almost always necessary".
- `PIG-WEB-TRANSVERSE.OPERABILITY.4` (central collector outside the database): tamper resistance
  against the database owner is the node's purpose. Stdout logs and the Postgres log already leave
  the database, so the collector adds little.
- `PIG-WEB-TRANSVERSE.OPERABILITY.5` (concurrency tests, tests as the consumer role): this is the
  only way to verify the procedural invariants and grants the default places in the database.
- `PIG-WEB-TRANSVERSE.CONTRACTS.2` (owner, meaning, quality, freshness, lifecycle per contract):
  this follows L563's own advice for one application database (the checklist, not the ODCS
  format). The cost is a catalogue comment per object.
- `PIG-WEB-TRANSVERSE.PERFORMANCE` (field targets, build budgets as the gate): L296 is a majority
  practice and INP is gated on field data, so the lab gate covers only lab-measurable vitals.
- `PIG-WEB-TRANSVERSE.EVOLUTION.2` (boundaries checked automatically): L123 is a majority row and
  no position opposes it. The open tool is recorded as a gap, not invented.
- `PIG-WEB-TRANSVERSE.TOPOLOGY.1` to `.4`, `.EVOLUTION.1`, `.EVOLUTION.3`, `.OPERABILITY.2`,
  `.OPERABILITY.3`, `.OPERABILITY.6`, `.SECURITY.2`, `.CONTRACTS.1`, `PIG-WEB-INTERACTION.VISUALIZE.1`
  to `.3`, `.AGENT.2`, `.COLLABORATE.3`, `.ENVIRONMENT.1`: each takes the simplest option that meets
  the purpose (one deployable, WSGI sync, proxy-served assets, HSTS preload not by default, no
  consumer-driven tests for the team's own browser), or follows consensus rows with no stricter
  rival.
- Not judged (deferred, recorded only): `PIG-WEB-INTERACTION.ENVIRONMENT.2`, `.ENVIRONMENT.3`,
  `PIG-WEB-TRANSVERSE.OPERABILITY.7`. Roll-up nodes inherit their children's verdicts.
