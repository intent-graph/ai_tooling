# Glossary

The terms this guideline uses before or without defining them: its own vocabulary first, then the acronyms and standards it relies on. Each file links the first use of a term here.

## Table of Contents

1. [Guideline Vocabulary](#guideline-vocabulary) _(Lines 14-42)_
1. [Acronyms and Standards](#acronyms-and-standards) _(Lines 45-71)_

---

## Guideline Vocabulary
<!-- Lines 14-42 -->

- <a id="actor"></a>**Actor**: the user, or the person an agent acts for, on whose behalf a database call runs. The backend asserts it for the transaction from its verified identity; the database treats it as a claim and checks that the session role may assert that kind of actor (asserted actor, claimed actor).
- <a id="authority"></a>**Authority**: the one tier whose decision on a responsibility counts. Every other tier holds at most a copy.
- <a id="backing-role"></a>**Backing role**: a supporting job a store does beside holding the data: job queue, schedules, derived caches, sessions, documents.
- <a id="change-cursor"></a>**Change cursor**: a position in the change table that no later commit can fall behind (a sequence id is not one); clients resume and catch up from it.
- <a id="consumer"></a>**Consumer**: anything that connects to the database: each backend, the reporting tool, admin consoles, scripts.
- <a id="consumer-role"></a>**Consumer role**: the database login role of one consumer: never the owner, never a superuser, bounded by its grants.
- <a id="copy"></a>**Copy**: data or a check held outside its authority, for feedback or latency. It carries a version or timestamp that detects staleness and never decides.
- <a id="data-job-checklist"></a>**Data-job checklist**: the procedure under which a human runs a large data change: batched, idempotent, run as the owner role with the operator and a ticket id as actor.
- <a id="default-context"></a>**Default context**: the project the decisions assume: a classic website, one team, single tenant, humans and agents as users, and a database shared by several backends and other consumers.
- <a id="deployed-together"></a>**Deployed together**: a breaking change that ships in the same deployment as every consumer of the changed object; the only case in which expand-migrate-contract may be skipped.
- <a id="drift-gate"></a>**Drift gate**: a CI check that fails when an interface description and its implementation differ, or when the live database differs from what the migrations produce.
- <a id="expand-migrate-contract"></a>**Expand-migrate-contract**: the route for an incompatible change: add the new structure or function beside the old (expand), move every consumer to it (migrate), remove the old once no deployed consumer uses it (contract).
- <a id="function-api"></a>**Function API**: the database functions, in a dedicated schema, through which consumers write data and run business operations; the default contract to the data.
- <a id="idempotency-key"></a>**Idempotency key**: a client-supplied key recorded with the effect in the same transaction, so a repeated request replays the first response instead of repeating the effect.
- <a id="island"></a>**Island**: a page region rendered and driven by browser JavaScript inside an otherwise server-rendered page, allowed only under the island criteria of [Rendering](allocation.md#rendering).
- <a id="lease"></a>**Lease**: a row with an owner and an expiry that grants exclusive editing for a while, checked by the writer function.
- <a id="maintainer-decision"></a>**Maintainer decision**: a decision taken by the guideline's maintainer that overrides any other source on its point; the seven are listed in the [README](README.md#maintainer-decisions).
- <a id="outbox"></a>**Outbox**: a table to which a database function writes the intent of a side effect in the same transaction as the data change; a worker delivers it after commit.
- <a id="owner-role"></a>**Owner role**: the database role that owns the tables and runs migrations and human-run jobs; it never serves requests.
- <a id="per-user-rule"></a>**Per-user rule**: a rule that depends on who the acting user is ("only the assignee may close a task", "a draft is visible only to its author").
- <a id="placement"></a>**Placement**: the decision of which tier is the authority for a responsibility, which copies other tiers may hold, which tiers are forbidden to hold it, and what would move it.
- <a id="sensitive-read"></a>**Sensitive read**: a read that is sensitive, complex, high-impact, built by a function, or shared by several backends; it goes through a database function. Per-user visibility rules are sensitive reads.
- <a id="staged-intent"></a>**Staged intent**: a row (outbox or job) recording that a side effect or deferred work must happen, written in the transaction of the change.
- <a id="state-column"></a>**State column**: a column holding the lifecycle state of a row, such as an order's status. Exactly one writer function may change it; consumer roles hold no direct update on it.
- <a id="status-resource"></a>**Status resource**: the URL a 202 response points to, reporting the progress and outcome of a long operation.
- <a id="tombstone"></a>**Tombstone**: a deleted comment kept as a row with its content cleared, so its thread stays readable.
- <a id="writer-function"></a>**Writer function**: the one database function allowed to perform an operation or write a state column. Every entry point routes through it, and it decides per-user write rules that the stored row and the actor can decide.

## Acronyms and Standards
<!-- Lines 45-71 -->

- <a id="adr"></a>**ADR**: architecture decision record: a short numbered document recording one decision with its forces, alternatives and the condition that would reverse it.
- <a id="aria"></a>**ARIA**: Accessible Rich Internet Applications: attributes that add accessibility semantics where native HTML cannot express a control.
- <a id="asgi"></a>**ASGI, WSGI**: the Python web server interfaces: WSGI for synchronous request handling, ASGI for asynchronous code and long-lived connections.
- <a id="asvs"></a>**ASVS**: the OWASP Application Security Verification Standard, a catalogue of verifiable security requirements in three levels.
- <a id="bff"></a>**BFF**: backend-for-frontend: a server component that holds tokens and sessions on behalf of a browser client.
- <a id="cdn"></a>**CDN**: content delivery network: caches serving files from locations near users.
- <a id="cls"></a>**CLS**: Cumulative Layout Shift, the Core Web Vital for visual stability.
- <a id="cors"></a>**CORS**: Cross-Origin Resource Sharing: the headers by which a server lets pages from other origins read its responses. It is not access control.
- <a id="crdt"></a>**CRDT**: conflict-free replicated data type: a structure that merges concurrent edits without a central server.
- <a id="csp"></a>**CSP**: Content Security Policy: a response header restricting which scripts and resources a page may load.
- <a id="csrf"></a>**CSRF**: cross-site request forgery: another site making the browser send an authenticated request.
- <a id="dpop"></a>**DPoP**: Demonstrating Proof of Possession: an OAuth mechanism binding a token to a key the client holds, so a stolen token is useless alone (a sender-constrained token).
- <a id="fetch-metadata"></a>**Fetch Metadata**: the request headers (`Sec-Fetch-Site`, `Sec-Fetch-Mode`) in which browsers state where a request comes from.
- <a id="hsts"></a>**HSTS**: HTTP Strict Transport Security: a header telling browsers to use HTTPS only for a host.
- <a id="inp"></a>**INP**: Interaction to Next Paint, the Core Web Vital for responsiveness.
- <a id="lcp"></a>**LCP**: Largest Contentful Paint, the Core Web Vital for loading speed.
- <a id="mcp"></a>**MCP**: Model Context Protocol: a protocol through which agent hosts call the tools a server exposes.
- <a id="mfa"></a>**MFA**: multi-factor authentication.
- <a id="oidc"></a>**OpenID Connect**: the identity layer on OAuth by which a login is delegated to an identity provider.
- <a id="pkce"></a>**PKCE**: Proof Key for Code Exchange: binds an OAuth authorization code to the client that requested it.
- <a id="row-level-security"></a>**Row-level security**: Postgres policies that filter rows per session role or setting; not used by default in this guideline.
- <a id="sbom"></a>**SBOM**: software bill of materials: the list of components in a release artifact.
- <a id="slsa"></a>**SLSA**: Supply-chain Levels for Software Artifacts: a framework grading build provenance in levels (Build L1 to L3).
- <a id="sse"></a>**SSE**: server-sent events: one-way streaming from server to browser over HTTP.
- <a id="wal"></a>**WAL**: the Postgres write-ahead log.
- <a id="wcag"></a>**WCAG**: Web Content Accessibility Guidelines, with conformance levels A, AA and AAA.
