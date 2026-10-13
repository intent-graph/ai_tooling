# Fixes of the patch-14 review (second security gap round)

Scope: findings F01 to F17 of `build/review/patch14/result.md`, decided in `build/review/patch14/fix_plan.md`. Edited: `build/distill/skeleton.md`, `build/distill/claims_ledger.md`, `build/distill/decisions_for_review.md`, `build/research/14_secgap2/result.md` (claim corrections and two new claims), `build/assemble/bookkeeping_log.md`, `intent_graphs/README.md`; both graphs rebuilt by `apply_flags.py`, `build_batches.py`, `build_graphs.sh` (never `integrate.py`).

## L1 headline

All 17 findings are addressed: 16 fixed, 1 partly fixed (F05, one half is structurally impossible without placing a claim twice); none left unfixed. The CSRF node no longer contradicts itself or misreports OWASP, the Node fetch redirect rule is grounded on undici's own code, constraints are rules only again, and both graphs rebuild and validate (0 errors). Certainty: grounded for the gate results and the node text (I ran the gates and read the built nodes); grounded for the two new claim quotes (fetched, tool-extracted digests); inferred for the choice of owner when merging the redirect rows.

Pinned:
- Findings: fixed 16 (F01, F02, F03, F04, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17), partly fixed 1 (F05), not fixed 0.
- Claims added: SECGAP2-C91 (undici `manual` returns the actual response), SECGAP2-C92 (CSRF token requirements). Claims corrected: SECGAP2-C56, C69, C88, C68. Slot 14 is now 92 claims (consensus 34, contested 1, single-source 57).
- `ig-tool validate` js-philosophy: status ok, nodes 108, links 48, errors 0, warnings 0. js-defaults: status ok, nodes 287, links 162, errors 0, warnings 0.
- `check_ledger.py`: `claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0`. `check_complete.py`: `FAILS: 0`. `check_claims.py 14_secgap2`: `total: 92 claims {'consensus': 34, 'single-source': 57, 'contested': 1}; errors 0; restricted citations 133`.

## L2 claims

Format: finding, status, what changed, certainty. All grounded unless marked.

- F01 fixed: `ORIGIN.6.1` states token or signed double-submit as primary; `conflict:` text dropped; epistemic `known | unvalidated: token-first and the layering are stricter than both sources`. C69 rewritten (OWASP and MDN both list Fetch Metadata among the primary defences, consensus), C56 pointer corrected to SRC-394 section "How to treat Fetch Metadata headers on the server-side", G4 rewritten.
- F02 fixed: constraint 1 names token or signed double-submit only and forbids a Sec-Fetch-Site check alone; the check is a layer (constraint 2); the MDN case stays the only acceptable-when row; the former contested row DEFENSE-252 is now a fact row.
- F03 fixed: same-origin only; same-site only where the threat model trusts sibling subdomains (OWASP quote, tool-extracted); in C56 and the constraint.
- F04 fixed: C91 added (SRC-402, quote "On the web this would return an `opaqueredirect` response, but that doesn't make sense server side." tool-extracted), carried by the rule row of `INJECTION.6.4`; flag and G2 rewritten; `INJECTION.6.3` states the opaque response is browser behaviour; README line rewritten.
- F05 partly fixed: `INJECTION.6.4` rows and impl_pointers now reach SRVSEC-C35, C36, C37, SECGAP2-C86 to C91. `INJECTION.5.3`: SRVSEC-C45 and RUNSEC-C44 stay on the philosophy row DEFENSE-017 (a claim may be placed once), so they are not in its impl_pointers; they are named in its epistemic text and judge record and reached through the refines link, whose sentence now says so. Open for the maintainer (inferred).
- F06 fixed: `INJECTION.5.3` carries `unvalidated: ... strict form of sources that say could or if available`.
- F07 fixed: `SECRETS.2.1` carries an `unvalidated:` clause naming the weaker wording and the single-source rules (C04, C08, C15).
- F08 fixed: `exp` required on every token; flagged as stricter than ASVS 9.2.1 (inferred reading of the OWASP REST sentence, kept as in the review).
- F09 fixed: `HOST.3.1` says "reject", not "sanitize"; the setHeader fact is in design notes, constraint 1 is now the validators call; flag for the three single-source rules.
- F10 fixed: facts, CVE notes and version ranges of `INJECTION.1.4`, `.5.4`, `.6.4`, `SECRETS.2.2`, `HOST.3.1` moved to claim-less fact rows DEFENSE-270 to DEFENSE-277 (design notes, dated). Version floors that are the rule itself (Handlebars, EJS, jsonwebtoken, fast-xml-parser) stay in constraints.
- F11 fixed: intents of `INJECTION.1` and `INJECTION.5` widened; `SECRETS.2` renamed "Cryptographic APIs and tokens" with a widened intent; no seventh L2.
- F12 fixed: redirect rule owned by `INJECTION.6.4` (DEFENSE-180 merged into DEFENSE-182, DEFENSE-181 moved there; `.6.3` keeps one fact); URL parsing owned by `INJECTION.6.1` (`DOM.2.3` keeps canParse caution, allowlist comparison; DEFENSE-139 is a rejected substring-test row); client file names owned by constraint 1 of `INJECTION.4.6`. Inferred: which rows to merge.
- F13 fixed: purpose-style intents for `INJECTION.4.4` and `SCREEN.3`, absence kept in epistemic_state; the pointer to the empty node removed from the `INJECTION.4.1` row. `4.4` stays undecided (settles with LC-01).
- F14 fixed: C88 names Proxy-Authorization only (the advisory impact sentence, fetched again, names both headers; the register restriction calls Authorization wrong; the claim explains it); constraint: keep the Node release current, `process.versions.undici` gives the version. Inferred (which reading wins).
- F15 fixed: C68 and `ORIGIN.2.1` positions gain MDN Clickjacking (SRC-378, quote tool-extracted); `conflict:` softened (ASVS requires the directive, silent on a fallback); G3 updated; "quote not obtained (C68)" flag dropped since C68 now has a quote.
- F16 fixed: `ORIGIN.6.3` carries `unvalidated: facts-only source, rule inferred, blog wording not re-confirmed`.
- F17 fixed: C92 added (SRC-394 sections "Synchronizer Token Pattern" and "Transmitting CSRF Tokens in Synchronized Patterns", quotes tool-extracted) and placed as a MUST on `ORIGIN.6.1`.

## L3 full

### Files and rows changed

- `build/research/14_secgap2/result.md`: C56, C68, C69, C88 rewritten; C91, C92 appended after C90; L1 counts (92; consensus 34, contested 1, single-source 57; grounded 82), contested-topics lines, L2 clusters and the cross-slot gap note updated.
- `build/distill/claims_ledger.md`: 699 rows (was 691 plus review changes: -1 merge, +9 new, ledger header "Rows:" line and a merge note updated); 644 rows carry 700 claim ids, 55 are claim-less. Rows reworded: 139 (role rejected), 160, 181 (node moved), 182 (claims SRVSEC-C35, C37, SECGAP2-C90, C91), 196, 202, 203, 207, 212, 214, 215, 223, 228, 231, 236, 238, 239, 249, 250, 252 (role fact), 259, 267. Rows added: 269 (C92), 270 to 277 (claim-less facts). Row 180 merged into 182.
- `build/distill/skeleton.md`: node rows, judge records of `ORIGIN.6.1`, `ORIGIN.2.1`, `INJECTION.6.3`, `.6.4`, `HOST.3.1`, `SECRETS.2.1`, `DOM.2.3`, rename of `SECRETS.2` (row and judge heading), links 87 and 107 reworded, header note.
- `build/distill/decisions_for_review.md`: G1, G2, G3 rewritten in place, G4 replaced ("no longer a contested topic"), G8 added (review fixes), slot header count 92.
- `intent_graphs/README.md`: defaults epistemic counts (76 known alone, 179 with unvalidated or conflict; other classes unchanged), ledger count 699 rows and 700 claims, "Not covered" fetch line.
- `build/assemble/bookkeeping_log.md`: one entry for the row moves.

### Source checks done in this run (tool-extracted digests, not raw page text)

- SRC-402 undici `lib/web/fetch/index.js`: the `manual` branch sets `response = actualResponse` under a comment "NOTE(spec): On the web this would return an `opaqueredirect` response, but that doesn't make sense server side." (grounded, digest).
- SRC-394 OWASP CSRF sheet: "Allow `same-origin`. Treat `same-site` as allowed only if your threat model trusts sibling subdomains" (under "How to treat Fetch Metadata headers on the server-side"); tokens "Unique per user session. Secret. Unpredictable (large random value generated by a secure method)" and "A CSRF token must not be leaked in the server logs or in the URL" (digest; the first token sentence is the digest's wording of the sheet's list). One sentence of the sheet says a token should not be carried in a cookie for the synchronizer pattern; C92 does not claim it (a signed double-submit cookie is a different pattern).
- SRC-368 advisory: impact sentence names Authorization and Proxy-Authorization; patched 5.28.4 and 6.11.1; workaround fetch or disable maxRedirections (digest). Conflicts with the register restriction; C88 follows the restriction and says why.

### Gate outputs (verbatim)

`python3 build/distill/check_ledger.py`:
```
claims in: 700; placed: 700; missing 0; duplicated 0; unknown 0
ledger rows by graph: {'js-philosophy': 121, 'pig-js-defaults': 578}; by role: {'rejected': 61, 'fact': 171, 'decision': 419, 'acceptable-when': 37, 'deferred': 11}; skeleton nodes: 395
```
`python3 build/assemble/check_complete.py` (report, last lines): js-philosophy nodes 108, intra 48, inter 23, ledger_rows 121, impl_pointers 118, constraints 75; pig-js-defaults nodes 287, intra 162, inter 111, ledger_rows 578, impl_pointers 582, constraints 381; then
```
FAILS: 0
```
`python3 build/research/check_claims.py 14_secgap2` (without NOTE lines):
```
14_secgap2: 92 claims {'consensus': 34, 'single-source': 57, 'contested': 1}
total: 92 claims {'consensus': 34, 'single-source': 57, 'contested': 1}; errors 0; restricted citations 133
```
`ig-tool validate -m intent_graphs/intent_resources.yaml`: js_philosophy `status: ok, nodes: 108, links: 48, errors: 0, warnings: 0`; js_defaults `status: ok, nodes: 287, links: 162, errors: 0, warnings: 0`.
`python3 build/assemble/apply_flags.py`: `{} nodes changed: 0` (my explicit flags already satisfied the rule). `build_batches.py`: problems [], decision_nodes_without_record [].

### Open and judgment calls

- F05 (5.3): to put SRVSEC-C45 and RUNSEC-C44 into its impl_pointers the claims would have to move off the philosophy principle `DEFENSE.INJECTION.5` or be placed twice; both rejected by the plan's rule. Recommendation: leave as is. Inferred.
- `INJECTION.6.3` is now a node with one fact and no constraint, a consequence of "one owner per rule" with the owner on 6.4; if that reads badly, the alternative is to keep the general ASVS rule (C35) on 6.3 and let 6.4 state only the Node options. Inferred.
- The row text of DEFENSE-249 and 250 is stricter than claims C55 and C56 (which state the sources); the strictness is flagged in the node's epistemic_state, per the principle of `build/review/fix_plan.md`.
- Claim C07 (exp "where tokens grant API access") was left as the source-side claim; only the rule row was tightened (F08).
- Public-repository hygiene: `check_complete.py` scans graphs and `build/assemble/` for absolute or home paths and private names: 0 matches.
