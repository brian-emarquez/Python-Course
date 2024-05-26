# Python Tkinter Color Picker
# Selector de color de Python Tkinter

from tkinter import *
from tkinter import colorchooser


root = Tk()
root.title('Python Tkinter Color Picker!')
root.geometry("400x400")
root.iconbitmap('Python Tkinter Color Picker/avatar.ico')

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label = Label(root, text="Ypu Picked a Color!", font=("Helvetica", 32), bg=my_color).pack()

my_button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()