import pytest

from mecsimcalc import string_to_file


def test_string_to_file():
    # download text from url
    text = getText()
    text = string_to_file(text)
    assert text.startswith("<a href=")


def getText():
    return "This is some text."
