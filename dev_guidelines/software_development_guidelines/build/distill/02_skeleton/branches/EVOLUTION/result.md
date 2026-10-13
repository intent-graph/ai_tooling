# Result: EVOLUTION branch refined below its L2 nodes

Pinned (word for word at every level):
- Nodes: 33 (EVOLUTION 1; L2 5; L3 27).
- Rows attached: 53 of 53; unattached: 0.
- Script (`check_branch.py`): PASS: all 53 routed rows attached exactly once, 0 unattached, uids follow the rules, every link target exists, MAINT rows named
- Routing objections: 3.

## L1 headline

The EVOLUTION branch is cut to 27 L3 nodes under its five L2 nodes (decision records 6, incremental change 6, debt and refactoring 5, decommissioning 6, keeping technologies few 4), all 53 routed rows attached once, and every node lists its competing positions without a verdict (grounded: the script ran and passed). Most of the 27 nodes hold one to three positions; the contested ones (record mutability, rewrite versus replace, taking debt, advisory versus compulsory deprecation, how firmly the stack is held, one store for several roles) are where judges will spend effort (inferred from the rows' agreement fields). Pinned: Nodes: 33 (EVOLUTION 1; L2 5; L3 27). Rows attached: 53 of 53; unattached: 0. Script: PASS: all 53 routed rows attached exactly once, 0 unattached, uids follow the rules, every link target exists, MAINT rows named. Routing objections: 3.

## L2 claims

Each claim: grounded (the file or script shows it), inferred (my reading of the rows), open (not settled by what I read).

- Pinned counts: Nodes: 33 (EVOLUTION 1; L2 5; L3 27). Rows attached: 53 of 53; unattached: 0. Script: PASS: all 53 routed rows attached exactly once, 0 unattached, uids follow the rules, every link target exists, MAINT rows named. Routing objections: 3. Grounded.
- DECISIONS (12 rows, 6 L3): content, threshold, form and storage, change of an accepted record, status and use in review, proposal versus record. Rows agree on short in-repository numbered records; the live disagreements are the threshold (record all significant decisions or only weighed ones) and immutable-with-supersession against a mutable living document, which the rows tie to document type. Grounded for the cut and rows; inferred that these two are the points judges must settle.
- INCREMENTAL (11 rows, 6 L3): step size and feedback, expand-migrate-contract, replacement versus rewrite, mass change and migration ownership, lifespan and consumer count, forward-only conventions. The one contested node is replacement versus rewrite (never rewrite, rewrite under conditions, incremental behind an interface, with big-bang open); L039 and L1017 state near-identical practice and sit together. Grounded for the cut; inferred for what is contested.
- DEBT (13 rows, 5 L3): what counts as debt, taking debt versus investing in quality, finding and inventorying, refactoring step size, timing and responsibility of repayment. Contested nodes: whether a little debt speeds work (L1020 against L1207, which records quality as not trading against speed), how to identify debt (tools against engineer survey), opportunistic against scheduled refactoring. L1020 is the only row where the origin says the payoff point is unproven. Grounded for the cut; inferred for the tensions.
- DECOMMISSION (11 rows, 6 L3): why remove, grounds to retire, announcing, support window, advisory or compulsory deprecation, carrying out. Announcing and window rows carry stack pointers (HTTP header fields, Kubernetes numbers). The one stated choice with two sides is advisory against compulsory (L1033); the window depends on consumer count (L1031). Grounded for the cut; inferred that interface compatibility rules sit in ASSURANCE.CONTRACTS (see the links).
- TECHNOLOGY (6 rows, 4 L3): adding as replacing, standing position per technology, how firmly the stack is held, one general-purpose store for several roles. L026, L1038 and L1229 are three near-equal statements of "keep few, replace rather than add"; L1040 (mandate, paved path, polyglot) and L1232 (one store, contested) carry the competing positions. Grounded for the cut; inferred for the grouping of the three near claims.
- Maintainer rows: L296 (EVOLUTION.INCREMENTAL.6) and L324 (EVOLUTION.DECISIONS.1) are named positions "Maintainer's codified practice (MAINT-S01)"; both rows read as agreeing with common practice. Grounded.
- Context variables: added only where a row says the practice moves with a condition, quoting the row id (for example CONSUMER_COUNT on L296 and L1031, DOCUMENT_TYPE on L232); none is a default team (MD-02). Grounded for the quotes; open whether judges keep them as variables or fold them into the "best when" conditions.
- Links: 50 link entries (Realizes to OWNERSHIP and ASSURANCE nodes, See to realization nodes, one Conflicts for L1026 against CHANGE_FLOW.REVIEW). All taken from the rows' see-also fields, none from the sources. Inferred; open whether judges want them as formal Realizes.
- Routing objections (3, none moved): L1236 to OWNERSHIP.STANCE, L1231 to OPERATION.RELIABILITY, L1007 to CHANGE_FLOW.REVIEW. Each is arguable, none is clear. Inferred.
- Open: no MD-03 index node exists in EVOLUTION, so no row was left unattached for restating content elsewhere; overlaps with data change (L1011, L1012, L1034) are held here by routing and linked, not restated. Grounded for the absence of split topics in `tree_l2.md`.

## L3 full

Source of truth: `branch.md` in this folder (tree, records, positions, links, routing objections). Condensed per node; certainty after each line (grounded: the record cites the row; inferred: my reading).

Pinned: Nodes: 33 (EVOLUTION 1; L2 5; L3 27). Rows attached: 53 of 53; unattached: 0. Script: PASS: all 53 routed rows attached exactly once, 0 unattached, uids follow the rules, every link target exists, MAINT rows named. Routing objections: 3.

Method (grounded): L3 cut top-down from each L2 intent in `tree_l2.md`, then the 53 rows routed to EVOLUTION.* in `routing.md` were read in full from the three ledgers and attached, one node each; no row edited, merged, moved or ranked. Positions state only what the rows record; where a row names no competitor the record says "single practice recorded".

EVOLUTION.DECISIONS (12 rows)
- .1 Content of a Record: L1001, L1002, L1009, L1233, L324. Positions: reasons and forces; alternatives, confidence and dissent; a fixed template; named forces as revisit trigger; maintainer position on stating the costs accepted. No competitor between them (they stack). Grounded.
- .2 Significance Threshold: L1004. Record every architecturally significant decision; only when weighed or no basis exists; skip workarounds. Condition: contributors and lifetime. Grounded.
- .3 Form and Storage: L1003. Single practice (short, numbered, in the repository beside the code). Grounded.
- .4 Changing an Accepted Record: L232, L1005. Immutable with supersession against mutable living document; assign by document type; origin agreement recorded as majority, contested and consensus. Grounded for positions; the rows name no single winner.
- .5 Status, Ownership and Use in Review: L1006, L1007. Single practices (status, owner, review; consult records in review). Grounded.
- .6 Proposal Versus Record: L1008. Separate proposal and record; one document for both; lightweight record only. Row certainty inferred.

EVOLUTION.INCREMENTAL (11 rows)
- .1 Step Size and Feedback: L1010, L1236. Releasable at every step; short feedback beats analysis. Grounded.
- .2 Expand, Migrate, Contract: L1011, L1012. Run the three steps; an unremoved migration is debt. L1012 inferred.
- .3 Replacement Versus Rewrite: L039, L1017. Never rewrite; rewrite when old costs more than new; incremental behind an interface; big-bang open. Contested (L1017). Grounded for positions; open whether any wins.
- .4 Mass Change and Migration Ownership: L1013, L1014. Tool-generated shards; central owner; consumers migrate themselves. Grounded.
- .5 Lifespan, Consumers and Cost of Change: L1015, L1016. Invest by expected lifespan; cost grows with consumer count, counter with consumer-capturing tests. Grounded.
- .6 Conventions Applied Forward Only: L296 (maintainer). Forward-only against retroactive rename; condition many consumers. Grounded.

EVOLUTION.DEBT (13 rows)
- .1 What Counts as Debt: L1018, L1021. Internal-quality liability; wider than code. Inferred for the full list in L1021.
- .2 Taking Debt Versus Investing in Quality: L1020, L1207, L1237, L1231. Little debt repaid promptly; no trade-off, payoff in weeks; prudent against reckless; simplicity as reliability. Contested; payoff point unproven (L1020, inferred).
- .3 Finding and Inventorying Debt: L1022, L1023, L1027. Tools; engineer survey; inventory with storage place open; maintainability measures. L1022 partly inferred, L1023 inferred.
- .4 Refactoring Step Size: L1024. Single practice. Grounded.
- .5 Timing and Responsibility of Repayment: L1019, L1025, L1026. Repay where changed; cost-comparison tidying; opportunistic; opportunistic plus capacity. Contested (L1026); one possible tension linked to CHANGE_FLOW.REVIEW. Grounded for Fowler's position, inferred for the alternative.

EVOLUTION.DECOMMISSION (11 rows)
- .1 Why Remove: L1028, L1029, L1041. Liability; unused code on production; ordinary work with owner and budget. L1041 inferred (synthesis).
- .2 Grounds to Retire: L1037. Stated grounds and record the decision. Record part inferred.
- .3 Announcing Retirement: L1030, L1032. Two stages (deprecation, sunset); actionable warnings plus machine-readable forms. Stack pointers: HTTP, Kubernetes. Grounded.
- .4 Support Window Before Removal: L1031. Tiered fixed windows against case by case; condition consumer count. Numbers Kubernetes-specific. Grounded.
- .5 Advisory or Compulsory Deprecation: L1033. Two sides, each with its condition. Contested. Grounded.
- .6 Carrying Out the Retirement: L1034, L1035, L1036. Verify users and restrict reversibly; owner and milestones; cover attached resources. Grounded.

EVOLUTION.TECHNOLOGY (6 rows)
- .1 Adding as Replacing: L026, L1038, L1229. Three near-equal statements (L026 and L1038 "state the same normative thing"). Grounded.
- .2 Standing Position per Technology: L1039. Adopt, trial, assess, hold with decision trail. Trail inferred.
- .3 How Firmly the Stack Is Held: L1040. Mandate; paved path; polyglot, each with its condition. Contested. Grounded.
- .4 One General-Purpose Store for Several Roles: L1232. One store until limits, against specialised system from the start (as the row's counter-condition). Contested; inferred, limits not verified from primary sources; stack restated neutral by the ledger, boundary DATA.

Routing objections (3, rows not moved): L1236 to OWNERSHIP.STANCE; L1231 to OPERATION.RELIABILITY; L1007 to CHANGE_FLOW.REVIEW. Inferred.

Open for the judges (nothing here is decided): which of the six contested nodes carry a context variable and which collapse to one practice; whether L026, L1038 and L1229 should count as one position or three (the ledger keeps them apart); whether the `See` links to realization nodes should be formalized.
