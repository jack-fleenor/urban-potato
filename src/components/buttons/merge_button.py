from tkinter import Button, filedialog
from tkinter.constants import DISABLED, NORMAL
from PyPDF2 import PdfMerger, PdfReader
from src.components.message.status_message import StatusMessage


class MergeButton:
  def __init__(self, trunk, files):
    self.trunk = trunk
    self.files = files
    self.button = Button(trunk, text="Merge", command=self.merge_files, state=DISABLED)
    self.merged_file = PdfMerger()
    self.blank_page = PdfReader("src/assets/Blank_Page.pdf")

  def merge_files(self):
    #IF NO FILES PRINT ERROR
    if len(self.files) == 0:
      StatusMessage(self.trunk).display_message("No files to merge.", "MERGE_ERROR")
    else:
      for file in self.files:
        # CHECK IF NEED TO ADD SPACE PAGE
        if len(PdfReader(file).pages) % 2 == 0:
          self.merged_file.append(file)
        else:
          self.merged_file.append(file)
          self.merged_file.append(self.blank_page)
      #ASK USER FOR LOCATION AND NAME FOR MERGED FOLDER
      self.merged_file.write(filedialog.asksaveasfile(mode="wb", defaultextension='.pdf'))
      #CLOSE FILE
      self.merged_file.close()
      #DISPLAY SUCCESS MESSAGE
      StatusMessage(self.trunk).display_message(f"{len(self.files)} files were successfully merged.", "MERGE_SUCCESS")

  def pack(self):
    self.button.pack()