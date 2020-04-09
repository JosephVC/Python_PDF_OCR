

import pdf2image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[0]

final_text = []
PDF_PATH = "../sample_pdfs/meetingminutes.pdf"
DPI = 300
OUTPUT_FOLDER = "../OCR'd_images"
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False
image_jpeg = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
for img in image_jpeg:
    txt = tool.image_to_string(
        img,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
final_text.append(txt)

print(final_text)