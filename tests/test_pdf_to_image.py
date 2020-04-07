import pytest
from pathlib import Path

from alterpdf import pdf_to_image

# use pytest.addoption to add necessary arguments
def pytest_addoption(parser):
    parser.addoption("-p", action="store", default="pdf file path")

# test cases for altering pdfs

# test whether the pdf_to_image module actually works
def test_pdf_to_image():
    pdf_to_image.convert()
    # run something through pdf_to_image and c.heck if it's there
    assert Path('../output_images/output1.jpg').is_file

