# Points for the maintainer

The final pass settled every flagged point it could from the evidence (see `resolutions.md`). One
point depends on the maintainer's own working context and is asked below. The second section lists, one
line each, every decision that goes against the maintainer's codified practice, even where settled, so
the maintainer can see them and object.

---

## Points to decide (1, answered: MD-08)

### 1. Can an automated reviewer be the independent check on a change?

**Situation.** The guideline requires every change to the main line of the code to be checked, before it
is integrated, by a party other than whoever wrote, pushed or requested it, with a named person
accountable for the change (the node "Independent review that binds", ASSURANCE.RULES.4). The sources
agree that the person who submits a change stays responsible for it; none of them addresses a team with
a single person, nor whether an automated reviewer (an AI model reviewing the change in its own,
separate context) can be the independent party. Under the maintainer's rule that who writes the code is
not a principle, two cases arise:
- the change was written by an AI agent: the person who reviews it is already independent of its author;
- the change was written by the only person on the team: no second person exists to review it.

**Options.**
- **A. Independence is a property of the reviewer's context, not of its kind.** Any reviewer that did
  not write the change and works from its own context (a person, or an automated reviewer given only the
  change, its stated intent and its tests) counts as the independent check; a named person stays
  accountable and approves every change. Cost: when author and reviewer are models of the same kind,
  their blind spots may overlap.
- **B. Only a person can be the independent check.** Cost: a team of one can never meet the rule for
  its own changes; it either breaks the rule or stops.
- **C. A person by default, an automated reviewer only for a declared low-risk tier.** Cost: a second
  list of change classes to keep; for every higher-risk change a team of one is back to option B.

**Recommendation.** A, with one addition for the changes the team's risk tier marks high (they hold
locks, change data irreversibly, or touch a security boundary): the reviewer is of a different kind from
the author. An AI-written change reviewed by the accountable person already meets this; a change written
by the only person is reviewed by an automated reviewer in a separate context, preferably a different
model, and the person approves.

**Default if unanswered.** Option A as recommended. ASSURANCE.RULES.4 then reads: "Every change to
mainline is checked before integration by a party other than whoever authored, pushed or requested it,
working from its own context: a person or an automated reviewer; for a change the team's risk tier marks
high, the reviewer is of a different kind from the author. A named person or role stays accountable for
each change, approves it and is able to defend it." Certainty stays inferred, and the point is marked
open in the graph until the maintainer answers.

Remi's answer:  A person by default, an automated reviewer only for a declared low-risk tier.
---

## Settled against your practice

Each line: the node, the maintainer's codified practice (ledger row), what was decided, and why.

1. ASSURANCE.BEHAVIOUR.1 and CHANGE_FLOW.BUILD.1 (L331): if the practice runs the test suite on demand
   only, it stands against the decision that the suite runs automatically on every change; an on-demand
   suite does not guard change (L081, L106, L144, consensus).
2. ASSURANCE.BEHAVIOUR.7 (L265): tests on shared or production-sized data under a forced rollback are
   kept only where the data cannot be cloned and the platform undoes every effect; the default is a
   disposable store per run, because a rollback cannot undo every effect (rebuild over clean-up, L111).
3. ASSURANCE.CONTRACTS.1 (L295): "no version numbers, coordinate and deploy together" holds for few,
   in-house, reachable consumers only; external or independently released consumers cannot be
   coordinated, so they get explicit versions and a deprecation window.
4. ASSURANCE.BEHAVIOUR.5 (L316): the reduced-scope test mode for a scheduled job is kept as an example,
   not a requirement; the requirement is the outcome (tested before scheduled, first runs bounded).
5. ASSURANCE.BEHAVIOUR.8 (L274): "exercise every branch on production-shaped data" is narrowed to code
   whose behaviour depends on data shape; "every branch" is a coverage target, which BEHAVIOUR.6 rejects.
6. OWNERSHIP.STANCE.1 and .2 (L308, L310): the four reasons for a layer become examples, and the
   built-in-first ranking becomes "the lowest-ownership case of the cost test"; no public row ranks them.
7. ASSURANCE.SECURITY.6 (L327): a job with a large blast radius is triggered by the accountable person
   through the guarded path (the pipeline where it reaches), not by default "by a person at their own
   terminal"; the outcome (an executor cannot bypass guards, the script was reviewed) is kept.
8. CONSTRUCTION.DESIGN.1 (L329): the fixed derivation order binds the decisions costly to reverse; cheap
   parts may emerge, since a fixed sequence there is ceremony without benefit.
9. CONSTRUCTION.SYSTEM_SHAPE.3 (L295): routine lock-step deployment of two units is read as a misplaced
   boundary; a coordinated breaking change stays legitimate as an exception (L171, consensus).
10. CONSTRUCTION.BOUNDARY.5 (L309): "prefer a signature over a shape-bound interface" becomes "choose by
    who composes the result"; a view also hides how its result is produced, and only the caller can
    compose a shape-bound surface.
11. CONSTRUCTION.BOUNDARY.6 (L315): offending values in errors go to logs and trusted callers only; an
    untrusted caller gets the stable code and field names (OWASP Error Handling Cheat Sheet).
12. CONSTRUCTION.PARADIGM.2 (L311): logic is placed by the property it must have, not by tier; in-store
    scheduling is kept only within its stated limits, an orchestrator otherwise.
13. CHANGE_FLOW.DATA_CHANGE.3 (L290): ordinary database changes reach production automatically; the
    risky class passes an authorization stage of the same pipeline instead of a manual run, with the
    risk criterion (including table size and unmeasured duration) deciding the class.
14. CHANGE_FLOW.DATA_CHANGE.1 (L289): idempotent DDL is required where a step can be partially applied
    or environments differ, not for every statement; once-only tooling already covers the transactional
    case.
15. CHANGE_FLOW.DATA_CHANGE.7 (L293): a migration skipped on the development dump is rehearsed on
    production-shaped data before its production run, so no migration reaches production unrehearsed.
16. CHANGE_FLOW.ROLLBACK.3 (L288): a written reverse is prepared only where reversal by script is faster
    than a restore, and counts only if rehearsed; otherwise the undo is a roll-forward or the tested
    restore (REG-244, REG-251).
17. CHANGE_FLOW.DEPLOY.3 (L328): if the row was meant to relax parity of backing-service type or version,
    it is decided against; divergence is accepted only for scale, data volume, permissions and schemas
    present only in production (Twelve-Factor).
18. EVOLUTION.INCREMENTAL.6 (L296): a deprecated item is marked in machine-readable metadata, and in its
    name only where the rename breaks no consumer, since a rename is a breaking change (CONTRACTS.1).
19. TRANSVERSE.DOCS.3 (L318): a dated change log in the unit header is kept only where readers cannot see
    the repository history (for example a definition read from a database catalogue); elsewhere history
    stays in version control, one origin per fact.
20. TRANSVERSE.DOCS.2 (L321): hand-kept line counts and line-number tables of contents are admitted only
    when a machine checks them (ASSURANCE.DOCS_SYNC.4), since unchecked they rot.
