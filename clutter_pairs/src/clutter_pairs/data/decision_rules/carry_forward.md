# Decision rule: does carry-forward help?

The owner's hypothesis: lessons distilled from earlier loops make later images need fewer iterations. This file fixes,
before any rental, how the `carry_forward` report decides it (design/loops.md, "Measuring carry-forward"). The report
reads the parameters below and records this file's hash with its verdict.

**Arms.** Each subject is drawn into the `off` arm (no lessons in its requests) with probability `off_share`, into
the `on` arm otherwise, by a seeded draw recorded on its loop.

**Compared loops.** Per stage: the loops in waves after the stage's first lesson became active, excluding the loops
that are evidence of a lesson (they were selected for being hard).

**Verdict, per stage.** Carry-forward *helps* when all three hold:

1. the `on` arm's mean iterations to acceptance (accepted loops only) is lower than the `off` arm's by at least
   `min_difference`;
2. a one-sided permutation test of that difference (`permutations` relabellings, seeded) gives p below `alpha`;
3. the `on` arm's acceptance share is not lower than the `off` arm's.

It *does not help* when the difference is at most zero; otherwise, or with fewer than `min_loops_per_arm` accepted
loops in either arm, the verdict is *undecided*.

Slice 1 has about 17 clean and 50 clutter loops: the test can show a large effect or none.

```toml
off_share = 0.333
min_difference = 0.5
alpha = 0.1
permutations = 10000
permutation_seed = 1
min_loops_per_arm = 3
```
