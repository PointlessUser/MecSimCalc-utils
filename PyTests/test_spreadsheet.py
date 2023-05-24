import sys
import os
import pytest
import base64
import mimetypes
from PIL import Image
import io

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from general_utils import decode_file_data, metadata_to_filetype
from spreadsheet_utils import input_to_dataframe, file_to_dataframe, print_dataframe


# returns a base64 encoded image
def get_input():
    return getSpreadsheetInput(os.path.join(THIS_DIR, "csvFile.csv"))


# returns a base64 encoded image
def getSpreadsheetInput(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    return metadata_string + encoded_string


# returns part of the image metadata
def get_mime_type(file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    return mime_type
