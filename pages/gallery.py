"""Gallery page -- demonstrates Picture, Figure, and FigCaption.

Reuses each phone's hero image from content.phones rather than a
separate gallery asset set. The Picture/PictureSource pairing here is
illustrative -- swap in real art-directed crops (a different image per
breakpoint) once actual product photography variants exist.
"""

from arklight import Page, Heading, Text, Container, Figure, FigCaption, Image, Picture, PictureSource
from components.nav import nav
from components.footer import footer
from content.phones import PHONES


def gallery():
    return Page(
        nav(),
        Heading("Gallery"),
        Text("A quick look at the lineup.", class_name="muted"),
        Container(
            *[
                Figure(
                    Picture(
                        PictureSource(srcset=phone["image"], media="(min-width: 800px)"),
                        Image(src=phone["image"], alt=phone["name"], loading="lazy"),
                    ),
                    FigCaption(f"{phone['name']} -- {phone['tagline']}"),
                )
                for phone in PHONES
            ],
            class_name="grid",
        ),
        footer(),
        title="Gallery - Product Showcase",
    )
