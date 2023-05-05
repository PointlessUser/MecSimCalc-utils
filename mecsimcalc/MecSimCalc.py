from PIL import Image
import base64
import io
import pandas as pd
from typing import Tuple, Union


def decode_file_data(
    encoded_data, metadata: bool = False
) -> Union[io.BytesIO, Tuple[str, io.BytesIO]]:
    """
    Converts a base64 encoded file data into a file object.

    Args:
        encoded_data (str): Base64 encoded file data
        metadata (bool, optional): If True, returns a tuple of (fileData, metadata). Defaults to False.

    Returns:
        io.BytesIO: fileData
        (io.BytesIO, str): fileData, metadata

    """

    meta, data = encoded_data.split(";base64,")

    file_data = io.BytesIO(base64.b64decode(data))
    meta_data = f"{meta};base64,"

    return (file_data, meta_data) if metadata else file_data


def file_data_to_dataframe(file_data) -> pd.DataFrame:
    """
    Converts a file object into a pandas dataframe

    Args:
        file_data (io.BytesIO): Decoded file data from decode_file_data()

    Raises:
        pd.errors.ParserError: If the file is not a CSV or Excel file (or if the file is corrupt)

    Returns:
        pd.DataFrame: a dataframe of the file data
    """

    try:
        df = pd.read_csv(file_data)
    except pd.errors.ParserError:
        df = pd.read_excel(file_data)
    except:
        raise Exception("File type not supported", pd.errors.ParserError)
    return df


def input_to_dataframe(file) -> pd.DataFrame:
    """
    Converts a base64 encoded file data into a pandas dataframe

    Args:
        file (str): base64 encoded file data

    Returns:
        pd.DataFrame: a dataframe of the file data
    """

    fileData = decode_file_data(file)
    return file_data_to_dataframe(fileData)


def dataframe_to_output(
    df, DownloadText: str = "Download File", DownloadFileName: str = "myfile"
) -> Tuple[str, str]:
    """
    Converts a pandas dataframe into an HTML table and a download link

    Args:
        df (df): pandas dataframe
        DownloadText (str, optional): download link text. Defaults to 'Download File'.
        DownloadFileName (str, optional): download file name. Defaults to 'myfile.csv'.

    Returns:
        Tuple[str, str]: HTML table, download link
    """

    csv_file = df.to_csv(index=False)
    encoded_data = (
        "data:text/csv;base64," + base64.b64encode(csv_file.encode()).decode()
    )

    return (
        df.to_html(),
        f"<a href='{encoded_data}'download='{DownloadFileName}.csv'>{DownloadText}</a>",
    )


def print_img(
    img,
    metadata,
    WIDTH: int = 200,
    HEIGHT: int = 200,
    OriginalSize: bool = False,
    DownloadText: str = "Download Image",
    ImageName: str = "myimg",
) -> Tuple[str, str]:
    """
    Converts a pillow image into an HTML image and a download link

    Args:
        img (PIL.Image): pillow image
        metadata (str): image metadata
        WIDTH (int, optional): width of the image. Defaults to 200.
        HEIGHT (int, optional): height of the image. Defaults to 200.
        OriginalSize (bool, optional): If True, the image will not be resized. Defaults to False.
        DownloadText (str, optional): download link text. Defaults to 'Download Image'.
        ImageName (str, optional): download file name. Defaults to 'myimg'.

    Returns:
        Tuple[str, str]: HTML image, download link
    """

    displayImg = img.copy()

    if not OriginalSize:
        displayImg.thumbnail((WIDTH, HEIGHT))

    # Get downloadable data (Full Resolution)
    buffer = io.BytesIO()
    img.save(buffer, format=img.format)
    encoded_data = metadata + base64.b64encode(buffer.getvalue()).decode()

    # Get displayable data (Custom Resolution)
    displayBuffer = io.BytesIO()
    displayImg.save(
        displayBuffer, format=img.format
    )  # It seems tempting to use displayImg.format here, but it doesn't work for some reason
    encoded_display_data = (
        metadata + base64.b64encode(displayBuffer.getvalue()).decode()
    )

    # Convert Display image to HTML
    image = f"<img src='{encoded_display_data}'>"

    # Convert full resolution image to an HTML download link
    downloadLink = f"<a href='{encoded_data}' download='{ImageName}.{img.format}'>{DownloadText}</a>"

    return image, downloadLink


def input_to_PIL(file) -> Tuple[Image.Image, str]:
    """
    converts a base64 encoded file data into a pillow image

    Args:
        file (str): base64 encoded file data

    Returns:
        Tuple[Image.Image, str]: pillow image, image metadata
    """

    [fileData, metaData] = decode_file_data(file, metadata=True)

    # Convert the file data into a Pillow's Image
    img = Image.open(fileData)

    return img, metaData
