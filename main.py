import PyPDF2

f1 = input("File 1: ")
f2 = input("File 2: ")
files = [f"{f1}.pdf", f"{f2}.pdf"]

merge = PyPDF2.PdfMerger()

for filename in files:
    pdffile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdffile)
    merge.append(pdfReader)
pdffile.close()
merge.write(f"merged_{f1}_{f2}.pdf")