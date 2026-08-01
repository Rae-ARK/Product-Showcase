"""Specification table helpers.

Turns a phone's `specs` list of (label, value) tuples into a real
`Table`, used on each product page. `TableHeaderCell`/`TableCell` are
real containers per the schema, but plain text is all we need here.
"""

from arklight import Table, Caption, TableHead, TableBody, TableRow, TableHeaderCell, TableCell


def specs_table(phone):
    return Table(
        Caption(f"{phone['name']} full specifications"),
        TableHead(
            TableRow(
                TableHeaderCell("Spec"),
                TableHeaderCell("Detail"),
            )
        ),
        TableBody(
            *[
                TableRow(
                    TableHeaderCell(label, scope="row"),
                    TableCell(value),
                )
                for label, value in phone["specs"]
            ]
        ),
        class_name="specs-table",
    )


def compare_table(phones):
    """Side-by-side spec comparison across every phone.

    Assumes each phone's `specs` list uses the same labels in the same
    order (true for content/phones.py today) -- if that ever changes,
    this should key by label instead of zipping by position.
    """
    return Table(
        Caption("Full specification comparison"),
        TableHead(
            TableRow(
                TableHeaderCell("Spec"),
                *[TableHeaderCell(phone["name"]) for phone in phones],
            )
        ),
        TableBody(
            TableRow(
                TableHeaderCell("Price", scope="row"),
                *[TableCell(phone["price"]) for phone in phones],
            ),
            *[
                TableRow(
                    TableHeaderCell(phones[0]["specs"][i][0], scope="row"),
                    *[TableCell(phone["specs"][i][1]) for phone in phones],
                )
                for i in range(len(phones[0]["specs"]))
            ],
        ),
        class_name="specs-table compare-table",
    )
