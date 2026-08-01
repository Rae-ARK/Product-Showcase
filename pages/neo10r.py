"""iQOO Neo 10R product page."""

from arklight import Page, Heading, Text, Container, Section, List, Item, Details, Summary, Link
from components.nav import nav
from components.footer import footer
from components.hero import hero
from components.specs import specs_table
from content.phones import PHONES

PHONE = next(p for p in PHONES if p["slug"] == "iqooneo10r")


def neo10r():
    return Page(
        nav(),
        hero(
            PHONE["name"],
            PHONE["tagline"],
            "See full specs",
            "#specs",
            PHONE["image"],
            image_alt=PHONE["name"],
        ),
        Section(
            Heading("Why choose the iQOO Neo 10R", level=2),
            List(*[Item(highlight) for highlight in PHONE["highlights"]]),
            class_name="stack",
        ),
        Section(
            Heading("Full specifications", level=2, id="specs"),
            specs_table(PHONE),
            class_name="stack",
        ),
        Details(
            Summary("Shipping & warranty"),
            Text("Ships in 3-5 business days. Covered by a 1-year manufacturer warranty."),
        ),
        Container(
            Link("Compare with other phones", href="/compare"),
            Link("Back to all phones", href="/"),
            class_name="cluster",
        ),
        footer(),
        title=f"{PHONE['name']} - Product Showcase",
    )
