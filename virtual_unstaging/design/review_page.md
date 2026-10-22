# virtual_unstaging — review page

How the owner reviews results on a local page and how every judgment is stored typed. It refines the
[review page claim](README.md#review-page) of the design; the tables it writes are in the
[data model](data_model.md).

> **Status:** implemented as `virtual_unstaging.review` (server, parsing, service, one static page) and
> `virtual_unstaging.store.review_queries` (all its SQL). Tested with the stand-in models; the page's layout and
> pointer drawing have not been exercised in a real browser.

## Views
<!-- Lines 13-31 -->

Start it with `unstage review [--port N] [--reviewer NAME]`; it prints one URL carrying this session's token.
`?run=<id>` picks the run of the typed review; `?compare=<run_a>,<run_b>` opens the blind comparison.

- **Review** (typed): for each photo of a run, its best attempt: the original, the candidate with the judge's
  findings drawn as dashed boxes with their codes, and the original with the removal region outlined (the stored
  `outline` tool output; the stage-0 removal mask when there is none). The reviewer gives a verdict, usable or
  unusable, and may add findings: a code from `defect_type`, a box dragged on the candidate (or none, for the whole
  image), a severity, a comment. Findings are kept in the page until the verdict is given, then stored with it.
- **Compare**: for each photo in both runs whose best attempts produced different images and that this reviewer
  has not compared yet: one row, left candidate, original, right candidate, all on one screen, engines hidden. The side shown is a
  hash of reviewer, photo and the two attempts, so it is pseudo-random and fixed per reviewer and photo. A pair
  already compared is skipped, in whichever order the runs are named.
- **Delivery**: for each photo, its current outcome, the candidates (the best attempt of each run, with the
  judge's score and the reviewer's verdict), and a choice of emptied (with the chosen attempt), original, or
  excluded.

Counts of what is left are in the header of each view.

## Keys
<!-- Lines 34-52 -->

The keys below work when no text field has the focus. Digits are read from the physical key (`Digit1`, `Numpad1`),
so they work on layouts where digits need Shift.

| View | Key | Does |
|---|---|---|
| all | `←` `→` | previous, next item |
| all | `g` then `r`, `c`, `d` | go to Review, Compare, Delivery |
| Review | `u`, `x` | verdict usable, unusable (stores the review, next photo) |
| Review | drag on the candidate | draws the box of a finding |
| Review | `f` | a finding on the whole image |
| Review | `1`-`9`, `s`, `c`, `Enter`, `Esc` | with a finding open: defect, severity, comment, add, cancel |
| Review | `Backspace` | remove the last finding not yet stored |
| Review | `Space` | show the original in place of the candidate, and back |
| Review | `m` | comment on the verdict |
| Compare | `1`, `2`, `=`, `0` | left better, right better, equal, both unusable |
| Delivery | `e`, `o`, `x` | emptied (with the picked candidate), original, excluded |
| Delivery | `1`-`9`, `r` | pick a candidate, reason |

## Security
<!-- Lines 55-71 -->

The page is a local web server, so the browser is the attacker's reach into it.

| Threat | Defence | Code of the refusal |
|---|---|---|
| Reached from the network | binds `127.0.0.1` only | — |
| DNS rebinding | the `Host` header must be `127.0.0.1:<port>` or `localhost:<port>` | `bad_host` |
| Another local process or page | a random 256-bit session token, compared in constant time, on every request: in the URL for pages and images, in the `X-Review-Token` header for the API | `missing_token`, `bad_token` |
| Cross-site request forgery | a write needs the token in the header, `Sec-Fetch-Site: same-origin` or an `Origin` equal to the page's origin (and neither contradicting), and `Content-Type: application/json` | `cross_origin`, `missing_token`, `unsupported_media_type` |
| Hostile body | strict JSON (UTF-8, one object, no duplicate keys, no NaN), at most 64 KiB, unknown fields refused, defect codes from the taxonomy, boxes with 0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1, attempt and photo ids that exist and agree | `invalid_json`, `invalid_body`, `unknown_defect`, `unknown_attempt`, `unknown_photo`, `payload_too_large` |
| File access through the image route | `/image/<64 hex>` only; the hash must be in the `image` table, which gives the media type; the file path is built from the hash alone and the bytes are checked against it | `not_found`, `blob_corrupted` |
| Injection | every SQL statement is fixed text with bound parameters, in `store.review_queries`; page text is set with `textContent` | — |
| Script injection, leaks | a Content-Security-Policy with a per-response nonce, no external address, `Referrer-Policy: no-referrer`, `nosniff`, no framing | — |

Errors are JSON `{"error": {"code", "message"}}`; the message names the field, never the value. A stack never
leaves the process.

## Data written
<!-- Lines 74-85 -->

Only these rows, each in one transaction, and only through the three `POST` endpoints:

| Endpoint | Writes | Rules |
|---|---|---|
| `/api/review` | one `review` and its `finding` rows (`review_id` set, `judgment_id` null) | the attempt exists and has an image; a later review of the same attempt is a new row, and the latest counts |
| `/api/preference` | one `preference` with `attempt_a` (the first run's best), `attempt_b`, `shown_left`, `choice` | the attempts differ and belong to one photo; `shown_left` is the side this reviewer was shown; one preference per reviewer and pair, a second is refused (`already_compared`) |
| `/api/delivery` | one `delivery` row, `decided_by = 'human:<reviewer>'`, replacing any earlier decision | `emptied` needs an attempt of that photo with an image, the others must not carry one; `deliver_by_rule` never overrides it |

A choice of `a` or `b` names a column of `preference`, not a side: the page turns "left is better" into `a` or
`b` with `shown_left` before sending.

## Limits
<!-- Lines 88-91 -->

- A stored preference cannot be undone from the page (the tables are append-only); a verdict can be revised.
- Pairs whose best attempts are different attempts but identical images are not shown.
- The reviewer name is given at start; there is no login, the token is the only credential.
