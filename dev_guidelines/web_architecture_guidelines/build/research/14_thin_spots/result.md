# Research result: thin spots of round 1 (area code THIN)

## L1 headline

Best practice on the thin spots is now grounded at T1/T2 for audit logging (OWASP), client error reporting and real-user monitoring (MDN, web.dev), partition-based retention and application-time history in PostgreSQL, normalization (Kent, T2) and Post/Redirect/Get with 303 (MDN, RFC 7231, Django); deletion strategy (soft delete vs hard delete plus archive) and logic placement (database vs application) remain genuinely contested and rest on one T3 and one T2 voice, so their certainty is moderate.

Pinned:
- Sources: 22 (T1 17, T2 3, T3 2, T4 0).
- Claims: 40 (THIN-C01 to THIN-C40).
- Contested topics: soft deletion vs hard delete plus archive; logic in the database vs in the application.
- Failed T1 fetch: RFC 9110 section 15.4.4 (303 See Other) could not be read in full, all three fetches of the RFC were truncated before section 15; its wording was confirmed only through a search-result extract, and RFC 7231 and MDN were read instead.

## L2 claims

Pinned (same block as L1):
- Sources: 22 (T1 17, T2 3, T3 2, T4 0).
- Claims: 40 (THIN-C01 to THIN-C40).
- Contested topics: soft deletion vs hard delete plus archive; logic in the database vs in the application.
- Failed T1 fetch: RFC 9110 section 15.4.4 (303 See Other) could not be read in full, all three fetches of the RFC were truncated before section 15; its wording was confirmed only through a search-result extract, and RFC 7231 and MDN were read instead.

Clusters (agreement, certainty, ids; area tag in brackets):

1. [OPS] Log security-relevant events always (validation, authn, authz and session failures, app errors, high-risk functionality) with who/what/when/where context and a shared vocabulary. Consensus, grounded. C01, C02, C03.
2. [OPS, boundary SEC] Never log secrets or tokens; treat client-supplied event data as untrusted input. Consensus, grounded. C04, C20.
3. [OPS, DATA] An audit trail for high-value transactions needs integrity controls (append-only tables or equivalent), storage separate from application data with a write-only account, protected and access-logged. Consensus, grounded. C05, C06, C08, C09.
4. [OPS] Retention is a recorded decision driven by legal, regulatory and contractual duty: not shorter, not longer. Consensus, grounded; the periods themselves are out of reach of architecture. C07.
5. [DATA] Audit by trigger in the same transaction as the change is the PostgreSQL mechanism; choose audit log vs temporal model by how tightly history is queried; record both actual and recording date. Consensus on the pattern, inferred on the application. C10, C11, C12, C13.
6. [OPS, UI] Client error capture: window error event plus unhandledrejection, shipped with sendBeacon on visibilitychange; platform reports (CSP, deprecation, crash) via the Reporting API to a server endpoint. Consensus, grounded; Reporting API support is newly baseline. C14, C15, C16.
7. [OPS] Real-user monitoring: field data via the web-vitals library or PerformanceObserver, percentiles not averages, segmented, cheap to run; correlate with server trace ids. Consensus, grounded (correlation inferred). C17, C18, C19.
8. [DATA] Deletion strategy: soft deletion has named costs (predicate leakage, useless foreign keys, hard purge); hard delete plus an archive table, or partition drop for time-bounded data, are the alternatives. Contested (T3 critique, defenders not read), grounded for the positions. C21, C22, C23, C26.
9. [DATA] History in PostgreSQL: application-time temporal keys exist from version 18 (WITHOUT OVERLAPS, PERIOD); no native system-versioned tables. Consensus on mechanics, inferred on the absence. C24, C25.
10. [DATA] Logic placement: application-first for modifiability and testability, profile before moving logic into SQL, team skill counts; triggers are atomic with the statement. Contested, T2 on one side. C27, C28, C29, C30, C31.
11. [DATA] Normalization: third normal form by default (fact about the key, the whole key, nothing but the key), purpose is preventing update anomalies, denormalize deliberately and document it. Consensus, grounded. C32, C33, C34, C35, C36.
12. [UI, boundary API] Post/Redirect/Get: answer a successful form POST with 303 See Other to a GET resource; 307 keeps the method and is not PRG. Consensus, grounded (RFC 9110 wording not read directly). C37, C38, C39, C40.

Live debates:
- Soft deletion (`deleted_at`) vs hard delete plus archive table vs temporal rows: T3 critique read (soft deletion undermines foreign keys, undelete is rare); pro-soft-deletion and event-sourcing voices not read, so open.
- Logic in the database vs application: Fowler (T2, 2003) is application-first with SQL for profiled hot spots; round 1 shows consensus that constraints belong in the database; the middle (triggers, functions) is the debated zone.

Not covered:
- A T2 source for client-side error reporting design (self-hosted endpoint vs hosted service, source maps, sampling, privacy of error payloads): only T1 browser mechanics read.
- Pro-soft-deletion and event-sourcing literature; Dahan's "Don't delete" essay (search failed to find the text).
- Normal forms beyond 3NF in a T1/T2 source other than Kent; Kleppmann on normalization trade-offs.
- Concrete retention periods and legal bases; incident response (deferred scope); GDPR erasure (deferred scope).
- Idempotency keys for double-click and retry duplicates (PRG only prevents refresh/Back resubmission).
- PostgreSQL wiki page on SQL:2011 temporal support (appeared in search, not fetched).

## L3 full

Pinned (same block as L1):
- Sources: 22 (T1 17, T2 3, T3 2, T4 0).
- Claims: 40 (THIN-C01 to THIN-C40).
- Contested topics: soft deletion vs hard delete plus archive; logic in the database vs in the application.
- Failed T1 fetch: RFC 9110 section 15.4.4 (303 See Other) could not be read in full, all three fetches of the RFC were truncated before section 15; its wording was confirmed only through a search-result extract, and RFC 7231 and MDN were read instead.

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| THIN-S01 | T1 | Logging Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | what to log, what never to log, storage, retention, protection, integrity, injection |
| THIN-S02 | T1 | Logging Vocabulary Cheat Sheet | OWASP Cheat Sheet Series | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html | event naming, timestamps |
| THIN-S03 | T1 | A09:2021 Security Logging and Monitoring Failures | OWASP Top 10 | https://top10.owasp.org/2021/A09_2021-Security_Logging_and_Monitoring_Failures | what to log, audit trail integrity (read after two redirects) |
| THIN-S04 | T1 | Table Partitioning, removing old data | PostgreSQL docs (current) | https://www.postgresql.org/docs/current/ddl-partitioning.html | DROP/DETACH vs bulk DELETE |
| THIN-S05 | T1 | CREATE TABLE | PostgreSQL docs (current, version 18) | https://www.postgresql.org/docs/current/sql-createtable.html | WITHOUT OVERLAPS, PERIOD |
| THIN-S06 | T1 | Constraints | PostgreSQL docs (current, version 18) | https://www.postgresql.org/docs/current/ddl-constraints.html | exclusion constraints; list of constraint types |
| THIN-S07 | T1 | Overview of Trigger Behavior | PostgreSQL docs (current) | https://www.postgresql.org/docs/current/trigger-definition.html | trigger timing, transaction scope |
| THIN-S08 | T1 | RFC 9110 HTTP Semantics, 15.4.4 303 See Other | IETF | https://www.rfc-editor.org/rfc/rfc9110.html, https://httpwg.org/specs/rfc9110.html, https://www.rfc-editor.org/rfc/rfc9110.txt (all truncated before section 15; wording seen only in a search-result extract) | 303 semantics |
| THIN-S09 | T1 | RFC 7231 (obsoleted by RFC 9110), 6.4.4 | IETF | https://www.rfc-editor.org/rfc/rfc7231.html | 303 use after POST |
| THIN-S10 | T1 | 303 See Other | MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303 | 303 and POST/PUT, vs 302/307 |
| THIN-S11 | T1 | Django tutorial part 4 | Django docs | https://docs.djangoproject.com/en/stable/intro/tutorial04/ | redirect after POST |
| THIN-S12 | T1 | Window: error event | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event | uncaught script errors |
| THIN-S13 | T1 | Window: unhandledrejection event | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event | unhandled promise rejections |
| THIN-S14 | T1 | Reporting API | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Reporting_API | browser-generated reports |
| THIN-S15 | T1 | How to measure Core Web Vitals in the field | web.dev | https://web.dev/articles/vitals-field-measurement-best-practices | RUM practice |
| THIN-S16 | T1 | PerformanceObserver | MDN | https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver | browser performance timeline |
| THIN-S17 | T1 | Navigator.sendBeacon() | MDN | https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon | sending telemetry at page end |
| THIN-S18 | T2 | Audit Log (Patterns of Enterprise Application Architecture, further development) | Martin Fowler | https://www.martinfowler.com/eaaDev/AuditLog.html | audit log pattern and its limits |
| THIN-S19 | T2 | Domain Logic and SQL | Martin Fowler | https://martinfowler.com/articles/dblogic.html | logic in SQL vs application |
| THIN-S20 | T2 | A Simple Guide to Five Normal Forms in Relational Database Theory (CACM 26(2), 1983) | William Kent | https://www.bkent.net/Doc/simple5.htm (author's copy) | normalization |
| THIN-S21 | T3 | Soft deletion probably isn't worth it | Brandur Leach (blog) | https://brandur.org/soft-deletion | critique of deleted_at |
| THIN-S22 | T3 | Database normalization description (archived support article) | Microsoft Learn | https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description | beginner normalization; its statement "fourth normal form, also called Boyce-Codd Normal Form" is inaccurate and not used |

### Claims

Audit logging (area tag OPS unless noted)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C01 | Always log input and output validation failures, authentication successes and failures, authorization failures, session management failures, application errors and use of higher-risk functionality; treat data-change events as optional extras chosen per need. Tag: OPS. | principle | neutral | S01 (What to log), S03 (How to prevent) | consensus | | grounded |
| THIN-C02 | Each audit-relevant record should answer when (timestamp), where (application, address, page), who (source address, authenticated identity) and what (event type, severity, affected object, result, reason). Tag: OPS. | practice | neutral | S01 (Event attributes) | consensus | | grounded |
| THIN-C03 | Use one consistent event vocabulary (category prefix plus action, for example authn and authz events) and ISO 8601 timestamps with UTC offset so monitoring can key on the terms. Tag: OPS. | practice | neutral | S02 | consensus (single source, no dissent) | | grounded |
| THIN-C04 | Never log passwords, session ids (hash them if tracking is needed), access tokens, keys, payment data, connection strings or unneeded personal data; pseudonymize where identity is not required. Tag: OPS, boundary: SEC. | principle | neutral | S01 (Data to exclude), S02 (Data events) | consensus | | grounded |
| THIN-C05 | High-value transactions should have an audit trail with integrity controls against tampering or deletion, such as append-only database tables, plus tamper detection that reveals modified or deleted records. Tag: DATA. | decision | neutral | S03 (Log integrity), S01 (Tamper detection) | consensus | | grounded |
| THIN-C06 | Keep logs apart from application data: a separate partition for files, or a separate database account used only to write logs with very restrictive permissions; send to a central collector in a standard format over secure transport. Tag: OPS. | practice | neutral | S01 (Storage) | consensus (single source, no dissent) | | grounded |
| THIN-C07 | Treat log retention as a recorded decision set by legal, regulatory and contractual obligations: keep records no shorter and no longer than the required period. Tag: OPS. | principle | neutral | S01 (Retention and disposal) | consensus (single source, no dissent) | | grounded |
| THIN-C08 | Protect logs at rest and in transit: copy to read-only media as soon as possible, record and monitor every access to the logs, verify the origin of logs received from outside. Tag: OPS. | practice | neutral | S01 (Protection) | consensus (single source, no dissent) | | grounded |
| THIN-C09 | Synchronize time across servers so events can be sequenced; accept that this is often impossible for remote client applications. Tag: OPS. | practice | neutral | S01 (Time) | consensus (single source, no dissent) | | grounded |
| THIN-C10 | Record both the actual date (when the event happened) and the record date (when it was written) in audit entries. Tag: DATA. | practice | neutral | S18 | consensus (single source, no dissent) | | grounded |
| THIN-C11 | Choose the history mechanism by how tightly history is queried: an audit log is simplest and non-intrusive but gets hard to read and poor for frequent integrated temporal queries; temporal properties or objects cost model complexity but integrate with queries. Tag: DATA. | decision | neutral | S18 (When to use) | consensus (single source, no dissent) | | grounded |
| THIN-C12 | In PostgreSQL an audit-by-trigger design commits or rolls back atomically with the audited change, because a trigger runs in the same transaction as its statement; an AFTER trigger sees the final row value, a BEFORE trigger may not. Tag: DATA. | practice | postgres | S07 (mechanism); audit use is my synthesis with S03 | consensus on mechanism | | grounded for the mechanism, inferred for the audit use |
| THIN-C13 | Keep two purposes apart in the design: the security event log (who tried what, for detection) and the business audit trail or history (what changed, for accountability and queries); they differ in storage, integrity needs and retention. Tag: OPS/DATA. | principle | neutral | S01 (data changes optional), S03 (high-value transactions), S18 | consensus (no source states the split) | | inferred from S01, S03, S18 |

Client-side error reporting and real-user monitoring (OPS; UI where noted)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C14 | Capture uncaught client errors with two global handlers: the window error event (message, source, line, column, error object) for synchronous script errors, and unhandledrejection for promise rejections without a handler, because the first does not fire for rejections. Tag: OPS, boundary: UI. | practice | js | S12, S13 | consensus | | grounded |
| THIN-C15 | Send client telemetry with navigator.sendBeacon (fetch as fallback) from a visibilitychange handler when the page becomes hidden, not from unload or beforeunload; the beacon payload is limited to about 64 KiB. Tag: OPS. | practice | js | S17, S15 | consensus | | grounded |
| THIN-C16 | Receive browser-detected problems (CSP violations, deprecations, crashes, interventions) through the Reporting API with a Reporting-Endpoints header pointing to a server endpoint; ReportingObserver in script is not failsafe and cannot report crashes; delivery is not guaranteed. Tag: OPS, boundary: SEC. | decision | http | S14 | consensus (single source, no dissent) | support is described as newly baseline with varying parts; check target browsers | grounded |
| THIN-C17 | Measure real-user performance in the field with the web-vitals library, report percentiles (75th) not averages, segment by device, connection and release, only collect what will be used, and keep measurement code from hurting the page. Tag: OPS, boundary: UI. | practice | js | S15 | consensus | | grounded |
| THIN-C18 | PerformanceObserver is the browser primitive for RUM: it delivers navigation, resource, largest-contentful-paint, layout-shift, event and longtask entries as they occur. Tag: OPS. | practice | js | S16 | consensus (single source, no dissent) | | grounded |
| THIN-C19 | Stamp client error and RUM events with the release version and the trace or request id so a browser error can be joined to server logs and traces. Tag: OPS. | practice | neutral | round-1 OPS L2 cluster 1 and 3 (not re-read), S15 (version tracking for segmentation) | consensus (inferred) | | inferred |
| THIN-C20 | Treat events arriving from clients as untrusted input: validate and sanitize them (CR, LF, delimiters) before writing to logs, and encode for the output format. Tag: OPS, boundary: SEC. | practice | neutral | S01 (Injection), S03 | consensus | | grounded |

Deletion and history (DATA)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C21 | Soft deletion with a deleted_at flag has costs that must be weighed: the predicate leaks into all queries, foreign keys no longer enforce consistency between a deleted parent and its children, and a legally required purge becomes harder; undelete is rarely used in practice. | decision | postgres | S21 | contested | For the critique: S21 (T3, practitioner experience of several systems). For soft deletion: not read at T1/T2 (open); the usual argument is recoverability and history, which S18 would serve differently. | grounded in one T3 |
| THIN-C22 | Prefer hard delete plus an archive written in the same transaction (a deleted-record table holding table name, id and a jsonb copy) over a deleted_at flag when you need recovery or audit, so foreign keys keep working. | decision | postgres | S21 | contested | Same as C21; the archive approach is the alternative named by S21; S18 supports "write a record of what happened" in general | grounded in one T3 |
| THIN-C23 | For time-bounded data (events, logs, measurements) partition by time and drop or detach old partitions instead of bulk DELETE: it is far faster and avoids vacuum overhead; DETACH PARTITION (optionally CONCURRENTLY) keeps the data available to back up or aggregate first; DROP TABLE takes an ACCESS EXCLUSIVE lock on the parent. | practice | postgres | S04 | consensus | | grounded |
| THIN-C24 | For history of validity periods, PostgreSQL 18 offers application-time constraints: PRIMARY KEY or UNIQUE with a last column WITHOUT OVERLAPS, and FOREIGN KEY with a last column PERIOD; exclusion constraints with ranges are the earlier mechanism. Check the project's PostgreSQL version before relying on this. | practice | postgres | S05, S06 | consensus | | grounded |
| THIN-C25 | PostgreSQL has no native SQL:2011 system-versioned (transaction-time) tables; record who changed what and when through audit triggers or application-written history tables. | decision | postgres | S05, S06 (documents list only application-time features) | consensus (T1 absence, T4 snippet agrees) | | inferred (absence in the pages read; the wiki page was not fetched) |
| THIN-C26 | Decide deletion per entity from the reason the data is kept: no need (hard delete), legal or audit retention (archive table or append-only audit), user-visible recovery (archive or soft delete with an owner for the predicate), queryable past values (temporal model), bulk expiry (partition drop); record the choice. | decision | neutral | S21, S18, S04, S05 | majority | Positions as C21 to C25 | inferred (synthesis across S04, S05, S18, S21) |

Where logic lives (DATA)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C27 | Put domain logic in the application first for modifiability, do not let performance be the first question, profile, and move proven hot spots into SQL, preferably as data-source queries rather than domain logic. | decision | neutral | S19 | contested | Application-first: S19 (T2, 2003). Database-heavy: not found at T1/T2 as an argument for domain logic; round 1 holds consensus that constraints and keys belong in the database. | grounded |
| THIN-C28 | Team skill is a legitimate input: if most of the team is less comfortable with SQL, that is a reason to keep domain logic out of SQL. | principle | neutral | S19 | consensus (single source, no dissent) | | grounded |
| THIN-C29 | Logic in the application is faster to test in memory behind a replaceable database interface; logic in the database needs a database to test. | principle | neutral | S19 | consensus (single source, no dissent) | | grounded |
| THIN-C30 | A trigger executes in the same transaction as its statement and rolls back with it; row-level BEFORE triggers can skip or alter the row, AFTER triggers see the final value; use triggers where an invariant or side record must be atomic with the write. | practice | postgres | S07 | consensus | | grounded |
| THIN-C31 | Rule for the split: rules that must hold whatever application writes the data (keys, NOT NULL, foreign keys, row-local checks, atomic audit) live in the database; workflow, policy and rules that change with product decisions live in the application. | decision | neutral | S19, S07, S06, round-1 DATA L2 cluster 4 and 10 (not re-read) | contested | The middle zone (triggers, functions, views for encapsulation) is where S19 and database-first practitioners disagree | inferred |

Normal forms (DATA)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C32 | Design relational tables to third normal form by default: every non-key field states a fact about the key, the whole key, and nothing but the key. | principle | neutral | S20 (summary of 1NF to 3NF), S22 | consensus | | grounded |
| THIN-C33 | The purpose of normalization is to prevent redundancy, update anomalies and inconsistent dependencies, so each fact is stored and changed in one place. | principle | neutral | S20, S22 | consensus | | grounded |
| THIN-C34 | Denormalize deliberately, not by default: there is no obligation to fully normalize where measured performance requires otherwise, but the application must then guard the redundancy. Normalization tends to penalize retrieval because data is spread over several records. | decision | neutral | S20, S22 (Exception to 3NF) | consensus | | grounded |
| THIN-C35 | Third normal form is the practical target for most applications; higher forms (Boyce-Codd, fourth, fifth) matter in specific multi-valued or overlapping-key designs. | principle | neutral | S22, S20 (covers up to fifth normal form) | majority | S22 (T3) says higher forms are rarely considered; S20 describes them without ranking | grounded for 3NF target, inferred for "specific designs" |
| THIN-C36 | Remove repeating groups (Class1, Class2, Class3 columns) into a child table linked by a foreign key; such columns signal design trouble. | practice | neutral | S22 (1NF) | consensus (single source, no dissent) | | grounded |

Post/Redirect/Get and 303 (UI, boundary: API)

| id | claim | level | stack | sources | agreement | positions | certainty |
|---|---|---|---|---|---|---|---|
| THIN-C37 | Answer a successfully processed form POST with 303 See Other and a Location header pointing to a GET-able page (confirmation or the new resource), so reload or Back does not resubmit. Tag: UI, boundary: API. Replaces the T4-only grounding of UI-C17. | practice | http | S10, S11, S09 | consensus | | grounded |
| THIN-C38 | 303 means the server redirects to a different resource that is an indirect response to the original request; the client retrieves it with GET (or HEAD). The RFC 9110 sentence was seen only in a search-result extract; MDN states the method to fetch the redirected resource is always GET; RFC 7231 allows the server to answer a POST with 303 pointing at an existing resource. | principle | http | S08 (secondary only), S10, S09 | consensus | | grounded via S09 and S10; S08 wording unconfirmed by direct read |
| THIN-C39 | Use 303, not 307, for PRG: 307 preserves the request method and so repeats the POST; 302 behavior varies by client, which is why 303 is the explicit choice. | practice | http | S10 (comparison table) | consensus (single source, no dissent) | | grounded |
| THIN-C40 | Frameworks document redirect-after-POST as general practice: Django states a view should always return a redirect after successfully dealing with POST data to prevent data being posted twice on Back. | practice | python | S11 | consensus | | grounded |

### Gaps

- Open: a T1/T2 source for client error reporting design (endpoint ownership, source maps, sampling, privacy). Only browser mechanics and field-measurement practice are grounded.
- Open: pro-soft-deletion, event-sourcing and Dahan literature; the contested status of C21/C22 rests on one T3 critique.
- Open: Kleppmann or another T2 on normalization trade-offs; only Kent (1983) read at T2.
- Open: PostgreSQL wiki page on SQL:2011 temporal support (listed in search, not fetched); C25 is inferred.
- Open: RFC 9110 section 15.4.4 direct read; three mirrors truncated. Recommended follow-up: read it from a downloaded copy.
- Not covered: idempotency keys for duplicate submits beyond refresh and Back; retention periods per jurisdiction; incident response and GDPR erasure (deferred scope).
- Source flaw noted: S22 equates fourth normal form with Boyce-Codd normal form, which is wrong; only its third-normal-form and repeating-group content was used.
- Boundaries: C04, C16, C20 touch SEC; C14, C17 touch UI; C37 to C40 touch API.
