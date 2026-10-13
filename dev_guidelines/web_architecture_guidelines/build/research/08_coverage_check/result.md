# Coverage check of the 7-area research sweep

## L1 headline

The sweep is solid enough to start distilling the `PIG-WEB` defaults graph, but not yet the web-app philosophy graph: tiers, contract, security and operations are well covered, while six cross-cutting topics fall between areas, five topics are claimed twice with diverging labels, and the principle set is mostly stack-neutral engineering wisdom, with the web-specific part resting on one inferred claim (ARCH-C45). Certainty: grounded on counts and on what each L2 says, inferred on the sufficiency verdicts, open on whether the missing topics matter for this guideline's scope.

Pinned:
- Areas checked: 7 of 7 (DATA, APP, API, UI, SEC, OPS, ARCH); missing: none. Read: L1 and L2 of each; L3 only for the claim-level column and the principle lines.
- Sources by area (T1/T2/T3/T4): DATA 24/5/9/3 = 41; APP 24/15/3/0 = 42; API 12/8/8/0 = 28; UI 19/4/10/2 = 35; SEC 33/2/0/0 = 35; OPS 18/16/2/0 = 36; ARCH 3/22/6/2 = 33. Total 250 (133 T1, 72 T2, 38 T3, 7 T4).
- Claims by area: DATA 56, APP 50, API 37, UI 35, SEC 60, OPS 53, ARCH 45 = 336. Principle-level claims: about 83 (DATA 5, APP 9, API 10, UI 10, SEC 10, OPS 13, ARCH 26).
- Gaps with no owner: 8 topics (rate limiting and abuse, file upload and object storage, real-time channels, multi-tenancy, runtime topology and TLS, audit logging, client-side error reporting, repository layout); 4 more thinly owned.
- Contested topics collected: 11 distinct debates (7 contested labels plus 4 that are labelled consensus in one area and contested in another).
- Same topic, diverging claim or label: 5 (queue/Postgres-for-everything, config and secrets, hypermedia vs SPA, monolith agreement label, RLS use).
- Philosophy verdict: partial; enough seed for roughly 15 to 20 web-distinct principles, but the "web app has its own philosophy" thesis is inferred, not sourced.

## L2 claims

### Gaps (topics no area owns)

1. Rate limiting and abuse protection: listed as not covered by API, APP and SEC, each assuming another owns it; no claim exists. Open. Follow-up: one targeted research slot (SEC lead, API boundary), T1 = OWASP API Security and RFC 6585/RateLimit headers draft.
2. File upload, object storage, large binaries: not covered by APP, API, SEC (and the seed expects it). Open. Follow-up: one slot "uploads and media" spanning APP, API, SEC.
3. Real-time channels (SSE, WebSocket, polling): not covered by APP, API, UI; it changes the statelessness and pooling claims (APP-C26 to C31, DATA-C36 to C39). Open. Follow-up: one slot, decision-level (poll vs SSE vs WebSocket).
4. Multi-tenancy: DATA, ARCH list it as not covered; SEC only quotes a debate (separate databases vs schemas vs RLS). No area owns the decision. Open. Follow-up: one slot or an explicit "out of scope: single-tenant" statement in the brief.
5. Runtime topology: reverse proxy, TLS termination and HTTPS/HSTS, WSGI/ASGI server, worker counts, static serving, CDN. SEC excludes TLS, OPS excludes CDN, containers and IaC, APP defers worker tuning to OPS, UI excludes CDN and HTTP/2/3. Nothing describes the deployment shape of the three tiers. Grounded (all four gap lists say so). Follow-up: one slot "deployment topology" (T1: Django deployment checklist, nginx/gunicorn/uvicorn docs, MDN HSTS, RFC 6797).
6. Audit logging: DATA reads only T3/T4 on audit tables; SEC marks it boundary OPS; OPS does not list it among clusters or gaps. Orphaned. Follow-up: assign to OPS, short pass (OWASP Logging cheat sheet).
7. Client-side error reporting: UI defers it to OPS; OPS covers browser OpenTelemetry (experimental) but not error capture or RUM. Orphaned. Follow-up: add to the OPS follow-up.
8. Repository layout and module structure: the seed expects it (section 2.G); APP lists Django layout and modular-monolith guidance as not covered, ARCH has modularity principles (ARCH-C10 to C13) but no layout. Open. Follow-up: derive from ARCH plus Django docs after the main distillation, or drop from scope.
9. Thinly owned, lower priority: HA, replication, failover and major upgrades (DATA, "not researched"); incident response and on-call, load testing, log retention and cost (OPS); CSS architecture, i18n, PWA/offline, micro-frontends (UI, ARCH); threat modeling (SEC); GDPR and erasure (DATA); scheduled jobs and email sending (APP, none); search (ARCH-C34 mentions it as a Postgres use, no area researches it). Mostly open. Follow-up: decide per topic whether it is in scope for "classic website"; most are not needed for a first release of the graphs.
10. Seed checklist items that are covered: tier ownership, contract, identity, security by tier, observability, caching, testing, delivery. Seed "Level 4 anti-patterns" has no research area; anti-patterns can be derived from the claims (inferred), no research needed.

### Overlaps and inconsistencies (same topic, two or more areas)

11. Postgres as queue/cache/everything: DATA-C52 to C56 (consensus on mechanics, majority on the ceiling, grounded), APP-C19 (contested backing store: database vs broker vs staged drain), ARCH-C34 (contested, inferred). Three framings of one debate, with different agreement labels. Grounded. Follow-up: merge into one contested node owned by ARCH, with DATA holding the mechanics and APP the choice.
12. Config and secrets: APP-C47 to C50 (env vars, consensus on principle), OPS-C35 (env vars vs versioned config files, contested), SEC-C50 to C54 (env vars vs secrets manager, contested). APP and OPS state the same Twelve-Factor claim, OPS marks the topic contested, APP does not. Grounded. Follow-up: split into two nodes (non-secret config: env vs file; secrets: env vs manager) and re-label APP's cluster as majority.
13. Hypermedia vs SPA: API-C01 (certainty open, advocate sources only), UI-C03/C04 (contested, grounded in T3/T4 plus T1 platform guidance); UI states a default (server-rendered for text/CRUD) while API gives a fit rule without a default. Certainty labels differ for the same debate. Grounded. Follow-up: one shared contested node; one research pass for a T1/T2 voice on the SPA side (both areas name this gap).
14. Monolith first: APP-C08 labelled consensus (one T2 plus Twelve-Factor), ARCH-C04 to C06 labelled majority (microservices-first dissent not read). Same claim, two labels. Grounded. Follow-up: use majority; read one microservices-first source (Newman or equivalent).
15. Row-level security: DATA-C18 to C27 treat RLS facts as consensus; SEC-C40 to C44 say consensus on mechanics, majority on whether to use it. Consistent but split; the "use it?" decision should live once. Grounded. Follow-up: single decision node in PIG-WEB under SEC, with DATA mechanics as practice children.
16. Pure duplicates to dedupe before distillation (no conflict found): HTTP caching and fingerprinted assets (UI-C19 to C25, OPS-C47 to C50, API-C10); Core Web Vitals and field data (UI-C26 to C31, OPS-C19 to C23); stateless processes (APP-C26 to C31, OPS-C45/C46, API-C10, ARCH-C23); expand-migrate-contract (DATA-C05/C06/C35, OPS-C38 to C41, ARCH-C21); server-side authority over client checks (API-C02, SEC-C01, UI-C18); layering of logic vs delivery (APP-C01 to C03, ARCH-C15/C18, UI-C11); idempotency (APP-C43 to C46, API-C23 to C26, with the key mechanism single T3 in APP and a draft in API); attached-resource database (DATA-C02, OPS-C37, APP-C26 to C31). Grounded. Follow-up: assign one owner per cluster, others as cross-links.
17. Tension between ARCH-C29 to C31 (few technologies, boring tech) and the open UI decision on an extra Node SSR tier (UI-C09/C10): the principle bears on the debate but no area links them. Inferred. Follow-up: link in the graph.

### Contested topics collected (11)

18. Key type: identity vs UUIDv7 vs UUIDv4 (DATA). Grounded.
19. Soft deletion vs hard delete plus archive (DATA). Grounded.
20. Logic in database vs application (DATA-C44/C45, inferred; touches APP). Inferred.
21. Contract schema (views) vs direct table access (DATA). Grounded; one T3 fetch failed (PostgREST).
22. Domain model decoupled from ORM vs ORM as domain (APP-C07). Grounded.
23. Job-queue backing store, and Postgres for everything (APP-C19, DATA-C56, ARCH-C34), see item 11. Inferred.
24. Framework choice Django vs FastAPI vs Flask (APP-C38); no neutral source. Open.
25. HTML over the wire vs JSON API / SPA (API-C01, UI-C03/C04). Open (advocate sources).
26. Version identifier placement, five positions (API-C30). Grounded.
27. Extra Node SSR tier vs Python-only rendering (UI-C09/C10). Grounded as fact, open as decision.
28. Sessions vs bearer JWT (SEC-C08 to C14) and secrets medium (SEC, OPS-C35). Grounded.
Smaller debates, not counted: contract-first vs code-first OpenAPI, idempotency header mechanism, config granularity, test ratios, browser tracing adoption, session timeout numbers, islands vs full hydration, request-wide vs use-case transaction.

### Thin areas (T1/T2 grounding)

29. SEC: 33 T1, 2 T2, 0 T3, 0 T4: very strong on norms, thin on practitioner voice, which is why sessions vs JWT is told only by standards bodies and framework tutorials; ASVS levels unread (open). Follow-up: add 2 or 3 T2/T3 sources on session/JWT practice.
30. UI: 4 T2, 10 T3, 2 T4; both contested topics rest on T3 advocates, the PRG claim (UI-C17) on T4 only, crawlability (UI-C32) on one T3, client-state taxonomy (UI-C12) inferred, a T1 fetch failed. Follow-up: read RFC 9110 on 303, one T2 on SPA trade-offs.
31. DATA: 29 of 41 sources T1/T2, but deletion/history/audit and the logic-placement debate have only T3/T4 grounding; no normal-form source. Follow-up: one short pass on those four topics.
32. ARCH: only 3 T1 (normal for this area) but the dissent on monolith-first and DDIA were not read, "just use Postgres" rests on T4 and vendor posts, and the central synthesis ARCH-C45 is inferred. Follow-up: read Newman or a microservices-first source, and Kleppmann chapters directly.
33. APP: well grounded (39 of 42 T1/T2) but books by Kleppmann, Nygard, Evans were not read directly; OPS notes its fetch tool returned condensed page renderings, so its quotes are not byte-verified (the same tool was probably used elsewhere; not checked). Follow-up: spot-check a sample of quoted claims before distillation.
34. API and OPS: adequate (20 and 34 T1/T2); API's gap is the SPA side, OPS's is browser OpenTelemetry maturity.

### Philosophy-level sufficiency

35. Quantity: about 83 principle-level claims; ARCH holds 26, DATA only 5, APP 9. Enough raw material for a philosophy graph. Inferred.
36. Distinctiveness: most principles hold equally for a backend alone (ownership, YAGNI, boring technology, small releases, config outside code, test pyramid, idempotent retries). The web-distinct candidates are about 15 to 20: untrusted client and server-side authority (SEC-C01, API-C02, UI-C18), JS is hostile territory and tokens stay out of it (SEC-C10), progressive enhancement (UI-C01/C02), web constraints bought and paid for (ARCH-C22 to C25), contract style decides where logic lives (API-C01), statelessness per request (API-C10), same-origin default (API-C33), field-measured user-perceived performance (UI-C26/C27, OPS-C20), cross-tier correlated observability (OPS-C01, C23), URL as state (UI-C16), accessibility from the start (UI-C35), ARCH-C45. Inferred.
37. Weak spot: the thesis itself. No source states that a web app as a whole needs its own philosophy; ARCH-C45 says so and is labelled inferred by its author. Missing web-specific principles that the sweep does not state: the browser is a runtime you do not control (version skew between client and server, caching you do not own, multiple tabs), latency and the network as design material, the URL as the public interface, graceful failure of the client. Open. Follow-up: a synthesis step that classifies every principle as shared-with-backend, shared-with-data or web-distinct, plus one short research pass on the missing four (candidates: Fielding thesis, Fowler on micro frontends and BFF, Resilient Web Design, web.dev, all T1/T2).

### Recommended order of follow-ups

38. Before distillation (cheap, blocks consistency): items 11 to 16 (merge and relabel), item 37 (classification step), item 6 and 7 (assign owners).
39. Before PIG-WEB distillation (new research): runtime topology (5), rate limiting (1), uploads (2), real-time (3), SPA-side T1/T2 voice (13), microservices-first dissent (14).
40. Can wait or drop: item 9 topics, repository layout (8) until the graphs exist, multi-tenancy (4) unless the project scope is multi-tenant.

## L3 full

### Method and limits

Read: the shared brief; L1 and L2 of the seven result files; the claim tables of each L3 only for the level column and principle lines (counts and the principle list); the seed outline headings as a checklist only (never as evidence). Principle counts come from a pattern match on the L3 tables: APP's L3 lists claims in a form that did not match for the principle lines, so APP 9 is from its own L1 pin, UI 10 and OPS 13 from the matched lines; DATA 5, API 10, SEC 10, ARCH 26 likewise. The per-level counts reconcile with each area's total claim count for DATA, API, UI, SEC, OPS, ARCH (56, 37, 35, 60, 54 versus 53 pinned for OPS, so OPS counts have a deviation of one, probably a boundary entry; not investigated). Source totals are summed from the pins as written; fetch failures are as reported by each area.

### Seed checklist versus coverage

- Mission, tier model, data, application, contract, presentation: covered by DATA, APP, API, UI, ARCH.
- Identity and access, security by tier: SEC.
- Observability, performance and caching, testing, delivery and environments: OPS (caching shared with UI).
- Repository layout: no owner (item 8).
- Decision register: the contested topics (items 18 to 28) and the decision-level claims form its raw material (about 83 decision-level claims across areas: DATA 13, APP 16 or 13, API 12, UI 8, SEC 16, OPS 14, ARCH 10; approximate).
- Anti-patterns: derived, not researched.
- Expected for a JS + Python + Postgres website but absent from the seed and from every area: runtime topology and TLS, rate limiting, uploads, real-time, multi-tenancy, audit logging, client error reporting, email and scheduled jobs, search.

### Boundary handling

Boundaries were handled consistently for CORS (API owns, SEC defers), Postgres roles (DATA owns, SEC defers), caching (shared UI and OPS, duplicated), and the BFF (API-C36, SEC-C09 to C12 both). Two boundaries leak: audit logging and client error reporting (items 6 and 7).

### Certainty summary

- Grounded: area-level counts, pins, the gap lists as stated by the areas, the overlaps in items 11 to 16 (visible in L2 text).
- Inferred: sufficiency verdicts (items 35 to 37), the tension in item 17, the ranking in items 38 to 40, the web-distinct principle shortlist.
- Open: whether each unowned topic is in scope; whether "web app philosophy distinct from backend philosophy" can be supported by sources beyond ARCH-C45.

### Not checked

Whether any L3 claim contradicts another in wording while the L2 hides it (only L3 principle lines and a few specific claims were opened); source URLs; the byte-accuracy of quotes.
