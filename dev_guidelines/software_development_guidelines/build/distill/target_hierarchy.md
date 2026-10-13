# Target hierarchy and selection rule (maintainer decisions)

Status: decided by the maintainer (`maintainer_decisions.md`, MD-01 to MD-07). Every later agent
reads this file and `maintainer_decisions.md` before working. The provisional skeleton in
`02_skeleton/` was cut before these decisions and is re-cut on this file.

## Functional hierarchy

**L0.** A team delivers, and keeps delivering, a system that does what is intended, at a cost it
can sustain.

**L1, in this order:**

1. **OWNERSHIP** (decision): for each capability, does the team write it, adopt it (a library or
   tool it runs) or rent it (an external service or API)? Finding, profiling and selecting,
   adopting versus writing, the dependency lifecycle, containment and exit, external services,
   licences.
   - forces: control, time to value, cost of ownership over time, exit risk, security exposure,
     fit.
2. **ASSURANCE** (decision): for each property that must hold, which mechanism, at which stage,
   guarantees it, and runs on every change so that it stays true. One placement node per
   property: behaviour, interfaces and contracts, data integrity under change, documentation in
   sync, security, performance, availability and recovery, artifact integrity; plus the rules
   common to every property. Mechanisms include design review, a type or static check, a test at
   a given level, code review, a CI gate, a deploy check and a production monitor.
   - forces: speed of feedback, realism of the confidence, cost to build and maintain,
     flakiness, cognitive load.
   - outcomes it guarantees whoever does the work (MD-02): the design was good, the testing was
     good, the review was trustworthy, what runs is what was reviewed.
3. **CONSTRUCTION** (realization): how code is structured so it is correct and stays changeable,
   in its language-neutral form: boundary contracts and call shape, information hiding, state in
   one place, effect-free modules, dependency direction, naming, paradigm by intent, keeping
   data from becoming code, process lifecycle.
4. **CHANGE_FLOW** (realization): version control and integration, review, build, release,
   deploy, rollback, data and schema change, measuring delivery.
5. **OPERATION** (realization): reliability targets, alerting, telemetry, incidents, capacity,
   readiness, runbooks, backup, restore and disaster recovery, feedback into development.
6. **EVOLUTION** (realization over time): decision records, incremental change, technical debt
   and refactoring, decommissioning, keeping the number of technologies small.
7. **TRANSVERSE**: documentation practice, security practice (including security monitoring,
   privacy and retention), configuration and secrets, development environments.

Realization branches carry out what OWNERSHIP and ASSURANCE decide and link back to the decision
nodes; they do not re-decide them.

## One location per fact (MD-03)

Where a topic spans a decision branch and a realization branch (documentation, security, data,
availability and recovery), the fact is stated once. The decision node holds which mechanism
guarantees the property; the realization node holds how the practice is carried out. Whichever
holds less on a topic is mostly an index: a one-line intent and links, no restated content.

## Selection rule: the best, not the average (MD-01)

For every node, the guideline states **the best practice for the node's purpose**, the one the
strongest arguments across all sources establish. Never the average, the most common answer, or
a blend; and "best" is not "most demanding". Agreement among sources is evidence, never the
verdict. A weaker practice stays only as "best when <condition>".

## No default team (MD-02)

The guideline states principles and the outcomes they guarantee, whoever does the work, human or
AI agent. A decision carries context variables only where the best practice genuinely differs
with them, each with the condition that moves it. "AI coding agents as contributors" enters as
what the outcomes require when change arrives at volume or from a non-human author, never as a
rule about who writes the code.

## Judge record (every decision node)

1. **Positions**: the competing practices, from the evidence (ledger ids, source ids).
2. **Forces**: which purpose or force each position serves, and at what cost.
3. **Decision**: the best practice, with its grounds.
4. **Rejected**: each other position, the reason, and the condition under which it would be the
   best.
5. **Flags**: points the judge or reviewer cannot settle with confidence, for the final Opus pass
   (MD-06).

The maintainer's codified practice (MAINT claims, source MAINT-S01, not citable) weighs as a
strong position, not an automatic winner; where it is the best, say so.

## Scope (MD-05)

Out, listed as deferred: regulated contexts; software that is not a hosted service (mobile, data
and ML pipelines, infrastructure-as-code).
