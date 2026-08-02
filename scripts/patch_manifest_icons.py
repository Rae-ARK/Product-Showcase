"""Patch manifest.json with this project's icon set.

`arklight pwa` has no --icons flag (confirmed against its own
--help output), so the generated manifest.json always has an empty
"icons" array. This fills it in as a small post-build step -- editing
already-generated output, not the compiler -- using the icon files in
assets/icons/, which `arklight build` already copies into the output
directory automatically as part of its normal assets/ copy step.
"""

import json
import sys
from pathlib import Path

ICONS = [
    {"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
    {
        "src": "assets/icons/icon-512.png",
        "sizes": "512x512",
        "type": "image/png",
        "purpose": "any maskable",
    },
]


def main():
    if len(sys.argv) != 2:
        print("usage: patch_manifest_icons.py <build_dir>", file=sys.stderr)
        sys.exit(1)

    build_dir = Path(sys.argv[1])
    manifest_path = build_dir / "manifest.json"

    if not manifest_path.is_file():
        print(
            f"No manifest.json in {build_dir} -- run `arklight pwa` before this step.",
            file=sys.stderr,
        )
        sys.exit(1)

    for icon in ICONS:
        icon_path = build_dir / icon["src"]
        if not icon_path.is_file():
            print(
                f"Warning: {icon_path} not found -- did `arklight build` copy "
                f"assets/icons/ into {build_dir}?",
                file=sys.stderr,
            )

    manifest = json.loads(manifest_path.read_text())
    manifest["icons"] = ICONS
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Patched {manifest_path} with {len(ICONS)} icon(s).")


if __name__ == "__main__":
    main()
