"""Hero banner.

Large introductory block for the home page. Real container (not Text),
since it mixes a heading, subtitle text, and a CTA button.
"""

from arklight import Header, Heading, Text, Button, Image


def hero(title, subtitle, cta_label, cta_target, image_src, image_alt=""):
    return Header(
        Image(src=image_src, alt=image_alt, loading="eager"),
        Heading(title, level=1),
        Text(subtitle, class_name="muted"),
        Button(
            cta_label,
            on_click="scroll-to",
            behavior_target=cta_target,
        ),
        class_name="hero",
    )
