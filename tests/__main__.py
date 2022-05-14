"""
This module will run tests on the App's functions.

To run this package, open the command prompt on this repository's root folder and type:

python -m tests
python3 -m tests
py -m tests

Or whatever way you call python in your machine followed by "-m tests".
"""

from . import test_main_window as test

test.capture_size_full_screen()
test.capture_size_small_box()

print("PASSED")