# Research result: Presentation tier (UI)

## L1 headline

Best practice for the browser tier is strongly settled on delivery and measurement (HTML-first with progressive enhancement, fingerprinted immutable assets, Core Web Vitals thresholds, native-HTML accessibility, server-side validation) and genuinely contested on the rendering default (server-rendered hypermedia versus SPA) and on whether to add a Node SSR tier; certainty is grounded for the settled parts (T1 sources) and inferred for the client-state taxonomy, which no single source states.

Pinned:
- Sources by tier: 35 total = 19 T1, 4 T2, 10 T3, 2 T4.
- Claims: 35 (UI-C01 to UI-C35).
- Contested topics: (1) SPA vs server-rendered HTML as the default; (2) extra Node SSR tier vs Python-only rendering.
- Failed T1 fetch: web.dev "javascript-startup-optimization" returned 404 and was not replaced; no cost-of-JavaScript claim rests on it.
- Weak grounds: the Post/Redirect/Get claim (UI-C17) rests on a T4 source only; the four-way client-state taxonomy (UI-C12) is inferred, not stated by any source.

## L2 claims

Pinned (repeated verbatim): 35 sources = 19 T1, 4 T2, 10 T3, 2 T4. 35 claims. Contested: SPA vs server-rendered HTML as the default; extra Node SSR tier vs Python-only rendering. Failed T1 fetch: web.dev javascript-startup-optimization (404), not replaced.

Clusters:
1. HTML is the baseline and JS enhances it (progressive enhancement, layered HTML/CSS/JS). Consensus, grounded. UI-C01, UI-C02.
2. Default rendering strategy: server-rendered HTML for text/CRUD-style sites; SPA only where interaction demands it. Contested, grounded in T3/T4 plus T1 platform guidance. UI-C03, UI-C04.
3. Prefer server or static rendering over full client rehydration; send JS only to interactive regions; islands fit content sites, not shared global state. Majority, grounded. UI-C05 to UI-C08.
4. An SSR meta-framework with request-time rendering adds a JS server runtime; static export or build-time rendering does not. Contested as a decision, grounded as fact (T3). UI-C09, UI-C10.
5. Ownership: presentation owns HTTP/HTML rendering and interaction, not domain rules; UI is separated from data storage. Consensus (T2), grounded. UI-C11.
6. Client state has distinct kinds (server, URL, form, UI) with different owners; server state is a stale-able cache; derive rather than duplicate. Majority/inferred. UI-C12 to UI-C15.
7. Navigation and form state live in URLs and native forms (History API, no fragments, Post/Redirect/Get); client validation is UX, server validation is mandatory. Consensus except PRG (T4 only). UI-C16 to UI-C18.
8. Static asset delivery: fingerprinted URLs, long-lived immutable caching, HTML revalidated not stored, personalized responses private, static files built at build time and served outside the app process. Consensus, grounded (T1). UI-C19 to UI-C25.
9. Performance as an architecture concern: Core Web Vitals thresholds at p75, field data first, LCP/INP/CLS structural causes, budgets enforced in the build. Consensus, grounded (T1). UI-C26 to UI-C31.
10. Crawlability: server or pre-rendering, History API URLs, soft-404 handling for CSR. Grounded in one vendor doc (T3). UI-C32.
11. Accessibility: page-level conformance target (WCAG 2.2), native HTML before ARIA, keyboard operability, consider from the start. Consensus, grounded (T1), except the choice of level AA as default (inferred). UI-C33 to UI-C35.

Live debates:
- SPA vs server-rendered HTML as the default: hypermedia camp (Hypermedia Systems, Turbo, htmx essay, MacWright) vs hybrid RSC camp (React, Next.js); applies by UI type (text/CRUD vs offline/high-frequency/spreadsheet-like).
- Extra Node SSR tier vs Python-only rendering: framework docs treat the server runtime as normal; hypermedia camp argues logic should stay in one server language.
- Islands/partial hydration vs full-app hydration: islands win for content sites, lose for shared cross-widget state.
- Performance budget numbers (170 KB, 5 s TTI) come from one 3G-era article and are examples, not norms.

Not covered: CSS architecture and design systems; internationalisation; client-side error reporting (OPS); service workers and offline/PWA; CDN topology and edge rendering; HTTP/2/3 and compression specifics; image/font delivery details beyond LCP/CLS notes; web components; micro-frontends; real-time channels (websockets/SSE); a T1 source for Post/Redirect/Get (RFC 9110 303 not read); the originators of islands (Sylor-Miller, Jason Miller) not read directly; cost-of-JavaScript evidence (fetch failed).

## L3 full

### Source register

URLs are the ones actually fetched. Framework docs (React, Next.js, TanStack, Turbo, htmx) are ranked T3 as maintainer documentation, not standards.

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| UI-S01 | T1 | Rendering on the Web | web.dev (Google) | https://web.dev/articles/rendering-on-the-web | SSR/CSR/static/hydration trade-offs |
| UI-S02 | T1 | Web Vitals | web.dev | https://web.dev/articles/vitals | Core Web Vitals thresholds, p75, field vs lab |
| UI-S03 | T1 | Progressive enhancement (glossary) | MDN | https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement | Definition of progressive enhancement |
| UI-S04 | T1 | HTTP caching | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching | Cache-Control practice for assets and HTML |
| UI-S05 | T1 | RFC 8246 HTTP Immutable Responses | IETF | https://www.rfc-editor.org/rfc/rfc8246.html | `immutable` directive |
| UI-S06 | T1 | RFC 9111 HTTP Caching | IETF | https://www.rfc-editor.org/rfc/rfc9111.html | Shared-cache rules, no-cache vs no-store, heuristics |
| UI-S07 | T1 | WCAG 2.2 | W3C | https://www.w3.org/TR/WCAG22/ | Accessibility principles, levels, conformance |
| UI-S08 | T1 | Accessibility principles | W3C WAI | https://www.w3.org/WAI/fundamentals/accessibility-principles/ | Early involvement of users (thin) |
| UI-S09 | T1 | Performance budgets 101 | web.dev | https://web.dev/articles/performance-budgets-101 | Budget definition and CI enforcement |
| UI-S10 | T1 | Optimize LCP | web.dev | https://web.dev/articles/optimize-lcp | LCP subparts and architectural levers |
| UI-S11 | T1 | Optimize INP | web.dev | https://web.dev/articles/optimize-inp | INP phases, long tasks, DOM size |
| UI-S12 | T1 | Interaction to Next Paint | web.dev | https://web.dev/articles/inp | INP definition, replaces FID |
| UI-S13 | T1 | Cumulative Layout Shift | web.dev | https://web.dev/articles/cls | Layout shift causes and fixes |
| UI-S14 | T1 | Back/forward cache | web.dev | https://web.dev/articles/bfcache | bfcache eligibility |
| UI-S15 | T1 | Using ARIA | W3C | https://www.w3.org/TR/using-aria/ | Four rules of ARIA use |
| UI-S16 | T1 | Client-side form validation | MDN | https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation | Client vs server validation |
| UI-S17 | T1 | History API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/History_API | pushState/replaceState/popstate |
| UI-S18 | T1 | Deploying static files | Django docs | https://docs.djangoproject.com/en/stable/howto/static-files/deployment/ | Static file serving in production |
| UI-S19 | T1 | The staticfiles app | Django docs | https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/ | ManifestStaticFilesStorage hashing |
| UI-S20 | T2 | Presentation Domain Data Layering | M. Fowler | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | Layer responsibilities |
| UI-S21 | T2 | Build, release, run (Twelve-Factor App) | A. Wiggins / Heroku | https://12factor.net/build-release-run | Stage separation, immutable releases |
| UI-S22 | T2 | REST architectural style (dissertation ch. 5) | R. Fielding | https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | Client-server separation, hypermedia, code-on-demand |
| UI-S23 | T2 | Resilient Web Design, ch. 2 | J. Keith | https://resilientwebdesign.com/chapter2/ | Loose coupling of HTML/CSS/JS |
| UI-S24 | T3 | Hypermedia Systems, ch. 1 | Gross, Stepinski, Akşimşek (htmx authors) | https://hypermedia.systems/hypermedia-a-reintroduction/ | Case for hypermedia-driven apps |
| UI-S25 | T3 | Turbo Handbook, introduction | Hotwire / 37signals | https://turbo.hotwired.dev/handbook/introduction | Server-rendered HTML with enhancement |
| UI-S26 | T3 | When to use hypermedia | htmx project essay | https://htmx.org/essays/when-to-use-hypermedia/ | Criteria for hypermedia vs SPA |
| UI-S27 | T3 | TanStack Query overview | TanStack maintainers | https://tanstack.com/query/latest/docs/framework/react/overview | Definition of server state |
| UI-S28 | T3 | Choosing the State Structure | React docs | https://react.dev/learn/choosing-the-state-structure | Single source of truth, derive state |
| UI-S29 | T3 | React Server Components | React docs | https://react.dev/reference/rsc/server-components | Server Components, build-time vs request-time |
| UI-S30 | T3 | Server and Client Components | Next.js docs | https://nextjs.org/docs/app/getting-started/server-and-client-components | Server/client boundary |
| UI-S31 | T3 | Static exports | Next.js docs | https://nextjs.org/docs/app/guides/static-exports | What needs a Node server |
| UI-S32 | T3 | JavaScript SEO basics | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | Crawlability of JS sites |
| UI-S33 | T3 | Islands Architecture | patterns.dev | https://www.patterns.dev/vanilla/islands-architecture/ | Islands definition and limits (secondary; originators not read) |
| UI-S34 | T4 | Second-guessing the modern web (SPA fatigue) | T. MacWright | https://macwright.com/2020/05/10/spa-fatigue | Live debate: SPA critique |
| UI-S35 | T4 | Post/Redirect/Get | Wikipedia | https://en.wikipedia.org/wiki/Post/Redirect/Get | PRG mechanics (needs T1 backing) |

Fetch failures: web.dev javascript-startup-optimization (T1) 404, not replaced. An MDN test page 404 (irrelevant, not used). The W3C APG page returned only its homepage; ARIA rules were taken from UI-S15 instead. UI-S08 yielded little beyond early involvement of users.

### Claims

Format: id | claim | level | stack | sources | agreement | positions | certainty. Boundary tags in the claim text.

**Rendering and progressive enhancement**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C01 | Provide a baseline of essential content and function that works without the latest browser capabilities, and enhance on top of it for capable browsers. | principle | neutral | S03 (definition), S23, S25 | consensus | - | grounded |
| UI-C02 | Keep structure (HTML), presentation (CSS) and behaviour (JS) loosely coupled so that a failing or absent layer does not take the others down. | principle | neutral | S23 (ch. 2), S03 | consensus | - | grounded |
| UI-C03 | Prefer server-rendered HTML (multi-page, optionally enhanced) as the default for text-, image- and form-centred (CRUD) sites. | decision | neutral | S24, S25, S26, S34, S01 | contested | Hypermedia camp (S24, S25, S26, S34): default to HTML from the server, logic stays server-side, tolerant of change; React/Next camp (S29, S30): hybrid server+client components, server-first by default but client JS layered in; applies by UI type, see UI-C04. | grounded (positions); the default itself is a judgment |
| UI-C04 | Choose a client-rendered SPA only when interaction demands it: spreadsheet-like interdependent state, offline use, or very frequent UI updates; otherwise its costs are not repaid. | decision | js | S26, S34 | majority | S26 and S34 agree on these cases; S34 adds corporate reasons (independent teams, lower server cost). No T1/T2 source states the criteria; web.dev (S01, S11) only documents the cost side. | grounded (T3/T4); inferred as a rule |
| UI-C05 | Prefer server-side or static rendering over a full rehydration approach, because rehydration makes pages look interactive before they respond and hurts TBT and INP. | decision | js | S01 ("consider SSR or static rendering over a full rehydration approach"), S34 ("dead" pages) | majority | S34 is a critique, not a measurement; S30 accepts hydration as the normal mechanism. | grounded |
| UI-C06 | Send JavaScript only for the parts of a page that are interactive; leave static regions as plain HTML. | practice | js | S33, S30 (reduce bundle by marking only interactive components as client), S01 | majority | Islands (S33) and Server Components (S30) both implement it; classic SPA bundles do not. | grounded |
| UI-C07 | Do not use islands (independently hydrated widgets) when many widgets must share live state; use a single client-state owner or the URL instead. | practice | js | S33 | majority | Single T3 source (secondary, patterns.dev); consistent with S26 on interdependent UI. | grounded (one source) |
| UI-C08 | Use static (build-time) rendering only when the set of URLs is known ahead of time; use per-request rendering otherwise. | practice | neutral | S01, S31 | consensus | - | grounded |

**Node tier and boundary**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C09 | Adding an SSR meta-framework with request-time rendering adds a JavaScript server runtime as a tier beside the Python application server; build-time rendering or static export avoids that tier. | decision | js | S29 (run at build time or per request on a web server), S31 (features needing a Node.js server are unsupported in static export), S30; boundary: ARCH | contested | Framework docs (S29, S30) present the server runtime as normal; hypermedia sources (S24, S25) argue the logic should stay in the one server language. No source weighs the operational cost of the extra tier. | inferred (synthesis of S29, S31, S25) |
| UI-C10 | Where a server/client code boundary exists, mark it explicitly and keep secrets on the server side of it; boundary: SEC. | practice | js | S30 (`use client`, `server-only`, env prefix rule) | consensus | Only one framework documented. | grounded |
| UI-C11 | The presentation tier owns handling of HTTP requests and rendering, and the interaction; domain rules and persistence belong to other tiers; and a team should span the layers rather than own one. Boundary: ARCH, APP. | principle | neutral | S20, S22 (separating UI from data storage improves UI portability and server scalability) | consensus | - | grounded |

**Client state**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C12 | Distinguish four kinds of client-side state and give each an explicit owner: server state (remote data), URL state (navigable view), form state (in-progress input), UI state (ephemeral widget state). | principle | neutral | S27 (server vs client), S17, S16, S28, S22 | majority | Server-vs-client is stated by S27; URL, form and UI state as classes are my synthesis; no source lists all four. | inferred (from S27, S17, S16, S28, S22) |
| UI-C13 | Treat server state as a cached copy of data owned elsewhere that can go stale, not as state the client owns. | principle | neutral | S27 (remote ownership, can change without your knowledge, can become out of date) | majority | One T3 source (maintainers of a caching library); consistent with HTTP caching sources S04/S06. | grounded |
| UI-C14 | In a client-rendered app, manage server state with a dedicated cache (deduplication, background refresh, staleness) rather than a general-purpose state store. | decision | js | S27 | majority | Vendor source with interest; alternatives (SWR in S31, framework data layers) exist. Does not apply to server-rendered pages, where the browser HTTP cache plays this role. | grounded (one source) |
| UI-C15 | Store the minimum state and derive the rest; keep one source of truth and avoid duplicated copies. | principle | js | S28 | consensus | Stated for React; the rule is general. | grounded |
| UI-C16 | Keep view state that users navigate, bookmark or share in the URL, use the History API for client-side routing, and do not use fragments to load different content. | practice | http | S17, S32, S22 (control state carried in representations) | consensus | - | grounded |
| UI-C17 | After a successful form POST, respond with a redirect (303) to a GET page so refresh and bookmarking do not resubmit. Boundary: API. | practice | http | S35 | majority | Only a T4 source read; the mechanism is standard but a T1 citation (RFC 9110, 303 See Other) was not read. | grounded in T4 only; promote after T1 read |
| UI-C18 | Use browser-native validation for user feedback, and always re-validate every submitted value on the server, because client checks are bypassable. Boundary: SEC, API. | practice | neutral | S16 | consensus | - | grounded |

**Delivery and caching**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C19 | Give static assets content-derived (fingerprinted) URLs and serve them with `Cache-Control: public, max-age=31536000, immutable`; change the URL when content changes. | practice | http | S04, S05, S19 | consensus | - | grounded |
| UI-C20 | Serve HTML documents with `Cache-Control: no-cache` plus `ETag`/`Last-Modified` (revalidate every time); use `no-store` only when nothing may be stored. | practice | http | S04, S06 (no-cache requires validation; no-store forbids storing) | consensus | - | grounded |
| UI-C21 | Mark responses personalised by cookie or login `private`, because shared caches could otherwise leak them; a shared cache must not reuse a response to an Authorization request unless the response allows it. Boundary: SEC. | practice | http | S04, S06 (sect. 3.5) | consensus | - | grounded |
| UI-C22 | Collect static files at build/deploy time and serve them from outside the Python application process (same web server, dedicated static server, or CDN); larger sites usually use a dedicated server or CDN. | decision | python | S18 | consensus | S18 lists four options and calls serving from Django itself a fallback; a CDN needs a storage backend. | grounded |
| UI-C23 | Use a hashing static-files storage so that asset references inside CSS/JS are rewritten to the fingerprinted names. | practice | python | S19 (ManifestStaticFilesStorage) | consensus | - | grounded |
| UI-C24 | Build assets in a build stage that is separate from release and run, and never mutate a release after creation. Boundary: OPS. | principle | neutral | S21 | consensus | Applying it to front-end assets is my reading of a general rule. | grounded (rule); inferred (assets) |
| UI-C25 | Do not set `no-store` on pages that are not sensitive and do not register `unload` handlers, so that pages stay eligible for the back/forward cache. | practice | http | S14 | consensus | - | grounded |

**Performance**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C26 | Target LCP of 2.5 s or less, INP of 200 ms or less and CLS of 0.1 or less, measured at the 75th percentile of page loads, segmented by mobile and desktop. | principle | neutral | S02, S12 | consensus | - | grounded |
| UI-C27 | Treat field measurement as the primary source of performance truth; lab tools do not substitute for it (and cannot measure INP). Boundary: OPS. | principle | neutral | S02 | consensus | - | grounded |
| UI-C28 | Make the LCP resource discoverable in the initial HTML, never lazy-load it, and avoid client-side rendering of the LCP element; the bulk of LCP time is HTML response (TTFB, about 40%) plus resource load (about 40%). | practice | http | S10 | consensus | - | grounded |
| UI-C29 | Keep the DOM small, break long event-handler work into separate tasks, and avoid rendering large HTML with client JS, to keep INP low. | practice | js | S11, S01 (JS amount grows with client rendering) | consensus | - | grounded |
| UI-C30 | Reserve space for asynchronously loaded content (images, embeds, late content) to avoid layout shift. | practice | neutral | S13 | consensus | - | grounded |
| UI-C31 | Set performance budgets per page type and enforce them in the build (for example Lighthouse CI), rejecting or optimising when exceeded. Boundary: OPS. | decision | neutral | S09 | majority | S09's sample numbers (TTI under 5 s, 170 KB critical path, 3G baseline) are examples tied to a past device baseline; metrics named there include non-Core-Web-Vitals timings. Use Core Web Vitals (UI-C26) as the budget metrics. | grounded (practice); numbers not adopted |

**Crawlability and accessibility**

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| UI-C32 | Prefer server-side or pre-rendering for pages that must be crawled and fast, since not all bots run JavaScript; for client-rendered error pages, redirect to a real 404 or inject `noindex`. | practice | http | S32 | consensus | One vendor source; matches S01 and S10. | grounded |
| UI-C33 | Decide a WCAG 2.2 conformance level (A, AA or AAA) as a project requirement; conformance is judged per full page, so every part of a page, including embedded third-party content, counts. | decision | neutral | S07 (sect. 5.2) | consensus | AA as the usual default is not stated in what I read. | grounded (page-level rule); AA default open |
| UI-C34 | Use native HTML elements and attributes before ARIA, do not change native semantics, and make every interactive control keyboard operable. | practice | neutral | S15 (rules 1-3), S03 | consensus | - | grounded |
| UI-C35 | Consider accessibility from the start of a project and involve users early, rather than adding it at the end. | principle | neutral | S08 | consensus | Thin: S08 says early involvement makes the work better; the business and legal case was not found in what was read. | grounded (weak) |

### Gaps

- No single authoritative source for the four-way client-state taxonomy (UI-C12): inferred.
- UI-C17 (Post/Redirect/Get): needs RFC 9110 (303 See Other) as T1 backing.
- No T1/T2 source gives the criteria for SPA vs server-rendered (UI-C03/C04): the debate is carried by T3/T4. A T2 candidate not read: Fowler or Kleppmann-style essays on client/server split; Ousterhout-style complexity arguments.
- Islands originators (Sylor-Miller, Jason Miller) not read; S33 is a secondary summary.
- Cost-of-JavaScript evidence: the web.dev page failed (404); S01 and S11 give only qualitative support.
- Operational cost of an extra Node tier is undocumented in any source read (UI-C09 inferred).
- Accessibility business/legal case (jurisdictional requirements) not covered; WCAG level default not grounded.
- Out of reading: service workers/PWA, CDN/edge rendering, compression and HTTP/2/3, CSS/design systems, i18n, micro-frontends, real-time channels, web components.
