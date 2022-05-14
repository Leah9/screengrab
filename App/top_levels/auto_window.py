"""This is a window that will pop up when selecting auto mode.
You'll find the button options here."""

import tkinter as tk
from tkinter import ttk


class AutoWindow(tk.Toplevel):
    """This is a pop up window for selecting the button press of the
    \rauto_button_clicked function"""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Auto Mode")
        self.parent = parent
        self.pressed_ok = False
        self.button_selected = tk.StringVar(master=self, value="Down")
        self.buttons_available = ["Down", "Up", "PageDown", "PageUp", "Enter"]
        self.inputs = {}

        self.config(padx=55, pady=25)
        self.attributes("-topmost", True)
        self._draw_window()

        x_offset = parent.x_offset + (parent.winfo_width() / 3)
        y_offset = parent.y_offset + (parent.winfo_height() / 3)
        self.geometry(f"+{int(x_offset)}+{int(y_offset)}")

        self.grab_set()
        # "parent.wait_window" needs to be the last thing this GUI calls when constructing itself.
        parent.wait_window(self)

    def _draw_window(self):
        self.inputs["OpMenu"] = ttk.Combobox(
            self,
            textvariable=self.button_selected,
            state="readonly",
            values=self.buttons_available,
            justify="center",
            width=self.parent.params["width"] - 1,
        )
        self.inputs["OpMenu"].pack(pady=4, ipady=8)
        self.inputs["OpMenu"].bind(
            "<<ComboboxSelected>>", lambda e: self.inputs["OkBTN"].focus_force()
        )

        self.inputs["OkBTN"] = ttk.Button(
            master=self,
            text="OK",
            style="my.TButton",
            padding=(0, 11, 0, 11),
            width=self.parent.params["width"] - 2,
            command=self.close_window,
        )

        self.inputs["OkBTN"].pack(pady=4)

    def close_window(self):
        """When the user presses ok on this window this function will be called.
        \rIt will set pressed_ok to true and close the window."""
        self.pressed_ok = True
        self.destroy()
