# Research result: 10_data_change (area DATA)

## L1 headline

Public best practice on changing persistent data and schemas safely is mature and mostly consensual on mechanism (version-controlled ordered migrations in the delivery pipeline, schema change decoupled from application release, expand/migrate/contract, lock-aware DDL, batched resumable backfills, restore as the true undo), but contested on three decisions (written undo versus roll-forward, testing on real data versus synthetic data, declarative versus versioned migrations) and thin at T1/T2 on backfills and data-migration testing, where the best sources are T3 engineering blogs and tool docs; certainty: grounded for the mechanisms, inferred for the mapping to the maintainer's claims, open for about eight maintainer claims with no public counterpart.

Pinned:
- Sources read: 22, by tier: 9 T1 (official tool and platform docs, DORA), 5 T2, 8 T3, 0 T4. One further T2 source (Designing Data-Intensive Applications ch. 4) could not be read (fetch failed, HTTP 403) and is used only as an inferred pointer.
- Claims: 43 (DATA-C01 to DATA-C43), of which 4 record a missing public counterpart (C35 to C38).
- Contested topics (7): written undo versus roll-forward with backward compatibility (C10); real production-shaped data versus synthetic data for migration tests (C26); declarative versus versioned migrations (C04); manual versus automated production application (C33); where a large backfill runs: in the migration, as a background job, or offline from a snapshot (C24); view versus function or access layer as the compatibility surface (C32); registry content by script versus migration (C35).
- Failed fetches on T1 sources: none. Failed fetches on others: DDIA ch. 4 (O'Reilly, 403), two Liquibase pages (404; replaced by the Liquibase rollback docs page), one Braintree blog (redirect to unrelated page), a Princeton DDIA PDF (404).

## L2 claims

Clusters (claim ids; agreement; certainty):

1. Data changes are a delivery risk managed inside the same pipeline: version-controlled, ordered, tracked, automated migrations; never ad-hoc manual SQL. Consensus, grounded. DATA-C01, C02, C03, C42. (Public counterpart of MAINT-C22, C23.)
2. Schema change is decoupled from application release; the schema is changed first to support both versions; backward-incompatible changes go through expand, migrate, contract, with the contract step explicitly scheduled and a stated cost (two structures, dual logic). Consensus, grounded. DATA-C05, C06, C07, C08, C09, C43. (MAINT-C31, C32 additive/coordinated changes; the "no version numbers" part has no public position.)
3. Rollback of data changes: the common authority view is that automatic down scripts are unreliable for destructive or data-bearing changes, so teams combine backward compatibility, roll-forward, and a tested restore; a minority (Liquibase, GitLab) requires a written reverse for every migration. Contested, grounded. DATA-C10, C11, C12, C13, C40. (MAINT-C24 sits between the two: written undo, not generated, forward-only.)
4. Locks govern what is safe: most ALTER TABLE forms take the strongest lock; use non-blocking forms (NOT VALID then validate, concurrent index, metadata-only defaults, INSTANT or INPLACE), set lock timeouts per session with retry, lint migrations, use online-change tools for big tables. Consensus, grounded; stack-tagged to Postgres and MySQL. DATA-C15, C16, C17, C18, C19, C20. (MAINT-C26, C34, C40.)
5. Backfills are batched, throttled, resumable, idempotent, kept out of the DDL transaction, paced by replica lag, and bounded by time budgets; where they run is a decision. Majority, grounded for the practice, T3 only for most of it. DATA-C21, C22, C23, C24, C25. (MAINT-C35 to C41.)
6. Migration testing: run migrations on production-size or production-shaped data and measure time and locks; masking is required when real data holds personal data; the counter-position keeps per-developer databases with versioned sample data. Contested, grounded, vendor-heavy (T3). DATA-C26, C27, C28, C29. (MAINT-C01, C29.)
7. Verify the new data before the old is removed: shadow reads compared against the old path, out-of-band validation jobs, soft deletion as first defense, restore tested. Majority, grounded, mostly T3 and one T2 (Google SRE). DATA-C14, C39, C40, C41, C12.
8. Human gate on change: involve the people who own the production database; whether production application is manual or automatic is contested. DATA-C31, C33, C34. (MAINT-C26, C27, C28, C34.)
9. Declarative (desired state) versus versioned (change script) schema management; official tool docs recommend a hybrid. Contested, grounded, vendor source. DATA-C04.
10. Maintainer claims with no public counterpart found: registry content by script, ticket key inside statements, convergence query as done, explicit opt-in for unbounded destructive ops, schema-version gate on deploy, named senior approvers by risk, no version numbers on interfaces, function-with-signature as stable interface. Open. DATA-C35 to C38, and boundary notes in C31, C32, C34.

Mapping of the maintainer's data-change claims to public positions (for / against):
- MAINT-C22 once-only tracked migrations: for = DORA, Fowler/Sadalage, Atlas versioned (C02). Against = declarative schema management (C04).
- MAINT-C23 never edit applied migration: for = Liquibase checksums and advice to roll back before editing, Atlas integrity file (C03). Against: none found.
- MAINT-C24 written undo, not automatic down: for = Liquibase "write rollback for every changeset", GitLab "must be reversible". Against = Fowler/Sadalage ("not cost effective", prefer compatibility), Redgate (compatibility and backups over undo). The maintainer's variant (prepared ahead, hand-written) is closest to Liquibase custom rollback (C10).
- MAINT-C25 idempotent DDL: for = Airflow idempotence rule transferred to jobs; no T1 or T2 source on DDL itself (C22, inferred).
- MAINT-C26 split by risk, long or lock-taking changes manual: for = GitLab (regular versus post-deployment versus batched background; 3 and 10 minute budgets), Strong Migrations (non-transactional migrations for concurrent indexes). Against = DORA and CD consensus that production application is automated (C33).
- MAINT-C27 manual production run by authorized people: for = GitLab post-deployment at release manager discretion; DORA "discuss with production DB owners". Against = automation-first position (C33). Note: Fowler/Sadalage's "never apply manually" means never hand-typed SQL, not that the trigger must be automatic.
- MAINT-C28 deploy gated on schema version: for = Fowler blue-green sequence (schema first, check, then app); no public explicit version gate (C34, open).
- MAINT-C29 CI on a data dump: for = GitLab migration pipeline with timing, DBLab and Neon clones (C26, C28). Against = Fowler/Sadalage sample-data-in-VC. The partial-dump skip marker has no counterpart.
- MAINT-C30 registry content by script outside migrations: partial = Fowler/Sadalage separate folder for data fixes (C29); the script-as-source-of-truth part has no public position (C35, open).
- MAINT-C31 additive, coordinated breaking, no version numbers: for = parallel change; DDIA compatibility (inferred). Against: versioned interfaces apply to remote APIs (Parallel Change names remote API evolution) (C32).
- MAINT-C32 deprecate, keep, remove later: for = Fowler/Sadalage transition period (C32).
- MAINT-C34 escalate by risk to named approvers: for = DORA (C31); the risk criteria (locks, duration, availability) match Postgres lock docs (C15).
- MAINT-C35 to C41 bulk procedure: for = Strong Migrations (batches, throttling, own migration), GitLab (batched background), Stripe (offline backfill, shadow verification), gh-ost (pause, lag limit, mid-run controls), Airflow (idempotent, bounded) (C21 to C25). Against: none; the "do not shard schema changes" rule is supported by lock mechanics (C20). Convergence query, ticket key in statement, ramp ladder: no public counterpart (C37).
- MAINT-C01 and C03 real data in rollback boundary: for = DBLab, Neon, GitLab (production-like data); the rolled-back transaction as harness has no public source (C26). Against = isolated developer databases and sample data (Fowler/Sadalage), and PII exposure (Neon).
- MAINT-C16 explicit opt-in for unbounded destructive operations: nearest = migration linters (Squawk, Strong Migrations) that refuse unsafe operations unless asserted (C38).

Live debates (forces in tension):
- Written undo versus roll-forward plus backward compatibility: reversibility and control versus cost of ownership and honesty about data loss (C10).
- Real or production-sized data versus synthetic data for migration tests: confidence and realistic timing versus isolation, personal-data exposure and cost of cloning (C26, C27).
- Declarative versus versioned migrations: developer cognitive load versus auditability and determinism (C04).
- Manual versus automated production application: reversibility and control versus delivery speed (C33).
- Backfill placement (in migration, background job, offline snapshot): simplicity versus impact on production and speed (C24).
- Compatibility surface as view or access layer versus function with signature: simplicity versus change absorption (C32; the public side favors views and a database access layer, the maintainer favors functions).
- Dual-write expand/contract versus a short maintenance window: availability versus cost of two structures and duration (C07, C14; the window position has no strong public advocate in this evidence, see gaps).

Candidate central decisions (others depend on them):
1. Whether every data change is a recorded migration in the delivery pipeline, and which kinds (long, locking, non-transactional, bulk) leave the default path (C02, C33).
2. How a backward-incompatible change is made: expand/migrate/contract with an owner for the contract step, versus a coordinated window (C06, C07).
3. What the undo of a data change is: written reverse, backward compatibility plus roll-forward, or restore, and what is tested (C10, C12).
4. Where migrations are rehearsed: what data, how real, how masked (C26, C27).
5. How a large data change is executed and declared done: batching, idempotence, pacing signals, convergence criterion (C21 to C25, C37).

What this slot did not cover: the physical backup and recovery design (only its role as undo), event sourcing and NoSQL migration (DORA lists them, not read in depth), zero-downtime change for non-relational stores, change data capture based migrations, data migration between systems (platform moves), data privacy law, schema registries for message formats (boundary: contract testing in VERIFY), and Humble and Farley's Continuous Delivery data chapter (not obtainable as text; its positions are represented only through Fowler and DORA).

## L3 full

### Source register

- DATA-S01, T2, Evolutionary Database Design, Fowler and Sadalage, https://martinfowler.com/articles/evodb.html. Authoritative on: migrations as first-class artifacts, small changes, per-developer databases, transition phase, data-fix folder, reverse migrations stance.
- DATA-S02, T2, Parallel Change, Fowler, https://martinfowler.com/bliki/ParallelChange.html. Expand, migrate, contract; drawbacks.
- DATA-S03, T2, Blue-Green Deployment (database section), Fowler, https://martinfowler.com/bliki/BlueGreenDeployment.html. Schema deployed separately and before the application.
- DATA-S04, T1, Database change management capability, DORA, https://dora.dev/capabilities/database-change-management/. Version-controlled scripts, sequencing, online schema tools, parallel change, expert communication.
- DATA-S05, T1, Explicit Locking (PostgreSQL docs), https://www.postgresql.org/docs/current/explicit-locking.html. ACCESS EXCLUSIVE semantics.
- DATA-S06, T1, ALTER TABLE (PostgreSQL docs), https://www.postgresql.org/docs/current/sql-altertable.html. Rewrites, NOT VALID, lock levels.
- DATA-S07, T1, Client connection defaults: lock_timeout and statement_timeout (PostgreSQL docs), https://www.postgresql.org/docs/current/runtime-config-client.html.
- DATA-S08, T1, InnoDB Online DDL operations (MySQL 8.4 docs), https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html.
- DATA-S09, T2, Data Integrity: What You Read Is What You Wrote (Google SRE book ch. 26), https://sre.google/sre-book/data-integrity/. Defense in depth, restores, soft deletion, validation pipelines.
- DATA-S10, T1, Undo migrations (Flyway documentation, Redgate), https://documentation.red-gate.com/flyway/flyway-concepts/migrations/undo-migrations.
- DATA-S11, T1, Rollback (Liquibase documentation), https://docs.liquibase.com/concepts/changelogs/rollback.html.
- DATA-S12, T1 (tool vendor docs), Declarative vs Versioned migrations (Atlas), https://atlasgo.io/concepts/declarative-vs-versioned.
- DATA-S13, T1, Best Practices (Apache Airflow docs), https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html. Idempotent, bounded tasks; pipeline stack.
- DATA-S14, T3, Migration style guide (GitLab development docs), https://docs.gitlab.com/development/migration_style_guide/.
- DATA-S15, T3, gh-ost: GitHub's online migration tool for MySQL (GitHub blog), https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/.
- DATA-S16, T3, Online migrations at scale (Stripe blog), https://stripe.com/blog/online-migrations.
- DATA-S17, T3, Strong Migrations README (maintainer of the tool), https://github.com/ankane/strong_migrations. Ruby on Rails with Postgres, MySQL.
- DATA-S18, T3, Squawk README, https://github.com/sbdchd/squawk. Postgres.
- DATA-S19, T3, Expand and contract pattern (Prisma Data Guide), https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern.
- DATA-S20, T3, DBLab Engine docs (Postgres.ai), https://postgres.ai/docs/database-lab. Vendor.
- DATA-S21, T3, Environments with masked production data (Neon blog), https://neon.com/blog/environments-masked-production-data. Vendor.
- DATA-S22, T2, Database Refactoring (Ambler and Sadalage), http://databaserefactoring.com/. Definition and catalog only; the page did not discuss transition periods.
- DATA-S23, T2, Designing Data-Intensive Applications ch. 4 (Kleppmann). NOT READ: O'Reilly fetch returned 403. Only a search-result summary was seen (backward and forward compatibility during rolling upgrades, "data outlives code"). Used for inferred pointers only.

### Claims

**DATA-C01**
- claim: Treat database change as a primary delivery risk and manage it in the same pipeline as application change, not as a separate manual track.
- level: principle
- stack: neutral
- sources: S04 (capability definition, key claims), S01
- agreement: consensus
- certainty: grounded

**DATA-C02**
- claim: Express every schema and data change as a migration script in version control, ordered by a unique sequence, applied by automation, never by hand-typed ad-hoc SQL.
- level: practice
- stack: neutral
- sources: S01 (migrations, automation), S04 (version control and migration scripts), S12 (versioned approach)
- agreement: consensus
- certainty: grounded

**DATA-C03**
- claim: Keep a per-database record of which migrations have run, and do not edit a migration that has been applied; correct it with a new migration.
- level: practice
- stack: neutral
- sources: S04 (tracking executed migrations), S11 (checksum caution: roll back before editing a changeset), S12 (integrity file)
- agreement: majority
- positions: strict immutability (checksum-enforced) serves correctness and reproducibility; Liquibase allows editing after rolling the changeset back. The strict form wins wherever more than one environment has applied the change.
- certainty: grounded for tracking and checksums; the "never edit" form is inferred from S11 and S12

**DATA-C04**
- claim: Decide per team whether the source of truth is the desired schema state (declarative) or the ordered change scripts (versioned), and record why.
- level: decision
- stack: neutral
- sources: S12 (both approaches, hybrid recommendation)
- agreement: contested
- positions: declarative serves developer cognitive load and fast iteration, and wins for fast local loops and when CI can reach the database; versioned serves auditability, determinism and offline CI, and wins under compliance, many instances, or packaged software; hybrid (develop declaratively, generate versioned files for review and deploy) is the vendor recommendation. Only a tool vendor source; T2 position not found.
- certainty: grounded (one vendor source)

**DATA-C05**
- claim: Deploy schema changes separately from, and before, the application version that needs them; the first schema step must support both old and new application versions.
- level: principle
- stack: neutral
- sources: S03 (database section), S01 (transition and compatibility), S04 (parallel change decouples database and application)
- agreement: consensus
- certainty: grounded

**DATA-C06**
- claim: Make a backward-incompatible change (rename, type change, split, move) as expand, migrate, contract: add the new structure beside the old, move writers and readers, backfill, then remove the old.
- level: principle
- stack: neutral
- sources: S02 (three phases), S19 (seven steps), S16 (four-step dual writing), S04
- agreement: consensus
- certainty: grounded

**DATA-C07**
- claim: Schedule and own the contract step; an unfinished contract leaves a state worse than the start, and the migrate phase carries two structures and dual-path code.
- level: practice
- stack: neutral
- sources: S02 (Drawbacks), S19 (Tradeoffs)
- agreement: consensus (the cost is stated in both; no source argues against)
- certainty: grounded

**DATA-C08**
- claim: Make each database change as small as possible, so errors are quick to spot.
- level: practice
- stack: neutral
- sources: S01 (small changes), S16 (never more than a few hundred lines at a time)
- agreement: consensus
- certainty: grounded

**DATA-C09**
- claim: Code is deployed over a window in which old and new versions run against the same data, so every stored-data change must be readable and writable by both versions across that window.
- level: principle
- stack: neutral
- sources: S03, S02 (Deployments scenario), S23 (not read; summary only)
- agreement: consensus
- certainty: inferred (S03 and S02 grounded; the data-compatibility framing from S23 unread)

**DATA-C10**
- claim: Decide how a failed data change is undone before it ships: a written reverse for each migration, or backward compatibility plus roll-forward plus restore; record the choice.
- level: decision
- stack: neutral
- sources: S01 (reverse migrations: not cost effective, prefer compatibility), S10 (compatibility and backups over undo), S11 (write rollback for every changeset; drops and deletes not auto-reversible), S14 (migrations must be reversible, even irreversible ones carry an explained down)
- agreement: contested
- positions: (a) written reverse for every migration: held by Liquibase and GitLab; serves reversibility and downgrade after a vulnerability; wins for regulated or packaged software with many installed versions. (b) backward compatibility plus roll-forward plus restore, no generated undo: held by Fowler/Sadalage and Redgate; serves cost of ownership (undo scripts are untested code) and honesty about data loss; wins for continuously deployed services with one production. (c) maintainer variant: forward-only with a hand-written undo section prepared ahead (MAINT-C24), a hybrid of (a) and (b).
- certainty: grounded

**DATA-C11**
- claim: Treat destructive changes (drop, delete, truncate) as not reversible by script; their undo is a restore of data, so prepare and test it before running them.
- level: principle
- stack: neutral
- sources: S11 (Non-auto-rollbackable), S10 (Key limitations), S09 (restores)
- agreement: consensus
- certainty: grounded

**DATA-C12**
- claim: Define a backup by whether it restores; test restores regularly and keep the restore path independent of schema-change tooling.
- level: practice
- stack: neutral
- sources: S09 (restores matter; recovery testing), S10 (backup strategy independent of structure)
- agreement: consensus
- certainty: grounded
- boundary: OPERATE

**DATA-C13**
- claim: Treat the last reversible point as the state before the old structure is removed and before reads move irreversibly; after new-only data accumulates, going back loses it.
- level: practice
- stack: neutral
- sources: S19 (Rollback Capability), S03 (rollback point after schema step)
- agreement: majority
- certainty: grounded

**DATA-C14**
- claim: Before cutting reads to a new structure, run old and new paths side by side and alert on mismatch (shadow read comparison).
- level: practice
- stack: neutral
- sources: S16 (Verification: Scientist)
- agreement: majority (single T3 source, S19 lists "test the new interface")
- certainty: grounded (one source)

**DATA-C15**
- claim: Know the lock a statement takes before running it on a shared database; most ALTER TABLE forms take the strongest lock and block all access, and rewriting forms need extra disk and are not MVCC-safe.
- level: principle
- stack: Postgres, MySQL (general idea neutral)
- sources: S05 (ACCESS EXCLUSIVE), S06 (Lock Levels, Table Rewrites, MVCC Caveat), S08 (algorithm and LOCK clause)
- agreement: consensus
- certainty: grounded
- boundary: ADOPT, database design

**DATA-C16**
- claim: Run migrations with a per-session lock timeout (not set globally) and retry on timeout, so a blocked DDL statement does not queue and starve the table.
- level: practice
- stack: Postgres
- sources: S07 (lock_timeout, not in postgresql.conf), S14 (lock retries)
- agreement: majority
- certainty: grounded for the timeout; the starvation reason is inferred (S05, S14)

**DATA-C17**
- claim: Prefer the non-blocking form of each change: add constraints as not-yet-validated then validate separately, build indexes concurrently, add columns without volatile defaults, request metadata-only or in-place algorithms with an explicit no-lock clause.
- level: practice
- stack: Postgres, MySQL
- sources: S06 (NOT VALID, VALIDATE, defaults), S08 (INSTANT, INPLACE, LOCK=NONE), S17 (safe alternatives), S18 (rules)
- agreement: consensus
- certainty: grounded

**DATA-C18**
- claim: Run operations that cannot execute inside a transaction (concurrent index builds) in their own non-transactional step, apart from transactional changes.
- level: practice
- stack: Postgres (Rails tool as source)
- sources: S17 (indexes), S14 (separate migration for steps that cannot be in one transaction)
- agreement: consensus
- certainty: grounded

**DATA-C19**
- claim: Lint migrations in CI against a rule list of unsafe operations, and require an explicit assertion to override a rule.
- level: practice
- stack: Postgres, Rails
- sources: S17 (dangerous operations, safety_assured), S18 (rules)
- agreement: majority (T3, tools in the same niche)
- certainty: grounded

**DATA-C20**
- claim: For large tables where in-place DDL blocks, use an online schema change tool that copies and swaps (triggerless and pausable preferred), and do not shard whole-object schema changes.
- level: decision
- stack: MySQL (gh-ost, pt-online-schema-change), Postgres equivalents
- sources: S04 (online migration frameworks), S15 (trigger drawbacks, pause, test-on-replica, postponable cutover), S05 (whole-table locks)
- agreement: majority
- positions: trigger-based tools are simpler and older but add write overhead and cannot pause (S15); log-based tools serve control and low impact and win on high-write masters; native online DDL (S08) wins when the operation is metadata-only. 
- certainty: grounded

**DATA-C21**
- claim: Run a large backfill in bounded batches with throttling pauses, in its own step, never inside a long DDL transaction.
- level: practice
- stack: neutral (examples Rails, Postgres)
- sources: S17 (Backfilling Stance), S14 (batched background migrations), S16 (backfill)
- agreement: consensus
- certainty: grounded

**DATA-C22**
- claim: Make each backfill batch re-runnable with the same result: upsert not insert, partition by a fixed key, never read "latest" data inside the job.
- level: practice
- stack: neutral (source is a pipeline scheduler)
- sources: S13 (Idempotent Tasks, Partitioned/Bounded Backfill)
- agreement: majority
- certainty: inferred (S13 states the rule for scheduled tasks; transfer to data migrations is our reading)

**DATA-C23**
- claim: Make a long data job pausable and pace it on the target system's health, replica lag first, with mid-run adjustment of batch size and lag limit.
- level: practice
- stack: neutral (MySQL tool as source)
- sources: S15 (pause, max-lag, dynamic controls)
- agreement: majority (single T3 source, plus S17 sleep between batches)
- certainty: grounded

**DATA-C24**
- claim: Decide where a backfill runs: inside a migration step with a time budget, as an application background job triggered by a migration, or offline from a snapshot; record why.
- level: decision
- stack: neutral
- sources: S14 (post-deployment migrations versus batched background migrations), S16 (offline snapshot backfill), S17 (separate migration)
- agreement: contested
- positions: in-migration serves simplicity and one delivery path and wins when the work is minutes; background job serves production safety and wins for long work; offline snapshot serves zero load on production and wins for very large, multi-table moves with analytic tooling; each is held by a different T3 source.
- certainty: grounded

**DATA-C25**
- claim: Give migrations a time budget by class, so the long ones are identified before deploy (one source: regular up to 3 minutes, post-deployment up to 10, queries under 1 second).
- level: practice
- stack: neutral (numbers are one team's)
- sources: S14 (Time Limits)
- agreement: majority (one T3 source; maintainer uses about 5 minutes)
- certainty: grounded (one source)

**DATA-C26**
- claim: Decide what data migrations are rehearsed on: production-sized or production-shaped data (to measure time, locks, plan) or synthetic developer data (for isolation and no personal data); record the choice.
- level: decision
- stack: neutral
- sources: S01 (per-developer database, sample data in version control), S20 (full-size thin clones to verify migrations), S21 (production-like data; seed data falls behind), S14 (timing from migration pipeline, Database Lab)
- agreement: contested
- positions: (a) production-shaped data: held by GitLab, Postgres.ai, Neon; serves confidence and realistic timing; wins for large tables and where plans or lock duration depend on volume; cost is cloning and personal-data risk. (b) developer-owned databases with versioned sample data: held by Fowler/Sadalage; serves isolation, speed and no exposure; wins for small data and early feedback. Vendor sources (S20, S21) are interested parties. Rehearsal inside a rolled-back transaction on shared real data (MAINT-C01) has no public source.
- certainty: grounded

**DATA-C27**
- claim: When production data is copied for tests, mask personal data before it leaves production, and block side-effects (mail, analytics) in the copy.
- level: practice
- stack: neutral (Postgres Anonymizer as example)
- sources: S21 (Risks of Direct Production Cloning, Masking)
- agreement: majority (single T3 vendor source)
- certainty: grounded (one source)
- boundary: TRANS

**DATA-C28**
- claim: Measure migration duration and lock behaviour on a rehearsal copy before production, and keep the measure with the change.
- level: practice
- stack: neutral
- sources: S14 (timing information), S20 (verify migrations and massive data operations), S15 (test-on-replica)
- agreement: majority
- certainty: grounded

**DATA-C29**
- claim: Keep urgent data fixes in a separate migration folder with its own tracking, apart from feature-driven schema migrations.
- level: practice
- stack: neutral
- sources: S01 (Separating Data Migrations)
- agreement: majority (one T2 source)
- certainty: grounded

**DATA-C30**
- claim: Keep data migrations apart from schema migrations in transaction and timing; schema steps stay fast, and data steps are batched.
- level: practice
- stack: neutral
- sources: S14 (Schema vs Data Migration Separation), S17
- agreement: majority
- certainty: grounded

**DATA-C31**
- claim: Involve the people who manage the production database before a risky change, and make pending changes visible across teams and environments.
- level: practice
- stack: neutral
- sources: S04 (Effective Communication)
- agreement: consensus
- certainty: grounded
- boundary: DELIVER (review)

**DATA-C32**
- claim: When a shared structure must change, support old and new access patterns during a transition period behind a stable compatibility layer, and put database access behind a clear layer in code.
- level: decision
- stack: neutral
- sources: S01 (Transition Phase: views and triggers; database access layer), S02
- agreement: contested
- positions: views or triggers as the compatibility surface and a code-side access layer (Fowler/Sadalage) serve ease and cost of ownership; a function with a signature as the stable interface (MAINT-C45) serves change absorption and has no public source; versioned interfaces apply to remote APIs (S02). Wins: views when consumers read shape; function or access layer when consumers are many and diverse.
- certainty: grounded for the Fowler position; maintainer position open
- boundary: ADOPT

**DATA-C33**
- claim: Decide which data changes apply automatically on merge and which are run by named people on request, and record the criterion (duration, locks, non-transactional, environment-specific).
- level: decision
- stack: neutral
- sources: S01 ("never applied manually": automation tools apply migrations), S04 (same pipeline), S14 (post-deployment migrations run at release manager discretion; regular migrations must stay ordinary)
- agreement: contested
- positions: automate fully through the pipeline serves delivery speed and consistency (DORA, CD consensus; wins with small, fast, compatible changes and high deploy frequency); gate long or locking changes behind a person serves reversibility and control (GitLab post-deployment; maintainer MAINT-C26, C27; wins at high criticality and large tables). Note: the public "never manual" rule bans hand-typed SQL, not a human-triggered automated run.
- certainty: grounded
- boundary: DELIVER

**DATA-C34**
- claim: Make application deploy depend on the schema state it needs (a declared required version checked before rollout).
- level: practice
- stack: neutral
- sources: S03 (schema first, check, then app) supports the order only
- agreement: majority (order is consensus; explicit version gate has no public source)
- certainty: inferred; explicit gate open

**DATA-C35**
- claim: Public counterpart not found for: configuration-like registry content deployed by an idempotent authoring script, with a migration as optional audit mirror (MAINT-C30).
- level: decision
- stack: neutral
- sources: S01 (data-fix folder is the nearest)
- agreement: contested (maintainer versus DORA same-pipeline)
- certainty: open

**DATA-C36**
- claim: Public counterpart not found for tagging long-running statements with the change ticket key in a comment so they show in activity views (MAINT-C42).
- level: practice
- stack: neutral
- sources: none
- agreement: n/a
- certainty: open

**DATA-C37**
- claim: Public counterpart not found for defining "done" of a bulk change as a convergence query returning zero remaining work, with a halt-on-first-failure first run and a ramp ladder (MAINT-C37, C38). Nearest: S16 shadow comparison, S15 controls, S13 idempotence.
- level: practice
- stack: neutral
- sources: S16, S15, S13
- agreement: n/a
- certainty: open (partly inferred from the nearest sources)

**DATA-C38**
- claim: Require an explicit opt-in assertion for operations whose scope can silently widen; nearest public form is a migration linter that blocks unsafe operations unless asserted.
- level: practice
- stack: Rails, Postgres tools
- sources: S17 (safety_assured), S18
- agreement: majority (only two T3 tools)
- certainty: inferred (the maintainer rule covers application-level bulk operations; the tools cover DDL)

**DATA-C39**
- claim: Validate the new data against the old before removing the old structure; continuous out-of-band validation jobs find corruption early, independent of application logic.
- level: practice
- stack: neutral
- sources: S09 (Out-of-Band Validation Pipelines), S16 (Scientist), S19 (test before cutting reads)
- agreement: majority
- certainty: grounded
- boundary: VERIFY

**DATA-C40**
- claim: Use soft deletion or a retention window as the first defense for destructive data changes, with restore as the last.
- level: practice
- stack: neutral
- sources: S09 (Soft Deletion, defense in depth)
- agreement: consensus
- certainty: grounded

**DATA-C41**
- claim: Defend data integrity in layers (multiple strategies that fall back to one another) because every single strategy eventually fails.
- level: principle
- stack: neutral
- sources: S09 (Defense in Depth)
- agreement: consensus
- certainty: grounded

**DATA-C42**
- claim: Track migration state in the target database itself so the pipeline can tell which instance is at which version; keep sample or reference data with the migrations so every environment is consistent.
- level: practice
- stack: neutral
- sources: S04, S01 (Test Data as Core Artifact)
- agreement: consensus
- certainty: grounded

**DATA-C43**
- claim: Before dropping a column or table, first stop the application from reading it (and any framework cache of it), then drop in a later deploy.
- level: practice
- stack: Rails (the generalization is neutral and follows C05, C06)
- sources: S17 (column removal)
- agreement: consensus
- certainty: grounded (tool-specific); generalization inferred

### Gaps

- No T1 or T2 source found on backfill procedure; the whole backfill cluster (C21 to C25) rests on T3 tool docs and company blogs plus one pipeline-scheduler doc.
- No T1 or T2 source found on data-migration testing beyond Fowler/Sadalage; production-shaped testing rests on vendor material (S20, S21) and GitLab.
- Humble and Farley's Continuous Delivery data chapter, and Kleppmann's compatibility chapter, could not be read as text; their positions on roll-forward versus rollback and on rolling-upgrade compatibility are not verified here.
- No public position found for: schema-version gate on deploy, ticket key inside statements, convergence query as done, registry content by script, function-with-signature as compatibility surface, named senior approvers by risk, no version numbers on shared interfaces.
- No source argues for a maintenance window as the preferred option; its place in the debates is inferred from the cost statements in S02 and S19.
- Stack-neutral wording of lock claims rests on Postgres and MySQL docs only; other engines not checked.
