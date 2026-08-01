# Product Showcase Architecture

## Purpose

A demonstration website built with ARKlight v0.003. The project showcases
static website construction using plain Python, semantic HTML, ARKlight's
compiler pipeline, intrinsic CSS layouts, and the built-in JavaScript
behaviors (`toggle`, `scroll-to`, `copy`, `dismiss`).

No custom JavaScript is used -- only ARKlight's fixed, closed behavior
vocabulary.

---

## Pages

### `/` -- Home
Hero banner, featured phone cards (Redmi 9A, POCO F4, iQOO Neo 10R), and
a CTA into the comparison page. Implemented (Stage 3).

### `/redmi9a` -- Redmi 9A
Entry-level product page. Not yet implemented (Stage 4).

### `/pocof4` -- POCO F4
Performance flagship-killer page. Not yet implemented (Stage 5).

### `/neo10r` -- iQOO Neo 10R
Gaming/performance phone page. Not yet implemented (Stage 6).

### `/compare` -- Compare
Full specification comparison across all three phones. Not yet
implemented (Stage 7).

### `/gallery` -- Gallery
Image gallery demonstrating `Picture`, `Figure`, and `FigCaption`. Not
yet implemented (Stage 7).

---

## Components

| Component | Role | Status |
|---|---|---|
| `nav` | Shared navigation, all six routes, automatic current-page highlighting | Done (Stage 2) |
| `footer` | Shared site footer | Done (Stage 2) |
| `section` | Titled `Section` + `Container` wrapper for reusable page blocks | Done (Stage 2) |
| `hero` | Large intro banner with a `scroll-to` CTA button | Done (Stage 3) |
| `card` | Product card rendered from one `content.phones.PHONES` entry | Done (Stage 3) |
| `specs` | Spec table helpers for product/compare pages | Not yet implemented (Stage 4+) |

All components are plain Python functions returning `ARKNode` trees --
ARKlight has no dedicated props-based component system yet (that's the
planned v0.010 milestone). Reuse today is ordinary Python function
composition.

---

## Content

Phone specifications live in `content/phones.py` as a plain list of
dicts (`PHONES`) -- no ARKlight involved. Pages and components import
from it and loop over it, so specification data stays out of
presentation code and each phone is defined in exactly one place.

---

## Assets

`assets/images/` holds hero images and per-phone product renders, one
subfolder per phone plus a shared `hero/` folder. Referenced by path
from `content/phones.py` and `components/hero.py` -- ARKlight only
references image paths, it does not process or optimize images itself.

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
- ARKlight v0.003
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
| 4 | Redmi 9A page | Pending |
| 5 | POCO F4 page | Pending |
| 6 | iQOO Neo 10R page | Pending |
| 7 | Compare page, gallery page | Pending |
| 8 | `site.py` full route wiring, build test, polish | Pending |

---

## Known gotchas

- `arklight/parser/discover.py` only recognizes the literal
  `@site.page("/route")` decorator syntax via static AST parsing. The
  explicit call form (`site.page("/route")(fn)`) is accepted at runtime
  by `loader.py` but is invisible to `discover()`, so a site file using
  only the call form fails the build with "No pages registered" even
  though the route would technically work. Always register routes with
  the decorator, even when the page function itself is imported from
  another file.

---

## Future expansion

- Search
- Themes
- Product filters
- A real component/props system once ARKlight v0.010 ships
- Alternate backend demonstrations (once ARKlight v0.100 lands)
