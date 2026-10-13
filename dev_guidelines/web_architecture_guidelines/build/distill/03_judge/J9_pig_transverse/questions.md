# J9 pig-web-defaults TRANSVERSE: questions for the maintainer

One question, awaiting maintainer. It is a check on the default context, not a trade-off: no node of this unit holds a genuine trade-off between forces it serves that the evidence or a maintainer decision leaves open. All 27 judged nodes are decided (`records.md`). The adversarial review of this branch found the question genuine and fairly framed, and kept it.

## Q1 Hosting model of the default context

**The ask**: should the default context assume self-managed hosts without a container orchestrator, or a platform that replicates containers for you?

**Recommendation**: assume one or a few self-managed hosts without an orchestrator, and record the other case as the condition that changes three defaults.

**If unanswered**: the verdicts stay as written. They assume self-managed hosts, and each names what wins when an orchestrator or a managed platform exists. For secrets, that means the file fallback described below is in force until the team adds a managed secret store.

**Situation**: the default context fixes the stack, the users and the shared database. It does not say where the system runs. Three stack defaults depend on that:
- **Process replication**:
  - without an orchestrator, each unit runs a process manager (Gunicorn's parent process with several workers), and background workers run as extra units on the same host;
  - with an orchestrator, each container runs one server process and the platform replicates it.
  - The sources split on exactly this line: the Uvicorn and FastAPI documentation, and Docker's one-concern rule.
- **Static files**:
  - without a platform, the reverse proxy on the application host serves them;
  - on a platform with no proxy of your own, the application serves them itself (WhiteNoise-style), always behind a CDN.
- **Secrets**:
  - the guideline makes a managed secret store the authority for every secret; a platform usually offers one;
  - self-managed hosts have none, so the store is a technology the team must add and justify like any other;
  - until it is added, the fallback is in force: a file outside source control, readable only by the service account, with rotation as a scheduled task.

**Options and costs**:
- **Self-managed hosts, no orchestrator (recommended)**:
  - fits a one-team classic website whose write load fits one Postgres primary;
  - adds no technology to operate;
  - costs manual scaling. The managed secret store holds only if the team adds one; otherwise the file fallback is the working default, with weaker revocation and no record of who read which secret.
- **Orchestrated containers or a managed platform**:
  - gives replication, rolling deploys and a secret store out of the box;
  - costs an orchestrator or a platform dependency to run and pay for, which the guideline's "few mature technologies" rule asks to justify by a measured need.

## Not a question from this unit

- **Read visibility of rows that carry per-user rules (for example, "a draft is visible only to its author"), with several backends sharing the database**: the open maintainer question stands and is not settled here. Two nodes record what holds if it stays unanswered, marked awaiting maintainer: the security requirement catalogue (access-control requirements) and testing (denial tests).
  - Each backend filters these reads from one shared written specification, with a shared denial-test suite that every backend runs.
  - Database read functions that receive the verified user stay acceptable when a per-user read rule must hold for two or more backends.
  - Consequence: roles that may read the base tables directly (reporting, operator) see every row, comments included, unless their own role is restricted. No requirement or test claims a stronger guarantee.
- **Decided, flagged for attention**: one narrowing of the maintainer's practice for the database function API is realized here, but counted once where the function API is judged. The practice says a breaking change is coordinated with every consuming team and deployed together, with no formal version numbers. The verdicts keep the coordination and the absence of version numbers. "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; otherwise the change goes expand, migrate, contract, the new function's name carrying the change. The never-committing boundary for tests in shared environments is adopted as is.
- **Decided after review, for information**: tests of behaviour that only shows at commit or between sessions (serialisation retries, lock waits, deferred constraints, the outbox) run with committing sessions in a disposable database, never a shared one; concurrency tests for the rules that need serializable isolation or locks are part of the default suite. HSTS preload is no longer the default end state: it becomes a recorded per-project decision, taken only when the team controls the whole registrable domain. Build provenance targets the hardened build level (SLSA Build L3), with the lower level acceptable when the build platform cannot isolate runs.
