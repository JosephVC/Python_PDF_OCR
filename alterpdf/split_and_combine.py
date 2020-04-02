"""
This is a program that will split pdf pages out of their original source and
allow for those pages to be re-combined into a new pdf.

The program will take several arguments:
  - the pdf you wish to extract pages from
  - the range of pages to pull out, whether that is a single page or multiple 
    pages
  - The program does *not* delete the range of pages, only copies them
  - 

"""
import os
from pdfrw import PdfReader, PdfWriter
import sys

#separate out selected pages
# RUNNING THIS SCRIPT python subset.py sample_pdfs/meetingminutes.pdf 4-5 

inpfn = sys.argv[1]
ranges = sys.argv[2:]
assert ranges, "Expected at least one range"

# This defines how you format the range, "x-y"
ranges = ([int(y) for y in x.split('-')] for x in ranges)

# Create the output file prefaced with the term "subset" and then the pdf name
outfn = 'subset.%s' % os.path.basename(inpfn)


pages = PdfReader(inpfn).pages 
outdata = PdfWriter(outfn)

for onerange in ranges:
    onerange = (onerange + onerange[-1:])[:2]
    for pagenum in range(onerange[0], onerange[1]+1):
        outdata.addpage(pages[pagenum-1])
outdata.write()

# combine the pages
import glob 
from PyPDF2 import PdfFileWriter, PdfFileReader 

def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    paths = glob.glob('sample_pdfs/*h.pdf')
    # retrieve all pdfs that start with h
    paths.sort()
    merger('pdf_merger.pdf', paths)


