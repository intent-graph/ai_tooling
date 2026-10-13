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

## MD-08 "Max" means the best practice, not the most demanding one

Status: decided by the maintainer on 2026-10-13, in the software-development guideline session
(recorded there as its MD-01), and applied here.

Maintainer's words: "it's not the most demanding thing, it's the best thing. The core idea is to
not default to average." The rule rests on the aggregation of sources as collective
intelligence: take the position the strongest arguments establish for the node's purpose, not
the most common one and not a blend.

The judges of this guideline worked under the earlier wording ("the most demanding practice
that best serves the purpose"). Their records keep that wording as history; the live documents
(`target_hierarchy.md`, `../RECIPE.md`, the guideline README) now state MD-08.

## MD-09 Re-audit under MD-08: seven verdicts corrected

Status: decided by the maintainer on 2026-10-13 ("ok apply all"), after the re-audit in
`08_reaudit/`.

The seven verdicts where strictness, not fitness for purpose, decided the outcome are replaced
by the re-audit's proposals (full evidence and propagation in `08_reaudit/*/result.md`):

1. MFA offered to every human account (phishing-resistant preferred), required for privileged
   accounts and at step-up before sensitive operations; universal requirement by risk level
   (LOGIC.SECURE and its stack realization).
2. Client-named fetches: the safe fetch helper is required; a network guard is preferred, and
   required only when the server's network holds internal services or a token-less metadata
   endpoint (PIG-WEB-LOGIC.SECURE.7).
3. Consequential agent scopes: sender-constrained tokens wherever the client can hold a key;
   otherwise short-lived, revocable bearer tokens with every consequential action behind the
   owner's exact-action approval (PIG-WEB-INTERACTION.AGENT.3, aligned with PIG-WEB-LOGIC.SECURE.4).
4. Normalization: keep the dependency-preserving third-normal-form design and enforce the
   dependency declaratively (composite foreign key); a trigger only where no declarative form
   exists (DATA.ORGANIZE).
5. Deferral: defer work expected to exceed a few seconds or the request timeout; 1 s stays the
   interactive-response target, not the deferral cut-off (ALLOCATION.ACT.3, ACT.2).
6. Paging: keyset for structured-data and agent interfaces and for large or growing sets;
   offset with page numbers acceptable for a human HTML list over a bounded result
   (ALLOCATION.DERIVE.2 and its stack realization).
7. Threat modelling per critical flow and trust boundary, revisited when a placement on the flow
   changes, with misuse-case tests per tier (TRANSVERSE.SECURITY).

## MD-10 Alignment with the software development guideline

Status: decided by the maintainer on 2026-10-13, after the linking pass in
`09_links_software/result.md` (tensions K1 to K12, outdated deferrals S1 to S3, gap G1).

1. **K1 and K2 (reads on base tables, default deletion): the web decisions stand** (MD-05,
   MD-04). The software guideline's session is asked to amend or scope its nodes; the web side
   does not change.
2. **K3 to K12: the web guideline aligns with the software guideline**, keeping its stack
   realization: secrets through a managed store primary, environment variables an exception
   with its reason recorded (K3); hardened isolated builds by risk, not by default (K4); host
   allowlist where the set of hosts is known, private-range refusal where users may name any
   public host (K5); recovery strategy per workload from its objectives, a copy out of reach of
   production credentials, automated restore tests (K6); circuit breakers only where a
   dependency fails slowly or is shared (K7); explicit API versions only for many, external or
   independently released consumers (K8); independent scaling, fault isolation and a different
   runtime as reasons to split a deployable (K9); a new technology as a replacement with the
   older one's retirement planned and owned (K10); accepted decision records may be corrected
   without changing the decision (K11); a verification level paired with outcome measures
   (K12).
3. **S1 to S3: the deferred web nodes point to the software guideline** for incident response,
   personal data erasure and high availability.
4. **G1 (rollback): recorded as a gap only.** No web realization of a rollback or fix-forward
   rule is added now.
