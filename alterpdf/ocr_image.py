# Using Tesseract OCR with Python
# TO RUN THE CODE: python ocr_image.py --image [path to whatever images you have to OCR]

# TODO: make sure you can actually convert an OCR'd image to an OCR'd pdf

# import the  necessary packages
from PIL import Image
import pytesseract
import argparse
from cv2 import cv2
import os


# construct the argument parser 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
    help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
    help="type of preprocessing to be done")
args = vars(ap.parse_args())


# load the example image and convert it to grayscale
def ocr():
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove noise
    elif args["preprocess"] == "blur":
        gray == cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a file, OCR it, then save it the
    #  "OCR'd images" directory so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    output_folder = "/OCR'd_images"
    text = pytesseract.image_to_string(Image.open(filename))
    cv2.imsave(output_folder, filename, image)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temp file
    # text = pytesseract.image_to_string(Image.open(filename))
    # os.remove(filename)
    # print(text)

    # show the output images
    # these need to be saved to a file rather than just output to the stdout

    
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)