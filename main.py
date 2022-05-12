# Use to grab docs or images from screen one page at a time

import pyscreenshot
import pyautogui
import time
import tkinter as tk
from fpdf import FPDF
import os
from PIL import Image

# Define the App class
class App:
    def __init__(self, x1=0, y1=0, x2=640, y2=480):  # Use sensible defaults
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.image_no = 1001
        self.show_image = False
        self.pages = 486

    def get_number(self):
        return int(self.x1)

    def get_box(self):  # Returns the box dimensions in the correct format
        return self.x1, self.y1, self.x2, self.y2

capture = App(408, 146, 1683, 1037)
print("get box :" + str(capture.get_box()))
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2
print(pyautogui.size())  # Prints screen resolution
# width, height = pyautogui.size()

# Init Tkinter call our GUI root
root = tk.Tk()
root.attributes('-topmost', True) # Keeps GUI on top
# place a label on the root window
message = tk.Label(root, text="ScreeGrab")


# Function is called when the Get Box button is clicked
def get_box_button_clicked():
    print("Top left position in 5 seconds")
    time.sleep(5)
    x1y1 = pyautogui.position()  # This gets the x and y position of the mouse the variable is an object
    print("Capturing bottom right in 5 seconds")
    time.sleep(5)
    x2y2 = pyautogui.position()
    print("Captured area")
    # update the values in the object
    capture.x1 = x1y1.x
    capture.y1 = x1y1.y
    capture.x2 = x2y2.x
    capture.y2 = x2y2.y
    print(capture.get_box())
    # print(pyautogui.position())

# Called when the Capture button is clicked
def capture_button_clicked():
    print('Button clicked')
    image = pyscreenshot.grab(bbox=(capture.get_box()))
    if capture.show_image:
        image.show()
    image.save(f"img/image{capture.image_no}.png")
    capture.image_no += 1
    print(capture.image_no)

def auto_button_clicked():
    capture.show_image = False
    print("Starting auto capture in 5 seconds")
    time.sleep(5)
    for i in range(capture.pages):
        capture_button_clicked()
        pyautogui.press('down')
        print(f"Captured image {capture.image_no}")

def create_pdf_button_clicked():
    print("Getting list of images from img folder")
    images_list = [x for x in os.listdir('img')]
    print(images_list)
    pdf = FPDF('l', 'pt', 'A4') # Init pdf l = landscape, pt = points / pixels, A4 default size
    pdf.set_auto_page_break(0)
    pdf.set_margin(0)
    for img in images_list:
        timage = Image.open(f"img/{img}")
        print(timage.width, timage.height)
        # Below will add a page the same size as the image.
        pdf.add_page(format=(timage.height, timage.width))
        pdf.image(f"img/{img}")
    pdf.output("Binder.pdf")

# Define the buttons
capture_button = tk.Button(root, text='Capture', command=lambda: capture_button_clicked())
# Pack the button, required.
capture_button.pack()
get_box_button = tk.Button(root, text='Get Box', command=lambda: get_box_button_clicked())
get_box_button.pack()
auto_button = tk.Button(root, text='Auto mode, down arrow', command=lambda : auto_button_clicked())
auto_button.pack()
create_pdf_button = tk.Button(root, text='Create pdf', command=lambda : create_pdf_button_clicked())
create_pdf_button.pack()
message.pack()

# Start the GUI
root.mainloop()

