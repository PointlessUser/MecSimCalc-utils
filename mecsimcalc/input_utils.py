from PIL import Image
import base64
import io
import pandas as pd
import re
from typing import Tuple, Union, List


def decode_file_data(
    encoded_data: str, metadata: bool = False
) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]:
    """
    Converts a base64 encoded file data into a file object and metadata

    Args:
        encoded_data (str): Base64 encoded file data
        metadata (bool, optional): If True, function returns file and metadata (Defaults to False)

    Returns:
        io.BytesIO: The decoded file data (if metadata is False)
        (io.BytesIO, str): The decoded file and metadata (if metadata is True)

    """

    meta, data = encoded_data.split(";base64,")

    file_data = io.BytesIO(base64.b64decode(data))
    meta_data = f"{meta};base64,"

    return (file_data, meta_data) if metadata else file_data


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


def input_to_dataframe(file: str) -> pd.DataFrame:
    """
    Converts a base64 encoded file data into a pandas DataFrame

    Args:
        file (str): Base64 encoded file data

    Returns:
        pd.DataFrame: DataFrame created from file data
    """

    fileData = decode_file_data(file)
    return file_to_dataframe(fileData)  # type: ignore


def input_to_PIL(
    file: str, getType: bool = True
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    converts a Base64 encoded file data into a pillow image

    Args:
        file (str): Base64 encoded file data
        getType (bool, optional): If True, function returns the image type (Defaults to False)

    Returns:
        str: pillow image (if getType is False)
        Tuple[Image.Image, str]: pillow image, imgType (if getType is True)
    """

    (fileData, metaData) = decode_file_data(file, metadata=True)

    # Convert the file data into a Pillow's Image
    img = Image.open(fileData)

    # Get the image type, if requested
    if getType:
        if match := re.search(r"image/(\w+);base64,", metaData):
            imgType = match[1]
        else:
            imgType = "png"

        return img, imgType
    return img


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
