# from wand.image import Image
# from PIL import Image as PI
# import pyocr
# import pyocr.builders
# import io

# tool = pyocr.get_available_tools()[0]
# lang = tool.get_available_languages()[1]

# req_image = []
# final_text = []

# image_pdf = Image(filename="../sample_pdfs/meetingminutes.pdf", resolution=300)
# image_jpeg = image_pdf.convert('jpeg')

# for img in image_jpeg.sequence:
#     img_page = Image(image=img)
#     req_image.append(img_page.make_blob('jpeg'))


# for img in req_image: 
#     txt = tool.image_to_string(
#         PI.open(io.BytesIO(img)),
#         lang=lang,
#         builder=pyocr.builders.TextBuilder()
#     )
#     final_text.append(txt)
# print(final_text)

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