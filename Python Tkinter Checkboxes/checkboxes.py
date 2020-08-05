# Python Tkinter Checkboxes

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Checkboxes')
root.iconbitmap('Python Tkinter Checkboxes/icon.ico')
root.geometry("400x400") 
# Funciones
def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root, text="Check this box. I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect() # Seleccion del del checkBoxs
c.pack()

myLabel = Label(root, text=var.get()).pack()
myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()