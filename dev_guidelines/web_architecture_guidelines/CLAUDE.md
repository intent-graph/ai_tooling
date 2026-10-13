# CLAUDE.md — Web Architecture Guidelines

Navigation card for agents designing or reviewing a web application on JavaScript, Python and Postgres.

1. **Read [README.md](README.md) first**: thesis, default context, file map, the nine maintainer decisions, the marker conventions.
2. **Drill one file** for the question at hand:
   - who decides a responsibility, which copies are allowed, what would move it: [allocation.md](allocation.md#allocation-matrix), matrix first;
   - what a tier does, stack-neutral: [philosophy.md](philosophy.md#durable-data);
   - which mechanism on this stack: [data](stack_defaults_data.md#data-tier-overview), [backend security](stack_defaults_logic_security.md#backend-security-overview), [Python tier](stack_defaults_logic.md#python-tier-overview), [browser surface](stack_defaults_interaction.md#browser-surface-overview), [agent surface](stack_defaults_agents.md#agent-surface-overview), [transverse](stack_defaults_transverse.md#transverse-overview);
   - what a term means: [glossary.md](glossary.md).
3. **Query a node for its grounds.** Each section ends with a full uid. `PIG-WEB-*` uids live in `web_defaults.ig.yaml`, all others in `web_app_philosophy.ig.yaml`:
   ```bash
   ig-tool query -g intent_graphs/<file> --node <UID>       # intent, constraints, state, design notes
   ig-tool query -g intent_graphs/<file> --children <UID>
   ig-tool query -g intent_graphs/<file> --links <UID>      # --projection-links for cross-graph links
   ```
4. **Never load a whole graph file** into context; use `ig-tool tree` or `query`.
5. **Maintainer decisions** override every other source; never reopen one. A clause marked **Open** is left to the project or to measurement: decide it per project and record it.
6. **Certainty**: a clause marked "(inferred)" is derived, not sourced; say so when you rely on it, and query its uid for the grounds.
7. **Context check**: the decisions hold for the default context (shared database, one team, humans and agents as users). If the project differs, read [Context](allocation.md#context) and move only the placements its table lists.
8. **Changing the guideline**: edit the graphs first (`ig-tool node`, `link`, `apply`), validate with `ig-tool validate -g <graph> -m intent_graphs/intent_resources.yaml`, then re-render the markdown. Maintainer decisions in `build/distill/maintainer_decisions.md` override every other source.
9. **Out of scope**: code-level conventions, in `../python_guidelines/` and `../javascript_guidelines/`.
