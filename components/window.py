from os import listdir
from tkinter import Tk, Label, Button, filedialog
from PyPDF2 import PdfMerger, PdfReader

class MergeButton:
  def __init__(self, trunk, files):
    self.trunk = trunk
    self.files = files
    self.button = Button(trunk, text="Merge", command=self.merge_files)
    self.merged_file = PdfMerger()
    self.blank_page = PdfReader("../assets/Blank_Page.pdf")
  
  def merge_files(self):
    for file in self.files:
      if len(PdfReader(file).pages) % 2 == 0:
        self.merged_file.append(file)
      else:
        self.merged_file.append(file)
        self.merged_file.append(self.blank_page)
    document = filedialog.asksaveasfile(mode="wb", defaultextension='.pdf')
    self.merged_file.write(document)
    self.merged_file.close()
    success_msg = Label(self.trunk, text="Merged files Successfully")
    success_msg.pack()
  
  def pack(self):
    self.button.pack()

class UploadButton:
  def __init__(self, trunk, com):
    self.button = Button(trunk, text="Upload File", command=self.upload_file)
    self.testrrrr = com
  def upload_file(self):
    file = filedialog.askopenfilename()
    self.testrrrr(file)
  def pack(self):
    self.button.pack()


class GUI:
  def __init__(self, trunk):
    self.trunk = trunk
    trunk.title("Python PDF Merge Tool")
    trunk.geometry("400x400")
    self.files = []
    self.label = Label(trunk, text="Select Files to Merge")
    self.label.pack()
    self.close_button = Button(trunk, text="Close", command=trunk.quit)
    self.close_button.pack()
    self.upload_button = UploadButton(trunk, com=self.com)
    self.upload_button.pack()
    self.merge_button = MergeButton(trunk, self.files)
    self.merge_button.pack()
  def com(self, file):
    self.files.append(file)
    labelItem = Label(self.trunk, text=f"{file}")
    labelItem.pack()

root=Tk()
my_gui = GUI(root)
root.mainloop()