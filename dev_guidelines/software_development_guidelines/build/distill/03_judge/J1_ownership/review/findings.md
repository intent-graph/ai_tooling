# J1_ownership review: findings

Format: id | node | check | severity | what is wrong | proposed correction | evidence. Check numbers are those of `brief_review.md`. `fix` = clear and settled, the judge can apply it. `flag` = subtle or contestable, for the Opus pass. Row ids Lnnn are ledger ids; REG-nnn source register ids.

## fix

R01 | STANCE.4 | 6 context creep | fix | The Decision names "a published contract" as a costly-to-reverse structure; no row says so (L330 gives only a very large relational store; L038 and L1208 name nothing). | Delete "a published contract", or keep it and mark it inferred in Certainty. | L330 positions "(b) ... wins when changes to structure are costly (a very large relational store)".

R02 | STANCE.4 | 2 grounding | fix | Grounds call "cheap repair of wrong guesses" L038's own argument; L038 lists repair of wrong guesses as one of four costs, it does not call it cheap. The reconciliation stands, but on L330's own condition only. | Reword: L330 states the condition itself ("YAGNI wins when change is cheap; probable use wins when structure changes are costly"); drop the claim about L038's argument. F1 is thereby settled (reconciliation accepted; the maintainer confirmation remains a human step). | L038 statement; L330 positions.

R03 | SELECTION.2 | 2 grounding | fix | The "exit or migration plan" for spent novelty is attributed to REG-013 ("REG-013 itself admits", copied from L024/ADOPT-C05). The fetched page says to commit to migrating old functionality to the new system, which is not an exit plan from the new tool. | Keep the decision (a reversible entry is the reversibility force of P2/P3), cite it as inferred, and cite REG-013 only for documenting why existing tools cannot solve it and for the migration commitment. | Fetched REG-013: "Set clear expectations about migrating old functionality to the new system. The policy should typically be 'we're committed to migrating'."

R04 | SELECTION.3 | 3 missed position | fix | L007 states that a single-maintainer project "needs a compensating reason or an exit plan"; the Decision only tolerates single-author projects that are small, stable and replaceable. | Add: a single-maintainer component outside that case needs a recorded compensating reason or an exit plan. | L007 statement.

R05 | SERVICES.2 | 7 consistency, 3 missed position | fix | The Decision says provider-side API evolution (L353) is "held in ASSURANCE.CONTRACTS". Neither the skeleton ASSURANCE.CONTRACTS nodes nor J2 `judged.md` carry L353 (date-pinned versus major versions); the pointer is orphaned and F3's hand-off to J2 cannot happen. | State that L353 is kept here as a consumer-facing question (the consumer must know which promise the provider makes, the row's own wording) with P3a and P3b each best under its condition; drop the pointer unless J2's reviewer confirms placement. F3 settled. | L353 statement; routing lists L353 only under OWNERSHIP.SERVICES; J2 `judged.md` has no "date-pinned" or L353.

R06 | LICENCE.3 | 2 grounding | fix | L375 is carried as open ("boundary between linking and separate programs not read"). REG-188 (fetched) speaks to exactly this boundary. | Mark the "interface, not proximity" half grounded in part by REG-188 (pipes, sockets, command-line arguments are normally between separate programs; intimate exchange of complex internal data structures may make one combined work); keep "legal review where the boundary matters". F4 settled. | Fetched REG-188: "Pipes, sockets and command-line arguments are communication mechanisms normally used between two separate programs."; intimate data-structure exchange may make a combined work.

R07 | SELECTION.5 and LIFECYCLE.4 | 8 duplication | fix | Official sources over secure links, signed packages, and rebuild from verified source are stated in both nodes (L012/L013 and L062/L1243/L065). MD-03: one location. The SELECTION.5 provenance sentence ("...rebuild from verified source where binary provenance cannot be confirmed, applied there") is also garbled and sits beside LIFECYCLE.4's narrower rule (rebuild everything only for critical or targeted organisations). | Keep authenticity and provenance in SELECTION.5; in LIFECYCLE.4 keep only channel choice, mirror, recursion and removal, with a link; state the rebuild rule once (LIFECYCLE.4, with its criticality condition) and have SELECTION.5 point to it; rewrite the garbled sentence. | judged.md SELECTION.5 and LIFECYCLE.4 Decisions; L013, L065 rows.

## flag

R08 | CONTAINMENT.2 | 7 consistency | flag | "or a rented service" makes a wrapper the rule for every rented service, while CONTAINMENT.3 treats a third-party service with a standard interface (SMTP, SQL) as a plain attached resource. REG-186 says the layer is not suitable when there are no significant semantic differences. | Scope the rented-service clause to services whose model differs, that are volatile or single-vendor; standard-interface services are attached resources. | L068 positions (wrap wins "for external services" but "not wrap wins ... stable, standard interface"); fetched REG-186 "might not be suitable when ... no significant semantic differences".

R09 | LIFECYCLE.3 | 1 averaging, 7 consistency | flag | "Where verification is weak or deployment costly, strengthen the tests first rather than upgrade rarely" removes the condition under which P1b is best, while Rejected still states that condition. No row says to strengthen tests first. | Either state P1b as best under its row condition, or keep the prescription and mark it inferred and drop the rejected-condition wording. | L052 positions "upgrade only when there is need ... wins when verification is weak or deployments are costly and risk of change exceeds exposure".

R10 | LIFECYCLE.2 (F6) | 1 | flag | The resolution rule is deferred to "whichever the ecosystem's tool provides", which is not a decision; L047's own statement prefers a rule close to what the author tested (MVS), with newest-compatible plus lock best when a tool updates the lock. The rule only bites for ranged dependencies; with the exact pins the same node prescribes for deployables it is moot. | Opus to decide: scope the rule to ranged dependencies (libraries), prefer the author-tested rule where reproducibility outweighs automatic fixes, keep the outcome sentence. | L047 statement and positions.

R11 | LIFECYCLE.3 (F2) | 2 grounding | flag | Judge's description of REG-036 is confirmed (one author, 10 attacks), but the same page recommends "7 days minimum" and calls cooldowns "not a panacea"; "up to about two weeks" comes from the ledger statement and tool settings, and L1543 records the benefit as unmeasured. The Decision states the cooldown with no such caveat. | Keep the cooldown, add "benefit unmeasured, inferred" to the Decision sentence; Opus to confirm the length wording. | Fetched REG-036: 8 of 10 windows under a week; 9 of 10 stopped by 14 days; recommends 7 days; L1543.

R12 | STANCE.2 | 2 grounding | flag | "In this order: a platform built-in ... preferred over custom code" is ranked first on L310 alone (MAINT, REG-181, not citable; its stack is materialized views versus cache tables); no public row ranks built-in first, and the ordering itself appears in no row. Certainty says "grounded for L310". | Mark the ordering inferred, or word it as the lowest-ownership case of the same cost test without ranking. | L310 sources REG-181 only; L002 has no ordering.

R13 | STANCE.1 | 2 grounding | flag | The list of reasons that justify a layer (reuse, business-level verb, tunable query, integrity once) comes from L308 only (REG-181, stored-function doctrine); certainty "grounded" rests on the maintainer row plus an unfetched reading of public practice. | Mark the layer reasons as MAINT-grounded, grounded only for the dependency half. | L308 sources REG-181, "public practice read as majority".

R14 | LICENCE.2 | 6 context creep, 1 | flag | The licence lists in the conservative policy (MIT, BSD, Apache, ISC allowed; AGPL, SSPL, non-commercial prohibited) are one organisation's policy ("not a standard"); the Decision gives them as the shippers' policy. | Present the list as an example of a conservative policy; the decision is the written classes with a named decider. | L373: "Google's policy is one organization's choice, not a standard."

R15 | SERVICES.5 and SERVICES.1 | 2 grounding | flag | Normative claims with no source: assurance reports as evidence (L365, no source id), non-library tools same criteria (L378, composed), monitoring each service (L033, no source id), remedy versus loss (L347, not assessable). They sit in Decisions beside sourced ones. Certainty lines do say open or inferred. | Mark these sentences inferred in the Decision text so the graph build does not treat them as sourced. | L365, L378, L033, L347 certainty fields.

R16 | CONTAINMENT.1 | 2 grounding | flag | "Require a tested exit and an alternative for regulated or critical functions" generalises L075(b), which names financial entities and critical functions and rests on DORA text that was not read (REG-216 summaries). | Keep, but state "regulated (for example EU financial entities) or critical", certainty inferred for the requirement. | L075 certainty "inferred for DORA (primary text unread)".

R17 | LIFECYCLE.3 | 8 duplication | flag | Credential rotation after a compromise is stated here (L1544) and held in TRANSVERSE.CONFIG (L252); the Link says "also held". | One location: keep the lockfile-review and pin-to-earlier-version parts here and point to TRANSVERSE.CONFIG for rotation, or accept the overlap explicitly (MD-03). | L1544 see-also L252.

R18 | SELECTION.2 | 7 consistency | flag | The Decision makes proven technology the default for everyone; Context says organisations with experiment capacity may run standing rings and spend more novelty. The condition that moves the default is not in the Decision. | Put the EXPERIMENT_CAPACITY condition into the Decision sentence. | L024 positions (boring wins small, operations-heavy, long-lived; staged novelty wins with capacity and churn tolerance).

R19 | CONTAINMENT.2 (F5) | 2 grounding | flag | "Never store a vendor's types or identifiers in own data or public interfaces without an owned mapping" is worded as a MUST; L345 is inferred, "not assessable", and fetched REG-186 states no such rule (it covers translation at the boundary, validation, latency, upkeep). | Keep as inferred (the judge's recommendation), softened to "avoid ... unless a mapping the team owns exists"; Opus to confirm it stays a constraint. | L345 certainty inferred; fetched REG-186.

## Judge flags F1 to F6

- F1 STANCE.4: settled (reconciliation accepted on L330's own condition; see R01, R02). Maintainer confirmation stays a human step.
- F2 LIFECYCLE.3: carried as R11.
- F3 SERVICES.2: settled as fix R05 (the target of the hand-off does not exist).
- F4 LICENCE.3: settled as fix R06.
- F5 CONTAINMENT.2: carried as R19.
- F6 LIFECYCLE.2: carried as R10.

## Sources fetched

| source | claim checked | result |
|---|---|---|
| REG-028 Renovate pinning (T1) | pin apps, ranges for libraries, lock does not replace ranges (LIFECYCLE.2) | confirmed |
| REG-195 GitHub Actions hardening (T1) | full commit hash, audit source, read-only default token, no self-hosted runners on public repos (SERVICES.6) | confirmed |
| REG-188 GPL FAQ (T1) | linking versus separate program (LICENCE.3) | confirmed; stronger than the judge records (R06) |
| REG-186 Anti-Corruption Layer (T1) | when to use, cost, no rule on vendor types (CONTAINMENT.2) | confirmed, including that L345 is not stated as a rule |
| REG-036 cooldowns (T3) | one author, 10 attacks (LIFECYCLE.3) | confirmed; adds "7 days minimum" and "not a panacea" (R11) |
| REG-013 Choose Boring Technology (T2) | exit or migration plan admitted (SELECTION.2) | contradicted in part (R03): migration commitment, not an exit plan |

## Summary checks (rows the summaries stood for)

The judge's list of the 14 rows it opened is not recorded in `judged.md` or `result.md`, so the check was run on 17 decisions chosen from across all six L2 nodes, reading every cited row in the ledger: STANCE.1, .2, .3, .4; SELECTION.2, .3; LIFECYCLE.2, .3, .4; CONTAINMENT.1, .2; SERVICES.2, .4, .5; LICENCE.2, .3.

- Summaries that misled a decision: 0. The branch records matched the rows on positions, conditions and certainty.
- Differences found: L310's row says "vs common practice: contradicts" while the branch record says "read as contested" and the judge relies on the row's own "matches, not a contradiction" cross-reference (harmless, see R12 for the real weakness). L024's "REG-013 itself admits" is wrong in the ledger row itself, so it reached the judge through both the row and the summary (R03). Rows L040, L035, L078, L345, L365, L375 carry inferred or open certainty in the row and the branch record alike; the judge kept them (R12, R15, R19).
