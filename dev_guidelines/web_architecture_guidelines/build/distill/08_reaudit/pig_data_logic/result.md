# Re-audit under MD-08: PIG-WEB-DATA and PIG-WEB-LOGIC

Read-only re-audit of the final verdicts of the `pig-web-defaults` DATA and LOGIC branches
(`intent_graphs/web_defaults.ig.yaml`) under the corrected selection rule MD-08: "max" is the
best practice for the node's purpose, not the most demanding one. MD-01 to MD-08 are treated as
settled and not re-audited. No graph or other file was changed.

## L1 headline

- Nodes read: 67, every node of both branches, each through `ig-tool query --node`. That is 36 in
  PIG-WEB-DATA and 31 in PIG-WEB-LOGIC; 4 of them are deferred and hold no verdict
  (DATA.MAINTAIN.6, DATA.MAINTAIN.7, DATA.DERIVE.3, LOGIC.PROCESS.7).
- Flagged: 1. `PIG-WEB-LOGIC.SECURE.7`. The egress proxy was made required only because
  required is the strictest reading of the source's "preferably".
- Every other verdict stays: purpose, a maintainer decision or a settled placement decided it.
  - In four kept verdicts the record uses strictness wording ("stricter max", "more demanding",
    "stricter than", "the most demanding form"). Under MD-08 the outcome holds, and only the
    stated ground should be rewritten: DATA.GUARD.1 (foreign keys), DATA.GUARD.2 (narrow
    function-owner roles), LOGIC.SECURE.5 (MFA required) and LOGIC.PROCESS.5 (no file URL
    before a clean scan).
  - "Best" still supports all six verdicts that go against the maintainer's codified practice:
    - CHECK constraints required;
    - `updated_at` set by trigger;
    - 8-byte keys unless the table is bounded;
    - declared self-referencing parent keys;
    - no `updated_at` on append-only tables;
    - expand, migrate, contract for breaking function-API changes.

## L2 claims

- `PIG-WEB-LOGIC.SECURE.7`. Current verdict: every client-named fetch leaves through an egress
  proxy, which is required.
  - Why strictness decided it: the record says "P1's 'preferably' made required (max)". The
    ledger row L662 says only "preferably". The node's own rejected clause ("acceptable when the
    deployment has no egress proxy") cancels the requirement, so the strictest reading was the
    only ground.
  - Proposed best choice:
    - The fetch helper is required: connect-time address check, every redirect hop checked,
      timeout and size cap.
    - A network guard is preferred, as the source says. It is an egress proxy with direct
      egress blocked, or outbound rules that deny the private, loopback, link-local and metadata
      ranges. It applies wherever the hosting can enforce such rules.
    - It is required only when the server's network holds internal services, or a metadata
      endpoint that answers without a token.
  - Confidence: high that strictness decided the verdict; medium on the exact wording of the
    replacement.

## L3 full

### Flagged: PIG-WEB-LOGIC.SECURE.7 Server-Side Fetch

**Positions** (judge record `PIG-WEB.LOGIC.SECURE.7`; ledger row L662, consensus, sources SRC-363
and SRC-367): one position. Any server-side fetch of an agent- or client-supplied URL must block
private, loopback and link-local ranges, validate each redirect hop, and "preferably go through
an egress proxy".

**Evidence of the tie-break** (the record, word for word):
- Decision: "... and leaves through an egress proxy: P1's \"preferably\" made required (max)."
- State: "unvalidated: egress proxy required (max applied to \"preferably\")".
- Rejected: "Direct egress without a proxy: acceptable when the deployment has no egress proxy;
  the helper's checks are then the only guard (inferred)."
- Rendered guideline (`stack_defaults_logic_security.md`, Server-Side Fetch): "It leaves through
  an egress proxy, required (inferred: the strongest reading of the source's \"preferably\")".

No force in the record is served better by a required proxy than by a preferred one. The only
ground given is the "max" rule applied to the strength of a modal verb. The rejected clause also
makes the requirement circular: it is required, unless the deployment has no proxy.

**Why the rejected reading serves the purpose as well, at lower cost, in the default context:**
- The node's purpose is that a client cannot make the server reach internal services or metadata
  endpoints. The helper already stops the named attacks:
  - its address check at connect time defeats DNS rebinding and alternative IP notations
    (inferred, as the node already marks it);
  - its check on each redirect hop defeats redirect chains.
- An egress proxy adds a guarantee only when direct egress is blocked at the network level.
  Without that, code that bypasses the helper also bypasses the proxy. Its value therefore
  depends on what the hosting can enforce, not on the strictness of the rule (inferred).
- The default context is a classic website. MD-06 sends a prototype down the fastest secure
  path, and the hosting model is chosen per project. A required proxy adds one more component to
  run for every deployment, including those whose network reaches no internal service.

**Proposed node text, in the node's style:**

- intent: "Every server-side fetch of a client- or agent-named URL goes through one fetch helper.
  The helper refuses private, loopback and link-local addresses, checks the address actually
  connected to, and validates every redirect hop the same way, so a client cannot make the
  server reach internal services or metadata endpoints. Where the hosting can enforce outbound
  rules, a network guard backs the helper: an egress proxy with direct egress blocked, or rules
  that deny the application those ranges."
- constraints:
  - One fetch helper for every fetch of a client- or agent-named URL.
  - Refuse private, loopback and link-local ranges, checking the address actually connected to
    rather than the hostname.
  - Validate every redirect hop the same way.
  - Run with a timeout and a size cap, and in a worker when the response does not need the
    result.
  - Network guard, preferred: where the hosting can enforce outbound rules, fetches leave through
    an egress proxy with direct egress blocked, or outbound rules deny the application's
    processes the private, loopback, link-local and metadata ranges. It is required when the
    server's network holds internal services or a metadata endpoint that answers without a
    token. Where the hosting cannot enforce outbound rules, the helper is the guard.
  - Forbidden: fetching without range checks.
- epistemic_state: "known | unvalidated: connect-time address check inferred; the network guard's
  'required when' condition inferred"
- design_notes, decision line: "P1 adopted as stated: the helper is the required control, and the
  network guard is preferred (L662). A proxy adds a guarantee only when direct egress is blocked.
  It is required only where an internal service or an unprotected metadata endpoint is reachable
  (inferred). Rejected: a proxy required for every deployment, since the record's only ground
  was the strictest reading of 'preferably' (MD-08)."

**Propagation:**
- `stack_defaults_logic_security.md`, Server-Side Fetch section: the "required" line and the
  "Acceptable when" line become the preferred and required-when rule above.
- No change is needed in:
  - PIG-WEB-LOGIC.SECURE (its constraint says only that fetches "cannot reach private, loopback
    or link-local addresses");
  - the PIG-WEB-LOGIC root ("guarded server-side fetch");
  - web-app-philosophy LOGIC.SECURE (it lifted only the stack-neutral clause);
  - PIG-WEB-INTERACTION.AGENT.2 (it hands the fetch defence to SECURE.7 by name).
- PIG-WEB-TRANSVERSE.TOPOLOGY places no egress proxy today. Nothing changes there unless the
  maintainer wants the optional proxy placed; those nodes were not read for this audit.
- The J7 records and result keep the old wording as history, as MD-08 provides.

### Kept with the ground to rewrite (strictness wording, outcome holds under MD-08)

- `PIG-WEB-DATA.GUARD.1`, foreign keys: the record says "P2' (L492, MAINT, stricter, max)", and
  the review says "the stricter max". The outcome holds for two reasons:
  - under MD-03, a cascading delete fired by any consumer reaches rows that no reviewer of that
    consumer sees;
  - under MD-04's soft-delete default, CASCADE on a soft-deletable table would be a hard-delete
    leak.

  L492 is also the maintainer's own practice. Rewrite the ground to these two reasons.
- `PIG-WEB-DATA.GUARD.2`, one narrow non-login owner role per family of definer functions. Review
  M3 calls it "the more demanding practice". It is the least-privilege form the sources state
  (L184 "grant the narrow attributes needed", L514 "narrow roles for sensitive features"). It
  also keeps a fault in one family away from another family's tables: a cache function cannot
  delete business rows or forge history. Its cost is a few NOLOGIN roles defined in migrations.
  Rewrite the ground as least privilege.
- `PIG-WEB-LOGIC.SECURE.5`, MFA required on human accounts. This is cited from the philosophy
  verdict (J3 LOGIC.SECURE: "requiring it is the most demanding form"); the consensus row L346
  says "offer". The outcome holds for the node's purpose, login security:
  - MFA is the first layer of L033;
  - in the default context a human account delegates to agents, so a takeover also yields agent
    access;
  - delegated OpenID Connect login (SECURE.4) and passkeys make MFA cheap;
  - J3's condition for optional MFA (an audience that cannot practically be required) is kept.

  Rewrite the ground in J3's record and in this node. The origin is the philosophy graph, which
  is outside this scope.
- `PIG-WEB-LOGIC.PROCESS.5`, no download URL before a clean scan, the uploader included. The
  record says "stricter than P1's 'any other user'; one gate". The outcome holds for a security
  reason, not for strictness: a signed download URL is a bearer credential. An uploader's URL to
  an unscanned object could be passed on and would serve unscanned bytes from the storage
  origin. Rewrite the ground to that.

### Examined closely and kept (one line each)

The six verdicts against the maintainer's codified practice:
- `PIG-WEB-DATA.GUARD.1`, CHECK constraints required (against L471, inherited from the J1
  placement): best. Only declared constraints bind every writer of a shared database, owner-run
  jobs included, and row-local CHECKs are cheap.
- `PIG-WEB-DATA.GUARD.4`, `updated_at` set by a narrow trigger that stamps only on change
  (against L529): best. It is the only mechanism that holds for owner-run jobs and direct
  writers under the DB_API exception, cache staleness checks read the column, and stamping only
  on change meets L529's own reason (WAL traffic).
- `PIG-WEB-DATA.ORGANIZE.2`, 8-byte keys unless the table's size is bounded by design (against
  L503): best. The ground was already corrected after review: an overflow is repaired by
  rewriting the table and every referencing column at the table's largest, against 4 bytes per
  key paid gradually. It is not a strictness ground.
- `PIG-WEB-DATA.GUARD.1`, an unbounded hierarchy keeps a declared self-referencing parent key,
  with path, closure or nested set only as derived copies (against L493): best. The parent link
  is the fact, stored once and declared. The derived forms keep their read benefits under
  DERIVE.1. The acyclicity trigger is the price of declaring the fact, not an added strictness.
- `PIG-WEB-DATA.ORGANIZE.3`, no `updated_at` on append-only tables (against L498): best. It asks
  for less, not more, since the column would state nothing.
- `PIG-WEB-DATA.INTERFACE.1`, expand, migrate, contract for breaking function-API changes
  (against L517): best. Under MD-03, consumers deploy on their own schedules. L517's "deployed
  together" stays acceptable when every consumer ships with the migration, and its coordination
  and no-version rules are kept.

Other verdicts examined closely:
- `PIG-WEB-DATA.CONCURRENCY.1`, Serializable for every writing role plus versions on edited rows.
  L568 is contested, but its own condition for (a) ("low contention and framework retry") holds
  for a classic website whose writes go through writer functions behind one retry wrapper. The
  decision is purpose-driven.
- `PIG-WEB-DATA.CONCURRENCY.5`, the `xid8` horizon over gap detection ("a guarantee over a
  heuristic"). One column buys a guarantee for readers that must see every row, which is the
  node's purpose. It is not strictness.
- `PIG-WEB-DATA.CONCURRENCY.6`, new transitions enforced from their first release, with
  observe-only kept as a migration aid. This narrows L598 without being counted against the
  doctrine. It has the same shape as Postgres's NOT VALID: new writes are checked, and existing
  violating data is tolerated with a recorded exit. The decision is purpose-driven.
- `PIG-WEB-DATA.INTERFACE.2`, an external transaction-mode pooler. It comes from the consensus
  row L199, not a strictness tie-break. Whether a small deployment needs it is a fitness question
  for MD-06, outside this rule.
- `PIG-WEB-DATA.MAINTAIN.3`, trigger-written history for every business table. It realizes the
  J1 ACT.4 placement; tamper detection applies to high-value data only.
- `PIG-WEB-LOGIC.SECURE.3`, every CSRF layer. Each layer is a consensus row (L330 to L332), and
  the cost in Django is low (Django already checks `Origin`).
- `PIG-WEB-LOGIC.SECURE.4`, sender-constrained tokens "wherever supported". This is the
  consensus row L341, conditioned on support, not made absolute.
- `PIG-WEB-LOGIC.SECURE.6`, two limit layers and a load shedder. These are source positions, not
  a strictness tie-break. The load shedder rests on one T3 source (L363), which is a fitness
  question, not a strictness one.
- `PIG-WEB-LOGIC.PROCESS.2`, foreign mutations in a worker behind a 202. This follows the J1
  ACT.3 placement (no foreign effect inside the request), and in-request phases stay acceptable
  under a 1 s budget.
- `PIG-WEB-LOGIC.PROCESS.4`, direct-to-storage uploads by default. The record decides it on the
  availability of synchronous workers, with scanning applying on either path. It is not
  strictness.
- `PIG-WEB-LOGIC.PROCESS.5`, content disarm and reconstruction for document formats. This is the
  source row L428 as stated, not a judge tie-break.
- `PIG-WEB-LOGIC.EXPOSE.1`, keyset paging, HTML lists included. The rule comes from the
  philosophy placement ALLOCATION.DERIVE.2, outside this scope. If numbered pages are wanted for
  small HTML lists, the place to revisit is that placement.
- Settled, not audited: MAINTAIN.2 (MD-04), the read-visibility clauses (MD-05), SameSite in
  SECURE.2 and SECURE.3 (MD-07), and the row-security parts of GUARD.3 and ORGANIZE.6 (MD-01).

### Noticed, outside the audit rule

The design_notes of `PIG-WEB-DATA.MAINTAIN.2` label the deletion default "decided by MD-05
(question 1)". They also still carry the superseded archive recommendation and the "If
unanswered" text, and the PIG-WEB-DATA root notes say "default decided by MD-05, question 1".
MD-04 decided deletion. The intents and constraints already state MD-04 correctly, so only the
notes are stale.

### Method

- `ig-tool tree` listed the 67 uids. A loop ran `ig-tool query --node` once per uid into scratch
  files. Intent, state, constraints and design_notes were read for every node.
- The J6 and J7 records, the data review, the J3 MFA passage and the ledger rows cited above were
  read where a node's notes named a tie-break or a contested row. A search over all judge
  records for strictness markers ("demanding", "stricter", "made required", "max applied",
  "tie-break") found every marked passage; each is handled above.
