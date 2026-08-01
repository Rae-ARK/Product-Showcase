# Product Showcase

A demonstration website built using ARKlight v0.003.

## Build

```bash
arklight build site.py -o dist
```

Output lands in `dist/` (`index.html`, `styles.css`, `arklight.js`, plus
one HTML file per registered route).

## Pages

- Home -- done
- Redmi 9A -- pending
- POCO F4 -- pending
- iQOO Neo 10R -- pending
- Compare -- pending
- Gallery -- pending

See `architecture.md` for the full page/component breakdown and current
build stage.

## Images

Place product renders under `assets/images/<phone-slug>/`, and shared
hero imagery under `assets/images/hero/`. Paths are referenced from
`content/phones.py` and `components/hero.py`.

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
