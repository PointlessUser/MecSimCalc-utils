import io
import base64
import pandas as pd
from typing import Union, Tuple
import os

from general_utils import input_to_file, metadata_to_filetype


def file_to_dataframe(file: io.BytesIO) -> pd.DataFrame:
    """
    Converts a file object into a pandas DataFrame

    Args:
        file (io.BytesIO): Decoded file data (e.g. from decode_file_data)

    Raises:
        pd.errors.ParserError: If the file data cannot be converted to a DataFrame (i.e. file is not an Excel or CSV file or is corrupted)

    Returns:
        pd.DataFrame: DataFrame created from file data
    """

    df = None

    # try to read the file as a CSV, if that fails try to read it as an Excel file
    try:
        df = pd.read_csv(file)
    except Exception:
        df = pd.read_excel(file)

    # if df is None, then the file type is not supported
    if df is None:
        raise pd.errors.ParserError("File Type Not Supported")
    return df


def input_to_dataframe(
    inputFile: str, getFileType: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]:
    """
    Converts a base64 encoded file data into a pandas DataFrame

    Args:
        inputFile (str): Base64 encoded file data
        getFileType (bool, optional): If True, function returns the file type (Defaults to False)

    Returns:
        pd.DataFrame: DataFrame created from file data (if getFileType is False)
        Tuple[pd.DataFrame, str]: DataFrame created from file data, and file type (if getFileType is True)
    """
    # if getFileType is True return the DataFrame and the file type

    fileData, metadata = input_to_file(inputFile, metadata=True)

    # if getFileType is True return the DataFrame and the file type, otherwise just return the DataFrame
    if getFileType:
        return file_to_dataframe(fileData), metadata_to_filetype(metadata)
    else:
        return file_to_dataframe(fileData)


def print_dataframe(
    df: pd.DataFrame,
    download: bool = False,
    downloadText: str = "Download Table",
    downloadFileName: str = "myfile",
    downloadFileType: str = "csv",
) -> Union[str, Tuple[str, str]]:
    """
    Creates an HTML table and a download link for a given DataFrame

    Args:
        df (pandas.DataFrame): DataFrame to be converted
        download (bool, optional): If True, function returns a download link (Defaults to False)
        downloadText (str, optional): Text to be displayed as the download link (Defaults to "Download File")
        downloadFileName (str, optional): Name of file when downloaded (Defaults to "myfile")
        downloadFileType (str, optional): File type of download (Defaults to "csv")

    Returns:
        str: HTML table (if download is False)
        Tuple[str, str]: HTML table, and download link (if download is True)
    """

    # TODO allow for large spreadsheets to be downloaded

    # create HTML table if download is False
    if not download:
        return df.to_html()

    downloadFileType = downloadFileType.lower()

    # check if file type is an alias of excel
    if downloadFileType in {
        "excel",
        "xlsx",
        "xls",
        "xlsm",
        "xlsb",
        "odf",
        "ods",
        "odt",
    }:
        # set file extension to xlsx
        extension = "xlsx"

        # create excel file and download link
        df.to_excel(f"{downloadFileName}.xlsx", index=False)

        # Read the file as binary
        with open(f"{downloadFileName}.xlsx", "rb") as f:
            data = f.read()

        # Encode the binary data into base64
        encoded_data = base64.b64encode(data).decode()

        # Add the base64 encoded data to the data URI
        encoded_data = (
            "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
            + encoded_data
        )

    else:
        # set file extension to csv
        extension = "csv"

        # create csv file and download link
        df.to_csv(f"{downloadFileName}.csv", index=False)
        csv_file = df.to_csv(index=False)
        encoded_data = (
            "data:text/csv;base64," + base64.b64encode(csv_file.encode()).decode()
        )

    # Create the download link
    download_link = f"<a href='{encoded_data}' download='{downloadFileName}.{extension}'>{downloadText}</a>"

    # remove the file
    if os.path.isfile(f"{downloadFileName}.{extension}"):
        os.remove(f"{downloadFileName}.{extension}")

    return df.to_html(), download_link
