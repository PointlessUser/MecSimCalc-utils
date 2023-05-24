import base64


def str_to_file(
    text: str,
    filename: str = "myfile",
    download_text: str = "Download File",
) -> str:
    """
    Generates a downloadable text file containing the given text.

    Args:
        text (str): Text to be downloaded.
        filename (str, optional): Name of the download file. Defaults to "myfile".
        download_text (str, optional): Text to be displayed as the download link. Defaults to "Download File".

    Raises:
        TypeError: If text is not a string.

    Returns:
        str: HTML text download link.
    """
    extension = ".txt"

    # Add a dot to the extension if it doesn't have one
    if extension[0] != "." and extension != "":
        extension = f".{extension}"

    # Encode the text
    encoded_text = base64.b64encode(text.encode()).decode()
    mime_type = "data:text/plain;base64,"
    encoded_data = mime_type + encoded_text

    # Return the download link
    return (
        f"<a href='{encoded_data}' download='{filename}{extension}'>{download_text}</a>"
    )
