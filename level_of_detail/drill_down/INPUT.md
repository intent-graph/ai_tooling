# Input — reading, searching, gathering at variable detail

Read this when the task needs knowledge you do not hold yet: a codebase, a document set, a data source, a conversation, a person's answer. Assumes `LOD_CORE.md`.

## Principle
<!-- Lines 7-9 -->

Acquire at the level the purpose needs and no finer. Your context window is the budget. Every full read of something you needed at label is volume you pay for on every later step.

## Outline first
<!-- Lines 12-18 -->

1. **Label**: what exists. Listing, file tree, headers, symbol index, table of contents, first lines. Cheap and wide.
2. **Claim**: what each thing says. A section, a docstring, a purpose paragraph, a search hit with a few lines of context.
3. **Full**: the whole file, the whole thread, the raw data. Only for the branch in focus.

Tool ladder, by level: list, tree, search for file names → label. Search with context, head, a table of contents, one section by line range → claim. The whole file → full.

## Procedure
<!-- Lines 21-27 -->

1. Name the purpose: what must you know to take the next step. Not "understand the codebase".
2. Build the source's outline at label. Note sizes: a large file gets its headers read, not its body.
3. Pick the branch the purpose needs and drill it to claim. Ask whether that answers. Stop when it does.
4. Drill to full only where you will act: edit, decide, quote.
5. Record what you rolled up. "Module X: parsing, 400 lines, not read" is a claim with a pointer; you can drill it later without re-orienting.

## Delegation is drilling elsewhere
<!-- Lines 30-34 -->

- Give the helper a view: its target in full, the surroundings at claim. Ask for a rolled-up return: a few claims, grounds on disk.
- Delegate when the branch is wide (many files, many hits) and you need the claim, not the members.
- Do not delegate what one search would answer.

## Reading people
<!-- Lines 37-41 -->

- The requester's one-line instruction is a claim; its children are unknown to you. Drill by reading their artifacts first, by asking second, by assuming never.
- Prior conversation is an outline too. Re-read the decision lines, not the whole thread.
- When the requester speaks at claim ("make it faster"), the leaves (which path, which measure, which threshold) are open until acquired.

## Certainty of what you acquired
<!-- Lines 44-48 -->

- What you read is grounded at the time of reading, and it decays. A pointer read last week is inferred now if the source moves fast.
- What a document says about an artifact is a claim about the artifact, not the artifact. Grounded only when checked against it.
- Counts, line numbers, and names you recall without re-checking are inferred.

## Edge cases
<!-- Lines 51-56 -->

- **A huge file with no headers.** Sample it (head, tail, a search for structural markers), build your own outline, then drill.
- **Opaque sources** (binary, encrypted, remote). The outline is the metadata; contents stay open until a tool reveals them.
- **Two sources disagree.** Both are inferred until a third settles it, ideally the artifact itself. Carry the disagreement as an open branch; do not pick silently.
- **Too many hits.** Roll the hits up by kind before reading any (which files, which patterns), then drill one representative per kind.
- **You already read it once.** Do not re-read to re-orient; read your own rolled-up record, then drill the one branch you need.
