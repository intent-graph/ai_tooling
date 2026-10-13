# J4 web-app-philosophy INTERACTION: judge records

One judge record per INTERACTION node of `web-app-philosophy` (12 nodes), under the max rule of `../../target_hierarchy.md`: per node, the most demanding practice that best serves the user's ability to work with the data, human or agent; weaker practices stay only as "acceptable when <condition>"; `undecided` only for a genuine trade-off between forces the node itself serves. Evidence is the ledger (`../../02_skeleton/claims_ledger.md`, ids `Lnnn`); source ids resolve through `../../02_skeleton/sources.md`. The maintainer's decisions (`../../maintainer_decisions.md`, MD-01 to MD-03) override on their points. The J1 placements (`../J1_allocation/allocation_matrix.md`, `../J1_allocation/records.md`) are settled: these nodes realize them and never re-decide allocation. Default context: J1's, restated by MD-03 (a classic website, one team, JavaScript + Python + Postgres, single tenant, humans and agents as users, a database shared by several backends, BI, consoles and scripts; browsers and agents never connect to the database).

Pinned:
- Nodes judged: 12 of 12 (2 roll-ups: INTERACTION, INTERACTION.ENVIRONMENT; 10 with owned rows; 28 rows read in full).
- Decided: 12; undecided nodes: 0. One inherited clause, `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (INTERACTION.COLLABORATE, from ALLOCATION.GUARD.3). Recorded default: each backend filters these reads from one shared written specification that lists every secondary surface, with a shared denial-test suite every backend runs; database read functions that receive the verified actor stay acceptable when a per-user read rule must hold for two or more backends. Consequence: roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted; COLLABORATE requires that restriction for comment content.
- Questions: 0 new (questions.md: none); the inherited read-visibility question stays with the allocation judge's open question, awaiting maintainer. The automated-traffic row (L652) is resolved per flow by a condition, not dissolved: on flows that hand out scarce goods or reward automation per account, completing the flow requires a human, or agents are excluded, whatever their identity.
- Verdicts against the maintainer doctrine: 0 (the unit owns no MAINT row; no verdict contradicts a MAINT row it cites). L517's "deployed together" departure is counted at the function-API node of the Postgres data tier, cited here only.
- Conflicts with J1 placements: 0.
- Review fixes: 6 findings of the INTERACTION review reach this unit (M1, M2, M3, M4, m1, m2), all applied, none rejected; cross-branch resolutions X1, X2, X6, X7 applied.
- Gaps in the evidence: 5. (1) INTERACTION.VISUALIZE rests on one weak row (L005): the conformance level is not grounded here (L300: "AA as the usual default is not stated"), handed to the pig-web interaction judge. (2) L682's "monotonic cursor (sequence id)" is contradicted by L594 (a sequence id does not follow commit order): the cursor is decided as one no later commit can fall behind, realization handed to PIG-WEB.DATA.CONCURRENCY.5. (3) L014's fallacies list was read only through a T4 copy. (4) L648 applied to agents the application runs or serves is inferred. (5) L687's list of leak surfaces is a synthesis.

## How to read

- **Decides**: the node's question, from the skeleton's node table.
- **Rows**: owned rows (read in full); rows owned elsewhere that the record cites are named in the text.
- **Positions**: P1.. competing practices from the evidence, with ledger ids. A position present only as the practice a row rejects is marked "(rejected in Lnnn)".
- **Forces**: what each position serves, at what cost.
- **Decision**: the max choice and its grounds. Inferred parts are marked.
- **Rejected**: each other position, why, and the condition under which it wins.
- **Realizes**: the intentlinks to J1 placements (and other nodes) and what this node carries out for each.
- **Hand-offs**: points the pig-web judges realize or decide.
- **State**: proposed `epistemic_state`: `known` = grounded verdict; `| unvalidated: X` = an inferred part X; `| open: X` = a named part not decided here; `| gap: X` = missing evidence.

## INTERACTION Interaction

- **Decides**: how users, human or agent, see, edit and discuss the data through clients the team does not control.
- **Rows**: none (roll-up).
- **Decision**: roll-up of the four children. The interaction tier lets humans and agents work with the data through clients the team does not control, and decides nothing durable (RULES.3, L019): it holds copies for feedback and latency, and every decision reaches a backend.
  - **Visualize**: server-rendered HTML that works for everyone, people with disabilities included, enhanced where the browser supports it; values formatted for the reader by the tier that renders them (VISUALIZE).
  - **Collaborate**: pages correct on plain load, push as a hint, conflicts and visibility per the allocation placements; comments are entities with their own abilities and never more visible than their target on any surface the application serves; roles that may SELECT the base tables see what their grants allow, so their comment grants are restricted (COLLABORATE).
  - **Agent access**: agents are users through an adapter on the same core, with audience-bound tokens, narrow scopes, few purpose-specific tools, quotas, server-side audit, and no decision of their own (AGENT).
  - **Environment**: seven properties are accepted as given and designed for: unknown runtime, unstable page lifecycle, version skew, unrecallable caches, unreliable network, public URLs, hostile page script (ENVIRONMENT).
- **Realizes**: through its children, ALLOCATION.PRESENT.1 to .3, GUARD.3, GUARD.5, GUARD.6, ACT.4, RULES.3, RULES.4, DERIVE.3.
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from ALLOCATION.GUARD.3, through COLLABORATE)`.

## INTERACTION.VISUALIZE Perceivable Interface

- **Decides**: how the interface stays usable by everyone, people with disabilities included.
- **Rows**: L005 (grounded, weak; SRC-165, T1). Cited: L003, L300, L301 (pig-web), L632 (via PRESENT.2).
- **Positions**: P1 accessibility as a requirement from the start, with users involved early (L005); P2 accessibility added at the end, as an audit and retrofit (rejected in L005).
- **Forces**: P1 serves the node's purpose (everyone can perceive and operate the interface) at the cost of design effort from the first page; P2 defers that cost and pays more later, with parts that never conform (inferred from L300: conformance is judged per full page, embedded third-party content included).
- **Decision**: P1, as the max for the node's purpose.
  - Accessibility is a project requirement from the first design: a conformance target is stated before building and judged per full page, embedded third-party content included (L005, L300).
  - The interface starts from native HTML semantics and keyboard operation; ARIA only where native elements cannot express the control (L301). This follows from the rendering placement: server-rendered HTML with enhancement (PRESENT.1, L003) carries native semantics by default.
  - Values are shown in the reader's locale and time zone by the tier that renders the text; nothing pre-formatted comes from storage (PRESENT.2, L632).
  - Users with disabilities take part in early testing, not only at acceptance (L005).
- **Rejected**: P2: wins never. A retrofit is acceptable only for a page that already exists and is brought to the stated target, never as the plan for new pages.
- **Realizes**: ALLOCATION.PRESENT.1 (renders what the backend renders, enhanced in the browser; islands only under L253's criteria); ALLOCATION.PRESENT.2 (formats for the reader where the rendering happens).
- **Hand-offs**: the conformance level (A, AA or AAA) belongs to PIG-WEB.INTERACTION.VISUALIZE.4, which owns L300; the evidence does not state AA as the default, so that choice needs a read source or stays open there.
- **State**: `known | unvalidated: one weak T1 row (L005); the native-first consequence of PRESENT.1 is inferred | gap: conformance level not grounded (L300)`.

## INTERACTION.COLLABORATE Collaboration on Data

- **Decides**: how several users discuss and change the same data and learn of each other's changes.
- **Rows**: L006, L435, L664, L682, L686, L687. Cited: L594 (pig-web data), L671, L674, L677, L679, L681, L683, L659.
- **Positions**:
  - Freshness: P1 delivered events are the client's state (rejected in L682), or a client replica with a sync engine (L302, L677); P2 push is a hint over a correct pull: every page correct on plain load, catch-up after any gap by fetching changes since a server-issued cursor (L682, L006).
  - Channel: P3 the simplest channel that meets the direction of flow, the update frequency and the tolerable latency: polling, then long polling or server-sent events, then a two-way channel (L435); P4 one two-way channel for everything (the WebSocket-first side of L436, owned by pig-web).
  - Comment model: P5 each comment its own entity with a mandatory target, its own author, lifecycle and permissions (L664); P6 comments embedded as columns or JSON in the annotated record (rejected in L664).
  - Abilities: P7 read, comment, edit, resolve and moderate as separate abilities, deny by default, checked per object on every request, streams and exports included (L686); P8 the comment right implied by the edit right, or the reverse (rejected in L686).
  - Visibility: P9 a comment never more visible than its target, optionally narrower (internal note versus shared reply), the same filter on every secondary surface: counts, notifications, search results, history, ETags, real-time channels (L687); P10 the filter on the main list only (the leak L687 warns against).
- **Forces**: P2 serves correctness under dropped connections and several tabs, at the cost of a catch-up endpoint; P1 serves latency and offline use, at the cost of every replica becoming an authority (L302). P3 serves simplicity and operability; P4 serves one code path and two-way traffic, at the cost of long-lived connection servers. P5 and P7 serve confidentiality and least privilege (comments are edited, hidden or deleted without touching the data; reviewers and customers may comment without editing), at the cost of one more entity and more checks. P9 serves confidentiality; P10 serves only simplicity.
- **Decision**:
  1. **Push is a hint over a correct pull** (P2; L682, L006). Every page is correct on plain load. A client that missed anything catches up by asking for the changes since the cursor the server last gave it; it never trusts the events it happened to receive. **The cursor is one no later commit can fall behind.** L682's "(sequence id)" is rejected as stated: a sequence id does not follow commit order, so a reader polling with "id greater than last seen" can skip a row forever (L594). Realization: PIG-WEB.DATA.CONCURRENCY.5.
  2. **The simplest channel that meets the need** (P3; L435): polling first; server-to-client push (long polling or server-sent events) when staleness of a poll interval is not tolerable; a two-way channel only for two-way traffic at high frequency. Correctness never depends on the channel (decision 1).
  3. **Concurrent edits surface the concurrency placement's policy** (GUARD.5): the browser keeps the version it read; a stale write is rejected and the user sees the other change and reapplies, never a silent overwrite of the whole record (L674); per-property last-writer-wins only for toggles, status, assignment and ordering (L674); a text engine only for genuinely collaborative long-text fields (L679, L677). The browser and agent clients never resolve a conflict on their own.
  4. **Presence is ephemeral** (PRESENT.3; L681): broadcast through a channel with a timeout, never written to tables; a persisted "last seen" is a separate, coarse field.
  5. **Comments are their own entities** (P5; L664): mandatory target reference, own author, lifecycle and permissions; append-only rows that need no merge (L679).
  6. **Separate abilities, checked on every surface** (P7; L686): read, comment, edit, resolve and moderate are distinct; deny by default; checked per object on every request, streams and exports included. Where each check lives follows GUARD.3 as settled: a rule decidable from the stored row and the actor ("an author may edit their own comment", "the target's author may resolve its threads", L671) is decided by the writer function (a resolve right for the thread's opener has no source and is not stated, review m2); the product roles that grant abilities (reviewer, customer, moderator) are each backend's product policy; the browser hides controls the user may not use, cosmetically.
  7. **A comment is never more visible than its target** (P9; L687), may have a narrower audience, and the same filter applies on every surface the application serves: counts, notifications, search results, history, exports, ETags and real-time channels (L686, L687). Notifications are created only for recipients who may see the target (L683, pig-web).
     - **Who applies the per-user read filter** when several backends read the same comments: `undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database` (ALLOCATION.GUARD.3). Recorded default (MD-01 as written): each backend filters these reads from one shared written specification of each visibility rule that lists every secondary surface above, with a shared denial-test suite every backend runs. J1's fallback stays acceptable: database read functions that receive the verified actor, when a per-user read rule must hold for two or more backends. This node does not settle it.
     - **Consequence of the default** (X1): roles that may SELECT the base tables (reporting, operator) see every row, comments included, unless their own role is restricted. The guarantee above covers the surfaces the application serves; it claims nothing stronger for those roles.
     - **Restriction required for comments until the question is answered** (review M1; inferred from the confidentiality purpose of P9 and from the reporting role's column grants excluding personal data by default, J5 TRANSVERSE.SECURITY): reporting and operator roles get no SELECT on comment content or on comments whose audience is narrower than their target; they read comments only through a projection limited to target-wide audiences, or not at all. Where a project does not apply this restriction, the leak to those roles is a known limit of the default, stated where comments are documented. The maintainer's read-visibility question should name comments as a consequence of its "each backend filters" position (hand-off to the allocation judge).
  8. **Agents collaborate under the same rules**: their writes are marked as agent-originated (L659, pig-web) and pass the same abilities and visibility filters.
- **Rejected**:
  - P1, delivered events as state: wins never. A client replica with a sync engine wins under the system-of-record placement's condition (offline use with user-owned data, RECORD.1), and even then catch-up uses a cursor.
  - P4 as the default: wins when traffic is two-way at high frequency (L435); the choice of push channel among server-sent events and WebSocket is the pig-web channel node's (L436).
  - P6: wins never for comments (they nearly always have other readers or writers than the record, L664). A single free-text note edited by exactly the people who edit the record is a field, not a comment (inferred).
  - P8: wins never (L686).
  - P10: wins never (L687).
- **Realizes**: ALLOCATION.GUARD.5 (shows conflicts with the policy the placement chose; holds only the version it read); ALLOCATION.PRESENT.3 (presence on a channel with timeout, drafts in the browser, durable comments in the database); requires ALLOCATION.GUARD.3 (abilities and visibility follow the authorization placement, its open read clause included).
- **Hand-offs**: commit-ordered change cursor (PIG-WEB.DATA.CONCURRENCY.5, L594); push channel default (PIG-WEB.INTERACTION.REALTIME.1, L436); anchoring, threads, moderation and notification rows (PIG-WEB.INTERACTION.COLLABORATE.1 to .4); comment grants of reporting and operator roles (PIG-WEB.DATA.GUARD.2); comments as a named consequence of the read-visibility question's default (ALLOCATION.GUARD.3).
- **State**: `known | undecided: awaiting maintainer, read visibility of rows with per-user rules when several backends share the database (inherited from ALLOCATION.GUARD.3; recorded default: each backend filters from one shared written specification with a shared denial-test suite; reporting and operator comment grants restricted) | unvalidated: leak-surface list (L687, synthesis); channel order from one T3 source (L435); the comment-grant restriction for reporting and operator roles (inferred) | conflict: L682's sequence-id cursor against L594, resolved for L594`.

## INTERACTION.AGENT Agent Access

- **Decides**: how agents act as users with bounded authority, verifiable identity and limited consumption.
- **Rows**: L640, L642, L645, L648, L652. Cited: L633, L644, L650, L646, L651, L658, L659, L034.
- **Positions**:
  - Tokens: P1 the server accepts only tokens issued for it and obtains its own token for downstream calls (L640); P2 forwarding the client's token downstream (rejected in L640).
  - Scopes: P3 narrowest scopes, read first, elevation on demand through precise challenges, no wildcard or omnibus scopes, each request still authorized in server code (L642); P4 coarser scopes (acceptable in L642 for trusted first-party agents).
  - Tools: P5 few, purpose-specific tools, each with only the permissions it needs (L645); P6 open-ended tools: raw shell, raw SQL, arbitrary URL fetch (acceptable in L645 only inside a sandbox, SRC-398).
  - Session capabilities: P7 never one agent session with untrusted input, access to private data and the power to change state or communicate externally; if all three are needed, supervision or a split session (L648); P8 rely on filtering the input (L649, pig-web: filters as an additional layer only).
  - Automated traffic: P9 deny non-human patterns on sensitive flows (L652 a, L034); P10 admit automated clients that identify and authenticate themselves, limited by quota (L652 b); P11 blanket bot blocking (rejected in L652).
- **Forces**: P1, P3, P5, P7 serve security and audit clarity (bounded authority), at the cost of consent friction, step-up round trips and fewer things an agent can do in one call. P4 and P6 serve the agent's capability and fewer round trips, at the cost of blast radius. P9 serves business integrity on flows whose automation harms the business; P10 serves agents as intended users; the ledger row states this trade-off itself ("serves business integrity against agent access", L652), and each side wins under its own condition. P11 serves neither once agents are users.
- **Decision**: the agent is one more user with bounded authority, served through an adapter on the same core.
  1. **One core** (RULES.4, L633): the agent surface is an adapter to a backend that only translates and shapes; rules, validation, authorization and state transitions never live in the adapter or in prompts. Agents never connect to the database (J1 access paths).
  2. **Agents never decide access** (GUARD.3; L644, L650): model output and client-supplied hints (tool annotations, claimed identity, client name) are untrusted input; the backend and the writer functions decide as the authorization placement says.
  3. **Audience-bound tokens, no passthrough** (P1; L640): the server accepts only tokens issued for it and never forwards a caller's token; downstream calls use its own token (exchange or its own grant). Each agent holds its own short-lived, revocable credential (GUARD.4).
  4. **Narrowest scopes** (P3; L642): read scopes first; elevation on demand through a precise insufficient-scope challenge; no wildcard or omnibus scope; every request still authorized in server code.
  5. **Minimum capabilities** (P5; L645): few, purpose-specific tools, each with only the permissions it needs; no raw shell, raw SQL or arbitrary fetch on the live system.
  6. **No lethal combination in one session** (P7; L648). Where the application runs or hosts an agent, no session holds untrusted input, private data and the power to change state or send outward together; if all three are needed, a supervised step or a split session. For agents the team does not run, the application's share is its tool shape: no tool sends data to an arbitrary destination (decision 5), and consequential or external effects go through the approval design of the pig-web approval node (L646) (application to external agents inferred).
  7. **Identify, then limit; protect harmful flows by name** (P10 with P9; L652, L034). Agents that identify and authenticate themselves are admitted to every flow their scopes allow and limited by quota per agent identity, so one runaway agent cannot exhaust its user's allowance (partition: L651, pig-web). The flows whose automation harms the business (purchase, sign-up, booking, referral) are named and protected specifically: per-flow limits for identified agents, approval by the owning user for irreversible effects, and anonymous automation denied or challenged there. On a flow that hands out scarce goods or rewards automation per account (limited stock, referral credit), per-agent quotas and owner approval do not stop one party running many accounts, each with its own approved agent (L652 a, L034): there, completing the flow requires a human, or agents are excluded from it, whatever their identity. The list of such flows is a decision recorded per project.
  8. **Duplicate-safe** (GUARD.6): every mutation offered to agents that is not idempotent by design takes an idempotency key, recorded with the effect.
  9. **Accountable** (ACT.4; L658): every agent action is logged on the server with acting identity, delegating subject, operation, correlation id and outcome, never only in a model transcript; the backend asserts the user and the agent as the actor (R1-3 of the allocation records), and agent-originated writes are marked in the data (L659).
- **Rejected**:
  - P2: wins never (L640).
  - P4: acceptable when the agent is first-party (built and run by the team) and every request is still authorized in server code (L642).
  - P6: acceptable only inside a sandbox that holds no authority and no connection to the system of record (L645, SRC-398; RECORD.2 forbids agent connections to the database).
  - P8 as the only control: wins never (L649); filters stay an additional layer.
  - P9 as the default for all automated traffic: rejected, since agents are intended users in the default context. P9 wins on the named harmful flows for anonymous automation, and it wins outright on a flow that hands out scarce goods or rewards automation per account (limited stock, referral credit): there, completing the flow requires a human, or agents are excluded from it, whatever their identity (L652 a: "wins for scarce-inventory or abuse-prone flows"). The contest is resolved per flow by this condition, not dissolved.
  - P11: wins never where agents are intended users (L652).
- **Realizes**: requires ALLOCATION.RULES.4 (one more adapter on the same core); ALLOCATION.GUARD.3 (agents never decide access); ALLOCATION.GUARD.6 (agent retries absorbed by keys recorded with the effect); ALLOCATION.ACT.4 (agent actions recorded where history is written, both session role and claimed actor).
- **Hand-offs**: protocol and transport (PIG-WEB.INTERACTION.AGENT.1), discovery (.2), identity, delegation and agent-write marking (.3), approval designs and injection containment (.4, L646, L649), rate-limit partition and agent-shaped errors (.5, L651, L656, L657).
- **State**: `known | unvalidated: L648 applied to agents the application runs or serves (inferred); the identify-then-limit synthesis of L652 (inferred) | open: the list of scarce-goods flows where agents are excluded or a human must complete the flow, recorded per project`.

## INTERACTION.ENVIRONMENT Web Environment

- **Decides**: which properties of browsers, networks, caches and URLs the design must accept as given.
- **Rows**: none (roll-up).
- **Decision**: roll-up. Seven properties are accepted as given, each with the design response that keeps the user able to work with the data:
  - the runtime is unknown: core content and function as HTML, enhanced in layers (.1);
  - pages are restored, frozen, discarded and opened in several tabs: the server stays the arbiter, the page refreshes and saves on lifecycle events (.2);
  - deployment is not atomic: every client-server contract, the agent tool surface included, has an explicit compatibility window; a breaking change goes expand, migrate, contract (.3);
  - stored responses cannot be recalled: cacheability is declared per URL, long lifetimes only for immutable URLs (.4);
  - the network fails: the client degrades gracefully and retries only what is safe (.5);
  - URLs are public and long-lived: stable, implementation-free, carrying navigable state, never a session token, bearer token or long-lived credential; short-lived, single-purpose signed URLs for file delivery are the one exception (.6);
  - page script may be hostile: no credential readable by script, escaping first, CSP second, CSRF independent of CORS, uploads on another site (.7).
- **State**: `known`.

## INTERACTION.ENVIRONMENT.1 Uncontrolled Client Runtime

- **Decides**: how the design copes with browsers of unknown capability, speed and script completion.
- **Rows**: L002, L003, L004. Cited: L253, L016.
- **Positions**: P1 design for a range of support: core content and function delivered as HTML that works without the latest capabilities, enhanced with CSS and JavaScript where supported, layers loosely coupled (L002, L003), no feature that works in one browser, OS or device class only (L004); P2 one target runtime, core function requiring script (the client-rendered application, L253, as the default product shape).
- **Forces**: P1 serves everyone's ability to reach the data (everybody is a non-JavaScript user until the script has loaded, L003) and interaction latency through a small script budget (L016), at the cost of building the HTML path first; P2 serves rich interaction and one code path, at the cost of a blank or broken page whenever script is late, blocked or failing.
- **Decision**: P1 (L002, L003, L004; consensus, T1 and T2). The core read and write paths work as HTML forms and links; enhancement is added by feature detection and fails without taking the core down. Client-rendered islands, where the rendering placement admits them (L253's criteria), sit inside a page whose surrounding content and navigation still work as HTML (inferred from PRESENT.1).
- **Rejected**: P2 as the default: wins only where most of the product meets L253's criteria (PRESENT.1's condition); even then no feature is limited to one browser, OS or device class (L004).
- **Realizes**: ALLOCATION.PRESENT.1 (the HTML-first rendering the placement gives the backend, enhanced in the browser).
- **Hand-offs**: feature detection and lifecycle mechanics (PIG-WEB.INTERACTION.ENVIRONMENT.1); rendering technique per page (PIG-WEB.INTERACTION.VISUALIZE.1).
- **State**: `known`.

## INTERACTION.ENVIRONMENT.2 Unstable Page Lifecycle

- **Decides**: how state and side effects survive pages that are restored, frozen, discarded or open in several tabs.
- **Rows**: L007, L008. Cited: L293, L294 (pig-web), GUARD.5, GUARD.6.
- **Positions**: P1 back/forward is part of the interface: pages stay eligible for restore and refresh time-sensitive or sensitive state when restored from memory (L007, L293); P2 opt pages out of restore (no-store, unload handlers) to avoid stale views (rejected in L293 for non-sensitive pages). Several tabs: P3 coordinate shared work in the client (Web Locks; BroadcastChannel unverified) (L008); P4 the server as the arbiter of concurrent and repeated work, whatever the number of tabs (GUARD.5, GUARD.6).
- **Forces**: P1 serves instant navigation and correct displayed state; P2 serves freshness at the cost of every back navigation reloading. P3 serves less duplicate work and consistent display across tabs; P4 serves correctness, since two tabs are two concurrent clients the client cannot fully coordinate (a tab may be frozen or discarded).
- **Decision**: P1 with P4 as the ground and P3 as a copy.
  - Pages stay eligible for back/forward restore; on restore from memory they refresh time-sensitive or sensitive state (L007).
  - Unsaved input is persisted when the page is hidden, never on unload, since the browser may freeze or discard it without notice (L294).
  - Two tabs editing the same data are two concurrent writers: the version check of GUARD.5 rejects the stale one; background work repeated by several tabs is absorbed by the keys of GUARD.6. Client-side coordination between tabs reduces duplicate work and stale displays; correctness never depends on it (inferred from authority and copies, RULES.1).
- **Rejected**: P2: acceptable for pages that display sensitive data (no-store) (L293); never as a general freshness fix. P3 as the guard: wins never; kept as an optimization.
- **Realizes**: ALLOCATION.PRESENT.3 (in-progress state in the browser, durable state in the database), ALLOCATION.GUARD.5 and .6 (the server arbitrates across tabs) (links inferred; the skeleton draws none).
- **Hand-offs**: lifecycle events and cache headers (PIG-WEB.INTERACTION.ENVIRONMENT.1).
- **State**: `known | unvalidated: several-tab design as a general principle (L008); server arbitration across tabs inferred from GUARD.5, GUARD.6`.

## INTERACTION.ENVIRONMENT.3 Non-Atomic Deployment

- **Decides**: how client and server changes coexist while old pages run against a new server.
- **Rows**: L009. Cited: L047, L056, L057, L058 (TRANSVERSE.CONTRACTS, J5 verdict), L277 (pig-web logic), L517 (MAINT, through J5 and the cross-branch resolution on "deployed together"), MD-02.
- **Positions**: P1 every client-server contract has a compatibility window: compatible additions, tolerant readers, no removal while in use (L009, L056, L057, L058); P2 assume client and server deploy together (rejected in L009). Mechanisms for incompatible change, owned by pig-web (L277, contested): explicit versioned paths, or routing each client to the server version that served its code.
- **Forces**: P1 serves every user whose tab holds old code (tabs keep old code for days, L009), at the cost of carrying old shapes for the window; P2 serves simplicity and breaks those users at each deploy.
- **Decision**: P1 (consensus, T1 to T3).
  - The compatibility window is explicit and at least as long as an old page can stay open (days, L009); within it, changes are additive and readers ignore what they do not know (L056, L057).
  - Before removing or changing a behaviour, its current use is found (L058).
  - Every surface used by code the team does not redeploy at once is a contract under this window: JSON endpoints, HTML form fields and URLs posted by old pages, the agent tools and their schemas (inferred extension; agents run code the team never deploys).
  - Every interface description consumers read is always in sync with the implementation by process (MD-02, extended to every agent-facing interface): the HTTP description, the database function API catalogue, and the agent tool surface (for example an MCP server's tool list and schemas). The compatibility window applies to each of them.
  - **A breaking change goes expand, migrate, contract** (L047; TRANSVERSE.CONTRACTS as judged): the new shape is added beside the old, each consumer moves, and the old one is removed once no consumer uses it; usage is known per consumer role (L058). A versioned path and routing each client to the server that served its code are the mechanisms that move old tabs during the migrate phase (L277; the mechanism is the pig-web choice). No client is silently broken.
- **Rejected**: P2: wins never on the web (L009). "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration; a browser tab never does, so for client-server contracts this condition does not hold (the departure from L517 is counted at the function-API node of the Postgres data tier, cited here).
- **Realizes**: requires TRANSVERSE.CONTRACTS (compatible contract evolution: expand, migrate, contract for every contract, lockstep rejected for browser clients); this record is aligned with that verdict.
- **Hand-offs**: skew policy mechanism (PIG-WEB.LOGIC.EXPOSE.7, L277); keeping the previous release's fingerprinted assets served during the window (PIG-WEB.TRANSVERSE.TOPOLOGY.4; not in the rows read, inferred); one origin and a drift gate for the agent tool surface (PIG-WEB.INTERACTION.AGENT.1, PIG-WEB.TRANSVERSE.CONTRACTS.1).
- **State**: `known | unvalidated: extension to form fields and agent tools inferred`.

## INTERACTION.ENVIRONMENT.4 Caches Beyond Reach

- **Decides**: how responses stored by caches the team cannot purge are anticipated.
- **Rows**: L010, L011. Cited: L414, L415, L416 (pig-web logic), DERIVE.3.
- **Positions**: P1 declare cacheability per URL in advance and set lifetimes by how stale a copy may be, since a stored response cannot be recalled: short or no-cache for URLs whose content changes in place (L010); P2 long lifetimes with purging on change (the practice L010 rules out for intermediaries); P3 avoid intermediaries; L011 states their price (latency, stale data) against their benefit (bounded complexity).
- **Forces**: P1 serves correctness of what the user sees, at the cost of revalidation requests; P2 serves latency and load, and leaves stale copies wherever purge does not reach; P3 serves freshness at the cost of latency and scale.
- **Decision**: P1. Every response is labelled on purpose (L414); long lifetimes only for immutable, fingerprinted URLs; HTML and other in-place content with no-cache and validators (L415); personalised responses private or no-store (L416). Every intermediary is accepted for what it bounds, with its staleness and added latency counted (L011).
- **Rejected**: P2: acceptable when the cache is one the team owns and can purge (its own CDN) and the lifetime given to browsers and other intermediaries stays short (inferred). P3: wins never as a rule; intermediaries are kept on purpose (L011).
- **Realizes**: constrains ALLOCATION.DERIVE.3 (copies in caches the team does not own cannot be recalled, so their staleness bound is set when the response is sent).
- **Hand-offs**: header practice (PIG-WEB.LOGIC.EXPOSE.4); static assets and CDN (PIG-WEB.TRANSVERSE.TOPOLOGY.4).
- **State**: `known | unvalidated: the owned-CDN condition for P2`.

## INTERACTION.ENVIRONMENT.5 Unreliable Network

- **Decides**: how the client keeps core function when requests or scripts fail.
- **Rows**: L014 (resilience T1/T2 grounded; fallacies list via a T4 copy). Cited: L003, L294, GUARD.6.
- **Positions**: P1 assume the network unreliable, slow, limited and heterogeneous; fail gracefully and keep core function when requests or scripts fail (L014); P2 assume success (rejected in L014). No other position was found.
- **Forces**: P1 serves the user's ability to keep working and not lose input, at the cost of handling pending, failed and repeated requests; P2 serves only simplicity.
- **Decision**: P1. Any request may fail, time out, arrive late or twice.
  - The core paths work as plain HTML requests (ENVIRONMENT.1), so a failed script does not remove them (L003).
  - The client shows pending and failed states and keeps the user's input across a failure (inferred from L014 with L294).
  - The client retries only what is idempotent or carries an idempotency key (GUARD.6); real-time channels reconnect and catch up by cursor (COLLABORATE).
- **Rejected**: P2: wins never.
- **Realizes**: ALLOCATION.GUARD.6 (safe retries depend on the duplicate-suppression placement) (link inferred; the skeleton draws none).
- **State**: `known | unvalidated: fallacies list read through a T4 copy (L014); input kept across failure inferred`.

## INTERACTION.ENVIRONMENT.6 URL as Public Interface

- **Decides**: how URLs serve as stable public addresses and as the contract for navigable state.
- **Rows**: L017, L018. Cited: L292 (pig-web), L422 (pig-web logic), L459 (pig-web), PRESENT.3.
- **Positions**: P1 URLs are the public, long-lived interface: stable, free of author, status, file extension and implementation details, the mapping from URL to resource owned over time (L017); P2 the URL as the contract for state and between independently built parts of a page (L018, one T2 source); P3 view state held only in client memory (the alternative L292 rules out for navigable state).
- **Forces**: P1 serves everyone who links, bookmarks or cites the data, humans and agents, at the cost of maintaining the mapping; P2 serves shareable, restorable state and loose coupling between page parts; P3 serves simplicity of client code and breaks back, reload and sharing.
- **Decision**: P1 and P2.
  - URLs are stable and implementation-free; when a resource moves, its old URL keeps resolving to it (owning the mapping, L017; redirect inferred).
  - View state that users navigate, bookmark or share lives in the URL (L018, L292; PRESENT.3's URL kind).
  - Because URLs are public and are logged, **no session token, bearer token or long-lived credential ever travels in a URL** (generalized from L459, inferred).
  - **The one allowed exception**: short-lived, single-purpose, scope-limited signed URLs for file delivery, with their lifetime and scope stated (L422: a presigned URL is a bearer token, so it is bounded like one). Such a URL is acceptable when all of these hold: it is issued only after an authorization check of the requester; it grants one operation on one object; it expires quickly; it is served from another origin than the application; the response that issues it is `no-store` and the page's referrer policy does not leak it (conditions inferred).
  - One-time OAuth authorization codes in redirects, bound to the client by PKCE, are none of the forbidden kinds (single-use, short-lived, useless without the client's verifier) and are acceptable under the identity placement (inferred).
- **Rejected**: P3: acceptable for ephemeral view state that nobody navigates to or shares (PRESENT.3). P2's second half (the URL as the channel between independently built page parts) is acceptable when independently built parts share a page; in the default context (one team, server-rendered) it reduces to the navigable-state rule. Any credential in a URL beyond the exception above: wins never.
- **Realizes**: ALLOCATION.PRESENT.3 (the URL as the authority for shareable view state) (link inferred; the skeleton draws none).
- **Hand-offs**: History API routing and fragment use (PIG-WEB.INTERACTION.VISUALIZE.2, L292); signed file-delivery URLs (PIG-WEB.LOGIC.PROCESS.4, .6, L422); authorization-code flow (PIG-WEB.LOGIC.SECURE.4, PIG-WEB.INTERACTION.AGENT.2).
- **State**: `known | unvalidated: URL as contract between page parts rests on one T2 source (L018); no-credentials-in-URLs generalized from L459; the conditions on signed file URLs and the status of PKCE-bound authorization codes inferred`.

## INTERACTION.ENVIRONMENT.7 Hostile Page Script

- **Decides**: how the design limits what script running in the page with the application's privileges can do.
- **Rows**: L024, L025, L026, L027, L028. Cited: L019, L644, GUARD.4.
- **Positions**:
  - Credentials: P1 assume malicious script has the application's privileges, so no long-lived credential is readable by script (L024); P2 tokens in script-readable storage (acceptance rows L320, L321, rejected by GUARD.4).
  - XSS defence: P3 escaping by default in output encoding and templates first, CSP as a second layer (L026), XSS prevention as a precondition to CSRF defence (L025); P4 CSP as the primary defence (rejected in L026).
  - Cross-origin: P5 CORS only relaxes the read block and is not access control; CSRF defence is needed independently (L027); P6 CORS treated as access control (rejected in L027).
  - Uploads: P7 user-uploaded content from a distinct registrable domain (L028, majority); P8 a different host of the same site (the weaker T1 in L028).
- **Forces**: P1, P3, P5, P7 serve the integrity of the user's data and session against injected script, at the cost of cookie-based sessions, template discipline, CSRF tokens and a second domain; P2, P4, P6, P8 serve convenience and leave a successful injection with more reach.
- **Decision**: P1, P3, P5, P7.
  - No long-lived credential is readable by page script: the session is an opaque, HttpOnly, Secure, SameSite cookie (GUARD.4; L024).
  - Output is escaped by default by the templates; CSP is the second layer (L026). XSS prevention comes first, because XSS defeats every CSRF defence (L025).
  - CORS is not access control; CSRF defence stands on its own (L027).
  - User-uploaded content is served from a distinct registrable domain (L028), so the same-origin policy contains any script in an upload.
  - Content written by other users or by models (comments, agent output) is untrusted wherever it is rendered (L644, inferred for rendering).
  - Because any script on the page holds the application's privileges, no check that grants access or protects integrity runs there (RULES.3, L019).
- **Rejected**: P2: wins only when no backend is possible (GUARD.4's condition, L314). P4: wins never as the first layer. P6: wins never. P8: the weaker T1 states only "different host" and does not address cookie and same-site reach shared within one registrable domain (inferred); no condition under which it wins was found in the evidence.
- **Realizes**: constrains ALLOCATION.RULES.3 (the browser cannot hold deciding checks); ALLOCATION.GUARD.4 (credentials out of script reach) (second link inferred; the skeleton draws none).
- **Hand-offs**: CSP and security headers (PIG-WEB.TRANSVERSE.SECURITY.3); CSRF defence (PIG-WEB.LOGIC.SECURE.3); CORS (PIG-WEB.LOGIC.EXPOSE.5); upload serving (PIG-WEB.LOGIC.PROCESS.6).
- **State**: `known | unvalidated: rendering of model output as untrusted inferred from L644`.
