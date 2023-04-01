from PIL import Image
import base64
import io

def printImg(img, metadata, WIDTH: int = 200, HEIGHT: int = 200, OriginalSize: bool = False, DownloadText: str = 'Download Image'):
    
    displayImg = img.copy()

    if not OriginalSize:
        displayImg.thumbnail((WIDTH, HEIGHT))

    # Get downloadable data (Full Resolution)
    buffer = io.BytesIO()
    img.save(buffer, format=img.format)
    encoded_data = metadata + \
        base64.b64encode(buffer.getvalue()).decode()
        
    # Get displayable data (Custom Resolution)
    displayBuffer = io.BytesIO()
    displayImg.save(displayBuffer, format=img.format) # It seems tempting to use displayImg.format here, but it doesn't work for some reason
    encoded_display_data = metadata + \
        base64.b64encode(displayBuffer.getvalue()).decode()

    # Convert Display image to HTML 
    image = f"<img src='{encoded_display_data}'>"
    
    # Convert full resolution image to an HTML download link
    downloadLink = f"<a href='{encoded_data}' download='myimg.{img.format}'>{DownloadText}</a>"

    return image, downloadLink


def inputToPIL(file):
    [meta, data] = file.split(";base64,")
    metadata = f"{meta};base64,"

    # Decode the file data
    file_data = io.BytesIO(base64.b64decode(data))

    # Convert the file data into a Pillow's Image
    img = Image.open(file_data)

    return img, metadata
