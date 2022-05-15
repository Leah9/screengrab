"""
This module implements assertions tests on the main window. When run,
they should raise AssertionErrors if something isn't right with the code.
If all assertions pas the package should print "PASSED".

Read this package's __main__.py docstring for guidance on how to run it.
"""

import os
from PIL import Image
import App


def capture_size_full_screen():
    """This will assert capture_button_clicked captures images of the
    \rcorrect expected size: (1920, 1080)"""
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


def capture_size_small_box():
    """This will assert capture_button_clicked captures images of the
    \rcorrect expected size: (200, 200)."""
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
