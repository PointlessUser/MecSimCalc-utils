import html
import pandas as pd
from typing import List


def table_to_dataframe(
    column_headers: List[str], rows: List[List[str]]
) -> pd.DataFrame:
    """
    Create a DataFrame from given rows and column headers.

    Args:
        column_headers (List[str]): List of column headers
        rows (List[List[str]]): List of rows to be converted into a DataFrame. Each row is a list of strings
    Raises:
        AssertionError: If any row has a different length than the column headers
    Return:
        pd.DataFrame: DataFrame constructed from rows and headers
    """
    # Ensure that each row has the same length as the column headers
    for row in rows:
        assert len(row) == len(
            column_headers
        ), "Row length does not match column headers length"

    return pd.DataFrame(rows, columns=column_headers)


def print_table(column_headers: List[str], rows: List[List[str]]) -> str:
    """
    Create an HTML table from given rows and column headers.

    Args:
        column_headers (List[str]): The header for each column
        rows (List[List[str]]): A list of rows (each row is a list of strings)

    Return:
        str: HTML table
    """
    # Create the header row
    header_row = (
        "<tr>"
        + "".join(f"<th>{html.escape(header)}</th>" for header in column_headers)
        + "</tr>"
    )

    # Create the data rows
    data_rows = "".join(
        "<tr>" + "".join(f"<td>{html.escape(str(item))}</td>" for item in row) + "</tr>"
        for row in rows
    )

    # Return the table
    return f"<table border='3' cellpadding='5' style='border-collapse:collapse;'>{header_row}{data_rows}</table>"
