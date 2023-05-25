import io
import base64
import re
from typing import Union, Tuple


def input_to_file(
    input_file: str, metadata: bool = False
) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]:
    """
    Transforms a base64 encoded string into an in-memory file-like object, along with optional metadata.

    Args:
        input_file (str): String of base64 encoded file data, prefixed with metadata.
        metadata (bool, optional): A flag indicating whether to return metadata with the file. Defaults to False.

    Raises:
        ValueError: If the input string doesn't contain ';base64,' which is required to separate metadata and file data.

    Returns:
        io.BytesIO: If metadata is False, returns a BytesIO object containing the decoded file data.
        (io.BytesIO, str): If metadata is True, returns a tuple containing the decoded file data and its metadata.
    """
    if ";base64," not in input_file:
        raise ValueError("Invalid input: must contain ';base64,'")

    meta, data = input_file.split(";base64,")
    file_data = io.BytesIO(base64.b64decode(data))
    meta_data = f"{meta};base64,"

    return (file_data, meta_data) if metadata else file_data


def metadata_to_filetype(metadata: str) -> str:
    """
    Parses the provided metadata to extract the file type.

    Args:
        metadata (str): Metadata string typically in the form "Data:<MIME type>;base64,"

    Returns:
        str: Extracted file type (e.g. "csv"). For a Microsoft Excel file, it returns "xlsx".
    """
    match = re.search(r"/(.+);base64,", metadata)
    file_type = match[1] if match else ""

    if file_type == "vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        file_type = "xlsx"

    return file_type
