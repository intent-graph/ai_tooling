# Request to the software development guideline: two tensions where the web decisions stand

Status: open, addressed to whoever maintains `../../../../software_development_guidelines/`.

The linking pass between the two guidelines (`result.md` in this folder, L3, tensions K1 and K2)
found two points where they disagree. The maintainer ruled that the web decisions stand and
asked that the software guideline amend or scope its nodes (web decision MD-10, in
`../maintainer_decisions.md`). Nothing in the software guideline was edited from the web side.

## 1. Default deletion

- Software node `ASSURANCE.DATA_INTEGRITY.3`: keeps a deleted flag only where undelete is a
  user-facing feature; otherwise deletes and archives in the same transaction.
- Maintainer decision (web MD-04): deletion is a per-table design choice weighed on the data's
  importance, how easily it can be reconstructed, how often it changes and its business value.
  Soft delete comes in two kinds (last-state, full-history). The default is basic soft delete: a
  `deleted_at` column, no primary-key change, every consumer excludes deleted rows ("a very easy
  part to enforce"). Hard delete plus a same-transaction archive is acceptable for some caches and
  when consumers must be unable to reach past data; its weaknesses are performance at scale and
  keeping the current and archive schemas in sync. Foreign keys always; functions or triggers
  propagate soft deletion down hierarchies where foreign keys are not enough.

## 2. Reads on base tables

- Software nodes `CONSTRUCTION.HIDING.4` (consumers never bind to base structures) and
  `CONSTRUCTION.BOUNDARY.4` (a published layer in the store when direct query access is needed).
- Maintainer decision (web MD-05): simple reads with no logic (a basic select, a few joins) are
  written by each backend directly on base tables; sensitive, complex or high-impact reads,
  reads that must be built by a function, and abstractions several backends share go through
  database functions.
