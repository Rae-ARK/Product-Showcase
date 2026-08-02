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

    Keyed by spec label, not positional zip -- row order follows the
    first phone's spec order, but each cell is looked up by label in
    every other phone's own spec dict. A phone missing a given label
    (a different spec set, a future addition with fewer rows) renders
    "--" for that cell instead of silently pulling a mismatched value
    from the wrong position or raising an IndexError.
    """
    label_order = [label for label, _value in phones[0]["specs"]]
    spec_maps = [dict(phone["specs"]) for phone in phones]

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
                    TableHeaderCell(label, scope="row"),
                    *[TableCell(spec_map.get(label, "--")) for spec_map in spec_maps],
                )
                for label in label_order
            ],
        ),
        class_name="specs-table compare-table",
    )
