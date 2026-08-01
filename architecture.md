# Product Showcase Architecture

## Purpose

A demonstration website built with ARKlight v0.003. The project showcases
static website construction using plain Python, semantic HTML, ARKlight's
compiler pipeline, intrinsic CSS layouts, and the built-in JavaScript
behaviors (`toggle`, `scroll-to`, `copy`, `dismiss`).

No custom JavaScript is used -- only ARKlight's fixed, closed behavior
vocabulary.

---

## Before you build: ARKlight must be installed from source

**ARKlight is not on PyPI.** `pip install arklight` will not work. This
project depends on cloning and installing the framework itself first:

```bash
git clone https://github.com/Rae-ARK/ARKlight.git
cd ARKlight
pip install -e .
```

That installs the `arklight` package and the `arklight` CLI command into
whatever Python environment you ran `pip install` in. This project was
built and verified against commit `840e295` of that repo. Requires
Python 3.10+. No other runtime dependencies -- `pyproject.toml` lists
none beyond the build backend.

Once `arklight` is installed and importable, come back to this project
directory and build normally:

```bash
arklight build site.py -o dist
```

If you get `ModuleNotFoundError: No module named 'arklight'`, the venv
you're building in doesn't have the framework installed -- go do the
clone-and-`pip install -e .` step above in that same venv.

---

## Pages -- all implemented

| Route | Page | Notes |
|---|---|---|
| `/` | Home | Hero, featured phone cards, CTA into Compare |
| `/redmi9a` | Redmi 9A | Hero, highlights, full specs, shipping details |
| `/pocof4` | POCO F4 | Same structure as Redmi 9A |
| `/neo10r` | iQOO Neo 10R | Same structure as Redmi 9A |
| `/compare` | Compare | Full spec comparison table, all three phones side by side |
| `/gallery` | Gallery | `Picture`/`Figure`/`FigCaption` demo, one image per phone |

Build produces `dist/index.html`, `redmi9a.html`, `pocof4.html`,
`neo10r.html`, `compare.html`, `gallery.html`, `styles.css`,
`arklight.js`.

---

## Components

| Component | Role |
|---|---|
| `nav` | Shared navigation, all six routes, automatic (client-side) current-page highlighting |
| `footer` | Shared site footer |
| `section` | Titled `Section` + `Container` wrapper for reusable page blocks |
| `hero` | Large intro banner with a `scroll-to` CTA button |
| `card` | Product card rendered from one `content.phones.PHONES` entry |
| `specs` | `specs_table(phone)` for a single product page, `compare_table(phones)` for the side-by-side comparison |

All components are plain Python functions returning `ARKNode` trees --
ARKlight has no dedicated props-based component system yet (that's the
planned v0.010 milestone). Reuse today is ordinary Python function
composition.

---

## Content

Phone specifications live in `content/phones.py` as a plain list of
dicts (`PHONES`) -- name, tagline, price, image path, highlights, and a
`specs` list of `(label, value)` tuples. Pages and components import
from it and loop over it, so specification data stays out of
presentation code. `compare_table()` assumes every phone's `specs` list
uses the same labels in the same order -- true today, but if you add a
phone with a different spec set, switch it to key by label instead of
zipping by position.

---

## Assets

`assets/images/` holds hero images and per-phone product renders, one
subfolder per phone plus a shared `hero/` folder. **ARKlight does not
validate that referenced image files actually exist** -- the build
succeeds either way, since it only emits `<img src="...">` paths, never
reads the image files themselves. A wrong filename or extension (e.g.
`.jpeg` source renamed to `.jpg`, which is fine -- browsers don't care
about extension vs. actual format for JPEG) will build clean and just
404 in the browser.

Real photography now lives at:

```
assets/images/hero/hero.jpg        -- home page hero (pages/home.py)
assets/images/redmi9a/hero.jpg     -- content/phones.py (Redmi 9A)
assets/images/pocof4/hero.jpg      -- content/phones.py (POCO F4)
assets/images/iqooneo10r/hero.jpg  -- content/phones.py (iQOO Neo 10R)
```

**Gotcha:** the iQOO Neo 10R's route is `/neo10r`, but its `PHONES`
slug and asset folder are `iqooneo10r`. Route naming and asset-folder
naming are independent strings in this codebase -- don't assume they
match when adding a new phone.

**Bigger gotcha -- `arklight build` never copies `assets/` into
`dist/`.** It only compiles the Python site file into HTML/CSS/JS.
Every image path emitted in the HTML is relative to the built file
(e.g. `dist/index.html` referencing `assets/images/hero/hero.jpg`
means the browser looks for `dist/assets/images/hero/hero.jpg`), but
the build step never creates that folder. Correct filenames at the
correct paths in the *source* `assets/` tree are necessary but not
sufficient -- you must also run `cp -r assets dist/assets` after every
build, or copy it as part of a wrapper script/Makefile. See the
`## Build` section in the README for the exact command.

---

## Design goals

- Modern, spacious, semantic HTML
- Mobile-friendly through intrinsic CSS layouts (`.stack`, `.cluster`,
  `.grid`, etc.) -- no media queries, since `Page` has no `<head>`
  breakpoint hook yet
- No custom JavaScript -- only the four built-in behaviors
- Exercise as much of ARKlight's component vocabulary as fits naturally
  (semantic layout, forms, tables, media, native zero-JS widgets)

---

## Technologies

- Python 3.10+
- ARKlight v0.003 (installed from source -- see above, not on PyPI)
- Generated static HTML, CSS, and the fixed ARKlight JS runtime

---

## Build

```bash
arklight build site.py -o dist
```

---

## Build log

| Stage | Contents | Status |
|---|---|---|
| 1 | Folder scaffold, empty files | Done |
| 2 | `nav`, `footer`, `section` components | Done |
| 3 | `hero`, `card`, `content/phones.py`, real home page | Done |
| 4-6 | Redmi 9A, POCO F4, iQOO Neo 10R product pages, `specs_table` | Done |
| 7-8 | Compare, Gallery, full `site.py` route wiring, polish | Done |

The site is feature-complete for all six planned routes as of Stage 8.

---

## Known gotchas (found while building this project)

These are real issues hit during development, verified against
ARKlight's actual source (`arklight/parser/discover.py`,
`arklight/__init__.py`, `arklight/ir/schema.py`) at commit `840e295` --
not just the README.

1. **Route registration only recognizes the decorator form.**
   `arklight/parser/discover.py` finds routes via static `ast` parsing
   that pattern-matches *only* `@site.page("/route")`. The equivalent
   call form, `site.page("/route")(some_fn)`, is accepted at runtime by
   `loader.py` but is invisible to `discover()` -- a site file using only
   the call form fails the build with "No pages registered" even though
   the route would technically work if discovery weren't blocking it
   first. **Always register routes with the decorator**, even when the
   page function itself is imported from another file (this project
   wraps every imported page function in a thin `@site.page(...)`
   function in `site.py` for exactly this reason).

2. **`from arklight import *` doesn't expose everything in the schema.**
   `arklight/__init__.py` only re-exports the *first* vocabulary
   addendum (semantic layout, text-level semantics, forms, tables,
   Video/Audio/Source). The entire *second* addendum -- `Picture`,
   `PictureSource`, `OrderedList`, `DescriptionList`/`DescriptionTerm`/
   `DescriptionDetails`, `Progress`, `Meter`, `Datalist`, `Output`,
   `Dialog`, `Kbd`, `Samp`, `Var`, `Data`, `Ins`, `Del`, `Q`, `Dfn`,
   `Address`, `Wbr`, `Bdi`, `Bdo`, `Ruby`/`Rt`/`Rp`, `ColGroup`, `Col`,
   `Track`, `Map`, `Area`, `IFrame`, `NoScript` -- is fully implemented
   in `arklight/api.py` and `arklight/ir/schema.py` (so it compiles and
   validates fine) but is **not** in `__init__.py`'s import list or
   `__all__`. Importing any of these via `from arklight import *` or
   `from arklight import Picture` raises `ImportError`. Workaround: import
   directly from the submodule, e.g.
   `from arklight.api import Picture, PictureSource` (used in
   `pages/gallery.py`).

3. **`TableHeaderCell`/`TableCell` auto-wrap bare strings in `<p>`.**
   They're real containers (not `text_only_children`), so normalization
   wraps a bare string child in a `Text` node, producing
   `<th><p>Display</p></th>` instead of `<th>Display</th>`. Valid HTML,
   just more markup than a spec table strictly needs -- cosmetic only.

4. **`.is-active` nav highlighting is client-side only.** It's added by
   `arklight.js` on `DOMContentLoaded`, comparing each nav link's
   resolved `href` against `location.href`. It will never appear if you
   inspect the raw generated HTML (e.g. with `grep`) -- only when the
   page is actually loaded in a browser.

5. **`arklight build` does not copy static assets into the output
   directory.** It compiles `site.py` and its page/component tree into
   HTML/CSS/JS in `dist/`, but `assets/` (images, and presumably any
   other static files) is never touched -- there's no asset-pipeline
   step in the CLI at all (`arklight build --help` confirms: just
   `entry`, `-o/--output`, `--open/--no-open`). Every `<img
   src="assets/...">` path is correct relative to the built HTML, but
   resolves to nothing until you separately run `cp -r assets
   dist/assets` (or equivalent) after every build. Easy to miss because
   the build reports success and the HTML looks completely correct --
   the images just silently 404 in the browser.

---

## Future expansion

- Search
- Themes
- Product filters
- A real component/props system once ARKlight v0.010 ships
- Alternate backend demonstrations (once ARKlight v0.100 lands)
- Real product photography to replace the placeholder image paths
