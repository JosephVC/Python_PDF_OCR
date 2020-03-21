# this converts individual pdf pages to images
# which can then be OCR'd

import argparse
from pdf2image import convert_from_path


# construct the arguments

# produce a list of images from the pdf
# specifically, these are PIL image files
images = convert_from_path('[PATH ARGS GO HERE]')

# now we just hop through the above list of images
# save and output with the title 'output[i].jpg', 
# specifying the output format as JPEG

for image in images:
   image.save('output' + str(i) + '.jpg', 'JPEG')
   i +=1
   
