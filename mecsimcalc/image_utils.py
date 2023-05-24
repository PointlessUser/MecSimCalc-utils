import base64
import io
from typing import Union, Tuple

from PIL import Image

from general_utils import input_to_file, metadata_to_filetype


def file_to_PIL(file: io.BytesIO) -> Image.Image:
    """
    Converts a file object into a pillow image

    Args:
        file (io.BytesIO): Decoded file data (returned by input_to_file)

    Returns:
        PIL.Image.Image: Pillow image created from file data
    """
    return Image.open(file)


def input_to_PIL(
    input_file: str, get_file_type: bool = False
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    Converts a Base64 encoded file data into a pillow image

    Args:
        input_file (str): Base64 encoded file data
        get_file_type (bool, optional): If True, function returns the file type (Defaults to False)

    Returns:
        PIL.Image.Image: pillow image (if get_file_type is False)
        Tuple[PIL.Image.Image, str]: pillow image, fileType (if get_file_type is True)
    """
    # Decode the file data and extract the metadata
    file_data, metadata = input_to_file(input_file, metadata=True)

    # Convert the file data into a Pillow Image
    img = Image.open(file_data)

    # Get the image type if get_file_type is True
    if get_file_type:
        file_type = metadata_to_filetype(metadata)
        return img, file_type

    # Return just the image if get_file_type is False
    return img


def print_img(
    img: Image.Image,
    width: int = 200,
    height: int = 200,
    original_size: bool = False,
    download: bool = False,
    download_text: str = "Download Image",
    download_file_name: str = "myimg",
    download_file_type: str = "png",
) -> Union[str, Tuple[str, str]]:
    """
    Converts a pillow image into an HTML image and a download link

    Args:
        img (PIL.Image.Image): Pillow image
        width (int, optional): Output width of the image in pixels. Defaults to 200.
        height (int, optional): Output height of the image in pixels. Defaults to 200.
        original_size (bool, optional): If True, the HTML image will be displayed in its original size. Defaults to False.
        download (bool, optional): If True, the download link will be displayed. Defaults to False.
        download_text (str, optional): The text to be displayed on the download link. Defaults to "Download Image".
        download_file_name (str, optional): Download file name. Defaults to 'myimg'.
        download_file_type (str, optional): File type of download. Defaults to "png".

    Returns:
        Union[str, Tuple[str, str]]: HTML image (if download is False), or HTML image and download link (if download is True)
    """
    display_img = img.copy()

    # Convert file type to lowercase and remove the period
    file_type = download_file_type.lower().replace(".", "")

    # Convert file type to the correct format
    if file_type == "jpg":
        file_type = "jpeg"
    elif file_type == "tif":
        file_type = "tiff"
    elif file_type == "ico":
        file_type = "x-icon"
    elif file_type == "svg":
        file_type = "svg+xml"

    # If filetype doesn't exist, it automatically defaults to png
    metadata = f"data:image/{file_type};base64,"

    if not original_size:
        display_img.thumbnail((width, height))

    # Get downloadable data (Full Resolution)
    buffer = io.BytesIO()
    img.save(buffer, format=img.format)
    encoded_data = metadata + base64.b64encode(buffer.getvalue()).decode()

    # Get displayable data (Custom Resolution)
    display_buffer = io.BytesIO()

    # It seems tempting to use display_img.format here, but it doesn't work for some reason
    display_img.save(display_buffer, format=img.format)

    # Get the encoded data
    encoded_display_data = (
        metadata + base64.b64encode(display_buffer.getvalue()).decode()
    )

    # Convert Display image to HTML
    image = f"<img src='{encoded_display_data}'>"

    if not download:
        return image

    # Convert full resolution image to an HTML download link
    download_link = f"<a href='{encoded_data}' download='{download_file_name}.{img.format}'>{download_text}</a>"

    return image, download_link
