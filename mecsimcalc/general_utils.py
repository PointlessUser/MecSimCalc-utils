import io
import base64
import re

from typing import Union, Tuple


def decode_input_file(
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


def metadata_to_filetype(metadata: str) -> str:
    """
    Converts a metadata string into file type string

    Args:
        metadata (str): Metadata string

    Returns:
        io.BytesIO: File object created from metadata
    """
    fileType = match[1] if (match := re.search(r"/(.+);base64,", metadata)) else ""

    if fileType == "vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        fileType = "xlsx"

    return fileType
