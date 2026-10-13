# Render notes: README, CLAUDE, allocation, philosophy

Slot output: `README.md` (119 lines), `CLAUDE.md` (20), `allocation.md` (475), `philosophy.md` (421).
Nodes rendered: 47 in allocation.md (39 `ALLOCATION*` + 8 `PIG-WEB-ALLOCATION*`), 40 in
philosophy.md (DATA, LOGIC, INTERACTION, TRANSVERSE subtrees), plus the philosophy `ROOT` as the
README thesis. A script checked that every in-scope uid appears and that every cited uid exists.
A second script checked every relative link and anchor in the four files.

## Where the graph did not allow a faithful render

1. **Recommendation for the read-visibility question is not in the graph.** `ALLOCATION.GUARD.3`
   carries only the recorded default and the fallback. The recommendation (B, database read
   functions) comes from `03_judge/J1_allocation/questions.md` and the J1 review. The README
   says so inline.
2. **SameSite and hosting questions.** The graph stores only the recorded default. The
   recommendation equals it, per `03_judge/J7_pig_logic/questions.md` and
   `03_judge/J9_pig_transverse/questions.md`.
3. **Fitting under 500 lines.** allocation.md (47 nodes, the matrix, the context table and one
   diagram) only fits with these choices:
   - TOC at H2 only, so H3 node sections carry no line comments;
   - no blank line between an intro sentence and its list;
   - the uid line placed directly after a closing list. In rendered markdown it joins the last
     bullet. In raw text it stays on its own line.

   philosophy.md has a TOC to H3; H4 nodes are not listed in it.
4. **Links into the stack files are file-level**, by branch name (for example "Postgres Data
   Tier"), not anchors. The other agent's headings were still changing.
5. **Context table.** The graph names placements by uid; the render uses node names.
6. **Threat map in `TRANSVERSE.SECURITY`.** Rendered with category names, without the OWASP
   Top 10:2025 codes (A01 to A10) the node uses.
7. **Seen, not mine.** `stack_defaults_logic.md` was 645 lines when checked, over the
   500-line maximum.
