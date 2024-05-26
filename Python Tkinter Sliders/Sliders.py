# Python Tkinter Sliders

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Tkinter')
root.iconbitmap('Python Tkinter Sliders/icon.ico')
root.geometry("400x400") # tamaño de la ventana

#---------------------funciones---------------------------------------
def slide():
    mylabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) #redimenciona la ventana

#---------------------------------------------------------------------
# barra vertial de 0-200
vertical = Scale(root, from_=0, to=200)
vertical.pack()

# barra horizontal de 0-200
horizontal =  Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

#---------------------------------------------------------------------
mylabel = Label(root, text=horizontal.get()).pack()
mybtn = Button(text="Click Me!", command=slide).pack()

root.mainloop()