import tkinter as tk
import keyboard

def hotkey_pressed():
    print("Space was pressed!")

root = tk.Tk()
root.title("Qwe")

keyboard.add_hotkey('ctrl+shift+f1', hotkey_pressed)

root.mainloop()