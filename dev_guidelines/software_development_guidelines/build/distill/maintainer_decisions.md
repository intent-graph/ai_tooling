# Maintainer decisions

Every later agent reads this file and cites a decision by its number. The questions these answer
are in `maintainer_questions.md` beside it (answered there in the maintainer's words).

## MD-01 Selection rule: the best, not the average

"Max" is not the most demanding practice: it is **the best practice for the point's purpose**.
The core idea is to never default to the average of what sources say. It rests on the
aggregation of sources as collective intelligence: across many sources, take the position the
strongest arguments establish, not the most common one and not a blend. Agreement among sources
is evidence, never the verdict. A weaker practice is kept only with the condition under which it
would be the best.

Maintainer's words: "it's not the most demanding thing, it's the best thing. The core idea is to
not default to average."

## MD-02 Principles and outcomes, not a default team

There is no default team or project context. The guideline codifies principles and the outcomes
they guarantee, which hold whoever does the work: the design was good, the testing was good, the
review was trustworthy. Who writes the code (human or AI agent) is not a principle. Context
variables appear on a decision only where the best practice genuinely differs with them, each
stated with the condition that moves it.

Maintainer's words: "who cares if AI or human write the code, what matters are the immutables:
the design was good, the testing was good, the review was trustworthy".

## MD-03 Decision and practice split, without duplication

Keep the split between "how we know it holds" (ASSURANCE) and "how we do it" (realization
branches) for documentation, security and data. Information is stated once: where a topic
appears in two branches, one location holds it and the other is mostly an index pointing to it.

## MD-04 EVOLUTION is a top-level branch

How the system and its decisions change over time: decision records, incremental change,
technical debt and refactoring, decommissioning, keeping the number of technologies small.

## MD-05 Scope

In: the six named topics (sourcing tools, libraries and APIs; adopting versus writing code;
making sure things work and keep working; CI/CD; deploy; monitoring), code design that holds for
every language (CONSTRUCTION, ruled in the JavaScript guideline session), EVOLUTION, AI coding
agents as contributors (stated as author-neutral outcomes, per MD-02), backup, restore and
disaster recovery, security beyond process (security testing depth, security monitoring, privacy
and retention).
Out, listed as deferred: regulated contexts; software that is not a hosted service (mobile, data
and ML pipelines, infrastructure-as-code).

## MD-06 Models for judging and review

Sonnet does the bulk: judges and reviewers. Each reviewer flags the subtle points it cannot
settle with confidence; an Opus agent has the final say on the flagged points only.

## MD-07 Name

Folder `software_development_guidelines/`, one stack-neutral IntentGraph, graph id
`software-development-philosophy`.

## MD-08 Who can be the independent check on a change

A person is the independent check by default. An automated reviewer, working from its own
context, can be the independent check only for a tier of low-risk changes the team declares in
advance; every other change is checked by a person other than its author. A named person stays
accountable for every change.

Maintainer's answer (option C of the question in `03_judge/final_pass/maintainer_points.md`): "A
person by default, an automated reviewer only for a declared low-risk tier." Accepted cost: the
team keeps a declared list of low-risk change classes, and a team of one cannot meet the rule for
its own higher-risk changes.
