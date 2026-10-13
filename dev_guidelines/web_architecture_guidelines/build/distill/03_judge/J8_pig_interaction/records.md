# J8 pig-web-defaults PIG-WEB.INTERACTION: judge records

One judge record per node of `PIG-WEB.INTERACTION` in `pig-web-defaults` (28 nodes, of which 2 are deferred and recorded only), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves the user's ability, human or agent, to work with the data; weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. The maintainer's decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points and are cited by id. The J1 placements (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled: these nodes realize them and never re-decide allocation. The J4 verdicts (`../J4_phil_interaction/records.md`) are the principles these nodes realize for JavaScript + Python + Postgres; no verdict here contradicts them.

Default context (J1, restated by MD-03): a classic website (documents, forms, CRUD), one team, JavaScript + Python + Postgres, single tenant, humans and agents as users; the database is shared by several backends and by BI, admin consoles and scripts; browsers and agents never connect to the database; Python renders HTML (PRESENT.1, JS_SERVER); Postgres carries the backing roles until a measured limit (POSTGRES_FIRST).

Pinned:
- Nodes: 28; judged 26 (6 roll-ups, 20 with owned rows; 88 owned rows read in full); 2 deferred, recorded and not judged (ENVIRONMENT.2 offline and installable apps, ENVIRONMENT.3 internationalization).
- Decided: 26; undecided nodes: 0. Inherited clause, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (from ALLOCATION.GUARD.3), reaching REALTIME.4 (per-subscriber filtering of pushed events) and COLLABORATE.4 (which mentioned users may be notified). Recorded default: each backend filters these reads from one shared written specification, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Consequence: roles that may SELECT the base tables (reporting, operator) see every row, comments and change rows included, unless their own role is restricted; until the question is answered they get no SELECT on comment content or narrower-audience comments.
- Questions: 0 (questions.md: none). Four contested rows were decided by composing positions along conditions the default context fixes: push channel (L436), token binding (L641), agent protocol surface (L635), approval design (L646). The automated-traffic row (L652) is carried into AGENT.5 with its winning condition: on flows that hand out scarce goods or reward automation per account, a human completes the flow or agents are excluded.
- Verdicts against the maintainer doctrine: 0 (the unit owns no MAINT row; the MAINT rows it cites, L566, L523 and L525, are followed; the tension between erasure and L525's archive copy is recorded and handed to the deferred personal-data node).
- Conflicts with J1 placements: 0. Two owned rows are narrowed to fit settled placements, not overridden against them: L437's "Redis when more than one process fans out" yields to POSTGRES_FIRST (Postgres wake-up plus table re-read first; Redis at a measured limit or where the framework requires it); L583's "wrap multi-step writes in atomic" yields to MD-03 and DB_API (one database API call per transaction; the backend transaction wraps that call only).
- Review fixes: 11 findings of the INTERACTION review reach this unit (M1, M2, M3, M4, m2, m3, m4, m5, m6, m7, m8), all applied, none rejected; cross-branch resolutions X1, X3, X4, X5, X6, X7 applied.
- Gaps in the evidence: 7. (1) No ledger row names AA: AA is grounded through the W3C page Understanding WCAG 2.2, Conformance (AAA not recommended site-wide; the level is a policy decision) plus the max rule (AA contains A and is the most demanding level every full page can meet); one legal floor at AA was read (US Department of Justice ADA Title II web rule, 2024: WCAG 2.1 AA); both sources are not yet in the register; other jurisdictions not read. (2) The push-channel debate rests on a T3 guide and a T4 vendor (L436, L437 inferred); the SSE buffering claim has one vendor source. (3) The comment model rests mostly on single or inferred sources (L665, L669, L670, L683; L673 has no source); the legal moderation obligations were not read (L689). (4) Agent identity and registration rest on moving specifications and drafts (L641, L653, L654, L661); agent-readable content (L636) rests on T4 and secondhand evidence. (5) A separate process type for long-lived connections (L458) and reconnect jitter (L454) are inferred. (6) No owned row chooses the enhancement library or the islands component library: left open, not invented. (7) The rate-limit partition (L651) is inferred; its combination here is a synthesis.

## How to read

- **Decides**: the node's question, from the skeleton's node table.
- **Rows**: owned rows (all read in full); rows owned elsewhere that the record cites are named in the text.
- **Positions**: P1.. competing practices from the evidence, with ledger ids; a position present only as what a row rejects is marked "(rejected in Lnnn)".
- **Forces**: what each position serves, at what cost.
- **Decision**: the max choice and its grounds; inferred parts are marked.
- **Rejected**: each other position, why, and the condition under which it wins.
- **Realizes**: the placements (J1) and philosophy verdicts (J4) the node carries out; links the skeleton does not draw are marked "(proposed)".
- **Hand-offs**: points other pig-web judges (DATA, LOGIC, TRANSVERSE) realize.
- **State**: proposed `epistemic_state`: `known` = grounded verdict; `| unvalidated: X` = an inferred part X; `| open: X` = a named part not decided here; `| gap: X` = missing evidence; `speculative` = thin evidence for the whole verdict.

## PIG-WEB.INTERACTION Browser and Agent Surface

- **Decides**: how browser JavaScript and the agent surface realize the interaction share of each placement.
- **Rows**: none (roll-up).
- **Decision**: roll-up of five children. Browsers get server-rendered HTML from Python, enhanced with JavaScript only where a part is interactive; agents get an OAuth-protected adapter over the same HTTP core. Neither decides anything durable: each holds copies (the version it read, drafts, a server-state cache, its own credential) and every decision reaches a backend and the database's writer functions.
  - **Visualize**: per-request HTML from Python, build-time output where the URL set is known, islands only under the rendering placement's criteria; view state in the URL; LCP content in the first HTML; WCAG 2.2 AA (VISUALIZE).
  - **Edit**: POST, then 303; the version travels with every edit and a stale write is shown as a conflict with both versions; layered duplicate suppression (EDIT).
  - **Real time**: polling, then server-sent events, then WebSocket for two-way traffic; events are hints keyed by a commit-safe cursor; Postgres wakes the connection processes, tables carry the data (REALTIME).
  - **Collaborate**: comments anchored by foreign key and target version, threads by parent pointer, tombstones and revisions, notifications as rows written with the comment, moderation as a recorded queue; a text engine only for long collaborative text, server-authoritative (COLLABORATE).
  - **Agent**: OpenAPI-described core, an MCP adapter for third-party agent hosts whose tool list and schemas are kept in sync like the description, protected-resource metadata, delegated identity recording user and agent, approval for irreversible effects held on the server, agent-shaped errors and per-agent quotas (AGENT).
  - **Environment**: feature detection, back/forward-cache eligibility, input saved on page hide (ENVIRONMENT).
- **Realizes**: refines INTERACTION (J4); through its children ALLOCATION.PRESENT.1 to .3, GUARD.3 to GUARD.6, ACT.2, ACT.4, RULES.4, PIG-WEB.ALLOCATION.JS_SERVER and POSTGRES_FIRST.
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from ALLOCATION.GUARD.3, through REALTIME.4 and COLLABORATE.4)`.

## PIG-WEB.INTERACTION.VISUALIZE Browser Rendering

- **Decides**: how pages are rendered, hold client state, perform and stay accessible in the browser.
- **Rows**: none (roll-up).
- **Decision**: roll-up of .1 to .4: Python renders HTML per request and ships JavaScript only for interactive parts (.1); client state by kind, navigable state in the URL, a server-state cache only inside client-rendered islands (.2); the LCP element in the first HTML, small DOM, short tasks, reserved space (.3); WCAG 2.2 AA on every full page, native HTML before ARIA (.4).
- **Realizes**: refines INTERACTION.VISUALIZE (J4); ALLOCATION.PRESENT.1, PRESENT.3, PIG-WEB.ALLOCATION.JS_SERVER through its children.
- **State**: `known | gap: accessibility mandates of jurisdictions other than the one read (.4)`.

## PIG-WEB.INTERACTION.VISUALIZE.1 Rendering Technique

- **Decides**: which rendering technique each kind of page uses and what JavaScript it ships.
- **Rows**: L282, L283, L284, L285, L286, L289, L290. Cited: L252, L253, L629, L016, L288 (J1 placements).
- **Positions**:
  - P1 server or static rendering, no full rehydration (L282, majority; SRC-181 T1/T2 against hydration's cost, SRC-321 a critique).
  - P2 full client rendering or full rehydration of a server-rendered page (accepted by SRC-292 as the normal mechanism; rejected in L282 for its interaction cost).
  - P3 JavaScript only for interactive parts, static regions plain HTML (L283).
  - P4 islands when widgets are independent; a single client-state owner or the URL when many widgets share live state (L284).
  - P5 build-time rendering when the URL set is known, per-request otherwise (L285).
  - P6 server or pre-rendering for crawled, fast pages; real 404 or `noindex` for client-rendered error pages (L286).
  - P7 an explicit server/client code boundary with secrets on the server side (L289).
  - P8 if a client-rendered React application is chosen, a framework with routing, data loading and server rendering rather than an assembled one (L290).
- **Forces**: P1, P3, P5, P6 serve fast first content, low interaction latency and crawlability (L016, L297), at the cost of building the HTML path first; P2 serves one client code path and rich interaction, at the cost of pages that look ready before they respond (TBT, INP) and a JavaScript server tier (L288). P4 serves islands' isolation and, for shared live state, consistency. P7 serves secret containment. P8 serves the team against an ad-hoc framework and request waterfalls, at the cost of the framework's server runtime.
- **Decision** (realizes PRESENT.1 and JS_SERVER as settled):
  1. **Per-request HTML from Python** for every page whose content depends on the request; **build-time output** for pages whose URL set is known ahead (documentation, marketing, help) (P5, L285). No request-time JavaScript server (JS_SERVER).
  2. **Partial updates as server-rendered HTML fragments** (the hypermedia contract of PRESENT.1, L629): enhancement swaps HTML the server rendered; it never renders large HTML with client JavaScript (L298) and never fully rehydrates a server page (P1, L282).
  3. **JavaScript only where a part is interactive** (P3, L283), added by feature detection (ENVIRONMENT.1), with the page's navigation and core forms working without it (J4 ENVIRONMENT.1).
  4. **Client-rendered islands only under the rendering placement's criteria** (L253: many interdependent controls, very high update frequency, real-time collaboration). Independent widgets are independent islands; widgets that share live state get one client-state owner for the region or share it through the URL, never state synchronized between islands (P4, L284).
  5. **Crawled pages are server- or build-time-rendered** (P6, L286), which the default already gives; an island never renders the page's main content or its error state.
  6. **Secrets never reach the browser bundle**: no credential, key or private setting is compiled into JavaScript or exposed through build-time variables meant for the client; where a framework marks a server/client boundary, it is explicit (P7, L289; the bundle rule is inferred for the default, which has no shared-code boundary).
- **Rejected**:
  - P2 as the default: wins only when PRESENT.1's condition holds for most of the product (L253, L254), and then with P8: a framework that provides routing, data loading and server rendering (L290), which also triggers JS_SERVER's condition when first load or crawlability needs server rendering (L288, L290).
  - Islands sharing live state among themselves: wins never (L284).
  - Client-rendered error pages without a real 404 or `noindex`: wins never for crawled pages (L286).
- **Open (not invented)**: no owned row chooses the library that swaps server fragments or the component library for islands; the choice is recorded per project with the criteria above (small script budget, L016; native semantics, VISUALIZE.4).
- **Realizes**: PIG-WEB.ALLOCATION.JS_SERVER (skeleton link); ALLOCATION.PRESENT.1 (proposed link: HTML from the backend, islands under L253); J4 INTERACTION.ENVIRONMENT.1.
- **Hand-offs**: page experience targets (PIG-WEB.TRANSVERSE.PERFORMANCE); fingerprinted asset delivery (PIG-WEB.TRANSVERSE.TOPOLOGY.4); generated island types (PIG-WEB.ALLOCATION.TYPE_CHAIN, settled).
- **State**: `known | unvalidated: the no-secrets-in-bundle extension of L289 | open: fragment-swap and island libraries (no row compares them)`.

## PIG-WEB.INTERACTION.VISUALIZE.2 Client State

- **Decides**: where server data and navigable view state are held in the browser.
- **Rows**: L291, L292. Cited: L070, L071, L631, L681 (PRESENT.3), L284, L294, L260.
- **Positions**: P1 server state in a dedicated server-state cache with deduplication, background refresh and staleness (L291, majority, one vendor source); P2 server state in a general-purpose client state store (rejected in L291); P3 server-rendered pages rely on the browser's HTTP cache for server state (L291's note); P4 navigable, bookmarkable or shareable view state in the URL via the History API, fragments not used to load content (L292, consensus); P5 navigable state in client memory only (rejected in L292).
- **Forces**: P1 and P3 treat server data as a stale-able copy (L071), at the cost of a cache layer in islands; P2 makes the client look like an owner of data it only copies, and drifts. P4 serves back, reload, sharing and agents that follow links, at the cost of URL design; P5 serves only simpler client code.
- **Decision**: state is held by kind, as PRESENT.3 places it:
  - **Server data on server-rendered pages**: the HTML is the copy; freshness by validators and the HTTP cache rules of the response caching node (P3).
  - **Server data inside a client-rendered island**: a dedicated server-state cache (deduplication, background refresh, explicit staleness), never a general-purpose store (P1, L291). Each cached record keeps the version it was read at, so a write from the island carries it (GUARD.5, L260).
  - **Navigable view state** (filters, sort, page, selected tab, open record): in the URL, through the History API; fragments only for in-page anchors (P4, L292).
  - **Form state**: in the browser until submitted; unsaved input persisted on page hide (ENVIRONMENT.1, L294) in per-tab or per-origin browser storage and cleared after a successful submit or at logout (storage choice and clearing inferred). On pages that show sensitive data (the `no-store` pages of ENVIRONMENT.1), drafts go to per-tab storage only or are not persisted, and are cleared at logout, so they do not outlive the session on a shared device (inferred).
  - **Presence**: on the real-time channel with a timeout, never in tables (PRESENT.3, L681).
  - **Never in browser storage**: credentials or session tokens (GUARD.4), or any state that must survive as data (RECORD.1).
- **Rejected**: P2: wins never for server data. P5: acceptable for ephemeral view state nobody navigates to or shares (PRESENT.3).
- **Realizes**: ALLOCATION.PRESENT.3 (skeleton link); ALLOCATION.GUARD.5 (the island keeps the version it read) and GUARD.4 (no credentials in script-readable storage) (proposed links).
- **Hand-offs**: response cache headers (PIG-WEB.LOGIC.EXPOSE.4).
- **State**: `known | unvalidated: P1 rests on one vendor T3 source (L291); draft storage, its clearing and the per-tab rule for sensitive pages inferred`.

## PIG-WEB.INTERACTION.VISUALIZE.3 Page Performance

- **Decides**: which page techniques keep loading, interaction and layout fast and stable.
- **Rows**: L297, L298, L299. Cited: L013, L016, L282.
- **Positions**: P1 the page techniques of the three rows: LCP resource discoverable in the initial HTML, never lazy-loaded, LCP element not client-rendered (L297); small DOM, long handlers split into tasks, no large HTML rendered by client JavaScript (L298); space reserved for late content (L299); all consensus, T1 and T2. P2 client-rendered main content with lazy loading everywhere (the practice L297 and L298 rule out).
- **Forces**: P1 serves the user's time to see and act on the data (L013's perceived limits), at the cost of discipline in templates and handlers; P2 serves only uniform client code.
- **Decision**: P1 entirely, as a release rule for every page template:
  - the LCP element is in the server HTML, its resource referenced there (preloaded when not discoverable early), never lazy-loaded and never rendered by an island (L297);
  - the DOM stays small; event handlers yield and split long work into separate tasks; no large HTML rendered in the browser (L298, consistent with VISUALIZE.1);
  - images, embeds and late content have reserved dimensions (L299).
  Measurement and thresholds are the performance node's: field measurement against the Web Vitals targets (L013 note: LCP 2.5 s, INP 200 ms, CLS 0.1).
- **Rejected**: P2: wins never for the main content; lazy loading is kept for below-the-fold media only (inferred from L297).
- **Realizes**: J4 INTERACTION.VISUALIZE; ALLOCATION.FORCES.4 latency (proposed link).
- **Hand-offs**: targets and field measurement (PIG-WEB.TRANSVERSE.PERFORMANCE, PIG-WEB.TRANSVERSE.OPERABILITY.2).
- **State**: `known`.

## PIG-WEB.INTERACTION.VISUALIZE.4 Accessibility

- **Decides**: which accessibility level is required and how controls meet it.
- **Rows**: L300, L301. Cited: L005 (J4), L003. Read during judging and confirmed at review (not yet in the source register, both to register): W3C, Understanding WCAG 2.2, Conformance (T1): "It is not recommended that Level AAA conformance be required as a general policy for entire sites because it is not possible to satisfy all Level AAA success criteria for some content"; the same page calls the choice of level "fundamentally a policy decision" and names no default. US Department of Justice, ADA Title II web accessibility rule (2024, T1): adopts WCAG 2.1 Level AA as the technical standard for state and local governments, a legal floor at AA in one jurisdiction.
- **Positions**: P1 WCAG 2.2 level A; P2 level AA; P3 level AAA for the whole site (L300 lists the three; "AA as the usual default is not stated"). Controls: P4 native HTML elements and attributes before ARIA, native semantics unchanged, every control keyboard-operable (L301, consensus T1); P5 custom controls rebuilt with ARIA (the practice L301 ranks second).
- **Forces**: the node's purpose is that everyone, people with disabilities included, can perceive and operate the interface. P3 serves it most on paper, but W3C states that all AAA criteria cannot be met by some content, so a site-wide AAA requirement cannot be met or verified as stated. P2 is the most demanding level that can be required of every full page. Moving from P1 to P2 needs no outside knowledge: AA contains every A criterion, so under the max rule AA dominates A wherever AA can be met, and the W3C page rules out only AAA as a site-wide requirement. P1 serves only a lower effort. P4 serves robustness across assistive technologies at no extra cost in server-rendered HTML; P5 costs testing effort and fails silently.
- **Decision**:
  - **WCAG 2.2 level AA is the conformance target of every full page**, embedded third-party content included (L300's page rule): a widget or embed that cannot meet AA is replaced or given an AA alternative on the same page. Grounds: the W3C conformance page plus the max rule (above); one legal floor at AA in one jurisdiction (US Department of Justice, ADA Title II rule, 2024, WCAG 2.1 AA) agrees.
  - **AAA criteria are adopted where the content allows** (for example enhanced contrast in the design system), and recorded per project; never stated as a site-wide requirement (W3C note above).
  - **Native HTML first** (P4, L301): elements and attributes before ARIA, native semantics unchanged, every interactive control keyboard-operable with visible focus. Server-rendered HTML (VISUALIZE.1) gives this by default; islands meet the same rules.
  - Checked from the first design (J4 VISUALIZE, L005): automated checks in delivery plus keyboard and screen-reader passes on each new template (test method inferred).
- **Rejected**: P1: wins never as the target (below the most demanding level every page can meet). P3 site-wide: wins never (W3C note); per criterion where content allows, as above. P5: acceptable only where no native element expresses the control (L301).
- **Realizes**: J4 INTERACTION.VISUALIZE (the conformance level it handed to this node); ALLOCATION.PRESENT.1 (proposed link: native semantics come from server-rendered HTML).
- **Hand-offs**: accessibility checks in testing (PIG-WEB.TRANSVERSE.OPERABILITY.5).
- **State**: `known (AA grounded through the W3C conformance page plus the max rule) | unvalidated: test method inferred; the W3C page and the US rule are not yet in the source register | gap: accessibility mandates of other jurisdictions not read`.

## PIG-WEB.INTERACTION.EDIT Editing Without Loss

- **Decides**: how forms submit, and how concurrent and repeated edits are detected and shown.
- **Rows**: L258, L260, L583, L675. Cited: L475, L582, L674, L676 (DATA), L259, L269, L546, L655 (LOGIC), L292, L294, L600.
- **Positions**:
  - Submission: P1 POST, then 303 See Other to a GET page (L258, consensus T1).
  - Lost updates: P2 optimistic concurrency: the version travels with the edit; ETag and `If-Match`; 412 on mismatch; 428 where a lost update matters (L260, consensus on mechanism, strictness varies by source); P3 the conflict shown with both versions (L583, conflict UI inferred); P4 the server returns current state and merges automatically when changed fields are disjoint; a patch carries a precondition and applies all or nothing (L675, majority; field-level merge inferred).
  - Transactions (L583's Django part): P5 wrap multi-step writes in `atomic`, `durable=True` for the outermost transaction, `on_commit` callbacks discarded after a rolled-back savepoint.
- **Forces**: P1 serves no resubmission on reload, Back or bookmark. P2 and P3 serve no silent loss of anyone's work, at the cost of a conflict screen. P4 serves fewer conflict screens, at the cost of applying a combination of fields no user saw, which per-row invariants catch only if declared. P5 serves atomic backend writes; under MD-03 the multi-table write is one database function call.
- **Decision** (realizes GUARD.5 and GUARD.6 as settled):
  1. **Every state-changing form POSTs; success answers 303** to the confirmation or the new resource (P1, L258); a failed validation re-renders the form with the user's input kept (inferred; status codes are the HTTP interface's). Search and filter forms submit with GET, so their state lands in the URL (VISUALIZE.2, L292).
  2. **The version travels with every edit** of a user-edited record: a hidden field in HTML forms (a plain form cannot send `If-Match`, inferred), `If-Match` with the ETag from JavaScript and agent clients. The backend passes it to the writer function as the expected version (P2, L260). The maximum strictness among the sources is adopted: the condition is required, not optional, except for per-property last-writer-wins updates (toggles, status, assignment, ordering), which are sent without the record version (GUARD.5, L674) and are exempt.
     - **`If-Match` clients**: a mismatch answers 412, a missing condition answers 428 on every endpoint editing such a record, per-property updates excepted (RFC 9110 defines both for conditional header fields).
     - **HTML forms**: a version in a hidden field that no longer matches is a conflict with current state, answered 409 with the conflict form of decision 3 (the mapping of PIG-WEB.LOGIC.EXPOSE.2: 409 for a conflict with current state); a form missing its version field is rejected as malformed and re-rendered with current values (inferred).
  3. **A stale write is shown, never merged silently**: the response re-renders the form with the user's input kept and the current values beside it, the fields changed by the other writer marked, and the new version embedded; the user reapplies (P3, L583).
  4. **A patch applies all or nothing** under its precondition (L675).
  5. **Duplicate submission, browser share** (GUARD.6, L582): the submit control is disabled with a pending state; create forms carry a form token minted at render, sent as the idempotency key the writer function records with the effect; 303 after success.
  6. **Unsaved input survives the page**: saved on page hide (ENVIRONMENT.1, L294), restored on return, cleared after a successful submit. On pages that show sensitive data, drafts go to per-tab storage only or are not persisted, and are cleared at logout (VISUALIZE.2; inferred).
  7. **Transactions** (P5 under MD-03): one business operation is one database function call in its own transaction; the backend opens one transaction per database API call (`atomic(durable=True)` in Django asserts that it is outermost) and never composes several calls into one operation (J1 R1-4, DB_API); `on_commit` only for losable work (L600). Multi-step writes are database functions; a database function may call another domain's published functions inside the same transaction, so composition across domains happens in the database, and only direct access to another domain's tables is forbidden.
- **Rejected**:
  - P4's automatic merge of disjoint fields: acceptable only for the properties GUARD.5 puts under per-property last-writer-wins (toggles, status, assignment, ordering, L674), which the client sends alone, without the record version. For other fields, a merged result nobody saw is not "without loss" of intent (inferred).
  - Optional preconditions (the Zalando and Google strictness in L260): wins never where a lost update matters, which is every user-edited record in the default.
  - 302 or 307 after POST: wins never (L258).
  - L583's "wrap multi-step writes" as several backend writes in one transaction: replaced by MD-03 (a database function per business operation); not a conflict with the row's intent (atomicity), which the function keeps.
- **Realizes**: ALLOCATION.GUARD.5 and GUARD.6 (skeleton links); ALLOCATION.PRESENT.3 (proposed: drafts in the browser); J4 INTERACTION.COLLABORATE decision 3.
- **Hand-offs**: the version predicate in the write (PIG-WEB.DATA.CONCURRENCY.2, L676); status codes and the idempotency-key contract (PIG-WEB.LOGIC.EXPOSE.2, .3, L269, L546); CSRF token on forms (PIG-WEB.LOGIC.SECURE.3); transaction handling (PIG-WEB.LOGIC.ENFORCE.2).
- **State**: `known | unvalidated: conflict screen content and hidden-field transport inferred (L583 conflict UI inferred); 409 for a stale hidden-field version follows the HTTP interface's mapping (L259); the handling of a form missing its version field and the per-tab draft rule inferred`.

## PIG-WEB.INTERACTION.REALTIME Real-Time Channels

- **Decides**: how the server pushes changes to the browser.
- **Rows**: none (roll-up).
- **Decision**: roll-up of .1 to .5. Push is a hint over a correct pull (J4 COLLABORATE): pages are correct on plain load and clients catch up from a commit-safe cursor. Channels in order of simplicity: none, polling, server-sent events, WebSocket for two-way traffic (.1); every stream resumable, kept alive below the shortest idle timeout, unbuffered, reconnecting with backoff (.2); held by an ASGI process type apart from page workers, fanned out from a Postgres wake-up (.3); same-origin, authenticated by the session cookie, authorized per subscription and per event, bounded (.4); `LISTEN`/`NOTIFY` as a wake-up only, the data in tables (.5).
- **Realizes**: refines INTERACTION.COLLABORATE (J4); PIG-WEB.ALLOCATION.POSTGRES_FIRST, ALLOCATION.GUARD.3, PRESENT.3 through its children.
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited, through .4)`.

## PIG-WEB.INTERACTION.REALTIME.1 Channel Choice

- **Decides**: which channel (polling, long polling, SSE, WebSocket) each push need uses.
- **Rows**: L436, L437, L438, L439, L440, L441, L442. Cited: L435, L006, L682 (J4), L451, L448, L127, L457.
- **Positions**: P1 SSE first for server-to-client push (L436 a, SRC-302 T3: plain HTTP, automatic reconnect and resume); P2 WebSocket first (L436 b, SRC-317 T4 vendor: SSE can be buffered by proxies and CDNs; one two-way channel); P3 the order none, polling, SSE, WebSocket only for two-way needs (L437, inferred, majority); P4 short polling for infrequent updates at second-scale latency (L438, L442: no connection state, works on any process model); P5 long polling, timeout about 30 s (L439).
- **Forces**: the node's purpose is that users learn of changes in time, without correctness depending on the channel. P1 serves operability (ordinary HTTP, built-in resume via `Last-Event-ID`, cookie authentication) at the cost of buffering risk through intermediaries the team does not run. P2 serves two-way traffic and robustness through unknown intermediaries, at the cost of no built-in resume (L453), a hand-built reconnect, upgrade support on every hop (L448) and long-lived connection servers. P4 serves simplicity and any process model at the cost of traffic grown by clients times frequency (L438).
- **Decision**: P3 with P1 as the push default (J4 decision 2 realized; the WebSocket-first position was handed here).
  1. No push where a page's data changes rarely or staleness does not matter.
  2. **Short polling** for slow-changing views with second-scale tolerance, ended by a status code when done (L438, L442).
  3. **Server-sent events** for one-way push (notifications, comment streams, status of long work): resume by event id (.2), authentication by the session cookie, which fits SSE's lack of custom headers (L440; GUARD.4).
  4. **WebSocket only for frequent two-way, low-latency traffic**: live cursors and typing, the collaborative text engine (L441; COLLABORATE.3).
  5. **Long polling** only as a fallback where streaming cannot pass a hop (L439).
  The buffering risk that motivates P2 is contained, not ignored: the team turns buffering off on its own proxy for streaming routes (L451); the client treats a stream that delivers nothing past the heartbeat interval as broken and falls back to polling (inferred); because push is only a hint (L682), a buffered stream delays updates but never corrupts state.
- **Rejected**:
  - P2 as the default: wins when the path to users crosses intermediaries the team cannot configure and buffering is observed there, or when traffic is two-way at high frequency (L436's own fit).
  - L437's "Redis layer when more than one process fans out": narrowed by POSTGRES_FIRST (settled): fan-out starts from a Postgres wake-up and a table re-read (.3, .5); Redis wins past a measured `NOTIFY` limit (L127) or where the chosen framework's only production backend is Redis (L457).
- **Realizes**: J4 INTERACTION.COLLABORATE decisions 1 and 2; PIG-WEB.ALLOCATION.POSTGRES_FIRST (proposed link: no Redis by default).
- **State**: `known | unvalidated: the order rests on a T3 guide (L435, L437 inferred); the buffering claim has one vendor source (L436); the silent-stream fallback is inferred`.

## PIG-WEB.INTERACTION.REALTIME.2 Channel Operation

- **Decides**: how channels resume, stay alive through intermediaries and reconnect.
- **Rows**: L443 to L454 (12 rows). Cited: L682, L594 (DATA), L127, L202.
- **Positions**: the rows are consensus practices except L454 (majority; jitter not in the sources). Competing positions exist on three points: P1 SSE over HTTP/2 (L447, stream limit negotiated) against P2 one stream per tab shared through a shared worker (L447); P3 replay from a store against P4 reload of state on reconnect (L445); P5 WebSocket over HTTP/2 extended CONNECT against P6 HTTP/1.1 upgrade (L449).
- **Forces**: all positions serve continuity of the user's view under dropped and idle connections; P1 costs an HTTP/2 edge, P2 costs client complexity; P3 costs a replayable store, P4 costs a full reload after every gap.
- **Decision**:
  - **No caching of streams**: long-poll and streaming responses `Cache-Control: no-cache`; the SSE client uses no-store (L443).
  - **Resume by a commit-safe cursor**: every event's `id` is the change cursor J4 decided (one no later commit can fall behind, L682 corrected by L594); on reconnect the server replays from the change table after `Last-Event-ID` (P3, L444, L445); when the cursor is too old to replay, the server tells the client to reload state (P4 as the fallback only). The `retry` field tunes reconnect delay (L444).
  - **Known latency cost of the commit-safe cursor**: the cursor PIG-WEB.DATA.CONCURRENCY.5 realizes reads only rows from transactions older than the oldest still in flight (the `xid8` horizon), so one long transaction on the primary holds back every push and every catch-up until it ends. This stall is accepted as the price of never skipping a row. The idle-in-transaction timeout (L202) ends abandoned transactions; a long active transaction is not bounded by it, so the horizon's lag is monitored like the notification queue (.5).
  - **Keep-alive below the shortest idle timeout**: an SSE comment line about every 15 s and WebSocket pings, under every hop's idle timeout; the application's idle timeout above the load balancer's (L446, L450). HTTP/2 PING frames do not count as activity on some balancers (L450 note).
  - **Unbuffered streaming routes only**: buffering off at the reverse proxy for SSE, long-poll and streaming routes (`proxy_buffering off` or `X-Accel-Buffering: no`), served by async workers (L451).
  - **HTTP/2 to the browser** so SSE escapes the six-connection cap (P1, L447); a shared worker holding one stream per origin is acceptable where an HTTP/1.1 hop remains.
  - **WebSocket through the proxy**: `Upgrade` and `Connection` set explicitly at nginx; the whole chain verified (L448); over HTTP/2 only where every hop enables extended CONNECT, HTTP/1.1 upgrade otherwise (L449).
  - **Bounded WebSocket input**: message size and rate capped in the browser handler (no backpressure in the API; L452).
  - **Reconnect with exponential backoff and random jitter, then resync by cursor** (L453, L454): deploys and restarts drop every connection at once.
- **Rejected**: P4 as the normal path: wins only when the cursor is older than the replay window (L445). P6 everywhere: acceptable where any hop lacks extended CONNECT (L449).
- **Realizes**: J4 INTERACTION.COLLABORATE decision 1 and INTERACTION.ENVIRONMENT.5 (retries and catch-up).
- **Hand-offs**: the commit-safe cursor and replay table (PIG-WEB.DATA.CONCURRENCY.5); proxy buffering, HTTP/2 and idle timeouts at the edge (PIG-WEB.TRANSVERSE.TOPOLOGY.1); monitoring of the cursor horizon's lag (PIG-WEB.TRANSVERSE.OPERABILITY.3).
- **State**: `known | unvalidated: jitter (L454) and the replay-window fallback inferred; L445 inferred from the specification; the horizon stall's bound and monitoring inferred`.

## PIG-WEB.INTERACTION.REALTIME.3 Long-Lived Connection Servers

- **Decides**: which server processes hold long-lived connections and how they fan out.
- **Rows**: L455, L456, L457, L458. Cited: L125, L127, L462 to L465 (.5), POSTGRES_FIRST.
- **Positions**: P1 long-lived connections on an ASGI server (L455, consensus T1); P2 streaming under WSGI (rejected in L455: a worker held for the whole stream); P3 long-lived connections in their own process type apart from short-request workers (L458, majority, inferred); P4 the same workers serve pages and streams (the alternative L458 rejects). Fan-out: P5 an in-process registry (L456: one process only); P6 a Redis-backed channel layer (L457, Django's only production backend); P7 a Postgres wake-up per process, which re-reads tables and fans out in memory (L465; POSTGRES_FIRST).
- **Forces**: P1 and P3 serve page requests that never starve behind sockets and independent scaling, at the cost of a second process type. P6 serves high fan-out at the cost of a second store; P7 serves one store and transactional consistency of the change and its notification, up to `NOTIFY`'s commit serialisation under write concurrency (L127).
- **Decision**:
  - **An ASGI process type dedicated to long-lived connections** (SSE, WebSocket, long polling), routed by path at the proxy, apart from the page and API workers, each scaled on its own measure (P1, P3). It is a process type of the same backend deployable, not a separate service: each backend is one deployable and is not split into services without a measured need.
  - **Fan-out from Postgres** (P7): each connection process holds one listening connection (.5), wakes on a notification, reads new changes after its last cursor from the change table, and pushes to its local subscribers after the per-subscriber filter (.4). No Redis in the default (POSTGRES_FIRST).
  - **Redis** (or a channel layer on it) when a measured limit is reached (`NOTIFY` commit serialisation, L127) or when the framework chosen for WebSocket groups has Redis as its only production backend (L457), with the change still committed to the table first (no dual write; RECORD.1).
- **Rejected**: P2: wins never for long-lived connections (L455). P4: acceptable while long-lived connections are few and the whole application already runs on ASGI with no synchronous workers (inferred). P5 alone: acceptable with exactly one connection process (L456).
- **Realizes**: PIG-WEB.ALLOCATION.POSTGRES_FIRST (proposed link: Postgres carries the wake-up role until a measured limit); ALLOCATION.RECORD.1 (the table is the source, push a copy).
- **Hand-offs**: process types and their placement (PIG-WEB.TRANSVERSE.TOPOLOGY.2, .3); the application concurrency model (PIG-WEB.LOGIC.ENFORCE.4).
- **State**: `known | unvalidated: separate process type (L458 inferred) | open: the NOTIFY threshold (L127)`.

## PIG-WEB.INTERACTION.REALTIME.4 Channel Security

- **Decides**: how long-lived connections are authenticated, authorized and bounded.
- **Rows**: L459, L460, L461. Cited: L022, L644, L686, L687 (J4), L463.
- **Positions**: P1 `wss` only, Origin checked against an allowlist at the handshake, no tokens in URLs, compression off unless needed, messages untrusted (L459, consensus); P2 authorization once at connect (rejected in L460); P3 authorization of each channel and each message against the read rights of the target, connections closed at session expiry or logout (L460, merging COLLAB-C24); P4 caps on message size, message rate and connections per client (L461).
- **Forces**: P1, P3, P4 serve confidentiality and availability, at the cost of a check per event and per subscription; P2 serves throughput and leaks every change made after a right is revoked.
- **Decision**: P1, P3, P4.
  - **Transport and origin**: TLS only; the WebSocket handshake and SSE endpoint check `Origin` against an explicit allowlist (cross-site WebSocket hijacking); compression off unless measured necessary (L459).
  - **Authentication by the session cookie** (HttpOnly, Secure, SameSite; GUARD.4); no session token, bearer token or long-lived credential ever travels in a URL (L459; J4 ENVIRONMENT.6, whose one exception, signed file-delivery URLs, does not apply to channels); agent clients use their bearer credential in the header on WebSocket-capable transports (inferred).
  - **Authorization per subscription and per event**: subscribing to a channel checks the user's right to read its target; each event is filtered per subscriber against the target's read rights before it is sent, with the same filter as every other surface (L460, L686, L687). Event payloads carry identifiers, the cursor and a change kind; content is fetched through the normal authorized endpoints (L463 applied to the browser hop, inferred), unless it has passed the same per-recipient filter.
  - **Session end closes the stream**: on logout or expiry the connection is closed; the connection process re-checks the session at an interval no longer than the session's idle timeout (interval inferred).
  - **Bounds**: message size, message rate and connections per user and per client capped; every inbound message parsed as untrusted input (L459, L461).
  - **Who filters reads across backends**: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (inherited from ALLOCATION.GUARD.3). Recorded default: each backend's connection process filters these reads from one shared written specification, with the shared denial-test suite covering the real-time channel; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Not settled here.
  - **Consequence of the default**: roles that may SELECT the base tables (reporting, operator) see every row, the change table and comments included, unless their own role is restricted. Per-event filtering protects the channel the application serves, nothing stronger. For comments, J4 COLLABORATE's restriction applies until the question is answered: those roles get no SELECT on comment content or on comments with a narrower audience than their target (grants: PIG-WEB.DATA.GUARD.2); otherwise the leak to them is a stated known limit.
- **Rejected**: P2: wins never (L460). Tokens in query strings for WebSocket authentication: wins never (L459).
- **Realizes**: ALLOCATION.GUARD.3 (proposed link, requires: per-subscriber filtering follows the authorization placement, its open read clause included); ALLOCATION.GUARD.4 (proposed: session cookie authenticates the channel); J4 INTERACTION.ENVIRONMENT.7.
- **Hand-offs**: session revocation signal (PIG-WEB.LOGIC.SECURE.2); per-client connection limits at the edge (PIG-WEB.LOGIC.SECURE.6); comment grants of reporting and operator roles (PIG-WEB.DATA.GUARD.2).
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from ALLOCATION.GUARD.3) | unvalidated: identifier-only payloads and the session re-check interval inferred`.

## PIG-WEB.INTERACTION.REALTIME.5 Database Notifications

- **Decides**: how Postgres notifications wake application processes.
- **Rows**: L462 to L467 (6 rows). Cited: L125, L127 (POSTGRES_FIRST), L202, L567, L594, L624.
- **Positions**: P1 `LISTEN`/`NOTIFY` as a wake-up signal, data in tables (L462, L463, L467, consensus T1); P2 `NOTIFY` as a message carrier, counter or event log (rejected in L462, L464, L467); P3 polling the change table without notifications (L467's fallback). Connection: P4 a direct session-level connection per process (L465); P5 through a transaction-pooling pooler (rejected in L465).
- **Forces**: P1 serves low-latency wake-up without a second store, bounded by at-most-once delivery, an 8000-byte payload and a global commit lock under write concurrency (L127). P2 loses events with no listener and collapses duplicates. P3 serves robustness at the cost of poll latency and load.
- **Decision**: P1 with P3 as the safety net (POSTGRES_FIRST realized).
  - The **writer function that commits a change also writes the change row and issues `NOTIFY` with an identifier payload** in the same transaction (L462, L463; issuer under MD-03 inferred): notification is delivered at commit, in commit order, never for a rolled-back change.
  - Consumers **`LISTEN` and commit, then read current state, then rely on notifications** (L463); on every wake-up they re-read from the table after their cursor; identical notifications collapsing to one is harmless (L464).
  - Events that must not be lost are rows (outbox or change table); `NOTIFY` or a poll only wakes the reader (L467). A low-frequency poll of the same table covers a missed wake-up (P3, interval inferred).
  - **`NOTIFY` only where a change has live subscribers**: a full notification queue makes committing transactions fail (L462), so with `NOTIFY` issued from writer functions one stuck listener could fail core writes. Only the writer functions whose changes feed a real-time channel issue it; others write their change rows without notifying (inferred).
  - **One direct, session-level listening connection per process**, outside any transaction, never through a transaction-pooling pooler (L465, L466); listener sessions run under the idle-in-transaction timeout (L202), so a listener stuck in a transaction is ended before it fills the queue.
  - **Queue usage is monitored**; a listener in a long transaction is an incident (L466).
  - **Tests**: the wake-up path only shows at commit (notification delivered at commit, in commit order), so it is tested with committing sessions in a disposable database, never a shared one; logic tests on shared data stay in never-committing transactions.
- **Rejected**: P2: wins never (L462, L464, L467). P5: wins only with a pooler that explicitly supports `LISTEN` (L465). P3 alone: acceptable when the measured `NOTIFY` limit is reached (L127) or the latency of the poll interval is tolerable.
- **Realizes**: PIG-WEB.ALLOCATION.POSTGRES_FIRST (skeleton link, requires); ALLOCATION.ACT.2 (proposed: the staged intent in the function's transaction, delivered after commit).
- **Hand-offs**: queue-usage monitoring (PIG-WEB.TRANSVERSE.OPERABILITY.3); the change table and its cursor (PIG-WEB.DATA.CONCURRENCY.5); pooler configuration and the idle-in-transaction timeout (PIG-WEB.DATA.INTERFACE.2); committing tests in a disposable database (PIG-WEB.TRANSVERSE.OPERABILITY.5).
- **State**: `known | unvalidated: the writer function as issuer (MD-03), the safety-net poll, the monitoring advice (L466) and NOTIFY limited to changes with live subscribers inferred | open: NOTIFY threshold (L127)`.

## PIG-WEB.INTERACTION.COLLABORATE Comments and Collaboration

- **Decides**: how comments, threads, shared text editing, notifications and moderation are realized.
- **Rows**: none (roll-up).
- **Decision**: roll-up of .1 to .4. Comments are their own rows (J4), anchored to their target by a foreign key and the target version they were written against, with redundant selectors for text ranges and an explicit anchor state (.1); threads by parent pointer with a thread-root id, resolution on the root, tombstones and append-only revisions (.2); a server-authoritative text engine only for long collaborative text fields (.3); notifications as rows written with the comment, moderation as a recorded queue (.4). Every write is one writer-function call (MD-03); abilities and visibility follow the authorization placement, its open read clause included.
- **Realizes**: refines INTERACTION.COLLABORATE (J4); ALLOCATION.GUARD.3, GUARD.5, ACT.2, ACT.4 through its children.
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited, through .4) | unvalidated: single-source comment model (.1, .2)`.

## PIG-WEB.INTERACTION.COLLABORATE.1 Comment Anchoring

- **Decides**: to what a comment is anchored and how anchors survive edits.
- **Rows**: L665, L666, L667, L668. Cited: L664 (J4), L684, L260.
- **Positions**: anchor granularity: P1 record (L665 default), P2 field, P3 version (L666), P4 text range (L667); range storage: P5 redundant selectors (exact quote with prefix and suffix, character offsets, structural path) (L667), P6 offsets alone (rejected in L667 unless text is immutable per version); anchor loss: P7 explicit states (anchored, moved, orphaned, outdated), comment kept visible apart (L668), P8 delete or silently reattach (rejected in L668).
- **Forces**: P1 serves simple queries and permissions; P3 serves the comment's meaning over time and auditability, at the cost of a version lookup (L666); P5 serves anchors that survive edits; P7 serves no silent loss of discussion.
- **Decision**:
  - **Anchor by identity**: a mandatory foreign key to the target record, plus an optional field name for per-attribute review (L665, L664). A type-and-id pair without a foreign key is not an anchor (integrity, inferred; table shape is DATA's).
  - **The target version is always recorded** (P3, L666): the default already versions every user-edited record (GUARD.5, L260) and writes its history (ACT.4, L684), so the cost L666 counts is paid; the interface marks a comment written on an earlier version. This takes L666 from "when" to "always" (inferred from those two placements).
  - **Ranges only for long text**, stored with redundant selectors (P5); offsets alone suffice for text immutable per version (L667).
  - **Anchor state is explicit**: anchored, moved, orphaned or outdated; a comment whose anchor is lost stays visible in a separate place, never deleted or silently reattached (P7, L668).
  - Comments are written through the comment writer function (MD-03: the comment, its notification rows and history are one multi-table operation).
- **Rejected**: P1 alone (without version): acceptable when the target is not versioned (no such target among user-edited records in the default). P6: acceptable when the text is immutable per version (L667). P8: wins never (L668).
- **Realizes**: J4 INTERACTION.COLLABORATE decision 5; ALLOCATION.GUARD.5 and ACT.4 (proposed links: the version and history it reuses); ALLOCATION.ACT.1 (proposed: one writer function).
- **Hand-offs**: comment and target table shapes (PIG-WEB.DATA.ORGANIZE.1, .2).
- **State**: `known | unvalidated: L665 inferred from one T1 model (SRC-376); "always record the version" inferred from GUARD.5 and ACT.4`.

## PIG-WEB.INTERACTION.COLLABORATE.2 Threads and Comment Lifecycle

- **Decides**: how threads are stored and resolved and how comments are edited and deleted.
- **Rows**: L669, L670, L671, L672, L673. Cited: L686 (J4), L684, L205, L209, L523 (MAINT), L525 (MAINT), L689.
- **Positions**: thread storage (L669, contested): P1 adjacency list with a displayed-depth cap; P2 path enumeration (`ltree`); P3 closure table. P4 a denormalized thread-root id on each reply (L670). Resolution: P5 state on the root (open or resolved, by whom, when), reversible, never a deletion, by the target's author or users with write rights on the target (L671); P6 any commenter resolves (L671, for open discussion without an owner). Deletion: P7 tombstone (content cleared, `deleted_at` and actor kept, replies preserved) (L672); P8 hard delete (L672, when erasure overrides). Edits: P9 append-only revisions shown as "edited" (L673, no source); P10 an edited flag only (L673, casual chat).
- **Forces**: P1 serves simple writes and integrity at the cost of a recursive read; P2 and P3 serve subtree reads at the cost of moves and writes. P4 serves one indexed thread read at the cost of a column set once. P5 serves workflow clarity and accountability. P7 and P9 serve thread integrity and moderation evidence, at the cost of storage; P8 serves privacy erasure.
- **Decision**:
  - **Adjacency list with one displayed level of replies** (P1; the depth most review tools use, L669 citing SRC-411) and a **thread-root id set once at insert** (P4, L670), so a thread loads in one indexed query and resolution, counts and permissions attach to the root.
  - **Resolution on the thread root**, reversible, never a deletion (P5, L671). Who may resolve follows GUARD.3 as settled (J4 decision 6): the row-decidable part (the target's author, L671) is decided by the writer function; users with write rights on the target and the product roles that grant "resolve" are each backend's policy. No source gives the thread's opener a resolve right, so none is stated.
  - **Deletion is a tombstone** (P7, L672): content cleared, `deleted_at` and actor kept, replies preserved. It is an update through the comment's deletion function, never a bare update or a DELETE grant (L523, L525). Keeping the replies is an explicit, justified deviation from the default soft-delete cascade (L523: a cascade equals what a native cascading delete would remove unless each deviation is explicit): a thread stays readable when one comment goes.
  - **Every edit is an append-only revision**, shown as "edited" (P9, L673): what was said and when stays reconstructable; the revision rows are the comment's history (ACT.4).
  - A tombstone clears the visible content; earlier revisions stay under the history's retention and access rules (moderators only) until a retention or erasure rule removes them (inferred; erasure itself is the deferred personal-data node).
  - **Erasure against the archive rule (recorded tension, not settled here)**: the maintainer doctrine allows hard deletion only for rebuildable derived data or after copying the row to an archive in the same operation, and grants no DELETE to application roles (L525). An archive copy defeats an erasure that must remove personal data. Hard deletion of comment content or revisions for erasure (P8) is therefore handed to the deferred personal-data node (PIG-WEB.DATA.MAINTAIN.6), which must reconcile it with L525. The default deletion mechanism for user-facing data awaits the maintainer at PIG-WEB.DATA.MAINTAIN.2; a tombstone keeps threads intact under either answer (inferred).
- **Rejected**: P2, P3: win when whole-subtree reads dominate and writes and moves are rare (L669). P6: acceptable for open discussion without an owner (L671). P8: wins when a privacy erasure or retention rule demands it (L672), through a deletion function, its tension with L525's archive copy handed to PIG-WEB.DATA.MAINTAIN.6. P10: acceptable for casual chat with no business or regulated use (L673), not the default.
- **Realizes**: J4 INTERACTION.COLLABORATE decisions 5 and 6; ALLOCATION.ACT.4 (proposed: revisions are history written in the same transaction); ALLOCATION.GUARD.3 (proposed: resolve right).
- **Hand-offs**: deletion and retention policy per entity (PIG-WEB.DATA.MAINTAIN.2, L205); history tables (PIG-WEB.DATA.MAINTAIN.3); personal-data erasure (PIG-WEB.DATA.MAINTAIN.6, deferred).
- **State**: `known | unvalidated: L669 contested (T4 comparison), L670 synthesis, L673 without source; revisions kept after tombstone inferred | gap: erasure deferred; its tension with L525's archive copy handed to PIG-WEB.DATA.MAINTAIN.6`.

## PIG-WEB.INTERACTION.COLLABORATE.3 Collaborative Text Editing

- **Decides**: which engine merges concurrent edits of long text, and for which fields.
- **Rows**: L677, L679, L680. Cited: L302, L674, L678 (GUARD.5), RECORD.1.
- **Positions** (L677, contested): P1 central-authority steps (ProseMirror, Figma: the server orders and accepts steps); P2 CRDT (Yjs; offline, multi-device, peer-to-peer, end-to-end encryption); P3 operational transformation (only where already invested). Scope: P4 optimistic versions for structured fields and a text engine only for genuinely collaborative long-text fields (L679); P5 an engine for the whole record (the over-engineering L678 warns against). P6 count a CRDT's cost first: 1.5x to 2x storage, no accepted move, peers cannot enforce server rules (L680).
- **Forces**: P1 serves convergence with server-enforced permissions and history, at the cost of always-online editing. P2 serves offline and peer editing, at the cost of storage, moves, and rules no server can enforce per operation (L680). P4 serves minimum machinery for maximum correctness.
- **Decision**: P4 with P1.
  - **Structured fields keep optimistic versions** (EDIT); only fields that people genuinely write together (description, notes, document body) get a text engine (L679, L678).
  - **The engine is server-authoritative** (P1): clients send steps against the document version they hold; the server accepts steps only against the current version, checks the user's edit right on each batch, persists accepted steps and the document through the writer function with the expected version (GUARD.5 detection in the database, MD-03; persistence path inferred), and broadcasts them; a client behind rebases and resends. This is the position L677 names for "a classic site with a server and permission checks".
  - Steps travel on a WebSocket (REALTIME.1: two-way, high frequency); presence and cursors on the same channel with a timeout, never in tables (PRESENT.3).
  - Comments are append-only rows and need no merge (L679).
- **Rejected**: P2: wins when RECORD.1's condition moves the system of record (offline use, multi-device sync or user-owned data, L302); vetoed while business rules must hold on every change (L680). P3: only where an OT implementation is already in place (L677). P5: wins never (L678).
- **Realizes**: ALLOCATION.GUARD.5 (skeleton link: the engine where the conflict policy calls for one); ALLOCATION.RECORD.1 (proposed: the server stays the authority); ALLOCATION.PRESENT.3 (presence).
- **Hand-offs**: the long-lived connection process (REALTIME.3); version predicate in the write (PIG-WEB.DATA.CONCURRENCY.2).
- **State**: `known | unvalidated: L679 secondhand (SRC-407); persistence through the writer function inferred`.

## PIG-WEB.INTERACTION.COLLABORATE.4 Notifications and Moderation

- **Decides**: how collaboration notifications are created and how comments are moderated.
- **Rows**: L683, L689. Cited: L624, L409, L410 (ACT.2), L686, L687 (J4), L659, L525 (MAINT).
- **Positions**: notifications: P1 rows (recipient, reason, target, read state) created in the same transaction as the comment, delivered asynchronously from those rows; mentions parsed on the server and each mentioned user's right to see the target checked before notifying (L683, inferred synthesis); P2 notifications sent directly from the request (the lost or phantom case L683 rules out). Moderation: P3 a queue: report row, status, action (hide, restore, remove) with reason, actor and time written to history; hide first; delete only by a retention or legal rule; authors edit their own comments within a stated window (L689, inferred); P4 hide and author edit only (L689, internal team comments).
- **Forces**: P1 serves no lost, phantom or leaking notification; P2 serves only fewer rows. P3 serves accountability and appeal, at the cost of a queue and a workflow; P4 serves simplicity where nobody outside the team reads or reports.
- **Decision**:
  - **Notifications are rows written by the comment writer function in the comment's transaction** (P1; MD-03: a multi-table operation; ACT.2's staged intent), delivered after commit from those rows (in-app read state; the real-time wake-up of REALTIME.5); external delivery (email, push) is the deferred delivery node.
  - **Mentions are parsed on the server** and a notification is created only for a recipient who may see the target (L683, L687: notifications are a secondary surface).
  - **Who checks a recipient's read right across backends**: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (inherited from ALLOCATION.GUARD.3). Recorded default: the backend that submits the comment checks each recipient against the one shared written specification before passing recipients to the writer function, covered by the shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Not settled here.
  - **Consequence of the default**: roles that may SELECT the base tables (reporting, operator) see every row, comments and notification rows included, unless their own role is restricted; the recipient check protects the notifications the application sends, nothing stronger. Until the question is answered, J4 COLLABORATE's restriction applies: those roles get no SELECT on comment content or on comments with a narrower audience than their target, and read comments only through a projection limited to target-wide audiences, or not at all (grants: PIG-WEB.DATA.GUARD.2); otherwise the leak to them is a stated known limit.
  - **Moderation actions are always recorded**: hide and restore with reason, actor and time written to history; hide first, remove only under a retention or legal rule; authors edit their own comments within a stated window, each edit a revision (.2). Removal runs through a deletion function, never a DELETE grant (L525); where a legal rule demands erasure rather than an archive copy, the tension with L525 is the personal-data node's (PIG-WEB.DATA.MAINTAIN.6, deferred).
  - **A report queue** (report rows, status, decision) is required whenever comments are visible to people outside the team (customers, the public) (P3, L689).
  - Moderate is a separate ability (L686); agent-authored comments are marked and filterable as a class (L659).
- **Rejected**: P2: wins never (L683). P4 (no report queue): acceptable when only team members read and write comments (L689); the recorded hide and restore stay.
- **Realizes**: ALLOCATION.ACT.2 (skeleton link: notifications as staged side effects); ALLOCATION.GUARD.3 (proposed, requires: recipient visibility, open read clause included); ALLOCATION.ACT.4 (proposed: moderation history).
- **Hand-offs**: notification delivery worker (PIG-WEB.LOGIC.PROCESS.2); email and push (PIG-WEB.LOGIC.PROCESS.7, deferred); comment grants of reporting and operator roles (PIG-WEB.DATA.GUARD.2); erasure against the archive rule (PIG-WEB.DATA.MAINTAIN.6, deferred).
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from ALLOCATION.GUARD.3; recorded default: the submitting backend checks recipients from the shared specification) | open: author edit window value | unvalidated: L683 and L689 are syntheses | gap: legal moderation obligations not read (L689)`.

## PIG-WEB.INTERACTION.AGENT Agent Surface

- **Decides**: how agents reach, identify themselves to, act through and are limited by the application.
- **Rows**: none (roll-up).
- **Decision**: roll-up of .1 to .5. One HTTP core described by OpenAPI, always in sync (MD-02), with an MCP adapter over it for third-party agent hosts whose tool list and schemas have one origin, a CI drift gate and additive evolution under the compatibility window; a stateless surface over OAuth (.1); protected-resource metadata, verifiable client identity, client ID metadata documents (.2); agents with their own identity acting for a user, both recorded, short-lived credentials with an owner, sender-constrained tokens for consequential scopes (.3); irreversible or external effects approved by the owning user on the application's own page and checked on the server, credentials collected out of band, structural injection defence (.4); problem-detail errors, agent-shaped responses, quotas per agent within the user's allowance, and scarce-goods flows that a human completes or agents are excluded from (.5).
- **Realizes**: refines INTERACTION.AGENT (J4); ALLOCATION.RULES.4, GUARD.3, GUARD.4, GUARD.6, ACT.4 through its children.
- **State**: `known | unvalidated: moving specifications (.1 to .3)`.

## PIG-WEB.INTERACTION.AGENT.1 Surface and Protocol

- **Decides**: which protocol surface and content forms agents get, and how the surface keeps state.
- **Rows**: L634, L635, L636, L661, L663. Cited: L633 (RULES.4), L054, MD-02.
- **Positions**:
  - Contract: P1 a machine-readable OpenAPI description generated from or checked against the implementation (L634, consensus T1).
  - Protocol (L635, contested): P2 an MCP server as the agent surface (third-party hosts connect without bespoke integration); P3 plain HTTP and OpenAPI only (one surface, less to secure); P4 both layered, MCP over the same HTTP core.
  - Content (L636, contested, T4): P5 publish `llms.txt`; P6 `llms.txt` is unused by AI services, spend nothing; P7 content negotiation (`Accept: text/markdown`, `Vary: Accept`) on the same URL.
  - State: P8 a stateless surface; cross-call state as an explicit server-minted handle validated against the caller on every call (L661); P9 hidden per-connection session (rejected in L661).
  - Transport (L663): P10 remote HTTP with OAuth; P11 local stdio with environment credentials, sandboxed; P12 local HTTP with an authorization token.
- **Forces**: the node's purpose is agents' ability to work with the data, bounded. P2 and P4 serve reach (hosts the team does not control), at the cost of one more surface to secure and maintain; P3 serves a smaller attack surface and loses third-party hosts. P5 to P7 serve agent token cost for content, on thin evidence. P8 serves scalability behind load balancers and security; P9 serves nothing a handle cannot.
- **Decision**:
  - **One core, one description**: the HTTP interface is described by OpenAPI kept always in sync with the implementation (MD-02, L634); the origin direction is the project's recorded choice (TYPE_CHAIN). Humans' pages, JSON clients and agents reach the same core (RULES.4, L633).
  - **An MCP adapter over the same core** for third-party agent hosts (P4): the default context has agents as users, which means agents the team does not build; the adapter only translates and shapes (L633), so the added surface holds no rule. Tools are few and purpose-specific (J4 AGENT, L645).
  - **The tool surface is an interface description too** (MD-02 covers every agent-facing interface): the tool names, input schemas and result shapes have one origin. They are generated from the core description, or checked against it for conformance, and the same CI gate fails on drift. They change additively; a breaking tool change goes expand, migrate, contract under the compatibility window J4 ENVIRONMENT.3 sets, so agents built against the old tools keep working through a deploy.
  - **Stateless surface** (P8, L661; LOGIC.EXPOSE.2, L054): no hidden per-connection session; cross-call state is a server-minted, unguessable handle checked against the caller on every call.
  - **Transport by trust boundary** (L663): the hosted surface is remote HTTP with OAuth (P10); a developer-local tool shipped with the product, if any, uses stdio with environment credentials in a sandbox (P11); a local HTTP server requires an authorization token (P12).
  - **Content for agents**: data through the API and the MCP adapter, never by scraping pages; pages stay semantic server-rendered HTML (VISUALIZE.1, .4), readable as they are. `llms.txt` is not relied on for discovery (P6, L636).
- **Rejected**:
  - P3 alone: wins when every agent client is the team's own code (L635 b).
  - P2 without the HTTP core: wins never; MCP sits on the core (L635).
  - P5: acceptable for a developer-documentation site whose readers' coding agents fetch it on purpose (L636 a).
  - P7: acceptable when pages already pass a CDN that converts them (L636 c); its cost in cache variants is unweighed.
  - P9: wins never (L661).
- **Realizes**: ALLOCATION.RULES.4 (proposed: one more adapter on the same core); ALLOCATION.RECORD.3 and PIG-WEB.ALLOCATION.TYPE_CHAIN (proposed: the description always in sync, MD-02).
- **Hand-offs**: payload schemas and API evolution (PIG-WEB.LOGIC.EXPOSE.6, .7); description drift gate in CI, extended to the MCP tool list and schemas (PIG-WEB.TRANSVERSE.CONTRACTS.1: the contract-verification judge should name the tool surface among the descriptions its gate checks).
- **State**: `known | unvalidated: P4 as default inferred from the default context (L635 inferred); content forms speculative (L636 T4); generation or conformance check of tool schemas from the core description inferred | open: MCP specification moving (L661)`.

## PIG-WEB.INTERACTION.AGENT.2 Discovery and Registration

- **Decides**: how agent clients discover the authorization server and register.
- **Rows**: L637, L653, L654. Cited: L662 (LOGIC.SECURE.7), L652 (J4).
- **Positions**: P1 OAuth Protected Resource Metadata and `WWW-Authenticate` with `resource_metadata` on unauthenticated requests (L637, consensus T1); P2 out-of-band configuration (the alternative L637 removes). Identity: P3 verifiable client identity (OAuth client ID metadata documents, or signed HTTP requests) (L653, majority, draft T2); P4 a self-declared User-Agent (rejected in L653). Registration (L654): P5 client ID metadata documents; P6 dynamic client registration; P7 pre-registration; all with per-client consent and exact redirect matching.
- **Forces**: P1 and P5 serve open-ecosystem interoperability; P3 serves attribution and per-agent policy (J4 decision 7); P6 serves compatibility with older clients at the cost of registry sprawl; P7 serves a small known set of agents.
- **Decision**:
  - **Publish protected-resource metadata** and answer unauthenticated calls with `WWW-Authenticate` carrying `resource_metadata` (P1, L637).
  - **Agent clients prove who they are** through OAuth client identity or signed requests, never a User-Agent string (P3, L653); this identity keys the per-agent quota (.5) and the agent marking in data (.3).
  - **Client ID metadata documents first**; dynamic client registration kept only for compatibility; pre-registration for closed sets; consent per client and exact redirect URI matching always (L654).
  - **Only one-time codes travel in redirects**: the authorization code in the redirect URL is single-use, short-lived and bound to the client by PKCE; no session token, bearer token or long-lived credential ever travels in a URL (J4 ENVIRONMENT.6; PKCE binding inferred as the condition).
  - Fetching a client's metadata document is a server-side fetch of a client-named URL: private, loopback and link-local ranges are blocked and every redirect hop validated (L662).
- **Rejected**: P2: acceptable for a closed set of pre-registered agents (P7 condition). P4: wins never as identity (L653). P6 as the primary path: wins only for clients that cannot publish a metadata document (L654).
- **Realizes**: ALLOCATION.GUARD.4 (proposed: agents hold their own revocable credentials); J4 INTERACTION.AGENT decisions 3 and 7.
- **Hand-offs**: the authorization server itself and federated login (PIG-WEB.LOGIC.SECURE.4); server-side fetch defence (PIG-WEB.LOGIC.SECURE.7).
- **State**: `known | unvalidated: L653 and L654 rest on drafts and a moving specification`.

## PIG-WEB.INTERACTION.AGENT.3 Identity and Delegation

- **Decides**: how an agent identity, its delegating user and its credentials are represented and recorded.
- **Rows**: L638, L639, L641, L643, L659, L660. Cited: L022, L311, L566 (MAINT), L685, L658, R1-3 of the J1 records.
- **Positions**: identity (L638): P1 the agent is the user (user token); P2 the agent has its own identity and permissions; P3 the agent acts for a user with both recorded, the strongest as a delegated token carrying both (RFC 8693 `act`, L639). Token binding (L641, contested): P4 short-lived, sender-constrained tokens (DPoP or mutual TLS); P5 plain bearer tokens, short-lived and narrow. P6 authorization bound to the transaction details for consequential operations (Rich Authorization Requests, L643, inferred for agents). P7 agent-originated writes marked in the data (actor type and id next to the user) (L659). P8 agent credentials with an owner and a lifecycle: short-lived, one revocable credential per agent, recorded sponsor, removal without orphaned permissions (L660).
- **Forces**: P3 serves audit and least privilege at the cost of design; P1 serves simplicity and loses attribution. P4 serves theft resistance at the cost of client complexity; P5 serves interoperability with today's agent clients. P6 serves least privilege on irreversible actions at the cost of authorization-server support. P7 and P8 serve review, undo and containment.
- **Decision**:
  - **P3**: an agent has its own identity and acts for a user; tokens carry the subject and the actor (`act` claim or its documented equivalent), so downstream services and logs see both and any chain (L638, L639).
  - **Both identities reach the database**: the backend asserts the user and the agent as the claimed actor in the transaction-local setting (L311, L566, L685), checked against the backend's role and recorded with the session role (J1 default context, R1-3); agent-originated writes are marked as a class (P7, L659).
  - **Token binding by consequence** (L641 composed, not split): tokens are short-lived and audience-bound (J4) for every scope; scopes that allow consequential operations (payments, transfers, deletions, bulk exports, the list of L643) require a sender-constrained token (DPoP or mutual TLS); short-lived, narrow bearer tokens are accepted for the rest, which keeps open agent clients able to connect.
  - **Consequential operations bound to their details**: Rich Authorization Requests where the authorization server supports them (P6); otherwise the exact-action approval of .4 binds the operation (inferred substitution).
  - **Credential lifecycle** (P8, L660; GUARD.4): one revocable credential per agent, a recorded sponsor, short lifetimes, and removal that leaves no orphaned permission.
- **Rejected**: P1: acceptable for a personal tool where the user and the agent are the same accountable party and no consequential scope is granted (L638 a). P2 alone: wins for unattended automation with no delegating user (L638 b), still recorded as the actor. P5 for consequential scopes: wins never; acceptable for the rest. P4 for every scope: wins when every agent client can hold a key (L641).
- **Realizes**: ALLOCATION.GUARD.4 (skeleton link); ALLOCATION.ACT.4 (proposed: both identities in the audit, L658); ALLOCATION.GUARD.3 (actor assertion, R1-3).
- **Hand-offs**: actor columns and history (PIG-WEB.DATA.MAINTAIN.3, L685); token issuance (PIG-WEB.LOGIC.SECURE.4).
- **State**: `known | unvalidated: "both is the max" inferred (L638); agent parameters of RFC 8693 open (L639); L643 inferred for agents; binding by consequence is a composition of L641`.

## PIG-WEB.INTERACTION.AGENT.4 Approval and Injection Defense

- **Decides**: how consequential agent actions are approved and how prompt injection is contained.
- **Rows**: L646, L647, L649, L650. Cited: L644, L648 (J4), L643, L659, GUARD.3.
- **Positions**: approval (L646, contested): P1 per-action human confirmation of the exact action; P2 classifier or policy auto-approval (17% false negatives on overeager actions, SRC-399 T3); P3 structural limits so approval is rarely needed (Rule of Two, CaMeL; costs capability); P4 out-of-band approval on a separate device (defeats a compromised client). P5 secrets, payment details and third-party authorization collected in the application's own page, never through the agent's context, bound to the same user (L647). Injection (L649, contested): P6 structural first, filters second; P7 filters as the main control. P8 the server never relies on client hints (tool annotations, claimed identity, client name) (L650).
- **Forces**: the node serves security of the user's data against the agent's throughput. P1 is strongest per action and causes approval fatigue when frequent; P2 keeps flow and misses consequential actions; P3 gives the strongest guarantee at a capability cost; P4 resists a compromised agent host. P5 keeps credentials out of model context and logs. P6 reduces residual risk; P7 alone leaves it.
- **Decision**: the approval design follows reversibility and blast radius (L646), and the approval lives on the server.
  - **Reads and reversible writes proceed**, authorized as every request is (GUARD.3; L644).
  - **Irreversible or external effects** (the consequential list of .3) **need approval by the user who owns the authority, shown the exact action, on the application's own page** (P1 realized out of band, P4): the agent's call creates a pending operation with its exact parameters; the user approves it in the application, authenticated by their own session; the writer function that performs the effect refuses an agent-originated operation without a matching approval by the delegating user (a rule decidable from the stored rows and the actor, so the writer function's under GUARD.3; inferred). An approval dialog in the agent host is a client hint, never the gate (P8, L650).
  - **Approvals stay rare** by scoping: only irreversible or external effects ask, so fatigue does not erode them (inferred from L646's 93% figure).
  - **Credentials, payment details and third-party authorization** are collected on the application's own page, bound to the user who started the flow, never through the agent (P5, L647).
  - **Injection is contained structurally** (P6, L649): few purpose-specific tools (J4), no agent session the application runs holds untrusted input, private data and outward power together (L648), filters only as an extra layer.
  - **No client hint is enforcement** (P8, L650): annotations, claimed identity and client names are untrusted.
- **Rejected**: P2: acceptable only for recoverable effects in developer tooling (L646 b), not for this application's consequential effects. P3 alone: the default for agents the application runs that read untrusted content (J4 decision 6), not a substitute for approval of irreversible effects. P7: wins never as the only control (L649).
- **Realizes**: ALLOCATION.GUARD.3 (skeleton link, requires: approval never replaces the authorization authority); ALLOCATION.ACT.1 (proposed: the effect's writer function checks the approval).
- **Hand-offs**: pending-operation storage (PIG-WEB.DATA.ORGANIZE); the approval page and its session (PIG-WEB.LOGIC.SECURE.2).
- **State**: `known | unvalidated: L646 is a synthesis; server-held approval checked by the writer function inferred`.

## PIG-WEB.INTERACTION.AGENT.5 Agent-Shaped Responses and Limits

- **Decides**: how responses, errors and rate-limit partitions are shaped for agent callers.
- **Rows**: L651, L656, L657. Cited: L652 (J4), L034, L052, L269.
- **Positions**: rate-limit partition (L651, contested): P1 per user; P2 per agent identity; P3 per client application; P4 a combination. Errors: P5 machine-readable problem details (type, status, detail, extensions), tool errors that tell the model how to correct the call (L656, consensus). Responses: P6 paginated and filtered by default, high-signal fields, size caps, readable labels beside opaque, unguessable handles, ownership checked on the server (L657).
- **Forces**: P1 is fair among humans and lets a delegated agent starve its user; P2 isolates agents and needs agent identity (.3); P3 protects the service from one integration. P5 serves recoverability and fewer wasted calls; P6 serves token cost and accuracy.
- **Decision**:
  - **Nested partitions** (P4): each agent identity has its own quota inside its user's allowance, so a runaway agent exhausts only its own share; each client application has a ceiling across its users; the user's own interactive traffic is counted apart from their agents' (J4 decision 7; nesting inferred). The flows whose automation harms the business carry their own per-flow limits (J4).
  - **Scarce-goods flows are closed to agents or need a human** (J4 AGENT, L652 a): quotas and owner approval do not stop one party running many accounts, each with its own approved agent. On a flow that hands out scarce goods or rewards automation per account (limited stock, referral credit), completing the flow requires a human step in the application's own page, or agent credentials are refused there, whatever their identity; the list of such flows is recorded per project.
  - **Problem details for every error** (P5, L656): stable `type`, status, detail and extensions; tool execution errors say what to change in the call.
  - **Agent-shaped responses** (P6, L657): paginated and filtered by default, size-capped, high-signal fields; readable labels beside opaque handles; every handle checked for ownership on the server.
- **Rejected**: P1, P2 or P3 alone: each leaves one of the failure cases L651 names; P1 alone wins never where agents act for users.
- **Realizes**: J4 INTERACTION.AGENT decision 7; ALLOCATION.GUARD.6 (proposed: rate-limited retries carry idempotency keys).
- **Hand-offs**: limiter storage and enforcement (PIG-WEB.LOGIC.SECURE.6); error format of the HTTP interface (PIG-WEB.LOGIC.EXPOSE.2).
- **State**: `known | unvalidated: L651 inferred; the nested partition is a synthesis | open: the list of scarce-goods flows, recorded per project`.

## PIG-WEB.INTERACTION.ENVIRONMENT Browser Environment

- **Decides**: how browser capability, page lifecycle, offline use and locale are handled.
- **Rows**: none (roll-up).
- **Decision**: roll-up of .1 (judged): feature detection, never user-agent sniffing; pages stay eligible for the back/forward cache; unsaved input saved on page hide. Offline and installable use (.2) and internationalization (.3) are deferred: recorded, not judged; their requires-links stand (RECORD.1, PRESENT.2).
- **Realizes**: refines INTERACTION.ENVIRONMENT (J4).
- **State**: `known | open: .2 and .3 deferred`.

## PIG-WEB.INTERACTION.ENVIRONMENT.1 Capability and Page Lifecycle

- **Decides**: how pages detect features and survive back-forward restore, freezing and discard.
- **Rows**: L287, L293, L294. Cited: L007 (J4), L416, L414.
- **Positions**: P1 feature detection; no behaviour or cache key varied on User-Agent (L287, consensus); P2 browser sniffing (rejected in L287). P3 no `no-store` on non-sensitive pages and no `unload` handlers, so pages stay eligible for the back/forward cache (L293); P4 `no-store` everywhere for freshness (rejected in L293). P5 unsaved state persisted on `visibilitychange` or `pagehide` (L294); P6 on `unload` (rejected in L294).
- **Forces**: P1 serves every browser the user may have; P3 serves instant back navigation; P5 serves the user's input when the browser freezes or discards the page. P4 serves freshness and, for sensitive pages, confidentiality on shared devices.
- **Decision**: P1, P3, P5.
  - Enhancement checks features and degrades without them; nothing varies on User-Agent (L287).
  - No `unload` handlers anywhere; `no-store` only on pages showing sensitive data (L293; authenticated personalised pages are `private` and revalidated, L416).
  - On `pageshow` from the back/forward cache, the page refreshes time-sensitive state, and re-checks the session so a page restored after logout does not stay usable (L007; the session re-check inferred).
  - Unsaved input is saved on `visibilitychange` or `pagehide`, never `unload` (L294), and restored on return (EDIT).
- **Rejected**: P2: wins never (L287). P4: acceptable for pages that display sensitive data (L293). P6: wins never (L294).
- **Realizes**: J4 INTERACTION.ENVIRONMENT.1 and .2; ALLOCATION.PRESENT.3 (proposed: in-progress state in the browser).
- **Hand-offs**: cache headers (PIG-WEB.LOGIC.EXPOSE.4).
- **State**: `known | unvalidated: session re-check on restore inferred; L294 partly single-vendor T3 (SRC-269)`.

## PIG-WEB.INTERACTION.ENVIRONMENT.2 Offline and Installable Apps [deferred]

- **Decides**: how the application works offline or installed (scope out, recorded only).
- **Not judged** (deferred by the judge plan). Recorded link: requires ALLOCATION.RECORD.1 (offline use with user-owned data is the condition that moves the system of record to a client replica).

## PIG-WEB.INTERACTION.ENVIRONMENT.3 Internationalization [deferred]

- **Decides**: how the interface is translated and adapted to locales (scope out, recorded only).
- **Not judged** (deferred by the judge plan). Recorded link: requires ALLOCATION.PRESENT.2 (the rendering tier formats; storage stays canonical).
