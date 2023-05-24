import io
import base64
import pandas as pd
from typing import Union, Tuple

from general_utils import decode_input_file, metadata_to_filetype


def file_to_dataframe(file_data: io.BytesIO) -> pd.DataFrame:
    """
    Converts a file object into a pandas DataFrame

    Args:
        file_data (io.BytesIO): Decoded file data (e.g. from decode_file_data)

    Raises:
        pd.errors.ParserError: If the file data cannot be converted to a DataFrame (i.e. file is not an Excel or CSV file or is corrupted)

    Returns:
        pd.DataFrame: DataFrame created from file data
    """

    df = None

    try:
        df = pd.read_csv(file_data)
    except Exception:
        df = pd.read_excel(file_data)

    if df is None:
        raise pd.errors.ParserError("File Type Not Supported")
    return df


def input_to_dataframe(
    file: str, getFileType: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]:
    """
    Converts a base64 encoded file data into a pandas DataFrame

    Args:
        file (str): Base64 encoded file data

    Returns:
        pd.DataFrame: DataFrame created from file data (if getFileType is False)
        Tuple[pd.DataFrame, str]: DataFrame created from file data, and file type (if getFileType is True)
    """
    if getFileType:
        fileData, fileType = decode_input_file(file, metadata=True)
        return file_to_dataframe(fileData), metadata_to_filetype(fileType)

    # if getFileType is False return only the DataFrame
    fileData = decode_input_file(file)
    return file_to_dataframe(fileData)


def print_dataframe(
    df: pd.DataFrame,
    download: bool = False,
    DownloadText: str = "Download Table",
    DownloadFileName: str = "myfile",
    fileType: str = "csv",
) -> Union[str, Tuple[str, str]]:
    """
    Creates an HTML table and a download link for a given DataFrame

    Args:
        df (pandas.DataFrame): DataFrame to be converted
        download (bool, optional): If True, function returns a download link (Defaults to False)
        DownloadText (str, optional): Text to be displayed as the download link (Defaults to "Download File")
        DownloadFileName (str, optional): Name of file when downloaded (Defaults to "myfile")
        FileType (str, optional): File type of download (Defaults to "csv")

    Returns:
        str: HTML table (if download is False)
        Tuple[str, str]: HTML table, and download link (if download is True)
    """

    if not download:
        return df.to_html()

    fileType = fileType.lower()

    # check if file type is an alias of excel
    if fileType in {
        "excel",
        "xlsx",
        "xls",
        "xlsm",
        "xlsb",
        "odf",
        "ods",
        "odt",
    }:
        # create excel file and download link
        df.to_excel(f"{DownloadFileName}.xlsx", index=False)

        # Read the file as binary
        with open(f"{DownloadFileName}.xlsx", "rb") as f:
            data = f.read()

        # Encode the binary data into base64
        encoded_data = base64.b64encode(data).decode()

        # Add the base64 encoded data to the data URI
        encoded_data = (
            "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
            + encoded_data
        )

        # Create the download link
        download_link = f"<a href='{encoded_data}' download='{DownloadFileName}.xlsx'>{DownloadText}</a>"

    # defaults to csv if file type is not excel
    else:
        # create csv file and download link
        df.to_csv(f"{DownloadFileName}.csv", index=False)
        csv_file = df.to_csv(index=False)
        encoded_data = (
            "data:text/csv;base64," + base64.b64encode(csv_file.encode()).decode()
        )
        download_link = f"<a href='{encoded_data}' download='{DownloadFileName}.csv'>{DownloadText}</a>"

    return df.to_html(), download_link
