# Drill down — when and how to go finer

Read this when a branch needs more resolution: to decide, to build, to explain, or because it is open or critical. Assumes `LOD_CORE.md`.

## When to drill
<!-- Lines 7-21 -->

Signals that a claim hides structure you need:
- Its one line joins distinct things with "and", "also", "with": "validate signatures and compare bodies and classify discrepancies".
- Its grounds sprawl across unrelated concerns (speed, safety, format). Judge by cohesion, not by count.
- It maps to several separate places: files, teams, systems, sources.
- Its grounds describe distinct phases or mechanisms.
- It is open or inferred and the purpose hinges on it.
- The receiver will act on the members, not on the claim.

When not to drill:
- The claim is atomic: one capability, one resolution, one place, one sentence without "and".
- Many grounds, one purpose: ten normalization rules are one claim.
- The finer detail is not where the purpose or the risk is. Drilling every branch equally is not choosing either.
- The purpose is already served at this height.

## How to partition
<!-- Lines 24-31 -->

1. Cluster the grounds: by place, by sub-capability, by phase when phases are genuinely distinct.
2. Each cluster becomes a child with its own claim and its own certainty. Typically two to six children; one child means you did not split. That is the outline's structure; how many of them you *show* in one place is a separate decision (`ROLL_UP.md`: one to four claims to a receiver). Orthogonal: no fact sits under two children. Together they cover the parent; none reaches beyond it. As in SADT, the child diagram has exactly the parent box's boundary.
3. Migrate the grounds downward: local evidence goes to the child it supports; cross-cutting constraints stay on the parent; the parent keeps the reason for the split.
4. Rewrite the parent as the roll-up of its children ("achieves X through A, B, C"), still readable on its own. Test: can a reader understand what the parent is without opening the children? If not, the parent is wrong, not the children.
5. Re-derive the parent's certainty from the children (invariant 2).
6. Relations: check each pair of new children (feeds, requires, conflicts with, refines) and each child against related branches elsewhere. Note the relation on the child; the parent keeps the coarser one.

## Drilling by acquiring
<!-- Lines 34-40 -->

Drilling down often means you do not hold the children yet. You must read, run, measure, or ask.
- Decide first which child you need and at what level; acquire only that.
- Acquire at the cheapest level that answers (`INPUT.md`).
- If acquisition fails or is unavailable, the child is open. Say so. Do not fill it with a plausible line (invariant 3).
- Asking a human is acquisition too: one shaped question (`COMMUNICATION.md`), batched with its siblings.

## Naming children
<!-- Lines 43-45 -->

Children are named as things (capabilities, components, claims), not as steps: "cache lookup", not "look up the cache". The outline is a resolution hierarchy, not a procedure. Order of execution is a detail of one child, never the structure of the parent.

## Edge cases
<!-- Lines 48-53 -->

- **The parent was procedural** ("first A, then B, then C"). Re-express it as what the whole achieves; the sequence becomes a note on the children.
- **Temporary mess is allowed.** A node overloaded before you split it, a stub child before you fill it. Mark it ("open: split pending", "stub") so nobody mistakes it for done.
- **Cascading.** A change on one child that forces changes two or three branches away means the outline is miscut: duplication, or a hidden dependency. Fix the cut instead of chasing the cascade.
- **A shared piece under two children** (a library both services call through, a step two processes share). The clean tree wants it as its own child; the receiver may think in the two children. Fold it into both and name it once, and say you did; a partition bent for the receiver is fine, a hidden one is not.
- **Over-drilling.** If you find yourself at full on a branch nobody will act on, roll it back up. Depth you did not need is volume you will carry on every later step.
