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
from PIL import Image
import App

if not os.path.exists("img"):
    os.makedirs("img")


def test_capture_size_full_screen():
    """
    This will assert capture_button_clicked captures images of the
    correct expected size: (1920, 1080)
    """
    root = App.MainWindow(0, 0, 1920, 1080)
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.destroy()

    image = Image.open(os.path.join(root.img_dir, "image1001.png"), mode="r")
    assert image.size == (1920, 1080)

    image = Image.open(os.path.join(root.img_dir, "image1002.png"), mode="r")
    assert image.size == (1920, 1080)

    image = Image.open(os.path.join(root.img_dir, "image1003.png"), mode="r")
    assert image.size == (1920, 1080)

    image = Image.open(os.path.join(root.img_dir, "image1004.png"), mode="r")
    assert image.size == (1920, 1080)


def test_capture_size_small_box():
    """
    This will assert capture_button_clicked captures images of the
    correct expected size: (200, 200).
    """
    root = App.MainWindow(200, 200, 400, 400)
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.capture_button_clicked()
    root.destroy()

    image = Image.open(os.path.join(root.img_dir, "image1001.png"), mode="r")
    assert image.size == (200, 200)

    image = Image.open(os.path.join(root.img_dir, "image1002.png"), mode="r")
    assert image.size == (200, 200)

    image = Image.open(os.path.join(root.img_dir, "image1003.png"), mode="r")
    assert image.size == (200, 200)

    image = Image.open(os.path.join(root.img_dir, "image1004.png"), mode="r")
    assert image.size == (200, 200)
