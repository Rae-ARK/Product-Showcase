"""Build-time asset validation.

ARKlight does not check that a referenced image file actually exists --
a wrong path builds clean and 404s the <img> in the browser instead of
failing the build (see architecture.md). This module closes that gap
for this project specifically: call assert_asset_exists() at module
import time (content/phones.py and pages/home.py both do this) so a
bad path fails `arklight build` immediately, with the offending path
and context in the error, instead of shipping a silent 404.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def assert_asset_exists(relative_path, context):
    """Raise AssertionError if relative_path doesn't exist under the project root.

    relative_path: the same string used as an ARKlight `src=` value,
        e.g. "assets/images/redmi9a/hero.jpg" -- relative to the site
        entry file, same as ARKlight itself resolves it at runtime.
    context: short human-readable string identifying where this path
        came from (a phone slug, a page name), included in the error
        so a failure points straight at the source, not just the path.
    """
    full_path = PROJECT_ROOT / relative_path
    if not full_path.is_file():
        raise AssertionError(
            f"Missing asset referenced from {context}: "
            f"'{relative_path}' does not exist at {full_path}. "
            f"This would build cleanly and 404 in the browser -- fix the "
            f"path or add the missing file before building."
        )
