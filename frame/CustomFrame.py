import tkinter as tk

class CustomFrame(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.parent = parent