# Fix plan for the patch-14 review findings

Decisions by the orchestrator on each finding of `result.md` (same folder), F01 to F17 of its
`## L2 claims`; evidence in its `## L3 full`. The principle of `../fix_plan.md` ("Principle for
every fix") applies: max, not average; strict forms allowed, their weakness visible in
`epistemic_state`.

- **F01, F02, F03** apply as the review proposes. `ORIGIN.6.1`: primary defence is a token or a
  signed double-submit cookie; a `Sec-Fetch-Site` check is a mandatory additional layer; the MDN
  case stays the only acceptable-when row; `same-origin` only, `same-site` only when the threat
  model trusts sibling subdomains (stated as the condition). Drop the `conflict:` text; state
  `known | unvalidated: token-first is stricter than both sources`. Correct claims SECGAP2-C69
  and SECGAP2-C56 in the claim table (wording and section pointer), and the matching G4 text.
- **F04** add the undici `manual` passage of SRC-402 as a new claim in
  `build/research/14_secgap2/result.md` (next free id, quote tool-extracted), ground
  `INJECTION.6.4` on it, and state in `INJECTION.6.3` that the opaque-redirect response is
  browser behaviour; update G2 and the README line.
- **F05** add the grounding claim ids to the ledger rows and `impl_pointers` of `INJECTION.5.3`
  (SRVSEC-C45, RUNSEC-C44 and any other claim the rule rests on) and `INJECTION.6.4`
  (SRVSEC-C35, SRVSEC-C36, SECGAP2-C86 to C89 and the new F04 claim). A claim still owned by
  another node stays there; link the nodes rather than placing a claim twice.
- **F06, F07, F09, F16** add the `unvalidated:` clauses the review names; F09 also: "reject"
  not "sanitize", the setHeader fact to design notes.
- **F08** require `exp` on every token, flagged `unvalidated: ASVS says if present`.
- **F10** move facts, CVE notes and version ranges from constraints to design notes as dated
  evidence.
- **F11** no seventh L2 under DEFENSE: widen the intents of `INJECTION.1` (code from strings and
  template engines) and `INJECTION.5` (data-only parsing, XML external entities included), and
  rename `SECRETS.2` to "Cryptographic APIs and tokens" with its intent widened.
- **F12** one owner per rule (`INJECTION.6.4` owns the redirect rule, `INJECTION.6.1` owns URL
  parsing, one constraint for client file names in `INJECTION.4.6`); the others link to it.
- **F13** purpose-style intents for `INJECTION.4.4` and `DEPENDENCIES.SCREEN.3` (what the node is
  for), the absence stays in `epistemic_state`; `INJECTION.4.1` states the rule it can state
  (never a raw string prefix) without sending the reader to an empty node.
- **F14** reconcile SECGAP2-C88 with the SRC-368 restriction (name both headers only if the
  advisory does; otherwise Proxy-Authorization); constraint: upgrade Node to get the bundled
  undici fix, check `process.versions.undici`.
- **F15** add MDN Clickjacking (SRC-378) to G3 and to `ORIGIN.2.1`'s positions; soften
  `conflict:` (ASVS requires the directive and is silent on a fallback).
- **F17** add the token requirements from SRC-394 to `ORIGIN.6.1` (unique per session,
  cryptographically random, never in a URL, a GET or a log), from claims; extract them as new
  SECGAP2 claims if none exists.

Rebuild and gate exactly as `../../patch/brief_patch.md` step 5 says (never `integrate.py`),
plus `python3 build/research/check_claims.py 14_secgap2` after claim-table edits.
