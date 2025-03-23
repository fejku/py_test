import tkinter as tk
import keyboard

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("qwe2")

        self.initHotkey()

        self.initDesign()

    def hotkey_pressed(self):
        print("Space was pressed!")

    def initHotkey(self):
        keyboard.add_hotkey('ctrl+shift+f1', self.hotkey_pressed)
        
    def initDesign(self):
        self.button_one = tk.Button(self.root, text="One", command=self.onOne)
        self.button_one.pack()

    def onOne(self):
        self.root.withdraw()
        
if __name__ == "__main__":
    app = Application()
    app.root.mainloop()