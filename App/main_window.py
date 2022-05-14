"""This file is where the Class of the main window of the App is implemented."""

import os
import time
import tkinter as tk
from tkinter import messagebox
import pyautogui
from PIL import Image
from fpdf import FPDF


class MainWindow(tk.Tk):
    """Main window of the App."""

    def __init__(self, x1=0, y1=0, x2=640, y2=480):  # Use sensible defaults
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.image_no = 1001
        self.show_image = False
        self.pages = tk.IntVar()
        self.pages.set(5)
        self.default_params = {
            "width": 20,
            "pady": 5,
            "borderwidth": 3,
            "button_bg": "#DEDEDE",
        }
        self._draw_screen()
        self.IMG_DIR = "img"
        self.auto_hide = True

    def _draw_screen(self):
        """This function is inteded to be called when constructing this class (in __init__).
        \rThis is where all the main widgets are supposed to be packed."""

        self.attributes("-topmost", True)  # Keeps GUI on top
        self.config(padx=20, pady=20)
        # Place a label on the root window
        message = tk.Label(self, text="ScreenGrab")
        message.pack(pady=2)

        # Define the buttons
        capture_button = tk.Button(
            self,
            text="Capture",
            borderwidth=self.default_params["borderwidth"],
            bg=self.default_params["button_bg"],
            width=self.default_params["width"],
            pady=self.default_params["pady"],
            command=self.capture_button_clicked,
        )
        # Pack the button, required.
        capture_button.pack(pady=2)

        get_box_button = tk.Button(
            self,
            text="Get Box",
            borderwidth=self.default_params["borderwidth"],
            bg=self.default_params["button_bg"],
            width=self.default_params["width"],
            pady=self.default_params["pady"],
            command=self.get_box_button_clicked,
        )
        get_box_button.pack(pady=2)

        auto_button = tk.Button(
            self,
            text="Auto mode, down arrow",
            borderwidth=self.default_params["borderwidth"],
            bg=self.default_params["button_bg"],
            width=self.default_params["width"],
            pady=self.default_params["pady"],
            command=self.auto_button_clicked,
        )
        auto_button.pack(pady=2)

        create_pdf_button = tk.Button(
            self,
            text="Create pdf",
            borderwidth=self.default_params["borderwidth"],
            bg=self.default_params["button_bg"],
            width=self.default_params["width"],
            pady=self.default_params["pady"],
            command=self.create_pdf_button_clicked,
        )
        create_pdf_button.pack(pady=2)

        # Text box for number of pages
        pages_entry_box = tk.Entry(
            self,
            justify=tk.CENTER,
            borderwidth=self.default_params["borderwidth"],
            width=self.default_params["width"],
            textvariable=self.pages,
        )
        pages_entry_box.pack(pady=2)

    # This is unused, should we remove it?
    # @property
    # def number(self):
    #     """Top left x is returned as an integer"""
    #     return int(self.box[0])

    @property
    def region(self):
        """Property that returns a region."""
        return (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)

    def get_box_button_clicked(self):
        """This function will capture two points on the screen to create a bounding box.
        \rIt's called when the Get Box button is clicked"""
        messagebox.showinfo(
            title="Attention: TOP LEFT",
            message="Position your mouse and press enter to capture TOP LEFT position.",
            icon="question",  # This specific icon removes the bell noise from the messagebox.
            parent=self,
        )
        # print("Top left position in 5 seconds")
        # time.sleep(5)

        # pyautogui.position() gets the x and y position of the mouse the variable is an object
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

        # update the values in the object
        self.x1, self.y1 = x1y1
        self.x2, self.y2 = x2y2
        print(self.region)
        messagebox.showinfo(
            title="Finished", message=f"Captured area was {self.region}", parent=self
        )

        # print("Captured area")
        # print(pyautogui.position())

    def capture_button_clicked(self):
        """This will capture an screen shot of the bounding box area when called.
        \rIts main use is when the Capture button is clicked."""
        print("Button clicked")
        # Hide GUI while capture takes place only if auto hide is True
        if self.auto_hide:
            self.withdraw()
            # Without the delay we capture a faded area of the GUI 0.2 seems to be the lowest delay
            time.sleep(0.2)
        image = pyautogui.screenshot(region=self.region)
        # Show GUI when capture has taken place
        if self.auto_hide:
            self.deiconify()
        if self.show_image:
            image.show()
        image.save(f"{self.IMG_DIR}/image{self.image_no}.png")
        self.image_no += 1
        print(self.image_no)

    def auto_button_clicked(self):
        """This will "auto click the capture button" (or, rather, call its function) for a
        \rgiven amount of times. That amount is written in the entry box."""
        self.show_image = False
        # This breaks auto capture, the 5 second delay is to allow the user to get focus on the intended app / site
        # to advance through pages e.g. Box.com
        # messagebox.showinfo(
        #    title="Attention",
        #    message="Press enter to start capturing the screen.",
        #    parent=self
        # )
        print("Starting auto capture in 5 seconds")
        self.auto_hide = False
        time.sleep(5)
        for _ in range(self.pages.get()):
            self.capture_button_clicked()
            pyautogui.press("down")
            print(f"Captured image {self.image_no}")

    def create_pdf_button_clicked(self):
        """This function will concatenate all images in the IMG_DIR folder into a PDF."""
        print("Getting list of images from img folder")
        images_list = os.listdir(self.IMG_DIR)
        print(images_list)
        pdf = FPDF(
            "l", "pt", "A4"
        )  # Init pdf l = landscape, pt = points / pixels, A4 default size
        pdf.set_auto_page_break(True)
        pdf.set_margins(0, 0)
        for img in images_list:
            timage = Image.open(f"{self.IMG_DIR}/{img}")
            print(timage.width, timage.height)
            # Below will add a page the same size as the image.
            pdf.add_page(format=(timage.height, timage.width))
            # format keyword gives out an error if using fpdf, fpdf2 is required
            # pip uninstall fpdf, pip install fpdf2
            pdf.image(f"{self.IMG_DIR}/{img}")
        pdf.output("Binder.pdf")
        messagebox.showinfo(
            title="Success", message="Finished creating PDF.", parent=self
        )
