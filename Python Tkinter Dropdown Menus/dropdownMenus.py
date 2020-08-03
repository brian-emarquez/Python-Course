# Python Tkinter Dropdown Menus

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Tkinter')
root.iconbitmap('Python Tkinter Dropdown Menus/icon.ico')
root.geometry("400x400") 

# Drop down Boxes
def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Lunes", 
    "Martes", 
    "Miercoles",
    "Jueves", 
    "Viernes"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()