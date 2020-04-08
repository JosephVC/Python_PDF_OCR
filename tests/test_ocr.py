from pathlib import Path
import pytest


from alterpdf import pdf_to_image

# test cases for altering pdfs

# test whether the pdf_to_image module actually works
def test_pdf_to_image():
    pdf_to_image.convert('-p', '../sample_pdfs/meetingminutes.pdf')
    # run something through pdf_to_image and check if it's there

    assert Path('../output_images/output1.jpg').is_file


def test_ocr_image_exists():
    pass

def image_made_to_pdf():
    pass

