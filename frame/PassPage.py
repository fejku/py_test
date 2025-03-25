import tkinter as tk

from frame.CustomFrame import CustomFrame

class PassPage(CustomFrame):
  def __init__(self, parent):    
    super().__init__(parent)  
    label = tk.Label(parent, text="Password Page").pack()