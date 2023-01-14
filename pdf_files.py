import  PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
#rb == read binary 

pdf_reader = PyPDF2.PdfFileReader(f)

pdf_reader.numPages

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

pdf_writer = PyPDF2.PdfFileWriter()

#To be added: 
if type (page_one) == 'PyPDF2.pdf.PageObject':
    pdf_writer.addPage(page_one)

pdf_output = open ('Un_Documento_Nuevo.pdf', 'wb')

pdf_writer.write(pdf_output)

f.close()
pdf_output.close()