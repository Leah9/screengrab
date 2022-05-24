"""
Main file of the ScreenGrab tool.
Use to grab docs or images from screen one page at a time.
"""

import pyautogui
import App


def main():
    """Main function"""

    # Init Tkinter call our GUI root
    root = App.MainWindow(0, 0, 1920, 1080)

    print("get box :" + str(root.region))
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.5
    print(pyautogui.size())  # Prints screen resolution
    print(root.img_dir)

    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
