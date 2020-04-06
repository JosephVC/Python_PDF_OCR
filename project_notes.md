# Tesseract OCR project notes

# BE ABLE TO EXPLAIN EVERY LINE

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

3.27.20 - Need to figure out a way to either 
 - have a single program that does imaging, ocr, and recombination
 - **or have several smaller programs imported into one main script, then run.**


## TASK LIST - OCR project
- [x] install a quality OCR package - tesseract in this case
- [x] get some experience in said package - online tutorials
- [x] create a program that will allow certain sections of pdf to be extracted from a file **-- done with pdfrw --**
- [x] create a way to re-combine the above split portions **-- also done with pdfrw; specifically, you can specify a single page or several ranges of pages to be split off, and then those are automatically combined into one pdf by pdfrw**
- [x] figure out a way to OCR an image via Tesseract/pytesseract
- [ ] create tests
- [ ] alter program in such a way as to 
    -  [ ] iterate through a pdf and generate images of each page = **pdf2image.py**
    - [ ] iterate through those images to OCR them = **ocr_image.py**
    - [ ] recombine those images (in their oritinal order) into a now-OCR'd pdf = **image2pdf.py**
- [ ] now that we have a working OCR program, we can tack on combining, splitting, rotating pdfs to make a fuller-featured application = **[all_this_stuff].py**
 
## TASK LIST - web site
- [ ] I'm wanting to explore React more than Django.

## Conceptual tasks
- [ ] understand what OCR is
- [ ] what is the OCR engine actually doing and how the engine works

## STRETCH GOAL
- [ ] build an app that is faster at OCR'ing a 1000 page pdf of random data faster than Adobe Pro