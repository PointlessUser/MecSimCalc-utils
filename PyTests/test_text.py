import sys
import os
import pytest
from PIL import Image
import pandas as pd
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from text_utils import str_to_file


def test_download_text():
    # download text from url
    text = getText()
    text = str_to_file(text)
    assert text.startswith("<a href=")


def getText():
    return "This is some text."
