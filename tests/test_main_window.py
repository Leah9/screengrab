"""
This module implements assertions tests on the main window. When run,
they should raise AssertionErrors if something isn't right with the code.

To run this you'll need pytest installed. Then make sure to run pytest from
this repository's root folder.

Example on how to run pytest (this may vary on each machine):
pytest
python -m pytest
py -m pytest
"""

import os
from tkinter import TclError
import pytest
from PIL import Image
import App

if not os.path.exists("img"):
    os.makedirs("img")


@pytest.mark.parametrize(
    "left,top,right,down",
    [
        (0, 0, 1920, 1080),
        (1000, 80, 1920, 1080),
        (0, 0, 100, 1080),
        (0, 0, 1920, 100),
        (1, 1, 100, 1080),
        (1, 1, 1920, 100),
        (0, 0, 200, 200),
        (200, 200, 400, 400),
        (200, 200, 450, 450),
        (250, 250, 400, 400),
    ],
)
def test_capture_sizes(left, top, right, down):
    """
    This will assert capture_button_clicked captures images of the
    correct expected size.
    """
    try:
        # Sometimes this will throw a TclError (??)
        root = App.MainWindow(left, top, right, down)
    except TclError:
        # If we try again it usually works
        root = App.MainWindow(left, top, right, down)
        # (my guess is that it tries to access a file that's
        # still being used by the last test)

    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.destroy()

    image = Image.open(os.path.join(root.img_dir, "image1001.png"), mode="r")
    assert image.size == (right - left, down - top)

    image = Image.open(os.path.join(root.img_dir, "image1002.png"), mode="r")
    assert image.size == (right - left, down - top)

    image = Image.open(os.path.join(root.img_dir, "image1003.png"), mode="r")
    assert image.size == (right - left, down - top)

    image = Image.open(os.path.join(root.img_dir, "image1004.png"), mode="r")
    assert image.size == (right - left, down - top)
