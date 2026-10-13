# Maintainer decisions

Decisions the maintainer took during distillation. Each overrides the judges and reviewers on
its point; judges cite the entry by its id.

## MD-01 Row-level security is not a default

Status: decided by the maintainer at the allocation checkpoint.

Postgres row-level security is an advanced mechanism. Do not use it by default. It is
acceptable only when all of these hold:

- the data model is simple;
- the scoping key (client, tenant or owner id) is present in every table the policy covers,
  which in practice forces composite primary keys led by that key;
- no all-powerful administrator role must read or write across scopes (such roles mesh badly
  with row policies).

Authorization stays a backend decision with database privileges per role as the second gate
(the allocation verdict for authorization stands). Applies to `PIG-WEB.ALLOCATION.ROW_SECURITY`
and to the authorization placement's "would move it" column; it replaces the J1 judge's
question and the J1 review's recommendation on that point.

## MD-02 Interface documentation is always in sync; its origin is per project

Status: decided by the maintainer at the allocation checkpoint.

The guideline's requirement is not design-first or code-first: it is that the interface
description (OpenAPI or equivalent) is **always in sync** with the implementation. That is
guaranteed by process: one origin per fact, the other side generated or conformance-checked,
review rules, and a CI/CD gate that fails on drift. Whether the description or the code is
the origin depends on the type of project and is recorded per project as a decision, with the
criteria for each direction. Applies to `ALLOCATION.RECORD.3` and
`PIG-WEB.ALLOCATION.TYPE_CHAIN`; replaces the J1 verdict and the J1 review's re-decision on
the origin direction.

## MD-03 Default context: several consumers share the database; multi-table operations belong to it

Status: decided by the maintainer at the allocation checkpoint.

Assume the database may be shared by several backends and by other consumers (BI and
reporting, admin consoles, scripts). Consequently:

- Operations that change several tables as one business operation are the **database's**
  responsibility (database functions), not a backend's. This matches the maintainer's model:
  the database stores, organizes and maintains the data.
- Everything that must hold whoever touches the data lives in the database: constraints,
  multi-table operations, per-role privileges, audit.
- The database function API is the default contract to the data, not a "two or more
  backends" exception.

This replaces the J1 default context ("the Python backend is the only database consumer") and
the J1 verdict on business rules and state transitions (ACT.1) where it kept multi-table
operations in the backend; the maintainer doctrine row L584 stands. Every verdict that relied
on a single consumer is re-judged under this context.

## MD-04 Deletion is a per-table design choice; the default is basic soft delete

Status: decided by the maintainer, answering the deletion question.

- Deletion strategy is a design choice per table, weighed on the data's importance, whether it
  can be reconstructed easily (caches can), how often it changes, and its business value.
- Soft delete comes in two kinds: a **last-state** soft delete (the row stays, marked deleted)
  and a **full-history** soft delete (every past state is kept).
- **Default: basic soft delete**: no change to the primary key, a `deleted_at` column. Every
  consumer excludes deleted rows; in the maintainer's experience this is easy to enforce.
- **Hard delete plus a same-transaction archive** is acceptable for some cache profiles, and when
  consumers must be guaranteed unable to reach past, historical or outdated data. Its
  weaknesses: performance cost at scale, and, the biggest one, the current and archive table
  schemas must be kept in sync.
- In every case foreign keys are required. Where they are not enough (full-history soft
  delete), database functions or triggers maintain the soft-delete logic, and soft deletion
  propagates down a hierarchy of soft-deleting tables as the model requires.

Replaces the J6 recommendation (hard delete plus archive by default) and closes the deletion
question; the research position becomes the "acceptable when" case above.

## MD-05 Simple reads direct; sensitive or complex reads through database functions

Status: decided by the maintainer, answering the read-visibility question.

- Simple reads that carry no logic (a basic select, a few joins) are written by each backend
  directly.
- A read that is sensitive, complex, high-impact, or must be built by a function (for example
  the JSON representation of a virtual object), or an abstraction several backends share, is
  wrapped in a database function.

Closes the read-visibility question. Per-user visibility rules are sensitive reads under this
rule: they go through database functions (the former fallback becomes the rule for them).

## MD-06 Hosting is chosen per project; a prototype takes the fastest secure path

Status: decided by the maintainer, answering the hosting question ("no opinions").

When prototyping, reach something that works fast, as long as it is secure. An orchestration
platform brings reliability and scaling; that is valuable, but not what a prototype needs
first. The hosting model is a per-project choice recorded as a decision; the guideline's
self-managed defaults are one acceptable route, and the orchestrated case lists what changes.
Closes the hosting question.

## MD-07 SameSite: no maintainer preference; the judged recommendation stands

Status: decided by the maintainer, answering the SameSite question ("No opinion").

The judge's recommendation is adopted as decided: Lax plus a server-side check rejecting
cross-site navigations on sensitive pages, Strict for operator consoles. Closes the question.

## Not answered at this checkpoint

The six overrides of the codified practice, the Obsidian `.gitignore` and the commit were not
answered: the overrides stay as judged (recorded in the graphs), the export stays untracked,
and nothing is committed.
