# CONTROL branch decisions for review

No contested topic of `12_dissent` (16 topics) concerns CONTROL; the weighty choices below are
judgement calls under the max rule, each overridable by the maintainer. Certainty tags: grounded,
inferred, open.

## A. Weighty choices

**D1. A failure the program cannot repair ends the process; nothing resumes (rows CONTROL-011, 075, 078, 079).**
Decision: unhandled rejections throw by default in Node; uncaughtException is for synchronous
cleanup, then exit, then an external supervisor restarts; the monitor hook only logs.
Rejected: resuming after uncaughtException (Node docs: not safe), wins under no condition named by an
admitted source; the non-default `--unhandled-rejections` modes (SRC-079), no condition named.
Grounds: SRC-082, SRC-068 (history), SRC-079; grounded, single T1 source for C05, C37, C38.

**D2. Every promise is observed (019 to 022).** Decision: await, return or handle each promise;
void is not handling; no async callback where a void callback is expected; no promise as a condition.
Rejected: floating promises and void-as-handling, no condition named. Grounds: SRC-072, SRC-073
(typescript-eslint rule documents, restricted to what the rules report and their rationale; they do not
ground a preference for that tool), SRC-082, SRC-077, SRC-081; grounded, single T1 for the void and
condition rules.

**D3. Throw only Error instances (031).** Merges ASYNC-C18 and LANG-C45 (Google's position, used as a
position only). Rejected: strings and plain objects, no condition named. Grounds: SRC-074 (T1
restricted rationale), SRC-239 (T2 position); grounded.

**D4. Empty catch demoted to acceptable-when (035).** ASYNC-C21 rests only on Google's style-guide
position (SRC-239, "never evidence"). The no-silent-swallow rule itself is carried by the inter link to
python DEFENSIVE and by TYPES-C12 plus the channel rule C22, not by a decision row. Rejected: empty
catch with no reason; wins nowhere. Certainty: grounded as a position, the demotion is a judgement.

**D5. AbortSignal is the one cancellation and timeout primitive (041 to 049).** Rejected: assuming promises
cancel (refuted, row 003); reusing one controller (one-shot). AbortSignal.any: MDN says the combined
signal cannot say which source fired, Node sets the reason of the source that aborted; the sources are
compatible, not contested (noted in the claim). Grounds: SRC-057, SRC-055, SRC-066, SRC-261 (position
only); grounded, consensus.

**D6. Concurrent by default (025).** Rejected: sequential loops of awaits, wins when a later operation
depends on an earlier result (the claim's own condition). Concurrency limits, retry and backoff: no
admitted source (undecided node PROMISES.4.1). Grounds: SRC-056, SRC-246, SRC-075 (MDN's position); grounded.

**D7. setImmediate over process.nextTick (050).** Rejected: nextTick for general deferral (refuted by
Node docs). Single T1 source (SRC-071, "we recommend setImmediate in all cases"); grounded, single-source.

**D8. CPU work to workers; partitioning only as the weaker alternative (057, 059).** The condition for
partitioning (work that cannot move to a worker) is inferred: SRC-080's offloading recommendations are
excluded by its restriction, so the choice between them rests on SRC-069 and the restriction, not on
SRC-080. Certainty: inferred for the ordering of the two.

**D9. Server timeouts configured, requestTimeout never disabled on an exposed server (047).** The
do-not-disable rule is inferred from "0 disables"; default values read through a digest, not verbatim.
Rejected: unbounded slow connections, no condition named. Certainty: inferred for the rule, grounded
for the mechanism.

**D10. pipeline over pipe (069).** Rejected: pipe(), leaks the destination when the source errors; no
condition named. Single T1 source (SRC-196); grounded, single-source.

**D11. Duplicate and overlap handling (from 11_coverage).** Merged into one row each: O01
(ASYNC-C04 with RUNTIME-C40, SRC-082 alone suffices, SRC-079 text unreliable per G-L15), O03
(ASYNC-C23 with RUNTIME-C31), O04 (ASYNC-C55 with RUNTIME-C42), O07 (ASYNC-C18 with LANG-C45; TYPES-C12
kept as its own row), O17 (ASYNC-C26 with STRUCT-C53). O02 is split on purpose: ASYNC-C05 states the
principle on CONTROL.LIFECYCLE, RUNTIME-C37 states the Node rule on PROCESS.2; the integrator may merge
them under P5 if it prefers one row.

**D12. Folklore (9 beliefs, all refuted, all grounded):** missing return harmless (015), unhandled
rejections only warn (077), Promise.all cancels (027), promises cancellable (003), setTimeout(0) exact
(007), 0 ms timers (054), then on a resolved promise runs now (005), nextTick for deferral (053),
async/await slower (086, T2 history only, the present-day gap open). The 12_dissent confirmed and
restricted beliefs concerning other branches are not placed here.

**D14. Async functions over then chains (029, 086), single T2, dated.** Searched: claims of slot 03 and the register for style-guide positions, MDN guidance, lint-rule documents and ASYNC-C52. Positions found: V8 team 2018 advice to favour async functions and await (SRC-249, T2, restricted to history, used here as a dated position); MDN flat chains (SRC-075); async functions convert exceptions to rejections (SRC-056 via ASYNC-C07). No admitted source advocates chains over async functions. Decision: async/await by default; flat chains acceptable. Winning condition of the rejected position: a flat chain as the whole body, or a nested chain confining a catch (inferred from MDN); the speed belief wins only on an admitted current measurement (open). Certainty: grounded for the positions, inferred for the explicit-failure argument and the condition. ASYNC-C52 moved from `rejected` on PROMISES.5 to `decision`; the belief is a claim-less rejected row.

**D13. Shutdown contract left to the sibling (082, 083).** `boundary: web-architecture` per routing.
The Node API side stays here (11_coverage: "the Node API side stays"); proposed planned boundary link
P6. If the integrator prefers `deferred`, change both rows' role.

## B. Single-source decisions

Each decision row below rests on one source (one T1 page, or one T2 paper); the epistemic state of its
node says `unvalidated`. 39 decision rows plus 2 acceptable-when, 8 fact and 2 rejected rows are
single-source. Decision rows, with the ledger row and claim:

| row | claim | source and tier | note |
|---|---|---|---|
| 011 | ASYNC-C05 | SRC-082 T1 | hooks are last resort |
| 014 | ASYNC-C15 | SRC-075 T1 restricted | MDN editorial position |
| 016 | ASYNC-C11 | SRC-059 T1 restricted | rule behaviour |
| 018 | ASYNC-C13 | SRC-245 T2 restricted | formal model |
| 020, 022 | ASYNC-C03, C17 | SRC-072, SRC-073 T1 restricted | rule documents; truthiness of objects is language semantics, not stated in the digest |
| 023 | ASYNC-C08 | SRC-056 T1 | |
| 026 | ASYNC-C54 | SRC-060 T1 restricted | detection heuristic |
| 028 | ASYNC-C53 | SRC-246 T2 restricted | 20-repository sample |
| 029 | ASYNC-C52 | SRC-249 T2 restricted | 2018 position of the V8 team, dated |
| 032 | ASYNC-C24 | SRC-065 T1 | |
| 033 | TYPES-C12 | SRC-052 T1 | |
| 037 | ASYNC-C20 | SRC-058 T1 | |
| 039, 040 | RUNTIME-C32, C33 | SRC-081 T1 | |
| 044 | RUNTIME-C06 | SRC-196 T1 | |
| 046 | ASYNC-C34 | SRC-067 T1 | |
| 047 | ASYNC-C55, RUNTIME-C42 | SRC-078, SRC-190 T1 | do-not-disable inferred |
| 048 | ASYNC-C30 | SRC-055 T1 | |
| 049 | RUNTIME-C34 | SRC-081 T1 | |
| 050 | ASYNC-C36 | SRC-071 T1 | |
| 055, 056 | ASYNC-C39, C41 | SRC-080 T1 restricted | mechanism only; C41 inferred |
| 060, 063 | ASYNC-C44, C47 | SRC-063, SRC-069 T1 | |
| 064 | ASYNC-C48 | SRC-064 T1 | |
| 067, 068 | RUNTIME-C02, C03 | SRC-184 T1 restricted | mechanism only |
| 069, 070, 073 | RUNTIME-C05, C08, C10 | SRC-196, SRC-197 T1 | |
| 078, 079, 080, 081 | RUNTIME-C37, C38, C35, C36 | SRC-082 T1 | |
| 082, 083 | RUNTIME-C39, C41 | SRC-082, SRC-190 T1 | C39 must-exit rule inferred |
| 084, 085 | RUNTIME-C17, C43 | SRC-188, SRC-190 T1 | C17 wording from digest |

Evidence that would validate them: a second independent T1 or T2 source per claim; none is
required by the max rule, only the epistemic tag.

## C. Undecided nodes

PROMISES.6 is decided (D14); three nodes remain undecided.

| node | question | evidence that would settle it |
|---|---|---|
| PIG-JS.CONTROL.PROMISES.4.1 | Concurrency limits, retry, backoff | An admitted T1 or two T2 sources on bounded concurrency and retry with jitter (11_coverage G-M08: LC-10 RFC 9110 Retry-After, a T1 candidate; LC-11 Amazon Builders' Library is T3 and cannot make a node known) |
| PIG-JS.CONTROL.ERRORS.2.1 | Operational versus programmer errors, detail shown to callers | An admitted source on error classification (11_coverage G-M07: LC-08 Pacheco not located; G-M16 for disclosure, owned by DEFENSE) |
| PIG-JS.CONTROL.SCHEDULING.2.1 | Yielding to the main thread in browsers | An admitted browser-support statement for scheduler.yield (11_coverage G-M09: LC-12 MDN Scheduler.yield is a T1 candidate, not admitted) |

Open notes (not nodes): return await inside try/catch is not evaluated by SRC-246 (ASYNC-C53);
ECMA-262 and HTML Standard clause text were not read by the extraction slots (11_coverage G-M04), so
mechanism cells rest on MDN and Node docs; async iteration and structured concurrency (G-L02) have no
claim.
