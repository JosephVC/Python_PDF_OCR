<<<<<<< HEAD
import sys
import os

from pdfrw import PdfReader, PdfWriter

#separate out selected pages
# RUNNING THIS SCRIPT: python subset.py sample_pdfs/meetingminutes.pdf 4-5

# our first argument is the pdf we're looking to extract pages from
inpfn = sys.argv[1]

# our second argument is the range of pages we want
ranges = sys.argv[2:]

# if the user does not enter a range, throw an error asking for a range
assert ranges, "Expected at least one range"

# This defines how you format the range, "x-y"
ranges = ([int(y) for y in x.split('-')] for x in ranges)

# Create the output file prefaced with the term "subset" and then the pdf name
outfn = 'subset.%s' % os.path.basename(inpfn)
pages = PdfReader(inpfn).pages 
outdata = PdfWriter(outfn)

# run through the ranges specified 
# remember to use a-b, x-y, c-d style
# the 
for onerange in ranges:
    onerange = (onerange + onerange[-1:])[:2]
    for pagenum in range(onerange[0], onerange[1]+1):
        # outdata.addpage(pages[pagenum-1])
        # FIXED: output began with one page less than specified
        outdata.addpage(pages[pagenum])
outdata.write()

# TODO: right now output files overwrite each other
=======
import sys
import os

from pdfrw import PdfReader, PdfWriter

#separate out selected pages
# RUNNING THIS SCRIPT: python subset.py sample_pdfs/meetingminutes.pdf 4-5

# our first argument is the pdf we're looking to extract pages from
inpfn = sys.argv[1]

# our second argument is the range of pages we want
ranges = sys.argv[2:]

# if the user does not enter a range, throw an error asking for a range
assert ranges, "Expected at least one range"

# This defines how you format the range, "x-y"
ranges = ([int(y) for y in x.split('-')] for x in ranges)

# Create the output file prefaced with the term "subset" and then the pdf name
outfn = 'subset.%s' % os.path.basename(inpfn)
pages = PdfReader(inpfn).pages 
outdata = PdfWriter(outfn)

# run through the ranges specified 
# remember to use a-b, x-y, c-d style
# the 
for onerange in ranges:
    onerange = (onerange + onerange[-1:])[:2]
    for pagenum in range(onerange[0], onerange[1]+1):
        # outdata.addpage(pages[pagenum-1])
        # FIXED: output began with one page less than specified
        outdata.addpage(pages[pagenum])
outdata.write()

# TODO: right now output files overwrite each other
>>>>>>> f03fb14cd0fe7abcca5da198d212ae9413ecb158
