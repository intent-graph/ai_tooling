# Elicitation round 1 — the brief, the questions, the answers

Purpose: the user's intent in their own words, and the questions that drew it out. This is the "intent behind the source". Dictation typos are cleaned; meaning is untouched. Questions are compressed to their ask and default.

## The brief (user, opening message, cleaned)
<!-- Lines 7-19 -->

I discovered you have trouble thinking and outputting with a level-of-detail approach. It is a concept I have been using through various projects, like my notes on working method, the full primers in `intent_graph/agents`, and more generally the IntentGraph pitch. Recently I wrote sort of an algorithm to help you grasp how to fabricate this level of detail.

The key insight is that working knowledge, the one used as the basis for thinking, for acting (building something) and for communicating (in various contexts), is not a flat set of facts. It is a hierarchical tree where facts and ideas are represented at various levels of detail, and aggregated as such. The level of detail is a tree, but of course the concepts, facts and ideas are connected between them, and that is more of a graph.

The second key insight is that once we know facts are not just a fact but a hierarchy of connected facts, it becomes clear that it is a strategic decision to decide which level of detail to use for which fact. It is an active, strategic decision to say, for instance, for this part of the work I keep branches 1, 2, 3 generic, but for branch 4 I need more granularity.

This should be something managed in parallel to the task at hand. The task is not "write the code"; it is "I want to write the code, and as I go through the various steps (design, implementation, test, doc), I dynamically adjust the level of detail to fit the task". It should be absolutely imbricated in the task. Not "I do the tests and then I decide if I should change my LOD"; more like "I do the test, so for the first one I can collapse this part of my knowledge but I need to expand this one, then for the second test...".

This is especially true for communication. Communication is determined by three things: the intent, goal, strategy; the person receiving the communication; the medium used. This is true when you are asked to write a wiki, a Slack message, an email, a doc, but also when we are chatting in session. Every time you ask me a question, you should manage the level of detail and decide what to include, to which level.

The outcome should be a skill or doc or text that is transverse to everything you do. It will de facto be loaded for every single task, so it needs to be powerfully structured and focused. (Mid-turn addition:) The skill should be self-contained and require no outside knowledge, such as knowledge about IntentGraph.

## Questions and answers
<!-- Lines 22-70 -->

**Q1 — Where it lives and how it loads.** Default offered: a versioned file in the tooling repo plus one import line in the global instructions.
> It should be a folder, not a file; the tooling repo is fine. I expect a document that is actionable and mostly self-contained, but also acting as an index for specific examples, use cases, edge cases. Those should live in the folder. Last, the folder should also hold the artifact that would be the input for a new session that wants to improve over the current effort. In terms of building blocks: you take a lot of material (existing, questions, outside research) and cook up an output. I want another future session to be able to redo what you did and improve it. So I want the "compiled binary" plus the "source code" plus the instructions and intent behind the source code. Once we have an actionable arm, it could be an `@import`, it could be an auto-loaded skill; to be decided.

**Q2 — Always-on budget.** Default offered: a core of roughly 120 lines plus a companion file.
> What to output is an exercise in level of detail in itself. You are thinking of a flat file; I see a short file (about 100 lines is classic) also pointing to further resources and details when required.

**Q3 — Overlap with existing rules** (global Interaction Protocol, tooling repo instructions, the user's personal communication instructions). Default offered: rewrite the Interaction Protocol to defer to the new doc.
> There will be repercussions for sure, but it is too early to think about it here, and you are giving a very partial list. It should be experimented on, not guessed. Once we have a one-pager LOD management and it auto-loads, launch a fresh subagent, give it a task, and check what it used from where, whether there was conflict or overlap, and so on.

**Q4 — Audience of the doc itself.** Default offered: written for any agent, voice-neutral.
> We are not producing a single thing. By definition the content intended for the agent should be geared for the agent. Space constraint will be extreme, so optimize for the agent, not the human. However I also want to keep track of the recipe, the ingredients, and so on; all of that should be explained in a clear format, human-OK. In general the master version should keep track not only of what the instructions are, but also why, and remember ruled-out instructions.

**Q5 — Names.** Default offered: keep "LOD", "height", reuse skeleton / lean / full.
> You can reuse vocabulary, but I would prefer a vocabulary optimized so that a fresh subagent seeing it for the first time is put in the right state of mind. Managing which implicit connections the subagent draws is very important. We want some connections (for instance to SADT), and we want to avoid confusing ones (for instance, to the anatomical skeleton). It is a subtle thing: each LLM has implicit connections, and we want to reverse-engineer that to our advantage.

**Q6 — Certainty as a first-class attribute, with "compression never raises certainty".**
> OK on the attribute. I would not say merging cannot raise certainty; I think that is wrong in practice and on theoretical grounds. You can become more certain, but not of the same fact. When you aggregate, the aggregated fact is lower resolution, and it can become very certain. I can be certain of who won an election without being certain of who individually voted for what. This might be too subtle, though.

**Q7 — Cross-links.** Default offered: one rule about links lifting on roll-up.
> You are not trying to re-implement IntentGraph. You are using IntentGraph to understand an underlying concept, and then deciding how to convey that concept in the best way to a subagent. A subagent will not have a formal link. What it could have, at best, is: facts a and b are linked somehow, and when we aggregate a into alpha, alpha might still be linked to b somehow.

**Q8 — Visibility of shaping decisions.** Default offered: silent unless contestable.
> Good question. This is about giving visibility, and possibly control, to the human. That is another strategic decision, and it depends on the criticality of the fact being handled, both in absolute terms and in the context of the work being done.

**Q9 — Explicit task tree as running state for long tasks.**
> Claude Code already ships with a mechanism for long-running tasks; I do not know how it works currently. If there is no hierarchy at all, we need to introduce some, and it would make sense. I am worried it would be too much instruction by default. It might be a specialized skill referenced by the main one.

**Q10 — Scope: include rules for acting and for reading input?**
> This is the crux. We want this philosophy enacted in all aspects of an agent's work. Deciding what to input, how to input it, what action to take, how to take it: essential.

**Q11 — Receiver archetypes** (five offered, software-flavoured).
> Again, two things, not one. The small file for agent usage will, by definition, be used by agents; you cannot assume the agent is building software. It might be preparing a presentation, a Slack message, whatever. The recipe, the code for how to come up with the instructions, is aimed at a session or a human specifically working on this, who has a lot of context and is high level.

**Q12 — Media and default budgets** (a table of word targets per medium).
> This question shows you have not understood the framework. As I said, the target is a strategic choice that depends on context, criticality, the person receiving the message, and so on. You could ground the process that should happen every time so it has higher chances to succeed, but it should not be a set number of words.

**Q13 — Intent taxonomy** (decide, inform, hand off, record, review, teach).
> What is this about? Give me more context; I do not understand.
Resolution taken by the author (pending confirmation): the purpose of a communication is named as a capability the receiver gains, with illustrative purposes rather than a fixed list (D11).

**Q14 — Adopt that compression algorithm as the general roll-up.**
> You are free to rewrite the algorithm, free to write a very short version and point to a more specialized, in-depth version with more edge cases. Do not think of the output as flat: a main short document, mostly self-sufficient, with provisions and pointers for edge cases and more detailed specialized skills.

**Q15 — Concrete failures observed.**
> That sounds like a separate project, where a session analyzes the logs of past sessions and finds the issues. Do not do it with your current context.

**Q16 — Verification.**
> Good practice is a separate subagent that reviews and evaluates the outcome; not Fable, use Opus. For proper evaluation in an experimental setting, I agree it is a good idea; how to do it in practice is more complicated because, to be efficient, you need to be able to judge quality by yourself without involving me. Table it for now.
