"""Main file of the ScreenGrab tool.
Use to grab docs or images from screen one page at a time.
"""

import os
import pyautogui
import app
from globals import IMG_DIR


def main():
    """Main function"""

    # Checking if directory exists.
    if not os.path.exists(IMG_DIR):
        # Creates it in case it doesn't
        os.makedirs(IMG_DIR)

    # Init Tkinter call our GUI root
    root = app.MainWindow(408, 146, 1683, 1037)

    print("get box :" + str(root.box))
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 2
    print(pyautogui.size())  # Prints screen resolution
    # width, height = pyautogui.size()

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
