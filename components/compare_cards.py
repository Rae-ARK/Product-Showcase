"""Responsive comparison cards.

A .switcher-based alternative to the flat comparison Table -- nothing
in .switcher's CSS ties it to any specific markup shape (it's a flex
rule on `> *` children), so it reflows any set of same-level children
from N columns on wide viewports to a single column on narrow ones.
Here it turns the phone lineup into per-phone spec cards instead of a
table that would otherwise need horizontal scroll on mobile.

This is presented as the primary comparison view; the full flat table
(components.specs.compare_table) remains available inside a collapsed
<details> on the compare page for anyone who wants every spec at once
in traditional table form.
"""

from arklight import Container, Heading, Text, List, Item, Link


def compare_cards(phones):
    return Container(
        *[
            Container(
                Heading(phone["name"], level=3),
                Text(phone["tagline"], class_name="muted"),
                Text(phone["price"], class_name="price"),
                List(
                    *[Item(f"{label}: {value}") for label, value in phone["specs"]]
                ),
                Link("View full page", href=phone["route"]),
                class_name="card",
            )
            for phone in phones
        ],
        class_name="switcher",
    )
