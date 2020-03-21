# this converts individual pdf pages to images
# which can then be OCR'd

import argparse
from pdf2image import convert_from_path


# construct the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pdf", required=True, 
    help="path to input pdf to be split into images")
args = vars(ap.parse_args())


# produce a list of images from the pdf
# specifically, these are PIL image files
images = convert_from_path(args["pdf"])

# now we just hop through the above list of images
# save and output with the title 'output[i].jpg', 
# specifying the output format as JPEG
i = 1
for image in images:
   image.save('output' + str(i) + '.jpg', 'JPEG')
   i +=1
   
