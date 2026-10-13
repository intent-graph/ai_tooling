# Inputs from the JavaScript guideline

The JavaScript guideline keeps only principles core to JavaScript and offers its language-general
ones to this guideline, to import or decline. Paths are relative to this file; read, never edit.

- Package: `../../../javascript_guidelines/build/handoff/to_software_guideline/package.md`: 56
  principles sent whole and the general parts of 9 split ones, each with intent, constraints,
  design notes, epistemic state, claims with sources, the JavaScript rules that relied on it, and
  its links to the Python philosophy graph. Its section "Outline of what is sent" lists the nodes.
- Verdict table and borderline calls: `result.md` in the same folder.
- Evidence: `../../../javascript_guidelines/build/research/<slot>/result.md`; source register
  `../../../javascript_guidelines/build/audit/source_register.md`; source admission policy
  `../../../javascript_guidelines/build/plan.md`, section "Source admission policy".

## Fit with this guideline's skeleton (triage, not yet imported)

- Inside the current scope: DEPENDENCIES (admission, updates, incident response, layered
  controls) to OWNERSHIP; VERIFICATION (static baseline, test suite, fault detection, test
  stability, enforcement at the merge) to ASSURANCE; RUNTIME (measurement before belief, method)
  to ASSURANCE.PERFORMANCE; DEFENSE.SECRETS to TRANSVERSE. DEPENDENCIES.PUBLISH (the team as a
  supplier) has no node yet.
- Language-general code design: SUBSET, CONTRACTS.BOUNDARY and SHAPE, CONTROL.LIFECYCLE,
  STRUCTURE (information hiding, state in one place, effect-free importing, dependency
  direction, naming, paradigm by intent), DEFENSE.INJECTION. In scope by the maintainer's ruling,
  given in the JavaScript guideline session and relayed here: "i think code-design should be
  part of the disucsssion, as long as it's true for all languages. if there are things specific
  to js or especially important in js, they can stay here". Import the language-neutral
  statement only, no JavaScript examples or mechanisms; needs a code-design branch.
- The JavaScript guideline re-checks what it sent against "especially important in JavaScript"
  and keeps a JavaScript-framed principle for those, linking to the general node here. Its list:
  `kept_with_js_emphasis.md` beside the package, once written.

## Links back

The JavaScript guideline lists 49 planned links to this guideline's graph. Once the graph exists,
its graph id and node uids go to the maintainer so those links become inter links.
