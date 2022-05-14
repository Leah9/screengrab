"""This file is so Python identifies this folder as a package.
This should import all app windows."""

# The imports below exist so we can import as:
# import top_levels
# root = top_levels.AutoWindow()

# instead of :
# from top_levels import AutoWindow
# root = auto_window.AutoWindow()

# or

# import top_levels
# root = top_levels.auto_window.AutoWindow()

# The dot before the file name means python should try to import a file in this same folder.
# from .file import SomeClass, SomeVariable, SomeFunction, ...

from .auto_window import AutoWindow
