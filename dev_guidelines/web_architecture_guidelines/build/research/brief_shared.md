# Research brief — shared by every research slot

Paths below are relative to the guideline folder `ai_tooling/dev_guidelines/web_architecture_guidelines/`.
Your task message gives the absolute root, your slot, and your area.

## Goal

Identify the **authoritative sources** of best practice for your area and extract their
**claims**, so that a later step can distill them into IntentGraphs. You are gathering
evidence, not writing the guideline.

## What is being built

An architecture-level guideline for a **classic website: a browser running JavaScript, a
Python application server, a Postgres database**. Architectural level means: what each tier
owns, how tiers talk, which decisions a project must make and record. Code-level style (JS
idioms, Python idioms) is out of scope: separate guidelines cover it.

The guideline will be held as **two IntentGraphs**:

1. **Web-app philosophy** (product graph): principles for designing a web application *as a
   whole*. It is expected to overlap with, but differ from, principles for designing a
   backend alone or a database alone. Claims that hold for any stack go here.
2. **`PIG-WEB` defaults** (projection graph): the stack-specific architecture decisions for
   JS + Python + Postgres, each traced to its sources.

So for every claim, say which level it lives at (see the claim format).

## Source authority tiers

Rank every source you use:

- **T1 — normative or official:** standards and RFCs (IETF, W3C, WHATWG), official docs of
  PostgreSQL, Python, Django, FastAPI, MDN, web.dev, OWASP projects, OpenTelemetry.
- **T2 — recognized authorities:** books and essays by widely cited practitioners (Fowler,
  Kleppmann, Twelve-Factor App, Cockburn, Nygard, Evans), public API guidelines of large
  engineering organizations (Google AIP, Microsoft REST guidelines, Zalando).
- **T3 — reputable practice:** engineering blogs of established companies and maintainers of
  the tools concerned, well-known conference talks.
- **T4 — community:** forums, personal blogs, popularity posts. Use only to document a live
  debate, never as the sole ground of a claim.

Prefer T1–T2. Read the actual source (fetch the page), not a summary of it. If a fetch fails,
look for another copy (official mirror, archived copy) before falling back, and say so.
Record the URL you actually read.

## Claim format (L3 of your result)

One table or list entry per claim:

- `id` — `<AREA>-C<nn>`, area code given in your task message.
- `claim` — one normative sentence ("X should…", "Prefer X over Y when Z").
- `level` — `principle` (holds for any web stack → philosophy graph) | `decision` (an
  architecture choice with alternatives → PIG-WEB) | `practice` (a concrete rule under a
  decision → PIG-WEB, lower node).
- `stack` — `neutral` | `postgres` | `python` | `js` | `http` (what it depends on).
- `sources` — source ids from your register, with the section or heading read.
- `agreement` — `consensus` (T1/T2 sources agree, none dissents) | `majority` | `contested`.
- `positions` — for `majority` or `contested`: each position, who holds it, and when it applies.
- `certainty` — grounded (you read it in a cited source) | inferred (your synthesis across
  sources, say from which) | open.

Aim for the claims that matter at architecture level: typically 25 to 60 for your area.
Do not invent claims to fill a quota; record gaps as open.

## Source register (also in L3)

`id` (`<AREA>-S<nn>`), tier, title, author or body, URL read, what it is authoritative on.

## Result file

Write your `result.md` in your slot with three sections, each readable alone:

- `## L1 headline` — one sentence on the state of best practice in your area, its certainty,
  then the `Pinned:` block.
- `## L2 claims` — one line per cluster of claims (5 to 12 clusters): the cluster's claim,
  agreement, certainty, claim ids. Then the live debates in one line each. Then what you did
  not cover.
- `## L3 full` — the source register, then every claim in the format above, then gaps.

Pin, word for word at every level: the number of sources by tier, the number of claims, every
`contested` topic named in a few words, any fetch that failed on a T1 source.

## Rules

- This is a public repository: no absolute or home paths in what you write, no names of
  private projects, employers or clients.
- Write only inside your slot folder. Never `git push`, never commit.
- Stay inside your area's boundary (task message lists your siblings). If a claim sits on a
  boundary, record it once, tagged `boundary: <sibling area>`.

## Round 2 addendum

Round 1 (slots 01 to 07) and its coverage check (`08_coverage_check/result.md`) are done.
Round 2 fills the gaps that check found. Decisions taken after round 1:

- **Tier of drafts:** an IETF Internet-Draft or W3C working draft counts as **T2**, not T1, until
  published as a standard. Say so when you cite one.
- **Scope in:** runtime topology, rate limiting and abuse, file uploads and object storage,
  real-time channels at decision level (polling vs SSE vs WebSocket).
- **Scope light:** multi-tenancy is one decision node, default single-tenant, options listed.
- **Scope out (recorded as deferred, not researched):** high availability and replication, i18n,
  PWA and offline, GDPR erasure, search, email and scheduled jobs, incident response.
- Round-2 slots may read round-1 results to avoid repeating them: read `## L2 claims` only,
  and `## L3 full` only for the claim ids your task names.

## Round 4 addendum

The structure and selection rule changed: read `../distill/target_hierarchy.md` first.
Round-4 slots look for the **strongest** argument for each position (max, not consensus):
record which force each position serves and the context under which it wins. Positions held
by a recognized school (even a minority one) are wanted, with their best source.
