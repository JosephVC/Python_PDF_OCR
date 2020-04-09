from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[1]

req_image = []
final_text = []

