# J5 web-app-philosophy TRANSVERSE: questions for the maintainer

None.

All 14 nodes are decided (`records.md`). No node holds a genuine trade-off between forces it serves, where the max choice for one force costs another that the node also serves and that neither the evidence nor a maintainer decision settles. The adversarial review of this branch upheld that no decided node should become a question.

## Not a question from this unit, and not settled here

The open maintainer question: who filters reads of rows that carry per-user rules (for example, "a draft is visible only to its author") when several backends share the database. Two nodes touch it and record the default that holds if the question stays unanswered, marked "awaiting maintainer":
- the security node, under broken access control;
- the testing node, under denial tests.

What is recorded if unanswered:
- Each backend filters these reads from one shared written specification, with a shared denial-test suite that every backend runs.
- Database read functions that receive the verified user stay acceptable when a per-user read rule must hold for two or more backends.
- Consequence, stated wherever it matters: roles that may read the base tables directly (reporting, operator) see every row, comments included, unless their own role is restricted. Nothing in these nodes claims a stronger visibility guarantee.

## Decided, flagged for the maintainer's attention

One verdict narrows the maintainer's codified practice. It is realized here and counted once, where the database function API is judged in the stack graph.
- The codified practice: a breaking change to the database function API is coordinated with every consuming team and deployed together, with no formal version numbers.
- This verdict keeps the coordination and the absence of version numbers. "Deployed together" stays acceptable only when every consumer of the changed object ships in the same deployment as the migration. Otherwise the change goes expand, migrate, contract: add the new function beside the old, move each consumer, remove the old one once no consumer calls it. The new function's name carries the change.
- Grounds: the database, several backends, BI reports and scripts deploy separately; backends roll out instance by instance; browser tabs run old code for days.
- The narrowing is smaller than it looks: the maintainer's own practice for stored contract schemas already gives a breaking change a new named version, retires the old one and lets consumers migrate gradually.
- If the maintainer prefers lockstep as the default, the verdict is reversed by a maintainer decision on that point.
