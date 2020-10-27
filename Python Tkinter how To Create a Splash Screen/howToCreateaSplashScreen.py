#  Python Tkinter how To Create a Splash Screen
#  Python Tkinter cómo crear una pantalla de bienvenida

from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen!!")
splash_root.geometry("300x200+-50+250")
# Hoide the itle bar
splash_root.overrideredirect(True)

spash_label = Label(splash_root, text="Splash Screen", font=("Helvetica", 18))
spash_label.pack(pady=20)

def main_window():
    splash_root.destroy()

    root = Tk()
    root.title("Python tkinter How to Disable or Delete a Menu item")
    root.iconbitmap("Python Tkinter how To Create a Splash Screen/icons/cat.ico")
    root.geometry("300x200+-50+250")

    main_label = Label(root, text="Splash Screen", font=("Helvetica", 18))
    main_label.pack(pady=20)

# Spash Screnn Timer
splash_root.after(1500, main_window)


mainloop()