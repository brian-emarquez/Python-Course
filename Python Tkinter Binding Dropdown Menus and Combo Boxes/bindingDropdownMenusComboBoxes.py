# Python Tkinter Binding Dropdown Menus and Combo Boxes
# Menús desplegables de enlace de Python Tkinter y cuadros combinados

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Binding Dropdown Menus and Combo Boxes!')
root.iconbitmap('Python Tkinter Binding Dropdown Menus and Combo Boxes/reload.ico')
root.geometry("400x400") 


def selected(event):
    myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Friday':
        myLabel = Label(root, text= "Vay! it's Friday").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()

def comboclick(event):
        myLabel = Label(root, text= myCombo.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command = selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

#myButton = Button (root, text= "Select from List", command=selected)
#myButton.pack()

root.mainloop()