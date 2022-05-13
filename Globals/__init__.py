"""This file is so Python identifies this folder as a package."""

# The imports below exist so we can import as:
# from Globals import IMG_DIR

# instead of :
# from Globals.settings import IMG_DIR

# The dot before the file name means python should try to import a file in this same folder.
# from .file import SomeClass, SomeVariable, SomeFunction, ...
from .settings import * # "*" means import everything in there.
