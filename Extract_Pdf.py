import PyPDF2

def get_content(filename):

    pdfFileObj = open(filename, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    pageObj = pdfReader.pages[0]
    
    print("Extracted Resume!!")
    resume_text = pageObj.extract_text()

    pdfFileObj.close()

    return resume_text
