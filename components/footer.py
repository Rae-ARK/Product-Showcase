"""Shared site footer."""

"""Shared site footer."""

from importlib.metadata import version

from arklight import Footer, Container, Text, Link

# Read the actually-installed ARKlight version at build time instead of
# hardcoding a string -- a hardcoded version drifts the moment the pin
# in requirements changes (this one had drifted: it said "v0.003" while
# 0.37 was actually installed). importlib.metadata reads the same
# installed-package metadata `pip show arklight` does, so it can't go
# stale the way a copy-pasted string can.
ARKLIGHT_VERSION = version("arklight")


def footer():
    return Footer(
        Container(
            Text(f"Product Showcase -- built with ARKlight v{ARKLIGHT_VERSION}.", class_name="muted"),
            Container(
                Link("Home", href="/"),
                Link("Compare", href="/compare"),
                Link("Gallery", href="/gallery"),
                class_name="cluster",
            ),
            class_name="stack",
        ),
        class_name="site-footer",
        # NOTE: "site-footer" is a project-defined class, not one of
        # ARKlight's built-in utility classes (.stack/.cluster/.card/
        # etc.) -- ARKlight only ships its own fixed default
        # stylesheet and has no mechanism for a project to register
        # additional CSS rules under a custom class name (confirmed:
        # no custom_css hook on Site, no project-stylesheet merge step
        # in the compiler pipeline). A class_name the compiler doesn't
        # recognize is silently inert, not an error -- so without this
        # inline style, "site-footer" would sit in the markup doing
        # nothing, and the footer would blend directly into the page
        # content above it. This mirrors .nav's bottom-border
        # treatment (see styles.css) so the page has matching
        # separators at both ends.
        style={
            "border-top": "1px solid var(--ark-border)",
            "margin-top": "3rem",
            "padding-top": "1.5rem",
        },
    )

