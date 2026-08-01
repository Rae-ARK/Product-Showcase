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
cp -r assets dist/assets
```

**The `cp -r assets dist/assets` step is required.** `arklight build`
only compiles `site.py` into HTML/CSS/JS -- it never copies the
`assets/` folder into `dist/`. Every page's `<img src="assets/...">`
is a path relative to the built HTML file, so without this step
`dist/` has no `assets/` folder at all and every image 404s in the
browser, even though the build itself reports success and every path
in the HTML is correct.

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

Real product photos are now in place. Each file must sit at the exact
path/filename the code expects -- ARKlight does not check that
referenced image files exist, so a wrong path builds cleanly and just
404s the `<img>` in the browser instead of failing the build.

| Path | Referenced from |
|---|---|
| `assets/images/hero/hero.jpg` | `pages/home.py` (home page hero banner) |
| `assets/images/redmi9a/hero.jpg` | `content/phones.py` (Redmi 9A) |
| `assets/images/pocof4/hero.jpg` | `content/phones.py` (POCO F4) |
| `assets/images/iqooneo10r/hero.jpg` | `content/phones.py` (iQOO Neo 10R) |

Note the phone slug for the iQOO Neo 10R is `iqooneo10r`, not `neo10r`
(the route is `/neo10r`, but the asset folder and `PHONES` slug are
`iqooneo10r` -- easy to trip over).

Extra unused source photos are left in `assets/images/hero/` (e.g.
`redmi.jpeg`, `poco.jpeg`) as spares for swapping the home page hero
later -- ARKlight only ever reads the exact path passed in code, so
extra files are ignored and harmless.

Having the right files at the right paths is necessary but **not
sufficient** -- see the `cp -r assets dist/assets` step in Build above.
Without it, correctly-named images still won't appear, because they
never get copied into `dist/` in the first place.

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
