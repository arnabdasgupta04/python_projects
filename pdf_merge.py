import PyPDF2
import sys

inputs= sys.argv[1:]
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
     #   print(pdf)
        pdfin = PyPDF2.PdfFileReader(open(pdf, 'rb'), strict=True)
      #  pdf_reader = PyPDF2.PdfFileReader(pdf,strict=False)
        merger.append(pdfin)
    merger.write('Merged_pdf.pdf')
    

    
pdf_combiner(inputs)
print("All the pdf files are merged successfully .")