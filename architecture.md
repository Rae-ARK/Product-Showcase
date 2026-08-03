# Product Showcase Architecture

## Purpose

A production-track demonstration site built with ARKlight. The
project exercises static website construction using plain Python,
semantic HTML, ARKlight's compiler pipeline, intrinsic CSS layouts,
and the built-in JavaScript behaviors (`toggle`, `scroll-to`, `copy`,
`dismiss`) -- and, as of this stage, targets a genuine multi-platform
deliverable: web, installable PWA, and single-file offline bundle
from the same build.

No custom JavaScript is used -- only ARKlight's fixed, closed behavior
vocabulary.

---

## Install

ARKlight is on PyPI:

```bash
pip install arklight
```

Requires Python 3.10+. No other runtime dependencies. This project is
tracked against `arklight` 0.37. Note: the CLI's `arklight --version`
currently prints `0.038`, which does not match the installed package
version (`pip show arklight` -> `0.37`) -- a real, minor discrepancy
in the upstream package's version reporting, not a project bug here.
Don't use `arklight --version` output to diagnose install issues;
use `pip show arklight` instead.

Once installed, build normally from this project directory:

```bash
arklight build site.py -o dist
```

---

## Pages -- all implemented

| Route | Page | Notes |
|---|---|---|
| `/` | Home | Hero, featured phone cards, CTA into Compare |
| `/redmi9a` | Redmi 9A | Hero, highlights, full specs, shipping details |
| `/pocof4` | POCO F4 | Same structure as Redmi 9A |
| `/neo10r` | iQOO Neo 10R | Same structure as Redmi 9A |
| `/compare` | Compare | Full spec comparison, all three phones side by side |
| `/gallery` | Gallery | `Picture`/`Figure`/`FigCaption` demo, one image per phone |

Build produces `dist/index.html`, `redmi9a.html`, `pocof4.html`,
`neo10r.html`, `compare.html`, `gallery.html`, `styles.css`,
`arklight.js`, and `dist/assets/` (copied automatically -- see
"Assets" below).

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
ARKlight has no dedicated props-based component system yet. Reuse
today is ordinary Python function composition.

---

## Content

Phone specifications live in `content/phones.py` as a plain list of
dicts (`PHONES`) -- name, tagline, price, image path, highlights, and a
`specs` list of `(label, value)` tuples. Pages and components import
from it and loop over it, so specification data stays out of
presentation code. `compare_table()` assumes every phone's `specs`
list uses the same labels in the same order -- true today; tracked as
a fragility to fix in Stage 2 (see Roadmap).

---

## Assets

`assets/images/` holds hero images and per-phone product renders, one
subfolder per phone plus a shared `hero/` folder.

**ARKlight does not validate that referenced image files actually
exist** -- the build succeeds either way, since it only emits `<img
src="...">` paths, never reads the image files themselves. A wrong
filename or extension will build clean and just 404 in the browser.
Tracked as a Stage 2 fix (build-time assertion, see Roadmap).

Real photography lives at:

```
assets/images/hero/hero.jpg        -- home page hero (pages/home.py)
assets/images/redmi9a/hero.jpg     -- content/phones.py (Redmi 9A)
assets/images/pocof4/hero.jpg      -- content/phones.py (POCO F4)
assets/images/iqooneo10r/hero.jpg  -- content/phones.py (iQOO Neo 10R)
```

**Gotcha:** the iQOO Neo 10R's route is `/neo10r`, but its `PHONES`
slug and asset folder are `iqooneo10r`. Route naming and asset-folder
naming are independent strings in this codebase -- don't assume they
match when adding a new phone. Tracked as a Stage 2 fix.

**Resolved as of this stage:** `arklight build` now copies `assets/`
into the output directory automatically (confirmed directly against
`arklight/compiler/pipeline.py`'s `_copy_assets` step in the PyPI
package). The previous manual `cp -r assets dist/assets` requirement
no longer applies against `arklight` >= the version pinned above.

---

## Multi-platform distribution

Three targets ship from the same `dist/` build, all native ARKlight
CLI commands, all independent and stackable:

```bash
arklight build site.py -o dist                                  # web
arklight pwa dist --name "Product Showcase" --display standalone # installable PWA
arklight pack dist -o product-showcase.ark --plain                # offline single-file bundle
```

`pwa` injects a manifest and service worker into the HTML/JS output;
`pack` bundles a directory (PWA-ified or not) into one portable file.
Neither assumes exclusive ownership of the build directory, so running
both against the same `dist/` produces a build that is simultaneously
web-hosted, installable, and offline-portable.

---

## Design goals

- Modern, spacious, semantic HTML
- Mobile-friendly through intrinsic CSS layouts (`.stack`, `.cluster`,
  `.grid`, `.switcher`, etc.) -- no media queries, since `Page` has no
  `<head>` breakpoint hook
- No custom JavaScript -- only ARKlight's built-in behaviors and, where
  it adds real value, its closed-form `State`/`Action` model
- Exercise ARKlight's component vocabulary as it naturally fits
  (semantic layout, forms, tables, media, native zero-JS widgets)
- Stay honest about what ARKlight cannot do yet (no derived state, no
  per-item list templating, no conditional rendering) rather than
  working around those gaps with fragile hacks

---

## Technologies

- Python 3.10+
- ARKlight (PyPI, `pip install arklight`)
- Generated static HTML, CSS, and the fixed ARKlight JS runtime
- GitHub Actions for CI/CD (Stage 5)

---

## Roadmap

This project is being rebuilt in five tracked stages toward a
genuinely production-grade, multi-platform reference site.

### Stage 1 -- Documentation (this pass)
- Update install/build instructions for the PyPI-published package
- Correct the now-resolved manual asset-copy gotcha
- Document the multi-platform build path (`pwa` + `pack`)
- Record this roadmap as the source of truth for remaining scope

### Stage 2 -- Content/data layer
- Fix the `route` vs. asset-folder-slug independence (`neo10r` vs.
  `iqooneo10r`) with an explicit, enforced relationship or a build-time
  assertion
- Add a build-time check that every `phone["image"]` path actually
  exists on disk, failing the build with a clear error instead of a
  silent 404
- Make `compare_table()` key by spec label instead of positional zip,
  so phones with differing spec sets don't silently misalign

### Stage 3 -- Component refactor
- Replace the flat comparison `Table` with a responsive card layout
  (`.switcher`) that reflows to one column per phone on narrow
  viewports, in addition to (or instead of) the literal table
- Add real, scoped interactivity using ARKlight's actual `State`/
  `Action` primitives (e.g., a "which phone fits your budget" tap-to-
  select flow) -- explicitly not promising derived state or
  conditional rendering that ARKlight doesn't support
- Move the `Picture`/`PictureSource` import off the `arklight.api`
  submodule workaround once/if it's re-exported upstream; until then,
  keep the workaround but pin the ARKlight version this depends on

### Stage 4 -- Multi-platform build
- Wire `arklight pwa` and `arklight pack` into a single build script
  (not just documented as separate manual commands)
- Add a real `manifest`/icon set instead of placeholder theme-color-only
  PWA config
- Verify the offline `.ark` bundle actually opens and renders correctly
  standalone (no server) as part of the build check

### Stage 5 -- CI/CD
- GitHub Actions workflow: build on every PR, fail the build if any
  referenced asset is missing (Stage 2's check) or if `arklight build`
  itself errors
- Deploy `dist/` to GitHub Pages automatically on merge to `main`
- Optionally attach the `.ark` bundle as a release artifact

---

## Known ARKlight behavior notes (found while building this)

Verified against ARKlight's actual source, not just its README.

1. **Route registration only recognizes the decorator form.**
   ARKlight's route discovery finds routes via static `ast` parsing
   that pattern-matches *only* `@site.page("/route")`. The equivalent
   call form, `site.page("/route")(some_fn)`, is accepted at runtime
   but invisible to discovery -- a site file using only the call form
   fails the build with "No pages registered." **Always register
   routes with the decorator**, even when the page function itself is
   imported from another file (this project wraps every imported page
   function in a thin `@site.page(...)` function in `site.py` for
   exactly this reason).

2. **Resolved, no longer a gotcha: the second component addendum.**
   Previously `arklight/__init__.py` only re-exported the first
   vocabulary addendum, and the full second addendum -- `Picture`,
   `PictureSource`, `OrderedList`,
   `DescriptionList`/`DescriptionTerm`/`DescriptionDetails`,
   `Progress`, `Meter`, `Datalist`, `Output`, `Dialog`, `Kbd`, `Samp`,
   `Var`, `Data`, `Ins`, `Del`, `Q`, `Dfn`, `Address`, `Wbr`, `Bdi`,
   `Bdo`, `Ruby`/`Rt`/`Rp`, `ColGroup`, `Col`, `Track`, `Map`, `Area`,
   `IFrame`, `NoScript` -- had to be imported from the `arklight.api`
   submodule directly. Confirmed fixed against the currently pinned
   version: every name above now imports cleanly straight from
   `arklight` (verified with a direct import check). `pages/gallery.py`
   now imports `Picture`/`PictureSource` straight from `arklight`
   like everything else -- no submodule workaround needed.

3. **`TableHeaderCell`/`TableCell` auto-wrap bare strings in `<p>`.**
   They're real containers (not `text_only_children`), so
   normalization wraps a bare string child in a `Text` node, producing
   `<th><p>Display</p></th>` instead of `<th>Display</th>`. Valid
   HTML, just more markup than strictly needed -- cosmetic only.

4. **`.is-active` nav highlighting is client-side only.** It's added
   by `arklight.js` on `DOMContentLoaded`, comparing each nav link's
   resolved `href` against `location.href`. It will never appear if
   you inspect the raw generated HTML -- only when the page is
   actually loaded in a browser.

5. **`arklight --version` and `pip show arklight` disagree.** CLI
   reports `0.038`; installed package metadata reports `0.37`. Treat
   `pip show` as authoritative.

6. **Resolved, no longer a gotcha:** `arklight build` copying
   `assets/` automatically. Previously required a manual `cp -r`
   step; confirmed fixed in the currently pinned version.

7. **ARKlight has no mechanism for a project to add its own CSS
   rules.** Confirmed by reading `arklight/backend/css/render.py`
   directly: the CSS backend emits one fixed, constant stylesheet
   (utility classes + bare-tag defaults) and that's the entire
   output -- there's no `Site(custom_css=...)` hook, no
   project-stylesheet merge step in the compiler pipeline, and no way
   to register a rule under a class name of your own choosing. A
   `class_name` that isn't one of ARKlight's own built-in classes
   (`.stack`, `.cluster`, `.card`, etc.) is **silently inert** -- it
   compiles fine, appears in the markup, and does nothing.
   This bit this project directly: `price`, `button-link`, `cta`, and
   `site-footer` were all project-invented class names with zero
   backing anywhere, so the price never stood out from body text, the
   "Open comparison" CTA rendered as a plain link, the CTA section had
   no visual separation, and the footer had no separator. **Fixed by
   switching those four to per-node `style={...}` dicts** (the only
   customization mechanism ARKlight actually supports beyond its own
   fixed classes) -- see `components/card.py`, `compare_cards.py`,
   `footer.py`, and `pages/home.py`. The inert `class_name`s were left
   in place alongside the new `style=` props, since they're harmless
   and self-document intent for if/when ARKlight adds real custom-CSS
   support.

8. **Hardcoded version strings drift.** `components/footer.py` said
   "built with ARKlight v0.003" long after the pinned version moved to
   0.37 -- nothing catches that kind of drift automatically. Fixed by
   reading `importlib.metadata.version("arklight")` at build time
   instead of hardcoding a string, so the footer can't go stale again.

