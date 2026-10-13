# Source register: deduplicated across all research slots

One row per document. Rules: a page read by several slots is one entry; a book, thesis or guideline set read across several pages (Twelve-Factor App, Fielding's dissertation, Google SRE book, Resilient Web Design) is one entry with the pages noted; an Internet-Draft is T2 until published (round-2 rule); where slots ranked the same document or body differently, one tier is set and the reason noted. URLs are the ones the slots read; the three T4 search-snippet entries of the data slot have no URL.

Pinned:
- Original source ids in: 446 (445 public, 1 maintainer). Register entries out: 358 public (T1 192, T2 85, T3 70, T4 11).
- Round 3: 31 new entries (SRC-328 onward); 13 existing entries absorbed a round-3 id; round-2 ids unchanged.
- Entries replacing more than one original id: 57. Tier changes noted: 7.

## T1

| id | tier | title | body | URL | replaces | note |
|---|---|---|---|---|---|---|
| SRC-001 | T1 | ASGI specification, HTTP and WebSocket | ASGI | https://asgi.readthedocs.io/en/latest/specs/www.html | RT-S15 | - |
| SRC-002 | T1 | ASGI introduction | ASGI spec | asgi.readthedocs.io/en/latest/introduction.html | APP-S21, TOPO-S23 | tier set to T1: official specification docs of the interface (APP, RT ranked T1; TOPO ranked T2) |
| SRC-003 | T1 | Daemonization | Celery | docs.celeryq.dev/en/stable/userguide/daemonizing.html | TOPO-S21 | - |
| SRC-004 | T1 | Tasks, tips and best practices | Celery | docs.celeryq.dev/en/stable/userguide/tasks.html | APP-S23 | - |
| SRC-005 | T1 | Asynchronous support | Django | docs.djangoproject.com/en/stable/topics/async/ | APP-S02, RT-S12 | - |
| SRC-006 | T1 | Database transactions | Django | docs.djangoproject.com/en/stable/topics/db/transactions/ | APP-S01, CONS-S09 | - |
| SRC-007 | T1 | Databases (pooling, persistent connections) | Django | docs.djangoproject.com/en/stable/ref/databases/ | APP-S03 | - |
| SRC-008 | T1 | Deployment checklist | Django | docs.djangoproject.com/en/stable/howto/deployment/checklist/ | APP-S05, TOPO-S01 | - |
| SRC-009 | T1 | Design philosophies | Django | docs.djangoproject.com/en/stable/misc/design-philosophies/ | APP-S06, ARCH-S28 | - |
| SRC-010 | T1 | Django Channels docs, Channel layers | Django | https://channels.readthedocs.io/en/stable/topics/channel_layers.html | RT-S14 | - |
| SRC-011 | T1 | Django docs, Request and response objects (StreamingHttpResponse) | Django | https://docs.djangoproject.com/en/stable/ref/request-response/ | RT-S13 | - |
| SRC-012 | T1 | How to deploy Django (index) | Django | docs.djangoproject.com/en/stable/howto/deployment/ | TOPO-S02 | - |
| SRC-013 | T1 | How to deploy with ASGI | Django | docs.djangoproject.com/en/stable/howto/deployment/asgi/ | TOPO-S03 | - |
| SRC-014 | T1 | How to use Django with Gunicorn | Django | docs.djangoproject.com/en/stable/howto/deployment/wsgi/gunicorn/ | TOPO-S06 | - |
| SRC-015 | T1 | Performing raw SQL queries | Django | docs.djangoproject.com/en/stable/topics/db/sql/ | APP-S07 | - |
| SRC-016 | T1 | Settings reference (SECURE_PROXY_SSL_HEADER, SECURE_SSL_REDIRECT, SECURE_HSTS_*) | Django | docs.djangoproject.com/en/stable/ref/settings/ | TOPO-S04, RATE-S10 | - |
| SRC-017 | T1 | Tasks framework | Django | docs.djangoproject.com/en/stable/topics/tasks/ | APP-S04 | - |
| SRC-018 | T1 | Deploying static files | Django docs | https://docs.djangoproject.com/en/stable/howto/static-files/deployment/ | UI-S18, TOPO-S05 | - |
| SRC-019 | T1 | Django tutorial part 4 | Django docs | https://docs.djangoproject.com/en/stable/intro/tutorial04/ | THIN-S11 | - |
| SRC-020 | T1 | Django's cache framework | Django docs | https://docs.djangoproject.com/en/stable/topics/cache/ | OPS-S15 | - |
| SRC-021 | T1 | How to use sessions | Django docs | https://docs.djangoproject.com/en/stable/topics/http/sessions/ | SEC-S23 | - |
| SRC-022 | T1 | Migration Operations | Django docs | https://docs.djangoproject.com/en/stable/ref/migration-operations/ | DATA-S24 | - |
| SRC-023 | T1 | Password management in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/auth/passwords/ | SEC-S24 | - |
| SRC-024 | T1 | Security in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/security/ | SEC-S22, RATE-S09 | - |
| SRC-025 | T1 | Testing in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/testing/overview/ | OPS-S14 | - |
| SRC-026 | T1 | The staticfiles app | Django docs | https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/ | UI-S19 | - |
| SRC-027 | T1 | Django: File Uploads; UploadedFile reference | Django project | https://docs.djangoproject.com/en/stable/topics/http/file-uploads/ and https://docs.djangoproject.com/en/stable/ref/files/uploads/ | UPLOAD-S02 | - |
| SRC-028 | T1 | Building best practices | Docker | docs.docker.com/build/building/best-practices/ | TOPO-S20 | - |
| SRC-029 | T1 | Background Tasks | FastAPI | fastapi.tiangolo.com/tutorial/background-tasks/ | APP-S09 | - |
| SRC-030 | T1 | Bigger Applications | FastAPI | fastapi.tiangolo.com/tutorial/bigger-applications/ | APP-S13 | - |
| SRC-031 | T1 | Concurrency and async / await | FastAPI | fastapi.tiangolo.com/async/ | APP-S08 | - |
| SRC-032 | T1 | Dependencies with yield | FastAPI | fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/ | APP-S10 | - |
| SRC-033 | T1 | Deployment concepts | FastAPI | fastapi.tiangolo.com/deployment/concepts/ | APP-S12, TOPO-S10 | - |
| SRC-034 | T1 | FastAPI docs, WebSockets | FastAPI | https://fastapi.tiangolo.com/advanced/websockets/ | RT-S16 | - |
| SRC-035 | T1 | FastAPI in containers | FastAPI | fastapi.tiangolo.com/deployment/docker/ | TOPO-S11 | - |
| SRC-036 | T1 | FastAPI: Request Files | FastAPI | https://fastapi.tiangolo.com/tutorial/request-files/ | UPLOAD-S03 | - |
| SRC-037 | T1 | Settings and Environment Variables | FastAPI | fastapi.tiangolo.com/advanced/settings/ | APP-S11 | - |
| SRC-038 | T1 | Security (tutorial intro) | FastAPI docs | https://fastapi.tiangolo.com/tutorial/security/ | SEC-S25 | - |
| SRC-328 | T1 | FastAPI docs: Response Model | FastAPI docs: Response Model | https://fastapi.tiangolo.com/tutorial/response-model/ | DCON-S06 | - |
| SRC-039 | T1 | OAuth2 with Password (and hashing), Bearer with JWT tokens | FastAPI documentation | https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ | CV-S20 | - |
| SRC-040 | T1 | Design | Gunicorn | gunicorn.org/design/ | APP-S24, TOPO-S07 | - |
| SRC-041 | T1 | Deploying Gunicorn | Gunicorn project | gunicorn.org/deploy/ | TOPO-S08 | - |
| SRC-042 | T1 | RFC 10017 OAuth 2.0 for Browser-Based Applications (BCP 212) | IETF | https://www.rfc-editor.org/rfc/rfc10017.html | SEC-S08 | - |
| SRC-043 | T1 | RFC 6202, Known Issues and Best Practices for Bidirectional HTTP (Informational RFC) | IETF | https://www.rfc-editor.org/rfc/rfc6202 | RT-S03 | - |
| SRC-044 | T1 | RFC 6455, The WebSocket Protocol | IETF | https://www.rfc-editor.org/rfc/rfc6455 | RT-S02 | - |
| SRC-045 | T1 | RFC 6585, section 4 (429 Too Many Requests) | IETF | https://www.rfc-editor.org/rfc/rfc6585.html | RATE-S02 | - |
| SRC-046 | T1 | RFC 6797 HTTP Strict Transport Security | IETF | rfc-editor.org/rfc/rfc6797.html | TOPO-S15 | - |
| SRC-047 | T1 | RFC 7231 (obsoleted by RFC 9110), 6.4.4 | IETF | https://www.rfc-editor.org/rfc/rfc7231.html | THIN-S09 | - |
| SRC-048 | T1 | RFC 7239 Forwarded HTTP Extension | IETF | rfc-editor.org/rfc/rfc7239.html | TOPO-S16 | - |
| SRC-049 | T1 | RFC 8246 HTTP Immutable Responses | IETF | https://www.rfc-editor.org/rfc/rfc8246.html | UI-S05 | - |
| SRC-050 | T1 | RFC 8441, Bootstrapping WebSockets with HTTP/2 | IETF | https://www.rfc-editor.org/rfc/rfc8441 | RT-S11 | - |
| SRC-051 | T1 | RFC 8594 The Sunset HTTP Header Field (Informational) | IETF | https://www.rfc-editor.org/rfc/rfc8594.html | API-S10 | - |
| SRC-052 | T1 | RFC 8725 JSON Web Token Best Current Practices | IETF | https://datatracker.ietf.org/doc/html/rfc8725 | SEC-S30 | - |
| SRC-053 | T1 | RFC 9110 HTTP Semantics | IETF | https://www.rfc-editor.org/rfc/rfc9110.html | API-S01, RATE-S03, THIN-S08 | one document; API read sections 9, 12, 13, 15; RATE read 15.5.14 and 10.2.3 as an extract; THIN-S08's three fetches were truncated before section 15 (15.4.4 seen only in a search extract) |
| SRC-054 | T1 | RFC 9111 HTTP Caching | IETF | https://www.rfc-editor.org/rfc/rfc9111.html | UI-S06, OPS-S10 | - |
| SRC-055 | T1 | RFC 9113, HTTP/2 (section 6.5.2 only) | IETF | https://www.rfc-editor.org/rfc/rfc9113 | RT-S10 | - |
| SRC-056 | T1 | RFC 9457 Problem Details for HTTP APIs | IETF | https://www.rfc-editor.org/rfc/rfc9457.html | API-S02 | - |
| SRC-057 | T1 | RFC 9700 OAuth 2.0 Security Best Current Practice | IETF | https://datatracker.ietf.org/doc/html/rfc9700 | SEC-S06 | - |
| SRC-058 | T1 | RFC 9745 The Deprecation HTTP Response Header Field | IETF | https://www.rfc-editor.org/rfc/rfc9745.html | API-S09 | - |
| SRC-329 | T1 | JSON Schema reference: object (additionalProperties, required, unevaluatedProperties) | json-schema.org | https://json-schema.org/understanding-json-schema/reference/object | DCON-S01 | - |
| SRC-330 | T1 | JSON Schema reference: type | json-schema.org | https://json-schema.org/understanding-json-schema/reference/type | DCON-S02 | - |
| SRC-059 | T1 | Client-side form validation | MDN | https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation | UI-S16 | - |
| SRC-060 | T1 | History API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/History_API | UI-S17 | - |
| SRC-061 | T1 | HTTP Cookies guide | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies | SEC-S19 | - |
| SRC-062 | T1 | MDN: 303 See Other | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303 | API-S06, THIN-S10 | - |
| SRC-063 | T1 | MDN: Conditional requests | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests | API-S05 | - |
| SRC-064 | T1 | MDN: Content-Disposition | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Disposition | UPLOAD-S05 | - |
| SRC-065 | T1 | MDN: Cross-Origin Resource Sharing (CORS) | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS | API-S03 | - |
| SRC-066 | T1 | MDN: HTTP caching | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching | API-S07, UI-S04, OPS-S09, WEB-S11 | - |
| SRC-067 | T1 | MDN: Same-origin policy | MDN | https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy | API-S04, TOPO-S22 | - |
| SRC-068 | T1 | MDN: X-Content-Type-Options | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options | UPLOAD-S04 | - |
| SRC-069 | T1 | MDN: X-Forwarded-For | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-For | RATE-S11 | - |
| SRC-070 | T1 | Navigator.sendBeacon() | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon | THIN-S17 | - |
| SRC-071 | T1 | PerformanceObserver | MDN | https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver | THIN-S16 | - |
| SRC-072 | T1 | Practical implementation guide: CSP | MDN | https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP | SEC-S12 | - |
| SRC-073 | T1 | Progressive enhancement (glossary) | MDN | https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement | UI-S03, WEB-S12 | - |
| SRC-074 | T1 | Reporting API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API | THIN-S14 | - |
| SRC-075 | T1 | Server-Timing | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing | OPS-S16 | - |
| SRC-076 | T1 | SPA (glossary) | MDN | https://developer.mozilla.org/en-US/docs/Glossary/SPA | CV-S09 | - |
| SRC-077 | T1 | Strict-Transport-Security | MDN | developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security | TOPO-S14 | - |
| SRC-078 | T1 | Web Locks API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Web_Locks_API | WEB-S13 | - |
| SRC-079 | T1 | Window: error event | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event | THIN-S12 | - |
| SRC-080 | T1 | Window: unhandledrejection event | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event | THIN-S13 | - |
| SRC-081 | T1 | MDN, Using server-sent events | Mozilla | https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events | RT-S06 | - |
| SRC-082 | T1 | MDN, WebSocket API | Mozilla | https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API | RT-S07 | - |
| SRC-083 | T1 | NGINX reverse proxy | nginx | docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/ | TOPO-S13 | - |
| SRC-084 | T1 | NGINX, WebSocket proxying | NGINX | https://nginx.org/en/docs/http/websocket.html | RT-S08 | - |
| SRC-085 | T1 | ngx_http_proxy_module | nginx | nginx.org/en/docs/http/ngx_http_proxy_module.html | TOPO-S12, RT-S09 | - |
| SRC-086 | T1 | nginx core module: client_max_body_size, client_body_timeout | nginx project | https://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size | RATE-S14 | tier set to T1: official nginx docs; harmonized with the other nginx pages ranked T1 (RATE ranked T3) |
| SRC-087 | T1 | nginx ngx_http_limit_req_module | nginx project | https://nginx.org/en/docs/http/ngx_http_limit_req_module.html | RATE-S13 | tier set to T1: official nginx docs; harmonized with the other nginx pages ranked T1 (RATE ranked T3) |
| SRC-088 | T1 | NIST SP 800-63B-4 Authentication and Authenticator Management | NIST | https://pages.nist.gov/800-63-4/sp800-63b.html | SEC-S18 | - |
| SRC-089 | T1 | OpenAPI Specification (latest, 3.2.1 in the copy read) | OpenAPI Initiative | https://spec.openapis.org/oas/latest.html | API-S08, DCON-S03 | - |
| SRC-090 | T1 | OpenID Connect Core 1.0 | OpenID Foundation | https://openid.net/specs/openid-connect-core-1_0.html | SEC-S17 | - |
| SRC-091 | T1 | Context propagation | OpenTelemetry | https://opentelemetry.io/docs/concepts/context-propagation/ | OPS-S03 | - |
| SRC-092 | T1 | General metric semantic conventions | OpenTelemetry | https://opentelemetry.io/docs/specs/semconv/general/metrics/ | OPS-S08 | - |
| SRC-093 | T1 | JavaScript browser getting started | OpenTelemetry | https://opentelemetry.io/docs/languages/js/getting-started/browser/ | OPS-S06 | - |
| SRC-094 | T1 | Logs specification | OpenTelemetry | https://opentelemetry.io/docs/specs/otel/logs/ | OPS-S04 | - |
| SRC-095 | T1 | Sampling | OpenTelemetry | https://opentelemetry.io/docs/concepts/sampling/ | OPS-S05 | - |
| SRC-096 | T1 | Signals | OpenTelemetry | https://opentelemetry.io/docs/concepts/signals/ | OPS-S02 | - |
| SRC-097 | T1 | Zero-code instrumentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/instrumentation/zero-code/ | OPS-S07 | - |
| SRC-098 | T1 | A01:2025 Broken Access Control | OWASP | https://top10.owasp.org/2025/A01_2025-Broken_Access_Control | SEC-S10 | - |
| SRC-099 | T1 | A03:2025 Software Supply Chain Failures | OWASP | https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures | SEC-S11 | - |
| SRC-100 | T1 | Authentication Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html | SEC-S15, RATE-S07 | - |
| SRC-101 | T1 | Authorization Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | SEC-S03 | - |
| SRC-102 | T1 | Content Security Policy Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html | SEC-S04 | - |
| SRC-103 | T1 | Credential Stuffing Prevention Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html | RATE-S06 | - |
| SRC-104 | T1 | CSRF Prevention Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html | SEC-S02 | - |
| SRC-105 | T1 | Denial of Service Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html | RATE-S08 | - |
| SRC-106 | T1 | File Upload Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html | UPLOAD-S01 | - |
| SRC-107 | T1 | HTML5 Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html | SEC-S31 | - |
| SRC-108 | T1 | HTTP Headers Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html | SEC-S14 | - |
| SRC-109 | T1 | Logging Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | OPS-S18, THIN-S01 | - |
| SRC-110 | T1 | Multi-Tenant Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html | SEC-S32 | - |
| SRC-111 | T1 | OWASP API4:2023 Unrestricted Resource Consumption | OWASP | https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption | RATE-S04 | - |
| SRC-112 | T1 | OWASP API6:2023 Unrestricted Access to Sensitive Business Flows | OWASP | https://api-security.owasp.org/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows | RATE-S05 | - |
| SRC-113 | T1 | OWASP Application Security Verification Standard project page | OWASP | https://owasp.org/www-project-application-security-verification-standard/ | SEC-S33 | - |
| SRC-114 | T1 | OWASP Secure Headers Project (page is an index only) | OWASP | https://owasp.org/www-project-secure-headers/ | SEC-S13 | - |
| SRC-115 | T1 | OWASP Top 10:2025 | OWASP | https://top10.owasp.org/2025 | SEC-S09 | - |
| SRC-116 | T1 | OWASP WebSocket Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html | RT-S17 | - |
| SRC-117 | T1 | Password Storage Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html | SEC-S16 | - |
| SRC-118 | T1 | Secrets Management Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | SEC-S05 | - |
| SRC-119 | T1 | Session Management Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html | SEC-S01 | - |
| SRC-120 | T1 | Software Supply Chain Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html | SEC-S28 | - |
| SRC-121 | T1 | Transport Layer Security Cheat Sheet | OWASP | cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html | TOPO-S17 | - |
| SRC-122 | T1 | Logging Vocabulary Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html | THIN-S02 | - |
| SRC-123 | T1 | A09:2021 Security Logging and Monitoring Failures | OWASP Top 10 | https://top10.owasp.org/2021/A09_2021-Security_Logging_and_Monitoring_Failures | THIN-S03 | - |
| SRC-124 | T1 | Design Decisions in Flask | Pallets | flask.palletsprojects.com/en/stable/design/ | APP-S17 | - |
| SRC-125 | T1 | Background Tasks with Celery | Pallets (Flask) | flask.palletsprojects.com/en/stable/patterns/celery/ | APP-S19 | - |
| SRC-126 | T1 | Using async and await | Pallets (Flask) | flask.palletsprojects.com/en/stable/async-await/ | APP-S18 | - |
| SRC-127 | T1 | PgBouncer features | PgBouncer maintainers | https://www.pgbouncer.org/features.html | DATA-S36, RT-S18 | tier set to T1: official docs of a tool in the runtime path (RT ranked T1; DATA ranked T3) |
| SRC-128 | T1 | Secure installs | pip docs (PyPA) | https://pip.pypa.io/en/stable/topics/secure-installs/ | SEC-S29 | - |
| SRC-331 | T1 | PostgreSQL docs, Data Consistency Checks at the Application Level | PostgreSQL | https://www.postgresql.org/docs/current/applevel-consistency.html | CONS-S05 | - |
| SRC-332 | T1 | PostgreSQL docs, Error Codes appendix | PostgreSQL | https://www.postgresql.org/docs/current/errcodes-appendix.html | CONS-S08 | - |
| SRC-333 | T1 | PostgreSQL docs, INSERT (ON CONFLICT) | PostgreSQL | https://www.postgresql.org/docs/current/sql-insert.html | CONS-S07 | - |
| SRC-129 | T1 | PostgreSQL docs, LISTEN | PostgreSQL | https://www.postgresql.org/docs/current/sql-listen.html | RT-S05 | - |
| SRC-334 | T1 | PostgreSQL docs, Sequence Manipulation Functions | PostgreSQL | https://www.postgresql.org/docs/current/functions-sequence.html | CONS-S03 | - |
| SRC-335 | T1 | PostgreSQL docs, Serialization Failure Handling | PostgreSQL | https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html | CONS-S04 | - |
| SRC-130 | T1 | ALTER TABLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-altertable.html | DATA-S05 | - |
| SRC-131 | T1 | Client Connection Defaults (19.11) | PostgreSQL docs | https://www.postgresql.org/docs/current/runtime-config-client.html | DATA-S17 | - |
| SRC-132 | T1 | Configuration settings functions (set_config) | PostgreSQL docs | https://www.postgresql.org/docs/current/functions-admin.html | SEC-S21 | - |
| SRC-133 | T1 | Connection Settings (19.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/runtime-config-connection.html | DATA-S18 | - |
| SRC-134 | T1 | Constraints (5.5) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-constraints.html | DATA-S01, THIN-S06, DCON-S04 | - |
| SRC-135 | T1 | Continuous Archiving and PITR (25.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/continuous-archiving.html | DATA-S04 | - |
| SRC-136 | T1 | CREATE INDEX | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createindex.html | DATA-S06 | - |
| SRC-137 | T1 | CREATE ROLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createrole.html | DATA-S11 | - |
| SRC-138 | T1 | CREATE TABLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createtable.html | DATA-S16, THIN-S05 | - |
| SRC-139 | T1 | CREATE TRIGGER | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createtrigger.html | DATA-S20 | - |
| SRC-140 | T1 | CREATE VIEW | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createview.html | DATA-S09 | - |
| SRC-141 | T1 | Explicit Locking (13.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/explicit-locking.html | DATA-S19, CONS-S02 | - |
| SRC-142 | T1 | Generated Columns (5.4) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-generated-columns.html | DATA-S23 | - |
| SRC-143 | T1 | NOTIFY | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-notify.html | DATA-S15, RT-S04 | - |
| SRC-144 | T1 | pg_hba.conf (20.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/auth-pg-hba-conf.html | DATA-S22 | - |
| SRC-145 | T1 | pg_stat_statements | PostgreSQL docs | https://www.postgresql.org/docs/current/pgstatstatements.html | OPS-S17 | - |
| SRC-146 | T1 | Privileges (5.8) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-priv.html | DATA-S03 | - |
| SRC-147 | T1 | Reliability (28.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/wal-reliability.html | DATA-S21 | - |
| SRC-148 | T1 | Role Attributes (21.2) | PostgreSQL docs | https://www.postgresql.org/docs/current/role-attributes.html | DATA-S10 | - |
| SRC-149 | T1 | Row Security Policies (5.9) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-rowsecurity.html | DATA-S07, SEC-S20 | - |
| SRC-150 | T1 | Schemas (5.10) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-schemas.html | DATA-S02 | - |
| SRC-151 | T1 | SELECT (locking clause) | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-select.html | DATA-S12, APP-S22, ARCH-S20, CONS-S06 | - |
| SRC-152 | T1 | SQL Dump (25.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/backup-dump.html | DATA-S14 | - |
| SRC-153 | T1 | Table Partitioning (5.12) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-partitioning.html | DATA-S13, THIN-S04 | - |
| SRC-154 | T1 | UUID Functions (9.14) | PostgreSQL docs | https://www.postgresql.org/docs/current/functions-uuid.html | DATA-S08 | - |
| SRC-155 | T1 | Overview of Trigger Behavior | PostgreSQL docs (current) | https://www.postgresql.org/docs/current/trigger-definition.html | THIN-S07 | - |
| SRC-336 | T1 | PostgreSQL docs: CREATE DOMAIN | PostgreSQL docs: CREATE DOMAIN | https://www.postgresql.org/docs/current/sql-createdomain.html | DCON-S05 | - |
| SRC-337 | T1 | PostgreSQL docs, Transaction Isolation (incl. Serializable Isolation Level) | PostgreSQL Global Development Group | https://www.postgresql.org/docs/current/transaction-iso.html | CONS-S01 | - |
| SRC-156 | T1 | PostgreSQL: TOAST | PostgreSQL project | https://www.postgresql.org/docs/current/storage-toast.html | UPLOAD-S06 | - |
| SRC-157 | T1 | Developing with asyncio | Python | docs.python.org/3/library/asyncio-dev.html | APP-S20 | - |
| SRC-158 | T1 | Asynchronous I/O (asyncio) extension | SQLAlchemy | docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html | APP-S15 | - |
| SRC-159 | T1 | Overview (Core vs ORM) | SQLAlchemy | docs.sqlalchemy.org/en/20/intro.html | APP-S16 | - |
| SRC-160 | T1 | Session Basics | SQLAlchemy | docs.sqlalchemy.org/en/20/orm/session_basics.html | APP-S14 | - |
| SRC-161 | T1 | Deployment | Uvicorn project | uvicorn.dev/deployment/ | TOPO-S09 | - |
| SRC-162 | T1 | Trace Context | W3C | https://www.w3.org/TR/trace-context/ | OPS-S01 | - |
| SRC-163 | T1 | Using ARIA | W3C | https://www.w3.org/TR/using-aria/ | UI-S15 | - |
| SRC-164 | T1 | WCAG 2.2 | W3C | https://www.w3.org/TR/WCAG22/ | UI-S07 | - |
| SRC-165 | T1 | Accessibility principles | W3C WAI | https://www.w3.org/WAI/fundamentals/accessibility-principles/ | UI-S08 | - |
| SRC-166 | T1 | Back/forward cache | web.dev | https://web.dev/articles/bfcache | UI-S14, WEB-S10 | - |
| SRC-167 | T1 | Content delivery networks | web.dev | web.dev/articles/content-delivery-networks | TOPO-S19 | - |
| SRC-168 | T1 | Cumulative Layout Shift | web.dev | https://web.dev/articles/cls | UI-S13 | - |
| SRC-169 | T1 | How to measure Core Web Vitals in the field | web.dev | https://web.dev/articles/vitals-field-measurement-best-practices | THIN-S15 | - |
| SRC-170 | T1 | Interaction to Next Paint | web.dev | https://web.dev/articles/inp | UI-S12 | - |
| SRC-171 | T1 | Lab and field data differences | web.dev | https://web.dev/articles/lab-and-field-data-differences | OPS-S12 | - |
| SRC-172 | T1 | Optimize INP | web.dev | https://web.dev/articles/optimize-inp | UI-S11 | - |
| SRC-173 | T1 | Optimize LCP | web.dev | https://web.dev/articles/optimize-lcp | UI-S10 | - |
| SRC-174 | T1 | Performance budgets 101 | web.dev | https://web.dev/articles/performance-budgets-101 | UI-S09 | - |
| SRC-175 | T1 | Prevent unnecessary network requests with the HTTP Cache | web.dev | https://web.dev/articles/http-cache | OPS-S13 | - |
| SRC-176 | T1 | Protect your resources from web attacks with Fetch Metadata | web.dev | https://web.dev/articles/fetch-metadata | SEC-S26 | - |
| SRC-177 | T1 | SameSite cookies explained | web.dev | https://web.dev/articles/samesite-cookies-explained | SEC-S27 | - |
| SRC-178 | T1 | Service worker lifecycle | web.dev | https://web.dev/articles/service-worker-lifecycle | WEB-S23 | - |
| SRC-179 | T1 | Web Vitals | web.dev | https://web.dev/articles/vitals | UI-S02, OPS-S11, WEB-S14 | - |
| SRC-180 | T1 | Why HTTPS matters | web.dev | web.dev/articles/why-https-matters | TOPO-S18 | - |
| SRC-181 | T1 | Rendering on the Web | web.dev (Google) | https://web.dev/articles/rendering-on-the-web | UI-S01, ARCH-S24, CV-S08 | - |
| SRC-182 | T1 | HTML Living Standard, Server-sent events | WHATWG | https://html.spec.whatwg.org/multipage/server-sent-events.html | RT-S01 | - |

## T2

| id | tier | title | body | URL | replaces | note |
|---|---|---|---|---|---|---|
| SRC-183 | T2 | The Twelve-Factor App (index and factors read across slots) | A. Wiggins et al. (Heroku) | https://12factor.net/ | DATA-S29, APP-S25, UI-S21, SEC-S34, OPS-S19, ARCH-S07, TOPO-S24, TOPO-S25, TOPO-S26, TOPO-S27, WEB-S22 | one document read across pages: 12factor.net/, 12factor.net/admin-processes, 12factor.net/concurrency, 12factor.net/disposability, 12factor.net/port-binding, 12factor.net/, 12factor.net/backing-services, 12factor.net/build-release-run, 12factor.net/config |
| SRC-338 | T2 | Parse, don't validate | Alexis King | https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/ | DCON-S07 | - |
| SRC-339 | T2 | Feral Concurrency Control (SIGMOD 2015) | Bailis et al. | https://www.bailis.org/papers/feral-sigmod2015.pdf (PDF text extracted locally) | CONS-S19 | - |
| SRC-340 | T2 | Open Data Contract Standard (overview, fundamentals, schema pages) | Bitol / Linux Foundation | https://bitol-io.github.io/open-data-contract-standard/latest/ (and /fundamentals/, /schema/) | DCON-S11 | - |
| SRC-341 | T2 | Pattern: Saga | C. Richardson, microservices.io | https://microservices.io/patterns/data/saga.html | CONS-S12 | - |
| SRC-184 | T2 | Micro Frontends | Cam Jackson, martinfowler.com | https://martinfowler.com/articles/micro-frontends.html | CV-S11, WEB-S16 | - |
| SRC-185 | T2 | Hexagonal Architecture | Cockburn | alistair.cockburn.us/hexagonal-architecture/ | APP-S26, ARCH-S23 | - |
| SRC-186 | T2 | Parallel Change | D. Sato, M. Fowler | https://martinfowler.com/bliki/ParallelChange.html | DATA-S28, OPS-S23 | - |
| SRC-187 | T2 | DORA capabilities | DORA (Google Cloud) | https://dora.dev/capabilities/ | OPS-S31 | - |
| SRC-188 | T2 | Evolutionary Architecture (book site) | Ford, Parsons, Kua | https://evolutionaryarchitecture.com/ | ARCH-S12 | - |
| SRC-189 | T2 | Anemic Domain Model | Fowler | martinfowler.com/bliki/AnemicDomainModel.html | APP-S31 | - |
| SRC-190 | T2 | Blue Green Deployment | Fowler | https://martinfowler.com/bliki/BlueGreenDeployment.html | OPS-S24 | - |
| SRC-191 | T2 | Contract Test | Fowler | https://martinfowler.com/bliki/ContractTest.html | OPS-S22, DCON-S10 | - |
| SRC-192 | T2 | Deployment Pipeline | Fowler | https://martinfowler.com/bliki/DeploymentPipeline.html | OPS-S25 | - |
| SRC-193 | T2 | Domain Model (PoEAA) | Fowler | martinfowler.com/eaaCatalog/domainModel.html | APP-S33 | - |
| SRC-194 | T2 | Monolith First | Fowler | martinfowler.com/bliki/MonolithFirst.html | APP-S29, ARCH-S01, CV-S03 | - |
| SRC-195 | T2 | OrmHate | Fowler | martinfowler.com/bliki/OrmHate.html | APP-S30 | - |
| SRC-196 | T2 | Repository (PoEAA) | Fowler | martinfowler.com/eaaCatalog/repository.html | APP-S34 | - |
| SRC-197 | T2 | Service Layer (PoEAA) | Fowler | martinfowler.com/eaaCatalog/serviceLayer.html | APP-S27 | - |
| SRC-198 | T2 | Test Pyramid | Fowler | https://martinfowler.com/bliki/TestPyramid.html | OPS-S21 | - |
| SRC-199 | T2 | Transaction Script (PoEAA) | Fowler | martinfowler.com/eaaCatalog/transactionScript.html | APP-S32 | - |
| SRC-200 | T2 | Unit of Work (PoEAA) | Fowler | martinfowler.com/eaaCatalog/unitOfWork.html | APP-S28 | - |
| SRC-201 | T2 | Two Hard Things | Fowler (attributing Karlton) | https://martinfowler.com/bliki/TwoHardThings.html | OPS-S34 | - |
| SRC-202 | T2 | Microservices (article) | Fowler and Lewis | https://martinfowler.com/articles/microservices.html | ARCH-S03, CV-S05 | - |
| SRC-203 | T2 | Google API Improvement Proposals: AIP-121, 151, 154, 155, 158, 180, 185, 193 | Google | https://google.aip.dev/ (each /NNN page read) | API-S17, CONS-S21 | - |
| SRC-204 | T2 | Site Reliability Engineering (book, ch. 4, 6, 8, 9 and Handling Overload) | Google SRE | https://sre.google/sre-book/ | APP-S39, OPS-S28, OPS-S29, OPS-S30, ARCH-S29 | one document read across pages: sre.google/sre-book/monitoring-distributed-systems/, sre.google/sre-book/release-engineering/, sre.google/sre-book/service-level-objectives/, sre.google/sre-book/simplicity/, sre.google/sre-book/handling-overload/ |
| SRC-205 | T2 | The USE Method | Gregg | https://www.brendangregg.com/usemethod.html | OPS-S32 | - |
| SRC-206 | T2 | Feature Toggles | Hodgson, on martinfowler.com | https://martinfowler.com/articles/feature-toggles.html | OPS-S27 | - |
| SRC-207 | T2 | High Performance Browser Networking, latency primer | I. Grigorik | https://hpbn.co/primer-on-latency-and-bandwidth/ | WEB-S19 | - |
| SRC-342 | T2 | Consumer-Driven Contracts | Ian Robinson on martinfowler.com | https://martinfowler.com/articles/consumerDrivenContracts.html | DCON-S09 | - |
| SRC-208 | T2 | draft-ietf-httpapi-idempotency-key-header-07 (Internet-Draft, expired 2026-04-18) | IETF HTTPAPI WG | https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html | API-S11, CONS-S10 | tier set to T2: Internet-Draft (expired -07): T2 under the round-2 rule |
| SRC-209 | T2 | RateLimit header fields for HTTP | IETF HTTPAPI working group | https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ | RATE-S01 | Internet-Draft, -11, active, expires 2026-11-24 |
| SRC-210 | T2 | OAuth 2.0 for Browser-Based Applications (draft version; header says later published as RFC 10017, not read) | IETF OAuth WG | https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps | API-S12, SEC-S07 | tier set to T2: Internet-Draft; its published form is RFC 10017 (separate entry, T1) |
| SRC-211 | T2 | Resilient Web Design (ch. 2, 4, 5) | J. Keith | https://resilientwebdesign.com/ | UI-S23, WEB-S05, WEB-S06 | one document read across pages: resilientwebdesign.com/chapter2/, resilientwebdesign.com/chapter4/, resilientwebdesign.com/chapter5/ |
| SRC-212 | T2 | Response Times: The 3 Important Limits | J. Nielsen, 1993 | https://www.nngroup.com/articles/response-times-3-important-limits/ | WEB-S20 | - |
| SRC-343 | T2 | Jepsen analysis: PostgreSQL 12.3 | Jepsen (K. Kingsbury) | https://jepsen.io/analyses/postgresql-12.3 | CONS-S17 | - |
| SRC-213 | T2 | Local-First Software | Kleppmann, Wiggins, van Hardenberg, McGranaghan (Ink & Switch, 2019) | https://www.inkandswitch.com/essay/local-first/ | CV-S12 | - |
| SRC-214 | T2 | Knuth, "Structured Programming with go to Statements" (1974), passage read as reproduced in a blog post | Knuth; copy at probablydance.com | https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/ | OPS-S33 | - |
| SRC-215 | T2 | Application Database | M. Fowler | https://martinfowler.com/bliki/ApplicationDatabase.html | DATA-S27 | - |
| SRC-216 | T2 | Integration Database | M. Fowler | https://martinfowler.com/bliki/IntegrationDatabase.html | DATA-S26, ARCH-S30 | - |
| SRC-344 | T2 | Optimistic Offline Lock (PoEAA) | M. Fowler | https://www.martinfowler.com/eaaCatalog/optimisticOfflineLock.html | CONS-S14 | - |
| SRC-345 | T2 | Pessimistic Offline Lock (PoEAA) | M. Fowler | https://www.martinfowler.com/eaaCatalog/pessimisticOfflineLock.html | CONS-S15 | - |
| SRC-217 | T2 | Presentation Domain Data Layering | M. Fowler | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | UI-S20, ARCH-S08 | - |
| SRC-218 | T2 | Richardson Maturity Model | M. Fowler | https://martinfowler.com/articles/richardsonMaturityModel.html | API-S15 | - |
| SRC-219 | T2 | Tolerant Reader | M. Fowler | https://martinfowler.com/bliki/TolerantReader.html | API-S16, DCON-S08 | - |
| SRC-220 | T2 | Evolutionary Database Design | M. Fowler, P. Sadalage | https://martinfowler.com/articles/evodb.html | DATA-S25, OPS-S26, ARCH-S31 | - |
| SRC-346 | T2 | How to do distributed locking | M. Kleppmann | https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html | CONS-S16 | - |
| SRC-221 | T2 | Architecture Decision Record | Martin Fowler | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | ARCH-S06 | - |
| SRC-222 | T2 | Audit Log (Patterns of Enterprise Application Architecture, further development) | Martin Fowler | https://www.martinfowler.com/eaaDev/AuditLog.html | THIN-S18 | - |
| SRC-223 | T2 | Bounded Context | Martin Fowler | https://martinfowler.com/bliki/BoundedContext.html | ARCH-S17 | - |
| SRC-224 | T2 | Domain Logic and SQL | Martin Fowler | https://martinfowler.com/articles/dblogic.html | THIN-S19 | - |
| SRC-225 | T2 | Is High Quality Software Worth the Cost? | Martin Fowler | https://martinfowler.com/articles/is-quality-worth-cost.html | ARCH-S14 | - |
| SRC-226 | T2 | Microservice Premium | Martin Fowler | https://martinfowler.com/bliki/MicroservicePremium.html | ARCH-S02, CV-S04 | - |
| SRC-227 | T2 | Sacrificial Architecture | Martin Fowler | https://martinfowler.com/bliki/SacrificialArchitecture.html | ARCH-S11 | - |
| SRC-228 | T2 | Software Architecture Guide | Martin Fowler | https://martinfowler.com/architecture/ | ARCH-S15 | - |
| SRC-229 | T2 | Strangler Fig Application | Martin Fowler | https://martinfowler.com/bliki/StranglerFigApplication.html | ARCH-S21 | - |
| SRC-230 | T2 | Technical Debt Quadrant | Martin Fowler | https://martinfowler.com/bliki/TechnicalDebtQuadrant.html | ARCH-S27 | - |
| SRC-231 | T2 | Yagni | Martin Fowler | https://martinfowler.com/bliki/Yagni.html | ARCH-S13 | - |
| SRC-232 | T2 | Please stop calling databases CP or AP (2015) | Martin Kleppmann | https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html | CV-S25 | - |
| SRC-233 | T2 | Rethinking caching in web apps (2012) | Martin Kleppmann | https://martin.kleppmann.com/2012/10/01/rethinking-caching-in-web-apps.html | CV-S22 | - |
| SRC-234 | T2 | Schema evolution in Avro, Protocol Buffers and Thrift (2012) | Martin Kleppmann | https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html | CV-S23 | - |
| SRC-235 | T2 | Using logs to build a solid data infrastructure (2015) | Martin Kleppmann | https://martin.kleppmann.com/2015/05/27/logs-for-data-infrastructure.html | CV-S24 | - |
| SRC-236 | T2 | How Do Committees Invent? | Melvin Conway | https://www.melconway.com/Home/Committees_Paper.html | ARCH-S22 | - |
| SRC-237 | T2 | Documenting Architecture Decisions | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | ARCH-S05 | - |
| SRC-238 | T2 | Azure REST API Guidelines | Microsoft | https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md | API-S19 | - |
| SRC-347 | T2 | Asynchronous Request-Reply pattern | Microsoft Azure Architecture Center | https://learn.microsoft.com/en-us/azure/architecture/patterns/async-request-reply | CONS-S20 | - |
| SRC-239 | T2 | Circuit Breaker pattern | Microsoft Azure Architecture Center | learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker | APP-S38 | - |
| SRC-240 | T2 | Retry pattern | Microsoft Azure Architecture Center | learn.microsoft.com/en-us/azure/architecture/patterns/retry | APP-S37 | - |
| SRC-241 | T2 | OpenAPI best practices (design-first) | OpenAPI Initiative | https://learn.openapis.org/best-practices.html | API-S20 | - |
| SRC-242 | T2 | SLSA v1.0 Build track levels | OpenSSF | https://slsa.dev/spec/v1.0/levels | SEC-S35 | - |
| SRC-348 | T2 | Life beyond Distributed Transactions: an Apostate's Opinion | Pat Helland (CIDR 2007) | https://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf (PDF text extracted locally) | CONS-S11 | - |
| SRC-243 | T2 | Architecture Patterns with Python (preface, ch. 2, 4, 6, 12) | Percival and Gregory | cosmicpython.com/book/ (preface, chapter_02, 04, 06, 12) | APP-S36 | - |
| SRC-244 | T2 | Architectural Styles and the Design of Network-based Software Architectures (dissertation, ch. 4, 5, 6) | R. Fielding | https://ics.uci.edu/~fielding/pubs/dissertation/ | API-S13, UI-S22, ARCH-S18, ARCH-S19, WEB-S01, WEB-S02, WEB-S03 | one document read across pages: ics.uci.edu/~fielding/pubs/dissertation/evaluation.htm, ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm, ics.uci.edu/~fielding/pubs/dissertation/web_arch_domain.htm, www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm, www.ics.uci.edu/~fielding/pubs/dissertation/web_arch_domain.htm |
| SRC-245 | T2 | REST APIs must be hypertext-driven | R. Fielding | https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven | API-S14, WEB-S04 | - |
| SRC-246 | T2 | Transactional outbox | Richardson, microservices.io | microservices.io/patterns/data/transactional-outbox.html | APP-S35, CONS-S13 | - |
| SRC-247 | T2 | Backends For Frontends | S. Newman | https://samnewman.io/patterns/architectural/bff/ | WEB-S17 | - |
| SRC-248 | T2 | Microservices For Greenfield? (April 2015) | Sam Newman | https://samnewman.io/blog/2015/04/07/microservices-for-greenfield/ | CV-S02 | - |
| SRC-249 | T2 | Don't start with a monolith (June 2015) | Stefan Tilkov, hosted on martinfowler.com | https://www.martinfowler.com/articles/dont-start-monolith.html | CV-S01 | - |
| SRC-250 | T2 | Cool URIs don't change | T. Berners-Lee, 1998 | https://www.w3.org/Provider/Style/URI | WEB-S09 | - |
| SRC-251 | T2 | The Practical Test Pyramid | Vocke, on martinfowler.com | https://martinfowler.com/articles/practical-test-pyramid.html | OPS-S20 | - |
| SRC-349 | T2 | Eventually Consistent | W. Vogels | https://www.allthingsdistributed.com/2008/12/eventually_consistent.html | CONS-S18 | - |
| SRC-252 | T2 | Ethical Web Principles (W3C TAG statement, 12 Dec 2024, non-normative) | W3C TAG | https://www.w3.org/2001/tag/doc/ethical-web-principles/ | WEB-S08 | - |
| SRC-253 | T2 | Web Platform Design Principles (W3C Group Note, status as shown on page: 14 September 2026) | W3C TAG | https://www.w3.org/TR/design-principles/ | WEB-S07 | - |
| SRC-254 | T2 | A Simple Guide to Five Normal Forms in Relational Database Theory (CACM 26(2), 1983) | William Kent | https://www.bkent.net/Doc/simple5.htm (author's copy) | THIN-S20 | - |
| SRC-255 | T2 | Zalando RESTful API Guidelines | Zalando | https://opensource.zalando.com/restful-api-guidelines/ | API-S18 | - |

## T3

| id | tier | title | body | URL | replaces | note |
|---|---|---|---|---|---|---|
| SRC-256 | T3 | Architectural Decision Records | ADR GitHub organization | https://adr.github.io/ | ARCH-S33 | - |
| SRC-257 | T3 | Cookies vs Tokens: the definitive guide | Auth0 blog | https://auth0.com/blog/cookies-vs-tokens-definitive-guide/ | CV-S21 | - |
| SRC-258 | T3 | Token storage | Auth0 documentation | https://auth0.com/docs/secure/security-guidance/data-security/token-storage | CV-S17 | - |
| SRC-259 | T3 | AWS docs, ALB attributes | AWS | https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-load-balancer-attributes.html | RT-S20 | - |
| SRC-260 | T3 | Amazon S3: multipart upload overview | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html | UPLOAD-S09 | - |
| SRC-261 | T3 | Amazon S3: POST policy conditions | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html (read as extract) | UPLOAD-S08 | - |
| SRC-262 | T3 | Amazon S3: presigned URLs and uploading with them | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html and .../PresignedUrlUploadObject.html | UPLOAD-S07 | - |
| SRC-263 | T3 | GuardDuty Malware Protection for S3: how it works; tag-based access control | AWS docs | https://docs.aws.amazon.com/guardduty/latest/ug/how-malware-protection-for-s3-gdu-works.html and .../tag-based-access-s3-malware-protection.html | UPLOAD-S10 | - |
| SRC-264 | T3 | Code in the database vs the app (fragment) | B. Leach | https://www.brandur.org/fragments/code-database-vs-app | DATA-S34 | - |
| SRC-265 | T3 | Soft deletion probably isn't worth it | B. Leach | https://brandur.org/soft-deletion | DATA-S32, THIN-S21 | - |
| SRC-266 | T3 | Transactionally staged job drains in Postgres | B. Leach | https://brandur.org/job-drain | DATA-S33, APP-S41, CONS-S23 | - |
| SRC-267 | T3 | Implementing Stripe-like Idempotency Keys in Postgres | Brandur Leach | brandur.org/idempotency-keys | APP-S40, CONS-S22 | - |
| SRC-268 | T3 | Monolithic architecture pattern | Chris Richardson, microservices.io | https://microservices.io/patterns/monolithic.html | CV-S06 | - |
| SRC-269 | T3 | Page Lifecycle API | Chrome developers (single vendor) | https://developer.chrome.com/docs/web-platform/page-lifecycle-api | WEB-S15 | - |
| SRC-270 | T3 | Rate limiting best practices | Cloudflare docs | https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/ | RATE-S17 | - |
| SRC-271 | T3 | Choose Boring Technology | Dan McKinley (talk) | https://boringtechnology.club/ | ARCH-S04 | - |
| SRC-272 | T3 | The Majestic Monolith | David Heinemeier Hansson | https://signalvnoise.com/svn3/the-majestic-monolith/ | ARCH-S09 | - |
| SRC-273 | T3 | Outbox Event Router | Debezium | debezium.io/documentation/reference/stable/transformations/outbox-event-router.html | APP-S42 | - |
| SRC-274 | T3 | Django REST framework: Throttling | DRF maintainers | https://www.django-rest-framework.org/api-guide/throttling/ | RATE-S12 | - |
| SRC-275 | T3 | BFF documentation | Duende Software | https://docs.duendesoftware.com/bff/ | CV-S19 | - |
| SRC-276 | T3 | GitHub REST API versions | GitHub | https://docs.github.com/en/rest/about-the-rest-api/api-versions | API-S23 | - |
| SRC-277 | T3 | Rate limits for the REST API | GitHub docs | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | RATE-S16 | - |
| SRC-278 | T3 | Migration style guide | GitLab development docs | https://docs.gitlab.com/ee/development/migration_style_guide.html | DATA-S31 | - |
| SRC-279 | T3 | JavaScript SEO basics | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | UI-S32 | - |
| SRC-280 | T3 | Just Say No to More End-to-End Tests | Google Testing Blog | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | OPS-S35 | - |
| SRC-281 | T3 | GraphQL: best practices index and schema design (avoiding versioning) | GraphQL Foundation | https://graphql.org/learn/best-practices/ and https://graphql.org/learn/schema-design/ | API-S24 | - |
| SRC-282 | T3 | Hypermedia Systems, ch. 1 | Gross, Stepinski, Akşimşek (htmx authors) | https://hypermedia.systems/hypermedia-a-reintroduction/ | UI-S24 | - |
| SRC-283 | T3 | Heroku Dev Center, HTTP routing | Heroku | https://devcenter.heroku.com/articles/http-routing | RT-S21 | - |
| SRC-284 | T3 | Turbo Handbook: Introduction | Hotwire / 37signals | https://turbo.hotwired.dev/handbook/introduction | API-S28, UI-S25 | - |
| SRC-285 | T3 | How did REST come to mean the opposite of REST | htmx maintainers | https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/ | API-S27 | - |
| SRC-286 | T3 | htmx docs | htmx maintainers | https://htmx.org/docs/ | RT-S19 | - |
| SRC-287 | T3 | Hypermedia-Driven Applications | htmx maintainers | https://htmx.org/essays/hypermedia-driven-applications/ | API-S25 | - |
| SRC-288 | T3 | When Is Hypermedia a Good Fit | htmx maintainers | https://htmx.org/essays/when-to-use-hypermedia/ | API-S26, UI-S26, CV-S15 | - |
| SRC-350 | T3 | Jepsen: Postgres | K. Kingsbury (aphyr.com, 2013) | https://aphyr.com/posts/282-jepsen-postgres | CONS-S25 | - |
| SRC-289 | T3 | Frequently asked questions | Let's Encrypt | letsencrypt.org/docs/faq/ | TOPO-S28 | - |
| SRC-290 | T3 | Version Skew | M. Ubl, 2023 | https://industrialempathy.com/posts/version-skew | WEB-S18 | - |
| SRC-291 | T3 | Database normalization description (archived support article) | Microsoft Learn | https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description | THIN-S22 | - |
| SRC-292 | T3 | Server and Client Components | Next.js docs | https://nextjs.org/docs/app/getting-started/server-and-client-components | UI-S30 | - |
| SRC-293 | T3 | Static exports | Next.js docs | https://nextjs.org/docs/app/guides/static-exports | UI-S31 | - |
| SRC-294 | T3 | Sam Newman on moving from monolith systems to microservices | O'Reilly interview | https://oreilly.com/ideas/sam-newman-on-moving-from-monolith-systems-to-microservices | CV-S07 | - |
| SRC-351 | T3 | Ordering in Postgres outbox | O. Dudycz | https://event-driven.io/en/ordering_in_postgres_outbox/ | CONS-S24 | - |
| SRC-352 | T3 | oasdiff README | oasdiff README | https://github.com/oasdiff/oasdiff | DCON-S17 | - |
| SRC-353 | T3 | openapi-typescript docs | openapi-typescript docs | https://openapi-ts.dev/introduction | DCON-S18 | - |
| SRC-354 | T3 | Pact docs: how Pact works | Pact docs: how Pact works | https://docs.pact.io/getting_started/how_pact_works | DCON-S16 | - |
| SRC-295 | T3 | Pact documentation (introduction) | Pact Foundation (tool vendor, interested party) | https://docs.pact.io/ | OPS-S36, DCON-S15 | - |
| SRC-296 | T3 | Islands Architecture | patterns.dev | https://www.patterns.dev/vanilla/islands-architecture/ | UI-S33 | - |
| SRC-297 | T3 | pgBackRest user guide | pgBackRest maintainers | https://pgbackrest.org/user-guide.html | DATA-S35 | - |
| SRC-298 | T3 | PgDog docs, pub/sub in transaction mode | PgDog | https://docs.pgdog.dev/features/connection-pooler/pub_sub/ | RT-S24 | - |
| SRC-299 | T3 | LocalStorage and XSS (token storage) | Philippe De Ryck, Pragmatic Web Security | https://pragmaticwebsecurity.com/articles/oauthoidc/localstorage-xss.html | CV-S18 | - |
| SRC-300 | T3 | Don't Do This | PostgreSQL community wiki | https://wiki.postgresql.org/wiki/Don't_Do_This | DATA-S37 | - |
| SRC-301 | T3 | Number of Database Connections | PostgreSQL community wiki | https://wiki.postgresql.org/wiki/Number_Of_Database_Connections | DATA-S38 | - |
| SRC-355 | T3 | PostgREST docs: Schema Isolation (read from source copy on GitHub; docs host returned 429) | PostgREST docs: Schema Isolation (read from source copy on GitHub; docs host returned 429) | https://raw.githubusercontent.com/PostgREST/postgrest-docs/main/docs/explanations/schema_isolation.rst | DCON-S14 | - |
| SRC-356 | T3 | Pydantic docs: JSON Schema | Pydantic docs: JSON Schema | https://pydantic.dev/docs/validation/latest/concepts/json_schema/ | DCON-S12 | - |
| SRC-357 | T3 | Pydantic docs: Strict Mode | Pydantic docs: Strict Mode | https://pydantic.dev/docs/validation/latest/concepts/strict_mode/ | DCON-S13 | - |
| SRC-302 | T3 | Railway guides, Choose between SSE and WebSockets | Railway | https://docs.railway.com/guides/sse-vs-websockets | RT-S22 | - |
| SRC-303 | T3 | Why JWTs suck as session tokens (Aug 2017) | Randall Degges, Okta developer blog | https://developer.okta.com/blog/2017/08/17/why-jwts-suck-as-session-tokens | CV-S16 | - |
| SRC-304 | T3 | Choosing the State Structure | React docs | https://react.dev/learn/choosing-the-state-structure | UI-S28 | - |
| SRC-305 | T3 | React Server Components | React docs | https://react.dev/reference/rsc/server-components | UI-S29 | - |
| SRC-306 | T3 | Build a React app from scratch | React documentation | https://react.dev/learn/build-a-react-app-from-scratch | CV-S10 | tier set to T3: front-end framework docs, harmonized with the other React and Next.js pages ranked T3 by UI (CV ranked T1) |
| SRC-307 | T3 | Postgres LISTEN/NOTIFY does not scale (postmortem) | Recall.ai engineering | https://www.recall.ai/blog/postgres-listen-notify-does-not-scale | RT-S23 | - |
| SRC-358 | T3 | SQLModel docs | Sebastian Ramirez | https://sqlmodel.tiangolo.com/ | DCON-S19 | - |
| SRC-308 | T3 | Deconstructing the Monolith | Shopify Engineering | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity | ARCH-S10 | - |
| SRC-309 | T3 | APIs as infrastructure: future-proofing Stripe with versioning | Stripe | https://stripe.com/blog/api-versioning | API-S22 | - |
| SRC-310 | T3 | Stripe docs: Idempotent requests | Stripe | https://docs.stripe.com/api/idempotent_requests | API-S21 | - |
| SRC-311 | T3 | Online migrations at scale | Stripe Engineering | https://stripe.com/blog/online-migrations | DATA-S30 | - |
| SRC-312 | T3 | Scaling your API with rate limiters | Stripe engineering | https://stripe.com/blog/rate-limiters | RATE-S15 | - |
| SRC-313 | T3 | TanStack Query overview | TanStack maintainers | https://tanstack.com/query/latest/docs/framework/react/overview | UI-S27 | - |
| SRC-314 | T3 | Fitness function-driven development | Thoughtworks | https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development | ARCH-S32 | - |
| SRC-315 | T3 | Goodbye Microservices | Twilio Segment | https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices/ (redirect from segment.com) | ARCH-S16 | - |
| SRC-316 | T3 | WhiteNoise documentation | WhiteNoise maintainers | whitenoise.readthedocs.io/en/latest/ | TOPO-S29 | - |

## T4

| id | tier | title | body | URL | replaces | note |
|---|---|---|---|---|---|---|
| SRC-317 | T4 | WebSocket vs SSE | Ably (commercial real-time vendor, author is its CEO) | https://websocket.org/comparisons/sse/ | RT-S25 | - |
| SRC-318 | T4 | A response to Rich Harris (htmx 4.0 essays) | htmx authors | https://four.htmx.org/essays/a-response-to-rich-harris | CV-S14 | - |
| SRC-319 | T4 | The Website vs. Web App Dichotomy Doesn't Exist | Jake Lazaroff | https://jakelazaroff.com/words/the-website-vs-web-app-dichotomy-doesnt-exist/ | CV-S13 | - |
| SRC-320 | T4 | Postgres for Everything | Stephan Schmidt (amazingcto) | https://www.amazingcto.com/postgres-for-everything/ | ARCH-S25 | - |
| SRC-321 | T4 | Second-guessing the modern web (SPA fatigue) | T. MacWright | https://macwright.com/2020/05/10/spa-fatigue | UI-S34 | - |
| SRC-322 | T4 | How to Collapse Your Stack Using PostgreSQL | Tiger Data (vendor, commercial interest) | https://www.tigerdata.com/blog/how-to-collapse-your-stack-using-postgresql-for-everything/ | ARCH-S26 | - |
| SRC-323 | T4 | Business logic in database vs application search results | various | search snippets only, not fetched | DATA-S40 | - |
| SRC-324 | T4 | PostgreSQL audit approaches search results | various | search snippets only, not fetched | DATA-S41 | - |
| SRC-325 | T4 | UUIDv7 vs bigint search results (benchmark and blog posts, e.g. ardentperf.com UUID benchmark post) | various | search snippets only, not fetched | DATA-S39 | - |
| SRC-326 | T4 | Fallacies of distributed computing (encyclopedia copy; originals by Deutsch and Gosling not read) | Wikipedia | https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing | WEB-S21 | - |
| SRC-327 | T4 | Post/Redirect/Get | Wikipedia | https://en.wikipedia.org/wiki/Post/Redirect/Get | UI-S35 | - |

## Maintainer source (not citable)

| id | tier | title | body | URL | replaces | note |
|---|---|---|---|---|---|---|
| MAINT-S01 | maintainer | maintainer's codified practice (private codebase, not citable) | maintainer | none (private, not a fetch) | MAINT-S01 | the maintainer's codified practice; carries the maintainer's authority for one context; never cited in public text beyond this id |

