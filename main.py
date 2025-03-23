import tkinter as tk
import keyboard
import pyautogui

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("qwe2")
        self.root.geometry('600x400')
        self.root.withdraw()
        self.initHotkey()
        self.initDesign()

    def hotkey_pressed(self):
        print("Space was pressed!")
        self.root.deiconify()

    def initHotkey(self):
        keyboard.add_hotkey('ctrl+shift+f1', self.hotkey_pressed)
        
    def initDesign(self):
        self.button_one = tk.Button(self.root, text="One", bg='purple', fg='white', command=self.onOne)
        self.button_one.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.button_two = tk.Button(self.root, text="Two", bg='purple', fg='white', command=self.onOne)
        self.button_two.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # self.button_one.pack(pady=10)
        # self.button_two.pack(pady=10)

        self.root.bind("1", lambda event: print("test"))
        self.root.bind("2", lambda event: print("test2"))

    def onOne(self):
        self.root.withdraw()
        pyautogui.write("Q1")
        pyautogui.press("enter")
        
if __name__ == "__main__":
    app = Application()
    app.root.mainloop()