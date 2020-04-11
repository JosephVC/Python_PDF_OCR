﻿# OCR_project
The overall plan for this project is to OCR pdfs via the web.  

I'll be going step-by-step to make sure a command-line version is stable and usable before porting the application to the web.

Initially, the program will be run via the command-line.  The web portion will be either Django or a JS framework, likely React.

The actual code doing the OCR to be in Python, using Tesseract.    

In addition, there would be the basic functionality of rotating, extracting pages from, and combining multiple individiual pdfs into a single pdf.  

**Stretch goals:** I want to have a system that can be accessed anywhere via the web, and *ideally* would OCR pages faster than using Adobe Pro.  I'm guessing the latter would be pretty hard, though. :)

Maybe, just maybe, I can get this project ported to work in WebAssembly.  Dunno if that would actually help with speed.


 
