from PIL import Image
import base64
import io
import pandas as pd
from typing import Tuple, Union


def decode_file_data(
    encoded_data, metadata: bool = False
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


def file_data_to_dataframe(file_data) -> pd.DataFrame:
    """
    Converts a file object into a pandas DataFrame

    Args:
        file_data (io.BytesIO): Decoded file data (e.g. from decode_file_data)

    Raises:
        pd.errors.ParserError: If the file data cannot be converted to a DataFrame (i.e. file is not an Excel or CSV file or is corrupted)

    Returns:
        pd.DataFrame: DataFrame created from file data
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
    Converts a base64 encoded file data into a pandas DataFrame

    Args:
        file (str): Base64 encoded file data

    Returns:
        pd.DataFrame: DataFrame created from file data
    """

    fileData = decode_file_data(file)
    return file_data_to_dataframe(fileData)


def dataframe_to_output(
    df, DownloadText: str = "Download File", DownloadFileName: str = "myfile"
) -> Tuple[str, str]:
    # TODO: Add selection of CSV or Excel for download
    """
    Creates an HTML table and a download link for a given DataFrame

    Args:
        df (pandas.df): DataFrame to be converted
        DownloadText (str, optional): Text to be displayed as the download link (Defaults to "Download File")
        DownloadFileName (str, optional): Name of file when downloaded (Defaults to "myfile")

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


def input_to_PIL(file) -> Tuple[Image.Image, str]:
    """
    converts a Base64 encoded file data into a pillow image

    Args:
        file (str): Base64 encoded file data

    Returns:
        Tuple[Image.Image, str]: pillow image, metadata
    """

    [fileData, metaData] = decode_file_data(file, metadata=True)

    # Convert the file data into a Pillow's Image
    img = Image.open(fileData)

    return img, metaData


def print_img(
    img: Image.Image,
    metadata: str,
    WIDTH: int = 200,
    HEIGHT: int = 200,
    OriginalSize: bool = False,
    DownloadText: str = "Download Image",
    ImageName: str = "myimg",
) -> Tuple[str, str]:
    """
    Converts a pillow image into an HTML image and a download link

    Args:
        img (PIL.Image.Image): Pillow image
        metadata (str): Image metadata
        WIDTH (int, optional): Output width of the image in pixels (Defaults to 200)
        HEIGHT (int, optional): Output height of the image in pixels (Defaults to 200)
        OriginalSize (bool, optional): If True, the HTML image will be displayed in its original size (Defaults to False)
        DownloadText (str, optional): The text to be displayed on the download link (Defaults to "Download Image")
        ImageName (str, optional): download file name (Defaults to 'myimg')

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

    # It seems tempting to use displayImg.format here, but it doesn't work for some reason
    displayImg.save(displayBuffer, format=img.format)

    # Get the encoded data
    encoded_display_data = (
        metadata + base64.b64encode(displayBuffer.getvalue()).decode()
    )

    # Convert Display image to HTML
    image = f"<img src='{encoded_display_data}'>"

    # Convert full resolution image to an HTML download link
    downloadLink = f"<a href='{encoded_data}' download='{ImageName}.{img.format}'>{DownloadText}</a>"

    return image, downloadLink
