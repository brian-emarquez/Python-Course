# Python Tktinter Button Mouse on-Hover Popup Message
# PMensaje emergente de desplazamiento del mouse del botón Tktinter de Python

from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('Python Tktinter Button Mouse on-Hover Popup Message')
root.iconbitmap('Python Tktinter Button Mouse on-Hover Popup Message/elvis.ico')
root.geometry("500x400") 


def button_hover(e):
    my_button["bg"] = "white"
    status_label.config(text="I m Hovering Over The Button")

def button_hover_leave(e):
    my_button["bg"] = "SystemButtonFace"
    status_label.config(text="")


my_button = Button(root, text="Click Me", font=("Helvetica", 28))
my_button.pack(pady=50)

status_label = Label(root, text="Test", bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>", button_hover)
my_button.bind("<Leave>", button_hover_leave)


root.mainloop()