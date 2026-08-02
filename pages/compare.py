"""Compare page -- responsive card comparison, a quick-pick interactive
flow, and the full spec table tucked into a collapsible <details> for
anyone who wants every row at once.
"""

from arklight import (
    Page, Heading, Text, Container, Section, Link,
    Details, Summary, State, Button, Bind, Action,
)
from components.nav import nav
from components.footer import footer
from components.specs import compare_table
from components.compare_cards import compare_cards
from content.phones import PHONES

DEFAULT_PICK_MESSAGE = "Tap a phone below to see your pick here."

# NOTE: Page(..., style={...}) does nothing -- confirmed by reading
# arklight/backend/html/render.py's _render_page: for the Page node
# specifically, it only ever emits data-ark-state on <body>, silently
# dropping every other prop (style, class_name, id). That's a real
# ARKlight limitation, not a bug in this project. To widen just this
# page beyond the site-wide --ark-max-width (720px, set on <body>),
# this wraps the page content in a Container using a userland CSS
# full-bleed technique instead -- no compiler change involved.
WIDE_STYLE = {
    "max-width": "1100px",
    "width": "100vw",
    "position": "relative",
    "left": "50%",
    "transform": "translateX(-50%)",
}


def compare():
    return Page(
        # State(...) must be a direct child of Page(...) -- ARKlight's
        # validator rejects it nested inside a Section or Container.
        State("budget_pick", DEFAULT_PICK_MESSAGE),
        nav(),
        Container(
            Section(
                Heading("Compare"),
                Text("Every spec, side by side.", class_name="muted"),
                class_name="stack",
            ),
            Section(
                Heading("Quick pick", level=2),
                Text(Bind("budget_pick"), class_name="muted"),
                Container(
                    *[
                        Button(
                            phone["name"],
                            on_click=Action.set(
                                "budget_pick",
                                f"You picked the {phone['name']} -- {phone['price']}.",
                            ),
                        )
                        for phone in PHONES
                    ],
                    Button(
                        "Clear",
                        on_click=Action.set("budget_pick", DEFAULT_PICK_MESSAGE),
                        class_name="muted",
                    ),
                    class_name="cluster",
                ),
                class_name="stack",
            ),
            Section(
                Heading("Compare at a glance", level=2),
                compare_cards(PHONES),
                class_name="stack",
            ),
            Details(
                Summary("Full specification table"),
                compare_table(PHONES),
            ),
            Container(
                *[Link(f"{phone['name']} page", href=phone["route"]) for phone in PHONES],
                class_name="cluster",
            ),
            style=WIDE_STYLE,
        ),
        footer(),
        title="Compare - Product Showcase",
    )
