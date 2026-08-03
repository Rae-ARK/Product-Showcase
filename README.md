# Product Showcase

A production-track demonstration site built with [ARKlight](https://pypi.org/project/arklight/),
showing what an ARKlight site looks like when it targets more than
"it built once." Three products, a comparison page, a gallery, and a
build pipeline that ships to the web, as an installable PWA, and as a
single portable offline file -- all from the same source.

## Install

ARKlight is on PyPI now -- no source clone required:

```bash
pip install arklight
```

Requires Python 3.10+. Verified against `arklight` 0.37 (the CLI's
own `--version` output currently reports `0.038`, a known cosmetic
mismatch upstream -- `pip show arklight` is the accurate source of
truth for what's actually installed).

## Build

```bash
arklight build site.py -o dist
```

That's the whole command. `assets/` is copied into `dist/assets`
automatically as of the version pinned above -- this used to require a
manual `cp -r assets dist/assets` step; that gap has been fixed
upstream and this project no longer needs the workaround. (If you're
building against an older ARKlight install and images 404, that's why
-- upgrade.)

Output lands in `dist/`: `index.html`, `redmi9a.html`, `pocof4.html`,
`neo10r.html`, `compare.html`, `gallery.html`, `styles.css`,
`arklight.js`, plus `assets/`.

## Multi-platform build

The same `dist/` output feeds two additional distribution targets,
both native to ARKlight's CLI:

```bash
# Installable, offline-capable PWA (adds manifest.json + service worker)
arklight pwa dist --name "Product Showcase" --theme-color "#0f172a" --display standalone

# Single-file offline handoff bundle (no server required to view it)
arklight pack dist -o product-showcase.ark --plain
```

Run `pwa` before `pack` if you want the offline bundle to include the
installable manifest too -- both operate on the same directory and are
order-insensitive otherwise.

## Pages

- Home
- Redmi 9A
- POCO F4
- iQOO Neo 10R
- Compare (responsive spec comparison)
- Gallery

See `architecture.md` for the full component/content breakdown, the
staged production roadmap, and a running list of real ARKlight
behavior notes hit while building this (route registration syntax,
an `__init__.py` export gap for `Picture`/`PictureSource`/etc., and
a couple of cosmetic rendering quirks).

## Images

Real product photos live under `assets/images/`, one subfolder per
phone plus a shared `hero/` folder. ARKlight does not validate that a
referenced image file exists at build time -- a wrong path builds
clean and 404s the `<img>` in the browser. See `architecture.md` for
the exact path table and a build-time guard against this class of
bug.

## Recent fixes

A rendered-output audit (not just "does it compile") turned up one
real gap: ARKlight has no mechanism for a project to add its own CSS
rules (confirmed against `arklight/backend/css/render.py`) -- a
`class_name` that isn't one of ARKlight's built-in classes is silently
inert. This project had four such classes (`price`, `button-link`,
`cta`, `site-footer`) rendering with zero styling as a result. Fixed
by moving those to per-node `style={...}` props, the only
customization mechanism ARKlight actually supports beyond its fixed
class set. Also fixed a stale hardcoded `"ARKlight v0.003"` string in
the footer -- now read live via `importlib.metadata`. Full detail in
`architecture.md` -> "Known ARKlight behavior notes" (items 7-8).

## Project layout

```
product-showcase/
├── architecture.md
├── README.md
├── site.py
├── assets/images/
├── components/
├── pages/
└── content/
```

## Roadmap status

This project is being rebuilt in stages toward a genuinely
production-grade, multi-platform reference site. Current stage:

- [x] **1. Documentation** -- this pass
- [x] **2. Content/data layer** -- route/slug fragility fix, asset-existence guard
- [x] **3. Component refactor** -- responsive compare view, real interactivity, dependency pin
- [x] **4. Multi-platform build** -- PWA + `.ark` bundle, verified working (`arklight pwa` / `arklight pack` / `arklight unpack` round-tripped clean against this build)
- [ ] **5. CI/CD** -- GitHub Actions build-and-verify on PRs, deploy to Pages on merge

See `architecture.md` -> "Roadmap" for scope detail on each stage.
