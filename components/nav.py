"""Shared navigation bar.

Plain Python function composition -- ARKlight has no dedicated component
system yet (that's the planned v0.010 milestone), so reuse today means
calling other functions. Current-page highlighting (`.is-active` on the
matching link) happens automatically, client-side, via arklight.js
comparing each link's resolved href against location.href on page
load -- it won't show up in the raw generated HTML, only in a browser.
No props needed here either way.
"""

from arklight import Nav, Link


def nav():
    return Nav(
        Link("Home", href="/"),
        Link("Redmi 9A", href="/redmi9a"),
        Link("POCO F4", href="/pocof4"),
        Link("iQOO Neo 10R", href="/neo10r"),
        Link("Compare", href="/compare"),
        Link("Gallery", href="/gallery"),
        class_name="nav",
        aria_label="Primary",
    )
