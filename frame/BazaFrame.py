import tkinter as tk

from frame.CustomFrame import CustomFrame

class BazaFrame(CustomFrame):
  def __init__(self, parent):
    super().__init__(parent)
    label = tk.Label(parent, text="Baza Page").pack()