import base64


def download_text(
    text: str,
    filename: str = "myfile",
    extension: str = ".txt",
    download_text: str = "Download File",
) -> str:
    """
    Generates a downloadable text file containing the given text

    Args:
        text (str): Text to be downloaded
        filename (str, optional): Name of the download file. (Defaults to "myfile")
        extension (str, optional): Extension of the download file. (Defaults to ".txt")
        download_text (str, optional): Text to be displayed as the download link (Defaults to "Download File")

    Returns:
        str: HTML text download link
    """

    # Add a dot to the extension if it doesn't have one
    if extension[0] != "." and extension != "":
        extension = f".{extension}"

    # Encode the text
    newdata = base64.b64encode(text.encode()).decode()
    meta = "data:text/plain;base64,"
    encoded_data = meta + newdata

    # Return the download link
    return (
        f"<a href='{encoded_data}' download='{filename}{extension}'>{download_text}</a>"
    )
