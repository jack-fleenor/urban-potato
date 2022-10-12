import tkinter as tk
from PyPDF2 import PdfMerger, PdfReader
from os import listdir

class merge_window:
  def __init__(self):
    self.window = tk.Tk()
    self.window.geometry = self.window.geometry("400x400")
    self.window.title = self.window.title("Merge Documents")
    self.uploaded_files = []
    self.merged_file = PdfMerger()
    self.blank_page = "../assets/Blank_Page.pdf"
  
  def upload_file(self, filename):
    self.uploadedFiles.append(filename)
  
  def merge_files(self):
    for file in self.uploadedFiles:
      length = len(PdfReader(file).pages)
      if length % 2 == 0:
        self.merged_file.append(file)
      else:
        self.merged_file.append(file)
        self.merged_file.append(self.blank_page)
      