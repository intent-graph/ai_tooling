# Principles that came back to the JavaScript guideline with a JavaScript emphasis

For the session that writes the software development guideline. Four nodes of the JavaScript philosophy graph
(`js-philosophy`, now 56 nodes) were restored after the first cut sent them to you. The maintainer's rule: the general
statement of each principle belongs to your guideline; what is specific to JavaScript or especially important in it stays
here. Each restored node states why the principle matters more in JavaScript, never the principle itself, so you still own
and ground the general principle. Names below are as in `package.md`.

Planned link, for each row (graph not built yet; also listed in `intent_graphs/README.md` section 3): the JavaScript node
`refines` the general principle in your graph. When your graph exists, create it with your node as the target.

| uid (JavaScript guideline) | name there | general principle it emphasizes (as in package.md) | why it matters more in JavaScript |
|---|---|---|---|
| `SUBSET.NUMBERS` | One number type, stated limits | "Stated numeric limits" | everyday arithmetic has one numeric type, a 64-bit binary float, so counts, identifiers and amounts share its precision and range and lose exactness silently beyond them |
| `SUBSET.STATE` | Immutability is stated, not assumed | "Distinguished immutability" | a fixed binding does not freeze its value, a freeze reaches one level and fails silently outside strict code, and some array methods mutate in place, so the lock is only as deep as the mechanism |
| `CONTRACTS.BOUNDARY` | Boundary parse is the only attestation | "Boundary contract" and "Validate at every trust boundary" (one node covers both) | types are erased before run time and outside data arrives with no run-time type, so the parse at the boundary is the only place a value earns its shape |
| `DEFENSE.CODE` | Strings become code in many ways | "Strings never become code" | many doors turn a string into running code (eval, the Function constructor, string arguments to timers, template engines, the vm module), all with the caller's privileges; template injection reaches the server |

Notes for you:

- **uids.** `SUBSET.NUMBERS`, `SUBSET.STATE` and `CONTRACTS.BOUNDARY` reuse the uid of the sent node. `DEFENSE.CODE` is new: the
  sent node was `DEFENSE.INJECTION.1`, whose parent `DEFENSE.INJECTION` stays with you, so the restored node sits directly under
  `DEFENSE`.
- **Claims.** Two claims left the `deferred` list and are placed on `DEFENSE.CODE`: `RUNSEC-C14` (its text names the JavaScript
  injection sinks and rests on MDN pages that call them injection sinks) and `SECGAP2-C31` (level js-principle, template
  injection). They remain in your package's claim tables; if you ground "never build code from strings" in your graph, cite
  `RUNSEC-C14` or a language-neutral source, the JavaScript guideline now holds it on its node. Every other claim of the four
  principles (`LANG-C29`, `STRUCT-C66`, `TYPES-C27`, `TYPES-C29`) stays deferred to you.
- **Links re-created here** (so drop them from your candidate list in `package.md`, "Removed links"): `SUBSET.STATE` to
  `SUBSET.FAILURE`; `CONTRACTS.BOUNDARY` to `CONTRACTS.STATIC.1`; `CONTRACTS.STATIC.2` to `CONTRACTS.BOUNDARY`;
  `STRUCTURE.STATE.2` to `SUBSET.STATE`; `SUBSET.VISIBLE` to `CONTRACTS.BOUNDARY`; `DEFENSE` to `CONTRACTS.BOUNDARY`;
  `DEFENSE.PROTOTYPE.2` to `DEFENSE.CODE`; and the Python link `CONTRACTS.BOUNDARY` refines `DEFENSIVE`. The defaults rules
  `PIG-JS.SUBSET.NUMBERS`, `PIG-JS.SUBSET.MUTATION.1`, `PIG-JS.CONTRACTS.BOUNDARY`, `PIG-JS.DEFENSE.INJECTION.1`, `.1.3` and
  `.1.4` link to the restored nodes now, so they no longer need a link to your principle; the other 43 planned links stand.
- **Left with you.** Everything else in the package: the siblings of these four (`CONTRACTS.BOUNDARY.2` to `.4`,
  `DEFENSE.INJECTION` and its other children, `DEFENSE.SECRETS`, and the rest) stay sent, each with a reason in
  `recheck/result.md`. Open calls where the opposite is defensible are listed there.
