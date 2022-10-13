from os import path
from tkinter import ACTIVE, DISABLED, Listbox, Tk, Label, Button 
from PyPDF2 import PdfMerger, PdfReader
from src.components.buttons.merge_button import MergeButton
from src.components.buttons.upload_button import UploadButton

class AppWindow:
  def __init__(self, trunk):
    self.trunk = trunk
    trunk.title("Python PDF Merge Tool")
    trunk.geometry("400x400")
    self.files = []
    self.label = Label(trunk, text="Select Files to Merge")
    self.label.pack()
    self.list_container = Listbox(trunk)
    self.close_button = Button(trunk, text="Clear", command=self.clear)
    self.upload_button = UploadButton(trunk, cmd=self.add_file_to_files)
    self.upload_button.pack()
    self.merge_button = MergeButton(trunk, self.files)
    self.merge_button.pack()
    self.trunk.mainloop()
  
  def add_file_to_files(self, file):
    if len(self.files) == 0:
      self.close_button.pack()
      self.list_container.pack()
    self.merge_button.button['state'] = ACTIVE
    self.files.append(file)
    self.list_container.insert(len(self.files), f"{path.basename(file)}")
  
  def clear(self):
    for i in reversed(range(len(self.files))):
      self.list_container.delete(i)
    self.list_container.pack_forget()
    self.close_button.pack_forget()
    self.files = []
    self.merge_button.button['state'] = DISABLED
