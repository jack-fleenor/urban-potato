from tkinter import Tk
from src.components.window.main_window import AppWindow

class main():
  def __init__(self):
    self.root = Tk()
    self.window = AppWindow(self.root)

if __name__ == "__main__":
  print("Starting application...")
  main()