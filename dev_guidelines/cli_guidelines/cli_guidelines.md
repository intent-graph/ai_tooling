# CLI Design Best Practices: A Hierarchical Level-of-Detail Reference

Summarises and paraphrases clig.dev (CC BY-SA 4.0, https://clig.dev), 12-Factor CLI Apps,
POSIX Utility Conventions and GNU Coding Standards; short quotes are attributed inline.

## TL;DR
<!-- Lines 8-11 -->
- Good CLI design means building programs that are **human-first yet composable** — intuitive for people to learn and use interactively, while remaining predictable enough to be scripted, piped, and automated; the authoritative consensus comes from clig.dev, the 12-Factor CLI Apps, POSIX Utility Syntax Guidelines, GNU Coding Standards, and Eric Raymond's Unix philosophy.
- The guidelines partition cleanly into ~11 major functional domains (arguments/flags, help/docs, output, errors, interactivity, configuration, composability, command structure, robustness, security, distribution) plus cross-cutting concerns (testing, accessibility, telemetry), each decomposable into concrete, atomic, mostly language-agnostic rules.
- Where sources diverge: POSIX favors strict short-option syntax while GNU adds long options and intermixed argument ordering; clig.dev updates the traditional "rule of silence" toward more human feedback; and consent models for telemetry are contested — GitHub CLI v2.91.0 (April 22, 2026) enabled opt-out-by-default telemetry with no first-run prompt and drew immediate criticism (419 points/302 comments on Hacker News within 24 hours per byteiota; critical coverage from The Register). These tensions are flagged so the graph can represent both traditional and modern positions.

## Key Findings
<!-- Lines 14-19 -->
- **A single abstraction hierarchy works cleanly.** Level 0 (mission) → Level 1 (functional domains) → Level 2 (sub-capabilities) → Level 3 (atomic guidelines). The domains are orthogonal enough to partition without major overlap.
- **The sources strongly agree on fundamentals:** stdout for data / stderr for messages; exit 0 on success and non-zero on failure; `-h/--help` and `--version` as universal flags; TTY detection to decide on color/prompts/progress; XDG Base Directory spec for config; flags-over-args; and never requiring interactivity.
- **The biggest philosophical shift** is from "machine-first" Unix tradition (rule of silence, terse output) to clig.dev's "human-first" stance (say just enough, give feedback, suggest next steps) — but both agree output must remain machine-parseable when piped.
- **Security guidance has hardened recently:** clig.dev now explicitly says do *not* read secrets from flags *or* environment variables, preferring files/stdin/sockets — a stronger stance than the 12-Factor App's original "config in env."
- **Telemetry is contested.** Best practice per most community sources is opt-in with transparency and a preview/log mode (GitHub CLI supports `GH_TELEMETRY=log`, which prints the JSON payload that would be sent to stderr instead of sending it). GitHub's 2026 opt-out-by-default rollout in the gh CLI illustrates the risk of the opposite approach.

## Details
<!-- Lines 22-22 -->

### LEVEL 0 — MISSION
<!-- Lines 25-39 -->
**Design command-line programs that are a pleasure for humans to use and reliable for machines to compose.** Every guideline below serves this dual mandate: empower interactive human users through discoverability, feedback, consistency, and empathy, while preserving the composability, predictability, and scriptability that make CLIs powerful building blocks. (Consensus of clig.dev "Philosophy"; Unix philosophy; 12-Factor CLI Apps.)

The philosophical pillars (clig.dev), which inform all lower levels:
- **Human-first design** — if a command is used primarily by humans, design for humans first, shedding machine-first baggage.
- **Simple parts that work together** (Unix "Rule of Composition": *design programs to be connected to other programs*; McIlroy's dictum, from Doug McIlroy, E.N. Pinson & B.A. Tague, "Unix Time-Sharing System: Foreword," *The Bell System Technical Journal*, 8 July 1978, pp. 1902–1903: "Expect the output of every program to become the input to another, as yet unknown, program").
- **Consistency across programs** — follow existing patterns so knowledge transfers; the terminal's conventions are "hardwired into our fingers."
- **Saying (just) enough** — balance between too little output (looks hung) and too much (drowns signal). Updates the Unix "Rule of Silence."
- **Ease of discovery** — comprehensive help, examples, suggested next commands.
- **Conversation as the norm** — interaction is a back-and-forth; guide the user through errors and multi-step operations.
- **Robustness** — both *be* robust (handle bad input, idempotency) and *feel* robust.
- **Empathy** — make the user feel you are on their side.
- **Chaos** — break conventions only with intention and clarity of purpose (Jef Raskin, *The Humane Interface*: "Abandon a standard when it is demonstrably harmful to productivity or user satisfaction").

---

### LEVEL 1.A — ARGUMENTS, FLAGS & OPTION SYNTAX
<!-- Lines 42-89 -->

**Rationale:** The argument surface is the primary contract between user/script and program; consistency here makes tools guessable and future-proof.

**1.A.1 — Terminology & structure**
- Distinguish *arguments/operands* (positional, order-significant, e.g. `cp SRC DST`) from *flags/options* (named, order-independent, e.g. `-r`, `--recursive`). (clig.dev)
- Options may take an *option-argument* (`--file foo.txt` or `--file=foo.txt`). Support both the space-separated and `=`-joined forms. (clig.dev, GNU)

**1.A.2 — POSIX Utility Syntax Guidelines (foundational short-option rules)** — from IEEE Std 1003.1-2017 / The Open Group Base Specifications §12.2. Note there are **14** guidelines, not 13:
- G1: Utility names should be between two and nine characters.
- G2: Utility names should use lowercase letters and digits only, from the portable character set.
- G3: Each option name should be a single alphanumeric character; `-W` is reserved for vendor options; multi-digit options should not be allowed.
- G4: All options should be preceded by the `-` delimiter.
- G5: One or more options without option-arguments, followed by at most one option that takes an option-argument, should be accepted grouped behind one `-` (e.g. `-lst` = `-l -s -t`).
- G6: Each option and option-argument should be a separate argument (with historical exceptions).
- G7: Option-arguments should not be optional.
- G8: When multiple option-arguments follow one option, present them as a single argument separated by commas or blanks.
- G9: All options should precede operands on the command line.
- G10: The first `--` that is not an option-argument marks the end of options; following args are operands even if they begin with `-`.
- G11: The order of different options relative to one another should not matter (unless documented mutually exclusive); repeated options with option-arguments are interpreted in the order specified.
- G12: The order of operands may matter, determined on a per-utility basis.
- G13: For file operands, `-` should mean only standard input (or standard output when context implies output), or a file literally named `-`.
- G14: If an argument can be identified per G3–G10 as an option or an option group, it should be treated as such.
- Conformance note: utilities claiming conformance "shall conform completely to these guidelines as if these guidelines contained the term 'shall' instead of 'should'."

**1.A.3 — GNU long-option extensions (modern layer atop POSIX)**
- Provide long-named options (`--verbose`) equivalent to single-letter options, for readability and self-documenting scripts. (GNU Coding Standards; clig.dev "Have full-length versions of all flags.")
- Long options: `--` followed by alphanumerics and dashes; `--name=value` syntax; unique-prefix abbreviation allowed at the getopt level (but see future-proofing caveat). (GNU C Library)
- GNU `getopt` permits intermixing options and operands (reorders argv) — a deliberate departure from POSIX G9. Note this divergence: POSIX says options precede operands; GNU relaxes it. (GNU)

**1.A.4 — Flag vs. argument choice**
- **Prefer flags to args** — more typing but clearer and more future-proof; adding new args later can create ambiguity. (clig.dev; 12-Factor #2, citing the `heroku fork FROMAPP --app TOAPP` → `--from/--to` redesign.)
- Multiple args are fine for a *single variable-length type* (`rm f1 f2 f3`, works with globbing); two-or-more different arg *types* is a smell. Exception: a common primary action like `cp <src> <dst>`. (clig.dev; 12-Factor: "1 type of argument is fine, 2 types are very suspect, 3 are never good.")

**1.A.5 — Standard flag names (consensus vocabulary)** — use these if the semantics fit, so users can guess (clig.dev, GNU Table of Long Options):
- `-h/--help` (help only — never overload), `--version` (and often `-V`), `-v` (verbose or version — choose carefully), `-q/--quiet`, `-a/--all`, `-d/--debug`, `-f/--force`, `-o/--output`, `-n/--dry-run`, `-p/--port`, `-u/--user`, `--json`, `--no-input`, `--no-color`.
- GNU note: every program accepting `--quiet` should accept `--silent` as a synonym and vice versa.
- Only use single-letter flags for commonly used options, to avoid polluting the short-flag namespace. (clig.dev; JReleaser adoption issue.)

**1.A.6 — Defaults, required/optional, prompting**
- Make the default the right thing for most users (clig.dev: if `ls` were designed today it'd default to `ls -lhF`).
- Prompt for missing input when interactive, but **never *require* a prompt** — always allow flags/args, and skip prompting when stdin is not a TTY. (clig.dev; 12-Factor #7.)
- Files as ordinary args should be *input*; specify output via `-o/--output`. (GNU.)
- Support `-` to mean stdin/stdout for file arguments (POSIX G13; clig.dev).
- If a flag has an optional value, allow a sentinel word like `none` rather than a blank value (clig.dev, `ssh -F none`).
- Make args/flags/subcommands order-independent where the parser allows (clig.dev).

---

### LEVEL 1.B — COMMAND STRUCTURE & SUBCOMMANDS
<!-- Lines 92-106 -->

**Rationale:** Structure determines discoverability and how the tool scales in complexity.

**1.B.1 — Single vs. multi-command** — Simple one-task tools are single-command (`cp`, `grep`); most non-trivial tools benefit from subcommands (`git`, `npm`). With no args, list subcommands / show help rather than doing a default action. (12-Factor #11.)

**1.B.2 — Noun-verb vs. verb-noun** — Both work; `noun verb` (e.g. `docker container create`) is common for object-rich tools, though kubectl uses `VERB NOUN`. Be consistent with verbs across object types. The noun-verb tree is especially discoverable (and agent-friendly, turning exploration into deterministic tree search). (clig.dev; kubectl conventions; Starich.)

**1.B.3 — Consistency across subcommands** — same flag names for same things, similar output formatting, shared config/storage. Do not reuse a flag for different semantic purposes, or use different flag names for the same purpose. (clig.dev; kubectl conventions.)

**1.B.4 — Naming disambiguation** — avoid ambiguous/similar names (`update` vs `upgrade`); no catch-all default subcommand; no arbitrary abbreviation of subcommands (locks you out of future names). Explicit stable aliases are fine. (clig.dev future-proofing.)

**1.B.5 — Sub-subcommand delimiter** — spaces (`git submodule add`) vs colons (`heroku domains:add`). Colons avoid parser ambiguity when topic-level commands also take arguments. (12-Factor #11.)

---

### LEVEL 1.C — HELP & DOCUMENTATION
<!-- Lines 109-123 -->

**Rationale:** "Great help is essential" — without a GUI to guide users, help *is* the interface. (12-Factor #1.)

**1.C.1 — Help invocation** — `myapp`, `myapp --help`, `myapp -h`, and (git-like) `myapp help`, `myapp help subcmd`, `myapp subcmd --help/-h` all show help. Adding `-h` to anything should show help; never overload `-h`. (clig.dev; 12-Factor.)
**1.C.2 — Concise default help** — when a command needs args and gets none, show concise help: description, 1–2 examples, key flags, and pointer to `--help`. (Exception: interactive-by-default tools like `npm init`.) (clig.dev, `jq` example.)
**1.C.3 — Extensive help on request** — full flag list, grouped, most common flags/commands first, with terminal-independent formatting (bold headings, no raw escape codes through a pager). (clig.dev, heroku/git examples.)
**1.C.4 — Lead with examples** — users prefer examples; build a narrative from simple to complex; move exhaustive examples to a cheat-sheet command or web page. (clig.dev; 12-Factor.)
**1.C.5 — `--version` output** — print name, version, origin, legal status on stdout and exit successfully; first line machine-parseable (version after last space); canonical name is a constant, not computed from `argv[0]`. (GNU `--version`.) Get version via `--version`, `-V`, and a `version` subcommand; embed extra debug info; send version as HTTP User-Agent for server-side debugging. (12-Factor #3.)
**1.C.6 — Web + terminal documentation** — provide searchable web docs (most inclusive) *and* terminal docs (fast, version-synced, offline). (clig.dev; 12-Factor.)
**1.C.7 — Man pages** — consider generating man pages (many users reflexively try `man mycmd`); expose them via a `help` subcommand too. 12-Factor is more skeptical (man pages "just aren't used often enough anymore," don't work on Windows) — a noted divergence.
**1.C.8 — Suggest next steps & corrections** — "did you mean?" for typos (ask, don't silently auto-run, since invalid input may be a logical error); suggest follow-up commands; provide a support/feedback path (URL, GitHub) and make bug reports effortless (pre-populated URLs). (clig.dev; GNU: end of `--help` says where to report bugs.)
**1.C.9 — Shell completion** — provide tab-completion; flags are easier to autocomplete than args. (12-Factor.)

---

### LEVEL 1.D — OUTPUT DESIGN
<!-- Lines 126-141 -->

**Rationale:** In the terminal, "information is the interface." Output must serve humans and machines simultaneously.

**1.D.1 — Stream discipline** — **stdout for primary/machine-readable output; stderr for logs, errors, progress, and messaging.** This keeps pipes clean and warnings visible even when stdout is redirected. (clig.dev "Basics"; 12-Factor #4: "stdout is for output, stderr is for messaging.") Not everything on stderr is an error (e.g. `curl` progress). When wrapping a subcommand, always pipe its stderr up to the user. (12-Factor #4.)
**1.D.2 — Human-readable by default, machine-readable available** — decide by TTY detection. Provide `--plain` for one-record-per-line tabular output when human formatting would break `grep`/`awk`, and `--json` for structured data (pipeable to `jq`, curl-able to web services). (clig.dev; 12-Factor #8.)
**1.D.3 — Tables** — one entry per row; never draw borders (noisy, breaks parsing); mind screen width, show few columns by default with `--columns`; support `--no-truncate`, `--no-headers`, `--sort`, `--filter`, and csv/json output. Column titles/values should avoid spaces so `cut`/`awk` can split fields. (12-Factor #8; kubectl conventions.)
**1.D.4 — Say just enough on success** — display brief confirmation (updates the Unix Rule of Silence, which said say nothing); when state changes, tell the user the new state (`git push`/`git status` examples); provide `-q` to suppress non-essential output for scripts. (clig.dev; Unix Rule of Silence noted as the traditional counterpoint.)
**1.D.5 — Color** — use with intention (highlight, red for errors); disable when: stdout/stderr is not a TTY, `NO_COLOR` is set (non-empty), `TERM=dumb`, or `--no-color` is passed; consider a `MYAPP_NO_COLOR` and a `FORCE_COLOR` override. Check stdout and stderr independently. (clig.dev; 12-Factor #6; no-color.org.)
**1.D.6 — Progress & animation** — show spinners/progress bars/ETA for long tasks, but only on a TTY (no "Christmas trees" in CI logs); print logs if an error occurs behind a progress display; parallel progress needs a library. (clig.dev robustness; 12-Factor #6.)
**1.D.7 — Pager** — page long output with `less` (e.g. `less -FIRX`) only when stdin/stdout is a TTY. (clig.dev.)
**1.D.8 — Density & symbols** — increase scannable information density (ls permission columns); use emoji/symbols sparingly for structure/attention. (clig.dev.)
**1.D.9 — Don't leak developer-only detail** — no log-level labels (`ERR`, `WARN`) or stack traces by default; reserve for verbose mode; write debug logs to a file. (clig.dev; 12-Factor #5.)
**1.D.10 — Device-independence (GNU)** — don't make behavior depend on output device type merely to save typing; if defaults differ, default to the terminal-friendly behavior with a flag for the other. (GNU — a mild divergence from clig.dev's TTY-based auto-switching, which GNU tolerates for formatting/color but not core behavior.)

---

### LEVEL 1.E — ERROR HANDLING & EXIT CODES
<!-- Lines 144-158 -->

**Rationale:** Errors are the most common reason to consult docs; good errors are documentation. "Rule of Repair: when you must fail, fail noisily and as soon as possible." (Raymond.)

**1.E.1 — Actionable messages** — catch expected errors and rewrite for humans: what happened + how to fix (clig.dev: "Can't write to file.txt. You might need to make it writable by running 'chmod +w file.txt'."). Ideal error contains: code, title, description, how-to-fix, URL. (12-Factor #5.)
**1.E.2 — Signal-to-noise** — group repeated errors under one header; put the most important info last (eye drawn to red); validate input early and bail before damage. (clig.dev.)
**1.E.3 — Unexpected errors** — provide traceback/debug info and bug-submission instructions on unexpected failures, but don't overwhelm; write debug logs to a file; enable verbose via `DEBUG` env var or `-d`. Error logs should carry timestamps, be truncated periodically, and contain no ANSI color codes. (clig.dev; 12-Factor #5.)
**1.E.4 — Exit codes** — **0 = success, non-zero = failure**; map non-zero codes to important failure modes. (clig.dev.) Conventions:
- 1 = general error; 2 = shell builtin/usage misuse (Bash reserves 2, 126, 127).
- 126 = command found but not executable; 127 = command not found.
- 128+N = terminated by signal N (e.g. 130 = SIGINT/Ctrl-C).
- `sysexits.h` (BSD, originated by Eric Allman in 1980 for sendmail): EX_USAGE 64, EX_DATAERR 65, EX_NOINPUT 66, EX_NOUSER 67, EX_NOHOST 68, EX_UNAVAILABLE 69, EX_SOFTWARE 70, EX_OSERR 71, EX_OSFILE 72, EX_CANTCREAT 73, EX_IOERR 74, EX_TEMPFAIL 75, EX_PROTOCOL 76, EX_NOPERM 77, EX_CONFIG 78.
- Document your exit codes as a contract; distinct codes let scripts/agents branch programmatically. Avoid overloading everything as exit 1.

---

### LEVEL 1.F — INTERACTIVITY & PROMPTS
<!-- Lines 161-172 -->

**Rationale:** Interactivity aids humans but must never block automation.

**1.F.1 — TTY-gated prompting** — only prompt/interact if stdin is a TTY; otherwise error telling the user which flag to pass. (clig.dev; 12-Factor #7.)
**1.F.2 — Non-interactive escape hatch** — honor `--no-input`; if required input is missing in non-interactive mode, fail with instructions. (clig.dev.)
**1.F.3 — Confirmation for destructive actions** — graduated by danger: mild (maybe prompt), moderate (prompt + offer dry-run), severe (require typing the resource name; offer `--confirm=name` for scripts). Provide `-f/--force` to bypass in scripts. (clig.dev; 12-Factor #7 heroku app-destroy example.)
**1.F.4 — Password entry** — turn off terminal echo when reading passwords. (clig.dev; 12-Factor #7.)
**1.F.5 — Let the user escape** — always keep Ctrl-C working; make exit obvious; for wrappers where Ctrl-C can't quit, document the escape sequence. (clig.dev.)
**1.F.6 — Rich interactive elements** — checkboxes/radio selections improve UX when a TTY is present, but must degrade gracefully. (12-Factor #7.)

---

### LEVEL 1.G — CONFIGURATION & ENVIRONMENT
<!-- Lines 175-186 -->

**Rationale:** Configuration must be predictable, layered, and stored in standard locations.

**1.G.1 — Precedence order (highest→lowest)**: flags → shell environment variables → project-level config (e.g. `.env`) → user-level config → system-wide config. (clig.dev.)
**1.G.2 — Choose the right mechanism by specificity/stability/complexity**: per-invocation variation → flags; context-varying → env vars; project-stable/version-controlled → a committed config file (`Makefile`, `package.json` style). (clig.dev.)
**1.G.3 — XDG Base Directory spec** — config in `$XDG_CONFIG_HOME` (`~/.config/myapp`), data in `$XDG_DATA_HOME` (`~/.local/share/myapp`), cache in `$XDG_CACHE_HOME` (`~/.cache/myapp`; on macOS `~/Library/Caches/myapp`, on Windows `%LOCALAPPDATA%\myapp`); avoid dotfile proliferation. (clig.dev; 12-Factor #12.)
**1.G.4 — Environment variables** — names uppercase + digits + underscores, not starting with a digit; single-line values; don't commandeer widely-used/POSIX names; check general-purpose vars (`NO_COLOR`, `DEBUG`, `EDITOR`, `HTTP_PROXY`/`NO_PROXY`, `SHELL`, `TERM`, `TMPDIR`, `HOME`, `PAGER`, `LINES`/`COLUMNS`). Read `.env` where appropriate but don't treat `.env` as a real config file (string-only, no history, credential risk). (clig.dev.)
**1.G.5 — `--config` flag** — allow explicitly pointing to a config file.
**1.G.6 — Modifying others' config** — get consent, say exactly what you'll change, prefer creating a new file (`/etc/cron.d/myapp`) over appending, use dated comments if you must append. (clig.dev.)

---

### LEVEL 1.H — COMPOSABILITY & THE UNIX PHILOSOPHY
<!-- Lines 189-201 -->

**Rationale:** Your program *will* become part of a larger system; the only choice is whether it's a well-behaved part.

**1.H.1 — Do one thing well** (Rule of Modularity/Parsimony) — small parts with clean interfaces, recombined rather than bloated. (Unix philosophy; clig.dev.)
**1.H.2 — Text streams as universal interface** — line-based text piping; data streams should be textual where possible so standard tools can filter them. (McIlroy; Raymond.)
**1.H.3 — Be a good pipeline citizen** — read stdin, write stdout, errors to stderr, support `-`, exit codes correct, machine-readable output for scripting. (clig.dev.)
**1.H.4 — Rule of Silence / Rule of Repair / Rule of Least Surprise** — traditional Unix rules; clig.dev tempers Silence toward human feedback but keeps the machine path clean. (Raymond's 17 rules.)
**1.H.5 — Rule of Composition & Separation** — design to connect to other programs; separate policy from mechanism, interfaces from engines. (Raymond.)

Raymond's 17 rules in full, for the graph's philosophy layer: Modularity, Clarity, Composition, Separation, Simplicity, Parsimony, Transparency, Robustness, Representation, Least Surprise, Silence, Repair, Economy, Generation, Optimization, Diversity, Extensibility.

---

### LEVEL 1.I — ROBUSTNESS, SIGNALS & FUTURE-PROOFING
<!-- Lines 204-215 -->

**Rationale:** Robustness is both objective (handles failure) and subjective (feels solid).

**1.I.1 — Responsiveness** — print something in <100ms; before network calls, print a message so it doesn't look hung; responsive > fast. (clig.dev.) Startup benchmark targets: <100ms very fast, 100–500ms aim here, 500ms–2s usable, 2s+ languid. (12-Factor #9.)
**1.I.2 — Timeouts & recovery** — configurable network timeouts with sane defaults; make operations recoverable (re-run picks up where it left off); prefer crash-only design (defer cleanup, exit immediately on failure). (clig.dev; "Crash-only software.")
**1.I.3 — Idempotency** — make operations idempotent where possible (kubectl `apply` model; declarative `ensure`/`apply`/`sync` are safer than imperative `create`/`delete`); if not idempotent, make conflicts detectable via distinct exit codes.
**1.I.4 — Signals** — on Ctrl-C (SIGINT) exit ASAP, say something before cleanup, timeout cleanup; on a second Ctrl-C during cleanup, skip it (tell the user, especially if destructive). Expect to be started in a state where cleanup didn't run. (clig.dev; GNU signal handling notes.)
**1.I.5 — Validate input & expect misuse** — bad data will come; people will wrap, parallelize, and run your tool in untested environments (e.g. case-insensitive-but-case-preserving macOS filesystems). (clig.dev.)
**1.I.6 — Future-proofing** — interfaces (subcommands, flags, config, env vars, output) are contracts; keep changes additive; warn before non-additive changes and offer a migration path (and stop warning once usage is fixed); changing human output is usually OK (encourage `--plain`/`--json` in scripts); no time-bombs (don't depend on servers that may vanish; don't add blocking analytics calls). SemVer can't excuse constant breakage. (clig.dev.)

---

### LEVEL 1.J — SECURITY
<!-- Lines 218-228 -->

**Rationale:** CLIs handle credentials and run in shared/logged environments.

**1.J.1 — Don't read secrets from flags** — flag values leak into `ps` output and shell history; prefer `--password-file`, stdin, pipes, `AF_UNIX` sockets, or a secret manager. (clig.dev.)
**1.J.2 — Don't read secrets from environment variables** — env vars leak to child processes, logs, `docker inspect`, `systemctl show`; a strengthening of the older 12-Factor "config in env" stance — noted divergence. (clig.dev.)
**1.J.3 — Secure password input** — no echo (see 1.F.4).
**1.J.4 — File permissions** — restrict config/secret file permissions; don't give setuid privilege to programs that search heuristically for files. (GNU.)
**1.J.5 — Supply-chain hygiene** — pin dependencies/base images by digest, verify checksums, avoid `curl | bash` at runtime for distributed images. (kubectl/aws image example.)

---

### LEVEL 1.K — DISTRIBUTION & PACKAGING
<!-- Lines 231-240 -->

**Rationale:** Ease of install determines adoption; "tread lightly on the user's computer."

**1.K.1 — Single self-contained binary ideal** — distribute as one binary where possible; minimal dependencies; if not a binary, use the platform's native installer so files can be cleanly removed. (clig.dev.)
**1.K.2 — Multiple install methods** — package managers (brew, apt, scoop), plus a scriptable download.
**1.K.3 — Version pinning & reproducibility** — allow installing a pinned version/tag.
**1.K.4 — Open source & contribution** — public repo, license, contribution guide, code of conduct encourage diagnosis and contribution. (12-Factor #10.)

---

### CROSS-CUTTING 2.A — TESTING CLIs
<!-- Lines 243-254 -->

**Rationale:** Unit tests of internal logic can pass while the CLI contract breaks (flag dropped before save, JSON output changed, error sent to stdout, config touching the real home dir). Test the *interface contract*.

- **Test the contract, not just internals** — exercise real argv, stdout, stderr, exit codes as a user hits them. (rednafi/testscript; Smashing Magazine.)
- **Separate concerns:** unit-test command logic (parsers, stores) *and* integration/end-to-end test the invoked CLI.
- **Assert on stdout and stderr separately, plus exit code**, for each case. (Click CliRunner; Go testscript; assert_cmd.)
- **Golden/snapshot tests** for output; normalize non-deterministic output (strip empty lines, ANSI color codes, timestamps) before comparison. (stdstream-snapshot; parrot; Smashing Magazine.)
- **Test interactive prompts** by feeding stdin (CliRunner `input=`); test with and without a TTY.
- **Test help output** and `--version` (they're contracts too).
- **Isolate the filesystem/home directory** so tests don't touch real user config (CliRunner `isolated_filesystem`).
- **Cross-platform testing** — path handling, case-insensitive filesystems, Windows.

### CROSS-CUTTING 2.B — ACCESSIBILITY & INTERNATIONALIZATION
<!-- Lines 257-265 -->

**Rationale:** CLIs are assumed accessible because they're text, but decorative formatting, ASCII art, spinners, and tables interfere with screen readers; there is no accessibility tree in the terminal. (ACM CHI 2021 "Accessibility of Command Line Interfaces" by Sampath, Merrick & Macvean; GitHub CLI a11y blog.)

- Offer a **plain/bare mode** (`--plain`, `--simple`, `--no-ascii`) free of color/animation/art; screen-reader users strongly prefer it and often fall back to `--json` and grep. (afixt; ACM study.)
- **Structure linearly** — blank lines between logical sections; textual descriptions accompanying any ASCII art. (afixt.)
- **Align color palettes to the 16 ANSI 4-bit colors** so users' terminal themes/high-contrast settings apply; support high contrast and colorblind-friendly choices. GitHub CLI exposes these via `gh a11y`. (GitHub CLI.)
- **Document accessibility features** in `--help`. (afixt.)
- **i18n** — use locale env vars (`LANG`, `LC_ALL`, `LC_MESSAGES`, `LC_CTYPE`), Unicode/UTF-8 encoding, don't truncate long lines or drop non-ASCII (GNU), keep "Copyright" untranslated in `--version` (GNU).

### CROSS-CUTTING 2.C — ANALYTICS / TELEMETRY ETHICS
<!-- Lines 268-278 -->

**Rationale:** Usage data helps prioritize work but risks user trust and privacy.

- **Prefer opt-in with an explicit first-run consent prompt.** Homebrew is the cited model: per its official docs (docs.brew.sh/Analytics), "You will be notified the first time you run `brew update` or install Homebrew. Analytics are not enabled until after this notice is shown, to ensure that you can opt out without ever sending analytics data," displaying "==> Homebrew has enabled anonymous aggregate user behaviour analytics." If opt-out, make opting out trivial and visible (env var, config).
- **Transparency** — open-source the telemetry code; offer a preview/log mode to show exactly what would be sent. GitHub CLI implements this: per GitHub Docs, "In logging mode, the JSON payload that would normally be sent is printed to stderr instead" (e.g. `GH_TELEMETRY=log gh skill install ...`). Document the schema. (GitHub CLI; Codex/kongctl discussions.)
- **Collect the minimum, anonymized/pseudonymized** — no credentials, tokens, resource names, file contents, or free-form arguments; aggregate; short retention; honor `DO_NOT_TRACK`. (kongctl; 1984.vc; privacy-first analytics.)
- **Never break execution** — telemetry must be best-effort and never block or fail the command; don't emit in CI/non-interactive by default.
- **Cautionary case:** GitHub's gh CLI v2.91.0 (released April 22, 2026) enabled pseudonymous telemetry **opt-out by default with no first-run prompt** — confirmed by the GitHub Changelog ("With the release of v2.91.0, GitHub CLI sends pseudonymous usage telemetry"), with opt-out via `GH_TELEMETRY=false`, `DO_NOT_TRACK=true`, or `gh config set telemetry disabled`. The rollout drew immediate criticism: 419 points and 302 comments on Hacker News within 24 hours (byteiota), and The Register faulted GitHub for "turning telemetry on by default and not being particularly clear on what telemetry might be harvested" and for having "no standalone blog post or announcement." The sampled payload (1% of invocations per Groundy) includes command name, a flags field (flag names only), `device_id`, `invocation_id`, OS, architecture, CI status, `is_tty`, and version; a filed issue (#13263, April 22, 2026) flags whether flag *values* are captured as an unresolved documentation gap. This illustrates the anti-pattern the consensus warns against.

---

## Recommendations
<!-- Lines 281-303 -->

**Stage 1 — Get the non-negotiable basics right (do these first):**
1. Use a mature argument-parsing library (see projection layer).
2. Enforce stream discipline (stdout=data, stderr=messages) and correct exit codes (0/non-zero).
3. Implement `-h/--help` (concise default + full on request) and `--version`.
4. Detect TTY and gate color, prompts, and progress accordingly; honor `NO_COLOR`.
*Benchmark to advance:* a script can pipe your tool and parse it; a human running it with no args gets useful help.

**Stage 2 — Make it pleasant and safe:**
5. Add `--json`/`--plain`, actionable error messages, "did you mean?", and confirmation for destructive actions with `--force`/`--no-input` escape hatches.
6. Follow XDG paths and the flags > env > project > user > system precedence.
7. Never accept secrets via flags or env vars.
*Benchmark:* new users complete common tasks without external docs; no secret appears in `ps`/history.

**Stage 3 — Robustness, distribution, and stewardship:**
8. Add timeouts, idempotency/crash-only behavior, graceful Ctrl-C.
9. Build a contract-level test suite (exit codes + stdout + stderr + golden output, TTY and non-TTY).
10. Distribute a single self-contained artifact; keep interface changes additive with deprecation warnings.
11. If adding telemetry, make it opt-in, transparent (offer a log/preview mode), and minimal.
*Benchmark:* CI tests catch interface regressions; users can install in one command and upgrade cleanly.

**Thresholds that change the plan:** If your tool is used mostly by *other programs/agents* (not humans), weight machine-readable output, stable exit-code contracts, and idempotency even more heavily and de-emphasize interactive prompting. If it's a full-screen TUI, clig.dev explicitly does not apply — use TUI-specific guidance instead.

## Caveats
<!-- Lines 306-310 -->
- **Source divergences to represent in the graph, not silently resolve:** POSIX (options precede operands, strict short options) vs. GNU (long options, intermixed ordering); Unix "Rule of Silence" (say nothing on success) vs. clig.dev "say just enough" (brief confirmation); 12-Factor's original "store config/secrets in env" vs. clig.dev's newer "never put secrets in env"; 12-Factor's skepticism of man pages vs. clig.dev's endorsement; GNU's "don't vary behavior by output-device type" vs. clig.dev's TTY-based auto-switching (GNU tolerates this only for formatting/color, not core behavior). Note also that the POSIX standard defines **14** syntax guidelines, not the 13 sometimes cited.
- **Provenance summary:** clig.dev (Prasad, Firshman, Tashian, Parish) is the broadest modern source and covers nearly every domain; 12-Factor CLI Apps (Jeff Dickey/Heroku) contributes help, streams, tables, speed, subcommand delimiters, XDG; POSIX §12.2 governs short-option syntax; GNU Coding Standards govern long options, `--version`/`--help` content, device independence, and the long-option table; Raymond's *Art of Unix Programming* supplies the philosophical rules; McIlroy's 1978 Bell System Technical Journal foreword supplies the composition dictum; sysexits.h/Bash supply exit-code conventions; kubectl/AWS/GitHub CLI supply real-world command-structure and accessibility patterns; the ACM CHI 2021 study supplies accessibility evidence.
- **Recency note:** the telemetry landscape is actively evolving (GitHub's April 2026 rollout and community pushback are recent); treat specific product behaviors as time-stamped rather than permanent.
- This reference is intentionally language-agnostic at Levels 0–3; the Python-specific projection below is secondary and must not be treated as part of the core design-intent hierarchy.

### SECONDARY PROJECTION — Python ecosystem specifics (subordinate, non-core)
<!-- Lines 313-317 -->
- **Parsing:** `argparse` (stdlib, no deps), `Click` (decorator-based, composable, testable), `Typer` (type-hint based, built on Click). (clig.dev lists all three.)
- **Output/color:** `rich` (tables, color, progress, markup), `colorama` (Windows ANSI), `tqdm` (progress bars).
- **Testing:** `pytest` + Click's `CliRunner` (`invoke`, `isolated_filesystem`, `input=` for prompts; captures `exit_code`/`output`; `capture="fd"` for fd-level output that bypasses `sys.stdout`); `subprocess` for true end-to-end; snapshot libraries for golden tests.
- **Packaging/distribution:** `pyproject.toml` `[project.scripts]` console entry points (the line that maps a command name to a `main()` callable); distribute via PyPI; install/run isolated with `pipx` (one venv per app, symlinks the entry point onto PATH, e.g. `~/.local/bin`); `PyInstaller` for a single self-contained binary.
- **Config:** `python-dotenv` for `.env`; `platformdirs` for XDG-correct paths.
