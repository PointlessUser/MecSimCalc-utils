import pandas as pd
from typing import List


def table_to_dataframe(columnHeaders: List[str], rows: List[List[str]]) -> pd.DataFrame:
    """
    Creates a DataFrame from given rows and column headers.

    Args:
        columnHeaders (List[str]): List of column headers
        rows (List[List[str]]): List of rows to be converted into a DataFrame. Each row is a list of strings
    raises:
        AssertionError: If any row has a different length than the column headers
    Returns:
        pd.DataFrame: DataFrame constructed from rows and headers
    """

    # Ensure that each row has the same length as the column headers
    for row in rows:
        assert len(row) == len(
            columnHeaders
        ), "Row length does not match column headers length"

    return pd.DataFrame(rows, columns=columnHeaders)


def print_table(columnHeaders: List[str], rows: List[List[str]]) -> str:
    """
    Creates an HTML table from given rows and column headers.

    Args:
        columnHeaders (List[str]): The header for each column
        rows (List[List[str]]): A list of rows (each row is a list of strings)

    Returns:
        str: HTML table
    """

    # Create the header row
    headerRow = (
        "<tr>" + "".join(f"<th>{header}</th>" for header in columnHeaders) + "</tr>"
    )

    # Create the data rows
    dataRows = "".join(
        "<tr>" + "".join(f"<td>{str(item)}</td>" for item in row) + "</tr>"
        for row in rows
    )

    # Return the table
    return f"<table border='3' cellpadding='5' style='border-collapse:collapse;'>{headerRow}{dataRows}</table>"
