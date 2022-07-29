"""
This file is where the main window of the App is implemented.
"""

import os
import time
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
import pyautogui
from PIL import Image
from fpdf import FPDF # Note both fpdf and fpdf2 are installed as fpdf. fpdf2 is required.
from . import top_levels


class MainWindow(tk.Tk):
    """Main window of the App."""

    def __init__(self, x1=0, y1=0, x2=640, y2=480):  # Use sensible defaults.
        super().__init__()
        self.title("ScreenGrab")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        # self.image_no = 1001
        self.show_image = False
        self.pages = tk.IntVar(master=self, value=5)
        self.auto_hide = tk.BooleanVar(master=self, value=True)
        self.params = {
            "width": 11,
            "pady": 8,
            "ipady": 12,
            "padding": 2,
            "borderwidth": 3,
            "button_bg": "#DEDEDE",
            "font": "helvetica 12",
        }
        self.option_add("*TCombobox*Listbox.font", self.params["font"])
        self.widgets = {}
        self.style = ttk.Style()
        # Checks for OS type, "Vista theme does not work on Linux".
        if os.name == "nt":
            self.style.theme_use("vista")
        self.style.configure("my.TButton", font=self.params["font"])
        # Set icon for main window, True also sets other called windows.
        self.iconphoto(True, tk.PhotoImage(file='./App/icon.png'))

        self._draw_screen()
        self.img_dir = "img"

        self.offset = {
            "x": int(0.05 * self.winfo_screenwidth()),
            "y": int(0.15 * self.winfo_screenheight()),
        }
        self.geometry(f"+{self.offset['x']}+{self.offset['y']}")

    def _draw_screen(self):
        """
        This function is inteded to be called when constructing this class (in __init__).
        This is where all the main widgets are supposed to be packed.
        """

        self.attributes("-topmost", True)  # Keeps GUI on top.
        self.config(padx=30, pady=15)
        # Place a label on the root window.
        message = tk.Label(self, text="ScreenGrab",
                           justify="right", font="arial 15")
        message.grid(row=0, column=0, columnspan=3, pady=10, sticky="NEWS")

        get_box_button = ttk.Button(
            self,
            text="Get Box",
            width=self.params["width"],
            style="my.TButton",
            command=self.get_box_button_clicked,
        )
        get_box_button.grid(
            row=1,
            column=0,
            padx=self.params["padding"],
            pady=self.params["padding"],
            ipady=self.params["ipady"],
            sticky="NEWS",
        )

        # Define the buttons.
        capture_button = ttk.Button(
            self,
            text="Capture",
            width=self.params["width"],
            style="my.TButton",
            command=self.capture_button_clicked,
        )
        capture_button.grid(
            row=2,
            column=0,
            padx=self.params["padding"],
            pady=self.params["padding"],
            ipady=self.params["ipady"],
            sticky="NEWS",
        )

        # Text box for number of pages.
        pages_entry_box_width = 1
        pages_entry_box = ttk.Entry(
            self,
            justify=tk.CENTER,
            width=pages_entry_box_width,
            font=self.params["font"],
            textvariable=self.pages,
        )
        pages_entry_box.grid(
            row=1,
            column=2,
            padx=(0, 2),
            pady=self.params["padding"] + 1,
            sticky="NEWS",
        )

        auto_button = ttk.Button(
            self,
            text="Auto Mode",
            width=self.params["width"] - pages_entry_box_width - 1,
            style="my.TButton",
            command=self.auto_button_clicked,
        )
        auto_button.grid(
            row=1,
            column=1,
            padx=self.params["padding"],
            pady=self.params["padding"],
            ipady=self.params["ipady"],
            ipadx=2,
            sticky="NEWS",
        )

        create_pdf_button = ttk.Button(
            self,
            text="Create PDF",
            width=self.params["width"],
            style="my.TButton",
            command=self.create_pdf_button_clicked,
        )
        create_pdf_button.grid(
            row=2,
            column=1,
            columnspan=2,
            padx=self.params["padding"],
            pady=self.params["padding"],
            ipady=self.params["ipady"],
            sticky="NEWS",
        )

        # Green
        self.hiding_gui = tk.PhotoImage(width=51, height=26)
        self.hiding_gui.put(("#52C788",), to=(0, 0, 24, 24)
                            )  # (LEFT, TOP, RIGHT, DOWN)
        # This is the box format that's going to be drawn with the given the colour in relation
        # to the PhotoImage.

        # Red
        self.showing_gui = tk.PhotoImage(width=51, height=26)
        self.showing_gui.put(("#F33",), to=(25, 0, 49, 24)
                             )  # (LEFT, TOP, RIGHT, DOWN)
        # This is the box format that's going to be drawn with the given the color in relation
        # to the PhotoImage.

        message = tk.Label(
            self,
            text=f"Auto Hide:\n{'ON' if self.auto_hide.get() else 'OFF'}",
            justify="center",
            font=self.params["font"],
        )
        message.grid(row=3, column=1)

        self.widgets["auto_hide_switch"] = tk.Checkbutton(
            self,
            image=self.showing_gui,
            selectimage=self.hiding_gui,
            bg="white",
            indicatoron=False,
            onvalue=True,
            offvalue=False,
            variable=self.auto_hide,
            offrelief="sunken",
            command=lambda: message.config(
                text=f"Auto Hide:\n{'ON' if self.auto_hide.get() else 'OFF'}"
            ),
        )
        self.widgets["auto_hide_switch"].grid(
            row=3, column=2, pady=self.params["pady"])
        self.widgets["auto_hide_switch"].bind(
            "<ButtonRelease-1>", self.switch_hiding_state
        )

    @property
    def region(self):
        """Property that returns a region."""
        return (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)

    @property
    def img_dir(self):
        """Property that returns the image directory."""
        return self._img_dir

    @img_dir.setter
    def img_dir(self, img_dir):
        """Property that sets the image directory."""
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        self._img_dir = img_dir

    def get_box_button_clicked(self):
        """
        This function will capture two points on the screen to create a bounding box.
        It's called when the Get Box button is clicked.
        """
        messagebox.showinfo(
            title="Attention: TOP LEFT",
            message="Position your mouse and press enter to capture TOP LEFT position.",
            # This specific icon removes the bell noise from the messagebox.
            icon="question",
            parent=self,
        )
        # print("Top left position in 5 seconds")
        # time.sleep(5)

        # pyautogui.position() gets the x and y position of the mouse the variable is an object.
        x1y1 = pyautogui.position()

        messagebox.showinfo(
            title="Attention: BOTTOM RIGHT",
            message="Position your mouse and press enter to capture BOTTOM RIGHT position",
            icon="question",
            parent=self,
        )
        # print("Capturing bottom right in 5 seconds")
        # time.sleep(5)
        x2y2 = pyautogui.position()

        # Update the values in the object
        self.x1, self.y1 = x1y1
        self.x2, self.y2 = x2y2
        print(self.region)
        messagebox.showinfo(
            title="Finished", message=f"Captured area was {self.region}", parent=self
        )

    def capture_button_clicked(self, control_hiding_state=True):
        """
        This will capture an screen shot of the bounding box area when called.
        Its main use is when the Capture button is clicked.
        """
        # print("Button clicked")
        # Hide GUI while capture takes place only if auto hide is True
        # print(f"Auto hide {self.auto_hide.get()}")
        # print("Show image " + str(self.show_image))
        if self.auto_hide.get() and control_hiding_state:
            self.withdraw()
            # Without the delay we capture a faded area of the GUI 0.2 seems to be the lowest delay
            time.sleep(0.2)
            image = pyautogui.screenshot(region=self.region)
            self.deiconify()
        else:
            time.sleep(0.1)
            image = pyautogui.screenshot(region=self.region)

        if self.show_image:
            image.show()

        curr_time = time.time()
        time_struct = time.localtime(curr_time)

        mili_sec = round(1000 * (round(curr_time, 3) - (curr_time // 1)))
        time_stamp = time.strftime(
            "%Y-%m-%d_%H%M%S", time_struct) + f"{mili_sec:03}"

        image.save(f"{self.img_dir}/SG_{time_stamp}.png")
        # self.image_no += 1
        # Testing statement
        # print(self.image_no) 

    def auto_button_clicked(self):
        """
        This will "auto click the capture button" (or, rather, call its function) for a
        the number of pages in the entry box.
        """
        self.show_image = False
        # This breaks auto capture, the 5 second delay is to allow the user to get focus on the
        # intended app / site to advance through pages e.g. Box.com
        # messagebox.showinfo(
        #    title="Attention",
        #    message="Press enter to start capturing the screen.",
        #    parent=self
        # )

        new_window = top_levels.AutoWindow(self)
        if not new_window.pressed_ok:
            return

        button = new_window.button_selected.get()
        print(button)

        print("Starting auto capture in 5 seconds")
        # self.auto_hide.set(False)
        # time.sleep(5) 
        if self.auto_hide.get():
            self.withdraw()
        new_window = top_levels.CountdownWindow(self)
        if not new_window.pressed_cancel:
            # If the sleep timer is any shorter the image captured may show transition effects.
            time.sleep(0.1)
            for curr_img in range(1, self.pages.get() + 1):
                self.capture_button_clicked(control_hiding_state=False)
                pyautogui.press(button)
                print(f"Captured image {curr_img:03}")
            messagebox.showinfo(
                title="Success", message="Finished capturing screen.", parent=self
            )
        if self.auto_hide.get():
            self.deiconify()

    def create_pdf_button_clicked(self):
        """
        This function will combine all images in the img_dir folder into Binder.PDF in the root rolder of the app.
        """
        print("Getting list of images from img_dir folder")
        images_list = os.listdir(self.img_dir)
        print(images_list)
        pdf = FPDF(
            "l", "pt", "A4"
        )  # These defaults are required, Init pdf l = landscape, pt = points / pixels, A4 is the default size.
        pdf.set_auto_page_break(True)
        pdf.set_margins(0, 0)
        for img in images_list:
            timage = Image.open(f"{self.img_dir}/{img}")
            print(timage.width, timage.height)
            # Below will add a page the same size as the image.
            pdf.add_page(format=(timage.height, timage.width))
            # Format keyword gives an error if using fpdf, fpdf2 is required.
            # Please remove fpdf 'pip uninstall fpdf' then 'pip install fpdf2'.
            pdf.image(f"{self.img_dir}/{img}")
        # Save the compiled images as a pdf document.   
        pdf.output("Binder.pdf")
        messagebox.showinfo(
            title="Success", message="Finished creating PDF.", parent=self
        )

    def switch_hiding_state(self, _event=None):
        """
        This function switchs the "hiding state" of the window every time it's called
        This is used to decide whether the main window is going to hide during auto mode.
        """
        self.widgets["auto_hide_switch"].configure(
            image=self.showing_gui if self.auto_hide.get() else self.hiding_gui
        )
