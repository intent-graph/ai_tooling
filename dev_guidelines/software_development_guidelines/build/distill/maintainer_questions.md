# Questions for the maintainer, before judging

Status: open. Answer under each question, in your own words, at the line marked **Answer**.
Every question stands alone; none needs the others or any other file. Each ends with a
recommendation and what happens if it stays unanswered.

Where things stand: research is done (11 research slots, 482 claims from 264 sources, of which
106 are standards or official documentation and 103 recognized authorities), consolidated into
one ledger of 460 rows, and cut into a provisional skeleton of 170 nodes. Nothing is judged yet.
Cost so far: about 2.2M Sonnet tokens.

## Contents

1. [Should "how we know it holds" live apart from "how we do it"?](#1-should-how-we-know-it-holds-live-apart-from-how-we-do-it)
2. [Should "how the system changes over time" be its own branch?](#2-should-how-the-system-changes-over-time-be-its-own-branch)
3. [What team and project is "take the max" judged against?](#3-what-team-and-project-is-take-the-max-judged-against)
4. [Which topics beyond the six named ones are covered?](#4-which-topics-beyond-the-six-named-ones-are-covered)
5. [Reviews of the judged decisions: Opus or Sonnet?](#5-reviews-of-the-judged-decisions-opus-or-sonnet)
6. [Is the folder name final?](#6-is-the-folder-name-final)

---

## 1. Should "how we know it holds" live apart from "how we do it"?

**Situation.** The guideline is cut into branches:

- **OWNERSHIP** (decision): per capability, does the team write it, adopt it (a library or tool)
  or rent it (an external service)?
- **ASSURANCE** (decision): per property that must hold (correct behaviour, interfaces, data
  integrity, documentation in sync, security, performance, availability), which mechanism, at
  which stage, guarantees it: a type check, a test level, review, a CI gate, a production
  monitor.
- **CHANGE FLOW** (version control, review, CI, release, deploy), **OPERATION** (monitoring,
  alerting, incidents), **TRANSVERSE** (docs, security, config, environments) and
  **CONSTRUCTION** (code design, ruled in scope by you in the JavaScript guideline session): they
  carry out what the two decision branches decide.

Three topics therefore appear twice:

- Documentation: ASSURANCE holds *how we guarantee docs stay in sync* (generated from code, a CI
  drift check, a review rule); TRANSVERSE holds *how docs are written and organized*.
- Security: "which mechanism catches which threat at which stage" versus security practice.
- Data: "data stays correct through change" versus the migration procedure in CHANGE FLOW.

**Options.**

- **Keep the split.** Every "how do we know X holds" question is answered in one branch, side by
  side, so gaps are visible. Same shape as the web guideline, where you approved "who does what
  across tiers" as a branch separate from how each tier does it. Cost: about 20 extra nodes; a
  reader looks in two places, joined by links.
- **One home per topic.** Simpler to read; the assurance question for docs, security and data is
  scattered, which is where "make sure it stays in sync" tends to get lost.

**Recommendation:** keep the split.
**If unanswered:** kept, marked provisional.

**Answer:** : keep the split; but avoid duplication of information. It's fine to have one location being mostly an index

---

## 2. Should "how the system changes over time" be its own branch?

**Situation.** Some material has no natural home in the branches above: recording decisions
(decision records), changing a system incrementally, technical debt and refactoring, retiring
your own software, keeping the number of technologies small. The web guideline holds these in
an EVOLUTION branch. Here they sit in a provisional "design" node or are parked, because
technical debt was outside the six topics you named.

**Options.**

- **Add EVOLUTION as a top-level branch.** Gives technical debt, decommissioning and decision
  records a home ("keeps working" over years is mostly evolution) and lines up with the web
  guideline's branch, which can then link here. Cost: one light research slot on debt and
  decommissioning (about 150K Sonnet tokens) and one more branch to judge.
- **Leave it out.** The guideline stays on owning, assuring, delivering, operating and code
  design; these topics stay with the stack guidelines or nowhere.

**Recommendation:** add EVOLUTION.
**If unanswered:** these topics stay parked and unjudged; nothing is lost.

**Answer:** add evolution

---

## 3. What team and project is "take the max" judged against?

**Situation.** The rule is to pick, per point, the most demanding practice that best serves its
purpose. What is best depends on the context: mandatory two-person code review, release freezes
when reliability targets are missed, or a full staging environment are right for one team and
dead weight for another. In the web guideline a judge silently assumed "one backend owns the
database" while your reality is a database shared by several backends and BI; everything that
leaned on it had to be re-judged.

The skeleton defines 19 context variables, among them team size, criticality, regulation,
number of consumers of a service, rate of change, and share of code written by AI agents. Every
decision will say which value would flip it. The default is the case judged first.

**Options.**

- **Proposed default** (an inference from your workspace, not something you stated): a small
  team (a handful of engineers) runs several services in production on a shared database; AI
  coding agents write a large share of the code; the software is business-critical but not
  safety-critical; no heavy regulation by default.
- **A larger organization** as default: dozens of engineers, several teams.
- **A regulated context** as default: medical, finance, audit trails.

**Recommendation:** the proposed default, with regulation and team size as the main variants
every decision must address.
**If unanswered:** nothing is judged. This is the one question that blocks progress.

**Answer:** you are confusion what max means. it's nto the most demanding thing, it's the best thing.
The core idea is to not default to average.
it's a very generic principle, based on the aggregation of sources, the collective intelligence theory.
I dont knwo if we need to codify who writes teh code  etc
what we need to codify is the principles and the outcome. 
who cares if AI or human write teh code, what matters are the immuntables: the design was good, the testing was good, the review was trustworthy, etc

---

## 4. Which topics beyond the six named ones are covered?

**Situation.** You named six topics: sourcing tools, libraries and APIs; adopting versus writing
code; making sure things work and keep working; CI/CD; deploy; monitoring. You have since ruled
code design in, as long as it holds for every language (in the JavaScript guideline session);
it becomes the CONSTRUCTION branch. Research found more adjacent topics with no evidence gathered
yet. Each costs one Sonnet research slot (about 150K tokens) plus judging.

Mark each **in** or **out**:

- **AI coding agents as contributors**: how review, verification and ownership change when
  agents write the code. One public claim so far; your own practice has two (one sanctioned,
  tool-enforced path for an agent; for high-risk jobs the agent writes the script and a human
  runs it). *Recommended: in.*
- **Backup, restore and disaster recovery**: no research slot covered it at all, yet it is the
  last line of "keeps working". *Recommended: in.*
- **Security beyond process**: depth of security testing, security monitoring, privacy and
  retention. *Recommended: out for now, listed as deferred.*
- **Regulated contexts**: change control and audit trails. *Recommended: out, unless question 3
  makes regulation the default.*
- **Software that is not a hosted service**: mobile, data and ML pipelines,
  infrastructure-as-code. *Recommended: out for now, listed as deferred.*

**If unanswered:** only the six named topics plus code design are covered; the rest is listed
as deferred.

**Answer:**
do everything except regulated context and Software that is not a hosted service

---

## 5. Reviews of the judged decisions: Opus or Sonnet?

**Situation.** After a judge agent decides each unit (about ten units, one per branch area), a
separate agent reviews it adversarially: averaging instead of taking the max, verdicts not backed
by sources, inconsistency across branches, positions the judge missed. Your standing instructions
send reviews to a separate Opus agent, confirmed with you first; you also asked to run this work
on Sonnet, not at maximum effort. So far about 2.2M Sonnet tokens; the web guideline cost about
12M.

**Options.**

- **Opus for all reviews**: strongest at catching subtle averaging and missed positions, the web
  guideline's main failure. Roughly 1 to 1.5M Opus tokens.
- **Sonnet for all reviews**: a fraction of the cost; weaker scrutiny of Sonnet judges by Sonnet
  reviewers.
- **Mixed**: Opus reviews the two decision branches (OWNERSHIP and ASSURANCE), whose verdicts
  everything else follows; Sonnet reviews the rest.

**Recommendation:** 
**If unanswered:** Sonnet for all, your standing request for this run.

**Answer:** do the brunt of the work with sonnet, and have the sonnet agent flag things that are subutle, then an opus agent does teh final say

---

## 6. Is the folder name final?

**Situation.** Everything lives in `ai_tooling/dev_guidelines/software_development_guidelines/`
(public repository), holding one stack-neutral IntentGraph. The web and JavaScript guideline
sessions are waiting for a stable folder name, graph id and file path to turn their planned links
into real ones; renaming after they link is costly. Sibling folders: `python_guidelines`,
`cli_guidelines`, `web_architecture_guidelines`, `javascript_guidelines`.

**Options.** Keep `software_development_guidelines/`; or `engineering_guidelines/` (shorter,
vaguer); or `software_practice_guidelines/` (stresses practice).

**Recommendation:** keep `software_development_guidelines/`, graph id
`software-development-philosophy`.
**If unanswered:** kept, but the other sessions are not told it is stable until you confirm.

**Answer:** keep
