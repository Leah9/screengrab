"""Main file of the ScreenGrab tool.
Use to grab docs or images from screen one page at a time.
"""

import os
import pyautogui
import App


def main():
    """Main function"""

    # Checking if directory exists.

    # Init Tkinter call our GUI root
    root = App.MainWindow(408, 146, 1683, 1037)

    if not os.path.exists(root.IMG_DIR):
        # Creates it in case it doesn't
        os.makedirs(root.IMG_DIR)

    print("get box :" + str(root.region))
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    print(pyautogui.size())  # Prints screen resolution
    # width, height = pyautogui.size()
    print(root.IMG_DIR)

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
