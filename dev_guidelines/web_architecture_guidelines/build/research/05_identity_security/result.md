# SEC research result: identity, access and security across tiers

## L1 headline

Best practice for web identity and security is mature and mostly consensual: decide access on the server, deny by default, keep tokens out of JavaScript (cookie session or a backend-for-frontend), layer CSRF and XSS defenses, delegate database-level isolation to Postgres row-level security as a second line, and treat dependencies and secrets as supply chains; certainty is high (grounded in T1 sources) except the sessions-versus-JWT choice and the secrets-storage medium, which are contested.

Pinned:
- Sources: 35 (T1: 33, T2: 2, T3: 0, T4: 0).
- Claims: 60.
- Contested: sessions vs bearer JWT for first-party browser apps; environment variables vs secrets manager for secrets.
- Failed T1 fetches: OWASP JWT-for-Java cheat sheet (404 on three URLs, replaced by RFC 8725 and the OWASP HTML5 cheat sheet); OWASP ASVS "Using ASVS" chapter (404 on two URLs, so ASVS levels are left open); OWASP Secure Headers project page (identity card only, header list taken from the OWASP HTTP Headers cheat sheet).

## L2 claims

Clusters (agreement, certainty, claim ids):

1. Access decisions live on the server: deny by default, one central mechanism applied to every request, object-level ownership, tested and logged; authentication is not authorization. Consensus, grounded. SEC-C01 to SEC-C07.
2. For a browser app, keep tokens away from JavaScript: a server-side session in an HttpOnly cookie, or a backend-for-frontend (BFF) that holds OAuth tokens; browser-held tokens are the last resort; stateless tokens cannot be revoked without server state. Consensus on BFF and no localStorage; contested on sessions vs JWT. Grounded. SEC-C08 to SEC-C14.
3. Sessions are an opaque random identifier in a hardened cookie (Secure, HttpOnly, SameSite, `__Host-`), renewed on login, expired server-side (idle and absolute), invalidated on logout, never scoped to a parent domain, built with the framework. Consensus, grounded. SEC-C15 to SEC-C23.
4. CSRF is defended in layers: framework token, SameSite, Origin and Fetch Metadata checks, no state change on safe methods; XSS defeats all of them. Consensus, grounded. SEC-C24 to SEC-C29.
5. Delegated login uses the OAuth 2 authorization code flow with PKCE, exact redirect matching, rotated or sender-constrained refresh tokens, and OpenID Connect ID token validation; link accounts by issuer plus subject. Consensus, grounded. SEC-C30 to SEC-C35.
6. Credentials: long passphrases without composition rules or forced rotation, breach blocklist, Argon2id hashing, MFA with phishing-resistant options, generic errors, throttling. Consensus (Django default hasher differs), grounded. SEC-C36 to SEC-C39.
7. Postgres row-level security is a default-deny second line under application checks, only effective when the app role is not superuser, not BYPASSRLS and not owner, and when identity is passed transaction-locally. Consensus on mechanics, majority on whether to use it. Grounded. SEC-C40 to SEC-C44.
8. Browser hardening: strict nonce or hash CSP rolled out in report-only, as a second layer behind output encoding; a small baseline of response headers; obsolete headers removed. Consensus, grounded. SEC-C45 to SEC-C49.
9. Secrets: never in code, centralized, least-privilege, rotated and audited, CI/CD treated as production; storage medium is debated. Consensus on principles, contested on medium. Grounded. SEC-C50 to SEC-C54.
10. Supply chain: pinned and hash-verified dependencies, SBOM and continuous scanning, trusted sources and staged rollout, verifiable build provenance. Consensus, grounded. SEC-C55 to SEC-C58.
11. Standards as maps: OWASP Top 10:2025 as an awareness map to tiers (my synthesis); ASVS 5.0 as a requirement catalogue whose levels I could not read. Inferred / open. SEC-C59, SEC-C60.

Live debates:
- Sessions vs bearer JWT for first-party browser apps: IETF, OWASP and Django favor server-side state and cookies; FastAPI's tutorial path teaches OAuth2 bearer with JWT.
- Secrets in environment variables (Twelve-Factor) vs a secrets manager with runtime injection (OWASP).
- Session timeout numbers: OWASP gives 15-30 min idle for low risk, NIST 800-63B-4 gives 1 h idle and 24 h overall at AAL2; both are risk-calibrated, not in conflict.
- Tenant isolation: separate databases, separate schemas, or shared tables with RLS (OWASP multi-tenant sheet lists all three by strength vs cost).

Not covered: ASVS level semantics and chapter contents; OWASP JWT cheat sheet itself; threat modeling and Insecure Design (A06); rate limiting and abuse protection in depth; SSRF and file upload; cryptography choices beyond passwords; TLS configuration; third-party content isolation; audit logging design (boundary OPS); CORS design (boundary API); Postgres role design (boundary DATA).

## L3 full

### Source register

All URLs were fetched and read in this session (page content, not summaries from search). Tier T1 = normative or official; T2 = recognized authority. Dates reported by the fetched pages (for example RFC 10017, August 2026) are taken as read.

| id | tier | title | body | URL read | authoritative on |
|---|---|---|---|---|---|
| SEC-S01 | T1 | Session Management Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html | session id, cookies, lifecycle, expiry |
| SEC-S02 | T1 | CSRF Prevention Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html | CSRF defenses |
| SEC-S03 | T1 | Authorization Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | authorization design |
| SEC-S04 | T1 | Content Security Policy Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html | CSP |
| SEC-S05 | T1 | Secrets Management Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | secrets |
| SEC-S06 | T1 | RFC 9700 OAuth 2.0 Security Best Current Practice | IETF | https://datatracker.ietf.org/doc/html/rfc9700 | OAuth 2 security |
| SEC-S07 | T1 | draft-ietf-oauth-browser-based-apps-27, OAuth 2.0 for Browser-Based Applications | IETF | https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps | BFF and browser patterns |
| SEC-S08 | T1 | RFC 10017 OAuth 2.0 for Browser-Based Applications (BCP 212) | IETF | https://www.rfc-editor.org/rfc/rfc10017.html | final form of S07 |
| SEC-S09 | T1 | OWASP Top 10:2025 | OWASP | https://top10.owasp.org/2025 | risk categories |
| SEC-S10 | T1 | A01:2025 Broken Access Control | OWASP | https://top10.owasp.org/2025/A01_2025-Broken_Access_Control | access control prevention |
| SEC-S11 | T1 | A03:2025 Software Supply Chain Failures | OWASP | https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures | supply chain prevention |
| SEC-S12 | T1 | Practical implementation guide: CSP | MDN | https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP | CSP rollout |
| SEC-S13 | T1 | OWASP Secure Headers Project (page is an index only) | OWASP | https://owasp.org/www-project-secure-headers/ | pointer to header list |
| SEC-S14 | T1 | HTTP Headers Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html | response headers |
| SEC-S15 | T1 | Authentication Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html | authentication |
| SEC-S16 | T1 | Password Storage Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html | password hashing |
| SEC-S17 | T1 | OpenID Connect Core 1.0 | OpenID Foundation | https://openid.net/specs/openid-connect-core-1_0.html | OIDC |
| SEC-S18 | T1 | NIST SP 800-63B-4 Authentication and Authenticator Management | NIST | https://pages.nist.gov/800-63-4/sp800-63b.html | passwords, session timeouts, AAL |
| SEC-S19 | T1 | HTTP Cookies guide | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies | cookie attributes |
| SEC-S20 | T1 | Row Security Policies | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-rowsecurity.html | RLS |
| SEC-S21 | T1 | Configuration settings functions (set_config) | PostgreSQL docs | https://www.postgresql.org/docs/current/functions-admin.html | transaction-local settings |
| SEC-S22 | T1 | Security in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/security/ | framework protections |
| SEC-S23 | T1 | How to use sessions | Django docs | https://docs.djangoproject.com/en/stable/topics/http/sessions/ | session backends and risks |
| SEC-S24 | T1 | Password management in Django | Django docs | https://docs.djangoproject.com/en/stable/topics/auth/passwords/ | hashers, validators |
| SEC-S25 | T1 | Security (tutorial intro) | FastAPI docs | https://fastapi.tiangolo.com/tutorial/security/ | FastAPI security tooling |
| SEC-S26 | T1 | Protect your resources from web attacks with Fetch Metadata | web.dev | https://web.dev/articles/fetch-metadata | resource isolation policy |
| SEC-S27 | T1 | SameSite cookies explained | web.dev | https://web.dev/articles/samesite-cookies-explained | same-site definition |
| SEC-S28 | T1 | Software Supply Chain Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html | dependency management |
| SEC-S29 | T1 | Secure installs | pip docs (PyPA) | https://pip.pypa.io/en/stable/topics/secure-installs/ | hash-checking installs |
| SEC-S30 | T1 | RFC 8725 JSON Web Token Best Current Practices | IETF | https://datatracker.ietf.org/doc/html/rfc8725 | JWT validation |
| SEC-S31 | T1 | HTML5 Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html | web storage, CORS |
| SEC-S32 | T1 | Multi-Tenant Security Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html | tenant isolation, RLS |
| SEC-S33 | T1 | OWASP Application Security Verification Standard project page | OWASP | https://owasp.org/www-project-application-security-verification-standard/ | ASVS version and identifiers |
| SEC-S34 | T2 | The Twelve-Factor App, III. Config | Wiggins et al. | https://12factor.net/config | config and secrets separation |
| SEC-S35 | T2 | SLSA v1.0 Build track levels | OpenSSF | https://slsa.dev/spec/v1.0/levels | build provenance levels |

Failed fetches (T1): OWASP JWT Cheat Sheet for Java (three URL spellings, all 404; a search snippet restated sidejacking, fingerprint cookie and denylist advice but it was not read as a source and no claim rests on it); OWASP ASVS "Using ASVS" chapter, raw and blob GitHub URLs (404). The `owasp.org/Top10` and `/Top10/2021/...` URLs redirected to `top10.owasp.org` and were re-fetched there.

### Claims

Format: id | claim | level | stack | sources | agreement | positions | certainty.

#### A. Where access is decided

- **SEC-C01** | Access control must be decided in trusted server-side code (server or gateway); client-side checks only improve user experience. | principle | neutral | S03 "Server-Side Enforcement"; S10 "Prevention" | consensus | | grounded
- **SEC-C02** | Deny by default: every request needs an explicit permit decision; except public resources, nothing is allowed implicitly. | principle | neutral | S03 "Deny by Default"; S10 | consensus | | grounded
- **SEC-C03** | Implement the authorization mechanism once, centrally (filters or middleware), and apply it to every request whatever its origin (AJAX, server-side, other). | decision | neutral | S03 "Validate on Every Request"; S10 "Centralized Mechanisms" | consensus | | grounded
- **SEC-C04** | Enforce object-level rules (record ownership), not only route or role checks. | practice | neutral | S10 "Record Ownership" (common failure: insecure direct object references) | consensus | | grounded
- **SEC-C05** | Prefer attribute- or relationship-based access control over plain role-based control when granularity or multi-tenancy grows. | decision | neutral | S03 "Prefer ABAC/ReBAC over RBAC" | consensus | single T1 source, no dissent found | grounded
- **SEC-C06** | Test authorization with unit and integration tests including denial cases, and log access-control failures with alerting. | practice | neutral | S03 "Implement Testing"; S10 "Logging & Monitoring" | consensus | boundary: OPS | grounded
- **SEC-C07** | Authentication is not authorization: an OpenID Connect ID token is for the client, not for access to APIs. | principle | neutral | S17 ID Token; S15 | consensus | | grounded

#### B. Browser authentication architecture

- **SEC-C08** | For browser apps handling business, sensitive or personal data, use a backend-for-frontend: the server is the confidential OAuth client, holds the tokens, proxies resource calls, and the browser holds only an HttpOnly, Secure, SameSite cookie session. | decision | http | S07 s6.1; S08 | consensus | | grounded
- **SEC-C09** | Use a token-mediating backend only if a BFF is not viable, and a browser-only public OAuth client only if no backend is possible; the latter must use PKCE, rotate refresh tokens or sender-constrain them, and expire them by maximum lifetime or inactivity. | decision | http | S07 s6.2, s6.3; S08 | consensus | | grounded
- **SEC-C10** | Assume malicious JavaScript has the same privileges as the legitimate app code; design so that a successful XSS cannot exfiltrate long-lived credentials (token theft, silent token acquisition). | principle | js | S07 s5.5 | consensus | | grounded
- **SEC-C11** | For a first-party browser app on the same site as its server, prefer an opaque server-side session in a cookie over bearer tokens held by JavaScript. | decision | http | S01; S19 summary ("store sensitive data server-side with opaque session identifiers"); S23; S07 s6.1; S31 | contested | Server-side session or BFF cookie: IETF browser-apps BCP, OWASP session and HTML5 sheets, Django docs; applies to first-party browser clients. Bearer JWT: FastAPI tutorial path teaches OAuth2 password flow with JWT bearer (chapter preview only; not read in depth), suited to API clients and third-party clients. No T1/T2 source read argues for stateless JWT as the browser session of a first-party app. | inferred (synthesis of S01, S07, S19, S23, S25, S31)
- **SEC-C12** | Never store session identifiers or tokens in localStorage or other JavaScript-readable storage; use an HttpOnly cookie. | practice | js | S31 "Local storage"; S01 "HttpOnly" | consensus | | grounded
- **SEC-C13** | Stateless signed tokens and signed-cookie sessions cannot be revoked on logout without server-held state; where instant revocation matters, keep server-side session state and invalidate it on logout. | principle | neutral | S23 "Cookie-based sessions"; S10 ("invalidate stateful sessions server-side after logout; short-lived JWTs"); S01 "Manual Logout" | consensus | | grounded
- **SEC-C14** | If JWTs are used, the verifier must pin the accepted algorithms, reject `none` unless protected otherwise, validate issuer, subject and audience, and keep different JWT kinds distinguishable (explicit `typ`, distinct keys or claims). | practice | neutral | S30 s3.1, s3.2, s3.8, s3.9, s3.11, s3.12 | consensus | | grounded

#### C. Sessions

- **SEC-C15** | Session identifiers are random (CSPRNG), at least 64 bits of entropy, meaningless, and carry no personal data; user data stays server-side. | practice | neutral | S01 "Session ID Properties" | consensus | | grounded
- **SEC-C16** | Use the framework's session management, not a custom one, and keep the framework updated. | decision | python | S01 "Built-in Implementations"; S22; S23 | consensus | | grounded
- **SEC-C17** | Session cookies carry `Secure`, `HttpOnly` and an explicit `SameSite=Lax` or `Strict`, use the `__Host-` prefix, omit `Domain`, and use the narrowest `Path`. | practice | http | S01 "Cookies"; S19 prefixes and attributes | consensus | | grounded
- **SEC-C18** | Renew the session identifier on every privilege change, above all at login (session fixation). | practice | neutral | S01 "Privilege Changes"; S23 "Session Fixation" (`login()` cycles the key) | consensus | | grounded
- **SEC-C19** | Enforce idle and absolute session timeouts on the server, calibrated to risk. | practice | neutral | S01 "Session Expiration" (idle 15-30 min low risk, 2-5 min high value; absolute 4-8 h office apps); S18 timeout table (AAL2: 1 h idle, 24 h overall; AAL3: 15 min idle, 12 h overall) | majority | Numbers differ by risk class and by body; the shared position is server-enforced idle plus absolute limits scaled to assurance level. | grounded
- **SEC-C20** | Logout invalidates the session on the server; responses carrying session identifiers use `Cache-Control: no-store`. | practice | http | S01 "Manual Logout", "Content Caching" | consensus | | grounded
- **SEC-C21** | Do not use the signed-cookie session backend for sensitive data: signed is not encrypted, replay is possible until expiry, there is no revocation, and a leaked secret key plus pickle serialization allows code execution. | practice | python | S23 "Cookie-Based Sessions" | consensus | single framework source | grounded
- **SEC-C22** | Do not scope the session cookie to a parent domain: sibling subdomains could plant cookies (subdomain session fixation); note that same-site means same registrable domain, not same origin. | practice | http | S23 "Subdomain Session Fixation"; S01 "Domain and Path"; S27 | consensus | | grounded
- **SEC-C23** | Serve the whole session over HTTPS (never mix), and set HSTS. | practice | http | S01 "Transport Layer Security"; S14 HSTS; S22 "HTTPS/SSL" | consensus | | grounded

#### D. CSRF

- **SEC-C24** | Use the framework's built-in CSRF protection first and avoid exempting views from it. | practice | python | S02 "Primary Defenses"; S22 CSRF | consensus | | grounded
- **SEC-C25** | Layer defenses: synchronizer token (or signed double-submit for stateless apps) plus SameSite cookies; SameSite alone is insufficient because Lax allows top-level GET navigations, covers the site rather than the origin, and does not stop client-side CSRF. | decision | http | S02 "SameSite", "Double-Submit"; S19; S27 | consensus | | grounded
- **SEC-C26** | Never change state on GET or other safe methods. | principle | http | S02 "What Is NOT a Defense" | consensus | boundary: API | grounded
- **SEC-C27** | Reject cross-site unsafe-method requests using `Origin` verification or `Sec-Fetch-Site` (Fetch Metadata), allowing requests that lack the headers for legacy browsers and exempting deliberate CORS endpoints; trial it in logging-only mode. | practice | http | S02 "Fetch Metadata", "Origin Verification"; S26 | consensus | | grounded
- **SEC-C28** | XSS defeats every CSRF defense, so XSS prevention is a precondition, not an alternative. | principle | neutral | S02 "What Is NOT a Defense" | consensus | | grounded
- **SEC-C29** | A custom request header on AJAX calls relies on CORS preflight to block simple cross-site requests; CORS must list explicit trusted origins (no wildcard) and does not replace CSRF protection. | practice | http | S02 "Custom Headers"; S31 CORS | consensus | boundary: API | grounded

#### E. OAuth 2 and OpenID Connect

- **SEC-C30** | Use the authorization code grant with PKCE (mandatory for public clients, recommended for confidential ones); do not use the implicit grant. | decision | http | S06 s2.1.1, s2.1.2 | consensus | | grounded
- **SEC-C31** | Match redirect URIs by exact string comparison and run no open redirectors. | practice | http | S06 s2.1, s4.11 | consensus | | grounded
- **SEC-C32** | Rotate or sender-constrain refresh tokens of public clients, and sender-constrain access tokens (mutual TLS or DPoP). | practice | http | S06 s2.2.1, s2.2.2; S07 s6.3 | consensus | | grounded
- **SEC-C33** | When using OpenID Connect for login, validate the ID token: issuer, audience contains the client id, expiry, and the `nonce` sent in the request. | practice | neutral | S17 "ID Token Validation" | consensus | | grounded
- **SEC-C34** | Link federated identities by issuer plus subject, never by e-mail alone, and require reauthentication before changing links. | practice | neutral | S15 "Standard Protocols & Federation" | consensus | | grounded
- **SEC-C35** | Choose explicitly between delegating login to an external identity provider via standard protocols (OAuth 2, OIDC, SAML) and operating your own credential store; record the choice. | decision | neutral | S15 (recommends standard protocols for integration); S25 (supports both own password flow and third-party providers) | majority | Delegate to a provider: reduces credential handling; own accounts: needed when no provider fits. No source ranks them outright. | inferred

#### F. Credentials

- **SEC-C36** | Password policy: allow at least 64 characters and all printable Unicode, impose no composition rules and no periodic rotation, and check against compromised and common-password lists; minimum length 8 with MFA, 15 without. | practice | neutral | S15 "Password Policy"; S18 "Password Requirements" | consensus | Django's default validators require 8 (configurable) and still include a numeric-only check (S24). | grounded
- **SEC-C37** | Hash passwords with Argon2id (at least 19 MiB, 2 iterations, parallelism 1), with scrypt, bcrypt or PBKDF2 as fallbacks, and upgrade hashes at login. | practice | python | S16 "Primary Recommendations"; S24 | majority | OWASP and the Django docs recommend Argon2; Django's default hasher is PBKDF2-SHA256, Argon2 is opt-in (`django[argon2]`); PBKDF2 stays acceptable where FIPS-140 applies (S16, S18). | grounded
- **SEC-C38** | Offer MFA and phishing-resistant authenticators (WebAuthn, passkeys). | decision | neutral | S15 "Multi-Factor", "Passkeys"; S18 phishing resistance | consensus | | grounded
- **SEC-C39** | Return generic authentication errors, count failures per account, throttle or lock out with growing delays, and rate-limit login. | practice | neutral | S15 "Error Handling", "Brute-Force"; S22 key recommendations | consensus | | grounded

#### G. Row-level security and database identity (boundary: DATA)

- **SEC-C40** | With row-level security enabled, a table denies all rows until a policy permits them; `USING` governs visibility, `WITH CHECK` governs written rows, permissive policies combine with OR and restrictive with AND. | practice | postgres | S20 | consensus | boundary: DATA | grounded
- **SEC-C41** | The application's request-path role must not be a superuser, hold BYPASSRLS, or (unless `FORCE ROW LEVEL SECURITY` is set) own the table, otherwise policies are skipped. | practice | postgres | S20 "Exemptions"; S32 "Row-Level Security" | consensus | boundary: DATA | grounded
- **SEC-C42** | Pass the application user or tenant to the database with transaction-local settings (`set_config(..., true)` or `SET LOCAL`), not session-level ones, so pooled connections cannot leak context; derive the value from the verified identity, never from a client-supplied id. | practice | postgres | S21 `is_local`; S32 "Tenant Context Propagation"; S20 (shows session variable pattern) | consensus | boundary: DATA, APP | grounded
- **SEC-C43** | Tenant isolation is a recorded decision among separate databases (strongest, costliest), separate schemas, or shared tables with RLS; where RLS is chosen, keep application-level checks too and test denial through the deployed role and connection path. | decision | postgres | S32 | majority | Strength versus cost trade-off; RLS as second line rather than sole control is the cheat sheet's stance; no source says application checks may be dropped. | grounded
- **SEC-C44** | RLS has known leaks: foreign-key and unique constraints bypass it, sub-selects in policies can race, so schemas and policies need design review. | practice | postgres | S20 "Caveats" | consensus | boundary: DATA | grounded

#### H. Browser hardening

- **SEC-C45** | Deploy a strict CSP (nonce or hash plus `strict-dynamic`, `object-src 'none'`, `base-uri 'none'`, no `unsafe-inline`/`unsafe-eval`) in preference to allowlist policies. | decision | http | S04 "Strict CSP"; S12 "Implement Strict CSP" | consensus | | grounded
- **SEC-C46** | CSP is a second layer against XSS; the first layer remains output encoding and templating that escape by default. | principle | neutral | S04 "Defense in Depth"; S22 XSS | consensus | boundary: UI, APP | grounded
- **SEC-C47** | Roll CSP out in `Content-Security-Policy-Report-Only` first, fix violations, then enforce. | practice | http | S04; S12 | consensus | | grounded
- **SEC-C48** | Nonces must be unique per response and injected by a real templating engine, whereas hashes suit static inline scripts; this ties CSP to how HTML is produced (server-rendered versus static). | decision | http | S04 "Nonce-Based", "Hash-Based" | consensus | boundary: UI | grounded
- **SEC-C49** | Send a small baseline of response headers (HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, CSP `frame-ancestors` in place of `X-Frame-Options`, `Permissions-Policy`, COOP) and remove `X-XSS-Protection`, `Expect-CT`, `Server` and `X-Powered-By`. | practice | http | S14; S04 "Complementary Headers"; S22 | consensus | | grounded

#### I. Secrets and configuration

- **SEC-C50** | Secrets are never hardcoded in source or committed config; the litmus test is that the code base could be open-sourced without leaking credentials. | principle | neutral | S05 "Eliminate Hardcoding"; S34 | consensus | | grounded
- **SEC-C51** | Where secrets live at runtime is contested: Twelve-Factor stores config, secrets included, in environment variables; OWASP warns against environment variables visible to many processes and prefers injection at runtime from a managed store. | decision | neutral | S34; S05 | contested | Environment variables: Twelve-Factor (simple, language-neutral, portable). Secrets manager with runtime injection: OWASP (access control, rotation, audit). Choice depends on team size and platform. | grounded
- **SEC-C52** | Centralize and standardize secret storage, grant least privilege per service, prefer short-lived dynamic secrets with automated rotation, and audit every access (keep logs at least 90 days). | practice | neutral | S05 | consensus | boundary: OPS | grounded
- **SEC-C53** | Keep the framework signing secret (Django `SECRET_KEY`) confidential, since it protects sessions, tokens and signed data. | practice | python | S22 "Key recommendations"; S23 | consensus | | grounded
- **SEC-C54** | Treat CI/CD as production: least-privilege service accounts, secrets scoped per environment, no secrets in pipeline output. | practice | neutral | S05 "CI/CD Pipeline Security"; S11 | consensus | boundary: OPS | grounded

#### J. Dependencies and supply chain

- **SEC-C55** | Pin dependencies through lockfiles, and for Python install with hash-checking (`--require-hashes`, which must cover transitive dependencies; optionally `--only-binary :all:`). | practice | python | S11 "Version Pinning"; S28 "Lockfiles"; S29 | consensus | | grounded
- **SEC-C56** | Keep a software bill of materials covering direct and transitive dependencies, and scan continuously against vulnerability databases. | practice | neutral | S11; S28 | consensus | boundary: OPS | grounded
- **SEC-C57** | Obtain components only from official sources over secure links (prefer signed packages) and deploy updates in staged or canary rollouts. | practice | neutral | S11 "Trusted Sources", "Staged Rollouts" | consensus | boundary: OPS | grounded
- **SEC-C58** | Produce verifiable build provenance (SLSA), at least from a hosted build platform with signed provenance (Build L2), and verify it before use. | decision | neutral | S28 "Provenance"; S35 | consensus | boundary: OPS | grounded

#### K. Standards as maps

- **SEC-C59** | Use the OWASP Top 10:2025 (A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions) as an awareness map and assign each category to an owning tier: A01 server and database (C01-C06, C40-C44); A02 headers, CSP and deployment (C45-C49); A03 pipeline and dependencies (C55-C58); A04 and A07 server (C15-C23, C36-C39); A05 server and database (out of SEC scope, DATA/APP); A09 operations (OPS). | principle | neutral | S09 (list read); mapping is my synthesis | consensus | Mapping to tiers is not stated by the source. | inferred
- **SEC-C60** | Use ASVS 5.0 as the catalogue of verifiable security requirements (identifiers carry the version, for example v5.0.0-1.2.5), choosing a verification level by application risk and citing requirement ids in the guideline's traces. | decision | neutral | S33 | consensus | Level definitions and chapter list not read from a T1 source (fetch failed). | open

### Gaps

- ASVS levels L1 to L3: definitions and per-chapter requirements not read; needed before mapping claims to ASVS ids.
- OWASP JWT cheat sheet not read (404); claims on JWT rest on RFC 8725 and the HTML5 sheet only. Fingerprint-cookie sidejacking defense unverified.
- No T1/T2 source read argues for stateless JWT as a first-party browser session; the contested claim C11 records the opposing position from FastAPI's tutorial structure, read only at chapter-preview level.
- Not researched: threat modeling and Insecure Design (A06), SSRF, file upload, rate limiting and abuse design, TLS configuration, cryptography choices beyond passwords, third-party script isolation, audit logging format.
- Django CSRF reference page and Starlette or FastAPI session and CSRF handling not read; C24 and C30 for FastAPI rely on Django docs only.
- Recording rule for the guideline: the dates and RFC numbers above are as shown by the fetched pages (the BFF document appears both as a draft revision 27 and as RFC 10017); cite the RFC.
