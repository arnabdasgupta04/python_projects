import PyPDF2
import sys
import docx

inputs=sys.argv[1]
pdfFileObj = open(inputs, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
a=int(pdfReader.numPages)
#print(a)


doc = docx.Document()
for x in range(a):
    #print(x)
    pageObj = pdfReader.getPage(int(x))
    p=pageObj.extractText()
    #print(p)
    doc.add_paragraph(p)
    
doc.save('pdftoword.docx')
print("Sucessfully converted the pdf file to word document.")