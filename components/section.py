"""Reusable section wrapper.

A thin helper around `Section` + optional `Heading` so pages don't repeat
the same three lines every time they need a titled block. Still just a
plain Python function -- ARKlight has no props-based component system yet.
"""

from arklight import Section, Heading, Container


def section(*children, title=None, class_name=None, level=2):
    heading = Heading(title, level=level) if title else None
    return Section(
        heading,
        Container(*children, class_name="stack"),
        class_name=class_name,
    )
