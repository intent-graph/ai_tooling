# WEB: principles specific to designing a web application as a whole (round 2)

## L1 headline

Best practice for the web-distinct part of a web app is well sourced as a set of environment constraints (uncontrolled client runtime, non-atomic client/server deployment, caches you do not own, public stable URLs, network latency as design material) but no source states "a web app needs its own philosophy"; the thesis holds only in a narrow, inferred form (the environment is distinct, most other principles are shared with any backend). Certainty: grounded per constraint, inferred for the thesis.

Pinned:
- Sources: 23 (T1 6, T2 14, T3 2, T4 1)
- Claims: 27
- Contested: whether a web app needs its own philosophy; hypermedia-driven clients (HATEOAS) strictness; cookies/sessions vs stateless REST; explicit API versioning vs deployment-layer skew protection; BFF for web-only apps
- Failed T1 fetch: web.dev "disable-unload-and-use-pagehide" (HTTP 404), replaced by the Chrome Page Lifecycle documentation (T3) and the web.dev bfcache article (T1)

## L2 claims

Pinned (repeated word for word):
- Sources: 23 (T1 6, T2 14, T3 2, T4 1)
- Claims: 27
- Contested: whether a web app needs its own philosophy; hypermedia-driven clients (HATEOAS) strictness; cookies/sessions vs stateless REST; explicit API versioning vs deployment-layer skew protection; BFF for web-only apps
- Failed T1 fetch: web.dev "disable-unload-and-use-pagehide" (HTTP 404), replaced by the Chrome Page Lifecycle documentation (T3) and the web.dev bfcache article (T1)

Clusters:
1. The browser is a runtime you do not control: assume unknown capability, deliver the core by HTML, enhance by feature detection, tolerate liberal input. Consensus, grounded. WEB-C01 to C04.
2. Client and server never deploy atomically: old clients and tabs run against new servers, so compatibility windows are a design input. Consensus on the problem, majority on the cure. Grounded. WEB-C05, C06, C21, C22.
3. Caches you do not own: you cannot recall a cached response, so cacheability is declared per URL up front and changing assets get new URLs. Consensus, grounded. WEB-C07 to C09.
4. The page is not a stable process: back/forward restores stale pages, the browser freezes or discards tabs, several tabs share one origin. Consensus, grounded. WEB-C10 to C12.
5. Latency and the network are design material: explicit design criterion, user-perceived thresholds, field measurement, no assumption of a reliable network. Consensus (fallacies list read only via a T4 secondary copy). WEB-C13 to C16.
6. The URL is the public interface: stable, implementation-free, usable as the contract between components. Consensus, grounded. WEB-C17, C18.
7. REST as the derivation of web constraints: hypermedia-driven clients, statelessness over cookies, extensibility. Contested at the strict end. Grounded. WEB-C19 to C21.
8. Users and the open web come first: multi-browser and multi-device, safe by default, minimal data. Consensus, grounded. WEB-C23, C24 (boundary: SEC, UI).
9. Frontend-shaped server pieces: BFF and micro frontends are options with a stated cost, not defaults. Majority, grounded. WEB-C25, C26.
10. Does a web app need its own philosophy? Narrow yes: the distinct core is the environment (clusters 1 to 6); the rest is shared with any service (Twelve-Factor targets "web apps" and SaaS generically). Inferred. WEB-C27.

Live debates:
- Own philosophy or not: no source asserts it; Twelve-Factor treats web apps as an instance of service software; Fielding, Keith and the TAG treat the Web environment as distinct. My synthesis sits between.
- Strict hypermedia (Fielding) vs fixed documented URL hierarchies (common API practice).
- Cookie session state (Fielding: "never reliable") vs practice; sibling area identity covers it.
- Skew: explicit URL versioning (Ubl) vs deployment-layer routing to the matching version (skew protection); the choice depends on who owns client and API.
- BFF: Newman says a web-only app needs it only with significant aggregation; applicability for a single-team JS+Python+Postgres site is open.
- Progressive enhancement as a rule vs SPA practice: Keith and MDN endorse it; no source read argues against it, but T4 counter-voices were not collected (sibling "counter-voices" slot).

Not covered: PWA, offline and service-worker strategy (deferred by brief); rate limiting, uploads, real-time, topology (siblings); security and identity detail (boundary only); accessibility and rendering location (round 1 UI); HTTP caching semantics at RFC level (RFC 9111 not read); Fowler's own writing on BFF (only Newman's page was read); original Deutsch fallacies text.

## L3 full

Pinned (repeated word for word):
- Sources: 23 (T1 6, T2 14, T3 2, T4 1)
- Claims: 27
- Contested: whether a web app needs its own philosophy; hypermedia-driven clients (HATEOAS) strictness; cookies/sessions vs stateless REST; explicit API versioning vs deployment-layer skew protection; BFF for web-only apps
- Failed T1 fetch: web.dev "disable-unload-and-use-pagehide" (HTTP 404), replaced by the Chrome Page Lifecycle documentation (T3) and the web.dev bfcache article (T1)

Prior work not repeated: round-1 ARCH-C22 to C25 (REST constraints bought and paid for, client-server, stateless, cache and layer costs) and ARCH-C45 (web app owns end-to-end concerns; inferred). This slot cites the same Fielding chapter 5 only for new claims.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| WEB-S01 | T2 | Architectural Styles and the Design of Network-based Software Architectures, ch. 5 (REST) | R. Fielding, 2000 | https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | REST constraints, resources and identifiers, hypermedia as engine of state |
| WEB-S02 | T2 | same, ch. 4 (Web architectural style) | R. Fielding | https://ics.uci.edu/~fielding/pubs/dissertation/web_arch_domain.htm | Web requirements: latency sensitivity, anarchic scalability, independent deployment, extensibility |
| WEB-S03 | T2 | same, ch. 6 (Experience and evaluation) | R. Fielding | https://ics.uci.edu/~fielding/pubs/dissertation/evaluation.htm | REST mismatches (cookies), extensibility rules, HTTP is not RPC |
| WEB-S04 | T2 | REST APIs must be hypertext-driven | R. Fielding, 2008 | https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven | strict reading of the hypermedia constraint |
| WEB-S05 | T2 | Resilient Web Design, ch. 4 Languages | J. Keith | https://resilientwebdesign.com/chapter4/ | browser as uncontrolled environment, Postel, JS fragility |
| WEB-S06 | T2 | Resilient Web Design, ch. 5 Layers | J. Keith | https://resilientwebdesign.com/chapter5/ | progressive enhancement, support vs optimization, feature detection |
| WEB-S07 | T2 | Web Platform Design Principles (W3C Group Note, status as shown on page: 14 September 2026) | W3C TAG | https://www.w3.org/TR/design-principles/ | platform-level principles; written for spec authors, applied here by analogy |
| WEB-S08 | T2 | Ethical Web Principles (W3C TAG statement, 12 Dec 2024, non-normative) | W3C TAG | https://www.w3.org/2001/tag/doc/ethical-web-principles/ | values of the open web |
| WEB-S09 | T2 | Cool URIs don't change | T. Berners-Lee, 1998 | https://www.w3.org/Provider/Style/URI | URL stability rules |
| WEB-S10 | T1 | Back/forward cache | web.dev | https://web.dev/articles/bfcache | back/forward restore behaviour |
| WEB-S11 | T1 | HTTP caching | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching | shared/private caches, versioned URLs, Vary |
| WEB-S12 | T1 | Progressive enhancement (glossary) | MDN | https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement | definition |
| WEB-S13 | T1 | Web Locks API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API | coordinating several tabs |
| WEB-S14 | T1 | Web Vitals | web.dev | https://web.dev/articles/vitals | field vs lab, thresholds at 75th percentile |
| WEB-S15 | T3 | Page Lifecycle API | Chrome developers (single vendor) | https://developer.chrome.com/docs/web-platform/page-lifecycle-api | frozen/discarded states, unreliable unload |
| WEB-S16 | T2 | Micro Frontends | C. Jackson, on martinfowler.com | https://martinfowler.com/articles/micro-frontends.html | independently deployed frontends, costs |
| WEB-S17 | T2 | Backends For Frontends | S. Newman | https://samnewman.io/patterns/architectural/bff/ | BFF definition, when and when not |
| WEB-S18 | T3 | Version Skew | M. Ubl, 2023 | https://industrialempathy.com/posts/version-skew | non-atomic deployment, mitigations |
| WEB-S19 | T2 | High Performance Browser Networking, latency primer | I. Grigorik | https://hpbn.co/primer-on-latency-and-bandwidth/ | latency as bottleneck |
| WEB-S20 | T2 | Response Times: The 3 Important Limits | J. Nielsen, 1993 | https://www.nngroup.com/articles/response-times-3-important-limits/ | perceived-latency thresholds |
| WEB-S21 | T4 | Fallacies of distributed computing (encyclopedia copy; originals by Deutsch and Gosling not read) | Wikipedia | https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing | list of eight fallacies, secondary only |
| WEB-S22 | T2 | The Twelve-Factor App, introduction | A. Wiggins et al. | https://12factor.net/ | scope: web apps / SaaS, any language |
| WEB-S23 | T1 | Service worker lifecycle | web.dev | https://web.dev/articles/service-worker-lifecycle | two versions of a site running at once (used for that point only; PWA otherwise deferred) |

Note: T2 for the Fielding dissertation is my ranking (academic, widely cited, not a standard). Drafts/notes by the TAG are T2 per brief.

### Claims

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| WEB-C01 | Treat the browser as an environment you do not control: capabilities, speed and JavaScript completion are unknown, so design for a range of support rather than one target. | principle | neutral | S05 (Languages), S06 (Layers), S07 (support full range of devices) | consensus | | grounded |
| WEB-C02 | Deliver the core content and function through HTML and enhance with CSS and JavaScript where supported (progressive enhancement); "everybody is a non-JavaScript user until the JavaScript has finished loading". | principle | js | S05, S06, S12 | consensus | Counter-voices (SPA-first) not collected in this slot | grounded |
| WEB-C03 | Detect features, not browsers; do not vary behaviour or cache keys on User-Agent. | practice | js | S06 (feature detection), S11 (Vary, User-Agent caveat), S07 (new features detectable) | consensus | | grounded |
| WEB-C04 | Be conservative in what you send and liberal in what you accept at the client-server boundary (Postel). | principle | neutral | S05 (Languages) | majority | Only one source read states it for the web; applying it to APIs is my extension; strictness vs tolerance is a trade-off | grounded for the browser case, inferred for APIs |
| WEB-C05 | Assume client and server run at different versions: deployment is not atomic, browser tabs keep old code for days, so every client-server contract needs a compatibility window. | principle | neutral | S18 (definition, why on the web), S02 (4.1.4.2 independent deployment: old and new co-exist), S23 | consensus | | grounded |
| WEB-C06 | Pick an explicit skew policy: backward-compatible changes within an N-day window, clients tolerant of unknown fields, and either versioned API paths or routing each client to the server version that served its code. | decision | http | S18 (mitigations list) | contested | Ubl: all of the above, each with cost. Hosting vendors: skew protection (route to matching deployment) is cheaper than API versioning when one team owns both sides (seen in search snippets only, not read). Applies by team ownership. | grounded (mitigations), open (which default for this stack) |
| WEB-C07 | Give changing static assets a new URL per content version (hash or version in the name) and serve them with a very long max-age and immutable. | practice | http | S11 (cache busting) | consensus | | grounded |
| WEB-C08 | Plan for caches you do not own: once a response with a long max-age is stored by an intermediary it cannot be deleted, so set short or no-cache for URLs whose content changes in place. | principle | http | S11 (controlling caches), S01 (cache constraint) | consensus | | grounded |
| WEB-C09 | Label every response cacheable or not on purpose (HTTP caches heuristically if you say nothing), use private for personalised responses, and Vary on any request header that changes the body. | practice | http | S11 (heuristic caching, shared vs private, Vary), S01 | consensus | | grounded |
| WEB-C10 | Treat back/forward as part of the interface: pages may be restored from memory without reload, so refresh time-sensitive or sensitive state on pageshow with persisted true. | principle | js | S10 | consensus | | grounded |
| WEB-C11 | Persist unsaved state on visibilitychange or pagehide, never on unload; the browser may freeze or discard a page without notice. | practice | js | S15 (states, unreliable unload), S10 (never use unload) | consensus | S15 is single-vendor T3, S10 is T1 on unload | grounded |
| WEB-C12 | Design for several tabs of the same origin at once (two versions, concurrent edits, duplicate background work) and coordinate shared work explicitly. | principle | js | S13 (leader election example), S23 (two versions of your site running at once) | majority | Tooling (Web Locks, BroadcastChannel) is one option; BroadcastChannel not verified in the page read | grounded for the problem, inferred as a general principle |
| WEB-C13 | Make network latency an explicit design criterion from the start: reduce round trips, move data closer, hide latency by caching and prefetching; latency, not bandwidth, is the usual bottleneck. | principle | neutral | S19, S02 (4.1.3) | consensus | | grounded |
| WEB-C14 | Budget interactions against user-perceived limits: about 0.1 s feels instantaneous, 1 s keeps the flow of thought, 10 s is the attention limit. | principle | neutral | S20, S02 (usability highly sensitive to user-perceived latency) | consensus | Thresholds are from 1993; Web Vitals targets (LCP 2.5 s, INP 200 ms, CLS 0.1) are the current web-specific form (S14) | grounded |
| WEB-C15 | Judge performance on field data at the 75th percentile, split by mobile and desktop; lab measurement does not substitute. | practice | neutral | S14 | consensus | boundary: UI (round 1 UI-C26/C27, OPS-C20) | grounded |
| WEB-C16 | Do not assume the network is reliable, latency zero, bandwidth infinite, or the network homogeneous; the client must fail gracefully and keep core function when requests or scripts fail. | principle | neutral | S21 (list, secondary), S06 (core function without JS), S12 | majority | The fallacies list is read only through a T4 copy; the resilience half is T1/T2 grounded | grounded (resilience), inferred (fallacies as web rule) |
| WEB-C17 | Treat URLs as the public, long-lived interface: keep them stable, free of author, status, file extension and implementation details, and own the mapping from URL to resource over time. | principle | http | S09, S01 (5.2.1 naming authority) | consensus | | grounded |
| WEB-C18 | Use the URL as the contract for state and for communication between independently built parts of the page: it is well defined, global, declarative and forces indirect coupling. | principle | js | S16 (cross-app communication) | majority | One source read; boundary: UI-C16 (URL as state) | grounded |
| WEB-C19 | Let server-provided representations drive client transitions and avoid fixed, out-of-band URL hierarchies; the most frequent violation is documentation-driven clients. | principle | http | S04, S01 (HATEOAS) | contested | Fielding: strict, buys independent evolution over decades at upfront cost. Common API practice: documented fixed URLs. Not decided here. | grounded |
| WEB-C20 | Do not keep application state in cookies as if it were part of the resource; Fielding holds cookie-based applications "will never be reliable". | decision | http | S03 (cookies) | contested | Fielding (REST purist) vs ubiquitous session cookies; boundary: identity and security | grounded as his claim, open as guidance |
| WEB-C21 | Design every message format to be extended: unknown headers or fields must not be required for understanding; old and new implementations co-exist. | practice | http | S03 (mandatory extensions), S02 (4.1.2 extensibility) | consensus | | grounded |
| WEB-C22 | Before changing or removing a behaviour, find how it is used today; breaking existing clients needs strong justification. | principle | neutral | S07 (prioritize compatibility) | majority | S07 addresses browser features; applying it to a site's own API is my analogy | grounded for platform, inferred for apps |
| WEB-C23 | Do not build features that only work in one browser, OS or device class. | principle | neutral | S08 (principle 11), S07 (full range of devices) | consensus | | grounded |
| WEB-C24 | Keep visiting a page safe and collect only the data needed for the user's goal. | principle | neutral | S07, S08 | consensus | boundary: SEC | grounded |
| WEB-C25 | Use a Backend for Frontend (one server component per user experience, owned by that frontend team) only when aggregation or divergent clients justify it; for a web-only app without much aggregation it is questionable. | decision | neutral | S17 | majority | Newman: yes for mobile plus web or heavy aggregation; no for plain web UI. Only his page was read. | grounded |
| WEB-C26 | Split the frontend into independently deployed micro frontends only with the organisational maturity to carry the extra pipelines, duplicated payload and integration testing. | decision | js | S16 | majority | One source read; boundary: ARCH, UI | grounded |
| WEB-C27 | A web app has a narrow philosophy of its own: the distinct part is the environment (clients and caches you do not own, non-atomic deployment, public URLs, network latency); all other principles (ownership, config, idempotent retries) are shared with any service. | principle | neutral | S22 (scope: web apps and SaaS, any language), S02, S05, S07, S09, S18 (distinct environment), ARCH-C45 (round 1) | contested | For distinctness: S02, S05, S07, S18. Against a separate philosophy: S22 treats web apps as service software generically; no source states the thesis. | inferred (my synthesis across the cited sources) |

### Gaps (open)

- No source found that explicitly argues "a web app as a whole needs its own philosophy" or argues the opposite; WEB-C27 is synthesis. Checked: Fielding ch. 4 to 6, Keith ch. 4 and 5, TAG notes, Twelve-Factor intro, Newman BFF, Fowler-site micro frontends.
- Fowler's own BFF or web-architecture writing, RFC 9111, original fallacies text, Keith chapters other than 4 and 5, BroadcastChannel docs: not read.
- Skew protection vendor claims are from search snippets only (not read); not used as grounds.
- Microsoft architecture-center BFF page seen only in search results; not read, not cited.
- Counter-voices on progressive enhancement and on strict REST belong to the sibling counter-voices slot.
