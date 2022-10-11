from PyPDF2 import PdfMerger, PdfReader
from os import listdir
import tkinter as tk

# root = tk.Tk()
# root.geometry('300x300')
# root.resizable(False, False)
# root.title('An Example of a Window in Tkinter')
# message = tk.Label(root, text="hello world")

# merger = PdfMerger()
# documents = listdir("./documents")
# print(f"Starting to create merged documents from: {documents}")

# class PDF:
#   def __init__(self, file):
#     self.raw = file
#     self.reader = PdfReader(file)
#   def pageNumers(self):
#     length = len(self.reader.pages)
#     return length

# for file in documents:
#   file_path = f"./documents/{file}"
#   pdf = PDF(file_path)
#   print(f"adding {file_path} to document")
#   if not pdf.pageNumers() % 2:
#     print(f"{file_path} has length {pdf.pageNumers()}")
#     merger.append(pdf.raw)
#   else:
#     print(f"{file_path} has length {pdf.pageNumers()} and has added a blank page to behind")
#     merger.append(pdf.raw)
#     merger.append("./assets/Blank_Page.pdf")
#   print(f"{file_path} added to document successfully")

# merger.write("merged-pdf.pdf")
# merger.close()

# print("Document created successfully")

# root.mainloop()

class main():
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("Merge Documents")
    self.window.geometry("300x300")
    self.uploadedFiles = []
    self.mergedFile = PdfMerger()
    self.blank_page = PdfReader("./assets/Blank_Page.pdf")

  def uploadFiles(self, filename):
    self.uploadedFiles.append(filename)
    print(f"Uploaded file {filename} to list {self.uploadedFiles}")

  def mergeDocuments(self):
    for file in self.uploadedFiles:
      length = len(PdfReader(file).pages)
      if length % 2 == 0:
        self.mergedFile.append(file)
      else:
        self.mergedFile.append(file)
        self.mergedFile.append(self.blank_page)
  
  def startWindow(self):
    self.window.mainloop()

if __name__ == "__main__":
  print("Starting application...")
  main().startWindow()