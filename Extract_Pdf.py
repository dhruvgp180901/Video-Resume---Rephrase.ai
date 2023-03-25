import PyPDF2

def get_content(filename):

    pdfFileObj = open(filename, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    pageObj = pdfReader.pages[0]

    pdfFileObj.close()
    print("Extracted Resume!!")
    return pageObj.extract_text()
