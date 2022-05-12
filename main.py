#Use to grab docs from websites

import pyscreenshot
import pyautogui
import random
import time
import tkinter as tk

#Define the App class
class App:
    def __init__(self, x1 = 0, y1 = 0, x2 = 640, y2 = 480): # Use sensible defaults
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.image_no = 1001
        self.show_image = False

    def get_number(self):
        return int(self.x1)

    def get_box(self): # Returns the box dimensions in the correct format
        return (self.x1, self.y1, self.x2, self.y2)

    #def __repr__(self):
    #   return self.image_no


capture = App(432, 240, 1989, 1334)
#capture = App()
print(capture.get_number())
print("get box :" + str(capture.get_box()))

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2
print(pyautogui.size()) #Prints screen resolution
#width, height = pyautogui.size()
root = tk.Tk()
root.attributes('-topmost',True)
#place a label on the root window
message = tk.Label(root, text="Screencap")

#Function is called when the Get Box button is clicked
def get_box_button_clicked():
    print("Top left position in 5 seconds")
    time.sleep(5)
    x1y1 = pyautogui.position() # This gets the x and y position of the mouse the variable is an object
    print("Capturing bottom right in 5 seconds")
    time.sleep(5)
    x2y2 = pyautogui.position()
    capture.x1 = x1y1.x
    capture.y1 = x1y1.y
    capture.x2 = x2y2.x
    capture.y2 = x2y2.y
    #print(pyautogui.position())

#Called when the Capture button is clicked
def button_clicked():
    print('Button clicked')
    image = pyscreenshot.grab(bbox=(capture.get_box()))
    if capture.show_image:
        image.show()
    image.save(f"image{capture.image_no}.png")
    capture.image_no += 1
    print(capture.image_no)


button = tk.Button(root, text='Capture', command=lambda: button_clicked())
button.pack()
get_box_button = tk.Button(root, text='Get Box', command=lambda: get_box_button_clicked())
get_box_button.pack()
message.pack()
root.mainloop()



# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))

# To view the screenshot
#image.show()

#image.save("image.png")