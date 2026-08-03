"""Reusable product card.

Takes one entry from content.phones.PHONES and renders it as a card.
Plain function composition -- see components/section.py for the same
pattern applied to section wrappers.
"""

from arklight import Container, Image, Heading, Text, List, Item, Link


def card(phone):
    return Container(
        Image(src=phone["image"], alt=phone["name"], loading="lazy"),
        Heading(phone["name"], level=3),
        Text(phone["tagline"], class_name="muted"),
        Text(phone["price"], class_name="price", style={"font-weight": "700", "font-size": "1.15em"}),
        List(*[Item(highlight) for highlight in phone["highlights"]]),
        Link("View details", href=phone["route"]),
        class_name="card",
    )
