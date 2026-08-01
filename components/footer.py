"""Shared site footer."""

from arklight import Footer, Container, Text, Link


def footer():
    return Footer(
        Container(
            Text("Product Showcase -- built with ARKlight v0.003.", class_name="muted"),
            Container(
                Link("Home", href="/"),
                Link("Compare", href="/compare"),
                Link("Gallery", href="/gallery"),
                class_name="cluster",
            ),
            class_name="stack",
        ),
        class_name="site-footer",
    )
