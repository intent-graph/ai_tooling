# Target hierarchy and selection rule (maintainer decisions)

Status: decided by the maintainer after the round-3 consolidation review. It supersedes the
partition of `01_consolidate/skeleton.md` (the evidence in `01_consolidate/claims_ledger.md`
stays valid and is re-attached to this tree).

## Why the first skeleton was rejected

- Its structure came from clustering the evidence; the guideline's job is to **filter and
  decide between competing intents**, not to mirror what sources discuss.
- Its selection rule was agreement among sources (consensus → known, contested → undecided),
  which yields the average of the web. The rule is now **max** (below).
- It left implicit the first decision of any web-app design: **who does what across the three
  tiers**.

## Functional hierarchy (maintainer's model)

**L0.** A web application lets users, human or agent, interact with data under business logic.

**L1, in this order:**

1. **ALLOCATION** — who does what across database, backend and browser. Decided first;
   it trades off performance, security, logical correctness, latency and more.
   - *forces*: correctness, security, performance (data locality, set-based work), latency
     (round trips, responsiveness), scalability (the database is the hardest tier to scale
     out), changeability (deploy cadence, testability, team skills).
   - *context*: the variables that move an allocation: number of database consumers, agent
     clients, offline needs, latency budget, team SQL skill (extend if the evidence shows more).
   - *rules*: authority versus copies (one tier is the authority for a responsibility; copies
     elsewhere serve latency or convenience and may be wrong without breaking correctness);
     the end-to-end argument; others the evidence supports.
   - *placements*: one node per responsibility, each stating its authority tier, permitted
     copies, forbidden tiers, the forces in tension, the max decision, rejected placements
     with reasons, and the context that would move it. Initial list: validation, invariants,
     authorization, business rules and state transitions, derived data and aggregation,
     filtering/sorting/paging/search, concurrency control, side effects and integrations,
     audit, formatting and localization, UI state, caching (extend if the evidence shows more).
2. **DATA** (database) — store, organize, maintain the data: how it carries out what it was
   allocated (organize, guard, maintain, derive).
3. **LOGIC** (backend) — secure, process, create and enforce business logic out of the data
   (secure, enforce, process, expose).
4. **INTERACTION** (browser, and the agent surface) — let users visualize, interact with,
   edit and comment on the data (visualize, edit, collaborate, agent access, environment).
5. **TRANSVERSE** — security, performance, standards and contracts, operability, evolution.

Tier branches hold realization only and link back to the placement nodes that assign them
work; they do not re-decide allocation. A contract sits with the role that offers it (the
database's function API under DATA, the backend's interface under LOGIC).

Both graphs share this L1 cut: `web-app-philosophy` holds the why (stack-neutral);
`pig-web-defaults` holds the JS + Python + Postgres choices under the same branches.

## Selection rule: max, not average

For every node, the guideline states **the most demanding practice that best serves the
purpose of the node's role**: integrity for DATA, enforcement and security for LOGIC, the
user's ability to work with the data for INTERACTION, the stated force for ALLOCATION
placements. Agreement among sources is evidence for the judgment, never the verdict.
Weaker practices stay only as "acceptable when <condition>". `undecided` is reserved for
genuine trade-offs, where maximizing one force costs another that the node also serves;
those go to the maintainer.

## Judge record (every node)

1. **Positions** — the competing practices, from the evidence (ledger ids, source ids).
2. **Forces** — which force or purpose each position serves, and at what cost.
3. **Decision** — the max choice, with its grounds.
4. **Rejected** — each other position, the reason, and the condition under which it would win.

The maintainer's codified practice (MAINT claims, source MAINT-S01) weighs as a strong
position, not as an automatic winner; where it is the max choice, say so.
