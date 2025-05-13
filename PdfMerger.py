from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
pdf_directory = "C:/Amogh/Python/PdfMerger"

files = [file for file in os.listdir(pdf_directory) if file.endswith(".pdf")]

print(files)
for pdf in files:
    filepath=pdf_directory+"/"+pdf
    merger.append(filepath)

merger.write(f"{pdf_directory}/merged-pdf.pdf")
merger.close()