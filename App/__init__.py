"""This file is so Python identifies this folder as a package.
This should import all app windows."""

# The imports below exist so we can import as:
# import app
# root = app.MainWindow()

# instead of :
# from app import MainWindow
# root = main_window.MainWindow()

# or

# import app
# root = app.main_window.MainWindow()

# The dot before the file name means python should try to import a file in this same folder.
# from .file import SomeClass, SomeVariable, SomeFunction, ...

from .main_window import MainWindow
