# Cross-branch fix resolutions (apply verbatim in every branch)

The four branch reviews (`review_data/`, `review_logic/`, `review_interaction/`,
`review_transverse/`) raised findings that cross branches. Each is resolved once here so the
fixers apply the same text. A branch fixer applies these first, then its own review.

## X1 Read-visibility clause (data B1, logic M1, interaction M1, transverse m7)

- One notation everywhere: epistemic clause `undecided: awaiting maintainer, read visibility of
  rows with per-user rules when several backends share the database`.
- Recorded default: each backend filters these reads from one shared written specification,
  with a shared denial-test suite every backend runs.
- Keep J1's stated fallback, do not forbid it: database read functions that receive the
  verified actor are acceptable when a per-user read rule must hold for two or more backends.
- State the consequence everywhere it matters: roles that may SELECT the base tables
  (reporting, operator) see every row, comments included, unless their own role is restricted.
  No statement may claim stronger visibility guarantees than this.

## X2 Departure from L517 ("coordinated and deployed together")

- Counted once, at its owner: the function-API node of the Postgres data tier (J6). Other units
  cite it, they do not count it.
- One condition, word for word: "deployed together" stays acceptable only when every consumer
  of the changed object ships in the same deployment as the migration; otherwise a breaking
  change goes expand, migrate, contract. L517's coordination with every consumer and "no
  formal version numbers, a new function name carries the change" are kept.

## X3 Cross-domain business operations (transverse B1, against ACT.1 and MD-03)

- One business operation is one database function call in its own transaction (J1 R1-4);
  backends never compose several calls into one operation.
- A database function may call another domain's published functions inside the same
  transaction: composition across domains happens in the database.
- What is forbidden across domains is direct access to another domain's tables, not calling its
  published functions.

## X4 Test boundary (transverse M2)

- Logic tests on shared data run in never-committing transactions (L567).
- Behaviour that only shows at commit (serialization retries, lock waits, deferred constraints,
  the outbox) is tested with committing sessions in a disposable database, never a shared one.
- Concurrency tests for the rules GUARD.2 requires (Serializable with retry, locks) are part of
  the default test suite, not a gap.

## X5 Backend deployables under MD-03 (transverse M3)

- Several backends may share the database (MD-03). Each backend is one deployable; it is not
  split into services without a measured need. "One backend deployable" is replaced by this.

## X6 Tokens in URLs (interaction M2)

- No session token, bearer token or long-lived credential ever travels in a URL.
- Short-lived, single-purpose, scope-limited signed URLs for file delivery are the one allowed
  exception, with their lifetime and scope stated.

## X7 MD-02 covers every agent-facing interface (interaction M3)

- "Always in sync by process" and the compatibility window apply to every interface
  description consumers read: the HTTP description, the database function API catalogue, and
  the agent tool surface (for example an MCP server's tool list and schemas).
