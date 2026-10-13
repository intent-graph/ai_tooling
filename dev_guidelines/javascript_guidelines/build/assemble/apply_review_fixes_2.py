"""Stage 7, second pass of one-time edits (run once, after apply_review_fixes.py and before apply_flags.py is re-run):
non-rule MUSTs rewritten as rules (F21) and build vocabulary taken out of a judge record (F09).
Every replacement asserts that the old text is present exactly once."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batches as b  # noqa: E402

led = b.LEDGER.read_text()
skel = b.SKEL.read_text()


def rep(text, old, new):
    assert text.count(old) == 1, old[:70]
    return text.replace(old, new)


for old, new in [
    ("Expect new type errors on upgrading TypeScript under strict, because future versions may add checks to the strict flag; pin the compiler version and upgrade deliberately (pinning inferred)",
     "Pin the compiler version and upgrade TypeScript deliberately, because future versions may add checks to the strict flag and raise new type errors under strict (pinning inferred)"),
    ("Know whether an interface is an abstract data type (representation hidden behind operations) or an object (procedural interface, information hidden by procedural abstraction); do not conflate the two when designing an API.",
     "Distinguish an abstract data type (representation hidden behind operations) from an object (procedural interface, information hidden by procedural abstraction), and do not conflate the two when designing an API."),
    ("Expect SRI to break on vendor updates and to fail without CORS on the vendor host; it protects only content you reviewed, so pin versions.",
     "Pin the versions of vendor scripts under SRI: SRI breaks on vendor updates, fails without CORS on the vendor host, and protects only content you reviewed."),
    ("Expect flaky tests to come mostly from async waits (45% of studied fixes), concurrency and test-order dependency, and to be flaky from the first run, so check new tests extensively when they are added.",
     "Check new tests extensively when they are added: flaky tests come mostly from async waits (45% of studied fixes), concurrency and test-order dependency, and are flaky from the first run."),
]:
    led = rep(led, old, new)

for old, new in [
    ("Positions: Candidates and their evidence are in the slot 10 matrix (build/research/10_frameworks/result.md, L3 full). Positions: (a) the slot 10 proposal: React, Angular, Vue, Lit, htmx, no framework as comparator; (b) this record: gates on trust evidence; (c) rank by popularity.",
     "Positions: Candidates and their evidence are in the framework evidence matrix (build/research/10_frameworks/result.md, L3 full). Positions: (a) an earlier proposal: React, Angular, Vue, Lit, htmx, no framework as comparator; (b) this note: gates on trust evidence; (c) rank by popularity."),
    ("(slot 10 matrix, owned by DEFENSE)", "(framework evidence matrix, owned by DEFENSE)"),
    ("SUPPLY-C12's 'consensus' label is relabelled single-source (12_dissent X5). ", "SUPPLY-C12's 'consensus' label is relabelled single-source. "),
]:
    skel = rep(skel, old, new)
b.LEDGER.write_text(led)
b.SKEL.write_text(skel)

log = Path(__file__).resolve().parent / "bookkeeping_log.md"
log.write_text(log.read_text() +
    "- Design notes: row ids in brackets and '(see ROW)' references, gap ids (G-L20, G-M02), 'Merged: ...' sentences and the label 12_dissent are scrubbed by build_batches.py::scrub_notes when the graph is built (ledger and skeleton keep them). Judge record of FRAMEWORK_SHORTLIST: 'slot 10' wording replaced.\n"
    "- Rules written as expectations ('Expect', 'Know') rewritten as verb-first rules: CONTRACTS-027, STRUCTURE-002, DEFENSE-067, VERIFICATION-016.\n")
print("ok")
