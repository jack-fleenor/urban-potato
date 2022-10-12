from tkinter import Button, filedialog

class UploadButton:
  def __init__(self, trunk, cmd):
    self.button = Button(trunk, text="Upload File", command=self.upload_file)
    self.add_file_to_files = cmd
  def upload_file(self):
    file = filedialog.askopenfilename()
    self.add_file_to_files(file)
  def pack(self):
    self.button.pack()