import pandas as pd
from typing import List


def table_to_dataframe(
    columns: List[List[str]], column_headers: List[str]
) -> pd.DataFrame:
    """
    Creates a DataFrame from given columns and column headers.

    Args:
        columns (List[List[str]]): List of columns to be converted into a DataFrame. Each column is a list of strings
        column_headers (List[str]): List of column headers
    Returns:
        pd.DataFrame: DataFrame constructed from columns and headers
    """

    # Create a dictionary mapping column headers to column values
    data_dict = dict(zip(column_headers, columns))

    return pd.DataFrame(data_dict)


def print_table(rows: List[List[str]], column_headers: List[str]) -> str:
    """
    Creates an HTML table from given rows and column headers.

    Args:
        rows (List[List[str]]): A list of rows (each row is a list of strings)
        column_headers (List[str]): The header for each column

    Returns:
        str: HTML table
    """

    # Create the header row
    header_row = (
        "<tr>" + "".join(f"<th>{header}</th>" for header in column_headers) + "</tr>"
    )

    # Create the data rows
    data_rows = "".join(
        "<tr>" + "".join(f"<td>{str(item)}</td>" for item in row) + "</tr>"
        for row in rows
    )

    # Return the table
    return f"<table border='3' cellpadding='5' style='border-collapse:collapse;'>{header_row}{data_rows}</table>"
