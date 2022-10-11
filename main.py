from PyPDF2 import PdfMerger, PdfReader
from os import listdir

merger = PdfMerger()
documents = listdir("./documents")
print(f"Starting to create merged documents from: {documents}")

class PDF:
  def __init__(self, file):
    self.raw = file
    self.reader = PdfReader(file)
  def pageNumers(self):
    length = len(self.reader.pages)
    return length


for file in documents:
  file_path = f"./documents/{file}"
  pdf = PDF(file_path)
  print(f"adding {file_path} to document")
  if not pdf.pageNumers() % 2:
    print(f"{file_path} has length {pdf.pageNumers()}")
    merger.append(pdf.raw)
  else:
    print(f"{file_path} has length {pdf.pageNumers()} and has added a blank page to behind")
    merger.append(pdf.raw)
    merger.append("./assets/Blank_Page.pdf")
  print(f"{file_path} added to document successfully")

merger.write("merged-pdf.pdf")
merger.close()

print("Document created successfully")