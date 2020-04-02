from pdfrw import PdfReader, PdfWriter

# this will grab a selection of pages out of a pdf
# this goes from the first page up to the given page number
# STRETCH GOAL: HOW TO INPUT SPECIFIC RANGES
def split(path, number_of_pages, output):
    pdf_obj = PdfReader(path)
    total_pages = len(pdf_obj.pages)
    
    writer = PdfWriter()
    
    for page in range(number_of_pages):
        if page <= total_pages:
            writer.addpage(pdf_obj.pages[page])
        
    writer.write(output)
    
if __name__ == '__main__':
    split('sample_pdfs/.pdf', 20, 'subset2.pdf')