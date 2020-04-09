# this converts individual pdf pages to images which can then be OCR'd

"""
 RUNNING SCRIPT: python pdf_to_image.py -p [path to whatever pdf you want to 
  make an image
  ]
  the above will create a series of files "output1.jpg", "output2.jpg", etc. in 
  the the "OCRd_images" directory
"""
import argparse
from pdf2image import convert_from_path

# construct the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pdf", required=True, 
    help="path to input pdf to be split into images")
args = vars(ap.parse_args())

def convert(args):
    # produce a list of images from the pdf
    # specifically, these are PIL image files
    images = convert_from_path(args["pdf"])


    # now we just hop through the above list of images
    # save and output with the title 'output[i].jpg', 
    # specifying the output format as JPEG
    i = 1
    for image in images:
        image.save('../output_images/output' + str(i) + '.jpg', 'JPEG')
        i +=1

convert(args)