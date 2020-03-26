# Tesseract OCR project notes

overall plan is to OCR pdfs in place and then port to WebAssembly
- want to have a system that can be accessed anywhere
 -- ideally would be faster than using Adobe Pro

using this on Windows, which is a bit harder/different than unix-based system
- special version of tesseract are needed for Windows
 -- https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows

following on how to use tesseract using a tutorial 
- https://www.youtube.com/watch?v=rSKYTefQv5g&feature=emb_rel_pause

**Basic command to recognize text in a .png image using tesseract:** 

  `tesseract.exe test_data.png .test_data_out.txt -l eng`

**pdfminer.six - https://pdfminersix.readthedocs.io/en/latest/index.html - can be used to extract particular page numbers to text; maybe convert those back to pdf?**

3.26.20 - There seems to be no real way to get around needing to convert a portion of text, whether it's from a pdf or some other format, to an image **first** and then applying OCR to the text in the image.  I got a bit excited and confused thinking I found a way around this.  So, as long as I can 
- split up a multi-page pdf into multiple images, 
- then iterate over those images to OCR them, 
- **then** convert the OCR'd images back into pdf format

I'll be good.



## TASK LIST - OCR project
- [x] install a quality OCR package - tesseract in this case
- [x] get some experience in said package - online tutorials
- [x] create a program that will allow certain sections of pdf to be extracted from a file **-- done with pdfrw --**
- [x] create a way to re-combine the above split portions **-- also done with pdfrw; specifically, you can specify a single page or several ranges of pages to be split off, and then those are automatically combined into one pdf by pdfrw**
- [x] figure out a way to OCR an image via Tesseract/pytesseract
- [x] OCR a pdf in-place (you OCR the pdf itself)
 
## TASK LIST - web site
- [ ]

## Conceptual tasks
- [ ] understand what OCR is
- [ ] what is the OCR engine actually doing
