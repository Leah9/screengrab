# Use to grab docs or images from screen one page at a time

import pyautogui
import os
import App
from Globals import IMG_DIR
# import Globals


def main():
    # Checking if directory exists.
    if not os.path.exists(IMG_DIR):
        # Creates it in case it doesn't
        os.makedirs(IMG_DIR)

    # Init Tkinter call our GUI root
    root = App.MainWindow(408, 146, 1683, 1037)

    print("get box :" + str(root.region))
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    print(pyautogui.size())  # Prints screen resolution
    # width, height = pyautogui.size()

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()