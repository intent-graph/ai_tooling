# Transverse: Documentation

How documentation is sized, organised and written. Part of [Transverse](transverse.md).

## Table of Contents

1. [Documentation Practice](#documentation-practice) _(Lines 15-21)_
   1. [Documentation Budget](#documentation-budget) _(Lines 24-42)_
   1. [Organisation and Structure](#organisation-and-structure) _(Lines 45-59)_
   1. [Layered Writing and Audience Split](#layered-writing-and-audience-split) _(Lines 62-78)_
   1. [Release Changelog](#release-changelog) _(Lines 81-94)_
   1. [Basis and Evolution of Guidelines](#basis-and-evolution-of-guidelines) _(Lines 97-110)_
## Documentation Practice
<!-- Lines 15-21 -->

Documentation is sized by its consumers, life and turnover, kept in small documents organised by
reader need and reached from an index, and written in layers for each audience. It is then found,
read at the depth the reader needs and cheap enough to keep current. Realizes
[Documentation in Sync](assurance_docs_security.md#documentation-in-sync), which holds the mechanisms that keep
it true (same-change delivery, gates, owners, executable examples). `TRANSVERSE.DOCS`

### Documentation Budget
<!-- Lines 24-42 -->

The amount of documentation is a recorded decision, and its upkeep is budgeted as part of
delivery. The level follows the system.

- MUST record the chosen level.
- MUST record the upkeep budget.
- Relies on the owners and gates of [Documentation in Sync](assurance_docs_security.md#documentation-in-sync)
  at the full level, and on [Ownership, Freshness and Single Source](assurance_docs_security.md#ownership-freshness-and-single-source)
  for read-only derived documents.

| Level | Best when |
|---|---|
| Minimal, conversation first | The team is small and co-located and the system short-lived |
| Living documentation, generated or extracted from code and tests | The knowledge is already in the code (it cannot hold why, context or decisions) |
| Full documentation with owners and gates | Consumers are many, life is long, people turn over |

Specialist writing effort goes to documents that cross interface boundaries and to shared
guidance; accuracy-critical text is written by someone who knows the system. `TRANSVERSE.DOCS.1`

### Organisation and Structure
<!-- Lines 45-59 -->

Documents are small and modular, each organised by one reader need (tutorial, how-to, reference,
explanation), reached from an index by role and situation, and improved in small increments.

- MUST keep an index updated in the change that adds or moves a document.
- MUST NOT keep a derived navigation aid (table of contents, line reference) by hand; size caps
  are enforced mechanically.
- Where a formal model exists, each guideline links to the node it derives from.

Best instead: hand-kept line counts and tables of contents are best never; they are admitted when a
tool generates and checks them. One large specification is best never for living documentation.
Relies on [Ownership, Freshness and Single Source](assurance_docs_security.md#ownership-freshness-and-single-source)
and [Mechanical Documentation Checks](assurance_docs_security.md#mechanical-documentation-checks).
`TRANSVERSE.DOCS.2`

### Layered Writing and Audience Split
<!-- Lines 62-78 -->

Text is written at layered depth (one sentence, one paragraph, then full what, why and how) with
diagrams at three zoom levels, so each reader stops at the depth they need. The durable explanation
of a code unit lives with the unit.

- MUST NOT state in an inline comment what the next line does; comments carry why, an invariant
  or a gotcha.
- MUST give an interface consumed by many callers a structured header (summary, parameters,
  returns, notes, examples with expected output).
- MUST NOT hold change history in two places: version control holds it.

Best instead: a dated change log in the header is best only where readers cannot see the
repository history (for example a definition read from a database catalogue). A header on every
unit is best never; for a private helper, self-documenting code is best when the contract is
obvious from name and types. Examples are executed by [Mechanical Documentation Checks](assurance_docs_security.md#mechanical-documentation-checks).
`TRANSVERSE.DOCS.3`

### Release Changelog
<!-- Lines 81-94 -->

Each release has a changelog written for its readers, grouped by change type, with an unreleased
section filled in the change that introduces each entry. A list generated from commit messages may
seed the draft but is not the record: commit logs are noisy, a changelog tells readers the
noteworthy differences.

- MUST write each entry in the unreleased section, in the change that introduces it (presence is
  enforced by [Mechanical Documentation Checks](assurance_docs_security.md#mechanical-documentation-checks)).
- A changelog belongs to a [Release](change_flow_delivery.md#release).

Open: the condition under which a commit-generated changelog would be best (plausibly: every
commit held to a convention written for readers who are the developers of the same code) is
inferred, not established. `TRANSVERSE.DOCS.4`

### Basis and Evolution of Guidelines
<!-- Lines 97-110 -->

Every rule records its basis: observed practice with its evidence, or a principle with the outcome
it guarantees. A reader can tell why a rule exists, how much evidence stands behind it and what it
replaced.

- MUST state the basis of each rule.
- MUST mark a deduced rule unconfirmed until practice confirms it.
- MUST state the overridden rule and its objects when a rule overrides an earlier one.

Best instead: induction from real production code wins in a mature codebase; in an immature one it
codifies habits, so deduction from principles applies until practice exists. Records of an
overriding rule are held in [Decision Records](evolution.md#decision-records).
`TRANSVERSE.DOCS.5`

