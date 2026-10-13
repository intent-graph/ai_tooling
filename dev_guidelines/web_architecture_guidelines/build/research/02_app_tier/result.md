# APP research result: Application tier (Python server)

## L1 headline

Best practice for the Python application tier is well settled on principles (separate business logic from delivery and infrastructure, explicit short transaction boundaries, stateless disposable processes, config in the environment, side effects only after commit, idempotent jobs and retries) and genuinely open on three choices (how far to decouple the domain from the ORM, what backs the job queue, which framework); certainty is grounded for the 50 claims below but rests on official docs and recognized essays read through a fetch tool, with no first-hand reading of the books by Kleppmann, Nygard or Evans.

Pinned:
- Sources: 42 in total, by tier: T1 = 24, T2 = 15, T3 = 3, T4 = 0.
- Claims: 50 (principle 9, decision 13, practice 28, counted from the level field of each entry).
- Contested topics: domain-model decoupling from ORM (repository or not); job-queue backing store (database vs broker vs staged drain); framework choice (Django vs FastAPI vs Flask).
- Failed fetches on T1 sources: none. One T2 fetch failed (Cosmic Python epilogue, HTTP 404); its claims were taken from other chapters of the same book.

## L2 claims

Clusters (agreement, certainty, claim ids):

1. Keep business logic independent of delivery (HTTP) and infrastructure (DB, mail, payment); expose use cases through a service layer; handlers stay thin. Consensus, grounded. APP-C01, C02, C03, C06.
2. Layering depth scales with domain complexity: transaction script for simple logic, domain model when logic is complex; do not build an anemic model on a complex domain. Consensus, grounded. APP-C04, C05.
3. Start as one deployable (monolith) and split only on proven boundaries. Consensus among sources read (single T2 source plus Twelve-Factor), grounded. APP-C08.
4. A transaction is one explicit, short, use-case-sized unit; one session per thread or task; do not swallow exceptions inside it. Consensus on shortness and scope, majority on explicit-commit default. Grounded. APP-C09 to C14.
5. Side effects (email, enqueue, publish) happen after commit; never hold a transaction across remote calls. Consensus (the second part inferred). APP-C15, C16.
6. Dual writes (DB plus broker) are unsafe: use a transactional outbox or staged job drain, with at-least-once delivery and idempotent consumers. Consensus, grounded. APP-C17, C18.
7. Slow or non-essential work leaves the request cycle into worker processes via a task queue; jobs take ids not objects and are idempotent. Consensus, grounded. APP-C20 to C25.
8. Processes are stateless, share-nothing, horizontally scaled by process type, disposable, with backing services as swappable attached resources. Consensus, grounded. APP-C26 to C31.
9. Sync is the default; async only where in-process I/O concurrency pays; never block the event loop; async data access has hard constraints. Consensus, grounded. APP-C32 to C37.
10. ORM for routine mapping with a route to parameterized SQL; reads may bypass the domain model. Consensus on the first, majority on the second. Grounded. APP-C40 to C42.
11. Calls to external services: bounded backoff retries only for idempotent operations, retry at one layer, circuit breaking for persistent faults, idempotency keys for mutations. Consensus, grounded (idempotency keys single T3 source). APP-C43 to C46.
12. Config lives outside code, as independent environment variables, validated at startup; secrets never in source. Consensus on the principle, majority on granularity. Grounded. APP-C47 to C50.

Live debates:
- Decouple the domain model from the ORM with repositories (Cosmic Python) vs use the ORM models as the domain (Django Active Record, Fowler for simple cases): APP-C07.
- Job queue backing store: in-database with SKIP LOCKED (PostgreSQL docs allow it) vs external broker (Celery, FastAPI docs) vs staged drain (Brandur): APP-C19.
- Framework choice: no neutral T1/T2 source; each framework's own docs state its niche: APP-C38.
- Request-wide transaction (Django ATOMIC_REQUESTS) vs use-case transaction: majority for the latter, listed in APP-C11.

Not covered: books by Kleppmann (DDIA), Nygard (Release It!), Evans (DDD) not read; caching, rate limiting, WebSockets, file uploads and object storage, scheduled jobs (cron/beat), dependency-injection style, modular-monolith guidance, Django project-layout conventions, external connection poolers (DATA), worker-count tuning evidence (OPS).

## L3 full

Reading note: every page was fetched through a tool that returns an extracted excerpt, not the raw page; the two Flask design pages and the Flask Celery page came back verbatim. Quotes in claims are paraphrase unless in quotation marks. Agreement is relative to the sources read; where only one source was read the claim says "single source" in positions. Official docs of Django, FastAPI, Python and PostgreSQL are T1 per the brief; the docs of Flask, SQLAlchemy, Celery, Gunicorn and the ASGI spec are treated as T1 by extension (official docs of the tool concerned).

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| APP-S01 | T1 | Database transactions | Django | docs.djangoproject.com/en/stable/topics/db/transactions/ | autocommit, ATOMIC_REQUESTS, atomic(), on_commit |
| APP-S02 | T1 | Asynchronous support | Django | docs.djangoproject.com/en/stable/topics/async/ | async views, ORM async, transactions, connections in async |
| APP-S03 | T1 | Databases (pooling, persistent connections) | Django | docs.djangoproject.com/en/stable/ref/databases/ | pooling, CONN_MAX_AGE |
| APP-S04 | T1 | Tasks framework | Django | docs.djangoproject.com/en/stable/topics/tasks/ | background tasks API, on_commit enqueue |
| APP-S05 | T1 | Deployment checklist | Django | docs.djangoproject.com/en/stable/howto/deployment/checklist/ | production settings, secrets |
| APP-S06 | T1 | Design philosophies | Django | docs.djangoproject.com/en/stable/misc/design-philosophies/ | Django's architecture stance |
| APP-S07 | T1 | Performing raw SQL queries | Django | docs.djangoproject.com/en/stable/topics/db/sql/ | ORM escape hatch, parameters |
| APP-S08 | T1 | Concurrency and async / await | FastAPI | fastapi.tiangolo.com/async/ | def vs async def |
| APP-S09 | T1 | Background Tasks | FastAPI | fastapi.tiangolo.com/tutorial/background-tasks/ | in-process tasks vs queue |
| APP-S10 | T1 | Dependencies with yield | FastAPI | fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/ | resource lifecycle per request |
| APP-S11 | T1 | Settings and Environment Variables | FastAPI | fastapi.tiangolo.com/advanced/settings/ | typed settings, injection |
| APP-S12 | T1 | Deployment concepts | FastAPI | fastapi.tiangolo.com/deployment/concepts/ | processes, restarts, pre-start steps |
| APP-S13 | T1 | Bigger Applications | FastAPI | fastapi.tiangolo.com/tutorial/bigger-applications/ | module structure |
| APP-S14 | T1 | Session Basics | SQLAlchemy | docs.sqlalchemy.org/en/20/orm/session_basics.html | session and transaction lifecycle |
| APP-S15 | T1 | Asynchronous I/O (asyncio) extension | SQLAlchemy | docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html | async session constraints |
| APP-S16 | T1 | Overview (Core vs ORM) | SQLAlchemy | docs.sqlalchemy.org/en/20/intro.html | ORM philosophy |
| APP-S17 | T1 | Design Decisions in Flask | Pallets | flask.palletsprojects.com/en/stable/design/ | Flask scope |
| APP-S18 | T1 | Using async and await | Pallets (Flask) | flask.palletsprojects.com/en/stable/async-await/ | async in WSGI, performance |
| APP-S19 | T1 | Background Tasks with Celery | Pallets (Flask) | flask.palletsprojects.com/en/stable/patterns/celery/ | queue use, task arguments |
| APP-S20 | T1 | Developing with asyncio | Python | docs.python.org/3/library/asyncio-dev.html | blocking code, task references |
| APP-S21 | T1 | ASGI introduction | ASGI spec | asgi.readthedocs.io/en/latest/introduction.html | ASGI vs WSGI |
| APP-S22 | T1 | SELECT, locking clause | PostgreSQL | postgresql.org/docs/current/sql-select.html | SKIP LOCKED for queue-like tables |
| APP-S23 | T1 | Tasks, tips and best practices | Celery | docs.celeryq.dev/en/stable/userguide/tasks.html | job design |
| APP-S24 | T1 | Design | Gunicorn | gunicorn.org/design/ | worker types, proxy, worker count |
| APP-S25 | T2 | The Twelve-Factor App (index; factors III, IV, VI, VIII, IX, XII) | Wiggins / Heroku | 12factor.net/ and /config /processes /backing-services /concurrency /disposability /admin-processes | process and config model |
| APP-S26 | T2 | Hexagonal Architecture | Cockburn | alistair.cockburn.us/hexagonal-architecture/ | ports and adapters |
| APP-S27 | T2 | Service Layer (PoEAA) | Fowler | martinfowler.com/eaaCatalog/serviceLayer.html | service layer |
| APP-S28 | T2 | Unit of Work (PoEAA) | Fowler | martinfowler.com/eaaCatalog/unitOfWork.html | unit of work |
| APP-S29 | T2 | Monolith First | Fowler | martinfowler.com/bliki/MonolithFirst.html | starting architecture |
| APP-S30 | T2 | OrmHate | Fowler | martinfowler.com/bliki/OrmHate.html | ORM trade-offs |
| APP-S31 | T2 | Anemic Domain Model | Fowler | martinfowler.com/bliki/AnemicDomainModel.html | domain model vs services |
| APP-S32 | T2 | Transaction Script (PoEAA) | Fowler | martinfowler.com/eaaCatalog/transactionScript.html | simple-logic pattern |
| APP-S33 | T2 | Domain Model (PoEAA) | Fowler | martinfowler.com/eaaCatalog/domainModel.html | complex-logic pattern |
| APP-S34 | T2 | Repository (PoEAA) | Fowler | martinfowler.com/eaaCatalog/repository.html | repository |
| APP-S35 | T2 | Transactional outbox | Richardson, microservices.io | microservices.io/patterns/data/transactional-outbox.html | outbox |
| APP-S36 | T2 | Architecture Patterns with Python (preface, ch. 2, 4, 6, 12) | Percival and Gregory | cosmicpython.com/book/ (preface, chapter_02, 04, 06, 12) | layering in Python; epilogue returned 404 |
| APP-S37 | T2 | Retry pattern | Microsoft Azure Architecture Center | learn.microsoft.com/en-us/azure/architecture/patterns/retry | retries |
| APP-S38 | T2 | Circuit Breaker pattern | Microsoft Azure Architecture Center | learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker | circuit breaking |
| APP-S39 | T2 | Handling Overload (SRE book) | Google | sre.google/sre-book/handling-overload/ | retry budgets, one-layer retries |
| APP-S40 | T3 | Implementing Stripe-like Idempotency Keys in Postgres | Brandur Leach | brandur.org/idempotency-keys | idempotency, atomic phases |
| APP-S41 | T3 | Transactionally Staged Job Drains in Postgres | Brandur Leach | brandur.org/job-drain | enqueue and commit ordering |
| APP-S42 | T3 | Outbox Event Router | Debezium | debezium.io/documentation/reference/stable/transformations/outbox-event-router.html | dual-write problem (consumer dedup not confirmed on this page) |

Tier counts: T1 24, T2 15, T3 3, T4 0, total 42.

### Claims

Fields: level / stack / sources / agreement / certainty. `boundary` is given where relevant.

**Layering and use cases**

- APP-C01. Code on the inside (business logic) should not leak into the outside (UI, DB, external devices); the application should run in isolation with test adapters. level principle / stack neutral / S26, S36 (preface, ch.4) / consensus / grounded.
- APP-C02. Define application operations in a use-case (service) layer that every entry point (HTTP, CLI, jobs) calls, instead of encoding orchestration in each interface. decision / neutral / S27, S36 ch.4 / consensus / grounded. positions: S36 notes it adds a layer and may be unnecessary for web-only apps with controllers alone; see C04.
- APP-C03. HTTP handlers should be thin: parse input, call a use case, map outcomes to status codes. practice / neutral / S36 ch.4, S27 / consensus / grounded.
- APP-C04. Scale layering to domain complexity: use transaction script (or plain ORM/Active Record) for simple or CRUD logic; use a domain model plus use-case layer when logic is complex. decision / neutral / S32, S33, S31, S36 ch.2 / consensus / grounded. Note: S32 itself only points to PoEAA ch. 9 for the comparison; the threshold statement comes from S33, S31 and S36.
- APP-C05. Do not put all logic in services over data-only models in a complex domain (anemic model); keep the service layer thin around behavior-rich objects. principle / neutral / S31, S36 ch.4 / consensus / grounded.
- APP-C06. Reach every external system (database, mail, payment, third-party API) through an adapter behind an application-owned port so it can be replaced or faked. principle / neutral / S26, S36 ch.2 / consensus / grounded.
- APP-C07. Whether to decouple the domain model from the ORM (ORM imports the model, repository abstraction) or use ORM models as the domain is a recorded decision. decision / python / S36 ch.2, S06, S30, S34 / contested / grounded. positions: Cosmic Python holds decouple, at the cost of extra code and mapping upkeep, worthwhile as domain complexity grows and "CRUD-focused applications don't require domain models or repositories"; Django holds models include all domain logic (Active Record); Fowler holds ORMs handle 80-90% of mapping and are better than home-grown mapping. Applies: decouple when domain logic is complex and unit-test speed matters; Active Record when mostly CRUD.
- APP-C08. Start a new web application as a single deployable and split into services only once boundaries are proven. decision / neutral / S29, S25 (factor I headline "one codebase, many deploys") / consensus / grounded. positions: single T2 essay (2015, self-described tentative); exception: system replacements with stable boundaries and an experienced team.

**Transactions and unit of work**

- APP-C09. Each business operation should have one explicit transaction boundary, owned by the use-case layer, with a clear notion of where it begins and ends. principle / neutral / S14, S27, S28, S36 ch.6 / consensus / grounded.
- APP-C10. Keep transactions short. practice / neutral / S01, S14 / consensus / grounded.
- APP-C11. Prefer a use-case-scoped transaction over a transaction around the whole HTTP request; a request-wide transaction is acceptable for simple applications. decision / python / S01, S14, S36 ch.6 / majority / grounded. positions: Django offers ATOMIC_REQUESTS as the simple option and warns of overhead under high traffic; SQLAlchemy shows session-per-request with commit on writes; Cosmic Python scopes a unit of work per use case.
- APP-C12. Make the safe path the default: no change is persisted unless the use case commits explicitly; roll back on any exception. practice / python / S36 ch.6, S14 / majority / grounded. positions: Django's default is autocommit (each query commits unless inside atomic), the opposite default (S01).
- APP-C13. Never catch and swallow exceptions inside an atomic block; catch outside it so the framework sees the failure. practice / python (Django) / S01 / consensus (single source) / grounded.
- APP-C14. A database session is stateful and not shareable: one session per thread, one AsyncSession per task, created and closed at the entry point. practice / python / S14, S15 / consensus / grounded.
- APP-C15. Trigger side effects (email, task enqueue, event publish, cache invalidation) only after the transaction commits (on_commit hooks). practice / python / S01, S04, S23 / consensus / grounded. boundary: none.
- APP-C16. Do not hold a database transaction open across calls to remote services; bracket each foreign mutation with its own short local transactions. practice / neutral / S01, S14, S40 / consensus / inferred (synthesis: short transactions plus Brandur's atomic phases around foreign mutations).

**Outbox, jobs and integration**

- APP-C17. Updating the database and notifying a broker or another service cannot be made atomic by two writes; record the message in the same transaction (outbox) or stage jobs in a table and drain them after commit. decision / postgres / S35, S41, S42 / consensus / grounded.
- APP-C18. Outbox relays deliver at least once, so consumers and jobs must be idempotent (for example by tracking processed message ids). practice / neutral / S35, S23, S37 / consensus / grounded.
- APP-C19. The job-queue backing store is a recorded decision. decision / postgres / S22, S41, S09, S19 / contested / grounded. positions: PostgreSQL docs say SKIP LOCKED "can be used to avoid lock contention with multiple consumers accessing a queue-like table" while being an inconsistent view; Brandur argues in-database queues scale poorly under load and long transactions and prefers staging in the database then draining to a broker; FastAPI and Flask docs point to a broker-based task queue (Celery with Redis or RabbitMQ). Applies: database queue at low volume where one fewer component matters; broker when volume or multi-server fan-out grows. boundary: DATA (SKIP LOCKED).
- APP-C20. Move slow or non-essential work out of the request cycle into separate worker processes. decision / neutral / S19, S09, S04, S25 (factor VIII) / consensus / grounded.
- APP-C21. Use in-process background execution only for small tasks that need the same process; use a task queue for heavy, durable or multi-server work. In an async-in-WSGI Flask view you cannot spawn background tasks at all. decision / python / S09, S18, S19 / consensus / grounded.
- APP-C22. Pass task arguments as small serializable data (ids), not ORM objects, and re-fetch inside the task. practice / python / S19, S23, S04 / consensus / grounded.
- APP-C23. Make tasks idempotent; enable late acknowledgement only for idempotent tasks. practice / python / S23 / consensus (single source for acks_late) / grounded.
- APP-C24. Do not make a task wait synchronously for another task (inefficiency and deadlock when the pool is exhausted); chain instead. practice / python / S23 / consensus (single source) / grounded.
- APP-C25. Django's Tasks framework ships no worker and its built-in backends are for development and testing; production needs a third-party backend and a separate worker process. practice / python / S04 / consensus (single source) / grounded.

**Stateless processes and scaling**

- APP-C26. Run the app as stateless, share-nothing processes; persist anything durable in a backing service; process memory or disk is at most a single-request cache. principle / neutral / S25 (factor VI) / consensus / grounded.
- APP-C27. Do not rely on sticky sessions; keep user sessions in an external store. practice / neutral / S25 (VI), S05 / consensus / grounded. boundary: SEC (session mechanism).
- APP-C28. Scale out by running more processes, separated by process type (web, worker), managed by an external process manager rather than self-daemonizing. principle / neutral / S25 (VIII), S12, S24 / consensus / grounded.
- APP-C29. Processes start fast, shut down gracefully on SIGTERM (a worker returns its current job to the queue) and tolerate sudden death. principle / neutral / S25 (IX) / consensus / grounded. boundary: OPS.
- APP-C30. Run one-off admin work (migrations, shells) with the same code and environment as the app, and run pre-start steps such as migrations once, not per worker. practice / neutral / S25 (XII), S12 / consensus / grounded. boundary: OPS, DATA.
- APP-C31. Treat each backing service (database, queue, mail, third-party API) as an attached resource whose location and credentials come from config, with no code distinction between local and third-party. principle / neutral / S25 (IV), S26 / consensus / grounded.

**Sync and async**

- APP-C32. Default to synchronous handlers; adopt async only where in-process I/O concurrency pays (many external calls, streaming, long-lived connections). Async is not inherently faster and does not help CPU-bound work or purely synchronous code. decision / python / S18, S02, S08, S15 / consensus / grounded.
- APP-C33. Never run blocking code on the event loop; use def handlers (threadpool) or run_in_executor/sync_to_async for blocking libraries. practice / python / S20, S08, S02 / consensus / grounded.
- APP-C34. Async data access has hard constraints: Django states transactions do not yet work in async mode (wrap transactional code in one sync function; version-dependent, re-check); SQLAlchemy needs one AsyncSession per task, no lazy loading or other implicit I/O, expire_on_commit off. practice / python / S02, S15 / consensus / grounded.
- APP-C35. Under async, disable per-thread persistent connections (CONN_MAX_AGE 0) and use a pool sized to target in-flight query concurrency. practice / python / S02, S03 / consensus / grounded. boundary: DATA.
- APP-C36. Choose ASGI when async, WebSockets or long-lived connections are needed; ASGI is a superset of WSGI and WSGI apps can run under it through a wrapper. decision / python / S21, S02 / consensus / grounded. boundary: API (long-lived connections).
- APP-C37. Sync workers need a buffering reverse proxy in front (slow clients); size workers modestly (starting point 2 x cores + 1, "workers are not clients"); threaded or async workers suit I/O-bound loads, sync suits CPU-bound. practice / python / S24, S12 / consensus / grounded. boundary: OPS (sizing).

**Framework and structure**

- APP-C38. The framework is a recorded decision whose criteria are the product's needs. decision / python / S06, S17, S08, S10, S13 / contested / grounded for each framework's self-description, open for neutral criteria. positions: Django, batteries-included with ORM, loose coupling, Active Record models; Flask, micro, no database layer, thread locals, "not designed for large applications or asynchronous servers", async via threads with a performance cost; FastAPI, ASGI, dependency injection, accepts def and async def, router modules for larger apps. No T1 or T2 source gives neutral selection criteria (gap).
- APP-C39. Construct the application object and its configuration explicitly (factory function, injected settings) so tests and other deploys can substitute them. practice / python / S17, S11, S10 / majority / grounded. positions: Flask and FastAPI document it; Django uses a settings module selected per deploy.

**ORM and SQL**

- APP-C40. Use an ORM for routine mapping while understanding the relational model, and keep a sanctioned route to hand-written SQL for what the ORM expresses badly; explore the ORM first. decision / python / S30, S07, S16 / consensus / grounded.
- APP-C41. Raw SQL always uses bound parameters, never string formatting. practice / python / S07 / consensus (single source) / grounded. boundary: SEC.
- APP-C42. Reads that do not need domain behavior may bypass the domain model (hand-written SQL, views, denormalized tables, separate read stores); use the repository or ORM when reads resemble the write model. practice / python / S36 ch.12, S30 / majority / grounded. positions: Cosmic Python lists five options with trade-offs (hand-rolled SQL means schema changes need dual updates); Fowler says read-only use needs a simpler approach than a full ORM.

**External services and resilience**

- APP-C43. Expect transient faults on calls to external services: retry with bounded attempts and increasing delay with jitter-like spreading, only operations that are idempotent; in interactive requests fail fast with few retries, in batch work retry more. practice / neutral / S37, S39 / consensus / grounded.
- APP-C44. Retry at one layer only, to avoid combinatorial request amplification; cap per-request and per-client retries (Google: three attempts and a 10% retry ratio). practice / neutral / S39, S37 / consensus / grounded.
- APP-C45. For persistent faults fail fast with a circuit breaker and timeouts short enough to protect threads and connections; do not use a breaker as a substitute for business exception handling. practice / neutral / S38, S37 / consensus / grounded.
- APP-C46. For calls that mutate foreign state, use client-supplied idempotency keys and recorded recovery points so interrupted requests can resume. practice / neutral / S40 / majority / grounded. positions: single T3 source, no dissent found; consistent with S37 idempotency advice.

**Configuration**

- APP-C47. Keep config strictly separate from code and store it in the environment; test: the codebase could be open-sourced without leaking credentials. principle / neutral / S25 (III), S05, S11 / consensus / grounded.
- APP-C48. Manage environment variables independently per deploy rather than grouping them into named environments. practice / neutral / S25 (III), S05, S11 / majority / grounded. positions: Twelve-Factor holds independent variables; Django's checklist and FastAPI's settings page use per-environment settings and .env files.
- APP-C49. Load config once into a typed, validated settings object at startup and inject it, so tests can override it. practice / python / S11 / consensus (single source) / grounded.
- APP-C50. Secrets come from the environment or a file outside source control; debug mode off in production; run the framework's deploy check before release. practice / python / S05 / consensus (single source) / grounded. boundary: SEC.

### Gaps (open)

- Books not read: Kleppmann (DDIA, dual writes, idempotence), Nygard (Release It!, timeouts and bulkheads), Evans (DDD, aggregates as transaction boundaries). Aggregate-per-transaction guidance is therefore absent.
- No T1 or T2 source found that gives neutral framework-selection criteria (APP-C38).
- Not researched: caching, rate limiting, scheduled jobs, file upload handling, WebSocket server architecture, dependency-injection style, modular-monolith internals, Django project layout, external connection poolers.
- Cosmic Python epilogue (incremental adoption advice) returned 404; adoption path not evidenced.
- Debezium page did not confirm consumer deduplication guidance; APP-C18 rests on S35 and S23.
- Django's "transactions do not yet work in async mode" is version-dependent; re-check against the Django version pinned by the guideline.
- All pages read as tool-extracted excerpts; verify any quoted wording against the page before publishing it verbatim.
