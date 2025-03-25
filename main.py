import tkinter as tk
# import keyboard
# import pyautogui
# import pystray

from frame.MainFrame import MainFrame

class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.frame = None
    self.switch_frame(MainFrame)

  def switch_frame(self, frame_class):
    if self.frame is not None:
      self.frame.destroy()
    self.frame = frame_class(self)
    self.frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

# class Application(tk.Tk):
#     def __init__(self):

#         self.root = tk.Tk()
#         self.root.title("qwe2")
#         self.root.geometry('600x400')
#         self.icon = pystray.Icon("name", self.create_image(), menu=self.create_menu())
#         self.root.withdraw()
#         self.initHotkey()
#         self.initDesign()

#     def hotkey_pressed(self):
#         print("Space was pressed!")
#         self.root.deiconify()

#     def initHotkey(self):
#         keyboard.add_hotkey('ctrl+shift+f1', self.hotkey_pressed)

#     def initDesign(self):
#         self.button_one = tk.Button(self.root, text="One", bg='purple', fg='white', command=self.onOne)
#         self.button_one.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

#         self.button_two = tk.Button(self.root, text="Two", bg='purple', fg='white', command=self.onOne)
#         self.button_two.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

#         # self.button_one.pack(pady=10)
#         # self.button_two.pack(pady=10)

#         self.root.bind("1", lambda event: print("test"))
#         self.root.bind("2", lambda event: print("test2"))

#     def onOne(self):
#         self.root.withdraw()
#         pyautogui.write("Q1")
#         pyautogui.press("enter")