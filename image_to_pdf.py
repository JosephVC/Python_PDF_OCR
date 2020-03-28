"""
This portion of the toolchain will take the OCR's images and recombine them
- in order - to  make a pdf that is now OCR'd
"""

# import os 
from pdfrw import PdfWriter
y = PdfWriter()
y.addpage(x.pages[0])
y.write('result.pdf')