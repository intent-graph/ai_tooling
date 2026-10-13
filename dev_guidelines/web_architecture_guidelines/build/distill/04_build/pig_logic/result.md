# PIG-WEB.LOGIC batch: result

## L1 headline

`batch.yaml` creates the 31 nodes of branch PIG-WEB.LOGIC (graph `pig-web-defaults`: 1 L1, 4 L2 roll-ups, 26 leaves, 1 deferred) and 0 links. Dry run and validate: pass with 0 errors on a scratch copy only with the uids aliased (root renamed `ROOT`, prefix `PIG-WEB.` dropped); with the real uids the tool refuses the first node, because its uid rule demands the child of `PIG-WEB.ROOT` to start with `PIG-WEB.ROOT.`. The real-uid batch is therefore unverified by the tool; see "Not transcribed".

## L2 nodes created (breadth-first; state in brief)

- PIG-WEB.LOGIC Python Application Tier: roll-up; known, two undecided clauses carried (read visibility, SameSite), framework unvalidated.
- PIG-WEB.LOGIC.SECURE Backend Security: roll-up; same two undecided clauses.
- PIG-WEB.LOGIC.ENFORCE Business Logic Realization: roll-up; framework unvalidated.
- PIG-WEB.LOGIC.PROCESS Processing and Side Effects: roll-up; known.
- PIG-WEB.LOGIC.EXPOSE HTTP Interface: roll-up; known.
- PIG-WEB.LOGIC.SECURE.1 Access Control Enforcement: central deny-by-default object-level policy; undecided read-visibility clause with recorded default.
- PIG-WEB.LOGIC.SECURE.2 Sessions: Postgres-held opaque sessions, `__Host-` cookie; SameSite undecided (default Lax plus navigation check).
- PIG-WEB.LOGIC.SECURE.3 CSRF Defense: every layer; known.
- PIG-WEB.LOGIC.SECURE.4 Federated Login and Tokens: OpenID Connect delegation, authentication context checked; known, delegation ranking unvalidated.
- PIG-WEB.LOGIC.SECURE.5 Passwords and Login Throttling: policy, Argon2id, MFA, no hard lockout; known.
- PIG-WEB.LOGIC.SECURE.6 Abuse and Rate Limits: two layers, 429 signalling; known, split is a synthesis.
- PIG-WEB.LOGIC.SECURE.7 Server-Side Fetch: one guarded fetch helper, egress proxy; known.
- PIG-WEB.LOGIC.ENFORCE.1 Use-Case Layer: one layer, ORM as read mappers; known with a tension.
- PIG-WEB.LOGIC.ENFORCE.2 Transactions: one call, one transaction, retries; known with a tension.
- PIG-WEB.LOGIC.ENFORCE.3 Data Access: wrappers for writes, one read layer; known with a tension, read-visibility clause.
- PIG-WEB.LOGIC.ENFORCE.4 Concurrency Model: synchronous by default; known.
- PIG-WEB.LOGIC.ENFORCE.5 Framework Choice: Django, criteria from settled verdicts; unvalidated with a gap (Pydantic and OpenAPI under Django).
- PIG-WEB.LOGIC.PROCESS.1 Background and Scheduled Jobs: queue rows claimed through writer functions; known, runner library open.
- PIG-WEB.LOGIC.PROCESS.2 Side Effects and Delivery: outbox, at-least-once, foreign mutations in a worker; known with a tension.
- PIG-WEB.LOGIC.PROCESS.3 Resilience: one retrying layer; known.
- PIG-WEB.LOGIC.PROCESS.4 File Upload Path: direct to object storage; known, unvalidated default.
- PIG-WEB.LOGIC.PROCESS.5 File Scanning and Storage: row with state and one writer function; known.
- PIG-WEB.LOGIC.PROCESS.6 File Serving: authorized redirect to a signed URL; known, read-visibility clause.
- PIG-WEB.LOGIC.PROCESS.7 Email and Push Delivery: deferred, scope out.
- PIG-WEB.LOGIC.EXPOSE.1 Contract Style and Resources: HTML plus resource-oriented JSON, keyset paging; known.
- PIG-WEB.LOGIC.EXPOSE.2 Status Codes and Errors: problem details, override-naming type; known.
- PIG-WEB.LOGIC.EXPOSE.3 Retries and Asynchronous Operations: natural idempotence, keys, 202 status resources; known with a tension.
- PIG-WEB.LOGIC.EXPOSE.4 Response Caching: every response labelled, caches in Postgres; known.
- PIG-WEB.LOGIC.EXPOSE.5 Origin and CORS: one origin, CORS off; known.
- PIG-WEB.LOGIC.EXPOSE.6 Payload Schemas: Pydantic at every entry, closed requests; known.
- PIG-WEB.LOGIC.EXPOSE.7 API Evolution: `/v1`, additive, CI gate; known, version location unvalidated.

## L3 notes

### Not transcribed or changed, and why

- **Dry run not passed with real uids.** `ig-tool apply` rejects `PIG-WEB.LOGIC` under `PIG-WEB.ROOT` ("Child node UID must start with parent prefix: expected `PIG-WEB.ROOT.<keyword-or-number>`"). The same rule rejects the sibling allocation batch. Checked instead on a scratch copy of the graph with the root renamed `ROOT` and every uid with `PIG-WEB.` dropped (same names, fields, parents, order): 31 operations succeeded, validate reported 0 errors, 0 warnings. Scratch files deleted. The coordinator must either relax the uid rule for a non-`ROOT` root or rename the root; the batch keeps the skeleton's uids unchanged as the brief requires.
- **Name of PIG-WEB.LOGIC.PROCESS.7.** The skeleton tree prints it as "Email and Push Delivery [deferred]"; the brackets are forbidden in names, so the name is "Email and Push Delivery" (as in the judge record) and the deferral is carried by `epistemic_state: deferred: ...` and the design notes. The skeleton's deferred table gives no reason beyond "scope out, recorded, not researched"; that is the stated reason.
- **Constraints and intents** are written for this batch from the judge's decisions (records give decisions, not a separate constraint list); `design_notes` carries the judge record's Positions, Forces, Decision, Rejected and Realizes text unchanged, with ledger and review ids kept.
- **Dropped line.** In ENFORCE.5 the one line citing the sibling Python guideline's scenario page by relative path was left out (a path into another folder; the record itself says it is not ledger evidence).
- **No `examples`**: the records give none. No `history` set.
- **impl_pointers**: the judge record pointer for every node; for each non-roll-up node, one pointer per original research claim behind the node's owned rows (skeleton ranges) and every ledger row its record cites (`merges` column of `claims_ledger.md`). The five roll-ups, which own no row, carry only the record pointer; their cited rows are carried by their children.
- **Result file of the judge** was checked for later revisions: its review-fix table (M1 to M7, m1 to m12, X1 to X7) is already applied in `records.md`; nothing further to transcribe.

### Links

0 `link.create` in the batch; 18 skeleton links and 5 judge-proposed links touching this branch are listed in `links_out.md`.
