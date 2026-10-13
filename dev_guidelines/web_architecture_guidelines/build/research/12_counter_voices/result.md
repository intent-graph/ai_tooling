# Counter-voices for one-sided debates (area CV, round 2)

## L1 headline

Round 1 told four debates from one side only; reading the other side shows that both sides agree on where the boundary lies and disagree on the default: a rich client is justified for realtime, offline or very frequent local state (hypermedia advocates concede it), services-first is justified only with strong domain knowledge, a large multi-team organisation and operational maturity (even Newman, the usual authority, argues monolith-first), server-side sessions are the sane default for ordinary first-party sites while bearer tokens fit SPA-to-API and federation, and a practitioner dissent (De Ryck) says token storage matters less than preventing XSS. Certainty: grounded on positions, thin on volume (one T2 source per dissent); DDIA itself could not be read, only Kleppmann's own essays.

Pinned: 25 sources (T1 = 4, T2 = 11, T3 = 8, T4 = 2); 24 claims; contested = SPA vs hypermedia as the default; services-first vs monolith-first; browser-held tokens in memory vs HttpOnly cookie session (and localStorage); client-owned data (local-first) vs server-authoritative data; failed fetches on T1 sources: none (DDIA itself, a T2 book, was not readable: publisher page returned 403, no free text exists).

## L2 claims

Pinned: 25 sources (T1 = 4, T2 = 11, T3 = 8, T4 = 2); 24 claims; contested = SPA vs hypermedia as the default; services-first vs monolith-first; browser-held tokens in memory vs HttpOnly cookie session (and localStorage); client-owned data (local-first) vs server-authoritative data; failed fetches on T1 sources: none (DDIA itself, a T2 book, was not readable: publisher page returned 403, no free text exists).

Clusters

1. Both camps agree on when a rich client is needed (realtime, offline, very frequent updates, many interdependent UI states); they disagree on which side is the default. Agreement majority on the boundary, contested on the default. Grounded (boundary), inferred (synthesis). CV-C01, C02.
2. The SPA side's own sources document its costs: JS grows with the app, hard on mobile, SEO, state, navigation, monitoring; React's docs make SPA the tool default yet steer to a server-capable framework. Consensus. Grounded. CV-C03, C04, C05.
3. Hybrid ("transitional") apps and independent frontend teams are the SPA-side arguments beyond raw interactivity; each is a single source or secondhand. Contested. Grounded (position), open (strength). CV-C06, C07.
4. Local-first software (Kleppmann and co-authors) puts the data copy on the client and sync in the background; strongest T2 argument against server-authoritative defaults, applies to offline and collaborative apps. Contested. Grounded. CV-C08.
5. Services-first has a real, conditional defence (Tilkov: splitting a monolith is extremely hard, in-monolith discipline rarely holds; needs domain knowledge and size). Newman, often cited as the opponent of monolith-first, in fact advises caution on greenfield. Contested. Grounded. CV-C09, C10, C11.
6. The split decision is driven by size, number of teams and independent deployability, not by fashion; all sources read name independent deployability as the point. Majority to consensus. Grounded, with an inferred decision rule. CV-C12, C13, C14.
7. Sessions vs bearer tokens: sessions for ordinary first-party sites (T3), JWT bearer for API clients, SPAs and federation (T3, official FastAPI path), BFF with cookie session as the secure SPA pattern (T3 plus round-1 IETF), in-memory tokens as the vendor's SPA advice, and De Ryck's dissent that XSS prevention outranks storage location. Contested. Grounded. CV-C15 to C20.
8. Kleppmann's essays (DDIA itself unread): no CP/AP labels, avoid dual writes (one system of record, derived stores), design encodings for forward and backward compatibility, keep logic separate from data fetching. Consensus or majority. Grounded. CV-C21 to C24.

Live debates (one line each)
- Default for text and CRUD sites: server-rendered hypermedia vs SPA/JSON API (conditions agreed, default not).
- Services-first (Tilkov) vs monolith-first (Fowler, Newman, Richardson as a starting point).
- Browser tokens in memory (Auth0) vs BFF cookie session (Duende, IETF BCP) vs "storage is secondary, stop XSS" (De Ryck, who accepts localStorage); contradicts the round-1 consensus claim SEC-C12 in part.
- Client-owned data with sync (local-first) vs server as the single authority.

Label corrections for round-1 claims
- ARCH-C05 and APP-C08: use `majority`; the named dissent is Tilkov (conditional), not Newman.
- UI-C03 and API-C01: one shared contested node; certainty "grounded (positions)" now that the SPA side is read, with T1 (web.dev, MDN, React docs) giving only the cost side.
- SEC-C11: stays contested; SEC-C12 should be marked `majority` (De Ryck dissent, Auth0 allows localStorage "if necessary").

Not covered
- DDIA chapters read directly (publisher page 403, no free copy); Kleppmann claims here come from his own essays only. Rich Harris's talk (only a secondhand report read). Hypermedia Systems book pages (404). Stateless-scalability argument for tokens (seen only in T4 search snippets, not read). The microservices-first literature beyond Tilkov (no second voice). Numeric team-size thresholds (none found).

## L3 full

Pinned: 25 sources (T1 = 4, T2 = 11, T3 = 8, T4 = 2); 24 claims; contested = SPA vs hypermedia as the default; services-first vs monolith-first; browser-held tokens in memory vs HttpOnly cookie session (and localStorage); client-owned data (local-first) vs server-authoritative data; failed fetches on T1 sources: none (DDIA itself, a T2 book, was not readable: publisher page returned 403, no free text exists).

Method note: the fetch tool returns a condensed rendering of each page, so quotes below are as returned, not byte-verified against the page.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| CV-S01 | T2 | Don't start with a monolith (June 2015) | Stefan Tilkov, hosted on martinfowler.com | https://www.martinfowler.com/articles/dont-start-monolith.html | The services-first position |
| CV-S02 | T2 | Microservices For Greenfield? (April 2015) | Sam Newman | https://samnewman.io/blog/2015/04/07/microservices-for-greenfield/ | Conditions for services early |
| CV-S03 | T2 | MonolithFirst | Martin Fowler | https://www.martinfowler.com/bliki/MonolithFirst.html | Monolith-first and its stated counter-view |
| CV-S04 | T2 | MicroservicePremium | Martin Fowler | https://martinfowler.com/bliki/MicroservicePremium.html | Cost of services vs complexity |
| CV-S05 | T2 | Microservices | James Lewis, Martin Fowler | https://martinfowler.com/articles/microservices.html | Benefits, Conway's law, "future?" caveats |
| CV-S06 | T3 | Monolithic architecture pattern | Chris Richardson, microservices.io | https://microservices.io/patterns/monolithic.html | When a monolith stops fitting |
| CV-S07 | T3 | Sam Newman on moving from monolith systems to microservices | O'Reilly interview | https://oreilly.com/ideas/sam-newman-on-moving-from-monolith-systems-to-microservices | Independent deployability as the goal |
| CV-S08 | T1 | Rendering on the Web | web.dev (Google) | https://web.dev/articles/rendering-on-the-web | Costs and fit of CSR, SSR, static |
| CV-S09 | T1 | SPA (glossary) | MDN | https://developer.mozilla.org/en-US/docs/Glossary/SPA | Definition, benefits, drawbacks of SPAs |
| CV-S10 | T1 | Build a React app from scratch | React documentation | https://react.dev/learn/build-a-react-app-from-scratch | React's own default and advice |
| CV-S11 | T2 | Micro Frontends | Cam Jackson, martinfowler.com | https://martinfowler.com/articles/micro-frontends.html | The independent-frontend-teams argument |
| CV-S12 | T2 | Local-First Software | Kleppmann, Wiggins, van Hardenberg, McGranaghan (Ink & Switch, 2019) | https://www.inkandswitch.com/essay/local-first/ | Client-owned data with sync |
| CV-S13 | T4 | The Website vs. Web App Dichotomy Doesn't Exist | Jake Lazaroff | https://jakelazaroff.com/words/the-website-vs-web-app-dichotomy-doesnt-exist/ | A classification by dynamism and connectivity |
| CV-S14 | T4 | A response to Rich Harris (htmx 4.0 essays) | htmx authors | https://four.htmx.org/essays/a-response-to-rich-harris | Secondhand report of Harris's talk (talk itself unread) |
| CV-S15 | T3 | When to use hypermedia | htmx authors | https://htmx.org/essays/when-to-use-hypermedia/ | The hypermedia camp's own limits |
| CV-S16 | T3 | Why JWTs suck as session tokens (Aug 2017) | Randall Degges, Okta developer blog | https://developer.okta.com/blog/2017/08/17/why-jwts-suck-as-session-tokens | Case for plain sessions (original on DZone returned 403, Okta copy read) |
| CV-S17 | T3 | Token storage | Auth0 documentation | https://auth0.com/docs/secure/security-guidance/data-security/token-storage | Vendor advice for SPA vs web app |
| CV-S18 | T3 | LocalStorage and XSS (token storage) | Philippe De Ryck, Pragmatic Web Security | https://pragmaticwebsecurity.com/articles/oauthoidc/localstorage-xss.html | Practitioner dissent on storage |
| CV-S19 | T3 | BFF documentation | Duende Software | https://docs.duendesoftware.com/bff/ | Case for BFF with cookie session |
| CV-S20 | T1 | OAuth2 with Password (and hashing), Bearer with JWT tokens | FastAPI documentation | https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ | What the framework path teaches |
| CV-S21 | T3 | Cookies vs Tokens: the definitive guide | Auth0 blog | https://auth0.com/blog/cookies-vs-tokens-definitive-guide/ | Token-side view; page barely compares (cookies mentioned once) |
| CV-S22 | T2 | Rethinking caching in web apps (2012) | Martin Kleppmann | https://martin.kleppmann.com/2012/10/01/rethinking-caching-in-web-apps.html | Logic vs data-fetching separation |
| CV-S23 | T2 | Schema evolution in Avro, Protocol Buffers and Thrift (2012) | Martin Kleppmann | https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html | Encoding and compatibility |
| CV-S24 | T2 | Using logs to build a solid data infrastructure (2015) | Martin Kleppmann | https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html | Dual writes, system of record |
| CV-S25 | T2 | Please stop calling databases CP or AP (2015) | Martin Kleppmann | https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html | CAP misuse |

Fetch failures: DDIA chapter 1 on the publisher's site (403, T2 book, no free copy found; dataintensive.net offers purchase links only); DZone copy of Degges (403, replaced by Okta copy); hypermedia.systems pages (404, replaced by the htmx essay on the same topic); an OWASP JWT cheat-sheet URL (404, not used); a Confluent event-sourcing article was fetched but its author is not Kleppmann, so it was dropped. No T1 fetch failed.

### Claims

Debate 1: hypermedia vs SPA/JSON API (coverage item 13)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| CV-C01 | Use a client-rendered rich client with a JSON or sync contract when the UI has many dynamic interdependencies, needs offline use, updates state extremely often (mouse-move rate), or is realtime or collaborative. | decision | neutral | CV-S15 ("not a good fit if" list), CV-S13, CV-S12, CV-S09 | majority | Hypermedia authors themselves list these cases (CV-S15: "a hypermedia network request in-between a mouse move and a UI update will not work well"); Lazaroff: realtime sites "are client-side apps by necessity". No source read argues the opposite. Refines UI-C04 (now two camps agree). | grounded |
| CV-C02 | The two camps agree on the boundary (interactivity, offline, update frequency) and differ on the default for text, forms and CRUD: hypermedia advocates default to server HTML, the React ecosystem defaults to a client app with optional server rendering; record the default as a project decision with the boundary conditions as its trigger. | decision | neutral | CV-S15, CV-S10, CV-S08, CV-S09, CV-S13 | contested | Server-HTML default: htmx authors (CV-S15), round-1 UI-C03 sources. Client-app default: React docs (SPA is "the default architecture for most build tools", CV-S10). Neutral platform guidance (CV-S08, CV-S09) lists costs of each and states no default. | inferred (synthesis across the cited sources) |
| CV-C03 | Budget client JavaScript: the amount grows with the app and hurts interaction latency, and client rendering is hard to keep fast on mobile; pure client rendering suits tight JS budgets with efficient round trips. | principle | js | CV-S08 "Client-side rendering" | consensus | | grounded |
| CV-C04 | Count the costs of an SPA before choosing it: harder search-engine indexing, more state management, extra work for navigation, harder performance monitoring; benefits are no full-page reloads and a more dynamic experience. | principle | js | CV-S09 "Benefits", "Drawbacks" | consensus | | grounded |
| CV-C05 | If a client-rendered React app is chosen, adopt a framework that provides routing, data-loading and server rendering rather than assembling one; a from-scratch setup "is often the same as building your own ad-hoc framework", and fetching data inside components creates request waterfalls. | practice | js | CV-S10 | consensus | Single official source; framework vendors have an interest in this advice. | grounded |
| CV-C06 | Pages that are neither documents nor applications ("transitional apps") should mix server navigation with client enhancement; MPAs fall short on persisting media across navigations, back-button with infinite scroll, animations and latency-gated interactions. | decision | js | CV-S14 (secondhand report of Harris's talk) | contested | Harris (as reported): mix of SPA and MPA techniques with progressive enhancement; htmx authors reply that hypermedia tooling (preserve, push-url, CSS transitions) solves the same MPA gaps. Talk not read. | open (strength of the MPA-gap list unverified; T4 secondhand) |
| CV-C07 | When several teams work on one product and the frontend monolith blocks them, split the frontend into independently deployed vertical slices, only if automation exists to run the extra infrastructure. | decision | js | CV-S11 | contested | Micro-frontend argument (independent deployment, incremental upgrades). Server-rendered camp reaches team independence through server-side components instead (CV-S15). Single T2 source. | grounded (position) |
| CV-C08 | For apps where offline use, multi-device collaboration or user data ownership matter, keep the primary copy of the data on the client and sync in the background (local-first, e.g. CRDTs), rather than treating the server as the single authority. | decision | neutral | CV-S12 | contested | Authors (Kleppmann et al.): server round trips cause unavoidable latency and cloud apps lose data when a service stops; the server-authoritative default (round-1 sources, CV-S15) keeps one source of truth. Authors state that CRDT viability was shown by their own prototypes. | grounded (position); open (maturity beyond the authors' prototypes) |

Debate 2: monolith first vs services first (coverage item 14)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| CV-C09 | A new system may be split into services from the start when the team already knows the domain well (ideally a second version of an existing system), the system is large enough to need distribution, and the subsystems can truly develop and deploy independently. | decision | neutral | CV-S01 | contested | Tilkov: splitting an existing monolith is "extremely hard" (shared libraries, domain objects, persistence model, transaction assumptions) and monolith discipline holds "only very rarely"; a two-person few-week project need not. Opposed by CV-S03, CV-S02, CV-S06 as a starting point. | grounded |
| CV-C10 | On a greenfield project be cautious with services: wrong boundaries are expensive; split only on boundaries that are very clear (e.g. a third-party integration unlikely to change), keep the rest monolithic, and keep separate data schemas for likely future services. | decision | neutral | CV-S02 | majority | Newman: "not saying never do microservices for greenfield"; conditions in favour: stable boundaries, cloud (not customer-installed) deployment, a team already competent at running distributed systems (add beyond two services only after that). This sits on the monolith-first side, so ARCH-C05's missing dissent is Tilkov, not Newman. | grounded |
| CV-C11 | Treat any advice on monolith vs services as tentative: the evidence is anecdotal, and "a good in-process interface is usually not a good service interface", so a modular monolith does not make later extraction free. | principle | neutral | CV-S03, CV-S05 | consensus | Fowler states he lacks enough anecdotes for a firm rule; services-first proponents cite team-first organisation from day one (CV-S03 reports this view). | grounded |
| CV-C12 | Move from one deployable to services when size, complexity and the number of teams make the single codebase and pipeline the bottleneck (team autonomy, deployment speed, technology and scaling needs differ by part); team structure shapes the result (Conway). | decision | neutral | CV-S06, CV-S05, CV-S04 | majority | Richardson: large internet services started as monoliths; drawbacks "become more severe" with size and team count. Fowler: services only when too complex to manage as a monolith (round-1 ARCH-C06). No numeric threshold in any source. | grounded |
| CV-C13 | Define the goal of any split as independent deployability, not the service count: pick the decomposition that gives teams independent releases, and start with one or two services before adding more. | principle | neutral | CV-S07, CV-S05, CV-S06 | consensus | | grounded |
| CV-C14 | Decision rule for the guideline: default to one deployable with enforced module boundaries when domain knowledge is weak or the team is small; consider services-first only when domain knowledge, size and operational maturity are all present. | decision | neutral | CV-S01, CV-S02, CV-S03, CV-S06 | majority | Tilkov dissents on the default for large known domains; the other four agree on the default for small or uncertain ones. | inferred (synthesis of the four sources) |

Debate 3: sessions vs bearer tokens for first-party browser apps (coverage item 29)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| CV-C15 | For ordinary first-party sites that mostly render dynamic CRUD content, use plain server-side sessions: a JWT carrying only a user id is about 51 times the size of a session cookie on every request, needs double signing, and the database is usually hit anyway, so statelessness buys little. | decision | http | CV-S16 | majority | Degges (2017): sessions with caching are faster and simpler; JWT stays for server-to-server, mobile or SPA to API, and federation. Round-1 SEC-C11 agrees (IETF, OWASP, Django). Dissent: bearer-token tutorials (CV-C20). | grounded |
| CV-C16 | Use bearer tokens (JWT) where the client is not a same-site browser page: API access from mobile or SPA clients, multi-party identity, OpenID Connect and federation. | decision | http | CV-S16, CV-S17, CV-S20 | majority | Session camp accepts these uses; the token camp (Auth0, FastAPI) presents tokens as the SPA default. Whether a same-site SPA counts as such a client is the open point (CV-C19). | grounded |
| CV-C17 | If tokens must live in an SPA, keep them in memory (a Web Worker scope where available, otherwise closures) rather than localStorage; accept localStorage only with short token lifetimes and few third-party scripts; for a server-rendered web app keep tokens server-side or in an encrypted session cookie (4 KB limit). | practice | js | CV-S17 | contested | Auth0: in-memory is "the most secure option". Round-1 SEC-C12: never localStorage. De Ryck (CV-C18) accepts localStorage. BFF camp (CV-C19) removes tokens from the browser. | grounded |
| CV-C18 | Spend effort on preventing XSS rather than on choosing a token storage location: "XSS means game over"; in-memory or Web Worker storage makes attacks harder but never solves the root problem, and when unsure localStorage is acceptable. | principle | js | CV-S18 | contested | De Ryck (T3 practitioner) vs SEC-C12 (consensus: never use localStorage) and Auth0 (in-memory). All three agree on the XSS premise (SEC-C10). | grounded |
| CV-C19 | For first-party browser apps, use a backend-for-frontend with a cookie session: no tokens in browser memory, the server can end sessions at once, and silent token renewal in the browser breaks under third-party cookie blocking. | decision | http | CV-S19 | majority | Duende (vendor docs, aligned with the IETF browser-apps BCP read in round 1) vs the token-in-browser camp (CV-C17). Vendor has a product interest. | grounded |
| CV-C20 | When following the framework's official JWT bearer tutorial for a browser client, decide token storage, revocation and session handling separately: the tutorial teaches an Authorization-header bearer flow with 30-minute expiry and does not address cookies, sessions or revocation. | practice | python | CV-S20 | consensus | Auth0's blog page (CV-S21) likewise promotes tokens with refresh rotation for SPAs and barely mentions cookies. | grounded |

Debate 4: Kleppmann read directly where possible (coverage item 32)

DDIA could not be read (see register). The following come from Kleppmann's own essays, which precede or restate the book's themes; none is cited as DDIA.

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| CV-C21 | Do not describe or choose a datastore as "CP" or "AP"; state the consistency model per operation (CAP "consistency" means linearizability only, ignores latency and multi-object transactions). | principle | neutral | CV-S25 | consensus | Single author; no dissent read. | grounded |
| CV-C22 | Avoid dual writes to several datastores from application code (races give permanent divergence, partial failure leaves half-finished changes); write to one system of record in transaction order and derive caches, indexes and other stores from its change log. | decision | postgres | CV-S24 | majority | Kleppmann proposes an append-only log (Kafka) as the carrier; the minimum rule (one system of record) supports round-1 ARCH-C34 (one Postgres first) by inference. Simpler carriers (outbox table) not read. | grounded (rule); inferred (link to ARCH-C34) |
| CV-C23 | Design encodings and APIs for forward and backward compatibility (tolerate unknown fields, add fields with defaults, keep removals safe) so components can be upgraded independently and at different times. | principle | neutral | CV-S23 | consensus | boundary: contract. | grounded |
| CV-C24 | Keep business logic free of data fetching and network concerns, declaring its data dependencies up front, so the same logic can run online, in batch, or in cache-invalidation, and dependency graphs can drive cache invalidation. | principle | neutral | CV-S22 | contested | Exploratory 2012 essay by one author; the common practice (TTL or manual invalidation, round-1 caching claims) was not argued against by any source read. | grounded (position); open (adoption) |

### Gaps

- DDIA read directly: not possible; open. Ch. 1 and 12 themes (reliability, derived data) are touched only through CV-C21 to C24.
- Rich Harris's talk and Hypermedia Systems pages not read; CV-C06 rests on a secondhand report.
- Second services-first voice (beyond Tilkov) not found among T1/T2; Newman turned out to favour caution. A book-length Newman text (Building Microservices) was paywalled and not read.
- Pro-token practitioner voices are vendor-tied (Auth0, FastAPI); the statelessness-scale argument was seen only in T4 search snippets and is not claimed.
- No T1/T2 numeric thresholds for team size, load or token size beyond Degges's single measurement.
