# Pyhton Tkinter Message Boxes

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn to Python')
root.iconbitmap('Pyhton Tkinter Create New Windows/icon.ico')

def open():
    global my_img

    top = Toplevel() # abre 2 ventanas
    top.title("My Second Windows")
    top.iconbitmap('Pyhton Tkinter Create New Windows/icon.ico')
    my_img = ImageTk.PhotoImage(Image.open("Pyhton Tkinter Create New Windows/image.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2= Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second windos", command=open).pack()


root.mainloop()
