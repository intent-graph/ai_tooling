# Research brief — shared by every research slot

Paths below are relative to the guideline folder `ai_tooling/dev_guidelines/software_development_guidelines/`.
Your task message gives the absolute root, your slot, and your area.

## Goal

Identify the **authoritative sources** of best practice for your area and extract their
**claims**, so that a later step can distill them into an IntentGraph. You are gathering
evidence, not writing the guideline.

## What is being built

A cross-cutting guideline of **software-development principles that hold for every stack**:
how a team sources and chooses libraries, tools and external services; when it adopts versus
writes its own code; how it makes sure the software works at every level and keeps working;
how changes flow to production (CI/CD, deploy); how it runs and watches what it shipped
(monitoring). Stack guidelines (Python, JavaScript, web architecture) will link to it and keep
only their stack realization. Code style and application architecture are out of scope.

The guideline is held as one stack-neutral **philosophy** IntentGraph. A claim that only makes
sense for one stack or tool is still recorded, tagged with its stack, as a pointer for the stack
guidelines.

## Selection rule: max, not average

The guideline is a set of **decisions between competing practices**. The later judge picks, for
every point, the best practice for its purpose, the one the strongest arguments establish: never
the average, the most common answer, or a blend; and "best" is not "most demanding". Agreement
among sources is evidence, never the verdict. So for every point where practices compete:

- record **each position with its strongest argument and its best source**, including positions
  held by a recognized minority school;
- say which **force** each position serves and at what cost. Candidate forces: correctness,
  confidence, speed of feedback, delivery speed, cost of ownership, control, security, exit risk,
  team cognitive load, reversibility (add others the evidence shows);
- say the **context under which it wins** (team size, criticality, rate of change, regulation,
  number of consumers, and others the evidence shows). Do not assume a default team or project:
  the guideline states principles and the outcomes they guarantee, whoever does the work.

## Source authority tiers

- **T1 — normative or official:** standards and frameworks (NIST SSDF, SLSA, OpenSSF, OWASP
  projects, ISO/IEC where public, IETF), official documentation of tools and platforms,
  OpenTelemetry.
- **T2 — recognized authorities:** books and essays by widely cited practitioners and research
  programs (Google SRE books, DORA / Accelerate, Fowler, Beck, Feathers, Humble and Farley,
  Twelve-Factor App, Nygard, Hyrum Wright and Google's *Software Engineering at Google*), public
  engineering handbooks of large organizations. An Internet-Draft or working draft counts as T2.
- **T3 — reputable practice:** engineering blogs of established companies, maintainers of the
  tools concerned, well-known conference talks, peer-reviewed empirical studies.
- **T4 — community:** forums, personal blogs, popularity posts. Only to document a live debate,
  never the sole ground of a claim.

Prefer T1–T2. Read the actual source (fetch the page), not a summary of it. If a fetch fails,
look for another copy (official mirror, author's page, archived copy) before falling back, and
say so. Record the URL you actually read.

## Claim format (L3 of your result)

- `id` — `<AREA>-C<nn>`, area code given in your task message.
- `claim` — one normative sentence ("X should…", "Prefer X over Y when Z").
- `level` — `principle` (holds whatever the stack and team) | `decision` (a choice with
  alternatives the team must make and record) | `practice` (a concrete rule under a decision).
- `stack` — `neutral`, or the stack or tool it depends on.
- `sources` — source ids from your register, with the section or heading read.
- `agreement` — `consensus` | `majority` | `contested`.
- `positions` — for `majority` or `contested`: each position, its strongest argument, who holds
  it, the force it serves, and when it wins.
- `certainty` — grounded (you read it in a cited source) | inferred (your synthesis across
  sources, say from which) | open.

Aim for the claims that matter at principle and decision level: typically 25 to 50 for your
area. Do not invent claims to fill a quota; record gaps as open.

## Source register (also in L3)

`id` (`<AREA>-S<nn>`), tier, title, author or body, URL read, what it is authoritative on.

## Result file

Write `result.md` in your slot with three sections, each readable alone:

- `## L1 headline` — one sentence on the state of best practice in your area, its certainty,
  then the `Pinned:` block.
- `## L2 claims` — one line per cluster of claims (5 to 12 clusters): the cluster's claim,
  agreement, certainty, claim ids. Then the live debates, one line each, naming the forces in
  tension. Then the candidate central decisions of your area (choices every team must make
  first, because others depend on them). Then what you did not cover.
- `## L3 full` — the source register, then every claim in the format above, then gaps.

Pin, word for word at every level: the number of sources by tier, the number of claims, every
`contested` topic named in a few words, any fetch that failed on a T1 source.

## Slots (round 1)

| Slot | Area code | Boundary |
|---|---|---|
| `01_sourcing` | SRC | finding and profiling libraries, tools and external services or APIs: discovery, evaluation criteria, health and risk signals, fit to the task's profile |
| `02_adoption` | ADOPT | adopt, write own, or rent a service; living with dependencies: pinning, updates, supply chain, wrapping, exit and lock-in |
| `03_verification` | VERIFY | how a team knows it works at each level and keeps working: static analysis and types, test levels and strategy, contracts, regression, test-suite health |
| `04_delivery` | DELIVER | version control, code review, continuous integration, build and release, deploy strategies, rollback, environments |
| `05_operation` | OPERATE | observability, monitoring, alerting, service-level objectives, incident handling, feedback from production into development |
| `06_transverse` | TRANS | documentation kept in sync with the system, security practice across the lifecycle (supply chain is ADOPT), configuration and secrets, reproducible development environments |
| `07_maintainer_doctrine` | MAINT | the maintainer's own codified practice, entered as anonymized claims (its task message has its own rules) |

## Rules

- This is a public repository: no absolute or home paths in what you write, no names of
  private projects, employers or clients.
- Write only inside your slot folder. Never `git push`, never commit.
- Stay inside your area's boundary (task message lists your siblings). If a claim sits on a
  boundary, record it once, tagged `boundary: <sibling area>`.

## Round 2 addendum

Round 1 (slots 01 to 07) and its coverage check (`08_coverage_check/result.md`) are done. Round 2
fills the gaps inside the named areas. Read `08_coverage_check/result.md`, `## L2 claims`
section 1 (gaps) and section 3 (contested topics), and the `## L2 claims` of the round-1 slots
your boundary touches, to avoid repeating them. Prefer T1/T2; where a topic only has T3, say so.

| Slot | Area code | Boundary (gap ids from the coverage check) |
|---|---|---|
| `09_external_services` | EXT | G1, G2, G3: choosing and depending on external services and APIs (contract and SLA terms, availability, data portability, pricing and deprecation risk, vendor assessment, how to consume an API safely); evaluating tools and platforms that are not libraries (dev tools, CI and hosting services); licence obligations and compatibility |
| `10_data_change` | DATA | G4: changing persistent data and schemas safely in delivery (expand and contract, backward-compatible migrations, backfills, data migration testing, rollback of data changes), stack-neutral |
| `11_performance_readiness` | PERF | G5, G12: performance, load and capacity verification and planning; operational readiness (runbooks, production-readiness review, synthetic monitoring, telemetry cost) |

## Round 3 addendum

The maintainer fixed the hierarchy and the selection rule: read `build/distill/target_hierarchy.md`
and `build/distill/maintainer_decisions.md` first. "Max" means the best practice for the purpose,
not the most demanding one. No default team: claims are principles and the outcomes they
guarantee, whoever does the work. Read `08_coverage_check/result.md`, `## L2 claims`, to avoid
repeating round 1.

| Slot | Area code | Boundary |
|---|---|---|
| `12_evolution` | EVOL | decision records, incremental and evolutionary change, technical debt (identifying, tracking, paying down) and refactoring policy, decommissioning and end of life of the team's own software, keeping the number of technologies small |
| `13_change_authors` | AUTH | what the outcomes (good design, good testing, trustworthy review, what runs is what was reviewed) require when change arrives at high volume or from a non-human author such as an AI coding agent: review, verification, provenance, permissions and blast radius; stated author-neutral, recording where sources argue the author changes the mechanism |
| `14_recovery` | RECOV | backup, restore and disaster recovery: recovery objectives, restore testing, backup integrity and isolation, continuity, recovery of data versus of service |
| `15_security_depth` | SECD | security beyond lifecycle process: depth and placement of security testing, security monitoring and detection, privacy and data retention, maturity models (ASVS, SAMM, BSIMM) |
