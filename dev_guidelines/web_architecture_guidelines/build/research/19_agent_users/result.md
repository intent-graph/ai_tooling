# Research result: AGENT, agents as users of a web application (round 4)

Area code AGENT. Siblings this round: ALLOCATION, COLLABORATION (boundary claims tagged).
Spec versions read: MCP specification 2026-07-28 (latest), OpenAPI 3.2.1, drafts as dated in the register.

## L1 headline

Best practice for agent users is firm where it reuses web security (one domain core behind several adapters, OAuth 2.x with audience-bound least-privilege tokens, server-side authorization the model cannot override, bounded consumption, idempotent retries, machine-readable errors), and unsettled where it is new (how an agent is identified, how consequential actions are approved, MCP versus plain OpenAPI, llms.txt); certainty is grounded for the T1 security layer and inferred for the agent-specific design choices.

Pinned:
- Sources by tier: T1 20, T2 12, T3 8, T4 2 (42 sources).
- Claims: 38.
- Contested topics: wrap-the-API vs purpose-built tools vs code-execution; MCP vs OpenAPI-only surface; llms.txt value; agent acts as user vs own identity vs both; per-action human approval vs structural constraint vs classifier approval; block automation vs identify and admit agents; bearer vs sender-constrained tokens; idempotency header vs body field vs natural idempotence; rate-limit key (user vs agent vs client app).
- Failed T1 fetches: OpenTelemetry GenAI agent-span conventions (page moved, the target repo page did not show the agent-span text, so telemetry claims are open); OWASP Top 10 for Agentic Applications (only the landing page was read, the item list comes from T4 search summaries); Web Bot Auth first URL returned 404 (an alternative copy was read); A2A well-known Agent Card path not confirmed in the text read.

## L2 claims

Pinned (same block as L1):
- Sources by tier: T1 20, T2 12, T3 8, T4 2 (42 sources).
- Claims: 38.
- Contested topics: wrap-the-API vs purpose-built tools vs code-execution; MCP vs OpenAPI-only surface; llms.txt value; agent acts as user vs own identity vs both; per-action human approval vs structural constraint vs classifier approval; block automation vs identify and admit agents; bearer vs sender-constrained tokens; idempotency header vs body field vs natural idempotence; rate-limit key (user vs agent vs client app).
- Failed T1 fetches: OpenTelemetry GenAI agent-span conventions (page moved, the target repo page did not show the agent-span text, so telemetry claims are open); OWASP Top 10 for Agentic Applications (only the landing page was read, the item list comes from T4 search summaries); Web Bot Auth first URL returned 404 (an alternative copy was read); A2A well-known Agent Card path not confirmed in the text read.

Clusters (claim, agreement, certainty, ids):
1. One domain core, several adapters: agents are one more driver of the same business logic; the agent surface adds no second copy of the rules. Consensus, grounded. AGENT-C01, C02, C36.
2. The agent-facing surface is a designed interface, not an auto-wrapped API: task-level tools, bounded outputs, actionable errors; MCP and OpenAPI are layers, not rivals. Majority, grounded for tool design, contested for the protocol choice. C03, C04, C05, C31, C32, C39.
3. Authentication and delegated authorization follow OAuth 2.x: code flow with PKCE, protected resource metadata, audience-bound tokens, no token passthrough. Consensus, grounded. C06, C07, C10, C27.
4. Agent identity: record both who the agent is and on whose authority it acts; a delegated token with subject and actor is the strongest form. Majority, grounded for the mechanisms, inferred for "both is the max". C08, C09, C11, C26, C35.
5. Least privilege and complete mediation: narrow scopes, fewer tools, authorization enforced by the application, never by the model's judgment. Consensus, grounded. C12, C13, C14, C15, C20.
6. Consequential actions need an approval design: the human who owns the authority approves the exact action out of band, and structure (Rule of Two, capability separation) reduces how often. Contested, inferred as a synthesis. C16, C17, C18, C19.
7. Bounded consumption and cost, per principal, communicated in machine-readable form. Consensus on bounding, majority on header detail. C21, C22, C23, C24.
8. Automation policy: sensitive business flows are protected specifically; blanket bot blocking conflicts with agents as first-class users, so admission is by identification. Contested. C25, C26.
9. Idempotency and safe retries are mandatory for any mutation an automated caller may repeat; the key mechanism is a decision. Consensus on the need, contested on the mechanism. C28, C29, C30.
10. Auditability: every agent action is attributable to an actor and a delegating subject, correlated, and free of secrets. Majority, grounded for attribution mechanisms, open for telemetry conventions. C33, C34.
11. Protocol-specific hygiene: SSRF on fetched URLs, local versus remote transport. Consensus within MCP. C37, C38.

Live debates (one line each):
- Thin wrapper over the existing API (cheap, drifts from how agents reason) vs consolidated task-level tools vs agents writing code against the API in a sandbox (token-cheap, needs a sandbox).
- MCP as the agent surface vs OpenAPI plus plain HTTP vs both layered.
- llms.txt: proposed and widely generated vs reported unused by AI services (T4 evidence).
- Agent acts as the user (OAuth delegation) vs agent has its own identity (installation or agent identity) vs both recorded.
- Per-action human approval vs classifier auto-approval (93% approval rate, 17% false negatives on dangerous actions) vs structural constraint so autonomy is safe.
- Block non-human traffic on sensitive flows (OWASP API6) vs admit identified agents (signed requests).
- Plain bearer tokens (what MCP specifies) vs sender-constrained tokens (RFC 9700 SHOULD).
- Idempotency-Key header (Stripe, expired IETF draft) vs request_id field (Google AIP-155) vs design POST/PATCH to be naturally idempotent (Zalando SHOULD).

Not covered: OpenTelemetry GenAI conventions (fetch failed); full OWASP agentic mitigation text; agent payments protocols; agent-to-agent trust beyond a one-page A2A read; model-side defenses (training, guardrail products) beyond what OWASP lists; billing and metering design for paid agent use; browser-driving agents (computer use) as a user of the human UI; legal and terms-of-service questions.

## L3 full

Pinned (same block as L1):
- Sources by tier: T1 20, T2 12, T3 8, T4 2 (42 sources).
- Claims: 38.
- Contested topics: wrap-the-API vs purpose-built tools vs code-execution; MCP vs OpenAPI-only surface; llms.txt value; agent acts as user vs own identity vs both; per-action human approval vs structural constraint vs classifier approval; block automation vs identify and admit agents; bearer vs sender-constrained tokens; idempotency header vs body field vs natural idempotence; rate-limit key (user vs agent vs client app).
- Failed T1 fetches: OpenTelemetry GenAI agent-span conventions (page moved, the target repo page did not show the agent-span text, so telemetry claims are open); OWASP Top 10 for Agentic Applications (only the landing page was read, the item list comes from T4 search summaries); Web Bot Auth first URL returned 404 (an alternative copy was read); A2A well-known Agent Card path not confirmed in the text read.

### Source register

Tier notes: the MCP specification is the normative text of that protocol and is ranked T1 for MCP questions. IETF Internet-Drafts count as T2 until published; the three drafts below (S22 to S25) are expired or individual drafts, said again where cited. Fetch details: the OWASP API Security pages redirected to a new host and were read there.

| id | tier | title, body | URL read | authoritative on |
|---|---|---|---|---|
| AGENT-S01 | T1 | MCP specification 2026-07-28, Authorization (Model Context Protocol) | modelcontextprotocol.io/specification/latest/basic/authorization | OAuth profile for agent-to-server access, scope strategy, step-up |
| AGENT-S02 | T1 | MCP Security Best Practices | modelcontextprotocol.io/specification/latest/basic/security_best_practices | confused deputy, token passthrough, SSRF, scope minimization, handle hijacking |
| AGENT-S03 | T1 | MCP specification, Tools | modelcontextprotocol.io/specification/latest/server/tools | human in the loop, annotations untrusted, error model, server security duties |
| AGENT-S04 | T1 | MCP specification, Elicitation | modelcontextprotocol.io/specification/latest/client/elicitation | secrets and third-party authorization out of band |
| AGENT-S05 | T1 | MCP specification, Key Changes (2026-07-28) | modelcontextprotocol.io/specification/2026-07-28/changelog | statelessness, DCR deprecation, trace context |
| AGENT-S06 | T1 | OWASP GenAI, LLM06:2025 Excessive Agency | genai.owasp.org/llmrisk/llm062025-excessive-agency/ | least functionality, permissions, autonomy |
| AGENT-S07 | T1 | OWASP GenAI, LLM10:2025 Unbounded Consumption | genai.owasp.org/llmrisk/llm102025-unbounded-consumption/ | rate limits, quotas, timeouts |
| AGENT-S08 | T1 | OWASP GenAI, LLM01:2025 Prompt Injection | genai.owasp.org/llmrisk/llm01-prompt-injection/ | privilege control, human approval, untrusted-content segregation |
| AGENT-S09 | T1 | OWASP API Security Top 10 2023, API6 Unrestricted Access to Sensitive Business Flows | api-security.owasp.org/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows | protecting flows from harmful automation |
| AGENT-S10 | T1 | OWASP API Security Top 10 2023, API4 Unrestricted Resource Consumption | api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption | limits, pagination, spending controls |
| AGENT-S11 | T1 (partial) | OWASP Top 10 for Agentic Applications for 2026 | genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026 | landing page only; item names taken from S42 |
| AGENT-S12 | T1 | RFC 8693 OAuth 2.0 Token Exchange, IETF | rfc-editor.org/rfc/rfc8693.html | delegation vs impersonation, act and may_act claims |
| AGENT-S13 | T1 | RFC 9396 OAuth 2.0 Rich Authorization Requests, IETF | rfc-editor.org/rfc/rfc9396.html | transaction-specific authorization_details |
| AGENT-S14 | T1 | RFC 9449 OAuth 2.0 DPoP, IETF | rfc-editor.org/rfc/rfc9449.html | sender-constrained tokens for public clients |
| AGENT-S15 | T1 | RFC 9700 Best Current Practice for OAuth 2.0 Security, IETF | rfc-editor.org/rfc/rfc9700.html | PKCE, audience restriction, privilege minimization, sender constraint |
| AGENT-S16 | T1 | RFC 9728 OAuth 2.0 Protected Resource Metadata, IETF | rfc-editor.org/rfc/rfc9728.html | resource self-description and discovery |
| AGENT-S17 | T1 | RFC 9457 Problem Details for HTTP APIs, IETF | rfc-editor.org/rfc/rfc9457.html | machine-readable errors |
| AGENT-S18 | T1 | RFC 9110 HTTP Semantics, section 9.2.2 Idempotent Methods, IETF | rfc-editor.org/rfc/rfc9110.html | idempotent methods and automatic retry |
| AGENT-S19 | T1 | OpenID Connect Client-Initiated Backchannel Authentication Core 1.0, OpenID Foundation | openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html | out-of-band user approval on a second device |
| AGENT-S20 | T1 | OpenAPI Specification 3.2.1, OpenAPI Initiative | spec.openapis.org/oas/latest.html | machine-readable HTTP API description |
| AGENT-S21 | T2 | Agent2Agent (A2A) Protocol specification 1.0.0 | a2a-protocol.org/latest/specification/ | agent-to-agent discovery (Agent Card) and declared auth schemes |
| AGENT-S22 | T2 (draft, expired) | The Idempotency-Key HTTP Header Field, draft-ietf-httpapi-idempotency-key-header-07 | ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html | key semantics, 409 and 422 behavior |
| AGENT-S23 | T2 (draft, active) | RateLimit header fields for HTTP, draft-ietf-httpapi-ratelimit-headers-11 | datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ | RateLimit and RateLimit-Policy fields |
| AGENT-S24 | T2 (individual draft, expired) | OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents, draft-oauth-ai-agents-on-behalf-of-user-02 | datatracker.ietf.org/doc/draft-oauth-ai-agents-on-behalf-of-user/ | requested_actor, actor_token, act chain for agents |
| AGENT-S25 | T2 (individual draft, expired) | HTTP Message Signatures for Automated Traffic Architecture, draft-meunier-web-bot-auth-architecture-05 | datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/ | signed identification of automated clients |
| AGENT-S26 | T2 | Hexagonal Architecture, Alistair Cockburn | alistair.cockburn.us/hexagonal-architecture/ | one application driven equally by users, programs, tests |
| AGENT-S27 | T2 | AIP-155 Request identification, Google API Improvement Proposals | google.aip.dev/155 | request_id idempotency |
| AGENT-S28 | T2 | Zalando RESTful API Guidelines (rules 153, 229, 230) | opensource.zalando.com/restful-api-guidelines/ | idempotent design, Idempotency-Key, 429 |
| AGENT-S29 | T2 | The lethal trifecta for AI agents, Simon Willison | simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | structural prompt-injection risk, skepticism of guardrails |
| AGENT-S30 | T2 | Agents Rule of Two, Meta AI | ai.meta.com/blog/practical-ai-agent-security/ | session-level capability limit |
| AGENT-S31 | T2 | Defeating Prompt Injections by Design (CaMeL), Debenedetti et al., arXiv 2503.18813 | arxiv.org/abs/2503.18813 | capability-based separation of control and data flow |
| AGENT-S32 | T2 | Design Patterns for Securing LLM Agents against Prompt Injections, Beurer-Kellner et al., arXiv 2506.08837 | arxiv.org/abs/2506.08837 | pattern catalogue (names not read) |
| AGENT-S33 | T3 | Writing effective tools for agents, Anthropic Engineering | anthropic.com/engineering/writing-tools-for-agents | consolidated tools, response shaping, errors |
| AGENT-S34 | T3 | Code execution with MCP, Anthropic Engineering | anthropic.com/engineering/code-execution-with-mcp | code-over-API alternative and its sandbox cost |
| AGENT-S35 | T3 | Claude Code auto mode, Anthropic Engineering | anthropic.com/engineering/claude-code-auto-mode | approval fatigue, classifier approval limits |
| AGENT-S36 | T3 | Idempotent requests, Stripe API docs | docs.stripe.com/api/idempotent_requests | production idempotency-key behavior |
| AGENT-S37 | T3 | Deciding when to build a GitHub App, GitHub Docs | docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app | app identity vs user-delegated tokens, rate limits, attribution |
| AGENT-S38 | T3 | What are agent identities, Microsoft Entra Agent ID, Microsoft Learn | learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id | agent identity as its own type, sponsor, delegated vs autonomous access |
| AGENT-S39 | T3 | Markdown for Agents, Cloudflare Docs | developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ | content negotiation for agent readers |
| AGENT-S40 | T3 | The /llms.txt file, Jeremy Howard | llmstxt.org/ | llms.txt proposal and claimed adoption |
| AGENT-S41 | T4 | Google's Mueller on llms.txt, Search Engine Journal | searchenginejournal.com/googles-mueller-llms-txt-is-comparable-to-the-keywords-meta-tag/544804/ | documents the dissent on llms.txt |
| AGENT-S42 | T4 | Web search result summaries (OWASP agentic list; MCP vs REST pieces; one log study reported secondhand) | search results, not fetched pages | documents live debates only |

### Claims

Format per claim: level, stack, sources (section read), agreement, positions, certainty, serves, wins when. Ledger ids (L...) are prior evidence cited, not repeated. Boundary tags mark claims that also sit with a sibling area.

**AGENT-C01** Agents should be served by the same domain core and data as humans, through an additional adapter, so that rules, validation and authorization exist once.
- level principle; stack neutral; sources S26 (Intent, Ports and Adapters), S03 (Security Considerations: servers implement access controls); ledger L062, L064; agreement consensus; certainty grounded.
- serves correctness and changeability; wins when more than one kind of client exists or is expected (always, once an agent surface is offered).

**AGENT-C02** Business rules, authorization and state transitions must not be duplicated in the agent adapter or in prompts; the adapter only translates and shapes.
- level principle; stack neutral; sources S26, S06 (Complete Mediation), S03; ledger L019; agreement consensus; certainty grounded for the principle, inferred for the application to agents (synthesis of S26 and S06).
- serves correctness, security; wins when the adapter is generated or maintained by a different team than the core. boundary: ALLOCATION (authorization placement).

**AGENT-C03** Describe the HTTP API in a machine-readable contract (OpenAPI) generated from or checked against the implementation, so humans, code generators and agents read one description.
- level decision; stack http; sources S20 (purpose statement, security schemes); ledger OpenAPI entries; agreement consensus; certainty grounded.
- serves discoverability, changeability (one contract); wins when the API has third-party or multiple internal consumers.

**AGENT-C04** Choose the agent protocol surface deliberately: expose an MCP server when third-party LLM hosts must connect without bespoke integration; use plain HTTP plus OpenAPI when clients are your own code; MCP can sit on top of the same HTTP core.
- level decision; stack http; sources S01, S03, S05 (stateless 2026-07-28), S20, S42 (debate, T4 only); agreement contested; certainty inferred.
- positions: (a) MCP as the agent surface: standard discovery, standard OAuth, tool descriptions the model is trained on (MCP spec; T4 pieces); wins when hosts you do not control are the clients. (b) OpenAPI and HTTP only: one surface, less to secure; wins when agents are your own programs and the API is already well-shaped. (c) Both layered, REST underneath, MCP as catalog (T4 only); wins when both client kinds exist.
- serves reach versus attack surface and maintenance cost.

**AGENT-C05** Expose agent-readable documentation and content by the cheapest standard mechanism; do not rely on llms.txt for discovery by AI services.
- level decision; stack http; sources S40, S41, S39, S42; agreement contested; certainty inferred (the adoption evidence is T4 and secondhand).
- positions: (a) publish llms.txt: low cost, reported adoption by documentation platforms, useful to coding agents that fetch it on purpose (Howard); wins for developer-documentation sites. (b) llms.txt is unused: Mueller reports AI services do not request it and compares it to the keywords meta tag; a reported log study (S42, not fetched) found nearly all files unrequested; wins as the reason not to spend effort. (c) content negotiation, `Accept: text/markdown` with `Vary: Accept`, so one URL serves both readers (Cloudflare); wins when pages already exist and traffic passes a CDN.
- serves token cost for agent readers and discoverability.

**AGENT-C06** A protected resource should publish OAuth Protected Resource Metadata and answer unauthenticated requests with `WWW-Authenticate` carrying `resource_metadata`, so a client can discover the authorization server without out-of-band setup.
- level practice; stack http; sources S16 (well-known URI, resource_metadata parameter), S01 (servers MUST implement RFC 9728); agreement consensus; certainty grounded.
- serves discoverability, interoperability; wins when clients are not pre-configured with your authorization server.

**AGENT-C07** Delegated user access by an agent should use the OAuth authorization code flow with PKCE, exact redirect-URI matching and HTTPS, not passwords, shared API keys or implicit flows.
- level practice; stack http; sources S15 (PKCE, exact match, implicit), S01 (OAuth 2.1 draft basis, PKCE flow); ledger L021, L022; agreement consensus; certainty grounded.
- serves security; wins when an agent acts for a human who can authenticate in a browser. Acceptable alternative: client-credentials for agents acting on their own behalf (S01 mentions it), static keys only for short scripts (S37).

**AGENT-C08** Record both identities of an agent action: the agent (actor) and the user or tenant on whose authority it acts; the strongest design issues a delegated token that carries both.
- level decision; stack neutral; sources S12 (delegation vs impersonation, act claim), S24 (draft), S37 (installation vs on-behalf-of-user), S38 (autonomous vs delegated access); agreement majority; certainty grounded for the mechanisms, inferred for "both is the max".
- positions: (a) agent is the user (OAuth user token, actions look user-initiated; GitHub OAuth apps): simplest, lowest friction, weakest attribution and widest blast radius; wins for personal tools. (b) agent has its own identity with its own permissions (GitHub App installation; Entra autonomous access): clean attribution, own rate limits and lifecycle; wins for unattended automation. (c) agent identity acting on behalf of a user with both recorded (GitHub App user-to-server, Entra delegated access, RFC 8693 `act`): best audit and least privilege; costs more design; wins when users delegate to third-party or multi-user agents.
- serves auditability and least privilege against simplicity.

**AGENT-C09** Express delegation with the RFC 8693 `act` claim (or its documented equivalent) so that downstream services and logs see subject and actor and any chain of actors.
- level practice; stack http; sources S12 (act, may_act, nested chain), S24 (extension draft, expired individual draft); agreement majority (the RFC is standard, the agent extension is not); certainty grounded for the claim semantics, open for agent-specific parameters.
- serves auditability; wins when more than one service or agent sits between the user and the data.

**AGENT-C10** A server accepts only tokens issued for it (audience check) and never forwards a client's token to another service; for downstream calls it obtains its own token (exchange or its own grant).
- level principle; stack http; sources S01 (Token Handling), S02 (Token Passthrough), S15 (audience restriction), S12; agreement consensus; certainty grounded.
- serves security, accountability; wins always where one service calls another on behalf of a caller.

**AGENT-C11** Prefer short-lived access tokens and sender-constrain them (DPoP or mutual TLS) where the client can hold a key; plain bearer tokens are acceptable when lifetime is short and scope narrow.
- level decision; stack http; sources S15 (SHOULD sender-constrain), S14, S01 (MCP specifies the `Authorization: Bearer` header; the text read does not mention DPoP), S37 (short-lived tokens); agreement contested; certainty grounded for each position.
- positions: sender-constrained (RFC 9700) serves theft resistance, costs client complexity; bearer (MCP core) serves interoperability today; wins respectively for high-value APIs and for open agent ecosystems.

**AGENT-C12** Grant agents the narrowest scopes: start with low-risk read scopes, elevate on demand with precise challenges (`insufficient_scope`), never publish wildcard or omnibus scopes, and still authorize each request in server code.
- level principle; stack http; sources S02 (Scope Minimization, Common Mistakes), S01 (scope selection, step-up), S15 (privilege minimization), S06; ledger L019; agreement consensus; certainty grounded.
- serves security, audit clarity; cost is consent friction and step-up round trips; wins always, with coarser scopes acceptable only for trusted first-party agents.

**AGENT-C13** For consequential operations bind the authorization to the transaction (amount, recipient, resource) with Rich Authorization Requests rather than a coarse scope.
- level practice; stack http; sources S13 (authorization_details, payment example); agreement majority (standard exists; no agent-specific source read); certainty inferred for agents.
- serves least privilege on irreversible actions; wins for payments, transfers, deletions, bulk exports; costs authorization-server support.

**AGENT-C14** Authorization is enforced by the application and the data layer under the acting user's rights; the model's output is treated as untrusted input, never as an authorization decision.
- level principle; stack neutral; sources S06 (Execute in User Context, Complete Mediation), S08 (treat model as untrusted user, privilege control), S03; ledger L019, L021; agreement consensus; certainty grounded.
- serves security; wins always. boundary: ALLOCATION (authorization placement; authority is the server tier, with a database-level backstop being that sibling's decision).

**AGENT-C15** Expose the minimum set of capabilities to an agent: few tools, purpose-specific rather than open-ended (no raw shell, raw SQL or arbitrary URL fetch), each with only the permissions it needs.
- level principle; stack neutral; sources S06 (Minimize Extensions, Functionality, Avoid Open-Ended); agreement consensus; certainty grounded.
- serves security (least agency), also tool-selection accuracy (S33); wins always; open-ended tools acceptable only inside a sandbox (S34).

**AGENT-C16** Gate consequential actions behind an approval design chosen by reversibility and blast radius: low-risk reads and reversible writes proceed; irreversible or external effects require approval by the user who owns the authority, shown the exact action.
- level decision; stack neutral; sources S03 (SHOULD human in loop, confirmation for sensitive operations), S06 (Require User Approval), S08, S19, S35, S30, S31; agreement contested; certainty inferred (synthesis across S03, S19, S35, S30).
- positions: (a) per-action human confirmation (MCP, OWASP): strongest for irreversible actions; suffers approval fatigue (Anthropic reports 93% of prompts approved). (b) classifier or policy auto-approval (S35): keeps flow, reported 17% false-negative rate on overeager actions, so not for high-stakes systems. (c) structural limits so approval is rarely needed (Rule of Two, CaMeL): strongest guarantee, costs capability (CaMeL completed 77% of tasks vs 84% undefended in the cited benchmark). (d) out-of-band approval on a separate device (CIBA): defeats a compromised client.
- serves security against throughput; wins respectively: (a) irreversible, rare actions; (b) developer tooling with recoverable effects; (c) agents that read untrusted content and hold private data; (d) payments and account changes.

**AGENT-C17** Collect secrets, payment details and third-party authorization out of band in the application's own page (URL mode), never through the agent's context; bind the flow to the same user who started it.
- level practice; stack http; sources S04 (MUST NOT form-mode secrets; phishing section; safe URL handling), S19 (binding_message on a second device); agreement consensus; certainty grounded.
- serves security (credentials never enter model context or logs); wins whenever an agent flow needs a credential or payment.

**AGENT-C18** Do not let one agent session combine untrusted input, access to private data and the power to change state or communicate externally; if all three are needed, require supervision or split the session.
- level principle; stack neutral; sources S29 (lethal trifecta), S30 (Rule of Two), S08 (segregate external content); agreement majority; certainty grounded for the rule, inferred that it generalizes to application agents.
- serves security against capability; wins when any content an agent reads can be written by third parties (email, tickets, web, user-generated content).

**AGENT-C19** Treat prompt-injection defense as structural first and filtering second; no filter is reliable enough to be the only control.
- level decision; stack neutral; sources S08 (no fool-proof method; filtering listed), S29 (skeptical of "95%" guardrails), S31, S32; agreement contested; certainty grounded.
- positions: structural (capability separation, constrained tool sets, human approval) vs filtering and guardrails; both appear in OWASP's list, Willison rejects filters as the sole control. Serves residual-risk reduction; filters win as an additional layer, structure wins where consequence is high.

**AGENT-C20** Servers must not rely on client-supplied hints (tool annotations, claimed user identity, client name) for enforcement; clients should treat annotations from untrusted servers as untrusted.
- level practice; stack neutral; sources S03 (annotations untrusted), S04 (Identifying the User: do not trust client-provided identity); agreement consensus; certainty grounded.
- serves security; wins always.

**AGENT-C21** Bound what any principal, including an agent, can consume: request rate, concurrency, payload size, time and downstream spend, with per-operation limits for expensive calls.
- level principle; stack neutral; sources S07 (rate limits, quotas, timeouts, throttling), S10, S03 (servers MUST rate limit tool invocations), S06 (damage limitation); ledger L031, L034; agreement consensus; certainty grounded.
- serves availability and cost; wins always; agents make loops and retries likelier than humans (inferred).

**AGENT-C22** Signal limits in machine-readable form: HTTP 429 with `Retry-After`, plus `RateLimit-Policy` and `RateLimit` fields so well-behaved clients pace themselves.
- level practice; stack http; sources S23 (draft 11, active), S28 (rule 153: MUST use 429 with headers); agreement majority (fields are a draft); certainty grounded.
- serves client cooperation and fewer wasted calls; wins when clients are programmatic. Draft status stated: T2.

**AGENT-C23** Choose the rate-limit partition deliberately: per user, per agent identity, per client application, or a combination, so one runaway agent cannot exhaust a user's or tenant's allowance.
- level decision; stack neutral; sources S37 (installation limits scale with repositories and users; OAuth-app limits do not), S23 (partition key), S10; agreement contested; certainty inferred.
- positions: per user (fair among humans, lets a delegated agent starve the human); per agent identity (isolates agents; needs agent identity, C08b or c); per client app (protects the service from one integration). Max serves isolation; wins respectively as stated.

**AGENT-C24** Bound cost, not only request counts: weight expensive operations, cap spend with downstream providers, and alert where capping is impossible.
- level practice; stack neutral; sources S10 (spending controls), S07 (resource allocation, quotas), S23 (quota units); agreement majority; certainty grounded for the lists, inferred for weighting.
- serves cost control; wins when one call can trigger a large paid or compute-heavy effect (exports, searches, model calls).

**AGENT-C25** Identify the business flows that automation harms (purchase, sign-up, booking) and protect those specifically; do not apply blanket bot blocking where agents are intended users.
- level principle; stack neutral; sources S09 (business-layer identification; device fingerprinting, human detection, secure machine-consumed APIs), S25; ledger L034; agreement contested; certainty grounded for each source, inferred for the synthesis.
- positions: (a) deny non-human patterns on sensitive flows (OWASP API6: fingerprinting, CAPTCHA, anomaly detection); wins for scarce-inventory or abuse-prone flows. (b) admit automated clients that identify themselves and are authenticated, limiting them by quota (OAuth clients, signed requests); wins where agent use is the product.
- serves business integrity against agent access; a flow-by-flow policy is the node's decision.

**AGENT-C26** Let an agent client prove who it is through a verifiable mechanism (OAuth client identity via client ID metadata documents, or signed HTTP requests), not through a self-declared User-Agent string.
- level decision; stack http; sources S25 (HTTP Message Signatures for automated traffic; expired individual draft), S01 (client ID metadata documents SHOULD), S09; agreement majority; certainty grounded for the mechanisms, open for adoption.
- serves attribution and abuse control; wins when per-agent policy or rate limits are wanted. Draft status stated: T2.

**AGENT-C27** For client registration prefer Client ID Metadata Documents; keep dynamic client registration only for compatibility; use pre-registration for closed ecosystems; apply per-client consent and exact redirect matching.
- level practice; stack http; sources S01 (Client Registration overview), S05 (DCR deprecated 2026-07-28), S02 (confused deputy, CIMD trust policies, localhost redirect risks); agreement consensus within the cited spec; certainty grounded (specification current at its date; moving).
- serves open-ecosystem interoperability against registry sprawl; pre-registration wins when the set of agents is small and known.

**AGENT-C28** Every mutating operation an automated caller may retry must be safe to repeat: idempotent by method design (PUT, DELETE) or made so with a key; the caller cannot know whether a timed-out request committed.
- level principle; stack http; sources S18 (idempotent methods and automatic retry), S36, S27, S22, S28; ledger L050, L051, L478, L479; agreement consensus; certainty grounded for the rule, inferred that agents raise the need (they retry on timeouts and re-issue calls after lost responses).
- serves correctness of effects; wins always for POST and PATCH that create or charge.

**AGENT-C29** Idempotency-key behavior should be specified: key unique per logical request; same key with a different payload is rejected (422 in the draft, an error in Stripe); a retry while the first is in flight returns 409; the stored response (including errors) is replayed; the retention window is published.
- level practice; stack http; sources S22 (server requirements), S36 (24-hour pruning, saved status and body incl. 500 in v1, parameter comparison; v2 retries failed work to completion), S27 (replay returns prior response, retention left to the API); agreement majority (details differ); certainty grounded.
- positions: replay the first result including 500 (Stripe v1) vs complete the work on retry (Stripe v2) vs return current state (AIP-155 permits). Serves safe retries against complexity; the choice depends on whether partial failures can be resumed.

**AGENT-C30** Prefer designing POST and PATCH to be idempotent by nature (client-supplied identifiers, upserts, conditional requests); add an Idempotency-Key where that is impossible.
- level decision; stack http; sources S28 (rule 229 SHOULD, rule 230 MAY), S36, S27, S22; agreement contested; certainty grounded.
- positions: natural idempotence (Zalando) wins when the domain has a stable client-side identifier; header (Stripe, draft) wins for payment-like creates; body field `request_id` (AIP-155) wins in RPC-style APIs where headers are awkward. Serves simplicity against generality.

**AGENT-C31** Return errors as stable, machine-readable problem details (type, status, detail, extensions), and for agent tools return execution errors that tell the model how to correct the call.
- level practice; stack http; sources S17, S03 (protocol errors vs `isError` execution errors for self-correction), S33; ledger L052; agreement consensus; certainty grounded.
- serves recoverability and fewer wasted calls; wins always.

**AGENT-C32** Shape responses for agent consumption: paginate and filter by default, return high-signal fields, cap sizes, prefer meaningful identifiers in what the model reads, and keep opaque, unguessable handles for state.
- level practice; stack neutral; sources S33 (pagination, filtering, truncation, natural-language identifiers), S10 (server-side pagination limits), S03 (Stateful Tools: handles opaque and bound to the caller), S02 (handle hijacking); agreement majority; certainty grounded.
- serves token cost and accuracy; small tension: readable names (Anthropic) vs opaque handles (MCP); resolve by showing readable labels beside opaque handles and checking ownership server-side. Wins when responses are large or identifiers are cryptic.

**AGENT-C33** Log every agent action with the acting identity, the delegating subject, the operation, a correlation id and the outcome, without secrets; keep these audit records on the server, not in the model transcript.
- level principle; stack neutral; sources S03 (clients SHOULD log tool usage), S02 (token passthrough breaks audit; log elevation events with correlation IDs), S38 (agent operations recorded as agent), S12, S05 (trace context in `_meta`); ledger L036; agreement majority; certainty grounded for the elements, open for the telemetry schema (the OpenTelemetry GenAI conventions could not be read).
- serves accountability and incident response; wins always where agents can change state. boundary: ALLOCATION (audit placement).

**AGENT-C34** Mark agent-originated writes in the data (actor type and actor id next to the user) so they can be filtered, reviewed, rolled back and revoked as a class.
- level practice; stack neutral; sources S37 (bot attribution in actions), S38 (agent actions distinguishable from workforce actions); agreement majority; certainty inferred (applies the attribution idea to application data).
- serves reviewability and undo; wins when agents write business data, and especially when humans co-edit it. boundary: COLLABORATION (human and agent editing the same records).

**AGENT-C35** Give agent credentials an owner and a lifecycle: short-lived tokens, one revocable credential per agent, a recorded sponsor, and removal without orphaned permissions.
- level practice; stack neutral; sources S38 (sponsor, bulk create and retire), S37 (short-lived tokens limit exposure), S01 (refresh tokens kept confidential; not assumed to be issued); ledger L022; agreement majority; certainty grounded.
- serves containment of compromise; wins when agents are created dynamically or in numbers.

**AGENT-C36** Keep the agent surface stateless: no hidden per-connection session; cross-call state is an explicit server-minted handle, validated against the caller on every call.
- level decision; stack http; sources S05 (sessions removed 2026-07-28), S03 (Stateful Tools), S02 (State Handle Hijacking); ledger L054; agreement consensus within MCP; certainty grounded (specification moving).
- serves scalability and security; wins when the surface runs behind load balancers. boundary: ALLOCATION (where state lives).

**AGENT-C37** Any server-side fetch of an agent- or client-supplied URL must block private, loopback and link-local ranges, validate each redirect hop and preferably go through an egress proxy.
- level practice; stack http; sources S02 (SSRF section), S06 (avoid open-ended URL fetching); agreement consensus; certainty grounded.
- serves security; wins whenever the server fetches client-named URLs (metadata documents, webhooks, link previews).

**AGENT-C38** Choose transport by trust boundary: local stdio tools take credentials from the environment and run sandboxed; remote HTTP surfaces use OAuth; local HTTP servers need an authorization token.
- level decision; stack http; sources S01 (stdio SHOULD NOT follow the spec), S02 (Local MCP Server Compromise); agreement consensus within MCP; certainty grounded.
- serves security; wins when the same application ships both a developer-local and a hosted agent surface.

### Gaps (open)

- Agent-to-agent calls: A2A declares security schemes in an Agent Card and requires clients to authenticate with one of them (S21), but trust between independent agent operators and the Agent Card discovery path were not confirmed. Open; boundary: COLLABORATION.
- OpenTelemetry GenAI conventions for agent and tool spans: fetch failed; recording of agent steps in the standard telemetry schema is open.
- OWASP agentic mitigations in full text, including any named least-agency principle: only the landing page was read.
- Evidence that MCP tool-call volume or cost differs from plain API use: only T4 opinion pieces found; no measurement read.
- Agent payments and spending-authority protocols: not researched.
- Browser-driving agents (computer use) acting through the human UI and how a site should treat them: not covered.
- The llms.txt non-use study was seen only in a search summary; the primary study was not read.
- Draft maturity: S22 to S25 are expired or individual drafts; their parameters may change or disappear.
