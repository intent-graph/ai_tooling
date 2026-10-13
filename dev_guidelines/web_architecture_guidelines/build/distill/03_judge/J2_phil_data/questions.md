# J2 web-app-philosophy DATA: questions for the maintainer

None.

No node of the DATA branch faces a genuine trade-off between forces it serves. Every position the evidence offers either serves the branch's purpose, integrity of the stored data, or trades it for a force the branch does not own (read performance, speed of change). Those positions stay as "acceptable when <condition>" in `records.md`.

Not asked here, recorded in `records.md`:
- Read visibility of rows that carry per-user rules, when several backends share the database, is already before the maintainer as the allocation judge's question, and stays awaiting the maintainer. The principle on guarding data does not settle it. It records the allocation judge's stated default: for now, each backend filters such reads, from one written specification per rule, with a shared denial-test suite every backend runs; read functions in the database, which filter by the acting user, are acceptable when a per-user read rule must hold for two or more backends. Either way, database roles allowed to read the base tables directly, such as reporting and operator roles, see every row unless their own role is restricted.
- A breaking change to the database's function API, against the maintainer's practice of deploying it together with every consumer, is judged and counted once, by the judge of the Postgres data tier, who owns that practice. The philosophy level keeps only the principle: an incompatible change keeps every running consumer working.
- Structure gaps go to the skeleton owner, not to the maintainer. Under the shared-database default, no philosophy node realizes the database function API. Collation has no evidence.
