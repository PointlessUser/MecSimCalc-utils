import pytest
import pandas as pd

from mecsimcalc import table_to_dataframe, print_table


def test_table_to_dataframe():
    # convert table data to pandas dataframe
    header, data = makeTable()
    df = table_to_dataframe(header, data)
    assert isinstance(df, pd.DataFrame)


def test_print_table():
    # convert table data to html table
    header, data = makeTable()
    HTMLtable = print_table(header, data)
    print(HTMLtable)
    assert HTMLtable.startswith("<table ")


def makeTable():
    header = ["A", "B", "C"]
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return header, data
