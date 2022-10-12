from tkinter import  Label 

class StatusMessage:
  def __init__(self, trunk):
    self.trunk = trunk
  def display_message(self, message, status):
    label = Label(self.trunk, text=f"{status}: {message}")
    label.pack()