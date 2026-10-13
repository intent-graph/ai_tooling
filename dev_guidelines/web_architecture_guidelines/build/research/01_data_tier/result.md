# Research result: DATA, Data tier (Postgres)

## L1 headline

Best practice for the Postgres data tier is well settled where PostgreSQL's own documentation speaks (constraints, locks, roles, backup and recovery, migration mechanics) and consistently backed by Fowler and Stripe/GitLab practice on evolutionary, expand-migrate-contract schema change; it is thin or contested on where logic lives, key type, deletion/history, and on contract schemas versus direct table access. Certainty: grounded on the T1/T2 core, inferred on cross-source synthesis, open on the contested topics.

Pinned:
- Sources: 41 (24 T1, 5 T2, 9 T3, 3 T4); 38 fetched as pages, 3 T4 known from search snippets only.
- Claims: 56 (DATA-C01 to DATA-C56).
- Contested topics: key type (identity vs UUIDv7 vs UUIDv4); soft deletion vs hard delete with archive; logic in database vs application; contract schema of views vs direct table access.
- Failed fetches: none on T1 sources. One T3 fetch failed (PostgREST schema isolation page, HTTP 429 twice), so claim DATA-C20 lacks its main T3 source.

## L2 claims

Clusters (agreement, certainty, ids):

1. Ownership and coupling: one application owns its database; others reach data through a service or a reporting copy; the database is an attached resource configured, not hard-coded. Consensus, grounded. DATA-C01, C02.
2. Schema as versioned, automated artifact: every change a migration in version control, applied only by automation, tested in CI on per-developer instances. Consensus, grounded. DATA-C03, C04.
3. Safe schema change over time: expand-migrate-contract, dual write then switch reads then switch writes then remove; renames/drops belong to the contract phase. Consensus, grounded (C35 inferred). DATA-C05, C06, C35.
4. Integrity in the database: declare keys, NOT NULL, foreign keys with ownership-driven ON DELETE, row-local CHECKs, partial unique indexes, exclusion constraints; index FK columns yourself. Consensus on mechanics, majority on the principle "database enforces what must always hold". Grounded. DATA-C07 to C13.
5. Types and keys: timestamptz, text, numeric, identity columns; generated columns for same-row derivation; key type is a live choice. Consensus for types, contested for keys. Grounded. DATA-C14 to C17.
6. Namespaces, views, roles, least privilege: schemas as namespaces, no application objects in public, separate owner and runtime roles, no superuser work, revoke PUBLIC defaults, RLS facts, scram-sha-256. Consensus on mechanics, inferred for the owner/runtime split, contested for contract schemas. Grounded/inferred. DATA-C18 to C27.
7. Zero-downtime DDL mechanics: lock levels, lock_timeout with retries, metadata-only column adds, NOT VALID then VALIDATE, CREATE INDEX CONCURRENTLY, type change as new column, batched backfills kept apart from schema migrations. Consensus, grounded. DATA-C28 to C34.
8. Connections and pooling: small server-side pool sized to cores, external pooler, transaction-pooling limits, reserved slots, idle-in-transaction timeout. Consensus, grounded (formula is a rule of thumb). DATA-C36 to C39.
9. Deletion, retention, history: soft deletion is disputed; time partitions make retention cheap; audit by trigger tables or pgaudit, no native temporal tables. Contested/majority, grounded for the sources read, open for consensus. DATA-C40 to C43.
10. Logic placement: constraints and few narrow triggers in the database, workflow in the application. Contested, inferred. DATA-C44, C45.
11. Backup and recovery: base backup plus continuous WAL archiving gives point-in-time recovery; test archiving and restores; dump is not PITR; config files and roles are not covered; repository off the database host; never disable fsync. Consensus, grounded (C47 inferred). DATA-C46 to C51.
12. Postgres as queue/cache (database side only): SKIP LOCKED for queues, enqueue in the same transaction, NOTIFY as wake-up only, UNLOGGED for rebuildable cache; scale ceiling of in-database queues. Consensus on mechanics, majority on the ceiling. Grounded. DATA-C52 to C56.

Live debates:
- Key type: bigint identity (compact, simple) vs UUIDv7 (time-ordered, globally unique, non-enumerable) vs UUIDv4 (random, poor index locality).
- Soft deletion (`deleted_at`) vs hard delete plus archive table or partition drop.
- Logic in the database (constraints, triggers, functions) vs application code.
- Contract schema (views/functions as the only consumer surface) vs consumers reading base tables directly.
- Postgres as job queue vs dedicated broker: majority view is "fine until lock contention under load", threshold open.

Not covered:
- Normalization theory beyond key/constraint mechanics (no T1/T2 normal-form source read).
- Replication, high availability, failover, major-version upgrades (out of scope list, not researched).
- Multi-tenancy models (schema-per-tenant vs row-level) beyond RLS facts; tagged SEC/ARCH.
- Indexing and query performance (OPS area); ORM behavior (APP area).
- Audit and temporal history from T1/T2 sources (only T3/T4 read).
- Managed-service specifics, extensions, encryption at rest, GDPR erasure procedures.

## L3 full

Reading method note: pages were fetched with the WebFetch tool, which returns an extraction by a small model, not raw text. Quotations below are as returned; claims that turn on exact wording should be re-checked against the page before the guideline quotes them.

### Source register

| id | tier | title | author / body | URL read | authoritative on |
|---|---|---|---|---|---|
| DATA-S01 | T1 | Constraints (5.5) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-constraints.html | CHECK, NOT NULL, UNIQUE, PK, FK, exclusion semantics |
| DATA-S02 | T1 | Schemas (5.10) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-schemas.html | namespaces, public schema, search_path, secure usage |
| DATA-S03 | T1 | Privileges (5.8) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-priv.html | ownership, GRANT/REVOKE, PUBLIC defaults |
| DATA-S04 | T1 | Continuous Archiving and PITR (25.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/continuous-archiving.html | base backup, WAL archiving, PITR |
| DATA-S05 | T1 | ALTER TABLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-altertable.html | lock levels, rewrites, NOT VALID |
| DATA-S06 | T1 | CREATE INDEX | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createindex.html | CONCURRENTLY behavior |
| DATA-S07 | T1 | Row Security Policies (5.9) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-rowsecurity.html | RLS semantics and leak caveats |
| DATA-S08 | T1 | UUID Functions (9.14) | PostgreSQL docs | https://www.postgresql.org/docs/current/functions-uuid.html | gen_random_uuid, uuidv7 |
| DATA-S09 | T1 | CREATE VIEW | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createview.html | view privileges, security_invoker/barrier |
| DATA-S10 | T1 | Role Attributes (21.2) | PostgreSQL docs | https://www.postgresql.org/docs/current/role-attributes.html | superuser caution, connection limit |
| DATA-S11 | T1 | CREATE ROLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createrole.html | group roles, privilege-bearing attributes |
| DATA-S12 | T1 | SELECT (locking clause) | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-select.html | FOR UPDATE SKIP LOCKED |
| DATA-S13 | T1 | Table Partitioning (5.12) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-partitioning.html | when partitioning helps, retention, limits |
| DATA-S14 | T1 | SQL Dump (25.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/backup-dump.html | pg_dump scope and limits |
| DATA-S15 | T1 | NOTIFY | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-notify.html | LISTEN/NOTIFY semantics and limits |
| DATA-S16 | T1 | CREATE TABLE | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createtable.html | identity columns, UNLOGGED |
| DATA-S17 | T1 | Client Connection Defaults (19.11) | PostgreSQL docs | https://www.postgresql.org/docs/current/runtime-config-client.html | lock_timeout, statement_timeout, idle_in_transaction_session_timeout |
| DATA-S18 | T1 | Connection Settings (19.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/runtime-config-connection.html | max_connections, reserved slots |
| DATA-S19 | T1 | Explicit Locking (13.3) | PostgreSQL docs | https://www.postgresql.org/docs/current/explicit-locking.html | lock modes, lock waiting, advisory locks |
| DATA-S20 | T1 | CREATE TRIGGER | PostgreSQL docs | https://www.postgresql.org/docs/current/sql-createtrigger.html | trigger kinds, constraint triggers, cautions |
| DATA-S21 | T1 | Reliability (28.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/wal-reliability.html | fsync, synchronous_commit, durability |
| DATA-S22 | T1 | pg_hba.conf (20.1) | PostgreSQL docs | https://www.postgresql.org/docs/current/auth-pg-hba-conf.html | auth methods, trust, scram-sha-256 |
| DATA-S23 | T1 | Generated Columns (5.4) | PostgreSQL docs | https://www.postgresql.org/docs/current/ddl-generated-columns.html | stored vs virtual generated columns |
| DATA-S24 | T1 | Migration Operations | Django docs | https://docs.djangoproject.com/en/stable/ref/migration-operations/ | RunPython, state vs database operations, PG caveat on schema+data |
| DATA-S25 | T2 | Evolutionary Database Design | M. Fowler, P. Sadalage | https://martinfowler.com/articles/evodb.html | migrations, VCS, CI, per-developer DB, DBA collaboration |
| DATA-S26 | T2 | Integration Database | M. Fowler | https://martinfowler.com/bliki/IntegrationDatabase.html | coupling cost of shared databases |
| DATA-S27 | T2 | Application Database | M. Fowler | https://martinfowler.com/bliki/ApplicationDatabase.html | single-owner database, services and reporting database |
| DATA-S28 | T2 | Parallel Change | D. Sato, M. Fowler | https://martinfowler.com/bliki/ParallelChange.html | expand-migrate-contract |
| DATA-S29 | T2 | The Twelve-Factor App, IV Backing services | A. Wiggins / Heroku | https://12factor.net/backing-services | database as attached resource |
| DATA-S30 | T3 | Online migrations at scale | Stripe Engineering | https://stripe.com/blog/online-migrations | four-step dual-write migration |
| DATA-S31 | T3 | Migration style guide | GitLab development docs | https://docs.gitlab.com/ee/development/migration_style_guide.html | zero-downtime rules, lock retries, batched migrations |
| DATA-S32 | T3 | Soft deletion probably isn't worth it | B. Leach | https://brandur.org/soft-deletion | argument against soft deletion |
| DATA-S33 | T3 | Transactionally staged job drains in Postgres | B. Leach | https://brandur.org/job-drain | dual-write problem, in-database job staging |
| DATA-S34 | T3 | Code in the database vs the app (fragment) | B. Leach | https://www.brandur.org/fragments/code-database-vs-app | position on logic placement |
| DATA-S35 | T3 | pgBackRest user guide | pgBackRest maintainers | https://pgbackrest.org/user-guide.html | backup types, retention, remote repository, restore verification |
| DATA-S36 | T3 | PgBouncer features | PgBouncer maintainers | https://www.pgbouncer.org/features.html | pooling modes, transaction-pooling incompatibilities |
| DATA-S37 | T3 | Don't Do This | PostgreSQL community wiki | https://wiki.postgresql.org/wiki/Don't_Do_This | type and syntax pitfalls |
| DATA-S38 | T3 | Number of Database Connections | PostgreSQL community wiki | https://wiki.postgresql.org/wiki/Number_Of_Database_Connections | pool sizing rule of thumb |
| DATA-S39 | T4 | UUIDv7 vs bigint search results (benchmark and blog posts, e.g. ardentperf.com UUID benchmark post) | various | search snippets only, not fetched | live debate on key type |
| DATA-S40 | T4 | Business logic in database vs application search results | various | search snippets only, not fetched | live debate on logic placement |
| DATA-S41 | T4 | PostgreSQL audit approaches search results | various | search snippets only, not fetched | catalogue of audit techniques |

Failed fetch: PostgREST "schema isolation" page (T3), HTTP 429 on both host spellings; not replaced by a copy.

### Claims

Format: id | claim | level | stack | sources | agreement | positions | certainty. Boundary tags in the claim line.

**Ownership, coupling, evolution**

- **DATA-C01** | A database should be owned by one application; other consumers reach its data through a service or a separate read-only reporting copy, not by sharing tables. | principle | neutral | S26, S27 | consensus | - | grounded. (boundary: ARCH)
- **DATA-C02** | The database is an attached resource addressed through configuration, so a different instance (for example one restored from backup) can be attached without code changes. | principle | neutral | S29 | consensus | - | grounded. (boundary: APP)
- **DATA-C03** | Every schema change should be a migration script held in version control with the application code, ordered, and applied only by automation, never by hand. | principle | neutral | S25, S24 | consensus | - | grounded.
- **DATA-C04** | Each developer should work on their own database instance, and migrations should run in the same continuous-integration pipeline as application code. | practice | neutral | S25 | consensus | - | grounded. (boundary: OPS)
- **DATA-C05** | A backward-incompatible schema change should proceed as expand (support old and new), migrate (move all clients), contract (remove old), so the system can be released in any phase. | principle | neutral | S28, S30, S31 | consensus | - | grounded.
- **DATA-C06** | Moving data to a new model should follow dual write, switch reads (verified by comparing old and new results), switch writes, then remove old data. | decision | neutral | S30, S28 | consensus | Detailed in one T3 source; T2 pattern is the generalization. | grounded.

**Integrity, keys, types**

- **DATA-C07** | Rules that must hold regardless of which code writes the data should be declared in the database as constraints, not only checked in application code. | principle | neutral | S01, S34, S26 | majority | Declare in DB: PostgreSQL docs (NOT NULL "in most designs the majority of columns"), S34 for deep consistency. App-only validation: common ORM practice, known only via S40 snippets. Applies when more than one writer or path can reach the data. | inferred (synthesis of S01, S34, S26).
- **DATA-C08** | Every table should have a primary key. | practice | postgres | S01 | consensus | - | grounded.
- **DATA-C09** | Most columns should be NOT NULL; nullable columns are the exception that needs a reason. | practice | postgres | S01 | consensus | - | grounded.
- **DATA-C10** | Foreign keys should be declared, with ON DELETE chosen by ownership: CASCADE for a component that cannot exist alone, RESTRICT or NO ACTION for independent objects, SET NULL for optional links. | practice | postgres | S01 | consensus | - | grounded.
- **DATA-C11** | Columns that reference another table should be indexed explicitly, because PostgreSQL does not index foreign-key columns automatically. | practice | postgres | S01 | consensus | - | grounded.
- **DATA-C12** | CHECK constraints should be row-local and immutable; a CHECK passes on NULL, so pair it with NOT NULL; cross-row rules need a unique index, exclusion constraint or constraint trigger. | practice | postgres | S01, S20 | consensus | - | grounded.
- **DATA-C13** | Conditional uniqueness should use a partial unique index (or NULLS NOT DISTINCT where NULLs must collide), and overlap rules an exclusion constraint. | practice | postgres | S01 | consensus | - | grounded.
- **DATA-C14** | Prefer timestamptz, text (with CHECK for limits), numeric (not money), and identity columns over timestamp without time zone, char(n), money, and serial. | practice | postgres | S37, S16 | consensus | - | grounded.
- **DATA-C15** | The primary-key type is a decision to record: bigint identity, UUIDv7, or UUIDv4. | decision | postgres | S16, S08, S39 | contested | Identity: compact, sequential, standard (S16), but guessable and tied to one database. UUIDv7: time-ordered with millisecond timestamp, good index locality, globally unique, non-enumerable (S08 documents ordering, S39 benchmarks, T4). UUIDv4: random, poor B-tree locality (S39). Choose by need for external identifiers and cross-system uniqueness; test locality claims on the workload. (boundary: API for exposing keys) | grounded for mechanics, open for the recommendation.
- **DATA-C16** | A UUIDv7 timestamp should not be used as the creation time; keep an explicit timestamptz column. | practice | postgres | S08 | consensus | - | grounded.
- **DATA-C17** | Values derivable from the same row should be generated columns (stored if read often or replicated logically) rather than application-maintained copies. | practice | postgres | S23 | consensus | - | grounded.

**Namespaces, views, roles**

- **DATA-C18** | Schemas should be used as namespaces to group objects by owner or purpose, and application objects should not live in the shared public schema. | decision | postgres | S02 | majority | S02 describes schemas as namespaces and the user-private-schema pattern; "not in public" is the secure pattern, not a stated universal rule. | inferred.
- **DATA-C19** | search_path should be set explicitly and minimal, because adding a schema to it trusts everyone with CREATE on that schema; revoke CREATE on public from PUBLIC. | practice | postgres | S02 | consensus | - | grounded. (boundary: SEC)
- **DATA-C20** | Consumers (application server, reporting) may be given a dedicated contract schema of views and functions while base tables stay hidden, so storage can change without breaking consumers. | decision | postgres | S09, S26 | contested | For: contract schema (database-as-API style, T3 source not read because fetch failed; S09 shows views give restricted access under owner privileges). Against/alternative: consumers use base tables through an ORM and rely on migrations discipline (S25, S28). Applies when several consumers or strict privilege separation exist. (boundary: API) | inferred.
- **DATA-C21** | Views run with the owner's privileges by default; use security_invoker when the caller's rights or row policies must apply, and security_barrier for views used as row filters. | practice | postgres | S09 | consensus | - | grounded. (boundary: SEC)
- **DATA-C22** | The role that owns objects and runs migrations should differ from the role the application uses at runtime, which gets only the DML privileges it needs. | decision | postgres | S03, S10, S11, S02 | consensus | S03: ownership rights cannot be granted separately; S10: do most work as a non-superuser. The split itself is a synthesis. | inferred.
- **DATA-C23** | Privileges should be granted to NOLOGIN group roles, and login roles made members. | practice | postgres | S11, S03 | consensus | - | grounded.
- **DATA-C24** | Day-to-day work and the application must not run as superuser; grant the narrow attributes needed instead. | practice | postgres | S10, S11 | consensus | - | grounded. (boundary: SEC)
- **DATA-C25** | PUBLIC defaults (CONNECT and TEMPORARY on databases, EXECUTE on functions) should be revoked where not wanted, ALTER DEFAULT PRIVILEGES used for future objects, and the REVOKE done in the same transaction as the creation. | practice | postgres | S03 | consensus | - | grounded. (boundary: SEC)
- **DATA-C26** | Row-level security, when used, is default-deny once enabled, but table owners bypass it unless FORCE is set, unique and foreign-key checks bypass it, and policies with sub-selects have race and leak caveats. | practice | postgres | S07 | consensus | Whether to use RLS or application-side tenant filtering is not settled by the source. | grounded for facts, open for the decision. (boundary: SEC)
- **DATA-C27** | Password authentication should use scram-sha-256, trust only for local sockets, and remote connections should require TLS (hostssl). | practice | postgres | S22 | consensus | - | grounded. (boundary: SEC)

**Zero-downtime schema change**

- **DATA-C28** | Because most ALTER TABLE forms take ACCESS EXCLUSIVE (blocking even reads) and waiting lock requests queue everything behind them, migrations should set a short lock_timeout and retry. | practice | postgres | S05, S19, S17, S31 | consensus | - | grounded.
- **DATA-C29** | lock_timeout, statement_timeout and idle_in_transaction_session_timeout should be set per role or session, not globally in the server configuration. | practice | postgres | S17 | consensus | - | grounded. (boundary: OPS)
- **DATA-C30** | Adding a column with a non-volatile default is metadata-only; volatile defaults, identity, stored generated columns and constrained domains rewrite the table and need the multi-step route. | practice | postgres | S05, S31 | consensus | - | grounded.
- **DATA-C31** | Constraints on large tables should be added NOT VALID and then validated in a separate step (lower lock level); SET NOT NULL can skip the scan when a validated CHECK proves it. | practice | postgres | S05, S31 | consensus | - | grounded.
- **DATA-C32** | Indexes on live tables should be built with CREATE INDEX CONCURRENTLY, outside a transaction block, and a failed build leaves an invalid index to drop and retry. | practice | postgres | S06, S31 | consensus | - | grounded.
- **DATA-C33** | A column type change rewrites the table; on large tables do it as add new column, backfill, switch, drop. | practice | postgres | S05, S28 | consensus | - | inferred (S05 for the rewrite, S28 for the pattern).
- **DATA-C34** | Large data backfills should run in batches outside the schema migration, and schema and data changes should not share one migration transaction. | practice | postgres | S31, S24 | consensus | - | grounded.
- **DATA-C35** | Column drops and renames used by running code belong to the contract phase, after no deployed version references the old name. | practice | neutral | S28, S30 | consensus | - | inferred.

**Connections and pooling**

- **DATA-C36** | Server-side concurrency should be kept small (rule of thumb: cores x 2 plus effective spindles) and enforced by an external pooler; max_connections should exceed the pool total slightly. | decision | postgres | S38, S18 | consensus | The formula is a heuristic from one T3 source; PostgreSQL docs only describe the settings. | grounded. (boundary: APP, OPS)
- **DATA-C37** | Transaction-mode pooling breaks session state: SET/RESET, LISTEN, WITH HOLD cursors, session-level advisory locks, and prepared statements (in PgBouncer's documented modes) must be avoided or session mode used. | practice | postgres | S36, S19, S15 | consensus | - | grounded. (boundary: APP)
- **DATA-C38** | Per-role connection limits and reserved connection slots should keep administrative access possible when the pool saturates. | practice | postgres | S10, S18 | consensus | - | grounded.
- **DATA-C39** | idle_in_transaction_session_timeout should be set so abandoned transactions do not hold locks or block vacuum. | practice | postgres | S17 | consensus | - | grounded. (boundary: OPS)

**Deletion, retention, history**

- **DATA-C40** | Deletion strategy is a decision to record: soft delete via deleted_at, hard delete with an archive table (for example jsonb), or hard delete only. | decision | postgres | S32, S41 | contested | Archive/hard delete: S32 (soft deletion leaks into every query, defeats foreign keys, complicates erasure, undelete rarely used). Soft delete flag: listed as a standard approach in S41 (T4), common in practice. Applies: soft delete when users need undo in the product itself; otherwise archive. (boundary: SEC for erasure obligations) | grounded for S32, open for consensus.
- **DATA-C41** | Time-based retention is cheapest with partitions: dropping or detaching (DETACH CONCURRENTLY) a partition replaces bulk DELETE and vacuum. | practice | postgres | S13 | consensus | - | grounded.
- **DATA-C42** | Partitioning should be adopted only when size justifies it (rule of thumb: table larger than memory); partition keys must be part of primary and unique keys. | practice | postgres | S13 | consensus | - | grounded.
- **DATA-C43** | Row-change history should be recorded by trigger-written audit tables (queryable in SQL) and statement-level audit by pgaudit/logging; PostgreSQL has no native temporal tables. | decision | postgres | S20, S41 | majority | Triggers for row history, pgaudit for who-ran-what (S41, T4 snippets); S20 lists auditing as a trigger use. No T1/T2 source on audit design read. (boundary: SEC) | inferred.

**Logic in the database**

- **DATA-C44** | Logic placement is a decision to record: constraints and referential rules in the database, workflow and business rules in the application. | decision | neutral | S34, S20, S40, S01 | contested | Minimal DB code (S34: only automated timestamps and deep consistency; opaque side effects, weak tooling, deployment friction). Constraints always in DB (S01). Heavier DB logic: for set-based bulk work and security boundaries (S40, T4). Applies by writer count and operation shape. | inferred.
- **DATA-C45** | Triggers should be few, narrow and documented (updated_at, cross-table consistency, audit), because they hide side effects from application code and fire in name order. | practice | postgres | S34, S20 | majority | S20 lists many valid trigger uses; S34 argues for sparing use. | grounded.

**Backup and recovery**

- **DATA-C46** | Recovery to a chosen moment requires a base backup plus continuous WAL archiving; the archive command must succeed only on real success and refuse to overwrite. | decision | postgres | S04, S35 | consensus | - | grounded.
- **DATA-C47** | Archiving should be set up, tested and monitored before the first base backup, and restores rehearsed, since a backup is only proven by a restore. | practice | postgres | S04, S35 | consensus | S04 states test-and-monitor archiving; restore rehearsal is stated in the extraction of S04 and supported by S35 restore verification. Re-check wording. | inferred.
- **DATA-C48** | pg_dump gives a consistent logical snapshot of one database, excludes roles and tablespaces (use pg_dumpall), and is not point-in-time recovery. | practice | postgres | S14, S04 | consensus | - | grounded.
- **DATA-C49** | Configuration files (postgresql.conf, pg_hba.conf) are not restored by WAL replay and must be kept in version control. | practice | postgres | S04 | consensus | - | grounded. (boundary: OPS)
- **DATA-C50** | The backup repository should be separate from the database host, with a retention policy and tracked full/differential/incremental chains. | practice | postgres | S35, S04 | consensus | - | grounded.
- **DATA-C51** | fsync must not be disabled and storage write caches must be safe; synchronous_commit is the explicit durability/latency trade-off. | practice | postgres | S21 | consensus | - | grounded. (boundary: OPS)

**Postgres as queue and cache (database side)**

- **DATA-C52** | A Postgres-backed queue should claim rows with FOR UPDATE SKIP LOCKED, which is for queue-like tables only because it gives an inconsistent view. | practice | postgres | S12 | consensus | - | grounded.
- **DATA-C53** | Background jobs should be enqueued in the same transaction as the data change (staged in a table), so a crash cannot lose or prematurely run a job; consumers must be idempotent (at-least-once). | decision | postgres | S33 | consensus | - | grounded. (boundary: APP)
- **DATA-C54** | An in-database queue is adequate until lock contention under load; beyond that, stage in Postgres and drain to a dedicated queue. | decision | postgres | S33 | majority | One T3 source states the ceiling; threshold unquantified. | open on threshold.
- **DATA-C55** | LISTEN/NOTIFY should be a wake-up signal only: it is delivered at commit, is not durable, has an 8000-byte payload limit, and a full queue makes committing transactions fail; the data stays in tables. | practice | postgres | S15 | consensus | - | grounded.
- **DATA-C56** | Rebuildable cache data may live in UNLOGGED tables (fast, truncated on crash, not replicated); anything not rebuildable must not. | decision | postgres | S16 | consensus | - | grounded.

### Gaps (open)

- No T1/T2 source read on normalization (3NF and beyond) or on denormalization trade-offs; kept out of claims.
- Audit and temporal history: only T3/T4 evidence (DATA-C43).
- Contract-schema pattern: main T3 source failed to load (DATA-C20).
- Key type recommendation (DATA-C15): benchmark evidence is T4 only.
- RPO/RTO as the decision that drives backup design: not stated in any source read; likely to appear in OPS.
- Replication, high availability, major upgrades, multi-tenancy models, encryption at rest, erasure procedures: not researched.
- Kleppmann (Designing Data-Intensive Applications) is a T2 authority in scope but was not available as a fetchable page; not used.
