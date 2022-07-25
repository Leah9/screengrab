"""
This is a window that will pop up when selecting auto mode.
This window counts 5 seconds and closes itself.
"""

import tkinter as tk
from tkinter import ttk


class CountdownWindow(tk.Toplevel):
    """
    This is a pop up window for counting down until the start of the screen shots
    auto_button_clicked function.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Countdown")
        self.pressed_cancel: bool = False
        self.countdown_var = tk.IntVar(master=self, value=5)
        self.widgets: dict = {}

        x_offset: int = 50
        y_offset: int = 50
        self.geometry(f"+{x_offset}+{y_offset}")

        self.config(padx=5, pady=5)
        self.attributes("-topmost", True)
        self._draw_window()

        self.grab_set()
        self.after(1000, self.count_down)
        # "parent.wait_window" needs to be the last thing this GUI calls when constructing itself.
        parent.wait_window(self)

    def _draw_window(self):
        self.widgets["Countdown_LB"] = tk.Label(
            self,
            textvariable=self.countdown_var,
            font="arial 18",
        )
        self.widgets["Countdown_LB"].pack(fill=tk.BOTH)

        self.widgets["Cancel_BTN"] = ttk.Button(
            master=self,
            text="Cancel",
            style="my.TButton",
            command=self.cancel_countdown,
        )

        self.widgets["Cancel_BTN"].pack(ipady=5, fill=tk.BOTH)

        self.widgets["Skip_BTN"] = ttk.Button(
            master=self,
            text="Skip",
            style="my.TButton",
            command=self.destroy,
        )

        self.widgets["Skip_BTN"].pack(ipady=5, fill=tk.BOTH)

    def cancel_countdown(self):
        """
        When the user presses cancel on this window this function will be called.
        It will set pressed_cancel to true and close the window.
        """
        self.pressed_cancel = True
        self.destroy()

    def count_down(self):
        """
        This function will call itself every second until self.countdown_var is about
        to hit 0.
        """
        current_count: int = self.countdown_var.get() - 1
        self.countdown_var.set(current_count)

        if current_count == 0:
            self.destroy()

        self.after(1000, self.count_down)


if __name__ == "__main__":
    # This section is so you can open only this window without going through
    # the main one (by running this file).
    import os
    import sys

    sys.path.insert(0, os.path.abspath("../.."))
    import App

    root = App.MainWindow(0, 0, 20, 20)
    root.withdraw()
    CD_window = CountdownWindow(root)
