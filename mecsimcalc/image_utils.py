import base64
import io
from typing import Union, Tuple
from PIL import Image

from general_utils import decode_input_file, metadata_to_filetype


def file_to_PIL(file: io.BytesIO) -> Image.Image:
    """
    Converts a file object into a pillow image

    Args:
        file (io.BytesIO): Decoded file data (e.g. from decode_file_data)

    Returns:
        Image.Image: Pillow image created from file data
    """

    return Image.open(file)


def input_to_PIL(
    file: str, getFileType: bool = False
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    converts a Base64 encoded file data into a pillow image

    Args:
        file (str): Base64 encoded file data
        getType (bool, optional): If True, function returns the image type (Defaults to False)

    Returns:
        str: pillow image (if getType is False)
        Tuple[Image.Image, str]: pillow image, fileType (if getType is True)
    """

    (fileData, metadata) = decode_input_file(file, metadata=True)

    # Convert the file data into a Pillow's Image
    img = Image.open(fileData)

    # Get the image type, if requested
    if getFileType:
        fileType = metadata_to_filetype(metadata)
        return img, fileType

    return img


def print_img(
    img: Image.Image,
    fileType: str = "png",
    WIDTH: int = 200,
    HEIGHT: int = 200,
    OriginalSize: bool = False,
    download: bool = False,
    DownloadText: str = "Download Image",
    ImageName: str = "myimg",
) -> Union[str, Tuple[str, str]]:
    """
    Converts a pillow image into an HTML image and a download link

    Args:
        img (PIL.Image.Image): Pillow image
        fileType (str, optional): Image file type (Defaults to "png")
        WIDTH (int, optional): Output width of the image in pixels (Defaults to 200)
        HEIGHT (int, optional): Output height of the image in pixels (Defaults to 200)
        OriginalSize (bool, optional): If True, the HTML image will be displayed in its original size (Defaults to False)
        download (bool, optional): If True, the download link will be displayed (Defaults to False)
        DownloadText (str, optional): The text to be displayed on the download link (Defaults to "Download Image")
        ImageName (str, optional): download file name (Defaults to 'myimg')

    Returns:
        str: HTML image (if download is False)
        Tuple[str, str]: HTML image, download link (if download is True)
    """
    displayImg = img.copy()

    # Convert file type to lowercase and remove the period
    fileType = fileType.lower().replace(".", "")

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

    if not OriginalSize:
        displayImg.thumbnail((WIDTH, HEIGHT))

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
    downloadLink = f"<a href='{encoded_data}' download='{ImageName}.{img.format}'>{DownloadText}</a>"

    return image, downloadLink
