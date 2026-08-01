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
