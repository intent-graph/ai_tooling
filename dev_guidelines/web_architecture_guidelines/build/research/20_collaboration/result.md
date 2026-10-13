# COLLAB: comments, annotation and collaboration on data (round 4)

## L1 headline

Best practice for comments and collaboration on data is settled at the base (comments are their own entity anchored to a record, field or version; conflicts are detected by an optimistic version check; presence is ephemeral; history is written atomically with the change; comment rights are separate from data rights) and genuinely contested at the top (silent last-writer-wins versus rejecting or merging, central-authority versus CRDT engines for text, SSE versus WebSocket, database-enforced versus backend-enforced comment visibility); certainty is grounded for the base and inferred for moderation, which could not be read from its legal source.

Pinned:
- Sources by tier: T1 13, T2 3, T3 8, T4 1 (25 total)
- Claims: 34
- Contested topics: last-writer-wins granularity; text engine (central-authority OT/steps vs CRDT); local-first vs server authority; SSE vs WebSocket; history by application vs trigger; comment visibility in database (RLS) vs backend; threading structure
- Failed T1 fetches: EU Digital Services Act (EUR-Lex, two URLs, empty page returned); two Kleppmann papers (T2, PDF unreadable, replaced by T3 summaries); RFC 9110 first fetch truncated, a second fetch returned the If-Match and ETag text

## L2 claims

Pinned:
- Sources by tier: T1 13, T2 3, T3 8, T4 1 (25 total)
- Claims: 34
- Contested topics: last-writer-wins granularity; text engine (central-authority OT/steps vs CRDT); local-first vs server authority; SSE vs WebSocket; history by application vs trigger; comment visibility in database (RLS) vs backend; threading structure
- Failed T1 fetches: EU Digital Services Act (EUR-Lex, two URLs, empty page returned); two Kleppmann papers (T2, PDF unreadable, replaced by T3 summaries); RFC 9110 first fetch truncated, a second fetch returned the If-Match and ETag text

Clusters (claim, agreement, certainty, ids):
1. A comment is its own entity pointing at a target (record, field, version, range), with its own lifecycle and rights; tombstone on delete, edit history kept. Consensus on the shape, grounded (W3C model) plus inferred (lifecycle). C01, C09, C10.
2. Anchor granularity follows the question "must the comment survive edits?": record or field by default, version-pinned for review or approval, redundant text selectors with an explicit orphaned state for ranges. Majority, grounded. C02 to C05.
3. Threads: parent pointer by default, depth capped, resolution state on the thread root, not on the comment. Majority; structure contested (parent pointer vs ltree vs closure). C06 to C08.
4. Conflict detection: optimistic version check (ETag with If-Match, 412 on mismatch, 428 to require it), enforced by a version predicate in the write. Consensus, grounded. C11, C16.
5. Conflict resolution: reject then rebase or merge by field is the default; silent last-writer-wins is acceptable only per property where conflicts are rare; pessimistic lease only where conflicts are frequent and lost work is costly. Contested, grounded. C12 to C15.
6. Collaborative text needs a text engine; discrete fields do not. Match engine to data shape; central-authority steps (or OT) when a server is anyway authoritative, CRDT when offline, multi-device or peer-to-peer matter. Contested, grounded. C17 to C21.
7. Presence is ephemeral and never written to Postgres tables; push is a hint over a cursor-based fetch that is correct on plain load. Majority, grounded plus inferred. C22, C25, C26.
8. Transport: SSE for server-to-client comment and notification streams, WebSocket only when low-latency bidirectional traffic is needed, Origin and per-channel authorization checked either way. Contested, grounded. C23, C24.
9. Notifications are persisted inbox rows created in the comment's transaction, delivered asynchronously. Inferred. C27.
10. History: append-only history row in the same transaction as the change, with actor and both dates; trigger-based where application bypass is unacceptable. Consensus on atomicity, contested on mechanism. C28 to C30.
11. Permissions: read, comment, resolve and moderate are separate abilities; a comment is never more visible than its target; deny by default, check per object per request. Consensus, grounded. C31, C32, C33.
12. Moderation: report, queue, action with reason and actor, hide rather than delete. Inferred; legal source unread. C34.

Live debates:
- Silent last-writer-wins (Figma, Linear, per property) versus reject-and-rebase (ProseMirror) versus lock (Fowler pessimistic).
- Central authority (ProseMirror, Figma, Linear, Google Docs OT) versus CRDT (Yjs, local-first essay, Gentle).
- Server as authority versus local-first primary copy.
- SSE versus WebSocket versus LISTEN/NOTIFY fan-out.
- Comment visibility enforced by row-level security versus backend only.
- Threading as parent pointer, ltree or closure table.

Not covered: DSA notice-and-action text (fetch failed), end-to-end encrypted collaboration, Linear and Notion primary sources (only a vendor summary read), @mention parsing and email digests (deferred round-2 topic), rate limiting and spam (round-2 abuse slot), a worked Postgres schema.

## L3 full

Pinned:
- Sources by tier: T1 13, T2 3, T3 8, T4 1 (25 total)
- Claims: 34
- Contested topics: last-writer-wins granularity; text engine (central-authority OT/steps vs CRDT); local-first vs server authority; SSE vs WebSocket; history by application vs trigger; comment visibility in database (RLS) vs backend; threading structure
- Failed T1 fetches: EU Digital Services Act (EUR-Lex, two URLs, empty page returned); two Kleppmann papers (T2, PDF unreadable, replaced by T3 summaries); RFC 9110 first fetch truncated, a second fetch returned the If-Match and ETag text

### Source register

| id | tier | title, body | URL read | authoritative on |
|---|---|---|---|---|
| COLLAB-S01 | T1 | Web Annotation Data Model, W3C Recommendation | https://www.w3.org/TR/annotation-model/ | body and target, selectors, states (time), motivations |
| COLLAB-S02 | T1 | RFC 9110 HTTP Semantics, sections 13.1.1 If-Match, 8.8.3 ETag | https://www.rfc-editor.org/rfc/rfc9110.html | conditional writes, strong comparison |
| COLLAB-S03 | T1 | RFC 6585 section 3, 428 Precondition Required | https://www.rfc-editor.org/rfc/rfc6585.html | requiring conditional requests against lost update |
| COLLAB-S04 | T1 | PostgreSQL, Explicit Locking | https://www.postgresql.org/docs/current/explicit-locking.html | row locks, advisory locks |
| COLLAB-S05 | T1 | PostgreSQL, NOTIFY | https://www.postgresql.org/docs/current/sql-notify.html | notification delivery semantics |
| COLLAB-S06 | T1 | PostgreSQL, Transaction Isolation | https://www.postgresql.org/docs/current/transaction-iso.html | concurrent update behavior, retry |
| COLLAB-S07 | T1 | PostgreSQL, Row Security Policies | https://www.postgresql.org/docs/current/ddl-rowsecurity.html | RLS semantics and caveats |
| COLLAB-S08 | T1 | PostgreSQL, ltree | https://www.postgresql.org/docs/current/ltree.html | path-enumeration trees and indexes |
| COLLAB-S09 | T1 | OWASP Authorization Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | deny by default, per-request object checks |
| COLLAB-S10 | T1 | RFC 6902 JSON Patch | https://www.rfc-editor.org/rfc/rfc6902 | atomic patch, test operation |
| COLLAB-S11 | T1 | RFC 6455 The WebSocket Protocol, section 10 | https://www.rfc-editor.org/rfc/rfc6455 | Origin check, handshake authentication |
| COLLAB-S12 | T1 | WHATWG HTML, Server-sent events | https://html.spec.whatwg.org/multipage/server-sent-events.html | Last-Event-ID resume, per-server connection limit |
| COLLAB-S13 | T1 | Activity Streams 2.0 Vocabulary, W3C Recommendation | https://www.w3.org/TR/activitystreams-vocabulary/ | inReplyTo, replies, Tombstone |
| COLLAB-S14 | T2 | Local-first software, Kleppmann et al., Ink and Switch | https://www.inkandswitch.com/essay/local-first/ | the local-first and CRDT position |
| COLLAB-S15 | T2 | Optimistic Offline Lock, Fowler, PoEAA | https://www.martinfowler.com/eaaCatalog/optimisticOfflineLock.html | version-check pattern |
| COLLAB-S16 | T2 | Pessimistic Offline Lock, Fowler, PoEAA | https://www.martinfowler.com/eaaCatalog/pessimisticOfflineLock.html | lock-first pattern and its cost |
| COLLAB-S17 | T3 | How Figma's multiplayer technology works, Figma engineering | https://www.figma.com/blog/how-figmas-multiplayer-technology-works/ | server-centric, per-property last-writer-wins |
| COLLAB-S18 | T3 | ProseMirror Guide, collaborative editing, maintainers | https://prosemirror.net/docs/guide/#collab | central authority, steps, rebase |
| COLLAB-S19 | T3 | Yjs docs, About Awareness | https://docs.yjs.dev/api/about-awareness | ephemeral presence |
| COLLAB-S20 | T3 | Understanding sync engines: Figma, Linear, Google Docs, Liveblocks (vendor) | https://www.liveblocks.io/blog/understanding-sync-engines-how-figma-linear-and-google-docs-work | comparison of three conflict models; Linear claims are second-hand |
| COLLAB-S21 | T3 | Fuzzy Anchoring, Hypothesis | https://web.hypothes.is/blog/fuzzy-anchoring/ | re-anchoring annotations after document change |
| COLLAB-S22 | T3 | django-simple-history docs | https://django-simple-history.readthedocs.io/en/latest/ | application-level history and its blind spots |
| COLLAB-S23 | T3 | I was wrong. CRDTs are the future, Joseph Gentle | https://josephg.com/blog/crdts-are-the-future/ | pro-CRDT argument and remaining obstacles |
| COLLAB-S24 | T4 | Search-result summaries on nested-comment storage (adjacency, ltree, closure table) | web search results only | the live debate on thread storage; never a sole ground |
| COLLAB-S25 | T3 | Commenting on a pull request, GitHub Docs | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request | resolve permission, outdated conversations; says nothing on hide or delete rules |

### Claims

Prior evidence is cited by ledger id (L475 version check across user time, L260 ETag rule, L476 fencing, L006 real-time as enhancement, L127 NOTIFY ceiling, L302 local-first, L049 security log versus audit trail, L208 to L212 history mechanisms, L566 request context in the database, L205 deletion per entity).

**C01** | Store each comment as its own entity with a mandatory target reference and its own author, lifecycle and permissions; do not embed comments as columns or JSON inside the annotated record.
- level principle; stack neutral; sources S01 sec 2 (targets mandatory, bodies separate); agreement consensus (single normative model, no dissent); certainty grounded for the model, inferred for the schema consequence.
- serves: independent lifecycle and permission boundary (comments may be edited, hidden or deleted without touching the data); wins when comments have different readers or writers than the record, which is nearly always.

**C02** | Anchor to the record by identity (foreign key) and optionally a field name by default; add a sub-field range only for long text values.
- level decision; stack postgres; sources S01 (selectors apply only to segments of text, media or DOM); agreement majority; positions: record-level (simplest, comment discusses the entity), field-level (review of one value), version-level (C03), range-level (C04); certainty inferred.
- serves: simplicity of query and permissions; wins as record-level when discussion is about the entity, field-level when review is per attribute.

**C03** | When a comment is about specific content (review, approval, legal), also store the version of the target it was written against, so it stays interpretable after edits.
- level decision; stack neutral; sources S01 sec 4.3.1 (TimeState: the time at which the source should be interpreted); agreement consensus (single source); certainty grounded.
- serves: correctness of meaning over time, auditability; costs a version or history table lookup; wins when edits can invalidate the comment ("this figure is wrong") and history exists (C28). Loses when comments are conversational and always about the current state.

**C04** | For comments on a text range, store redundant selectors (exact quote with prefix and suffix, plus character offsets, plus structural path), because offsets alone break under any edit.
- level practice; stack neutral; sources S01 sec 4.2.4, 4.2.5 (note: edits may change a position selection), S21 (stores three selector kinds and tries four re-anchoring strategies in order); agreement consensus; certainty grounded.
- serves: survival of anchors across edits; wins when the annotated text is editable or re-imported. If the text is immutable per version (C03), offsets alone suffice.

**C05** | Model anchor loss explicitly (anchored, moved, orphaned or outdated) and keep the comment visible in a separate place; never delete or silently reattach to a wrong place.
- level practice; stack neutral; sources S21 (orphans tab), S25 (conversations shown as unresolved, resolved, outdated); agreement majority; certainty grounded.
- serves: no silent loss of discussion; wins whenever targets change after commenting.

**C06** | Store threads as a parent pointer (adjacency list) with a cap on displayed depth; move to path enumeration (ltree) or a closure table only when whole-subtree reads dominate and writes are rare.
- level decision; stack postgres; sources S08 (ltree with GiST and B-tree indexes), S24 (T4 summary: adjacency simple but recursive reads; ltree efficient subtree reads but costly path update on move; closure table O(depth) rows per insert); agreement contested; positions: adjacency list (writes simple, recursive CTE for reads), ltree (read-optimized, move is costly), closure table (deep trees); GitHub and most review tools use one level of replies (S25); certainty inferred (T1 read for ltree only, comparison is T4).
- serves: write simplicity versus subtree read speed; wins as adjacency when threads are shallow and comments are rarely moved, which is the usual case for record comments.

**C07** | Denormalize a thread-root identifier on each reply so a thread loads in one indexed query and resolution state, counts and permissions attach to the root.
- level practice; stack postgres; sources S13 (inReplyTo and a replies collection per object); agreement majority; certainty inferred (S13 gives the relation, the denormalization is synthesis).
- serves: read latency and simple resolution; wins when threads are the unit of display; costs one more column to keep consistent (set once at insert, never updated).

**C08** | Keep resolution state (open, resolved, with who and when) on the thread root, separate from the comments; resolving is reversible and never a deletion; permit resolving by the target's author or users with write rights on the target.
- level decision; stack neutral; sources S25 (resolve if you opened the PR or have write access; resolved conversations collapse); agreement majority (single product read); certainty grounded for the rule, inferred for generality.
- serves: workflow clarity and accountability; wins in review and approval flows; for open discussion without an owner, any commenter may resolve.

**C09** | Delete a comment as a tombstone (content cleared, deleted_at and actor kept, replies preserved) unless a retention rule demands erasure.
- level practice; stack neutral; sources S13 (Tombstone with formerType and deleted time); ledger L205 (deletion chosen per entity from the reason data is kept); agreement consensus; certainty grounded. boundary: DATA lifecycle.
- serves: thread integrity and audit; wins when replies exist or moderation needs evidence; hard delete wins when privacy erasure overrides.

**C10** | Keep every edit of a comment as a revision (append-only), shown as "edited", so what was said and when stays reconstructable.
- level practice; stack postgres; sources none direct; ledger L208, L209, L212; agreement majority; certainty inferred from the audit claims.
- serves: accountability, moderation evidence; wins in business and regulated contexts; casual chat may keep only an edited flag.

**C11** | Detect concurrent edits of a record with an optimistic version: send the version read, reject the write with 412 when it is stale, and require the condition (428) on endpoints where a lost update would matter.
- level principle; stack http; sources S02 (If-Match, strong comparison), S03 (428 so clients work with correct copies), S15 (validate before commit within one system transaction; assumes conflicts are unlikely); ledger L475, L260; agreement consensus; certainty grounded.
- serves: correctness (no lost update) at near-zero concurrency cost; wins when conflicts are rare and an edit spans several requests (all form-based editing of records).

**C12** | Silent last-writer-wins is a data-loss risk at whole-record granularity; at per-property granularity it is acceptable when different users rarely edit the same property.
- level decision; stack neutral; sources S17 (per-property last-writer-wins, result is always a value sent by some client), S20 (Figma and Linear use it; "conflicts are actually quite rare"; fails for text at the same position); agreement contested; positions: (a) last-writer-wins per property, accepted by Figma and Linear for speed and simplicity, wins when overwrites are cheap to redo; (b) reject on stale version (C11), wins when an overwrite loses unseen work; (c) merge (C17); certainty grounded for what the vendors do, inferred for the rule.
- serves: simplicity and responsiveness versus integrity; wins as (a) for toggles, status, assignment, ordering, where the latest intent is the right one.

**C13** | Use a pessimistic checkout (a lease with owner and expiry stored in a row) only where conflicts are frequent and a rejected save wastes much work; otherwise do not.
- level decision; stack postgres; sources S16 (acquire a lock before using the data; cost: serialized access; use when optimistic causes frequent failures near completion); ledger L476 (fencing token checked by storage); agreement majority; certainty grounded.
- serves: user effort protected; costs concurrency and needs expiry and takeover; wins for long edits of a single shared document by few editors. Checkout is a courtesy signal unless the write path also checks the lease owner.

**C14** | Never hold a database transaction, row lock or session advisory lock across user think time; session-level advisory locks survive rollback and are application-managed.
- level principle; stack postgres; sources S04 (advisory locks "up to the application"; session-level locks do not honor transaction semantics; LIMIT hazard), ledger L475; agreement consensus; certainty grounded.
- serves: connection pool health and correctness; wins always; advisory locks fit short server-side mutual exclusion (transaction-level) only.

**C15** | On a stale write, return the current state and let the client rebase or merge: the server may merge automatically when the changed fields are disjoint, and a patch can carry a precondition so it applies all or nothing.
- level practice; stack http; sources S18 (rejected editor receives remote changes, rebases its steps, resubmits), S10 (PATCH atomic; test operation as a precondition); agreement majority; certainty grounded for the mechanisms, inferred for field-level server merge.
- serves: no lost work without a lock; wins when edits are partly disjoint (different fields of one record).

**C16** | In Postgres put the version predicate in the write itself (update where id and version match, then check the affected-row count), because a read-then-write in application code is not protected at the default Read Committed level; under Repeatable Read, retry the whole transaction on a serialization failure.
- level practice; stack postgres; sources S06 (Read Committed re-evaluates the WHERE on the updated row; Repeatable Read raises "could not serialize access" and the application must retry); ledger L475; agreement consensus; certainty grounded.
- serves: correctness at the point of write; wins always for conditional updates; boundary: allocation (concurrency control, database as authority).

**C17** | Real-time editing of long text needs a text engine; choose central-authority steps or OT when a server is authoritative anyway, a CRDT when offline use, multi-device sync or peer-to-peer matter.
- level decision; stack js; sources S18 (central authority tracks version, accepts steps only on matching version, others rebase), S17 (OT judged "unnecessarily complex", CRDT-inspired but server-centric), S23 (CRDT can do everything OT does, reverse not true; OT needs central ordering), S14, S20; agreement contested; positions: central authority (ProseMirror, Figma; simpler, easier permissions and history, wins when always online and the server enforces rules); CRDT (Yjs, local-first school; wins for offline, local-first, no single server, end-to-end encryption); OT (Google Docs, wins only where already invested); certainty grounded.
- serves: convergence of concurrent text edits; wins as central authority for a classic site with a server and permission checks.

**C18** | Match the conflict strategy to the data shape: discrete fields get version checks or per-property last-writer-wins; ordered sequences and long text get a sequence algorithm; the two are not interchangeable.
- level principle; stack neutral; sources S20 ("match your data model to the right conflict resolution strategy"), S17; agreement majority; certainty grounded (vendor source).
- serves: avoiding both overengineering and corrupt merges; wins always as a design question per field.

**C19** | For a record page, use optimistic versions for structured fields and give only genuinely collaborative long-text fields (description, notes, document body) a text engine.
- level decision; stack js; sources S20 (Linear: server-authoritative per-property last-writer-wins plus CRDT for descriptions); agreement majority; certainty inferred (second-hand report of Linear).
- serves: minimum machinery for maximum correctness; wins for line-of-business data with occasional rich text. Comments themselves are append-only rows and need no merge.

**C20** | Count the cost of a CRDT before choosing it: storage overhead of about 1.5x to 2x the content, no accepted algorithm for object move, and peers cannot be made to enforce server-side business rules or permissions on each operation.
- level practice; stack neutral; sources S23 (size overhead, no object move, theory complexity); the permissions point is inferred from S18 (server accepts or rejects steps) versus S14 (clients hold primary copy); agreement majority; certainty grounded for overhead and move, inferred for rules.
- serves: honest trade-off; wins as a veto when business rules must be enforced on every change.

**C21** | Choose a local-first primary copy (CRDT, background sync) when offline use, multi-device collaboration and user ownership of data matter more than central enforcement; otherwise keep the server authoritative.
- level decision; stack neutral; sources S14 (seven ideals; server copy as mere cache; speed-of-light latency; loss of ownership if the service ends), ledger L302; agreement contested; positions: local-first (Kleppmann et al.), server-authoritative (most line-of-business practice); certainty grounded. boundary: allocation.
- serves: latency, ownership, offline; costs central validation, simple permissions and simple audit; wins for personal and creative tools, loses for governed business data.

**C22** | Treat presence (who is online, cursors, "typing") as ephemeral: broadcast through a channel with a timeout (Yjs drops a peer after 30 seconds without update), never write it to Postgres tables.
- level principle; stack neutral; sources S19 (awareness is not persisted, timeout 30 s, periodic rebroadcast), S17 (presence outside the persistent protocol); agreement majority; certainty grounded.
- serves: write load and database health; wins always; a persisted "last seen" is a separate, coarse field.

**C23** | For server-to-client streams of new comments and notifications use Server-Sent Events with Last-Event-ID resume; use WebSocket only where low-latency bidirectional traffic (cursors, live typing) is required.
- level decision; stack http; sources S12 (Last-Event-ID, retry, HTTP/1 per-server connection limit per page), S11; ledger L006, L094; agreement contested; positions: SSE (plain HTTP, automatic reconnect and resume, wins for one-way push), WebSocket (full duplex, wins for presence and live editing), polling (wins for low frequency); certainty grounded for protocol behavior, inferred for the recommendation.
- serves: operational simplicity; wins as SSE for comment feeds.

**C24** | Authenticate every real-time connection and authorize each channel and each message against the target's read rights; on WebSocket verify the Origin header at the handshake.
- level practice; stack http; sources S11 sec 10.2 and 10.5, S09 (validate permissions on every request); agreement consensus; certainty grounded.
- serves: security (a stream is a data export path); wins always; boundary: allocation (authorization).

**C25** | Use LISTEN/NOTIFY only as a wake-up with an identifier payload, never as the data carrier or as a durable queue: it is transactional (sent at commit), limited to about 8000 bytes, not persisted for absent listeners, and the queue fails commits when full.
- level practice; stack postgres; sources S05; ledger L127 (commit-time global lock ceiling under write concurrency); agreement contested on scale (ledger L127); certainty grounded.
- serves: low latency without extra infrastructure; wins at modest write rates with one application tier; loses to a broker or application-layer fan-out at high write concurrency.

**C26** | Make push a hint over a correct pull: every page works on plain load, and a client catches up after any gap by fetching changes since a monotonic cursor (sequence id) rather than trusting delivered events.
- level principle; stack neutral; sources S12 (resume by last event id), S05 (no persistence), S20 (Linear: monotonically increasing sync ids), ledger L006; agreement majority; certainty grounded plus inferred.
- serves: correctness under dropped connections and multiple tabs; wins always.

**C27** | Create notifications as rows (recipient, reason, target, read state) in the same transaction as the comment, and deliver them asynchronously from those rows; parse mentions server-side and check each mentioned user's right to see the target before notifying.
- level decision; stack postgres; sources S05 (notifications are not persisted, so they cannot be the record), S09; agreement majority; certainty inferred (synthesis; no source describes the notification model directly). boundary: allocation (side effects).
- serves: no lost or phantom notifications, no leak of private content; wins always; the delivery channel (email, push) is a separate, deferred decision.

**C28** | Write an append-only history row in the same transaction as every change to collaborated data, with actor, change type, record date and actual date, and the changed values or a diff.
- level principle; stack postgres; sources ledger L208, L209, L210, L212 (trigger and statement commit or roll back together); agreement consensus; certainty grounded. boundary: allocation (audit).
- serves: accountability, "who changed what"; wins always for data that people dispute; a history of a mutable comment text is C10.

**C29** | Choose where history is written by what must not be bypassed: application-level history (a history table per model, user from the request) is convenient but bulk operations and raw SQL escape it; database triggers capture every writer at the cost of hidden behavior and the need to pass the actor in.
- level decision; stack postgres; sources S22 (bulk create, queryset update and raw SQL do not create history), ledger L208, L212, L216; agreement contested; positions: application library (Python ecosystem convenience, wins with one writer and an ORM-only code path), trigger (wins with several writers, SQL scripts, agents or batch jobs); certainty grounded for the limits, inferred for the rule.
- serves: completeness versus transparency; wins as trigger when more than one consumer writes to the database.

**C30** | Record who acted on every change and comment as a real principal; when a program acts for a user, store both the acting identity and the person it acts for, passing the actor into the database through a transaction-local setting.
- level practice; stack postgres; sources S22 (middleware sets history user), ledger L566 (transaction-local settings); agreement majority; certainty inferred. boundary: agents as users.
- serves: attribution and later moderation; wins always; shared service accounts defeat attribution.

**C31** | Treat read, comment, edit, resolve and moderate as separate abilities; the right to comment is neither implied by nor implies the right to edit the data, and a deny-by-default check runs per object on every request, including streams and exports.
- level principle; stack neutral; sources S09 (deny by default, least privilege, per-request per-object check, server-side only; prefer ABAC and ReBAC over plain roles; IDOR); S25 (resolve rule); agreement consensus; certainty grounded.
- serves: security and least privilege; wins always; a "comment" right is often granted to people who cannot edit (reviewers, customers).

**C32** | A comment is never more visible than its target, and a comment may be given a narrower audience (internal note versus shared reply); every secondary surface, namely counts, notifications, search results, history, ETags and real-time channels, must apply the same filter.
- level principle; stack neutral; sources S09, S07 (row policies, default deny); agreement consensus on the rule; certainty inferred for the list of leak surfaces (synthesis; S07 itself notes constraint checks bypass policies and can leak).
- serves: confidentiality; wins always; this is where comment systems typically leak.

**C33** | Enforce comment and target visibility where the data is shared by several consumers: in Postgres with row-level security (default deny, USING and WITH CHECK) when more than one application or agent reads the database; in the backend alone when one application tier is the only consumer.
- level decision; stack postgres; sources S07 (default deny; owners bypass unless forced; referential checks bypass policies; sub-selects in policies can race with concurrent privilege changes); S09; agreement contested; positions: database RLS (cannot be bypassed by a new client, cost: policy complexity and the sub-select race), backend only (simple, testable, wins with one tier); certainty grounded. boundary: allocation (authorization).
- serves: security under many consumers versus changeability; wins as RLS when agents or several services connect.

**C34** | Moderate through a queue: a report row, a status, an action (hide, restore, remove) with reason, actor and time written to history; hide first, delete only by a retention or legal rule; let authors edit their own comments within a stated window.
- level decision; stack neutral; sources S25 (reporting abuse path exists; resolution rights tied to write access), ledger L205, L209; agreement majority; certainty inferred. The legal obligations (notice-and-action and statement of reasons for hosting services) were not read: fetch of the regulation failed, so they are open.
- serves: accountability and appeal; wins for public or customer-facing comments; internal team comments may need only hide and author edit.

### Gaps

- Moderation law (DSA articles 16 and 17) unread: T1 fetch failed twice; treat C34 as inferred.
- Kleppmann's convergence and local-first PDFs were fetched but unreadable; the local-first essay (HTML) was read instead, and claims on LWW data loss rest on S17, S20 and S23.
- Linear's architecture is known only through a vendor article (S20), not a primary talk.
- No source read on comment schema in Postgres from a T1 or T2 authority beyond ltree docs; thread-storage trade-offs rest on T4.
- Undo of collaborative changes, comment search and e-mail digests: not researched.
- Notification delivery channels are deferred (round-2 scope out).
