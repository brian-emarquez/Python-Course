# Python Tkinter How to Resize a Window Dynamically
# Python Tkinter Cómo cambiar el tamaño de una ventana dinámicamente

from tkinter import *
import time

root = Tk()
root.title('Python Tkinter How to Resize a Window Dynamically')
root.iconbitmap('Python Tkinter How to Resize a Window Dynamically/pineapple.ico')
root.geometry("800x800") 

def resize():
    w= width_label.get()
    h= height_label.get()

    root.geometry(f"{w}x{h}")
    #root.geometry("%ix%i" %(w,h))

width_label = Label(root, text="Widht:")
width_label.pack(pady=20)
width_label = Entry(root)
width_label.pack()

my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)

height_label = Label(root, text="Height:")
height_label.pack(pady=20)
height_label= Entry(root)
height_label.pack()

root.mainloop()