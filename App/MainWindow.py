import tkinter as tk
# import pyscreenshot
import time
from fpdf import FPDF
import os
from PIL import Image
import pyautogui
from Globals import IMG_DIR


# import Globals

# Define the App class
class MainWindow(tk.Tk):
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
        self.default_width = 20
        self.default_pady = 5
        self.default_border_width = 3
        self.default_button_bg = "#DEDEDE"
        self.draw_screen()
        # self.region = self.x1, self.y1, self.x2-self.x1, self.y2-self.y1

    def draw_screen(self):
        self.attributes('-topmost', True)  # Keeps GUI on top
        self.config(padx=20, pady=20)
        # place a label on the root window
        message = tk.Label(self, text="ScreenGrab")

        # Define the buttons
        capture_button = tk.Button(self, text='Capture', borderwidth=self.default_border_width,
                                   bg=self.default_button_bg, width=self.default_width, pady=self.default_pady,
                                   command=lambda: self.capture_button_clicked())
        # Pack the button, required.
        capture_button.pack(pady=2)
        get_box_button = tk.Button(self, text='Get Box', borderwidth=self.default_border_width,
                                   bg=self.default_button_bg, width=self.default_width, pady=self.default_pady,
                                   command=lambda: self.get_box_button_clicked())
        get_box_button.pack(pady=2)
        auto_button = tk.Button(self, text='Auto mode, down arrow', borderwidth=self.default_border_width,
                                bg=self.default_button_bg, width=self.default_width, pady=self.default_pady,
                                command=lambda: self.auto_button_clicked())
        auto_button.pack(pady=2)
        create_pdf_button = tk.Button(self, text='Create pdf', borderwidth=self.default_border_width,
                                      bg=self.default_button_bg, width=self.default_width, pady=self.default_pady,
                                      command=lambda: self.create_pdf_button_clicked())
        create_pdf_button.pack(pady=2)
        message.pack(pady=2)

        # Text box for number of pages
        pages_entry_box = tk.Entry(self, justify=tk.CENTER, borderwidth=self.default_border_width,
                                   width=self.default_width, textvariable=self.pages)
        pages_entry_box.pack(pady=2)

    @property
    def number(self):
        return int(self.x1)

    # @property
    # def box(self):  # Returns the box dimensions in the correct format
    # return self.x1, self.y1, self.x2, self.y2

    @property
    def region(self):
        return self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1

    # Function is called when the Get Box button is clicked
    def get_box_button_clicked(self):
        print("Top left position in 5 seconds")
        time.sleep(5)
        x1y1 = pyautogui.position()  # This gets the x and y position of the mouse the variable is an object
        print("Capturing bottom right in 5 seconds")
        time.sleep(5)
        x2y2 = pyautogui.position()
        print("Captured area")
        # update the values in the object
        self.x1 = x1y1.x
        self.y1 = x1y1.y
        self.x2 = x2y2.x
        self.y2 = x2y2.y
        # print(self.box)
        # print(pyautogui.position())

    # Called when the Capture button is clicked
    def capture_button_clicked(self):
        print('Button clicked')
        image = pyautogui.screenshot(region=self.region)
        # image = pyscreenshot.grab(bbox=(self.box))
        if self.show_image:
            image.show()
        image.save(f"{IMG_DIR}/image{self.image_no}.png")
        self.image_no += 1
        print(self.image_no)

    def auto_button_clicked(self):
        self.show_image = False
        print("Starting auto capture in 5 seconds")
        time.sleep(5)
        for i in range(self.pages.get()):
            self.capture_button_clicked()
            pyautogui.press('down')
            print(f"Captured image {self.image_no}")

    def create_pdf_button_clicked(self):
        print("Getting list of images from img folder")
        images_list = [x for x in os.listdir(IMG_DIR)]
        print(images_list)
        pdf = FPDF('l', 'pt', 'A4')  # Init pdf l = landscape, pt = points / pixels, A4 default size
        pdf.set_auto_page_break(True)
        pdf.set_margins(0, 0)
        for img in images_list:
            timage = Image.open(f"{IMG_DIR}/{img}")
            print(timage.width, timage.height)
            # Below will add a page the same size as the image.
            pdf.add_page(format=(timage.height, timage.width))
            # format=(timage.height, timage.width)) # format keyword gives out an error if using fpdf, fpdf2 is required
            # pip uninstall fpdf, pip install fpdf2
            pdf.image(f"{IMG_DIR}/{img}")
        pdf.output("Binder.pdf")
