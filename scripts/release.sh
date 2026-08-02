#!/usr/bin/env bash
# Multi-platform build pipeline: web build -> installable PWA -> offline
# single-file bundle. Every step is a real ARKlight CLI command (or a
# small post-processing step on already-generated output) -- nothing
# here touches the compiler itself.
set -euo pipefail

OUT_DIR="${1:-dist}"
BUNDLE_NAME="${2:-product-showcase.ark}"

echo "== 1/4  Building static site -> ${OUT_DIR}/ =="
arklight build site.py -o "${OUT_DIR}" --no-open

echo "== 2/4  Enabling PWA support (manifest + service worker) =="
arklight pwa "${OUT_DIR}" \
  --name "Product Showcase" \
  --short-name "ProdShow" \
  --theme-color "#0f172a" \
  --background-color "#0f172a" \
  --display standalone

echo "== 3/4  Patching manifest.json with the project icon set =="
python3 scripts/patch_manifest_icons.py "${OUT_DIR}"

echo "== 4/4  Packing offline single-file bundle -> ${BUNDLE_NAME} =="
arklight pack "${OUT_DIR}" -o "${BUNDLE_NAME}" --plain

echo
echo "Done."
echo "  Web build:      ${OUT_DIR}/       (deploy as-is, e.g. GitHub Pages)"
echo "  Installable PWA: same directory -- manifest.json + sw.js are in place"
echo "  Offline bundle:  ${BUNDLE_NAME}   (arklight unpack ${BUNDLE_NAME} -o <dir> to open)"
