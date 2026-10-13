# Stack Defaults: Backend Security

How the Django backend secures entry for every caller, human or agent: one central access policy, server-held sessions after a delegated login, every [CSRF](glossary.md#csrf) layer, limits at two depths and fetches that cannot reach internal addresses. The rest of the Python tier is in [Stack Defaults: Python Application Tier](stack_defaults_logic.md#python-tier-overview).

## Table of Contents

1. [Backend Security Overview](#backend-security-overview) _(Lines 20-30)_
1. [Access Control Enforcement](#access-control-enforcement) _(Lines 33-55)_
1. [Sessions](#sessions) _(Lines 58-70)_
1. [CSRF Defense](#csrf-defense) _(Lines 73-83)_
1. [Federated Login and Tokens](#federated-login-and-tokens) _(Lines 86-99)_
1. [Passwords and Login Throttling](#passwords-and-login-throttling) _(Lines 102-111)_
1. [Abuse and Rate Limits](#abuse-and-rate-limits) _(Lines 114-126)_
1. [Server-Side Fetch](#server-side-fetch) _(Lines 129-137)_

---

## Backend Security Overview
<!-- Lines 20-30 -->

The Python backend is the one gate every caller passes and decides nothing on the caller's word. Refines [Secured Entry](philosophy.md#secured-entry) and the guarding [placements](glossary.md#placement) of [Authorization](allocation.md#authorization) and [Identity and Session State](allocation.md#identity-and-session-state).
- Access checks are central, deny by default and object level; the backend's checks are kept in full because [row-level security](glossary.md#row-level-security) is off by default.
- Humans hold an opaque, revocable, server-side session in Postgres after a delegated [OpenID Connect](glossary.md#oidc) login, with [MFA](glossary.md#mfa) offered on every account and required by privilege and risk level; its cookie is `SameSite=Lax` plus a cross-site navigation check, `Strict` for operator consoles. Agents hold short-lived, audience-bound, revocable tokens.
- No session token, bearer token or long-lived credential travels in a URL. The signed upload policy and the signed download URL are both cases of the single signed-file-URL exception of [URL as Public Interface](philosophy.md#url-as-public-interface).
- Limits apply at two depths: identity-blind at the proxy, identity-aware per identity and operation in the backend.
- Server-side fetches of client- or agent-named URLs cannot reach private, loopback or link-local addresses.
- Per-user read visibility: simple reads are written by the backend directly; sensitive, complex, high-impact or shared reads, per-user visibility rules included, go through database functions that receive the verified actor ([Access Control Enforcement](#access-control-enforcement)).

`PIG-WEB-LOGIC.SECURE`

## Access Control Enforcement
<!-- Lines 33-55 -->

One central policy module per backend, deny by default, object level, applied to every request whatever its origin. Refines [Authorization](allocation.md#authorization).
- Middleware refuses any route that declares no permission. Every use case calls the module with [actor](glossary.md#actor), action and object for each single object it reads or changes.
- Collection reads apply a query predicate emitted by the module inside the read statement (inferred), never a check on rows already loaded (short pages, leaked counts).
- Model: product roles for policy not stored in the data, plus attribute and relationship rules evaluated on the object.
- An override flag on a blockable business rule is authorized per actor by the module, audited with the actor, and never taken from client input unchecked.
- The backend sets the verified actor for every database call.
- [Per-user write rules](glossary.md#per-user-rule) decidable from the row are decided by the [writer function](glossary.md#writer-function); the backend's identical check is generated from or tested against it, and the function's named denial maps to the same response.
- Every rule has a denial test, at unit level and through the deployed stack against a live database under the backend's real role. Every denial goes to the security event log (separate from the business audit), with alerting on bursts.
- Forbidden: route- or role-only checks; per-view checks without one module; per-object checks on loaded collections; an override flag passed through from client input.

Per-user read visibility:
- Simple reads that carry no logic (a basic select, a few joins) are written by each backend directly.
- A read that is sensitive, complex, high-impact, built by a function, or an abstraction several backends share goes through a database function that receives the verified actor. Per-user visibility rules count as [sensitive reads](glossary.md#sensitive-read); for them the table is not read directly by the roles that must not see every row.

Roles, stated so no line claims more:
- The reporting role reads comment content and comments with a narrower audience than their target only through database functions.
- The operator role (administrators, all-powerful by the maintainer's model) sees every row, the change table, comments and notification rows included.
- Any other role that may SELECT the base tables sees every row unless its own role is restricted. Per-role grants bound which tables and columns a role sees, not which users' rows; the change table, comments and notification rows follow the same rule.

Changes when: plain role-based control suffices when no rule depends on object attributes or relations; row-level security only under the three conditions of [Row Security Placement](allocation.md#row-security-placement), with the backend checks kept.
`PIG-WEB-LOGIC.SECURE.1`

## Sessions
<!-- Lines 58-70 -->

An opaque random identifier, with the session data server-side in Postgres through Django's database session backend. Refines [Identity and Session State](allocation.md#identity-and-session-state).
- Framework session management, no custom mechanism; expired sessions purged by a scheduled job. The session table is written under the direct-write exception of [Database Function API](allocation.md#database-function-api) (inferred).
- Cookie: `__Host-` name, `Secure`, `HttpOnly`, explicit `SameSite`, no `Domain`, `Path=/`; never `SameSite=None`; the identifier carries no personal data and never appears in a URL.
- `SameSite`: `Lax` plus a [Fetch Metadata](glossary.md#fetch-metadata) check (inferred) that refuses or redirects cross-site navigations (`Sec-Fetch-Site: cross-site`, `Sec-Fetch-Mode: navigate`) to authenticated pages not declared as entry points; `Strict` for operator consoles and other applications never entered from other sites' links. `Lax` keeps users logged in when they arrive from another site's link; the navigation check closes what that lets an attacker's page open.
- Renew the identifier at login, logout, privilege change and step-up.
- Idle and absolute timeouts both enforced server-side, values recorded per project by risk class (NIST assurance levels as reference).
- Logout deletes the server record; deleting a user's rows revokes every session. Responses that set or contain an identifier are `no-store`.
- Forbidden: signed-cookie or stateless JWT sessions in the browser; sessions in process memory; a session identifier in a URL.

Acceptable when no backend can hold sessions: stateless sessions.
`PIG-WEB-LOGIC.SECURE.2`

## CSRF Defense
<!-- Lines 73-83 -->

Every layer on every request the session cookie authenticates. Realizes the CSRF rule of [Hostile Page Script](philosophy.md#hostile-page-script).
- Django's CSRF middleware, a synchronizer token in every form and in a header for [island](glossary.md#island) scripts; no view that accepts the session cookie is exempt.
- The cookie's `SameSite` value as second layer, never alone: `Lax`, or `Strict` for operator consoles ([Sessions](#sessions)).
- A Fetch Metadata and `Origin` check rejects cross-site unsafe requests (logging-only first, then enforced); requests without the headers fall back to the token.
- Safe methods change nothing, so GET carries no token. Bearer-token endpoints never accept the session cookie and are the only exemption (inferred).
- Forbidden: a custom header alone as defence.

Acceptable when the application holds no server session: signed double-submit.
`PIG-WEB-LOGIC.SECURE.3`

## Federated Login and Tokens
<!-- Lines 86-99 -->

Login delegated to an OpenID Connect server (an external provider or a self-run one); the backend is the confidential [backend-for-frontend](glossary.md#bff) client.
- Delegation is recorded as a decision; an own credential store only when no OpenID Connect server can be used or run (the ranking is inferred).
- Code flow with [PKCE](glossary.md#pkce), exact redirect-URI match, no open redirector, ID token validated (issuer, audience, expiry, nonce); provider tokens never reach the browser.
- Request the authentication context required for privileged accounts (`acr_values`, or a provider MFA policy yielding a known `amr`) and refuse a login of such an account that lacks it; sensitive operations need a fresh, sufficient context (`max_age`, `auth_time`) for every account.
- Local identity keyed by issuer plus subject, never e-mail; reauthenticate before any link change.
- Agent tokens: audience-bound to this server, short-lived, revocable; PKCE code flow when acting for a human, client credentials otherwise; refresh tokens rotated or sender-constrained; access tokens sender-constrained ([DPoP](glossary.md#dpop), mutual TLS) wherever supported.
- Every JWT verified with pinned algorithms, `none` rejected, issuer, subject, audience and explicit `typ` checked. Downstream calls use the backend's own token; an ID token is never an API credential.
- Forbidden: implicit and password grants, shared static keys for agents (short scripts only), tokens in browser JavaScript, credentials in a URL (the single-use authorization code is not one), accepting a login without checking the asserted authentication context.
- Gap: sender-constraining support across agent hosts was not read.

Acceptable when no such server exists: an own credential store, and then [Passwords and Login Throttling](#passwords-and-login-throttling) applies in full, MFA included. When the provider or agent host cannot sender-constrain: bearer-only access tokens with short lifetime and server-held revocation.
`PIG-WEB-LOGIC.SECURE.4`

## Passwords and Login Throttling
<!-- Lines 102-111 -->

Where the backend holds passwords; also the bar the OpenID Connect server must meet (inferred).
- Length: maximum at least 64, all printable Unicode, no composition rules, no periodic rotation, compromised and common lists checked. Minimum 8 where MFA is enforced, 15 for any account a password alone authenticates; numeric-only validator removed.
- Argon2id first in the hasher list (at least 19 MiB, 2 iterations, parallelism 1); upgrade old hashes at login.
- MFA offered on every human account, passkeys and WebAuthn preferred; required on privileged accounts (operator, owner, administrator) and at step-up before sensitive operations; required on every account when the project's chosen risk level says so. The OpenID Connect server emits `acr` or `amr` and `auth_time` so the backend verifies MFA for privileged accounts and step-up rather than assumes it.
- Generic errors; failures counted per account and source; growing delays, never hard lockout; a recovery path; one-time-code endpoints count failures only. The limit is enforced in the proxy and in login logic, never by framework throttling alone.

Acceptable when FIPS-140 applies: PBKDF2. When the project's chosen risk level requires it: MFA required on every account.
`PIG-WEB-LOGIC.SECURE.5`

## Abuse and Rate Limits
<!-- Lines 114-126 -->

Two depths (the split is inferred). Refines the consumption limits of [Secured Entry](philosophy.md#secured-entry); proxy configuration in [Reverse Proxy Edge](stack_defaults_transverse.md#reverse-proxy-edge).
- Proxy: identity-blind rate, connection, body-size and time limits, keyed on the address it appends itself (counted from the right of `X-Forwarded-For`).
- Backend: identity-aware limits per account, key or session plus address, per operation, tighter and cost-weighted where operations spend money or call third parties; concurrency limits on heavy endpoints; capacity reserved for critical routes (login, core write paths) when workers saturate.
- A spending cap and billing alert with every external provider (alert alone where no cap).
- Counters in a rebuildable `UNLOGGED` Postgres table (inferred); a shared cache service when measured counter writes load the primary. The proxy keeps its own state.
- New limits roll out observe-only, then enforced, with a switch. Challenges only on human-only flows; agents get 429, never a challenge.
- Over-limit: 429 with problem details, `Retry-After` never earlier than the window's end, `no-store`; the proxy answers 429, never 503.
- Send IETF `RateLimit` and `RateLimit-Policy` fields on the JSON interface and the agent surface, documented as unstable until the draft is published.
- Forbidden: proxy-only or application-only limits; the leftmost `X-Forwarded-For` value or the address alone as key.

`PIG-WEB-LOGIC.SECURE.6`

## Server-Side Fetch
<!-- Lines 129-137 -->

One helper for every fetch of a client- or agent-named URL is the required control, so a client cannot make the server reach internal services or metadata endpoints; a network guard backs it where the hosting allows.
- It refuses private, loopback and link-local ranges, checking the address actually connected to rather than the hostname (inferred); it validates every redirect hop the same way.
- Timeout and size cap; in a worker when the response does not need the result.
- Network guard, preferred: where the hosting can enforce outbound rules, fetches leave through an egress proxy with direct egress blocked, or outbound rules deny the application's processes the private, loopback, link-local and metadata ranges. It is required when the server's network holds internal services or a metadata endpoint that answers without a token (inferred). Where the hosting cannot enforce outbound rules, the helper is the guard.
- Forbidden: fetching without range checks.

Principle: [Paths and Destinations](../software_development_guidelines/construction.md#paths-and-destinations).
`PIG-WEB-LOGIC.SECURE.7`
