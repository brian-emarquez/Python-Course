# Python Tkinter Create New Window
# Python Tkinter Crear nueva ventana

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Python Tkinter Create New Windows')
root.iconbitmap('Python Tkinter Create New Windows/icon.ico')

def open():
    global my_img

    top = Toplevel() # abre 2 ventanas
    top.title("My Second Windows")
    top.iconbitmap('Python Tkinter Create New Windows/icon.ico')
    my_img = ImageTk.PhotoImage(Image.open("Python Tkinter Create New Windows/image.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2= Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second windos", command=open).pack()


root.mainloop()
