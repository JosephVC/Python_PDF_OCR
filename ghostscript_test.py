import ghostscript
import locale

def pdf2jpeg(pdf_input_path, jpeg_output_path):
    args = ["pef2jpeg", # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r144",
            "-sOutputFile=" + jpeg_output_path,
            pdf_input_path]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]

    with ghostscript.Ghostscript(*args) as g:
        ghostscript.cleanup()

pdf2jpeg(
    "/sample_pdfs/a.pdf",
    "/sample_pdfs/a.jpeg",
)