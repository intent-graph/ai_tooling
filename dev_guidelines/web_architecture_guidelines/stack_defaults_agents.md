# Stack Defaults: Agent Surface

How AI agents use the application on this stack: one described HTTP core with an [MCP](glossary.md#mcp) adapter, OAuth discovery, delegated identity, approval of irreversible effects on the application's own page, and responses and quotas shaped for agents. The browser side of the same tier is in [Stack Defaults: Browser Surface](stack_defaults_interaction.md#browser-surface-overview).

## Table of Contents

1. [Agent Surface Overview](#agent-surface-overview) _(Lines 18-21)_
1. [Surface and Protocol](#surface-and-protocol) _(Lines 24-33)_
1. [Discovery and Registration](#discovery-and-registration) _(Lines 36-44)_
1. [Identity and Delegation](#identity-and-delegation) _(Lines 47-60)_
1. [Approval and Injection Defense](#approval-and-injection-defense) _(Lines 63-72)_
1. [Agent-Shaped Responses and Limits](#agent-shaped-responses-and-limits) _(Lines 75-84)_

---

## Agent Surface Overview
<!-- Lines 18-21 -->

One HTTP core described by OpenAPI, always in sync, with an MCP adapter for third-party agent hosts, over OAuth. An agent has its own identity and acts for a user, both recorded; irreversible or external effects are approved by the owning user on the application's own page and checked on the server; responses and quotas are shaped for agents. The specifications involved are still moving, so the discovery, registration and delegation rules below rest partly on drafts. Refines [Agent Access](philosophy.md#agent-access); part of the interaction tier of [Browser Surface Overview](stack_defaults_interaction.md#browser-surface-overview).
`PIG-WEB-INTERACTION.AGENT`

## Surface and Protocol
<!-- Lines 24-33 -->

The HTTP interface is described by OpenAPI kept in sync with the implementation; an MCP adapter over the same core serves third-party agent hosts (inferred from the [default context](glossary.md#default-context)), its tools having one origin checked by the same CI [drift gate](glossary.md#drift-gate).
- One core, one description: pages, JSON clients and agents reach the same core. The origin direction is the project's recorded choice ([Type Definition Chain](allocation.md#type-definition-chain)).
- MCP adapter for agent hosts the team does not build; it only translates and shapes, so it holds no rule. Tools are few and purpose-specific. Names, input schemas and result shapes are generated from the core description or checked against it (inferred), and the CI gate fails on drift. They change additively; a breaking change goes [expand, migrate, contract](glossary.md#expand-migrate-contract) under the compatibility window of [Non-Atomic Deployment](philosophy.md#non-atomic-deployment).
- Stateless: no hidden per-connection session; cross-call state is a server-minted, unguessable handle checked against the caller on every call.
- Transport by trust boundary: the hosted surface is remote HTTP with OAuth; a developer-local tool, if any, uses stdio with environment credentials in a sandbox; a local HTTP server requires an authorization token.
- Agents get data through the API and the adapter, never by scraping; do not rely on llms.txt.

`PIG-WEB-INTERACTION.AGENT.1`

## Discovery and Registration
<!-- Lines 36-44 -->

The application publishes OAuth protected-resource metadata and answers unauthenticated calls with `WWW-Authenticate` carrying `resource_metadata`. Agent clients prove identity through client ID metadata documents or signed requests, never a User-Agent string; identity keys the per-agent quota and the agent marking in data. These mechanisms rest on drafts and a moving specification (inferred).
- Client ID metadata documents first; dynamic registration only for compatibility; pre-registration for closed sets; consent per client and exact redirect URI matching always.
- Only single-use, short-lived, [PKCE](glossary.md#pkce)-bound codes travel in redirects (binding inferred); no session, bearer or long-lived token in a URL.
- Fetching a client's metadata document is a server-side fetch of a client-named URL through the fetch helper: any public host may be named, so private, loopback and link-local ranges are refused and every redirect hop validated ([Server-Side Fetch](stack_defaults_logic_security.md#server-side-fetch)).

Refines [Identity and Session State](allocation.md#identity-and-session-state).
`PIG-WEB-INTERACTION.AGENT.2`

## Identity and Delegation
<!-- Lines 47-60 -->

An agent has its own identity and acts for a user, with tokens carrying subject and [actor](glossary.md#actor) so both are recorded in logs and in the database. Every agent credential has an owner, is revocable and has a lifecycle.
- Tokens carry subject and actor (act claim or equivalent). The backend asserts both to the database in the transaction-local setting, checked against its role; agent-originated writes are marked as a class.
- Binding by client capability: tokens are short-lived and audience-bound for every scope. They are sender-constrained ([DPoP](glossary.md#dpop) or mutual TLS) for every client that can hold a key, and the authorization server issues bound tokens to every client that supports them.
- A client that can hold only bearer tokens keeps consequential scopes (payments, transfers, deletions, bulk exports) under three conditions: its tokens are short-lived and narrow, revocation is held on the server, and every consequential operation it requests runs only through the exact-action approval of [Approval and Injection Defense](#approval-and-injection-defense), which the writer function checks (inferred). An approved effect whose result returns to the caller (a bulk export) is delivered to the approving user in the application, not to the token holder (inferred).
- Consequential operations are bound to their details by Rich Authorization Requests where supported, else by the exact-action approval in [Approval and Injection Defense](#approval-and-injection-defense) (inferred).
- Lifecycle: one revocable credential per agent, a recorded sponsor, short lifetimes, no orphaned permission after removal.
- Open: the agent parameters of token exchange. Gap: sender-constraining support across agent hosts was not read.

Acceptable when every client that needs consequential scopes can hold a key (a closed or certified set of agents), or when an approved effect's result must return to the token holder: sender-constrained tokens required for consequential scopes.

Refines [Identity and Session State](allocation.md#identity-and-session-state), [Audit and History](allocation.md#audit-and-history) and [Authorization](allocation.md#authorization).
`PIG-WEB-INTERACTION.AGENT.3`

## Approval and Injection Defense
<!-- Lines 63-72 -->

Reads and reversible writes proceed under ordinary authorization. Irreversible or external effects require approval by the owning user, shown the exact action on the application's own page, and the effect's [writer function](glossary.md#writer-function) refuses an agent-originated operation without it.
- Flow: the agent's call creates a pending operation with exact parameters; the user approves it in the application under their own session; the writer function refuses an agent-originated operation without a matching approval by the delegating user (inferred). An approval dialog in the agent host is a client hint, never the gate; approval never replaces authorization. For a bearer-only client this approval is the gate for consequential operations ([Identity and Delegation](#identity-and-delegation)).
- Approvals stay rare by scoping, so fatigue does not erode them (inferred).
- Credentials, payment details and third-party authorization are collected on the application's own page, bound to the user who started the flow, never through the agent.
- Injection is contained structurally: few purpose-specific tools; no agent session the application runs holds untrusted input, private data and outward power together; filters only as an extra layer. Annotations, claimed identity and client names are untrusted.

Refines [Authorization](allocation.md#authorization) and [Business Rules and State Transitions](allocation.md#business-rules-and-state-transitions).
`PIG-WEB-INTERACTION.AGENT.4`

## Agent-Shaped Responses and Limits
<!-- Lines 75-84 -->

Rate limits are nested. Errors are machine-readable problem details; responses are paginated, size-capped and high-signal. Flows that hand out scarce goods need a human step or refuse agents.
- Each agent identity has its own quota inside its user's allowance, so a runaway agent exhausts only its own share; each client application has a ceiling across its users; the user's own interactive traffic is counted apart (nesting inferred). Flows whose automation harms the business carry per-flow limits.
- Scarce-goods flows (limited stock, referral credit per account): quotas and approval do not stop one party running many accounts with an agent each, so completion needs a human step on the application's own page, or agent credentials are refused there (inferred).
- Problem details for every error (stable type, status, detail, extensions); tool errors say what to change in the call ([Status Codes and Errors](stack_defaults_logic.md#status-codes-and-errors)).
- Paginated and filtered by default, size-capped; readable labels beside opaque handles, every handle ownership-checked on the server.
- Open: the list of scarce-goods flows is recorded per project.

Refines [Duplicate Suppression](allocation.md#duplicate-suppression): rate-limited retries carry [idempotency keys](glossary.md#idempotency-key).
`PIG-WEB-INTERACTION.AGENT.5`
