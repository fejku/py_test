import tkinter as tk

from frame.CustomFrame import CustomFrame
from frame.BazaFrame import BazaFrame
from frame.WklejFrame import WklejFrame
from frame.PasswordFrame import PasswordFrame

class MainFrame(CustomFrame):
  def __init__(self, parent):
    super().__init__(parent)

    tk.Button(self, text="1. Baza", command=self.onBaza).pack()
    tk.Button(self, text="2. Wklej", command=self.onWklej).pack()

    self.bind("1", lambda event: self.onBaza())
    self.bind("2", lambda event: self.onWklej())
    self.bind("`", lambda event: self.onPass())

    self.focus_set()
    
  def onBaza(self):
    self.parent.switch_frame(BazaFrame)

  def onWklej(self):
    self.parent.switch_frame(WklejFrame)

  def onPass(self):
    self.parent.switch_frame(PasswordFrame)
    print("Password Page")