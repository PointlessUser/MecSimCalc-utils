import sys
import os
import pytest
import base64
import mimetypes
from PIL import Image
import io
import pandas as pd

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from general_utils import decode_input_file, metadata_to_filetype
from spreadsheet_utils import input_to_dataframe, file_to_dataframe, print_dataframe


def test_decode_input_file():
    # decode file data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # try decoding data with metadata
    fileCSV, metadataCSV = decode_input_file(inputCSV, metadata=True)
    fileXLSX, metadataXLSX = decode_input_file(inputXLSX, metadata=True)

    # for csvFile.csv, metadata should be "data:image/csv;base64,"
    # for xlsxFile.xlsx, metadata should be "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
    assert metadataCSV == "data:text/csv;base64,"
    assert (
        metadataXLSX
        == "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
    )
    assert isinstance(fileCSV, io.BytesIO)
    assert isinstance(fileXLSX, io.BytesIO)

    # try converting metadata to file type
    fileType = metadata_to_filetype(metadataCSV)
    assert fileType == "csv"

    fileType = metadata_to_filetype(metadataXLSX)
    assert fileType == "xlsx"

    # try decoding data without metadata
    file = decode_input_file(inputCSV)
    assert isinstance(file, io.BytesIO)

    file = decode_input_file(inputXLSX)
    assert isinstance(file, io.BytesIO)


# def test_file_to_dataframe():
def test_file_to_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # decode file data
    fileCSV = decode_input_file(inputCSV)
    fileXLSX = decode_input_file(inputXLSX)

    # convert file data to dataframe
    dfCSV = file_to_dataframe(fileCSV)
    dfXLSX = file_to_dataframe(fileXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)


def test_input_to_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # convert input data to dataframe
    dfCSV = input_to_dataframe(inputCSV)
    dfXLSX = input_to_dataframe(inputXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)


def test_print_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # convert input data to dataframe
    dfCSV = input_to_dataframe(inputCSV)
    dfXLSX = input_to_dataframe(inputXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # print dataframe
    dfHTMLcsv = print_dataframe(dfCSV)
    dfHTMLxlsx = print_dataframe(dfXLSX)

    # make sure html is a string
    assert dfHTMLcsv.startswith("<table")
    assert dfHTMLxlsx.startswith("<table")

    # convert input data to dataframe with metadata
    dfCSV, fileTypeCSV = input_to_dataframe(inputCSV, getFileType=True)
    dfXLSX, fileTypeXLSX = input_to_dataframe(inputXLSX, getFileType=True)

    # make sure dataframe is a pandas dataframe and file type is correct
    assert fileTypeCSV == "csv"
    assert fileTypeXLSX == "xlsx"
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # print dataframe
    dfHTMLcsv = print_dataframe(dfCSV, fileType=fileTypeCSV)
    dfHTMLxlsx = print_dataframe(dfXLSX, fileType=fileTypeXLSX)

    # make sure dfHTML is actually html
    assert dfHTMLcsv.startswith("<table")
    assert dfHTMLxlsx.startswith("<table")


# returns a base64 encoded image
def get_csv():
    return getSpreadsheetInput(os.path.join(THIS_DIR, "csvFile.csv"))


def get_xlsx():
    return getSpreadsheetInput(os.path.join(THIS_DIR, "xlsxFile.xlsx"), xlsx=True)


# returns a base64 encoded image
def getSpreadsheetInput(path, xlsx=False):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    if xlsx:
        metadata_string = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"

    return metadata_string + encoded_string


# returns part of the spreadsheet's metadata
def get_mime_type(file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    return mime_type


test_print_dataframe()
