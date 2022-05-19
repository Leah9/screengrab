"""
This is a window that will pop up when selecting auto mode.
You'll find the button options here.
"""

import tkinter as tk
from tkinter import ttk


class AutoWindow(tk.Toplevel):
    """
    This is a pop up window for selecting the button press of the
    auto_button_clicked function
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Auto Mode")
        self.parent = parent
        self.pressed_ok = False
        self.button_selected = tk.StringVar(master=self, value="Down")
        self.buttons_available = ["Down", "Up", "PageDown", "PageUp", "Enter"]
        self.inputs = {}

        self.config(padx=60, pady=35)
        self.attributes("-topmost", True)
        self._draw_window()

        self.withdraw()
        x_offset = self.parent.winfo_rootx() + self.parent.winfo_width() // 2
        y_offset = self.parent.winfo_rooty() + self.parent.winfo_height() // 2 - 30
        self.update()
        x_offset -= self.winfo_width() // 2
        y_offset -= self.winfo_height() // 2
        self.geometry(f"+{x_offset}+{y_offset}")
        self.deiconify()

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
            font=self.parent.params["font"],
            width=3 * self.parent.params["width"] // 2 - 1,
        )
        self.inputs["OpMenu"].pack(pady=4, ipady=8, fill=tk.BOTH)
        self.inputs["OpMenu"].bind(
            "<<ComboboxSelected>>", lambda event: self.inputs["OkBTN"].focus_force()
        )

        self.inputs["OkBTN"] = ttk.Button(
            master=self,
            text="OK",
            style="my.TButton",
            padding=(0, 11, 0, 11),
            width=3 * self.parent.params["width"] // 2 - 2,
            command=self.close_window,
        )

        self.inputs["OkBTN"].pack(pady=4, fill=tk.BOTH)

    def close_window(self):
        """
        When the user presses ok on this window this function will be called.
        It will set pressed_ok to true and close the window.
        """
        self.pressed_ok = True
        self.destroy()
