import sys
import os
import pytest

import matplotlib.pyplot as plt
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from plotting_utils import print_plt


def test_print_plt():
    # convert file data to pillow image
    fig = make_fig()
    plt = make_plt()

    # try converting plot to html img
    fig_html = print_plt(fig)
    plt_html = print_plt(plt)

    # check that html img is correct
    assert fig_html.startswith("<img src='data:image/png;base64,")

    # check that html img is correct with download
    fig_html, downloadHTMLfig = print_plt(fig, download=True)
    plt_html, downloadHTMLplt = print_plt(plt, download=True)

    # check that html img is correct with download
    assert fig_html.startswith("<img src='data:image/png;base64,")
    assert plt_html.startswith("<img src='data:image/png;base64,")

    # check that download is correct
    assert downloadHTMLfig.startswith("<a href='data:image/png;base64,")
    assert downloadHTMLplt.startswith("<a href='data:image/png;base64,")


def make_fig():
    # make plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    ax.plot(x, y)
    return fig


def make_plt():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    plt.plot(x, y, label="sin(x)")
    plt.title("A Simple Plot")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    return plt
