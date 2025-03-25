import tkinter as tk

from frame.CustomFrame import CustomFrame

class WklejFrame(CustomFrame):
  def __init__(self, parent):
    super().__init__(parent)
    label = tk.Label(parent, text="Wklej Page").pack()