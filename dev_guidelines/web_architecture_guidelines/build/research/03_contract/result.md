# Research result: API, contract between browser and server

## L1 headline

Best practice for the browser-server contract is well settled on mechanics (HTTP semantics, RFC 9457 errors, opaque-cursor pagination, additive evolution, idempotency keys, explicit CORS) and genuinely contested on two foundations (HTML-over-the-wire vs JSON API; where a breaking-change version identifier goes); certainty is grounded for the mechanics and open for the first debate, because every source read on the hypermedia side is a T3 advocate and no T1/T2 source weighing the SPA side was read.

Pinned:
- Sources by tier: T1 12, T2 8, T3 8, T4 0 (28 sources in total).
- Claims: 37 (API-C01 to API-C37).
- Contested: hypermedia (HTML over the wire) vs JSON API as the browser contract; where the version identifier goes for breaking changes (URL path vs query parameter vs media type vs date header vs none).
- Failed T1 fetch: none. One T2 page (Microsoft REST API Guidelines, legacy) returned only a deprecation stub; the Azure REST API Guidelines were read instead. The Idempotency-Key header is still an Internet-Draft (-07), expired 2026-04-18 in the copy read.

## L2 claims

Pinned:
- Sources by tier: T1 12, T2 8, T3 8, T4 0 (28 sources in total).
- Claims: 37 (API-C01 to API-C37).
- Contested: hypermedia (HTML over the wire) vs JSON API as the browser contract; where the version identifier goes for breaking changes (URL path vs query parameter vs media type vs date header vs none).
- Failed T1 fetch: none. One T2 page (Microsoft REST API Guidelines, legacy) returned only a deprecation stub; the Azure REST API Guidelines were read instead. The Idempotency-Key header is still an Internet-Draft (-07), expired 2026-04-18 in the copy read.

Clusters (agreement, certainty, claim ids):

1. Contract style is a first-order decision: server-rendered hypermedia or a JSON data API, and it decides where logic lives. Contested; open (advocate sources only). API-C01, C02, C03, C04, C37.
2. HTTP semantics are the shared base: safe/idempotent methods, 303 after POST, precise status codes, optimistic concurrency with ETag/If-Match, explicit Cache-Control. Consensus; grounded. API-C05, C06, C07, C08, C09, C10.
3. Model the API as resources and standard methods, with Fielding dissenting on fixed hierarchies. Majority; grounded. API-C11.
4. Describe the contract in OpenAPI, design-first, and check conformance in CI; the HTML itself is the contract in a hypermedia design. Majority (design-first) ; grounded, C14 inferred. API-C12, C13, C14.
5. Errors: RFC 9457 problem details, status advisory, stable machine-readable code, no internals, clients ignore unknown members. Majority on the format (Azure and Google use own models), consensus on content rules; grounded. API-C15, C16, C17, C18.
6. Pagination: paginate every collection with a server cap; server-issued opaque continuation over offset. Consensus; grounded. API-C19, C20, C21, C22.
7. Retries and long operations: retried operations must be idempotent; client-supplied key for POST (mechanism varies, standard still a draft); 202 plus status monitor for slow work. Consensus on principle, majority on mechanism; grounded, C25 inferred. API-C23, C24, C25, C26.
8. Evolution: additive changes, an explicit definition of breaking, tolerant-reader clients, announced deprecation (Deprecation/Sunset), a skew rule for first-party clients. Consensus; grounded except C32 inferred. API-C27, C28, C29, C31, C32.
9. Version identifier placement: contested, five positions. Contested; grounded. API-C30.
10. Same origin by default, CORS only for real cross-origin consumers, explicit allowlist, CORS is not access control, BFF for token-bearing apps. Consensus on mechanics; the same-origin default is inferred. Boundary SEC. API-C33, C34, C35, C36.

Live debates:
- HTML over the wire (htmx, Turbo) vs JSON API plus client rendering: fit depends on interactivity, offline need and update granularity (API-C01).
- Version identifier: URL path (Google) vs required `api-version` query parameter (Azure, no path segment) vs media type (Zalando, URL forbidden) vs date header (Stripe, GitHub) vs none (GraphQL) (API-C30).
- Contract-first vs code-first OpenAPI: OpenAPI Initiative and Zalando say design-first; code-first defended only by lower learning cost (API-C12).
- Idempotency mechanism: `Idempotency-Key` header vs `request_id` field vs `Repeatability-*` headers (API-C24).
- Fixed resource hierarchy design vs Fielding's hypermedia-driven discovery (API-C11).

Not covered: see L3 "Gaps" (PATCH formats, rate limiting, streaming/SSE/WebSocket, file upload, RFC 9111 read directly, Microsoft Graph guidelines, an independent source on the SPA side, Kleppmann on encoding evolution).

## L3 full

Pinned:
- Sources by tier: T1 12, T2 8, T3 8, T4 0 (28 sources in total).
- Claims: 37 (API-C01 to API-C37).
- Contested: hypermedia (HTML over the wire) vs JSON API as the browser contract; where the version identifier goes for breaking changes (URL path vs query parameter vs media type vs date header vs none).
- Failed T1 fetch: none. One T2 page (Microsoft REST API Guidelines, legacy) returned only a deprecation stub; the Azure REST API Guidelines were read instead. The Idempotency-Key header is still an Internet-Draft (-07), expired 2026-04-18 in the copy read.

Method note: pages were fetched through a fetch tool that returns a model-written extract of the page, not raw text. Quotes and rule or section numbers below are as reported in those extracts; the rule numbers (Zalando) and section numbers (RFCs) should be re-verified against the page before the guideline cites them verbatim.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| API-S01 | T1 | RFC 9110 HTTP Semantics (sections 9.2, 9.3, 12, 13, 15.4.4, 15.5) | IETF | https://www.rfc-editor.org/rfc/rfc9110.html | method semantics, conditional requests, status codes |
| API-S02 | T1 | RFC 9457 Problem Details for HTTP APIs | IETF | https://www.rfc-editor.org/rfc/rfc9457.html | error body format |
| API-S03 | T1 | MDN: Cross-Origin Resource Sharing (CORS) | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS | CORS mechanics |
| API-S04 | T1 | MDN: Same-origin policy | MDN | https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy | origin definition, default cross-origin rules |
| API-S05 | T1 | MDN: Conditional requests | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests | ETag, If-Match, lost update |
| API-S06 | T1 | MDN: 303 See Other | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303 | Post/Redirect/Get |
| API-S07 | T1 | MDN: HTTP caching | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching | Cache-Control, Vary, private |
| API-S08 | T1 | OpenAPI Specification (latest, 3.2.1 in the copy read) | OpenAPI Initiative | https://spec.openapis.org/oas/latest.html | machine-readable HTTP API description |
| API-S09 | T1 | RFC 9745 The Deprecation HTTP Response Header Field | IETF | https://www.rfc-editor.org/rfc/rfc9745.html | deprecation signalling |
| API-S10 | T1 | RFC 8594 The Sunset HTTP Header Field (Informational) | IETF | https://www.rfc-editor.org/rfc/rfc8594.html | removal date signalling |
| API-S11 | T1 | draft-ietf-httpapi-idempotency-key-header-07 (Internet-Draft, expired 2026-04-18) | IETF HTTPAPI WG | https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html | Idempotency-Key header, draft only |
| API-S12 | T1 | OAuth 2.0 for Browser-Based Applications (draft version; header says later published as RFC 10017, not read) | IETF OAuth WG | https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps | BFF pattern (boundary SEC) |
| API-S13 | T2 | Fielding dissertation, ch. 5 REST | R. Fielding | https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | REST constraints, trade-offs |
| API-S14 | T2 | REST APIs must be hypertext-driven | R. Fielding | https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven | what REST requires |
| API-S15 | T2 | Richardson Maturity Model | M. Fowler | https://martinfowler.com/articles/richardsonMaturityModel.html | levels of REST adoption |
| API-S16 | T2 | Tolerant Reader | M. Fowler | https://martinfowler.com/bliki/TolerantReader.html | consumer-side evolution |
| API-S17 | T2 | Google API Improvement Proposals: AIP-121, 151, 154, 155, 158, 180, 185, 193 | Google | https://google.aip.dev/ (each /NNN page read) | resource design, LRO, etags, idempotency, pagination, compatibility, versioning, errors |
| API-S18 | T2 | Zalando RESTful API Guidelines | Zalando | https://opensource.zalando.com/restful-api-guidelines/ | API-first, compatibility, versioning, pagination, idempotency, problem JSON, deprecation |
| API-S19 | T2 | Azure REST API Guidelines | Microsoft | https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md | versioning, LRO, pagination, errors, repeatability, ETag |
| API-S20 | T2 | OpenAPI best practices (design-first) | OpenAPI Initiative | https://learn.openapis.org/best-practices.html | design-first vs code-first |
| API-S21 | T3 | Stripe docs: Idempotent requests | Stripe | https://docs.stripe.com/api/idempotent_requests | idempotency key in production |
| API-S22 | T3 | APIs as infrastructure: future-proofing Stripe with versioning | Stripe | https://stripe.com/blog/api-versioning | date-based versions, pinning |
| API-S23 | T3 | GitHub REST API versions | GitHub | https://docs.github.com/en/rest/about-the-rest-api/api-versions | header-selected date versions, support window |
| API-S24 | T3 | GraphQL: best practices index and schema design (avoiding versioning) | GraphQL Foundation | https://graphql.org/learn/best-practices/ and https://graphql.org/learn/schema-design/ | GraphQL's own claims |
| API-S25 | T3 | Hypermedia-Driven Applications | htmx maintainers | https://htmx.org/essays/hypermedia-driven-applications/ | HDA argument (advocate) |
| API-S26 | T3 | When Is Hypermedia a Good Fit | htmx maintainers | https://htmx.org/essays/when-to-use-hypermedia/ | fit criteria (advocate) |
| API-S27 | T3 | How did REST come to mean the opposite of REST | htmx maintainers | https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/ | HTML vs JSON as hypermedia (advocate) |
| API-S28 | T3 | Turbo Handbook: Introduction | Hotwire / 37signals | https://turbo.hotwired.dev/handbook/introduction | HTML over the wire in practice |

### Claims

Format: id | claim | level | stack | sources | agreement | positions | certainty. Boundary tags in the claim.

**Contract style**

- **API-C01** | The browser contract is an explicit decision between server-rendered hypermedia (HTML over the wire) and a JSON data API with client-side rendering; choose hypermedia for text-heavy, CRUD, localized-update UIs, and a JSON API for UIs with many cross-component dependencies, offline needs or very frequent state updates. | decision | neutral | S25, S26, S28 (hypermedia side); S13, S27 (REST framing) | contested | Hypermedia: htmx and Turbo maintainers say all logic stays on the server, no mirroring across a JSON divide, SPA-like UX via partial HTML; they list its poor fits themselves (many dynamic interdependencies, offline, extremely frequent updates). JSON/SPA: the position is only seen through these authors' description (client-side model, data APIs); no SPA-side source was read. Applies: hypermedia when the page is mostly documents and forms; JSON API when the client holds substantial state or a non-browser consumer exists. | grounded for the fit criteria as stated by advocates; open for the choice, no balanced source read
- **API-C02** | Authorization, validation and domain rules are enforced on the server whichever contract style is chosen; client-side checks are a convenience. (boundary: APP, SEC) | principle | neutral | S28 (logic lives server-side in the hypermedia design) | majority | Only the Turbo handbook states the corollary directly; no source read argues the opposite. | inferred (from S28 plus the shape of the browser trust boundary)
- **API-C03** | Describe a JSON API that carries no hypermedia controls as resource-oriented HTTP (Richardson level 2), not as REST; Fielding makes hypermedia a precondition of REST. | principle | http | S14, S15, S27, S13 | consensus | Fielding and Fowler agree on the definition; industry guidelines (S17, S18) design level-2 APIs and use "REST" loosely. | grounded
- **API-C04** | The uniform interface trades efficiency for visibility and independent evolution of client and server. | principle | http | S13 (uniform interface section) | consensus | | grounded
- **API-C37** | GraphQL is a third option when many clients need different field subsets of one graph; its own documentation claims versionless evolution through additive change and states the spec is silent on network, authorization and pagination. | decision | neutral | S24 | contested | Only the GraphQL project's own pages were read (advocate, T3); no independent comparison read. | grounded for what S24 says; open for when it is the right choice

**HTTP semantics**

- **API-C05** | Use HTTP methods by their defined semantics: GET (and HEAD) safe, PUT and DELETE idempotent, POST for non-idempotent processing; never change state through GET. | principle | http | S01 section 9.2, 9.3; S18 (HTTP methods rules); S15 level 2 | consensus | | grounded
- **API-C06** | After a successful form POST in a server-rendered flow, answer 303 See Other to a GET page, so a browser refresh cannot resubmit the form. | practice | http | S01 section 15.4.4; S06 | consensus | | grounded
- **API-C07** | Use status codes precisely: 409 for conflict with current resource state, 412 when a precondition fails, 428 when the server requires a precondition, 422 for well-formed but unprocessable content. | practice | http | S01 section 15.5, 13 | consensus | | grounded
- **API-C08** | Prevent lost updates with optimistic concurrency: return an ETag, require `If-Match` on updates, answer 412 (HTTP) or ABORTED (Google) on mismatch. (boundary: DATA, the stored version marker) | decision | http | S01 section 13; S05; S17 AIP-154; S18 (ETag rule); S19 (ETag, preconditions) | consensus | Mechanism agreed; strictness differs: Zalando MAY support, Azure MUST honor preconditions received and SHOULD return ETag, Google accepts a missing etag unless the service needs strong consistency. | grounded
- **API-C09** | Give every response an explicit `Cache-Control`; for HTML that must stay fresh use `no-cache`, for personalized responses add `private`, and set `Vary` for any request header the response depends on. (boundary: OPS) | practice | http | S07; S01 section 12 | consensus | | grounded
- **API-C10** | Requests are stateless: each carries all the information needed to understand it, so any server instance can handle it. (boundary: APP, ARCH) | principle | http | S13 (stateless); S17 AIP-121 | consensus | | grounded

**Resource modelling**

- **API-C11** | Model a data API as a hierarchy of named resources (nouns) manipulated by a small set of standard methods; add custom methods only where standard ones do not fit. | decision | http | S17 AIP-121; S18 (method rules); S15 levels 1-2 | majority | Google, Zalando, Fowler's levels: resource hierarchy designed up front. Fielding: never fix resource hierarchies in advance, let representations drive transitions. | grounded

**Contract artifact**

- **API-C12** | Define a JSON API's contract first, as an OpenAPI description, before implementing it; treat the description, not the code, as the source of truth. | decision | http | S08; S18 (API first, single self-contained OpenAPI file); S20 | majority | Design-first: Zalando (MUST), OpenAPI Initiative ("cannot be stressed strongly enough"). Code-first (spec generated from code): accepted as cheaper because developers learn no other language, but flagged as yielding incomplete descriptions. Code-first tooling in Python frameworks not read (APP). | grounded
- **API-C13** | Check in CI that the implementation conforms to its OpenAPI description, and design inside what OpenAPI can express. (boundary: OPS) | practice | http | S20 | consensus | | grounded
- **API-C14** | In a hypermedia design the HTML (links, forms) is the contract, and a separate OpenAPI file is needed only for the JSON endpoints that exist. | decision | neutral | S14, S27 (self-description of HTML) | majority | No source states the OpenAPI-optional corollary. | inferred (from S14, S27)

**Errors**

- **API-C15** | Return API errors as RFC 9457 problem details (`application/problem+json`). | decision | http | S02 section 3; S18 (problem JSON MUST); S17 AIP-193; S19 | majority | RFC 9457 and Zalando: problem+json. Google: `google.rpc.Status` with mandatory `ErrorInfo`. Azure: top-level `error` object with `code`, `message` and an `x-ms-error-code` header. | grounded
- **API-C16** | An error body supplements the HTTP status line (RFC 9457 `status` is advisory); its `detail` helps the client correct the problem, not debug the server, and never exposes stack traces or implementation details. (boundary: SEC) | practice | http | S02 section 3.1.2, 3.1.4, 5; S17 AIP-193 | consensus | | grounded
- **API-C17** | Clients ignore problem-detail extension members they do not recognize, so problem types can evolve. | practice | http | S02 section 3.2 | consensus | | grounded
- **API-C18** | Give each error a stable machine-readable identifier (`type` URI, `ErrorInfo.reason`, or error code) separate from the human-readable message. | principle | http | S02 section 3.1.1; S17 AIP-193; S19 | consensus | | grounded

**Pagination**

- **API-C19** | Every collection endpoint is paginated, and the server enforces a maximum page size, coercing larger requests down. | practice | http | S18 (pagination MUST); S17 AIP-158; S19 | consensus | | grounded
- **API-C20** | Page with a server-issued continuation (opaque token or ready-made next link) rather than offset/limit. (boundary: DATA, keyset queries) | decision | http | S18 (prefer cursor, avoid offset); S17 AIP-158; S19 (nextLink) | consensus | Zalando states the preference; Google and Azure use continuation only. Microsoft Graph, which reportedly offers `$skip`, was not read. | grounded
- **API-C21** | Page tokens are opaque and not parseable by clients, carry no authorization, and the end of the collection is signalled by an empty token or an absent next link. (boundary: SEC) | practice | http | S17 AIP-158; S19 | consensus | | grounded
- **API-C22** | A total count is optional, and an estimated total is documented as an estimate. (boundary: DATA, count cost) | practice | http | S17 AIP-158 | consensus | Single source family. | grounded

**Retries and long operations**

- **API-C23** | Operations a client may retry after a timeout must be idempotent by method semantics or made so with a key. | principle | http | S01 section 9.2.2; S17 AIP-155; S18 (idempotency rules); S19 ("all HTTP methods idempotent"); S21; S11 | consensus | | grounded
- **API-C24** | For POSTs that create or charge, accept a client-generated unique key, return the stored first response on repeat, reject the same key with a different payload, and document key retention. | decision | http | S11; S21; S17 AIP-155; S19; S18 | majority | Header `Idempotency-Key`: Stripe (255 chars, 24 h pruning, mismatch error, stores 500s too in v1), IETF draft (400 missing, 422 payload mismatch, 409 concurrent), Zalando (MAY). Request field `request_id` (UUID): Google. Headers `Repeatability-Request-ID` and `Repeatability-First-Sent`, 5 min tracking: Azure. The IETF standard is an expired draft. | grounded
- **API-C25** | Record the idempotency key and the operation's effect atomically, so a crash between them cannot repeat the effect. (boundary: DATA) | practice | postgres | none read states it | open | | inferred (from the key-store semantics in S21, S11)
- **API-C26** | Operations that may outlast a request return 202 with a status-monitor URL rather than blocking. | practice | http | S19 (202, `operation-location`, LRO when p99 over 1 s); S17 AIP-151 (about 10 s rule of thumb, Operation resource) | majority | Both agree on the pattern; thresholds differ (1 s vs 10 s). (boundary: APP, background jobs) | grounded

**Evolution and versioning**

- **API-C27** | Evolve APIs by compatible additions and avoid breaking changes; versioning is the exception. | principle | neutral | S17 AIP-180; S18 (do not break, prefer compatible, avoid versioning); S19; S22; S23; S24; S27 | consensus | | grounded
- **API-C28** | Write down what counts as breaking: removing or renaming components, adding a required request field, changing a type, default, format or semantics of an existing field. | practice | neutral | S17 AIP-180; S23; S22 | consensus | Adding enum values is compatible only where the enum appears in requests alone (Google). | grounded
- **API-C29** | Clients are tolerant readers: extract only what they need and ignore unknown fields and members. | principle | neutral | S16; S18 (accept compatible extensions); S02 section 3.2 | consensus | | grounded
- **API-C30** | When a breaking change is unavoidable, the version identifier sits in one agreed place. | decision | http | S17 AIP-185; S19; S18; S22; S23; S24 | contested | URL path major version, no minor: Google (MUST, `v1`). Required `api-version` query parameter in date form, no path segment: Azure. Media type versioning, URL versions prohibited: Zalando. Date-based version in a request header, account pinned: Stripe, GitHub (default version if header absent). No version, continuous additive evolution: GraphQL. | grounded
- **API-C31** | Announce removal with machine-readable signals and a support window: `Deprecation` header (it changes no behavior), `Sunset` header no earlier than the deprecation date (advisory), a documentation link, the flag in the OpenAPI file, and two versions coexisting during the transition. | practice | http | S09 section 2, 4, 5; S10; S18 (deprecation rules); S17 AIP-185; S23 (previous version supported 24 months, then 410) | consensus | Window lengths differ; RFC 8594 is Informational. | grounded
- **API-C32** | A first-party browser client that ships with the server still sees a version skew (cached or open pages running old JavaScript against a new server), so deployments keep API changes additive across that window. (boundary: OPS, delivery) | practice | http | none read states it | open | | inferred (from the compatibility claims C27, C28 plus how browsers cache assets)

**Same origin and CORS** (all boundary: SEC)

- **API-C33** | Serve pages and their API from one origin by default, and add CORS only for consumers that are truly cross-origin. | decision | http | S04; S03 (same-origin requests are outside CORS); S12 (same-domain BFF) | consensus | No source recommends cross-origin as a default for a first-party UI; the default itself is a synthesis. | inferred (from S03, S04, S12)
- **API-C34** | When CORS is needed: name explicit origins, never `*` with credentials, add `Vary: Origin` when the allowed origin is computed, and set `Access-Control-Max-Age` to cache preflights. | practice | http | S03 | consensus | | grounded
- **API-C35** | CORS relaxes the browser's cross-origin read block; it is not access control. Cross-origin writes (form posts, redirects) are allowed by default, so CSRF defense is needed independently. | principle | http | S04; S03 (CSRF note) | consensus | | grounded
- **API-C36** | For browser apps that hold tokens, a backend-for-frontend that keeps tokens server-side is strongly recommended for business, sensitive or personal-data applications. | decision | http | S12 | majority | One document; its final RFC form was not read. | grounded (draft)

### Gaps (open, not covered)

- No T1/T2 source weighing the SPA/JSON side against hypermedia was read; C01 rests on advocates plus Fielding. Next step: a balanced treatment (e.g. a web.dev or MDN architecture comparison, or a Fowler/Thoughtworks piece).
- Not read: RFC 9111 (caching) directly, PATCH formats (RFC 5789, 7396, 6902), rate limiting (429, Retry-After), streaming (SSE, WebSocket), file upload, content negotiation beyond RFC 9110 extract, HTTP/2 and HTTP/3 effects, WHATWG Fetch/CORS spec itself, Microsoft Graph guidelines, JSON:API, Kleppmann on encoding and evolvability (forward and backward compatibility).
- RFC 10017 (final BFF text) was not read; only its draft.
- Idempotency-Key: no later revision than -07 was found by search; whether it was superseded after April 2026 is unchecked.
- Zalando rule numbers and RFC section numbers come from extracts and need re-verification before verbatim citation.
- No source read covers the error experience for HTML (non-API) responses, nor how form-validation errors should be returned; open.
- Boundary claims (C02, C08, C09, C16, C20 to C22, C25, C26, C32 to C36) are recorded once here and should be reconciled with DATA, APP, SEC, OPS results.
