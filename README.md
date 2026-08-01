# Product Showcase

A demonstration website built using ARKlight v0.003.

## Before you build: install ARKlight first

**ARKlight is not on PyPI.** This project won't build until you clone
and install the framework itself, in the same Python environment
you'll run `arklight build` from:

```bash
git clone https://github.com/Rae-ARK/ARKlight.git
cd ARKlight
pip install -e .
```

Requires Python 3.10+. No other runtime dependencies. Verified against
commit `840e295`.

If `arklight build` fails with `ModuleNotFoundError: No module named
'arklight'`, that's this step -- go run it in your venv.

## Build

```bash
arklight build site.py -o dist
```

Output lands in `dist/`: `index.html`, `redmi9a.html`, `pocof4.html`,
`neo10r.html`, `compare.html`, `gallery.html`, `styles.css`,
`arklight.js`.

## Pages

- Home
- Redmi 9A
- POCO F4
- iQOO Neo 10R
- Compare
- Gallery

All six are implemented and build cleanly. See `architecture.md` for
the full component/content breakdown and a list of real ARKlight
gotchas hit while building this (route registration syntax, an
`__init__.py` export gap for `Picture`/`PictureSource`/etc., and a
couple of cosmetic rendering quirks).

## Images

`assets/images/<phone-slug>/` and `assets/images/hero/` are currently
**empty placeholders**. ARKlight does not check that referenced image
files exist -- the build will succeed either way -- so add real product
photography before deploying, or every `<img>` will 404 in the browser.

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
# Product-Showcase
