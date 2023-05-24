import io
import base64
import pandas as pd
import os
from typing import Union, Tuple

from general_utils import input_to_file, metadata_to_filetype


def file_to_dataframe(file: io.BytesIO) -> pd.DataFrame:
    """
    Converts a file object into a pandas DataFrame

    Args:
        file (io.BytesIO): Decoded file data

    Raises:
        pd.errors.ParserError: If the file data cannot be converted to a DataFrame
                               (i.e. file is not an Excel or CSV file or is corrupted)

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
    input_file: str, get_file_type: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]:
    """
    Converts a base64 encoded file data into a pandas DataFrame

    Args:
        input_file (str): Base64 encoded file data
        get_file_type (bool, optional): If True, function returns the file type (Defaults to False)

    Returns:
        pd.DataFrame: DataFrame created from file data (if get_file_type is False)
        Tuple[pd.DataFrame, str]: DataFrame created from file data, and file type (if get_file_type is True)
    """

    file_data, metadata = input_to_file(input_file, metadata=True)

    # if get_file_type is True return the DataFrame and the file type,
    # otherwise just return the DataFrame
    if get_file_type:
        return file_to_dataframe(file_data), metadata_to_filetype(metadata)
    else:
        return file_to_dataframe(file_data)


def print_dataframe(
    df: pd.DataFrame,
    download: bool = False,
    download_text: str = "Download Table",
    download_file_name: str = "myfile",
    download_file_type: str = "csv",
) -> Union[str, Tuple[str, str]]:
    """
    Creates an HTML table and a download link for a given DataFrame

    Args:
        df (pandas.DataFrame): DataFrame to be converted
        download (bool, optional): If True, function returns a download link (Defaults to False)
        download_text (str, optional): Text to be displayed as the download link (Defaults to "Download File")
        download_file_name (str, optional): Name of file when downloaded (Defaults to "myfile")
        download_file_type (str, optional): File type of download (Defaults to "csv")

    Returns:
        str: HTML table (if download is False)
        Tuple[str, str]: HTML table, and download link (if download is True)
    """

    # create HTML table if download is False
    if not download:
        return df.to_html()

    download_file_type = download_file_type.lower()

    # check if file type is an alias of excel
    if download_file_type in {
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
        df.to_excel(f"{download_file_name}.xlsx", index=False)

        # Read the file as binary
        with open(f"{download_file_name}.xlsx", "rb") as f:
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
        df.to_csv(f"{download_file_name}.csv", index=False)
        csv_file = df.to_csv(index=False)
        encoded_data = (
            "data:text/csv;base64," + base64.b64encode(csv_file.encode()).decode()
        )

    # Create the download link
    download_link = f"<a href='{encoded_data}' download='{download_file_name}.{extension}'>{download_text}</a>"

    # remove the file
    if os.path.isfile(f"{download_file_name}.{extension}"):
        os.remove(f"{download_file_name}.{extension}")

    return df.to_html(), download_link
