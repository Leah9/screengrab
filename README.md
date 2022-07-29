# Screen Grab [![Windows Tests](https://github.com/ArielMAJ/screengrab/actions/workflows/windows-tests.yml/badge.svg)](https://github.com/ArielMAJ/screengrab/actions/workflows/windows-tests.yml)

## Important notes
FPDF2 is required in order to create a pdf with the correct dimensions.
To remove the older version if present run : pip uninstall fpdf
To install the new version pip install fpdf2

Required libraries
* FPDF2
* pyautogui
* tkinter

# Testing functionality
## Please carry out the following to check the main functionality of the code.
* The app needs to be able to capture a user selected area of the screen.
* It needs to process all images into a pdf
* Navigate here https://app.box.com/s/xtt0vzw90ocmhajgtp2sxo387kqy5ibn and use auto mode to capture the 3 pages and combine in to a pdf.
* The above is easier in Edge full screen mode F11, zoom in / out to fit the page to the screen.


## Intended Purpose
To grab a user defined area of the screen repeatedly and save images for later processing.
This has been expanded to create a pdf from the captured images.

## Why Do I Need This
Documentation on some websites is not accessible for my needs and in some cases not possible to download in an accessible format or at all!
I also prefer a record or point in time copy of materials in a format suitable for offline use in the future.

## Why Not Use Snip
It is possible to use snip but I need to extract documents with hundreds of pages, snip is too slow and I need more control over the captured area and repeatability.
This application now also saves the files as a multi-page pdf.

## OCR ?
I have looked at doing this and the current conclusion is that it is too complex to add to this project.
The generated pdf can be OCR'd using the following :
ocrmypdf https://ocrmypdf.readthedocs.io/en/latest/index.html
It is not a casual installation but it is very quick once it is working especially on a multi-core machine.

## Compatibility
* Windows, works and is the primary development platform.
* Linux / Ubuntu, testing in progress. Currently working with some small issues.
 sudo apt install python3-pip
 pip install pyautogui
 sudo apt-get install python3-tk python3-dev
 pip install fpdf2

* Mac, developers / testers needed.
