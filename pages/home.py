"""Home page.

Hero, featured phones, and a CTA into the full comparison page. Phone
data comes from content.phones so this file stays presentation-only.
The featured section is built directly (not via components.section)
because it needs an `id` on its heading as the scroll-to target for the
hero's CTA button -- `section()` doesn't expose that hook.
"""

from arklight import Page, Heading, Text, Container, Link
from components.nav import nav
from components.footer import footer
from components.hero import hero
from components.card import card
from content.phones import PHONES


def home():
    return Page(
        nav(),
        hero(
            "Product Showcase",
            "Three phones, three price points, one place to compare them.",
            "See the lineup",
            "#featured",
            "assets/images/hero/hero.jpg",
            image_alt="Product showcase hero image",
        ),
        Container(
            Heading("Featured phones", level=2, id="featured"),
            Container(*[card(phone) for phone in PHONES], class_name="grid"),
            class_name="stack",
        ),
        Container(
            Heading("Not sure which one fits?", level=2),
            Text("Compare specs side by side across all three phones."),
            Link("Open comparison", href="/compare", class_name="button-link"),
            class_name="stack cta",
        ),
        footer(),
        title="Home - Product Showcase",
    )
