# TOPO: runtime topology of the three tiers (round 2)

## L1 headline

Best practice for the runtime shape of a browser + Python + Postgres site is settled and well documented at T1: a reverse proxy is the single public entry that terminates TLS (HTTPS site-wide, HSTS staged), a WSGI or ASGI server runs as supervised pre-fork worker processes behind it, static files are served by the proxy or a CDN and not by Python, background workers are a second process type of the same release, and containers are ephemeral one-concern units. Certainty: grounded for the proxy, TLS, HSTS, worker-model and process-supervision claims; inferred for the single-origin default, worker placement and CDN adoption thresholds; open for worker-count evidence and proxy-to-app encryption across a network hop.

Pinned:
- Sources: 29 read (T1 22, T2 5, T3 2, T4 0).
- Claims: 45 (principle 7, decision 11, practice 27).
- Contested: ASGI process supervision model (gunicorn workers vs uvicorn --workers vs orchestrator replicas); replication location in containers (in-container workers vs one process per container).
- Failed fetches: none on T1 (docs.gunicorn.org moved, read at its new address); one T3 failed: Mozilla Server Side TLS wiki is now a stub, and the successor page read gave no version or cipher detail.

## L2 claims

Pinned (same block, word for word):
- Sources: 29 read (T1 22, T2 5, T3 2, T4 0).
- Claims: 45 (principle 7, decision 11, practice 27).
- Contested: ASGI process supervision model (gunicorn workers vs uvicorn --workers vs orchestrator replicas); replication location in containers (in-container workers vs one process per container).
- Failed fetches: none on T1 (docs.gunicorn.org moved, read at its new address); one T3 failed: Mozilla Server Side TLS wiki is now a stub, and the successor page read gave no version or cipher detail.

Clusters (claim, agreement, certainty, ids):

1. The Python server never faces the internet: a reverse proxy is the single public entry, buffers slow clients, forwards the original Host and scheme, and the app trusts forwarded headers only from it. Consensus on buffering and trust, majority on "one proxy for every stack" (ASGI servers can be exposed, docs advise against). Grounded. TOPO-C01 to C09.
2. HTTPS is site-wide, terminated at the proxy or edge, with a permanent redirect from HTTP, automated certificates, TLS 1.3 (1.2 for compatibility), Secure cookies and no mixed content. Consensus, grounded (TLS-version claim rests on one T1 source). C10 to C16.
3. HSTS is sent over HTTPS only, does not protect the first visit, and its includeSubDomains and preload options are near-irreversible, so adopt it in stages. Consensus, grounded (staging itself inferred). C17 to C19.
4. Pick WSGI (default, sync) or ASGI (long-lived connections, async) by need; the dev server is never production; the app server runs as a pre-fork master plus workers started at boot and restarted by an external supervisor. Consensus, grounded. C20, C21, C22, C24, C27, C28, C29.
5. Worker sizing: start at (2 x cores) + 1 for sync workers, memory is per process times workers, target 50 to 90 percent resource use, tune by measurement. Majority (two T1 sources, no empirical study), grounded. C25, C26.
6. ASGI process supervision has three live shapes. Contested, grounded. C23, C43.
7. Static assets: collectstatic at build, then served by the proxy, a dedicated server, or object storage plus CDN, not by Python workers; WhiteNoise is acceptable behind a CDN. Majority (options by context), grounded. C30 to C32.
8. A CDN is an optional layer added for latency and origin offload; it takes long TTLs on fingerprinted assets, seconds-long micro-caching on dynamic responses, a 90 percent hit-ratio goal. Consensus on role, grounded (single T1 source); adoption threshold inferred. C33 to C35.
9. Default to one origin (one hostname, path routing at the proxy); a second origin needs explicit CORS and isolates browser storage. Majority, inferred from T1 mechanics. C36, C37.
10. Background workers are a second process type of the same codebase, release and config, run under a supervisor as an unprivileged user; whether they sit on the web host or scale separately is a decision. Consensus on the principle, inferred on placement. C38 to C41.
11. Containers are ephemeral, one concern each, built with multi-stage builds, non-root user and pinned bases; the proxy-headers trust setting is needed behind a TLS proxy. Consensus, grounded. C42, C44, C45.

Live debates:
- Supervision of ASGI servers: Uvicorn docs advise gunicorn with UvicornWorker and also support --workers; FastAPI docs prefer one process per container with orchestrator replicas; Gunicorn design is pre-fork inside one unit (C23, C43).
- Static serving location: proxy on the same host, dedicated server or CDN, or WhiteNoise in the app; all documented, chosen by hosting model (C30).

Not covered: re-encryption between proxy and app across a network hop, HTTP/2 and HTTP/3 termination details, certificate pinning and CAA, load-balancer health checks, zero-downtime restart procedure, empirical worker-count studies, Kubernetes and PaaS specifics, scheduled jobs (deferred), HA and replication (deferred), uploads and media (sibling area), rate limiting (sibling area), Mozilla TLS profiles (source unreadable).

## L3 full

Pinned (same block, word for word):
- Sources: 29 read (T1 22, T2 5, T3 2, T4 0).
- Claims: 45 (principle 7, decision 11, practice 27).
- Contested: ASGI process supervision model (gunicorn workers vs uvicorn --workers vs orchestrator replicas); replication location in containers (in-container workers vs one process per container).
- Failed fetches: none on T1 (docs.gunicorn.org moved, read at its new address); one T3 failed: Mozilla Server Side TLS wiki is now a stub, and the successor page read gave no version or cipher detail.

Method note: pages were fetched through a summarizing reader, so quotes are as returned by it; claims marked grounded rest on those passages. Where tool docs (nginx, Gunicorn, Uvicorn, Docker, Celery) are cited as T1, that follows the round-1 coverage check, which named them T1 for this area.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| TOPO-S01 | T1 | Deployment checklist | Django | docs.djangoproject.com/en/stable/howto/deployment/checklist/ | HTTPS redirect, secure cookies, ALLOWED_HOSTS, DEBUG, static root |
| TOPO-S02 | T1 | How to deploy Django (index) | Django | docs.djangoproject.com/en/stable/howto/deployment/ | WSGI and ASGI server lists, runserver unsuitable |
| TOPO-S03 | T1 | How to deploy with ASGI | Django | docs.djangoproject.com/en/stable/howto/deployment/asgi/ | ASGI servers, async-safety |
| TOPO-S04 | T1 | Settings reference (SECURE_PROXY_SSL_HEADER, SECURE_SSL_REDIRECT, SECURE_HSTS_*) | Django | docs.djangoproject.com/en/stable/ref/settings/ | proxy scheme, HSTS settings and warnings |
| TOPO-S05 | T1 | Deploying static files | Django | docs.djangoproject.com/en/stable/howto/static-files/deployment/ | collectstatic, same server, dedicated server, CDN |
| TOPO-S06 | T1 | How to use Django with Gunicorn | Django | docs.djangoproject.com/en/stable/howto/deployment/wsgi/gunicorn/ | invocation only (page thin) |
| TOPO-S07 | T1 | Design (Gunicorn) | Gunicorn project | gunicorn.org/design/ | pre-fork model, sync workers, slow clients, worker count |
| TOPO-S08 | T1 | Deploying Gunicorn | Gunicorn project | gunicorn.org/deploy/ | nginx in front, buffering, forwarded-allow-ips, systemd |
| TOPO-S09 | T1 | Deployment | Uvicorn project | uvicorn.dev/deployment/ | production layering, workers, proxy headers, unix socket |
| TOPO-S10 | T1 | Deployment concepts | FastAPI | fastapi.tiangolo.com/deployment/concepts/ | TLS proxy, restarts, replication, memory, previous steps |
| TOPO-S11 | T1 | FastAPI in containers | FastAPI | fastapi.tiangolo.com/deployment/docker/ | one process per container, proxy headers |
| TOPO-S12 | T1 | ngx_http_proxy_module | nginx | nginx.org/en/docs/http/ngx_http_proxy_module.html | buffering, Host header, timeouts |
| TOPO-S13 | T1 | NGINX reverse proxy | nginx | docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/ | reverse proxy duties |
| TOPO-S14 | T1 | Strict-Transport-Security | MDN | developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security | HSTS directives, preload, first visit |
| TOPO-S15 | T1 | RFC 6797 HTTP Strict Transport Security | IETF | rfc-editor.org/rfc/rfc6797.html | HSTS normative rules (7.2, 6.1, 14.6) |
| TOPO-S16 | T1 | RFC 7239 Forwarded HTTP Extension | IETF | rfc-editor.org/rfc/rfc7239.html | proxy-disclosed info, spoofing, trust |
| TOPO-S17 | T1 | Transport Layer Security Cheat Sheet | OWASP | cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html | TLS for all pages, versions, redirect, mixed content |
| TOPO-S18 | T1 | Why HTTPS matters | web.dev | web.dev/articles/why-https-matters | site-wide HTTPS rationale |
| TOPO-S19 | T1 | Content delivery networks | web.dev | web.dev/articles/content-delivery-networks | CDN role, TTLs, compression, hit ratio |
| TOPO-S20 | T1 | Building best practices | Docker | docs.docker.com/build/building/best-practices/ | ephemeral, one concern, multi-stage, USER, pinning |
| TOPO-S21 | T1 | Daemonization | Celery | docs.celeryq.dev/en/stable/userguide/daemonizing.html | worker supervision, no root |
| TOPO-S22 | T1 | Same-origin policy | MDN | developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy | origin definition, CORS, isolated storage |
| TOPO-S23 | T2 | ASGI introduction | ASGI project | asgi.readthedocs.io/en/latest/introduction.html | why ASGI, WSGI limits, superset relation |
| TOPO-S24 | T2 | IV. Port binding | Twelve-Factor App | 12factor.net/port-binding | self-contained app, routing layer |
| TOPO-S25 | T2 | VIII. Concurrency | Twelve-Factor App | 12factor.net/concurrency | process types, no daemonizing, process manager |
| TOPO-S26 | T2 | IX. Disposability | Twelve-Factor App | 12factor.net/disposability | fast start, graceful shutdown |
| TOPO-S27 | T2 | XII. Admin processes | Twelve-Factor App | 12factor.net/admin-processes | one-off tasks in same release and environment |
| TOPO-S28 | T3 | Frequently asked questions | Let's Encrypt | letsencrypt.org/docs/faq/ | certificate validity, renewal cadence, automation |
| TOPO-S29 | T3 | WhiteNoise documentation | WhiteNoise maintainers | whitenoise.readthedocs.io/en/latest/ | static serving from the app behind a CDN |

Not read (failed): Mozilla Server Side TLS wiki page (T3) now a redirect stub; tlsref.org successor page gave no profile detail. Not counted in the register.

### Claims

Cluster 1: proxy and entry

- **TOPO-C01** | principle | http | S07 (Buffering proxy), S08, S24 (Routing layer), S09 | consensus | grounded. The application server should not face the public internet directly; a reverse proxy or routing layer sits in front and maps the public hostname to the app's bound port.
- **TOPO-C02** | decision | http | S07, S08 (nginx recommended), S09 (nginx layer, then CDN), S10, S13 | majority | grounded. Use one reverse proxy (nginx, Caddy, Traefik, HAProxy or a cloud load balancer) as the single public entry. Positions: Gunicorn docs require it for sync workers; Uvicorn docs list the proxy as an optional second layer and can serve TLS itself; Twelve-Factor needs a routing layer but does not name a proxy. Applies as stated for any WSGI deployment; for ASGI it is advice, not a requirement.
- **TOPO-C03** | practice | http | S07, S08 ("you must ensure the proxy buffers slow clients"), S12 (proxy_buffering on by default; request buffering) | consensus | grounded. The proxy should buffer both the client request and the upstream response, so slow clients do not hold a worker; without it, sync workers are open to trickle-style denial of service.
- **TOPO-C04** | practice | http | S08 (proxy_buffering off for streaming), S12 | majority | grounded. Turn proxy buffering off only on routes that stream (SSE, long polling, streaming bodies), and serve those from async-capable workers. Single T1 source for the streaming advice; no dissent. boundary: real-time channels.
- **TOPO-C05** | practice | http | S12 (Host and Connection are redefined by default; use $host), S08 (X-Forwarded-Proto), S04 | consensus | grounded. The proxy should pass the original Host and the original scheme to the app, because nginx by default replaces Host and the app cannot see HTTPS otherwise.
- **TOPO-C06** | practice | http | S08 (forwarded-allow-ips, "dangerous if untrusted clients can reach Gunicorn directly"), S09 ("Only trust clients you can actually trust"), S16 (header "cannot be relied upon") | consensus | grounded. The app server should honor X-Forwarded-* or Forwarded headers only from the proxy's address, and must not be reachable by clients except through the proxy.
- **TOPO-C07** | practice | python | S04 (SECURE_PROXY_SSL_HEADER; is_secure, CSRF), S16 | consensus | grounded (the rule that the proxy must overwrite any client-sent copy of the header is inferred from S16). Configure the framework to read the request scheme from the proxy header, so that is_secure and CSRF checks see HTTPS.
- **TOPO-C08** | practice | python | S01 (ALLOWED_HOSTS: "also configure the web server ... to validate the host") | consensus | grounded. Validate the Host header at two layers: the proxy's server names and the framework's allowed-hosts list; with debug off Django does not run without it.
- **TOPO-C09** | practice | http | S09 ("UNIX domain socket between Nginx and ... the process manager"), S08 (unix-socket test) | majority | grounded. When proxy and app server share a host, connect them over a unix domain socket. Single-source performance and isolation advice, no dissent. Re-encryption across a network hop: open, see gaps.

Cluster 2: HTTPS and TLS

- **TOPO-C10** | principle | http | S01 ("any website which allows users to log in should enforce site-wide HTTPS"), S17 ("all pages, not just ... login"), S18 ("always protect all your websites") | consensus | grounded. Serve the whole site over HTTPS, not only sensitive pages.
- **TOPO-C11** | decision | http | S10 ("normally provided by a component external ... a TLS Termination Proxy"), S11, S09 (also offers --ssl-keyfile), S24 | majority | grounded. Terminate TLS at the proxy or edge, not in the Python server. Positions: FastAPI docs say external is normal, naming Traefik, Caddy, nginx plus Certbot, HAProxy, ingress, cloud services; Uvicorn documents direct certificate options without recommending them for a layered production setup.
- **TOPO-C12** | practice | http | S01 ("web server must redirect all HTTP traffic to HTTPS, and only transmit HTTPS requests to Django"), S15 (7.2, 301), S17, S14 | consensus | grounded. Redirect HTTP to HTTPS with a permanent redirect at the proxy and forward only HTTPS-originated requests to the app.
- **TOPO-C13** | practice | http | S10 (Traefik and Caddy renew automatically), S28 (renew at 60 of 90 days, automate, random time) | majority | grounded. Automate certificate issuance and renewal; renew about two-thirds into the validity period; prefer a proxy that does it itself or a tested ACME client. Two sources, one T3.
- **TOPO-C14** | practice | http | S17 (default TLS 1.3, 1.2 for compatibility; 1.0 and 1.1 disabled per RFC 8996) | majority | grounded. Enable TLS 1.3, keep 1.2 only for compatibility, disable older versions. Single T1 source read; Mozilla profiles unreadable.
- **TOPO-C15** | practice | http | S17 (Secure attribute; mixed content), S01 (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE) | consensus | grounded. Mark session and CSRF cookies Secure and load no subresource over HTTP. boundary: identity and security.
- **TOPO-C16** | principle | http | S18 (powerful features require HTTPS) | consensus | grounded. Treat HTTPS as a precondition for modern browser capabilities (geolocation, media capture, service workers), not as an add-on.

Cluster 3: HSTS

- **TOPO-C17** | practice | http | S14 (header ignored over HTTP), S15 (7.2: MUST NOT include over non-secure transport) | consensus | grounded. Send Strict-Transport-Security on HTTPS responses only, with max-age set; ignore it on HTTP responses.
- **TOPO-C18** | decision | http | S04 (HSTS "can irreversibly (for some time) break your site"), S14 (preload needs 1 year, includeSubDomains; "permanent and difficult to remove") | consensus | grounded for the risk; the staged ramp is inferred. Treat HSTS scope as a commitment: add includeSubDomains and preload only after every subdomain serves HTTPS, and raise max-age in steps.
- **TOPO-C19** | principle | http | S14 (first-visit weakness), S15 (14.6 bootstrap MITM) | consensus | grounded. HSTS does not protect the first request to a host; only the browser preload list closes that gap, so keep the HTTP-to-HTTPS redirect in place.

Cluster 4: server interface and process model

- **TOPO-C20** | decision | python | S23 (WSGI is "a single, synchronous callable ... doesn't allow for long-lived connections"; ASGI is a superset), S02, S03 | consensus | grounded. Run a WSGI server by default; choose ASGI when the app needs long-lived connections (WebSocket, long polling) or native async I/O. ASGI can host WSGI apps, so the choice is reversible. boundary: application tier (sync default), real-time channels.
- **TOPO-C21** | decision | python | S02 (WSGI: Granian, Gunicorn, uWSGI, mod_wsgi; ASGI: Daphne, Granian, Hypercorn, Uvicorn), S03 | consensus | grounded for the lists; the default is inferred. Choose a server from the framework's documented list; the docs rank none. Inferred default: Gunicorn for WSGI, Uvicorn for ASGI (the two with the most deployment documentation read here).
- **TOPO-C22** | principle | python | S02 (runserver "not suitable for production"), S01 (never enable debug) | consensus | grounded. The development server is never the production server.
- **TOPO-C23** | decision | python | S09 (gunicorn with UvicornWorker for production; also --workers with SIGHUP, SIGTTIN, SIGTTOU), S11 (single process per container; cluster-level replication), S07 (arbiter plus workers) | contested | grounded. Positions: (a) Gunicorn as process manager with Uvicorn workers, for self-hosted single servers (Uvicorn docs); (b) Uvicorn's own --workers supervisor, no pre-fork (Uvicorn docs); (c) one Uvicorn process per instance, replication by the orchestrator or platform (FastAPI docs, when a cluster exists). Choose by hosting model: single VM favors (a) or (b), orchestrated platform favors (c).
- **TOPO-C24** | practice | python | S07 (pre-fork: arbiter manages workers), S10 (only one process can listen on a port, so one parent hands off to workers) | consensus | grounded. Run the app server as a parent process that owns the listening socket plus several worker processes, so a worker crash is contained.
- **TOPO-C25** | practice | python | S07 ("(2 x CPU cores) + 1"; "Workers are not clients"; 4 to 12 workers usually enough) | majority | grounded. Start sync workers at (2 x cores) + 1, treat that as a starting point, and tune from measurement. Single T1 source, no empirical study; open.
- **TOPO-C26** | practice | neutral | S10 (each process has its own memory; N workers cost N times; target 50 to 90 percent utilization) | majority | grounded. Budget memory as per-process footprint times worker count, plus database connections per worker (see C25), and aim for 50 to 90 percent resource use, not 100. boundary: operations, data tier (connections).
- **TOPO-C27** | practice | python | S07 (sync assumes CPU- or network-bound, no keep-alive, needs buffering proxy; async for long blocking calls, streaming; threads share memory, workers isolate faults), S08 | consensus | grounded. Use sync workers behind a buffering proxy by default; move to threads or async workers for long blocking external calls or streaming, accepting less fault isolation from threads.
- **TOPO-C28** | principle | neutral | S25 (never daemonize; rely on process manager), S10 (start on boot, external restarter), S08 (systemd Type=notify), S21 | consensus | grounded. An external supervisor (systemd, container runtime, orchestrator, platform) starts the processes at boot and restarts them after a crash; the app does not daemonize or write PID files.
- **TOPO-C29** | practice | neutral | S10 ("single process to perform those previous steps"), S27 (one-off processes in same release) | consensus | grounded. Run one-time steps (migrations, collectstatic) once per release in a single process before the workers start (init container, release phase, or deploy script). boundary: operations.

Cluster 5: static files and CDN

- **TOPO-C30** | decision | http | S05 (same server; dedicated server "most larger Django sites"; cloud storage and CDN), S29 (WhiteNoise: PaaS, behind CDN) | majority | grounded. Serve static assets from the proxy on the app host, a dedicated static server, object storage plus CDN, or from the app via WhiteNoise behind a CDN. Positions: Django lists all three non-WhiteNoise options and says larger sites split; WhiteNoise docs favor in-app serving on PaaS. Choose by hosting model.
- **TOPO-C31** | practice | python | S05 (collectstatic, then serve STATIC_ROOT), S01 (define STATIC_ROOT in production) | consensus | grounded. Collect static files into one directory at build or release, and serve that directory with a static-capable server, not through Python request handlers (outside the WhiteNoise case).
- **TOPO-C32** | practice | python | S29 (CDN absorbs requests; two settings: CDN knows origin, app knows CDN URL) | majority | grounded. If WhiteNoise-style serving is used, put a CDN in front so most static requests never reach Python. Single T3 source.
- **TOPO-C33** | decision | http | S19 (shorter RTT, offload origin, "caches eliminate the need for a request to travel to the origin"), S05 | consensus on role | inferred for the adoption threshold. A CDN is an optional layer: add it when users are geographically distant or origin load justifies it; it is not needed for the first release of a single-region site.
- **TOPO-C34** | practice | http | S19 (static TTL 6 months to 1 year; dynamic cached for about 5 seconds under load; hit ratio goal 90 percent) | majority | grounded. At the CDN, cache fingerprinted static assets for the long term, consider seconds-long micro-caching of anonymous dynamic responses under load, and watch the hit ratio. Single T1 source. boundary: operations (cache headers duplicate round 1).
- **TOPO-C35** | practice | http | S19 ("all text-based responses should be compressed with gzip or Brotli") | majority | grounded. Compress text responses at the proxy or CDN. boundary: presentation.

Cluster 6: single origin

- **TOPO-C36** | decision | http | S22 (same origin = scheme, host, port; cross-origin reads blocked; CORS needed; storage isolated per origin), S05 (same-server option first) | majority | inferred. Default to one public origin: the proxy routes page, API and static paths by prefix on one hostname, one certificate, one HSTS scope. Positions: single origin avoids CORS and storage isolation (implied by S22); a separate static or CDN host is common and harmless for non-credentialed assets (S05, S19). No source states the default; it is synthesis.
- **TOPO-C37** | practice | http | S22 (CORS lets servers name hosts allowed to read) | consensus | grounded. If a second origin must read responses (API host, separate front-end), grant access through an explicit CORS allow-list, never a wildcard on credentialed routes (the wildcard rule is inferred). boundary: contract, identity and security.

Cluster 7: background workers

- **TOPO-C38** | principle | neutral | S25 ("HTTP requests ... web process; long-running background tasks ... worker process"; adding concurrency is "simple and reliable"), S27 | consensus | grounded. Web and background workers are different process types of the same codebase, release and configuration, scaled independently. boundary: application tier (queue mechanics).
- **TOPO-C39** | practice | python | S21 (workers run as unprivileged user, never root; pickle risk; systemd or supervisor) | consensus | grounded. Run workers under a supervisor as an unprivileged account.
- **TOPO-C40** | decision | neutral | S25, S20 (one concern per container), S11 | majority | inferred. Place workers either as extra units on the web host (systemd units, compose services) or as separately scaled containers or services. Positions: single host, same image and unit file style, simplest; separate scaling pays when job load differs from web load. Neither is endorsed by a source; synthesis.
- **TOPO-C41** | practice | neutral | S27 (admin tasks "identical environment", same codebase and config; ship with the app) | consensus | grounded. Workers and one-off admin commands run from the same release image or checkout and the same config as the web processes.

Cluster 8: containers at architecture level

- **TOPO-C42** | principle | neutral | S20 ("as ephemeral as possible"; "each container should have only one concern"; one process per container as rule of thumb) | consensus | grounded. Containers are disposable and hold one concern each (web, worker, proxy, database as separate units).
- **TOPO-C43** | decision | neutral | S11 (cluster: replicate at cluster level; special cases: simple single-server app, Docker Compose), S09, S07 | contested | grounded. Positions: replicate at the orchestrator, one server process per container (FastAPI docs, Docker rule of thumb); keep a worker manager inside the container for a single server or Compose (FastAPI docs' own exceptions; Gunicorn and Uvicorn designs). Choose by whether an orchestrator exists.
- **TOPO-C44** | practice | neutral | S20 (multi-stage builds, USER non-root, pin base image to digest, .dockerignore) | consensus | grounded. Build images in stages, run as non-root, pin base images, and exclude non-build files from the context.
- **TOPO-C45** | practice | python | S11 (--proxy-headers behind a TLS proxy), S09 | consensus | grounded. Behind a TLS-terminating proxy, the containerized server must be told to trust the proxy's forwarded headers, subject to C06.

### Gaps (open)

- Proxy-to-app encryption across a network hop (different host or cluster): not read in any source; open.
- Empirical worker-count and thread-count evidence: only formulas from tool docs; open (round 1 asked for it).
- Mozilla TLS profiles (modern, intermediate): source moved, unreadable; TLS-version claim rests on OWASP alone.
- HTTP/2 and HTTP/3 at the proxy, zero-downtime restart and reload, health-check endpoints, graceful worker restarts under load: not read.
- Whether Postgres runs in a container, on the same host, or managed: not researched (data tier and HA deferred).
- Uploaded media and object storage topology: sibling area (file uploads). Rate limiting at the proxy: sibling area.
- Scheduled jobs and beat singleton rule: deferred by the brief.
- Django ASGI page does not list Gunicorn; Uvicorn docs recommend Gunicorn plus UvicornWorker. The two T1 pages disagree in emphasis; recorded under C23.
