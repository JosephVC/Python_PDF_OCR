"""
This portion of the toolchain will take the OCR's images and recombine them
- in order - to  make a pdf that is now OCR'd
"""

import img2pdf
from PIL import Image
import os

# store image and pdf path
# TODO: update this to take arguments rather than hard-coded paths
# TODO: update to iterate through a directory of OCR'd images
img_path = "../OCR'd_images/output1.jpg"
pdf_path = "../OCRd_pdfs/output1.pdf"

# open image
image = Image.open(img_path)

#converting into chunks of bytes 
pdf_bytes = img2pdf.convert(image.filename)

#opening or creating pdf file
file = open(pdf_path, "wb")

file.write(pdf_bytes)

# close the image and pdf file
image.close()
file.close()

# output to signal success
print("Image -> pdf conversion successful")

