import tkinter as tk

from frame.CustomFrame import CustomFrame

class PasswordFrame(CustomFrame):
  def __init__(self, parent):    
    super().__init__(parent)  

    self.bind("1", lambda event: self.onWklej("ASD"))
    
    self.focus_set()

  def onWklej(self, text):
    print("Wklej:", text)