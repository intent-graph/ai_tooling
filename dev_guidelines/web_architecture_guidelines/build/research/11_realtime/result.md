# Research result: RT, real-time channels at decision level (round 2, coverage item 3)

## L1 headline

Best practice for real-time channels is consensus on the mechanics (direction of data picks the channel; SSE and WebSocket need an async server and per-hop idle-timeout and buffering care; Postgres LISTEN/NOTIFY is a wake-up signal, not a queue) but contested on the default (SSE-first vs WebSocket-first) and on how far NOTIFY scales; certainty is grounded for mechanics (18 T1 sources) and inferred for the stack-level default.

Pinned:
- Sources: 25 (T1 18, T2 0, T3 6, T4 1).
- Claims: 38 (principle 4, decision 11, practice 23).
- Contested topics: SSE-first vs WebSocket-first as default; LISTEN/NOTIFY scaling ceiling under write concurrency.
- Failed fetch on a T1 source: Gunicorn design page (docs moved, redirect then 404 on 3 attempts); no replacement read, no Gunicorn claim made.

## L2 claims

Pinned:
- Sources: 25 (T1 18, T2 0, T3 6, T4 1).
- Claims: 38 (principle 4, decision 11, practice 23).
- Contested topics: SSE-first vs WebSocket-first as default; LISTEN/NOTIFY scaling ceiling under write concurrency.
- Failed fetch on a T1 source: Gunicorn design page (docs moved, redirect then 404 on 3 attempts); no replacement read, no Gunicorn claim made.

Clusters (agreement, certainty, ids):
1. The channel is picked by data direction, frequency and latency tolerance; take the weakest channel that fits (polling, long polling, SSE, WebSocket). Majority, inferred from T1 definitions plus T3 guides. RT-C01, C02, C03, C04, C36, C37.
2. SSE is one-way plain HTTP with built-in reconnect and resume; its limits are 6 connections per browser and domain on HTTP/1.1, GET only, text only; resume works only if the server can replay. Consensus, grounded (one inferred). RT-C05 to C09.
3. WebSocket is the bidirectional, low-overhead channel; it needs an Upgrade-aware proxy chain, has no automatic reconnect and no backpressure in the classic API. Consensus, grounded. RT-C10, C11, C12, C16, C17.
4. Every hop (reverse proxy, load balancer, platform router) has idle timeouts and may buffer; streaming endpoints need heartbeats under the shortest timeout and buffering off. Consensus, grounded. RT-C13, C14.
5. Stateless processes survive real-time if connections are disposable and truth stays in backing services; in-process connection registries work for one process only. Consensus on mechanism, inferred on the reconciliation. RT-C18, C20, C21, C23, C25.
6. Long-lived connections need an async (ASGI) server or a dedicated process type; a sync WSGI worker is tied up for the whole stream. Consensus, grounded. RT-C19, C22, C24.
7. Security and abuse: wss, Origin allowlist, no tokens in URLs, per-message authorization, size and rate limits, long-lived connections widen DoS exposure. Consensus, grounded. RT-C26, C27, C28.
8. LISTEN/NOTIFY is a wake-up signal: payload under 8000 bytes, not stored, transactional and ordered, lost when nobody listens, so notify then re-read state. Consensus, grounded. RT-C29, C30, C31, C35.
9. LISTEN needs a session-level connection (incompatible with transaction pooling); a listener stuck in a long transaction blocks queue cleanup. Consensus, grounded. RT-C32, C33.
10. NOTIFY scaling ceiling: commit-time global serialization reported by one production postmortem. Contested, grounded in one T3 account, thresholds open. RT-C34.

Live debates:
- SSE-first (simplicity, HTTP-native) vs WebSocket-first (intermediaries may silently buffer SSE; one channel for both directions): RT-C15.
- Use NOTIFY as the fan-out source vs move to an application-layer or broker mechanism once write concurrency is high: RT-C34.

Not covered: managed real-time services (Pusher, Ably, Supabase Realtime) as a build-vs-buy decision; WebTransport; Django Channels deployment topology and worker counts (sibling: runtime topology); presence, ordering and conflict resolution in collaborative apps; mobile push; Postgres logical replication or CDC as a fan-out source; Gunicorn behavior (fetch failed); load numbers (how many connections one process holds).

## L3 full

Pinned:
- Sources: 25 (T1 18, T2 0, T3 6, T4 1).
- Claims: 38 (principle 4, decision 11, practice 23).
- Contested topics: SSE-first vs WebSocket-first as default; LISTEN/NOTIFY scaling ceiling under write concurrency.
- Failed fetch on a T1 source: Gunicorn design page (docs moved, redirect then 404 on 3 attempts); no replacement read, no Gunicorn claim made.

### Source register

Note: the fetch tool returned condensed renderings of pages; quotes below are as returned, not byte-verified against the originals.

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| RT-S01 | T1 | HTML Living Standard, Server-sent events | WHATWG | https://html.spec.whatwg.org/multipage/server-sent-events.html | EventSource, reconnection, Last-Event-ID, keep-alive comment, GET only |
| RT-S02 | T1 | RFC 6455, The WebSocket Protocol | IETF | https://www.rfc-editor.org/rfc/rfc6455 | WebSocket rationale, origin model, masking, per-IP connection serialization |
| RT-S03 | T1 | RFC 6202, Known Issues and Best Practices for Bidirectional HTTP (Informational RFC) | IETF | https://www.rfc-editor.org/rfc/rfc6202 | polling, long polling, streaming: issues, timeouts, DoS |
| RT-S04 | T1 | PostgreSQL docs, NOTIFY | PostgreSQL | https://www.postgresql.org/docs/current/sql-notify.html | payload limit, queue, ordering, dedup, commit-time delivery |
| RT-S05 | T1 | PostgreSQL docs, LISTEN | PostgreSQL | https://www.postgresql.org/docs/current/sql-listen.html | session scope, race at setup, recommended pattern |
| RT-S06 | T1 | MDN, Using server-sent events | Mozilla | https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events | 6-connection limit, HTTP/2 100 streams, one-way |
| RT-S07 | T1 | MDN, WebSocket API | Mozilla | https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API | two-way sessions, no backpressure, WebSocketStream |
| RT-S08 | T1 | NGINX, WebSocket proxying | NGINX | https://nginx.org/en/docs/http/websocket.html | hop-by-hop Upgrade headers, 60 s idle close, ping frames |
| RT-S09 | T1 | NGINX, ngx_http_proxy_module | NGINX | https://nginx.org/en/docs/http/ngx_http_proxy_module.html | proxy_buffering, X-Accel-Buffering, proxy_read_timeout |
| RT-S10 | T1 | RFC 9113, HTTP/2 (section 6.5.2 only) | IETF | https://www.rfc-editor.org/rfc/rfc9113 | SETTINGS_MAX_CONCURRENT_STREAMS recommended minimum 100 |
| RT-S11 | T1 | RFC 8441, Bootstrapping WebSockets with HTTP/2 | IETF | https://www.rfc-editor.org/rfc/rfc8441 | extended CONNECT, opt-in setting |
| RT-S12 | T1 | Django docs, Asynchronous support | Django | https://docs.djangoproject.com/en/stable/topics/async/ | ASGI vs WSGI, async DB constraints |
| RT-S13 | T1 | Django docs, Request and response objects (StreamingHttpResponse) | Django | https://docs.djangoproject.com/en/stable/ref/request-response/ | streaming under WSGI vs ASGI |
| RT-S14 | T1 | Django Channels docs, Channel layers | Django | https://channels.readthedocs.io/en/stable/topics/channel_layers.html | cross-process messaging, official backend |
| RT-S15 | T1 | ASGI specification, HTTP and WebSocket | ASGI | https://asgi.readthedocs.io/en/latest/specs/www.html | connection scope lifetime for sockets and long polls |
| RT-S16 | T1 | FastAPI docs, WebSockets | FastAPI | https://fastapi.tiangolo.com/advanced/websockets/ | in-memory broadcast limited to one process |
| RT-S17 | T1 | OWASP WebSocket Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html | wss, Origin, tokens, limits |
| RT-S18 | T1 | PgBouncer docs, Features | PgBouncer | https://www.pgbouncer.org/features.html | LISTEN incompatible with transaction pooling |
| RT-S19 | T3 | htmx docs | htmx maintainers | https://htmx.org/docs/ | polling via hx-trigger, SSE and WebSocket as extensions |
| RT-S20 | T3 | AWS docs, ALB attributes | AWS | https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-load-balancer-attributes.html | idle timeout 60 s, app timeout above LB, HTTP/2 PING not counted |
| RT-S21 | T3 | Heroku Dev Center, HTTP routing | Heroku | https://devcenter.heroku.com/articles/http-routing | 30 s first byte, 55 s rolling idle window, WebSocket support |
| RT-S22 | T3 | Railway guides, Choose between SSE and WebSockets | Railway | https://docs.railway.com/guides/sse-vs-websockets | decision criteria, platform idle limits |
| RT-S23 | T3 | Postgres LISTEN/NOTIFY does not scale (postmortem) | Recall.ai engineering | https://www.recall.ai/blog/postgres-listen-notify-does-not-scale | commit-time global lock under load |
| RT-S24 | T3 | PgDog docs, pub/sub in transaction mode | PgDog | https://docs.pgdog.dev/features/connection-pooler/pub_sub/ | NOTIFY at-most-once through a pooler |
| RT-S25 | T4 | WebSocket vs SSE | Ably (commercial real-time vendor, author is its CEO) | https://websocket.org/comparisons/sse/ | the WebSocket-first side of the debate; vendor bias |

Also read via search result summaries only (not cited as grounds): general SSE-vs-WebSocket guides, a pg-listen note on one listener connection per process.

### Claims

Format: id | claim | level | stack | sources | agreement | positions | certainty.

- RT-C01 | Choose the channel from the direction of data flow, update frequency and tolerable latency, and take the simplest one that meets the need: polling, then long polling or SSE for server-to-client push, then WebSocket for two-way traffic. | principle | neutral | S03, S22, S25 | majority | the criteria agree across S22 and S25; the order "simplest first" is stated by S22 only | inferred (synthesis of S03 definitions and S22, S25 criteria)
- RT-C02 | Short polling suits infrequent updates and second-scale latency; each poll carries full HTTP headers and most polls return nothing, so cost grows with clients times frequency. | decision | http | S03, S19 | consensus | - | grounded
- RT-C03 | Long polling (server answers only on an event or timeout) cuts latency and waste against short polling but has a worst-case latency of three network transits and per-message header overhead; use a timeout around 30 seconds. | decision | http | S03 | consensus | - | grounded
- RT-C04 | Long-poll and streaming responses must not be cached (Cache-Control: no-cache); the SSE client itself uses cache mode no-store. | practice | http | S03, S01 | consensus | - | grounded
- RT-C05 | Use SSE when only the server pushes: it runs over ordinary HTTP, is GET-only, text-only, cannot send custom headers, and the client cannot send events back on it. | decision | http | S01, S06, S22 | consensus | - | grounded
- RT-C06 | SSE resume works through the event id field and the Last-Event-ID request header; the server may tune reconnect delay with the retry field. | practice | http | S01, S06 | consensus | - | grounded
- RT-C07 | Resume only closes the gap if the server can replay events after a given id (a log or a table to read from); otherwise the client must reload state on reconnect. | practice | neutral | S01, S06 | consensus | - | inferred (the spec defines the header, not the replay store)
- RT-C08 | Send an SSE comment line about every 15 seconds so proxies do not time out an idle stream. | practice | http | S01 | consensus | - | grounded
- RT-C09 | Under HTTP/1.1 SSE is capped at 6 connections per browser and domain across all tabs; prefer HTTP/2 (stream limit negotiated, default 100, recommended minimum 100) or one stream per tab shared via a shared worker. | practice | http | S06, S01, S10 | consensus | - | grounded
- RT-C10 | Use WebSocket when both sides send frequently or low latency matters: one persistent TCP connection replaces repeated HTTP requests and their header overhead. | decision | http | S02, S07, S22 | consensus | - | grounded
- RT-C11 | Proxying WebSocket through nginx requires setting the hop-by-hop Upgrade and Connection headers explicitly; some proxies and load balancers do not support the upgrade, so verify the whole chain. | practice | http | S08, S22 | consensus | - | grounded (the "verify the chain" part is S22)
- RT-C12 | WebSocket over HTTP/2 requires extended CONNECT (RFC 8441), enabled by an opt-in server setting; where any hop lacks it, WebSocket runs on an HTTP/1.1 connection. | practice | http | S11 | consensus | - | grounded (fallback sentence inferred)
- RT-C13 | Every hop closes idle connections (nginx 60 s default, ALB 60 s default, Heroku 55 s rolling window): send heartbeats (SSE comment, WebSocket ping) under the shortest timeout, and set the application idle timeout above the load balancer's to avoid 502s. | practice | http | S08, S09, S20, S21 | consensus | ALB does not count HTTP/2 PING frames as activity (S20) | grounded
- RT-C14 | Turn off response buffering for streaming endpoints on the reverse proxy (proxy_buffering off or the X-Accel-Buffering: no response header), otherwise events arrive in batches. | practice | http | S09, S25 | consensus | - | grounded
- RT-C15 | The default channel for server-to-client push is contested: SSE first, or WebSocket first. | decision | http | S22, S25, S01, S06, S08 | contested | SSE-first: simpler, plain HTTP, auto reconnect and resume, enough for notifications, dashboards, token streaming (S22; T3). WebSocket-first: SSE can be silently buffered by corporate proxies, firewalls and some CDNs, so it works in development and batches in production; one bidirectional channel (S25; T4, vendor with a commercial interest). Fits: SSE-first when the path to the user is under your control and traffic is one-way; WebSocket when intermediaries are unknown or traffic is two-way. | grounded as a debate; the buffering claim for SSE has one vendor source
- RT-C16 | The browser WebSocket API has no backpressure: messages arriving faster than the app can process fill memory or CPU; bound message size and rate, or use WebSocketStream where available. | practice | js | S07, S17 | consensus | - | grounded
- RT-C17 | WebSocket has no built-in reconnect or resume: the client needs a reconnection wrapper with exponential backoff and a way to resync state. | practice | js | S22, S01 | consensus | SSE spec says a user agent may apply backoff | grounded
- RT-C18 | A connection is disposable state held by one process: keep truth and durable state in backing services, and design the client to reconnect, land on any process, and resync. This fits stateless processes (APP-C26, C27) with the connection as the one tolerated exception. | principle | neutral | S15, S16, S14 | majority | no source states the reconciliation; sources agree that connection scope lives and dies with the process | inferred (S15 scope lifetime, S16 limitation, round-1 APP-C26/C27) | boundary: APP
- RT-C19 | Long-lived connections (SSE, WebSocket, long polling) need an ASGI server; under WSGI a streaming response ties up a worker for its whole duration, and async views under WSGI lose the async benefit. | decision | python | S13, S12, S15 | consensus | - | grounded
- RT-C20 | An in-process list of connected clients works only inside one process; with more than one process, fan-out needs a shared layer. | practice | python | S16, S14 | consensus | - | grounded
- RT-C21 | For cross-process fan-out in Django, use a channel layer backed by Redis (the only official production backend); the in-memory layer is for tests and has no cross-process messaging. FastAPI points to a broker-backed helper (Redis, PostgreSQL) for the same need. | decision | python | S14, S16 | consensus | - | grounded
- RT-C22 | In Django's async mode, persistent database connections are not supported (CONN_MAX_AGE 0) and ORM calls run through sync_to_async in a thread; real-time handlers should keep database work short and out of the connection's lifetime. | practice | python | S12 | consensus | - | grounded (condensed fetch; not byte-verified)
- RT-C23 | Never hold a database connection or transaction per connected client; the count of real-time clients (thousands) must stay independent of the small server-side pool (DATA-C36). | principle | postgres | S12, S18 | consensus | - | inferred (from S12 and round-1 DATA-C36, C37) | boundary: DATA
- RT-C24 | Run long-lived connection handling as its own process type or service, apart from short-request workers, so sockets cannot starve page requests and each type scales separately. | practice | python | S13, S12 | majority | S13 only says WSGI streaming "may result in poor performance" and to do expensive work outside the request cycle | inferred (S13 plus round-1 APP-C28) | boundary: runtime topology
- RT-C25 | Deploys, restarts and keep-alive limits drop all connections at once; clients should reconnect with backoff and random jitter to avoid a reconnect storm. | practice | neutral | S01, S20, S22 | majority | S01 and S22 mention backoff; jitter is not in the sources | inferred
- RT-C26 | WebSocket security: use wss only, validate Origin against an explicit allowlist (cross-site WebSocket hijacking), keep tokens out of URLs (they leak into logs), disable compression unless needed, treat all messages as untrusted input. | practice | http | S17, S02 | consensus | the protocol's origin model protects browsers only, not other clients (S02) | grounded | boundary: SEC
- RT-C27 | Authorize each action on a long-lived connection, not once at connect, and close connections when the session expires or the user logs out. | practice | neutral | S17 | consensus | - | grounded | boundary: SEC
- RT-C28 | Long-lived connections widen denial-of-service exposure; cap message size, message rate and connections per client. | practice | http | S03, S17, S02 | consensus | - | grounded | boundary: rate limiting and abuse
- RT-C29 | Use LISTEN/NOTIFY as a signal from the database to application processes ("something changed"), not as a message store: payload under 8000 bytes, nothing persisted, delivery only to sessions listening at that moment, delivered at commit, in commit order. | decision | postgres | S04, S05 | consensus | - | grounded
- RT-C30 | Put an identifier or hint in the payload and have the consumer re-read state from tables; on (re)connect run LISTEN and commit it, then read current state, then rely on notifications. | practice | postgres | S05, S04 | consensus | - | grounded
- RT-C31 | Do not use NOTIFY as a counter or event log: identical channel and payload within one transaction collapse to one delivery. | practice | postgres | S04 | consensus | - | grounded
- RT-C32 | LISTEN needs a session-level connection: it does not work through a transaction-pooling pooler; use a direct connection (one per application process, which then fans out in memory or via Redis) or a pooler that explicitly supports it. | practice | postgres | S18, S05, S24 | consensus | - | grounded | boundary: DATA (restates DATA-C37 for this use)
- RT-C33 | A listening session that stays in a long transaction blocks queue cleanup; the queue is 8 GB by default, warnings begin at half full, and when it is full NOTIFY transactions fail at commit. Keep listener connections outside transactions and watch queue usage. | practice | postgres | S04 | consensus | - | grounded (monitoring advice inferred)
- RT-C34 | NOTIFY has a scaling ceiling under write concurrency: because commit order must be preserved, a transaction that issued NOTIFY takes a global lock during commit, serializing commits; one production postmortem (March 2025) saw throughput collapse while CPU and I/O fell, and fixed it by moving the logic to the application layer. | decision | postgres | S23, S04 | contested | Use NOTIFY: fine at low write rates, no extra infrastructure (S04 describes it as ordinary feature, with no scale warning). Avoid at high concurrency: S23, a single T3 account; the lock itself was read from source code by that author, not from the docs. Thresholds unknown. | grounded for the incident; open for thresholds and for versions affected
- RT-C35 | NOTIFY is at-most-once (lost if no one is listening or the connection breaks); when events must not be lost, write them to a table (outbox) and use NOTIFY or polling only to wake the reader. | decision | postgres | S04, S05, S24 | consensus | - | inferred (S04, S05 imply loss for non-listeners; S24 states at-most-once for its pooler)
- RT-C36 | For a classic site on JS, Python and Postgres, a defensible default order is: no real-time; polling for slow-changing views; SSE for one-way push; WebSocket only for true two-way needs; with Postgres NOTIFY as the wake-up signal and a Redis layer only when more than one process must fan out. | decision | python | S01, S13, S14, S19, S22, S04 | majority | rests on RT-C15 (contested) and RT-C34 (contested) | inferred
- RT-C37 | Treat real-time as an enhancement on top of a working request-response page: the page must be correct on plain load, and push only reduces staleness. | principle | neutral | S19 | majority | one T3 source (htmx keeps SSE and WebSocket optional extensions); fits round-1 progressive enhancement (UI-C01) | inferred
- RT-C38 | Polling needs no server-side connection state and works under any process model, including sync WSGI workers; the server can end polling with a status code once done. | practice | http | S19, S03 | consensus | - | grounded

Level counts: principle 4, decision 11, practice 23.

### Gaps (open)

- Build vs buy of a managed real-time service: not researched.
- NOTIFY ceiling thresholds and affected versions: one source, no numbers from the PostgreSQL docs.
- Connections per process, memory per connection: no T1 or T2 source read.
- Gunicorn worker behavior with long-lived connections: T1 page not reachable.
- Collaborative-editing concerns (presence, ordering, conflicts): out of scope at decision level.
- Corporate-proxy buffering of SSE: only the vendor source (S25) asserts it; no neutral measurement found.
