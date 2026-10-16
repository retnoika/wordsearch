# Changelog

Notable changes to Word Search Maker. A release is the tagged state of
`web/index.html` together with its vendored fonts — the app has no build step.

## v1.0.0 — 16 October 2026

First production release. Everything runs in the browser: no server, no account,
no tracking, and nothing you type or make leaves your device. It also works
straight from disk, offline.

### Making a puzzle

- **Words your way** — type your own (one per line; commas or spaces also work)
  or pick them from the built-in offline word bank: 39 topics with about 700
  words, synonyms included, so "fall" finds autumn.
- **Grid 5–30** rows and columns, chosen from dropdowns, with diagonals and
  backwards words as checkboxes.
- **Reusable seeds** — the same seed with the same words rebuilds the identical
  puzzle, so a sheet can be reprinted later. The seed used is shown, and it can
  be tapped to put back in the Seed box.
- Words that cannot be placed are listed with a reason on screen — never
  silently dropped.

### Printing and exports

- **Save as PDF** gives a composed A4 sheet: exactly two pages at every size from
  5x5 to 30x30. Page 1 is the puzzle — eyebrow, title, optional name and date
  line, the grid sized to fill the print width, the word list, and a footer
  pointing at the key. Page 2 is the answer key, carrying the puzzle title so a
  printed key identifies its puzzle.
- **Options menu** — the answer key as `.txt`, the puzzle as `.svg` (vector, with
  the letters still editable type, sized in millimetres), or the puzzle as `.png`
  (300 dpi, sized from the printed grid).
- The grid is drawn as vector, and the print path uses explicit millimetre page
  sizes, so browsers agree on the paper size.

### Interface

- One self-contained HTML file: no build step, no framework, no CDN, no network
  at runtime. Fraunces and DM Sans are vendored beside it, with a system fallback
  if the page is copied on its own.
- Works on desktop, tablet and phone; the phone layout is checked at 390px.

### Credits and licence

- App icon "Word game" by Graphics Hill on Flaticon, used under Flaticon's free
  licence, which requires attribution; credited in the app and in the README.
- Fraunces and DM Sans are bundled under the SIL Open Font License; the interface
  icons are Tabler, MIT licensed. The project itself is MIT — see `LICENSE`.

### Known limits

- **The grid stops at 30x30 by choice.** At 30 the letters print at about 8.7pt;
  smaller than that stops being comfortable to do with a pencil.
- **A very long word list can push the printed sheet to a third page.** The
  built-in topic picker stops at 20 words to stay clear of that, and a hand-typed
  list of about 30 or fewer keeps the two-page promise at 30x30.
- The exported `.svg` names its font rather than embedding it, so a design app
  substitutes unless DM Sans is installed.
