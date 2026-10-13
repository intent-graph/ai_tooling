# Development Guidelines

Guideline knowledge bases an engineer or an agent consults mid-task. Each subfolder documents
itself: read its `README.md` (and `CLAUDE.md` where present) before using it.

## Guidelines
<!-- Lines 8-16 -->

| Folder | Scope |
|---|---|
| [software_development_guidelines/](software_development_guidelines/README.md) | Principles common to every stack: what a team writes, adopts or rents; how it knows each property holds and keeps holding; how it constructs, changes (CI/CD, deploy), operates (monitoring, recovery) and evolves the system; one IntentGraph |
| [python_guidelines/](python_guidelines/README.md) | Python development, from empty folder to production: a knowledge base in six levels of detail, plus two IntentGraphs |
| [cli_guidelines/](cli_guidelines/README.md) | Interface contract of command-line tools: flags, output, exit codes, help (clig.dev, Twelve-Factor, POSIX, GNU) |
| [web_architecture_guidelines/](web_architecture_guidelines/README.md) | Architecture of a JavaScript + Python + Postgres web application: who does what across database, backend and browser, then how each tier carries it out; two IntentGraphs |
| [javascript_guidelines/](javascript_guidelines/README.md) | Solid, maintainable, secure JavaScript in the browser and in Node, at the language level: a checked subset of the language, types, async, structure, defense, dependencies, verification, runtime; two IntentGraphs distilled from audited authoritative sources |

## How a guideline is distilled
<!-- Lines 19-34 -->

- **Take the max, not the average.** A guideline is a set of decisions between competing
  practices, not a summary of what sources say. For each point, choose the best practice for its
  purpose, the one the strongest arguments across all sources establish: the max of the
  collective, never its average, its most common answer, or a blend. "Best" is not "most
  demanding". Agreement among sources is evidence for that choice, never the verdict. Keep each
  weaker practice only with the condition under which it would be the best.
- **Structure from the purpose, not from the evidence.** Fix the functional hierarchy and the
  first decision of the domain with the maintainer before judging; attach the evidence to that
  structure afterwards.
- **Genuine trade-offs go to the maintainer**, as self-contained questions with a
  recommendation and a recorded default; everything else is decided and reviewed.

The full procedure, with the lessons of its first run, is in
[web_architecture_guidelines/build/RECIPE.md](web_architecture_guidelines/build/RECIPE.md).

## License
<!-- Lines 37-38 -->

CC BY 4.0, see [LICENSE.md](LICENSE.md).
