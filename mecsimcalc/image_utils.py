import base64
import io
from typing import Union, Tuple
from PIL import Image

from general_utils import input_to_file, metadata_to_filetype


def file_to_PIL(file: io.BytesIO) -> Image.Image:
    """
    Converts a file object into a pillow image

    Args:
        inputFile (io.BytesIO): Decoded file data (returned by input_to_file)

    Returns:
        PIL.Image.Image: Pillow image created from file data
    """

    return Image.open(file)


def input_to_PIL(
    inputFile: str, getFileType: bool = False
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    converts a Base64 encoded file data into a pillow image

    Args:
        inputFile (str): Base64 encoded file data
        getFileType (bool, optional): If True, function returns the file type (Defaults to False)

    Returns:
        PIL.Image.Image: pillow image (if getFileType is False)
        Tuple[PIL.Image.Image, str]: pillow image, fileType (if getFileType is True)
    """

    # Decode the file data and extract the metadata
    (fileData, metadata) = input_to_file(inputFile, metadata=True)

    # Convert the file data into a Pillow Image
    img = Image.open(fileData)

    # Get the image type if getFileType is True
    if getFileType:
        fileType = metadata_to_filetype(metadata)
        return img, fileType

    # Return just the image if getFileType is False
    return img


def print_img(
    img: Image.Image,
    width: int = 200,
    height: int = 200,
    originalSize: bool = False,
    download: bool = False,
    downloadText: str = "Download Image",
    downloadFileName: str = "myimg",
    downloadFileType: str = "png",
) -> Union[str, Tuple[str, str]]:
    """
    Converts a pillow image into an HTML image and a download link

    Args:
        img (PIL.Image.Image): Pillow image
        width (int, optional): Output width of the image in pixels (Defaults to 200)
        height (int, optional): Output height of the image in pixels (Defaults to 200)
        originalSize (bool, optional): If True, the HTML image will be displayed in its original size (Defaults to False)
        download (bool, optional): If True, the download link will be displayed (Defaults to False)
        downloadText (str, optional): The text to be displayed on the download link (Defaults to "Download Image")
        downloadFileName (str, optional): Download file name (Defaults to 'myimg')
        downloadFileType (str, optional): File type of download (Defaults to "png")

    Returns:
        str: HTML image (if download is False)
        Tuple[str, str]: HTML image, download link (if download is True)
    """
    displayImg = img.copy()

    # Convert file type to lowercase and remove the period
    fileType = downloadFileType.lower().replace(".", "")

    # Convert file type to the correct format
    if fileType == "jpg":
        fileType = "jpeg"
    elif fileType == "tif":
        fileType = "tiff"
    elif fileType == "ico":
        fileType = "x-icon"
    elif fileType == "svg":
        fileType = "svg+xml"

    # if filetype doesn't exist, it automatically defaults to png
    metadata = f"data:image/{fileType};base64,"

    if not originalSize:
        displayImg.thumbnail((width, height))

    # Get downloadable data (Full Resolution)
    buffer = io.BytesIO()
    img.save(buffer, format=img.format)
    encoded_data = metadata + base64.b64encode(buffer.getvalue()).decode()

    # Get displayable data (Custom Resolution)
    displayBuffer = io.BytesIO()

    # It seems tempting to use displayImg.format here, but it doesn't work for some reason
    displayImg.save(displayBuffer, format=img.format)

    # Get the encoded data
    encoded_display_data = (
        metadata + base64.b64encode(displayBuffer.getvalue()).decode()
    )

    # Convert Display image to HTML
    image = f"<img src='{encoded_display_data}'>"

    if not download:
        return image

    # Convert full resolution image to an HTML download link
    downloadLink = f"<a href='{encoded_data}' download='{downloadFileName}.{img.format}'>{downloadText}</a>"

    return image, downloadLink
