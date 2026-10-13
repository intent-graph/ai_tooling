# J6 Postgres data tier: questions for the maintainer

One question, awaiting the maintainer. Every other node of the Postgres data tier is decided. The decisions that go against your codified practice are listed in `result.md`, each with its grounds. They are not asked here because, in each case, one force the node serves wins outright.

## Q1. What is the default way to delete user-facing data? (awaiting maintainer)

**The ask.** Which deletion should be the default for user-facing transactional data, such as documents, comments and tasks?

**Recommendation.** By default, remove the row and copy it to an archive in the same transaction. Keep a deleted-at marker on the tables where the product lets users restore or undo what they deleted (a trash, an undo), or where reports must count deleted rows in place. This is the most demanding choice for the integrity of the stored data.

**If unanswered.** The guideline records your current practice: soft delete by default for user-facing transactional data, with three safeguards made mandatory (listed at the end). The recommendation stays recorded beside it, and the point stays marked as awaiting your decision.

**The situation.** When a user or an agent deletes an item, the database can do one of two things:
- mark the row deleted and keep it in place (soft delete, a `deleted_at` timestamp);
- remove the row and copy it, in the same transaction, to an archive table.

Your practice makes soft delete the default for user-facing transactional data, about 60% of tables. It pays the costs explicitly:
- deletion functions soft-delete the children a cascade would otherwise reach;
- checks exempt deleted rows, and uniqueness covers active rows only;
- partial indexes cover active rows;
- no application role can DELETE.

The research leans the other way: archive by default, soft delete only where the product offers undo. That lean rests on one practitioner critique, a single experience-based source rather than a standard or a study. The critique says soft delete:
- leaks its "not deleted" filter into every query;
- stops foreign keys from protecting deleted parents;
- makes a legal purge harder;
- is rarely used for undelete (an observation from that one source).

Your practice answers most of that critique. The guideline now assumes a shared database, which your practice predates: several backends, BI and reporting, admin consoles and scripts all read the base tables. That cuts both ways, as the options show.

**What is at stake.** Both options keep deleted data recoverable and kept for audit. They differ on two forces:
- the integrity of references and reads for every consumer of the database, which favours the archive;
- immediate undo and in-place history, for users and agents (one update undoes a mistake) and for reporting (deleted items stay in the base table for historical figures), which favours soft delete.

The first is what the data tier exists to protect. The second belongs to the people and tools that use the data. Choosing between them is a judgment on your products, which is why it is asked.

**Option A: soft delete by default (your practice).**
- Gains:
  - a restore or an undo is a single update, immediate for the user or agent;
  - history stays in place: a report on last year's orders still finds the orders deleted since, with no extra query.
- Costs:
  - every consumer that reads base tables must filter out deleted rows: each backend, every BI query and every script. A forgotten filter shows deleted data, and some of these consumers are outside the team's review.
  - Foreign keys no longer stop a new active row from pointing at a deleted parent, so a trigger on each child table must refuse it.
  - Unique values need partial indexes.
  - A personal-data purge must also find the soft-deleted rows.

**Option B: archive by default; soft delete where the product offers restore or undo, or where reports must count deleted rows in place.**
- Gains:
  - foreign keys and unique constraints keep working unchanged;
  - no consumer can read a deleted row by forgetting a filter;
  - a purge is a delete from the archive.
- Costs:
  - a restore is a function that re-inserts the row and its children from the archive and re-checks them against today's rules, slower to build and to run than one update;
  - the archive holds old row shapes as JSON, which a restore must map;
  - a report that must count deleted items in historical figures, on a table where that need was not foreseen, has to combine the base table with the archive, and every reporting consumer must know to do so;
  - deleting a parent that has children still needs a deletion function that archives and removes the children in order, because cascading deletes are not allowed on core entities;
  - the archive overlaps with the trigger-written history, which already holds the deleted row.

**Why B is recommended.** On integrity, B wins: under A the costs fall on every consumer of a shared database, some outside the team's review; under B they fall on one restore function the team owns. A wins on immediate undo and in-place history, and B keeps soft delete exactly where the product offers undo or reports need deleted rows in place. Restores being rare, as the critique reports, would make B's slower restore cheap, but that rests on one source.

**What would make A the better default.** Most user-facing tables offer undo in the product, or most reports must count deleted rows, or every consumer reads through one shared, tested layer that applies the filter.

**What is decided either way.**
- Deletion runs only through functions, owned by a narrow role that holds only the delete and archive rights; no consumer role holds DELETE.
- Retained data is never removed without an archive copy.
- Caches are invalidated or dropped, never soft-deleted.
- Time-bounded data expires by dropping partitions.

**The three safeguards required with soft delete:**
1. A trigger on each child table refuses an active row whose parent is soft-deleted, so the rule holds for every writer, including direct writes and maintenance jobs.
2. The "not deleted" filter is written once, in the shared specification every consumer reads with.
3. A restore re-checks the row against the current constraints.
