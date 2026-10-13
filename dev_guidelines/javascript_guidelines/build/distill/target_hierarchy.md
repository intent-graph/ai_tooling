# Target hierarchy and selection rule

Status: decided by the maintainer. In the maintainer's words: "I dont want you to bring me the
internet average, aka avg(all sources). I want you to do max(all sources). It's ok to make
choices and pick the best." The judge record is carried over from the web-architecture
guideline (`../../../web_architecture_guidelines/build/distill/target_hierarchy.md`).

## Functional hierarchy

The tree comes from what solid JavaScript must achieve, not from how the sources cluster.
Evidence (the claim tables of `../research/`) is attached to it afterwards.

**L0.** JavaScript code whose behaviour is predictable, whose changes stay cheap, and which
resists attack, in the browser and in Node. JavaScript is permissive and widely misused; with
strong principles it is made useful and safe by narrowing it to a checked subset.

**L1, in dependency order:**

1. **SUBSET**: which parts of the language to use and which to forbid, so that behaviour is
   predictable (strict semantics, modules, equality and coercion, numbers, immutability,
   classes and `this`, features to avoid and to prefer). Research slot 01.
2. **CONTRACTS**: make intent checkable, at build time by a type layer and at run time by
   parsing untrusted data at every trust boundary; shapes of functions and objects. Slot 02,
   API-design part of 04.
3. **CONTROL**: make time, failure and resources explicit (promises and async functions,
   cancellation and timeouts, error types and propagation, unhandled rejections, streams and
   backpressure, process lifecycle). Slot 03, lifecycle and streams part of 09.
4. **STRUCTURE**: organize code so that a change touches one place (modules and their
   dependency direction, side-effect-free imports, state, paradigm choice, naming). Slot 04.
5. **DEFENSE**: treat every input as hostile and every sink as dangerous (DOM sinks and Trusted
   Types, injection classes, prototype pollution, `eval`, ReDoS, deserialization, secrets).
   Slots 05 and 06.
6. **DEPENDENCIES**: third-party code runs with your privileges (selection and minimalism,
   lockfiles and install scripts, provenance, update policy; the framework choice as the
   largest dependency decision, with its candidate short list). Slots 07 and 10.
7. **VERIFICATION**: let machines check what people forget (lint rule sets, type checking and
   tests in CI, test strategy, gates). Slot 08.
8. **RUNTIME**: behave well under load and over time (performance claims that hold, memory,
   profiling and diagnosis). Performance and memory part of slot 09.

Both graphs share this L1 cut: `js-philosophy` holds the why (language-neutral where possible,
JavaScript-distinct where not), `pig-js-defaults` holds the concrete JavaScript rules under the
same branches.

## Selection rule: max, not average

For every node, the guideline states **the best practice for the purpose of the node's
branch**, the one the strongest arguments across all sources establish: the max of the
collective, never its average, its most common answer, or a blend; "best" is not "most
demanding" (maintainer correction: "it's nto the most demanding thing, it's the best thing. The
core idea is to not default to average."). The purposes: predictability for SUBSET, checkability for CONTRACTS,
explicit failure for CONTROL, locality of change for STRUCTURE, safety for DEFENSE, trust for
DEPENDENCIES, automation for VERIFICATION, measured behaviour for RUNTIME. Agreement among
sources is evidence for the judgment, never the verdict. Weaker practices stay only as
"acceptable when <condition>". **The build makes the choices**: contested topics, the
type-layer choice and the framework short list included, are decided by this rule, each with
its rejected positions and the condition under which each would win, so the maintainer can
overrule any of them. `undecided` is reserved for nodes where no admitted source supports any
position.

The max rule never overrides grounding: a demanding practice no admitted source supports is
not invented; it is recorded as open.

## Judge record (every node)

1. **Positions**: the competing practices, from the evidence (claim ids, source ids).
2. **Forces**: which purpose each position serves, and at what cost.
3. **Decision**: the max choice, with its grounds.
4. **Rejected**: each other position, the reason, and the condition under which it would win.
