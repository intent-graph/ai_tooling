# Research result: rate limiting and abuse (RATE), file uploads and object storage (UPLOAD)

## L1 headline

Best practice is well settled on the mechanics (bound every resource a client can consume, return 429, key limits on more than the IP, validate and isolate uploaded files, keep metadata in the database and bytes in object storage) and thin on the choices that matter most (where to place limits, direct-to-storage versus through-the-app uploads, header names); certainty is grounded for rules read in T1 sources and inferred for the placement and lifecycle syntheses.

Pinned:
- Sources by tier: T1 16, T2 1, T3 10, T4 0 (27 sources in total).
- Claims: 34 (RATE-C01 to RATE-C19, UPLOAD-C01 to UPLOAD-C15).
- Contested: rate-limit header names (RateLimit draft vs X-RateLimit-* vs none); direct-to-object-storage vs through-the-app uploads.
- Failed T1 fetch: none. The OWASP API pages redirected and were read at the new host; the OWASP community "Unrestricted File Upload" page redirected and was not read; the RateLimit headers spec is still an Internet-Draft (-11, T2), expiring 2026-11-24 in the copy read.

## L2 claims

Pinned:
- Sources by tier: T1 16, T2 1, T3 10, T4 0 (27 sources in total).
- Claims: 34 (RATE-C01 to RATE-C19, UPLOAD-C01 to UPLOAD-C15).
- Contested: rate-limit header names (RateLimit draft vs X-RateLimit-* vs none); direct-to-object-storage vs through-the-app uploads.
- Failed T1 fetch: none. The OWASP API pages redirected and were read at the new host; the OWASP community "Unrestricted File Upload" page redirected and was not read; the RateLimit headers spec is still an Internet-Draft (-11, T2), expiring 2026-11-24 in the copy read.

Clusters (agreement, certainty, claim ids):

1. Bound everything a client can make the server consume (requests, bytes, concurrency, time, third-party spend), tuned per operation; costly operations get tighter limits and spending caps. Consensus, grounded. RATE-C01, C02, C09.
2. Limits are layered: coarse, cheap limits and size and time bounds at the proxy or edge, identity-aware limits in the application. Majority on the split, inferred; consensus on bounds at the edge, grounded. RATE-C03, C18, C19.
3. Identify the client carefully: use only IPs added by a trusted proxy, and key on account, API key or session as well, because IP-only fails behind shared addresses and against distributed attacks. Consensus, grounded. RATE-C04, C05.
4. Signal limits in HTTP: 429 (never cached, Retry-After optional); quota headers are only an IETF draft and the de facto names differ; clients must not read remaining quota as a guarantee. Consensus on 429, contested on header names, grounded. RATE-C06, C07, C08.
5. Operate limiters like production features: shared state across processes, dry-run first, kill switch, concurrency limits and load shedding for overload. Majority (mostly one T3 practitioner source), grounded. RATE-C10, C11, C12.
6. Framework throttling in Python is not a security control: Django does not throttle logins, DRF says its throttling is not protection against brute force. Consensus, grounded. RATE-C13, C19.
7. Login and business-flow abuse: account-keyed throttling, lockout that cannot be turned into denial of service, layered credential-stuffing defense with MFA first, protection of sensitive business flows. Consensus, grounded (boundary: SEC). RATE-C14, C15, C16, C17.
8. Uploaded files are untrusted input: never trust client name, type or extension; allowlist, size and name limits, authenticated and CSRF-protected endpoint; store outside the web root and serve through a handler. Consensus, grounded. UPLOAD-C05, C06, C07, C15.
9. Direct-to-storage upload with short-lived presigned URLs or POST policies versus streaming through the app; direct upload needs server-chosen keys, short expiry, policy constraints, multipart for large files. Contested; mechanics grounded in vendor docs, the choice criteria inferred. UPLOAD-C01, C02, C03, C04.
10. Scan uploads for malware and keep them unreadable until the scan is clean; track upload state in Postgres. Majority on mechanism, grounded for scanning, inferred for the state machine. UPLOAD-C08, C09, C10.
11. Metadata in Postgres, bytes in object storage (bytea capped at 1 GB per value). Majority, partly inferred. UPLOAD-C11.
12. Serve user content safely: distinct registrable domain, correct Content-Type with nosniff, attachment disposition, signed short-lived URLs for private content. Consensus on headers and domain, grounded; signed GET inferred. UPLOAD-C12, C13, C14.

Live debates:
- Header names for quota signalling: IETF draft RateLimit and RateLimit-Policy (-11, still a draft) vs GitHub-style x-ratelimit-* vs no headers (RATE-C07).
- Direct-to-object-storage vs through-the-app uploads: vendor docs describe direct upload, OWASP and framework docs assume the app receives the file; neither side argues the trade-off (UPLOAD-C01).
- Where limits live (proxy vs app): both layers recommended by different sources; Django points to the web server, Stripe implements in app middleware (RATE-C03).

Not covered: CAPTCHA and bot-management products in depth; ASVS requirements; resumable-upload protocols (tus and its IETF draft); image and document processing hazards (polyglot files, decompression bombs beyond one line); CDN signed URLs and cache behaviour for media; GCS and Azure equivalents; Postgres large objects; whether a presigned PUT can enforce a size limit (not verified); an independent T1/T2 source arguing direct vs proxied upload; GDPR deletion of stored files (deferred by the brief).

## L3 full

Pinned:
- Sources by tier: T1 16, T2 1, T3 10, T4 0 (27 sources in total).
- Claims: 34 (RATE-C01 to RATE-C19, UPLOAD-C01 to UPLOAD-C15).
- Contested: rate-limit header names (RateLimit draft vs X-RateLimit-* vs none); direct-to-object-storage vs through-the-app uploads.
- Failed T1 fetch: none. The OWASP API pages redirected and were read at the new host; the OWASP community "Unrestricted File Upload" page redirected and was not read; the RateLimit headers spec is still an Internet-Draft (-11, T2), expiring 2026-11-24 in the copy read.

Note on method: pages were fetched through a tool that returns a model-made extract of the page with quotes; quotes below are as returned. Where a first fetch returned nothing (AWS GuardDuty landing page) another page of the same documentation was read.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| RATE-S01 | T2 (Internet-Draft, -11, active, expires 2026-11-24) | RateLimit header fields for HTTP | IETF HTTPAPI working group | https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ | RateLimit and RateLimit-Policy fields, quota units, client behavior |
| RATE-S02 | T1 | RFC 6585, section 4 (429 Too Many Requests) | IETF | https://www.rfc-editor.org/rfc/rfc6585.html | status 429 semantics |
| RATE-S03 | T1 | RFC 9110, 15.5.14 (413) and 10.2.3 (Retry-After) | IETF | https://www.rfc-editor.org/rfc/rfc9110.html (read as extract) | 413, Retry-After |
| RATE-S04 | T1 | OWASP API4:2023 Unrestricted Resource Consumption | OWASP | https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption | resource limits, spending limits |
| RATE-S05 | T1 | OWASP API6:2023 Unrestricted Access to Sensitive Business Flows | OWASP | https://api-security.owasp.org/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows | automated abuse of business flows |
| RATE-S06 | T1 | Credential Stuffing Prevention Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html | layered defense, limits of IP throttling |
| RATE-S07 | T1 | Authentication Cheat Sheet (lockout and throttling section) | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html | login throttling, lockout DoS |
| RATE-S08 | T1 | Denial of Service Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html | application-level DoS controls and where to apply them |
| RATE-S09 | T1 | Django: Security in Django (user-uploaded content, throttling) | Django project | https://docs.djangoproject.com/en/stable/topics/security/ | request body limits, separate domain, no built-in login throttle |
| RATE-S10 | T1 | Django settings reference (upload and data size settings) | Django project | https://docs.djangoproject.com/en/stable/ref/settings/ | DATA_UPLOAD_MAX_MEMORY_SIZE, FILE_UPLOAD_MAX_MEMORY_SIZE |
| RATE-S11 | T1 | MDN: X-Forwarded-For | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-For | trusting forwarded IPs for rate limiting |
| RATE-S12 | T3 | Django REST framework: Throttling | DRF maintainers | https://www.django-rest-framework.org/api-guide/throttling/ | DRF throttling semantics and stated limits |
| RATE-S13 | T3 | nginx ngx_http_limit_req_module | nginx project | https://nginx.org/en/docs/http/ngx_http_limit_req_module.html | proxy-level request limiting, dry run |
| RATE-S14 | T3 | nginx core module: client_max_body_size, client_body_timeout | nginx project | https://nginx.org/en/docs/http/ngx_http_core_module.html#client_max_body_size | proxy-level body size and read timeout |
| RATE-S15 | T3 | Scaling your API with rate limiters | Stripe engineering | https://stripe.com/blog/rate-limiters | four limiter types, rollout practice |
| RATE-S16 | T3 | Rate limits for the REST API | GitHub docs | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | x-ratelimit-* headers, client back-off |
| RATE-S17 | T3 | Rate limiting best practices | Cloudflare docs | https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/ | counting characteristics, failure-only counting, tiered escalation |
| UPLOAD-S01 | T1 | File Upload Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html | upload validation and storage rules |
| UPLOAD-S02 | T1 | Django: File Uploads; UploadedFile reference | Django project | https://docs.djangoproject.com/en/stable/topics/http/file-uploads/ and https://docs.djangoproject.com/en/stable/ref/files/uploads/ | upload handlers, untrusted content_type |
| UPLOAD-S03 | T1 | FastAPI: Request Files | FastAPI | https://fastapi.tiangolo.com/tutorial/request-files/ | bytes vs UploadFile, spooling |
| UPLOAD-S04 | T1 | MDN: X-Content-Type-Options | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options | nosniff |
| UPLOAD-S05 | T1 | MDN: Content-Disposition | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Disposition | inline vs attachment, filename |
| UPLOAD-S06 | T1 | PostgreSQL: TOAST | PostgreSQL project | https://www.postgresql.org/docs/current/storage-toast.html | 1 GB value limit (the bytea page read had no size information) |
| UPLOAD-S07 | T3 | Amazon S3: presigned URLs and uploading with them | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html and .../PresignedUrlUploadObject.html | presigned URL semantics, expiry, bearer nature |
| UPLOAD-S08 | T3 | Amazon S3: POST policy conditions | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html (read as extract) | content-length-range, key and type conditions |
| UPLOAD-S09 | T3 | Amazon S3: multipart upload overview | AWS docs | https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html | multipart, checksums, incomplete upload cleanup |
| UPLOAD-S10 | T3 | GuardDuty Malware Protection for S3: how it works; tag-based access control | AWS docs | https://docs.aws.amazon.com/guardduty/latest/ug/how-malware-protection-for-s3-gdu-works.html and .../tag-based-access-s3-malware-protection.html | event-driven upload scanning, quarantine by tag |

Vendor sources (AWS, nginx, Cloudflare, GitHub, Stripe) are T3 and name vendor features; claims drawn from them state the vendor-neutral rule and say so.

### Claims: RATE (rate limiting and abuse)

**RATE-C01**
- claim: Bound every resource a client can make the server consume (request rate, payload size, memory, concurrency, time, third-party spend) and tune each limit to the operation and the business need.
- level: principle | stack: neutral | sources: RATE-S04 (prevention list), RATE-S08 | agreement: consensus | certainty: grounded

**RATE-C02**
- claim: Give operations that cost money or trigger third parties (SMS, email, exports, uploads, storage egress) their own tighter per-client limits, and set spending limits and billing alerts with every external provider.
- level: practice | stack: neutral | sources: RATE-S04 (scenarios 1, 3; "configure spending limits"), RATE-S05 | agreement: consensus | certainty: grounded

**RATE-C03**
- claim: Apply limits in two layers: coarse, identity-blind limits and size and time bounds at the proxy or edge before the application spends work, and identity-aware limits (per user, per API key, per plan) in the application where identity is known.
- level: decision | stack: neutral | sources: RATE-S08 (controls "work best at infrastructure edges"), RATE-S13 (key-based limiting in the proxy), RATE-S15 (limiters in application middleware), RATE-S09 (Django: use a plugin or web server module) | agreement: majority | positions: proxy-only (Django security page points to the web server; nginx keys on IP or any variable); app-level (Stripe runs four limiters in middleware keyed on user); both (OWASP DoS sheet: edge for connection and bandwidth limits). No source argues the split explicitly. | certainty: inferred (my synthesis across these four)

**RATE-C04**
- claim: When limiting by IP behind proxies, use only addresses appended by a proxy you control (trusted proxy count or list, counted from the right of X-Forwarded-For); never the leftmost value.
- level: practice | stack: http | sources: RATE-S11 (security section), RATE-S12 (X-Forwarded-For plus NUM_PROXIES) | agreement: consensus | certainty: grounded

**RATE-C05**
- claim: Do not rely on the IP address alone as the limiting key: combine it with an account, API key, session cookie or path, because shared addresses and distributed attacks defeat per-IP counting.
- level: practice | stack: neutral | sources: RATE-S06 ("may defeat both IP block-lists and rate limiting"), RATE-S17 (counting characteristics), RATE-S07 (counter on the account) | agreement: consensus | certainty: grounded

**RATE-C06**
- claim: Reject over-limit requests with 429 Too Many Requests, a body explaining the condition, and a Retry-After header where the wait is known; never let a cache store a 429; set the proxy to 429 where its default is 503.
- level: practice | stack: http | sources: RATE-S02 (section 4), RATE-S13 (limit_req_status default 503), RATE-S12 (429, Retry-After via wait()) | agreement: consensus | certainty: grounded. RFC 6585 states it does not define how clients are identified or requests counted.

**RATE-C07**
- claim: Advertise remaining quota to clients with response headers, preferring the IETF RateLimit and RateLimit-Policy fields but treating them as unstable until the draft is published.
- level: decision | stack: http | sources: RATE-S01 (draft -11: RateLimit-Policy with q, qu, w, pk; RateLimit with r, t, pk), RATE-S16 (x-ratelimit-limit, -remaining, -used, -reset) | agreement: contested | positions: (a) IETF draft fields RateLimit and RateLimit-Policy, a draft and so T2 only, expires 2026-11-24 in the copy read; (b) de facto X-RateLimit-* names with reset as epoch seconds (GitHub); (c) no quota headers, only 429 and Retry-After (RFC 6585 baseline, Django REST framework). Pick (a) for new APIs if clients are first-party and can change; (b) where clients already expect it. | certainty: grounded on the facts, inferred on the recommendation

**RATE-C08**
- claim: Clients must treat remaining quota as advisory, never a guarantee, and honor Retry-After before any quota header; servers should not send a Retry-After earlier than the end of the effective window.
- level: practice | stack: http | sources: RATE-S01 (client behavior, Retry-After coordination), RATE-S16 (pause until reset; exponential back-off for secondary limits) | agreement: consensus | certainty: grounded

**RATE-C09**
- claim: Limit concurrent requests as well as request rate on CPU-heavy or long endpoints; request count, bytes and concurrency are distinct quota units.
- level: practice | stack: neutral | sources: RATE-S01 (quota units requests, content-bytes, concurrent-requests), RATE-S15 (concurrent requests limiter) | agreement: majority (one T2 draft, one T3 practitioner) | certainty: grounded

**RATE-C10**
- claim: Behind per-client limits, keep a load shedder that reserves capacity for critical requests and drops lower-priority traffic first when the fleet or the workers are overloaded.
- level: practice | stack: neutral | sources: RATE-S15 (fleet usage and worker utilization load shedders) | agreement: majority (single T3 source, no dissent found; consensus not claimed) | certainty: grounded

**RATE-C11**
- claim: Roll out a new limit in observe-only mode first, escalate gradually (challenge before block), and keep a switch to disable it.
- level: practice | stack: neutral | sources: RATE-S15 (dark launch, kill switches), RATE-S13 (limit_req_dry_run), RATE-S17 (tiered escalation) | agreement: majority | certainty: grounded

**RATE-C12**
- claim: Keep limiter state outside the individual application process (shared cache or the proxy), or accept that limits are approximate; a per-process in-memory store is adequate only for simple setups.
- level: practice | stack: neutral | sources: RATE-S15 (token bucket in Redis), RATE-S12 (LocMemCache "okay for simple setups"; race conditions under high concurrency), RATE-S13 (shared memory zone) | agreement: majority | certainty: grounded; link to the stateless-process principle is my inference

**RATE-C13**
- claim: Do not count on framework-level throttling as a security control: Django does not throttle authentication, and DRF states its throttling is not protection against brute force or denial of service; put the real limit in the proxy, a dedicated limiter or the login logic.
- level: practice | stack: python | sources: RATE-S09 (rate-limiting statement), RATE-S12 (limitations) | agreement: consensus | certainty: grounded

**RATE-C14**
- claim: Count failed logins against the account, not only the source IP, with delay or exponential backoff rather than a hard lockout, and keep a recovery path so an attacker cannot lock legitimate users out.
- level: practice | stack: neutral | sources: RATE-S07 | agreement: consensus | certainty: grounded | boundary: SEC

**RATE-C15**
- claim: Defend against credential stuffing in layers with MFA first, then breached-password checks, then device fingerprinting and CAPTCHA understood as spoofable and breakable, and never IP blocking alone.
- level: principle | stack: neutral | sources: RATE-S06, RATE-S05 (fingerprinting, human detection, non-human patterns, known proxies) | agreement: consensus | certainty: grounded | boundary: SEC (credential rules are SEC-C36 to C39)

**RATE-C16**
- claim: Identify the business flows whose automation harms the business (sign-up, purchase, booking, referral) and protect those specifically, including machine-to-machine APIs that lack browser-side defenses.
- level: principle | stack: neutral | sources: RATE-S05 | agreement: consensus | certainty: grounded

**RATE-C17**
- claim: For one-time-code and verification endpoints, count failed attempts only so that legitimate users submitting valid codes are not limited.
- level: practice | stack: neutral | sources: RATE-S17 | agreement: majority (single T3 source) | certainty: grounded

**RATE-C18**
- claim: Enforce a maximum request body size, a minimum read rate and read timeouts at the outermost layer, and return 413 or 408 there; also check size in the client, since browsers display the proxy's error poorly.
- level: principle | stack: http | sources: RATE-S04 ("maximum size of data on all incoming parameters and payloads"), RATE-S08 (minimum ingress rate, request-read timeouts, total request size), RATE-S14 (client_max_body_size default 1m returns 413; browsers cannot display it correctly; client_body_timeout 60 s returns 408), RATE-S03 (413 may close the connection) | agreement: consensus | certainty: grounded; the client-side check is my inference from the nginx note

**RATE-C19**
- claim: Set the body-size limit in the web server in addition to the framework, because Django's DATA_UPLOAD_MAX_MEMORY_SIZE (default 2.5 MB) excludes file data from the request.POST check and under ASGI the whole request may be spooled to disk before file validation.
- level: practice | stack: python | sources: RATE-S09 (user-uploaded content, form submission limits), RATE-S10 | agreement: consensus | certainty: grounded

### Claims: UPLOAD (files and object storage)

**UPLOAD-C01**
- claim: Decide per project whether bytes travel browser to object storage directly (the app authorizes and issues a short-lived credential) or through the app (the app streams, validates and stores); default to direct for large or numerous files and through-the-app for small files that need synchronous validation.
- level: decision | stack: neutral | sources: UPLOAD-S07 (upload without the uploader holding credentials), UPLOAD-S01 (written for an app that receives the file), UPLOAD-S02, UPLOAD-S03 (framework streaming) | agreement: contested | positions: direct to storage (cloud vendor documentation describes it as a capability, with the benefit that the uploader needs no credentials; the load-off-the-app benefit is my inference); through the app (OWASP and framework docs assume the app handles the file and give the validation rules). No source weighs the two. The size threshold in the claim is my judgment and is open. | certainty: inferred

**UPLOAD-C02**
- claim: For direct upload, treat the presigned URL as a bearer token: the server picks a random object key, grants one operation on one key, uses a short expiry, and authorizes the requester before issuing it.
- level: practice | stack: neutral (vendor docs: S3) | sources: UPLOAD-S07 ("bearer tokens"; usable many times until expiry; same key overwrites; limited by creator's permissions; SigV4 signatureAge condition) | agreement: majority (single vendor, rule is vendor-neutral by nature) | certainty: grounded on bearer and overwrite facts; "short expiry" and "random key" are my inference

**UPLOAD-C03**
- claim: When the storage layer must enforce limits on a browser upload, issue a POST policy with a content-length-range, an exact content type and a key prefix rather than an unconstrained URL.
- level: practice | stack: neutral (vendor docs: S3) | sources: UPLOAD-S08 | agreement: majority (single vendor) | certainty: grounded for what POST policies can enforce; I did not verify whether a presigned PUT can bound size

**UPLOAD-C04**
- claim: Use multipart or resumable upload for large files, verify integrity with checksums, and delete incomplete uploads with a lifecycle rule because their parts are billed until completed or aborted.
- level: practice | stack: neutral (vendor docs: S3) | sources: UPLOAD-S09 (best practice at 100 MB and above; no expiry of an initiated upload; AbortIncompleteMultipartUpload rule; checksums), UPLOAD-S07 (checksums on presigned uploads) | agreement: majority | certainty: grounded

**UPLOAD-C05**
- claim: Treat every part of an upload supplied by the client (filename, extension, Content-Type, charset) as untrusted: allowlist extensions, check the file's actual signature or content, and generate the stored name yourself.
- level: principle | stack: neutral | sources: UPLOAD-S01 (extension allowlist, "cannot be trusted", application-generated filename, signature validation), UPLOAD-S02 ("trust but verify"), UPLOAD-S05 (strip path from filename) | agreement: consensus | certainty: grounded

**UPLOAD-C06**
- claim: Put limits and gates on the upload endpoint: authenticated and authorized uploaders, a file size limit, a filename length limit, post-decompression size for archives, and CSRF protection.
- level: practice | stack: neutral | sources: UPLOAD-S01 | agreement: consensus | certainty: grounded

**UPLOAD-C07**
- claim: Store uploads outside the web root or on a different host, and if they must be publicly reachable, serve them through a handler that maps an identifier to the stored object rather than exposing a file path.
- level: practice | stack: neutral | sources: UPLOAD-S01 | agreement: consensus (one T1 source, no dissent) | certainty: grounded

**UPLOAD-C08**
- claim: Scan untrusted uploads with antivirus or a sandbox, and apply content disarm and reconstruction for document formats such as PDF and Office, before any other user can open them.
- level: decision | stack: neutral | sources: UPLOAD-S01 (antivirus or sandbox, CDR), UPLOAD-S10 | agreement: consensus on scanning, majority on mechanism | positions: OWASP names antivirus, sandbox and CDR generically; the only concrete mechanism read is a managed object-store scanner (S10). | certainty: grounded

**UPLOAD-C09**
- claim: For asynchronous scanning of objects in storage, make objects unreadable until the scan reports clean (tag-based access control) and design the consumer to receive duplicate scan results.
- level: practice | stack: neutral (vendor docs: S3 with GuardDuty) | sources: UPLOAD-S10 (scan starts on object creation; result tag values include NO_THREATS_FOUND, THREATS_FOUND, UNSUPPORTED, ACCESS_DENIED, FAILED; example policy denies reads unless tagged clean; at-least-once delivery; tagging must be enabled before the upload) | agreement: majority (single vendor) | certainty: grounded

**UPLOAD-C10**
- claim: Track each upload as a row in Postgres with an explicit state (pending when the URL is issued, available only after storage-side confirmation and a clean scan, failed or expired otherwise), and sweep rows and objects that never complete.
- level: practice | stack: postgres | sources: synthesis of UPLOAD-S07 (URL may be unused or reused), UPLOAD-S09 (incomplete uploads persist), UPLOAD-S10 (asynchronous, duplicate results) | agreement: majority (no source gives this state machine) | certainty: inferred

**UPLOAD-C11**
- claim: Keep file metadata (object key, owner, size, content type, checksum, state) in Postgres and the bytes in object storage; reserve bytea in Postgres for small files that must commit atomically with other data.
- level: decision | stack: postgres | sources: UPLOAD-S06 (a TOASTable value is limited to 1 GB), UPLOAD-S02, UPLOAD-S03 (frameworks stream files to disk or storage, not to the database) | agreement: majority | positions: metadata-in-database plus bytes-in-object-storage (assumed by the vendor and framework docs read); bytes-in-database (not argued in any source read; I did not find an authority for or against beyond the 1 GB limit). The database-bloat and backup-size reasons are not grounded in a read source. | certainty: grounded on the limit, inferred on the recommendation

**UPLOAD-C12**
- claim: Serve user-uploaded content from a distinct registrable domain, not a subdomain of the main site, so the same-origin policy contains any script in an upload.
- level: principle | stack: http | sources: RATE-S09 (Django: "distinct top-level or second-level domain ... not sufficient to serve from a subdomain"), UPLOAD-S01 (different host) | agreement: majority (one T1 states the domain rule; the other T1 says only "different host") | certainty: grounded

**UPLOAD-C13**
- claim: Serve uploads with a correct stored Content-Type, `X-Content-Type-Options: nosniff`, and `Content-Disposition: attachment` with a sanitized filename for anything not meant to render inline.
- level: practice | stack: http | sources: UPLOAD-S04 (nosniff prevents uploaded content from being executed as HTML; relies on a correct Content-Type), UPLOAD-S05 (inline vs attachment; strip path separators) | agreement: consensus | certainty: grounded

**UPLOAD-C14**
- claim: Serve private files through the application's authorization check, redirecting to a short-lived signed download URL instead of proxying the bytes or exposing a public bucket.
- level: practice | stack: neutral (vendor docs: S3) | sources: UPLOAD-S07 (presigned GET grants time-limited access; bearer token) | agreement: majority | certainty: inferred (the redirect pattern is my synthesis; the mechanism is grounded)

**UPLOAD-C15**
- claim: In the Python app, stream uploads rather than reading them whole: iterate Django's `chunks()` (files above 2.5 MB go to a temporary file) and use FastAPI `UploadFile` (spooled file) instead of `bytes`.
- level: practice | stack: python | sources: UPLOAD-S02, UPLOAD-S03, RATE-S10 (FILE_UPLOAD_MAX_MEMORY_SIZE) | agreement: consensus | certainty: grounded. FastAPI's page states no size limit.

### Gaps

- Open: no T1 or T2 source weighs direct-to-storage against through-the-app uploads (UPLOAD-C01); the size threshold is a judgment.
- Open: whether a presigned PUT can enforce a maximum size (only POST policy was read); equivalents on GCS and Azure; self-hosted S3-compatible stores.
- Not read: OWASP community Unrestricted File Upload page (redirect not followed); ASVS requirements; resumable-upload protocol tus and the IETF resumable-uploads draft; image-processing hazards (decompression bombs, polyglot files); CDN signed URLs and media caching; Postgres large objects; django-ratelimit and similar libraries; Cloudflare/Turnstile-type bot management beyond one page; RFC 9110 and the S3 POST policy page were read as extracts only.
- Deferred by the brief: GDPR erasure of stored files, search over file content.
