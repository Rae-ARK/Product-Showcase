"""Compare page -- full specification comparison across all three phones."""

from arklight import Page, Heading, Text, Container, Section, Link
from components.nav import nav
from components.footer import footer
from components.specs import compare_table
from content.phones import PHONES


def compare():
    return Page(
        nav(),
        Section(
            Heading("Compare"),
            Text("Every spec, side by side.", class_name="muted"),
            class_name="stack",
        ),
        Section(
            compare_table(PHONES),
            class_name="stack",
        ),
        Container(
            *[Link(f"{phone['name']} page", href=phone["route"]) for phone in PHONES],
            class_name="cluster",
        ),
        footer(),
        title="Compare - Product Showcase",
    )
