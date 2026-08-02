"""Phone data.

Plain Python -- no ARKlight involved here at all. Pages import this and
loop over it, keeping specification data out of presentation code.
Specs are approximate/representative for showcase purposes; update with
exact figures before shipping.

Note: `route` and `image`'s folder name are independent strings by
design (e.g. iQOO Neo 10R is routed at /neo10r but its asset folder is
iqooneo10r) -- don't assume they match when adding a phone. The
assert_asset_exists() call at the bottom of this file is what actually
guards against that class of mistake: it fails the build immediately
if a phone's image path is wrong, rather than letting a typo silently
404 in the browser.
"""

from content.validate import assert_asset_exists

PHONES = [
    {
        "slug": "redmi9a",
        "route": "/redmi9a",
        "name": "Redmi 9A",
        "tagline": "Dependable basics, all-day battery.",
        "price": "$109",
        "image": "assets/images/redmi9a/hero.jpg",
        "highlights": ["6.53\" HD+ display", "5000mAh battery", "MediaTek Helio G25"],
        "specs": [
            ("Display", "6.53\" HD+, 400 nits"),
            ("Chipset", "MediaTek Helio G25"),
            ("RAM / Storage", "3GB + 32GB"),
            ("Rear camera", "13MP single"),
            ("Battery", "5000mAh"),
            ("Charging", "10W wired"),
            ("OS", "Android 10"),
        ],
    },
    {
        "slug": "pocof4",
        "route": "/pocof4",
        "name": "POCO F4",
        "tagline": "Flagship-grade performance, sharp price.",
        "price": "$399",
        "image": "assets/images/pocof4/hero.jpg",
        "highlights": ["Snapdragon 870", "120Hz AMOLED", "67W fast charging"],
        "specs": [
            ("Display", "6.67\" AMOLED, 120Hz"),
            ("Chipset", "Snapdragon 870"),
            ("RAM / Storage", "6/8GB + 128/256GB"),
            ("Rear camera", "64MP main"),
            ("Battery", "4500mAh"),
            ("Charging", "67W wired"),
            ("OS", "Android 12"),
        ],
    },
    {
        "slug": "iqooneo10r",
        "route": "/neo10r",
        "name": "iQOO Neo 10R",
        "tagline": "Built for gaming, tuned for speed.",
        "price": "$329",
        "image": "assets/images/iqooneo10r/hero.jpg",
        "highlights": ["Snapdragon 8s Gen 3", "144Hz display", "120W flash charging"],
        "specs": [
            ("Display", "6.78\" AMOLED, 144Hz"),
            ("Chipset", "Snapdragon 8s Gen 3"),
            ("RAM / Storage", "8/12GB + 128/256GB"),
            ("Rear camera", "50MP OIS"),
            ("Battery", "5500mAh"),
            ("Charging", "120W wired"),
            ("OS", "Android 14"),
        ],
    },
]

for _phone in PHONES:
    assert_asset_exists(_phone["image"], context=f"content/phones.py ({_phone['slug']})")
