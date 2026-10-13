# Discovery brief: shared by every stage-1 slot

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`.
Your task message gives the absolute root, your slot and your area.

## Read first

- `build/plan.md`, sections **Goal**, **Boundary with sibling guidelines**, **Source admission
  policy** (all of it: tiers, the six gates, standing rules), **Research areas** (your row and
  your siblings' rows), **Maintainer decisions**. Use the line-number table of contents.
- Nothing else is required. Do not read the web-architecture build except to check a boundary.

## Goal of this stage

Find the **candidate sources** for your area that are likely to pass the admission policy, and
record enough about each for an independent auditor to admit or reject it. **You do not extract
claims.** A later stage reads admitted sources in full.

Open each candidate (fetch it) far enough to confirm: it exists at that URL, who wrote it, when
it was last updated, and which sub-topics of your area it actually covers. Do not trust a search
snippet for any of these.

## What to look for

- **Every sub-topic of your area** (your row in Research areas) needs at least one T1 candidate,
  or an explicit gap saying what you searched.
- **Primary first.** For each sub-topic, find the origin: the spec section, the runtime doc, the
  paper, the maintainer's own text. If you meet a derivative (a talk summarizing a paper), list
  the origin, not the derivative.
- **Authorities that disagree.** If two admissible sources take opposite positions, list both
  and say so: later stages need every position.
- **Restricted candidates.** Popular style guides or vendor material that the policy admits only
  for positions or facts: list them, labelled `expect-restricted`, with the restriction.
- **Do not list T4.** Instead, keep a tally of what you dismissed on sight, by category (for
  example "SEO tutorials 14, unattributed Medium or dev.to posts 9, listicles 6, Stack Overflow
  5"). That tally is evidence the filter ran.

Aim for 15 to 35 candidates. Fewer, all admissible, beats more padded with weak ones.

## Candidate format (L3 of your result)

One row per candidate:

- `id`: `<AREA>-K<nn>`, area code from your task message.
- `title`; `author or body`; `standing`: the checkable fact that makes the author authoritative
  on this topic (for example "TC39 delegate, co-champion of the proposal", "Node.js TSC member",
  "first author, USENIX Security 2019").
- `url`: the URL you fetched; `fetched`: yes, or failed with the error and the alternative copy
  you tried.
- `date`: publication or last-update date, or the spec edition or software version.
- `kind`: spec | official-doc | paper | book | style-guide | maintainer-writing | research-blog |
  advisory | dataset.
- `proposed tier`: T1 | T2 | T3, with `expect-restricted: <restriction>` when it applies.
- `gates`: one line, your self-check against G1 to G6; name any gate you are unsure of.
- `covers`: the sub-topics of your area it would ground.
- `boundary`: a sibling area or sibling guideline, when it sits on a boundary.

## Result file

Write `build/discover/<your slot>/result.md` with three sections, each readable alone:

- `## L1 headline`: one sentence on how well authoritative sources cover your area, with its
  certainty; then the `Pinned:` block.
- `## L2 claims`: one line per sub-topic: its best candidates by id and tier, and whether it has
  a T1. Then disagreements between candidates, one line each. Then gaps.
- `## L3 full`: the candidate table, then the dismissed-on-sight tally, then the searches you ran
  (queries, one line each).

Mark each L2 line grounded (you fetched and checked it), inferred, or open. Pin, word for word at every level: the number of candidates by proposed tier; every sub-topic
with no T1 candidate; every failed fetch on a T1 candidate.

## Rules

- Public repository: no absolute or home paths, no names of private projects, employers or
  clients, in anything you write.
- Write only inside your slot folder. Never commit, never `git push`.
- Stay inside your area; if a source serves a sibling area as well, list it in yours with
  `boundary: <sibling>`, once.
