# LOGIC branch review: result

The adversarial review of the judged LOGIC branch: `../J3_phil_logic/` (stack-neutral, 8 nodes) and `../J7_pig_logic/` (JavaScript + Python + Postgres, 31 nodes, 30 judged). Findings in full: `review.md`. Each level below reads alone.

## L1 headline

The LOGIC verdicts are sound in structure and faithful to MD-01, MD-02 and MD-03, with no blocking finding. Seven major findings must be fixed before the graphs are built:
- the read-visibility fallback B is dropped;
- reads in autocommit cannot carry the actor;
- the duplicate-key rule breaks on multi-phase payments;
- a foreign mutation runs inside the request, against ACT.3;
- `SameSite=Lax` is decided on usability, a force the branch says it does not serve;
- MFA is required but never verified on a delegated login;
- the maintainer row L530 (error codes, override flag) is missed.

Pinned:
- Findings: blocking 0, major 7, minor 12.
- Major: M1 read-visibility fallback B dropped (J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6); M2 autocommit reads cannot carry the actor read functions need (J7 ENFORCE.2); M3 concurrent-duplicate rule wrong for multi-phase keyed operations (J7 EXPOSE.3 against PROCESS.2); M4 foreign mutation inside the request against ACT.3's forbidden column, inherited from ACT.2 (J7 PROCESS.2); M5 SameSite=Lax decided on a force the branch says it does not serve (J7 SECURE.2); M6 MFA required but never verified on delegated logins (J7 SECURE.4, SECURE.5); M7 MAINT row L530 missed: error codes and the override flag for blockable rules (J7 EXPOSE.2, SECURE.1).
- Verdicts against the doctrine: J3 0 and J7 0, both confirmed; none contradicts a MAINT row; J7 under-weighs L530 (M7) and does not cite L587, which supports its EXPOSE.3.
- Questions: J3 none, agreed. J7 none: agreed on framework, login delegation, upload path, version location and limiter state; disagreed on SameSite (decide by max or raise it, M5). Inherited read-visibility question: kept open with J1's default in both units, but without J1's fallback B (M1).
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully in both units; J1 placements realized, except the ACT.3 tension in M4, which J1 itself carries.

## L2 claims

- **What holds.** Both units realize J1's placements without re-deciding them. MD-03 holds throughout: one function call per operation, the actor asserted, the backend's share limited to policy, workflow and external calls. MD-01 holds: no row security, backend checks kept. MD-02 holds: the description is always in sync, the origin is recorded per project, a CI gate catches drift. The J7 nodes refine J3's principles without contradicting them. The owned-row counts are right (28 and 133). The max rule is applied well in several places: MFA required, egress proxy required, no download before a clean scan, transitions as custom methods.
- **Open question kept open, incompletely (M1).** Both units record J1's default A, with the shared specification and shared denial tests. They omit B ("acceptable when a per-user read rule must hold for two or more backends"), and they do not mark ENFORCE.3, SECURE.1 and PROCESS.6, which change if the maintainer answers B. J1's B condition already holds in MD-03's default context, so J1's owner should reword it.
- **Correctness of the stack mechanics (M2, M3).**
  - Read functions read the actor from a transaction-local setting (L566, MAINT). Reads in autocommit lose that setting, so a read that applies a rule needs a short read-only transaction.
  - Atomic-phase payments commit the key before any outcome exists. A concurrent duplicate then has nothing to replay, so it needs 409 and a lock with an expiry (L546), not a wait.
- **Placement tension (M4).** J1's ACT.2 allows in-request atomic phases; its ACT.3 forbids foreign effects inside the request. J7 follows ACT.2 and reports zero conflicts. The 202 path through a worker satisfies both placements.
- **Forces applied inconsistently (M5).** Lax is chosen for the session's usability, while the same branch requires MFA on the ground that usability is not its force. The doctrine's test points one way or the other: if the force counts, raise the choice as a question; if it does not, Strict is the max. The claim that Strict protects only safe requests is incomplete: the cookie draft calls Lax a "speedbump" against attacker-opened navigations.
- **Enforcement left to the provider's word (M6).** With delegated login, "MFA required" holds only if the backend requests and checks `acr` or `amr` (OpenID Connect Core: the client "SHOULD check" `acr`).
- **Doctrine under-weighed (M7).** L530 grounds the mapping from function errors to problem types (which J7 marks inferred) and adds an override flag for blockable rules. No node says who may set the flag, so as written a client could bypass a blockable rule.
- **Minor (12).** Retries on 40001 and 40P01 at any isolation level; the upload signature check; challenges in front of agents; closed request schemas during deploy skew; `/v1` from the start; the job claim through a writer function; the Django read layer and OpenAPI production (Django Ninja is a candidate to verify); list reads filtered in the statement; agent affordances; `no-store` wording; self-run OIDC servers; citing L587.

Pinned:
- Findings: blocking 0, major 7, minor 12.
- Major: M1 read-visibility fallback B dropped (J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6); M2 autocommit reads cannot carry the actor read functions need (J7 ENFORCE.2); M3 concurrent-duplicate rule wrong for multi-phase keyed operations (J7 EXPOSE.3 against PROCESS.2); M4 foreign mutation inside the request against ACT.3's forbidden column, inherited from ACT.2 (J7 PROCESS.2); M5 SameSite=Lax decided on a force the branch says it does not serve (J7 SECURE.2); M6 MFA required but never verified on delegated logins (J7 SECURE.4, SECURE.5); M7 MAINT row L530 missed: error codes and the override flag for blockable rules (J7 EXPOSE.2, SECURE.1).
- Verdicts against the doctrine: J3 0 and J7 0, both confirmed; none contradicts a MAINT row; J7 under-weighs L530 (M7) and does not cite L587, which supports its EXPOSE.3.
- Questions: J3 none, agreed. J7 none: agreed on framework, login delegation, upload path, version location and limiter state; disagreed on SameSite (decide by max or raise it, M5). Inherited read-visibility question: kept open with J1's default in both units, but without J1's fallback B (M1).
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully in both units; J1 placements realized, except the ACT.3 tension in M4, which J1 itself carries.

## L3 full

### Inputs read

- `../../target_hierarchy.md`, `../../maintainer_decisions.md`, `../J1_allocation/allocation_matrix.md` (whole); in `../J1_allocation/records.md`: GUARD.3 to GUARD.6, ACT.1 to ACT.3, DB_API, TYPE_CHAIN; `../J1_allocation/questions.md` (Q1).
- Under review, whole: `../J3_phil_logic/` and `../J7_pig_logic/` (`result.md`, `records.md`, `questions.md`).
- Ledger (`../../02_skeleton/claims_ledger.md`): every MAINT row listed with its owner. In full: L023, L031, L033, L034, L229, L242, L270, L276 to L278, L307, L311, L324, L331, L338, L344, L346, L410, L420, L421, L423, L434, L495, L515, L516, L530, L546, L557, L566, L587, L589, L599, L640, L652, L655, L661. Owned-row counts per branch counted from the owner column.
- Sources fetched: draft-ietf-httpbis-rfc6265bis (SameSite Lax limits); OpenID Connect Core 1.0 (`acr`, `amr`, `acr_values`); the Django Ninja front page (Pydantic, OpenAPI generation). No research result (L3) was opened: no doubtful row needed it.

### Method

Each node was checked for: hedging or averaging; grounding and certainty words; consistency with J1, with MD-01 to MD-03, between the two units and across sibling links; a stronger position in the evidence that was missed; verdicts against the maintainer doctrine; and whether each question, raised or not raised, was a genuine trade-off.

### Findings

The full findings, with evidence and fixes, are in `review.md`. In brief:

| id | severity | node | issue | fix |
|---|---|---|---|---|
| M1 | major | J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6 | J1's fallback B omitted; verdicts that flip under Q1-B unmarked | add B's "acceptable when"; add a flip line per node; J1 to reword B's condition |
| M2 | major | J7 ENFORCE.2 | autocommit reads lose the transaction-local actor (L566) | reads needing the actor run in a short read-only transaction through the wrapper |
| M3 | major | J7 EXPOSE.3 vs PROCESS.2 | wait-then-replay fails for atomic-phase operations | key row with recovery point and lock with expiry; 409 with `Retry-After` mid-flight (L546) |
| M4 | major | J7 PROCESS.2 | in-request foreign mutation against ACT.3's forbidden column | atomic phases in a worker behind 202; in-request only under a stated condition; route ACT.2/ACT.3 to J1 |
| M5 | major | J7 SECURE.2 | Lax decided on usability; incomplete security claim | raise as a question (recommended) or Strict by max; drop the "only safe requests" claim |
| M6 | major | J7 SECURE.4, SECURE.5 | MFA not verified on delegated login | request and check `acr` or `amr`; step-up with `max_age` |
| M7 | major | J7 EXPOSE.2, SECURE.1, ENFORCE.1 | L530 (MAINT) missed; override flag unguarded | ground the mapping on L530; the override is authorized by policy and audited |
| m1 to m12 | minor | see `review.md` | retries, upload signature, agent challenges, skew and closed schemas, `/v1`, job claim writer, Django read layer and OpenAPI, list filtering, agent affordances, `no-store` wording, self-run OIDC, L587 | one-line fixes in `review.md` |

### Verdicts against the doctrine

- J3: 0 against, confirmed. It owns no MAINT row; L527, L584 and L596 are applied as J1 placed them.
- J7: 0 against, confirmed. L605 is adopted as the max; L516, L517, L604 and L566 are applied. Under-weighed: L530 (M7). Not cited: L587 (m12).
- The max rule sides with the judges on: MFA required; egress proxy required; the uploader gate before a clean scan; Active Record narrowed; no view as a contract. It does not side with SameSite=Lax as argued (M5).

### Verdicts on the questions

- J3, none raised: agreed. MFA is decided by the max rule, because usability is not the LOGIC role's force; its cost lands on INTERACTION, which can see it in the record. Full JSON hypermedia is rightly settled by MD-02.
- J7, six considered and not raised:
  - framework: agreed, with the m7 gap to close;
  - login delegation: agreed, with M6 and m11;
  - upload path: agreed;
  - version location: agreed, with m5;
  - limiter state: agreed (settled by POSTGRES_FIRST and CACHE_STORE);
  - SameSite: disagreed (M5). Its own Forces line names a force the node serves, so by the doctrine's test it is a question, unless that force is dropped and Strict is decided.
- Inherited Q1 (read visibility): kept open in both units at J1's default A and marked awaiting maintainer, as required. The record is incomplete without B and the flip lines (M1).

### Nodes found sound

The one-line list is in `review.md`, "Nodes found sound": all 8 J3 nodes (two with a fix: M1, m9), and 14 of the 30 judged J7 nodes (5 roll-ups and 9 leaves; PROCESS.6 and EXPOSE.4 carry only a one-line fix, M1 and m10). The other 16 J7 nodes carry a finding.

### For the graph builder

- Do not build SECURE.2, EXPOSE.3, PROCESS.2 or ENFORCE.2 from the current text until M2 to M5 are resolved.
- M1's flip lines and M7's override rule are additions; they change no decided default.
- M4 needs J1's owner too: ACT.2 and ACT.3 disagree in J1's own records.

Pinned:
- Findings: blocking 0, major 7, minor 12.
- Major: M1 read-visibility fallback B dropped (J3 LOGIC.SECURE; J7 SECURE.1, ENFORCE.3, PROCESS.6); M2 autocommit reads cannot carry the actor read functions need (J7 ENFORCE.2); M3 concurrent-duplicate rule wrong for multi-phase keyed operations (J7 EXPOSE.3 against PROCESS.2); M4 foreign mutation inside the request against ACT.3's forbidden column, inherited from ACT.2 (J7 PROCESS.2); M5 SameSite=Lax decided on a force the branch says it does not serve (J7 SECURE.2); M6 MFA required but never verified on delegated logins (J7 SECURE.4, SECURE.5); M7 MAINT row L530 missed: error codes and the override flag for blockable rules (J7 EXPOSE.2, SECURE.1).
- Verdicts against the doctrine: J3 0 and J7 0, both confirmed; none contradicts a MAINT row; J7 under-weighs L530 (M7) and does not cite L587, which supports its EXPOSE.3.
- Questions: J3 none, agreed. J7 none: agreed on framework, login delegation, upload path, version location and limiter state; disagreed on SameSite (decide by max or raise it, M5). Inherited read-visibility question: kept open with J1's default in both units, but without J1's fallback B (M1).
- Maintainer decisions: MD-01, MD-02, MD-03 applied faithfully in both units; J1 placements realized, except the ACT.3 tension in M4, which J1 itself carries.
