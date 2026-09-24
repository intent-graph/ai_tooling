# Level of Detail — a transverse practice for agents

Everything an agent knows about a task is an outline of claims at several resolutions, not a flat list. At every step the agent chooses a view: which branches to hold or show at label, at claim, in full. This folder ships that practice as an agent-loadable core, its on-demand satellites, and the source material and recipe needed to improve it.

## Routing
<!-- Lines 7-14 -->

| You are | Load | Then |
|---|---|---|
| An agent doing any task, and this practice is loaded or pointed at | [`LOD_CORE.md`](LOD_CORE.md) | drill into [`drill_down/`](drill_down/) only when the core points you there |
| A session or human improving this artifact | [`build/README.md`](build/README.md) | then [`build/NEXT_SESSION.md`](build/NEXT_SESSION.md) for the reading order, the open questions, and the next experiment |
| Checking why something is the way it is | [`build/DECISIONS.md`](build/DECISIONS.md) | then [`build/ELICITATION_ROUND_1.md`](build/ELICITATION_ROUND_1.md) for the user's words |
| Changing a word | [`build/VOCABULARY.md`](build/VOCABULARY.md) first | then the agent-facing files |

## Functional hierarchy
<!-- Lines 17-26 -->

**Level 0** — every act of reading, thinking, acting, and communicating goes through a deliberately chosen level-of-detail view, re-chosen at every step.

**Level 1**
1. **Model** knowledge as an outline: facts, claims, height, certainty, informal relations.
2. **Set the view** per branch from purpose, criticality, certainty, receiver, channel; the budget is an output.
3. **Enact** it on input, thinking, action, communication.
4. **Show or hand over** the view decision to the human, proportional to criticality.
5. **Self-check** before anything leaves: heights vary, focus justified, lines grounded, receiver can act.

## Folder map
<!-- Lines 29-50 -->

```
level_of_detail/
├── LOD_CORE.md              the compiled, agent-facing core (about 100 lines)
├── drill_down/              agent-facing satellites, read on demand
│   ├── ROLL_UP.md           compression moves, certainty after roll-up, grounding pass, examples
│   ├── DRILL_DOWN.md        when a claim hides structure; how to partition; acquiring
│   ├── COMMUNICATION.md     purpose, receiver, channel; questions, status, records, decks, briefs
│   ├── INPUT.md             reading and gathering at variable detail
│   ├── ACTION.md            thin path first, verification at matching height
│   ├── TASK_OUTLINE.md      the view as running state across a long task
│   └── HUMAN_CONTROL.md     criticality axes, three modes of visibility and control
└── build/                   builder-facing source: why, how, what was ruled out
│   ├── README.md            what this folder is, where to start
│   ├── NEXT_SESSION.md      entry point for an improvement session
│   ├── DECISIONS.md         decision log with ruled-out alternatives
│   ├── VOCABULARY.md        terms to use, and terms not to use
│   ├── SOURCES.md           ingredients and what was taken from each
│   ├── RECIPE.md            the procedure to remake the artifact
│   └── ELICITATION_ROUND_1.md   the user's brief and answers
```

## Status
<!-- Lines 53-55 -->

Two review rounds by fresh Opus readers (round 1: 4 blocking, 8 major, 9 minor; round 2: 9 of 12 resolved, 0 new blocking, 3 major, 6 minor; reports not retained). All blocking and major findings applied; changes and declined items are logged in `build/DECISIONS.md` (D23–D42). An overlap experiment with the core loaded as standing instructions informed D43–D46 (see `build/DECISIONS.md`). The core is wired via one `@import` in the user's global instructions (D50); further overlap experiments and open questions are tracked in `build/NEXT_SESSION.md`.

## Relation to the rest of this repository
<!-- Lines 58-59 -->

The concept was understood through the intent-graph primers, and the Python knowledge base's LOD levels; the files here stand alone and use none of those tools' vocabulary. See `build/SOURCES.md`.
